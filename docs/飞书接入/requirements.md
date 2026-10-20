# 飞书接入：需求与调研

## 需求

- 一局游戏对应一个给定的飞书群聊，作为公屏大群。
- 所有 agent 玩家和任意数量的真人玩家都在大群里。
- agent 能在大群发言，也能在小群里沟通；小群从大群成员里拉人（真人或 agent 均可），用于密谈。沟通只有大群和小群两种形式，不用单聊。
- 运行时负责把初始化好的 agent 接进群聊。

## 要回答的问题

1. 怎么接入飞书：应用怎么建、权限怎么开、消息怎么收怎么发。
2. agent 初始化之后，怎么把它拉进给定的群聊。
3. 飞书的 bot 和本地的 agent 怎么绑定：一个 bot 对一个 agent，还是一个 bot 扮演多个？
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

## 实测清单（待做）

1. 群聊里 bot A 发消息，bot B（开 `im:message.group_msg.include_bot:read`）能否收到 `im.message.receive_v1` 事件。
2. bot 能否建小群、把其他 bot 拉进小群（建群 API 与成员添加对 bot 的支持）。
3. 小群里的互见行为是否与大群相同。
