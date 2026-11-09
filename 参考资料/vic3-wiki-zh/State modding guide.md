---
translated: 2026-10-27
translator: machine (glm-5.3)
title: State modding guide
source: https://vic3.paradoxwikis.com/State_modding_guide
pageid: 5031
categories: [Potentially_outdated, Unknown_version, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。至少有一部分内容最后是针对 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 未知 验证的。

另见：
State modding
，
Map modding#State Modding

## 创建新的州区域

本指南介绍如何在不编辑省份地图的情况下创建新的州区域。

开始前的重要提示：

- 建议使用比普通记事本更好的文本编辑器进行编辑。我推荐 Notepad++（本指南将使用它）、Visual Studio Code 和 Sublime。
- 游戏中所有 .txt 文件必须采用 `UTF8-BOM` 编码，否则可能无法正常工作。如果你不知道如何设置编码，只需复制一个现有文件并修改其内容即可。
- 文本文件中 `#` 之后的所有内容都会被“注释掉”，即游戏会忽略 # 之后的内容。
- 本指南是在一个已搭建并正常运行 mod 的前提下编写的，请确保先完成这一重要步骤。

### 获取省份 ID

首先，你需要知道将从旧州划出、并成为新州一部分的省份的 ID。一种方法是在 debug mode 下进入游戏，将鼠标悬停在地块上，你会看到“省份 ID”。把它们全部记录下来。或者，打开 /Victoria 3/game/map_data/provinces.png 并记下该图像中各省份的十六进制颜色代码。

在本指南中，我们将取出新加坡省份，并将其设为独立的州。新加坡的省份 ID 是 `xC00130`。你也可以记录多个省份 ID。

### 定义州区域

在这一部分，我们将定义新建新加坡州的地图数据。你的 mod 文件应放在：

/<mod>/map_data/state_regions/<filename>.txt

你可以在以下位置找到对应的文件：

/Victoria 3/game/map_data/state_regions/<anyfile>.txt

从那里复制相关州的脚本，粘贴到新的 mod 文件中。从旧州中移除这些省份并将其移入新州，包括枢纽（城市、港口、农场等）。此外，在新州中，这些枢纽只能使用所包含的省份 ID。

每个州区域都需要唯一的脚本名称和州 ID。这里我们使用 `STATE_SINGAPORE` 作为脚本名称，使用 `800` 作为州 ID。

在我们的新加坡示例中，脚本如下所示：

```
STATE_MALAYA = {
    id = 540
    subsistence_building = "building_subsistence_rice_paddies"
    provinces = { "x0080B0" "x08673B" "x23578B" "x374A68" "x660411" "x66170B" "x6CFA94" "x76546D" "x78EF92" "x8080B0" "x80C0B0" "x8E3305" "xAA2287" "xAF3737" "xB6B53D" "xC84C4C" "xCAB9F2" "xCF3E8D" "xD8E596" "xE87C53" "xF9F87A" "xFCBAFC" }
    city = "x8E3305"
    port = "x8E3305"
    farm = "x76546D"
    mine = "x08673B"
    wood = "xCAB9F2"
    arable_land = 35
    arable_resources = { "bg_rice_farms" "bg_livestock_ranches" "bg_coffee_plantations" "bg_tea_plantations" "bg_sugar_plantations" "bg_banana_plantations" }
    capped_resources = {
        bg_coal_mining = 32
        bg_lead_mining = 24
        bg_logging = 17
        bg_fishing = 10
    }
    resource = {
        type = "bg_rubber"
        undiscovered_amount = 40
    }
    naval_exit_id = 3052
}
STATE_SINGAPORE = {
    id = 800
    subsistence_building = "building_subsistence_rice_paddies"
    provinces = { "xC00130" }
    city = "xC00130"
    port = "xC00130"
    farm = "xC00130"
    mine = "xC00130"
    wood = "xC00130"
    arable_land = 4
    arable_resources = { "bg_rice_farms" "bg_livestock_ranches" "bg_coffee_plantations" "bg_tea_plantations" "bg_sugar_plantations" "bg_banana_plantations" }
    capped_resources = {
        bg_logging = 1
        bg_fishing = 12
    }
    naval_exit_id = 3052
}
```

#### 战略区域

要将新州纳入某个战略区域，你需要在以下路径定义 mod 文件：

/<mod>/common/strategic_regions/<filename>.txt

对应的文件在这里：

/Victoria 3/game/common/strategic_regions/<any file>.txt

接下来，你需要找到目标区域的脚本名称，并在新文件中重新定义它。在我们的新加坡示例中，该区域是印度支那。因此，新文件将如下所示：

```
region_indochina = {
	graphical_culture = "asian"
	capital_province = x5C3070
	map_color = { 0.9 0.1 0.1 }
	states = { STATE_CAMBODIA STATE_MEKONG STATE_TONKIN STATE_ANNAM STATE_LAOS STATE_CHIANG_MAI STATE_NAKHON_RATCHASIMA STATE_MALAYA STATE_TENASSERIM STATE_BANGKOK STATE_KACHIN STATE_SHAN_STATES STATE_BURMA STATE_PEGU STATE_SINGAPORE}
}
```

注意我们在其中添加了 `STATE_SINGAPORE`。

#### 本地化

要为州区域赋予游戏内名称，请在以下路径创建文件。

<mod>/localization/english/map/<filename>_l_english.yml

记住，在文件名末尾加上"`_l_english`"。是小写的“L”，而不是大写的“i”或数字 1。

该 mod 文件将如下所示。

```
l_english:
 STATE_SINGAPORE:0 "Singapore"
```

### 地图元素

主条目：
Map_modding#State_Modding
有若干地图元素，是新州区域正常运行所必需的。

### 州历史

要定义新州的历史，请参阅以下指南。

## 覆盖现有州

另见：
Mod files load order
下面的示例针对新国家，但这同样适用于现有国家。[1] 本指南只提及相关的历史文件。所有其他历史文件正常工作，不需要任何特殊处理。这整个流程是必需的，这样游戏的人口和建筑计算才正确。如果你在 /<mod>/common/history/states 中吞并整个州，建筑和人口将不会被完全整合，建筑在游戏开局时将没有工人。

这些文件都不应覆盖原版游戏文件。

### 定义州

/<mod>/common/history/states

我们做的第一件事是创建一个新文件。在这个文件中，我们添加除每个已拥有该州的国家各留一个省份之外的所有省份。这会创建一个完全空白的新分裂州，并且不会吞并任何现有州。

下面是一个我将危地马拉交给 `GOK` 的示例：

```
STATES = {
    s:STATE_GUATEMALA = {
        create_state = {
            country = c:GOK
            owned_provinces = {
                x02073E x7D333F x464F6A x0F5049
                xBD8628 xA9090A x78C465 xD9BEFE
                xD030C0 x42124E xB2E11E x50B040
                x2D4EB6 x5449D0 x6D71DA x702CD9
                x65C19A x30E01C x50B0C0 xC67219
                xD176F3 xFA4B41 x011E0F
            }
        }
    }
}
```

如果你是在创建新的州区域或分裂州，而不是覆盖一个州，则只需添加相关省份。

### 添加人口

/<mod>/common/history/pops

添加人口时，我们需要从原先拥有该州的国家中移除现有人口，这样之后正式吞并时我们就不会得到他们的人口。移除并重新创建可以使人口工作场所得到正确整合。

**注意**：即使你打算保留相同的人口，也需要执行此操作。在这种情况下，你需要从原版游戏中复制人口。

在这个示例中，我们首先消灭危地马拉的全部人口，然后添加我们自己的人口。由于这是一个分裂州，我们需要对 UCA 和 GBR 执行此操作：

```
POPS = {
    s:STATE_GUATEMALA = {
        region_state:UCA = {
            kill_population_percent_in_state = {
                percent = 1 # 100%
            }
        }
        region_state:GBR = {
            kill_population_percent_in_state = {
                percent = 1 # 100%
            }
        }
        region_state:GOK = {
            create_pop = {
                culture = orcish
                size = 200000
            }
            create_pop = {
                pop_type = slaves
                culture = central_american
                size = 164404
            }
            create_pop = {
                pop_type = slaves
                culture = mayan
                size = 312000
            }
        }
    }
}
```

如果你是在创建新的州区域或分裂州，而不是覆盖一个州，则只有在你重新定义原州中人口数量时才需要消灭人口。

### 添加建筑

/<mod>/common/history/buildings

添加建筑时，我们需要从原先拥有该州的国家中移除现有建筑，这样之后正式吞并时我们就不会得到没有劳动力的建筑。移除并重新创建可以使人口工作场所得到正确整合。要查找需要移除哪些建筑，请参阅原版游戏的历史文件。

**注意**：即使你打算保留相同的建筑，也需要执行此操作。在这种情况下，你需要从原版游戏中复制建筑。

在这个示例中，我们首先移除危地马拉的所有建筑，然后添加我们自己的建筑。由于这是一个分裂州，我们需要对 UCA 和 GBR 执行此操作：

```
BUILDINGS = {
    s:STATE_GUATEMALA = {
        region_state:UCA = {
            # Clean up base game buildings
            remove_building = building_government_administration
            remove_building = building_maize_farm
            remove_building = building_livestock_ranch
            remove_building = building_barracks
        }
        region_state:GBR = {
            # Clean up base game buildings
            remove_building = building_port
        }
        region_state:GOK = {
            create_building = {
                building = "building_port"
                add_ownership = {
                    country = {
                        country = "c:GOK"
                        levels = 2
                    }
                }
                reserves = 1
                activate_production_methods = { "pm_anchorage" }
            }
            # More buildings could be here
        }
    }
}
```

如果你是在创建新的州区域或分裂州，而不是覆盖一个州，则只有在你重新定义原州中建筑数量时才需要移除建筑。

### 正式吞并州

/<mod>/common/on_actions

最后，我们需要通过夺取最后的省份来吞并现在已空置的州。这需要通过 `on_game_started` [on action](https://vic3.paradoxwikis.com/On_actions) 来完成。请务必创建一个新的 on action 文件并使用自定义 on action，以保证兼容性。

下面是我们为危地马拉夺取最后两个省份（GBR 和 UCA）的示例：

```
on_game_started = {
    on_actions = {
        mod_history_setup_on_action
    }
}

mod_history_setup_on_action = {
    effect = {
        s:STATE_GUATEMALA = {
            set_owner_of_provinces = {
                country = c:GOK
                provinces = {
                    xDEC8D3
                    xD0B040
                }
            }
        }
    }
}
```

当然，如果不覆盖原州，请跳过此步骤。

## 参考

1. ↑ 改编自 [Victoria 3 Mod Co-op Discord](https://discord.com/invite/uUbuMTQjA7) 上 [Bahmut | Chris 的指南](https://discord.com/channels/827163966551621662/1346877562143510622)

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

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • State modding guide |
|---|---|