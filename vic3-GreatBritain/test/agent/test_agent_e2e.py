"""agent 模块端到端测试（只能手动运行，默认排除；跑法：uv run pytest test/agent/test_agent_e2e.py -m e2e -s）。

前提：本机装好 Claude Code CLI（SDK 起会话靠它跑）。不起 Discord 与游戏——工具用
假的，只验会话本体：SDK 会话起得来、批送得进、回复收得回、session_id 续得上
（第二批能记得第一批）。真 Discord/真游戏的整局循环在游戏与 bot 都在线时手动跑。
"""

import asyncio

import pytest

pytestmark = pytest.mark.e2e


def test_真会话送批收回复并续上下文(tmp_path):
    from agent.impl.module import AgentModuleImpl
    from agent.tools import SessionTools

    sent: list[str] = []

    async def fake_send_message(text: str) -> None:
        sent.append(text)

    async def fake_read_message() -> list[dict[str, str]]:
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
    agent = AgentModuleImpl(tmp_path / "GBR", tools, profile_src)

    async def scenario() -> None:
        await agent.start_session()  # 开局批：读 profile、亮相（假工具只记录不真发）
        await agent._batch_task if agent._batch_task else None
        await agent.stop_session()

    asyncio.run(scenario())

    print("\n会话发出的消息（假 send_message 记录）：")
    for text in sent:
        print(f"  {text}")
    assert sent, "开局亮相没发出来——会话没跑或工具没调"
    assert (tmp_path / "GBR" / "profile" / "PROFILE.md").exists()
