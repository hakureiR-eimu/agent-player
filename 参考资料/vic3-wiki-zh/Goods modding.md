---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Goods modding
source: https://vic3.paradoxwikis.com/Goods_modding
pageid: 5327
categories: [Potentially_outdated, 1.9, Articles_with_potentially_outdated_sections, Modding]
fetched: 2026-10-27
---
请帮助核实或更新本条目中较旧的部分。其中至少有一部分最后是针对[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.9 核实的。

[商品](Goods.md)是《维多利亚3》的基石之一。因此，对于许多添加新建筑或新生产方式的 mod 来说，添加新商品是核心工作。

## 商品（Goods）

商品
**游戏文件夹 存储此类文件的文件夹。：** `common/goods`

---

**图标文件夹 原版游戏此类图标通常存放的文件夹。：** `gfx/interface/icons/goods_icons`

---

**可注入（Injectable） 能否对此类型使用 INJECT 数据库功能？：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) 是 **可替换（Replaceable） 能否对此类型使用 REPLACE 数据库功能？：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) 是

---

**相关游戏对象：** [生产方式](Building modding.md)、需求（Needs）

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助核实或更新本节。其最后是针对版本 1.9 核实的。 |
|---|---|

商品定义于 /common/goods/。

最基本的商品遵循以下格式：

```
<good> = {
	texture = <path> # GFX reference used to define equipment picture in lend-lease
	cost = <int> # The base cost
	category = staple # staple/industrial/luxury/military

	prestige_factor = 5 # Base prestige for occupying the rank MIN_PRESTIGE_AWARD spot on the goods production leaderboard. x2 awarded for every rank above the minimum.
}
```

此外，还可以添加以下特性：

| consumption_tax_cost = <int> | 为该商品开启消费税的权威力成本 |
|---|---|
| local = yes | 使商品局限于本州，如电力、服务、运输。 |
| tradeable = no | 禁止该商品的贸易。原版游戏中仅黄金使用。 |
| fixed_price = yes | 用于黄金。用于创建以基础价格设定的永久“虚假需求”，以支付员工工资和分红。 |

每个本地商品也会自动不可贸易。

虽然目前只有黄金同时使用 "tradable = no" 和 "fixed_price = yes"，但没有任何东西阻止混合使用各种特性。例如，一个非本地且不可贸易的商品，描述的就是 1.5 版本之前的电力和服务。固定价格的商品也可以用作投入品。

### 威望商品（Prestige goods）

威望商品
**游戏文件夹 存储此类文件的文件夹。：** `common/prestige_goods`

---

**图标文件夹 原版游戏此类图标通常存放的文件夹。：** `gfx/interface/icons/goods_icons/prestige_goods`

---

**可注入（Injectable） 能否对此类型使用 INJECT 数据库功能？：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) 是 **可替换（Replaceable） 能否对此类型使用 REPLACE 数据库功能？：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) 是

---

**相关游戏对象：** 公司（Companies）

威望商品定义于 common/prestige_goods/。每个威望商品定义其基础商品和图标。此外还有一个 `prestige_bonus` 参数，其功能尚不明确。例如：

```
prestige_good_krupp_guns = {
	base_good = artillery
	prestige_bonus = 0.1
	texture = "gfx/interface/icons/goods_icons/prestige_goods/krupp_guns_prestige.dds"
}
```

任意一个基础商品最多只能定义三个威望商品。最先定义的三个会被使用，之后的任何定义都会被“合并”到第三个定义中。在未经修改的《维多利亚3》中，“特色”威望商品与“通用”威望商品是有区别的，这是由一种阻止立即生产“通用”威望商品的机制驱动的。这是通过一个[日志条目](https://vic3.paradoxwikis.com/Journal_entry_modding)设置的，该日志条目会在指定公司上设置一个[变量](Variable.md)。

## 文本图标

每个商品都应在 /gui/ 中定义一个图标。原版游戏示例参见 /Victoria 3/game/gui/goods_texticons.gui。

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

## 本地化（Localization）

另见：
本地化
每个商品都必须在你的 mod 内的 localization 文件夹中的 .yml 文件中进行本地化。

```
 <good>: "X"
```

## 商品类别

另见：
界面 mod 制作
添加新的商品类别（如 staple、luxury 等）似乎是可行的，但这是一个复杂的过程，涉及编辑大量 GUI 和 GFX。

觉得这篇文章缺少了什么？
+
把它添加到本条目中，
帮助其他玩家！
请注意
样式指南。

## 实现

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助核实或更新本节。其最后是针对版本 1.9 核实的。 |
|---|---|

### 建筑使用

另见：
Modifier types § 基于对象的修改器
要让一种商品能被生产方式生产和消耗，需要在 /common/modifier_type_definitions/ 中有一个 modifier（修改器）。

相关条目如下所示：

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

倍率型 modifier 也可以定义为：

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

此外，还需要添加以下本地化：

```
 modifier_goods_output_<good>_add:0 "@<good>! Videogames output per level"
 modifier_goods_output_<good>_add_desc:0 "The amount of @<good>! Videogames produced by buildings"

 modifier_goods_input_<good>_add:0 "@<good>! Videogames input per level"
 modifier_goods_input_<good>_add_desc:0 "The amount of @<good>! Videogames consumed by buildings"
```

### 人口消费

人口需求（Pop needs）
**游戏文件夹 存储此类文件的文件夹。：** `common/pop_needs`

---

**可注入（Injectable） 能否对此类型使用 INJECT 数据库功能？：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) 是 **可替换（Replaceable） 能否对此类型使用 REPLACE 数据库功能？：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) 是

---

**相关游戏对象：** 商品、[人口](Pop modding.md)、购买包（Buy packages）

另见：
需求（Needs）
要让人口消费该商品，需要在 /common/pop_needs/ 中有一个条目。

#### 添加到现有需求

将一种商品作为替代品添加相当简单，这里以简陋物品需求为例：

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

需求还可以定义对痴迷需求倍率以及威望商品需求增加的 modifier。这些是在需求层面而非商品层面完成的。例如：

```
popneed_leisure = {
	default = services
	
	obsession_demand_min = 0.5 #Obsessions have this minimum share weight, overriding smaller defined minimums
	obsession_demand_mult = 2.0 #Obsessions multiply their demand weight multiplied by this
	prestige_goods_demand_increase = 1.0 #Prestige goods add this to their demand weight, scaled by percentage of the market share
```

#### 创建新需求

创建一个全新的需求更复杂，需要更多工作量，但并没有难多少。

首先，需要在 /common/pop_needs/ 中创建一个全新的需求。

```
popneed_<name> = {
	default = <good> 

	entry = {
		goods = <good>
	}
}
```

以及以下本地化条目：

```
popneed_<name>: "Digital Entertainment"
```

默认商品是替代品围绕其定位的商品。通常是最基础、最初级、最便宜的商品。例如，即使是 `popneed_art` 也以 `services` 作为默认值。

如果只有一种商品，则不需要 weight 以及 min 和 max。

购买包（Buy packages）
**游戏文件夹 存储此类文件的文件夹。：** `common/buy_packages`

---

**可注入（Injectable） 能否对此类型使用 INJECT 数据库功能？：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) 是 **可替换（Replaceable） 能否对此类型使用 REPLACE 数据库功能？：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) 是

---

**相关游戏对象：** 人口需求、[人口](Pop modding.md)

然后必须在 /common/buy_packages/ 中修改 `buy_package`。

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

新需求随后必须被添加到**每一个**相关的财富等级中。因此，如果这是一个生活水平（SoL）在 15 到 40 之间的人口应拥有的需求，那就意味着将该条目添加到 `wealth_15`、`wealth_16`、`wealth_17`、`wealth_18`、`wealth_18`……`wealth_39`、`wealth_40`。

整数值决定了必须在该商品上花费多少钱才能让一个“Normal”规模的人口满足该需求。更多信息请参见[需求#公式](Needs.md)。已经有人编写了各种脚本和工具来帮助自动化这一过程。其中一个工具是 [Vic3 Dev Utilities](https://github.com/Imperia-Development-Victoria-3/Victoria-3-dev-utilities)。

## 可发现性

另见：
可发现商品
尽管无论是口语中还是在大多数工具提示等场合，人们都谈论发现商品（例如“发现石油”），但实际上这完全是通�过建筑组和州来处理的。

参见：[建筑 mod 制作#资源上限与农场类型](Building modding.md)

## 参考

Mod 制作
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • Goods • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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