# 相关项目：外交 AI 先例

> 调研日期：2026-10-12。与我们"多国家 LLM agent 合纵连横"需求同构的先例项目。

## 1. CICERO（Meta AI，2022）— 外交 AI 的标杆

- **是什么**：在桌游 Diplomacy（纯谈判+策略）上达到人类水平（webDiplomacy 前 10%）的 agent，发表于 Science。
- **架构启示**：**两层架构**——语言模型（沟通）+ 规划引擎（战略推理 + RL），并从对话中推断其他玩家的信念与意图。这直接回答了我们要不要"纯 LLM"的问题：纯 LLM 谈吐好但战略一致性差，值得分层。
- **后续分析值得警惕**：后续论文（arXiv 2024-06 "More Victories, Less Cooperation"）发现 CICERO 战略能力强但**偏不合作、倾向背叛**——我们的信誉机制设计要考虑这点。
- 链接：[AI at Meta – Diplomacy and CICERO](https://ai.meta.com) / Science 2022 原论文 / [Noam Brown 主页](https://noambrown.com)

## 2. WarAgent（Rutgers + Michigan，2023）— 与本项目几乎同构

- **是什么**：LLM 多 agent 模拟世界大战（一战/二战），**每个国家一个 agent**，进行外交沟通、谈判与决策，研究战争触发机制。
- **借鉴点**：国家 agent 的 prompt 结构（国家角色设定 + 目标 + 约束 + 局势摘要）、国家间消息协议、回合制决策循环——就是我们"角色书 + 国家目标"的学术版原型。
- **差异**：WarAgent 是纯文本沙盘，没有真游戏；我们接的是 Victoria 3 真实对局。
- 论文：[arXiv:2311.17227 "War and Peace (WarAgent)"](https://arxiv.org/abs/2311.17227)；官方代码 `AgentialTwister/WarAgent`（GitHub，链接待本地核实）

## 3. GoodStartLabs/AI_Diplomacy — 最值得直接抄作业的工程实现

- **是什么**：开源 harness，让前沿模型（GPT/Claude/Gemini）互玩完整 webDiplomacy 对局；媒体评测中 o3 因"最会骗"胜出。
- **直接可借鉴的模块结构**（已核实仓库）：
  - `ai_diplomacy/agent.py` — agent 主循环
  - `ai_diplomacy/planning.py` — 规划层（对应 CICERO 的战略层）
  - `ai_diplomacy/negotiations.py` — 谈判协议
  - `ai_diplomacy/prompt_constructor.py` + `prompts/` — **按国家构造 system prompt，就是"角色书"思路的现成实现**
  - `ai_diplomacy/diary_logic.py` / `narrative.py` — 日记/叙事（风味来源！）
  - `analysis/` — 对局分析管线
  - `twitch-streamer/` + `ai_animation/` — **直播/对局可视化**，我们做"观众模式"的现成参考
  - 内嵌完整开源 Diplomacy 游戏引擎 `diplomacy/`
- 链接：[github.com/GoodStartLabs/AI_Diplomacy](https://github.com/GoodStartLabs/AI_Diplomacy) / [Every.to 评测报道](https://every.to)

## 4. 相关但更远的项目

- **Generative Agents（斯坦福小镇）**：多 agent 社会模拟 + 记忆流（记忆检索/反思/重要性评分）——跨局长期记忆的设计来源。
- **tsinghua-fib-lab/LLM-Agent-Based-Modeling-and-Simulation**：LLM agent 社会模拟论文清单仓库，按图索骥用。
- 社区讨论（Steam/Paradox Forum）：对"LLM 做大战略 AI"的常见质疑是延迟/成本/决策规模，**共识是 LLM 最适合先做"外交风味与谈判"**——恰好就是我们的切入点。

## 来源

- [AI at Meta – CICERO](https://ai.meta.com) · [Science 2022 论文](https://www.science.org)
- [arXiv:2311.17227 – WarAgent](https://arxiv.org/abs/2311.17227)
- [GoodStartLabs/AI_Diplomacy](https://github.com/GoodStartLabs/AI_Diplomacy) · [Every.to 报道](https://every.to)
