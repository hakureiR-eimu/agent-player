---
title: Macro
source: https://vic3.paradoxwikis.com/Macro
pageid: 8876
categories: [Potentially_outdated, 1.10, Modding]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10.

See also:
Effects
,
Triggers
**Macros** are blocks of script that can be reused. There are two main types of macros: **scripted effects** and **scripted triggers**. A macro is usually equivalent to copying the script from where it is defined to where it is used. They are useful for maintaining commonly used effects, as only one script block needs to be updated to update the effect across multiple triggers or effects.

## Definition

Scripted effects and triggers are defined in their respective folders: /common/scripted_effects/ and /common/scripted_triggers/

A scripted effect or trigger is defined as a script name and a block of script, for example:

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

This particular scripted effect is used for several country formation events.

A scripted effect is a regular [effect](Effect.md) block and can use any effect scripting as required. Similarly, a scripted trigger is a regular [trigger](Trigger.md) block and can use any trigger scripting as required. This includes the use of scripted effects and triggers within other scripted effects and triggers.

### Localization

See also:
Localization
By default, using a scripted effect or trigger generates the same tooltip as if it were scripted in place. Thus, it is often convenient to wrap the macro script in a `hidden_effect/hidden_trigger = { }`, `custom_tooltip = { }`, or `custom_description = { }` block. These script blocks function similarly, by hiding the auto-generated tooltip. The first, `hidden_effect/hidden_trigger = { }`, simply prevents any contained script from generating tooltips. The second, `custom_tooltip = { }`, prevents auto tooltips and instead displays a specified localization string. The last, `custom_description = { }`, sets up a full effect or trigger localization set, defined in common/effect_localization/ or common/trigger_localization/, respectively. See /Victoria 3/game/common/trigger_localization/trigger_localization.md for details on how to create the localization set.

## Use

Simple scripted effects are called with `scripted_effect_name = yes`. Simple scripted triggers can are called with `scripted_trigger_name = yes/no`. `scripted_trigger_name = no` is equivalent to `NOT = { scripted_trigger_name = yes }`, that is, it returns true if the scripted trigger returns false.

Using the scripted effect macro from above, this event option:

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

And this event option are exactly identical in effect:

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

The game reads the first as though it were the second, with the script block referenced by the scripted effect name effectively being inserted in its place.

## Parameters

Scripted effects and triggers can also make use of *parameters*, which are literal script replacements. This allows for customization of the macro when it is called.

Example definition:

```
transfer_state = { # Changes ownership of any state within a STATE region (e.g. s:STATE_MONTENEGRO) from GIVER to TAKER countries (e.g. c:TUR). Automatically checks GIVER exists and owns the state.
    if = {
        limit = {
            exists = $GIVER$
            exists = $TAKER$
            $TAKER$ != $GIVER$
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

This scripted effect has three parameters, indicated as the strings starting and ending with `$`: `$GIVER$`, `$TAKER$`, and `$STATE$`. The strings can be anything, but should be mnemonic for their purpose.

### Parameter use

When calling a scripted effect or trigger with parameters, the format is like the following:

```
transfer_state = {
    STATE = s:STATE_MONTENEGRO
    GIVER = c:TUR
    TAKER = root
}
```

Note that the parameters are given with the same capitalization, but without `$`'s. The text given to the parameters can be given "bare" or wrapped in double quotes. Quotes are necessary if the given text has spaces

The parameters are passed as literal text replacement, so this call is equivalent to the following, given the scripted effect above:

```
transfer_state = { # Changes ownership of any state within a STATE region (e.g. s:STATE_MONTENEGRO) from GIVER to TAKER countries (e.g. c:TUR). Automatically checks GIVER exists and owns the state.
    if = {
        limit = {
            exists = c:TUR
            exists = root
            root != c:TUR
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

#### Unpaired parameter use

Most examples of parameters in the base game are paired with an effect or trigger, but it also possible to use unpaired parameters, where the entire trigger or effect is passed through when the macro is used. For example:

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

This can be used for example as the following. Note that quote marks are necessary as the passed text contains white space, both spaces and line returns.

```
save_neighbor_with_state = {
    CRITERIA = "NOT = { is_country_type = decentralized }
        average_sol > root.average_sol"
}
```

#### Partial script replacement

Further, because this is literal script text replacement, parameters can even be used to replace part of a script term, so that a scripted effect could read:

```
example_effect = {
    $TYPE$_country = {
        add_treasury = 10
    }
}
```

And valid example calls include

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

As long as the resulting effect is a valid game effect, such parameter use is valid.

## Other macros

Beside scripted effects and triggers, there are a few other macro or macro-like script elements.

### GUI function macros

See also:
Interface modding
,
Data types
GUI function macros are defined in /data_binding/. See /Victoria 3/game/data_binding/gui_macros.txt for examples. These macros can be used in GUI and localization functions. Like scripted effects and triggers, these are direct text replacement and can use parameters.

For example:

```
macro = {
    description = "Add a loc key with a trailing newline if a condition is satisfied"
    definition = "MakeLineIf(Condition, LocKey)"
    replace_with = "ConcatIfNeitherEmpty(AddLocalizationIf(Condition, LocKey), Localize( 'NEWLINE' ))"
}
```

This macro can be called with `[MakeLineIf(boolean, loc key)]`. For example:

```
[MakeLineIf( IsZero(State.GetTradeCapacity), 'NO_WORLD_MARKET_ACCESS_DUE_TO_NO_TRADE_CAPACITY')]
```

This is equivalent to and read by the game as:

```
[ConcatIfNeitherEmpty(AddLocalizationIf( IsZero(State.GetTradeCapacity), 'NO_WORLD_MARKET_ACCESS_DUE_TO_NO_TRADE_CAPACITY'), Localize( 'NEWLINE' )]
```

### Scripted lists

See also:
Scope § Iterators
Scripted lists are defined in /common/scripted_lists/. These are customized [iterator lists](Scope.md) with a built in trigger. They are defined as follows:

```
scripted_list_name = {
    base = base_game_list
    conditions = {
        <triggers>
    }
}
```

A base game list is the same as an iterator/list set without its prefixes. For example, the base game list `country` is used in `any_country`, `every_country`, `ordered_country`, and `random_country`.

Scripted lists filter the base list with given triggers and can be used as `any_scripted_list_name`, `every_scripted_list_name`, `ordered_scripted_list_name`, and `random_scripted_list_name`. For example, with a scripted list:

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

The following example scripts would be equivalent:

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

The latter iterator contains the same limit triggers as they are scripted in the list definition.

### Script values

Main article:
Script value
Script values, defined in /common/script_values/, are similar to macros, particularly static script values. In particular, script values can be used in most places that expect a number or numerical value.

### @ values

Main article:
Script value § @ values
@ values are intra-file macros. They must be defined in the file where they are used, and can be used in place of most number values.

## References

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) Macros • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
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
