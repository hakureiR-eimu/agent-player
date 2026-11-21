"""im 模块单测：命令解析（@ 前缀剥离、白名单）、回调分发（喂假消息断言回调收到、bot 账号
被滤）、发送方法（回执发到命令来的频道、回复发回玩家私信）、本局频道的建销查（假服务器）。

喂的是假消息（自含 FakeUser/FakeChannel/FakeMessage/FakeGuild，只带 bot 会用的字段）；
bot 的 self.user 登录后才有值，单测直接往 _connection.user 里塞。模块方法走真路径：
白名单、滤账号、频道记账都是实现本体，不造 mock。
"""

import asyncio
from dataclasses import dataclass, field

import pytest

from config import load_config
from im.impl.bots import (
    COMMANDS,
    GUILD_MENTION_HINT,
    UNKNOWN_COMMAND_HINT,
    BotCallbacks,
    DmBot,
    GbrBot,
    strip_mention,
)
from im.impl.module import ImModuleImpl

SELF_ID = 100  # 单测里两个 bot 的自我身份（塞进 _connection.user 的假用户 ID）


@dataclass
class FakeUser:
    id: int
    bot: bool = False


@dataclass
class FakeChannel:
    sent: list = field(default_factory=list)
    guild: object | None = None

    async def send(self, text: str) -> None:
        self.sent.append(text)


@dataclass
class FakeMessage:
    author: FakeUser
    content: str
    channel: FakeChannel
    guild: object | None  # None 即私信，非 None 即服务器频道


@dataclass
class FakeTextChannel:
    """服务器里的文字频道：名字＋销毁标记（dm bot 建销本局频道用）。"""

    name: str
    deleted: bool = False

    async def delete(self) -> None:
        self.deleted = True


@dataclass
class FakeGuild:
    """假服务器：记现有的频道与新建的频道（dm bot 建频道用）。"""

    channels: list = field(default_factory=list)
    created: list = field(default_factory=list)

    @property
    def text_channels(self) -> list:
        return [channel for channel in self.channels if not channel.deleted]

    async def create_text_channel(self, name: str) -> FakeTextChannel:
        channel = FakeTextChannel(name)
        self.channels.append(channel)
        self.created.append(name)
        return channel


def make_dm_bot(callbacks: BotCallbacks | None = None) -> DmBot:
    bot = DmBot(callbacks or BotCallbacks())
    bot._connection.user = FakeUser(id=SELF_ID)  # discord.py 登录后 self.user 才有值，单测直接塞
    return bot


def make_gbr_bot(callbacks: BotCallbacks | None = None) -> GbrBot:
    bot = GbrBot(callbacks or BotCallbacks())
    bot._connection.user = FakeUser(id=SELF_ID)
    return bot


def dm_message(content: str, *, author_id: int = 7, channel: FakeChannel | None = None) -> FakeMessage:
    """公屏消息（guild 非 None），频道不传给个新的。"""
    return FakeMessage(FakeUser(id=author_id), content, channel or FakeChannel(), guild=object())


def direct_message(content: str, *, author_id: int = 7, channel: FakeChannel | None = None) -> FakeMessage:
    """私信（guild 为 None）。"""
    return FakeMessage(FakeUser(id=author_id), content, channel or FakeChannel(), guild=None)


# ---- 命令解析：@ 前缀剥离（strip_mention 是纯函数，白名单匹配在 dm bot 流程里验） ----


def test_strip_mention_剥掉普通与昵称两种前缀():
    assert strip_mention(f"<@{SELF_ID}> 开始游戏", SELF_ID) == "开始游戏"
    assert strip_mention(f"<@!{SELF_ID}> 结束游戏 ", SELF_ID) == "结束游戏"
    assert strip_mention(f"  <@{SELF_ID}>   保存游戏  ", SELF_ID) == "保存游戏"
    assert strip_mention(f"<@{SELF_ID}>", SELF_ID) == ""


def test_strip_mention_没到本bot返回None():
    assert strip_mention(f"<@999> 开始游戏", SELF_ID) is None  # @ 的是别的 bot
    assert strip_mention("开始游戏", SELF_ID) is None  # 根本没 @
    assert strip_mention("开始游戏 <@100>", SELF_ID) is None  # @ 不在开头不算叫它


# ---- 回调分发：dm bot（公屏命令） ----


def test_dm_bot_公屏命中白名单调命令回调并记回执去处():
    commands: list = []
    callbacks = BotCallbacks()
    callbacks.command = commands.append
    bot = make_dm_bot(callbacks)
    lobby = FakeChannel()

    asyncio.run(bot.on_message(dm_message(f"<@{SELF_ID}> 开始游戏", channel=lobby)))

    assert commands == ["开始游戏"]
    assert bot.receipt_channel() is lobby


def test_dm_bot_白名单三条都认():
    callbacks = BotCallbacks()
    commands: list = []
    callbacks.command = commands.append
    bot = make_dm_bot(callbacks)
    for command in COMMANDS:
        asyncio.run(bot.on_message(dm_message(f"<@{SELF_ID}> {command}")))
    assert commands == ["开始游戏", "保存游戏", "结束游戏"]


def test_dm_bot_不认识的词直回固定提示不调回调():
    commands: list = []
    callbacks = BotCallbacks()
    callbacks.command = commands.append
    bot = make_dm_bot(callbacks)
    lobby = FakeChannel()

    asyncio.run(bot.on_message(dm_message(f"<@{SELF_ID}> 重开游戏", channel=lobby)))
    asyncio.run(bot.on_message(dm_message(f"<@{SELF_ID}>", channel=lobby)))  # 光 @ 没命令词

    assert commands == []
    assert lobby.sent == [UNKNOWN_COMMAND_HINT, UNKNOWN_COMMAND_HINT]


def test_dm_bot_滤bot账号与没到的消息():
    callbacks = BotCallbacks()
    commands: list = []
    callbacks.command = commands.append
    bot = make_dm_bot(callbacks)

    asyncio.run(
        bot.on_message(
            FakeMessage(FakeUser(id=1, bot=True), f"<@{SELF_ID}> 开始游戏", FakeChannel(), object())
        )
    )  # bot 账号（回执、别的 bot、自己）：一律不搭理
    asyncio.run(bot.on_message(dm_message(f"<@999> 开始游戏")))  # @ 的是别的 bot
    asyncio.run(bot.on_message(dm_message("开始游戏")))  # 没 @
    asyncio.run(bot.on_message(direct_message(f"<@{SELF_ID}> 开始游戏")))  # 私信不归主持 bot 管

    assert commands == []


# ---- 本局频道（GreatBritain）：建、销、查（dm bot，在命令来的服务器里操作） ----


def make_channel_bot(guild: FakeGuild) -> DmBot:
    """已收到过一条命令的 dm bot：频道操作都在命令来的服务器（假 guild）里。"""
    bot = make_dm_bot()
    lobby = FakeChannel(guild=guild)
    asyncio.run(bot.on_message(dm_message(f"<@{SELF_ID}> 开始游戏", channel=lobby)))
    return bot


def test_dm_bot_建本局频道():
    guild = FakeGuild()
    bot = make_channel_bot(guild)
    asyncio.run(bot.create_channel())
    assert guild.created == ["GreatBritain"]


def test_dm_bot_频道已在不能再建():
    guild = FakeGuild(channels=[FakeTextChannel("greatbritain")])  # 找频道名字不区分大小写
    bot = make_channel_bot(guild)
    with pytest.raises(RuntimeError):
        asyncio.run(bot.create_channel())
    assert guild.created == []


def test_dm_bot_查频道在不在():
    guild = FakeGuild()
    bot = make_channel_bot(guild)
    assert asyncio.run(bot.has_channel()) is False
    asyncio.run(bot.create_channel())
    assert asyncio.run(bot.has_channel()) is True


def test_dm_bot_销本局频道():
    channel = FakeTextChannel("GreatBritain")
    guild = FakeGuild(channels=[channel])
    bot = make_channel_bot(guild)
    asyncio.run(bot.destroy_channel())
    assert channel.deleted is True


def test_dm_bot_没有频道可销明确报错():
    guild = FakeGuild()
    bot = make_channel_bot(guild)
    with pytest.raises(RuntimeError):
        asyncio.run(bot.destroy_channel())


def test_dm_bot_还没命令来过频道操作明确报错():
    bot = make_dm_bot()  # 没喂过命令，不知道在哪个服务器操作
    with pytest.raises(RuntimeError):
        asyncio.run(bot.create_channel())
    with pytest.raises(RuntimeError):
        asyncio.run(bot.destroy_channel())
    with pytest.raises(RuntimeError):
        asyncio.run(bot.has_channel())


# ---- 回调分发：gbr bot（私信） ----


def test_gbr_bot_私信交消息回调带玩家与正文():
    received: list = []
    callbacks = BotCallbacks()
    callbacks.message = lambda player, text: received.append((player, text))
    bot = make_gbr_bot(callbacks)
    channel = FakeChannel()

    asyncio.run(bot.on_message(direct_message("在吗，谈谈关税", author_id=7, channel=channel)))

    assert received == [("7", "在吗，谈谈关税")]
    assert bot.dm_channel_for("7") is channel  # 私信频道记下，回复发回这里


def test_gbr_bot_公屏被_at_直回固定指引不交回调():
    received: list = []
    callbacks = BotCallbacks()
    callbacks.message = lambda player, text: received.append((player, text))
    bot = make_gbr_bot(callbacks)
    lobby = FakeChannel()

    asyncio.run(bot.on_message(dm_message(f"<@{SELF_ID}> 借我点钱", channel=lobby)))
    asyncio.run(bot.on_message(dm_message("大家聊得挺好", channel=lobby)))  # 没 @ 不搭话
    asyncio.run(
        bot.on_message(
            FakeMessage(FakeUser(id=1, bot=True), f"<@{SELF_ID}> 在吗", lobby, object())
        )
    )  # bot 账号被滤

    assert received == []
    assert lobby.sent == [GUILD_MENTION_HINT]


# ---- 发送方法（模块层） ----


def make_module(tmp_path):
    module = ImModuleImpl(load_config(tmp_path / "config.toml"))
    module._dm._connection.user = FakeUser(id=SELF_ID)  # 模块自建的 bot 也塞上假身份
    module._gbr._connection.user = FakeUser(id=SELF_ID)
    return module


def test_send_reply_发回玩家的私信频道(tmp_path):
    module = make_module(tmp_path)
    received: list = []
    module.on_message(lambda player, text: received.append((player, text)))
    channel = FakeChannel()

    asyncio.run(module._gbr.on_message(direct_message("在吗", author_id=7, channel=channel)))
    asyncio.run(module.send_reply("7", "回话：在"))

    assert received == [("7", "在吗")]
    assert channel.sent == ["回话：在"]


def test_send_receipt_发到命令来的频道(tmp_path):
    module = make_module(tmp_path)
    commands: list = []
    module.on_command(commands.append)
    lobby = FakeChannel()

    asyncio.run(module._dm.on_message(dm_message(f"<@{SELF_ID}> 开始游戏", channel=lobby)))
    asyncio.run(module.send_receipt("开始游戏 执行完成"))

    assert commands == ["开始游戏"]
    assert lobby.sent == ["开始游戏 执行完成"]


def test_send_receipt_还没命令来过明确报错(tmp_path):
    module = make_module(tmp_path)
    with pytest.raises(RuntimeError):
        asyncio.run(module.send_receipt("开始游戏 执行完成"))


def test_start_缺token明确报缺哪项(tmp_path):
    module = make_module(tmp_path)  # 临时 config.toml 没建，token 全缺
    with pytest.raises(RuntimeError) as info:
        asyncio.run(module.start())
    assert "dm_token" in str(info.value)
    assert "gbr_token" in str(info.value)


def test_代理配置传进两个bot(tmp_path):
    toml = tmp_path / "config.toml"
    toml.write_text('discord_proxy = "http://127.0.0.1:7890"\n', encoding="utf-8")
    module = ImModuleImpl(load_config(toml))
    assert module._dm.http.proxy == "http://127.0.0.1:7890"
    assert module._gbr.http.proxy == "http://127.0.0.1:7890"


def test_模块转发频道的建销查(tmp_path):
    module = make_module(tmp_path)
    guild = FakeGuild()
    lobby = FakeChannel(guild=guild)
    asyncio.run(module._dm.on_message(dm_message(f"<@{SELF_ID}> 开始游戏", channel=lobby)))

    asyncio.run(module.create_channel())
    assert asyncio.run(module.has_channel()) is True
    asyncio.run(module.destroy_channel())
    assert asyncio.run(module.has_channel()) is False
