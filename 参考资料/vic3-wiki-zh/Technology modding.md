---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Technology modding
source: https://vic3.paradoxwikis.com/Technology_modding
pageid: 5749
categories: [Potentially_outdated, 1.11, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。至少部分内容最后是针对 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.11 验证的。

[Technologies](https://vic3.paradoxwikis.com/Technologies) 代表物质、社会与政治方面的发明。每项技术可以解锁各种其他机制，提供直接的 [modifier](Modifier types.md) 效果，或两者兼有。

## 技术示例

技术定义始终包含一个时代（era）、一个类别、一个贴图和一个 AI 权重。大多数技术还包含前置解锁技术列表，并可能包含一系列 modifier。

```
nitroglycerin = {
	# Unlocks Nitroglycerin PM in Coal, Iron, Lead, Sulfur Mines
	# Unlocks Ammonia-Soda Process PM in Chemical Industries
	# Countries get a +25% chance of discovering new resources
	
	era = era_2
	texture = "gfx/interface/icons/invention_icons/nitroglycerin.dds"
	category = production
	
	modifier = {
		country_resource_discovery_chance_mult = 0.25
	}
	
	unlocking_technologies = {	
		intensive_agriculture
		prospecting
	}
	
	ai_weight = {
		value = 1
	}
}
```

## 技术时代

技术时代定义了每项技术的基础成本。技术时代定义于 /Victoria 3/game/common/technology/eras。每个时代都是一个简单的列表，包含一个唯一的脚本名称作为一个块，以及一个技术成本。该成本是在没有任何成本修正的情况下研究该技术所需的创新点数。

```
era_1 = { #Pre-1836
	technology_cost = 7500 # for progress bonuses, use an approximate third: 2500
}
```

时代的脚本名称还会与 effect `add_era_researched` 一起使用，该 effect 会解锁该时代的所有技术。

## 技术条目

技术定义于 /Victoria 3/game/common/technology/technologies。每项技术都被定义为一个具有唯一脚本名称的块，该名称同时充当 [localization](Localization.md) 键。在该块内，技术必须定义时代、贴图、类别和 AI 权重。技术还可以包含一个 modifier 块和一个解锁技术列表——即在此技术可以研究之前必须先研究的前置技术。解锁建筑、法律或其他类似内容的技术并不会把这些解锁内容包含在自身定义中，而是列在它们所解锁的条目或机制的定义里。还可以通过添加 `can_research = no` 将技术从技术界面中隐藏，这使该技术只能通过 effect 获得，并且只在被研究后显示。

| 元素 | 取值 | 必需 |
|---|---|---|
| `era` | 时代脚本名称 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| `texture` | 图像文件路径 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| `category` | `production`、`military` 或 `society` | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| `ai_weight = { }` | [script value](Script value.md) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| `modifier = { }` | [modifier 类型](Modifier types.md) 列表 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| `unlocking_technologies = { }` | 技术列表 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| `can_research` | `yes` 或 `no` | ![No](/images/thumb/0/04/No.png/24px-No.png) |

## 实操指南

### 定义时代

在你的 /<mod>/common/technology/eras 文件夹中，创建一个任意名称的 .txt 文件，例如 "01_my_eras.txt"

在 "01_my_eras.txt" 中，创建一个新的时代块并写入其技术成本：

```
cool_era = { #Post-1936
	technology_cost = 20000 # for progress bonuses, use an approximate third: 7000
}
```

游戏会按时代本身的顺序及其所在文件的顺序读取时代。因此 01_my_eras.txt 会排在原版的 00_eras.txt 之后，从而新添加的时代在游戏中会作为“时代 6”或"VI"追加到原版时代之后。technology_cost 不需要线性递增，可以设置为任意所需的数值。

如果你沿用原版时代，可以跳过这一步，但请记得为你添加的任何技术指定正确的时代。

### 定义一项技术

在 /<mod>/common/technology/technologies 文件夹中，创建一个新的任意名称的 .txt 文件，例如 "40_my_techs.txt"

如果你想修改某项原版技术，将其条目复制到你的新文件中并进行修改。如果你的文件在 ASCII 排序中位于原版文件之后，你修改后的条目将覆盖原版条目。这不仅能更容易地与其他 mod 保持兼容，也能让新版本的更新更轻松，因为你的修改仅限于你改动过的技术。

要创建一项新技术，只需在你的文件中添加一个新条目。请注意，解锁其他特性（例如生产方式）的技术必须被添加到那些特性的定义中。另外请记住，技术的时代应当等于或晚于所有前置技术，否则可能导致技术成本出现问题。

```
technicolor = {
	era = cool_era
	texture = "gfx/interface/icons/invention_icons/<new icon>.dds"
	category = society
	
	modifier = {
		country_prestige_mult = 0.1 #color film is awesome!
	}
    
	unlocking_technologies = {	
		mass_propaganda
	}
	
	ai_weight = {
		value = 1
	}
}
```

## 参考

Mod 制作
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier 类型](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • Technology • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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