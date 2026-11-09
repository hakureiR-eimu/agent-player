---
translated: 2026-10-27
translator: machine (glm-5.3)
title: On action
source: https://vic3.paradoxwikis.com/On_action
pageid: 3144
categories: [Potentially_outdated, 1.12, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。至少部分章节最后核实于[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.12。

On actions（on_action 机制）
**游戏文件夹 该类型文件存放的文件夹。 ：** `common/on_actions`

---

**可注入（Injectable） 该类型能否使用 INJECT 数据库函数？ ：** ![No](/images/thumb/0/04/No.png/24px-No.png) no **可替换（Replaceable） 该类型能否使用 REPLACE 数据库函数？ ：** ![No](/images/thumb/0/04/No.png/24px-No.png) no

---

**相关游戏对象：**[事件](Event modding.md)

**On actions（on_action 机制）**是由特定情形触发的 effect（游戏内效果脚本）。常见的例子是按固定周期发生的脉冲（pulse），例如每月或每年。其他例子包括各类游戏事件，例如战争开始或结束、获得新统治者，或某个角色死亡。

## On action 结构

On action 具有以下包含若干可选块的结构。大多数 on action 都有指定的 root scope，有些还有额外的 scope。

```
on_action_name = {
	trigger = {			# On_actions can have triggers. If an on_action fires and its trigger returns false, nothing happens
		trigger_conditions = yes
	}

	weight_multiplier = {	# Used to manipulate the weight of this on_action if it is a candidate in a random_on_actions list (see below)
		base = 1
		modifier = {
			add = 1
			trigger_conditions = yes
		}
	}

	events = {		# Events listed in "events" brackets will always fire as long as their trigger evaluates to true
		event_id.1
		delay = { days = 365 }		# A delay will mean that all events listed after it will only be fired after the delay has passed. NOTE: For performance reasons, an event will only successfully fire if it is valid both when the on_action is executed AND once the delay is complete. All firing entries support delays, whether for events or on_actions.
		event_id.2
		delay = { months = { 6 12 } }	# Setting a new delay overrides a previous delay. Delays support random ranges
		event_id.3
	}
	
	random_events = {	# A single event will be picked to fire
		
		chance_to_happen = 25	# A percentage chance determining whether the events involved will be evaluated at all

		chance_of_no_event = { 	# An entry that can be formatted as a script value (and therefore have conditional entries). Separated from "chance_to_happen" for performance reasons. Will only be evaluated if chance_to_happen is true.
			value = 0
			if = {
				limit = { trigger_conditions = yes }
				add = 10
			}
		}

		100 = event_id.1 	# The number is the weight for picking a specific event. The weight is factored by the event's weight_multiplier entry. (If no weight_multiplier is defined for the event, it is 1)
		200 = event_id.2
		100 = 0		# Having a "0" entry means that there is a chance no event fires, even if there are other valid events. Good for making sure that rare events don't always fire just because every other possible event is invalid.
	}

	first_valid = {		# Pick the first event for which the trigger returns true
		event_id.1
		event_id.2
		fallback_event_without_trigger
	}

	on_actions = {	# An on_action can fire other on_actions, following the same rules as with events
		on_action_1
		on_action_2
		on_action_3
	}

	random_on_action = {	# Same as with events. On_actions are also factored by their weight_multipliers, which defaults to 1
		100 = on_action_1
		200 = on_action_2
		100 = 0
	}

	first_valid_on_action = {
		on_action_1
		on_action_2
	}

	effect = { 	# An on_action can run effects. It can access the same default or saved scopes as the script chain/code functionality it was fired from. Note that it happens concurrently to events triggered by the on_action, NOT before. Effects run here create a separate chain than events the on_action fires, so you can for example not manipulate values in the effect, and then reliably access those in an event that was fired at the same time. Scopes or local variables set in the effect here will not carry over to any event fired by the on_action.
		effects = yes
	}

	fallback = another_on_action 	# on_actions can define a fallback on_action. If no events/on_actions are run by the on_action, the fallback gets called instead. Avoid creating infinite fallback loops, or the game may be prevented from advancing time!
}
```

| 块 | 描述 |
|---|---|
| trigger | 决定该 on action 被调用时能否触发的 [triggers](Trigger.md) |
| events | 该 on action 触发时被调用的 [事件](Event modding.md)列表 |
| random_events | 从列表中按权重随机选取一个有效事件调用 |
| first_valid | 从列表中调用第一个有效事件，由被调用事件的 trigger 决定 |
| on_actions | 该 on action 触发时被调用的 on action 列表 |
| random_on_action | 从列表中按权重随机选取一个有效 on action 调用 |
| first_valid_on_action | 从列表中调用第一个有效 on action，由被调用 on_action 的 trigger 决定 |
| effect | 随该 on action 一同触发的 [effects](Effect.md) |
| weight_multiplier | 一个 MTTH 块，用于修改该 on action 的权重，以便在 random_on_actions 块中使用 |
| fallback | 若该 on action 未触发任何 effect、事件或 on action，则调用的单个 on action |

每个块都可以有任意数量的 `delay` 块。delay 之后的任何事件、on action 或 effect 都会等待到延迟结束。

On action 也可以通过 effect `trigger_event` 来调用，如下所示：

```
	trigger_event = {
		on_action = on_action_name
		days/months/years = X  	# Optional, to delay the firing time
	}
```

### 修改 on action

On action 可以很容易地通过从硬编码的 on action 中调用新的脚本化 on action 来进行 mod 修改。只有新的 `on_actions` 和 `events` 块可以添加到现有 on action 中。向现有 on action 添加其他块会导致错误。

例如，要向每月国家脉冲添加新的 effect，可在 mod 的 common/on_actions 文件夹中的新文件里使用以下模板：

```
on_monthly_pulse_country = {
	on_actions = {
    	new_on_action #the name should be unique, but does not need to follow any strict pattern
    }
}
new_on_action = {
	effect = {
		newly added effects
	}
}
```

这样，基础游戏的 on action 在每次触发时都会调用这个被修改的 on action。

## On action 列表

除非另有说明，给定的 scope 为 `root`

| 名称 | 给定 scope | 描述 / 备注 |
|---|---|---|
| on_acquired_technology | Root = 适用的国家 scope:technology = 其开始研究的技术类型 | 若由 effect 调用，请从 `country` scope 调用 |
| on_ally_capitulated_notification | country |  |
| on_amendment_repealed | Root = 国家 scope:amendment = 正被废除的修正案 |  |
| on_battle_ended | Root = 进攻方或防守方国家 scope:enemy_country = root 的敌国 scope:battle = 战斗 scope:attacker = 进攻方指挥官 scope:defender = 防守方指挥官 scope:state = 所在州 |  |
| on_battle_lost |  |  |
| on_battle_started |  |  |
| on_battle_won | 若由 effect 调用，请从 `country` scope 调用 |  |
| on_become_independent | Root = 新独立的国家 scope:overlord = 前宗主国 |  |
| on_become_subject | Root = 新成为附属国的国家 scope:overlord = 新宗主国 |  |
| on_building_built | building |  |
| on_building_expanded | building |  |
| on_capitulation | Root = 投降的国家 scope:diplomatic_play = 外交博弈 |  |
| on_character_creation | character |  |
| on_character_death | character |  |
| on_character_recruitment | character |  |
| on_civil_war_won | country |  |
| on_claim_added | Root = 国家（拥有该州区域中某州的国家）scope:actor = 提出声索的国家 scope:region = 被声索的州区域 |  |
| on_colony_created | state |  |
| on_company_disbanded | Root = 国家（公司被解散的国家）scope:company = 被解散的公司 |  |
| on_company_established | Root = 国家（公司被建立的国家）scope:company = 被建立的公司 |  |
| on_country_broke_treaty | Root = 条约 scope:withdrawing_country = 退出条约的国家 scope:non_withdrawing_country = 未退出条约的国家 | 当约束期仍在生效时触发，以此代替 on_country_withdrawn_from_treaty |
| on_country_default | country |  |
| on_country_formed | country |  |
| on_country_no_longer_default | country |  |
| on_country_released_as_company_subject | Root = 释放国 scope:target = 被释放的国家 |  |
| on_country_released_as_independent | Root = 释放国 scope:target = 被释放的国家 |  |
| on_country_released_as_overlord_subject | Root = 释放国 scope:target = 被释放的国家 |  |
| on_country_released_as_own_subject | Root = 释放国 scope:target = 被释放的国家 |  |
| on_country_swayed | Root = diplomatic_play scope:actor = 进行拉拢的国家 scope:target = 被拉拢的目标 scope:recipient = 被拉拢的国家 scope:notification_target = 被通知的国家 |  |
| on_country_withdrawn_from_treaty | Root = 条约 scope:withdrawing_country = 退出条约的国家 scope:non_withdrawing_country = 未退出条约的国家 | 当约束期未生效时触发 |
| on_create_market | market |  |
| on_deactivate_link |  |  |
| on_decade_pulse_character | character |  |
| on_decade_pulse_country | country | 若由 effect 调用，请从 `country` scope 调用 |
| on_decade_pulse_country_elections | country | 仅在启用选举时触发 |
| on_decade_pulse_state | state |  |
| on_demobilized_army | military_formation |  |
| on_demobilized_general | chracter |  |
| on_diplo_play_abandon_side | diplomatic_play |  |
| on_diplo_play_back_down | Root = diplomatic_play scope:actor = 退让的国家 scope:notification_target = 被通知的国家 |  |
| on_diplo_play_back_down_involved | Root = diplomatic_play scope:actor = 退让的国家 scope:target = 对立一方的领导者 scope:notification_target = 被通知的国家 |  |
| on_diplo_play_declare_neutrality | Root = diplomatic_play scope:actor = 宣布中立的国家 scope:initiator = 博弈发起者 scope:target = 博弈目标 scope:notification_target = 被通知的国家 |  |
| on_diplo_play_join_side | Root = diplomatic_play scope:actor = 加入的国家 scope:target = 所加入博弈的目标 scope:recipient = 加入的国家 scope:notification_target = 被通知的国家 |  |
| on_diplo_play_start | Root = diplomatic_play scope:actor = 博弈发起者 scope:notification_target = 被通知的国家 |  |
| on_diplo_play_start_third_party | diplomatic_play |  |
| on_diplo_play_subject_released | diplomatic_play |  |
| on_diplo_play_subject_released_overlord | diplomatic_play |  |
| on_diplo_play_switch_sides | Root = 外交博弈 scope:country = 转入的国家 scope:previous = 转出的国家 |  |
| on_diplo_play_war_start | Root = diplomatic_play scope:actor = 博弈发起者 scope:target = 博弈目标 |  |
| on_diplomatic_action | Root = diplomatic_action scope:actor = 执行行动的国家 scope:recipient = 行动目标 scope:notification_target = 被通知的国家 |  |
| on_diplomatic_action_break |  |  |
| on_diplomatic_action_overlord_decrease_autonomy | diplomatic_action |  |
| on_diplomatic_action_overlord_increase_autonomy | diplomatic_action |  |
| on_diplomatic_action_subject_increase_own_autonomy | diplomatic_action |  |
| on_diplomatic_action_third_party | diplomatic_action |  |
| on_diplomatic_action_third_party_accepted | diplomatic_action |  |
| on_diplomatic_action_third_party_break | diplomatic_action |  |
| on_diplomatic_action_third_party_break_accepted | diplomatic_action |  |
| on_diplomatic_action_third_party_break_declined | diplomatic_action |  |
| on_diplomatic_action_third_party_declined | diplomatic_action |  |
| on_diplomatic_demand | Root = diplomatic_demand scope:actor = 提出要求的国家 scope:recipient = 要求的目标 scope:notification_target = 被通知的国家 |  |
| on_diplomatic_demand_accepted | diplomatic_demand |  |
| on_diplomatic_demand_rejected | Root = diplomatic_demand scope:recipient = 要求的目标 scope:notification_target = 被通知的国家 |  |
| on_diplomatic_incident | Root = 战略区域 scope:actor = 挑衅国 scope:target = 目标国 |  |
| on_diplomatic_pact_auto_break | Root = diplomatic_action scope:country = 条约的第一国 scope:target_country = 条约的第二国 scope:notification_target = 被通知的国家 |  |
| on_diplomatic_pact_third_party_auto_break | diplomatic_action |  |
| on_diplomatic_play_started | root = 已开始的外交博弈 scope:initiator = 博弈发起者 scope:target = 博弈目标 |  |
| on_diplomatic_proposal | root = diplomatic_action scope:actor = 提议国 scope:recipient = 被提议国 scope:notification_target = 被通知的国家 |  |
| on_diplomatic_proposal_accepted |  |  |
| on_diplomatic_proposal_break | diplomatic_action |  |
| on_diplomatic_proposal_break_accepted | diplomatic_action |  |
| on_diplomatic_proposal_break_call_in_obligation | diplomatic_action |  |
| on_diplomatic_proposal_break_declined | diplomatic_action |  |
| on_diplomatic_proposal_break_owe_obligation | diplomatic_action |  |
| on_diplomatic_proposal_call_in_obligation | diplomatic_action |  |
| on_diplomatic_proposal_declined | root = diplomatic_action scope:actor = 提议国 scope:recipient = 被提议国 scope:notification_target = 被通知的国家 |  |
| on_diplomatic_proposal_owe_obligation | diplomatic_action |  |
| on_diplomats_expelled | diplomatic_action |  |
| on_election_campaign_end | country |  |
| on_election_campaign_start | country |  |
| on_empty_battle_lost | Root = 进攻方或防守方国家 scope:enemy_country = root 的敌国 scope:battle = 战斗 scope:attacker = 进攻方指挥官 scope:defender = 防守方指挥官 scope:state = 所在州 | 当一方在结束时没有部队 |
| on_empty_battle_won | 当一方在结束时没有部队 |  |
| on_enemy_capitulated_notification | Root = 被通知的国家 scope:target = 投降的国家 scope:diplomatic_play = 外交博弈 |  |
| on_enemy_convoys_raided | Root = 国家 scope:region = 袭击发生的海域 |  |
| on_five_year_pulse_character | character |  |
| on_five_year_pulse_country | country | 若由 effect 调用，请从 `country` scope 调用 |
| on_five_year_pulse_country_elections | country | 仅在启用选举时触发 |
| on_five_year_pulse_state | state |  |
| on_game_started | none | 在历史加载完成后立即触发，但在国家选择之前（无玩家） |
| on_game_started_after_lobby | none | 在国家选择之后加载时立即触发 |
| on_government_reformed | country |  |
| on_half_yearly_pulse_character | character |  |
| on_half_yearly_pulse_country | country | 若由 effect 调用，请从 `country` scope 调用 |
| on_half_yearly_pulse_country_elections | country | 仅在启用选举时触发 |
| on_half_yearly_pulse_state | state | 若由 effect 调用，请从 `state` scope 调用 |
| on_harvest_condition_started_in_country | Root = 国家 scope:area = 收获状况区域 scope:state = 受影响程度最高的州 scope:duration = 收获状况持续天数 scope:num_states = 该国受影响的州的数量 scope:intensity = 受影响州中的最高强度 |  |
| on_heir_born | character |  |
| on_ig_resigned_government | interest_group |  |
| on_impose_law | Root = 被强加法律的国家 scope:initiator = 强加法律的国家 scope:law = 被强加的法律 | 当法律类型上没有覆盖性的 on_impose effect 时会触发此 on action。若该法律类型存在 on_impose effect，则不会执行此 on action。 |
| on_investment_decreased | institution |  |
| on_investment_increased | institution |  |
| on_journal_entry_activated | journal_entry |  |
| on_journal_entry_completed | journal_entry |  |
| on_journal_entry_deactivated | journal_entry |  |
| on_journal_entry_failed | journal_entry |  |
| on_law_activated | law | 不能使用 `currently_enacting_law` |
| on_law_checkpoint_advance | country | 若由 effect 调用，请从 country scope 调用 可使用 currently_enacting_law |
| on_law_checkpoint_debate | country |  |
| on_law_checkpoint_stall | country |  |
| on_law_checkpoint_success | country | 可使用 `currently_enacting_law` |
| on_law_enactment_ended | country |  |
| on_law_enactment_fail | country |  |
| on_law_enactment_pass | country |  |
| on_law_enactment_started | country |  |
| on_merge_markets | Root = 被并入的市场 scope:market = 并入的市场 scope:trade_center = root 的贸易中心州 |  |
| on_migration_target_created | Root = state scope:country = 迁移来源国 scope:notification_target = 被通知的国家 |  |
| on_migration_target_created_other |  |  |
| on_military_formation_created | military_formation |  |
| on_mobilized_army | military_formation |  |
| on_mobilized_general | character |  |
| on_monthly_pulse | none |  |
| on_monthly_pulse_character | character |  |
| on_monthly_pulse_country | country | 若由 effect 调用，请从 `country` scope 调用 |
| on_monthly_pulse_country_elections | country | 若由 effect 调用，请从 `country` scope 调用 仅在启用选举时触发 |
| on_monthly_pulse_state | state |  |
| on_national_awakening_started | Root = 文化 scope:region = 觉醒发生的州区域 scope:culture = 发生觉醒的文化 |  |
| on_native_uprising | Root = 殖民国家 scope:actor = 起义国家 |  |
| on_new_culture_obsession | Root = 文化 scope:goods = 痴迷的商品 |  |
| on_new_interest_group_leader | character |  |
| on_new_ruler | Root = character scope:previous = 前任统治者 |  |
| on_objective_completed | objective |  |
| on_obligation_owed_by_us_expired | country |  |
| on_obligation_owed_to_us_expired | country |  |
| on_our_convoys_raided | Root = 国家 scope:region = 袭击发生的海域 |  |
| on_party_created | Root = 国家 scope:target = 被创建的政党 |  |
| on_party_disbanded | Root = 国家 scope:target = 被解散的政党 |  |
| on_peace_agreement_signed_non_participant | country |  |
| on_peace_agreement_signed_war_leader | country |  |
| on_peace_agreement_signed_war_participant | country |  |
| on_political_movement_disbanded | political_movement |  |
| on_political_movement_formed | political_movement |  |
| on_political_movement_supported_law_cancelled | political_movement |  |
| on_power_bloc_struggle_ended | Root = 领导权被争夺的强权集团 scope:successful_contender = 赢得强权斗争的国家 scope:failed_contender = 输掉强权斗争的国家 |  |
| on_power_bloc_struggle_started | country | Root = 发起强权斗争的国家 |
| on_production_method_changed | building |  |
| on_rank_changed | country |  |
| on_repudiate_obligation | country |  |
| on_research_technology_started | Root = 适用的国家 scope:technology = 其开始研究的技术类型 |  |
| on_resource_depleted | state | 若由 effect 调用，请从 `state` scope 调用 |
| on_resource_discovered | Root = state scope:target = 建筑类型 | 若由 effect 调用，请从 `state` scope 调用 |
| on_retarget_link | state |  |
| on_reverse_sway_offer | diplomatic_play |  |
| on_reverse_sway_offer_accepted | diplomatic_play |  |
| on_reverse_sway_offer_rejected | diplomatic_play |  |
| on_revolution_checkpoint_reached | country | 若由 effect 调用，请从 `country` scope 调用 |
| on_revolution_end | Root = 国家 scope:target = 起义国家 |  |
| on_revolution_start | Root = 国家 scope:target = 起义国家 | 可用于对新建的起义国家施加 effect。 |
| on_secession_checkpoint_reached | country | 若由 effect 调用，请从 `country` scope 调用 |
| on_secession_country_helped_by_home_country | Root = 母国 scope:target = 分离主义国家 |  |
| on_secession_country_not_helped_by_home_country | Root = 母国 scope:target = 分离主义国家 |  |
| on_secession_end | Root = 国家 scope:target = 起义国家 |  |
| on_secession_start | Root = 国家 scope:target = 起义国家 | 可用于对新建的分离主义国家施加 effect。 |
| on_self_capitulated_notification | Root = 国家 scope:target = 投降的国家 scope:diplomatic_play = 外交博弈 |  |
| on_spreading_technology | Root = 适用的国家 scope:technology = 其开始研究的技术类型 |  |
| on_start_expanding_building | building |  |
| on_start_supporting_unification | country |  |
| on_state_created | state |  |
| on_state_incorporation | state |  |
| on_state_owner_change | state |  |
| on_stop_supporting_unification | country |  |
| on_sub_objective_completed | objective |  |
| on_sub_objective_failed | objective |  |
| on_sway_offer | Root = diplomatic_play scope:actor = 进行拉拢的国家 scope:target = 被拉拢的目标 scope:recipient = 被拉拢的国家 scope:notification_target = 被通知的国家 |  |
| on_sway_offer_accepted | Root = diplomatic_play scope:target = 被拉拢的目标 scope:recipient = 被拉拢的国家 scope:notification_target = 被通知的国家 |  |
| on_sway_offer_rejected | diplomatic_play |  |
| on_travel_deploy_to_sea_node_cancelled | Root = 军事编队 scope:province = 原定前往的海洋节点 scope:target = 当前目标移动位置——总部或省份（海洋节点） |  |
| on_travel_station_in_hq_cancelled | Root = 军事编队 scope:hq = 原定前往的总部 scope:target = 当前目标移动位置——总部或省份（海洋节点） |  |
| on_travel_to_front_cancelled | Root = 军事编队 scope:front = 原定前往的前线 scope:target = 当前目标移动位置——总部或省份（海洋节点） |  |
| on_travel_track_formation_cancelled | Root = 军事编队 scope:formation = 原定追踪的编队 scope:target = 当前目标移动位置——总部或省份（海洋节点） |  |
| on_treaty_article_removed | Root = 条约 scope:article = 条约条款 |  |
| on_treaty_dissolved | treaty |  |
| on_treaty_enforced | treaty | 对于通过外交博弈等强制执行的条约，除 on_treaty_entered_into_force 外还会触发此 on action |
| on_treaty_entered_into_force | treaty |  |
| on_treaty_proposal_declined | Root = 条约 scope:declining_country = 拒绝的国家 scope:proposing_country = 提议的国家 |  |
| on_treaty_proposed | root = 条约 scope:actor = 提议的国家 scope:recipient = 接收的国家 scope:first_country = 提议的国家 scope:second_country = 接收的国家 |  |
| on_unification_candidate_added | country |  |
| on_unification_candidate_removed | country |  |
| on_war_end | Root = 外交博弈 scope:actor = 发起国 scope:target = 目标国 |  |
| on_wargoal_added | Root = 外交博弈 scope:actor = 战争目标所有者 scope:war_goal = 战争目标 |  |
| on_wargoal_enforced | Root = 国家 scope:target = 战争目标被强加于的国家 scope:diplomatic_play = 相关的外交博弈 scope:wargoal_impact = 被强加战争目标的影响 |  |
| on_wargoal_removed | Root = 外交博弈 scope:actor = 战争目标所有者 |  |
| on_yearly_pulse | none |  |
| on_yearly_pulse_character | character |  |
| on_yearly_pulse_country | country | 若由 effect 调用，请从 `country` scope 调用 |
| on_yearly_pulse_country_elections | country | 仅在启用选举时触发 |
| on_yearly_pulse_state | state | 若由 effect 调用，请从 `state` scope 调用 |
## 参考

Modding（模组制作）
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

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|