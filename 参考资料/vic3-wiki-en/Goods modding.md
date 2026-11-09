---
title: Goods modding
source: https://vic3.paradoxwikis.com/Goods_modding
pageid: 5327
categories: [Potentially_outdated, 1.9, Articles_with_potentially_outdated_sections, Modding]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.9.

[Goods](Goods.md) are one of the foundational pillars of Victoria 3. Thus adding new goods is something that is central to many mods that add new buildings or production methods.

## Goods

Goods
**Game folder The folder where the files for this type are stored. :** `common/goods`

---

**Icon folder The folder where base game icons for this type typically go. :** `gfx/interface/icons/goods_icons`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**Related game objects:** [Production methods](Building modding.md), Needs

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.9. |
|---|---|

Goods are defined in /common/goods/.

Most basic goods follow the following format:

```
<good> = {
	texture = <path> # GFX reference used to define equipment picture in lend-lease
	cost = <int> # The base cost
	category = staple # staple/industrial/luxury/military

	prestige_factor = 5 # Base prestige for occupying the rank MIN_PRESTIGE_AWARD spot on the goods production leaderboard. x2 awarded for every rank above the minimum.
}
```

Further, the following characteristics can be added:

| consumption_tax_cost = <int> | Authority cost to turn on consumption tax for this good |
|---|---|
| local = yes | Makes good local to the state, like Electricity, Services, Transportation. |
| tradeable = no | Disallows trading of the good. Only used for gold in base game. |
| fixed_price = yes | Used for gold. Used to create a permanent "fake demand" set at the base price, to pay employees and dividends. |

Every local good is also automatically not tradable.

While currently only gold uses both "tradable = no" and "fixed_price = yes", there is nothing that prevents mixing various characteristics. A non-tradable good that is not local, for example, describes pre-1.5 electricity and services. A fixed_price good could be used as an input.

### Prestige goods

Prestige goods
**Game folder The folder where the files for this type are stored. :** `common/prestige_goods`

---

**Icon folder The folder where base game icons for this type typically go. :** `gfx/interface/icons/goods_icons/prestige_goods`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**Related game objects:** Companies

Prestige goods are defined in common/prestige_goods/. Each prestige good defines its base good and an icon. There is also a `prestige_bonus` parameter, with unclear function. For example:

```
prestige_good_krupp_guns = {
	base_good = artillery
	prestige_bonus = 0.1
	texture = "gfx/interface/icons/goods_icons/prestige_goods/krupp_guns_prestige.dds"
}
```

Only three prestige goods can be defined for any given base good. The first three defined are used, and any later definitions are "merged" into the third definition. In unmodified Victoria 3, there is a distinction between "flavored" and "generic" prestige goods, which is driven by a mechanic that prevents immediate production of "generic" prestige goods. This is set via a [journal entry](https://vic3.paradoxwikis.com/Journal_entry_modding) which sets a [variable](Variable.md) on a given company.

## Text icon

Each good should have an icon defined in /gui/. See /Victoria 3/game/gui/goods_texticons.gui for the base game examples.

```
texticon = {
	icon = <good>
	iconsize = {
		texture = <path>
		size = { 25 25 }
		offset = { 0 7 }
		fontsize = 18
	}
}
```

## Localization

See also:
Localization
Each good must be localized in a .yml file in the localization folder within your mod.

```
 <good>: "X"
```

## Goods categories

See also:
Interface modding
Adding new goods category (staple, luxury etc.) seems possible, but is a complicated process involving editing a bunch of GUI and GFX.

Feel that something is missing in this article?
+
Add it to this article
and help other players!
Please note the
style guidelines
.

## Implementation

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.9. |
|---|---|

### Building use

See also:
Modifier types § Object-based modifiers
For a good to be produced and consumed by production methods there needs to be a modifier in /common/modifier_type_definitions/.

The relevant entries look like this:

```
goods_input_<good>_add = {
	decimals=1
	color=bad
	game_data={
		ai_value=0
	}
}
goods_output_<good>_add = {
	decimals=1
	color=good
	game_data={
		ai_value=0
	}
}
```

Multiplier modifiers can also be defined as:

```
goods_input_<good>_mult={
	decimals=0
	color=bad
	percent=yes
	game_data={
		ai_value=0
	}
}
goods_output_<good>_mult={
	decimals=1
	color=good
	percent=yes
	game_data={
		ai_value=0
	}
}
```

In addition, following localization needs to be added:

```
 modifier_goods_output_<good>_add:0 "@<good>! Videogames output per level"
 modifier_goods_output_<good>_add_desc:0 "The amount of @<good>! Videogames produced by buildings"

 modifier_goods_input_<good>_add:0 "@<good>! Videogames input per level"
 modifier_goods_input_<good>_add_desc:0 "The amount of @<good>! Videogames consumed by buildings"
```

### Pop consumption

Pop needs
**Game folder The folder where the files for this type are stored. :** `common/pop_needs`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**Related game objects:** Goods, [Pops](Pop modding.md), Buy packages

See also:
Needs
To have pops consume the good, there needs to be an entry in /common/pop_needs/.

#### Adding to existing need

Adding a good as a substitute is rather simple, using the crude items need as an example here:

```
# goods						The good being referenced
# weight					The base weight that is applied to this good based on market Sell Order share
# max_supply_share			The maximum weight that can be applied to this good based on market Sell Order share, relative supply above this amount will have no further impact on base weight
# min_supply_share			If above 0, a minimum of this multiplier of the base weight will be applied to a good regardless of its market Sell Order share

INJECT:popneed_crude_items = {
	entry = {
		goods = <good>
		
		weight = 2
		max_supply_share = 1.0
		min_supply_share = 0.0
	}
}
```

Needs can also define modifiers to obsession demand multipliers and prestige good demand increases. These are done at the need level, not at the goods level. For example:

```
popneed_leisure = {
	default = services
	
	obsession_demand_min = 0.5 #Obsessions have this minimum share weight, overriding smaller defined minimums
	obsession_demand_mult = 2.0 #Obsessions multiply their demand weight multiplied by this
	prestige_goods_demand_increase = 1.0 #Prestige goods add this to their demand weight, scaled by percentage of the market share
```

#### Creating a new need

Creating a completely new need is more complicated and requires more work but not that much harder.

First, a completely new need needs to be created in /common/pop_needs/.

```
popneed_<name> = {
	default = <good> 

	entry = {
		goods = <good>
	}
}
```

And following localization entry:

```
popneed_<name>: "Digital Entertainment"
```

The default good is what substitutes orient themselves around. Usually the most basic, initial and cheapest good. E.g. even the `popneed_art` has `services` as a default.

Weight, and min and max are not needed if there is only a single good.

Buy packages
**Game folder The folder where the files for this type are stored. :** `common/buy_packages`

---

**Injectable Can INJECT database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **Replaceable Can REPLACE database functions be used with this type? :** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**Related game objects:** Pop needs, [Pops](Pop modding.md)

Then the `buy_package` must be modified in /common/buy_packages/.

```
INJECT:wealth_1 = {
	goods = {
		popneed_<name> = <int>
	}
}
INJECT:wealth_2 = {
	goods = {
		popneed_<name> = <int>
	}
}
...
INJECT:wealth_99 = {
	goods = {
		popneed_<name> = <int>
	}
}
```

The new need then needs to be added to **every** relevant wealth level. So, if this is a need that pops of between SoL 15 and 40 should have, then that means adding the entry to `wealth_15`, `wealth_16`, `wealth_17`, `wealth_18`, `wealth_18`...`wealth_39`, `wealth_40`.

The integer value decides on how much money must be spend on this good to satisfy the need by one "Normal" pop size. For more info, refer to [Needs#Formulas](Needs.md) Various people have already come up with various scripts and tools to help automate this process. One such tool would be [Vic3 Dev Utilities](https://github.com/Imperia-Development-Victoria-3/Victoria-3-dev-utilities)

## Discoverability

See also:
Discoverable goods
Even though both colloquially and in most instances of tooltips and the like, people talk of discovering goods (e.g. "discovering oil"), this is actually exclusively handled through building groups and states.

See: [Building modding#Resource caps and farm types](Building modding.md)

## References

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • Goods • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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
