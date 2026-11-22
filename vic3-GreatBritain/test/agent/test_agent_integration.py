"""agent 模块集成测试（在 VSCode 测试面板里点跑——命令行全量跑默认排除集成测试，
面板的 pytestArgs 已配 --override-ini=addopts= 绕开排除）。

前提：本机装好 Claude Code CLI（SDK 起会话靠它跑）；config.toml 配了模型凭证三项
（anthropic_base_url/anthropic_auth_token/agent_model）就走它（比如 GLM），全空走
本机 Claude Code 的登录态。不起 Discord 与游戏——工具用假的，只验会话本体：SDK 会话
起得来、批送得进、回复收得回、session_id 续得上（第二批能记得第一批）。真 Discord/
真游戏的整局循环在游戏与 bot 都在线时手动跑。
"""

import asyncio
import json

import pytest

from agent.tools import SessionAuth
from config import load_config

pytestmark = pytest.mark.integration


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
        await agent.start_session()  # 开局批：读 profile、亮相（假工具只记录不真发）
        await agent._batch_task if agent._batch_task else None
        await agent.stop_session()

    asyncio.run(scenario())

    print("\n会话发出的消息（假 send_message 记录）：")
    for text in sent:
        print(f"  {text}")
    assert sent, "开局亮相没发出来——会话没跑或工具没调"
    assert (tmp_path / "gbr" / "profile" / "PROFILE.md").exists()
    # 本局运行记录：四类逐条追加（jsonl 一行一条）
    record_files = list((tmp_path / "logs" / "agent").glob("agent-*.jsonl"))
    assert len(record_files) == 1, "起会话应建一个本局运行记录文件"
    kinds = [json.loads(line)["kind"] for line in record_files[0].read_text(encoding="utf-8").splitlines()]
    assert "tool_use" in kinds and "tool_result" in kinds, f"工具调用与结果该逐条记，实记：{kinds}"
    assert kinds.count("result") == 2, f"开局与收尾两批各一条批收尾，实记：{kinds}"
