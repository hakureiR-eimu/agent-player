"""agent 模块本体（接口声明见 src/agent/module.py，设计见 docs/prd/agent-运行时.md）。

消息队列＋会话起止：订 message、new_year 收进消息队列——会话空闲即送进会话唤醒，
忙时攒着、空闲了把攒下的合并成一段上下文（最前面带一行忙期间标注）送进会话。
会话本体在 session.py（Claude Agent SDK 的封装，system prompt 吃项目里的
agent-system-prompt.md），本模块经注入的 factory 起会话（单测用假 factory）；gbr 随
会话起止——起会话把开发文件夹 prompt/ 的 gbr-template/ 整个复制成全新的 gbr，收尾让会话整理
账本后结束。起会话还在 agent 日志目录（局文件夹 logs/agent，见 docs/prd/日志功能.md）
建本局运行记录文件，路径递进会话、由会话逐条追加。
"""

from __future__ import annotations

import asyncio
import logging
import shutil
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Callable

from agent.tools import SessionAuth, SessionTools
from events import Event, EventBus, EventType

if TYPE_CHECKING:
    from agent.impl.session import AgentSession

logger = logging.getLogger(__name__)

# 会话类型标注的字符串引用（运行时不 import session，单测不需要装 SDK）；第四参是
# 本局运行记录文件（起会话时建好，路径递进会话逐条追加）
SessionFactory = Callable[[Path, SessionTools, SessionAuth, Path], "AgentSession"]

# 开局送进会话的第一批：一次性的开局事件（你是谁、怎么工作在 system prompt，开局年度
# 流程在 gbr 的 CLAUDE.md，都不在这里）；玩家没先说话 agent 不主动发话——玩家第一条
# 私信进来才亮相
OPENING_PROMPT = """新的一局开始了：把开局的事办了（怎么办见你文件夹里的 CLAUDE.md）。
玩家还没跟你说话，先别主动发他私信——等他第一条私信来了，再自我介绍、开谈。"""

# 收尾批：保存游戏时让会话整理自己的文件夹（账本收尾）
CLOSING_PROMPT = "这局要存档了。把账本整理收尾——补全历史记录、把该记的账记全；不用给玩家发消息。"

# 忙时攒下的批送进会话时的开头标注：告诉 agent 这段是它忙期间积下的事件
BUSY_PREFIX = "你在忙期间发生了以下事件："


def default_session_factory(
    cwd: Path, tools: SessionTools, auth: SessionAuth, record_path: Path
) -> AgentSession:
    """真会话工厂：Claude Agent SDK 的封装在 session.py（延迟 import，SDK 只在真起会话时碰）。"""
    from agent.impl.session import SdkSession

    return SdkSession(cwd, tools, auth, record_path)


class AgentModuleImpl:
    """AgentModule 协议（src/agent/module.py）的实现：消息队列、gbr 起止。"""

    def __init__(
        self,
        gbr_dir: Path,
        agent_log_dir: Path,
        tools: SessionTools,
        gbr_template_src: Path,
        auth: SessionAuth = SessionAuth(),
        session_factory: SessionFactory = default_session_factory,
    ) -> None:
        self._gbr_dir = gbr_dir
        self._agent_log_dir = agent_log_dir
        self._tools = tools
        self._gbr_template_src = gbr_template_src
        self._auth = auth
        self._session_factory = session_factory
        self._session: AgentSession | None = None
        self._pending: list[str] = []
        self._batch_task: asyncio.Task[None] | None = None
        self._busy_deferred = False
        self._closing = False

    # ---- 总线（start 时订：收进消息队列） ----

    async def start(self, bus: EventBus) -> None:
        bus.subscribe(EventType.MESSAGE, self._on_message)
        bus.subscribe(EventType.NEW_YEAR, self._on_new_year)

    async def _on_message(self, event: Event) -> None:
        player, text = event.data["player"], event.data["text"]
        if self._session is None:
            logger.warning("没挂着的局，玩家 %s 的私信没人接：%s", player, text)
            return
        self._defer(f"玩家 {player} 发来私信：\n{text}")

    async def _on_new_year(self, event: Event) -> None:
        if self._session is None:
            return  # 局都没挂着，年不年的无所谓
        self._defer(f"游戏进入了 {event.data} 年。")

    def _defer(self, item: str) -> None:
        """收进消息队列：会话在忙时到达的记一笔，合并送批时好在最前面标注。"""
        if self._batch_task is not None:
            self._busy_deferred = True
        self._pending.append(item)
        self._try_send_batch()

    # ---- 消息队列：攒与送 ----

    def _try_send_batch(self) -> None:
        """会话空闲（没有批在跑）且队列有货：把攒下的合并成一段上下文送进会话。"""
        if self._session is None or self._closing or self._batch_task is not None or not self._pending:
            return
        prompt = "\n\n".join(self._pending)
        if self._busy_deferred:
            prompt = f"{BUSY_PREFIX}\n\n{prompt}"
            self._busy_deferred = False
        self._pending.clear()
        self._batch_task = asyncio.create_task(self._run_batch(prompt))

    async def _run_batch(self, prompt: str) -> None:
        session = self._session
        assert session is not None  # 起批时会话必在
        try:
            reply = await session.send(prompt)
            if reply.strip():
                logger.info("会话一批跑完，产出：%s", reply)
        except Exception:
            logger.exception("会话跑批抛错，这批丢掉")  # 会话还在，下一批照送
        finally:
            self._batch_task = None
            self._try_send_batch()  # 攒下的接着送

    # ---- 会话随局起止（dispatcher 按命令排着调） ----

    async def start_session(self) -> None:
        if self._session is not None:
            raise RuntimeError("会话已在跑，先保存游戏再开新的一局")
        self._build_gbr()
        record_path = self._new_record_path()
        self._session = self._session_factory(self._gbr_dir, self._tools, self._auth, record_path)
        self._closing = False
        self._pending.append(OPENING_PROMPT)
        self._try_send_batch()

    async def stop_session(self) -> None:
        if self._session is None:
            return
        self._closing = True  # 收尾期间新到的事件不再起批
        if self._batch_task is not None:
            await self._batch_task  # 在跑的批等它跑完
        session = self._session
        self._session = None
        try:
            await session.send(CLOSING_PROMPT)
        finally:
            await session.close()

    async def stop(self) -> None:
        """进程收摊用：会话还在跑就按保存游戏的收尾来（正常流里 dispatcher 已收过）。"""
        await self.stop_session()

    def _build_gbr(self) -> None:
        """建全新的 gbr：残留清掉，模板整个复制过来（手册 CLAUDE.md 与账本 md）。"""
        shutil.rmtree(self._gbr_dir, ignore_errors=True)
        shutil.copytree(self._gbr_template_src, self._gbr_dir)
        logger.info("建了全新的 gbr（从模板复制）：%s", self._gbr_dir)

    def _new_record_path(self) -> Path:
        """建本局运行记录文件：agent 日志目录下按开局时刻命名（一次会话一个，整局追加）。"""
        self._agent_log_dir.mkdir(parents=True, exist_ok=True)
        record_path = self._agent_log_dir / f"agent-{datetime.now():%Y-%m-%d_%H-%M-%S}.jsonl"
        record_path.touch()
        logger.info("建了本局运行记录：%s", record_path)
        return record_path
