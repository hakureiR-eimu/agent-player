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

- 判强国：钩子第一层用 `global_country_ranking <= 16` 做门槛（比较国家世界名次的 trigger，wiki Trigger 文档已证，同族示例 `global_country_ranking > 42`）。各国触发顺序不保证按名次，所以每行记录自带 rank 值，排序交给 mcp 侧

- 取国别两项（作用域都是 country，均 wiki Trigger 文档已证）：
  - GDP：`gdp`（"yearly predicted GDP"）
  - 常备军：`army_size`（营队数）

- 大不列颠财政：同一钩子里特判 tag GBR，追加财政行——`gold_reserves`（金库）、`principal`（债务本金）、`net_total_income`（每周净收支，收抵支后的余量）。均 wiki Trigger 文档已证，原版脚本有用例：`principal` 直接当值取（script_values 里 `add = principal`），`net_total_income` 用在条件判断（`net_total_income > 0`）。

- 写日志：一行一国，`debug_log` 的消息支持本地化字符串内插（ROOT/SCOPE/PREV 可用，wiki Effect 文档已证），数值经内插写进字符串。实现形式是 data function 内插：`[THIS.GetCountry.XXX]` 前缀为原版 debug_log 用例写法，各数值函数（GetGDP、GetRankNumber 等）出自 wiki GUI 脚本函数表，年份取 `[TimeKeeper.GetCurrentDate.GetString]`（原版用例）；tag 不走内插取名，GBR 特判用 scope 比较 `c:GBR = ROOT`（原版 journal 用例写法）。行格式（`<>` 为占位）：

  - 国家行（rank 1–16 每国一行）：`vic3-GreatBritain state tag=<tag> year=<年> rank=<名次> gdp=<GDP> army=<营队数>`
    - 示例：`vic3-GreatBritain state tag=FRA year=1836 rank=3 gdp=12345.6 army=20`
  - 财政行（仅 GBR，每年追加一行）：`vic3-GreatBritain fin tag=<tag> year=<年> gold=<金库> debt=<债务本金> week_net=<每周净收支>`
    - 示例：`vic3-GreatBritain fin tag=GBR year=1836 gold=54321.0 debt=0.0 week_net=12.3`

待实测清单（首次跑 mod 一起验证）：

- debug.log 落点与 -debug_mode 依赖（即前提节的待验项），含行是否带游戏加的时间戳/来源头（影响 mcp 侧的过滤与解析写法）
- 数值 data function 内插的输出格式：小数位、有无千分位/单位缩写（GetGDP 等是 CFixedPoint）；若内插不可行或格式不可控，回退：effect 里 set_variable 存数、内插取变量
- GetTagName 输出是否为三字码（如 GBR、FRA）
- GetRankNumber 是否即世界名次（与 trigger `global_country_ranking` 同值）
- GetNumBattalions 是否排除已征召兵（与 trigger `army_size` 同口径）；不符则换 GetBattalions
- year 字段现取 TimeKeeper.GetCurrentDate.GetString（完整日期字符串），实测输出是否纯年；若带月日，试 Date.Format 取纯年，或交 mcp 侧截取
- 周净收支取的 GetWeeklyBalance 与 trigger `net_total_income`（收抵支后的余量）是否同值；不符则回退记周收入（GetWeeklyIncome，对应 trigger `income`），行格式的 week_net 字段随回退改为 income
- 全量值表的来源修正：不是游戏安装目录的文件（实测无 documentation/ 文件夹），是游戏内 `script_docs` 控制台命令导出的；wiki 的 Trigger/Effect 表即由它生成，需要全量表时游戏内导一次

## 前提

- 游戏须以 -debug_mode 启动；是否为 debug.log 输出所必需，与落点一起实测确认
