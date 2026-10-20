# 相关项目：Claude Agent SDK 实践

> 调研日期：2026-10-20。定位：**已用 Claude Agent SDK 实际构建的 agent 项目**，作为《主体程序需求》SDK 落点的参照——此前设计是在真空里推演 SDK 用法，本文补上实盘对照。按证据等级分档（沿用"官方一等、同类项目二等"的惯例）：官方示范 demos（一等）、SDK 仓库自带参考实现（一等）、社区实践（二等）、演进情报（二等，待本地验证）。文末另记**排除项**（看似 SDK 实则不是，防止后续调研走弯路）与**性能情报**（对"按需 resume 成本"待定问题的首个外部数据）。

## 一、官方示范（anthropics/claude-agent-sdk-demos）

### 1. email-agent — 与主体程序需求最同构的官方示范（逐点对照）

- **是什么**：Anthropic 官方 demo——邮件客户端接 Claude Agent SDK（TS，Bun/Node），WebSocket UI + IMAP 收发 + 自定义工具。官方定位"本地开发用，非生产"，但机制是 Anthropic 亲手示范的标准姿势
- **按需 resume 的官方实现**（`ccsdk/session.ts` 的 `addUserMessage`）：每条用户消息一次 `query()`——有 `sdkSessionId` 就带 `resume`，没有就新建；session id 从流中 `system/init` 消息捕获；收到 `result` 即本轮结束。**会话不常驻、每事件一个 turn**——正是决策 0006 进程模型的官方印证，且代码量很小（Session 类约百行）
- **串行化的最简实现**：`queryPromise` 互斥——上一条消息没跑完（Promise 非 null）就先 `await` 它，跑完才开下一轮。**主体程序需求 §六"国级串行"的官方同构物，不到二十行**；我们的"攒批合并"是它的超集（它逐条处理不合并）
- **内存 MCP 的官方姿势**（`ccsdk/custom-tools.ts`）：`createSdkMcpServer({ name, version, tools: [tool(名, 描述, zodSchema, execute)] })`，实例直接传 `options.mcpServers.email`——不走 stdio、进程内。与 §5.2 已核对的用法一致，官方实盘验证
- **PreToolUse hook 做路径约束**：matcher `"Write|Edit|MultiEdit"`，钩子内检查 `tool_input.file_path`，越界目录返回 `{ decision: "block", stopReason: "…must be written to <目录>…", continue: false }`——**把"只能写指定目录"做成硬约束并把正确路径告诉模型**，与 §二第 2 层沙箱路径校验同构（他们防的是写错地方，我们防的是越界窥探，机制相同）
- **大结果落文件、工具只返回路径+摘要**：`search_inbox` 把全量结果写 `logs/*.json`，返回体只有 `{ totalResults, logFilePath }`——与 §六"快照通知式注入"（全量落 `world/`、事件体只有两三行）是同一手法，官方背书了"工具返回大 payload 会灌爆上下文"的判断
- **工具面控制用的是 `allowedTools` 白名单**（放行 `mcp__email__*` + 一批内置工具），不是 `tools: []`。两条路线都通：我们的 `tools: []` 全卸更严格（模型看不到任何内置工具），官方 demo 的白名单更宽松。维持我们的选择，此处仅记录官方实际姿势
- **inbox 的官方同构物**：`MessageQueue<T>`（push/next/close，约 40 行手写）——事件队列不需要重设施
- **差异**：单 agent 单会话、无多国隔离、无凭据闭包绑定（EmailAPI 是 lazy import，不按"国"闭包）——这些都是我们的增量，官方示范只覆盖到"事件 → 按需 resume 的 SDK 会话"这一段
- 链接：[anthropics/claude-agent-sdk-demos/email-agent](https://github.com/anthropics/claude-agent-sdk-demos/tree/master/email-agent)

### 2. simple-chatapp — 流式输入常驻模式的官方示范（另一选项的实证）

- **是什么**：官方最简聊天应用 demo。`query()` 的 `prompt` 传 **AsyncIterable**（自写带 `[Symbol.asyncIterator]` 的队列），构造函数里立即启动 query，输入流不关闭、子进程常驻；`sendMessage` 就是往队列 push 一条
- **对我们的意义**：§5.2 待定项"单次 query 传 AsyncIterable（yield 本轮合并消息后即关闭）以保 canUseTool 流式模式"——官方 demo 证明该模式可行，且展示了**常驻**端点的形态（若 12s/query 开销（见 §五）实测不可接受，"高峰期短暂常驻"的应急形态有官方示范可依）
- **差异**：常驻进程正是决策 0006 放弃的模型（无事件也占资源）；它单会话、`allowedTools` 放行全套内置工具，仅作模式参照
- 链接：[anthropics/claude-agent-sdk-demos/simple-chatapp](https://github.com/anthropics/claude-agent-sdk-demos/tree/master/simple-chatapp)

### 3. hello-world-v2 — v2 API：会话对象化，resume 一等公民

- **是什么**：SDK v2 接口的官方示例：`unstable_v2_createSession()` / `unstable_v2_resumeSession(sessionId)` / `unstable_v2_prompt()`；session 对象上 `await session.send(...)` + `for await (msg of session.stream())`，`await using` 自动清理——**比 v1 手动 `query({ resume })` 更贴合"会话集"模型**（每窗口会话/内心会话天然映射为一个 session 对象的生死）
- **风险**：函数带 `unstable_` 前缀，API 未稳定；采用则必须锁 SDK 版本
- 链接：[anthropics/claude-agent-sdk-demos/hello-world-v2](https://github.com/anthropics/claude-agent-sdk-demos/tree/master/hello-world-v2)

## 二、SDK 仓库自带参考实现（anthropics/claude-agent-sdk-typescript）

### 4. examples/session-stores — transcript 自管存储（对局档案的新落点）

- **是什么**：SDK 的 `sessionStore` 选项（`query({ options: { sessionStore } })`）参考适配器：S3 / Redis / Postgres 三份，附 13 项行为契约一致性测试（`shared/conformance.ts`）。官方定位"复制进你的项目改用"，非发布包
- **接口形状**：`append()`（增量写）/ `load()`（全量读）/ `delete()`；append 失败只记流错误、不阻塞对话；SDK 不主动删，留存策略自理
- **对我们的意义（修正机会）**：主体程序需求 §六现依赖"harness 自动落 JSONL 于 `~/.claude/projects/`"——位置与格式由 harness 固定、还会被 CLI `cleanupPeriodDays` 独立清扫。**自写一个 FileSessionStore 把 transcript 直接落 `runtime/<TAG>/` 即可把对局档案（§七）收进自家目录**：沙箱、inbox、transcript 一体留存，不受外部清理策略影响，续局 resume 走同一 store。13 项契约照 conformance 套件自测即可
- **细节可借**：JSONB/多写者时钟偏差等坑README 已列（本地文件存储天然避开）
- 链接：[anthropics/claude-agent-sdk-typescript/examples/session-stores](https://github.com/anthropics/claude-agent-sdk-typescript/tree/master/examples/session-stores)

## 三、社区实践（二等证据）

### 5. chrisleekr/github-app — 事件驱动长驻服务（外部事件源 → SDK）

- **是什么**：GitHub App 监听 PR/issue 的 bot mention，用 SDK（`@anthropic-ai/claude-agent-sdk` + MCP servers）自主应答。形态与"飞书事件 → 宿主 → SDK 会话"同构（webhook 事件源替代飞书长连接）。小众项目，机制细节未深读——形态参考即可
- 链接：[github.com/chrisleekr/github-app](https://github.com/chrisleekr/github-app)

### 6. MetaMask/agent-runner — 企业封装：SDK 生命周期可观测

- **是什么**：MetaMask 开源的 SDK 封装 runner（TS），带 Langfuse/OpenTelemetry 生命周期集成——把"跑一个 agent 会话"包成可复用单元并全链路观测。README 细节未取得（仓库未被 zread 收录），作为"企业怎么包 SDK"的存在性证据与后续可深挖项
- 链接：[github.com/MetaMask/agent-runner](https://github.com/MetaMask/agent-runner)

### 7. SDK 演进情报（claude-world 2026-03 综述；Python 版先行、TS 基本对齐——待本地 `.d.ts` 验证）

- **会话历史读取**：`list_sessions()` / `get_session_messages()`——不碰 JSONL 文件读全部会话与消息（纯文件系统操作，无需活进程）。§六"审计日志"的官方姿势补充：不必自消费 SDKMessage 流也能事后回放
- **MCP 运行时增删**：会话中途 `add/remove/toggle/reconnect_mcp_server`——工具面可动态收放（我们暂无此需求：一国工具面开局定死，留档备查）
- **hook 输入带 `agent_id` / `agent_type`**：多 agent 并行时工具调用的归属识别——若未来用 Task 子 agent，hook 层可分辨
- **`ResultMessage.stop_reason`**：turn 结束原因结构化——inbox 的 ack 判定可多一个信号
- **版本敏感实证**：字符串 prompt 曾致 MCP server 初始化失败（v0.1.46 修复）；未知消息类型曾直接崩会话（v0.1.40 修复，改为静默跳过）——**落地时锁版本、升级单独验证**，列入主体程序需求 §5.2 已有的"以本地 `.d.ts` 复核"口径
- 来源：[claude-world.com/articles/agent-sdk-session-mcp-update](https://claude-world.com/articles/agent-sdk-session-mcp-update)

## 四、排除项（看似 SDK 实则不是——防后续调研走弯路）

- **OpenClaw**：agent 部分是自研 harness（`llm-core` + provider transport 直连各 API），**不用 Claude Agent SDK**。其网关/多账号/bindings/防环的参照价值已在《相关项目-多agent聊天基座》记档；SDK 用法层面无参照价值
- **vibe-kanban**：Rust 后端 spawn 各家 CLI 的编排器（`StandardCodingAgentExecutor`），非 SDK；且项目已关停（2026，官方公告找不到商业模式）
- **CloseCrab / lark-acp-bridge**：驱动现成 CLI / ACP 协议，非 SDK（此前调研已知，此处归档口径）

## 五、性能情报：每 query 启动开销（"按需 resume 成本"待定问题的首个外部数据）

- **[issue #34](https://github.com/anthropics/claude-agent-sdk-typescript/issues/34)（2025-10，Windows 11 实测）**：`query()` 每次调用约 **12s 启动开销**，无热进程复用（旧版 SDK 约 40s，新版降到 12s）；issue 定位 HIGHEST PRIORITY，社区要求 daemon/进程池模式——截至该期未落地
- **解读**（推断部分待实测）：12s 主要是**延迟**成本（子进程拉起 + CLI 初始化），不是 token 成本；token 成本取决于 prompt cache 命中，而 **prompt cache 在服务端、跨进程理论上可命中**（5 分钟 TTL 是硬约束——事件稀疏时过期，密集谈判时可命中）。这直接待实测验证主体程序需求待定问题②的"cache 跨进程命中"
- **对我们场景的影响评估**：外交事件频率远低于实时聊天（一国一天几十个事件量级），12s 首响应在"国家正在考虑"的语境下大概率可接受；但**密集谈判往返**（玩家连发、多国连环）会显钝。MVP 实测应包含：① Windows 下每次 query 实测开销；② resume 后 cache 命中率（`cache_read_input_tokens`）；③ 不可接受时的缓解序位——v2 `resumeSession` 是否更快 → 高峰期短暂常驻（simple-chatapp 模式）→ 回常驻模型（决策 0006 回退）
- **注意时效**：该 issue 数据是 2025-10 的（距今一年），SDK 已迭代多版（issue #34 之后至少 350+ issue），现状须以本地实测为准

## 六、对本项目定案的佐证与修正

**佐证**（设计未偏离官方姿势）：

- 按需 resume（决策 0006）：email-agent 官方示范同款，v2 API 更把 `resumeSession` 提为一等公民
- 国级串行（§六）：`queryPromise` 互斥即最简实现，官方同构
- 内存 MCP + PreToolUse 路径约束（§5.2、§二）：官方 demo 实战了完整链路（createSdkMcpServer + tool + zod + hook block + stopReason 回传）
- 快照通知式注入（§六）：官方"大结果落文件、返回只带路径"同款
- inbox/事件队列（§六）：手写 `MessageQueue` 级别的小设施即可，不需要重中间件

**修正/新增机会**（择要，是否采纳另议）：

1. **sessionStore 自管 transcript**：自写 FileSessionStore 把 transcript 落 `runtime/<TAG>/`——对局档案一体化，摆脱 `~/.claude/projects/` 位置依赖与 `cleanupPeriodDays` 清扫风险；13 项契约有官方 conformance 套件可自测
2. **v2 API 优先试**：session 对象（send/stream）比裸 `query({resume})` 更贴合会话集模型；代价是 unstable，须锁版本
3. **12s/query 开销进实测清单**：作为待定问题②的外部基线，实测项补"密集谈判往返下的体验"与"cache 命中率"
4. 会话历史 `list_sessions`/`get_session_messages`：审计/回放可后置到局末做，不必实时消费 SDKMessage 流

## 来源汇总

- 官方：[anthropics/claude-agent-sdk-demos](https://github.com/anthropics/claude-agent-sdk-demos)（email-agent / simple-chatapp / hello-world-v2）· [anthropics/claude-agent-sdk-typescript/examples/session-stores](https://github.com/anthropics/claude-agent-sdk-typescript/tree/master/examples/session-stores) · [issue #34 性能](https://github.com/anthropics/claude-agent-sdk-typescript/issues/34)
- 社区：[chrisleekr/github-app](https://github.com/chrisleekr/github-app) · [MetaMask/agent-runner](https://github.com/MetaMask/agent-runner) · [claude-world SDK 综述](https://claude-world.com/articles/agent-sdk-session-mcp-update)
