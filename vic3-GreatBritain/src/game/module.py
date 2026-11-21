"""游戏接入的接口声明（agent 的眼睛）：实现在 impl/（parser 解析、process 在跑检测、module 模块本体）。

get_state/start_play 两个方法给 agent 调，经 SDK 的进程内 MCP 注册进会话随 agent 模块
实现落。实现语义见 docs/prd/游戏接入-harness侧.md。
"""

from __future__ import annotations

from typing import Protocol

from events import EventBus


class GameModule(Protocol):
    """游戏接入的接口形状：实现 GameModuleImpl 在 impl/。"""

    async def start(self, bus: EventBus) -> None:
        """接上总线、起 error.log 轮询：发现新年份的本局记录推 new_year（data 为年份数字）。"""
        ...

    async def attach_session(self) -> None:
        """会话接上游戏接入：get_state/start_play 注册进会话（随 agent 模块实现落）。"""
        ...

    async def stop(self) -> None: ...
