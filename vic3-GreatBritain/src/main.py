"""入口与装配（声明见 docs/prd/harness.md 主体实现）。

进程从这起：读总配置 → 建事件总线 → 建三大模块 → 装配接线（挂 IM 回调、起年度节拍）→
事件主循环 → 收摊退出。三大模块的实现在各自包里：src/game/、src/agent/、src/im/，实现进各包 impl/。
"""

from __future__ import annotations

import asyncio
import contextlib
import logging

from agent.module import AgentModule
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


def build_session_tools(game: GameModule):
    """会话工具（主体是翻译层）：把游戏接入的方法包成 agent 会话的工具——agent 调
    get_state/start_play 工具时，翻译成对 game.get_state()/start_play() 的实际调用。
    经 SDK 的进程内 MCP 实现，随 agent 模块落地。
    """
    raise NotImplementedError("会话工具随 agent 模块落地：主体把 game 的方法包成会话工具")


def build_modules(config: Config) -> tuple[GameModule, AgentModule | None, ImModule]:
    """装配第一步：按配置把三大模块建出来。游戏接入与 IM 接入已落地，agent 待建（返回
    None，进程照跑：起会话的命令执行时回执会明确报未实现）：

    - 游戏接入：GameModuleImpl（src/game/impl/），吃总配置的 error.log 路径与游戏进程名
    - agent：src/agent/impl/ 实现后在此实例化（构造时吃主体建的会话工具，起会话挂上）
    - IM 接入：ImModuleImpl（src/im/impl/），吃总配置的两个 Discord bot token
    """
    game: GameModule = GameModuleImpl(config)
    agent: AgentModule | None = None  # 待建：src/agent/impl/
    im: ImModule = ImModuleImpl(config)
    return game, agent, im


def wire_im(bus: EventBus, im: ImModule) -> None:
    """装配处的 IM 接线：收经回调交进来（闭包在装配处把事件包进队列——模块零总线知识），
    reply 事件接到发送方法上。message 带玩家（Discord 用户 ID 字符串）与正文，reply 同。
    """
    im.on_command(lambda command: bus.put(Event(EventType.COMMAND, command)))

    def put_message(player: str, text: str) -> None:
        bus.put(Event(EventType.MESSAGE, {"player": player, "text": text}))

    im.on_message(put_message)

    async def send_reply(event: Event) -> None:
        await im.send_reply(event.data["player"], event.data["text"])

    bus.subscribe(EventType.REPLY, send_reply)


async def run() -> None:
    config = load_config()
    bus = EventBus()
    game, agent, im = build_modules(config)
    dispatcher = Dispatcher(bus, game, agent, im, config.gbr_dir)
    wire_im(bus, im)
    # 年度节拍：主体定时调游戏接入的新年判定，模块自己不碰总线
    year_poll = asyncio.create_task(poll_new_year(bus, game))
    if agent is not None:
        await agent.start(bus)
    await im.start()
    try:
        await bus.run()
    finally:
        # 进程收摊：先停年度节拍，会话还在跑再按保存游戏收尾，最后按装配的反序让模块停
        year_poll.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await year_poll
        await dispatcher.shutdown()
        await im.stop()
        if agent is not None:
            await agent.stop()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        logger.info("收到 Ctrl+C，进程退出")


if __name__ == "__main__":
    main()
