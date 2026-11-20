---
translated: 2026-10-27
translator: machine (glm-5.3)
title: AI modding
source: https://vic3.paradoxwikis.com/AI_modding
pageid: 7816
categories: [Potentially_outdated, 1.9, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。至少部分内容最后验证于 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.9。

AI 模组制作（AI modding）涉及通过各种文件来改变 AI 的行为。

## AI defines

主条目：
AI defines
AI defines 通过为许多机制设置静态数值来控制 AI 的大部分行为。

## AI 策略

AI 策略决定了 AI 在游戏中的大部分行为方式。它们位于 `common/ai_strategies/` 中。AI 策略会周期性地重新选择；新策略基于所有有效策略的权重，按加权随机方式选出。

AI 策略有三种类型：行政、外交和政治。外交类型中还有一个针对附属国的子集，定义在另一个文件中。

每个国家在同一种策略类型下只能拥有一个策略。

### 基础块

以下是 AI 策略内部的各个块。“默认值”在此处指默认策略（即 `00_default_strategy`）中的取值，“在其他策略中使用”描述了如果你在任何策略中使用它会发生什么。

| 块 | 默认值 | 在其他策略中使用 | 描述 |
|---|---|---|---|
| `icon` | `gfx/interface/icons/ai_strategy_icons/placate_population.dds` | override | 图标 |
| `will_form_power_bloc` |  | 如果此 trigger 对任意一个策略判定为真，该国将组建强权集团。空 trigger 在此情况下视为假 |  |
| `desired_tax_level` | `medium` | 这些是 AI 会尽量保持的税收等级，但在紧急情况下可以超过最大等级 |  |
| `max_tax_level` | `high` |  |  |
| `min_tax_level` | `low` |  |  |
| `ideological_opinion_effect_mult` | `1.0` | AI 的外交接受度等受政府意识形态差异影响的程度 |  |
| `revolution_aversion` | `5`（奥斯曼在“欧洲病夫”期间和七月王朝有例外） | AI 每天放弃制定会导致内战的法律的概率（1 点厌恶度约相当于 25%） |  |
| `min_law_chance_to_pass` | `50` | AI 制定法律所需的基础概率 |  |
| `max_progressiveness` | `25` | AI 制定法律时会考虑的最大进步度 |  |
| `max_regressiveness` | `25` | AI 制定法律时会考虑的最大退步度 |  |
| `colonial_interest_ratio` | `0.0`-`0.3`（取决于海军规模） | AI 应将多少利益投向有未认可政权和松散政权的区域 |  |
| `change_law_chance` | `1` | additive | AI 每次更新时愿意开始修改法律的概率（1 = 1%） |
| `pro_interest_groups` |  | AI 会试图让哪些利益集团上台/避免其上台 |  |
| `anti_interest_groups` |  |  |  |
| `pro_movements` | AI 会试图支持/压制哪些运动 |  |  |
| `anti_movements` |  |  |  |
| `obligation_value` | 取决于等级、陆军对比和态度 | AI 对来自他国的义务的重视程度 |  |
| `nationalization_desire` | `0.0`，计划经济为 `100` | AI 将建筑国有化/私有化的意愿，使用 `NATIONALIZATION_DESIRE_NATIONALIZE_THRESHOLD` 和 `NATIONALIZATION_DESIRE_PRIVATIZE_THRESHOLD` 这两个 defines 进行比较。 |  |
| `strategic_region_scores` | 取决于区域 | 此块内部接受更小的战略区域块 |  |
| `possible` | `always = no` | 每个策略各不相同 | 此策略是否可以分配给某个国家 |
| `weight` | `0` | 此策略被随机分配给某个国家的概率 |  |

### 外交块

#### 外交博弈支持

diplomatic_play_support 块会加到一国在外交博弈中对另一国的支持度上。它只对目标和发起方评估支持度。

它可以使用以下 scope：

- `root`（进行评估的支持方国家）
- `country`（AI 正在评估是否支持的国家）
- `enemy_country`（对方国家）
- `diplomatic_play_type`（外交博弈的类型）
- `is_initiator`（AI 正在评估支持的国家是否为发起方）

你还可以在添加数值时附带描述，这些描述会显示在提示信息中。

#### 战争目标分值

`wargoal_scores` 决定 AI 对某个战争目标的重视程度。它是一个 additive 块。

它可以使用以下 scope：

- `root`（进行评估的国家）
- `target_country`（战争目标的目标国家）
- `target_state`（战争目标的目标州，如果有）

它可以使用以下战争目标：

- `conquer_state`
- `return_state`
- `transfer_subject`
- `make_protectorate`
- `make_trading_post`
- `make_puppet`
- `make_tributary`
- `increase_autonomy`
- `reduce_autonomy`
- `humiliation`
- `join_power_bloc`
- `regime_change`
- `force_nationalization`
- `foreign_investment_rights`
- `open_market`
- `revoke_claim`
- `contain_threat`
- `annex_country`
- `colonization_rights`
- `unification`
- `unification_leadership`
- `liberate_subject`
- `liberate_country`
- `leave_power_bloc`
- `independence`
- `secession`

#### 战争目标权重

`wargoal_weights` 块是战争目标数值的乘数。它是乘法性的。

#### 秘密目标

secret_goal_scores 块决定 AI 对另一个国家持有某种特定战略意图的可能性。它是一个 additive 块。它可以使用以下 scope：

- `root`（进行评估的国家）
- `target_country`（目标国家）

秘密目标包括：

- `none`
- `befriend`
- `reconcile`
- `protect`
- `antagonize`
- `conquer`
- `dominate`

#### 秘密目标权重

`secret_goal_weights` 块是战争目标数值的乘数。它是乘法性的。

#### 条约

`treaty_category_scores` 块可以使用以下类别：

- `economy`（默认 4）
- `trade`（默认 5）
- `military`（默认 3）
- `military_defense`（默认 4）
- `ideology`（默认 0）
- `expansion`（默认 4）
- `power_bloc`（默认 1）
- `other`（默认 1）
- `none`（默认 0）

#### 其他外交博弈块

| 块 | 默认值 | 在其他策略中使用 | 描述 |
|---|---|---|---|
| `undesirable_infamy_level` | `50` | override | AI 会避免达到这么多恶名，除非是为了它非常想要的战争目标 |
| `unacceptable_infamy_level` | `100` | AI 绝不会故意添加会使其恶名达到这么高的战争目标 |  |
| `diplomatic_play_neutrality` | `50`（奥斯曼在“欧洲病夫”期间有例外） | additive | 加到外交博弈基础中立度上的数值（注意：我认为不能减去数值） |
| `diplomatic_play_boldness` | `50`（例外情况太多，无法在此一一列举） | 一个国家的自信程度 |  |
| `wargoal_maneuvers_fraction` | `0.35`（叙利亚、昭昭天命和法国天然边界有例外） | AI 在初始阶段愿意用多少周旋点来添加更多战争目标。低于 0 和高于 1 的数值没有额外效果 |  |
| `recklessness` | `1`（对国际弃民、宗主国及其他特定情况翻倍） | AI 对自身实力估计的乘数。AI 希望在它认为的己方兵力与敌方兵力之间至少保持均势 |  |
| `aggression` | `0.5` | 当态度允许时，AI 对另一个国家发起外交博弈的可能性 |  |

### 建筑块

#### 建筑组权重

`building_group_weights` 是 AI 分配给建筑组分值的乘数（默认为 1）。它在其他策略中的使用是乘法性的，这意味着可能会产生多次相乘。

此块接受建筑组，例如：

```
building_group_weights = {
		bg_agriculture = 1.25
}
```

#### 补贴与战争补贴

`subsidies` 和 `war_subsidies` 块控制 AI 会补贴哪些建筑。在其他策略中使用时会覆盖。

这些块接受建筑类型，并按优先级递增顺序具有以下取值（如 defines/00_ai.txt 中的 MONEY_SPENDING_* 所描述）：

- `nice_to_have`
- `wants_to_have`
- `should_have`
- `must_have`（始终开启）

默认补贴中，`building_power_plant`、`building_railway` 和 `building_port` 为 `must_have`。

#### 商品

`goods_stances` 块决定 AI 想要某种商品有多少供给。在其他策略中使用时会覆盖。

其格式如下：

```
<good> = {
	stance = <stance>
	trigger = { <trigger> }
}
```

其中立场（stance）可以是：

- `wants_high_supply`
- `wants_export`
- `does_not_want`

### 期望块

| 块 | 默认值 | 在其他策略中使用 | 描述 |
|---|---|---|---|
| `wanted_construction_output` | 取决于投资池、收入、人口和等级 | additive | AI 应以多少建造产出为目标 |
| `wanted_army_size` | 取决于收入（每 2.5k）、人口、海外人口、技术、策略，英国国家有一个 `0.75` 的乘数作为特殊情况 | AI 应拥有多少级兵营 |  |
| `wanted_navy_size` | 取决于沿海和海外人口、收入（每 5k）、技术、策略，英国国家有额外的 `50` 作为特殊情况 | AI 应拥有多少级海军基地 |  |

### 军事块

#### 战斗单位组

`combat_unit_group_weights` 设置每个战斗单位组的权重，从而决定 AI 力求达到的各单位组比例。它是一个 additive 块。它可以使用以下 scope：

- `root`（进行评估的国家）
- `military_formation`（军事编队）

原版有以下组：

- `combat_unit_group_infantry`
- `combat_unit_group_artillery`
- `combat_unit_group_cavalry`
- `combat_unit_group_light_ship`
- `combat_unit_group_capital_ship`
- `combat_unit_group_support_ship`

#### 征兵比例

conscript_battalion_ratio 块设定 AI 在一个编队中每个常备营应拥有多少征召营。它是一个 additive 块。它可以使用以下 scope：

- `root`（进行评估的国家）
- `military_formation`（军事编队）

默认情况下，它取决于陆军法律和技术。

### 其他块

#### 机构分值

`institution_scores` 块控制 AI 偏好投资哪些机构。原版中包括以下机构：

- `institution_colonial_affairs`
- `institution_social_security`
- `institution_workplace_safety`
- `institution_schools`
- `institution_police`
- `institution_health_system`
- `institution_home_affairs`

默认情况下，它们都被设为 `10`。

#### 州价值

`state_value` 块是 additive 的，控制 AI 对一个州的重视程度。

它可以使用以下 scope：

- `root`（进行评估的国家）
- `target_state`（州）
- `target_country`（州的所有者）

默认值主要基于人口和 GDP，有很多特殊情况，包括大量日志条目相关的情况，以及除非其他列强已经这样做，否则不占领中国的州。

默认情况下，已拥有的州上限为 `1000`，未拥有的州上限为 `200`。

#### 条约港价值

treaty_port_value 块是 additive 的，控制 AI 对一个条约港的重视程度。它可以使用以下 scope：

- `root`（进行评估的国家）
- `target_state`（州）
- `target_country`（州的所有者）

默认值主要基于人口和 GDP，鸦片战争和瓜分中国相关的情况有额外加成。

默认情况下，上限为 `100`。

#### 附属国价值

有两个相关的块：`subject_value` 和 `become_subject_value`。

`subject_value` 可以使用以下 scope：

- `root`（进行评估的国家）
- `target_country`（潜在的附属国）

`become_subject_value` 可以使用以下 scope：

- `root`（进行评估的国家）
- `overlord`（潜在的宗主国）

默认值主要基于 GDP，对已拥有的附属国，威望也是一个因素。

## AI 数值

AI 数值决定 AI 采取某种行动的可能性。这些包括 ai_chance、ai_weight、ai_value、ai_will_do 以及其他若干种。其具体实现和效果因所使用的内容或类型而异。有关这些机制如何运作的更多细节，请参阅脚本化内容和类型模组制作的相关页面。

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
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

| 其他 | AI • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|