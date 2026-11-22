"""IM 模块集成测试（在 VSCode 测试面板里点跑——命令行全量跑默认排除集成测试，
面板的 pytestArgs 已配 --override-ini=addopts= 绕开排除）。

前提：开发文件夹下的 config.toml 填好 dm_token、gbr_token，代理能到 Discord——前提
没满足时测试立即失败并报错。一个测试盖 IM 接入的两头：

1. 收（回调）：在公屏 @ dm bot 下一条命令（开始游戏 / 保存游戏 / 结束游戏 任一）、给
   gbr bot 发一条私信，回调应真的收到
2. 发（send_message）：测试用收到的私信里带的玩家回话——Discord 上应看到回执落回
   公屏原处、回话落回私信

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


def test_收命令与私信后回话discord上看得到():
    """收（回调）与发（send_message）：公屏 @ dm bot 下命令、私信 gbr bot，回调应收到；再用私信里带的玩家回话，两头都看得到。"""
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
            # 回话：回执发回公屏原处、回复发给私信里带的玩家——Discord 上应看得到
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
