---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Treaty modding
source: https://vic3.paradoxwikis.com/Treaty_modding
pageid: 7705
categories: [Potentially_outdated, 1.11, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。其中至少部分内容最后核实时适用的版本为 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.11。

参见：
条约
**条约**（Treaty）是两个国家之间的外交协议。条约可以通过外交谈判达成，也可以由战争强加。每份条约由一条或多条条款组成。

## 条约 defines

| define | 默认值 | 开发者注释 |
|---|---|---|
| LAW_ENACTMENT_LAW_COMMITMENT_EFFECT | 0.05 | # 通过条约承诺制定某项法律时，为通过几率增加此数值，并按被承诺国对承诺国所拥有的等级数进行缩放 |

| define | 默认值 | 开发者注释 |
|---|---|---|
| TREATY_PROPOSAL_PENDING_APPROVAL_DAYS | 30 | # 待批准的条约提案在自动被拒绝前的天数 |
| TREATY_ARTICLE_COST_LOBBY_CLOUT_MULT | 0.01 | # 亲/反某国游说集团的每一点政治力量都会按此数值降低或提高与该国维持条约条款的影响力花费乘数 |
| TREATY_ARTICLE_COST_LOBBY_CLOUT_MAX | 0.5 | # 亲/反某国游说集团对花费乘数的影响不能超过此值 |
| MAX_TREATY_OBLIGATIONS_DELAY_DAYS | 3650 | # 作为条约一部分承诺的义务在约束期结束时生效，或自条约最初签署起经过此天数后生效，以先到者为准 [>= 0] |
| BINDING_PERIOD_THRESHOLD_TO_EFFECTUATE_TREATY_OBLIGATIONS_DAYS | 30 | # 当约束期等于或少于此天数时，义务生效 |
| TREATY_ARTICLE_MONEY_TRANSFER_ARTICLE_TYPE | "money_transfer" |  |
| TREATY_ARTICLE_TREATY_PORT_ARTICLE_TYPE | "treaty_port" |  |
| TREATY_ARTICLE_INVESTMENT_RIGHTS_ARTICLE_TYPE | "foreign_investment_rights" |  |
| TREATY_ARTICLE_LAW_COMMITMENT_ARTICLE_TYPE | "law_commitment" |  |
| DEFAULT_WAR_REPARATIONS_MONEY_TRANSFER | 0.1 |  |
| TREATY_PROPOSAL_COOLDOWN_DAYS | 7 | # 一份提案被拒绝后，经过多少天才可以发送另一份条约提案 |
| TREATY_DEFAULT_BINDING_DURATION_YEARS | 5 |  |
| TREATY_THREATEN_HOSTILITIES_DURATION_DAYS | 365 |  |
| THREATEN_NAVAL_HOSTILITIES_COOLDOWN_DAYS | 1825 | # 5 年后才能再次对同一国家威胁海军敌对行动 |
| NAVAL_HOSTILITIES_POINTS_MAX | 100 | # 单次海军敌对行动中可造成的最大伤害点数 |
| NAVAL_VULNERABILITY_MAX | 1.0 | # 最大海军脆弱度得分。用于判定一个国家有多惧怕海军敌对行动。 |
| NAVAL_VULNERABILITY_TRADE_MULTIPLIER | 0.75 | # 来自贸易的脆弱度：此值 *（贸易基础成本 / GDP）= 脆弱度点数 |
| NAVAL_VULNERABILITY_COASTAL_GDP_MULTIPLIER | 0.5 | # 来自沿海 GDP 的脆弱度：此值 *（沿海 GDP / GDP）= 脆弱度点数 |
| NAVAL_VULNERABILITY_PRESTIGE_MULTIPLIER | 1.0 | # 来自海军威望的脆弱度：此值 *（海军威望 / 总威望）= 脆弱度点数 |
| NAVAL_HOSTILITIES_POINTS_SHIPS_SUNK_AT_FULL_FLEET | 500 | # 当一国舰队建造费用的 100% 被击沉时给予的伤害点数 |
| NAVAL_HOSTILITIES_POINTS_BLOCKADE_GDP_WEEKLY | 20 | # 当一国 GDP 的 100% 被封锁时，每周造成的伤害点数 |
| NAVAL_HOSTILITIES_POINTS_PIRACY_GDP_WEEKLY | 20 | # 当一国相当于 GDP 100% 的商品被海盗掠夺时，每周造成的伤害点数 |
| NAVAL_HOSTILITIES_POINTS_BOMBARDMENT_DEVASTATION | 20 | # 每单位荒废度增加的伤害点数，按州 GDP / 受害国 GDP 缩放 |
| NAVAL_HOSTILITIES_POINTS_BOMBARDMENT_BUILDING_DESTROYED | 10 | # 炮击每摧毁一级建筑给予的固定伤害点数 |
| PAST_TEMPORARY_HOSTILITIES_KEEP_YEARS | 20 | # 临时敌对行动数据到期后保留的年数 |
| PIRACY_DAMAGE_TRACKING_WEEKS | 26 | # 用于取平均值而保留的海盗伤害历史周数 |

| define | 默认值 | 开发者注释 |
|---|---|---|
| DIPLO_PROPOSAL_DAYS_LEFT_MAX | 28 | # 当提案剩余天数多于此值时，AI 不会答复提案（应与 DIPLOMATIC_ACTION_PENDING_APPROVAL_DAYS 对应） |
| DIPLO_PROPOSAL_DAYS_LEFT_MIN | 20 | # 当提案剩余天数等于或少于此值时，AI 一定会答复提案（应与 DIPLOMATIC_ACTION_PENDING_APPROVAL_DAYS 对应） |
| DIPLO_PROPOSAL_ANSWER_CHANCE | 5 | # AI 每次 tick 答复提案的几率（1 = 1%） |
| DIPLO_PROPOSAL_TO_PLAYER_COOLDOWN_MONTHS | 120 | # 在此月数内不会向玩家提出完全相同的提案 |
| DIPLO_PROPOSAL_LIKELY_NON_ACCEPTED_COOLDOWN_MONTHS | 120 | # 当 AI 掷骰决定是否尝试一个它认为会被拒绝的提案时，若不尝试则在此时间内不再尝试 |
| DIPLO_PROPOSAL_LIKELY_NON_ACCEPTED_TREATY_COOLDOWN_MONTHS | 12 | # 当 AI 向另一个 AI 提出条约失败后，等这么久才会再次尝试与同一国家缔约 |
| DIPLO_PROPOSAL_NO_OBLIGATION_COOLDOWN_MONTHS | 120 | # 如果 AI 决定不为提案提供义务，则记住该决定这么多个月 |
| DIPLO_PROPOSAL_ACCEPT_THRESHOLD | 1 | # 对于不带 uses_random_approval 标志的外交行动，达到或超过此接受度时，AI 会对提案说“是”。每超出一点都会提高接受带 uses_random_approval 标志的外交行动或条约提案的几率 |
| DIPLO_PROPOSAL_HALFWAY_RANDOM_ACCEPTANCE_THRESHOLD | 10 | # 对于带 uses_random_approval 标志的外交行动或条约提案，达到或超过此接受度时，AI 有 50% 的几率接受，并在提出该提案时将其视为会被接受 |
| DIPLO_PROPOSAL_GUARANTEED_RANDOM_ACCEPTANCE_THRESHOLD | 30 | # 对于带 uses_random_approval 标志的外交行动或条约提案，达到或超过此接受度时，AI 一定会接受 |
| DIPLO_PROPOSAL_BREAK_THRESHOLD | -100 | # 达到或低于此接受度时，AI 会撕毁现有协定 |
| DIPLO_PROPOSAL_TRANSFER_PACT_RELUCTANCE | 25 | # 在转让协定类提案中，将此值加到现有协定的接受度数值上 |
| INFLUENCE_DEFICIT_RECOVER_INFLUENCE_BASE_VALUE | 50 | # 加到我们为恢复影响力而撕毁的条约或协定的评分上 |
| INFLUENCE_DEFICIT_RECOVER_INFLUENCE_RANDOM_FACTOR | 1.0 | # 此值越高，AI 因影响力赤字而撕毁协定/条约的行为就越随机 |
| TRADE_VALUE_DELTA_FACTOR | 3.0 | # 计算条约贸易价值时，生产/消费之间的差值比基础生产/消费数值的权重高出这么多倍 |
| TRADE_VALUE_BASE_MULTIPLIER | 0.001 | # 仅基于生产与消费应用于条约贸易价值的基础乘数 |
| TRADE_VALUE_RELATIVE_MULTIPLIER | 100 | # 应用于条约贸易价值并除以市场总价值的相对乘数 |
| TREATY_FAIRNESS_BASE_SCORE | 10 | # 在考虑各国接受度之前条约公平性的基础分，接受度差值小于此值的条约会被视为对双方都公平 |
| REJECTED_TREATY_MEMORY_DURATION_DAYS | 365 | # AI 记住被拒绝的条约多少天，并在此期间拒绝任何没有足够显著改进的条约 |
| REJECTED_TREATY_MIN_ACCEPTANCE_IMPROVEMENT_FOR_NEW_PROPOSAL | 10 | # 在近期拒绝过一项条约后，若想让 AI 有机会接受新的条约提案，新提案必须比旧提案好这么多 |
| REJECTED_TREATY_UNDER_MIN_ACCEPTANCE_IMPROVEMENT_PENALTY | -1000 | # 当条约提案在被拒条约记忆期内没有得到足够改进时，加到接受度上的数值 |
| # Treaties |  |  |
| TREATIES_RANDOM_FACTOR | 1.0 | # AI 在拟定条约时选择条款的随机程度是多少？ |
| TREATIES_CHECK_CATEGORIES_WHEN_COMPOSING_TREATY | no | # AI 在收集初始条款后拟定条约时是否考虑类别？ |
| TREATIES_NUMBER_CHECKED_CATEGORIES_TREATY_COMPOSER | 3 | # AI 拟定条约时会尝试收集多少个类别来进行比对 |
| TREATIES_MINIMUM_ACCEPTANCE_TO_PROPOSE | 15 | # AI 要求对方具有多少接受度才会尝试发送提案？0 = 永不接受，30 = 总是接受，介于两者之间 = 随机几率 |
| TREATIES_MINIMUM_OWN_ACCEPTANCE_TO_PROPOSE | 10 | # AI 自身需要具有多少自身接受度才会发送提案？ |
| TREATIES_MAX_NUMBER_ARTICLES | 6 | # AI 在一份条约中最多会考虑多少条条款 |
| TREATIES_ACCEPTANCE_BASE | 0 | # 条约的基础接受度 |
| TREATIES_ACCEPTANCE_WITHDRAW_THRESHOLD | -50 | # 达到或低于此阈值时，AI 会退出处于约束期之外的条约 |
| TREATIES_ACCEPTANCE_WITHDRAW_BINDING_PERIOD_THRESHOLD | -10000 | # 达到或低于此阈值时，AI 会在条约仍处于约束期时退出条约 |
| TREATIES_DEFAULT_LENGTH_YEARS | 5 | # AI 提议的条约长度 |
| TREATY_OBLIGATION_WE_OWE_THEM_ACCEPTANCE | -40 | # 如果作为条约的一部分，A 国将欠 B 国一项义务，A 国对该条约接受度的变化量。注意："WE" 是进行评估的国家，而非玩家 |
| TREATY_OBLIGATION_THEY_OWE_US_ACCEPTANCE | 30 | # 如果作为条约的一部分，A 国将获得 B 国所欠的一项义务，A 国对该条约接受度的变化量。注意："US" 是进行评估的国家，而非玩家 |
| TREATY_OBLIGATION_THEY_OWE_US_RECENTLY_REPUDIATED_ACCEPTANCE | 15 | # 同上，但如果 B 国近期曾拒不履行义务则使用此值（A 国对它的估值更低，因为 B 国的承诺没那么值钱） |
| TREATY_OBLIGATION_THEY_CALL_US_IN_ACCEPTANCE | 30 | # 如果 B 国正在要求 A 国履行其所欠的义务，A 国接受度的变化量。注意："US" 是进行评估的国家，而非玩家 |
| TREATY_OBLIGATION_THEY_CALL_US_IN_RECENTLY_REPUDIATED_ACCEPTANCE | 15 | # 同上，但如果 B 国近期曾拒不履行义务则使用此值（A 国对它的估值更低，因为 B 国愿意无视的那些荣誉协议，A 国也不那么倾向于遵守） |

| define | 默认值 | 开发者注释 |
|---|---|---|
| # 条约签署地点的选取分两步进行 # 1. 从最多 6 个州中随机选择一个，这 6 个州是： # - 首都（1 个） # - GDP 最高的州（1 个） # - GDP 第二高的州（0 或 1 个） # - 以上针对两个条约参与国 # - 单一州国家没有 GDP 第二高的州 # 2. 一旦随机选定一个州，便在该州所属的 # 州区域中随机选择一个枢纽（如适用，例如内陆 # 州区域没有港口） # 每次随机选取都按以下权重进行加权 |  |  |
| TREATY_SIGNING_STATE_WEIGHT_CAPITAL | 1 | # 为条约随机选择签署地点时首都州拥有的权重 [>= 1] |
| TREATY_SIGNING_STATE_WEIGHT_HIGHEST_GDP | 1 | # 同上，针对 GDP 最高的州 [>=1] |
| TREATY_SIGNING_STATE_WEIGHT_SECOND_HIGHEST_GDP | 1 | # 同上，针对 GDP 第二高的州 [>=1] |
| TREATY_SIGNING_HUB_WEIGHT_CITY | 5 | # 为条约随机选择签署地点时城市枢纽拥有的权重 [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_PORT | 3 | # 同上，针对港口枢纽 [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_FARM | 2 | # 同上，针对农场枢纽 [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_MINE | 1 | # 同上，针对矿山枢纽 [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_WOOD | 1 | # 同上，针对木材枢纽 [>= 1] |

## 条约条款定义

条约条款提供了更深层次的外交互动，更重要的是，它允许 mod 作者添加战争目标。每条条约条款都在 common/treaty_articles 中定义。

此定义中的基本元素有：

| 元素 | 选项 | 示例 | 说明 |
|---|---|---|---|
| kind | directed mutual | `kind = directed` | 条约条款的类型 |
| cost | `value` | `cost = 100` | 维持所需的影响力花费（必须为非负值） |
| relations_progress_per_day | `value` | `relations_progress_per_day = 1` | 两国之间的每日关系进展（可以为负值） |
| relations_improvement_max | `value` | `relations_improvement_max = 100` | 仅凭此条款能达到的关系最大值（必须为非负值） |
| relations_improvement_min | `value` | `relations_improvement_min = 100` | 仅凭此条款能达到的关系最小值（必须为非负值） |
| icon | `path` | `icon = "gfx/interface/icons/diplomatic_treaties_articles_icons/alliance_treaties.dds"` | 条约条款图标的路径 |
| maintenance_paid_by | source_country target_country | `maintenance_paid_by = target_country` | 由谁支付影响力来维持该条约条款（若为 mutual 则忽略） |
| usage_limit | once_per_side once_per_treaty once_per_side_with_same_inputs | `usage_limit = once_per_side` | 对该条款可使用次数的限制。`once_per_side` 为每个国家一次，但请注意可能还有其他限制 |
| flags | is_alliance is_defensive_pact is_gurantee_independence is_support_independence is_investment_rights is_trade_privilege is_military_access is_transit_rights is_non_colonization_agreement is_goods_transfer is_money_transfer is_monopoly_for_company is_prohibit_goods_trade_with_world_market is_no_tariffs is_no_subventions is_treaty_port is_law_commitment can_be_renegotiated can_be_enforced causes_state_transfer friendly hostile giftable | flags = { is_transit_rights can_be_enforced can_be_renegotiated giftable friendly } | 这些是可以应用于条约条款的代码标志，对于大多数 `is` 类标志，很可能会触发相应的行为 |
| mutual_exclusions | `article type` | mutual_exclusions = { alliance defensive_pact guarantee_independence } | 该条约条款不能与所列条款一同使用 |
| unlocked_by_technologies | `technology` | unlocked_by_technologies = { international_trade } | 应由哪项技术解锁该条约条款的使用。[1] |
| automatically_support | `diplomatic play types` | automatically_support = { dp_independence dp_increase_autonomy dp_annex_subject } | 源国家将在哪些外交博弈中自动支持目标国家 |
| source_modifier | `modifier types` | source_modifier = { country_treaty_leverage_generation_add = 300 } | 应用于源国家的修正（若为 mutual 条款则必须为空） |
| target_modifier | `modifier types` | target_modifier = { unit_experience_gain_mult = 0.5 building_training_rate_mult = 0.2 country_military_goods_cost_mult = -0.1 country_military_tech_spread_mult = 0.1 } | 应用于目标国家的修正（若为 mutual 条款则必须为空） |
| mutual_modifier | `modifier types` | mutual_modifier = { country_treaty_leverage_generation_add = 400 } | 应用于两国的修正 |

### 有效性验证

这些参数决定一条条款何时可以使用。

#### 可见性（Visible）

`visible` trigger 代码块控制该条款是否对该国完全可见。它会对两国分别进行检查。

它拥有以下 scope：

- `root`

#### 可行性（Possible）

`possible` trigger 代码块控制该条款在两国之间是否可以考虑使用。它还会自动运行 `visible` trigger。

它拥有以下 scope：

- `root`
- `other_country`

#### 维持（Maintain）

`requirement_to_maintain` trigger 代码块是一个可重复检查的代码块，用于判定一条条款是否可行以及是否应予维持。

它拥有以下 scope：

- `root`
- `article`
- `treaty`

仅适用于 mutual 条款：

- `first_country`
- `second_country`

仅适用于 directed 条款：

- `source_country`
- `target_country`

#### 能否批准（Can ratify）

`can_ratify` trigger 代码块控制两国能否批准一份包含此类条款的条约。它会自动运行 `visible` 和 `possible` trigger。

它拥有以下 scope：

- `root`
- `article`
- `treaty`

仅适用于 mutual 条款：

- `first_country`
- `second_country`

仅适用于 directed 条款：

- `source_country`
- `target_country`
### 生效时

该 effect 块在包含此条款的条约通过外交手段或战争批准后立即执行。

它拥有 scope `article_options`，其中包含条款的参数，例如 `source_country`、`target_country` 和 `input_state`。

### 被强制执行时

该 effect 块在包含此条款的条约通过战争被强制执行后立即执行。

它拥有 scope `article_options`，其中包含条款的参数，例如 `source_country`、`target_country` 和 `input_state`。

### 未履行

未履行块描述一国如何违反条约，以及当条款的源国家未履行其义务时会发生什么。

#### 条件（Conditions）

条件块用于检查一国何时构成违约，可使用以下时间间隔：

- `weekly`
- `monthly`
- `yearly`

并可用以下 scope：

- `root`
- `article`

例如：

```
conditions = {
weekly = {
    scope:article = { source_country = { in_default = yes } }
}
}
```

#### 后果（Consequences）

consequences 参数可以是以下值：

| 后果 | 说明 |
|---|---|
| none | 无 |
| withdraw | 违约方自动单方面退出条约，并承担可能适用的任何惩罚 |
| freeze | 违约方必须继续履行其义务，而另一方的义务则被解除，条约变成单方面的交易，直到违约方能够再次履行其义务为止 |

#### 违约次数

还提供了一个选项，用于设置在触发后果前允许的最大违约次数：

- `max_consecutive_contraventions`

它限制一国在连续多少次满足未履行条件后进入未履行状态。

### 条款输入

条款可以接受以下类型的输入：

- `quantity`
- `goods`
- `state`
- `strategic_region`
- `company`
- `building_type`
- `law_type`
- `country`

不过，这些输入在游戏文件中的实现并没有清晰的文档，而且有些在没有特定条款标志（flag）的情况下无法工作。例如，选择 strategic_region 的 localization 只适用于非殖民协议，尽管该条约条款并非如此。如果它们存在于未经修改的《维多利亚3》中，那么它们很可能是可用的。

#### 条款输入触发器（trigger）

每种输入类型都有一个 `valid_trigger` 块：

- `goods_valid_trigger = {}`
- `state_valid_trigger = {}`
- `strategic_region_valid_trigger = {}`
- `company_valid_trigger = {}`
- `building_type_valid_trigger = {}`
- `law_type_valid_trigger = {}`
- `country_valid_trigger = {}`

有效性触发器可以使用以下 scope：

| Scope | 说明 |
|---|---|
| `root` | 条款的源国家 |
| `article` | 条款本身。（注意此时并非所有输入都已被设置） |
| `input` | 正在被检查的特定输入 |
| `other_country` | 另一个国家 |

专门针对商品有效性触发器：

| Scope | 说明 |
|---|---|
| `goods` | 正在被检查的商品输入 |
| `market_goods` | 相同的商品，但作为源国家市场中的市场商品 |

#### 数量的最小值与最大值

要设置输入的最小值和最大值，请使用：

- `quantity_min_value = {}`
- `quantity_max_value = {}`

每一个都应包含一个 [script value](Script value.md) 块。

### 退出

#### 可以退出（Can withdraw）

`can_withdraw` trigger 块决定一国是否被允许退出条约。它拥有以下 scope：

- `withdrawing_country`
- `non_withdrawing_country`

对于对等条款，还包括：

- `first_country`
- `second_country`

对于单向条款，还包括：

- `source_country`
- `target_country`

#### 退出时（On withdrawal）

`on_withdrawal` effect 块在一方退出条约时、退出生效之前立即执行。

它拥有以下 scope：

- `treaty_options`
- `article`
- `withdrawing_country`
- `non_withdrawing_country`

#### 违约退出时（On break）

`on_break` effect 块额外在一方于约束期结束前退出条约时、退出生效之前立即执行。

它拥有以下 scope：

- `treaty_options`
- `article`
- `withdrawing_country`
- `non_withdrawing_country`

### AI

AI 块包含关于 AI 应如何使用及评估该条款的信息。

#### 条约类别（Treaty categories）

在此可以设置条约条款的类别。提供以下类别：

- `economy`
- `trade`
- `military`
- `military_defense`
- `ideology`
- `expansion`
- `power_bloc`
- `other`
- `none`

#### 条款使用方式

AI 将如何使用该条款。可以是多个。提供以下选项：

- `none`
- `will_offer`
- `will_request`

#### 接受度

提供以下参数来限制获得的接受度。这些参数接受整数：

- `combined_acceptance_cap_max`
- `combined_acceptance_cap_min`

`inherent_accept_score` 与 `contextual_accept_score` 相加得到最终的接受度数值，但在其中一个 script value 中进行的数学运算不会应用到另一个，反之亦然。

##### 固有接受度

`inherent_accept_score` 块是一个**不会**在 AI 每次尝试添加条款时重新求值的 script value。它拥有以下 scope：

- `root`
- `article`

仅用于对等条款：

- `first_country`
- `second_country`

仅用于单向条款：

- `source_country`
- `target_country`

##### 情境接受度

`contextual_accept_score` 块是一个可以访问条约本身的 script value，因此可以检查其他条款。它拥有以下 scope：

- `root`
- `article`
- `treaty`

仅用于对等条款：

- `first_country`
- `second_country`

仅用于单向条款：

- `source_country`
- `target_country`

##### 战争目标倍率

`wargoal_score_multiplier` 是一个 script value。它是加到 AI 接受度上的倍率，用于决定 AI 将该条款作为战争目标追求的可能性。它拥有以下 scope：

- `root`
- `article`

仅用于对等条款：

- `first_country`
- `second_country`

仅用于单向条款：

- `source_country`
- `target_country`

### 战争目标数据

#### 执行优先级

一个整数。优先级更高的战争目标会被优先执行。

#### 争夺类型

战争目标如何被“控制”。可用以下选项：

- `control_target_state`
- `control_target_country_capital`
- `control_any_target_country_state`
- `control_own_state`
- `control_own_capital`
- `control_all_own_states`
- `control_all_target_country_claims`

#### 博弈点数与恶名

`maneuvers` 和 `infamy` 块都是 script value。它们决定了将该条款用作战争目标时的博弈点数（maneuver）消耗和恶名获取。

它们拥有以下 scope：

- `root`
- `target_country`

以及以下取决于相关输入的 scope：

- `quantity`
- `country`
- `company`
- `state`
- `region`
- `building`
- `law`
- `goods`
- `market_goods`

## 条约脚本文档

以下 [effect](Effect.md)、[event target](Event target.md) 和 [trigger](Trigger.md) 可以在条约 scope 中使用。

### 条约 scope

| Effect | 说明 | 示例 | 目标 |
|---|---|---|---|
| every_scope_article | 遍历 scope 条约的条款 | every_scope_article = { limit = { <triggers> } #optional <effects> } | treaty_article |
| every_scope_article_option | 遍历 scope 条约或 treaty_options 的 article_options | every_scope_article_option = { limit = { <triggers> } #optional <effects> } | treaty_article_options |
| ordered_scope_article | 遍历 scope 条约的条款 | ordered_scope_article = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty_article |
| ordered_scope_article_option | 遍历 scope 条约或 treaty_options 的 article_options | ordered_scope_article_option = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty_article_options |
| random_scope_article | 遍历 scope 条约的条款 | random_scope_article = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty_article |
| random_scope_article_option | 遍历 scope 条约或 treaty_options 的 article_options | random_scope_article_option = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty_article_options |
| withdraw | 使一国退出条约 | scope:treaty = { withdraw = { country = <country scope> # must be valid and must be bound by the treaty apply_break_penalties = yes/no # optional, default no. If yes, break effects and on-actions apply when treaty is in binding time } } |  |

| Trigger | 说明 | 示例 | 目标 |
|---|---|---|---|
| any_scope_article | 遍历 scope 条约的条款 | any_scope_article = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty_article |
| any_scope_article_option | 遍历 scope 条约或 treaty_options 的 article_options | any_scope_article_option = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty_article_options |
| binds | 检查 scope 条约或 treaty_options 是否约束给定国家 | scope:some_treaty = { if = { limit = { binds = c:FRA binds = c:BEL } } } | country |
| is_enforced | 检查 scope 条约是否被强制执行于任一方 | scope:some_treaty = { if = { limit = { is_enforced = yes } } } | boolean |
| is_equal_exchange | 检查 scope 条约双方是否拥有相同条款 | scope:some_treaty = { if = { limit = { is_equal_exchange = yes } } } | boolean |
| is_fulfilled_by | 检查 scope 条约是否被给定国家履行 | scope:treaty = { is_fulfilled_by = c:FRA } | country |
| is_historical_treaty | 检查 scope 条约是否在游戏开始日期之前签署 | is_historical_treaty = yes/no | boolean |
| is_renegotiation | 检查 scope 条约是否在修订一份现有条约 | scope:some_treaty = { if = { limit = { is_renegotiation = yes } } } | boolean |
| was_coerced_with_naval_threat | 检查 scope 条约是否是通过威胁进行海上敌对行动而被接受的 | was_coerced_with_naval_threat = yes/no | boolean |

| Event target | 说明 | 转换至 scope |
|---|---|---|
| amended_treaty | 转至 scope 条约正在修订的那份条约 | treaty |
| binding_period | 获取 scope 条约在签署时的原始约束期天数 | value |
| enforced_on_country | 转至被强制执行条约的 enforced_on_country | country |
| enforcer_country | 转至被强制执行条约的 enforcer_country | country |
| first_country | 转至以下任一对象的 first_country：外交协定、条约、treaty options、条约条款所属的条约、条约条款选项（仅限对等条款类型） | country |
| remaining_binding_period | 获取 scope 条约当前剩余的约束期天数 | value |
| second_country | 转至以下任一对象的 second_country：外交协定、条约、treaty options、条约条款所属的条约、条约条款选项（仅限对等条款类型） | country |

### 条约条款 scope

| Effect | 说明 | 示例 | 目标 |
|---|---|---|---|

| Trigger | 说明 | 示例 | 目标 |
|---|---|---|---|
| has_type | 检查 scope 对象是否具有给定字符串所标识的类型 | scope:some_object = { has_type = defensive_pact } |  |
| is_treaty_article_in_danger | 检查条约条款是否面临破裂危险 | is_treaty_article_in_danger = yes | boolean |
| max_contraventions | 检查 scope 条款或 article_options 的条款类型的最大违约次数 | scope:treaty_article = { max_contraventions >= 1 } | value |
| num_contraventions | 检查 scope 条款是否被给定国家违约了给定次数 | scope:treaty_article = { num_contraventions = { target = c:FRA value > 0 } } | value |

| Event target | 说明 | 转换至 scope |
|---|---|---|
| first_country | 转至以下任一对象的 first_country：外交协定、条约、treaty options、条约条款所属的条约、条约条款选项（仅限对等条款类型） | country |
| input_building_type | 转至条约条款中的建筑类型输入 | building_type |
| input_company | 转至条约条款中的公司输入 | company |
| input_country | 转至条约条款中的国家输入 | country |
| input_goods | 转至条约条款中的商品输入 | goods |
| input_law | 转至条约条款中的法律输入 | law_type |
| input_market_goods | 转至条约条款中的市场商品输入（示例：input_market_goods:root） | market_goods |
| input_quantity | 转至条约条款中的数量输入 | value |
| input_ship | 转至条约条款中的船只输入 | ship |
| input_state | 转至条约条款中的州输入 | state |
| input_strategic_region | 转至条约条款中的战略区域输入 | strategic_region |
| second_country | 转至以下任一对象的 second_country：外交协定、条约、treaty options、条约条款所属的条约、条约条款选项（仅限对等条款类型） | country |
| shipping_lane | 转至军事编队或条约条款（商品转让）的航线 | shipping_lanes |
| source_country | 转至以下任一对象的 source_country：条约条款（仅限单向条款类型）、条约条款选项（仅限单向条款类型） | country |
| target_country | 转至以下任一对象的 target_country：条约条款（仅限单向条款类型）、条约条款选项（仅限单向条款类型） | country |
| treaty | 转至条约条款所属的条约 | treaty |

### 条约选项 scope

| Effect | 说明 | 示例 | 目标 |
|---|---|---|---|
| every_scope_article_option | 遍历 scope 条约或 treaty_options 的 article_options | every_scope_article_option = { limit = { <triggers> } #optional <effects> } | treaty_article_options |
| ordered_scope_article_option | 遍历 scope 条约或 treaty_options 的 article_options | ordered_scope_article_option = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty_article_options |
| random_scope_article_option | 遍历 scope 条约或 treaty_options 的 article_options | random_scope_article_option = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty_article_options |

| Trigger | 说明 | 示例 | 目标 |
|---|---|---|---|
| any_scope_article_option | 遍历 scope 条约或 treaty_options 的 article_options | any_scope_article_option = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty_article_options |
| binds | 检查 scope 条约或 treaty_options 是否约束给定国家 | scope:some_treaty = { if = { limit = { binds = c:FRA binds = c:BEL } } } | country |
| is_equal_exchange | 检查 scope 条约双方是否拥有相同条款 | scope:some_treaty = { if = { limit = { is_equal_exchange = yes } } } | boolean |
| is_historical_treaty | 检查 scope 条约是否在游戏开始日期之前签署 | is_historical_treaty = yes/no | boolean |
| is_renegotiation | 检查 scope 条约是否在修订一份现有条约 | scope:some_treaty = { if = { limit = { is_renegotiation = yes } } } | boolean |
| event target | 描述 | 目标 scope |
|---|---|---|
| amended_treaty | 转到当前 scope 条约所修订的那份条约 | treaty |
| binding_period | 获取当前 scope 条约在签署时的原始有效期限（天数） | value |
| first_country | 转到以下任意对象的 first_country：外交条约、条约选项、条约条款所属的条约、条约条款选项（仅限双向条款类型） | country |
| remaining_binding_period | 获取当前 scope 条约当前剩余的有效期限（天数） | value |
| second_country | 转到以下任意对象的 second_country：外交条约、条约选项、条约条款所属的条约、条约条款选项（仅限双向条款类型） | country |

### 条约条款选项 scope

| effect | 描述 | 示例 | 目标 |
|---|---|---|---|

| trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| has_type | 检查当前 scope 对象是否具有给定字符串所标识的类型 | scope:some_object = { has_type = defensive_pact } |  |
| max_contraventions | 检查当前 scope 条款或条款选项的条款类型的最大违约次数 | scope:treaty_article = { max_contraventions >= 1 } | value |

| event target | 描述 | 目标 scope |
|---|---|---|
| first_country | 转到以下任意对象的 first_country：外交条约、条约选项、条约条款所属的条约、条约条款选项（仅限双向条款类型） | country |
| input_building_type | 转到条约条款中输入的建筑类型 | building_type |
| input_company | 转到条约条款中输入的公司 | company |
| input_country | 转到条约条款中输入的国家 | country |
| input_goods | 转到条约条款中输入的商品 | goods |
| input_law | 转到条约条款中输入的法律 | law_type |
| input_market_goods | 转到条约条款中输入的市场商品（示例：input_market_goods:root） | market_goods |
| input_quantity | 转到条约条款中输入的数量 | value |
| input_ship | 转到条约条款中输入的舰船 | ship |
| input_state | 转到条约条款中输入的州 | state |
| input_strategic_region | 转到条约条款中输入的战略区域 | strategic_region |
| second_country | 转到以下任意对象的 second_country：外交条约、条约选项、条约条款所属的条约、条约条款选项（仅限双向条款类型） | country |
| source_country | 转到以下任意对象的 source_country：条约条款（仅限单向条款类型）、条约条款选项（仅限单向条款类型） | country |
| target_country | 转到以下任意对象的 target_country：条约条款（仅限单向条款类型）、条约条款选项（仅限单向条款类型） | country |

## 参考

1. ↑ 可能存在 bug，并不会阻止条款

模组制作
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [变量](Variable.md) |
|---|---|---|

| 脚本内容 | [决议](Decision modding.md) • [事件](Event modding.md) • [历史](History modding.md) • [日志](Journal modding.md) • [修正](Modifier modding.md) • 目标 • [Scripted gui](Scripted gui.md) |
|---|---|---|

| 脚本类型 | [建筑](Building modding.md) • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • 条约 • [战争目标](War goal modding.md) |
|---|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [可自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图像](Event images.md) • [图形资源](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|---|

| 音频 | 音乐 • [声音](Sound modding.md) |
|---|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [模组](Mod.md) • [模组兼容性](Mod compatibility.md) • [模组结构](Mod structure.md) • [脚本测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|---|

| 指南 | [模组翻译](Mod translation.md) • [新国家模组制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州模组制作指南](State modding guide.md) |
|---|---|---|