---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Pop modding
source: https://vic3.paradoxwikis.com/Pop_modding
pageid: 3816
categories: [Potentially_outdated, 1.9, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。至少部分内容最后验证于 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.9。

[人口](Pops.md)（Pops）有许多属性，但最根本的定义依据是它们的[职业](Profession.md)。

## 职业定义（Profession definition）

职业定义于 /Victoria 3/game/common/pop_types。每个职业通过一个脚本名称和若干特征来定义。

```
example = {	# profession name
	texture = "gfx/interface/icons/pops_icons/example.dds"		# profession icon
	color = { 12 251 123 }				# profession color; unmodified professions all use decimal hsv
	strata = Deprecated ###DO NOT USE IN NEW VERSIONS!###
	start_quality_of_life = 10			# basic quality of life/standard of living
	wage_weight = 3					# multiplier of the pop's wage from building's base wage
	paid_private_wage = yes/no			# whether this pop type receives wages in a non government funded building (default no)
	education_access = 0.25				# bonus amount of education access
	consumption_mult = 1				# optional goods consumption multiplier (default = 1)
	dependent_wage = 0.5				# wage for dependents per year
	unemployment = yes				# can pop be unemployed
	unemployment_wealth = 5				# unemployed pops whose wealth drops to or below this level switches '''to''' this profession
	can_always_hire = yes				# profession does not require qualifications
	subsistence_income = yes			# profession benefits from subsistence income
	ignores_employment_proportionality = yes	# buildings can hire this profession even if unable to hire other professions
	is_slave = yes					# profession is enslaved
    military = yes					# profession is military
    
	# 50% - 100% politically engaged
	political_engagement_base = 0.5				# basic political engagement
	political_engagement_literacy_factor = 1.0		# literacy to political engagement, scaled by literacy
	
	political_engagement_mult = { value = 1	}		# scripted value to escalate dynamic political engagement value
	
	qualifications_growth_desc = "ENGINEERS_QUALIFICATIONS_DESC"		# Qualifications growth desc localization
	qualifications = {}					# Qualifications scripted values list

	portrait_age = { value = 30 }				# Age for portrait
	portrait_pose = { value = 0 }				# Pose for portrait
	portrait_is_female = { always = yes }			# Is portrait female or male
}
```

有两个直接涉及职业的 [defines](Defines.md)：`DEFAULT_POP_TYPE` 和 `SLAVE_POP_TYPE`，在替换原版职业时务必同步更新它们。

## 职业 modifier

另见：
Modifier types § 基于对象的 modifier
每个职业都有若干相关的 [modifier 类型](Modifier types.md)。新增职业时也需要编写这些新的 modifier。

| 常用 modifier |
|---|
| building_employment_[profession]_add building_employment_[profession]_mult country_[profession]_pol_str_mult country_[profession]_voting_power_add state_[profession]_mortality_mult |
| 较少用的 modifier |
| building_group_[group]_[profession]_mortality_mult building_group_[group]_[profession]_standard_of_living_add building_[profession]_shares_add state_[profession]_investment_pool_contribution_add state_[profession]_investment_pool_contribution_mult |

## 人口脚本文档

以下 [effect](Effect.md)、[event target](Event target.md) 和 [trigger](Trigger.md) 可用于 pop scope。

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_pop_wealth | 增加人口的财富 | add_pop_wealth = { wealth_distribution = { script_value } update_loyalties = yes/no } |  |
| change_pop_culture | 按指定百分比将 scope 人口的[文化](Culture modding.md)改为指定文化 | change_pop_culture = { target = cu:spanish value = 0.33 } |  |
| change_pop_religion | 按指定百分比将 scope 人口的[宗教](Religion modding.md)改为指定宗教 | change_pop_religion = { target = rel:catholic value = 0.5 } |  |
| change_poptype | 将人口的类型改为给定类型 |  | pop_type |
| move_partial_pop | 将 scope 人口迁移到指定的[州](State modding.md)（他们会失业） | move_partial_pop = { state = s:STATE_TUSCANY.region_state:TUS } move_partial_pop = { state = s:STATE_TUSCANY.region_state:TUS population = 1000 } move_partial_pop = { state = s:STATE_TUSCANY.region_state:TUS population_ratio = 0.2 } 注意：非常重要！此 effect _可能_ 改变被迁移人口的类型。在以下条件下会发生：1. 如果当前人口类型不能失业，新类型将是默认类型 2. 如果当前人口类型是奴隶类型而目标州不允许奴隶制，新类型将是默认类型 |  |
| move_pop | 将 scope 人口整体迁移到指定的州（他们会失业） | move_pop = s:STATE_TUSCANY.region_state:TUS 注意：非常重要！此 effect _可能_ 改变被迁移人口的类型。在以下条件下会发生：1. 如果当前人口类型不能失业，新类型将是默认类型 2. 如果当前人口类型是奴隶类型而目标州不允许奴隶制，新类型将是默认类型 | state |
| set_pop_literacy | 设置人口劳动力的识字率百分比 | set_pop_literacy = { literacy_rate = { script_value } } |  |
| set_pop_qualifications | 为给定类型设置人口[劳动力]中一定比例的资质 | set_pop_qualifications = { pop_type = {} qualifications = { script_value } } |  |
| set_pop_wealth | 设置人口的财富 | set_pop_wealth = { wealth_distribution = { script_value } update_loyalties = true/false } |  |

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| dependents | 比较 scope 人口的受抚养者数量 | dependents >= 2000 | value |
| food_security | 检查人口是否拥有一定程度的粮食安全 | food_security = value | value |
| has_ongoing_assimilation | 检查 scope 人口是否有正在进行的同化 | has_ongoing_assimilation = yes | boolean |
| has_ongoing_conversion | 检查 scope 人口是否有正在进行的宗教皈依 | has_ongoing_conversion = yes | boolean |
| has_pop_culture | 检查人口是否具有特定文化 | has_pop_culture = culture |  |
| has_pop_religion | 检查人口是否具有特定宗教 | has_pop_religion = religion |  |
| has_social_class | 检查 scope 人口是否属于特定社会阶层 | has_social_class = <key> |  |
| has_state_religion | 检查人口是否信仰国教 |  | boolean |
| is_employed | 检查人口是否就业 |  | boolean |
| is_in_mild_starvation | 检查人口是否处于轻度饥荒 | is_in_mild_starvation = yes | boolean |
| is_in_severe_starvation | 检查人口是否处于严重饥荒 | is_in_severe_starvation = yes | boolean |
| is_in_starvation | 检查人口是否处于饥荒（轻度或严重） | is_in_starvation = yes | boolean |
| is_pop_type | 检查人口是否为指定类型 | is_pop_type = poptype |  |
| literacy_rate | 检查人口、州或国家是否拥有一定程度的识字率 | literacy = value | value |
| pop_acceptance | 将 scope 人口的接受度与某个接受度值进行比较 | pop_acceptance > 50 | value |
| pop_employment_building | 检查人口是否在特定[建筑](Building modding.md)类型中工作 | pop_employment_building = building |  |
| pop_employment_building_group | 检查人口是否在特定建筑类型中工作 | pop_employment_building = building |  |
| pop_has_primary_culture | 检查人口的文化是否为主要文化 | pop_has_primary_culture = bool | boolean |
| pop_loyalist_fraction | 比较人口中忠诚派数量与其总规模的比值 | pop_loyalty_fraction < 0.5 | value |
| pop_neutral_fraction | 比较人口中中立者（非激进派、非忠诚派）数量与其总规模的比值 | pop_neutral_fraction > 0.95 | value |
| pop_radical_fraction | 比较人口中激进派数量与其总规模的比值 | pop_radical_fraction > 0.25 | value |
| quality_of_life | 比较给定人口的生活质量 | quality_of_life > 10 | value |
| standard_of_living | 比较给定人口的生活水平 | standard_of_living > 10 | value |
| strata | 检查 scope 人口的阶层 | strata >= upper/middle/lower | value |
| total_size | 比较 scope 人口的总规模 | total_size >= 3000 | value |
| wealth | 检查人口是否拥有一定数量的财富 | wealth = value | value |
| workforce | 比较 scope 人口的劳动力规模 | workforce >= 1000 | value |

| Event target | 描述 | 转到 scope |
|---|---|---|
| culture | 转到人口或[人物](Character modding.md)的文化 | culture |
| home_country | 转到流亡者的母国 | country |
| owner | 转到对象的所有者国家 | country |
| pop_weight_modifier_scale | 获取人口的权重 modifier 缩放倍率 | value |
| religion | 转到国家或国家定义的主要宗教，或人口的宗教 | religion |
| state | 转到对象所在的州 | state |
| workplace | 转到人口的工作场所 | building |

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | Buildings • Characters • Concepts • [Countries](Country modding.md) • Culture • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • Pops • [Power blocs](Power bloc modding.md) • Religion • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| 地图 | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • States |
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