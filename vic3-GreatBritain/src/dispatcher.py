"""调度（声明见 docs/prd/harness.md 主体实现·局状态与命令执行）。

主体记一个状态——会话在不在跑；命令到了按状态排动作。主体只排顺序，动作本身调三大
模块干。三大模块的接口形状在各自包的 module.py 声明（game/agent/im），本文件只引用。
"""

from __future__ import annotations

from agent.module import AgentModule
from events import Event, EventBus, EventType
from game.module import GameModule
from im.module import ImModule


class CommandError(Exception):
    pass


class Dispatcher:
    """局状态＋三条命令的执行顺序，执行完调 IM 接入发回执（发到命令来的频道）。装配时订 command 事件。"""

    def __init__(self, bus: EventBus, game: GameModule, agent: AgentModule | None, im: ImModule) -> None:
        self._game = game
        self._agent = agent  # agent 未建时为 None：会话命令的回执会明确报未实现
        self._im = im
        self._session_running = False
        bus.subscribe(EventType.COMMAND, self._handle_command)

    @property
    def session_running(self) -> bool:
        return self._session_running

    async def _handle_command(self, event: Event) -> None:
        try:
            await self.execute_command(event.data)
        except CommandError as e:
            await self._im.send_receipt(f"命令没执行成：{e}")
        else:
            await self._im.send_receipt(f"{event.data} 执行完成")

    async def execute_command(self, command: str) -> None:
        if command == "开始新游戏":
            if self._session_running:
                raise CommandError("会话已在跑，先保存游戏再开始新游戏")
            self._require_agent()
            await self._agent.start_session(fresh=True)
            self._session_running = True
        elif command == "继续游戏":
            if self._session_running:
                raise CommandError("会话已在跑，先保存游戏再继续游戏")
            self._require_agent()
            await self._agent.start_session(fresh=False)
            self._session_running = True
        elif command == "保存游戏":
            if self._session_running:
                await self._agent.stop_session()
                self._session_running = False
        else:
            raise CommandError(f"未知命令：{command}")

    def _require_agent(self) -> None:
        if self._agent is None:
            raise CommandError("agent 模块未建（src/agent/impl/），起不了会话")

    async def shutdown(self) -> None:
        """进程收摊用：会话还在跑就先按保存游戏收尾。"""
        if self._session_running:
            await self.execute_command("保存游戏")
