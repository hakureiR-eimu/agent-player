"""agent 模块集成测试（在 VSCode 测试面板里点跑——命令行全量跑默认排除集成测试，
面板的 pytestArgs 已配 --override-ini=addopts= 绕开排除）。

前提：本机装好 Claude Code CLI（SDK 起会话靠它跑）；config.toml 配了模型凭证三项
（anthropic_base_url/anthropic_auth_token/agent_model）就走它（比如 GLM），全空走
本机 Claude Code 的登录态。两个测试都起真 SDK 会话：测试指令写进临时 profile，开局
批读 profile 时指令随设定进会话；会话写进 gbr 根下的回执文件是验收口——等会话空闲
后读出内容打印、删掉文件，结束时打印各自测了什么：

1. 读世界局势写 test_state.md：get_state 是真工具（直打真 error.log），游戏得在跑；
   agent 开局调它把世界局势写进自己文件夹根下的 test_state.md
2. 收私信回"收到"写 test_message：IM 也是真的（两个 bot 在线、发消息工具直连
   Discord），人在 Discord 私信 gbr bot，agent 把私信原文写进 test_message 并回
   私信"收到"（player_id 用私信里带的——发消息定向就是这么学的）

等待时长默认 300 秒，环境变量 INTEGRATION_AGENT_WAIT_SECONDS 可调。
"""

import asyncio
import contextlib
import os
import time
from pathlib import Path

import pytest

from agent.impl.module import AgentModuleImpl
from agent.tools import SessionAuth, SessionTools
from config import load_config
from events import EventBus
from game.impl.module import GameModuleImpl
from game.impl.process import game_running
from im.impl.module import ImModuleImpl
from main import build_session_tools, wire_im

pytestmark = pytest.mark.integration

WAIT_SECONDS = int(os.environ.get("INTEGRATION_AGENT_WAIT_SECONDS", "300"))


def make_profile(tmp_path: Path, instruction: str) -> Path:
    """临时 profile：最小设定＋测试指令（开局批读 profile，指令随设定进会话）。"""
    profile_src = tmp_path / "profile"
    profile_src.mkdir()
    (profile_src / "PROFILE.md").write_text(
        f"# 大不列颠玩家\n\n你是玩维多利亚3的玩家，执掌大不列颠。\n\n{instruction}\n",
        encoding="utf-8",
    )
    return profile_src


def make_agent(tmp_path: Path, tools: SessionTools, profile_src: Path) -> AgentModuleImpl:
    """真会话工厂的 agent 模块：gbr 与日志目录在临时目录，凭证吃总配置三项。"""
    config = load_config()
    return AgentModuleImpl(
        tmp_path / "gbr",
        tmp_path / "logs" / "agent",
        tools,
        profile_src,
        SessionAuth(
            base_url=config.anthropic_base_url,
            auth_token=config.anthropic_auth_token,
            model=config.agent_model,
        ),
    )


async def wait_written_and_idle(agent: AgentModuleImpl, path: Path) -> None:
    """等会话把回执文件写出来并回到空闲（文件在、没有批在跑、队列也空了），超时失败。"""
    deadline = time.monotonic() + WAIT_SECONDS
    while time.monotonic() < deadline:
        if path.exists() and agent._batch_task is None and not agent._pending:
            return
        await asyncio.sleep(1)
    pytest.fail(
        f"{WAIT_SECONDS}s 内会话没把 {path.name} 写出来——会话跑起来了吗（上面有会话报错吗），指令进会话了吗"
    )


def test_agent_reads_state_into_test_state_file(tmp_path):
    """读世界局势写 test_state.md：get_state 是真工具，agent 开局调它把结果写进自己文件夹。"""
    config = load_config()
    if not game_running(config.game_process):
        pytest.fail(f"游戏未在跑：进程表里没有 {config.game_process}，get_state 读不到真局势——先启动 Victoria 3 再跑")

    async def no_send(player_id: str, text: str) -> None:
        pass

    async def no_read(player_id: str) -> list[dict[str, str]]:
        return []

    game = GameModuleImpl(config)
    tools = SessionTools(
        get_state=game.get_state,  # 真工具：直打真 error.log
        start_play=game.start_play,
        send_message=no_send,  # 假的：这项不碰 Discord
        read_message=no_read,
    )
    profile_src = make_profile(
        tmp_path,
        "【测试指令】调用 get_state 工具读取当前世界局势，把工具返回的结果写进你文件夹"
        "根下的 test_state.md 文件（就在 profile/、world/、memory/ 旁边——本条指令优先于"
        "「只有 memory/ 可写」的常规约束）。写完就待着，不用给任何玩家发消息。",
    )
    agent = make_agent(tmp_path, tools, profile_src)
    state_path = tmp_path / "gbr" / "test_state.md"

    async def scenario() -> str:
        bus = EventBus()
        await agent.start(bus)
        try:
            await agent.start_session()
            await wait_written_and_idle(agent, state_path)
        finally:
            await agent.stop_session()
        content = state_path.read_text(encoding="utf-8")
        state_path.unlink()
        return content

    content = asyncio.run(scenario())

    print(f"\ntest_state.md 内容：\n{content}")
    print("本测试测了：agent 会话开局调真 get_state 读世界局势，写进自己文件夹的 test_state.md")
    assert content.strip(), "test_state.md 是空的——会话没把世界局势写进去"


def test_agent_replies_dm_and_records_test_message(tmp_path):
    """收私信回"收到"写 test_message：IM 全真，人私信 gbr bot，agent 记下原文并回私信。"""
    config = load_config()
    missing = [name for name, token in (("dm_token", config.dm_token), ("gbr_token", config.gbr_token)) if not token]
    if missing:
        pytest.fail(f"config.toml 缺 {'、'.join(missing)}：复制 config.example.toml 成 config.toml 填上")

    game = GameModuleImpl(config)
    im = ImModuleImpl(config)
    profile_src = make_profile(
        tmp_path,
        "【测试指令】接下来会有玩家给你发 Discord 私信。收到后做两件事：一、把私信原文"
        "写进你文件夹根下的 test_message 文件（就在 profile/、world/、memory/ 旁边——本条"
        "指令优先于「只有 memory/ 可写」的常规约束）；二、用 send_message 工具回复该玩家，"
        "就说两个字「收到」，player_id 填私信里带的 Discord 用户 ID。在玩家开口之前，先别"
        "主动发信。",
    )
    agent = make_agent(tmp_path, build_session_tools(game, im), profile_src)
    message_path = tmp_path / "gbr" / "test_message"

    async def scenario() -> str:
        bus = EventBus()
        wire_im(bus, im)  # 与主体装配同一套接线：私信进总线，agent 订着
        bus_task = asyncio.create_task(bus.run())
        await agent.start(bus)
        try:
            await agent.start_session()
            await im.start()
            print(f"\n请在 Discord 给 gbr bot 发一条私信（限时 {WAIT_SECONDS}s）")
            await wait_written_and_idle(agent, message_path)
        finally:
            bus_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await bus_task
            await agent.stop_session()
            await im.stop()
        content = message_path.read_text(encoding="utf-8")
        message_path.unlink()
        return content

    content = asyncio.run(scenario())

    print(f"\ntest_message 内容：\n{content}")
    print("本测试测了：Discord 私信经总线唤醒会话，agent 记下原文并回私信「收到」")
    assert content.strip(), "test_message 是空的——会话没把收到的私信写进去"
