---
title: Variable
source: https://vic3.paradoxwikis.com/Variable
pageid: 7819
categories: [1.13, Modding]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

**Variables** are the primary method for content-makers to capture, access, and manipulate information.

These are scripted [event targets](Event target.md) that can hold values or scopes. Many [effects](Effect.md) and [triggers](Trigger.md) can use variables as a target in place of a directly scripted object or value. Variables can also be used as [scopes](Scope.md).

This article also covers the associated **List**, **Variable List**, and **Variable Map** systems.

## Scripted Variables

### Overview

There are three types of variables: "regular", global, and local.

| Variable type | Scoped | Persistent | Event target |
|---|---|---|---|
| "regular" | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | var: |
| global | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | global_var: |
| local | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | local_var: |

- "Regular" variables are saved to game objects and persist outside of the effect chain. These are accessed using the `var:` event target in that object's scope.

- Local variables are scope-agnostic and are garbage collected at the end of the effect chain. These are accessed using the `local_var:` event target in *any scope* until the end of the effect chain.
- Global variables are saved to the global state and persist outside of the effect chain. These are accessed using the `global_var:` event target in any scope.

*Note: Local variables are automatically removed at the end of the effect chain; regular and global variables will persist until explicitly removed by effect.*

### Scripted Variable Usage

**Setting and Using Variables**

Variables are set, manipulated, and removed via effect. For example:

```
# This sets a variable in the current scope that is named "foo" and has a value of "1"
set_variable = {
  name = foo
  value = 1
}

# This removes a variable in the current scope with the name "foo"
remove_variable = foo
```

Variables can hold a numerical or Boolean value, a game object as a scope, or a localization key. Any script term where a [scope](Scope.md) or [script value](Script value.md) can be used can generally accept a variable as well. A saved scope can be cached to a variable for access outside of its initial effect chain. For example:

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

#### Accessing and Manipulating Numerical Variables

Once a variable has been set, its value can be used in many effects and triggers. For example:

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

The `change_variable` and `clamp_variable` effects can be used to directly manipulate variables. For example:

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

While manipulating values with these effects is easy, they provide no protection for cases where a variable becomes unset or loses its value. As an alternative, it is often more reliable to use `set_variable` to change a numerical variable by using script math. For example:

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

This effect checks if the variable foo exists. If it already exists, the new value is set to the current value. If it does not exist yet, the value gets set to 0. Then 5 is added to the value. This means the variable is set, even if it does not yet exist and changes its current value by 5. If this effect is used a lot, it might be a good idea to create a scripted effect with [parameters](Macro.md) for it. This is an example for such a scripted effect:

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

This effect does the same as the effect further up but it is more versatile and can easily get reused. An example for its usage might look like this:

```
 prefix_change_variable_effect = {
	NAME = foo
	AMOUNT = -3
	ADDITIONAL_SCRIPT_MATH = "min = 0 max = 100"
}
```

This usage would change the variable `foo` by `-3` and would additionally limit the variable to a minimum of 0 and a maximum of 100. Note that `ADDITIONAL_SCRIPT_MATH` could be used for even more script math.

### Flags and Variables

Scopes corresponding to [localization](Localization.md) keys can be saved to variables using the `flag:` event target. This is essential for interface modding as it allows mod-makers to dynamic change text displayed in the UI. For example:

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

Flag variables can be used in comparisons in a manner similar to event flags in other games:

```
if = {
    limit = {
        var:foo = flag:test
    }
    <effects>
}
```

In [GUIscript](GUI script.md), the function `GetFlagName` accesses and displays the localization string associated with the saved key. For example:

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

In this example, the variable `test` would display the text `bar.`

*Note: the flag variable does not contain the entire localization string. It only contains the localization key. The GetFlagName gui function is required to access its associated key.*

### Scripted Variable Effects

See also:
Effect
| Effect | Description | Example | Scopes | Targets |
|---|---|---|---|---|
| add_to_global_variable_list | Adds the event target to a global variable list for the given duration | add_to_global_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| add_to_global_variable_map | Adds the event target to a global variable map for the given duration; cannot update a value for an existing key | add_to_global_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| add_to_local_variable_list | Adds the event target to a local variable list for the given duration | add_to_local_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| add_to_local_variable_map | Adds the event target to a local variable map for the given duration; cannot update a value for an existing key | add_to_local_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| add_to_variable_list | Adds the event target to a variable list for the given duration | add_to_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| add_to_variable_map | Adds the event target to a variable map for the given duration; cannot update a value for an existing key | add_to_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| change_global_variable | Changes the value of a numeric global variable | change_global_variable = { name = <global variable> <operation type> = <value> } The valid operations are add, subtract, multiply, divide, modulo, min and max | none |  |
| change_local_variable | Changes the value of a numeric local variable | change_local_variable = { name = <local variable> <operation type> = <value> } The valid operations are add, subtract, multiply, divide, modulo, min and max | none |  |
| change_variable | Changes the value of a numeric variable | change_variable = { name = <variable name> <operation type> = <value> } The valid operations are add, subtract, multiply, divide, modulo, min and max | none |  |
| clamp_global_variable | Clamps a global variable the specified max and min | clamp_global_variable = { name = <global variable> max = <value> min = <value> } | none |  |
| clamp_local_variable | Clamps a local variable the specified max and min | clamp_local_variable = { name = <local variable> max = <value> min = <value> } | none |  |
| clamp_variable | Clamps a variable the specified max and min | clamp_variable = { name = <variable name> max = <value> min = <value> } | none |  |
| clear_global_variable_list | Empties the list | clear_global_variable_list = variable_name | none |  |
| clear_global_variable_map | Empties the map | clear_global_variable_map = variable_name | none |  |
| clear_local_variable_list | Empties the list | clear_local_variable_list = variable_name | none |  |
| clear_local_variable_map | Empties the map | clear_local_variable_map = variable_name | none |  |
| clear_variable_list | Empties the list | clear_variable_list = variable_name | none |  |
| clear_variable_map | Empties the map | clear_variable_map = variable_name | none |  |
| every_in_global_list | Iterate through all items in global list. | every_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| every_in_list | Iterate through all items in list. | every_in_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| every_key_in_global_variable_map | Iterate through all keys in a global variable map. | every_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_local_variable_map | Iterate through all keys in a local variable map. | every_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_variable_map | Iterate through all keys in a variable map. | every_key_in_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| ordered_in_list | Iterate through all items in list. | ordered_in_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_key_in_global_variable_map | Iterate through all keys in a global variable map. | ordered_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_key_in_local_variable_map | Iterate through all keys in a local variable map. | ordered_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_key_in_variable_map | Iterate through all keys in a variable map. | ordered_key_in_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| random_in_list | Iterate through all items in list. | random_in_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| random_key_in_global_variable_map | Iterate through all keys in a global variable map. | random_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_local_variable_map | Iterate through all keys in a local variable map. | random_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_variable_map | Iterate through all keys in a variable map. | random_key_in_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| remove_from_global_variable_map | Removes the target from a global variable map | remove_from_global_variable_map = { name = name of the map key = event target } | none |  |
| remove_from_list | Removes the current scope from a named list | remove_from_list = <list_name> | none |  |
| remove_from_local_variable_map | Removes the target from a local variable map | remove_from_variable_map = { name = name of the map key = event target } | none |  |
| remove_from_variable_map | Removes the target from a variable map | remove_from_variable_map = { name = name of the map key = event target } | none |  |
| remove_global_variable | Removes a global variable | remove_global_variable = variable_name | none |  |
| remove_list_global_variable | Removes the target from a global variable list | remove_list_global_variable = { name = <global variable> target = <event target> } | none |  |
| remove_list_local_variable | Removes the target from a local variable list | remove_list_local_variable = { name = <local variable> target = <event target> } | none |  |
| remove_list_variable | Removes the target from a variable list | remove_list_variable = { name = <variable name> target = <event target> } | none |  |
| remove_variable | Removes a variable | remove_variable = variable_name | none |  |
| round_global_variable | Rounds a global variable to the nearest specified value | round_global_variable = { name = <global variable> nearest = <script_value> } | none |  |
| round_local_variable | Rounds a local variable to the nearest specified value | round_local_variable = { name = <local variable> nearest = <script_value> } | none |  |
| round_variable | Rounds a variable to the nearest specified value | round_variable = { name = <variable name> nearest = <script_value> } | none |  |
| set_global_variable | Sets a global variable | set_global_variable = { name = <global variable> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } This variable will be accessible with global_var:<variable name>. Can also be used as set_global_variable = X (equivalent to set_global_variable = { name = X value = yes }) | none |  |
| set_local_variable | Sets a local variable | set_local_variable = { name = <local variable> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } This variable will be accessible with local_var:<variable name>, until the end of the current effect or event chain. Can also be used as set_local_variable = X (equivalent to set_local_variable = { name = X value = yes }) | none |  |
| set_variable | Sets a variable | set_variable = { name = <variable name> value = <event target>/<script_value>/<flag> days/weeks/months/years = <script_value> (optional) } This variable will be accessible from the scope where it is set with var:<variable name>. Can also be used as set_variable = X (equivalent to set_variable = { name = X value = yes }) | none |  |
| sort_global_variable_list | Sorts a global variable list | sort_global_variable_list = { name = <global variable> order = <math script> } | none |  |
| sort_local_variable_list | Sorts a local variable list | sort_local_variable_list = { name = <local variable> order = <math script> } | none |  |
| sort_variable_list | Sorts a variable list | sort_variable_list = { name = <variable name> order = <math script> } | none |  |

### Scripted Variable Triggers

See also:
Trigger
| Trigger | Description | Example | Scopes | Targets |
|---|---|---|---|---|
| has_global_variable | Checks whether the current scope has the specified global variable set | has_global_variable = name | none |  |
| has_local_variable | Checks whether the current scope has the specified local variable set | has_local_variable = name | none |  |
| has_variable | Checks whether the current scope has the specified variable set | has_variable = name | none |  |

## Temporary Lists

**Lists** are temporary collections of [scopes](Scope.md) built during effect execution.

### Overview

There are two variants, following the same pattern as `save_scope_as` and `save_temporary_scope_as`

- `add_to_list` — the list persists for the entire top-level effect execution (i.e. across an event's `immediate` and `option` blocks).
- `add_to_temporary_list` — the list only persists within the current block and its children.

### List Usage

Lists are built by adding scopes during effect execution and used by iterating over them.

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

### List Effects

See also:
Effect
| Effect | Description | Example | Scopes | Targets |
|---|---|---|---|---|
| add_to_list | Adds the current scope to an arbitrarily-named list (or creates the list if not already present) to be referenced later in the (unbroken) event chain | scope = { add_to_list = <name_of_list> } add_to_list = { name = <name_of_list> value = <script_value> } NOTE, if adding a permanent target to a temporary list, the whole list becomes permanent | none |  |
| add_to_temporary_list | Adds the current scope to an arbitrarily-named list (or creates the list if not already present) to be referenced later in the same effect | add_to_temporary_list = <name_of_list> add_to_temporary_list = { name = <name_of_list> value = <script_value> } NOTE, if adding a temporary target to a permanent list, the list will stay permanent | none |  |
| every_in_list | Iterate through all items in list. | every_in_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_in_list | Iterate through all items in list. | ordered_in_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| random_in_list | Iterate through all items in list. | random_in_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| remove_from_list | Removes the current scope from a named list | remove_from_list = <list_name> | none |  |

### List Triggers

See also:
Trigger
| Trigger | Description | Example | Scopes | Targets |
|---|---|---|---|---|
| add_to_temporary_list | Saves a temporary target for use during the trigger execution | This is used to build lists in triggers. If used within an any-trigger, placement within the trigger is quite important. The game will iterate through every instance of the any-trigger until it finds a single instance that fulfills the requirements, and then it will stop. In order to add every instance of a scope that fulfills certain conditions, use "count = all" while also placing this "effect" at the very end of the any-trigger so that every condition is evaluated for every iteration. | none |  |
| any_in_list | Iterate through all items in list. | any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| is_in_list | Checks if a target in in a list |  | none |  |
| list_size | Checks the size of a list | list_size = { name = <list name> value >= <value> } | none | value |

## Variable Lists

**Variable lists** (also called "lists" or "varlists") are persistent, ordered, and [iterable](https://vic3.paradoxwikis.com/Iterators) collections of [scopes](Scope.md) stored as named lists. Like scripted variables, there are three types of variable lists:

- "**Regular" variable lists** are saved to game objects and persist outside of the effect chain. These are accessed using the `x_in_variable_list` iterators in that object's scope.

- **Local variable lists** are scope-agnostic and are garbage collected at the end of the effect chain. These are accessed using the `x_in_local_list` iterators in *any scope* until the end of the effect chain.
- **Global variable lists** are saved to the global state and persist outside of the effect chain. These are accessed using the `x_in_global_list` iterators in any scope.

### Overview

Variable lists are effectively custom [iterator](https://vic3.paradoxwikis.com/Iterator) lists, whose elements are specifically added and removed by effect. In every other way, variable lists are the same as any other iterator. Variable lists follow the same three-type pattern as variables:

| Type | Scoped | Persistent | Effect prefix | Trigger prefix |
|---|---|---|---|---|
| "regular" | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | `add_to_variable_list` | `is_target_in_variable_list` |
| global | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | `add_to_global_variable_list` | `is_target_in_global_variable_list` |
| local | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | `add_to_local_variable_list` | `is_target_in_local_variable_list` |

*Note: Local variable lists are automatically removed at the end of the effect chain; regular and global lists will persist until explicitly removed by effect.*

### Variable List Usage

An object is added to a variable list by using the `add_to_variable_list` effect. If the variable list does not exist yet, it will be created. For example:

```
add_to_variable_list = {
	name = states_list
	target = c:FRA.capital
}
```

Game objects can also be evaluated for presence in a given list with the relevant trigger. For example:

```
is_target_in_variable_list = {
	name = states_list
	target = c:FRA.capital
}
```

Once a list exits, the items in it can be iterated using the same iterator effects and triggers as temporary lists, but using the `variable` parameter instead of `list`. For global and local variable lists, the iterator name includes the scope prefix. For example:

| Type | Effect iterators | Trigger iterator |
|---|---|---|
| "regular" | `every_in_list`, `random_in_list`, `ordered_in_list` | `any_in_list` |
| global | `every_in_global_list`, `random_in_global_list`, `ordered_in_global_list` | `any_in_global_list` |
| local | `every_in_local_list`, `random_in_local_list`, `ordered_in_local_list` | `any_in_local_list` |

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

### Variable List Effects

See also:
Effect
| Effect | Description | Example | Scopes | Targets |
|---|---|---|---|---|
| add_to_global_variable_list | Adds the event target to a global variable list for the given duration | add_to_global_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| add_to_local_variable_list | Adds the event target to a local variable list for the given duration | add_to_local_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| add_to_variable_list | Adds the event target to a variable list for the given duration | add_to_variable_list = { name = <variable name> target = <event target> days/weeks/months/years = <script_value> } | none |  |
| clear_global_variable_list | Empties the list | clear_global_variable_list = variable_name | none |  |
| clear_local_variable_list | Empties the list | clear_local_variable_list = variable_name | none |  |
| clear_variable_list | Empties the list | clear_variable_list = variable_name | none |  |
| every_in_global_list | Iterate through all items in global list. | every_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| every_in_list | Iterate through all items in list. | every_in_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| every_in_local_list | Iterate through all items in local list. | every_in_local_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_in_global_list | Iterate through all items in global list. list = name or variable = name | ordered_in_global_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_in_list | Iterate through all items in list. | ordered_in_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_in_local_list | Iterate through all items in local list. list = name or variable = name | ordered_in_local_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| random_in_global_list | Iterate through all items in global list. | random_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| random_in_list | Iterate through all items in list. | random_in_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| random_in_local_list | Iterate through all items in local list. | random_in_local_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| remove_list_global_variable | Removes the target from a global variable list | remove_list_global_variable = { name = <global variable> target = <event target> } | none |  |
| remove_list_local_variable | Removes the target from a local variable list | remove_list_local_variable = { name = <local variable> target = <event target> } | none |  |
| remove_list_variable | Removes the target from a variable list | remove_list_variable = { name = <variable name> target = <event target> } | none |  |
| sort_global_variable_list | Sorts a global variable list | sort_global_variable_list = { name = <global variable> order = <math script> } | none |  |
| sort_local_variable_list | Sorts a local variable list | sort_local_variable_list = { name = <local variable> order = <math script> } | none |  |
| sort_variable_list | Sorts a variable list | sort_variable_list = { name = <variable name> order = <math script> } | none |  |

### Variable List Triggers

See also:
Trigger
| Trigger | Description | Example | Scopes | Targets |
|---|---|---|---|---|
| add_to_temporary_list | Saves a temporary target for use during the trigger execution | This is used to build lists in triggers. If used within an any-trigger, placement within the trigger is quite important. The game will iterate through every instance of the any-trigger until it finds a single instance that fulfills the requirements, and then it will stop. In order to add every instance of a scope that fulfills certain conditions, use "count = all" while also placing this "effect" at the very end of the any-trigger so that every condition is evaluated for every iteration. | none |  |
| any_in_global_list | Iterate through all items in global list. | any_in_global_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| any_in_list | Iterate through all items in list. | any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| any_in_local_list | Iterate through all items in local list. | any_in_local_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| global_variable_list_size | Checks the size of a global variable list | global_variable_list_size = { name = <variable name> value >= <value> } | none |  |
| has_global_variable_list | Checks whether the current scope has the specified global variable list set | has_global_variable_list = name | none |  |
| has_local_variable_list | Checks whether the current scope has the specified local variable list set | has_local_variable_list = name | none |  |
| has_variable_list | Checks whether the current scope has the specified variable list set | has_variable_list = name | none |  |
| is_target_in_global_variable_list | Checks if a target is in a global variable list | is_target_in_global_variable_list = { name = <variable name> target = <event target> } | none |  |
| is_target_in_local_variable_list | Checks if a target is in a local variable list | is_target_in_local_variable_list = { name = <variable name> target = <event target> } | none |  |
| is_target_in_variable_list | Checks if a target is in a variable list | is_target_in_variable_list = { name = <variable name> target = <event target> } | none |  |
| local_variable_list_size | Checks the size of a local variable list | local_variable_list_size = { name = <variable name> value >= <value> } | none |  |
| variable_list_size | Checks the size of a variable list | variable_list_size = { name = <variable name> value >= <value> } | none |  |

### Variable Lists in UI

Variable Lists can be utilized as a `datamodel` for UI elements with the objects in the list being forwarded as the `datacontext` of its children. For example:

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

The following UI functions are useful for managing and using variable maps in GUI:

| Function | Description | Type |
|---|---|---|
| Scope.GetList | Gets the objects saved to a list that is present in the current scope. | Function |
| GetGlobalList | Gets the objects saved to a global list. | Global Promote |
| IsDataModelEmpty | Checks for the provided datamodel has any objects in it. Silently fails if the provided Variable List does not exist | Global Function |
| DataModelHasItems | Checks for the presence of any objects in the provided datamodel. | Global Function |
| GetDataModelSize | Gets the size the provided datamodel | Global Function |

## Variable Maps

**Variable maps** (also called "maps" or "varmaps") are associative arrays that map relationships between two [scopes](Scope.md), where one scope (the key) links to another (the value). These relationships are also called "key-value pairs."

Like scripted variables, there are three types of variable lists:

- "**Regular" variable maps** are saved to game objects and persist outside of the effect chain. These are accessed using the `variable_map` event target in that object's scope.

- **Local variable maps** are scope-agnostic and are garbage collected at the end of the effect chain. These are accessed using the `local_variable_map` event target in *any scope* until the end of the effect chain.
- **Global variable maps** are saved to the global state and persist outside of the effect chain. These are accessed using the `global_variable_map` event target in any scope.

### Overview

Variable maps follow the same three-type pattern as variables and variable lists:

| Type | Scoped | Persistent | Effect prefix | Scope link |
|---|---|---|---|---|
| "regular" | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | `add_to_variable_map` | `"variable_map(name\|key)"` |
| global | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | `add_to_global_variable_map` | `"global_variable_map(name\|key)"` |
| local | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | `add_to_local_variable_map` | `"local_variable_map(name\|key)"` |

*Note: Local variable maps are automatically removed at the end of the effect chain; regular and global variable maps will persist until explicitly removed by effect.*

Variable maps have several properties that distinguish them from other data structures:

- **Scope substitution:** Some scopes in the game do not accept variables to be stored on them. Global variable maps can work around this by using the scope as a key and storing associated data as the value.
- **Performance at scale:** Accessing a value by key and checking whether a key exists are relatively fast operations. These benefits become more significant as the data structure grows larger. For systems that operate on many scopes (e.g. a large proportion of countries, locations, or pops), variable maps may offer performance improvements over variable lists.
- **Unordered:** Variable maps are unordered. Regardless of insertion order, iterating through a map produces a fixed, internal order. Sorting is still possible using `ordered_key_in_variable_map`.
- **Any scope as key or value:** Besides game objects (countries, characters, locations, etc.), variable maps can use numerical values, boolean values, and other expressions the game considers scopes as both keys and values.
- **Usable as arrays:** Since integer values can be used as map keys, variable maps can serve as indexed arrays where the key is the position.

### Variable List Usage

A key-value pair is added to a variable map using the `add_to_variable_map` effect. If the variable map does not exist yet, it will be created. For example:

```
add_to_variable_map = {
    name = rival_map # the map name, a string identifier. This is used to access the map in other script. 
    key = c:FRA # any scope (countries, locations, characters, etc.) or a number (1, 2, 3) 
    value = c:ENG # any scope or number — what the key is "paired" or "mapped" with
}
```

A value in a variable map can be accessed using the appropriate `variable_map` event target with its key. For example: *Note: The variable map event targets must be wrapped with " since it requires arguments. These are the map name and the key.*

```
"variable_map(rival_map|c:FRA)" = {
    add_prestige = -10 # Since the key "c:FRA" is paired to the scope "c:ENG" (the stored value), accessing the key c:FRA will scope to c:ENG
}
```

**Adding a key that already exists does not overwrite the existing key-value pair.** The `add_to_variable_map` effect will fail if a key is already present. To update an entry, the old key must be removed first, then re-added with the new paired value:

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

You can also use this event target in comparisons:

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

#### Using Parameters in Variable Maps

Main article:
Macro
Because the variable map statement is enclosed in quotation marks, scripted effect and scripted trigger arguments are not resolved inside it. To pass a dynamic key, save the argument to a local variable first:

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

This workaround only applies to the key (second argument). The map name (first argument) is a identifier, not a scope, so it cannot be parameterized through variables or arguments:

```
# Neither of these work
"global_variable_map($my_map$|c:ENG)" = { ... }
"global_variable_map(local_var:map_name|c:ENG)" = { ... }
```

### Variable Maps in UI

Variable maps can be accessed in GUI files using the following data functions:

| Function | Description |
|---|---|
| `Scope.GetMapKeys('<name>')` | Returns a datamodel of all keys in the map stored on a scope. |
| `GetGlobalMapKeys('<name>')` | Returns a datamodel of all keys in a global map. |
| `Scope.GetVariableFromVariableMap('<name>', Scope)` | Returns the value for a given key in the map. The second argument is the key, provided as a scope (use `.MakeScope` if needed). |
| `GetVariableFromGlobalVariableMap('<name>', Scope)` | Returns the value for a given key in a global map. |

### Variable Map Effects

See also:
Effect
| Effect | Description | Example | Scopes | Targets |
|---|---|---|---|---|
| add_to_global_variable_map | Adds the event target to a global variable map for the given duration; cannot update a value for an existing key | add_to_global_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| add_to_local_variable_map | Adds the event target to a local variable map for the given duration; cannot update a value for an existing key | add_to_local_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| add_to_variable_map | Adds the event target to a variable map for the given duration; cannot update a value for an existing key | add_to_variable_map = { name = The name of the variable map key = An event target value = Another event target days/weeks/months/years = An optional duration; the number of days or script value } | none |  |
| clear_global_variable_map | Empties the map | clear_global_variable_map = variable_name | none |  |
| clear_local_variable_map | Empties the map | clear_local_variable_map = variable_name | none |  |
| clear_variable_map | Empties the map | clear_variable_map = variable_name | none |  |
| every_key_in_global_variable_map | Iterate through all keys in a global variable map. | every_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_local_variable_map | Iterate through all keys in a local variable map. | every_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_variable_map | Iterate through all keys in a variable map. | every_key_in_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| ordered_key_in_global_variable_map | Iterate through all keys in a global variable map. | ordered_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_key_in_local_variable_map | Iterate through all keys in a local variable map. | ordered_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_key_in_variable_map | Iterate through all keys in a variable map. | ordered_key_in_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| random_key_in_global_variable_map | Iterate through all keys in a global variable map. | random_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_local_variable_map | Iterate through all keys in a local variable map. | random_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_variable_map | Iterate through all keys in a variable map. | random_key_in_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| remove_from_global_variable_map | Removes the target from a global variable map | remove_from_global_variable_map = { name = name of the map key = event target } | none |  |
| remove_from_local_variable_map | Removes the target from a local variable map | remove_from_variable_map = { name = name of the map key = event target } | none |  |
| remove_from_variable_map | Removes the target from a variable map | remove_from_variable_map = { name = name of the map key = event target } | none |  |

### Variable Map Triggers

See also:
Trigger
| Trigger | Description | Example | Scopes | Targets |
|---|---|---|---|---|
| any_key_in_global_variable_map | Iterate through all keys in a global variable map. | any_key_in_global_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_key_in_local_variable_map | Iterate through all keys in a local variable map. | any_key_in_local_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_key_in_variable_map | Iterate through all keys in a variable map. | any_key_in_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| global_variable_map_size |  | global_variable_map_size = { name = the name of the global map value >= script value or number } | none |  |
| has_global_variable_map | Checks whether the current scope has the specified global variable map | has_global_variable_map = name | none |  |
| has_local_variable_map | Checks whether the current scope has the specified local variable map | has_local_variable_map = name | none |  |
| has_variable_map | Checks whether the current scope has the specified variable map | has_variable_map = name | none |  |
| is_key_in_global_variable_map | Checks if a target is a key in a global variable map | is_key_in_global_variable_map = { name = name of the variable target = event target } | none |  |
| is_key_in_local_variable_map | Checks if a target is a key in a local variable map | is_key_in_local_variable_map = { name = name of the variable target = event target } | none |  |
| is_key_in_variable_map | Checks if a target is a key in a variable map | is_key_in_variable_map = { name = name of the variable target = event target } | none |  |
| is_value_in_global_variable_map | Checks if a target is a value in a global variable map | is_value_in_global_variable_map = { name = name of the variable target = event target } | none | none |
| is_value_in_local_variable_map | Checks if a target is a value in a local variable map | is_value_in_local_variable_map = { name = name of the variable target = event target } | none | none |
| is_value_in_variable_map | Checks if a target is a value in a variable map | is_value_in_variable_map = { name = name of the variable target = event target } | none | none |
| local_variable_map_size |  | local_variable_map_size = { name = the name of the local map value >= script value or number } | none |  |
| variable_map_size |  | variable_map_size = { name = the name of the global map value >= script value or number } | none |  |

## References

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • Variables |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| Map | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • [States](State modding.md) |
|---|---|

| Interface | [Interface](Interface modding.md) • [GUI script](GUI script.md) • [Localization](Localization.md) • [Customizable localization](Localization.md) • [Script localization](Script localization.md) |
|---|---|

| Graphics | [3D Models](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|

| Audio | Music • [Sound](Sound modding.md) |
|---|---|

| Other | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| Guides | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|
