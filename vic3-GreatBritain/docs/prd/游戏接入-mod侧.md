# 游戏接入-mod侧

一局单机维多利亚3，真人玩家玩其他国家，大不列颠由 agent 扮演：第一版只做读——agent 观察局势，大不列颠的操作全部留给游戏原生 AI；接管操作与禁用原生 AI 的写侧（操作宏库、AI 禁用）第一版不实现。游戏接入拆成两侧：mod 侧（本文件）与 mcp 侧（[游戏接入-mcp侧](游戏接入-mcp侧.md)）。vic3-GreatBritain 整体还有 harness、agent 本体两块，另有说明文件。

## 职责与边界

mod 在 vic3-GreatBritain/mod/，是游戏内的唯一改动面，别的组件不直接碰游戏文件。mod 侧的边界：从游戏进程到 error.log 为止——把游戏内状态变成 error.log 里的机器友好记录。日志的解析与对外暴露归 mcp 侧；两侧以 error.log 的记录格式为交接面，格式与内容由本文件定义。

## 声明：做什么

当前只有一个功能：状态导出。每年（游戏内年度）把世界格局写成 debug.log 里的年度快照，内容是封闭清单，清单外不导出：

- 8 个列强＋8 个次强（rank 1–16），每国两项：
  - GDP：年度预测 GDP（游戏对本国这一年 GDP 的预估值）
  - 常备军数量：营队数（battalion 数）
- 大不列颠的财政状态，三项：
  - 金库：国库现存的钱
  - 债务本金：欠债的本金总额（未偿部分，不含利息）
  - 每周净收支：一周内全部收入抵掉全部支出后的余量，负数即入不敷出

## 实现：怎么做

### 状态导出

按数据流分四步：挂年度钩子 → 在钩子里判强国 → 取国别四项 → 写日志；大不列颠的财政在同一钩子里特判追加。

- 挂年度钩子：在 mod 的 common/on_actions 文件里给基础 on_action `on_yearly_pulse_country` 附加（wiki On action 文档已证：country 作用域，每国每年触发一次；on_actions 的游戏目录是 common/on_actions；给基础 on_action 只能追加 on_actions/events 块，加别的块会报错，官方模板即"基础 on_action 触发时调用 mod 自建的 on_action"，effect 写在自建 on_action 里）

- 判强国：钩子第一层用 `global_country_ranking <= 16` 做门槛（比较国家世界名次的 trigger，wiki Trigger 文档已证，同族示例 `global_country_ranking > 42`）。各国触发顺序不保证按名次，且实测同一年的各行触发日期散布全年（各国不同日；每国是否每年固定同一天未验，见文末待实测清单），所以每行记录自带 rank 值，mcp 侧每国取最新一条、按行内 rank 排序

- 取国别两项（作用域都是 country，均 wiki Trigger 文档已证）：
  - GDP：`gdp`（"yearly predicted GDP"）
  - 常备军：`army_size`（营队数）

- 大不列颠财政：同一钩子里特判 tag GBR，追加财政行——`gold_reserves`（金库）、`principal`（债务本金）、`net_total_income`（每周净收支，收抵支后的余量）。均 wiki Trigger 文档已证，原版脚本有用例：`principal` 直接当值取（script_values 里 `add = principal`），`net_total_income` 用在条件判断（`net_total_income > 0`）。

- 写日志：一行一国，`error_log` 的消息支持本地化字符串内插（ROOT/SCOPE/PREV 可用，引擎内联文档已证），数值经内插写进字符串。实现形式是 data function 内插：`[THIS.GetCountry.XXX]` 前缀为原版脚本标准写法，各数值函数出自 wiki GUI 脚本函数表（GDP 用 GetGDP、名次用 GetCountryScorePosition、营队用 GetNumBattalions、财政用 GetGoldReserves/GetPrincipal/GetWeeklyBalance；该表由游戏内 `script_docs` 控制台命令导出生成，需要全量表时游戏内导一次）；GBR 特判用 scope 比较 `c:GBR = ROOT`（原版 journal 用例写法）。落点 `Documents\Paradox Interactive\Victoria 3\logs\error.log`，随游戏启动轮转（error.log → error.1.log，各保留 5 份），会话内不轮转。行格式（`<>` 为占位，`<>` 外是字面量）：

  - 国家行（rank 1–16 每国一行）：`vic3-GreatBritain state tag=<tag> year=<日期> rank=<名次> gdp=<GDP> army=<营队数>`
    - 示例行（消息体，值取自 2026-11-20 实测；行首另被游戏加头，见下"行的形态"）：`vic3-GreatBritain state tag=FRA year=12月 27, 1837 rank=3 gdp=24109387.47464 army=282`
  - 财政行（仅 GBR，每年追加一行）：`vic3-GreatBritain fin tag=<tag> year=<日期> gold=<金库> debt=<债务本金> week_net=<每周净收支>`
    - 示例行（消息体，值取自 2026-11-20 实测）：`vic3-GreatBritain fin tag=GBR year=12月 31, 1836 gold=0 debt=440232.39442 week_net=-108278.71675`

  行的形态（mcp 侧解析须知）：

  - 每行被游戏加头：`[墙钟时间][来源文件:行号]: `（error.log 实有格式）——墙钟时间不是游戏内时间；行尾 CRLF；与原版的错误输出混在同一文件，按行内 `vic3-GreatBritain ` 前缀过滤
  - year 值是完整本地化日期（`12月 27, 1837`，含空格逗号、随游戏语言走）：解析按字段名取值、不按空格切分，从值尾取 4 位数字为年份
  - rank 是触发当刻的世界名次：同一年的各行取的是各自触发时点的当刻值，可能出现并列（实测 1837 年 BRZ 与 BEL 均 rank=11，不同时点）；每年通常 16 行，席位年中变动时理论可 15–17 行，不硬性假设恰好 16
  - 数值为原始小数（无千分位无单位缩写），负数带负号
  - 游戏写日志不是逐行立刻写进文件，而是先攒在内存里攒一批才落盘：游戏跑着时去读，文件的最后一行可能只有前半截（实测遇到过财政行只落了开头一段）。mcp 侧解析时最后一行解析不出就跳过，下次读它就完整了

## 待实测清单（下次跑 mod 验证）

- 年度触发的日期机制：每国每年固定同一天，还是每年随机一天——判别法是对比同一 tag 连续两年的触发日期（行内 year 值），同月同日为固定、不同为随机；只影响快照时点的语义解读，不影响 mcp 侧按年分组
