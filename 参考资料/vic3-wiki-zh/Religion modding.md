---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Religion modding
source: https://vic3.paradoxwikis.com/Religion_modding
pageid: 6776
categories: [Potentially_outdated, 1.11, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。至少部分内容最后核实时为 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.11。

参见：
Culture modding
**《维多利亚3》中的宗教（Religion）代表了人口（Pops）与国家的抽象化信仰。**

## 宗教定义

宗教定义于 /Victoria 3/game/common/religions。其定义包含一个脚本名、贴图、特质、颜色，以及可选的禁忌。

例如：

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

脚本名既用作 localizatio n 键（本地化键），也用于 trigger 和 effect。

- 图标是一个图像文件。
- 颜色为 RGB 十进制格式。
- 血统可以是任意血统特质。
- 颜色用于界面和地图颜色标记。

每个宗教还可以有一个 `taboo` 块，列出一种或多种该宗教视为禁忌的可消费商品。禁忌数量是否有上限尚不清楚。

## 歧视特质

[Cultures](Culture modding.md) 和宗教都使用定义于 /Victoria 3/game/common/discrimination_traits/ 的歧视特质。每个特质由唯一的脚本名和块定义。每个特质有一个 `type`，可以是 `heritage`、`language` 或 `tradition`。脚本名同时也是一个 localization 键。

例如：

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

前缀只是为了便于引用和分类。

除了在文化定义与宗教定义中的用途不同外，文化特质与宗教特质并无区别。宗教只使用血统（heritage）特质，不使用语言或传统特质。

血统和语言特质还有一个特质组，代表一组相似的特质。

### 特质组

歧视特质组定义于 /Victoria 3/game/common/discrimination_trait_groups/。特质组与特质完全相同，只是不能是 tradition 类型，也没有更进一步的组。

例如：

```
language_group_germanic = { # a language trait group
	type = language
}

heritage_group_african = { # a heritage trait group
	type = heritage
}
```

## 修正定义

参见：
Modifier types
,
Modifier modding
创建宗教时，还必须创建两个[静态修正](Modifier modding.md)，分别命名为 `(religion name)_standard_of_living_modifier_positive` 和 `(religion name)_standard_of_living_modifier_negative`。

还必须创建一个名为 `state_(religion name)_standard_of_living_add` 的[修正类型](https://vic3.paradoxwikis.com/Modifier_type)，它被 [effect](Effect.md)（游戏内效果脚本）`add_religion_standard_of_living_modifier` 所使用。原版宗教的这些定义示例可见于 /Victoria 3/game/common/static_modifiers/08_religion_standard_of_living.txt 和 /Victoria 3/game/common/modifier_type_definitions/99_todo_sort_into_other_files.txt

例如：

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

## 宗教脚本文档

以下 [effects](Effect.md)、[event targets](Event target.md) 和 [triggers](Trigger.md) 可在宗教 scope 中使用。

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| has_discrimination_trait | 检查 scope 中的文化或宗教是否具有给定的歧视特质 | has_trait = trait |  |
| has_religious_taboo | 检查宗教是否将某种商品视为禁忌 | has_religious_taboo = <goods key> |  |
| is_state_religion | 检查该宗教是否为某国的国教 | is_accepted_religion = <country> | country |
| shares_heritage_trait_group_with_religion | 检查该宗教是否与另一宗教共享任意血统特质组 | shares_heritage_trait_group_with_religion = <religion> | religion |
| shares_heritage_trait_with_religion | 检查该宗教是否与另一宗教共享任意标记为 "heritage" 的特质 | shares_heritage_trait_with_religion = <religion> | religion |
| shares_heritage_trait_with_state_religion | 检查该宗教是否与某国的宗教共享任意血统 | shares_heritage_trait_with_state_religion = <country> | country |

| Event target | 描述 | 转至 scope |
|---|---|---|

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • Religion • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|---|

| 地图 | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • [States](State modding.md) |
|---|---|---|

| 界面 | [Interface](Interface modding.md) • [GUI script](GUI script.md) • [Localization](Localization.md) • [Customizable localization](Localization.md) • [Script localization](Script localization.md) |
|---|---|---|

| 图形 | [3D Models](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|---|

| 音频 | Music • [Sound](Sound modding.md) |
|---|---|---|

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|---|