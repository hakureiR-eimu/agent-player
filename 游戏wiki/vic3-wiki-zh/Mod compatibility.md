---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Mod compatibility
source: https://vic3.paradoxwikis.com/Mod_compatibility
pageid: 7399
categories: [1.13, Modding]
fetched: 2026-10-27
---
本文已针对游戏当前 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

本文详细介绍各种兼容性机制，它们使多个 mod 能够更容易地协同工作，并且由于无需直接依赖本体游戏文件，也使 mod 的维护更加轻松。

## 概述

以下是基本的兼容性机制，适用于大多数游戏文件，必要之处会注明例外情况。

### 文件加载顺序

《维多利亚3》始终按固定顺序加载文件。这对游戏功能本身没有影响，但对 mod 的兼容性影响极大。

所有文件按 [ASCII 顺序](https://en.wikipedia.org/wiki/ASCII#Printable_character_table) 加载，这意味着名为 `00_foo.txt` 的文件会在名为 `01_bar.txt` 的文件之前加载，依此类推，不过这种覆盖行为存在一些 [Exceptions](https://vic3.paradoxwikis.com/Mod_compatibility#Exceptions)。文件是来自本体游戏还是 mod 并不重要。子文件夹中的文件在父文件夹中的文件之后加载，例如位于 events/zz_example.txt 的事件文件会在位于 events/example/00_example.txt 的事件文件之前加载，尽管后者按 ASCII 顺序排列更靠前。

### 文件覆盖

当 mod 中存在某个文件，其文件名和路径[1]与本体游戏、DLC 或其他 mod 中的文件完全相同时，就会发生直接文件覆盖。此时，mod 的文件优先于本体游戏或 DLC 的文件，而播放列表中位置靠下的 mod 的文件优先于位置靠上的 mod 的文件。

优先级最高的文件会被使用，其他文件如同不存在一样。

### 游戏对象加载顺序

已定义的游戏对象——例如建筑、意识形态或法律——按其被定义的顺序加载。

例如，这两个法律文件 `00_test_laws.txt` 和 `01_example_laws.txt`：

```
File: 00_test_laws.txt
  law_foo = {
     law_group = example_group
     <law definition>
  }
  law_bar = {
     law_group = example_group
     <law definition>
  }
-------------------------------
File: 01_example_laws.txt
  law_baz = {
     law_group = example_group
     <law definition>
  }
  law_test = {
     law_group = example_group
     <law definition>
  }
```

它们等价于一个包含全部四条法律的单一文件：

```
law_foo = {
   law_group = example_group
   <law definition>
}
law_bar = {
   law_group = example_group
   <law definition>
}
law_baz = {
   law_group = example_group
   <law definition>
}
law_test = {
   law_group = example_group
   <law definition>
}
```

一般来说，这对游戏玩法几乎没有影响，但会影响对象在相关界面中的显示顺序。

## 注入与替换（Inject and replace）

`INJECT:` 和 `REPLACE:` 关键字允许在不覆盖原始文件的情况下修改已定义的游戏对象。[2] 大多数已定义的游戏对象都需要使用这些关键字，否则就需要直接覆盖文件。使用这些关键字的文件夹列表如下。

| 关键字 | 功能 |
|---|---|
| `INJECT:` | 将注入的脚本追加到现有条目的末尾。如果指定的条目不存在，则报错。 |
| `REPLACE:` | 用新条目替换现有条目。如果指定的条目不存在，则报错 |
| `TRY_INJECT:` | 与 `INJECT:` 相同，但如果指定的条目不存在，不报错 |
| `TRY_REPLACE:` | 与 `REPLACE:` 相同，但如果指定的条目不存在，不报错 |
| `INJECT_OR_CREATE:` | 与 `INJECT:` 相同，但如果指定的条目不存在，则会创建它 |
| `REPLACE_OR_CREATE:` | 与 `REPLACE:` 相同，但如果指定的条目不存在，则会创建它 |

`INJECT:` 和 `REPLACE:` 关键字只能用于文件中的顶层块（top level block）。例如，以下是可行的：

```
INJECT:building_example = {
    production_method_groups = {
        pmg_foo
    }
    <etc.>
}
```

以下是不可行的：

```
building_example = {
    INJECT:production_method_groups = {
        pmg_foo
    }
    <etc.>
}
--------------------------------------------
INJECT:building_example = {
   	INJECT:production_method_groups = {
		pmg_foo
	}
    <etc.>
}
```

重要的是，这意味着某些类型无法轻易注入，因为不可能注入到子块中。

### 行为

`REPLACE:` 关键字会按预期覆盖指定的对象，用新定义替换之前的任何定义。注意，这仍然按照通常的加载顺序发生，因此如果多个 mod 都试图替换同一个对象条目，最后加载的那个“获胜”。类似地，如果替换定义得太“早”，它也无法正确生效。

`INJECT:` 关键字将指定的脚本追加到对象中，而不改变之前的任何定义。如果某类脚本已经定义，则某些类型的脚本无法通过这种方式注入，主要是大多数 trigger 和 effect 块。例如，如果某条法律已经定义了 `is_visible` 块，尝试向其注入 `is_visible` 块就会失败；但如果该法律没有定义 `is_visible` 块，注入新的块就会按预期生效。注意，`INJECT:` 对 scripted effect 和 scripted trigger 不起作用。对这两者使用 `INJECT:` 会导致原有的 effect/trigger 被`REPLACE:` 那样覆盖。

在注入可以多次定义的块时，`INJECT:` 关键字会将其内容追加到对象定义的末尾。例如，假设本体游戏中有如下策略：

```
ai_strategy_default = {
    #... some code
    wargoal_scores = {
        a = {
            # some score calc
        }
        b = {
            # some score calc
        }
        c = {
            # some score calc
        }
    }
    #... some code
}
```

从 mod 中注入以下内容：

```
INJECT:ai_strategy_default = {
    wargoal_scores = {
        d = {
            # some score calc
        }
    }
}
```

实际效果等同于以下内容：

```
ai_strategy_default = {
    #... some code
    wargoal_scores = {
        a = {
            # some score calc
        }
        b = {
            # some score calc
        }
        c = {
            # some score calc
        }
    }
    #... some code
    wargoal_scores = {
        d = {
            # some score calc
        }
    }
}
```

如果注入的块与之前定义的块试图引用相同的元素，可能会导致意外行为。例如，如果注入的块引用了 `a`，它可能会覆盖本体游戏的计算，也可能不被读取。

### 处理顺序

关键字按固定顺序运作，文件名只在同一关键字之间发生冲突时才起作用。

操作顺序为：

`INJECT_OR_CREATE -> REPLACE_OR_CREATE -> TRY_INJECT -> TRY_REPLACE -> INJECT -> REPLACE`

文件名顺序只解决使用相同操作类型的条目之间的冲突。例如，如果两个文件都对同一对象使用 `REPLACE:`，则文件名优先级靠后的那个获胜。然而，如果一个文件使用 `REPLACE_OR_CREATE:`，另一个使用 `REPLACE:`，那么无论文件名优先级如何，`REPLACE:` 条目都会获胜，因为 `REPLACE:` 的处理时间更晚。

在组合注入和替换操作时，这一点很重要。`TRY_INJECT:` 和 `INJECT:` 会在 `REPLACE:` 之前处理，因此注入的更改可能被之后的替换操作覆盖。反之，`REPLACE_OR_CREATE:` 会在注入操作之前处理，因此之后的注入仍然可以作用于由 `REPLACE_OR_CREATE:` 创建或替换的对象。

### 隐式替换

不使用 `INJECT` 和 `REPLACE` 关键字的文件夹通常通过隐式替换（implicit replace）运作。例如，如果文件 `00_foo.txt` 定义了一个纹章：

```
FOO = {
	pattern = "pattern_solid.tga"
	color1 = "red"
	color2 = "red"

	colored_emblem = {
		texture = "ce_bicolor_bottom.dds"
		color1 = "blue"
		color2 = "blue"
	}
}
```

然后文件 `01_bar.txt` 将其重新定义为：

```
FOO = {
	pattern = "pattern_solid.tga"
	color1 = "blue"
	color2 = "blue"

	colored_emblem = {
		texture = "ce_bicolor_bottom.dds"
		color1 = "red"
		color2 = "red"
	}
}
```

则只有后者会被使用。

![Warning](/images/thumb/c/cb/Warning.png/24px-Warning.png) 隐式替换在使用 `INJECT` 和 `REPLACE` 的文件夹中**不起作用**。

## 例外情况

上述规则存在一些例外。

### GUI 类型

另见：
界面 mod 制作
相关文件夹：game/gui/

当 GUI 的 `type` 或 `template`（注意不是 `types`）被加载后，它无法被覆盖。因此，最先加载的那个*获胜*并被使用。除此之外，上述规则仍然适用。GUI `type` 和 `template` 示例：

```
types gate_main_panel_types {
    type gate_main_panel = default_block_window {
        # Some gui stuff
    }
}

template test {
  # Some gui stuff
}
```

**注意：**上面示例中的 `types` 容器不需要唯一，并且完全没有覆盖逻辑。

### 事件

另见：
事件 mod 制作
相关文件夹：game/events/

事件遵循与 GUI 类型相同的逻辑，即最先加载的那个*获胜*。因此，在较早加载的文件中定义的事件会被使用，而不是像其他定义那样采用最后定义的。

特别值得注意的是，子文件夹总是在主 events 文件夹中的文件*之后*加载，这在修改本体游戏事件时可能导致意外行为。

### Defines

另见：
Defines
相关文件夹：`game/common/defines/`

Defines 使用一种独特的替换机制，允许替换单个 define 而无需替换整个 define 类别：

```
NSomeCategory = {
    A_SINGLE_DEFINE = X
}
```

这只会更改指定类别中的指定 defines。

### On actions

另见：
On action
相关文件夹：game/common/on_actions/

On actions 允许追加更多的 `on_actions`、`events` 或 `random_events`，但不允许替换 on action 的 `trigger` 和 `effect` 块，除非替换整个文件。

以下是可行的：

```
# Base game on action
on_monthly_pulse = {
    on_actions = {
        some_custom_on_action
    }
}

# Modded on action
some_custom_on_action = {
    trigger = {
        # Trigger logic
    }
    effect = {
        # Effect logic
    }
}
```

以下会产生错误，并覆盖本体游戏的 `effect`：

```
on_monthly_pulse = {
    effect = {
        # Effect logic
    }
}
```

### 本地化（Localization）

另见：
本地化
相关文件夹：game/localization/

本地化使用一种通过特殊文件夹实现的独特替换机制。

要覆盖单个本地化键（localization key），必须在 [mod_name]/localization/[language]/replace 文件夹中定义。完整文件覆盖仍然有效，但较晚加载的本地化键**不会**覆盖先前定义的键。

### DNA 数据

另见：
人物 mod 制作
相关文件夹：game/common/dna_data/

已定义的人物 DNA 不会互相覆盖，而是会产生重复项。只有文件覆盖才能正确替换人物的 DNA。

### 基因（Genes）

另见：
人物 mod 制作
相关文件夹：game/common/genes/

Genes 在对象的*第二*层级使用 `INJECT:` 关键字，例如：

```
accessory_genes = {
    INJECT:eye_accessory = {
        no_eyes = {
            index = 1
            male = {
                1 = empty
            }
            female = male
            boy = male
            girl = male
        }
    }
}
```

## 文件夹列表

如果你知道任何未记录的差异，请在此列表中添加或删除文件夹
以下文件夹——*且仅有以下文件夹*——支持 `INJECT:` 和 `REPLACE:` 关键字。[3]

- `common/acceptance_statuses`
- `common/achievements`
- `common/ai_strategies`
- `common/alert_groups`
- `common/alert_types`
- `common/amendments`
- `common/battle_conditions`
- `common/building_groups`
- `common/buildings`
- `common/buy_packages`
- `common/character_interactions`
- `common/character_templates`
- `common/character_traits`
- `common/cohesion_levels`
- `common/combat_unit_experience_levels`
- `common/combat_unit_groups`
- `common/combat_unit_types`
- `common/commander_orders`
- `common/commander_ranks`
- `common/company_charter_types`
- `common/company_types`
- `common/country_creation`
- `common/country_definitions`
- `common/country_formation`
- `common/country_ranks`
- `common/country_types`
- `common/culture_graphics`
- `common/cultures`
- `common/decisions`
- `common/decrees`
- `common/diplomatic_actions`
- `common/diplomatic_catalyst_categories`
- `common/diplomatic_catalysts`
- `common/diplomatic_plays`
- `common/discrimination_trait_groups`
- `common/discrimination_traits`
- `common/dna_data`
- `common/dynamic_company_names`
- `common/dynamic_country_map_colors`
- `common/dynamic_country_names`
- `common/dynamic_treaty_names`
- `common/ethnicities`
- `common/flag_definitions`
- `common/game_concepts`
- `common/genes`
- `common/geographic_regions`
- `common/goods`
- `common/government_types`
- `common/harvest_condition_types`
- `common/ideologies`
- `common/institutions`
- `common/interest_group_traits`
- `common/interest_groups`
- `common/journal_entries`
- `common/journal_entry_groups`
- `common/labels`
- `common/law_groups`
- `common/laws`
- `common/legitimacy_levels`
- `common/liberty_desire_levels`
- `common/military_formation_flags`
- `common/mobilization_option_groups`
- `common/mobilization_options`
- `common/modifier_type_definitions`
- `common/objective_subgoal_categories`
- `common/objective_subgoals`
- `common/objectives`
- `common/parties`
- `common/political_lobbies`
- `common/political_lobby_appeasement (factor)`
- `common/political_lobby_appeasement (reason)`
- `common/political_movement_categories`
- `common/political_movement_pop_support`
- `common/political_movements`
- `common/pop_needs`
- `common/pop_types`
- `common/power_bloc_coa_pieces`
- `common/power_bloc_identities`
- `common/power_bloc_map_textures`
- `common/power_bloc_names`
- `common/power_bloc_principle_groups`
- `common/power_bloc_principles`
- `common/prestige_goods`
- `common/production_method_groups`
- `common/production_methods`
- `common/proposal_types`
- `common/religions`
- `common/script_values (REPLACE only)`
- `common/scripted_buttons`
- `common/scripted_effects (REPLACE only)`
- `common/scripted_guis`
- `common/scripted_lists`
- `common/scripted_modifiers`
- `common/scripted_progress_bars`
- `common/scripted_rules (REPLACE only)`
- `common/scripted_triggers (REPLACE only)`
- `common/social_classes`
- `common/social_hierarchies`
- `common/state_traits`
- `common/static_modifiers`
- `common/strategic_regions`
- `common/subject_types`
- `common/technology`
- `common/terrain`
- `common/terrain_manipulators`
- `common/themes`
- `common/treaty_articles`
- `common/trigger_localization`
- `common/tutorial_lesson_chains`
- `common/tutorial_lessons`
- `common/war_goal_types`
- `gfx/map/army_dioramas`
- `gfx/map/city_data/city_building_vfx`
- `gfx/map/city_data/city_types`
- `gfx/map/fleet_dioramas`
- `gfx/map/fleet_entities`
- `gfx/map/front_entities`
- `gfx/portraits/accessories`
- `gfx/portraits/portrait_modifiers`
- `gui_animations`
- `modifier_icons`
- `music`
- `notifications`
- `sound/persistent_objects`

其他文件夹**不支持** `INJECT:` 和 `REPLACE:` 关键字，只能使用直接文件覆盖或隐式替换

## 参考资料

1. ↑ 相对于 `game/` 和 `[mod_name]/` 文件夹
2. ↑ 改编自 Bahmut 的 [Modding Digest](https://github.com/Victoria-3-Modding-Co-op/Modding-Digests/blob/main/1.12.0/inject_types.md)。
3. ↑ 此列表由 mod 社区自家的“内线人员”提供：**Doodlez**

Mod 制作
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|
| 脚本类型 | [建筑](Building modding.md) • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [可自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图像](Event images.md) • [图像资源](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [音效](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [模组](Mod.md) • 模组兼容性 • [模组结构](Mod structure.md) • [脚本测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [模组翻译](Mod translation.md) • [新国家模组制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州模组制作指南](State modding guide.md) |
|---|---|