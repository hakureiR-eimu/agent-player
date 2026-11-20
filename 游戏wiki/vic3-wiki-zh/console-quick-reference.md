---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Console 命令速查表（自动提取）
source: https://vic3.paradoxwikis.com/Console_commands
extracted_from: Console commands.md
fetched: 2026-10-27
---
共 156 条命令，自动提取自 [控制台命令](Console%20commands.md)；完整说明（含 debug mode 开启方法、按键、注意事项）见原页。

| 命令 | 说明 |
|---|---|
| `add_journal_entry [journal entry type]` | 为玩家国家添加指定的日志条目 |
| `add_mandates [amount]` | 为当前强权集团增加托管权 |
| `add_supply_ships [amount]` | 立即增加指定数量的补给船。 |
| `ai_evaluate_autonomous_construction [<building key> <state region key>]` | 打印所选州与建筑类型的 AI 调试数据。 |
| `ai_evaluate_company [<company type key>]` | 打印所选公司的 AI 调试数据。 |
| `ai_evaluate_government_construction [<building key> <state region key>]` | 打印所选州与建筑类型的 AI 调试数据。 |
| `ai_evaluate_interest [<strategic region key>]` | 打印所选战略区域宣告利益的 AI 调试数据。 |
| `ai_evaluate_mobilization` | 打印动员的 AI 调试数据。 |
| `ai_evaluate_privatization [<building key> <state region key>]` | 打印所选州与建筑类型的 AI 调试数据。 |
| `ai_evaluate_production_method [<building key> <pm key> <state region key>]` | 打印所选州内该建筑类型指定生产方式的 AI 调试数据。 |
| `ai_evaluate_state [<state region key> <country tag>]` | 打印所选州的 AI 战略价值。 |
| `ai_evaluate_subject [<country tag>]` | 打印所选附属国的 AI 调试数据。 |
| `ai_evaluate_trade_route [<goods key> <country tag>]` | 打印所选商品与贸易伙伴国家的 AI 调试数据。 |
| `ai_evaluate_treaty_port [<state region key> <country tag>]` | 打印 AI 的条约港评分。 |
| `ai_evaluate_wargoal [<wargoal type> <country tag> <state region key>]` | 打印战争目标的 AI 调试数据。 |
| `annex [<country tag/id>]` | 吞并一个国家 |
| `annex_all` | 吞并所有其他国家 |
| `callstack` | 打印调用栈 |
| `change_law` | 将一项法律改为指定的键值（如 "law_monarchy" 等） |
| `check_pollution_level [state region tag]` | 打印指定州区域的污染数据 |
| `check_save` | 检查保存与加载是否一致 |
| `clearlines` | 清除线条 |
| `clearspawnedentities` | 清除由 spawnentity 命令生成的实体 |
| `coa_preview_window` | 打开纹章预览窗口 |
| `compound_nodeeditor` | 复合节点编辑器 |
| `conquerall [country tag]` | 将所有敌方省份置于我方控制之下。 |
| `crash` | 使应用程序崩溃 |
| `create_ai [self/all/tag]` | 为一个或多个国家创建 AI |
| `create_building_history` | 创建一个符合游戏历史格式的 .txt 文件，包含世界上所有建筑（或指定州 ID）及其生产方式/补贴配置。 |
| `create_political_movement [<movement type key>]` | 创建一个政治运动 |
| `create_pop_history` | 在 debug.log 中导出完整的人口历史记录 |
| `create_state_region_data` | 创建一个符合游戏数据库格式的 .txt 文件，包含世界上所有州区域及其省份/资源 |
| `cthulhu` | ? |
| `data_types_explorer` | 打开数据类型浏览器（可停靠窗口） |
| `data_wrappers_stats [Filter]` | 打印有关数据包装器的统计信息 |
| `date [date in format yyyy.mm.dd.hh]` | 更改当前日期 |
| `debug [arguments]` | 各种调试操作。参见 [console command 参数](Console commands.md)。 |
| `debug_lens_option` | 切换作弊模式 debug_lens_option |
| `debug_mode` | 切换 debug mode |
| `debugcharacters` | 创建一个以分号分隔的日志文件，包含所有人物的调试信息。 |
| `debugcountrybudgets` | 创建一个以分号分隔的日志文件，包含所有国家及其预算的调试信息。 |
| `debugemployment` | 创建并追加一个以逗号分隔的日志文件，包含指定州 ID 就业情况的调试信息。 |
| `debugmarkets` | 创建一个以分号分隔的日志文件，包含所有商品与市场的调试信息。 |
| `debugpopconsumption` | 创建一个以分号分隔的日志文件，包含所有人口消费情况的调试信息 |
| `debugpopwealth` | 创建一个以分号分隔的日志文件，记录所有人口当前的财富状况。 |
| `debugstates` | 写入一个以分号分隔的日志文件，包含所有州的调试信息。 |
| `debugterrainweights` | 打印……的数量 |
| `debugtheaters` | 写入一个以分号分隔的日志文件，包含所有战区的调试信息。 |
| `deiron` | 禁用铁人模式 |
| `disable_ai [all/tag]` | 禁用 AI |
| `disable_pop_growth` | 切换作弊模式 disable_pop_growth |
| `disable_retooling` | 切换作弊模式 disable_retooling |
| `drawcmdsviewer` | 绘制命令查看器 |
| `dump_data_types` | 导出已注册的数据类型 |
| `enable_ai [all/tag]` | 启用 AI |
| `entity_editor` | 实体编辑器（可停靠窗口） |
| `escalate [<amount>]` | 为玩家的外交博弈升级程度加值。 |
| `explorer` | 显示对象浏览器窗口 |
| `exportbuildings` | 写入一个以分号分隔的日志文件，包含所有建筑类型信息 |
| `fastbattle` | 切换作弊模式 fastbattle（战斗在一个刻度内结束）**（影响 AI）** |
| `fastbuild` | 切换作弊模式 fastbuild（使所有建造立即完成）**（影响 AI）** |
| `fastbuildships` | 立即生产船只。 |
| `fastcivilwars` | 切换作弊模式 fastcivilwars |
| `fastcolonize` | 切换作弊模式 fastcolonize **（影响 AI）** |
| `fastenact` | 切换作弊模式 fastenact（政策的制定即刻完成） |
| `fasthire` | 切换作弊模式 fasthire |
| `fastincorporate` | 切换作弊模式 fastincorporate（使州的合并仅需 1 天） |
| `fastinstitutions` | 切换作弊模式 fastinstitutions |
| `fastinterests` | 切换作弊模式 fastinterests |
| `fastlobbies` | 切换作弊模式 fastlobbies |
| `fastmobilize` | 切换作弊模式 fastmobilize |
| `fastmovements` | 切换作弊模式 fastmovements |
| `fastresearch` | 切换作弊模式 fastresearch |
| `fastrevolution` | 切换作弊模式 fastrevolution |
| `fastsecession` | 切换作弊模式 fastsecession |
| `fastsecretgoals` | 切换作弊模式 fastsecretgoals |
| `fasttravels` | 切换作弊模式 fasttravels |
| `find_unemployed` | 查找并报告所有失业人口，可指定可选的截止值 |
| `fix_state_regions` | 修复州区域。 |
| `force_oos` | 使本客户端在多人游戏中失去同步 |
| `generate_province_center_objects` | 在每个省份中心生成一个带网格的文件 |
| `gui_animation_editor` | GUI 动画时间轴（可停靠窗口） |
| `gui_editor` | 启动 GUI 编辑器（1.9 版本已移除） |
| `help [command name]` | 打印所有 console command 或某个具体命令的说明。 |
| `hq_show_id` | 切换作弊模式 hq_show_id |
| `ig_devout` | 虔信派 |
| `ig_industrialists` | 实业家 |
| `ig_intelligentsia` | 知识分子 |
| `ig_landowners` | 地主 |
| `ig_petty_bourgeoisie` | 小市民 |
| `ig_rural_folk` | 乡民 |
| `ig_trade_unions` | 工会 |
| `ignore_government_support` | 切换作弊模式 ignore_government_support |
| `ignore_power_bloc_requirements` | 切换作弊模式 ignore_power_bloc_requirements（退出和加入时忽略影响力要求） |
| `invalidate_character [character id]` | 使指定 ID 人物身上的 modifier 失效 |
| `invalidate_country [country id]` | 使指定 ID 国家身上的 modifier 失效 |
| `invalidate_ig [interest group id]` | 使指定 ID 利益集团身上的 modifier 失效 |
| `invalidate_state [state id]` | 使指定 ID 州身上的 modifier 失效 |
| `io_stats` | 切换 IO 统计 |
| `kill_character [character name]` | 杀死指定姓名的人物 |
| `log_status` | 日志状态（可停靠窗口） |
| `log_ticktask_performance` | 开始向 profiling.log 输出刻度任务性能数据 |
| `log_viewer` | 日志查看器（可停靠窗口） |
| `map_editor` | 切换地图编辑器 |
| `mapmode [mapmode]` | 切换到指定的地图模式 |
| `measure_frame_time ["start" or "stop" measuring]` | 测量平均/最小/最大帧时间，停止后将结果打印到 debug.log |
| `memory_stats` | 切换内存统计 |
| `minidump [file path]` | 创建一个小型转储文件 |
| `money [amount]` | 增加指定数额的金钱 |
| `net_debuginfo` | 打印网络层的调试信息 |
| `net_stats` | 切换网络统计 |
| `norevolution` | 切换作弊模式 norevolution |
| `nosecession` | 切换作弊模式 nosecession |
| `noshortages` | 防止建筑因补给短缺而受罚 |
| `nosupportloss` | 防止国家损失战争支持度 |
| `observe` | 开始观察游戏 |
| `particleeditor` | 粒子节点编辑器 |
| `permitmarginalizedingovernment` | 切换作弊模式 permitmarginalizedingovernment |
| `pops_account_disconnect_steam` | 将 Paradox 账号与 Steam 解绑 |
| `pops_account_logout` | 退出登录 POPS 账号 |
| `pops_account_status` | 显示当前是否已登录 POPS。 |
| `popstat` | 打印活跃人口的数量。 |
| `portrait_editor` | 打开肖像编辑器 |
| `print_gamestate_modifiers` | 打印游戏状态 modifier |
| `province_borders [true/false]` | 切换省份边界的显示 |
| `recalc_cached_data` | 重新计算缓存的游戏状态数据。 |
| `release_mode` | 切换发行模式 |
| `reload [file name]` | 重新加载资源 |
| `rendertype` | 报告当前使用的渲染后端 |
| `research` | 获得技术 |
| `save_game_analyzer` | 打开存档分析器 |
| `screenshot` | 截图 |
| `script_docs` | 打印脚本文档 |
| `settings` | 启动设置 GUI，可用可选参数指定初始选中的类别 |
| `shader_editor` | 着色器编辑器（可停靠窗口） |
| `show_goals` | 显示 AI 目标。 |
| `skip_migration` | 切换作弊模式 skip_migration |
| `sleep` | 休眠指定的毫秒数 |
| `social_debuginfo` | 打印社交层的调试信息 |
| `switchlanguage [language name]` | 重新加载本地化文件并切换语言 |
| `tag [country_tag]` | 将控制权切换到另一个国家 |
| `testaipacts` | 测试 AI 是否会解散当前条约 |
| `testobjective [<subgoal key (optional)>]` | 测试目标的触发式 effect |
| `texturelist` | 纹理列表 |
| `textureviewer` | 纹理查看器 |
| `time` | 现在几点了？ |
| `treatyport [<state region tag>]` | 在指定州区域夺取条约港 |
| `tweak` | 启动一个调整器 GUI |
| `update_distribution` | 更新指定州 ID 总部中卫戍单位的分配 |
| `update_employment` | 在指定州 ID 的建筑之间调动雇员。 |
| `validate_employment` | 打印各州的失业情况。 |
| `validate_income` | 打印存在收入赤字的国家。 |
| `validate_pops` | 确保所有人口参数有效，否则将其打印到错误日志中。 |
| `version` | 显示当前版本信息，第二个参数填 1 可显示完整版本 |
| `vsync` | 切换主交换链的垂直同步 |
| `yesmen` | AI 将同意玩家的所有外交提议与拉拢出价 |