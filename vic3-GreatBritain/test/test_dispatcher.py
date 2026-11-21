"""调度单测：三条命令的动作顺序、局状态流转、命令走总线到执行。替身模块见 conftest。"""

import asyncio

import pytest
from conftest import RecordingAgentModule, RecordingGame, RecordingIm

from dispatcher import CommandError, Dispatcher
from events import Event, EventBus, EventType


def make_sut():
    """构造一条带替身模块的调度：bus ＋ Dispatcher ＋ 三个替身，共写一份 calls。"""
    calls: list = []
    bus = EventBus()
    game = RecordingGame(calls)
    agent = RecordingAgentModule(calls)
    im = RecordingIm(calls)
    dispatcher = Dispatcher(bus, game, agent, im)
    return bus, dispatcher, calls


def drain(bus: EventBus) -> None:
    async def main():
        while await bus.dispatch_next():
            pass

    asyncio.run(main())


def test_startGame_建全新GBR起会话接上两块():
    _, dispatcher, calls = make_sut()
    asyncio.run(dispatcher.execute_command("startGame"))
    assert calls == [("agent.start_session", True)]
    assert dispatcher.session_running is True


def test_loadGame_用已有GBR起会话接上两块():
    _, dispatcher, calls = make_sut()
    asyncio.run(dispatcher.execute_command("loadGame"))
    assert calls == [("agent.start_session", False)]
    assert dispatcher.session_running is True


def test_会话在跑再startGame拒绝():
    _, dispatcher, calls = make_sut()
    asyncio.run(dispatcher.execute_command("startGame"))
    calls.clear()
    with pytest.raises(CommandError):
        asyncio.run(dispatcher.execute_command("startGame"))
    assert calls == []


def test_会话在跑再loadGame拒绝():
    _, dispatcher, calls = make_sut()
    asyncio.run(dispatcher.execute_command("loadGame"))
    calls.clear()
    with pytest.raises(CommandError):
        asyncio.run(dispatcher.execute_command("loadGame"))
    assert calls == []


def test_stopGame_会话整理后结束():
    _, dispatcher, calls = make_sut()
    asyncio.run(dispatcher.execute_command("startGame"))
    calls.clear()
    asyncio.run(dispatcher.execute_command("stopGame"))
    assert calls == ["agent.stop_session"]
    assert dispatcher.session_running is False


def test_stopGame_没在跑不动():
    _, dispatcher, calls = make_sut()
    asyncio.run(dispatcher.execute_command("stopGame"))
    assert calls == []
    assert dispatcher.session_running is False


def test_未知命令拒绝():
    _, dispatcher, calls = make_sut()
    with pytest.raises(CommandError):
        asyncio.run(dispatcher.execute_command("restartGame"))
    assert calls == []


def test_command事件走总线到命令执行并回执():
    bus, dispatcher, calls = make_sut()

    async def main():
        bus.put(Event(EventType.COMMAND, "startGame"))
        await bus.dispatch_next()

    asyncio.run(main())
    assert dispatcher.session_running is True
    assert calls == [("agent.start_session", True), ("im.send_receipt", "startGame 执行完成")]


def test_command事件没执行成回执带原因():
    bus, _, calls = make_sut()

    async def main():
        bus.put(Event(EventType.COMMAND, "restartGame"))
        await bus.dispatch_next()

    asyncio.run(main())
    assert calls == [("im.send_receipt", "命令没执行成：未知命令：restartGame")]


def test_agent未建时起会话命令明确报未实现():
    calls: list = []
    bus = EventBus()
    game = RecordingGame(calls)
    im = RecordingIm(calls)
    dispatcher = Dispatcher(bus, game, None, im)
    with pytest.raises(CommandError) as info:
        asyncio.run(dispatcher.execute_command("startGame"))
    assert "agent 模块未建" in str(info.value)
    assert calls == []
    assert dispatcher.session_running is False


def test_shutdown_会话在跑先按stopGame收尾():
    _, dispatcher, calls = make_sut()
    asyncio.run(dispatcher.execute_command("startGame"))
    calls.clear()
    asyncio.run(dispatcher.shutdown())
    assert calls == ["agent.stop_session"]


def test_shutdown_没在跑不动():
    _, dispatcher, calls = make_sut()
    asyncio.run(dispatcher.shutdown())
    assert calls == []
