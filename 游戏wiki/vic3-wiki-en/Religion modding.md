---
title: Religion modding
source: https://vic3.paradoxwikis.com/Religion_modding
pageid: 6776
categories: [Potentially_outdated, 1.11, Modding]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.11.

See also:
Culture modding
**Religion in Victoria 3 represents the abstracted faith of pops and countries.**

## Religion definition

Religions are defined in /Victoria 3/game/common/religions. The definition is a script name, texture, traits, color, and optionally taboos.

For example:

```
hindu = {	#script name, also used as localization key
	icon = "gfx/interface/icons/religion_icons/hindu.dds"	#image file
	heritage = heritage_dharmic #a heritage trait
	color = { 0.8 0.2 0.3 }	#color in RGB decimal
	taboos = {	#optional list of consumable goods
		meat
	}
}
```

The script name is used as a localization key as well as for triggers and effects.

- The icon is an image file.
- The color is RGB decimal format.
- The heritage can be any heritage trait.
- Color is used for interface and map color marking.

Each religion may also have an `taboo` block, listing one or more consumable goods that the religion considers taboo. It is not clear if there is a maximum number of taboos.

## Discrimination traits

[Cultures](Culture modding.md) and religions both use discrimination traits defined in /Victoria 3/game/common/discrimination_traits/. Each trait is defined as by a unique script name and block. Each trait has a `type` which can be `heritage`, `language`, or `tradition`. The script name is also a localization key.

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
When creating a religion, you must also create two [static modifiers](Modifier modding.md), named `(religion name)_standard_of_living_modifier_positive` and `(religion name)_standard_of_living_modifier_negative`.

You must also create a [modifier type](https://vic3.paradoxwikis.com/Modifier_type) named `state_(religion name)_standard_of_living_add`, which is used by the [effect](Effect.md) `add_religion_standard_of_living_modifier`. Examples of these definitions for vanilla religions can be found at /Victoria 3/game/common/static_modifiers/08_religion_standard_of_living.txt and /Victoria 3/game/common/modifier_type_definitions/99_todo_sort_into_other_files.txt

For example:

```
#in static_modifiers
catholic_standard_of_living_modifier_positive = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_positive.dds"
	state_catholic_standard_of_living_add = 1
}

catholic_standard_of_living_modifier_negative = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_negative.dds"
	state_catholic_standard_of_living_add = 1
}
#############################
#in modifier_types
state_catholic_standard_of_living_add = {
	decimals=1
	color=good
	game_data = {
		ai_value=0
	}
}
```

## Religion script documentation

The following [effects](Effect.md), [event targets](Event target.md), and [triggers](Trigger.md) can be used in religion scope.

| Effect | Description | Example | Targets |
|---|---|---|---|

| Trigger | Description | Example | Targets |
|---|---|---|---|
| has_discrimination_trait | Checks if scoped culture or religion has the given discrimination trait | has_trait = trait |  |
| has_religious_taboo | Checks if a religion has a certain goods as taboo | has_religious_taboo = <goods key> |  |
| is_state_religion | Checks if the religion is the state religion in a country | is_accepted_religion = <country> | country |
| shares_heritage_trait_group_with_religion | Checks if the religion shares any heritage trait group with another religion | shares_heritage_trait_group_with_religion = <religion> | religion |
| shares_heritage_trait_with_religion | Checks if religion shares any trait marked as 'heritage' with another religion | shares_heritage_trait_with_religion = <religion> | religion |
| shares_heritage_trait_with_state_religion | Checks if the religion shares any heritage with a country's religion | shares_heritage_trait_with_state_religion = <country> | country |

| Event target | Description | To scope |
|---|---|---|

## References

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • Religion • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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
