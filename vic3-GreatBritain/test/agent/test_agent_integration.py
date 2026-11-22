"""agent 模块集成测试（在 VSCode 测试面板里点跑——命令行全量跑默认排除集成测试，
面板的 pytestArgs 已配 --override-ini=addopts= 绕开排除）。

前提：本机装好 Claude Code CLI（SDK 起会话靠它跑）；config.toml 配了模型凭证三项
（anthropic_base_url/anthropic_auth_token/agent_model）就走它（比如 GLM），全空走
本机 Claude Code 的登录态。不起 Discord 与游戏——工具用假的，只验会话本体：SDK 会话
起得来、批送得进、回复收得回、session_id 续得上（后一批能记得前一批）。真 Discord/
真游戏的整局循环在游戏与 bot 都在线时手动跑。
"""

import asyncio
import json

import pytest

from agent.tools import SessionAuth
from config import load_config
from events import Event, EventBus, EventType

pytestmark = pytest.mark.integration


def test_真会话送批收回复并续上下文(tmp_path):
    from agent.impl.module import AgentModuleImpl
    from agent.tools import SessionTools

    sent: list[tuple[str, str]] = []

    async def fake_send_message(player_id: str, text: str) -> None:
        sent.append((player_id, text))

    async def fake_read_message(player_id: str) -> list[dict[str, str]]:
        return [{"author": "人类玩家", "text": "（历史私信）", "time": "t001"}]

    tools = SessionTools(
        get_state=lambda: {"powers": [], "gbr_finance": None},
        start_play=lambda: "（假博弈已发起）",
        send_message=fake_send_message,
        read_message=fake_read_message,
    )
    profile_src = tmp_path / "profile"
    profile_src.mkdir()
    (profile_src / "PROFILE.md").write_text(
        "# 大不列颠玩家\n\n你是玩维多利亚3的玩家，执掌大不列颠。", encoding="utf-8"
    )
    config = load_config()
    agent = AgentModuleImpl(
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

    async def scenario() -> None:
        bus = EventBus()
        await agent.start(bus)
        await agent.start_session()  # 开局批：读 profile 进入角色（不发话）
        await agent._batch_task if agent._batch_task else None
        bus.put(Event(EventType.MESSAGE, {"player": "7", "text": "在吗，你是哪位"}))
        await bus.dispatch_next()  # 私信进队列、唤醒会话——agent 该用它带的玩家 ID 回话
        await agent._batch_task if agent._batch_task else None
        await agent.stop_session()

    asyncio.run(scenario())

    print("\n会话发出的私信（假 send_message 记录）：")
    for player_id, text in sent:
        print(f"  → 玩家 {player_id}：{text}")
    assert sent, "玩家私信进来后会话没回话——会话没跑或工具没调"
    assert all(player_id == "7" for player_id, _ in sent), (
        f"回话该定向玩家 7（私信里带的 Discord 用户 ID，agent 自己填），实发：{sent}"
    )
    assert (tmp_path / "gbr" / "profile" / "PROFILE.md").exists()
    # 本局运行记录：四类逐条追加（jsonl 一行一条）
    record_files = list((tmp_path / "logs" / "agent").glob("agent-*.jsonl"))
    assert len(record_files) == 1, "起会话应建一个本局运行记录文件"
    kinds = [json.loads(line)["kind"] for line in record_files[0].read_text(encoding="utf-8").splitlines()]
    assert "tool_use" in kinds and "tool_result" in kinds, f"工具调用与结果该逐条记，实记：{kinds}"
    assert kinds.count("result") == 3, f"开局、私信、收尾三批各一条批收尾，实记：{kinds}"
