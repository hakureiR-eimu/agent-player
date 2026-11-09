---
title: Interest group modding
source: https://vic3.paradoxwikis.com/Interest_group_modding
pageid: 3651
categories: [Potentially_outdated, 1.11, Modding]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.11.

See also:
Interest groups
**Interest groups** (often abbreviated as IG) represent common socio-political interests. Each interest group has a number of ideologies, three traits, and a number of other characteristics.

## Example definition

Interest groups are defined in common/interest_groups.

Example interest group definition:
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

## Interest group traits

Interest group traits are defined in common/interest_group_traits. They consist of a script name, an icon, a minimum approval, and a [modifier](Modifier types.md) block.

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

## Interest group script documentation

The following [effects](Effect.md), [event targets](Event target.md), and [triggers](Trigger.md) can be used in interest group scope.

| Effect | Description | Example | Targets |
|---|---|---|---|
| abandon_revolution | Removes interest group from revolution | abandon_revolution = yes/no |  |
| add_ideology | Adds an ideology to scoped interest group | add_ideology = ideology:<ideology key> |  |
| add_modifier | Adds a timed modifier effect to object in scope | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_ruling_interest_group | Adds interest group to government | add_ruling_interest_group = yes/no |  |
| every_political_lobby | Iterate through all political lobbies in a country or interest group | every_political_lobby = { limit = { <triggers> } #optional <effects> } | political_lobby |
| every_preferred_law | Iterate through all active and possible laws in an interest group's country, ordered by how much they prefer that law | every_preferred_law = { limit = { <triggers> } #optional <effects> } | law |
| every_scope_admiral | Iterate through all admirals in a: country, interest group, or military formation | every_scope_admiral = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_character | Iterate through all characters in a: country, interest group, or front | every_scope_character = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_general | Iterate through all generals in a: country, interest group, front, or military formation | every_scope_general = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_politician | Iterate through all politicians in a: country or interest group | every_scope_politician = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_pop | Iterate through all pops in a: country, state, interest group, culture | every_scope_pop = { limit = { <triggers> } #optional <effects> } | pop |
| join_revolution | Adds interest group to ongoing revolution | join_revolution = yes/no |  |
| ordered_political_lobby | Iterate through all political lobbies in a country or interest group | ordered_political_lobby = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_lobby |
| ordered_preferred_law | Iterate through all active and possible laws in an interest group's country, ordered by how much they prefer that law | ordered_preferred_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | law |
| ordered_scope_admiral | Iterate through all admirals in a: country, interest group, or military formation | ordered_scope_admiral = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_character | Iterate through all characters in a: country, interest group, or front | ordered_scope_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_general | Iterate through all generals in a: country, interest group, front, or military formation | ordered_scope_general = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_politician | Iterate through all politicians in a: country or interest group | ordered_scope_politician = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_pop | Iterate through all pops in a: country, state, interest group, culture | ordered_scope_pop = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | pop |
| random_political_lobby | Iterate through all political lobbies in a country or interest group | random_political_lobby = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_lobby |
| random_preferred_law | Iterate through all active and possible laws in an interest group's country, ordered by how much they prefer that law | random_preferred_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | law |
| random_scope_admiral | Iterate through all admirals in a: country, interest group, or military formation | random_scope_admiral = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character |
| random_scope_character | Iterate through all characters in a: country, interest group, or front | random_scope_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character |
| random_scope_general | Iterate through all generals in a: country, interest group, front, or military formation | random_scope_general = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character |
| random_scope_politician | Iterate through all politicians in a: country or interest group | random_scope_politician = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character |
| random_scope_pop | Iterate through all pops in a: country, state, interest group, culture | random_scope_pop = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | pop |
| remove_ideology | Removes an ideology from scoped interest group | remove_ideology = ideology:<ideology key> |  |
| remove_modifier | Removes a timed modifier effect to object in scope | remove_modifier = static_modifier_name |  |
| remove_ruling_interest_group | Removes interest group in scope from government | remove_ruling_interest_group = yes/no |  |
| set_ig_trait | Adds a trait to the Interest Group, or replaces their current trait with the same approval level | set_ig_trait = ig_trait:ig_trait_engines_of_progress | interest_group_trait |
| set_interest_group_name | Renames interest group to the specified loc key | set_interest_group_name = x |  |

| Trigger | Description | Example | Targets |
|---|---|---|---|
| any_political_lobby | Iterate through all political lobbies in a country or interest group | any_political_lobby = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_lobby |
| any_preferred_law | Iterate through all active and possible laws in an interest group's country, ordered by how much they prefer that law | any_preferred_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | law |
| any_scope_admiral | Iterate through all admirals in a: country, interest group, or military formation | any_scope_admiral = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_character | Iterate through all characters in a: country, interest group, or front | any_scope_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_general | Iterate through all generals in a: country, interest group, front, or military formation | any_scope_general = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_politician | Iterate through all politicians in a: country or interest group | any_scope_politician = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_pop | Iterate through all pops in a: country, state, interest group, culture | any_scope_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | pop |
| has_ideology | Check if scoped character or interest group has ideology |  |  |
| has_modifier | Check if a supported scope has a certain timed modifier | has_modifier = <key> |  |
| has_party | True if IG scope has a party | has_party = bool | boolean |
| ig_approval | Compare to scoped interest group approval | ig_approval > 2 ig_approval < happy | value |
| ig_clout | Compare to scoped interest group's clout | ig_clout >= 0.2 | value |
| ig_government_power_share | Compare to scoped interest group's political strength divided by total government political strength | ig_government_power_share >= 0.5 | value |
| interest_group_population | Compares population number in an interest group | interest_group_population > 1000 | value |
| interest_group_population_percentage | Compares percentage of population in an interest group | interest_group_population_percentage > 0.2 | value |
| interest_group_supports_political_movement | Checks whether the scoped interest group supports a political movement | interest_group_supports_political_movement = yes/no | boolean |
| is_in_government | True if IG scope is in the government | is_in_government = bool | boolean |
| is_insurrectionary | Check if country, movement or IG is insurrectionary |  | boolean |
| is_interest_group_type | Checks if Interest Group is of a certain type Can also be used on characters directly | is_interest_group_type = x |  |
| is_marginal | True if IG scope is marginal | is_marginal = bool | boolean |
| is_member_of_any_lobby | Checks if interest group is member of any lobby | is_member_of_any_lobby = yes | boolean |
| is_member_of_lobby | Checks if interest group is member of a certain lobby type | is_member_of_lobby = lobby_type:pro_country_lobby | political_lobby_type |
| is_member_of_party | Checks if Interest Group is a member of target party | is_member_of_party = <party> | party |
| is_powerful | True if IG scope is influential | is_powerful = bool | boolean |
| is_revolutionary | Check if the country, movement or interest group is revolutionary |  | boolean |
| is_same_interest_group_type | Checks if Interest Group is of the same IG type as target | is_interest_group_type = scope:neighbor_leading_ig | interest_group |
| is_secessionist | Check if the country, movement or interest group is secessionist |  | boolean |
| is_strongest_ig_in_government | Checks whether the scoped interest group has the most clout out of all interest groups in government | is_strongest_ig_in_government = yes/no | boolean |
| law_enactment_stance | Compares the stance of the scoped character, movement or interest group has about enactment of the specified law compared to the current active law in the same group |  |  |
| law_stance | Compares the base stance of the scoped character, movement or interest group has about the specified law, ignoring the current active law in the same group |  |  |
| most_powerful_strata | Compares an interest groups most powerful strata |  |  |
| num_political_lobbies | Compare to number of political lobbies in scoped country or interest group | num_political_lobbies > 0 | value |
| prefers_law | Checks if the scoped interest group prefers the specified law over the comparison law | prefers_law = { law = law_type:<law a> comparison_law = law_type:<law b> } |  |

| Event target | Description | To scope |
|---|---|---|
| average_progressiveness | Get the average progressiveness of the scoped character or interest group | value |
| leader | Scope to the leader of the interest group | character |
| lobby_join_weight | Scope to the join weight of an interest group to a particular lobby (lobby_join_weight:root >= 5) | value |
| modifier | Scope to the value of the modifier type of specified key belonging to the current object, example: modifier:country_influence_add | boolean, value |
| owner | Scope to the owner country of object | country |
| party | Scope to the party that an IG is supporting | party |
| type | Scope from an object to its type | amendment_type, building_type, company_type, diplomatic_play_type, harvest_condition_type, institution_type, interest_group_type, law_type, political_movement_type, ship_type, strait_type |

### Interest group modifier types

`interest_group_` [modifier types](Modifier types.md) apply their effects to interest groups. When applied to a country, it applies to all interest groups in the country.

| Modifier type | Localization | Type | Format | Notes |
|---|---|---|---|---|
| interest_group_amenability_add | Interest Group Amenability | additive | good |  |
| interest_group_approval_add | Interest Group Approval | additive | good |  |
| interest_group_ig_armed_forces_approval_add | Armed Forces Approval | additive | good |  |
| interest_group_ig_armed_forces_pol_str_mult | Armed Forces Political Strength | multiplicative | percent, neutral |  |
| interest_group_ig_armed_forces_pop_attraction_mult | Armed Forces Pop Attraction | multiplicative | percent, neutral |  |
| interest_group_ig_devout_approval_add | Devout Approval | additive | good |  |
| interest_group_ig_devout_pol_str_mult | Devout Political Strength | multiplicative | percent, neutral |  |
| interest_group_ig_devout_pop_attraction_mult | Devout Pop Attraction | multiplicative | percent, neutral |  |
| interest_group_ig_industrialists_approval_add | Industrialists Approval | additive | good |  |
| interest_group_ig_industrialists_pol_str_mult | Industrialists Political Strength | multiplicative | percent, neutral |  |
| interest_group_ig_industrialists_pop_attraction_mult | Industrialists Pop Attraction | multiplicative | percent, neutral |  |
| interest_group_ig_intelligentsia_approval_add | Intelligentsia Approval | additive | good |  |
| interest_group_ig_intelligentsia_pol_str_mult | Intelligentsia Political Strength | multiplicative | percent, neutral |  |
| interest_group_ig_intelligentsia_pop_attraction_mult | Intelligentsia Pop Attraction | multiplicative | percent, neutral |  |
| interest_group_ig_landowners_approval_add | Landowners Approval | additive | good |  |
| interest_group_ig_landowners_pol_str_mult | Landowners Political Strength | multiplicative | percent, neutral |  |
| interest_group_ig_landowners_pop_attraction_mult | Landowners Pop Attraction | multiplicative | percent, neutral |  |
| interest_group_ig_petty_bourgeoisie_approval_add | Petite Bourgeoisie Approval | additive | good |  |
| interest_group_ig_petty_bourgeoisie_pol_str_mult | Petite Bourgeoisie Political Strength | multiplicative | percent, neutral |  |
| interest_group_ig_petty_bourgeoisie_pop_attraction_mult | Petite Bourgeoisie Pop Attraction | multiplicative | percent, neutral |  |
| interest_group_ig_rural_folk_approval_add | Rural Folk Approval | additive | good |  |
| interest_group_ig_rural_folk_pol_str_mult | Rural Folk Political Strength | multiplicative | percent, neutral |  |
| interest_group_ig_rural_folk_pop_attraction_mult | Rural Folk Pop Attraction | multiplicative | percent, neutral |  |
| interest_group_ig_trade_unions_approval_add | Trade Unions Approval | additive | good |  |
| interest_group_ig_trade_unions_pol_str_mult | Trade Unions Political Strength | multiplicative | percent, neutral |  |
| interest_group_ig_trade_unions_pop_attraction_mult | Trade Unions Pop Attraction | multiplicative | percent, neutral |  |
| interest_group_in_government_approval_add | Government Interest Group Approval | additive | good |  |
| interest_group_in_government_attraction_mult | Attraction of Interest Groups In Government | multiplicative | percent, neutral |  |
| interest_group_in_opposition_agitator_popularity_add | Popularity of Agitators In Opposition | additive | good |  |
| interest_group_in_opposition_approval_add | Opposition Interest Group Approval | additive | good |  |
| interest_group_pol_str_factor | Interest Group Political Strength | multiplicative | percent, good |  |
| interest_group_pol_str_mult | Interest Group Political Strength | multiplicative | percent, neutral |  |
| interest_group_pop_attraction_mult | Interest Group Pop Attraction | multiplicative | percent, neutral |  |

### Interest group GUI script

Main article:
GUI script
| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessAllIdeologies |  | Unknown | Category: const |
| AccessCheapestLawsToPass |  | Unknown | Category: const |
| AccessCountry |  | Country | Category: const |
| AccessIntrinsicIdeologies |  | Unknown | Category: const |
| AccessLeader |  | Character | Category: const |
| AccessModifier |  | Modifier | Category: const |
| AccessSelf |  | InterestGroup | Category: const |
| AccessTraits |  | Unknown | Category: const |
| CalcApprovalFromLoyalties |  | int32 |  |
| CalcApprovalFromLoyaltiesDesc |  | CString |  |
| GetAffiliationBreakdown |  | CString | Category: nonconst |
| GetAffiliationBreakdownForParty | Party | CString | Category: nonconst |
| GetAffiliationRaw |  | CFixedPoint | Category: nonconst |
| GetAgitators |  | Unknown | Category: nonconst |
| GetAmenability |  | CFixedPoint | Category: nonconst |
| GetAmenabilityLabel |  | CString | Category: nonconst |
| GetApprovalRating |  | CString | Category: nonconst |
| GetApprovalValue |  | int32 | Category: nonconst |
| GetApprovalValueDecayIfEnactedDesc | LawType | CString | Category: nonconst |
| GetApprovalValueDeltaFromEnactment | LawType | int32 | Category: nonconst |
| GetApprovalValueDesc |  | CString | Category: nonconst |
| GetApprovalValueIfEnacted | LawType | int32 | Category: nonconst |
| GetClout |  | CFixedPoint | Category: nonconst |
| GetCloutAsFloat |  | float | Category: nonconst |
| GetCloutSupportingMovement | PoliticalMovement | CFixedPoint | Category: nonconst |
| GetCloutTrend |  | DataTrend | Category: nonconst |
| GetColor |  | CVector4f | Category: nonconst |
| GetCountry |  | Country | Category: nonconst |
| GetCountrySupport |  | CFixedPoint | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetDesc |  | CString | Category: nonconst |
| GetFractionOfCloutSupportingMovement | PoliticalMovement | CFixedPoint | Category: nonconst |
| GetGraphicalLoyalistsRatioInAllInterestGroups |  | float | Category: nonconst |
| GetGraphicalRadicalsRatioInAllInterestGroups |  | float | Category: nonconst |
| GetID |  | uint32 | Category: nonconst |
| GetIdeologyDesc |  | CString | Category: nonconst |
| GetInfluenceDesc |  | CString | Category: nonconst |
| GetInfluenceReason |  | CString | Category: nonconst |
| GetInfluencingMovements |  | Unknown | Category: nonconst |
| GetLawApprovalBreakdown | Law | CString | Category: nonconst |
| GetLawApprovalValue | Unknown | int32 | Category: nonconst |
| GetLawStanceLabel | LawType | CString | Category: nonconst |
| GetLeader |  | Character | Category: nonconst |
| GetLeaderIdeology |  | Ideology | Category: nonconst |
| GetLeaderIdeologyDesc |  | CString | Category: nonconst |
| GetLoyalistsPoliticalStrength |  | int64 | Category: nonconst |
| GetLoyalistsTrend |  | DataTrend | Category: nonconst |
| GetModifier |  | Modifier | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetNameNoIcon |  | CString | Category: nonconst |
| GetNameWithCountryVariant |  | CString | Category: nonconst |
| GetNumLoyalists |  | int64 | Category: nonconst |
| GetNumLoyalistsRatio |  | float | Category: nonconst |
| GetNumNeutrals |  | int64 | Category: nonconst |
| GetNumNeutralsRatio |  | float | Category: nonconst |
| GetNumPossibleLeaderIdeologies |  | int32 | Category: nonconst |
| GetNumRadicals |  | int64 | Category: nonconst |
| GetNumRadicalsRatio |  | float | Category: nonconst |
| GetNumSupportersForMovement | PoliticalMovement | int64 | Category: nonconst |
| GetParty |  | Party | Category: nonconst |
| GetPartyAffiliationHighest |  | Party | Category: nonconst |
| GetPartyAffiliationTooltip |  | CString | Category: nonconst |
| GetPoliticalLobbies |  | Unknown | Category: nonconst |
| GetPoliticalStrength |  | int64 | Category: nonconst |
| GetPoliticalStrengthDesc |  | CString | Category: nonconst |
| GetPoliticalStrengthInState | State | int64 | Category: nonconst |
| GetPoliticalStrengthInStateAsPercentage | State | CFixedPoint | Category: nonconst |
| GetPoliticallyActivePercentage |  | CFixedPoint | Category: nonconst |
| GetPoliticallyActiveRaw |  | int64 | Category: nonconst |
| GetPopPotentialDesc |  | CString | Category: nonconst |
| GetPopWithIG | Unknown | PopWithIG | Category: nonconst |
| GetPopulation |  | int64 | Category: nonconst |
| GetPopulationAsFloat |  | float | Category: nonconst |
| GetPopulationInCountryAsPercentage |  | CFixedPoint | Category: nonconst |
| GetPopulationInState | State | int64 | Category: nonconst |
| GetPopulationNonZero |  | int64 | Category: nonconst |
| GetPossibleCharacterLeaderIdeologies |  | Unknown | Category: nonconst |
| GetPossibleRandomLeaderIdeologies |  | Unknown | Category: nonconst |
| GetRadicalsPoliticalStrength |  | int64 | Category: nonconst |
| GetRadicalsTrend |  | DataTrend | Category: nonconst |
| GetStatusTooltip |  | CString | Category: nonconst |
| GetSupportingPopTypesDesc |  | CString | Category: nonconst |
| GetTextIcon |  | CString | Category: nonconst |
| GetTexture |  | Unknown | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetTotalPoliticalStrengthIncludingPartyVotes |  | int64 | Category: nonconst |
| GetTraitsDesc |  | CString | Category: nonconst |
| GetWillJoinPartyDesc |  | CString | Category: nonconst |
| GetWillJoinPartyTooltip |  | CString | Category: nonconst |
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

| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessSelf |  | InterestGroupTrait | Category: const |
| GetBaseModifiersDesc |  | CString | Category: nonconst |
| GetBaseTriggersDesc |  | CString | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetDesc |  | CString | Category: nonconst |
| GetInactiveString | InterestGroup | CString | Category: nonconst |
| GetModifiersDesc | InterestGroup | CString | Category: nonconst |
| GetName | InterestGroup | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetNameWithStatus | Unknown | CString | Category: nonconst |
| GetTexture |  | Unknown | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetTriggersDesc | InterestGroup | CString | Category: nonconst |
| IsEnabled | InterestGroup | bool |  |
| MakeScope |  | Scope |  |
| Self |  | InterestGroupTrait |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| AccessCountry |  | Country | Category: const |
| AccessLeader |  | Character | Category: const |
| AccessModifier |  | Modifier | Category: const |
| GetCountry |  | Country | Category: nonconst |
| GetLeader |  | Character | Category: nonconst |
| GetLeaderIdeology |  | Ideology | Category: nonconst |
| GetModifier |  | Modifier | Category: nonconst |
| GetParty |  | Party | Category: nonconst |
| GetPartyAffiliationHighest |  | Party | Category: nonconst |
| GetPopWithIG | Pop | PopWithIG | Category: nonconst |
| MakeScope |  | Scope |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| MakeScope |  | Scope |  |

## References

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • Interest groups • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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
