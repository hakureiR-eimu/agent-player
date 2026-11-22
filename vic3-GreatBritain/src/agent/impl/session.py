"""Claude Agent SDK 的会话封装（agent 模块的会话本体，设计见 docs/prd/agent.md）。

一次随局的会话：每批一次 query（prompt 进、最终回复出），批与批之间靠 session_id 续
上下文（SDK 把会话记在盘上，resume 即续，没有要维护的长连接）；工具经 SDK 的进程内
MCP 挂进——主体递入的 SessionTools 在这包成 SdkMcpTool。上下文压缩归 SDK 的上下文
管理。写权限先走引导软约束（OPENING_PROMPT 里写明只有 memory/ 可写），路径级的硬
限制随后实测再配。
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import TypedDict

from agent.tools import SessionTools
from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    McpSdkServerConfig,
    ResultMessage,
    TextBlock,
    create_sdk_mcp_server,
    query,
    tool,
)

logger = logging.getLogger(__name__)

# 挂进会话的进程内 MCP 服务器名（工具在会话里以 mcp__<服务器名>__<工具名> 出现）
MCP_SERVER_NAME = "agent-tools"


class AgentSession(ABC):
    """会话的形状：送批（prompt 进、回复文本出）与关闭。单测用假替身。"""

    @abstractmethod
    async def send(self, prompt: str) -> str:
        """送一批进会话，跑完收最终回复文本。"""
        ...

    @abstractmethod
    async def close(self) -> None:
        """结束会话。"""
        ...


class _NoInput(TypedDict):
    pass


class _SendMessageInput(TypedDict):
    text: str


def build_mcp_server(tools: SessionTools) -> McpSdkServerConfig:
    """把主体递入的 SessionTools 包成进程内 MCP 工具（名字与描述就是 agent 看到的说明）。"""

    @tool(
        name="get_state",
        description="读取世界局势：各国最新格局拼成的快照（powers 按 rank 升序＋大不列颠财政）",
        input_schema=_NoInput,
    )
    async def get_state(args: _NoInput) -> dict:
        return {"state": tools.get_state()}

    @tool(name="start_play", description="发起一局外交博弈", input_schema=_NoInput)
    async def start_play(args: _NoInput) -> dict:
        return {"result": tools.start_play()}

    @tool(
        name="send_message",
        description="给玩家发 Discord 私信——把话说出去，你的话只在你主动发出去时才算数",
        input_schema=_SendMessageInput,
    )
    async def send_message(args: _SendMessageInput) -> dict:
        await tools.send_message(args["text"])
        return {"ok": True}

    @tool(
        name="read_message",
        description="读与玩家的 Discord 私信记录（最近 100 条，从新到旧排）",
        input_schema=_NoInput,
    )
    async def read_message(args: _NoInput) -> dict:
        return {"messages": await tools.read_message()}

    return create_sdk_mcp_server(
        MCP_SERVER_NAME, tools=[get_state, start_play, send_message, read_message]
    )


class SdkSession(AgentSession):
    """真会话：Claude Agent SDK 的 query，批间靠 session_id 续。"""

    def __init__(self, cwd: Path, tools: SessionTools) -> None:
        self._cwd = cwd
        self._session_id: str | None = None
        self._server = build_mcp_server(tools)

    async def send(self, prompt: str) -> str:
        options = ClaudeAgentOptions(
            cwd=self._cwd,
            permission_mode="bypassPermissions",
            mcp_servers={MCP_SERVER_NAME: self._server},
            resume=self._session_id,  # None 即新会话，有 id 即续上批
        )
        texts: list[str] = []
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, AssistantMessage):
                texts.extend(
                    block.text for block in message.content if isinstance(block, TextBlock)
                )
            elif isinstance(message, ResultMessage):
                self._session_id = message.session_id
        return "\n".join(texts)

    async def close(self) -> None:
        pass  # 每批独立 query（resume 续），没有要关的长连接
