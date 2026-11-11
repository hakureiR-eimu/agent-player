# 飞书接入：需求与调研

## 需求

- 一局游戏对应一个公屏大群：群名就是局名，由 DM 创建、DM 当群主。DM 是一个非 LLM 的飞书 bot，名字就是局名。
- 所有 agent 玩家和任意数量的真人玩家都在大群里。
- agent 能在大群发言，也能在小群里沟通；小群同样由 DM 创建、DM 当群主：发起的玩家找 DM 拉一个 2 人群（自己和 DM），再由 DM 把其他玩家拉进来（从大群成员里选，真人或 agent 均可），用于密谈。沟通只有大群和小群两种形式，不用单聊。
- 运行时负责把初始化好的 agent 接进群聊。

## 要回答的问题

1. 怎么接入飞书：应用怎么建、权限怎么开、消息怎么收怎么发。
2. agent 初始化之后，怎么把它拉进给定的群聊。
3. 飞书的 bot 和本地的 agent 怎么绑定：一国一应用已定（每个国家一个应用）；DM 是额外的应用，非 LLM、不当玩家，只做建群、拉人、当群主。
4. 飞书动作具体有哪些：大群发言、小群发言之外还需要什么（建小群、拉成员、退群？），各自怎么实现。
5. agent 之间互见互达（已有调研结论，见下）。

## 调研结论

### agent 互见互达（2026-10-20，官方文档）

**群聊互见：官方文档明确支持，与二手说法矛盾、以实测为准。**

- 官方一级证据：机器人可接收群内其他机器人发的消息。权限 `im:message.group_msg.include_bot:read`（收群内所有用户和其他机器人的消息，不含自己发的），@ 消息场景另有 `im:message.group_at_msg.include_bot:readonly`。
- 矛盾点：旧调研引用的 OpenClaw 生产文档称"即使配了 include_bot 也只在被 @ 时投递"。
- 来源：接收消息事件文档 https://open.feishu.cn/document/server-docs/im-v1/message/events/receive

**bot 给 bot 发单聊：官方文档层面未支持。已定案不用单聊，此项不再阻塞设计，留作背景。**

- 发送接口的接收者 ID 类型只有用户类 ID（open_id/user_id/union_id/email）和群 ID（chat_id），没有应用类 ID。来源：https://open.feishu.cn/document/server-docs/im-v1/message/create
- 接收侧的单聊权限只描述了"用户发给机器人的单聊消息"。
- 旧调研（OpenClaw，高置信）也称 bot 间私聊不通。
- 2026-10-20 定案：沟通只用大群和小群，不用单聊。

### 建群与拉人（2026-10-20，官方文档）

**拉人直接进群，没有被拉者同意这一环。**

- 建群接口（im/v1/chats）：机器人可以建群，不指定群主时建群的机器人自己就是群主；建群时可直接带成员 user_id_list（每次最多 50 人）和机器人 bot_id_list（每次最多 5 个，群内机器人总数上限 15——一局 8 国都在大群也够用）。
- 拉人接口（im/v1/chats/:chat_id/members）：把用户或机器人直接拉入群内。响应里有个 pending_approval_id_list（等待群主或管理员审批的成员）——审批是群主/管理员的事，不是被拉者的事；我们的场景里 bot 自己建群、自己是群主，拉人即直接生效。
- 建群参数 membership_approval（加群审批）默认 no_approval_required，且它管的是"申请加群"，不影响被拉进群。
- 拉机器人的前提：对方应用开启机器人能力、且在本租户已安装启用。拉真人的前提：对方在应用的可用范围内——一国一应用意味着每个国家应用都要把玩家放进可用范围。
- 其它：频控 1000 次/分钟、50 次/秒；对同一个群连续拉人要串行，并发会报 232019。
- 群主规则：群必有群主，建群时不指定 owner_id 则建群的机器人自己就是群主；建群时指定群主、事后转让群主（更新群信息接口）都只收用户 ID，给不了 bot。bot 当群主的唯一方式是自己建群。
- 应用改名：飞书没有改应用名称的 API，改名要在开发者后台手动改并重新发布（官方帮助中心说法）。DM 的名字=局名，只能开局人工改，一局一次。
- 定案（2026-10-21，再次修订）：大群、小群都由 DM 创建并当群主，玩家（真人或 agent）一律由 DM 拉进群；小群由玩家发起，DM 先拉 2 人群（发起者和 DM），再拉其他玩家。DM 名字改成局名（人工，见上一条）。此前"第一个拉起的国家应用建群"作废。
- 来源：建群 https://open.feishu.cn/document/server-docs/group/chat/create 、拉人 https://open.feishu.cn/document/server-docs/group/chat-member/create 、更新群信息（转让群主）https://open.feishu.cn/document/server-docs/group/chat/update-2 、应用改名 https://www.feishu.cn/hc/zh-CN/articles/360024984973

### 各应用要开的权限（2026-10-21，官方接口文档的"权限要求"段）

- 国家应用（玩家）：只要 `im:message:send_as_bot`（在群里发言）。收消息权限一个不用开——运行时把 agent 的话直接扇入其他 agent 的会话，不靠飞书平台转投 bot 消息。
- DM（主持人）：三个权限——
  - `im:message.group_msg.include_bot:read`：收群里所有用户和 bot 的消息（配合事件订阅 im.message.receive_v1、长连接方式）；
  - `im:message:send_as_bot`：发系统通知；
  - `im:chat`：一个覆盖建群、拉人、查群成员三个接口（三者的"开启任一权限即可"列表里都有它）。
- 单接口的备选权限（开任一即可，供对照）：建群 `im:chat` 或 `im:chat:create`；拉人 `im:chat` 或 `im:chat.members:write_only`；查成员 `im:chat`、`im:chat:readonly`、`im:chat.members:read` 等。
- 权限和应用配置（开机器人能力、事件订阅、发版）都只能登录开发者后台人工操作，官方没有开放 API/CLI 代办——"申请 API 权限"文档给的步骤就是后台点按钮；2026 年的官方 CLI（lark-cli）管的是用应用操作飞书内容（消息/文档/表格），管不了应用自己的配置。
- 来源：建群 https://open.feishu.cn/document/server-docs/group/chat/create 、拉人 https://open.feishu.cn/document/server-docs/group/chat-member/create 、查成员 https://open.feishu.cn/document/server-docs/group/chat-member/get 、申请权限流程 https://open.feishu.cn/document/server-docs/application-scope/introduction

### Vercel Chat SDK 官方飞书适配器（2026-10-21，官方文档，不引入）

飞书发布了 Vercel Chat SDK（多平台聊天机器人框架）的官方适配器 @larksuite/vercel-chat-adapter，底层是 @larksuiteoapi/node-sdk 里的 Channel SDK（LarkChannel）。查证后不引入：

- 它解决的问题（一套代码接 Slack/Teams/Discord 等多平台、单 bot 的 @ 提及/私信回调模型）和我们的形状不匹配：我们只上飞书，一国一应用是 9 个 bot 身份的编排（DM 建群拉人、各国自己发消息），收发路由、排队打包、扇入、限速都是局规则，不是通用 bot 框架能替的。我们已用同一个底层 node-sdk 自建了这一层（src/feishuHub.ts），薄且已验。

两个可借鉴的点，留档：

1. `registerLarkApp` 扫码授权一键建应用（自动返回 client_id/secret 并预配权限）——如果它能自定义应用名，可以省掉"人工建 9 个应用"里的一部分手工；待查证：扫码建的应用能不能指定名字（国家应用名必须等于 tag）、预配的权限是不是我们要的那套。来源：https://open.feishu.cn/document/mcp_open_tools/integrating-agents-with-feishu/vercel-chat-sdk-lark-message-publish
2. Channel SDK 的 cardkit 流式输出（typewriter 打字机效果，非轮询）——以后做沉浸感打磨时可以考虑让 agent 的长消息在群里流式出现；现在用不上。

## 实测清单（待做）

1. 群聊里 bot A 发消息，bot B（开 `im:message.group_msg.include_bot:read`）能否收到 `im.message.receive_v1` 事件。
2. bot 建小群、拉其他 bot 进群：API 层官方已支持（建群带 bot_id_list、拉人接口收 app_id），要实测的是拉进来之后的互见与消息收发。
3. 小群里的互见行为是否与大群相同。
4. 拉人直接进群、无审批（bot 为群主时）：官方文档即此行为，实测顺手确认一次 pending_approval_id_list 是否始终为空。
5. DM 改名的实际流程：后台改名是否必须发版、要不要管理员批准、生效多快。
