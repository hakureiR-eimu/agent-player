# 游戏 agent

维多利亚3 联机局的 agent 玩家：一国一个 agent，活在飞书群里，像真人玩家那样外交、记事、拉群密谈。是什么、要什么见 [docs/项目需求](docs/项目需求.md)；干到哪了见 [docs/执行](docs/执行.md)（全局唯一的现状文档）。

## 跑起来

```
npm install
npm start
```

启动后自动打开控制台（默认 http://localhost:5678，端口被占用时 `GAME_AGENT_PORT=5699 npm start`）。控制台上：给局起名 → 勾国家 → 选真/假 agent → 创建。建局会在仓库根生成 局名/agents/<tag>/（profile 自动从模板＋资料装好）。

- 没配飞书 = 本地模式：群只在控制台里，页面下方可以以真人身份发言——这就是新的试跑环境。
- agent 类型：假 agent 是固定回复的小脚本（不调大模型，验链路用）；真 agent 是 Claude 会话，按 profile 扮演国家（认证走 ANTHROPIC_* 环境变量或 ~/.claude/settings.json）。

## 接飞书

一国一应用（每个国家一个飞书自建应用）＋一个 DM 应用（非 LLM，负责建群拉人当群主），都只能在飞书开发者后台人工建：

1. 建各国应用：开启机器人能力，**机器人名称直接设为国家 tag**（GBR、FRA……，机器人在群里的显示名就是它，没有改群昵称的 API）；事件与权限里开通长连接模式，加权限：接收群聊中群内所有消息（`im:message.group_msg:read` 之类）、拉用户进群、建群、获取群成员信息（各应用消息权限照 [docs/飞书接入](docs/飞书接入/requirements.md) 的调研清单开）。
2. 建 DM 应用：同样开机器人和长连接，名字改成局名（改名要发版，一局一次）。
3. 各应用发布并在租户内启用、可用范围放全租户（拉真人进群要求真人在 DM 应用的可用范围内）。
4. 把 config/feishu.example.json 拷成 config/feishu.json，填 DM 和要上的国家的 appId/appSecret。配好后 npm start 就是飞书模式：DM 以局名建大群、拉各国 bot 进群、拉起 agent 报到；真人的 open_id/user_id 从控制台拉进群。

## 代码

src/ 是运行时（TypeScript）：main 入口、server 控制台服务、gameManager 建局编排、agent 真会话、fakeAgent 薄链路、chatHub 聊天账本与扇入、feishuHub 飞书收发。`npm run typecheck` 查类型。
