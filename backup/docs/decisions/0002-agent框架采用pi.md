# 决策 0002：agent 运行时采用 pi

- **日期**：2026-10-12
- **状态**：**已修订（2026-10-13）**——运行时基底改为 Claude Agent SDK，见文末修订记录；下文为原始决策，保留存档

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

---

## 修订（2026-10-13）：基底改为 Claude Agent SDK

**决策**：agent 运行时基底由 pi 换为 **Claude Agent SDK**（TypeScript 版；宿主进程驱动，每会话一个 CLI 子进程，流式输入模式下常驻——2026-10-13 spike 核对后修正，非最初以为的单进程内嵌）。原文其余部分（对比其余候选的结论、"库不框架"的选型哲学、技术栈 TypeScript/Node）不变。

**为什么推翻原决策**：

1. **机制自建面积是真实成本**：pi 路线下 compaction、会话持久化与重建、工具前置钩子、事件合并注入都要自己组装并长期维护；SDK 全部现成（hooks、permission、compaction、resume）。项目重心在外交语义与游戏桥，省下的工程应投产品而不是重造 harness
2. **MCP 语义原生对齐**：agent需求 §三已定案"载体 MCP 语义对齐"——SDK 的 custom tools 本来就是这个形状，不需要"对齐"
3. **重新评估原否决理由"绑定单一生态"**：默认绑 Claude 属实，但可经 `ANTHROPIC_BASE_URL` 兼容层接其他模型（本机 Claude Code 接非 Claude 模型已验证该路径可行）——从"死路"变为"有逃逸口的默认约束"，兼容层行为差异需 spike 验证
4. **体感优势**：日常开发即在 Claude Code 中，其 hooks / 工具 / 会话机制有一手体感，文档与排错资源充足

**代价与遗留**：

- ~~主体与沟通.md 的 pi 源码核对全部作废，SDK 映射待 spike 核对~~ → 2026-10-13 文档级核对完成（工具注册、拦截拒绝路径、systemPrompt 锁定、流式输入多轮、resume、compaction 均落实，见主体程序需求 §5.2 / §六）；剩两项实测：兼容层（非 Claude 模型）行为、Windows 下 8 常驻子进程资源
- 进程模型修正：SDK 为子进程模型（1 宿主 + 8 CLI 子进程），非单进程内嵌——隔离更强（进程级故障隔离白送），代价是子进程资源开销
- pi 时代的机制设计不浪费——noTools、钩子约束、写前留痕、限流计数都是需求不是实现，已平移为 SDK 落点（`tools: []` + 内存 MCP server + execute 内路径校验，与 pi 方案同构）
- 若实测发现兼容层不可接受（工具调用 / compaction 行为差异过大），回退路径即本文原始决策
