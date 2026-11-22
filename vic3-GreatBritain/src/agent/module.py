"""agent 的接口声明：agent 本体是 Claude Code 会话。已实现——实现在 impl/（消息队列
与 GBR 起止在 module.py、SDK 会话封装在 session.py），设计见 docs/prd/agent.md。

会话的工具由主体装配时递入（主体把游戏接入的方法与 IM 接入的收发包成会话工具，
agent 调工具由主体翻译成实际函数），agent 模块只管把它挂进会话，不知道工具背后是什么。
文档见 docs/prd/harness.md 的 agent 节。
"""

from __future__ import annotations

from typing import Protocol

from events import EventBus


class AgentModule(Protocol):
    """agent 的接口形状（能力声明待补齐后写全）：实现在 impl/。"""

    async def start(self, bus: EventBus) -> None:
        """接上总线：订 message、new_year 收进消息队列——会话空闲即送进会话唤醒，
        忙时攒着、空闲了合并成一段上下文送进会话。"""
        ...

    async def start_session(self) -> None:
        """起一个基于全新 GBR 的 agent 会话：先建全新的 GBR 文件夹（装入 profile）再起。"""
        ...

    async def stop_session(self) -> None:
        """让会话整理自己的文件夹，然后结束会话。"""
        ...

    async def stop(self) -> None: ...
