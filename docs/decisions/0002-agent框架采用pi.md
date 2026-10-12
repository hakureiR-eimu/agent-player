# 决策 0002：agent 运行时采用 pi

- **日期**：2026-10-12
- **状态**：已采纳（作者拍板）

## 背景

候选：LangGraph、CrewAI、AutoGen/AG2、OpenAI Agents SDK、Claude Agent SDK（对比见《参考/基础设施-agent与角色书》）。国家 agent 的本质需求是固定循环（读局面 → 思考 → 发言/行动 → 调工具执行），外加 8 国并发与自定义外交工具集——不需要图编排、角色抽象这类重框架能力。

## 决策

**采用 [pi](https://github.com/earendil-works/pi)（Mario Zechner / earendil-works）作为 agent 运行时。**

Monorepo 按需取用：

| 包 | 用途 |
|----|------|
| `packages/agent` | agent 核心循环（可编程嵌入，不 fork） |
| `packages/ai` | 统一 LLM API，多 provider 可换模型 |
| `packages/mcp` | 工具/MCP 生态 |
| `packages/coding-agent` | 完整 harness，仅作参考实现（其 read/write/edit/exec 四工具我们基本不用） |

## 理由

1. **理念契合**：pi 的哲学是"agent = 循环 + 工具，通过 extension 适配你的工作流，而不是反过来"。外交工具集（读游戏状态、飞书收发、外交操作）以自定义工具接入即可。
2. **零件齐全且轻**：agent core、统一 LLM API、MCP 都是现成的，没有框架税。
3. **技术栈统一**：TypeScript/Node，与飞书开放平台 SDK 同栈。

## 后果

- 项目技术栈定为 **TypeScript / Node.js**
- 放弃 Python 系框架路线（LangGraph 等）
- 需要调研 `packages/agent` 的嵌入用法与扩展机制（`examples/` 目录）
- pi 的 4 个核心工具大多用不上，我们注册自己的外交工具集替代

## 被否决的方案

- **LangGraph**：图编排能力过剩，且引入 Python 双语言栈
- **CrewAI / AutoGen**：角色化/自由对话抽象与"行动受游戏接口白名单约束"的需求不匹配
- **OpenAI Agents SDK / Claude Agent SDK**：绑定单一生态；pi 的 `ai` 包本身就支持多 provider，选型自由度更高
