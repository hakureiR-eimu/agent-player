---
title: Country modding
source: https://vic3.paradoxwikis.com/Country_modding
pageid: 4805
categories: [Potentially_outdated, 1.10, Modding]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10.

Country definitions
**Game folder The folder where the files for this type are stored. :** `common/country_definitions`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**Related game objects:** Country creation, Country formation

[Countries](Countries.md) in Victoria 3 are defined by a small number of base characteristics, most of which are adjustable in-game by scripting or player action; however the base characteristics always remain as scripted.

## Country definition

Countries are defined in /common/country_definitions/; each country definition has required and optional elements:

| Characteristic | Use | Example | Required? |
|---|---|---|---|
| TAG | Internal script ID, always three letters, creates the definition block | GER | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| color | Base map color: in RGB, hsv, or hsv360 colorspace | color = { 147 130 110 } | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| country_type | Starting diplomatic type, defined in common/country_types | country_type = recognized | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| tier | Prestige tier, currently a hardcoded [list](Rank.md) | tier = empire | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| cultures | Primary cultures, one or more | cultures = { north_german south_german } | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| religion | State religion, if different from default religion of first primary culture | religion = protestant | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| capital | Default capital state, technically optional | capital = STATE_BRANDENBURG | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| is_named_from_capital | Overrides usual state naming mechanics for split states | is_named_from_capital = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| valid_as_home_country_for_separatists | Can separatists revolt for this country | valid_as_home_country_for_separatists = { triggers } | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| social_hierarchy | Sets a social hierarchy for use by this country | social_hierarchy = british_indian_caste_system | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| <order>_unit_color | Sets a consistent unit model color (in RGB); `primary, secondary, or tertiary` | primary_unit_color = { 20 20 120 } | ![No](/images/thumb/0/04/No.png/24px-No.png) |

A full definition typically appears similar to this example:

```
GER = {
	color = { 147 130 110 }
	
	country_type = recognized

	tier = empire
	
	cultures = { north_german south_german }
	capital = STATE_BRANDENBURG
}
```

More notes:

- `color` is assumed as rgb unless set as hsv or hsv360:
  - thus `color = { 147 130 110 }` is read as rgb (in 0-255 values)
  - while `color = hsv{ 0.99 0.7 0.9 }` uses percentage HSV
  - and `color = hsv360{ 20 80 80 }` uses 0-360 Hue and 0-100 Saturation and Value.
- Characteristics which can be changed by script – such as type, cultures, and religion – are reset to the defined values if the country ceases to exist during the game and then later is released or reformed.

### Country formation

Country formations
**Game folder The folder where the files for this type are stored. :** `common/country_formation`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**Related game objects:** Country creation, Country definitions

Country formations – i.e. [unifications](Formable countries.md) – are defined in /common/country_formation/. Each formation must be based on an already existing country definition. Formations are defined on two axes: major versus minor, and cultural homelands versus defined list of states.

All formations require a list of states, either explicitly defined or with `use_culture_states = yes` which uses all states with a homeland of any of the country's primary cultures as its list of states.

| Characteristic | Use | Example | Notes |
|---|---|---|---|
| TAG | Internal script ID, creates the definition block | LAO | Must match already defined country |
| states | A defined list of states, one or more | states = { STATE_LAOS } | Don't use along with `use_culture_states` |
| use_culture_states | All cultural homelands of the country's cultures are used | use_culture_states = yes | Don't use along with `states` |
| required_states_fraction | Percentage of states required for formation | required_states_fraction = 0.75 | Defaults to 0.75 if omitted |
| ai_will_do | Conditions for the AI to decide to form this country | ai_will_do = { triggers } | Vanilla mainly uses `always = yes` |
| possible | Additional requirements for formation | possible = { triggers } | Vanilla mainly uses `has_technology_researched = (pan-)nationalism` |
| max_num_formation_candidates | Overrides the default amount of formation candidates | max_num_formation_candidates = 1 | Default is 3 |
| can_be_formation_candidate | Additional requirements to be a candidate for a major formation | can_be_formation_candidate = { triggers } | candidates must also fulfill the possible block |
| can_be_unification_target | Additional requirements to be a valid target for unification plays | can_be_unification_target = { triggers } |  |

An example with a defined state list:

```
LAO = {
	states = {
		STATE_LAOS
	}

	required_states_fraction = 1.0
	
	ai_will_do = { always = yes }
}
```

An example with `use_culture_states = yes`

```
UBD = {
	use_culture_states = yes

	required_states_fraction = 1
	
	ai_will_do = { always = yes }

	possible = {
		has_technology_researched = pan-nationalism
	}
}
```

Major formations are declared by adding `is_major_formation = yes`. Major formations also have two diplomatic plays `unification_play` and `leadership_play` which should match existing [diplomatic plays](Diplomacy modding.md) with the wargoals of `unification` and `unification_leadership` respectively

An example of a major formation:

```
ITA = {
	use_culture_states = yes

	is_major_formation = yes

	unification_play = dp_unify_italy
	leadership_play = dp_leadership_italy

	required_states_fraction = 0.7

	ai_will_do = { has_technology_researched = nationalism }

	possible = {
		OR = {
			country_has_primary_culture = cu:north_italian
			country_has_primary_culture = cu:south_italian
		}
	}
	
	max_num_formation_candidates = 3
	can_be_formation_candidate = {
		country_rank >= rank_value:minor_power
		any_country = {
			filter = {
				OR = {
					country_has_primary_culture = cu:north_italian
					country_has_primary_culture = cu:south_italian
				}
			}
			has_technology_researched = nationalism
			percent = 1
		}
	}
}
```

Forming the country requires only the possible block, while the unification candidate mechanic requires both the possible block and the can_be_formation_candidate block.

### Country creation

Country creation
**Game folder The folder where the files for this type are stored. :** `common/country_creation`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**Related game objects:** Country definitions, Country formation

Country creations – i.e. [liberations](Releasable countries.md) – are defined in /common/country_creation/. Each creation must be based on an already existing country definition. Creations are defined by either cultural homelands, a defined list of states, or a defined list of provinces. Note that a country's defined capital is effectively always included in the list of required states or culture states, even if not explicitly added to the list or a cultural homeland.

| Characteristic | Use | Example | Notes |
|---|---|---|---|
| TAG | Internal script ID, creates the definition block | JAM | Must match already defined country |
| provinces | A defined list of provinces, one or more | provinces = { xC08061 x68BE66 } | Don't use along with `use_culture_states` or `states` The provinces do not need to belong to the same state |
| states | A defined list of states, one or more | states = { STATE_JAMAICA } | Don't use along with `use_culture_states` or `provinces` |
| use_culture_states | All cultural homelands of the country's cultures are used | use_culture_states = yes | Don't use along with `states` or `provinces` |
| required_num_states | Number of states required for release | required_num_states = 2 | Defaults to 0 (effectively 1) if omitted |
| ai_will_do | Conditions for the AI to decide to release this country | ai_will_do = { triggers } | Vanilla always uses `always = no` |
| possible | Additional requirements for release | possible = { triggers } | Vanilla mainly uses `has_technology_researched = (pan-)nationalism` |

An example of a country release definition

```
PHI = {
	states = { 
		STATE_MINDANAO
		STATE_LUZON
		STATE_VISAYAS
	}
	required_num_states = 2
	ai_will_do = { always = no }
}
```

## Localization

Dynamic country names
**Game folder The folder where the files for this type are stored. :** `common/dynamic_country_names`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

Countries automatically generate [localization](Localization.md) keys based on their tags: TAG and TAG_ADJ, which define the country's name and adjective.

Dynamic names can be defined in common/dynamic_country_names, with a `DEFAULT` block usable by any country and then TAG blocks specific to those tags

```
TAG = {
	dynamic_country_name = {
		name = string # This can be set to the default name by using TAG as the string
		adjective = string # This can be set to the default adjective by using TAG_ADJ as the string

		is_revolutionary = yes # default no, if yes then used for revolts only
        
		is_main_tag_only = yes # default no, if yes then only the primary country for a definition can use this name (ie Poland, not dynamic revolt Poland)
        
		priority = 0 # default 0, if multiple names have valid triggers, higher priority is used. If same priority, first one in file is used
		
		# Scripted trigger, country-scope
		trigger = {
		}
	}	
}
```

## Map color

Dynamic country colors
**Game folder The folder where the files for this type are stored. :** `common/dynamic_country_map_colors`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**Related game objects:** Named colors

A country's default map color is defined as above, but dynamic colors can be scripted in common/dynamic_country_map_colors. The first dynamic color which returns true is used, unless the [game rule](Game rule.md) *Map Color for Subjects* on and the country is a subject.

```
kalmar_union = { #This is just an arbitrary script name, should be unique for dynamic colors
	color = "kalmar_orange" # a "named color" defined in common/named_colors

	possible = { # Scripted trigger, country-scope
		exists = c:SCA
		THIS = c:SCA
		has_law = law_type:law_monarchy
		ruler = {
			has_culture = cu:danish
		}
	}
}
```

Named colors are defined in the same way as a country's default color, with a declared hsv360 or rgb color, except tied to a script name. Named colors can be used for dynamic map colors as well as flag colors.

## Flags

Main article:
Flag modding
Countries have flags dynamically generated if they do not have a defined flag; otherwise they use a defined flag as scripted.

### Flag colors and unit model colors

Unit models in game draw their colors from either the country's defined unit colors or from the currently used coat of arms' colors.

Unit model colors can be defined in a country's definition as:

```
    primary_unit_color = { 20 20 120 }
    secondary_unit_color  = { 150 190 210 }
    tertiary_unit_color = { 5 5 90 }
```

Otherwise, the first three base/pattern colors defined for a coat of arms determine the unit model colors, even if those colors don't appear on the flag. Colors defined for emblems are never considered.

## Country history

See also:
History modding
/common/history/countries/ contains the starting political set up for countries that exist at game start. These are effect blocks, with several effects set up as scripted effects to unify common sets of laws and technologies.

One of those effect blocks is `effect_starting_politics_conservative = yes` which gives the following laws:

| Monarchy | Interventionism | Censorship |
|---|---|---|
| Oligarchy | Mercantilism | No Workers' right |
| National Supremacy | Per-Capita Taxation | Child Labor Allowed |
| State Religion | Tenant farmers | Legal Guardianship |
| Appointed Bureaucrats | No Colonial Affairs | No social security |
| Professional Army | Local Police Force | Migration Controls |
| No Home Affairs | Religious Schools | Slavery Banned |
|  | No Health System | Combination Acts |

If no laws are defined for a group, the "default" law in each group is active at game start. These are generally the first law scripted in the law files, unless a country does not meet the requirements for that law.

**Technologies**

You can unlock an individual technology for a country, such as Sericulture, by writing `add_technology_researched = sericulture` in its country file. A technology tier is a group of technologies you can assign a country in a single line like `effect_starting_technology_tier_6_tech = yes` for ease of use. There are 6 tiers, and tier 5 contains tier 6, tier 4 contains tier 5, tier 3 contains tier 4, and so on. The following tables show the difference in technologies between consecutive tiers. Best practice is to assign a country a tier and then assign specific technologies which the assigned tier does not contain in a way that the technology tree stays connected.

| Production | Military | Society |
|---|---|---|
| Enclosure | Standing Army | Urbanization |

| Production | Military | Society |
|---|---|---|
| Manufacturies Shaft Mining | Navigation Military Drill | Rationalism Bureaucracy |

| Production | Military | Society |
|---|---|---|
| Prospecting Steelworking Distillation | Drydocks Admiralty Gunsmithing Artillery | International Trade Centralization International Relations Democracy |

| Production | Military | Society |
|---|---|---|
| Cotton Gin | Mandatory Service Line Infantry Army Reserves | Law Enforcement Currency Standards Colonization Academia Medical Degrees Romanticism |

| Production | Military | Society |
|---|---|---|
| Lathe Atmospheric Engine Mechanical Tools | Paddle Streamer Army Reserves Napoleonic Warfare | Stock Exchange Corporate Charters Banking Egalitarianism Mass Communication Empiricism Dialectics |

| Production | Military | Society |
|---|---|---|
| Railways | Screw Frigate Power of the Purse General Staff Percussion Cap | Central Banking Central Archives |

These preset scripted effects can be modified by defining other laws or additional technologies following the scripted effect call.

Other country starting circumstances are defined in the other history folders, such as diplomatic relations, owned states, and characters.

## Country script documentation

The following [effects](Effect.md), [event targets](Event target.md), and [triggers](Trigger.md) can be used in country scope.

| Effect | Description | Example | Targets |
|---|---|---|---|
| activate_law | Activates a law for a country, does not apply `when_enacted` effects | activate_law = law_type:<law_key> | law_type |
| activate_production_method | Activates the named production method for buildings of a certain type in country/state | activate_production_method = { building_type = building_key production_method = production_method_key } |  |
| add_banned_goods | Adds a total ban of a good to a country | add_banned_goods = <goods key/scope> | goods |
| add_change_relations_progress | Add progress towards changing relations between two countries | add_change_relations_progress = { country = country scope/tag value = amount } |  |
| add_company | Adds company type to a country's companies | add_company = company_type:key | company_type |
| add_country_monopoly | Adds a monopoly to a country scope | add_country_monopoly = bt:building_textile_mills | building_type |
| add_culture_acceptance_modifier | Apply a cultural acceptance modifier in the scoped country for the given culture. Other than the required culture argument, this effect has the same syntax as add_modifier. | add_culture_acceptance_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } |  |
| add_enactment_modifier | Adds an enactment-related timed modifier effect to object in scope | add_enactment_modifier = { name = modifier_key } |  |
| add_enactment_phase | Changes the current law enactment phase in scope country by an added amount. The result will be clamped between 0 and NPolitics::LAW_ENACTMENT_MAX_PHASES. The enacting law will pass if the resulting value equals NPolitics::LAW_ENACTMENT_MAX_PHASES. |  |  |
| add_enactment_setback | Changes the current law enactment setback count in scope country by an added amount. The result will be clamped between 0 and country_law_max_setbacks_add. The law enactment will fail if the resulting value equals country_law_max_setbacks_add |  |  |
| add_era_researched | Add specified era as researched in a country scope | add_era_researched = era |  |
| add_fervor_target_modifier | Apply a fervor target modifier in the scoped country for the given culture. Other than the required culture argument, this effect has the same syntax as add_modifier. | add_fervor_target_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } |  |
| add_investment_pool | Directly adds money to the investment pool | add_investment_pool = 50 |  |
| add_journal_entry | Adds a journal entry to a scoped country's journal, with optional saved scope target | add_journal_entry = { type = <key> target = <scope> } |  |
| add_law_progress | Adds x% progress to the current checkpoint of the law being passed (range is [0, 1], 0.1 means 10 percentage points) | add_law_progress = 0.1 / -0.1 |  |
| add_liberty_desire | Adds Liberty Desire to a Subject Country. Does nothing if the scoped country is not a subject in a Diplomatic Pact. | add_liberty_desire = -5 |  |
| add_loyalists | Adds loyalists to pops in the scoped country. All parameters except value are optional. | value is the percentage of each pop that will move towards loyalism. if interest_group is specified pops gain loyalists based on their ig membership. pop type and strata are mutually exclusive. add_radicals = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } |  |
| add_modifier | Adds a timed modifier effect to object in scope | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_primary_culture | Adds a culture to the primary cultures of a country | add_primary_culture = <culture> | culture |
| add_radicals | Adds radicals to pops in the scoped country. All parameters except value are optional. | value is the percentage of each pop that will move towards radicalism. if interest_group is specified pops gain radicals based on their ig membership. pop type and strata are mutually exclusive. add_radicals = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } |  |
| add_taxed_goods | Adds consumption taxes on a good to a country | add_taxed_goods = <goods key/scope> | goods |
| add_technology_progress | Add technology progress | add_technology_progress = { progress = <script_value> technology = <technology key> } |  |
| add_technology_researched | Research the specified technology in a country scope | add_technology_researched = technology |  |
| add_treasury | Add/remove money from a country | add_treasury = fixed point |  |
| annex | Annexes a country | annex = scope | country |
| annex_as_civil_war | Annexes a country with all the inheritance effects of a victorious side in a civil war | annex_as_civil_war = scope | country |
| annex_with_incorporation | Annexes a country, inheriting incorporation of their states | annex_with_incorporation = scope | country |
| call_election | Sets the next election date for country in N months | call_election = { months = 6 } |  |
| cancel_enactment | Stops enacting the country's currently enacting law | cancel_enactment = yes |  |
| change_infamy | Change infamy of scope country | change_infamy = amount |  |
| change_institution_investment_level | Add/remove the investment level for the institution | change_institution_investment_level = { institution = institution_police investment = -1 } |  |
| change_relations | Change relations between two countries | change_relations = { country = country scope/tag value = amount } |  |
| change_subject_type | Changes the subject type of the country in scope while retaining the current Liberty Desire value. | change_subject_type = subject_type_dominion |  |
| change_tag | Change the tag for the scoped country | c:GBR = { change_tag = FRA } |  |
| change_tension | Change tension between two countries | change_tension = { country = country scope/tag value = amount } |  |
| clear_debt | Clear country loans = bool |  |  |
| clear_enactment_modifier | Clears all current law enactment modifiers of scope country. |  |  |
| clear_scaled_debt | Clears an amount of debt equal to the defined multiplier on target's max credit | clear_scaled_debt = value |  |
| complete_objective_subgoal | Completes an objective subgoal | complete_objective_subgoal = <key> |  |
| copy_laws | Copies the constitution of the target country scope | Warning: This stops any current enactment. copy_laws = scope | country |
| create_bidirectional_truce | Create a bidirectional truce between two countries | create_bidirectional_truce = { country = country scope/tag months = integer } |  |
| create_character | Creates a character, any option can be omitted. | create_character = { name = loc_key or alternatively first_name and last_name separately culture = culture_tag religion = religion scope (if omitted, it's defined by the character's culture religion) female = bool or character scope (gets the same value from the character) noble = bool or character scope (gets the same value from the character) ruler = bool heir = bool historical = bool age = integer, range, or character scope (gets the age from a character) ideology = ideology key or scope interest_group = interest group key or scope template = base template to generate the character from on_created = effect save_scope_as = scope name trait_generation = effect hq = HQ scope or strategic region scope } |  |
| create_diplomatic_catalyst | Creates a new diplomatic catalyst | create_diplomatic_catalyst = { type = catalyst_relations_level_increased arget = <country scope> } |  |
| create_diplomatic_pact | Create a diplomatic pact between two countries, with scope country as initiator | create_diplomatic_pact = { country = country scope/tag first_state = state scope/tag second_state = state scope/tag type = diplomatic action type } |  |
| create_diplomatic_play | Create a diplomatic play with the scoped object as initiator add_initiator_backers, add_target_backers, and add_war_goal can be included as direct effects | create_diplomatic_play = { name = loc_key escalation = integer between 0 and 100 target_country = country scope/tag type = diplomatic play type annex_as_civil_war = yes/no add_initiator_backers = { list of country scopes/tags } add_target_backers = { list of country scopes/tags } add_war_goal = { holder = country scope/tag war_goal = <war goal key> target_state = <state scope> (if required) target_country = <country scope> (if required) target_region = <region scope> (if required) } } |  |
| create_incident | Creates a diplomatic incident that generates infamy, with target country as the victim | create_incident = { country = country scope/tag value = infamy amount } |  |
| create_military_formation | Creates a military formation | create_military_formation = { # Optional name name = name # type defaults to army type = army/fleet hq_region = sr:region_russia # Optional, overrides the automatic supply hub selection supply_hub = s:STATE_MOSCOW # Add as many combat_unit specifications as necessary combat_unit = { type = unit_type:combat_unit_type_irregular_infantry # service_type defaults to regular and conscript is not applicable for fleets service_type = regular/conscript state_region = s:STATE_MOSCOW count = 5 } # mobilization_options are not applicable for fleets mobilization_options = { mobilization_option:mobilization_option_basic_supplies mobilization_option:mobilization_option_truck_transport } } |  |
| create_political_lobby | Creates a new political lobby | create_political_lobby = { type = lobby_pro_country arget = <country scope> add_interest_group = <ig scope 1> add_interest_group = <ig scope 2> add_interest_group = <ig scope 3> } |  |
| create_political_movement | Creates a political movement of the specified type in the country, culture/religion optional | create_political_movement = { movement_type = x religion = <scope> (if relevant) culture = <scope> (if relevant) } |  |
| create_power_bloc | Creates a power bloc with the scoped object as leader | create_power_bloc = { name = loc_key map_color = { R G B } or hsv{ H S V } founding_date = yyyy.mm.dd, optional identity = power bloc identity key principle = power bloc principle key, can be repeated member = country scope, can be repeated } |  |
| create_ship | Creates a ship in a scoped country | create_ship = { type = ship_type:key # Type of ship to create fleet = scope:fleet # Fleet to assign the created ship to save_scope_as = scope_name # If specified, saves the created ship in the given scope name name = loc_key # Optional name for the ship } |  |
| create_unidirectional_truce | Create a unidirectional truce for one country towards another | create_unidirectional_truce = { country = country scope/tag months = integer } |  |
| deactivate_law | Deactivates a law for a country |  | law_type |
| deactivate_parties | Deactivates parties in scoped country. | deactivate_parties = yes |  |
| decrease_autonomy | Change a country's subject type to a less autonomus one | decrease_autonomy = yes |  |
| end_truce | Ends any truce betweeen two countries | end_truce = country_scope | country |
| every_active_law | Iterate through all active laws in a country | every_active_law = { limit = { <triggers> } #optional <effects> } | law |
| every_active_party | Iterate through all active political parties in a country | every_active_party = { limit = { <triggers> } #optional <effects> } | party |
| every_civil_war | Iterate through all civil wars related to the scoped country | every_civil_war = { limit = { <triggers> } #optional <effects> } | civil_war |
| every_cobelligerent_in_diplo_play | Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars) | every_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional <effects> } | country |
| every_cobelligerent_in_war | Iterate through all co-belligerents of scope country in all wars | every_cobelligerent_in_war = { limit = { <triggers> } #optional <effects> } | country |
| every_company | Iterate through all companies in a country | every_company = { limit = { <triggers> } #optional <effects> } | company |
| every_country_strategic_region | Iterate through all strategic regions containing states owned by the scoped country | every_country_strategic_region = { limit = { <triggers> } #optional <effects> } | strategic_region |
| every_diplomatic_catalyst | Iterate through all diplomatic catalysts in the recent memory of a country | every_diplomatic_catalyst = { limit = { <triggers> } #optional <effects> } | diplomatic_catalyst |
| every_diplomatically_relevant_country | Iterate through all diplomatically relevant countries of a country scope | every_diplomatically_relevant_country = { limit = { <triggers> } #optional <effects> } | country |
| every_direct_subject | Any country directly below current in hierarchy | every_direct_subject = { limit = { <triggers> } #optional <effects> } | country |
| every_enemy_in_diplo_play | Iterate through all enemies of scope country in all diplomatic plays (includes wars) | every_enemy_in_diplo_play = { limit = { <triggers> } #optional <effects> } | country |
| every_enemy_in_war | Iterate through all enemies of scope country in all wars | every_enemy_in_war = { limit = { <triggers> } #optional <effects> } | country |
| every_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | every_harvest_condition = { limit = { <triggers> } #optional <effects> } | harvest_condition |
| every_in_hierarchy | Any country in current hierarchy, including current | every_in_hierarchy = { limit = { <triggers> } #optional <effects> } | country |
| every_interest_group | Iterate through all interest groups in a country | every_interest_group = { limit = { <triggers> } #optional <effects> } | interest_group |
| every_law | Iterate through all laws in a country | every_law = { limit = { <triggers> } #optional <effects> } | law |
| every_military_formation | Iterate through all military formations currently present at input scope | every_military_formation = { limit = { <triggers> } #optional <effects> } | military_formation |
| every_neighbouring_state | Iterate through all states neighbouring current scope Note British spelling | every_neighbouring_state = { limit = { <triggers> } #optional <effects> } | state |
| every_overlord_or_above | Any country above current in hierarchy | every_overlord_or_above = { limit = { <triggers> } #optional <effects> } | country |
| every_political_lobby | Iterate through all political lobbies in a country or interest group | every_political_lobby = { limit = { <triggers> } #optional <effects> } | political_lobby |
| every_political_movement | Iterate through all political movements in a country | every_political_movement = { limit = { <triggers> } #optional <effects> } | political_movement |
| every_potential_party | Iterate through all potential political parties in a country | every_potential_party = { limit = { <triggers> } #optional <effects> } | party |
| every_primary_culture | Primary cultures of the scoped country or country definition | every_primary_culture = { limit = { <triggers> } #optional <effects> } | culture |
| every_rival_country | Any country that is being rivaled by the country in a scope | every_rival_country = { limit = { <triggers> } #optional <effects> } | country |
| every_rivaling_country | Any country that is rivaling the country in a scope | every_rivaling_country = { limit = { <triggers> } #optional <effects> } | country |
| every_scope_admiral | Iterate through all admirals in a: country, interest group, or military formation | every_scope_admiral = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_ally | Iterate through all allies to a: country | every_scope_ally = { limit = { <triggers> } #optional <effects> } | country |
| every_scope_army | Iterate through all armies currently present at input scope | every_scope_army = { limit = { <triggers> } #optional <effects> } | military_formation |
| every_scope_building | Iterate through all buildings in a: state, country | every_scope_building = { limit = { <triggers> } #optional <effects> } | building |
| every_scope_character | Iterate through all characters in a: country, interest group, or front | every_scope_character = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_culture | Iterate through all cultures in the scope | every_scope_culture = { limit = { <triggers> } #optional <effects> } | culture |
| every_scope_diplomatic_pact | Any diplomatic pact of the country in a scope | every_scope_diplomatic_pact = { limit = { <triggers> } #optional <effects> } | diplomatic_pact |
| every_scope_fleet | Iterate through all fleets currently present at input scope | every_scope_fleet = { limit = { <triggers> } #optional <effects> } | military_formation |
| every_scope_general | Iterate through all generals in a: country, interest group, front, or military formation | every_scope_general = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_held_interest_marker | Iterate through all interest markers held by a country | every_scope_held_interest_marker = { limit = { <triggers> } #optional <effects> } | interest_marker |
| every_scope_homeland_state | Iterate through all states that are a homeland for the scoped culture, or a homeland of any primary culture of the scoped country | every_scope_homeland_state = { limit = { <triggers> } #optional <effects> } | state |
| every_scope_interest_marker | Iterate through all interest markers in a: country, state_region, strategic region | every_scope_interest_marker = { limit = { <triggers> } #optional <effects> } | interest_marker |
| every_scope_politician | Iterate through all politicians in a: country or interest group | every_scope_politician = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_pop | Iterate through all pops in a: country, state, interest group, culture | every_scope_pop = { limit = { <triggers> } #optional <effects> } | pop |
| every_scope_ship | Iterate through all ships in a country or military formation | every_scope_ship = { limit = { <triggers> } #optional <effects> } | ship |
| every_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | every_scope_state = { limit = { <triggers> } #optional <effects> } | state |
| every_scope_strait | Iterate through all straits with a land endpoint in the scoped state or country | every_scope_strait = { limit = { <triggers> } #optional <effects> } | strait |
| every_scope_theater | Iterate through all theaters in a: country | every_scope_theater = { limit = { <triggers> } #optional <effects> } | theater |
| every_scope_treaty | Iterate through in force treaties binding the scoped country | every_scope_treaty = { limit = { <triggers> } #optional <effects> } | treaty |
| every_scope_violate_sovereignty_interested_parties | Iterate through all countries that would be interested if country in scope has their sovereignty violated | every_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional <effects> } | country |
| every_scope_violate_sovereignty_wars | Iterate through all relevant wars if target country had their sovereignty violated by scoped country | every_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional <effects> } | war |
| every_scope_war | Iterate through all wars related to the scope | every_scope_war = { limit = { <triggers> } #optional <effects> } | war |
| every_strategic_objective | Iterate through all Strategic Objective states from the scoped Country | every_strategic_objective = { limit = { <triggers> } #optional <effects> } | state |
| every_subject_of_subject | Any country below direct subjects in hierarchy | every_subject_of_subject = { limit = { <triggers> } #optional <effects> } | country |
| every_subject_or_below | Any country below current in hierarchy | every_subject_or_below = { limit = { <triggers> } #optional <effects> } | country |
| every_valid_mass_migration_culture | Lists for cultures in the scoped country that are valid for mass migration | every_valid_mass_migration_culture = { limit = { <triggers> } #optional <effects> } | culture |
| increase_autonomy | Change a country's subject type to a more autonomus one | increase_autonomy = yes |  |
| join_power_bloc | Scoped country joins the power bloc of the target scoped country | join_power_bloc = c:USA | country |
| kill_population | Kills a number of individuals in the population in the scoped country. | All parameters except percent are optional. Pop type and strata cannot be used at the same time. kill_population = { value = <integer value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } |  |
| kill_population_percent | Kills a percentage of the population in the scoped country. | All parameters except percent are optional. Pop type and strata cannot be used at the same time. kill_population_percent = { percent = <decimal value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } |  |
| liberate_slaves | Frees all slaves in the country/state | liberate_slaves = yes |  |
| liberate_slaves_in_incorporated_states | Frees all slaves in the country's incorporated states | liberate_slaves_in_incorporated_states = yes |  |
| liberate_slaves_in_unincorporated_states | Frees all slaves in the country's unincorporated states | liberate_slaves_in_unincorporated_states = yes |  |
| make_independent | Makes a country independent. | make_independent = bool |  |
| ordered_active_law | Iterate through all active laws in a country | ordered_active_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | law |
| ordered_active_party | Iterate through all active political parties in a country | ordered_active_party = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | party |
| ordered_civil_war | Iterate through all civil wars related to the scoped country | ordered_civil_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | civil_war |
| ordered_cobelligerent_in_diplo_play | Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars) | ordered_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_cobelligerent_in_war | Iterate through all co-belligerents of scope country in all wars | ordered_cobelligerent_in_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_company | Iterate through all companies in a country | ordered_company = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | company |
| ordered_country_strategic_region | Iterate through all strategic regions containing states owned by the scoped country | ordered_country_strategic_region = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | strategic_region |
| ordered_diplomatic_catalyst | Iterate through all diplomatic catalysts in the recent memory of a country | ordered_diplomatic_catalyst = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_catalyst |
| ordered_diplomatically_relevant_country | Iterate through all diplomatically relevant countries of a country scope | ordered_diplomatically_relevant_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_direct_subject | Any country directly below current in hierarchy | ordered_direct_subject = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_enemy_in_diplo_play | Iterate through all enemies of scope country in all diplomatic plays (includes wars) | ordered_enemy_in_diplo_play = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_enemy_in_war | Iterate through all enemies of scope country in all wars | ordered_enemy_in_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | ordered_harvest_condition = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | harvest_condition |
| ordered_in_hierarchy | Any country in current hierarchy, including current | ordered_in_hierarchy = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_interest_group | Iterate through all interest groups in a country | ordered_interest_group = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | interest_group |
| ordered_law | Iterate through all laws in a country | ordered_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | law |
| ordered_military_formation | Iterate through all military formations currently present at input scope | ordered_military_formation = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | military_formation |
| ordered_neighbouring_state | Iterate through all states neighbouring a state region | ordered_neighbouring_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_overlord_or_above | Any country above current in hierarchy | ordered_overlord_or_above = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_political_lobby | Iterate through all political lobbies in a country or interest group | ordered_political_lobby = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_lobby |
| ordered_political_movement | Iterate through all political movements in a country | ordered_political_movement = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_movement |
| ordered_potential_party | Iterate through all potential political parties in a country | ordered_potential_party = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | party |
| ordered_primary_culture | Primary cultures of the scoped country or country definition | ordered_primary_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | culture |
| ordered_rival_country | Any country that is being rivaled by the country in a scope | ordered_rival_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_rivaling_country | Any country that is rivaling the country in a scope | ordered_rivaling_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_scope_admiral | Iterate through all admirals in a: country, interest group, or military formation | ordered_scope_admiral = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_ally | Iterate through all allies to a: country | ordered_scope_ally = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_scope_army | Iterate through all armies currently present at input scope | ordered_scope_army = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | military_formation |
| ordered_scope_building | Iterate through all buildings in a: state, country | ordered_scope_building = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | building |
| ordered_scope_character | Iterate through all characters in a: country, interest group, or front | ordered_scope_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_culture | Iterate through all cultures in the scope | ordered_scope_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | culture |
| ordered_scope_diplomatic_pact | Any diplomatic pact of the country in a scope | ordered_scope_diplomatic_pact = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_pact |
| ordered_scope_fleet | Iterate through all fleets currently present at input scope | ordered_scope_fleet = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | military_formation |
| ordered_scope_general | Iterate through all generals in a: country, interest group, front, or military formation | ordered_scope_general = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_held_interest_marker | Iterate through all interest markers held by a country | ordered_scope_held_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | interest_marker |
| ordered_scope_homeland_state | Iterate through all states that are a homeland for the scoped culture, or a homeland of any primary culture of the scoped country | ordered_scope_homeland_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_scope_interest_marker | Iterate through all interest markers in a: country, state_region, strategic region | ordered_scope_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | interest_marker |
| ordered_scope_politician | Iterate through all politicians in a: country or interest group | ordered_scope_politician = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_pop | Iterate through all pops in a: country, state, interest group, culture | ordered_scope_pop = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | pop |
| ordered_scope_ship | Iterate through all ships in a country or military formation | ordered_scope_ship = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | ship |
| ordered_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | ordered_scope_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_scope_strait | Iterate through all straits with a land endpoint in the scoped state or country | ordered_scope_strait = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | strait |
| ordered_scope_theater | Iterate through all theaters in a: country | ordered_scope_theater = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | theater |
| ordered_scope_treaty | Iterate through in force treaties binding the scoped country | ordered_scope_treaty = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty |
| ordered_scope_violate_sovereignty_interested_parties | Iterate through all countries that would be interested if country in scope has their sovereignty violated | ordered_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_scope_violate_sovereignty_wars | Iterate through all relevant wars if target country had their sovereignty violated by scoped country | ordered_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | war |
| ordered_scope_war | Iterate through all wars related to the scope | ordered_scope_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | war |
| ordered_strategic_objective | Iterate through all Strategic Objective states from the scoped Country | ordered_strategic_objective = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_subject_of_subject | Any country below direct subjects in hierarchy | ordered_subject_of_subject = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_subject_or_below | Any country below current in hierarchy | ordered_subject_or_below = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_valid_mass_migration_culture | Lists for cultures in the scoped country that are valid for mass migration | ordered_valid_mass_migration_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | culture |
| play_as | Change which country scoped country's player will play as | play_as = <scope> | country |
| random_active_law | Iterate through all active laws in a country | random_active_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | law |
| random_active_party | Iterate through all active political parties in a country | random_active_party = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | party |
| random_civil_war | Iterate through all civil wars related to the scoped country | random_civil_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | civil_war |
| random_cobelligerent_in_diplo_play | Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars) | random_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_cobelligerent_in_war | Iterate through all co-belligerents of scope country in all wars | random_cobelligerent_in_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_company | Iterate through all companies in a country | random_company = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | company |
| random_country_strategic_region | Iterate through all strategic regions containing states owned by the scoped country | random_country_strategic_region = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | strategic_region |
| random_diplomatic_catalyst | Iterate through all diplomatic catalysts in the recent memory of a country | random_diplomatic_catalyst = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_catalyst |
| random_diplomatically_relevant_country | Iterate through all diplomatically relevant countries of a country scope | random_diplomatically_relevant_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_direct_subject | Any country directly below current in hierarchy | random_direct_subject = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_enemy_in_diplo_play | Iterate through all enemies of scope country in all diplomatic plays (includes wars) | random_enemy_in_diplo_play = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_enemy_in_war | Iterate through all enemies of scope country in all wars | random_enemy_in_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | random_harvest_condition = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | harvest_condition |
| random_in_hierarchy | Any country in current hierarchy, including current | random_in_hierarchy = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_interest_group | Iterate through all interest groups in a country | random_interest_group = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | interest_group |
| random_law | Iterate through all laws in a country | random_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | law |
| random_military_formation | Iterate through all military formations currently present at input scope | random_military_formation = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | military_formation |
| random_neighbouring_state | Iterate through all states neighbouring a state region | random_neighbouring_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| random_overlord_or_above | Any country above current in hierarchy | random_overlord_or_above = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_political_lobby | Iterate through all political lobbies in a country or interest group | random_political_lobby = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_lobby |
| random_political_movement | Iterate through all political movements in a country | random_political_movement = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_movement |
| random_potential_party | Iterate through all potential political parties in a country | random_potential_party = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | party |
| random_primary_culture | Primary cultures of the scoped country or country definition | random_primary_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | culture |
| random_rival_country | Any country that is being rivaled by the country in a scope | random_rival_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_rivaling_country | Any country that is rivaling the country in a scope | random_rivaling_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_scope_admiral | Iterate through all admirals in a: country, interest group, or military formation | random_scope_admiral = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character |
| random_scope_ally | Iterate through all allies to a: country | random_scope_ally = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_scope_army | Iterate through all armies currently present at input scope | random_scope_army = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | military_formation |
| random_scope_building | Iterate through all buildings in a: state, country | random_scope_building = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | building |
| random_scope_character | Iterate through all characters in a: country, interest group, or front | random_scope_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character |
| random_scope_culture | Iterate through all cultures in the scope | random_scope_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | culture |
| random_scope_diplomatic_pact | Any diplomatic pact of the country in a scope | random_scope_diplomatic_pact = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_pact |
| random_scope_fleet | Iterate through all fleets currently present at input scope | random_scope_fleet = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | military_formation |
| random_scope_general | Iterate through all generals in a: country, interest group, front, or military formation | random_scope_general = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character |
| random_scope_held_interest_marker | Iterate through all interest markers held by a country | random_scope_held_interest_marker = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | interest_marker |
| random_scope_homeland_state | Iterate through all states that are a homeland for the scoped culture, or a homeland of any primary culture of the scoped country | random_scope_homeland_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| random_scope_interest_marker | Iterate through all interest markers in a: country, state_region, strategic region | random_scope_interest_marker = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | interest_marker |
| random_scope_politician | Iterate through all politicians in a: country or interest group | random_scope_politician = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character |
| random_scope_pop | Iterate through all pops in a: country, state, interest group, culture | random_scope_pop = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | pop |
| random_scope_ship | Iterate through all ships in a country or military formation | random_scope_ship = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | ship |
| random_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | random_scope_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| random_scope_strait | Iterate through all straits with a land endpoint in the scoped state or country | random_scope_strait = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | strait |
| random_scope_theater | Iterate through all theaters in a: country | random_scope_theater = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | theater |
| random_scope_treaty | Iterate through in force treaties binding the scoped country | random_scope_treaty = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty |
| random_scope_violate_sovereignty_interested_parties | Iterate through all countries that would be interested if country in scope has their sovereignty violated | random_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_scope_violate_sovereignty_wars | Iterate through all relevant wars if target country had their sovereignty violated by scoped country | random_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | war |
| random_scope_war | Iterate through all wars related to the scope | random_scope_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | war |
| random_strategic_objective | Iterate through all Strategic Objective states from the scoped Country | random_strategic_objective = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| random_subject_of_subject | Any country below direct subjects in hierarchy | random_subject_of_subject = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_subject_or_below | Any country below current in hierarchy | random_subject_or_below = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_valid_mass_migration_culture | Lists for cultures in the scoped country that are valid for mass migration | random_valid_mass_migration_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | culture |
| recalculate_pop_ig_support | Recalculates and updates a country's pop IG memberships = bool |  |  |
| regime_change | Executes a regime change by the scope country in the target country. | regime_change = scope:upstart_country | country |
| remove_active_objective_subgoal | Removes an active objective subgoal | remove_active_objective_subgoal = <key> |  |
| remove_banned_goods | Removes a total ban of a good from a country | remove_banned_goods = <goods key/scope> | goods |
| remove_company | Removes company of specified type from a country's companies | remove_company = company_type:key | company_type |
| remove_diplomatic_pact | Removes a diplomatic pact between two countries, with scope country as initiator | remove_diplomatic_pact = { country = country scope/tag type = diplomatic action type } |  |
| remove_enactment_modifier | Removes an enactment-related timed modifier effect to object in scope |  |  |
| remove_modifier | Removes a timed modifier effect to object in scope | remove_modifier = static_modifier_name |  |
| remove_monopoly | removes a monopoly in a country scope for a specific building | remove_monopoly = bt:building_textile_mills | building_type |
| remove_primary_culture | Removes a culture from the primary cultures of a country | remove_primary_culture = <culture> | culture |
| remove_taxed_goods | Removes consumption taxes on a good from a country | remove_taxed_goods = <goods key/scope> | goods |
| seize_investment_pool | Seize investment pool for the treasury and transfer all private construction queue elements to the government queue = bool |  |  |
| set_capital | Set capital state in a country scope | set_capital = <state_region key> |  |
| set_country_type | Sets the type of country for a country, for history |  |  |
| set_diplomats_expelled | Expels diplomats from target country in scoped country | set_diplomats_expelled = scope:target_country | country |
| set_export_tariff_level | Sets export tariff level for a good in scoped country | set_export_tariff_level = { goods = g:iron level = max_tariffs } |  |
| set_government_wage_level | Sets the government wage level of scoped country | set_government_wage_level = very_low/low/medium/high/very_high |  |
| set_heir | Sets the heir of the scoped country to the character scope specified | set_heir = scope_victoria | character |
| set_immune_to_revolutions | Makes a country immune to revolutions or removes such immunity. | set_immune_to_revolutions = yes/no |  |
| set_import_tariff_level | Sets import tariff level for a good in scoped country | set_import_tariff_level = { goods = g:iron level = max_tariffs } |  |
| set_institution_investment_level | Sets the investment level for an institution | set_institution_investment_level = { institution = <key> level = x } |  |
| set_market_capital | Set market capital in a country scope | set_market_capital = <state_region key> |  |
| set_military_wage_level | Sets the military wage level of scoped country | set_military_wage_level = very_low/low/medium/high/very_high |  |
| set_mutual_secret_goal | Set mutual secret AI goal for scope country and target country | set_mutual_secret_goal = { country = country scope/tag secret_goal = secret goal type } |  |
| set_next_election_date | Set next election date for country | set_next_election_date = year.month.day |  |
| set_only_legal_party_from_ig | Sets the only party that is legal in a country, used for single-party state law. | set_only_legal_party_from_ig = ruler.interest_group | interest_group |
| set_owes_obligation_to | Set whether a country owes another a obligation | set_owes_obligation = { country = country scope/tag setting = yes/no } |  |
| set_relations | Set relations between two countries | set_relations = { country = country scope/tag value = amount } |  |
| set_ruling_interest_groups | Creates a government for the country in scope from a set of interest groups | set_ruling_interest_groups = { ig_tag1 ig_tag2 } |  |
| set_secret_goal | Set a secret AI goal for scope country towards another country | set_secret_goal = { country = country scope/tag secret_goal = secret goal type } |  |
| set_social_hierarchy | Sets the social hierarchy the scoped country | set_social_hierarchy = <key> |  |
| set_state_religion | Changes the state religion of the country to the specified religion | set_state_religion = <religion_scope | religion |
| set_strategy | Set AI strategy for scope country | set_strategy = <key> |  |
| set_tax_level | Sets the overall tax level of scoped country | set_tax_level = very_low/low/medium/high/very_high |  |
| set_tension | Set tension between two countries | set_tension = { country = country scope/tag value = amount } |  |
| start_enactment | Starts enacting the specified law type for the country in scope | start_enactment = law_type:law_multicultural | law_type |
| start_national_awakening | Starts a cultural awakening | start_national_awakening = { culture = cu:british # the culture that will have a national awakening months = 12 # the number of months the awakening will last for state_region = s:STATE_HOME_COUNTIES # optional, if not specified the state region with the highest literacy rate of the culture is used } |  |
| start_research_random_technology | Scoped country starts research of any random technology they can | start_research_random_technology = yes |  |
| take_on_scaled_debt | Transfers an amount of debt equal to the defined multiplier on target's max credit | take_on_scaled_debt = { who = <country scope> value = <0-1 value> } |  |
| try_form_government_with | Tries to form a new govt with provided IGs, If not possible with legitimacy provided will try and add as many IGs into the govt as possible | try_form_government_with = { value = 30 interest_group_type = ig_armed_forces interest_group_type = ig_devout interest_group_type = ig_landowners } |  |
| unset_only_legal_party | Returns the country to a non single-party state state, where multiple parties can exist if they are allowed by other laws | unset_only_legal_party = yes |  |
| update_party_support | Updates party support in scoped country. | update_party_support = yes |  |
| validate_subsidies | Validates subsidies across a country's buildings. No base game uses | validate_subsidies = bool |  |
| violate_sovereignty_join | Scope country joins war on side of violator or target | violate_sovereignty_accept = { violator = <country scope> target = <country scope> join_violator = yes/no } |  |

| Trigger | Description | Example | Targets |
|---|---|---|---|
| additional_war_exhaustion | Compares the additional war exhaustion the scoped country has accumulated from scripted events in the target diplomatic play | additional_war_exhaustion = { target = scope:war.diplomatic_play value > 1.0 } | value |
| aggressive_diplomatic_plays_permitted | True if country is independent or permitted to start their own Diplomatic Plays | aggressive_diplomatic_plays_permitted = bool | boolean |
| ai_ship_value | AI valuation of a ship in £, equal to the current template-version construction cost times NAI::SHIP_TRANSFER_BASE_VALUE_PER_CONSTRUCTION_POINT | ai_ship_value >= 5000 | value |
| any_active_law | Iterate through all active laws in a country | any_active_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | law |
| any_active_party | Iterate through all active political parties in a country | any_active_party = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | party |
| any_civil_war | Iterate through all civil wars related to the scoped country | any_civil_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | civil_war |
| any_cobelligerent_in_diplo_play | Iterate through all co-belligerents of scope country in all diplomatic plays (includes wars) | any_cobelligerent_in_diplo_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_cobelligerent_in_war | Iterate through all co-belligerents of scope country in all wars | any_cobelligerent_in_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_company | Iterate through all companies in a country | any_company = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | company |
| any_country_strategic_region | Iterate through all strategic regions containing states owned by the scoped country | any_country_strategic_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | strategic_region |
| any_diplomatic_catalyst | Iterate through all diplomatic catalysts in the recent memory of a country | any_diplomatic_catalyst = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_catalyst |
| any_diplomatically_relevant_country | Iterate through all diplomatically relevant countries of a country scope | any_diplomatically_relevant_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_direct_subject | Any country directly below current in hierarchy | any_direct_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_enemy_in_diplo_play | Iterate through all enemies of scope country in all diplomatic plays (includes wars) | any_enemy_in_diplo_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_enemy_in_war | Iterate through all enemies of scope country in all wars | any_enemy_in_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_harvest_condition | Iterate through all harvest conditions affecting a state, state region, strategic region, or country | any_harvest_condition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | harvest_condition |
| any_in_hierarchy | Any country in current hierarchy, including current | any_in_hierarchy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_interest_group | Iterate through all interest groups in a country | any_interest_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | interest_group |
| any_law | Iterate through all laws in a country | any_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | law |
| any_military_formation | Iterate through all military formations currently present at input scope | any_military_formation = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | military_formation |
| any_neighbouring_state | Iterate through all states neighbouring a state region | any_neighbouring_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| any_overlord_or_above | Any country above current in hierarchy | any_overlord_or_above = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_political_lobby | Iterate through all political lobbies in a country or interest group | any_political_lobby = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_lobby |
| any_political_movement | Iterate through all political movements in a country | any_political_movement = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_movement |
| any_potential_party | Iterate through all potential political parties in a country | any_potential_party = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | party |
| any_primary_culture | Primary cultures of the scoped country or country definition | any_primary_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | culture |
| any_rival_country | Any country that is being rivaled by the country in a scope | any_rival_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_rivaling_country | Any country that is rivaling the country in a scope | any_rivaling_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_scope_admiral | Iterate through all admirals in a: country, interest group, or military formation | any_scope_admiral = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_ally | Iterate through all allies to a: country | any_scope_ally = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_scope_army | Iterate through all armies currently present at input scope | any_scope_army = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | military_formation |
| any_scope_building | Iterate through all buildings in a: state, country | any_scope_building = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | building |
| any_scope_character | Iterate through all characters in a: country, interest group, or front | any_scope_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_culture | Iterate through all cultures in the scope | any_scope_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | culture |
| any_scope_diplomatic_pact | Any diplomatic pact of the country in a scope | any_scope_diplomatic_pact = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_pact |
| any_scope_fleet | Iterate through all fleets currently present at input scope | any_scope_fleet = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | military_formation |
| any_scope_general | Iterate through all generals in a: country, interest group, front, or military formation | any_scope_general = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_held_interest_marker | Iterate through all interest markers held by a country | any_scope_held_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | interest_marker |
| any_scope_homeland_state | Iterate through all states that are a homeland for the scoped culture, or a homeland of any primary culture of the scoped country | any_scope_homeland_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| any_scope_interest_marker | Iterate through all interest markers in a: country, strategic region | any_scope_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | interest_marker |
| any_scope_politician | Iterate through all politicians in a: country or interest group | any_scope_politician = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_pop | Iterate through all pops in a: country, state, interest group, culture | any_scope_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | pop |
| any_scope_ship | Iterate through all ships in a country or military formation | any_scope_ship = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | ship |
| any_scope_state | Iterate through all states including provinces from a: country, state_region, theater, front, or strait | any_scope_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| any_scope_strait | Iterate through all straits with a land endpoint in the scoped state or country | any_scope_strait = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | strait |
| any_scope_theater | Iterate through all theaters in a: country | any_scope_theater = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | theater |
| any_scope_treaty | Iterate through in force treaties binding the scoped country | any_scope_treaty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty |
| any_scope_violate_sovereignty_interested_parties | Iterate through all countries that would be interested if country in scope has their sovereignty violated | any_scope_violate_sovereignty_interested_parties = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_scope_violate_sovereignty_wars | Iterate through all relevant wars if target country had their sovereignty violated by scoped country | any_scope_violate_sovereignty_wars = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | war |
| any_scope_war | Iterate through all wars related to the scope | any_scope_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | war |
| any_strategic_objective | Iterate through all Strategic Objective states from the scoped Country | any_strategic_objective = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| any_subject_of_subject | Any country below direct subjects in hierarchy | any_subject_of_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_subject_or_below | Any country below current in hierarchy | any_subject_or_below = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_valid_mass_migration_culture | Lists for cultures in the scoped country that are valid for mass migration | any_valid_mass_migration_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | culture |
| approaching_bureaucracy_shortage | Check if Institutions in the country will incur a Bureaucracy shortage eventually |  | boolean |
| arable_land_country | Compare arable land in *all* states | arable_land_country > 10 | value |
| army_mobilization_option_fraction | Checks that a countries army has a certain percentage of units with a specific monbilization option | scope:country = { army_mobilization_option_fraction = { target = mobilization_option:key value >= 0.2 } } | value |
| army_power_projection | Compare to a country's total army power projection | scope:example_country = { army_power_projection < root.army_power_projection } | value |
| authority | Compares the available authority of the scoped country |  | value |
| authority_usage | Compares the consumed authority of the scoped country |  | value |
| average_country_infrastructure | Check average infrastructure in all states owned by scope country | average_country_infrastructure = 3 | value |
| average_incorporated_country_infrastructure | Check average infrastructure in incorporated states owned by the scope country | average_incorporated_country_infrastructure = 3 | value |
| average_sol_for_culture | Compares the average standard of living for the target culture in the country | average_sol_for_culture = { target = cu:polish value > 10 } | value |
| average_sol_for_primary_cultures | Compare average standard of living for primary cultures |  | value |
| average_sol_for_religion | Compares the average standard of living for the target religion in the country | average_sol_for_religion = { target = rel:catholic value > 10 } | value |
| average_sol_for_slaves | Compare average standard of living for enslaved pops |  | value |
| bureaucracy | Compares the available bureaucracy of the scoped country |  | value |
| bureaucracy_usage | Compares the consumed bureaucracy of the scoped country |  | value |
| can_afford_diplomatic_action | Checks if the country in scope can afford the Influence for the specified diplomatic action (pact or ongoing) | can_afford_diplomatic_action = { target = <country scope> type = <diplomatic action key> } |  |
| can_break_diplomatic_pact | Checks if there is a diplomatic pact of the specified type with target country that can be broken by scope country | can_break_diplomatic_pact = { target = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> } |  |
| can_create_diplomatic_pact | Checks if a diplomatic pact is valid to create with another country | can_create_diplomatic_pact = { target = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> } |  |
| can_decrease_autonomy | Check if a subject country is able to become a less autonomous subject type | can_increase_autonomy = yes | boolean |
| can_establish_company | Check if the country can establish a new company |  | boolean |
| can_form_nation | Check if the target country is able to potentially form a nation | can_form_nation = <tag> |  |
| can_have_as_subject | Checks if a country can have another country as a particular type of subject | can_have_as_subject = { who = <country scope> type = <subject type key> } |  |
| can_have_subjects | Check if the country is able to have subjects of its own |  | boolean |
| can_increase_autonomy | Check if a subject country is able to become a more autonomous subject type | can_increase_autonomy = yes | boolean |
| can_leave_power_bloc | Checks if the country in scope can leave its current Power Bloc (returns false if country is not in a Power Bloc) | can_leave_power_bloc = yes | boolean |
| can_lobbies_target | Checks if target country is a valid target for lobbies in the scoped country | can_lobbies_target = <target country scope> | country |
| can_own_autonomy_be_decreased | Check if scoped country can have it's autonomy decreased | can_own_autonomy_be_decreased = yes/no | boolean |
| can_research | True if a country can research an technology | can_research = technology |  |
| can_send_diplomatic_action | Checks if a diplomatic action is valid to send by scope country to target country | can_send_diplomatic_action = { target = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> } |  |
| can_take_on_scaled_debt | Checks if scoped country can take on a certain amount of scaled debt from another country | can_take_on_scaled_debt = { who = <country scope> value = <0-1 value> } |  |
| can_trigger_event | Check if country can trigger the specified event | can_trigger_event = key |  |
| check_area | Compares areas of object to another object |  |  |
| construction_queue_duration | Compares the maximum of all the very roughly approximated weeks remaining to finish the constructions in any queue | construction_queue_duration < 52 | value |
| construction_queue_government_duration | Compares the very roughly approximated weeks remaining to finish the constructions in the government queue | construction_queue_government_duration < 52 | value |
| construction_queue_num_queued_government_levels | Compares the number of government constructed building levels in the construction queue |  | value |
| construction_queue_num_queued_levels | Compares the number of building levels in the construction queue |  | value |
| construction_queue_num_queued_private_levels | Compares the number of privately constructed building levels in the construction queue |  | value |
| construction_queue_private_duration | Compares the very roughly approximated weeks remaining to finish the constructions in the private queue | construction_queue_private_duration < 52 | value |
| country_army_unit_type_fraction | Checks that a country has a certain percentage of a specific army unit type | scope:example_formation = { country_military_unit_type_fraction = { target = unit_type:key value >= 0.2 } } | value |
| country_average_cultural_acceptance | Compares the average acceptance of a culture that is present in a country against a value | country_average_cultural_acceptance = { target = cu:french value >= 50 } | value |
| country_average_religious_acceptance | Compares the average acceptance of a religion that is present in a country against a value | country_average_religious_acceptance = { target = rel:catholic value >= 50 } | value |
| country_can_have_mass_migration_to | Checks if the scoped country can have mass migration to target country | can_have_mass_migration_to = c:country | country |
| country_fervor_primary_culture | Compares with the hightest fervor of a country's primary cultures | country_fervor_primary_culture > 0.2 | value |
| country_has_building_group_levels | Checks the sum of building levels for a building group in a country | country_has_building_group_levels = { type = bg_heavy_industry value >= 100 } | value |
| country_has_building_levels | Checks the sum of building levels for a country | country_has_building_levels >= 10 | value |
| country_has_building_type_levels | Checks the sum of building levels for a building type in a country | country_has_building_type_levels = { target = bt:building_barracks value >= 100 } | value |
| country_has_building_type_monopoly | Check if the scoped country has a monopoly of the specified building type | country_has_building_type_monopoly = bt:building_food_industry | building_type |
| country_has_country_monopoly | Check if the scoped country has any country monopolies |  | boolean |
| country_has_primary_culture | Checks if a culture is one of the primary cultures in the country | country_has_primary_culture = <culture> | culture |
| country_has_state_religion | Checks if a religion is the state religion in the country | country_has_accepted_religion = <religion> | religion |
| country_innovation | Checks the amount of weekly innovation a country produces | country_innovation <= 200 | value |
| country_or_subject_owns_entire_state_region | Checks whether the scoped country or any of its subjects owns the entire specified state region | country_or_subject_owns_entire_state_region = key |  |
| country_rank | Compares a Country's Power Ranking | country_rank < rank_value:major_power | value |
| country_ship_type_fraction | Checks that a country has a certain percentage of a specific ship type | scope:example_formation = { country_ship_type_fraction = { target = unit_type:key value >= 0.2 } } | value |
| country_tier | Compare tier of country tag | country_tier = x |  |
| country_turmoil | Compares the country's population weighted turmoil | country_turmoil > 0.2 | value |
| cultural_acceptance_base | Compares the acceptance from shared cultural traits of a culture in the scoped country against an acceptence value | cultural_acceptance_base = { target = cu:french value > 50 } | value |
| culture_percent_country | Checks that a country's population has a certain percentage of a specific culture | scope:example_country = { culture_percent_country = { target = cu:dixie value >= 0.2 } } | value |
| discriminates_religion | Checks if the scoped country discriminates the given religion (key) | discriminates_religion = <religion key/scope> | religion |
| economic_dependence | Compares the degree of dependence the country in scope has to the target country. **Note: This is an expensive trigger** | economic_dependence = { target = scope:other_country value > 2.2 } | value |
| empty_agitator_slots | Checks number of empty agitator slots in a country | empty_agitator_slots >= 1 | value |
| enacting_any_law | Checks if the country is enacting any law. | enacting_any_law = bool | boolean |
| enactment_chance | Compares the current enactment chance in scope country, including values from enactment modifiers |  | value |
| enactment_chance_for_law | Compares the enactment chance in scope country for given law, including values from enactment modifiers | enactment_chance_for_law = { target = scope:my_lawtype value > 0.2 } | value |
| enactment_chance_for_law_without_enactment_modifier | Compares the enactment chance in scope country for given law, excluding values from enactment modifiers | enactment_chance_for_law_without_enactment_modifier = { target = scope:my_lawtype value > 0.2 } | value |
| enactment_chance_without_enactment_modifier | Compares the current enactment chance in scope country, excluding values from enactment modifiers |  | value |
| enactment_phase | Compares the current law enactment phase in scope country. |  | value |
| enactment_setback_count | Compares the current enactment setback count in scope country. |  | value |
| enemy_contested_wargoals | Determines the fraction of wargoals that enemies in the war are currently contesting | enemy_contested_wargoals = { target = scope:war value > 0.4 } | value |
| enemy_occupation | Determines the (weighted) enemy occupation score of a country | enemy_occupation > 0.2 | value |
| expanding_institution | Checks if the institution is expanding | expanding_institution = <scope/key> |  |
| gdp_ownership_ratio | Compares the ratio of GDP the specified country owns in the scoped country | gdp_ownership_ratio = { target = scope:owner_country value > 0.1 } | value |
| gdp_per_capita_ranking | Compares a Country's GDP per Capita Ranking (position) | gdp_per_capita_ranking > 42 | value |
| global_country_ranking | Compares a Country's Power Ranking (position) | global_country_ranking > 42 | value |
| gold_reserves | Does the country have the required gold reserves | gold_reserves > 500 | value |
| gold_reserves_limit | Compares the country's gold reserves limit | gold_reserves > gold_reserves_limit | value |
| goods_production_rank | Compare to a country's production leaderboard rank of a good | "goods_production_rank(g:luxury_clothes)" < 10 | value |
| government_legitimacy | Compare Legitimacy |  | value |
| government_transfer_of_power | Checks country's government's transfer of power | government_transfer_of_power = key | value |
| government_wage_level | Compares the government wage level of scoped country. `very_low, low, medium, high, very_high`; returns same number as government_wage_level_value trigger | government_wage_level = <level_term> | value |
| government_wage_level_value | Compares the government wage level value of scoped country. `0, 1, 2, 3, 4` | government_wage_level_value = <level_num> | value |
| has_active_peace_deal | True if the country is in a war where there is a proposed peace deal | has_active_peace_deal = bool | boolean |
| has_any_law_commitment | Checks if a country has a commitment to enact any law | has_any_law_commitment = yes | boolean |
| has_any_naval_only_hostilities | Check if the country has naval hostilities with any country it is not also at war with | has_any_naval_only_hostilities = yes | boolean |
| has_any_secessionists_broken_out | Check if the country has secessionists broken out |  | boolean |
| has_any_secessionists_growing | Check if the country has any secessionists growing |  | boolean |
| has_any_strait_control | Check if the scoped country owns a strait province with naval fortification | has_any_strait_control = yes | boolean |
| has_any_strait_province | Check if the scoped country owns any strait province | has_any_strait_province = yes | boolean |
| has_any_subventions_on | Check if the scoped country has any level of subventions on a goods | scope:country = { has_any_subventions_on = <goods scope> } | goods |
| has_any_tariffs_on | Check if the scoped country has any level of tariffs on a goods | scope:country = { has_any_tariffs_on = <goods scope> } | goods |
| has_attitude | Checks if scoped country has a particular attitude towards another country | has_attitude = { who = <country scope> attitude = <attitude key> } |  |
| has_building | True if a state/market/state region/country has a building type | has_building = building |  |
| has_civil_war_from_movement_type | Checks if a country is having a civil war started by a particular movement type | has_civil_war_from_movement_type = <political_movement_type scope> | political_movement_type |
| has_claim | Checks if country in scope has a claim on state/state region/country | has_claim = <scope> |  |
| has_company | Checks if a company of the specified type exists in scope country | has_company = <company_type scope> | company_type |
| has_completed_subgoal | Checks if the scoped country has completed a certain subgoal | has_completed_subgoal = subgoal_key |  |
| has_consumption_tax | Checks if the country is taxing the target good. | c:FRA = { has_consumption_tax = <goods scope> } | goods |
| has_convoys_being_sunk | Check if the country has convoys being sunk through convoy raiding |  | boolean |
| has_diplomatic_pact | Checks if two countries have an active diplomatic pact of type | has_diplomatic_pact = { who = <country scope> type = <diplomatic action key> is_initiator = yes/no } is_initiator is optional parameter that checks to see if scope country is the original initiator/target of the pact |  |
| has_diplomatic_relevance | Checks if target country is diplomatically relevant for scope country | has_diplomatic_relevance = <scope> | country |
| has_diplomats_expelled | Checks if country in scope has recently expelled diplomats of event target | has_diplomats_expelled = country | country |
| has_famine | Check if state or country has famine | has_famine = yes/no | boolean |
| has_free_government_reform | Check if the country has a free (of radicals) government reform | has_free_government_reform = <yes/no> | boolean |
| has_global_highest_gdp | Checks if the scoped country has the highest GDP | has_global_highest_gdp = yes/no | boolean |
| has_global_highest_innovation | Checks if the scoped country has the highest weekly innovation | has_global_highest_innovation = yes/no | boolean |
| has_government_clout | Does the country's government have the necessary total Clout |  | value |
| has_government_type | Is the country's government type as specified | has_government_type = key |  |
| has_healthy_economy | Check if the country has a healthy economy |  | boolean |
| has_inactive_journal_entry | Check if the country has at least one inactive journal entry of the specified type | has_inactive_journal_entry = key |  |
| has_institution | Checks if scope country has a particular type of institution | has_institution = <scope/key> |  |
| has_insurrectionary_interest_groups | Check if the country has Interest Groups that are insurrectionary |  | boolean |
| has_interest_marker_in_region | True if scope country has an interest marker in target region | has_interest_marker_in_region = region scope/tag |  |
| has_journal_entry | Check if the country has at least one active journal entry of the specified type | has_journal_entry = key |  |
| has_law | Checks if a country has a certain law active |  | law_type |
| has_law_commitment | Checks if a country has a commitment to enact a certain law |  | law_type |
| has_law_imposition_rights | Checks if the scoped country has the necessary permits to demand another country enacts a certain law | has_law_imposition_rights = { target_country = <country scope> type = <law type scope> } |  |
| has_law_or_variant | Checks if a country has a certain law or one its variant laws active |  | law_type |
| has_modifier | Check if a supported scope has a certain timed modifier | has_modifier = <key> |  |
| has_objective | Checks if the scoped country has a certain objective type | has_objective = objective_type_key |  |
| has_overlapping_interests | Checks if country in scope has an overlapping interest marker with any of target country's interests | has_overlapping_interests = <scope> | country |
| has_port_country | Check if scoped country has at least one port | has_port_country = yes/no | boolean |
| has_possible_decisions | Check if a country has any possible Decisions | has_possible_decisions = yes | boolean |
| has_potential_to_form_country | Check if the target country could ever be able to form a nation | has_potential_to_form_country = <tag> |  |
| has_power_struggle | Checks if scope Power Bloc has a power struggle | has_power_struggle = yes/no | boolean |
| has_region_stance | Checks if the scoped country's AI has the specified stance for a strategic region | region_stance = { region = sr:some_region stance = <conquer_region> } |  |
| has_researchable_technology | Check if the country has any researchable technology left. |  | boolean |
| has_revolution | Check if the country has revolutionary uprising |  | boolean |
| has_ruling_interest_group | Does the country's government include the named IG |  |  |
| has_ruling_interest_group_count | Does the country's government consist of the specified number of IGs |  | value |
| has_secret_goal | Checks if scoped country has a particular secret goal towards another country | has_secret_goal = { who = <country scope> secret_goal = <secret_goal key> } |  |
| has_social_hierarchy | Checks if the scoped country has adopted a specific social hierarchy | has_social_hierarchy = <key> |  |
| has_state_in_state_region | Check if country has a state in the state region | has_state_in_state_region = key |  |
| has_strategic_adjacency | Checks if country in scope has a strategic adjacency (direct/coastal/wargoal adjacency) to target state/country | has_strategic_adjacency = <scope> |  |
| has_strategic_land_adjacency | Checks if country in scope has a strategic adjacency (direct land border or wargoal adjacency only) to target state/country | has_strategic_adjacency = <scope> |  |
| has_strategic_region_interest_tier | Checks the scoped country's interest tier rank in a specific strategic region | has_strategic_region_interest_tier = { strategic_region = sr:target_region value >= 3 } |  |
| has_strategy | Checks if country in scope has a particular AI strategy | has_strategy = <key> |  |
| has_subject_relation_with | Checks if country in scope is subject or overlord of event target | has_subject_relation_with = country | country |
| has_sufficient_construction_capacity_for_investment | Check if country has enough construction capacity to be spending all of its incoming investment pool funds. |  | boolean |
| has_technology_progress | Does the country have the required progress for an technology | has_technology_progress = { technology = <technology key> progress = <0-1 value> } | value |
| has_technology_researched | True if a country has researched an technology | has_technology_researched = <scope/key> |  |
| has_treaty_port_in_market | Checks if the scoped country has a treaty port in target market | c:POR = { has_treaty_port_in_market = c:CHI.market } | market |
| has_truce_with | Check if a country has a truce with a different target country | has_truce_with = c:GBR | country |
| has_war_with | Checks if country in scope is at war with event target | has_war_with = country | country |
| has_wasted_construction | Check if country is wasting any of its produced construction. |  | boolean |
| highest_overlapping_interest_tier | Compares the highest interest tier rank (scope country) among strategic regions where both countries have an interest. | highest_overlapping_interest_tier = { target = c:GBR value >= 2 } | value |
| highest_secession_progress | Compares the highest secession progress of any secession movement in a given country | highest_secession_progress > 0.7 | value |
| in_default | Check if the country is currently in default |  | boolean |
| in_election_campaign | Check if the country is in election campaign period | in_election_campaign = <yes/no> | boolean |
| influence | Compares the available influence of the scoped country |  | value |
| influence_usage | Compares the consumed influence of the scoped country |  | value |
| institution_investment_level | Compares the level of investment in an institution | institution_investment_level = { institution = <key> value = <comparator value> } | value |
| investment_pool | Does the country have this amount of money saved in its investment pool | investment_pool > 1000 | value |
| investment_pool_gross_income | Does the country have this amount of gross income (income before expenses) for its investment pool | investment_pool_gross_income > 1000 | value |
| investment_pool_net_income | Does the country have this amount of net income (income after expenses) for its investment pool | investment_pool_net_income > 1000 | value |
| is_adjacent_to_country | Checks if country in scope is adjacent to a target country | is_adjacent_to_country = <scope> | country |
| is_adjacent_to_state | Checks if country in scope is adjacent to a target state | is_adjacent_to_state = <state scope> | state |
| is_ai | True if country scope is controlled by an AI | is_ai = bool | boolean |
| is_at_war | Check if the country is at war |  | boolean |
| is_banning_goods | Check if a country is banning a good | is_banning_goods = <goods key/scope> |  |
| is_considered_adjacent_due_to_wargoals | Checks if the scoped country is considered adjacent to the target country by virtue of the scoped country having war goals that are adjacent to the target country in a committed diplomatic play | is_considered_adjacent_due_to_wargoals = <target country scope> | country |
| is_construction_paused | Check if construction in a state is paused. |  | boolean |
| is_country_alive | Checks if the scoped country is alive, i.e. if it has at least one state on the map and can be interacted with | is_country_alive = yes/no | boolean |
| is_country_type | Checks the countrys type | is_country_type = country type |  |
| is_diplomatic_play_ally_of | Checks if country in scope is in a diplomatic play together with event target | is_diplomatic_play_ally_of = country | country |
| is_diplomatic_play_committed_participant | True if country is a committed participant of any diplomatic play | is_diplomatic_play_participant = bool | boolean |
| is_diplomatic_play_enemy_of | Checks if country in scope is in a diplomatic play against event target | is_diplomatic_play_enemy_of = country | country |
| is_diplomatic_play_initiator | True if country is the initiator of any diplomatic play | is_diplomatic_play_initiator = bool | boolean |
| is_diplomatic_play_involved_with | Checks if country in scope is involved in the same diplomatic play as event target | is_diplomatic_play_involved_with = country | country |
| is_diplomatic_play_participant_with | Checks if country in scope is a committed participant in the same diplomatic play as event target | is_diplomatic_play_participant_with = country | country |
| is_diplomatic_play_target | True if country is the target of any diplomatic play | is_diplomatic_play_target = bool | boolean |
| is_diplomatic_play_undecided_participant | True if country is a undecided participant of any diplomatic play | is_diplomatic_play_participant = bool | boolean |
| is_direct_subject_of | Checks if country in scope is a direct subject (not subject-of-subject) of event target | is_direct_subject_of = country | country |
| is_enacting_law | Checks if the scoped country is enacting a specific law type. | is_enacting_law = law_type:law_conscription | law_type |
| is_expanding_institution | Are you expanding an institution | is_expanding_institution = <yes>/<no> | boolean |
| is_forced_to_join_plays | Checks if the scoped country is forced to join the target country's Diplomatic Plays | is_forced_to_join_plays = c:country | country |
| is_home_country_for | Checks if a country is the home country for target country |  | country |
| is_immune_to_revolutions | Checks if the country has been set to be immune to revolutions via set_immune_to_revolutions | Warning: This does not check if the country is naturally immune to revolutions due to for example being a revolutionary country itself, only for the effects of set_immune_to_revolutions. is_immune_to_revolutions = yes/no | boolean |
| is_in_customs_union | Check if the country is part of a customs union |  | boolean |
| is_in_customs_union_with | Check if the country is in a customs union with scoped country | is_in_customs_union_with = c:FRA | country |
| is_in_power_bloc | Checks if the country is in a Power Bloc | is_in_power_bloc = yes/no | boolean |
| is_in_same_power_bloc | Checks if the scoped country is in the same power bloc as the target scoped country | is_in_same_power_bloc = c:GBR | country |
| is_in_war_together | Checks if country in scope is in war on the same side as event target | is_in_war_together = country | country |
| is_indirect_subject_of | Checks if country in scope is an indirect subject (subject-of-subject) of event target | is_indirect_subject_of = country | country |
| is_insurrectionary | Check if country, movement or IG is insurrectionary |  | boolean |
| is_junior_in_customs_union | True if country is a junior country in a customs custom | is_junior_in_customs_union = bool | boolean |
| is_local_player | True if country scope is a player | is_local_player = bool | boolean |
| is_losing_power_rank | Check if the country is in the process of dropping in power ranking |  | boolean |
| is_market_reachable_for_trade | Check if the scope country can reach the specified market scope for purposes of trade | is_market_reachable_for_trade = scope:my_market_scope | market |
| is_mass_migration_origin | Checks if the scoped country is the origin of mass migration | is_mass_migration_origin = yes | boolean |
| is_mass_migration_origin_of_culture | Checks if the scoped country origin of mass migration of specific culture | is_mass_migration_origin_of_culture = cu:example_culture | culture |
| is_owed_obligation_by | Checks if the scoped country is owed a obligation by the target country | is_owed_obligation_by = c:FRA | country |
| is_player | True if country scope is a player | is_player = bool | boolean |
| is_power_bloc_leader | Checks if the country is a leader of a Power Bloc | is_power_bloc_leader = yes/no | boolean |
| is_researching_technology | Check if the country is actively researching a tech | is_researching_technology = <scope/key/any> |  |
| is_researching_technology_category | Check if the country is actively researching a tech category | is_researching_technology_category = <key/any> |  |
| is_revolutionary | Check if the country, movement or interest group is revolutionary |  | boolean |
| is_secessionist | Check if the country, movement or interest group is secessionist |  | boolean |
| is_subject | True if country is a subject | is_subject = bool | boolean |
| is_subject_of | Checks if country in scope is subject (or subject-of-subject) of event target | is_subject_of = country | country |
| is_subject_type | Checks the country's subject type | is_subject_type = subject type |  |
| is_supporting_unification_candidate | Check if scope country is supporting a unification candidate for a specific country formation | is_supporting_unification_candidate = { who = c:PRU country_formation = GER } |  |
| is_taxing_goods | Check if a country is taxing a good | has_embargo = <goods key/scope> |  |
| is_unification_candidate | Check if scope country is a unification candidate for country tag | is_unification_candidate = GER |  |
| is_violating_sovereignty_of | Check if the scoped country is violating the sovereignty of a target country | is_violating_sovereignty_of = c:GBR | country |
| isolated_states | Compare number of Isolated States |  | value |
| leading_producer_of | Checks if country is producing the most of a certain good | leading_producer_of = g:luxury_clothes | goods |
| leads_customs_union | Check if any other country is part of this country's customs union | leads_customs_union = bool | boolean |
| liberty_desire | Compare trigger for the Liberty Desire value in a scoped country. | liberty_desire > 50 | value |
| liberty_desire_weekly_progress | Compare trigger for the weekly Liberty Desire progress value in a scoped country. | liberty_desire_weekly_progress > 0 | value |
| liberty_desire_weekly_progress_from_support_independence | Compare trigger for the weekly Liberty Desire progress value from the scoped country having their independence supported. | liberty_desire_weekly_progress_from_support_independence > 0 | value |
| literacy_rate | Checks if a pop, state or country has a certain amount of literacy | literacy = value | value |
| loyalist_fraction | Compares loyalist fraction in pops in state or country, all parameters except value are optional | loyalist_fraction = { value = <script_value> pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> } | value |
| max_law_enactment_setbacks | Compares to the max number of law enactment setbacks a country can suffer before the law fails |  | value |
| max_num_companies | The limit of how many companies the scoped country is allowed to have | num_num_companies > 0 | value |
| military_ship_maintenance_fulfillment | Compares the military ship maintenance fulfillment ratio of a country | military_ship_maintenance_fulfillment = <value> | value |
| military_wage_level | Compares the military wage level of scoped country. `very_low, low, medium, high, very_high`; returns same number as military_wage_level_value trigger | military_wage_level = <level_term> | value |
| military_wage_level_value | Compares the military wage level value of scoped country. `0, 1, 2, 3, 4` | military_wage_level_value = <level_num> | value |
| nationalization_cost | Compares the total cost of nationalizing all buildings in scope country owned by the government or pops of target country | nationalization_cost = { target = scope:other_country value > 100000 } | value |
| naval_power_projection | Compare to a country's total navy power projection | scope:example_country = { naval_power_projection < root.naval_power_projection } | value |
| neighbors_any_power_bloc | Checks if the scoped country neighbors any power bloc. Note: the scoped country is not considered to be neighboring the power bloc it belongs to (if any) | neighbors_any_power_bloc = yes/no | boolean |
| neighbors_member_of_same_power_bloc | Checks if the scoped country neighbors any other country belonging to the same power bloc | neighbors_member_of_same_power_bloc = yes/no | boolean |
| neighbors_power_bloc | Checks if the scoped country neighbors the target power bloc. Note: the scoped country is not considered to be neighboring the power bloc it belongs to (if any) | neighbors_power_bloc = c:PRU.power_bloc | power_bloc |
| num_companies | How many companies the scoped country has | num_companies > 0 | value |
| num_diplomatic_pacts | Compare to a country's number of diplomatic pacts of the specified type | num_diplomatic_pacts = { type = <key> value < 10 } | value |
| num_investments_of_type | Checks the number of buildings levels of a given type the scoped country has outside their own country. | num_investments_of_type = { type = building_oil_rig value > 5 } | value |
| num_political_lobbies | Compare to number of political lobbies in scoped country or interest group | num_political_lobbies > 0 | value |
| num_subjects | Compares the number of subjects of scoped country | num_subjects = <value> | value |
| num_taxed_goods | Compares the number of consumption taxed goods of scoped country | num_taxed_goods = <value> | value |
| number_of_claims | The number of claims on foreign states the country has | number_of_claims > 0 | value |
| number_of_possible_decisions | The number of possible decisions a Country can take | number_of_possible_decisions > 0 | value |
| overlord_can_decrease_subject_autonomy | Check if an overlord can decrease a subject autonomy | overlord_can_decrease_subject_autonomy = bool | boolean |
| owes_obligation_to | Checks if country in scope owes a obligation to event target | owes_obligation_to = country | country |
| owns_entire_state_region | Check if country owns entire region | owns_entire_state_region = key |  |
| owns_treaty_port_in | Does country own the treaty port in assigned state region | owns_treaty_port_in = key |  |
| play_participant_has_war_goal_of_type_against | Checks if scope country holds a wargoal of a specific type targeting a specific country in any diplomatic play | play_participant_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } |  |
| play_side_has_war_goal_of_type_against | Checks if any country on the same side as scope country in any diplomatic play holds a wargoal of a specific type targeting a specific country | play_side_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } |  |
| political_strength_share | Checks the political strength share of a pop type, religion or culture in a country or state. Exactly one of pop_type, religion or culture must be specified. | political_strength_share = { pop_type/religion/culture = <key/scope> value <compare operator> <value> } | value |
| politically_involved_ratio | Compares the percentage of politically involved population in a country | politically_involved_ratio > 0.25 | value |
| pop_type_percent_country | Checks whether the scoped country has <percent> of its population belonging to the specified pop type | scope:example_country = { pop_type_percent_country = { pop_type = <pop_type> percent <compare operator (<,>,= and so on)> <percent> } } | value |
| potential_diplomatic_play_power_ratio | Check the expected power ratio between scope country side and target country side in a potential diplomatic play | Attempts to predict which sides involved participants will take (if any) so doesn't just check 'starting strengths' potential_diplomatic_play_power_ratio = { type = dp_open_market target = c:BEL state = c:BEL.capital value > 1.0 } state and type are optional, will default to dp_open_market on target capital | value |
| potential_income | Compare the potential income of the country (weekly income plus tax waste) | potential_income > 1000 | value |
| power_bloc_share_gdp | Compare the share of GDP of the country in scope against all its Power Bloc current members, returns -1 if not in a Power Bloc | power_bloc_share_gdp > 0.2 | value |
| power_bloc_share_gdp_with | Compare the share of GDP of the country in scope against all its Power Bloc members plus an additional country, returns -1 if not in a Power Bloc | "power_bloc_share_gdp_with(scope:country) > 0.2" | value |
| power_bloc_share_gdp_without | Compare the share of GDP of the country in scope against all its Power Bloc members minus one of the members, returns -1 if not in a Power Bloc | "power_bloc_share_gdp_without(scope:country) > 0.2" | value |
| power_bloc_share_power_projection | Compare the share of Power Projection of the country in scope against all its Power Bloc members, returns -1 if not in a Power Bloc | power_bloc_share_power_projection > 0.2 | value |
| power_bloc_share_power_projection_with | Compare the share of Power Projection of the country in scope against all its Power Bloc members plus an additional country, returns -1 if not in a Power Bloc | "power_bloc_share_power_projection_with(scope:country) > 0.2" | value |
| power_bloc_share_power_projection_without | Compare the share of Power Projection of the country in scope against all its Power Bloc members minus one of the members, returns -1 if not in a Power Bloc | "power_bloc_share_power_projection_without(scope:country) > 0.2" | value |
| power_bloc_share_prestige | Compare the share of Prestige of the country in scope against all its Power Bloc members, returns -1 if not in a Power Bloc | power_bloc_share_prestige > 0.2 | value |
| power_bloc_share_prestige_with | Compare the share of Prestige of the country in scope against all its Power Bloc members plus an additional country, returns -1 if not in a Power Bloc | "power_bloc_share_prestige_with(scope:country) > 0.2" | value |
| power_bloc_share_prestige_without | Compare the share of Prestige of the country in scope against all its Power Bloc members minus one of the members, returns -1 if not in a Power Bloc | "power_bloc_share_prestige_without(scope:country) > 0.2" | value |
| prestige | Compare prestige |  | value |
| primary_cultures_percent_country | Checks that a country's population has a certain percentage of the country's primary cultures | scope:example_country = { primary_cultures_percent_country >= 0.2 } | value |
| produced_authority | Compares the produced authority of the scoped country |  | value |
| produced_bureaucracy | Compares the produced bureaucracy of the scoped country |  | value |
| produced_influence | Compares the produced influence of the scoped country |  | value |
| radical_fraction | Compares radical fraction in pops in state or country, all parameters except value are optional | radical_fraction = { value = <script_value> pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> } | value |
| radical_population_fraction | Compares the fraction of the population that are radicals in a given country | radical_population_fraction > 0.2 | value |
| region_score | Compares the aggregated AI strategy region score for the specified strategic region in country scope Returns 0 in case the country is player controled | region_score = { strategic_region = sr:region_key value >= 300 } "region_score(sr:region_key)" >= 300 | value |
| relative_authority | Compares the unused fraction of authority for the scoped country |  | value |
| relative_bureaucracy | Compares the unused fraction of bureaucracy for the scoped country |  | value |
| relative_influence | Compares the unused fraction of influence for the scoped country |  | value |
| religion_percent_country | Checks that a country's population has a certain percentage of a specific religion | scope:example_country = { religion_percent_country = { target = rel:catholic value <= 0.8 } } | value |
| ruler_can_have_command | Checks if the country's government type allows its ruler to have command | ruler_can_have_command = yes/no | boolean |
| scaled_debt | Compare value to a country's debt relative to debt ceiling | scaled_debt = value | value |
| scaled_gold_reserves | Compare value to a country's gold reserves relative to reserves limit | scaled_gold_reserves = value | value |
| ship_modification_market_demand_ratio | Goods-weighted buy/sell ratio for the construction goods of the target ship modification, evaluated against the country-scope's market. | "ship_modification_market_demand_ratio(scope:ship_modification_type) > 1.25" | value |
| should_set_wargoal | Check if the country is lacking a primary wargoal in any diplomatic play it is part of |  | boolean |
| shrinking_institution | Checks if the institution is shrinking | expanding_institution = <scope/key> |  |
| size_weighted_lost_battles_fraction | Determines the fraction of battles the target country has lost in the target war, weighted by manpower size of all battles in the war | size_weighted_lost_battles_fraction = { target = scope:war value > 0.3 } add = "size_weighted_lost_battles_fraction(scope:war)" | value |
| sol_ranking | Compares a Country's Standard of Living Ranking (position) | sol_ranking > 42 | value |
| subject_can_increase_autonomy | Check if a subject can increase its autonomy | subject_can_increase_autonomy = bool | boolean |
| supply_network_strength | Compares the country's supply network strength (can exceed 1) | supply_network_strength > 1.1 | value |
| supply_ship_maintenance_fulfillment | Compares the supply ship maintenance fulfillment ratio of a country | supply_ship_maintenance_fulfillment < 1 | value |
| taking_loans | Check if the country is currently running a weekly deficit and taking loans to compensate |  | boolean |
| tax_level | Compares the overall tax level of scoped country. `very_low, low, medium, high, very_high`; returns same number as tax_level_value trigger | tax_level = <level_term> | value |
| tax_level_value | Compares the overall tax level integer value of scoped country. `0, 1, 2, 3, 4` | income_tax_level_value = <level_num> | value |
| tax_waste | Compare the tax waste of the country | tax_waste > 100 | value |
| tenure_in_current_power_bloc_days | Compare the number of days the country in scope has been a member of their current Power Bloc | tenure_in_current_power_bloc_days > 720 | value |
| tenure_in_current_power_bloc_months | Compare the number of (whole) months the country in scope has been a member of their current Power Bloc | tenure_in_current_power_bloc_months > 20 | value |
| tenure_in_current_power_bloc_weeks | Compare the number of (whole) weeks the country in scope has been a member of their current Power Bloc | tenure_in_current_power_bloc_weeks > 12 | value |
| tenure_in_current_power_bloc_years | Compare the number of (whole) years the country in scope has been a member of their current Power Bloc | tenure_in_current_power_bloc_years > 5 | value |
| total_population | Compares the total population of a given country | total_population > 100000 | value |
| total_population_including_subjects | Compares the total population in the scope country and its subjects | total_population_including_subjects > 40000000 | value |
| total_population_including_subjects_share | Compares the total population in the scope country and its subjects' share of the global population | total_population_including_subjects_share > 0.4 | value |
| total_population_share | Compares the total population of a given country's share of the global population | total_population_share > 0.02 | value |
| transfer_money_gross_income | Does the country have this amount of gross income (income before expenses) from money transfer treaties | transfer_money_gross_income > 1000 | value |
| transfer_money_net_income | Does the country have this amount of net income (income after expenses) from money transfer treaties | transfer_money_net_income > 1000 | value |
| war_participant_has_war_goal_of_type_against | Checks if scope country holds a wargoal of a specific type targeting a specific country in any war | war_participant_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } |  |
| war_side_has_war_goal_of_type_against | Checks if any country on the same side as scope country in any war holds a wargoal of a specific type targeting a specific country | war_side_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } |  |
| was_formed_from | Check if a formed country previously had a specific definition | was_formed_from = <tag> |  |
| wealth_share | Checks the wealth political strength share of a pop type, religion or culture in a country or state. Exactly one of pop_type, religion or culture must be specified. | wealth_share = { pop_type/religion/culture = <key/scope> value <compare operator> <value> } | value |
| would_accept_diplomatic_action | Checks if a country would accept a diplomatic action proposed by another country | would_accept_diplomatic_action = { actor = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> modify_acceptance = <script value, optional> } if set, modify_acceptance will be added to their acceptance score, to allow for checking if they would accept with an obligation, etc |  |

| Event target | Description | To scope |
|---|---|---|
| active_law | Scope to the scoped country's active law in the named law group (active_law:lawgroup_trade_policy) | law |
| ai_army_comparison | Scope to comparative army strength between two countries (example: value = ai_army_comparison:root) | value |
| ai_gdp_comparison | Scope to comparative GDP between two countries (example: value = ai_army_comparison:root) | value |
| ai_ideological_opinion | Scope to AI ideological opinion of scope country on target country (example: value = ai_ideological_opinion:root) | value |
| ai_navy_comparison | Scope to comparative navy strength between two countries (example: value = ai_navy_comparison:root) | value |
| ai_subject_value | Scope to AI desire of target country to have scope country as a subject (example: value = ai_subject_value:root) | value |
| ai_transit_rights_value | Scope to AI desire of to have transit rights through target country (example: value = ai_transit_rights_value:root) | value |
| ai_treaty_fairness | Scope to AI evaluation of how fair (to both sides) it considers existing treaty articles with the target country to be (example: value = ai_treaty_fairness_score:root) | value |
| ai_treaty_value | Scope to AI evaluation of how favorable to itself it considers existing treaty articles with the target country to be (example: value = ai_treaty_value:root) | value |
| army_size | Number of battalions of scope country, excluding currently raised conscripts. | value |
| army_size_including_conscripts | Number of battalions of scope country, including currently raised conscripts. | value |
| army_size_including_raised_conscripts | Number of battalions of scope country, including currently raised conscripts but excluding unraised conscripts. | value |
| average_expected_sol | Get the average expected Standard of Living of the scope | value |
| average_sol | Get the average Standard of Living of the scope | value |
| building_levels | Get the total number of non-subsistence building levels of the scoped country | value |
| cached_ai_coastal_population | Scope to total coastal population recorded in AI spending variables (example: value = cached_ai_coastal_population) | value |
| cached_ai_incorporated_coastal_population | Scope to total incorporated coastal population recorded in AI spending variables (example: value = cached_ai_incorporated_coastal_population) | value |
| cached_ai_incorporated_population | Scope to total incorporated population recorded in AI spending variables (example: value = cached_ai_incorporated_population) | value |
| cached_ai_overseas_subject_population | Scope to total population in direct non-adjacent subjects recorded in AI spending variables (example: value = cached_ai_overseas_subject_population) | value |
| cached_ai_subject_population | Scope to total population in direct subjects recorded in AI spending variables (example: value = cached_ai_subject_population) | value |
| cached_ai_total_population | Scope to total population recorded in AI spending variables (example: value = cached_ai_total_population) | value |
| cached_ai_unincorporated_coastal_population | Scope to total unincorporated coastal population recorded in AI spending variables (example: value = cached_ai_unincorporated_coastal_population) | value |
| cached_ai_unincorporated_population | Scope to total unincorporated population recorded in AI spending variables (example: value = cached_ai_unincorporated_population) | value |
| capital | Scope to the capital state of a country | state |
| civil_war_origin_country | Scope to the origin country of a civil war country | country |
| colonial_growth_per_colony | Scope to the country's colonial growth per colony value (example: colonial_growth_per_colony > 0) | value |
| company | Scope to the scoped country's company of the named company type (company:company_rheinmetall) | company |
| country_definition | Scope to country's definition | country_definition |
| credit | Scope to the current amount of max credit the country can take | value |
| currently_enacting_law | Scope from a country to the law that they're currently enacting | law |
| diplomatic_pact_expense_ratio | Scope to the ratio of diplomatic pact expenses to income for this country, clamped 0-1 (example: value = diplomatic_pact_expense_ratio) | value |
| flagship | Get the flagship of the scoped country | ship |
| gdp | Get the scoped country's yearly predicted GDP | value |
| get_ruler_for | Scopes from country to a character that would be ruler, under the given transfer of power type get_ruler_for:parliamentary_elective = { effects... } | character |
| government_size | Get the scoped country's current number of Parties & independent IGs in government | value |
| heir | Scope to the heir of a country | character |
| ig | Scope to the interest group of specified key belonging to the country, example: ig:ig_armed_forces | interest_group |
| imposed_law | Scope from a country to the law currently imposed on them (enacting or not) | law |
| imposer_of_law | Scope from a country to the country currently imposing a law on them | country |
| income | Get the current weekly income of the scoped country | value |
| income_transfer_expenses | Scope to the amount of money scope country is transferring to other countries via treaties & pacts (example:income_transfer_expenses >= 100) | value |
| income_transfer_relative_expenses | Scope to the fraction of their income country is transferring to other countries via treaties & pacts (example:income_transfer_relative_expenses >= 0.2) | value |
| infamy | Scope to infamy of scope country (example: infamy >= 2) | value |
| institution | Scope to a country's institution from its name (institution:institution_health_system) | institution |
| investment_pool_income | Get the current weekly investment pool income of the scoped country | value |
| je | Scope to the journal entry of specified key belonging to the country, example: je:je_antarctica | journal_entry |
| legitimacy | Scope to the current amount of legitimacy in country | value |
| lobby_foreign_anti_clout | Scope to the total clout of all anti-country foreign policy lobbies targeting a specific country (lobby_foreign_anti_clout:root >= 0.2) | value |
| lobby_foreign_pro_clout | Scope to the total clout of all pro-country foreign policy lobbies targeting a specific country (lobby_foreign_pro_clout:root >= 0.2) | value |
| lobby_in_government_foreign_anti_clout | Scope to the total clout of all anti-country foreign policy lobbies in government targeting a specific country (lobby_in_government_foreign_anti_clout:root >= 0.2) | value |
| lobby_in_government_foreign_pro_clout | Scope to the total clout of all pro-country foreign policy lobbies in government targeting a specific country (lobby_in_government_foreign_pro_clout:root >= 0.2) | value |
| lobby_war_opposition | Scope to the total clout of all lobbies that oppose the scoped war (lobby_war_opposition:root >= 0.2) | value |
| lobby_war_support | Scope to the total clout of all lobbies that support the scoped war (lobby_war_support:root >= 0.2) | value |
| market | Scope to the market of the object | market |
| market_capital | Scope to the market capital of a country | state |
| migration_pull | Get the migration pull for a state or the mass migration pull for a country. | value |
| military_expenses | Get the current military expenses (slaves, wages and goods) of the scoped country | value |
| military_expenses_share | Get the current share of military expenses (slaves, wages and goods) relative to the total expenses of the scoped country | value |
| modifier | Scope to the value of the modifier type of specified key belonging to the current object, example: modifier:country_influence_add | boolean, value |
| mutual_trade_value_with_country | Scope to the total base value of goods traded in trade routes between the two markets (example: mutual_trade_value_with_country:root >= 1000) | value |
| naval_combat_power | Scope to the country's navy combat power (example: naval_combat_power > 100) | value |
| naval_hostility_average_damage_dealt | Scope to average damage dealt by this country in naval hostilities it initiated over the lookback period. Returns -1 if no hostilities found. | value |
| naval_hostility_damage | Scope to damage points inflicted by this country against another in active naval hostilities (example: naval_hostility_damage:root >= 50) | value |
| naval_vulnerability | Scope to a country's naval vulnerability score based on trade reliance and coastal GDP share, capped at a define maximum | value |
| navy_size | Number of flotillas of scope country. | value |
| num_active_interests | Scope to the number of active interests a country has num_active_interests > 5 | value |
| num_active_natural_interests | Scope to the number of active natural interests a country has num_active_natural_interests > 5 | value |
| num_active_plays | Get the current number of active Diplomatic Plays the scoped country started | value |
| num_active_ships | Get the number of active ships for a country, commander or military formation OR Get the number of active ships for military formations in the province that are allied to the specified country | value |
| num_active_ships_in_battle | Get the number of active ships in battle for a country, commander or military formation OR Get the number of active ships in battle for military formations in the province that are allied to the specified country | value |
| num_active_ships_not_in_battle | Get the number of active ships not in battle for a country, commander or military formation OR Get the number of active ships not in battle for military formations in the province that are allied to the specified country | value |
| num_admirals | Scope to the country's number of admirals | value |
| num_alliances | Get the total number of alliances of the scoped country (example: num_alliances:root >= 2) | value |
| num_alliances_and_defensive_pacts_with_allies | Scope to the number of alliances target country has with allies of scope country (example: num_alliances_and_defensive_pacts_with_allies:root >= 2) | value |
| num_alliances_and_defensive_pacts_with_rivals | Scope to the number of alliances & defensive pacts target country has with rivals of scope country (example: num_alliances_and_defensive_pacts_with_rivals:root >= 2) | value |
| num_characters | Scope to the country's number of characters | value |
| num_colony_projects | Get the scoped country's current number of incomplete / in progress colony projects | value |
| num_commanders | Scope to the country's number of commanders | value |
| num_defensive_pacts | Scope to the number of defensive pacts target country has in total (example: num_defensive_pacts >= 2) | value |
| num_generals | Scope to the country's number of generals | value |
| num_income_transfer_pacts | Scope to the number of income-transferring (to others) pacts target country has in total (example: num_income_transfer_pacts >= 2) | value |
| num_income_transfer_treaty_articles | Scope to the number of income-transferring (to others) treaty articles target country has in total (example: num_income_transfer_treaty_articles >= 2) | value |
| num_income_transfers | Scope to the number of income-transferring (to others) pacts and treaty articles target country has in total (example: num_income_transfers >= 2) | value |
| num_incorporated_states | Get the scoped country's current number of incorporated states | value |
| num_interests | Scope to the number of interests a country has (including inactive) num_interests > 5 | value |
| num_natural_interests | Scope to the number of natural interests a country has (including inactive) num_natural_interests > 5 | value |
| num_non_destroyed_ships | Get the number of non-destroyed ships for a country, commander or military formation OR Get the number of non-destroyed ships for military formations in the province that are allied to the specified country | value |
| num_non_destroyed_ships_in_battle | Get the number of non-destroyed ships in battle for a country, commander or military formation OR Get the number of non-destroyed ships in battle for military formations in the province that are allied to the specified country | value |
| num_non_destroyed_ships_not_in_battle | Get the number of non-destroyed ships not in battle for a country, commander or military formation OR Get the number of non-destroyed ships not in battle for military formations in the province that are allied to the specified country | value |
| num_obligations_earned | Scope from a country to the number of obligations others owe them (=which they have earned) | value |
| num_pending_events | Scope to the number of pending events in scope country, generally or for a specified category num_pending_events > 0 num_pending_events:enactment > 0 | value |
| num_politicians | Scope to the country's number of politicians | value |
| num_positive_relations | Get the current number of countries with positive Relation with the scoped country | value |
| num_queued_constructions | Scope to the number of queued constructions target country has in total (example: num_queued_constructions >= 2) | value |
| num_queued_government_constructions | Scope to the number of queued government constructions target country has in total (example: num_queued_government_constructions >= 2) | value |
| num_queued_private_constructions | Scope to the number of queued private constructions target country has in total (example: num_queued_private_constructions >= 2) | value |
| num_rivals | Scope to the number of rivals target country has in total (example: num_rivals >= 2) | value |
| num_ruling_igs | Get the scoped country's current number of IGs in government | value |
| num_shared_rivals | Scope to the number of shared rivals scope country has with target country (example: num_shared_rivals:root >= 2) | value |
| num_ships | Get the number of ships for a country, commander or military formation OR Get the number of ships for military formations in the province that are allied to the specified country | value |
| num_ships_in_battle | Get the number of ships in battle for a country, commander or military formation OR Get the number of ships in battle for military formations in the province that are allied to the specified country | value |
| num_ships_not_in_battle | Get the number of ships not in battle for a country, commander or military formation OR Get the number of ships not in battle for military formations in the province that are allied to the specified country | value |
| num_ships_of_group | Number of ships of the provided ship group in the scoped country or military formation | value |
| num_states | Get the scoped country's current number of states | value |
| num_unincorporated_states | Get the scoped country's current number of unincorporated states | value |
| overlord | Scope to the direct overlord of the country in scope | country |
| owner | Scope to the owner country of object | country |
| owning_company | Scope to the company owning the scoped country | company |
| pirated_trade_value_by | Scope to the average weekly base value of goods pilfered from this country by a target country (example: pirated_trade_value_by:root >= 50) | value |
| power_bloc | Scope to the power bloc for the scoped country | power_bloc |
| principal | Get the current debt principal of the country | value |
| py | Scope to the active party of specified key belonging to the country, example: py:communist_party | party |
| relations | Scope to relations between two countries (example: relations:root >= 2) | value |
| relations_change_rate | Scope to daily change in relations progress between two countries (example: relations_change_rate:root > 0) | value |
| religion | Scope to country or country definition's primary religion or pop religion | religion |
| ruler | Scope to the ruler of a country | character |
| strait_trade_importance_by | Scope to the trade importance of goods this country is trading through straits controlled by a target country. Accumulated value is multiplied by STRAIT_FULL_CONTROL_TRADE_IMPORTANCE_MULT for straits where the controller controls both sides (example: strait_trade_importance_by:root >= 100) | value |
| technology_being_researched | Scope to the current technology a country is researching | technology |
| techs_researched | Scope to the current amount of techs researched of a country | value |
| tension | Scope to tension between two countries (example: tension:root >= 2) | value |
| top_overlord | Scope to the top overlord of the country in scope | country |
| total_crew_needed | Get the total crew needed by all ships of a country | value |
| total_export_value | Scope to the total value of scope country's exports to the world market (example: total_export_value >= 1000) | value |
| total_import_value | Scope to the total value of scope country's imports from the world market (example: total_import_value >= 1000) | value |
| total_marine_capacity | Get the total marine capacity across all fleets of a country | value |
| total_trade_value | Scope to the total value of scope country's trade with the world market (example: total_trade_value >= 1000) | value |

### Country modifier types

`country_` [modifier types](Modifier types.md) apply their effects to countries.

For reasons of length, the culture-based modifier types `country_[culture]_cultural_acceptance_add` and `country_fervor_target_[culture]_add` are excluded.

| Modifier type | Localization | Type | Format | Notes |
|---|---|---|---|---|
| country_academics_pol_str_mult | Political Strength of Academics | multiplicative | percent, neutral |  |
| country_academics_voting_power_add | Political Strength from the Votes of Academics | additive | neutral | Object-based Enables elections |
| country_acceptance_homeland_add | Acceptance from Homeland | additive | good |  |
| country_acceptance_no_shared_heritage_trait_add | Acceptance from no shared Heritage Traits | additive | good |  |
| country_acceptance_no_shared_language_trait_add | Acceptance from no shared Language Traits | additive | good |  |
| country_acceptance_no_shared_religious_trait_add | Acceptance from no shared Religious Traits | additive | good |  |
| country_acceptance_no_shared_tradition_trait_add | Acceptance from no shared Tradition Traits | additive | good |  |
| country_acceptance_not_homeland_add | Acceptance from not Homeland | additive | good |  |
| country_acceptance_primary_culture_add | Acceptance from Primary Culture | additive | good |  |
| country_acceptance_shared_heritage_trait_add | Acceptance from Heritage Trait | additive | good |  |
| country_acceptance_shared_heritage_trait_group_add | Acceptance from Heritage Trait Group | additive | good |  |
| country_acceptance_shared_language_trait_add | Acceptance from Language Trait | additive | good |  |
| country_acceptance_shared_language_trait_group_add | Acceptance from Language Trait Group | additive | good |  |
| country_acceptance_shared_religious_trait_add | Acceptance from Religious Traits | additive | good |  |
| country_acceptance_shared_religious_trait_group_add | Acceptance from Religious Trait Groups | additive | good |  |
| country_acceptance_shared_tradition_trait_add | Acceptance from Tradition Trait | additive | good |  |
| country_acceptance_state_religion_add | Acceptance from State Religion | additive | good |  |
| country_admiral_rank_impact_mult | Admiral Rank Impact | multiplicative | percent, good |  |
| country_agitator_slots_add | Potential Agitators | additive | good |  |
| country_ahead_of_time_research_penalty_mult | Ahead of Time Penalty | multiplicative | percent, bad |  |
| country_all_buildings_protected_bool | Disallow Downsizing All Buildings | boolean | bad |  |
| country_allow_assimilation_cultural_erasure_bool | Allows Assimilation for the Cultural Erasure Status | boolean | neutral |  |
| country_allow_assimilation_full_acceptance_bool | Allows Assimilation for the Full Acceptance Status | boolean | neutral |  |
| country_allow_assimilation_open_prejudice_bool | Allows Assimilation for the Open Prejudice Status | boolean | neutral |  |
| country_allow_assimilation_second_rate_citizen_bool | Allows Assimilation for the Second-class Citizen Status | boolean | neutral |  |
| country_allow_assimilation_violent_hostility_bool | Allows Assimilation for the Violent Hostility Status | boolean | neutral |  |
| country_allow_conversion_cultural_erasure_bool | Allows Conversion for the Cultural Erasure Status | boolean | neutral |  |
| country_allow_conversion_full_acceptance_bool | Allows Conversion for the Full Acceptance Status | boolean | neutral |  |
| country_allow_conversion_open_prejudice_bool | Allows Conversion for the Open Prejudice Status | boolean | neutral |  |
| country_allow_conversion_second_rate_citizen_bool | Allows Conversion for the Second-class Citizen Status | boolean | neutral |  |
| country_allow_conversion_violent_hostility_bool | Allows Conversion for the Violent Hostility Status | boolean | neutral |  |
| country_allow_enacting_decrees_in_subject_bool | Allow enacting Decrees on Subject States | boolean | good |  |
| country_allow_multiple_alliances_bool | Allow Multiple Alliances | boolean | good |  |
| country_allow_voting_cultural_erasure_bool | Gives Voting Rights to the Cultural Erasure Status | boolean | neutral |  |
| country_allow_voting_full_acceptance_bool | Gives Voting Rights to the Full Acceptance Status | boolean | neutral |  |
| country_allow_voting_open_prejudice_bool | Gives Voting Rights to the Open Prejudice Status | boolean | neutral |  |
| country_allow_voting_second_rate_citizen_bool | Gives Voting Rights to the Second-class Citizen Status | boolean | neutral |  |
| country_allow_voting_violent_hostility_bool | Gives Voting Rights to the Violent Hostility Status | boolean | neutral |  |
| country_amenability_add | Country Amenability | additive | good |  |
| country_aristocrats_pol_str_mult | Political Strength of Aristocrats | multiplicative | percent, neutral |  |
| country_aristocrats_voting_power_add | Political Strength from the Votes of Aristocrats | additive | neutral | Object-based Enables elections |
| country_assimilation_cultural_erasure_mult | Assimilation for the Cultural Erasure Status | multiplicative | percent, neutral |  |
| country_assimilation_delta_threshold_add | Cultural Assimilation Threshold | additive | good |  |
| country_assimilation_full_acceptance_mult | Assimilation for the Full Acceptance Status | multiplicative | percent, neutral |  |
| country_assimilation_open_prejudice_mult | Assimilation for the Open Prejudice Status | multiplicative | percent, neutral |  |
| country_assimilation_second_rate_citizen_mult | Assimilation for the Second-class Citizen Status | multiplicative | percent, neutral |  |
| country_assimilation_violent_hostility_mult | Assimilation for the Violent Hostility Status | multiplicative | percent, neutral |  |
| country_authority_add | Authority | additive | good |  |
| country_authority_cost_add | Authority Cost | additive | bad |  |
| country_authority_mult | Authority | multiplicative | percent, good |  |
| country_authority_per_subject_add | Authority per Subject | additive | good |  |
| country_bg_manufacturing_require_subsidies_bool | Forced Subsidies for Manufacturing | boolean | bad |  |
| country_block_government_reform_bool | Blocks Government Reform | boolean | neutral |  |
| country_bolster_attraction_factor | Bolstered impact on Political Movement attraction | multiplicative | percent, neutral |  |
| country_bolster_cost_mult | Bolstering cost | multiplicative | percent, bad |  |
| country_brahmins_acceptance_min_add | Minimum Acceptance for the Brahmins Social Class | additive | good |  |
| country_brahmins_qualification_growth_other_class_mult | Qualification Growth outside the Brahmins Social Class for Brahmins | multiplicative | percent, good |  |
| country_brahmins_qualification_growth_same_class_mult | Qualification Growth within Brahmins Social Class | multiplicative | percent, good |  |
| country_bureaucracy_add | Bureaucracy | additive | good |  |
| country_bureaucracy_cost_add | Bureaucracy Cost | additive | bad |  |
| country_bureaucracy_investment_cost_factor_mult | Bureaucracy Institution Cost Multiplier | multiplicative | percent, bad |  |
| country_bureaucracy_mult | Bureaucracy | multiplicative | percent, good |  |
| country_bureaucrats_pol_str_mult | Political Strength of Bureaucrats | multiplicative | percent, neutral |  |
| country_bureaucrats_voting_power_add | Political Strength from the Votes of Bureaucrats | additive | neutral | Object-based Enables elections |
| country_can_form_construction_company_bool | Can form Construction type Companies | boolean | neutral |  |
| country_can_impose_same_lawgroup_army_model_in_power_bloc_bool | **Impose** same Army Model Law on Bloc Members | boolean | good |  |
| country_can_impose_same_lawgroup_church_and_state_in_power_bloc_bool | **Impose** same Church and State Law on Bloc Members | boolean | good |  |
| country_can_impose_same_lawgroup_citizenship_in_power_bloc_bool | **Impose** same Citizenship Law on Bloc Members | boolean | good |  |
| country_can_impose_same_lawgroup_colonization_in_power_bloc_bool | **Impose** same Colonization Law on Bloc Members | boolean | good |  |
| country_can_impose_same_lawgroup_distribution_of_power_in_power_bloc_bool | **Impose** same Distribution of Power Law on Bloc Members | boolean | good |  |
| country_can_impose_same_lawgroup_education_system_in_power_bloc_bool | **Impose** same Education System Law on Bloc Members | boolean | good |  |
| country_can_impose_same_lawgroup_governance_principles_in_power_bloc_bool | **Impose** same Governance Principles Law on Bloc Members | boolean | good |  |
| country_can_impose_same_lawgroup_policing_in_power_bloc_bool | **Impose** same Policing Law on Bloc Members | boolean | good |  |
| country_can_only_conscript_peasants_bool | Allows only Infantry Conscript Battalions | boolean | good |  |
| country_cannot_be_subjugated_bool | Cannot be Subjugated | boolean | neutral |  |
| country_cannot_be_target_for_law_imposition_bool | Cannot be targeted for Law Imposition | boolean | good |  |
| country_cannot_cancel_law_enactment_bool | Disallow}} Cancel Law Enactment | boolean | bad |  |
| country_cannot_enact_laws_bool | Disallow}} Enacting Laws | boolean | bad |  |
| country_cannot_join_power_bloc_bool | Cannot join Power Blocks | boolean | neutral |  |
| country_cannot_start_law_enactment_bool | Disallow}} Start Law Enactment | boolean | bad |  |
| country_capitalists_pol_str_mult | Political Strength of Capitalists | multiplicative | percent, neutral |  |
| country_capitalists_voting_power_add | Political Strength from the Votes of Capitalists | additive | neutral | Object-based Enables elections |
| country_clergymen_pol_str_mult | Political Strength of Clergymen | multiplicative | percent, neutral |  |
| country_clergymen_voting_power_add | Political Strength from the Votes of Clergymen | additive | neutral | Object-based Enables elections |
| country_clerks_pol_str_mult | Political Strength of Clerks | multiplicative | percent, neutral |  |
| country_clerks_voting_power_add | Political Strength from the Votes of Clerks | additive | neutral | Object-based Enables elections |
| country_company_construction_efficiency_bonus_add | Company Construction Bonus | additive | percent, good |  |
| country_company_throughput_bonus_add | Company Throughput Bonus | additive | percent, good |  |
| country_construction_add | Construction | additive | good |  |
| country_construction_goods_cost_mult | Construction Goods Cost | multiplicative | percent, bad |  |
| country_consumption_tax_cost_mult | Consumption Tax Cost | multiplicative | percent, bad |  |
| country_conversion_delta_threshold_add | Religious Conversion Threshold | additive | good |  |
| country_coup_resistance_add | Coup Resistance | additive | neutral |  |
| country_coup_resistance_mult | Coup Resistance | multiplicative | percent, neutral |  |
| country_dalit_acceptance_max_add | Maximum Acceptance for the Dalit Social Class | additive | bad |  |
| country_dalit_cultural_acceptance_mult | Cultural Acceptance for the Dalit Social Class | multiplicative | percent, good |  |
| country_dalit_education_access_add | Education Access for the Dalit Social Class | additive | good |  |
| country_dalit_education_access_mult | Education Access for the Dalit Social Class | multiplicative | percent, good |  |
| country_dalit_qualification_growth_add | Qualification Growth for the Dalit Social Class | additive | good |  |
| country_dalit_qualification_growth_mult | Qualification Growth for the Dalit Social Class | multiplicative | percent, good |  |
| country_dalit_qualification_growth_other_class_mult | Qualification Growth outside the Dalit Social Class for Dalit | multiplicative | percent, good |  |
| country_dalit_qualification_growth_same_class_mult | Qualification Growth within Dalit Social Class | multiplicative | percent, good |  |
| country_damage_relations_speed_mult | Damage Relations Speed | multiplicative | percent, good |  |
| country_diplomatic_play_maneuvers_add | Maneuvers per Diplomatic Play | additive | good |  |
| country_diplomatic_play_maneuvers_mult | Maneuvers per Diplomatic Play | multiplicative | percent, good |  |
| country_diplomatic_reputation_add | Diplomatic Reputation | additive | good |  |
| country_disable_investment_pool_bool | Disable Investment Pool (except for Companies) | boolean | bad |  |
| country_disable_nationalization_bool | Disable Nationalization | boolean | bad |  |
| country_disable_nationalization_without_compensation_bool | Disable Nationalization without compensation | boolean | bad |  |
| country_disable_non_company_privatization_bool | Disable Privatization (except for Companies) | boolean | bad |  |
| country_disallow_aggressive_plays_bool | Disallow Aggressive Diplomatic Plays | boolean | neutral |  |
| country_disallow_agitator_invites_bool | Disallowed from inviting Exiles | boolean | neutral |  |
| country_disallow_government_work_cultural_erasure_bool | Disallow Upper and Middle Strata work in Government Buildings for the Cultural Erasure Status | boolean | neutral |  |
| country_disallow_government_work_full_acceptance_bool | Disallow Upper and Middle Strata work in Government Buildings for the Full Acceptance Status | boolean | neutral |  |
| country_disallow_government_work_open_prejudice_bool | Disallow Upper and Middle Strata work in Government Buildings for the Open Prejudice Status | boolean | neutral |  |
| country_disallow_government_work_second_rate_citizen_bool | Disallow Upper and Middle Strata work in Government Buildings for the Second-class Citizen Status | boolean | neutral |  |
| country_disallow_government_work_violent_hostility_bool | Disallow Upper and Middle Strata work in Government Buildings for the Violent Hostility Status | boolean | neutral |  |
| country_disallow_law_no_colonial_affairs_bool | Disallow No Colonial Affairs | boolean | bad |  |
| country_disallow_law_no_police_bool | Disallow No Police | boolean | bad |  |
| country_disallow_law_no_schools_bool | Disallow No Schools | boolean | bad |  |
| country_disallow_military_work_cultural_erasure_bool | Disallow work in Military Buildings for the Cultural Erasure Status | boolean | neutral |  |
| country_disallow_military_work_full_acceptance_bool | Disallow work in Military Buildings for the Full Acceptance Status | boolean | neutral |  |
| country_disallow_military_work_open_prejudice_bool | Disallow work in Military Buildings for the Open Prejudice Status | boolean | neutral |  |
| country_disallow_military_work_second_rate_citizen_bool | Disallow work in Military Buildings for the Second-class Citizen Status | boolean | neutral |  |
| country_disallow_military_work_violent_hostility_bool | Disallow work in Military Buildings for the Violent Hostility Status | boolean | neutral |  |
| country_disallow_trade_bool | Disable Trade Centers | boolean | bad |  |
| country_disallow_trade_outside_canton_bool | Disable Trade Centers outside Western Guangdong | boolean | bad | Script-only |
| country_disallow_trade_outside_kyushu_bool | Disable Trade Centers outside Kyushu | boolean | bad |  |
| country_economic_dependence_on_overlord_add | Economic Dependence on Overlord | additive | bad |  |
| country_education_fervor_add | Education Institution Fervor | additive | neutral |  |
| country_electoral_confidence_impact_mult | Electoral Confidence Impact | multiplicative | percent, neutral |  |
| country_electoral_confidence_over_time | Monthly Electoral Confidence Change |  | percent, good |  |
| country_enactment_speed_law_anarchy_mult | country_enactment_speed_law_anarchy_mult | multiplicative | percent, good |  |
| country_enactment_speed_law_autocracy_mult | country_enactment_speed_law_autocracy_mult | multiplicative | percent, good |  |
| country_enactment_speed_law_oligarchy_mult | country_enactment_speed_law_oligarchy_mult | multiplicative | percent, good |  |
| country_enactment_speed_law_public_schools_mult | Enactment Speed for Public Schools | multiplicative | percent, good |  |
| country_enactment_speed_law_single_party_state_mult | country_enactment_speed_law_single_party_state_mult | multiplicative | percent, good |  |
| country_enactment_speed_law_technocracy_mult | Enactment Speed for Technocracy | multiplicative | percent, good |  |
| country_enactment_success_chance_law_anarchy_add | Enactment Success chance for Anarchy | additive | percent, good |  |
| country_enactment_success_chance_law_autocracy_add | Enactment Success chance for Autocracy | additive | percent, good |  |
| country_enactment_success_chance_law_oligarchy_add | Enactment Success chance for Oligarchy | additive | percent, good |  |
| country_enactment_success_chance_law_public_schools_add | Enactment Success chance for Public Schools | additive | percent, good |  |
| country_enactment_success_chance_law_single_party_state_add | Enactment Success chance for Single-Party State | additive | percent, good |  |
| country_enactment_success_chance_law_technocracy_add | Enactment Success chance for Technocracy | additive | percent, good |  |
| country_engineers_pol_str_mult | Political Strength of Engineers | multiplicative | percent, neutral |  |
| country_engineers_voting_power_add | Political Strength from the Votes of Engineers | additive | neutral | Object-based Enables elections |
| country_expedition_events_explorer_mult | Expedition Opportunity | multiplicative | percent, good |  |
| country_expenses_add | Government Expenses | additive | bad |  |
| country_farmers_pol_str_mult | Political Strength of Farmers | multiplicative | percent, neutral |  |
| country_farmers_voting_power_add | Political Strength from the Votes of Farmers | additive | neutral | Object-based Enables elections |
| country_financial_districts_buy_farms_likelihood | Financial Districts investment into Plantations, Ranches, and Agriculture |  | percent, good |  |
| country_flagship_interest_gain_mult | Flagship Involvement Gain | multiplicative | percent, good |  |
| country_forbid_electoral_fraud_bool | Forbid Electoral Manipulation | boolean | neutral |  |
| country_forbid_monopoly_bool | Forbid Monopolies | boolean | bad |  |
| country_force_privatization_bool | Force Privatization | boolean | neutral |  |
| country_foreign_collectivization_bool | Foreign Collectivization | boolean | neutral |  |
| country_frankenstein_company_bool | Experimental Modules Operational | boolean | neutral |  |
| country_free_charters_add | Free Company Charters | additive | good |  |
| country_general_rank_impact_mult | General Rank Impact | multiplicative | percent, good |  |
| country_gold_reserve_limit_mult | Gold reserve limit | multiplicative | percent, good |  |
| country_government_buildings_protected_bool | Disallow Downsizing Government Buildings | boolean | bad |  |
| country_government_dividends_efficiency_add | Government Dividends Efficiency | additive | percent, good |  |
| country_government_dividends_reinvestment_add | Government Dividends Reinvestment | additive | percent, neutral |  |
| country_government_dividends_waste_add | Government Dividends Waste | additive | percent, bad |  |
| country_government_wages_mult | Government Wages | multiplicative | percent, neutral |  |
| country_higher_diplomatic_acceptance_same_religion_bool | Higher Diplomatic Proposal Acceptance for Countries with same Religion | boolean | good |  |
| country_higher_leverage_from_economic_dependence_bool | Increased Leverage from Economic Dependence | boolean | good |  |
| country_improve_relations_speed_mult | Improve Relations Speed | multiplicative | percent, good |  |
| country_infamy_decay_mult | Infamy Decay | multiplicative | percent, good |  |
| country_infamy_generation_against_unrecognized_mult | Infamy Generation against Unrecognized Powers | multiplicative | percent, bad |  |
| country_infamy_generation_mult | Infamy Generation | multiplicative | percent, bad |  |
| country_influence_add | Influence | additive | good |  |
| country_influence_cost_add | Influence Cost | additive | bad |  |
| country_influence_mult | Influence | multiplicative | percent, good |  |
| country_initiator_war_goal_maneuver_cost_mult | War Goal Maneuver cost for the Diplomatic Play Initiator | multiplicative | percent, bad |  |
| country_institution_colonial_affairs_max_investment_add | Max Colonial Affairs Institution Investment | additive | good |  |
| country_institution_cost_institution_colonial_affairs_mult | Bureaucracy Cost of Colonial Affairs | multiplicative | percent, bad |  |
| country_institution_cost_institution_health_system_mult | Bureaucracy Cost of Health System | multiplicative | percent, bad |  |
| country_institution_cost_institution_home_affairs_mult | Bureaucracy Cost of Home Affairs | multiplicative | percent, bad |  |
| country_institution_cost_institution_police_mult | Bureaucracy Cost of Law Enforcement | multiplicative | percent, bad |  |
| country_institution_cost_institution_schools_mult | Bureaucracy Cost of Education | multiplicative | percent, bad |  |
| country_institution_cost_institution_social_security_mult | Bureaucracy Cost of Social Security | multiplicative | percent, bad |  |
| country_institution_health_system_max_investment_add | Max Health System Institution Investment | additive | good |  |
| country_institution_home_affairs_max_investment_add | Max Home Affairs Institution Investment | additive | good |  |
| country_institution_impact_institution_health_system_mult | Impact of Health System | multiplicative | percent, good |  |
| country_institution_police_max_investment_add | Max Law Enforcement Institution Investment | additive | good |  |
| country_institution_schools_max_investment_add | Max Education Institution Investment | additive | good |  |
| country_institution_size_change_speed_institution_colonial_affairs_mult | Institution Size Change Speed for Colonial Affairs | multiplicative | percent, good |  |
| country_institution_size_change_speed_institution_police_mult | Institution Size Change Speed for Law Enforcement | multiplicative | percent, good |  |
| country_institution_size_change_speed_institution_schools_mult | Institution Size Change Speed for Education | multiplicative | percent, good |  |
| country_institution_size_change_speed_mult | Institution Size Change Speed | multiplicative | percent, good |  |
| country_institution_social_security_max_investment_add | Max Social Security Institution Investment | additive | good |  |
| country_institution_workplace_safety_max_investment_add | Max Workplace Safety Office Institution Investment | additive | good |  |
| country_je_korea_action_cost | country_je_korea_action_cost |  | percent, bad |  |
| country_join_power_bloc_member_in_defensive_plays_bool | Can call Power Bloc members with the Call Ally Sway in **defensive** Diplomatic Plays | boolean | neutral |  |
| country_join_power_bloc_member_in_plays_bool | Can call Power Bloc members with the Call Ally Sway in **all** Diplomatic Plays | boolean | neutral |  |
| country_kshatriyas_acceptance_max_add | Maximum Acceptance for the Kshatriyas Social Class | additive | bad |  |
| country_kshatriyas_acceptance_min_add | Minimum Acceptance for the Kshatriyas Social Class | additive | good |  |
| country_kshatriyas_cultural_acceptance_mult | Cultural Acceptance for the Kshatriyas Social Class | multiplicative | percent, good |  |
| country_kshatriyas_education_access_add | Education Access for the Kshatriyas Social Class | additive | good |  |
| country_kshatriyas_education_access_mult | Education Access for the Kshatriyas Social Class | multiplicative | percent, good |  |
| country_kshatriyas_qualification_growth_add | Qualification Growth for the Kshatriyas Social Class | additive | good |  |
| country_kshatriyas_qualification_growth_mult | Qualification Growth for the Kshatriyas Social Class | multiplicative | percent, good |  |
| country_kshatriyas_qualification_growth_other_class_mult | Qualification Growth outside the Kshatriyas Social Class for Kshatriyas | multiplicative | percent, good |  |
| country_kshatriyas_qualification_growth_same_class_mult | Qualification Growth within Kshatriyas Social Class | multiplicative | percent, good |  |
| country_laborers_pol_str_mult | Political Strength of Laborers | multiplicative | percent, neutral |  |
| country_laborers_voting_power_add | Political Strength from the Votes of Laborers | additive | neutral | Object-based Enables elections |
| country_law_enactment_imposition_success_add | Imposed Enactment Success Chance | additive | percent, good |  |
| country_law_enactment_max_setbacks_add | Maximum Law Enactment Setbacks | additive | good |  |
| country_law_enactment_speed_mult | Enactment Speed | multiplicative | percent, good |  |
| country_law_enactment_stall_add | Enactment Stall Chance | additive | percent, bad |  |
| country_law_enactment_stall_mult | Enactment Stall Chance | multiplicative | percent, bad |  |
| country_law_enactment_success_add | Enactment Success Chance | additive | percent, good |  |
| country_leader_has_law_enactment_success_mult | Power Bloc Legal Synergy | multiplicative | percent, good |  |
| country_legitimacy_base_add | Legitimacy | additive | good |  |
| country_legitimacy_govt_leader_clout_add | Legitimacy based on Government Leader Clout | additive | good |  |
| country_legitimacy_govt_size_add | Government size allowance | additive | good |  |
| country_legitimacy_govt_total_clout_add | Legitimacy based on Government Clout | additive | good |  |
| country_legitimacy_govt_total_votes_add | Legitimacy based on Votes | additive | good |  |
| country_legitimacy_headofstate_add | Legitimacy from including the Head of State In Government | additive | good |  |
| country_legitimacy_ideological_incoherence_mult | Legitimacy penalty from Ideological Incompatibility | multiplicative | percent, bad |  |
| country_legitimacy_min_add | Minimum Legitimacy | additive | neutral |  |
| country_leverage_generation_add | Leverage Generation | additive | good |  |
| country_leverage_generation_mult | Leverage Generation | multiplicative | percent, good |  |
| country_leverage_resistance_add | Leverage Resistance | additive | neutral |  |
| country_leverage_resistance_mult | Leverage Resistance | multiplicative | percent, neutral |  |
| country_liberty_desire_add | Weekly Liberty Desire | additive | neutral |  |
| country_liberty_desire_decrease_mult | Weekly Liberty Desire Decrease | multiplicative | percent, neutral |  |
| country_liberty_desire_increase_mult | Weekly Liberty Desire Increase | multiplicative | percent, neutral |  |
| country_liberty_desire_of_subjects_add | Weekly Liberty Desire for all Subjects | additive | neutral |  |
| country_limit_officers_qualifications_to_upper_strata | Officers qualifications limited to Upper Strata | boolean | neutral |  |
| country_loan_interest_rate_add | Loan interest rate | additive | percent, bad |  |
| country_loan_interest_rate_mult | Loan interest rate | multiplicative | percent, bad |  |
| country_lobby_leverage_generation_mult | Leverage Generation from Political Lobbies | multiplicative | percent, good |  |
| country_lobby_support | Lobby Support |  | good |  |
| country_loyalism_increases_cultural_erasure_mult | Loyalism increases for the Cultural Erasure Status | multiplicative | percent, good |  |
| country_loyalism_increases_full_acceptance_mult | Loyalism increases for the Full Acceptance Status | multiplicative | percent, good |  |
| country_loyalism_increases_open_prejudice_mult | Loyalism increases for the Open Prejudice Status | multiplicative | percent, good |  |
| country_loyalism_increases_second_rate_citizen_mult | Loyalism increases for the Second-class Citizen Status | multiplicative | percent, good |  |
| country_loyalism_increases_violent_hostility_mult | Loyalism increases for the Violent Hostility Status | multiplicative | percent, good |  |
| country_loyalists_from_legitimacy_mult | Loyalists from high Legitimacy | multiplicative | percent, good |  |
| country_machinists_pol_str_mult | Political Strength of Machinists | multiplicative | percent, neutral |  |
| country_machinists_voting_power_add | Political Strength from the Votes of Machinists | additive | neutral | Object-based Enables elections |
| country_mass_migration_attraction_mult | Mass Migration Attraction | multiplicative | percent, good |  |
| country_max_companies_add | Max Number of Companies | additive | good |  |
| country_max_unassigned_admirals_add | Maximum Idle Admirals | additive | good |  |
| country_max_unassigned_generals_add | Maximum Idle Generals | additive | good |  |
| country_max_weekly_construction_progress_add | Max Weekly Construction Progress | additive | good |  |
| country_migration_restrictiveness_add | Migration Restrictiveness | additive | neutral |  |
| country_military_goods_cost_mult | Military Goods Cost | multiplicative | percent, bad |  |
| country_military_tech_research_speed_mult | Military Research Speed | multiplicative | percent, good |  |
| country_military_tech_spread_mult | Technology Spread for Military | multiplicative | percent, good |  |
| country_military_wages_mult | Military Wages | multiplicative | percent, neutral |  |
| country_minting_add | Minting | additive | good |  |
| country_minting_mult | Minting | multiplicative | percent, good |  |
| country_must_have_movement_to_enact_laws_bool | Must have Political Movement to Enact Laws | boolean | bad |  |
| country_nationalization_cost_non_members_mult | Cost for Nationalization | multiplicative | percent, bad |  |
| country_navy_goods_cost_mult | Navy Goods Cost | multiplicative | percent, bad |  |
| country_no_advantage_loss_from_lack_of_interest_bool | Ignores Trade Advantage penalty from Interests | boolean | good |  |
| country_non_state_religion_wages_mult | Wages for Non-State Religion Pops | multiplicative | percent, neutral |  |
| country_officers_pol_str_mult | Political Strength of Officers | multiplicative | percent, neutral |  |
| country_officers_voting_power_add | Political Strength from the Votes of Officers | additive | neutral | Object-based Enables elections |
| country_opposition_ig_approval_add | Opposition Interest Group Approval | additive | good |  |
| country_overlord_income_transfer_mult | Overlord Income Transfer | multiplicative | percent, bad |  |
| country_pact_leverage_generation_add | Leverage Generation from Diplomatic Pact | additive | good |  |
| country_pact_leverage_generation_mult | Leverage Generation from Diplomatic Pact | multiplicative | percent, good |  |
| country_party_whip_impact_add | Party Whip Impact on Ideological Incoherence | additive | percent, good |  |
| country_peasants_pol_str_mult | Political Strength of Peasants | multiplicative | percent, neutral |  |
| country_peasants_voting_power_add | Political Strength from the Votes of Peasants | additive | neutral | Object-based Enables elections |
| country_piracy_income_add | Piracy Income | additive | percent, good |  |
| country_political_strength_cultural_erasure_mult | Political Strength for the Cultural Erasure Status | multiplicative | percent, good |  |
| country_political_strength_full_acceptance_mult | Political Strength for the Full Acceptance Status | multiplicative | percent, good |  |
| country_political_strength_open_prejudice_mult | Political Strength for the Open Prejudice Status | multiplicative | percent, good |  |
| country_political_strength_second_rate_citizen_mult | Political Strength for the Second-class Citizen Status | multiplicative | percent, good |  |
| country_political_strength_violent_hostility_mult | Political Strength for the Violent Hostility Status | multiplicative | percent, good |  |
| country_port_connection_cost_mult | Merchant Marine Cost of Port Connections | multiplicative | percent, bad |  |
| country_prestige_add | Prestige | additive | good |  |
| country_prestige_from_army_power_projection_mult | Prestige from Army Power Projection | multiplicative | percent, good |  |
| country_prestige_from_navy_power_projection_mult | Prestige from Navy Power Projection | multiplicative | percent, good |  |
| country_prestige_mult | Prestige | multiplicative | percent, good |  |
| country_primary_culture_fervor_from_laws_add | Primary Culture Fervor from Laws | additive | neutral |  |
| country_private_construction_allocation_mult | Private Construction Allocation | multiplicative | percent, neutral |  |
| country_production_tech_research_speed_mult | Production Research Speed | multiplicative | percent, good |  |
| country_production_tech_spread_mult | Technology Spread for Production | multiplicative | percent, good |  |
| country_qualification_growth_cultural_erasure_mult | Qualifications advancement for the Cultural Erasure Status | multiplicative | percent, good |  |
| country_qualification_growth_full_acceptance_mult | Qualifications advancement for the Full Acceptance Status | multiplicative | percent, good |  |
| country_qualification_growth_open_prejudice_mult | Qualifications advancement for the Open Prejudice Status | multiplicative | percent, good |  |
| country_qualification_growth_second_rate_citizen_mult | Qualifications advancement for the Second-class Citizen Status | multiplicative | percent, good |  |
| country_qualification_growth_violent_hostility_mult | Qualifications advancement for the Violent Hostility Status | multiplicative | percent, good |  |
| country_radicalism_increases_cultural_erasure_mult | Radicalism increases for the Cultural Erasure Status | multiplicative | percent, bad |  |
| country_radicalism_increases_full_acceptance_mult | Radicalism increases for the Full Acceptance Status | multiplicative | percent, bad |  |
| country_radicalism_increases_open_prejudice_mult | Radicalism increases for the Open Prejudice Status | multiplicative | percent, bad |  |
| country_radicalism_increases_second_rate_citizen_mult | Radicalism increases for the Second-class Citizen Status | multiplicative | percent, bad |  |
| country_radicalism_increases_violent_hostility_mult | Radicalism increases for the Violent Hostility Status | multiplicative | percent, bad |  |
| country_radicals_from_conquest_mult | Radicals from Conquest | multiplicative | percent, bad |  |
| country_radicals_from_legitimacy_mult | Radicals from low Legitimacy | multiplicative | percent, bad |  |
| country_reduced_liberty_desire_same_religion_bool | Reduced Liberty Desire for Same Religion | boolean | good |  |
| country_resource_depletion_chance_mult | Resource Depletion Chance | multiplicative | percent, bad |  |
| country_resource_discovery_chance_mult | Resource Discovery Chance | multiplicative | percent, good |  |
| country_revolution_clock_time_add | Revolution Clock Time | additive | neutral |  |
| country_revolution_progress_add | Revolution Progression Speed | additive | percent, bad |  |
| country_revolution_progress_mult | Revolution Progression Speed | multiplicative | percent, bad |  |
| country_sailors_max_add | Max Sailors | additive | good |  |
| country_secession_clock_time_add | Secession Clock Time | additive | neutral |  |
| country_secession_progress_add | Secession Progression Speed | additive | percent, bad |  |
| country_secession_progress_mult | Secession Progression Speed | multiplicative | percent, bad |  |
| country_ship_construction_add | Ship Construction | additive | good |  |
| country_ship_construction_efficiency_add | Ship Construction Efficiency | additive | percent, good |  |
| country_ship_construction_goods_cost_mult | Ship Construction Goods Cost | multiplicative | percent, bad |  |
| country_ship_construction_progress_max_add | Max Ship Construction Progress | additive | good |  |
| country_ship_crew_starting_veterancy_experience_add | Starting Ship Crew Experience | additive | good |  |
| country_ship_crew_starting_veterancy_experience_mult | Starting Ship Crew Experience | multiplicative | percent, good |  |
| country_ship_group_capital_ships_construction_efficiency_add | Capital Ships Construction Efficiency | additive | percent, good |  |
| country_ship_group_capital_ships_construction_progress_max_add | Capital Ships Max Construction Progress | additive | good |  |
| country_ship_group_capital_ships_construction_progress_max_mult | Capital Ships Max Construction Progress | multiplicative | percent, good |  |
| country_ship_group_cruisers_construction_efficiency_add | Cruisers Construction Efficiency | additive | percent, good |  |
| country_ship_group_cruisers_construction_progress_max_add | Cruisers Max Construction Progress | additive | good |  |
| country_ship_group_cruisers_construction_progress_max_mult | Cruisers Max Construction Progress | multiplicative | percent, good |  |
| country_ship_group_supply_ships_construction_efficiency_add | Supply Ships Construction Efficiency | additive | percent, good |  |
| country_ship_group_torpedo_craft_construction_efficiency_add | Torpedo Craft Construction Efficiency | additive | percent, good |  |
| country_ship_group_torpedo_craft_construction_progress_max_add | Torpedo Craft Max Construction Progress | additive | good |  |
| country_ship_group_torpedo_craft_construction_progress_max_mult | Torpedo Craft Max Construction Progress | multiplicative | percent, good |  |
| country_ship_type_armored_cruiser_construction_efficiency_add | Armored Cruiser Construction Efficiency | additive | percent, good |  |
| country_ship_type_light_cruiser_construction_efficiency_add | Light Cruiser Construction Efficiency | additive | percent, good |  |
| country_ship_type_protected_cruiser_construction_efficiency_add | Protected Cruiser Construction Efficiency | additive | percent, good |  |
| country_ship_type_troop_ship_construction_efficiency_add | Troopship Construction Efficiency | additive | percent, good |  |
| country_shopkeepers_pol_str_mult | Political Strength of Shopkeepers | multiplicative | percent, neutral |  |
| country_shopkeepers_voting_power_add | Political Strength from the Votes of Shopkeepers | additive | neutral | Object-based Enables elections |
| country_shudras_acceptance_max_add | Maximum Acceptance for the Shudras Social Class | additive | bad |  |
| country_shudras_cultural_acceptance_mult | Cultural Acceptance for the Shudras Social Class | multiplicative | percent, good |  |
| country_shudras_education_access_add | Education Access for the Shudras Social Class | additive | good |  |
| country_shudras_education_access_mult | Education Access for the Shudras Social Class | multiplicative | percent, good |  |
| country_shudras_qualification_growth_add | Qualification Growth for the Shudras Social Class | additive | good |  |
| country_shudras_qualification_growth_mult | Qualification Growth for the Shudras Social Class | multiplicative | percent, good |  |
| country_shudras_qualification_growth_other_class_mult | Qualification Growth outside the Shudras Social Class for Shudras | multiplicative | percent, good |  |
| country_shudras_qualification_growth_same_class_mult | Qualification Growth within Shudras Social Class | multiplicative | percent, good |  |
| country_slaves_voting_power_add | Political Strength from the Votes of Slaves | additive | neutral | Object-based Enables elections |
| country_society_tech_research_speed_mult | Society Research Speed | multiplicative | percent, good |  |
| country_society_tech_spread_mult | Technology Spread for Society | multiplicative | percent, good |  |
| country_soldiers_pol_str_mult | Political Strength of Servicemen | multiplicative | percent, neutral |  |
| country_soldiers_voting_power_add | Political Strength from the Votes of Servicemen | additive | neutral | Object-based Enables elections |
| country_standard_of_living_cultural_erasure_add | Standard of Living for the Cultural Erasure Status | additive | good |  |
| country_standard_of_living_full_acceptance_add | Standard of Living for the Full Acceptance Status | additive | good |  |
| country_standard_of_living_open_prejudice_add | Standard of Living for the Open Prejudice Status | additive | good |  |
| country_standard_of_living_second_rate_citizen_add | Standard of Living for the Second-class Citizen Status | additive | good |  |
| country_standard_of_living_violent_hostility_add | Standard of Living for the Violent Hostility Status | additive | good |  |
| country_state_religion_wages_mult | Wages for State Religion Pops | multiplicative | percent, neutral |  |
| country_strata_commoners_peasants_acceptance_max_add | Maximum Acceptance for the Hyakushō Social Class | additive | bad |  |
| country_strata_commoners_peasants_acceptance_min_add | Minimum Acceptance for the Hyakushō Social Class | additive | good |  |
| country_strata_commoners_peasants_cultural_acceptance_mult | Cultural Acceptance for the Hyakushō Social Class | multiplicative | percent, good |  |
| country_strata_commoners_peasants_education_access_add | Education Access for the Hyakushō Social Class | additive | good |  |
| country_strata_commoners_peasants_education_access_mult | Education Access for the Hyakushō Social Class | multiplicative | percent, good |  |
| country_strata_commoners_peasants_qualification_growth_add | Qualification Growth for the Hyakushō Social Class | additive | good |  |
| country_strata_commoners_peasants_qualification_growth_mult | Qualification Growth for the Hyakushō Social Class | multiplicative | percent, good |  |
| country_strata_commoners_peasants_qualification_growth_other_class_mult | Qualification Growth outside the Hyakushō Social Class for Hyakushō | multiplicative | percent, good |  |
| country_strata_commoners_peasants_qualification_growth_same_class_mult | Qualification Growth within Hyakushō Social Class | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_acceptance_max_add | Maximum Acceptance for the Chōnin Social Class | additive | bad |  |
| country_strata_commoners_townspeople_acceptance_min_add | Minimum Acceptance for the Chōnin Social Class | additive | good |  |
| country_strata_commoners_townspeople_cultural_acceptance_mult | Cultural Acceptance for the Chōnin Social Class | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_education_access_add | Education Access for the Chōnin Social Class | additive | good |  |
| country_strata_commoners_townspeople_education_access_mult | Education Access for the Chōnin Social Class | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_qualification_growth_add | Qualification Growth for the Chōnin Social Class | additive | good |  |
| country_strata_commoners_townspeople_qualification_growth_mult | Qualification Growth for the Chōnin Social Class | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_qualification_growth_other_class_mult | Qualification Growth outside the Chōnin Social Class for Chōnin | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_qualification_growth_same_class_mult | Qualification Growth within Chōnin Social Class | multiplicative | percent, good |  |
| country_strata_outcastes_acceptance_max_add | Maximum Acceptance for the Eta-Hinin Social Class | additive | bad |  |
| country_strata_outcastes_acceptance_min_add | Minimum Acceptance for the Eta-Hinin Social Class | additive | good |  |
| country_strata_outcastes_cultural_acceptance_mult | Cultural Acceptance for the Eta-Hinin Social Class | multiplicative | percent, good |  |
| country_strata_outcastes_education_access_add | Education Access for the Eta-Hinin Social Class | additive | good |  |
| country_strata_outcastes_education_access_mult | Education Access for the Eta-Hinin Social Class | multiplicative | percent, good |  |
| country_strata_outcastes_qualification_growth_add | Qualification Growth for the Eta-Hinin Social Class | additive | good |  |
| country_strata_outcastes_qualification_growth_mult | Qualification Growth for the Eta-Hinin Social Class | multiplicative | percent, good |  |
| country_strata_outcastes_qualification_growth_other_class_mult | Qualification Growth outside the Eta-Hinin Social Class for Eta-Hinin | multiplicative | percent, good |  |
| country_strata_outcastes_qualification_growth_same_class_mult | Qualification Growth within Eta-Hinin Social Class | multiplicative | percent, good |  |
| country_strata_religious_acceptance_max_add | Maximum Acceptance for the Jisha Social Class | additive | bad |  |
| country_strata_religious_acceptance_min_add | Minimum Acceptance for the Jisha Social Class | additive | good |  |
| country_strata_religious_cultural_acceptance_mult | Cultural Acceptance for the Jisha Social Class | multiplicative | percent, good |  |
| country_strata_religious_education_access_add | Education Access for the Jisha Social Class | additive | good |  |
| country_strata_religious_education_access_mult | Education Access for the Jisha Social Class | multiplicative | percent, good |  |
| country_strata_religious_qualification_growth_add | Qualification Growth for the Jisha Social Class | additive | good |  |
| country_strata_religious_qualification_growth_mult | Qualification Growth for the Jisha Social Class | multiplicative | percent, good |  |
| country_strata_religious_qualification_growth_other_class_mult | Qualification Growth outside the Jisha Social Class for Jisha | multiplicative | percent, good |  |
| country_strata_religious_qualification_growth_same_class_mult | Qualification Growth within Jisha Social Class | multiplicative | percent, good |  |
| country_strata_samurai_high_acceptance_max_add | Maximum Acceptance for the Upper Samurai Social Class | additive | bad |  |
| country_strata_samurai_high_acceptance_min_add | Minimum Acceptance for the Upper Samurai Social Class | additive | good |  |
| country_strata_samurai_high_cultural_acceptance_mult | Cultural Acceptance for the Upper Samurai Social Class | multiplicative | percent, good |  |
| country_strata_samurai_high_education_access_add | Education Access for the Upper Samurai Social Class | additive | good |  |
| country_strata_samurai_high_education_access_mult | Education Access for the Upper Samurai Social Class | multiplicative | percent, good |  |
| country_strata_samurai_high_qualification_growth_add | Qualification Growth for the Upper Samurai Social Class | additive | good |  |
| country_strata_samurai_high_qualification_growth_mult | Qualification Growth for the Upper Samurai Social Class | multiplicative | percent, good |  |
| country_strata_samurai_high_qualification_growth_other_class_mult | Qualification Growth outside the Upper Samurai Social Class for Upper Samurai | multiplicative | percent, good |  |
| country_strata_samurai_high_qualification_growth_same_class_mult | Qualification Growth within Upper Samurai Social Class | multiplicative | percent, good |  |
| country_strata_samurai_low_acceptance_max_add | Maximum Acceptance for the Lower Samurai Social Class | additive | bad |  |
| country_strata_samurai_low_acceptance_min_add | Minimum Acceptance for the Lower Samurai Social Class | additive | good |  |
| country_strata_samurai_low_cultural_acceptance_mult | Cultural Acceptance for the Lower Samurai Social Class | multiplicative | percent, good |  |
| country_strata_samurai_low_education_access_add | Education Access for the Lower Samurai Social Class | additive | good |  |
| country_strata_samurai_low_education_access_mult | Education Access for the Lower Samurai Social Class | multiplicative | percent, good |  |
| country_strata_samurai_low_qualification_growth_add | Qualification Growth for the Lower Samurai Social Class | additive | good |  |
| country_strata_samurai_low_qualification_growth_mult | Qualification Growth for the Lower Samurai Social Class | multiplicative | percent, good |  |
| country_strata_samurai_low_qualification_growth_other_class_mult | Qualification Growth outside the Lower Samurai Social Class for Lower Samurai | multiplicative | percent, good |  |
| country_strata_samurai_low_qualification_growth_same_class_mult | Qualification Growth within Lower Samurai Social Class | multiplicative | percent, good |  |
| country_subject_income_transfer_heathen_mult | Income transfer from Heathen Subjects | multiplicative | percent, good |  |
| country_subject_income_transfer_mult | Income transfer from Subjects | multiplicative | percent, good |  |
| country_supply_ship_construction_progress_max_add | Supply Ship Max Construction Progress | additive | good |  |
| country_supply_ship_construction_progress_max_mult | Supply Ship Max Construction Progress | multiplicative | percent, good |  |
| country_supply_ship_construction_ratio_add | Supply Ship Construction Ratio | additive | percent, good |  |
| country_support_independence_weekly_liberty_desire_add | Support Independence weekly Liberty Desire | additive | neutral |  |
| country_support_separatism_resistance_mult | Support Separatism Resistance | multiplicative | percent, good |  |
| country_support_separatism_strength_mult | Support Separatism Strength | multiplicative | percent, good |  |
| country_suppression_attraction_factor | Suppression impact on Political Movement attraction | multiplicative | percent, bad |  |
| country_suppression_cost_mult | Suppression cost | multiplicative | percent, bad |  |
| country_tax_income_add | Tax Income | additive | good |  |
| country_tech_group_research_speed_mult | Technology Research Speed as a group | multiplicative | percent, good |  |
| country_tech_research_speed_mult | Technology Research Speed | multiplicative | percent, good |  |
| country_tech_spread_add | Technology Spread | additive | good |  |
| country_tech_spread_mult | Technology Spread | multiplicative | percent, good |  |
| country_tension_decay_mult | Tension Decay | multiplicative | percent, good |  |
| country_treaty_leverage_generation_add | Leverage Generation from Treaty | additive | good |  |
| country_treaty_leverage_generation_mult | Leverage Generation from Treaty | multiplicative | percent, good |  |
| country_two_spains_conservative_drift_add | **The Two Spains** Conservative Progress | additive | good |  |
| country_two_spains_liberal_drift_add | **The Two Spains** Liberal Progress | additive | good |  |
| country_vaishyas_acceptance_max_add | Maximum Acceptance for the Vaishyas Social Class | additive | bad |  |
| country_vaishyas_acceptance_min_add | Minimum Acceptance for the Vaishyas Social Class | additive | good |  |
| country_vaishyas_cultural_acceptance_mult | Cultural Acceptance for the Vaishyas Social Class | multiplicative | percent, good |  |
| country_vaishyas_education_access_add | Education Access for the Vaishyas Social Class | additive | good |  |
| country_vaishyas_education_access_mult | Education Access for the Vaishyas Social Class | multiplicative | percent, good |  |
| country_vaishyas_qualification_growth_add | Qualification Growth for the Vaishyas Social Class | additive | good |  |
| country_vaishyas_qualification_growth_mult | Qualification Growth for the Vaishyas Social Class | multiplicative | percent, good |  |
| country_vaishyas_qualification_growth_other_class_mult | Qualification Growth outside the Vaishyas Social Class for Vaishyas | multiplicative | percent, good |  |
| country_vaishyas_qualification_growth_same_class_mult | Qualification Growth within Vaishyas Social Class | multiplicative | percent, good |  |
| country_voting_power_base_add | Political Strength per Vote | additive | neutral | Hardcoded Enables elections |
| country_voting_power_cultural_erasure_mult | Voting contribution of Political Strength for the Cultural Erasure Status | multiplicative | percent, neutral |  |
| country_voting_power_from_literacy_add | Political Strength from Literate Pops' Votes | additive | neutral | Hardcoded Enables elections |
| country_voting_power_full_acceptance_mult | Voting contribution of Political Strength for the Full Acceptance Status | multiplicative | percent, neutral |  |
| country_voting_power_mult | Political Strength per Vote | multiplicative | percent, neutral |  |
| country_voting_power_open_prejudice_mult | Voting contribution of Political Strength for the Open Prejudice Status | multiplicative | percent, neutral |  |
| country_voting_power_second_rate_citizen_mult | Voting contribution of Political Strength for the Second-class Citizen Status | multiplicative | percent, neutral |  |
| country_voting_power_violent_hostility_mult | Voting contribution of Political Strength for the Violent Hostility Status | multiplicative | percent, neutral |  |
| country_voting_power_wealth_threshold_add | Wealth Threshold for Voting | additive | neutral | Hardcoded Enables elections |
| country_wage_cultural_erasure_mult | Wage for the Cultural Erasure Status | multiplicative | percent, good |  |
| country_wage_full_acceptance_mult | Wage for the Full Acceptance Status | multiplicative | percent, good |  |
| country_wage_open_prejudice_mult | Wage for the Open Prejudice Status | multiplicative | percent, good |  |
| country_wage_second_rate_citizen_mult | Wage for the Second-class Citizen Status | multiplicative | percent, good |  |
| country_wage_violent_hostility_mult | Wage for the Violent Hostility Status | multiplicative | percent, good |  |
| country_war_exhaustion_casualties_mult | War Exhaustion from Casualties | multiplicative | percent, bad |  |
| country_weekly_innovation_add | Innovation | additive | good |  |
| country_weekly_innovation_max_add | Maximum Innovation Investment | additive | good |  |
| country_weekly_innovation_mult | Innovation | multiplicative | percent, good |  |
| country_yankee_and_dixie_cultures_obsessed_with_guns | Yankee and Dixie Cultures gain an Obsession with Small Arms | boolean | neutral |  |

### Country GUI script

Main article:
GUI script
| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessActiveDiplomaticPactTypes |  | Unknown | Category: const |
| AccessActiveDiplomaticPacts | ContextualDiplomaticActionType | Unknown | Category: const |
| AccessActiveDiplomaticPlays |  | Unknown | Category: const |
| AccessActiveEconomyLaws |  | Unknown | Category: const |
| AccessActiveHumanRightsLaws |  | Unknown | Category: const |
| AccessActiveInterestGroups |  | Unknown | Category: const |
| AccessActiveJournalEntries |  | Unknown | Category: const |
| AccessActiveLawFromGroup | LawGroup | Law | Category: const |
| AccessActiveNonPlayerObjectiveJournalEntries |  | Unknown | Category: const |
| AccessActiveOtherLaws |  | Unknown | Category: const |
| AccessActiveParties |  | Unknown | Category: const |
| AccessActivePinnedNonPlayerObjectiveJournalEntries |  | Unknown | Category: const |
| AccessActivePinnedPlayerObjectiveJournalEntries |  | Unknown | Category: const |
| AccessActivePlayerObjectiveJournalEntries |  | Unknown | Category: const |
| AccessActivePowerStructureLaws |  | Unknown | Category: const |
| AccessAdmirals |  | Unknown | Category: const |
| AccessAdmiralsOffer |  | Unknown | Category: const |
| AccessAllInterestGroups |  | Unknown | Category: const |
| AccessCapital |  | State | Category: const |
| AccessCivilWars |  | Unknown | Category: const |
| AccessConstructionQueue |  | Unknown | Category: const |
| AccessCurrentlyResearchedTechnology |  | Technology | Category: const |
| AccessDefinition |  | CountryDefinition | Category: const |
| AccessFirstMarket |  | Market | Category: const |
| AccessFormableCountries |  | Unknown | Category: const |
| AccessGenerals |  | Unknown | Category: const |
| AccessGeneralsOffer |  | Unknown | Category: const |
| AccessGovernment |  | GovernmentType | Category: const |
| AccessGovernmentConstructionQueue |  | Unknown | Category: const |
| AccessHeaviestJournalEntry |  | JournalEntry | Category: const |
| AccessHeir |  | Character | Category: const |
| AccessInactiveJournalEntries |  | Unknown | Category: const |
| AccessInstitutions |  | Unknown | Category: const |
| AccessInterestGroupsInGovernment |  | Unknown | Category: const |
| AccessInterestGroupsInOpposition |  | Unknown | Category: const |
| AccessInterests |  | Unknown | Category: const |
| AccessLandHQs |  | Unknown | Category: const |
| AccessLastElectionParties |  | Unknown | Category: const |
| AccessLawBeingEnacted |  | Law | Category: const |
| AccessLawsWithGovernmentOrMovementSupport |  | Unknown | Category: const |
| AccessLawsWithoutGovernmentOrMovementSupport |  | Unknown | Category: const |
| AccessMarginalInterestGroups |  | Unknown | Category: const |
| AccessModifier |  | Modifier | Category: const |
| AccessNavalHQs |  | Unknown | Category: const |
| AccessNonRevolutionaryPoliticalMovements |  | Unknown | Category: const |
| AccessNumResearchableTechnologies |  | int32 | Category: const |
| AccessOverlord |  | Country | Category: const |
| AccessPagedGovernmentConstructionQueue | int32 Unknown | Unknown | Category: const |
| AccessPagedPrivateConstructionQueue | int32 Unknown | Unknown | Category: const |
| AccessPoliticalMovements |  | Unknown | Category: const |
| AccessPopCultures |  | Unknown | Category: const |
| AccessPopCulturesSortedByPolStr |  | Unknown | Category: const |
| AccessPopCulturesSortedByPopulation |  | Unknown | Category: const |
| AccessPopReligionsSortedByPolStr |  | Unknown | Category: const |
| AccessPopReligionsSortedByPopulation |  | Unknown | Category: const |
| AccessPopTypes |  | Unknown | Category: const |
| AccessPopTypesSortedOnPolStr |  | Unknown | Category: const |
| AccessPopTypesSortedOnPopulation |  | Unknown | Category: const |
| AccessPowerBloc |  | PowerBloc | Category: const |
| AccessPrivateConstructionQueue |  | Unknown | Category: const |
| AccessReleasableCountries |  | Unknown | Category: const |
| AccessResearchableTechnologiesMilitary |  | Unknown | Category: const |
| AccessResearchableTechnologiesOther |  | Unknown | Category: const |
| AccessResearchableTechnologiesProduction |  | Unknown | Category: const |
| AccessResearchableTechnologiesSociety |  | Unknown | Category: const |
| AccessRuler |  | Character | Category: const |
| AccessSecessions |  | Unknown | Category: const |
| AccessSelf |  | Country | Category: const |
| AccessShippingLanes |  | Unknown | Category: const |
| AccessShippingOriginStates | Province | Unknown | Category: const |
| AccessShownCurrentlyConstructingGovernmentQueue |  | Unknown | Category: const |
| AccessShownCurrentlyConstructingPrivateQueue |  | Unknown | Category: const |
| AccessShownCurrentlyConstructingQueue |  | Unknown | Category: const |
| AccessStateReligion |  | Religion | Category: const |
| AccessStates |  | Unknown | Category: const |
| AccessStrategies |  | Unknown | Category: const |
| AccessTopOverlord |  | Country | Category: const |
| AccessTruces |  | Unknown | Category: const |
| AccessVioSovInterestedCountries | Country | Unknown | Category: const |
| AccessVioSovWars | Country | Unknown | Category: const |
| AccessVisibleJournalEntries |  | Unknown | Category: const |
| AccessWars |  | Unknown | Category: const |
| CalcBaseConstructionSpeed |  | CFixedPoint |  |
| CalcConscriptableBattalions |  | int32 |  |
| CalcCulturalTurmoil | Culture | CFixedPoint |  |
| CalcLibertyDesireLevel |  | LibertyDesireLevel |  |
| CalcMaxNumDeclaredInterests |  | int32 |  |
| CalcNumStatesInTurmoil |  | int32 |  |
| CalcRelativeUsedGovernmentConstruction |  | CFixedPoint |  |
| CalcRelativeUsedPrivateConstruction |  | CFixedPoint |  |
| CalcTurmoil |  | CFixedPoint |  |
| CalcUnusedConstruction |  | CFixedPoint |  |
| CalcUsedConstruction |  | CFixedPoint |  |
| CalcUsedGovernmentConstruction |  | CFixedPoint |  |
| CalcUsedPrivateConstruction |  | CFixedPoint |  |
| CanBuildingTypeBeMonopolized | BuildingType | bool |  |
| CanSignTreatyWith | Country | bool |  |
| CanTradeGoods | Unknown | bool |  |
| CreateCompany | CompanyType | Command |  |
| DeclareBankruptcy |  | Command |  |
| DeclareInterest | StrategicRegion | Command |  |
| DemobilizeAllArmies |  | Command |  |
| EstimatedConstructionQueueDuration |  | int32 |  |
| EstimatedGovernmentConstructionQueueDuration |  | int32 |  |
| EstimatedPrivateConstructionQueueDuration |  | int32 |  |
| Exists |  | bool |  |
| GetAIStrategiesDesc |  | CString | Category: nonconst |
| GetActiveConstructionProjectsDesc |  | CString | Category: nonconst |
| GetActiveLawFrom | Unknown | Law | Category: nonconst |
| GetActiveLawFromGroup | CString | Law | Category: nonconst |
| GetActivePeaceDealDesc |  | CString | Category: nonconst |
| GetAdditionalExpensesTrend |  | DataTrend | Category: nonconst |
| GetAdditionalIncomeTrend |  | DataTrend | Category: nonconst |
| GetAdditionalSOLFactorsDescAll |  | CString | Category: nonconst |
| GetAdditionalSOLFactorsDescMiddle |  | CString | Category: nonconst |
| GetAdditionalSOLFactorsDescPoor |  | CString | Category: nonconst |
| GetAdditionalSOLFactorsDescRich |  | CString | Category: nonconst |
| GetAdditionalSOLFactorsDescWithCulture | Culture | CString | Category: nonconst |
| GetAdditionalSOLFactorsDescWithCultureMiddle | Culture | CString | Category: nonconst |
| GetAdditionalSOLFactorsDescWithCulturePoor | Culture | CString | Category: nonconst |
| GetAdditionalSOLFactorsDescWithCultureRich | Culture | CString | Category: nonconst |
| GetAdjective |  | CString | Category: nonconst |
| GetAdjectiveNoFlag |  | CString | Category: nonconst |
| GetAdjectiveNoFormatting |  | CString | Category: nonconst |
| GetAllAcceptanceStatusSegments |  | Unknown | Category: nonconst |
| GetAllGeneralDiploActions |  | Unknown | Category: nonconst |
| GetAllOverlordDiploActions |  | Unknown | Category: nonconst |
| GetAllPowerBlocLeaderDiploActions |  | Unknown | Category: nonconst |
| GetAllPowerBlocMemberDiploActions |  | Unknown | Category: nonconst |
| GetAllSubjectDiploActions |  | Unknown | Category: nonconst |
| GetAllianceLikeTreatiesBrokenDesc | Country | CString | Category: nonconst |
| GetAllianceLikeTreatiesBrokenFromPlayDesc | DiplomaticPlay | CString | Category: nonconst |
| GetAllianceLikeTreatiesBrokenOnWarDesc | Country | CString | Category: nonconst |
| GetAllianceLikeTreatiesList | Unknown | CString | Category: nonconst |
| GetAltAdjective | CString | CString | Category: nonconst |
| GetAltAdjectiveNoFlag | CString | CString | Category: nonconst |
| GetAltAdjectiveNoFormatting | CString | CString | Category: nonconst |
| GetAltName | CString | CString | Category: nonconst |
| GetAltNameNoFlag | CString | CString | Category: nonconst |
| GetAltNameNoFormatting | CString | CString | Category: nonconst |
| GetArableLand |  | int32 | Category: nonconst |
| GetArableLandDesc |  | CString | Category: nonconst |
| GetArmiesBreakdown |  | CString | Category: nonconst |
| GetArmyPowerProjection |  | CFixedPoint | Category: nonconst |
| GetArmyPowerProjectionDesc |  | CString | Category: nonconst |
| GetArmyReadinessStatusDesc |  | CString | Category: nonconst |
| GetAttainableCompanies |  | Unknown | Category: nonconst |
| GetAttitudeColor | Unknown | CVector4f | Category: nonconst |
| GetAttitudeTowards | Country | AIAttitude | Category: nonconst |
| GetAvailableCompanies |  | Unknown | Category: nonconst |
| GetAvailableGeneralDiploActions |  | Unknown | Category: nonconst |
| GetAvailableOverlordDiploActions |  | Unknown | Category: nonconst |
| GetAvailablePowerBlocLeaderDiploActions |  | Unknown | Category: nonconst |
| GetAvailablePowerBlocMemberDiploActions |  | Unknown | Category: nonconst |
| GetAvailableSubjectDiploActions |  | Unknown | Category: nonconst |
| GetAverageExpectedStandardOfLivingWithCultureMiddle | Unknown | CFixedPoint | Category: nonconst |
| GetAverageExpectedStandardOfLivingWithCulturePoor | Unknown | CFixedPoint | Category: nonconst |
| GetAverageExpectedStandardOfLivingWithCultureRich | Unknown | CFixedPoint | Category: nonconst |
| GetAverageSoLByPoliticalStrength |  | CFixedPoint | Category: nonconst |
| GetAverageSoLByPopulation |  | CFixedPoint | Category: nonconst |
| GetAverageSoLByPopulationTrend |  | DataTrend | Category: nonconst |
| GetAverageSoLByPopulationWithCulture | Unknown | CFixedPoint | Category: nonconst |
| GetAverageSoLLowerTrend |  | DataTrend | Category: nonconst |
| GetAverageSoLMiddleTrend |  | DataTrend | Category: nonconst |
| GetAverageSoLUpperTrend |  | DataTrend | Category: nonconst |
| GetAverageStandardOfLivingMiddle |  | CFixedPoint | Category: nonconst |
| GetAverageStandardOfLivingPoor |  | CFixedPoint | Category: nonconst |
| GetAverageStandardOfLivingRich |  | CFixedPoint | Category: nonconst |
| GetAverageStandardOfLivingWithCultureMiddle | Unknown | CFixedPoint | Category: nonconst |
| GetAverageStandardOfLivingWithCulturePoor | Unknown | CFixedPoint | Category: nonconst |
| GetAverageStandardOfLivingWithCultureRich | Unknown | CFixedPoint | Category: nonconst |
| GetAverageStateTaxCollectionMult |  | CFixedPoint | Category: nonconst |
| GetAverageStateTaxCollectionMultBreakdown |  | CString | Category: nonconst |
| GetAverageTaxWaste |  | CFixedPoint | Category: nonconst |
| GetAverageTaxWasteBreakdown |  | CString | Category: nonconst |
| GetBalanceTrend |  | DataDynamicTrend | Category: nonconst |
| GetBaseConstructionSpeedDesc |  | CString | Category: nonconst |
| GetBaseWeeklyTechnologySpread |  | CFixedPoint | Category: nonconst |
| GetBaseWeeklyTechnologySpreadForTech | Unknown | CFixedPoint | Category: nonconst |
| GetBattalions |  | int32 | Category: nonconst |
| GetBattalionsDesc |  | CString | Category: nonconst |
| GetBattalionsMobilizing |  | int32 | Category: nonconst |
| GetBattalionsRanking |  | CString | Category: nonconst |
| GetBolsterDesc |  | CString | Category: nonconst |
| GetBolsteringCostDesc |  | CString | Category: nonconst |
| GetCanBuildingTypeBeMonopolizedDesc | BuildingType | CString | Category: nonconst |
| GetCanSignTreatyWithDesc | Country | CString | Category: nonconst |
| GetCapital |  | State | Category: nonconst |
| GetColonialGrowthDetails |  | CString | Category: nonconst |
| GetCompanies |  | Unknown | Category: nonconst |
| GetCompanyConstructionEfficiencyBonusFormatted |  | CString | Category: nonconst |
| GetCompanyThroughputBonusFormatted |  | CString | Category: nonconst |
| GetConscriptedBattalions |  | int32 | Category: nonconst |
| GetConscriptionRatio |  | CFixedPoint | Category: nonconst |
| GetConstructionGoodsExpenseTrend |  | DataTrend | Category: nonconst |
| GetConstructionGoodsExpenses |  | CFixedPoint | Category: nonconst |
| GetConstructionGoodsExpensesByGoodsDesc | Unknown | CString | Category: nonconst |
| GetConstructionGoodsExpensesDesc |  | CString | Category: nonconst |
| GetConstructionQueueDesc |  | CString | Category: nonconst |
| GetConstructionsInCountry | Country | Unknown | Category: nonconst |
| GetConsumptionTaxIncome |  | CFixedPoint | Category: nonconst |
| GetConsumptionTaxTrend |  | DataTrend | Category: nonconst |
| GetConsumptionTaxesDesc |  | CString | Category: nonconst |
| GetConvoyEffectDesc |  | CString | Category: nonconst |
| GetCountriesWithTreaties |  | Unknown | Category: nonconst |
| GetCountryScorePosition |  | int32 | Category: nonconst |
| GetCountryScorePositionDesc |  | CString | Category: nonconst |
| GetCreditRatio |  | CFixedPoint | Category: nonconst |
| GetCreditTooltip |  | CString | Category: nonconst |
| GetCulturePolStrAsPercentage | Culture | CFixedPoint | Category: nonconst |
| GetCulturePopulation | Culture | int64 | Category: nonconst |
| GetCurrentLeverage | Unknown | CFixedPoint | Category: nonconst |
| GetCurrentLeverageShare | PowerBloc | CFixedPoint | Category: nonconst |
| GetCurrentPowerStruggleMonth |  | int32 | Category: nonconst |
| GetCurrentlyResearchedTechnology |  | Technology | Category: nonconst |
| GetCurrentlySpreadingTechsDesc |  | CString | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetDailyRelationsProgress | Country | CFixedPoint | Category: nonconst |
| GetDaysUntilElection |  | int32 | Category: nonconst |
| GetDaysUntilRankLoss |  | int32 | Category: nonconst |
| GetDecisions |  | Unknown | Category: nonconst |
| GetDeclareBankruptcyDesc |  | CString | Category: nonconst |
| GetDecreasingInterestsDesc |  | CString | Category: nonconst |
| GetDeficitConvoyRatio |  | CFixedPoint | Category: nonconst |
| GetDeficitConvoyRatioForProgressBar |  | CFixedPoint | Category: nonconst |
| GetDeficitPowerRatio | Unknown | CFixedPoint | Category: nonconst |
| GetDeficitPowerRatioForProgressBar | CString | CFixedPoint | Category: nonconst |
| GetDefinition |  | CountryDefinition | Category: nonconst |
| GetDependents |  | int64 | Category: nonconst |
| GetDiplomaticAction | Unknown Unknown | DiplomaticAction | Category: nonconst |
| GetDiplomaticActionWithStates | Unknown Unknown Unknown Unknown | DiplomaticAction | Category: nonconst |
| GetDiplomaticPactsExpenseTrend |  | DataTrend | Category: nonconst |
| GetDiplomaticPactsIncomeTrend |  | DataTrend | Category: nonconst |
| GetDiplomaticStatusColor | Country | CVector4f | Category: nonconst |
| GetDividendsTaxTrend |  | DataTrend | Category: nonconst |
| GetDomesticallyOwnedGDP |  | CFixedPoint | Category: nonconst |
| GetDomesticallyOwnedGDPFraction |  | CFixedPoint | Category: nonconst |
| GetDraftTreaties |  | Unknown | Category: nonconst |
| GetDraftTreatiesWith | Unknown | Unknown | Category: nonconst |
| GetEconomicDependenceOn | Country | CString | Category: nonconst |
| GetEconomicDependenceOnDesc | Unknown | CString | Category: nonconst |
| GetEconomicDependenceOnRaw | Unknown | CFixedPoint | Category: nonconst |
| GetElection |  | Election | Category: nonconst |
| GetElectionPollTooltip |  | CString | Category: nonconst |
| GetElectoralConfidence |  | CFixedPoint | Category: nonconst |
| GetElectoralConfidenceEffectDesc |  | CString | Category: nonconst |
| GetEmployedWorkingAdults |  | int64 | Category: nonconst |
| GetEmptyAgitatorSlots |  | int32 | Category: nonconst |
| GetEnemyOccupation |  | CFixedPoint | Category: nonconst |
| GetEnforcedTreaties |  | Unknown | Category: nonconst |
| GetEnforcedTreatiesWith | Country | Unknown | Category: nonconst |
| GetEnforcedTreatiesWithDesc | Unknown | CString | Category: nonconst |
| GetEventsByCategory | CString | Unknown | Category: nonconst |
| GetExcessConvoyRatio |  | CFixedPoint | Category: nonconst |
| GetExcessConvoyRatioForProgressBar |  | CFixedPoint | Category: nonconst |
| GetExcessPowerRatio | Unknown | CFixedPoint | Category: nonconst |
| GetExcessPowerRatioForProgressBar | CString | CFixedPoint | Category: nonconst |
| GetExpectedSOLFactorsDescAll |  | CString | Category: nonconst |
| GetExpectedSOLFactorsDescMiddle |  | CString | Category: nonconst |
| GetExpectedSOLFactorsDescPoor |  | CString | Category: nonconst |
| GetExpectedSOLFactorsDescRich |  | CString | Category: nonconst |
| GetExpectedSOLFactorsDescWithCulture | Unknown | CString | Category: nonconst |
| GetExpectedSoLByPopulation |  | CFixedPoint | Category: nonconst |
| GetExpectedStandardOfLivingMiddle |  | CFixedPoint | Category: nonconst |
| GetExpectedStandardOfLivingPoor |  | CFixedPoint | Category: nonconst |
| GetExpectedStandardOfLivingRich |  | CFixedPoint | Category: nonconst |
| GetExpensesBreakdown |  | CString | Category: nonconst |
| GetExportSubventionsDescHigh | Goods | CString | Category: nonconst |
| GetExportSubventionsDescLow | Goods | CString | Category: nonconst |
| GetExportSubventionsDescMax | Goods | CString | Category: nonconst |
| GetExportTariffsDescHigh | Goods | CString | Category: nonconst |
| GetExportTariffsDescLow | Goods | CString | Category: nonconst |
| GetExportTariffsDescMax | Goods | CString | Category: nonconst |
| GetExportTariffsDescNone | Goods | CString | Category: nonconst |
| GetExportedAmount | Unknown | CFixedPoint | Category: nonconst |
| GetExports |  | Unknown | Category: nonconst |
| GetFirstPrimaryCulture |  | Culture | Category: nonconst |
| GetFlag |  | CoatOfArms | Category: nonconst |
| GetFlagTextIcon |  | CString | Category: nonconst |
| GetFlavorText |  | CString | Category: nonconst |
| GetFleetsBreakdown |  | CString | Category: nonconst |
| GetFlotillasRanking |  | CString | Category: nonconst |
| GetForeignOwnedGDP |  | CFixedPoint | Category: nonconst |
| GetForeignOwnedGDPDesc |  | CString | Category: nonconst |
| GetForeignOwnedGDPFraction |  | CFixedPoint | Category: nonconst |
| GetFormattedStandardOfLivingAll |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingAllWithCulture | Culture | CString | Category: nonconst |
| GetFormattedStandardOfLivingLabelAll |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingLabelAllWithCulture | Culture | CString | Category: nonconst |
| GetFormattedStandardOfLivingLabelMiddle |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingLabelMiddleWithCulture | Culture | CString | Category: nonconst |
| GetFormattedStandardOfLivingLabelPoor |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingLabelPoorWithCulture | Culture | CString | Category: nonconst |
| GetFormattedStandardOfLivingLabelRich |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingLabelRichWithCulture | Culture | CString | Category: nonconst |
| GetFormattedStandardOfLivingMiddle |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingMiddleWithCulture | Culture | CString | Category: nonconst |
| GetFormattedStandardOfLivingPoor |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingPoorWithCulture | Culture | CString | Category: nonconst |
| GetFormattedStandardOfLivingRich |  | CString | Category: nonconst |
| GetFormattedStandardOfLivingRichWithCulture | Culture | CString | Category: nonconst |
| GetFreeArableLand |  | int32 | Category: nonconst |
| GetGDP |  | CFixedPoint | Category: nonconst |
| GetGDPOwnedInForeignCountries |  | CFixedPoint | Category: nonconst |
| GetGDPOwnedInForeignCountriesDesc |  | CString | Category: nonconst |
| GetGDPPerCapita |  | CFixedPoint | Category: nonconst |
| GetGDPPerCapitaRanking |  | CString | Category: nonconst |
| GetGDPRanking |  | CString | Category: nonconst |
| GetGDPTrend |  | DataTrend | Category: nonconst |
| GetGDPWithOwnershipsInForeignCountries |  | CFixedPoint | Category: nonconst |
| GetGameOverDateString |  | CString | Category: nonconst |
| GetGdpRatioOwnedBy | Unknown | CString | Category: nonconst |
| GetGdpRatioOwnedByDesc | Unknown | CString | Category: nonconst |
| GetGdpRatioOwnedByRaw | Unknown | CFixedPoint | Category: nonconst |
| GetGoldProgressDesc |  | CString | Category: nonconst |
| GetGoldReserveLimit |  | CFixedPoint | Category: nonconst |
| GetGoldReserveLimitDesc |  | CString | Category: nonconst |
| GetGoldReserveRatio |  | CFixedPoint | Category: nonconst |
| GetGoldReserves |  | CFixedPoint | Category: nonconst |
| GetGoldReservesTrend |  | DataDynamicTrend | Category: nonconst |
| GetGoodsLeaderboardDesc |  | CString | Category: nonconst |
| GetGovernment |  | GovernmentType | Category: nonconst |
| GetGovernmentConstructionGoodsExpenses |  | CFixedPoint | Category: nonconst |
| GetGovernmentConstructionGoodsExpensesByGoodsDesc |  | CString | Category: nonconst |
| GetGovernmentGoodsExpenseTrend |  | DataTrend | Category: nonconst |
| GetGovernmentGoodsExpenses |  | CFixedPoint | Category: nonconst |
| GetGovernmentGoodsExpensesByGoodsDesc |  | CString | Category: nonconst |
| GetGovernmentGoodsExpensesDesc |  | CString | Category: nonconst |
| GetGovernmentIGsDesc |  | CString | Category: nonconst |
| GetGovernmentInterestGroupsDesc |  | CString | Category: nonconst |
| GetGovernmentInterestGroupsPopulationDesc |  | CString | Category: nonconst |
| GetGovernmentLegitimacy |  | int32 | Category: nonconst |
| GetGovernmentLegitimacyDesc |  | CString | Category: nonconst |
| GetGovernmentLegitimacyLevel |  | LegitimacyLevel | Category: nonconst |
| GetGovernmentSelfDebt |  | CFixedPoint | Category: nonconst |
| GetGovernmentSelfDebtFraction |  | CFixedPoint | Category: nonconst |
| GetGovernmentShareDividendsTrend |  | DataTrend | Category: nonconst |
| GetGovernmentShareLossesTrend |  | DataTrend | Category: nonconst |
| GetGovernmentSlavesExpenseTrend |  | DataTrend | Category: nonconst |
| GetGovernmentSlavesExpenses |  | CFixedPoint | Category: nonconst |
| GetGovernmentSlavesExpensesDesc |  | CString | Category: nonconst |
| GetGovernmentWageLevelDescHigh |  | CString | Category: nonconst |
| GetGovernmentWageLevelDescLow |  | CString | Category: nonconst |
| GetGovernmentWageLevelDescMedium |  | CString | Category: nonconst |
| GetGovernmentWageLevelDescVeryHigh |  | CString | Category: nonconst |
| GetGovernmentWageLevelDescVeryLow |  | CString | Category: nonconst |
| GetGovernmentWagesExpenseTrend |  | DataTrend | Category: nonconst |
| GetGovernmentWagesExpenses |  | CFixedPoint | Category: nonconst |
| GetGovernmentWagesExpensesDesc |  | CString | Category: nonconst |
| GetGroupsForActiveJournalEntries |  | Unknown | Category: nonconst |
| GetGroupsForInActiveJournalEntries |  | Unknown | Category: nonconst |
| GetGrowingCivilWars |  | Unknown | Category: nonconst |
| GetHeir |  | Character | Category: nonconst |
| GetHighestPossibleRank |  | CString | Category: nonconst |
| GetID |  | int32 | Category: nonconst |
| GetIDString |  | CString | Category: nonconst |
| GetIGApprovalFromLoyalistsBreakdown |  | CString | Category: nonconst |
| GetIGApprovalFromRadicalsBreakdown |  | CString | Category: nonconst |
| GetImportSubventionsDescHigh | Goods | CString | Category: nonconst |
| GetImportSubventionsDescLow | Goods | CString | Category: nonconst |
| GetImportSubventionsDescMax | Goods | CString | Category: nonconst |
| GetImportTariffsDescHigh | Goods | CString | Category: nonconst |
| GetImportTariffsDescLow | Goods | CString | Category: nonconst |
| GetImportTariffsDescMax | Goods | CString | Category: nonconst |
| GetImportTariffsDescNone | Goods | CString | Category: nonconst |
| GetImportedAmount | Unknown | CFixedPoint | Category: nonconst |
| GetImports |  | Unknown | Category: nonconst |
| GetInDefaultEffectsDesc |  | CString | Category: nonconst |
| GetInForceTreaties |  | Unknown | Category: nonconst |
| GetInactiveConstructionProjectsDesc |  | CString | Category: nonconst |
| GetInactivePopulation |  | int64 | Category: nonconst |
| GetInactivePopulationDesc |  | CString | Category: nonconst |
| GetIncomeBreakdown |  | CString | Category: nonconst |
| GetIncomeTaxIncome |  | CFixedPoint | Category: nonconst |
| GetIncorporatedLiteracyRanking |  | CString | Category: nonconst |
| GetIncorporatedLiteracyRate |  | CFixedPoint | Category: nonconst |
| GetIncorporatedLiteracyTrend |  | DataTrend | Category: nonconst |
| GetIncorporatedPopulation |  | int64 | Category: nonconst |
| GetIncorporatedStatesLawCostDesc |  | CString | Category: nonconst |
| GetIndependentInterestGroupsInGovernment |  | Unknown | Category: nonconst |
| GetIndependentInterestGroupsInOpposition |  | Unknown | Category: nonconst |
| GetInfamy |  | CFixedPoint | Category: nonconst |
| GetInfamyColor |  | CVector4f | Category: nonconst |
| GetInfamyDesc |  | CString | Category: nonconst |
| GetInfamyIconTexture |  | Unknown | Category: nonconst |
| GetInfamyLabel |  | CString | Category: nonconst |
| GetInstitutionInvestment |  | CFixedPoint | Category: nonconst |
| GetInstitutionInvestmentBureaucracyCost |  | CFixedPoint | Category: nonconst |
| GetInstitutionInvestmentBureaucracyCostDesc |  | CString | Category: nonconst |
| GetInstitutionInvestmentBureaucracyFactor |  | CFixedPoint | Category: nonconst |
| GetInstitutionInvestmentBureaucracyFactorDesc |  | CString | Category: nonconst |
| GetInstitutionInvestmentDesc |  | CString | Category: nonconst |
| GetInstitutionsSummary |  | CString | Category: nonconst |
| GetInsurrectionaryIGsDesc |  | CString | Category: nonconst |
| GetInterestExpenseTrend |  | DataTrend | Category: nonconst |
| GetInterestGroupOfType | Unknown | InterestGroup | Category: nonconst |
| GetInterestPayment |  | CFixedPoint | Category: nonconst |
| GetInterestRateTooltip |  | CString | Category: nonconst |
| GetInvestmentFundTrend |  | DataTrend | Category: nonconst |
| GetInvestmentGdpFractionInCountry | Country | CFixedPoint | Category: nonconst |
| GetInvestmentIncome |  | CFixedPoint | Category: nonconst |
| GetInvestmentIncomeTrend |  | DataTrend | Category: nonconst |
| GetInvestmentLevelsInCountry | Country | int32 | Category: nonconst |
| GetInvestmentPool |  | CFixedPoint | Category: nonconst |
| GetInvestmentPoolChange |  | CFixedPoint | Category: nonconst |
| GetInvestmentPoolChangeFromConstructionDesc |  | CString | Category: nonconst |
| GetInvestmentPoolChangeFromInvestmentBreakdown |  | CString | Category: nonconst |
| GetInvestmentPoolChangeFromInvestmentDesc |  | CString | Category: nonconst |
| GetInvestmentPoolPredictedNextBuildingDesc |  | CString | Category: nonconst |
| GetJournalEntry | Unknown | JournalEntry | Category: nonconst |
| GetKillRateNavy |  | CFixedPoint | Category: nonconst |
| GetLabel | Country | CString | Category: nonconst |
| GetLackOfAutonomousInvestmentReasonDesc |  | CString | Category: nonconst |
| GetLastCatalystExpiryDate | Country DiplomaticCatalyst | CString | Category: nonconst |
| GetLastElectionResultsTooltip |  | CString | Category: nonconst |
| GetLawBeingEnacted |  | Law | Category: nonconst |
| GetLawBeingEnactedFromGroup | Unknown | Law | Category: nonconst |
| GetLawEnactmentProgress |  | CFixedPoint | Category: nonconst |
| GetLawEnactmentProgressDesc |  | CString | Category: nonconst |
| GetLeaderReligionPercentage |  | CFixedPoint | Category: nonconst |
| GetLeverageAdvantage | PowerBloc | CFixedPoint | Category: nonconst |
| GetLeverageAdvantageTarget | PowerBloc | CFixedPoint | Category: nonconst |
| GetLeverageBreakdown |  | CString | Category: nonconst |
| GetLeverageComparisonDesc | PowerBloc | CString | Category: nonconst |
| GetLeverageGain | PowerBloc | CFixedPoint | Category: nonconst |
| GetLeverageGainBreakdown | PowerBloc | CString | Category: nonconst |
| GetLeverageResistance |  | CFixedPoint | Category: nonconst |
| GetLeverageTarget | PowerBloc | CFixedPoint | Category: nonconst |
| GetLeverageTooltip |  | CString | Category: nonconst |
| GetLibertyDesireLevelLabel |  | CString | Category: nonconst |
| GetLibertyDesireRaw |  | CFixedPoint | Category: nonconst |
| GetLimitedMassMigrationCountryAttraction |  | CFixedPoint | Category: nonconst |
| GetLobbyJournalEntries |  | Unknown | Category: nonconst |
| GetLowerStrataPopulationTrend |  | DataTrend | Category: nonconst |
| GetLoyalistsChangeSummary |  | CString | Category: nonconst |
| GetLoyalistsDecreaseBreakdown |  | CString | Category: nonconst |
| GetLoyalistsIncreaseBreakdown |  | CString | Category: nonconst |
| GetLoyalistsOrRadicalsGainedFromLegitimacy |  | int64 | Category: nonconst |
| GetLoyalistsOrRadicalsGainedFromLegitimacyModifierDescription | Unknown | CString | Category: nonconst |
| GetLoyalistsSummaryDesc |  | CString | Category: nonconst |
| GetLoyalistsTrend |  | DataTrend | Category: nonconst |
| GetLoyaltiesGain |  | CFixedPoint | Category: nonconst |
| GetMapColor |  | CVector4f | Category: nonconst |
| GetMarginalAndInactivePopulationInCountryAsPercentage |  | float | Category: nonconst |
| GetMarginalCloutInCountryAsPercentage |  | float | Category: nonconst |
| GetMarginalInterestGroupsDesc |  | CString | Category: nonconst |
| GetMarginalInterestGroupsPopulationDesc |  | CString | Category: nonconst |
| GetMarket |  | Market | Category: nonconst |
| GetMarketOwnerName |  | CString | Category: nonconst |
| GetMassMigrationAttractionBreakdown |  | CString | Category: nonconst |
| GetMassMigrationAttractionDesc |  | CString | Category: nonconst |
| GetMaxCloutOrPopulationPercentage |  | float | Category: nonconst |
| GetMaxCredit |  | CFixedPoint | Category: nonconst |
| GetMaxFreeCharters |  | int32 | Category: nonconst |
| GetMaxLawEnactmentSetbacks |  | int32 | Category: nonconst |
| GetMaxNumCompanies |  | int32 | Category: nonconst |
| GetMaxNumCompaniesDesc |  | CString | Category: nonconst |
| GetMaxNumDeclaredInterestsBreakdown |  | CString | Category: nonconst |
| GetMaxPowerStruggleMonth |  | int32 | Category: nonconst |
| GetMaxWeeklyTechnologyProgressForTech | Unknown | CFixedPoint | Category: nonconst |
| GetMaxWeeklyTechnologySpread |  | CFixedPoint | Category: nonconst |
| GetMaxWeeklyTechnologySpreadForTech | Unknown | CFixedPoint | Category: nonconst |
| GetMiddleStrataPopulationTrend |  | DataTrend | Category: nonconst |
| GetMilitaryFormationsArmy |  | Unknown | Category: nonconst |
| GetMilitaryFormationsFleet |  | Unknown | Category: nonconst |
| GetMilitaryGoodsExpenseTrend |  | DataTrend | Category: nonconst |
| GetMilitaryGoodsExpenses |  | CFixedPoint | Category: nonconst |
| GetMilitaryGoodsExpensesByGoodsDesc |  | CString | Category: nonconst |
| GetMilitaryGoodsExpensesDesc |  | CString | Category: nonconst |
| GetMilitaryInterfaceColor |  | CVector4f | Category: nonconst |
| GetMilitarySlavesExpenseTrend |  | DataTrend | Category: nonconst |
| GetMilitarySlavesExpenses |  | CFixedPoint | Category: nonconst |
| GetMilitarySlavesExpensesDesc |  | CString | Category: nonconst |
| GetMilitaryWageLevelDescHigh |  | CString | Category: nonconst |
| GetMilitaryWageLevelDescLow |  | CString | Category: nonconst |
| GetMilitaryWageLevelDescMedium |  | CString | Category: nonconst |
| GetMilitaryWageLevelDescVeryHigh |  | CString | Category: nonconst |
| GetMilitaryWageLevelDescVeryLow |  | CString | Category: nonconst |
| GetMilitaryWagesExpenseTrend |  | DataTrend | Category: nonconst |
| GetMilitaryWagesExpenses |  | CFixedPoint | Category: nonconst |
| GetMilitaryWagesExpensesDesc |  | CString | Category: nonconst |
| GetMinWeeklyTechnologyProgressForTech | Technology | CFixedPoint | Category: nonconst |
| GetMinWeeklyTechnologySpread |  | CFixedPoint | Category: nonconst |
| GetMinWeeklyTechnologySpreadForTech | Unknown | CFixedPoint | Category: nonconst |
| GetMintingTrend |  | DataTrend | Category: nonconst |
| GetMobilizationRatio |  | CFixedPoint | Category: nonconst |
| GetModifier |  | Modifier | Category: nonconst |
| GetMoveCapitalEffectsDesc |  | CString | Category: nonconst |
| GetMoveMarketCapitalEffectsDesc |  | CString | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFlag |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetNavyPowerProjection |  | CFixedPoint | Category: nonconst |
| GetNavyPowerProjectionDesc |  | CString | Category: nonconst |
| GetNegotiatingInterestGroup |  | InterestGroup | Category: nonconst |
| GetNextElectionDate |  | CString | Category: nonconst |
| GetNextRank |  | CString | Category: nonconst |
| GetNextRankDesc |  | CString | Category: nonconst |
| GetNextRankNumber |  | int32 | Category: nonconst |
| GetNextStartOfCampaignDate |  | CString | Category: nonconst |
| GetNonPotentialDiploPlays |  | Unknown | Category: nonconst |
| GetNonSubjectDiplomaticPactsWith | Country | Unknown | Category: nonconst |
| GetNumActiveConstructionQueueElements |  | int32 | Category: nonconst |
| GetNumActiveGovernmentConstructionQueueElements |  | int32 | Category: nonconst |
| GetNumActivePrivateConstructionQueueElements |  | int32 | Category: nonconst |
| GetNumActiveShownConstructionQueueElements |  | int32 | Category: nonconst |
| GetNumActiveShownGovernmentConstructionQueueElements |  | int32 | Category: nonconst |
| GetNumActiveShownPrivateConstructionQueueElements |  | int32 | Category: nonconst |
| GetNumAvailableCompanies |  | int32 | Category: nonconst |
| GetNumAvailableConvoys |  | int32 | Category: nonconst |
| GetNumAvailableNegotiations |  | int32 | Category: nonconst |
| GetNumBattalions |  | int32 | Category: nonconst |
| GetNumBuildingsInConstructionQueueInState | State | int32 | Category: nonconst |
| GetNumBuildingsUnderConstructionInState | State | int32 | Category: nonconst |
| GetNumCombatUnits |  | int32 | Category: nonconst |
| GetNumCompanies |  | int32 | Category: nonconst |
| GetNumConvoys |  | int32 | Category: nonconst |
| GetNumConvoysDamagedDesc |  | CString | Category: nonconst |
| GetNumConvoysDesc |  | CString | Category: nonconst |
| GetNumDamagedConvoys |  | int32 | Category: nonconst |
| GetNumDeclaredInterests |  | int32 | Category: nonconst |
| GetNumFlotillas |  | int32 | Category: nonconst |
| GetNumGovernmentConstructionsInQueue |  | int32 | Category: nonconst |
| GetNumInactiveAndNonShownGovernmentConstructionQueueElements |  | int32 | Category: nonconst |
| GetNumInactiveAndNonShownPrivateConstructionQueueElements |  | int32 | Category: nonconst |
| GetNumInactiveConstructionQueueElements |  | int32 | Category: nonconst |
| GetNumInactiveGovernmentConstructionQueueElements |  | int32 | Category: nonconst |
| GetNumInactivePrivateConstructionQueueElements |  | int32 | Category: nonconst |
| GetNumIncorporatedLiteratePops |  | int64 | Category: nonconst |
| GetNumIncorporatedStates |  | int32 | Category: nonconst |
| GetNumIncorporatedStatesDesc |  | CString | Category: nonconst |
| GetNumInsufficientTaxCapacityStates |  | int32 | Category: nonconst |
| GetNumInterestGroupMembers |  | int64 | Category: nonconst |
| GetNumIsolatedStates |  | int32 | Category: nonconst |
| GetNumLowMarketAccessStates |  | int32 | Category: nonconst |
| GetNumLoyalists |  | int64 | Category: nonconst |
| GetNumNeutrals |  | int64 | Category: nonconst |
| GetNumPoliticallyInactiveLoyalists |  | int64 | Category: nonconst |
| GetNumPoliticallyInactiveNeutrals |  | int64 | Category: nonconst |
| GetNumPoliticallyInactiveRadicals |  | int64 | Category: nonconst |
| GetNumPrivateConstructionsInQueue |  | int32 | Category: nonconst |
| GetNumRadicals |  | int64 | Category: nonconst |
| GetNumStatesThatCanBeIncorporated |  | int32 | Category: nonconst |
| GetNumStatesWithConstruction |  | int32 | Category: nonconst |
| GetNumStatesWithoutConstruction |  | int32 | Category: nonconst |
| GetNumTotalLiteratePops |  | int64 | Category: nonconst |
| GetNumTurmoilStates |  | int32 | Category: nonconst |
| GetNumUnincorporatedStates |  | int32 | Category: nonconst |
| GetNumUnincorporatedStatesDesc |  | CString | Category: nonconst |
| GetNumUsableConvoys |  | int32 | Category: nonconst |
| GetNumberOfActiveConscriptionCenters |  | int32 | Category: nonconst |
| GetNumberOfInactiveConscriptionCenters |  | int32 | Category: nonconst |
| GetObjective |  | Objective | Category: nonconst |
| GetObligationFromExpirationDate | Country | CString | Category: nonconst |
| GetObligationFromExpirationDesc | Country | CString | Category: nonconst |
| GetObligationToExpirationDate | Country | CString | Category: nonconst |
| GetObligationToExpirationDesc | Country | CString | Category: nonconst |
| GetObligationsOwedFrom |  | Unknown | Category: nonconst |
| GetObligationsOwedTo |  | Unknown | Category: nonconst |
| GetOppositionInterestGroupsDesc |  | CString | Category: nonconst |
| GetOppositionInterestGroupsPopulationDesc |  | CString | Category: nonconst |
| GetOtherPowerBlocWithHighestLeverage | Unknown | PowerBloc | Category: nonconst |
| GetOverlord |  | Country | Category: nonconst |
| GetOwningCompany |  | Company | Category: nonconst |
| GetPartiesInGovernment |  | Unknown | Category: nonconst |
| GetPartiesInOpposition |  | Unknown | Category: nonconst |
| GetPeopleAbroad |  | int64 | Category: nonconst |
| GetPlayedByDesc |  | CString | Category: nonconst |
| GetPlayer |  | Player | Category: nonconst |
| GetPoliticalLobbies |  | Unknown | Category: nonconst |
| GetPoliticallyInvolvedPercentage |  | CFixedPoint | Category: nonconst |
| GetPoliticallyInvolvedPopulation |  | int64 | Category: nonconst |
| GetPoliticallyInvolvedPopulationDesc |  | CString | Category: nonconst |
| GetPollTaxIncome |  | CFixedPoint | Category: nonconst |
| GetPollTaxTrend |  | DataTrend | Category: nonconst |
| GetPopConsumptionDependenceOn | Unknown | CString | Category: nonconst |
| GetPopConsumptionDependenceOnDesc | Unknown | CString | Category: nonconst |
| GetPopConsumptionDependenceOnRaw | Unknown | CFixedPoint | Category: nonconst |
| GetPopGrowthDesc |  | CString | Category: nonconst |
| GetPopReligions |  | Unknown | Category: nonconst |
| GetPopulationRanking |  | CString | Category: nonconst |
| GetPopulationTrend |  | DataTrend | Category: nonconst |
| GetPotentialCompanies |  | Unknown | Category: nonconst |
| GetPotentialDiploPlays |  | Unknown | Category: nonconst |
| GetPotentialGeneralDiploActions |  | Unknown | Category: nonconst |
| GetPotentialInvestors |  | Unknown | Category: nonconst |
| GetPotentialLabor |  | int64 | Category: nonconst |
| GetPotentialOverlordDiploActions |  | Unknown | Category: nonconst |
| GetPotentialPowerBlocLeaderDiploActions |  | Unknown | Category: nonconst |
| GetPotentialPowerBlocMemberDiploActions |  | Unknown | Category: nonconst |
| GetPotentialSubjectDiploActions |  | Unknown | Category: nonconst |
| GetPowerBloc |  | PowerBloc | Category: nonconst |
| GetPowerBlocExpenseDesc |  | CString | Category: nonconst |
| GetPowerBlocExpenseRaw |  | CFixedPoint | Category: nonconst |
| GetPowerBlocExpenseTrend |  | DataTrend | Category: nonconst |
| GetPowerBlocIncomeDesc |  | CString | Category: nonconst |
| GetPowerBlocIncomeRaw |  | CFixedPoint | Category: nonconst |
| GetPowerBlocIncomeTrend |  | DataTrend | Category: nonconst |
| GetPowerBlocNonMemberCountryTooltip |  | CString | Category: nonconst |
| GetPowerBlocWithHighestLeverage |  | PowerBloc | Category: nonconst |
| GetPowerBlocsTotalLeverageShare |  | CFixedPoint | Category: nonconst |
| GetPowerBlocsWithLeverage |  | Unknown | Category: nonconst |
| GetPowerDelta | CString | CFixedPoint | Category: nonconst |
| GetPowerDeltaIcon | CString | CString | Category: nonconst |
| GetPowerExpensesString | CString | CString | Category: nonconst |
| GetPowerIncome | CString | CFixedPoint | Category: nonconst |
| GetPowerIncomeString | CString | CString | Category: nonconst |
| GetPowerTooltip | CString | CString | Category: nonconst |
| GetPredictedBalanceFromBankruptcy |  | CFixedPoint | Category: nonconst |
| GetPrestige |  | int32 | Category: nonconst |
| GetPrestigeDesc |  | CString | Category: nonconst |
| GetPrestigeForCurrentRank |  | int32 | Category: nonconst |
| GetPrestigeForNextRank |  | int32 | Category: nonconst |
| GetPrestigeGoodsLeaderboardDesc |  | CString | Category: nonconst |
| GetPrestigeToMaintainRank |  | int32 | Category: nonconst |
| GetPrestigeTrend |  | DataTrend | Category: nonconst |
| GetPreviousAttitudeTowards | Unknown | AIAttitude | Category: nonconst |
| GetPreviousAutonomousInvestmentsDesc |  | CString | Category: nonconst |
| GetPreviousRank |  | CString | Category: nonconst |
| GetPriceReportDesc |  | CString | Category: nonconst |
| GetPrimaryCulturesDesc |  | CString | Category: nonconst |
| GetPrincipal |  | CFixedPoint | Category: nonconst |
| GetPrivateConstructionGoodsExpenses |  | CFixedPoint | Category: nonconst |
| GetPrivateConstructionGoodsExpensesByGoodsDesc |  | CString | Category: nonconst |
| GetPrivateConstructionQueueDesc |  | CString | Category: nonconst |
| GetRadicalizationFromBankruptcy |  | int64 | Category: nonconst |
| GetRadicalsChangeSummary |  | CString | Category: nonconst |
| GetRadicalsDecreaseBreakdown |  | CString | Category: nonconst |
| GetRadicalsIncreaseBreakdown |  | CString | Category: nonconst |
| GetRadicalsLoyalistsChangeStartDate |  | CString | Category: nonconst |
| GetRadicalsSummaryDesc |  | CString | Category: nonconst |
| GetRadicalsTrend |  | DataTrend | Category: nonconst |
| GetRank |  | CString | Category: nonconst |
| GetRankDesc |  | CString | Category: nonconst |
| GetRankIconIndex |  | int32 | Category: nonconst |
| GetRankModifier |  | Modifier | Category: nonconst |
| GetRankNumber |  | int32 | Category: nonconst |
| GetRankProgress |  | float | Category: nonconst |
| GetRankTooltip |  | CString | Category: nonconst |
| GetRecentPartiesDesc |  | CString | Category: nonconst |
| GetRegularBattalions |  | int32 | Category: nonconst |
| GetReinforcementRateArmy |  | CFixedPoint | Category: nonconst |
| GetReinforcementRateNavy |  | CFixedPoint | Category: nonconst |
| GetRelationsColor | Unknown | CVector4f | Category: nonconst |
| GetRelationsIconTexture | Country | Unknown | Category: nonconst |
| GetRelationsProgress | Unknown | CFixedPoint | Category: nonconst |
| GetRelationsProgressDesc | Unknown | CString | Category: nonconst |
| GetRelationsTooltip | Country | CString | Category: nonconst |
| GetRelationsWith | Country | int32 | Category: nonconst |
| GetRelationsWithDesc | Country | CString | Category: nonconst |
| GetRelativePrestige | Country | CFixedPoint | Category: nonconst |
| GetRemainingCredit |  | CFixedPoint | Category: nonconst |
| GetRemainingDaysForFreeGovernmentReformRaw |  | int32 | Category: nonconst |
| GetRequiredConvoys |  | int32 | Category: nonconst |
| GetRequiredConvoysBreakdown |  | CString | Category: nonconst |
| GetResearchQueueBottom |  | Unknown | Category: nonconst |
| GetResearchQueueTop |  | Unknown | Category: nonconst |
| GetRuler |  | Character | Category: nonconst |
| GetRulingIGsDesc |  | CString | Category: nonconst |
| GetSOLDescForAllStratas |  | CString | Category: nonconst |
| GetSalariedWorkingAdults |  | int64 | Category: nonconst |
| GetSeaNodesMightBeConvoyRaidedInDesc |  | CString | Category: nonconst |
| GetSelectedLaw |  | Law | Category: nonconst |
| GetSocialHierarchy |  | SocialHierarchy | Category: nonconst |
| GetSpecialSocialHierarchy |  | SocialHierarchy | Category: nonconst |
| GetStandardOfLivingRanking |  | CString | Category: nonconst |
| GetStateOwnedBuildingsBureaucracyCostForLevels | int32 | CFixedPoint | Category: nonconst |
| GetStateReligion |  | Religion | Category: nonconst |
| GetStatesInTurmoilBreakdown |  | CString | Category: nonconst |
| GetStatus | Country | CString | Category: nonconst |
| GetStrategicObjectives |  | Unknown | Category: nonconst |
| GetStrategicRegions |  | Unknown | Category: nonconst |
| GetSubjectOrPowerBlocHierarchyLabel | Country | CString | Category: nonconst |
| GetSubjectPact |  | DiplomaticPact | Category: nonconst |
| GetSubjectType |  | SubjectType | Category: nonconst |
| GetSubjectTypeName |  | CString | Category: nonconst |
| GetSubjects |  | Unknown | Category: nonconst |
| GetSubjectsOfType | SubjectType | Unknown | Category: nonconst |
| GetSubsidiesExpenseTrend |  | DataTrend | Category: nonconst |
| GetSubsidiesExpenses |  | CFixedPoint | Category: nonconst |
| GetSubsidiesExpensesDesc |  | CString | Category: nonconst |
| GetSubsistingWorkingAdults |  | int64 | Category: nonconst |
| GetSubventionsExpenseTrend |  | DataTrend | Category: nonconst |
| GetSubventionsExpenses |  | CFixedPoint | Category: nonconst |
| GetSubventionsExpensesDesc |  | CString | Category: nonconst |
| GetSupplyNetworkNumSeaNodes |  | int32 | Category: nonconst |
| GetSupplyNetworkNumSeaNodesDesc |  | CString | Category: nonconst |
| GetSupplyNetworkStrength |  | CFixedPoint | Category: nonconst |
| GetSuppressionCostDesc |  | CString | Category: nonconst |
| GetSuppressionDesc |  | CString | Category: nonconst |
| GetTagName |  | CString | Category: nonconst |
| GetTargetLeverage | Unknown | CFixedPoint | Category: nonconst |
| GetTargetLeverageShare | PowerBloc | CFixedPoint | Category: nonconst |
| GetTargetRank |  | CString | Category: nonconst |
| GetTariffTrend |  | DataTrend | Category: nonconst |
| GetTaxIncomeFor | Unknown | CFixedPoint | Category: nonconst |
| GetTaxIncomeTrend |  | DataTrend | Category: nonconst |
| GetTaxLevelDescHigh |  | CString | Category: nonconst |
| GetTaxLevelDescLow |  | CString | Category: nonconst |
| GetTaxLevelDescMedium |  | CString | Category: nonconst |
| GetTaxLevelDescVeryHigh |  | CString | Category: nonconst |
| GetTaxLevelDescVeryLow |  | CString | Category: nonconst |
| GetTensionIconTexture | Country | Unknown | Category: nonconst |
| GetTensionTooltip | Country | CString | Category: nonconst |
| GetTensionWith | Country | int32 | Category: nonconst |
| GetTensionWithDesc | Country | CString | Category: nonconst |
| GetTimeUntilTargetReachedArmy |  | CString | Category: nonconst |
| GetTimeUntilTargetReachedNavy |  | CString | Category: nonconst |
| GetTimedModifierDurationRemaining | Modifier | CString | Category: nonconst |
| GetTimedModifiers |  | Unknown | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetTopOverlord |  | Country | Category: nonconst |
| GetTotalAgitatorSlots |  | int32 | Category: nonconst |
| GetTotalExpensesTrend |  | DataTrend | Category: nonconst |
| GetTotalExportedAmount |  | CFixedPoint | Category: nonconst |
| GetTotalForeignConstructions |  | int32 | Category: nonconst |
| GetTotalGovernmentClout |  | CFixedPoint | Category: nonconst |
| GetTotalImportedAmount |  | CFixedPoint | Category: nonconst |
| GetTotalIncomeTrend |  | DataTrend | Category: nonconst |
| GetTotalLeverageFactors |  | CFixedPoint | Category: nonconst |
| GetTotalLeverageFactorsBreakdown |  | CString | Category: nonconst |
| GetTotalLeverageFactorsWithResistance |  | CFixedPoint | Category: nonconst |
| GetTotalLeverageFactorsWithResistanceBreakdown |  | CString | Category: nonconst |
| GetTotalLiteracyRanking |  | CString | Category: nonconst |
| GetTotalLiteracyRate |  | CFixedPoint | Category: nonconst |
| GetTotalMarginalClout |  | CFixedPoint | Category: nonconst |
| GetTotalNumLoyalistsChange |  | int64 | Category: nonconst |
| GetTotalNumLoyalistsDecrease |  | int64 | Category: nonconst |
| GetTotalNumLoyalistsIncrease |  | int64 | Category: nonconst |
| GetTotalNumRadicalsChange |  | int64 | Category: nonconst |
| GetTotalNumRadicalsDecrease |  | int64 | Category: nonconst |
| GetTotalNumRadicalsIncrease |  | int64 | Category: nonconst |
| GetTotalOppositionClout |  | CFixedPoint | Category: nonconst |
| GetTotalPopulation |  | int64 | Category: nonconst |
| GetTotalUrbanization |  | int32 | Category: nonconst |
| GetTreatiesBrokenFromNeutralityDesc | DiplomaticPlay | CString | Category: nonconst |
| GetTreatiesExpenseTrend |  | DataTrend | Category: nonconst |
| GetTreatiesIncomeTrend |  | DataTrend | Category: nonconst |
| GetTreatiesWith | Country | Unknown | Category: nonconst |
| GetTreatiesWithDesc | Country | CString | Category: nonconst |
| GetTruceDate | Country | CString | Category: nonconst |
| GetUnclaimedLeverage |  | CFixedPoint | Category: nonconst |
| GetUnclaimedLeverageFormatted |  | CString | Category: nonconst |
| GetUnclaimedLeverageShare |  | CFixedPoint | Category: nonconst |
| GetUnclaimedLeverageShareTarget |  | CFixedPoint | Category: nonconst |
| GetUnclaimedLeverageTarget |  | CFixedPoint | Category: nonconst |
| GetUnemployedWorkingAdults |  | int64 | Category: nonconst |
| GetUnenforcedTreaties |  | Unknown | Category: nonconst |
| GetUnenforcedTreatiesWith | Country | Unknown | Category: nonconst |
| GetUnenforcedTreatiesWithDesc | Unknown | CString | Category: nonconst |
| GetUnrealizedTaxes |  | CFixedPoint | Category: nonconst |
| GetUpperStrataPopulationTrend |  | DataTrend | Category: nonconst |
| GetUsedAgitatorSlots |  | int32 | Category: nonconst |
| GetUsedFreeCharters |  | int32 | Category: nonconst |
| GetWarships |  | int32 | Category: nonconst |
| GetWeeklyBalance |  | CFixedPoint | Category: nonconst |
| GetWeeklyCostArmy |  | CFixedPoint | Category: nonconst |
| GetWeeklyCostNavy |  | CFixedPoint | Category: nonconst |
| GetWeeklyExpenses |  | CFixedPoint | Category: nonconst |
| GetWeeklyFixedExpenses |  | CFixedPoint | Category: nonconst |
| GetWeeklyGDP |  | CFixedPoint | Category: nonconst |
| GetWeeklyIncome |  | CFixedPoint | Category: nonconst |
| GetWeeklyInnovation |  | CFixedPoint | Category: nonconst |
| GetWeeklyInnovationDesc |  | CString | Category: nonconst |
| GetWeeklyInterestRate |  | CFixedPoint | Category: nonconst |
| GetWeeklyLeverageGain | PowerBloc | CFixedPoint | Category: nonconst |
| GetWeeklyLibertyDesireChange |  | CFixedPoint | Category: nonconst |
| GetWeeklyLibertyDesireChangeDesc |  | CString | Category: nonconst |
| GetWeeklyLibertyDesireChangeFromSupportIndependence |  | CFixedPoint | Category: nonconst |
| GetWeeklyLibertyDesireChangeFromSupportIndependenceDesc |  | CString | Category: nonconst |
| GetWeeklyMaxInnovation |  | CFixedPoint | Category: nonconst |
| GetWeeklyMaxInnovationDesc |  | CString | Category: nonconst |
| GetWeeklyRawInnovation |  | CFixedPoint | Category: nonconst |
| GetWeeklyResearchSpeed |  | CFixedPoint | Category: nonconst |
| GetWeeklyResearchSpeedDesc |  | CString | Category: nonconst |
| GetWeeklyTechnologyProgressDescForTech | Technology | CString | Category: nonconst |
| GetWeeklyTechnologySpreadBreakdown |  | CString | Category: nonconst |
| GetWeeklyTechnologySpreadDesc |  | CString | Category: nonconst |
| GetWeeklyTechnologySpreadForTechDesc | Technology | CString | Category: nonconst |
| GetWeeklyTemporaryExpenses |  | CFixedPoint | Category: nonconst |
| GetWeeklyTemporaryIncome |  | CFixedPoint | Category: nonconst |
| GetWelfarePaymentsExpenses |  | CFixedPoint | Category: nonconst |
| GetWelfarePaymentsTrend |  | DataTrend | Category: nonconst |
| GetWorkingAdults |  | int64 | Category: nonconst |
| GetYearlyInterestRate |  | CFixedPoint | Category: nonconst |
| GetYouOrCountryName |  | CString | Category: nonconst |
| GetZeroBalancePlotPoints |  | Unknown | Category: nonconst |
| GetZeroMoneyPlotPoints |  | Unknown | Category: nonconst |
| HasActiveDiplomacy |  | bool |  |
| HasAnyAllianceLikeTreatiesWith | Unknown | bool |  |
| HasAnySlavery |  | bool |  |
| HasAnyTaxes |  | bool |  |
| HasConstructionQueued |  | bool |  |
| HasCurrentlyResearchedTechnology |  | bool |  |
| HasDamagedConvoys |  | bool |  |
| HasDeclaredInterest | Unknown | bool |  |
| HasDecreasingInterests |  | bool |  |
| HasDiplomaticPactWith | Unknown Unknown | bool |  |
| HasElectionTrendData |  | bool |  |
| HasElections |  | bool |  |
| HasExportSubventionsHigh | Goods | bool |  |
| HasExportSubventionsLow | Goods | bool |  |
| HasExportSubventionsMax | Goods | bool |  |
| HasExportTariffsHigh | Goods | bool |  |
| HasExportTariffsLow | Goods | bool |  |
| HasExportTariffsMax | Goods | bool |  |
| HasExportTariffsNone | Goods | bool |  |
| HasForeignInvestmentRights | Country | bool |  |
| HasGovernmentWages |  | bool |  |
| HasHeir |  | bool |  |
| HasHigherUnclaimedLeverage |  | bool |  |
| HasHigherUnclaimedLeverageTarget |  | bool |  |
| HasIGApprovalFromLoyalists |  | bool |  |
| HasIGApprovalFromRadicals |  | bool |  |
| HasImportSubventionsHigh | Goods | bool |  |
| HasImportSubventionsLow | Goods | bool |  |
| HasImportSubventionsMax | Goods | bool |  |
| HasImportTariffsHigh | Goods | bool |  |
| HasImportTariffsLow | Goods | bool |  |
| HasImportTariffsMax | Goods | bool |  |
| HasImportTariffsNone | Goods | bool |  |
| HasInterestIn | StrategicRegion | bool |  |
| HasMilitaryWages |  | bool |  |
| HasNewProductionMethodInGroup | ProductionMethodGroup | bool |  |
| HasNewProductionMethodInSameGroup | BuildingType ProductionMethod | bool |  |
| HasObjective |  | bool |  |
| HasOverlappingInterestsWith | Unknown | bool |  |
| HasOwningCompany |  | bool |  |
| HasProgressingLawEnactment |  | bool |  |
| HasRuler |  | bool |  |
| HasSelectedLaw |  | bool |  |
| HasSpecialSocialHierarchy |  | bool |  |
| InDefault |  | bool |  |
| IsAI |  | bool |  |
| IsAIOrOtherPlayer |  | bool |  |
| IsAlliedInDiploPlayWith | Country | bool |  |
| IsAnySubjectOf | Unknown | bool |  |
| IsAtWar |  | bool |  |
| IsAtWarWith | Country | bool |  |
| IsBeingHighlighted |  | bool |  |
| IsBeingTutorialHighlighted |  | bool |  |
| IsColonizable |  | bool |  |
| IsCommittedInDiplomaticPlay |  | bool |  |
| IsConscripting |  | bool |  |
| IsConstructionPaused |  | bool |  |
| IsDead |  | bool |  |
| IsDiplomaticallyRelevantCountry | Unknown | bool |  |
| IsEconomyHealthy |  | bool |  |
| IsEconomyHealthyDesc |  | CString |  |
| IsEnactingLaw |  | bool |  |
| IsHighestRank |  | bool |  |
| IsIgnoringCountryFormation | CountryFormation | bool |  |
| IsIgnoringDecision | Decision | bool |  |
| IsInElectionCampaignPeriod |  | bool |  |
| IsInPowerBloc |  | bool |  |
| IsInsurrectionary |  | bool |  |
| IsInvolvedInActiveConflict |  | bool |  |
| IsLocalPlayer |  | bool |  |
| IsLowestRank |  | bool |  |
| IsMobilized |  | bool |  |
| IsNegotiating |  | bool |  |
| IsNeighborsWith | Unknown | bool |  |
| IsNewProductionMethod | ProductionMethod | bool |  |
| IsObjectiveIdle |  | bool |  |
| IsOtherPlayer |  | bool |  |
| IsPinnedInOutliner |  | bool |  |
| IsPlayer |  | bool |  |
| IsPowerBlocLeader |  | bool |  |
| IsPowerStruggling |  | bool |  |
| IsRank | Unknown | bool |  |
| IsRevolutionary |  | bool |  |
| IsSecessionist |  | bool |  |
| IsSubject |  | bool |  |
| IsSubjectOf | Country | bool |  |
| IsTaxingAnyGood |  | bool |  |
| IsValid |  | bool |  |
| LeavePowerBloc |  | Command |  |
| MakeScope |  | Scope |  |
| MobilizeAllArmies |  | Command |  |
| OwesObligationTo | Unknown | bool |  |
| PauseConstruction |  | Command |  |
| PauseConstructionTooltip |  | CString |  |
| PredictBalanceWithoutTemporaryIncomeAndExpenses |  | CFixedPoint |  |
| PredictConsumptionTaxes |  | CFixedPoint |  |
| PredictDiplomaticPactsExpenses |  | CFixedPoint |  |
| PredictDiplomaticPactsExpensesDesc |  | CString |  |
| PredictDiplomaticPactsIncome |  | CFixedPoint |  |
| PredictDiplomaticPactsIncomeDesc |  | CString |  |
| PredictDividendsTaxes |  | CFixedPoint |  |
| PredictDividendsTaxesDesc |  | CString |  |
| PredictEconomyHealthDesc |  | CString |  |
| PredictGovernmentShareDividends |  | CFixedPoint |  |
| PredictGovernmentShareDividendsDesc |  | CString |  |
| PredictGovernmentShareLosses |  | CFixedPoint |  |
| PredictGovernmentShareLossesDesc |  | CString |  |
| PredictGovernmentWagesExpenses |  | CFixedPoint |  |
| PredictMaxWeeklyTechnologyProgressForTech | Unknown | CFixedPoint |  |
| PredictMilitaryWagesExpenses |  | CFixedPoint |  |
| PredictMinWeeklyTechnologyProgressForTech | Unknown | CFixedPoint |  |
| PredictMinting |  | CFixedPoint |  |
| PredictMintingDesc |  | CString |  |
| PredictTariffs |  | CFixedPoint |  |
| PredictTariffsDesc |  | CString |  |
| PredictTotalMilitaryExpenses |  | CFixedPoint |  |
| PredictTreatyExpenses |  | CFixedPoint |  |
| PredictTreatyExpensesDesc |  | CString |  |
| PredictTreatyIncome |  | CFixedPoint |  |
| PredictTreatyIncomeDesc |  | CString |  |
| PredictWeeklyBalance |  | CFixedPoint |  |
| PredictWeeklyBalanceWithEconomyHealthHint |  | CString |  |
| PredictWeeklyFixedIncome |  | CFixedPoint |  |
| PredictWeeklyIncome |  | CFixedPoint |  |
| RemoveCompany | CompanyType | Command |  |
| ResumeConstruction |  | Command |  |
| ResumeConstructionTooltip |  | CString |  |
| Self |  | Country |  |
| SetExportSubventionsHigh | Goods | Command |  |
| SetExportSubventionsLow | Goods | Command |  |
| SetExportSubventionsMax | Goods | Command |  |
| SetExportTariffsHigh | Goods | Command |  |
| SetExportTariffsLow | Goods | Command |  |
| SetExportTariffsMax | Goods | Command |  |
| SetExportTariffsNone | Goods | Command |  |
| SetGovernmentWageLevelHigh |  | Command |  |
| SetGovernmentWageLevelLow |  | Command |  |
| SetGovernmentWageLevelMedium |  | Command |  |
| SetGovernmentWageLevelVeryHigh |  | Command |  |
| SetGovernmentWageLevelVeryLow |  | Command |  |
| SetImportSubventionsHigh | Goods | Command |  |
| SetImportSubventionsLow | Goods | Command |  |
| SetImportSubventionsMax | Goods | Command |  |
| SetImportTariffsHigh | Goods | Command |  |
| SetImportTariffsLow | Goods | Command |  |
| SetImportTariffsMax | Goods | Command |  |
| SetImportTariffsNone | Goods | Command |  |
| SetMilitaryWageLevelHigh |  | Command |  |
| SetMilitaryWageLevelLow |  | Command |  |
| SetMilitaryWageLevelMedium |  | Command |  |
| SetMilitaryWageLevelVeryHigh |  | Command |  |
| SetMilitaryWageLevelVeryLow |  | Command |  |
| SetTaxLevelHigh |  | Command |  |
| SetTaxLevelLow |  | Command |  |
| SetTaxLevelMedium |  | Command |  |
| SetTaxLevelVeryHigh |  | Command |  |
| SetTaxLevelVeryLow |  | Command |  |
| ShowInvestmentPoolPredictedNextBuilding |  | bool |  |
| SortCompanies | Unknown | void |  |
| SortCultures | CString | void |  |
| SortReligions | CString | void |  |
| SortStates | Unknown | void |  |
| SortSubjects | CString | void |  |
| StartNegotiationWith | InterestGroup | Command |  |
| ToggleIgnoreCountryFormation | CountryFormation | Command |  |
| ToggleIgnoreDecision | Decision | Command |  |
| TogglePinInOutliner |  | void |  |
| TryGetOverlordTooltipEntry |  | CString |  |
| TryGetSubjectsTooltipEntry |  | CString |  |

| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessSelf |  | CountryDefinition | Category: const |
| GetAdjective |  | CString | Category: nonconst |
| GetBaseFlag |  | CoatOfArms | Category: nonconst |
| GetColor |  | CVector4f | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetFlag | CString | CoatOfArms | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetPrimaryCulture |  | Culture | Category: nonconst |
| GetPrimaryCultureName |  | CString | Category: nonconst |
| GetTier |  | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| IsValid |  | bool |  |
| MakeScope |  | Scope |  |
| Self |  | CountryDefinition |  |

| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessFormationCandidates |  | Unknown | Category: const |
| AccessFormationCultureCountries |  | Unknown | Category: const |
| AccessFormationStateRegions |  | Unknown | Category: const |
| AccessSelf |  | CountryFormation | Category: const |
| CanFormCountry | Unknown | bool |  |
| CanLaunchLeadershipPlay | Country | bool |  |
| CanLaunchUnificationPlay |  | bool |  |
| ControlsStateRegion | Country StateRegion | bool |  |
| FormCountry | Country | Command |  |
| GetAdjective |  | CString | Category: nonconst |
| GetControlsStateRegionDesc | Country StateRegion | CString | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetDefinition |  | CountryDefinition | Category: nonconst |
| GetFormDesc | Country | CString | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNumControlledStates | Country | int32 | Category: nonconst |
| GetNumRequiredStates |  | int32 | Category: nonconst |
| GetNumSupportingCountries | Country | int32 | Category: nonconst |
| GetSupportCandidateDesc | Country Country | CString | Category: nonconst |
| GetSupportForAllCandidatesDesc | Country | CString | Category: nonconst |
| GetSupportForCandidateBreakdown | Unknown Unknown | CString | Category: nonconst |
| GetSupportedCandidateCountry | Unknown | Country | Category: nonconst |
| GetSupportingCountriesDesc | Country | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetTotalNumStates |  | int32 | Category: nonconst |
| GetTriggerLeadershipPlayDesc | Country Country | CString | Category: nonconst |
| GetTriggerUnificationPlayDesc | Country | CString | Category: nonconst |
| IsCandidateForFormation | Unknown | bool |  |
| IsMajorFormation |  | bool |  |
| IsSupportingAnyCandidate | Unknown | bool |  |
| IsSupportingCandidate | Unknown Unknown | bool |  |
| ListCultures |  | CString |  |
| ListRequiredStates | Country | CString |  |
| MakeScope |  | Scope |  |
| Self |  | CountryFormation |  |
| ShowLeadershipPlayConfirmation | Unknown | void |  |
| ShowUnificationPlayConfirmation |  | void |  |
| SupportCandidate | Unknown Unknown | Command |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| AccessActiveLawFromGroup | LawGroup | Law | Category: const |
| AccessCapital |  | State | Category: const |
| AccessCurrentlyResearchedTechnology |  | Technology | Category: const |
| AccessDefinition |  | CountryDefinition | Category: const |
| AccessFirstMarket |  | Market | Category: const |
| AccessGovernment |  | GovernmentType | Category: const |
| AccessHeaviestJournalEntry |  | JournalEntry | Category: const |
| AccessHeir |  | Character | Category: const |
| AccessLawBeingEnacted |  | Law | Category: const |
| AccessModifier |  | Modifier | Category: const |
| AccessOverlord |  | Country | Category: const |
| AccessPowerBloc |  | PowerBloc | Category: const |
| AccessRuler |  | Character | Category: const |
| AccessStateReligion |  | Religion | Category: const |
| AccessTopOverlord |  | Country | Category: const |
| CalcLibertyDesireLevel |  | LibertyDesireLevel |  |
| GetActiveLawFrom | Unknown | Law | Category: nonconst |
| GetActiveLawFromGroup | LawGroup | Law | Category: nonconst |
| GetAttitudeTowards | Country | AIAttitude | Category: nonconst |
| GetCapital |  | State | Category: nonconst |
| GetCurrentlyResearchedTechnology |  | Technology | Category: nonconst |
| GetDefinition |  | CountryDefinition | Category: nonconst |
| GetDiplomaticAction | Unknown Unknown | DiplomaticAction | Category: nonconst |
| GetDiplomaticActionWithStates | Unknown Unknown Unknown Unknown | DiplomaticAction | Category: nonconst |
| GetElection |  | Election | Category: nonconst |
| GetFirstPrimaryCulture |  | Culture | Category: nonconst |
| GetFlag |  | CoatOfArms | Category: nonconst |
| GetFoodSecurity |  | FoodSecurity | Category: nonconst |
| GetGovernment |  | GovernmentType | Category: nonconst |
| GetGovernmentLegitimacyLevel |  | LegitimacyLevel | Category: nonconst |
| GetHeir |  | Character | Category: nonconst |
| GetInterestGroupOfType | InterestGroup | InterestGroup | Category: nonconst |
| GetJournalEntry | Unknown | JournalEntry | Category: nonconst |
| GetLawBeingEnacted |  | Law | Category: nonconst |
| GetLawBeingEnactedFromGroup | Unknown | Law | Category: nonconst |
| GetMarket |  | Market | Category: nonconst |
| GetModifier |  | Modifier | Category: nonconst |
| GetMonopolyCountryOnBuildingType | BuildingType | Country | Category: nonconst |
| GetNegotiatingInterestGroup |  | InterestGroup | Category: nonconst |
| GetObjective |  | Objective | Category: nonconst |
| GetOtherPowerBlocWithHighestLeverage | Unknown | PowerBloc | Category: nonconst |
| GetOverlord |  | Country | Category: nonconst |
| GetOwningCompany |  | Company | Category: nonconst |
| GetPlayer |  | Player | Category: nonconst |
| GetPowerBloc |  | PowerBloc | Category: nonconst |
| GetPowerBlocWithHighestLeverage |  | PowerBloc | Category: nonconst |
| GetPreviousAttitudeTowards | Country | AIAttitude | Category: nonconst |
| GetRankModifier |  | Modifier | Category: nonconst |
| GetRuler |  | Character | Category: nonconst |
| GetSampleLowerStrataPop |  | Pop | Category: nonconst |
| GetSampleLowerStrataPopForCulture | Unknown | Pop | Category: nonconst |
| GetSampleMiddleStrataPop |  | Pop | Category: nonconst |
| GetSampleMiddleStrataPopForCulture | Unknown | Pop | Category: nonconst |
| GetSampleUpperStrataPop |  | Pop | Category: nonconst |
| GetSampleUpperStrataPopForCulture | Unknown | Pop | Category: nonconst |
| GetSelectedLaw |  | Law | Category: nonconst |
| GetSocialHierarchy |  | SocialHierarchy | Category: nonconst |
| GetSpecialSocialHierarchy |  | SocialHierarchy | Category: nonconst |
| GetStateReligion |  | Religion | Category: nonconst |
| GetSubjectPact |  | DiplomaticPact | Category: nonconst |
| GetSubjectType |  | SubjectType | Category: nonconst |
| GetTopOverlord |  | Country | Category: nonconst |
| MakeScope |  | Scope |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| GetBaseFlag |  | CoatOfArms | Category: nonconst |
| GetFlag | CString | CoatOfArms | Category: nonconst |
| GetPrimaryCulture |  | Culture | Category: nonconst |
| MakeScope |  | Scope |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| GetDefinition |  | CountryDefinition | Category: nonconst |
| GetSupportedCandidateCountry | Country | Country | Category: nonconst |
| MakeScope |  | Scope |  |

## References

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • Countries • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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
