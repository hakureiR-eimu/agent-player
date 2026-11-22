"""IM 接入模块本体（接口声明见 src/im/module.py，实现设计见 docs/prd/discord接入.md）。

harness 进程内两个 discord.py client（dm bot、gbr bot）跑在同一个事件循环里——回调与
事件队列同循环，无跨线程问题。收是被动：bot 在线收着（Gateway 长连接，心跳重连归
discord.py 管），滤 bot 账号后调主体注册的回调，模块零总线知识；发与读是主动：主体调
send_message（发玩家私信）、read_message（读私信历史）与 send_receipt（发回执到命令来的
频道）；本局频道（GreatBritain）的建、销与查也归本模块，转发给 dm bot 干。玩家一律用
Discord 用户 ID 的字符串指代——发回私信要拿它找频道。
"""

from __future__ import annotations

import asyncio
import logging

import discord

from config import Config
from im.impl.bots import BotCallbacks, DmBot, GbrBot
from im.module import CommandCallback, MessageCallback

logger = logging.getLogger(__name__)

# 登录后等 bot 在线的时限：超时按没连上处理（token 错或网络不通）
READY_TIMEOUT_SECONDS = 30.0

# 读私信历史的条数上限：只翻最近的，不读太多（更早的对话在 world/chat/ 落盘里）
DM_HISTORY_LIMIT = 100


class ImModuleImpl:
    """ImModule 协议（src/im/module.py）的实现：两个 bot 的登录、收、发。"""

    def __init__(self, config: Config) -> None:
        self._dm_token = config.dm_token
        self._gbr_token = config.gbr_token
        self._callbacks = BotCallbacks()
        self._dm = DmBot(self._callbacks, proxy=config.discord_proxy)
        self._gbr = GbrBot(self._callbacks, proxy=config.discord_proxy)
        self._tasks: list[asyncio.Task] = []

    # ---- 收（被动）：装配时挂回调，bot 收到即调 ----

    def on_command(self, callback: CommandCallback) -> None:
        self._callbacks.command = callback

    def on_message(self, callback: MessageCallback) -> None:
        self._callbacks.message = callback

    # ---- 发（主动）：主体调 ----

    async def _dm_channel(self, player: str) -> discord.DMChannel:
        """拿该玩家的私信频道：bot 记着（玩家私信过）直用；没记着就查到人开一个
        （前提：玩家与 bot 同服务器、玩家隐私设置允许 bot 私信）。"""
        channel = self._gbr.dm_channel_for(player)
        if channel is not None:
            return channel
        user = self._gbr.get_user(int(player))
        if user is None:
            user = await self._gbr.fetch_user(int(player))
        channel = await user.create_dm()
        self._gbr.remember_dm_channel(player, channel)
        return channel

    async def send_message(self, player: str, text: str) -> None:
        """把 agent 的话发到该玩家的私信频道。"""
        channel = await self._dm_channel(player)
        await channel.send(text)

    async def read_message(self, player: str) -> list[dict[str, str]]:
        """读与该玩家的私信频道里最近的消息（DM_HISTORY_LIMIT 条，从新到旧排——照
        Discord API 的顺序，最新的在最前）。"""
        channel = await self._dm_channel(player)
        messages: list[dict[str, str]] = []
        async for message in channel.history(limit=DM_HISTORY_LIMIT):
            messages.append(
                {
                    "author": message.author.display_name,
                    "text": message.content,
                    "time": message.created_at.isoformat(),
                }
            )
        return messages

    async def send_receipt(self, text: str) -> None:
        """把命令回执发到大厅频道原处（最近一条命令来的频道）。"""
        channel = self._dm.receipt_channel()
        if channel is None:
            raise RuntimeError("还没有命令来过，回执不知道发哪（回执发到命令来的频道）")
        await channel.send(text)

    # ---- 本局频道（GreatBritain）：转发给 dm bot ----

    async def has_channel(self) -> bool:
        return await self._dm.has_channel()

    async def create_channel(self) -> None:
        await self._dm.create_channel()

    async def destroy_channel(self) -> None:
        await self._dm.destroy_channel()

    # ---- 起停 ----

    async def start(self) -> None:
        """登录两个 bot（dm、gbr）、起 Gateway 长连接，等两个都在线。"""
        dm_token = self._dm_token
        gbr_token = self._gbr_token
        if not dm_token or not gbr_token:  # 直接判空：过了这道检查，类型上 token 就不是 None
            missing = [
                name
                for name, token in (("dm_token", dm_token), ("gbr_token", gbr_token))
                if not token
            ]
            raise RuntimeError(
                f"config.toml 缺 {'、'.join(missing)}：复制 config.example.toml 成 config.toml 填上"
            )
        try:
            await self._dm.login(dm_token)
            await self._gbr.login(gbr_token)
            self._tasks = [
                asyncio.create_task(self._dm.connect()),
                asyncio.create_task(self._gbr.connect()),
            ]
            for bot in (self._dm, self._gbr):
                await asyncio.wait_for(bot.wait_until_ready(), timeout=READY_TIMEOUT_SECONDS)
            logger.info("IM 接入连上 Discord：dm bot、gbr bot 都在线")
        except Exception:
            await self.stop()
            raise

    async def stop(self) -> None:
        for bot in (self._dm, self._gbr):
            if not bot.is_closed():
                await bot.close()
        if self._tasks:
            await asyncio.gather(*self._tasks, return_exceptions=True)
            self._tasks = []
