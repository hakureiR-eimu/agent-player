---
title: Modifier types
source: https://vic3.paradoxwikis.com/Modifier_types
pageid: 3448
categories: [1.13, Modding]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

See also:
Modifier modding
**Modifier types** are game script which modify various game statistics or allow or block certain actions. A *static modifier* may include multiple modifier types. Modifier types are also used in many other game objects, such as [laws](Law modding.md), [institutions](Institution modding.md), and [technologies](Technology modding.md), among others.

## Behavior of modifier types

Modifier types can hold a numerical or Boolean value. Identical numerical modifier types affecting the same scope sum together to provide the final effect. Boolean modifier types can return only `yes` or `no`.

There are three categories of modifier types: hardcoded, object-based, and script-only.

- Hardcoded modifier types are defined based on game code and are only minimally moddable.
- Object-based modifier types are defined based on a mix game code and game objects, and new modifier types can be defined for new game objects.
- Script-only modifier types are defined entirely by script and do not have a direct effect on gameplay.

Modifier types have a default value of `0` for numerical types and `no` for Boolean types.

### Modifier blocks

A **modifier block** is an script element that accepts modifier types. A common example is a **static modifier** defined in common/static_modifiers. Some static modifiers are defined in code, generally those in in /Victoria 3/game/common/static_modifiers/00_code_static_modifiers.txt, but most are "event" modifiers, applied with the [effect](Effect.md) `add_modifier`.

A static modifier generally looks like this:

```
unification_prestige = {
	icon = gfx/interface/icons/timed_modifier_icons/modifier_statue_positive.dds
	country_prestige_add = 25
}
```

This includes a modifier icon and a number of modifier types. A static modifier does not need a modifier type, in which case it is mainly cosmetic or indicative of some other mechanic.

Other examples of modifier blocks include [laws](Law modding.md), [technologies](Technology modding.md), and [state traits](State modding.md). In most cases, the modifier block is explicitly labeled with the term `modifier` or a similar variation.

### Modifier type flow

Modifier types "flow" from the object where they are applied to the object type they affect. For example, if a modifier block is applied to a country (say by a law) and contains a `state` modifier type, that modifier type affects all states owned by the country.

[Static modifiers](Modifier modding.md) apply to the scope that they are added to, while other modifier blocks have their behavior determined by game code. For example [production methods](https://vic3.paradoxwikis.com/Production_methods_modding) have three blocks: one that applies only to its building, one that applies to its state, and one that applies to the whole country.

| Target scope | Flows from scopes | Flow Prefix | Notes |
|---|---|---|---|
| Battle | Character Country State (for battles in state) | `battle_` |  |
| Building | Country State | `building_` |  |
| Building group | Country State | `building_group_` |  |
| Character | Military formation | `character_` |  |
| Country |  | `country_` |  |
| Goods | Building Building group Country | `goods_` | _add modifier types only work in production method building modifiers _mult modifier types work anywhere that can flow to buildings |
| Interest group | Country | `interest_group_` |  |
| Market |  | `market_` |  |
| Military formation | Country | `military_formation_` |  |
| Political movement | Country | `political_movement_` |  |
| Power Bloc |  | `power_bloc_` |  |
| Ship | Battle Country Military formation State (for battles in state) | `ship_` | Likely same flow and non-combat effects as Unit |
| State | Country | `state_` |  |
| Tax | Country | `tax_` |  |
| Unit | Battle Character Country Military formation State (for battles in state) | `unit_` | Non-combat unit modifiers flow from Battle, Character, and State but do nothing |

Other connections do not work, so a `battle` modifier type applied to a military formation will not flow through to affect a battle. Note that some flows do not appear to work even if they *should*, such as applying building employment or goods input or output modifier types outside of production methods.

Modifier types can generally "flow through" scopes, so for example a building modifier type applied to a country flows through the country's states and to the states' buildings.

Script-only modifiers flow through if they start with the same pattern as hardcoded or object-based modifiers. So a script-only modifier starting with `building_` should flow through from country to state to building just as others would.

`Unit_` modifiers can flow through either Military Formation or Battle to get to Units. They get to Units from either scope, but not all work when applied from Battle. This appears to be based on whether the modifier applies effects in combat (eg. offense, kill rate) or out of combat (eg. advancement speed, convoy raiding). Note that experience gain modifiers work while in combat, but experience is only added on the weekly tick. If the battle starts and ends without crossing into a new week, they won't do anything. This may not match the expected behaviour.

### Modifier type values in script

The [event target](Event target.md) `modifier` returns the summed value of the given modifier type. This value can be used in [script values](Script value.md) as well as [triggers](Trigger.md) and [effects](Effect.md) that accept script values. For example, a trigger can check if a country has more or less than a certain value of a given modifier type, or an effect can scale its impact by a given modifier type. Boolean modifiers return `yes` or `no` which can be used in direct comparisons or for certain triggers.

## Defining modifier types

All modifier types are defined in common/modifier_type_definitions. Each modifier type is scripted as its own block and may contain a number of parameters:

| Parameter | Description |
|---|---|
| decimals | Defines how many decimals are used in displaying the modifier type's value Unmodified Victoria 3 only uses 0, 1, and 2 |
| color | Defines how the value is colored: neutral, good, or bad `neutral` is always black; `good` uses green for positive, red for negative; `bad` is the opposite. |
| percent | If set to `yes`, displays value as a percentage This multiplies the displayed value by 100 |
| boolean | If set to `yes`, defines the modifier as Boolean instead of numerical |
| prefix | Determines which localization key should be prefixed when displaying the values for entries of this type |
| suffix | Determines which localization key should be suffixed when displaying the values for entries of this type |
| script_only | If set to `yes`, flags the modifier as not interacting with any game mechanics directly; the modifier type value still flows as normal |
| game_data | Used for internal handling, described in modifier_types.md as: # the value to the AI of having this modifier, multiplied by the value to determine the chance the AI will go after static modifiers of this type; only implemented for certain modifier types ai_value = 0 # the alternate modifier definition this type should be treated as in bespoke regions of code. Not generically applicable, used for applying the same effect in contextually appropriate situations translate = battle_offense_add # the modifier typesets this type belongs to, used in code to perform bespoke operations (such as updating cultural community acceptance deltas when a country enacts a law with a modifier entry of this type) type_set = { cultural_acceptance } |

Hardcoded and object-based modifier types must use the exact script name or pattern expected, while script-only modifier types can use any script name.

### Localization

Each modifier type generates two [localization](Localization.md) keys, `<name>` and `<name>_desc`

## Object-based modifiers

Object-based modifiers can be extended for mods that add new types for each object category. Unmodified Victoria 3 contains many, but not all possible modifier types for the game's objects. Some object-based modifiers refer to two objects, while most refer to only one.

| Category | Description | Definition folder |
|---|---|---|
| $AcceptanceStatus$ | Acceptance status | common/acceptance_statuses |
| $BuildingGroup$ | Building group | common/building_groups |
| $BuildingType$ | Building type | common/buildings |
| $Culture$ | Culture | common/cultures |
| $Goods$ | Good type | common/goods |
| $Institution$ | Institution | common/institutions |
| $Law$ | Law | common/laws |
| $InterestGroup$ | Interest Group | common/interest_groups |
| $PoliticalMovement$ | Political movement | common/political_movements |
| $PopType$ | Profession | common/pop_types |
| $Religion$ | Religion | common/religions |
| $SocialClass$ | Social class | common/social_classes |
| $ShipGroup$ | Ship group | common/ship_groups |
| $ShipType$ | Ship type | common/ship_types |

| Modifier type | Description | Category | Type |
|---|---|---|---|
| $BuildingType$_throughput_add | Adds throughput to $BuildingType$ | building | additive |
| building_$PopType$_fertility_mult | Multiplies birth rate of $PopType$ employed in building | building | multiplicative |
| building_$PopType$_job_attractiveness_mult | Multiplies attractiveness of jobs for $PopType$ in building | building | multiplicative |
| building_$PopType$_mortality_mult | Multiplies mortality of $PopType$ employed in building | building | multiplicative |
| building_$PopType$_shares_add | Adds ownership shares for $PopType$ employed in building | building | additive |
| building_$PopType$_shares_mult | Multiplies ownership shares for $PopType$ employed in building | building | multiplicative |
| building_$PopType$_standard_of_living_add | Adds standard of living for $PopType$ employed in building | building | additive |
| building_employment_$PopType$_add | Adds number of $PopType$ employed in building | building | additive |
| building_employment_$PopType$_mult | Multiplies number of $PopType$ employed in building | building | multiplicative |
| building_group_$BuildingGroup$_$PopType$_fertility_mult | Multiplies birth rate of $PopType$ employed in $BuildingGroup$ | building_group | multiplicative |
| building_group_$BuildingGroup$_$PopType$_mortality_mult | Multiplies mortality of $PopType$ employed in $BuildingGroup$ | building_group | multiplicative |
| building_group_$BuildingGroup$_$PopType$_standard_of_living_add | Adds standard of living to $PopType$ employed in $BuildingGroup$ | building_group | additive |
| building_group_$BuildingGroup$_allowed_collectivization_add | Increases collectivization percent of $BuildingGroup$ | building_group | additive |
| building_group_$BuildingGroup$_construction_efficiency_add | Increases construction efficiency for $BuildingGroup$ Requires building group to have `construction_efficiency_modifier = yes` | building_group | additive |
| building_group_$BuildingGroup$_employee_mult | Multiplies number of all pops employed in $BuildingGroup$ | building_group | multiplicative |
| building_group_$BuildingGroup$_fertility_mult | Multiplies birth rate of all pops employed in $BuildingGroup$ | building_group | multiplicative |
| building_group_$BuildingGroup$_infrastructure_usage_mult | Multiplies infrastructure usage of $BuildingGroup$ | building_group | multiplicative |
| building_group_$BuildingGroup$_mortality_mult | Multiplies mortality of all pops employed in $BuildingGroup$ | building_group | multiplicative |
| building_group_$BuildingGroup$_self_investment_chance_add | Adds chance of $BuildingGroup$ to invest in building more of itself | building_group | additive |
| building_group_$BuildingGroup$_standard_of_living_add | Adds standard of living to all pops employed in $BuildingGroup$ | building_group | additive |
| building_group_$BuildingGroup$_tax_mult | Multiplies tax paid by $BuildingGroup$ | building_group | multiplicative |
| building_group_$BuildingGroup$_throughput_add | Adds throughput to $BuildingGroup$ | building_group | additive |
| building_group_$BuildingGroup$_unincorporated_throughput_add | Adds throughput to $BuildingGroup$ built in unincorporated states | building_group | additive |
| country_$BuildingGroup$_require_subsidies_bool | (No base game usage) $BuildingGroup$ must be subsidized? | country | boolean |
| country_$Culture$_cultural_acceptance_add | Adds acceptance for $Culture$ | country | additive |
| country_$Goods$_export_tariffs_rate_add | (No base game usage) Adds export tariffs for $Goods$? | country | additive |
| country_$Goods$_import_tariffs_rate_add | (No base game usage) Adds import tariffs for $Goods$? | country | additive |
| country_$Goods$_max_export_tariffs_level_add | (No base game usage) Adds max export tariff level for $Goods$? | country | additive |
| country_$Goods$_max_import_tariffs_level_add | (No base game usage) Adds max import tariff level for $Goods$? | country | additive |
| country_$Goods$_min_export_tariffs_level_add | (No base game usage) Adds min export tariff level for $Goods$? | country | additive |
| country_$Goods$_min_import_tariffs_level_add | (No base game usage) Adds min import tariff level for $Goods$? | country | additive |
| country_$Institution$_max_investment_add | Increase max investment level of $Institution$ | country | additive |
| country_$PopType$_pol_str_mult | Multiplies political strength of $PopType$ | country | multiplicative |
| country_$PopType$_voting_power_add | Adds voting strength to $PopType$ | country | additive |
| country_$ShipGroup$_construction_efficiency_add | Adds construction efficiency for $ShipGroup$ | country | additive |
| country_$ShipGroup$_construction_progress_max_add | Multiplies maximum weekly construction progress for $ShipGroup$ | country | additive |
| country_$ShipType$_construction_efficiency_add | Adds construction efficiency for $ShipType$ | country | additive |
| country_$SocialClass$_acceptance_max_add | Sets acceptance max for $SocialClass$ | country | additive |
| country_$SocialClass$_acceptance_min_add | Sets acceptance min for $SocialClass$ | country | additive |
| country_$SocialClass$_cultural_acceptance_add | Adds cultural acceptance for $SocialClass$ | country | additive |
| country_$SocialClass$_cultural_acceptance_mult | Multiplies cultural acceptance for $SocialClass$ | country | multiplicative |
| country_$SocialClass$_education_access_add | Adds education access for $SocialClass$ | country | additive |
| country_$SocialClass$_education_access_mult | Multiplies education access for $SocialClass$ | country | multiplicative |
| country_$SocialClass$_qualification_growth_add | Adds qualification growth for $SocialClass$ | country | additive |
| country_$SocialClass$_qualification_growth_mult | Multiplies qualification growth for $SocialClass$ | country | multiplicative |
| country_$SocialClass$_qualification_growth_other_class_mult | Multiplies qualification growth for $SocialClass$ towards other social classes | country | multiplicative |
| country_$SocialClass$_qualification_growth_same_class_mult | Multiplies qualification growth for $SocialClass$ towards other professions in the same social class | country | multiplicative |
| country_allow_assimilation_$AcceptanceStatus$_bool | Allows assimilation of $AcceptanceStatus$ | country | boolean |
| country_allow_conversion_$AcceptanceStatus$_bool | Allows conversion of $AcceptanceStatus$ | country | boolean |
| country_allow_voting_$AcceptanceStatus$_bool | Allows voting by $AcceptanceStatus$ | country | boolean |
| country_assimilation_$AcceptanceStatus$_mult | Multiplies assimilation of $AcceptanceStatus$ | country | multiplicative |
| country_disallow_government_work_$AcceptanceStatus$_bool | Blocks upper and middle strata $AcceptanceStatus$ from working in government-funded buildings | country | boolean |
| country_disallow_military_work_$AcceptanceStatus$_bool | Blocks $AcceptanceStatus$ from working in military buildings | country | boolean |
| country_enactment_speed_$Law$_mult | Multiplies enactment speed for $Law$ | country | multiplicative |
| country_enactment_success_chance_$Law$_add | Adds success chance to enact $Law$ | country | additive |
| country_fervor_target_$Culture$_add | Adds fervor target for $Culture$ | country | additive |
| country_institution_cost_$Institution$_add | Adds bureaucracy cost for $Institution$ | country | additive |
| country_institution_cost_$Institution$_mult | Multiplies bureaucracy cost for $Institution$ | country | multiplicative |
| country_institution_impact_$Institution$_mult | Multiplies effect of $Institution$ | country | multiplicative |
| country_institution_size_change_speed_$Institution$_mult | Multiplies speed of investment change for $Institution$ | country | multiplicative |
| country_loyalism_increases_$AcceptanceStatus$_mult | Multiplies loyalists gain for $AcceptanceStatus$ | country | multiplicative |
| country_political_strength_$AcceptanceStatus$_mult | Multiplies political strength for $AcceptanceStatus$ | country | multiplicative |
| country_qualification_growth_$AcceptanceStatus$_mult | Multiplies qualification growth for $AcceptanceStatus$ | country | multiplicative |
| country_radicalism_increases_$AcceptanceStatus$_mult | Multiplies radicals gain for $AcceptanceStatus$ | country | multiplicative |
| country_standard_of_living_$AcceptanceStatus$_add | Adds standard of living to $AcceptanceStatus$ | country | additive |
| country_voting_power_$AcceptanceStatus$_mult | Multiplies voting strength for $AcceptanceStatus$ | country | multiplicative |
| country_wage_$AcceptanceStatus$_mult | Multiplies wages paid to $AcceptanceStatus$ | country | multiplicative |
| goods_input_$Goods$_add | Adds $Goods$ input for building/production method | goods | additive |
| goods_input_$Goods$_mult | Multiplies $Goods$ input for building/production method | goods | multiplicative |
| goods_output_$Goods$_add | Adds $Goods$ output for building/production method | goods | additive |
| goods_output_$Goods$_mult | Multiplies $Goods$ input for building/production method | goods | multiplicative |
| goods_trade_advantage_$Goods$_mult | Multiplies trade advantage for $Goods$ | goods | multiplicative |
| interest_group_$InterestGroup$_approval_add | Adds approval for $InterestGroup$ | interest_group | additive |
| interest_group_$InterestGroup$_pol_str_mult | Multiplies political strength of $InterestGroup$ | interest_group | multiplicative |
| interest_group_$InterestGroup$_pop_attraction_mult | Multiplies pop attraction of $InterestGroup$ | interest_group | multiplicative |
| ship_$ShipType$_hull_damage_mult | Multiplies hull damage done by $ShipType$ | ship | multiplicative |
| ship_$ShipType$_supply_capacity_mult | Multiplies supply capacity of $ShipType$ | ship | multiplicative |
| ship_battle_against_$ShipType$_accuracy_add | Adds accuracy when targeting $ShipType$ | ship | additive |
| ship_battle_against_$ShipType$_accuracy_mult | Multiplies accuracy when targeting $ShipType$ | ship | multiplicative |
| ship_battle_against_$ShipType$_hull_damage_mult | Multiplies hull damage dealt when targeting $ShipType$ | ship | multiplicative |
| state_$BuildingType$_max_level_add | Adds level max for $BuildingType$ | state | additive |
| state_$Culture$_standard_of_living_add | Adds standard of living for $Culture$ | state | additive |
| state_$PopType$_consumption_multiplier_add | Adds consumption multiplier for $PopType$ | state | additive |
| state_$PopType$_dependent_wage_mult | Multiplies dependent wages for $PopType$ | state | multiplicative |
| state_$PopType$_internal_migration_disallowed_bool | Blocks non-mass migration for $PopType$ | state | boolean |
| state_$PopType$_investment_pool_contribution_add | Adds investment pool contribution for $PopType$ | state | additive |
| state_$PopType$_investment_pool_efficiency_mult | Multiplies investment pool contribution by $PopType$ | state | multiplicative |
| state_$PopType$_mass_migration_disallowed_bool | Blocks mass migration for $PopType$ | state | boolean |
| state_$PopType$_mortality_mult | Multiplies mortality for $PopType$ | state | multiplicative |
| state_$Religion$_standard_of_living_add | Adds standard of living for $Religion$ | state | additive |
| state_buy_orders_$Goods$_add | Adds local buy orders of $Goods$ in state | state | additive |
| state_harvest_condition_$HarvestConditionType$_duration_mult | Multiplies duration of $HarvestConditionType$ | state | multiplicative |
| state_harvest_condition_$HarvestConditionType$_impact_mult | Multiplies effect of $HarvestConditionType$ | state | multiplicative |
| state_infrastructure_from_$Goods$_consumption_add | Adds infrastructure from consumption of $Goods$ in state | state | additive |
| state_pop_support_$PoliticalMovement$_add | Adds pop attraction for $PoliticalMovement$ | state | additive |
| state_pop_support_$PoliticalMovement$_mult | Multiplies pop attraction for $PoliticalMovement$ | state | multiplicative |
| state_sell_orders_$Goods$_add | Adds local sell orders of $Goods$ in state | state | additive |
| unit_$CombatUnit$_offense_add | Adds offense for $CombatUnit$ | unit | additive |
| unit_$CombatUnit$_offense_mult | Adds defense for $CombatUnit$ | unit | multiplicative |
| unit_defense_$TerrainKey$_add | Adds defense in $TerrainKey$ | unit | additive |
| unit_defense_$TerrainKey$_mult | Multiplies defense in $TerrainKey$ | unit | multiplicative |
| unit_offense_$TerrainKey$_add | Adds offense in $TerrainKey$ | unit | additive |
| unit_offense_$TerrainKey$_mult | Multiplies defense in $TerrainKey$ | unit | multiplicative |

## Script-only modifier types

Script-only modifier types do not have a direct effect on the gamestate. Instead, they act as "hooks" for other scripting. For example, the modifier type `country_disallow_law_no_schools_bool` has no effect by itself, but the law No Schools is scripted to be blocked from enactment if this modifier type is set. Script-only modifier types can also be used with scripted values, as for example `power_bloc_mandate_progress_per_major_power_member_add` which is used in a script value to determine mandate growth for a power bloc.

The value of any modifier type can be returned with the [event target](Event target.md) `modifier`. For example, `modifier:country_disallow_law_no_schools_bool` which returns `yes` or `no` depending on the value of the modifier type. Numerical modifiers are summed when returned with `modifier` so that separate sources add together as with hardcoded and object-based modifier types.

Finally, some script-only modifier types act only as indicators while the actual effect is implemented in another way.

## List of all defined modifier types

The following modifiers are all defined in unmodified Victoria 3 in common/modifier_type_definitions. This includes all hardcoded modifier types, many of the potential object-based modifier types, and all script-only modifier types used for base game mechanics. It does not include potential modifier types which are not defined.

The following defined object-based modifier types are not included in the table for sake of concision:

- `country_$Culture$_cultural_acceptance_add`
- `country_$SocialClass$_cultural_acceptance_add`
- `country_fervor_target_$Culture$_add`
- `state_$Culture$_standard_of_living_add`
- `state_$Religion$_standard_of_living_add`

These types are exhaustively defined in the base game and can be seen at [List of culture modifier types](List of culture modifier types.md).

| Modifier type | Localization | Category | Type | Format | Notes |
|---|---|---|---|---|---|
| battle_casualties_mult | Casualties Taken | battle | multiplicative | percent, bad |  |
| battle_combat_width_mult | Terrain Combat Width | battle | multiplicative | percent, good |  |
| battle_defense_owned_province_mult | Home Defense | battle | multiplicative | percent, good |  |
| battle_naval_condition_calm_waters_chance_mult | Calm Waters Chance | battle | multiplicative | percent, neutral |  |
| battle_naval_condition_cyclone_chance_mult | Cyclone Chance | battle | multiplicative | percent, neutral |  |
| battle_naval_condition_fog_chance_mult | Fog Chance | battle | multiplicative | percent, neutral |  |
| battle_naval_condition_ice_chance_mult | Ice Chance | battle | multiplicative | percent, neutral |  |
| battle_naval_condition_rough_waters_chance_mult | Rough Waters Chance | battle | multiplicative | percent, neutral |  |
| battle_naval_condition_strong_winds_chance_mult | Strong Winds Chance | battle | multiplicative | percent, neutral |  |
| battle_naval_condition_tropical_storm_chance_mult | Tropical Storm Chance | battle | multiplicative | percent, neutral |  |
| battle_offense_owned_province_mult | Home Offense | battle | multiplicative | percent, good |  |
| battle_total_combat_width_mult | Total Combat Width | battle | multiplicative | percent, neutral |  |
| building_academics_job_attractiveness_mult | Job Attractiveness for Academics | building | multiplicative | percent, good |  |
| building_academics_mortality_mult | Mortality of Academics | building | multiplicative | percent, bad |  |
| building_academics_shares_add | Academics Pop Ownership Shares | building | additive | neutral |  |
| building_academics_standard_of_living_add | Standard of Living for Academics | building | additive | good |  |
| building_aristocrats_job_attractiveness_mult | Job Attractiveness for Aristocrats | building | multiplicative | percent, good |  |
| building_aristocrats_shares_add | Aristocrats Pop Ownership Shares | building | additive | neutral |  |
| building_aristocrats_standard_of_living_add | Standard of Living for Aristocrats | building | additive | good |  |
| building_arms_industry_throughput_add | Arms Industries building Throughput | building | additive | percent, good |  |
| building_art_academy_throughput_add | Arts Academy building Throughput | building | additive | percent, good |  |
| building_artillery_foundry_throughput_add | Artillery Foundry building Throughput | building | additive | percent, good |  |
| building_automotive_industry_throughput_add | Automotive Industries building Throughput | building | additive | percent, good |  |
| building_barrack_throughput_add | Barracks building Throughput | building | additive | percent, good |  |
| building_bureaucrats_job_attractiveness_mult | Job Attractiveness for Bureaucrats | building | multiplicative | percent, good |  |
| building_bureaucrats_shares_add | Bureaucrats Pop Ownership Shares | building | additive | neutral |  |
| building_bureaucrats_standard_of_living_add | Standard of Living for Bureaucrats | building | additive | good |  |
| building_capitalists_job_attractiveness_mult | Job Attractiveness for Capitalists | building | multiplicative | percent, good |  |
| building_capitalists_shares_add | Capitalists Pop Ownership Shares | building | additive | neutral |  |
| building_capitalists_standard_of_living_add | Standard of Living for Capitalists | building | additive | good |  |
| building_cash_reserves_mult | Maximum Cash Reserves | building | multiplicative | percent, good |  |
| building_chemical_plant_throughput_add | Fertilizer Plants building Throughput | building | additive | percent, good |  |
| building_clergymen_job_attractiveness_mult | Job Attractiveness for Clergymen | building | multiplicative | percent, good |  |
| building_clergymen_shares_add | Clergymen Pop Ownership Shares | building | additive | neutral |  |
| building_clergymen_standard_of_living_add | Standard of Living for Clergymen | building | additive | good |  |
| building_clerks_job_attractiveness_mult | Job Attractiveness for Clerks | building | multiplicative | percent, good |  |
| building_clerks_shares_add | Clerks Pop Ownership Shares | building | additive | neutral |  |
| building_clerks_standard_of_living_add | Standard of Living for Clerks | building | additive | good |  |
| building_coal_mine_throughput_add | Coal Mines building Throughput | building | additive | percent, good |  |
| building_coffee_plantation_throughput_add | Coffee Plantations building Throughput | building | additive | percent, good |  |
| building_company_government_dividends_add | Company Government Dividends | building | additive | percent, neutral |  |
| building_company_worker_dividends_add | Company Workforce Dividends | building | additive | percent, neutral |  |
| building_construction_sector_throughput_add | Construction Sector building Throughput | building | additive | percent, good |  |
| building_cotton_plantation_throughput_add | Cotton Plantations building Throughput | building | additive | percent, good |  |
| building_dye_plantation_throughput_add | Dye Plantations building Throughput | building | additive | percent, good |  |
| building_economy_of_scale_level_cap_add | Economy of Scale Building Level Cap | building | additive | good |  |
| building_electrics_industry_throughput_add | Electrics Industries building Throughput | building | additive | percent, good |  |
| building_employment_academics_add | Academics Per Level | building | additive | neutral |  |
| building_employment_aristocrats_add | Aristocrats Per Level | building | additive | neutral |  |
| building_employment_bureaucrats_add | Bureaucrats Per Level | building | additive | neutral |  |
| building_employment_capitalists_add | Capitalists Per Level | building | additive | neutral |  |
| building_employment_clergymen_add | Clergymen Per Level | building | additive | neutral |  |
| building_employment_clerks_add | Clerks Per Level | building | additive | neutral |  |
| building_employment_engineers_add | Engineers Per Level | building | additive | neutral |  |
| building_employment_farmers_add | Farmers Per Level | building | additive | neutral |  |
| building_employment_laborers_add | Laborers Per Level | building | additive | neutral |  |
| building_employment_machinists_add | Machinists Per Level | building | additive | neutral |  |
| building_employment_officers_add | Officers Per Level | building | additive | neutral |  |
| building_employment_peasants_add | Peasants Per Level | building | additive | neutral |  |
| building_employment_shopkeepers_add | Shopkeepers Per Level | building | additive | neutral |  |
| building_employment_slaves_add | Slaves Per Level | building | additive | neutral |  |
| building_employment_soldiers_add | Servicemen Per Level | building | additive | neutral |  |
| building_engineers_job_attractiveness_mult | Job Attractiveness for Engineers | building | multiplicative | percent, good |  |
| building_engineers_mortality_mult | Mortality of Engineers | building | multiplicative | percent, bad |  |
| building_engineers_shares_add | Engineers Pop Ownership Shares | building | additive | neutral |  |
| building_engineers_standard_of_living_add | Standard of Living for Engineers | building | additive | good |  |
| building_explosives_factory_throughput_add | Explosives Factory building Throughput | building | additive | percent, good |  |
| building_farmers_job_attractiveness_mult | Job Attractiveness for Farmers | building | multiplicative | percent, good |  |
| building_farmers_standard_of_living_add | Standard of Living for Farmers | building | additive | good |  |
| building_fishing_wharf_throughput_add | Fishing Wharves building Throughput | building | additive | percent, good |  |
| building_food_industry_throughput_add | Food Industries building Throughput | building | additive | percent, good |  |
| building_furniture_manufactory_throughput_add | Furniture Manufacturies building Throughput | building | additive | percent, good |  |
| building_glassworks_throughput_add | Glassworks building Throughput | building | additive | percent, good |  |
| building_gold_field_throughput_add | Gold Fields building Throughput | building | additive | percent, good |  |
| building_gold_mine_throughput_add | Gold Mines building Throughput | building | additive | percent, good |  |
| building_goods_input_mult | Goods Input | building | multiplicative | percent, bad |  |
| building_government_administration_throughput_add | Government Administration building Throughput | building | additive | percent, good |  |
| building_group_bg_agriculture_allowed_collectivization_add | Minimum Worker-Owned Agriculture Building Levels | building_group | additive | percent, good |  |
| building_group_bg_agriculture_construction_efficiency_add | Agriculture Construction Efficiency | building_group | additive | percent, good |  |
| building_group_bg_agriculture_employee_mult | Agriculture Employees | building_group | multiplicative | percent, bad |  |
| building_group_bg_agriculture_farmers_mortality_mult | Mortality of Farmers employed in Agriculture | building_group | multiplicative | percent, bad |  |
| building_group_bg_agriculture_infrastructure_usage_mult | Infrastructure Usage of Agriculture buildings | building_group | multiplicative | percent, bad |  |
| building_group_bg_agriculture_laborers_mortality_mult | Mortality of Laborers employed in Agriculture | building_group | multiplicative | percent, bad |  |
| building_group_bg_agriculture_mortality_mult | Agriculture Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_agriculture_self_investment_chance_add | Agriculture Building Self-Investment Chance | building_group | additive | percent, neutral |  |
| building_group_bg_agriculture_standard_of_living_add | Agriculture Employee Standard of Living | building_group | additive | good |  |
| building_group_bg_agriculture_tax_mult | Agriculture Tax Income | building_group | multiplicative | percent, neutral |  |
| building_group_bg_agriculture_throughput_add | Agriculture Throughput | building_group | additive | percent, good |  |
| building_group_bg_arts_allowed_collectivization_add | Minimum Worker-Owned Arts Buildings Building Levels | building_group | additive | percent, good |  |
| building_group_bg_arts_throughput_add | Arts Buildings Throughput | building_group | additive | percent, good |  |
| building_group_bg_construction_infrastructure_usage_mult | Infrastructure Usage of Construction Sector buildings | building_group | multiplicative | percent, bad |  |
| building_group_bg_construction_laborers_mortality_mult | Mortality of Laborers employed in Construction | building_group | multiplicative | percent, bad |  |
| building_group_bg_extraction_allowed_collectivization_add | Minimum Worker-Owned Extraction Building Levels | building_group | additive | percent, good |  |
| building_group_bg_extraction_construction_efficiency_add | Extraction Construction Efficiency | building_group | additive | percent, good |  |
| building_group_bg_extraction_self_investment_chance_add | Extraction Building Self-Investment Chance | building_group | additive | percent, neutral |  |
| building_group_bg_extraction_throughput_add | Extraction Throughput | building_group | additive | percent, good |  |
| building_group_bg_fishing_employee_mult | Fishing Employees | building_group | multiplicative | percent, bad |  |
| building_group_bg_fishing_engineers_mortality_mult | Mortality of Engineers employed in Fishing Wharves | building_group | multiplicative | percent, bad |  |
| building_group_bg_fishing_laborers_mortality_mult | Mortality of Laborers employed in Fishing Wharves | building_group | multiplicative | percent, bad |  |
| building_group_bg_fishing_machinists_mortality_mult | Mortality of Machinists employed in Fishing Wharves | building_group | multiplicative | percent, bad |  |
| building_group_bg_fishing_mortality_mult | Fishing Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_fishing_standard_of_living_add | Fishing Employee Standard of Living | building_group | additive | good |  |
| building_group_bg_fishing_tax_mult | Fishing Tax Income | building_group | multiplicative | percent, neutral |  |
| building_group_bg_fishing_throughput_add | Fishing Industry Throughput | building_group | additive | percent, good |  |
| building_group_bg_government_construction_efficiency_add | Government Structures Construction Efficiency | building_group | additive | percent, good |  |
| building_group_bg_government_employee_mult | Government Employees | building_group | multiplicative | percent, bad |  |
| building_group_bg_government_mortality_mult | Government Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_government_standard_of_living_add | Government Employee Standard of Living | building_group | additive | good |  |
| building_group_bg_government_tax_mult | Government Tax Income | building_group | multiplicative | percent, neutral |  |
| building_group_bg_government_throughput_add | Government Structures Throughput | building_group | additive | percent, good |  |
| building_group_bg_heavy_industry_allowed_collectivization_add | Minimum Worker-Owned Heavy Industries Building Levels | building_group | additive | percent, good |  |
| building_group_bg_heavy_industry_construction_efficiency_add | Heavy Industries Construction Efficiency | building_group | additive | percent, good |  |
| building_group_bg_heavy_industry_engineers_mortality_mult | Mortality of Engineers employed in Heavy Industry | building_group | multiplicative | percent, bad |  |
| building_group_bg_heavy_industry_laborers_mortality_mult | Mortality of Laborers employed in Heavy Industry | building_group | multiplicative | percent, bad |  |
| building_group_bg_heavy_industry_machinists_mortality_mult | Mortality of Machinists employed in Heavy Industry | building_group | multiplicative | percent, bad |  |
| building_group_bg_heavy_industry_mortality_mult | Heavy Industry Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_heavy_industry_throughput_add | Heavy Industries Throughput | building_group | additive | percent, good |  |
| building_group_bg_infrastructure_construction_efficiency_add | Infrastructure Construction Efficiency | building_group | additive | percent, good |  |
| building_group_bg_infrastructure_employee_mult | Infrastructure Employees | building_group | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_engineers_mortality_mult | Mortality of Engineers employed in Infrastructure | building_group | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_laborers_mortality_mult | Mortality of Laborers employed in Infrastructure | building_group | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_machinists_mortality_mult | Mortality of Machinists employed in Infrastructure | building_group | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_mortality_mult | Infrastructure Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_self_investment_chance_add | Infrastructure Building Self-Investment Chance | building_group | additive | percent, neutral |  |
| building_group_bg_infrastructure_standard_of_living_add | Infrastructure Employee Standard of Living | building_group | additive | good |  |
| building_group_bg_infrastructure_tax_mult | Infrastructure Tax Income | building_group | multiplicative | percent, neutral |  |
| building_group_bg_infrastructure_throughput_add | Infrastructure Throughput | building_group | additive | percent, good |  |
| building_group_bg_light_industry_allowed_collectivization_add | Minimum Worker-Owned Light Industries Building Levels | building_group | additive | percent, good |  |
| building_group_bg_light_industry_construction_efficiency_add | Light Industries Construction Efficiency | building_group | additive | percent, good |  |
| building_group_bg_light_industry_laborers_mortality_mult | Mortality of Laborers employed in Light Industry | building_group | multiplicative | percent, bad |  |
| building_group_bg_light_industry_machinists_mortality_mult | Mortality of Machinists employed in Light Industry | building_group | multiplicative | percent, bad |  |
| building_group_bg_light_industry_throughput_add | Light Industries Throughput | building_group | additive | percent, good |  |
| building_group_bg_logging_employee_mult | Logging Industry Employees | building_group | multiplicative | percent, bad |  |
| building_group_bg_logging_engineers_mortality_mult | Mortality of Engineers employed in Logging | building_group | multiplicative | percent, bad |  |
| building_group_bg_logging_laborers_mortality_mult | Mortality of Laborers employed in Logging | building_group | multiplicative | percent, bad |  |
| building_group_bg_logging_machinists_mortality_mult | Mortality of Machinists employed in Logging | building_group | multiplicative | percent, bad |  |
| building_group_bg_logging_mortality_mult | Logging Industry Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_logging_slaves_mortality_mult | Mortality of Slaves employed in Logging | building_group | multiplicative | percent, bad |  |
| building_group_bg_logging_standard_of_living_add | Logging Industry Employee Standard of Living | building_group | additive | good |  |
| building_group_bg_logging_tax_mult | Logging Industry Tax Income | building_group | multiplicative | percent, neutral |  |
| building_group_bg_logging_throughput_add | Logging Industry Throughput | building_group | additive | percent, good |  |
| building_group_bg_logging_unincorporated_throughput_add | Forestries Throughput in Unincorporated States | building_group | additive | percent, good |  |
| building_group_bg_manor_houses_aristocrats_standard_of_living_add | Standard of Living of Aristocrats employed in Manor Houses | building_group | additive | good |  |
| building_group_bg_manufacturing_allowed_collectivization_add | Minimum Worker-Owned Manufacturing Industries Building Levels | building_group | additive | percent, good |  |
| building_group_bg_manufacturing_employee_mult | Manufacturing Employees | building_group | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_engineers_mortality_mult | Mortality of Engineers employed in Manufacturing | building_group | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_engineers_standard_of_living_add | Standard of Living of Engineers employed in Manufacturing | building_group | additive | good |  |
| building_group_bg_manufacturing_laborers_mortality_mult | Mortality of Laborers employed in Manufacturing | building_group | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_laborers_standard_of_living_add | Standard of Living of Laborers employed in Manufacturing | building_group | additive | good |  |
| building_group_bg_manufacturing_machinists_mortality_mult | Mortality of Machinists employed in Manufacturing | building_group | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_machinists_standard_of_living_add | Standard of Living of Machinists employed in Manufacturing | building_group | additive | good |  |
| building_group_bg_manufacturing_mortality_mult | Manufacturing Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_self_investment_chance_add | Manufacturing Industries Building Self-Investment Chance | building_group | additive | percent, neutral |  |
| building_group_bg_manufacturing_standard_of_living_add | Manufacturing Employee Standard of Living | building_group | additive | good |  |
| building_group_bg_manufacturing_tax_mult | Manufacturing Tax Income | building_group | multiplicative | percent, neutral |  |
| building_group_bg_manufacturing_throughput_add | Manufacturing Industries Throughput | building_group | additive | percent, good |  |
| building_group_bg_manufacturing_unincorporated_throughput_add | Manufacturing Industries Throughput in Unincorporated States | building_group | additive | percent, good |  |
| building_group_bg_military_construction_efficiency_add | Military Buildings Construction Efficiency | building_group | additive | percent, good |  |
| building_group_bg_military_industry_allowed_collectivization_add | Minimum Worker-Owned Military Industries Building Levels | building_group | additive | percent, good |  |
| building_group_bg_military_industry_construction_efficiency_add | Military Industries Construction Efficiency | building_group | additive | percent, good |  |
| building_group_bg_military_industry_engineers_mortality_mult | Mortality of Engineers employed in Military Industry | building_group | multiplicative | percent, bad |  |
| building_group_bg_military_industry_laborers_mortality_mult | Mortality of Laborers employed in Military Industry | building_group | multiplicative | percent, bad |  |
| building_group_bg_military_industry_machinists_mortality_mult | Mortality of Machinists employed in Military Industry | building_group | multiplicative | percent, bad |  |
| building_group_bg_military_industry_mortality_mult | Military Industry Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_military_industry_throughput_add | Military Industries Throughput | building_group | additive | percent, good |  |
| building_group_bg_military_throughput_add | Military Buildings Throughput | building_group | additive | percent, good |  |
| building_group_bg_mining_allowed_collectivization_add | Minimum Worker-Owned Mines Building Levels | building_group | additive | percent, good |  |
| building_group_bg_mining_employee_mult | Mining Employees | building_group | multiplicative | percent, bad |  |
| building_group_bg_mining_engineers_mortality_mult | Mortality of Engineers employed in Mines | building_group | multiplicative | percent, bad |  |
| building_group_bg_mining_engineers_standard_of_living_add | Standard of Living of Engineers employed in Mines | building_group | additive | good |  |
| building_group_bg_mining_laborers_mortality_mult | Mortality of Laborers employed in Mines | building_group | multiplicative | percent, bad |  |
| building_group_bg_mining_laborers_standard_of_living_add | Standard of Living of Laborers employed in Mines | building_group | additive | good |  |
| building_group_bg_mining_machinists_mortality_mult | Mortality of Machinists employed in Mines | building_group | multiplicative | percent, bad |  |
| building_group_bg_mining_machinists_standard_of_living_add | Standard of Living of Machinists employed in Mines | building_group | additive | good |  |
| building_group_bg_mining_mortality_mult | Mining Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_mining_slaves_mortality_mult | Mortality of Slaves employed in Mines | building_group | multiplicative | percent, bad |  |
| building_group_bg_mining_standard_of_living_add | Mining Employee Standard of Living | building_group | additive | good |  |
| building_group_bg_mining_tax_mult | Mining Tax Income | building_group | multiplicative | percent, neutral |  |
| building_group_bg_mining_throughput_add | Mines Throughput | building_group | additive | percent, good |  |
| building_group_bg_mining_unincorporated_throughput_add | Mines Throughput in Unincorporated States | building_group | additive | percent, good |  |
| building_group_bg_oil_extraction_employee_mult | Oil Industry Employees | building_group | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_engineers_mortality_mult | Mortality of Engineers employed in Oil Extraction | building_group | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_laborers_mortality_mult | Mortality of Laborers employed in Oil Extraction | building_group | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_machinists_mortality_mult | Mortality of Machinists employed in Oil Extraction | building_group | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_mortality_mult | Oil Industry Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_standard_of_living_add | Oil Industry Employee Standard of Living | building_group | additive | good |  |
| building_group_bg_oil_extraction_tax_mult | Oil Industry Tax Income | building_group | multiplicative | percent, neutral |  |
| building_group_bg_oil_extraction_throughput_add | Oil Extractors Throughput | building_group | additive | percent, good |  |
| building_group_bg_plantations_allowed_collectivization_add | Minimum Worker-Owned Plantations Building Levels | building_group | additive | percent, good |  |
| building_group_bg_plantations_construction_efficiency_add | Plantations Construction Efficiency | building_group | additive | percent, good |  |
| building_group_bg_plantations_employee_mult | Plantation Employees | building_group | multiplicative | percent, bad |  |
| building_group_bg_plantations_farmers_mortality_mult | Mortality of Farmers employed on Plantations | building_group | multiplicative | percent, bad |  |
| building_group_bg_plantations_infrastructure_usage_mult | Infrastructure Usage of Plantations | building_group | multiplicative | percent, bad |  |
| building_group_bg_plantations_laborers_mortality_mult | Mortality of Laborers employed on Plantations | building_group | multiplicative | percent, bad |  |
| building_group_bg_plantations_mortality_mult | Plantation Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_plantations_self_investment_chance_add | Plantations Building Self-Investment Chance | building_group | additive | percent, neutral |  |
| building_group_bg_plantations_slaves_mortality_mult | Mortality of Slaves employed in Plantations | building_group | multiplicative | percent, bad |  |
| building_group_bg_plantations_standard_of_living_add | Plantation Employee Standard of Living | building_group | additive | good |  |
| building_group_bg_plantations_tax_mult | Plantation Tax Income | building_group | multiplicative | percent, neutral |  |
| building_group_bg_plantations_throughput_add | Plantations Throughput | building_group | additive | percent, good |  |
| building_group_bg_plantations_unincorporated_throughput_add | Plantations Throughput in Unincorporated States | building_group | additive | percent, good |  |
| building_group_bg_power_allowed_collectivization_add | Minimum Worker-Owned Power Plants Building Levels | building_group | additive | percent, good |  |
| building_group_bg_power_self_investment_chance_add | Power Plants Building Self-Investment Chance | building_group | additive | percent, neutral |  |
| building_group_bg_private_infrastructure_allowed_collectivization_add | Minimum Worker-Owned Private Infrastructure Building Levels | building_group | additive | percent, good |  |
| building_group_bg_ranching_allowed_collectivization_add | Minimum Worker-Owned Ranches Building Levels | building_group | additive | percent, good |  |
| building_group_bg_ranching_construction_efficiency_add | Ranches Construction Efficiency | building_group | additive | percent, good |  |
| building_group_bg_ranching_farmers_mortality_mult | Mortality of Farmers employed in Ranching | building_group | multiplicative | percent, bad |  |
| building_group_bg_ranching_infrastructure_usage_mult | Infrastructure Usage of Ranches | building_group | multiplicative | percent, bad |  |
| building_group_bg_ranching_laborers_mortality_mult | Mortality of Laborers employed in Ranching | building_group | multiplicative | percent, bad |  |
| building_group_bg_ranching_mortality_mult | Ranching Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_ranching_self_investment_chance_add | Ranches Building Self-Investment Chance | building_group | additive | percent, neutral |  |
| building_group_bg_ranching_standard_of_living_add | Ranching Employee Standard of Living | building_group | additive | good |  |
| building_group_bg_ranching_tax_mult | Ranching Tax Income | building_group | multiplicative | percent, neutral |  |
| building_group_bg_ranching_throughput_add | Ranches Throughput | building_group | additive | percent, good |  |
| building_group_bg_rubber_employee_mult | Rubber Industry Employees | building_group | multiplicative | percent, bad |  |
| building_group_bg_rubber_laborers_mortality_mult | Mortality of Laborers employed on Rubber Plantations | building_group | multiplicative | percent, bad |  |
| building_group_bg_rubber_mortality_mult | Rubber Industry Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_rubber_slaves_mortality_mult | Mortality of Slaves employed on Rubber Plantations | building_group | multiplicative | percent, bad |  |
| building_group_bg_rubber_standard_of_living_add | Rubber Industry Employee Standard of Living | building_group | additive | good |  |
| building_group_bg_rubber_tax_mult | Rubber Industry Tax Income | building_group | multiplicative | percent, neutral |  |
| building_group_bg_rubber_throughput_add | Rubber Plantations Throughput | building_group | additive | percent, good |  |
| building_group_bg_rubber_unincorporated_throughput_add | Rubber Plantations Throughput in Unincorporated States | building_group | additive | percent, good |  |
| building_group_bg_service_employee_mult | Urban Center Employees | building_group | multiplicative | percent, bad |  |
| building_group_bg_service_mortality_mult | Urban Center Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_service_standard_of_living_add | Urban Center Employee Standard of Living | building_group | additive | good |  |
| building_group_bg_service_tax_mult | Urban Center Tax Income | building_group | multiplicative | percent, neutral |  |
| building_group_bg_service_throughput_add | Service Industries Throughput | building_group | additive | percent, good |  |
| building_group_bg_subsistence_agriculture_allowed_collectivization_add | Minimum Worker-Owned Subsistence Agriculture Building Levels | building_group | additive | percent, good |  |
| building_group_bg_subsistence_agriculture_peasants_standard_of_living_add | Standard of Living of Peasants employed in Subsistence Agriculture | building_group | additive | good |  |
| building_group_bg_subsistence_ranching_allowed_collectivization_add | Minimum Worker-Owned Subsistence Ranching Building Levels | building_group | additive | percent, good |  |
| building_group_bg_subsistence_ranching_peasants_standard_of_living_add | Standard of Living of Peasants employed in Subsistence Ranching | building_group | additive | good |  |
| building_group_bg_whaling_employee_mult | Whaling Employees | building_group | multiplicative | percent, bad |  |
| building_group_bg_whaling_laborers_mortality_mult | Mortality of Laborers employed in Whaling Stations | building_group | multiplicative | percent, bad |  |
| building_group_bg_whaling_machinists_mortality_mult | Mortality of Machinists employed in Whaling Stations | building_group | multiplicative | percent, bad |  |
| building_group_bg_whaling_mortality_mult | Whaling Employee Mortality | building_group | multiplicative | percent, bad |  |
| building_group_bg_whaling_standard_of_living_add | Whaling Employee Standard of Living | building_group | additive | good |  |
| building_group_bg_whaling_tax_mult | Whaling Tax Income | building_group | multiplicative | percent, neutral |  |
| building_group_bg_whaling_throughput_add | Whaling Industry Throughput | building_group | additive | percent, good |  |
| building_iron_mine_throughput_add | Iron Mines building Throughput | building | additive | percent, good |  |
| building_job_attractiveness_mult | Job Attractiveness | building | multiplicative | percent, good |  |
| building_laborers_job_attractiveness_mult | Job Attractiveness for Laborers | building | multiplicative | percent, good |  |
| building_laborers_mortality_mult | Mortality of Laborers | building | multiplicative | percent, bad |  |
| building_laborers_shares_add | Laborers Pop Ownership Shares | building | additive | neutral |  |
| building_laborers_standard_of_living_add | Standard of Living for Laborers | building | additive | good |  |
| building_lead_mine_throughput_add | Lead Mines building Throughput | building | additive | percent, good |  |
| building_level_bureaucracy_cost_add | Building Level Bureaucracy Cost | building | additive | bad |  |
| building_livestock_ranch_throughput_add | Livestock Ranches building Throughput | building | additive | percent, good |  |
| building_machinists_job_attractiveness_mult | Job Attractiveness for Machinists | building | multiplicative | percent, good |  |
| building_machinists_mortality_mult | Mortality of Machinists | building | multiplicative | percent, bad |  |
| building_machinists_shares_add | Machinists Pop Ownership Shares | building | additive | neutral |  |
| building_machinists_standard_of_living_add | Standard of Living for Machinists | building | additive | good |  |
| building_maize_farm_throughput_add | Maize Farms building Throughput | building | additive | percent, good |  |
| building_millet_farm_throughput_add | Millet Farms building Throughput | building | additive | percent, good |  |
| building_minimum_incorporated_subsistence_employment_add | Protected Subsistence Employment in Incorporated States | building | additive | percent, neutral |  |
| building_minimum_wage_mult | Building Wage Target | building | multiplicative | percent, neutral |  |
| building_mobilization_cost_mult | Mobilization Goods Requirements | building | multiplicative | percent, bad |  |
| building_motor_industry_throughput_add | Motor Industries building Throughput | building | additive | percent, good |  |
| building_munition_plant_throughput_add | Munition Plants building Throughput | building | additive | percent, good |  |
| building_nationalization_cost_mult | Nationalization Compensation | building | multiplicative | percent, bad |  |
| building_nationalization_investment_return_add | Nationalization Investment Return | building | additive | percent, good |  |
| building_nationalization_radicals_mult | Radicals from Nationalization | building | multiplicative | percent, bad |  |
| building_naval_administration_hiring_rate_mult | Naval Administration Hiring Speed | building | multiplicative | percent, good |  |
| building_naval_administration_throughput_add | Naval Administration building Throughput | building | additive | percent, good |  |
| building_naval_administration_training_rate_add | Naval Administration Training Rate | building | additive | good |  |
| building_naval_administration_training_rate_mult | Naval Administration Training Rate | building | multiplicative | percent, good |  |
| building_officers_job_attractiveness_mult | Job Attractiveness for Officers | building | multiplicative | percent, good |  |
| building_officers_shares_add | Officers Pop Ownership Shares | building | additive | neutral |  |
| building_officers_standard_of_living_add | Standard of Living for Officers | building | additive | good |  |
| building_opium_plantation_throughput_add | Opium Plantations building Throughput | building | additive | percent, good |  |
| building_paper_mill_throughput_add | Paper Mills building Throughput | building | additive | percent, good |  |
| building_peasants_job_attractiveness_mult | Job Attractiveness for Peasants | building | multiplicative | percent, good |  |
| building_peasants_standard_of_living_add | Standard of Living for Peasants | building | additive | good |  |
| building_port_throughput_add | Port building Throughput | building | additive | percent, good |  |
| building_power_plant_throughput_add | Power Plants building Throughput | building | additive | percent, good |  |
| building_railway_throughput_add | Railway building Throughput | building | additive | percent, good |  |
| building_rice_farm_throughput_add | Rice Farms building Throughput | building | additive | percent, good |  |
| building_rubber_plantation_throughput_add | Rubber Plantations building Throughput | building | additive | percent, good |  |
| building_rye_farm_throughput_add | Rye Farms building Throughput | building | additive | percent, good |  |
| building_self_investment_chance_add | Building Self-Investment Chance | building | additive | percent, neutral |  |
| building_shipyard_throughput_add | Shipyards building Throughput | building | additive | percent, good |  |
| building_shopkeepers_job_attractiveness_mult | Job Attractiveness for Shopkeepers | building | multiplicative | percent, good |  |
| building_shopkeepers_shares_add | Shopkeepers Pop Ownership Shares | building | additive | neutral |  |
| building_shopkeepers_standard_of_living_add | Standard of Living for Shopkeepers | building | additive | good |  |
| building_silk_plantation_throughput_add | Silk Plantations building Throughput | building | additive | percent, good |  |
| building_slaves_mortality_mult | Mortality of Slaves | building | multiplicative | percent, bad |  |
| building_slaves_standard_of_living_add | Standard of Living for Slaves | building | additive | good |  |
| building_soldiers_job_attractiveness_mult | Job Attractiveness for Servicemen | building | multiplicative | percent, good |  |
| building_soldiers_shares_add | Servicemen Pop Ownership Shares | building | additive | neutral |  |
| building_soldiers_standard_of_living_add | Standard of Living for Servicemen | building | additive | good |  |
| building_steel_mill_throughput_add | Steel Mills building Throughput | building | additive | percent, good |  |
| building_subsistence_farm_throughput_add | Subsistence Farms building Throughput | building | additive | percent, good |  |
| building_subsistence_output_add | Subsistence Output | building | additive | neutral |  |
| building_subsistence_output_mult | Subsistence Output | building | multiplicative | percent, neutral |  |
| building_sugar_plantation_throughput_add | Sugar Plantations building Throughput | building | additive | percent, good |  |
| building_sulfur_mine_throughput_add | Sulfur Mines building Throughput | building | additive | percent, good |  |
| building_synthetics_plant_throughput_add | Synthetics Plants building Throughput | building | additive | percent, good |  |
| building_tea_plantation_throughput_add | Tea Plantations building Throughput | building | additive | percent, good |  |
| building_textile_mill_throughput_add | Textile Mills building Throughput | building | additive | percent, good |  |
| building_throughput_add | Throughput | building | additive | percent, good |  |
| building_tobacco_plantation_throughput_add | Tobacco Plantations building Throughput | building | additive | percent, good |  |
| building_tooling_workshop_throughput_add | Tooling Workshops building Throughput | building | additive | percent, good |  |
| building_trade_center_throughput_add | Trade Center building Throughput | building | additive | percent, good |  |
| building_training_rate_add | Training Rate | building | additive | good |  |
| building_training_rate_mult | Training Rate | building | multiplicative | percent, good |  |
| building_unincorporated_subsistence_output_mult | Subsistence Output in Unincorporated States | building | multiplicative | percent, good |  |
| building_unincorporated_throughput_add | Throughput in Unincorporated States | building | additive | percent, good |  |
| building_university_throughput_add | University building Throughput | building | additive | percent, good |  |
| building_urban_center_throughput_add | Urban Center building Throughput | building | additive | percent, good |  |
| building_vineyard_throughput_add | Vineyards building Throughput | building | additive | percent, good |  |
| building_whaling_station_throughput_add | Whaling Stations building Throughput | building | additive | percent, good |  |
| building_wheat_farm_throughput_add | Wheat Farms building Throughput | building | additive | percent, good |  |
| building_working_conditions_mult | Dangerous Working Conditions | building | multiplicative | percent, bad |  |
| character_advancement_speed_add | General Advancement Speed | character | additive | good |  |
| character_advancement_speed_mult | General Advancement Speed | character | multiplicative | percent, good |  |
| character_battle_condition_aggressive_maneuver_mult | Aggressive Maneuver Chance | character | multiplicative | percent, neutral |  |
| character_battle_condition_blunder_mult | Blunder Chance | character | multiplicative | percent, bad |  |
| character_battle_condition_broken_supply_line_mult | Broken Supply Line Chance | character | multiplicative | percent, bad |  |
| character_battle_condition_camouflaged_mult | Camouflaged Chance | character | multiplicative | percent, good |  |
| character_battle_condition_careful_maneuver_mult | Careful Maneuver Chance | character | multiplicative | percent, good |  |
| character_battle_condition_charted_terrain_mult | Charted Terrain Chance | character | multiplicative | percent, good |  |
| character_battle_condition_death_from_below_mult | Death from Below Chance | character | multiplicative | percent, good |  |
| character_battle_condition_dug_in_mult | Dug In Chance | character | multiplicative | percent, good |  |
| character_battle_condition_exhausted_mult | Exhausted Chance | character | multiplicative | percent, bad |  |
| character_battle_condition_good_visibility_mult | Good Visibility Chance | character | multiplicative | percent, good |  |
| character_battle_condition_guerilla_ambush_mult | Ambush Chance | character | multiplicative | percent, good |  |
| character_battle_condition_logistics_secured_mult | Logistics Secured Chance | character | multiplicative | percent, good |  |
| character_battle_condition_lost_mult | Lost Chance | character | multiplicative | percent, bad |  |
| character_battle_condition_mud_mult | Mud Chance | character | multiplicative | percent, bad |  |
| character_battle_condition_poor_visibility_mult | Poor Visibility Chance | character | multiplicative | percent, bad |  |
| character_battle_condition_ramming_maneuver_mult | Ramming Maneuver Chance | character | multiplicative | percent, neutral |  |
| character_battle_condition_rapid_advance_mult | Rapid Advance Chance | character | multiplicative | percent, good |  |
| character_battle_condition_rough_waters_mult | Rough Waters Chance | character | multiplicative | percent, neutral |  |
| character_battle_condition_strong_winds_mult | Strong Winds Chance | character | multiplicative | percent, neutral |  |
| character_battle_condition_surprise_maneuver_mult | Surprise Maneuver Chance | character | multiplicative | percent, good |  |
| character_blockade_mult | Admiral Blockade Strength | character | multiplicative | percent, good |  |
| character_command_limit_add | Command Limit | character | additive | good |  |
| character_command_limit_mult | Command Limit | character | multiplicative | percent, good |  |
| character_commander_loyalty_add | Commander Loyalty | character | additive | good |  |
| character_convoy_protection_mult | Admiral Merchant Marine Protection | character | multiplicative | percent, good |  |
| character_convoy_raiding_mult | Admiral Merchant Marine Raiding Efficiency | character | multiplicative | percent, good |  |
| character_coup_strength_add | Coup Strength | character | additive | neutral |  |
| character_coup_strength_mult | Coup Strength | character | multiplicative | percent, neutral |  |
| character_expedition_events_explorer_mult | Expedition Opportunity | character | multiplicative | percent, good |  |
| character_health_add | Character Health | character | additive | percent, good |  |
| character_interception_add | Admiral Interception Chance | character | additive | good |  |
| character_loyalty_add | Loyalty | character | additive | good |  |
| character_loyalty_mult | Loyalty | character | multiplicative | percent, good |  |
| character_max_offensive_battles_add | Max Offensive Battles | character | additive | good |  |
| character_naval_mission_area_add | Naval Mission Area Size | character | additive | good |  |
| character_piracy_goods_capacity_mult | Pirating Capacity | character | multiplicative | percent, good |  |
| character_popularity_add | Popularity | character | additive | good |  |
| character_prominence_add | Prominence | character | additive | neutral |  |
| character_raid_supply_add | Admiral Raid Supply Chance | character | additive | good |  |
| country_academics_pol_str_mult | Political Strength of Academics | country | multiplicative | percent, neutral |  |
| country_academics_voting_power_add | Political Strength from the Votes of Academics | country | additive | neutral | Object-based Enables elections |
| country_acceptance_homeland_add | Acceptance from Homeland | country | additive | good |  |
| country_acceptance_no_shared_heritage_trait_add | Acceptance from no shared Heritage Traits | country | additive | good |  |
| country_acceptance_no_shared_language_trait_add | Acceptance from no shared Language Traits | country | additive | good |  |
| country_acceptance_no_shared_religious_trait_add | Acceptance from no shared Religious Traits | country | additive | good |  |
| country_acceptance_no_shared_tradition_trait_add | Acceptance from no shared Tradition Traits | country | additive | good |  |
| country_acceptance_not_homeland_add | Acceptance from not Homeland | country | additive | good |  |
| country_acceptance_primary_culture_add | Acceptance from Primary Culture | country | additive | good |  |
| country_acceptance_shared_heritage_trait_add | Acceptance from Heritage Trait | country | additive | good |  |
| country_acceptance_shared_heritage_trait_group_add | Acceptance from Heritage Trait Group | country | additive | good |  |
| country_acceptance_shared_language_trait_add | Acceptance from Language Trait | country | additive | good |  |
| country_acceptance_shared_language_trait_group_add | Acceptance from Language Trait Group | country | additive | good |  |
| country_acceptance_shared_religious_trait_add | Acceptance from Religious Traits | country | additive | good |  |
| country_acceptance_shared_religious_trait_group_add | Acceptance from Religious Trait Groups | country | additive | good |  |
| country_acceptance_shared_tradition_trait_add | Acceptance from Tradition Trait | country | additive | good |  |
| country_acceptance_state_religion_add | Acceptance from State Religion | country | additive | good |  |
| country_admiral_rank_impact_mult | Admiral Rank Impact | country | multiplicative | percent, good |  |
| country_agitator_slots_add | Potential Agitators | country | additive | good |  |
| country_ahead_of_time_research_penalty_mult | Ahead of Time Penalty | country | multiplicative | percent, bad |  |
| country_all_buildings_protected_bool | Disallow Downsizing All Buildings | country | boolean | bad |  |
| country_allow_assimilation_cultural_erasure_bool | Allows Assimilation for the Cultural Erasure Status | country | boolean | neutral |  |
| country_allow_assimilation_full_acceptance_bool | Allows Assimilation for the Full Acceptance Status | country | boolean | neutral |  |
| country_allow_assimilation_open_prejudice_bool | Allows Assimilation for the Open Prejudice Status | country | boolean | neutral |  |
| country_allow_assimilation_second_rate_citizen_bool | Allows Assimilation for the Second-class Citizen Status | country | boolean | neutral |  |
| country_allow_assimilation_violent_hostility_bool | Allows Assimilation for the Violent Hostility Status | country | boolean | neutral |  |
| country_allow_conversion_cultural_erasure_bool | Allows Conversion for the Cultural Erasure Status | country | boolean | neutral |  |
| country_allow_conversion_full_acceptance_bool | Allows Conversion for the Full Acceptance Status | country | boolean | neutral |  |
| country_allow_conversion_open_prejudice_bool | Allows Conversion for the Open Prejudice Status | country | boolean | neutral |  |
| country_allow_conversion_second_rate_citizen_bool | Allows Conversion for the Second-class Citizen Status | country | boolean | neutral |  |
| country_allow_conversion_violent_hostility_bool | Allows Conversion for the Violent Hostility Status | country | boolean | neutral |  |
| country_allow_enacting_decrees_in_subject_bool | Allow enacting Decrees on Subject States | country | boolean | good |  |
| country_allow_multiple_alliances_bool | Allow Multiple Alliances | country | boolean | good |  |
| country_allow_voting_cultural_erasure_bool | Gives Voting Rights to the Cultural Erasure Status | country | boolean | neutral |  |
| country_allow_voting_full_acceptance_bool | Gives Voting Rights to the Full Acceptance Status | country | boolean | neutral |  |
| country_allow_voting_open_prejudice_bool | Gives Voting Rights to the Open Prejudice Status | country | boolean | neutral |  |
| country_allow_voting_second_rate_citizen_bool | Gives Voting Rights to the Second-class Citizen Status | country | boolean | neutral |  |
| country_allow_voting_violent_hostility_bool | Gives Voting Rights to the Violent Hostility Status | country | boolean | neutral |  |
| country_amenability_add | Country Amenability | country | additive | good |  |
| country_aristocrats_pol_str_mult | Political Strength of Aristocrats | country | multiplicative | percent, neutral |  |
| country_aristocrats_voting_power_add | Political Strength from the Votes of Aristocrats | country | additive | neutral | Object-based Enables elections |
| country_assimilation_cultural_erasure_mult | Assimilation for the Cultural Erasure Status | country | multiplicative | percent, neutral |  |
| country_assimilation_delta_threshold_add | Cultural Assimilation Threshold | country | additive | good |  |
| country_assimilation_full_acceptance_mult | Assimilation for the Full Acceptance Status | country | multiplicative | percent, neutral |  |
| country_assimilation_open_prejudice_mult | Assimilation for the Open Prejudice Status | country | multiplicative | percent, neutral |  |
| country_assimilation_second_rate_citizen_mult | Assimilation for the Second-class Citizen Status | country | multiplicative | percent, neutral |  |
| country_assimilation_violent_hostility_mult | Assimilation for the Violent Hostility Status | country | multiplicative | percent, neutral |  |
| country_authority_add | Authority | country | additive | good |  |
| country_authority_cost_add | Authority Cost | country | additive | bad |  |
| country_authority_mult | Authority | country | multiplicative | percent, good |  |
| country_authority_per_subject_add | Authority per Subject | country | additive | good |  |
| country_bg_manufacturing_require_subsidies_bool | Forced Subsidies for Manufacturing | country | boolean | bad |  |
| country_block_government_reform_bool | Blocks Government Reform | country | boolean | neutral |  |
| country_bolster_attraction_factor | Bolstered impact on Political Movement attraction | country | multiplicative | percent, neutral |  |
| country_bolster_cost_mult | Bolstering cost | country | multiplicative | percent, bad |  |
| country_brahmins_acceptance_min_add | Minimum Acceptance for the Brahmins Social Class | country | additive | good |  |
| country_brahmins_qualification_growth_other_class_mult | Qualification Growth outside the Brahmins Social Class for Brahmins | country | multiplicative | percent, good |  |
| country_brahmins_qualification_growth_same_class_mult | Qualification Growth within Brahmins Social Class | country | multiplicative | percent, good |  |
| country_bureaucracy_add | Bureaucracy | country | additive | good |  |
| country_bureaucracy_cost_add | Bureaucracy Cost | country | additive | bad |  |
| country_bureaucracy_investment_cost_factor_mult | Bureaucracy Institution Cost Multiplier | country | multiplicative | percent, bad |  |
| country_bureaucracy_mult | Bureaucracy | country | multiplicative | percent, good |  |
| country_bureaucrats_pol_str_mult | Political Strength of Bureaucrats | country | multiplicative | percent, neutral |  |
| country_bureaucrats_voting_power_add | Political Strength from the Votes of Bureaucrats | country | additive | neutral | Object-based Enables elections |
| country_can_form_construction_company_bool | Can form Construction type Companies | country | boolean | neutral |  |
| country_can_impose_same_lawgroup_army_model_in_power_bloc_bool | **Impose** same Army Model Law on Bloc Members | country | boolean | good |  |
| country_can_impose_same_lawgroup_church_and_state_in_power_bloc_bool | **Impose** same Church and State Law on Bloc Members | country | boolean | good |  |
| country_can_impose_same_lawgroup_citizenship_in_power_bloc_bool | **Impose** same Citizenship Law on Bloc Members | country | boolean | good |  |
| country_can_impose_same_lawgroup_colonization_in_power_bloc_bool | **Impose** same Colonization Law on Bloc Members | country | boolean | good |  |
| country_can_impose_same_lawgroup_distribution_of_power_in_power_bloc_bool | **Impose** same Distribution of Power Law on Bloc Members | country | boolean | good |  |
| country_can_impose_same_lawgroup_education_system_in_power_bloc_bool | **Impose** same Education System Law on Bloc Members | country | boolean | good |  |
| country_can_impose_same_lawgroup_governance_principles_in_power_bloc_bool | **Impose** same Governance Principles Law on Bloc Members | country | boolean | good |  |
| country_can_impose_same_lawgroup_policing_in_power_bloc_bool | **Impose** same Policing Law on Bloc Members | country | boolean | good |  |
| country_can_only_conscript_peasants_bool | Allows only Infantry Conscript Battalions | country | boolean | good |  |
| country_cannot_be_subjugated_bool | Cannot be Subjugated | country | boolean | neutral |  |
| country_cannot_be_target_for_law_imposition_bool | Cannot be targeted for Law Imposition | country | boolean | good |  |
| country_cannot_cancel_law_enactment_bool | Disallow}} Cancel Law Enactment | country | boolean | bad |  |
| country_cannot_enact_laws_bool | Disallow}} Enacting Laws | country | boolean | bad |  |
| country_cannot_join_power_bloc_bool | Cannot join Power Blocks | country | boolean | neutral |  |
| country_cannot_start_law_enactment_bool | Disallow}} Start Law Enactment | country | boolean | bad |  |
| country_capitalists_pol_str_mult | Political Strength of Capitalists | country | multiplicative | percent, neutral |  |
| country_capitalists_voting_power_add | Political Strength from the Votes of Capitalists | country | additive | neutral | Object-based Enables elections |
| country_clergymen_pol_str_mult | Political Strength of Clergymen | country | multiplicative | percent, neutral |  |
| country_clergymen_voting_power_add | Political Strength from the Votes of Clergymen | country | additive | neutral | Object-based Enables elections |
| country_clerks_pol_str_mult | Political Strength of Clerks | country | multiplicative | percent, neutral |  |
| country_clerks_voting_power_add | Political Strength from the Votes of Clerks | country | additive | neutral | Object-based Enables elections |
| country_company_construction_efficiency_bonus_add | Company Construction Bonus | country | additive | percent, good |  |
| country_company_throughput_bonus_add | Company Throughput Bonus | country | additive | percent, good |  |
| country_construction_add | Construction | country | additive | good |  |
| country_construction_goods_cost_mult | Construction Goods Cost | country | multiplicative | percent, bad |  |
| country_consumption_tax_cost_mult | Consumption Tax Cost | country | multiplicative | percent, bad |  |
| country_conversion_delta_threshold_add | Religious Conversion Threshold | country | additive | good |  |
| country_coup_resistance_add | Coup Resistance | country | additive | neutral |  |
| country_coup_resistance_mult | Coup Resistance | country | multiplicative | percent, neutral |  |
| country_dalit_acceptance_max_add | Maximum Acceptance for the Dalit Social Class | country | additive | bad |  |
| country_dalit_cultural_acceptance_mult | Cultural Acceptance for the Dalit Social Class | country | multiplicative | percent, good |  |
| country_dalit_education_access_add | Education Access for the Dalit Social Class | country | additive | good |  |
| country_dalit_education_access_mult | Education Access for the Dalit Social Class | country | multiplicative | percent, good |  |
| country_dalit_qualification_growth_add | Qualification Growth for the Dalit Social Class | country | additive | good |  |
| country_dalit_qualification_growth_mult | Qualification Growth for the Dalit Social Class | country | multiplicative | percent, good |  |
| country_dalit_qualification_growth_other_class_mult | Qualification Growth outside the Dalit Social Class for Dalit | country | multiplicative | percent, good |  |
| country_dalit_qualification_growth_same_class_mult | Qualification Growth within Dalit Social Class | country | multiplicative | percent, good |  |
| country_damage_relations_speed_mult | Damage Relations Speed | country | multiplicative | percent, good |  |
| country_diplomatic_play_maneuvers_add | Maneuvers per Diplomatic Play | country | additive | good |  |
| country_diplomatic_play_maneuvers_mult | Maneuvers per Diplomatic Play | country | multiplicative | percent, good |  |
| country_diplomatic_reputation_add | Diplomatic Reputation | country | additive | good |  |
| country_disable_investment_pool_bool | Disable Investment Pool (except for Companies) | country | boolean | bad |  |
| country_disable_nationalization_bool | Disable Nationalization | country | boolean | bad |  |
| country_disable_nationalization_without_compensation_bool | Disable Nationalization without compensation | country | boolean | bad |  |
| country_disable_non_company_privatization_bool | Disable Privatization (except for Companies) | country | boolean | bad |  |
| country_disallow_aggressive_plays_bool | Disallow Aggressive Diplomatic Plays | country | boolean | neutral |  |
| country_disallow_agitator_invites_bool | Disallowed from inviting Exiles | country | boolean | neutral |  |
| country_disallow_government_work_cultural_erasure_bool | Disallow Upper and Middle Strata work in Government Buildings for the Cultural Erasure Status | country | boolean | neutral |  |
| country_disallow_government_work_full_acceptance_bool | Disallow Upper and Middle Strata work in Government Buildings for the Full Acceptance Status | country | boolean | neutral |  |
| country_disallow_government_work_open_prejudice_bool | Disallow Upper and Middle Strata work in Government Buildings for the Open Prejudice Status | country | boolean | neutral |  |
| country_disallow_government_work_second_rate_citizen_bool | Disallow Upper and Middle Strata work in Government Buildings for the Second-class Citizen Status | country | boolean | neutral |  |
| country_disallow_government_work_violent_hostility_bool | Disallow Upper and Middle Strata work in Government Buildings for the Violent Hostility Status | country | boolean | neutral |  |
| country_disallow_law_no_colonial_affairs_bool | Disallow No Colonial Affairs | country | boolean | bad |  |
| country_disallow_law_no_police_bool | Disallow No Police | country | boolean | bad |  |
| country_disallow_law_no_schools_bool | Disallow No Schools | country | boolean | bad |  |
| country_disallow_military_work_cultural_erasure_bool | Disallow work in Military Buildings for the Cultural Erasure Status | country | boolean | neutral |  |
| country_disallow_military_work_full_acceptance_bool | Disallow work in Military Buildings for the Full Acceptance Status | country | boolean | neutral |  |
| country_disallow_military_work_open_prejudice_bool | Disallow work in Military Buildings for the Open Prejudice Status | country | boolean | neutral |  |
| country_disallow_military_work_second_rate_citizen_bool | Disallow work in Military Buildings for the Second-class Citizen Status | country | boolean | neutral |  |
| country_disallow_military_work_violent_hostility_bool | Disallow work in Military Buildings for the Violent Hostility Status | country | boolean | neutral |  |
| country_disallow_trade_bool | Disable Trade Centers | country | boolean | bad |  |
| country_disallow_trade_outside_canton_bool | Disable Trade Centers outside Western Guangdong | country | boolean | bad | Script-only |
| country_disallow_trade_outside_kyushu_bool | Disable Trade Centers outside Kyushu | country | boolean | bad |  |
| country_economic_dependence_on_overlord_add | Economic Dependence on Overlord | country | additive | bad |  |
| country_education_fervor_add | Education Institution Fervor | country | additive | neutral |  |
| country_electoral_confidence_impact_mult | Electoral Confidence Impact | country | multiplicative | percent, neutral |  |
| country_electoral_confidence_over_time | Monthly Electoral Confidence Change | country |  | percent, good |  |
| country_enactment_speed_law_anarchy_mult | country_enactment_speed_law_anarchy_mult | country | multiplicative | percent, good |  |
| country_enactment_speed_law_autocracy_mult | country_enactment_speed_law_autocracy_mult | country | multiplicative | percent, good |  |
| country_enactment_speed_law_oligarchy_mult | country_enactment_speed_law_oligarchy_mult | country | multiplicative | percent, good |  |
| country_enactment_speed_law_public_schools_mult | Enactment Speed for Public Schools | country | multiplicative | percent, good |  |
| country_enactment_speed_law_single_party_state_mult | country_enactment_speed_law_single_party_state_mult | country | multiplicative | percent, good |  |
| country_enactment_speed_law_technocracy_mult | Enactment Speed for Technocracy | country | multiplicative | percent, good |  |
| country_enactment_success_chance_law_anarchy_add | Enactment Success chance for Anarchy | country | additive | percent, good |  |
| country_enactment_success_chance_law_autocracy_add | Enactment Success chance for Autocracy | country | additive | percent, good |  |
| country_enactment_success_chance_law_oligarchy_add | Enactment Success chance for Oligarchy | country | additive | percent, good |  |
| country_enactment_success_chance_law_public_schools_add | Enactment Success chance for Public Schools | country | additive | percent, good |  |
| country_enactment_success_chance_law_single_party_state_add | Enactment Success chance for Single-Party State | country | additive | percent, good |  |
| country_enactment_success_chance_law_technocracy_add | Enactment Success chance for Technocracy | country | additive | percent, good |  |
| country_engineers_pol_str_mult | Political Strength of Engineers | country | multiplicative | percent, neutral |  |
| country_engineers_voting_power_add | Political Strength from the Votes of Engineers | country | additive | neutral | Object-based Enables elections |
| country_expedition_events_explorer_mult | Expedition Opportunity | country | multiplicative | percent, good |  |
| country_expenses_add | Government Expenses | country | additive | bad |  |
| country_farmers_pol_str_mult | Political Strength of Farmers | country | multiplicative | percent, neutral |  |
| country_farmers_voting_power_add | Political Strength from the Votes of Farmers | country | additive | neutral | Object-based Enables elections |
| country_financial_districts_buy_farms_likelihood | Financial Districts investment into Plantations, Ranches, and Agriculture | country |  | percent, good |  |
| country_flagship_interest_gain_mult | Flagship Involvement Gain | country | multiplicative | percent, good |  |
| country_forbid_electoral_fraud_bool | Forbid Electoral Manipulation | country | boolean | neutral |  |
| country_forbid_monopoly_bool | Forbid Monopolies | country | boolean | bad |  |
| country_force_privatization_bool | Force Privatization | country | boolean | neutral |  |
| country_foreign_collectivization_bool | Foreign Collectivization | country | boolean | neutral |  |
| country_frankenstein_company_bool | Experimental Modules Operational | country | boolean | neutral |  |
| country_free_charters_add | Free Company Charters | country | additive | good |  |
| country_general_rank_impact_mult | General Rank Impact | country | multiplicative | percent, good |  |
| country_gold_reserve_limit_mult | Gold reserve limit | country | multiplicative | percent, good |  |
| country_government_buildings_protected_bool | Disallow Downsizing Government Buildings | country | boolean | bad |  |
| country_government_dividends_efficiency_add | Government Dividends Efficiency | country | additive | percent, good |  |
| country_government_dividends_reinvestment_add | Government Dividends Reinvestment | country | additive | percent, neutral |  |
| country_government_dividends_waste_add | Government Dividends Waste | country | additive | percent, bad |  |
| country_government_wages_mult | Government Wages | country | multiplicative | percent, neutral |  |
| country_higher_diplomatic_acceptance_same_religion_bool | Higher Diplomatic Proposal Acceptance for Countries with same Religion | country | boolean | good |  |
| country_higher_leverage_from_economic_dependence_bool | Increased Leverage from Economic Dependence | country | boolean | good |  |
| country_improve_relations_speed_mult | Improve Relations Speed | country | multiplicative | percent, good |  |
| country_infamy_decay_mult | Infamy Decay | country | multiplicative | percent, good |  |
| country_infamy_generation_against_unrecognized_mult | Infamy Generation against Unrecognized Powers | country | multiplicative | percent, bad |  |
| country_infamy_generation_mult | Infamy Generation | country | multiplicative | percent, bad |  |
| country_influence_add | Influence | country | additive | good |  |
| country_influence_cost_add | Influence Cost | country | additive | bad |  |
| country_influence_mult | Influence | country | multiplicative | percent, good |  |
| country_initiator_war_goal_maneuver_cost_mult | War Goal Maneuver cost for the Diplomatic Play Initiator | country | multiplicative | percent, bad |  |
| country_institution_colonial_affairs_max_investment_add | Max Colonial Affairs Institution Investment | country | additive | good |  |
| country_institution_cost_institution_colonial_affairs_mult | Bureaucracy Cost of Colonial Affairs | country | multiplicative | percent, bad |  |
| country_institution_cost_institution_health_system_mult | Bureaucracy Cost of Health System | country | multiplicative | percent, bad |  |
| country_institution_cost_institution_home_affairs_mult | Bureaucracy Cost of Home Affairs | country | multiplicative | percent, bad |  |
| country_institution_cost_institution_police_mult | Bureaucracy Cost of Law Enforcement | country | multiplicative | percent, bad |  |
| country_institution_cost_institution_schools_mult | Bureaucracy Cost of Education | country | multiplicative | percent, bad |  |
| country_institution_cost_institution_social_security_mult | Bureaucracy Cost of Social Security | country | multiplicative | percent, bad |  |
| country_institution_health_system_max_investment_add | Max Health System Institution Investment | country | additive | good |  |
| country_institution_home_affairs_max_investment_add | Max Home Affairs Institution Investment | country | additive | good |  |
| country_institution_impact_institution_health_system_mult | Impact of Health System | country | multiplicative | percent, good |  |
| country_institution_police_max_investment_add | Max Law Enforcement Institution Investment | country | additive | good |  |
| country_institution_schools_max_investment_add | Max Education Institution Investment | country | additive | good |  |
| country_institution_size_change_speed_institution_colonial_affairs_mult | Institution Size Change Speed for Colonial Affairs | country | multiplicative | percent, good |  |
| country_institution_size_change_speed_institution_police_mult | Institution Size Change Speed for Law Enforcement | country | multiplicative | percent, good |  |
| country_institution_size_change_speed_institution_schools_mult | Institution Size Change Speed for Education | country | multiplicative | percent, good |  |
| country_institution_size_change_speed_mult | Institution Size Change Speed | country | multiplicative | percent, good |  |
| country_institution_social_security_max_investment_add | Max Social Security Institution Investment | country | additive | good |  |
| country_institution_workplace_safety_max_investment_add | Max Workplace Safety Office Institution Investment | country | additive | good |  |
| country_je_korea_action_cost | country_je_korea_action_cost | country |  | percent, bad |  |
| country_join_power_bloc_member_in_defensive_plays_bool | Can call Power Bloc members with the Call Ally Sway in **defensive** Diplomatic Plays | country | boolean | neutral |  |
| country_join_power_bloc_member_in_plays_bool | Can call Power Bloc members with the Call Ally Sway in **all** Diplomatic Plays | country | boolean | neutral |  |
| country_kshatriyas_acceptance_max_add | Maximum Acceptance for the Kshatriyas Social Class | country | additive | bad |  |
| country_kshatriyas_acceptance_min_add | Minimum Acceptance for the Kshatriyas Social Class | country | additive | good |  |
| country_kshatriyas_cultural_acceptance_mult | Cultural Acceptance for the Kshatriyas Social Class | country | multiplicative | percent, good |  |
| country_kshatriyas_education_access_add | Education Access for the Kshatriyas Social Class | country | additive | good |  |
| country_kshatriyas_education_access_mult | Education Access for the Kshatriyas Social Class | country | multiplicative | percent, good |  |
| country_kshatriyas_qualification_growth_add | Qualification Growth for the Kshatriyas Social Class | country | additive | good |  |
| country_kshatriyas_qualification_growth_mult | Qualification Growth for the Kshatriyas Social Class | country | multiplicative | percent, good |  |
| country_kshatriyas_qualification_growth_other_class_mult | Qualification Growth outside the Kshatriyas Social Class for Kshatriyas | country | multiplicative | percent, good |  |
| country_kshatriyas_qualification_growth_same_class_mult | Qualification Growth within Kshatriyas Social Class | country | multiplicative | percent, good |  |
| country_laborers_pol_str_mult | Political Strength of Laborers | country | multiplicative | percent, neutral |  |
| country_laborers_voting_power_add | Political Strength from the Votes of Laborers | country | additive | neutral | Object-based Enables elections |
| country_law_enactment_imposition_success_add | Imposed Enactment Success Chance | country | additive | percent, good |  |
| country_law_enactment_max_setbacks_add | Maximum Law Enactment Setbacks | country | additive | good |  |
| country_law_enactment_speed_mult | Enactment Speed | country | multiplicative | percent, good |  |
| country_law_enactment_stall_add | Enactment Stall Chance | country | additive | percent, bad |  |
| country_law_enactment_stall_mult | Enactment Stall Chance | country | multiplicative | percent, bad |  |
| country_law_enactment_success_add | Enactment Success Chance | country | additive | percent, good |  |
| country_leader_has_law_enactment_success_mult | Power Bloc Legal Synergy | country | multiplicative | percent, good |  |
| country_legitimacy_base_add | Legitimacy | country | additive | good |  |
| country_legitimacy_govt_leader_clout_add | Legitimacy based on Government Leader Clout | country | additive | good |  |
| country_legitimacy_govt_size_add | Government size allowance | country | additive | good |  |
| country_legitimacy_govt_total_clout_add | Legitimacy based on Government Clout | country | additive | good |  |
| country_legitimacy_govt_total_votes_add | Legitimacy based on Votes | country | additive | good |  |
| country_legitimacy_headofstate_add | Legitimacy from including the Head of State In Government | country | additive | good |  |
| country_legitimacy_ideological_incoherence_mult | Legitimacy penalty from Ideological Incompatibility | country | multiplicative | percent, bad |  |
| country_legitimacy_min_add | Minimum Legitimacy | country | additive | neutral |  |
| country_leverage_generation_add | Leverage Generation | country | additive | good |  |
| country_leverage_generation_mult | Leverage Generation | country | multiplicative | percent, good |  |
| country_leverage_resistance_add | Leverage Resistance | country | additive | neutral |  |
| country_leverage_resistance_mult | Leverage Resistance | country | multiplicative | percent, neutral |  |
| country_liberty_desire_add | Weekly Liberty Desire | country | additive | neutral |  |
| country_liberty_desire_decrease_mult | Weekly Liberty Desire Decrease | country | multiplicative | percent, neutral |  |
| country_liberty_desire_increase_mult | Weekly Liberty Desire Increase | country | multiplicative | percent, neutral |  |
| country_liberty_desire_of_subjects_add | Weekly Liberty Desire for all Subjects | country | additive | neutral |  |
| country_limit_officers_qualifications_to_upper_strata | Officers qualifications limited to Upper Strata | country | boolean | neutral |  |
| country_loan_interest_rate_add | Loan interest rate | country | additive | percent, bad |  |
| country_loan_interest_rate_mult | Loan interest rate | country | multiplicative | percent, bad |  |
| country_lobby_leverage_generation_mult | Leverage Generation from Political Lobbies | country | multiplicative | percent, good |  |
| country_lobby_support | Lobby Support | country |  | good |  |
| country_loyalism_increases_cultural_erasure_mult | Loyalism increases for the Cultural Erasure Status | country | multiplicative | percent, good |  |
| country_loyalism_increases_full_acceptance_mult | Loyalism increases for the Full Acceptance Status | country | multiplicative | percent, good |  |
| country_loyalism_increases_open_prejudice_mult | Loyalism increases for the Open Prejudice Status | country | multiplicative | percent, good |  |
| country_loyalism_increases_second_rate_citizen_mult | Loyalism increases for the Second-class Citizen Status | country | multiplicative | percent, good |  |
| country_loyalism_increases_violent_hostility_mult | Loyalism increases for the Violent Hostility Status | country | multiplicative | percent, good |  |
| country_loyalists_from_legitimacy_mult | Loyalists from high Legitimacy | country | multiplicative | percent, good |  |
| country_machinists_pol_str_mult | Political Strength of Machinists | country | multiplicative | percent, neutral |  |
| country_machinists_voting_power_add | Political Strength from the Votes of Machinists | country | additive | neutral | Object-based Enables elections |
| country_mass_migration_attraction_mult | Mass Migration Attraction | country | multiplicative | percent, good |  |
| country_max_companies_add | Max Number of Companies | country | additive | good |  |
| country_max_unassigned_admirals_add | Maximum Idle Admirals | country | additive | good |  |
| country_max_unassigned_generals_add | Maximum Idle Generals | country | additive | good |  |
| country_max_weekly_construction_progress_add | Max Weekly Construction Progress | country | additive | good |  |
| country_migration_restrictiveness_add | Migration Restrictiveness | country | additive | neutral |  |
| country_military_goods_cost_mult | Military Goods Cost | country | multiplicative | percent, bad |  |
| country_military_tech_research_speed_mult | Military Research Speed | country | multiplicative | percent, good |  |
| country_military_tech_spread_mult | Technology Spread for Military | country | multiplicative | percent, good |  |
| country_military_wages_mult | Military Wages | country | multiplicative | percent, neutral |  |
| country_minting_add | Minting | country | additive | good |  |
| country_minting_mult | Minting | country | multiplicative | percent, good |  |
| country_must_have_movement_to_enact_laws_bool | Must have Political Movement to Enact Laws | country | boolean | bad |  |
| country_nationalization_cost_non_members_mult | Cost for Nationalization | country | multiplicative | percent, bad |  |
| country_navy_goods_cost_mult | Navy Goods Cost | country | multiplicative | percent, bad |  |
| country_no_advantage_loss_from_lack_of_interest_bool | Ignores Trade Advantage penalty from Interests | country | boolean | good |  |
| country_non_state_religion_wages_mult | Wages for Non-State Religion Pops | country | multiplicative | percent, neutral |  |
| country_officers_pol_str_mult | Political Strength of Officers | country | multiplicative | percent, neutral |  |
| country_officers_voting_power_add | Political Strength from the Votes of Officers | country | additive | neutral | Object-based Enables elections |
| country_opposition_ig_approval_add | Opposition Interest Group Approval | country | additive | good |  |
| country_overlord_income_transfer_mult | Overlord Income Transfer | country | multiplicative | percent, bad |  |
| country_pact_leverage_generation_add | Leverage Generation from Diplomatic Pact | country | additive | good |  |
| country_pact_leverage_generation_mult | Leverage Generation from Diplomatic Pact | country | multiplicative | percent, good |  |
| country_party_whip_impact_add | Party Whip Impact on Ideological Incoherence | country | additive | percent, good |  |
| country_peasants_pol_str_mult | Political Strength of Peasants | country | multiplicative | percent, neutral |  |
| country_peasants_voting_power_add | Political Strength from the Votes of Peasants | country | additive | neutral | Object-based Enables elections |
| country_piracy_income_add | Piracy Income | country | additive | percent, good |  |
| country_political_strength_cultural_erasure_mult | Political Strength for the Cultural Erasure Status | country | multiplicative | percent, good |  |
| country_political_strength_full_acceptance_mult | Political Strength for the Full Acceptance Status | country | multiplicative | percent, good |  |
| country_political_strength_open_prejudice_mult | Political Strength for the Open Prejudice Status | country | multiplicative | percent, good |  |
| country_political_strength_second_rate_citizen_mult | Political Strength for the Second-class Citizen Status | country | multiplicative | percent, good |  |
| country_political_strength_violent_hostility_mult | Political Strength for the Violent Hostility Status | country | multiplicative | percent, good |  |
| country_port_connection_cost_mult | Merchant Marine Cost of Port Connections | country | multiplicative | percent, bad |  |
| country_prestige_add | Prestige | country | additive | good |  |
| country_prestige_from_army_power_projection_mult | Prestige from Army Power Projection | country | multiplicative | percent, good |  |
| country_prestige_from_navy_power_projection_mult | Prestige from Navy Power Projection | country | multiplicative | percent, good |  |
| country_prestige_mult | Prestige | country | multiplicative | percent, good |  |
| country_primary_culture_fervor_from_laws_add | Primary Culture Fervor from Laws | country | additive | neutral |  |
| country_private_construction_allocation_mult | Private Construction Allocation | country | multiplicative | percent, neutral |  |
| country_production_tech_research_speed_mult | Production Research Speed | country | multiplicative | percent, good |  |
| country_production_tech_spread_mult | Technology Spread for Production | country | multiplicative | percent, good |  |
| country_qualification_growth_cultural_erasure_mult | Qualifications advancement for the Cultural Erasure Status | country | multiplicative | percent, good |  |
| country_qualification_growth_full_acceptance_mult | Qualifications advancement for the Full Acceptance Status | country | multiplicative | percent, good |  |
| country_qualification_growth_open_prejudice_mult | Qualifications advancement for the Open Prejudice Status | country | multiplicative | percent, good |  |
| country_qualification_growth_second_rate_citizen_mult | Qualifications advancement for the Second-class Citizen Status | country | multiplicative | percent, good |  |
| country_qualification_growth_violent_hostility_mult | Qualifications advancement for the Violent Hostility Status | country | multiplicative | percent, good |  |
| country_radicalism_increases_cultural_erasure_mult | Radicalism increases for the Cultural Erasure Status | country | multiplicative | percent, bad |  |
| country_radicalism_increases_full_acceptance_mult | Radicalism increases for the Full Acceptance Status | country | multiplicative | percent, bad |  |
| country_radicalism_increases_open_prejudice_mult | Radicalism increases for the Open Prejudice Status | country | multiplicative | percent, bad |  |
| country_radicalism_increases_second_rate_citizen_mult | Radicalism increases for the Second-class Citizen Status | country | multiplicative | percent, bad |  |
| country_radicalism_increases_violent_hostility_mult | Radicalism increases for the Violent Hostility Status | country | multiplicative | percent, bad |  |
| country_radicals_from_conquest_mult | Radicals from Conquest | country | multiplicative | percent, bad |  |
| country_radicals_from_legitimacy_mult | Radicals from low Legitimacy | country | multiplicative | percent, bad |  |
| country_reduced_liberty_desire_same_religion_bool | Reduced Liberty Desire for Same Religion | country | boolean | good |  |
| country_resource_depletion_chance_mult | Resource Depletion Chance | country | multiplicative | percent, bad |  |
| country_resource_discovery_chance_mult | Resource Discovery Chance | country | multiplicative | percent, good |  |
| country_revolution_clock_time_add | Revolution Clock Time | country | additive | neutral |  |
| country_revolution_progress_add | Revolution Progression Speed | country | additive | percent, bad |  |
| country_revolution_progress_mult | Revolution Progression Speed | country | multiplicative | percent, bad |  |
| country_sailors_max_add | Max Sailors | country | additive | good |  |
| country_secession_clock_time_add | Secession Clock Time | country | additive | neutral |  |
| country_secession_progress_add | Secession Progression Speed | country | additive | percent, bad |  |
| country_secession_progress_mult | Secession Progression Speed | country | multiplicative | percent, bad |  |
| country_ship_construction_add | Ship Construction | country | additive | good |  |
| country_ship_construction_efficiency_add | Ship Construction Efficiency | country | additive | percent, good |  |
| country_ship_construction_goods_cost_mult | Ship Construction Goods Cost | country | multiplicative | percent, bad |  |
| country_ship_construction_progress_max_add | Max Ship Construction Progress | country | additive | good |  |
| country_ship_crew_starting_veterancy_experience_add | Starting Ship Crew Experience | country | additive | good |  |
| country_ship_crew_starting_veterancy_experience_mult | Starting Ship Crew Experience | country | multiplicative | percent, good |  |
| country_ship_group_capital_ships_construction_efficiency_add | Capital Ships Construction Efficiency | country | additive | percent, good |  |
| country_ship_group_capital_ships_construction_progress_max_add | Capital Ships Max Construction Progress | country | additive | good |  |
| country_ship_group_capital_ships_construction_progress_max_mult | Capital Ships Max Construction Progress | country | multiplicative | percent, good |  |
| country_ship_group_cruisers_construction_efficiency_add | Cruisers Construction Efficiency | country | additive | percent, good |  |
| country_ship_group_cruisers_construction_progress_max_add | Cruisers Max Construction Progress | country | additive | good |  |
| country_ship_group_cruisers_construction_progress_max_mult | Cruisers Max Construction Progress | country | multiplicative | percent, good |  |
| country_ship_group_supply_ships_construction_efficiency_add | Supply Ships Construction Efficiency | country | additive | percent, good |  |
| country_ship_group_torpedo_craft_construction_efficiency_add | Torpedo Craft Construction Efficiency | country | additive | percent, good |  |
| country_ship_group_torpedo_craft_construction_progress_max_add | Torpedo Craft Max Construction Progress | country | additive | good |  |
| country_ship_group_torpedo_craft_construction_progress_max_mult | Torpedo Craft Max Construction Progress | country | multiplicative | percent, good |  |
| country_ship_type_armored_cruiser_construction_efficiency_add | Armored Cruiser Construction Efficiency | country | additive | percent, good |  |
| country_ship_type_light_cruiser_construction_efficiency_add | Light Cruiser Construction Efficiency | country | additive | percent, good |  |
| country_ship_type_protected_cruiser_construction_efficiency_add | Protected Cruiser Construction Efficiency | country | additive | percent, good |  |
| country_ship_type_troop_ship_construction_efficiency_add | Troopship Construction Efficiency | country | additive | percent, good |  |
| country_shopkeepers_pol_str_mult | Political Strength of Shopkeepers | country | multiplicative | percent, neutral |  |
| country_shopkeepers_voting_power_add | Political Strength from the Votes of Shopkeepers | country | additive | neutral | Object-based Enables elections |
| country_shudras_acceptance_max_add | Maximum Acceptance for the Shudras Social Class | country | additive | bad |  |
| country_shudras_cultural_acceptance_mult | Cultural Acceptance for the Shudras Social Class | country | multiplicative | percent, good |  |
| country_shudras_education_access_add | Education Access for the Shudras Social Class | country | additive | good |  |
| country_shudras_education_access_mult | Education Access for the Shudras Social Class | country | multiplicative | percent, good |  |
| country_shudras_qualification_growth_add | Qualification Growth for the Shudras Social Class | country | additive | good |  |
| country_shudras_qualification_growth_mult | Qualification Growth for the Shudras Social Class | country | multiplicative | percent, good |  |
| country_shudras_qualification_growth_other_class_mult | Qualification Growth outside the Shudras Social Class for Shudras | country | multiplicative | percent, good |  |
| country_shudras_qualification_growth_same_class_mult | Qualification Growth within Shudras Social Class | country | multiplicative | percent, good |  |
| country_slaves_voting_power_add | Political Strength from the Votes of Slaves | country | additive | neutral | Object-based Enables elections |
| country_society_tech_research_speed_mult | Society Research Speed | country | multiplicative | percent, good |  |
| country_society_tech_spread_mult | Technology Spread for Society | country | multiplicative | percent, good |  |
| country_soldiers_pol_str_mult | Political Strength of Servicemen | country | multiplicative | percent, neutral |  |
| country_soldiers_voting_power_add | Political Strength from the Votes of Servicemen | country | additive | neutral | Object-based Enables elections |
| country_standard_of_living_cultural_erasure_add | Standard of Living for the Cultural Erasure Status | country | additive | good |  |
| country_standard_of_living_full_acceptance_add | Standard of Living for the Full Acceptance Status | country | additive | good |  |
| country_standard_of_living_open_prejudice_add | Standard of Living for the Open Prejudice Status | country | additive | good |  |
| country_standard_of_living_second_rate_citizen_add | Standard of Living for the Second-class Citizen Status | country | additive | good |  |
| country_standard_of_living_violent_hostility_add | Standard of Living for the Violent Hostility Status | country | additive | good |  |
| country_state_religion_wages_mult | Wages for State Religion Pops | country | multiplicative | percent, neutral |  |
| country_strata_commoners_peasants_acceptance_max_add | Maximum Acceptance for the Hyakushō Social Class | country | additive | bad |  |
| country_strata_commoners_peasants_acceptance_min_add | Minimum Acceptance for the Hyakushō Social Class | country | additive | good |  |
| country_strata_commoners_peasants_cultural_acceptance_mult | Cultural Acceptance for the Hyakushō Social Class | country | multiplicative | percent, good |  |
| country_strata_commoners_peasants_education_access_add | Education Access for the Hyakushō Social Class | country | additive | good |  |
| country_strata_commoners_peasants_education_access_mult | Education Access for the Hyakushō Social Class | country | multiplicative | percent, good |  |
| country_strata_commoners_peasants_qualification_growth_add | Qualification Growth for the Hyakushō Social Class | country | additive | good |  |
| country_strata_commoners_peasants_qualification_growth_mult | Qualification Growth for the Hyakushō Social Class | country | multiplicative | percent, good |  |
| country_strata_commoners_peasants_qualification_growth_other_class_mult | Qualification Growth outside the Hyakushō Social Class for Hyakushō | country | multiplicative | percent, good |  |
| country_strata_commoners_peasants_qualification_growth_same_class_mult | Qualification Growth within Hyakushō Social Class | country | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_acceptance_max_add | Maximum Acceptance for the Chōnin Social Class | country | additive | bad |  |
| country_strata_commoners_townspeople_acceptance_min_add | Minimum Acceptance for the Chōnin Social Class | country | additive | good |  |
| country_strata_commoners_townspeople_cultural_acceptance_mult | Cultural Acceptance for the Chōnin Social Class | country | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_education_access_add | Education Access for the Chōnin Social Class | country | additive | good |  |
| country_strata_commoners_townspeople_education_access_mult | Education Access for the Chōnin Social Class | country | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_qualification_growth_add | Qualification Growth for the Chōnin Social Class | country | additive | good |  |
| country_strata_commoners_townspeople_qualification_growth_mult | Qualification Growth for the Chōnin Social Class | country | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_qualification_growth_other_class_mult | Qualification Growth outside the Chōnin Social Class for Chōnin | country | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_qualification_growth_same_class_mult | Qualification Growth within Chōnin Social Class | country | multiplicative | percent, good |  |
| country_strata_outcastes_acceptance_max_add | Maximum Acceptance for the Eta-Hinin Social Class | country | additive | bad |  |
| country_strata_outcastes_acceptance_min_add | Minimum Acceptance for the Eta-Hinin Social Class | country | additive | good |  |
| country_strata_outcastes_cultural_acceptance_mult | Cultural Acceptance for the Eta-Hinin Social Class | country | multiplicative | percent, good |  |
| country_strata_outcastes_education_access_add | Education Access for the Eta-Hinin Social Class | country | additive | good |  |
| country_strata_outcastes_education_access_mult | Education Access for the Eta-Hinin Social Class | country | multiplicative | percent, good |  |
| country_strata_outcastes_qualification_growth_add | Qualification Growth for the Eta-Hinin Social Class | country | additive | good |  |
| country_strata_outcastes_qualification_growth_mult | Qualification Growth for the Eta-Hinin Social Class | country | multiplicative | percent, good |  |
| country_strata_outcastes_qualification_growth_other_class_mult | Qualification Growth outside the Eta-Hinin Social Class for Eta-Hinin | country | multiplicative | percent, good |  |
| country_strata_outcastes_qualification_growth_same_class_mult | Qualification Growth within Eta-Hinin Social Class | country | multiplicative | percent, good |  |
| country_strata_religious_acceptance_max_add | Maximum Acceptance for the Jisha Social Class | country | additive | bad |  |
| country_strata_religious_acceptance_min_add | Minimum Acceptance for the Jisha Social Class | country | additive | good |  |
| country_strata_religious_cultural_acceptance_mult | Cultural Acceptance for the Jisha Social Class | country | multiplicative | percent, good |  |
| country_strata_religious_education_access_add | Education Access for the Jisha Social Class | country | additive | good |  |
| country_strata_religious_education_access_mult | Education Access for the Jisha Social Class | country | multiplicative | percent, good |  |
| country_strata_religious_qualification_growth_add | Qualification Growth for the Jisha Social Class | country | additive | good |  |
| country_strata_religious_qualification_growth_mult | Qualification Growth for the Jisha Social Class | country | multiplicative | percent, good |  |
| country_strata_religious_qualification_growth_other_class_mult | Qualification Growth outside the Jisha Social Class for Jisha | country | multiplicative | percent, good |  |
| country_strata_religious_qualification_growth_same_class_mult | Qualification Growth within Jisha Social Class | country | multiplicative | percent, good |  |
| country_strata_samurai_high_acceptance_max_add | Maximum Acceptance for the Upper Samurai Social Class | country | additive | bad |  |
| country_strata_samurai_high_acceptance_min_add | Minimum Acceptance for the Upper Samurai Social Class | country | additive | good |  |
| country_strata_samurai_high_cultural_acceptance_mult | Cultural Acceptance for the Upper Samurai Social Class | country | multiplicative | percent, good |  |
| country_strata_samurai_high_education_access_add | Education Access for the Upper Samurai Social Class | country | additive | good |  |
| country_strata_samurai_high_education_access_mult | Education Access for the Upper Samurai Social Class | country | multiplicative | percent, good |  |
| country_strata_samurai_high_qualification_growth_add | Qualification Growth for the Upper Samurai Social Class | country | additive | good |  |
| country_strata_samurai_high_qualification_growth_mult | Qualification Growth for the Upper Samurai Social Class | country | multiplicative | percent, good |  |
| country_strata_samurai_high_qualification_growth_other_class_mult | Qualification Growth outside the Upper Samurai Social Class for Upper Samurai | country | multiplicative | percent, good |  |
| country_strata_samurai_high_qualification_growth_same_class_mult | Qualification Growth within Upper Samurai Social Class | country | multiplicative | percent, good |  |
| country_strata_samurai_low_acceptance_max_add | Maximum Acceptance for the Lower Samurai Social Class | country | additive | bad |  |
| country_strata_samurai_low_acceptance_min_add | Minimum Acceptance for the Lower Samurai Social Class | country | additive | good |  |
| country_strata_samurai_low_cultural_acceptance_mult | Cultural Acceptance for the Lower Samurai Social Class | country | multiplicative | percent, good |  |
| country_strata_samurai_low_education_access_add | Education Access for the Lower Samurai Social Class | country | additive | good |  |
| country_strata_samurai_low_education_access_mult | Education Access for the Lower Samurai Social Class | country | multiplicative | percent, good |  |
| country_strata_samurai_low_qualification_growth_add | Qualification Growth for the Lower Samurai Social Class | country | additive | good |  |
| country_strata_samurai_low_qualification_growth_mult | Qualification Growth for the Lower Samurai Social Class | country | multiplicative | percent, good |  |
| country_strata_samurai_low_qualification_growth_other_class_mult | Qualification Growth outside the Lower Samurai Social Class for Lower Samurai | country | multiplicative | percent, good |  |
| country_strata_samurai_low_qualification_growth_same_class_mult | Qualification Growth within Lower Samurai Social Class | country | multiplicative | percent, good |  |
| country_subject_income_transfer_heathen_mult | Income transfer from Heathen Subjects | country | multiplicative | percent, good |  |
| country_subject_income_transfer_mult | Income transfer from Subjects | country | multiplicative | percent, good |  |
| country_supply_ship_construction_progress_max_add | Supply Ship Max Construction Progress | country | additive | good |  |
| country_supply_ship_construction_progress_max_mult | Supply Ship Max Construction Progress | country | multiplicative | percent, good |  |
| country_supply_ship_construction_ratio_add | Supply Ship Construction Ratio | country | additive | percent, good |  |
| country_support_independence_weekly_liberty_desire_add | Support Independence weekly Liberty Desire | country | additive | neutral |  |
| country_support_separatism_resistance_mult | Support Separatism Resistance | country | multiplicative | percent, good |  |
| country_support_separatism_strength_mult | Support Separatism Strength | country | multiplicative | percent, good |  |
| country_suppression_attraction_factor | Suppression impact on Political Movement attraction | country | multiplicative | percent, bad |  |
| country_suppression_cost_mult | Suppression cost | country | multiplicative | percent, bad |  |
| country_tax_income_add | Tax Income | country | additive | good |  |
| country_tech_group_research_speed_mult | Technology Research Speed as a group | country | multiplicative | percent, good |  |
| country_tech_research_speed_mult | Technology Research Speed | country | multiplicative | percent, good |  |
| country_tech_spread_add | Technology Spread | country | additive | good |  |
| country_tech_spread_mult | Technology Spread | country | multiplicative | percent, good |  |
| country_tension_decay_mult | Tension Decay | country | multiplicative | percent, good |  |
| country_treaty_leverage_generation_add | Leverage Generation from Treaty | country | additive | good |  |
| country_treaty_leverage_generation_mult | Leverage Generation from Treaty | country | multiplicative | percent, good |  |
| country_two_spains_conservative_drift_add | **The Two Spains** Conservative Progress | country | additive | good |  |
| country_two_spains_liberal_drift_add | **The Two Spains** Liberal Progress | country | additive | good |  |
| country_vaishyas_acceptance_max_add | Maximum Acceptance for the Vaishyas Social Class | country | additive | bad |  |
| country_vaishyas_acceptance_min_add | Minimum Acceptance for the Vaishyas Social Class | country | additive | good |  |
| country_vaishyas_cultural_acceptance_mult | Cultural Acceptance for the Vaishyas Social Class | country | multiplicative | percent, good |  |
| country_vaishyas_education_access_add | Education Access for the Vaishyas Social Class | country | additive | good |  |
| country_vaishyas_education_access_mult | Education Access for the Vaishyas Social Class | country | multiplicative | percent, good |  |
| country_vaishyas_qualification_growth_add | Qualification Growth for the Vaishyas Social Class | country | additive | good |  |
| country_vaishyas_qualification_growth_mult | Qualification Growth for the Vaishyas Social Class | country | multiplicative | percent, good |  |
| country_vaishyas_qualification_growth_other_class_mult | Qualification Growth outside the Vaishyas Social Class for Vaishyas | country | multiplicative | percent, good |  |
| country_vaishyas_qualification_growth_same_class_mult | Qualification Growth within Vaishyas Social Class | country | multiplicative | percent, good |  |
| country_voting_power_base_add | Political Strength per Vote | country | additive | neutral | Hardcoded Enables elections |
| country_voting_power_cultural_erasure_mult | Voting contribution of Political Strength for the Cultural Erasure Status | country | multiplicative | percent, neutral |  |
| country_voting_power_from_literacy_add | Political Strength from Literate Pops' Votes | country | additive | neutral | Hardcoded Enables elections |
| country_voting_power_full_acceptance_mult | Voting contribution of Political Strength for the Full Acceptance Status | country | multiplicative | percent, neutral |  |
| country_voting_power_mult | Political Strength per Vote | country | multiplicative | percent, neutral |  |
| country_voting_power_open_prejudice_mult | Voting contribution of Political Strength for the Open Prejudice Status | country | multiplicative | percent, neutral |  |
| country_voting_power_second_rate_citizen_mult | Voting contribution of Political Strength for the Second-class Citizen Status | country | multiplicative | percent, neutral |  |
| country_voting_power_violent_hostility_mult | Voting contribution of Political Strength for the Violent Hostility Status | country | multiplicative | percent, neutral |  |
| country_voting_power_wealth_threshold_add | Wealth Threshold for Voting | country | additive | neutral | Hardcoded Enables elections |
| country_wage_cultural_erasure_mult | Wage for the Cultural Erasure Status | country | multiplicative | percent, good |  |
| country_wage_full_acceptance_mult | Wage for the Full Acceptance Status | country | multiplicative | percent, good |  |
| country_wage_open_prejudice_mult | Wage for the Open Prejudice Status | country | multiplicative | percent, good |  |
| country_wage_second_rate_citizen_mult | Wage for the Second-class Citizen Status | country | multiplicative | percent, good |  |
| country_wage_violent_hostility_mult | Wage for the Violent Hostility Status | country | multiplicative | percent, good |  |
| country_war_exhaustion_casualties_mult | War Exhaustion from Casualties | country | multiplicative | percent, bad |  |
| country_weekly_innovation_add | Innovation | country | additive | good |  |
| country_weekly_innovation_max_add | Maximum Innovation Investment | country | additive | good |  |
| country_weekly_innovation_mult | Innovation | country | multiplicative | percent, good |  |
| country_yankee_and_dixie_cultures_obsessed_with_guns | Yankee and Dixie Cultures gain an Obsession with Small Arms | country | boolean | neutral |  |
| dummy_modifier_type | This modifier type should never be used |  |  | bad |  |
| goods_input_aeroplanes_add | Aeroplanes input | goods | additive | bad |  |
| goods_input_ammunition_add | Ammunition input | goods | additive | bad |  |
| goods_input_ammunition_mult | Ammunition input | goods | multiplicative | percent, bad |  |
| goods_input_artillery_add | Artillery input | goods | additive | bad |  |
| goods_input_artillery_mult | Artillery input | goods | multiplicative | percent, bad |  |
| goods_input_automobiles_add | Automobiles input | goods | additive | bad |  |
| goods_input_clippers_add | Clippers input | goods | additive | bad |  |
| goods_input_clothes_add | Clothes input | goods | additive | bad |  |
| goods_input_coal_add | Coal input | goods | additive | bad |  |
| goods_input_dye_add | Dye input | goods | additive | bad |  |
| goods_input_electricity_add | Electricity input | goods | additive | bad |  |
| goods_input_engines_add | Engines input | goods | additive | bad |  |
| goods_input_explosives_add | Explosives input | goods | additive | bad |  |
| goods_input_fabric_add | Fabric input | goods | additive | bad |  |
| goods_input_fertilizer_add | Fertilizer input | goods | additive | bad |  |
| goods_input_fish_add | Fish input | goods | additive | bad |  |
| goods_input_fruit_add | Fruit input | goods | additive | bad |  |
| goods_input_glass_add | Glass input | goods | additive | bad |  |
| goods_input_grain_add | Grain input | goods | additive | bad |  |
| goods_input_groceries_add | Groceries input | goods | additive | bad |  |
| goods_input_hardwood_add | Hardwood input | goods | additive | bad |  |
| goods_input_iron_add | Iron input | goods | additive | bad |  |
| goods_input_ironclads_add | Ironclads input | goods | additive | bad |  |
| goods_input_lead_add | Lead input | goods | additive | bad |  |
| goods_input_liquor_add | Liquor input | goods | additive | bad |  |
| goods_input_manowars_add | Man-o-Wars input | goods | additive | bad |  |
| goods_input_meat_add | Meat input | goods | additive | bad |  |
| goods_input_merchant_marine_add | Merchant Marine input | goods | additive | bad |  |
| goods_input_oil_add | Oil input | goods | additive | bad |  |
| goods_input_oil_mult | Oil input | goods | multiplicative | percent, bad |  |
| goods_input_opium_add | Opium input | goods | additive | bad |  |
| goods_input_paper_add | Paper input | goods | additive | bad |  |
| goods_input_radios_add | Radio input | goods | additive | bad |  |
| goods_input_radios_mult | Radios input | goods | multiplicative | percent, bad |  |
| goods_input_rubber_add | Rubber input | goods | additive | bad |  |
| goods_input_silk_add | Fine Silk input | goods | additive | bad |  |
| goods_input_small_arms_add | Small Arms input | goods | additive | bad |  |
| goods_input_small_arms_mult | Small Arms input | goods | multiplicative | percent, bad |  |
| goods_input_steamers_add | Steamers input | goods | additive | bad |  |
| goods_input_steel_add | Steel input | goods | additive | bad |  |
| goods_input_sugar_add | Sugar input | goods | additive | bad |  |
| goods_input_sulfur_add | Sulfur input | goods | additive | bad |  |
| goods_input_tanks_add | Tanks input | goods | additive | bad |  |
| goods_input_tanks_mult | Tanks input | goods | multiplicative | percent, bad |  |
| goods_input_telephones_add | Telephone input | goods | additive | bad |  |
| goods_input_tobacco_add | Tobacco input | goods | additive | bad |  |
| goods_input_tools_add | Tools input | goods | additive | bad |  |
| goods_input_transportation_add | Transportation input | goods | additive | bad |  |
| goods_input_wine_add | Wine input | goods | additive | bad |  |
| goods_input_wood_add | Wood input | goods | additive | bad |  |
| goods_output_aeroplanes_add | Aeroplanes output | goods | additive | good |  |
| goods_output_aeroplanes_mult | Building Aeroplanes output | goods | multiplicative | percent, good |  |
| goods_output_ammunition_add | Ammunition output | goods | additive | good |  |
| goods_output_ammunition_mult | Building ammunition output | goods | multiplicative | percent, good |  |
| goods_output_artillery_add | Artillery output | goods | additive | good |  |
| goods_output_artillery_mult | Building Artillery output | goods | multiplicative | percent, good |  |
| goods_output_automobiles_add | Automobiles output | goods | additive | good |  |
| goods_output_automobiles_mult | Building Automobiles output | goods | multiplicative | percent, good |  |
| goods_output_clippers_add | Clippers output | goods | additive | good |  |
| goods_output_clippers_mult | Building Clippers output | goods | multiplicative | percent, good |  |
| goods_output_clothes_add | Clothes output | goods | additive | good |  |
| goods_output_coal_add | Coal output | goods | additive | good |  |
| goods_output_coffee_add | Coffee output | goods | additive | good |  |
| goods_output_dye_add | Dye output | goods | additive | good |  |
| goods_output_electricity_add | Electricity output | goods | additive | good |  |
| goods_output_electricity_mult | Building Electricity output | goods | multiplicative | percent, good |  |
| goods_output_engines_add | Engines output | goods | additive | good |  |
| goods_output_engines_mult | Building Engines output | goods | multiplicative | percent, good |  |
| goods_output_explosives_add | Explosives output | goods | additive | good |  |
| goods_output_fabric_add | Fabric output | goods | additive | good |  |
| goods_output_fabric_mult | Building Fabric output | goods | multiplicative | percent, good |  |
| goods_output_fertilizer_add | Fertilizer output | goods | additive | good |  |
| goods_output_fine_art_add | Fine Art output | goods | additive | good |  |
| goods_output_fish_add | Fish output | goods | additive | good |  |
| goods_output_fruit_add | Fruit output | goods | additive | good |  |
| goods_output_fruit_mult | Building Fruit output | goods | multiplicative | percent, good |  |
| goods_output_furniture_add | Furniture output | goods | additive | good |  |
| goods_output_glass_add | Glass output | goods | additive | good |  |
| goods_output_gold_add | Gold output | goods | additive | good |  |
| goods_output_grain_add | Grain output | goods | additive | good |  |
| goods_output_groceries_add | Groceries output | goods | additive | good |  |
| goods_output_hardwood_add | Hardwood output | goods | additive | good |  |
| goods_output_hardwood_mult | Building Hardwood output | goods | multiplicative | percent, good |  |
| goods_output_iron_add | Iron output | goods | additive | good |  |
| goods_output_ironclads_add | Ironclads output | goods | additive | good |  |
| goods_output_ironclads_mult | Building Ironclads output | goods | multiplicative | percent, good |  |
| goods_output_lead_add | Lead output | goods | additive | good |  |
| goods_output_liquor_add | Liquor output | goods | additive | good |  |
| goods_output_liquor_mult | Building Liquor output | goods | multiplicative | percent, good |  |
| goods_output_luxury_clothes_add | Luxury Clothes output | goods | additive | good |  |
| goods_output_luxury_furniture_add | Luxury Furniture output | goods | additive | good |  |
| goods_output_manowars_add | Man-o-Wars output | goods | additive | good |  |
| goods_output_manowars_mult | Building Man-o-Wars output | goods | multiplicative | percent, good |  |
| goods_output_meat_add | Meat output | goods | additive | good |  |
| goods_output_merchant_marine_add | Merchant Marine output | goods | additive | good |  |
| goods_output_oil_add | Oil output | goods | additive | good |  |
| goods_output_oil_mult | Building Oil output | goods | multiplicative | percent, good |  |
| goods_output_opium_add | Opium output | goods | additive | good |  |
| goods_output_paper_add | Paper output | goods | additive | good |  |
| goods_output_porcelain_add | Porcelain output | goods | additive | good |  |
| goods_output_radios_add | Radios output | goods | additive | good |  |
| goods_output_radios_mult | Building Radio output | goods | multiplicative | percent, good |  |
| goods_output_rubber_add | Rubber output | goods | additive | good |  |
| goods_output_services_add | Services output | goods | additive | good |  |
| goods_output_silk_add | Fine Silk output | goods | additive | good |  |
| goods_output_silk_mult | Building Silk output | goods | multiplicative | percent, good |  |
| goods_output_small_arms_add | Small Arms output | goods | additive | good |  |
| goods_output_small_arms_mult | Building Small Arms output | goods | multiplicative | percent, good |  |
| goods_output_steamers_add | Steamers output | goods | additive | good |  |
| goods_output_steamers_mult | Building Steamers output | goods | multiplicative | percent, good |  |
| goods_output_steel_add | Steel output | goods | additive | good |  |
| goods_output_sugar_add | Sugar output | goods | additive | good |  |
| goods_output_sugar_mult | Building Sugar output | goods | multiplicative | percent, good |  |
| goods_output_sulfur_add | Sulfur output | goods | additive | good |  |
| goods_output_tanks_add | Tanks output | goods | additive | good |  |
| goods_output_tanks_mult | Building Tanks output | goods | multiplicative | percent, good |  |
| goods_output_tea_add | Tea output | goods | additive | good |  |
| goods_output_telephones_add | Telephones output | goods | additive | good |  |
| goods_output_tobacco_add | Tobacco output | goods | additive | good |  |
| goods_output_tools_add | Tools output | goods | additive | good |  |
| goods_output_tools_mult | Building Tools output | goods | multiplicative | percent, good |  |
| goods_output_transportation_add | Transportation output | goods | additive | good |  |
| goods_output_wine_add | Wine output | goods | additive | good |  |
| goods_output_wine_mult | Building Wine output | goods | multiplicative | percent, good |  |
| goods_output_wood_add | Wood output | goods | additive | good |  |
| interest_group_amenability_add | Interest Group Amenability | interest_group | additive | good |  |
| interest_group_approval_add | Interest Group Approval | interest_group | additive | good |  |
| interest_group_ig_armed_forces_approval_add | Armed Forces Approval | interest_group | additive | good |  |
| interest_group_ig_armed_forces_pol_str_mult | Armed Forces Political Strength | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_armed_forces_pop_attraction_mult | Armed Forces Pop Attraction | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_devout_approval_add | Devout Approval | interest_group | additive | good |  |
| interest_group_ig_devout_pol_str_mult | Devout Political Strength | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_devout_pop_attraction_mult | Devout Pop Attraction | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_industrialists_approval_add | Industrialists Approval | interest_group | additive | good |  |
| interest_group_ig_industrialists_pol_str_mult | Industrialists Political Strength | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_industrialists_pop_attraction_mult | Industrialists Pop Attraction | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_intelligentsia_approval_add | Intelligentsia Approval | interest_group | additive | good |  |
| interest_group_ig_intelligentsia_pol_str_mult | Intelligentsia Political Strength | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_intelligentsia_pop_attraction_mult | Intelligentsia Pop Attraction | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_landowners_approval_add | Landowners Approval | interest_group | additive | good |  |
| interest_group_ig_landowners_pol_str_mult | Landowners Political Strength | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_landowners_pop_attraction_mult | Landowners Pop Attraction | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_petty_bourgeoisie_approval_add | Petite Bourgeoisie Approval | interest_group | additive | good |  |
| interest_group_ig_petty_bourgeoisie_pol_str_mult | Petite Bourgeoisie Political Strength | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_petty_bourgeoisie_pop_attraction_mult | Petite Bourgeoisie Pop Attraction | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_rural_folk_approval_add | Rural Folk Approval | interest_group | additive | good |  |
| interest_group_ig_rural_folk_pol_str_mult | Rural Folk Political Strength | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_rural_folk_pop_attraction_mult | Rural Folk Pop Attraction | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_trade_unions_approval_add | Trade Unions Approval | interest_group | additive | good |  |
| interest_group_ig_trade_unions_pol_str_mult | Trade Unions Political Strength | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_trade_unions_pop_attraction_mult | Trade Unions Pop Attraction | interest_group | multiplicative | percent, neutral |  |
| interest_group_in_government_approval_add | Government Interest Group Approval | interest_group | additive | good |  |
| interest_group_in_government_attraction_mult | Attraction of Interest Groups In Government | interest_group | multiplicative | percent, neutral |  |
| interest_group_in_opposition_agitator_popularity_add | Popularity of Agitators In Opposition | interest_group | additive | good |  |
| interest_group_in_opposition_approval_add | Opposition Interest Group Approval | interest_group | additive | good |  |
| interest_group_pol_str_factor | Interest Group Political Strength | interest_group | multiplicative | percent, good |  |
| interest_group_pol_str_mult | Interest Group Political Strength | interest_group | multiplicative | percent, neutral |  |
| interest_group_pop_attraction_mult | Interest Group Pop Attraction | interest_group | multiplicative | percent, neutral |  |
| military_formation_army_movement_speed_add | Army Speed | military_formation | additive | good |  |
| military_formation_army_movement_speed_mult | Army Speed | military_formation | multiplicative | percent, good |  |
| military_formation_attrition_risk_add | Attrition Risk | military_formation | additive | percent, bad |  |
| military_formation_attrition_risk_mult | Attrition Risk Multiplier | military_formation | multiplicative | percent, bad |  |
| military_formation_fleet_movement_speed_add | Fleet Speed | military_formation | additive | good |  |
| military_formation_fleet_movement_speed_mult | Fleet Speed | military_formation | multiplicative | percent, good |  |
| military_formation_interest_gain_mult | Fleet involvement Generation | military_formation | multiplicative | percent, good |  |
| military_formation_mobilization_speed_add | Formation Mobilization Speed | military_formation | additive | good |  |
| military_formation_mobilization_speed_mult | Formation Mobilization Speed | military_formation | multiplicative | percent, good |  |
| military_formation_organization_gain_add | Daily Organization Gain | military_formation | additive | good |  |
| military_formation_organization_gain_mult | Daily Organization Gain | military_formation | multiplicative | percent, good |  |
| political_movement_activism_growth_mult | Political Movement Activism Growth | political_movement | multiplicative | percent, bad |  |
| political_movement_character_attraction_mult | political_movement_character_attraction_mult | political_movement | multiplicative | percent, neutral |  |
| political_movement_pop_attraction_mult | Political Movement Pop Attraction | political_movement | multiplicative | percent, neutral |  |
| political_movement_radicalism_add | Political Movement Activism | political_movement | additive | percent, bad |  |
| political_movement_radicalism_from_enactment_approval_mult | Political Movement Activism Reduction from Approved Enactment | political_movement | multiplicative | percent, good |  |
| political_movement_radicalism_from_enactment_disapproval_mult | Political Movement Activism Increase from Disapproved Enactment | political_movement | multiplicative | percent, bad |  |
| power_bloc_allow_foreign_investment_lower_rank_bool | Foreign Investment Rights in Power Bloc Member with lower Rank | power_bloc | boolean | good |  |
| power_bloc_allow_port_access_bool | Allows port access between Power Bloc members | power_bloc | boolean | good |  |
| power_bloc_allow_wider_migration_area_bool | Allow Migration within a Power Bloc | power_bloc | boolean | good |  |
| power_bloc_cohesion_add | Power Bloc Cohesion | power_bloc | additive | good |  |
| power_bloc_cohesion_mult | Power Bloc Cohesion | power_bloc | multiplicative | percent, good |  |
| power_bloc_cohesion_per_member_add | Power Bloc Cohesion per Power Bloc Member | power_bloc | additive | good |  |
| power_bloc_customs_union_bool | Customs Union | power_bloc | boolean | neutral |  |
| power_bloc_disallow_embargo_bool | Cannot}} place Embargo on another Power Bloc member | power_bloc | boolean | neutral |  |
| power_bloc_disallow_war_bool | Cannot}} start or join wars amongst Power Bloc members | power_bloc | boolean | neutral |  |
| power_bloc_income_transfer_to_leader_factor | Income Transfer to Power Bloc Leader | power_bloc | multiplicative | neutral |  |
| power_bloc_invite_acceptance_add | Power Bloc Invitation Acceptance Chance | power_bloc | additive | good |  |
| power_bloc_invite_acceptance_great_power_add | Great Power Power Bloc Invitation Acceptance Chance | power_bloc | additive | good |  |
| power_bloc_invite_acceptance_major_power_add | Major Power Power Bloc Invitation Acceptance Chance | power_bloc | additive | good |  |
| power_bloc_invite_acceptance_minor_power_add | Minor Power Power Bloc Invitation Acceptance Chance | power_bloc | additive | good |  |
| power_bloc_invite_acceptance_unrecognized_major_power_add | Unrecognized Major Power Power Bloc Invitation Acceptance Chance | power_bloc | additive | good |  |
| power_bloc_invite_acceptance_unrecognized_regional_power_add | Unrecognized Regional Power Power Bloc Invitation Acceptance Chance | power_bloc | additive | good |  |
| power_bloc_leader_can_add_wargoal_bool | Allows free War Goal | power_bloc | boolean | neutral |  |
| power_bloc_leader_can_force_state_religion_bool | Allows Impose State Religion | power_bloc | boolean | neutral |  |
| power_bloc_leader_can_make_subjects_bool | Can **Subjugate** Power Bloc Member | power_bloc | boolean | neutral |  |
| power_bloc_leader_can_regime_change_bool | Allows Force Regime Change | power_bloc | boolean | neutral |  |
| power_bloc_leader_can_spread_culture_to_pb_bool | Allows Spread Primary Culture in Power Bloc Members | power_bloc | boolean | neutral |  |
| power_bloc_leverage_generation_mult | Leverage Generation | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_mult | Weekly Mandate Progress | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_great_power_member_add | Mandate Progress per Great Power | power_bloc | additive | good |  |
| power_bloc_mandate_progress_per_great_power_member_mult | Mandate Progress per Great Power | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_insignificant_power_member_add | Mandate Progress per Insignificant Power | power_bloc | additive | good |  |
| power_bloc_mandate_progress_per_insignificant_power_member_mult | Mandate Progress per Insignificant Power | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_major_power_member_add | Mandate Progress per Major Power | power_bloc | additive | good |  |
| power_bloc_mandate_progress_per_major_power_member_mult | Mandate Progress per Major Power | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_minor_power_member_add | Mandate Progress per Minor Power | power_bloc | additive | good |  |
| power_bloc_mandate_progress_per_minor_power_member_mult | Mandate Progress per Minor Power | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_unrecognized_major_power_member_add | Mandate Progress per Unrecognized Major Power | power_bloc | additive | good |  |
| power_bloc_mandate_progress_per_unrecognized_major_power_member_mult | Mandate Progress per Unrecognized Major Power | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_unrecognized_power_member_add | Mandate Progress per Unrecognized Power | power_bloc | additive | good |  |
| power_bloc_mandate_progress_per_unrecognized_power_member_mult | Mandate Progress per Unrecognized Power | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_unrecognized_regional_power_member_add | Mandate Progress per Unrecognized Regional Power | power_bloc | additive | good |  |
| power_bloc_mandate_progress_per_unrecognized_regional_power_member_mult | Mandate Progress per Unrecognized Regional Power | power_bloc | multiplicative | percent, good |  |
| power_bloc_target_sway_cost_mult | Sway Maneuver cost for the Diplomatic Play Target | power_bloc | multiplicative | percent, bad |  |
| power_bloc_trade_advantage_add | Trade Advantage within Power Bloc | power_bloc | additive | good |  |
| ship_accuracy_add | Accuracy | ship | additive | good |  |
| ship_accuracy_mult | Accuracy | ship | multiplicative | percent, good |  |
| ship_armor_add | Ship Armor | ship | additive | good |  |
| ship_armor_mult | Ship Armor | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_destroyer_accuracy_add | Destroyer Accuracy | ship | additive | percent, good |  |
| ship_battle_against_ship_type_destroyer_accuracy_mult | Destroyer Accuracy | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_dreadnought_hull_damage_mult | Dreadnought Hull Attack Damage | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_modern_ironclad_hull_damage_mult | Modern Ironclad Hull Attack Damage | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_pre_dreadnought_hull_damage_mult | Pre-Dreadnought Hull Attack Damage | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_submarine_accuracy_add | Submarine Accuracy | ship | additive | percent, good |  |
| ship_battle_against_ship_type_submarine_accuracy_mult | Submarine Accuracy | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_super_dreadnought_hull_damage_mult | Super Dreadnought Hull Attack Damage | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_torpedo_boat_accuracy_add | Torpedo Boat Accuracy | ship | additive | percent, good |  |
| ship_battle_against_ship_type_torpedo_boat_accuracy_mult | Torpedo Boat Accuracy | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_torpedo_boat_destroyer_accuracy_add | Torpedo Boat Destroyer Accuracy | ship | additive | percent, good |  |
| ship_battle_against_ship_type_torpedo_boat_destroyer_accuracy_mult | Torpedo Boat Destroyer Accuracy | ship | multiplicative | percent, good |  |
| ship_battle_condition_accuracy_penalty_mult | Battle Condition Accuracy Penalty | ship | multiplicative | percent, good |  |
| ship_blockade_strength_add | Blockade Strength | ship | additive | good |  |
| ship_blockade_strength_mult | Blockade Strength | ship | multiplicative | percent, good |  |
| ship_carrying_capacity_add | Carrying Capacity | ship | additive | good |  |
| ship_carrying_capacity_mult | Carrying Capacity | ship | multiplicative | percent, good |  |
| ship_construction_progress_max_add | Max Ship Construction Progress | ship | additive | neutral |  |
| ship_construction_progress_max_mult | Max Ship Construction Progress | ship | multiplicative | percent, good |  |
| ship_crew_damage_add | Crew Attack Damage | ship | additive | good |  |
| ship_crew_damage_mult | Crew Attack Damage | ship | multiplicative | percent, good |  |
| ship_crew_experience_gain_add | Weekly Experience Gain for Ship Crew | ship | additive | good |  |
| ship_crew_experience_gain_mult | Weekly Experience Gain for Ship Crew | ship | multiplicative | percent, good |  |
| ship_crew_max_add | Ship Crew | ship | additive | good |  |
| ship_crew_max_mult | Ship Crew | ship | multiplicative | percent, good |  |
| ship_critical_hit_chance_add | Critical Chance | ship | additive | percent, good |  |
| ship_critical_hit_chance_mult | Critical Chance | ship | multiplicative | percent, good |  |
| ship_critical_hit_multiplier_add | Critical Damage | ship | additive | percent, good |  |
| ship_critical_hit_multiplier_mult | Critical Damage | ship | multiplicative | percent, good |  |
| ship_detection_add | Detection | ship | additive | good |  |
| ship_detection_mult | Detection | ship | multiplicative | percent, good |  |
| ship_hit_points_max_add | Maximum Ship Hit Points | ship | additive | good |  |
| ship_hit_points_max_mult | Maximum Ship Hit Points | ship | multiplicative | percent, good |  |
| ship_hull_damage_add | Hull Attack Damage | ship | additive | good |  |
| ship_hull_damage_mult | Hull Attack Damage | ship | multiplicative | percent, good |  |
| ship_interest_gain_add | Ship Involvement Generation | ship | additive | good |  |
| ship_interest_gain_mult | Ship Involvement Generation | ship | multiplicative | percent, good |  |
| ship_marine_capacity_add | Marine Capacity | ship | additive | good |  |
| ship_marine_capacity_mult | Marine Capacity | ship | multiplicative | percent, good |  |
| ship_max_distance_to_port_add | Max Distance to Port | ship | additive | good |  |
| ship_max_distance_to_port_mult | Max Distance to Port | ship | multiplicative | percent, good |  |
| ship_movement_speed_add | Ship Speed | ship | additive | good |  |
| ship_movement_speed_mult | Ship Speed | ship | multiplicative | percent, good |  |
| ship_naval_invasion_efficiency_mult | Naval Invasion Efficiency | ship | multiplicative | percent, good |  |
| ship_readiness_gain_add | Readiness | ship | additive | good |  |
| ship_readiness_gain_mult | Readiness | ship | multiplicative | percent, good |  |
| ship_screening_add | Screening | ship | additive | good |  |
| ship_screening_mult | Screening | ship | multiplicative | percent, good |  |
| ship_ship_type_aircraft_carrier_hull_damage_mult | Aircraft Carrier Hull Attack Damage | ship | multiplicative | percent, good |  |
| ship_ship_type_submarine_hull_damage_mult | Submarine Hull Attack Damage | ship | multiplicative | percent, good |  |
| ship_ship_type_supply_ship_supply_capacity_mult | Supply Ship Supply Capacity | ship | multiplicative | percent, good |  |
| ship_suffered_accuracy_mult | Suffered Accuracy | ship | multiplicative | percent, bad |  |
| ship_suffered_crew_damage_mult | Suffered Crew Attack Damage | ship | multiplicative | percent, bad |  |
| ship_suffered_crit_chance_mult | Suffered Critical Chance | ship | multiplicative | percent, bad |  |
| ship_suffered_crit_damage_mult | Suffered Critical Damage | ship | multiplicative | percent, bad |  |
| ship_suffered_hull_damage_mult | Suffered Hull Attack Damage | ship | multiplicative | percent, bad |  |
| ship_supply_capacity_add | Supply Capacity | ship | additive | good |  |
| ship_supply_capacity_mult | Supply Capacity | ship | multiplicative | percent, good |  |
| ship_supply_efficiency_add | Supply Efficiency | ship | additive | percent, good |  |
| ship_supply_efficiency_mult | Supply Efficiency | ship | multiplicative | percent, good |  |
| ship_visibility_add | Visibility | ship | additive | bad |  |
| ship_visibility_mult | Visibility | ship | multiplicative | percent, bad |  |
| ship_vulnerability_add | Vulnerability | ship | additive | bad |  |
| ship_vulnerability_mult | Vulnerability | ship | multiplicative | percent, bad |  |
| state_academics_investment_pool_contribution_add | Academics Investment Pool contribution | state | additive | percent, good |  |
| state_academics_investment_pool_efficiency_mult | Academics Investment Pool contribution efficiency | state | multiplicative | percent, good |  |
| state_academics_mortality_mult | Mortality of Academics | state | multiplicative | percent, bad |  |
| state_allow_assimilation_in_homeland_bool | Assimilation in Homeland States Allowed | state | boolean | good |  |
| state_allow_assimilation_without_presence_bool | Assimilation to Primary Culture Always Allowed | state | boolean | good |  |
| state_allow_conversion_without_presence_bool | Conversion to State Religion Always Allowed | state | boolean | good |  |
| state_aristocrats_investment_pool_contribution_add | Aristocrats Investment Pool contribution | state | additive | percent, good |  |
| state_aristocrats_investment_pool_efficiency_mult | Aristocrats Investment Pool contribution efficiency | state | multiplicative | percent, good |  |
| state_aristocrats_mortality_mult | Mortality of Aristocrats | state | multiplicative | percent, bad |  |
| state_assimilation_mult | Assimilation | state | multiplicative | percent, good |  |
| state_birth_rate_mult | Birth Rate | state | multiplicative | percent, good |  |
| state_blockade_resistance_add | Blockade Resistance | state | additive | good |  |
| state_building_barrack_max_level_add | Barracks Max Level | state | additive | good |  |
| state_building_conscription_center_max_level_add | Maximum Conscription Limit | state | additive | good |  |
| state_building_construction_sector_max_level_add | Construction Sector Max Level | state | additive | good |  |
| state_building_naval_fortification_max_level_add | Naval Fortification Max Level | state | additive | good |  |
| state_bureaucracy_population_base_cost_factor_mult | Bureaucracy Population Cost Multiplier | state | multiplicative | percent, bad |  |
| state_bureaucrats_investment_pool_contribution_add | Bureaucrats Investment Pool contribution | state | additive | percent, good |  |
| state_bureaucrats_investment_pool_efficiency_mult | Bureaucrats Investment Pool contribution efficiency | state | multiplicative | percent, good |  |
| state_buy_orders_ammunition_add | Ammunition Buy Orders | state | additive | neutral |  |
| state_buy_orders_artillery_add | Artillery Buy Orders | state | additive | neutral |  |
| state_buy_orders_small_arms_add | Small Arms Buy Orders | state | additive | neutral |  |
| state_capitalists_investment_pool_contribution_add | Capitalists Investment Pool contribution | state | additive | percent, good |  |
| state_capitalists_investment_pool_efficiency_mult | Capitalists Investment Pool contribution efficiency | state | multiplicative | percent, good |  |
| state_clergymen_investment_pool_contribution_add | Clergymen Investment Pool contribution | state | additive | percent, good |  |
| state_clergymen_investment_pool_efficiency_mult | Clergymen Investment Pool contribution efficiency | state | multiplicative | percent, good |  |
| state_clerks_investment_pool_contribution_add | Clerks Investment Pool contribution | state | additive | percent, good |  |
| state_clerks_investment_pool_efficiency_mult | Clerks Investment Pool contribution efficiency | state | multiplicative | percent, good |  |
| state_colony_growth_creation_factor | Colonial Growth Generation | state | multiplicative | good |  |
| state_colony_growth_speed_mult | Colony Growth Speed | state | multiplicative | percent, good |  |
| state_conscription_rate_add | Conscription Rate | state | additive | percent, good |  |
| state_conscription_rate_mult | Conscriptable Battalions | state | multiplicative | percent, good |  |
| state_construction_mult | State Construction Efficiency | state | multiplicative | percent, good |  |
| state_contiguous_incorporation_speed_mult | Contiguous Incorporation Speed | state | multiplicative | percent, good |  |
| state_control_strait_bool | Control Strait | state | boolean | good |  |
| state_conversion_mult | Conversion | state | multiplicative | percent, good |  |
| state_decree_cost_mult | Decree Cost | state | multiplicative | percent, bad |  |
| state_dependent_political_participation_add | Dependent Enfranchisement | state | additive | percent, good |  |
| state_dependent_wage_add | Yearly Dependents Income | state | additive | good |  |
| state_dependent_wage_mult | Dependents Income | state | multiplicative | percent, good |  |
| state_devastation_decay_mult | Devastation Recovery | state | multiplicative | percent, good |  |
| state_disallow_incorporation_bool | State Incorporation Disallowed | state | boolean | bad |  |
| state_education_access_add | Education Access | state | additive | percent, good |  |
| state_education_access_wealth_add | Education Access (Wealth-based) | state | additive | percent, good |  |
| state_engineers_investment_pool_contribution_add | Engineers Investment Pool contribution | state | additive | percent, good |  |
| state_engineers_investment_pool_efficiency_mult | Engineers Investment Pool contribution efficiency | state | multiplicative | percent, good |  |
| state_expected_sol_from_literacy | Minimum Expected Standard of Living from Literacy | state |  | bad |  |
| state_expected_sol_mult | Minimum Expected Standard of Living | state | multiplicative | percent, bad |  |
| state_export_advantage_mult | Trade Advantage for Exports | state | multiplicative | percent, good |  |
| state_farmers_investment_pool_contribution_add | Farmers Investment Pool contribution | state | additive | percent, good |  |
| state_farmers_investment_pool_efficiency_mult | Farmers Investment Pool contribution efficiency | state | multiplicative | percent, good |  |
| state_farmers_mortality_mult | Mortality of Farmers | state | multiplicative | percent, bad |  |
| state_food_security_add | Food Security | state | additive | percent, good |  |
| state_fortification_bombardment_resistance_add | Naval Fortification Bombardment Resistance | state | additive | good |  |
| state_fortification_naval_battle_mult | Naval Fortification Battle Defense | state | multiplicative | percent, good |  |
| state_fortification_naval_invasion_add | Naval Fortification Invasion Defense | state | additive | good |  |
| state_free_state_pop_support_movement_anti_slavery_mult | Abolitionist Movement Pop Attraction in non-Slave States | state | multiplicative | percent, neutral |  |
| state_harvest_condition_disease_outbreak_duration_mult | Disease Outbreak Harvest Condition Duration | state | multiplicative | percent, bad |  |
| state_harvest_condition_disease_outbreak_impact_mult | Disease Outbreak Harvest Condition Impact | state | multiplicative | percent, bad |  |
| state_harvest_condition_drought_duration_mult | Drought Harvest Condition Duration | state | multiplicative | percent, bad |  |
| state_harvest_condition_drought_impact_mult | Drought Harvest Condition Impact | state | multiplicative | percent, bad |  |
| state_harvest_condition_earthquake_duration_mult | Earthquake Harvest Condition Duration | state | multiplicative | percent, bad |  |
| state_harvest_condition_earthquake_impact_mult | Earthquake Harvest Condition Impact | state | multiplicative | percent, bad |  |
| state_harvest_condition_extreme_winds_duration_mult | Extreme Winds Harvest Condition Duration | state | multiplicative | percent, bad |  |
| state_harvest_condition_extreme_winds_impact_mult | Extreme Winds Harvest Condition Impact | state | multiplicative | percent, bad |  |
| state_harvest_condition_flood_duration_mult | Flood Harvest Condition Duration | state | multiplicative | percent, bad |  |
| state_harvest_condition_flood_impact_mult | Flood Harvest Condition Impact | state | multiplicative | percent, bad |  |
| state_harvest_condition_heatwave_duration_mult | Heatwave Harvest Condition Duration | state | multiplicative | percent, bad |  |
| state_harvest_condition_heatwave_impact_mult | Heatwave Harvest Condition Impact | state | multiplicative | percent, bad |  |
| state_harvest_condition_tsunami_duration_mult | Tsunami Harvest Condition Duration | state | multiplicative | percent, bad |  |
| state_harvest_condition_tsunami_impact_mult | Tsunami Harvest Condition Impact | state | multiplicative | percent, bad |  |
| state_harvest_condition_wildfire_duration_mult | Wildfire Harvest Condition Duration | state | multiplicative | percent, bad |  |
| state_harvest_condition_wildfire_impact_mult | Wildfire Harvest Condition Impact | state | multiplicative | percent, bad |  |
| state_import_advantage_mult | Trade Advantage for Imports | state | multiplicative | percent, good |  |
| state_incorporation_speed_mult | Incorporation Speed | state | multiplicative | percent, good |  |
| state_infrastructure_add | Infrastructure | state | additive | good |  |
| state_infrastructure_from_automobiles_consumption_add | Infrastructure from Pop Automobiles Consumption | state | additive | good |  |
| state_infrastructure_from_population_add | Infrastructure per 100.0K Population | state | additive | good |  |
| state_infrastructure_from_population_max_add | Maximum Infrastructure from Population | state | additive | good |  |
| state_infrastructure_from_population_max_mult | Maximum Infrastructure from Population | state | multiplicative | percent, good |  |
| state_infrastructure_from_population_mult | Infrastructure per 100.0K Population | state | multiplicative | percent, good |  |
| state_infrastructure_mult | Infrastructure | state | multiplicative | percent, good |  |
| state_institution_impact_add | Impact of Institutions | state | additive | percent, good |  |
| state_laborers_investment_pool_contribution_add | Laborers Investment Pool contribution | state | additive | percent, good |  |
| state_laborers_investment_pool_efficiency_mult | Laborers Investment Pool contribution efficiency | state | multiplicative | percent, good |  |
| state_laborers_mortality_mult | Mortality of Laborers | state | multiplicative | percent, bad |  |
| state_literacy_growth_add | Literacy Growth | state | additive | percent, good |  |
| state_lower_strata_expected_sol_add | Minimum Expected Standard of Living for the Lower Strata | state | additive | neutral |  |
| state_loyalism_increases_cultural_erasure_mult | Loyalism increases for the Cultural Erasure Status | state | multiplicative | percent, good |  |
| state_loyalism_increases_full_acceptance_mult | Loyalism increases for the Full Acceptance Status | state | multiplicative | percent, good |  |
| state_loyalism_increases_open_prejudice_mult | Loyalism increases for the Open Prejudice Status | state | multiplicative | percent, good |  |
| state_loyalism_increases_second_rate_citizen_mult | Loyalism increases for the Second-class Citizen Status | state | multiplicative | percent, good |  |
| state_loyalism_increases_violent_hostility_mult | Loyalism increases for the Violent Hostility Status | state | multiplicative | percent, good |  |
| state_loyalists_from_political_movements_mult | Loyalists from Political Movements | state | multiplicative | percent, good |  |
| state_machinists_investment_pool_contribution_add | Machinists Investment Pool contribution | state | additive | percent, good |  |
| state_machinists_investment_pool_efficiency_mult | Machinists Investment Pool contribution efficiency | state | multiplicative | percent, good |  |
| state_machinists_mortality_mult | Mortality of Machinists | state | multiplicative | percent, bad |  |
| state_market_access_price_impact | Market Access Price Impact | state |  | percent, neutral |  |
| state_max_trade_advantage_from_capacity_add | Maximum Trade Advantage from Capacity | state | additive | percent, good |  |
| state_middle_strata_expected_sol_add | Minimum Expected Standard of Living for the Middle Strata | state | additive | neutral |  |
| state_migration_pull_add | Migration Attraction | state | additive | good |  |
| state_migration_pull_mult | Migration Attraction | state | multiplicative | percent, good |  |
| state_migration_pull_unincorporated_mult | Migration Attraction in Unincorporated States | state | multiplicative | percent, good |  |
| state_migration_quota_mult | Migration Quota | state | multiplicative | percent, neutral |  |
| state_minimum_incorporated_subsistence_arable_land_add | Minimum Subsistence Land Share in Incorporated States | state | additive | percent, neutral |  |
| state_mortality_mult | Mortality | state | multiplicative | percent, bad |  |
| state_mortality_turmoil_mult | Mortality per Turmoil | state | multiplicative | percent, bad |  |
| state_mortality_wealth_mult | Mortality per Wealth | state | multiplicative | percent, bad |  |
| state_non_contiguous_incorporation_speed_mult | Non-Contiguous Incorporation Speed | state | multiplicative | percent, good |  |
| state_non_homeland_colony_growth_speed_mult | Colony Growth Speed in non-Homeland States | state | multiplicative | percent, good |  |
| state_non_homeland_mortality_mult | Mortality in non-Homeland States | state | multiplicative | percent, bad |  |
| state_officers_investment_pool_contribution_add | Officers Investment Pool contribution | state | additive | percent, good |  |
| state_officers_investment_pool_efficiency_mult | Officers Investment Pool contribution efficiency | state | multiplicative | percent, good |  |
| state_peasants_consumption_multiplier_add | Goods consumption for Peasants | state | additive | percent, bad |  |
| state_peasants_education_access_add | Education Access for Peasants | state | additive | percent, good |  |
| state_peasants_internal_migration_disallowed_bool | Disallowed Internal Migration for Peasants | state | boolean | bad |  |
| state_peasants_mass_migration_disallowed_bool | Disallowed Mass Migration for Peasants | state | boolean | bad |  |
| state_peasants_mortality_mult | Mortality of Peasants | state | multiplicative | percent, bad |  |
| state_political_strength_from_wealth_mult | Political Strength from Wealth | state | multiplicative | percent, neutral |  |
| state_political_strength_from_welfare_mult | Political Strength when receiving Welfare | state | multiplicative | percent, neutral |  |
| state_pollution_generation_add | Generated Pollution | state | additive | bad |  |
| state_pollution_reduction_health_mult | Pollution Health Effects Reduction | state | multiplicative | percent, bad |  |
| state_pop_pol_str_add | Universal Pop Political Strength | state | additive | neutral |  |
| state_pop_pol_str_mult | Universal Pop Political Strength | state | multiplicative | percent, neutral |  |
| state_pop_qualifications_mult | Qualifications | state | multiplicative | percent, good |  |
| state_pop_support_movement_anarchist_add | Anarchist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_anarchist_mult | Anarchist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_anti_slavery_add | Abolitionist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_anti_slavery_mult | Abolitionist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_bonapartist_add | Bonapartist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_bonapartist_mult | Bonapartist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_carlist_add | Carlist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_carlist_mult | Carlist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_communist_add | Communist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_communist_mult | Communist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_corporatist_add | Corporatist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_corporatist_mult | Corporatist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_cultural_majority_add | Cultural Majority Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_cultural_majority_mult | Cultural Majority Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_cultural_minority_add | Cultural Minority Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_cultural_minority_mult | Cultural Minority Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_fascist_add | Fascist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_fascist_mult | Fascist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_feminist_add | Feminist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_feminist_mult | Feminist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_german_national_add | German National Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_german_national_mult | German National Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_india_pan_national_add | Indian National Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_india_pan_national_mult | Indian National Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_italian_national_add | Italian National Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_italian_national_mult | Italian National Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_labor_add | Labor Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_labor_mult | Labor Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_land_reform_add | Peasant Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_land_reform_mult | Peasant Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_legitimist_add | Legitimist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_legitimist_mult | Legitimist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_liberal_add | Liberal Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_liberal_mult | Liberal Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_miguelist_add | Miguelist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_miguelist_mult | Miguelist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_modernizer_add | Modernization Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_modernizer_mult | Modernization Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_nihilist_add | Nihilist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_nihilist_mult | Nihilist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_orleanist_add | Orleanist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_orleanist_mult | Orleanist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_positivist_add | Positivist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_positivist_mult | Positivist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_pro_slavery_add | Pro-Slavery Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_pro_slavery_mult | Pro-Slavery Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_radical_add | Radical Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_radical_mult | Radical Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_reactionary_add | Reactionary Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_reactionary_mult | Reactionary Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_religious_majority_add | Religious Majority Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_religious_majority_mult | Religious Majority Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_religious_minority_add | Religious Minority Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_religious_minority_mult | Religious Minority Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_royalist_absolutist_add | Absolutist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_royalist_absolutist_mult | Absolutist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_royalist_constitutional_add | Royalist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_royalist_constitutional_mult | Royalist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_slave_revolt_add | Slave Revolt Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_slave_revolt_mult | Slave Revolt Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_socialist_add | Socialist Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_socialist_mult | Socialist Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_utilitarian_add | Utilitarian Movement Pop Attraction | state | additive | neutral |  |
| state_pop_support_movement_utilitarian_mult | Utilitarian Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_yugoslav_national_add | state_pop_support_movement_yugoslav_national_add | state | additive | neutral |  |
| state_pop_support_movement_yugoslav_national_mult | German National Movement Pop Attraction | state | multiplicative | percent, neutral |  |
| state_radicalism_increases_cultural_erasure_mult | Radicalism increases for the Cultural Erasure Status | state | multiplicative | percent, bad |  |
| state_radicalism_increases_full_acceptance_mult | Radicalism increases for the Full Acceptance Status | state | multiplicative | percent, bad |  |
| state_radicalism_increases_open_prejudice_mult | Radicalism increases for the Open Prejudice Status | state | multiplicative | percent, bad |  |
| state_radicalism_increases_second_rate_citizen_mult | Radicalism increases for the Second-class Citizen Status | state | multiplicative | percent, bad |  |
| state_radicalism_increases_violent_hostility_mult | Radicalism increases for the Violent Hostility Status | state | multiplicative | percent, bad |  |
| state_radicals_and_loyalists_from_sol_change_mult | Radicals and Loyalists from Standard of Living changes | state | multiplicative | percent, neutral |  |
| state_radicals_from_political_movements_mult | Radicals from Political Movements | state | multiplicative | percent, bad |  |
| state_sell_orders_ammunition_add | Ammunition Sell Orders | state | additive | neutral |  |
| state_sell_orders_artillery_add | Artillery Sell Orders | state | additive | neutral |  |
| state_sell_orders_grain_add | Grain Sell Orders | state | additive | neutral |  |
| state_sell_orders_small_arms_add | Small Arms Sell Orders | state | additive | neutral |  |
| state_shopkeepers_investment_pool_contribution_add | Shopkeepers Investment Pool contribution | state | additive | percent, good |  |
| state_shopkeepers_investment_pool_efficiency_mult | Shopkeepers Investment Pool contribution efficiency | state | multiplicative | percent, good |  |
| state_slave_import_mult | Slave Imports | state | multiplicative | percent, good |  |
| state_slaves_mortality_mult | Mortality of Slaves | state | multiplicative | percent, bad |  |
| state_soldiers_investment_pool_contribution_add | Servicemen Investment Pool contribution | state | additive | percent, good |  |
| state_soldiers_investment_pool_efficiency_mult | Servicemen Investment Pool contribution efficiency | state | multiplicative | percent, good |  |
| state_soldiers_mortality_mult | Mortality of Servicemen | state | multiplicative | percent, bad |  |
| state_standard_of_living_add | Standard of Living | state | additive | good |  |
| state_subvention_export_add | Maximum Subventions on Exports | state | additive | percent, neutral |  |
| state_subvention_import_add | Maximum Subventions on Imports | state | additive | percent, neutral |  |
| state_tariff_export_add | Maximum Tariffs on Exports | state | additive | percent, neutral |  |
| state_tariff_import_add | Maximum Tariffs on Imports | state | additive | percent, neutral |  |
| state_tax_capacity_add | Taxation Capacity | state | additive | good |  |
| state_tax_capacity_mult | Taxation Capacity | state | multiplicative | percent, good |  |
| state_tax_collection_mult | Tax Collection | state | multiplicative | percent, neutral |  |
| state_tax_waste_add | Tax Waste | state | additive | percent, bad |  |
| state_trade_advantage_from_capacity_add | Trade Advantage from Capacity | state | additive | percent, good |  |
| state_trade_advantage_mult | Trade Advantage | state | multiplicative | percent, good |  |
| state_trade_advantage_same_religion_add | Trade Advantage with Co-Religionists | state | additive | good |  |
| state_trade_capacity_add | Trade Capacity | state | additive | good |  |
| state_trade_capacity_mult | Trade Capacity | state | multiplicative | percent, good |  |
| state_trade_center_max_limit_add | Trade Center Max Level | state | additive | good |  |
| state_trade_quantity_mult | Traded Quantity | state | multiplicative | percent, good |  |
| state_turmoil_effects_mult | State Penalties from Turmoil | state | multiplicative | percent, bad |  |
| state_unincorporated_starting_wages_mult | Starting Wages in Unincorporated States | state | multiplicative | percent, neutral |  |
| state_upper_strata_expected_sol_add | Minimum Expected Standard of Living for the Upper Strata | state | additive | neutral |  |
| state_urbanization_per_level_add | Urbanization per Urban Center | state | additive | neutral |  |
| state_urbanization_per_level_mult | Urbanization per Urban Center | state | multiplicative | percent, bad |  |
| state_weekly_trades_add | Weekly Trades | state | additive | good |  |
| state_welfare_payments_add | Welfare Payments | state | additive | percent, neutral |  |
| state_welfare_payments_mult | Welfare Payments Multiplier | state | multiplicative | percent, neutral |  |
| state_working_adult_ratio_add | Workforce Ratio | state | additive | percent, good |  |
| tax_consumption_add | Consumption Tax Rate | tax | additive | percent, neutral |  |
| tax_dividends_add | Dividends Tax Rate | tax | additive | percent, neutral |  |
| tax_heathen_add | Religious Tax | tax | additive | neutral |  |
| tax_income_add | Income Tax Rate | tax | additive | percent, neutral |  |
| tax_land_add | Land Tax | tax | additive | neutral |  |
| tax_per_capita_add | Per Capita Tax | tax | additive | neutral |  |
| unit_army_defense_add | Army Defense | unit | additive | good | combat |
| unit_army_defense_mult | Army Defense | unit | multiplicative | percent, good | combat |
| unit_army_experience_gain_add | Weekly Experience Gain for Armies | unit | additive | good | non-combat combat (if in battle on weekly tick) |
| unit_army_experience_gain_mult | Weekly Experience Gain for Armies | unit | multiplicative | percent, good | non-combat combat (if in battle on weekly tick) |
| unit_army_offense_add | Army Offense | unit | additive | good | combat |
| unit_army_offense_mult | Army Offense | unit | multiplicative | percent, good | combat |
| unit_combat_unit_type_cannon_artillery_offense_mult | Cannon Artillery Offense | unit | multiplicative | percent, good |  |
| unit_combat_unit_type_heavy_tank_offense_mult | Heavy Tanks Offense | unit | multiplicative | percent, good |  |
| unit_combat_unit_type_mechanized_infantry_offense_add | Mechanized Infantry Offense | unit | additive | good |  |
| unit_combat_unit_type_mobile_artillery_offense_mult | Mobile Artillery Offense | unit | multiplicative | percent, good |  |
| unit_combat_unit_type_shrapnel_artillery_offense_mult | Shrapnel Artillery Offense | unit | multiplicative | percent, good |  |
| unit_combat_unit_type_siege_artillery_offense_mult | Siege Artillery Offense | unit | multiplicative | percent, good |  |
| unit_combat_unit_type_squad_infantry_offense_add | Squad Infantry Offense | unit | additive | good |  |
| unit_combat_unit_type_trench_infantry_offense_add | Trench Infantry Offense | unit | additive | good |  |
| unit_defense_add | Defense | unit | additive | good | combat |
| unit_defense_developed_add | Defense in Flat Terrain | unit | additive | good |  |
| unit_defense_developed_mult | Defense in Flat Terrain | unit | multiplicative | percent, good |  |
| unit_defense_elevated_add | Defense in Elevated Terrain | unit | additive | good |  |
| unit_defense_elevated_mult | Defense in Elevated Terrain | unit | multiplicative | percent, good |  |
| unit_defense_flat_add | Defense in Flat Terrain | unit | additive | good |  |
| unit_defense_flat_mult | Defense in Flat Terrain | unit | multiplicative | percent, good |  |
| unit_defense_forested_add | Defense in Forested Terrain | unit | additive | good |  |
| unit_defense_forested_mult | Defense in Forested Terrain | unit | multiplicative | percent, good |  |
| unit_defense_hazardous_add | Defense in Hazardous Terrain | unit | additive | good |  |
| unit_defense_hazardous_mult | Defense in Hazardous Terrain | unit | multiplicative | percent, good |  |
| unit_defense_mult | Defense | unit | multiplicative | percent, good | combat |
| unit_defense_water_add | Defense in Flat Terrain | unit | additive | good |  |
| unit_defense_water_mult | Defense in Flat Terrain | unit | multiplicative | percent, good |  |
| unit_devastation_mult | Devastation | unit | multiplicative | percent, neutral | combat |
| unit_experience_gain_add | Weekly Experience Gain for Armies | unit | additive | good | non-combat combat (if in battle on weekly tick) |
| unit_experience_gain_mult | Weekly Experience Gain for Armies | unit | multiplicative | percent, good | non-combat combat (if in battle on weekly tick) |
| unit_kill_rate_add | Kill Rate | unit | additive | percent, good | combat |
| unit_morale_damage_mult | Morale Damage | unit | multiplicative | percent, good | combat |
| unit_morale_loss_add | Morale Loss | unit | additive | bad | combat |
| unit_morale_loss_mult | Morale Loss | unit | multiplicative | percent, bad | combat |
| unit_morale_recovery_mult | Morale Recovery | unit | multiplicative | percent, good | non-combat |
| unit_naval_invasion_efficiency_mult | Naval Invasion Efficiency | unit | multiplicative | percent, good |  |
| unit_occupation_mult | Battle Occupation | unit | multiplicative | percent, good | combat |
| unit_offense_add | Offense | unit | additive | good | combat |
| unit_offense_developed_add | Offense in Flat Terrain | unit | additive | good |  |
| unit_offense_developed_mult | Offense in Flat Terrain | unit | multiplicative | percent, good |  |
| unit_offense_elevated_add | Offense in Elevated Terrain | unit | additive | good |  |
| unit_offense_elevated_mult | Offense in Elevated Terrain | unit | multiplicative | percent, good |  |
| unit_offense_flat_add | Offense in Flat Terrain | unit | additive | good |  |
| unit_offense_flat_mult | Offense in Flat Terrain | unit | multiplicative | percent, good |  |
| unit_offense_forested_add | Offense in Forested Terrain | unit | additive | good |  |
| unit_offense_forested_mult | Offense in Forested Terrain | unit | multiplicative | percent, good |  |
| unit_offense_hazardous_add | Offense in Hazardous Terrain | unit | additive | good |  |
| unit_offense_hazardous_mult | Offense in Hazardous Terrain | unit | multiplicative | percent, good |  |
| unit_offense_mult | Offense | unit | multiplicative | percent, good | combat |
| unit_offense_water_add | Offense in Flat Terrain | unit | additive | good |  |
| unit_offense_water_mult | Offense in Flat Terrain | unit | multiplicative | percent, good |  |
| unit_provinces_captured_mult | Provinces Captured | unit | multiplicative | percent, good | combat |
| unit_provinces_lost_mult | Provinces Lost | unit | multiplicative | percent, bad | combat |
| unit_recovery_rate_add | Recovery Rate | unit | additive | percent, good | combat |
| unit_supply_consumption_mult | Supply Consumption | unit | multiplicative | percent, bad | non-combat |

## References

1. ↑ Modifier type flow connections determined by BrokenRobot for the [Tiger validator](https://github.com/amtep/tiger)

---

- To update notes of defined modifier types, see [Module:Modifier type/Notes](https://vic3.paradoxwikis.com/Module:Modifier_type/Notes)
- To update the potential modifier types, see [Module:Modifier type/Potential](https://vic3.paradoxwikis.com/Module:Modifier_type/Potential)

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • Modifier types • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
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
