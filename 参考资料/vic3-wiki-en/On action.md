---
title: On action
source: https://vic3.paradoxwikis.com/On_action
pageid: 3144
categories: [Potentially_outdated, 1.12, Modding]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.12.

On actions
**Game folder The folder where the files for this type are stored. :** `common/on_actions`

---

**Injectable Can INJECT database functions be used with this type? :** ![No](/images/thumb/0/04/No.png/24px-No.png) no **Replaceable Can REPLACE database functions be used with this type? :** ![No](/images/thumb/0/04/No.png/24px-No.png) no

---

**Related game objects:** [Events](Event modding.md)

**On actions** are effects called by specific circumstances. Common examples are pulses which happen on a regular period, such as monthly or yearly. Other examples include various game occurrences such as starting or ending a war, gaining a new ruler, or a character dying.

## On action structure

On actions have the following structure with several optional blocks. Most on actions have a specified root scope, some have additional scopes as well.

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

| Block | Description |
|---|---|
| trigger | [Triggers](Trigger.md) that determine if the on action can fire when called |
| events | List of [events](Event modding.md) that are called when the on action fires |
| random_events | A single valid event is called from the list, selected by weighted random |
| first_valid | The first valid event is called from the list, determined by the triggers of the called events |
| on_actions | List of on actions that are called when the on action fires |
| random_on_action | A single valid on action is called from the list, selected by weighted random |
| first_valid_on_action | The first valid on action is called from the list, determined by the triggers of the called on_actions |
| effect | [Effects](Effect.md) that are fired with the on action |
| weight_multiplier | A MTTH block that modifies the weight of the on action for use with a random_on_actions block |
| fallback | A single on action that is called if no effects, events, or on actions are fired by this this on action |

Each block can have any number of `delay` blocks. Any events, on actions, or effects after the delay waits until the delay passes.

On actions can also be called with the effect `trigger_event` as such:

```
	trigger_event = {
		on_action = on_action_name
		days/months/years = X  	# Optional, to delay the firing time
	}
```

### Modding on actions

On actions can easily modded by calling a new scripted on action from a hardcoded on action. Only new `on_actions` and `events` block can be added to existing on actions. Adding other blocks to an existing on action causes errors.

For example, to add new effects to the monthly country pulse, use the following template in a new file in the mod's common/on_actions folder:

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

This makes the base game on-action call the modded on-action whenever it fires.

## List of on actions

The given scope is `root` unless otherwise indicated

| Name | Given scope | Description / Notes |
|---|---|---|
| on_acquired_technology | Root = The applicable country scope:technology = The technology type they started to research | If called by effect, call from `country` scope |
| on_ally_capitulated_notification | country |  |
| on_amendment_repealed | Root = country scope:amendment = amendment being repealed |  |
| on_battle_ended | Root = attacker or defender country scope:enemy_country = enemy of root scope:battle = battle scope:attacker = attacking commander scope:defender = defending commander scope:state = location state |  |
| on_battle_lost |  |  |
| on_battle_started |  |  |
| on_battle_won | If called by effect, call from `country` scope |  |
| on_become_independent | Root = newly independent country scope:overlord = former overlord |  |
| on_become_subject | Root = newly subject country scope:overlord = new overlord |  |
| on_building_built | building |  |
| on_building_expanded | building |  |
| on_capitulation | Root = Capitulating country scope:diplomatic_play = diplomatic play |  |
| on_character_creation | character |  |
| on_character_death | character |  |
| on_character_recruitment | character |  |
| on_civil_war_won | country |  |
| on_claim_added | Root = Country (that owns a state in the state region) scope:actor = Claimant country scope:region = State Region claimed |  |
| on_colony_created | state |  |
| on_company_disbanded | Root = Country (in which the company is disbanded) scope:company = The company that was disbanded |  |
| on_company_established | Root = Country (in which the company is established) scope:company = The company that was established |  |
| on_country_broke_treaty | Root = Treaty scope:withdrawing_country = Withdrawing Country scope:non_withdrawing_country = Non-Withdrawing Country | Fires instead of on_country_withdrawn_from_treaty when the binding period is still active |
| on_country_default | country |  |
| on_country_formed | country |  |
| on_country_no_longer_default | country |  |
| on_country_released_as_company_subject | Root = Releasing Country scope:target = Released Country |  |
| on_country_released_as_independent | Root = Releasing Country scope:target = Released Country |  |
| on_country_released_as_overlord_subject | Root = Releasing Country scope:target = Released Country |  |
| on_country_released_as_own_subject | Root = Releasing Country scope:target = Released Country |  |
| on_country_swayed | Root = diplomatic_play scope:actor = swaying country scope:target = target of sway scope:recipient = swayed country scope:notification_target = notified country |  |
| on_country_withdrawn_from_treaty | Root = Treaty scope:withdrawing_country = Withdrawing Country scope:non_withdrawing_country = Non-Withdrawing Country | Fires when the binding period is not active |
| on_create_market | market |  |
| on_deactivate_link |  |  |
| on_decade_pulse_character | character |  |
| on_decade_pulse_country | country | If called by effect, call from `country` scope |
| on_decade_pulse_country_elections | country | Only fires if elections are enabled |
| on_decade_pulse_state | state |  |
| on_demobilized_army | military_formation |  |
| on_demobilized_general | chracter |  |
| on_diplo_play_abandon_side | diplomatic_play |  |
| on_diplo_play_back_down | Root = diplomatic_play scope:actor = country backing down scope:notification_target = notified country |  |
| on_diplo_play_back_down_involved | Root = diplomatic_play scope:actor = country backing down scope:target = leader of opposing side scope:notification_target = notified country |  |
| on_diplo_play_declare_neutrality | Root = diplomatic_play scope:actor = country declaring neutrality scope:initiator = initiator of diploplay scope:target = target of diploplay scope:notification_target = notified country |  |
| on_diplo_play_join_side | Root = diplomatic_play scope:actor = joining country scope:target = target of joined play scope:recipient = joined country scope:notification_target = notified country |  |
| on_diplo_play_start | Root = diplomatic_play scope:actor = initiator of play scope:notification_target = notified country |  |
| on_diplo_play_start_third_party | diplomatic_play |  |
| on_diplo_play_subject_released | diplomatic_play |  |
| on_diplo_play_subject_released_overlord | diplomatic_play |  |
| on_diplo_play_switch_sides | Root = Diplomatic Play scope:country = Country switched to scope:previous = Country switched from |  |
| on_diplo_play_war_start | Root = diplomatic_play scope:actor = initiator of play scope:target = target of play |  |
| on_diplomatic_action | Root = diplomatic_action scope:actor = country performing action scope:recipient = target of action scope:notification_target = notified country |  |
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
| on_diplomatic_demand | Root = diplomatic_demand scope:actor = country performing demand scope:recipient = target of demand scope:notification_target = notified country |  |
| on_diplomatic_demand_accepted | diplomatic_demand |  |
| on_diplomatic_demand_rejected | Root = diplomatic_demand scope:recipient = target of demand scope:notification_target = notified country |  |
| on_diplomatic_incident | Root = Strategic Region scope:actor = Aggressor country scope:target = Target country |  |
| on_diplomatic_pact_auto_break | Root = diplomatic_action scope:country = first country of pact scope:target_country = second country of pact scope:notification_target = notified country |  |
| on_diplomatic_pact_third_party_auto_break | diplomatic_action |  |
| on_diplomatic_play_started | root = The diplomatic play that has been started scope:initiator = Initiator of the play scope:target = Target of the play |  |
| on_diplomatic_proposal | root = diplomatic_action scope:actor = proposer country scope:recipient = proposed country scope:notification_target = notified country |  |
| on_diplomatic_proposal_accepted |  |  |
| on_diplomatic_proposal_break | diplomatic_action |  |
| on_diplomatic_proposal_break_accepted | diplomatic_action |  |
| on_diplomatic_proposal_break_call_in_obligation | diplomatic_action |  |
| on_diplomatic_proposal_break_declined | diplomatic_action |  |
| on_diplomatic_proposal_break_owe_obligation | diplomatic_action |  |
| on_diplomatic_proposal_call_in_obligation | diplomatic_action |  |
| on_diplomatic_proposal_declined | root = diplomatic_action scope:actor = proposer country scope:recipient = proposed country scope:notification_target = notified country |  |
| on_diplomatic_proposal_owe_obligation | diplomatic_action |  |
| on_diplomats_expelled | diplomatic_action |  |
| on_election_campaign_end | country |  |
| on_election_campaign_start | country |  |
| on_empty_battle_lost | Root = attacker or defender country scope:enemy_country = enemy of root scope:battle = battle scope:attacker = attacking commander scope:defender = defending commander scope:state = location state | When one side has no units at end |
| on_empty_battle_won | When one side has no units at end |  |
| on_enemy_capitulated_notification | Root = notified country scope:target = capitulating country scope:diplomatic_play = diplomatic play |  |
| on_enemy_convoys_raided | Root = Country scope:region = the sea region where the raid happened |  |
| on_five_year_pulse_character | character |  |
| on_five_year_pulse_country | country | If called by effect, call from `country` scope |
| on_five_year_pulse_country_elections | country | Only fires if elections are enabled |
| on_five_year_pulse_state | state |  |
| on_game_started | none | Immediately after history, but before country selection (no players) |
| on_game_started_after_lobby | none | Immediately on load after country selection |
| on_government_reformed | country |  |
| on_half_yearly_pulse_character | character |  |
| on_half_yearly_pulse_country | country | If called by effect, call from `country` scope |
| on_half_yearly_pulse_country_elections | country | Only fires if elections are enabled |
| on_half_yearly_pulse_state | state | If called by effect, call from `state` scope |
| on_harvest_condition_started_in_country | Root = country scope:area = harvest condition area scope:state = affected state with the highest intensity scope:duration = duration of the harvest condition in days scope:num_states = the number of affected states in the country scope:intensity = the highest intensity of the affected states |  |
| on_heir_born | character |  |
| on_ig_resigned_government | interest_group |  |
| on_impose_law | Root = country being imposed upon scope:initiator = country doing the imposition scope:law = law being imposed | This on-action is triggered in cases where there is no overriding on_impose effect on a law type. In case an on_impose effect exists on the law type, this will NOT be executed. |
| on_investment_decreased | institution |  |
| on_investment_increased | institution |  |
| on_journal_entry_activated | journal_entry |  |
| on_journal_entry_completed | journal_entry |  |
| on_journal_entry_deactivated | journal_entry |  |
| on_journal_entry_failed | journal_entry |  |
| on_law_activated | law | Cannot use `currently_enacting_law` |
| on_law_checkpoint_advance | country | If called by effect, call from country scope Can use currently_enacting_law |
| on_law_checkpoint_debate | country |  |
| on_law_checkpoint_stall | country |  |
| on_law_checkpoint_success | country | Can use `currently_enacting_law` |
| on_law_enactment_ended | country |  |
| on_law_enactment_fail | country |  |
| on_law_enactment_pass | country |  |
| on_law_enactment_started | country |  |
| on_merge_markets | Root = From Market scope:market = Market merging into scope:trade_center = Trade Center state of root |  |
| on_migration_target_created | Root = state scope:country = source country of migration scope:notification_target = notified country |  |
| on_migration_target_created_other |  |  |
| on_military_formation_created | military_formation |  |
| on_mobilized_army | military_formation |  |
| on_mobilized_general | character |  |
| on_monthly_pulse | none |  |
| on_monthly_pulse_character | character |  |
| on_monthly_pulse_country | country | If called by effect, call from `country` scope |
| on_monthly_pulse_country_elections | country | If called by effect, call from `country` scope Only fires if elections are enabled |
| on_monthly_pulse_state | state |  |
| on_national_awakening_started | Root = Culture scope:region = state region where the awakening started scope:culture = culture that had an awakening |  |
| on_native_uprising | Root = Colonizing country scope:actor = Uprising country |  |
| on_new_culture_obsession | Root = culture scope:goods = obsession goods |  |
| on_new_interest_group_leader | character |  |
| on_new_ruler | Root = character scope:previous = previous ruler |  |
| on_objective_completed | objective |  |
| on_obligation_owed_by_us_expired | country |  |
| on_obligation_owed_to_us_expired | country |  |
| on_our_convoys_raided | Root = Country scope:region - the sea region where the raid happened |  |
| on_party_created | Root = Country scope:target = Party created |  |
| on_party_disbanded | Root = Country scope:target = Party disbanded |  |
| on_peace_agreement_signed_non_participant | country |  |
| on_peace_agreement_signed_war_leader | country |  |
| on_peace_agreement_signed_war_participant | country |  |
| on_political_movement_disbanded | political_movement |  |
| on_political_movement_formed | political_movement |  |
| on_political_movement_supported_law_cancelled | political_movement |  |
| on_power_bloc_struggle_ended | Root = Power Bloc whose leadership position is being fought over scope:successful_contender = country that won the Power Struggle scope:failed_contender = country that lost the Power Struggle |  |
| on_power_bloc_struggle_started | country | Root = Country that started the Power Struggle |
| on_production_method_changed | building |  |
| on_rank_changed | country |  |
| on_repudiate_obligation | country |  |
| on_research_technology_started | Root = The applicable country scope:technology = The technology type they started to research |  |
| on_resource_depleted | state | If called by effect, call from `state` scope |
| on_resource_discovered | Root = state scope:target = building type | If called by effect, call from `state` scope |
| on_retarget_link | state |  |
| on_reverse_sway_offer | diplomatic_play |  |
| on_reverse_sway_offer_accepted | diplomatic_play |  |
| on_reverse_sway_offer_rejected | diplomatic_play |  |
| on_revolution_checkpoint_reached | country | If called by effect, call from `country` scope |
| on_revolution_end | Root = Country scope:target = Uprising country |  |
| on_revolution_start | Root = Country scope:target = Uprising country | Can be used to apply effects to a newly-created revolting country. |
| on_secession_checkpoint_reached | country | If called by effect, call from `country` scope |
| on_secession_country_helped_by_home_country | Root = Home Country scope:target = Secession country |  |
| on_secession_country_not_helped_by_home_country | Root = Home Country scope:target = Secession country |  |
| on_secession_end | Root = Country scope:target = Uprising country |  |
| on_secession_start | Root = Country scope:target = Uprising country | Can be used to apply effects to a newly-created secessionist country. |
| on_self_capitulated_notification | Root = country scope:target = capitulating country scope:diplomatic_play = diplomatic play |  |
| on_spreading_technology | Root = The applicable country scope:technology = The technology type they started to research |  |
| on_start_expanding_building | building |  |
| on_start_supporting_unification | country |  |
| on_state_created | state |  |
| on_state_incorporation | state |  |
| on_state_owner_change | state |  |
| on_stop_supporting_unification | country |  |
| on_sub_objective_completed | objective |  |
| on_sub_objective_failed | objective |  |
| on_sway_offer | Root = diplomatic_play scope:actor = swaying country scope:target = target of sway scope:recipient = swayed country scope:notification_target = notified country |  |
| on_sway_offer_accepted | Root = diplomatic_play scope:target = target of sway scope:recipient = swayed country scope:notification_target = notified country |  |
| on_sway_offer_rejected | diplomatic_play |  |
| on_travel_deploy_to_sea_node_cancelled | Root = Military Formation scope:province = Sea Node we were going to scope:target = current target travel location - HQ or Province (Sea Node) |  |
| on_travel_station_in_hq_cancelled | Root = Military Formation scope:hq = HQ we were going to scope:target = current target travel location - HQ or Province (Sea Node) |  |
| on_travel_to_front_cancelled | Root = Military Formation scope:front = front we were going to scope:target = current target travel location - HQ or Province (Sea Node) |  |
| on_travel_track_formation_cancelled | Root = Military Formation scope:formation = Formation we were tracking scope:target = current target travel location - HQ or Province (Sea Node) |  |
| on_treaty_article_removed | Root = Treaty scope:article = Treaty Article |  |
| on_treaty_dissolved | treaty |  |
| on_treaty_enforced | treaty | Fires in addition to on_treaty_entered_into_force for treaties enforced by plays, etc |
| on_treaty_entered_into_force | treaty |  |
| on_treaty_proposal_declined | Root = treaty scope:declining_country = declining country scope:proposing_country = proposing country |  |
| on_treaty_proposed | root = treaty scope:actor = proposing country scope:recipient = receiving country scope:first_country = proposing country scope:second_country = receiving country |  |
| on_unification_candidate_added | country |  |
| on_unification_candidate_removed | country |  |
| on_war_end | Root = Diplomatic Play scope:actor = Initiator country scope:target = Target country |  |
| on_wargoal_added | Root = Diplomatic Play scope:actor = War Goal Owner scope:war_goal = war goal |  |
| on_wargoal_enforced | Root = Country scope:target = the country the wargoal was enforced against scope:diplomatic_play = the relevant diplomatic play scope:wargoal_impact = the impact of the wargoal enforced |  |
| on_wargoal_removed | Root = Diplomatic Play scope:actor = War Goal Owner |  |
| on_yearly_pulse | none |  |
| on_yearly_pulse_character | character |  |
| on_yearly_pulse_country | country | If called by effect, call from `country` scope |
| on_yearly_pulse_country_elections | country | Only fires if elections are enabled |
| on_yearly_pulse_state | state | If called by effect, call from `state` scope |

## References

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
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
