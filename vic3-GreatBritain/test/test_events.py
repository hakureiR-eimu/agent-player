"""事件总线单测：推了订者收到、串行投递、多订者、没订的类型、订阅者抛错不断线。"""

import asyncio

from events import Event, EventBus, EventType


def test_事件投给订了的模块():
    async def main():
        bus = EventBus()
        got = []

        async def on_new_year(event):
            got.append(event.data)

        bus.subscribe(EventType.NEW_YEAR, on_new_year)
        bus.put(Event(EventType.NEW_YEAR, 1838))
        assert await bus.dispatch_next() is True
        assert got == [1838]
        assert await bus.dispatch_next() is False

    asyncio.run(main())


def test_没订的类型丢了不炸():
    async def main():
        bus = EventBus()
        bus.put(Event(EventType.MESSAGE, "玩家消息"))
        assert await bus.dispatch_next() is True

    asyncio.run(main())


def test_同一事件多个订者按订阅顺序串行():
    async def main():
        bus = EventBus()
        order = []

        async def first(event):
            order.append("first 进")
            await asyncio.sleep(0)
            order.append("first 出")

        async def second(event):
            order.append("second 进")

        bus.subscribe(EventType.NEW_YEAR, first)
        bus.subscribe(EventType.NEW_YEAR, second)
        bus.put(Event(EventType.NEW_YEAR, 1838))
        await bus.dispatch_next()
        assert order == ["first 进", "first 出", "second 进"]

    asyncio.run(main())


def test_一个订者抛错后面的订者照投():
    async def main():
        bus = EventBus()
        got = []

        async def bad(event):
            raise ValueError("订阅者坏了")

        async def good(event):
            got.append(event.data)

        bus.subscribe(EventType.COMMAND, bad)
        bus.subscribe(EventType.COMMAND, good)
        bus.put(Event(EventType.COMMAND, "开始游戏"))
        assert await bus.dispatch_next() is True
        assert got == ["开始游戏"]

    asyncio.run(main())
