---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Institution modding
source: https://vic3.paradoxwikis.com/Institution_modding
pageid: 4732
categories: [Potentially_outdated, 1.11, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。其中至少部分内容最后核实于 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.11。

《维多利亚3》中的[机构](Institutions.md)（Institutions）是一种向已整合的州施加 [modifier](Modifier modding.md)（游戏内修正脚本）的机制。为机构制作 mod 通常涉及修改若干相关概念。

## 机构定义

机构定义于 /Victoria 3/game/common/institutions。基本定义包括一个脚本名、图标、背景纹理，以及一个可选的基础 modifier。例如：

```
institution_home_affairs = {
	icon = "gfx/interface/icons/institution_icons/home_affairs.dds"
	background_texture = "gfx/interface/illustrations/institutions/home_affairs.dds"
	modifier = {
		country_revolution_progress_mult = -0.1
		country_secession_progress_mult = -0.1
	}
}
```

机构的所有其他特性都在其他文件中定义或编写脚本。

## 机构等级

机构等级的上下限设置在 /Victoria 3/game/common/defines/00_defines.txt 中，由 `MIN_INSTITUTION_INVESTMENT` 和 `MAX_INSTITUTION_INVESTMENT` 控制，在原版《维多利亚3》中分别设为 1 和 5。等级上限还受 modifier `country_[institution_script_name]_investment_add` 限制，该 modifier 必须在 /Victoria 3/game/common/modifier_type_definitions 中定义。例如：

```
country_institution_home_affairs_max_investment_add={
	decimals=0
	color=good
	game_data={
		ai_value=0
	}
}
```

在原版《维多利亚3》中，这个 modifier 用于[技术](Technology modding.md)和[法律](Law modding.md)，但它可以应用于任何能使用 modifier 的地方。

从一个等级升降至另一个等级的速度由 define `DAILY_INSTITUTION_SIZE_CHANGE` 设置。modifier `country_institution_size_change_speed_mult` 或已定义的机构专属 modifier `country_institution_size_change_speed_[institution_script_name]_mult` 也能影响这一速度。

## 机构成本

机构每级消耗的行政力定义为 1 乘以 `STATE_BUREAUCRACY_POP_MULTIPLE`。此外还有由 `MINIMUM_INVESTMENT_COST` 定义的最低成本。这一成本可被 modifier `country_bureaucracy_investment_cost_factor_mult` 或已定义的机构专属 modifier `country_institution_cost_[institution_script_name]_mult` 修改。modifier `state_bureaucracy_population_base_cost_factor_mult` 也会通过改变 `STATE_BUREAUCRACY_POP_MULTIPLE` 的有效数值来影响成本。

## 机构 modifier

除了已定义的 modifier 外，还可以向机构动态添加其他 modifier。机构甚至可以拥有完全动态的效果，即省略基础 modifier，仅使用添加的 modifier。

向机构添加额外 modifier 的方式如下：

```
institution = institution_home_affairs	#which institution is affected
institution_modifier = {				#what modifiers are added
	state_conscription_rate_add = 0.005
	political_movement_radicalism_mult = -0.05
}
```

请注意，这些 modifier 会乘以机构的等级，与已定义的基础 modifier 相同；并且所有与州相关的 modifier 只影响已整合的州。在原版《维多利亚3》中，额外 modifier 仅用于法律或强权集团的原则，能否通过其他方式应用尚不明确。

## 启用机构

在原版《维多利亚3》中，所有机构都通过法律启用。在法律中启用机构只需一行脚本：`institution = [institution_script_name]`。其后可以接一个如上所示的 institution_modifier 数据块（data block），也可以单独使用。机构能否通过其他方式启用尚不明确。

## 参考

Mod 制作
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • Institutions • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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