---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Culture modding
source: https://vic3.paradoxwikis.com/Culture_modding
pageid: 6775
categories: [Potentially_outdated, 1.11, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。至少有部分内容最后核实的版本为 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.11。

参见：
宗教模组制作（Religion modding）
《维多利亚3》中的[文化](Culture.md)（Culture）表示人口与国家的抽象化族群属性和传统。

## 文化定义（Culture definition）

文化定义于 /Victoria 3/game/common/cultures/ 中。定义内容包括脚本名称、颜色、宗教、特质、姓名列表、族群以及图像。例如：

```
mazanderani ={	#Script name can be anything, but best to match desired in-game localization unless it overlaps some other script term
    color= rgb{ 158 68 137 }	#either rgb (255) or hsv (decimal)

    religion = shiite	#Any defined religion; default religion for pops and countries of this culture
    heritage = heritage_iranian
    language = language_tabari
    traditions = { tradition_persianate }

    male_common_first_names={	#space or line-separated list of names, each is a localization key, and so must have no spaces
        [names]
    }
    female_common_first_names = {
	[names]
    }
    common_last_names={
	[names]
    }

    ethnicities = {	#weighted list of ethnicities, affects appearance of pop and character models
	1 = arab
    }
    graphics = arabic	#Graphical culture used for pops and countries with this culture
}
```

脚本名称既用作本地化键，也用于 trigger 和 effect。

颜色可以采用 RGB 或 HSV 格式：RGB 使用 0-255 的数值，而 HSV 使用小数值。

传承（heritage）是单个传承特质，语言（language）是单个语言特质，传统（tradition）则可以是任意数量的传统特质。

姓名列表用于生成该文化的人物，应至少包含 `male_common_first_names`、`female_common_first_names` 和 `common_last_names`。额外的列表可以用 `noble` 和 `regal` 替代 `common`，例如 `male_noble_first_names` 或 `regal_last_names`。

族群是在 /Victoria 3/game/common/ethnicities/ 中定义的带权重的族群列表。未经修改的文化通常只有一个族群，少数有两个或更多。

图像定义于 /Victoria 3/game/common/culture_graphics/ 中，只是一个简单的定义块，如 `arabic = {}`。它在文化以及各种图像文件中被引用。

每种文化还可以有一个 `obsessions` 块，列出该文化开局即痴迷的一种或多种消耗品（goods）。不要将超过 `MAX_NUM_OBSESSIONS` 数量的商品定义为开局痴迷。

类似地，每种文化还可以有一个 `taboos` 块，列出该文化视为禁忌的一种或多种消耗品。禁忌数量是否有上限尚不清楚。文化禁忌会覆盖宗教禁忌。

## 歧视特质（Discrimination traits）

文化和[宗教](Religion modding.md)都使用定义于 /Victoria 3/game/common/discrimination_traits/ 的歧视特质（discrimination trait）。每个特质由唯一的脚本名称和定义块定义。每个特质有一个 `type`，可以为 `heritage`、`language` 或 `tradition`。脚本名称同时也是本地化键。

例如：

```
language_germanophone = { # a language trait
	type = language
	trait_group = language_group_germanic
}

heritage_abyssinian = { # a heritage trait
	type = heritage
	trait_group = heritage_group_african
}

tradition_rumelian = {
	type = tradition
}
```

这些前缀仅用于便于引用和分类。

除了在文化和宗教定义中的用途之外，文化特质与宗教特质没有任何区别。宗教只使用传承特质，不使用语言或传统特质。

传承特质和语言特质还有一个特质组（trait group），代表一组相似的特质。

### 特质组（Trait groups）

歧视特质组定义于 /Victoria 3/game/common/discrimination_trait_groups/。特质组与特质完全相同，只是不能是 tradition 类型，也没有更进一步的组。

例如：

```
language_group_germanic = { # a language trait group
	type = language
}

heritage_group_african = { # a heritage trait group
	type = heritage
}
```

## 修正定义（Modifier Definitions）

参见：
修正类型
，
修正模组制作
创建文化时，你还必须创建三组[静态修正](Modifier modding.md)（static modifier）：`(culture name)_standard_of_living_modifier_positive` 与 `(culture name)_standard_of_living_modifier_negative`、`(culture name)_cultural_acceptance_modifier_positive` 与 `(culture name)_cultural_acceptance_modifier_negative`，以及 `(culture name)_fervor_target_modifier_positive` 与 `(culture name)_fervor_target_modifier_negative`。你还必须创建名为 `state_(culture name)_standard_of_living_add` 的[修正类型](Modifier types.md)（modifier type，供 [effect](Effect.md)（游戏内效果脚本）add_culture_standard_of_living_modifier 使用）、`country_(culture name)_cultural_acceptance_add`（与 add_culture_acceptance_modifier 配合使用），以及 `country_fervor_target_(culture name)_add`（与 add_fervor_target_modifier 配合使用）。原版文化这些定义的示例可见于 /Victoria 3/game/common/static_modifiers/07_culture_standard_of_living.txt、/Victoria 3/game/common/static_modifiers/10_culture_cultural_acceptance_modifiers.txt、/Victoria 3/game/common/static_modifiers/11_culture_fervor_target_modifiers.txt、/Victoria 3/game/common/modifier_type_definitions/10_country_cultural_acceptance_culture_modifier_types.txt 以及 /Victoria 3/game/common/modifier_type_definitions/99_todo_sort_into_other_files.txt

例如：

```
#in static_modifiers
scottish_standard_of_living_modifier_positive = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_positive.dds"
	state_scottish_standard_of_living_add = 1
}

scottish_standard_of_living_modifier_negative = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_negative.dds"
	state_scottish_standard_of_living_add = 1
}

scottish_cultural_acceptance_modifier_positive = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_positive.dds"
	country_scottish_cultural_acceptance_add = 1
}

scottish_cultural_acceptance_modifier_negative = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_negative.dds"
	country_scottish_cultural_acceptance_add = 1
}

scottish_fervor_target_modifier_positive = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_positive.dds"
	country_fervor_target_scottish_add = 1
}

scottish_fervor_target_modifier_negative = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_negative.dds"
	country_fervor_target_scottish_add = 1
}

#############################
#in modifier_types
state_scottish_standard_of_living_add = {
	decimals=1
	color=good
	game_data = {
		ai_value=0
	}
}

country_scottish_cultural_acceptance_add = {
	decimals=1
	color=good
	game_data = {
		ai_value=0
	}
}

country_fervor_target_scottish_add={
	decimals=1
	color=good
	game_data={
		ai_value=0
	}
}
```

## 原版文化（Base game cultures）

参见：
文化列表
大多数原版文化的脚本名称与英文本地化名称相同，但全部为小写，空格或连字符替换为下划线，并把所有非 ASCII 字符替换为最接近的等价字符。

以下文化不符合这一模式，使用了不直观的脚本名称。有些是轻微改写，有些则使用了该文化的别名。

| 文化 | 脚本名称 |
|---|---|
| 法兰克-普罗旺斯 | francoprovencal |
| 英格兰 | british |
| 塞法迪犹太 | sephardic |
| 阿马齐格 | berber |
| 哈萨克 | kazak |
| 吉尔吉斯 | kirgiz |
| 奥里亚 | oriya |
| 旁遮普 | panjabi |
| 泰卢固 | telegu |
| 澳洲原住民 | aborigine |
| 奥'odham | oodham |
| 河流班图 | fluvian_bantu |
| 奇特拉尔 | kho |
| 塞凯伊 | szekely |

## 文化脚本文档（Culture script documentation）

以下 [effect](Effect.md)、[event target](Event target.md) 和 [trigger](Trigger.md) 可在文化 scope 中使用。

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_cultural_community_in_state | 为目标州中的 scope 文化添加一个文化社区。 | cu:zulu = { add_cultural_community_in_state = scope:some_state } | state |
| add_cultural_obsession | 为 scope 中的文化添加新的痴迷 | add_cultural_obsession = <goods> |  |
| add_cultural_taboo | 为 scope 中的文化添加新的禁忌 | add_cultural_taboo = <goods> |  |
| add_fervor | 为 scope 中的文化添加狂热 | add_fervor = 2.6 |  |
| add_tradition_trait | 为 scope 中的文化添加新的传统特质 | add_tradition_trait = <tradition_trait> |  |
| every_scope_homeland_state | 遍历所有作为 scope 文化家园的州，或 scope 国家任一主流文化家园的州 | every_scope_homeland_state = { limit = { <triggers> } #optional <effects> } | state |
| every_scope_pop | 遍历以下范围中的所有人口：国家、州、利益集团、文化 | every_scope_pop = { limit = { <triggers> } #optional <effects> } | pop |
| ordered_scope_homeland_state | 遍历所有作为 scope 文化家园的州，或 scope 国家任一主流文化家园的州 | ordered_scope_homeland_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_scope_pop | 遍历以下范围中的所有人口：国家、州、利益集团、文化 | ordered_scope_pop = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | pop |
| random_scope_homeland_state | 遍历所有作为 scope 文化家园的州，或 scope 国家任一主流文化家园的州 | random_scope_homeland_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| random_scope_pop | 遍历以下范围中的所有人口：国家、州、利益集团、文化 | random_scope_pop = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | pop |
| remove_cultural_obsession | 移除 scope 中文化的痴迷 | remove_cultural_obsession = <goods> |  |
| remove_cultural_taboo | 移除 scope 中文化的禁忌 | remove_cultural_taboo = <goods> |  |
| remove_tradition_trait | 移除 scope 中文化的现有传统特质 | remove_tradition_trait = <tradition_trait> |  |
| set_fervor | 设置 scope 中文化的狂热 | set_fervor = 3.0 |  |
| set_name_format | 设置 scope 中文化的姓名格式 | set_name_format = first_last/last_first |  |

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| any_scope_pop | 遍历以下范围中的所有人口：国家、州、利益集团、文化 | any_scope_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | pop |
| culture_can_have_mass_migration_to_country | 检查 scope 文化是否可以大规模迁移到目标国家 | can_have_mass_migration_to_country = c:country | country |
| culture_current_fervor | 比较给定文化的当前狂热 | culture_current_fervor > 0.2 | value |
| culture_has_community_in_state | 检查 scope 文化是否在某州拥有文化社区。 | culture_has_community_in_state = <state> |  |
| culture_has_national_awakening | 检查 scope 文化是否有正在进行的民族觉醒 | culture_has_national_awakening = yes / no | boolean |
| culture_national_awakening_occurred | 检查 scope 文化是否曾启动过民族觉醒 | culture_national_awakening_occurred = yes / no | boolean |
| culture_secession_progress | 检查文化在某国家中的分裂进度百分比。若无正在进行的分裂运动则为 0。 | culture_secession_progress = { target = scope:example_country value > 0.5 } | value |
| culture_target_fervor | 比较给定文化的目标狂热 | culture_target_fervor > 0.2 | value |
| has_cultural_obsession | 检查文化是否痴迷于某种商品 | has_cultural_obsession = <goods key> |  |
| has_culture_graphics | 检查文化是否使用某种 culture_graphics | has_culture_graphics = <culture graphics key> |  |
| has_discrimination_trait | 检查 scope 文化或宗教是否具有给定的歧视特质 | has_trait = trait |  |
| has_homeland | 检查 scope 文化在目标州或州区域是否拥有家园 | has_homeland = state/state region |  |
| is_primary_culture_of | 检查文化是否为某国的任一主流文化 | is_primary_culture_of = <country> | country |
| shares_heritage_trait_group_with_any_primary_culture | 检查文化是否与某国任一主流文化共享标记为‘heritage’的特质组 | shares_heritage_trait_group_with_any_primary_culture = <country> | country |
| shares_heritage_trait_group_with_culture | 检查文化是否与另一文化共享标记为‘heritage’的特质组 | shares_heritage_trait_group_with_culture = <culture> | culture |
| shares_heritage_trait_group_with_state_religion | 检查该宗教是否与某国的国教共享任一传承特质组 | shares_heritage_trait_group_with_state_religion = <country> | country |
| shares_heritage_trait_with_any_primary_culture | 检查文化是否与某国任一主流文化共享标记为‘heritage’的特质 | shares_heritage_trait_with_any_primary_culture = <country> | country |
| shares_heritage_trait_with_culture | 检查文化是否与另一文化共享标记为‘heritage’的特质 | shares_heritage_trait_with_culture = <culture> | culture |
| shares_language_trait_group_with_any_primary_culture | 检查文化是否与某国任一主流文化共享标记为‘language’的特质组 | shares_language_trait_group_with_any_primary_culture = <country> | country |
| shares_language_trait_group_with_culture | 检查文化是否与另一文化共享标记为‘language’的特质组 | shares_language_trait_group_with_culture = <culture> | culture |
| shares_language_trait_with_any_primary_culture | 检查文化是否与某国任一主流文化共享标记为‘language’的特质 | shares_language_trait_with_any_primary_culture = <country> | country |
| shares_language_trait_with_culture | 检查文化是否与另一文化共享标记为‘language’的特质 | shares_language_trait_with_culture = <culture> | culture |
| shares_tradition_trait_with_any_primary_culture | 检查文化是否与某国任一主流文化共享标记为‘tradition’的特质 | shares_language_trait_with_any_primary_culture = <country> | country |
| shares_tradition_trait_with_culture | 检查文化是否与另一文化共享标记为‘tradition’的特质 | shares_language_trait_with_culture = <culture> | culture |

| Event target | 描述 | 转至 scope |
|---|---|---|
| national_awakening_state_region | 从文化 scope 链接到该文化正在发生民族觉醒的州区域 | state_region |

### 文化 GUI 脚本（Culture GUI script）

主条目：
GUI 脚本
| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessHomelands |  | Unknown | Category: const |
| AccessReligion |  | Religion | Category: const |
| AccessSameHeritageCultures |  | Unknown | Category: const |
| AccessSelf |  | Culture | Category: const |
| CalcAvgSoL |  | CFixedPoint |  |
| CalcAvgSoLForMiddle |  | CFixedPoint |  |
| CalcAvgSoLForPoor |  | CFixedPoint |  |
| CalcAvgSoLForRich |  | CFixedPoint |  |
| CalcTurmoilInCountry | Unknown | CFixedPoint |  |
| GetAcceptanceDescIn | Country | CString | Category: nonconst |
| GetAcceptanceIn | Country | int32 | Category: nonconst |
| GetAllAcceptanceStatusSegments | Country | Unknown | Category: nonconst |
| GetCasualtiesFromWars |  | int64 | Category: nonconst |
| GetColor |  | CVector4f | Category: nonconst |
| GetCulturalTraitsDesc |  | CString | Category: nonconst |
| GetCurrentFervor |  | CFixedPoint | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetDependents | Country | int64 | Category: nonconst |
| GetDependentsAsPercentage | Country | CFixedPoint | Category: nonconst |
| GetHeritageTrait |  | DiscriminationTrait | Category: nonconst |
| GetID |  | uint32 | Category: nonconst |
| GetLanguageTrait |  | DiscriminationTrait | Category: nonconst |
| GetMigrationTargetsDesc |  | CString | Category: nonconst |
| GetMonthlyChangeFervor |  | CFixedPoint | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetObsessionsDesc |  | CString | Category: nonconst |
| GetPolStr | Country | int64 | Category: nonconst |
| GetPolStrAsFloat | Unknown | float | Category: nonconst |
| GetPolStrAsPercentage | Country | CFixedPoint | Category: nonconst |
| GetPopulation | Country | int64 | Category: nonconst |
| GetPopulationAsFloat | Unknown | float | Category: nonconst |
| GetPopulationAsPercentage | Country | CFixedPoint | Category: nonconst |
| GetPopulationChange | Country | int64 | Category: nonconst |
| GetPopulationChangeDesc | Country | CString | Category: nonconst |
| GetPopulationInCountryAsPercentage | Unknown | CFixedPoint | Category: nonconst |
| GetReligion |  | Religion | Category: nonconst |
| GetReligionsDesc |  | CString | Category: nonconst |
| GetStateDependents | State | int64 | Category: nonconst |
| GetStateDependentsAsPercentage | State | CFixedPoint | Category: nonconst |
| GetStatePolStr | State | int64 | Category: nonconst |
| GetStatePolStrAsFloat | Unknown | float | Category: nonconst |
| GetStatePolStrAsPercentage | State | CFixedPoint | Category: nonconst |
| GetStatePopulation | State | int64 | Category: nonconst |
| GetStatePopulationAsFloat | Unknown | float | Category: nonconst |
| GetStatePopulationAsPercentage | State | CFixedPoint | Category: nonconst |
| GetStateWorkforce | State | int64 | Category: nonconst |
| GetStateWorkforceAsPercentage | State | CFixedPoint | Category: nonconst |
| GetTaboosDesc |  | CString | Category: nonconst |
| GetTargetFervor |  | CFixedPoint | Category: nonconst |
| GetTargetFervorBreakdown |  | CString | Category: nonconst |
| GetTargetFervorFromCountryModifiers |  | CFixedPoint | Category: nonconst |
| GetTargetFervorFromCountryModifiersBreakdown |  | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetTraditionTraits |  | Unknown | Category: nonconst |
| GetTurmoil |  | CFixedPoint | Category: nonconst |
| GetWorkforce | Country | int64 | Category: nonconst |
| GetWorkforceAsPercentage | Country | CFixedPoint | Category: nonconst |
| HasNationalAwakening |  | bool |  |
| HasSecessionMovement | Country | bool |  |
| IsPrimaryCultureIn | Country | bool |  |
| IsPrimaryCultureInYesNo | Unknown | CString |  |
| IsValid |  | bool |  |
| MakeScope |  | Scope |  |
| Self |  | Culture |  |
| Function（函数） | Arguments（参数） | Output（输出） | Description（描述） |
|---|---|---|---|
| AccessSelf |  | CulturalCommunity | 类别：const |
| GetCulture |  | Culture | 类别：nonconst |
| GetCustom | CustomLocalization | CString | 类别：nonconst |
| GetID |  | uint32 | 类别：nonconst |
| GetLocalAcceptanceDifference |  | CFixedPoint | 类别：nonconst |
| GetLocalAcceptanceDifferenceDesc |  | CString | 类别：nonconst |
| GetName |  | CString | 类别：nonconst |
| GetState |  | State | 类别：nonconst |
| GetTooltipTag |  | CString | 类别：nonconst |
| IsValid |  | bool |  |
| MakeScope |  | Scope |  |
| Self |  | CulturalCommunity |  |

| Promote | Arguments（参数） | Output（输出） | Description（描述） |
|---|---|---|---|
| AccessReligion |  | Religion | 类别：const |
| GetHeritageTrait |  | DiscriminationTrait | 类别：nonconst |
| GetLanguageTrait |  | DiscriminationTrait | 类别：nonconst |
| GetReligion |  | Religion | 类别：nonconst |
| GetSampleGlobalLowerStrataPop |  | Pop | 类别：nonconst |
| GetSampleGlobalMiddleStrataPop |  | Pop | 类别：nonconst |
| GetSampleGlobalUpperStrataPop |  | Pop | 类别：nonconst |
| MakeScope |  | Scope |  |

| Promote | Arguments（参数） | Output（输出） | Description（描述） |
|---|---|---|---|
| GetCulture |  | Culture | 类别：nonconst |
| GetState |  | State | 类别：nonconst |
| MakeScope |  | Scope |  |

## 参考

Mod 制作（Modding）
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • Culture • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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