"""game 模块集成测试（在 VSCode 测试面板里点跑——命令行全量跑默认排除集成测试，
面板的 pytestArgs 已配 --override-ini=addopts= 绕开排除）。

前提：Victoria 3 在跑（mod 装好），配置用开发文件夹下的 config.toml（不建即默认，
默认值即真实值）——游戏没跑时测试立即失败并报错。三个测试对应游戏接入的三个能力，
结束时打印各自测了什么：

1. 读取世界局势（get_state）
2. 发动外交博弈（start_play，写侧占位）
3. 接收新年事件（new_year）

第三个要等游戏内过一年：error.log 里已有本局记录时，主体的年度节拍数秒内即推（首轮
把已察觉的当前年份推出来）；还没有本局记录时（新开局第一年），等游戏跑完当年才推。
默认等 5 分钟，可用环境变量 INTEGRATION_NEW_YEAR_WAIT_SECONDS 调整。
"""

import asyncio
import contextlib
import os
import time

import pytest

from config import load_config
from events import Event, EventBus, EventType
from game.impl.module import GameModuleImpl
from game.impl.process import game_running
from main import poll_new_year

pytestmark = pytest.mark.integration

WAIT_SECONDS = int(os.environ.get("INTEGRATION_NEW_YEAR_WAIT_SECONDS", "300"))


def require_game_running() -> None:
    """三个测试的共同前提：游戏没在跑就立刻失败——年度通知测试不先查会白等几分钟。"""
    config = load_config()
    if not game_running(config.game_process):
        pytest.fail(f"游戏未在跑：进程表里没有 {config.game_process}，先启动 Victoria 3 再跑集成测试")


def test_get_state_reads_world_situation():
    """读取世界局势：get_state 从真 error.log 拼出世界格局快照。"""
    require_game_running()
    snapshot = GameModuleImpl(load_config()).get_state()

    assert snapshot["powers"], "一条国家记录都没读到——error.log 里有本局记录吗？"
    assert snapshot["gbr_finance"], "没读到 GBR 财政记录"
    print(f"\n本测试测了：读取世界局势——get_state 读出 {len(snapshot['powers'])} 国记录与 GBR 财政")


def test_start_play_returns_response():
    """发动外交博弈：start_play 打真游戏侧（写侧占位，返回占位应答）。"""
    require_game_running()
    response = GameModuleImpl(load_config()).start_play()

    assert response, "start_play 没返回应答"
    print(f"\n本测试测了：发动外交博弈——start_play 返回：{response}")


def test_new_year_event_arrives():
    """接收新年事件：起主体的年度节拍＋事件总线主循环，收到 new_year 事件。"""
    require_game_running()

    async def scenario() -> list[Event]:
        bus = EventBus()
        received: list[Event] = []

        async def record(event: Event) -> None:
            received.append(event)

        bus.subscribe(EventType.NEW_YEAR, record)
        module = GameModuleImpl(load_config())
        poll_task = asyncio.create_task(poll_new_year(bus, module))
        loop_task = asyncio.create_task(bus.run())
        deadline = time.monotonic() + WAIT_SECONDS
        try:
            while not received and time.monotonic() < deadline:
                await asyncio.sleep(1)
        finally:
            loop_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await loop_task
            poll_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await poll_task
        return received

    received = asyncio.run(scenario())

    assert received, (
        f"{WAIT_SECONDS}s 内没收到 new_year 事件——游戏在跑吗？一年推一次；"
        "等待时长可用环境变量 INTEGRATION_NEW_YEAR_WAIT_SECONDS 调整"
    )
    assert received[0].type is EventType.NEW_YEAR
    assert isinstance(received[0].data, int)
    print(f"\n本测试测了：接收新年事件——收到 {len(received)} 个：{[event.data for event in received]}")
