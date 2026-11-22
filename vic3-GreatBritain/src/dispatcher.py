"""调度（声明见 docs/prd/harness.md 主体实现·局状态与命令执行）。

主体记一个状态——会话在不在跑；本局频道（GreatBritain）在不在是局挂没挂着的外显，
问 IM 接入（has_channel）。命令到了按状态排动作，主体只排顺序，动作本身调三大模块干。
三大模块的接口形状在各自包的 module.py 声明（game/agent/im），本文件只引用。
"""

from __future__ import annotations

import logging
import shutil
from pathlib import Path

from agent.module import AgentModule
from events import Event, EventBus, EventType
from game.module import GameModule
from im.module import ImModule

logger = logging.getLogger(__name__)


class CommandError(Exception):
    pass


class Dispatcher:
    """局状态＋三条命令的执行顺序，执行完调 IM 接入发回执（发到命令来的频道）。装配时订 command 事件。"""

    def __init__(self, bus: EventBus, game: GameModule, agent: AgentModule | None, im: ImModule, gbr_dir: Path) -> None:
        self._game = game
        self._agent = agent  # agent 未建时为 None：起会话的命令回执会明确报未实现
        self._im = im
        self._gbr_dir = gbr_dir  # 结束游戏时清掉（这局彻底完）
        self._session_running = False
        bus.subscribe(EventType.COMMAND, self._handle_command)

    @property
    def session_running(self) -> bool:
        return self._session_running

    async def _handle_command(self, event: Event) -> None:
        logger.info("收到命令：%s", event.data)
        try:
            await self.execute_command(event.data)
        except CommandError as e:
            logger.warning("命令没执行成：%s", e)
            await self._im.send_receipt(f"命令没执行成：{e}")
        else:
            logger.info("命令执行完成：%s", event.data)
            await self._im.send_receipt(f"{event.data} 执行完成")

    async def execute_command(self, command: str) -> None:
        if command == "开始游戏":
            if await self._im.has_channel():
                raise CommandError("GreatBritain 频道已在，先结束游戏再开新的一局")
            agent = self._require_agent()
            await self._im.create_channel()
            await agent.start_session()
            self._session_running = True
        elif command == "保存游戏":
            if self._session_running:
                await self._require_agent().stop_session()
                self._session_running = False
        elif command == "结束游戏":
            if not await self._im.has_channel():
                raise CommandError("没有 GreatBritain 频道，没有挂着的局")
            if self._session_running:
                await self._require_agent().stop_session()
                self._session_running = False
            await self._im.destroy_channel()
            shutil.rmtree(self._gbr_dir, ignore_errors=True)  # 没建过 gbr 不算错
        else:
            raise CommandError(f"未知命令：{command}")

    def _require_agent(self) -> AgentModule:
        """取 agent 模块；未建时报错（起会话的命令用它落实 agent 必在）。"""
        if self._agent is None:
            raise CommandError("agent 模块未建（src/agent/impl/），起不了会话")
        return self._agent

    async def shutdown(self) -> None:
        """进程收摊用：会话还在跑就先按保存游戏收尾（局还挂着，频道与 gbr 都不动）。"""
        if self._session_running:
            await self.execute_command("保存游戏")
