"""端到端：真起一个 stdio MCP server 子进程，用 MCP 客户端调工具。

游戏在跑检测用"把进程名配成当前解释器"来过真路径（单测配置，不造 mock）；
游戏没在跑用查不到的进程名触发报错。
"""

import asyncio
import json
import os
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from conftest import EXPECTED_SNAPSHOT, FIXTURE

SERVER_DIR = Path(__file__).resolve().parents[1]


def _server_env(**overrides) -> dict:
    env = {
        **os.environ,
        "PYTHONIOENCODING": "utf-8",
        "VIC3_MCP_LOG_DIR": str(FIXTURE.parent),
        "VIC3_MCP_LOG_FILE": FIXTURE.name,
    }
    env.update({key: str(value) for key, value in overrides.items()})
    return env


def _call_tools(env: dict):
    async def run():
        params = StdioServerParameters(
            command=sys.executable,
            args=["server.py"],
            cwd=str(SERVER_DIR),
            env=env,
        )
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await session.list_tools()
                state = await session.call_tool("get_state", {})
                play = await session.call_tool("start_play", {})
                return tools, state, play

    return asyncio.run(run())


def test_游戏在跑_get_state返回样例快照_start_play返回未实现():
    _, state, play = _call_tools(
        _server_env(VIC3_MCP_GAME_PROCESS=Path(sys.executable).name)
    )
    assert state.is_error is False
    assert json.loads(state.content[0].text) == EXPECTED_SNAPSHOT
    assert play.is_error is False
    assert "未实现" in play.content[0].text


def test_注册了两个工具():
    tools, _, _ = _call_tools(
        _server_env(VIC3_MCP_GAME_PROCESS=Path(sys.executable).name)
    )
    assert sorted(tool.name for tool in tools.tools) == ["get_state", "start_play"]


def test_游戏没在跑_工具报错():
    _, state, play = _call_tools(_server_env(VIC3_MCP_GAME_PROCESS="no-such-game.exe"))
    assert state.is_error is True
    assert "游戏未启动" in state.content[0].text
    assert "no-such-game.exe" in state.content[0].text
    assert play.is_error is True
