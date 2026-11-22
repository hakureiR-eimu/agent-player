"""IM 模块集成测试（在 VSCode 测试面板里点跑——命令行全量跑默认排除集成测试，
面板的 pytestArgs 已配 --override-ini=addopts= 绕开排除）。

前提：开发文件夹下的 config.toml 填好 dm_token、gbr_token，代理能到 Discord——前提
没满足时测试立即失败并报错。player_id 在玩家发来消息以前无从得知（值要从收到的
消息里学），所以两项测试都等人先动手、bot 收到后再回话，结束时打印各自测了什么：

1. dm bot 收命令回回执：人在服务器频道 @ dm bot 下命令，dm bot 在同一频道回"收到命令"
2. gbr bot 收私信回私信：人私信 gbr bot，gbr bot 反向私信"收到消息"

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


def test_dm_bot_replies_receipt_in_channel():
    """dm bot 收命令回回执：人在服务器频道 @ dm bot 下命令，回执落回同一频道。"""
    require_config()
    received: list[str] = []

    async def scenario() -> str:
        im = ImModuleImpl(load_config())
        im.on_command(lambda command: received.append(command))
        await im.start()
        print(f"\n请在 Discord 服务器频道 @ dm bot 下一条命令（限时 {WAIT_SECONDS}s）")
        deadline = time.monotonic() + WAIT_SECONDS
        try:
            while not received and time.monotonic() < deadline:
                await asyncio.sleep(1)
            if received:
                await im.send_receipt(f"收到命令：{received[0]}")
        finally:
            await im.stop()
        return received[0] if received else ""

    command = asyncio.run(scenario())

    print(f"\nDM收到命令：{command}")
    print("本测试测了：dm bot 在服务器频道收命令，回执发回同一频道")
    assert command, f"{WAIT_SECONDS}s 内没收到命令——在服务器频道 @ dm bot 下了吗？"


def test_gbr_bot_replies_dm_to_player():
    """gbr bot 收私信回私信：人私信 gbr bot，回话定向私信里带的玩家发回去。"""
    require_config()
    received: list[tuple[str, str]] = []

    async def scenario() -> tuple[str, str]:
        im = ImModuleImpl(load_config())
        im.on_message(lambda player, text: received.append((player, text)))
        await im.start()
        print(f"\n请给 gbr bot 发一条 Discord 私信（限时 {WAIT_SECONDS}s）")
        deadline = time.monotonic() + WAIT_SECONDS
        try:
            while not received and time.monotonic() < deadline:
                await asyncio.sleep(1)
            if received:
                player, text = received[0]
                await im.send_message(player, f"收到消息：{text}")
        finally:
            await im.stop()
        return received[0] if received else ("", "")

    player, text = asyncio.run(scenario())

    print(f"\nGBR收到消息：{text}（来自玩家 {player}）")
    print("本测试测了：gbr bot 收玩家私信，用私信里带的 player_id 定向回话")
    assert text, f"{WAIT_SECONDS}s 内没收到私信——给 gbr bot 发了吗？"
