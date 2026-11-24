# LLM 操作游戏调研（2026-11-24）

## 1. 结论

「让 LLM 读游戏局势、在游戏里做动作」这件事，按游戏给外部程序留的口子分四条路线：官方调试接口、mod 脚本桥、模拟器/引擎级、像素+键鼠。PDX 游戏没有官方外部通道，只能走 mod 脚本桥——与本项目的 error.log 导出＋博弈按钮同一谱系，且该谱系已有跑通整局的先例。

对本项目最有分量的两个先例：

- **Vox Deorum（文明5）**：混合 LLM+X 架构——LLM 只做宏观决策（调 5 个工具），战术执行全部留给游戏算法 AI。2327 局完整对局、胜率与算法 AI 统计打平、成本约 $0.86/局。这正是本项目「agent 定方向、操作留给游戏原生 AI」的路线，已被验证可行。
- **Voices of the Court（CK3）**：与 Vic3 同引擎（Jomini）。读侧走游戏日志文件，写侧走「命令文件轮询＋预定义动作白名单」。证明 Jomini 引擎上文件通道足以撑起万人用的 mod。

写侧缺的那一截（harness 发请求→游戏执行），别人的做法就两种，见 §5。

## 2. 四条路线总览

| 路线 | 通道 | 代表 | 适用前提 |
|---|---|---|---|
| 官方调试接口 | 游戏自带网络端口，外部进程直连 | Civ6 FireTuner（TCP 4318）、星际2 官方 API | 游戏厂商留了口子；Vic3 没有 |
| mod 脚本桥 | 游戏内 mod 做执行器，外部进程经文件/管道握手 | Vox Deorum、Voices of the Court、本项目 | 游戏可 mod 且脚本能触发 effect；PDX 系唯一可行路线 |
| 模拟器/引擎级 | 模拟器暴露内存与按键 API | 宝可梦（GPT-4 通关、Gemini Plays Pokémon） | 游戏跑在可控的模拟器里 |
| 像素+键鼠 | 截图给模型看、虚拟按键操作 | Claude Plays Pokémon、SIMA 2 | 什么都不用改，但最脆、最贵 |

## 3. 各项目实现细节

### 3.1 文明6：civ6-mcp

[lmwilki/civ6-mcp](https://github.com/lmwilki/civ6-mcp)——MCP server 让 LLM 玩完整局文明6，76 个工具覆盖单位、城市、地图、科研、外交、贸易、政体、总督、宗教、伟人、世界议会、胜负进度、存读档与回合结束，可接 Claude Code 直接玩。

- **通道**：Civ6 开启 FireTuner 调试后，游戏自身监听 TCP 4318（需装 Civ6 SDK，Windows 上 tuner 服务端属于 SDK 而非本体；连接挂掉常要重启游戏进程）。MCP server 与之保持一条长连接。
- **读**：server 运行时生成 Lua 代码，送进游戏的 GameCore Lua 虚拟机执行，取回结构化状态。
- **写**：同样生成 Lua，送进 InGame 虚拟机发玩家命令；规则由引擎强制，README 明言「no cheats, no vision model required」。
- **给 LLM 的形态**：叙述性文本（narrated text），不是原始数据。
- **闭环**：`end_turn` 自动做前后快照，报告本回合发生了什么（单位损血、城市增长、威胁出现）——每回合自动给 agent 一次复盘。
- 仓库附 AGENTS.md 给 agent 的玩法手册（回合循环、战斗、外交、常见坑），并有配套回放 web 应用。

### 3.2 文明5：Vox Deorum（本项目最直接的参照）

[CIVITAS-John/vox-deorum](https://github.com/CIVITAS-John/vox-deorum)，[论文](https://arxiv.org/abs/2512.18564)（FDG 2026）。基于 Vox Populi mod（含社区 DLL）。

- **通道**：游戏内部机制暴露成 Windows 命名管道 → REST API → MCP server → MCP client 起 LLM。
- **分工**：LLM 每次决策只调 5 个工具——`set-strategy`（大战略/经济/军事策略）、`set-research`（下一个科技）、`set-policy`（下一个政策）、`set-persona`（外交人设）、`keep-status-quo`。单位移动、战斗 targeting、城市生产队列全留给原版算法 AI（VPAI）。
- **写的本质**：LLM 决策落地为算法 AI 的权重参数（flavor 数字），不是逐条操作指令。如选「WinningWars」→ 战术算法更倾向进攻。被 LLM 接管的战略模块会禁用原版对应模块。
- **读的表示**：每回合编码成结构化 Markdown，六节：胜利进度、战略选项与现选、玩家摘要、城市摘要、军事摘要、上轮以来事件。比啰嗦编码省约三分之二 token。
- **时机**：玩家回合结束后触发 LLM；LLM 思考时其他玩家回合照常进行，延迟被吸收（实测平均每回合约 15 秒，在文明5最快回合计时之内）。
- **结果**：GPT-OSS-120B 与 GLM-4.6 各跑数百局，胜率、存活率与算法 AI 统计打平；两个模型表现出彼此不同且不同于算法 AI 的玩法风格（胜利路线偏好、政策轨迹、外交人设）。
- **踩到的坑**：输入 token 随游戏进程线性增长（后期单回合可达 10 万 token，压迫上下文窗口）；LLM 有「战略固执」和一厢情愿（打输时反而切主战策略）；纯文本坐标下 LLM 地缘判断差（对遥远敌人打「假战争」浪费国力）；更大模型并不自动更强。

### 3.3 CK3：Voices of the Court（Jomini 引擎上的文件通道）

[Demeter29/Voices_of_the_Court](https://github.com/Demeter29/Voices_of_the_Court)（原版）与 [Voices-of-the-Court/VOTC](https://github.com/Voices-of-the-Court/VOTC)（社区重实现），CK3 上用户量最大的 LLM 集成（Steam 创意工坊 2.0 版持续更新）。两部分：CK3 脚本 mod ＋ 外部 Electron 应用（TypeScript，调 OpenAI/OpenRouter/Ollama 等）。

- **读**：mod 收集角色/特质/关系/事件数据写日志文件（CK3 用户目录 `logs/` 下），外部应用解析（仓库 `src/main/gameData/`，社区另有 ck3_log_parser 工具）。
- **写**：预定义 Action 白名单——LLM 只能触发 mod 里定义好的动作，不能发明新的。外部应用把 LLM 选中的 action 转成 CK3 effect 脚本（`ActionRegistry` / `ActionEffectWriter.ts`），经 `%appdata%\Voices of the Court\votc_data\scripts\` 目录交给游戏侧执行；动作脚本由用户以动作包形式安装到该目录。执行机制的具体轮询细节在源码里，本轮未逐行核。
- **教训**（官方文档原话概括）：动作必须白名单；LLM 输出要做修复（仓库里有 `responseHealing.ts`）。

### 3.4 星际争霸2：官方 API 路线及其教训

- 基座是暴雪官方 [pysc2](https://github.com/google-deepmind/pysc2)（SC2 客户端自带 API：结构化观察＋动作调用，AlphaStar 同款接口）。
- LLM 侧包装是 [LLM-PySC2](https://github.com/NKAI-Decision-Team/LLM-PySC2)（NKAI/国防科大团队，[论文](https://arxiv.org/html/2411.05348v2)）：把 pysc2 观察转成文本/多模态给 LLM，LLM 文本输出转回完整动作空间；另附游戏 wiki 知识。
- **教训**：LLM 能提出像样的高层战略，但微操差——幻觉动作、无效指令、单位指错目标；实时操作延迟撑不住。RTS 类必须把微操留给执行层。

### 3.5 Freeciv（开源文明克隆）：协议直连

开源游戏本身就是服务器，无需 mod：[taso-labs/freeciv-llm](https://github.com/taso-labs/freeciv-llm) 做 WebSocket API（agent 连接认证、取结构化状态、交动作）；[bigai-ai/civrealm](https://github.com/bigai-ai/civrealm)（清华系）提供 Gymnasium 张量接口与 LLM 文本接口双轨，含小游戏基准与整局模式。CivRealm 论文的结论：纯 LLM 与纯 RL 都活不完一整局（RL 短视刷分，LLM 守不住经济与国防），明确建议混合架构——Vox Deorum 即照此实现。

### 3.6 宝可梦：截图+按键，外加内存辅助

- Peter Whidden 的 GPT-4 通关宝可梦（2023）：JS 模拟器，观察 = 模拟器状态＋截图，动作 = 模拟器按键 API，LLM 逐步选按钮。
- Claude Plays Pokémon（2025-02 起 Twitch 直播）、Gemini Plays Pokémon 同路线。一个被后续论文点破的细节：Gemini 的 harness 还从模拟器内存读格子可走性（tile navigability）喂给模型——纯看截图并不够。

### 3.7 GTA V：没有 LLM 玩家先例

GTA V 在 AI 圈的定位是自动驾驶/CV 训练环境（多家媒体报道）：用 mod 从游戏内存导出深度图/语义标注数据。控制层标准底座是 [ScriptHookV](https://www.dev-c.com/gtav/nativetrainer)（调用游戏 native 函数的 .asi 插件框架，仅单机）。「LLM 玩 GTA」没有代表性公开项目。Google 的 SIMA 2 走截图＋虚拟输入玩 3D 游戏的通用路线，属研究阶段。

### 3.8 PDX 系读侧先例：Stellaris Companion

[gitmaan/stellaris-companion](https://github.com/gitmaan/stellaris-companion)：解析群星存档 → AI 战略顾问＋帝国编年史，文档提到支持本地 MCP 连接。纯读侧，与本项目的读侧闭环同款思路。

## 4. 排查过但查无实据的事

怀疑过 Jomini 引擎（CK3/Vic3 同引擎）存在隐藏的「远程控制台」TCP 端口可供外部注入命令（类似 Civ6 FireTuner）。搜官方 wiki（vic3/ck3.paradoxwikis.com 的 Modding、Console commands 页）与 Paradox 论坛，**没有任何文档或讨论**。PDX 官方口径只有 `-debug_mode` 启动后的游戏内控制台，无对外通道。此路不指望。

## 5. 对本项目的映射

本项目「agent 定方向、操作留给游戏原生 AI」的现状即 Vox Deorum 的 LLM+X 架构（X＝vic3 原生 AI），路线已验证。写侧触发通道（harness 发请求→游戏执行）有两种成熟做法：

1. **命令文件轮询（VotC 式）**——现有路线的自然延伸。mod 里挂定期 on_action（每日/每周），轮询读约定路径的命令文件，解析后用 effect 执行，执行完写回执。GreatBritainStartPlay 按钮已证明 mod 能执行发起博弈的脚本，剩下的只是把「人点按钮」换成「mod 读文件」。VotC 以此撑起万人用的 mod，机制成熟。
2. **参数覆盖（Vox Deorum 式）**——agent 不逐条下命令，而是改一组战略参数（对应 vic3 可以是国家 AI 策略倾向，或 mod 自定义的「国策方向」枚举），原生 AI 照参数执行。粒度粗但稳，且与「agent 是玩家」的设定不冲突——玩家也是定方向不点每一下鼠标的。

可直接抄的经验：

- 读侧用结构化分节文本（Vox Deorum 六节式，省 2/3 token），并预算管理状态膨胀（他们后期单回合 10 万 token）。
- 写侧工具一律白名单＋输出修复（VotC 的 ActionRegistry＋responseHealing）。
- 回合复盘用前后快照差分（civ6-mcp 的 end_turn 模式）。

## 参考来源

- [lmwilki/civ6-mcp](https://github.com/lmwilki/civ6-mcp)——README 全文，架构自述（一等，2026-11-24 读）
- [Vox Deorum 论文](https://arxiv.org/abs/2512.18564)（arXiv 2512.18564，FDG 2026）——全文细读，架构/实验数据（一等）
- [CIVITAS-John/vox-deorum](https://github.com/CIVITAS-John/vox-deorum)＋[CivFanatics 发布帖](https://forums.civfanatics.com/threads/beta-vox-deorum-0-14-0-play-civilization-with-llms-vp-5-2-7-compatible.701133)（一等/二等）
- [Demeter29/Voices_of_the_Court](https://github.com/Demeter29/Voices_of_the_Court)、[Voices-of-the-Court/VOTC](https://github.com/Voices-of-the-Court/VOTC)——README＋目录结构（`gameData/`、`actions/ActionEffectWriter.ts`、`responseHealing.ts`）（一等）；[官方文档](https://docs.voicesofthecourt.app)（一等）；[MrAndroPC/votc-actions-repo](https://github.com/MrAndroPC/votc-actions-repo)——scripts 目录与日志路径佐证（一等）；游戏侧轮询执行细节未逐行核码，待需要时查
- [NKAI-Decision-Team/LLM-PySC2](https://github.com/NKAI-Decision-Team/LLM-PySC2)＋[论文](https://arxiv.org/html/2411.05348v2)（一等）
- [google-deepmind/pysc2](https://github.com/google-deepmind/pysc2)（一等）
- [taso-labs/freeciv-llm](https://github.com/taso-labs/freeciv-llm)、[bigai-ai/civrealm](https://github.com/bigai-ai/civrealm)——README（一等）；CivRealm 结论转引自 Vox Deorum 论文 related work（二等）
- 宝可梦：Gemini harness 内存读 tile 的细节转引自论文《A Testbed for Self-Improvement in Embodied Video Games》对该直播的描述（二等）；[jcz.dev 博客](https://blog.jcz.dev/gemini-3-pro-vs-25-pro-in-pokemon-crystal)（二等）
- GTA：[ScriptHookV 官方站](https://www.dev-c.com/gtav/nativetrainer)（一等）；自动驾驶训练用途为多家媒体综合（二等）
- [gitmaan/stellaris-companion](https://github.com/gitmaan/stellaris-companion)＋[文档站](https://galacticfilingcabinet.com/docs)（二等，未逐页核）
- 「Jomini 无远程控制台」：vic3/ck3.paradoxwikis.com 官方 wiki＋Paradox 论坛检索无果（一等——否定性结论，检索于 2026-11-24）
