# 游戏接入-mod侧

一局单机维多利亚3，真人玩家玩其他国家，大不列颠由 agent 扮演：第一版只做读——agent 观察局势，大不列颠的操作全部留给游戏原生 AI；接管操作与禁用原生 AI 的写侧（操作宏库、AI 禁用）第一版不实现。游戏接入拆成两侧：mod 侧（本文件）与 mcp 侧（[游戏接入-mcp侧](游戏接入-mcp侧.md)）。vic3-GreatBritain 整体还有 harness、agent 本体两块，另有说明文件。

## 职责与边界

mod 在 vic3-GreatBritain/mod/，是游戏内的唯一改动面，别的组件不直接碰游戏文件。mod 侧的边界：从游戏进程到 debug.log 为止——把游戏内状态变成 debug.log 里的机器友好记录。日志的解析与对外暴露归 mcp 侧；两侧以 debug.log 的记录格式为交接面，格式与内容由本文件定义。

## 声明：做什么

当前只有一个功能：状态导出。每年（游戏内年度）把世界格局写成 debug.log 里的年度快照，内容是封闭清单，清单外不导出：

- 8 个列强＋8 个次强（rank 1–16），每国两项：GDP、常备军数量
- 大不列颠的财政状态

## 实现：怎么做

### 状态导出

按数据流分四步：挂年度钩子 → 在钩子里判强国 → 取国别四项 → 写日志；大不列颠的财政在同一钩子里特判追加。

- 挂年度钩子：在 mod 的 common/on_actions 文件里给基础 on_action `on_yearly_pulse_country` 附加（wiki On action 文档已证：country 作用域，每国每年触发一次；on_actions 的游戏目录是 common/on_actions；给基础 on_action 只能追加 on_actions/events 块，加别的块会报错，官方模板即"基础 on_action 触发时调用 mod 自建的 on_action"，effect 写在自建 on_action 里）

- 判强国：钩子第一层用 `global_country_ranking <= 16` 做门槛（比较国家世界名次的 trigger，wiki Trigger 文档已证，同族示例 `global_country_ranking > 42`）。各国触发顺序不保证按名次，且实测各国在各自周年日触发、同一年的快照散布全年，所以每行记录自带 rank 值，mcp 侧按行内年份分组聚合、排序

- 取国别两项（作用域都是 country，均 wiki Trigger 文档已证）：
  - GDP：`gdp`（"yearly predicted GDP"）
  - 常备军：`army_size`（营队数）

- 大不列颠财政：同一钩子里特判 tag GBR，追加财政行——`gold_reserves`（金库）、`principal`（债务本金）、`net_total_income`（每周净收支，收抵支后的余量）。均 wiki Trigger 文档已证，原版脚本有用例：`principal` 直接当值取（script_values 里 `add = principal`），`net_total_income` 用在条件判断（`net_total_income > 0`）。

- 写日志：一行一国，`debug_log` 的消息支持本地化字符串内插（ROOT/SCOPE/PREV 可用，wiki Effect 文档已证），数值经内插写进字符串。实现形式是 data function 内插：`[THIS.GetCountry.XXX]` 前缀为原版 debug_log 用例写法，各数值函数（GetGDP、GetRankNumber 等）出自 wiki GUI 脚本函数表，年份取 `[TimeKeeper.GetCurrentDate.GetString]`（原版用例）；tag 不走内插取名，GBR 特判用 scope 比较 `c:GBR = ROOT`（原版 journal 用例写法）。行格式（`<>` 为占位）：

  - 国家行（rank 1–16 每国一行）：`vic3-GreatBritain state tag=<tag> year=<年> rank=<名次> gdp=<GDP> army=<营队数>`
    - 示例：`vic3-GreatBritain state tag=FRA year=1836 rank=3 gdp=12345.6 army=20`
  - 财政行（仅 GBR，每年追加一行）：`vic3-GreatBritain fin tag=<tag> year=<年> gold=<金库> debt=<债务本金> week_net=<每周净收支>`
    - 示例：`vic3-GreatBritain fin tag=GBR year=1836 gold=54321.0 debt=0.0 week_net=12.3`

首次实测（2026-11-20，俄罗斯开局跑过 1836 年度钩子，-debug_mode）已收敛：

- 脚本 debug_log 输出成立，进 `Documents\Paradox Interactive\Victoria 3\logs\debug.log`；行头 `[墙钟时间][jomini_effect_impl.cpp:459]: common/scripted_effects/gb_agent_effects.txt:<行号>: `，mcp 侧按行内 `vic3-GreatBritain ` 前缀过滤即可；-debug_mode 下成立，不加是否也出不再验（前提已定要开）
- 数值 data function 内插成立：原始小数、无千分位无缩写、负数带负号（CFixedPoint 与 int32 均如此）
- GetTagName 输出三字码；国家行恰好 16 行；GBR 财政行每年恰好一行
- week_net 用 GetWeeklyBalance 输出带符号原始小数，开局量级合理（GBR 周净 -10.8 万），与 trigger `net_total_income` 严格同值无从交叉验证，按界面语义采信
- year 输出完整本地化日期（如"6月 13, 1836"，含空格逗号）：定案 year 由 mcp 侧从值尾抽 4 位年份数字，mcp 解析按字段名取值、不按空格切分
- 年度触发机制：on_yearly_pulse_country 不是统一 1月1日，每国在各自周年日触发（实测从 6月13日 BRZ 到 12月31日 GBR 不等），同一年的快照散布全年，mcp 侧按行内年份分组聚合

待二次实测（rank 换写法后跑一年核对）：

- GetRankNumber 首次实测输出 5/6/7，是国家分级（country tier）不是世界名次；已换 GetCountryScorePosition（int32，对应 `global_country_ranking` 的 Power Ranking position），与门槛同值性待核对——16 行的 rank 值恰为 1–16 且互不重复即成立
- GetNumBattalions 开局值合理（GBR 135、RUS 200、CHI 578）；是否排除征召兵和平期验不出，遇到战争年顺带观察即可，不单独立项验证
- 全量值表的来源修正：不是游戏安装目录的文件（实测无 documentation/ 文件夹），是游戏内 `script_docs` 控制台命令导出的；wiki 的 Trigger/Effect 表即由它生成，需要全量表时游戏内导一次

## 前提

- 游戏须以 -debug_mode 启动；是否为 debug.log 输出所必需，与落点一起实测确认
