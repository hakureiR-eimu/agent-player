---
translated: 2026-10-28
translator: machine (glm-4.7 + dictionary)
title: Introduction to the Paradox Scripting Language
source: https://vic3.paradoxwikis.com/Introduction_to_the_Paradox_Scripting_Language
pageid: 9975
categories: [Timeless, Modding]
fetched: 2026-10-27
---
本文是[常青](https://vic3.paradoxwikis.com/Category:Timeless)内容，对游戏的任何版本均应准确无误。

**脚本**是模组制作者在《维多利亚3》中添加、修改并与内容进行交互的方式。这通过 Paradox 自定义脚本语言来实现。这门语言没有官方名称，社区将其称为“Paradox 脚本语言”，简称“**PDXscript**”。从设计原则上讲，它易于阅读、学习和调试。在《维多利亚3》中，大多数 function 都设计为人类可读的形式，例如 `set_variable` 或 `add_modifier`。

**PDXscript** 用于 `/common` 和 `/events` 文件夹中的内容，包括事件、国家/国旗定义、modifier、文化、商品等内容。

*注意*：*本指南不涵盖以下主题：*

- 同化、贸易、军事编队移动/战斗、工资等的大部分机制。这些机制在“游戏代码”中实现，不对模组制作者开放。我们称这类机制为“硬编码”。这通常出于性能考虑，因为脚本*始终*比代码慢
- GUI 脚本语言用于 `/gui` 文件夹中的文件，是一门独立的脚本语言。PDXscript 无法直接访问 UI 或 UI function。当需要通过 UI 元素执行脚本时，可以使用[Scripted GUIs](Scripted gui.md)。
- `/common/history` 中的[历史](History modding.md)文件。这些文件使用静态脚本系统，但在执行时可以使用脚本 effect。
- 位于 `/map_data/state_regions` 中的[州区域](Map modding.md)文件。这些文件使用一种独特的静态脚本，*仅在游戏启动时读取一次*。
- `/localization` 中的游戏[本地化](Localization.md)。这些文件使用的字符串能够调用 UI function，并可在脚本中调用，例如脚本化按钮的本地化文本或 script value 的分解说明。此外，在某些情况下，本地化 function 会检查脚本端的元素，例如在 `/common/customizable_localization` 或 `/common/trigger_localization` 中。

*注意：一些开发者偶尔会将脚本称为“Jomini script”。这是因为它是更庞大的 Jomini 共享库的一部分。“Clausewitz”则是游戏引擎的名称。*

## 概述

这是一份快速指南，帮助你学习并使用《维多利亚3》中的 PDXscript。

本指南应能为你打下扎实的模组制作基础，但无法替代你自己的实践。一般而言，良好的做法是在原版游戏或其他模组中寻找你所需脚本的示例，或者如果你对某个 effect 或 trigger 的用法和实现感到好奇，可以在文件中搜索其用例。你也可以通过[Victoria 3 Mod Co-op](https://discord.gg/pJCJ8H7HB7)与模组社区交流。

### 文档

《维多利亚3》拥有内置的脚本文档。可以通过在运行时执行控制台命令 `script_docs` 来生成。

文档文件将生成在 `~\Paradox Interactive\Victoria 3\docs`。

这些文件会列出以下重要信息：

- **Effects**（effect）- 用于以某种方式改变游戏状态。
- **Triggers**（trigger）- 用于检查游戏状态的特定方面。
- **Event Targets**（event target）- 用于在脚本执行过程中改变 scope。

脚本文档还包括以下信息：

- **Custom Localizations**（自定义本地化）- 已编译的自定义本地化列表。它们在本地化文本中被调用，可根据脚本定义的 trigger 改变显示的文本。
- **Modifiers**（modifier）- 所有可用 [modifier类型](Modifier types.md) 的列表。它们用于构建游戏内使用的[静态修正](Modifier modding.md)。
- **on_actions** - 所有可用 [on actions](On action.md) 的列表。它们用于在游戏过程中发生特定行动时执行[事件](Event modding.md)或[effect](Effect.md)。

**局限性：**

PDXscript 是一个极其强大且灵活的工具，可以重塑游戏。但它有以下局限：

- 无法直接访问 UI 或任何 UI 专属的值
- 无法访问操作系统或用户输入
- 无法进行字符串操作
- 比“在代码中”执行的 function 慢得多

### 调试

- 脚本问题通常会将错误打印到日志中。日志位于 `~\Paradox Interactive\Victoria 3\logs`。在排查脚本无法运行的原因时，这里应当是你的第一站。
  - *警告*：如果你遇到 CTD（崩溃回到桌面，crash-to-desktop），导致游戏崩溃的错误通常不会打印到错误日志中。这意味着日志中的最后一条错误并不一定就是真正导致崩溃的错误。
- 使用 `-debug_mode` 启动选项启动《维多利亚3》将同时启用[控制台命令](Console commands.md)和文件热加载
  - **对象浏览器（Object Explorer）** 可以通过脚本运行器来测试脚本
- amtep 的 [Tiger Validator](https://github.com/amtep/tiger) 为《维多利亚3》提供深入的脚本验证

### 术语

《维多利亚3》有一套大量的行话用于非正式地指代脚本特性，其中许多与其他 Paradox 模组社区通用：

- **Script（脚本）：** 模组制作者用来改变游戏运作方式的“代码”。
- **Effect（effect）：** 对游戏状态执行某种更改的脚本
- **Trigger（trigger）：** 检查游戏状态的脚本；主要用于为 effect/事件设置条件
- **Scope（scope）：** trigger 或 effect 的上下文；也用于表示将上下文切换到某个对象，例如“切换到某个国家”
- **Scope Link / Event Target（scope 链接 / event target）：** 表示某个 scope 或游戏值的关键字
- **Type（类型）：** 游戏对象的“类”
- **Key（键）：** 某个类型的脚本名称
- **Tag/TAG：** 国家的键，例如法国这个国家为 `FRA`
- **Logs（日志）：** 打印到 `~/Paradox Interactive/Victoria 3/logs` 的游戏日志；其中通常包含错误或脚本冲突的相关信息
- **Docs（文档）：** 开发团队提供的游戏内文档。通常位于相关脚本所在目录中。生成的**脚本文档**也包含在此术语中。
- **CTD：** “crash to desktop”（崩溃回到桌面）的缩写；指导致游戏意外关闭的错误
# 基础

本指南假设你已经设置好了模组文件夹，并正在创建/修改内容。初次设置模组请参见模组结构。

### 语法与格式

##### 脚本结构

PDXscript 使用如下结构的语句：

`<lvalue> <operator> <rvalue>`

游戏将其称为"left value"（左值）、"operator"（运算符）和"right value"（右值），文档和日志中也会使用这些称呼。所有脚本操作都*必须*有一个有效的"左值"和"右值"，并用运算符连接。

一般来说，语句的结构大致如下之一：

- `x = y` – "简单"语句
- `x = { y = z }` – "复杂"或"块"语句

示例：

- `is_subject = yes`
- `add_treasury = 100`
- `debug_log = "hello world"`
- `overlord = { add_modifier = modifier_regency }`

##### 代码块与缩进

简单的 trigger 和 effect 通常写作 `x = y` 的形式，但更复杂的脚本或任何参数都需要使用花括号（`{}`）。这被称为**代码块（block）**。

缩进风格以及空白字符对脚本本身的执行没有任何影响。但是，**缩进对可读性和调试至关重要**。

一般来说，每个代码块的缩进都应清楚地表明各 effect、trigger 和 scope 之间的关系。Paradox 在其脚本中使用的风格似乎类似于 *Kernighan & Ritchie (K&R) 风格*，这一风格也已被模组制作社区广泛采用。
```
c:GBR = {
    add_treasury = 50000
}
```

每个代码块都以一个左值（lvalue）和一个运算符开头。花括号内的内容充当其右值（rvalue）。这些花括号内的每条语句本身也必须遵循 `<lvalue> <operator> <rvalue>` 的结构。

**注意：** *某些代码块是“列表块”（list blocks），不遵循这一约定。这些例外会在各自对应的 wiki 页面上注明。*
###### Script comments

The # symbol will turn everything after it in the same line into a "comment." This means that it will be ignored by the engine when compiling your script. You can use this to leave notes for yourself or others regarding your script. There are no multi-line comments, so each comment line must start with #.


### Scopes（作用域）与 targets（目标）

##### Scopes（作用域）

关于 scope 的更多信息请参阅
Scope
页面。
Scope 是用于评估 trigger 和执行 effect 的游戏对象。Trigger 和 effect 在特定的 scope 中运行。Scope 可以是国家、州、人口、建筑等等。全局 trigger 和 effect 可以在任何 scope 中使用。

脚本内容通常有一个基础 scope，取决于其执行的发起位置。这被称为 **root**（根）scope。对大多数脚本内容而言，该 scope 是接收该内容的国家。脚本可以通过使用 **event target** 来切换 scope，例如把 scope 从一个*建筑*切换到它的*所有者*。
##### 切换 scope

关于 event target 的更多信息，请参阅
Event targets。
**Event target**（也称 *Scope Link*）允许我们从一个 scope 切换到另一个 scope（社区称之为 "scoping"）。例如：

```
# This starts in the country scope
ruler = { # Now we have changed to the character scope for the country's ruler
  interest_group = { # Finally, we change to the interest group that the ruler is a member of.
    add_modifier = modifier_failed_coup
  }
}
```

某些 event target 还**需要数据**才能运作。例如：

```
# This is the country event target. In this case, the target scopes to a country with the GBR definition.
c:GBR = {}

# This is the state region target. In this case, the target scopes to the STATE_ATTICA state region.
s:STATE_ATTICA = {}

# This is the market goods target. In this case, the target scopes to the meat good within a market scope.
market = {
  mg:meat = {}
}
```

某些 event target 是**全局链接（global links）**。这意味着它们可以在任何 scope 中调用。例如：

```
# This will always scope to a country with the definition "FRA"
c:FRA

# This will always scope to the "catholic" religion
rel:catholic

# This will always scope to the "liberal" ideology
ideology:ideology_liberal
```

*可用的 event target 列在 docs/event_targets.log 中，其中包含有关所支持的输入与输出 scope 的信息。*

##### 链式 scope

可以使用**点号连接（dot linkage）**将 scope 链接起来，例如 `a.b.c`

例如，以下脚本：

```
ruler.interest_group.ig_clout = {}
```

等价于：

```
ruler = {
  interest_group = {
    ig_clout = {}
  }
}
```

### 特殊目标

`root` - 某个脚本实例的*起始 scope（origin scope）*。它会随脚本执行的位置而变化。虽然它通常是国家 scope，但这既不是约定，也不保证一致。

`prev` - scope 链中的*上一个 scope*。它可用于访问某个特定 scope 中可用的对象，并快速返回原来的 scope。`prev` 目标可以链式使用，从而在 scope 链中"向后回溯"，例如 `prev.prev = {}`

`this` - *当前 scope*。用于在你切换到某个对象之后比较其身份。它常与**迭代器（iterators）**一起使用，或用于你不确定当前 scope 的对象是否是目标对象的情形（例如，某个仅限单一国家的日志条目）。

### 运算符

##### 比较运算符

*Scope* 使用 = 或 != 进行比较。例如：

- `ruler != ig:ig_devout.leader`
- `infamy = 100`

数值可以用 <、<=、>、>=、= 和 != 进行比较。例如：

- `ruler.popularity > 50`
- `ig:ig_landowners.ig_clout <= 0.25`
- `c:RUS != this`
- `root.gdp > c:FRA.army_size`（这是个毫无意义的比较，但足以说明你可以比较*任意*两个数值
*!= 表示“不等于”，既可用于 scope 也可用于数值。*

##### 布尔运算符

PDXscript 支持以下布尔运算符：

`AND, OR, NOT, NOR, NAND`

它们在 trigger 块内用于评估游戏状态。例如：

```
# This will return true if the country has a treasury over 50000 or is not at war.
OR = {
  treasury > 50000
  is_at_war = no
}
```

- **AND** 仅当其中**所有**条件都为**真**时返回真。
- **OR** 只要其中**任意一个**条件为**真**就返回真。
- **NOT** 和 **NOR** 实际上是相同的。仅当其中**所有**条件都为**假**时返回真。
- **NAND** 只要其中**任意一个**条件为**假**就返回真。

trigger 块始终以 **AND** 作为隐式的基础运算符。

##### 断言运算符

?= 是安全断言运算符。它会先检查 `lvalue` 对象是否存在，然后再按照 `rvalue` 的指定进行比较或作用域切换以执行脚本。

例如，这段脚本：

`capital ?= state_region.s:STATE_HOME_COUNTIES`

在功能上与这段脚本完全相同：

```
exists = capital
capital = state_region.s:STATE_HOME_COUNTIES
```

这有助于避免因未设置/null 的 scope 而产生的错误，并使脚本更简洁。但是，如果你*需要*在出现 null scope 时打印错误信息，就应该使用 = 让错误照常打印出来。

### 文件特有的属性

PDXscript 的一个关键特性是针对每种文件类型的特定实现。`/common` 各子目录中的文件经常会呈现专属于该文件的**列表块（list block）**、**脚本数学块（script math block）**或其他 trigger 块。

例如，看看 `law_peasant_levies` 中出现的不同块：

```
# Excerpt from law_peasant_levies
law_peasant_levies = {
	...

	# Here you can see that the syntax within this block is identical that seen in the /static_modifiers directory
	modifier = {
		country_can_only_conscript_peasants_bool = yes
		unit_morale_loss_mult = 0.1
		unit_experience_gain_mult = -0.25
		state_conscription_rate_add = 0.04
		country_aristocrats_pol_str_mult = 0.25
		country_military_goods_cost_mult = -0.1
		state_building_barrack_max_level_add = 25
		state_building_conscription_center_max_level_add = 25
	}

	...

	# Further down in this file is the is_visible block, which is a trigger block
	is_visible = {
		NOT = {
			country_has_primary_culture = cu:japanese
		}
	}

	...

	# At the bottom of the definition is a script math block
	ai_enact_weight_modifier = { #Petitions
		value = 0

		if = {
			limit = { ai_has_enact_weight_modifier_journal_entries = yes }
			add = 750
		}
	}
}
```

再看另一个例子，这次是定义 `ig_armed_forces`，我们可以同时看到属性和列表块：

```
# excerpt from /common/interest_groups/00_armed_forces.txt
ig_armed_forces = {
	color = hsv{ 0.09 0.29 0.39 }					# This is a color property, using the hsv syntax
	texture = "gfx/interface/icons/ig_icons/armed_forces.dds"	# This is a texture property which points to a texture

	layer = "revolution_dynamic_armed_forces"
	index = 0

	ideologies = {							# This is a list block; all you have to do is add the ideologies you want for this IG
		ideology_jingoist
		ideology_loyalist
		ideology_patriotic
	}

	character_ideologies = {					# This is also a list block
		ideology_moderate
		ideology_authoritarian
	}

	enable = {							# This is a trigger block
		always = yes
	}

	
	traits = {							# List block
		ig_trait_patriotic_fervor
		ig_trait_veteran_consultation
		ig_trait_materiel_waste
	}
	
	...
}
```

## Triggers（触发条件）

参见 Triggers 以获取 trigger 的文档。
Trigger 用于通过读取游戏状态来构建条件语句，例如人物（Character）的意识形态、州（State）的所有权等等。

Trigger 只能在 *trigger 块*中使用。它们各自有预定的语法，通常由游戏引擎在当前 scope 下进行评估。有些 trigger 可以在任何 scope 中使用，而另一些则会相对于当前 scope 评估不同的对象。

*注意：*只有当其中所有 trigger 都为真时，trigger 块才返回真。这种行为可以通过布尔运算符修改。

Trigger 有两种基本类型：*内联（inline）*和*块（block）*：

**内联 trigger** 接受一个简单的目标，例如 scope、script value 或 defined type：

```
# root = country
capital.state_region = s:STATE_MONTENEGRO

# root = character
interest_group.leader.ideology = ideology:ideology_moderate
```

**块 trigger** 更复杂，通常接受多个目标，例如一个 scope 和一个 script value。

```
# root = country
radical_fraction = {
    culture = cu:han
    value >= 0.10
}

calc_true_if = {
	 amount >= 2
	 has_law_or_variant = law_type:law_autocracy
	 has_law_or_variant = law_type:law_oligarchy
	 has_law_or_variant = law_type:law_landed_voting
	 has_law = law_type:law_monarchy
	 has_law_or_variant = law_type:law_theocracy
}
```

**提前退出（Early Out / Return Early）：**

除非是在 tooltip 中调用，trigger 块通常遵循“提前退出”原则。

如前所述，只有当其中所有 trigger 都为真时，trigger 块才返回真。“提前退出”意味着一旦块中的某个 trigger 评估为假，该块中后续的 trigger 就不再被评估。这一特性对于避免错误和编写高性能脚本至关重要。

```
# For example, this script will print errors should FRA not exist:
c:FRA.country_rank >= rank_value:great_power

# This can be avoided by two methods; the first is using the exists trigger:
exists = c:FRA # If FRA does not exist, the trigger fails here, and will not advance to the second trigger
c:FRA.country_rank >= rank_value:great_power

# The second method uses safe assertion:
c:FRA ?= { # If FRA does not exist, the trigger will fail before evaluating anything within the block
    country_rank >= rank_value:great_power
}
```

## Effects（效果）

参见 Effects 以获取 effect 的文档。
Effect 会改变当前的游戏状态，例如创建或杀死人物（Character）、改变州的所有权等等。

Effect 只能在 *effect 块*中使用。它们有预定的语法，通常由游戏引擎在当前 scope 下执行。有些 effect 可以在任何 scope 中使用，而另一些只有在正确的 scope 类型中使用才能生效。注意，有些 effect 会改变当前 scope，或者会相对于调用它们的 scope 来执行其效果。

Effect 按照 effect 块从开头到结尾的顺序依次执行。Effect 始终是语句中的 lvalue，并且只能使用 `=` 运算符。

**布尔形式：**

布尔 effect 使用 `yes`——有时是 `no`——作为 rvalue。这类 effect 通常不需要任何参数，不过有些 effect 具有可选参数，可以通过使用块来调用。

例如，这个 effect 会流放一名利益集团（Interest group）领袖：

```
# root = country
ig:ig_landowners = {
    leader = {
        exile_character = yes
    }
}
```

布尔 effect 通常作用于执行该 effect 的 scope。**简单形式：**

这种风格的 effect 需要一个作为 rvalue 传入的单一参数。这些参数可以是诸如：

| scope | `set_character_as_ruler = scope:foo` | `set_state_owner = c:FRA` |
|---|---|---|
| database key | `add_character_role = agitator` | `set_capital = STATE_EASTERN_THRACE` |
| value | `add_treasury = 5000` | `change_infamy = var:infamy_amount` |

简单 effect 可能作用于执行它的 scope 或 rvalue，具体取决于 effect 本身。

**复杂形式**

这种风格的 effect 在脚本块中使用多个参数。有些 effect 即使只有一个参数也只接受这种形式。

```
# root = country
capital = {
    add_radicals_in_state = {
        culture = cu:french
        value = medium_radicals # this is a base game script value; equals 0.05
    }
}

# Kill Character has an optional "hidden" parameter
# For example, this will post a notification that the character has died
ruler = {
    kill_character = yes
}

# Adding the "hidden" parameter will silently kill the character
ruler = {
    kill_character = {
        hidden = yes
    }
}
```

某些复杂 effect 带有一个可选的 effect 块，并隐式包含 scope 切换。

## 迭代器

**迭代器（Iterator）**用于遍历一列对象并对它们执行操作，而无需逐一写出每个对象。例如一个国家中的所有人物、一个州区域中的所有州，或一个政党（Political party）中的所有利益集团。

#### Trigger 迭代器

参见 Trigger iterators 以获取文档。
Trigger 迭代器的形式为 `any_x`，其完整名称表明了它迭代的对象类型。与 trigger 一样，trigger 迭代器通常需要特定的 scope 才能运作。

```
# This trigger iterates all of the characters in a country
any_scope_character = {
    has_ideology = ideology:ideology_moderate
}

# This trigger iterates all countries globally
any_country = {
    is_in_geographic_region = geographic_region_europe
    country_has_primary_culture = cu:turkish
}
```

默认情况下，只要**任意一个**对象满足所包含的条件，trigger 迭代器就返回真。这可以通过使用 `count` 或 `percent` 参数来改变。使用这些参数时，可以通过 `filter` trigger 块来限制对象列表，该块中的 trigger 仅用于确定哪些对象会被针对主 trigger 进行测试。

#### Effect 迭代器

参见 Effect iterators 以获取文档。
Effect 迭代器有三种形式：

- `random_x` - 从列表中随机选取一个对象，并且可以选择操纵各对象的权重
- `every_x` - 按顺序遍历列表中的所有对象
- `ordered_x` - 按提供的数值对列表排序；然后可以遍历其中部分或全部对象，或按位置选取特定对象

Effect 迭代器还可以接受一个可选的 `limit` trigger 块，用于将列表中的某些对象排除在考虑之外。

```
# This effect iterates all countries, but only those with enough money
every_country = {
    limit = {
        gold_reserves > 100000
    }
    add_modifier = modifier_has_money
}
```

## 控制流

参见 Flow effects 以获取控制流 effect 的文档。
PDXscript 以条件语句、`switch` 语句和 `while` 语句的形式提供控制流。

### 条件 Effect 语句

#### if 语句

这些语句使用一个 **limit** trigger 块来控制所包含的 effect 是否被执行。例如：

```
if = { # Only exile unpopular characters
  limit = {
    popularity < 0
  }
  exile_character = yes
}
```

#### else_if / else 语句

如果 trigger 块返回假，则不会执行该 effect。多个条件语句可以通过 **else_if** 和 **else** 块串联在一起。只有当紧邻其前的 **if** 或 **else_if** 的 limit 返回假时，它们才会被评估。这可以用来为脚本执行创建分支。当分支中的所有脚本执行完毕后，脚本会“返回”到分支起点继续执行。例如：

```
ruler = {
  # If this limit block is true, kill_character will be executed
  if = {
    limit = {
      culture != root.culture
    }
    kill_character = yes
  }
  # If the preceding limit block was false, exile_character will be executed
  else = {
    exile_character = yes
  }
}
# Regardless of the outcome of the conditionals above, your script will continue execution here
set_variable = yeeted_ruler
```

#### 嵌套条件语句

这些语句还可以相互嵌套，以实现更复杂的分支。例如：

```
if = {
  limit = {
     # If this is true, the nested statements will be evaluated
    is_at_war = yes
  }
  if = {
    limit = {
       radical_fraction < 0.25
    }
    trigger_event = my_event.1
  }
  else = {
    trigger_event = my_event.2
  }
}
else = {
  trigger_event = my_event.3
}
```

### 条件 Trigger 语句
触发器还可以使用带 `trigger_` 前缀变体的条件语句。这些语句遵循与 effect 语句相同的逻辑，但用于选择性地激活触发器。例如：

```
AND = {
  gdp >= 5000000
  authority > 100
  # These statements will evaluate a different trigger based on the presence of the "declared_bankruptcy" modifier in scope
  trigger_if = {
    limit = {
      has_modifier = declared_bankruptcy
    }
    treasury > 0
  }
  trigger_else = {
    is_in_default = no
  }
}
```

### switch 语句

`switch` 语句允许根据某个触发器返回的值来改变 effect 的执行。

注意 `switch` 仅限于返回 scope 或值的触发器。这也可以包括直接使用变量、保存的 scope 或其他 event target。

```
# This evaluates the value of a variable "foo"
switch = {
  trigger = var:foo
  0 = { <effects> } # Executes if var:foo = 0
  1 = { <effects> } # Executes if var:foo = 1
  2 = { <effects> } # Executes if var:foo = 2
  fallback = { <effects> } # Executes if var:foo meets none of the prior criteria, optional
}
```

### while 语句

`while` 循环允许在某些条件为真时或在给定迭代次数内重复执行 effect。

如果与 `limit` 一起使用，只要 `limit` 中的触发器保持为真，其中的 effect 就会不断重复。例如：

```
while = {
  limit = { 
    treasury < 0 
  }
  add_treasury = 5000
}
```

如果使用 `count` 参数，则其行为类似于 **for 循环**，其中的 effect 会重复执行指定的次数。例如：

```
while = {
  count = 100
  add_treasury = 5000
}
```

*警告：使用 while 时，必须注意不要让游戏陷入无限循环。这通常会导致游戏崩溃，但也可能使应用程序或你的机器挂起。*

## 数据管理

PDXscript 提供了多种访问、保存和操作数据的方法。

### 变量

关于变量的更多信息，请参阅 Variable（变量）页面。
**变量**是基于脚本的 event target，可以保存值或 scope。变量在赋值之前无需定义或声明。

变量有三种类型：“常规”变量、局部变量和全局变量。

- “常规”变量保存到游戏对象中，并在 effect 链之外持续存在。在该对象的 scope 中使用 `var:` event target 访问。

- 局部变量与 scope 无关，并在 effect 链结束时被清除。在 effect 链结束之前的*任何 scope* 中都可以使用 `local_var:` event target 访问。
- 全局变量保存到全局状态中，并在 effect 链之外持续存在。在任何 scope 中都可以使用 `global_var:` event target 访问。

变量通过 effect 设置和移除。例如：

```
# This sets a variable in the current scope that is named "foo" and has a value of "1"
set_variable = {
  name = foo
  value = 1
}

# This removes a variable in the current scope with the name "foo"
remove_variable = foo
```

触发器和 effect 可以把变量作为目标来使用，以替代脚本对象或值。例如：

```
# This statement evaluates the value of the variable "foo"
if = {
  limit = {
    var:foo = 10
  }
  activate_law = law_type:law_autocracy
}

# This effect uses the value of the local variable "foo" as a multiplier value
add_modifier = {
  name = modifier_awesome_government
  multiplier = local_var:foo
}
```

### 保存的 scope

关于 scope 的更多信息，请参阅 Scope（作用域）页面。
保存的 scope 与变量类似，区别在于它只在**effect 链**（文档中称为 event chain）的持续期间存在。将对象保存到 scope 中，可以让你在脚本的下游继续访问该 scope。

Scope 通过 `save_scope_as` effect 保存，并使用 `scope:` event target 访问。例如：

```
# This effect saves a country with poor relations and then triggers a diplomatic incident with them.
random_country = {
  limit = {
    relations:root < relations_threshold:neutral
  }
  save_scope_as = unfriendly_country
}
create_diplomatic_incident = {
  target = scope:unfriendly_country
  value = 10
}
```

保存的 scope 会**被转发到由脚本调用的事件和 effect 中**。保存的 scope 会一直保留到 effect 链结束，届时被丢弃。如果 effect 链由某个 on_action 启动，游戏引擎有时会转发与该 on_action 相关的 scope，例如 `scope:target` 或 `scope:recipient`。

只有调用 effect 时已经存在的 scope 才会被转发。例如：

```
ruler = {
  save_scope_as = ruler_scope # this scope will be forwarded to ruler_event.1
}
trigger_event = ruler_event.1
capital = {
  save_scope_as = capital_scope # this scope was saved after the trigger_event effect, and thus will not be forwarded to ruler_event.1
}
```

保存的 scope 也可以缓存到变量中，以便在其初始 effect 链之外访问。例如：

```
# This saves the country scope FRA to a variable
c:FRA = {
  save_scope_as = france_scope
}
set_variable = {
  name = foo
  value = scope:france_scope
}

# In another script; since we saved the FRA scope to this variable, this the same as scoping via c:FRA
var:foo = {
  add_treasury = 5000
}
```

### 变量列表

关于使用变量列表的更多信息，请参阅 Variable Lists（变量列表）。
变量列表用于将对象存储在列表中以便日后引用。列表可以被迭代和排序，但仅凭脚本无法直接对列表中的对象进行 scope 操作。

### 变量映射

关于使用变量映射的详细指南，请参阅 Variable Maps（变量映射）。
变量映射是键值对的列表，实际上起到数组的作用。它们同样可以被迭代和排序。

### 脚本数学

关于使用脚本数学的详细指南，请参阅 Script value（脚本值）。
PDXscript 包含一个强大的数学系统，包括各种算术运算，并支持条件运算。

**注意**：脚本值（script value）每次被使用时都会重新计算。在可能被频繁调用的场合，例如 localization 或 GUI 中，最佳实践是将该值“缓存”到变量中。这个变量可以用于与其他脚本的比较，只在需要时更新该变量。例如：

```
# initial effect that saved a script value to a variable
set_variable = {
	name = foo
	value = script_value_bar
}

# trigger elsewhere that checks the value of the variable
c:GBR.var:foo = script_value_boom

# this is more efficient than comparing the script value directly
c:GBR.script_value_var = script_value_boom
```

## 宏

主条目：Macro
**宏**是可以重复使用的脚本块。宏有两种主要类型：**scripted effect**（脚本化 effect）和 **scripted trigger**（脚本化触发器）。游戏会像对待直接在使用处定义的脚本一样来解析宏。

Scripted effect 和 trigger 分别定义在各自的文件夹中：`/common/scripted_effects/` 和 `/common/scripted_triggers/`。它们在脚本中通过其数据库键名调用。

### Scripted trigger

```
# This is the definition in /common/scripted_triggers. It can be invoked using its key, "is_broke_trigger"
is_broke_trigger = {
	OR = {
		in_default = yes
		AND = {
			has_modifier = declared_bankruptcy
			gold_reserves < 0
		}
	}
}

# This is how it would appear in a trigger block:
if = {
    limit = {
        is_broke_trigger = yes
    }
    add_treasury = 100
}
```

### Scripted effect

```
# The base game defines this scripted effect:
the_balkan_league_activated_modifier_cleanser = {
	hidden_effect = {
		remove_modifier = balkan_wars_military_tech_boost_mod
		remove_modifier = balkan_wars_military_industry_overworked_mod
	}
}

# Which is called in the on_complete block of je_the_balkan_league
je_the_balkan_league = {
    <...>
    
    on_complete = {
        <...>
        the_balkan_league_activated_modifier_cleanser = yes
    }
}
```

### 参数与替换

Scripted trigger 和 effect 还可以定义*参数*，在宏被使用时进行替换。

参数使用 `$$` 标记，例如：

```
# This trigger has two parameters "type" and "peril"
my_cool_trigger = {
	has_variable = $type$_expedition_peril_var
	var:$type$_expedition_peril_var >= $value$
}

# This can be invoked with its parameters like so:
my_cool_trigger = {
    type = antarctic
    value = 3
}

# Which the engine compiles into this script:
has_variable = antarctic_expedition_peril_var
var:antarctic_expedition_peril_var >= 3
```

参数是字面上的文本替换，因此不能用来传递保存的值，例如变量或保存的 scope 的值。

## 参考资料

论坛帖子：

- [Grand Jomini Modding Information Manuscript](https://forum.paradoxplaza.com/forum/index.php?threads/1170261)
- [Victoria 3 - Dev Diary #60 - Modding](https://forum.paradoxplaza.com/forum/index.php?threads/1545200)
- [Victoria 3 - Dev Diary #164 - Marvelous Modding Monday](https://forum.paradoxplaza.com/forum/index.php?threads/1868975)

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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