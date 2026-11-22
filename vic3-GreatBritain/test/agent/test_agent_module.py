"""agent 模块单测：消息队列（空闲即送、忙时攒批合并送）、gbr 随会话起止、
本局运行记录文件的建立。

会话用假替身（FakeSession 记收到的批与开关，经 factory 注入）——SDK 的真会话走
test/agent/test_agent_integration.py（起真会话跑一局，样式照 test/im/）。
"""

import asyncio
import re
import time

from agent.impl.module import BUSY_PREFIX, CLOSING_PROMPT, OPENING_PROMPT, RESUME_PROMPT, AgentModuleImpl
from agent.tools import SessionTools
from events import Event, EventBus, EventType


class FakeSession:
    """假会话：记收到的批与开关、递进的记录文件路径；gate 不为 None 时 send 卡住等放行
    （测攒批用）。"""

    def __init__(self) -> None:
        self.prompts: list[str] = []
        self.closed = False
        self.gate: asyncio.Event | None = None
        self.record_path = None

    async def send(self, prompt: str) -> str:
        self.prompts.append(prompt)
        if self.gate is not None:
            await self.gate.wait()
        return "（一批跑完）"

    async def close(self) -> None:
        self.closed = True


def make_tools() -> SessionTools:
    async def send_message(player_id: str, text: str) -> None:
        pass

    async def read_message(player_id: str) -> list[dict[str, str]]:
        return []

    return SessionTools(
        get_state=lambda: {"powers": [], "gbr_finance": None},
        start_play=lambda: "",
        send_message=send_message,
        read_message=read_message,
    )


def make_agent(tmp_path, sessions: list[FakeSession]) -> tuple[AgentModuleImpl, EventBus]:
    """建模块＋总线（已订）：gbr、日志目录、工具、gbr 模板源都在临时目录，factory 记录
    造出的假会话（也记递进的记录文件路径）。"""
    template_src = tmp_path / "gbr-template"
    template_src.mkdir()
    (template_src / "CLAUDE.md").write_text("大不列颠玩家手册", encoding="utf-8")
    (template_src / "历史记录.md").write_text("# 历史记录", encoding="utf-8")

    def factory(cwd, tools, auth, record_path):
        session = FakeSession()
        session.record_path = record_path
        sessions.append(session)
        return session

    agent = AgentModuleImpl(
        tmp_path / "gbr",
        tmp_path / "logs" / "agent",
        make_tools(),
        template_src,
        session_factory=factory,
    )
    bus = EventBus()
    asyncio.run(agent.start(bus))
    return agent, bus


def put_message(bus: EventBus, text: str, player: str = "7") -> None:
    bus.put(Event(EventType.MESSAGE, {"player": player, "text": text}))


async def settle(seconds: float = 1.0) -> None:
    """让事件循环把攒着的 task 链跑几步（批的起与收都是 task）。"""
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        await asyncio.sleep(0.01)


# ---- 起会话：新局复制模板成全新 gbr、继续沿用挂着的 gbr，各送各的第一批 ----


def test_起会话从模板复制全新gbr并送开局批(tmp_path):
    sessions: list[FakeSession] = []
    agent, _ = make_agent(tmp_path, sessions)

    async def main():
        await agent.start_session()
        await settle()

    asyncio.run(main())
    assert (tmp_path / "gbr" / "CLAUDE.md").read_text(encoding="utf-8") == "大不列颠玩家手册"
    assert (tmp_path / "gbr" / "历史记录.md").is_file()
    assert sessions[0].prompts[0] == OPENING_PROMPT


def test_起会话清掉残留永远全新(tmp_path):
    sessions: list[FakeSession] = []
    agent, _ = make_agent(tmp_path, sessions)
    (tmp_path / "gbr").mkdir()
    (tmp_path / "gbr" / "old.json").write_text("上局残留", encoding="utf-8")

    async def main():
        await agent.start_session()
        await settle()

    asyncio.run(main())
    assert not (tmp_path / "gbr" / "old.json").exists()  # 残留清掉
    assert (tmp_path / "gbr" / "CLAUDE.md").exists()  # 新局从模板装齐


def test_会话已在跑再起明确报错(tmp_path):
    sessions: list[FakeSession] = []
    agent, _ = make_agent(tmp_path, sessions)

    async def main():
        await agent.start_session()
        try:
            await agent.start_session()
            raise AssertionError("应报错")
        except RuntimeError:
            pass

    asyncio.run(main())


def test_起会话建本局运行记录文件带时刻(tmp_path):
    sessions: list[FakeSession] = []
    agent, _ = make_agent(tmp_path, sessions)

    async def main():
        await agent.start_session()
        await settle()

    asyncio.run(main())
    record_path = sessions[0].record_path
    assert record_path.parent == tmp_path / "logs" / "agent"  # 在 agent 日志目录下
    assert record_path.exists()  # 起会话即建
    assert re.fullmatch(r"agent-\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}\.jsonl", record_path.name)


def test_继续会话不动gbr送继续批(tmp_path):
    sessions: list[FakeSession] = []
    agent, _ = make_agent(tmp_path, sessions)
    gbr = tmp_path / "gbr"
    gbr.mkdir()  # 挂着的局：gbr 已在（进程收摊收过尾，账本留下）
    (gbr / "历史记录.md").write_text("# 这一局的记忆", encoding="utf-8")

    async def main():
        await agent.resume_session()
        await settle()

    asyncio.run(main())
    assert (gbr / "历史记录.md").read_text(encoding="utf-8") == "# 这一局的记忆"  # 记忆延续，模板不复制
    assert sessions[0].prompts[0] == RESUME_PROMPT


def test_会话已在跑再继续明确报错(tmp_path):
    sessions: list[FakeSession] = []
    agent, _ = make_agent(tmp_path, sessions)

    async def main():
        await agent.start_session()
        try:
            await agent.resume_session()
            raise AssertionError("应报错")
        except RuntimeError:
            pass

    asyncio.run(main())


# ---- 消息队列：空闲即送、忙时攒批 ----


def test_私信到达送进会话(tmp_path):
    sessions: list[FakeSession] = []
    agent, bus = make_agent(tmp_path, sessions)

    async def main():
        await agent.start_session()
        await settle()
        put_message(bus, "在吗，谈谈关税")
        await bus.dispatch_next()
        await settle()

    asyncio.run(main())
    assert len(sessions[0].prompts) == 2  # 开局批＋私信批
    assert "在吗，谈谈关税" in sessions[0].prompts[1]
    assert "7" in sessions[0].prompts[1]
    assert not sessions[0].prompts[1].startswith(BUSY_PREFIX)  # 空闲即送的单条不带忙期间标注


def test_忙时攒批空闲合并成一段送(tmp_path):
    sessions: list[FakeSession] = []
    agent, bus = make_agent(tmp_path, sessions)

    async def main():
        await agent.start_session()
        sessions[0].gate = asyncio.Event()  # 开局批卡住（会话忙）
        await settle()
        for text in ("第一句", "第二句", "第三句"):
            put_message(bus, text)
            await bus.dispatch_next()
        await settle()
        assert len(sessions[0].prompts) == 1  # 忙：三条都攒着
        sessions[0].gate.set()  # 放行：开局批跑完，攒下的合并送
        await settle()
        assert len(sessions[0].prompts) == 2
        assert sessions[0].prompts[1].startswith(BUSY_PREFIX)  # 忙时攒的批，最前面带忙期间标注
        for text in ("第一句", "第二句", "第三句"):
            assert text in sessions[0].prompts[1]

    asyncio.run(main())


def test_新年进队列送到会话(tmp_path):
    sessions: list[FakeSession] = []
    agent, bus = make_agent(tmp_path, sessions)

    async def main():
        await agent.start_session()
        await settle()
        bus.put(Event(EventType.NEW_YEAR, 1837))
        await bus.dispatch_next()
        await settle()

    asyncio.run(main())
    assert "游戏进入了 1837 年。" in sessions[0].prompts[1]


def test_局外的私信与新年不炸(tmp_path):
    sessions: list[FakeSession] = []
    agent, bus = make_agent(tmp_path, sessions)

    async def main():
        put_message(bus, "没挂局呢")
        await bus.dispatch_next()
        bus.put(Event(EventType.NEW_YEAR, 1837))
        await bus.dispatch_next()

    asyncio.run(main())
    assert sessions == []  # 没起过会话


# ---- 收尾：整理账本后关会话 ----


def test_收尾送整理批并关会话(tmp_path):
    sessions: list[FakeSession] = []
    agent, bus = make_agent(tmp_path, sessions)

    async def main():
        await agent.start_session()
        await settle()
        put_message(bus, "先聊到这")
        await bus.dispatch_next()
        await settle()
        await agent.stop_session()
        await agent.stop_session()  # 再收一次没会话，无事发生

    asyncio.run(main())
    assert sessions[0].prompts[-1] == CLOSING_PROMPT
    assert sessions[0].closed
