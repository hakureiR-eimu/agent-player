"""入口与装配（声明见 docs/prd/harness.md 主体实现）。

进程从这起：读总配置 → 建事件总线 → 建三大模块 → 装配接线（挂 IM 回调、起年度节拍）→
事件主循环 → 收摊退出。三大模块的实现在各自包里：src/game/、src/agent/、src/im/，实现进各包 impl/。
"""

from __future__ import annotations

import asyncio
import contextlib
import logging
from datetime import datetime
from pathlib import Path

from agent.impl.module import AgentModuleImpl
from agent.module import AgentModule
from agent.tools import SessionAuth, SessionTools
from config import Config, load_config
from dispatcher import Dispatcher
from events import Event, EventBus, EventType
from game.impl.module import GameModuleImpl
from game.module import GameModule
from im.impl.module import ImModuleImpl
from im.module import ImModule

logger = logging.getLogger(__name__)

# 年度节拍：一年才触发一次、mod 记录攒批落盘、error.log 混有引擎自己的行，精确即时
# 没有意义，解析确认才是准的——间隔几秒就够
NEW_YEAR_POLL_INTERVAL_SECONDS = 3.0

# profile 模板源：开发文件夹下的 profile/（开始游戏时装进全新的 gbr）
PROFILE_SRC = Path(__file__).resolve().parents[1] / "profile"


async def poll_new_year(bus: EventBus, game: GameModule) -> None:
    """年度通知的节拍：定时调游戏接入的新年判定，查到新年份往事件队列推 new_year（data 为年份数字）。"""
    while True:
        await asyncio.sleep(NEW_YEAR_POLL_INTERVAL_SECONDS)
        try:
            year = game.check_new_year()
        except Exception:
            logger.exception("新年判定出错，等下一轮")
            continue
        if year is not None:
            bus.put(Event(EventType.NEW_YEAR, year))
            logger.info("游戏进入 %s 年，推 new_year 事件", year)


def build_session_tools(game: GameModule, im: ImModule) -> SessionTools:
    """会话工具（主体是组合层）：把游戏接入的方法（get_state/start_play）与 IM 接入的
    收发（send_message/read_message，带玩家参数、agent 调用时自己填——值从收到的私信里
    学）组合成 SessionTools 递给 agent 模块。挂进会话的 SDK 细节在 agent/impl/session.py。
    """
    return SessionTools(
        get_state=game.get_state,
        start_play=game.start_play,
        send_message=im.send_message,
        read_message=im.read_message,
    )


def build_modules(config: Config) -> tuple[GameModule, AgentModule, ImModule]:
    """装配第一步：按配置把三大模块建出来。

    - 游戏接入：GameModuleImpl（src/game/impl/），吃总配置的 error.log 路径与游戏进程名
    - agent：AgentModuleImpl（src/agent/impl/），吃 gbr 路径、agent 日志目录（本局运行
      记录所在）、会话工具、profile 模板源与会话的模型凭证（SessionAuth，总配置三项——
      配了 agent 会话走它，与玩家自己的 Claude Code 分开）
    - IM 接入：ImModuleImpl（src/im/impl/），吃总配置的两个 Discord bot token
    """
    game: GameModule = GameModuleImpl(config)
    im: ImModule = ImModuleImpl(config)
    agent: AgentModule = AgentModuleImpl(
        config.gbr_dir,
        config.agent_log_dir,
        build_session_tools(game, im),
        PROFILE_SRC,
        SessionAuth(
            base_url=config.anthropic_base_url,
            auth_token=config.anthropic_auth_token,
            model=config.agent_model,
        ),
    )
    return game, agent, im


def wire_im(bus: EventBus, im: ImModule) -> None:
    """装配处的 IM 接线：收经回调交进来（闭包在装配处把事件包进队列——模块零总线知识），
    message 带玩家（Discord 用户 ID 字符串）与正文。发与读由主体包成 agent 的会话工具
    （build_session_tools），不经总线。
    """
    im.on_command(lambda command: bus.put(Event(EventType.COMMAND, command)))

    def put_message(player: str, text: str) -> None:
        bus.put(Event(EventType.MESSAGE, {"player": player, "text": text}))

    im.on_message(put_message)


def setup_logging(system_log_dir: Path) -> Path:
    """系统日志双写：本次进程启动在 system 目录建一个新文件（名字带启动时刻），控制台
    同步输出。全库各模块的 logger 都汇到这（格式沿用既往）。返回日志文件路径。
    """
    system_log_dir.mkdir(parents=True, exist_ok=True)
    log_path = system_log_dir / f"harness-{datetime.now():%Y-%m-%d_%H-%M-%S}.log"
    fmt = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(fmt)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(fmt)
    logging.basicConfig(level=logging.INFO, handlers=[file_handler, console_handler])
    return log_path


async def run(config: Config) -> None:
    bus = EventBus()
    game, agent, im = build_modules(config)
    dispatcher = Dispatcher(bus, game, agent, im, config.gbr_dir)
    wire_im(bus, im)
    # 年度节拍：主体定时调游戏接入的新年判定，模块自己不碰总线
    year_poll = asyncio.create_task(poll_new_year(bus, game))
    await agent.start(bus)
    await im.start()
    logger.info("模块起齐：agent 接上总线，IM 接入上线（两个 bot 登录完成）")
    try:
        await bus.run()
    finally:
        # 进程收摊：先停年度节拍，会话还在跑再按保存游戏收尾，最后按装配的反序让模块停
        logger.info("进程收摊：停年度节拍，会话按保存游戏收尾，模块按装配反序停")
        year_poll.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await year_poll
        await dispatcher.shutdown()
        await im.stop()
        await agent.stop()
        logger.info("模块全停，进程退出")


def main() -> None:
    config = load_config()
    log_path = setup_logging(config.system_log_dir)
    logger.info("harness 启动，本次运行日志：%s", log_path)
    try:
        asyncio.run(run(config))
    except KeyboardInterrupt:
        logger.info("收到 Ctrl+C，进程退出")


if __name__ == "__main__":
    main()
