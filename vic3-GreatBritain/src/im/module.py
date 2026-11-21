"""IM 接入的接口声明（agent 的嘴和耳朵，通 Discord）：实现在 impl/。

文档见 docs/prd/harness.md 的 IM 接入节。
"""

from __future__ import annotations

from typing import Protocol

from events import EventBus


class ImModule(Protocol):
    """IM 接入的接口形状：实现在 impl/。"""

    async def start(self, bus: EventBus) -> None:
        """接上总线、登录 Discord：大厅频道与私信的命令推 command，局频道消息推 message、订 reply。"""
        ...

    async def attach_session(self) -> None:
        """会话接上 IM：局频道通到会话（实现时落）。"""
        ...

    async def stop(self) -> None: ...
