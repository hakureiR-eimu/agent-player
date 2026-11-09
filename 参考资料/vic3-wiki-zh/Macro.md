---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Macro
source: https://vic3.paradoxwikis.com/Macro
pageid: 8876
categories: [Potentially_outdated, 1.10, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。至少部分内容最后验证于 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10。

参见：
Effects
，
Triggers
**宏（Macros）** 是可复用的脚本块。宏主要有两种类型：**scripted effect（脚本化效果）** 和 **scripted trigger（脚本化触发器）**。宏通常等价于把脚本从定义处复制到使用处。宏对于维护常用效果非常有用，因为只需更新一个脚本块，即可同时更新多个 trigger 或 effect 中的效果。

## 定义

scripted effect 和 scripted trigger 分别定义在各自的文件夹中：/common/scripted_effects/ 与 /common/scripted_triggers/

一个 scripted effect 或 trigger 由一个脚本名称和一个脚本块定义，例如：

```
unification_claims_effect = {
    if = {
        limit = {
            any_state_region = {
                any_scope_state = {
                    is_homeland_of_country_cultures = ROOT
                    NOT = { owner = ROOT }
                    NOT = { has_claim_by = ROOT }
                }
            }
        }
        every_state_region = {
            limit = {
                any_scope_state = {
                    is_homeland_of_country_cultures = ROOT
                    NOT = { owner = ROOT }
                    NOT = { has_claim_by = ROOT }
                }
            }
            add_claim = ROOT
        }
    }
    else = {
        add_loyalists = {
            value = 0.05
        }
    }
}
```

这个特定的 scripted effect 被用于多个国家成立事件。

scripted effect 是一个常规的 [effect](Effect.md) 块，可以按需使用任何效果脚本。类似地，scripted trigger 是一个常规的 [trigger](Trigger.md) 块，可以按需使用任何触发器脚本。这包括在其他 scripted effect 和 scripted trigger 中使用 scripted effect 和 scripted trigger。

### 本地化（Localization）

参见：
Localization
默认情况下，使用 scripted effect 或 trigger 会生成与直接在原地编写脚本相同的工具提示。因此，把宏脚本包在 `hidden_effect/hidden_trigger = { }`、`custom_tooltip = { }` 或 `custom_description = { }` 块中往往很方便。这些脚本块的功能类似，都是隐藏自动生成的工具提示。第一种 `hidden_effect/hidden_trigger = { }` 只是阻止其中的任何脚本生成工具提示。第二种 `custom_tooltip = { }` 会阻止自动工具提示，改为显示指定的本地化字符串。最后一种 `custom_description = { }` 会设置一整套效果或触发器本地化集，分别定义在 common/effect_localization/ 或 common/trigger_localization/ 中。有关如何创建本地化集的详情，参见 /Victoria 3/game/common/trigger_localization/trigger_localization.md。

## 使用

简单的 scripted effect 通过 `scripted_effect_name = yes` 调用。简单的 scripted trigger 可通过 `scripted_trigger_name = yes/no` 调用。`scripted_trigger_name = no` 等价于 `NOT = { scripted_trigger_name = yes }`，即当该 scripted trigger 返回 false 时它返回 true。

使用上面那个 scripted effect 宏，这个事件选项：

```
option = {
    name = formation_example.1.a
    unification_claims_effect = yes
    add_modifier = {
        name = unification_prestige
        days = very_long_modifier_time
    }
}
```

与下面这个事件选项在效果上完全相同：

```
option = {
    name = formation_example.2.a
    if = {
        limit = {
            any_state_region = {
                any_scope_state = {
                    is_homeland_of_country_cultures = ROOT
                    NOT = { owner = ROOT }
                    NOT = { has_claim_by = ROOT }
                }
            }
        }
        every_state_region = {
            limit = {
                any_scope_state = {
                    is_homeland_of_country_cultures = ROOT
                    NOT = { owner = ROOT }
                    NOT = { has_claim_by = ROOT }
                }
            }
            add_claim = ROOT
        }
    }
    else = {
        add_loyalists = {
            value = 0.05
        }
    }
    add_modifier = {
        name = unification_prestige
        days = very_long_modifier_time
    }
}
```

游戏会把前者当作后者来读取，scripted effect 名称所引用的脚本块实际上被插入到了调用处。

## 参数

scripted effect 和 trigger 还可以使用*参数*，即字面上的脚本替换。这样可以在调用宏时对其进行定制。

定义示例：

```
transfer_state = { # Changes ownership of any state within a STATE region (e.g. s:STATE_MONTENEGRO) from GIVER to TAKER countries (e.g. c:TUR). Automatically checks GIVER exists and owns the state.
    if = {
        limit = {
            exists = $GIVER$
            exists = $TAKER$
            $TAKER$ != $GIVER$
            $STATE$ = {
                any_scope_state = {
                    $GIVER$ = owner
                }
            }
        }
        $STATE$ = {
            every_scope_state = {
                limit = {
                    owner = $GIVER$
                }
                set_state_owner = $TAKER$
            }
        }
    }
}
```

这个 scripted effect 有三个参数，以 `$` 开头和结尾的字符串表示：`$GIVER$`、`$TAKER$` 和 `$STATE$`。字符串可以是任何内容，但应便于记忆其用途。

### 参数的使用

调用带参数的 scripted effect 或 trigger 时，格式如下：

```
transfer_state = {
    STATE = s:STATE_MONTENEGRO
    GIVER = c:TUR
    TAKER = root
}
```

注意参数使用相同的大小写，但不带 `$`。传给参数的文本可以“裸露”给出，也可以用双引号包裹。如果所给文本含有空格，则必须使用引号。

参数以字面文本替换的方式传递，因此对于上面定义的 scripted effect，这次调用等价于以下脚本：

```
transfer_state = { # Changes ownership of any state within a STATE region (e.g. s:STATE_MONTENEGRO) from GIVER to TAKER countries (e.g. c:TUR). Automatically checks GIVER exists and owns the state.
    if = {
        limit = {
            exists = c:TUR
            exists = root
            root != c:TUR
            s:STATE_MONTENEGRO = {
                any_scope_state = {
                    c:TUR = owner
                }
            }
        }
        s:STATE_MONTENEGRO = {
            every_scope_state = {
                limit = {
                    owner = c:TUR
                }
                set_state_owner = root
            }
        }
    }
}
```

#### 非成对参数的使用

原版游戏中大多数参数示例都与某个 effect 或 trigger 成对使用，但也可以使用非成对参数，即在调用宏时传入整个 trigger 或 effect。例如：

```
save_neighbor_with_state = {
    random_neighbouring_state = {
        limit = {
            owner = {
                $CRITERIA$
            }
        }
        save_scope_as = neighbor_state
        owner = {
            save_scope_as = neighbor_country
        }

        random_neighbouring_state = {
            limit = {
                owner = ROOT
            }
            save_scope_as = neighbor_neighbor_state
        }
    }
}
```

例如可以像下面这样使用。注意由于传入的文本包含空白字符（空格和换行），必须使用引号。

```
save_neighbor_with_state = {
    CRITERIA = "NOT = { is_country_type = decentralized }
        average_sol > root.average_sol"
}
```

#### 部分脚本替换

此外，由于这是字面上的脚本文本替换，参数甚至可以用来替换某个脚本术语的一部分，例如一个 scripted effect 可以写成：

```
example_effect = {
    $TYPE$_country = {
        add_treasury = 10
    }
}
```

有效的调用示例如下：

```
example_effect = {
    TYPE = random
}

example_effect = {
    TYPE = every_decentralized
}

example_effect = {
    TYPE = random_rival
}
```

只要最终生成的效果是有效的游戏效果，这样的参数用法就是有效的。

## 其他宏

除 scripted effect 和 trigger 之外，还有其他一些宏或类似宏的脚本元素。

### GUI function 宏

参见：
Interface modding
，
Data types
GUI function 宏定义在 /data_binding/ 中。示例参见 /Victoria 3/game/data_binding/gui_macros.txt。这些宏可用于 GUI 和本地化 function 中。与 scripted effect 和 trigger 一样，它们也是直接的文本替换，并且可以使用参数。

例如：

```
macro = {
    description = "Add a loc key with a trailing newline if a condition is satisfied"
    definition = "MakeLineIf(Condition, LocKey)"
    replace_with = "ConcatIfNeitherEmpty(AddLocalizationIf(Condition, LocKey), Localize( 'NEWLINE' ))"
}
```

这个宏可以通过 `[MakeLineIf(boolean, loc key)]` 调用。例如：

```
[MakeLineIf( IsZero(State.GetTradeCapacity), 'NO_WORLD_MARKET_ACCESS_DUE_TO_NO_TRADE_CAPACITY')]
```

这等价于以下内容，游戏会这样读取：

```
[ConcatIfNeitherEmpty(AddLocalizationIf( IsZero(State.GetTradeCapacity), 'NO_WORLD_MARKET_ACCESS_DUE_TO_NO_TRADE_CAPACITY'), Localize( 'NEWLINE' )]
```

### 脚本化列表（Scripted lists）

参见：
Scope § Iterators
脚本化列表定义在 /common/scripted_lists/ 中。它们是带内置 trigger 的自定义 [迭代器列表](Scope.md)。其定义方式如下：

```
scripted_list_name = {
    base = base_game_list
    conditions = {
        <triggers>
    }
}
```

基础游戏列表与去掉前缀的迭代器/列表集相同。例如，基础游戏列表 `country` 用于 `any_country`、`every_country`、`ordered_country` 和 `random_country`。

脚本化列表用给定的 trigger 过滤基础列表，可以像 `any_scripted_list_name`、`every_scripted_list_name`、`ordered_scripted_list_name` 和 `random_scripted_list_name` 一样使用。例如，有一个脚本化列表：

```
islamic_country = {
    base = country
    conditions = {
        OR = {
            country_has_state_religion = rel:sunni
            country_has_state_religion = rel:shiite
            country_has_state_religion = rel:ibadi
        }
    }
}
```

那么下面两段示例脚本是等价的：

```
every_country = {
    limit = {
        OR = {
            country_has_state_religion = rel:sunni
            country_has_state_religion = rel:shiite
            country_has_state_religion = rel:ibadi
        }
    }
    add_treasury = 10
}

every_islamic_country = {
    add_treasury = 10
}
```

后一个迭代器包含与列表定义中编写相同的 limit trigger。

### 脚本值（Script values）

主条目：
Script value
脚本值定义在 /common/script_values/ 中，与宏类似，尤其是静态脚本值。特别是，脚本值可用在大多数需要数字或数值的地方。

### @ 值

主条目：
Script value § @ values
@ 值是文件内部的宏。它们必须定义在使用它们的文件中，并且可以替代大多数数字值。

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) Macros • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本化内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本化类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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