"""调度单测：三条命令的动作顺序、局状态流转（本局频道＋会话）、边界拒绝（频道已在不能再
开始、没频道不能结束）、命令走总线到执行。替身模块见 conftest。"""

import asyncio

import pytest
from conftest import RecordingAgentModule, RecordingGame, RecordingIm

from dispatcher import CommandError, Dispatcher
from events import Event, EventBus, EventType


def make_sut(tmp_path):
    """构造一条带替身模块的调度：bus ＋ Dispatcher ＋ 三个替身，共写一份 calls；GBR 落临时目录。"""
    calls: list = []
    bus = EventBus()
    game = RecordingGame(calls)
    agent = RecordingAgentModule(calls)
    im = RecordingIm(calls)
    dispatcher = Dispatcher(bus, game, agent, im, gbr_dir=tmp_path / "GBR")
    return bus, dispatcher, im, calls


def drain(bus: EventBus) -> None:
    async def main():
        while await bus.dispatch_next():
            pass

    asyncio.run(main())


def test_开始游戏_建本局频道起全新会话(tmp_path):
    _, dispatcher, im, calls = make_sut(tmp_path)
    asyncio.run(dispatcher.execute_command("开始游戏"))
    assert calls == ["im.create_channel", "agent.start_session"]
    assert dispatcher.session_running is True
    assert im.channel_exists is True  # 频道建了，局挂着


def test_开始游戏_频道已在拒绝(tmp_path):
    _, dispatcher, im, calls = make_sut(tmp_path)
    im.channel_exists = True  # 上次局没结束，频道还挂着
    with pytest.raises(CommandError):
        asyncio.run(dispatcher.execute_command("开始游戏"))
    assert calls == []  # 频道不动、会话不起


def test_开始游戏_agent未建不建频道(tmp_path):
    calls: list = []
    bus = EventBus()
    game = RecordingGame(calls)
    im = RecordingIm(calls)
    dispatcher = Dispatcher(bus, game, None, im, gbr_dir=tmp_path / "GBR")
    with pytest.raises(CommandError) as info:
        asyncio.run(dispatcher.execute_command("开始游戏"))
    assert "agent 模块未建" in str(info.value)
    assert calls == []  # 报未实现在建频道之前，频道没建
    assert dispatcher.session_running is False


def test_会话在跑再开始游戏拒绝(tmp_path):
    _, dispatcher, _, calls = make_sut(tmp_path)
    asyncio.run(dispatcher.execute_command("开始游戏"))
    calls.clear()
    with pytest.raises(CommandError):
        asyncio.run(dispatcher.execute_command("开始游戏"))
    assert calls == []


def test_保存游戏_会话收尾频道留着(tmp_path):
    _, dispatcher, im, calls = make_sut(tmp_path)
    asyncio.run(dispatcher.execute_command("开始游戏"))
    calls.clear()
    asyncio.run(dispatcher.execute_command("保存游戏"))
    assert calls == ["agent.stop_session"]
    assert dispatcher.session_running is False
    assert im.channel_exists is True  # 局还挂着，频道不动


def test_保存游戏_没在跑不动(tmp_path):
    _, dispatcher, _, calls = make_sut(tmp_path)
    asyncio.run(dispatcher.execute_command("保存游戏"))
    assert calls == []
    assert dispatcher.session_running is False


def test_结束游戏_会话在跑先收尾再销频道清GBR(tmp_path):
    _, dispatcher, im, calls = make_sut(tmp_path)
    gbr = tmp_path / "GBR"
    gbr.mkdir()
    (gbr / "memory.md").write_text("这一局的记忆", encoding="utf-8")
    asyncio.run(dispatcher.execute_command("开始游戏"))
    calls.clear()

    asyncio.run(dispatcher.execute_command("结束游戏"))

    assert calls == ["agent.stop_session", "im.destroy_channel"]
    assert dispatcher.session_running is False
    assert im.channel_exists is False
    assert not gbr.exists()  # 这局彻底完，GBR 清掉


def test_结束游戏_保存过的局只销频道清GBR(tmp_path):
    _, dispatcher, _, calls = make_sut(tmp_path)
    gbr = tmp_path / "GBR"
    gbr.mkdir()
    asyncio.run(dispatcher.execute_command("开始游戏"))
    asyncio.run(dispatcher.execute_command("保存游戏"))
    calls.clear()

    asyncio.run(dispatcher.execute_command("结束游戏"))

    assert calls == ["im.destroy_channel"]  # 会话早收尾了，只销频道清 GBR
    assert not gbr.exists()


def test_结束游戏_没频道拒绝(tmp_path):
    _, dispatcher, _, calls = make_sut(tmp_path)
    gbr = tmp_path / "GBR"
    gbr.mkdir()
    with pytest.raises(CommandError):
        asyncio.run(dispatcher.execute_command("结束游戏"))
    assert calls == []
    assert gbr.exists()  # GBR 也没动


def test_未知命令拒绝(tmp_path):
    _, dispatcher, _, calls = make_sut(tmp_path)
    with pytest.raises(CommandError):
        asyncio.run(dispatcher.execute_command("重开游戏"))
    assert calls == []


def test_command事件走总线到命令执行并回执(tmp_path):
    bus, dispatcher, _, calls = make_sut(tmp_path)

    async def main():
        bus.put(Event(EventType.COMMAND, "开始游戏"))
        await bus.dispatch_next()

    asyncio.run(main())
    assert dispatcher.session_running is True
    assert calls == ["im.create_channel", "agent.start_session", ("im.send_receipt", "开始游戏 执行完成")]


def test_command事件没执行成回执带原因(tmp_path):
    bus, _, _, calls = make_sut(tmp_path)

    async def main():
        bus.put(Event(EventType.COMMAND, "重开游戏"))
        await bus.dispatch_next()

    asyncio.run(main())
    assert calls == [("im.send_receipt", "命令没执行成：未知命令：重开游戏")]


def test_shutdown_会话在跑先按保存游戏收尾(tmp_path):
    _, dispatcher, im, calls = make_sut(tmp_path)
    gbr = tmp_path / "GBR"
    gbr.mkdir()
    asyncio.run(dispatcher.execute_command("开始游戏"))
    calls.clear()
    asyncio.run(dispatcher.shutdown())
    assert calls == ["agent.stop_session"]
    assert im.channel_exists is True  # 进程退出不是局结束，频道与 GBR 都不动
    assert gbr.exists()


def test_shutdown_没在跑不动(tmp_path):
    _, dispatcher, _, calls = make_sut(tmp_path)
    asyncio.run(dispatcher.shutdown())
    assert calls == []
