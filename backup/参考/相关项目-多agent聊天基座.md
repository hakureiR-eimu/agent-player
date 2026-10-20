# 相关项目：多 agent 聊天基座

> 调研日期：2026-10-13。与"排除游戏交互后的主体需求"同构的先例项目：**一个宿主程序跑 N 个 agent，每个 agent 接入真实 IM，支持大群发言 / 私聊 / 拉群**。按同构度分三档：真实 IM 载体（最同构）、学术系框架内聊天环境（消息模型可参考）、角色扮演群聊（发言门控可参考）。

## 一、真实 IM 载体的多 agent 互聊（最同构）

### 1. CloseCrab（yangwhale/CloseCrab）— 形态最同构：飞书 + coding agent 进程 + 多 bot 协作

- **是什么**：把 Claude Code / OpenClaw / Kilo / Gemini CLI / DeepSeek Harness 等 coding agent CLI 包装成 24/7 在线的聊天 bot，跑在飞书（一等公民）/ Discord / 钉钉上。Python。飞书为主战场，与我们的平台选择重合
- **架构与我们逐点对应**：**Runtime = 驱动 CLI 进程**（不重实现 agent，直接驱动现成 agent 进程——与我们"每国一个 SDK 子进程"同构）；**turn = 一次消息进来到回复发出的完整往返**（成本单位——与我们流式输入模式的 turn 概念一致）；**Channel 适配层统一各家消息为 `UnifiedMessage`**（对应我们的飞书网关）
- **bot 间协作双通道**：协调通道——Leader 在 `#team-ops` 飞书频道用 @mention 派活、Teammate 完成后 @Leader 汇报（**bot 之间以 IM 频道为协作媒介**，是我们"agent 间通信走飞书"（决策 0003）的工程先例）；异步通道——Firestore inbox 实时推送（on_snapshot，不走 IM 的直连通道）。差异：他们双通道是任务协作的效率选择，我们"唯一信道"是外交玩法的透明性要求
- **四层持久化记忆**：MEMORY.md（身份+偏好+索引，每次注入 system prompt）→ memory/*.md（100+ topic 文件按需读）→ shared/*.md（多 bot 实时共享，gcsfuse 挂载）→ 向量索引（memory_search）。对照我们：thin/（不可变）+ self/ + memory/（agent 自主读写），"常驻薄层 + 按需读厚层"的思路同源；他们多了跨 bot 共享层——我们明确不做（隔离是玩法要求）
- **可借鉴**：多 bot 跨机部署的工程形态；per-user worker 的消息路由（`core/bot.py`）；急刹车机制。**他们无"沉默默认"**——bot 被叫就回，外交场景的发言门控要看 §四 telegram-presence
- 链接：[github.com/yangwhale/CloseCrab](https://github.com/yangwhale/CloseCrab)

### 2. lostsock1/pi-groupchat — pi agent 的 Telegram 多人格群聊（节奏参数清单）

- **是什么**：pi coding agent 的 Telegram 群聊扩展，多 persona 与真人同群聊天。TypeScript，2026-05 一天内写完的项目（3251 行单文件），全部人格共享**一个 bot token**、一个进程、一个内存 transcript。长轮询接入
- **发言门控（纯时间参数 + 协议词）**：LLM 输出 "pass" 即沉默；12 个 Flow 参数控制节奏——humanGracePeriodMs（等人打完 3s）、agentCooldownMs（同人冷却 15s）、globalCooldownMs（任意两条间隔 4s）、maxAgentBurst（无人类输入最多连发 2 条）、selfConversationMaxRounds（agent 互辩最多 4 轮）；发言人按"历史上说得最少的优先"，每轮最多 2 人；每模型断路器
- **可借鉴**：**12 个节奏参数是一份现成的"群聊节奏配置清单"**，pass 协议简单可靠、断路器可抄。差异：共享单 bot（我们一国一应用）、无 DM / 建群、门控全靠冷却时间而非"想不想说"
- 链接：[github.com/lostsock1/pi-groupchat](https://github.com/lostsock1/pi-groupchat)

### 3. clemente-turrubiates/telegram-agent-mcp — 每 agent 一个 bot + hub 总线（含平台限制实证）

- **是什么**：Rust 的 MCP server，让多个 LLM agent 通过共享 Telegram 群协作。**每 agent 一个 bot token**（与我们一国一应用同构），但所有 agent 的 MCP 客户端连同一个 hub 后台进程
- **平台限制实证（重要情报）**：**Telegram Bot API 不把一个 bot 发的消息投给另一个 bot 的 getUpdates**——试遍 @mention、隐私模式关闭、双 admin 均无效，bot-bot DM 直接被拒。他们的解法：agent 间流量不走 Telegram，hub 维护单一共享消息日志（**消息在发送侧即写总线**，其他 agent 立即可见），人类消息正常走轮询
- **对我们的启示**：① 飞书是否同样限制 bot 间消息可见性——**必须列入长连接实测清单**；若同样受限，我们的"宿主收发一切、出站即扇入各 agent 队列"架构天然免疫（我们从不依赖 bot 之间的推送，§六收消息路由本来就是宿主自己分发）——这可以作为宿主扇入架构的选型佐证；② **runaway brake**：最近 1000 条全是 bot 消息时拒绝再阻塞等待，逼 agent 总结收尾——正是我们待定问题"agent×agent 连锁熔断"的现成答案；③ "人类最后发言未被回应时 transcript 加 ⚠ 警告行"——防晾玩家的机制
- 链接：[github.com/clemente-turrubiates/telegram-agent-mcp](https://github.com/clemente-turrubiates/telegram-agent-mcp)

### 4. tigrohvost/telegram-presence — 发言门控的系统性解法（对我们参考价值最高的单点）

- **是什么**：不是编排框架，是从线上自主 agent 实战栈提取的"**agent 群聊出场器官**"——专门解决"agent 要不要说话、说多深"。Python 纯标准库，2026-07 起持续更新（385 个测试）。单 agent 视角库，每个 agent 装一份（恰好映射我们 8 agent 各装一份）
- **机制（一套完整的发言门控）**：
  - **社交预读**：每条消息先让轻量 decider 输出 addressed_to（自己/群/他人/不明）、referent（说的是谁）、置信度——"**被谈论 ≠ 被搭话**"，两者都不强制/禁止发言（对应我们"与我有关吗"判定，但拆得更细）
  - **want/depth 门控**：decider 必须声明 want: yes/no 和 quick/deep；want=no 直接丢弃——"有话要说才说，不出于礼貌"（与我们"沉默是默认"同构，且给出了结构化的判定输出格式）
  - **delegate 升级**：深度问题从轻量草稿升级到完整 composer（KB+记忆+场景+社交预读）——两级响应，对应我们"搪塞 vs 认真谈"
  - **burst 合并**：同人连发合并为一个候选，回复锚定被指名那条——对应我们"攒批"待定项
  - **wait**：话轮还在流动时暂存已成形的话（有限次）——"等别人说完"
  - 决策全记 jsonl 日志（内心想法只存哈希）——决策可审计
- **可借鉴**：want/depth 输出契约可直接搬进 agent prompt 契约 + 宿主策略层；与实现语言无关。差异：不管多 agent 编排与建群
- 链接：[github.com/tigrohvost/telegram-presence](https://github.com/tigrohvost/telegram-presence)

### 5. wthislifehuh/lark-acp-bridge — 飞书 bot ↔ coding agent 单桥先例

- **是什么**：把飞书 bot 桥接到任何 ACP（Agent Client Protocol）agent——Claude Code、Codex、Gemini CLI 等。TypeScript/npm 发布，源自 4t145/lark-acp。官方 Lark CLI 的推荐搭配
- **可借鉴**：① **把 chat context（chat id、发送者名、群名）注入 agent prompt**——与我们 §六"环境头 + 事件本身"的注入设计互相印证；② 跨重启 session resume、任务打断、工具授权都在飞书卡片内交互——飞书交互形态的成熟参考；③ 验证了"飞书消息 → 本地 agent 会话"的通路形态（单 bot）
- 链接：[github.com/wthislifehuh/lark-acp-bridge](https://github.com/wthislifehuh/lark-acp-bridge)

### 6. openclaw/openclaw（39 万 stars）— 问题域几乎重合：TS 宿主 + 飞书多账号 + 多 agent 共群

- **是什么**：个人 AI agent 网关（原 Moltbot/Clawdbot，现为基金会项目），TypeScript/Node，极活跃。单一 Gateway 进程接入 WhatsApp / Telegram / Discord / **飞书**（官方插件 `@openclaw/feishu`，DM+群聊标称 production-ready）/ Slack / iMessage 等渠道
- **三层解耦的身份模型**：`agents.entries`（agentId = 一个人格边界：独立 workspace、独立 SQLite 会话库）× `channels.<ch>.accounts`（accountId = 渠道账号实例，**一个 Gateway 配 8 个飞书 appId/appSecret 完全支持**）× `bindings`（按 (channel, accountId, peer) 最具体匹配路由到 agentId）——**就是我们"一国一应用 × 一国一 agent × 会话路由"的身份层原型**。飞书传输默认 WebSocket 长连接（无需公网 URL），webhook 可选——与我们长连接定案（§四）互相印证
- **飞书 bot 互听的硬约束（对我们的最重要情报，详见 §四汇总）**：飞书默认忽略其他 bot 的消息；要收到须加 `im:message.group_at_msg.include_bot:readonly` + `im:message:readonly` 权限并开 `allowBots`，且**飞书只在"对方 bot @ 了本 bot"时才投递**；bot 之间不能互发私聊。OpenClaw 的对策：回复时自动 @ 对方、丢弃自己发的消息、pair 级防环
- **防死循环（连锁熔断的现成答案）**：核心入站 runner 追踪 **bot 对**（A→B 与 B→A 算同一对），滑动窗口预算（默认 20 事件/60 秒），超限冷却（默认 60 秒抑制），可按 channel/account/room 覆盖
- **broadcast groups（同群多 agent，实验特性）**：一条入站消息扇出给最多 16 个 agent 各自独立 session；`maxRounds ≤ 4`、`maxTurns ≤ 32` 回合预算；后续轮靠"兄弟回复摘要"（单条 4000 字符上限）注入；prompt 要求无新意即回 `NO_REPLY`——公屏回合制的现成模型（对照我们：无 NO_REPLY 需求——我们沉默就是不发工具调用）
- **差异**：面向单操作者的个人助理，agent 间主流通道在进程内（tools.agentToAgent、A2A JSON-RPC）而非 IM——违背我们"IM 唯一信道"（决策 0003，那是外交玩法的透明性要求）；broadcast 是协调者内部扇出，不是对等多边外交
- **必读文档**：`docs/channels/bot-loop-protection.md`、`docs/channels/broadcast-groups.md`、`docs/channels/feishu/access-control.md`（bot-authored messages 一节）、`docs/channels/feishu/advanced-configuration.md`（多账号）
- 链接：[github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)

### 7. langbot-app/LangBot（1.8 万 stars）— 多平台 IM bot 的工程范式（飞书适配成熟度标杆）

- **是什么**：生产级多平台 LLM 聊天机器人平台，Python/asyncio + React 控制台，2022 年至今极活跃。20+ 平台适配器（飞书/Discord/Telegram/Slack/微信/企微/QQ/钉钉/Matrix…），流水线引擎、RAG、插件系统、MCP、多租户
- **多账号架构**：适配器 = Python 模块 + **YAML 声明式清单**（配置 schema，面板动态渲染表单）；`botmgr.py` 的 PlatformManager 为每个 bot 实例生成一个 RuntimeBot 长驻 asyncio 任务——**一个平台同时跑多个 bot 账号（如 8 个飞书应用各带凭据）**。消息流：适配器 → RuntimeBot（路由规则选 pipeline）→ MessageAggregator（**N→1 攒批**）→ QueryPool → Controller（**按会话并发控制**）→ Pipeline → LLM → 原路回复。飞书适配：**WS 长连接默认**、webhook 可选、流式卡片、扫码建应用——验证了"多实例 WS 长连接并存"的可行性
- **定位（中等参考价值）**：它是"人来消息 → 一个 AI 应答"的**单向应答架构**，没有多 AI 同群互聊、发言权、回合制语义，主动私聊/建群拉人也不是核心能力。价值在工程范式：声明式适配器、RuntimeBot 生命周期、消息聚合与会话并发控制——自己写飞书适配层时的参照。不作为框架底座
- 链接：[github.com/langbot-app/LangBot](https://github.com/langbot-app/LangBot)

## 二、学术系框架内聊天环境（消息模型可参考）

### 8. tsinghua-fib-lab/AgentSociety（1.3k stars）— P2P/P2G/群聊三层消息 + tick 分发 + 深度限制

- **是什么**：LLM-native 社会模拟平台（AgentSociety 2），社会科学研究用。消息层显式支持**点对点（P2P）、点对群（P2G）、群聊**三种交互——正是我们"私聊 / 拉群 / 公屏"的学术版
- **消息机制**：发布-订阅 + Ray 分布式；每个模拟 tick 内 agent 发的消息进待处理队列 → 拦截器验证/修改/阻止（MessageInterceptor——研究干预用，映照我们的发言限流/硬约束）→ 分发给目标 agent → agent 处理器持久化 + 触发响应。**消息深度限制防指数级传播**（传播计数机制）——我们待定问题"连锁熔断"的又一先例
- **差异**：tick 批量节奏是模拟器的节拍器（我们无心跳、事件驱动逐条即时——外交场景要实时性，但"每 turn 收集→分发"的批处理思想在攒批场景有用）；框架内模拟 IM，非真实 IM 载体
- 链接：[github.com/tsinghua-fib-lab/AgentSociety](https://github.com/tsinghua-fib-lab/AgentSociety)

### 9. camel-ai/OASIS（5.3k stars）— 把"消息可见性"当一等问题的社交模拟

- **是什么**：CAMEL-AI 的开源社交媒体模拟器（Twitter/Reddit 风格，百万级 agent），研究信息传播用。Python，活跃（2025 年仍在新功能），配套论文 arXiv 2411.11581
- **消息/社交模型**：33 个 ActionType（发帖/评论/点赞/转发/关注/屏蔽/采访……），**2025-06 加入群聊五件套：CREATE_GROUP / JOIN_GROUP / LEAVE_GROUP / SEND_TO_GROUP / LISTEN_FROM_GROUP**——"拉群"场景的同构物，可对照设计我们的受限操作接口。无一对一 DM（群聊是最近似物）。**消息可见性是核心设计**：平台 SQLite 数据库是唯一事实源，agent 每步 REFRESH 拉时间线，看到什么由关注图 + 推荐系统决定——不是广播而是"平台筛选后投喂"（映照决策 0004：会话可见性＝群成员制，由宿主这一层筛选）
- **编排**：全局同步 tick，`OasisEnv.step(actions)` 内被激活 agent 经 `asyncio.gather` 并发执行；agent 与平台之间用 `Channel` 通信——**按 message_id 配对的 async RPC**（对应"宿主代 agent 调飞书 API 收发"）；LLM 调用 Semaphore(128) 限流；动作 trace 全量落库可审计
- **可借鉴**：Channel 请求-响应配对模型；平台 DB 唯一事实源 + trace 审计（对应飞书侧会话状态存储与回放）；群聊 action 集的粒度。不适用：同步 tick（我们事件驱动）、推荐系统（8 人群全可见）、百万级扩容工程
- 链接：[github.com/camel-ai/oasis](https://github.com/camel-ai/oasis)（群聊样例 `examples/group_chat_simulation.py`）

### 10. microsoft/TinyTroupe（7.6k stars）— 深人格小群体 + 记忆三层的先例

- **是什么**：微软 LLM 多人格模拟库：TinyPerson（人格化模拟人）在 TinyWorld 里互动，主打商业模拟（焦点小组、广告评估）。Python，MIT，论文 arXiv 2507.09788
- **消息模型**：每 step 各 agent 产出 JSON 动作（TALK / REACH_OUT / SHOW / DONE），环境解释执行——**TALK 带 target 定向投递（等价私聊）、不带 target 广播全房间（等价公屏），一套动作模型两种通道**；**REACH_OUT：agent 默认互相不可见，先建立关系才可见**（对外交网络演化有启发——我们 MVP 直接全员群，但"关系先于可见性"是远期方向）
- **人格定义（对角色书的直接参考）**：persona JSON schema（年龄/职业{title,organization,description}/style/personality{traits+big_five}/long_term_goals/preferences/beliefs/behaviors）+ **fragment 片段跨 agent 复用**（如"旅行爱好者"子规格——对应我们"共用骨架 + 风味包"的生产方式）；TinyPersonFactory 可 LLM 批量生成人格（对应 0005 薄层生产）
- **记忆三层**：EpisodicMemory（**固定前缀 20 条 + 最近 100 条进 prompt**）、SemanticMemory（向量检索 top-k）、**EpisodicConsolidator（LLM 把情节记忆固化成 facts/impressions，带 timestamp**）——正是长战役外交的记忆管理方案，对照我们"近期保原文、远期保摘要"（agent需求 §2.3），其固化器是一个可抄的实现形态
- **可借鉴**：TALK 二分法、persona schema + fragment、记忆三层与固化器。不适用：同步 run(steps) 轮次、进程内函数直投（无真实 IM 的投递失败/乱序/身份问题——**这块没有先例可抄，恰是我们要自己解决的**）
- 链接：[github.com/microsoft/TinyTroupe](https://github.com/microsoft/TinyTroupe)

### 11. Farama-Foundation/ChatArena（1.6k stars，已废弃）— visible_to：把可见性做成消息的一等属性

- **是什么**：LLM 多智能体语言游戏库（gym/MDP 风格 + 现成游戏环境 + Web UI），2023 出品，**2025-08 官方宣布废弃**。虽废，抽象干净
- **消息模型**：全局单一 `MessagePool`，每条 `Message` 带 **`visible_to: str|List[str] = "all"`**——一条消息可声明广播 / 点对点 / 组播（名单）。agent 不直接寻址发送：回合主循环把消息写进池，每个玩家用 `get_visible_messages(agent_name, turn)` 读自己的视图（只能看到"当前回合之前 + visible_to 含自己"；Moderator 全知）。**"私聊 vs 群聊"不是独立信道，而是同一池内的可见性过滤**——语义上直接映射飞书投递：群消息＝群成员名单、私聊＝[对方]、拉新群＝新可见域。Chameleon 环境是实战范例（秘密词只对非变色龙可见、投票只对投票者可见——同池共存多层秘密）
- **环境抽象**：`Environment`（reset/step/get_next_player/check_action/is_terminal）+ `Arena` 封装；**玩家只见 observation 不见全局状态；动作先 check_action 校验，无效重试 5 次判负**——受限动作接口的雏形（对照我们白名单动作 + 失败回执）
- **改造判断**：保留 `visible_to` 语义与"只见 observation + 动作校验"两原则；中央池轮询过滤换成真实 IM 的事件驱动投递（飞书自己就是投递层），`get_next_player` 回合调度删掉（真实 IM 谁想说谁说）
- 链接：[github.com/Farama-Foundation/ChatArena](https://github.com/Farama-Foundation/ChatArena)

### 12. sotopia-lab/sotopia（ICLR 2024 spotlight，活跃维护）— per-viewer 信息分级：外交信息不对称的正中要题

- **是什么**：开放式社交智能模拟环境（双人/小组社交互动，评估并训练社交智能），Python + Redis 持久化，2026-06 仍在更新。主题就是谈判 / 合作 / 背叛
- **消息模型**：环境与 agent 各有 inbox（无路由，整箱拼成自然语言 history 喂 LLM）；回合制批处理 `step(actions)`，action_order = simultaneous / round-robin / random + action_mask 控制发言权
- **可见性（最大亮点）**：文本可嵌 **XML viewer 标签（`<p viewer='agent_1'>…</p>`），XMLRenderer 按收件人渲染——agent 只见带自己标签或无标签的内容**，环境见全部。即"**不同人看到同一文本的不同版本**"，比布尔式可见性强一档——直接可用于"角色书 + 国家目标 + 对各国认知档案"的分级披露
- **社交目标与心智模型**：`EnvironmentProfile.agent_goals` 每个 agent 一条自然语言 goal，非 omniscient 模式下别人的 goal 渲染为 "Unknown"（**目标私有化**）；`AgentProfile` 含 **secret 字段**；`RelationshipType`（stranger→acquaintance→friend…）决定 `get_bio` 对你可见的段落——**关系决定信息披露梯度**（对照我们态度档案 + 信任演化）；LLM evaluator 做终止判定与终局打分（可做外交回合裁判）；HumanAgent 与 LLMAgent 同接口人机同场
- **改造判断**：保留 per-viewer 渲染、goal 私有化、关系披露梯度、LLM 裁判；换掉单房间静态拓扑（我们要动态建群）与同步回合调度
- 链接：[github.com/sotopia-lab/sotopia](https://github.com/sotopia-lab/sotopia)

## 五、综合判断

**没有一个先例完整覆盖我们的问题域**——真实 IM 载体 + 对等多边外交 + 玩法级信息不对称 + 事件驱动沉默默认，四者交集是空档，恰是本项目要自己解决的。但四个侧面各有最佳参考：

| 侧面 | 最值得参考 | 次选 | 理由 |
|------|-----------|------|------|
| 宿主架构（飞书 + CLI 进程 + 多 bot） | **OpenClaw**（多账号/bindings/防环/长连接默认） | CloseCrab（飞书一等公民 + turn 成本单位） | TS 同栈、飞书生产实证 |
| 公屏消息送达 | **telegram-agent-mcp**（发送侧写总线） | OpenClaw broadcast（扇出 + 回合预算） | bot 互不投递的平台事实下的同解法 |
| 发言门控（沉默默认） | **telegram-presence**（want/depth + 社交预读） | SillyTavern（talkativeness）、pi-groupchat（节奏参数） | 唯一把"要不要开口"当第一性问题的 |
| 信息不对称 / 会话模型 | **sotopia**（per-viewer 渲染 + goal 私有化） | ChatArena（visible_to）、OASIS（可见性一等 + 群聊 action 集） | 不同人看到不同版本 > 布尔可见性 |

**对既有定案的佐证与修正**（详见《飞书接入.md》2026-10-13 调研修订）：

- 佐证：WS 长连接默认（LangBot/OpenClaw 双源）；宿主统一收发（hub/总线三处同构）；沉默默认与门控（三档先例）；白名单动作 + 失败回执（ChatArena check_action）
- **修正：收消息必须双路**——bot 互不投递（Telegram 实证、飞书高置信）意味着"群内 agent 互相看见"不能依赖飞书推送，须由宿主在 send 成功后扇入其他成员国；玩家消息照走长连接推送

## 三、角色扮演群聊（发言门控的另一来源）

### 13. SillyTavern 群聊模式 — Talkativeness 与防自触发

- **是什么**：单 LLM 上下文内模拟多角色卡轮流发言的群聊（非多 agent——一个上下文装多个角色轮流生成），但**发言门控策略经过海量用户实测**：
  - **Reply order strategies**：Manual / **Natural Order**（提取 @mention → Talkativeness 概率 → 随机兜底）/ List / Pooled
  - **Talkativeness（话痨度 0-100%）**：每角色一个"多话程度"参数——量化"沉默是默认"的现成先例（对照我们"探索期话多、开发期隐身"的阶段基调，可以给阶段配 talkativeness 档位）
  - **Allow Self Responses 默认关**——防自触发死循环
  - 群成员动态管理（加/移除/静音/排序）——"拉群"的 UI 版
- **对我们的定位**：机制级参考（门控参数化、防自触发），不是架构参考
- 链接：[docs.sillytavern.app — Group Chats](https://docs.sillytavern.app/usage/core-concepts/groupchats/)

## 四、平台限制情报（跨项目实证汇总，落地前以本地实测为准）

**bot 之间互相收不到消息——Telegram 与飞书皆然，这是"多 agent 同群"的第一平台事实**：

- **Telegram**（telegram-agent-mcp 实证）：Bot API 不把一个 bot 发的消息投给另一个 bot 的 getUpdates，@mention / 隐私模式 / 双 admin 均绕不过，bot-bot DM 直接被拒
- **飞书**（OpenClaw 生产文档，高置信线索）：飞书默认忽略其他 bot 的消息；要收到须给应用加 `im:message.group_at_msg.include_bot:readonly` + `im:message:readonly` 权限并开 `allowBots`，且**只在"对方 bot @ 了本 bot"时才投递**该事件；bot 之间不能互发私聊。（2026-10-13 补查佐证：[feishu-bot-relay](https://github.com/sendwealth/feishu-bot-relay) 中转项目的立项依据即"bot A 在群内 @ bot B，B 收不到任何消息事件"——有人专门造轮子绕过，最强的行为证据；[V2EX t/1194837](https://www.v2ex.com/t/1194837) 同；[官方文档](https://open.feishu.cn/document/faq/bot?lang=zh-CN)消息事件模型仅面向"用户→机器人"方向，无 bot↔bot 支持明文）→ 语义：即使配齐权限，**"agent A 在群里不 @ 地发言，agent B 的长连接也收不到"**
- **对我们的直接推论**：不能依赖飞书推送实现"群内 agent 互相看见"，须走**宿主发送侧扇入**——agent 的发言本来就要经宿主的 `send_message` 工具（闭包绑定本国凭据）发出，发送成功后由**宿主直接把该消息作为事件注入群内其他成员国的会话**（telegram-agent-mcp 的"发送侧写总线"、OpenClaw broadcast 的"协调者扇出"都是同一解法）。于是收消息分两路：**玩家消息走飞书长连接推送（按群成员 bot 路由），agent 消息走宿主扇入**。这不违反决策 0003——消息以飞书消息形态真实存在于群里（玩家全程可见），只是"送达其他 agent"这一跳由宿主完成；对 agent 而言它只是"在群里看到有人说话"，与眼中皆玩家定案相容
- **待本地实测**（列入《飞书接入.md》待定问题清单）：① 上述权限与 @ 投递行为在长连接（WSClient）模式下是否一致；② 玩家消息在群/私聊/被拉群三通道下的事件类型覆盖；③ bot 建群、拉 bot 入群的行为

**防死循环（agent×agent 连锁）的三个先例档位**：纯时间参数（pi-groupchat：冷却 + maxBurst + 互辩轮上限）→ pair 级滑动窗口预算（OpenClaw：bot 对 20 事件/60s + 冷却 60s）→ 回合预算 + 摘要注入 + NO_REPLY（OpenClaw broadcast：maxRounds≤4 / maxTurns≤32）。我们是事件驱动 + 沉默默认，最接近第三档的形状，但无 NO_REPLY 需求——沉默就是不调用发送工具

## 来源汇总

- 真实 IM 载体：[openclaw/openclaw](https://github.com/openclaw/openclaw) · [langbot-app/LangBot](https://github.com/langbot-app/LangBot) · [yangwhale/CloseCrab](https://github.com/yangwhale/CloseCrab) · [lostsock1/pi-groupchat](https://github.com/lostsock1/pi-groupchat) · [clemente-turrubiates/telegram-agent-mcp](https://github.com/clemente-turrubiates/telegram-agent-mcp) · [tigrohvost/telegram-presence](https://github.com/tigrohvost/telegram-presence) · [wthislifehuh/lark-acp-bridge](https://github.com/wthislifehuh/lark-acp-bridge)
- 学术系：[Farama-Foundation/ChatArena](https://github.com/Farama-Foundation/ChatArena) · [sotopia-lab/sotopia](https://github.com/sotopia-lab/sotopia) · [tsinghua-fib-lab/AgentSociety](https://github.com/tsinghua-fib-lab/AgentSociety) · [camel-ai/oasis](https://github.com/camel-ai/oasis) · [microsoft/TinyTroupe](https://github.com/microsoft/TinyTroupe)
- 角色扮演：[SillyTavern Group Chats 文档](https://docs.sillytavern.app/usage/core-concepts/groupchats/)
