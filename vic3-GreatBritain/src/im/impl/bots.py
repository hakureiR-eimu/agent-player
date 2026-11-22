"""两个 bot（discord.py Client 子类）：dm bot 主持命令、gbr bot 是大不列颠玩家的门面。

收消息先滤 bot 账号（防互触发：回执、别的 bot、自己的消息一律不搭理），再按分工处理：
dm bot 只管服务器频道里 @ 自己的消息，命令词对白名单匹配，不认识的词直回固定提示
（Discord 侧的应酬话留在此层）；gbr bot 只管私信，在频道被 @ 直回一句固定指引。
dm bot 还管本局频道（GreatBritain）的建、销与查——开始新游戏建、保存并结束游戏销，
在哪个服务器操作取最近一条命令来的频道。免特权 intent：私信与 @ 到 bot 的消息不开
MESSAGE_CONTENT 也能读内容（见 Discord 官方 Gateway 文档），Intents.default() 即够。
设计见 docs/prd/discord接入.md。
"""

from __future__ import annotations

import logging
from typing import cast

import discord

from im.module import CommandCallback, MessageCallback

logger = logging.getLogger(__name__)

# dm bot 认的三条命令（白名单，命令词精确匹配）
COMMANDS = ("开始新游戏", "继续游戏", "保存并结束游戏")

# 本局频道名：开始新游戏建、保存并结束游戏销，频道在不在就是局挂没挂着的外显
CHANNEL_NAME = "GreatBritain"

UNKNOWN_COMMAND_HINT = "命令没认出来。我认这三条：开始新游戏、继续游戏、保存并结束游戏——@ 我加命令词。"
GUILD_MENTION_HINT = "公屏上我不聊天，有事私信我。"


class BotCallbacks:
    """装配时经模块的 on_command/on_message 挂进来的回调，模块转发给两个 bot 持有。"""

    def __init__(self) -> None:
        self.command: CommandCallback | None = None
        self.message: MessageCallback | None = None


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
    """主持 bot：公屏 @ 自己下命令。命中白名单调命令回调，不认识的词直回固定提示；
    本局频道（GreatBritain）的建、销与查也归它，操作的服务器取最近一条命令来的。"""

    def __init__(self, callbacks: BotCallbacks, proxy: str | None = None) -> None:
        super().__init__(callbacks, "dm bot", proxy)
        self._command_channel: discord.abc.Messageable | None = None
        self._command_guild: discord.Guild | None = None

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
            self._command_guild = message.guild  # 频道建销查在命令来的服务器
            if self._callbacks.command is not None:
                self._callbacks.command(phrase)
        else:
            logger.info("dm bot 收到没认出的命令词 %r（来自 %s）", phrase, message.author)
            await message.channel.send(UNKNOWN_COMMAND_HINT)

    def receipt_channel(self) -> discord.abc.Messageable | None:
        """回执的去处：最近一条命令来的频道。"""
        return self._command_channel

    # ---- 本局频道（GreatBritain）：建、销、查，主体按命令排着调 ----

    def find_channel(self, guild: discord.Guild) -> discord.TextChannel | None:
        """在服务器里找本局频道（名字不区分大小写），没有返回 None。"""
        for channel in guild.text_channels:
            if channel.name.casefold() == CHANNEL_NAME.casefold():
                return channel
        return None

    async def has_channel(self) -> bool:
        """查本局频道在不在——局挂没挂着的外显，主体用它挡命令。"""
        return self.find_channel(self._require_guild()) is not None

    async def create_channel(self) -> None:
        """建本局频道。已在（上次局没结束）报错——要不要建由主体先查，这里是兜底。"""
        guild = self._require_guild()
        if self.find_channel(guild) is not None:
            raise RuntimeError("GreatBritain 频道已在，先保存并结束游戏再开新的一局")
        await guild.create_text_channel(CHANNEL_NAME)
        logger.info("dm bot 建了本局频道 %s（服务器 %s）", CHANNEL_NAME, guild)

    async def destroy_channel(self) -> None:
        """销毁本局频道。没有可销的报错——主体先查过，这里是兜底。"""
        channel = self.find_channel(self._require_guild())
        if channel is None:
            raise RuntimeError("没有 GreatBritain 频道可销毁")
        await channel.delete()
        logger.info("dm bot 销毁了本局频道 %s", CHANNEL_NAME)

    def _require_guild(self) -> discord.Guild:
        """频道操作所在的服务器：最近一条命令来的。还没命令来过就明确报错。"""
        if self._command_guild is None:
            raise RuntimeError("还没有命令来过，不知道在哪个服务器操作频道")
        return self._command_guild


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
        # guild 为 None 的消息必来自私信频道（bot 进不了群聊私信）——类型标注表达不了这层
        # 关联，cast 落实，字典照记 DMChannel
        self._dm_channels[player] = cast(discord.DMChannel, message.channel)  # 回复发回这里
        logger.info("gbr bot 收到私信（来自 %s）：%s", message.author, message.content)
        if self._callbacks.message is not None:
            self._callbacks.message(player, message.content)

    def dm_channel_for(self, player: str) -> discord.DMChannel | None:
        return self._dm_channels.get(player)

    def remember_dm_channel(self, player: str, channel: discord.DMChannel) -> None:
        """记下玩家的私信频道（send_message/read_message 给没私信过的玩家开频道后记下，下次直用）。"""
        self._dm_channels[player] = channel
