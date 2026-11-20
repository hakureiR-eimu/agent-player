---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Variable
source: https://vic3.paradoxwikis.com/Variable
pageid: 7819
categories: [1.13, Modding]
fetched: 2026-10-27
---
本文已针对游戏当前 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

**变量（Variables）** 是内容制作者捕获、访问和操作信息的主要方法。

这些是脚本化的 [event targets](Event target.md)，可以保存值或 scope。许多 [effect](Effect.md) 和 [trigger](Trigger.md) 可以使用变量作为目标，以代替直接脚本化的对象或值。变量也可以用作 [scope](Scope.md)。

本文还会涵盖相关的**列表（List）**、**变量列表（Variable List）**和**变量映射（Variable Map）**系统。

## 脚本变量

### 概述

变量有三种类型："常规"、全局和局部。

| 变量类型 | 有作用域 | 持久化 | Event target |
|---|---|---|---|
| "常规" | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | var: |
| 全局 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | global_var: |
| 局部 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | local_var: |

- "常规"变量会保存到游戏对象上，并在 effect 链之外持久存在。在对象的 scope 中使用 `var:` event target 来访问它们。

- 局部变量与作用域无关，会在 effect 链结束时被垃圾回收。在 effect 链结束之前，可以在*任意 scope* 中使用 `local_var:` event target 来访问它们。
- 全局变量会保存到全局状态中，并在 effect 链之外持久存在。可以在任意 scope 中使用 `global_var:` event target 来访问它们。

*注意：局部变量会在 effect 链结束时自动移除；常规变量和全局变量会一直存在，直到被 effect 显式移除。*

### 脚本变量的用法

**设置和使用变量**

变量通过 effect 来设置、操作和移除。例如：

```
# This sets a variable in the current scope that is named "foo" and has a value of "1"
set_variable = {
  name = foo
  value = 1
}

# This removes a variable in the current scope with the name "foo"
remove_variable = foo
```

变量可以保存数值或布尔值、作为 scope 的游戏对象，或一个 localization 键。凡是可以使用 [scope](Scope.md) 或 [script value](Script value.md) 的脚本位置，一般都可以接受变量。已保存的 scope 可以缓存到变量中，以便在其初始 effect 链之外访问。例如：

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

#### 访问和操作数值变量

变量设置好之后，其值可以在许多 effect 和 trigger 中使用。例如：

```
if = {
  # This statement checks if the variable "foo" is set and checks its value
  limit = {
    has_variable = foo
    var:foo > 5
  }
  # This effect uses the value of "foo" for an operation in variable "bar"
  set_variable = {
    name = bar
    value = {
      add = var:foo
      multiply = 2
    }
  }
}
```

`change_variable` 和 `clamp_variable` effect 可用于直接操作变量。例如：

```
# This effect adds "5" to the variable "foo"
change_variable = {
  name = foo
  add = 5
}
# This effect "clamps" the variable into the specified range
clamp_variable = {
  name = foo
  max = 3
  min = 0
}
```

虽然用这些 effect 操作值很简单，但当变量被取消设置或丢失其值时，它们不提供任何保护。作为替代方案，通常更可靠的做法是使用 `set_variable` 并借助脚本数学来修改数值变量。例如：

```
 # This implementation has the advantage of restoring the variable "foo" should it become unset, and will restore it to a value-holding variable should its value become unset
set_variable = {
	name = foo        
	value = {
		if = {
			limit = { has_variable = foo }
			value = var:foo
		}
		add = 5
	}
}
```

这个 effect 会检查变量 foo 是否存在。如果它已经存在，新值会被设为当前值；如果它尚不存在，值会被设为 0。然后在该值上加 5。这意味着即使变量尚不存在也会被设置，并且将其当前值改变 5。如果这个 effect 会被大量使用，最好为它创建一个带 [参数](Macro.md) 的 scripted effect。下面是这种 scripted effect 的一个例子：

```
 prefix_change_variable_effect = {
	set_variable = {
		name = $NAME$
		value = {
			if = {
				limit = { has_variable = $NAME$ }
				value = var:$NAME$
			}
			add = $AMOUNT$
			$ADDITIONAL_SCRIPT_MATH$
		}
	}
}
```

这个 effect 与上面的 effect 作用相同，但更加通用，也便于复用。其用法示例可能如下所示：

```
 prefix_change_variable_effect = {
	NAME = foo
	AMOUNT = -3
	ADDITIONAL_SCRIPT_MATH = "min = 0 max = 100"
}
```

这种用法会将变量 `foo` 改变 `-3`，并额外将变量限制在最小 0、最大 100 的范围内。注意 `ADDITIONAL_SCRIPT_MATH` 还可以用于更多的脚本数学。

### 标志与变量

与 [localization](Localization.md) 键对应的 scope 可以使用 `flag:` event target 保存到变量中。这对于界面 mod 制作至关重要，因为它允许 mod 制作者动态更改 UI 中显示的文本。例如：

```
# This key in your localization:
l_english:
 foo: "bar"

# Can be saved to a variable like this:
set_variable = {
    name = test
    value = flag:foo
}
```

标志变量可以像其他游戏中的事件标志那样用于比较：

```
if = {
    limit = {
        var:foo = flag:test
    }
    <effects>
}
```

在 [GUIscript](GUI script.md) 中，function `GetFlagName` 会访问并显示与所保存键相关联的 localization 字符串。例如：

```
textbox = {
	parentanchor = top|hcenter
	autoresize = yes
	raw_text = "[Country.MakeScope.Var('test').GetFlagName]"
	align = center|nobaseline
	elide = right
	using = fontsize_large
}
```

在这个例子中，变量 `test` 会显示文本 `bar.`

*注意：标志变量并不包含整个 localization 字符串，它只包含 localization 键。需要使用 GetFlagName gui function 才能访问其相关联的键。*

### 脚本变量 Effect

另请参见：
Effect
| Effect | 描述 | 示例 | 作用域 | 目标 |
|---|---|---|---|---|
| add_to_global_variable_list | 将 event target 添加到全局变量列表中，持续指定时长 | add_to_global_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | 无 |  |
| add_to_global_variable_map | 将 event target 添加到全局变量映射中，持续指定时长；不能更新已有键的值 | add_to_global_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | 无 |  |
| add_to_local_variable_list | 将 event target 添加到局部变量列表中，持续指定时长 | add_to_local_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | 无 |  |
| add_to_local_variable_map | 将 event target 添加到局部变量映射中，持续指定时长；不能更新已有键的值 | add_to_local_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | 无 |  |
| add_to_variable_list | 将 event target 添加到变量列表中，持续指定时长 | add_to_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | 无 |  |
| add_to_variable_map | 将 event target 添加到变量映射中，持续指定时长；不能更新已有键的值 | add_to_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | 无 |  |
| change_global_variable | 修改数值型全局变量的值 | change_global_variable = { name = <global variable> <operation type> = <value> } 有效的运算有 add、subtract、multiply、divide、modulo、min 和 max | 无 |  |
| change_local_variable | 修改数值型局部变量的值 | change_local_variable = { name = <local variable> <operation type> = <value> } 有效的运算有 add、subtract、multiply、divide、modulo、min 和 max | 无 |  |
| change_variable | 修改数值型变量的值 | change_variable = { name = <variable name> <operation type> = <value> } 有效的运算有 add、subtract、multiply、divide、modulo、min 和 max | 无 |  |
| clamp_global_variable | 将全局变量限制在指定的最大值和最小值之间 | clamp_global_variable = { name = <global variable> max = <value> min = <value> } | 无 |  |
| clamp_local_variable | 将局部变量限制在指定的最大值和最小值之间 | clamp_local_variable = { name = <local variable> max = <value> min = <value> } | 无 |  |
| clamp_variable | 将变量限制在指定的最大值和最小值之间 | clamp_variable = { name = <variable name> max = <value> min = <value> } | 无 |  |
| clear_global_variable_list | 清空列表 | clear_global_variable_list = variable_name | 无 |  |
| clear_global_variable_map | 清空映射 | clear_global_variable_map = variable_name | 无 |  |
| clear_local_variable_list | 清空列表 | clear_local_variable_list = variable_name | 无 |  |
| clear_local_variable_map | 清空映射 | clear_local_variable_map = variable_name | 无 |  |
| clear_variable_list | 清空列表 | clear_variable_list = variable_name | 无 |  |
| clear_variable_map | 清空映射 | clear_variable_map = variable_name | 无 |  |
| every_in_global_list | 遍历全局列表中的所有项。 | every_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | 无 |  |
| every_in_list | 遍历列表中的所有项。 | every_in_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | 无 |  |
| every_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | every_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | 无 |  |
| every_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | every_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | 无 |  |
| every_key_in_variable_map | 遍历变量映射中的所有键。 | every_key_in_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | 无 |  |
| ordered_in_list | 遍历列表中的所有项。 | ordered_in_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | 无 |  |
| ordered_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | ordered_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | 无 |  |
| ordered_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | ordered_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | 无 |  |
| ordered_key_in_variable_map | 遍历变量映射中的所有键。 | ordered_key_in_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | 无 |  |
| random_in_list | 遍历列表中的所有项。 | random_in_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | 无 |  |
| random_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | random_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | 无 |  |
| random_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | random_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | 无 |  |
| random_key_in_variable_map | 遍历变量映射中的所有键。 | random_key_in_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | 无 |  |
| remove_from_global_variable_map | 从全局变量映射中移除目标 | remove_from_global_variable_map = { name = name of the map key = event target } | 无 |  |
| remove_from_list | 从命名列表中移除当前 scope | remove_from_list = <list_name> | 无 |  |
| remove_from_local_variable_map | 从局部变量映射中移除目标 | remove_from_variable_map = { name = name of the map key = event target } | 无 |  |
| remove_from_variable_map | 从变量映射中移除目标 | remove_from_variable_map = { name = name of the map key = event target } | 无 |  |
| remove_global_variable | 移除一个全局变量 | remove_global_variable = variable_name | 无 |  |
| remove_list_global_variable | 从全局变量列表中移除目标 | remove_list_global_variable = { name = <global variable> target = <event target> } | 无 |  |
| remove_list_local_variable | 从局部变量列表中移除目标 | remove_list_local_variable = { name = <local variable> target = <event target> } | 无 |  |
| remove_list_variable | 从变量列表中移除目标 | remove_list_variable = { name = <variable name> target = <event target> } | 无 |  |
| remove_variable | 移除一个变量 | remove_variable = variable_name | 无 |  |
| round_global_variable | 将全局变量四舍五入到最近的指定值 | round_global_variable = { name = <global variable> nearest = <script_value> } | 无 |  |
| round_local_variable | 将局部变量四舍五入到最近的指定值 | round_local_variable = { name = <local variable> nearest = <script_value> } | 无 |  |
| round_variable | 将变量四舍五入到最近的指定值 | round_variable = { name = <variable name> nearest = <script_value> } | 无 |  |
| set_global_variable | 设置一个全局变量 | set_global_variable = { name = <global variable> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } 该变量可通过 global_var:<variable name> 访问。也可以写成 set_global_variable = X（等价于 set_global_variable = { name = X value = yes }） | 无 |  |
| set_local_variable | 设置一个局部变量 | set_local_variable = { name = <local variable> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } 该变量可通过 local_var:<variable name> 访问，直到当前 effect 或事件链结束为止。也可以写成 set_local_variable = X（等价于 set_local_variable = { name = X value = yes }） | 无 |  |
| set_variable | 设置一个变量 | set_variable = { name = <variable name> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } 该变量可在其被设置的 scope 中通过 var:<variable name> 访问。也可以写成 set_variable = X（等价于 set_variable = { name = X value = yes }） | 无 |  |
| sort_global_variable_list | 对全局变量列表排序 | sort_global_variable_list = { name = <global variable> order = <math script> } | 无 |  |
| sort_local_variable_list | 对局部变量列表排序 | sort_local_variable_list = { name = <local variable> order = <math script> } | 无 |  |
| sort_variable_list | 对变量列表排序 | sort_variable_list = { name = <variable name> order = <math script> } | 无 |  |
### 脚本变量 Trigger

另请参见：
Trigger
| Trigger | 描述 | 示例 | Scopes | Targets |
|---|---|---|---|---|
| has_global_variable | 检查当前 scope 是否设置了指定的全局变量 | has_global_variable = name | none |  |
| has_local_variable | 检查当前 scope 是否设置了指定的局部变量 | has_local_variable = name | none |  |
| has_variable | 检查当前 scope 是否设置了指定的变量 | has_variable = name | none |  |

## 临时列表

**列表**是在 effect 执行期间构建的 [scopes](Scope.md) 临时集合。

### 概述

共有两种变体，遵循与 `save_scope_as` 和 `save_temporary_scope_as` 相同的模式：

- `add_to_list` —— 该列表在整个顶层 effect 执行期间持续存在（即跨越一个事件的 `immediate` 和 `option` 块）。
- `add_to_temporary_list` —— 该列表仅在当前块及其子块内持续存在。

### 列表用法

列表通过在 effect 执行期间添加 scope 来构建，并通过对其进行迭代来使用。

```
# Build a list of countries at war
every_country = {
	limit = { is_at_war = yes }
	add_to_list = countries_at_war
}

# Later, iterate the list
every_in_list = {
	list = countries_at_war
	<triggers>
	<effects>
}
```

### 列表 Effect

另请参见：
Effect
| Effect | 描述 | 示例 | Scopes | Targets |
|---|---|---|---|---|
| add_to_list | 将当前 scope 添加到任意命名的列表中（若列表尚不存在则创建），以便在之后（未中断）的事件链中引用 | scope = { add_to_list = <name_of_list> } add_to_list = { name = <name_of_list> value = <script_value> } 注意，若将永久目标添加到临时列表，整个列表将变为永久 | none |  |
| add_to_temporary_list | 将当前 scope 添加到任意命名的列表中（若列表尚不存在则创建），以便在同一 effect 中稍后引用 | add_to_temporary_list = <name_of_list> add_to_temporary_list = { name = <name_of_list> value = <script_value> } 注意，若将临时目标添加到永久列表，该列表仍保持永久 | none |  |
| every_in_list | 遍历列表中的所有项目。 | every_in_list = { list = name or variable = name limit = { <triggers> }（可选） <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| ordered_in_list | 遍历列表中的所有项目。 | ordered_in_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| random_in_list | 遍历列表中的所有项目。 | random_in_list = { list = name or variable = name limit = { <triggers> }（可选） weight = { mtth }（可选） <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| remove_from_list | 将当前 scope 从指定名称的列表中移除 | remove_from_list = <list_name> | none |  |

### 列表 Trigger

另请参见：
Trigger
| Trigger | 描述 | 示例 | Scopes | Targets |
|---|---|---|---|---|
| add_to_temporary_list | 保存一个临时目标，供 trigger 执行期间使用 | 用于在 trigger 中构建列表。若在 any-trigger 中使用，其放置位置非常重要。游戏会迭代 any-trigger 的每个实例，直到找到满足条件的单个实例，然后停止。为了添加满足特定条件的 scope 的所有实例，请使用 "count = all"，同时将这个 "effect" 放在 any-trigger 的最末尾，以便对每次迭代都评估所有条件。 | none |  |
| any_in_list | 遍历列表中的所有项目。 | any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| is_in_list | 检查某个目标是否在列表中 |  | none |  |
| list_size | 检查列表的大小 | list_size = { name = <list name> value >= <value> } | none | value |

## 变量列表

**变量列表**（也称为“列表”或 "varlists"）是以命名列表形式存储的、持久的、有序且[可迭代](https://vic3.paradoxwikis.com/Iterators)的 [scopes](Scope.md) 集合。与脚本变量一样，变量列表也分为三种类型：

- **“常规”变量列表**保存到游戏对象中，在 effect 链之外仍然持久存在。可在该对象的 scope 中使用 `x_in_variable_list` 迭代器来访问。

- **局部变量列表**与 scope 无关，在 effect 链结束时被垃圾回收。在 effect 链结束之前，可在*任意 scope* 中使用 `x_in_local_list` 迭代器来访问。
- **全局变量列表**保存到全局状态中，在 effect 链之外仍然持久存在。可在任意 scope 中使用 `x_in_global_list` 迭代器来访问。

### 概述

变量列表实际上是自定义的[迭代器](https://vic3.paradoxwikis.com/Iterator)列表，其元素由 effect 专门添加和移除。在其他所有方面，变量列表与任何其他迭代器相同。变量列表遵循与变量相同的三种类型模式：

| 类型 | 限定 scope | 持久 | Effect 前缀 | Trigger 前缀 |
|---|---|---|---|---|
| “常规” | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | `add_to_variable_list` | `is_target_in_variable_list` |
| global | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | `add_to_global_variable_list` | `is_target_in_global_variable_list` |
| local | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | `add_to_local_variable_list` | `is_target_in_local_variable_list` |

*注意：局部变量列表会在 effect 链结束时自动移除；常规列表和全局列表将持续存在，直到被 effect 显式移除。*

### 变量列表用法

使用 `add_to_variable_list` effect 将对象添加到变量列表中。如果该变量列表尚不存在，则会创建它。例如：

```
add_to_variable_list = {
	name = states_list
	target = c:FRA.capital
}
```

还可以使用相应的 trigger 检查游戏对象是否存在于给定列表中。例如：

```
is_target_in_variable_list = {
	name = states_list
	target = c:FRA.capital
}
```

一旦列表存在，就可以使用与临时列表相同的迭代 effect 和 trigger 对其中的项目进行迭代，但需使用 `variable` 参数而非 `list`。对于全局变量列表和局部变量列表，迭代器名称包含 scope 前缀。例如：

| 类型 | Effect 迭代器 | Trigger 迭代器 |
|---|---|---|
| “常规” | `every_in_list`、`random_in_list`、`ordered_in_list` | `any_in_list` |
| global | `every_in_global_list`、`random_in_global_list`、`ordered_in_global_list` | `any_in_global_list` |
| local | `every_in_local_list`、`random_in_local_list`、`ordered_in_local_list` | `any_in_local_list` |

```
# These first three are effect blocks, and function exactly like the every_x, random_x, and ordered_x iterators.
every_in_list = {
	variable = my_list
	<effects> # effects run on each item
}
random_in_global_list = {
	variable = my_list
	limit = { ... } # optional filter, i.e. limit = { is_alive = yes }
	<effects> # effects run on one random matching item
}
ordered_in_local_list = {
	variable = my_list
	position = 0 # Lists are zero-indexed
	<effects> # effects are run on the item at the specified position
}

# This is a trigger block, like the any_x iterators
any_in_global_list = {
	variable = my_list
	<triggers> # triggers are checked against each item, i.e. is_at_war = yes
}
```

### 变量列表 Effect

另请参见：
Effect
| Effect | 描述 | 示例 | Scopes | Targets |
|---|---|---|---|---|
| add_to_global_variable_list | 在给定时长内将 event target 添加到全局变量列表 | add_to_global_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| add_to_local_variable_list | 在给定时长内将 event target 添加到局部变量列表 | add_to_local_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| add_to_variable_list | 在给定时长内将 event target 添加到变量列表 | add_to_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| clear_global_variable_list | 清空该列表 | clear_global_variable_list = variable_name | none |  |
| clear_local_variable_list | 清空该列表 | clear_local_variable_list = variable_name | none |  |
| clear_variable_list | 清空该列表 | clear_variable_list = variable_name | none |  |
| every_in_global_list | 遍历全局列表中的所有项目。 | every_in_global_list = { list = name or variable = name limit = { <triggers> }（可选） <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| every_in_list | 遍历列表中的所有项目。 | every_in_list = { list = name or variable = name limit = { <triggers> }（可选） <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| every_in_local_list | 遍历局部列表中的所有项目。 | every_in_local_list = { list = name or variable = name limit = { <triggers> }（可选） <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| ordered_in_global_list | 遍历全局列表中的所有项目。list = name or variable = name | ordered_in_global_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| ordered_in_list | 遍历列表中的所有项目。 | ordered_in_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| ordered_in_local_list | 遍历局部列表中的所有项目。list = name or variable = name | ordered_in_local_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| random_in_global_list | 遍历全局列表中的所有项目。 | random_in_global_list = { list = name or variable = name limit = { <triggers> }（可选） weight = { mtth }（可选） <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| random_in_list | 遍历列表中的所有项目。 | random_in_list = { list = name or variable = name limit = { <triggers> }（可选） weight = { mtth }（可选） <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| random_in_local_list | 遍历局部列表中的所有项目。 | random_in_local_list = { list = name or variable = name limit = { <triggers> }（可选） weight = { mtth }（可选） <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| remove_list_global_variable | 将目标从全局变量列表中移除 | remove_list_global_variable = { name = <global variable> target = <event target> } | none |  |
| remove_list_local_variable | 将目标从局部变量列表中移除 | remove_list_local_variable = { name = <local variable> target = <event target> } | none |  |
| remove_list_variable | 将目标从变量列表中移除 | remove_list_variable = { name = <variable name> target = <event target> } | none |  |
| sort_global_variable_list | 对全局变量列表排序 | sort_global_variable_list = { name = <global variable> order = <math script> } | none |  |
| sort_local_variable_list | 对局部变量列表排序 | sort_local_variable_list = { name = <local variable> order = <math script> } | none |  |
| sort_variable_list | 对变量列表排序 | sort_variable_list = { name = <variable name> order = <math script> } | none |  |

### 变量列表 Trigger

另请参见：
Trigger
| Trigger | 描述 | 示例 | Scopes | Targets |
|---|---|---|---|---|
| add_to_temporary_list | 保存一个临时目标，供 trigger 执行期间使用 | 用于在 trigger 中构建列表。若在 any-trigger 中使用，其放置位置非常重要。游戏会迭代 any-trigger 的每个实例，直到找到满足条件的单个实例，然后停止。为了添加满足特定条件的 scope 的所有实例，请使用 "count = all"，同时将这个 "effect" 放在 any-trigger 的最末尾，以便对每次迭代都评估所有条件。 | none |  |
| any_in_global_list | 遍历全局列表中的所有项目。 | any_in_global_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| any_in_list | 遍历列表中的所有项目。 | any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| any_in_local_list | 遍历局部列表中的所有项目。 | any_in_local_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } 对由 add_to_(temporary)_list 创建的列表使用 "list"；对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| global_variable_list_size | 检查全局变量列表的大小 | global_variable_list_size = { name = <variable name> value >= <value> } | none |  |
| has_global_variable_list | 检查当前 scope 是否设置了指定的全局变量列表 | has_global_variable_list = name | none |  |
| has_local_variable_list | 检查当前 scope 是否设置了指定的局部变量列表 | has_local_variable_list = name | none |  |
| has_variable_list | 检查当前 scope 是否设置了指定的变量列表 | has_variable_list = name | none |  |
| is_target_in_global_variable_list | 检查某个目标是否在全局变量列表中 | is_target_in_global_variable_list = { name = <variable name> target = <event target> } | none |  |
| is_target_in_local_variable_list | 检查某个目标是否在局部变量列表中 | is_target_in_local_variable_list = { name = <variable name> target = <event target> } | none |  |
| is_target_in_variable_list | 检查某个目标是否在变量列表中 | is_target_in_variable_list = { name = <variable name> target = <event target> } | none |  |
| local_variable_list_size | 检查局部变量列表的大小 | local_variable_list_size = { name = <variable name> value >= <value> } | none |  |
| variable_list_size | 检查变量列表的大小 | variable_list_size = { name = <variable name> value >= <value> } | none |  |
### UI 中的变量列表

变量列表可以用作 UI 元素的 `datamodel`，列表中的对象会作为其子元素的 `datacontext` 传递。例如：

```
type my_fancy_flowcontainer = flowcontainer {
		direction = vertical
		parentanchor = top|hcenter
		ignoreinvisible = yes
		minimumsize = { 540 -1 }
		using = entry_bg_fancy
		spacing = 10
		margin_bottom = 20
		
		visible = "[Not(
			IsDataModelEmpty(
				Country.MakeScope.GetList('sassy_countries_list')
			)
		)]"
		datamodel = "[Country.MakeScope.GetList('sassy_countries_list')]"
		
		default_header_clean_faded = {
			parentanchor = hcenter
			blockoverride "text" {
				raw_text = "Sassy Countries"
			}
			blockoverride "size" {
				size = { 532 45 }
			}
		}
		
		item = {
			widget = {
				size = { 400 40 }
				tiny_flag = {}
			}
		}
	}
}
```

以下 UI function（函数）有助于在 GUI 中管理和使用变量映射：

| 函数 | 描述 | 类型 |
|---|---|---|
| Scope.GetList | 获取当前 scope（作用域）中保存到某个列表的对象。 | Function |
| GetGlobalList | 获取保存到全局列表的对象。 | Global Promote |
| IsDataModelEmpty | 检查所提供的 datamodel 中是否含有对象。如果所提供的变量列表不存在，则静默失败 | Global Function |
| DataModelHasItems | 检查所提供的 datamodel 中是否存在任何对象。 | Global Function |
| GetDataModelSize | 获取所提供的 datamodel 的大小 | Global Function |

## 变量映射

**变量映射**（Variable maps，也称为"maps"或"varmaps"）是关联数组，用于映射两个 [scope](Scope.md) 之间的关系，其中一个 scope（键）链接到另一个 scope（值）。这种关系也被称为"键值对"。

与脚本变量类似，变量映射有三种类型：

- **"常规"变量映射**保存到游戏对象上，在 effect 链之外仍然存在。在该对象的 scope 中使用 `variable_map` event target 访问。

- **局部变量映射**与 scope 无关，在 effect 链结束时被垃圾回收。在 effect 链结束之前，可以在*任何 scope* 中使用 `local_variable_map` event target 访问。
- **全局变量映射**保存到全局状态中，在 effect 链之外仍然存在。可以在任何 scope 中使用 `global_variable_map` event target 访问。

### 概述

变量映射遵循与变量和变量列表相同的三类型模式：

| 类型 | 限定 scope | 持久化 | effect 前缀 | scope 链接 |
|---|---|---|---|---|
| "regular" | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | `add_to_variable_map` | `"variable_map(name\|key)"` |
| global | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | `add_to_global_variable_map` | `"global_variable_map(name\|key)"` |
| local | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | `add_to_local_variable_map` | `"local_variable_map(name\|key)"` |

*注意：局部变量映射会在 effect 链结束时自动移除；常规和全局变量映射会一直存在，直到被 effect 显式移除。*

变量映射具有若干区别于其他数据结构的特性：

- **scope 替代：** 游戏中的某些 scope 不允许在其上存储变量。全局变量映射可以通过将该 scope 用作键、将关联数据存储为值来绕过这一限制。
- **规模化性能：** 按键访问值以及检查键是否存在都是相对较快的操作。随着数据结构变大，这些优势会愈发明显。对于需要处理大量 scope 的系统（例如大量国家、地点或人口），变量映射相比变量列表可能带来性能提升。
- **无序性：** 变量映射是无序的。无论插入顺序如何，遍历映射时产生的都是固定的内部顺序。仍然可以使用 `ordered_key_in_variable_map` 进行排序。
- **任意 scope 作为键或值：** 除游戏对象（国家、人物、地点等）之外，变量映射还可以将数值、布尔值以及游戏视为 scope 的其他表达式同时用作键和值。
- **可用作数组：** 由于整数可以用作映射的键，变量映射可以充当索引数组，其中键即位置。

### 变量列表的用法

使用 `add_to_variable_map` effect 向变量映射添加键值对。如果该变量映射尚不存在，则会创建它。例如：

```
add_to_variable_map = {
    name = rival_map # the map name, a string identifier. This is used to access the map in other script. 
    key = c:FRA # any scope (countries, locations, characters, etc.) or a number (1, 2, 3) 
    value = c:ENG # any scope or number — what the key is "paired" or "mapped" with
}
```

可以使用相应的 `variable_map` event target 及其键来访问变量映射中的值。例如：*注意：变量映射的 event target 必须用 " 包裹，因为它需要参数。参数即映射名称和键。*

```
"variable_map(rival_map|c:FRA)" = {
    add_prestige = -10 # Since the key "c:FRA" is paired to the scope "c:ENG" (the stored value), accessing the key c:FRA will scope to c:ENG
}
```

**添加已存在的键不会覆盖现有的键值对。** 如果键已存在，`add_to_variable_map` effect 会失败。要更新条目，必须先移除旧键，再用新的配对值重新添加：

```
# If you add a key-value pair earlier in script:
add_to_variable_map = { 
    name = rival_map 
    key = c:FRA
    value = c:ENG
}

# Running this effect will NOT update the key-value pair. The existing paired value is kept.
add_to_variable_map = { 
    name = rival_map 
    key = c:FRA
    value = c:SPA # This will fail and the value c:ENG will remain paired
}

# The correct script is to remove the key first, and then add the new key-value pair.
# Removing a key from a map also deletes any information about its paired value
remove_from_variable_map = {
    name = rival_map 
    key = c:FRA
}
add_to_variable_map = {
    name = rival_map
    key = c:FRA
    value = c:SPA # now correctly set to c:SPA
}
```

还可以在比较中使用此 event target：

```
if = {
    limit = {
        "variable_map(rival_map|c:FRA)" = c:ENG
    }
    "variable_map(rival_map|c:FRA)" = {
        change_relations = {
            country = root
            value = -10
        }
    }
}
else = {
    "variable_map(rival_map|c:FRA)" = {
        change_relations = {
            country = root
            value = -10
        }
    }
}
```

#### 在变量映射中使用参数

主条目：
宏
由于变量映射语句被包含在引号中，scripted effect 和 scripted trigger 的参数不会在其中被解析。要传递动态键，请先将参数保存到局部变量：

```
# Does NOT work — $key$ is not resolved inside quotes
"global_variable_map(my_map|$key$)" = { ... }

# Workaround: save the argument to a local variable
set_local_variable = {
	name = temp_key
	value = $key$            # resolved outside quotes, saved as local_var:temp_key
}
"global_variable_map(my_map|local_var:temp_key)" = { ... }
```

此变通方法仅适用于键（第二个参数）。映射名称（第一个参数）是标识符而非 scope，因此无法通过变量或参数进行参数化：

```
# Neither of these work
"global_variable_map($my_map$|c:ENG)" = { ... }
"global_variable_map(local_var:map_name|c:ENG)" = { ... }
```

### UI 中的变量映射

在 GUI 文件中可以使用以下数据函数访问变量映射：

| 函数 | 描述 |
|---|---|
| `Scope.GetMapKeys('<name>')` | 返回存储在某个 scope 上的映射中所有键的 datamodel。 |
| `GetGlobalMapKeys('<name>')` | 返回全局映射中所有键的 datamodel。 |
| `Scope.GetVariableFromVariableMap('<name>', Scope)` | 返回映射中给定键对应的值。第二个参数是键，以 scope 形式提供（如需要可使用 `.MakeScope`）。 |
| `GetVariableFromGlobalVariableMap('<name>', Scope)` | 返回全局映射中给定键对应的值。 |

### 变量映射 Effect

另见：
Effect
| Effect | 描述 | 示例 | Scopes | 目标 |
|---|---|---|---|---|
| add_to_global_variable_map | 将 event target 添加到全局变量映射中，持续指定时长；无法更新现有键的值 | add_to_global_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| add_to_local_variable_map | 将 event target 添加到局部变量映射中，持续指定时长；无法更新现有键的值 | add_to_local_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| add_to_variable_map | 将 event target 添加到变量映射中，持续指定时长；无法更新现有键的值 | add_to_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| clear_global_variable_map | 清空映射 | clear_global_variable_map = variable_name | none |  |
| clear_local_variable_map | 清空映射 | clear_local_variable_map = variable_name | none |  |
| clear_variable_map | 清空映射 | clear_variable_map = variable_name | none |  |
| every_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | every_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | every_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_variable_map | 遍历变量映射中的所有键。 | every_key_in_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| ordered_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | ordered_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | ordered_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_key_in_variable_map | 遍历变量映射中的所有键。 | ordered_key_in_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| random_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | random_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | random_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_variable_map | 遍历变量映射中的所有键。 | random_key_in_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| remove_from_global_variable_map | 从全局变量映射中移除目标 | remove_from_global_variable_map = { name = name of the map key = event target } | none |  |
| remove_from_local_variable_map | 从局部变量映射中移除目标 | remove_from_variable_map = { name = name of the map key = event target } | none |  |
| remove_from_variable_map | 从变量映射中移除目标 | remove_from_variable_map = { name = name of the map key = event target } | none |  |

### 变量映射 Trigger

另见：
Trigger
| Trigger | 描述 | 示例 | Scopes | 目标 |
|---|---|---|---|---|
| any_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | any_key_in_global_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | any_key_in_local_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_key_in_variable_map | 遍历变量映射中的所有键。 | any_key_in_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| global_variable_map_size |  | global_variable_map_size = { name = the name of the global map value >= script value or number } | none |  |
| has_global_variable_map | 检查当前 scope 是否拥有指定的全局变量映射 | has_global_variable_map = name | none |  |
| has_local_variable_map | 检查当前 scope 是否拥有指定的局部变量映射 | has_local_variable_map = name | none |  |
| has_variable_map | 检查当前 scope 是否拥有指定的变量映射 | has_variable_map = name | none |  |
| is_key_in_global_variable_map | 检查某个目标是否是全局变量映射中的键 | is_key_in_global_variable_map = { name = name of the variable target = event target } | none |  |
| is_key_in_local_variable_map | 检查某个目标是否是局部变量映射中的键 | is_key_in_local_variable_map = { name = name of the variable target = event target } | none |  |
| is_key_in_variable_map | 检查某个目标是否是变量映射中的键 | is_key_in_variable_map = { name = name of the variable target = event target } | none |  |
| is_value_in_global_variable_map | 检查某个目标是否是全局变量映射中的值 | is_value_in_global_variable_map = { name = name of the variable target = event target } | none | none |
| is_value_in_local_variable_map | 检查某个目标是否是局部变量映射中的值 | is_value_in_local_variable_map = { name = name of the variable target = event target } | none | none |
| is_value_in_variable_map | 检查某个目标是否是变量映射中的值 | is_value_in_variable_map = { name = name of the variable target = event target } | none | none |
| local_variable_map_size |  | local_variable_map_size = { name = the name of the local map value >= script value or number } | none |  |
| variable_map_size |  | variable_map_size = { name = the name of the global map value >= script value or number } | none |  |

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effect](Effect.md) • [Event target](Event target.md) • [Scope](Scope.md) • [Trigger](Trigger.md) [宏](Macro.md) • [修改器类型](Modifier types.md) • [On action](https://vic3.paradoxwikis.com/On_actions) • [脚本值](Script value.md) • 变量 |
|---|---|

| 脚本内容 | [决议](Decision modding.md) • [事件](Event modding.md) • [历史](History modding.md) • [日志](Journal modding.md) • [修改器](Modifier modding.md) • 目标 • [脚本 GUI](Scripted gui.md) |
|---|---|
| Scripted types | [建筑](Building modding.md) • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图片](Event images.md) • [图像资源](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [音效](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [模组](Mod.md) • [模组兼容性](Mod compatibility.md) • [模组结构](Mod structure.md) • [脚本测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [模组翻译](Mod translation.md) • [新国家模组制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州模组制作指南](State modding guide.md) |
|---|---|