"""IM 模块集成测试（在 VSCode 测试面板里点跑——命令行全量跑默认排除集成测试，
面板的 pytestArgs 已配 --override-ini=addopts= 绕开排除）。

前提：开发文件夹下的 config.toml 填好 dm_token、gbr_token 与 player_id（私信发给
player_id 这位人类玩家），代理能到 Discord——前提没满足时测试立即失败并报错。
两个测试对应 IM 接入的两头：

1. 发（send_message）：起两个真 bot，给玩家发私信——Discord 上应真的收到 gbr bot 的私信
2. 收（回调）：在公屏 @ dm bot 下一条命令（开始游戏 / 保存游戏 / 结束游戏 任一）、给
   gbr bot 发一条私信，回调应真的收到；测试再用 send_receipt / send_message 回话，Discord
   上能看到回执落回公屏原处、回话落回私信

等待时长默认 300 秒，环境变量 INTEGRATION_IM_WAIT_SECONDS 可调。
"""

import asyncio
import os
import time

import pytest

from config import load_config
from im.impl.module import ImModuleImpl

pytestmark = pytest.mark.integration

WAIT_SECONDS = int(os.environ.get("INTEGRATION_IM_WAIT_SECONDS", "300"))


def require_config() -> None:
    config = load_config()
    missing = [name for name, token in (("dm_token", config.dm_token), ("gbr_token", config.gbr_token)) if not token]
    if missing:
        pytest.fail(f"config.toml 缺 {'、'.join(missing)}：复制 config.example.toml 成 config.toml 填上")


def require_player_id() -> str:
    """收信人：环境变量 INTEGRATION_DISCORD_PLAYER_ID 优先（临时换人用），没有则取
    config.toml 的 player_id——面板点跑不带环境变量，config 是常规路径。"""
    player = os.environ.get("INTEGRATION_DISCORD_PLAYER_ID", "") or load_config().player_id
    if not player:
        pytest.fail("不知道私信发给谁：环境变量 INTEGRATION_DISCORD_PLAYER_ID 没填，config.toml 的 player_id 也是空——填上其一（人类玩家的 Discord 用户 ID，开发者模式右键头像复制）")
    return player


def test_send_message_给人发私信discord上收得到():
    """能力一 发（send_message）：起两个真 bot，给玩家发私信，Discord 上应收到。"""
    require_config()
    player = require_player_id()

    async def scenario() -> None:
        im = ImModuleImpl(load_config())
        await im.start()
        try:
            await im.send_message(player, "集成测试：这是 gbr bot 通过 send_message 发出的私信")
        finally:
            await im.stop()

    asyncio.run(scenario())


def test_收命令与私信后回话discord上看得到():
    """能力二 收（回调）：公屏 @ dm bot 下命令、私信 gbr bot，回调应收到；再回话两头都看得到。"""
    require_config()
    received: dict[str, list] = {"command": [], "message": []}

    async def scenario() -> dict[str, list]:
        im = ImModuleImpl(load_config())
        im.on_command(lambda command: received["command"].append(command))
        im.on_message(lambda player, text: received["message"].append((player, text)))
        await im.start()
        print(f"\n请在 Discord 做两件事（限时 {WAIT_SECONDS}s）：")
        print("  1. 公屏 @ dm bot 下一条命令（如：@ dm bot 开始游戏）")
        print("  2. 给 gbr bot 发一条私信")
        deadline = time.monotonic() + WAIT_SECONDS
        try:
            while (
                not received["command"] or not received["message"]
            ) and time.monotonic() < deadline:
                await asyncio.sleep(1)
        finally:
            # 回话：回执发回公屏原处、回复发回玩家私信——Discord 上应看得到
            if received["command"]:
                await im.send_receipt(f"收到命令：{received['command'][0]}")
            if received["message"]:
                player, text = received["message"][0]
                await im.send_message(player, f"收到私信：{text}")
            await im.stop()
        return received

    asyncio.run(scenario())

    print(f"\n收到的命令：{received['command']}")
    print(f"收到的私信：{received['message']}")
    assert received["command"], f"{WAIT_SECONDS}s 内没收到命令——在公屏 @ dm bot 下了吗？"
    assert received["command"][0] in ("开始游戏", "保存游戏", "结束游戏")
    assert received["message"], f"{WAIT_SECONDS}s 内没收到私信——给 gbr bot 发了吗？"
