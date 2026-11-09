---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Script value
source: https://vic3.paradoxwikis.com/Script_value
pageid: 5679
categories: [Potentially_outdated, 1.10, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。至少部分内容最后核实于 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10。

参见：
Macro
**Script value（脚本值）** 是一种数学计算，允许在游戏过程中基于游戏数值创建动态的值。

Script value 可以用于大多数接受数值的脚本中，即 [effects](Effect.md)、[triggers](Trigger.md) 和 [variables](Variable.md)，也可用于许多 AI 行为计算。

Script value 每次被使用时都会重新计算。这通常是有用的；但在该值可能被频繁调用的情况下——例如在 localization（本地化文本）或 GUI 中——通常更好的做法是将其保存为一个变量并显示或使用该变量，仅在需要时更新变量。

Script value 可以直接在 effect 或 trigger 中定义，也可以定义为一个便于复用的具名 script value。

## 具名值与内联值

具名值定义于 common/script_values/ 目录下的 .txt 文件中。内联值则直接在其使用处（某个 effect、trigger 或其他用途）定义。在大多数情况下，具名值和内联值可以互换使用。

Script value 不能使用超过 5 位小数。如果计算中需要更高的精度，可以先乘以 10 的若干次幂。可能的最大值（最正）为 92233720368547.75807，可能的最小值（最负）为 -92233720368547.75808；超出这些值可能导致上溢/下溢。[1]

注意避免值的循环依赖。一个值绝不应直接依赖于它自身。

### 静态值

最简单的 script value 就是一个字面值。这对于确保一个公共值在所有用途中保持一致最为有用。静态 script value 就是脚本名后跟一个字面数值，例如 `construction_cost_medium = 400`。

## 公式与运算符

大多数 script value 是由一个或多个运算符组成的公式。以下是可用于 script value 的运算符[2]。大多数运算符按给定术语的常规数学含义运作。运算符按线性顺序求值，从左到右、从上到下；不存在诸如 PEMDAS/BEDMAS 的运算优先级。大多数运算符的右侧可以是任何数值：字面数字、返回数值的 [event target](Event target.md)，甚至另一个 script value。这样可以构建更复杂的公式，而 event target 则允许使用动态的游戏数值。

| 运算符 | 描述 |
|---|---|
| value | 将 script value 设为此值（覆盖任何先前的值） |
| add | 将此值加到 script value 上 |
| subtract | 从 script value 中减去此值 |
| multiply | 将 script value 乘以此值 |
| divide | 将 script value 除以此值 |
| modulo | 取 script value 除以此值后的余数 |
| max | 若 script value 更大（更正），则将 script value 设为此值 |
| min | 若 script value 更小（更负），则将 script value 设为此值 |
| round | 将 script value 四舍五入为整数；右侧为布尔值 |
| ceiling | 将 script value 向上（更正方向）取整为整数；右侧为布尔值 |
| floor | 将 script value 向下（更负方向）取整为整数；右侧为布尔值 |
| round_to | 将 script value 四舍五入到此值的最近倍数 |
| fixed_range | 将 script value 设为所包含的 min 与 max 设定范围内的随机定点值；右侧为一个数据块 |
| integer_range | 将 script value 设为所包含的 min 与 max 设定范围内的随机整数值；右侧为一个数据块 |
| pow | 将值提升到指定的指数；接受小数和负数；在大多数情况下不返回精确值 |

公式还可以使用 `if`、`else_if` 和 `else` 的条件值，其运作方式与常规脚本中相同。

### 示例

一个基础公式只是使用若干运算符来计算最终值。

```
example_value = {
  #values start at null/0
  add = 5         #value is 5
  multiply = 4    #value is 20
  max = 10        #value is 10
  subtract = 3    #value is 7
  value = 13      #value is 13
}
```

也可以为运算符的值使用内联公式；这等同于定义一个单独的具名值并将其用作该运算符的值。

```
first_example = {
  add = 6         #value is 6
  multiply = {
    value = 3
    divide = 2
  }               #same as multiply by 1.5, value is now 9
  max = 10        #value is 9
  subtract = 3    #value is 6
}

second_example = {
  add = 6                 #value is 6
  multiply = sub_value    #value is now 9
  max = 10                #value is 9
  subtract = 3            #value is 6
}
sub_value = {
  value = 3
  divide = 2
}
```

返回数值的 [Event targets](Event target.md) 也可以用作运算符的值。请注意，许多 [triggers](Trigger.md) 只要用于比较数值，就可以用作 event target。

```
half_expenses = {
  value = expenses    #sets value to current weekly government expenses
  divide = 2          #divides it by two
}
```

## Script value 与 scope

Script value 通常在其被调用的 [scope](Scope.md) 中计算。在使用 [event targets](Event target.md)、条件值和迭代器时这一点尤为重要，因为其中大多数都依赖于特定的 scope。例如，effect `c:GBR = { add_treasury = half_expenses }` 在 GBR 的 scope 中计算其值，而 `c:FRA = { add_treasury = half_expenses }` 则在法国的 scope 中计算。取决于游戏状态和 `half_expenses` 的公式，两者可能得出截然不同的值。

有两种方法可以为 script value 设定特定的 scope：

1. 调用 script value 时，可以用 event target 对其进行点式 scope 定位。例如，`c:FRA = { add_treasury = c:GBR.half_expenses }` 与 `c:GBR = { add_treasury = half_expenses }` 得到相同的值，因为 `half_expenses` 两次都是在 GBR 的 scope 中计算的。
2. 定义公式时，公式中的值可以用 event target 或迭代器进行 scope 定位。由于 `half_expenses` 使用了 event target `expenses`，使用 `c:GBR.expenses` 将始终使用 GBR scope 中的值，无论 `half_expenses` 在何处被调用。

这些方法也可以混合使用，使某些值始终引用固定的 scope，而另一些值引用当前 scope。

## 条件

使用 `if`、`else_if` 和 `else` 条件可以使公式根据游戏状态以受控的方式变化。例如，以下公式会根据已研究的技术得出不同的值：

```
tech_scaled_income = {
  value = income    #sets value to current weekly government income
  if = {
    limit = { has_technology_researched = currency_standards }
    multiply = 1.05 #increase by 5%
  }
  if = {
    limit = { has_technology_researched = banking }
    multiply = 1.05 #increase by another 5%
  }
  if = {
    limit = { has_technology_researched = central_banking }
    multiply = 1.1  #increase by another 10%
  }
}
```

注意这些效果是累乘的，也可以定义互斥的条件。在本例中，只考虑最先进的技术。

```
tech_scaled_income = {
  value = income     #sets value to current weekly government income
  if = {
    limit = { has_technology_researched = central_banking }
    multiply = 1.1   #increase by 10%
  }
  else_if = {
    limit = { has_technology_researched = banking }
    multiply = 1.075 #increase by 7.5%
  }
  else_if = {
    limit = { has_technology_researched = currency_standards }
    multiply = 1.05  #increase by 5%
  }
}
```

## 迭代器

[Iterators](https://vic3.paradoxwikis.com/Iterators)（迭代器）或列表可以在公式内使用，以多次运行同一组运算符。注意迭代器通常会改变 scope，因此 event target 可能需要进行 scope 定位才能获取所需的值。迭代器的一个常见用途是对某个对象集合（如拥有的州）求总和。

本例通过累加每个拥有州的基础设施，得出一国的基础设施总量：

```
total_infrastructure = {
  every_scope_state = {
    add = infrastructure
  }
}
```

还可以使用条件和迭代器参数来缩小所用对象的范围。以下公式仅累加已整合州的设施。

```
total_incorporated_infrastructure = {
  every_scope_state = {
    limit = { is_incorporated = yes }
    add = infrastructure
  }
}
```

迭代器也可以在正确的 scope 定位下嵌套使用，例如：

```
number_of_steel_mills_of_allies = {
    every_scope_ally = {
        every_scope_building = {
            limit = { is_building_type = building_steel_mills }
            add = level
        }
    }
}
```

该公式遍历该国的每一个盟友，然后遍历*他们各自*的建筑，并将其中钢厂的等级相加。简而言之，它返回该国所有盟友的钢厂等级总数。

虽然 `every_` 迭代器通常对公式最为有用，但 `ordered_` 和 `random_` 也有各自的用途。

注意运算符应放在迭代器数据块的内部还是外部。例如，要得到拥有州的平均基础设施，除法需要放在州 scope 之外。

```
average_infrastructure = {
  every_scope_state = {
    add = infrastructure
  }
  divide = num_states
}
```

如果除法发生在州 scope 内部并使用有效值，则会对每个值分别执行除法，而不是对总和值执行。

## 本地化

主条目：
Localization
Script value 可以通过 function `ScriptValue('named_script_value')` 在 localization 中显示。关于如何使用和格式化 function，请参阅本地化页面。

在某些用途中，可以为运算符使用 `desc = loc_key` 给出描述。该运算符必须使用数据块形式才能这样做。描述随后会与当前值一同在游戏中显示。这常用于日志条目的脚本化进度条以及外交接受度。

当 `desc` 可用时，值本身可以通过 `format = loc_key` 获得自定义格式。格式本地化使用两个特殊术语，但除此之外可以像任何本地化文本一样格式化。特殊术语是 `$VALUE$`（即值本身）和 `$KEY$`（即 `desc` 的键）。它们可以按任意顺序排列，也可以添加其他文本。最后，`$VALUE$` 可以使用 [Function formatting](Localization.md)，例如 `$VALUE|=$`。

## 临时值

可以使用 `save_temporary_value_as` 保存临时值。这可用于保存在同一脚本内会被频繁使用的值。

已保存的临时值可以通过 event target `scope:` 获取。

```
coal_synergy = {
    every_scope_building = {
        limit = { is_building_type = building_steel_mills }
        add = level
    }
    save_temporary_value_as = number_of_steel_mills

    # "Reset" the value
    value = 0

    every_scope_building = {
        limit = { is_building_type = building_coal_mine }
        add = level
    }
    save_temporary_value_as = number_of_coal_mines

    value = 0

    if = {
        limit = {
            scope:number_of_coal_mines > scope:number_of_steel_mills
        }
        value = scope:number_of_coal_mines
        multiply = scope:number_of_steel_mills
    }
    else = {
        value = scope:number_of_coal_mines
        add = scope:number_of_steel_mills
    }
}
```

在此示例代码中，如果你的煤矿多于钢厂，则该值等于煤矿数 × 钢厂数；否则，该值等于煤矿数 + 钢厂数。

## 示例 script value 列表

主条目：
List of example script values
本页面收录了可能有用或有趣、可供使用或学习的 script value 示例。欢迎添加你自己的示例。

## @ 值

请勿与
localization
中用于文本图标的
@ function 混淆
**@ 值**（或称 at 值）是 script value 的一个功能更受限的版本。@ 值只能在同一文件内使用，且只能定义为纯数学公式或字面字符串，不能引用游戏状态。因此 @ 值始终是常量。@ 值可用于大多数文件中——包括 script value——并广泛用于 gui 和图形相关文件。它们的主要目的是标准化以及便于统一修改相关的值。

@ 值可以定义为简单的数字、数学公式、字面字符串或另一个 @ 值，之后每当该 @ 值被使用时，文件会在原位替换为其值。

@ 值定义示例：

```
@pi = 3.1416
@third = @[1/3]
@sub_YUC_hoist_scale = @[third*2]
@canton_scale_cross_x = @[ ( 333 / 768 ) + 0.001 ]
@birthrate_at_growth_max = @[(pop_growth_max_sol-pop_growth_transition_sol)*((min_birthrate-birthrate_at_transition)/(pop_growth_stable_sol-pop_growth_transition_sol))+birthrate_at_transition]
@this_is_you = "this_is_you.dds"
@default_window_file = "gui/notifications/jomini_message.gui"
@default_window_name = "jomini_message"
@tex_star_position = @sixth
```

@ 公式总是包裹在 `@[ ]` 中，公式内使用的任何 @ 值都不带其 @。@ 公式可以使用加法 `+`、减法 `-`、乘法 `*` 和除法 `/`。这些公式**确实**遵循 PEMDAS/BEDMAS 运算优先级，并可以使用括号将应在乘除之前执行的加减法分组。公式元素之间可以自由选择是否使用空格分隔。也可以用 `-` 进行一元取负：`@[-1]` 等于 `@[0 - 1]`，`@[-1/2]` 等于 `@[1/-2]`。

@ 公式也可以直接代替已定义的 @ 值使用；例如，使用上述定义，`width = @[1/3]` 与 `width = @third` 得到相同的结果。

在公式之外使用 @ 值时，必须带 @ 调用；例如 `max_width = @texture_importer_output_text_width`。在其他所有方面，它可以在任何可以使用字面数字或字符串的地方使用。

## 参考文献

1. ↑ Script value 为 64 位，含 5 位小数
2. ↑ 改编自 /Victoria 3/game/common/script_values/script_values.md

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • Script value • [Variables](Variable.md) |
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
| 音频 | 音乐 • [声音](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [模组](Mod.md) • [模组兼容性](Mod compatibility.md) • [模组结构](Mod structure.md) • [脚本化测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [模组翻译](Mod translation.md) • [新国家模组制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州模组制作指南](State modding guide.md) |
|---|---|