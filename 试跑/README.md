# 试跑

阶段一的本地试跑环境（见 [docs/游戏agent/design](../docs/游戏agent/design.md) 的"本地试跑"）：不接飞书，终端当群。

```
npm install        # 第一次
npm start          # 交互：你扮演其他玩家，逐行敲 【场景】说话人：内容
npm run once       # 只跑开局报到一轮，自检用
node run.mjs FRA   # 换个国家跑（agents/ 下要有对应文件夹）
```

- 系统提示词照常从 agents/<tag>/profile/ 组装；子会话的工作目录就是 agents/<tag>/。
- 权限照 design：读限自己的文件夹，写限 memory/，聊天走 terminal 工具（send_message / list_groups / list_members / create_group）。
- 聊天记录落 agents/<tag>/world/chat/<群ID>.md，运行时负责写；agent 的草稿落 memory/。
- 会话靠 resume 续着，多轮就是一个 SDK 会话。
