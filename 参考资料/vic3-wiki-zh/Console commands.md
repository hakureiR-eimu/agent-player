---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Console commands
source: https://vic3.paradoxwikis.com/Console_commands
pageid: 3139
categories: [Potentially_outdated, Unknown_version, Expand, Modding, Guides]
fetched: 2026-10-27
---
请帮助核实或更新本文中较旧的章节。其中至少部分内容最后核实的[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)未知。

|  | 请通过[扩充](https://vic3.paradoxwikis.com/index.php?title=Console_commands&action=edit)以下内容来帮助改进本条目或章节：更新的控制台命令信息。 |
|---|---|

《维多利亚3》提供了一个调试模式（debug mode）**（默认关闭）**，允许输入控制台命令。本页面列出了可以输入到控制台窗口的各种代码。控制台窗口是一个特殊的调试窗口，在非铁人模式下且开启调试模式时可以访问。调试模式必须在启动游戏之前开启。之后可以按 Shift+2、ALT+2+1、Shift+3、§、~、^、°、² 或 `（具体按键因键盘布局而异）打开控制台命令窗口。对于 QWERTY 键盘，该按键是 `。如果上述组合键都无效，也可以尝试 Shift + Alt + C。按上、下方向键可浏览之前执行过的命令。输入命令的开头后按 ⇆Tab 可以自动补全，或显示包含所输入序列的所有命令。许多代码可以通过再次输入相同命令来关闭，但有时需要重新加载存档或退出游戏。

## 调试模式（Debug mode）

调试模式是一套游戏工具，允许通过正常途径之外的方式修改游戏行为。它包括：

- 控制台窗口（接受控制台命令）
- 调试菜单（包括 GUI 编辑器、脚本浏览器等）
- 调试信息
- 按 Ctrl 并点击地图上的国家即可接管该国
- 按 Ctrl + Alt 并点击地图上的州即可占领该州
- 文件监视器，可自动将已更改的文件（包括 mod）重新加载到内存中

### 开启调试模式

调试模式可以在启动游戏之前开启，也可以在游戏中使用 mod 切换。它可以在控制台中关闭，但一旦关闭就无法重新开启（除非使用 mod）。

开启方法：

#### Mod

有许多 mod，例如 [Free Console Access](https://steamcommunity.com/sharedfiles/filedetails/?id=2879839709)，可以在开启和关闭之间切换调试模式，便于一边使用控制台一边游玩，但这无法启用文件的即时重载。如果是为了做 mod，最好同时使用 mod 和启动选项。

#### 启动器

在游戏启动器中：

1. 切换到左侧的游戏设置
2. 向下滚动到“Open game in Debug Mode”（以调试模式启动游戏）部分，然后点击启动

#### Steam

在 Steam 上：

1. 右键点击游戏，打开属性
2. 在底部的启动选项中添加 `-debug_mode`
3. 启动游戏

#### Windows

不通过 Steam、直接在 Windows 上：

1. 进入你的《维多利亚3》目录下的 "binaries" 文件夹
2. 右键点击 victoria3.exe 并创建快捷方式
3. 右键点击该快捷方式，打开属性
4. 在“目标”字段末尾添加 `-debug_mode`（使其看起来像这样 `"...\victoria3.exe" -debug_mode`）
5. 使用该快捷方式启动游戏

### 关闭调试模式

要重新激活成就，需要禁用所有已启用的 mod，并从启动选项中移除 -debug_mode。启动游戏后，请确认[校验和正确](Patches.md)。校验和显示在主菜单的右下角。

### 调试信息

当调试模式激活时，部分提示信息（尤其是地图上的）会显示在正常游玩时通常隐藏的调试信息。

## 控制台命令列表

|  | 请通过[扩充](https://vic3.paradoxwikis.com/index.php?title=Console_commands&action=edit)以下内容来帮助改进本条目或章节。 |
|---|---|

| 命令 | 描述 |
|---|---|
| 3dstats | 切换 3D 统计的显示 |
| 3dstats.EnableGfxZoneStats | 切换 3D Gfx 区域统计的显示 |
| Adjacencies.Rebuild | 重建所有邻接关系 |
| Application.ChangeResolution | 通过控制台更改分辨率 |
| Browser.OpenURL [<url>] | 用提供的 URL 打开浏览器 |
| Camera.Debug | 打印摄像机调试信息 |
| Camera.Load | 加载摄像机位置 |
| Camera.Save | 保存摄像机位置 |
| Checksum.Log | 将游戏状态校验和记录到游戏日志 |
| CrashReporter.DeleteCrashData | 删除超过 X 天的本地崩溃转储 |
| CrashReporter.SimulateCrash | 模拟一次崩溃（导致游戏退出） |
| Complete_journal_entry [<journal entry type>] | 为玩家国家完成一个特定的日志条目 |
| Fail_journal_entry [<journal entry type>] | 使玩家国家的一个特定日志条目失败 |
| Debug.Achievements.Lock [<key>] | 重新锁定一项成就 |
| Debug.Achievements.ResetAll | 重新锁定所有成就 |
| Debug.Achievements.ToggleDebug [<value>] | 将成就系统置于调试模式 |
| Debug.Achievements.Unlock [<key>] | 根据键解锁一项成就 |
| Debug.TextureMode [Name of debug mode] | 启用用于调试的纹理模式 |
| Dockables.Create [Dockable name] | 创建 dockable |
| Dockables.CreateUserLayout [Dockable layout name] | 以新名称创建当前布局的用户布局副本 |
| Dockables.DeleteUserLayout [Dockable layout name] | 将布局删除为用户布局 |
| Dockables.HideLayout | 隐藏任何已显示的 dockable 布局 |
| Dockables.SaveUserLayout | 将当前布局作为用户布局保存到磁盘，可选用新名称 |
| Dockables.ShowLayout [Dockable layout name] | 显示一个现有的（用户）布局，隐藏当前布局 |
| Dockables.ShowManager | 显示 dockable 布局管理器 |
| GUI.AnimationTimeline.LogStats | 将 GUI 动画时间轴系统的统计信息转储到调试日志 |
| GUI.ClearWidgets | 清除虚拟控件 |
| GUI.CreateDockable [File name] [Widget name] [Dockable id. If doesn't exist, it will be registered] | 创建虚拟 dockable 控件。不带参数时，文件名将为 gui/test_gui.gui，控件名将为 test_window |
| GUI.CreateWidget | 创建虚拟控件。不带参数时，文件名将为 gui/test_gui.gui，控件名将为 test_window |
| GenerateCoastalRegionNavalExits |  |
| Graphics.CapFramerate |  |
| Graphics.DumpMemoryInformation |  |
| Localization.ToggleIncludeKeyInLocOutput | 在本地化输出中包含 loc 键 |
| Localization.ToggleOnlyKeyInLocOutput | 在本地化输出中仅显示 loc 键 |
| Localization.ToggleSkipDataSystemInLocOutput | 在 loc 中完全跳过数据系统 |
| Log.ClearAll | 清除所有日志 |
| Log.ClearErrorLog | 清除错误日志并重置错误计数 |
| Map.SavePNG [<map mode>] [<file name>] [<yes/no> Should render flat (optional)] | 将特定地图模式下地图保存为 PNG 截图。已知唯一可用的地图模式是 "countries" |
| MapObjects.Debug | 打印地图物体调试信息 |
| MapObjects.GenerateGameLocators [<type>] [<filename> (optional)] | 为游戏地图物体生成定位器 |
| MapObjects.Painter.AddPosition | 在光标下放置一个地图物体 |
| ModifierNode.Graph | 打开 tick 任务的图表视图 |
| ModifierNode.List | 打开 tick 任务的图表视图 |
| Music.PauseFactor | 显示或设置音乐系统的当前 pause_factor |
| Music.PlayTrack [<track name>] | 播放指定的曲目 |
| Music.Reset | 重置音乐系统 |
| Music.StopTrack | 停止当前播放的曲目 |
| PopsFileStorage.Sync | 同步 POP 文件存储 |
| Portrait.ClearCache | 清除肖像缓存。强制刷新所有肖像 |
| Print.EventDebug | 打印事件调试统计信息，需要先设置 Debug.Events 来收集统计信息 |
| RandomLog | 切换随机日志 |
| RandomLog.Dump [Frame count to dump, or * to dump all available frames (defaults to *)] [Target filename (defaults to random.log)] | 将随机日志数据转储到文件 |
| SDL.EventLogging |  |
| ScriptProfiling.Dump |  |
| SplineNetwork.AppendAssets |  |
| SplineNetwork.ClearAssets |  |
| SplineNetwork.Database.Reload |  |
| SplineNetwork.Graphics.AddAllSplines |  |
| SplineNetwork.Graphics.ClearAllSplines |  |
| SplineNetwork.SetAssetGenerationMode | 设置样条条带和锚点的生成模式 <naval/default> |
| SplineNetwork.ValidateSplines | 验证游戏内样条系统的完整性 |
| Terrain.Regenerate | 重新生成地形位图 |
| Terrain.Save |  |
| Threading.TaskThreadCount [The number of task threads] | 设置或获取任务线程数量 |
| TickTask.Graph | 打开 tick 任务的图表视图 |
| TickTask.List | 打开 tick 任务的图表视图 |
| add_approval [[interest group name](Console commands.md)] [amount] [time] | 为指定利益集团添加一个限时 modifier 来调整其认可度，[amount] 可选（默认=1），[time] 以月为单位且可选（默认=1），例如：add_approval ig_armed_forces 20(认可度) 20(月)，集团名称可在 game/common/interest_groups 中查找 |
| add_clout [[interest group name](Console commands.md)] [amount] [time] | 通过限时 modifier 改变利益集团的政治力量，从而增加或减少其政治力量，[amount] 可选（默认=1），[time] 以月为单位且可选（默认=1） |
| add_ideology [[interest group name](Console commands.md)] [Ideology to add.] | 为指定利益集团添加一种意识形态 |
| add_journal_entry [journal entry type] | 为玩家国家添加一个特定的日志条目 |
| add_loyalists [culture] [amount] | 按人口比例向文化添加忠诚派 |
| add_mandates [amount] | 为当前强权集团添加托管权 |
| add_radicals [culture] [amount] | 按人口比例向文化添加激进派 |
| add_relations [<country tag>] [amount] | 按给定数值改变与某国的关系 |
| add_supply_ships [amount] | 立即添加指定数量的补给船 |
| add_war_support [country_tag] [amount] | 按数值改变某国在其所有战争中的战争支持度 |
| add_liberty_desire [country_tag] [amount] | 按给定数值改变该国的独立倾向 |
| ai.debug [tag] | 转储该国的调试信息 |
| ai.goal [tag] [goal type] | 检查 AI 目标。这里的 ai goals 不是指 ai_strategies 中的秘密目标，而是通过 ai.debug 获取的 ai_goals |
| ai_evaluate_autonomous_construction [<building key> <state region key>] | 打印所选州和建筑类型的 AI 调试数据 |
| ai_evaluate_company [<company type key>] | 打印所选公司的 AI 调试数据 |
| ai_evaluate_government_construction [<building key> <state region key>] | 打印所选州和建筑类型的 AI 调试数据 |
| ai_evaluate_interest [<strategic region key>] | 打印所选战略区域宣示利益的 AI 调试数据 |
| ai_evaluate_mobilization | 打印动员的 AI 调试数据 |
| ai_evaluate_privatization [<building key> <state region key>] | 打印所选州和建筑类型的 AI 调试数据 |
| ai_evaluate_production_method [<building key> <pm key> <state region key>] | 打印所选州中某建筑类型特定生产方式的 AI 调试数据 |
| ai_evaluate_state [<state region key> <country tag>] | 打印所选州的 AI 战略价值 |
| ai_evaluate_subject [<country tag>] | 打印所选附属国的 AI 调试数据 |
| ai_evaluate_trade_route [<goods key> <country tag>] | 打印所选商品和贸易伙伴国的 AI 调试数据 |
| ai_evaluate_treaty_port [<state region key> <country tag>] | 打印 AI 的条约港评分 |
| ai_evaluate_wargoal [<wargoal type> <country tag> <state region key>] | 打印战争目标的 AI 调试数据 |
| annex [<country tag/id>] | 吞并一个国家 |
| annex_all | 吞并所有其他国家 |
| audio.cpu_info | 显示当前 CPU 占用 |
| audio.list_events | 列出音频事件 |
| audio.play_event [audio event] | 播放音频事件 |
| callstack | 打印调用堆栈 |
| change_law | 将法律更改为指定的键（如 "law_monarchy" 等） |
| changestatepop [state_id] [pop_type / all] [factor] | 按至多给定的系数改变给定人口类型（可以为 'all'）的人口规模。**将受每种人口最大就业人数的限制** |
| check_pollution_level [state region tag] | 打印指定州区域的污染 |
| check_save | 检查保存和加载是否一致 |
| clearlines | 清除线条 |
| clearspawnedentities | 清除用 spawnentity 命令生成的实体 |
| coa_preview_window | 打开纹章预览窗口 |
| compound_nodeeditor | 复合节点编辑器 |
| conquerall [country tag] | 将所有敌方省份置于我方控制之下 |
| crash | 导致应用程序崩溃 |
| create_ai [self/all/tag] | 为一个或多个国家创建 AI |
| create_building_history | 创建一个符合游戏历史格式的 .txt 文件，包含世界上所有建筑及其州 ID，以及它们的生产方式/补贴配置 |
| create_country [country definition] [country type] [culture] [state id] | 创建一个国家 |
| create_political_movement [<movement type key>] | 创建一个政治运动 |
| create_pop_history | 在 debug.log 中创建包含完整人口历史的转储 |
| create_state_region_data | 创建一个符合游戏数据库格式的 .txt 文件，包含世界上所有州区域及其省份/资源 |
| cthulhu | ? |
| data_types_explorer | 打开数据类型浏览器 dockable |
| data_wrappers_stats [Filter] | 打印有关数据包装器的统计信息 |
| date [date in format yyyy.mm.dd.hh] | 更改当前日期 |
| debug [arguments] | 各种调试操作。参见[控制台命令参数](Console commands.md)。 |
| debug_lens_option | 切换作弊模式 debug_lens_option |
| debug_mode | 切换调试模式 |
| debugcharacters | 创建一个以分号分隔的日志文件，包含有关所有人物的调试信息 |
| debugcountrybudgets | 创建一个以分号分隔的日志文件，包含有关所有国家及其预算的调试信息 |
| debugemployment | 创建并追加一个以逗号分隔的日志文件，包含指定州 ID 中就业的调试信息 |
| debugmarkets | 创建一个以分号分隔的日志文件，包含有关所有商品和市场的调试信息 |
| debugpopconsumption | 创建一个以分号分隔的日志文件，包含所有人口消费的调试信息 |
| debugpopwealth | 创建一个以分号分隔的日志文件，记录所有人口当前的财富状况 |
| debugstates | 写入一个以分号分隔的日志文件，包含有关所有州的调试信息 |
| debugterrainweights | 打印……的数量 |
| debugtheaters | 写入一个以分号分隔的日志文件，包含有关所有战区的调试信息 |
| deiron | 禁用铁人模式 |
| disable_ai [all/tag] | 禁用 AI |
| disable_pop_growth | 切换作弊模式 disable_pop_growth |
| disable_retooling | 切换作弊模式 disable_retooling |
| drawcmdsviewer | 绘制命令查看器 |
| dump_data_types | 转储已注册的数据类型 |
| dump_ref_lookup_memory_report |  |
| enable_ai [all/tag] | 启用 AI |
| entity_editor | 实体编辑器 Dockable |
| escalate [<amount>] | 为玩家的外交博弈增加升级度 |
| event [event name] [<country_tag/province_id>] | 执行一个事件 |
| explorer | 显示对象浏览器窗口 |
| exportbuildings | 写入一个以分号分隔的日志文件，包含所有建筑类型信息 |
| fastbattle | 切换作弊模式 fastbattle（战斗只需一个 tick）**（影响 AI）** |
| fastbuild | 切换作弊模式 fastbuild（使所有建造立即完成）**（影响 AI）** |
| fastbuildships | 立即生产舰船 |
| fastcivilwars | 切换作弊模式 fastcivilwars |
| fastcolonize | 切换作弊模式 fastcolonize **（影响 AI）** |
| fastenact | 切换作弊模式 fastenact（政策颁布立即完成） |
| fasthire | 切换作弊模式 fasthire |
| fastincorporate | 切换作弊模式 fastincorporate（使州的整合只需 1 天） |
| fastinstitutions | 切换作弊模式 fastinstitutions |
| fastinterests | 切换作弊模式 fastinterests |
| fastlobbies | 切换作弊模式 fastlobbies |
| fastmobilize | 切换作弊模式 fastmobilize |
| fastmovements | 切换作弊模式 fastmovements |
| fastresearch | 切换作弊模式 fastresearch |
| fastrevolution | 切换作弊模式 fastrevolution |
| fastsecession | 切换作弊模式 fastsecession |
| fastsecretgoals | 切换作弊模式 fastsecretgoals |
| fasttravels | 切换作弊模式 fasttravels |
| find_unemployed | 查找并报告所有失业人口，可选截断值 |
| fix_state_regions | 修复州区域 |
| force_oos | 使本客户端在多人游戏中失去同步 |
| generate_province_center_objects | 在每个省份中心生成一个带网格的文件 |
| gfx.reloadtexture | 重新加载纹理 |
| gfx.skin | 选择活动的 gfx 皮肤 |
| gfx.texture_limit | 以兆字节为单位设置纹理显存上限 |
| gui_animation_editor | GUI 动画时间轴 Dockable |
| gui_editor | 生成 GUI 编辑器（1.9 中已移除） |
| help [command name] | 打印所有控制台命令或特定命令的说明 |
| hq_show_id | 切换作弊模式 hq_show_id |
| ignore_government_support | 切换作弊模式 ignore_government_support |
| ignore_power_bloc_requirements | 切换作弊模式 ignore_power_bloc_requirements（忽略加入和退出强权集团的影响力要求） |
| invalidate_character [character id] | 使指定 ID 人物上的 modifier 失效 |
| invalidate_country [country id] | 使指定 ID 国家上的 modifier 失效 |
| invalidate_ig [interest group id] | 使指定 ID 利益集团上的 modifier 失效 |
| invalidate_state [state id] | 使指定 ID 州上的 modifier 失效 |
| io_stats | 切换 IO 统计的显示 |
| io_stats.Reset | 重置 IO 统计 |
| kill_character [character name] | 杀死指定姓名的人物 |
| log_status | 日志状态 Dockable |
| log_ticktask_performance | 开始向 profiling.log 输出 ticktask 性能数据 |
| log_viewer | 日志查看器 Dockable |
| map_editor | 切换地图编辑器 |
| mapmode [mapmode] | 切换到给定的地图模式 |
| measure_frame_time ["start" or "stop" measuring] | 测量平均/最小/最大帧时间，停止后将结果打印到 debug.log |
| memory_stats | 切换内存统计的显示 |
| memory_stats.Reset | 重置内存统计 |
| minidump [file path] | 创建一个 minidump |
| money [amount] | 添加指定数量的金钱 |
| net_debuginfo | 打印有关网络层的调试信息 |
| net_stats | 切换网络统计的显示 |
| net_stats.Reset | 重置网络统计 |
| norevolution | 切换作弊模式 norevolution |
| nosecession | 切换作弊模式 nosecession |
| nosupportloss | 防止国家损失战争支持度 |
| noshortages | 防止建筑因补给短缺而受到惩罚 |
| observe | 开始观察游戏 |
| own [province id/state region tag] [country tag] | 更改指定省份或州区域的所有者。州区域标签可在[州区域列表](List of state regions.md)中查找 |
| particleeditor | 粒子节点编辑器 |
| permitmarginalizedingovernment | 切换作弊模式 permitmarginalizedingovernment |
| pops_account_disconnect_steam | 将 Paradox 账户与 Steam 断开连接 |
| pops_account_login [email] [password] | 登录 POPS 账户 |
| pops_account_logout | 退出 POPS 账户 |
| pops_account_status | 显示你是否已登录 POPS |
| popstat | 打印活动人口数量 |
| portrait_editor | 打开肖像编辑器 |
| print_gamestate_modifiers | 打印游戏状态 modifier |
| province_borders [true/false] | 切换省份边界的显示 |
| pseudoLoc | 在文本控件上启用/禁用伪本地化 |
| recalc_cached_data | 重新计算缓存的游戏状态数据 |
| release_mode | 切换发行模式 |
| reload [file name] | 重新加载资源 |
| rendertype | 报告当前使用的渲染后端 |
| research | 获得技术 |
| save_game_analyzer | 打开存档分析器 |
| savegames.delete_all | 删除所有本地存档 |
| savegames.delete_cloud | 删除所有云端存档 |
| screenshot | 截图 |
| script_docs | 打印脚本文档 |
| set_devastation_level [state region tag] [amount] | 设置指定州区域的破坏程度 |
| set_cohesion [committee] [value] | 将委员会的凝聚力设为给定值 |
| set_pollution_level [state region tag] [amount] | 设置指定州区域的污染程度 |
| settings | 生成设置 GUI，可选参数用于初始选中的分类 |
| shader_debug |  |
| shader_editor | 着色器编辑器 Dockable |
| show_goals | 显示 AI 目标 |
| skip_migration | 切换作弊模式 skip_migration |
| sleep | 休眠指定的毫秒数 |
| social_addfriend [Context Index] [Account ID] | 将好友添加到好友列表 |
| social_debuginfo | 打印有关社交层的调试信息 |
| social_joinroom [Context Index] [Room Name] [Nick Name] | 使用给定的社交上下文加入聊天室 |
| social_sendmessage [Context Index] [Room Name] [Message] | 向聊天室发送消息 |
| spawnentity [<entity name>] [<state> (optional)] | 在光标位置生成指定实体 |
| spawnentity_at [<entity name>] [x] [y] [<state> (optional)] | 在 xy 坐标处生成指定实体 |
| spawnline [<line name>] [<start position 'x,y,z'> (no spaces)] [<end position x,y,z> (no spaces)] | 在两个位置之间生成指定的线条 |
| spawnnotification [notificationtype] [<scopeindex>] | 生成指定类型的通知 |
| swapchain.buffers | 查询/设置交换链缓冲区 |
| switchlanguage [language name] | 重新加载本地化文件并切换语言 |
| tag [country_tag] | 切换控制到另一个国家 |
| testaipacts | 测试 AI 是否会解散当前协议 |
| testevent [event name] [<country_tag/province_id>] | 测试一个事件 |
| testobjective [<subgoal key (optional)>] | 测试目标的触发效果 |
| texturelist | 纹理列表 |
| textureviewer | 纹理查看器 |
| time | 现在几点了？ |
| tools.skins | 皮肤编辑器 |
| treatyport [<state region tag>] | 在州区域中夺取条约港 |
| tweak | 生成一个微调 GUI |
| update_distribution | 更新指定州 ID 司令部中的驻军单位分配 |
| update_employment | 在指定州 ID 中的建筑之间转移雇员 |
| validate_employment | 打印各州的失业情况 |
| validate_hubs |  |
| validate_income | 打印存在收入赤字的国家 |
| validate_naval_exits |  |
| validate_pops | 确保所有人口拥有有效参数，否则将其打印到错误日志 |
| version | 显示当前版本信息，输入 1 作为第二个参数可显示长版本 |
| vsync | 切换主交换链的垂直同步 |
| wagerate [building_id] [value] | 获取或设置建筑的工资率 |
| yesmen | AI 将同意玩家的所有外交提案和拉拢出价 |
### 控制台命令参数

| 参数 | 值 | 描述 |
|---|---|---|
| 利益集团名称 | ig_armed_forces | 军队 |
| ig_devout | 虔信派 |  |
| ig_industrialists | 实业家 |  |
| ig_intelligentsia | 知识分子 |  |
| ig_landowners | 地主 |  |
| ig_petty_bourgeoisie | 小资产阶级 |  |
| ig_rural_folk | 乡村民众 |  |
| ig_trade_unions | 工会 |  |
| debug 模式 | ai |  |
| allmoney |  |  |
| alwaysdiplo |  |  |
| alwaysreform |  |  |
| alwaysupgradecolony |  |  |
| artisanchange |  |  |
| assert |  |  |
| cb_use |  |  |
| color |  |  |
| demotiondesc |  |  |
| eco |  |  |
| focusai |  |  |
| fow |  |  |
| influence |  |  |
| info |  |  |
| lines |  |  |
| market |  |  |
| minzoom |  |  |
| pops |  |  |
| profile |  |  |
| promotiondesc |  |  |
| render |  |  |
| textures |  |  |
| tooltips |  |  |
| wireframe |  |  |
| yesmen |  |  |

## 参考

模组制作
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| 地图 | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • [States](State modding.md) |
|---|---|

| 界面 | [Interface](Interface modding.md) • [GUI script](GUI script.md) • [Localization](Localization.md) • [Customizable localization](Localization.md) • [Script localization](Script localization.md) |
|---|---|

| 图形 | [3D Models](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|

| 音频 | Music • [Sound](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • Console commands • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|