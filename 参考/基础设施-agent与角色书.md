# 基础设施：Agent 框架与角色书规范

> 调研日期：2026-10-12；定案更新：2026-10-12。原则：agent 不从头手撸，能借就借。

## Agent 框架：已定案 pi（决策 0002）

**采用 [pi](https://github.com/earendil-works/pi)（Mario Zechner / earendil-works，npm：`@earendil-works/pi-coding-agent`）作为 agent 运行时。** 详见 `docs/decisions/0002`。

Monorepo 取用方式：`packages/agent`（agent 核心循环，可嵌入不 fork）+ `packages/ai`（统一 LLM API，多 provider）+ `packages/mcp`（工具生态）；`packages/coding-agent` 仅作参考实现。技术栈由此定为 **TypeScript / Node.js**。

以下是当初的选型对比，留作背景资料：

| 框架 | 特点 | 对本项目的适配度 |
|------|------|----------------|
| **pi** | 极简 harness："agent = 循环 + 工具"，extension 机制适配工作流 | ✅ **已定案** |
| **LangGraph** | 图编排、确定性恢复、控制力最强，学习曲线陡 | 备选。能力过剩，且引入 Python 双语言栈 |
| **CrewAI** | 角色化抽象、上手最快 | 落选。自由对话抽象与"行动受白名单约束"不匹配 |
| **AutoGen / AG2** | 对话式多 agent，研究向 | 落选。同上 |
| **OpenAI Agents SDK** | 轻量、生产成熟、handoff/guardrail | 落选。绑定 OpenAI 生态 |
| **Claude Agent SDK** | agent 循环、工具、子 agent 齐全 | 落选。绑定 Claude；pi 的 `ai` 包支持多 provider |

扩展阅读：[Galileo 四框架对比](https://galileo.ai/blog/autogen-vs-crewai-vs-langgraph-vs-openai-agents-framework) · [Splunk 2026 框架盘点](https://www.splunk.com/en_us/blog/learn/agent-frameworks.html) · [Langfuse 开源框架对比](https://langfuse.com/blog/2025-03-19-ai-agent-comparison) · [Mario Zechner：构建极简 coding agent的经验](https://mariozechner.at)

## 架构原则：所有通信走飞书（决策 0003）

**agent 之间（以及 agent 与玩家）的所有通信必须走飞书 API，禁止进程内总线/本地消息队列直连。** 信息不对称由飞书权限模型天然保证，飞书会话即完整审计日志。详见 `docs/decisions/0003`。

待验证：飞书 bot 与 bot 之间能否直接互发消息；若不允许，以"两国小群"形态实现双边密谈。

## 角色书：直接借用 SillyTavern 角色卡规范

"角色书"概念的标准化来源是 SillyTavern 生态的 **Character Card V2/V3 规范**：

- 核心字段：`name` / `description`（人设）/ `personality` / `scenario` / `first_mes` / `mes_example`
- **`character_book`（内嵌世界书）**：带关键词触发的知识条目（keys → content），支持插入顺序、扫描深度、上下文预算控制——**正好是"国家角色书"需要的结构**：固定人设（英帝国的傲慢与光荣孤立）+ 条件触发的史实/局势知识（提到殖民地纠纷时才注入相关历史背景）
- 生态红利：现成编辑器（The Grimoire 等）、卡片可嵌入 PNG 分发、大量可参考的角色卡写法
- 链接：[malfoyslastname/character-card-spec-v2](https://github.com/malfoyslastname/character-card-spec-v2) · [SillyTavern World Info 文档](https://docs.sillytavern.app)

**初判**：以 character_book 格式为蓝本定义我们的"国家角色书" schema，在其上扩展 V3 特有字段（`national_objectives` 国家目标、`standing` 当前立场、`red_lines` 底线）。不直接跑 SillyTavern（它是聊天前端，不是决策引擎），只借格式与写法。

## 其他可借用的零件

- **结构化输出**：外交动作走 JSON schema 约束的工具调用（pi 自定义工具天然承担此角色），杜绝自由文本直接操作游戏
- **记忆**：单局内对话历史 + 摘要；跨局记忆参考 Generative Agents 记忆流（远期）
- **评测**：AI_Diplomacy 的 `analysis/` 对局分析管线可参考（见《相关项目-外交AI》）
