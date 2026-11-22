"""会话工具集：主体装配时把模块方法对接成这四件，递给 agent 模块挂进会话。

agent 调工具由主体翻译成对模块方法的实际调用（主体是翻译层，见 docs/prd/harness.md
主体实现·装配）；把工具挂进会话的 SDK 细节在 impl/session.py，本文件只有形状。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Awaitable, Callable

from game.module import WorldSnapshot


@dataclass(frozen=True)
class SessionTools:
    """会话工具集（四件）：游戏两件、Discord 收发两件。

    send_message/read_message 带玩家参数（player_id 由 agent 填，值从收到的私信里
    带的玩家 Discord 用户 ID 学来）。
    """

    get_state: Callable[[], WorldSnapshot]
    start_play: Callable[[], str]
    send_message: Callable[[str, str], Awaitable[None]]
    read_message: Callable[[str], Awaitable[list[dict[str, str]]]]


@dataclass(frozen=True)
class SessionAuth:
    """会话的模型与凭证（config.toml 的三项）：配了走 config——与玩家自己的 Claude Code
    分开（比如接 GLM 的 Anthropic 兼容入口）；全空走本机默认（Claude Code 的登录态）。
    """

    base_url: str | None = None
    auth_token: str | None = None
    model: str | None = None
