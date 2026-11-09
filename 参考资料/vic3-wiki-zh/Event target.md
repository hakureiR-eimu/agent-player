---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Event target
source: https://vic3.paradoxwikis.com/Event_target
pageid: 3452
categories: [1.13, Modding]
fetched: 2026-10-27
---
本文已针对游戏当前[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

本页面讨论的是名为"event targets"（事件目标）的游戏脚本元素。关于弹窗叙事类内容事件，请参见
事件模组制作
；关于《维多利亚3》中存在的事件的列表与细节，请参见
事件
。
另请参见：
Effect
，
Trigger
**Event targets**（事件目标）是《维多利亚3》游戏脚本中使用的对象、[scope](Scope.md)或数值引用。大多数 event targets 在指向合适的 scope、对象或数值时，可作为 [effect](Effect.md)或 [trigger](Trigger.md)的目标。类似地，event targets 也可以作为 scope 或数值比较的左侧使用。

代表 scope 的 event targets 通常可以在点链（dot chain）中使用，例如：`p:xF98DA3.state.owner.capital` 会先查看指定的省份，然后链至该省份所在的州、拥有该州的国家，最后到该国的首都州。

## 数据类 event targets

这些 event targets 需要额外的输入，例如脚本类型或指定的 scope。其形式通常为 `event_target:data`；部分使用 `event_target(data)` 格式，此类类型必须用引号括起来，包括任何点链 scope 元素，例如 `"scope:power_bloc.power_bloc_leader.market.market_number_goods_shortages_with(scope:with_country)"`。

| Event target | 描述 | 来源 scope | 目标 scope |
|---|---|---|---|
| active_law | scope 到所 scope 国家在指定法律组中的现行法律（active_law:lawgroup_trade_policy） | country | law |
| ai_army_comparison | scope 到两国之间的陆军实力对比（示例：value = ai_army_comparison:root） | country | value |
| ai_colonization_value | scope 到目标国家 AI 对殖民某一战略区域的意愿（示例：value = ai_colonization_value:root） | strategic_region | value |
| ai_gdp_comparison | scope 到两国之间的 GDP 对比（示例：value = ai_army_comparison:root） | country | value |
| ai_ideological_opinion | scope 到 AI 对 scope 国家在目标国家上的意识形态看法（示例：value = ai_ideological_opinion:root） | country | value |
| ai_navy_comparison | scope 到两国之间的海军实力对比（示例：value = ai_navy_comparison:root） | country | value |
| ai_state_value | scope 到目标国家 AI 对拥有该 scope 州的意愿（示例：value = ai_state_value:root） | state | value |
| ai_subject_value | scope 到目标国家 AI 想将 scope 国家作为附属国的意愿（示例：value = ai_subject_value:root） | country | value |
| ai_transit_rights_value | scope 到 AI 想获得通过目标国家过境权的意愿（示例：value = ai_transit_rights_value:root） | country | value |
| ai_treaty_export_value | scope 到目标国家 AI 通过条约出口所 scope 市场商品的意愿（示例：value = ai_market_export_value:root） | market_goods | value |
| ai_treaty_fairness | scope 到 AI 对其与目标国家之间现有条约条款对双方公平程度的评估（示例：value = ai_treaty_fairness_score:root） | country | value |
| ai_treaty_import_value | scope 到目标国家 AI 通过条约进口所 scope 市场商品的意愿（示例：value = ai_market_import_value:root） | market_goods | value |
| ai_treaty_port_value | scope 到目标国家 AI 想在该 scope 州获得条约港的意愿（示例：value = ai_treaty_port_value:root） | state | value |
| ai_treaty_trade_value | scope 到目标国家 AI 进出口所 scope 市场商品的意愿（示例：value = ai_market_trade_value:root） | market_goods | value |
| ai_treaty_value | scope 到 AI 对其与目标国家之间现有条约条款对自身有利程度的评估（示例：value = ai_treaty_value:root） | country | value |
| amendment_type | 通过名称 scope 到某一修正案类型（amendment_type:key） | none | amendment_type |
| array_define | 引用数组 define 中数值的值：array_define:Namespace\|Name\|Index。索引从 0 开始。 | none | value |
| average_defense | 返回与国家同属一方的前线上单位的平均防御 | front | value |
| average_offense | 返回与国家同属一方的前线上单位的平均进攻 | front | value |
| b | scope 到该州中指定键值的建筑，示例：b:building_port | state | building |
| bg | 通过名称 scope 到某一建筑组（bg:bg_logging） | none | building_group |
| bt | scope 到某一建筑类型，示例：bt:building_tooling_workshops | none | building_type |
| c | scope 到指定 tag 的国家，示例：c:GBR | none | country |
| catalyst_type | 通过名称 scope 到某一外交催化剂类型（catalyst_type:catalyst_relations_level_improved） | none | diplomatic_catalyst_type |
| cd | scope 到指定 tag 的国家定义，示例：cd:FRA | none | country_definition |
| company | scope 到所 scope 国家中指定名称类型的公司（company:company_rheinmetall） | country | company |
| company_type | 通过名称 scope 到某一公司类型（company_type:company_rheinmetall） | none | company_type |
| compare_complex_value | 一个需要可解析字符串参数的比较 trigger，会在其所用的上下文中返回该值，例如：scope:root.number_of(armies) | varies | value |
| cu | scope 到指定键值的文化，示例：cu:welsh | none | culture |
| decree_cost | scope 到某州颁布某项法令的威力消耗 > decree_cost:decree_road_maintaintenance | state | value |
| define | 引用数值或颜色 define 的值：define:Namespace\|Name | none | value |
| diplomatic_pact_other_country | scope 到所 scope 外交条约中的另一国家，示例：diplomatic_pact_other_country(root) | diplomatic_pact | country |
| flag | 一个本地化键，例如 flag:the_boss | none | flag |
| g | scope 到指定键值的商品，示例：g:iron | none | goods |
| get_ruler_for | 从国家 scope 到在指定权力移交类型下将成为统治者的人物 get_ruler_for:parliamentary_elective = { effects... } | country | character |
| global_productivity | scope 到全局生产力数值（示例：global_productivity:high_threshold） | none | value |
| global_var | 通过名称引用之前设置的全局变量，例如：global_var:important_thing | none | varies |
| harvest_condition_type | 通过名称 scope 到某一收成条件类型（harvest_condition_type:drought） | none | harvest_condition_type |
| i | scope 到指定键值的意识形态，示例：i:ideology_patriarchal | none | ideology |
| identity | 通过名称 scope 到强权集团的身份（identity:key） | none | power_bloc_identity |
| ideology | 双重用途：通过名称 scope 到某一意识形态（ideology:ideology_anarchist）；scope 到所 scope 人物的意识形态 | character, none | ideology |
| ig | scope 到属于该国家的指定键值的利益集团，示例：ig:ig_armed_forces | country, political_movement | interest_group |
| ig_trait | scope 到指定键值的利益集团特质，示例：ig_trait:ig_trait_xenophobia | none | interest_group_trait |
| ig_type | scope 到某一利益集团类型，示例：ig_type:ig_landowners | none | interest_group_type |
| infamy_threshold | scope 到恶名等级阈值用于比较（infamy_threshold:infamous） | none | value |
| input_market_goods | scope 到条约条款中的市场商品输入（示例：input_market_goods:root） | treaty_article, treaty_article_options | market_goods |
| institution | 通过名称 scope 到某一国家的机构（institution:institution_health_system） | country | institution |
| je | scope 到属于该国家的指定键值的日志条目，示例：je:je_antarctica | country | journal_entry |
| law_type | 通过名称（law_type:law_protected_speech）或从所 scope 的法律 scope 到某一法律类型 | law, none | law_type |
| lobby_foreign_anti_clout | scope 到针对某一特定国家的所有反该国外交政策游说团的总政治力量（lobby_foreign_anti_clout:root >= 0.2） | country | value |
| lobby_foreign_pro_clout | scope 到针对某一特定国家的所有亲该国外交政策游说团的总政治力量（lobby_foreign_pro_clout:root >= 0.2） | country | value |
| lobby_in_government_foreign_anti_clout | scope 到针对某一特定国家、处于执政地位的所有反该国外交政策游说团的总政治力量（lobby_in_government_foreign_anti_clout:root >= 0.2） | country | value |
| lobby_in_government_foreign_pro_clout | scope 到针对某一特定国家、处于执政地位的所有亲该国外交政策游说团的总政治力量（lobby_in_government_foreign_pro_clout:root >= 0.2） | country | value |
| lobby_join_weight | scope 到利益集团加入某一游说团的加入权重（lobby_join_weight:root >= 5） | interest_group | value |
| lobby_type | 通过名称 scope 到某一政治游说团类型（lobby_type:lobby_pro_country） | none | political_lobby_type |
| lobby_war_opposition | scope 到反对所 scope 战争的所有游说团的总政治力量（lobby_war_opposition:root >= 0.2） | country | value |
| lobby_war_support | scope 到支持所 scope 战争的所有游说团的总政治力量（lobby_war_support:root >= 0.2） | country | value |
| local_var | 通过名称引用之前设置的局部变量，例如：local_var:person_of_interest | none | varies |
| mg | 从市场 scope 到指定键值的市场商品（示例：mg:tools） | market | market_goods |
| mobilization_option | 通过名称 scope 到某一动员选项（mobilization_option:key） | none | mobilization_option |
| modifier | scope 到属于当前对象的指定键值 modifier 类型的数值，示例：modifier:country_influence_add | battle_side, building, character, country, interest_group, market, power_bloc, state | boolean, value |
| movement_type | 通过名称 scope 到某一政治运动类型（movement_type:movement_religious_majority） | none | political_movement_type |
| mutual_trade_value_with_country | scope 到两市场之间贸易路线中商品贸易的总基础价值（示例：mutual_trade_value_with_country:root >= 1000） | country | value |
| naval_hostility_damage | scope 到该国在当前海军敌对行动中对另一国造成的伤害点数（示例：naval_hostility_damage:root >= 50） | country | value |
| nf | scope 到应用于该州的指定键值的法令，示例：nf:decree_road_maintaintenance | state | decree |
| num_active_ships | 获取国家、指挥官或军事编队的现役舰船数量，或获取该省境内与指定国家结盟的军事编队的现役舰船数量 | character, country, military_formation, province | value |
| num_active_ships_in_battle | 获取国家、指挥官或军事编队的战斗中现役舰船数量，或获取该省境内与指定国家结盟的军事编队的战斗中现役舰船数量 | character, country, military_formation, province | value |
| num_active_ships_not_in_battle | 获取国家、指挥官或军事编队的非战斗中现役舰船数量，或获取该省境内与指定国家结盟的军事编队的非战斗中现役舰船数量 | character, country, military_formation, province | value |
| num_alliances | 获取所 scope 国家的同盟总数（示例：num_alliances:root >= 2） | country | value |
| num_alliances_and_defensive_pacts_with_allies | scope 到目标国家与 scope 国家盟友之间的同盟数量（示例：num_alliances_and_defensive_pacts_with_allies:root >= 2） | country | value |
| num_alliances_and_defensive_pacts_with_rivals | scope 到目标国家与 scope 国家竞争对手之间的同盟及防御条约数量（示例：num_alliances_and_defensive_pacts_with_rivals:root >= 2） | country | value |
| num_defending_battalions | 返回与国家同属一方的前线上战斗中单位的总数，示例：num_defending_battalions(root) | front | value |
| num_non_destroyed_ships | 获取国家、指挥官或军事编队的未沉没舰船数量，或获取该省境内与指定国家结盟的军事编队的未沉没舰船数量 | character, country, military_formation, province | value |
| num_non_destroyed_ships_in_battle | 获取国家、指挥官或军事编队的战斗中未沉没舰船数量，或获取该省境内与指定国家结盟的军事编队的战斗中未沉没舰船数量 | character, country, military_formation, province | value |
| num_non_destroyed_ships_not_in_battle | 获取国家、指挥官或军事编队的非战斗中未沉没舰船数量，或获取该省境内与指定国家结盟的军事编队的非战斗中未沉没舰船数量 | character, country, military_formation, province | value |
| num_pending_events | scope 到所 scope 国家的待处理事件数量，可为总体或指定类别 num_pending_events > 0 num_pending_events:enactment > 0 | country | value |
| num_shared_rivals | scope 到 scope 国家与目标国家共同拥有的竞争对手数量（示例：num_shared_rivals:root >= 2） | country | value |
| num_ships | 获取国家、指挥官或军事编队的舰船数量，或获取该省境内与指定国家结盟的军事编队的舰船数量 | character, country, military_formation, province | value |
| num_ships_in_battle | 获取国家、指挥官或军事编队的战斗中舰船数量，或获取该省境内与指定国家结盟的军事编队的战斗中舰船数量 | character, country, military_formation, province | value |
| num_ships_not_in_battle | 获取国家、指挥官或军事编队的非战斗中舰船数量，或获取该省境内与指定国家结盟的军事编队的非战斗中舰船数量 | character, country, military_formation, province | value |
| num_ships_of_group | 所 scope 国家或军事编队中指定舰船群的舰船数量 | country, military_formation | value |
| num_total_battalions | 返回与国家同属一方的前线上单位的总数，示例：num_total_battalions(root) | front | value |
| num_units | 获取指挥官或军事编队的现役单位数量，或获取该省境内与指定国家结盟的军事编队的现役单位数量 | character, military_formation, province | value |
| num_units_in_battle | 获取指挥官或军事编队的战斗中现役单位数量，或获取该省境内与指定国家结盟的军事编队的战斗中现役单位数量 | character, military_formation, province | value |
| num_units_not_in_battle | 获取指挥官或军事编队的非战斗中现役单位数量，或获取该省境内与指定国家结盟的军事编队的非战斗中现役单位数量 | character, military_formation, province | value |
| p | scope 到由十六进制键值指定的省份，示例：p:x1A6E5B | none | province |
| pirated_trade_value_by | scope 到目标国家每周从该国劫掠商品的平均基础价值（示例：pirated_trade_value_by:root >= 50） | country | value |
| play_type | 通过名称 scope 到某一外交博弈类型（play_type:dp_default_treaty_article） | none | diplomatic_play_type |
| pop_type | 通过名称 scope 到某一人口类型（pop_type:laborers） | none | pop_type |
| principle | 通过名称 scope 到强权集团原则（principle:key） | none | power_bloc_principle |
| principle_group | 通过名称 scope 到强权集团原则组（principle_group:key） | none | power_bloc_principle_group |
| py | scope 到属于该国家的指定键值的活跃政党，示例：py:communist_party | country | party |
| rank_value | scope 到某一特定国家等级的等级值（rank_value:great_power） | none | value |
| region_state | scope 到目标国家拥有的州（示例：region_state:BIC） | state_region | state |
| rel | scope 到指定键值的宗教，示例：rel:catholic | none | religion |
| relations | scope 到两国之间的关系（示例：relations:root >= 2） | country | value |
| relations_change_rate | scope 到两国之间关系进展的每日变化（示例：relations_change_rate:root > 0） | country | value |
| relations_threshold | scope 到关系阈值等级用于比较（relations_threshold:warm） | none | value |
| s | scope 到由键值指定的州区域，示例：s:STATE_UTAH | none | state_region |
| scope | 通过名称引用之前保存的 scope，例如：scope:target | none | varies |
| sg | 从州 scope 到指定键值的州商品，示例：sg:wood | state | state_goods |
| ship_group | 从舰船 scope 到其所属群组，或通过名称 scope 到某一舰船群（ship_group:ship_group_capital_ships） | none, ship | ship_group |
| ship_type | 通过名称 scope 到某一舰船类型（ship_type:ship_type_frigate） | none | ship_type |
| sr | scope 到指定键值的战略区域，示例：sr:region_persia | none | strategic_region |
| strait_trade_importance_by | scope 到该国经由目标国家控制的海峡所贸易商品的重要性。当控制方控制海峡两侧时，累计值会乘以 STRAIT_FULL_CONTROL_TRADE_IMPORTANCE_MULT（示例：strait_trade_importance_by:root >= 100） | country | value |
| strait_type | 通过名称 scope 到某一海峡类型（strait_type:key） | none | strait_type |
| tension | scope 到两国之间的紧张度（示例：tension:root >= 2） | country | value |
| tension_threshold | scope 到紧张度等级阈值用于比较（tension_threshold:warm） | none | value |
| unit_type | 通过名称 scope 到某一作战单位类型（unit_type:key） | none | combat_unit_type |
| var | 通过名称引用 scope 中之前设置的变量，例如：var:mortal_enemy | varies | varies |
## 数值 event target

这些 event target 返回数值或布尔值，因此可用于比较或 script value。

| Event target | 描述 | 来源 scope |
|---|---|---|
| ai_army_comparison | Scope 到两国之间的陆军实力对比值（示例：value = ai_army_comparison:root） | country |
| ai_colonization_value | Scope 到目标国家 AI 殖民某战略区域的意愿（示例：value = ai_colonization_value:root） | strategic_region |
| ai_gdp_comparison | Scope 到两国之间的 GDP 对比值（示例：value = ai_army_comparison:root） | country |
| ai_ideological_opinion | Scope 到 AI 对 scope 国家在目标国家上的意识形态看法（示例：value = ai_ideological_opinion:root） | country |
| ai_navy_comparison | Scope 到两国之间的海军实力对比值（示例：value = ai_navy_comparison:root） | country |
| ai_state_value | Scope 到目标国家 AI 获得该 scope 州的意愿（示例：value = ai_state_value:root） | state |
| ai_subject_value | Scope 到目标国家 AI 想让 scope 国家成为其附属国的意愿（示例：value = ai_subject_value:root） | country |
| ai_transit_rights_value | Scope 到 AI 想获得穿越目标国家通行权的意愿（示例：value = ai_transit_rights_value:root） | country |
| ai_treaty_export_value | Scope 到目标国家 AI 通过条约出口 scope 市场商品的意愿（示例：value = ai_market_export_value:root） | market_goods |
| ai_treaty_fairness | Scope 到 AI 对与目标国家现有条约条款对双方公平程度的评估（示例：value = ai_treaty_fairness_score:root） | country |
| ai_treaty_import_value | Scope 到目标国家 AI 通过条约进口 scope 市场商品的意愿（示例：value = ai_market_import_value:root） | market_goods |
| ai_treatyport_value | Scope 到目标国家 AI 想在 scope 州获得条约港的意愿（示例：value = ai_treaty_port_value:root） | state |
| ai_treaty_trade_value | Scope 到目标国家 AI 进出口 scope 市场商品的意愿（示例：value = ai_market_trade_value:root） | market_goods |
| ai_treaty_value | Scope 到 AI 对与目标国家现有条约条款对自身有利程度的评估（示例：value = ai_treaty_value:root） | country |
| army_size | scope 国家的营数量，不含当前已征召的征召兵。 | country |
| army_size_including_conscripts | scope 国家的营数量，含当前已征召的征召兵。 | country |
| army_size_including_raised_conscripts | scope 国家的营数量，含当前已征召的征召兵，不含未征召的征召兵。 | country |
| array_define | 引用数组 define 中某数值的值：array_define:Namespace\|Name\|Index。Index 从 0 开始。 | 无 |
| average_defense | 返回前线（Front）上与国家同阵营单位的平均防御 | front |
| average_expected_sol | 获取 scope 的平均预期生活水平 | country, state |
| average_offense | 返回前线（Front）上与国家同阵营单位的平均进攻 | front |
| average_progressiveness | 获取 scope 人物或利益集团的平均进步性 | character, interest_group |
| average_sol | 获取 scope 的平均生活水平 | country, state |
| base_price | 获取 scope 商品的基础价格 | goods |
| binding_period | 获取 scope 条约签署时的原始约束期天数 | treaty, treaty_options |
| building_levels | 获取 scope 国家非自给建筑的总等级数 | country |
| cached_ai_coastal_population | Scope 到记录在 AI 支出变量中的沿海人口总数（示例：value = cached_ai_coastal_population） | country |
| cached_ai_incorporated_coastal_population | Scope 到记录在 AI 支出变量中的已整合沿海人口总数（示例：value = cached_ai_incorporated_coastal_population） | country |
| cached_ai_incorporated_population | Scope 到记录在 AI 支出变量中的已整合人口总数（示例：value = cached_ai_incorporated_population） | country |
| cached_ai_overseas_subject_population | Scope 到记录在 AI 支出变量中的直接非相邻附属国人口总数（示例：value = cached_ai_overseas_subject_population） | country |
| cached_ai_subject_population | Scope 到记录在 AI 支出变量中的直接附属国人口总数（示例：value = cached_ai_subject_population） | country |
| cached_ai_total_population | Scope 到记录在 AI 支出变量中的总人口数（示例：value = cached_ai_total_population） | country |
| cached_ai_unincorporated_coastal_population | Scope 到记录在 AI 支出变量中的未整合沿海人口总数（示例：value = cached_ai_unincorporated_coastal_population） | country |
| cached_ai_unincorporated_population | Scope 到记录在 AI 支出变量中的未整合人口总数（示例：value = cached_ai_unincorporated_population） | country |
| colonial_growth_per_colony | Scope 到该国家每个殖民地的殖民增长值（示例：colonial_growth_per_colony > 0） | country |
| combat_width | Scope 到 scope 省份的战斗宽度乘数 | province |
| command_limit_num_units | 获取指挥官按其指挥上限通常能从所属军事编队获得的基准单位数量 | character |
| compare_complex_value | 一个需要可解析字符串参数的比较 trigger，会在使用它的上下文中返回其值，例如：scope:root.number_of(armies) | 不定 |
| compare_value | 一个会在使用它的上下文中返回其值的比较 trigger，例如：root.gold | 不定 |
| credit | Scope 到该国家当前可获取的最大信贷额度 | country |
| decree_cost | Scope 到某州施行某项法令的花费 authority > decree_cost:decree_road_maintaintenance | state |
| defense | 返回单位的防御值（含其指挥官的影响） | new_combat_unit |
| define | 引用数值或颜色 define 的值：define:Namespace\|Name | 无 |
| demoralized | 返回单位士气崩溃的人力数量 | new_combat_unit |
| detection | 从舰队 scope 链接到舰队中船只的合计侦测 | military_formation |
| diplomatic_pact_expense_ratio | Scope 到该国家外交条约支出与收入的比率，限制在 0-1 之间（示例：value = diplomatic_pact_expense_ratio） | country |
| front_length | 返回前线（Front）中的省份数量 | front |
| gdp | 获取 scope 国家/州的年度预测 GDP | country, state |
| global_gdp | 获取全球年度预测 GDP | 无 |
| global_productivity | Scope 到全球生产力值（示例：global_productivity:high_threshold） | 无 |
| goal_value | Scope 到日志条目的目标值 | journal_entry |
| government_size | 获取 scope 国家当前政府中的政党与独立利益集团数量 | country |
| income | 获取 scope 国家的当前每周收入 | country |
| income_transfer_expenses | Scope 到 scope 国家通过条约和协议向其他国家转移的金额（示例：income_transfer_expenses >= 100） | country |
| income_transfer_relative_expenses | Scope 到该国家通过条约和协议向其他国家转移的收入比例（示例：income_transfer_relative_expenses >= 0.2） | country |
| infamy | Scope 到 scope 国家的恶名（示例：infamy >= 2） | country |
| infamy_threshold | Scope 到恶名等级阈值，用于比较（infamy_threshold:infamous） | 无 |
| input_quantity | Scope 到条约条款中的投入数量 | treaty_article, treaty_article_options |
| investment | Scope 到机构当前的投资等级（示例：investment < investment_max） | institution |
| investment_max | Scope 到该国家在机构中的当前最大投资等级（示例：investment < investment_max） | institution |
| investment_pool_income | 获取 scope 国家的当前每周投资池收入 | country |
| legitimacy | Scope 到该国家当前的合法性 | country |
| level | Scope 到建筑的等级 | building |
| level_after_queued_constructions | Scope 到所有排队中的建造完成后建筑的等级 | building |
| lobby_foreign_anti_clout | Scope 到针对特定国家的所有反该国游说团的总政治力量（lobby_foreign_anti_clout:root >= 0.2） | country |
| lobby_foreign_pro_clout | Scope 到针对特定国家的所有亲该国游说团的总政治力量（lobby_foreign_pro_clout:root >= 0.2） | country |
| lobby_in_government_foreign_anti_clout | Scope 到政府中针对特定国家的所有反该国游说团的总政治力量（lobby_in_government_foreign_anti_clout:root >= 0.2） | country |
| lobby_in_government_foreign_pro_clout | Scope 到政府中针对特定国家的所有亲该国游说团的总政治力量（lobby_in_government_foreign_pro_clout:root >= 0.2） | country |
| lobby_join_weight | Scope 到利益集团加入某游说团的加入权重（lobby_join_weight:root >= 5） | interest_group |
| lobby_war_opposition | Scope 到所有反对 scope 战争的游说团的总政治力量（lobby_war_opposition:root >= 0.2） | country |
| lobby_war_support | Scope 到所有支持 scope 战争的游说团的总政治力量（lobby_war_support:root >= 0.2） | country |
| manpower | 返回单位的人力 | new_combat_unit |
| market_export_cap | 基于 scope 市场商品的生产获取市场可出口的最大商品量 | market_goods |
| market_import_cap | 基于 scope 市场商品的消费获取市场可进口的最大商品量 | market_goods |
| migration_pull | 获取州的迁移拉力或国家的大规模迁移拉力。 | country, state |
| military_expenses | 获取 scope 国家的当前军事支出（奴隶、工资和商品） | country |
| military_expenses_share | 获取 scope 国家当前军事支出（奴隶、工资和商品）占总支出的比例 | country |
| mobilization | 返回单位的动员值，介于 0 和 1 之间 | new_combat_unit |
| modifier | Scope 到当前对象指定键的 modifier 类型值，示例：modifier:country_influence_add | battle_side, building, character, country, interest_group, market, power_bloc, state |
| momentum | 获取 scope 政党的原始势头 | party |
| morale | 返回单位的士气 | new_combat_unit |
| mutual_trade_value_with_country | Scope 到两个市场之间贸易路线中商品交易的总基础价值（示例：mutual_trade_value_with_country:root >= 1000） | country |
| named_script_value | 一个会在使用它的上下文中计算并返回其值的 script value | 无 |
| naval_combat_power | Scope 到该国家的海军战斗力（示例：naval_combat_power > 100） | country |
| naval_hostility_average_damage_dealt | Scope 到该国家在回顾期内其发起的海军敌对行动中造成的平均伤害。未找到敌对行动时返回 -1。 | country |
| naval_hostility_damage | Scope 到该国家在当前海军敌对行动中对另一国造成的伤害点数（示例：naval_hostility_damage:root >= 50） | country |
| naval_vulnerability | Scope 到基于贸易依赖度和沿海 GDP 占比计算的国家海军脆弱性评分，上限为某 define 最大值 | country |
| navy_size | scope 国家的分舰队数量。 | country |
| num_active_interests | Scope 到该国家拥有的活跃利益数量 num_active_interests > 5 | country |
| num_active_natural_interests | Scope 到该国家拥有的活跃天然利益数量 num_active_natural_interests > 5 | country |
| num_active_plays | 获取 scope 国家当前发起的活跃外交博弈数量 | country |
| num_active_ships | 获取国家、指挥官或军事编队的活跃船只数量，或获取省份中与指定国家结盟的军事编队的活跃船只数量 | character, country, military_formation, province |
| num_active_ships_in_battle | 获取国家、指挥官或军事编队处于战斗中的活跃船只数量，或获取省份中与指定国家结盟的军事编队处于战斗中的活跃船只数量 | character, country, military_formation, province |
| num_active_ships_not_in_battle | 获取国家、指挥官或军事编队未处于战斗中的活跃船只数量，或获取省份中与指定国家结盟的军事编队未处于战斗中的活跃船只数量 | character, country, military_formation, province |
| num_admirals | Scope 到该国家的海军上将数量 | country |
| num_alliances | 获取 scope 国家的同盟总数（示例：num_alliances:root >= 2） | country |
| num_alliances_and_defensive_pacts_with_allies | Scope 到目标国家与 scope 国家盟友达成的同盟及防御条约数量（示例：num_alliances_and_defensive_pacts_with_allies:root >= 2） | country |
| num_alliances_and_defensive_pacts_with_rivals | Scope 到目标国家与 scope 国家竞争对手达成的同盟及防御条约数量（示例：num_alliances_and_defensive_pacts_with_rivals:root >= 2） | country |
| num_battalions | 返回指挥官麾下活跃营的数量 | character |
| num_characters | Scope 到该国家的人物数量 | country |
| num_colony_projects | 获取 scope 国家当前未完成/进行中的殖民项目数量 | country |
| num_commanderless_units | 军事编队中因指挥官指挥上限而当前没有指挥官的单位数量。注：被击败的指挥官不指挥单位，即被击败的指挥官越多，无指挥官的单位越多。 | military_formation |
| num_commanders | Scope 到该国家的指挥官数量 | country |
| num_defending_battalions | 返回前线（Front）上与国家同阵营参战单位的总数，示例：num_defending_battalions(root) | front |
| num_defensive_pacts | Scope 到目标国家拥有的防御条约总数（示例：num_defensive_pacts >= 2） | country |
| num_garrison_units | 返回驻扎在某总部（HQ）的单位数量 | hq |
| num_generals | Scope 到该国家的将军数量 | country |
| num_income_transfer_pacts | Scope 到目标国家拥有的收入转出（向他国转移）协议总数（示例：num_income_transfer_pacts >= 2） | country |
| num_income_transfer_treaty_articles | Scope 到目标国家拥有的收入转出（向他国转移）条约条款总数（示例：num_income_transfer_treaty_articles >= 2） | country |
| num_income_transfers | Scope 到目标国家拥有的收入转出（向他国转移）协议和条约条款总数（示例：num_income_transfers >= 2） | country |
| num_incorporated_states | 获取 scope 国家当前已整合州的数量 | country |
| num_interests | Scope 到该国家拥有的利益数量（含非活跃）num_interests > 5 | country |
| num_mandates | Scope 到 scope 强权集团可用的法令数量（power_bloc.num_mandates > 0） | power_bloc |
| num_mobilized_battalions | 返回将军麾下已完全动员的单位数量 | character |
| num_natural_interests | Scope 到该国家拥有的天然利益数量（含非活跃）num_natural_interests > 5 | country |
| num_non_destroyed_ships | 获取国家、指挥官或军事编队未被摧毁的船只数量，或获取省份中与指定国家结盟的军事编队未被摧毁的船只数量 | character, country, military_formation, province |
| num_non_destroyed_ships_in_battle | 获取国家、指挥官或军事编队处于战斗中且未被摧毁的船只数量，或获取省份中与指定国家结盟的军事编队处于战斗中且未被摧毁的船只数量 | character, country, military_formation, province |
| num_non_destroyed_ships_not_in_battle | 获取国家、指挥官或军事编队未处于战斗中且未被摧毁的船只数量，或获取省份中与指定国家结盟的军事编队未处于战斗中且未被摧毁的船只数量 | character, country, military_formation, province |
| num_obligations_earned | 从国家 Scope 到他国欠其（即其已赚取）的义务数量 | country |
| num_pending_events | Scope 到 scope 国家待处理事件的数量，可以是总量或指定类别的数量 num_pending_events > 0 num_pending_events:enactment > 0 | country |
| num_politicians | Scope 到该国家的政治家数量 | country |
| num_positive_relations | 获取当前与 scope 国家关系为正的国家数量 | country |
| num_provinces | 获取 scope 实体当前的省份数量 | front, state, state_region |
| num_queued_constructions | Scope 到目标国家排队中的建造总数（示例：num_queued_constructions >= 2） | country |
| num_queued_government_constructions | Scope 到目标国家排队中的政府建造总数（示例：num_queued_government_constructions >= 2） | country |
| num_queued_private_constructions | Scope 到目标国家排队中的私人建造总数（示例：num_queued_private_constructions >= 2） | country |
| num_rivals | Scope 到目标国家拥有的竞争对手总数（示例：num_rivals >= 2） | country |
| num_ruling_igs | 获取 scope 国家当前政府中的利益集团数量 | country |
| num_shared_rivals | Scope 到 scope 国家与目标国家共有的竞争对手数量（示例：num_shared_rivals:root >= 2） | country |
| num_ships | 获取国家、指挥官或军事编队的船只数量，或获取省份中与指定国家结盟的军事编队的船只数量 | character, country, military_formation, province |
| num_ships_in_battle | 获取国家、指挥官或军事编队处于战斗中的船只数量，或获取省份中与指定国家结盟的军事编队处于战斗中的船只数量 | character, country, military_formation, province |
| num_ships_not_in_battle | 获取国家、指挥官或军事编队未处于战斗中的船只数量，或获取省份中与指定国家结盟的军事编队未处于战斗中的船只数量 | character, country, military_formation, province |
| num_ships_of_group | scope 国家或军事编队中指定船只编组的船只数量 | country, military_formation |
| num_states | 获取 scope 国家当前的州数量 | country |
| num_total_battalions | 返回前线（Front）上与国家同阵营的单位总数，示例：num_total_battalions(root) | front |
| num_unincorporated_states | 获取 scope 国家当前未整合州的数量 | country |
| num_units | 获取指挥官或军事编队的活跃单位数量，或获取省份中与指定国家结盟的军事编队的活跃单位数量 | character, military_formation, province |
| num_units_in_battle | 获取指挥官或军事编队处于战斗中的活跃单位数量，或获取省份中与指定国家结盟的军事编队处于战斗中的活跃单位数量 | character, military_formation, province |
| num_units_not_in_battle | 获取指挥官或军事编队未处于战斗中的活跃单位数量，或获取省份中与指定国家结盟的军事编队未处于战斗中的活跃单位数量 | character, military_formation, province |
| num_units_share | 考虑指挥上限后指挥官获得的单位比例。示例：若人物有 30 指挥上限，舰队共有 60 总指挥上限，编队共有 50 支分舰队，则该人物在其战斗中应获得 25 支分舰队 | character |
| num_world_market_hub_trade_center_levels | 获取与 scope 世界市场中心州关联的贸易中心等级总数 | state |
| offense | 返回单位的进攻值（含其指挥官的影响） | new_combat_unit |
| participants | 获取 scope 市场中的参与国家总数 | market |
| pirated_trade_value_by | Scope 到目标国家平均每周从该国劫掠的商品基础价值（示例：pirated_trade_value_by:root >= 50） | country |
| player_owed_obligation_days_left | Scope 到外交关系 scope 中某义务剩余的天数（示例：obligation_days_left >= 2） | diplomatic_relations |
| pop_weight_modifier_scale | 获取人口的权重修正乘数 | pop |
| popularity | 获取 scope 人物的人气，通常介于 -100 到 +100 之间 | character |
| population_below_expected_sol | Scope 到该州当前生活水平低于其预期生活水平的人口百分比（0-1） | state |
| power_projection | 获取 scope 编队、单位或船只的力量投射值 | military_formation, new_combat_unit, ship |
| principal | 获取该国家当前的债务本金 | country |
| prosperity | Scope 到 scope 公司的繁荣度（示例：prosperity >= 2） | company |
| rank_value | Scope 到某特定国家等级的等级值（rank_value:great_power） | 无 |
| relations | Scope 到两国之间的关系（示例：relations:root >= 2） | country |
| relations_change_rate | Scope 到两国之间关系进展的每日变化（示例：relations_change_rate:root > 0） | country |
| relations_threshold | Scope 到关系等级阈值，用于比较（relations_threshold:warm） | 无 |
| remaining_binding_period | 获取 scope 条约当前剩余的约束期天数 | treaty, treaty_options |
| required_construction | 获取 scope 建筑类型所需的建造量 | building_type |
| scope_relations | Scope 到外交关系 scope 中的关系值（示例：scope_relations >= 2） | diplomatic_relations |
| scope_tension | Scope 到外交关系 scope 中的紧张度值（示例：scope_tension >= 2） | diplomatic_relations |
| screening | 从舰队 scope 链接到舰队中船只的合计掩护 | military_formation |
| strait_trade_importance_by | Scope 到该国通过目标国家所控海峡进行贸易的商品贸易重要性。对控制方同时控制两侧的海峡，累计值会乘以 STRAIT_FULL_CONTROL_TRADE_IMPORTANCE_MULT（示例：strait_trade_importance_by:root >= 100） | country |
| techs_researched | Scope 到该国当前已研究的科技数量 | country |
| tension | Scope 到两国之间的紧张度（示例：tension:root >= 2） | country |
| tension_threshold | Scope 到紧张度等级阈值，用于比较（tension_threshold:warm） | 无 |
| total_crew_needed | 获取该国所有船只所需的船员总数 | country |
| total_export_value | Scope 到 scope 国家向世界市场出口的总价值（示例：total_export_value >= 1000） | country |
| total_import_value | 作用于 scope 国家从世界市场进口的总值（示例：total_import_value >= 1000） | country |
| total_marine_capacity | 获取一个国家所有舰队总的海运能力 | country |
| total_pirated_trade_value | 作用于外交关系 scope 中两国间通过海盗行为遭劫掠商品的每周基础平均值（示例：total_pirated_trade_value >= 100） | diplomatic_relations |
| total_trade_value | 作用于 scope 国家与世界市场贸易的总值（示例：total_trade_value >= 1000） | country |
| training_rate | 作用于一个建筑当前每周最大训练速率 | building |
| treaty_exports | 获取该商品向 scope 的 MarketGoods 所在市场进行条约（而非世界市场）出口的当前数量 | market_goods |
| treaty_imports | 获取该商品向 scope 的 MarketGoods 所在市场进行条约（而非世界市场）进口的当前数量 | market_goods |
| value | 数值字面值，例如：1、5.2、-6 | none |
| visibility | 从舰队 scope 链接到该舰队中舰船的总可见度 | military_formation |
| vulnerability | 从舰队 scope 链接到该舰队中舰船的总脆弱度 | military_formation |
| weekly_prosperity_change | 作用于 scope 公司的每周繁荣度变化（示例：weekly_prosperity_change >= 2） | company |

## 通配 event target

这些 event target 指向某一类 event target，而非某个具名的 event target。例如，event target `compare_value` 指任何检查数值（如 `free_arable_land`）的简单内联 [trigger](Trigger.md)。类似地，`named_script_value` 按名称指向计算出的 [script value](Script value.md)。

| Event target | 描述 | 来源 scope | 目标 scope |
|---|---|---|---|
| compare_complex_value | 一个需要可解析字符串参数的比较 trigger，会在其使用的上下文中返回该值，例如：scope:root.number_of(armies) | 不定 | value |
| compare_value | 一个比较 trigger，会在其使用的上下文中返回该值，例如：root.gold | 不定 | value |
| named_script_value | 一个 script value，会在其使用的上下文中计算并返回其值 | none | color, value |
| value | 数值字面值，例如：1、5.2、-6 | none | value |

## 按 scope 分类的事件目标

下表按 event target 所需的 scope 列出。部分 event target 因可用于多个 scope 而重复出现。可用于任意 scope 的 event target 以 `none` 标示。

### 无 scope（scopeless）

| Event target | 描述 | 目标 scope |
|---|---|---|
| amendment_type | 按名称作用于一种修正案类型（amendment_type:key） | amendment_type |
| array_define | 引用数组 define 中某个数值的值：array_define:Namespace\|Name\|Index。Index 从 0 开始。 | value |
| bg | 按名称作用于一个建筑组（bg:bg_logging） | building_group |
| bt | 作用于一种建筑类型，示例：bt:building_tooling_workshops | building_type |
| c | 作用于指定 tag 的国家，示例：c:GBR | country |
| catalyst_type | 按名称作用于一种外交催化剂类型（catalyst_type:catalyst_relations_level_improved） | diplomatic_catalyst_type |
| cd | 作用于指定 tag 的国家定义，示例：cd:FRA | country_definition |
| company_type | 按名称作用于一种公司类型（company_type:company_rheinmetall） | company_type |
| cu | 作用于指定 key 的文化，示例：cu:welsh | culture |
| define | 引用数值或颜色 define 的值：define:Namespace\|Name | value |
| flag | 一个本地化键，例如 flag:the_boss | flag |
| g | 作用于指定 key 的商品，示例：g:iron | goods |
| global_gdp | 获取全球年度预测 GDP | value |
| global_productivity | 作用于全球生产率数值（示例：global_productivity:high_threshold） | value |
| global_var | 按名称引用之前设置的全局变量，例如：global_var:important_thing | 不定 |
| harvest_condition_type | 按名称作用于一种收成状况类型（harvest_condition_type:drought） | harvest_condition_type |
| i | 作用于指定 key 的意识形态，示例：i:ideology_patriarchal | ideology |
| identity | 按名称作用于强权集团的身份（identity:key） | power_bloc_identity |
| ideology | 双重用途 按名称作用于一种意识形态（ideology:ideology_anarchist） 作用于 scope 人物的意识形态 | ideology |
| ig_trait | 作用于指定 key 的利益集团特质，示例：ig_trait:ig_trait_xenophobia | interest_group_trait |
| ig_type | 作用于一种利益集团类型，示例：ig_type:ig_landowners | interest_group_type |
| infamy_threshold | 作用于用于比较的恶名等级阈值（infamy_threshold:infamous） | value |
| is_setup | 作用于 true/false，表示游戏状态是否正在初始化！ | boolean |
| je_tutorial | 作用于当前激活教程课程的日志条目（不要在教程之外使用） | journal_entry |
| law_type | 按名称（law_type:law_protected_speech）或从 scoped 法律作用于一种法律类型 | law_type |
| lobby_type | 按名称作用于一种政治游说团类型（lobby_type:lobby_pro_country） | political_lobby_type |
| local_var | 按名称引用之前设置的局部变量，例如：local_var:person_of_interest | 不定 |
| mobilization_option | 按名称作用于一个动员选项（mobilization_option:key） | mobilization_option |
| movement_type | 按名称作用于一种政治运动类型（movement_type:movement_religious_majority） | political_movement_type |
| named_script_value | 一个 script value，会在其使用的上下文中计算并返回其值 | color, value |
| no | 布尔字面值，表示 false | boolean |
| p | 作用于指定十六进制 key 的省份，示例：p:x1A6E5B | province |
| play_type | 按名称作用于一种外交博弈类型（play_type:dp_default_treaty_article） | diplomatic_play_type |
| player | 作用于玩家（不要在教程之外使用） | country |
| pop_type | 按名称作用于一个人口类型（pop_type:laborers） | pop_type |
| prev | 上一个 scope | 不定 |
| principle | 按名称作用于一条强权集团原则（principle:key） | power_bloc_principle |
| principle_group | 按名称作用于一个强权集团原则组（principle_group:key） | power_bloc_principle_group |
| rank_value | 作用于特定国家等级的等级值（rank_value:great_power） | value |
| rel | 作用于指定 key 的宗教，示例：rel:catholic | religion |
| relations_threshold | 作用于用于比较的关系等级阈值（relations_threshold:warm） | value |
| root | 当前顶层 scope 的头，例如事件的接收者、决议的执行者 | 不定 |
| s | 作用于指定 key 的州区域，示例：s:STATE_UTAH | state_region |
| scope | 按名称引用之前保存的 scope，例如：scope:target | 不定 |
| ship_group | 从一艘舰船作用于其所属编组，或按名称作用于一个舰船编组（ship_group:ship_group_capital_ships） | ship_group |
| ship_type | 按名称作用于一种舰船类型（ship_type:ship_type_frigate） | ship_type |
| sr | 作用于指定 key 的战略区域，示例：sr:region_persia | strategic_region |
| strait_type | 按名称作用于一种海峡类型（strait_type:key） | strait_type |
| tension_threshold | 作用于用于比较的紧张度等级阈值（tension_threshold:warm） | value |
| this | 当前 scope | 不定 |
| unit_type | 按名称作用于一种作战单位类型（unit_type:key） | combat_unit_type |
| value | 数值字面值，例如：1、5.2、-6 | value |
| yes | 布尔字面值，表示 true | boolean |

### 战斗（Battle）scope

| Event target | 描述 | 目标 scope |
|---|---|---|
| attacker_side | 从一场战斗作用于进攻方对应的 BattleSide | battle_side |
| defender_side | 从一场战斗作用于防守方对应的 BattleSide | battle_side |
| front | 从多种 scope 作用于一条前线 从战斗作用于其发生的前线 从人物作用于其所在或正在前往的前线 从军事编队作用于其当前所在的前线 从省份作用于包含该省的前线 从入侵作用于入侵前线 | front |

### 建筑 scope

| Event target | 描述 | 目标 scope |
|---|---|---|
| group | 从建筑对象或建筑类型作用于其所属建筑组 | building_group |
| level | 作用于一个建筑的等级 | value |
| level_after_queued_constructions | 作用于一个建筑在所有排队中建造完成后的等级 | value |
| market | 作用于该对象的市场 | market |
| modifier | 作用于当前对象所拥有的指定 key 的 modifier 类型之值，示例：modifier:country_influence_add | boolean, value |
| owner | 作用于对象的拥有国 | country |
| region | 作用于该对象的战略区域！ | strategic_region |
| state | 作用于该对象所在的州 | state |
| training_rate | 作用于一个建筑当前每周最大训练速率 | value |
| type | 从一个对象作用于其类型 | amendment_type, building_type, company_type, diplomatic_play_type, harvest_condition_type, institution_type, interest_group_type, law_type, political_movement_type, ship_type, strait_type |

### 人物 scope

| Event target | 描述 | 目标 scope |
|---|---|---|
| average_progressiveness | 获取 scope 人物或利益集团的平均进步度 | value |
| command_limit_num_units | 获取一名指挥官根据其指挥上限通常能从其军事编队获得的基础单位数量 | value |
| commander_military_formation | 作用于人物的军事编队。 | military_formation |
| culture | 作用于人口或人物的文化 | culture |
| front | 从多种 scope 作用于一条前线 从战斗作用于其发生的前线 从人物作用于其所在或正在前往的前线 从军事编队作用于其当前所在的前线 从省份作用于包含该省的前线 从入侵作用于入侵前线 | front |
| home_country | 作用于流亡者的母国 | country |
| ideology | 双重用途 按名称作用于一种意识形态（ideology:ideology_anarchist） 作用于 scope 人物的意识形态 | ideology |
| interest_group | 作用于该人物所属的利益集团！ | interest_group |
| interest_group_type | 作用于 scope 人物所属利益集团的类型 | interest_group_type |
| modifier | 作用于当前对象所拥有的指定 key 的 modifier 类型之值，示例：modifier:country_influence_add | boolean, value |
| num_active_ships | 获取一个国家、指挥官或军事编队的现役舰船数量，或获取该省份内与指定国家结盟的军事编队的现役舰船数量 | value |
| num_active_ships_in_battle | 获取一个国家、指挥官或军事编队的参战现役舰船数量，或获取该省份内与指定国家结盟的军事编队的参战现役舰船数量 | value |
| num_active_ships_not_in_battle | 获取一个国家、指挥官或军事编队的未参战现役舰船数量，或获取该省份内与指定国家结盟的军事编队的未参战现役舰船数量 | value |
| num_battalions | 返回一名指挥官麾下现役营的数量 | value |
| num_mobilized_battalions | 返回一名将军麾下已完全动员单位数量 | value |
| num_non_destroyed_ships | 获取一个国家、指挥官或军事编队的未被击毁舰船数量，或获取该省份内与指定国家结盟的军事编队的未被击毁舰船数量 | value |
| num_non_destroyed_ships_in_battle | 获取一个国家、指挥官或军事编队的参战中未被击毁舰船数量，或获取该省份内与指定国家结盟的军事编队的参战中未被击毁舰船数量 | value |
| num_non_destroyed_ships_not_in_battle | 获取一个国家、指挥官或军事编队的未参战且未被击毁舰船数量，或获取该省份内与指定国家结盟的军事编队的未参战且未被击毁舰船数量 | value |
| num_ships | 获取一个国家、指挥官或军事编队的舰船数量，或获取该省份内与指定国家结盟的军事编队的舰船数量 | value |
| num_ships_in_battle | 获取一个国家、指挥官或军事编队的参战舰船数量，或获取该省份内与指定国家结盟的军事编队的参战舰船数量 | value |
| num_ships_not_in_battle | 获取一个国家、指挥官或军事编队的未参战舰船数量，或获取该省份内与指定国家结盟的军事编队的未参战舰船数量 | value |
| num_units | 获取一名指挥官或军事编队的现役单位数量 获取该省份内与指定国家结盟的军事编队的现役单位数量 | value |
| num_units_in_battle | 获取一名指挥官或军事编队的参战现役单位数量 获取该省份内与指定国家结盟的军事编队的参战现役单位数量 | value |
| num_units_not_in_battle | 获取一名指挥官或军事编队的未参战现役单位数量 获取该省份内与指定国家结盟的军事编队的未参战现役单位数量 | value |
| num_units_share | 一名指挥官在考虑其指挥上限后所拥有的单位份额。示例：若该人物的指挥上限为 30，舰队总指挥上限为 60，编队总共有 50 支小型舰队，则该人物在其战斗中应分得 25 支小型舰队 | value |
| opposing_commander | 从战斗中的一名人物作用于战斗另一方的人物 | character |
| owner | 作用于对象的拥有国 | country |
| political_movement | 若在人物 scope 中使用，作用于该人物支持的政治运动。若在革命内战 scope 中使用，作用于发起革命的运动。若在利益集团 scope 中使用，作用于该集团的主导运动。 | political_movement |
| popularity | 获取 scope 人物的声望，通常在 -100 到 +100 之间 | value |
| religion | 作用于国家或国家定义的主要宗教，或人口的宗教 | religion |

### 国家 scope

| Event target | 描述 | 目标 scope |
|---|---|---|
| active_law | 作用于 scope 国家在指定法律组中已生效的法律（active_law:lawgroup_trade_policy） | law |
| ai_army_comparison | 作用于两国间的陆军实力对比（示例：value = ai_army_comparison:root） | value |
| ai_gdp_comparison | 作用于两国间的 GDP 对比（示例：value = ai_army_comparison:root） | value |
| ai_ideological_opinion | 作用于 AI 对目标国家在意识形态上对 scope 国家的看法（示例：value = ai_ideological_opinion:root） | value |
| ai_navy_comparison | 作用于两国间的海军实力对比（示例：value = ai_navy_comparison:root） | value |
| ai_subject_value | 作用于 AI 对让 scope 国家成为目标国附属国的意愿（示例：value = ai_subject_value:root） | value |
| ai_transit_rights_value | 作用于 AI 对获得穿越目标国通行权的意愿（示例：value = ai_transit_rights_value:root） | value |
| ai_treaty_fairness | 作用于 AI 对与目标国现有条约条款（对双方）公平程度的评估（示例：value = ai_treaty_fairness_score:root） | value |
| ai_treaty_value | 作用于 AI 对与目标国现有条约条款对自身有利程度的评估（示例：value = ai_treaty_value:root） | value |
| army_size | scope 国家的营数量，不含当前已征召的征召兵。 | value |
| army_size_including_conscripts | scope 国家的营数量，含当前已征召的征召兵。 | value |
| army_size_including_raised_conscripts | scope 国家的营数量，含当前已征召的征召兵，不含未征召的征召兵。 | value |
| average_expected_sol | 获取 scope 的平均预期生活水平 | value |
| average_sol | 获取 scope 的平均生活水平 | value |
| building_levels | 获取 scope 国家的非自给建筑总等级数 | value |
| cached_ai_coastal_population | 作用于 AI 支出变量中记录的沿海总人口（示例：value = cached_ai_coastal_population） | value |
| cached_ai_incorporated_coastal_population | 作用于 AI 支出变量中记录的已合并沿海人口总数（示例：value = cached_ai_incorporated_coastal_population） | value |
| cached_ai_incorporated_population | 作用于 AI 支出变量中记录的已合并人口总数（示例：value = cached_ai_incorporated_population） | value |
| cached_ai_overseas_subject_population | 作用于 AI 支出变量中记录的非相邻直属附属国人口总数（示例：value = cached_ai_overseas_subject_population） | value |
| cached_ai_subject_population | 作用于 AI 支出变量中记录的直属附属国人口总数（示例：value = cached_ai_subject_population） | value |
| cached_ai_total_population | 作用于 AI 支出变量中记录的人口总数（示例：value = cached_ai_total_population） | value |
| cached_ai_unincorporated_coastal_population | 作用于 AI 支出变量中记录的未合并沿海人口总数（示例：value = cached_ai_unincorporated_coastal_population） | value |
| cached_ai_unincorporated_population | 作用于 AI 支出变量中记录的未合并人口总数（示例：value = cached_ai_unincorporated_population） | value |
| capital | 作用于一个国家的首都州 | state |
| civil_war_origin_country | 作用于内战国家的起源国 | country |
| colonial_growth_per_colony | 作用于该国家每个殖民地的殖民增长值（示例：colonial_growth_per_colony > 0） | value |
| company | 作用于 scope 国家指定公司类型的公司（company:company_rheinmetall） | company |
| country_definition | 作用于国家的定义 | country_definition |
| credit | 作用于该国当前可借取的最大信贷额度 | value |
| currently_enacting_law | 从一个国家作用于其当前正在制定的法律 | law |
| diplomatic_pact_expense_ratio | 作用于该国外交协定支出与收入的比率，截取在 0-1 之间（示例：value = diplomatic_pact_expense_ratio） | value |
| flagship | 获取 scope 国家的旗舰 | ship |
| gdp | 获取 scope 国家的年度预测 GDP | value |
| get_ruler_for | 从国家作用于在指定权力移交类型下将成为统治者的人物 get_ruler_for:parliamentary_elective = { effects... } | character |
| government_size | 获取 scope 国家当前政府中政党与独立利益集团的数量 | value |
| heir | 作用于一个国家的继承人 | character |
| ig | 作用于该国拥有的指定 key 的利益集团，示例：ig:ig_armed_forces | interest_group |
| imposed_law | 从一个国家作用于当前被强加于其的法律（无论是否在制定中） | law |
| imposer_of_law | 从一个国家作用于当前对其强加法律的国家 | country |
| income | 获取 scope 国家当前的每周收入 | value |
| income_transfer_expenses | 作用于 scope 国家通过条约与协定向他国转移的金额（示例：income_transfer_expenses >= 100） | value |
| income_transfer_relative_expenses | 作用于该国通过条约与协定向他国转移的收入比例（示例：income_transfer_relative_expenses >= 0.2） | value |
| infamy | 作用于 scope 国家的恶名（示例：infamy >= 2） | value |
| institution | 按名称作用于一个国家的机构（institution:institution_health_system） | institution |
| investment_pool_income | 获取 scope 国家当前的每周投资池收入 | value |
| je | 作用于该国拥有的指定 key 的日志条目，示例：je:je_antarctica | journal_entry |
| legitimacy | 作用于该国当前的合法性数值 | value |
| lobby_foreign_anti_clout | 作用于针对特定国家的所有反该国外交政策游说团的总政治力量（lobby_foreign_anti_clout:root >= 0.2） | value |
| lobby_foreign_pro_clout | 作用于针对特定国家的所有亲该国外交政策游说团的总政治力量（lobby_foreign_pro_clout:root >= 0.2） | value |
| lobby_in_government_foreign_anti_clout | 作用于针对特定国家、执政的所有反该国外交政策游说团的总政治力量（lobby_in_government_foreign_anti_clout:root >= 0.2） | value |
| lobby_in_government_foreign_pro_clout | 作用于针对特定国家、执政的所有亲该国外交政策游说团的总政治力量（lobby_in_government_foreign_pro_clout:root >= 0.2） | value |
| lobby_war_opposition | 作用于所有反对 scope 战争的游说团的总政治力量（lobby_war_opposition:root >= 0.2） | value |
| lobby_war_support | 作用于所有支持 scope 战争的游说团的总政治力量（lobby_war_support:root >= 0.2） | value |
| market | 作用于该对象的市场 | market |
| market_capital | 作用于一个国家的市场首府 | state |
| migration_pull | 获取一个州的迁移拉力，或一个国家的大规模迁移拉力。 | value |
| military_expenses | 获取 scope 国家当前的军事开支（奴隶、工资和商品） | value |
| military_expenses_share | 获取 scope 国家当前军事开支（奴隶、工资和商品）相对于总开支的比例 | value |
| modifier | 作用于当前对象所拥有的指定 key 的 modifier 类型之值，示例：modifier:country_influence_add | boolean, value |
| mutual_trade_value_with_country | 作用于两个市场之间贸易路线上交易商品的总基础价值（示例：mutual_trade_value_with_country:root >= 1000） | value |
| naval_combat_power | 作用于该国的海军战力（示例：naval_combat_power > 100） | value |
| naval_hostility_average_damage_dealt | 作用于该国在回溯期内其主动发起的海军敌对行动中造成的平均伤害。若无敌对行动则返回 -1。 | value |
| naval_hostility_damage | 作用于该国在当前海军敌对行动中对另一国造成的伤害点数（示例：naval_hostility_damage:root >= 50） | value |
| naval_vulnerability | 作用于该国基于贸易依赖度和沿海 GDP 份额的海军脆弱度评分，上限为某个 define 的最大值 | value |
| navy_size | scope 国家的小型舰队数量。 | value |
| num_active_interests | 作用于一个国家拥有的活跃利益数量 num_active_interests > 5 | value |
| num_active_natural_interests | 作用于一个国家拥有的活跃天然利益数量 num_active_natural_interests > 5 | value |
| num_active_plays | 获取 scope 国家当前已发起的外交博弈数量 | value |
| num_active_ships | 获取国家、指挥官或军事编队的现役船只数量，或获取省份内与指定国家同盟的军事编队的现役船只数量 | value |
| num_active_ships_in_battle | 获取国家、指挥官或军事编队的战斗中现役船只数量，或获取省份内与指定国家同盟的军事编队的战斗中现役船只数量 | value |
| num_active_ships_not_in_battle | 获取国家、指挥官或军事编队的非战斗中现役船只数量，或获取省份内与指定国家同盟的军事编队的非战斗中现役船只数量 | value |
| num_admirals | Scope 到国家的海军上将数量 | value |
| num_alliances | 获取 scope 国家的同盟总数（示例：num_alliances:root >= 2） | value |
| num_alliances_and_defensive_pacts_with_allies | Scope 到目标国家与 scope 国家的盟友之间的同盟数量（示例：num_alliances_and_defensive_pacts_with_allies:root >= 2） | value |
| num_alliances_and_defensive_pacts_with_rivals | Scope 到目标国家与 scope 国家的对手之间的同盟及防御条约数量（示例：num_alliances_and_defensive_pacts_with_rivals:root >= 2） | value |
| num_characters | Scope 到国家的人物数量 | value |
| num_colony_projects | 获取 scope 国家当前未完成／进行中的殖民地项目数量 | value |
| num_commanders | Scope 到国家的指挥官数量 | value |
| num_defensive_pacts | Scope 到目标国家拥有的防御条约总数（示例：num_defensive_pacts >= 2） | value |
| num_generals | Scope 到国家的将军数量 | value |
| num_income_transfer_pacts | Scope 到目标国家拥有的（向他国）转移收入的条约总数（示例：num_income_transfer_pacts >= 2） | value |
| num_income_transfer_treaty_articles | Scope 到目标国家拥有的（向他国）转移收入的条约条款总数（示例：num_income_transfer_treaty_articles >= 2） | value |
| num_income_transfers | Scope 到目标国家拥有的（向他国）转移收入的条约及条款总数（示例：num_income_transfers >= 2） | value |
| num_incorporated_states | 获取 scope 国家当前已合并州的数量 | value |
| num_interests | Scope 到国家拥有的利益数量（包括未激活的）num_interests > 5 | value |
| num_natural_interests | Scope 到国家拥有的自然利益数量（包括未激活的）num_natural_interests > 5 | value |
| num_non_destroyed_ships | 获取国家、指挥官或军事编队的未损毁船只数量，或获取省份内与指定国家同盟的军事编队的未损毁船只数量 | value |
| num_non_destroyed_ships_in_battle | 获取国家、指挥官或军事编队的战斗中未损毁船只数量，或获取省份内与指定国家同盟的军事编队的战斗中未损毁船只数量 | value |
| num_non_destroyed_ships_not_in_battle | 获取国家、指挥官或军事编队的非战斗中未损毁船只数量，或获取省份内与指定国家同盟的军事编队的非战斗中未损毁船只数量 | value |
| num_obligations_earned | 从国家 Scope 到他国欠该国的义务（Obligation）数量（＝该国已获得的） | value |
| num_pending_events | Scope 到 scope 国家中待处理事件的数量，可按总体或指定类别 num_pending_events > 0 num_pending_events:enactment > 0 | value |
| num_politicians | Scope 到国家的政治家人数 | value |
| num_positive_relations | 获取当前与 scope 国家关系为正的国家数量 | value |
| num_queued_constructions | Scope 到目标国家排队的建造总数（示例：num_queued_constructions >= 2） | value |
| num_queued_government_constructions | Scope 到目标国家排队的政府建造总数（示例：num_queued_government_constructions >= 2） | value |
| num_queued_private_constructions | Scope 到目标国家排队的私人建造总数（示例：num_queued_private_constructions >= 2） | value |
| num_rivals | Scope 到目标国家的对手总数（示例：num_rivals >= 2） | value |
| num_ruling_igs | 获取 scope 国家当前政府中利益集团的数量 | value |
| num_shared_rivals | Scope 到 scope 国家与目标国家共同的对手数量（示例：num_shared_rivals:root >= 2） | value |
| num_ships | 获取国家、指挥官或军事编队的船只数量，或获取省份内与指定国家同盟的军事编队的船只数量 | value |
| num_ships_in_battle | 获取国家、指挥官或军事编队的战斗中船只数量，或获取省份内与指定国家同盟的军事编队的战斗中船只数量 | value |
| num_ships_not_in_battle | 获取国家、指挥官或军事编队的非战斗中船只数量，或获取省份内与指定国家同盟的军事编队的非战斗中船只数量 | value |
| num_ships_of_group | scope 国家或军事编队中指定船只编队的船只数量 | value |
| num_states | 获取 scope 国家当前的州数量 | value |
| num_unincorporated_states | 获取 scope 国家当前未合并州的数量 | value |
| overlord | Scope 到该国家的直接宗主国 | country |
| owner | Scope 到对象的拥有国 | country |
| owning_company | Scope 到拥有该 scope 国家的公司 | company |
| pirated_trade_value_by | Scope 到目标国家每周从该国劫掠的商品基础价值平均值（示例：pirated_trade_value_by:root >= 50） | value |
| power_bloc | Scope 到该国家的强权集团 | power_bloc |
| principal | 获取该国当前的债务本金 | value |
| py | Scope 到该国属于指定键值的活跃政党，示例：py:communist_party | party |
| relations | Scope 到两国之间的关系（示例：relations:root >= 2） | value |
| relations_change_rate | Scope 到两国关系进展的每日变化（示例：relations_change_rate:root > 0） | value |
| religion | Scope 到国家或国家定义的主要宗教，或人口的宗教 | religion |
| ruler | Scope 到国家的统治者 | character |
| strait_trade_importance_by | Scope 到该国经由目标国家控制的海峡进行贸易的商品贸易重要度。若控制者控制海峡两侧，累计值将乘以 STRAIT_FULL_CONTROL_TRADE_IMPORTANCE_MULT（示例：strait_trade_importance_by:root >= 100） | value |
| technology_being_researched | Scope 到国家当前正在研究的技术 | technology |
| techs_researched | Scope 到国家当前已研究的科技数量 | value |
| tension | Scope 到两国之间的紧张度（示例：tension:root >= 2） | value |
| top_overlord | Scope 到该国的最上层宗主国 | country |
| total_crew_needed | 获取国家所有船只所需的船员总数 | value |
| total_export_value | Scope 到 scope 国家向世界市场出口的总价值（示例：total_export_value >= 1000） | value |
| total_import_value | Scope 到 scope 国家从世界市场进口的总价值（示例：total_import_value >= 1000） | value |
| total_marine_capacity | 获取国家所有舰队的海军陆战队运力总数 | value |
| total_trade_value | Scope 到 scope 国家与世界市场贸易的总价值（示例：total_trade_value >= 1000） | value |

### 外交 scope

| Event target | 说明 | 目标 scope |
|---|---|---|
| initiator | Scope 到对象的发起国 | country |
| region | Scope 到该对象的战略区域！ | strategic_region |
| target | Scope 到对象的目标 | varies |
| type | 从对象 Scope 到其类型 | amendment_type, building_type, company_type, diplomatic_play_type, harvest_condition_type, institution_type, interest_group_type, law_type, political_movement_type, ship_type, strait_type |
| war | 从外交博弈 Scope 到其对应的战争 | war |

| Event target | 说明 | 目标 scope |
|---|---|---|
| diplomatic_pact_other_country | Scope 到该外交条约中的另一国家，示例：diplomatic_pact_other_country(root) | country |
| first_country | Scope 到以下任意对象的第一国（first_country）：外交条约、条约、条约选项、条约条款的条约、条约条款选项（仅限双边条款类型） | country |
| second_country | Scope 到以下任意对象的第二国（second_country）：外交条约、条约、条约选项、条约条款的条约、条约条款选项（仅限双边条款类型） | country |

| Event target | 说明 | 目标 scope |
|---|---|---|
| player_owed_obligation_days_left | Scope 到外交关系 scope 中某项义务的剩余天数（示例：obligation_days_left >= 2） | value |
| scope_relations | Scope 到外交关系 scope 中的关系值（示例：scope_relations >= 2） | value |
| scope_tension | Scope 到外交关系 scope 中的紧张度值（示例：scope_tension >= 2） | value |
| total_pirated_trade_value | Scope 到外交关系 scope 中两国间通过海盗行为劫掠的商品每周基础价值总平均值（示例：total_pirated_trade_value >= 100） | value |

### 商品 scope

| Event target | 说明 | 目标 scope |
|---|---|---|
| base_price | 获取该 scope 商品的基准价格 | value |

| Event target | 说明 | 目标 scope |
|---|---|---|
| ai_treaty_export_value | Scope 到目标国家 AI 对 scope 市场商品的出口意愿（示例：value = ai_market_export_value:root） | value |
| ai_treaty_import_value | Scope 到目标国家 AI 通过条约进口 scope 市场商品的意愿（示例：value = ai_market_import_value:root） | value |
| ai_treaty_trade_value | Scope 到目标国家 AI 对 scope 市场商品的进出口意愿（示例：value = ai_market_trade_value:root） | value |
| goods | Scope 到贸易路线贸易的商品 | goods |
| largest_exporting_market | Scope 到将该 scope 市场商品向本地市场出口最多的市场 | market |
| largest_importing_market | Scope 到从本地市场进口该 scope 市场商品最多的市场 | market |
| market | Scope 到对象所在的市场 | market |
| market_export_cap | 根据该 scope 市场商品的生产，获取市场可出口的最大商品数量 | value |
| market_import_cap | 根据该 scope 市场商品的消费，获取市场可进口的最大商品数量 | value |
| owner | Scope 到对象的拥有国 | country |
| treaty_exports | 获取该商品向该 scope 市场商品所在市场的当前条约（而非世界市场）出口数量 | value |
| treaty_imports | 获取该商品向该 scope 市场商品所在市场的当前条约（而非世界市场）进口数量 | value |

| Event target | 说明 | 目标 scope |
|---|---|---|
| goods | Scope 到贸易路线贸易的商品 | goods |
| market | Scope 到对象所在的市场 | market |

### 法律 scope

| Event target | 说明 | 目标 scope |
|---|---|---|
| currently_active_law_in_group | 从某法律 Scope 到该法律组中当前生效的法律 | law |
| imposer_of_law | 从国家 Scope 到当前对其强加某法律的国家 | country |
| law_type | 通过名称（law_type:law_protected_speech）或从某个 scope 法律 Scope 到其法律类型 | law_type |
| owner | Scope 到对象的拥有国 | country |
| type | 从对象 Scope 到其类型 | amendment_type, building_type, company_type, diplomatic_play_type, harvest_condition_type, institution_type, interest_group_type, law_type, political_movement_type, ship_type, strait_type |

### 市场 scope

| Event target | 说明 | 目标 scope |
|---|---|---|
| market | Scope 到对象所在的市场 | market |
| mg | 从市场 Scope 到指定键值的市场商品（MarketGoods），（示例：mg:tools） | market_goods |
| modifier | Scope 到当前对象拥有的指定键值修正类型的数值，示例：modifier:country_influence_add | boolean, value |
| owner | Scope 到对象的拥有国 | country |
| participants | 获取该 scope 市场的参与国总数 | value |
| state | Scope 到对象所在的州 | state |
| trade_center | Scope 到该市场的贸易中心州！ | state |

### 人口 scope

| Event target | 说明 | 目标 scope |
|---|---|---|
| culture | Scope 到人口或人物的文化 | culture |
| home_country | Scope 到流亡者的祖国 | country |
| owner | Scope 到对象的拥有国 | country |
| pop_weight_modifier_scale | 获取该人口的权重修正缩放乘数 | value |
| religion | Scope 到国家或国家定义的主要宗教，或人口的宗教 | religion |
| state | Scope 到对象所在的州 | state |
| workplace | Scope 到人口的工作场所 | building |

### 强权集团 scope

| Event target | 说明 | 目标 scope |
|---|---|---|
| modifier | Scope 到当前对象拥有的指定键值修正类型的数值，示例：modifier:country_influence_add | boolean, value |
| num_mandates | Scope 到该 scope 强权集团的可用信条数量（power_bloc.num_mandates > 0） | value |
| power_bloc_leader | Scope 到该强权集团的领导国 | country |
| power_struggle_contender | 若存在权力斗争，Scope 到竞争国 | country |

### 州 scope

| Event target | 说明 | 目标 scope |
|---|---|---|
| ai_state_value | Scope 到目标国家 AI 对拥有该 scope 州的意愿（示例：value = ai_state_value:root） | value |
| ai_treaty_port_value | Scope 到目标国家 AI 在该 scope 州设立条约港的意愿（示例：value = ai_treaty_port_value:root） | value |
| average_expected_sol | 获取该 scope 的平均预期生活水平 | value |
| average_sol | 获取该 scope 的平均生活水平 | value |
| b | Scope 到该州中指定键值的建筑，示例：b:building_port | building |
| controller | Scope 到对象的控制国 | country |
| decree_cost | Scope 到某州针对特定法令的成本 authority > decree_cost:decree_road_maintaintenance | value |
| gdp | 获取该 scope 国家的年度预测 GDP | value |
| land_controller_hq | 返回省份或州控制者的陆地总部 | hq |
| land_hq | 返回省份或州拥有者的本地陆地总部 | hq |
| market | Scope 到对象所在的市场 | market |
| mass_migration_culture | Scope 到某州大规模迁移的目标文化 | culture |
| migration_pull | 获取某州的迁移拉力，或某国的大规模迁移拉力。 | value |
| modifier | Scope 到当前对象拥有的指定键值修正类型的数值，示例：modifier:country_influence_add | boolean, value |
| nf | Scope 到应用于该州的指定键值的法令，示例：nf:decree_road_maintaintenance | decree |
| num_provinces | 获取该 scope 实体当前的省份数量 | value |
| num_world_market_hub_trade_center_levels | 获取与该 scope 世界市场枢纽州关联的贸易中心等级总数 | value |
| owner | Scope 到对象的拥有国 | country |
| population_below_expected_sol | Scope 到该州人口中低于其预期生活水平的当前百分比（0-1） | value |
| region | Scope 到该对象的战略区域！ | strategic_region |
| sg | 从州 Scope 到指定键值的州商品（StateGoods），示例：sg:wood | state_goods |
| state_region | Scope 到某州的州区域 | state_region |
| theater | 从战侧或州 Scope 到其战区 | theater |
| world_market_hub | Scope 到与该 scope 州关联的世界市场枢纽州 | state |
### 条约 scope

| Event target | 描述 | 目标 scope |
|---|---|---|
| amended_treaty | 转到当前 scope 条约所修订的那份条约 | treaty |
| binding_period | 获取当前 scope 条约签署时的原始约束期（以天为单位） | value |
| enforced_on_country | 转到被强制执行的条约的 enforced_on_country | country |
| enforcer_country | 转到被强制执行的条约的 enforcer_country | country |
| first_country | 转到以下任意对象的 first_country：外交条约 外交条约选项 条约条款所属的条约 条约条款选项（仅限双向条款类型） | country |
| remaining_binding_period | 获取当前 scope 条约当前剩余的约束期（以天为单位） | value |
| second_country | 转到以下任意对象的 second_country：外交条约 外交条约选项 条约条款所属的条约 条约条款选项（仅限双向条款类型） | country |

| Event target | 描述 | 目标 scope |
|---|---|---|
| first_country | 转到以下任意对象的 first_country：外交条约 外交条约选项 条约条款所属的条约 条约条款选项（仅限双向条款类型） | country |
| input_building_type | 转到条约条款中输入的建筑类型 | building_type |
| input_company | 转到条约条款中输入的公司 | company |
| input_country | 转到条约条款中输入的国家 | country |
| input_goods | 转到条约条款中输入的商品 | goods |
| input_law | 转到条约条款中输入的法律 | law_type |
| input_market_goods | 转到条约条款中输入的市场商品（示例：input_market_goods:root） | market_goods |
| input_quantity | 转到条约条款中输入的数量 | value |
| input_ship | 转到条约条款中输入的舰船 | ship |
| input_state | 转到条约条款中输入的州 | state |
| input_strategic_region | 转到条约条款中输入的战略区域 | strategic_region |
| second_country | 转到以下任意对象的 second_country：外交条约 外交条约选项 条约条款所属的条约 条约条款选项（仅限双向条款类型） | country |
| shipping_lane | 转到军事编队或条约条款（商品转让）的航运路线 | shipping_lanes |
| source_country | 转到以下任意对象的 source_country：条约条款（仅限单向条款类型） 条约条款选项（仅限单向条款类型） | country |
| target_country | 转到以下任意对象的 target_country：条约条款（仅限单向条款类型） 条约条款选项（仅限单向条款类型） | country |
| treaty | 转到条约条款所属的条约 | treaty |

| Event target | 描述 | 目标 scope |
|---|---|---|
| first_country | 转到以下任意对象的 first_country：外交条约 外交条约选项 条约条款所属的条约 条约条款选项（仅限双向条款类型） | country |
| input_building_type | 转到条约条款中输入的建筑类型 | building_type |
| input_company | 转到条约条款中输入的公司 | company |
| input_country | 转到条约条款中输入的国家 | country |
| input_goods | 转到条约条款中输入的商品 | goods |
| input_law | 转到条约条款中输入的法律 | law_type |
| input_market_goods | 转到条约条款中输入的市场商品（示例：input_market_goods:root） | market_goods |
| input_quantity | 转到条约条款中输入的数量 | value |
| input_ship | 转到条约条款中输入的舰船 | ship |
| input_state | 转到条约条款中输入的州 | state |
| input_strategic_region | 转到条约条款中输入的战略区域 | strategic_region |
| second_country | 转到以下任意对象的 second_country：外交条约 外交条约选项 条约条款所属的条约 条约条款选项（仅限双向条款类型） | country |
| source_country | 转到以下任意对象的 source_country：条约条款（仅限单向条款类型） 条约条款选项（仅限单向条款类型） | country |
| target_country | 转到以下任意对象的 target_country：条约条款（仅限单向条款类型） 条约条款选项（仅限单向条款类型） | country |

### 战争 scope

| Event target | 描述 | 目标 scope |
|---|---|---|
| attacker_warleader | 转到战争的进攻方战时领袖 | country |
| defender_warleader | 转到战争的防守方战时领袖 | country |
| diplomatic_play | 从战争转到其对应的外交博弈 | diplomatic_play |

## 所有 event target

| Event target | 描述 | 来源 scope | 目标 scope |
|---|---|---|---|
| active_law | 转到当前 scope 国家在指定法律组中的现行法律（active_law:lawgroup_trade_policy） | country | law |
| ai_army_comparison | 转到两国之间的陆军实力对比（示例：value = ai_army_comparison:root） | country | value |
| ai_colonization_value | 转到目标国家 AI 对某一战略区域的殖民意愿（示例：value = ai_colonization_value:root） | strategic_region | value |
| ai_gdp_comparison | 转到两国之间的 GDP 对比（示例：value = ai_army_comparison:root） | country | value |
| ai_ideological_opinion | 转到 AI 对当前 scope 国家关于目标国家的意识形态看法（示例：value = ai_ideological_opinion:root） | country | value |
| ai_navy_comparison | 转到两国之间的海军实力对比（示例：value = ai_navy_comparison:root） | country | value |
| ai_state_value | 转到目标国家 AI 对拥有当前 scope 州的意愿（示例：value = ai_state_value:root） | state | value |
| ai_subject_value | 转到目标国家 AI 想让当前 scope 国家成为其附属国的意愿（示例：value = ai_subject_value:root） | country | value |
| ai_transit_rights_value | 转到 AI 想获得通过目标国家通行权的意愿（示例：value = ai_transit_rights_value:root） | country | value |
| ai_treaty_export_value | 转到目标国家 AI 对出口当前 scope 市场商品的意愿（示例：value = ai_market_export_value:root） | market_goods | value |
| ai_treaty_fairness | 转到 AI 对其与目标国家之间现有条约条款公平性（对双方而言）的评估（示例：value = ai_treaty_fairness_score:root） | country | value |
| ai_treaty_import_value | 转到目标国家 AI 想通过条约进口当前 scope 市场商品的意愿（示例：value = ai_market_import_value:root） | market_goods | value |
| ai_treaty_port_value | 转到目标国家 AI 想在当前 scope 州获得条约港的意愿（示例：value = ai_treaty_port_value:root） | state | value |
| ai_treaty_trade_value | 转到目标国家 AI 想进口和出口当前 scope 市场商品的意愿（示例：value = ai_market_trade_value:root） | market_goods | value |
| ai_treaty_value | 转到 AI 对其与目标国家之间现有条约条款对自身有利程度的评估（示例：value = ai_treaty_value:root） | country | value |
| amended_treaty | 转到当前 scope 条约所修订的那份条约 | treaty, treaty_options | treaty |
| amendment_type | 通过名称转到某一修订类型（amendment_type:key） | none | amendment_type |
| army_size | 当前 scope 国家的营数量，不含当前已征召的征召兵。 | country | value |
| army_size_including_conscripts | 当前 scope 国家的营数量，含当前已征召的征召兵。 | country | value |
| army_size_including_raised_conscripts | 当前 scope 国家的营数量，含当前已征召的征召兵，不含未征召的征召兵。 | country | value |
| array_define | 引用数组 define 中某个数值的值：array_define:Namespace\|Name\|Index。索引从 0 开始。 | none | value |
| attached_law | 从修订 scope 链接到该修订所附加的法律 | amendment | law |
| attacker_side | 从战斗转到对应进攻方的 BattleSide | battle | battle_side |
| attacker_warleader | 转到战争的进攻方战时领袖 | war | country |
| average_defense | 返回与国家同属一方的前线上单位的平均防御 | front | value |
| average_expected_sol | 获取当前 scope 的平均预期生活水平 | country, state | value |
| average_offense | 返回与国家同属一方的前线上单位的平均进攻 | front | value |
| average_progressiveness | 获取当前 scope 人物或利益集团的平均进步性 | character, interest_group | value |
| average_sol | 获取当前 scope 的平均生活水平 | country, state | value |
| b | 转到州内指定键的建筑，示例：b:building_port | state | building |
| base_price | 获取当前 scope 商品的基础价格 | goods | value |
| battle | 从战斗一侧转到战斗本身 | battle_side | battle |
| bg | 通过名称转到某一建筑组（bg:bg_logging） | none | building_group |
| binding_period | 获取当前 scope 条约签署时的原始约束期（以天为单位） | treaty, treaty_options | value |
| bt | 转到某一建筑类型，示例：bt:building_tooling_workshops | none | building_type |
| building | 转到相关建筑 | new_combat_unit | building |
| building_levels | 获取当前 scope 国家非自给建筑的总等级数 | country | value |
| c | 转到指定 tag 的国家，示例：c:GBR | none | country |
| cached_ai_coastal_population | 转到 AI 支出变量中记录的沿海总人口（示例：value = cached_ai_coastal_population） | country | value |
| cached_ai_incorporated_coastal_population | 转到 AI 支出变量中记录的已设为本土的沿海人口总数（示例：value = cached_ai_incorporated_coastal_population） | country | value |
| cached_ai_incorporated_population | 转到 AI 支出变量中记录的已设为本土的人口总数（示例：value = cached_ai_incorporated_population） | country | value |
| cached_ai_overseas_subject_population | 转到 AI 支出变量中记录的不相邻直属附属国的人口总数（示例：value = cached_ai_overseas_subject_population） | country | value |
| cached_ai_subject_population | 转到 AI 支出变量中记录的直属附属国的人口总数（示例：value = cached_ai_subject_population） | country | value |
| cached_ai_total_population | 转到 AI 支出变量中记录的人口总数（示例：value = cached_ai_total_population） | country | value |
| cached_ai_unincorporated_coastal_population | 转到 AI 支出变量中记录的未设为本土的沿海人口总数（示例：value = cached_ai_unincorporated_coastal_population） | country | value |
| cached_ai_unincorporated_population | 转到 AI 支出变量中记录的未设为本土的人口总数（示例：value = cached_ai_unincorporated_population） | country | value |
| capital | 转到国家的首都所在的州 | country | state |
| catalyst_type | 通过名称转到某一外交催化剂类型（catalyst_type:catalyst_relations_level_improved） | none | diplomatic_catalyst_type |
| cd | 转到指定 tag 的国家定义，示例：cd:FRA | none | country_definition |
| civil_war | 转到由当前 scope（革命性）政治运动引发的内战。 | political_movement | civil_war |
| civil_war_origin_country | 转到内战国家的起因国 | country | country |
| colonial_growth_per_colony | 转到国家的单块殖民地殖民增长值（示例：colonial_growth_per_colony > 0） | country | value |
| combat_width | 转到当前 scope 省份的战斗宽度乘数 | province | value |
| command_limit_num_units | 根据指挥官的指挥上限，获取其通常能从所属军事编队获得的基准单位数量 | character | value |
| commander | 从军事编队转到其指挥官人物 | military_formation | character |
| commander_military_formation | 转到人物的军事编队。 | character | military_formation |
| company | 转到当前 scope 国家指定公司类型的公司（company:company_rheinmetall） | country | company |
| company_type | 通过名称转到某一公司类型（company_type:company_rheinmetall） | none | company_type |
| compare_complex_value | 一个需要可解析字符串参数的对比 trigger，会返回其在其使用上下文中的值，例如：scope:root.number_of(armies) | varies | value |
| compare_value | 一个对比 trigger，会返回其在其使用上下文中的值，例如：root.gold | varies | value |
| controller | 转到对象的控制者 | province, state | country |
| country | 转到军事编队或舰船所属的国家 | military_formation, ship | country |
| country_definition | 转到国家的定义 | country | country_definition |
| credit | 转到国家当前可承担的最大信贷额度 | country | value |
| cu | 转到指定键的文化，示例：cu:welsh | none | culture |
| culture | 转到人口或人物的文化 | character, new_combat_unit, political_movement, pop | culture |
| current_hq | 返回当前 scope 军事编队当前的总部（若编队当前未驻扎在任何总部则可能无效） | military_formation | hq |
| currently_active_law_in_group | 从一部法律转到该法律组中当前生效的法律 | law | law |
| currently_enacting_law | 从国家转到其当前正在制定的法律 | country | law |
| decree_cost | 转到州颁布某项法令的费用 authority > decree_cost:decree_road_maintaintenance | state | value |
| defender_side | 从战斗转到对应防守方的 BattleSide | battle | battle_side |
| defender_warleader | 转到战争的防守方战时领袖 | war | country |
| defense | 返回单位的防御评级（含其指挥官带来的影响） | new_combat_unit | value |
| define | 引用数值或颜色 define 的值：define:Namespace\|Name | none | value |
| demoralized | 返回单位的士气受挫人力数量 | new_combat_unit | value |
| detection | 从舰队 scope 链接到舰队中舰船的总侦测 | military_formation | value |
| diplomatic_pact_expense_ratio | 转到该国公使费用占收入的比例，限定在 0-1 之间（示例：value = diplomatic_pact_expense_ratio） | country | value |
| diplomatic_pact_other_country | 转到当前 scope 公约中的另一国，示例：diplomatic_pact_other_country(root) | diplomatic_pact | country |
| diplomatic_play | 从战争转到其对应的外交博弈 | war | diplomatic_play |
| enforced_on_country | 转到被强制执行的条约的 enforced_on_country | treaty | country |
| enforcer_country | 转到被强制执行的条约的 enforcer_country | treaty | country |
| executive | 从公司转到其高管人物 | company | character |
| first_country | 转到以下任意对象的 first_country：外交条约 外交条约选项 条约条款所属的条约 条约条款选项（仅限双向条款类型） | diplomatic_pact, treaty, treaty_article, treaty_article_options, treaty_options | country |
| flag | 一个 localization 键，例如 flag:the_boss | none | flag |
| flagship | 获取当前 scope 国家的旗舰 | country | ship |
| front | 从多种 scope 转到前线：从战斗转到其发生的前线 从人物转到其所在或正前往的前线 从军事编队转到其当前所在的前线 从省份转到包含该省的前线 从入侵转到入侵前线 | battle, character, invasion, military_formation, province | front |
| front_length | 返回前线的省份数量 | front | value |
| g | 转到指定键的商品，示例：g:iron | none | goods |
| gdp | 获取当前 scope 国家或州的年度预测 GDP | country, state | value |
| get_ruler_for | 从国家转到在指定权力移交类型下将成为统治者的人物 get_ruler_for:parliamentary_elective = { effects... } | country | character |
| global_gdp | 获取全球年度预测 GDP | none | value |
| global_productivity | 转到全球生产力数值（示例：global_productivity:high_threshold） | none | value |
| global_var | 通过名称引用先前设置的全局变量，例如：global_var:important_thing | none | varies |
| goal_value | 转到日志条目的目标值 | journal_entry | value |
| goods | 转到贸易路线交易的商品 | market_goods, state_goods | goods |
| government_size | 获取当前 scope 国家政府中政党与独立利益集团的当前数量 | country | value |
| group | 从建筑对象或建筑类型转到其所属的组 | building, building_type | building_group |
| harvest_condition_type | 通过名称转到某一收成条件类型（harvest_condition_type:drought） | none | harvest_condition_type |
| heir | 转到国家的继承人 | country | character |
| home_country | 转到流亡者的祖国 | character, pop | country |
| home_hq | 返回当前 scope 军事编队的本土总部 | military_formation | hq |
| i | 转到指定键的意识形态，示例：i:ideology_patriarchal | none | ideology |
| identity | 通过名称转到强权集团身份（identity:key） | none | power_bloc_identity |
| ideology | 双重用途：通过名称转到某一意识形态（ideology:ideology_anarchist） 转到当前 scope 人物的意识形态 | character, none | ideology |
| ig | 转到属于该国家的指定键的利益集团，示例：ig:ig_armed_forces | country, political_movement | interest_group |
| ig_trait | 转到指定键的利益集团特质，示例：ig_trait:ig_trait_xenophobia | none | interest_group_trait |
| ig_type | 转到某一利益集团类型，示例：ig_type:ig_landowners | none | interest_group_type |
| imposed_law | 从国家转到当前被强加于其的法律（无论是否正在制定） | country | law |
| imposer_of_law | 从国家转到当前对其强加法律的国家 | country, law | country |
| income | 获取当前 scope 国家当前的每周收入 | country | value |
| income_transfer_expenses | 转到当前 scope 国家通过条约与公约向其他国家转移的资金数额（示例：income_transfer_expenses >= 100） | country | value |
| income_transfer_relative_expenses | 转到该国通过条约与公约向其他国家转移的资金占其收入的比例（示例：income_transfer_relative_expenses >= 0.2） | country | value |
| infamy | 转到当前 scope 国家的恶名（示例：infamy >= 2） | country | value |
| infamy_threshold | 转到用于对比目的的恶名等级阈值（infamy_threshold:infamous） | none | value |
| initiator | 转到对象的发起者 | diplomatic_play | country |
| input_building_type | 转到条约条款中输入的建筑类型 | treaty_article, treaty_article_options | building_type |
| input_company | 转到条约条款中输入的公司 | treaty_article, treaty_article_options | company |
| input_country | 转到条约条款中输入的国家 | treaty_article, treaty_article_options | country |
| input_goods | 转到条约条款中输入的商品 | treaty_article, treaty_article_options | goods |
| input_law | 转到条约条款中输入的法律 | treaty_article, treaty_article_options | law_type |
| input_market_goods | 转到条约条款中输入的市场商品（示例：input_market_goods:root） | treaty_article, treaty_article_options | market_goods |
| input_quantity | 转到条约条款中输入的数量 | treaty_article, treaty_article_options | value |
| input_ship | 转到条约条款中输入的舰船 | treaty_article, treaty_article_options | ship |
| input_state | 转到条约条款中输入的州 | treaty_article, treaty_article_options | state |
| input_strategic_region | 转到条约条款中输入的战略区域 | treaty_article, treaty_article_options | strategic_region |
| institution | 通过名称转到国家的机构（institution:institution_health_system） | country | institution |
| interest_group | 转到人物所属的利益集团！ | character | interest_group |
| interest_group_type | 转到当前 scope 人物所属利益集团的类型 | character | interest_group_type |
| invasion | 返回当前 scope 前线的入侵（如果存在） | front | invasion |
| invasion_attacker | 若在入侵 scope 中使用，转到执行入侵的国家。 | invasion | country |
| invasion_defender | 若在入侵 scope 中使用，转到被攻击州的控制国。 | invasion | country |
| investment | 转到机构当前的投资等级（示例：investment < investment_max） | institution | value |
| investment_max | 转到国家在机构中的当前最大投资等级（示例：investment < investment_max） | institution | value |
| investment_pool_income | 获取当前 scope 国家当前的每周投资池收入 | country | value |
| is_setup | 若游戏状态正在初始化则转到 true/false！ | none | boolean |
| je | 转到属于该国家的指定键的日志条目，示例：je:je_antarctica | country | journal_entry |
| je_tutorial | 转到当前激活的教程课程的日志条目（不要在教程之外使用） | none | journal_entry |
| land_controller_hq | 返回省份或州的控制者的所属陆军总部 | province, state | hq |
| land_hq | 返回省份或州所有者的本地陆军总部 | province, state | hq |
| largest_exporting_market | 转到当前 scope 市场商品对本地市场而言最大的出口市场 | market_goods | market |
| largest_importing_market | 转到当前 scope 市场商品从本地市场而言最大的进口市场 | market_goods | market |
| law_type | 通过名称转到某一法律类型（law_type:law_protected_speech），或从当前 scope 的法律转到其类型 | law, none | law_type |
| leader | 转到利益集团的领袖 | interest_group | character |
| legitimacy | 转到国家当前的合法性数值 | country | value |
| level | 转到建筑的等级 | building | value |
| level_after_queued_constructions | 转到建筑在所有排队建造完成后的等级 | building | value |
| lobby_foreign_anti_clout | 转到针对特定国家的所有反该国游说团的总政治力量（lobby_foreign_anti_clout:root >= 0.2） | country | value |
| lobby_foreign_pro_clout | 转到针对特定国家的所有亲该国游说团的总政治力量（lobby_foreign_pro_clout:root >= 0.2） | country | value |
| lobby_in_government_foreign_anti_clout | 转到针对特定国家的所有执政的反该国外交政策游说团的总政治力量（lobby_in_government_foreign_anti_clout:root >= 0.2） | country | value |
| lobby_in_government_foreign_pro_clout | 转到针对特定国家的所有执政的亲该国外交政策游说团的总政治力量（lobby_in_government_foreign_pro_clout:root >= 0.2） | country | value |
| lobby_join_weight | 转到利益集团加入某一游说团的加入权重（lobby_join_weight:root >= 5） | interest_group | value |
| lobby_type | 从名称指向某一政治游说类型（lobby_type:lobby_pro_country） | none | political_lobby_type |
| lobby_war_opposition | 指向所有反对该 scope 战争的游说集团的政治力量总和（lobby_war_opposition:root >= 0.2） | country | value |
| lobby_war_support | 指向所有支持该 scope 战争的游说集团的政治力量总和（lobby_war_support:root >= 0.2） | country | value |
| local_var | 通过名称引用先前设置的局部变量，例如：local_var:person_of_interest | none | varies |
| manpower | 返回单位的兵员 | new_combat_unit | value |
| market | 指向该对象所属的市场 | building, country, market, market_goods, province, state, state_goods, state_region | market |
| market_capital | 指向一个国家的市场首府 | country | state |
| market_export_cap | 基于 scope MarketGoods 的产量获取该市场可出口的最大商品数量 | market_goods | value |
| market_import_cap | 基于 scope MarketGoods 的消费量获取该市场可进口的最大商品数量 | market_goods | value |
| mass_migration_culture | 指向一个州的大规模迁移目标文化 | state | culture |
| mg | 从市场指向具有指定键的 MarketGoods（示例：mg:tools） | market | market_goods |
| migration_pull | 获取一个州的迁移拉力或一个国家的大规模迁移拉力。 | country, state | value |
| military_expenses | 获取该 scope 国家当前的军事开支（奴隶、工资和商品） | country | value |
| military_expenses_share | 获取该 scope 国家当前军事开支（奴隶、工资和商品）相对总开支的份额 | country | value |
| mobilization | 返回单位介于 0 到 1 之间的动员值 | new_combat_unit | value |
| mobilization_option | 从名称指向某一动员选项（mobilization_option:key） | none | mobilization_option |
| modifier | 指向属于当前对象的指定键的 modifier 类型数值，示例：modifier:country_influence_add | battle_side, building, character, country, interest_group, market, power_bloc, state | boolean, value |
| momentum | 获取该 scope 政党的原始势头 | party | value |
| morale | 返回单位的士气 | new_combat_unit | value |
| most_desired_law | 指向政治运动最希望颁布的法律类型（如果存在）。 | political_movement | law_type |
| movement_type | 从名称指向某一政治运动类型（movement_type:movement_religious_majority） | none | political_movement_type |
| mutual_trade_value_with_country | 指向两个市场之间贸易路线上交易商品的总基础价值（示例：mutual_trade_value_with_country:root >= 1000） | country | value |
| named_script_value | 在其使用的上下文中计算并返回数值的 script value | none | color, value |
| national_awakening_state_region | 从文化 scope 指向该文化正在发生民族觉醒的州区域 | culture | state_region |
| naval_combat_power | 指向该国家的海军战斗力（示例：naval_combat_power > 100） | country | value |
| naval_controller_hq | 返回省份或州控制者的海军总部 | province | hq |
| naval_hostility_average_damage_dealt | 指向该国家在其发起的海上敌对行动中于回溯期内造成的平均伤害。若未发现敌对行动则返回 -1。 | country | value |
| naval_hostility_damage | 指向该国家在当前海上敌对行动中对另一国家造成的伤害点数（示例：naval_hostility_damage:root >= 50） | country | value |
| naval_hq | 返回省份或州所有者的本地海军总部 | province | hq |
| naval_vulnerability | 指向一个国家基于贸易依赖度和沿海 GDP 份额的海军脆弱度评分，上限为某个 define 最大值 | country | value |
| navy_size | 该 scope 国家的分舰队数量。 | country | value |
| nf | 指向应用于该州的指定键的法令，示例：nf:decree_road_maintaintenance | state | decree |
| no | 假值的布尔字面量 | none | boolean |
| num_active_interests | 指向一个国家当前活跃利益的数量 num_active_interests > 5 | country | value |
| num_active_natural_interests | 指向一个国家当前活跃天然利益的数量 num_active_natural_interests > 5 | country | value |
| num_active_plays | 获取该 scope 国家当前发起的活跃外交博弈数量 | country | value |
| num_active_ships | 获取一个国家、指挥官或军事编队的活跃船只数量，或获取该省份内与指定国家结盟的军事编队的活跃船只数量 | character, country, military_formation, province | value |
| num_active_ships_in_battle | 获取一个国家、指挥官或军事编队战斗中的活跃船只数量，或获取该省份内与指定国家结盟的军事编队战斗中的活跃船只数量 | character, country, military_formation, province | value |
| num_active_ships_not_in_battle | 获取一个国家、指挥官或军事编队非战斗中的活跃船只数量，或获取该省份内与指定国家结盟的军事编队非战斗中的活跃船只数量 | character, country, military_formation, province | value |
| num_admirals | 指向该国家的海军上将数量 | country | value |
| num_alliances | 获取该 scope 国家的同盟总数（示例：num_alliances:root >= 2） | country | value |
| num_alliances_and_defensive_pacts_with_allies | 指向目标国家与该 scope 国家盟友之间的同盟数量（示例：num_alliances_and_defensive_pacts_with_allies:root >= 2） | country | value |
| num_alliances_and_defensive_pacts_with_rivals | 指向目标国家与该 scope 国家竞争对手之间的同盟与防御条约数量（示例：num_alliances_and_defensive_pacts_with_rivals:root >= 2） | country | value |
| num_battalions | 返回一名指挥官麾下活跃营的数量 | character | value |
| num_characters | 指向该国家的人物数量 | country | value |
| num_colony_projects | 获取该 scope 国家当前未完成/进行中的殖民地项目数量 | country | value |
| num_commanderless_units | 军事编队中因指挥官指挥上限而当前没有指挥官的单位数量。注：被击败的指挥官不指挥单位，即被击败的指挥官越多，无指挥官的单位越多。 | military_formation | value |
| num_commanders | 指向该国家的指挥官数量 | country | value |
| num_defending_battalions | 返回前线上与该国同一方参战单位的总数，示例：num_defending_battalions(root) | front | value |
| num_defensive_pacts | 指向目标国家拥有的防御条约总数（示例：num_defensive_pacts >= 2） | country | value |
| num_garrison_units | 返回驻扎在一个总部的单位数量 | hq | value |
| num_generals | 指向该国家的将军数量 | country | value |
| num_income_transfer_pacts | 指向目标国家拥有的（向他国）转移收入的条约总数（示例：num_income_transfer_pacts >= 2） | country | value |
| num_income_transfer_treaty_articles | 指向目标国家拥有的（向他国）转移收入的条约条款总数（示例：num_income_transfer_treaty_articles >= 2） | country | value |
| num_income_transfers | 指向目标国家拥有的（向他国）转移收入的条约及条约条款总数（示例：num_income_transfers >= 2） | country | value |
| num_incorporated_states | 获取该 scope 国家当前的已整合州数量 | country | value |
| num_interests | 指向一个国家拥有的利益数量（包括未激活的）num_interests > 5 | country | value |
| num_mandates | 指向该 scope 强权集团可用指令的数量（power_bloc.num_mandates > 0） | power_bloc | value |
| num_mobilized_battalions | 返回一名将军麾下已完全动员的单位数量 | character | value |
| num_natural_interests | 指向一个国家拥有的天然利益数量（包括未激活的）num_natural_interests > 5 | country | value |
| num_non_destroyed_ships | 获取一个国家、指挥官或军事编队未被击毁的船只数量，或获取该省份内与指定国家结盟的军事编队未被击毁的船只数量 | character, country, military_formation, province | value |
| num_non_destroyed_ships_in_battle | 获取一个国家、指挥官或军事编队战斗中未被击毁的船只数量，或获取该省份内与指定国家结盟的军事编队战斗中未被击毁的船只数量 | character, country, military_formation, province | value |
| num_non_destroyed_ships_not_in_battle | 获取一个国家、指挥官或军事编队非战斗中未被击毁的船只数量，或获取该省份内与指定国家结盟的军事编队非战斗中未被击毁的船只数量 | character, country, military_formation, province | value |
| num_obligations_earned | 从国家指向他国欠其（即其已挣得）的义务数量 | country | value |
| num_pending_events | 指向该 scope 国家中待处理事件的数量，可为总体或为指定类别 num_pending_events > 0 num_pending_events:enactment > 0 | country | value |
| num_politicians | 指向该国家的政治家数量 | country | value |
| num_positive_relations | 获取当前与该 scope 国家关系为正的国家数量 | country | value |
| num_provinces | 获取该 scope 实体当前的省份数量 | front, state, state_region | value |
| num_queued_constructions | 指向目标国家排队中建造项目的总数（示例：num_queued_constructions >= 2） | country | value |
| num_queued_government_constructions | 指向目标国家排队中政府建造项目的总数（示例：num_queued_government_constructions >= 2） | country | value |
| num_queued_private_constructions | 指向目标国家排队中私人建造项目的总数（示例：num_queued_private_constructions >= 2） | country | value |
| num_rivals | 指向目标国家拥有的竞争对手总数（示例：num_rivals >= 2） | country | value |
| num_ruling_igs | 获取该 scope 国家当前执政利益集团的数量 | country | value |
| num_shared_rivals | 指向该 scope 国家与目标国家共同竞争对手的数量（示例：num_shared_rivals:root >= 2） | country | value |
| num_ships | 获取一个国家、指挥官或军事编队的船只数量，或获取该省份内与指定国家结盟的军事编队的船只数量 | character, country, military_formation, province | value |
| num_ships_in_battle | 获取一个国家、指挥官或军事编队战斗中的船只数量，或获取该省份内与指定国家结盟的军事编队战斗中的船只数量 | character, country, military_formation, province | value |
| num_ships_not_in_battle | 获取一个国家、指挥官或军事编队非战斗中的船只数量，或获取该省份内与指定国家结盟的军事编队非战斗中的船只数量 | character, country, military_formation, province | value |
| num_ships_of_group | 该 scope 国家或军事编队中指定船只群的船只数量 | country, military_formation | value |
| num_states | 获取该 scope 国家当前的州数量 | country | value |
| num_total_battalions | 返回前线上与该国同一方单位的总数，示例：num_total_battalions(root) | front | value |
| num_unincorporated_states | 获取该 scope 国家当前的未整合州数量 | country | value |
| num_units | 获取一名指挥官或军事编队的活跃单位数量，或获取该省份内与指定国家结盟的军事编队的活跃单位数量 | character, military_formation, province | value |
| num_units_in_battle | 获取一名指挥官或军事编队战斗中的活跃单位数量，或获取该省份内与指定国家结盟的军事编队战斗中的活跃单位数量 | character, military_formation, province | value |
| num_units_not_in_battle | 获取一名指挥官或军事编队非战斗中的活跃单位数量，或获取该省份内与指定国家结盟的军事编队非战斗中的活跃单位数量 | character, military_formation, province | value |
| num_units_share | 一名指挥官考虑其指挥上限后所获单位的份额。示例：若该人物拥有 30 指挥上限，舰队共有 60 总指挥上限，编队共有 50 艘分舰队，则该人物应为其战斗获得 25 艘分舰队） | character | value |
| num_world_market_hub_trade_center_levels | 获取该 scope 世界市场枢纽州关联的贸易中心等级总数 | state | value |
| offense | 返回单位的进攻评分（包括其指挥官带来的影响） | new_combat_unit | value |
| opposing_commander | 从战斗中的人物指向战斗另一方的人物 | character | character |
| opposite_battle_side | 从战斗一方指向其对立方 | battle_side | battle_side |
| overlord | 指向该 scope 国家的直接宗主国 | country | country |
| owner | 指向该对象的所有者国家 | building, character, company, country, decree, institution, interest_group, interest_marker, journal_entry, law, market, market_goods, military_formation, new_combat_unit, political_movement, pop, province, state | country |
| owning_company | 指向拥有该 scope 国家的公司 | country | company |
| p | 指向由十六进制键指定的省份，示例：p:x1A6E5B | none | province |
| parent_law_type | 从修正案 scope 指向被视为该修正案母法的法律类型 | amendment | law_type |
| participants | 获取该 scope 市场的参与国总数 | market | value |
| party | 指向某一利益集团支持的政党 | interest_group | party |
| pirated_trade_value_by | 指向目标国家每周从该国劫掠商品的平均基础价值（示例：pirated_trade_value_by:root >= 50） | country | value |
| play_type | 从名称指向某一外交博弈类型（play_type:dp_default_treaty_article） | none | diplomatic_play_type |
| player | 指向玩家（请勿在教程之外使用） | none | country |
| player_owed_obligation_days_left | 指向外交关系 scope 中一项义务的剩余天数（示例：obligation_days_left >= 2） | diplomatic_relations | value |
| political_movement | 若在人物 scope 中使用，指向该人物支持的政治运动。若在革命内战 scope 中使用，指向发动革命的运动。若在利益集团 scope 中使用，指向该集团的主导运动。 | character, civil_war | political_movement |
| pop_type | 从名称指向某一人口类型（pop_type:laborers） | none | pop_type |
| pop_weight_modifier_scale | 获取该人口的权重修正比例乘数 | pop | value |
| popularity | 获取该 scope 人物的人气，通常介于 -100 到 +100 之间 | character | value |
| population_below_expected_sol | 指向该州当前低于其预期生活水平的人口百分比（0-1） | state | value |
| power_bloc | 指向该 scope 国家的强权集团 | country | power_bloc |
| power_bloc_leader | 指向该 scope 强权集团的领导国 | power_bloc | country |
| power_projection | 获取该 scope 编队、单位或船只的力量投射值 | military_formation, new_combat_unit, ship | value |
| power_struggle_contender | 若存在权力斗争，指向竞争国 | power_bloc | country |
| prev | 上一个 scope | none | varies |
| principal | 获取该国家当前的债务本金 | country | value |
| principle | 从名称指向强权集团原则（principle:key） | none | power_bloc_principle |
| principle_group | 从名称指向强权集团原则组（principle_group:key） | none | power_bloc_principle_group |
| prosperity | 指向该 scope 公司的繁荣度（示例：prosperity >= 2） | company | value |
| province | 从战斗一方指向战斗发生所在的省份 | battle_side | province |
| py | 指向该国指定键的活跃政党，示例：py:communist_party | country | party |
| rank_value | 指向特定国家等级的等级值（rank_value:great_power） | none | value |
| region | 指向该对象所属的战略区域！ | building, diplomatic_play, hq, interest_marker, province, state, state_region | strategic_region |
| region_state | 指向目标国家拥有的州（示例：region_state:BIC） | state_region | state |
| rel | 指向具有指定键的宗教，示例：rel:catholic | none | religion |
| relations | 指向两个国家之间的关系（示例：relations:root >= 2） | country | value |
| relations_change_rate | 指向两个国家之间关系进度的每日变化（示例：relations_change_rate:root > 0） | country | value |
| relations_threshold | 指向用于比较的关系阈值等级（relations_threshold:warm） | none | value |
| religion | 指向国家或国家定义的主要宗教，或人口的宗教 | character, country, country_definition, political_movement, pop | religion |
| remaining_binding_period | 获取该 scope 条约当前剩余的约束期天数 | treaty, treaty_options | value |
| required_construction | 获取该 scope 建筑类型所需的建造量 | building_type | value |
| root | 当前顶层 scope 的头部，例如：事件的接收者、决议的执行者 | none | varies |
| ruler | 指向一个国家的统治者 | country | character |
| s | 指向由键指定的州区域，示例：s:STATE_UTAH | none | state_region |
| scope | 通过名称引用先前保存的 scope，例如：scope:target | none | varies |
| scope_relations | 指向外交关系 scope 中的关系值（示例：scope_relations >= 2） | diplomatic_relations | value |
| scope_tension | 指向外交关系 scope 中的紧张度值（示例：scope_tension >= 2） | diplomatic_relations | value |
| screening | 从舰队 scope 指向该舰队中船只的总屏卫值 | military_formation | value |
| second_country | 指向以下任意对象的 second_country：外交条约、条约选项、条约条款的条约、条约条款选项（仅限双向条款类型） | diplomatic_pact, treaty, treaty_article, treaty_article_options, treaty_options | country |
| sg | 从州指向具有指定键的 StateGoods，示例：sg:wood | state | state_goods |
| ship_fleet | 从船只 scope 指向其所属舰队 | ship | military_formation |
| ship_group | 从船只指向其所属群组，或从名称指向某一船只群组（ship_group:ship_group_capital_ships） | none, ship | ship_group |
| ship_type | 从名称指向某一船只类型（ship_type:ship_type_frigate） | none | ship_type |
| shipping_lane | 指向该军事编队或条约条款（商品转移）的运输航线 | military_formation, treaty_article | shipping_lanes |
| slaves_role | 从建筑类型指向其奴隶角色人口类型 | building_type | pop_type |
| source_country | 指向以下任意对象的 source_country：条约条款（仅限定向条款类型）、条约条款选项（仅限定向条款类型） | treaty_article, treaty_article_options | country |
| sponsor | 从修正案 scope 指向赞助该修正案的利益集团 | amendment | interest_group |
| sr | 指向指定键的战略区域，示例：sr:region_persia | none | strategic_region |
| state | 指向该对象所在的州 | building, market, pop, province | state |
| state_region | 指向一个州所在的州区域 | state | state_region |
| strait_trade_importance_by | 指向该国经由目标国家控制的海峡进行贸易的商品贸易重要度。若控制者控制海峡两侧，累计值将乘以 STRAIT_FULL_CONTROL_TRADE_IMPORTANCE_MULT（示例：strait_trade_importance_by:root >= 100） | country | value |
| strait_type | 从名称指向某一海峡类型（strait_type:key） | none | strait_type |
| target | 指向该对象的目标 | diplomatic_catalyst, diplomatic_play, journal_entry, political_lobby | varies |
| target_country | 指向以下任意对象的 target_country：条约条款（仅限定向条款类型）、条约条款选项（仅限定向条款类型） | treaty_article, treaty_article_options | country |
| technology_being_researched | 指向一个国家当前正在研究的技术 | country | technology |
| techs_researched | 指向一个国家当前已研究的技术数量 | country | value |
| tension | 指向两个国家之间的紧张度（示例：tension:root >= 2） | country | value |
| tension_threshold | 指向用于比较的紧张度等级阈值（tension_threshold:warm） | none | value |
| theater | 从战斗一方或州指向其战区 | battle_side, state | theater |
| this | 当前 scope | none | varies |
| top_overlord | 指向该 scope 国家的最顶层宗主国 | country | country |
| total_crew_needed | 获取一个国家所有船只所需的船员总数 | country | value |
| total_export_value | 指向该 scope 国家向世界市场出口的总价值（示例：total_export_value >= 1000） | country | value |
| total_import_value | 指向该 scope 国家从世界市场进口的总价值（示例：total_import_value >= 1000） | country | value |
| total_marine_capacity | 获取一个国家所有舰队的总海军陆战队运力 | country | value |
| total_pirated_trade_value | 指向外交关系 scope 中两国之间通过海盗行为劫掠商品的总平均每周基础价值（示例：total_pirated_trade_value >= 100） | diplomatic_relations | value |
| total_trade_value | 指向该 scope 国家与世界市场贸易的总价值（示例：total_trade_value >= 1000） | country | value |
| trade_center | 指向该市场的贸易中心州！ | market | state |
| training_rate | 指向一个建筑当前的每周最大训练速率 | building | value |
| treaty | 指向某条约条款所属的条约 | treaty_article | treaty |
| treaty_exports | 获取该商品向该 scope MarketGoods 市场的当前条约（非世界市场）出口数量 | market_goods | value |
| treaty_imports | 获取该商品向该 scope MarketGoods 市场的当前条约（非世界市场）进口数量 | market_goods | value |
| type | 从对象指向其类型 | amendment, building, company, diplomatic_catalyst, diplomatic_play, harvest_condition_area, institution, interest_group, law, political_lobby, political_movement, ship, strait | amendment_type, building_type, company_type, diplomatic_play_type, harvest_condition_type, institution_type, interest_group_type, law_type, political_movement_type, ship_type, strait_type |
| unit_type | 从名称（unit_type:key）scope 到一个作战单位类型 | 无 | combat_unit_type |
| value | 数值字面量，例如：1、5.2、-6 | 无 | value |
| var | 通过名称引用此前在 scope 中设置的变量，例如：var:mortal_enemy | 不定 | 不定 |
| visibility | 从舰队 scope 链接到舰队中舰船的总可见度 | military_formation | value |
| vulnerability | 从舰队 scope 链接到舰队中舰船的总脆弱度 | military_formation | value |
| war | 从外交博弈 scope 到其战争 | diplomatic_play | war |
| weekly_prosperity_change | scope 到当前 scope 公司的每周繁荣度变化（示例：weekly_prosperity_change >= 2） | company | value |
| workplace | scope 到一个人口的工作场所 | pop | building |
| world_market_hub | scope 到与当前 scope 州相关联的世界市场中心州 | state | state |
| yes | 表示真值的布尔字面量 | 无 | boolean |

## 参考

---

- 要更新这些表格，请参见 [Module:Script docs/Event targets](https://vic3.paradoxwikis.com/Module:Script_docs/Event_targets)

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • Event targets • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本化内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本化类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| 地图 | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • [States](State modding.md) |
|---|---|

| 界面 | [Interface](Interface modding.md) • [GUI script](GUI script.md) • [Localization](Localization.md) • [Customizable localization](Localization.md) • [Script localization](Script localization.md) |
|---|---|

| 图形 | [3D Models](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|

| 音频 | Music • [Sound](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|