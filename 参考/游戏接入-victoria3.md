# 游戏接入：Victoria 3 技术路径调研

> 调研日期：2026-10-12；**本地静态验证：2026-10-12 完成**（游戏目录 `D:\SteamLibrary\steamapps\common\Victoria 3`，版本 1.9.6）。

## 核心结论

1. **V3 没有官方运行时外部 API**。Modding 以静态脚本为主（游戏启动时加载），社区工具几乎全部面向离线编辑/校验/发布。**"游戏状态接口化"的桥接层自建**（设计见 `docs/游戏桥接设计.md`）。
2. **存档是二进制 token 格式**（静态验证修正：头部 `SAV0103` + hash + 二进制 token 流，非 zip 文本——forum 信息有误/过时）。两个出路：a) **`-debug` 模式下存档大概率保存为明文**（Paradox 惯例，待启动验证——主路径本就要求 -debug）；b) 二进制档可走社区解析器（pdx_unlimiter 支持 V3 含铁人档）。
3. Paradox 脚本（Clausewitz/Jomini）**不是图灵完备语言，没有运行时文件 IO**——mod 无法运行中读取外部指令文件。这是桥接设计的最大硬约束。

## 静态验证发现（2026-10-12，均已在游戏文件中确认）

| 发现 | 位置 | 对桥接的意义 |
|------|------|-------------|
| **控制台命令宏系统（原生）** | `game/common/console_command_macros/00_macros.txt` | 带参数（`$1`）、可嵌套、mod 可自定义。**写入通道的白名单动作可封装成游戏内宏**，外部只需注入 `宏名 参数`——极短、极稳、天然白名单 |
| **on_actions 官方文档** | `game/common/on_actions/_on_actions.md` | 周期钩子：`on_monthly_pulse_country`（root=country，月级）为最细原生粒度；**mod 追加机制**：vanilla on_action 转调 modded on_action，无文件冲突 |
| **日级输出循环可自建** | 同上文档 `trigger_event` 条目 | `trigger_event = { on_action = X days = 1 }` 支持按天延迟——事件自循环即可实现**日级状态输出**，绕过月级限制 |
| **`debug_log` effect/trigger 存在** | `common/scripted_effects/00_victoria_scripted_effects.txt`（用例 `debug_log_scopes`）、`common/trigger_localization/` | 日志输出原语确认存在；具体签名（能否变量插值）待启动后从生成的 script_docs 确认 |
| **外交动作官方文档** | `game/common/diplomatic_actions/diplomatic_action.md` | 动作结构 = `effect + pact + ai` 块；**acceptance/accept_score 机制**（"讨价还价"的游戏内接口）；全套动作定义文件在 `diplomatic_actions/` |
| **列强枚举原语** | `common/on_actions/00_code_on_actions.txt` | 游戏原生用 `country_rank >= rank_value:great_power` + `add_to_global_variable_list` 维护列强清单——状态导出直接复用同一口径，天然支持动态列强 |
| **日志目录齐全** | `Documents/Paradox Interactive/Victoria 3/logs/` | `game.log` / `error.log` / `debug.log` / `message.log` 均在；带滚动归档（`.1.log`…） |
| **script_docs 不预置** | — | 启动游戏后从控制台生成（`script_docs` 命令，导出到用户目录），是 effects/triggers 的权威清单 |
| **开局外交定义** | `game/common/history/diplomacy/` | relations / favors / rivalries / truces 开局脚本 |

## 可借用的外部基础设施

| 工具 | 用途 | 链接 |
|------|------|------|
| Pdx-Unlimiter | 存档管理/解包（二进制档解析参考），支持 V3 含铁人档 | [github.com/crschnick/pdx_unlimiter](https://github.com/crschnick/pdx_unlimiter) |
| CWTools | Paradox 脚本解析/校验 | [Victoria 3 Wiki – Modding](https://vic3.paradoxwikis.com/Modding) |
| Paradox Modding Toolkit | VS Code 扩展：脚本编辑、Workshop 发布 | VS Code Marketplace |

## 运行时桥接方案

见 `docs/游戏桥接设计.md`（消息队列架构，主路径：日志桥读 + 控制台宏注入写）。

## 剩余待启动验证清单（需 `-debug` 启动游戏）

- [ ] **S1 控制台能力**：确认控制台打开键与命令列表（重点：`effect` 命令、`script_docs` 生成、annex/tag 等）；顺手记录 1836 列强名单
- [ ] **S2 命令注入**：手动执行一条外交 effect 成功 → PowerShell SendInput 自动化成功（窗口激活 + 英文输入法）
- [ ] **S3 日志签名**：`debug_log` 能否输出带变量插值的自定义文本（决定日志桥输出格式设计）
- [ ] **S5 文件监听**：游戏运行中 Node tail `game.log` 可行性（文件占用行为）
- [ ] **S6 存档验证**：`-debug` 下存档是否明文；明文改外交字段 → 重载 → 生效
- [ ] **S7 日级循环实测**：自建每日 on_action 自循环的日志量与性能
- [ ] **S8 行为一致性**：effect 宏创建/加入的外交博弈与玩家 UI 操作行为一致（通知/可见性、AI 照常评估站边、合法性前置）

## 来源

- 本地游戏文件（见上表）
- [Victoria 3 Wiki – Modding](https://vic3.paradoxwikis.com/Modding)（wiki 有反爬，以本地文件为准）
- [crschnick/pdx_unlimiter](https://github.com/crschnick/pdx_unlimiter)
