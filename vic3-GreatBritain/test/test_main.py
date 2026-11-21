"""入口与装配单测：骨架阶段装配明确报待建、进程从装配到退出的完整顺序。替身模块见 conftest。"""

import asyncio
import contextlib

from conftest import RecordingAgentModule, RecordingGame, RecordingIm

from config import load_config
from events import Event, EventType
import main as main_module


def test_build_modules_骨架阶段明确报待建(tmp_path):
    try:
        main_module.build_modules(load_config(tmp_path / "config.toml"))
    except NotImplementedError as e:
        assert "src/game/impl/" in str(e)
    else:
        raise AssertionError("骨架阶段 build_modules 应报 NotImplementedError")


def test_run_从装配经命令到退出的完整顺序(monkeypatch):
    calls: list = []

    class StartGameIm(RecordingIm):
        """登录后立刻收到玩家 startGame 命令的 IM 替身：start 里推 command 事件。"""

        async def start(self, bus) -> None:
            await super().start(bus)
            await bus.put(Event(EventType.COMMAND, "startGame"))

    game = RecordingGame(calls)
    agent = RecordingAgentModule(calls)
    im = StartGameIm(calls)
    monkeypatch.setattr(main_module, "build_modules", lambda config: (game, agent, im))

    async def main():
        task = asyncio.create_task(main_module.run())
        # 让装配、命令事件、会话起接都跑完
        await asyncio.sleep(0.1)
        task.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await task

    asyncio.run(main())
    assert calls == [
        # 装配：三模块接上总线（游戏接入先起，它的轮询最早该跑）
        "game.start",
        "agent.start",
        "im.start",
        # im 推的 startGame 命令经总线到调度：起会话、接上两块
        ("agent.start_session", True),
        "game.attach_session",
        "im.attach_session",
        # 取消主循环后收摊：先按 stopGame 收尾，再按装配反序停模块
        "agent.stop_session",
        "im.stop",
        "agent.stop",
        "game.stop",
    ]
