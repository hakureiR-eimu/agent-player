"""调度（声明见 docs/prd/harness.md 主体实现·局状态与命令执行）。

主体记一个状态——会话在不在跑；命令到了按状态排动作。主体只排顺序，动作本身调三大
模块干。三大模块的接口形状在本文件以 Protocol 声明：游戏接入迁入 src/game/、
agent 落 src/agent/、IM 接入落 src/im/ 时照此实现。
"""

from __future__ import annotations

from typing import Protocol

from events import Event, EventBus, EventType


class GameModule(Protocol):
    """游戏接入（现有 mcp-server 迁入 src/game/，实现进 game/impl/）。"""

    async def start(self, bus: EventBus) -> None:
        """接上总线、起 error.log 轮询：发现新年份的本局记录推 new_year。"""
        ...

    async def attach_session(self) -> None:
        """会话接上游戏接入：get_state/start_play 注册进会话（迁入时落）。"""
        ...

    async def stop(self) -> None: ...


class AgentModule(Protocol):
    """agent（实现在 src/agent/，实现进 agent/impl/，能力声明待补齐后写）。"""

    async def start(self, bus: EventBus) -> None:
        """接上总线：订 message、new_year（空闲叫醒、忙时攒批），推 reply。"""
        ...

    async def start_session(self, fresh: bool) -> None:
        """起一个基于 GBR 的 agent 会话：fresh=True 先建全新的 GBR 文件夹，False 用已有的。"""
        ...

    async def stop_session(self) -> None:
        """让会话整理自己的文件夹，然后结束会话。"""
        ...

    async def stop(self) -> None: ...


class ImModule(Protocol):
    """IM 接入（实现在 src/im/，实现进 im/impl/）。"""

    async def start(self, bus: EventBus) -> None:
        """接上总线、登录 Discord：大厅频道与私信的命令推 command，局频道消息推 message、订 reply。"""
        ...

    async def attach_session(self) -> None:
        """会话接上 IM：局频道通到会话（实现时落）。"""
        ...

    async def stop(self) -> None: ...


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
            await self._game.attach_session()
            await self._im.attach_session()
            self._session_running = True
        elif command == "loadGame":
            if self._session_running:
                raise CommandError("会话已在跑，先 stopGame 再 loadGame")
            await self._agent.start_session(fresh=False)
            await self._game.attach_session()
            await self._im.attach_session()
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
