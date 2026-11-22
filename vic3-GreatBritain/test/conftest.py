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
    def check_new_year(self) -> int | None:
        self.calls.append("game.check_new_year")
        return None


class RecordingAgentModule(RecordingModule):
    async def start(self, bus) -> None:
        self.calls.append("agent.start")

    async def start_session(self) -> None:
        self.calls.append("agent.start_session")

    async def stop_session(self) -> None:
        self.calls.append("agent.stop_session")

    async def stop(self) -> None:
        self.calls.append("agent.stop")


class RecordingIm(RecordingModule):
    """IM 替身（回调式）：记录注册的回调与发送调用；测试可直接调 command_callback 模拟玩家下命令。
    channel_exists 模拟本局频道在不在（局挂没挂着的外显），测试按场景拨。"""

    def __init__(self, calls: list) -> None:
        super().__init__(calls)
        self.command_callback = None
        self.message_callback = None
        self.channel_exists = False

    def on_command(self, callback) -> None:
        self.command_callback = callback

    def on_message(self, callback) -> None:
        self.message_callback = callback

    async def send_message(self, player: str, text: str) -> None:
        self.calls.append(("im.send_message", player, text))

    async def read_message(self, player: str) -> list[dict[str, str]]:
        self.calls.append(("im.read_message", player))
        return []

    async def send_receipt(self, text: str) -> None:
        self.calls.append(("im.send_receipt", text))

    async def has_channel(self) -> bool:
        return self.channel_exists

    async def create_channel(self) -> None:
        self.channel_exists = True
        self.calls.append("im.create_channel")

    async def destroy_channel(self) -> None:
        self.channel_exists = False
        self.calls.append("im.destroy_channel")

    async def start(self) -> None:
        self.calls.append("im.start")

    async def stop(self) -> None:
        self.calls.append("im.stop")
