"""入口与装配单测：装配现状（game 与 im 落地、agent 待建）、进程从装配到退出的完整顺序。替身模块见 conftest。"""

import asyncio
import contextlib

from conftest import RecordingAgentModule, RecordingGame, RecordingIm

from config import load_config
from game.impl.module import GameModuleImpl
from im.impl.module import ImModuleImpl
import main as main_module


def test_build_modules_game与im落地agent待建(tmp_path):
    game, agent, im = main_module.build_modules(load_config(tmp_path / "config.toml"))
    assert isinstance(game, GameModuleImpl)
    assert isinstance(im, ImModuleImpl)
    assert agent is None


def test_run_从装配经命令到退出的完整顺序(monkeypatch):
    calls: list = []

    class StartGameIm(RecordingIm):
        """登录后立刻有玩家下 startGame 命令的 IM 替身：start 里调命令回调（装配处已挂上闭包）。"""

        async def start(self) -> None:
            await super().start()
            assert self.command_callback is not None, "装配处没挂命令回调"
            self.command_callback("startGame")

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
        # 装配：agent 接上总线；im 的命令回调在装配处挂上闭包（命令闭包把 startGame 包进队列）
        "agent.start",
        "im.start",
        # startGame 命令经总线到调度：起会话（工具装配时已递进 agent 模块），执行完发回执
        ("agent.start_session", True),
        ("im.send_receipt", "startGame 执行完成"),
        # 取消主循环后收摊：先按 stopGame 收尾，再按装配反序停模块
        "agent.stop_session",
        "im.stop",
        "agent.stop",
    ]
