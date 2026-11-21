"""事件总线（声明见 docs/prd/harness.md 主体·事件队列）。

主体维护一条事件队列，模块之间互不引用，来往全走它——每个模块都可以推事件、订事件，
主体自己也订。四种事件：

  command   玩家命令    IM 接入推   主体（调度）订
  message   玩家消息    IM 接入推   agent 订
  new_year  年度通知    游戏接入推  agent 订
  reply     会话回复    agent 推    IM 接入订

data 的结构由推事件的一方定义，已定两件：command 是命令名字符串（startGame /
loadGame / stopGame，IM 接入推），new_year 是年份数字（游戏接入推，指日志里新出现的
本局记录年份）；message 与 reply 随 agent、IM 接入实现落定。
"""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Awaitable, Callable

logger = logging.getLogger(__name__)


class EventType(str, Enum):
    COMMAND = "command"
    MESSAGE = "message"
    NEW_YEAR = "new_year"
    REPLY = "reply"


@dataclass
class Event:
    type: EventType
    data: Any


Handler = Callable[[Event], Awaitable[None]]


class EventBus:
    """一条 asyncio 队列＋按事件类型记订阅。订事件在装配时办，推事件随时可推。"""

    def __init__(self) -> None:
        self._queue: asyncio.Queue[Event] = asyncio.Queue()
        self._subscribers: dict[EventType, list[Handler]] = {}

    async def put(self, event: Event) -> None:
        self._queue.put_nowait(event)

    def subscribe(self, event_type: EventType, handler: Handler) -> None:
        self._subscribers.setdefault(event_type, []).append(handler)

    async def _deliver(self, event: Event) -> None:
        # 一次投一个，同一事件的订阅者挨个投完才轮到下一个事件；一个订阅者抛错不让
        # 进程停——记日志，后面的订阅者照投
        for handler in self._subscribers.get(event.type, []):
            try:
                await handler(event)
            except Exception:
                logger.exception("处理 %s 事件的订阅者抛错", event.type.value)

    async def dispatch_next(self) -> bool:
        """取一个事件投给订了它的模块；队列空返回 False（测试排空队列用）。"""
        try:
            event = self._queue.get_nowait()
        except asyncio.QueueEmpty:
            return False
        await self._deliver(event)
        return True

    async def run(self) -> None:
        """事件主循环：进程活着就在等事件，逐个取、逐个投。取消即退出。"""
        while True:
            event = await self._queue.get()
            await self._deliver(event)
