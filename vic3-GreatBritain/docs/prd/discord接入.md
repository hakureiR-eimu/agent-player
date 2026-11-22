# Discord 接入

Discord 接入就是 harness 的 IM 接入子模块（接口声明见 [harness](harness.md) 的 IM 接入节），通 Discord、收发两头：收玩家的命令与消息，发 agent 的话。本文件细化声明、写实现设计，代码落在 src/im/impl/。平台侧的建号、邀请与 token 管理见 [discord侧管理](discord侧管理.md)。

## 先例：CivAgent 的 Discord 结构

CivAgent（网易伏羲，LLM 扮演文明玩 Unciv 的数字玩家，论文 arXiv 2502.20807）用 Discord 做玩家与 agent 的对话通道，结构与我们同构：

- 两类 bot 分工：一个管理 bot（Unciv_Bot）收玩家的 gameid、给每局建私密频道（本局参与的文明 bot 与人类玩家逐个授权可见）；每个可选文明一个 chatbot，扮演该国与玩家对话
- 两个交流场所：每局的群频道（公开讨论＋事件广播）与玩家和文明 bot 的私信（私下外交）——谈判、许诺、欺骗发生在私信里
- agent 主动开口：agent 决策产生对话时，主动给玩家发私信、往频道发言（发信直接调 Discord HTTP API）
- bot 只做门面：bot 收到消息全部经服务器中转进 agent；agent 之间的对话也不走 Discord（bot 之间互相收不到消息），在服务器进程内直接交换
- 防互触发：bot 收消息第一步排除 bot 账号的消息

（以上读自其开源代码 deployment/chatbot/，同类项目实现，二等证据）

## 两个 bot 的分工

- dm bot：主持 bot，非 LLM 驱动。玩家在大厅频道 @ 它下三条命令（开始游戏、保存游戏、结束游戏），交主体注册的命令回调（装配处包成 command 事件推进队列），主体订到后执行；命令格式的问题（不认识的词）它自己回固定提示，执行结果的回执由主体执行完调它发出（固定文案，发到命令来的地方）。本局频道（GreatBritain）也归它管：开始游戏建、结束游戏销，主体按命令排着调；频道在不在是局挂没挂着的外显，主体靠它挡命令（已在不能再开始、没有不能结束）
- gbr bot：大不列颠玩家的门面——agent 是玩维多利亚3的玩家，与人机同局的人类玩家对等，只是他执掌的国家是大不列颠；agent 的话全从它嘴里出；玩家对它说的话交主体注册的消息回调（装配处包成 message 事件推进队列）

两个身份分开，玩家对谁说话就分明：@ dm bot 是对系统下命令，私信 gbr bot 是和玩大不列颠的那位玩家打交道。

## 玩家与 gbr bot 的私信

对话只发生在一个场所：玩家私信 gbr bot——两位玩家就各自执掌的国家谈交易、结盟、威胁、试探，只有双方知道；gbr bot 的回复也回到私信里。

message 事件带玩家（谁在私信），agent 收进消息队列；agent 发话走会话工具（发消息——主体装配时把本模块的发送方法包成工具），gbr bot 把话发到玩家私信。gbr bot 主动开口（先私信玩家）随外交博弈（start_play）一起做，声明在案、实现随后。

## 平台事实

（证据等级：一等＝Discord 官方文档）

- 免特权 intent 的消息（一等，Gateway 文档）：与 bot 的私信、@ 到该 bot 的消息，不开 MESSAGE_CONTENT 也能读内容——dm bot 的入口（大厅频道 @）与 gbr bot 的入口（私信）都在豁免内，特权 intent 不用开
- bot 建销服务器频道要 Manage Channels 权限（一等，Permissions 文档），邀请进服务器时给——dm bot 建销本局频道（GreatBritain）用；找频道按名字不区分大小写比对（GreatBritain 存成什么样都找得到）
- bot 主动私信玩家走 Create DM 端点（一等，Channels 文档），前提是玩家与 bot 同服务器、玩家隐私设置允许 bot 私信
- bot 之间互相收不到消息（二等，CivAgent 代码绕开此限制的写法可证）——两个 bot 各管各的入口，收消息一律忽略 bot 账号（含 dm bot 的回执、自己的消息），互不触发

## 实现：怎么做

收发的分界：收是被动的——bot 在线收着（Gateway 长连接，心跳重连归 discord.py 管），收到消息先滤掉 bot 账号（含 dm bot 的回执、自己的消息，防互触发），再调主体注册的回调；IM 接入零总线知识，包事件推进队列在装配处。发与读是主动的——主体调模块的发送与读取方法（包成 agent 的会话工具：发消息、读消息）。

- 登录：harness 进程内两个 discord.py client 并行登录（dm bot、gbr bot），token 两项进 config.toml（dm_token、gbr_token），两个 client 跑在同一个事件循环里——回调与事件队列同循环，无跨线程问题
- bot 结构：每个 bot 一个子类 Client（构造时存回调），on_message 里滤 bot 账号再调回调
- dm bot：监听大厅频道 @ 自己的消息，正文命令词对白名单匹配——命中调命令回调（带命令词）；不认识的词模块内直回固定提示（Discord 侧的应酬话留在此层）
- gbr bot：监听自己的私信，调消息回调（带玩家、正文）；在大厅频道被 @ 模块内直回一句固定指引（请私信我）
- 交给主体：回调在装配时挂（on_command/on_message 注册），闭包里包事件推进队列——回调在 discord.py 的事件任务里被同步调，只做入队立刻返回，事件总线为此补一个同步 push（put_nowait 的同步皮）
- 发消息：发送方法（send_message）由主体包成 agent 会话的发消息工具，agent 调工具时按目标玩家发他的私信频道
- 读消息：读取方法（read_message）由主体包成会话的读消息工具，翻与玩家的私信频道里最近的消息（只取最近 100 条，从新到旧排）
- 命令回执：主体执行完 command（起会话、拒绝重复起、收尾完成）调发送方法（send_receipt），回执发到大厅频道原处，固定文案
- 本局频道：dm bot 管建与销（guild.create_text_channel / channel.delete），在哪个服务器操作取最近一条命令来的频道。边界判定归主体——先问 IM 接入频道在不在（has_channel）再排动作，模块方法里的报错只是兜底
- 测试：单测盖命令解析（@ 前缀剥离、白名单）、回调分发（喂假消息断言回调收到、bot 账号被滤）、发送与读取方法；集成测试起真 bot 手动收发（test/im/test_im_integration.py，在 VSCode 测试面板里跑），样式照 test/game/
