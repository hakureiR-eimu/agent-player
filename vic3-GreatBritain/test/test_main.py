"""入口与装配单测：三大模块全落地、进程从装配到退出的完整顺序。替身模块见 conftest。"""

import asyncio
import contextlib

from conftest import RecordingAgentModule, RecordingGame, RecordingIm

from agent.impl.module import AgentModuleImpl
from config import load_config
from game.impl.module import GameModuleImpl
from im.impl.module import ImModuleImpl
import main as main_module


def test_build_modules_三大模块全落地(tmp_path):
    game, agent, im = main_module.build_modules(load_config(tmp_path / "config.toml"))
    assert isinstance(game, GameModuleImpl)
    assert isinstance(agent, AgentModuleImpl)
    assert isinstance(im, ImModuleImpl)


def test_run_从装配经命令到退出的完整顺序(monkeypatch):
    calls: list = []

    class CommandOnStartIm(RecordingIm):
        """登录后立刻有玩家下开始游戏命令的 IM 替身：start 里调命令回调（装配处已挂上闭包）。"""

        async def start(self) -> None:
            await super().start()
            assert self.command_callback is not None, "装配处没挂命令回调"
            self.command_callback("开始游戏")

    game = RecordingGame(calls)
    agent = RecordingAgentModule(calls)
    im = CommandOnStartIm(calls)
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
        # 装配：agent 接上总线；im 的命令回调在装配处挂上闭包（命令闭包把开始游戏包进队列）
        "agent.start",
        "im.start",
        # 开始游戏命令经总线到调度：建本局频道、起会话（工具装配时已递进 agent 模块），执行完发回执
        "im.create_channel",
        "agent.start_session",
        ("im.send_receipt", "开始游戏 执行完成"),
        # 取消主循环后收摊：先按保存游戏收尾（局还挂着，频道与 gbr 不动），再按装配反序停模块
        "agent.stop_session",
        "im.stop",
        "agent.stop",
    ]
