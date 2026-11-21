"""两个 bot（discord.py Client 子类）：dm bot 主持命令、gbr bot 是大不列颠玩家的门面。

收消息先滤 bot 账号（防互触发：回执、别的 bot、自己的消息一律不搭理），再按分工处理：
dm bot 只管服务器频道里 @ 自己的消息，命令词对白名单匹配，不认识的词直回固定提示
（Discord 侧的应酬话留在此层）；gbr bot 只管私信，在频道被 @ 直回一句固定指引。
免特权 intent：私信与 @ 到 bot 的消息不开 MESSAGE_CONTENT 也能读内容（见 Discord 官方
Gateway 文档），Intents.default() 即够。设计见 docs/prd/discord接入.md。
"""

from __future__ import annotations

import logging
from typing import Callable

import discord

logger = logging.getLogger(__name__)

# dm bot 认的三条命令（白名单，命令词精确匹配）
COMMANDS = ("开始新游戏", "继续游戏", "保存游戏")

UNKNOWN_COMMAND_HINT = "命令没认出来。我认这三条：开始新游戏、继续游戏、保存游戏——@ 我加命令词。"
GUILD_MENTION_HINT = "公屏上我不聊天，有事私信我。"


class BotCallbacks:
    """装配时经模块的 on_command/on_message 挂进来的回调，模块转发给两个 bot 持有。"""

    def __init__(self) -> None:
        self.command: Callable[[str], None] | None = None
        self.message: Callable[[str, str], None] | None = None


def strip_mention(content: str, self_id: int) -> str | None:
    """剥掉对本 bot 的 @ 前缀（<@id> 与带昵称标记的 <@!id>），返回剩余正文。

    正文不是 @ 本 bot 开头返回 None（没被 @ 到、@ 的是别的 bot 都算没叫到它）。
    """
    text = content.strip()
    for prefix in (f"<@{self_id}>", f"<@!{self_id}>"):
        if text.startswith(prefix):
            return text[len(prefix) :].strip()
    return None


class BotBase(discord.Client):
    """公共底子：构造时存回调，on_message 里滤 bot 账号再交子类处理。"""

    def __init__(self, callbacks: BotCallbacks, name: str, proxy: str | None = None) -> None:
        # proxy：网络直连不到 discord.com 时走本地代理（REST 登录与 Gateway 长连接都走它）；
        # 代理软件开 TUN 接管时整个进程的路由都被接管，填 None 直连即可
        super().__init__(intents=discord.Intents.default(), proxy=proxy)
        self._callbacks = callbacks
        self._name = name

    async def on_ready(self) -> None:
        logger.info("%s 已登录 Discord：%s", self._name, self.user)

    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return
        await self.handle(message)

    async def handle(self, message: discord.Message) -> None:
        raise NotImplementedError


class DmBot(BotBase):
    """主持 bot：公屏 @ 自己下命令。命中白名单调命令回调，不认识的词直回固定提示。"""

    def __init__(self, callbacks: BotCallbacks, proxy: str | None = None) -> None:
        super().__init__(callbacks, "dm bot", proxy)
        self._command_channel: discord.abc.Messageable | None = None

    async def handle(self, message: discord.Message) -> None:
        if message.guild is None:
            return  # 私信不归主持 bot 管，不搭理
        if self.user is None:
            return
        phrase = strip_mention(message.content, self.user.id)
        if phrase is None:
            return  # 没 @ 本 bot，不搭话
        if phrase in COMMANDS:
            logger.info("dm bot 收到命令 %s（来自 %s）", phrase, message.author)
            self._command_channel = message.channel  # 回执发到命令来的频道
            if self._callbacks.command is not None:
                self._callbacks.command(phrase)
        else:
            logger.info("dm bot 收到没认出的命令词 %r（来自 %s）", phrase, message.author)
            await message.channel.send(UNKNOWN_COMMAND_HINT)

    def receipt_channel(self) -> discord.abc.Messageable | None:
        """回执的去处：最近一条命令来的频道。"""
        return self._command_channel


class GbrBot(BotBase):
    """大不列颠玩家的门面：私信交消息回调，公屏被 @ 直回固定指引（请私信我）。"""

    def __init__(self, callbacks: BotCallbacks, proxy: str | None = None) -> None:
        super().__init__(callbacks, "gbr bot", proxy)
        self._dm_channels: dict[str, discord.DMChannel] = {}

    async def handle(self, message: discord.Message) -> None:
        if message.guild is not None:
            if self.user is not None and strip_mention(message.content, self.user.id) is not None:
                await message.channel.send(GUILD_MENTION_HINT)
            return
        player = str(message.author.id)
        self._dm_channels[player] = message.channel  # 记下私信频道，回复发回这里
        logger.info("gbr bot 收到私信（来自 %s）：%s", message.author, message.content)
        if self._callbacks.message is not None:
            self._callbacks.message(player, message.content)

    def dm_channel_for(self, player: str) -> discord.DMChannel | None:
        return self._dm_channels.get(player)

    def remember_dm_channel(self, player: str, channel: discord.DMChannel) -> None:
        """记下玩家的私信频道（send_reply 给没私信过的玩家开频道后记下，下次直用）。"""
        self._dm_channels[player] = channel
