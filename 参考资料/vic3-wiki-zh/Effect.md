---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Effect
source: https://vic3.paradoxwikis.com/Effect
pageid: 3445
categories: [1.13, Modding]
fetched: 2026-10-27
---
本文已针对游戏当前[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

另见：
Event target
，
Trigger
**Effect**（游戏内效果脚本）会改变当前游戏状态——例如创建或移除人物、更改某个州的所有权等等。

effect 分为两种基本类型：内联（inline）与代码块（block）。内联 effect 接受一个简单的目标，例如 scope、script value 或已定义的类型。代码块 effect 更为复杂，通常接受多个目标，例如一个 scope 和一个 script value。

所有 effect 都要求特定的 [scope](Scope.md)。某些 effect 可在任何 scope 中使用（下表中标注为"none"），另一些则只有在正确的 scope 中才会生效。部分 effect 会改变当前 scope。

下表由脚本文档生成（*script_docs* console command）。

## 迭代器 effect

迭代器会检查所有相关的 scope 并输出一个或多个。

| Effect | 描述 | 示例 | Scope | 目标 |
|---|---|---|---|---|
| every_active_law | 遍历一国当前生效的所有法律 | every_active_law = { limit = { <triggers> } #optional <effects> } | country | law |
| every_active_party | 遍历一国当前所有活跃的政党 | every_active_party = { limit = { <triggers> } #optional <effects> } | country | party |
| every_character | 遍历全局所有人物 | every_character = { limit = { <triggers> } #optional <effects> } | none | character |
| every_character_in_exile_pool | 遍历流放池中的人物 | every_character_in_exile_pool = { limit = { <triggers> } #optional <effects> } | none | character |
| every_character_in_void | 遍历虚空（void）中的人物 | every_character_in_void = { limit = { <triggers> } #optional <effects> } | none | character |
| every_character_role | 遍历 scope 人物的所有角色 | every_character_role = { limit = { <triggers> } #optional <effects> } | character | character_role |
| every_civil_war | 遍历与 scope 国家相关的所有内战 | every_civil_war = { limit = { <triggers> } #optional <effects> } | country | civil_war |
| every_cobelligerent_in_diplo_play | 遍历 scope 国家在所有外交博弈（包括战争）中的所有共同交战国 | every_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional <effects> } | country | country |
| every_cobelligerent_in_war | 遍历 scope 国家在所有战争中的所有共同交战国 | every_cobelligerent_in_war = { limit = { <triggers> } #optional <effects> } | country | country |
| every_combat_unit | 遍历输入 scope 的所有作战单位 | every_combat_unit = { limit = { <triggers> } #optional <effects> } | battle, building, front, hq, military_formation | new_combat_unit |
| every_company | 遍历一国所有公司 | every_company = { limit = { <triggers> } #optional <effects> } | country | company |
| every_country | 遍历全局所有国家 | every_country = { limit = { <triggers> } #optional <effects> } | none | country |
| every_country_in_<georegion_short_name> | 遍历指定地理区域内的所有国家 | every_country_in_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | country |
| every_country_strategic_region | 遍历所有包含 scope 国家所拥有州的战略区域 | every_country_strategic_region = { limit = { <triggers> } #optional <effects> } | country | strategic_region |
| every_decentralized_country | 遍历所有松散（非中央集权）国家 | every_decentralized_country = { limit = { <triggers> } #optional <effects> } | none | country |
| every_diplomatic_catalyst | 遍历一国近期记忆中的所有外交催化剂 | every_diplomatic_catalyst = { limit = { <triggers> } #optional <effects> } | country | diplomatic_catalyst |
| every_diplomatic_play | 遍历全局所有外交博弈 | every_diplomatic_play = { limit = { <triggers> } #optional <effects> } | none | diplomatic_play |
| every_diplomatically_relevant_country | 遍历国家 scope 在外交上相关的所有国家 | every_diplomatically_relevant_country = { limit = { <triggers> } #optional <effects> } | country | country |
| every_direct_subject | 层级中直接位于当前国家之下的任意国家 | every_direct_subject = { limit = { <triggers> } #optional <effects> } | country | country |
| every_enemy_in_diplo_play | 遍历 scope 国家在所有外交博弈（包括战争）中的所有敌国 | every_enemy_in_diplo_play = { limit = { <triggers> } #optional <effects> } | country | country |
| every_enemy_in_war | 遍历 scope 国家在所有战争中的所有敌国 | every_enemy_in_war = { limit = { <triggers> } #optional <effects> } | country | country |
| every_harvest_condition | 遍历影响某个州、州区域、战略区域或国家的所有收成状况 | every_harvest_condition = { limit = { <triggers> } #optional <effects> } | country, state, state_region, strategic_region | harvest_condition |
| every_in_global_list | 遍历全局列表中的所有条目。 | every_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| every_in_hierarchy | 当前层级中的任意国家，包括当前国家自身 | every_in_hierarchy = { limit = { <triggers> } #optional <effects> } | country | country |
| every_in_list | 遍历列表中的所有条目。 | every_in_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| every_in_local_list | 遍历局部列表中的所有条目。 | every_in_local_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| every_influenced_interest_group | 遍历受某场政治运动影响的所有利益集团 | every_influenced_interest_group = { limit = { <triggers> } #optional <effects> } | political_movement | interest_group |
| every_interest_group | 遍历一国所有利益集团 | every_interest_group = { limit = { <triggers> } #optional <effects> } | country | interest_group |
| every_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | every_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | every_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_variable_map | 遍历变量映射中的所有键。 | every_key_in_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_law | 遍历一国所有法律 | every_law = { limit = { <triggers> } #optional <effects> } | country | law |
| every_lobby_member | 遍历某个游说团（lobby）的所有利益集团成员 | every_lobby_member = { limit = { <triggers> } #optional <effects> } | political_lobby | interest_group |
| every_market | 遍历全局所有市场 | every_market = { limit = { <triggers> } #optional <effects> } | none | market |
| every_market_goods | 遍历某市场所有活跃的（市场）商品 | every_market_goods = { limit = { <triggers> } #optional <effects> } | market | market_goods |
| every_member | 遍历某个政党的所有利益集团成员 | every_member = { limit = { <triggers> } #optional <effects> } | party | interest_group |
| every_military_formation | 遍历输入 scope 当前存在的所有军事编队 | every_military_formation = { limit = { <triggers> } #optional <effects> } | country, front, hq | military_formation |
| every_neighbouring_state | 遍历与当前 scope 相邻的所有州 注意使用英式拼写 | every_neighbouring_state = { limit = { <triggers> } #optional <effects> } | country, state, state_region, strategic_region | state |
| every_overlord_or_above | 层级中位于当前国家之上的任意国家 | every_overlord_or_above = { limit = { <triggers> } #optional <effects> } | country | country |
| every_owned_country | 遍历 scope 公司拥有的所有国家 | every_owned_country = { limit = { <triggers> } #optional <effects> } | company | country |
| every_participant | scope 中外交条约（pact）的两个参与方中的任意一个 | every_participant = { limit = { <triggers> } #optional <effects> } | diplomatic_pact | country |
| every_political_lobby | 遍历一国或某利益集团中的所有政治游说团 | every_political_lobby = { limit = { <triggers> } #optional <effects> } | country, interest_group | political_lobby |
| every_political_movement | 遍历一国所有政治运动 | every_political_movement = { limit = { <triggers> } #optional <effects> } | country | political_movement |
| every_possible_amendment_type | 遍历可添加到 scope 法律的修正案类型 | every_possible_amendment_type = { limit = { <triggers> } #optional <effects> } | law | amendment_type |
| every_potential_party | 遍历一国所有潜在的政党 | every_potential_party = { limit = { <triggers> } #optional <effects> } | country | party |
| every_power_bloc | 遍历所有强权集团 | every_power_bloc = { limit = { <triggers> } #optional <effects> } | none | power_bloc |
| every_power_bloc_member | 遍历 scope 强权集团的所有成员，包括领袖 | every_power_bloc_member = { limit = { <triggers> } #optional <effects> } | power_bloc | country |
| every_preferred_law | 遍历利益集团所在国家当前生效及可能的所有法律，按其对该法律的偏好程度排序 | every_preferred_law = { limit = { <triggers> } #optional <effects> } | interest_group | law |
| every_primary_culture | scope 国家或国家定义的主要文化 | every_primary_culture = { limit = { <triggers> } #optional <effects> } | country, country_definition | culture |
| every_province | 遍历 scope 州中的所有省份（Province） | every_province = { limit = { <triggers> } #optional <effects> } | province | state |
| every_province_in_<georegion_short_name> | 遍历指定地理区域内的所有省份 | every_province_in_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | province |
| every_rival_country | 被 scope 国家视为竞争对手的任意国家 | every_rival_country = { limit = { <triggers> } #optional <effects> } | country | country |
| every_rivaling_country | 将 scope 国家视为竞争对手的任意国家 | every_rivaling_country = { limit = { <triggers> } #optional <effects> } | country | country |
| every_scope_admiral | 遍历以下范围中的所有海军上将：国家、利益集团或军事编队 | every_scope_admiral = { limit = { <triggers> } #optional <effects> } | country, front, interest_group, military_formation | character |
| every_scope_ally | 遍历一个国家的所有盟友 | every_scope_ally = { limit = { <triggers> } #optional <effects> } | country | country |
| every_scope_amendment | 遍历 scope 法律的修正案 | every_scope_amendment = { limit = { <triggers> } #optional <effects> } | law | amendment |
| every_scope_army | 遍历输入 scope 当前存在的所有陆军 | every_scope_army = { limit = { <triggers> } #optional <effects> } | country, front, hq | military_formation |
| every_scope_article | 遍历 scope 条约的条款 | every_scope_article = { limit = { <triggers> } #optional <effects> } | treaty | treaty_article |
| every_scope_article_option | 遍历 scope 条约或 treaty_options 的 article_options | every_scope_article_option = { limit = { <triggers> } #optional <effects> } | treaty, treaty_options | treaty_article_options |
| every_scope_building | 遍历以下范围中的所有建筑：州、国家 | every_scope_building = { limit = { <triggers> } #optional <effects> } | country, state | building |
| every_scope_character | 遍历以下范围中的所有人物：国家、利益集团或前线 | every_scope_character = { limit = { <triggers> } #optional <effects> } | country, front, interest_group, military_formation | character |
| every_scope_country | 遍历在受支持的 scope（当前为：market、state_region、strategic region）中有存在的所有国家 | every_scope_country = { limit = { <triggers> } #optional <effects> } | market, state_region, strategic_region | country |
| every_scope_culture | 遍历该 scope 中的所有文化 | every_scope_culture = { limit = { <triggers> } #optional <effects> } | country, state | culture |
| every_scope_diplomatic_pact | scope 国家的任意外交条约 | every_scope_diplomatic_pact = { limit = { <triggers> } #optional <effects> } | country | diplomatic_pact |
| every_scope_fleet | 遍历输入 scope 当前存在的所有舰队 | every_scope_fleet = { limit = { <triggers> } #optional <effects> } | country, hq | military_formation |
| every_scope_front | 遍历与 scope 战争相关的所有前线 | every_scope_front = { limit = { <triggers> } #optional <effects> } | war | front |
| every_scope_general | 遍历以下范围中的所有将军：国家、利益集团、前线或军事编队 | every_scope_general = { limit = { <triggers> } #optional <effects> } | country, front, interest_group, military_formation | character |
| every_scope_held_interest_marker | 遍历一国持有的所有利益标记 | every_scope_held_interest_marker = { limit = { <triggers> } #optional <effects> } | country | interest_marker |
| every_scope_homeland_state | 遍历作为 scope 文化的家园的所有州，或 scope 国家任一主要文化的家园的所有州 | every_scope_homeland_state = { limit = { <triggers> } #optional <effects> } | country, culture | state |
| every_scope_initiator_ally | 遍历外交博弈中发起方的所有盟友 | every_scope_initiator_ally = { limit = { <triggers> } #optional <effects> } | diplomatic_play | country |
| every_scope_interest_marker | 遍历以下范围中的所有利益标记：国家、州区域、战略区域 | every_scope_interest_marker = { limit = { <triggers> } #optional <effects> } | country, state_region, strategic_region | interest_marker |
| every_scope_je_involved | 遍历某个日志条目的所有相关方 | every_scope_je_involved = { limit = { <triggers> } #optional <effects> } | journal_entry | country |
| every_scope_play_involved | 遍历外交博弈中的所有相关方 | every_scope_play_involved = { limit = { <triggers> } #optional <effects> } | diplomatic_play | country |
| every_scope_politician | 遍历以下范围中的所有政客：国家或利益集团 | every_scope_politician = { limit = { <triggers> } #optional <effects> } | country, front, interest_group, military_formation | character |
| every_scope_pop | 遍历以下范围中的所有人口：国家、州、利益集团、文化 | every_scope_pop = { limit = { <triggers> } #optional <effects> } | country, culture, interest_group, state | pop |
| every_scope_regional_hqs | 遍历 scope 公司的地区总部 | every_scope_regional_hqs = { limit = { <triggers> } #optional <effects> } | company | building |
| every_scope_ship | 遍历一国或军事编队中的所有船只 | every_scope_ship = { limit = { <triggers> } #optional <effects> } | country, military_formation | ship |
| every_scope_state | 遍历以下范围中包含省份在内的所有州：国家、州区域、战区、前线或海峡 | every_scope_state = { limit = { <triggers> } #optional <effects> } | country, front, state_region, strait, strategic_region, theater | state |
| every_scope_strait | 遍历在 scope 州或国家拥有陆地端点的所有海峡 | every_scope_strait = { limit = { <triggers> } #optional <effects> } | country, state | strait |
| every_scope_target_ally | 遍历外交博弈中目标的盟友 | every_scope_target_ally = { limit = { <triggers> } #optional <effects> } | diplomatic_play | country |
| every_scope_theater | 遍历一国中的所有战区 | every_scope_theater = { limit = { <triggers> } #optional <effects> } | country | theater |
| every_scope_treaty | 遍历对 scope 国家有约束力的所有生效条约 | every_scope_treaty = { limit = { <triggers> } #optional <effects> } | country | treaty |
| every_scope_violate_sovereignty_interested_parties | 遍历在 scope 国家主权被侵犯时会产生关注的所有国家 | every_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional <effects> } | country | country |
| every_scope_violate_sovereignty_wars | 遍历目标国家主权被 scope 国家侵犯时会引发的所有相关战争 | every_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional <effects> } | country | war |
| every_scope_war | 遍历与该 scope 相关的所有战争 | every_scope_war = { limit = { <triggers> } #optional <effects> } | country | war |
| every_sea_node_adjacent_state | 遍历与某个州共享海域节点的所有州 | every_sea_node_adjacent_state = { limit = { <triggers> } #optional <effects> } | state | state |
| every_state | 遍历全局所有州 | every_state = { limit = { <triggers> } #optional <effects> } | none | state |
| every_state_in_<georegion_short_name> | 遍历指定地理区域内的所有州 | every_state_in_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | state |
| every_state_region | 遍历所有州区域 | every_state_region = { limit = { <triggers> } #optional <effects> } | none | state_region |
| every_state_region_<georegion_short_name> | 遍历指定地理区域内的所有州区域 | every_state_region_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | state_region |
| every_strategic_objective | 遍历 scope 国家的所有战略目标州 | every_strategic_objective = { limit = { <triggers> } #optional <effects> } | country | state |
| every_strategic_region | 遍历全局所有战略区域 | every_strategic_region = { limit = { <triggers> } #optional <effects> } | none | strategic_region |
| every_strategic_region_in_<georegion_short_name> | 遍历指定地理区域内的所有战略区域 | every_strategic_region_in_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | strategic_region |
| every_subject_of_subject | 层级中位于直接附属国之下的任意国家 | every_subject_of_subject = { limit = { <triggers> } #optional <effects> } | country | country |
| every_subject_or_below | 层级中位于当前国家之下的任意国家 | every_subject_or_below = { limit = { <triggers> } #optional <effects> } | country | country |
| every_supporting_character | 遍历支持 scope 政治运动的所有人物 | every_supporting_character = { limit = { <triggers> } #optional <effects> } | political_movement | character |
| every_treaty | 遍历所有条约（包括生效条约与草案） | every_treaty = { limit = { <triggers> } #optional <effects> } | none | treaty |
| every_valid_mass_migration_culture | 列出 scope 国家中适合进行大规模迁移的文化 | every_valid_mass_migration_culture = { limit = { <triggers> } #optional <effects> } | country | culture |
| every_war_participant | 遍历一场战争中的所有参战方 | every_war_participant = { limit = { <triggers> } #optional <effects> } | war | country |
| ordered_active_law | 遍历一国当前生效的所有法律 | ordered_active_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | law |
| ordered_active_party | 遍历一国当前所有活跃的政党 | ordered_active_party = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | party |
| ordered_character | 遍历全局所有人物 | ordered_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | character |
| ordered_character_in_exile_pool | 遍历流放池中的人物 | ordered_character_in_exile_pool = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | character |
| ordered_character_in_void | 遍历虚空（void）中的人物 | ordered_character_in_void = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | character |
| ordered_character_role | 遍历 scope 人物的所有角色 | ordered_character_role = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character | character_role |
| ordered_civil_war | 遍历与 scope 国家相关的所有内战 | ordered_civil_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | civil_war |
| ordered_cobelligerent_in_diplo_play | 遍历 scope 国家在所有外交博弈（包括战争）中的所有共同交战国 | ordered_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_cobelligerent_in_war | 遍历 scope 国家在所有战争中的所有共同交战国 | ordered_cobelligerent_in_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_combat_unit | 遍历输入 scope 的所有作战单位 | ordered_combat_unit = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | battle, building, front, hq, military_formation | new_combat_unit |
| ordered_company | 遍历一个国家中的所有公司 | ordered_company = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | company |
| ordered_country | 遍历全球所有国家 | ordered_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | country |
| ordered_country_in_<georegion_short_name> | 遍历指定地理区域中的所有国家 | ordered_country_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | country |
| ordered_country_strategic_region | 遍历包含 scope 国家所拥有州的所有战略区域 | ordered_country_strategic_region = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | strategic_region |
| ordered_decentralized_country | 遍历所有未中央集权化的国家 | ordered_decentralized_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | country |
| ordered_diplomatic_catalyst | 遍历一个国家近期记忆中的所有外交催化剂 | ordered_diplomatic_catalyst = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | diplomatic_catalyst |
| ordered_diplomatic_play | 遍历全球所有外交博弈 | ordered_diplomatic_play = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | diplomatic_play |
| ordered_diplomatically_relevant_country | 遍历一个国家 scope 的所有外交相关国家 | ordered_diplomatically_relevant_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_direct_subject | 层级结构中直接位于当前国家之下的任何国家 | ordered_direct_subject = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_enemy_in_diplo_play | 遍历 scope 国家在所有外交博弈（包括战争）中的所有敌国 | ordered_enemy_in_diplo_play = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_enemy_in_war | 遍历 scope 国家在所有战争中的所有敌国 | ordered_enemy_in_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成状况 | ordered_harvest_condition = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state, state_region, strategic_region | harvest_condition |
| ordered_in_global_list | 遍历全局列表中的所有项目。list = 名称 或 variable = 名称 | ordered_in_global_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_in_hierarchy | 当前层级结构中的任何国家，包括当前国家 | ordered_in_hierarchy = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_in_list | 遍历列表中的所有项目。 | ordered_in_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_in_local_list | 遍历局部列表中的所有项目。list = 名称 或 variable = 名称 | ordered_in_local_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_influenced_interest_group | 遍历受一个政治运动影响的所有利益集团 | ordered_influenced_interest_group = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_movement | interest_group |
| ordered_interest_group | 遍历一个国家中的所有利益集团 | ordered_interest_group = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | interest_group |
| ordered_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | ordered_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | ordered_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_key_in_variable_map | 遍历变量映射中的所有键。 | ordered_key_in_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_law | 遍历一个国家中的所有法律 | ordered_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | law |
| ordered_lobby_member | 遍历一个政治游说团的所有利益集团成员 | ordered_lobby_member = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_lobby | interest_group |
| ordered_market | 遍历全球所有市场 | ordered_market = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | market |
| ordered_market_goods | 遍历一个市场中的所有活跃（市场）商品 | ordered_market_goods = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | market | market_goods |
| ordered_member | 遍历一个政党的所有利益集团成员 | ordered_member = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | party | interest_group |
| ordered_military_formation | 遍历当前存在于输入 scope 的所有军事编队 | ordered_military_formation = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, hq | military_formation |
| ordered_neighbouring_state | 遍历与一个州区域相邻的所有州 | ordered_neighbouring_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state, state_region, strategic_region | state |
| ordered_overlord_or_above | 层级结构中位于当前国家之上的任何国家 | ordered_overlord_or_above = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_owned_country | 遍历 scope 公司拥有的所有国家 | ordered_owned_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | company | country |
| ordered_participant | scope 中外交协定的两个参与方中的任何一个 | ordered_participant = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_pact | country |
| ordered_political_lobby | 遍历一个国家或利益集团中的所有政治游说团 | ordered_political_lobby = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, interest_group | political_lobby |
| ordered_political_movement | 遍历一个国家中的所有政治运动 | ordered_political_movement = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | political_movement |
| ordered_possible_amendment_type | 遍历可添加到 scope 法律的修正案类型 | ordered_possible_amendment_type = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | law | amendment_type |
| ordered_potential_party | 遍历一个国家中所有潜在的政党 | ordered_potential_party = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | party |
| ordered_power_bloc | 遍历所有强权集团 | ordered_power_bloc = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | power_bloc |
| ordered_power_bloc_member | 遍历该 scope 强权集团的所有成员，包括领导者 | ordered_power_bloc_member = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | power_bloc | country |
| ordered_preferred_law | 遍历利益集团所在国家的所有已生效及可能的法律，按其对该法律的偏好程度排序 | ordered_preferred_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | interest_group | law |
| ordered_primary_culture | 该 scope 国家或国家定义的主要文化 | ordered_primary_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, country_definition | culture |
| ordered_province | 遍历该 scope 州的所有省份（Province） | ordered_province = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state | province |
| ordered_province_in_<georegion_short_name> | 遍历指定地理区域的的所有省份 | ordered_province_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | province |
| ordered_rival_country | 任何被该 scope 国家视为竞争对手的国家 | ordered_rival_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_rivaling_country | 任何视该 scope 国家为竞争对手的国家 | ordered_rivaling_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_scope_admiral | 遍历以下 scope 中的所有海军上将：国家、利益集团或军事编队 | ordered_scope_admiral = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_ally | 遍历一个国家的所有盟友 | ordered_scope_ally = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_scope_amendment | 遍历该 scope 法律的修正案 | ordered_scope_amendment = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | law | amendment |
| ordered_scope_army | 遍历当前处于输入 scope 的所有陆军 | ordered_scope_army = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, hq | military_formation |
| ordered_scope_article | 遍历该 scope 条约的条款 | ordered_scope_article = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty | treaty_article |
| ordered_scope_article_option | 遍历该 scope 条约或条约选项（treaty_options）的条款选项 | ordered_scope_article_option = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty, treaty_options | treaty_article_options |
| ordered_scope_building | 遍历以下 scope 中的所有建筑：州、国家 | ordered_scope_building = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state | building |
| ordered_scope_character | 遍历以下 scope 中的所有人物：国家、利益集团或前线 | ordered_scope_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_country | 遍历在支持的 scope（目前为：市场、地区、战略区域）中存在的所有国家 | ordered_scope_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | market, state_region, strategic_region | country |
| ordered_scope_culture | 遍历该 scope 中的所有文化 | ordered_scope_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state | culture |
| ordered_scope_diplomatic_pact | 该 scope 国家的任何外交协定 | ordered_scope_diplomatic_pact = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | diplomatic_pact |
| ordered_scope_fleet | 遍历当前处于输入 scope 的所有舰队 | ordered_scope_fleet = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, hq | military_formation |
| ordered_scope_front | 遍历与该 scope 战争相关的所有前线 | ordered_scope_front = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | war | front |
| ordered_scope_general | 遍历以下 scope 中的所有将军：国家、利益集团、前线或军事编队 | ordered_scope_general = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_held_interest_marker | 遍历一个国家持有的所有利益标记 | ordered_scope_held_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | interest_marker |
| ordered_scope_homeland_state | 遍历作为该 scope 文化家园的所有州，或该 scope 国家任一主要文化家园的所有州 | ordered_scope_homeland_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, culture | state |
| ordered_scope_initiator_ally | 遍历外交博弈中发起方的所有盟友 | ordered_scope_initiator_ally = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_play | country |
| ordered_scope_interest_marker | 遍历以下 scope 中的所有利益标记：国家、地区、战略区域 | ordered_scope_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state_region, strategic_region | interest_marker |
| ordered_scope_je_involved | 遍历日志条目的所有参与方 | ordered_scope_je_involved = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | journal_entry | country |
| ordered_scope_play_involved | 遍历外交博弈的所有参与方 | ordered_scope_play_involved = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_play | country |
| ordered_scope_politician | 遍历以下 scope 中的所有政客：国家或利益集团 | ordered_scope_politician = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_pop | 遍历以下 scope 中的所有人口：国家、州、利益集团、文化 | ordered_scope_pop = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, culture, interest_group, state | pop |
| ordered_scope_regional_hqs | 遍历该 scope 公司的区域总部 | ordered_scope_regional_hqs = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | company | building |
| ordered_scope_ship | 遍历一个国家或军事编队中的所有舰船 | ordered_scope_ship = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, military_formation | ship |
| ordered_scope_state | 遍历以下 scope 中包含省份在内的所有州：国家、地区、战区、前线或海峡 | ordered_scope_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, state_region, strait, strategic_region, theater | state |
| ordered_scope_strait | 遍历在该 scope 州或国家拥有陆地端点的所有海峡 | ordered_scope_strait = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state | strait |
| ordered_scope_target_ally | 遍历外交博弈中目标的的所有盟友 | ordered_scope_target_ally = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_play | country |
| ordered_scope_theater | 遍历一个国家的所有战区 | ordered_scope_theater = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | theater |
| ordered_scope_treaty | 遍历对该 scope 国家有约束力的所有生效条约 | ordered_scope_treaty = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | treaty |
| ordered_scope_violate_sovereignty_interested_parties | 遍历所有会在该 scope 国家主权被侵犯时产生利害关系的国家 | ordered_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_scope_violate_sovereignty_wars | 遍历目标国家被 scope 所在国家侵犯主权的所有相关战争 | ordered_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | war |
| ordered_scope_war | 遍历与该 scope 相关的所有战争 | ordered_scope_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | war |
| ordered_sea_node_adjacent_state | 遍历与某个州共享海洋节点的所有州 | ordered_sea_node_adjacent_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state | state |
| ordered_state | 遍历全球所有州 | ordered_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state |
| ordered_state_in_<georegion_short_name> | 遍历指定地理区域内的所有州 | ordered_state_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state |
| ordered_state_region | 遍历所有州区域（state region） | ordered_state_region = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state_region |
| ordered_state_region_in_<georegion_short_name> | 遍历指定地理区域内的所有州区域 | ordered_state_region_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state_region |
| ordered_strategic_objective | 遍历该 scope 国家的所有战略目标州 | ordered_strategic_objective = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | state |
| ordered_strategic_region | 遍历全球所有战略区域 | ordered_strategic_region = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | strategic_region |
| ordered_strategic_region_in_<georegion_short_name> | 遍历指定地理区域内的所有战略区域 | ordered_state_region_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | strategic_region |
| ordered_subject_of_subject | 层级中直接附属国之下的任何国家 | ordered_subject_of_subject = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_subject_or_below | 层级中当前国家之下的任何国家 | ordered_subject_or_below = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_supporting_character | 遍历支持该 scope 政治运动的所有人物 | ordered_supporting_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_movement | character |
| ordered_treaty | 遍历所有条约（包括生效中的和草案） | ordered_treaty = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | treaty |
| ordered_valid_mass_migration_culture | 列出该 scope 国家中符合大规模迁移条件的文化 | ordered_valid_mass_migration_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | culture |
| ordered_war_participant | 遍历一场战争中的所有参战方 | ordered_war_participant = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | war | country |
| random_active_law | 遍历一个国家的所有现行法律 | random_active_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | law |
| random_active_party | 遍历一个国家的所有活跃政党 | random_active_party = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | party |
| random_character | 遍历全球所有人物 | random_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | character |
| random_character_in_exile_pool | 遍历流放者池中的人物 | random_character_in_exile_pool = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | character |
| random_character_in_void | 遍历虚空（void）中的人物 | random_character_in_void = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | character |
| random_character_role | 遍历该 scope 人物的所有角色 | random_character_role = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character | character_role |
| random_civil_war | 遍历与该 scope 国家相关的所有内战 | random_civil_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | civil_war |
| random_cobelligerent_in_diplo_play | 遍历 scope 国家在所有外交博弈（包括战争）中的所有共同交战国 | random_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_cobelligerent_in_war | 遍历 scope 国家在所有战争中的所有共同交战国 | random_cobelligerent_in_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_combat_unit | 遍历输入 scope 的所有作战单位 | random_combat_unit = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | battle, building, front, hq, military_formation | new_combat_unit |
| random_company | 遍历一个国家的所有公司 | random_company = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | company |
| random_country | 遍历全球所有国家 | random_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | country |
| random_country_in_<georegion_short_name> | 遍历指定地理区域内的所有国家 | random_country_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | country |
| random_country_strategic_region | 遍历包含该 scope 国家所拥有州的所有战略区域 | random_country_strategic_region = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | strategic_region |
| random_decentralized_country | 遍历所有松散国家（decentralized country） | random_decentralized_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | country |
| random_diplomatic_catalyst | 遍历一个国家近期记忆中的所有外交催化剂 | random_diplomatic_catalyst = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | diplomatic_catalyst |
| random_diplomatic_play | 遍历全球所有外交博弈 | random_diplomatic_play = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | diplomatic_play |
| random_diplomatically_relevant_country | 遍历一个国家 scope 的所有外交相关国家 | random_diplomatically_relevant_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_direct_subject | 层级中直接位于当前国家之下的任何国家 | random_direct_subject = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_enemy_in_diplo_play | 遍历 scope 国家在所有外交博弈（包括战争）中的所有敌国 | random_enemy_in_diplo_play = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_enemy_in_war | 遍历 scope 国家在所有战争中的所有敌国 | random_enemy_in_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成状况 | random_harvest_condition = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state, state_region, strategic_region | harvest_condition |
| random_in_global_list | 遍历全局列表中的所有项目。 | random_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| random_in_hierarchy | 当前层级中的任何国家，包括当前国家 | random_in_hierarchy = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_in_list | 遍历列表中的所有项目。 | random_in_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| random_in_local_list | 遍历本地列表中的所有项目。 | random_in_local_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| random_influenced_interest_group | 遍历受一个政治运动影响的所有利益集团 | random_influenced_interest_group = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_movement | interest_group |
| random_interest_group | 遍历一个国家中的所有利益集团 | random_interest_group = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | interest_group |
| random_key_in_global_variable_map | 遍历全局变量映射（variable map）中的所有键。 | random_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_local_variable_map | 遍历本地变量映射中的所有键。 | random_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_variable_map | 遍历变量映射中的所有键。 | random_key_in_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_law | 遍历一个国家中的所有法律 | random_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | law |
| random_lobby_member | 遍历一个政治游说团的所有利益集团成员 | random_lobby_member = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_lobby | interest_group |
| random_market | 遍历全球所有市场 | random_market = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | market |
| random_market_goods | 遍历一个市场中的所有活跃（市场）商品 | random_market_goods = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | market | market_goods |
| random_member | 遍历一个政党的所有利益集团成员 | random_member = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | party | interest_group |
| random_military_formation | 遍历输入 scope 当前存在的所有军事编队 | random_military_formation = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, hq | military_formation |
| random_neighbouring_state | 遍历与某个州区域相邻的所有州 | random_neighbouring_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state, state_region, strategic_region | state |
| random_overlord_or_above | 层级中当前国家之上的任何国家 | random_overlord_or_above = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_owned_country | 遍历该 scope 公司拥有的所有国家 | random_owned_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | company | country |
| random_participant | scope 中外交协定的两个参与方中的任意一方 | random_participant = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_pact | country |
| random_political_lobby | 遍历一个国家或利益集团中的所有政治游说团 | random_political_lobby = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, interest_group | political_lobby |
| random_political_movement | 遍历一个国家中的所有政治运动 | random_political_movement = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | political_movement |
| random_possible_amendment_type | 遍历可添加到该 scope 法律的修正案类型 | random_possible_amendment_type = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | law | amendment_type |
| random_potential_party | 遍历一个国家中所有潜在政党 | random_potential_party = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | party |
| random_power_bloc | 遍历所有强权集团 | random_power_bloc = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | power_bloc |
| random_power_bloc_member | 遍历该 scope 强权集团的所有成员，包括领袖 | random_power_bloc_member = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | power_bloc | country |
| random_preferred_law | 遍历利益集团所在国家中所有现行和可能的法律，按其对法律的偏好程度排序 | random_preferred_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | interest_group | law |
| random_primary_culture | 该 scope 国家或国家定义（country definition）的主流文化 | random_primary_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, country_definition | culture |
| random_province | 遍历该 scope 州中的所有省份 | random_province = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state | province |
| random_province_in_<georegion_short_name> | 遍历指定地理区域内的所有省份 | random_province_in_<georegion_short_name>' = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | province |
| random_rival_country | 被 scope 国家视为竞争对手的任何国家 | random_rival_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_rivaling_country | 将 scope 国家视为竞争对手的任何国家 | random_rivaling_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_scope_admiral | 遍历以下 scope 中的所有海军上将：国家、利益集团或军事编队 | random_scope_admiral = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_ally | 遍历一个国家的所有盟友 | random_scope_ally = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_scope_amendment | 遍历该 scope 法律的修正案 | random_scope_amendment = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | law | amendment |
| random_scope_army | 遍历输入 scope 当前存在的所有陆军 | random_scope_army = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, hq | military_formation |
| random_scope_article | 遍历该 scope 条约的条款 | random_scope_article = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty | treaty_article |
| random_scope_article_option | 遍历该 scope 条约或条约选项（treaty_options）的条款选项 | random_scope_article_option = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty, treaty_options | treaty_article_options |
| random_scope_building | 遍历以下 scope 中的所有建筑：州、国家 | random_scope_building = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state | building |
| random_scope_character | 遍历以下 scope 中的所有人物：国家、利益集团或前线 | random_scope_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_country | 遍历在支持的 scope（目前为：市场、州区域、战略区域）中有存在的所有国家 | random_scope_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | market, state_region, strategic_region | country |
| random_scope_culture | 遍历该 scope 中的所有文化 | random_scope_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state | culture |
| random_scope_diplomatic_pact | scope 中国家的任意外交条约 | random_scope_diplomatic_pact = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | diplomatic_pact |
| random_scope_fleet | 遍历当前存在于输入 scope 中的所有舰队 | random_scope_fleet = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, hq | military_formation |
| random_scope_front | 遍历与该 scope 的战争相关的所有前线 | random_scope_front = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | war | front |
| random_scope_general | 遍历以下 scope 中的所有将军：国家、利益集团、前线或军事编队 | random_scope_general = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_held_interest_marker | 遍历一个国家持有的所有利益标记 | random_scope_held_interest_marker = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | interest_marker |
| random_scope_homeland_state | 遍历所有作为该 scope 文化的本土的州，或该 scope 国家任一主要文化的本土的州 | random_scope_homeland_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, culture | state |
| random_scope_initiator_ally | 遍历外交博弈中发起方的所有盟友 | random_scope_initiator_ally = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_play | country |
| random_scope_interest_marker | 遍历以下 scope 中的所有利益标记：国家、州区域、战略区域 | random_scope_interest_marker = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state_region, strategic_region | interest_marker |
| random_scope_je_involved | 遍历日志条目的所有参与方 | random_scope_je_involved = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | journal_entry | country |
| random_scope_play_involved | 遍历外交博弈的所有参与方 | random_scope_play_involved = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_play | country |
| random_scope_politician | 遍历以下 scope 中的所有政治家：国家或利益集团 | random_scope_politician = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_pop | 遍历以下 scope 中的所有人口：国家、州、利益集团、文化 | random_scope_pop = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, culture, interest_group, state | pop |
| random_scope_regional_hqs | 遍历该 scope 公司的地区总部 | random_scope_regional_hqs = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | company | building |
| random_scope_ship | 遍历国家或军事编队中的所有舰船 | random_scope_ship = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, military_formation | ship |
| random_scope_state | 遍历包含以下 scope 省份的所有州：国家、州区域、战区、前线或海峡 | random_scope_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, state_region, strait, strategic_region, theater | state |
| random_scope_strait | 遍历在所 scope 的州或国家中拥有陆上端点的所有海峡 | random_scope_strait = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state | strait |
| random_scope_target_ally | 遍历外交博弈中目标的所在盟友 | random_scope_target_ally = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_play | country |
| random_scope_theater | 遍历一个国家中的所有战区 | random_scope_theater = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | theater |
| random_scope_treaty | 遍历约束该 scope 国家的所有生效条约 | random_scope_treaty = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | treaty |
| random_scope_violate_sovereignty_interested_parties | 遍历在 scope 中国家的主权被侵犯时会表示关切的所在国家 | random_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_scope_violate_sovereignty_wars | 遍历如果目标国家的主权被该 scope 国家侵犯会产生的所有相关战争 | random_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | war |
| random_scope_war | 遍历与该 scope 相关的所有战争 | random_scope_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | war |
| random_sea_node_adjacent_state | 遍历与某个州共享海上节点的所有州 | random_sea_node_adjacent_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state | state |
| random_state | 遍历全球所有州 | random_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state |
| random_state_in_<georegion_short_name> | 遍历指定地理区域中的所有州 | random_state_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state |
| random_state_region | 遍历所有州区域 | random_state_region = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state_region |
| random_state_region_in_<georegion_short_name> | 遍历指定地理区域中的所有州区域 | random_state_region_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state_region |
| random_strategic_objective | 遍历该 scope 国家的所有战略目标州 | random_strategic_objective = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | state |
| random_strategic_region | 遍历全球所有战略区域 | random_strategic_region = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | strategic_region |
| random_strategic_region_in_<georegion_short_name> | 遍历指定地理区域中的所有战略区域 | random_strategic_region_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | strategic_region |
| random_subject_or_below | 层级中位于当前国家之下的任意国家 | random_subject_or_below = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_supporting_character | 遍历支持该 scope 政治运动的所有人物 | random_supporting_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_movement | character |
| random_treaty | 遍历条约（包括生效条约和草案） | random_treaty = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | treaty |
| random_valid_mass_migration_culture | 列出该 scope 国家中适合进行大规模迁移的文化 | random_valid_mass_migration_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | culture |
| random_war_participant | 遍历一场战争中的所有参与者 | random_war_participant = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | war | country |

## 流程 effect

流程 effect 控制其他 effect 的使用方式，包括条件判断、循环以及提示文本。它们始终可以在任意 scope 中使用

| Effect | 描述 | 示例 | Scopes | Targets |
|---|---|---|---|---|
| assert_if | 有条件地在运行时触发一个断言 | assert_if = { limit = { <triggers> } text = <string> (optional) } | none |  |
| custom_description | 为包裹的 effect 提供自定义描述，而非自动生成的描述 | custom_description = { text = <effect_localization_key> subject = <optional subject scope> #defaults to current scope object = <optional object scope> value = <optional script value> ... effects ... } | none |  |
| custom_description_no_bullet | 为包裹的 effect 提供自定义描述，而非自动生成的描述。同时确保不显示项目符号 | custom_description_no_bullet = { text = <effect_localization_key> subject = <optional subject scope> #defaults to current scope object = <optional object scope> value = <optional script value> ... effects ... } | none |  |
| custom_label | 仅作为提示文本，以 scope 作为对象（用于分组、本地化）。 | custom_label = key alternatively, custom_label = { text = key subject = scope (optional) <hidden effects> } | none |  |
| custom_label_no_bullet | 仅作为提示文本，以 scope 作为对象（用于分组、本地化）。无项目符号。 | custom_label_no_bullet = key alternatively, custom_label_no_bullet = { text = key subject = scope (optional) <hidden effects> } | none |  |
| custom_tooltip | 仅作为提示文本，以 scope 作为主语（用于分组、本地化）。 | custom_tooltip = key alternatively, custom_tooltip = { text = key subject = scope (optional) <hidden effects> } | none |  |
| custom_tooltip_no_bullet | 仅作为提示文本，以 scope 作为主语（用于分组、本地化）。无项目符号。 | custom_tooltip_no_bullet = key alternatively, custom_tooltip_no_bullet = { text = key subject = scope (optional) <hidden effects> } | none |  |
| else | 当前一个 'if' 或 'else_if' 的 limit 条件未满足时，执行包裹的 effect | if = { limit = { <triggers> } <effects> } else = { <effects> } | none |  |
| else_if | 当前一个 'if' 或 'else_if' 的 limit 条件未满足，且自身的 limit 条件满足时，执行包裹的 effect | if = { limit = { <triggers> } <effects> } else_if = { limit = { <triggers> } <effects> } | none |  |
| hidden_effect | 包裹的 effect 不会显示在提示文本中 | hidden_effect = { <more effects> } | none |  |
| if | 当 limit 条件满足时执行包裹的 effect | if = { limit = { <triggers> } <effects> } | none |  |
| random | 依据随机概率执行一个 effect，否则不执行任何操作。 | random = { chance = 0-100 # random chance in percent. can also be a script value or complex math modifier = { ... } # optional MTTH-style modifier for the chance effects... # effects to run if the random roll succeeds } | none |  |
| random_list | 从加权随机列表中选择一个 effect 并执行。 | random_list = { 10 = { trigger = { enable / disable this effect } modifier = { if = { limit = { is_foo } add = 10 } # Note: can have multiple conditions in the same `modifier` block to # have different scenarios affect the chances differently if = { limit = { is_bar } add = 20 } } # Warning: do _not_ add multilpe `modifier` blocks, since only the last one # is taken into consideration. Instead, use multiple `if` conditions inside # only one `modifier` block (one for each effect, that is) <effect_1> } 30 = { # trigger is optional, leaving it out means this effect is enabled # modifier is also optional, it means that the base weight (30) is final # Note: totally fine to have a `modifier` block here. It's important to only # have one `modifier` block per effect, not one in total. <effect_2> } } The effects are weighted by their relative weights (10 and 30 in the example). E.g. in this example the first effect has a base 25% chance of being picked, while the second effect has a 75% base chance. The chance is given by the formula `Wn / Wt` where `Wn` is the weight of a specific event while `Wt` is the sum of all the weights. So the chances in the example are, respectively, 10 / 40 (25%) and 30 / 40 (75%). The weight of an effect can be modified by a `modifier` block. In the example, if the scoped object satisfies the `is_foo` trigger, its relative weight increases by 10. So in that situation, the relative weights would be 20 and 30 rather than 10 and 30, meaning the chances would be 40% and 60% rather than 25% and 75%. | none |  |
| show_as_tooltip | 包裹的 effect 仅显示在提示文本中（但不会实际执行） | show_as_tooltip = { <more effects> } | none |  |
| switch | 依据一个 trigger 进行分支，以评估另一个 trigger，并可选一个后备 trigger。 | switch = { trigger = simple_assign_trigger case_1 = { <effects> } case_2 = { <effects> } case_n = { <effects> } fallback = { <effects> } | none |  |
| while | 当 limit 条件满足或达到设定的迭代次数之前，重复执行包裹的 effect | while = { limit = { <triggers> } <effects> } while = { count = <integer> <effects> } Default max of 1000. | none |  |

## 日志 effect

日志 effect 出于测试和调试目的输出一条消息。它们始终可以在任意 scope 中使用。

| Effect | 描述 | 示例 | Scopes | Targets |
|---|---|---|---|---|
| assert_if | 有条件地在运行时触发一个断言 | assert_if = { limit = { <triggers> } text = <string> (optional) } | none |  |
| assert_read | 有条件地在读取时触发一个断言 | assert_read = yes / <string> | none |  |
| debug_log | 当此 effect 执行时向调试日志输出一条字符串 | debug_log = message the message can be a localization string with ROOT, SCOPE and PREV available | none |  |
| debug_log_scopes | 当此 effect 执行时将当前 scope 输出到调试日志 | debug_log_scopes = yes # log full scope info debug_log_scopes = no # log only current scope | none |  |
| error_log | 当此 effect 执行时向错误日志输出一条字符串 | error_log = message the message can be a localization string with ROOT, SCOPE and PREV available | none |  |
| random_log_scopes | 当此 effect 执行时将当前 scope 输出到随机日志。 | Only use temporarily for debugging purposes as it can introduce localized strings into the random log. random_log_scopes = yes # log full scope info random_log_scopes = no # log only current scope | none |  |

## 变量 effect

变量 effect 用于设置或更改[变量](Variable.md)的值。它们始终可以在任意 scope 中使用，但可能需要特定的 scope 才能影响正确的变量。

| Effect | 描述 | 示例 | Scopes | Targets |
|---|---|---|---|---|
| add_to_global_variable_list | 在指定持续时间内将 event target 添加到全局变量列表 | add_to_global_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| add_to_global_variable_map | 在指定持续时间内将 event target 添加到全局变量映射；无法更新已有键的值 | add_to_global_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| add_to_local_variable_list | 在指定持续时间内将 event target 添加到局部变量列表 | add_to_local_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| add_to_local_variable_map | 在指定持续时间内将 event target 添加到局部变量映射；无法更新已有键的值 | add_to_local_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| add_to_variable_list | 在指定持续时间内将 event target 添加到变量列表 | add_to_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| add_to_variable_map | 在指定持续时间内将 event target 添加到变量映射；无法更新已有键的值 | add_to_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| change_global_variable | 更改数值型全局变量的值 | change_global_variable = { name = <global variable> <operation type> = <value> } The valid operations are add, subtract, multiply, divide, modulo, min and max | none |  |
| change_local_variable | 更改数值型局部变量的值 | change_local_variable = { name = <local variable> <operation type> = <value> } The valid operations are add, subtract, multiply, divide, modulo, min and max | none |  |
| change_variable | 更改数值型变量的值 | change_variable = { name = <variable name> <operation type> = <value> } The valid operations are add, subtract, multiply, divide, modulo, min and max | none |  |
| clamp_global_variable | 将全局变量钳制在指定的最大值和最小值之间 | clamp_global_variable = { name = <global variable> max = <value> min = <value> } | none |  |
| clamp_local_variable | 将局部变量钳制在指定的最大值和最小值之间 | clamp_local_variable = { name = <local variable> max = <value> min = <value> } | none |  |
| clamp_variable | 将变量钳制在指定的最大值和最小值之间 | clamp_variable = { name = <variable name> max = <value> min = <value> } | none |  |
| clear_global_variable_list | 清空该列表 | clear_global_variable_list = variable_name | none |  |
| clear_global_variable_map | 清空该映射 | clear_global_variable_map = variable_name | none |  |
| clear_local_variable_list | 清空该列表 | clear_local_variable_list = variable_name | none |  |
| clear_local_variable_map | 清空该映射 | clear_local_variable_map = variable_name | none |  |
| clear_variable_list | 清空该列表 | clear_variable_list = variable_name | none |  |
| clear_variable_map | 清空该映射 | clear_variable_map = variable_name | none |  |
| every_in_global_list | 遍历全局列表中的所有项。 | every_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| every_in_list | 遍历列表中的所有项。 | every_in_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| every_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | every_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | every_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_variable_map | 遍历变量映射中的所有键。 | every_key_in_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| ordered_in_list | 遍历列表中的所有项。 | ordered_in_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | ordered_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | ordered_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_key_in_variable_map | 遍历变量映射中的所有键。 | ordered_key_in_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| random_in_list | 遍历列表中的所有项。 | random_in_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| random_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | random_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | random_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_variable_map | 遍历变量映射中的所有键。 | random_key_in_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| remove_from_global_variable_map | 从全局变量映射中移除目标 | remove_from_global_variable_map = { name = name of the map key = event target } | none |  |
| remove_from_list | 将当前 scope 从指定名称的列表中移除 | remove_from_list = <list_name> | none |  |
| remove_from_local_variable_map | 从局部变量映射中移除目标 | remove_from_variable_map = { name = name of the map key = event target } | none |  |
| remove_from_variable_map | 从变量映射中移除目标 | remove_from_variable_map = { name = name of the map key = event target } | none |  |
| remove_global_variable | 移除一个全局变量 | remove_global_variable = variable_name | none |  |
| remove_list_global_variable | 从全局变量列表中移除目标 | remove_list_global_variable = { name = <global variable> target = <event target> } | none |  |
| remove_list_local_variable | 从局部变量列表中移除目标 | remove_list_local_variable = { name = <local variable> target = <event target> } | none |  |
| remove_list_variable | 从变量列表中移除目标 | remove_list_variable = { name = <variable name> target = <event target> } | none |  |
| remove_variable | 移除一个变量 | remove_variable = variable_name | none |  |
| round_global_variable | 将全局变量四舍五入到最近的指定值 | round_global_variable = { name = <global variable> nearest = <script_value> } | none |  |
| round_local_variable | 将局部变量四舍五入到最近的指定值 | round_local_variable = { name = <local variable> nearest = <script_value> } | none |  |
| round_variable | 将变量四舍五入到最近的指定值 | round_variable = { name = <variable name> nearest = <script_value> } | none |  |
| set_global_variable | 设置一个全局变量 | set_global_variable = { name = <global variable> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } This variable will be accessible with global_var:<variable name>. Can also be used as set_global_variable = X (equivalent to set_global_variable = { name = X value = yes }) | none |  |
| set_local_variable | 设置一个局部变量 | set_local_variable = { name = <local variable> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } This variable will be accessible with local_var:<variable name>, until the end of the current effect or event chain. Can also be used as set_local_variable = X (equivalent to set_local_variable = { name = X value = yes }) | none |  |
| set_variable | 设置一个变量 | set_variable = { name = <variable name> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } This variable will be accessible from the scope where it is set with var:<variable name>. Can also be used as set_variable = X (equivalent to set_variable = { name = X value = yes }) | none |  |
| sort_global_variable_list | 对全局变量列表排序 | sort_global_variable_list = { name = <global variable> order = <math script> } | none |  |
| sort_local_variable_list | 对局部变量列表排序 | sort_local_variable_list = { name = <local variable> order = <math script> } | none |  |
| sort_variable_list | 对变量列表排序 | sort_variable_list = { name = <variable name> order = <math script> } | none |  |

## 按 scope 分类的 effect

下表按所需 scope 列出各 effect。较少使用的 scope 以及只有少量专属 effect 的 scope 已省略，可在完整 effect 列表中找到。迭代器（iterator）已省略，可在上文或下文找到。部分 effect 会重复出现，因为它们可用于多个 scope。

### 无/任意 scope

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_to_global_variable_list | 在给定的持续时间内将 event target 添加到全局变量列表 | add_to_global_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } |  |
| add_to_global_variable_map | 在给定的持续时间内将 event target 添加到全局变量映射（map）中；无法更新已有键的值 | add_to_global_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } |  |
| add_to_list | 将当前 scope 添加到任意命名的列表中（若列表尚不存在则创建），以便稍后在（未中断的）事件链中引用 | scope = { add_to_list = <name_of_list> } add_to_list = { name = <name_of_list> value = <script_value> } NOTE, if adding a permanent target to a temporary list, the whole list becomes permanent |  |
| add_to_local_variable_list | 在给定的持续时间内将 event target 添加到局部变量列表 | add_to_local_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } |  |
| add_to_local_variable_map | 在给定的持续时间内将 event target 添加到局部变量映射（map）中；无法更新已有键的值 | add_to_local_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } |  |
| add_to_temporary_list | 将当前 scope 添加到任意命名的列表中（若列表尚不存在则创建），以便稍后在同一 effect 中引用 | add_to_temporary_list = <name_of_list> add_to_temporary_list = { name = <name_of_list> value = <script_value> } NOTE, if adding a temporary target to a permanent list, the list will stay permanent |  |
| add_to_variable_list | 在给定的持续时间内将 event target 添加到变量列表 | add_to_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } |  |
| add_to_variable_map | 在给定的持续时间内将 event target 添加到变量映射（map）中；无法更新已有键的值 | add_to_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } |  |
| assert_if | 在运行时按条件触发断言（assert） | assert_if = { limit = { <triggers> } text = <string> (optional) } |  |
| assert_read | 在读取时按条件触发断言（assert） | assert_read = yes / <string> |  |
| cancel_imposition | 取消 scope 中对该项法律（而非法律类型）的强制推行 | scope:country.imposed_law = { cancel_imposition = yes } |  |
| change_global_variable | 更改数值型全局变量的值 | change_global_variable = { name = <global variable> <operation type> = <value> } The valid operations are add, subtract, multiply, divide, modulo, min and max |  |
| change_local_variable | 更改数值型局部变量的值 | change_local_variable = { name = <local variable> <operation type> = <value> } The valid operations are add, subtract, multiply, divide, modulo, min and max |  |
| change_variable | 更改数值型变量的值 | change_variable = { name = <variable name> <operation type> = <value> } The valid operations are add, subtract, multiply, divide, modulo, min and max |  |
| clamp_global_variable | 将全局变量限制在指定的最大值和最小值之间 | clamp_global_variable = { name = <global variable> max = <value> min = <value> } |  |
| clamp_local_variable | 将局部变量限制在指定的最大值和最小值之间 | clamp_local_variable = { name = <local variable> max = <value> min = <value> } |  |
| clamp_variable | 将变量限制在指定的最大值和最小值之间 | clamp_variable = { name = <variable name> max = <value> min = <value> } |  |
| clear_global_variable_list | 清空该列表 | clear_global_variable_list = variable_name |  |
| clear_global_variable_map | 清空该映射 | clear_global_variable_map = variable_name |  |
| clear_local_variable_list | 清空该列表 | clear_local_variable_list = variable_name |  |
| clear_local_variable_map | 清空该映射 | clear_local_variable_map = variable_name |  |
| clear_saved_scope | 从顶层 scope 中清除一个已保存的 scope | save_scope_as = cool_scope -> clear_saved_scope = cool_scope |  |
| clear_variable_list | 清空该列表 | clear_variable_list = variable_name |  |
| clear_variable_map | 清空该映射 | clear_variable_map = variable_name |  |
| create_country | 创建一个新国家 | create_country = { tag = TAG # optional, if not specified origin's tag will be used origin = country # optional, newly created country will inherit certain values from the origin country # at least one of tag or origin must be supplied state = state # can be repeated; at least one state or province must be supplied province = province # can be repeated; at least one state or province must be supplied # both states and provinces can be supplied at the same time on_created = effect # optional effect that will be run with the newly created country in scope } |  |
| create_dynamic_country | 创建一个带有动态 tag 的新国家 | create_dynamic_country = { origin = country # optional, newly created country may inherit certain values from the origin country country_type = country type # optional if origin is set, may be repeated, will try to inherit country type from origin if not specified tier = country tier # optional if origin is set, may be repeated, will try to inherit country tier from origin if not specified culture = culture # optional if origin is set, may be repeated, will try to inherit cultures from origin if not specified religion = religion # optional if origin is set, if no religion is specified, will try to inherit religion from origin if not specified capital = state # optional if states have been supplied, will try to set a capital from supplied states if not specified social_hierarchy = social hierarchy key # optional; if not specified: same as origin's if origin is set, default hierarchy otherwise cede_state_trigger = trigger # if this trigger is set, each state in the world for which it evaluates true will be ceded to the new country color = rgb # optional, will try to inherit map color from origin if not specified primary_unit_color = rgb # optional, will try to inherit unit color from origin if not specified secondary_unit_color = rgb # optional, will try to inherit unit color from origin if not specified tertiary_unit_color = rgb # optional, will try to inherit unit color from origin if not specified on_created = effect # optional effect that will be run with the newly created country in scope } |  |
| create_treaty | 在国家之间创建一项条约 | create_treaty = { name = <loc key> # (default: empty) if specified, this treaty's name will be determined by the localization of the specified key first_country = <country> # (default: none) must _not_ be specified if the created treaty is an amendment second_country = <country> # (default: none) must _not_ be specified if the created treaty is an amendment amends = <treaty> # (default: none) if specified, the created treaty will be an amendment to the specified treaty is_draft = yes \| no # (default: yes) must be yes if this treaty is an amendement to an existing treaty entered_into_force_on = <date> # (default: none) means today = true if not specified (for non-drafts). Must _not_ be specified for drafts. Cannot be in the future binding_period = { # (default: 0) must be a nonnegative number, fractional parts will be ignored (truncation) days = <nonnegative number> \| weeks = <nonnegative number> \| months = <nonnegative number> \| years = <nonnegative number> } articles_to_create = { # (default: empty) non-amendments must have at least one article to create { article = <key> # (default: empty) the type of article (determined by script) source_country = <country> # (default: none) directed articles _must_ specify this value, mutual articles _must not_ specify this value target_country = <country> # (default: none) directed articles _must_ specify this value, mutual articles _must not_ specify this value inputs = { # (default: empty) list of inputs values as required by the article { quantity = <positive number> \| goods = <goods> \| state = <state> \| strategic_region = <strategic region> \| company = <company> \| building_type = <building_type> \| law_type = <law_type> \| country = <country> } { ... } # one input per required input of the corresponding article type } } # some examples of valid articles { article = alliance } # mutual, no inputs { article = goods_transfer # directed source_country = c:FRA # because directed target_country = c:GBR # because directed inputs = { { quantity = 250 } # because goods_transfer has required_inputs = { quantity goods } { goods = g:coal } # because goods_transfer has required_inputs = { quantity goods } } } } } |  |
| custom_description | 为其中的 effect 使用自定义描述，而非自动生成的描述 | custom_description = { text = <effect_localization_key> subject = <optional subject scope> #defaults to current scope object = <optional object scope> value = <optional script value> ... effects ... } |  |
| custom_description_no_bullet | 为其中的 effect 使用自定义描述，而非自动生成的描述。同时确保不显示项目符号 | custom_description_no_bullet = { text = <effect_localization_key> subject = <optional subject scope> #defaults to current scope object = <optional object scope> value = <optional script value> ... effects ... } |  |
| custom_label | 仅显示一个工具提示，以 scope 作为对象（用于分组、本地化）。 | custom_label = key alternatively, custom_label = { text = key subject = scope (optional) <hidden effects> } |  |
| custom_label_no_bullet | 仅显示一个工具提示，以 scope 作为对象（用于分组、本地化）。不显示项目符号。 | custom_label_no_bullet = key alternatively, custom_label_no_bullet = { text = key subject = scope (optional) <hidden effects> } |  |
| custom_tooltip | 仅显示一个工具提示，以 scope 作为主体（用于分组、本地化）。 | custom_tooltip = key alternatively, custom_tooltip = { text = key subject = scope (optional) <hidden effects> } |  |
| custom_tooltip_no_bullet | 仅显示一个工具提示，以 scope 作为主体（用于分组、本地化）。不显示项目符号。 | custom_tooltip_no_bullet = key alternatively, custom_tooltip_no_bullet = { text = key subject = scope (optional) <hidden effects> } |  |
| debug_log | 当此 effect 执行时，向调试日志记录一条字符串 | debug_log = message the message can be a localization string with ROOT, SCOPE and PREV available |  |
| debug_log_scopes | 当此 effect 执行时，将当前 scope 记录到调试日志 | debug_log_scopes = yes # log full scope info debug_log_scopes = no # log only current scope |  |
| else | 若前一个 'if' 或 'else_if' 的 limit 条件未满足，则执行其中的 effect | if = { limit = { <triggers> } <effects> } else = { <effects> } |  |
| else_if | 若前一个 'if' 或 'else_if' 的 limit 条件未满足，且自身的 limit 条件满足，则执行其中的 effect | if = { limit = { <triggers> } <effects> } else_if = { limit = { <triggers> } <effects> } |  |
| error_log | 当此 effect 执行时，向错误日志记录一条字符串 | error_log = message the message can be a localization string with ROOT, SCOPE and PREV available |  |
| execute_event_option | 执行指定事件中指定事件选项的 effect | execute_event_option = { event = events.1 option = 0 } |  |
| hidden_effect | 其中的 effect 不会显示在工具提示中 | hidden_effect = { <more effects> } |  |
| if | 若 limit 条件满足，则执行其中的 effect | if = { limit = { <triggers> } <effects> } |  |
| post_audio_event | 在一个 persistent = true 的音频对象上运行音频事件 | post_audio_event = { persistent_object = [object_name] # For example music_manager event = [audio_event] # For example start_debug_music } |  |
| post_notification | 发布通知 |  |  |
| post_proposal | 发布提案 |  |  |
| random | 根据随机概率运行一个 effect，否则什么都不做。 | random = { chance = 0-100 # random chance in percent. can also be a script value or complex math modifier = { ... } # optional MTTH-style modifier for the chance effects... # effects to run if the random roll succeeds } |  |
| random_list | 从加权随机列表中选择一个 effect 并执行。 | random_list = { 10 = { trigger = { enable / disable this effect } modifier = { if = { limit = { is_foo } add = 10 } # Note: can have multiple conditions in the same `modifier` block to # have different scenarios affect the chances differently if = { limit = { is_bar } add = 20 } } # Warning: do _not_ add multilpe `modifier` blocks, since only the last one # is taken into consideration. Instead, use multiple `if` conditions inside # only one `modifier` block (one for each effect, that is) <effect_1> } 30 = { # trigger is optional, leaving it out means this effect is enabled # modifier is also optional, it means that the base weight (30) is final # Note: totally fine to have a `modifier` block here. It's important to only # have one `modifier` block per effect, not one in total. <effect_2> } } The effects are weighted by their relative weights (10 and 30 in the example). E.g. in this example the first effect has a base 25% chance of being picked, while the second effect has a 75% base chance. The chance is given by the formula `Wn / Wt` where `Wn` is the weight of a specific event while `Wt` is the sum of all the weights. So the chances in the example are, respectively, 10 / 40 (25%) and 30 / 40 (75%). The weight of an effect can be modified by a `modifier` block. In the example, if the scoped object satisfies the `is_foo` trigger, its relative weight increases by 10. So in that situation, the relative weights would be 20 and 30 rather than 10 and 30, meaning the chances would be 40% and 60% rather than 25% and 75%. |  |
| random_log_scopes | 当此 effect 执行时，将当前 scope 记录到随机日志。 | Only use temporarily for debugging purposes as it can introduce localized strings into the random log. random_log_scopes = yes # log full scope info random_log_scopes = no # log only current scope |  |
| remove_from_global_variable_map | 从全局变量映射中移除目标 | remove_from_global_variable_map = { name = name of the map key = event target } |  |
| remove_from_list | 将当前 scope 从命名列表中移除 | remove_from_list = <list_name> |  |
| remove_from_local_variable_map | 从局部变量映射中移除目标 | remove_from_variable_map = { name = name of the map key = event target } |  |
| remove_from_variable_map | 从变量映射中移除目标 | remove_from_variable_map = { name = name of the map key = event target } |  |
| remove_global_variable | 移除一个全局变量 | remove_global_variable = variable_name |  |
| remove_list_global_variable | 从全局变量列表中移除目标 | remove_list_global_variable = { name = <global variable> target = <event target> } |  |
| remove_list_local_variable | 从局部变量列表中移除目标 | remove_list_local_variable = { name = <local variable> target = <event target> } |  |
| remove_list_variable | 从变量列表中移除目标 | remove_list_variable = { name = <variable name> target = <event target> } |  |
| remove_local_variable | 移除一个局部变量 | remove_local_variable = variable_name |  |
| remove_variable | 移除一个变量 | remove_variable = variable_name |  |
| round_global_variable | 将全局变量四舍五入到最近的指定值 | round_global_variable = { name = <global variable> nearest = <script_value> } |  |
| round_local_variable | 将局部变量四舍五入到最近的指定值 | round_local_variable = { name = <local variable> nearest = <script_value> } |  |
| round_variable | 将变量四舍五入到最近的指定值 | round_variable = { name = <variable name> nearest = <script_value> } |  |
| save_scope_as | 将当前 scope 保存为任意命名的目标，以便稍后在（未中断的）事件链中引用 | save_scope_as = <string> |  |
| save_scope_value_as | 将数值或布尔值保存为任意命名的目标，以便稍后在（未中断的）事件链中引用 | save_scope_value_as = { name = <string> value = x } |  |
| save_temporary_scope_as | 将当前 scope 保存为任意命名的临时目标，以便稍后在同一 effect 中引用 | save_temporary_scope_as = <string> |  |
| save_temporary_scope_value_as | 将数值或布尔值保存为任意命名的临时目标，以便稍后在同一 effect 中引用 | save_temporary_scope_value_as = { name = <string> value = x } |  |
| set_global_variable | 设置一个全局变量 | set_global_variable = { name = <global variable> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } This variable will be accessible with global_var:<variable name>. Can also be used as set_global_variable = X (equivalent to set_global_variable = { name = X value = yes }) |  |
| set_local_variable | 设置一个局部变量 | set_local_variable = { name = <local variable> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } This variable will be accessible with local_var:<variable name>, until the end of the current effect or event chain. Can also be used as set_local_variable = X (equivalent to set_local_variable = { name = X value = yes }) |  |
| set_variable | 设置一个变量 | set_variable = { name = <variable name> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } This variable will be accessible from the scope where it is set with var:<variable name>. Can also be used as set_variable = X (equivalent to set_variable = { name = X value = yes }) |  |
| show_as_tooltip | 其中的 effect 仅显示在工具提示中（但不会实际执行） | show_as_tooltip = { <more effects> } |  |
| sort_global_variable_list | 对全局变量列表排序 | sort_global_variable_list = { name = <global variable> order = <math script> } |  |
| sort_local_variable_list | 对局部变量列表排序 | sort_local_variable_list = { name = <local variable> order = <math script> } |  |
| sort_variable_list | 对变量列表排序 | sort_variable_list = { name = <variable name> order = <math script> } |  |
| start_tutorial_lesson | 启动具有给定键的教程课程。若教程未运行、课程已完成（或已在运行中），或课程无法触发（例如 trigger 失败），则不做任何事 |  |  |
| switch | 对一个 trigger 进行判断，以评估另一个 trigger，并可带一个可选的回退 trigger。 | switch = { trigger = simple_assign_trigger case_1 = { <effects> } case_2 = { <effects> } case_n = { <effects> } fallback = { <effects> } |  |
| trigger_event | 为当前 scope 触发一个事件 | trigger_event = <event id> trigger_event = { id = <event id> days/weeks/months/years = <integer value> popup = yes (optional) } |  |
| while | 当 limit 条件满足时，或达到设定的迭代次数之前，重复执行其中的 effect | while = { limit = { <triggers> } <effects> } while = { count = <integer> <effects> } Default max of 1000. |  |
### Character scope（人物作用域）

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_career_length | 增加人物当前某一职位的任职时长。职位可以是具体的数据库职位，也可以是职位类型（例如 general）。若未指定职位，则应用于所有有任职结束日期的职位。 | add_career_length = { role = role_key/role_type days/months/years = 5 random_range = { 0.8 1.2 } } |  |
| add_character_role | 为人物添加一个新职位，可使用原型（archetype）或数据库职位 | add_character_role = general/character_role_general |  |
| add_commander_rank | 将人物晋升/降级给定数量的军衔等级 | add_commander_rank = integer |  |
| add_experience | 为指挥官增加一定数量的经验 | add_experience = 0.2 |  |
| add_modifier | 为作用域中的对象添加一个有时限的 modifier 效果 | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_random_trait | 随机添加指定类别中一个符合条件的特质 | add_random_trait = personality / skill / condition |  |
| add_trait | 为人物添加一个特质 | add_trait = trait |  |
| change_character_culture | 改变作用域人物的文化 | change_character_culture = cu:colombian | culture |
| change_character_religion | 改变作用域人物的宗教 | change_character_religion = rel:protestant | religion |
| disinherit_character | 剥夺作用域人物在其适用的所有国家中的继承人地位。 | scope:larry = { disinherit_character = yes } |  |
| exile_character | 将人物流放至流放池 | exile_character = yes |  |
| free_character_from_void | 将人物从虚空（void）中释放，若设为 no 则改为删除该人物 | free_character_from_void = yes |  |
| kill_character | 杀死一个人物 | kill_character = bool (yes - kill [by default], no - don't do anything) kill_character = { hidden = bool (yes - without notification; no - show notification [by default]) value = bool (yes - kill [by default], no - don't do anything) } |  |
| place_character_in_void | 将人物放逐到虚空，时长为人物被删除前保留的时间 | place_character_in_void = months |  |
| remove_as_interest_group_leader | 将人物从利益集团领袖的位置上移除 | remove_as_interest_group_leader = yes |  |
| remove_character_role | 移除人物的一个现有职位，可使用原型或数据库职位 | remove_character_role = general/character_role_general |  |
| remove_modifier | 移除作用域中对象的一个有时限的 modifier 效果 | remove_modifier = static_modifier_name |  |
| remove_trait | 移除人物的一个特质 | remove_trait = trait |  |
| replace_character_roles | 将人物的一个或多个现有职位替换为其他职位，可使用原型或数据库职位 | replace_character_role = { add = { roles } remove = { roles } remove_all = no/yes } |  |
| set_as_adult | 若作用域人物尚未成年，则将其变为成年人。 | set_as_adult = yes |  |
| set_as_interest_group_leader | 将人物设为利益集团领袖 | set_as_interest_group_leader = yes |  |
| set_career_length | 从现在起设置人物某一职位的任职时长。职位可以是具体的数据库职位，也可以是职位类型（例如 general）。若未指定职位，则应用于所有有任职结束日期的职位。 | set_career_length = { role = role_key/role_type days/months/years = 10 random_range = { 0.8 1.2 } } |  |
| set_character_as_ruler | 将作用域人物设为其国家的统治者。 | scope:larry = { set_character_as_ruler = yes } 注意：不要对特许公司使用此 effect，因为人物的所属国家会受到影响 |  |
| set_character_busy_and_immortal | 将人物标记为忙碌且不朽，或清除该标记 | set_character_busy = bool |  |
| set_character_immortal | 设置作用域人物是否不朽。 | scope:larry = { set_character_immortal = yes/no } |  |
| set_commander_rank | 将人物晋升/降级到给定的军衔数值 | set_commander_rank = 3 |  |
| set_first_name | 将人物的名字更改为一个本地化键 | set_first_name = loc_key |  |
| set_home_country | 设置人物的原属国。这会使其开始认为自己是被流放的，即 was_exiled 对其开始判定为 yes。 | set_home_country = c:FRA | country |
| set_home_country_definition | 将人物的原属国直接设置为一个 tag，可用此方法避免确认该 tag 是否存在，这会使其成为流亡者 | set_home_country_definition = cd:FRA | country_definition |
| set_home_state | 更改作用域人物的家乡州 | set_home_state = <state scope> | state |
| set_ideology | 更改作用域人物的意识形态 | set_ideology = ideology:<ideology key> | ideology |
| set_interest_group | 设置人物的利益集团 | set_interest_group = ruler.interest_group | interest_group |
| set_is_noble | 设置作用域人物的贵族标记。 | set_is_noble = yes/no |  |
| set_last_name | 将人物的姓氏更改为一个本地化键 | set_last_name = loc_key |  |
| transfer_character | 将当前作用域人物转移至目标国家 | transfer_character = country | country |
| transfer_to_formation | 将作用域人物转移至目标编队 | transfer_to_formation = scope:formation | military_formation |

### Company scope（公司作用域）

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_company_monopoly | 为公司作用域添加一个垄断 | add_company_monopoly = bt:building_textile_mills | building_type |
| add_owned_country | 将作用域公司设为目标国家的创始公司 | set_founding_company = country:key | country |
| remove_owned_country | 移除作用域公司对目标国家的所有权 | remove_owned_country = country:key | country |
| set_company_establishment_date | 设置作用域公司的成立日期 | set_company_establishment_date = 1782.7.18 |  |
| set_company_state_region | 设置作用域公司所在的州区域，使公司建筑可以建造在那里 | set_company_state_region = s:STATE_WALLONIA | state_region |

### Country scope（国家作用域）

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| activate_law | 为国家激活一项法律，不会应用 `when_enacted` 效果 | activate_law = law_type:<law_key> | law_type |
| activate_production_method | 为国家/州内某一类型的建筑激活指定的生产方式 | activate_production_method = { building_type = building_key production_method = production_method_key } |  |
| add_banned_goods | 为国家添加对某种商品的全面禁令 | add_banned_goods = <goods key/scope> | goods |
| add_change_relations_progress | 增加两个国家之间关系变动的进度 | add_change_relations_progress = { country = country scope/tag value = amount } |  |
| add_company | 将公司类型添加到国家的公司中 | add_company = company_type:key | company_type |
| add_country_monopoly | 为国家作用域添加一个垄断 | add_country_monopoly = bt:building_textile_mills | building_type |
| add_culture_acceptance_modifier | 在作用域国家对给定文化应用一个文化接受度修正。除必需的 culture 参数外，此 effect 的语法与 add_modifier 相同。 | add_culture_acceptance_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } |  |
| add_enactment_modifier | 为作用域中的对象添加一个与立法相关的有时限的 modifier 效果 | add_enactment_modifier = { name = modifier_key } |  |
| add_enactment_phase | 以增量方式更改作用域国家当前的立法阶段。结果将被限制在 0 与 NPolitics::LAW_ENACTMENT_MAX_PHASES 之间。若结果等于 NPolitics::LAW_ENACTMENT_MAX_PHASES，正在通过的法律将通过。 |  |  |
| add_enactment_setback | 以增量方式更改作用域国家当前的立法受挫次数。结果将被限制在 0 与 country_law_max_setbacks_add 之间。若结果等于 country_law_max_setbacks_add，立法将失败 |  |  |
| add_era_researched | 在国家作用域中将指定时代标记为已研究 | add_era_researched = era |  |
| add_fervor_target_modifier | 在作用域国家对给定文化应用一个狂热目标修正。除必需的 culture 参数外，此 effect 的语法与 add_modifier 相同。 | add_fervor_target_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } |  |
| add_investment_pool | 直接向投资池注入资金 | add_investment_pool = 50 |  |
| add_journal_entry | 向作用域国家的日志添加一个日志条目，可选保存 scope 目标 | add_journal_entry = { type = <key> target = <scope> } |  |
| add_law_progress | 为当前正在通过的法律的当前检查点增加 x% 进度（范围为 [0, 1]，0.1 表示 10 个百分点） | add_law_progress = 0.1 / -0.1 |  |
| add_liberty_desire | 为附属国增加独立倾向。若作用域国家不是某个外交条约中的附属国，则不产生任何效果。 | add_liberty_desire = -5 |  |
| add_loyalists | 为作用域国家的人口增加忠诚派。除 value 外所有参数均为可选。 | value is the percentage of each pop that will move towards loyalism. if interest_group is specified pops gain loyalists based on their ig membership. pop type and strata are mutually exclusive. add_radicals = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } |  |
| add_modifier | 为作用域中的对象添加一个有时限的 modifier 效果 | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_primary_culture | 将一种文化添加到国家的主要文化中 | add_primary_culture = <culture> | culture |
| add_radicals | 为作用域国家的人口增加激进派。除 value 外所有参数均为可选。 | value is the percentage of each pop that will move towards radicalism. if interest_group is specified pops gain radicals based on their ig membership. pop type and strata are mutually exclusive. add_radicals = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } |  |
| add_taxed_goods | 为国家添加对某种商品的消费税 | add_taxed_goods = <goods key/scope> | goods |
| add_technology_progress | 增加技术进度 | add_technology_progress = { progress = <script_value> technology = <technology key> } |  |
| add_technology_researched | 在国家作用域中研究指定技术 | add_technology_researched = technology |  |
| add_treasury | 为国家增加/扣除资金 | add_treasury = fixed point |  |
| annex | 吞并一个国家 | annex = scope | country |
| annex_as_civil_war | 吞并一个国家，并附带内战中获胜方的全部继承效果 | annex_as_civil_war = scope | country |
| annex_with_incorporation | 吞并一个国家，并继承其各州的整合状态 | annex_with_incorporation = scope | country |
| call_election | 将国家的下次选举日期设置为 N 个月后 | call_election = { months = 6 } |  |
| cancel_enactment | 停止该国当前正在进行的立法 | cancel_enactment = yes |  |
| change_infamy | 更改作用域国家的恶名 | change_infamy = amount |  |
| change_institution_investment_level | 增加/减少机构的投资等级 | change_institution_investment_level = { institution = institution_police investment = -1 } |  |
| change_relations | 更改两个国家之间的关系 | change_relations = { country = country scope/tag value = amount } |  |
| change_subject_type | 更改作用域国家的附属国类型，同时保留当前的独立倾向值。 | change_subject_type = subject_type_dominion |  |
| change_tag | 更改作用域国家的 tag | c:GBR = { change_tag = FRA } |  |
| change_tension | 更改两个国家之间的紧张度 | change_tension = { country = country scope/tag value = amount } |  |
| clear_debt | 清除国家贷款 = bool |  |  |
| clear_enactment_modifier | 清除作用域国家当前所有的立法 modifier。 |  |  |
| clear_scaled_debt | 清除相当于目标最大信用额度乘以指定乘数的债务量 | clear_scaled_debt = value |  |
| complete_objective_subgoal | 完成一个目标子目标 | complete_objective_subgoal = <key> |  |
| copy_laws | 复制目标国家作用域的宪法 | 注意：这会中止当前正在进行的立法。copy_laws = scope | country |
| create_bidirectional_truce | 在两个国家之间创建一个双向停战 | create_bidirectional_truce = { country = country scope/tag months = integer } |  |
| create_character | 创建一个人物，任何选项都可以省略。 | create_character = { name = loc_key or alternatively first_name and last_name separately culture = culture_tag religion = religion scope (if omitted, it's defined by the character's culture religion) female = bool or character scope (gets the same value from the character) noble = bool or character scope (gets the same value from the character) ruler = bool heir = bool historical = bool age = integer, range, or character scope (gets the age from a character) ideology = ideology key or scope interest_group = interest group key or scope template = base template to generate the character from on_created = effect save_scope_as = scope name trait_generation = effect hq = HQ scope or strategic region scope } |  |
| create_diplomatic_catalyst | 创建一个新的外交催化剂 | create_diplomatic_catalyst = { type = catalyst_relations_level_increased arget = <country scope> } |  |
| create_diplomatic_pact | 在两个国家之间创建一个外交条约，作用域国家为发起方 | create_diplomatic_pact = { country = country scope/tag first_state = state scope/tag second_state = state scope/tag type = diplomatic action type } |  |
| create_diplomatic_play | 以作用域对象为发起方创建一个外交博弈，add_initiator_backers、add_target_backers 和 add_war_goal 可作为直接 effect 包含在内 | create_diplomatic_play = { name = loc_key escalation = integer between 0 and 100 target_country = country scope/tag type = diplomatic play type annex_as_civil_war = yes/no add_initiator_backers = { list of country scopes/tags } add_target_backers = { list of country scopes/tags } add_war_goal = { holder = country scope/tag war_goal = <war goal key> target_state = <state scope> (if required) target_country = <country scope> (if required) target_region = <region scope> (if required) } } |  |
| create_incident | 创建一个产生恶名的外交事件，目标国家为受害方 | create_incident = { country = country scope/tag value = infamy amount } |  |
| create_military_formation | 创建一个军事编队 | create_military_formation = { # Optional name name = name # type defaults to army type = army/fleet hq_region = sr:region_russia # Optional, overrides the automatic supply hub selection supply_hub = s:STATE_MOSCOW # Add as many combat_unit specifications as necessary combat_unit = { type = unit_type:combat_unit_type_irregular_infantry # service_type defaults to regular and conscript is not applicable for fleets service_type = regular/conscript state_region = s:STATE_MOSCOW count = 5 } # mobilization_options are not applicable for fleets mobilization_options = { mobilization_option:mobilization_option_basic_supplies mobilization_option:mobilization_option_truck_transport } } |  |
| create_political_lobby | 创建一个新的政治游说团体 | create_political_lobby = { type = lobby_pro_country arget = <country scope> add_interest_group = <ig scope 1> add_interest_group = <ig scope 2> add_interest_group = <ig scope 3> } |  |
| create_political_movement | 在该国创建一个指定类型的政治运动，culture/religion 为可选 | create_political_movement = { movement_type = x religion = <scope> (if relevant) culture = <scope> (if relevant) } |  |
| create_power_bloc | 以作用域对象为领袖创建一个强权集团 | create_power_bloc = { name = loc_key map_color = { R G B } or hsv{ H S V } founding_date = yyyy.mm.dd, optional identity = power bloc identity key principle = power bloc principle key, can be repeated member = country scope, can be repeated } |  |
| create_ship | 在作用域国家中创建一艘船 | create_ship = { type = ship_type:key # Type of ship to create fleet = scope:fleet # Fleet to assign the created ship to save_scope_as = scope_name # If specified, saves the created ship in the given scope name name = loc_key # Optional name for the ship } |  |
| create_unidirectional_truce | 为一个国家创建针对另一个国家的单向停战 | create_unidirectional_truce = { country = country scope/tag months = integer } |  |
| deactivate_law | 为国家停用一项法律 |  | law_type |
| deactivate_parties | 停用作用域国家的政党。 | deactivate_parties = yes |  |
| decrease_autonomy | 将国家的附属国类型改为自治程度更低的一种 | decrease_autonomy = yes |  |
| end_truce | 结束两个国家之间的任何停战 | end_truce = country_scope | country |
| increase_autonomy | 将国家的附属国类型改为自治程度更高的一种 | increase_autonomy = yes |  |
| join_power_bloc | 作用域国家加入目标作用域国家所在的强权集团 | join_power_bloc = c:USA | country |
| kill_population | 杀死作用域国家人口中的一定数量的个体。 | All parameters except percent are optional. Pop type and strata cannot be used at the same time. kill_population = { value = <integer value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } |  |
| kill_population_percent | 杀死作用域国家人口中的一定百分比。 | All parameters except percent are optional. Pop type and strata cannot be used at the same time. kill_population_percent = { percent = <decimal value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } |  |
| liberate_slaves | 解放该国家/州的所有奴隶 | liberate_slaves = yes |  |
| liberate_slaves_in_incorporated_states | 解放该国已整合州的所有奴隶 | liberate_slaves_in_incorporated_states = yes |  |
| liberate_slaves_in_unincorporated_states | 解放该国未整合州的所有奴隶 | liberate_slaves_in_unincorporated_states = yes |  |
| make_independent | 使一个国家独立。 | make_independent = bool |  |
| play_as | 更改作用域国家的玩家将扮演的国家 | play_as = <scope> | country |
| random_subject_of_subject | 层级中直属附属国以下的任何国家 | random_subject_of_subject = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| recalculate_pop_ig_support | 重新计算并更新国家人口的利益集团成员身份 = bool |  |  |
| regime_change | 由作用域国家对目标国家执行政权更迭。 | regime_change = scope:upstart_country | country |
| remove_active_objective_subgoal | 移除一个激活的目标子目标 | remove_active_objective_subgoal = <key> |  |
| remove_banned_goods | 移除国家对某种商品的全面禁令 | remove_banned_goods = <goods key/scope> | goods |
| remove_company | 从国家的公司中移除指定类型的公司 | remove_company = company_type:key | company_type |
| remove_diplomatic_pact | 移除两个国家之间的一个外交条约，作用域国家为发起方 | remove_diplomatic_pact = { country = country scope/tag type = diplomatic action type } |  |
| remove_enactment_modifier | 移除作用域对象的一个与立法相关的有时限的 modifier 效果 |  |  |
| remove_modifier | 移除作用域中对象的一个有时限的 modifier 效果 | remove_modifier = static_modifier_name |  |
| remove_monopoly | 移除国家作用域中针对某一特定建筑的垄断 | remove_monopoly = bt:building_textile_mills | building_type |
| remove_primary_culture | 从国家的主要文化中移除一种文化 | remove_primary_culture = <culture> | culture |
| remove_taxed_goods | 移除国家对某种商品的消费税 | remove_taxed_goods = <goods key/scope> | goods |
| seize_investment_pool | 将投资池收归国库，并将所有私人建造队列中的条目转移到政府队列 = bool |  |  |
| set_capital | 在国家作用域中设置首都州 | set_capital = <state_region key> |  |
| set_country_type | 设置国家的国家类型，用于历史记录 |  |  |
| set_diplomats_expelled | 在作用域国家中驱逐目标国家的外交官 | set_diplomats_expelled = scope:target_country | country |
| set_export_tariff_level | 设置作用域国家中某种商品的出口关税等级 | set_export_tariff_level = { goods = g:iron level = max_tariffs } |  |
| set_government_wage_level | 设置作用域国家的政府工资等级 | set_government_wage_level = very_low/low/medium/high/very_high |  |
| set_heir | 将作用域国家的继承人设置为指定的人物作用域 | set_heir = scope_victoria | character |
| set_immune_to_revolutions | 使一个国家免受革命影响，或移除该免疫。 | set_immune_to_revolutions = yes/no |  |
| set_import_tariff_level | 设置作用域国家中某种商品的进口关税等级 | set_import_tariff_level = { goods = g:iron level = max_tariffs } |  |
| set_institution_investment_level | 设置机构的投资等级 | set_institution_investment_level = { institution = <key> level = x } |  |
| set_market_capital | 在国家作用域中设置市场首都 | set_market_capital = <state_region key> |  |
| set_military_wage_level | 设置作用域国家的军队工资等级 | set_military_wage_level = very_low/low/medium/high/very_high |  |
| set_mutual_secret_goal | 为作用域国家和目标国家设置相互的秘密 AI 目标 | set_mutual_secret_goal = { country = country scope/tag secret_goal = secret goal type } |  |
| set_next_election_date | 设置国家的下次选举日期 | set_next_election_date = year.month.day |  |
| set_only_legal_party_from_ig | 设置一国中唯一合法的政党，用于一党制国家法律。 | set_only_legal_party_from_ig = ruler.interest_group | interest_group |
| set_owes_obligation_to | 设置一个国家是否对另一个国家负有义务 | set_owes_obligation = { country = country scope/tag setting = yes/no } |  |
| set_relations | 设置两个国家之间的关系 | set_relations = { country = country scope/tag value = amount } |  |
| set_ruling_interest_groups | 为 scope 国家由一组利益集团组建政府 | set_ruling_interest_groups = { ig_tag1 ig_tag2 } |  |
| set_secret_goal | 为 scope 国家设定针对另一个国家的秘密 AI 目标 | set_secret_goal = { country = country scope/tag secret_goal = secret goal type } |  |
| set_social_hierarchy | 设定 scope 国家的社会层级 | set_social_hierarchy = <key> |  |
| set_state_religion | 将该国的国教改为指定的宗教 | set_state_religion = <religion_scope | religion |
| set_strategy | 为 scope 国家设定 AI 策略 | set_strategy = <key> |  |
| set_tax_level | 设定 scope 国家的总体税收等级 | set_tax_level = very_low/low/medium/high/very_high |  |
| set_tension | 设定两个国家之间的紧张度 | set_tension = { country = country scope/tag value = amount } |  |
| start_enactment | 为 scope 国家开始制定指定的法律类型 | start_enactment = law_type:law_multicultural | law_type |
| start_national_awakening | 开始一场文化觉醒 | start_national_awakening = { culture = cu:british # the culture that will have a national awakening months = 12 # the number of months the awakening will last for state_region = s:STATE_HOME_COUNTIES # optional, if not specified the state region with the highest literacy rate of the culture is used } |  |
| start_research_random_technology | scope 国家开始研究其可研究的任意随机技术 | start_research_random_technology = yes |  |
| take_on_scaled_debt | 转移相当于目标最大信贷额度指定乘数的债务 | take_on_scaled_debt = { who = <country scope> value = <0-1 value> } |  |
| try_form_government_with | 尝试以提供的利益集团组建新政府，若在给定合法性下不可行，则尝试将尽可能多的利益集团纳入政府 | try_form_government_with = { value = 30 interest_group_type = ig_armed_forces interest_group_type = ig_devout interest_group_type = ig_landowners } |  |
| unset_only_legal_party | 使该国恢复为非一党制国家，只要其他法律允许，多个政党可以并存 | unset_only_legal_party = yes |  |
| update_party_support | 更新 scope 国家的政党支持度 | update_party_support = yes |  |
| validate_subsidies | 验证一个国家所有建筑的补贴。原版游戏无使用 | validate_subsidies = bool |  |
| violate_sovereignty_join | scope 国家在侵犯主权战争中加入侵犯方或目标方一侧 | violate_sovereignty_accept = { violator = <country scope> target = <country scope> join_violator = yes/no } |  |

### 文化（Culture）scope

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_cultural_community_in_state | 为 scope 文化在目标州添加一个文化社区。 | cu:zulu = { add_cultural_community_in_state = scope:some_state } | state |
| add_cultural_obsession | 为 scope 文化添加一种新的痴迷 | add_cultural_obsession = <goods> |  |
| add_cultural_taboo | 为 scope 文化添加一种新的禁忌 | add_cultural_taboo = <goods> |  |
| add_fervor | 为 scope 文化增加狂热度 | add_fervor = 2.6 |  |
| add_tradition_trait | 为 scope 文化添加一个新的传统特质 | add_tradition_trait = <tradition_trait> |  |
| remove_cultural_obsession | 从 scope 文化移除一种痴迷 | remove_cultural_obsession = <goods> |  |
| remove_cultural_taboo | 从 scope 文化移除一种禁忌 | remove_cultural_taboo = <goods> |  |
| remove_tradition_trait | 从 scope 文化移除一个已有的传统特质 | remove_tradition_trait = <tradition_trait> |  |
| set_fervor | 设定 scope 文化的狂热度 | set_fervor = 3.0 |  |
| set_name_format | 设定 scope 文化的姓名格式 | set_name_format = first_last/last_first |  |

### 外交博弈（Diplomatic play）scope

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_diplomatic_play_war_support | 为 scope 外交博弈中的目标国家增加战争支持度。该数值会显示在工具提示的“局势”标题下 | add_diplomatic_play_war_support = { target = country value = value } |  |
| add_escalation | 为外交博弈增加升级度 | add_escalation = integer |  |
| add_initiator_backers | 将一个 tag/scope 国家加入外交博弈的发起方 | add_initiator_backers = { list of scopes/tags } |  |
| add_target_backers | 将一个 tag/scope 国家加入外交博弈的目标方 | add_target_backers = { list of scopes/tags } |  |
| add_war_goal | 为外交博弈添加一个战争目标。 | add_war_goal = { holder = country scope/tag war_goal = <war goal key> target_state = <state scope> (if required) target_country = <country scope> (if required) target_region = <region scope> (if required) primary_demand = yes (optional) } |  |
| end_play | 结束一场外交博弈 | end_play = bool |  |
| remove_initiator_backers | 从外交博弈的发起方移除一个 tag/scope 国家 | remove_initiator_backers = { list of scopes/tags } |  |
| remove_target_backers | 从外交博弈的目标方移除一个 tag/scope 国家 | remove_target_backers = { list of scopes/tags } |  |
| remove_war_goal | 从外交博弈移除一个战争目标。语法与 add_war_goal/create_diplomatic_play 相同 | remove_war_goal = { holder = country scope/tag war_goal = <war goal key> target_state = <state scope> (if required) target_country = <country scope> (if required) target_region = <region scope> (if required) } |  |
| resolve_play_for | 结束一方的外交博弈，使其获得战争目标 | resolve_play_for = initiator resolve_play_for = scope:custom_scoped_country | country |
| set_key | 为外交博弈设定名称 | set_key = loc_key |  |
| set_war | 将一场外交博弈设定为战争状态 | set_war = bool |  |

### 利益集团（Interest group）scope

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| abandon_revolution | 将利益集团从革命中移除 | abandon_revolution = yes/no |  |
| add_ideology | 为 scope 利益集团添加一种意识形态 | add_ideology = ideology:<ideology key> |  |
| add_modifier | 为 scope 对象添加带时限的 modifier 效果 | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_ruling_interest_group | 将利益集团加入政府 | add_ruling_interest_group = yes/no |  |
| join_revolution | 将利益集团加入正在进行的革命 | join_revolution = yes/no |  |
| remove_ideology | 从 scope 利益集团移除一种意识形态 | remove_ideology = ideology:<ideology key> |  |
| remove_modifier | 移除 scope 对象上带时限的 modifier 效果 | remove_modifier = static_modifier_name |  |
| remove_ruling_interest_group | 将 scope 利益集团从政府中移除 | remove_ruling_interest_group = yes/no |  |
| set_ig_trait | 为利益集团添加一个特质，或以相同认可度等级替换其当前特质 | set_ig_trait = ig_trait:ig_trait_engines_of_progress | interest_group_trait |
| set_interest_group_name | 将利益集团重命名为指定的本地化键名 | set_interest_group_name = x |  |

### 日志条目（Journal entry）scope

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_modifier | 为 scope 对象添加带时限的 modifier 效果 | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_progress | 为日志条目的进度条增加进度 | add_progress = { value = -5 name = example_progress_bar_name } |  |
| remove_modifier | 移除 scope 对象上带时限的 modifier 效果 | remove_modifier = static_modifier_name |  |
| set_bar_progress | 设定日志条目脚本化进度条的进度 | set_bar_progress = { value = -5 name = example_progress_bar_name } |  |
| set_target_technology | 为日志条目设定（新的）目标技术 scope | set_target_technology = <scope> |  |

### 军事编队（Military formation）scope

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_organization | 为 scope 军事编队增加指定数量的组织度 | add_organization = -10 |  |
| deploy_to_front | 将 scope 编队部署到目标前线 | deploy_to_front = p:xFAFAFA.front Can also take a base_camp parameter, will use given province to search for the nearest connected base camp deploy_to_front = { front = p:xFAFAFA.front base_camp = p:xFAFAFA = true, } | front |
| fully_mobilize_army | 完全动员 scope 陆军 | fully_mobilize_army = yes |  |
| mobilize_army | 动员 scope 陆军 | mobilize_army = yes |  |
| teleport_to_front | 将 scope 编队传送至目标前线 | teleport_to_front = p:xFAFAFA.front Can also take a base_camp parameter, will use given province to search for the nearest connected base camp teleport_to_front = { front = p:xFAFAFA.front base_camp = p:xFAFAFA = true, } | front |

### 政党（Party）scope

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_ig_to_party | 将目标利益集团加入 scope 政党 | py:py_key = { add_ig_to_party = ig:ig_key } | interest_group |
| add_momentum | 在竞选期间为政党增加势头 | add_momentum = value |  |
| disband_party | 将所有利益集团移出政党，使其解散 | disband_party = yes |  |
| remove_ig_from_party | 将目标利益集团移出 scope 政党 | py:py_key = { remove_ig_from_party = ig:ig_key } | interest_group |
| set_ruling_party | 将政党中的所有利益集团加入政府，并将其他所有利益集团移出政府 | set_ruling_party = yes |  |

### 政治游说团（Political lobby）scope

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_lobby_member | 将一个利益集团添加为 scope 政治游说团的成员 | add_lobby_member = scope:interest_group | interest_group |
| change_appeasement | 改变 scope 政治游说团的绥靖度 | change_appeasement = { amount = 1 factor = trade_agreement_formed } |  |
| disband_political_lobby | 解散 scope 政治游说团 | disband_political_lobby = yes |  |
| remove_lobby_member | 将一个利益集团从 scope 政治游说团成员中移除 | remove_lobby_member = scope:interest_group | interest_group |

### 政治运动（Political movement）scope

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_character_ideology | 将一种人物意识形态添加到 scope 政治运动的人物意识形态列表中 | add_character_ideology = ideology:<ideology key> |  |
| add_modifier | 为 scope 对象添加带时限的 modifier 效果 | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| remove_character_ideology | 从 scope 政治运动的人物意识形态列表中移除一种人物意识形态 | remove_character_ideology = ideology:<ideology key> |  |
| remove_modifier | 移除 scope 对象上带时限的 modifier 效果 | remove_modifier = static_modifier_name |  |
| set_bolpondering | 开始/停止扶植 scope 政治运动 | set_bolstering = yes/no |  |
| set_core_ideology | 设定政治运动的核心意识形态 | set_ideology = ideology:<ideology key> |  |
| set_suppression | 开始/停止镇压 scope 政治运动 | set_suppression = yes/no |  |

### 人口（Pop）scope

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_pop_wealth | 增加人口的财富 | add_pop_wealth = { wealth_distribution = { script_value } update_loyalties = yes/no } |  |
| change_pop_culture | 按指定百分比将 scope 人口的文化变更为指定文化 | change_pop_culture = { target = cu:spanish value = 0.33 } |  |
| change_pop_religion | 按指定百分比将 scope 人口的宗教变更为指定宗教 | change_pop_religion = { target = rel:catholic value = 0.5 } |  |
| change_poptype | 将人口的类型变更为给定类型 |  | pop_type |
| move_partial_pop | 将 scope 人口的一部分迁移到指定州（他们将成为失业者） | move_partial_pop = { state = s:STATE_TUSCANY.region_state:TUS } move_partial_pop = { state = s:STATE_TUSCANY.region_state:TUS population = 1000 } move_partial_pop = { state = s:STATE_TUSCANY.region_state:TUS population_ratio = 0.2 } NOTE: VERY IMPORTANT! This effect _may_ change the pop type of the moved pop. This will happen under the following conditions: 1. if the current pop type cannot be unemployed, the new pop type will be the default one 2.if the current pop type is a slave type and the target state does not allow slavery, the new pop type will be the default one |  |
| move_pop | 将 scope 人口整体迁移到指定州（他们将成为失业者） | move_pop = s:STATE_TUSCANY.region_state:TUS NOTE: VERY IMPORTANT! This effect _may_ change the pop type of the moved pop. This will happen under the following conditions: 1. if the current pop type cannot be unemployed, the new pop type will be the default one 2.if the current pop type is a slave type and the target state does not allow slavery, the new pop type will be the default one | state |
| set_pop_literacy | 设定人口劳动力的识字率百分比 | set_pop_literacy = { literacy_rate = { script_value } } |  |
| set_pop_qualifications | 为给定类型设定人口劳动力中具备资质的百分比 | set_pop_qualifications = { pop_type = {} qualifications = { script_value } } |  |
| set_pop_wealth | 设定人口的财富 | set_pop_wealth = { wealth_distribution = { script_value } update_loyalties = true/false } |  |

### 强权集团（Power bloc）scope

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_cohesion_number | 为 scope 强权集团增加指定数量的凝聚力 | add_cohesion_number = 100 (adds 100 points to Cohesion) |  |
| add_cohesion_percent | 为 scope 强权集团增加基于百分比的凝聚力 | add_cohesion_percent = -0.2 (reduces Cohesion by 20% of its maximum value) |  |
| add_leverage | 为 scope 强权集团增加对指定国家指定数量的影响力筹码 | If the value is positive, also reduces the amount of Leverage of all other Blocs proportionally to match add_leverage = { target = country_scope value = script_value } |  |
| add_modifier | 为 scope 对象添加带时限的 modifier 效果 | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_principle | 为强权集团添加原则 | power_bloc = { add_principle = test_principle_group_A_1 } |  |
| remove_modifier | 移除 scope 对象上带时限的 modifier 效果 | remove_modifier = static_modifier_name |  |
| remove_principle | 从强权集团移除原则 | power_bloc = { remove_principle = test_principle_group_A_1 } |  |
### 舰船 scope（Ship scope）

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| kill_crew | 杀死舰船乘员中给定数量的人员 | kill_crew = 20 |  |
| kill_crew_percent | 杀死舰船乘员中给定百分比的人员 | kill_crew_percent = 0.2 |  |
| kill_ship | 摧毁当前 scope 中的舰船 | kill_ship = bool # yes - 摧毁舰船[默认]，no - 不做任何事 |  |
| set_as_flagship | 将该舰船指派/取消指派为国家的旗舰 | set_as_flagship = yes/no |  |
| set_ship_owner | 设置舰船所属国家 | set_ship_owner = <country> | country |
| set_ship_owner_multiple | 设置舰船所属国家，在连续设置多艘舰船时使用，可将它们放入单一的移交舰队，然后使用 clear_ownership_transfer_fleet 清除 | set_ship_owner_multiple = <country> | country |

### 州 scope（State scope）

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| activate_building | 激活州中的一座建筑 | activate_building = { building = building_key } |  |
| activate_production_method | 为国家/州中某一类型的建筑激活指定名称的生产方式 | activate_production_method = { building_type = building_key production_method = production_method_key } |  |
| add_acceptance | 为州中的一种文化增加接受度增量 | add_acceptance = { culture = cu:romanian value = -10 } |  |
| add_cultural_community | 在当前 scope 的州中为目标文化添加一个文化社区。 | scope:some_state = { add_cultural_community = cu:zulu } | culture |
| add_culture_standard_of_living_modifier | 在当前 scope 的州中为给定文化应用一个生活水平修正。除必需的 culture 参数外，此 effect 的语法与 add_modifier 相同。 | add_culture_standard_of_living_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } |  |
| add_loyalists_in_state | 为当前 scope 的州中的人口添加忠诚派。除 value 外所有参数均为可选。 | value 是每个人口中向忠诚主义转变的百分比。如果指定了 interest_group，则人口根据其利益集团归属获得忠诚派。pop type 与 strata 互斥。 add_radicals_in_state = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } |  |
| add_modifier | 为 scope 中的对象添加一个限时修正 effect | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_radicals_in_state | 为当前 scope 的州中的人口添加激进派。除 value 外所有参数均为可选。 | value 是每个人口中向激进主义转变的百分比。如果指定了 interest_group，则人口根据其利益集团归属获得激进派。pop type 与 strata 互斥。 add_radicals_in_state = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } |  |
| add_religion_standard_of_living_modifier | 在当前 scope 的州中为给定宗教应用一个生活水平修正。除必需的 religion 参数外，此 effect 的语法与 add_modifier 相同。 | add_religion_standard_of_living_modifier = { religion = religion_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } |  |
| cede_treaty_port | 将 scope 州中的条约港割让给目标国家 | cede_treaty_port = scope/country | country |
| convert_population | 将不同宗教人口的 X% 改宗为指定宗教。 | convert_population = { target = rel:catholic value = 0.5 } |  |
| create_building | 在当前 scope 的州中创建一座建筑。支持的值有： | building = <building> activate_production_methods = { <production_methods> } subsidized = yes/no reserves = [0..1] (percentage of cash reserves the building should be created with) add_ownership = { (mutually exclusive with level) country = { (give ownership levels to a specific country) country = s:GBR (country script target) levels = 5 } country = { (give ownership levels to a specific building) type = building_financial_district (building type that will get ownership levels, should be self or other ownership type) region = STATE_SINAI (region where owning building is placed) country = s:GBR (country script target for a region) levels = 3 } } level = arable_land/integer(mutually exclusive with add_ownership) 若 level 为 arable_land，建筑将建到足以耗尽该州所有可用可耕地的等级。若 level 为整数，建筑将为该等级。请注意：如果州中已存在指定类型的建筑，此 effect 的运作方式略有不同。此时：1. 等级将取脚本等级与现有建筑等级中的较大值 2. 现金储备将取脚本值与现有现金储备中的较大值 |  |
| create_mass_migration | 发起特定文化从来源国向当前 scope 的州的大规模迁移 | create_mass_migration = { origin = c:GBR culture = cu:english } |  |
| create_pop | 在当前 scope 的州中创建一个人口 |  |  |
| deactivate_building | 停用州中的一座建筑 | deactivate_building = { building = building_key } |  |
| force_resource_depletion | 强制触发州中的资源枯竭 | force_resource_depletion = bg_gold_mining |  |
| force_resource_discovery | 强制触发州中的资源发现 | force_resource_discovery = bg_gold_mining |  |
| kill_population_in_state | 杀死当前 scope 的州中人口的一定数量个体。 | 除 percent 外所有参数均为可选。pop type 与 strata 不能同时使用。 kill_population = { value = <integer value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } |  |
| kill_population_percent_in_state | 杀死当前 scope 的州中人口的某一百分比。 | 除 percent 外所有参数均为可选。pop type 与 strata 不能同时使用。 kill_population_percent = { percent = <decimal value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } |  |
| liberate_slaves | 解放国家/州中的所有奴隶 | liberate_slaves = yes |  |
| remove_building | 移除 scope 州中某建筑的所有等级 | remove_building = building_key |  |
| remove_modifier | 移除 scope 中对象的限时修正 effect | remove_modifier = static_modifier_name |  |
| remove_resource_potential | 从州区域的资源潜力中移除某建筑类型 | remove_resource_potential = building_iron_mine |  |
| reset_hub_names | 重置当前 scope 的州中所有枢纽的名称 | reset_hub_names = yes |  |
| reset_state_name | 重置当前 scope 的州的名称 | reset_state_name = yes |  |
| set_available_for_autonomous_investment | 将某建筑类型设为当前 scope 的州中可用于自主投资 | set_available_for_autonomous_investment = building type scope | building_type |
| set_devastation | 设置州区域或州的荒废度 |  |  |
| set_hub_name | 将当前 scope 的州中某枢纽的名称设为一个本地化字符串 | set_state_name = { type = city ( can be any hub type city/port/farm/mine/wood ) name = HUB_NAME_STATE_KIEV_city_ukrainian } |  |
| set_hub_names | 基于州区域名称、枢纽类型和指定后缀，将当前 scope 的州中所有枢纽的名称设为本地化字符串 | set_hub_names = ukrainian |  |
| set_state_name | 将当前 scope 的州的名称设为一个本地化字符串 | set_state_name = STATE_KIEV_ukrainian |  |
| set_state_owner | 设置州的所有者 | set_state_owner = scope | country |
| set_state_type | 将州设为特定类型（已合并、未合并、条约港） |  |  |
| start_building_construction | 在当前 scope 的州中以政府建设的形式开始建造一座建筑 | start_building_construction = building_barracks |  |
| start_privately_funded_building_construction | 在当前 scope 的州中以私人建设的形式开始建造一座建筑 | start_privately_funded_building_construction = building_barracks |  |
| unset_available_for_autonomous_investment | 将某建筑类型设为当前 scope 的州中不可用于自主投资 | unset_available_for_autonomous_investment = building type scope | building_type |

### 州区域 scope（State region scope）

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_arable_land | 增加/移除州区域的可耕地 |  |  |
| add_claim | 将 scope 中的州区域添加为目标国家的宣称 | add_claim = scope/country | country |
| add_devastation | 增加/移除州区域的荒废度 |  |  |
| add_homeland | 将 scope 中的州区域添加为目标文化的本土 | add_homeland = cu:culture | culture |
| add_pollution | 提高/降低当前 scope 的州区域的污染水平 | add_pollution = 10 |  |
| add_state_trait | 在当前 scope 的州区域中添加州特质 | add_state_trait = <state_trait_name> |  |
| create_state | 在州区域中创建一个州 |  |  |
| finish_harvest_condition | 结束当前 scope 的州区域中指定类型的收成状况 | finish_harvest_condition = <key> |  |
| remove_claim | 移除目标国家对 scope 中州区域的宣称 | add_claim = scope/country | country |
| remove_homeland | 移除目标文化在 scope 中州区域的本土地位 | remove_homeland = cu:culture | culture |
| remove_resource_potential | 从州区域的资源潜力中移除某建筑类型 | remove_resource_potential = building_iron_mine |  |
| remove_state_trait | 移除当前 scope 的州区域中的州特质 | remove_state_trait = <state_trait_name> |  |
| set_devastation | 设置州区域或州的荒废度 |  |  |
| set_owner_of_provinces | 将州区域中的一组省份给予特定国家 | set_owner_of_provinces = { country = <scope> provinces = { <province list> } } |  |
| start_harvest_condition | 在当前 scope 的州区域中开始指定类型的收成状况（若已存在则刷新） | start_harvest_condition = <key> |  |
| start_harvest_condition_with_params | 在当前 scope 的州区域中开始指定类型的收成状况，可选提供强度和持续时间（以天计） | start_harvest_condition_with_params = { type = flood intensity = 5 (optional) duration = 5 (optional) } |  |

## 全部 effect（All effects）

使用此表搜索所有 effect。

| Effect | 描述 | 示例 | Scope | 目标 |
|---|---|---|---|---|
| abandon_revolution | 将利益集团从革命中移除 | abandon_revolution = yes/no | interest_group |  |
| activate_building | 激活州中的一座建筑 | activate_building = { building = building_key } | state |  |
| activate_law | 为国家激活一项法律，不应用 `when_enacted` effect | activate_law = law_type:<law_key> | country | law_type |
| activate_production_method | 为国家/州中某一类型的建筑激活指定名称的生产方式 | activate_production_method = { building_type = building_key production_method = production_method_key } | country, state |  |
| add_acceptance | 为州中的一种文化增加接受度增量 | add_acceptance = { culture = cu:romanian value = -10 } | state |  |
| add_amendment | 为 scope 中的法律添加一项修正案。 | add_amendment = { type = amendment_example sponsor = interest_group cooldown = 120 # months timeout = 240 # months (optional, 0 = none) } | law |  |
| add_arable_land | 增加/移除州区域的可耕地 |  | state_region |  |
| add_banned_goods | 为国家添加对某种商品的全面禁令 | add_banned_goods = <goods key/scope> | country | goods |
| add_career_length | 增加人物当前某一职务的任期长度。职务可以是特定的数据库职务或职务类型（例如 general）。若未指定职务，则应用于所有有任期结束日期的职务。 | add_career_length = { role = role_key/role_type days/months/years = 5 random_range = { 0.8 1.2 } } | character |  |
| add_change_relations_progress | 增加两国关系变更的进度 | add_change_relations_progress = { country = country scope/tag value = amount } | country |  |
| add_character_ideology | 向 scope 中的政治运动的人物意识形态列表添加一项人物意识形态 | add_character_ideology = ideology:<ideology key> | political_movement |  |
| add_character_role | 为人物添加一个新职务，可用于原型或数据库职务 | add_character_role = general/character_role_general | character |  |
| add_civil_war_progress | 为内战进度增加指定数量的百分点（范围为 [0, 1]，0.1 表示 10 个百分点） | add_civil_war_progress = 0.1 / -0.1 | civil_war |  |
| add_claim | 将 scope 中的州区域添加为目标国家的宣称 | add_claim = scope/country | state_region | country |
| add_cohesion_number | 为 scope 中的强权集团增加特定数量的凝聚力 | add_cohesion_number = 100 (adds 100 points to Cohesion) | power_bloc |  |
| add_cohesion_percent | 为 scope 中的强权集团增加基于百分比的凝聚力 | add_cohesion_percent = -0.2 (reduces Cohesion by 20% of its maximum value) | power_bloc |  |
| add_commander_rank | 将人物晋升/降级指定数量的军衔等级 | add_commander_rank = integer | character |  |
| add_company | 将公司类型添加到国家的公司中 | add_company = company_type:key | country | company_type |
| add_company_monopoly | 为公司 scope 添加一项垄断 | add_company_monopoly = bt:building_textile_mills | company | building_type |
| add_contextless_journal_entry | 激活指定类型的无上下文日志条目 | add_contextless_journal_entry = <key> | none |  |
| add_country_monopoly | 为国家 scope 添加一项垄断 | add_country_monopoly = bt:building_textile_mills | country | building_type |
| add_cultural_community | 在当前 scope 的州中为目标文化添加一个文化社区。 | scope:some_state = { add_cultural_community = cu:zulu } | state | culture |
| add_cultural_community_in_state | 在目标州中为 scope 中的文化添加一个文化社区。 | cu:zulu = { add_cultural_community_in_state = scope:some_state } | culture | state |
| add_cultural_obsession | 为 scope 中的文化添加一项新的痴迷 | add_cultural_obsession = <goods> | culture |  |
| add_cultural_taboo | 为 scope 中的文化添加一项新的禁忌 | add_cultural_taboo = <goods> | culture |  |
| add_culture_acceptance_modifier | 在当前 scope 的国家中为给定文化应用一个文化接受度修正。除必需的 culture 参数外，此 effect 的语法与 add_modifier 相同。 | add_culture_acceptance_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } | country |  |
| add_culture_standard_of_living_modifier | 在当前 scope 的州中为给定文化应用一个生活水平修正。除必需的 culture 参数外，此 effect 的语法与 add_modifier 相同。 | add_culture_standard_of_living_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } | state |  |
| add_devastation | 增加/移除州区域的荒废度 |  | state_region |  |
| add_diplomatic_play_war_support | 为当前 scope 的外交博弈中的目标国家增加战争支持度。该数值将显示在提示的“局势”标题下 | add_diplomatic_play_war_support = { target = country value = value } | diplomatic_play |  |
| add_electoral_confidence | 为 scope 国家增加 x% 的选举信心 | add_electoral_confidence = 0.1 / -0.1 | country |  |
| add_enactment_modifier | 为 scope 中的对象添加一个与立法相关的限时修正 effect | add_enactment_modifier = { name = modifier_key } | country |  |
| add_enactment_phase | 按增量改变 scope 国家当前的立法阶段。结果将被限制在 0 到 NPolitics::LAW_ENACTMENT_MAX_PHASES 之间。若结果等于 NPolitics::LAW_ENACTMENT_MAX_PHASES，正在立法的法律将获得通过。 |  | country |  |
| add_enactment_setback | 按增量改变 scope 国家当前的立法受挫次数。结果将被限制在 0 到 country_law_max_setbacks_add 之间。若结果等于 country_law_max_setbacks_add，立法将失败 |  | country |  |
| add_era_researched | 在国家 scope 中将指定时代标记为已研究 | add_era_researched = era | country |  |
| add_escalation | 为外交博弈增加紧张度 | add_escalation = integer | diplomatic_play |  |
| add_experience | 为指挥官增加一定数量的经验 | add_experience = 0.2 | character |  |
| add_exports | 为 scope 中的州商品增加出口倍率 | add_exports = 3 | state_goods |  |
| add_fervor | 为 scope 中的文化增加热忱 | add_fervor = 2.6 | culture |  |
| add_fervor_target_modifier | 在当前 scope 的国家中为给定文化应用一个热忱目标修正。除必需的 culture 参数外，此 effect 的语法与 add_modifier 相同。 | add_fervor_target_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } | country |  |
| add_homeland | 将 scope 中的州区域添加为目标文化的本土 | add_homeland = cu:culture | state_region | culture |
| add_ideology | 为 scope 中的利益集团添加一项意识形态 | add_ideology = ideology:<ideology key> | interest_group |  |
| add_ig_to_party | 将目标利益集团添加到 scope 中的政党 | py:py_key = { add_ig_to_party = ig:ig_key } | party | interest_group |
| add_imports | 为 scope 中的州商品增加进口倍率 | add_imports = 3 | state_goods |  |
| add_initiator_backers | 将一个 tag/scope 国家添加到外交博弈的发起方 | add_initiator_backers = { list of scopes/tags } | diplomatic_play |  |
| add_investment_pool | 直接向投资池注入资金 | add_investment_pool = 50 | country |  |
| add_involved_country | 使目标国家成为 scope 中的日志条目的相关国家 | add_involved_country = c:FRA | journal_entry | country |
| add_involvement | 为 scope 国家在给定战略区域中增加介入度 | add_involvement = { strategic_region = sr:poland value = 10 } | country |  |
| add_journal_entry | 向 scope 国家的日志添加一条日志条目，可选保存 scope 目标 | add_journal_entry = { type = <key> target = <scope> } | country |  |
| add_law_progress | 为正在通过的法律的当前检查点增加 x% 进度（范围为 [0, 1]，0.1 表示 10 个百分点） | add_law_progress = 0.1 / -0.1 | country |  |
| add_leverage | 为 scope 中的强权集团增加对指定国家的特定数量的杠杆 | 若数值为正，还会按比例减少所有其他集团的杠杆以匹配 add_leverage = { target = country_scope value = script_value } | power_bloc |  |
| add_liberty_desire | 为附属国增加独立倾向。若 scope 国家不是外交条约中的附属国，则不做任何事。 | add_liberty_desire = -5 | country |  |
| add_lobby_member | 将一个利益集团添加为 scope 政治游说团体的成员 | add_lobby_member = scope:interest_group | political_lobby | interest_group |
| add_loyalists | 为当前 scope 的国家中的人口添加忠诚派。除 value 外所有参数均为可选。 | value 是每个人口中向忠诚主义转变的百分比。如果指定了 interest_group，则人口根据其利益集团归属获得忠诚派。pop type 与 strata 互斥。 add_radicals = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } | country |  |
| add_loyalists_in_state | 为当前 scope 的州中的人口添加忠诚派。除 value 外所有参数均为可选。 | value 是每个人口中向忠诚主义转变的百分比。如果指定了 interest_group，则人口根据其利益集团归属获得忠诚派。pop type 与 strata 互斥。 add_radicals_in_state = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } | state |  |
| add_modifier | 为 scope 中的对象添加一个限时修正 effect | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay | building, character, country, institution, interest_group, journal_entry, political_movement, power_bloc, state |  |
| add_momentum | 在竞选期间为政党增加势头 | add_momentum = value | party |  |
| add_morale | 为 scope 中的作战单位增加特定数量的士气 | add_morale = -0.2 | new_combat_unit |  |
| add_organization | 为 scope 中的军事编队增加特定数量的组织度 | add_organization = -10 | military_formation |  |
| add_owned_country | 将 scope 中的公司设为目标国家的创始公司 | set_founding_company = country:key | company | country |
| add_pollution | 提高/降低当前 scope 的州区域的污染水平 | add_pollution = 10 | state_region |  |
| add_pop_wealth | 增加人口的财富 | add_pop_wealth = { wealth_distribution = { script_value } update_loyalties = yes/no } | pop |  |
| add_primary_culture | 将一种文化添加为国家的主要文化 | add_primary_culture = <culture> | country | culture |
| add_principle | 为强权集团添加原则 | power_bloc = { add_principle = test_principle_group_A_1 } | power_bloc |  |
| add_progress | 为日志条目的进度条增加进度 | add_progress = { value = -5 name = example_progress_bar_name } | journal_entry |  |
| add_radicals | 为当前 scope 的国家中的人口添加激进派。除 value 外所有参数均为可选。 | value 是每个人口中向激进主义转变的百分比。如果指定了 interest_group，则人口根据其利益集团归属获得激进派。pop type 与 strata 互斥。 add_radicals = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } | country |  |
| add_radicals_in_state | 向 scope 州的人口添加激进派。除 value 外所有参数均为可选。 | value 是每个人口中转向激进化的比例。若指定了 interest_group，则人口根据其利益集团成员身份获得激进派。pop_type 与 strata 互斥。add_radicals_in_state = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } | state |  |
| add_random_trait | 添加一个指定类别的随机合格特质（Trait） | add_random_trait = personality / skill / condition | character |  |
| add_religion_standard_of_living_modifier | 在 scope 州为指定宗教应用一个生活水平修正。除必需的 religion 参数外，此 effect 的语法与 add_modifier 相同。 | add_religion_standard_of_living_modifier = { religion = religion_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } | state |  |
| add_resource_potential | 将一种建筑类型作为资源潜力添加到一个州区域 | add_resource_potential = building_iron_mine | state, state_region |  |
| add_ruling_interest_group | 将利益集团加入政府 | add_ruling_interest_group = yes/no | interest_group |  |
| add_state_trait | 在 scope 州区域添加州特质 | add_state_trait = <state_trait_name> | state_region |  |
| add_supply_ships | 向 scope 国家添加若干补给舰 | add_supply_ships = 10 | country |  |
| add_target_backers | 将一个 tag/scope 国家添加到外交博弈的目标方 | add_target_backers = { list of scopes/tags } | diplomatic_play |  |
| add_taxed_goods | 对一个国家的一种商品征收消费税 | add_taxed_goods = <goods key/scope> | country | goods |
| add_technology_progress | 添加技术进度 | add_technology_progress = { progress = <script_value> technology = <technology key> } | country |  |
| add_technology_researched | 在 country scope 中研究指定技术 | add_technology_researched = technology | country |  |
| add_to_global_variable_list | 将 event target 添加到全局变量列表中，持续指定时长 | add_to_global_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| add_to_global_variable_map | 将 event target 添加到全局变量映射中，持续指定时长；无法更新已有键的值 | add_to_global_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| add_to_list | 将当前 scope 添加到任意命名的列表中（若列表尚不存在则创建），以便在（未中断的）事件链中稍后引用 | scope = { add_to_list = <name_of_list> } add_to_list = { name = <name_of_list> value = <script_value> } 注意，若将永久目标添加到临时列表，整个列表会变为永久 | none |  |
| add_to_local_variable_list | 将 event target 添加到局部变量列表中，持续指定时长 | add_to_local_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| add_to_local_variable_map | 将 event target 添加到局部变量映射中，持续指定时长；无法更新已有键的值 | add_to_local_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| add_to_temporary_list | 将当前 scope 添加到任意命名的列表中（若列表尚不存在则创建），以便在同一 effect 中稍后引用 | add_to_temporary_list = <name_of_list> add_to_temporary_list = { name = <name_of_list> value = <script_value> } 注意，若将临时目标添加到永久列表，列表仍将保持永久 | none |  |
| add_to_variable_list | 将 event target 添加到变量列表中，持续指定时长 | add_to_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| add_to_variable_map | 将 event target 添加到变量映射中，持续指定时长；无法更新已有键的值 | add_to_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| add_tradition_trait | 向 scope 文化添加一个新的传统特质 | add_tradition_trait = <tradition_trait> | culture |  |
| add_trait | 为一个人物添加特质 | add_trait = trait | character |  |
| add_treasury | 向一个国家添加/扣除资金 | add_treasury = fixed point | country |  |
| add_war_exhaustion | 向 scope 战争中的目标国家添加厌战度。其数值将显示在提示中的“局势”标题下 | add_war_exhaustion = { target = country value = value } | war |  |
| add_war_goal | 向一个外交博弈添加战争目标。 | add_war_goal = { holder = country scope/tag war_goal = <war goal key> target_state = <state scope> (if required) target_country = <country scope> (if required) target_region = <region scope> (if required) primary_demand = yes (optional) } | diplomatic_play |  |
| add_war_war_support | 向 scope 战争中的目标国家添加战争支持度。其数值将显示在提示中的“局势”标题下 | add_war_war_support = { target = country value = value } | war |  |
| annex | 吞并一个国家 | annex = scope | country | country |
| annex_as_civil_war | 吞并一个国家，并附带内战中获胜一方的全部继承效果 | annex_as_civil_war = scope | country | country |
| annex_with_incorporation | 吞并一个国家，并继承其各州的建制地位 | annex_with_incorporation = scope | country | country |
| assert_if | 有条件地在运行时触发一个断言 | assert_if = { limit = { <triggers> } text = <string> (optional) } | none |  |
| assert_read | 有条件地在读取时触发一个断言 | assert_read = yes / <string> | none |  |
| call_election | 将国家的下一次选举日期设定为 N 个月后 | call_election = { months = 6 } | country |  |
| cancel_enactment | 停止该国当前正在颁布的法律 | cancel_enactment = yes | country |  |
| cancel_imposition | 取消 scope 中该法律（而非法律类型）的强制推行 | scope:country.imposed_law = { cancel_imposition = yes } | none |  |
| cede_treaty_port | 将 scope 州的一个条约港割让给目标国家 | cede_treaty_port = scope/country | state | country |
| change_appeasement | 更改 scope 政治游说团的绥靖程度 | change_appeasement = { amount = 1 factor = trade_agreement_formed } | political_lobby |  |
| change_character_culture | 更改 scope 人物的文化 | change_character_culture = cu:colombian | character | culture |
| change_character_religion | 更改 scope 人物的宗教 | change_character_religion = rel:protestant | character | religion |
| change_global_variable | 更改一个数值型全局变量的值 | change_global_variable = { name = <global variable> <operation type> = <value> } 有效操作有 add、subtract、multiply、divide、modulo、min 和 max | none |  |
| change_infamy | 更改 scope 国家的恶名 | change_infamy = amount | country |  |
| change_institution_investment_level | 添加/扣除机构的投资等级 | change_institution_investment_level = { institution = institution_police investment = -1 } | country |  |
| change_local_variable | 更改一个数值型局部变量的值 | change_local_variable = { name = <local variable> <operation type> = <value> } 有效操作有 add、subtract、multiply、divide、modulo、min 和 max | none |  |
| change_pop_culture | 按 specified 百分比将 scope 人口的文化更改为指定文化 | change_pop_culture = { target = cu:spanish value = 0.33 } | pop |  |
| change_pop_religion | 按指定百分比将 scope 人口的宗教更改为指定宗教 | change_pop_religion = { target = rel:catholic value = 0.5 } | pop |  |
| change_poptype | 将人口的类型更改为给定类型 |  | pop | pop_type |
| change_relations | 更改两个国家之间的关系 | change_relations = { country = country scope/tag value = amount } | country |  |
| change_resource_potential | 更改一个州区域中某种资源的潜在最大建筑数量。仅对受资源限制的建筑类型有效。 | change_resource_potential = { type = building_iron_mine amount = 5 } | state, state_region |  |
| change_subject_type | 更改 scope 国家的附属国类型，同时保留当前的独立倾向数值。 | change_subject_type = subject_type_dominion | country |  |
| change_tag | 更改 scope 国家的 tag | c:GBR = { change_tag = FRA } | country |  |
| change_tension | 更改两个国家之间的紧张度 | change_tension = { country = country scope/tag value = amount } | country |  |
| change_variable | 更改一个数值型变量的值 | change_variable = { name = <variable name> <operation type> = <value> } 有效操作有 add、subtract、multiply、divide、modulo、min 和 max | none |  |
| clamp_global_variable | 将全局变量限制在指定的最大值和最小值之间 | clamp_global_variable = { name = <global variable> max = <value> min = <value> } | none |  |
| clamp_local_variable | 将局部变量限制在指定的最大值和最小值之间 | clamp_local_variable = { name = <local variable> max = <value> min = <value> } | none |  |
| clamp_variable | 将变量限制在指定的最大值和最小值之间 | clamp_variable = { name = <variable name> max = <value> min = <value> } | none |  |
| clear_debt | 清除国家贷款 = bool |  | country |  |
| clear_enactment_modifier | 清除 scope 国家当前所有的法律颁布修正。 |  | country |  |
| clear_global_variable_list | 清空列表 | clear_global_variable_list = variable_name | none |  |
| clear_global_variable_map | 清空映射 | clear_global_variable_map = variable_name | none |  |
| clear_local_variable_list | 清空列表 | clear_local_variable_list = variable_name | none |  |
| clear_local_variable_map | 清空映射 | clear_local_variable_map = variable_name | none |  |
| clear_ownership_transfer_fleet | 清除 scope 国家的所有权转移舰队，应在一系列 set_ship_owner_multiple 之后执行 | clear_ownership_transfer_fleet = yes | country |  |
| clear_saved_scope | 从顶层 scope 中清除一个已保存的 scope | save_scope_as = cool_scope -> clear_saved_scope = cool_scope | none |  |
| clear_scaled_debt | 清除相当于目标最大信贷额度乘以指定乘数的债务量 | clear_scaled_debt = value | country |  |
| clear_variable_list | 清空列表 | clear_variable_list = variable_name | none |  |
| clear_variable_map | 清空映射 | clear_variable_map = variable_name | none |  |
| complete_objective_subgoal | 完成一个目标子目标 | complete_objective_subgoal = <key> | country |  |
| convert_population | 将 X% 的异宗教人口更改为指定宗教。 | convert_population = { target = rel:catholic value = 0.5 } | state |  |
| copy_laws | 复制目标国家 scope 的宪法 | 警告：这会中止任何当前正在进行的颁布。copy_laws = scope | country | country |
| create_bidirectional_truce | 在两个国家之间创建双向休战 | create_bidirectional_truce = { country = country scope/tag months = integer } | country |  |
| create_building | 在 scope 州创建一个建筑。支持的值有： | building = <building> activate_production_methods = { <production_methods> } subsidized = yes/no reserves = [0..1] (percentage of cash reserves the building should be created with) add_ownership = { (mutually exclusive with level) country = { (give ownership levels to a specific country) country = s:GBR (country script target) levels = 5 } country = { (give ownership levels to a specific building) type = building_financial_district (building type that will get ownership levels, should be self or other ownership type) region = STATE_SINAI (region where owning building is placed) country = s:GBR (country script target for a region) levels = 3 } } level = arable_land/integer(mutually exclusive with add_ownership) 若 level 为 arable_land，建筑的等级将达到足以用尽该州全部可用耕地的等级。若 level 为整数，建筑将为该等级 请注意：若该州已存在指定类型的建筑，此 effect 的工作方式略有不同。此时：1. 等级将取脚本等级与现有建筑等级中的较大值 2. 现金储备将取脚本值与现有现金储备中的较大值 | state |  |
| create_character | 创建一个人物，任何选项均可省略。 | create_character = { name = loc_key or alternatively first_name and last_name separately culture = culture_tag religion = religion scope (if omitted, it's defined by the character's culture religion) female = bool or character scope (gets the same value from the character) noble = bool or character scope (gets the same value from the character) ruler = bool heir = bool historical = bool age = integer, range, or character scope (gets the age from a character) ideology = ideology key or scope interest_group = interest group key or scope template = base template to generate the character from on_created = effect save_scope_as = scope name trait_generation = effect hq = HQ scope or strategic region scope } | country |  |
| create_country | 创建一个新国家 | create_country = { tag = TAG # optional, if not specified origin's tag will be used origin = country # optional, newly created country will inherit certain values from the origin country # at least one of tag or origin must be supplied state = state # can be repeated; at least one state or province must be supplied province = province # can be repeated; at least one state or province must be supplied # both states and provinces can be supplied at the same time on_created = effect # optional effect that will be run with the newly created country in scope } | none |  |
| create_diplomatic_catalyst | 创建一个新的外交催化剂 | create_diplomatic_catalyst = { type = catalyst_relations_level_increased arget = <country scope> } | country |  |
| create_diplomatic_pact | 在两个国家之间创建一个外交协议，scope 国家为发起方 | create_diplomatic_pact = { country = country scope/tag first_state = state scope/tag second_state = state scope/tag type = diplomatic action type } | country |  |
| create_diplomatic_play | 以 scope 对象为发起方创建一个外交博弈。add_initiator_backers、add_target_backers 和 add_war_goal 可作为直接 effect 包含在内 | create_diplomatic_play = { name = loc_key escalation = integer between 0 and 100 target_country = country scope/tag type = diplomatic play type annex_as_civil_war = yes/no add_initiator_backers = { list of country scopes/tags } add_target_backers = { list of country scopes/tags } add_war_goal = { holder = country scope/tag war_goal = <war goal key> target_state = <state scope> (if required) target_country = <country scope> (if required) target_region = <region scope> (if required) } } | country |  |
| create_dynamic_country | 创建一个带动态 tag 的新国家 | create_dynamic_country = { origin = country # optional, newly created country may inherit certain values from the origin country country_type = country type # optional if origin is set, may be repeated, will try to inherit country type from origin if not specified tier = country tier # optional if origin is set, may be repeated, will try to inherit country tier from origin if not specified culture = culture # optional if origin is set, may be repeated, will try to inherit cultures from origin if not specified religion = religion # optional if origin is set, if no religion is specified, will try to inherit religion from origin if not specified capital = state # optional if states have been supplied, will try to set a capital from supplied states if not specified social_hierarchy = social hierarchy key # optional; if not specified: same as origin's if origin is set, default hierarchy otherwise cede_state_trigger = trigger # if this trigger is set, each state in the world for which it evaluates true will be ceded to the new country color = rgb # optional, will try to inherit map color from origin if not specified primary_unit_color = rgb # optional, will try to inherit unit color from origin if not specified secondary_unit_color = rgb # optional, will try to inherit unit color from origin if not specified tertiary_unit_color = rgb # optional, will try to inherit unit color from origin if not specified on_created = effect # optional effect that will be run with the newly created country in scope } | none |  |
| create_incident | 创建一个产生恶名的外交事件，目标国家为受害方 | create_incident = { country = country scope/tag value = infamy amount } | country |  |
| create_mass_migration | 发起一个特定文化从来源国向 scope 州的大规模迁移 | create_mass_migration = { origin = c:GBR culture = cu:english } | state |  |
| create_military_formation | 创建一个军事编队 | create_military_formation = { # Optional name name = name # type defaults to army type = army/fleet hq_region = sr:region_russia # Optional, overrides the automatic supply hub selection supply_hub = s:STATE_MOSCOW # Add as many combat_unit specifications as necessary combat_unit = { type = unit_type:combat_unit_type_irregular_infantry # service_type defaults to regular and conscript is not applicable for fleets service_type = regular/conscript state_region = s:STATE_MOSCOW count = 5 } # mobilization_options are not applicable for fleets mobilization_options = { mobilization_option:mobilization_option_basic_supplies mobilization_option:mobilization_option_truck_transport } } | country |  |
| create_political_lobby | 创建一个新的政治游说团 | create_political_lobby = { type = lobby_pro_country arget = <country scope> add_interest_group = <ig scope 1> add_interest_group = <ig scope 2> add_interest_group = <ig scope 3> } | country |  |
| create_political_movement | 在该国创建一个指定类型的政治运动，culture/religion 为可选 | create_political_movement = { movement_type = x religion = <scope> (if relevant) culture = <scope> (if relevant) } | country |  |
| create_pop | 在 scope 州创建一个人口 |  | state |  |
| create_power_bloc | 创建一个以 scope 对象为首领的强权集团 | create_power_bloc = { name = loc_key map_color = { R G B } or hsv{ H S V } founding_date = yyyy.mm.dd, optional identity = power bloc identity key principle = power bloc principle key, can be repeated member = country scope, can be repeated } | country |  |
| create_ship | 在 scope 国家创建一艘舰船 | create_ship = { type = ship_type:key # Type of ship to create fleet = scope:fleet # Fleet to assign the created ship to save_scope_as = scope_name # If specified, saves the created ship in the given scope name name = loc_key # Optional name for the ship } | country |  |
| create_state | 在一个州区域中创建一个州 |  | state_region |  |
| create_treaty | 在国家之间创建一项条约 | create_treaty = { name = <loc key> # (default: empty) if specified, this treaty's name will be determined by the localization of the specified key first_country = <country> # (default: none) must _not_ be specified if the created treaty is an amendment second_country = <country> # (default: none) must _not_ be specified if the created treaty is an amendment amends = <treaty> # (default: none) if specified, the created treaty will be an amendment to the specified treaty is_draft = yes \| no # (default: yes) must be yes if this treaty is an amendement to an existing treaty entered_into_force_on = <date> # (default: none) means today = true if not specified (for non-drafts). Must _not_ be specified for drafts. Cannot be in the future binding_period = { # (default: 0) must be a nonnegative number, fractional parts will be ignored (truncation) days = <nonnegative number> \| weeks = <nonnegative number> \| months = <nonnegative number> \| years = <nonnegative number> } articles_to_create = { # (default: empty) non-amendments must have at least one article to create { article = <key> # (default: empty) the type of article (determined by script) source_country = <country> # (default: none) directed articles _must_ specify this value, mutual articles _must not_ specify this value target_country = <country> # (default: none) directed articles _must_ specify this value, mutual articles _must not_ specify this value inputs = { # (default: empty) list of inputs values as required by the article { quantity = <positive number> \| goods = <goods> \| state = <state> \| strategic_region = <strategic region> \| company = <company> \| building_type = <building_type> \| law_type = <law_type> \| country = <country> } { ... } # one input per required input of the corresponding article type } } # some examples of valid articles { article = alliance } # mutual, no inputs { article = goods_transfer # directed source_country = c:FRA # because directed target_country = c:GBR # because directed inputs = { { quantity = 250 } # because goods_transfer has required_inputs = { quantity goods } { goods = g:coal } # because goods_transfer has required_inputs = { quantity goods } } } } } | none |  |
| create_unidirectional_truce | 为一个国家针对另一个国家创建单向休战 | create_unidirectional_truce = { country = country scope/tag months = integer } | country |  |
| custom_description | 包装 effect，使其获得自定义描述而非自动生成的描述 | custom_description = { text = <effect_localization_key> subject = <optional subject scope> #defaults to current scope object = <optional object scope> value = <optional script value> ... effects ... } | none |  |
| custom_description_no_bullet | 包装 effect，使其获得自定义描述而非自动生成的描述。同时确保不显示项目符号 | custom_description_no_bullet = { text = <effect_localization_key> subject = <optional subject scope> #defaults to current scope object = <optional object scope> value = <optional script value> ... effects ... } | none |  |
| custom_label | 仅作提示文本之用，scope 作为对象（用于分组、本地化）。 | custom_label = key 或者 custom_label = { text = key subject = scope (optional) <hidden effects> } | none |  |
| custom_label_no_bullet | 仅作提示文本之用，scope 作为对象（用于分组、本地化）。不显示项目符号。 | custom_label_no_bullet = key 或者 custom_label_no_bullet = { text = key subject = scope (optional) <hidden effects> } | none |  |
| custom_tooltip | 仅作提示文本之用，scope 作为主语（用于分组、本地化）。 | custom_tooltip = key 或者 custom_tooltip = { text = key subject = scope (optional) <hidden effects> } | none |  |
| custom_tooltip_no_bullet | 仅作提示文本之用，scope 作为主语（用于分组、本地化）。不显示项目符号。 | custom_tooltip_no_bullet = key 或者 custom_tooltip_no_bullet = { text = key subject = scope (optional) <hidden effects> } | none |  |
| damage_ship_hull | 按给定数值损伤一艘船只的船体 | damage_ship_hull = 20 | ship |  |
| damage_ship_hull_percent | 按其总生命值的给定百分比损伤一艘船只的船体 | damage_ship_hull_percent = 0.2 | ship |  |
| deactivate_building | 停用一个州中的建筑 | deactivate_building = { building = building_key } | state |  |
| deactivate_law | 为一个国家停用某项法律 |  | country | law_type |
| deactivate_parties | 停用 scope 国家的政党。 | deactivate_parties = yes | country |  |
| debug_log | 在此 effect 执行时向调试日志记录一条字符串 | debug_log = message 该消息可以是一个 localization 字符串，其中可使用 ROOT、SCOPE 和 PREV | none |  |
| debug_log_scopes | 在此 effect 执行时向调试日志记录当前 scope | debug_log_scopes = yes # 记录完整 scope 信息 debug_log_scopes = no # 仅记录当前 scope | none |  |
| decrease_autonomy | 将一个国家的附属国类型改为自治程度更低的一种 | decrease_autonomy = yes | country |  |
| deploy_to_front | 将 scope 编队部署到目标前线 | deploy_to_front = p:xFAFAFA.front 也可接受 base_camp 参数，将使用给定省份搜索最近的可连接大本营 deploy_to_front = { front = p:xFAFAFA.front base_camp = p:xFAFAFA = true, } | military_formation | front |
| disable_temporary_hostilities | 禁用两个国家之间给定类型的临时敌对状态 | disable_temporary_hostilities = { country = country scope/tag type = naval/war/limited_war } | country |  |
| disband_party | 将所有利益集团从该政党中移除，使其解散 | disband_party = yes | party |  |
| disband_political_lobby | 解散 scope 的政治游说团 | disband_political_lobby = yes | political_lobby |  |
| disinherit_character | 剥夺 scope 人物在其适用的所有国家中的继承人身份。 | scope:larry = { disinherit_character = yes } | character |  |
| else | 若前一个 'if' 或 'else_if' 的 limit 条件未满足，则执行其中包含的 effect | if = { limit = { <triggers> } <effects> } else = { <effects> } | none |  |
| else_if | 若前一个 'if' 或 'else_if' 的 limit 条件未满足且自身 limit 满足，则执行其中包含的 effect | if = { limit = { <triggers> } <effects> } else_if = { limit = { <triggers> } <effects> } | none |  |
| enable_temporary_hostilities | 启用两个国家之间给定类型的临时敌对状态 | enable_temporary_hostilities = { country = country scope/tag type = naval/war/limited_war } | country |  |
| end_national_awakening | 结束一场文化觉醒 | end_national_awakening = cu:british | country | culture |
| end_play | 结束一场外交博弈 | end_play = bool | diplomatic_play |  |
| end_truce | 结束两个国家之间的任何休战 | end_truce = country_scope | country | country |
| error_log | 在此 effect 执行时向错误日志记录一条字符串 | error_log = message 该消息可以是一个 localization 字符串，其中可使用 ROOT、SCOPE 和 PREV | none |  |
| every_active_law | 遍历一个国家中的所有现行法律 | every_active_law = { limit = { <triggers> } #可选 <effects> } | country | law |
| every_active_party | 遍历一个国家中的所有活跃政党 | every_active_party = { limit = { <triggers> } #可选 <effects> } | country | party |
| every_character | 遍历全球所有人物 | every_character = { limit = { <triggers> } #可选 <effects> } | none | character |
| every_character_in_exile_pool | 遍历流放池中的人物 | every_character_in_exile_pool = { limit = { <triggers> } #可选 <effects> } | none | character |
| every_character_in_void | 遍历虚空（void）中的人物 | every_character_in_void = { limit = { <triggers> } #可选 <effects> } | none | character |
| every_character_role | 遍历 scope 人物的所有角色 | every_character_role = { limit = { <triggers> } #可选 <effects> } | character | character_role |
| every_civil_war | 遍历与 scope 国家相关的所有内战 | every_civil_war = { limit = { <triggers> } #可选 <effects> } | country | civil_war |
| every_cobelligerent_in_diplo_play | 遍历 scope 国家在所有外交博弈（包括战争）中的所有共同交战国 | every_cobelligerent_in_diplo_play = { limit = { <triggers> } #可选 <effects> } | country | country |
| every_cobelligerent_in_war | 遍历 scope 国家在所有战争中的所有共同交战国 | every_cobelligerent_in_war = { limit = { <triggers> } #可选 <effects> } | country | country |
| every_combat_unit | 遍历输入 scope 的所有作战单位 | every_combat_unit = { limit = { <triggers> } #可选 <effects> } | battle, building, front, hq, military_formation | new_combat_unit |
| every_company | 遍历一个国家中的所有公司 | every_company = { limit = { <triggers> } #可选 <effects> } | country | company |
| every_country | 遍历全球所有国家 | every_country = { limit = { <triggers> } #可选 <effects> } | none | country |
| every_country_in_<georegion_short_name> | 遍历指定地理区域中的所有国家 | every_country_in_<georegion_short_name> = { limit = { <triggers> } #可选 <effects> } | none | country |
| every_country_strategic_region | 遍历包含 scope 国家所拥有州的所有战略区域 | every_country_strategic_region = { limit = { <triggers> } #可选 <effects> } | country | strategic_region |
| every_decentralized_country | 遍历所有非中央集权的国家 | every_decentralized_country = { limit = { <triggers> } #可选 <effects> } | none | country |
| every_diplomatic_catalyst | 遍历一个国家近期记忆中的所有外交催化剂 | every_diplomatic_catalyst = { limit = { <triggers> } #可选 <effects> } | country | diplomatic_catalyst |
| every_diplomatic_play | 遍历全球所有外交博弈 | every_diplomatic_play = { limit = { <triggers> } #可选 <effects> } | none | diplomatic_play |
| every_diplomatically_relevant_country | 遍历一个国家 scope 的所有外交相关国家 | every_diplomatically_relevant_country = { limit = { <triggers> } #可选 <effects> } | country | country |
| every_direct_subject | 层级中直接位于当前国家之下的任何国家 | every_direct_subject = { limit = { <triggers> } #可选 <effects> } | country | country |
| every_enemy_in_diplo_play | 遍历 scope 国家在所有外交博弈（包括战争）中的所有敌国 | every_enemy_in_diplo_play = { limit = { <triggers> } #可选 <effects> } | country | country |
| every_enemy_in_war | 遍历 scope 国家在所有战争中的所有敌国 | every_enemy_in_war = { limit = { <triggers> } #可选 <effects> } | country | country |
| every_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成状况 | every_harvest_condition = { limit = { <triggers> } #可选 <effects> } | country, state, state_region, strategic_region | harvest_condition |
| every_in_global_list | 遍历全局列表中的所有项目。 | every_in_global_list = { list = name 或 variable = name limit = { <triggers> }（可选）<effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| every_in_hierarchy | 当前层级中的任何国家，包括当前国家 | every_in_hierarchy = { limit = { <triggers> } #可选 <effects> } | country | country |
| every_in_list | 遍历列表中的所有项目。 | every_in_list = { list = name 或 variable = name limit = { <triggers> }（可选）<effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| every_in_local_list | 遍历本地列表中的所有项目。 | every_in_local_list = { list = name 或 variable = name limit = { <triggers> }（可选）<effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| every_influenced_interest_group | 遍历受一场政治运动影响的所有利益集团 | every_influenced_interest_group = { limit = { <triggers> } #可选 <effects> } | political_movement | interest_group |
| every_interest_group | 遍历一个国家中的所有利益集团 | every_interest_group = { limit = { <triggers> } #可选 <effects> } | country | interest_group |
| every_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | every_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_local_variable_map | 遍历本地变量映射中的所有键。 | every_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_variable_map | 遍历变量映射中的所有键。 | every_key_in_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_law | 遍历一个国家中的所有法律 | every_law = { limit = { <triggers> } #可选 <effects> } | country | law |
| every_lobby_member | 遍历一个游说团的所有利益集团成员 | every_lobby_member = { limit = { <triggers> } #可选 <effects> } | political_lobby | interest_group |
| every_market | 遍历全球所有市场 | every_market = { limit = { <triggers> } #可选 <effects> } | none | market |
| every_market_goods | 遍历一个市场中所有活跃的（市场）商品 | every_market_goods = { limit = { <triggers> } #可选 <effects> } | market | market_goods |
| every_member | 遍历一个政党的所有利益集团成员 | every_member = { limit = { <triggers> } #可选 <effects> } | party | interest_group |
| every_military_formation | 遍历输入 scope 当前存在的所有军事编队 | every_military_formation = { limit = { <triggers> } #可选 <effects> } | country, front, hq | military_formation |
| every_neighbouring_state | 遍历当前 scope 的所有邻接州 注意英式拼写 | every_neighbouring_state = { limit = { <triggers> } #可选 <effects> } | country, state, state_region, strategic_region | state |
| every_overlord_or_above | 层级中位于当前国家之上的任何国家 | every_overlord_or_above = { limit = { <triggers> } #可选 <effects> } | country | country |
| every_owned_country | 遍历 scope 公司拥有的所有国家 | every_owned_country = { limit = { <triggers> } #可选 <effects> } | company | country |
| every_participant | scope 中外交协定双方的任何参与者 | every_participant = { limit = { <triggers> } #可选 <effects> } | diplomatic_pact | country |
| every_political_lobby | 遍历一个国家或利益集团中的所有政治游说团 | every_political_lobby = { limit = { <triggers> } #可选 <effects> } | country, interest_group | political_lobby |
| every_political_movement | 遍历一个国家中的所有政治运动 | every_political_movement = { limit = { <triggers> } #可选 <effects> } | country | political_movement |
| every_possible_amendment_type | 遍历可添加到 scope 法律的修正案类型 | every_possible_amendment_type = { limit = { <triggers> } #可选 <effects> } | law | amendment_type |
| every_potential_party | 遍历一个国家中所有潜在的政党 | every_potential_party = { limit = { <triggers> } #可选 <effects> } | country | party |
| every_power_bloc | 遍历所有强权集团 | every_power_bloc = { limit = { <triggers> } #可选 <effects> } | none | power_bloc |
| every_power_bloc_member | 遍历 scope 强权集团的所有成员，包括领导者 | every_power_bloc_member = { limit = { <triggers> } #可选 <effects> } | power_bloc | country |
| every_preferred_law | 遍历利益集团所在国家的所有现行及可能法律，按其对法律的偏好程度排序 | every_preferred_law = { limit = { <triggers> } #可选 <effects> } | interest_group | law |
| every_primary_culture | scope 国家或国家定义的主流文化 | every_primary_culture = { limit = { <triggers> } #可选 <effects> } | country, country_definition | culture |
| every_province | 遍历 scope 州中的所有省份 | every_province = { limit = { <triggers> } #可选 <effects> } | province | state |
| every_province_in_<georegion_short_name> | 遍历指定地理区域中的所有省份 | every_province_in_<georegion_short_name> = { limit = { <triggers> } #可选 <effects> } | none | province |
| every_rival_country | 被 scope 国家视为竞争对手的任何国家 | every_rival_country = { limit = { <triggers> } #可选 <effects> } | country | country |
| every_rivaling_country | 视 scope 国家为竞争对手的任何国家 | every_rivaling_country = { limit = { <triggers> } #可选 <effects> } | country | country |
| every_scope_admiral | 遍历以下 scope 中的所有海军上将：国家、利益集团或军事编队 | every_scope_admiral = { limit = { <triggers> } #可选 <effects> } | country, front, interest_group, military_formation | character |
| every_scope_ally | 遍历一个国家的所有盟友 | every_scope_ally = { limit = { <triggers> } #可选 <effects> } | country | country |
| every_scope_amendment | 遍历 scope 法律的修正案 | every_scope_amendment = { limit = { <triggers> } #可选 <effects> } | law | amendment |
| every_scope_army | 遍历输入 scope 当前存在的所有陆军 | every_scope_army = { limit = { <triggers> } #可选 <effects> } | country, front, hq | military_formation |
| every_scope_article | 遍历 scope 条约的条款 | every_scope_article = { limit = { <triggers> } #可选 <effects> } | treaty | treaty_article |
| every_scope_article_option | 遍历 scope 条约或条约选项（treaty_options）的条款选项 | every_scope_article_option = { limit = { <triggers> } #可选 <effects> } | treaty, treaty_options | treaty_article_options |
| every_scope_building | 遍历以下 scope 中的所有建筑：州、国家 | every_scope_building = { limit = { <triggers> } #可选 <effects> } | country, state | building |
| every_scope_character | 遍历以下 scope 中的所有人物：国家、利益集团或前线 | every_scope_character = { limit = { <triggers> } #可选 <effects> } | country, front, interest_group, military_formation | character |
| every_scope_country | 遍历在受支持的 scope（目前为：market、state_region、strategic region）中有存在的所有国家 | every_scope_country = { limit = { <triggers> } #可选 <effects> } | market, state_region, strategic_region | country |
| every_scope_culture | 遍历 scope 中的所有文化 | every_scope_culture = { limit = { <triggers> } #可选 <effects> } | country, state | culture |
| every_scope_diplomatic_pact | scope 国家的任何外交协定 | every_scope_diplomatic_pact = { limit = { <triggers> } #可选 <effects> } | country | diplomatic_pact |
| every_scope_fleet | 遍历输入 scope 当前存在的所有舰队 | every_scope_fleet = { limit = { <triggers> } #可选 <effects> } | country, hq | military_formation |
| every_scope_front | 遍历与 scope 战争相关的所有前线 | every_scope_front = { limit = { <triggers> } #可选 <effects> } | war | front |
| every_scope_general | 遍历以下 scope 中的所有将军：国家、利益集团、前线或军事编队 | every_scope_general = { limit = { <triggers> } #可选 <effects> } | country, front, interest_group, military_formation | character |
| every_scope_held_interest_marker | 遍历一个国家持有的所有利益标记 | every_scope_held_interest_marker = { limit = { <triggers> } #可选 <effects> } | country | interest_marker |
| every_scope_homeland_state | 遍历作为 scope 文化的本土，或 scope 国家任一主流文化本土的所有州 | every_scope_homeland_state = { limit = { <triggers> } #可选 <effects> } | country, culture | state |
| every_scope_initiator_ally | 遍历外交博弈中发起方的所有盟友 | every_scope_initiator_ally = { limit = { <triggers> } #可选 <effects> } | diplomatic_play | country |
| every_scope_interest_marker | 遍历以下 scope 中的所有利益标记：国家、州区域、战略区域 | every_scope_interest_marker = { limit = { <triggers> } #可选 <effects> } | country, state_region, strategic_region | interest_marker |
| every_scope_je_involved | 遍历一个日志条目的所有相关方 | every_scope_je_involved = { limit = { <triggers> } #可选 <effects> } | journal_entry | country |
| every_scope_play_involved | 遍历一场外交博弈的所有相关方 | every_scope_play_involved = { limit = { <triggers> } #可选 <effects> } | diplomatic_play | country |
| every_scope_politician | 遍历以下 scope 中的所有政治家：国家或利益集团 | every_scope_politician = { limit = { <triggers> } #可选 <effects> } | country, front, interest_group, military_formation | character |
| every_scope_pop | 遍历以下 scope 中的所有人口：国家、州、利益集团、文化 | every_scope_pop = { limit = { <triggers> } #可选 <effects> } | country, culture, interest_group, state | pop |
| every_scope_regional_hqs | 遍历 scope 公司的区域总部 | every_scope_regional_hqs = { limit = { <triggers> } #可选 <effects> } | company | building |
| every_scope_ship | 遍历一个国家或军事编队中的所有船只 | every_scope_ship = { limit = { <triggers> } #可选 <effects> } | country, military_formation | ship |
| every_scope_state | 遍历以下 scope 中包含省份在内的所有州：国家、州区域、战区、前线或海峡 | every_scope_state = { limit = { <triggers> } #可选 <effects> } | country, front, state_region, strait, strategic_region, theater | state |
| every_scope_strait | 遍历在 scope 州或国家拥有陆地端点的所有海峡 | every_scope_strait = { limit = { <triggers> } #可选 <effects> } | country, state | strait |
| every_scope_target_ally | 遍历外交博弈中目标方的所有盟友 | every_scope_target_ally = { limit = { <triggers> } #可选 <effects> } | diplomatic_play | country |
| every_scope_theater | 遍历一个国家中的所有战区 | every_scope_theater = { limit = { <triggers> } #可选 <effects> } | country | theater |
| every_scope_treaty | 遍历约束 scope 国家的所有生效条约 | every_scope_treaty = { limit = { <triggers> } #可选 <effects> } | country | treaty |
| every_scope_violate_sovereignty_interested_parties | 遍历在 scope 国家的主权被侵犯时会产生关切的所有国家 | every_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #可选 <effects> } | country | country |
| every_scope_violate_sovereignty_wars | 遍历目标国家主权被 scope 国家侵犯时会爆发的所有相关战争 | every_scope_violate_sovereignty_wars = { limit = { <triggers> } #可选 <effects> } | country | war |
| every_scope_war | 遍历与 scope 相关的所有战争 | every_scope_war = { limit = { <triggers> } #可选 <effects> } | country | war |
| every_sea_node_adjacent_state | 遍历与一个州共享海域节点的所有州 | every_sea_node_adjacent_state = { limit = { <triggers> } #可选 <effects> } | state | state |
| every_state | 遍历全球所有州 | every_state = { limit = { <triggers> } #可选 <effects> } | none | state |
| every_state_in_<georegion_short_name> | 遍历指定地理区域中的所有州 | every_state_in_<georegion_short_name> = { limit = { <triggers> } #可选 <effects> } | none | state |
| every_state_region | 遍历所有州区域 | every_state_region = { limit = { <triggers> } #可选 <effects> } | none | state_region |
| every_state_region_<georegion_short_name> | 遍历指定地理区域中的所有州区域 | every_state_region_<georegion_short_name> = { limit = { <triggers> } #可选 <effects> } | none | state_region |
| every_strategic_objective | 遍历 scope 国家的所有战略目标州 | every_strategic_objective = { limit = { <triggers> } #可选 <effects> } | country | state |
| every_strategic_region | 遍历全球所有战略区域 | every_strategic_region = { limit = { <triggers> } #可选 <effects> } | none | strategic_region |
| every_strategic_region_in_<georegion_short_name> | 遍历指定地理区域中的所有战略区域 | every_strategic_region_in_<georegion_short_name> = { limit = { <triggers> } #可选 <effects> } | none | strategic_region |
| every_subject_of_subject | 层级中位于直接附属国之下的任何国家 | every_subject_of_subject = { limit = { <triggers> } #可选 <effects> } | country | country |
| every_subject_or_below | 层级中位于当前国家之下的任何国家 | every_subject_or_below = { limit = { <triggers> } #可选 <effects> } | country | country |
| every_supporting_character | 遍历支持 scope 政治运动的所有人物 | every_supporting_character = { limit = { <triggers> } #可选 <effects> } | political_movement | character |
| every_treaty | 遍历所有条约（包括生效条约和草案） | every_treaty = { limit = { <triggers> } #可选 <effects> } | none | treaty |
| every_valid_mass_migration_culture | 列出 scope 国家中符合大规模迁移条件的文化 | every_valid_mass_migration_culture = { limit = { <triggers> } #可选 <effects> } | country | culture |
| every_war_participant | 遍历一场战争中的所有参战方 | every_war_participant = { limit = { <triggers> } #可选 <effects> } | war | country |
| execute_event_option | 在指定事件中执行指定事件选项的 effect | execute_event_option = { event = events.1 option = 0 } | none |  |
| exile_character | 将一个人物流放至流放池 | exile_character = yes | character |  |
| finish_harvest_condition | 结束 scope 州区域中给定类型的收成状况 | finish_harvest_condition = <key> | state_region |  |
| finish_negotiation | 结束已为某个利益集团开始的谈判 | finish_negotiation = yes/no | interest_group |  |
| force_resource_depletion | 强制触发州中的资源枯竭 | force_resource_depletion = bg_gold_mining | state |  |
| force_resource_discovery | 强制触发州中的资源发现 | force_resource_discovery = bg_gold_mining | state |  |
| free_character_from_void | 将一个人物从虚空中释放，若设为 no 则改为删除该人物 | free_character_from_void = yes | character |  |
| fully_mobilize_army | 完全动员 scope 陆军 | fully_mobilize_army = yes | military_formation |  |
| hidden_effect | 其中包含的 effect 不会在工具提示中显示 | hidden_effect = { <more effects> } | none |  |
| if | 若 limit 条件满足则执行其中包含的 effect | if = { limit = { <triggers> } <effects> } | none |  |
| improve_stance | 将利益集团对当前正在制定的法律的立场改善给定的步数 | improve_stance = value | interest_group |  |
| increase_autonomy | 将一个国家的附属国类型改为自治程度更高的一种 | increase_autonomy = yes | country |  |
| join_power_bloc | 作用域国家加入目标作用域国家的强权集团 | join_power_bloc = c:USA | country | country |
| join_revolution | 将利益集团加入正在进行的革命 | join_revolution = yes/no | interest_group |  |
| kill_character | 杀死一个人物 | kill_character = bool（yes - 杀死［默认］，no - 不做任何事）kill_character = { hidden = bool（yes - 不显示通知；no - 显示通知［默认］）value = bool（yes - 杀死［默认］，no - 不做任何事）} | character |  |
| kill_crew | 杀死舰船船员的指定数量 | kill_crew = 20 | ship |  |
| kill_crew_percent | 杀死舰船船员的指定百分比 | kill_crew_percent = 0.2 | ship |  |
| kill_population | 杀死作用域国家人口中的一定数量的个体。 | 除 percent 外所有参数均为可选。pop_type 和 strata 不能同时使用。kill_population = { value = <integer value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } | country |  |
| kill_population_in_state | 杀死作用域州人口中的一定数量的个体。 | 除 percent 外所有参数均为可选。pop_type 和 strata 不能同时使用。kill_population = { value = <integer value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } | state |  |
| kill_population_percent | 杀死作用域国家人口的一定百分比。 | 除 percent 外所有参数均为可选。pop_type 和 strata 不能同时使用。kill_population_percent = { percent = <decimal value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } | country |  |
| kill_population_percent_in_state | 杀死作用域州人口的一定百分比。 | 除 percent 外所有参数均为可选。pop_type 和 strata 不能同时使用。kill_population_percent = { percent = <decimal value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } | state |  |
| kill_ship | 摧毁作用域舰船 | kill_ship = bool # yes - 摧毁舰船［默认］，no - 不做任何事 | ship |  |
| liberate_slaves | 解放国家/州内的所有奴隶 | liberate_slaves = yes | country, state |  |
| liberate_slaves_in_incorporated_states | 解放国家已整合州内的所有奴隶 | liberate_slaves_in_incorporated_states = yes | country |  |
| liberate_slaves_in_unincorporated_states | 解放国家未整合州内的所有奴隶 | liberate_slaves_in_unincorporated_states = yes | country |  |
| make_independent | 使一个国家独立。 | make_independent = bool | country |  |
| mobilize_army | 动员作用域陆军 | mobilize_army = yes | military_formation |  |
| move_partial_pop | 将作用域人口的一部分移动到指定州（他们将成为失业状态） | move_partial_pop = { state = s:STATE_TUSCANY.region_state:TUS } move_partial_pop = { state = s:STATE_TUSCANY.region_state:TUS population = 1000 } move_partial_pop = { state = s:STATE_TUSCANY.region_state:TUS population_ratio = 0.2 } 注意：非常重要！该 effect _可能_ 改变被移动人口的类型。发生条件如下：1. 如果当前人口类型不能处于失业状态，新的人口类型将为默认类型 2. 如果当前人口类型为奴隶类型且目标州不允许奴隶制，新的人口类型将为默认类型 | pop |  |
| move_pop | 将作用域人口整体移动到指定州（他们将成为失业状态） | move_pop = s:STATE_TUSCANY.region_state:TUS 注意：非常重要！该 effect _可能_ 改变被移动人口的类型。发生条件如下：1. 如果当前人口类型不能处于失业状态，新的人口类型将为默认类型 2. 如果当前人口类型为奴隶类型且目标州不允许奴隶制，新的人口类型将为默认类型 | pop | state |
| ordered_active_law | 遍历一个国家所有已生效的法律 | ordered_active_law = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | law |
| ordered_active_party | 遍历一个国家所有活跃的政党 | ordered_active_party = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | party |
| ordered_character | 遍历全局所有人物 | ordered_character = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | none | character |
| ordered_character_in_exile_pool | 遍历流亡池中的人物 | ordered_character_in_exile_pool = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | none | character |
| ordered_character_in_void | 遍历“虚空”中的人物 | ordered_character_in_void = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | none | character |
| ordered_character_role | 遍历作用域人物的所有角色 | ordered_character_role = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | character | character_role |
| ordered_civil_war | 遍历与作用域国家相关的所有内战 | ordered_civil_war = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | civil_war |
| ordered_cobelligerent_in_diplo_play | 遍历作用域国家在所有外交博弈中的所有共同交战国（包括战争） | ordered_cobelligerent_in_diplo_play = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | country |
| ordered_cobelligerent_in_war | 遍历作用域国家在所有战争中的所有共同交战国 | ordered_cobelligerent_in_war = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | country |
| ordered_combat_unit | 遍历输入作用域的所有作战单位 | ordered_combat_unit = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | battle, building, front, hq, military_formation | new_combat_unit |
| ordered_company | 遍历一个国家所有公司 | ordered_company = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | company |
| ordered_country | 遍历全局所有国家 | ordered_country = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | none | country |
| ordered_country_in_<georegion_short_name> | 遍历指定地理区域内的所有国家 | ordered_country_in_<georegion_short_name> = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | none | country |
| ordered_country_strategic_region | 遍历包含作用域国家所拥有州的全部战略区域 | ordered_country_strategic_region = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | strategic_region |
| ordered_decentralized_country | 遍历所有松散的国家 | ordered_decentralized_country = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | none | country |
| ordered_diplomatic_catalyst | 遍历一个国家近期记忆中的所有外交催化剂 | ordered_diplomatic_catalyst = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | diplomatic_catalyst |
| ordered_diplomatic_play | 遍历全局所有外交博弈 | ordered_diplomatic_play = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | none | diplomatic_play |
| ordered_diplomatically_relevant_country | 遍历一个国家作用域的所有外交相关国家 | ordered_diplomatically_relevant_country = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | country |
| ordered_direct_subject | 层级中直接位于当前国家之下的任何国家 | ordered_direct_subject = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | country |
| ordered_enemy_in_diplo_play | 遍历作用域国家在所有外交博弈中的所有敌国（包括战争） | ordered_enemy_in_diplo_play = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | country |
| ordered_enemy_in_war | 遍历作用域国家在所有战争中的所有敌国 | ordered_enemy_in_war = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | country |
| ordered_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成状况 | ordered_harvest_condition = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country, state, state_region, strategic_region | harvest_condition |
| ordered_in_global_list | 遍历全局列表中的所有条目。list = 名称或 variable = 名称 | ordered_in_global_list = { list = name or variable = name limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；排序比较要考虑的最小值 max = script_value #可选，默认 inf；排序比较要考虑的最大值 check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| ordered_in_hierarchy | 当前层级中的任何国家，包括当前国家 | ordered_in_hierarchy = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | country |
| ordered_in_list | 遍历列表中的所有条目。 | ordered_in_list = { list = name or variable = name limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；排序比较要考虑的最小值 max = script_value #可选，默认 inf；排序比较要考虑的最大值 check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| ordered_in_local_list | 遍历局部列表中的所有条目。list = 名称或 variable = 名称 | ordered_in_local_list = { list = name or variable = name limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；排序比较要考虑的最小值 max = script_value #可选，默认 inf；排序比较要考虑的最大值 check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| ordered_influenced_interest_group | 遍历受一个政治运动影响的所有利益集团 | ordered_influenced_interest_group = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | political_movement | interest_group |
| ordered_interest_group | 遍历一个国家所有利益集团 | ordered_interest_group = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | interest_group |
| ordered_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | ordered_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # 如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | none |  |
| ordered_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | ordered_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # 如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | none |  |
| ordered_key_in_variable_map | 遍历变量映射中的所有键。 | ordered_key_in_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # 如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | none |  |
| ordered_law | 遍历一个国家所有法律 | ordered_law = { limit = { <triggers> } #可选 order_by = script_value #通过比较决定 scope 的排序 position = int #可选，默认 0；从排序结果中选取 scope，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的 scope 数量，未指定 min 时为 1，指定了则为 inf。check_range_bounds = no #可选；如果列表小于 min/max 时你不希望在日志中记录错误 <effects> } | country | law |
| ordered_lobby_member | 遍历政治游说团（lobby）的所有利益集团成员 | ordered_lobby_member = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_lobby | interest_group |
| ordered_market | 遍历全球所有市场 | ordered_market = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | market |
| ordered_market_goods | 遍历市场中所有活跃的（市场）商品 | ordered_market_goods = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | market | market_goods |
| ordered_member | 遍行政党的所有利益集团成员 | ordered_member = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | party | interest_group |
| ordered_military_formation | 遍历当前存在于输入 scope 的所有军事编队 | ordered_military_formation = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, hq | military_formation |
| ordered_neighbouring_state | 遍历某州区域（state region）相邻的所有州 | ordered_neighbouring_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state, state_region, strategic_region | state |
| ordered_overlord_or_above | 层级结构中位于当前国家之上的任意国家 | ordered_overlord_or_above = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_owned_country | 遍历 scope 公司所拥有的所有国家 | ordered_owned_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | company | country |
| ordered_participant | 外交条约（diplomatic pact）scope 中的两个参与国中的任意一个 | ordered_participant = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_pact | country |
| ordered_political_lobby | 遍历国家或利益集团中的所有政治游说团（political lobby） | ordered_political_lobby = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, interest_group | political_lobby |
| ordered_political_movement | 遍历一个国家中的所有政治运动 | ordered_political_movement = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | political_movement |
| ordered_possible_amendment_type | 遍历可添加到 scope 法律中的修正案（amendment）类型 | ordered_possible_amendment_type = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | law | amendment_type |
| ordered_potential_party | 遍历一个国家中所有潜在的政党 | ordered_potential_party = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | party |
| ordered_power_bloc | 遍历所有强权集团 | ordered_power_bloc = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | power_bloc |
| ordered_power_bloc_member | 遍历 scope 强权集团的所有成员，包括领导者 | ordered_power_bloc_member = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | power_bloc | country |
| ordered_preferred_law | 遍历利益集团所在国家中所有现行及可能的法律，按其对该法律的偏好程度排序 | ordered_preferred_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | interest_group | law |
| ordered_primary_culture | scope 国家或国家定义（country definition）的主流文化 | ordered_primary_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, country_definition | culture |
| ordered_province | 遍历 scope 州中的所有省份（Province） | ordered_province = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state | province |
| ordered_province_in_<georegion_short_name> | 遍历指定地理区域（geographic region）中的所有省份 | ordered_province_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | province |
| ordered_rival_country | 被 scope 国家视为竞争对手的任意国家 | ordered_rival_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_rivaling_country | 与 scope 国家互为竞争对手的任意国家 | ordered_rivaling_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_scope_admiral | 遍历以下 scope 中的所有海军上将：国家、利益集团或军事编队 | ordered_scope_admiral = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_ally | 遍历一个国家的所有盟友 | ordered_scope_ally = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_scope_amendment | 遍历 scope 法律的修正案 | ordered_scope_amendment = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | law | amendment |
| ordered_scope_army | 遍历当前存在于输入 scope 的所有陆军 | ordered_scope_army = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, hq | military_formation |
| ordered_scope_article | 遍历 scope 条约的条款 | ordered_scope_article = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty | treaty_article |
| ordered_scope_article_option | 遍历 scope 条约或条约选项（treaty_options）的条款选项（article_options） | ordered_scope_article_option = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty, treaty_options | treaty_article_options |
| ordered_scope_building | 遍历以下 scope 中的所有建筑：州、国家 | ordered_scope_building = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state | building |
| ordered_scope_character | 遍历以下 scope 中的所有人物：国家、利益集团或前线 | ordered_scope_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_country | 遍历在支持的 scope（当前为：市场、州区域、战略区域）中有存在的所有国家 | ordered_scope_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | market, state_region, strategic_region | country |
| ordered_scope_culture | 遍历 scope 中的所有文化 | ordered_scope_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state | culture |
| ordered_scope_diplomatic_pact | scope 国家的任意外交条约 | ordered_scope_diplomatic_pact = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | diplomatic_pact |
| ordered_scope_fleet | 遍历当前存在于输入 scope 的所有舰队 | ordered_scope_fleet = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, hq | military_formation |
| ordered_scope_front | 遍历与 scope 战争相关的所有前线 | ordered_scope_front = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | war | front |
| ordered_scope_general | 遍历以下 scope 中的所有将军：国家、利益集团、前线或军事编队 | ordered_scope_general = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_held_interest_marker | 遍历一个国家持有的所有利益标记（interest marker） | ordered_scope_held_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | interest_marker |
| ordered_scope_homeland_state | 遍历作为 scope 文化故乡（homeland）的所有州，或作为 scope 国家任一主流文化故乡的所有州 | ordered_scope_homeland_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, culture | state |
| ordered_scope_initiator_ally | 遍历外交博弈中发起方的所有盟友 | ordered_scope_initiator_ally = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_play | country |
| ordered_scope_interest_marker | 遍历以下 scope 中的所有利益标记：国家、state_region、战略区域 | ordered_scope_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state_region, strategic_region | interest_marker |
| ordered_scope_je_involved | 遍历日志条目中的所有参与方 | ordered_scope_je_involved = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | journal_entry | country |
| ordered_scope_play_involved | 遍历以下 scope 中外交博弈的所有参与方 | ordered_scope_play_involved = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_play | country |
| ordered_scope_politician | 遍历以下 scope 中的所有政客：国家或利益集团 | ordered_scope_politician = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_pop | 遍历以下 scope 中的所有人口：国家、州、利益集团、文化 | ordered_scope_pop = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, culture, interest_group, state | pop |
| ordered_scope_regional_hqs | 遍历 scope 所指公司的所有地区总部 | ordered_scope_regional_hqs = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | company | building |
| ordered_scope_ship | 遍历国家或军事编制中的所有舰船 | ordered_scope_ship = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, military_formation | ship |
| ordered_scope_state | 遍历以下 scope 中包含省份的所有州：国家、state_region、战区、前线或海峡 | ordered_scope_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, state_region, strait, strategic_region, theater | state |
| ordered_scope_strait | 遍历在 scope 所指的州或国家拥有陆地端点的所有海峡 | ordered_scope_strait = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state | strait |
| ordered_scope_target_ally | 遍历以下 scope 中外交博弈目标的所有盟友 | ordered_scope_target_ally = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_play | country |
| ordered_scope_theater | 遍历以下 scope 中的所有战区：国家 | ordered_scope_theater = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | theater |
| ordered_scope_treaty | 遍历约束 scope 所指国家的所有生效条约 | ordered_scope_treaty = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | treaty |
| ordered_scope_violate_sovereignty_interested_parties | 遍历在 scope 所指国家的主权被侵犯时会表示关注的所有国家 | ordered_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_scope_violate_sovereignty_wars | 遍历目标国家的主权被 scope 所指国家侵犯时涉及的所有战争 | ordered_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | war |
| ordered_scope_war | 遍历与该 scope 相关的所有战争 | ordered_scope_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | war |
| ordered_sea_node_adjacent_state | 遍历与某个州共享海洋节点的所有州 | ordered_sea_node_adjacent_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state | state |
| ordered_state | 遍历全球所有州 | ordered_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state |
| ordered_state_in_<georegion_short_name> | 遍历指定地理区域中的所有州 | ordered_state_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state |
| ordered_state_region | 遍历所有州区域 | ordered_state_region = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state_region |
| ordered_state_region_in_<georegion_short_name> | 遍历指定地理区域中的所有州区域 | ordered_state_region_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state_region |
| ordered_strategic_objective | 遍历 scope 所指国家的所有战略目标州 | ordered_strategic_objective = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | state |
| ordered_strategic_region | 遍历全球所有战略区域 | ordered_strategic_region = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | strategic_region |
| ordered_strategic_region_in_<georegion_short_name> | 遍历指定地理区域中的所有战略区域 | ordered_state_region_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | strategic_region |
| ordered_subject_of_subject | 层级中直接附属国之下的任何国家 | ordered_subject_of_subject = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_subject_or_below | 层级中当前国家之下的任何国家 | ordered_subject_or_below = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_supporting_character | 遍历支持 scope 所指政治运动的所有人物 | ordered_supporting_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_movement | character |
| ordered_treaty | 遍历所有条约（包括生效条约与草案） | ordered_treaty = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | treaty |
| ordered_valid_mass_migration_culture | 列出 scope 所指国家中符合大规模迁移条件的文化 | ordered_valid_mass_migration_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | culture |
| ordered_war_participant | 遍历战争中的所有参战方 | ordered_war_participant = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | war | country |
| place_character_in_void | 将一个人物放逐至虚空，duration 为人物在被删除前保留的时长 | place_character_in_void = months | character |  |
| play_as | 更改 scope 所指国家的玩家将扮演的国家 | play_as = <scope> | country | country |
| post_audio_event | 在一个 persistent = true 的音频对象上运行音频事件 | post_audio_event = { persistent_object = [object_name] # For example music_manager event = [audio_event] # For example start_debug_music } | none |  |
| post_notification | 发布通知 |  | none |  |
| post_proposal | 发布提案 |  | none |  |
| random | 根据随机几率运行一个 effect，否则不执行任何操作。 | random = { chance = 0-100 # random chance in percent. can also be a script value or complex math modifier = { ... } # optional MTTH-style modifier for the chance effects... # effects to run if the random roll succeeds } | none |  |
| random_active_law | 遍历一个国家中的所有生效法律 | random_active_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | law |
| random_active_party | 遍历一个国家中的所有活跃政党 | random_active_party = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | party |
| random_character | 遍历全球所有人物 | random_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | character |
| random_character_in_exile_pool | 遍历流亡者池中的人物 | random_character_in_exile_pool = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | character |
| random_character_in_void | 遍历虚空中的人物 | random_character_in_void = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | character |
| random_character_role | 遍历 scope 所指人物的所有角色 | random_character_role = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character | character_role |
| random_civil_war | 遍历与 scope 所指国家相关的所有内战 | random_civil_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | civil_war |
| random_cobelligerent_in_diplo_play | 遍历 scope 所指国家在所有外交博弈（包括战争）中的所有共同交战国 | random_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_cobelligerent_in_war | 遍历 scope 所指国家在所有战争中的所有共同交战国 | random_cobelligerent_in_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_combat_unit | 遍历输入 scope 的所有作战单位 | random_combat_unit = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | battle, building, front, hq, military_formation | new_combat_unit |
| random_company | 遍历一个国家中的所有公司 | random_company = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | company |
| random_country | 遍历全球所有国家 | random_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | country |
| random_country_in_<georegion_short_name> | 遍历指定地理区域中的所有国家 | random_country_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | country |
| random_country_strategic_region | 遍历包含 scope 所指国家拥有州的所有战略区域 | random_country_strategic_region = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | strategic_region |
| random_decentralized_country | 遍历所有非集权化国家 | random_decentralized_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | country |
| random_diplomatic_catalyst | 遍历一个国家近期记忆中的所有外交催化剂 | random_diplomatic_catalyst = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | diplomatic_catalyst |
| random_diplomatic_play | 遍历全球所有外交博弈 | random_diplomatic_play = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | diplomatic_play |
| random_diplomatically_relevant_country | 遍历一个国家 scope 的所有外交相关国家 | random_diplomatically_relevant_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_direct_subject | 层级中直接位于当前国家之下的任何国家 | random_direct_subject = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_enemy_in_diplo_play | 遍历 scope 所指国家在所有外交博弈（包括战争）中的所有敌人 | random_enemy_in_diplo_play = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_enemy_in_war | 遍历 scope 国家在所有战争中的全部敌方国家 | random_enemy_in_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_harvest_condition | 遍历影响某个州、州区域、战略区域或国家的全部收成状况 | random_harvest_condition = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state, state_region, strategic_region | harvest_condition |
| random_in_global_list | 遍历全局列表中的所有项目。 | random_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| random_in_hierarchy | 当前层级体系中的任意国家，包括当前国家 | random_in_hierarchy = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_in_list | 遍历列表中的所有项目。 | random_in_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| random_in_local_list | 遍历本地列表中的所有项目。 | random_in_local_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| random_influenced_interest_group | 遍历受某个政治运动影响的全部利益集团 | random_influenced_interest_group = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_movement | interest_group |
| random_interest_group | 遍历某个国家中的全部利益集团 | random_interest_group = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | interest_group |
| random_key_in_global_variable_map | 遍历全局变量映射表中的所有键。 | random_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_local_variable_map | 遍历本地变量映射表中的所有键。 | random_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_variable_map | 遍历变量映射表中的所有键。 | random_key_in_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_law | 遍历某个国家中的全部法律 | random_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | law |
| random_list | 从一个加权随机列表中选择一个 effect 并执行。 | random_list = { 10 = { trigger = { enable / disable this effect } modifier = { if = { limit = { is_foo } add = 10 } # 注意：可以在同一个 `modifier` 块中包含多个条件， # 使不同场景以不同方式影响几率 if = { limit = { is_bar } add = 20 } } # 警告：不要添加多个 `modifier` 块，因为只有最后一个 # 会被考虑。相反，应在一个 # `modifier` 块内使用多个 `if` 条件（即每个 effect 各一个） <effect_1> } 30 = { # trigger 是可选的，省略它意味着该 effect 始终启用 # modifier 同样是可选的，省略它意味着基础权重 (30) 是最终值 # 注意：在此处使用 `modifier` 块完全没问题。重要的是每个 # effect 只能有一个 `modifier` 块，而不是总共只能有一个。 <effect_2> } } 各 effect 按其相对权重加权（示例中为 10 和 30）。例如在本例中，第一个 effect 有 25% 的基础概率被选中，而第二个 effect 有 75% 的基础概率。概率由公式 `Wn / Wt` 给出，其中 `Wn` 是某个特定事件的权重，而 `Wt` 是所有权重的总和。因此本例中的概率分别为 10 / 40 (25%) 和 30 / 40 (75%)。effect 的权重可以通过 `modifier` 块来修改。在本例中，如果 scope 对象满足 `is_foo` 触发条件，其相对权重增加 10。那么在该情况下，相对权重将变为 20 和 30 而非 10 和 30，意味着概率将变为 40% 和 60% 而非 25% 和 75%。 | none |  |
| random_lobby_member | 遍历某个政治游说团的全部利益集团成员 | random_lobby_member = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_lobby | interest_group |
| random_log_scopes | 当此 effect 执行时，将当前 scope 记录到随机日志中。 | 仅临时用于调试目的，因为它可能将本地化字符串引入随机日志。 random_log_scopes = yes # 记录完整 scope 信息 random_log_scopes = no # 仅记录当前 scope | none |  |
| random_market | 遍历全球所有市场 | random_market = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | market |
| random_market_goods | 遍历某个市场中的所有活跃（市场）商品 | random_market_goods = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | market | market_goods |
| random_member | 遍历某个政党的全部利益集团成员 | random_member = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | party | interest_group |
| random_military_formation | 遍历当前存在于输入 scope 的所有军事编队 | random_military_formation = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, hq | military_formation |
| random_neighbouring_state | 遍历与某个州区域相邻的所有州 | random_neighbouring_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state, state_region, strategic_region | state |
| random_overlord_or_above | 层级体系中位于当前国家之上的任意国家 | random_overlord_or_above = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_owned_country | 遍历 scope 公司所拥有的全部国家 | random_owned_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | company | country |
| random_participant | 某个 scope 中外交协定的两方参与者之一 | random_participant = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_pact | country |
| random_political_lobby | 遍历某个国家或利益集团中的所有政治游说团 | random_political_lobby = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, interest_group | political_lobby |
| random_political_movement | 遍历某个国家中的所有政治运动 | random_political_movement = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | political_movement |
| random_possible_amendment_type | 遍历可添加到 scope 法律的修正案类型 | random_possible_amendment_type = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | law | amendment_type |
| random_potential_party | 遍历某个国家中所有潜在的政党 | random_potential_party = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | party |
| random_power_bloc | 遍历所有强权集团 | random_power_bloc = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | power_bloc |
| random_power_bloc_member | 遍历 scope 强权集团的所有成员，包括领导者 | random_power_bloc_member = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | power_bloc | country |
| random_preferred_law | 遍历某个利益集团所在国家的所有现行及可能的法律，按其对该法律的偏好程度排序 | random_preferred_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | interest_group | law |
| random_primary_culture | scope 国家或国家定义的主要文化 | random_primary_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, country_definition | culture |
| random_province | 遍历 scope 州中的所有省份 | random_province = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state | province |
| random_province_in_<georegion_short_name> | 遍历指定地理区域中的所有省份 | random_province_in_<georegion_short_name>' = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | province |
| random_rival_country | 被 scope 中的国家视为竞争对手的任意国家 | random_rival_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_rivaling_country | 与 scope 中的国家互为竞争对手的任意国家 | random_rivaling_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_scope_admiral | 遍历以下对象中的所有海军上将：国家、利益集团或军事编队 | random_scope_admiral = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_ally | 遍历某个国家的所有同盟国 | random_scope_ally = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_scope_amendment | 遍历 scope 法律的修正案 | random_scope_amendment = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | law | amendment |
| random_scope_army | 遍历当前存在于输入 scope 的所有陆军 | random_scope_army = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, hq | military_formation |
| random_scope_article | 遍历 scope 条约的条款 | random_scope_article = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty | treaty_article |
| random_scope_article_option | 遍历 scope 条约或条约选项的条款选项 | random_scope_article_option = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty, treaty_options | treaty_article_options |
| random_scope_building | 遍历以下对象中的所有建筑：州、国家 | random_scope_building = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state | building |
| random_scope_character | 遍历以下对象中的所有人物：国家、利益集团或前线 | random_scope_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_country | 遍历在受支持的 scope（当前为：市场、州区域、战略区域）中有存在的所有国家 | random_scope_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | market, state_region, strategic-region | country |
| random_scope_culture | 遍历 scope 中的所有文化 | random_scope_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state | culture |
| random_scope_diplomatic_pact | scope 中国家的任意外交协定 | random_scope_diplomatic_pact = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | diplomatic_pact |
| random_scope_fleet | 遍历当前存在于输入 scope 的所有舰队 | random_scope_fleet = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, hq | military_formation |
| random_scope_front | 遍历与 scope 战争相关的所有前线 | random_scope_front = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | war | front |
| random_scope_general | 遍历以下对象中的所有将军：国家、利益集团、前线或军事编队 | random_scope_general = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_held_interest_marker | 遍历某个国家持有的所有利益标记 | random_scope_held_interest_marker = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | interest_marker |
| random_scope_homeland_state | 遍历作为 scope 文化的家园的所有州，或作为 scope 国家任意主要文化家园的所有州 | random_scope_homeland_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, culture | state |
| random_scope_initiator_ally | 遍历外交博弈中发起方的所有同盟国 | random_scope_initiator_ally = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_play | country |
| random_scope_interest_marker | 遍历以下对象中的所有利益标记：国家、州区域、战略区域 | random_scope_interest_marker = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state_region, strategic-region | interest_marker |
| random_scope_je_involved | 遍历某个日志条目的所有参与方 | random_scope_je_involved = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | journal_entry | country |
| random_scope_play_involved | 遍历某个外交博弈中的所有参与方 | random_scope_play_involved = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_play | country |
| random_scope_politician | 遍历以下对象中的所有政客：国家或利益集团 | random_scope_politician = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_pop | 遍历以下对象中的所有人口：国家、州、利益集团、文化 | random_scope_pop = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, culture, interest_group, state | pop |
| random_scope_regional_hqs | 遍历 scope 公司的区域总部 | random_scope_regional_hqs = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | company | building |
| random_scope_ship | 遍历某个国家或军事编队中的所有舰船 | random_scope_ship = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, military_formation | ship |
| random_scope_state | 遍历以下对象中包含省份在内的所有州：国家、州区域、战区、前线或海峡 | random_scope_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, state_region, strait, strategic_region, theater | state |
| random_scope_strait | 遍历在 scope 州或国家拥有陆上端点的所有海峡 | random_scope_strait = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state | strait |
| random_scope_target_ally | 遍历外交博弈中目标方的所有同盟国 | random_scope_target_ally = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_play | country |
| random_scope_theater | 遍历某个国家中的所有战区 | random_scope_theater = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | theater |
| random_scope_treaty | 遍历对 scope 国家有约束力的所有生效条约 | random_scope_treaty = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | treaty |
| random_scope_violate_sovereignty_interested_parties | 遍历在 scope 国家的主权被侵犯时会关注的所有国家 | random_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_scope_violate_sovereignty_wars | 遍历在目标国家被 scope 国家侵犯主权时相关的所有战争 | random_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | war |
| random_scope_war | 遍历与该 scope 相关的所有战争 | random_scope_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | war |
| random_sea_node_adjacent_state | 遍历与某个州共享海洋节点的所有州 | random_sea_node_adjacent_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state | state |
| random_state | 遍历全球所有州 | random_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state |
| random_state_in_<georegion_short_name> | 遍历指定地理区域中的所有州 | random_state_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state |
| random_state_region | 遍历所有州区域 | random_state_region = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state_region |
| random_state_region_in_<georegion_short_name> | 遍历指定地理区域中的所有州区域 | random_state_region_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state_region |
| random_strategic_objective | 遍历 scope 国家的所有战略目标州 | random_strategic_objective = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | state |
| random_strategic_region | 遍历全球所有战略区域 | random_strategic_region = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | strategic_region |
| random_strategic_region_in_<georegion_short_name> | 遍历指定地理区域中的所有战略区域 | random_strategic_region_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | strategic_region |
| random_subject_of_subject | 层级体系中位于直接附属国之下的任意国家 | random_subject_of_subject = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_subject_or_below | 层级体系中位于当前国家之下的任意国家 | random_subject_or_below = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_supporting_character | 遍历支持 scope 政治运动的所有人物 | random_supporting_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_movement | character |
| random_treaty | 遍历所有条约（包括生效条约和草案） | random_treaty = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | treaty |
| random_valid_mass_migration_culture | 列出 scope 国家中适合大规模迁移的文化 | random_valid_mass_migration_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | culture |
| random_war_participant | 遍历某场战争中的所有参战方 | random_war_participant = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | war | country |
| recalculate_pop_ig_support | 重新计算并更新某个国家的人口利益集团成员身份 = bool |  | country |  |
| regime_change | 由 scope 国家对目标国家执行政权更迭。 | regime_change = scope:upstart_country | country | country |
| remove_active_objective_subgoal | 移除一个激活的目标子目标 | remove_active_objective_subgoal = <key> | country |  |
| remove_amendment | 立即移除一项修正案，不检查冷却时间 | remove_amendment = bool | amendment |  |
| remove_as_interest_group_leader | 将某个人物从利益集团领袖职位上移除 | remove_as_interest_group_leader = yes | character |  |
| remove_banned_goods | 移除某个国家对某种商品的全面禁令 | remove_banned_goods = <goods key/scope> | country | goods |
| remove_building | 移除 scope 州中某个建筑的所有等级 | remove_building = building_key | state |  |
| remove_character_ideology | 从 scope 政治运动的人物意识形态列表中移除一项人物意识形态 | remove_character_ideology = ideology:<ideology key> | political_movement |  |
| remove_character_role | 移除人物的现有角色，可使用原型或数据库角色 | remove_character_role = general/character_role_general | character |  |
| remove_claim | 将 scope 州区域作为目标国家的领土主张移除 | add_claim = scope/country | state_region | country |
| remove_company | 从某个国家的公司中移除指定类型的公司 | remove_company = company_type:key | country | company_type |
| remove_cultural_obsession | 移除 scope 文化对某种商品的痴迷 | remove_cultural_obsession = <goods> | culture |  |
| remove_cultural_taboo | 移除 scope 文化对某种商品的禁忌 | remove_cultural_taboo = <goods> | culture |  |
| remove_diplomatic_pact | 移除两国之间的外交协定，以 scope 国家为发起方 | remove_diplomatic_pact = { country = country scope/tag type = diplomatic action type } | country |  |
| remove_enactment_modifier | 移除 scope 对象上一个与立法相关的限时 modifier 效果 |  | country |  |
| remove_exports | 为 scope 州商品移除该州出口的乘数 | remove_exports = 3 | state_goods |  |
| remove_from_global_variable_map | 从全局变量映射表中移除目标 | remove_from_global_variable_map = { name = name of the map key = event target } | none |  |
| remove_from_list | 将当前 scope 从命名列表中移除 | remove_from_list = <list_name> | none |  |
| remove_from_local_variable_map | 从本地变量映射表中移除目标 | remove_from_variable_map = { name = name of the map key = event target } | none |  |
| remove_from_variable_map | 从变量映射表中移除目标 | remove_from_variable_map = { name = name of the map key = event target } | none |  |
| remove_global_variable | 移除一个全局变量 | remove_global_variable = variable_name | none |  |
| remove_homeland | 将 scope 州区域作为目标文化的家园移除 | remove_homeland = cu:culture | state_region | culture |
| remove_ideology | 从 scope 利益集团中移除一项意识形态 | remove_ideology = ideology:<ideology key> | interest_group |  |
| remove_ig_from_party | 将目标利益集团从 scope 政党中移除 | py:py_key = { remove_ig_from_party = ig:ig_key } | party | interest_group |
| remove_imports | 为 scope 州商品移除一个进口乘数 | remove_imports = 3 | state_goods |  |
| remove_initiator_backers | 将一个 tag/scope 国家从外交博弈的发起方移除 | remove_initiator_backers = { list of scopes/tags } | diplomatic_play |  |
| remove_involved_country | 将目标国家从 scope 日志条目的参与国家中移除 | remove_involved_country = c:FRA | journal_entry | country |
| remove_list_global_variable | 将目标从一个全局变量列表中移除 | remove_list_global_variable = { name = <global variable> target = <event target> } | none |  |
| remove_list_local_variable | 将目标从一个局部变量列表中移除 | remove_list_local_variable = { name = <local variable> target = <event target> } | none |  |
| remove_list_variable | 将目标从一个变量列表中移除 | remove_list_variable = { name = <variable name> target = <event target> } | none |  |
| remove_lobby_member | 将一个利益集团从 scope 政治游说团成员中移除 | remove_lobby_member = scope:interest_group | political_lobby | interest_group |
| remove_local_variable | 移除一个局部变量 | remove_local_variable = variable_name | none |  |
| remove_modifier | 移除施加于 scope 对象的限时 modifier 效果 | remove_modifier = static_modifier_name | building, character, country, institution, interest_group, journal_entry, political_movement, power_bloc, state |  |
| remove_monopoly | 在国家 scope 中移除某一特定建筑的垄断 | remove_monopoly = bt:building_textile_mills | country | building_type |
| remove_owned_country | 移除 scope 公司对目标国家的所有权 | remove_owned_country = country:key | company | country |
| remove_primary_culture | 从国家的主要文化中移除一种文化 | remove_primary_culture = <culture> | country | culture |
| remove_principle | 从强权集团中移除一项原则 | power_bloc = { remove_principle = test_principle_group_A_1 } | power_bloc |  |
| remove_resource_potential | 从州区域的资源潜力中移除一种建筑类型 | remove_resource_potential = building_iron_mine | state, state_region |  |
| remove_ruling_interest_group | 将 scope 中的利益集团从政府中移除 | remove_ruling_interest_group = yes/no | interest_group |  |
| remove_state_trait | 移除 scope 州区域中的一个州特质 | remove_state_trait = <state_trait_name> | state_region |  |
| remove_target_backers | 将一个 tag/scope 国家添加到外交博弈的目标方并从中移除 | remove_target_backers = { list of scopes/tags } | diplomatic_play |  |
| remove_taxed_goods | 移除国家对某种商品的消费税 | remove_taxed_goods = <goods key/scope> | country | goods |
| remove_tradition_trait | 移除 scope 文化中已有的一个传统特质 | remove_tradition_trait = <tradition_trait> | culture |  |
| remove_trait | 移除一个人物的特质 | remove_trait = trait | character |  |
| remove_variable | 移除一个变量 | remove_variable = variable_name | none |  |
| remove_war_goal | 从一个外交博弈中移除战争目标。使用与 add_war_goal/create_diplomatic_play 相同的语法 | remove_war_goal = { holder = country scope/tag war_goal = <war goal key> target_state = <state scope> (if required) target_country = <country scope> (if required) target_region = <region scope> (if required) } | diplomatic_play |  |
| replace_character_roles | 用其他角色替换一个人物的现有角色，可使用 archetype 或数据库角色 | replace_character_role = { add = { roles } remove = { roles } remove_all = no/yes } | character |  |
| reset_hub_names | 重置 scope 州中所有枢纽的名称 | reset_hub_names = yes | state |  |
| reset_state_name | 重置 scope 州的名称 | reset_state_name = yes | state |  |
| resolve_play_for | 为一方结束外交博弈效果，并使其获得战争目标 | resolve_play_for = initiator resolve_play_for = scope:custom_scoped_country | diplomatic_play | country |
| retire_character | 使一个人物退休 | retire_character = bool (yes - retire [by default], no - don't do anything) retire_character = { hidden = bool (yes - without notification; no - show notification [by default]) value = bool (yes - retire [by default], no - don't do anything) } | character |  |
| retire_character_if_should_be_culled | 若一个人物应被清理，则有条件地使其退休 | retire_character_if_should_be_culled = bool (yes - retire [by default], no - don't do anything) retire_character_if_should_be_culled = { hidden = bool (yes - without notification; no - show notification [by default]) value = bool (yes - retire [by default], no - don't do anything) } | character |  |
| round_global_variable | 将一个全局变量四舍五入到最接近的指定值 | round_global_variable = { name = <global variable> nearest = <script_value> } | none |  |
| round_local_variable | 将一个局部变量四舍五入到最接近的指定值 | round_local_variable = { name = <local variable> nearest = <script_value> } | none |  |
| round_variable | 将一个变量四舍五入到最接近的指定值 | round_variable = { name = <variable name> nearest = <script_value> } | none |  |
| save_scope_as | 将当前 scope 保存为任意命名的目标，以便在（未中断的）事件链中稍后引用 | save_scope_as = <string> | none |  |
| save_scope_value_as | 将一个数值或布尔值保存为任意命名的目标，以便在（未中断的）事件链中稍后引用 | save_scope_value_as = { name = <string> value = x } | none |  |
| save_temporary_scope_as | 将当前 scope 保存为任意命名的临时目标，以便在同一 effect 中稍后引用 | save_temporary_scope_as = <string> | none |  |
| save_temporary_scope_value_as | 将一个数值或布尔值保存为任意命名的临时目标，以便在同一 effect 中稍后引用 | save_temporary_scope_value_as = { name = <string> value = x } | none |  |
| seize_investment_pool | 将投资池收归国库，并将所有私人建设队列元素转移到政府队列 = bool |  | country |  |
| set_as_adult | 若 scope 人物尚非成年人，则将其变为成年人。 | set_as_adult = yes | character |  |
| set_as_flagship | 将该舰船指定/取消指定为国家的旗舰 | set_as_flagship = yes/no | ship |  |
| set_as_interest_group_leader | 将一个人物设为利益集团领袖 | set_as_interest_group_leader = yes | character |  |
| set_available_for_autonomous_investment | 在当前 scope 州中将一种建筑类型设为可用于自主投资 | set_available_for_autonomous_investment = building type scope | state | building_type |
| set_bar_progress | 为日志条目的脚本化进度条设置进度 | set_bar_progress = { value = -5 name = example_progress_bar_name } | journal_entry |  |
| set_bolstering | 开始/停止扶植 scope 中的政治运动 | set_bolstering = yes/no | political_movement |  |
| set_capital | 在国家 scope 中设置首都州 | set_capital = <state_region key> | country |  |
| set_career_length | 为担任某一角色的人物设置从现在起算的任期长度。角色可以是特定的数据库角色或角色类型（例如 general）。若未指定角色，则应用于所有有任期结束日期的角色。 | set_career_length = { role = role_key/role_type days/months/years = 10 random_range = { 0.8 1.2 } } | character |  |
| set_character_as_executive | 使 scope 人物成为目标公司的高管 | set_character_as_executive = <company scope> | character | company |
| set_character_as_ruler | 将 scope 人物设为其国家的统治者。 | scope:larry = { set_character_as_ruler = yes } 注意：不要对特许公司使用此 effect，因为该人物的国家会受到影响 | character |  |
| set_character_busy_and_immortal | 将一个人物标记为忙碌且不朽，或清除该标记 | set_character_busy = bool | character |  |
| set_character_immortal | 设置 scope 人物是否不朽。 | scope:larry = { set_character_immortal = yes/no } | character |  |
| set_commander_rank | 将一个人物晋升/降级到给定的军衔值 | set_commander_rank = 3 | character |  |
| set_company_establishment_date | 设置 scope 公司的成立日期 | set_company_establishment_date = 1782.7.18 | company |  |
| set_company_state_region | 为 scope 公司设置州区域，使公司建筑可以在该处建造 | set_company_state_region = s:STATE_WALLONIA | company | state_region |
| set_core_ideology | 设置政治运动的核心意识形态 | set_ideology = ideology:<ideology key> | political_movement |  |
| set_country_type | 为一个国家设置国家类型，用于历史 |  | country |  |
| set_devastation | 为一个州区域或州设置荒废度 |  | state, state_region |  |
| set_diplomats_expelled | 在 scope 国家中驱逐目标国家的外交官 | set_diplomats_expelled = scope:target_country | country | country |
| set_electoral_confidence | 在 scope 国家中设置 x% 的选举信心 | set_electoral_confidence = 0.5 | country |  |
| set_export_tariff_level | 为 scope 国家的某种商品设置出口关税等级 | set_export_tariff_level = { goods = g:iron level = max_tariffs } | country |  |
| set_exports | 为 scope 州商品设置一个出口乘数 | set_exports = 3 | state_goods |  |
| set_fervor | 设置 scope 文化的狂热度 | set_fervor = 3.0 | culture |  |
| set_first_name | 将一个人物的名字更改为一个 loc key | set_first_name = loc_key | character |  |
| set_global_variable | 设置一个全局变量 | set_global_variable = { name = <global variable> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } 该变量可通过 global_var:<variable name> 访问。也可用作 set_global_variable = X（等价于 set_global_variable = { name = X value = yes }） | none |  |
| set_government_wage_level | 设置 scope 国家的政府工资等级 | set_government_wage_level = very_low/low/medium/high/very_high | country |  |
| set_has_negotiated | 设置一个利益集团是否已完成谈判 | set_has_negotiated = yes/no | interest_group |  |
| set_heir | 将 scope 国家的继承人设为指定的人物 scope | set_heir = scope_victoria | country | character |
| set_home_country | 设置一个人物的母国。这会使他们开始认为自己处于流放状态，即 was_exiled 对他们开始判定为 yes。 | set_home_country = c:FRA | character | country |
| set_home_country_definition | 将一个人物的母国直接设置为一个 tag，可借此避免确认该 tag 是否存在，这会使他们成为流亡者 | set_home_country_definition = cd:FRA | character | country_definition |
| set_home_state | 更改 scope 人物的家乡州 | set_home_state = <state scope> | character | state |
| set_hub_name | 将 scope 州中某一枢纽的名称设置为一个本地化字符串 | set_state_name = { type = city ( can be any hub type city/port/farm/mine/wood ) name = HUB_NAME_STATE_KIEV_city_ukrainian } | state |  |
| set_hub_names | 基于州区域名称、枢纽类型和指定后缀，将 scope 州中所有枢纽的名称设置为本地化字符串 | set_hub_names = ukrainian | state |  |
| set_ideology | 更改 scope 人物的意识形态 | set_ideology = ideology:<ideology key> | character | ideology |
| set_ig_trait | 为利益集团添加一个特质，或用具有相同支持度等级的特质替换其当前特质 | set_ig_trait = ig_trait:ig_trait_engines_of_progress | interest_group | interest_group_trait |
| set_immune_to_revolutions | 使一个国家对革命免疫，或移除该免疫。 | set_immune_to_revolutions = yes/no | country |  |
| set_import_tariff_level | 为 scope 国家的某种商品设置进口关税等级 | set_import_tariff_level = { goods = g:iron level = max_tariffs } | country |  |
| set_imports | 为 scope 州商品设置一个进口乘数 | set_imports = 3 | state_goods |  |
| set_institution_investment_level | 设置一个机构的投资等级 | set_institution_investment_level = { institution = <key> level = x } | country |  |
| set_interest_group | 设置人物所属的利益集团 | set_interest_group = ruler.interest_group | character | interest_group |
| set_interest_group_name | 将利益集团重命名为指定的 loc key | set_interest_group_name = x | interest_group |  |
| set_is_noble | 设置 scope 人物的贵族标记。 | set_is_noble = yes/no | character |  |
| set_key | 为一个外交博弈设置名称 | set_key = loc_key | diplomatic_play |  |
| set_last_name | 将一个人物的姓氏更改为一个 loc key | set_last_name = loc_key | character |  |
| set_local_variable | 设置一个局部变量 | set_local_variable = { name = <local variable> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } 该变量可通过 local_var:<variable name> 访问，直至当前 effect 或事件链结束。也可用作 set_local_variable = X（等价于 set_local_variable = { name = X value = yes }） | none |  |
| set_market_capital | 在国家 scope 中设置市场首都 | set_market_capital = <state_region key> | country |  |
| set_military_wage_level | 设置 scope 国家的军队工资等级 | set_military_wage_level = very_low/low/medium/high/very_high | country |  |
| set_mutual_secret_goal | 为 scope 国家和目标国家设置相互的秘密 AI 目标 | set_mutual_secret_goal = { country = country scope/tag secret_goal = secret goal type } | country |  |
| set_name_format | 设置 scope 文化的姓名格式 | set_name_format = first_last/last_first | culture |  |
| set_next_election_date | 为国家设置下一次选举日期 | set_next_election_date = year.month.day | country |  |
| set_only_legal_party_from_ig | 设置国家中唯一合法的政党，用于一党制国家法律。 | set_only_legal_party_from_ig = ruler.interest_group | country | interest_group |
| set_owes_obligation_to | 设置一个国家是否对另一个国家负有义务 | set_owes_obligation = { country = country scope/tag setting = yes/no } | country |  |
| set_owner_of_provinces | 将一个州区域中的一组省份给予特定国家 | set_owner_of_provinces = { country = <scope> provinces = { <province list> } } | state_region |  |
| set_pop_literacy | 设置该人口劳动力的识字率百分比 | set_pop_literacy = { literacy_rate = { script_value } } | pop |  |
| set_pop_qualifications | 为给定类型设置该人口劳动力中某百分比人口对应的资质 | set_pop_qualifications = { pop_type = {} qualifications = { script_value } } | pop |  |
| set_pop_wealth | 设置该人口的财富 | set_pop_wealth = { wealth_distribution = { script_value } update_loyalties = true/false } | pop |  |
| set_relations | 设置两个国家之间的关系 | set_relations = { country = country scope/tag value = amount } | country |  |
| set_ruling_interest_groups | 由一组利益集团为 scope 国家组建政府 | set_ruling_interest_groups = { ig_tag1 ig_tag2 } | country |  |
| set_ruling_party | 将一个政党中的所有利益集团加入政府，并将所有其他利益集团移出政府 | set_ruling_party = yes | party |  |
| set_secret_goal | 为 scope 国家设置针对另一个国家的秘密 AI 目标 | set_secret_goal = { country = country scope/tag secret_goal = secret goal type } | country |  |
| set_ship_owner | 设置舰船的所有者国家 | set_ship_owner = <country> | ship | country |
| set_ship_owner_multiple | 设置舰船的所有者国家，在连续设置多艘舰船时使用，可将它们置于单一所有权转移舰队中，随后使用 clear_ownership_transfer_fleet 清除 | set_ship_owner_multiple = <country> | ship | country |
| set_social_hierarchy | 设置 scope 国家的社会等级制度 | set_social_hierarchy = <key> | country |  |
| set_state_name | 将 scope 州的名称设置为一个本地化字符串 | set_state_name = STATE_KIEV_ukrainian | state |  |
| set_state_owner | 设置州所有者 | set_state_owner = scope | state | country |
| set_state_religion | 将该国家的国教更改为指定宗教 | set_state_religion = <religion_scope | country | religion |
| set_state_type | 将一个州设置为特定类型（已合并、未合并、条约港） |  | state |  |
| set_strategy | 为 scope 国家设置 AI 战略 | set_strategy = <key> | country |  |
| set_subsidized | 设置一个建筑是否受补贴 | set_subsidized = yes/no | building |  |
| set_suppression | 开始/停止压制 scope 中的政治运动 | set_suppression = yes/no | political_movement |  |
| set_target_technology | 为一个日志条目设置（新的）目标技术 scope | set_target_technology = <scope> | journal_entry |  |
| set_tax_level | 设置 scope 国家的总体税收等级 | set_tax_level = very_low/low/medium/high/very_high | country |  |
| set_tension | 设置两个国家之间的紧张度 | set_tension = { country = country scope/tag value = amount } | country |  |
| set_variable | 设置一个变量 | set_variable = { name = <variable name> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } 该变量可通过 var:<variable name> 从其被设置的 scope 中访问。也可用作 set_variable = X（等价于 set_variable = { name = X value = yes }） | none |  |
| set_war | 将一个外交博弈设为战争 | set_war = bool | diplomatic_play |  |
| show_as_tooltip | 包含的 effect 仅在提示框中显示（但不会实际执行） | show_as_tooltip = { <more effects> } | none |  |
| sort_global_variable_list | 对一个全局变量列表排序 | sort_global_variable_list = { name = <global variable> order = <math script> } | none |  |
| sort_local_variable_list | 对一个局部变量列表排序 | sort_local_variable_list = { name = <local variable> order = <math script> } | none |  |
| sort_variable_list | 对一个变量列表排序 | sort_variable_list = { name = <variable name> order = <math script> } | none |  |
| spawn_entity_effect | 在 scope 州区域中心生成一个持续若干秒的临时实体 | spawn_entity_effect = { name = "entity_type" duration = X = true, } | state_region |  |
| start_building_construction | 在 scope 州中开始作为政府建设建造一个建筑 | start_building_construction = building_barracks | state |  |
| start_earthquake_effect | 以 scope 州区域为中心开始地震镜头震动 | start_earthquake_effect = yes | state_region |  |
| start_enactment | 为 scope 国家开始制定指定的法律类型 | start_enactment = law_type:law_multicultural | country | law_type |
| start_harvest_condition | 在 scope 州区域中开始某一类型的收成状况（若已存在则刷新） | start_harvest_condition = <key> | state_region |  |
| start_harvest_condition_with_params | 在 scope 州区域中开始某一类型的收成状况，可选择提供强度和持续时间（以天计） | start_harvest_condition_with_params = { type = flood intensity = 5 (optional) duration = 5 (optional) } | state_region |  |
| start_national_awakening | 开始一次文化觉醒 | start_national_awakening = { culture = cu:british # the culture that will have a national awakening months = 12 # the number of months the awakening will last for state_region = s:STATE_HOME_COUNTIES # optional, if not specified the state region with the highest literacy rate of the culture is used } | country |  |
| start_privately_funded_building_construction | 在 scope 州中开始作为私人建设建造一个建筑 | start_privately_funded_building_construction = building_barracks | state |  |
| start_research_random_technology | scope 国家开始研究其可研究的任意随机技术 | start_research_random_technology = yes | country |  |
| start_tutorial_lesson | 以给定 key 开始教程课程。若教程未运行、课程已完成（或已在运行），或课程无法触发（例如 trigger 失败），则不做任何事 |  | none |  |
| switch | 依据一个 trigger 的判定结果来执行相应 effect，并可选一个 fallback trigger | switch = { trigger = simple_assign_trigger case_1 = { <effects> } case_2 = { <effects> } case_n = { <effects> } fallback = { <effects> } | none |  |
| take_on_scaled_debt | 转移相当于目标最大信贷额度指定乘数比例的债务 | take_on_scaled_debt = { who = <country scope> value = <0-1 value> } | country |  |
| teleport_to_front | 将 scope 编队传送到目标前线 | teleport_to_front = p:xFAFAFA.front 也可接受 base_camp 参数，将使用给定省份搜索最近且相连的大本营 teleport_to_front = { front = p:xFAFAFA.front base_camp = p:xFAFAFA = true, } | military_formation | front |
| transfer_character | 将当前 scope 人物转移到目标国家 | transfer_character = country | character | country |
| transfer_subject | 将附属国从另一个国家转移到当前 scope 国家 | transfer_subject = scope | country | country |
| transfer_to_formation | 将 scope 人物转移到目标编队 | transfer_to_formation = scope:formation | character | military_formation |
| trigger_event | 为当前 scope 触发一个事件 | trigger_event = <event id> trigger_event = { id = <event id> days/weeks/months/years = <integer value> popup = yes (optional) } | none |  |
| try_form_government_with | 尝试以给定的利益集团组建新政府，若在给定合法性下不可行，将尽量把尽可能多的利益集团纳入政府 | try_form_government_with = { value = 30 interest_group_type = ig_armed_forces interest_group_type = ig_devout interest_group_type = ig_landowners } | country |  |
| unset_available_for_autonomous_investment | 在当前 scope 州中将一种建筑类型设为不可用于自主投资 | unset_available_for_autonomous_investment = building type scope | state | building_type |
| unset_only_legal_party | 使国家恢复为非一党制国家状态，只要其他法律允许，多个政党可以并存 | unset_only_legal_party = yes | country |  |
| update_party_support | 更新 scope 国家的政党支持度。 | update_party_support = yes | country |  |
| validate_subsidies | 校验一个国家所有建筑的补贴。原版游戏无使用 | validate_subsidies = bool | country |  |
| violate_sovereignty_join | scope 国家加入侵犯方或目标方的战争一方 | violate_sovereignty_accept = { violator = <country scope> target = <country scope> join_violator = yes/no } | country |  |
| while | 在满足 limit 条件时重复执行包含的 effect，或直至达到设定的迭代次数 | while = { limit = { <triggers> } <effects> } while = { count = <integer> <effects> } 默认上限为 1000。 | none |  |
| withdraw | 使一个国家退出条约 | scope:treaty = { withdraw = { country = <country scope> # must be valid and must be bound by the treaty apply_break_penalties = yes/no # optional, default no. If yes, break effects and on-actions apply when treaty is in binding time } } | treaty |  |
## 参考资料

---

- 要更新这些表格，请参见 [Module:Script docs/Effects](https://vic3.paradoxwikis.com/Module:Script_docs/Effects)

Modding（模组制作）
返回顶部
| 文档 | [Defines](Defines.md) • Effects • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
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

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|