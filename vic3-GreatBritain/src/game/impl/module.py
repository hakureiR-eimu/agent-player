"""游戏接入模块本体（声明见 docs/prd/harness.md 游戏接入节，实现语义见 docs/prd/游戏接入-harness侧.md）。

跑在 harness 进程内：get_state/start_play 两个方法给 agent 调（经 SDK 的进程内 MCP
注册进会话，随 agent 模块实现落）；start 起 error.log 轮询，察觉新年份的本局记录就往
事件队列推 new_year 事件（data 为年份数字）。两个方法与年度通知都以游戏在跑为前提。
"""

from __future__ import annotations

import asyncio
import logging
from pathlib import Path

from config import Config
from events import Event, EventBus, EventType
from game.impl.parser import build_snapshot, parse_record
from game.impl.process import game_running

logger = logging.getLogger(__name__)

# 轮询间隔：一年才触发一次、mod 记录攒批落盘、error.log 混有引擎自己的行，精确即时
# 没有意义，解析确认才是准的——间隔几秒就够（单测传小间隔）
POLL_INTERVAL_SECONDS = 3.0


class GameNotRunningError(RuntimeError):
    """游戏没启动就调方法：不读日志、不发通知。"""


class GameModuleImpl:
    """GameModule 协议（src/game/module.py）的实现。"""

    def __init__(self, config: Config, poll_interval: float = POLL_INTERVAL_SECONDS) -> None:
        self._log_path = config.log_path
        self._game_process = config.game_process
        self._poll_interval = poll_interval
        self._bus: EventBus | None = None
        self._poll_task: asyncio.Task | None = None
        self._last_mtime: float | None = None
        self._notified_year: int | None = None

    # ---- 两个方法（给 agent 调） ----

    def get_state(self) -> dict:
        """读取世界局势：各国最新一条记录拼成的快照（powers 按行内 rank 升序），
        游戏第一年还没导出过记录时返回空。"""
        self._require_game()
        try:
            text = self._log_path.read_text(encoding="utf-8", errors="replace")
        except FileNotFoundError:
            return {"powers": [], "gbr_finance": None}
        return build_snapshot(text)

    def start_play(self) -> str:
        """发起外交博弈（写侧占位）：实现随写侧版本补，当前返回固定的"未实现"应答。"""
        self._require_game()
        return "未实现：start_play 是写侧方法，随写侧版本补，当前只读。"

    def _require_game(self) -> None:
        if not game_running(self._game_process):
            raise GameNotRunningError(
                f"游戏未启动：进程表里没有 {self._game_process}，先启动 Victoria 3 再调用方法"
            )

    # ---- 模块生命周期 ----

    async def start(self, bus: EventBus) -> None:
        """接上总线、起 error.log 轮询。"""
        self._bus = bus
        self._poll_task = asyncio.create_task(self._poll_loop())

    async def attach_session(self) -> None:
        """get_state/start_play 注册进 agent 会话：随 agent 模块实现落。"""
        raise NotImplementedError("get_state/start_play 注册进会话：随 agent 模块实现落")

    async def stop(self) -> None:
        if self._poll_task is not None:
            self._poll_task.cancel()
            try:
                await self._poll_task
            except asyncio.CancelledError:
                pass
            self._poll_task = None

    # ---- 年度通知（轮询） ----

    async def _poll_loop(self) -> None:
        while True:
            await asyncio.sleep(self._poll_interval)
            try:
                await self._poll_once()
            except Exception:
                logger.exception("error.log 轮询出错，等下一轮")

    async def _poll_once(self) -> None:
        # 先看文件修改时间，变了才解析
        try:
            mtime = self._log_path.stat().st_mtime
        except FileNotFoundError:
            return
        if mtime == self._last_mtime:
            return
        self._last_mtime = mtime

        year = _latest_year(self._log_path)
        if year is None or (self._notified_year is not None and year <= self._notified_year):
            return
        # 年度通知以游戏在跑为前提：游戏没跑时读到的是上次留下的旧日志，只记年份不推
        if not game_running(self._game_process):
            self._notified_year = year
            return
        self._notified_year = year
        assert self._bus is not None
        await self._bus.put(Event(EventType.NEW_YEAR, year))
        logger.info("游戏进入 %s 年，推 new_year 事件", year)


def _latest_year(log_path: Path) -> int | None:
    """整份日志里本局记录的最新年份；没有本局记录返回 None。"""
    try:
        text = log_path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return None
    years = [
        record["year"]
        for line in text.splitlines()
        if (record := parse_record(line)) is not None
    ]
    return max(years, default=None)
