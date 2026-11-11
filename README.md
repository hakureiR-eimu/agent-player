# 游戏 agent

维多利亚3 联机局的 agent 玩家：一国一个 agent，活在飞书群里，像真人玩家那样外交、记事、拉群密谈。是什么、要什么见 [docs/项目需求](docs/项目需求.md)；干到哪了见 [docs/执行](docs/执行.md)（全局唯一的现状文档）。

## 跑起来

```
npm install
npm start
```

启动后自动打开控制台（默认 http://localhost:5678，端口被占用时 `GAME_AGENT_PORT=5699 npm start`）。控制台上：给局起名 → 勾国家 → 创建。建局会在仓库根生成 局名/agents/<tag>/（profile 自动从模板＋资料装好）。

局的生命周期：**开始 →（运行中）保存并退出 → 继续 / 结束**。同时只能有一局；agent 的状态（会话、聊天账本、memory）都在 局名/ 文件夹里，局与局不共享；飞书应用（DM 和各国）多局复用，建一次管所有局，旧局的群留在飞书里当档案。保存与恢复不依赖进程活着：状态落在 局名/game.json（根下的 state.json 指着当前局），进程崩了下次启动照样能继续。

- 飞书是必配项：没配 config/feishu.json（或缺 DM 应用凭证）启动就报错退出，没有本地兜底。试跑链路就用一份小配置（DM ＋ 一两个国家）在真飞书上跑。
- agent 是真的 Claude 会话，按 profile 扮演国家。大模型认证：把 config/llm.example.json 拷成 config/llm.json 填 GLM 的 APIKey（走智谱的 Anthropic 兼容端点）；不配就回落到环境变量 ANTHROPIC_* 或 ~/.claude/settings.json。

## 接飞书

一国一应用（每个国家一个飞书自建应用）＋一个 DM 应用（非 LLM，负责建群拉人当群主），都只能在飞书开发者后台人工建：

1. 建各国应用：开启机器人能力，**机器人名称直接设为国家 tag**（GBR、FRA……，机器人在群里的显示名就是它，没有改群昵称的 API）；事件与权限里开通长连接模式，加权限：接收群聊中群内所有消息（`im:message.group_msg:read` 之类）、拉用户进群、建群、获取群成员信息（各应用消息权限照 [docs/飞书接入](docs/飞书接入/requirements.md) 的调研清单开）。
2. 建 DM 应用：同样开机器人和长连接。应用是**多局复用**的，名字起个顺眼的固定用（比如 DM）——大群名才是局名，DM 的名字不再跟局走。
3. 各应用发布并在租户内启用、可用范围放全租户（拉真人进群要求真人在 DM 应用的可用范围内）。
4. 把 config/feishu.example.json 拷成 config/feishu.json，填 DM 和要上的国家的 appId/appSecret（countries 配多少国家上多少，没配的国家建局时勾不了）。配好后 npm start：DM 以局名建大群、拉各国 bot 进群、拉起 agent 报到；真人的 open_id/user_id 从控制台拉进群。

## 代码

src/ 是运行时（TypeScript）：main 入口、server 控制台服务、gameManager 建局编排、agent 会话、chatHub 聊天账本与扇入、feishuHub 飞书收发。`npm run typecheck` 查类型。
