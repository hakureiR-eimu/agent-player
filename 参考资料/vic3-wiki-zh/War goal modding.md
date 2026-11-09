---
translated: 2026-10-27
translator: machine (glm-5.3)
title: War goal modding
source: https://vic3.paradoxwikis.com/War_goal_modding
pageid: 9130
categories: [Potentially_outdated, 1.12, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。其中至少部分内容最后核实的版本为 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.12。

另见：
战争目标
**战争目标（War goals）** 是一国可以向另一国提出的外交要求。其定义位于 `common/war_goal_types`

## 战争目标定义

### 基础

| 块 | 说明 |
|---|---|
| `icon` | 图标路径 |
| `execution_priority` | 数值越高越先执行 |

### 类型（Kind）

这里的“类型（Kind）”指预定义的执行行为和预定义的检查。原版所有战争目标都关联到一个类型，情况基本就是这样。如果不需要预定义的 effect 或检查，使用 `custom`。

可使用以下值：

- `annex_country`
- `ban_slavery`
- `colonization_rights`
- `conquer_state`
- `contain_threat`
- `enforce_treaty_article`
- `force_nationalization`
- `foreign_investment_rights`
- `humiliation`
- `increase_autonomy`
- `independence`
- `join_power_bloc`
- `leave_power_bloc`
- `liberate_country`
- `liberate_subject`
- `make_dominion`
- `make_protectorate`
- `make_tributary`
- `open_market`
- `reduce_autonomy`
- `regime_change`
- `return_state`
- `revoke_all_claims`
- `revoke_claim`
- `secession`
- `take_treaty_port`
- `transfer_subject`
- `unification`
- `unification_leadership`
- `custom`

### 设置

#### 验证

你可以在战争目标设置中设定标记，以对其进行验证。

| 设置 | 说明 |
|---|---|
| `annexes_entire_state` | 为战争目标标记预期行为，用于计算冲突 |
| `annexes_entire_country` |  |
| `country_creation` |  |
| `turns_into_subject` |  |

| 设置 | 说明 |
|---|---|
| `conflicts_with_annex_state` | 标记该战争目标可能与相应类型的战争目标发生冲突 |
| `conflicts_with_annex_country` |  |
| `conflicts_with_make_subject` |  |
| `conflicts_with_existing_subject` |  |
| `conflicts_with_country_creation` |  |

随后你可以让战争目标针对特定事项进行验证，或根据其他战争目标的设置与其产生冲突。

| 设置 | 说明 |
|---|---|
| `validate_subject_relation` | 检查该战争目标产生的附属国关系是否有效 |
| `validate_formation_candidate_self` | 检查以确保目标持有者是统一候选国 |
| `validate_formation_candidate_target` | 检查以确保目标是统一候选国 |
| `validate_sole_formation_candidate` | 检查以确保目标持有者是唯一的统一候选国 |
| `validate_target_not_treaty_port` | 检查以确保目标州不是条约港 |
| `validate_join_power_bloc` | 相应战争目标类型的特殊验证 |
| `validate_colonization_rights` |  |
| `validate_force_nationalization` |  |
| `validate_foreign_investment_rights` |  |
| `validate_regime_change` |  |
| `validate_contain_threat` |  |
| `validate_revoke_claims` |  |
| `validate_increase_autonomy` |  |
| `validate_take_treaty_port` |  |
| `validate_independence` |  |
| `validate_conflicts_war_goals_holder` | 验证与持有者提出的同类型战争目标之间的冲突 |
| `validate_conflicts_war_goals_all` | 验证与所有参战国提出的同类型战争目标之间的冲突 |
| `validate_conflicts_conquer_state` | 验证与带有相应冲突标记的战争目标类型之间的冲突 |
| `validate_conflicts_annex_country` |  |
| `validate_conflicts_make_subject` |  |
| `validate_conflicts_existing_subject` |  |

#### 其他

这些是更多可用的设置。

| 设置 | 说明 |
|---|---|
| `require_target_be_part_of_war` | 不能以中立国为目标 |
| `can_add_for_other_country` | 允许为其他参战国添加该目标 |
| `overlord_is_stakeholder` | 战争目标的利益相关方是否应为宗主国 |
| `can_target_decentralized` | 该战争目标是否可以以未受认可的国家为目标 |
| `has_other_stakeholder` | 该战争目标的利益相关方是否与目标不同 |
| `skip_build_list` | 该战争目标是否可在战争目标菜单中被选取 |
| `targets_enemy_subject` | 该战争目标是否应专门以敌方附属国为目标 |
| `targets_enemy_claims` | 该战争目标是否应以某国的宣称领土为目标 |
| `requires_interest` | 该战争目标是否要求你在相关战略区域拥有利益 |

### 争夺类型

设定什么情况算作“控制”该战争目标。

可使用以下值：

- `control_target_state`
- `control_target_country_capital`
- `control_any_target_country_state`
- `control_any_target_incorporated_state`
- `control_own_state`
- `control_own_capital`
- `control_all_own_states`
- `control_all_target_country_claims`
- `control_any_releasable_state`

### 目标类型

设定战争目标指向的对象类型。

可取值：

- `country`（遍历敌国以生成战争目标备选项）
- `state`（遍历敌国所属的州）
- `treaty_article`（先遍历条约条款类型，再遍历敌国）

### 验证触发器（Trigger）

这些是用于判定战争目标能否使用的 trigger 块。可用的 scope 如下：

- `root`（持有国）
- `creator_country`
- `diplomatic_play`
- `target_country`
- `target_state`
- `stakeholder`
- `target_region`
- `article_options`

| Trigger | 说明 |
|---|---|
| `possible` | 决定在外交博弈中选择战争目标时是否列出该目标 |
| `valid` | 决定该战争目标从脚本角度是否有效 |

### 恶名与博弈行动点

这些块设定选择某战争目标需要多少恶名和博弈行动点（在应用 modifier 之前）。两者都接受 script value。

可用的 scope 如下：

- `root`（持有国）
- `creator_country`
- `diplomatic_play`
- `target_country`
- `target_state`
- `stakeholder`
- `target_region`
- `article_options`

### 强制执行时

`on_enforced` 块是你放置战争目标要执行的脚本的地方。这与 `kind` 块中定义的行为是分开的。

可用的 scope 如下：

- `root`（持有国）
- `creator_country`
- `diplomatic_play`
- `target_country`
- `target_state`
- `stakeholder`
- `target_region`
- `article_options`

### AI

AI 块中只有一个设置。

| 设置 | 取值 | 说明 |
|---|---|---|
| `is_significant_demand` | yes/no | 一个标记，决定 AI 认为该战争目标有多重要 |

## 战争目标示例

```
conquer_state = {
	icon = "gfx/interface/icons/war_goals/conquer_state.dds"

	kind = conquer_state

	settings = {
		require_target_be_part_of_war
		annexes_entire_state
		can_add_for_other_country
		requires_interest

		# Validation
		validate_target_not_treaty_port
		validate_conflicts_conquer_state

		conflicts_with_country_creation
		conflicts_with_annex_state
	}

	execution_priority = 69

	contestation_type = control_target_state

	target_type = state

	possible = {
		# trigger to determine if a goal with its target data is listed when selecting a war goal in the diplo play panel
		# scopes: root = holder, creator_country, diplomatic_play, target_country, target_state, stakeholder, target_region, article_options
	}

	valid = {
		# trigger in addition to some basic validation code-side
		# scopes: root = holder, creator_country, diplomatic_play, target_country, target_state, stakeholder, target_region, article_options
		scope:target_state = {
			owner = scope:target_country
			NOT = { has_claim_by = root }
		}
	}

	maneuvers = {
		value = 0

		add = {
			desc = "MANEUVERS_BASE_VALUE"
			value = 10
		}

		multiply = {
			desc = "MANEUVERS_TARGET_STATE_POPULATION_FACTOR"
			value = scope:target_state.state_population
			divide = define:NDiplomacy|SWAY_OFFER_WARGOAL_MANEUVERS_COST_POPULATION_SCALING_FACTOR
			multiply = define:NDiplomacy|SWAY_OFFER_WARGOAL_MANEUVERS_COST_POPULATION_SCALING_MULTIPLIER
			max = define:NDiplomacy|SWAY_OFFER_WARGOAL_MANEUVERS_COST_POPULATION_SCALING_MULTIPLIER_MAX_PER_STATE
		}
	}

	infamy = {
		value = 0

		add = {
			desc = "INFAMY_BASE_VALUE"
			value = 5
		}

		multiply = {
			desc = "INFAMY_STATE_POPULATION_FACTOR"
			value = scope:target_state.state_population
			divide = define:NDiplomacy|WAR_GOAL_INFAMY_POPULATION_SCALING_FACTOR
			multiply = define:NDiplomacy|WAR_GOAL_INFAMY_POPULATION_SCALING_MULTIPLIER
			add = 1
			max = define:NDiplomacy|WAR_GOAL_INFAMY_POPULATION_SCALING_MULTIPLIER_MAX_PER_STATE
		}

		multiply = {
			desc = "country_infamy_generation_against_unrecognized_mult"
			value = 1
			if = {
				limit = {
					scope:target_country = {
						is_country_type = unrecognized
					}
				}
				add = modifier:country_infamy_generation_against_unrecognized_mult
			}
		}

		multiply = {
			desc = "IG_OTHER_FACTORS_HEADER"
			value = 1

			if = {
				limit = {
					scope:target_state = {
						is_homeland_of_country_cultures = root
					}
				}
				add = define:NDiplomacy|WAR_GOAL_INFAMY_HOMELAND_FACTOR
			}

			if = {
				limit = {
					scope:target_state = {
						is_incorporated = no
					}
				}
				add = define:NDiplomacy|WAR_GOAL_INFAMY_UNINCORPORATED_FACTOR
			}
		}

		min = 5
	}

	on_enforced = {
		# script effect on top of the predefined code effect
	}

	ai = {
		is_significant_demand = yes
	}
}
```

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • War goals |
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