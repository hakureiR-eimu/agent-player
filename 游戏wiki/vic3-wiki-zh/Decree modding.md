---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Decree modding
source: https://vic3.paradoxwikis.com/Decree_modding
pageid: 6773
categories: [Potentially_outdated, 1.10, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。至少部分章节最后一次核实是在 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10 时进行的。

《维多利亚3》中的[法令](Decrees.md)（Decree）允许为特定州添加 modifier。

## 法令定义

法令定义于 /Victoria 3/game/common/decrees。基本定义包括脚本名、贴图、花费、modifier 以及 AI 权重。例如：

```
decree_promote_social_mobility = {	#Any unique script name
	texture = "gfx/interface/icons/decree/decree_promote_social_mobility.dds"	#An image file
	modifier = {	#List of modifiers, can be left out if decree is used for triggers only
		state_education_access_add = 0.25
		state_pop_qualifications_mult = 0.25
	}
	cost = 100	#Cost in authority to apply the decree
	
	ai_weight = {	#Script value for AI to decide to use the decree, triggers in state scope
		value = 0

		[script values]
	}
}
```

法令的统治力花费受 modifier `country_decree_cost_mult` 影响，并且 define `MIN_DECREE_COST` 限制了最大折扣幅度。

脚本名可以是任意内容，且脚本名还会生成本地化键：`[script name]` 和 `[script_name]_desc`。脚本名用于 trigger，因此使用清晰但唯一的名称是好的做法。

每个法令还可以编写以下附加特性：

| 元素 | 描述 |
|---|---|
| unlocking_technologies | 一份[技术](Technology modding.md)列表，必须研究其中之一才能使用该法令，功能上相当于“拥有这些技术之一”的 trigger 简写 |
| unlocking_laws | 一份[法律](Law modding.md)列表，必须通过其中之一才能使用该法令，功能上相当于“拥有这些法律之一”的 trigger 简写 |
| country_trigger | 一个 trigger 块，必须对国家返回 true 才能使用该法令；若为 false，还会禁用并隐藏该法令 |
| state_trigger | 一个 trigger 块，必须在给定州返回 true 才能使用该法令；若为 false，还会禁用该法令 |

## 参考

Mod 模组制作
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • Decrees • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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