---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Interest group modding
source: https://vic3.paradoxwikis.com/Interest_group_modding
pageid: 3651
categories: [Potentially_outdated, 1.11, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。其中至少部分内容最后核实于 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.11。

参见：
利益集团
**利益集团**（常缩写为 IG）代表共同的社会政治利益。每个利益集团拥有若干意识形态、三个特质以及其他一些特征。

## 定义示例

利益集团定义于 common/interest_groups 中。

利益集团定义示例：
```
ig_example = {
	color = hsv{ 0.09 0.29 0.39 } # HSV for IG icon
	texture = "gfx/interface/icons/ig_icons/armed_forces.dds" # Texture for IG icon
	layer = "revolution_dynamic_armed_forces" #refers to map graphics for revolutions
    index = 0 #relative ordering of IG, 0-indexed should be unique
    
	ideologies = { # Base ideologies for this IG
		ideology_jingoist
		ideology_loyalist
		ideology_patriotic
	}

	character_ideologies = { #default ideologies avaiable to characters affiliated with this IG
		ideology_moderate
		ideology_orleanist
		ideology_bonapartist
	}
    
	enable = {  #Country scope, checks monthly, enables IG when true, disables it when false
		# enable allows for setting a condition to enable an IG for specific countries and under certain condition
		# 
		# by default it is set to always = yes for all IGs in basegame.
		#
		# A note about triggers is that any trigger which is a dynamic condition (such as army_size = 10)
		# will not be checked until the first month of the game ends.
		#
		# Some of your IGs may thus be missing at game-start.
		# 
		always = yes
	}
    
	# Deprecated; use on_enable effect to assign traits instead
	traits = {  # IG traits provide a bonus or malus depending on the IG approval. Definitions go in common/interest_group_traits
		ig_trait_patriotic_fervor
		ig_trait_veteran_consultation
		ig_trait_materiel_waste
	}	
	
	on_enable = {} #Country scope, fires when an IG is enabled
	on_disable = {} #Country scope, fires when an IG is no longer enabled, because the enable trigger evaluated to false.
    
	priority_cultures = { #sets cultures for generated characters affiliated with this IG, defaults to primary cultures of country otherwise
		rule = { #Repeat block for each set of rules (different culture lists)
			trigger = { #Country scope
				<triggers>
			}
			cultures = {
				<list of culture keys>
			}
		}
	}
    
	on_character_ig_membership = { # Triggered when a major character becomes an IG member.
		change_character_religion = scope:interest_group.owner.religion
	} 
	
	pop_potential = { #Pop scope, Defines which pops are ALLOWED TO join the IG
		OR = {
			is_pop_type = soldiers
			is_pop_type = officers
			is_pop_type = aristocrats
			pop_is_discriminated = no
		}		
	}
	
	pop_weight = { #Pop scope, defines the likelihood (weight) certain pops are to join the IG; uses script values
		value = 0
		
		add = {
			desc = "POP_NOT_DISCRIMINATED"
			if = {
				limit = { 
					pop_is_discriminated = no
				}
				value = 25
			}
		}		
		
		add = {
			desc = "POP_SOLDIERS"
			if = {
				limit = { 
					is_pop_type = soldiers
				}
				value = 100
			}
		}
		
		add = {
			desc = "POP_ARISTOCRATS"
			if = {
				limit = { 
					is_pop_type = aristocrats
				}
				value = 50
			}
		}		
	
		add = {
			desc = "POP_OFFICERS"
			if = {
				limit = { 
					is_pop_type = officers
				}
				value = 200
			}
		}
					
		multiply = {
			desc = "LEADER_POPULARITY"
			scope:interest_group = {
				leader = {
					value = popularity
					multiply = 0.0025
					add = 1
					max = 1.25
					min = 0.75
				}
			}
		}	
	}
	
    # Character weights are the likelihood (weight, multiplied by clout) that this type of character is affiliated with the IG; uses script values
	monarch_weight = { #IG scope, for monarch or heir
		value = 0.25
	}
	
	commander_weight = { #? scope, for general or admiral
		value = 5.0
	}

	agitator_weight = { #Character scope
		value = 0.0
	}
    
	executive_weight = { #? scope
		value = 0.0
	}
	
	noble_chance = { #chance that character uses a noble name rather than a common name
		value = 0.5
	}
	
	female_commander_chance = { #chance of female character in this role
		value = 0.0
	}
	
	female_politician_chance = { #chance of female character in this role
		value = 0.0
	}

	female_executive_chance = { #chance of female character in this role
		value = 0.0
	}
	
	# The chance that a commander belonging to this IG takes over leadership when it changes
	# scope:character is the most popular commander in the IG
	commander_leader_chance = {
		value = 0.75
		if = {
			limit = {
				exists = scope:character
			}
			multiply = {
				value = 1
				add = scope:character.popularity
				min = 0
			}
		}
	}
    # The chance that a executive belonging to this IG takes over leadership when it changes
	# scope:character is the most popular executive in the IG
	executive_leader_chance = {
		value = 0.1
	}
}
```

## 利益集团特质

利益集团特质定义于 common/interest_group_traits 中。它们由脚本名称、图标、最低认可度以及一个 [modifier](Modifier types.md)（游戏内修正脚本）块组成。

```
ig_trait_patriotic_fervor = {
	icon = "gfx/interface/icons/ig_trait_icons/patriotic_fervor.dds"
	min_approval = loyal

	modifier = {
		unit_offense_mult = 0.1
		unit_defense_mult = 0.1
	}
}

ig_trait_veteran_consultation = {
	icon = "gfx/interface/icons/ig_trait_icons/veteran_consultation.dds"
	min_approval = happy

	modifier = {
		country_military_tech_research_speed_mult = 0.1
	}
}

ig_trait_materiel_waste = {
	icon = "gfx/interface/icons/ig_trait_icons/materiel_waste.dds"
	max_approval = unhappy

	modifier = {
		country_military_goods_cost_mult = 0.15
	}
}
```

## 利益集团脚本文档

以下 [effect](Effect.md)（游戏内效果脚本）、[event target](Event target.md)（事件目标）和 [trigger](Trigger.md)（游戏内条件脚本）可用于利益集团 scope（作用域）。

| effect | 说明 | 示例 | 目标 |
|---|---|---|---|
| abandon_revolution | 将利益集团从革命中移除 | abandon_revolution = yes/no |  |
| add_ideology | 为 scope 中的利益集团添加一个意识形态 | add_ideology = ideology:<ideology key> |  |
| add_modifier | 为 scope 中的对象添加限时修正效果 | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_ruling_interest_group | 将利益集团加入政府 | add_ruling_interest_group = yes/no |  |
| every_political_lobby | 遍历国家或利益集团中的所有政治游说团 | every_political_lobby = { limit = { <triggers> } #optional <effects> } | political_lobby |
| every_preferred_law | 按偏好程度排序，遍历利益集团所在国家所有已生效及可能的法律 | every_preferred_law = { limit = { <triggers> } #optional <effects> } | law |
| every_scope_admiral | 遍历以下 scope 中的所有海军上将：国家、利益集团或军事编队 | every_scope_admiral = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_character | 遍历以下 scope 中的所有人物：国家、利益集团或前线 | every_scope_character = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_general | 遍历以下 scope 中的所有将军：国家、利益集团、前线或军事编队 | every_scope_general = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_politician | 遍历以下 scope 中的所有政客：国家或利益集团 | every_scope_politician = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_pop | 遍历以下 scope 中的所有人口：国家、州、利益集团、文化 | every_scope_pop = { limit = { <triggers> } #optional <effects> } | pop |
| join_revolution | 将利益集团加入正在进行的革命 | join_revolution = yes/no |  |
| ordered_political_lobby | 遍历国家或利益集团中的所有政治游说团 | ordered_political_lobby = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_lobby |
| ordered_preferred_law | 按偏好程度排序，遍历利益集团所在国家所有已生效及可能的法律 | ordered_preferred_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | law |
| ordered_scope_admiral | 遍历以下 scope 中的所有海军上将：国家、利益集团或军事编队 | ordered_scope_admiral = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_character | 遍历以下 scope 中的所有人物：国家、利益集团或前线 | ordered_scope_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_general | 遍历以下 scope 中的所有将军：国家、利益集团、前线或军事编队 | ordered_scope_general = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_politician | 遍历以下 scope 中的所有政客：国家或利益集团 | ordered_scope_politician = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_pop | 遍历以下 scope 中的所有人口：国家、州、利益集团、文化 | ordered_scope_pop = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | pop |
| random_political_lobby | 遍历国家或利益集团中的所有政治游说团 | random_political_lobby = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_lobby |
| random_preferred_law | 按偏好程度排序，遍历利益集团所在国家所有已生效及可能的法律 | random_preferred_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | law |
| random_scope_admiral | 遍历以下 scope 中的所有海军上将：国家、利益集团或军事编队 | random_scope_admiral = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character |
| random_scope_character | 遍历以下 scope 中的所有人物：国家、利益集团或前线 | random_scope_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character |
| random_scope_general | 遍历以下 scope 中的所有将军：国家、利益集团、前线或军事编队 | random_scope_general = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character |
| random_scope_politician | 遍历以下 scope 中的所有政客：国家或利益集团 | random_scope_politician = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character |
| random_scope_pop | 遍历以下 scope 中的所有人口：国家、州、利益集团、文化 | random_scope_pop = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | pop |
| remove_ideology | 从 scope 中的利益集团移除一个意识形态 | remove_ideology = ideology:<ideology key> |  |
| remove_modifier | 移除 scope 中对象的限时修正效果 | remove_modifier = static_modifier_name |  |
| remove_ruling_interest_group | 将 scope 中的利益集团从政府中移除 | remove_ruling_interest_group = yes/no |  |
| set_ig_trait | 为利益集团添加一个特质，或替换其当前具有相同认可度等级的特质 | set_ig_trait = ig_trait:ig_trait_engines_of_progress | interest_group_trait |
| set_interest_group_name | 将利益集团重命名为指定的本地化键名 | set_interest_group_name = x |  |

| trigger | 说明 | 示例 | 目标 |
|---|---|---|---|
| any_political_lobby | 遍历国家或利益集团中的所有政治游说团 | any_political_lobby = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_lobby |
| any_preferred_law | 按偏好程度排序，遍历利益集团所在国家所有已生效及可能的法律 | any_preferred_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | law |
| any_scope_admiral | 遍历以下 scope 中的所有海军上将：国家、利益集团或军事编队 | any_scope_admiral = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_character | 遍历以下 scope 中的所有人物：国家、利益集团或前线 | any_scope_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_general | 遍历以下 scope 中的所有将军：国家、利益集团、前线或军事编队 | any_scope_general = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_politician | 遍历以下 scope 中的所有政客：国家或利益集团 | any_scope_politician = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_pop | 遍历以下 scope 中的所有人口：国家、州、利益集团、文化 | any_scope_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | pop |
| has_ideology | 检查 scope 中的人物或利益集团是否拥有某意识形态 |  |  |
| has_modifier | 检查受支持的 scope 是否拥有某个限时修正 | has_modifier = <key> |  |
| has_party | 若利益集团 scope 拥有政党则为真 | has_party = bool | boolean |
| ig_approval | 与 scope 中利益集团的认可度比较 | ig_approval > 2 ig_approval < happy | value |
| ig_clout | 与 scope 中利益集团的政治力量比较 | ig_clout >= 0.2 | value |
| ig_government_power_share | 与 scope 中利益集团的政治力量除以政府总政治力量的份额比较 | ig_government_power_share >= 0.5 | value |
| interest_group_population | 比较利益集团中的人口数量 | interest_group_population > 1000 | value |
| interest_group_population_percentage | 比较利益集团中人口的百分比 | interest_group_population_percentage > 0.2 | value |
| interest_group_supports_political_movement | 检查 scope 中的利益集团是否支持某个政治运动 | interest_group_supports_political_movement = yes/no | boolean |
| is_in_government | 若利益集团 scope 在政府中则为真 | is_in_government = bool | boolean |
| is_insurrectionary | 检查国家、运动或利益集团是否处于叛乱状态 |  | boolean |
| is_interest_group_type | 检查利益集团是否属于某种类型，也可直接用于人物 | is_interest_group_type = x |  |
| is_marginal | 若利益集团 scope 处于边缘化状态则为真 | is_marginal = bool | boolean |
| is_member_of_any_lobby | 检查利益集团是否是任意游说团的成员 | is_member_of_any_lobby = yes | boolean |
| is_member_of_lobby | 检查利益集团是否是某种游说团类型的成员 | is_member_of_lobby = lobby_type:pro_country_lobby | political_lobby_type |
| is_member_of_party | 检查利益集团是否是目标政党的成员 | is_member_of_party = <party> | party |
| is_powerful | 若利益集团 scope 具有影响力则为真 | is_powerful = bool | boolean |
| is_revolutionary | 检查国家、运动或利益集团是否处于革命状态 |  | boolean |
| is_same_interest_group_type | 检查利益集团是否与目标属于同一利益集团类型 | is_interest_group_type = scope:neighbor_leading_ig | interest_group |
| is_secessionist | 检查国家、运动或利益集团是否处于分离主义状态 |  | boolean |
| is_strongest_ig_in_government | 检查 scope 中的利益集团在政府所有利益集团中是否拥有最高的政治力量 | is_strongest_ig_in_government = yes/no | boolean |
| law_enactment_stance | 比较 scope 中的人物、运动或利益集团对制定指定法律（相对于同法律组中当前已生效法律）的立场 |  |  |
| law_stance | 比较 scope 中的人物、运动或利益集团对指定法律的基础立场（忽略同法律组中当前已生效的法律） |  |  |
| most_powerful_strata | 比较利益集团中最强大的阶层 |  |  |
| num_political_lobbies | 与 scope 中国家或利益集团的政治游说团数量比较 | num_political_lobbies > 0 | value |
| prefers_law | 检查 scope 中的利益集团是否相较于比较法律更偏好指定法律 | prefers_law = { law = law_type:<law a> comparison_law = law_type:<law b> } |  |
| 事件目标 | 描述 | 目标 scope |
|---|---|---|
| average_progressiveness | 获取当前 scope 中人物或利益集团的平均进步度 | value |
| leader | 转到该利益集团的领袖 | character |
| lobby_join_weight | 转到利益集团加入特定游说集团的权重（lobby_join_weight:root >= 5） | value |
| modifier | 转到当前对象所属指定键的 modifier 类型数值，例如：modifier:country_influence_add | boolean, value |
| owner | 转到该对象的所有者国家 | country |
| party | 转到该利益集团支持的政党 | party |
| type | 从对象转到其类型 | amendment_type, building_type, company_type, diplomatic_play_type, harvest_condition_type, institution_type, interest_group_type, law_type, political_movement_type, ship_type, strait_type |

### 利益集团 modifier 类型

`interest_group_` [modifier 类型](Modifier types.md)将其效果作用于利益集团。当作用于国家时，会应用于该国所有利益集团。

| Modifier 类型 | 本地化文本 | 类型 | 格式 | 备注 |
|---|---|---|---|---|
| interest_group_amenability_add | 利益集团顺从度 | additive | good |  |
| interest_group_approval_add | 利益集团支持度 | additive | good |  |
| interest_group_ig_armed_forces_approval_add | 军队支持度 | additive | good |  |
| interest_group_ig_armed_forces_pol_str_mult | 军队政治力量 | multiplicative | percent, neutral |  |
| interest_group_ig_armed_forces_pop_attraction_mult | 军队人口吸引力 | multiplicative | percent, neutral |  |
| interest_group_ig_devout_approval_add | 虔信派支持度 | additive | good |  |
| interest_group_ig_devout_pol_str_mult | 虔信派政治力量 | multiplicative | percent, neutral |  |
| interest_group_ig_devout_pop_attraction_mult | 虔信派人口吸引力 | multiplicative | percent, neutral |  |
| interest_group_ig_industrialists_approval_add | 实业家支持度 | additive | good |  |
| interest_group_ig_industrialists_pol_str_mult | 实业家政治力量 | multiplicative | percent, neutral |  |
| interest_group_ig_industrialists_pop_attraction_mult | 实业家人口吸引力 | multiplicative | percent, neutral |  |
| interest_group_ig_intelligentsia_approval_add | 知识分子支持度 | additive | good |  |
| interest_group_ig_intelligentsia_pol_str_mult | 知识分子政治力量 | multiplicative | percent, neutral |  |
| interest_group_ig_intelligentsia_pop_attraction_mult | 知识分子人口吸引力 | multiplicative | percent, neutral |  |
| interest_group_ig_landowners_approval_add | 地主支持度 | additive | good |  |
| interest_group_ig_landowners_pol_str_mult | 地主政治力量 | multiplicative | percent, neutral |  |
| interest_group_ig_landowners_pop_attraction_mult | 地主人口吸引力 | multiplicative | percent, neutral |  |
| interest_group_ig_petty_bourgeoisie_approval_add | 小资产阶级支持度 | additive | good |  |
| interest_group_ig_petty_bourgeoisie_pol_str_mult | 小资产阶级政治力量 | multiplicative | percent, neutral |  |
| interest_group_ig_petty_bourgeoisie_pop_attraction_mult | 小资产阶级人口吸引力 | multiplicative | percent, neutral |  |
| interest_group_ig_rural_folk_approval_add | 乡民支持度 | additive | good |  |
| interest_group_ig_rural_folk_pol_str_mult | 乡民政治力量 | multiplicative | percent, neutral |  |
| interest_group_ig_rural_folk_pop_attraction_mult | 乡民人口吸引力 | multiplicative | percent, neutral |  |
| interest_group_ig_trade_unions_approval_add | 工会支持度 | additive | good |  |
| interest_group_ig_trade_unions_pol_str_mult | 工会政治力量 | multiplicative | percent, neutral |  |
| interest_group_ig_trade_unions_pop_attraction_mult | 工会人口吸引力 | multiplicative | percent, neutral |  |
| interest_group_in_government_approval_add | 政府利益集团支持度 | additive | good |  |
| interest_group_in_government_attraction_mult | 政府中利益集团的吸引力 | multiplicative | percent, neutral |  |
| interest_group_in_opposition_agitator_popularity_add | 反对派鼓动家声望 | additive | good |  |
| interest_group_in_opposition_approval_add | 反对派利益集团支持度 | additive | good |  |
| interest_group_pol_str_factor | 利益集团政治力量 | multiplicative | percent, good |  |
| interest_group_pol_str_mult | 利益集团政治力量 | multiplicative | percent, neutral |  |
| interest_group_pop_attraction_mult | 利益集团人口吸引力 | multiplicative | percent, neutral |  |

### 利益集团 GUI 脚本

主条目：
GUI 脚本
| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessAllIdeologies |  | Unknown | 类别： const |
| AccessCheapestLawsToPass |  | Unknown | 类别： const |
| AccessCountry |  | Country | 类别： const |
| AccessIntrinsicIdeologies |  | Unknown | 类别： const |
| AccessLeader |  | Character | 类别： const |
| AccessModifier |  | Modifier | 类别： const |
| AccessSelf |  | InterestGroup | 类别： const |
| AccessTraits |  | Unknown | 类别： const |
| CalcApprovalFromLoyalties |  | int32 |  |
| CalcApprovalFromLoyaltiesDesc |  | CString |  |
| GetAffiliationBreakdown |  | CString | 类别： nonconst |
| GetAffiliationBreakdownForParty | Party | CString | 类别： nonconst |
| GetAffiliationRaw |  | CFixedPoint | 类别： nonconst |
| GetAgitators |  | Unknown | 类别： nonconst |
| GetAmenability |  | CFixedPoint | 类别： nonconst |
| GetAmenabilityLabel |  | CString | 类别： nonconst |
| GetApprovalRating |  | CString | 类别： nonconst |
| GetApprovalValue |  | int32 | 类别： nonconst |
| GetApprovalValueDecayIfEnactedDesc | LawType | CString | 类别： nonconst |
| GetApprovalValueDeltaFromEnactment | LawType | int32 | 类别： nonconst |
| GetApprovalValueDesc |  | CString | 类别： nonconst |
| GetApprovalValueIfEnacted | LawType | int32 | 类别： nonconst |
| GetClout |  | CFixedPoint | 类别： nonconst |
| GetCloutAsFloat |  | float | 类别： nonconst |
| GetCloutSupportingMovement | PoliticalMovement | CFixedPoint | 类别： nonconst |
| GetCloutTrend |  | DataTrend | 类别： nonconst |
| GetColor |  | CVector4f | 类别： nonconst |
| GetCountry |  | Country | 类别： nonconst |
| GetCountrySupport |  | CFixedPoint | 类别： nonconst |
| GetCustom | CustomLocalization | CString | 类别： nonconst |
| GetDesc |  | CString | 类别： nonconst |
| GetFractionOfCloutSupportingMovement | PoliticalMovement | CFixedPoint | 类别： nonconst |
| GetGraphicalLoyalistsRatioInAllInterestGroups |  | float | 类别： nonconst |
| GetGraphicalRadicalsRatioInAllInterestGroups |  | float | 类别： nonconst |
| GetID |  | uint32 | 类别： nonconst |
| GetIdeologyDesc |  | CString | 类别： nonconst |
| GetInfluenceDesc |  | CString | 类别： nonconst |
| GetInfluenceReason |  | CString | 类别： nonconst |
| GetInfluencingMovements |  | Unknown | 类别： nonconst |
| GetLawApprovalBreakdown | Law | CString | 类别： nonconst |
| GetLawApprovalValue | Unknown | int32 | 类别： nonconst |
| GetLawStanceLabel | LawType | CString | 类别： nonconst |
| GetLeader |  | Character | 类别： nonconst |
| GetLeaderIdeology |  | Ideology | 类别： nonconst |
| GetLeaderIdeologyDesc |  | CString | 类别： nonconst |
| GetLoyalistsPoliticalStrength |  | int64 | 类别： nonconst |
| GetLoyalistsTrend |  | DataTrend | 类别： nonconst |
| GetModifier |  | Modifier | 类别： nonconst |
| GetName |  | CString | 类别： nonconst |
| GetNameNoFormatting |  | CString | 类别： nonconst |
| GetNameNoIcon |  | CString | 类别： nonconst |
| GetNameWithCountryVariant |  | CString | 类别： nonconst |
| GetNumLoyalists |  | int64 | 类别： nonconst |
| GetNumLoyalistsRatio |  | float | 类别： nonconst |
| GetNumNeutrals |  | int64 | 类别： nonconst |
| GetNumNeutralsRatio |  | float | 类别： nonconst |
| GetNumPossibleLeaderIdeologies |  | int32 | 类别： nonconst |
| GetNumRadicals |  | int64 | 类别： nonconst |
| GetNumRadicalsRatio |  | float | 类别： nonconst |
| GetNumSupportersForMovement | PoliticalMovement | int64 | 类别： nonconst |
| GetParty |  | Party | 类别： nonconst |
| GetPartyAffiliationHighest |  | Party | 类别： nonconst |
| GetPartyAffiliationTooltip |  | CString | 类别： nonconst |
| GetPoliticalLobbies |  | Unknown | 类别： nonconst |
| GetPoliticalStrength |  | int64 | 类别： nonconst |
| GetPoliticalStrengthDesc |  | CString | 类别： nonconst |
| GetPoliticalStrengthInState | State | int64 | 类别： nonconst |
| GetPoliticalStrengthInStateAsPercentage | State | CFixedPoint | 类别： nonconst |
| GetPoliticallyActivePercentage |  | CFixedPoint | 类别： nonconst |
| GetPoliticallyActiveRaw |  | int64 | 类别： nonconst |
| GetPopPotentialDesc |  | CString | 类别： nonconst |
| GetPopWithIG | Unknown | PopWithIG | 类别： nonconst |
| GetPopulation |  | int64 | 类别： nonconst |
| GetPopulationAsFloat |  | float | 类别： nonconst |
| GetPopulationInCountryAsPercentage |  | CFixedPoint | 类别： nonconst |
| GetPopulationInState | State | int64 | 类别： nonconst |
| GetPopulationNonZero |  | int64 | 类别： nonconst |
| GetPossibleCharacterLeaderIdeologies |  | Unknown | 类别： nonconst |
| GetPossibleRandomLeaderIdeologies |  | Unknown | 类别： nonconst |
| GetRadicalsPoliticalStrength |  | int64 | 类别： nonconst |
| GetRadicalsTrend |  | DataTrend | 类别： nonconst |
| GetStatusTooltip |  | CString | 类别： nonconst |
| GetSupportingPopTypesDesc |  | CString | 类别： nonconst |
| GetTextIcon |  | CString | 类别： nonconst |
| GetTexture |  | Unknown | 类别： nonconst |
| GetTooltipTag |  | CString | 类别： nonconst |
| GetTotalPoliticalStrengthIncludingPartyVotes |  | int64 | 类别： nonconst |
| GetTraitsDesc |  | CString | 类别： nonconst |
| GetWillJoinPartyDesc |  | CString | 类别： nonconst |
| GetWillJoinPartyTooltip |  | CString | 类别： nonconst |
| HasNegotiated |  | bool |  |
| HasParty |  | bool |  |
| IsEndorsingLawEnactment | Unknown | bool |  |
| IsInGovernment |  | bool |  |
| IsIndifferentToLawEnactment | Unknown | bool |  |
| IsInfluencedByMovement | Unknown | bool |  |
| IsInsurrectionary |  | bool |  |
| IsLeaderInfluencingEnactment | LawType | bool |  |
| IsLeadingGovernment |  | bool |  |
| IsMarginal |  | bool |  |
| IsNegotiating |  | bool |  |
| IsOpposingLawEnactment | Law | bool |  |
| IsPinnedInOutliner |  | bool |  |
| IsPowerful |  | bool |  |
| IsRevolutionary |  | bool |  |
| IsSecessionist |  | bool |  |
| IsValid |  | bool |  |
| MakeScope |  | Scope |  |
| PredictLegitimacyChangeDesc |  | CString |  |
| PredictLegitimacyChangeToSwitch |  | CFixedPoint |  |
| Self |  | InterestGroup |  |
| TogglePinInOutliner |  | void |  |
| WillRadicalizeIfEnacted | LawType | bool |  |

| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessSelf |  | InterestGroupTrait | 类别： const |
| GetBaseModifiersDesc |  | CString | 类别： nonconst |
| GetBaseTriggersDesc |  | CString | 类别： nonconst |
| GetCustom | CustomLocalization | CString | 类别： nonconst |
| GetDesc |  | CString | 类别： nonconst |
| GetInactiveString | InterestGroup | CString | 类别： nonconst |
| GetModifiersDesc | InterestGroup | CString | 类别： nonconst |
| GetName | InterestGroup | CString | 类别： nonconst |
| GetNameNoFormatting |  | CString | 类别： nonconst |
| GetNameWithStatus | Unknown | CString | 类别： nonconst |
| GetTexture |  | Unknown | 类别： nonconst |
| GetTooltipTag |  | CString | 类别： nonconst |
| GetTriggersDesc | InterestGroup | CString | 类别： nonconst |
| IsEnabled | InterestGroup | bool |  |
| MakeScope |  | Scope |  |
| Self |  | InterestGroupTrait |  |

| Promote | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessCountry |  | Country | 类别： const |
| AccessLeader |  | Character | 类别： const |
| AccessModifier |  | Modifier | 类别： const |
| GetCountry |  | Country | 类别： nonconst |
| GetLeader |  | Character | 类别： nonconst |
| GetLeaderIdeology |  | Ideology | 类别： nonconst |
| GetModifier |  | Modifier | 类别： nonconst |
| GetParty |  | Party | 类别： nonconst |
| GetPartyAffiliationHighest |  | Party | 类别： nonconst |
| GetPopWithIG | Pop | PopWithIG | 类别： nonconst |
| MakeScope |  | Scope |  |

| Promote | 参数 | 输出 | 描述 |
|---|---|---|---|
| MakeScope |  | Scope |  |

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [事件目标](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier 类型](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本化内容 | [决议](Decision modding.md) • [事件](Event modding.md) • [历史](History modding.md) • [日志](Journal modding.md) • [Modifiers](Modifier modding.md) • 目标 • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本化类型 | [建筑](Building modding.md) • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • 利益集团 • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [可自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图片](Event images.md) • [图形资产](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [音效](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod 兼容性](Mod compatibility.md) • [Mod 结构](Mod structure.md) • [脚本化测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [Mod 翻译](Mod translation.md) • [新国家 Mod 制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州 Mod 制作指南](State modding guide.md) |
|---|---|