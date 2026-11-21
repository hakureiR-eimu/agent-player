# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目是什么

维多利亚3 agent 玩家：agent 扮演一国（当前局：大不列颠，局文件夹 `vic3-GreatBritain/`），通过 MCP 工具读游戏局势，人在 Discord 上与它对话。2026-10-20 推倒重来，旧的 TS 运行时（控制台、飞书接入、假 agent）已全部清除，当前处于第一版实现起步：**只读**游戏接入——agent 观察局势、出研判，游戏操作全部留给游戏原生 AI；写侧（操作注入）与多 agent 后续版本再做。

推倒重来前的旧运行时（控制台、飞书接入、旧 README）已全部清除，现状以本文件和 `vic3-GreatBritain/docs/` 为准。

## 三块主线与关系

- **游戏接入**（mod＋mcp-server）＝ agent 的眼睛。mod 在游戏里每年把世界格局写进 error.log；mcp-server 把日志解析成 MCP 读工具。只知道"游戏→MCP 工具"这一段，不依赖 Discord 和 harness，可直接挂给任何 MCP 客户端。
- **Discord 接入**＝ agent 的嘴和耳朵。bot 收玩家消息、把 agent 的话发回频道，只是消息通道，不知道游戏。
- **harness**＝ agent 的身体。把前两者接到 agent 本体（Claude Code 会话）上：Discord 消息进来 → harness 叫醒 agent 会话 → agent 调 mcp-server 读局势 → 回复发回 Discord；profile/world/memory 三区落在局文件夹，由 harness 管生命周期。