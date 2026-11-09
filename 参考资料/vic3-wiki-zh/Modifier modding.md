---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Modifier modding
source: https://vic3.paradoxwikis.com/Modifier_modding
pageid: 3497
categories: [1.13, Modding]
fetched: 2026-10-27
---
本文已针对当前游戏[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

另请参见：
修改器类型
静态修改器
**游戏文件夹 该类型的文件所存储的文件夹。 ：** `common/static_modifiers`

---

**图标文件夹 该类型的原版游戏图标通常存放的文件夹。 ：** `gfx/interface/icons/timed_modifier_icons`

---

**可注入 该类型是否可以使用 INJECT 数据库函数？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) 是 **可替换 该类型是否可以使用 REPLACE 数据库函数？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) 是

---

**相关游戏对象：** [修改器类型](Modifier types.md)

**修改器**是影响游戏玩法的数值容器。修改器使用[修改器类型](Modifier types.md)来定义其效果。修改器可以定义为*静态修改器*（有时也称为*事件修改器*），也可以定义在各种脚本类型中，例如[技术](Technology modding.md)、[法律](Law modding.md)等。

## 静态修改器

静态修改器定义于 /common/static_modifiers，例如：

```
splendid_coastal_state = { # This is the static modifier
    icon = gfx/interface/icons/timed_modifier_icons/modifier_gear_positive.dds # This is an icon, and it is optional
    state_infrastructure_add = 20 # This is a modifier type
    character_popularity_add = 100 # You can add whatever modifier types you want, but be mindful of the scope
}
```

一个静态修改器可以使用任意数量的[修改器类型](Modifier types.md)，但请注意每个修改器类型的*作用域流向*（flow），如果静态修改器被应用于错误的作用域（scope），它们可能不会产生任何效果。

### 静态修改器的 effect 与 trigger

要应用一个静态修改器，可使用 [effect](Effect.md)（游戏内效果脚本）`add_modifier`：

```
add_modifier = { # Applies a modifier to the current scope
    name = splendid_coastal_state # the static modifier you want
    multiplier = -3 # Optional, multiply modifier type values by a number, script value, or math block
    is_decaying = no # Optional, if yes, it will decay over its lifetime, default is no
    months = 3 # Optional, if it is not set or negative, the modifier is permanent. Can also use days, weeks, or years instead.
}
```

multiplier 值会调整静态修改器的基础数值。这可以反转或缩放静态修改器的效果。

也可以使用简写形式 `add_modifier = static_modifier_name`，它等价于

```
add_modifier = {
    name = static_modifier_name
    multiplier = 1 #i.e., no multiplier
    is_decaying = no
    months = -1 #i.e., permanent
}
```

effect `remove_modifier = static_modifier_name` 会从当前作用域中移除指定的静态修改器。

| Effect | 描述 | 示例 | 作用域 | 目标 |
|---|---|---|---|---|
| add_culture_acceptance_modifier | 在作用域国家中为给定文化应用一个文化接受度修改器。除必需的 culture 参数外，该 effect 的语法与 add_modifier 相同。 | add_culture_acceptance_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } | country |  |
| add_culture_standard_of_living_modifier | 在作用域州中为给定文化应用一个生活水平修改器。除必需的 culture 参数外，该 effect 的语法与 add_modifier 相同。 | add_culture_standard_of_living_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } | state |  |
| add_enactment_modifier | 为作用域中的对象添加一个与立法相关的限时修改器效果 | add_enactment_modifier = { name = modifier_key } | country |  |
| add_fervor_target_modifier | 在作用域国家中为给定文化应用一个狂热目标修改器。除必需的 culture 参数外，该 effect 的语法与 add_modifier 相同。 | add_fervor_target_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } | country |  |
| add_modifier | 为作用域中的对象添加一个限时修改器效果 | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay | building, character, country, institution, interest_group, journal_entry, political_movement, power_bloc, state |  |
| add_religion_standard_of_living_modifier | 在作用域州中为给定宗教应用一个生活水平修改器。除必需的 religion 参数外，该 effect 的语法与 add_modifier 相同。 | add_religion_standard_of_living_modifier = { religion = religion_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } | state |  |
| clear_enactment_modifier | 清除作用域国家当前的所有法律立法修改器。 |  | country |  |
| remove_enactment_modifier | 移除作用域中对象的一个与立法相关的限时修改器效果 |  | country |  |
| remove_modifier | 移除作用域中对象的一个限时修改器效果 | remove_modifier = static_modifier_name | building, character, country, institution, interest_group, journal_entry, political_movement, power_bloc, state |  |

[trigger](Trigger.md)（触发条件）`has_modifier = static_modifier_name` 会检查当前作用域中是否存在指定的静态修改器。

游戏所使用的脚本值定义于 /Victoria 3/game/common/script_values/event_values.txt

## 修改器块

许多脚本类型可以包含一个或多个修改器块。它们通常定义为 `modifier = { }` 或类似的块。它们的工作方式与静态修改器完全相同，区别在于它们会自动应用于某个特定作用域，而不是通过 effect 添加。

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [修改器类型](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [决议](Decision modding.md) • [事件](Event modding.md) • [历史](History modding.md) • [日志](Journal modding.md) • 修改器 • 目标 • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [建筑](Building modding.md) • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [可自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图像](Event images.md) • [图形资产](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [声音](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [Mod](Mod.md) • [Mod 兼容性](Mod compatibility.md) • [Mod 结构](Mod structure.md) • [脚本测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [Mod 翻译](Mod translation.md) • [新国家 Mod 制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州 Mod 制作指南](State modding guide.md) |
|---|---|