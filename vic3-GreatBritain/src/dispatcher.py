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
    """局状态＋三条命令的执行顺序。装配时订 command 事件。"""

    def __init__(self, bus: EventBus, game: GameModule, agent: AgentModule, im: ImModule) -> None:
        self._game = game
        self._agent = agent
        self._im = im
        self._session_running = False
        bus.subscribe(EventType.COMMAND, self._handle_command)

    @property
    def session_running(self) -> bool:
        return self._session_running

    async def _handle_command(self, event: Event) -> None:
        await self.execute_command(event.data)

    async def execute_command(self, command: str) -> None:
        if command == "startGame":
            if self._session_running:
                raise CommandError("会话已在跑，先 stopGame 再 startGame")
            await self._agent.start_session(fresh=True)
            self._session_running = True
        elif command == "loadGame":
            if self._session_running:
                raise CommandError("会话已在跑，先 stopGame 再 loadGame")
            await self._agent.start_session(fresh=False)
            self._session_running = True
        elif command == "stopGame":
            if self._session_running:
                await self._agent.stop_session()
                self._session_running = False
        else:
            raise CommandError(f"未知命令：{command}")

    async def shutdown(self) -> None:
        """进程收摊用：会话还在跑就先按 stopGame 收尾。"""
        if self._session_running:
            await self.execute_command("stopGame")
