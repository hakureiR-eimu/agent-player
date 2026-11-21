# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目是什么

维多利亚3 agent 玩家：agent 是玩维多利亚3的玩家，与人机同局的人类玩家对等（当前局执掌大不列颠，开发文件夹 `vic3-GreatBritain/`），通过 MCP 工具读游戏局势，人在 Discord 上与它对话。2026-10-20 推倒重来，旧的 TS 运行时（控制台、飞书接入、假 agent）已全部清除，当前处于第一版实现起步：**只读**游戏接入——agent 观察局势、出研判，游戏操作全部留给游戏原生 AI；写侧（操作注入）与多 agent 后续版本再做。

推倒重来前的旧运行时（控制台、飞书接入、旧 README）已全部清除，现状以本文件和 `vic3-GreatBritain/docs/` 为准。

## 三块主线与关系

- **游戏接入**（mod＋harness 的游戏接入子模块）＝ agent 的眼睛。mod 在游戏里每年把世界格局写进 error.log；子模块跑在 harness 进程内，把日志解析成三个方法（读取世界局势、发起博弈、新年判定），主体定时调新年判定，每年查到新年份记录时往事件队列推年度通知。接口声明在 harness 文档，实现在子模块文档（游戏接入-harness侧）。
- **Discord 接入**＝ agent 的嘴和耳朵。bot 收玩家消息、把 agent 的话发回频道，只是消息通道，不知道游戏。
- **harness**＝ agent 的身体。一个 Python 进程，装四块——主体管生命周期、调用其余三块（游戏接入、agent、IM 接入）——把 Discord 消息和游戏状态接到 agent 本体（Claude Code 会话）上：Discord 消息或游戏内年度更替 → harness 叫醒 agent 会话 → agent 调游戏接入读局势 → 回复发回 Discord。harness 代码一份（vic3-GreatBritain/src/，测试在 test/），进程不绑局：局文件夹固定一个（Victoria 3 用户目录下的 vic3-GreatBritain），agent 记忆文件在其下的 GBR 文件夹（profile/world/memory 三区，由 agent 管理装载）；agent 会话随局起止——开始游戏建本局频道（GreatBritain）起会话，保存游戏让会话整理文件夹后结束（频道留着），结束游戏收尾会话并销频道清 GBR。