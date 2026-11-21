"""IM 接入的接口声明（agent 的嘴和耳朵，通 Discord）：实现在 impl/。

收是被动、发是主动：bot 在线收着（Gateway 长连接），收到的命令与消息调主体注册的
回调交出去——包事件推进队列在装配处，本模块零总线知识；发回复与回执是主体调方法。
文档见 docs/prd/harness.md 的 IM 接入节、docs/prd/discord接入.md。
"""

from __future__ import annotations

from typing import Callable, Protocol


class ImModule(Protocol):
    """IM 接入的接口形状：实现在 impl/。

    两组能力加起停——收（被动）：装配时挂回调，收到即调；发（主动）：主体调方法。
    """

    # ---- 收（被动）：交出去，事件打包在装配处 ----

    def on_command(self, callback: Callable[[str], None]) -> None:
        """注册命令回调：玩家在大厅频道 @ dm bot 下命令，命中白名单后带命令词调它。"""
        ...

    def on_message(self, callback: Callable[[str, str], None]) -> None:
        """注册消息回调：玩家私信 gbr bot，带（玩家、正文）调它。"""
        ...

    # ---- 发（主动）：主体调 ----

    async def send_reply(self, player: str, text: str) -> None:
        """把 agent 的回复发到该玩家的私信频道（主体订到 reply 事件后调）。"""
        ...

    async def send_receipt(self, text: str) -> None:
        """把命令回执发到大厅频道原处（主体执行完命令后调，固定文案）。"""
        ...

    # ---- 本局频道（GreatBritain）：主体按命令排着调 ----

    async def has_channel(self) -> bool:
        """查本局频道在不在——局挂没挂着的外显，主体用它挡开始游戏与结束游戏。"""
        ...

    async def create_channel(self) -> None:
        """建本局频道（开始游戏排的第一步，在哪个服务器取最近一条命令来的）。"""
        ...

    async def destroy_channel(self) -> None:
        """销毁本局频道（结束游戏排的动作，会话收尾之后调）。"""
        ...

    # ---- 起停 ----

    async def start(self) -> None:
        """登录两个 bot（dm、gbr）、起 Gateway 长连接。"""
        ...

    async def stop(self) -> None: ...
