---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Modifier types
source: https://vic3.paradoxwikis.com/Modifier_types
pageid: 3448
categories: [1.13, Modding]
fetched: 2026-10-27
---
本文已针对游戏当前的[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行验证。

另见：
Modifier modding（修改器修改）
**修改器类型（Modifier types）** 是用于修改各类游戏统计数值、或允许/禁止特定行为的游戏脚本。一个*静态修改器（static modifier）*可以包含多种修改器类型。修改器类型也被用于许多其他游戏对象中，例如[法律](Law modding.md)、[机构](Institution modding.md)、[技术](Technology modding.md)等。

## 修改器类型的行为

修改器类型可以持有数值或布尔值。影响同一 scope 的相同数值型修改器类型会相加，得到最终效果。布尔型修改器类型只能返回 `yes` 或 `no`。

修改器类型分为三类：硬编码（hardcoded）、基于对象（object-based）和纯脚本（script-only）。

- 硬编码修改器类型基于游戏代码定义，仅可在极小程度上修改。
- 基于对象的修改器类型基于游戏代码与游戏对象的混合定义，并且可以为新的游戏对象定义新的修改器类型。
- 纯脚本修改器类型完全由脚本定义，不会对游戏玩法产生直接影响。

数值型修改器类型的默认值为 `0`，布尔型修改器类型的默认值为 `no`。

### 修改器块（Modifier blocks）

**修改器块（modifier block）**是接受修改器类型的脚本元素。一个常见的例子是定义在 common/static_modifiers 中的**静态修改器（static modifier）**。有些静态修改器在代码中定义，通常是 /Victoria 3/game/common/static_modifiers/00_code_static_modifiers.txt 中的那些，但大多数是“事件”修改器，通过 [effect](Effect.md) `add_modifier` 施加。

一个静态修改器通常如下所示：

```
unification_prestige = {
	icon = gfx/interface/icons/timed_modifier_icons/modifier_statue_positive.dds
	country_prestige_add = 25
}
```

其中包含一个修改器图标和若干修改器类型。静态修改器不一定需要修改器类型，此时它主要是装饰性的，或用于指示其他某种机制。

修改器块的其他例子包括[法律](Law modding.md)、[技术](Technology modding.md)和[州特质](State modding.md)。在大多数情况下，修改器块会用 `modifier` 或类似变体一词显式标注。

### 修改器类型的流向

修改器类型从其被施加的对象“流向”其影响的对象类型。例如，如果一个修改器块被施加到一个国家（比如通过某项法律），并且包含一个 `state` 修改器类型，那么该修改器类型会影响该国拥有的所有州。

[静态修改器](Modifier modding.md)作用于其被添加到的 scope，而其他修改器块的行为则由游戏代码决定。例如[生产方式](https://vic3.paradoxwikis.com/Production_methods_modding)有三个块：一个仅作用于其建筑，一个作用于其所在州，还有一个作用于整个国家。

| 目标 scope | 可从哪些 scope 流入 | 流向前缀 | 备注 |
|---|---|---|---|
| 战斗（Battle） | 人物 国家 州（州内的战斗） | `battle_` |  |
| 建筑（Building） | 国家 州 | `building_` |  |
| 建筑组（Building group） | 国家 州 | `building_group_` |  |
| 人物（Character） | 军事编队 | `character_` |  |
| 国家（Country） |  | `country_` |  |
| 商品（Goods） | 建筑 建筑组 国家 | `goods_` | _add 修改器类型仅在生产方式的建筑修改器中生效 _mult 修改器类型在任何能流向建筑的场合都生效 |
| 利益集团（Interest group） | 国家 | `interest_group_` |  |
| 市场（Market） |  | `market_` |  |
| 军事编队（Military formation） | 国家 | `military_formation_` |  |
| 政治运动（Political movement） | 国家 | `political_movement_` |  |
| 强权集团（Power Bloc） |  | `power_bloc_` |  |
| 舰船（Ship） | 战斗 国家 军事编队 州（州内的战斗） | `ship_` | 与单位的流向和非战斗效果可能相同 |
| 州（State） | 国家 | `state_` |  |
| 税收（Tax） | 国家 | `tax_` |  |
| 单位（Unit） | 战斗 人物 国家 军事编队 州（州内的战斗） | `unit_` | 非战斗单位修改器可从战斗、人物和州流入，但不起任何作用 |

其他连接方式不起作用，因此施加于军事编队的 `battle` 修改器类型不会流向来影响战斗。注意，有些流向即使*本应*生效似乎也不起作用，例如在生产方式之外施加建筑就业或商品投入/产出修改器类型。

修改器类型通常可以“穿透”scope，例如施加于国家的建筑修改器类型会穿过该国的州，再到达各州的建筑。

纯脚本修改器如果以与硬编码或基于对象的修改器相同的前缀模式开头，就可以穿透传递。因此，以 `building_` 开头的纯脚本修改器应当像其他修改器一样从国家流向州再到建筑。

`Unit_` 修改器可以通过军事编队或战斗流入到单位。从任一 scope 都能到达单位，但从战斗施加时并非全部生效。这似乎取决于该修改器是在战斗中生效（如进攻、杀伤率）还是在战斗外生效（如推进速度、袭击护航船队）。注意，经验获取修改器在战斗中生效，但经验只会在每周结算时增加。如果一场战斗开始并结束都没有跨入新的一周，它们就不会起任何作用。这可能与预期行为不符。

### 脚本中的修改器类型数值

[event target](Event target.md) `modifier` 返回给定修改器类型的累加值。该数值可用于 [script value](Script value.md)，以及接受 script value 的 [trigger](Trigger.md) 和 [effect](Effect.md)。例如，一个 trigger 可以检查一个国家某项修改器类型的数值是否高于或低于某个值，或者一个 effect 可以根据某项修改器类型来缩放其影响。布尔型修改器返回 `yes` 或 `no`，可直接用于比较或用于某些 trigger。

## 定义修改器类型

所有修改器类型都在 common/modifier_type_definitions 中定义。每个修改器类型都作为一个独立的块编写，并可以包含若干参数：

| 参数 | 描述 |
|---|---|
| decimals | 定义显示该修改器类型数值时使用的小数位数 未修改的原版维多利亚3只使用 0、1 和 2 |
| color | 定义数值的着色方式：中性、良好或不良 `neutral` 始终为黑色；`good` 正值用绿色、负值用红色；`bad` 则相反。 |
| percent | 若设为 `yes`，则将数值显示为百分比 这会将显示值乘以 100 |
| boolean | 若设为 `yes`，则将该修改器定义为布尔型而非数值型 |
| prefix | 决定显示该类型条目的数值时应加上的本地化键前缀 |
| suffix | 决定显示该类型条目的数值时应加上的本地化键后缀 |
| script_only | 若设为 `yes`，则将该修改器标记为不与任何游戏机制直接交互；该修改器类型的数值仍会照常流动 |
| game_data | 用于内部处理，在 modifier_types.md 中描述如下： # AI 拥有此修改器的价值，乘以数值以决定 AI 追逐此类静态修改器的概率；仅对部分修改器类型实现 ai_value = 0 # 在代码的特定区域中，此类型应被视为的替代修改器定义。并非通用适用，用于在情境合适的情况下施加相同效果 translate = battle_offense_add # 此类型所属的修改器类型集，代码中用于执行特定操作（例如当一个国家颁布带有此类型修改器条目的法律时，更新文化社群接纳度增量） type_set = { cultural_acceptance } |

硬编码和基于对象的修改器类型必须使用确切的脚本名称或预期模式，而纯脚本修改器类型可以使用任意脚本名称。

### 本地化

每个修改器类型会生成两个[本地化](Localization.md)键：`<name>` 和 `<name>_desc`

## 基于对象的修改器

基于对象的修改器可以为那些在各对象类别中新增类型的 mod 进行扩展。未修改的原版维多利亚3包含了游戏对象的许多但并非全部可能的修改器类型。有些基于对象的修改器涉及两个对象，而大多数只涉及一个。

| 类别 | 描述 | 定义文件夹 |
|---|---|---|
| $AcceptanceStatus$ | 接纳状态 | common/acceptance_statuses |
| $BuildingGroup$ | 建筑组 | common/building_groups |
| $BuildingType$ | 建筑类型 | common/buildings |
| $Culture$ | 文化 | common/cultures |
| $Goods$ | 商品类型 | common/goods |
| $Institution$ | 机构 | common/institutions |
| $Law$ | 法律 | common/laws |
| $InterestGroup$ | 利益集团 | common/interest_groups |
| $PoliticalMovement$ | 政治运动 | common/political_movements |
| $PopType$ | 职业 | common/pop_types |
| $Religion$ | 宗教 | common/religions |
| $SocialClass$ | 社会阶层 | common/social_classes |
| $ShipGroup$ | 舰船组 | common/ship_groups |
| $ShipType$ | 舰船类型 | common/ship_types |

| 修改器类型 | 描述 | 类别 | 类型 |
|---|---|---|---|
| $BuildingType$_throughput_add | 为 $BuildingType$ 增加吞吐量 | building | additive |
| building_$PopType$_fertility_mult | 乘以建筑中雇佣的 $PopType$ 的出生率 | building | multiplicative |
| building_$PopType$_job_attractiveness_mult | 乘以建筑中对 $PopType$ 的工作岗位吸引力 | building | multiplicative |
| building_$PopType$_mortality_mult | 乘以建筑中雇佣的 $PopType$ 的死亡率 | building | multiplicative |
| building_$PopType$_shares_add | 为建筑中雇佣的 $PopType$ 增加所有权份额 | building | additive |
| building_$PopType$_shares_mult | 乘以建筑中雇佣的 $PopType$ 的所有权份额 | building | multiplicative |
| building_$PopType$_standard_of_living_add | 为建筑中雇佣的 $PopType$ 增加生活水平 | building | additive |
| building_employment_$PopType$_add | 增加建筑中雇佣的 $PopType$ 数量 | building | additive |
| building_employment_$PopType$_mult | 乘以建筑中雇佣的 $PopType$ 数量 | building | multiplicative |
| building_group_$BuildingGroup$_$PopType$_fertility_mult | 乘以 $BuildingGroup$ 中雇佣的 $PopType$ 的出生率 | building_group | multiplicative |
| building_group_$BuildingGroup$_$PopType$_mortality_mult | 乘以 $BuildingGroup$ 中雇佣的 $PopType$ 的死亡率 | building_group | multiplicative |
| building_group_$BuildingGroup$_$PopType$_standard_of_living_add | 为 $BuildingGroup$ 中雇佣的 $PopType$ 增加生活水平 | building_group | additive |
| building_group_$BuildingGroup$_allowed_collectivization_add | 提高 $BuildingGroup$ 的集体化百分比 | building_group | additive |
| building_group_$BuildingGroup$_construction_efficiency_add | 提高 $BuildingGroup$ 的建造效率 需要建筑组设有 `construction_efficiency_modifier = yes` | building_group | additive |
| building_group_$BuildingGroup$_employee_mult | 乘以 $BuildingGroup$ 中雇佣的所有人口数量 | building_group | multiplicative |
| building_group_$BuildingGroup$_fertility_mult | 乘以 $BuildingGroup$ 中雇佣的所有人口的出生率 | building_group | multiplicative |
| building_group_$BuildingGroup$_infrastructure_usage_mult | 乘以 $BuildingGroup$ 的基础设施使用量 | building_group | multiplicative |
| building_group_$BuildingGroup$_mortality_mult | 乘以 $BuildingGroup$ 中雇佣的所有人口的死亡率 | building_group | multiplicative |
| building_group_$BuildingGroup$_self_investment_chance_add | 增加 $BuildingGroup$ 自我投资扩建自身的概率 | building_group | additive |
| building_group_$BuildingGroup$_standard_of_living_add | 为 $BuildingGroup$ 中雇佣的所有人口增加生活水平 | building_group | additive |
| building_group_$BuildingGroup$_tax_mult | 乘以 $BuildingGroup$ 缴纳的税款 | building_group | multiplicative |
| building_group_$BuildingGroup$_throughput_add | 为 $BuildingGroup$ 增加吞吐量 | building_group | additive |
| building_group_$BuildingGroup$_unincorporated_throughput_add | 为建在非合并州的 $BuildingGroup$ 增加吞吐量 | building_group | additive |
| country_$BuildingGroup$_require_subsidies_bool | （原版无使用）$BuildingGroup$ 是否必须补贴？ | country | boolean |
| country_$Culture$_cultural_acceptance_add | 增加 $Culture$ 的接纳度 | country | additive |
| country_$Goods$_export_tariffs_rate_add | （原版无使用）增加 $Goods$ 的出口关税？ | country | additive |
| country_$Goods$_import_tariffs_rate_add | （原版无使用）增加 $Goods$ 的进口关税？ | country | additive |
| country_$Goods$_max_export_tariffs_level_add | （原版无使用）增加 $Goods$ 的最高出口关税等级？ | country | additive |
| country_$Goods$_max_import_tariffs_level_add | （原版无使用）增加 $Goods$ 的最高进口关税等级？ | country | additive |
| country_$Goods$_min_export_tariffs_level_add | （原版无使用）增加 $Goods$ 的最低出口关税等级？ | country | additive |
| country_$Goods$_min_import_tariffs_level_add | （原版无使用）增加 $Goods$ 的最低进口关税等级？ | country | additive |
| country_$Institution$_max_investment_add | 提高 $Institution$ 的最高投资等级 | country | additive |
| country_$PopType$_pol_str_mult | 乘以 $PopType$ 的政治力量 | country | multiplicative |
| country_$PopType$_voting_power_add | 为 $PopType$ 增加投票力量 | country | additive |
| country_$ShipGroup$_construction_efficiency_add | 为 $ShipGroup$ 增加建造效率 | country | additive |
| country_$ShipGroup$_construction_progress_max_add | 乘以 $ShipGroup$ 的每周最大建造进度 | country | additive |
| country_$ShipType$_construction_efficiency_add | 为 $ShipType$ 增加建造效率 | country | additive |
| country_$SocialClass$_acceptance_max_add | 设定 $SocialClass$ 的接纳度上限 | country | additive |
| country_$SocialClass$_acceptance_min_add | 设定 $SocialClass$ 的接纳度下限 | country | additive |
| country_$SocialClass$_cultural_acceptance_add | 增加 $SocialClass$ 的文化接纳度 | country | additive |
| country_$SocialClass$_cultural_acceptance_mult | 乘以 $SocialClass$ 的文化接纳度 | country | multiplicative |
| country_$SocialClass$_education_access_add | 增加 $SocialClass$ 的教育接入度 | country | additive |
| country_$SocialClass$_education_access_mult | 乘以 $SocialClass$ 的教育接入度 | country | multiplicative |
| country_$SocialClass$_qualification_growth_add | 增加 $SocialClass$ 的资质增长 | country | additive |
| country_$SocialClass$_qualification_growth_mult | 乘以 $SocialClass$ 的资质增长 | country | multiplicative |
| country_$SocialClass$_qualification_growth_other_class_mult | 乘以 $SocialClass$ 向其他社会阶层的资质增长 | country | multiplicative |
| country_$SocialClass$_qualification_growth_same_class_mult | 乘以 $SocialClass$ 向同一社会阶层内其他职业的资质增长 | country | multiplicative |
| country_allow_assimilation_$AcceptanceStatus$_bool | 允许同化 $AcceptanceStatus$ | country | boolean |
| country_allow_conversion_$AcceptanceStatus$_bool | 允许皈依 $AcceptanceStatus$ | country | boolean |
| country_allow_voting_$AcceptanceStatus$_bool | 允许 $AcceptanceStatus$ 投票 | country | boolean |
| country_assimilation_$AcceptanceStatus$_mult | 乘以 $AcceptanceStatus$ 的同化速度 | country | multiplicative |
| country_disallow_government_work_$AcceptanceStatus$_bool | 禁止中上层的 $AcceptanceStatus$ 在政府出资的建筑中工作 | country | boolean |
| country_disallow_military_work_$AcceptanceStatus$_bool | 禁止 $AcceptanceStatus$ 在军事建筑中工作 | country | boolean |
| country_enactment_speed_$Law$_mult | 乘以 $Law$ 的颁布速度 | country | multiplicative |
| country_enactment_success_chance_$Law$_add | 增加颁布 $Law$ 的成功概率 | country | additive |
| country_fervor_target_$Culture$_add | 增加 $Culture$ 的狂热度目标 | country | additive |
| country_institution_cost_$Institution$_add | 增加 $Institution$ 的行政力开销 | country | additive |
| country_institution_cost_$Institution$_mult | 乘以 $Institution$ 的行政力开销 | country | multiplicative |
| country_institution_impact_$Institution$_mult | 乘以 $Institution$ 的效果 | country | multiplicative |
| country_institution_size_change_speed_$Institution$_mult | 乘以 $Institution$ 的投资等级变更速度 | country | multiplicative |
| country_loyalism_increases_$AcceptanceStatus$_mult | 乘以 $AcceptanceStatus$ 的忠诚派增长 | country | multiplicative |
| country_political_strength_$AcceptanceStatus$_mult | 乘以 $AcceptanceStatus$ 的政治力量 | country | multiplicative |
| country_qualification_growth_$AcceptanceStatus$_mult | 乘以 $AcceptanceStatus$ 的资质增长 | country | multiplicative |
| country_radicalism_increases_$AcceptanceStatus$_mult | 乘以 $AcceptanceStatus$ 的激进派增长 | country | multiplicative |
| country_standard_of_living_$AcceptanceStatus$_add | 为 $AcceptanceStatus$ 增加生活水平 | country | additive |
| country_voting_power_$AcceptanceStatus$_mult | 乘以 $AcceptanceStatus$ 的投票力量 | country | multiplicative |
| country_wage_$AcceptanceStatus$_mult | 乘以支付给 $AcceptanceStatus$ 的工资 | country | multiplicative |
| goods_input_$Goods$_add | 增加建筑/生产方式的 $Goods$ 投入 | goods | additive |
| goods_input_$Goods$_mult | 乘以建筑/生产方式的 $Goods$ 投入 | goods | multiplicative |
| goods_output_$Goods$_add | 增加建筑/生产方式的 $Goods$ 产出 | goods | additive |
| goods_output_$Goods$_mult | 乘以建筑/生产方式的 $Goods$ 投入 | goods | multiplicative |
| goods_trade_advantage_$Goods$_mult | 乘以 $Goods$ 的贸易优势 | goods | multiplicative |
| interest_group_$InterestGroup$_approval_add | 增加 $InterestGroup$ 的认可度 | interest_group | additive |
| interest_group_$InterestGroup$_pol_str_mult | 乘以 $InterestGroup$ 的政治力量 | interest_group | multiplicative |
| interest_group_$InterestGroup$_pop_attraction_mult | 乘以 $InterestGroup$ 的人口吸引力 | interest_group | multiplicative |
| ship_$ShipType$_hull_damage_mult | 乘以 $ShipType$ 造成的船体伤害 | ship | multiplicative |
| ship_$ShipType$_supply_capacity_mult | 乘以 $ShipType$ 的补给容量 | ship | multiplicative |
| ship_battle_against_$ShipType$_accuracy_add | 增加瞄准 $ShipType$ 时的命中率 | ship | additive |
| ship_battle_against_$ShipType$_accuracy_mult | 乘以瞄准 $ShipType$ 时的命中率 | ship | multiplicative |
| ship_battle_against_$ShipType$_hull_damage_mult | 乘以瞄准 $ShipType$ 时造成的船体伤害 | ship | multiplicative |
| state_$BuildingType$_max_level_add | 增加 $BuildingType$ 的最高等级 | state | additive |
| state_$Culture$_standard_of_living_add | 增加 $Culture$ 的生活水平 | state | additive |
| state_$PopType$_consumption_multiplier_add | 增加 $PopType$ 的消费乘数 | state | additive |
| state_$PopType$_dependent_wage_mult | 乘以 $PopType$ 的受抚养者工资 | state | multiplicative |
| state_$PopType$_internal_migration_disallowed_bool | 禁止 $PopType$ 进行非大规模迁移 | state | boolean |
| state_$PopType$_investment_pool_contribution_add | 增加 $PopType$ 的投资池贡献 | state | additive |
| state_$PopType$_investment_pool_efficiency_mult | 乘以 $PopType$ 的投资池贡献 | state | multiplicative |
| state_$PopType$_mass_migration_disallowed_bool | 禁止 $PopType$ 进行大规模迁移 | state | boolean |
| state_$PopType$_mortality_mult | 乘以 $PopType$ 的死亡率 | state | multiplicative |
| state_$Religion$_standard_of_living_add | 增加 $Religion$ 的生活水平 | state | additive |
| state_buy_orders_$Goods$_add | 增加州内 $Goods$ 的本地购买订单 | state | additive |
| state_harvest_condition_$HarvestConditionType$_duration_mult | 乘以 $HarvestConditionType$ 的持续时间 | state | multiplicative |
| state_harvest_condition_$HarvestConditionType$_impact_mult | 乘以 $HarvestConditionType$ 的效果 | state | multiplicative |
| state_infrastructure_from_$Goods$_consumption_add | 增加州内因消费 $Goods$ 而获得的基础设施 | state | additive |
| state_pop_support_$PoliticalMovement$_add | 增加 $PoliticalMovement$ 的人口吸引力 | state | additive |
| state_pop_support_$PoliticalMovement$_mult | 乘以 $PoliticalMovement$ 的人口吸引力 | state | multiplicative |
| state_sell_orders_$Goods$_add | 增加州内 $Goods$ 的本地出售订单 | state | additive |
| unit_$CombatUnit$_offense_add | 增加 $CombatUnit$ 的进攻 | unit | additive |
| unit_$CombatUnit$_offense_mult | 增加 $CombatUnit$ 的防御 | unit | multiplicative |
| unit_defense_$TerrainKey$_add | 增加 $TerrainKey$ 中的防御 | unit | additive |
| unit_defense_$TerrainKey$_mult | 乘以 $TerrainKey$ 中的防御 | unit | multiplicative |
| unit_offense_$TerrainKey$_add | 增加 $TerrainKey$ 中的进攻 | unit | additive |
| unit_offense_$TerrainKey$_mult | 增加 $TerrainKey$ 中的防御 | unit | multiplicative |
## 仅脚本用 modifier 类型

仅脚本用 modifier 类型不会对游戏状态产生直接影响，而是充当其他脚本的“挂钩”。例如，modifier 类型 `country_disallow_law_no_schools_bool` 本身没有任何效果，但“无学校”这项法律被脚本设定为在该 modifier 类型被设置时禁止颁布。仅脚本用 modifier 类型也可以与 script value（脚本值）配合使用，例如 `power_bloc_mandate_progress_per_major_power_member_add` 就在一个 script value 中用于计算强权集团的托管事项进度增长。

任何 modifier 类型的值都可以通过 [event target](Event target.md) `modifier` 返回。例如，`modifier:country_disallow_law_no_schools_bool` 会根据该 modifier 类型的值返回 `yes` 或 `no`。数值型 modifier 在通过 `modifier` 返回时会求和，因此不同来源的数值会像硬编码和基于对象的 modifier 类型一样累加。

最后，某些仅脚本用 modifier 类型仅充当指示器，而实际效果是以其他方式实现的。

## 所有已定义 modifier 类型列表

以下 modifier 均在未修改的原版《维多利亚3》中于 common/modifier_type_definitions 里定义。其中包括所有硬编码 modifier 类型、许多潜在的基于对象的 modifier 类型，以及原版游戏机制使用的所有仅脚本用 modifier 类型。其中不包括未被定义的潜在 modifier 类型。

以下已定义的基于对象的 modifier 类型为求简洁未列入表中：

- `country_$Culture$_cultural_acceptance_add`
- `country_$SocialClass$_cultural_acceptance_add`
- `country_fervor_target_$Culture$_add`
- `state_$Culture$_standard_of_living_add`
- `state_$Religion$_standard_of_living_add`

这些类型在原版游戏中已详尽定义，可在[文化 modifier 类型列表](List of culture modifier types.md)中查看。

| Modifier 类型 | 本地化文本 | 类别 | 类型 | 格式 | 备注 |
|---|---|---|---|---|---|
| battle_casualties_mult | 承受伤亡 | battle | multiplicative | 百分比，有害 |  |
| battle_combat_width_mult | 地形战斗宽度 | battle | multiplicative | 百分比，有益 |  |
| battle_defense_owned_province_mult | 本土防御 | battle | multiplicative | 百分比，有益 |  |
| battle_naval_condition_calm_waters_chance_mult | 平静水面概率 | battle | multiplicative | 百分比，中性 |  |
| battle_naval_condition_cyclone_chance_mult | 气旋概率 | battle | multiplicative | 百分比，中性 |  |
| battle_naval_condition_fog_chance_mult | 迷雾概率 | battle | multiplicative | 百分比，中性 |  |
| battle_naval_condition_ice_chance_mult | 结冰概率 | battle | multiplicative | 百分比，中性 |  |
| battle_naval_condition_rough_waters_chance_mult | 汹涌水面概率 | battle | multiplicative | 百分比，中性 |  |
| battle_naval_condition_strong_winds_chance_mult | 强风概率 | battle | multiplicative | 百分比，中性 |  |
| battle_naval_condition_tropical_storm_chance_mult | 热带风暴概率 | battle | multiplicative | 百分比，中性 |  |
| battle_offense_owned_province_mult | 本土进攻 | battle | multiplicative | 百分比，有益 |  |
| battle_total_combat_width_mult | 总战斗宽度 | battle | multiplicative | 百分比，中性 |  |
| building_academics_job_attractiveness_mult | 学者职位吸引力 | building | multiplicative | 百分比，有益 |  |
| building_academics_mortality_mult | 学者死亡率 | building | multiplicative | 百分比，有害 |  |
| building_academics_shares_add | 学者人口持股份额 | building | additive | 中性 |  |
| building_academics_standard_of_living_add | 学者生活水平 | building | additive | 有益 |  |
| building_aristocrats_job_attractiveness_mult | 贵族职位吸引力 | building | multiplicative | 百分比，有益 |  |
| building_aristocrats_shares_add | 贵族人口持股份额 | building | additive | 中性 |  |
| building_aristocrats_standard_of_living_add | 贵族生活水平 | building | additive | 有益 |  |
| building_arms_industry_throughput_add | 军火工业建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_art_academy_throughput_add | 艺术学院建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_artillery_foundry_throughput_add | 火炮铸造厂建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_automotive_industry_throughput_add | 汽车工业建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_barrack_throughput_add | 兵营建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_bureaucrats_job_attractiveness_mult | 官僚职位吸引力 | building | multiplicative | 百分比，有益 |  |
| building_bureaucrats_shares_add | 官僚人口持股份额 | building | additive | 中性 |  |
| building_bureaucrats_standard_of_living_add | 官僚生活水平 | building | additive | 有益 |  |
| building_capitalists_job_attractiveness_mult | 资本家职位吸引力 | building | multiplicative | 百分比，有益 |  |
| building_capitalists_shares_add | 资本家人口持股份额 | building | additive | 中性 |  |
| building_capitalists_standard_of_living_add | 资本家生活水平 | building | additive | 有益 |  |
| building_cash_reserves_mult | 最大现金储备 | building | multiplicative | 百分比，有益 |  |
| building_chemical_plant_throughput_add | 肥料厂建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_clergymen_job_attractiveness_mult | 教士职位吸引力 | building | multiplicative | 百分比，有益 |  |
| building_clergymen_shares_add | 教士人口持股份额 | building | additive | 中性 |  |
| building_clergymen_standard_of_living_add | 教士生活水平 | building | additive | 有益 |  |
| building_clerks_job_attractiveness_mult | 职员，有益 |  |
| building_clerks_shares_add | 职员人口持股份额 | building | additive | 中性 |  |
| building_clerks_standard_of_living_add | 职员生活水平 | building | additive | 有益 |  |
| building_coal_mine_throughput_add | 煤矿建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_coffee_plantation_throughput_add | 咖啡种植园建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_company_government_dividends_add | 公司政府分红 | building | additive | 百分比，中性 |  |
| building_company_worker_dividends_add | 公司劳动力分红 | building | additive | 百分比，中性 |  |
| building_construction_sector_throughput_add | 建造部门建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_cotton_plantation_throughput_add | 棉花种植园建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_dye_plantation_throughput_add | 染料种植园建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_economy_of_scale_level_cap_add | 规模经济建筑等级上限 | building | additive | 有益 |  |
| building_electrics_industry_throughput_add | 电力工业建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_employment_academics_add | 每等级学者数 | building | additive | 中性 |  |
| building_employment_aristocrats_add | 每等级贵族数 | building | additive | 中性 |  |
| building_employment_bureaucrats_add | 每等级官僚数 | building | additive | 中性 |  |
| building_employment_capitalists_add | 每等级资本家数 | building | additive | 中性 |  |
| building_employment_clergymen_add | 每等级教士数 | building | additive | 中性 |  |
| building_employment_clerks_add | 每等级职员数 | building | additive | 中性 |  |
| building_employment_engineers_add | 每等级工程师数 | building | additive | 中性 |  |
| building_employment_farmers_add | 每等级农民数 | building | additive | 中性 |  |
| building_employment_laborers_add | 每等级劳工数 | building | additive | 中性 |  |
| building_employment_machinists_add | 每等级机械师数 | building | additive | 中性 |  |
| building_employment_officers_add | 每等级军官数 | building | additive | 中性 |  |
| building_employment_peasants_add | 每等级农奴数 | building | additive | 中性 |  |
| building_employment_shopkeepers_add | 每等级店主数 | building | additive | 中性 |  |
| building_employment_slaves_add | 每等级奴隶数 | building | additive | 中性 |  |
| building_employment_soldiers_add | 每等级士兵数 | building | additive | 中性 |  |
| building_engineers_job_attractiveness_mult | 工程师职位吸引力 | building | multiplicative | 百分比，有益 |  |
| building_engineers_mortality_mult | 工程师死亡率 | building | multiplicative | 百分比，有害 |  |
| building_engineers_shares_add | 工程师人口持股份额 | building | additive | 中性 |  |
| building_engineers_standard_of_living_add | 工程师生活水平 | building | additive | 有益 |  |
| building_explosives_factory_throughput_add | 炸药工厂建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_farmers_job_attractiveness_mult | 农民职位吸引力 | building | multiplicative | 百分比，有益 |  |
| building_farmers_standard_of_living_add | 农民生活水平 | building | additive | 有益 |  |
| building_fishing_wharf_throughput_add | 渔业码头建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_food_industry_throughput_add | 食品工业建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_furniture_manufactory_throughput_add | 家具制造厂建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_glassworks_throughput_add | 玻璃厂建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_gold_field_throughput_add | 金矿区建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_gold_mine_throughput_add | 金矿建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_goods_input_mult | 商品投入 | building | multiplicative | 百分比，有害 |  |
| building_government_administration_throughput_add | 政府行政建筑吞吐量 | building | additive | 百分比，有益 |  |
| building_group_bg_agriculture_allowed_collectivization_add | 集体化农业建筑最低等级 | building_group | additive | 百分比，有益 |  |
| building_group_bg_agriculture_construction_efficiency_add | 农业建造效率 | building_group | additive | 百分比，有益 |  |
| building_group_bg_agriculture_employee_mult | 农业雇员数 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_agriculture_farmers_mortality_mult | 农业受雇农民死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_agriculture_infrastructure_usage_mult | 农业建筑基础设施占用 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_agriculture_laborers_mortality_mult | 农业受雇劳工死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_agriculture_mortality_mult | 农业雇员死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_agriculture_self_investment_chance_add | 农业建筑自主投资概率 | building_group | additive | 百分比，中性 |  |
| building_group_bg_agriculture_standard_of_living_add | 农业雇员生活水平 | building_group | additive | 有益 |  |
| building_group_bg_agriculture_tax_mult | 农业税收收入 | building_group | multiplicative | 百分比，中性 |  |
| building_group_bg_agriculture_throughput_add | 农业吞吐量 | building_group | additive | 百分比，有益 |  |
| building_group_bg_arts_allowed_collectivization_add | 集体化艺术建筑最低等级 | building_group | additive | 百分比，有益 |  |
| building_group_bg_arts_throughput_add | 艺术建筑吞吐量 | building_group | additive | 百分比，有益 |  |
| building_group_bg_construction_infrastructure_usage_mult | 建造部门建筑基础设施占用 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_construction_laborers_mortality_mult | 建造业受雇劳工死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_extraction_allowed_collectivization_add | 集体化采集业建筑最低等级 | building_group | additive | 百分比，有益 |  |
| building_group_bg_extraction_construction_efficiency_add | 采集业建造效率 | building_group | additive | 百分比，有益 |  |
| building_group_bg_extraction_self_investment_chance_add | 采集业建筑自主投资概率 | building_group | additive | 百分比，中性 |  |
| building_group_bg_extraction_throughput_add | 采集业吞吐量 | building_group | additive | 百分比，有益 |  |
| building_group_bg_fishing_employee_mult | 渔业雇员数 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_fishing_engineers_mortality_mult | 渔业码头受雇工程师死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_fishing_laborers_mortality_mult | 渔业码头受雇劳工死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_fishing_machinists_mortality_mult | 渔业码头受雇机械师死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_fishing_mortality_mult | 渔业雇员死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_fishing_standard_of_living_add | 渔业雇员生活水平 | building_group | additive | 有益 |  |
| building_group_bg_fishing_tax_mult | 渔业税收收入 | building_group | multiplicative | 百分比，中性 |  |
| building_group_bg_fishing_throughput_add | 渔业吞吐量 | building_group | additive | 百分比，有益 |  |
| building_group_bg_government_construction_efficiency_add | 政府建筑建造效率 | building_group | additive | 百分比，有益 |  |
| building_group_bg_government_employee_mult | 政府雇员数 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_government_mortality_mult | 政府雇员死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_government_standard_of_living_add | 政府雇员生活水平 | building_group | additive | 有益 |  |
| building_group_bg_government_tax_mult | 政府税收收入 | building_group | multiplicative | 百分比，中性 |  |
| building_group_bg_government_throughput_add | 政府建筑吞吐量 | building_group | additive | 百分比，有益 |  |
| building_group_bg_heavy_industry_allowed_collectivization_add | 集体化重工业建筑最低等级 | building_group | additive | 百分比，有益 |  |
| building_group_bg_heavy_industry_construction_efficiency_add | 重工业建造效率 | building_group | additive | 百分比，有益 |  |
| building_group_bg_heavy_industry_engineers_mortality_mult | 重工业受雇工程师死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_heavy_industry_laborers_mortality_mult | 重工业受雇劳工死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_heavy_industry_machinists_mortality_mult | 重工业受雇机械师死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_heavy_industry_mortality_mult | 重工业雇员死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_heavy_industry_throughput_add | 重工业吞吐量 | building_group | additive | 百分比，有益 |  |
| building_group_bg_infrastructure_construction_efficiency_add | 基础设施建造效率 | building_group | additive | 百分比，有益 |  |
| building_group_bg_infrastructure_employee_mult | 基础设施雇员数 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_infrastructure_engineers_mortality_mult | 基础设施受雇工程师死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_infrastructure_laborers_mortality_mult | 基础设施受雇劳工死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_infrastructure_machinists_mortality_mult | 基础设施受雇机械师死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_infrastructure_mortality_mult | 基础设施雇员死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_infrastructure_self_investment_chance_add | 基础设施建筑自主投资概率 | building_group | additive | 百分比，中性 |  |
| building_group_bg_infrastructure_standard_of_living_add | 基础设施雇员生活水平 | building_group | additive | 有益 |  |
| building_group_bg_infrastructure_tax_mult | 基础设施税收收入 | building_group | multiplicative | 百分比，中性 |  |
| building_group_bg_infrastructure_throughput_add | 基础设施吞吐量 | building_group | additive | 百分比，有益 |  |
| building_group_bg_light_industry_allowed_collectivization_add | 集体化轻工业建筑最低等级 | building_group | additive | 百分比，有益 |  |
| building_group_bg_light_industry_construction_efficiency_add | 轻工业建造效率 | building_group | additive | 百分比，有益 |  |
| building_group_bg_light_industry_laborers_mortality_mult | 轻工业受雇劳工死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_light_industry_machinists_mortality_mult | 轻工业受雇机械师死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_light_industry_throughput_add | 轻工业吞吐量 | building_group | additive | 百分比，有益 |  |
| building_group_bg_logging_employee_mult | 伐木业雇员数 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_logging_engineers_mortality_mult | 伐木业受雇工程师死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_logging_laborers_mortality_mult | 伐木业受雇劳工死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_logging_machinists_mortality_mult | 伐木业受雇机械师死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_logging_mortality_mult | 伐木业雇员死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_logging_slaves_mortality_mult | 伐木业受雇奴隶死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_logging_standard_of_living_add | 伐木业雇员生活水平 | building_group | additive | 有益 |  |
| building_group_bg_logging_tax_mult | 伐木业税收收入 | building_group | multiplicative | 百分比，中性 |  |
| building_group_bg_logging_throughput_add | 伐木业吞吐量 | building_group | additive | 百分比，有益 |  |
| building_group_bg_logging_unincorporated_throughput_add | 林业在非整合州的吞吐量 | building_group | additive | 百分比，有益 |  |
| building_group_bg_manor_houses_aristocrats_standard_of_living_add | 庄园受雇贵族生活水平 | building_group | additive | 有益 |  |
| building_group_bg_manufacturing_allowed_collectivization_add | 集体化制造业建筑最低等级 | building_group | additive | 百分比，有益 |  |
| building_group_bg_manufacturing_employee_mult | 制造业雇员数 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_manufacturing_engineers_mortality_mult | 制造业受雇工程师死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_manufacturing_engineers_standard_of_living_add | 制造业受雇工程师生活水平 | building_group | additive | 有益 |  |
| building_group_bg_manufacturing_laborers_mortality_mult | 制造业受雇劳工死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_manufacturing_laborers_standard_of_living_add | 制造业受雇劳工生活水平 | building_group | additive | 有益 |  |
| building_group_bg_manufacturing_machinists_mortality_mult | 制造业受雇机械师死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_manufacturing_machinists_standard_of_living_add | 制造业受雇机械师生活水平 | building_group | additive | 有益 |  |
| building_group_bg_manufacturing_mortality_mult | 制造业雇员死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_manufacturing_self_investment_chance_add | 制造业建筑自主投资概率 | building_group | additive | 百分比，中性 |  |
| building_group_bg_manufacturing_standard_of_living_add | 制造业雇员生活水平 | building_group | additive | 有益 |  |
| building_group_bg_manufacturing_tax_mult | 制造业税收收入 | building_group | multiplicative | 百分比，中性 |  |
| building_group_bg_manufacturing_throughput_add | 制造业吞吐量 | building_group | additive | 百分比，有益 |  |
| building_group_bg_manufacturing_unincorporated_throughput_add | 制造业在非整合州的吞吐量 | building_group | additive | 百分比，有益 |  |
| building_group_bg_military_construction_efficiency_add | 军事建筑建造效率 | building_group | additive | 百分比，有益 |  |
| building_group_bg_military_industry_allowed_collectivization_add | 集体化军工建筑最低等级 | building_group | additive | 百分比，有益 |  |
| building_group_bg_military_industry_construction_efficiency_add | 军工建造效率 | building_group | additive | 百分比，有益 |  |
| building_group_bg_military_industry_engineers_mortality_mult | 军工受雇工程师死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_military_industry_laborers_mortality_mult | 军工受雇劳工死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_military_industry_machinists_mortality_mult | 军工受雇机械师死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_military_industry_mortality_mult | 军工雇员死亡率 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_military_industry_throughput_add | 军工吞吐量 | building_group | additive | 百分比，有益 |  |
| building_group_bg_military_throughput_add | 军事建筑吞吐量 | building_group | additive | 百分比，有益 |  |
| building_group_bg_mining_allowed_collectivization_add | 集体化矿业建筑最低等级 | building_group | additive | 百分比，有益 |  |
| building_group_bg_mining_employee_mult | 矿业雇员数 | building_group | multiplicative | 百分比，有害 |  |
| building_group_bg_mining_engineers_mortality_mult | 矿场雇用工程师的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_mining_engineers_standard_of_living_add | 矿场雇用工程师的生活水平 | building_group | additive | good |  |
| building_group_bg_mining_laborers_mortality_mult | 矿场雇用劳工的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_mining_laborers_standard_of_living_add | 矿场雇用劳工的生活水平 | building_group | additive | good |  |
| building_group_bg_mining_machinists_mortality_mult | 矿场雇用机械师的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_mining_machinists_standard_of_living_add | 矿场雇用机械师的生活水平 | building_group | additive | good |  |
| building_group_bg_mining_mortality_mult | 矿业雇员死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_mining_slaves_mortality_mult | 矿场雇用奴隶的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_mining_standard_of_living_add | 矿业雇员生活水平 | building_group | additive | good |  |
| building_group_bg_mining_tax_mult | 矿业税收收入 | building_group | multiplicative | percent, neutral |  |
| building_group_bg_mining_throughput_add | 矿场吞吐量 | building_group | additive | percent, good |  |
| building_group_bg_mining_unincorporated_throughput_add | 未合并州的矿场吞吐量 | building_group | additive | percent, good |  |
| building_group_bg_oil_extraction_employee_mult | 石油业雇员数 | building_group | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_engineers_mortality_mult | 石油开采雇用工程师的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_laborers_mortality_mult | 石油开采雇用劳工的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_machinists_mortality_mult | 石油开采雇用机械师的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_mortality_mult | 石油业雇员死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_standard_of_living_add | 石油业雇员生活水平 | building_group | additive | good |  |
| building_group_bg_oil_extraction_tax_mult | 石油业税收收入 | building_group | multiplicative | percent, neutral |  |
| building_group_bg_oil_extraction_throughput_add | 石油开采设施吞吐量 | building_group | additive | percent, good |  |
| building_group_bg_plantations_allowed_collectivization_add | 工人所有种植园建筑最低等级 | building_group | additive | percent, good |  |
| building_group_bg_plantations_construction_efficiency_add | 种植园建造效率 | building_group | additive | percent, good |  |
| building_group_bg_plantations_employee_mult | 种植园雇员数 | building_group | multiplicative | percent, bad |  |
| building_group_bg_plantations_farmers_mortality_mult | 种植园雇用农民的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_plantations_infrastructure_usage_mult | 种植园的基础设施使用量 | building_group | multiplicative | percent, bad |  |
| building_group_bg_plantations_laborers_mortality_mult | 种植园雇用劳工的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_plantations_mortality_mult | 种植园雇员死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_plantations_self_investment_chance_add | 种植园建筑自主投资几率 | building_group | additive | percent, neutral |  |
| building_group_bg_plantations_slaves_mortality_mult | 种植园雇用奴隶的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_plantations_standard_of_living_add | 种植园雇员生活水平 | building_group | additive | good |  |
| building_group_bg_plantations_tax_mult | 种植园税收收入 | building_group | multiplicative | percent, neutral |  |
| building_group_bg_plantations_throughput_add | 种植园吞吐量 | building_group | additive | percent, good |  |
| building_group_bg_plantations_unincorporated_throughput_add | 未合并州的种植园吞吐量 | building_group | additive | percent, good |  |
| building_group_bg_power_allowed_collectivization_add | 工人所有发电厂建筑最低等级 | building_group | additive | percent, good |  |
| building_group_bg_power_self_investment_chance_add | 发电厂建筑自主投资几率 | building_group | additive | percent, neutral |  |
| building_group_bg_private_infrastructure_allowed_collectivization_add | 工人所有私营基础设施建筑最低等级 | building_group | additive | percent, good |  |
| building_group_bg_ranching_allowed_collectivization_add | 工人所有牧场建筑最低等级 | building_group | additive | percent, good |  |
| building_group_bg_ranching_construction_efficiency_add | 牧场建造效率 | building_group | additive | percent, good |  |
| building_group_bg_ranching_farmers_mortality_mult | 畜牧业雇用农民的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_ranching_infrastructure_usage_mult | 牧场的基础设施使用量 | building_group | multiplicative | percent, bad |  |
| building_group_bg_ranching_laborers_mortality_mult | 畜牧业雇用劳工的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_ranching_mortality_mult | 畜牧业雇员死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_ranching_self_investment_chance_add | 牧场建筑自主投资几率 | building_group | additive | percent, neutral |  |
| building_group_bg_ranching_standard_of_living_add | 畜牧业雇员生活水平 | building_group | additive | good |  |
| building_group_bg_ranching_tax_mult | 畜牧业税收收入 | building_group | multiplicative | percent, neutral |  |
| building_group_bg_ranching_throughput_add | 牧场吞吐量 | building_group | additive | percent, good |  |
| building_group_bg_rubber_employee_mult | 橡胶业雇员数 | building_group | multiplicative | percent, bad |  |
| building_group_bg_rubber_laborers_mortality_mult | 橡胶种植园雇用劳工的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_rubber_mortality_mult | 橡胶业雇员死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_rubber_slaves_mortality_mult | 橡胶种植园雇用奴隶的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_rubber_standard_of_living_add | 橡胶业雇员生活水平 | building_group | additive | good |  |
| building_group_bg_rubber_tax_mult | 橡胶业税收收入 | building_group | multiplicative | percent, neutral |  |
| building_group_bg_rubber_throughput_add | 橡胶种植园吞吐量 | building_group | additive | percent, good |  |
| building_group_bg_rubber_unincorporated_throughput_add | 未合并州的橡胶种植园吞吐量 | building_group | additive | percent, good |  |
| building_group_bg_service_employee_mult | 城市中心雇员数 | building_group | multiplicative | percent, bad |  |
| building_group_bg_service_mortality_mult | 城市中心雇员死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_service_standard_of_living_add | 城市中心雇员生活水平 | building_group | additive | good |  |
| building_group_bg_service_tax_mult | 城市中心税收收入 | building_group | multiplicative | percent, neutral |  |
| building_group_bg_service_throughput_add | 服务业吞吐量 | building_group | additive | percent, good |  |
| building_group_bg_subsistence_agriculture_allowed_collectivization_add | 工人所有自给农业建筑最低等级 | building_group | additive | percent, good |  |
| building_group_bg_subsistence_agriculture_peasants_standard_of_living_add | 自给农业雇用农民的生活水平 | building_group | additive | good |  |
| building_group_bg_subsistence_ranching_allowed_collectivization_add | 工人所有自给畜牧业建筑最低等级 | building_group | additive | percent, good |  |
| building_group_bg_subsistence_ranching_peasants_standard_of_living_add | 自给畜牧业雇用农民的生活水平 | building_group | additive | good |  |
| building_group_bg_whaling_employee_mult | 捕鲸业雇员数 | building_group | multiplicative | percent, bad |  |
| building_group_bg_whaling_laborers_mortality_mult | 捕鲸站雇用劳工的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_whaling_machinists_mortality_mult | 捕鲸站雇用机械师的死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_whaling_mortality_mult | 捕鲸业雇员死亡率 | building_group | multiplicative | percent, bad |  |
| building_group_bg_whaling_standard_of_living_add | 捕鲸业雇员生活水平 | building_group | additive | good |  |
| building_group_bg_whaling_tax_mult | 捕鲸业税收收入 | building_group | multiplicative | percent, neutral |  |
| building_group_bg_whaling_throughput_add | 捕鲸业吞吐量 | building_group | additive | percent, good |  |
| building_iron_mine_throughput_add | 铁矿建筑吞吐量 | building | additive | percent, good |  |
| building_job_attractiveness_mult | 工作吸引力 | building | multiplicative | percent, good |  |
| building_laborers_job_attractiveness_mult | 劳工的工作吸引力 | building | multiplicative | percent, good |  |
| building_laborers_mortality_mult | 劳工的死亡率 | building | multiplicative | percent, bad |  |
| building_laborers_shares_add | 劳工人口持股份额 | building | additive | neutral |  |
| building_laborers_standard_of_living_add | 劳工的生活水平 | building | additive | good |  |
| building_lead_mine_throughput_add | 铅矿建筑吞吐量 | building | additive | percent, good |  |
| building_level_bureaucracy_cost_add | 建筑等级行政力成本 | building | additive | bad |  |
| building_livestock_ranch_throughput_add | 畜牧场建筑吞吐量 | building | additive | percent, good |  |
| building_machinists_job_attractiveness_mult | 机械师的工作吸引力 | building | multiplicative | percent, good |  |
| building_machinists_mortality_mult | 机械师的死亡率 | building | multiplicative | percent, bad |  |
| building_machinists_shares_add | 机械师人口持股份额 | building | additive | neutral |  |
| building_machinists_standard_of_living_add | 机械师的生活水平 | building | additive | good |  |
| building_maize_farm_throughput_add | 玉米农场建筑吞吐量 | building | additive | percent, good |  |
| building_millet_farm_throughput_add | 小米农场建筑吞吐量 | building | additive | percent, good |  |
| building_minimum_incorporated_subsistence_employment_add | 已合并州受保护的自给就业 | building | additive | percent, neutral |  |
| building_minimum_wage_mult | 建筑工资目标 | building | multiplicative | percent, neutral |  |
| building_mobilization_cost_mult | 动员商品需求 | building | multiplicative | percent, bad |  |
| building_motor_industry_throughput_add | 汽车工业建筑吞吐量 | building | additive | percent, good |  |
| building_munition_plant_throughput_add | 弹药厂建筑吞吐量 | building | additive | percent, good |  |
| building_nationalization_cost_mult | 国有化补偿 | building | multiplicative | percent, bad |  |
| building_nationalization_investment_return_add | 国有化投资回报 | building | additive | percent, good |  |
| building_nationalization_radicals_mult | 国有化产生的激进派 | building | multiplicative | percent, bad |  |
| building_naval_administration_hiring_rate_mult | 海军行政署雇佣速度 | building | multiplicative | percent, good |  |
| building_naval_administration_throughput_add | 海军行政署建筑吞吐量 | building | additive | percent, good |  |
| building_naval_administration_training_rate_add | 海军行政署训练率 | building | additive | good |  |
| building_naval_administration_training_rate_mult | 海军行政署训练率 | building | multiplicative | percent, good |  |
| building_officers_job_attractiveness_mult | 军官的工作吸引力 | building | multiplicative | percent, good |  |
| building_officers_shares_add | 军官人口持股份额 | building | additive | neutral |  |
| building_officers_standard_of_living_add | 军官的生活水平 | building | additive | good |  |
| building_opium_plantation_throughput_add | 鸦片种植园建筑吞吐量 | building | additive | percent, good |  |
| building_paper_mill_throughput_add | 造纸厂建筑吞吐量 | building | additive | percent, good |  |
| building_peasants_job_attractiveness_mult | 农民的工作吸引力 | building | multiplicative | percent, good |  |
| building_peasants_standard_of_living_add | 农民的生活水平 | building | additive | good |  |
| building_port_throughput_add | 港口建筑吞吐量 | building | additive | percent, good |  |
| building_power_plant_throughput_add | 发电厂建筑吞吐量 | building | additive | percent, good |  |
| building_railway_throughput_add | 铁路建筑吞吐量 | building | additive | percent, good |  |
| building_rice_farm_throughput_add | 稻田建筑吞吐量 | building | additive | percent, good |  |
| building_rubber_plantation_throughput_add | 橡胶种植园建筑吞吐量 | building | additive | percent, good |  |
| building_rye_farm_throughput_add | 黑麦农场建筑吞吐量 | building | additive | percent, good |  |
| building_self_investment_chance_add | 建筑自主投资几率 | building | additive | percent, neutral |  |
| building_shipyard_throughput_add | 造船厂建筑吞吐量 | building | additive | percent, good |  |
| building_shopkeepers_job_attractiveness_mult | 店主的工作吸引力 | building | multiplicative | percent, good |  |
| building_shopkeepers_shares_add | 店主人口持股份额 | building | additive | neutral |  |
| building_shopkeepers_standard_of_living_add | 店主的生活水平 | building | additive | good |  |
| building_silk_plantation_throughput_add | 丝织种植园建筑吞吐量 | building | additive | percent, good |  |
| building_slaves_mortality_mult | 奴隶的死亡率 | building | multiplicative | percent, bad |  |
| building_slaves_standard_of_living_add | 奴隶的生活水平 | building | additive | good |  |
| building_soldiers_job_attractiveness_mult | 士兵的工作吸引力 | building | multiplicative | percent, good |  |
| building_soldiers_shares_add | 士兵人口持股份额 | building | additive | neutral |  |
| building_soldiers_standard_of_living_add | 士兵的生活水平 | building | additive | good |  |
| building_steel_mill_throughput_add | 钢厂建筑吞吐量 | building | additive | percent, good |  |
| building_subsistence_farm_throughput_add | 自给农场建筑吞吐量 | building | additive | percent, good |  |
| building_subsistence_output_add | 自给产出 | building | additive | neutral |  |
| building_subsistence_output_mult | 自给产出 | building | multiplicative | percent, neutral |  |
| building_sugar_plantation_throughput_add | 糖料种植园建筑吞吐量 | building | additive | percent, good |  |
| building_sulfur_mine_throughput_add | 硫矿建筑吞吐量 | building | additive | percent, good |  |
| building_synthetics_plant_throughput_add | 合成材料厂建筑吞吐量 | building | additive | percent, good |  |
| building_tea_plantation_throughput_add | 茶园建筑吞吐量 | building | additive | percent, good |  |
| building_textile_mill_throughput_add | 纺织厂建筑吞吐量 | building | additive | percent, good |  |
| building_throughput_add | 吞吐量 | building | additive | percent, good |  |
| building_tobacco_plantation_throughput_add | 烟草种植园建筑吞吐量 | building | additive | percent, good |  |
| building_tooling_workshop_throughput_add | 工具作坊建筑吞吐量 | building | additive | percent, good |  |
| building_trade_center_throughput_add | 贸易中心建筑吞吐量 | building | additive | percent, good |  |
| building_training_rate_add | 训练率 | building | additive | good |  |
| building_training_rate_mult | 训练率 | building | multiplicative | percent, good |  |
| building_unincorporated_subsistence_output_mult | 未合并州的自给产出 | building | multiplicative | percent, good |  |
| building_unincorporated_throughput_add | 未合并州的吞吐量 | building | additive | percent, good |  |
| building_university_throughput_add | 大学建筑吞吐量 | building | additive | percent, good |  |
| building_urban_center_throughput_add | 城市中心建筑吞吐量 | building | additive | percent, good |  |
| building_vineyard_throughput_add | 葡萄园建筑吞吐量 | building | additive | percent, good |  |
| building_whaling_station_throughput_add | 捕鲸站建筑吞吐量 | building | additive | percent, good |  |
| building_wheat_farm_throughput_add | 小麦农场建筑吞吐量 | building | additive | percent, good |  |
| building_working_conditions_mult | 危险的工作条件 | building | multiplicative | percent, bad |  |
| character_advancement_speed_add | 将军晋升速度 | character | additive | good |  |
| character_advancement_speed_mult | 将军晋升速度 | character | multiplicative | percent, good |  |
| character_battle_condition_aggressive_maneuver_mult | 激进机动几率 | character | multiplicative | percent, neutral |  |
| character_battle_condition_blunder_mult | 失误几率 | character | multiplicative | percent, bad |  |
| character_battle_condition_broken_supply_line_mult | 补给线被切断几率 | character | multiplicative | percent, bad |  |
| character_battle_condition_camouflaged_mult | 伪装几率 | character | multiplicative | percent, good |  |
| character_battle_condition_careful_maneuver_mult | 谨慎机动几率 | character | multiplicative | percent, good |  |
| character_battle_condition_charted_terrain_mult | 勘明地形几率 | character | multiplicative | percent, good |  |
| character_battle_condition_death_from_below_mult | 水下杀机几率 | character | multiplicative | percent, good |  |
| character_battle_condition_dug_in_mult | 坚守工事几率 | character | multiplicative | percent, good |  |
| character_battle_condition_exhausted_mult | 疲惫几率 | character | multiplicative | percent, bad |  |
| character_battle_condition_good_visibility_mult | 良好能见度几率 | character | multiplicative | percent, good |  |
| character_battle_condition_guerilla_ambush_mult | 伏击几率 | character | multiplicative | percent, good |  |
| character_battle_condition_logistics_secured_mult | 后勤有保障几率 | character | multiplicative | percent, good |  |
| character_battle_condition_lost_mult | 迷路几率 | character | multiplicative | percent, bad |  |
| character_battle_condition_mud_mult | 泥泞几率 | character | multiplicative | percent, bad |  |
| character_battle_condition_poor_visibility_mult | 能见度不良几率 | character | multiplicative | percent, bad |  |
| character_battle_condition_ramming_maneuver_mult | 撞击机动几率 | character | multiplicative | percent, neutral |  |
| character_battle_condition_rapid_advance_mult | 快速推进几率 | character | multiplicative | percent, good |  |
| character_battle_condition_rough_waters_mult | 波涛汹涌几率 | character | multiplicative | percent, neutral |  |
| character_battle_condition_strong_winds_mult | 强风几率 | character | multiplicative | percent, neutral |  |
| character_battle_condition_surprise_maneuver_mult | 出其不意机动几率 | character | multiplicative | percent, good |  |
| character_blockade_mult | 海军上将封锁强度 | character | multiplicative | percent, good |  |
| character_command_limit_add | 指挥上限 | character | additive | good |  |
| character_command_limit_mult | 指挥上限 | character | multiplicative | percent, good |  |
| character_commander_loyalty_add | 指挥官忠诚度 | character | additive | good |  |
| character_convoy_protection_mult | 海军上将商船护航能力 | character | multiplicative | percent, good |  |
| character_convoy_raiding_mult | 海军上将商船袭击效率 | character | multiplicative | percent, good |  |
| character_coup_strength_add | 政变强度 | character | additive | neutral |  |
| character_coup_strength_mult | 政变强度 | character | multiplicative | percent, neutral |  |
| character_expedition_events_explorer_mult | 远征机遇 | character | multiplicative | percent, good |  |
| character_health_add | 人物健康 | character | additive | percent, good |  |
| character_interception_add | 海军上将拦截几率 | character | additive | good |  |
| character_loyalty_add | 忠诚度 | character | additive | good |  |
| character_loyalty_mult | 忠诚度 | character | multiplicative | percent, good |  |
| character_max_offensive_battles_add | 最大进攻战斗数 | character | additive | good |  |
| character_naval_mission_area_add | 海军任务区域大小 | character | additive | good |  |
| character_piracy_goods_capacity_mult | 劫掠容量 | character | multiplicative | percent, good |  |
| character_popularity_add | 名望 | character | additive | good |  |
| character_prominence_add | 显赫度 | character | additive | neutral |  |
| character_raid_supply_add | 海军上将袭击补给几率 | character | additive | good |  |
| country_academics_pol_str_mult | 学者的政治力量 | country | multiplicative | percent, neutral |  |
| country_academics_voting_power_add | 学者选票带来的政治力量 | country | additive | neutral | Object-based Enables elections |
| country_acceptance_homeland_add | 来自本土的接纳度 | country | additive | good |  |
| country_acceptance_no_shared_heritage_trait_add | 来自无共同传承特质的接纳度 | country | additive | good |  |
| country_acceptance_no_shared_language_trait_add | 来自无共同语言特质的接纳度 | country | additive | good |  |
| country_acceptance_no_shared_religious_trait_add | 来自无共同宗教特质的接纳度 | country | additive | good |  |
| country_acceptance_no_shared_tradition_trait_add | 来自无共同传统特质的接纳度 | country | additive | good |  |
| country_acceptance_not_homeland_add | 来自非本土的接纳度 | country | additive | good |  |
| country_acceptance_primary_culture_add | 来自主流文化的接纳度 | country | additive | good |  |
| country_acceptance_shared_heritage_trait_add | 来自传承特质的接纳度 | country | additive | good |  |
| country_acceptance_shared_heritage_trait_group_add | 来自传承特质组的接纳度 | country | additive | good |  |
| country_acceptance_shared_language_trait_add | 来自语言特质的接纳度 | country | additive | good |  |
| country_acceptance_shared_language_trait_group_add | 来自语言特质组的接纳度 | country | additive | good |  |
| country_acceptance_shared_religious_trait_add | 来自宗教特质的接纳度 | country | additive | good |  |
| country_acceptance_shared_religious_trait_group_add | 来自宗教特质组的接纳度 | country | additive | good |  |
| country_acceptance_shared_tradition_trait_add | 来自传统特质的接纳度 | country | additive | good |  |
| country_acceptance_state_religion_add | 来自国教的接纳度 | country | additive | good |  |
| country_admiral_rank_impact_mult | 海军上将军衔影响 | country | multiplicative | percent, good |  |
| country_agitator_slots_add | 潜在鼓动家数量 | country | additive | good |  |
| country_ahead_of_time_research_penalty_mult | 超前研究惩罚 | country | multiplicative | percent, bad |  |
| country_all_buildings_protected_bool | 禁止缩减所有建筑规模 | country | boolean | bad |  |
| country_allow_assimilation_cultural_erasure_bool | 允许文化抹除地位的人口进行同化 | country | boolean | neutral |  |
| country_allow_assimilation_full_acceptance_bool | 允许完全接纳地位的人口进行同化 | country | boolean | neutral |  |
| country_allow_assimilation_open_prejudice_bool | 允许公然歧视地位的人口进行同化 | country | boolean | neutral |  |
| country_allow_assimilation_second_rate_citizen_bool | 允许二等公民地位的人口进行同化 | country | boolean | neutral |  |
| country_allow_assimilation_violent_hostility_bool | 允许暴力敌视地位的人口进行同化 | country | boolean | neutral |  |
| country_allow_conversion_cultural_erasure_bool | 允许文化抹除地位的人口改宗 | country | boolean | neutral |  |
| country_allow_conversion_full_acceptance_bool | 允许完全接纳地位的人口改宗 | country | boolean | neutral |  |
| country_allow_conversion_open_prejudice_bool | 允许公然歧视地位的人口改宗 | country | boolean | neutral |  |
| country_allow_conversion_second_rate_citizen_bool | 允许二等公民地位的人口改宗 | country | boolean | neutral |  |
| country_allow_conversion_violent_hostility_bool | 允许暴力敌视地位的人口改宗 | country | boolean | neutral |  |
| country_allow_enacting_decrees_in_subject_bool | 允许在附属国的州颁布法令 | country | boolean | good |  |
| country_allow_multiple_alliances_bool | 允许多个同盟 | country | boolean | good |  |
| country_allow_voting_cultural_erasure_bool | 给予文化抹除地位投票权 | country | boolean | neutral |  |
| country_allow_voting_full_acceptance_bool | 给予完全接纳地位投票权 | country | boolean | neutral |  |
| country_allow_voting_open_prejudice_bool | 给予公然歧视地位投票权 | country | boolean | neutral |  |
| country_allow_voting_second_rate_citizen_bool | 给予二等公民地位投票权 | country | boolean | neutral |  |
| country_allow_voting_violent_hostility_bool | 给予暴力敌视地位投票权 | country | boolean | neutral |  |
| country_amenability_add | 国家服从度 | country | additive | good |  |
| country_aristocrats_pol_str_mult | 贵族的政治力量 | country | multiplicative | percent, neutral |  |
| country_aristocrats_voting_power_add | 来自贵族选票的政治力量 | country | additive | neutral | 基于对象，启用选举 |
| country_assimilation_cultural_erasure_mult | 文化抹除地位的同化 | country | multiplicative | percent, neutral |  |
| country_assimilation_delta_threshold_add | 文化同化阈值 | country | additive | good |  |
| country_assimilation_full_acceptance_mult | 完全接纳地位的同化 | country | multiplicative | percent, neutral |  |
| country_assimilation_open_prejudice_mult | 公然歧视地位的同化 | country | multiplicative | percent, neutral |  |
| country_assimilation_second_rate_citizen_mult | 二等公民地位的同化 | country | multiplicative | percent, neutral |  |
| country_assimilation_violent_hostility_mult | 暴力敌视地位的同化 | country | multiplicative | percent, neutral |  |
| country_authority_add | 权威力 | country | additive | good |  |
| country_authority_cost_add | 权威力消耗 | country | additive | bad |  |
| country_authority_mult | 权威力 | country | multiplicative | percent, good |  |
| country_authority_per_subject_add | 每个附属国的权威力 | country | additive | good |  |
| country_bg_manufacturing_require_subsidies_bool | 制造业强制补贴 | country | boolean | bad |  |
| country_block_government_reform_bool | 阻止政府改革 | country | boolean | neutral |  |
| country_bolster_attraction_factor | 扶持对政治运动吸引力的效果 | country | multiplicative | percent, neutral |  |
| country_bolster_cost_mult | 扶持消耗 | country | multiplicative | percent, bad |  |
| country_brahmins_acceptance_min_add | 婆罗门社会阶层的最低接纳度 | country | additive | good |  |
| country_brahmins_qualification_growth_other_class_mult | 婆罗门在婆罗门社会阶层之外的资质增长 | country | multiplicative | percent, good |  |
| country_brahmins_qualification_growth_same_class_mult | 婆罗门社会阶层内部的资质增长 | country | multiplicative | percent, good |  |
| country_bureaucracy_add | 行政力 | country | additive | good |  |
| country_bureaucracy_cost_add | 行政力消耗 | country | additive | bad |  |
| country_bureaucracy_investment_cost_factor_mult | 机构行政力消耗倍率 | country | multiplicative | percent, bad |  |
| country_bureaucracy_mult | 行政力 | country | multiplicative | percent, good |  |
| country_bureaucrats_pol_str_mult | 官僚的政治力量 | country | multiplicative | percent, neutral |  |
| country_bureaucrats_voting_power_add | 来自官僚选票的政治力量 | country | additive | neutral | 基于对象，启用选举 |
| country_can_form_construction_company_bool | 可以成立建筑类公司 | country | boolean | neutral |  |
| country_can_impose_same_lawgroup_army_model_in_power_bloc_bool | **强制**集团成员采用相同陆军模式法律 | country | boolean | good |  |
| country_can_impose_same_lawgroup_church_and_state_in_power_bloc_bool | **强制**集团成员采用相同政教关系法律 | country | boolean | good |  |
| country_can_impose_same_lawgroup_citizenship_in_power_bloc_bool | **强制**集团成员采用相同公民权法律 | country | boolean | good |  |
| country_can_impose_same_lawgroup_colonization_in_power_bloc_bool | **强制**集团成员采用相同殖民法律 | country | boolean | good |  |
| country_can_impose_same_lawgroup_distribution_of_power_in_power_bloc_bool | **强制**集团成员采用相同权力分配法律 | country | boolean | good |  |
| country_can_impose_same_lawgroup_education_system_in_power_bloc_bool | **强制**集团成员采用相同教育体制法律 | country | boolean | good |  |
| country_can_impose_same_lawgroup_governance_principles_in_power_bloc_bool | **强制**集团成员采用相同治理原则法律 | country | boolean | good |  |
| country_can_impose_same_lawgroup_policing_in_power_bloc_bool | **强制**集团成员采用相同治安法律 | country | boolean | good |  |
| country_can_only_conscript_peasants_bool | 仅允许征募步兵营 | country | boolean | good |  |
| country_cannot_be_subjugated_bool | 不可被臣属 | country | boolean | neutral |  |
| country_cannot_be_target_for_law_imposition_bool | 不可成为法律强制的对象 | country | boolean | good |  |
| country_cannot_cancel_law_enactment_bool | 禁止}}取消法律制定 | country | boolean | bad |  |
| country_cannot_enact_laws_bool | 禁止}}制定法律 | country | boolean | bad |  |
| country_cannot_join_power_bloc_bool | 不可加入强权集团 | country | boolean | neutral |  |
| country_cannot_start_law_enactment_bool | 禁止}}启动法律制定 | country | boolean | bad |  |
| country_capitalists_pol_str_mult | 资本家的政治力量 | country | multiplicative | percent, neutral |  |
| country_capitalists_voting_power_add | 来自资本家选票的政治力量 | country | additive | neutral | 基于对象，启用选举 |
| country_clergymen_pol_str_mult | 神职人员的政治力量 | country | multiplicative | percent, neutral |  |
| country_clergymen_voting_power_add | 来自神职人员选票的政治力量 | country | additive | neutral | 基于对象，启用选举 |
| country_clerks_pol_str_mult | 职员的政治力量 | country | multiplicative | percent, neutral |  |
| country_clerks_voting_power_add | 来自职员选票的政治力量 | country | additive | neutral | 基于对象，启用选举 |
| country_company_construction_efficiency_bonus_add | 公司建筑加成 | country | additive | percent, good |  |
| country_company_throughput_bonus_add | 公司吞吐量加成 | country | additive | percent, good |  |
| country_construction_add | 建造力 | country | additive | good |  |
| country_construction_goods_cost_mult | 建筑商品消耗 | country | multiplicative | percent, bad |  |
| country_consumption_tax_cost_mult | 消费税成本 | country | multiplicative | percent, bad |  |
| country_conversion_delta_threshold_add | 宗教改宗阈值 | country | additive | good |  |
| country_coup_resistance_add | 政变抵抗力 | country | additive | neutral |  |
| country_coup_resistance_mult | 政变抵抗力 | country | multiplicative | percent, neutral |  |
| country_dalit_acceptance_max_add | 达利特社会阶层的最高接纳度 | country | additive | bad |  |
| country_dalit_cultural_acceptance_mult | 达利特社会阶层的文化接纳度 | country | multiplicative | percent, good |  |
| country_dalit_education_access_add | 达利特社会阶层的教育机会 | country | additive | good |  |
| country_dalit_education_access_mult | 达利特社会阶层的教育机会 | country | multiplicative | percent, good |  |
| country_dalit_qualification_growth_add | 达利特社会阶层的资质增长 | country | additive | good |  |
| country_dalit_qualification_growth_mult | 达利特社会阶层的资质增长 | country | multiplicative | percent, good |  |
| country_dalit_qualification_growth_other_class_mult | 达利特在达利特社会阶层之外的资质增长 | country | multiplicative | percent, good |  |
| country_dalit_qualification_growth_same_class_mult | 达利特社会阶层内部的资质增长 | country | multiplicative | percent, good |  |
| country_damage_relations_speed_mult | 恶化关系速度 | country | multiplicative | percent, good |  |
| country_diplomatic_play_maneuvers_add | 每次外交博弈的博弈点数 | country | additive | good |  |
| country_diplomatic_play_maneuvers_mult | 每次外交博弈的博弈点数 | country | multiplicative | percent, good |  |
| country_diplomatic_reputation_add | 外交声誉 | country | additive | good |  |
| country_disable_investment_pool_bool | 禁用投资池（公司除外） | country | boolean | bad |  |
| country_disable_nationalization_bool | 禁用国有化 | country | boolean | bad |  |
| country_disable_nationalization_without_compensation_bool | 禁用无偿国有化 | country | boolean | bad |  |
| country_disable_non_company_privatization_bool | 禁用私有化（公司除外） | country | boolean | bad |  |
| country_disallow_aggressive_plays_bool | 禁止进攻性外交博弈 | country | boolean | neutral |  |
| country_disallow_agitator_invites_bool | 不可邀请流亡者 | country | boolean | neutral |  |
| country_disallow_government_work_cultural_erasure_bool | 禁止文化抹除地位的中上层人口在政府建筑工作 | country | boolean | neutral |  |
| country_disallow_government_work_full_acceptance_bool | 禁止完全接纳地位的中上层人口在政府建筑工作 | country | boolean | neutral |  |
| country_disallow_government_work_open_prejudice_bool | 禁止公然歧视地位的中上层人口在政府建筑工作 | country | boolean | neutral |  |
| country_disallow_government_work_second_rate_citizen_bool | 禁止二等公民地位的中上层人口在政府建筑工作 | country | boolean | neutral |  |
| country_disallow_government_work_violent_hostility_bool | 禁止暴力敌视地位的中上层人口在政府建筑工作 | country | boolean | neutral |  |
| country_disallow_law_no_colonial_affairs_bool | 禁止“无殖民事务” | country | boolean | bad |  |
| country_disallow_law_no_police_bool | 禁止“无警察” | country | boolean | bad |  |
| country_disallow_law_no_schools_bool | 禁止“无学校” | country | boolean | bad |  |
| country_disallow_military_work_cultural_erasure_bool | 禁止文化抹除地位的人口在军事建筑工作 | country | boolean | neutral |  |
| country_disallow_military_work_full_acceptance_bool | 禁止完全接纳地位的人口在军事建筑工作 | country | boolean | neutral |  |
| country_disallow_military_work_open_prejudice_bool | 禁止公然歧视地位的人口在军事建筑工作 | country | boolean | neutral |  |
| country_disallow_military_work_second_rate_citizen_bool | 禁止二等公民地位的人口在军事建筑工作 | country | boolean | neutral |  |
| country_disallow_military_work_violent_hostility_bool | 禁止暴力敌视地位的人口在军事建筑工作 | country | boolean | neutral |  |
| country_disallow_trade_bool | 禁用贸易中心 | country | boolean | bad |  |
| country_disallow_trade_outside_canton_bool | 禁用广东以西以外的贸易中心 | country | boolean | bad | 仅限脚本 |
| country_disallow_trade_outside_kyushu_bool | 禁用九州以外的贸易中心 | country | boolean | bad |  |
| country_economic_dependence_on_overlord_add | 对宗主国的经济依附 | country | additive | bad |  |
| country_education_fervor_add | 教育机构狂热 | country | additive | neutral |  |
| country_electoral_confidence_impact_mult | 选举信心影响 | country | multiplicative | percent, neutral |  |
| country_electoral_confidence_over_time | 每月选举信心变化 | country |  | percent, good |  |
| country_enactment_speed_law_anarchy_mult | country_enactment_speed_law_anarchy_mult | country | multiplicative | percent, good |  |
| country_enactment_speed_law_autocracy_mult | country_enactment_speed_law_autocracy_mult | country | multiplicative | percent, good |  |
| country_enactment_speed_law_oligarchy_mult | country_enactment_speed_law_oligarchy_mult | country | multiplicative | percent, good |  |
| country_enactment_speed_law_public_schools_mult | 公立学校的制定速度 | country | multiplicative | percent, good |  |
| country_enactment_speed_law_single_party_state_mult | country_enactment_speed_law_single_party_state_mult | country | multiplicative | percent, good |  |
| country_enactment_speed_law_technocracy_mult | 技术官僚制的制定速度 | country | multiplicative | percent, good |  |
| country_enactment_success_chance_law_anarchy_add | 无政府状态的制定成功率 | country | additive | percent, good |  |
| country_enactment_success_chance_law_autocracy_add | 独裁制的制定成功率 | country | additive | percent, good |  |
| country_enactment_success_chance_law_oligarchy_add | 寡头制的制定成功率 | country | additive | percent, good |  |
| country_enactment_success_chance_law_public_schools_add | 公立学校的制定成功率 | country | additive | percent, good |  |
| country_enactment_success_chance_law_single_party_state_add | 一党制国家的制定成功率 | country | additive | percent, good |  |
| country_enactment_success_chance_law_technocracy_add | 技术官僚制的制定成功率 | country | additive | percent, good |  |
| country_engineers_pol_str_mult | 工程师的政治力量 | country | multiplicative | percent, neutral |  |
| country_engineers_voting_power_add | 来自工程师选票的政治力量 | country | additive | neutral | 基于对象，启用选举 |
| country_expedition_events_explorer_mult | 远征机遇 | country | multiplicative | percent, good |  |
| country_expenses_add | 政府开支 | country | additive | bad |  |
| country_farmers_pol_str_mult | 农场主的政治力量 | country | multiplicative | percent, neutral |  |
| country_farmers_voting_power_add | 来自农场主选票的政治力量 | country | additive | neutral | 基于对象，启用选举 |
| country_financial_districts_buy_farms_likelihood | 金融区对种植园、牧场和农业的投资 | country |  | percent, good |  |
| country_flagship_interest_gain_mult | 旗舰参与度增长 | country | multiplicative | percent, good |  |
| country_forbid_electoral_fraud_bool | 禁止选举舞弊 | country | boolean | neutral |  |
| country_forbid_monopoly_bool | 禁止垄断 | country | boolean | bad |  |
| country_force_privatization_bool | 强制私有化 | country | boolean | neutral |  |
| country_foreign_collectivization_bool | 外国集体化 | country | boolean | neutral |  |
| country_frankenstein_company_bool | 实验性模组可运行 | country | boolean | neutral |  |
| country_free_charters_add | 免费公司特许状 | country | additive | good |  |
| country_general_rank_impact_mult | 将军军衔影响 | country | multiplicative | percent, good |  |
| country_gold_reserve_limit_mult | 黄金储备上限 | country | multiplicative | percent, good |  |
| country_government_buildings_protected_bool | 禁止缩减政府建筑规模 | country | boolean | bad |  |
| country_government_dividends_efficiency_add | 政府分红效率 | country | additive | percent, good |  |
| country_government_dividends_reinvestment_add | 政府分红再投资 | country | additive | percent, neutral |  |
| country_government_dividends_waste_add | 政府分红浪费 | country | additive | percent, bad |  |
| country_government_wages_mult | 政府工资 | country | multiplicative | percent, neutral |  |
| country_higher_diplomatic_acceptance_same_religion_bool | 相同宗教国家更高的外交提案接受度 | country | boolean | good |  |
| country_higher_leverage_from_economic_dependence_bool | 提高经济依附带来的筹码 | country | boolean | good |  |
| country_improve_relations_speed_mult | 改善关系速度 | country | multiplicative | percent, good |  |
| country_infamy_decay_mult | 恶名衰减 | country | multiplicative | percent, good |  |
| country_infamy_generation_against_unrecognized_mult | 对未受承认政权的恶名产生 | country | multiplicative | percent, bad |  |
| country_infamy_generation_mult | 恶名产生 | country | multiplicative | percent, bad |  |
| country_influence_add | 影响力 | country | additive | good |  |
| country_influence_cost_add | 影响力消耗 | country | additive | bad |  |
| country_influence_mult | 影响力 | country | multiplicative | percent, good |  |
| country_initiator_war_goal_maneuver_cost_mult | 外交博弈发起者的战争目标博弈点数消耗 | country | multiplicative | percent, bad |  |
| country_institution_colonial_affairs_max_investment_add | 殖民事务机构最大投入 | country | additive | good |  |
| country_institution_cost_institution_colonial_affairs_mult | 殖民事务的行政力消耗 | country | multiplicative | percent, bad |  |
| country_institution_cost_institution_health_system_mult | 卫生系统的行政力消耗 | country | multiplicative | percent, bad |  |
| country_institution_cost_institution_home_affairs_mult | 内政事务的行政力消耗 | country | multiplicative | percent, bad |  |
| country_institution_cost_institution_police_mult | 执法的行政力消耗 | country | multiplicative | percent, bad |  |
| country_institution_cost_institution_schools_mult | 教育的行政力消耗 | country | multiplicative | percent, bad |  |
| country_institution_cost_institution_social_security_mult | 社会保障的行政力消耗 | country | multiplicative | percent, bad |  |
| country_institution_health_system_max_investment_add | 卫生系统机构最大投入 | country | additive | good |  |
| country_institution_home_affairs_max_investment_add | 内政事务机构最大投入 | country | additive | good |  |
| country_institution_impact_institution_health_system_mult | 卫生系统的影响 | country | multiplicative | percent, good |  |
| country_institution_police_max_investment_add | 执法机构最大投入 | country | additive | good |  |
| country_institution_schools_max_investment_add | 教育机构最大投入 | country | additive | good |  |
| country_institution_size_change_speed_institution_colonial_affairs_mult | 殖民事务的机构规模变化速度 | country | multiplicative | percent, good |  |
| country_institution_size_change_speed_institution_police_mult | 执法的机构规模变化速度 | country | multiplicative | percent, good |  |
| country_institution_size_change_speed_institution_schools_mult | 教育的机构规模变化速度 | country | multiplicative | percent, good |  |
| country_institution_size_change_speed_mult | 机构规模变化速度 | country | multiplicative | percent, good |  |
| country_institution_social_security_max_investment_add | 社会保障机构最大投入 | country | additive | good |  |
| country_institution_workplace_safety_max_investment_add | 劳动安全局机构最大投入 | country | additive | good |  |
| country_je_korea_action_cost | country_je_korea_action_cost | country |  | percent, bad |  |
| country_join_power_bloc_member_in_defensive_plays_bool | 可在**防御性**外交博弈中通过“召唤盟友”拉拢召集强权集团成员 | country | boolean | neutral |  |
| country_join_power_bloc_member_in_plays_bool | 可在**所有**外交博弈中通过“召唤盟友”拉拢召集强权集团成员 | country | boolean | neutral |  |
| country_kshatriyas_acceptance_max_add | 刹帝利社会阶层的最高接纳度 | country | additive | bad |  |
| country_kshatriyas_acceptance_min_add | 刹帝利社会阶层的最低接纳度 | country | additive | good |  |
| country_kshatriyas_cultural_acceptance_mult | 刹帝利社会阶层的文化接纳度 | country | multiplicative | percent, good |  |
| country_kshatriyas_education_access_add | 刹帝利社会阶层的教育机会 | country | additive | good |  |
| country_kshatriyas_education_access_mult | 刹帝利社会阶级的教育机会 | country | multiplicative | percent, good |  |
| country_kshatriyas_qualification_growth_add | 刹帝利社会阶级的资质增长 | country | additive | good |  |
| country_kshatriyas_qualification_growth_mult | 刹帝利社会阶级的资质增长 | country | multiplicative | percent, good |  |
| country_kshatriyas_qualification_growth_other_class_mult | 刹帝利在社会阶级之外的资质增长 | country | multiplicative | percent, good |  |
| country_kshatriyas_qualification_growth_same_class_mult | 刹帝利社会阶级内部的资质增长 | country | multiplicative | percent, good |  |
| country_laborers_pol_str_mult | 劳工的政治力量 | country | multiplicative | percent, neutral |  |
| country_laborers_voting_power_add | 来自劳工选票的政治力量 | country | additive | neutral | 基于对象 启用选举 |
| country_law_enactment_imposition_success_add | 强制推行法律成功率 | country | additive | percent, good |  |
| country_law_enactment_max_setbacks_add | 法律制定最大挫折数 | country | additive | good |  |
| country_law_enactment_speed_mult | 制定速度 | country | multiplicative | percent, good |  |
| country_law_enactment_stall_add | 制定停滞几率 | country | additive | percent, bad |  |
| country_law_enactment_stall_mult | 制定停滞几率 | country | multiplicative | percent, bad |  |
| country_law_enactment_success_add | 制定成功率 | country | additive | percent, good |  |
| country_leader_has_law_enactment_success_mult | 强权集团法律协同 | country | multiplicative | percent, good |  |
| country_legitimacy_base_add | 合法性 | country | additive | good |  |
| country_legitimacy_govt_leader_clout_add | 基于政府领袖政治力量的合法性 | country | additive | good |  |
| country_legitimacy_govt_size_add | 政府规模容许量 | country | additive | good |  |
| country_legitimacy_govt_total_clout_add | 基于政府政治力量的合法性 | country | additive | good |  |
| country_legitimacy_govt_total_votes_add | 基于选票的合法性 | country | additive | good |  |
| country_legitimacy_headofstate_add | 将国家元首纳入政府所带来的合法性 | country | additive | good |  |
| country_legitimacy_ideological_incoherence_mult | 意识形态不相容造成的合法性惩罚 | country | multiplicative | percent, bad |  |
| country_legitimacy_min_add | 最低合法性 | country | additive | neutral |  |
| country_leverage_generation_add | 杠杆值产生 | country | additive | good |  |
| country_leverage_generation_mult | 杠杆值产生 | country | multiplicative | percent, good |  |
| country_leverage_resistance_add | 杠杆值抵抗 | country | additive | neutral |  |
| country_leverage_resistance_mult | 杠杆值抵抗 | country | multiplicative | percent, neutral |  |
| country_liberty_desire_add | 每周独立倾向 | country | additive | neutral |  |
| country_liberty_desire_decrease_mult | 每周独立倾向降低 | country | multiplicative | percent, neutral |  |
| country_liberty_desire_increase_mult | 每周独立倾向提升 | country | multiplicative | percent, neutral |  |
| country_liberty_desire_of_subjects_add | 所有附属国的每周独立倾向 | country | additive | neutral |  |
| country_limit_officers_qualifications_to_upper_strata | 军官资质限于上层阶级 | country | boolean | neutral |  |
| country_loan_interest_rate_add | 贷款利率 | country | additive | percent, bad |  |
| country_loan_interest_rate_mult | 贷款利率 | country | multiplicative | percent, bad |  |
| country_lobby_leverage_generation_mult | 来自政治游说团的杠杆值产生 | country | multiplicative | percent, good |  |
| country_lobby_support | 游说团支持 | country |  | good |  |
| country_loyalism_increases_cultural_erasure_mult | 文化抹除地位下的忠诚度增长 | country | multiplicative | percent, good |  |
| country_loyalism_increases_full_acceptance_mult | 完全接纳地位下的忠诚度增长 | country | multiplicative | percent, good |  |
| country_loyalism_increases_open_prejudice_mult | 公开偏见地位下的忠诚度增长 | country | multiplicative | percent, good |  |
| country_loyalism_increases_second_rate_citizen_mult | 二等公民地位下的忠诚度增长 | country | multiplicative | percent, good |  |
| country_loyalism_increases_violent_hostility_mult | 暴力敌视地位下的忠诚度增长 | country | multiplicative | percent, good |  |
| country_loyalists_from_legitimacy_mult | 高合法性带来的忠诚派 | country | multiplicative | percent, good |  |
| country_machinists_pol_str_mult | 机器操作员的政治力量 | country | multiplicative | percent, neutral |  |
| country_machinists_voting_power_add | 来自机器操作员选票的政治力量 | country | additive | neutral | 基于对象 启用选举 |
| country_mass_migration_attraction_mult | 大规模迁移吸引力 | country | multiplicative | percent, good |  |
| country_max_companies_add | 最大公司数量 | country | additive | good |  |
| country_max_unassigned_admirals_add | 最大闲置海军上将数 | country | additive | good |  |
| country_max_unassigned_generals_add | 最大闲置将军数 | country | additive | good |  |
| country_max_weekly_construction_progress_add | 每周最大建造进度 | country | additive | good |  |
| country_migration_restrictiveness_add | 迁移限制性 | country | additive | neutral |  |
| country_military_goods_cost_mult | 军用商品成本 | country | multiplicative | percent, bad |  |
| country_military_tech_research_speed_mult | 军事研究速度 | country | multiplicative | percent, good |  |
| country_military_tech_spread_mult | 军事技术扩散 | country | multiplicative | percent, good |  |
| country_military_wages_mult | 军队工资 | country | multiplicative | percent, neutral |  |
| country_minting_add | 铸币 | country | additive | good |  |
| country_minting_mult | 铸币 | country | multiplicative | percent, good |  |
| country_must_have_movement_to_enact_laws_bool | 制定法律必须有政治运动 | country | boolean | bad |  |
| country_nationalization_cost_non_members_mult | 国有化成本 | country | multiplicative | percent, bad |  |
| country_navy_goods_cost_mult | 海军商品成本 | country | multiplicative | percent, bad |  |
| country_no_advantage_loss_from_lack_of_interest_bool | 无视因缺少利益而受到的贸易优势惩罚 | country | boolean | good |  |
| country_non_state_religion_wages_mult | 非国教人口的工资 | country | multiplicative | percent, neutral |  |
| country_officers_pol_str_mult | 军官的政治力量 | country | multiplicative | percent, neutral |  |
| country_officers_voting_power_add | 来自军官选票的政治力量 | country | additive | neutral | 基于对象 启用选举 |
| country_opposition_ig_approval_add | 反对党利益集团认可度 | country | additive | good |  |
| country_overlord_income_transfer_mult | 宗主国收入转移 | country | multiplicative | percent, bad |  |
| country_pact_leverage_generation_add | 来自外交条约的杠杆值产生 | country | additive | good |  |
| country_pact_leverage_generation_mult | 来自外交条约的杠杆值产生 | country | multiplicative | percent, good |  |
| country_party_whip_impact_add | 政党党鞭对意识形态混乱的影响 | country | additive | percent, good |  |
| country_peasants_pol_str_mult | 农民的政治力量 | country | multiplicative | percent, neutral |  |
| country_peasants_voting_power_add | 来自农民选票的政治力量 | country | additive | neutral | 基于对象 启用选举 |
| country_piracy_income_add | 海盗收入 | country | additive | percent, good |  |
| country_political_strength_cultural_erasure_mult | 文化抹除地位下的政治力量 | country | multiplicative | percent, good |  |
| country_political_strength_full_acceptance_mult | 完全接纳地位下的政治力量 | country | multiplicative | percent, good |  |
| country_political_strength_open_prejudice_mult | 公开偏见地位下的政治力量 | country | multiplicative | percent, good |  |
| country_political_strength_second_rate_citizen_mult | 二等公民地位下的政治力量 | country | multiplicative | percent, good |  |
| country_political_strength_violent_hostility_mult | 暴力敌视地位下的政治力量 | country | multiplicative | percent, good |  |
| country_port_connection_cost_mult | 港口连接的商船队成本 | country | multiplicative | percent, bad |  |
| country_prestige_add | 威望 | country | additive | good |  |
| country_prestige_from_army_power_projection_mult | 来自陆军力量投射的威望 | country | multiplicative | percent, good |  |
| country_prestige_from_navy_power_projection_mult | 来自海军力量投射的威望 | country | multiplicative | percent, good |  |
| country_prestige_mult | 威望 | country | multiplicative | percent, good |  |
| country_primary_culture_fervor_from_laws_add | 法律带来的主流文化狂热 | country | additive | neutral |  |
| country_private_construction_allocation_mult | 私人建造分配 | country | multiplicative | percent, neutral |  |
| country_production_tech_research_speed_mult | 生产研究速度 | country | multiplicative | percent, good |  |
| country_production_tech_spread_mult | 生产技术扩散 | country | multiplicative | percent, good |  |
| country_qualification_growth_cultural_erasure_mult | 文化抹除地位下的资质提升 | country | multiplicative | percent, good |  |
| country_qualification_growth_full_acceptance_mult | 完全接纳地位下的资质提升 | country | multiplicative | percent, good |  |
| country_qualification_growth_open_prejudice_mult | 公开偏见地位下的资质提升 | country | multiplicative | percent, good |  |
| country_qualification_growth_second_rate_citizen_mult | 二等公民地位下的资质提升 | country | multiplicative | percent, good |  |
| country_qualification_growth_violent_hostility_mult | 暴力敌视地位下的资质提升 | country | multiplicative | percent, good |  |
| country_radicalism_increases_cultural_erasure_mult | 文化抹除地位下的激进主义增长 | country | multiplicative | percent, bad |  |
| country_radicalism_increases_full_acceptance_mult | 完全接纳地位下的激进主义增长 | country | multiplicative | percent, bad |  |
| country_radicalism_increases_open_prejudice_mult | 公开偏见地位下的激进主义增长 | country | multiplicative | percent, bad |  |
| country_radicalism_increases_second_rate_citizen_mult | 二等公民地位下的激进主义增长 | country | multiplicative | percent, bad |  |
| country_radicalism_increases_violent_hostility_mult | 暴力敌视地位下的激进主义增长 | country | multiplicative | percent, bad |  |
| country_radicals_from_conquest_mult | 征服带来的激进派 | country | multiplicative | percent, bad |  |
| country_radicals_from_legitimacy_mult | 低合法性带来的激进派 | country | multiplicative | percent, bad |  |
| country_reduced_liberty_desire_same_religion_bool | 同宗教独立倾向降低 | country | boolean | good |  |
| country_resource_depletion_chance_mult | 资源枯竭几率 | country | multiplicative | percent, bad |  |
| country_resource_discovery_chance_mult | 资源发现几率 | country | multiplicative | percent, good |  |
| country_revolution_clock_time_add | 革命倒计时时间 | country | additive | neutral |  |
| country_revolution_progress_add | 革命进展速度 | country | additive | percent, bad |  |
| country_revolution_progress_mult | 革命进展速度 | country | multiplicative | percent, bad |  |
| country_sailors_max_add | 最大水手数 | country | additive | good |  |
| country_secession_clock_time_add | 脱离倒计时时间 | country | additive | neutral |  |
| country_secession_progress_add | 脱离进展速度 | country | additive | percent, bad |  |
| country_secession_progress_mult | 脱离进展速度 | country | multiplicative | percent, bad |  |
| country_ship_construction_add | 舰船建造 | country | additive | good |  |
| country_ship_construction_efficiency_add | 舰船建造效率 | country | additive | percent, good |  |
| country_ship_construction_goods_cost_mult | 舰船建造成本 | country | multiplicative | percent, bad |  |
| country_ship_construction_progress_max_add | 最大舰船建造进度 | country | additive | good |  |
| country_ship_crew_starting_veterancy_experience_add | 舰员初始经验 | country | additive | good |  |
| country_ship_crew_starting_veterancy_experience_mult | 舰员初始经验 | country | multiplicative | percent, good |  |
| country_ship_group_capital_ships_construction_efficiency_add | 主力舰建造效率 | country | additive | percent, good |  |
| country_ship_group_capital_ships_construction_progress_max_add | 主力舰最大建造进度 | country | additive | good |  |
| country_ship_group_capital_ships_construction_progress_max_mult | 主力舰最大建造进度 | country | multiplicative | percent, good |  |
| country_ship_group_cruisers_construction_efficiency_add | 巡洋舰建造效率 | country | additive | percent, good |  |
| country_ship_group_cruisers_construction_progress_max_add | 巡洋舰最大建造进度 | country | additive | good |  |
| country_ship_group_cruisers_construction_progress_max_mult | 巡洋舰最大建造进度 | country | multiplicative | percent, good |  |
| country_ship_group_supply_ships_construction_efficiency_add | 补给舰建造效率 | country | additive | percent, good |  |
| country_ship_group_torpedo_craft_construction_efficiency_add | 雷击舰建造效率 | country | additive | percent, good |  |
| country_ship_group_torpedo_craft_construction_progress_max_add | 雷击舰最大建造进度 | country | additive | good |  |
| country_ship_group_torpedo_craft_construction_progress_max_mult | 雷击舰最大建造进度 | country | multiplicative | percent, good |  |
| country_ship_type_armored_cruiser_construction_efficiency_add | 装甲巡洋舰建造效率 | country | additive | percent, good |  |
| country_ship_type_light_cruiser_construction_efficiency_add | 轻巡洋舰建造效率 | country | additive | percent, good |  |
| country_ship_type_protected_cruiser_construction_efficiency_add | 防护巡洋舰建造效率 | country | additive | percent, good |  |
| country_ship_type_troop_ship_construction_efficiency_add | 运兵船建造效率 | country | additive | percent, good |  |
| country_shopkeepers_pol_str_mult | 店主的政治力量 | country | multiplicative | percent, neutral |  |
| country_shopkeepers_voting_power_add | 来自店主选票的政治力量 | country | additive | neutral | 基于对象 启用选举 |
| country_shudras_acceptance_max_add | 首陀罗社会阶级的最大接纳度 | country | additive | bad |  |
| country_shudras_cultural_acceptance_mult | 首陀罗社会阶级的文化接纳度 | country | multiplicative | percent, good |  |
| country_shudras_education_access_add | 首陀罗社会阶级的教育机会 | country | additive | good |  |
| country_shudras_education_access_mult | 首陀罗社会阶级的教育机会 | country | multiplicative | percent, good |  |
| country_shudras_qualification_growth_add | 首陀罗社会阶级的资质增长 | country | additive | good |  |
| country_shudras_qualification_growth_mult | 首陀罗社会阶级的资质增长 | country | multiplicative | percent, good |  |
| country_shudras_qualification_growth_other_class_mult | 首陀罗在社会阶级之外的资质增长 | country | multiplicative | percent, good |  |
| country_shudras_qualification_growth_same_class_mult | 首陀罗社会阶级内部的资质增长 | country | multiplicative | percent, good |  |
| country_slaves_voting_power_add | 来自奴隶选票的政治力量 | country | additive | neutral | 基于对象 启用选举 |
| country_society_tech_research_speed_mult | 社会研究速度 | country | multiplicative | percent, good |  |
| country_society_tech_spread_mult | 社会技术扩散 | country | multiplicative | percent, good |  |
| country_soldiers_pol_str_mult | 军人的政治力量 | country | multiplicative | percent, neutral |  |
| country_soldiers_voting_power_add | 来自军人选票的政治力量 | country | additive | neutral | 基于对象 启用选举 |
| country_standard_of_living_cultural_erasure_add | 文化抹除地位下的生活水平 | country | additive | good |  |
| country_standard_of_living_full_acceptance_add | 完全接纳地位下的生活水平 | country | additive | good |  |
| country_standard_of_living_open_prejudice_add | 公开偏见地位下的生活水平 | country | additive | good |  |
| country_standard_of_living_second_rate_citizen_add | 二等公民地位下的生活水平 | country | additive | good |  |
| country_standard_of_living_violent_hostility_add | 暴力敌视地位下的生活水平 | country | additive | good |  |
| country_state_religion_wages_mult | 国教人口的工资 | country | multiplicative | percent, neutral |  |
| country_strata_commoners_peasants_acceptance_max_add | 百姓社会阶级的最大接纳度 | country | additive | bad |  |
| country_strata_commoners_peasants_acceptance_min_add | 百姓社会阶级的最低接纳度 | country | additive | good |  |
| country_strata_commoners_peasants_cultural_acceptance_mult | 百姓社会阶级的文化接纳度 | country | multiplicative | percent, good |  |
| country_strata_commoners_peasants_education_access_add | 百姓社会阶级的教育机会 | country | additive | good |  |
| country_strata_commoners_peasants_education_access_mult | 百姓社会阶级的教育机会 | country | multiplicative | percent, good |  |
| country_strata_commoners_peasants_qualification_growth_add | 百姓社会阶级的资质增长 | country | additive | good |  |
| country_strata_commoners_peasants_qualification_growth_mult | 百姓社会阶级的资质增长 | country | multiplicative | percent, good |  |
| country_strata_commoners_peasants_qualification_growth_other_class_mult | 百姓在社会阶级之外的资质增长 | country | multiplicative | percent, good |  |
| country_strata_commoners_peasants_qualification_growth_same_class_mult | 百姓社会阶级内部的资质增长 | country | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_acceptance_max_add | 町人社会阶级的最大接纳度 | country | additive | bad |  |
| country_strata_commoners_townspeople_acceptance_min_add | 町人社会阶级的最低接纳度 | country | additive | good |  |
| country_strata_commoners_townspeople_cultural_acceptance_mult | 町人社会阶级的文化接纳度 | country | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_education_access_add | 町人社会阶级的教育机会 | country | additive | good |  |
| country_strata_commoners_townspeople_education_access_mult | 町人社会阶级的教育机会 | country | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_qualification_growth_add | 町人社会阶级的资质增长 | country | additive | good |  |
| country_strata_commoners_townspeople_qualification_growth_mult | 町人社会阶级的资质增长 | country | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_qualification_growth_other_class_mult | 町人在社会阶级之外的资质增长 | country | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_qualification_growth_same_class_mult | 町人社会阶级内部的资质增长 | country | multiplicative | percent, good |  |
| country_strata_outcastes_acceptance_max_add | 秽多非人社会阶级的最大接纳度 | country | additive | bad |  |
| country_strata_outcastes_acceptance_min_add | 秽多非人社会阶级的最低接纳度 | country | additive | good |  |
| country_strata_outcastes_cultural_acceptance_mult | 秽多非人社会阶级的文化接纳度 | country | multiplicative | percent, good |  |
| country_strata_outcastes_education_access_add | 秽多非人社会阶级的教育机会 | country | additive | good |  |
| country_strata_outcastes_education_access_mult | 秽多非人社会阶级的教育机会 | country | multiplicative | percent, good |  |
| country_strata_outcastes_qualification_growth_add | 秽多非人社会阶级的资质增长 | country | additive | good |  |
| country_strata_outcastes_qualification_growth_mult | 秽多非人社会阶级的资质增长 | country | multiplicative | percent, good |  |
| country_strata_outcastes_qualification_growth_other_class_mult | 秽多非人在社会阶级之外的资质增长 | country | multiplicative | percent, good |  |
| country_strata_outcastes_qualification_growth_same_class_mult | 秽多非人社会阶级内部的资质增长 | country | multiplicative | percent, good |  |
| country_strata_religious_acceptance_max_add | 寺社社会阶级的最大接纳度 | country | additive | bad |  |
| country_strata_religious_acceptance_min_add | 寺社社会阶级的最低接纳度 | country | additive | good |  |
| country_strata_religious_cultural_acceptance_mult | 寺社社会阶级的文化接纳度 | country | multiplicative | percent, good |  |
| country_strata_religious_education_access_add | 寺社社会阶级的教育机会 | country | additive | good |  |
| country_strata_religious_education_access_mult | 寺社社会阶级的教育机会 | country | multiplicative | percent, good |  |
| country_strata_religious_qualification_growth_add | 寺社社会阶级的资质增长 | country | additive | good |  |
| country_strata_religious_qualification_growth_mult | 寺社社会阶级的资质增长 | country | multiplicative | percent, good |  |
| country_strata_religious_qualification_growth_other_class_mult | 寺社在社会阶级之外的资质增长 | country | multiplicative | percent, good |  |
| country_strata_religious_qualification_growth_same_class_mult | 寺社社会阶级内部的资质增长 | country | multiplicative | percent, good |  |
| country_strata_samurai_high_acceptance_max_add | 上级武士社会阶级的最大接纳度 | country | additive | bad |  |
| country_strata_samurai_high_acceptance_min_add | 上层武士社会阶层的最低接纳度 | country | additive | good |  |
| country_strata_samurai_high_cultural_acceptance_mult | 上层武士社会阶层的文化接纳度 | country | multiplicative | percent, good |  |
| country_strata_samurai_high_education_access_add | 上层武士社会阶层的教育机会 | country | additive | good |  |
| country_strata_samurai_high_education_access_mult | 上层武士社会阶层的教育机会 | country | multiplicative | percent, good |  |
| country_strata_samurai_high_qualification_growth_add | 上层武士社会阶层的资质增长 | country | additive | good |  |
| country_strata_samurai_high_qualification_growth_mult | 上层武士社会阶层的资质增长 | country | multiplicative | percent, good |  |
| country_strata_samurai_high_qualification_growth_other_class_mult | 上层武士在武士上层阶层以外的资质增长 | country | multiplicative | percent, good |  |
| country_strata_samurai_high_qualification_growth_same_class_mult | 上层武士社会阶层内部的资质增长 | country | multiplicative | percent, good |  |
| country_strata_samurai_low_acceptance_max_add | 下层武士社会阶层的最高接纳度 | country | additive | bad |  |
| country_strata_samurai_low_acceptance_min_add | 下层武士社会阶层的最低接纳度 | country | additive | good |  |
| country_strata_samurai_low_cultural_acceptance_mult | 下层武士社会阶层的文化接纳度 | country | multiplicative | percent, good |  |
| country_strata_samurai_low_education_access_add | 下层武士社会阶层的教育机会 | country | additive | good |  |
| country_strata_samurai_low_education_access_mult | 下层武士社会阶层的教育机会 | country | multiplicative | percent, good |  |
| country_strata_samurai_low_qualification_growth_add | 下层武士社会阶层的资质增长 | country | additive | good |  |
| country_strata_samurai_low_qualification_growth_mult | 下层武士社会阶层的资质增长 | country | multiplicative | percent, good |  |
| country_strata_samurai_low_qualification_growth_other_class_mult | 下层武士在武士下层阶层以外的资质增长 | country | multiplicative | percent, good |  |
| country_strata_samurai_low_qualification_growth_same_class_mult | 下层武士社会阶层内部的资质增长 | country | multiplicative | percent, good |  |
| country_subject_income_transfer_heathen_mult | 来自异教附属国的收入转移 | country | multiplicative | percent, good |  |
| country_subject_income_transfer_mult | 来自附属国的收入转移 | country | multiplicative | percent, good |  |
| country_supply_ship_construction_progress_max_add | 补给船最大建造进度 | country | additive | good |  |
| country_supply_ship_construction_progress_max_mult | 补给船最大建造进度 | country | multiplicative | percent, good |  |
| country_supply_ship_construction_ratio_add | 补给船建造比例 | country | additive | percent, good |  |
| country_support_independence_weekly_liberty_desire_add | 支持独立带来的每周独立倾向 | country | additive | neutral |  |
| country_support_separatism_resistance_mult | 支持分离主义抵抗 | country | multiplicative | percent, good |  |
| country_support_separatism_strength_mult | 支持分离主义强度 | country | multiplicative | percent, good |  |
| country_suppression_attraction_factor | 镇压对政治运动吸引力的影响 | country | multiplicative | percent, bad |  |
| country_suppression_cost_mult | 镇压花费 | country | multiplicative | percent, bad |  |
| country_tax_income_add | 税收收入 | country | additive | good |  |
| country_tech_group_research_speed_mult | 集团的技术研究速度 | country | multiplicative | percent, good |  |
| country_tech_research_speed_mult | 技术研究速度 | country | multiplicative | percent, good |  |
| country_tech_spread_add | 技术扩散 | country | additive | good |  |
| country_tech_spread_mult | 技术扩散 | country | multiplicative | percent, good |  |
| country_tension_decay_mult | 紧张度衰减 | country | multiplicative | percent, good |  |
| country_treaty_leverage_generation_add | 来自条约的筹码获取 | country | additive | good |  |
| country_treaty_leverage_generation_mult | 来自条约的筹码获取 | country | multiplicative | percent, good |  |
| country_two_spains_conservative_drift_add | **两个西班牙**保守派进度 | country | additive | good |  |
| country_two_spains_liberal_drift_add | **两个西班牙**自由派进度 | country | additive | good |  |
| country_vaishyas_acceptance_max_add | 吠舍社会阶层的最高接纳度 | country | additive | bad |  |
| country_vaishyas_acceptance_min_add | 吠舍社会阶层的最低接纳度 | country | additive | good |  |
| country_vaishyas_cultural_acceptance_mult | 吠舍社会阶层的文化接纳度 | country | multiplicative | percent, good |  |
| country_vaishyas_education_access_add | 吠舍社会阶层的教育机会 | country | additive | good |  |
| country_vaishyas_education_access_mult | 吠舍社会阶层的教育机会 | country | multiplicative | percent, good |  |
| country_vaishyas_qualification_growth_add | 吠舍社会阶层的资质增长 | country | additive | good |  |
| country_vaishyas_qualification_growth_mult | 吠舍社会阶层的资质增长 | country | multiplicative | percent, good |  |
| country_vaishyas_qualification_growth_other_class_mult | 吠舍在吠舍社会阶层以外的资质增长 | country | multiplicative | percent, good |  |
| country_vaishyas_qualification_growth_same_class_mult | 吠舍社会阶层内部的资质增长 | country | multiplicative | percent, good |  |
| country_voting_power_base_add | 每张选票的政治力量 | country | additive | neutral | 硬编码 启用选举 |
| country_voting_power_cultural_erasure_mult | 文化灭绝状态下政治力量的投票贡献 | country | multiplicative | percent, neutral |  |
| country_voting_power_from_literacy_add | 来自识字人口选票的政治力量 | country | additive | neutral | 硬编码 启用选举 |
| country_voting_power_full_acceptance_mult | 完全接纳状态下政治力量的投票贡献 | country | multiplicative | percent, neutral |  |
| country_voting_power_mult | 每张选票的政治力量 | country | multiplicative | percent, neutral |  |
| country_voting_power_open_prejudice_mult | 公开偏见状态下政治力量的投票贡献 | country | multiplicative | percent, neutral |  |
| country_voting_power_second_rate_citizen_mult | 二等公民状态下政治力量的投票贡献 | country | multiplicative | percent, neutral |  |
| country_voting_power_violent_hostility_mult | 暴力敌视状态下政治力量的投票贡献 | country | multiplicative | percent, neutral |  |
| country_voting_power_wealth_threshold_add | 投票的财富门槛 | country | additive | neutral | 硬编码 启用选举 |
| country_wage_cultural_erasure_mult | 文化灭绝状态下的工资 | country | multiplicative | percent, good |  |
| country_wage_full_acceptance_mult | 完全接纳状态下的工资 | country | multiplicative | percent, good |  |
| country_wage_open_prejudice_mult | 公开偏见状态下的工资 | country | multiplicative | percent, good |  |
| country_wage_second_rate_citizen_mult | 二等公民状态下的工资 | country | multiplicative | percent, good |  |
| country_wage_violent_hostility_mult | 暴力敌视状态下的工资 | country | multiplicative | percent, good |  |
| country_war_exhaustion_casualties_mult | 伤亡带来的厌战度 | country | multiplicative | percent, bad |  |
| country_weekly_innovation_add | 创新 | country | additive | good |  |
| country_weekly_innovation_max_add | 最大创新投入 | country | additive | good |  |
| country_weekly_innovation_mult | 创新 | country | multiplicative | percent, good |  |
| country_yankee_and_dixie_cultures_obsessed_with_guns | 扬基与迪克西文化获得对轻武器的痴迷 | country | boolean | neutral |  |
| dummy_modifier_type | 此 modifier 类型绝不应被使用 |  |  | bad |  |
| goods_input_aeroplanes_add | 飞机投入 | goods | additive | bad |  |
| goods_input_ammunition_add | 弹药投入 | goods | additive | bad |  |
| goods_input_ammunition_mult | 弹药投入 | goods | multiplicative | percent, bad |  |
| goods_input_artillery_add | 火炮投入 | goods | additive | bad |  |
| goods_input_artillery_mult | 火炮投入 | goods | multiplicative | percent, bad |  |
| goods_input_automobiles_add | 汽车投入 | goods | additive | bad |  |
| goods_input_clippers_add | 快速帆船投入 | goods | additive | bad |  |
| goods_input_clothes_add | 衣物投入 | goods | additive | bad |  |
| goods_input_coal_add | 煤炭投入 | goods | additive | bad |  |
| goods_input_dye_add | 染料投入 | goods | additive | bad |  |
| goods_input_electricity_add | 电力投入 | goods | additive | bad |  |
| goods_input_engines_add | 发动机投入 | goods | additive | bad |  |
| goods_input_explosives_add | 炸药投入 | goods | additive | bad |  |
| goods_input_fabric_add | 布匹投入 | goods | additive | bad |  |
| goods_input_fertilizer_add | 肥料投入 | goods | additive | bad |  |
| goods_input_fish_add | 鱼类投入 | goods | additive | bad |  |
| goods_input_fruit_add | 水果投入 | goods | additive | bad |  |
| goods_input_glass_add | 玻璃投入 | goods | additive | bad |  |
| goods_input_grain_add | 谷物投入 | goods | additive | bad |  |
| goods_input_groceries_add | 食品杂货投入 | goods | additive | bad |  |
| goods_input_hardwood_add | 硬木投入 | goods | additive | bad |  |
| goods_input_iron_add | 铁投入 | goods | additive | bad |  |
| goods_input_ironclads_add | 铁甲舰投入 | goods | additive | bad |  |
| goods_input_lead_add | 铅投入 | goods | additive | bad |  |
| goods_input_liquor_add | 烈酒投入 | goods | additive | bad |  |
| goods_input_manowars_add | 风帆战列舰投入 | goods | additive | bad |  |
| goods_input_meat_add | 肉类投入 | goods | additive | bad |  |
| goods_input_merchant_marine_add | 商船队投入 | goods | additive | bad |  |
| goods_input_oil_add | 石油投入 | goods | additive | bad |  |
| goods_input_oil_mult | 石油投入 | goods | multiplicative | percent, bad |  |
| goods_input_opium_add | 鸦片投入 | goods | additive | bad |  |
| goods_input_paper_add | 纸张投入 | goods | additive | bad |  |
| goods_input_radios_add | 收音机投入 | goods | additive | bad |  |
| goods_input_radios_mult | 收音机投入 | goods | multiplicative | percent, bad |  |
| goods_input_rubber_add | 橡胶投入 | goods | additive | bad |  |
| goods_input_silk_add | 高级丝绸投入 | goods | additive | bad |  |
| goods_input_small_arms_add | 轻武器投入 | goods | additive | bad |  |
| goods_input_small_arms_mult | 轻武器投入 | goods | multiplicative | percent, bad |  |
| goods_input_steamers_add | 蒸汽船投入 | goods | additive | bad |  |
| goods_input_steel_add | 钢铁投入 | goods | additive | bad |  |
| goods_input_sugar_add | 糖投入 | goods | additive | bad |  |
| goods_input_sulfur_add | 硫磺投入 | goods | additive | bad |  |
| goods_input_tanks_add | 坦克投入 | goods | additive | bad |  |
| goods_input_tanks_mult | 坦克投入 | goods | multiplicative | percent, bad |  |
| goods_input_telephones_add | 电话投入 | goods | additive | bad |  |
| goods_input_tobacco_add | 烟草投入 | goods | additive | bad |  |
| goods_input_tools_add | 工具投入 | goods | additive | bad |  |
| goods_input_transportation_add | 运输投入 | goods | additive | bad |  |
| goods_input_wine_add | 葡萄酒投入 | goods | additive | bad |  |
| goods_input_wood_add | 木材投入 | goods | additive | bad |  |
| goods_output_aeroplanes_add | 飞机产出 | goods | additive | good |  |
| goods_output_aeroplanes_mult | 建筑飞机产出 | goods | multiplicative | percent, good |  |
| goods_output_ammunition_add | 弹药产出 | goods | additive | good |  |
| goods_output_ammunition_mult | 建筑弹药产出 | goods | multiplicative | percent, good |  |
| goods_output_artillery_add | 火炮产出 | goods | additive | good |  |
| goods_output_artillery_mult | 建筑火炮产出 | goods | multiplicative | percent, good |  |
| goods_output_automobiles_add | 汽车产出 | goods | additive | good |  |
| goods_output_automobiles_mult | 建筑汽车产出 | goods | multiplicative | percent, good |  |
| goods_output_clippers_add | 快速帆船产出 | goods | additive | good |  |
| goods_output_clippers_mult | 建筑快速帆船产出 | goods | multiplicative | percent, good |  |
| goods_output_clothes_add | 衣物产出 | goods | additive | good |  |
| goods_output_coal_add | 煤炭产出 | goods | additive | good |  |
| goods_output_coffee_add | 咖啡产出 | goods | additive | good |  |
| goods_output_dye_add | 染料产出 | goods | additive | good |  |
| goods_output_electricity_add | 电力产出 | goods | additive | good |  |
| goods_output_electricity_mult | 建筑电力产出 | goods | multiplicative | percent, good |  |
| goods_output_engines_add | 发动机产出 | goods | additive | good |  |
| goods_output_engines_mult | 建筑发动机产出 | goods | multiplicative | percent, good |  |
| goods_output_explosives_add | 炸药产出 | goods | additive | good |  |
| goods_output_fabric_add | 布匹产出 | goods | additive | good |  |
| goods_output_fabric_mult | 建筑布匹产出 | goods | multiplicative | percent, good |  |
| goods_output_fertilizer_add | 肥料产出 | goods | additive | good |  |
| goods_output_fine_art_add | 艺术品产出 | goods | additive | good |  |
| goods_output_fish_add | 鱼类产出 | goods | additive | good |  |
| goods_output_fruit_add | 水果产出 | goods | additive | good |  |
| goods_output_fruit_mult | 建筑水果产出 | goods | multiplicative | percent, good |  |
| goods_output_furniture_add | 家具产出 | goods | additive | good |  |
| goods_output_glass_add | 玻璃产出 | goods | additive | good |  |
| goods_output_gold_add | 黄金产出 | goods | additive | good |  |
| goods_output_grain_add | 谷物产出 | goods | additive | good |  |
| goods_output_groceries_add | 食品杂货产出 | goods | additive | good |  |
| goods_output_hardwood_add | 硬木产出 | goods | additive | good |  |
| goods_output_hardwood_mult | 建筑硬木产出 | goods | multiplicative | percent, good |  |
| goods_output_iron_add | 铁产出 | goods | additive | good |  |
| goods_output_ironclads_add | 铁甲舰产出 | goods | additive | good |  |
| goods_output_ironclads_mult | 建筑铁甲舰产出 | goods | multiplicative | percent, good |  |
| goods_output_lead_add | 铅产出 | goods | additive | good |  |
| goods_output_liquor_add | 烈酒产出 | goods | additive | good |  |
| goods_output_liquor_mult | 建筑烈酒产出 | goods | multiplicative | percent, good |  |
| goods_output_luxury_clothes_add | 奢华衣物产出 | goods | additive | good |  |
| goods_output_luxury_furniture_add | 奢华家具产出 | goods | additive | good |  |
| goods_output_manowars_add | 风帆战列舰产出 | goods | additive | good |  |
| goods_output_manowars_mult | 建筑风帆战列舰产出 | goods | multiplicative | percent, good |  |
| goods_output_meat_add | 肉类产出 | goods | additive | good |  |
| goods_output_merchant_marine_add | 商船队产出 | goods | additive | good |  |
| goods_output_oil_add | 石油产出 | goods | additive | good |  |
| goods_output_oil_mult | 建筑石油产出 | goods | multiplicative | percent, good |  |
| goods_output_opium_add | 鸦片产出 | goods | additive | good |  |
| goods_output_paper_add | 纸张产出 | goods | additive | good |  |
| goods_output_porcelain_add | 瓷器产出 | goods | additive | good |  |
| goods_output_radios_add | 收音机产出 | goods | additive | good |  |
| goods_output_radios_mult | 建筑收音机产出 | goods | multiplicative | percent, good |  |
| goods_output_rubber_add | 橡胶产出 | goods | additive | good |  |
| goods_output_services_add | 服务产出 | goods | additive | good |  |
| goods_output_silk_add | 高级丝绸产出 | goods | additive | good |  |
| goods_output_silk_mult | 建筑丝绸产出 | goods | multiplicative | percent, good |  |
| goods_output_small_arms_add | 轻武器产出 | goods | additive | good |  |
| goods_output_small_arms_mult | 建筑轻武器产出 | goods | multiplicative | percent, good |  |
| goods_output_steamers_add | 蒸汽船产出 | goods | additive | good |  |
| goods_output_steamers_mult | 建筑蒸汽船产出 | goods | multiplicative | percent, good |  |
| goods_output_steel_add | 钢铁产出 | goods | additive | good |  |
| goods_output_sugar_add | 糖产出 | goods | additive | good |  |
| goods_output_sugar_mult | 建筑糖产出 | goods | multiplicative | percent, good |  |
| goods_output_sulfur_add | 硫磺产出 | goods | additive | good |  |
| goods_output_tanks_add | 坦克产出 | goods | additive | good |  |
| goods_output_tanks_mult | 建筑坦克产出 | goods | multiplicative | percent, good |  |
| goods_output_tea_add | 茶叶产出 | goods | additive | good |  |
| goods_output_telephones_add | 电话产出 | goods | additive | good |  |
| goods_output_tobacco_add | 烟草产出 | goods | additive | good |  |
| goods_output_tools_add | 工具产出 | goods | additive | good |  |
| goods_output_tools_mult | 建筑工具产出 | goods | multiplicative | percent, good |  |
| goods_output_transportation_add | 运输产出 | goods | additive | good |  |
| goods_output_wine_add | 葡萄酒产出 | goods | additive | good |  |
| goods_output_wine_mult | 建筑葡萄酒产出 | goods | multiplicative | percent, good |  |
| goods_output_wood_add | 木材产出 | goods | additive | good |  |
| interest_group_amenability_add | 利益集团顺从度 | interest_group | additive | good |  |
| interest_group_approval_add | 利益集团认可度 | interest_group | additive | good |  |
| interest_group_ig_armed_forces_approval_add | 军队认可度 | interest_group | additive | good |  |
| interest_group_ig_armed_forces_pol_str_mult | 军队政治力量 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_armed_forces_pop_attraction_mult | 军队人口吸引力 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_devout_approval_add | 信教者认可度 | interest_group | additive | good |  |
| interest_group_ig_devout_pol_str_mult | 信教者政治力量 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_devout_pop_attraction_mult | 信教者人口吸引力 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_industrialists_approval_add | 实业家认可度 | interest_group | additive | good |  |
| interest_group_ig_industrialists_pol_str_mult | 实业家政治力量 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_industrialists_pop_attraction_mult | 实业家人口吸引力 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_intelligentsia_approval_add | 知识分子认可度 | interest_group | additive | good |  |
| interest_group_ig_intelligentsia_pol_str_mult | 知识分子政治力量 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_intelligentsia_pop_attraction_mult | 知识分子人口吸引力 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_landowners_approval_add | 地主认可度 | interest_group | additive | good |  |
| interest_group_ig_landowners_pol_str_mult | 地主政治力量 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_landowners_pop_attraction_mult | 地主人口吸引力 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_petty_bourgeoisie_approval_add | 小资产阶级认可度 | interest_group | additive | good |  |
| interest_group_ig_petty_bourgeoisie_pol_str_mult | 小资产阶级政治力量 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_petty_bourgeoisie_pop_attraction_mult | 小资产阶级人口吸引力 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_rural_folk_approval_add | 乡民认可度 | interest_group | additive | good |  |
| interest_group_ig_rural_folk_pol_str_mult | 乡民政治力量 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_rural_folk_pop_attraction_mult | 乡民人口吸引力 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_trade_unions_approval_add | 工会认可度 | interest_group | additive | good |  |
| interest_group_ig_trade_unions_pol_str_mult | 工会政治力量 | interest_group | multiplicative | percent, neutral |  |
| interest_group_ig_trade_unions_pop_attraction_mult | 工会人口吸引力 | interest_group | multiplicative | percent, neutral |  |
| interest_group_in_government_approval_add | 执政府利益集团认可度 | interest_group | additive | good |  |
| interest_group_in_government_attraction_mult | 执政府利益集团的吸引力 | interest_group | multiplicative | percent, neutral |  |
| interest_group_in_opposition_agitator_popularity_add | 反对派鼓动家的人气 | interest_group | additive | good |  |
| interest_group_in_opposition_approval_add | 反对派利益集团认可度 | interest_group | additive | good |  |
| interest_group_pol_str_factor | 利益集团政治力量 | interest_group | multiplicative | percent, good |  |
| interest_group_pol_str_mult | 利益集团政治力量 | interest_group | multiplicative | percent, neutral |  |
| interest_group_pop_attraction_mult | 利益集团人口吸引力 | interest_group | multiplicative | percent, neutral |  |
| military_formation_army_movement_speed_add | 陆军速度 | military_formation | additive | good |  |
| military_formation_army_movement_speed_mult | 陆军速度 | military_formation | multiplicative | percent, good |  |
| military_formation_attrition_risk_add | 损耗风险 | military_formation | additive | percent, bad |  |
| military_formation_attrition_risk_mult | 损耗风险乘数 | military_formation | multiplicative | percent, bad |  |
| military_formation_fleet_movement_speed_add | 舰队速度 | military_formation | additive | good |  |
| military_formation_fleet_movement_speed_mult | 舰队速度 | military_formation | multiplicative | percent, good |  |
| military_formation_interest_gain_mult | 舰队参与度获取 | military_formation | multiplicative | percent, good |  |
| military_formation_mobilization_speed_add | 编队动员速度 | military_formation | additive | good |  |
| military_formation_mobilization_speed_mult | 编队动员速度 | military_formation | multiplicative | percent, good |  |
| military_formation_organization_gain_add | 每日组织度增长 | military_formation | additive | good |  |
| military_formation_organization_gain_mult | 每日组织度增长 | military_formation | multiplicative | percent, good |  |
| political_movement_activism_growth_mult | 政治运动活跃度增长 | political_movement | multiplicative | percent, bad |  |
| political_movement_character_attraction_mult | political_movement_character_attraction_mult | political_movement | multiplicative | percent, neutral |  |
| political_movement_pop_attraction_mult | 政治运动人口吸引力 | political_movement | multiplicative | percent, neutral |  |
| political_movement_radicalism_add | 政治运动活跃度 | political_movement | additive | percent, bad |  |
| political_movement_radicalism_from_enactment_approval_mult | 法律通过带来的政治运动活跃度降低 | political_movement | multiplicative | percent, good |  |
| political_movement_radicalism_from_enactment_disapproval_mult | 法律否决带来的政治运动活跃度提升 | political_movement | multiplicative | percent, bad |  |
| power_bloc_allow_foreign_investment_lower_rank_bool | 允许对强权集团内较低等级成员的外国投资权 | power_bloc | boolean | good |  |
| power_bloc_allow_port_access_bool | 允许强权集团成员之间互相使用港口 | power_bloc | boolean | good |  |
| power_bloc_allow_wider_migration_area_bool | 允许在强权集团内迁移 | power_bloc | boolean | good |  |
| power_bloc_cohesion_add | 强权集团凝聚力 | power_bloc | additive | good |  |
| power_bloc_cohesion_mult | 强权集团凝聚力 | power_bloc | multiplicative | percent, good |  |
| power_bloc_cohesion_per_member_add | 每个强权集团成员的强权集团凝聚力 | power_bloc | additive | good |  |
| power_bloc_customs_union_bool | 关税同盟 | power_bloc | boolean | neutral |  |
| power_bloc_disallow_embargo_bool | 不能对其他强权集团成员实施禁运 | power_bloc | boolean | neutral |  |
| power_bloc_disallow_war_bool | 不能在强权集团成员之间发动或加入战争 | power_bloc | boolean | neutral |  |
| power_bloc_income_transfer_to_leader_factor | 转移给强权集团领袖的收入 | power_bloc | multiplicative | neutral |  |
| power_bloc_invite_acceptance_add | 强权集团邀请接受几率 | power_bloc | additive | good |  |
| power_bloc_invite_acceptance_great_power_add | 列强接受强权集团邀请的几率 | power_bloc | additive | good |  |
| power_bloc_invite_acceptance_major_power_add | 主要政权接受强权集团邀请的几率 | power_bloc | additive | good |  |
| power_bloc_invite_acceptance_minor_power_add | 次要政权接受强权集团邀请的几率 | power_bloc | additive | good |  |
| power_bloc_invite_acceptance_unrecognized_major_power_add | 未受认可的主要政权接受强权集团邀请的几率 | power_bloc | additive | good |  |
| power_bloc_invite_acceptance_unrecognized_regional_power_add | 未受认可的区域政权接受强权集团邀请的几率 | power_bloc | additive | good |  |
| power_bloc_leader_can_add_wargoal_bool | 允许自由添加战争目标 | power_bloc | boolean | neutral |  |
| power_bloc_leader_can_force_state_religion_bool | 允许强推国教 | power_bloc | boolean | neutral |  |
| power_bloc_leader_can_make_subjects_bool | 可**使役**强权集团成员为其附属国 | power_bloc | boolean | neutral |  |
| power_bloc_leader_can_regime_change_bool | 允许强制变更政权 | power_bloc | boolean | neutral |  |
| power_bloc_leader_can_spread_culture_to_pb_bool | 允许在强权集团成员中传播主流文化 | power_bloc | boolean | neutral |  |
| power_bloc_leverage_generation_mult | 影响力（Leverage）生成 | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_mult | 每周委任进度 | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_great_power_member_add | 每个列强带来的委任进度 | power_bloc | additive | good |  |
| power_bloc_mandate_progress_per_great_power_member_mult | 每个列强带来的委任进度 | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_insignificant_power_member_add | 每个无足轻重的政权带来的委任进度 | power_bloc | additive | good |  |
| power_bloc_mandate_progress_per_insignificant_power_member_mult | 每个无足轻重的政权带来的委任进度 | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_major_power_member_add | 每个主要政权带来的委任进度 | power_bloc | additive | good |  |
| power_bloc_mandate_progress_per_major_power_member_mult | 每个主要政权带来的委任进度 | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_minor_power_member_add | 每个次要政权带来的委任进度 | power_bloc | additive | good |  |
| power_bloc_mandate_progress_per_minor_power_member_mult | 每个次要政权带来的委任进度 | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_unrecognized_major_power_member_add | 每个未受认可的主要政权带来的委任进度 | power_bloc | additive | good |  |
| power_bloc_mandate_progress_per_unrecognized_major_power_member_mult | 每个未受认可的主要政权带来的委任进度 | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_unrecognized_power_member_add | 每个未受认可的政权带来的委任进度 | power_bloc | additive | good |  |
| power_bloc_mandate_progress_per_unrecognized_power_member_mult | 每个未受认可的政权带来的委任进度 | power_bloc | multiplicative | percent, good |  |
| power_bloc_mandate_progress_per_unrecognized_regional_power_member_add | 每个未受认可的区域政权带来的委任进度 | power_bloc | additive | good |  |
| power_bloc_mandate_progress_per_unrecognized_regional_power_member_mult | 每个未受认可的区域政权带来的委任进度 | power_bloc | multiplicative | percent, good |  |
| power_bloc_target_sway_cost_mult | 外交博弈目标拉拢行动的花费 | power_bloc | multiplicative | percent, bad |  |
| power_bloc_trade_advantage_add | 强权集团内的贸易优势 | power_bloc | additive | good |  |
| ship_accuracy_add | 精准度 | ship | additive | good |  |
| ship_accuracy_mult | 精准度 | ship | multiplicative | percent, good |  |
| ship_armor_add | 舰船装甲 | ship | additive | good |  |
| ship_armor_mult | 舰船装甲 | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_destroyer_accuracy_add | 对驱逐舰精准度 | ship | additive | percent, good |  |
| ship_battle_against_ship_type_destroyer_accuracy_mult | 对驱逐舰精准度 | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_dreadnought_hull_damage_mult | 对无畏舰船体攻击伤害 | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_modern_ironclad_hull_damage_mult | 对现代铁甲舰船体攻击伤害 | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_pre_dreadnought_hull_damage_mult | 对前无畏舰船体攻击伤害 | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_submarine_accuracy_add | 对潜艇精准度 | ship | additive | percent, good |  |
| ship_battle_against_ship_type_submarine_accuracy_mult | 对潜艇精准度 | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_super_dreadnought_hull_damage_mult | 对超无畏舰船体攻击伤害 | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_torpedo_boat_accuracy_add | 对雷击艇精准度 | ship | additive | percent, good |  |
| ship_battle_against_ship_type_torpedo_boat_accuracy_mult | 对雷击艇精准度 | ship | multiplicative | percent, good |  |
| ship_battle_against_ship_type_torpedo_boat_destroyer_accuracy_add | 对雷击艇驱逐舰精准度 | ship | additive | percent, good |  |
| ship_battle_against_ship_type_torpedo_boat_destroyer_accuracy_mult | 对雷击艇驱逐舰精准度 | ship | multiplicative | percent, good |  |
| ship_battle_condition_accuracy_penalty_mult | 战斗条件精准度惩罚 | ship | multiplicative | percent, good |  |
| ship_blockade_strength_add | 封锁强度 | ship | additive | good |  |
| ship_blockade_strength_mult | 封锁强度 | ship | multiplicative | percent, good |  |
| ship_carrying_capacity_add | 运载容量 | ship | additive | good |  |
| ship_carrying_capacity_mult | 运载容量 | ship | multiplicative | percent, good |  |
| ship_construction_progress_max_add | 最大舰船建造进度 | ship | additive | neutral |  |
| ship_construction_progress_max_mult | 最大舰船建造进度 | ship | multiplicative | percent, good |  |
| ship_crew_damage_add | 船员攻击伤害 | ship | additive | good |  |
| ship_crew_damage_mult | 船员攻击伤害 | ship | multiplicative | percent, good |  |
| ship_crew_experience_gain_add | 舰船船员每周经验获取 | ship | additive | good |  |
| ship_crew_experience_gain_mult | 舰船船员每周经验获取 | ship | multiplicative | percent, good |  |
| ship_crew_max_add | 舰船船员 | ship | additive | good |  |
| ship_crew_max_mult | 舰船船员 | ship | multiplicative | percent, good |  |
| ship_critical_hit_chance_add | 暴击几率 | ship | additive | percent, good |  |
| ship_critical_hit_chance_mult | 暴击几率 | ship | multiplicative | percent, good |  |
| ship_critical_hit_multiplier_add | 暴击伤害 | ship | additive | percent, good |  |
| ship_critical_hit_multiplier_mult | 暴击伤害 | ship | multiplicative | percent, good |  |
| ship_detection_add | 侦测 | ship | additive | good |  |
| ship_detection_mult | 侦测 | ship | multiplicative | percent, good |  |
| ship_hit_points_max_add | 舰船最大耐久 | ship | additive | good |  |
| ship_hit_points_max_mult | 舰船最大耐久 | ship | multiplicative | percent, good |  |
| ship_hull_damage_add | 船体攻击伤害 | ship | additive | good |  |
| ship_hull_damage_mult | 船体攻击伤害 | ship | multiplicative | percent, good |  |
| ship_interest_gain_add | 舰船介入度生成 | ship | additive | good |  |
| ship_interest_gain_mult | 舰船介入度生成 | ship | multiplicative | percent, good |  |
| ship_marine_capacity_add | 海军陆战队容量 | ship | additive | good |  |
| ship_marine_capacity_mult | 海军陆战队容量 | ship | multiplicative | percent, good |  |
| ship_max_distance_to_port_add | 距港口最大距离 | ship | additive | good |  |
| ship_max_distance_to_port_mult | 距港口最大距离 | ship | multiplicative | percent, good |  |
| ship_movement_speed_add | 舰船速度 | ship | additive | good |  |
| ship_movement_speed_mult | 舰船速度 | ship | multiplicative | percent, good |  |
| ship_naval_invasion_efficiency_mult | 海上入侵效率 | ship | multiplicative | percent, good |  |
| ship_readiness_gain_add | 战备度 | ship | additive | good |  |
| ship_readiness_gain_mult | 战备度 | ship | multiplicative | percent, good |  |
| ship_screening_add | 掩护 | ship | additive | good |  |
| ship_screening_mult | 掩护 | ship | multiplicative | percent, good |  |
| ship_ship_type_aircraft_carrier_hull_damage_mult | 航空母舰船体攻击伤害 | ship | multiplicative | percent, good |  |
| ship_ship_type_submarine_hull_damage_mult | 潜艇船体攻击伤害 | ship | multiplicative | percent, good |  |
| ship_ship_type_supply_ship_supply_capacity_mult | 补给舰补给容量 | ship | multiplicative | percent, good |  |
| ship_suffered_accuracy_mult | 承受精准度 | ship | multiplicative | percent, bad |  |
| ship_suffered_crew_damage_mult | 承受船员攻击伤害 | ship | multiplicative | percent, bad |  |
| ship_suffered_crit_chance_mult | 承受暴击几率 | ship | multiplicative | percent, bad |  |
| ship_suffered_crit_damage_mult | 承受暴击伤害 | ship | multiplicative | percent, bad |  |
| ship_suffered_hull_damage_mult | 承受船体攻击伤害 | ship | multiplicative | percent, bad |  |
| ship_supply_capacity_add | 补给容量 | ship | additive | good |  |
| ship_supply_capacity_mult | 补给容量 | ship | multiplicative | percent, good |  |
| ship_supply_efficiency_add | 补给效率 | ship | additive | percent, good |  |
| ship_supply_efficiency_mult | 补给效率 | ship | multiplicative | percent, good |  |
| ship_visibility_add | 可见度 | ship | additive | bad |  |
| ship_visibility_mult | 可见度 | ship | multiplicative | percent, bad |  |
| ship_vulnerability_add | 易受攻击性 | ship | additive | bad |  |
| ship_vulnerability_mult | 易受攻击性 | ship | multiplicative | percent, bad |  |
| state_academics_investment_pool_contribution_add | 学者投资池贡献 | state | additive | percent, good |  |
| state_academics_investment_pool_efficiency_mult | 学者投资池贡献效率 | state | multiplicative | percent, good |  |
| state_academics_mortality_mult | 学者死亡率 | state | multiplicative | percent, bad |  |
| state_allow_assimilation_in_homeland_bool | 允许在本土州进行同化 | state | boolean | good |  |
| state_allow_assimilation_without_presence_bool | 始终允许同化为主流文化 | state | boolean | good |  |
| state_allow_conversion_without_presence_bool | 始终允许改信为国教 | state | boolean | good |  |
| state_aristocrats_investment_pool_contribution_add | 贵族投资池贡献 | state | additive | percent, good |  |
| state_aristocrats_investment_pool_efficiency_mult | 贵族投资池贡献效率 | state | multiplicative | percent, good |  |
| state_aristocrats_mortality_mult | 贵族死亡率 | state | multiplicative | percent, bad |  |
| state_assimilation_mult | 同化 | state | multiplicative | percent, good |  |
| state_birth_rate_mult | 出生率 | state | multiplicative | percent, good |  |
| state_blockade_resistance_add | 封锁抗性 | state | additive | good |  |
| state_building_barrack_max_level_add | 兵营最大等级 | state | additive | good |  |
| state_building_conscription_center_max_level_add | 最大征兵上限 | state | additive | good |  |
| state_building_construction_sector_max_level_add | 建造部门最大等级 | state | additive | good |  |
| state_building_naval_fortification_max_level_add | 海防要塞最大等级 | state | additive | good |  |
| state_bureaucracy_population_base_cost_factor_mult | 行政力人口成本倍率 | state | multiplicative | percent, bad |  |
| state_bureaucrats_investment_pool_contribution_add | 官僚投资池贡献 | state | additive | percent, good |  |
| state_bureaucrats_investment_pool_efficiency_mult | 官僚投资池贡献效率 | state | multiplicative | percent, good |  |
| state_buy_orders_ammunition_add | 弹药购买订单 | state | additive | neutral |  |
| state_buy_orders_artillery_add | 火炮购买订单 | state | additive | neutral |  |
| state_buy_orders_small_arms_add | 轻武器购买订单 | state | additive | neutral |  |
| state_capitalists_investment_pool_contribution_add | 资本家投资池贡献 | state | additive | percent, good |  |
| state_capitalists_investment_pool_efficiency_mult | 资本家投资池贡献效率 | state | multiplicative | percent, good |  |
| state_clergymen_investment_pool_contribution_add | 教士投资池贡献 | state | additive | percent, good |  |
| state_clergymen_investment_pool_efficiency_mult | 教士投资池贡献效率 | state | multiplicative | percent, good |  |
| state_clerks_investment_pool_contribution_add | 职员（Clerks）投资池贡献 | state | additive | percent, good |  |
| state_clerks_investment_pool_efficiency_mult | 职员（Clerks）投资池贡献效率 | state | multiplicative | percent, good |  |
| state_colony_growth_creation_factor | 殖民增长生成 | state | multiplicative | good |  |
| state_colony_growth_speed_mult | 殖民地增长速度 | state | multiplicative | percent, good |  |
| state_conscription_rate_add | 征兵率 | state | additive | percent, good |  |
| state_conscription_rate_mult | 可征募营 | state | multiplicative | percent, good |  |
| state_construction_mult | 州建造效率 | state | multiplicative | percent, good |  |
| state_contiguous_incorporation_speed_mult | 毗邻建州（并入）速度 | state | multiplicative | percent, good |  |
| state_control_strait_bool | 控制海峡 | state | boolean | good |  |
| state_conversion_mult | 皈依 | state | multiplicative | percent, good |  |
| state_decree_cost_mult | 法令花费 | state | multiplicative | percent, bad |  |
| state_dependent_political_participation_add | 受抚养者选举权 | state | additive | percent, good |  |
| state_dependent_wage_add | 受抚养者年收入 | state | additive | good |  |
| state_dependent_wage_mult | 受抚养者收入 | state | multiplicative | percent, good |  |
| state_devastation_decay_mult | 破坏度恢复 | state | multiplicative | percent, good |  |
| state_disallow_incorporation_bool | 州建州（并入）被禁止 | state | boolean | bad |  |
| state_education_access_add | 教育接入 | state | additive | percent, good |  |
| state_education_access_wealth_add | 教育接入（基于财富） | state | additive | percent, good |  |
| state_engineers_investment_pool_contribution_add | 工程师投资池贡献 | state | additive | percent, good |  |
| state_engineers_investment_pool_efficiency_mult | 工程师投资池贡献效率 | state | multiplicative | percent, good |  |
| state_expected_sol_from_literacy | 识字带来的最低预期生活水平 | state |  | bad |  |
| state_expected_sol_mult | 最低预期生活水平 | state | multiplicative | percent, bad |  |
| state_export_advantage_mult | 出口贸易优势 | state | multiplicative | percent, good |  |
| state_farmers_investment_pool_contribution_add | 农场主投资池贡献 | state | additive | percent, good |  |
| state_farmers_investment_pool_efficiency_mult | 农场主投资池贡献效率 | state | multiplicative | percent, good |  |
| state_farmers_mortality_mult | 农场主死亡率 | state | multiplicative | percent, bad |  |
| state_food_security_add | 粮食安全 | state | additive | percent, good |  |
| state_fortification_bombardment_resistance_add | 海防要塞炮击抗性 | state | additive | good |  |
| state_fortification_naval_battle_mult | 海防要塞战斗防御 | state | multiplicative | percent, good |  |
| state_fortification_naval_invasion_add | 海防要塞入侵防御 | state | additive | good |  |
| state_free_state_pop_support_movement_anti_slavery_mult | 非蓄奴州的废奴运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_harvest_condition_disease_outbreak_duration_mult | 疫病爆发收成状况持续时间 | state | multiplicative | percent, bad |  |
| state_harvest_condition_disease_outbreak_impact_mult | 疫病爆发收成状况影响 | state | multiplicative | percent, bad |  |
| state_harvest_condition_drought_duration_mult | 干旱收成状况持续时间 | state | multiplicative | percent, bad |  |
| state_harvest_condition_drought_impact_mult | 干旱收成状况影响 | state | multiplicative | percent, bad |  |
| state_harvest_condition_earthquake_duration_mult | 地震收成状况持续时间 | state | multiplicative | percent, bad |  |
| state_harvest_condition_earthquake_impact_mult | 地震收成状况影响 | state | multiplicative | percent, bad |  |
| state_harvest_condition_extreme_winds_duration_mult | 极端大风收成状况持续时间 | state | multiplicative | percent, bad |  |
| state_harvest_condition_extreme_winds_impact_mult | 极端大风收成状况影响 | state | multiplicative | percent, bad |  |
| state_harvest_condition_flood_duration_mult | 洪水收成状况持续时间 | state | multiplicative | percent, bad |  |
| state_harvest_condition_flood_impact_mult | 洪水收成状况影响 | state | multiplicative | percent, bad |  |
| state_harvest_condition_heatwave_duration_mult | 热浪收成状况持续时间 | state | multiplicative | percent, bad |  |
| state_harvest_condition_heatwave_impact_mult | 热浪收成状况影响 | state | multiplicative | percent, bad |  |
| state_harvest_condition_tsunami_duration_mult | 海啸收成状况持续时间 | state | multiplicative | percent, bad |  |
| state_harvest_condition_tsunami_impact_mult | 海啸收成状况影响 | state | multiplicative | percent, bad |  |
| state_harvest_condition_wildfire_duration_mult | 野火收成状况持续时间 | state | multiplicative | percent, bad |  |
| state_harvest_condition_wildfire_impact_mult | 野火收成状况影响 | state | multiplicative | percent, bad |  |
| state_import_advantage_mult | 进口贸易优势 | state | multiplicative | percent, good |  |
| state_incorporation_speed_mult | 建州（并入）速度 | state | multiplicative | percent, good |  |
| state_infrastructure_add | 基础设施 | state | additive | good |  |
| state_infrastructure_from_automobiles_consumption_add | 人口汽车消费带来的基础设施 | state | additive | good |  |
| state_infrastructure_from_population_add | 每 10 万人口基础设施 | state | additive | good |  |
| state_infrastructure_from_population_max_add | 人口带来的最大基础设施 | state | additive | good |  |
| state_infrastructure_from_population_max_mult | 人口带来的最大基础设施 | state | multiplicative | percent, good |  |
| state_infrastructure_from_population_mult | 每 10 万人口基础设施 | state | multiplicative | percent, good |  |
| state_infrastructure_mult | 基础设施 | state | multiplicative | percent, good |  |
| state_institution_impact_add | 机构影响 | state | additive | percent, good |  |
| state_laborers_investment_pool_contribution_add | 劳工投资池贡献 | state | additive | percent, good |  |
| state_laborers_investment_pool_efficiency_mult | 劳工投资池贡献效率 | state | multiplicative | percent, good |  |
| state_laborers_mortality_mult | 劳工死亡率 | state | multiplicative | percent, bad |  |
| state_literacy_growth_add | 识字率增长 | state | additive | percent, good |  |
| state_lower_strata_expected_sol_add | 下层阶级的最低预期生活水平 | state | additive | neutral |  |
| state_loyalism_increases_cultural_erasure_mult | 文化抹除状态下忠诚派增长 | state | multiplicative | percent, good |  |
| state_loyalism_increases_full_acceptance_mult | 完全接纳状态下忠诚派增长 | state | multiplicative | percent, good |  |
| state_loyalism_increases_open_prejudice_mult | 公开偏见状态下忠诚派增长 | state | multiplicative | percent, good |  |
| state_loyalism_increases_second_rate_citizen_mult | 二等公民状态下忠诚派增长 | state | multiplicative | percent, good |  |
| state_loyalism_increases_violent_hostility_mult | 暴力敌意状态下忠诚派增长 | state | multiplicative | percent, good |  |
| state_loyalists_from_political_movements_mult | 政治运动带来的忠诚派 | state | multiplicative | percent, good |  |
| state_machinists_investment_pool_contribution_add | 机械师投资池贡献 | state | additive | percent, good |  |
| state_machinists_investment_pool_efficiency_mult | 机械师投资池贡献效率 | state | multiplicative | percent, good |  |
| state_machinists_mortality_mult | 机械师死亡率 | state | multiplicative | percent, bad |  |
| state_market_access_price_impact | 市场接入价格影响 | state |  | percent, neutral |  |
| state_max_trade_advantage_from_capacity_add | 容量带来的最大贸易优势 | state | additive | percent, good |  |
| state_middle_strata_expected_sol_add | 中等阶层最低预期生活水平 | state | additive | neutral |  |
| state_migration_pull_add | 迁移吸引力 | state | additive | good |  |
| state_migration_pull_mult | 迁移吸引力 | state | multiplicative | percent, good |  |
| state_migration_pull_unincorporated_mult | 未整合州的迁移吸引力 | state | multiplicative | percent, good |  |
| state_migration_quota_mult | 迁移配额 | state | multiplicative | percent, neutral |  |
| state_minimum_incorporated_subsistence_arable_land_add | 已整合州最低自给耕地份额 | state | additive | percent, neutral |  |
| state_mortality_mult | 死亡率 | state | multiplicative | percent, bad |  |
| state_mortality_turmoil_mult | 每点动荡的死亡率 | state | multiplicative | percent, bad |  |
| state_mortality_wealth_mult | 每点财富的死亡率 | state | multiplicative | percent, bad |  |
| state_non_contiguous_incorporation_speed_mult | 非毗连整合速度 | state | multiplicative | percent, good |  |
| state_non_homeland_colony_growth_speed_mult | 非本土州的殖民地增长速度 | state | multiplicative | percent, good |  |
| state_non_homeland_mortality_mult | 非本土州死亡率 | state | multiplicative | percent, bad |  |
| state_officers_investment_pool_contribution_add | 军官投资池贡献 | state | additive | percent, good |  |
| state_officers_investment_pool_efficiency_mult | 军官投资池贡献效率 | state | multiplicative | percent, good |  |
| state_peasants_consumption_multiplier_add | 农民的商品消费 | state | additive | percent, bad |  |
| state_peasants_education_access_add | 农民的教育机会 | state | additive | percent, good |  |
| state_peasants_internal_migration_disallowed_bool | 禁止农民国内迁移 | state | boolean | bad |  |
| state_peasants_mass_migration_disallowed_bool | 禁止农民大规模迁移 | state | boolean | bad |  |
| state_peasants_mortality_mult | 农民死亡率 | state | multiplicative | percent, bad |  |
| state_political_strength_from_wealth_mult | 财富带来的政治力量 | state | multiplicative | percent, neutral |  |
| state_political_strength_from_welfare_mult | 领取救济时的政治力量 | state | multiplicative | percent, neutral |  |
| state_pollution_generation_add | 产生的污染 | state | additive | bad |  |
| state_pollution_reduction_health_mult | 污染健康影响削减 | state | multiplicative | percent, bad |  |
| state_pop_pol_str_add | 人口通用政治力量 | state | additive | neutral |  |
| state_pop_pol_str_mult | 人口通用政治力量 | state | multiplicative | percent, neutral |  |
| state_pop_qualifications_mult | 资质 | state | multiplicative | percent, good |  |
| state_pop_support_movement_anarchist_add | 无政府主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_anarchist_mult | 无政府主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_anti_slavery_add | 废奴主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_anti_slavery_mult | 废奴主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_bonapartist_add | 波拿巴主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_bonapartist_mult | 波拿巴主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_carlist_add | 卡洛斯运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_carlist_mult | 卡洛斯运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_communist_add | 共产主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_communist_mult | 共产主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_corporatist_add | 社团主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_corporatist_mult | 社团主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_cultural_majority_add | 文化多数派运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_cultural_majority_mult | 文化多数派运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_cultural_minority_add | 文化少数派运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_cultural_minority_mult | 文化少数派运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_fascist_add | 法西斯主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_fascist_mult | 法西斯主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_feminist_add | 女权主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_feminist_mult | 女权主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_german_national_add | 德意志民族主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_german_national_mult | 德意志民族主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_india_pan_national_add | 印度泛民族主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_india_pan_national_mult | 印度泛民族主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_italian_national_add | 意大利民族主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_italian_national_mult | 意大利民族主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_labor_add | 工人运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_labor_mult | 工人运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_land_reform_add | 农民运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_land_reform_mult | 农民运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_legitimist_add | 正统派运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_legitimist_mult | 正统派运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_liberal_add | 自由主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_liberal_mult | 自由主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_miguelist_add | 米格尔派运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_miguelist_mult | 米格尔派运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_modernizer_add | 现代化运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_modernizer_mult | 现代化运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_nihilist_add | 虚无主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_nihilist_mult | 虚无主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_orleanist_add | 奥尔良派运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_orleanist_mult | 奥尔良派运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_positivist_add | 实证主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_positivist_mult | 实证主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_pro_slavery_add | 拥奴主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_pro_slavery_mult | 拥奴主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_radical_add | 激进主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_radical_mult | 激进主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_reactionary_add | 反动主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_reactionary_mult | 反动主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_religious_majority_add | 宗教多数派运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_religious_majority_mult | 宗教多数派运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_religious_minority_add | 宗教少数派运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_religious_minority_mult | 宗教少数派运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_royalist_absolutist_add | 绝对主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_royalist_absolutist_mult | 绝对主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_royalist_constitutional_add | 保皇主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_royalist_constitutional_mult | 保皇主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_slave_revolt_add | 奴隶起义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_slave_revolt_mult | 奴隶起义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_socialist_add | 社会主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_socialist_mult | 社会主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_utilitarian_add | 功利主义运动人口吸引力 | state | additive | neutral |  |
| state_pop_support_movement_utilitarian_mult | 功利主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_pop_support_movement_yugoslav_national_add | state_pop_support_movement_yugoslav_national_add | state | additive | neutral |  |
| state_pop_support_movement_yugoslav_national_mult | 德意志民族主义运动人口吸引力 | state | multiplicative | percent, neutral |  |
| state_radicalism_increases_cultural_erasure_mult | 文化抹除状态下的激进派增长 | state | multiplicative | percent, bad |  |
| state_radicalism_increases_full_acceptance_mult | 完全接纳状态下的激进派增长 | state | multiplicative | percent, bad |  |
| state_radicalism_increases_open_prejudice_mult | 公开偏见状态下的激进派增长 | state | multiplicative | percent, bad |  |
| state_radicalism_increases_second_rate_citizen_mult | 二等公民状态下的激进派增长 | state | multiplicative | percent, bad |  |
| state_radicalism_increases_violent_hostility_mult | 暴力敌视状态下的激进派增长 | state | multiplicative | percent, bad |  |
| state_radicals_and_loyalists_from_sol_change_mult | 生活水平变化产生的激进派与忠诚派 | state | multiplicative | percent, neutral |  |
| state_radicals_from_political_movements_mult | 政治运动产生的激进派 | state | multiplicative | percent, bad |  |
| state_sell_orders_ammunition_add | 弹药卖出订单 | state | additive | neutral |  |
| state_sell_orders_artillery_add | 火炮卖出订单 | state | additive | neutral |  |
| state_sell_orders_grain_add | 谷物卖出订单 | state | additive | neutral |  |
| state_sell_orders_small_arms_add | 轻武器卖出订单 | state | additive | neutral |  |
| state_shopkeepers_investment_pool_contribution_add | 店主投资池贡献 | state | additive | percent, good |  |
| state_shopkeepers_investment_pool_efficiency_mult | 店主投资池贡献效率 | state | multiplicative | percent, good |  |
| state_slave_import_mult | 奴隶进口 | state | multiplicative | percent, good |  |
| state_slaves_mortality_mult | 奴隶死亡率 | state | multiplicative | percent, bad |  |
| state_soldiers_investment_pool_contribution_add | 军人投资池贡献 | state | additive | percent, good |  |
| state_soldiers_investment_pool_efficiency_mult | 军人投资池贡献效率 | state | multiplicative | percent, good |  |
| state_soldiers_mortality_mult | 军人死亡率 | state | multiplicative | percent, bad |  |
| state_standard_of_living_add | 生活水平 | state | additive | good |  |
| state_subvention_export_add | 出口最高补贴 | state | additive | percent, neutral |  |
| state_subvention_import_add | 进口最高补贴 | state | additive | percent, neutral |  |
| state_tariff_export_add | 出口最高关税 | state | additive | percent, neutral |  |
| state_tariff_import_add | 进口最高关税 | state | additive | percent, neutral |  |
| state_tax_capacity_add | 税收能力 | state | additive | good |  |
| state_tax_capacity_mult | 税收能力 | state | multiplicative | percent, good |  |
| state_tax_collection_mult | 税收征收 | state | multiplicative | percent, neutral |  |
| state_tax_waste_add | 税收损耗 | state | additive | percent, bad |  |
| state_trade_advantage_from_capacity_add | 容量带来的贸易优势 | state | additive | percent, good |  |
| state_trade_advantage_mult | 贸易优势 | state | multiplicative | percent, good |  |
| state_trade_advantage_same_religion_add | 与同宗教者的贸易优势 | state | additive | good |  |
| state_trade_capacity_add | 贸易容量 | state | additive | good |  |
| state_trade_capacity_mult | 贸易容量 | state | multiplicative | percent, good |  |
| state_trade_center_max_limit_add | 贸易中心最大等级 | state | additive | good |  |
| state_trade_quantity_mult | 贸易数量 | state | multiplicative | percent, good |  |
| state_turmoil_effects_mult | 动荡带来的州惩罚 | state | multiplicative | percent, bad |  |
| state_unincorporated_starting_wages_mult | 未整合州的起始工资 | state | multiplicative | percent, neutral |  |
| state_upper_strata_expected_sol_add | 上等阶层最低预期生活水平 | state | additive | neutral |  |
| state_urbanization_per_level_add | 每级城市中心的城市化 | state | additive | neutral |  |
| state_urbanization_per_level_mult | 每级城市中心的城市化 | state | multiplicative | percent, bad |  |
| state_weekly_trades_add | 每周贸易次数 | state | additive | good |  |
| state_welfare_payments_add | 救济金 | state | additive | percent, neutral |  |
| state_welfare_payments_mult | 救济金倍率 | state | multiplicative | percent, neutral |  |
| state_working_adult_ratio_add | 劳动力比例 | state | additive | percent, good |  |
| tax_consumption_add | 消费税率 | tax | additive | percent, neutral |  |
| tax_dividends_add | 股息税率 | tax | additive | percent, neutral |  |
| tax_heathen_add | 宗教税 | tax | additive | neutral |  |
| tax_income_add | 所得税率 | tax | additive | percent, neutral |  |
| tax_land_add | 土地税 | tax | additive | neutral |  |
| tax_per_capita_add | 人头税 | tax | additive | neutral |  |
| unit_army_defense_add | 陆军防御 | unit | additive | good | combat |
| unit_army_defense_mult | 陆军防御 | unit | multiplicative | percent, good | combat |
| unit_army_experience_gain_add | 陆军每周经验获取 | unit | additive | good | non-combat combat (if in battle on weekly tick) |
| unit_army_experience_gain_mult | 陆军每周经验获取 | unit | multiplicative | percent, good | non-combat combat (if in battle on weekly tick) |
| unit_army_offense_add | 陆军进攻 | unit | additive | good | combat |
| unit_army_offense_mult | 陆军进攻 | unit | multiplicative | percent, good | combat |
| unit_combat_unit_type_cannon_artillery_offense_mult | 加农炮兵进攻 | unit | multiplicative | percent, good |  |
| unit_combat_unit_type_heavy_tank_offense_mult | 重型坦克进攻 | unit | multiplicative | percent, good |  |
| unit_combat_unit_type_mechanized_infantry_offense_add | 机械化步兵进攻 | unit | additive | good |  |
| unit_combat_unit_type_mobile_artillery_offense_mult | 机动火炮进攻 | unit | multiplicative | percent, good |  |
| unit_combat_unit_type_shrapnel_artillery_offense_mult | 榴霰炮兵进攻 | unit | multiplicative | percent, good |  |
| unit_combat_unit_type_siege_artillery_offense_mult | 攻城炮兵进攻 | unit | multiplicative | percent, good |  |
| unit_combat_unit_type_squad_infantry_offense_add | 班组步兵进攻 | unit | additive | good |  |
| unit_combat_unit_type_trench_infantry_offense_add | 堑壕步兵进攻 | unit | additive | good |  |
| unit_defense_add | 防御 | unit | additive | good | combat |
| unit_defense_developed_add | 已开发地形防御 | unit | additive | good |  |
| unit_defense_developed_mult | 已开发地形防御 | unit | multiplicative | percent, good |  |
| unit_defense_elevated_add | 高地地形防御 | unit | additive | good |  |
| unit_defense_elevated_mult | 高地地形防御 | unit | multiplicative | percent, good |  |
| unit_defense_flat_add | 平坦地形防御 | unit | additive | good |  |
| unit_defense_flat_mult | 平坦地形防御 | unit | multiplicative | percent, good |  |
| unit_defense_forested_add | 森林地形防御 | unit | additive | good |  |
| unit_defense_forested_mult | 森林地形防御 | unit | multiplicative | percent, good |  |
| unit_defense_hazardous_add | 险恶地形防御 | unit | additive | good |  |
| unit_defense_hazardous_mult | 险恶地形防御 | unit | multiplicative | percent, good |  |
| unit_defense_mult | 防御 | unit | multiplicative | percent, good | combat |
| unit_defense_water_add | 平坦地形防御 | unit | additive | good |  |
| unit_defense_water_mult | 平坦地形防御 | unit | multiplicative | percent, good |  |
| unit_devastation_mult | 破坏度 | unit | multiplicative | percent, neutral | combat |
| unit_experience_gain_add | 陆军每周经验获取 | unit | additive | good | non-combat combat (if in battle on weekly tick) |
| unit_experience_gain_mult | 陆军每周经验获取 | unit | multiplicative | percent, good | non-combat combat (if in battle on weekly tick) |
| unit_kill_rate_add | 杀伤率 | unit | additive | percent, good | combat |
| unit_morale_damage_mult | 士气伤害 | unit | multiplicative | percent, good | combat |
| unit_morale_loss_add | 士气损失 | unit | additive | bad | combat |
| unit_morale_loss_mult | 士气损失 | unit | multiplicative | percent, bad | combat |
| unit_morale_recovery_mult | 士气恢复 | unit | multiplicative | percent, good | non-combat |
| unit_naval_invasion_efficiency_mult | 海上入侵效率 | unit | multiplicative | percent, good |  |
| unit_occupation_mult | 战斗占领 | unit | multiplicative | percent, good | combat |
| unit_offense_add | 进攻 | unit | additive | good | combat |
| unit_offense_developed_add | 已开发地形进攻 | unit | additive | good |  |
| unit_offense_developed_mult | 已开发地形进攻 | unit | multiplicative | percent, good |  |
| unit_offense_elevated_add | 高地地形进攻 | unit | additive | good |  |
| unit_offense_elevated_mult | 高地地形进攻 | unit | multiplicative | percent, good |  |
| unit_offense_flat_add | 平坦地形进攻 | unit | additive | good |  |
| unit_offense_flat_mult | 平坦地形进攻 | unit | multiplicative | percent, good |  |
| unit_offense_forested_add | 森林地形进攻 | unit | additive | good |  |
| unit_offense_forested_mult | 森林地形进攻 | unit | multiplicative | percent, good |  |
| unit_offense_hazardous_add | 险恶地形进攻 | unit | additive | good |  |
| unit_offense_hazardous_mult | 险恶地形进攻 | unit | multiplicative | percent, good |  |
| unit_offense_mult | 进攻 | unit | multiplicative | percent, good | combat |
| unit_offense_water_add | 平坦地形进攻 | unit | additive | good |  |
| unit_offense_water_mult | 平坦地形进攻 | unit | multiplicative | percent, good |  |
| unit_provinces_captured_mult | 占领的省份 | unit | multiplicative | percent, good | combat |
| unit_provinces_lost_mult | 失去的省份 | unit | multiplicative | percent, bad | combat |
| unit_recovery_rate_add | 恢复率 | unit | additive | percent, good | combat |
| unit_supply_consumption_mult | 补给消耗 | unit | multiplicative | percent, bad | non-combat |
## 参考资料

1. ↑ Modifier 类型的流程连接由 BrokenRobot 为 [Tiger 验证器](https://github.com/amtep/tiger) 判定

---

- 如需更新已定义 modifier 类型的注释，参见 [Module:Modifier type/Notes](https://vic3.paradoxwikis.com/Module:Modifier_type/Notes)
- 如需更新潜在的 modifier 类型，参见 [Module:Modifier type/Potential](https://vic3.paradoxwikis.com/Module:Modifier_type/Potential)

模组制作
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • Modifier 类型 • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [决议](Decision modding.md) • [事件](Event modding.md) • [历史](History modding.md) • [日志](Journal modding.md) • [Modifiers](Modifier modding.md) • 目标 • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [建筑](Building modding.md) • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图像 | [3D 模型](Model modding.md) • [事件图片](Event images.md) • [图像资源](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [音效](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [模组](Mod.md) • [模组兼容性](Mod compatibility.md) • [模组结构](Mod structure.md) • [脚本测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [模组翻译](Mod translation.md) • [新国家模组制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州模组制作指南](State modding guide.md) |
|---|---|