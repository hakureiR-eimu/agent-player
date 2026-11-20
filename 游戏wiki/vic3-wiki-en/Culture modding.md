---
title: Culture modding
source: https://vic3.paradoxwikis.com/Culture_modding
pageid: 6775
categories: [Potentially_outdated, 1.11, Modding]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.11.

See also:
Religion modding
[Culture](Culture.md) in Victoria 3 represents the abstracted ethnicity and traditions of pops and countries.

## Culture definition

Cultures are defined in /Victoria 3/game/common/cultures/. The definition is a script name, color, religion, traits, list of names, ethnicities, and graphics. For example:

```
mazanderani ={	#Script name can be anything, but best to match desired in-game localization unless it overlaps some other script term
    color= rgb{ 158 68 137 }	#either rgb (255) or hsv (decimal)

    religion = shiite	#Any defined religion; default religion for pops and countries of this culture
    heritage = heritage_iranian
    language = language_tabari
    traditions = { tradition_persianate }

    male_common_first_names={	#space or line-separated list of names, each is a localization key, and so must have no spaces
        [names]
    }
    female_common_first_names = {
	[names]
    }
    common_last_names={
	[names]
    }

    ethnicities = {	#weighted list of ethnicities, affects appearance of pop and character models
	1 = arab
    }
    graphics = arabic	#Graphical culture used for pops and countries with this culture
}
```

The script name is used as a localization key as well as for triggers and effects.

The color can be either RGB or HSV format: RGB uses 0-255 values while HSV uses decimal values.

Heritage is a single heritage trait, language a single language trait, and tradition any number of tradition traits.

Name lists are used for generating characters of that culture and should include at least `male_common_first_names`, `female_common_first_names`, and `common_last_names`. Additional lists can use `noble` and `regal` in place of `common`, e.g. `male_noble_first_names` or `regal_last_names`.

Ethnicities are a weighted list of defined ethnicities in /Victoria 3/game/common/ethnicities/. Unmodified cultures typically have one ethnicity, with a few that have two or more.

Graphics are defined in /Victoria 3/game/common/culture_graphics/, just as a simple defined block, `arabic = {}`. This is referenced in cultures and in various graphics files.

Each culture may also have an `obsessions` block, listing one or more consumable goods that the culture starts obsessed with. Do not define more than the `MAX_NUM_OBSESSIONS` goods as starting obsessions.

Similarly, each culture may also have a `taboos` block, listing one or more consumable goods that the culture has as a taboo. It is not clear if there is a maximum number of taboos. Culture taboos override religion taboos

## Discrimination traits

Cultures and [religions](Religion modding.md) both use discrimination traits defined in /Victoria 3/game/common/discrimination_traits/. Each trait is defined as by a unique script name and block. Each trait has a `type` which can be `heritage`, `language`, or `tradition`. The script name is also a localization key.

For example:

```
language_germanophone = { # a language trait
	type = language
	trait_group = language_group_germanic
}

heritage_abyssinian = { # a heritage trait
	type = heritage
	trait_group = heritage_group_african
}

tradition_rumelian = {
	type = tradition
}
```

The prefixes are only for easy reference and categorization.

Nothing distinguishes a cultural trait from a religious trait besides its use in culture and religion definitions. Religions only use heritage traits, not language or tradition traits.

Heritage and language traits also have a trait group, representing a collection of similar traits.

### Trait groups

Discrimination trait groups are defined in /Victoria 3/game/common/discrimination_trait_groups/. Trait groups are identical to traits except that they cannot be a tradition type, nor do they have a further group.

For example

```
language_group_germanic = { # a language trait group
	type = language
}

heritage_group_african = { # a heritage trait group
	type = heritage
}
```

## Modifier Definitions

See also:
Modifier types
,
Modifier modding
When creating a culture, you must also create three sets of [static modifiers](Modifier modding.md), `(culture name)_standard_of_living_modifier_positive` and `(culture name)_standard_of_living_modifier_negative` and `(culture name)_cultural_acceptance_modifier_positive` and `(culture name)_cultural_acceptance_modifier_negative` and `(culture name)_fervor_target_modifier_positive` and `(culture name)_fervor_target_modifier_negative`. You must also create [modifier types](Modifier types.md) named `state_(culture name)_standard_of_living_add`, which is used by the [effect](Effect.md) add_culture_standard_of_living_modifier and `country_(culture name)_cultural_acceptance_add`, which is used with add_culture_acceptance_modifier, and `country_fervor_target_(culture name)_add`, which is used with add_fervor_target_modifier. Examples of these definitions for vanilla cultures can be found at /Victoria 3/game/common/static_modifiers/07_culture_standard_of_living.txt and /Victoria 3/game/common/static_modifiers/10_culture_cultural_acceptance_modifiers.txt and /Victoria 3/game/common/static_modifiers/11_culture_fervor_target_modifiers.txt and /Victoria 3/game/common/modifier_type_definitions/10_country_cultural_acceptance_culture_modifier_types.txt and /Victoria 3/game/common/modifier_type_definitions/99_todo_sort_into_other_files.txt

For example:

```
#in static_modifiers
scottish_standard_of_living_modifier_positive = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_positive.dds"
	state_scottish_standard_of_living_add = 1
}

scottish_standard_of_living_modifier_negative = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_negative.dds"
	state_scottish_standard_of_living_add = 1
}

scottish_cultural_acceptance_modifier_positive = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_positive.dds"
	country_scottish_cultural_acceptance_add = 1
}

scottish_cultural_acceptance_modifier_negative = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_negative.dds"
	country_scottish_cultural_acceptance_add = 1
}

scottish_fervor_target_modifier_positive = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_positive.dds"
	country_fervor_target_scottish_add = 1
}

scottish_fervor_target_modifier_negative = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_negative.dds"
	country_fervor_target_scottish_add = 1
}

#############################
#in modifier_types
state_scottish_standard_of_living_add = {
	decimals=1
	color=good
	game_data = {
		ai_value=0
	}
}

country_scottish_cultural_acceptance_add = {
	decimals=1
	color=good
	game_data = {
		ai_value=0
	}
}

country_fervor_target_scottish_add={
	decimals=1
	color=good
	game_data={
		ai_value=0
	}
}
```

## Base game cultures

See also:
List of cultures
Most base game cultures use the same script name as the English localized name, except all in lowercase, and with spaces or hyphens replaced by underscores and replacing all non-ASCII characters with their closest equivalent.

The following cultures differ from this pattern and use a non-obvious script name. Some are slight respellings, others use alternate names for the culture.

| Culture | Script name |
|---|---|
| Franco-Provençal | francoprovencal |
| English | british |
| Sephardim | sephardic |
| Amazigh | berber |
| Kazakh | kazak |
| Kyrgyz | kirgiz |
| Oria | oriya |
| Punjabi | panjabi |
| Telugu | telegu |
| Aboriginal | aborigine |
| O’odham | oodham |
| Fluvial Bantu | fluvian_bantu |
| Chitrali | kho |
| Szekler | szekely |

## Culture script documentation

The following [effects](Effect.md), [event targets](Event target.md), and [triggers](Trigger.md) can be used in culture scope.

| Effect | Description | Example | Targets |
|---|---|---|---|
| add_cultural_community_in_state | Adds a cultural community for the scoped culture in the target state. | cu:zulu = { add_cultural_community_in_state = scope:some_state } | state |
| add_cultural_obsession | Adds a new obsession to the culture in scope | add_cultural_obsession = <goods> |  |
| add_cultural_taboo | Adds a new taboo to the culture in scope | add_cultural_taboo = <goods> |  |
| add_fervor | Adds fervor to a scoped culture | add_fervor = 2.6 |  |
| add_tradition_trait | Adds a new tradition trait to the culture in scope | add_tradition_trait = <tradition_trait> |  |
| every_scope_homeland_state | Iterate through all states that are a homeland for the scoped culture, or a homeland of any primary culture of the scoped country | every_scope_homeland_state = { limit = { <triggers> } #optional <effects> } | state |
| every_scope_pop | Iterate through all pops in a: country, state, interest group, culture | every_scope_pop = { limit = { <triggers> } #optional <effects> } | pop |
| ordered_scope_homeland_state | Iterate through all states that are a homeland for the scoped culture, or a homeland of any primary culture of the scoped country | ordered_scope_homeland_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_scope_pop | Iterate through all pops in a: country, state, interest group, culture | ordered_scope_pop = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | pop |
| random_scope_homeland_state | Iterate through all states that are a homeland for the scoped culture, or a homeland of any primary culture of the scoped country | random_scope_homeland_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| random_scope_pop | Iterate through all pops in a: country, state, interest group, culture | random_scope_pop = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | pop |
| remove_cultural_obsession | Removes an obsession from the culture in scope | remove_cultural_obsession = <goods> |  |
| remove_cultural_taboo | Removes a taboo from the culture in scope | remove_cultural_taboo = <goods> |  |
| remove_tradition_trait | Removes a existing tradition trait to the culture in scope | remove_tradition_trait = <tradition_trait> |  |
| set_fervor | Sets the fervor of a scoped culture | set_fervor = 3.0 |  |
| set_name_format | Sets the name format of a scoped culture | set_name_format = first_last/last_first |  |

| Trigger | Description | Example | Targets |
|---|---|---|---|
| any_scope_pop | Iterate through all pops in a: country, state, interest group, culture | any_scope_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | pop |
| culture_can_have_mass_migration_to_country | Checks if the scoped culture can have mass migration to target country | can_have_mass_migration_to_country = c:country | country |
| culture_current_fervor | Compares the current fervor for a given culture | culture_current_fervor > 0.2 | value |
| culture_has_community_in_state | Checks if the scoped culture has a cultural community in a state. | culture_has_community_in_state = <state> |  |
| culture_has_national_awakening | Checks if the scoped culture has an active national awakening | culture_has_national_awakening = yes / no | boolean |
| culture_national_awakening_occurred | Checks if the scoped culture has ever had a national awakening started | culture_national_awakening_occurred = yes / no | boolean |
| culture_secession_progress | Checks the culture's progress percentage towards secession in a country. 0 if no secession movement is active for the culture. | culture_secession_progress = { target = scope:example_country value > 0.5 } | value |
| culture_target_fervor | Compares the target fervor for a given culture | culture_target_fervor > 0.2 | value |
| has_cultural_obsession | Checks if a culture has a certain goods as obsession | has_cultural_obsession = <goods key> |  |
| has_culture_graphics | Checks if a culture has a certain culture_graphics | has_culture_graphics = <culture graphics key> |  |
| has_discrimination_trait | Checks if scoped culture or religion has the given discrimination trait | has_trait = trait |  |
| has_homeland | Checks if scoped culture has a homeland in target state or state region | has_homeland = state/state region |  |
| is_primary_culture_of | Checks if culture is any of a country's primary cultures | is_primary_culture_of = <country> | country |
| shares_heritage_trait_group_with_any_primary_culture | Checks if culture shares any trait group marked as 'heritage' with any of a country's primary cultures | shares_heritage_trait_group_with_any_primary_culture = <country> | country |
| shares_heritage_trait_group_with_culture | Checks if culture shares any trait group marked as 'heritage' with another culture | shares_heritage_trait_group_with_culture = <culture> | culture |
| shares_heritage_trait_group_with_state_religion | Checks if the religion shares any heritage trait group with a country's state religion | shares_heritage_trait_group_with_state_religion = <country> | country |
| shares_heritage_trait_with_any_primary_culture | Checks if culture shares any trait marked as 'heritage' with any of a country's primary cultures | shares_heritage_trait_with_any_primary_culture = <country> | country |
| shares_heritage_trait_with_culture | Checks if culture shares any trait marked as 'heritage' with another culture | shares_heritage_trait_with_culture = <culture> | culture |
| shares_language_trait_group_with_any_primary_culture | Checks if culture shares any trait group marked as 'language' with any of a country's primary cultures | shares_language_trait_group_with_any_primary_culture = <country> | country |
| shares_language_trait_group_with_culture | Checks if culture shares any trait group marked as 'language' with another culture | shares_language_trait_group_with_culture = <culture> | culture |
| shares_language_trait_with_any_primary_culture | Checks if culture shares any trait marked as 'language' with any of a country's primary cultures | shares_language_trait_with_any_primary_culture = <country> | country |
| shares_language_trait_with_culture | Checks if culture shares any trait marked as 'language' with another culture | shares_language_trait_with_culture = <culture> | culture |
| shares_tradition_trait_with_any_primary_culture | Checks if culture shares any trait marked as 'tradition' with any of a country's primary cultures | shares_language_trait_with_any_primary_culture = <country> | country |
| shares_tradition_trait_with_culture | Checks if culture shares any trait marked as 'tradition' with another culture | shares_language_trait_with_culture = <culture> | culture |

| Event target | Description | To scope |
|---|---|---|
| national_awakening_state_region | Links from a culture scope to the state region with an active national awakening for that culture | state_region |

### Culture GUI script

Main article:
GUI script
| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessHomelands |  | Unknown | Category: const |
| AccessReligion |  | Religion | Category: const |
| AccessSameHeritageCultures |  | Unknown | Category: const |
| AccessSelf |  | Culture | Category: const |
| CalcAvgSoL |  | CFixedPoint |  |
| CalcAvgSoLForMiddle |  | CFixedPoint |  |
| CalcAvgSoLForPoor |  | CFixedPoint |  |
| CalcAvgSoLForRich |  | CFixedPoint |  |
| CalcTurmoilInCountry | Unknown | CFixedPoint |  |
| GetAcceptanceDescIn | Country | CString | Category: nonconst |
| GetAcceptanceIn | Country | int32 | Category: nonconst |
| GetAllAcceptanceStatusSegments | Country | Unknown | Category: nonconst |
| GetCasualtiesFromWars |  | int64 | Category: nonconst |
| GetColor |  | CVector4f | Category: nonconst |
| GetCulturalTraitsDesc |  | CString | Category: nonconst |
| GetCurrentFervor |  | CFixedPoint | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetDependents | Country | int64 | Category: nonconst |
| GetDependentsAsPercentage | Country | CFixedPoint | Category: nonconst |
| GetHeritageTrait |  | DiscriminationTrait | Category: nonconst |
| GetID |  | uint32 | Category: nonconst |
| GetLanguageTrait |  | DiscriminationTrait | Category: nonconst |
| GetMigrationTargetsDesc |  | CString | Category: nonconst |
| GetMonthlyChangeFervor |  | CFixedPoint | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetObsessionsDesc |  | CString | Category: nonconst |
| GetPolStr | Country | int64 | Category: nonconst |
| GetPolStrAsFloat | Unknown | float | Category: nonconst |
| GetPolStrAsPercentage | Country | CFixedPoint | Category: nonconst |
| GetPopulation | Country | int64 | Category: nonconst |
| GetPopulationAsFloat | Unknown | float | Category: nonconst |
| GetPopulationAsPercentage | Country | CFixedPoint | Category: nonconst |
| GetPopulationChange | Country | int64 | Category: nonconst |
| GetPopulationChangeDesc | Country | CString | Category: nonconst |
| GetPopulationInCountryAsPercentage | Unknown | CFixedPoint | Category: nonconst |
| GetReligion |  | Religion | Category: nonconst |
| GetReligionsDesc |  | CString | Category: nonconst |
| GetStateDependents | State | int64 | Category: nonconst |
| GetStateDependentsAsPercentage | State | CFixedPoint | Category: nonconst |
| GetStatePolStr | State | int64 | Category: nonconst |
| GetStatePolStrAsFloat | Unknown | float | Category: nonconst |
| GetStatePolStrAsPercentage | State | CFixedPoint | Category: nonconst |
| GetStatePopulation | State | int64 | Category: nonconst |
| GetStatePopulationAsFloat | Unknown | float | Category: nonconst |
| GetStatePopulationAsPercentage | State | CFixedPoint | Category: nonconst |
| GetStateWorkforce | State | int64 | Category: nonconst |
| GetStateWorkforceAsPercentage | State | CFixedPoint | Category: nonconst |
| GetTaboosDesc |  | CString | Category: nonconst |
| GetTargetFervor |  | CFixedPoint | Category: nonconst |
| GetTargetFervorBreakdown |  | CString | Category: nonconst |
| GetTargetFervorFromCountryModifiers |  | CFixedPoint | Category: nonconst |
| GetTargetFervorFromCountryModifiersBreakdown |  | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetTraditionTraits |  | Unknown | Category: nonconst |
| GetTurmoil |  | CFixedPoint | Category: nonconst |
| GetWorkforce | Country | int64 | Category: nonconst |
| GetWorkforceAsPercentage | Country | CFixedPoint | Category: nonconst |
| HasNationalAwakening |  | bool |  |
| HasSecessionMovement | Country | bool |  |
| IsPrimaryCultureIn | Country | bool |  |
| IsPrimaryCultureInYesNo | Unknown | CString |  |
| IsValid |  | bool |  |
| MakeScope |  | Scope |  |
| Self |  | Culture |  |

| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessSelf |  | CulturalCommunity | Category: const |
| GetCulture |  | Culture | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetID |  | uint32 | Category: nonconst |
| GetLocalAcceptanceDifference |  | CFixedPoint | Category: nonconst |
| GetLocalAcceptanceDifferenceDesc |  | CString | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetState |  | State | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| IsValid |  | bool |  |
| MakeScope |  | Scope |  |
| Self |  | CulturalCommunity |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| AccessReligion |  | Religion | Category: const |
| GetHeritageTrait |  | DiscriminationTrait | Category: nonconst |
| GetLanguageTrait |  | DiscriminationTrait | Category: nonconst |
| GetReligion |  | Religion | Category: nonconst |
| GetSampleGlobalLowerStrataPop |  | Pop | Category: nonconst |
| GetSampleGlobalMiddleStrataPop |  | Pop | Category: nonconst |
| GetSampleGlobalUpperStrataPop |  | Pop | Category: nonconst |
| MakeScope |  | Scope |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| GetCulture |  | Culture | Category: nonconst |
| GetState |  | State | Category: nonconst |
| MakeScope |  | Scope |  |

## References

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • Culture • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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
