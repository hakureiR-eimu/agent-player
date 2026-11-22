"""game 模块集成测试（在 VSCode 测试面板里点跑——命令行全量跑默认排除集成测试，
面板的 pytestArgs 已配 --override-ini=addopts= 绕开排除）。

前提：Victoria 3 在跑（mod 装好），配置用开发文件夹下的 config.toml（不建即默认，
默认值即真实值）——游戏没跑时测试立即失败并报错。三个测试对应游戏接入的三个能力：

1. 读取世界局势（get_state）：读到真实世界格局快照
2. 发动外交博弈（start_play）：写侧占位，返回固定的"未实现"应答
3. 收到年度通知推送（new_year）：订阅事件总线，收到游戏年份前进的推送

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
from game.impl.module import GameModuleImpl, GameNotRunningError
from game.impl.process import game_running
from main import poll_new_year

pytestmark = pytest.mark.integration

WAIT_SECONDS = int(os.environ.get("INTEGRATION_NEW_YEAR_WAIT_SECONDS", "300"))


def require_game_running() -> None:
    """三个测试的共同前提：游戏没在跑就立刻失败——年度通知测试不先查会白等几分钟。"""
    config = load_config()
    if not game_running(config.game_process):
        pytest.fail(f"游戏未在跑：进程表里没有 {config.game_process}，先启动 Victoria 3 再跑集成测试")


def test_get_state_reads_real_world_snapshot():
    """能力一 读取世界局势：游戏在跑时，get_state 返回真实世界格局快照。"""
    module = GameModuleImpl(load_config())
    try:
        snapshot = module.get_state()
    except GameNotRunningError as e:
        pytest.fail(f"游戏未在跑：{e}")

    print(f"\nget_state() —— powers（{len(snapshot['powers'])} 国，按名次）：")
    for power in snapshot["powers"]:
        print(
            f"  {power['rank']:>2}  {power['tag']}  {power['year']}  "
            f"gdp={power['gdp']:.0f}  army={power['army']}"
        )
    fin = snapshot["gbr_finance"]
    if fin:
        print(
            f"GBR 财政 {fin['year']}：金库={fin['gold']:.0f} "
            f"债务本金={fin['debt']:.0f} 周净收支={fin['week_net']:.0f}"
        )
    assert snapshot["powers"], "一条国家记录都没读到——error.log 里有本局记录吗？"
    assert fin, "没读到 GBR 财政记录"


def test_start_play_returns_fixed_not_implemented_response():
    """能力二 发动外交博弈：写侧占位方法，返回固定的"未实现"应答。"""
    module = GameModuleImpl(load_config())
    try:
        response = module.start_play()
    except GameNotRunningError as e:
        pytest.fail(f"游戏未在跑：{e}")

    print(f"\nstart_play() —— {response}")
    assert "未实现" in response


def test_new_year_event_arrives_when_game_year_advances():
    """能力三 收到年度通知推送：起主体的年度节拍＋事件总线主循环，收到 new_year 事件。"""
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

    print(f"\nnew_year 事件（等了最多 {WAIT_SECONDS}s，收到 {len(received)} 个）：")
    for event in received:
        print(f"  {event.type.value} → {event.data}")
    assert received, (
        f"{WAIT_SECONDS}s 内没收到 new_year 事件——游戏在跑吗？一年推一次；"
        "等待时长可用环境变量 INTEGRATION_NEW_YEAR_WAIT_SECONDS 调整"
    )
    assert received[0].type is EventType.NEW_YEAR
    assert isinstance(received[0].data, int)
