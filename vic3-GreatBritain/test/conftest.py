"""测试公共：import 路径＋三大模块的替身（记录动作序列，测主体的装配、命令顺序、退出顺序）。

真模块随迁入/实现替换，替身只在测试里用。
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


class RecordingModule:
    def __init__(self, calls: list) -> None:
        self.calls = calls


class RecordingGame(RecordingModule):
    async def start(self, bus) -> None:
        self.calls.append("game.start")

    async def attach_session(self) -> None:
        self.calls.append("game.attach_session")

    async def stop(self) -> None:
        self.calls.append("game.stop")


class RecordingAgentModule(RecordingModule):
    async def start(self, bus) -> None:
        self.calls.append("agent.start")

    async def start_session(self, fresh: bool) -> None:
        self.calls.append(("agent.start_session", fresh))

    async def stop_session(self) -> None:
        self.calls.append("agent.stop_session")

    async def stop(self) -> None:
        self.calls.append("agent.stop")


class RecordingIm(RecordingModule):
    async def start(self, bus) -> None:
        self.calls.append("im.start")

    async def attach_session(self) -> None:
        self.calls.append("im.attach_session")

    async def stop(self) -> None:
        self.calls.append("im.stop")
