---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Trigger
source: https://vic3.paradoxwikis.com/Trigger
pageid: 3389
categories: [1.13, Modding]
fetched: 2026-10-27
---
本文已针对游戏当前[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

另见：
Effect
，
Event target
trigger 通过读取当前游戏状态来充当条件——例如人物的意识形态、某个州的所有权等等。

trigger 分为两种基本类型：内联（inline）和块（block）。内联 trigger 接受一个简单的目标，例如 scope、script value 或已定义的类型。块 trigger 更为复杂，通常接受多个目标，例如一个 scope 和一个 script value。

所有 trigger 都要求处于特定的[scope](Scope.md)。有些 trigger 可在任何 scope 中使用（在下表中标注为"none"），另一些则只在正确的 scope 中才起作用。有些 trigger 会改变当前 scope。

下表由脚本文档生成（*script_docs* 控制台命令）。

## 比较 trigger

比较（comparison）是一种常见的 trigger 类型，用于比较两个数值或游戏对象。下表中的许多 trigger 都是比较 trigger（以目标 `value` 标注），但也可以使用 [script value](Script value.md)、[变量](Variable.md)和[event target](Event target.md)在数值或对象之间直接进行比较。

比较使用以下比较运算符之一：

| 运算符 | 含义 | 反转含义 | 用法 |
|---|---|---|---|
| `<` | （严格）小于 | 大于或等于 | 左侧严格小于右侧 |
| `<=` | 小于或等于 | （严格）大于 | 左侧小于或等于右侧 |
| `=` | （严格）等于 | 不等于 | 左侧与右侧完全相等（可用于非数值） |
| `!=` | 不等于 | （严格）等于 | 左侧与右侧不相等（可用于非数值） |
| `>` | （严格）大于 | 小于或等于 | 左侧严格大于右侧 |
| `>=` | 大于或等于 | （严格）小于 | 左侧大于或等于右侧 |

如果在否定块（例如 `NOT = { }`）内使用比较，则采用其反转含义。

注意，`=` 也用作非比较 trigger、effect 和块的运算符。在这些情况下，`=` 表示赋值而非比较。

### 作为 trigger 的 event target

主条目：
Event target
event target 可用作比较 trigger 的左侧或右侧。例如，`army_size > c:FRA.army_size` 在当前 scope 的陆军规模大于法国的陆军规模时返回 true。对于返回 scope 的 event target，只能检查相等性；而返回数值的 event target 也可用于不等式比较。

| Event target | 描述 | 来源 scope |
|---|---|---|
| ai_army_comparison | 切换到两个国家之间陆军实力对比的 scope（示例：value = ai_army_comparison:root） | country |
| ai_colonization_value | 切换到目标国家 AI 对殖民某战略区域意愿的 scope（示例：value = ai_colonization_value:root） | strategic_region |
| ai_gdp_comparison | 切换到两个国家之间 GDP 对比的 scope（示例：value = ai_army_comparison:root） | country |
| ai_ideological_opinion | 切换到 AI 对 scope 国家在目标国家上的意识形态看法的 scope（示例：value = ai_ideological_opinion:root） | country |
| ai_navy_comparison | 切换到两个国家之间海军实力对比的 scope（示例：value = ai_navy_comparison:root） | country |
| ai_state_value | 切换到目标国家 AI 想拥有 scope 州的意愿的 scope（示例：value = ai_state_value:root） | state |
| ai_subject_value | 切换到 AI 想让 scope 国家成为目标国家附属国的意愿的 scope（示例：value = ai_subject_value:root） | country |
| ai_transit_rights_value | 切换到 AI 想获得穿越目标国家通行权的意愿的 scope（示例：value = ai_transit_rights_value:root） | country |
| ai_treaty_export_value | 切换到目标国家 AI 想通过条约出口 scope 市场商品的意愿的 scope（示例：value = ai_market_export_value:root） | market_goods |
| ai_treaty_fairness | 切换到 AI 对与目标国家现有条约条款（对双方）公平程度评估的 scope（示例：value = ai_treaty_fairness_score:root） | country |
| ai_treaty_import_value | 切换到目标国家 AI 想通过条约进口 scope 市场商品的意愿的 scope（示例：value = ai_market_import_value:root） | market_goods |
| ai_treaty_port_value | 切换到目标国家 AI 想在 scope 州获得条约港的意愿的 scope（示例：value = ai_treaty_port_value:root） | state |
| ai_treaty_trade_value | 切换到目标国家 AI 想进口和出口 scope 市场商品的意愿的 scope（示例：value = ai_market_trade_value:root） | market_goods |
| ai_treaty_value | 切换到 AI 对与目标国家现有条约条款对自身有利程度评估的 scope（示例：value = ai_treaty_value:root） | country |
| army_size | scope 国家的营数，不包括当前已征召的征召兵。 | country |
| army_size_including_conscripts | scope 国家的营数，包括当前已征召的征召兵。 | country |
| army_size_including_raised_conscripts | scope 国家的营数，包括当前已征召的征召兵，但不包括未征召的征召兵。 | country |
| array_define | 引用数组 define 中某个数值的值：array_define:Namespace\|Name\|Index。Index 从 0 开始。 | none |
| average_defense | 返回与国家同属一方的前线上单位的平均防御 | front |
| average_expected_sol | 获取 scope 的平均预期生活水平 | country, state |
| average_offense | 返回与国家同属一方的前线上单位的平均进攻 | front |
| average_progressiveness | 获取 scope 人物或利益集团的平均进步性 | character, interest_group |
| average_sol | 获取 scope 的平均生活水平 | country, state |
| base_price | 获取 scope 商品的基础价格 | goods |
| binding_period | 获取 scope 条约签署时的原始约束期（以天计） | treaty, treaty_options |
| building_levels | 获取 scope 国家的非自给建筑总等级数 | country |
| cached_ai_coastal_population | 切换到记录在 AI 支出变量中的沿海总人口（示例：value = cached_ai_coastal_population） | country |
| cached_ai_incorporated_coastal_population | 切换到记录在 AI 支出变量中的已并入州沿海人口总数（示例：value = cached_ai_incorporated_coastal_population） | country |
| cached_ai_incorporated_population | 切换到记录在 AI 支出变量中的已并入州人口总数（示例：value = cached_ai_incorporated_population） | country |
| cached_ai_overseas_subject_population | 切换到记录在 AI 支出变量中的非相邻直接附属国人口总数（示例：value = cached_ai_overseas_subject_population） | country |
| cached_ai_subject_population | 切换到记录在 AI 支出变量中的直接附属国人口总数（示例：value = cached_ai_subject_population） | country |
| cached_ai_total_population | 切换到记录在 AI 支出变量中的总人口（示例：value = cached_ai_total_population） | country |
| cached_ai_unincorporated_coastal_population | 切换到记录在 AI 支出变量中的未并入州沿海人口总数（示例：value = cached_ai_unincorporated_coastal_population） | country |
| cached_ai_unincorporated_population | 切换到记录在 AI 支出变量中的未并入州人口总数（示例：value = cached_ai_unincorporated_population） | country |
| colonial_growth_per_colony | 切换到国家的每殖民地殖民增长值（示例：colonial_growth_per_colony > 0） | country |
| combat_width | 切换到 scope 省份的战斗宽度乘数 | province |
| command_limit_num_units | 获取一名指挥官根据其指挥上限通常可从其军事编队获得的基准单位数 | character |
| compare_complex_value | 一个需要可解析字符串参数的比较 trigger，会在其使用的上下文中返回该值，例如：scope:root.number_of(armies) | varies |
| compare_value | 一个会在其使用的上下文中返回其值的比较 trigger，例如：root.gold | varies |
| credit | 切换到国家当前可借取的最大信贷额度 | country |
| decree_cost | 切换到某州颁布特定法令的花费 authority > decree_cost:decree_road_maintaintenance | state |
| defense | 返回单位的防御评级（包括其指挥官的影响） | new_combat_unit |
| define | 引用数值或颜色 define 的值：define:Namespace\|Name | none |
| demoralized | 返回单位士气崩溃的人力数 | new_combat_unit |
| detection | 从舰队 scope 链接到舰队中舰船的总侦测值 | military_formation |
| diplomatic_pact_expense_ratio | 切换到该国家外交协定支出与收入之比，限制在 0-1 之间（示例：value = diplomatic_pact_expense_ratio） | country |
| front_length | 返回前线的省份数 | front |
| gdp | 获取 scope 国家的年度预测 GDP | country, state |
| global_gdp | 获取全球年度预测 GDP | none |
| global_productivity | 切换到全球生产力值（示例：global_productivity:high_threshold） | none |
| goal_value | 切换到日志条目的目标值 | journal_entry |
| government_size | 获取 scope 国家当前政府中的政党与独立利益集团数量 | country |
| income | 获取 scope 国家的当前每周收入 | country |
| income_transfer_expenses | 切换到 scope 国家通过条约和协定转移给其他国家的金额（示例：income_transfer_expenses >= 100） | country |
| income_transfer_relative_expenses | 切换到国家通过条约和协定转移给其他国家的收入比例（示例：income_transfer_relative_expenses >= 0.2） | country |
| infamy | 切换到 scope 国家的恶名（示例：infamy >= 2） | country |
| infamy_threshold | 切换到用于比较的恶名等级阈值（infamy_threshold:infamous） | none |
| input_quantity | 切换到条约条款中的输入数量 | treaty_article, treaty_article_options |
| investment | 切换到某机构的当前投资等级（示例：investment < investment_max） | institution |
| investment_max | 切换到国家在某机构的当前最大投资等级（示例：investment < investment_max） | institution |
| investment_pool_income | 获取 scope 国家的当前每周投资池收入 | country |
| legitimacy | 切换到国家的当前合法性格数 | country |
| level | 切换到建筑的等级 | building |
| level_after_queued_constructions | 切换到所有排队建造完成后建筑的等级 | building |
| lobby_foreign_anti_clout | 切换到针对特定国家的所有反该国游说团的总政治力量（lobby_foreign_anti_clout:root >= 0.2） | country |
| lobby_foreign_pro_clout | 切换到针对特定国家的所有亲该国游说团的总政治力量（lobby_foreign_pro_clout:root >= 0.2） | country |
| lobby_in_government_foreign_anti_clout | 切换到针对特定国家的执政政府中所有反该国游说团的总政治力量（lobby_in_government_foreign_anti_clout:root >= 0.2） | country |
| lobby_in_government_foreign_pro_clout | 切换到针对特定国家的执政政府中所有亲该国游说团的总政治力量（lobby_in_government_foreign_pro_clout:root >= 0.2） | country |
| lobby_join_weight | 切换到利益集团加入特定游说团的加入权重（lobby_join_weight:root >= 5） | interest_group |
| lobby_war_opposition | 切换到反对 scope 战争的所有游说团的总政治力量（lobby_war_opposition:root >= 0.2） | country |
| lobby_war_support | 切换到支持 scope 战争的所有游说团的总政治力量（lobby_war_support:root >= 0.2） | country |
| manpower | 返回单位的人力 | new_combat_unit |
| market_export_cap | 基于 scope 市场商品的生产获取市场可出口的最大商品量 | market_goods |
| market_import_cap | 基于 scope 市场商品的消费获取市场可进口的最大商品量 | market_goods |
| migration_pull | 获取某州的迁移拉力或某国家的大规模迁移拉力。 | country, state |
| military_expenses | 获取 scope 国家的当前军事支出（奴隶、工资和商品） | country |
| military_expenses_share | 获取 scope 国家当前军事支出（奴隶、工资和商品）相对于总支出占比 | country |
| mobilization | 返回单位介于 0 到 1 之间的动员值 | new_combat_unit |
| modifier | 切换到当前对象拥有的指定键的 modifier 类型值，例如：modifier:country_influence_add | battle_side, building, character, country, interest_group, market, power_bloc, state |
| momentum | 获取 scope 政党的原始势势头 | party |
| morale | 返回单位的士气 | new_combat_unit |
| mutual_trade_value_with_country | 切换到两个市场之间贸易路线中交易商品的总基础价值（示例：mutual_trade_value_with_country:root >= 1000） | country |
| named_script_value | 一个会在其使用的上下文中计算并返回其值的 script value | none |
| naval_combat_power | 切换到国家的海军战斗力（示例：naval_combat_power > 100） | country |
| naval_hostility_average_damage_dealt | 切换到该国在回溯期内其主动发起的海军敌对行动中造成的平均伤害。如未发现敌对行动则返回 -1。 | country |
| naval_hostility_damage | 切换到该国在当前海军敌对行动中对另一国造成的伤害点数（示例：naval_hostility_damage:root >= 50） | country |
| naval_vulnerability | 切换到基于贸易依赖度和沿海 GDP 占比的国家海军脆弱性得分，上限为某个 define 最大值 | country |
| navy_size | scope 国家的分舰队数。 | country |
| num_active_interests | 切换到国家拥有的活跃利益数量 num_active_interests > 5 | country |
| num_active_natural_interests | 切换到国家拥有的活跃天然利益数量 num_active_natural_interests > 5 | country |
| num_active_plays | 获取 scope 国家当前发起的活跃外交博弈数量 | country |
| num_active_ships | 获取国家、指挥官或军事编队的活跃舰船数，或获取该省中与指定国家结盟的军事编队的活跃舰船数 | character, country, military_formation, province |
| num_active_ships_in_battle | 获取国家、指挥官或军事编队的战斗中活跃舰船数，或获取该省中与指定国家结盟的军事编队的战斗中活跃舰船数 | character, country, military_formation, province |
| num_active_ships_not_in_battle | 获取国家、指挥官或军事编队的非战斗中活跃舰船数，或获取该省中与指定国家结盟的军事编队的非战斗中活跃舰船数 | character, country, military_formation, province |
| num_admirals | 切换到国家的海军上将数量 | country |
| num_alliances | 获取 scope 国家的同盟总数（示例：num_alliances:root >= 2） | country |
| num_alliances_and_defensive_pacts_with_allies | 切换到目标国家与 scope 国家盟友结成的同盟数量（示例：num_alliances_and_defensive_pacts_with_allies:root >= 2） | country |
| num_alliances_and_defensive_pacts_with_rivals | 切换到目标国家与 scope 国家竞争对手结成的同盟和防御条约数量（示例：num_alliances_and_defensive_pacts_with_rivals:root >= 2） | country |
| num_battalions | 返回一名指挥官麾下活跃营的数量 | character |
| num_characters | 切换到国家的人物数量 | country |
| num_colony_projects | 获取 scope 国家当前未完成/进行中的殖民地项目数量 | country |
| num_commanderless_units | 军事编队中因指挥官指挥上限而目前没有指挥官的单位数量。注：被击败的指挥官不指挥单位，即被击败的指挥官越多，无指挥官的单位越多。 | military_formation |
| num_commanders | 切换到国家的指挥官数量 | country |
| num_defending_battalions | 返回与国家同属一方的前线上参与战斗的单位总数，示例：num_defending_battalions(root) | front |
| num_defensive_pacts | 切换到目标国家拥有的防御条约总数（示例：num_defensive_pacts >= 2） | country |
| num_garrison_units | 返回驻扎在某总部的单位数量 | hq |
| num_generals | 切换到国家的将军数量 | country |
| num_income_transfer_pacts | 切换到目标国家拥有的（向他国）转移收入的协定总数（示例：num_income_transfer_pacts >= 2） | country |
| num_income_transfer_treaty_articles | 切换到目标国家拥有的（向他国）转移收入的条约条款总数（示例：num_income_transfer_treaty_articles >= 2） | country |
| num_income_transfers | 切换到目标国家拥有的（向他国）转移收入的协定和条约条款总数（示例：num_income_transfers >= 2） | country |
| num_incorporated_states | 获取 scope 国家当前已并入州的数量 | country |
| num_interests | 切换到国家拥有的利益数量（包括未活跃的） num_interests > 5 | country |
| num_mandates | 切换到 scope 强权集团可用的托管数量（power_bloc.num_mandates > 0） | power_bloc |
| num_mobilized_battalions | 返回一名将军麾下完全动员的单位数量 | character |
| num_natural_interests | 切换到国家拥有的天然利益数量（包括未活跃的） num_natural_interests > 5 | country |
| num_non_destroyed_ships | 获取国家、指挥官或军事编队的未击毁舰船数，或获取该省中与指定国家结盟的军事编队的未击毁舰船数 | character, country, military_formation, province |
| num_non_destroyed_ships_in_battle | 获取国家、指挥官或军事编队的战斗中未击毁舰船数，或获取该省中与指定国家结盟的军事编队的战斗中未击毁舰船数 | character, country, military_formation, province |
| num_non_destroyed_ships_not_in_battle | 获取国家、指挥官或军事编队的非战斗中未击毁舰船数，或获取该省中与指定国家结盟的军事编队的非战斗中未击毁舰船数 | character, country, military_formation, province |
| num_obligations_earned | 从国家切换到他国欠其（=其已赚取）的义务数量 | country |
| num_pending_events | 切换到 scope 国家待处理事件的数量，可为总体或指定类别 num_pending_events > 0 num_pending_events:enactment > 0 | country |
| num_politicians | 切换到国家的政治家数量 | country |
| num_positive_relations | 获取当前与 scope 国家关系为正的国家数量 | country |
| num_provinces | 获取 scope 实体当前的省份数量 | front, state, state_region |
| num_queued_constructions | 切换到目标国家排队的建造总数（示例：num_queued_constructions >= 2） | country |
| num_queued_government_constructions | 切换到目标国家排队的政府建造总数（示例：num_queued_government_constructions >= 2） | country |
| num_queued_private_constructions | 切换到目标国家排队的私人建造总数（示例：num_queued_private_constructions >= 2） | country |
| num_rivals | 切换到目标国家拥有的竞争对手总数（示例：num_rivals >= 2） | country |
| num_ruling_igs | 获取 scope 国家当前政府中利益集团的数量 | country |
| num_shared_rivals | 切换到 scope 国家与目标国家共有的竞争对手数量（示例：num_shared_rivals:root >= 2） | country |
| num_ships | 获取国家、指挥官或军事编队的舰船数，或获取该省中与指定国家结盟的军事编队的舰船数 | character, country, military_formation, province |
| num_ships_in_battle | 获取国家、指挥官或军事编队的战斗中舰船数，或获取该省中与指定国家结盟的军事编队的战斗中舰船数 | character, country, military_formation, province |
| num_ships_not_in_battle | 获取国家、指挥官或军事编队的非战斗中舰船数，或获取该省中与指定国家结盟的军事编队的非战斗中舰船数 | character, country, military_formation, province |
| num_ships_of_group | scope 国家或军事编队中指定舰船组的舰船数 | country, military_formation |
| num_states | 获取 scope 国家当前的州数量 | country |
| num_total_battalions | 返回与国家同属一方的前线上的单位总数，示例：num_total_battalions(root) | front |
| num_unincorporated_states | 获取 scope 国家当前未并入州的数量 | country |
| num_units | 获取指挥官或军事编队的活跃单位数，获取该省中与指定国家结盟的军事编队的活跃单位数 | character, military_formation, province |
| num_units_in_battle | 获取指挥官或军事编队的战斗中活跃单位数，获取该省中与指定国家结盟的军事编队的战斗中活跃单位数 | character, military_formation, province |
| num_units_not_in_battle | 获取指挥官或军事编队的非战斗中活跃单位数，获取该省中与指定国家结盟的军事编队的非战斗中活跃单位数 | character, military_formation, province |
| num_units_share | 指挥官考虑其指挥上限后所得的单位份额。示例：如果该人物有 30 指挥上限，舰队总指挥上限为 60，编队总共有 50 支分舰队，那么该人物应为其战斗分得 25 支分舰队） | character |
| num_world_market_hub_trade_center_levels | 获取与 scope 世界市场中心州关联的贸易中心等级总数 | state |
| offense | 返回单位的进攻评级（包括其指挥官的影响） | new_combat_unit |
| participants | 获取 scope 市场的参与国总数 | market |
| pirated_trade_value_by | 切换到目标国家每周从该国劫掠商品的平均基础价值（示例：pirated_trade_value_by:root >= 50） | country |
| player_owed_obligation_days_left | 切换到外交关系 scope 中某项义务的剩余天数（示例：obligation_days_left >= 2） | diplomatic_relations |
| pop_weight_modifier_scale | 获取人口的权重修正倍率 | pop |
| popularity | 获取作用域人物的人气值，通常介于 -100 到 +100 之间 | character |
| population_below_expected_sol | 作用域切换到该州人口中低于其预期生活水平的百分比（0-1） | state |
| power_projection | 获取作用域编队、单位或舰船的力量投射值 | military_formation, new_combat_unit, ship |
| principal | 获取该国当前的债务本金 | country |
| prosperity | 作用域切换到作用域公司的繁荣度数值（示例：prosperity >= 2） | company |
| rank_value | 作用域切换到特定国家等级的等级值（rank_value:great_power） | none |
| relations | 作用域切换到两国之间的关系值（示例：relations:root >= 2） | country |
| relations_change_rate | 作用域切换到两国关系进展的每日变化值（示例：relations_change_rate:root > 0） | country |
| relations_threshold | 作用域切换到用于比较的关系阈值等级（relations_threshold:warm） | none |
| remaining_binding_period | 获取作用域条约当前剩余的约束期天数 | treaty, treaty_options |
| required_construction | 获取作用域建筑类型所需的建造量 | building_type |
| scope_relations | 作用域切换到外交关系作用域中的关系值（示例：scope_relations >= 2） | diplomatic_relations |
| scope_tension | 作用域切换到外交关系作用域中的紧张度值（示例：scope_tension >= 2） | diplomatic_relations |
| screening | 从舰队作用域链接到舰队中舰船的掩护总值 | military_formation |
| strait_trade_importance_by | 作用域切换到该国经由目标国家所控制海峡进行贸易的商品贸易重要度。若控制者同时控制海峡两侧，累计值会乘以 STRAIT_FULL_CONTROL_TRADE_IMPORTANCE_MULT（示例：strait_trade_importance_by:root >= 100） | country |
| techs_researched | 作用域切换到一国当前已完成研究的科技数量 | country |
| tension | 作用域切换到两国之间的紧张度（示例：tension:root >= 2） | country |
| tension_threshold | 作用域切换到用于比较的紧张度等级阈值（tension_threshold:warm） | none |
| total_crew_needed | 获取一国所有舰船所需的水手总数 | country |
| total_export_value | 作用域切换到作用域国家向世界市场出口的总价值（示例：total_export_value >= 1000） | country |
| total_import_value | 作用域切换到作用域国家从世界市场进口的总价值（示例：total_import_value >= 1000） | country |
| total_marine_capacity | 获取一国所有舰队的海军陆战队容量总数 | country |
| total_pirated_trade_value | 作用域切换到外交关系作用域中两国之间通过海盗行为劫掠的商品每周平均基础总价值（示例：total_pirated_trade_value >= 100） | diplomatic_relations |
| total_trade_value | 作用域切换到作用域国家与世界市场贸易的总价值（示例：total_trade_value >= 1000） | country |
| training_rate | 作用域切换到建筑当前每周的最大训练速率 | building |
| treaty_exports | 获取作用域 MarketGoods 中该商品向该市场出口的条约（非世界市场）数量 | market_goods |
| treaty_imports | 获取作用域 MarketGoods 中该商品向该市场进口的条约（非世界市场）数量 | market_goods |
| value | 数值字面量，例如：1、5.2、-6 | none |
| visibility | 从舰队作用域链接到舰队中舰船的能见度总值 | military_formation |
| vulnerability | 从舰队作用域链接到舰队中舰船的脆弱性总值 | military_formation |
| weekly_prosperity_change | 作用域切换到作用域公司的每周繁荣度变化（示例：weekly_prosperity_change >= 2） | company |

## 迭代器 trigger

迭代器（Iterator）会检视所有相关 scope 并输出其中一个或多个。默认情况下，迭代器只检视其中一个相关 scope，但可以通过 `count` 或 `percent` 参数强制检视更多

| Trigger | 描述 | 示例 | Scopes | 目标 |
|---|---|---|---|---|
| any_active_law | 遍历一国所有生效中的法律 | any_active_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | law |
| any_active_party | 遍历一国所有活跃的政党 | any_active_party = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | party |
| any_character | 遍历全球所有人物 | any_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | character |
| any_character_in_exile_pool | 遍历流亡池中的人物 | any_character_in_exile_pool = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | character |
| any_character_in_void | 遍历虚空（void）中的人物 | any_character_in_void = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | character |
| any_character_role | 遍历作用域人物的所有角色 | any_character_role = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character | character_role |
| any_civil_war | 遍历与作用域国家相关的所有内战 | any_civil_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | civil_war |
| any_cobelligerent_in_diplo_play | 遍历作用域国家在所有外交博弈（包括战争）中的所有共同交战国 | any_cobelligerent_in_diplo_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_cobelligerent_in_war | 遍历作用域国家在所有战争中的所有共同交战国 | any_cobelligerent_in_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_combat_unit | 遍历输入作用域的所有作战单位 | any_combat_unit = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | battle, building, front, hq, military_formation | new_combat_unit |
| any_company | 遍历一国所有公司 | any_company = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | company |
| any_country | 遍历全球所有国家 | any_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | country |
| any_country_in_<georegion_short_name> | 遍历指定地理区域内的所有国家 | any_country_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | country |
| any_country_strategic_region | 遍历包含作用域国家所拥有州的所有战略区域 | any_country_strategic_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | strategic_region |
| any_decentralized_country | 遍历所有非中央集权（decentralized）国家 | any_decentralized_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | country |
| any_diplomatic_catalyst | 遍历一国近期记忆中的所有外交催化剂 | any_diplomatic_catalyst = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | diplomatic_catalyst |
| any_diplomatic_play | 遍历全球所有外交博弈 | any_diplomatic_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | diplomatic_play |
| any_diplomatically_relevant_country | 遍历国家作用域的所有外交相关国家 | any_diplomatically_relevant_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_direct_subject | 层级中直接位于当前国家之下的任何国家 | any_direct_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_enemy_in_diplo_play | 遍历作用域国家在所有外交博弈（包括战争）中的所有敌国 | any_enemy_in_diplo_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_enemy_in_war | 遍历作用域国家在所有战争中的所有敌国 | any_enemy_in_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成状况 | any_harvest_condition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state, state_region, strategic_region | harvest_condition |
| any_in_global_list | 遍历全局列表中的所有条目。 | any_in_global_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } 由 add_to_(temporary)_list 创建的列表使用 "list" 由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| any_in_hierarchy | 当前层级中的任何国家，包括当前国家本身 | any_in_hierarchy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_in_list | 遍历列表中的所有条目。 | any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } 由 add_to_(temporary)_list 创建的列表使用 "list" 由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| any_in_local_list | 遍历局部列表中的所有条目。 | any_in_local_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } 由 add_to_(temporary)_list 创建的列表使用 "list" 由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| any_influenced_interest_group | 遍历受一个政治运动影响的所有利益集团 | any_influenced_interest_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_movement | interest_group |
| any_interest_group | 遍历一国所有利益集团 | any_interest_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | interest_group |
| any_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | any_key_in_global_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | any_key_in_local_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_key_in_variable_map | 遍历变量映射中的所有键。 | any_key_in_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_law | 遍历一国所有法律 | any_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | law |
| any_lobby_member | 遍历一个游说团体的所有利益集团成员 | any_lobby_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_lobby | interest_group |
| any_market | 遍历全球所有市场 | any_market = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | market |
| any_market_goods | 遍历一个市场中所有活跃的（市场）商品 | any_market_goods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | market | market_goods |
| any_member | 遍历一个政党的所有利益集团成员 | any_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | party | interest_group |
| any_military_formation | 遍历输入作用域中当前存在的所有军事编队 | any_military_formation = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, hq | military_formation |
| any_neighbouring_state | 遍历一个州区域相邻的所有州 | any_neighbouring_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state, state_region, strategic_region | state |
| any_overlord_or_above | 层级中位于当前国家之上的任何国家 | any_overlord_or_above = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_owned_country | 遍历作用域公司拥有的所有国家 | any_owned_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | company | country |
| any_participant | 作用域中外交条约的任意一方参与者 | any_participant = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_pact | country |
| any_political_lobby | 遍历一个国家或利益集团中的所有政治游说团体 | any_political_lobby = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, interest_group | political_lobby |
| any_political_movement | 遍历一国所有政治运动 | any_political_movement = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | political_movement |
| any_possible_amendment_type | 遍历可添加到作用域法律的修正案类型 | any_possible_amendment_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | law | amendment_type |
| any_potential_party | 遍历一国所有潜在的政党 | any_potential_party = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | party |
| any_power_bloc | 遍历所有强权集团 | any_power_bloc = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | power_bloc |
| any_power_bloc_member | 遍历作用域强权集团的所有成员，包括领导者 | any_power_bloc_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | power_bloc | country |
| any_preferred_law | 遍历利益集团所在国家所有生效及可能的法律，按其对该法律的偏好程度排序 | any_preferred_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | interest_group | law |
| any_primary_culture | 作用域国家或国家定义的主要文化 | any_primary_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, country_definition | culture |
| any_province | 遍历作用域州中的所有省份 | any_province = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state | province |
| any_province_in_<georegion_short_name> | 遍历指定地理区域中的所有省份 | any_province_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | province |
| any_rival_country | 作用域国家与之竞争的任何国家 | any_rival_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_rivaling_country | 与作用域国家相竞争的任何国家 | any_rivaling_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_scope_admiral | 遍历以下作用域中的所有海军上将：国家、利益集团或军事编队 | any_scope_admiral = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_ally | 遍历一个国家的所有同盟 | any_scope_ally = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_scope_amendment | 遍历作用域法律的修正案 | any_scope_amendment = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | law | amendment |
| any_scope_army | 遍历输入作用域中当前存在的所有陆军 | any_scope_army = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, hq | military_formation |
| any_scope_article | 遍历作用域条约的条款 | any_scope_article = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty | treaty_article |
| any_scope_article_option | 遍历作用域条约或 treaty_options 的条款选项 | any_scope_article_option = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty, treaty_options | treaty_article_options |
| any_scope_building | 遍历以下作用域中的所有建筑：州、国家 | any_scope_building = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state | building |
| any_scope_character | 遍历以下作用域中的所有人物：国家、利益集团或前线 | any_scope_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_country | 遍历在支持的作用域（目前：市场、战略区域）中有存在的所有国家 | any_scope_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | market, state_region, strategic_region | country |
| any_scope_culture | 遍历作用域中的所有文化 | any_scope_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state | culture |
| any_scope_diplomatic_pact | 作用域国家的任何外交条约 | any_scope_diplomatic_pact = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | diplomatic_pact |
| any_scope_fleet | 遍历输入作用域中当前存在的所有舰队 | any_scope_fleet = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, hq | military_formation |
| any_scope_front | 遍历与作用域战争相关的所有前线 | any_scope_front = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | war | front |
| any_scope_general | 遍历以下作用域中的所有将军：国家、利益集团、前线或军事编队 | any_scope_general = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_held_interest_marker | 遍历一个国家持有的所有利益标记 | any_scope_held_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | interest_marker |
| any_scope_homeland_state | 遍历作为作用域文化家园的所有州，或作用域国家任一主要文化家园的所有州 | any_scope_homeland_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character, country | state |
| any_scope_initiator_ally | 遍历外交博弈中发起方的所有同盟 | any_scope_initiator_ally = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_play | country |
| any_scope_interest_marker | 遍历以下作用域中的所有利益标记：国家、战略区域 | any_scope_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state_region, strategic_region | interest_marker |
| any_scope_je_involved | 遍历一个日志条目的所有参与方 | any_scope_je_involved = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | journal_entry | country |
| any_scope_play_involved | 遍历一个外交博弈的所有参与方 | any_scope_play_involved = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_play | country |
| any_scope_politician | 遍历以下作用域中的所有政客：国家或利益集团 | any_scope_politician = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_pop | 遍历以下作用域中的所有人口：国家、州、利益集团、文化 | any_scope_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, culture, interest_group, state | pop |
| any_scope_regional_hqs | 遍历作用域公司的区域总部 | any_scope_regional_hqs = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | company | building |
| any_scope_ship | 遍历一个国家或军事编队中的所有舰船 | any_scope_ship = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, military_formation | ship |
| any_scope_state | 遍历以下作用域中包括省份在内的所有州：国家、州区域、战区、前线或海峡 | any_scope_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, state_region, strait, strategic_region, theater | state |
| any_scope_strait | 遍历在作用域州或国家拥有陆地端点的所有海峡 | any_scope_strait = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state | strait |
| any_scope_target_ally | 遍历外交博弈中目标方的所有同盟 | any_scope_target_ally = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_play | country |
| any_scope_theater | 遍历一个国家的所有战区（theater） | any_scope_theater = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | theater |
| any_scope_treaty | 遍历约束 scope 所指国家的生效条约 | any_scope_treaty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | treaty |
| any_scope_violate_sovereignty_interested_parties | 遍历所有会因 scope 所指国家的主权被侵犯而感兴趣的国家 | any_scope_violate_sovereignty_interested_parties = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_scope_violate_sovereignty_wars | 遍历目标国家被 scope 所指国家侵犯主权时会涉及的所有相关战争 | any_scope_violate_sovereignty_wars = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | war |
| any_scope_war | 遍历与该 scope 相关的所有战争 | any_scope_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | war |
| any_sea_node_adjacent_state | 遍历与某个州共享一个海上节点的所有州 | any_sea_node_adjacent_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state | state |
| any_state | 遍历全球所有州 | any_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state |
| any_state_in_<georegion_short_name> | 遍历指定地理区域内的所有州 | any_state_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state |
| any_state_region | 遍历所有州域（state region） | any_state_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state_region |
| any_state_region_in_<georegion_short_name> | 遍历指定地理区域内的所有州域 | any_state_region_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state_region |
| any_strategic_objective | 遍历 scope 所指国家的所有战略目标州 | any_strategic_objective = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | state |
| any_strategic_region | 遍历全球所有战略区域 | any_strategic_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | strategic_region |
| any_strategic_region_in_<georegion_short_name> | 遍历指定地理区域内的所有战略区域 | any_strategic_region_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | strategic_region |
| any_subject_of_subject | 层级中位于直接附属国之下的任何国家 | any_subject_of_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_subject_or_below | 层级中位于当前国家之下的任何国家 | any_subject_or_below = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_supporting_character | 遍历支持 scope 所指政治运动的所有人物 | any_supporting_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_movement | character |
| any_treaty | 遍历条约（包括生效条约和草案） | any_treaty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | treaty |
| any_valid_mass_migration_culture | 列出 scope 所指国家中适合进行大规模迁移的文化 | any_valid_mass_migration_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | culture |
| any_war_participant | 遍历一场战争中的所有参战方 | any_war_participant = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | war | country |

## 流程 trigger

流程 trigger 控制其他 trigger 的使用方式，包括条件判断、循环以及提示文本。它们可在任何 scope 中使用。

| Trigger | 描述 | 示例 | Scopes | Targets |
|---|---|---|---|---|
| all_false | 若所有包含的 trigger 均为假则为真（等价于 NOR） |  | none |  |
| and | 若所有包含的 trigger 均为真则为真；遇到第一个为假的子 trigger 时即返回假 |  | none |  |
| any_false | 若任一包含的 trigger 为假则为真（等价于 NAND） |  | none |  |
| calc_true_if | 若指定数量的子 trigger 返回真，则返回真 | calc_true_if = { amount = 2 <trigger> <trigger> <trigger> } | none |  |
| custom_description | 为所包裹的 trigger 提供自定义描述，而非自动生成的描述 | custom_description = { text = <trigger_localization_key> subject = <optional subject scope> #defaults to current scope object = <optional object scope> value = <optional script value> ... triggers ... } | none |  |
| custom_tooltip | 用自定义文本替换所包裹 trigger 的提示内容 | custom_tooltip = { text = <text> subject = <scope> (optional) <trigger> } | none |  |
| hidden_trigger | 所包裹的 trigger 不会在提示中显示 | hidden_trigger = { <more triggers> } | none |  |
| nand | 取反的 AND trigger。若所有包含的 trigger 均返回真则返回假；遇到第一个为假的子 trigger 时即返回真 |  | none |  |
| nor | 取反的 OR trigger。若所有包含的 trigger 均返回假则返回真；遇到第一个为真的 trigger 时即返回假 |  | none |  |
| not | 对 trigger 内容取反。若所有包含的 trigger 均返回假则返回真 |  | none |  |
| or | 若所有包含的 trigger 均为假则为假；遇到第一个为真的子 trigger 时即返回真 |  | none |  |
| switch | 依据某个 trigger 的结果进行分支判断，以评估另一个 trigger，并可附加一个可选的回退 trigger | switch = { trigger = simple_assign_trigger case_1 = { <triggers> } case_2 = { <triggers> } case_n = { <triggers> } fallback = { <triggers> } | none |  |
| trigger_else | 若前序 'trigger_if' 或 'trigger_else_if' 的 trigger 条件未满足，则评估其中的 display_triggers | trigger_if = { limit = { <triggers> } <display_triggers> } trigger_else = { <display_triggers> } | none |  |
| trigger_else_if | 若前序 `trigger_if` 或 `trigger_else_if` 的 trigger 条件未满足、且自身 limit 的 trigger 已满足，则评估其中的 display_triggers | trigger_if = { limit = { <triggers> } <display_triggers> } trigger_else_if = { limit = { <triggers> } <display_triggers> } | none |  |
| trigger_if | 若 limit 的 trigger 条件已满足，则评估其中的 display_triggers | trigger_if = { limit = { <triggers> } <display_triggers> } | none |  |
| weighted_calc_true_if | 若已满足的子 trigger 权重之和达到指定数值，则返回真 | weighted_calc_true_if = { amount = 10 5 = { <trigger> } 15 = { <trigger> } 7 = { <trigger> } } | none |  |

## 日志 trigger

日志 trigger 会输出消息，用于测试和调试。它们可在任何 scope 中使用。

| Trigger | 描述 | 示例 | Scopes | Targets |
|---|---|---|---|---|
| assert_if | 在运行时有条件地触发一个断言 | assert_if = { limit = { <triggers> } text = <string> (optional) } | none |  |
| assert_read | 在读取时有条件地触发一个断言 | assert_read = yes / <string> | none |  |
| debug_log | 记录父 trigger 成功或失败 |  | none |  |
| debug_log_details | 记录父 trigger 成功或失败，并记录哪些子 trigger 成功或失败 |  | none |  |

## 变量 trigger

变量 trigger 用于检查一个[变量](Variable.md)。它们可在任何 scope 中使用，但可能需要特定 scope 才能读取到正确的变量。

| Trigger | 描述 | 示例 | Scopes | Targets |
|---|---|---|---|---|
| add_to_temporary_list | 保存一个临时目标，供 trigger 执行期间使用 | 此方法用于在 trigger 中构建列表。如果在 any 类 trigger 内使用，其在 trigger 中的位置十分重要。游戏会遍历该 any 类 trigger 的每一个实例，直到找到单个满足条件的实例，然后停止。若要添加所有满足特定条件的 scope 实例，请使用 "count = all"，同时将这个 "effect" 放在 any 类 trigger 的最末尾，以便在每次迭代时对所有条件进行评估。 | none |  |
| any_in_global_list | 遍历全局列表中的所有项目。 | any_in_global_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| any_in_list | 遍历列表中的所有项目。 | any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| any_in_local_list | 遍历局部列表中的所有项目。 | any_in_local_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| any_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | any_key_in_global_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | any_key_in_local_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_key_in_variable_map | 遍历变量映射中的所有键。 | any_key_in_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| global_variable_list_size | 检查全局变量列表的大小 | global_variable_list_size = { name = <variable name> value >= <value> } | none |  |
| global_variable_map_size |  | global_variable_map_size = { name = the name of the global map value >= script value or number } | none |  |
| has_global_variable | 检查当前 scope 是否设置了指定的全局变量 | has_global_variable = name | none |  |
| has_global_variable_list | 检查当前 scope 是否设置了指定的全局变量列表 | has_global_variable_list = name | none |  |
| has_global_variable_map | 检查当前 scope 是否设置了指定的全局变量映射 | has_global_variable_map = name | none |  |
| has_local_variable | 检查当前 scope 是否设置了指定的局部变量 | has_local_variable = name | none |  |
| has_local_variable_list | 检查当前 scope 是否设置了指定的局部变量列表 | has_local_variable_list = name | none |  |
| has_local_variable_map | 检查当前 scope 是否设置了指定的局部变量映射 | has_local_variable_map = name | none |  |
| has_variable | 检查当前 scope 是否设置了指定的变量 | has_variable = name | none |  |
| has_variable_list | 检查当前 scope 是否设置了指定的变量列表 | has_variable_list = name | none |  |
| has_variable_map | 检查当前 scope 是否设置了指定的变量映射 | has_variable_map = name | none |  |
| is_in_list | 检查某个目标是否在列表中 |  | none |  |
| is_key_in_global_variable_map | 检查某个目标是否为全局变量映射中的键 | is_key_in_global_variable_map = { name = name of the variable target = event target } | none |  |
| is_key_in_local_variable_map | 检查某个目标是否为局部变量映射中的键 | is_key_in_local_variable_map = { name = name of the variable target = event target } | none |  |
| is_key_in_variable_map | 检查某个目标是否为变量映射中的键 | is_key_in_variable_map = { name = name of the variable target = event target } | none |  |
| is_target_in_global_variable_list | 检查某个目标是否在全局变量列表中 | is_target_in_global_variable_list = { name = <variable name> target = <event target> } | none |  |
| is_target_in_local_variable_list | 检查某个目标是否在局部变量列表中 | is_target_in_local_variable_list = { name = <variable name> target = <event target> } | none |  |
| is_target_in_variable_list | 检查某个目标是否在变量列表中 | is_target_in_variable_list = { name = <variable name> target = <event target> } | none |  |
| is_value_in_global_variable_map | 检查某个目标是否为全局变量映射中的值 | is_value_in_global_variable_map = { name = name of the variable target = event target } | none | none |
| is_value_in_local_variable_map | 检查某个目标是否为局部变量映射中的值 | is_value_in_local_variable_map = { name = name of the variable target = event target } | none | none |
| is_value_in_variable_map | 检查某个目标是否为变量映射中的值 | is_value_in_variable_map = { name = name of the variable target = event target } | none | none |
| list_size | 检查列表的大小 | list_size = { name = <list name> value >= <value> } | none | value |
| local_variable_list_size | 检查局部变量列表的大小 | local_variable_list_size = { name = <variable name> value >= <value> } | none |  |
| local_variable_map_size |  | local_variable_map_size = { name = the name of the local map value >= script value or number } | none |  |
| variable_list_size | 检查变量列表的大小 | variable_list_size = { name = <variable name> value >= <value> } | none |  |
| variable_map_size |  | variable_map_size = { name = the name of the global map value >= script value or number } | none |  |

## 按 scope 分类的 trigger

下表按所需 scope 列出各 trigger。较少使用的 scope 以及只有少量特定 effect 的 scope 已被省略，可在完整的 trigger 列表中查找。迭代器（iterator）已被省略，可在上文或下文中查找。部分 trigger 会重复出现，因为它们可用于多个 scope。

### 无/任意 scope

| Trigger | 描述 | 示例 | Targets |
|---|---|---|---|
| active_lens | 检查指定的镜头（lens）是否已打开 | active_lens = lens |  |
| active_lens_option | 检查指定的镜头选项是否已激活 | active_lens_option = lens_option_key |  |
| add_to_temporary_list | 保存一个临时目标，供 trigger 执行期间使用 | 此方法用于在 trigger 中构建列表。如果在 any 类 trigger 内使用，其在 trigger 中的位置十分重要。游戏会遍历该 any 类 trigger 的每一个实例，直到找到单个满足条件的实例，然后停止。若要添加所有满足特定条件的 scope 实例，请使用 "count = all"，同时将这个 "effect" 放在 any 类 trigger 的最末尾，以便在每次迭代时对所有条件进行评估。 |  |
| all_false | 若所有包含的 trigger 均为假则为真（等价于 NOR） |  |  |
| always | 检查所赋的 yes/no 值是否为真 | always = yes # always succeeds always = no # always fails always = scope:a_boolean_value # evaluated at runtime | boolean |
| and | 若所有包含的 trigger 均为真则为真；遇到第一个为假的子 trigger 时即返回假 |  |  |
| any_false | 若任一包含的 trigger 为假则为真（等价于 NAND） |  |  |
| assert_if | 在运行时有条件地触发一个断言 | assert_if = { limit = { <triggers> } text = <string> (optional) } |  |
| assert_read | 在读取时有条件地触发一个断言 | assert_read = yes / <string> |  |
| calc_true_if | 若指定数量的子 trigger 返回真，则返回真 | calc_true_if = { amount = 2 <trigger> <trigger> <trigger> } |  |
| can_create_treaty | 检查国家之间能否创建条约 | can_create_treaty = { first_country = <country> # (default: none) must _not_ be specified if the created treaty is an amendment second_country = <country> # (default: none) must _not_ be specified if the created treaty is an amendment amends = <treaty> # (default: none) if specified, the created treaty will be an amendment to the specified treaty is_draft = yes \| no # (default: yes) must be yes if this treaty is an amendement to an existing treaty entered_into_force_on = <date> # (default: none) means "today" if not specified (for non-drafts). Must _not_ be specified for drafts. Cannot be in the future binding_period = { # (default: 0) must be a nonnegative number, fractional parts will be ignored (truncation) days = <nonnegative number> \| weeks = <nonnegative number> \| months = <nonnegative number> \| years = <nonnegative number> } articles_to_create = { # (default: empty) non-amendments must have at least one article to create { article = <key> # (default: empty) the type of article (determined by script) source_country = <country> # (default: none) directed articles _must_ specify this value, mutual articles _must not_ specify this value target_country = <country> # (default: none) directed articles _must_ specify this value, mutual articles _must not_ specify this value inputs = { # (default: empty) list of inputs values as required by the article { quantity = <positive number> \| good = <good> \| state = <state> \| strategic_region = <strategic region> \| company = <company> # TODO: or company type? \| building = <building> # TODO: or building type? \| law = <law> # TODO: or law type? \| country = <country> } { ... } # one input per required input of the corresponding article type } } # some examples of valid articles { article = alliance } # mutual, no inputs { article = resource_transfer # directed source_country = c:FRA # because directed target_country = c:GBR # because directed inputs = { { quantity = 250 } # because resource_transfer has required_inputs = { quantity good } { good = g:coal } # because resource_transfer has required_inputs = { quantity good } } } } } |  |
| can_start_tutorial_lesson | 能否开始指定的教程课程？ | can_start_tutorial_lesson = reactive_advice_succession |  |
| current_tooltip_depth | 返回当前屏幕上已打开提示的数量 |  | value |
| custom_description | 为所包裹的 trigger 提供自定义描述，而非自动生成的描述 | custom_description = { text = <trigger_localization_key> subject = <optional subject scope> #defaults to current scope object = <optional object scope> value = <optional script value> ... triggers ... } |  |
| custom_tooltip | 用自定义文本替换所包裹 trigger 的提示内容 | custom_tooltip = { text = <text> subject = <scope> (optional) <trigger> } |  |
| day_value | 昼间值 |  | value |
| daynight_value | 昼夜值 |  | value |
| debug_log | 记录父 trigger 成功或失败 |  |  |
| debug_log_details | 记录父 trigger 成功或失败，并记录哪些子 trigger 成功或失败 |  |  |
| exists | 检查指定的 scope 目标是否存在（即检查其是否为 null 对象） | exists = from.owner.var:cool_var.mother |  |
| game_date | 与当前游戏日期进行比较 | game_date = 1837.1.1 | value |
| global_population | 比较全球人口 | global_population > 2000000000 | value |
| global_variable_list_size | 检查全局变量列表的大小 | global_variable_list_size = { name = <variable name> value >= <value> } |  |
| global_variable_map_size |  | global_variable_map_size = { name = the name of the global map value >= script value or number } |  |
| has_account_item | 玩家的账户中是否拥有该物品 | has_account_item = <key> |  |
| has_cosmetic_dlc | 客户端是否拥有该外观 DLC |  |  |
| has_dlc_feature | 主机是否拥有启用该特定功能的 DLC |  |  |
| has_game_rule | 给定的游戏规则设置是否已启用？ | has_game_rule = faster_conversion |  |
| has_game_started | 若游戏已开始则为真 | has_game_started = bool | boolean |
| has_gameplay_dlc | 主机是否拥有该玩法 DLC |  |  |
| has_global_variable | 检查当前 scope 是否设置了指定的全局变量 | has_global_variable = name |  |
| has_global_variable_list | 检查当前 scope 是否设置了指定的全局变量列表 | has_global_variable_list = name |  |
| has_global_variable_map | 检查当前 scope 是否设置了指定的全局变量映射 | has_global_variable_map = name |  |
| has_local_variable | 检查当前 scope 是否设置了指定的局部变量 | has_local_variable = name |  |
| has_local_variable_list | 检查当前 scope 是否设置了指定的局部变量列表 | has_local_variable_list = name |  |
| has_local_variable_map | 检查当前 scope 是否设置了指定的局部变量映射 | has_local_variable_map = name |  |
| has_map_interaction | 检查该地图交互类型是否处于激活状态 | has_map_interaction = key |  |
| has_map_interaction_diplomatic_action | 检查我们当前的地图交互是否为特定的外交行动 | has_map_interaction_diplomatic_action = <key> |  |
| has_reached_end_date | 若已到达结束日期（NDefines::NGame::END_DATE）则为真 | has_reached_end_date = yes | boolean |
| has_unification_candidate | 检查该国家 tag 是否至少拥有一个统一候选国 | has_country_unification_candidate = GER |  |
| has_variable | 检查当前 scope 是否设置了指定的变量 | has_variable = name |  |
| has_variable_list | 检查当前 scope 是否设置了指定的变量列表 | has_variable_list = name |  |
| has_variable_map | 检查当前 scope 是否设置了指定的变量映射 | has_variable_map = name |  |
| hidden_trigger | 所包裹的 trigger 不会在提示中显示 | hidden_trigger = { <more triggers> } |  |
| is_building_type_expanded | 检查某个 CBuildingType 对应的 CProductionMethodsPanelEntry 是否已展开 | is_building_type_expanded = <scope/key> |  |
| is_game_paused | 检查游戏是否已暂停 | is_game_paused = yes/no | boolean |
| is_gamestate_tutorial_active | 游戏状态教程是否处于激活状态？参见 tutorial_lesson_chains 文档中的 save_progress_in_gamestate。 |  | boolean |
| is_in_list | 检查某个目标是否在列表中 |  |  |
| is_key_in_global_variable_map | 检查某个目标是否为全局变量映射中的键 | is_key_in_global_variable_map = { name = name of the variable target = event target } |  |
| is_key_in_local_variable_map | 检查某个目标是否为局部变量映射中的键 | is_key_in_local_variable_map = { name = name of the variable target = event target } |  |
| is_key_in_variable_map | 检查某个目标是否为变量映射中的键 | is_key_in_variable_map = { name = name of the variable target = event target } |  |
| is_lens_open | 检查某个镜头是否已打开，以镜头 key 指定。可指定一个可选的具名标签页，以检查该标签页是否已打开。 | is_lens_open = { lens = lens_key tab_name = tab_key } |  |
| is_objective_completed | scope 所指国家的该目标是否已完成？ | is_objective_completed = yes | boolean |
| is_panel_open | 检查某个信息面板是否打开，以 event target（target）或字符串（panel_name）指定。可指定一个可选的具名标签页（tab_name）来检查该标签页是否打开。 | is_panel_open = { target = <scope> OR panel_name = panel_name tab_name = tab_name } |  |
| is_popup_open | 检查指定的弹窗面板是否打开 | is_popup_open = popup |  |
| is_rightclick_menu_open | 检查指定的右键菜单是否打开 | is_rightclick_menu_open = <menu_key> |  |
| is_set | 检查指定的 scope 目标是否已被设置（包括为空对象的情况） | is_set = from.owner.var:cool_var.mother |  |
| is_target_in_global_variable_list | 检查某个目标是否在一个全局变量列表中 | is_target_in_global_variable_list = { name = <variable name> target = <event target> } |  |
| is_target_in_local_variable_list | 检查某个目标是否在一个局部变量列表中 | is_target_in_local_variable_list = { name = <variable name> target = <event target> } |  |
| is_target_in_variable_list | 检查某个目标是否在一个变量列表中 | is_target_in_variable_list = { name = <variable name> target = <event target> } |  |
| is_template_used | 检查人物模板是否已被使用 | is_template_used = template_key |  |
| is_theme_selected | 玩家是否在设置中选择了该主题 | is_theme_selected = <key> |  |
| is_tutorial_active | 教程是否处于激活状态？ |  | boolean |
| is_tutorial_lesson_active | 这是否是当前的教程课程？ | is_tutorial_lesson_active = reactive_advice_succession |  |
| is_tutorial_lesson_chain_completed | 指定键的教程课程链是否已完成？ |  |  |
| is_tutorial_lesson_completed | 指定名称的教程课程是否已完成？ |  |  |
| is_tutorial_lesson_step_completed | 教程课程步骤是否已完成？ | is_tutorial_lesson_step_completed = lesson_key:step_key |  |
| is_value_in_global_variable_map | 检查某个目标是否是全局变量映射中的一个值 | is_value_in_global_variable_map = { name = name of the variable target = event target } | none |
| is_value_in_local_variable_map | 检查某个目标是否是局部变量映射中的一个值 | is_value_in_local_variable_map = { name = name of the variable target = event target } | none |
| is_value_in_variable_map | 检查某个目标是否是变量映射中的一个值 | is_value_in_variable_map = { name = name of the variable target = event target } | none |
| list_size | 检查列表的大小 | list_size = { name = <list name> value >= <value> } | value |
| local_variable_list_size | 检查局部变量列表的大小 | local_variable_list_size = { name = <variable name> value >= <value> } |  |
| local_variable_map_size |  | local_variable_map_size = { name = the name of the local map value >= script value or number } |  |
| month | 与当前游戏日期的月份比较（一月：0，十二月：11） | month > 10 | value |
| nand | 取反的 AND trigger 若所有包含的 trigger 均返回 true 则返回 false；在遇到第一个返回 false 的子 trigger 时返回 true |  |  |
| night_value | 夜晚值 |  | value |
| nor | 取反的 OR trigger 若所有包含的 trigger 均返回 false 则返回 true；在遇到第一个返回 true 的 trigger 时返回 false |  |  |
| not | 对 trigger 的内容取反 若所有包含的 trigger 均返回 false 则返回 true |  |  |
| or | 若所有包含的 trigger 均为 false 则返回 false 在遇到第一个为 true 的子 trigger 时返回 true |  |  |
| real_month | 与当前现实日期的月份比较（一月：1，十二月：12） | real_month > 10 | value |
| save_temporary_scope_as | 将当前 scope 保存为一个临时目标，供本次 trigger 执行期间使用。不能覆盖已保存的 scope | save_temporary_scope_as = <string> |  |
| save_temporary_scope_value_as | 将一个数值或布尔值保存为任意命名的临时目标，供稍后在同一 trigger 中引用。不能覆盖已保存的 scope 值 | save_temporary_scope_value_as = { name = <string> value = <script_value> } |  |
| should_show_nudity | 是否可以显示裸露内容？ | should_show_nudity = yes/no | boolean |
| switch | 依据一个 trigger 进行分支以评估另一个 trigger，可带一个可选的回退 trigger。 | switch = { trigger = simple_assign_trigger case_1 = { <triggers> } case_2 = { <triggers> } case_n = { <triggers> } fallback = { <triggers> } |  |
| trigger_else | 当前面的 'trigger_if' 或 'trigger_else_if' 的 trigger 不满足时，评估其中的 display_triggers | trigger_if = { limit = { <triggers> } <display_triggers> } trigger_else = { <display_triggers> } |  |
| trigger_else_if | 当前面的 `trigger_if` 或 `trigger_else_if` 的 trigger 不满足且自身 limit 的 trigger 满足时，评估其中的 display_triggers | trigger_if = { limit = { <triggers> } <display_triggers> } trigger_else_if = { limit = { <triggers> } <display_triggers> } |  |
| trigger_if | 当 limit 的 trigger 满足时，评估其中的 display_triggers | trigger_if = { limit = { <triggers> } <display_triggers> } |  |
| variable_list_size | 检查变量列表的大小 | variable_list_size = { name = <variable name> value >= <value> } |  |
| variable_map_size |  | variable_map_size = { name = the name of the global map value >= script value or number } |  |
| weighted_calc_true_if | 若已满足的子 trigger 的权重之和达到指定的数值则返回 true | weighted_calc_true_if = { amount = 10 5 = { <trigger> } 15 = { <trigger> } 7 = { <trigger> } } |  |
| year | 比较游戏的当前年份 | year > 1850 | value |

### 建筑 scope

| Trigger | 说明 | 示例 | 目标 |
|---|---|---|---|
| building_has_goods_shortage | 检查建筑是否缺少其任一投入品 | building_has_goods_shortage = yes/no | boolean |
| can_queue_building_levels | 检查建筑的所有者能否在不触及等级或资源潜力上限的情况下排入指定数量的额外等级 | can_queue_building_levels = number |  |
| cash_reserves_available | 评估一个生产建筑可用的现金储备 | cash_reserves_available > 25000 | value |
| cash_reserves_ratio | 评估一个生产建筑的可用现金储备与其最大值的比率 若建筑没有最大现金储备则返回 1 | cash_reserves_ratio > 0.2 | value |
| country_ownership_fraction | 比较该建筑的等级中被国家持有的比例 | country_ownership_fraction > 0.5 | value |
| earnings | 比较建筑当前每名雇员的年收益 | earnings >= 10 | value |
| fraction_of_levels_owned_by_country | 比较某国或该国投资者持有的建筑总等级比例 | fraction_of_levels_owned_by_country = { target = c:GBR value > 0.5 } | value |
| has_active_production_method | 检查 scope 建筑是否激活了指定的生产方式 | has_active_production_method = key |  |
| has_deployed_units | 检查建筑是否支持任何已被部署到本土总部之外的单位 | has_deployed_units = yes/no | boolean |
| has_employee_slots_filled | 检查某一人口类型的雇员数量是否高于或低于建筑当前可雇佣总量的给定百分比。例如建筑对店主的当前雇佣容量达到了 80%（以 0.8 表示）。 | has_employee_slots_filled = { pop_type = <pop type> percent = <0-1 value> } |  |
| has_failed_hires | 检查建筑上周是否未能雇到人 | has_failed_hires = yes/no | boolean |
| has_modifier | 检查受支持的 scope 是否带有某个限时 modifier | has_modifier = <key> |  |
| is_buildable | 检查建筑是否为可建造 = yes（默认值） | is_buildable = yes/no | boolean |
| is_building_group | 若 scope 是给定类别的建筑则为 true | building_group = building |  |
| is_building_type | 若 scope 是给定类型的建筑则为 true | is_building_type = building |  |
| is_government_funded | 检查建筑是否为政府资助 | is_government_funded = yes/no | boolean |
| is_subsidized | 检查建筑是否正在被补贴 | is_subsidized = yes/no | boolean |
| is_subsistence_building | 检查建筑是否为自给建筑 | is_subsistence_building = yes/no | boolean |
| is_under_construction | 检查建筑是否正在建造中 | is_under_construction = bool | boolean |
| levels_owned_by_country | 比较某国或该国投资者在建筑中持有的等级数量 | levels_owned_by_country = { target = c:GBR value >= 1 } | value |
| occupancy | 评估建筑当前的入住率 | occupancy < 0.25 | value |
| private_ownership_fraction | 比较该建筑的等级中私有持有的比例 | private_ownership_fraction > 0.5 | value |
| self_ownership_fraction | 比较该建筑的等级中由建筑自身持有的比例 | self_ownership_fraction > 0.5 | value |
| weekly_profit | 检查建筑本周获得的利润是否高于或低于给定数值 | weekly_profit >= 20.0 | value |

### 人物 scope

| Trigger | 说明 | 示例 | 目标 |
|---|---|---|---|
| age | 比较人物的年龄 | age > 20 | value |
| can_agitate | 检查 scope 人物能否在目标国家进行鼓动 | can_agitate = <scope/c:TAG> | country |
| character_acceptance | 将 scope 人物在目标国家的接纳度与一个接纳度数值比较 | character_acceptance = { target = c:FRA value > 50 } | value |
| character_supports_political_movement | 检查 scope 人物是否支持某项政治运动 | character_supports_political_movement = yes/no | boolean |
| commander_is_available | 检查指挥官是否空闲 | commander_is_available = bool | boolean |
| commander_rank | 比较指挥官的军衔 | commander_rank > 2 | value |
| could_support_political_movement | 检查人物是否有可能支持某项政治运动 | could_support_political_movement = <scope> |  |
| experience_level | 比较人物的经验等级 | experience_level > 1 | value |
| has_commander_order | 检查 scope 人物是否在执行给定的命令 | has_commander_order = order type key/order type scope |  |
| has_culture | 检查人物的文化 | has_culture = culture scope or character scope |  |
| has_ideology | 检查 scope 人物或利益集团是否拥有某意识形态 |  |  |
| has_military_formation | 检查人物是否拥有一个军事编队 | has_military_formation = bool | boolean |
| has_modifier | 检查受支持的 scope 是否带有某个限时 modifier | has_modifier = <key> |  |
| has_religion | 检查人物的宗教 | has_religion = religion/character scope |  |
| has_role | 检查人物是否拥有特定角色 | has_role = role |  |
| has_role_of_type | 检查人物是否拥有指定原型的角色 | has_role_of_type = archetype |  |
| has_template | 检查人物是否由指定模板生成 | has_template = template_key |  |
| has_trait | 检查人物是否拥有特定特质 | has_trait = trait |  |
| is_adult | 检查人物是否为成年人 | is_adult = bool | boolean |
| is_advancing_on_front | 检查指挥官是否正在某条前线推进 | is_advancing_on_front = <front scope> | front |
| is_attacker_in_battle | 检查指挥官或舰船在某场战斗中是否为进攻方 | is_attacker_in_battle = bool | boolean |
| is_busy | 检查人物是否繁忙 | is_busy = bool | boolean |
| is_character_alive | 检查 scope 人物是否存活 | is_character_alive = bool | boolean |
| is_defender_in_battle | 检查指挥官或舰船在某场战斗中是否为防守方 | is_defender_in_battle = bool | boolean |
| is_female | 检查人物是否为女性 | is_female = bool | boolean |
| is_heir_of_own_country | 检查 scope 人物是否为其所在国家的继承人 | is_heir_of_own_country = yes / no | boolean |
| is_historical | 检查人物是否为历史人物 | is_historical = yes/no | boolean |
| is_immortal | 检查 scope 人物是否不朽 | scope:abbath = { is_immortal = yes } | boolean |
| is_in_battle | 检查指挥官或舰船是否正在交战 | is_in_battle = bool | boolean |
| is_in_exile_pool | 检查 scope 人物是否在流亡者池中 | is_in_exile_pool = yes/no | boolean |
| is_in_void | 检查人物是否处于虚无之中 | is_in_void = bool | boolean |
| is_interest_group_leader | 检查人物是否为其所在利益集团的领袖 | is_interest_group_leader = yes/no | boolean |
| is_interest_group_type | 检查利益集团是否属于某种类型 也可直接用于人物 | is_interest_group_type = x |  |
| is_monarch | 检查人物是否为实行世袭继承制国家的君主 | is_monarch = bool | boolean |
| is_noble | 检查人物是否为贵族 | is_noble = bool | boolean |
| is_on_front | 检查人物或军事编队是否已被分配到某条前线并已抵达 | is_on_front = yes/no | boolean |
| is_ruler_of_any_country | 检查人物是否为任意国家的统治者/国家元首 | is_ruler_of_any_country = bool | boolean |
| is_ruler_of_other_country | 检查人物是否为其所居住国家以外任意国家的统治者/国家元首 | is_ruler_of_other_country = bool | boolean |
| is_ruler_of_own_country | 检查人物是否为其所居住国家的统治者/国家元首 | is_ruler_of_own_country = bool | boolean |
| law_enactment_stance | 比较 scope 人物、运动或利益集团对制定指定法律的立场，与同组当前生效的法律相比较 |  |  |
| law_stance | 比较 scope 人物、运动或利益集团对指定法律的基础立场，忽略同组当前生效的法律 |  |  |
| lifetime_piracy_income | 比较人物一生中的海盗收入 | lifetime_piracy_income >= 1000000 | value |
| loyalty | 比较人物的忠诚度 | loyalty > 1 | value |
| primary_role | 检查人物的主要角色是否为指定角色 | primary_role = role |  |
| prominence | 比较人物的声望 | prominence > 1 | value |
| remaining_career_length | 检查人物剩余的职业生涯长度是否达到一个时长阈值。role 可以是特定的数据库角色、角色类型，或省略以使用距职业生涯结束最远的角色。 | remaining_career_length = { role = general years = 5 } | value |
| role_priority | 比较人物角色的优先级 | role_priority >= 10 | value |
| trait_value | 比较人物的特质总值 | trait_value < experience_level | value |
| was_exiled | 检查 scope 人物是否曾遭流放 | was_exiled = yes/no | boolean |
| years_of_service | 比较指挥官的服役年数 | years_of_service > 1 | value |

### 公司 scope

| Trigger | 说明 | 示例 | 目标 |
|---|---|---|---|
| can_potentially_produce_prestige_goods | 检查 scope 公司是否有潜力生产目标威望商品类型 | can_potentially_produce_prestige_good = pg:prestige_good_generic_clothes |  |
| company_employed_levels | 检查 scope 公司已雇佣等级的数量 | company_employed_levels > 1.5 | value |
| company_global_productivity_comparison | 检查与该公司建筑相匹配的建筑的全球平均生产力，按各类型的持有等级加权 | company_global_productivity_comparison > 1.0 | value |
| company_has_building_type_monopoly | 检查 scope 公司是否垄断了指定的建筑类型 | company_has_building_type_monopoly = bt:building_food_industry | building_type |
| company_has_monopoly | 检查 scope 公司是否拥有任何垄断 | company_has_monopoly = yes | boolean |
| company_is_prosperous | 检查公司是否被视为繁荣 |  | boolean |
| company_owned_levels | 检查 scope 公司持有等级的数量 | company_owned_levels > 1.5 | value |
| company_productivity | 检查 scope 公司的生产力 | company_productivity > 1.0 | value |
| company_prosperity | 检查公司的繁荣度 | company_prosperity > 0 | value |
| is_company_type | 检查 scope 公司是否属于指定类型 | is_company_type = <company_type scope> | company_type |
| is_producing_prestige_goods | 检查 scope 公司是否正在生产威望商品 | is_producing_prestige_goods = yes | boolean |
### 国家 scope

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| additional_war_exhaustion | 比较所在国家从目标外交博弈中的脚本事件累积的额外战争疲惫度 | additional_war_exhaustion = { target = scope:war.diplomatic_play value > 1.0 } | value |
| aggressive_diplomatic_plays_permitted | 若国家独立或被允许发起自己的外交博弈则为真 | aggressive_diplomatic_plays_permitted = bool | boolean |
| ai_ship_value | AI 对一艘船的估值（以英镑计），等于当前模板版本的建造成本乘以 NAI::SHIP_TRANSFER_BASE_VALUE_PER_CONSTRUCTION_POINT | ai_ship_value >= 5000 | value |
| approaching_bureaucracy_shortage | 检查该国的机构最终是否会面临行政力短缺 |  | boolean |
| arable_land_country | 比较*所有*州的可耕地总量 | arable_land_country > 10 | value |
| army_mobilization_option_fraction | 检查一国的陆军中有特定动员选项的单位是否达到一定比例 | scope:country = { army_mobilization_option_fraction = { target = mobilization_option:key value >= 0.2 } } | value |
| army_power_projection | 与一国的总陆军力量投射进行比较 | scope:example_country = { army_power_projection < root.army_power_projection } | value |
| authority | 比较所在国家的可用权威力 |  | value |
| authority_usage | 比较所在国家已消耗的权威力 |  | value |
| average_country_infrastructure | 检查所在国家拥有的所有州的平均基础设施 | average_country_infrastructure = 3 | value |
| average_incorporated_country_infrastructure | 检查所在国家拥有的已整合州的平均基础设施 | average_incorporated_country_infrastructure = 3 | value |
| average_sol_for_culture | 比较该国目标文化的平均生活水平 | average_sol_for_culture = { target = cu:polish value > 10 } | value |
| average_sol_for_primary_cultures | 比较主要文化的平均生活水平 |  | value |
| average_sol_for_religion | 比较该国目标宗教的平均生活水平 | average_sol_for_religion = { target = rel:catholic value > 10 } | value |
| average_sol_for_slaves | 比较被奴役人口的平均生活水平 |  | value |
| bureaucracy | 比较所在国家的可用行政力 |  | value |
| bureaucracy_usage | 比较所在国家已消耗的行政力 |  | value |
| can_afford_diplomatic_action | 检查所在 scope 的国家能否负担指定外交行动（条约或持续性行动）所需的影响力 | can_afford_diplomatic_action = { target = <country scope> type = <diplomatic action key> } |  |
| can_break_diplomatic_pact | 检查与目标国家是否存在指定类型的、可被所在国家撕毁的外交条约 | can_break_diplomatic_pact = { target = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> } |  |
| can_create_diplomatic_pact | 检查与另一国家建立某外交条约是否有效 | can_create_diplomatic_pact = { target = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> } |  |
| can_decrease_autonomy | 检查一个附属国是否能够变为自治程度更低的附属国类型 | can_increase_autonomy = yes | boolean |
| can_establish_company | 检查该国能否建立一家新公司 |  | boolean |
| can_form_nation | 检查目标国家是否有潜力成立一个国家 | can_form_nation = <tag> |  |
| can_have_as_subject | 检查一国能否以特定附属国类型拥有另一国 | can_have_as_subject = { who = <country scope> type = <subject type key> } |  |
| can_have_subjects | 检查该国是否能拥有自己的附属国 |  | boolean |
| can_increase_autonomy | 检查一个附属国是否能够变为自治程度更高的附属国类型 | can_increase_autonomy = yes | boolean |
| can_leave_power_bloc | 检查所在 scope 的国家能否离开当前强权集团（若国家不在强权集团中则返回 false） | can_leave_power_bloc = yes | boolean |
| can_lobbies_target | 检查目标国家是否为所在国家的游说团的有效目标 | can_lobbies_target = <target country scope> | country |
| can_own_autonomy_be_decreased | 检查所在 scope 的国家的自治程度能否被降低 | can_own_autonomy_be_decreased = yes/no | boolean |
| can_research | 若一国能研究某项技术则为真 | can_research = technology |  |
| can_send_diplomatic_action | 检查由所在国家向目标国家发送某外交行动是否有效 | can_send_diplomatic_action = { target = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> } |  |
| can_take_on_scaled_debt | 检查所在 scope 的国家能否从另一国承接一定数量的比例债务 | can_take_on_scaled_debt = { who = <country scope> value = <0-1 value> } |  |
| can_trigger_event | 检查该国能否触发指定事件 | can_trigger_event = key |  |
| check_area | 比较一个对象的区域与另一对象 |  |  |
| construction_queue_duration | 比较所有建造队列中完成建造所需剩余周数（粗略估算）的最大值 | construction_queue_duration < 52 | value |
| construction_queue_government_duration | 比较政府队列中完成建造所需的粗略估算剩余周数 | construction_queue_government_duration < 52 | value |
| construction_queue_num_queued_government_levels | 比较建造队列中政府建造的建筑等级数量 |  | value |
| construction_queue_num_queued_levels | 比较建造队列中的建筑等级数量 |  | value |
| construction_queue_num_queued_private_levels | 比较建造队列中私人建造的建筑等级数量 |  | value |
| construction_queue_private_duration | 比较私人队列中完成建造所需的粗略估算剩余周数 | construction_queue_private_duration < 52 | value |
| country_army_unit_type_fraction | 检查一国是否拥有特定陆军单位类型达到一定比例 | scope:example_formation = { country_military_unit_type_fraction = { target = unit_type:key value >= 0.2 } } | value |
| country_average_cultural_acceptance | 将一国国内某一文化的平均接受度与一个数值进行比较 | country_average_cultural_acceptance = { target = cu:french value >= 50 } | value |
| country_average_religious_acceptance | 将一国国内某一宗教的平均接受度与一个数值进行比较 | country_average_religious_acceptance = { target = rel:catholic value >= 50 } | value |
| country_can_have_mass_migration_to | 检查所在 scope 的国家能否向目标国家进行大规模迁移 | can_have_mass_migration_to = c:country | country |
| country_fervor_primary_culture | 与一国主要文化的最高狂热度进行比较 | country_fervor_primary_culture > 0.2 | value |
| country_has_building_group_levels | 检查一国某建筑组的建筑等级总和 | country_has_building_group_levels = { type = bg_heavy_industry value >= 100 } | value |
| country_has_building_levels | 检查一国的建筑等级总和 | country_has_building_levels >= 10 | value |
| country_has_building_type_levels | 检查一国某建筑类型的建筑等级总和 | country_has_building_type_levels = { target = bt:building_barracks value >= 100 } | value |
| country_has_building_type_monopoly | 检查所在 scope 的国家是否拥有指定建筑类型的垄断 | country_has_building_type_monopoly = bt:building_food_industry | building_type |
| country_has_country_monopoly | 检查所在 scope 的国家是否拥有任何国家垄断 |  | boolean |
| country_has_primary_culture | 检查某一文化是否为该国的主要文化之一 | country_has_primary_culture = <culture> | culture |
| country_has_state_religion | 检查某一宗教是否为该国的国教 | country_has_accepted_religion = <religion> | religion |
| country_innovation | 检查一国每周产出的创新数量 | country_innovation <= 200 | value |
| country_or_subject_owns_entire_state_region | 检查所在 scope 的国家或其任一附属国是否拥有整个指定的州区域 | country_or_subject_owns_entire_state_region = key |  |
| country_rank | 比较一国的政权等级 | country_rank < rank_value:major_power | value |
| country_ship_type_fraction | 检查一国是否拥有特定舰船类型达到一定比例 | scope:example_formation = { country_ship_type_fraction = { target = unit_type:key value >= 0.2 } } | value |
| country_tier | 比较国家 tag 的层级 | country_tier = x |  |
| country_turmoil | 比较该国按人口加权的动荡 | country_turmoil > 0.2 | value |
| cultural_acceptance_base | 将所在 scope 的国家中某一文化因共同文化特质而获得的接受度与一个接受度数值进行比较 | cultural_acceptance_base = { target = cu:french value > 50 } | value |
| culture_percent_country | 检查一国人口中特定文化是否达到一定比例 | scope:example_country = { culture_percent_country = { target = cu:dixie value >= 0.2 } } | value |
| discriminates_religion | 检查所在 scope 的国家是否歧视给定宗教（key） | discriminates_religion = <religion key/scope> | religion |
| economic_dependence | 比较所在 scope 的国家对目标国家的依赖程度。**注意：这是一个开销很大的 trigger** | economic_dependence = { target = scope:other_country value > 2.2 } | value |
| empty_agitator_slots | 检查一国空余的鼓动家槽位数量 | empty_agitator_slots >= 1 | value |
| enacting_any_law | 检查该国是否正在制定任何法律。 | enacting_any_law = bool | boolean |
| enactment_chance | 比较所在 scope 的国家的当前立法通过概率，包括立法修正项带来的数值 |  | value |
| enactment_chance_for_law | 比较所在 scope 的国家对给定法律的立法通过概率，包括立法修正项带来的数值 | enactment_chance_for_law = { target = scope:my_lawtype value > 0.2 } | value |
| enactment_chance_for_law_without_enactment_modifier | 比较所在 scope 的国家对给定法律的立法通过概率，不包括立法修正项带来的数值 | enactment_chance_for_law_without_enactment_modifier = { target = scope:my_lawtype value > 0.2 } | value |
| enactment_chance_without_enactment_modifier | 比较所在 scope 的国家的当前立法通过概率，不包括立法修正项带来的数值 |  | value |
| enactment_phase | 比较所在 scope 的国家的当前立法阶段。 |  | value |
| enactment_setback_count | 比较所在 scope 的国家的当前立法受挫次数。 |  | value |
| enemy_contested_wargoals | 判定战争中敌方目前正在争夺的战争目标的比例 | enemy_contested_wargoals = { target = scope:war value > 0.4 } | value |
| enemy_occupation | 判定一个国家的（加权）敌方占领分数 | enemy_occupation > 0.2 | value |
| expanding_institution | 检查该机构是否正在扩张 | expanding_institution = <scope/key> |  |
| gdp_ownership_ratio | 比较指定国家在所在 scope 的国家中拥有的 GDP 比例 | gdp_ownership_ratio = { target = scope:owner_country value > 0.1 } | value |
| gdp_per_capita_ranking | 比较一国的人均 GDP 排名（名次） | gdp_per_capita_ranking > 42 | value |
| global_country_ranking | 比较一国的政权等级排名（名次） | global_country_ranking > 42 | value |
| gold_reserves | 该国是否拥有所需的黄金储备 | gold_reserves > 500 | value |
| gold_reserves_limit | 比较该国的黄金储备上限 | gold_reserves > gold_reserves_limit | value |
| goods_production_rank | 与一国某商品的生产排行榜名次进行比较 | "goods_production_rank(g:luxury_clothes)" < 10 | value |
| government_legitimacy | 比较合法性 |  | value |
| government_transfer_of_power | 检查该国政府的权力移交方式 | government_transfer_of_power = key | value |
| government_wage_level | 比较所在 scope 的国家的政府工资水平。`very_low, low, medium, high, very_high`；返回数值与 government_wage_level_value trigger 相同 | government_wage_level = <level_term> | value |
| government_wage_level_value | 比较所在 scope 的国家的政府工资水平数值。`0, 1, 2, 3, 4` | government_wage_level_value = <level_num> | value |
| has_active_peace_deal | 若该国处于一场已有提议和平协议的战争中则为真 | has_active_peace_deal = bool | boolean |
| has_any_law_commitment | 检查一国是否有制定任何法律的承诺 | has_any_law_commitment = yes | boolean |
| has_any_naval_only_hostilities | 检查该国是否与任何未处于战争状态的国家存在海上敌对 | has_any_naval_only_hostilities = yes | boolean |
| has_any_secessionists_broken_out | 检查该国是否已有分离主义者爆发 |  | boolean |
| has_any_secessionists_growing | 检查该国是否有任何正在壮大的分离主义者 |  | boolean |
| has_any_strait_control | 检查所在 scope 的国家是否拥有带海军要塞的海峡省份 | has_any_strait_control = yes | boolean |
| has_any_strait_province | 检查所在 scope 的国家是否拥有任何海峡省份 | has_any_strait_province = yes | boolean |
| has_any_subventions_on | 检查所在 scope 的国家是否对某商品启用了任何等级的补贴 | scope:country = { has_any_subventions_on = <goods scope> } | goods |
| has_any_tariffs_on | 检查所在 scope 的国家是否对某商品设置了任何等级的关税 | scope:country = { has_any_tariffs_on = <goods scope> } | goods |
| has_attitude | 检查所在 scope 的国家对另一国家是否有特定态度 | has_attitude = { who = <country scope> attitude = <attitude key> } |  |
| has_building | 若一个州/市场/州区域/国家拥有某建筑类型则为真 | has_building = building |  |
| has_civil_war_from_movement_type | 检查一国是否正处于由特定运动类型引发的内战 | has_civil_war_from_movement_type = <political_movement_type scope> | political_movement_type |
| has_claim | 检查所在 scope 的国家是否对某州/州区域/国家有领土主张 | has_claim = <scope> |  |
| has_company | 检查所在 scope 的国家中是否存在指定类型的公司 | has_company = <company_type scope> | company_type |
| has_completed_subgoal | 检查所在 scope 的国家是否已完成某个子目标 | has_completed_subgoal = subgoal_key |  |
| has_consumption_tax | 检查该国是否正在对目标商品征收消费税。 | c:FRA = { has_consumption_tax = <goods scope> } | goods |
| has_convoys_being_sunk | 检查该国的船队护航是否正因护航船队袭击而损失 |  | boolean |
| has_diplomatic_pact | 检查两国之间是否存在指定类型的有效外交条约 | has_diplomatic_pact = { who = <country scope> type = <diplomatic action key> is_initiator = yes/no } is_initiator 为可选参数，用于检查所在 scope 的国家是否为该条约的最初发起方/目标方 |  |
| has_diplomatic_relevance | 检查目标国家对所在 scope 的国家是否具有外交相关性 | has_diplomatic_relevance = <scope> | country |
| has_diplomats_expelled | 检查所在 scope 的国家最近是否驱逐了 event target 的外交官 | has_diplomats_expelled = country | country |
| has_famine | 检查一个州或国家是否发生饥荒 | has_famine = yes/no | boolean |
| has_free_government_reform | 检查该国是否拥有一次免费（不产生激进派的）政府改革 | has_free_government_reform = <yes/no> | boolean |
| has_global_highest_gdp | 检查所在 scope 的国家是否拥有最高 GDP | has_global_highest_gdp = yes/no | boolean |
| has_global_highest_innovation | 检查所在 scope 的国家是否拥有最高的每周创新 | has_global_highest_innovation = yes/no | boolean |
| has_government_clout | 该国政府的政治力量总和是否达到所需数值 |  | value |
| has_government_type | 该国的政府类型是否如指定 | has_government_type = key |  |
| has_healthy_economy | 检查该国经济是否健康 |  | boolean |
| has_inactive_journal_entry | 检查该国是否拥有至少一个指定类型的未激活日志条目 | has_inactive_journal_entry = key |  |
| has_institution | 检查所在 scope 的国家是否拥有特定类型的机构 | has_institution = <scope/key> |  |
| has_insurrectionary_interest_groups | 检查该国是否有处于叛乱状态的利益集团 |  | boolean |
| has_interest_marker_in_region | 若所在 scope 的国家在目标区域拥有利益标记则为真 | has_interest_marker_in_region = region scope/tag |  |
| has_journal_entry | 检查该国是否拥有至少一个指定类型的活跃日志条目 | has_journal_entry = key |  |
| has_law | 检查一国是否已激活某项法律 |  | law_type |
| has_law_commitment | 检查一国是否有制定某项法律的承诺 |  | law_type |
| has_law_imposition_rights | 检查所在 scope 的国家是否拥有必要许可，可要求另一国制定某项法律 | has_law_imposition_rights = { target_country = <country scope> type = <law type scope> } |  |
| has_law_or_variant | 检查一国是否已激活某项法律或其变体法律之一 |  | law_type |
| has_modifier | 检查一个受支持的 scope 是否拥有某个限时 modifier | has_modifier = <key> |  |
| has_objective | 检查所在 scope 的国家是否拥有某个目标类型 | has_objective = objective_type_key |  |
| has_overlapping_interests | 检查所在 scope 的国家是否与目标国家的任一利益存在重叠的利益标记 | has_overlapping_interests = <scope> | country |
| has_port_country | 检查所在 scope 的国家是否拥有至少一个港口 | has_port_country = yes/no | boolean |
| has_possible_decisions | 检查一国是否有任何可用的决策 | has_possible_decisions = yes | boolean |
| has_potential_to_form_country | 检查目标国家是否有朝一日能够成立一个国家 | has_potential_to_form_country = <tag> |  |
| has_power_struggle | 检查所在 scope 的强权集团是否正处于权力斗争 | has_power_struggle = yes/no | boolean |
| has_region_stance | 检查所在 scope 的国家的 AI 对某战略区域是否持有指定立场 | region_stance = { region = sr:some_region stance = <conquer_region> } |  |
| has_researchable_technology | 检查该国是否还有任何可研究的技术。 |  | boolean |
| has_revolution | 检查该国是否发生革命起义 |  | boolean |
| has_ruling_interest_group | 该国政府是否包含指定利益集团 |  |  |
| has_ruling_interest_group_count | 该国政府是否由指定数量的利益集团组成 |  | value |
| has_secret_goal | 检查所在 scope 的国家对另一国家是否有特定秘密目标 | has_secret_goal = { who = <country scope> secret_goal = <secret_goal key> } |  |
| has_social_hierarchy | 检查所在 scope 的国家是否已采用特定的社会等级制度 | has_social_hierarchy = <key> |  |
| has_state_in_state_region | 检查国家是否在该州区域中拥有一个州 | has_state_in_state_region = key |  |
| has_strategic_adjacency | 检查所在 scope 的国家是否与目标州/国家存在战略毗邻（直接/沿海/战争目标毗邻） | has_strategic_adjacency = <scope> |  |
| has_strategic_land_adjacency | 检查所在 scope 的国家是否与目标州/国家存在战略毗邻（仅限直接陆上接壤或战争目标毗邻） | has_strategic_adjacency = <scope> |  |
| has_strategic_region_interest_tier | 检查所在 scope 的国家在特定战略区域中的利益等级名次 | has_strategic_region_interest_tier = { strategic_region = sr:target_region value >= 3 } |  |
| has_strategy | 检查所在 scope 的国家是否有特定的 AI 策略 | has_strategy = <key> |  |
| has_subject_relation_with | 检查所在 scope 的国家是否为 event target 的附属国或宗主国 | has_subject_relation_with = country | country |
| has_sufficient_construction_capacity_for_investment | 检查国家是否拥有足够的建造能力来用尽其所有流入的投资池资金。 |  | boolean |
| has_technology_progress | 该国是否拥有某项技术所需的进度 | has_technology_progress = { technology = <technology key> progress = <0-1 value> } | value |
| has_technology_researched | 若一国已研究某项技术则为真 | has_technology_researched = <scope/key> |  |
| has_treaty_port_in_market | 检查所在 scope 的国家是否在目标市场中拥有条约港 | c:POR = { has_treaty_port_in_market = c:CHI.market } | market |
| has_truce_with | 检查一国是否与另一目标国家处于休战 | has_truce_with = c:GBR | country |
| has_war_with | 检查所在 scope 的国家是否与 event target 处于战争状态 | has_war_with = country | country |
| has_wasted_construction | 检查国家是否正在浪费其任何已产出的建造。 |  | boolean |
| highest_overlapping_interest_tier | 比较两国均有利益的各战略区域中（所在 scope 的国家）的最高利益等级名次。 | highest_overlapping_interest_tier = { target = c:GBR value >= 2 } | value |
| highest_secession_progress | 比较一个国家中任何分离运动的最高分离进度 | highest_secession_progress > 0.7 | value |
| in_default | 检查该国当前是否处于违约状态 |  | boolean |
| in_election_campaign | 检查该国是否处于竞选活动期间 | in_election_campaign = <yes/no> | boolean |
| influence | 比较所在 scope 的国家的可用影响力 |  | value |
| influence_usage | 比较所在 scope 的国家已消耗的影响力 |  | value |
| institution_investment_level | 比较一个机构的投入等级 | institution_investment_level = { institution = <key> value = <comparator value> } | value |
| investment_pool | 该国的投资池中是否拥有该数量的资金 | investment_pool > 1000 | value |
| investment_pool_gross_income | 该国的投资池是否拥有该数量的总收入（支出前的收入） | investment_pool_gross_income > 1000 | value |
| investment_pool_net_income | 该国的投资池是否拥有该数量的净收入（支出后的收入） | investment_pool_net_income > 1000 | value |
| is_adjacent_to_country | 检查所在 scope 的国家是否与目标国家接壤 | is_adjacent_to_country = <scope> | country |
| is_adjacent_to_state | 检查所在 scope 的国家是否与目标州接壤 | is_adjacent_to_state = <state scope> | state |
| is_ai | 若国家 scope 由 AI 控制则为真 | is_ai = bool | boolean |
| is_at_war | 检查该国是否处于战争状态 |  | boolean |
| is_banning_goods | 检查一国是否正在禁运某商品 | is_banning_goods = <goods key/scope> |  |
| is_considered_adjacent_due_to_wargoals | 检查所在 scope 的国家是否因在已承诺的外交博弈中拥有与目标国家毗邻的战争目标而被视为与目标国家毗邻 | is_considered_adjacent_due_to_wargoals = <target country scope> | country |
| is_construction_paused | 检查一个州的建造是否已暂停。 |  | boolean |
| is_country_alive | 检查 scope 国家是否存续，即在地图上是否至少拥有一个州并且可以与之互动 | is_country_alive = yes/no | boolean |
| is_country_type | 检查国家的类型 | is_country_type = country type |  |
| is_diplomatic_play_ally_of | 检查 scope 国家是否与 event target 处于同一场外交博弈（Diplomatic play）中 | is_diplomatic_play_ally_of = country | country |
| is_diplomatic_play_committed_participant | 若国家是任意外交博弈中立场已定的参与者则为真 | is_diplomatic_play_participant = bool | boolean |
| is_diplomatic_play_enemy_of | 检查 scope 国家是否在一场针对 event target 的外交博弈中与其敌对 | is_diplomatic_play_enemy_of = country | country |
| is_diplomatic_play_initiator | 若国家是任意外交博弈的发起者则为真 | is_diplomatic_play_initiator = bool | boolean |
| is_diplomatic_play_involved_with | 检查 scope 国家是否卷入与 event target 相同的外交博弈 | is_diplomatic_play_involved_with = country | country |
| is_diplomatic_play_participant_with | 检查 scope 国家是否是与 event target 相同的外交博弈中立场已定的参与者 | is_diplomatic_play_participant_with = country | country |
| is_diplomatic_play_target | 若国家是任意外交博弈的目标则为真 | is_diplomatic_play_target = bool | boolean |
| is_diplomatic_play_undecided_participant | 若国家是任意外交博弈中立场未定的参与者则为真 | is_diplomatic_play_participant = bool | boolean |
| is_direct_subject_of | 检查 scope 国家是否是 event target 的直接附属国（并非附属国的附属国） | is_direct_subject_of = country | country |
| is_enacting_law | 检查 scope 国家是否正在制定某类特定法律。 | is_enacting_law = law_type:law_conscription | law_type |
| is_expanding_institution | 是否正在扩张一个机构（Institution） | is_expanding_institution = <yes>/<no> | boolean |
| is_forced_to_join_plays | 检查 scope 国家是否被迫加入目标国家的外交博弈 | is_forced_to_join_plays = c:country | country |
| is_home_country_for | 检查一个国家是否是目标国家的母国 |  | country |
| is_immune_to_revolutions | 检查该国是否已通过 set_immune_to_revolutions 被设置为对革命免疫。警告：这不会检查该国是否因其他原因（例如自身就是革命国家）而天然对革命免疫，只检查 set_immune_to_revolutions 的效果。 is_immune_to_revolutions = yes/no | boolean |
| is_in_customs_union | 检查该国是否属于某个关税同盟 |  | boolean |
| is_in_customs_union_with | 检查该国是否与 scope 国家处于同一关税同盟 | is_in_customs_union_with = c:FRA | country |
| is_in_power_bloc | 检查该国是否属于某个强权集团（Power Bloc） | is_in_power_bloc = yes/no | boolean |
| is_in_same_power_bloc | 检查 scope 国家是否与目标 scope 国家处于同一强权集团 | is_in_same_power_bloc = c:GBR | country |
| is_in_war_together | 检查 scope 国家是否与 event target 处于战争中的同一方 | is_in_war_together = country | country |
| is_indirect_subject_of | 检查 scope 国家是否是 event target 的间接附属国（附属国的附属国） | is_indirect_subject_of = country | country |
| is_insurrectionary | 检查国家、运动或利益集团是否处于起义状态 |  | boolean |
| is_junior_in_customs_union | 若国家是关税同盟中的次级成员则为真 | is_junior_in_customs_union = bool | boolean |
| is_local_player | 若国家 scope 是本地玩家则为真 | is_local_player = bool | boolean |
| is_losing_power_rank | 检查该国是否正在经历等级地位下降的过程 |  | boolean |
| is_market_reachable_for_trade | 检查 scope 国家处于贸易目的能否到达指定的市场 scope | is_market_reachable_for_trade = scope:my_market_scope | market |
| is_mass_migration_origin | 检查 scope 国家是否是大规模迁移的来源地 | is_mass_migration_origin = yes | boolean |
| is_mass_migration_origin_of_culture | 检查 scope 国家是否是特定文化大规模迁移的来源地 | is_mass_migration_origin_of_culture = cu:example_culture | culture |
| is_owed_obligation_by | 检查 scope 国家是否持有目标国家所欠的一项义务（Obligation） | is_owed_obligation_by = c:FRA | country |
| is_player | 若国家 scope 是玩家则为真 | is_player = bool | boolean |
| is_power_bloc_leader | 检查该国是否是某个强权集团的领袖 | is_power_bloc_leader = yes/no | boolean |
| is_researching_technology | 检查该国是否正在积极研究某项技术 | is_researching_technology = <scope/key/any> |  |
| is_researching_technology_category | 检查该国是否正在积极研究某个技术类别 | is_researching_technology_category = <key/any> |  |
| is_revolutionary | 检查国家、运动或利益集团是否是革命性的 |  | boolean |
| is_secessionist | 检查国家、运动或利益集团是否是分裂主义性的 |  | boolean |
| is_subject | 若国家是附属国则为真 | is_subject = bool | boolean |
| is_subject_of | 检查 scope 国家是否是 event target 的附属国（或附属国的附属国） | is_subject_of = country | country |
| is_subject_type | 检查该国的附属国类型 | is_subject_type = subject type |  |
| is_supporting_unification_candidate | 检查 scope 国家是否支持某项特定国家统一（country formation）的统一候选国 | is_supporting_unification_candidate = { who = c:PRU country_formation = GER } |  |
| is_taxing_goods | 检查一个国家是否正在对某商品征税 | has_embargo = <goods key/scope> |  |
| is_unification_candidate | 检查 scope 国家是否是某个国家 tag 的统一候选国 | is_unification_candidate = GER |  |
| is_violating_sovereignty_of | 检查 scope 国家是否正在侵犯目标国家的主权 | is_violating_sovereignty_of = c:GBR | country |
| isolated_states | 比较孤立州的数量 |  | value |
| leading_producer_of | 检查国家是否是某种特定商品的最大生产国 | leading_producer_of = g:luxury_clothes | goods |
| leads_customs_union | 检查是否有其他国家属于该国的关税同盟 | leads_customs_union = bool | boolean |
| liberty_desire | 比较 scope 国家独立倾向（Liberty desire）数值的 trigger。 | liberty_desire > 50 | value |
| liberty_desire_weekly_progress | 比较 scope 国家每周独立倾向进展数值的 trigger。 | liberty_desire_weekly_progress > 0 | value |
| liberty_desire_weekly_progress_from_support_independence | 比较 scope 国家因独立受到支持而获得的每周独立倾向进展数值的 trigger。 | liberty_desire_weekly_progress_from_support_independence > 0 | value |
| literacy_rate | 检查一个人口、州或国家是否拥有一定的识字率 | literacy = value | value |
| loyalist_fraction | 比较州或国家中人口里忠诚派的比例，除 value 外所有参数均为可选 | loyalist_fraction = { value = <script_value> pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> } | value |
| max_law_enactment_setbacks | 与国家在法律制定失败前可遭受的最大挫折次数进行比较 |  | value |
| max_num_companies | scope 国家被允许拥有的公司数量上限 | num_num_companies > 0 | value |
| military_ship_maintenance_fulfillment | 比较国家的军用舰船维护满足比率 | military_ship_maintenance_fulfillment = <value> | value |
| military_wage_level | 比较 scope 国家的军队工资等级。`very_low, low, medium, high, very_high`；返回与 military_wage_level_value trigger 相同的数值 | military_wage_level = <level_term> | value |
| military_wage_level_value | 比较 scope 国家的军队工资等级数值。`0, 1, 2, 3, 4` | military_wage_level_value = <level_num> | value |
| nationalization_cost | 比较 scope 国家内由目标国家的政府或人口所拥有的全部建筑国有化的总成本 | nationalization_cost = { target = scope:other_country value > 100000 } | value |
| naval_power_projection | 与国家的海军总力量投射进行比较 | scope:example_country = { naval_power_projection < root.naval_power_projection } | value |
| neighbors_any_power_bloc | 检查 scope 国家是否与任意强权集团相邻。注意：scope 国家不被视为与其自身所属强权集团（若有）相邻 | neighbors_any_power_bloc = yes/no | boolean |
| neighbors_member_of_same_power_bloc | 检查 scope 国家是否与属于同一强权集团的其他任意国家相邻 | neighbors_member_of_same_power_bloc = yes/no | boolean |
| neighbors_power_bloc | 检查 scope 国家是否与目标强权集团相邻。注意：scope 国家不被视为与其自身所属强权集团（若有）相邻 | neighbors_power_bloc = c:PRU.power_bloc | power_bloc |
| num_companies | scope 国家拥有多少公司 | num_companies > 0 | value |
| num_diplomatic_pacts | 与国家指定类型的外交协约数量进行比较 | num_diplomatic_pacts = { type = <key> value < 10 } | value |
| num_investments_of_type | 检查 scope 国家在其本国之外拥有的指定类型建筑等级数量。 | num_investments_of_type = { type = building_oil_rig value > 5 } | value |
| num_political_lobbies | 与 scope 国家或利益集团中的政治游说团数量进行比较 | num_political_lobbies > 0 | value |
| num_subjects | 比较 scope 国家的附属国数量 | num_subjects = <value> | value |
| num_taxed_goods | 比较 scope 国家征收消费税的商品数量 | num_taxed_goods = <value> | value |
| number_of_claims | 该国对外国州拥有的主张数量 | number_of_claims > 0 | value |
| number_of_possible_decisions | 一个国家可以采取的可能决策数量 | number_of_possible_decisions > 0 | value |
| overlord_can_decrease_subject_autonomy | 检查宗主国（Overlord）是否能够降低附属国的自治度 | overlord_can_decrease_subject_autonomy = bool | boolean |
| owes_obligation_to | 检查 scope 国家是否欠 event target 一项义务 | owes_obligation_to = country | country |
| owns_entire_state_region | 检查国家是否拥有整个地区 | owns_entire_state_region = key |  |
| owns_treaty_port_in | 该国是否在指定州地区拥有条约港（Treaty port） | owns_treaty_port_in = key |  |
| play_participant_has_war_goal_of_type_against | 检查 scope 国家在任意外交博弈中是否持有针对特定国家的特定类型战争目标（War goal） | play_participant_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } |  |
| play_side_has_war_goal_of_type_against | 检查在任意外交博弈中与 scope 国家同属一方的任意国家是否持有针对特定国家的特定类型战争目标 | play_side_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } |  |
| political_strength_share | 检查某个人口类型、宗教或文化在国家或州中的政治力量份额。必须且只能指定 pop_type、religion 或 culture 中的一项。 | political_strength_share = { pop_type/religion/culture = <key/scope> value <compare operator> <value> } | value |
| politically_involved_ratio | 比较国家中参与政治的人口的百分比 | politically_involved_ratio > 0.25 | value |
| pop_type_percent_country | 检查 scope 国家是否有 <percent> 比例的人口属于指定的人口类型 | scope:example_country = { pop_type_percent_country = { pop_type = <pop_type> percent <compare operator (<,>,= and so on)> <percent> } } | value |
| potential_diplomatic_play_power_ratio | 检查在一场潜在外交博弈中 scope 国家一方与目标国家一方之间的预期实力比 | 尝试预测相关参与者将（如果有的话）站在哪一方，因此不只是检查“起始实力” potential_diplomatic_play_power_ratio = { type = dp_open_market target = c:BEL state = c:BEL.capital value > 1.0 } state 与 type 为可选，默认为目标国首都上的 dp_open_market | value |
| potential_income | 比较国家的潜在收入（每周收入加上税收流失） | potential_income > 1000 | value |
| power_bloc_share_gdp | 比较 scope 国家的 GDP 相对其强权集团所有当前成员的份额，若不属于强权集团则返回 -1 | power_bloc_share_gdp > 0.2 | value |
| power_bloc_share_gdp_with | 比较 scope 国家的 GDP 相对其强权集团所有成员加上一个额外国家的份额，若不属于强权集团则返回 -1 | "power_bloc_share_gdp_with(scope:country) > 0.2" | value |
| power_bloc_share_gdp_without | 比较 scope 国家的 GDP 相对其强权集团所有成员减去其中一员的份额，若不属于强权集团则返回 -1 | "power_bloc_share_gdp_without(scope:country) > 0.2" | value |
| power_bloc_share_power_projection | 比较 scope 国家的力量投射相对其强权集团所有成员的份额，若不属于强权集团则返回 -1 | power_bloc_share_power_projection > 0.2 | value |
| power_bloc_share_power_projection_with | 比较 scope 国家的力量投射相对其强权集团所有成员加上一个额外国家的份额，若不属于强权集团则返回 -1 | "power_bloc_share_power_projection_with(scope:country) > 0.2" | value |
| power_bloc_share_power_projection_without | 比较 scope 国家的力量投射相对其强权集团所有成员减去其中一员的份额，若不属于强权集团则返回 -1 | "power_bloc_share_power_projection_without(scope:country) > 0.2" | value |
| power_bloc_share_prestige | 比较 scope 国家的威望相对其强权集团所有成员的份额，若不属于强权集团则返回 -1 | power_bloc_share_prestige > 0.2 | value |
| power_bloc_share_prestige_with | 比较 scope 国家的威望相对其强权集团所有成员加上一个额外国家的份额，若不属于强权集团则返回 -1 | "power_bloc_share_prestige_with(scope:country) > 0.2" | value |
| power_bloc_share_prestige_without | 比较 scope 国家的威望相对其强权集团所有成员减去其中一员的份额，若不属于强权集团则返回 -1 | "power_bloc_share_prestige_without(scope:country) > 0.2" | value |
| prestige | 比较威望 |  | value |
| primary_cultures_percent_country | 检查一个国家的人口中有一定比例属于该国的主流文化 | scope:example_country = { primary_cultures_percent_country >= 0.2 } | value |
| produced_authority | 比较 scope 国家产出的统治力 |  | value |
| produced_bureaucracy | 比较 scope 国家产出的行政力 |  | value |
| produced_influence | 比较 scope 国家产出的影响力 |  | value |
| radical_fraction | 比较州或国家中人口里激进派的比例，除 value 外所有参数均为可选 | radical_fraction = { value = <script_value> pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> } | value |
| radical_population_fraction | 比较给定国家中激进派人口占人口的比例 | radical_population_fraction > 0.2 | value |
| region_score | 比较 scope 国家针对指定战略区域的 AI 策略地区评分汇总。若国家由玩家控制则返回 0 | region_score = { strategic_region = sr:region_key value >= 300 } "region_score(sr:region_key)" >= 300 | value |
| relative_authority | 比较 scope 国家统治力的未使用比例 |  | value |
| relative_bureaucracy | 比较 scope 国家行政力的未使用比例 |  | value |
| relative_influence | 比较 scope 国家影响力的未使用比例 |  | value |
| religion_percent_country | 检查一个国家的人口中有一定比例属于特定宗教 | scope:example_country = { religion_percent_country = { target = rel:catholic value <= 0.8 } } | value |
| ruler_can_have_command | 检查国家的政体是否允许其统治者（Ruler）担任指挥 | ruler_can_have_command = yes/no | boolean |
| scaled_debt | 将数值与国家相对于债务上限的债务进行比较 | scaled_debt = value | value |
| scaled_gold_reserves | 将数值与国家相对于储备上限的黄金储备进行比较 | scaled_gold_reserves = value | value |
| ship_modification_market_demand_ratio | 目标舰船改装所需建造商品的按商品权重计算的买/卖比率，以国家 scope 的市场为基准进行评估。 | "ship_modification_market_demand_ratio(scope:ship_modification_type) > 1.25" | value |
| should_set_wargoal | 检查该国在其参与的任意外交博弈中是否缺少主要战争目标 |  | boolean |
| shrinking_institution | 检查机构是否正在缩减 | expanding_institution = <scope/key> |  |
| size_weighted_lost_battles_fraction | 判定目标国家在目标战争中失败战斗的比例，按战争中所有战斗的人力规模加权 | size_weighted_lost_battles_fraction = { target = scope:war value > 0.3 } add = "size_weighted_lost_battles_fraction(scope:war)" | value |
| sol_ranking | 比较一个国家的生活水平排名（名次） | sol_ranking > 42 | value |
| subject_can_increase_autonomy | 检查附属国是否能够提高其自治度 | subject_can_increase_autonomy = bool | boolean |
| supply_network_strength | 比较该国的补给网络强度（可以超过 1） | supply_network_strength > 1.1 | value |
| supply_ship_maintenance_fulfillment | 比较国家的补给舰船维护满足比率 | supply_ship_maintenance_fulfillment < 1 | value |
| taking_loans | 检查该国当前是否处于每周赤字并正在借贷以弥补 |  | boolean |
| tax_level | 比较 scope 国家的总体税收等级。`very_low, low, medium, high, very_high`；返回与 tax_level_value trigger 相同的数值 | tax_level = <level_term> | value |
| tax_level_value | 比较 scope 国家总体税收等级的整数值。`0, 1, 2, 3, 4` | income_tax_level_value = <level_num> | value |
| tax_waste | 比较该国的税收流失 | tax_waste > 100 | value |
| tenure_in_current_power_bloc_days | 比较 scope 国家成为其当前强权集团成员的天数 | tenure_in_current_power_bloc_days > 720 | value |
| tenure_in_current_power_bloc_months | 比较 scope 国家成为其当前强权集团成员的（整）月数 | tenure_in_current_power_bloc_months > 20 | value |
| tenure_in_current_power_bloc_weeks | 比较 scope 国家成为其当前强权集团成员的（整）周数 | tenure_in_current_power_bloc_weeks > 12 | value |
| tenure_in_current_power_bloc_years | 比较 scope 国家成为其当前强权集团成员的（整）年数 | tenure_in_current_power_bloc_years > 5 | value |
| total_population | 比较给定国家的总人口 | total_population > 100000 | value |
| total_population_including_subjects | 比较 scope 国家及其附属国的总人口 | total_population_including_subjects > 40000000 | value |
| total_population_including_subjects_share | 比较 scope 国家及其附属国总人口占全球人口的比例 | total_population_including_subjects_share > 0.4 | value |
| total_population_share | 比较给定国家总人口占全球人口的比例 | total_population_share > 0.02 | value |
| transfer_money_gross_income | 该国从资金转移条约中获得的毛收入（支出前的收入）是否达到该数额 | transfer_money_gross_income > 1000 | value |
| transfer_money_net_income | 该国从资金转移条约中获得的净收入（支出后的收入）是否达到该数额 | transfer_money_net_income > 1000 | value |
| war_participant_has_war_goal_of_type_against | 检查 scope 国家在任意战争中是否持有针对特定国家的特定类型战争目标 | war_participant_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } |  |
| war_side_has_war_goal_of_type_against | 检查在任意战争中与 scope 国家同属一方的任意国家是否持有针对特定国家的特定类型战争目标 | war_side_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } |  |
| was_formed_from | 检查一个被成立的国家此前是否具有特定的定义 | was_formed_from = <tag> |  |
| wealth_share | 检查某个人口类型、宗教或文化在国家或州中的财富政治力量份额。必须且只能指定 pop_type、religion 或 culture 中的一项。 | wealth_share = { pop_type/religion/culture = <key/scope> value <compare operator> <value> } | value |
| would_accept_diplomatic_action | 检查一个国家是否会接受另一个国家提议的外交行动 | would_accept_diplomatic_action = { actor = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> modify_acceptance = <script value, optional> } 若设置了 modify_acceptance，其将被加到对方的接受分数上，以便检查对方是否会在附带义务等条件下接受 |  |
### 文化（Culture）scope

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| culture_can_have_mass_migration_to_country | 检查 scope 文化是否能向目标国家进行大规模迁移 | can_have_mass_migration_to_country = c:country | country |
| culture_current_fervor | 比较给定文化的当前热度 | culture_current_fervor > 0.2 | value |
| culture_has_community_in_state | 检查 scope 文化是否在某州拥有文化社区 | culture_has_community_in_state = <state> |  |
| culture_has_national_awakening | 检查 scope 文化是否有正在进行中的民族觉醒 | culture_has_national_awakening = yes / no | boolean |
| culture_national_awakening_occurred | 检查 scope 文化是否曾经启动过民族觉醒 | culture_national_awakening_occurred = yes / no | boolean |
| culture_secession_progress | 检查该文化在某国中走向分裂的进度百分比。若该文化没有活跃的分裂运动则为 0 | culture_secession_progress = { target = scope:example_country value > 0.5 } | value |
| culture_target_fervor | 比较给定文化的目标热度 | culture_target_fervor > 0.2 | value |
| has_cultural_obsession | 检查一个文化是否痴迷于某种商品 | has_cultural_obsession = <goods key> |  |
| has_culture_graphics | 检查一个文化是否使用某种 culture_graphics | has_culture_graphics = <culture graphics key> |  |
| has_discrimination_trait | 检查 scope 文化或宗教是否具有给定的歧视特质 | has_trait = trait |  |
| has_homeland | 检查 scope 文化在目标州或州区域是否拥有家园 | has_homeland = state/state region |  |
| is_primary_culture_of | 检查该文化是否是某国的任一主流文化 | is_primary_culture_of = <country> | country |
| shares_heritage_trait_group_with_any_primary_culture | 检查该文化是否与某国的任一主流文化共享任一标记为“heritage”（传承）的特质组 | shares_heritage_trait_group_with_any_primary_culture = <country> | country |
| shares_heritage_trait_group_with_culture | 检查该文化是否与另一个文化共享任一标记为“heritage”的特质组 | shares_heritage_trait_group_with_culture = <culture> | culture |
| shares_heritage_trait_group_with_state_religion | 检查该宗教是否与某国的国教共享任一传承特质组 | shares_heritage_trait_group_with_state_religion = <country> | country |
| shares_heritage_trait_with_any_primary_culture | 检查该文化是否与某国的任一主流文化共享任一标记为“heritage”的特质 | shares_heritage_trait_with_any_primary_culture = <country> | country |
| shares_heritage_trait_with_culture | 检查该文化是否与另一个文化共享任一标记为“heritage”的特质 | shares_heritage_trait_with_culture = <culture> | culture |
| shares_language_trait_group_with_any_primary_culture | 检查该文化是否与某国的任一主流文化共享任一标记为“language”（语言）的特质组 | shares_language_trait_group_with_any_primary_culture = <country> | country |
| shares_language_trait_group_with_culture | 检查该文化是否与另一个文化共享任一标记为“language”的特质组 | shares_language_trait_group_with_culture = <culture> | culture |
| shares_language_trait_with_any_primary_culture | 检查该文化是否与某国的任一主流文化共享任一标记为“language”的特质 | shares_language_trait_with_any_primary_culture = <country> | country |
| shares_language_trait_with_culture | 检查该文化是否与另一个文化共享任一标记为“language”的特质 | shares_language_trait_with_culture = <culture> | culture |
| shares_tradition_trait_with_any_primary_culture | 检查该文化是否与某国的任一主流文化共享任一标记为“tradition”（传统）的特质 | shares_language_trait_with_any_primary_culture = <country> | country |
| shares_tradition_trait_with_culture | 检查该文化是否与另一个文化共享任一标记为“tradition”的特质 | shares_tradition_trait_with_culture = <culture> | culture |

### 外交博弈（Diplomatic play）scope

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| escalation | 检查紧张升级是否已超过某个阈值 | escalation > -58 | value |
| has_play_goal | 检查外交博弈是否拥有某种战争目标类型 | has_play_goal = return_state |  |
| initiator_is | 检查外交博弈的发起者是谁 | initiator_is = country | country |
| is_diplomatic_play_type | 检查外交博弈是否属于某种类型 | is_diplomatic_play_type = play type |  |
| is_war | 若外交博弈已升级为战争则为真 | is_war = bool | boolean |
| target_is | 检查外交博弈的目标是谁 | target_is = country | country |

### 利益集团（Interest group）scope

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| has_ideology | 检查 scope 人物或利益集团是否具有某种意识形态 |  |  |
| has_modifier | 检查受支持的 scope 是否具有某种限时 modifier | has_modifier = <key> |  |
| has_party | 若利益集团 scope 拥有政党则为真 | has_party = bool | boolean |
| ig_approval | 与 scope 利益集团的认可度比较 | ig_approval > 2 ig_approval < happy | value |
| ig_clout | 与 scope 利益集团的政治力量比较 | ig_clout >= 0.2 | value |
| ig_government_power_share | 与 scope 利益集团的政治力量除以政府总政治力量的比例比较 | ig_government_power_share >= 0.5 | value |
| interest_group_population | 比较利益集团中的 population 数量 | interest_group_population > 1000 | value |
| interest_group_population_percentage | 比较利益集团中 population 的比例 | interest_group_population_percentage > 0.2 | value |
| interest_group_supports_political_movement | 检查 scope 利益集团是否支持某个政治运动 | interest_group_supports_political_movement = yes/no | boolean |
| is_in_government | 若利益集团 scope 处于政府中则为真 | is_in_government = bool | boolean |
| is_insurrectionary | 检查国家、运动或利益集团是否处于暴动状态 |  | boolean |
| is_interest_group_type | 检查利益集团是否属于某种类型，也可直接用于人物 | is_interest_group_type = x |  |
| is_marginal | 若利益集团 scope 处于边缘化状态则为真 | is_marginal = bool | boolean |
| is_member_of_any_lobby | 检查利益集团是否是任一政治游说团的成员 | is_member_of_any_lobby = yes | boolean |
| is_member_of_lobby | 检查利益集团是否是某种游说团类型的成员 | is_member_of_lobby = lobby_type:pro_country_lobby | political_lobby_type |
| is_member_of_party | 检查利益集团是否是目标政党的成员 | is_member_of_party = <party> | party |
| is_powerful | 若利益集团 scope 具有影响力则为真 | is_powerful = bool | boolean |
| is_revolutionary | 检查国家、运动或利益集团是否处于革命状态 |  | boolean |
| is_same_interest_group_type | 检查利益集团是否与目标属于同一利益集团类型 | is_interest_group_type = scope:neighbor_leading_ig | interest_group |
| is_secessionist | 检查国家、运动或利益集团是否处于分裂主义状态 |  | boolean |
| is_strongest_ig_in_government | 检查 scope 利益集团在政府所有利益集团中是否拥有最多的政治力量 | is_strongest_ig_in_government = yes/no | boolean |
| law_enactment_stance | 比较 scope 人物、运动或利益集团对制定指定法律相对于同组当前生效法律的立场 |  |  |
| law_stance | 比较 scope 人物、运动或利益集团对指定法律的基础立场，忽略同组当前生效的法律 |  |  |
| most_powerful_strata | 比较利益集团最强大的阶层 |  |  |
| num_political_lobbies | 与 scope 国家或利益集团中的政治游说团数量比较 | num_political_lobbies > 0 | value |
| prefers_law | 检查 scope 利益集团相对于比较法律是否更偏好指定法律 | prefers_law = { law = law_type:<law a> comparison_law = law_type:<law b> } |  |

### 机构（Institution）scope

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| has_modifier | 检查受支持的 scope 是否具有某种限时 modifier | has_modifier = <key> |  |

### 日志条目（Journal entry）scope

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| has_modifier | 检查受支持的 scope 是否具有某种限时 modifier | has_modifier = <key> |  |
| is_goal_complete | 检查日志条目的目标是否已达成 | is_goal_complete = yes/no | boolean |
| is_progressing | 检查日志条目是否正在推进 | is_progressing = yes/no | boolean |
| journal_entry_age | 返回日志条目自激活以来的天数 | journal_entry_age > 720 | value |
| scripted_bar_progress | 判定脚本进度条的进度 | scripted_bar_progress = { name = progress_bar_tag value > 0.4 } | value |

### 市场（Market）scope

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| check_area | 将对象的面积与另一个对象比较 |  |  |
| has_active_building | 若某州拥有某种活跃建筑类型则为真 | has_active_building = building |  |
| has_building | 若某州/市场/州区域/国家拥有某种建筑类型则为真 | has_building = building |  |
| has_port_market | 检查 scope 市场是否至少拥有一个港口 | has_port_market = yes/no | boolean |
| market_consumption_share | 比较 scope 市场中来自目标国家的消费占比 | market_consumption_share = { target = <country scope> goods = key (optional) value > 0.5 } | value |
| market_exports | 比较从 scope 出口到目标市场（若设定）或世界市场总体（若未指定市场）的商品总单位数 | market_exports = { target = market scope (optional) goods = key (optional) value > 100 } | value |
| market_exports_reliance | 比较 scope 市场中因出口到目标市场（若设定）或世界市场总体（若未指定市场）而产生的买单占比 | market_exports_reliance = { target = market scope (optional) goods = key (optional) value > 0.5 } | value |
| market_has_goods_shortage | 检查市场是否在其任一建筑投入品上存在短缺 | market_has_goods_shortage = yes/no | boolean |
| market_imports | 比较从目标市场进口到 scope 市场的商品总单位数 | market_imports = { target = market scope (optional) goods = key (optional) value > 100 } | value |
| market_imports_reliance | 比较 scope 市场中因从目标市场（若设定）或世界市场总体（若未指定市场）进口而产生的买单占比 | market_imports_reliance = { target = market scope (optional) goods = key (optional) value > 0.5 } | value |
| market_number_goods_shortages | 检查市场在其建筑投入品上存在多少短缺 | market_number_goods_shortages >= 2 | value |
| market_number_goods_shortages_with | 检查市场在其建筑投入品上存在多少短缺，并加上来自目标国家的短缺 | "market_number_goods_shortages_with(scope:target)" >= 2 | value |
| market_number_goods_shortages_without | 检查市场在其建筑投入品上存在多少短缺，并减去来自目标国家的短缺 | "market_number_goods_shortages_without(scope:target)" >= 2 | value |
| market_production_share | 比较 scope 市场中来自目标国家的生产占比 | market_production_share = { target = <country scope> goods = key (optional) value > 0.5 } | value |
| market_trade | 比较 scope 市场与目标市场（若设定）或世界市场总体（若未指定市场）之间交易的商品总单位数 | market_trade = { target = market scope (optional) goods = key (optional) value > 100 } | value |
| market_trade_reliance | 比较 scope 市场中因与目标市场（若设定）或世界市场总体（若未指定市场）交易而产生的买卖单占比 | market_trade_reliance = { target = market scope (optional) goods = key (optional) value > 0.5 } | value |

### 军事编队（Military formation）scope

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| formation_army_unit_type_fraction | 检查编队中某种陆军单位类型是否达到一定比例 | scope:example_formation = { country_military_unit_type_fraction = { target = unit_type:key value >= 0.2 } } | value |
| formation_ship_type_fraction | 检查编队中某种舰船类型是否达到一定比例 | formation_ship_type_fraction = { target = ship_type:key value >= 0.2 } | value |
| has_high_attrition | 检查军事编队的损耗风险是否高于其类型的基础值 | has_high_attrition = bool | boolean |
| has_mobilization_option | 检查编队是否拥有特定的动员选项 | has_mobilization_option = mobilization_option:key | mobilization_option |
| has_ship_outside_max_port_distance | 检查舰队是否有任何舰船超出其距港口的最大距离 |  | boolean |
| is_army | 检查军事编队是否为陆军 | is_army = bool | boolean |
| is_doing_piracy_in_region | 检查舰队是否在指定战略区域进行海盗活动 | is_doing_piracy_in_region = sr:region_baltic_sea | strategic_region |
| is_fleet | 检查军事编队是否为舰队 | is_fleet = bool | boolean |
| is_fully_mobilized | 检查军事编队是否已完全动员 | is_fully_mobilized = bool | boolean |
| is_invalid_naval_mission_grace_period_active | 检查舰队是否处于海军任务无效后的宽限期内 | is_invalid_naval_mission_grace_period_active = yes/no | boolean |
| is_mobilized | 检查军事编队是否已动员 | is_mobilized = bool | boolean |
| is_on_front | 检查人物或军事编队是否已被分配到某条前线并已抵达 | is_on_front = yes/no | boolean |
| organization | 比较 scope 军事编队的组织度 | organization <= define:NMilitary\|MILITARY_FORMATION_ORGANIZATION_MIN | value |
| organization_target | 比较 scope 军事编队的目标组织度 | organization_target < define:NMilitary\|MILITARY_FORMATION_ORGANIZATION_MAX | value |

### 政党（Party）scope

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| election_momentum | 将 scope 政党的选举势头与某个值比较 | election_momentum = 0.75 | value |
| has_party_member | 检查目标利益集团是否是 scope 政党的成员 | has_party_member = <ig> | interest_group |
| is_party | 检查目标政党是否与 scope 政党相同。只对完全相同的政党对象有效，即无法跨国比较 | is_party = <party> | party |
| is_party_type | 检查 scope 政党的类型是否为指定类型 | is_party_type = party_type_database_key |  |
| is_same_party_type | 检查政党是否与目标属于同一政党类型 | is_same_party_type_as = scope:neighboring_party | party |

### 政治游说团（Political lobby）scope

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| appeasement | 比较政治游说团的安抚度 |  | value |
| is_political_lobby_type | 检查政治游说团是否属于某种游说团类型 | is_political_lobby_type = political lobby type |  |
| lobby_clout | 与 scope 游说团下属利益集团的政治力量总和比较 | lobby_clout >= 0.2 | value |
| lobby_formation_reason | 检查 scope 外交催化剂或政治游说团的游说团形成原因 | lobby_formation_reason = diplomacy |  |

### 政治运动（Political movement）scope

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| has_character_ideology | 检查 scope 政治运动是否具有人物意识形态 |  |  |
| has_core_ideology | 检查 scope 政治运动是否具有核心意识形态 |  |  |
| has_ideology | 检查 scope 人物或利益集团是否具有某种意识形态 |  |  |
| has_modifier | 检查受支持的 scope 是否具有某种限时 modifier | has_modifier = <key> |  |
| is_being_bolstered | 检查 scope 运动是否正在被扶持 | is_being_bolstered = <yes>/<no> | boolean |
| is_being_suppressed | 检查 scope 运动是否正在被压制 | is_being_suppressed = <yes>/<no> | boolean |
| is_insurrectionary | 检查国家、运动或利益集团是否处于暴动状态 |  | boolean |
| is_political_movement_type | 检查政治运动是否属于某种特定类型 | is_political_movement_type = movement_to_enact |  |
| is_revolutionary | 检查国家、运动或利益集团是否处于革命状态 |  | boolean |
| is_secessionist | 检查国家、运动或利益集团是否处于分裂主义状态 |  | boolean |
| law_enactment_stance | 比较 scope 人物、运动或利益集团对制定指定法律相对于同组当前生效法律的立场 |  |  |
| law_stance | 比较 scope 人物、运动或利益集团对指定法律的基础立场，忽略同组当前生效的法律 |  |  |
| movement_can_cause_obstinance | 检查政治运动是否能在各州引发顽强抵制 | movement_can_cause_obstinance = yes | boolean |
| movement_is_causing_obstinance | 检查政治运动是否正在任一州引发顽强抵制 | movement_is_causing_obstinance = no | boolean |
| movement_pressure | 比较 scope 运动对目标利益集团施加的压力 | "movement_pressure(ig:ig_intelligentsia)" > 0.1 | value |
| political_movement_identity_support | 比较政治运动获得的具有正确文化/宗教认同的 pop 的支持 | political_movement_identity_support > 0.5 | value |
| political_movement_military_support | 比较政治运动的军方支持 | political_movement_military_support > 0.5 | value |
| political_movement_popular_support | 比较政治运动的民众支持 | political_movement_popular_support > 0.5 | value |
| political_movement_radicalism | 比较政治运动的激进程度 | political_movement_radicalism > 50 | value |
| political_movement_support | 比较政治运动的支持度 | political_movement_support > 0.5 | value |
| political_movement_wealth_support | 比较政治运动的财富支持 | political_movement_wealth_support > 0.5 | value |
### 人口（Pop）作用域

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| dependents | 比较作用域内人口的受抚养者数量 | dependents >= 2000 | value |
| food_security | 检查人口是否拥有一定数量的粮食安全度 | food_security = value | value |
| has_ongoing_assimilation | 检查作用域内人口是否有正在进行的同化 | has_ongoing_assimilation = yes | boolean |
| has_ongoing_conversion | 检查作用域内人口是否有正在进行的宗教皈依 | has_ongoing_conversion = yes | boolean |
| has_pop_culture | 检查人口是否具有特定文化 | has_pop_culture = culture |  |
| has_pop_religion | 检查人口是否具有特定宗教 | has_pop_religion = religion |  |
| has_social_class | 检查作用域内人口是否属于特定社会阶层 | has_social_class = <key> |  |
| has_state_religion | 检查人口是否信仰国教 |  | boolean |
| is_employed | 检查人口是否就业 |  | boolean |
| is_in_mild_starvation | 检查人口是否处于轻度饥荒 | is_in_mild_starvation = yes | boolean |
| is_in_severe_starvation | 检查人口是否处于严重饥荒 | is_in_severe_starvation = yes | boolean |
| is_in_starvation | 检查人口是否处于饥荒（轻度或严重） | is_in_starvation = yes | boolean |
| is_pop_type | 检查人口是否为指定类型 | is_pop_type = poptype |  |
| literacy_rate | 检查人口、州或国家是否拥有一定的识字率 | literacy = value | value |
| pop_acceptance | 将作用域内人口的接受度与一个接受度数值进行比较 | pop_acceptance > 50 | value |
| pop_employment_building | 检查人口是否在特定建筑类型中工作 | pop_employment_building = building |  |
| pop_employment_building_group | 检查人口是否在特定建筑类型中工作 | pop_employment_building = building |  |
| pop_has_primary_culture | 检查人口的文化是否为主要文化 | pop_has_primary_culture = bool | boolean |
| pop_loyalist_fraction | 将人口中忠诚派的数量与其总人口进行比较 | pop_loyalty_fraction < 0.5 | value |
| pop_neutral_fraction | 将人口中中立者（既非激进派也非忠诚派）的数量与其总人口进行比较 | pop_neutral_fraction > 0.95 | value |
| pop_radical_fraction | 将人口中激进派的数量与其总人口进行比较 | pop_radical_fraction > 0.25 | value |
| quality_of_life | 比较给定人口的生活质量 | quality_of_life > 10 | value |
| standard_of_living | 比较给定人口的生活水平 | standard_of_living > 10 | value |
| strata | 检查作用域内人口的阶层 | strata >= upper/middle/lower | value |
| total_size | 比较作用域内人口的总规模 | total_size >= 3000 | value |
| wealth | 检查人口是否拥有一定数量的财富 | wealth = value | value |
| workforce | 比较作用域内人口的劳动力规模 | workforce >= 1000 | value |

### 强权集团作用域

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| can_invite_any_country | 检查是否可以向作用域内的强权集团邀请任何国家 | can_invite_any_country = yes/no | boolean |
| current_cohesion_number | 以数值形式比较当前凝聚力 | current_cohesion_number > 50 | value |
| current_cohesion_percentage | 以占作用域内强权集团最大凝聚力的百分比形式比较当前凝聚力 | current_cohesion_percentage > 0.5 | value |
| free_principle_slots | 比较强权集团的空闲原则槽位数量 | power_bloc = { free_principle_slots >= 2 } | value |
| has_identity | 检查作用域内的强权集团是否具有特定的核心认同 | has_identity = identity:key | power_bloc_identity |
| has_modifier | 检查受支持的作用域是否具有特定的限时修正 | has_modifier = <key> |  |
| has_principle | 检查作用域内的强权集团是否具有特定原则 | has_principle = principle:key | power_bloc_principle |
| has_principle_group | 检查作用域内的强权集团是否在指定组别中拥有原则 | has_principle_group = principle_group:key | power_bloc_principle_group |
| leverage_advantage | 检查强权集团与目标国家之间的影响力优势是否满足条件 | power_bloc = { leverage_advantage = { target = c:BEL value > 0 } } | value |
| num_power_bloc_members | 将强权集团的成员数量与一个数值进行比较 | num_power_bloc_members >= 2 | value |
| num_power_bloc_states | 将强权集团内的州数量与一个数值进行比较 | num_power_bloc_states >= 2 | value |
| power_bloc_rank | 比较强权集团的排名 | power_bloc_rank <= 2 | value |
| power_bloc_total_leading_goods_producers | 比较有多少成员位列全球所有商品的领先生产者之中，并按其在排名中的位置加权。排名第一的生产者权重为 MIN_SPOT_PRESTIGE_AWARD，其后每个名次的权重依次递减一。默认情况下，第 1 名计为 3，第 2 名计为 2，第 3 名计为 1，其他名次计为 0。 | power_bloc_total_leading_goods_producers > 15 | value |
| power_bloc_total_leading_goods_producers_with | 比较有多少成员位列全球所有商品的领先生产者之中，并按其在排名中的位置加权，外加一个当前不属于该强权集团的国家。排名第一的生产者权重为 MIN_SPOT_PRESTIGE_AWARD，其后每个名次的权重依次递减一。默认情况下，第 1 名计为 3，第 2 名计为 2，第 3 名计为 1，其他名次计为 0。 | "power_bloc_total_leading_goods_producers_with(scope:target) > 15" | value |
| power_bloc_total_leading_goods_producers_without | 比较有多少成员位列全球所有商品的领先生产者之中，并按其在排名中的位置加权，减去一个当前属于该强权集团的国家。排名第一的生产者权重为 MIN_SPOT_PRESTIGE_AWARD，其后每个名次的权重依次递减一。默认情况下，第 1 名计为 3，第 2 名计为 2，第 3 名计为 1，其他名次计为 0。 | "power_bloc_total_leading_goods_producers_without(scope:target) > 15" | value |
| power_bloc_worst_economic_dependence | 若在强权集团作用域中使用，比较对领袖经济依赖最低的成员 | power_bloc_worst_economic_dependence > 2.2 | value |
| power_bloc_worst_economic_dependence_with | 若在强权集团作用域中使用，比较对领袖经济依赖最低的成员 | power_bloc_worst_economic_dependence > 2.2 | value |
| power_bloc_worst_economic_dependence_without | 若在强权集团作用域中使用，比较对领袖经济依赖最低的成员 | power_bloc_worst_economic_dependence > 2.2 | value |
| power_bloc_worst_infamy | 若在强权集团作用域中使用，比较恶名值最差（最高）的成员国的恶名值 | power_bloc_worst_infamy > 50 | value |
| power_bloc_worst_infamy_with | 若在强权集团作用域中使用，比较恶名值最差（最高）的成员国的恶名值 | power_bloc_worst_infamy > 50 | value |
| power_bloc_worst_infamy_without | 若在强权集团作用域中使用，比较恶名值最差（最高）的成员国的恶名值 | power_bloc_worst_infamy > 50 | value |
| power_bloc_worst_leader_relations | 若在强权集团作用域中使用，比较与强权集团领袖关系值最差（最低）的成员国的关系值 | power_bloc_worst_leader_relations > 10 | value |
| power_bloc_worst_leader_relations_with | 若在强权集团作用域中使用，比较与强权集团领袖关系值最差（最低）的成员国的关系值 | power_bloc_worst_leader_relations > 10 | value |
| power_bloc_worst_leader_relations_without | 若在强权集团作用域中使用，比较与强权集团领袖关系值最差（最低）的成员国的关系值 | power_bloc_worst_leader_relations > 10 | value |
| power_bloc_worst_leader_religion_population_fraction | 若在强权集团作用域中使用，比较成员国中信仰领袖宗教的人口比例的最低值 | power_bloc_worst_leader_religion_population_fraction > 10 | value |
| power_bloc_worst_leader_religion_population_fraction_with | 若在强权集团作用域中使用，比较成员国中信仰领袖宗教的人口比例的最低值 | power_bloc_worst_leader_religion_population_fraction > 10 | value |
| power_bloc_worst_leader_religion_population_fraction_without | 若在强权集团作用域中使用，比较成员国中信仰领袖宗教的人口比例的最低值 | power_bloc_worst_leader_religion_population_fraction > 10 | value |
| power_bloc_worst_liberty_desire | 若在强权集团作用域中使用，比较独立倾向值最差（最高）的成员国的独立倾向 | power_bloc_worst_liberty_desire > 75 | value |
| power_bloc_worst_liberty_desire_with | 若在强权集团作用域中使用，比较独立倾向值最差（最高）的成员国的独立倾向 | power_bloc_worst_liberty_desire > 75 | value |
| power_bloc_worst_liberty_desire_without | 若在强权集团作用域中使用，比较独立倾向值最差（最高）的成员国的独立倾向 | power_bloc_worst_liberty_desire > 75 | value |
| power_bloc_worst_progressiveness_difference_government_type | 若在强权集团作用域中使用，比较其治理原则与权力分配法律相较于强权集团领袖的进步性差异总值最差（最高）的成员国的进步性差异 | power_bloc_worst_progressiveness_compatibility_government_type > 100 | value |
| power_bloc_worst_progressiveness_difference_government_type_with | 若在强权集团作用域中使用，比较其治理原则与权力分配法律相较于强权集团领袖的进步性差异总值最差（最高）的成员国的进步性差异 | power_bloc_worst_progressiveness_compatibility_government_type > 100 | value |
| power_bloc_worst_progressiveness_difference_government_type_without | 若在强权集团作用域中使用，比较其治理原则与权力分配法律相较于强权集团领袖的进步性差异总值最差（最高）的成员国的进步性差异 | power_bloc_worst_progressiveness_compatibility_government_type > 100 | value |
| predicted_cohesion_percentage_with | 预测强权集团在将目标国家纳入为成员后的凝聚力（以 1 为基数的比例） | predicted_cohesion_percentage_with, = { target = scope:other_country value > 0.9 } | value |
| target_cohesion_number | 以数值形式比较目标凝聚力 | target_cohesion_number > 50 | value |
| target_cohesion_percentage | 以占作用域内强权集团最大凝聚力的百分比形式比较目标凝聚力 | target_cohesion_percentage > 0.5 | value |
| total_used_principle_levels | 比较强权集团已激活原则等级的总数 | power_bloc = { total_used_principle_levels >= 10 } | value |
| used_principle_slots | 比较强权集团已使用的原则槽位数量 | power_bloc = { used_principle_slots >= 2 } | value |

### 舰船作用域

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| armor | 比较舰船的装甲 | armor >= 10 | value |
| crew | 比较舰船的当前船员数 | crew >= 10 | value |
| crew_percent | 比较舰船的当前船员百分比 | crew_percent >= 0.1 | value |
| days_obsolete | 比较舰船首次被 AI 标记为过时以来的天数。若舰船从未被标记则返回 0。 | days_obsolete >= 1825 | value |
| hit_points | 比较舰船的当前耐久值 | hit_points >= 10 | value |
| hit_points_percent | 比较舰船的当前耐久百分比 | hit_points_percent >= 0.1 | value |
| is_attacker_in_battle | 检查指挥官或舰船是否为某场战斗中的进攻方 | is_attacker_in_battle = bool | boolean |
| is_damaged | 检查舰船是否受损 | is_damaged = bool | boolean |
| is_defender_in_battle | 检查指挥官或舰船是否为某场战斗中的防守方 | is_defender_in_battle = bool | boolean |
| is_flagship | 检查作用域内的舰船是否被指定为旗舰 | is_flagship = bool | boolean |
| is_in_battle | 检查指挥官或舰船是否正在交战中 | is_in_battle = bool | boolean |
| is_in_port | 检查舰船是否位于港口中 | is_in_port = bool | boolean |
| is_ship_type | 检查作用域内的舰船是否为指定类型 | is_ship_type = ship_type:ship_type_frigate | ship_type |
| power_projection_value | 比较舰船的力量投射值 | power_projection_value >= 10 | value |
| speed | 比较舰船的速度 | speed >= 10 | value |

### 州作用域

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| arable_land | 检查州内的可耕地 | arable_land > 10 | value |
| available_jobs | 检查州内非自给型建筑的可用职位数量 | available_jobs > 10000 | value |
| blockade_level | 与州的封锁等级进行比较 | blockade_level > 0.1 | value |
| can_activate_production_method | 检查作用域内州的特定类型建筑能否激活指定的生产方式 | can_activate_production_method = { building_type = <key> production_method = <key> } |  |
| can_construct_building | 检查是否可以在作用域内的州中建造 1 级 <building_type> | can_construct_building = <building_type> |  |
| check_area | 将对象的区域与另一个对象进行比较 |  |  |
| cultural_acceptance_delta | 比较作用域内州中某文化接受度的当前本地增量（修正） | cultural_acceptance_delta = { target = cu:romanian value < -10 } | value |
| culture_percent_state | 检查州的人口中特定文化是否占有一定百分比 | scope:example_state = { culture_percent_state = { target = cu:dixie value >= 0.2 } } | value |
| devastation | 比较给定州的破坏度 | devastation > 5 | value |
| free_arable_land | 检查州内的空闲可耕地 | free_arable_land > 0 | value |
| has_active_building | 若州拥有一个处于活跃状态的建筑类型则为真 | has_active_building = building |  |
| has_assimilating_pops | 检查州内是否有任何人口正处于同化过程中。 |  | boolean |
| has_building | 若州/市场/州区域/国家拥有某建筑类型则为真 | has_building = building |  |
| has_claim_by | 检查州是否被某国家声索 | any_state = { owner = root has_claim_by = c:MEX } | country |
| has_converting_pops | 检查州内是否有任何人口正处于皈依过程中。 |  | boolean |
| has_cultural_community | 检查某文化是否在作用域内的州中拥有文化社区。 | has_cultural_community = <culture> |  |
| has_decree | 检查作用域内的州是否拥有特定类型的法令 | has_decree = <key> |  |
| has_famine | 检查州或国家是否发生饥荒 | has_famine = yes/no | boolean |
| has_mobilizing_unit | 检查作用域内的州中是否有任何建筑维持着当前正在动员的作战单位 | has_mobilizing_unit = bool | boolean |
| has_modifier | 检查受支持的作用域是否具有特定的限时修正 | has_modifier = <key> |  |
| has_port_state | 检查作用域内的州是否拥有至少一个港口 | has_port = yes/no | boolean |
| has_potential_resource | 检查指定建筑组是否被允许在作用域内的州中建造。用于检查州是否具有生产某资源的潜力 | has_potential_resource = bg_rubber_plantations | building_group |
| has_state_trait | 检查作用域内的州是否拥有特定特质 | has_state_trait = key |  |
| ig_state_pol_strength_share | 若作用域内利益集团在州中拥有脚定的政治力量则为真 | ig_state_pol_strength_share = { target = scope:target_ig value = 0.3 } | value |
| incorporation_progress | 检查州的整合进度 | incorporation_progress > 0.25 | value |
| infrastructure | 比较给定州的基础设施值 | infrastructure > 10 | value |
| infrastructure_delta | 比较给定州的基础设施差额 | infrastructure_delta > 0 | value |
| infrastructure_usage | 比较给定州的基础设施使用值 | infrastructure_usage > 10 | value |
| is_being_bombarded | 检查州当前是否正被敌对舰队炮击港口 |  | boolean |
| is_blockaded_by | 检查州是否被某国家封锁 |  | country |
| is_capital | 检查州是否为其所有者的首都 = bool |  | boolean |
| is_coastal | 检查州是否与（可通行的）海域接壤 | is_coastal = yes/no | boolean |
| is_homeland_of_country_cultures | 检查州是否为目标国家任一主要文化的本土 | is_homeland_of_country_cultures = <country> | country |
| is_in_revolt | 检查州是否有任何机会分裂为革命国家或分离国家 | is_in_revolt = yes/no. | boolean |
| is_incorporated | 检查州是否已整合 = bool |  | boolean |
| is_isolated_from_market | 检查州是否与其市场隔绝 |  | boolean |
| is_largest_state_in_region | 检查州是否为州区域中最大的州 = bool |  | boolean |
| is_mass_migration_target | 大规模迁移的目的地为该州。 | is_mass_migration_target = yes | boolean |
| is_mass_migration_target_for_culture | 作用域内的州是指定文化的大规模迁移目的地。 | is_mass_migration_target_for_culture = scope:my_culture | culture |
| is_potential_treaty_port | 检查作用域内的州是否有潜力成为目标国家的条约港 | is_potential_treaty_port = c:FRA | country |
| is_production_method_active | 检查作用域内州的特定类型建筑是否已激活指定的生产方式 | is_production_method_active = { building_type = <key> production_method = <key> } |  |
| is_sea_adjacent | 检查州是否与海域接壤（普通或不可通行） | is_sea_adjacent = yes/no | boolean |
| is_slave_state | 检查州是否正在使用或有可能使用奴隶。 |  | boolean |
| is_split_state | 检查作用域内的州是否为被分割的州。 | scope:example_state = { is_split_state = yes } | boolean |
| is_strategic_objective | 检查作用域内的州是否为某国家的战略目标 | is_strategic_objective = <country> | country |
| is_target_of_wargoal | 检查州是否为涉及指定国家的战争中任何战争目标的目标 | has_war_goal = <country> | country |
| is_treaty_port | 检查作用域内的州是否为条约港 | is_treaty_port = yes/no | boolean |
| is_under_colonization | 检查州是否正处于殖民中 | is_under_colonization = yes/no | boolean |
| is_world_market_hub | 检查州是否为世界市场枢纽 | is_world_market_hub = yes | boolean |
| literacy_rate | 检查人口、州或国家是否拥有一定的识字率 | literacy = value | value |
| loyalist_fraction | 比较州或国家中各人口的忠诚派比例，除 value 外的所有参数均为可选 | loyalist_fraction = { value = <script_value> pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> } | value |
| loyalists | 比较给定州的忠诚度，即忠诚派的比例 | loyalists > 0.2 | value |
| market_access | 检查作用域内州的市场接入 | market_access > 0.8 | value |
| most_prominent_revolting_interest_group | 检查作用域内的州中最显眼的叛乱利益集团是否为给定的利益集团类型。若作用域内的州未处于叛乱中则判定为假。 | most_prominent_revolting_interest_group = ig_landowners |  |
| num_cultural_communities | 检查州内的文化社区数量 | num_cultural_communities > 5 | value |
| obstinance | 比较州的顽固度 | obstinance > 0.5 | value |
| political_strength_share | 检查某人口类型、宗教或文化在国家或州中的政治力量份额。必须且只能指定 pop_type、religion 或 culture 其中之一。 | political_strength_share = { pop_type/religion/culture = <key/scope> value <compare operator> <value> } | value |
| pollution_generation | 比较州内所有建筑的总污染产生量 |  | value |
| pop_type_percent_state | 检查州的人口中特定人口类型是否占有一定百分比 | scope:example_state = { pop_type_percent_state = { target = pop_type:laborer value <= 0.8 } } | value |
| population_by_culture | 比较作用域内的州中目标文化的当前人口 | population_by_culture = { target = cu:romanian value > 2500 } | value |
| primary_cultures_percent_state | 检查州的人口中国家主要文化是否占有一定百分比 | scope:example_state = { primary_cultures_percent_state >= 0.2 } | value |
| radical_fraction | 比较州或国家中各人口的激进派比例，除 value 外的所有参数均为可选 | radical_fraction = { value = <script_value> pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> } | value |
| relative_infrastructure | 比较州的基础设施与基础设施使用量 | relative_infrastructure > 1.1 | value |
| religion_percent_state | 检查州的人口中特定宗教是否占有一定百分比 | scope:example_state = { religion_percent_state = { target = rel:catholic value <= 0.8 } } | value |
| state_cultural_acceptance | 检查目标文化的人口在作用域内的州中的接受程度 | state_cultural_acceptance = { target = cu:french value >= 50 | value |
| state_exports | 比较从作用域州出口到目标州（若已设定）或全世界总体（若未指定州）的总商品单位数 | state_exports = { target = state scope (optional) goods = key (optional) value >= 100 } | value |
| state_has_building_group_levels | 检查州内某建筑组的建筑等级总和 | state_has_building_group_levels = { type = bg_heavy_industry value >= 100 } | value |
| state_has_building_levels | 检查州的建筑等级总和 | state_has_building_levels >= 10 | value |
| state_has_building_type_levels | 检查州内某建筑类型的建筑等级总和 | state_has_building_type_levels = { target = bt:building_barracks value >= 100 } | value |
| state_has_goods_shortage | 检查州的任何建筑投入是否存在短缺 | state_has_goods_shortage = yes/no | boolean |
| state_has_national_awakening | 检查作用域内的州是否位于带有活跃的民族觉醒地图标记的州区域中 | state_has_national_awakening = yes/no | boolean |
| state_imports | 比较从目标州进口到作用域州的总商品单位数 | state_imports = { target = state scope (optional) goods = key (optional) value >= 100 } | value |
| state_is_eligible_as_mass_migration_target | 检查州是否完全有资格接收大规模迁移。 | any_state = { state_is_eligible_as_mass_migration_target = yes } | boolean |
| state_population | 检查作用域内州的总人口 | state_population <= 250000 | value |
| state_religious_acceptance | 检查给定宗教的人口在作用域内的州中的接受程度 | state_religious_acceptance = { target = rel:catholic value >= 50 | value |
| state_trade | 比较作用域州与目标州（若已设定）或全世界总体（若未指定州）之间交易的商品总单位数 | state_trade = { target = state scope (optional) goods = key (optional) value >= 100 } | value |
| state_unemployment_rate | 检查作用域内州的失业率（百分比） | state_unemployment_rate > 0.1 | value |
| tax_capacity | 检查作用域内州的税收能力 | tax_capacity > 50 | value |
| tax_capacity_usage | 检查所在州的税收能力使用量 | tax_capacity_usage > 50 | value |
| total_urbanization | 比较给定州的总城市化度 | total_urbanization > 5 | value |
| turmoil | 比较给定州的动荡度，即激进派的比例 | turmoil > 0.2 | value |
| wealth_share | 检查某国家或州中某人口类型、宗教或文化的财富政治力量份额。必须且只能指定 pop_type、religion 或 culture 中的一项。 | wealth_share = { pop_type/religion/culture = <key/scope> value <compare operator> <value> } | value |
| world_market_access | 检查所在州的世界市场接入度 | world_market_access > 0.8 | value |

### 州商品作用域

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| export_advantage | 与州商品出口优势比较 | export_advantage >= 100 | value |
| export_tariff_level | 检查州商品是否设置了特定的出口关税等级 | export_tariff_level = max_tariffs |  |
| has_potential_supply | 检查市场商品或州商品是否有潜在供给，可来自本地生产或理论进口 |  | boolean |
| import_advantage | 与州商品进口优势比较 | import_advantage >= 100 | value |
| import_tariff_level | 检查州商品是否设置了特定的进口关税等级 | import_tariff_level = max_tariffs |  |
| relative_export_advantage | 与州商品相对出口优势比较 | relative_export_advantage > 0.1 | value |
| relative_import_advantage | 与州商品相对进口优势比较 | relative_import_advantage > 0.1 | value |
| state_goods_cheaper | 检查州商品是否至少比基准价便宜指定百分比 | state_goods_cheaper > <value> | value |
| state_goods_consumption | 检查州商品的总消费量是否达到指定数值 | state_goods_consumption < <value> | value |
| state_goods_delta | 检查州是否有指定的商品差额（生产 - 消费） | state_goods_delta < <value> | value |
| state_goods_has_local_goods_shortage | 检查州商品在该州是否存在短缺，但整个市场并不短缺 | state_goods_has_local_goods_shortage = yes/no | boolean |
| state_goods_pricier | 检查州商品是否至少比基准价贵指定百分比 | state_goods_pricier > <value> | value |
| state_goods_production | 检查州商品的总生产量是否达到指定数值 | state_goods_production < <value> | value |

### 州地区作用域

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| check_area | 将对象面积与另一对象比较 |  |  |
| contains_capital_of | 检查所在州地区是否包含目标 tag 的首都 | contains_capital_of = country scope/tag |  |
| has_building | 若州/市场/州地区/国家拥有某建筑类型则为真 | has_building = building |  |
| has_harvest_condition | 检查所在州地区是否有指定类型的收成状况 | has_harvest_condition = drought |  |
| infrastructure | 比较给定州的基础设施值 | infrastructure > 10 | value |
| infrastructure_delta | 比较给定州的基础设施平衡 | infrastructure_delta > 0 | value |
| infrastructure_usage | 比较给定州的基础设施使用值 | infrastructure_usage > 10 | value |
| is_homeland | 检查所在州地区是否为目标文化的本土 | is_homeland = culture scope/name |  |
| is_state_region_land | 检查州地区是否位于陆地上 |  | boolean |
| pollution_amount | 比较州地区污染 |  | value |
| remaining_undepleted | 检查剩余资源量，例如州中的金矿 | remaining_undepleted = { type = bg_gold_mining amount > 1 } | value |

### 条约作用域

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| binds | 检查所在条约或 treaty_options 是否约束给定国家 | scope:some_treaty = { if = { limit = { binds = c:FRA binds = c:BEL } } } | country |
| is_enforced | 检查所在条约是否对任意一方强制执行 | scope:some_treaty = { if = { limit = { is_enforced = yes } } } | boolean |
| is_equal_exchange | 检查所在条约双方条款是否相同 | scope:some_treaty = { if = { limit = { is_equal_exchange = yes } } } | boolean |
| is_fulfilled_by | 检查所在条约是否由给定国家履行 | scope:treaty = { is_fulfilled_by = c:FRA } | country |
| is_historical_treaty | 检查所在条约是否在游戏开始日期前签署 | is_historical_treaty = yes/no | boolean |
| is_renegotiation | 检查所在条约是否在修订现有条约 | scope:some_treaty = { if = { limit = { is_renegotiation = yes } } } | boolean |
| was_coerced_with_naval_threat | 检查所在条约是否通过海军敌对威胁而被接受 | was_coerced_with_naval_threat = yes/no | boolean |

### 战争作用域

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| has_war_exhaustion | 检查所在战争中目标国家的厌战度 | has_war_exhaustion = { target = c:GBR value > 50 } | value |
| has_war_goal | 检查战争是否有某种战争目标类型 | has_war_goal = return_state |  |
| has_war_support | 检查所在战争中目标国家的战争支持度 | has_war_support = { target = c:GBR value > 50 } | value |
| is_holder_of_wargoal_in_war | 检查指定国家是否是所在战争中任一战争目标的持有者 | is_holder_of_wargoal_in_war = <country> | country |
| is_war_participant | 检查目标国家是否是战争参与者 |  | country |
| is_warleader | 检查国家是否是战争中的战争领袖 |  | country |
| num_casualties | 检查所在战争的总伤亡人数 | num_casualties >= 5000 | value |
| num_country_casualties | 检查所在战争中目标国家的伤亡人数 | num_country_casualties = { target = country value < 5000 } | value |
| num_country_dead | 检查所在战争中目标国家的死亡人数 | num_country_dead = { target = country value < 5000 } | value |
| num_country_wounded | 检查所在战争中目标国家的受伤人数 | num_country_wounded = { target = country value < 5000 } | value |
| num_dead | 检查所在战争的总死亡人数 | num_dead >= 5000 | value |
| num_wounded | 检查所在战争的总受伤人数 | num_wounded >= 5000 | value |
| war_exhaustion_from_acceptance_of_dead | 判定一个国家因对战争中阵亡人力的文化接受程度而产生的厌战度，无论其属于哪一方 | war_exhaustion_from_acceptance_of_dead = { target = root value >= 0.4 } | value |
| war_has_active_peace_deal | 若战争已有提议的和约则为真 | war_has_active_peace_deal = bool | boolean |

## 所有 trigger

使用此表搜索所有 trigger。

| Trigger | 描述 | 示例 | 作用域 | 目标 |
|---|---|---|---|---|
| active_lens | 检查指定的镜头（lens）是否打开 | active_lens = lens | none |  |
| active_lens_option | 检查指定的镜头选项是否已激活 | active_lens_option = lens_option_key | none |  |
| add_to_temporary_list | 保存一个临时目标，供 trigger 执行期间使用 | 用于在 trigger 中构建列表。若在 any 类 trigger 中使用，其位置相当重要。游戏会遍历 any 类 trigger 的每个实例，直到找到单个满足要求的实例，然后停止。要添加所有满足特定条件的作用域实例，请使用 "count = all"，同时将此 "effect" 放在 any 类 trigger 的最末尾，以便每次迭代都评估所有条件。 | none |  |
| additional_war_exhaustion | 比较所在国家在目标外交博弈中从脚本事件累积的额外厌战度 | additional_war_exhaustion = { target = scope:war.diplomatic_play value > 1.0 } | country | value |
| age | 比较人物年龄 | age > 20 | character | value |
| aggressive_diplomatic_plays_permitted | 若国家独立或被允许发起自己的外交博弈则为真 | aggressive_diplomatic_plays_permitted = bool | country | boolean |
| ai_ship_value | AI 对一艘船的估值（单位英镑），等于当前模板版本建造成本乘以 NAI::SHIP_TRANSFER_BASE_VALUE_PER_CONSTRUCTION_POINT | ai_ship_value >= 5000 | country | value |
| all_false | 若所有包含的 trigger 均为假则为真（等价于 NOR） |  | none |  |
| always | 检查指定的 yes/no 值是否为真 | always = yes # 总是成功 always = no # 总是失败 always = scope:a_boolean_value # 运行时求值 | none | boolean |
| amendment_can_be_repealed | 检查修正案是否可被废除 | amendment_can_be_repealed = yes/no | amendment | boolean |
| amendment_count | 比较作用域内法律中的修正案数量 | amendment_count >= 2 | law | value |
| amendment_stance | 比较所在人物、政治运动或利益集团对指定修正案类型的立场（前提是该修正案类型有母法律） | amendment_stance = { amendment = <scope> value = <stance> } | character, interest_group, political_movement |  |
| and | 若所有包含的 trigger 均为真则为真 遇到第一个为假的子 trigger 即返回假 |  | none |  |
| any_active_law | 遍历一个国家所有生效的法律 | any_active_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | law |
| any_active_party | 遍历一个国家所有活跃的政党 | any_active_party = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | party |
| any_character | 遍历全局所有人物 | any_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | character |
| any_character_in_exile_pool | 遍历流放池中的人物 | any_character_in_exile_pool = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | character |
| any_character_in_void | 遍历虚空（void）中的人物 | any_character_in_void = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | character |
| any_character_role | 遍历所在人物的所有角色 | any_character_role = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character | character_role |
| any_civil_war | 遍历与所在国家相关的所有内战 | any_civil_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | civil_war |
| any_cobelligerent_in_diplo_play | 遍历所在国家在所有外交博弈（包括战争）中的所有共同交战国 | any_cobelligerent_in_diplo_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_cobelligerent_in_war | 遍历所在国家在所有战争中的所有共同交战国 | any_cobelligerent_in_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_combat_unit | 遍历输入作用域中的所有作战单位 | any_combat_unit = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | battle, building, front, hq, military_formation | new_combat_unit |
| any_company | 遍历一个国家中的所有公司 | any_company = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | company |
| any_country | 遍历全局所有国家 | any_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | country |
| any_country_in_<georegion_short_name> | 遍历指定地理区域中的所有国家 | any_country_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | country |
| any_country_strategic_region | 遍历包含所在国家拥有的州的所有战略区域 | any_country_strategic_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | strategic_region |
| any_decentralized_country | 遍历所有非中央集权国家 | any_decentralized_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | country |
| any_diplomatic_catalyst | 遍历一个国家近期记忆中的所有外交催化剂 | any_diplomatic_catalyst = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | diplomatic_catalyst |
| any_diplomatic_play | 遍历全局所有外交博弈 | any_diplomatic_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | diplomatic_play |
| any_diplomatically_relevant_country | 遍历一个国家作用域的所有外交相关国家 | any_diplomatically_relevant_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_direct_subject | 层级中直接位于当前国家之下的任何国家 | any_direct_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_enemy_in_diplo_play | 遍历所在国家在所有外交博弈（包括战争）中的所有敌人 | any_enemy_in_diplo_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_enemy_in_war | 遍历所在国家在所有战争中的所有敌人 | any_enemy_in_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_false | 若任一包含的 trigger 为假则为真（等价于 NAND） |  | none |  |
| any_harvest_condition | 遍历影响一个州、州地区、战略区域或国家的所有收成状况 | any_harvest_condition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state, state_region, strategic_region | harvest_condition |
| any_in_global_list | 遍历全局列表中的所有项目。 | any_in_global_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } 由 add_to_(temporary)_list 创建的列表使用 "list" 由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| any_in_hierarchy | 当前层级中的任何国家，包括当前国家 | any_in_hierarchy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_in_list | 遍历列表中的所有项目。 | any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } 由 add_to_(temporary)_list 创建的列表使用 "list" 由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| any_in_local_list | 遍历局部列表中的所有项目。 | any_in_local_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } 由 add_to_(temporary)_list 创建的列表使用 "list" 由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| any_influenced_interest_group | 遍历受一个政治运动影响的所有利益集团 | any_influenced_interest_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_movement | interest_group |
| any_interest_group | 遍历一个国家中的所有利益集团 | any_interest_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | interest_group |
| any_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | any_key_in_global_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | any_key_in_local_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_key_in_variable_map | 遍历变量映射中的所有键。 | any_key_in_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_law | 遍历一个国家中的所有法律 | any_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | law |
| any_lobby_member | 遍历一个游说团体的所有利益集团成员 | any_lobby_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_lobby | interest_group |
| any_market | 遍历全局所有市场 | any_market = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | market |
| any_market_goods | 遍历一个市场中的所有活跃（市场）商品 | any_market_goods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | market | market_goods |
| any_member | 遍历一个政党的所有利益集团成员 | any_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | party | interest_group |
| any_military_formation | 遍历输入作用域当前的所有军事编队 | any_military_formation = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, hq | military_formation |
| any_neighbouring_state | 遍历与一个州地区相邻的所有州 | any_neighbouring_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state, state_region, strategic_region | state |
| any_overlord_or_above | 层级中位于当前国家之上的任何国家 | any_overlord_or_above = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_owned_country | 遍历所在公司拥有的所有国家 | any_owned_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | company | country |
| any_participant | 作用域内外交协定的两个参与者中的任一个 | any_participant = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_pact | country |
| any_political_lobby | 遍历一个国家或利益集团中的所有政治游说团体 | any_political_lobby = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, interest_group | political_lobby |
| any_political_movement | 遍历一个国家中的所有政治运动 | any_political_movement = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | political_movement |
| any_possible_amendment_type | 遍历可添加到所在法律的修正案类型 | any_possible_amendment_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | law | amendment_type |
| any_potential_party | 遍历一个国家所有潜在的政党 | any_potential_party = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | party |
| any_power_bloc | 遍历所有强权集团 | any_power_bloc = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | power_bloc |
| any_power_bloc_member | 遍历所在强权集团的所有成员，包括领袖 | any_power_bloc_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | power_bloc | country |
| any_preferred_law | 按偏好程度顺序遍历利益集团所在国家所有生效及可能的法律 | any_preferred_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | interest_group | law |
| any_primary_culture | 所在国家或国家定义的主流文化 | any_primary_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, country_definition | culture |
| any_province | 遍历所在州中的所有省份 | any_province = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state | province |
| any_province_in_<georegion_short_name> | 遍历指定地理区域中的所有省份 | any_province_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | province |
| any_rival_country | 与作用域中国家处于竞争关系的任何国家 | any_rival_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_rivaling_country | 作用域中国家正在与之竞争的任何国家 | any_rivaling_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_scope_admiral | 遍历以下作用域中的所有海军上将：国家、利益集团或军事编队 | any_scope_admiral = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_ally | 遍历一个国家的所有盟友 | any_scope_ally = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_scope_amendment | 遍历所在法律的修正案 | any_scope_amendment = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | law | amendment |
| any_scope_army | 遍历输入作用域当前的所有陆军 | any_scope_army = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, hq | military_formation |
| any_scope_article | 遍历所在条约的条款 | any_scope_article = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty | treaty_article |
| any_scope_article_option | 遍历所在条约或 treaty_options 的条款选项 | any_scope_article_option = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty, treaty_options | treaty_article_options |
| any_scope_building | 遍历以下作用域中的所有建筑：州、国家 | any_scope_building = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state | building |
| any_scope_character | 遍历以下 scope 中的所有人物：国家、利益集团或前线 | any_scope_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_country | 遍历在受支持的 scope（当前为：市场、战略区域）中存在的所有国家 | any_scope_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | market, state_region, strategic_region | country |
| any_scope_culture | 遍历该 scope 中的所有文化 | any_scope_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state | culture |
| any_scope_diplomatic_pact | scope 中国家的任意外交条约 | any_scope_diplomatic_pact = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | diplomatic_pact |
| any_scope_fleet | 遍历当前存在于输入 scope 中的所有舰队 | any_scope_fleet = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, hq | military_formation |
| any_scope_front | 遍历与 scope 中的战争相关的所有前线 | any_scope_front = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | war | front |
| any_scope_general | 遍历以下 scope 中的所有将军：国家、利益集团、前线或军事编队 | any_scope_general = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_held_interest_marker | 遍历一个国家持有的所有利益标记 | any_scope_held_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | interest_marker |
| any_scope_homeland_state | 遍历作为 scope 文化的家园，或 scope 国家任意主流文化家园的所有州 | any_scope_homeland_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character, country | state |
| any_scope_initiator_ally | 遍历外交博弈中发起方的所有盟友 | any_scope_initiator_ally = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_play | country |
| any_scope_interest_marker | 遍历以下 scope 中的所有利益标记：国家、战略区域 | any_scope_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state_region, strategic_region | interest_marker |
| any_scope_je_involved | 遍历日志条目的所有相关方 | any_scope_je_involved = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | journal_entry | country |
| any_scope_play_involved | 遍历外交博弈的所有相关方 | any_scope_play_involved = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_play | country |
| any_scope_politician | 遍历以下 scope 中的所有政客：国家或利益集团 | any_scope_politician = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_pop | 遍历以下 scope 中的所有人口：国家、州、利益集团、文化 | any_scope_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, culture, interest_group, state | pop |
| any_scope_regional_hqs | 遍历 scope 公司的地区总部 | any_scope_regional_hqs = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | company | building |
| any_scope_ship | 遍历一个国家或军事编队中的所有舰船 | any_scope_ship = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, military_formation | ship |
| any_scope_state | 遍历以下 scope 中包含地区的所有州：国家、州区域、战区、前线或海峡 | any_scope_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, state_region, strait, strategic_region, theater | state |
| any_scope_strait | 遍历在 scope 州或国家拥有陆地端点的所有海峡 | any_scope_strait = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state | strait |
| any_scope_target_ally | 遍历外交博弈中目标方的所有盟友 | any_scope_target_ally = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_play | country |
| any_scope_theater | 遍历一个国家中的所有战区 | any_scope_theater = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | theater |
| any_scope_treaty | 遍历对 scope 国家有约束力的生效条约 | any_scope_treaty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | treaty |
| any_scope_violate_sovereignty_interested_parties | 遍历在 scope 国家的主权被侵犯时会关切的所有国家 | any_scope_violate_sovereignty_interested_parties = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_scope_violate_sovereignty_wars | 遍历目标国家被 scope 国家侵犯主权时的所有相关战争 | any_scope_violate_sovereignty_wars = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | war |
| any_scope_war | 遍历与该 scope 相关的所有战争 | any_scope_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | war |
| any_sea_node_adjacent_state | 遍历与某个州共享海洋节点的所有州 | any_sea_node_adjacent_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state | state |
| any_state | 遍历全球所有州 | any_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state |
| any_state_in_<georegion_short_name> | 遍历指定地理区域中的所有州 | any_state_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state |
| any_state_region | 遍历所有州区域 | any_state_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state_region |
| any_state_region_in_<georegion_short_name> | 遍历指定地理区域中的所有州区域 | any_state_region_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state_region |
| any_strategic_objective | 遍历 scope 国家的所有战略目标州 | any_strategic_objective = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | state |
| any_strategic_region | 遍历全球所有战略区域 | any_strategic_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | strategic_region |
| any_strategic_region_in_<georegion_short_name> | 遍历指定地理区域中的所有战略区域 | any_strategic_region_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | strategic_region |
| any_subject_of_subject | 层级中直属附属国之下的任意国家 | any_subject_of_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_subject_or_below | 层级中当前国家之下的任意国家 | any_subject_or_below = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_supporting_character | 遍历支持 scope 政治运动的所有人物 | any_supporting_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_movement | character |
| any_treaty | 遍历所有条约（包括生效条约和草案） | any_treaty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | treaty |
| any_valid_mass_migration_culture | 列出 scope 国家中符合大规模迁移条件的文化 | any_valid_mass_migration_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | culture |
| any_war_participant | 遍历一场战争中的所有参战方 | any_war_participant = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | war | country |
| appeasement | 比较一个政治游说团的绥靖程度。 |  | political_lobby | value |
| approaching_bureaucracy_shortage | 检查国家的机构是否最终会出现行政力短缺 |  | country | boolean |
| arable_land | 检查州的可耕地 | arable_land > 10 | state | value |
| arable_land_country | 比较*所有*州的可耕地总量 | arable_land_country > 10 | country | value |
| armor | 比较一艘舰船的装甲 | armor >= 10 | ship | value |
| army_mobilization_option_fraction | 检查一个国家的陆军是否有一定比例的单位使用特定动员选项 | scope:country = { army_mobilization_option_fraction = { target = mobilization_option:key value >= 0.2 } } | country | value |
| army_power_projection | 与一个国家的总陆军力量投射进行比较 | scope:example_country = { army_power_projection < root.army_power_projection } | country | value |
| assert_if | 在运行时有条件地触发断言 | assert_if = { limit = { <triggers> } text = <string> (optional) } | none |  |
| assert_read | 在读取时有条件地触发断言 | assert_read = yes / <string> | none |  |
| authority | 比较 scope 国家的可用统治力 |  | country | value |
| authority_usage | 比较 scope 国家已消耗的统治力 |  | country | value |
| available_jobs | 检查该州非自给建筑中的可用职位数量 | available_jobs > 10000 | state | value |
| average_country_infrastructure | 检查 scope 国家拥有的所有州的平均基础设施 | average_country_infrastructure = 3 | country | value |
| average_incorporated_country_infrastructure | 检查 scope 国家拥有的已并入州的平均基础设施 | average_incorporated_country_infrastructure = 3 | country | value |
| average_sol_for_culture | 比较目标文化在该国家的平均生活水平 | average_sol_for_culture = { target = cu:polish value > 10 } | country | value |
| average_sol_for_primary_cultures | 比较主流文化的平均生活水平 |  | country | value |
| average_sol_for_religion | 比较目标宗教在该国家的平均生活水平 | average_sol_for_religion = { target = rel:catholic value > 10 } | country | value |
| average_sol_for_slaves | 比较被奴役人口的平均生活水平 |  | country | value |
| binds | 检查 scope 条约或 treaty_options 是否约束给定国家 | scope:some_treaty = { if = { limit = { binds = c:FRA binds = c:BEL } } } | treaty, treaty_options | country |
| blockade_level | 与该州的封锁程度进行比较 | blockade_level > 0.1 | state | value |
| building_has_goods_shortage | 检查建筑是否短缺其任一投入品 | building_has_goods_shortage = yes/no | building | boolean |
| bureaucracy | 比较 scope 国家的可用行政力 |  | country | value |
| bureaucracy_usage | 比较 scope 国家已消耗的行政力 |  | country | value |
| calc_true_if | 若指定数量的子 trigger 返回真则返回真 | calc_true_if = { amount = 2 <trigger> <trigger> <trigger> } | none |  |
| can_activate_production_method | 检查 scope 州中特定类型的建筑能否启用指定的生产方式 | can_activate_production_method = { building_type = <key> production_method = <key> } | state |  |
| can_afford_diplomatic_action | 检查 scope 国家能否负担指定外交行动（条约或持续性行动）所需的影响力 | can_afford_diplomatic_action = { target = <country scope> type = <diplomatic action key> } | country |  |
| can_agitate | 检查 scope 人物能否在目标国家进行鼓动 | can_agitate = <scope/c:TAG> | character | country |
| can_be_enacted | 检查一项法律能否被其国家在当前形势下颁布 | can_be_enacted = yes | law | boolean |
| can_break_diplomatic_pact | 检查 scope 国家与目标国家之间是否存在可废除的指定类型外交条约 | can_break_diplomatic_pact = { target = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> } | country |  |
| can_construct_building | 检查 scope 州中能否建造 1 级 <building_type> | can_construct_building = <building_type> | state |  |
| can_create_diplomatic_pact | 检查与另一个国家建立外交条约是否有效 | can_create_diplomatic_pact = { target = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> } | country |  |
| can_create_treaty | 检查国家之间能否创建条约 | can_create_treaty = { first_country = <country> # (default: none) must _not_ be specified if the created treaty is an amendment second_country = <country> # (default: none) must _not_ be specified if the created treaty is an amendment amends = <treaty> # (default: none) if specified, the created treaty will be an amendment to the specified treaty is_draft = yes \| no # (default: yes) must be yes if this treaty is an amendement to an existing treaty entered_into_force_on = <date> # (default: none) means "today" if not specified (for non-drafts). Must _not_ be specified for drafts. Cannot be in the future binding_period = { # (default: 0) must be a nonnegative number, fractional parts will be ignored (truncation) days = <nonnegative number> \| weeks = <nonnegative number> \| months = <nonnegative number> \| years = <nonnegative number> } articles_to_create = { # (default: empty) non-amendments must have at least one article to create { article = <key> # (default: empty) the type of article (determined by script) source_country = <country> # (default: none) directed articles _must_ specify this value, mutual articles _must not_ specify this value target_country = <country> # (default: none) directed articles _must_ specify this value, mutual articles _must not_ specify this value inputs = { # (default: empty) list of inputs values as required by the article { quantity = <positive number> \| good = <good> \| state = <state> \| strategic_region = <strategic region> \| company = <company> # TODO: or company type? \| building = <building> # TODO: or building type? \| law = <law> # TODO: or law type? \| country = <country> } { ... } # one input per required input of the corresponding article type } } # some examples of valid articles { article = alliance } # mutual, no inputs { article = resource_transfer # directed source_country = c:FRA # because directed target_country = c:GBR # because directed inputs = { { quantity = 250 } # because resource_transfer has required_inputs = { quantity good } { good = g:coal } # because resource_transfer has required_inputs = { quantity good } } } } } | none |  |
| can_decrease_autonomy | 检查一个附属国能否成为自治程度更低的附属国类型 | can_increase_autonomy = yes | country | boolean |
| can_establish_company | 检查该国家能否建立一家新公司 |  | country | boolean |
| can_form_nation | 检查目标国家是否有可能成立一个民族国家 | can_form_nation = <tag> | country |  |
| can_have_as_subject | 检查一个国家能否将另一个国家作为特定类型的附属国 | can_have_as_subject = { who = <country scope> type = <subject type key> } | country |  |
| can_have_subjects | 检查该国家能否拥有自己的附属国 |  | country | boolean |
| can_increase_autonomy | 检查一个附属国能否成为自治程度更高的附属国类型 | can_increase_autonomy = yes | country | boolean |
| can_invite_any_country | 检查是否有可能邀请任意国家加入该 scope 强权集团。 | can_invite_any_country = yes/no | power_bloc | boolean |
| can_leave_power_bloc | 检查 scope 国家能否离开其当前所在的强权集团（若国家不在任何强权集团中则返回假） | can_leave_power_bloc = yes | country | boolean |
| can_lobbies_target | 检查目标国家是否是 scope 国家政治游说团的有效目标 | can_lobbies_target = <target country scope> | country | country |
| can_own_autonomy_be_decreased | 检查 scope 国家的自治程度能否被降低 | can_own_autonomy_be_decreased = yes/no | country | boolean |
| can_potentially_produce_prestige_goods | 检查 scope 公司是否有潜力生产目标威望商品类型 | can_potentially_produce_prestige_good = pg:prestige_good_generic_clothes | company |  |
| can_queue_building_levels | 检查建筑的所有者能否在不触及等级或资源潜力上限的情况下排队建造指定数量的额外等级 | can_queue_building_levels = number | building |  |
| can_research | 若一个国家能研究某项技术则为真 | can_research = technology | country |  |
| can_send_diplomatic_action | 检查 scope 国家向目标国家发送某项外交行动是否有效 | can_send_diplomatic_action = { target = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> } | country |  |
| can_start_tutorial_lesson | 能否开始指定的教程课程？ | can_start_tutorial_lesson = reactive_advice_succession | none |  |
| can_take_on_scaled_debt | 检查 scope 国家能否从另一个国家承接一定数量的比例债务 | can_take_on_scaled_debt = { who = <country scope> value = <0-1 value> } | country |  |
| can_transfer_subject | 检查目标国家能否作为附属国被移交给 scope 国家 | scope:country = { can_transfer_subject = c:FRA } | country | country |
| can_trigger_event | 检查国家能否触发指定事件 | can_trigger_event = key | country |  |
| cash_reserves_available | 评估一个生产建筑的可用现金储备 | cash_reserves_available > 25000 | building | value |
| cash_reserves_ratio | 评估一个生产建筑的可用现金储备相对于其上限的比例。若建筑没有现金储备上限则返回 1 | cash_reserves_ratio > 0.2 | building | value |
| character_acceptance | 将 scope 人物在目标国家的认可度与一个认可值进行比较 | character_acceptance = { target = c:FRA value > 50 } | character | value |
| character_supports_political_movement | 检查 scope 人物是否支持某项政治运动 | character_supports_political_movement = yes/no | character | boolean |
| check_area | 将对象的面积与另一个对象进行比较 |  | country, market, province, state, state_region, strategic_region, theater |  |
| civil_war_progress | 比较内战的进度 | civil_war_progress > 0.50 | civil_war | value |
| commander_is_available | 检查一名指挥官是否空闲 | commander_is_available = bool | character | boolean |
| commander_rank | 比较指挥官的军衔 | commander_rank > 2 | character | value |
| company_employed_levels | 检查 scope 公司的已雇用建筑等级数量 | company_employed_levels > 1.5 | company | value |
| company_global_productivity_comparison | 检查与该公司建筑匹配的建筑的全球平均生产力，并按各类型的拥有等级加权 | company_global_productivity_comparison > 1.0 | company | value |
| company_has_building_type_monopoly | 检查 scope 公司是否垄断指定的建筑类型 | company_has_building_type_monopoly = bt:building_food_industry | company | building_type |
| company_has_monopoly | 检查 scope 公司是否拥有任意垄断 | company_has_monopoly = yes | company | boolean |
| company_is_prosperous | 检查一家公司是否被视为兴旺 |  | company | boolean |
| company_owned_levels | 检查 scope 公司的已拥有建筑等级数量 | company_owned_levels > 1.5 | company | value |
| company_productivity | 检查 scope 公司的生产力 | company_productivity > 1.0 | company | value |
| company_prosperity | 检查一家公司的兴旺程度 | company_prosperity > 0 | company | value |
| construction_queue_duration | 比较任意队列中所有建筑的极粗略估计剩余完工周数的最大值 | construction_queue_duration < 52 | country | value |
| construction_queue_government_duration | 比较政府队列中建筑的极粗略估计剩余完工周数 | construction_queue_government_duration < 52 | country | value |
| construction_queue_num_queued_government_levels | 比较建造队列中政府建造的建筑等级数量 |  | country | value |
| construction_queue_num_queued_levels | 比较建造队列中的建筑等级数量 |  | country | value |
| construction_queue_num_queued_private_levels | 比较建造队列中私人建造的建筑等级数量 |  | country | value |
| construction_queue_private_duration | 比较私人队列中建筑的极粗略估计剩余完工周数 | construction_queue_private_duration < 52 | country | value |
| contains_capital_of | 检查 scope 州区域是否包含目标 tag 的首都 | contains_capital_of = country scope/tag | state_region |  |
| controls_treaty_port_province | 检查 scope 州是否控制该州区域中的条约港地区 | controls_treaty_port_province = yes/no | state | boolean |
| could_support_political_movement | 检查一个人物是否有可能支持某项政治运动 | could_support_political_movement = <scope> | character |  |
| country_army_unit_type_fraction | 检查一个国家是否有一定比例的特定陆军单位类型 | scope:example_formation = { country_military_unit_type_fraction = { target = unit_type:key value >= 0.2 } } | country | value |
| country_average_cultural_acceptance | 将一个国家中某文化的平均认可度与一个值进行比较 | country_average_cultural_acceptance = { target = cu:french value >= 50 } | country | value |
| country_average_culture_and_religion_pop_acceptance | 国家人口对特定文化和宗教的平均接受度。 | country_average_culture_and_religion_pop_acceptance = { culture = cu:polish religion = rel:catholic value >=60 } | country | value |
| country_average_culture_pop_acceptance | 国家人口对特定文化的平均接受度。 | country_average_culture_pop_acceptance = { culture = cu:polish value >=60 } | country | value |
| country_average_religion_pop_acceptance | 国家人口对特定宗教的平均接受度。 | country_average_religion_pop_acceptance = { religion = rel:catholic value >=60 } | country | value |
| country_average_religious_acceptance | 将国家内某一宗教的平均接受度与一个数值进行比较 | country_average_religious_acceptance = { target = rel:catholic value >= 50 } | country | value |
| country_can_have_mass_migration_to | 检查 scope 所指国家能否向目标国家进行大规模迁移 | can_have_mass_migration_to = c:country | country | country |
| country_definition_has_culture | 检查某一文化是否属于该国定义中的文化之一 | country_definition_has_culture = <culture> | country_definition | culture |
| country_fervor_primary_culture | 与国家主流文化的最高狂热度进行比较 | country_fervor_primary_culture > 0.2 | country | value |
| country_has_building_group_levels | 检查国家内某一建筑组的建筑等级总和 | country_has_building_group_levels = { type = bg_heavy_industry value >= 100 } | country | value |
| country_has_building_levels | 检查国家的建筑等级总和 | country_has_building_levels >= 10 | country | value |
| country_has_building_type_levels | 检查国家内某一建筑类型的建筑等级总和 | country_has_building_type_levels = { target = bt:building_barracks value >= 100 } | country | value |
| country_has_building_type_monopoly | 检查 scope 所指国家是否垄断了指定的建筑类型 | country_has_building_type_monopoly = bt:building_food_industry | country | building_type |
| country_has_country_monopoly | 检查 scope 所指国家是否拥有任意国家垄断 |  | country | boolean |
| country_has_local_shortage | scope 所指市场商品在目标国家是否处于短缺状态 | country_has_local_shortage = scope:example_country | market_goods | country |
| country_has_primary_culture | 检查某一文化是否属于该国的主流文化之一 | country_has_primary_culture = <culture> | country | culture |
| country_has_state_religion | 检查某一宗教是否是该国的国教 | country_has_accepted_religion = <religion> | country | religion |
| country_innovation | 检查国家每周产出的创新数量 | country_innovation <= 200 | country | value |
| country_or_subject_owns_entire_state_region | 检查 scope 所指国家或其任意附属国是否拥有整个指定的州区域 | country_or_subject_owns_entire_state_region = key | country |  |
| country_ownership_fraction | 比较该建筑的等级中由某一国家拥有的比例 | country_ownership_fraction > 0.5 | building | value |
| country_rank | 比较一个国家的权力等级 | country_rank < rank_value:major_power | country | value |
| country_ship_type_fraction | 检查国家是否拥有特定舰船类型的某一百分比 | scope:example_formation = { country_ship_type_fraction = { target = unit_type:key value >= 0.2 } } | country | value |
| country_tier | 比较国家 tag 的层级 | country_tier = x | country |  |
| country_turmoil | 比较国家按人口加权的动荡值 | country_turmoil > 0.2 | country | value |
| crew | 比较一艘舰船的当前船员数 | crew >= 10 | ship | value |
| crew_percent | 比较一艘舰船的当前船员百分比 | crew_percent >= 0.1 | ship | value |
| cultural_acceptance_base | 将 scope 所指国家中某一文化因共享文化特质而获得的接受度与一个接受度数值进行比较 | cultural_acceptance_base = { target = cu:french value > 50 } | country | value |
| cultural_acceptance_delta | 比较 scope 所指州内某一文化接受度的当前本地增量（修正值） | cultural_acceptance_delta = { target = cu:romanian value < -10 } | state | value |
| culture_can_have_mass_migration_to_country | 检查 scope 所指文化能否向目标国家进行大规模迁移 | can_have_mass_migration_to_country = c:country | culture | country |
| culture_current_fervor | 比较某一文化的当前狂热度 | culture_current_fervor > 0.2 | culture | value |
| culture_has_community_in_state | 检查 scope 所指文化是否在某一州拥有文化社区。 | culture_has_community_in_state = <state> | culture |  |
| culture_has_national_awakening | 检查 scope 所指文化是否有正在进行中的民族觉醒 | culture_has_national_awakening = yes / no | culture | boolean |
| culture_national_awakening_occurred | 检查 scope 所指文化是否曾经启动过民族觉醒 | culture_national_awakening_occurred = yes / no | culture | boolean |
| culture_percent_country | 检查一个国家的人口中特定文化是否占某一百分比 | scope:example_country = { culture_percent_country = { target = cu:dixie value >= 0.2 } } | country | value |
| culture_percent_state | 检查一个州的人口中特定文化是否占某一百分比 | scope:example_state = { culture_percent_state = { target = cu:dixie value >= 0.2 } } | state | value |
| culture_secession_progress | 检查某一文化在一个国家中走向分裂的进度百分比。若该文化没有正在进行的分裂运动则为 0。 | culture_secession_progress = { target = scope:example_country value > 0.5 } | culture | value |
| culture_target_fervor | 比较某一文化的目标狂热度 | culture_target_fervor > 0.2 | culture | value |
| current_cohesion_number | 以数值形式比较当前凝聚力 | current_cohesion_number > 50 | power_bloc | value |
| current_cohesion_percentage | 以占 scope 所指强权集团凝聚力上限的百分比比较当前凝聚力 | current_cohesion_percentage > 0.5 | power_bloc | value |
| current_law_enactment_score | 检查 scope 所指国家当前正在颁布的法律的 AI 颁布评分 |  | country | value |
| current_manpower | 比较某一战斗方当前的可用人力 | manpower > 10000 | battle_side | value |
| current_tooltip_depth | 返回当前屏幕上打开的提示数量 |  | none | value |
| custom_description | 为其中的 trigger 提供自定义描述，而非自动生成的描述 | custom_description = { text = <trigger_localization_key> subject = <optional subject scope> #defaults to current scope object = <optional object scope> value = <optional script value> ... triggers ... } | none |  |
| custom_tooltip | 用自定义文本替换其中 trigger 的提示 | custom_tooltip = { text = <text> subject = <scope> (optional) <trigger> } | none |  |
| day_value | Day 值 |  | none | value |
| daynight_value | DayNight 值 |  | none | value |
| days_obsolete | 比较一艘舰船首次被 AI 标记为过时以来的天数。若该舰船从未被标记则返回 0。 | days_obsolete >= 1825 | ship | value |
| debug_log | 记录父级 trigger 成功或失败 |  | none |  |
| debug_log_details | 记录父级 trigger 成功或失败。并记录哪些子级成功或失败 |  | none |  |
| dependents | 比较 scope 所指人口的受抚养者数量 | dependents >= 2000 | pop | value |
| devastation | 比较某一州的荒废度 | devastation > 5 | state | value |
| discriminates_religion | 检查 scope 所指国家是否歧视给定的宗教（key） | discriminates_religion = <religion key/scope> | country | religion |
| earnings | 比较一栋建筑当前的人均年收益 | earnings >= 10 | building | value |
| economic_dependence | 比较 scope 所指国家对目标国家的依赖程度。**注意：这是一个开销较大的 trigger** | economic_dependence = { target = scope:other_country value > 2.2 } | country | value |
| election_momentum | 比较 scope 所指政党的选举势头与一个数值 | election_momentum = 0.75 | party | value |
| electoral_confidence | 比较 scope 所指国家的选举信心 | electoral_confidence > 0.1 | country | value |
| empty_agitator_slots | 检查一个国家中空缺的鼓动家槽位数量 | empty_agitator_slots >= 1 | country | value |
| enacting_any_law | 检查国家是否正在颁布任何法律。 | enacting_any_law = bool | country | boolean |
| enactment_chance | 比较 scope 所指国家当前的颁布几率，包括来自颁布修正器的数值 |  | country | value |
| enactment_chance_for_law | 比较 scope 所指国家对给定法律当前的颁布几率，包括来自颁布修正器的数值 | enactment_chance_for_law = { target = scope:my_lawtype value > 0.2 } | country | value |
| enactment_chance_for_law_without_enactment_modifier | 比较 scope 所指国家对给定法律的颁布几率，不包括来自颁布修正器的数值 | enactment_chance_for_law_without_enactment_modifier = { target = scope:my_lawtype value > 0.2 } | country | value |
| enactment_chance_without_enactment_modifier | 比较 scope 所指国家当前的颁布几率，不包括来自颁布修正器的数值 |  | country | value |
| enactment_phase | 比较 scope 所指国家当前的法律颁布阶段。 |  | country | value |
| enactment_setback_count | 比较 scope 所指国家当前的颁布挫折次数。 |  | country | value |
| enemy_contested_wargoals | 判定战争中敌方目前正在争夺的战争目标的比例 | enemy_contested_wargoals = { target = scope:war value > 0.4 } | country | value |
| enemy_occupation | 判定一个国家的（加权）敌方占领分 | enemy_occupation > 0.2 | country | value |
| escalation | 检查紧张升级是否已超过某一阈值 | escalation > -58 | diplomatic_play | value |
| exists | 检查指定的 scope 目标是否存在（即检查其不是 null 对象） | exists = from.owner.var:cool_var.mother | none |  |
| expanding_institution | 检查机构是否正在扩张 | expanding_institution = <scope/key> | country |  |
| experience_level | 比较人物的经验等级 | experience_level > 1 | character | value |
| export_advantage | 与州商品的出口优势进行比较 | export_advantage >= 100 | state_goods | value |
| export_tariff_level | 检查州商品是否设置了特定的出口关税等级 | export_tariff_level = max_tariffs | state_goods |  |
| fixed_expenses | 国家是否拥有这一数额的每周固定支出 | fixed_expenses > 1000 | country | value |
| fixed_income | 国家是否拥有这一数额的每周固定收入 | fixed_income > 1000 | country | value |
| food_security | 检查一个人口是否拥有一定数量的粮食安全 | food_security = value | pop | value |
| formation_army_unit_type_fraction | 检查一个编队是否拥有特定陆军单位类型的某一百分比 | scope:example_formation = { country_military_unit_type_fraction = { target = unit_type:key value >= 0.2 } } | military_formation | value |
| formation_ship_type_fraction | 检查一个编队是否拥有特定舰船类型的某一比例 | formation_ship_type_fraction = { target = ship_type:key value >= 0.2 } | military_formation | value |
| fraction_of_levels_owned_by_country | 比较一栋建筑的总等级中由某一国家或该国投资者拥有的比例 | fraction_of_levels_owned_by_country = { target = c:GBR value > 0.5 } | building | value |
| free_arable_land | 检查州内的可用耕地 | free_arable_land > 0 | state | value |
| free_principle_slots | 比较一个强权集团的空闲原则槽位数量 | power_bloc = { free_principle_slots >= 2 } | power_bloc | value |
| game_date | 与当前游戏日期进行比较 | game_date = 1837.1.1 | none | value |
| gdp_ownership_ratio | 比较指定国家在 scope 所指国家拥有的 GDP 比例 | gdp_ownership_ratio = { target = scope:owner_country value > 0.1 } | country | value |
| gdp_per_capita_ranking | 比较一个国家的人均 GDP 排名（名次） | gdp_per_capita_ranking > 42 | country | value |
| gdp_ranking | 比较一个国家的 GDP 排名（名次） | gdp_ranking > 42 | country | value |
| global_country_ranking | 比较一个国家的权力排名（名次） | global_country_ranking > 42 | country | value |
| global_population | 比较全球人口 | global_population > 2000000000 | none | value |
| global_variable_list_size | 检查全局变量列表的大小 | global_variable_list_size = { name = <variable name> value >= <value> } | none |  |
| global_variable_map_size |  | global_variable_map_size = { name = the name of the global map value >= script value or number } | none |  |
| gold_reserves | 国家是否拥有所需的黄金储备 | gold_reserves > 500 | country | value |
| gold_reserves_limit | 比较国家的黄金储备上限 | gold_reserves > gold_reserves_limit | country | value |
| goods_production_rank | 与一个国家某一商品的生产排行榜名次进行比较 | "goods_production_rank(g:luxury_clothes)" < 10 | country | value |
| government_legitimacy | 比较合法性 |  | country | value |
| government_transfer_of_power | 检查国家政府的权力移交 | government_transfer_of_power = key | country | value |
| government_wage_level | 比较 scope 所指国家的政府工资等级。`very_low, low, medium, high, very_high`；返回与 government_wage_level_value trigger 相同的数值 | government_wage_level = <level_term> | country | value |
| government_wage_level_value | 比较 scope 所指国家的政府工资等级值。`0, 1, 2, 3, 4` | government_wage_level_value = <level_num> | country | value |
| harvest_condition_intensity | 在收获条件 scope 下，比较给定国家中该收获条件的强度（因为州区域可能跨越多个国家） | harvest_condition_intensity = { target = scope:my_country_scope value > 0.5 } | harvest_condition | value |
| has_account_item | 玩家账户中是否拥有该物品 | has_account_item = <key> | none |  |
| has_active_building | 若一个州拥有某一处于活跃状态的建筑类型则为真 | has_active_building = building | market, state |  |
| has_active_peace_deal | 若国家正处于一场已有提议和平协议的战争中则为真 | has_active_peace_deal = bool | country | boolean |
| has_active_production_method | 检查 scope 所指建筑是否启用了指定的生产方式 | has_active_production_method = key | building |  |
| has_amendment | 检查 scope 所指法律是否带有给定类型的修正案 | has_amendment = <amendment type scope> | law | amendment_type |
| has_any_law_commitment | 检查国家是否有颁布任何法律的承诺 | has_any_law_commitment = yes | country | boolean |
| has_any_naval_only_hostilities | 检查国家是否与任何国家仅存在海军敌对状态（即未与其正式交战） | has_any_naval_only_hostilities = yes | country | boolean |
| has_any_secessionists_broken_out | 检查国家是否已有分裂分子爆发 |  | country | boolean |
| has_any_secessionists_growing | 检查国家是否有正在壮大的分裂分子 |  | country | boolean |
| has_any_strait_control | 检查 scope 所指国家是否拥有带海军要塞的海峡省份 | has_any_strait_control = yes | country | boolean |
| has_any_strait_province | 检查 scope 所指国家是否拥有任意海峡省份 | has_any_strait_province = yes | country | boolean |
| has_any_subventions_on | 检查 scope 所指国家是否对某一商品启用了任意等级的补贴 | scope:country = { has_any_subventions_on = <goods scope> } | country | goods |
| has_any_tariffs_on | 检查 scope 所指国家是否对某一商品征收了任意等级的关税 | scope:country = { has_any_tariffs_on = <goods scope> } | country | goods |
| has_assimilating_pops | 检查一个州是否有任何正处于同化过程中的人口。 |  | state | boolean |
| has_attitude | 检查 scope 所指国家对另一个国家是否持特定态度 | has_attitude = { who = <country scope> attitude = <attitude key> } | country |  |
| has_battle_condition | 若战斗方当前带有给定 key 的战斗条件则为真 | has_battle_condition = battle_condition_key | battle_side |  |
| has_building | 若一个州/市场/州区域/国家拥有某一建筑类型则为真 | has_building = building | country, market, state, state_region |  |
| has_character_ideology | 检查 scope 所指政治运动是否有人物意识形态 |  | political_movement |  |
| has_civil_war_from_movement_type | 检查一个国家是否正爆发由特定运动类型引发的内战 | has_civil_war_from_movement_type = <political_movement_type scope> | country | political_movement_type |
| has_claim | 检查 scope 所指国家是否对某州/州区域/国家拥有主张 | has_claim = <scope> | country |  |
| has_claim_by | 检查一个州是否被某一国家主张 | any_state = { owner = root has_claim_by = c:MEX } | state | country |
| has_commander_order | 检查 scope 所指人物是否正在执行给定的命令 | has_commander_order = order type key/order type scope | character |  |
| has_company | 检查 scope 所指国家中是否存在指定类型的公司 | has_company = <company_type scope> | country | company_type |
| has_completed_subgoal | 检查 scope 所指国家是否已完成某一子目标 | has_completed_subgoal = subgoal_key | country |  |
| has_consumption_tax | 检查国家是否对目标商品征收消费税。 | c:FRA = { has_consumption_tax = <goods scope> } | country | goods |
| has_converting_pops | 检查一个州是否有任何正处于转教过程中的人口。 |  | state | boolean |
| has_convoys_being_sunk | 检查国家是否有护航舰队正因袭击护航而被击沉 |  | country | boolean |
| has_core_ideology | 检查 scope 所指政治运动是否拥有核心意识形态 |  | political_movement |  |
| has_cosmetic_dlc | 客户端是否拥有该外观 DLC |  | none |  |
| has_cosmetic_dlc_feature | 客户端是否拥有启用该特定外观功能的 DLC |  | none |  |
| has_cultural_community | 检查某一文化是否在 scope 所指州拥有文化社区。 | has_cultural_community = <culture> | state |  |
| has_cultural_obsession | 检查某一文化是否痴迷于某一商品 | has_cultural_obsession = <goods key> | culture |  |
| has_culture | 检查人物的文化 | has_culture = culture scope or character scope | character |  |
| has_culture_graphics | 检查某一文化是否拥有特定的 culture_graphics | has_culture_graphics = <culture graphics key> | culture |  |
| has_decree | 检查 scope 所指州是否颁布了特定类型的法令 | has_decree = <key> | state |  |
| has_deployed_units | 检查一栋建筑是否支援了任何已部署到本土总部之外的单位 | has_deployed_units = yes/no | building | boolean |
| has_diplomatic_pact | 检查两个国家之间是否有某一类型的活跃外交协议 | has_diplomatic_pact = { who = <country scope> type = <diplomatic action key> is_initiator = yes/no } is_initiator 为可选参数，用于检查 scope 所指国家是否是该协议的最初发起方/目标方 | country |  |
| has_diplomatic_play | 检查战略区域是否有外交博弈 |  | strategic_region | boolean |
| has_diplomatic_relevance | 检查目标国家对 scope 所指国家是否具有外交相关性 | has_diplomatic_relevance = <scope> | country | country |
| has_diplomats_expelled | 检查 scope 所指国家是否最近驱逐了 event target 的外交官 | has_diplomats_expelled = country | country | country |
| has_discrimination_trait | 检查 scope 所指文化或宗教是否拥有给定的歧视特质 | has_trait = trait | culture, religion |  |
| has_discrimination_trait_group | 检查 scope 所指文化或宗教是否拥有给定的歧视特质组 | has_discrimination_trait_group = trait_group | culture, religion |  |
| has_dlc_feature | 主机是否拥有启用该特定功能的 DLC |  | none |  |
| has_employee_slots_filled | 检查某一 poptype 的雇员数量是否高于或低于该建筑当前可雇用总量的某一百分比。例如，一栋建筑的店主的雇用数是否达到其当前雇用容量的 80%（以 0.8 表示）。 | has_employee_slots_filled = { pop_type = <pop type> percent = <0-1 value> } | building |  |
| has_failed_hires | 检查一栋建筑上周是否雇用失败 | has_failed_hires = yes/no | building | boolean |
| has_famine | 检查州或国家是否发生饥荒 | has_famine = yes/no | country, state | boolean |
| has_free_government_reform | 检查国家是否拥有一次免费的（无激进派产生的）政府改革 | has_free_government_reform = <yes/no> | country | boolean |
| has_game_rule | 给定的游戏规则设置是否已启用？ | has_game_rule = faster_conversion | none |  |
| has_game_started | 若游戏已开始则为真 | has_game_started = bool | none | boolean |
| has_gameplay_dlc | 主机是否拥有该玩法 DLC |  | none |  |
| has_global_highest_gdp | 检查 scope 所指国家是否拥有最高 GDP | has_global_highest_gdp = yes/no | country | boolean |
| has_global_highest_innovation | 检查 scope 所指国家是否拥有最高的每周创新 | has_global_highest_innovation = yes/no | country | boolean |
| has_global_variable | 检查当前 scope 是否设置了指定的全局变量 | has_global_variable = name | none |  |
| has_global_variable_list | 检查当前 scope 是否设置了指定的全局变量列表 | has_global_variable_list = name | none |  |
| has_global_variable_map | 检查当前 scope 是否拥有指定的全局变量映射 | has_global_variable_map = name | none |  |
| has_government_clout | 国家政府是否拥有必要的政治力量总和 |  | country | value |
| has_government_type | 国家的政府类型是否如指定 | has_government_type = key | country |  |
| has_harvest_condition | 检查 scope 所指州区域是否有某一类型的收获条件 | has_harvest_condition = drought | state_region |  |
| has_healthy_economy | 检查国家是否拥有健康的经济 |  | country | boolean |
| has_high_attrition | 检查一个军事编队的损耗风险是否高于其类型的基础值 | has_high_attrition = bool | military_formation | boolean |
| has_homeland | 检查 scope 所指文化是否在目标州或州区域拥有家园 | has_homeland = state/state region | culture |  |
| has_identity | 检查 scope 所指强权集团是否拥有特定的中央认同 | has_identity = identity:key | power_bloc | power_bloc_identity |
| has_ideology | 检查 scope 所指人物或利益集团是否拥有意识形态 |  | character, interest_group, political_movement |  |
| has_inactive_journal_entry | 检查国家是否拥有至少一个指定类型的未激活日志条目 | has_inactive_journal_entry = key | country |  |
| has_institution | 检查 scope 所指国家是否拥有某一特定类型的机构 | has_institution = <scope/key> | country |  |
| has_insurrectionary_interest_groups | 检查国家是否拥有处于叛乱状态的利益集团 |  | country | boolean |
| has_interest_marker_in_region | 若 scope 所指国家在目标区域拥有利益标记则为真 | has_interest_marker_in_region = region scope/tag | country |  |
| has_journal_entry | 检查国家是否拥有至少一个指定类型的活跃日志条目 | has_journal_entry = key | country |  |
| has_label | 检查 scope 对象是否拥有指定的标签 | has_label = label_key | province |  |
| has_law | 检查国家是否已通过某项特定法律 |  | country | law_type |
| has_law_commitment | 检查国家是否承诺制定某项特定法律 |  | country | law_type |
| has_law_imposition_rights | 检查 scope 国家是否拥有必要许可，可要求另一个国家制定某项特定法律 | has_law_imposition_rights = { target_country = <country scope> type = <law type scope> } | country |  |
| has_law_or_variant | 检查国家是否已通过某项特定法律或其变体法律之一 |  | country | law_type |
| has_local_variable | 检查当前 scope 是否设置了指定的局部变量 | has_local_variable = name | none |  |
| has_local_variable_list | 检查当前 scope 是否设置了指定的局部变量列表 | has_local_variable_list = name | none |  |
| has_local_variable_map | 检查当前 scope 是否拥有指定的局部变量映射 | has_local_variable_map = name | none |  |
| has_map_interaction | 检查地图交互类型是否处于激活状态 | has_map_interaction = key | none |  |
| has_map_interaction_diplomatic_action | 检查当前的地图交互是否为特定的外交行动 | has_map_interaction_diplomatic_action = <key> | none |  |
| has_military_formation | 检查人物是否拥有军事编队 | has_military_formation = bool | character | boolean |
| has_mobilization_option | 检查编队是否拥有特定的动员选项 | has_mobilization_option = mobilization_option:key | military_formation | mobilization_option |
| has_mobilizing_unit | 检查 scope 州内的任意建筑是否保有任意正在动员的作战单位 | has_mobilizing_unit = bool | state | boolean |
| has_modifier | 检查受支持的 scope 是否拥有某个限时的 modifier | has_modifier = <key> | building, character, country, institution, interest_group, journal_entry, political_movement, power_bloc, state |  |
| has_naval_mission_with_invalid_area | 检查舰队是否有任务区域无效的海军任务 |  | military_formation | boolean |
| has_negotiated | 检查利益集团是否已完成谈判：has_negotiated = yes/no |  | interest_group | boolean |
| has_objective | 检查 scope 国家是否拥有某个特定类型的目标 | has_objective = objective_type_key | country |  |
| has_ongoing_assimilation | 检查 scope 人口是否有正在进行的同化 | has_ongoing_assimilation = yes | pop | boolean |
| has_ongoing_conversion | 检查 scope 人口是否有正在进行的宗教皈依 | has_ongoing_conversion = yes | pop | boolean |
| has_overlapping_interests | 检查 scope 国家是否与目标国家的任一利益存在重叠的利益标记 | has_overlapping_interests = <scope> | country | country |
| has_parent_law | 检查修正案类型是否有母法律 | has_parent_law = yes/no | amendment_type | boolean |
| has_party | 如果利益集团 scope 拥有政党则为真 | has_party = bool | interest_group | boolean |
| has_party_member | 检查目标利益集团是否为 scope 政党的成员 | has_party_member = <ig> | party | interest_group |
| has_play_goal | 检查外交博弈是否拥有某个战争目标类型 | has_play_goal = return_state | diplomatic_play |  |
| has_pop_culture | 检查人口是否拥有特定文化 | has_pop_culture = culture | pop |  |
| has_pop_religion | 检查人口是否拥有特定宗教 | has_pop_religion = religion | pop |  |
| has_port_country | 检查 scope 国家是否拥有至少一个港口 | has_port_country = yes/no | country | boolean |
| has_port_market | 检查 scope 市场是否拥有至少一个港口 | has_port_market = yes/no | market | boolean |
| has_port_state | 检查 scope 州是否拥有至少一个港口 | has_port = yes/no | state | boolean |
| has_possible_decisions | 检查国家是否有任何可行的决议 | has_possible_decisions = yes | country | boolean |
| has_potential_resource | 检查指定的建筑组是否被允许在 scope 州中存在。用于检查一个州是否有可能生产某种资源 | has_potential_resource = bg_rubber_plantations | state | building_group |
| has_potential_supply | 检查市场商品或州商品是否具有潜在供应，无论是通过本地生产还是理论上的进口 |  | market_goods, state_goods | boolean |
| has_potential_to_form_country | 检查目标国家是否有朝一日能够成立该国家 | has_potential_to_form_country = <tag> | country |  |
| has_power_struggle | 检查 scope 强权集团是否正在发生权力斗争 | has_power_struggle = yes/no | country | boolean |
| has_principle | 检查 scope 强权集团是否拥有某项原则 | has_principle = principle:key | power_bloc | power_bloc_principle |
| has_principle_group | 检查 scope 强权集团是否在指定的组中拥有原则 | has_principle_group = principle_group:key | power_bloc | power_bloc_principle_group |
| has_reached_end_date | 如果已到达结束日期（NDefines::NGame::END_DATE）则为真 | has_reached_end_date = yes | none | boolean |
| has_region_stance | 检查 scope 国家的 AI 对某个战略区域是否持指定立场 | region_stance = { region = sr:some_region stance = <conquer_region> } | country |  |
| has_religion | 检查人物的宗教 | has_religion = religion/character scope | character |  |
| has_religious_taboo | 检查某宗教是否将某种商品视为禁忌 | has_religious_taboo = <goods key> | religion |  |
| has_researchable_technology | 检查国家是否还有任何可研究的技术。 |  | country | boolean |
| has_revolution | 检查国家是否发生革命起义 |  | country | boolean |
| has_role | 检查人物是否拥有特定角色 | has_role = role | character |  |
| has_role_of_type | 检查人物是否拥有指定原型的角色 | has_role_of_type = archetype | character |  |
| has_ruling_interest_group | 该国的政府是否包含指定的利益集团 |  | country |  |
| has_ruling_interest_group_count | 该国的政府是否由指定数量的利益集团组成 |  | country | value |
| has_secret_goal | 检查 scope 国家是否对另一个国家抱有特定的秘密目标 | has_secret_goal = { who = <country scope> secret_goal = <secret_goal key> } | country |  |
| has_ship_outside_max_port_distance | 检查舰队是否有任何舰船超出其与港口的最大距离 |  | military_formation | boolean |
| has_social_class | 检查 scope 人口是否属于特定社会阶层 | has_social_class = <key> | pop |  |
| has_social_hierarchy | 检查 scope 国家是否采用了特定的社会等级制度 | has_social_hierarchy = <key> | country |  |
| has_state_in_state_region | 检查国家是否在该州区域内拥有一个州 | has_state_in_state_region = key | country |  |
| has_state_religion | 检查该人口是否信奉国教 |  | pop | boolean |
| has_state_trait | 检查 scope 州是否拥有某个特质 | has_state_trait = key | state |  |
| has_strategic_adjacency | 检查 scope 国家是否与目标州/国家存在战略相邻（直接/沿海/战争目标相邻） | has_strategic_adjacency = <scope> | country |  |
| has_strategic_land_adjacency | 检查 scope 国家是否与目标州/国家存在战略相邻（仅限直接陆地接壤或战争目标相邻） | has_strategic_adjacency = <scope> | country |  |
| has_strategic_region_interest_tier | 检查 scope 国家在特定战略区域中的利益层级排名 | has_strategic_region_interest_tier = { strategic_region = sr:target_region value >= 3 } | country |  |
| has_strategy | 检查 scope 国家是否有特定的 AI 策略 | has_strategy = <key> | country |  |
| has_subject_relation_with | 检查 scope 国家是否为 event target 的附属国或宗主国 | has_subject_relation_with = country | country | country |
| has_sufficient_construction_capacity_for_investment | 检查国家是否有足够的建造能力来花光其所有流入的投资池资金。 |  | country | boolean |
| has_technology_progress | 该国是否拥有某项技术所需的进度 | has_technology_progress = { technology = <technology key> progress = <0-1 value> } | country | value |
| has_technology_researched | 如果国家已研究出某项技术则为真 | has_technology_researched = <scope/key> | country |  |
| has_template | 检查人物是否由指定模板生成 | has_template = template_key | character |  |
| has_terrain | 检查省份是否拥有指定的地形类型 | has_terrain = terrain_key | province |  |
| has_trait | 检查人物是否拥有特定特质 | has_trait = trait | character |  |
| has_treaty_port_in_market | 检查 scope 国家是否在目标市场中拥有条约港 | c:POR = { has_treaty_port_in_market = c:CHI.market } | country | market |
| has_truce_with | 检查国家是否与另一个目标国家处于停战状态 | has_truce_with = c:GBR | country | country |
| has_type | 检查 scope 对象是否具有由给定字符串标识的类型 | scope:some_object = { has_type = defensive_pact } | treaty_article, treaty_article_options |  |
| has_unification_candidate | 检查该国家 tag 是否存在至少一个统一候选国 | has_country_unification_candidate = GER | none |  |
| has_unit_type | 检查作战单位是否为指定类型 | has_unit_type = unit_type:key | new_combat_unit | combat_unit_type |
| has_variable | 检查当前 scope 是否设置了指定的变量 | has_variable = name | none |  |
| has_variable_list | 检查当前 scope 是否设置了指定的变量列表 | has_variable_list = name | none |  |
| has_variable_map | 检查当前 scope 是否拥有指定的变量映射 | has_variable_map = name | none |  |
| has_war_exhaustion | 检查 scope 战争中目标国家的厌战度 | has_war_exhaustion = { target = c:GBR value > 50 } | war | value |
| has_war_goal | 检查战争是否拥有某个战争目标类型 | has_war_goal = return_state | war |  |
| has_war_support | 检查 scope 战争中目标国家的战争支持度 | has_war_support = { target = c:GBR value > 50 } | war | value |
| has_war_with | 检查 scope 国家是否与 event target 处于交战状态 | has_war_with = country | country | country |
| has_wasted_construction | 检查国家是否在浪费其任何已产出的建造。 |  | country | boolean |
| hidden_trigger | 所包含的 trigger 不会显示在工具提示中 | hidden_trigger = { <more triggers> } | none |  |
| highest_overlapping_interest_tier | 比较两国均设有利益的各战略区域中（scope 国家的）最高利益层级排名。 | highest_overlapping_interest_tier = { target = c:GBR value >= 2 } | country | value |
| highest_secession_progress | 比较给定国家中任何分离运动的最高分离进度 | highest_secession_progress > 0.7 | country | value |
| hit_points | 比较舰船的当前耐久值 | hit_points >= 10 | ship | value |
| hit_points_percent | 比较舰船的当前耐久值百分比 | hit_points_percent >= 0.1 | ship | value |
| ig_approval | 与 scope 利益集团的支持度比较 | ig_approval > 2 ig_approval < happy | interest_group | value |
| ig_clout | 与 scope 利益集团的政治力量比较 | ig_clout >= 0.2 | interest_group | value |
| ig_government_power_share | 与 scope 利益集团的政治力量除以政府总政治力量所得的份额比较 | ig_government_power_share >= 0.5 | interest_group | value |
| ig_state_pol_strength_share | 如果 scope 中的利益集团在该州拥有脚本化的政治力量则为真 | ig_state_pol_strength_share = { target = scope:target_ig value = 0.3 } | state | value |
| import_advantage | 与州商品进口优势比较 | import_advantage >= 100 | state_goods | value |
| import_tariff_level | 检查州商品是否设置了特定的进口关税等级 | import_tariff_level = max_tariffs | state_goods |  |
| in_default | 检查国家当前是否处于违约状态 |  | country | boolean |
| in_election_campaign | 检查国家是否处于竞选活动期间 | in_election_campaign = <yes/no> | country | boolean |
| income_transfer | 与该外交协定的基础收入转移比较 | income_transfer > 0.05 | diplomatic_pact | value |
| incorporation_progress | 检查州中的整合进度 | incorporation_progress > 0.25 | state | value |
| influence | 与 scope 国家的可用影响力比较 |  | country | value |
| influence_usage | 与 scope 国家已消耗的影响力比较 |  | country | value |
| infrastructure | 与给定州的基础设施数值比较 | infrastructure > 10 | state, state_region | value |
| infrastructure_delta | 与给定州的基础设施收支比较 | infrastructure_delta > 0 | state, state_region | value |
| infrastructure_usage | 与给定州的基础设施使用量数值比较 | infrastructure_usage > 10 | state, state_region | value |
| initiator_is | 检查外交博弈的发起者是谁 | initiator_is = country | diplomatic_play | country |
| institution_investment_level | 与某一机构的投资等级比较 | institution_investment_level = { institution = <key> value = <comparator value> } | country | value |
| interest_group_population | 与利益集团中的人口数量比较 | interest_group_population > 1000 | interest_group | value |
| interest_group_population_percentage | 与利益集团中的人口百分比比较 | interest_group_population_percentage > 0.2 | interest_group | value |
| interest_group_supports_political_movement | 检查 scope 利益集团是否支持某个政治运动 | interest_group_supports_political_movement = yes/no | interest_group | boolean |
| invasion_has_marines | 检查 scope 入侵行动的陆军中是否有任意作战单位为海军陆战队 | invasion_has_marines = bool | invasion | boolean |
| investment_pool | 该国的投资池中是否存有这么多资金 | investment_pool > 1000 | country | value |
| investment_pool_gross_income | 该国的投资池是否拥有这么多总收入（支出前的收入） | investment_pool_gross_income > 1000 | country | value |
| investment_pool_net_income | 该国的投资池是否拥有这么多净收入（支出后的收入） | investment_pool_net_income > 1000 | country | value |
| is_adjacent_to_country | 检查 scope 国家是否与目标国家相邻 | is_adjacent_to_country = <scope> | country | country |
| is_adjacent_to_market | 检查 scope 市场是否与目标市场相邻 | is_adjacent_to_market = <market scope> | market | market |
| is_adjacent_to_state | 检查 scope 国家是否与目标州相邻 | is_adjacent_to_state = <state scope> | country | state |
| is_adult | 检查人物是否为成年人 | is_adult = bool | character | boolean |
| is_advancing_on_front | 检查指挥官是否正在某条前线推进 | is_advancing_on_front = <front scope> | character | front |
| is_ai | 如果国家 scope 由 AI 控制则为真 | is_ai = bool | country | boolean |
| is_army | 检查军事编队是否为陆军 | is_army = bool | military_formation | boolean |
| is_at_war | 检查国家是否处于交战状态 |  | country | boolean |
| is_attacker_in_battle | 检查指挥官或舰船是否为某场战斗中的进攻方 | is_attacker_in_battle = bool | character, ship | boolean |
| is_auto_assigned | 检查人物角色是否为自动分配 | is_auto_assigned = bool | character_role | boolean |
| is_banning_goods | 检查国家是否正在禁止某种商品 | is_banning_goods = <goods key/scope> | country |  |
| is_being_bolstered | 检查 scope 运动是否正在受到鼓动 | is_being_bolstered = <yes>/<no> | political_movement | boolean |
| is_being_bombarded | 检查某州当前是否正被敌对舰队炮击港口 |  | state | boolean |
| is_being_suppressed | 检查 scope 运动是否正在受到压制 | is_being_suppressed = <yes>/<no> | political_movement | boolean |
| is_blockaded_by | 检查某州是否被某国封锁 |  | state | country |
| is_buildable | 检查建筑是否可建造 = yes（默认值） | is_buildable = yes/no | building | boolean |
| is_building_group | 如果 scope 是指定分组的建筑则为真 | building_group = building | building |  |
| is_building_type | 如果 scope 是指定类型的建筑则为真 | is_building_type = building | building |  |
| is_building_type_expanded | 检查特定 CBuildingType 的 CProductionMethodsPanelEntry 是否已展开 | is_building_type_expanded = <scope/key> | none |  |
| is_busy | 检查人物是否忙碌 | is_busy = bool | character | boolean |
| is_capital | 检查该州是否为所有者的首都 = bool |  | state | boolean |
| is_character_alive | 检查 scope 人物是否存活 | is_character_alive = bool | character | boolean |
| is_character_role | 检查 scope 人物角色是否为特定角色 | is_character_role = role | character_role |  |
| is_character_role_type | 检查人物角色是否为自动分配 | is_character_role_type = archetype | character_role |  |
| is_civil_war_type | 检查 scope 人物角色是否为特定原型 | is_civil_war_type = revolution / secession | civil_war |  |
| is_coastal | 检查该州是否与某个（不可通行的除外）海域接壤 | is_coastal = yes/no | state | boolean |
| is_company_type | 检查 scope 公司是否为指定类型 | is_company_type = <company_type scope> | company | company_type |
| is_considered_adjacent_due_to_wargoals | 检查 scope 国家是否因在已承诺的外交博弈中拥有与目标国家相邻的战争目标而被视为与目标国家相邻 | is_considered_adjacent_due_to_wargoals = <target country scope> | country | country |
| is_construction_paused | 检查某州的建造是否已暂停。 |  | country | boolean |
| is_consumed_by_government_buildings | 检查该市场商品是否为运转官僚机器所必需 |  | market_goods | boolean |
| is_consumed_by_military_buildings | 检查该商品是否为运转战争机器所必需 |  | market_goods | boolean |
| is_country_alive | 检查 scope 国家是否存活，即它在地图上是否至少拥有一个州且可与之互动 | is_country_alive = yes/no | country | boolean |
| is_country_type | 检查国家的类型 | is_country_type = country type | country |  |
| is_damaged | 检查舰船是否受损 | is_damaged = bool | ship | boolean |
| is_defender_in_battle | 检查指挥官或舰船是否为某场战斗中的防守方 | is_defender_in_battle = bool | character, ship | boolean |
| is_desired_by | 检查 scope 条约或条约选项与目标国家是否具有正向的固有接受度 | scope:treaty_article = { is_desired_by = c:FRA } | treaty_article, treaty_article_options | country |
| is_diplomatic_action_type | 检查外交协定是否为某种行动类型 | is_diplomatic_action_type = diplomatic action type | diplomatic_pact |  |
| is_diplomatic_catalyst_type | 检查外交催化剂是否为某种催化剂类型 | is_diplomatic_catalyst_type = diplomatic catalyst type | diplomatic_catalyst |  |
| is_diplomatic_pact_in_danger | 检查外交协定是否有破裂的危险 | is_diplomatic_pact_in_danger = yes | diplomatic_pact | boolean |
| is_diplomatic_play_ally_of | 检查 scope 国家是否与 event target 同处一场外交博弈 | is_diplomatic_play_ally_of = country | country | country |
| is_diplomatic_play_committed_participant | 如果国家是任一外交博弈的已承诺参与者则为真 | is_diplomatic_play_participant = bool | country | boolean |
| is_diplomatic_play_enemy_of | 检查 scope 国家是否在一场外交博弈中与 event target 敌对 | is_diplomatic_play_enemy_of = country | country | country |
| is_diplomatic_play_initiator | 如果国家是任一外交博弈的发起者则为真 | is_diplomatic_play_initiator = bool | country | boolean |
| is_diplomatic_play_involved_with | 检查 scope 国家是否与 event target 卷入同一场外交博弈 | is_diplomatic_play_involved_with = country | country | country |
| is_diplomatic_play_participant_with | 检查 scope 国家是否与 event target 同为同一场外交博弈的已承诺参与者 | is_diplomatic_play_participant_with = country | country | country |
| is_diplomatic_play_target | 如果国家是任一外交博弈的目标则为真 | is_diplomatic_play_target = bool | country | boolean |
| is_diplomatic_play_type | 检查外交博弈是否为某种类型 | is_diplomatic_play_type = play type | diplomatic_play |  |
| is_diplomatic_play_undecided_participant | 如果国家是任一外交博弈的未表态参与者则为真 | is_diplomatic_play_participant = bool | country | boolean |
| is_direct_subject_of | 检查 scope 国家是否为 event target 的直属附属国（而非附属国的附属国） | is_direct_subject_of = country | country | country |
| is_doing_piracy_in_region | 检查舰队是否正在指定的战略区域进行私掠 | is_doing_piracy_in_region = sr:region_baltic_sea | military_formation | strategic_region |
| is_employed | 检查该人口是否就业 |  | pop | boolean |
| is_enacting_law | 检查 scope 国家是否正在制定特定类型的法律。 | is_enacting_law = law_type:law_conscription | country | law_type |
| is_enforced | 检查 scope 条约是否对任一方强制执行 | scope:some_treaty = { if = { limit = { is_enforced = yes } } } | treaty | boolean |
| is_equal_exchange | 检查 scope 条约双方是否拥有相同的条约条款 | scope:some_treaty = { if = { limit = { is_equal_exchange = yes } } } | treaty, treaty_options | boolean |
| is_exchanging_obligations | 检查 scope 条约是否在交换任何义务， | scope:some_treaty = { is_exchanging_obligations= yes } | treaty, treaty_options | boolean |
| is_expanding_institution | 你是否正在扩张某一机构 | is_expanding_institution = <yes>/<no> | country | boolean |
| is_exported_to | scope 市场商品是否正由本地市场出口到目标市场 | is_exported_to = <market scope> | market_goods | market |
| is_female | 检查人物是否为女性 | is_female = bool | character | boolean |
| is_flagship | 检查 scope 舰船是否被指派为旗舰 | is_flagship = bool | ship | boolean |
| is_fleet | 检查军事编队是否为舰队 | is_fleet = bool | military_formation | boolean |
| is_forced_pact | 检查外交协定是否由于施压或义务等原因而有强制期限 |  | diplomatic_pact | boolean |
| is_forced_to_join_plays | 检查 scope 国家是否被迫加入目标国家的外交博弈 | is_forced_to_join_plays = c:country | country | country |
| is_fulfilled_by | 检查 scope 条约是否由给定国家履行 | scope:treaty = { is_fulfilled_by = c:FRA } | treaty | country |
| is_fully_mobilized | 检查军事编队是否已完全动员 | is_fully_mobilized = bool | military_formation | boolean |
| is_game_paused | 检查游戏是否暂停 | is_game_paused = yes/no | none | boolean |
| is_gamestate_tutorial_active | 游戏状态教程是否处于激活状态？参见 tutorial_lesson_chains 文档中的 save_progress_in_gamestate。 |  | none | boolean |
| is_giftable_to | 检查作用域内的条约条款（treaty article）或条款选项（article_options）是否可作为礼物赠予目标国家 | scope:treaty_article = { is_giftable_to = c:FRA } | treaty_article, treaty_article_options | country |
| is_goal_complete | 检查日志条目的目标是否已达成 | is_goal_complete = yes/no | journal_entry | boolean |
| is_government_funded | 检查建筑是否由政府出资 | is_government_funded = yes/no | building | boolean |
| is_heir_of_own_country | 检查作用域内的人物是否是其所在国家的继承人 | is_heir_of_own_country = yes / no | character | boolean |
| is_historical | 检查人物是否为历史人物 | is_historical = yes/no | character | boolean |
| is_historical_treaty | 检查作用域内的条约是否在游戏开始日期之前签署 | is_historical_treaty = yes/no | treaty, treaty_options | boolean |
| is_holder_of_wargoal_in_war | 检查指定国家是否是作用域内战争中任意战争目标的持有者 | is_holder_of_wargoal_in_war = <country> | war | country |
| is_home_country_for | 检查一个国家是否是目标国家的母国 |  | country | country |
| is_homeland | 检查作用域内的州区域是否为目标文化的本土（homeland） | is_homeland = culture scope/name | state_region |  |
| is_homeland_of_country_cultures | 检查州是否为目标国家任意主流文化的本土 | is_homeland_of_country_cultures = <country> | state | country |
| is_immortal | 检查作用域内的人物是否不朽 | scope:abbath = { is_immortal = yes } | character | boolean |
| is_immune_to_revolutions | 检查国家是否已通过 set_immune_to_revolutions 被设置为免疫革命。注意：这不会检查国家是否由于其他原因（例如其本身就是一个革命国家）而天然免疫革命，只针对 set_immune_to_revolutions 的效果。 is_immune_to_revolutions = yes/no | country | boolean |
| is_imported_from | 作用域内的市场商品是否正由本地市场从目标市场进口 | is_imported_from = <market scope> | market_goods | market |
| is_in_battle | 检查指挥官或舰船是否正在参与战斗 | is_in_battle = bool | character, ship | boolean |
| is_in_customs_union | 检查国家是否属于某个关税同盟 |  | country | boolean |
| is_in_customs_union_with | 检查国家是否与作用域内国家处于同一关税同盟 | is_in_customs_union_with = c:FRA | country | country |
| is_in_exile_pool | 检查作用域内的人物是否处于流亡者池中 | is_in_exile_pool = yes/no | character | boolean |
| is_in_geographic_region | 检查作用域内的对象是否位于特定地理区域 | is_in_geographic_region = <geographic_region scope> | country, state, state_region, strategic_region | geographic_region |
| is_in_government | 若利益集团作用域在政府中则为真 | is_in_government = bool | interest_group | boolean |
| is_in_list | 检查目标是否在列表中 |  | none |  |
| is_in_mild_starvation | 检查人口是否处于轻度饥荒 | is_in_mild_starvation = yes | pop | boolean |
| is_in_port | 检查舰船是否在港口中 | is_in_port = bool | ship | boolean |
| is_in_power_bloc | 检查国家是否属于某个强权集团 | is_in_power_bloc = yes/no | country | boolean |
| is_in_revolt | 检查州是否有任何机会分裂为革命国家或脱离国家 | is_in_revolt = yes/no。 | state | boolean |
| is_in_same_market_area | 检查作用域内的州是否与目标州处于同一市场区域 | is_in_same_market_area = <state scope> | state | state |
| is_in_same_power_bloc | 检查作用域内的国家是否与目标作用域国家处于同一强权集团 | is_in_same_power_bloc = c:GBR | country | country |
| is_in_severe_starvation | 检查人口是否处于严重饥荒 | is_in_severe_starvation = yes | pop | boolean |
| is_in_starvation | 检查人口是否处于饥荒（轻度或严重）状态 | is_in_starvation = yes | pop | boolean |
| is_in_void | 检查人物是否处于虚空（void）中 | is_in_void = bool | character | boolean |
| is_in_war_together | 检查作用域内国家是否与 event target 处于战争中的同一方 | is_in_war_together = country | country | country |
| is_incorporated | 检查州是否已被整合 = bool |  | state | boolean |
| is_indirect_subject_of | 检查作用域内国家是否是 event target 的间接附属国（附属国的附属国） | is_indirect_subject_of = country | country | country |
| is_insurrectionary | 检查国家、政治运动或利益集团是否处于起义状态 |  | country, interest_group, political_movement | boolean |
| is_interest_group_leader | 检查人物是否是其所在利益集团的领袖 | is_interest_group_leader = yes/no | character | boolean |
| is_interest_group_type | 检查利益集团是否为特定类型，也可直接用于人物 | is_interest_group_type = x | character, interest_group |  |
| is_invalid_naval_mission_grace_period_active | 检查舰队是否处于因海军任务无效而触发的宽限期内 | is_invalid_naval_mission_grace_period_active = yes/no | military_formation | boolean |
| is_invasion_stalled | 检查入侵是否因指挥官命令错误而停滞 | is_invasion_stalled = bool | invasion | boolean |
| is_involved_in_journal_entry | 检查国家是否参与了特定的日志条目 | is_involved_in_journal_entry = key | country |  |
| is_isolated_from_market | 检查州是否与其市场隔绝 |  | state | boolean |
| is_junior_in_customs_union | 若国家是关税同盟中的从属成员则为真 | is_junior_in_customs_union = bool | country | boolean |
| is_key_in_global_variable_map | 检查目标是否是全局变量映射（map）中的键 | is_key_in_global_variable_map = { name = name of the variable target = event target } | none |  |
| is_key_in_local_variable_map | 检查目标是否是局部变量映射中的键 | is_key_in_local_variable_map = { name = name of the variable target = event target } | none |  |
| is_key_in_variable_map | 检查目标是否是变量映射中的键 | is_key_in_variable_map = { name = name of the variable target = event target } | none |  |
| is_land_theater | 检查战区（theater）是否为陆地战区 | is_land_theater = bool | theater | boolean |
| is_largest_state_in_region | 检查州是否是其所在州区域中最大的州 = bool |  | state | boolean |
| is_lens_open | 检查特定镜头（lens）是否打开，以镜头键值指定。可指定一个可选的命名标签页来检查该标签页是否打开。 | is_lens_open = { lens = lens_key tab_name = tab_key } | none |  |
| is_local_player | 若国家作用域是本地玩家则为真 | is_local_player = bool | country | boolean |
| is_losing_power_rank | 检查国家是否正处于权力等级下降的过程中 |  | country | boolean |
| is_major_formation | 检查国家组建（country formation）是否为重大组建 | is_major_formation = yes | country_formation | boolean |
| is_marginal | 若利益集团作用域处于边缘地位则为真 | is_marginal = bool | interest_group | boolean |
| is_market_reachable_for_trade | 检查作用域内国家出于贸易目的能否到达指定的市场作用域 | is_market_reachable_for_trade = scope:my_market_scope | country | market |
| is_mass_migration_origin | 检查作用域内国家是否是大规模迁移的迁出地 | is_mass_migration_origin = yes | country | boolean |
| is_mass_migration_origin_of_culture | 检查作用域内国家是否是特定文化大规模迁移的迁出地 | is_mass_migration_origin_of_culture = cu:example_culture | country | culture |
| is_mass_migration_target | 大规模迁移的目的地是州。 | is_mass_migration_target = yes | state | boolean |
| is_mass_migration_target_for_culture | 作用域内的州是特定文化大规模迁移的目的地。 | is_mass_migration_target_for_culture = scope:my_culture | state | culture |
| is_member_of_any_lobby | 检查利益集团是否是任意政治游说团（lobby）的成员 | is_member_of_any_lobby = yes | interest_group | boolean |
| is_member_of_lobby | 检查利益集团是否是特定类型游说团的成员 | is_member_of_lobby = lobby_type:pro_country_lobby | interest_group | political_lobby_type |
| is_member_of_party | 检查利益集团是否是目标政党的成员 | is_member_of_party = <party> | interest_group | party |
| is_mobilized | 检查军事编队是否已被动员 | is_mobilized = bool | military_formation | boolean |
| is_monarch | 检查人物是否是实行世袭继承制的国家的君主 | is_monarch = bool | character | boolean |
| is_naval_invasion | 检查作用域内的入侵是否为海上入侵 | is_naval_invasion = bool | invasion | boolean |
| is_negotiating | 检查作用域内的国家或利益集团是否正在进行谈判。 |  | country, interest_group | boolean |
| is_noble | 检查人物是否为贵族 | is_noble = bool | character | boolean |
| is_not_in_geographic_region | 检查作用域内的对象是否不位于特定地理区域 | is_not_in_geographic_region = <geographic_region scope> | country, state, state_region, strategic_region | geograpic_region |
| is_objective_completed | 作用域内国家的目标（objective）是否已完成？ | is_objective_completed = yes | none | boolean |
| is_on_front | 检查人物或军事编队是否已被分配至某条前线并已抵达 | is_on_front = yes/no | character, military_formation | boolean |
| is_owed_obligation_by | 检查作用域内国家是否被目标国家欠有义务 | is_owed_obligation_by = c:FRA | country | country |
| is_panel_open | 检查特定信息面板是否打开，以 event target（target）或字符串（panel_name）指定。可指定一个可选的命名标签页（tab_name）来检查该标签页是否打开。 | is_panel_open = { target = <scope> OR panel_name = panel_name tab_name = tab_name } | none |  |
| is_party | 检查目标政党是否与作用域内政党相同。只对完全相同的政党对象有效，即不能跨国家比较。 | is_party = <party> | party | party |
| is_party_type | 检查作用域内政党的类型是否为指定类型 | is_party_type = party_type_database_key | party |  |
| is_player | 若国家作用域是玩家则为真 | is_player = bool | country | boolean |
| is_political_lobby_type | 检查政治游说团是否为特定游说团类型 | is_political_lobby_type = political lobby type | political_lobby |  |
| is_political_movement_type | 检查政治运动是否为特定类型 | is_political_movement_type = movement_to_enact | political_movement |  |
| is_pop_type | 检查人口是否为指定类型 | is_pop_type = poptype | pop |  |
| is_popup_open | 检查指定的弹窗面板是否打开 | is_popup_open = popup | none |  |
| is_potential_treaty_port | 检查作用域内的州是否有潜力成为目标国家的条约港 | is_potential_treaty_port = c:FRA | state | country |
| is_power_bloc_leader | 检查国家是否是某个强权集团的领袖 | is_power_bloc_leader = yes/no | country | boolean |
| is_powerful | 若利益集团作用域具有影响力则为真 | is_powerful = bool | interest_group | boolean |
| is_primary_culture_of | 检查文化是否是某个国家的主流文化之一 | is_primary_culture_of = <country> | culture | country |
| is_producing_prestige_goods | 检查作用域内的公司是否在生产威望商品 | is_producing_prestige_goods = yes | company | boolean |
| is_production_method_active | 检查作用域内州中特定类型的建筑是否启用了指定的生产方式 | is_production_method_active = { building_type = <key> production_method = <key> } | state |  |
| is_progressing | 检查日志条目是否正在推进 | is_progressing = yes/no | journal_entry | boolean |
| is_province_land | 检查省份是否位于陆地上 |  | province | boolean |
| is_reasonable_law_for_petition | 检查一项法律是否被认为合理到可由政府请愿颁布 | is_reasonable_law_for_petition = yes | law | boolean |
| is_renegotiation | 检查作用域内的条约是否是对现有条约的修订 | scope:some_treaty = { if = { limit = { is_renegotiation = yes } } } | treaty, treaty_options | boolean |
| is_researching_technology | 检查国家是否正在积极研究某项技术 | is_researching_technology = <scope/key/any> | country |  |
| is_researching_technology_category | 检查国家是否正在积极研究某个技术类别 | is_researching_technology_category = <key/any> | country |  |
| is_revolutionary | 检查国家、政治运动或利益集团是否具有革命性 |  | country, interest_group, political_movement | boolean |
| is_rightclick_menu_open | 检查指定的右键菜单是否打开 | is_rightclick_menu_open = <menu_key> | none |  |
| is_ruler_of_any_country | 检查人物是否是任意国家的统治者／国家元首 | is_ruler_of_any_country = bool | character | boolean |
| is_ruler_of_other_country | 检查人物是否是其并未居住的某个国家的统治者／国家元首 | is_ruler_of_other_country = bool | character | boolean |
| is_ruler_of_own_country | 检查人物是否是其居住国家的统治者／国家元首 | is_ruler_of_own_country = bool | character | boolean |
| is_same_interest_group_type | 检查利益集团是否与目标属于同一利益集团类型 | is_interest_group_type = scope:neighbor_leading_ig | interest_group | interest_group |
| is_same_law_group_as | 检查作用域内的法律类型是否与目标法律类型作用域属于同一法律组 | is_same_law_group_as = <law type scope> | law_type | law_type |
| is_same_party_type | 检查政党是否与目标属于同一政党类型 | is_same_party_type_as = scope:neighboring_party | party | party |
| is_sea_adjacent | 检查州是否与海洋区域相邻（普通或不可通行的海域） | is_sea_adjacent = yes/no | state | boolean |
| is_secessionist | 检查国家、政治运动或利益集团是否主张分离主义 |  | country, interest_group, political_movement | boolean |
| is_set | 检查指定的 scope 目标是否已被设置（包括为 null 对象的情况） | is_set = from.owner.var:cool_var.mother | none |  |
| is_ship_type | 检查作用域内的舰船是否为指定类型 | is_ship_type = ship_type:ship_type_frigate | ship | ship_type |
| is_slave_state | 检查州是否正在使用或有可能使用奴隶。 |  | state | boolean |
| is_split_state | 检查作用域内的州是否为被分割的州。 | scope:example_state = { is_split_state = yes } | state | boolean |
| is_state_region_land | 检查州区域是否位于陆地上 |  | state_region | boolean |
| is_state_religion | 检查宗教是否是某个国家的国教 | is_accepted_religion = <country> | religion | country |
| is_strategic_objective | 检查作用域内的州是否是某个国家的战略目标 | is_strategic_objective = <country> | state | country |
| is_strongest_ig_in_government | 检查作用域内的利益集团是否在政府所有利益集团中拥有最多的政治力量 | is_strongest_ig_in_government = yes/no | interest_group | boolean |
| is_subject | 若国家是附属国则为真 | is_subject = bool | country | boolean |
| is_subject_of | 检查作用域内国家是否是 event target 的附属国（或附属国的附属国） | is_subject_of = country | country | country |
| is_subject_type | 检查国家的附属国类型 | is_subject_type = subject type | country |  |
| is_subsidized | 检查建筑是否正在接受补贴 | is_subsidized = yes/no | building | boolean |
| is_subsistence_building | 检查建筑是否为自给建筑 | is_subsistence_building = yes/no | building | boolean |
| is_supporting_unification_candidate | 检查作用域内国家是否支持特定国家组建的统一候选人 | is_supporting_unification_candidate = { who = c:PRU country_formation = GER } | country |  |
| is_target_in_global_variable_list | 检查目标是否在全局变量列表中 | is_target_in_global_variable_list = { name = <variable name> target = <event target> } | none |  |
| is_target_in_local_variable_list | 检查目标是否在局部变量列表中 | is_target_in_local_variable_list = { name = <variable name> target = <event target> } | none |  |
| is_target_in_variable_list | 检查目标是否在变量列表中 | is_target_in_variable_list = { name = <variable name> target = <event target> } | none |  |
| is_target_of_wargoal | 检查州是否是涉及特定国家的战争中任意战争目标的目标 | has_war_goal = <country> | state | country |
| is_target_of_wargoal_in_war | 检查指定国家是否是作用域内战争中任意战争目标的目标 | is_target_of_wargoal_in_war = <country> | war | country |
| is_taxing_goods | 检查国家是否正在对某种商品征税 | has_embargo = <goods key/scope> | country |  |
| is_template_used | 检查人物模板是否已被使用 | is_template_used = template_key | none |  |
| is_theme_selected | 玩家是否在设置中选中了该主题 | is_theme_selected = <key> | none |  |
| is_tradeable | 检查商品或市场商品是否可交易 | is_tradeable = yes/no | goods, market_goods | boolean |
| is_treaty_article_in_danger | 检查条约条款是否有失效的危险 | is_treaty_article_in_danger = yes | treaty_article | boolean |
| is_treaty_port | 检查作用域内的州是否为条约港 | is_treaty_port = yes/no | state | boolean |
| is_tutorial_active | 教程是否处于激活状态？ |  | none | boolean |
| is_tutorial_lesson_active | 这是否是当前的教程课程？ | is_tutorial_lesson_active = reactive_advice_succession | none |  |
| is_tutorial_lesson_chain_completed | 指定键值的教程课程链是否已完成？ |  | none |  |
| is_tutorial_lesson_completed | 指定名称的教程课程是否已完成？ |  | none |  |
| is_tutorial_lesson_step_completed | 教程课程步骤是否已完成？ | is_tutorial_lesson_step_completed = lesson_key:step_key | none |  |
| is_under_colonization | 检查州是否正在被殖民 | is_under_colonization = yes/no | state | boolean |
| is_under_construction | 检查建筑是否正在建设中 | is_under_construction = bool | building | boolean |
| is_unification_candidate | 检查作用域内国家是否是特定国家标签的统一候选人 | is_unification_candidate = GER | country |  |
| is_value_in_global_variable_map | 检查目标是否是全局变量映射中的值 | is_value_in_global_variable_map = { name = name of the variable target = event target } | none | none |
| is_value_in_local_variable_map | 检查目标是否是局部变量映射中的值 | is_value_in_local_variable_map = { name = name of the variable target = event target } | none | none |
| is_value_in_variable_map | 检查目标是否是变量映射中的值 | is_value_in_variable_map = { name = name of the variable target = event target } | none | none |
| is_violating_sovereignty_of | 检查作用域内的国家是否正在侵犯目标国家的主权 | is_violating_sovereignty_of = c:GBR | country | country |
| is_vulnerable_front | 作用域内的前线在目标一侧是否既没有任何营也没有任何将军，且敌方至少有一名将军。 | is_vulnerable_front = scope:example_country | front | country |
| is_war | 若外交博弈已升级为战争则为真 | is_war = bool | diplomatic_play | boolean |
| is_war_participant | 检查目标国家是否是一场战争的参战方 |  | war | country |
| is_warleader | 检查国家是否是战争中的战争领袖 |  | war | country |
| is_world_market_hub | 检查州是否为世界市场枢纽 | is_world_market_hub = yes | state | boolean |
| isolated_states | 比较孤立州的数量 |  | country | value |
| journal_entry_age | 返回日志条目自激活以来的天数（即其存在时长） | journal_entry_age > 720 | journal_entry | value |
| law_approved_by | 检查作用域内的法律是否被某个利益集团认可 | law_approved_by = ig_rural_folk | law |  |
| law_enactment_stance | 比较作用域内人物、政治运动或利益集团对颁布指定法律的立场，并与同组当前生效法律进行比较 |  | character, interest_group, political_movement |  |
| law_is_available | 检查法律在其国家当前形势下是否可用。类似于 can_be_enacted，但忽略政府支持度 | law_is_available = yes | law | boolean |
| law_progressiveness_difference | 比较作用域内法律类型与目标法律类型的进步度差异，数值越高差异越大 | "law_progressiveness_difference(scope:target_law)" > 50 | law_type | value |
| law_stance | 比较作用域内人物、政治运动或利益集团对指定法律的基础立场，忽略同组当前生效法律 |  | character, interest_group, political_movement |  |
| leading_producer_of | 检查国家是否是某种商品的最大生产国 | leading_producer_of = g:luxury_clothes | country | goods |
| leads_customs_union | 检查是否有其他国家属于该国的关税同盟 | leads_customs_union = bool | country | boolean |
| levels_owned_by_country | 比较某国或该国投资者在某建筑中拥有的等级数 | levels_owned_by_country = { target = c:GBR value >= 1 } | building | value |
| leverage_advantage | 检查强权集团与目标国家之间的杠杆优势是否满足条件 | power_bloc = { leverage_advantage = { target = c:BEL value > 0 } } | power_bloc | value |
| liberty_desire | 作用域内国家独立倾向值的比较 trigger。 | liberty_desire > 50 | country | value |
| liberty_desire_weekly_progress | 作用域内国家独立倾向每周进展值的比较 trigger。 | liberty_desire_weekly_progress > 0 | country | value |
| liberty_desire_weekly_progress_from_support_independence | 作用域内国家因独立受到支持而产生的独立倾向每周进展值的比较 trigger。 | liberty_desire_weekly_progress_from_support_independence > 0 | country | value |
| lifetime_piracy_income | 比较人物一生中的海盗收入 | lifetime_piracy_income >= 1000000 | character | value |
| list_size | 检查列表的大小 | list_size = { name = <list name> value >= <value> } | none | value |
| literacy_rate | 检查人口、州或国家是否拥有一定的识字率 | literacy = value | country, pop, state | value |
| lobby_clout | 与作用域内游说团下属利益集团的政治力量总和比较 | lobby_clout >= 0.2 | political_lobby | value |
| lobby_formation_reason | 检查作用域内的外交催化剂（diplomatic catalyst）或政治游说团作用域的游说团成立原因 | lobby_formation_reason = diplomacy | diplomatic_catalyst, political_lobby |  |
| local_variable_list_size | 检查局部变量列表的大小 | local_variable_list_size = { name = <variable name> value >= <value> } | none |  |
| local_variable_map_size |  | local_variable_map_size = { name = the name of the local map value >= script value or number } | none |  |
| loyalist_fraction | 比较州或国家中人口的忠诚派比例，除 value 外所有参数均为可选 | loyalist_fraction = { value = <script_value> pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> } | country, state | value |
| loyalists | 比较给定州的忠诚度，即忠诚派所占比例 | loyalists > 0.2 | state | value |
| loyalty | 比较人物的忠诚度 | loyalty > 1 | character | value |
| market_access | 检查作用域内州的市场接入 | market_access > 0.8 | state | value |
| market_consumption_share | 比较作用域内市场来自目标国家的消费占比 | market_consumption_share = { target = <country scope> goods = key（可选） value > 0.5 } | market | value |
| market_exports | 比较 scope 市场向目标市场（若已设置）或世界市场（若未指定市场）出口的总单位数 | market_exports = { target = market scope (optional) goods = key (optional) value > 100 } | market | value |
| market_exports_reliance | 比较 scope 市场中由向目标市场（若已设置）或世界市场（若未指定市场）出口所产生的买单所占比例 | market_exports_reliance = { target = market scope (optional) goods = key (optional) value > 0.5 } | market | value |
| market_goods_buy_orders | 检查市场商品是否具有指定数量的买单 | market_goods_buy_orders < <value> | market_goods | value |
| market_goods_cheaper | 检查市场商品是否至少比基准价格便宜指定百分比 | market_goods_cheaper > <value> | market_goods | value |
| market_goods_consumption | 检查市场商品是否具有指定数量的总消费 | market_goods_consumption < <value> | market_goods | value |
| market_goods_delta | 检查市场是否具有指定的商品增量 (production + imports) - (consumption + exports) | market_goods_delta < <value> | market_goods | value |
| market_goods_export_share | 检查市场商品出口是否占世界市场出口的指定比例 | market_goods_export_share < <value> | market_goods | value |
| market_goods_exports | 检查市场商品是否具有指定数量的出口 | market_goods_exports < <vaue> | market_goods | value |
| market_goods_has_goods_shortage | 检查市场商品在市场中是否存在短缺 | market_goods_has_goods_shortage = yes/no | market_goods | boolean |
| market_goods_import_share | 检查市场商品进口是否占世界市场进口的指定比例 | market_goods_import_share < <value> | market_goods | value |
| market_goods_imports | 检查市场商品是否具有指定数量的进口 | market_goods_imports < <value> | market_goods | value |
| market_goods_pricier | 检查市场商品是否至少比基准价格贵指定百分比 | market_goods_pricier > <value> | market_goods | value |
| market_goods_production | 检查市场商品是否具有指定数量的总生产 | market_goods_production < <value> | market_goods | value |
| market_goods_sell_orders | 检查市场商品是否具有指定数量的卖单 | market_goods_sell_orders < <value> | market_goods | value |
| market_goods_shortage_ratio | 比较市场商品在其市场中的短缺比率 | market_goods_shortage_ratio > 0.33 | market_goods | value |
| market_has_goods_shortage | 检查市场的任何建筑投入品是否存在短缺 | market_has_goods_shortage = yes/no | market | boolean |
| market_imports | 比较目标市场向 scope 市场进口的总单位数 | market_imports = { target = market scope (optional) goods = key (optional) value > 100 } | market | value |
| market_imports_reliance | 比较 scope 市场中由从目标市场（若已设置）或世界市场（若未指定市场）进口所产生的买单所占比例 | market_imports_reliance = { target = market scope (optional) goods = key (optional) value > 0.5 } | market | value |
| market_number_goods_shortages | 检查市场在其任何建筑投入品上有多少短缺 | market_number_goods_shortages >= 2 | market | value |
| market_number_goods_shortages_with | 检查市场在其任何建筑投入品上有多少短缺，再加上来自目标国家的短缺 | "market_number_goods_shortages_with(scope:target)" >= 2 | market | value |
| market_number_goods_shortages_without | 检查市场在其任何建筑投入品上有多少短缺，减去来自目标国家的短缺 | "market_number_goods_shortages_without(scope:target)" >= 2 | market | value |
| market_prestige_goods_buy_orders | 比较市场中特定威望商品类型的买单 | market_prestige_goods_buy_orders = { type = <prestige_good_type> value >= <amount> } | market_goods | value |
| market_prestige_goods_consumption | 比较市场中特定威望商品类型的消费值 | market_prestige_goods_consumption = { type = <prestige_good_type> value >= <amount> } | market_goods | value |
| market_prestige_goods_delta | 比较市场中特定威望商品类型的增量（卖单 - 买单） | market_prestige_goods_delta = { type = <prestige_good_type> value >= <amount> } | market_goods | value |
| market_prestige_goods_export_share | 比较市场中特定威望商品类型的世界市场出口份额 | market_prestige_goods_export_share = { type = <prestige_good_type> value >= <amount> } | market_goods | value |
| market_prestige_goods_exports | 比较市场中特定威望商品类型的出口值 | market_prestige_goods_exports = { type = <prestige_good_type> value >= <amount> } | market_goods | value |
| market_prestige_goods_import_share | 比较市场中特定威望商品类型的世界市场进口份额 | market_prestige_goods_import_share = { type = <prestige_good_type> value >= <amount> } | market_goods | value |
| market_prestige_goods_imports | 比较市场中特定威望商品类型的进口值 | market_prestige_goods_imports = { type = <prestige_good_type> value >= <amount> } | market_goods | value |
| market_prestige_goods_production | 比较市场中特定威望商品类型的生产值 | market_prestige_goods_production = { type = <prestige_good_type> value >= <amount> } | market_goods | value |
| market_prestige_goods_sell_orders | 比较市场中特定威望商品类型的卖单 | market_prestige_goods_sell_orders = { type = <prestige_good_type> value >= <amount> } | market_goods | value |
| market_production_share | 比较来自目标国家的生产占 scope 市场生产的比例 | market_production_share = { target = <country scope> goods = key (optional) value > 0.5 } | market | value |
| market_trade | 比较 scope 市场与目标市场（若已设置）或世界市场（若未指定市场）之间交易的商品总单位数 | market_trade = { target = market scope (optional) goods = key (optional) value > 100 } | market | value |
| market_trade_reliance | 比较 scope 市场中由与目标市场（若已设置）或世界市场（若未指定市场）交易产生的买卖单所占比例 | market_trade_reliance = { target = market scope (optional) goods = key (optional) value > 0.5 } | market | value |
| max_contraventions | 检查 scope 条款或条款选项所属条款类型的最大违约次数 | scope:treaty_article = { max_contraventions >= 1 } | treaty_article, treaty_article_options | value |
| max_law_enactment_setbacks | 与国家在法律失败前可遭受的法律颁布挫折的最大次数进行比较 |  | country | value |
| max_num_companies | scope 国家被允许拥有的公司数量上限 | num_num_companies > 0 | country | value |
| military_ship_maintenance_fulfillment | 比较国家的军舰维护满足率 | military_ship_maintenance_fulfillment = <value> | country | value |
| military_wage_level | 比较 scope 国家的军队工资水平。`very_low, low, medium, high, very_high`；返回与 military_wage_level_value trigger 相同的数值 | military_wage_level = <level_term> | country | value |
| military_wage_level_value | 比较 scope 国家的军队工资水平值。`0, 1, 2, 3, 4` | military_wage_level_value = <level_num> | country | value |
| month | 与当前游戏日期的月份比较（1 月：0，12 月：11） | month > 10 | none | value |
| most_powerful_strata | 比较利益集团中最强大的阶层 |  | interest_group |  |
| most_prominent_revolting_interest_group | 检查 scope 州中最主要的叛乱利益集团是否为给定的利益集团类型。若 scope 州未处于叛乱状态则判定为 false。 | most_prominent_revolting_interest_group = ig_landowners | state |  |
| movement_can_cause_obstinance | 检查政治运动是否能在各州产生抗拒 | movement_can_cause_obstinance = yes | political_movement | boolean |
| movement_is_causing_obstinance | 检查政治运动是否在任何州引起抗拒 | movement_is_causing_obstinance = no | political_movement | boolean |
| movement_pressure | 比较 scope 运动对目标利益集团施加的压力 | "movement_pressure(ig:ig_intelligentsia)" > 0.1 | political_movement | value |
| nand | 取反的 AND trigger 若所有包含的 trigger 均返回 true 则返回 false；在遇到第一个为 false 的子 trigger 时返回 true |  | none |  |
| nationalization_cost | 比较将 scope 国家中由目标国家的政府或人口拥有的所有建筑国有化的总成本 | nationalization_cost = { target = scope:other_country value > 100000 } | country | value |
| naval_power_projection | 与国家的海军总力量投射进行比较 | scope:example_country = { naval_power_projection < root.naval_power_projection } | country | value |
| neighbors_any_power_bloc | 检查 scope 国家是否与任何强权集团相邻。注意：scope 国家不被视为与自身所属的强权集团（若有）相邻 | neighbors_any_power_bloc = yes/no | country | boolean |
| neighbors_member_of_same_power_bloc | 检查 scope 国家是否与属于同一强权集团的任何其他国家相邻 | neighbors_member_of_same_power_bloc = yes/no | country | boolean |
| neighbors_power_bloc | 检查 scope 国家是否与目标强权集团相邻。注意：scope 国家不被视为与自身所属的强权集团（若有）相邻 | neighbors_power_bloc = c:PRU.power_bloc | country | power_bloc |
| net_fixed_income | 国家在扣除支出后是否有此数额的收入（仅计固定收入与支出） | net_fixed_income > 1000 | country | value |
| net_total_income | 国家在扣除支出后是否有此数额的收入（计入全部收入与支出） | net_total_income > 1000 | country | value |
| night_value | 夜晚值 |  | none | value |
| nor | 取反的 OR trigger 若所有包含的 trigger 均返回 false 则返回 true；在遇到第一个为 true 的 trigger 时返回 false |  | none |  |
| not | 对 trigger 内容取反 若所有包含的 trigger 均返回 false 则返回 true |  | none |  |
| num_casualties | 检查 scope 战争中的总伤亡人数 | num_casualties >= 5000 | war | value |
| num_companies | scope 国家拥有多少公司 | num_companies > 0 | country | value |
| num_contraventions | 检查 scope 条款是否有来自给定国家的给定次数的违约 | scope:treaty_article = { num_contraventions = { target = c:FRA value > 0 } } | treaty_article | value |
| num_country_casualties | 检查 scope 战争中目标国家的伤亡人数 | num_country_casualties = { target = country value < 5000 } | war | value |
| num_country_dead | 检查 scope 战争中目标国家的死亡人数 | num_country_dead = { target = country value < 5000 } | war | value |
| num_country_wounded | 检查 scope 战争中目标国家的受伤人数 | num_country_wounded = { target = country value < 5000 } | war | value |
| num_cultural_communities | 检查州中的文化社区数量 | num_cultural_communities > 5 | state | value |
| num_dead | 检查 scope 战争中的总死亡人数 | num_dead >= 5000 | war | value |
| num_diplomatic_pacts | 与国家指定类型的外交协约数量进行比较 | num_diplomatic_pacts = { type = <key> value < 10 } | country | value |
| num_front_casualties | 检查 scope 前线中目标国家的伤亡人数 | num_front_casualties = { target = country value < 5000 } | front | value |
| num_front_dead | 检查 scope 前线中目标国家的死亡人数 | num_front_dead = { target = country value < 5000 } | front | value |
| num_front_wounded | 检查 scope 前线中目标国家的受伤人数 | num_front_wounded = { target = country value < 5000 } | front | value |
| num_investments_of_type | 检查 scope 国家在其本国之外拥有的给定类型建筑等级数量。 | num_investments_of_type = { type = building_oil_rig value > 5 } | country | value |
| num_mobilized_units_in_theater | 确定在与 scope 战区相交的前线上，属于 scope 战区所有者或其盟友的已动员单位数量 | num_mobilized_units_in_theater > 25 | theater | value |
| num_political_lobbies | 与 scope 国家或利益集团中的政治游说团数量进行比较 | num_political_lobbies > 0 | country, interest_group | value |
| num_potential_resources | 检查州中允许的指定建筑类型的数量。若用于没有等级上限的建筑类型则会报错 | "num_potential_resources(building_rubber_plantation)" > 0 | state | value |
| num_power_bloc_members | 将强权集团的成员数量与一个值进行比较 | num_power_bloc_members >= 2 | power_bloc | value |
| num_power_bloc_states | 将强权集团中的州数量与一个值进行比较 | num_power_bloc_states >= 2 | power_bloc | value |
| num_provinces_in_theater | 确定 scope 战区中的省份数量 | num_provinces_in_theater > 10 | theater | value |
| num_subjects | 比较 scope 国家的附属国数量 | num_subjects = <value> | country | value |
| num_taxed_goods | 比较 scope 国家的消费税商品数量 | num_taxed_goods = <value> | country | value |
| num_wounded | 检查 scope 战争中的总受伤人数 | num_wounded >= 5000 | war | value |
| number_of_claims | 国家拥有的对外国州的声索数量 | number_of_claims > 0 | country | value |
| number_of_possible_decisions | 国家可采取的可能决策数量 | number_of_possible_decisions > 0 | country | value |
| obstinance | 比较州的抗拒值 | obstinance > 0.5 | state | value |
| occupancy | 评估建筑的当前使用率 | occupancy < 0.25 | building | value |
| or | 若所有包含的 trigger 均为 false 则返回 false 在遇到第一个为 true 的子 trigger 时返回 true |  | none |  |
| organization | 比较 scope 中军事编队的组织度 | organization <= define:NMilitary\|MILITARY_FORMATION_ORGANIZATION_MIN | military_formation | value |
| organization_target | 比较 scope 中军事编队的目标组织度 | organization_target < define:NMilitary\|MILITARY_FORMATION_ORGANIZATION_MAX | military_formation | value |
| overlord_can_decrease_subject_autonomy | 检查宗主国能否降低附属国的自治度 | overlord_can_decrease_subject_autonomy = bool | country | boolean |
| owes_obligation_to | 检查 scope 国家是否对 event target 负有义务 | owes_obligation_to = country | country | country |
| owns_entire_state_region | 检查国家是否拥有整个地区 | owns_entire_state_region = key | country |  |
| owns_treaty_port_in | 国家是否拥有指定州地区中的条约港 | owns_treaty_port_in = key | country |  |
| play_participant_has_war_goal_of_type_against | 检查 scope 国家在任何外交博弈中是否持有针对特定国家的特定类型的战争目标 | play_participant_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } | country |  |
| play_side_has_war_goal_of_type_against | 检查在任何外交博弈中与 scope 国家同阵营的任何国家是否持有针对特定国家的特定类型的战争目标 | play_side_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } | country |  |
| political_movement_identity_support | 比较具有正确文化/宗教认同的人口对政治运动的支持度 | political_movement_identity_support > 0.5 | political_movement | value |
| political_movement_military_support | 比较政治运动的军方支持度 | political_movement_military_support > 0.5 | political_movement | value |
| political_movement_popular_support | 比较政治运动的民众支持度 | political_movement_popular_support > 0.5 | political_movement | value |
| political_movement_radicalism | 比较政治运动的激进程度 | political_movement_radicalism > 50 | political_movement | value |
| political_movement_support | 比较政治运动的支持度 | political_movement_support > 0.5 | political_movement | value |
| political_movement_wealth_support | 比较政治运动的财富支持度 | political_movement_wealth_support > 0.5 | political_movement | value |
| political_strength_share | 检查某一人口类型、宗教或文化在国家或州中的政治力量份额。必须且只能指定 pop_type、religion 或 culture 中的一项。 | political_strength_share = { pop_type/religion/culture = <key/scope> value <compare operator> <value> } | country, state | value |
| politically_involved_ratio | 比较国家中参与政治的人口百分比 | politically_involved_ratio > 0.25 | country | value |
| pollution_amount | 比较州地区的污染 |  | state_region | value |
| pollution_generation | 比较州中所有建筑的总污染产生量 |  | state | value |
| pop_acceptance | 比较 scope 人口的接纳度与一个接纳值 | pop_acceptance > 50 | pop | value |
| pop_employment_building | 检查人口是否在特定建筑类型中工作 | pop_employment_building = building | pop |  |
| pop_employment_building_group | 检查人口是否在特定建筑类型中工作 | pop_employment_building = building | pop |  |
| pop_has_primary_culture | 检查人口的文化是否为主要文化 | pop_has_primary_culture = bool | pop | boolean |
| pop_loyalist_fraction | 比较人口中忠诚派数量与其总规模 | pop_loyalty_fraction < 0.5 | pop | value |
| pop_neutral_fraction | 比较人口中中立者（既非激进派也非忠诚派）数量与其总规模 | pop_neutral_fraction > 0.95 | pop | value |
| pop_radical_fraction | 比较人口中激进派数量与其总规模 | pop_radical_fraction > 0.25 | pop | value |
| pop_type_percent_country | 检查 scope 国家是否有 <percent> 比例的人口属于指定的人口类型 | scope:example_country = { pop_type_percent_country = { pop_type = <pop_type> percent <compare operator (<,>,= and so on)> <percent> } } | country | value |
| pop_type_percent_state | 检查州的人口中某一特定人口类型是否占指定百分比 | scope:example_state = { pop_type_percent_state = { target = pop_type:laborer value <= 0.8 } } | state | value |
| population_by_culture | 比较 scope 州中目标文化的当前人口 | population_by_culture = { target = cu:romanian value > 2500 } | state | value |
| potential_diplomatic_play_power_ratio | 检查潜在外交博弈中 scope 国家一方与目标国家一方的预期力量比 会尝试预测相关参与者的立场（若有），因此不仅仅检查“初始实力” potential_diplomatic_play_power_ratio = { type = dp_open_market target = c:BEL state = c:BEL.capital value > 1.0 } state 和 type 为可选，默认为对目标首都使用 dp_open_market | country | value |
| potential_income | 比较国家的潜在收入（每周收入加上税收浪费） | potential_income > 1000 | country | value |
| power_bloc_rank | 比较强权集团的排名 | power_bloc_rank <= 2 | power_bloc | value |
| power_bloc_share_gdp | 比较 scope 国家占其强权集团全部现有成员的 GDP 份额，若不在强权集团中则返回 -1 | power_bloc_share_gdp > 0.2 | country | value |
| power_bloc_share_gdp_with | 比较 scope 国家占其强权集团全部成员加上一个额外国家的 GDP 份额，若不在强权集团中则返回 -1 | "power_bloc_share_gdp_with(scope:country) > 0.2" | country | value |
| power_bloc_share_gdp_without | 比较 scope 国家占其强权集团全部成员减去其中一员的 GDP 份额，若不在强权集团中则返回 -1 | "power_bloc_share_gdp_without(scope:country) > 0.2" | country | value |
| power_bloc_share_power_projection | 比较 scope 国家占其强权集团全部成员的力量投射份额，若不在强权集团中则返回 -1 | power_bloc_share_power_projection > 0.2 | country | value |
| power_bloc_share_power_projection_with | 比较 scope 国家占其强权集团全部成员加上一个额外国家的力量投射份额，若不在强权集团中则返回 -1 | "power_bloc_share_power_projection_with(scope:country) > 0.2" | country | value |
| power_bloc_share_power_projection_without | 比较 scope 国家占其强权集团全部成员减去其中一员的力量投射份额，若不在强权集团中则返回 -1 | "power_bloc_share_power_projection_without(scope:country) > 0.2" | country | value |
| power_bloc_share_prestige | 比较 scope 国家占其强权集团全部成员的威望份额，若不在强权集团中则返回 -1 | power_bloc_share_prestige > 0.2 | country | value |
| power_bloc_share_prestige_with | 比较 scope 国家占其强权集团全部成员加上一个额外国家的威望份额，若不在强权集团中则返回 -1 | "power_bloc_share_prestige_with(scope:country) > 0.2" | country | value |
| power_bloc_share_prestige_without | 比较 scope 国家占其强权集团全部成员减去其中一员的威望份额，若不在强权集团中则返回 -1 | "power_bloc_share_prestige_without(scope:country) > 0.2" | country | value |
| power_bloc_total_leading_goods_producers | 比较有多少成员位列全球所有商品的领先生产者之中，并按其排名位置加权。排名第一的生产者权重为 MIN_SPOT_PRESTIGE_AWARD，其后每个名次的权重依次递减一。默认情况下即第 1 名计为 3，第 2 名计为 2，第 3 名计为 1，其他名次计为 0。 | power_bloc_total_leading_goods_producers > 15 | power_bloc | value |
| power_bloc_total_leading_goods_producers_with | 比较有多少成员位列全球所有商品的领先生产者之中并按其排名位置加权，再加上一个当前不在该强权集团中的额外国家。排名第一的生产者权重为 MIN_SPOT_PRESTIGE_AWARD，其后每个名次的权重依次递减一。默认情况下即第 1 名计为 3，第 2 名计为 2，第 3 名计为 1，其他名次计为 0。 | "power_bloc_total_leading_goods_producers_with(scope:target) > 15" | power_bloc | value |
| power_bloc_total_leading_goods_producers_without | 比较有多少成员位列全球所有商品的领先生产者之中并按其排名位置加权，再减去一个当前在该强权集团中的国家。排名第一的生产者权重为 MIN_SPOT_PRESTIGE_AWARD，其后每个名次的权重依次递减一。默认情况下即第 1 名计为 3，第 2 名计为 2，第 3 名计为 1，其他名次计为 0。 | "power_bloc_total_leading_goods_producers_without(scope:target) > 15" | power_bloc | value |
| power_bloc_worst_economic_dependence | 若在强权集团 scope 中使用，则比较对领袖经济依赖度最低的成员。 | power_bloc_worst_economic_dependence > 2.2 | power_bloc | value |
| power_bloc_worst_economic_dependence_with | 若在强权集团 scope 中使用，比较对领导者经济依赖度最低的成员国。 | power_bloc_worst_economic_dependence > 2.2 | power_bloc | value |
| power_bloc_worst_economic_dependence_without | 若在强权集团 scope 中使用，比较对领导者经济依赖度最低的成员国。 | power_bloc_worst_economic_dependence > 2.2 | power_bloc | value |
| power_bloc_worst_infamy | 若在强权集团 scope 中使用，比较恶名值最差（最高）的成员国的恶名值 | power_bloc_worst_infamy > 50 | power_bloc | value |
| power_bloc_worst_infamy_with | 若在强权集团 scope 中使用，比较恶名值最差（最高）的成员国的恶名值 | power_bloc_worst_infamy > 50 | power_bloc | value |
| power_bloc_worst_infamy_without | 若在强权集团 scope 中使用，比较恶名值最差（最高）的成员国的恶名值 | power_bloc_worst_infamy > 50 | power_bloc | value |
| power_bloc_worst_leader_relations | 若在强权集团 scope 中使用，比较与强权集团领导者关系值最差（最低）的成员国的关系值 | power_bloc_worst_leader_relations > 10 | power_bloc | value |
| power_bloc_worst_leader_relations_with | 若在强权集团 scope 中使用，比较与强权集团领导者关系值最差（最低）的成员国的关系值 | power_bloc_worst_leader_relations > 10 | power_bloc | value |
| power_bloc_worst_leader_relations_without | 若在强权集团 scope 中使用，比较与强权集团领导者关系值最差（最低）的成员国的关系值 | power_bloc_worst_leader_relations > 10 | power_bloc | value |
| power_bloc_worst_leader_religion_population_fraction | 若在强权集团 scope 中使用，比较成员国中信仰领导者宗教的人口比例最低值。 | power_bloc_worst_leader_religion_population_fraction > 10 | power_bloc | value |
| power_bloc_worst_leader_religion_population_fraction_with | 若在强权集团 scope 中使用，比较成员国中信仰领导者宗教的人口比例最低值。 | power_bloc_worst_leader_religion_population_fraction > 10 | power_bloc | value |
| power_bloc_worst_leader_religion_population_fraction_without | 若在强权集团 scope 中使用，比较成员国中信仰领导者宗教的人口比例最低值。 | power_bloc_worst_leader_religion_population_fraction > 10 | power_bloc | value |
| power_bloc_worst_liberty_desire | 若在强权集团 scope 中使用，比较独立倾向最差（最高）的成员国的独立倾向值 | power_bloc_worst_liberty_desire > 75 | power_bloc | value |
| power_bloc_worst_liberty_desire_with | 若在强权集团 scope 中使用，比较独立倾向最差（最高）的成员国的独立倾向值 | power_bloc_worst_liberty_desire > 75 | power_bloc | value |
| power_bloc_worst_liberty_desire_without | 若在强权集团 scope 中使用，比较独立倾向最差（最高）的成员国的独立倾向值 | power_bloc_worst_liberty_desire > 75 | power_bloc | value |
| power_bloc_worst_progressiveness_difference_government_type | 若在强权集团 scope 中使用，比较其治理原则与权力分配法律相对强权集团领导者的进步性差值最差（最高）的成员国的进步性总差值 | power_bloc_worst_progressiveness_compatibility_government_type > 100 | power_bloc | value |
| power_bloc_worst_progressiveness_difference_government_type_with | 若在强权集团 scope 中使用，比较其治理原则与权力分配法律相对强权集团领导者的进步性差值最差（最高）的成员国的进步性总差值 | power_bloc_worst_progressiveness_compatibility_government_type > 100 | power_bloc | value |
| power_bloc_worst_progressiveness_difference_government_type_without | 若在强权集团 scope 中使用，比较其治理原则与权力分配法律相对强权集团领导者的进步性差值最差（最高）的成员国的进步性总差值 | power_bloc_worst_progressiveness_compatibility_government_type > 100 | power_bloc | value |
| power_projection_value | 比较一艘船只的力量投射值 | power_projection_value >= 10 | ship | value |
| predicted_cohesion_percentage_with | 预测强权集团（以 1 为分数）在将目标国家纳入为成员时的凝聚力 | predicted_cohesion_percentage_with, = { target = scope:other_country value > 0.9 } | power_bloc | value |
| prefers_law | 检查 scope 中的利益集团是否更偏好指定的法律而非用于比较的法律 | prefers_law = { law = law_type:<law a> comparison_law = law_type:<law b> } | interest_group |  |
| prestige | 比较威望 |  | country | value |
| primary_cultures_percent_country | 检查一个国家的人口中主体文化所占的百分比 | scope:example_country = { primary_cultures_percent_country >= 0.2 } | country | value |
| primary_cultures_percent_state | 检查一个州的人口中该国主体文化所占的百分比 | scope:example_state = { primary_cultures_percent_state >= 0.2 } | state | value |
| primary_role | 检查人物的主要角色是否为指定角色 | primary_role = role | character |  |
| private_ownership_fraction | 比较该建筑的等级中私人所有的比例 | private_ownership_fraction > 0.5 | building | value |
| produced_authority | 比较 scope 中国家产出的统治力 |  | country | value |
| produced_bureaucracy | 比较 scope 中国家产出的行政力 |  | country | value |
| produced_influence | 比较 scope 中国家产出的影响力 |  | country | value |
| progressiveness | 比较 scope 中法律类型的进步性 | law_type:law_isolationism.progressiveness > 50 | law_type | value |
| prominence | 比较人物的显赫度 | prominence > 1 | character | value |
| quality_of_life | 比较给定人口的生活质量 | quality_of_life > 10 | pop | value |
| radical_fraction | 比较州或国家人口中的激进派比例，除 value 外所有参数均为可选 | radical_fraction = { value = <script_value> pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> } | country, state | value |
| radical_population_fraction | 比较给定国家人口中激进派的比例 | radical_population_fraction > 0.2 | country | value |
| real_month | 与当前现实日期的月份比较（一月为 1，十二月为 12） | real_month > 10 | none | value |
| region_score | 比较国家 scope 中指定战略区域的 AI 策略区域得分总和。若该国由玩家控制则返回 0 | region_score = { strategic_region = sr:region_key value >= 300 } "region_score(sr:region_key)" >= 300 | country | value |
| relative_authority | 比较 scope 中国家未使用的统治力比例 |  | country | value |
| relative_bureaucracy | 比较 scope 中国家未使用的行政力比例 |  | country | value |
| relative_export_advantage | 比较州商品的相对出口优势 | relative_export_advantage > 0.1 | state_goods | value |
| relative_import_advantage | 比较州商品的相对进口优势 | relative_import_advantage > 0.1 | state_goods | value |
| relative_influence | 比较 scope 中国家未使用的影响力比例 |  | country | value |
| relative_infrastructure | 比较一个州的基础设施与基础设施使用量 | relative_infrastructure > 1.1 | state | value |
| religion_percent_country | 检查一个国家的人口中特定宗教所占的百分比 | scope:example_country = { religion_percent_country = { target = rel:catholic value <= 0.8 } } | country | value |
| religion_percent_state | 检查一个州的人口中特定宗教所占的百分比 | scope:example_state = { religion_percent_state = { target = rel:catholic value <= 0.8 } } | state | value |
| remaining_career_length | 检查人物的剩余职业生涯长度是否达到时间阈值。角色可以是特定的数据库角色、角色类型，或省略以使用离职业生涯结束最远的角色。 | remaining_career_length = { role = general years = 5 } | character | value |
| remaining_undepleted | 检查剩余的资源数量，例如一个州区域中的金矿 | remaining_undepleted = { type = bg_gold_mining amount > 1 } | state_region | value |
| role_priority | 比较人物角色的优先级 | role_priority >= 10 | character | value |
| ruler_can_have_command | 检查国家的政府类型是否允许其统治者担任指挥 | ruler_can_have_command = yes/no | country | boolean |
| save_temporary_scope_as | 将当前 scope 保存为临时目标，供本次 trigger 执行期间使用。不能覆盖已保存的 scope | save_temporary_scope_as = <string> | none |  |
| save_temporary_scope_value_as | 将一个数值或布尔值保存为任意命名的临时目标，供稍后在同一 trigger 中引用。不能覆盖已保存的 scope 值 | save_temporary_scope_value_as = { name = <string> value = <script_value> } | none |  |
| scaled_debt | 将数值与国家相对债务上限的债务进行比较 | scaled_debt = value | country | value |
| scaled_gold_reserves | 将数值与国家相对储备上限的黄金储备进行比较 | scaled_gold_reserves = value | country | value |
| scripted_bar_progress | 确定脚本化进度条的进度 | scripted_bar_progress = { name = progress_bar_tag value > 0.4 } | journal_entry | value |
| self_ownership_fraction | 比较该建筑的等级中由建筑自身所有的比例 | self_ownership_fraction > 0.5 | building | value |
| shares_heritage_trait_group_with_any_primary_culture | 检查文化是否与一国任一主体文化共享任一标记为“heritage”的特质组 | shares_heritage_trait_group_with_any_primary_culture = <country> | culture | country |
| shares_heritage_trait_group_with_culture | 检查文化是否与另一文化共享任一标记为“heritage”的特质组 | shares_heritage_trait_group_with_culture = <culture> | culture | culture |
| shares_heritage_trait_group_with_religion | 检查该宗教是否与另一宗教共享任一传承（heritage）特质组 | shares_heritage_trait_group_with_religion = <religion> | religion | religion |
| shares_heritage_trait_group_with_state_religion | 检查该宗教是否与一国的国教共享任一传承（heritage）特质组 | shares_heritage_trait_group_with_state_religion = <country> | culture | country |
| shares_heritage_trait_with_any_primary_culture | 检查文化是否与一国任一主体文化共享任一标记为“heritage”的特质 | shares_heritage_trait_with_any_primary_culture = <country> | culture | country |
| shares_heritage_trait_with_culture | 检查文化是否与另一文化共享任一标记为“heritage”的特质 | shares_heritage_trait_with_culture = <culture> | culture | culture |
| shares_heritage_trait_with_religion | 检查宗教是否与另一宗教共享任一标记为“heritage”的特质 | shares_heritage_trait_with_religion = <religion> | religion | religion |
| shares_heritage_trait_with_state_religion | 检查该宗教是否与一国的宗教共享任一传承（heritage） | shares_heritage_trait_with_state_religion = <country> | religion | country |
| shares_language_trait_group_with_any_primary_culture | 检查文化是否与一国任一主体文化共享任一标记为“language”的特质组 | shares_language_trait_group_with_any_primary_culture = <country> | culture | country |
| shares_language_trait_group_with_culture | 检查文化是否与另一文化共享任一标记为“language”的特质组 | shares_language_trait_group_with_culture = <culture> | culture | culture |
| shares_language_trait_with_any_primary_culture | 检查文化是否与一国任一主体文化共享任一标记为“language”的特质 | shares_language_trait_with_any_primary_culture = <country> | culture | country |
| shares_language_trait_with_culture | 检查文化是否与另一文化共享任一标记为“language”的特质 | shares_language_trait_with_culture = <culture> | culture | culture |
| shares_tradition_trait_with_any_primary_culture | 检查文化是否与一国任一主体文化共享任一标记为“tradition”的特质 | shares_language_trait_with_any_primary_culture = <country> | culture | country |
| shares_tradition_trait_with_culture | 检查文化是否与另一文化共享任一标记为“tradition”的特质 | shares_language_trait_with_culture = <culture> | culture | culture |
| ship_modification_market_demand_ratio | 目标船只改装所需建造商品的商品加权买入/卖出比，相对国家 scope 的市场进行评估。 | "ship_modification_market_demand_ratio(scope:ship_modification_type) > 1.25" | country | value |
| should_set_wargoal | 检查国家在其参与的任一外交博弈中是否缺少主要战争目标 |  | country | boolean |
| should_show_nudity | 是否可以显示裸体？ | should_show_nudity = yes/no | none | boolean |
| shrinking_institution | 检查机构是否正在收缩 | expanding_institution = <scope/key> | country |  |
| size_weighted_lost_battles_fraction | 确定目标国家在目标战争中败北的战斗比例，以战争中所有战斗的人力规模加权 | size_weighted_lost_battles_fraction = { target = scope:war value > 0.3 } add = "size_weighted_lost_battles_fraction(scope:war)" | country | value |
| sol_ranking | 比较一个国家的生活水平排名（位次） | sol_ranking > 42 | country | value |
| spawns_characters_to_pool | 检查该人物角色是否向人物池生成人物 | spawns_characters_to_pool = yes/no | character_role | boolean |
| speed | 比较一艘船只的速度 | speed >= 10 | ship | value |
| stall_chance | 比较 scope 中国家当前的立法停滞概率（包含来自立法修正值的影响） |  | country | value |
| stall_chance_for_law | 比较 scope 中国家针对指定法律的立法停滞概率（包含来自立法修正值的影响） | stall_chance_for_law = { target = scope:my_lawtype value > 0.2 } | country | value |
| stall_chance_for_law_without_enactment_modifier | 比较 scope 中国家针对指定法律的立法停滞概率，但不包含来自立法修正值的影响 | stall_chance_for_law_without_enactment_modifier = { target = scope:my_lawtype value > 0.2 } | country | value |
| stall_chance_without_enactment_modifier | 比较 scope 中国家当前的立法停滞概率，但不包含来自立法修正值的影响 |  | country | value |
| standard_of_living | 比较给定人口的生活水平 | standard_of_living > 10 | pop | value |
| starting_manpower | 比较一个战斗侧的初始人力 | starting_manpower > 25000 | battle_side | value |
| state_average_culture_and_religion_pop_acceptance | 州中特定文化与宗教人口的平均接受度。 | state_average_culture_and_religion_pop_acceptance = { culture = cu:polish religion = rel:catholic value >=60 } | state | value |
| state_average_culture_pop_acceptance | 州中特定文化人口的平均接受度。 | state_average_culture_pop_acceptance = { culture = cu:polish value >=60 } | state | value |
| state_average_religion_pop_acceptance | 州中特定宗教人口的平均接受度。 | state_average_religion_pop_acceptance = { religion = rel:catholic value >=60 } | state | value |
| state_cultural_acceptance | 检查目标文化的人口在 scope 州的接受度 | state_cultural_acceptance = { target = cu:french value >= 50 | state | value |
| state_exports | 比较从 scope 州向目标州（若设置）或整个世界市场（若未指定州）的出口总单位数 | state_exports = { target = state scope (optional) goods = key (optional) value >= 100 } | state | value |
| state_goods_cheaper | 检查州商品是否比基准价便宜至少指定百分比 | state_goods_cheaper > <value> | state_goods | value |
| state_goods_consumption | 检查州商品的总消费量是否为指定数量 | state_goods_consumption < <value> | state_goods | value |
| state_goods_delta | 检查州是否具有指定的商品差额（生产 − 消费） | state_goods_delta < <value> | state_goods | value |
| state_goods_has_local_goods_shortage | 检查州商品在该州是否存在短缺，但整个市场并无短缺 | state_goods_has_local_goods_shortage = yes/no | state_goods | boolean |
| state_goods_pricier | 检查州商品是否比基准价贵至少指定百分比 | state_goods_pricier > <value> | state_goods | value |
| state_goods_production | 检查州商品的总生产量是否为指定数量 | state_goods_production < <value> | state_goods | value |
| state_has_building_group_levels | 检查一个州中某建筑组的建筑等级总和 | state_has_building_group_levels = { type = bg_heavy_industry value >= 100 } | state | value |
| state_has_building_levels | 检查一个州的建筑等级总和 | state_has_building_levels >= 10 | state | value |
| state_has_building_type_levels | 检查一个州中某建筑类型的建筑等级总和 | state_has_building_type_levels = { target = bt:building_barracks value >= 100 } | state | value |
| state_has_goods_shortage | 检查州的任一建筑输入是否存在商品短缺 | state_has_goods_shortage = yes/no | state | boolean |
| state_has_national_awakening | 检查 scope 州是否处于带有活跃的民族觉醒地图标记的州区域中 | state_has_national_awakening = yes/no | state | boolean |
| state_imports | 比较从目标州向 scope 州的进口总单位数 | state_imports = { target = state scope (optional) goods = key (optional) value >= 100 } | state | value |
| state_is_eligible_as_mass_migration_target | 检查州是否完全能够接收大规模迁移。 | any_state = { state_is_eligible_as_mass_migration_target = yes } | state | boolean |
| state_population | 检查 scope 州的总人口 | state_population <= 250000 | state | value |
| state_religious_acceptance | 检查给定宗教的人口在 scope 州的接受度 | state_religious_acceptance = { target = rel:catholic value >= 50 | state | value |
| state_trade | 比较 scope 州与目标州（若设置）或整个世界市场（若未指定州）之间的商品贸易总单位数 | state_trade = { target = state scope (optional) goods = key (optional) value >= 100 } | state | value |
| state_unemployment_rate | 检查 scope 州的失业率（百分比） | state_unemployment_rate > 0.1 | state | value |
| strata | 检查 scope 人口的阶层 | strata >= upper/middle/lower | pop | value |
| subject_can_increase_autonomy | 检查附属国能否提升其自治度 | subject_can_increase_autonomy = bool | country | boolean |
| supply_network_strength | 比较该国的补给网络强度（可超过 1） | supply_network_strength > 1.1 | country | value |
| supply_ship_maintenance_fulfillment | 比较一国的补给舰维护满足率 | supply_ship_maintenance_fulfillment < 1 | country | value |
| switch | 依据一个 trigger 的结果切换以评估另一个 trigger，并可附带一个备选 trigger。 | switch = { trigger = simple_assign_trigger case_1 = { <triggers> } case_2 = { <triggers> } case_n = { <triggers> } fallback = { <triggers> } | none |  |
| taking_loans | 检查国家当前是否存在每周赤字并靠举债弥补 |  | country | boolean |
| target_cohesion_number | 以数值形式比较目标凝聚力 | target_cohesion_number > 50 | power_bloc | value |
| target_cohesion_percentage | 比较 scope 中强权集团的目标凝聚力占最大值的百分比 | target_cohesion_percentage > 0.5 | power_bloc | value |
| target_is | 检查外交博弈的目标是谁 | target_is = country | diplomatic_play | country |
| tax_capacity | 检查 scope 州的税收能力 | tax_capacity > 50 | state | value |
| tax_capacity_usage | 检查 scope 州的税收能力使用量 | tax_capacity_usage > 50 | state | value |
| tax_level | 比较 scope 国家的整体税收等级。`very_low, low, medium, high, very_high`；返回与 tax_level_value trigger 相同的数值 | tax_level = <level_term> | country | value |
| tax_level_value | 比较 scope 国家的整体税收等级整数值。`0, 1, 2, 3, 4` | income_tax_level_value = <level_num> | country | value |
| tax_waste | 比较该国的税收损耗 | tax_waste > 100 | country | value |
| tenure_in_current_power_bloc_days | 比较 scope 中国家作为其当前强权集团成员的天数 | tenure_in_current_power_bloc_days > 720 | country | value |
| tenure_in_current_power_bloc_months | 比较 scope 中国家作为其当前强权集团成员的（整）月数 | tenure_in_current_power_bloc_months > 20 | country | value |
| tenure_in_current_power_bloc_weeks | 比较 scope 中国家作为其当前强权集团成员的（整）周数 | tenure_in_current_power_bloc_weeks > 12 | country | value |
| tenure_in_current_power_bloc_years | 比较 scope 中国家作为其当前强权集团成员的（整）年数 | tenure_in_current_power_bloc_years > 5 | country | value |
| total_expenses | 该国的支出（包括来自临时性来源的支出）是否达到该数额 | total_expenses > 1000 | country | value |
| total_income | 该国的收入（包括来自临时性来源的收入）是否达到该数额 | total_income > 1000 | country | value |
| total_population | 比较给定国家的总人口 | total_population > 100000 | country | value |
| total_population_including_subjects | 比较 scope 国家及其附属国的总人口 | total_population_including_subjects > 40000000 | country | value |
| total_population_including_subjects_share | 比较 scope 国家及其附属国总人口占全球人口的比例 | total_population_including_subjects_share > 0.4 | country | value |
| total_population_share | 比较给定国家总人口占全球人口的比例 | total_population_share > 0.02 | country | value |
| total_size | 比较 scope 人口的总规模 | total_size >= 3000 | pop | value |
| total_urbanization | 比较给定州的总城市化程度 | total_urbanization > 5 | state | value |
| total_used_principle_levels | 比较一个强权集团已启用的原则等级总数 | power_bloc = { total_used_principle_levels >= 10 } | power_bloc | value |
| trait_value | 比较人物的特质总值 | trait_value < experience_level | character | value |
| transfer_money_gross_income | 该国从资金转移条约获得的毛收入（扣除支出前的收入）是否达到该数额 | transfer_money_gross_income > 1000 | country | value |
| transfer_money_net_income | 该国从金钱转让条约获得的净收入（扣除开支后的收入）是否达到该数值 | transfer_money_net_income > 1000 | country | value |
| trigger_else | 若前面 `trigger_if` 或 `trigger_else_if` 的 trigger 未满足，则评估其 display_triggers | trigger_if = { limit = { <triggers> } <display_triggers> } trigger_else = { <display_triggers> } | none |  |
| trigger_else_if | 若前面的 `trigger_if` 或 `trigger_else_if` 的 trigger 未满足，且自身 limit 的 trigger 满足，则评估其 display_triggers | trigger_if = { limit = { <triggers> } <display_triggers> } trigger_else_if = { limit = { <triggers> } <display_triggers> } | none |  |
| trigger_if | 若 limit 的 trigger 满足，则评估其 display_triggers | trigger_if = { limit = { <triggers> } <display_triggers> } | none |  |
| turmoil | 比较给定州的动荡（Turmoil）程度，即激进派所占比例 | turmoil > 0.2 | state | value |
| unit_formation_has_commander | 检查 scope 下战斗单位所属的编队是否拥有指定人物作为其指挥官之一 | unit_formation_has_commander = <character> | new_combat_unit | character |
| used_principle_slots | 比较强权集团已使用的信条槽位数量 | power_bloc = { used_principle_slots >= 2 } | power_bloc | value |
| variable_list_size | 检查变量列表的大小 | variable_list_size = { name = <variable name> value >= <value> } | none |  |
| variable_map_size |  | variable_map_size = { name = the name of the global map value >= script value or number } | none |  |
| war_exhaustion_from_acceptance_of_dead | 确定一国因战争中阵亡兵员的文化接受度而获得的厌战度（War exhaustion），无论其属于哪一方 | war_exhaustion_from_acceptance_of_dead = { target = root value >= 0.4 } | war | value |
| war_has_active_peace_deal | 若该战争存在已提出的和平协议则为真 | war_has_active_peace_deal = bool | war | boolean |
| war_participant_has_war_goal_of_type_against | 检查 scope 国家在任意战争中是否持有针对特定国家的特定类型的战争目标 | war_participant_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } | country |  |
| war_side_has_war_goal_of_type_against | 检查在任意战争中与 scope 国家同阵营的任意国家是否持有针对特定国家的特定类型的战争目标 | war_side_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } | country |  |
| was_coerced_with_naval_threat | 检查 scope 下的条约是否是通过威胁进行海上敌对行动而被接受的 | was_coerced_with_naval_threat = yes/no | treaty | boolean |
| was_exiled | 检查 scope 下的人物是否曾被流放 | was_exiled = yes/no | character | boolean |
| was_formed_from | 检查一个新成立的国家此前是否具有特定的定义 | was_formed_from = <tag> | country |  |
| wealth | 检查一个人口是否拥有一定数量的财富 | wealth = value | pop | value |
| wealth_share | 检查某一人口类型、宗教或文化在国家或州中的财富政治力量份额。必须且只能指定 pop_type、religion 或 culture 其中之一 | wealth_share = { pop_type/religion/culture = <key/scope> value <compare operator> <value> } | country, state | value |
| weekly_profit | 检查该建筑本周的利润是否高于或低于给定数值 | weekly_profit >= 20.0 | building | value |
| weighted_calc_true_if | 若已满足的子 trigger 的权重之和达到指定数值则返回真 | weighted_calc_true_if = { amount = 10 5 = { <trigger> } 15 = { <trigger> } 7 = { <trigger> } } | none |  |
| workforce | 比较 scope 下人口的劳动力规模 | workforce >= 1000 | pop | value |
| world_market_access | 检查 scope 下州的世界市场接入度 | world_market_access > 0.8 | state | value |
| world_market_delta | 检查商品在世界市场中的出口减进口之差是否为指定数值 | world_market_delta < <value> | goods | value |
| world_market_exports | 检查商品在世界市场中的出口量是否为指定数值 | world_market_exports < <value> | goods | value |
| world_market_imports | 检查商品在世界市场中的进口量是否为指定数值 | world_market_imports < <value> | goods | value |
| would_accept_diplomatic_action | 检查一国是否会接受另一国提出的某种外交行动 | would_accept_diplomatic_action = { actor = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> modify_acceptance = <script value, optional> } 若设置了 modify_acceptance，其数值将被加入对方的接受分数，以便检查例如附带义务时对方是否会接受等 | country |  |
| would_sponsor_amendment | 检查 scope 下的利益集团是否会支持某一类型的修正案 | would_sponsor_amendment = <amendment type scope> | interest_group | amendment_type |
| year | 比较游戏当前年份 | year > 1850 | none | value |
| years_of_service | 比较指挥官的服役年数 | years_of_service > 1 | character | value |
| years_to_incorporate | 检查目标国家将 scope 下的州设为已整合（incorporated）需要多少年 | years_to_incorporate = { target = c:FRA value > 5 } | state | value |

## 参考

---

- 若要更新这些表格，参见 [Module:Script docs/Triggers](https://vic3.paradoxwikis.com/Module:Script_docs/Triggers)

Modding
返回顶部
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • Triggers [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| Map | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • [States](State modding.md) |
|---|---|

| Interface | [Interface](Interface modding.md) • [GUI script](GUI script.md) • [Localization](Localization.md) • [Customizable localization](Localization.md) • [Script localization](Script localization.md) |
|---|---|

| Graphics | [3D Models](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|

| Audio | Music • [Sound](Sound modding.md) |
|---|---|

| Other | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| Guides | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|