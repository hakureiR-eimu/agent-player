---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Power bloc modding
source: https://vic3.paradoxwikis.com/Power_bloc_modding
pageid: 6891
categories: [Potentially_outdated, 1.10, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。至少部分内容最后针对 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10 进行过验证。

参见：
强权集团
[强权集团](Power bloc.md) 代表国际组织、联盟与帝国。每个强权集团都有一个*核心认同*（central identity）和若干*原则*（principle）。为强权集团和原则做模组（mod）通常需要修改若干相关概念。

## DLC 锁定功能

强权集团有若干由 DLC 锁定的功能。这包括大多数未经修改的认同与原则，以及为一个强权集团添加多条原则的能力。Mod 不得解锁 DLC 锁定内容，因此任何修改或复制 DLC 锁定的强权集团内容的 mod 功能**必须**包含 trigger `has_dlc_feature = power_bloc_features` 来启用这些功能。某些原则或核心认同也可能或转而由特定 DLC 锁定，使用诸如 `has_dlc_feature = ep3_content` 的 trigger。

完全新增的认同、原则或其他与强权集团相关的新内容不需要这个 trigger，除非它们复制或依赖于已有的 DLC 锁定功能。

贸易联盟及其主要原则“对外贸易”和“内部贸易”*不*受 DLC 锁定，因此可以自由修改。

| 解锁强权集团功能的 DLC |
|---|
| **势力范围（Sphere of Influence）** |

## 核心认同定义

强权集团认同定义了强权集团的类型，并包含基础修正值和数值（如凝聚力）。

核心认同定义于 /Victoria 3/game/common/power_bloc_identities。基本定义包括一个脚本名、图标、背景以及若干 trigger、modifier 和 script value。例如：

```
identity_trade_league = {
	power_bloc_modifier = {
		power_bloc_customs_union_bool = yes
		power_bloc_mandate_progress_per_great_power_member_add = 10
		power_bloc_mandate_progress_per_major_power_member_add = 5
		power_bloc_mandate_progress_per_minor_power_member_add = 2
		power_bloc_mandate_progress_per_unrecognized_major_power_member_add = 2
		power_bloc_mandate_progress_per_unrecognized_regional_power_member_add = 1
		power_bloc_cohesion_per_member_add = -1
		power_bloc_invite_acceptance_great_power_add = -15
	}

	leader_modifier = {
		country_trade_route_quantity_mult = 0.1
	}
	
	non_leader_modifier = {
		country_convoy_contribution_to_market_owner_add = 0.2
	}

	member_modifier = {
	}

	can_leave = {
		OR = {
			is_power_bloc_leader = yes
			power_bloc = {
				leverage_advantage = {
					target = root
					value <= 30
				}
			}
		}
	}
	
	possible = {
		# NOT = { has_law = law_type:law_isolationism }
	}

	icon = "gfx/interface/icons/central_identity_pillars_icons/trade_league.dds"
	background = "gfx/interface/power_blocs/backgrounds/pb_background_generic.dds"

	mandate_progress = power_bloc_mandate_progress_by_rank
	
	on_created = { relations_hit_with_power_bloc_leaders = yes }
	
	cohesion = {
		[script value]
		add = {
			add = 0.15
			multiply = define:NPowerBlocs|COHESION_TARGET_MAX
			desc = POWER_BLOC_COHESION_BASE
		}
	}
	
	ai_weight = {
		[script value]
	}
}
```

脚本名可以是任意内容，并且脚本名还会生成 [localization](Localization.md) 键：`[script name]` 和 `[script_name]_desc`。认同会被用于 trigger 中，因此使用清晰但唯一的名称为佳。

可以为每个认同编写以下特性：

| 特性 | 描述 |
|---|---|
| icon | 代表该认同的图标 |
| background | 使用该认同时强权集团界面的背景图像 |
| visible | 必须返回 true 该认同才可见的 trigger 块 |
| possible | 必须返回 true 该认同才可被选择的 trigger 块 |
| can_leave | 必须返回 true 一国才能自愿离开强权集团的 trigger 块 |
| on_created | 该强权集团首次成立时执行的 effect 块 |
| power_bloc_modifier | 直接影响强权集团的修正值 |
| leader_modifier | 仅影响强权集团领导者的修正值 |
| non_leader_modifier | 仅影响强权集团中非领导者成员的修正值 |
| member_modifier | 影响强权集团所有成员的修正值 |
| mandate_progress | 决定获得指令（mandate）速度的 script value |
| cohesion | 决定该集团凝聚力目标的 script value |
| ai_weight | 决定 AI 最看重哪个认同的 script value |

## 原则组定义

强权集团原则是按组划分的，每个组代表一项原则，组内定义各个等级。原则组定义于 /Victoria 3/game/common/power_bloc_principle_groups。每个原则组需要一个脚本名和一个列出一条或多条原则的 `levels` 块。此外，还可以包含以下特性：

| 特性 | 描述 |
|---|---|
| unlocking_identity | 选择该原则组所需的认同 |
| blocking_identity | 无法选择该原则组的认同 |
| primary_for_identity | 该原则组是指定认同的主要原则 |

与认同一样，脚本名可以是任意内容，并生成 localization 键 `[script_name]` 和 `[script_name]_desc`

未经修改的《维多利亚3》中每个组始终且只使用三个等级，但这并不是严格的要求。每个条目被视为比前一个更高的等级，这会影响切换到该原则所需的指令数量。

原则组示例：

```
principle_group_internal_trade = {
	primary_for_identity = identity_trade_league
	unlocking_identity = identity_trade_league
	
	levels = {
		principle_internal_trade_1
		principle_internal_trade_2
		principle_internal_trade_3
	}
}
```

## 原则定义

原则定义于 /Victoria 3/game/common/power_bloc_principles。每条原则都有某些必需元素和若干可选元素。基本定义需要以下内容：一个脚本名、一个图标、一个背景以及一个 ai_weight trigger 块。

```
principle_internal_trade_1 = {
	icon = "gfx/interface/icons/principles_icons/internal_trade.dds"
	background = "gfx/interface/icons/principles_icons/principle_tier_1.dds"
	
	member_modifier = {
		# Members get a bonus to Company throughput
		country_company_throughput_bonus_add = 0.1
		# More convoy going to the market owner, effect scaling upwards with principle levels
		country_convoy_contribution_to_market_owner_add = 0.2
	}
	
	ai_weight = {
		value = 200 # Good for trade leagues to have
			
		if = {
			limit = { 
				OR = {
					has_law = law_type:law_mercantilism 
					has_law = law_type:law_command_economy
				}
			}
			add = 100
		}	

		if = {
			limit = { 
				power_bloc ?= { has_principle_group = principle_group:principle_group_external_trade }
			}
			multiply = 0.5
		}
	}	
}
```

原则继承其原则组的 localization，但仍会生成新的 desc `[script_name]_desc`。在未经修改的《维多利亚3》中，原则描述被设置为复用原则组描述，但如果需要，它们可以有自己独立的描述 localization。

原则具有以下特性：

| 元素 | 描述 |
|---|---|
| icon | 代表该原则的图标 |
| background | 该原则等级的背景图像 |
| visible | 必须返回 true 该原则才可见的 trigger 块 |
| possible | 必须返回 true 该原则才可被选择的 trigger 块 |
| power_bloc_modifier | 直接影响强权集团的修正值 |
| leader_modifier | 仅影响强权集团领导者的修正值 |
| non_leader_modifier | 仅影响强权集团中非领导者成员的修正值 |
| member_modifier | 影响强权集团所有成员的修正值 |
| ai_weight | 决定 AI 最看重哪个原则的 script value |
| institution | 受该原则影响的[机构](Institution modding.md) |
| institution_modifier | 由该原则添加到机构上的 modifier 块 |

### 原则槽位

原则槽位由 /Victoria 3/game/common/scripted_rules/00_scripted_rules.txt 中的 scripted rules 控制。每个槽位有两条规则 `unlock_power_bloc_principle_slot_#` 和 `unlock_power_bloc_formation_principle_slot_#`。每条规则接受一个 trigger 块来决定给定槽位能否使用。能否添加额外槽位尚不明确（注意这也需要图形方面的修改）。注意，使用第一个以外的槽位是 DLC 锁定功能，因此需要 `has_dlc_feature = power_bloc_features` 作为启用更多槽位的必要 trigger。

## 强权集团 script value

文件 /Victoria 3/game/common/script_values/01_power_bloc_values.txt 包含若干与强权集团相关的已定义 script value。例如，影响力杠杆（leverage）和指令获取的 script value 都定义于此，此外还有 AI 加入强权集团的接受度。

## 其他效果

强权集团认同和原则可以通过引用该认同或原则在其他文件中启用 effect 或行动。生产方式就是这样一个例子，某些原则可以启用替代的生产方式。

## 强权集团 defines

除可脚本化的特性外，还有若干 [defines](Defines.md) 控制强权集团的机制。

| Define | 默认值 | 开发者注释 |
|---|---|---|
| MAX_PRINCIPLES | 4 | # Max number of principles that a Power Bloc can have |
| INITIAL_PRINCIPLE_LEVELS | 1 | # Max total levels of principles that a Power Bloc can have during formation |
| FORMATION_COOLDOWN_MONTHS | 24 | # Cooldown in months between the attempts to form Power Blocs |
| JOIN_COOLDOWN_MONTHS | 6 | # If a Country leaves a Power Bloc they cannot re-join before X months |
| LEAVE_COOLDOWN_MONTHS | 6 | # If a Country joins a Power Bloc they cannot leave within X months |
| MIN_MEMBERS | 2 | # This is the minimum number of members that the bloc needs to have to be considered active. Members include the leader. |
| LEVERAGE_LOBBY_CLOUT_FACTOR | 500 | # Leverage gain is increased or decreased by the Lobby's total Clout * this factor |
| INVITE_ACTION_NAME | "invite_to_power_bloc" |  |
| JOIN_ACTION_NAME | "join_power_bloc" |  |
| MAX_MANDATE_PROGRESS | 2000 | # When mandate progress reaches this value, the power bloc gains one mandate |
| MAX_MANDATES | 3 | # This is the maximum number of mandates that can be accumulated at once |
| PRINCIPLE_SELECTION_COOLDOWN_DAYS | 90 | # Once a principle is selected, it cannot be changed for this many days. Upgrading is unaffected by the cooldown, but resets it. |
| POWER_STRUGGLE_PRESTIGE_THRESHOLD_START | 1.2 | # If a power bloc member has more prestige than leader's prestige X this - power struggle starts with the member becoming contender |
| POWER_STRUGGLE_PRESTIGE_THRESHOLD_FAIL | 1.15 | # If a contender has less prestige than leader's prestige X this - power struggle fails |
| POWER_STRUGGLE_DURATION_SUCCESS_MONTHS | 12 | # Power struggle succeeds after this months |
| POWER_STRUGGLE_DURATION_FACTOR_FOR_FOUNDER | 0.75 | # Power struggle succeeds after this X POWER_STRUGGLE_DURATION_SUCCESS_MONTHS if the contender is the founder of the power bloc |
| COHESION_WEEKLY_DRIFT_MAX | 1 | # At most, Cohesion will drift by +/- this value each week |
| COHESION_TARGET_MAX | 100 | # The highest value Cohesion can reach |
| POWER_BLOC_INFLUENCE_COST | 500 | # Cost in Influence to form / be the leader of a Power Bloc |
| MAX_LEVERAGE | 1000 | # How much "raw" Leverage can be split between parties (the country itself + each Power Bloc) |
| LEVERAGE_WEEKLY_DRIFT_FACTOR | 0.02 | # The delta between current Leverage and Target Leverage will be multiplied by this to determine the weekly Leverage drift |
| LEVERAGE_WEEKLY_DRIFT_MIN | 1 | # At minimum, Leverage will drift by +/- this value each week, up/down to the target |
| COUNTRY_POPULATION_LEVERAGE_RESISTANCE_MODIFIER_DIVISOR | 1000000 | # Population divided by this is multiplied by country_leverage_resistance_per_population to give a certain amount of leverage per million people |
| COUNTRY_POPULATION_LEVERAGE_RESISTANCE_MODIFIER_MAX_MULTIPLIER | 100 | # Max multiplier given by population. With the value above at 1 000 000, this means the cap for leverage resistance is at 100 000 000. |

## 强权集团纹章

主条目：
旗帜 modding
强权集团纹章的编写方式与旗帜纹章相同。主要区别在于其宽高比为正方形（1:1），而旗帜为矩形（3:2）。

原版游戏定义为：

```
template_power_bloc_1 = {
    pattern = "pattern_solid.tga"
    color1 = { 0.0 0.0 0.0 0.0 }

    # If we ever change the order of layers here, remember to also update them
    # in NGraphics::NPowerBlocCoa::PIECE_LAYERS_ORDER.

    colored_emblem = {
        texture = list "power_bloc_shield"
        color1 = list "power_bloc_colors"
        color2 = list "power_bloc_colors"
        instance = { scale = { 0.72 0.72 } position = { 0.49 0.6 } }  # when changing this remember to update NPowerBlocCoa in 00_defines.txt
    }

    textured_emblem = {
        texture = list "power_bloc_top"
        instance = { scale = { 0.7 0.7 } position = { 0.5 0.19 } }  # when changing this remember to update NPowerBlocCoa in 00_defines.txt
    }

    textured_emblem = {
        texture = list "power_bloc_frame"
        instance = { scale = { 0.9 0.9 } position = { 0.5 0.6 } }  # when changing this remember to update NPowerBlocCoa in 00_defines.txt
    }

    colored_emblem = {
        texture = list "power_bloc_center"
        color1 = list "power_bloc_colors"
        instance = { scale = { 0.45 0.45 } position = { 0.49 0.54 } }  # when changing this remember to update NPowerBlocCoa in 00_defines.txt
    }

    textured_emblem = {
        texture = list "power_bloc_side"
        instance = { scale = { 0.65 0.65 } position = { 0.155 0.55 } }  # when changing this remember to update NPowerBlocCoa in 00_defines.txt
    }

    textured_emblem = {
        texture = list "power_bloc_side"
        instance = { scale = { -0.65 0.65 } position = { 0.82 0.55 } }  # when changing this remember to update NPowerBlocCoa in 00_defines.txt
    }
}
```

列表定义于 /Victoria 3/game/common/coat_of_arms/template_lists。如注释所述，这些值也在 [defines](Defines.md) 中被引用。

强权集团的*盾徽*（346×346px）和*中心图案*（220×220px）是与旗帜彩色纹章位于同一文件夹中的彩色纹章，但文件前缀为 `pb_` 而非 `ce_`。类似地，顶部图案（346×346px）、边框（432×432px）和侧边图案（360×360px）是纹理纹章。注意第二个（右侧）侧边图案通过反转其 X 缩放系数来实现水平翻转。

启用“势力范围”DLC 的玩家可以从可用元素中自定义其强权集团纹章，而没有该 DLC 的玩家只能使用随机或预置的纹章。

预置强权集团纹章的创建方式是按上述方法编写纹章，然后在 /Victoria 3/game/common/coat_of_arms/template_lists/coa_templates.txt 的随机强权集团纹章列表中为该脚本化纹章赋予极高的权重，原版游戏的初始强权集团即采用此做法。

## 强权集团名称

强权集团有一组可用于随机名称和 AI 主导集团名称的名称选项。这些名称编写于 /common/power_bloc_names/。每个名称都是一个带有 trigger 的块，trigger 决定该名称何时可作为随机名称使用。

```
power_bloc_name = {
	trigger = {	
		# Trigger evaluated in leader scope
		# scope:selected_identity - the identity that is selected in the power bloc formation panel
	}
}
```

一个名称可以始终可用，例如简单地编写 `always = yes`，也可以使用更复杂的 trigger，例如仅对特定国家或领导者拥有特定州的集团可用的名称。
## 强权集团脚本文档

以下 [effect](Effect.md)、[event target](Event target.md) 与 [trigger](Trigger.md) 可在强权集团（Power Bloc）scope（作用域）中使用。

| Effect | 说明 | 示例 | 目标 |
|---|---|---|---|
| add_cohesion_number | 为 scope 中的强权集团增加指定数值的凝聚力 | add_cohesion_number = 100（增加 100 点凝聚力） |  |
| add_cohesion_percent | 为 scope 中的强权集团增加按百分比计算的凝聚力 | add_cohesion_percent = -0.2（减少凝聚力最大值的 20%） |  |
| add_leverage | 为 scope 中的强权集团增加对指定国家的杠杆值 | 若数值为正，还会按比例减少所有其他集团的杠杆值以保持匹配 add_leverage = { target = country_scope value = script_value } |  |
| add_modifier | 为 scope 中的对象添加限时 modifier 效果 | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_principle | 为强权集团添加原则 | power_bloc = { add_principle = test_principle_group_A_1 } |  |
| every_power_bloc_member | 遍历 scope 中强权集团的所有成员，包括领导者 | every_power_bloc_member = { limit = { <triggers> } #optional <effects> } | country |
| ordered_power_bloc_member | 遍历 scope 中强权集团的所有成员，包括领导者 | ordered_power_bloc_member = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| random_power_bloc_member | 遍历 scope 中强权集团的所有成员，包括领导者 | random_power_bloc_member = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| remove_modifier | 移除 scope 中对象的限时 modifier 效果 | remove_modifier = static_modifier_name |  |
| remove_principle | 从强权集团移除原则 | power_bloc = { remove_principle = test_principle_group_A_1 } |  |

| Trigger | 说明 | 示例 | 目标 |
|---|---|---|---|
| any_power_bloc_member | 遍历 scope 中强权集团的所有成员，包括领导者 | any_power_bloc_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| can_invite_any_country | 检查是否有可能邀请任何国家加入 scope 中的强权集团 | can_invite_any_country = yes/no | boolean |
| current_cohesion_number | 以数值形式比较当前凝聚力 | current_cohesion_number > 50 | value |
| current_cohesion_percentage | 以占 scope 中强权集团凝聚力最大值百分比的形式比较当前凝聚力 | current_cohesion_percentage > 0.5 | value |
| free_principle_slots | 比较强权集团的空闲原则槽位数量 | power_bloc = { free_principle_slots >= 2 } | value |
| has_identity | 检查 scope 中的强权集团是否具有特定的中央认同 | has_identity = identity:key | power_bloc_identity |
| has_modifier | 检查受支持的 scope 是否具有某个限时 modifier | has_modifier = <key> |  |
| has_principle | 检查 scope 中的强权集团是否具有特定原则 | has_principle = principle:key | power_bloc_principle |
| has_principle_group | 检查 scope 中的强权集团是否在指定组中拥有原则 | has_principle_group = principle_group:key | power_bloc_principle_group |
| leverage_advantage | 检查强权集团与目标国家之间的杠杆优势是否满足条件 | power_bloc = { leverage_advantage = { target = c:BEL value > 0 } } | value |
| num_power_bloc_members | 将强权集团的成员数量与一个值进行比较 | num_power_bloc_members >= 2 | value |
| num_power_bloc_states | 将强权集团的州数量与一个值进行比较 | num_power_bloc_states >= 2 | value |
| power_bloc_rank | 比较强权集团的排名 | power_bloc_rank <= 2 | value |
| power_bloc_total_leading_goods_producers | 比较有多少成员位居全球所有商品的领先生产者之列，并按其在排名中的位置加权。排名第一的生产者按 MIN_SPOT_PRESTIGE_AWARD 加权，其后每个名次依次减一。默认情况下，第 1 名计为 3，第 2 名计为 2，第 3 名计为 1，其他名次计为 0。 | power_bloc_total_leading_goods_producers > 15 | value |
| power_bloc_total_leading_goods_producers_with | 比较有多少成员位居全球所有商品的领先生产者之列（按排名位置加权），外加一个当前不在强权集团中的国家。排名第一的生产者按 MIN_SPOT_PRESTIGE_AWARD 加权，其后每个名次依次减一。默认情况下，第 1 名计为 3，第 2 名计为 2，第 3 名计为 1，其他名次计为 0。 | "power_bloc_total_leading_goods_producers_with(scope:target) > 15" | value |
| power_bloc_total_leading_goods_producers_without | 比较有多少成员位居全球所有商品的领先生产者之列（按排名位置加权），减去一个当前在强权集团中的国家。排名第一的生产者按 MIN_SPOT_PRESTIGE_AWARD 加权，其后每个名次依次减一。默认情况下，第 1 名计为 3，第 2 名计为 2，第 3 名计为 1，其他名次计为 0。 | "power_bloc_total_leading_goods_producers_without(scope:target) > 15" | value |
| power_bloc_worst_economic_dependence | 若在强权集团 scope 中使用，比较对领导者经济依赖最低的成员 | power_bloc_worst_economic_dependence > 2.2 | value |
| power_bloc_worst_economic_dependence_with | 若在强权集团 scope 中使用，比较对领导者经济依赖最低的成员 | power_bloc_worst_economic_dependence > 2.2 | value |
| power_bloc_worst_economic_dependence_without | 若在强权集团 scope 中使用，比较对领导者经济依赖最低的成员 | power_bloc_worst_economic_dependence > 2.2 | value |
| power_bloc_worst_infamy | 若在强权集团 scope 中使用，比较恶名（Infamy）值最差（最高）的成员国的恶名值 | power_bloc_worst_infamy > 50 | value |
| power_bloc_worst_infamy_with | 若在强权集团 scope 中使用，比较恶名值最差（最高）的成员国的恶名值 | power_bloc_worst_infamy > 50 | value |
| power_bloc_worst_infamy_without | 若在强权集团 scope 中使用，比较恶名值最差（最高）的成员国的恶名值 | power_bloc_worst_infamy > 50 | value |
| power_bloc_worst_leader_relations | 若在强权集团 scope 中使用，比较与强权集团领导者关系（Relations）值最差（最低）的成员国的关系值 | power_bloc_worst_leader_relations > 10 | value |
| power_bloc_worst_leader_relations_with | 若在强权集团 scope 中使用，比较与强权集团领导者关系值最差（最低）的成员国的关系值 | power_bloc_worst_leader_relations > 10 | value |
| power_bloc_worst_leader_relations_without | 若在强权集团 scope 中使用，比较与强权集团领导者关系值最差（最低）的成员国的关系值 | power_bloc_worst_leader_relations > 10 | value |
| power_bloc_worst_leader_religion_population_fraction | 若在强权集团 scope 中使用，比较成员国中信仰领导者宗教的人口比例的最低值 | power_bloc_worst_leader_religion_population_fraction > 10 | value |
| power_bloc_worst_leader_religion_population_fraction_with | 若在强权集团 scope 中使用，比较成员国中信仰领导者宗教的人口比例的最低值 | power_bloc_worst_leader_religion_population_fraction > 10 | value |
| power_bloc_worst_leader_religion_population_fraction_without | 若在强权集团 scope 中使用，比较成员国中信仰领导者宗教的人口比例的最低值 | power_bloc_worst_leader_religion_population_fraction > 10 | value |
| power_bloc_worst_liberty_desire | 若在强权集团 scope 中使用，比较独立倾向（Liberty Desire）值最差（最高）的成员国的独立倾向值 | power_bloc_worst_liberty_desire > 75 | value |
| power_bloc_worst_liberty_desire_with | 若在强权集团 scope 中使用，比较独立倾向值最差（最高）的成员国的独立倾向值 | power_bloc_worst_liberty_desire > 75 | value |
| power_bloc_worst_liberty_desire_without | 若在强权集团 scope 中使用，比较独立倾向值最差（最高）的成员国的独立倾向值 | power_bloc_worst_liberty_desire > 75 | value |
| power_bloc_worst_progressiveness_difference_government_type | 若在强权集团 scope 中使用，比较成员国的“治理原则”与“权力分配”法律相对强权集团领导者的进步性总差值最差（最大）的国家 | power_bloc_worst_progressiveness_compatibility_government_type > 100 | value |
| power_bloc_worst_progressiveness_difference_government_type_with | 若在强权集团 scope 中使用，比较成员国的“治理原则”与“权力分配”法律相对强权集团领导者的进步性总差值最差（最大）的国家 | power_bloc_worst_progressiveness_compatibility_government_type > 100 | value |
| power_bloc_worst_progressiveness_difference_government_type_without | 若在强权集团 scope 中使用，比较成员国的“治理原则”与“权力分配”法律相对强权集团领导者的进步性总差值最差（最大）的国家 | power_bloc_worst_progressiveness_compatibility_government_type > 100 | value |
| predicted_cohesion_percentage_with | 预测强权集团若将目标国家纳为成员后的凝聚力（以 1 为基准的比例） | predicted_cohesion_percentage_with, = { target = scope:other_country value > 0.9 } | value |
| target_cohesion_number | 以数值形式比较目标凝聚力 | target_cohesion_number > 50 | value |
| target_cohesion_percentage | 以占 scope 中强权集团凝聚力最大值百分比的形式比较目标凝聚力 | target_cohesion_percentage > 0.5 | value |
| total_used_principle_levels | 比较强权集团已激活原则等级的总数 | power_bloc = { total_used_principle_levels >= 10 } | value |
| used_principle_slots | 比较强权集团已使用的原则槽位数量 | power_bloc = { used_principle_slots >= 2 } | value |

| Event target | 说明 | 目标 scope |
|---|---|---|
| modifier | 转到当前对象所拥有的指定键的 modifier 类型值，例如：modifier:country_influence_add | boolean, value |
| num_mandates | 转到 scope 中强权集团可用委任的数量（power_bloc.num_mandates > 0） | value |
| power_bloc_leader | 转到 scope 中强权集团的领导者国家 | country |
| power_struggle_contender | 若存在权力斗争，转到竞争者国家 | country |

### 强权集团 modifier 类型

`power_bloc_` 前缀的 [modifier 类型](Modifier types.md) 会将其效果应用于强权集团。

| Modifier 类型 | 本地化文本 | 类型 | 格式 | 备注 |
|---|---|---|---|---|
| power_bloc_allow_foreign_investment_lower_rank_bool | 在强权集团内对排名较低成员的外国投资权 | boolean | good |  |
| power_bloc_allow_port_access_bool | 允许强权集团成员之间的港口准入 | boolean | good |  |
| power_bloc_allow_wider_migration_area_bool | 允许强权集团内的迁移 | boolean | good |  |
| power_bloc_cohesion_add | 强权集团凝聚力 | additive | good |  |
| power_bloc_cohesion_mult | 强权集团凝聚力 | multiplicative | percent, good |  |
| power_bloc_cohesion_per_member_add | 每个强权集团成员的强权集团凝聚力 | additive | good |  |
| power_bloc_customs_union_bool | 关税同盟 | boolean | neutral |  |
| power_bloc_disallow_embargo_bool | 不能}}对其他强权集团成员实施禁运 | boolean | neutral |  |
| power_bloc_disallow_war_bool | 不能}}在强权集团成员之间发动或加入战争 | boolean | neutral |  |
| power_bloc_income_transfer_to_leader_factor | 向强权集团领导者的收入转移 | multiplicative | neutral |  |
| power_bloc_invite_acceptance_add | 强权集团邀请接受几率 | additive | good |  |
| power_bloc_invite_acceptance_great_power_add | 列强接受强权集团邀请的几率 | additive | good |  |
| power_bloc_invite_acceptance_major_power_add | 主要政权接受强权集团邀请的几率 | additive | good |  |
| power_bloc_invite_acceptance_minor_power_add | 次要政权接受强权集团邀请的几率 | additive | good |  |
| power_bloc_invite_acceptance_unrecognized_major_power_add | 未受承认的主要政权接受强权集团邀请的几率 | additive | good |  |
| power_bloc_invite_acceptance_unrecognized_regional_power_add | 未受承认的区域政权接受强权集团邀请的几率 | additive | good |  |
| power_bloc_leader_can_add_wargoal_bool | 允许自由设置战争目标 | boolean | neutral |  |
| power_bloc_leader_can_force_state_religion_bool | 允许强推国教 | boolean | neutral |  |
| power_bloc_leader_can_make_subjects_bool | 可**使**强权集团成员**成为附属国** | boolean | neutral |  |
| power_bloc_leader_can_regime_change_bool | 允许强制政权更迭 | boolean | neutral |  |
| power_bloc_leader_can_spread_culture_to_pb_bool | 允许在强权集团成员中传播主流文化 | boolean | neutral |  |
| power_bloc_leverage_generation_mult | 杠杆值生成 | multiplicative | percent, good |  |
| power_bloc_mandate_progress_mult | 每周委任进度 | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_great_power_member_add | 每个列强的委任进度 | additive | good |  |
| power_bloc_mandate_progress_per_great_power_member_mult | 每个列强的委任进度 | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_insignificant_power_member_add | 每个无足轻重政权的委任进度 | additive | good |  |
| power_bloc_mandate_progress_per_insignificant_power_member_mult | 每个无足轻重政权的委任进度 | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_major_power_member_add | 每个主要政权的委任进度 | additive | good |  |
| power_bloc_mandate_progress_per_major_power_member_mult | 每个主要政权的委任进度 | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_minor_power_member_add | 每个次要政权的委任进度 | additive | good |  |
| power_bloc_mandate_progress_per_minor_power_member_mult | 每个次要政权的委任进度 | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_unrecognized_major_power_member_add | 每个未受承认主要政权的委任进度 | additive | good |  |
| power_bloc_mandate_progress_per_unrecognized_major_power_member_mult | 每个未受承认主要政权的委任进度 | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_unrecognized_power_member_add | 每个未受承认政权的委任进度 | additive | good |  |
| power_bloc_mandate_progress_per_unrecognized_power_member_mult | 每个未受承认政权的委任进度 | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_unrecognized_regional_power_member_add | 每个未受承认区域政权的委任进度 | additive | good |  |
| power_bloc_mandate_progress_per_unrecognized_regional_power_member_mult | 每个未受承认区域政权的委任进度 | multiplicative | percent, good |  |
| power_bloc_target_sway_cost_mult | 外交博弈目标的拉拢行动成本 | multiplicative | percent, bad |  |
| power_bloc_trade_advantage_add | 强权集团内的贸易优势 | additive | good |  |
## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • Power blocs • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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