"""Claude Agent SDK 的会话封装（agent 模块的会话本体，设计见 docs/prd/agent-运行时.md）。

一次随局的会话：每批一次 query（prompt 进、最终回复出），批与批之间靠 session_id 续
上下文（SDK 把会话记在盘上，resume 即续，没有要维护的长连接）；工具经 SDK 的进程内
MCP 挂进——主体递入的 SessionTools 在这包成 SdkMcpTool。system prompt 吃开发文件夹
下的 agent-system-prompt.md（固定内容，完全替换 SDK 默认的 system prompt——agent 是
玩家，不吃助手默认人设），gbr 里复制的 CLAUDE.md 手册由 SDK 作为项目指令自动装载。
上下文压缩归 SDK 的上下文管理。写权限先走软约束（system prompt 写明只有 memory/
可写），路径级的硬限制随后实测再配。

送批期间流过的消息按四类逐条追加进本局运行记录（jsonl，agent 模块起会话时建好递进
来，格式见 docs/prd/日志功能.md）：agent 说的话（assistant）、工具调用（tool_use）、
工具结果（tool_result）、批收尾（result）。
"""

from __future__ import annotations

import json
import logging
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Any, TypedDict

from agent.tools import SessionAuth, SessionTools
from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    McpSdkServerConfig,
    ResultMessage,
    TextBlock,
    ToolResultBlock,
    ToolUseBlock,
    UserMessage,
    create_sdk_mcp_server,
    query,
    tool,
)

logger = logging.getLogger(__name__)

# 挂进会话的进程内 MCP 服务器名（工具在会话里以 mcp__<服务器名>__<工具名> 出现）
MCP_SERVER_NAME = "agent-tools"

# agent 的 system prompt 源：开发文件夹下的 agent-system-prompt.md（起会话时读进来，
# 每批 query 都带上——完全替换 SDK 默认的 system prompt）
SYSTEM_PROMPT_PATH = Path(__file__).resolve().parents[3] / "agent-system-prompt.md"


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


class _PlayerInput(TypedDict):
    player_id: str


class _SendMessageInput(TypedDict):
    player_id: str
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
        description="给玩家发 Discord 私信——player_id 填玩家的 Discord 用户 ID（玩家私信进来时带着的那串数字），把话说出去，你的话只在你主动发出去时才算数",
        input_schema=_SendMessageInput,
    )
    async def send_message(args: _SendMessageInput) -> dict:
        await tools.send_message(args["player_id"], args["text"])
        return {"ok": True}

    @tool(
        name="read_message",
        description="读与玩家的 Discord 私信记录（最近 100 条，从新到旧排）——player_id 填玩家的 Discord 用户 ID",
        input_schema=_PlayerInput,
    )
    async def read_message(args: _PlayerInput) -> dict:
        return {"messages": await tools.read_message(args["player_id"])}

    return create_sdk_mcp_server(
        MCP_SERVER_NAME, tools=[get_state, start_play, send_message, read_message]
    )


def _now() -> str:
    return datetime.now().isoformat(timespec="seconds")


def _tool_result_text(content: str | list[dict[str, Any]] | None) -> str:
    """工具结果的回执取文本：str 原样，块列表序列化保留原文，None 记空串。"""
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    return json.dumps(content, ensure_ascii=False)


class SdkSession(AgentSession):
    """真会话：Claude Agent SDK 的 query，批间靠 session_id 续。模型与凭证吃 SessionAuth
    （config 配了走 config——模型名进 options、入口与 token 化成子进程环境变量；全空
    走本机 Claude Code 的默认）。本局运行记录文件（record_path）由 agent 模块建好递入，
    送批流过的消息按四类逐条追加进它。"""

    def __init__(
        self, cwd: Path, tools: SessionTools, auth: SessionAuth, record_path: Path
    ) -> None:
        self._cwd = cwd
        self._auth = auth
        self._record_path = record_path
        self._session_id: str | None = None
        self._server = build_mcp_server(tools)
        self._system_prompt = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")

    def _record(self, record: dict[str, Any]) -> None:
        """运行记录逐条追加：一行一条 json。"""
        with self._record_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def _env(self) -> dict[str, str]:
        """凭证进子进程环境变量：只在配了的时候设，没配的留给本机默认。"""
        env: dict[str, str] = {}
        if self._auth.base_url:
            env["ANTHROPIC_BASE_URL"] = self._auth.base_url
        if self._auth.auth_token:
            env["ANTHROPIC_AUTH_TOKEN"] = self._auth.auth_token
        return env

    async def send(self, prompt: str) -> str:
        options = ClaudeAgentOptions(
            cwd=self._cwd,
            permission_mode="bypassPermissions",
            mcp_servers={MCP_SERVER_NAME: self._server},
            resume=self._session_id,  # None 即新会话，有 id 即续上批
            model=self._auth.model,
            env=self._env(),
            system_prompt=self._system_prompt,
            # 不读本机 Claude Code 的 settings（~/.claude/settings.json 的 env 段会把
            # 传入的凭证覆盖回去——2026-11-22 实测），配置只来自显式传入的这些项
            setting_sources=[],
        )
        texts: list[str] = []
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        texts.append(block.text)
                        self._record({"time": _now(), "kind": "assistant", "text": block.text})
                    elif isinstance(block, ToolUseBlock):
                        self._record(
                            {
                                "time": _now(),
                                "kind": "tool_use",
                                "tool": block.name,
                                "input": block.input,
                            }
                        )
            elif isinstance(message, UserMessage) and isinstance(message.content, list):
                for block in message.content:
                    if isinstance(block, ToolResultBlock):
                        self._record(
                            {
                                "time": _now(),
                                "kind": "tool_result",
                                "text": _tool_result_text(block.content),
                            }
                        )
            elif isinstance(message, ResultMessage):
                self._session_id = message.session_id
                self._record(
                    {
                        "time": _now(),
                        "kind": "result",
                        "session_id": message.session_id,
                        "duration_ms": message.duration_ms,
                        "num_turns": message.num_turns,
                        "total_cost_usd": message.total_cost_usd,
                    }
                )
        return "\n".join(texts)

    async def close(self) -> None:
        pass  # 每批独立 query（resume 续），没有要关的长连接
