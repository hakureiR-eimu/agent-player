---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Geographic region modding
source: https://vic3.paradoxwikis.com/Geographic_region_modding
pageid: 9339
categories: [1.13, Modding]
fetched: 2026-10-27
---
本文已针对游戏当前 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

**地理区域**（Geographic regions），也称为 *Georegions*，是在脚本中定义的 [州区域和/或战略区域](State modding.md) 的静态列表。它们可以在脚本中被迭代，有助于降低迭代的复杂度，并且游戏引擎对其性能支持更好。在 [localization](Localization.md)（本地化）中使用时，将鼠标悬停在地理区域名称上会在游戏地图上高亮显示所有包含的州区域。地理区域可以用于将州区域与战略区域分开分组，还可以包含更抽象的区域，例如气候带或海岸线。

*出于性能原因，游戏开发者强烈推荐使用地理区域迭代器。*

## 定义

地理区域在 common/geographic_regions 文件夹中定义。

*所有地理区域文件必须使用 UTF-8 BOM 编码。*

一个地理区域定义由以下元素组成：

- 地理区域键（key），用于调用该地理区域
- 短键（short key），用于迭代器
- 包含的战略区域列表
- 包含的州区域列表

一个地理区域可以包含任意数量的战略区域或州区域，也可以只包含州区域或战略区域。

```
geographic_region_key = {
	# All state/strategic regions are added together to form a geographic region

	# the key to access this in script lists i.e <any/..>_<state/...>_in_europe
	short_key = "europe"

	# The Strategic Regions this geographic region encompasses
	strategic_regions = { sr:<key> sr:<key> sr:<key> }

	# The State Regions this geographic region encompasses
	state_regions = { <STATE_REGION> <STATE_REGION> }
}
```

## 用法

[trigger](Trigger.md)（触发条件）`is_in_geographic_region` 用于检查所在 scope 中的对象是否包含在某个特定地理区域中。它可以在 country、state、state_region 或 strategic_region 这些 scope 中使用。

```
any_scope_state = {
    is_in_geographic_region = geographic_region_south_america
    is_incorporated = yes
    count >= 10
}
```

在 country scope 或国家迭代器中使用时，该 trigger 只检查该国的*首都州*。

### 迭代器

地理区域可以用于以性能更友好的方式迭代任何包含的区域。*游戏开发者强烈推荐此方法，因为 _country 和 _state 迭代器本身开销很高。*

支持的迭代器如下：

- `{any|every|ordered|random}_country_in_<geographic_region_short_key>`
- `{any|every|ordered|random}_province_in_<geographic_region_short_key>`
- `{any|every|ordered|random}_state_in_<geographic_region_short_key>`
- `{any|every|ordered|random}_state_region_in_<geographic_region_short_key>`
- `{any|every|ordered|random}_strategic_region_in_<geographic_region_short_key>`

示例，来自 `je_springtime_of_the_peoples`：

```
	possible = {
		any_country_in_europe = {
			has_technology_researched = egalitarianism
        }
		custom_tooltip = {
			text = peoples_springtime_underway_tt
			has_global_variable = peoples_springtime_happening
		}
	}
```

示例，来自 `je_sale_of_alaska`：

```
		custom_tooltip = {
			text = friendly_nation_with_interest_in_alaska_tt
			any_country_in_north_america = {
				NOT = {
					is_subject = yes
				}
				relations:root >= 0
				country_rank >= rank_value:great_power
				any_scope_state = {
					region = sr:region_pacific_coast
					is_incorporated = yes
				}
			}
		}
```

### 生产方式

地理区域可用于解锁 [生产方式](https://vic3.paradoxwikis.com/Production_methods_modding)，方法是向该生产方式添加 `unlocking_geographic_regions` 并按完整键名列出任意地理区域。例如：

```
	unlocking_geographic_regions = {
		geographic_region_wet_process_coffee_region
	}
```

## 本地化

地理区域的本地化方式如下：

- `<geographic_region_key>` 用于地理区域的名称
- `<geographic_region_key>_desc` 用于地理区域的任何背景/设定描述

例如：

```
 geographic_region_ring_of_fire: "Ring of Fire"
 geographic_region_ring_of_fire_desc: "A chain of seismically active sites and volcanoes around the edge of the Pacific Ocean."
```

在本地化中可以通过 `GetGeographicRegion()` function 以脚本名称调用地理区域。例如：

```
 je_eastern_frontier_tt_1: "[GetGeographicRegion('geographic_region_greater_khorasan').GetName] is owned by [SCOPE.GetRootScope.GetCountry.GetName] or its subjects."
 je_eastern_frontier_tt_2: "[GetGeographicRegion('geographic_region_chorasmia').GetName] is owned by [SCOPE.GetRootScope.GetCountry.GetName] or its subjects."
 je_eastern_frontier_tt_3: "[GetGeographicRegion('geographic_region_transoxiana').GetName] is owned by [SCOPE.GetRootScope.GetCountry.GetName] or its subjects."
```

*在 UI 中将鼠标悬停时，该地理区域会在游戏地图上高亮显示。*

## 参考

Modding
Return to top
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| 地图 | [Map](Map modding.md) • Geographic regions • [States](State modding.md) |
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