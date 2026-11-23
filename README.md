# game-agent

给维多利亚 3（Victoria 3）造一个 LLM 驱动的 AI 玩家：它执掌大不列颠，与人类玩家同局对等游玩——观察世界局势、经营外交关系、经 Discord 谈判博弈，也能主动向玩家发动外交博弈。

P 社游戏的传统 AI 与玩家没有交流：玩家无法与 AI 沟通、无从了解其意图；AI 靠机械数值计算外交关系，难以基于局势选择盟友与敌人、展开合纵连横的外交博弈。本项目补上这一块。项目分三块：游戏接入、Discord 接入、agent。

## 游戏接入

在原版游戏上加 mod 完成，不动游戏引擎：

- mod 把世界局势与大不列颠内政写进游戏日志，agent 经工具按需查询
- 博弈操作日志让 agent 可主动向玩家发动外交博弈
- 年度判定事件定期唤醒 agent

## Discord 接入

双 bot 分工，消息监听与接收经闭包和回调函数实现：

- **dm bot** 管理游戏——玩家在大厅频道 @ 它下「开始新游戏 / 继续游戏 / 保存并结束游戏」三条命令，公屏回执
- **gbr bot** 负责交流——接收玩家私信、以大不列颠的身份给玩家发消息

## agent

以 Claude Agent SDK 为底座，复用 coding agent 的会话、工具与文件能力来承载游戏玩家；harness 负责调度：

- 用消息队列解耦 agent 与各接入模块——agent 订阅玩家私信、游戏年度更替等事件，忙时队列阻塞，空闲时 harness 合并投递
- system prompt 注入大不列颠玩家身份与工作规则，装载真实联机规则与游戏攻略作玩法知识，据外交账本推进长程计划
- 行动经调用工具完成：查询局势、收发消息、发起博弈

## 目录

```
vic3-GreatBritain/    主体工程：源码、mod、文档、prompt 模板
  src/                harness 与 game / im / agent 三个模块
  mod/                维多利亚 3 mod
  prompt/             agent 工作空间模板（gbr-template）
  docs/               prd、调研、运行与测试
游戏wiki/             中英文游戏 wiki
游戏原版/             原版游戏文件
scripts/              wiki 抓取与整理脚本
```

怎么跑见 [vic3-GreatBritain/docs/运行与测试/运行.md](vic3-GreatBritain/docs/运行与测试/运行.md)。

## 技术栈

Python · Claude Agent SDK · discord.py · 维多利亚 3 mod
