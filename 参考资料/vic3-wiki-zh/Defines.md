---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Defines
source: https://vic3.paradoxwikis.com/Defines
pageid: 3688
categories: [1.13, Modding]
fetched: 2026-10-27
---
本文已针对游戏当前 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

**Defines** 是引擎使用的变量。它们调控未开放给脚本系统的基本游戏行为与设置（利益集团支持度阈值、镜头视野等）。

Defines 是静态且全局的：它们作用于整个游戏，无法被动态更改。

原版数值配置于文件夹 /Victoria 3/game/common/defines 中，主要在 `00_defines.txt` 里。

本页各列表各代表 defines 的一个分区；在 defines 文件中，这些分区均带有前缀 `N`，例如 `NCountry`。

## Define 修改

Defines 可以单独或成批修改，而无需覆盖整个 defines 文件。这样能更好地保持兼容性，也更容易跟上未来补丁的改动。

要修改某个 define，可在 <mod>/common/defines/ 中创建一个在原版文件之后加载的新文件，例如 `01_mod_defines.txt`。在该文件中，为每一组要修改的 defines 添加一个块，并把修改后的 defines 放入这些块中，例如：

```
NCountry = {
	INCORPORATION_TIME_NO_MATCH = 100	# Base game 20 years; Years if the state's Homeland cultures have nothing in common with the country's primary cultures
}

NDiplomacy = {
	COUNTRY_TIER_HEGEMONY_PRESTIGE = 150	# Base game 50
}
```

若多个 mod 修改了同一个 define，则加载文件名排序最靠后的 mod 决定该 define 的最终数值。

## 00_defines

### Game

| Define | 默认值 | 开发者注释 |
|---|---|---|
| START_DATE | "1836.1.1" |  |
| END_DATE | "1936.1.1" |  |
| SAVE_VERSION | 0 |  |
| MP_LAG_TICKS_BOUNDS | 28 | # Host will advance up to a week ahead of players ( 7 * 4 ) |
| DEAD_OBJ_UNDESTROYED_DAYS | 22 | # number of days "killed"/removed objects will persist in memory before ultimately destroyed as they are referenced by events etc |
| MAX_NUMBER_OF_AUTOSAVES | 5 | # The game will only keep the MAX_NUMBER_OF_AUTOSAVES latest autosaves. |

### JominiMap

| Define | 默认值 | 开发者注释 |
|---|---|---|
| WORLD_EXTENTS_X | 8192 |  |
| WORLD_EXTENTS_Y | 24 | #This determines the max height of the world. Original settings = 25.5 |
| WORLD_EXTENTS_Z | 3615 |  |
| WATERLEVEL | 1.74 | #Original Settings 3.7 |

### Country

| Define | 默认值 | 开发者注释 |
|---|---|---|
| DEFAULT_COUNTRY_TYPE | "recognized" |  |
| COMPANY_COUNTRY_TYPE | "company" |  |
| COMPANY_FALLBACK_COUNTRY_TYPE | "colonial" |  |
| DEFAULT_MAX_NUM_COUNTRY_FORMATION_CANDIDATES | 3 | # If nothing is specified in the country formation, this is used |
| COUNTRY_FORMATION_CANDIDATE_MIN_RANK | 6 | # countries with a lower rank value than this cannot be formation candidates |
| MOVE_CAPITAL_COOLDOWN_YEARS | 5 |  |
| MOVE_MARKET_CAPITAL_COOLDOWN_YEARS | 5 |  |
| MAX_POWER_EFFECT | 1.0 | # The max by which a power excess/deficiency modifier can scale |
| GREAT_POWER_RANK_KEY | "great_power" |  |
| MAJOR_POWER_RANK_KEY | "major_power" |  |
| MINOR_POWER_RANK_KEY | "minor_power" |  |
| SPLIT_STATE_DOMINANT_LAND_SHARE_THRESHOLD | 0.5 | # States with more land share than this can use the region's name |
| SPLIT_STATE_PRIME_LAND_WEIGHT | 5.0 |  |
| CAPITAL_CULTURE_CORE_WEIGHT | 10 |  |
| CAPITAL_NON_INCORPORATED_WEIGHT | 0.001 |  |
| DEFAULT_SUBSISTENCE_BUILDING | "building_subsistence_farm" |  |
| CONSTRUCTION_CAMP_BUILDING | "building_construction_sector" |  |
| BARRACKS_BUILDING | "building_barrack" |  |
| NAVAL_ADMINISTRATION_BUILDING | "building_naval_administration" |  |
| NAVAL_FORTIFICATION_BUILDING | "building_naval_fortification" |  |
| PORT_BUILDING | "building_port" |  |
| URBAN_CENTER_BUILDING | "building_urban_center" |  |
| CONSCRIPTION_CENTER_BUILDING | "building_conscription_center" |  |
| NAVAL_LOGISTICS_CENTER_BUILDING | "building_naval_logistics_center" |  |
| LAND_LOGISTICS_CENTER_BUILDING | "building_land_logistics_center" |  |
| CONSCRIPTION_CENTER_LEVEL_POPULATION_DIVISOR | 1000 | # 平民人口除以此数值以计算征兵中心最大等级 [>=1] |
| TRADE_CENTER_BUILDING | "building_trade_center" |  |
| MANOR_HOUSE_BUILDING | "building_manor_house" |  |
| FINANCIAL_DISTRICT_BUILDING | "building_financial_district" |  |
| RAILWAY_BUILDING | "building_railway" |  |
| POWER_BLOC_STATUE_BUILDING | "building_power_bloc_statue" |  |
| COMPANY_HEADQUARTER_BUILDING | "building_company_headquarter" |  |
| COMPANY_REGIONAL_HEADQUARTER_BUILDING | "building_company_regional_headquarter" |  |
| CONSTRUCTION_QUEUE_INCREMENT_SHIFT | 5 | # 按住 Shift 时建筑建造队列使用的增减幅度 |
| CONSTRUCTION_QUEUE_INCREMENT_CONTROL | 10 | # 按住 Ctrl 时建筑建造队列使用的增减幅度 |
| WEEKS_TO_STORE_LOYALIST_RADICAL_STATISTICS | 52 | # 存储并显示的忠诚派/激进派统计数据的周数 |
| INCORPORATION_TIME_SAME_CULTURE | 2 | # 若该州是该国某一主流文化的本土（Homeland）时的年数 |
| INCORPORATION_TIME_SAME_HERITAGE_AND_LANGUAGE | 5 | # 若该州是某一与该国主流文化之一的传承（Heritage）和语言（Language）特质均匹配的文化的本土时的年数 |
| INCORPORATION_TIME_SAME_HERITAGE_OR_LANGUAGE | 10 | # 若该州是某一与该国主流文化之一的传承特质匹配的文化的本土时的年数 |
| INCORPORATION_TIME_SAME_TRAIT_GROUP | 15 | # 若该州是某一与该国主流文化拥有任一共同特质的文化的本土时的年数 |
| INCORPORATION_TIME_NO_MATCH | 25 | # 若该州的本土文化与该国主流文化毫无共同之处时的年数 |
| INCORPORATION_TIME_MIN_MULTIPLIER | 0.1 | # 同化速度无法通过修正（modifier）降低到低于此数值 |
| JOURNAL_ENTRY_UPDATE_ACTIVE | 4 | # 活跃（可能）日志条目每次更新之间的刻数，可在日志条目类型上覆盖 |
| JOURNAL_ENTRY_UPDATE_INACTIVE | 14 | # 非活跃日志条目每次更新之间的刻数，可在日志条目类型上覆盖 |
| MAX_TRADITION_TRAITS_PER_CULTURE | 4 | # 一种文化最多可拥有的传统特质数量 |
### 政治

| Define | 默认值 | 开发者注释 |
|---|---|---|
| GOVERNANCE_PRINCIPLES_GROUP | "lawgroup_governance_principles" | # 该法律组中的法律用于 power_bloc_worst_progressiveness_difference_government_type trigger，以代表治理原则 |
| DISTRIBUTION_OF_POWER_GROUP | "lawgroup_distribution_of_power" | # 该法律组中的法律用于 power_bloc_worst_progressiveness_difference_government_type trigger，以代表权力分配 |
| TARIFF_LAW_GROUP | "lawgroup_trade_policy" | # 该法律组中的法律作为玩家的关税法律显示 |
| TAX_LAW_GROUP | "lawgroup_taxation" | # 该法律组中的法律作为玩家的税收法律显示 |
| NUM_TIMES_TO_LOOP_THROUGH_LAWS | 3 | # 创建法律集时，遍历所有法律组的次数？之所以不止一次，是为了允许修改由其他法律解锁的法律 |
| DEFAULT_IDEOLOGY | "ideology_moderate" | # 若无法为人物选择意识形态，则用作后备 |
| CHILD_IDEOLOGY | "ideology_child" | # 儿童使用此意识形态，年满 16 岁后会被替换 |
| MIN_POP_NUMBER_JOIN_OR_LEAVE_IG | 10 | # 单次更新中变更利益集团的人口/支持的最大数量的下限（覆盖下方最大比例） |
| MAX_POP_FRACTION_JOIN_OR_LEAVE_IG | 0.05 | # 单次更新中一个人口中可变更利益集团的最大比例（针对每个利益集团） |
| MIN_POP_NUMBER_JOIN_OR_LEAVE_MOVEMENT | 10 | # 单次更新中变更政治运动的人口/支持的最大数量的下限（覆盖下方最大比例） |
| MAX_POP_FRACTION_JOIN_OR_LEAVE_MOVEMENT | 0.1 | # 单次更新中一个人口中可变更政治运动的最大比例（针对每个运动） |
| MOVEMENT_POP_SUPPORT_ATTRACTION_CAP | 0.01 | # 一个人口中支持某运动的人口比例上限为（运动吸引力 × 此值），以避免吸引力低但无竞争的运动吸引走国内的每一个人口 |
| # 具有文化/宗教认同的运动要生成，该文化/宗教必须至少满足以下两个阈值之一： |  |  |
| MOVEMENT_IDENTITY_MIN_INDIVIDUALS_ABSOLUTE_THRESHOLD | 200000 | # 个人的绝对数量 |
| MOVEMENT_IDENTITY_MIN_INDIVIDUALS_RELATIVE_THRESHOLD | 0.2 | # 相对于国家人口的个人数量 |
| MOVEMENT_DEFAULT_MIN_SUPPORT_TO_CREATE | 0.025 | # 创建政治运动所需的默认支持度（以计算值表示），可在数据库中覆盖 |
| MOVEMENT_DEFAULT_MIN_SUPPORT_TO_MAINTAIN | 0.01 | # 维持政治运动所需的默认支持度（以实际值表示），可在数据库中覆盖 |
| MOVEMENT_FAILED_MOVEMENT_DURATION_DAYS | 365 | # 记住某个政治运动创建失败、且不再针对完全相同的运动重试的时长（天数） |
| MOVEMENT_MIN_SUPPORT_GRACE_MONTHS | 12 | # 政治运动在创建后的这几个月内不会因支持度过低而解散 |
| MOVEMENT_AGITATOR_STICKYNESS | 2.0 | # 鼓动家在考虑是否更换运动时，会将其已支持运动的分数乘以此倍率 |
| # 以下三个 defines 之和应为 1.0 |  |  |
| MOVEMENT_SUPPORT_POPULAR_SUPPORT_FRACTION | 0.34 | # 政治运动总支持度中来自民众支持的比例 |
| MOVEMENT_SUPPORT_MILITARY_SUPPORT_FRACTION | 0.33 | # 政治运动总支持度中来自军事支持的比例 |
| MOVEMENT_SUPPORT_WEALTH_SUPPORT_FRACTION | 0.33 | # 政治运动总支持度中来自财富支持的比例 |
| MOVEMENT_WEEKLY_RADICALISM_CHANGE | 0.01 | # 运动的激进程度每周向其计算目标值变化多少 |
| MOVEMENT_MONTHLY_RADICALS_THRESHOLD | 0.5 | # 达到这一激进度时，政治运动的支持者开始每月被激进化，数量按激进度数值成比例缩放 |
| MOVEMENT_MONTHLY_RADICALS_SCALING_MIN | 0.005 | # 超过激进化阈值后，每月被激进化的支持者最低百分比 |
| MOVEMENT_MONTHLY_RADICALS_SCALING_MAX | 0.025 | # 超过激进化阈值后，每月被激进化的支持者最高百分比 |
| MOVEMENT_LOYALISTS_ON_APPROVED_ENACTMENT | 0.25 | # 当政治运动赞成的法律通过时，变得更加忠诚的支持者百分比 |
| # 激进度低于此值的政治运动不会影响法律通过几率 # 此外，当一项他们关注的法律正在通过时，政治运动的激进度不会降到低于此值，以免通过法律带来的激进度下降产生反效果 |  |  |
| MOVEMENT_MIN_RADICALISM_FOR_LAW_ENACTMENT_IMPACT | 0.25 |  |
| MOVEMENT_IMMEDIATE_RADICALISM_FROM_ENACTMENT | 0.5 | # 法律通过带来的目标激进度影响，该乘数会在通过开始时立即生效 |
| MOVEMENT_IMMEDIATE_RADICALISM_FROM_CANCELLATION | -0.5 | # 法律通过带来的目标激进度影响，该乘数会在通过被取消时立即生效 |
| MOVEMENT_RADICALISM_FROM_ACTIVE_LAW_STANCE | -0.05 | # 乘以政治运动对每项现行法律的立场（正面立场 = 负面激进度） |
| MOVEMENT_RADICALISM_FROM_ENACTED_LAW_STANCE | -0.25 | # 乘以政治运动对当前或近期通过的法律的相对立场（正面立场 = 负面激进度） |
| MOVEMENT_RADICALISM_FROM_RADICAL_SUPPORTERS | 1.0 | # 与政治运动支持者中激进派的比例成比例 |
| MOVEMENT_RADICALISM_FROM_LOYALIST_SUPPORTERS | -0.75 | # 与政治运动支持者中忠诚派的比例成比例 |
| MOVEMENT_RADICALISM_FROM_SUPPRESSION | 0.0 | # 受到镇压的政治运动激进度增加此数值 |
| MOVEMENT_RADICALISM_FROM_BOLSTERING | 0.0 | # 受到扶持的政治运动激进度降低此数值 |
| MOVEMENT_PRESSURE_IDEOLOGY_FACTOR | 4.0 | # 来自利益集团的人物选择某种意识形态的几率会随信奉该意识形态的政治运动施加的压力总量而增加 # 压力达到 100% 时，该意识形态的权重乘以 ( 1 + 此值 ) |
| colspan=3 | # 利益集团下一任领袖信奉某种意识形态的几率会随信奉该意识形态的潜在领袖的总显赫度而增加 # 与政治运动压力不同，此效果不会在为该利益集团的其他人物生成意识形态时生效 # 此数值还受利益集团上各角色专属权重影响，例如指挥官显赫度的 commander_leader_weight # 乘数为 ( 1 + ( 此值 * 总显赫度 * 角色权重 ) ) |  |
| CHARACTER_PROMINENCE_AND_ROLE_LEADER_IDEOLOGY_FACTOR | 0.04 |  |
| IG_MAX_INFLUENCING_MOVEMENTS | 3 | # 一个利益集团的影响力政治运动数量不能超过此数 |
| IG_SUPPORTING_MOVEMENT_MIN_SUPPORTING_CLOUT | 0.05 | # 一个政治运动必须获得利益集团内至少此百分比的政治力量支持，才会显示为该政治运动的支持利益集团 |
| IG_INFLUENCING_MOVEMENT_MIN_SUPPORTING_CLOUT | 0.10 | # 一个政治运动必须获得利益集团内至少此百分比的政治力量支持，才会成为该利益集团的影响力政治运动 |
| IG_INFLFLUENCING_MOVEMENT_STICKYNESS | 1.25 | # 在判断当前影响力政治运动是否继续保有影响力时，将其支持的政�治力量乘以此值 |
| # 以下数值决定一个利益集团与一场叛乱性政治运动在意识形态上可以有多大分歧，并仍依据其认可度加入内战一方 # 满意/忠诚的利益集团绝不会加入内战 |  |  |

（注：第 20 行标识符按原文应为 `IG_INFLUENCING_MOVEMENT_STICKYNESS`，上文中显示为 `IG_INFLFLUENCING_MOVEMENT_STICKYNESS` 系笔误，此处已更正。如需严格原样保留，请以原文为准。）
| IG_MAX_IDEOLOGICAL_DELTA_TO_JOIN_CIVIL_WAR_NEUTRAL | 1 |  |
| IG_MAX_IDEOLOGICAL_DELTA_TO_JOIN_CIVIL_WAR_UNHAPPY | 1.5 |  |
| IG_MAX_IDEOLOGICAL_DELTA_TO_JOIN_CIVIL_WAR_ANGRY | 2 |  |
| # 利益集团领袖的意识形态对相关法律持有的态度，会以该乘数影响其加入内战时的意识形态分歧 |  |  |
| IG_MAX_IDEOLOGICAL_DELTA_TO_JOIN_CIVIL_WAR_LEADER_FACTOR | 2.0 |  |
| BASE_IG_APPROVAL | 0 | # 利益集团支持度的基础值 |
| MIN_IG_APPROVAL | -20 | # 利益集团支持度的最小值 |
| MAX_IG_APPROVAL | 20 | # 利益集团支持度的最大值 |
| MIN_IG_APPROVAL_FROM_LAWS | -5 | # 利益集团从“成文”法律中获得的支持度总和不会低于此值 |
| MAX_IG_APPROVAL_FROM_LAWS | 5 | # 利益集团从“成文”法律中获得的支持度总和不会高于此值 |
| IG_APPROVAL_FROM_LOYALISTS | 15 | # 如果利益集团政治力量的 100% 来自忠诚派，则支持度按此数值变化 |
| IG_APPROVAL_FROM_RADICALS | -15 | # 如果利益集团政治力量的 100% 来自激进派，则支持度按此数值变化 |
| IG_LAW_DESIRE_RADICAL_CHANGE_THRESHOLD | 2 | # 立场差值达到或超过此值即被视为激进 |
| IG_LAW_DESIRE_EXTREME_CHANGE_THRESHOLD | 3 | # 立场差值达到或超过此值即被视为极端 |
| IG_APPROVAL_FROM_LAW | 1 | # 利益集团对符合/违背其意识形态的法律的支持度/反对度 |
| IG_APPROVAL_FROM_LAW_STRONG_STANCE | 2 | # 利益集团对强烈符合/强烈违背其意识形态的法律的支持度/反对度 |
| IG_APPROVAL_FROM_LAW_CHANGE | 5 | # 利益集团对改立其他法律的支持度/反对度 |
| IG_APPROVAL_FROM_RADICAL_LAW_CHANGE | 10 | # 利益集团对改立其他法律的支持度/反对度（若该变更属重大变更） |
| IG_APPROVAL_FROM_EXTREME_LAW_CHANGE | 20 | # 利益集团对改立其他法律的支持度/反对度（若该变更属极端变更） |
| IG_IN_GOVERNMENT_APPROVAL | 0 | # 利益集团处于政府时附加的值 |
| IG_IN_OPPOSITION_APPROVAL | 0 | # 利益集团处于反对派（且不强势）时附加的值 |
| IG_POWERFUL_IN_OPPOSITION_APPROVAL | -1 | # 强势的利益集团处于反对派时附加的值 |
| STARTUP_MIN_LEGITIMACY_IG_BARRIER | 40 | # 游戏开始时，允许将降低合法性的利益集团移出政府时所需的最低合法性 |
| APPROVAL_THRESHOLD_ANGRY | -10 | # 支持度达到或低于此值时，利益集团被视为愤怒 |
| APPROVAL_THRESHOLD_UNHAPPY | -5 | # 支持度达到或低于此值时，利益集团被视为不满 |
| APPROVAL_THRESHOLD_HAPPY | 5 | # 支持度达到或高于此值时，利益集团被视为满意 |
| APPROVAL_THRESHOLD_LOYAL | 10 | # 支持度达到或高于此值时，利益集团被视为忠诚 |
| CHANGED_LAW_APPROVAL_MONTHS | 60 | # 法律变更带来的支持度/反对度在该法律链条结束后会持续多少个月 |
| # 如果当前生效法律与替代法律之间的进步性差值达到此值，则该诉求被视为激进诉求 # 只有当不存在政府可以转而诉求的更温和的替代方案时，激进诉求才会出现 |  |  |
| GOVERNMENT_RADICAL_PETITION_THRESHOLD | 100 |  |
| LAW_ENACTMENT_MIN_TOTAL_DAYS | 1 | # 立法检查点所需的最少总天数 [>=1] |
| LAW_ENACTMENT_DEFAULT_BASE_DAYS | 100 | # 达到立法检查点所需的默认基础天数 [>=1] |
| LAW_ENACTMENT_COOLDOWN_DAYS | 730 | # 当立法失败，或在至少一个检查点之后被手动中止时，该法律在这些天数内不能再次尝试颁布 [>=0] |
| LAW_ENACTMENT_ADVANCE_FACTOR | 2 | # _基础_推进概率为成功概率乘以此系数 [>=1] |
| LAW_ENACTMENT_RULER_IDEOLOGY_EFFECT | 0.05 | # 统治者的意识形态会依据相对支持度，以此数值影响法律通过或停滞的概率 |
| LAW_ENACTMENT_LAW_COMMITMENT_EFFECT | 0.05 | # 通过条约承诺颁布某项法律时，会按该数值提升通过概率，数值随受约国对缔约国拥有的等级数而缩放 |
| LAW_ENACTMENT_MOVEMENT_SUPPORT_PASS_EFFECT | 1.0 | # 政治运动支持度对法律通过几率的影响 |
| LAW_ENACTMENT_MOVEMENT_SUPPORT_STALL_EFFECT | 1.0 | # 政治运动支持度对法律停滞几率的影响 |
| LAW_ENACTMENT_IG_CLOUT_STALL_EFFECT | 1.0 | # 反对利益集团的政治力量对法律停滞几率的基础影响 |
| LAW_ENACTMENT_IG_NEUTRAL_MULT | 0.5 | # 中立利益集团的反对停滞效果乘以此系数 |
| LAW_ENACTMENT_IG_UNHAPPY_MULT | 1.0 | # 不满利益集团的反对停滞效果乘以此系数 |
| LAW_ENACTMENT_IG_ANGRY_MULT | 1.5 | # 愤怒利益集团的反对停滞效果乘以此系数 |
| LAW_ENACTMENT_MAX_PHASES | 3 | # 法律制定推进到此阶段即视为成功完成 |
| LAW_MIN_SUCCESS_CHANCE | 0.01 | # 法律必须至少有这个最低几率才会被考虑。 |
| STATE_BUREAUCRACY_BASE_COST | 10 | # 每个已整合州的行政力基础成本 |
| STATE_BUREAUCRACY_POP_BASE_COST | 4 | # 每个人口倍数的行政力基础乘数 |
| STATE_BUREAUCRACY_POP_MULTIPLE | 100000 | # 行政力成本所基于的人口数量 |
| MINIMUM_INVESTMENT_COST | 10 | # 每级投资等级的行政力绝对最低成本 |
| POWERFUL_IG_THRESHOLD | 0.20 | # 政治力量超过此值的利益集团被视为具有影响力 |
| POWERFUL_IG_CUTOFF | 0.18 | # 强势利益集团的政治力量低于此值后将不再具有影响力 |
| POWERFUL_IG_TRAIT_BONUS | 1 | # 具有影响力的利益集团的所有特质修正效果按此值增强，1 = +100% |
| IG_TRAIT_STICKINESS | 2 | # 若利益集团特质已激活，需要这么多的支持度差值才能将其停用 |
| MARGINAL_IG_THRESHOLD | 0.05 | # 政治力量高于此值的利益集团被视为相关集团，低于此值的则被边缘化（除非同时处于政府中） |
| MARGINAL_IG_CUTOFF | 0.04 | # 已被视为相关的利益集团只有在跌至此值以下才会重新被边缘化。 |
| MARGINAL_IG_JOIN_PARTY_POPULATION_THRESHOLD | 0.025 | # 至少获得这个比例人口支持的边缘利益集团能够加入政党并摆脱边缘地位 |
| MIN_AMENABILITY | 0 |  |
| MAX_AMENABILITY | 100 |  |
| MIN_AMENABILITY_TENSE_NEGOTIATION | 25 |  |
| MIN_AMENABILITY_NORMAL_NEGOTIATION | 50 |  |
| MIN_AMENABILITY_FRIENDLY_NEGOTIATION | 75 |  |
| RECENT_PARTY_DAYS | 14 | # 政党在 RECENT_PARTY_DAYS 天数范围内成立即被视为新近成立 |
| MAX_GOVERNMENT_ALTERNATIVES_TO_CONSIDER_AI | 64 | # 在评估政府改革方案（针对 AI）时，只考虑这么多种组合（按平均政治力量降序排列）[>=1] |
| MAX_GOVERNMENT_ALTERNATIVES_TO_CONSIDER_PLAYER | 256 | # 在评估政府改革方案（界面向玩家推荐的 3 种方案）时，只考虑这么多种组合（按平均政治力量降序排列）[>=3] |
| MAX_GOVERNMENT_ALTERNATIVES_OPTIONS_WANTED_FOR_VALIDATION | 8 | # 在政府验证阶段评估政府改革方案时使用 |
| MAX_GOVERNMENT_ALTERNATIVES_TO_CONSIDER_FOR_VALIDATION | 256 | # 在政府验证阶段评估政府改革方案时使用 |
| DEFAULT_LAW_ACTIVATION_DATE | "1836.1.1" |  |
| CIVIL_WAR_COOLDOWN_MONTHS | 9 | # 一场内战结束后，需要这么长时间才能开始下一场内战 |
| FAILED_CIVIL_WAR_START_COOLDOWN_MONTHS | 3 | # 若一场政治运动在试图发动内战时未能获得任何支持的州或（对革命而言）支持的陆军单位，则需等待这么长时间后再次尝试 |
| # 若可能爆发多场内战，而当前活跃内战的活跃度较低，则其可能被更可行的内战取代 # 这是另一场内战取代当前活跃内战所需的最低差值 |  |  |
| MIN_ACTIVISM_DELTA_TO_REPLACE_OTHER_CIVIL_WAR | 0.1 |  |
| # 以下数值用于计算当内战未指定明确的 target_fraction_of_states 时，起义的州的目标数量 # 这只是一个目标值——最终结果可能因内战脚本中定义的州权重而有所不同 |  |  |
| CIVIL_WAR_UPRISING_STATES_DEFAULT_CLOUT_FACTOR | 1.0 | # 国家总州数的比例，乘以革命利益集团的政治力量 |
| CIVIL_WAR_UPRISING_STATES_DEFAULT_POPULAR_SUPPORT_FACTOR | 0.5 | # 国家总州数的比例，乘以政治运动的民众支持度 |
| CIVIL_WAR_UPRISING_STATES_DEFAULT_MILITARY_SUPPORT_FACTOR | 0.25 | # 国家总州数的比例，乘以政治运动的军事支持度 |
| CIVIL_WAR_UPRISING_STATES_DEFAULT_WEALTH_SUPPORT_FACTOR | 0.25 | # 国家总州数的比例，乘以政治运动的财富支持度 |
| CIVIL_WAR_UPRISING_STATES_DEFAULT_MIN_FRACTION | 0.10 | # 尝试起义的国家总州数的最小比例 |
| CIVIL_WAR_UPRISING_STATES_DEFAULT_MAX_FRACTION | 0.75 | # 尝试起义的国家总州数的最大比例 |
| CIVIL_WAR_POTENTIAL_UPRISING_STATE_MIN_MULTIPLIER | 0.01 | # 起义州的权重不能因当地人口的政治力量/认同占比而低于此值 |
| CIVIL_WAR_UPRISING_STATE_RANDOM_FACTOR | 0.5 | # 此值越高，起义州的选择就越随机 |
| CIVIL_WAR_UPRISING_STATE_CONNECTIONS_FACTOR | 1.0 | # 起义州的得分乘以（1 + 此数值 * 与其相连的其他起义州数量） |
| CIVIL_WAR_UPRISING_STATE_NON_CONNECTED_SECESSION_FACTOR | 0.01 | # 对于不与同一区域内任何其他叛乱州相连的脱离州，其起义州得分乘以此值 |
| CIVIL_WAR_UPRISING_ISOLATED_STATE_FACTOR | 100.0 | # 如果起义州被起义州与最忠诚的州隔开，其得分乘以此值 |
| CIVIL_WAR_NON_CONTIGUOUS_UPRISING_STATE_FACTOR | 0.25 | # 如果起义会导致切断的忠诚州数量大于剩余应叛乱的州数量，起义州的得分乘以此值 |
| CIVIL_WAR_UPRISING_ARMY_TARGET_DELTA_FACTOR | 10.0 | # 根据该州的倒戈对理想叛乱陆军单位数量的影响，对州是否起义进行加权的程度 |
| CIVIL_WAR_UPRISING_NAVY_TARGET_DELTA_FACTOR | 5.0 | # 根据该州的倒戈对理想叛乱海军单位数量的影响，对州是否起义进行加权的程度 |
| # 国家本土以外被视为殖民地的区域，将根据以下逻辑完全忠诚或完全叛乱 |  |  |
| CIVIL_WAR_UPRISING_STATES_OVERSEAS_HIGH_UNINCORPORATED_FRACTION | 0.5 | # 非首都区域中未合并州的比例达到此百分比或以上时，即使与首都隔着较近的海上相邻关系，也会被视为“殖民地” |
| CIVIL_WAR_COLONIAL_UPRISING_MIN_CHANCE | 0.25 | # 如果殖民地区域的叛乱几率低于此值，它将始终保持忠诚 |
| CIVIL_WAR_COLONIAL_UPRISING_CHANCE_WEALTH_SUPPORT_FACTOR | 2.0 | # 每个殖民地区域的叛乱几率，乘以起义运动的财富支持度 |
| CIVIL_WAR_COLONIAL_UPRISING_CHANCE_CLOUT_FACTOR | 1.0 | # 每个殖民地区域的叛乱几率，乘以该区域内起义利益集团的政治力量 |
| CIVIL_WAR_UPRISING_STATE_EXCESSIVE_ARMY_FRACTION | 0.5 | # 如果一个州拥有至少此比例的区域陆军 |
| CIVIL_WAR_UPRISING_ARMY_FRACTION_MILITARY_SUPPORT_FACTOR | 0.75 | # 应叛乱的陆军目标比例，乘以起义运动的军事支持度 |
| CIVIL_WAR_UPRISING_ARMY_FRACTION_CLOUT_FACTOR | 0.25 | # 应叛乱的陆军目标比例，乘以该地区起义利益集团的政治力量 |
| CIVIL_WAR_UPRISING_NAVY_FRACTION_MILITARY_SUPPORT_FACTOR | 0.75 | # 应叛乱的海军目标比例，乘以起义运动的军方支持度 |
| CIVIL_WAR_UPRISING_NAVY_FRACTION_CLOUT_FACTOR | 0.25 | # 应叛乱的海军目标比例，乘以该地区起义利益集团的政治力量 |
| # 起义国家会在其首都获得一批军事商品注入，以下数值控制注入哪些商品以及数量 # 乘数基于分配给内战的州以及内战前的市场卖出与买入订单 |  |  |
| CIVIL_WAR_STOCKPILE_SMALL_ARMS_GOODS_TYPE | "small_arms" |  |
| CIVIL_WAR_STOCKPILE_SMALL_ARMS_MULTIPLIER | 0.80 |  |
| CIVIL_WAR_STOCKPILE_AMMUNITION_GOODS_TYPE | "ammunition" |  |
| CIVIL_WAR_STOCKPILE_AMMUNITION_MULTIPLIER | 0.80 |  |
| CIVIL_WAR_STOCKPILE_ARTILLERY_GOODS_TYPE | "artillery" |  |
| CIVIL_WAR_STOCKPILE_ARTILLERY_MULTIPLIER | 0.65 |  |
| CIVIL_WAR_MAX_PROGRESS_AT_CHECKPOINT | 0.25 | # 无论激进程度如何，内战在每个检查点最多推进此数值 |
| MIN_RADICALISM_FOR_CIVIL_WAR_PROGRESSION | 0.75 | # 政治运动必须达到此激进程度，内战才会开始组织 |
| MIN_RADICALISM_FOR_CIVIL_WAR_START | 1.0 | # 允许内战在此激进程度或以上时爆发 |
| CIVIL_WAR_PROGRESS_DECAY | 0.1 | # 支持不足的内战其进度会以此速率衰减 |
| CIVIL_WAR_PROGRESS_RADICALISM_WEIGHT | 0.2 | # 内战基于运动的激进程度获得进度，并乘以此权重（可能受修正影响） |
| CIVIL_WAR_CHECKPOINT_INTERVAL_BASE_WEEKS | 8 | # 内战进度将每隔这么多周更新一次（可能受修正影响） |
| CIVIL_WAR_CHECKPOINT_INTERVAL_MAXIMUM_WEEKS | 52 | # 此值作为上限，防止修正将进度速度降为零 |
| CIVIL_WAR_CONSCRIPTION_RATE_POPULAR_SUPPORT_MULTIPLIER | 0.25 | # 在 100% 民众支持度下，起义各州获得此乘数的 civil_war_conscription 修正 |
| CIVIL_WAR_CONSCRIPTION_RATE_CLOUT_MULTIPLIER | 0.05 | # 在来自支持的利益集团 100% 政治力量下，起义各州获得此乘数的 civil_war_conscription 修正 |
| CIVIL_WAR_CONSCRIPTION_RATE_MAX_MULTIPLIER | 0.1 | # civil_war_conscription 修正的总乘数不能超过此数值（此值有意设定得远低于上述可能的最大值，因为运动极少拥有超过 10-20% 的民众支持度） |
| CIVIL_WAR_LOSER_IG_AND_MOVEMENT_DEBUFF_YEARS | 20 | # 在革命中失败的利益集团所受减益的持续年数 |
| SECESSION_WON_LOYALISTS_INCREASED_PERCENTAGE | 0.5 | # 分离运动胜利后，分离国家中分离文化的人口中有此比例会变得更加忠诚 |
| SECESSION_START_RADICALS_REDUCED_PERCENTAGE | 1.0 | # 分离战争开始时，已分离各州中分离文化人口的激进派数量将减少此数值 |
| SECESSION_LOST_RADICALS_REDUCED_PERCENTAGE | 1.0 | # 分离运动被镇压时，已分离各州中分离文化人口的激进派数量将减少此数值 |
| REVOLUTION_START_REBEL_IG_RADICALS_REDUCED_PERCENTAGE | 1.0 | # 革命开始时，人口的激进派数量将减少此数值（相对于起义利益集团的成员数量） |
| REVOLUTION_ENDED_RADICAL_BASE_REMOVAL_PERCENTAGE | 0.5 | # 革命结束时，无论属于哪个利益集团，所有人口中会有此基础比例的激进派被移除，以体现“内战疲劳” |
| REVOLUTION_LOST_REBEL_IG_RADICALS_REDUCED_PERCENTAGE | 0.25 | # 革命被镇压时，人口中的激进派数量将额外减少这一比例（相对于被击败的利益集团的成员数） |
| REVOLUTION_WON_LOYAL_IG_RADICALS_REDUCED_PERCENTAGE | 0.5 | # 革命被镇压时，人口中的激进派数量将额外减少这一比例（相对于获胜利益集团的成员数） |
| IG_SUPPRESSION_COST | 200 | # 压制一个利益集团所需的权威力（AUT）数量 |
| IG_BOLSTER_COST | 200 | # 扶持一个利益集团所需的权威力（AUT）数量 |
| DEFAULT_GOODS_TAX_COST | 100 | # 默认情况下对一种商品征税所需的权威力（AUT）数量 |
| TURMOIL_STATE_EFFECTS_THRESHOLD | 0.25 | # 一个州需要达到多少动荡才会开始受到全州性效果的影响 |
| TURMOIL_STATE_HIGH_EFFECTS_THRESHOLD | 0.50 | # 动荡超过此值时，施加更严厉的修正 |
| TURMOIL_STATE_EXTREME_EFFECTS_THRESHOLD | 0.75 | # 动荡超过此值时，施加最严厉的修正 |
| OBSTINANCE_MAX | 0.2 | # 一个州可拥有的最高顽固度（达到最大值时，该州将获得顽固度修正的 100% 效果） |
| OBSTINANCE_MOVEMENT_REQUIRED_RADICALISM | 0.5 | # 一场运动要对州的顽固度产生贡献所需的最低激进程度/活跃程度 |
| MIN_INSTITUTION_INVESTMENT | 1 | # 活跃机构的最低投入等级（修正将被限制在此值） |
| MAX_INSTITUTION_INVESTMENT | 5 | # 活跃机构的最高投入等级（修正将被限制在此值） |
| DAILY_INSTITUTION_SIZE_CHANGE | 0.0028 | # 机构规模每日的增减百分比（0.0028 ≈ 1/365） |
| INITIAL_MOMENTUM_MIN | 0.5 | # 选举期开始时随机分配的最低势头值 |
| INITIAL_MOMENTUM_MAX | 1.5 | # 选举期开始时随机分配的最高势头值 |
| POPULARITY_MOMENTUM_FACTOR | 0.005 | # 政党因领袖人气而获得或失去的势头值 |
| ELECTION_INTERVAL_YEARS | 4 | # 两次选举之间通常间隔的年数 |
| CAMPAIGN_PERIOD_MONTHS | 6 | # 选举前的竞选期时长 |
| MIN_AFFILIATION_TO_STAY_IN_PARTY | 0 | # 利益集团与政党的归属感需达到此值才会愿意留在该党 |
| MIN_AFFILIATION_TO_JOIN_PARTY | 1 | # 利益集团与政党的归属感需达到此值才会愿意加入该党 |
| MAX_ELECTORAL_CONFIDENCE | 1.0 | # 选举信心永远不会高于此值 |
| INITIAL_ELECTORAL_CONFIDENCE | 1.0 | # 游戏开始或首次引入选举时的初始选举信心 |
| REFORM_GOVERNMENT_PERIOD | 6 | # 选举后可以免费改组政府的月数 |
| REFORM_GOVERNMENT_RADICALIZATION_RATE | 0.25 | # 一个利益集团被移出政府时，其支持者中被激进化的人数百分比 |
| RADICALISM_AGITATING_THRESHOLD | 0.25 |  |
| RADICALISM_PROTESTING_THRESHOLD | 0.50 |  |
| RADICALISM_MILITANT_THRESHOLD | 0.75 |  |
| SUPPORT_RELEVANT_THRESHOLD | 0.05 |  |
| SUPPORT_SIGNIFICANT_THRESHOLD | 0.25 |  |
| SUPPORT_DOMINANT_THRESHOLD | 0.5 |  |
| SUPPORT_UNIVERSAL_THRESHOLD | 0.75 |  |
| INCOHERENCE_FACTOR | 5 | # 将支持度数值乘以该系数以得出用于合法性计算的不协调得分 |
| LEGITIMACY_PENALTY_FOR_EACH_EXCESS_ENTITY | 20 | # 政府中每个超出 country_legitimacy_govt_size_add 所定限额的集团会导致多少合法性损失 |
| SHOW_CONFIRMATION_BELOW_LEGITIMACY | 25 |  |
| POLITICAL_LOBBY_BASELINE_DECAY_FACTOR_KEY | "appeasement_baseline_decay" | # 如果在数据库中更改此绥靖因子的名称，必须在此处同步更改，反之亦然 |
| # 如果新创建的政治游说集团的利益集团成员数低于 POLITICAL_LOBBY_DESIRED_MEMBERS，利益集团加入该游说集团的权重将乘以 1 +（达到 POLITICAL_LOBBY_DESIRED_MEMBERS 所需的成员数 * POLITICAL_LOBBY_OVER_DESIRED_MEMBERS_JOIN_FACTOR）# 如果新创建的政治游说集团的利益集团成员数高于 POLITICAL_LOBBY_DESIRED_MEMBERS，利益集团加入该游说集团的权重将除以 1 +（达到 POLITICAL_LOBBY_DESIRED_MEMBERS 所需的成员数 * POLITICAL_LOBBY_OVER_DESIRED_MEMBERS_JOIN_FACTOR）# 新创建的政治游说集团的利益集团成员数绝不应超过 POLITICAL_LOBBY_CREATION_MAX_MEMBERS # 这些系数*仅*在游说集团创建期间适用 |  |  |
| POLITICAL_LOBBY_CREATION_DESIRED_MEMBERS | 2 |  |
| POLITICAL_LOBBY_CREATION_DESIRED_MEMBERS_JOIN_FACTOR | 0.5 |  |
| POLITICAL_LOBBY_CREATION_MAX_MEMBERS | 3 |  |
| POLITICAL_LOBBY_MIN_NON_MARGINALIZED_MEMBERS | 1 | # 至少要有这么多个非边缘化利益集团愿意加入，政治游说团才会被创建 |
| POLITICAL_LOBBY_MINIMUM_JOIN_WEIGHT_THRESHOLD | 50 | # 加入权重达到此值时，利益集团在游说团成立时有机会加入 |
| POLITICAL_LOBBY_GUARANTEED_JOIN_WEIGHT_THRESHOLD | 100 | # 加入权重达到此值时，利益集团在游说团成立时必定加入。若低于此值但高于 POLITICAL_LOBBY_MINIMUM_JOIN_WEIGHT_THRESHOLD，则会根据其加入权重有随机几率加入 |
| # 一个利益集团不能同时属于超过此数量的同类政治游说团 # 如果某个利益集团想加入一个游说团但已达上限，当新游说团在利益集团吸引力上得分更高时，它可能会退出当前所在的某个游说团 |  |  |
| MAX_NUM_POLITICAL_LOBBIES_OF_SAME_CATEGORY_PER_IG | 1 |  |
| # 如果一个新建游说团的加入权重大于或等于某个利益集团现有同类游说团加入权重乘以此值，该利益集团将加入新游说团并退出旧游说团 # 这只在利益集团因 MAX_NUM_POLITICAL_LOBBIES_OF_SAME_TYPE_PER_IG 限制而无法加入更多游说团时适用 |  |  |
| POLITICAL_LOBBY_JOIN_WEIGHT_REPLACEMENT_THRESHOLD | 1.25 |  |
| POLITICAL_LOBBY_APPEASEMENT_APPROVAL_AVERAGED | no | # 若设为 yes，来自游说团安抚的认可度将在各游说团之间取平均值，而不是总和 |
| POLITICAL_LOBBY_MIN_APPEASEMENT | -10 | # 安抚值不能低于此值 |
| POLITICAL_LOBBY_MAX_APPEASEMENT | 10 | # 安抚值不能高于此值 |
| POLITICAL_LOBBY_STARTING_APPEASEMENT | 0 | # 游说团以此安抚值开始 |
| POLITICAL_LOBBY_BASELINE_APPEASEMENT | 0 | # 安抚值会随时间自然衰减至该值 |
| POLITICAL_LOBBY_APPEASEMENT_DECAY_TIME | 1025 | # 游说团的安抚值向基线值衰减 1 点需要这么多天 |
| POLITICAL_LOBBY_APPEASEMENT_APPROVAL_IMPACT | 1.0 | # 游说团每一点安抚值会转化为该游说团成员利益集团的这么多认可度 |
| MIN_DECREE_COST | 0.1 | # 无论你有多少 modifier 折扣，法令的成本都不能低于基础成本的这一比例 |

### 经济

| Define | 默认值 | 开发者注释 |
|---|---|---|
| MIN_CONSTRUCTION_EFFICIENCY | 0.05 | # 建造效率不能低于此值 |
| NUM_TIMES_TO_INITIALIZE_WEALTH | 10 | # 运行次数越多，人口财富相对于收入的初始设置就越精确 |
| NUM_TIMES_TO_UPDATE_TRADE_DURING_INITIALIZATION | 10 | # 初始化期间单独的贸易更新步骤额外运行的次数 |
| COUNTRY_GDP_MODIFIER_DIVISOR | 1000 | # 以此 GDP 除数来缩放 country_gdp 静态 modifier |
| COUNTRY_GDP_MODIFIER_MAX_MULTIPLIER | 200000 | # country_gdp modifier 的乘数不能高于此值 |
| COUNTRY_GDP_CONSTRUCTION_MODIFIER_DIVISOR | 2000000 | # 以此 GDP 除数来缩放 country_gdp_construction 静态 modifier |
| COUNTRY_GDP_CONSTRUCTION_MODIFIER_BASE_MULTIPLIER | 0.2 | # 无论 GDP 多少，始终加到 country_gdp_construction 乘数上的数值 |
| COUNTRY_GDP_CONSTRUCTION_MODIFIER_SCALED_MULTIPLIER | 0.8 | # country_gdp_construction modifier 的乘数以此为缩放基准 |
| COUNTRY_GDP_CONSTRUCTION_MODIFIER_MAX_MULTIPLIER | 1.0 | # country_gdp_construction modifier 的乘数不能高于此值 |
| ECONOMY_OF_SCALE_START_LEVEL | 1 | # 建筑从此等级开始获得规模经济加成。低于此值的等级不提供加成 [>=1] |
| USE_NATIONALIZED_ECONOMY_OF_SCALE_PENALTY | no | # 是否应对国有化等级的建筑应用 ECONOMY_OF_SCALE_NATIONALIZED_FRACTION_MULT 的规模经济修正 |
| ECONOMY_OF_SCALE_NATIONALIZED_FRACTION_MULT | 0.5 | # 非政府建筑的规模经济修正乘以（1 - 国有化等级比例 * 此值） |
| IN_DEFAULT_MINIMUM_PENALTY_SCALE | 0.1 | # “违约”状态下的吞吐量惩罚中，这一比例会立即生效 |
| IN_DEFAULT_DAYS_TO_FULL_PENALTY | 365 | # 需要违约多少天才能达到全额吞吐量惩罚 |
| DECLARE_BANKRUPTCY_PENALTY_DURATION_YEARS | 10 | # 宣告破产的惩罚需要多少年才能完全消退 |
| DECLARE_BANKRUPTCY_RADICALIZATION_BASE_FACTOR | 0.1 | # 宣告破产时，所有人口中这一百分比会变得激进 |
| DECLARE_BANKRUPTCY_RADICALIZATION_SHARES_FACTOR | 0.05 | # 宣告破产时，每个人口基于其在建筑中持有的股份，按这一百分比变得激进 |
| FIRED_POP_RADICALIZATION_FRACTION | 0.1 | # 当人口失去工作时（例如因建筑缩减规模），这一百分比的人口会变得激进 |
| # 当建筑被国有化时，人口会通过以下两种方式之一变得激进：# 1：在建筑中工作的人口基于被国有化的等级数量变得激进，其程度取决于该建筑中自持等级的比例 # 2：在全国任何地方持有所有权类建筑（即庄园宅邸/金融区）股份的人口，基于被国有化的私人持有等级数量及其建筑对被国有化建筑类型的投资分数变得激进 |  |  |
| NATIONALIZE_BUILDING_SELF_OWNED_RADICALIZATION_FACTOR | 0.25 | # 乘以自持等级的比例 |
| NATIONALIZE_BUILDING_PRIVATELY_OWNED_RADICALIZATION_FACTOR | 0.01 | # 乘以由另一建筑持有的等级数量（上限为 NATIONALIZE_BUILDING_OWNING_POP_TYPE_RADICALIZATION_MAX_MULTIPLIER） |
| NATIONALIZE_BUILDING_PRIVATELY_OWNED_RADICALIZATION_MAX_MULTIPLIER | 20 |  |
| NATIONALIZE_BUILDING_PRIVATELY_OWNED_RADICALIZATION_SCORE_DIVISOR | 1 | # 变得激进的所有权类人口数量乘以其建筑的投资值，再除以此值 |
| NATIONALIZE_BUILDING_OTHER_COUNTRY_OWNED_RELATIONS_IMPACT | -2 | # 国有化由他国政府拥有的建筑时，每国有化一个建筑等级产生这一数值的关系影响 |
| NATIONALIZE_BUILDING_OTHER_COUNTRY_POP_OWNED_RELATIONS_IMPACT | -1 | # 国有化由他国人口拥有的建筑时，每国有化一个建筑等级产生这一数值的关系影响 |
| NATIONALIZE_BUILDING_NO_COMPENSATION_IMPACT_MULT | 3.0 | # 若国有化时未给予货币补偿，激进派数量与关系损失乘以此系数 |
| AUTO_DOWNSIZE_BUILDING_MIN_EMPTY_PRIVATE_LEVELS | 1.0 | 一个（非贸易中心的）建筑必须至少缺失这么多私人持有的就业等级，才会开始考虑自动缩减规模（此条件与下方条件须同时满足） |
| AUTO_DOWNSIZE_BUILDING_MIN_EMPTY_FRACTION | 0.1 | # 一个（非贸易中心的）建筑必须至少缺失这么多就业等级（相对数值），才会开始考虑自动缩减规模（此条件与上方条件须同时满足） |
| AUTO_DOWNSIZE_BUILDING_MIN_UNUSED_TRADE_CAPACITY_FRACTION | 0.1 | # 一个贸易中心必须至少有这么多未使用的贸易容量（占整体的比例）才会考虑自动缩减规模 |
| AUTO_DOWNSIZE_BUILDING_MIN_UNUSED_TRADE_CAPACITY | 20 | # 一个贸易中心必须至少有这么多未使用的贸易容量（绝对数值）才会考虑自动缩减规模 |
| AUTO_DOWNSIZE_BUILDING_MONTHS_TO_WAIT | 6 | # 建筑决定开始自动缩减规模后，等待这么多个月才真正开始缩减，以防条件发生变化 |
| # 污染影响 = (GeneratedPollution (StateRegion) / (DIVISOR_BASE + DIVISOR_ARABLE_LAND_MULT * SQRT(ArableLand (State Region)))/POLLUTION_MAX |  |  |
| POLLUTION_TARGET_DIVISOR_BASE | 50 | # 用于计算州区域污染目标水平时，总污染产生量除以此基础值 |
| POLLUTION_TARGET_DIVISOR_ARABLE_LAND_MULT | 1.5 | # 每点可耕种土地加到污染除数上的数值 |
| POLLUTION_CHANGE_SPEED | 0.255 | # 州区域的污染每天朝目标值变化此数值 |
| POLLUTION_MAX | 255 |  |
| POLLUTION_SPREAD_TO_NEIGHBOR | 0.25 | # 相邻州区域至少拥有其邻近区域污染水平的这个比例 |
| GOODS_LEADERBOARD_SIZE | 10 | # 每个商品排行榜上有多少个席位 |
| MIN_SPOT_PRESTIGE_AWARD | 3 | # 商品排行榜上有多少个席位会被授予威望 |
| GOODS_LEADERBOARD_GLOBAL_GDP_SCALING | 10000000000 | # 当全球年度 GDP 达到此数值时，顶级商品生产者的威望加成将应用最大缩放 |
| GOODS_LEADERBOARD_PRESTIGE_BASE | 0.25 | # 作为顶级商品生产者所获得的威望的这一乘数始终会被授予 |
| GOODS_LEADERBOARD_PRESTIGE_SCALED | 2.75 | # 作为顶级商品生产者所获得的威望的这一乘数会根据全球 GDP 进行缩放 |
| MIN_GOODS_PRICE | 1 | # 商品的基础价格不会低于此值 |
| PRICE_RANGE | 0.75 | # 商品的最低价格为基础价格 * (1 - PRICE_RANGE)，最高价格为基础价格 * (1 + PRICE_RANGE)，PRICE_RANGE 被锁定在 [0-1] 之间 |
| BUY_SELL_DIFF_AT_MAX_FACTOR | 2 | # 在最低/最高定价时买入/消费与卖出/生产之间的差异，例如设为 4 时，若购买订单是销售订单的 4 倍，价格将达到最高 |
| GOODS_SHORTAGE_PENALTY_THRESHOLD | 0.5 | # 若供给 / 需求低于此值，开始施加产出惩罚，默认情况下此值应为 ( 1 / BUY_SELL_DIFF_AT_MAX_FACTOR ) |
| GOODS_SHORTAGE_PENALTY_INCREASE_SPEED | 0.01 | # 商品短缺惩罚每天按目标值的这个比例增加 |
| GOODS_SHORTAGE_PENALTY_DECREASE_SPEED | 0.01 | # 商品短缺惩罚每天按 GOODS_SHORTAGE_PENALTY_MAX 的这个比例减少 |
| GOODS_SHORTAGE_PENALTY_MIN | 0.05 | # 只要有任何短缺，商品短缺惩罚就不会低于此值 |
| GOODS_SHORTAGE_PENALTY_MAX | 0.5 | # 只要所有投入商品仍有一定数量存在，商品短缺惩罚就不会高于此值 |
| GOODS_SHORTAGE_PENALTY_MISSING_INPUTS | 0.75 | # 当某种投入商品在本地供给中完全缺失时，施加此惩罚 |
| GOODS_SHORTAGE_PENALTY_MILITARY_BUILDING_SPEED_MULT | 5.0 | # 军事建筑的短缺惩罚以这个倍率的速度增减 |
| POP_NEED_BASIC_FOOD | "popneed_basic_food" |  |
| MINIMUM_GOODS_TRADED_QUANTITY | 0.5 | # 商品的贸易数量永远不会低于此值 |
| WORLD_MARKET_GOODS_DEMAND_BUFFER | 10 | # 以下数值的存在是为了确保世界市场进口中注入“新”商品，方法是将该商品的贸易数量乘以此数值加到世界市场需求中 # 这是为了让第一个出口某种商品的国家始终有利可图 |
| WORLD_MARKET_HUB_SCORE_STICKYNESS | 3.0 | # 若某个州是世界市场枢纽，另一个州的枢纽分数必须超过其这个倍数才能取代它成为新枢纽 |
| WORLD_MARKET_HUB_SCORE_PORT_FACTOR | 10 | # 每拥有一定等级的港口，对枢纽分数施加此数值 |
| WORLD_MARKET_HUB_SCORE_GDP_FACTOR_DIVISOR | 100000 | # 该州每达到这个数值的 GDP 便增加 1 点枢纽分数 |
| WORLD_MARKET_HUB_SCORE_TRADE_CAPACITY_FACTOR | 0.1 | # 该州每点贸易能力对枢纽分数施加此数值 |
| WORLD_MARKET_HUB_SCORE_MARKET_CAPITAL_FACTOR | 100 | # 为市场首府添加此数量的枢纽分数 |
| WORLD_MARKET_LOCATION | "x9137A4" | # 该省份用于判定一个州是否接入世界市场。该省份本身不会直接展示给玩家。 |
| NON_TRADE_CENTER_STATE_TRADE_POTENTIAL_UPDATE_FREQUENCY | 30 | # 没有贸易中心的州更新贸易潜力的间隔天数 # 此值越低，AI 在评估新建贸易中心时掌握的数据就越新，但会影响性能 |
| TRADE_CENTER_ADVANTAGE_PRICE_MULTIPLIER | 0.25 | # 相对优势中有这么多比例会转化为价格乘数 # 应用于相对优势与 1 之间的差值 # 例如，如果 TRADE_CENTER_ADVANTAGE_PRICE_MULTIPLIER 为 0.5 且相对优势为 2，则价格乘数为 1 + ( ( 2 - 1 ) * 0.5 ) = 1.5 |
| TRADE_CENTER_ADVANTAGE_BASE | 100 | # 贸易中心拥有的基础优势值 |
| TRADE_CENTER_ADVANTAGE_MARKET_AREA_PRODUCTION_FACTOR | 200 | # 贸易中心就市场区域生产获得此数量的出口优势（相对于全球生产/消费进行缩放，并乘以市场接入） |
| TRADE_ADVANTAGE_COMPANY_CHARTER_FACTOR | 50 | # 公司特许状就市场生产获得此数量的出口优势 |
| TRADE_CENTER_ADVANTAGE_MARKET_PRESTIGE_GOOD_FACTOR | 100 | # 贸易中心根据其市场中威望商品占商品生产的比例获得此数量的出口优势（威望商品对进口优势没有影响） |
| TRADE_CENTER_ADVANTAGE_TRADE_AGREEMENT_FACTOR | 100 | # 贸易中心获得此数量的出口/进口优势，按相反方向贸易中来自贸易协定所覆盖市场的百分比进行缩放 |
| TRADE_CENTER_ADVANTAGE_TREATY_PORT_FACTOR | 200 | # 贸易中心获得此数量的出口/进口优势，按相反方向贸易中来自其母国拥有的条约港的百分比进行缩放 |
| # 以下惩罚同一时间只会应用其中之一，优先顺序为：禁运、战争 |  |  |
| TRADE_CENTER_ADVANTAGE_EMBARGO_FACTOR | -100 | # 贸易中心失去此数量的出口/进口优势，按相反方向贸易中来自市场控制者对拥有者实施禁运的市场的百分比进行缩放 |
| TRADE_CENTER_ADVANTAGE_AT_WAR_FACTOR | -75 | # 贸易中心失去此数量的出口/进口优势，按相反方向贸易中来自市场控制者与拥有者处于战争状态的市场的百分比进行缩放 |
| # 贸易中心在向其他特定贸易中心进口/出口时的偏好权重 |  |  |
| TRADE_CENTER_PREFERENCE_BASE | 1 | # 对其他每个贸易中心的基础偏好权重 |
| TRADE_CENTER_PREFERENCE_SAME_POWER_BLOC_MULTIPLIER | 0.5 | # 若两个贸易中心属于同一强权集团，则加到权重乘数上的值 |
| TRADE_CENTER_PREFERENCE_TRADE_AGREEMENT_MULTIPLIER | 4.0 | # 两国之间每有一项贸易协定，加到权重乘数上的值 |
| TRADE_CENTER_PREFERENCE_EMBARGO_DIVISOR | 2.0 | # 两国之间每有一项禁运，加到权重除数上的值 |
| TRADE_CENTER_PREFERENCE_NO_INTEREST_DIVISOR | 0.25 | # 每有一方未在对方市场宣示利益，加到权重除数上的值 |
| TRADE_CENTER_PREFERENCE_DISTANCE_DIVISOR | 0.25 | # 两个贸易中心枢纽之间距离每超出预期距离一倍，加到权重除数上的值 |
| TRADE_CENTER_PREFERENCE_TOLL_DIVISOR | 0.05 | # 权重除以 1 + ( 海峡通行税整百分比 * 此值 )，针对两个贸易中心枢纽之间路线上的海峡通行税 |
| SEA_DISTANCE_EXPECTED_TRAVEL_DISTANCE | 1000 | # 预期海上航行距离——低于此值的距离不应用任何缩放，高于此值的距离线性缩放 |
| MAX_TRADE_ROUTE_ALTERNATIVES | 3 | # 在世界市场中心之间计算的替代海路的最大数量 |
| MARKET_SHARE_FROM_GDP | 1.0 | # 州内每 1 英镑 GDP 可获得此数值的市场份额点数 |
| MARKET_SHARE_MARKET_CONTROLLER_FACTOR | 1.33 | # 市场控制者的市场点数按此倍数加权计算 |
| MARKET_SHARE_MARKET_ACCESS_BASE | 0.5 | # 无论市场接入如何，始终可获得的市场点数比例 |
| MARKET_SHARE_MARKET_ACCESS_SCALED | 0.5 | # 依据市场接入可获得的市场点数比例 |
| COUNTRY_MIN_CREDIT_BASE | 100000 | # 加到建筑总现金储备上以确定信贷上限（基础值） |
| COUNTRY_MIN_CREDIT_SCALED | 0.5 | # 加到建筑总现金储备上以确定信贷上限（乘以 GDP） |
| CREDIT_RATIO_MAX_OVERRUN | 0.01 | # 国家违约时，债务“窟窿”可超出其信贷上限的百分比 |
| GOLD_RESERVE_RATIO_AT_START | 0.25 | # 除非国家历史的 'treasury' 参数被设为非零值，否则国家开局时黄金储备按此比例以黄金形式持有 |
| BUILDING_INITIAL_WAGE_WEEKS | 2 | # 建筑在存在的前此数量周内不会调整其工资 |
| MAX_WAGE_STEP_CHANGE | 0.1 | # 工资率每周最多变动此数值 |
| SUBSIDIES_MIN_GAIN | 0 | # 若建筑受补贴，其获得的补贴将始终至少保证每周现金储备增长此数值 |
| DEFAULT_MIN_HIRING_RATE | 0.01 | # 建筑中每种职业每周最低雇佣限制，按满就业的比例计（默认值） |
| DEFAULT_MAX_HIRING_RATE | 0.1 | # 建筑中每种职业每周最高雇佣限制，按满就业的比例计（默认值） |
| HIRING_RANGE_WEEKLY_CHANGE | 0.01 | # 建筑的雇佣范围每周按此数值减小或增大，取决于其是否无法以当前速率完成雇佣 |
| EMPLOYMENT_PROPORTIONALITY_LIMIT | 0.1 | # 建筑中任意两种职业之间的满就业比例之差不能超过此限制 |
| MINIMUM_EMPLOYEES | 10 | # 若建筑雇员少于此数量，它将始终尝试雇佣 |
| BUILDING_WAGES_DIVIDEND_INCOME_FACTOR | 0.5 | # 拥有分红收入的人口，其财富乘以 1 -（分红占其收入的比例 * 此数值），以确保建筑不会仅因所有雇员都获得分红就开始压低工资 |
| BUILDING_WAGES_WELFARE_INCOME_FACTOR | 0.8 | # 拥有福利收入的人口，其财富乘以 1 -（福利占其收入的比例 * 此数值），以确保建筑不会仅因所有雇员都获得福利就开始压低工资 |
| BUILDING_WAGES_OWNERSHIP_BUILDING_FACTOR | 0.75 | # 持有其他建筑的建筑将其目标工资乘以此数值，以确保盈利能力 |
| BUILDING_WAGES_MIN_RELEVANT_POP_SIZE | 50 | # 在检查盈利建筑是否应因工人变得激进而提高工资时，劳动力少于此数量的人口将被忽略 |
| BUILDING_WAGES_MIN_EMPLOYEES_FOR_RELEVANT_POP_SIZE_CHECK | 200 | # 要启用 BUILDING_WAGES_MIN_RELEVANT_POP_SIZE 检查，建筑必须至少拥有此数量的雇员，以避免小型建筑压低工资 |
| BUILDING_RAISE_WAGES_TARGET_WEALTH_MULT | 0.9 | # 若建筑中任何重要人口的数值低于或等于目标财富与预期生活水平之比 * 此数值，建筑将考虑提高工资 |
| BUILDING_LOWER_WAGES_TARGET_WEALTH_MULT | 1.2 | # 若建筑中所有重要人口的数值均高于或等于目标财富与预期生活水平之比 * 此数值，建筑将考虑降低工资 |
| BUILDING_WAGES_AVERAGE_PRODUCTIVITY_THRESHOLD | 0.5 | # 与平均生产率的比值达到此数值时，BUILDING_WAGES_AVERAGE_PRODUCTIVITY_FACTOR 开始生效（由于持股建筑与贸易中心，平均值往往偏高，因此此数值应相当低） |
| BUILDING_WAGES_AVERAGE_PRODUCTIVITY_FACTOR | 0.5 | # 相比该建筑类型平均值生产率更高的建筑，在盈利尚可的情况下，其工资会慷慨到何种程度 |
| BUILDING_WAGES_AVERAGE_PRODUCTIVITY_FACTOR_MAX | 2.5 | # 相比平均生产率超过此比率后，BUILDING_WAGES_AVERAGE_PRODUCTIVITY_FACTOR 的效果将被封顶 |
| BUILDING_PREFER_LAYOFFS_TARGET_WEALTH_MULT | 0.66 | # 如果建筑中任何重要人口的 目标财富与预期生活水平之比 低于或等于此值，建筑将倾向于解雇人口 |
| BUILDING_FOREIGN_OWNERSHIP_WAGE_FACTOR | -0.25 | # 外国所有者拥有的建筑，其工资目标将按此数额调整（乘以外资持股比例），因为所有者不太在意低工资产生的激进派 |
| BUILDING_DEFAULT_MIN_EARNINGS_TO_HIRE_EMPLOYEES | 3 | # 非补贴建筑在雇用会导致其 年人均收入 低于此阈值时将不再雇用（默认值，可针对建筑组覆盖） |
| BUILDING_PROFIT_TARGET_TO_RAISE_WAGES | 0.25 | # 达到此利润率才会考虑将工资提高到预期最低水平，并有 BUILDING_WEEKS_BETWEEN_PAY_RAISES 周的冷却时间 |
| BUILDING_PROFIT_TARGET_TO_LOWER_WAGES | 0.15 | # 如果利润率低于或等于此值，建筑应降低工资，并有 BUILDING_WEEKS_BETWEEN_PAY_CHANGES 周的冷却时间 |
| BUILDING_PROFIT_TARGET_TO_WITHDRAW_CASH | 0.15 | # 如果利润率低于或等于此值，建筑应从现金储备中取钱以弥补差额 |
| BUILDING_PROFIT_TARGET_TO_HIRE_EMPLOYEES | 0.25 | # 如果利润率高于或等于此值，建筑应尝试雇用新工人 |
| OWNERSHIP_BUILDING_PROFIT_TARGET_TO_RAISE_WAGES | 0.5 | # 覆盖持有其他建筑的建筑的 BUILDING_PROFIT_TARGET_TO_RAISE_WAGES |
| OWNERSHIP_BUILDING_PROFIT_TARGET_TO_LOWER_WAGES | 0.3 | # 覆盖持有其他建筑的建筑的 BUILDING_PROFIT_TARGET_TO_LOWER_WAGES |
| OWNERSHIP_BUILDING_PROFIT_TARGET_TO_WITHDRAW_CASH | 0.3 | # 覆盖持有其他建筑的建筑的 BUILDING_PROFIT_TARGET_TO_WITHDRAW_CASH |
| OWNERSHIP_BUILDING_PROFIT_TARGET_TO_HIRE_EMPLOYEES | 0.5 | # 覆盖持有其他建筑的建筑的 BUILDING_PROFIT_TARGET_TO_HIRE_EMPLOYEES |
| SUBSISTENCE_BUILDING_PROFIT_TARGET_TO_RAISE_WAGES | 0.7 | # 覆盖自给建筑的 BUILDING_PROFIT_TARGET_TO_RAISE_WAGES |
| SUBSISTENCE_BUILDING_PROFIT_TARGET_TO_LOWER_WAGES | 0.5 | # 覆盖自给建筑的 BUILDING_PROFIT_TARGET_TO_LOWER_WAGES |
| SUBSISTENCE_BUILDING_PROFIT_TARGET_TO_WITHDRAW_CASH | 0.5 | # 覆盖自给建筑的 BUILDING_PROFIT_TARGET_TO_WITHDRAW_CASH |
| BUILDING_MAX_EMPLOYMENT_FRACTION_TO_RAISE_WAGES | 0.5 | # 如果建筑的就业比例高于此值，则不会仅为从其他建筑挖走员工而提高工资 |
| BUILDING_WEEKS_BETWEEN_PAY_CHANGES | 0 | # 工资变动之间的冷却时间，以防建筑对环境中的临时性变化作出过度补偿。如果建筑处于亏损状态，则改用 BUILDING_WEEKS_BETWEEN_PAY_CHANGES_WHEN_UNPROFITABLE。 |
| BUILDING_WEEKS_BETWEEN_PAY_CHANGES_WHEN_UNPROFITABLE | 0 | # 工资变动之间的冷却时间，以防建筑对环境中的临时性变化作出过度补偿。仅在亏损时使用。 |
| MIN_RAISE_TO_HIRE | 0.10 | # 员工跳槽所需的最低工资涨幅（1.0 = +100% = 翻倍） |
| MIN_JOB_ATTRACTIVENESS | 0.10 | # 叠加修正词不能使职位吸引力低于此值 |
| BASE_RESOURCE_DISCOVER_CHANCE | 0.02 | # 每天（1.0 = 1%） |
| EMPLOYMENT_RESOURCE_DEPLETE_CHANCE | 0.005 | # 乘以建筑满员雇佣的等级数 |
| RESOURCE_DISCOVER_MIN_FRACTION | 0.2 | # 每次成功判定时可发现资源的最小比例 |
| RESOURCE_DISCOVER_MAX_FRACTION | 0.5 | # 每次成功判定时可发现资源的最大比例 |
| FULLY_DISCOVERED_RESOURCE_DEPLETE_CHANCE_MULT | 1.0 | # 当资源全部被发现时，资源枯竭的概率乘以此值 |
| RESOURCE_DEPLETE_MIN_AMOUNT | 2 | # 每次成功判定时枯竭资源的最小数量 |
| RESOURCE_DEPLETE_MAX_AMOUNT | 5 | # 每次成功判定时枯竭资源的最大数量 |
| QUALITY_OF_LIFE_MIN | 1 |  |
| QUALITY_OF_LIFE_MAX | 100 |  |
| SUBSISTENCE_OUTPUT_AVERAGE_WAGE_RATE_FACTOR | 150 | # 在设定正常工资时，每 1.0 维持性产出计为此数值的工资率 |
| PEASANT_STARTING_WAGE_RATE_FACTOR | 1.0 | # 为计算初始正常工资，将农民视为拥有此人口类型工资乘数 |
| STARTING_WAGE_RATE_MULTIPLIER | 1.0 | # 初始工资率乘以此值（便于平衡调整） |
| STARTING_WAGE_RATE_SUBSISTENCE_MULTIPLIER | 0.5 | # 对维持性建筑，STARTING_WAGE_RATE_MULTIPLIER 进一步乘以此值 |
| NORMAL_WAGE_RATE_FALLBACK | 500.0 | # 如果无法计算正常工资率（例如所有已合并人口均在政府建筑中工作），则设为此值（每周每 POP_SIZE_PACKAGE 名雇员的英镑数） |
| MINIMUM_WAGE_RATE | 10.0 | # 无论如何，工资率永远不会低于此值（每周每 POP_SIZE_PACKAGE 名雇员的英镑数） |
| MAXIMUM_WAGE_RATE | 100000.0 | # 建筑工资率可提升到的绝对上限。 |
| CREDIT_RATIO_HEALTH_THRESHOLD | 0.5 | # 如果本金低于总信贷的此比例，则经济被视为健康 |
| GOLD_RESERVE_MIN | 1000 | # 如果计算出的黄金储备低于此值，则改设为此值 |
| GOLD_RESERVE_LIMIT_FACTOR | 0.2 | # 应作为黄金储备提供的年度 GDP 的基础比例 |
| GOLD_RESERVE_RETURNS_FACTOR | 1 | # 达到上限后，收益递减导致黄金储备下降的速度（数值越高惩罚越大） |
| RETOOLING_WEEKS | 0 | # 建筑切换生产方式后恢复满负荷生产所需的时间 |
| BUILDING_TIMED_MODIFIER_WEEKS | 52 | # 切换生产方式后施加的限时 modifier 的持续时间 |
| BUILDING_PAUSE_HIRES_CASH_RESERVES_THRESHOLD | 0.75 | # 如果现金储备高于此值，且就业比例低于 BUILDING_MAX_EMPLOYMENT_FRACTION_TO_CONSIDER_CASH_RESERVES，则即使利润较低也允许雇用 |
| BUILDING_MIN_EMPLOYMENT_FRACTION_TO_PAUSE_HIRES | 0.1 | # 如果建筑至少拥有此就业比例，则可以暂停雇用 |
| BUILDING_MAX_EMPLOYMENT_FRACTION_TO_CONSIDER_CASH_RESERVES | 0.5 | # 如果建筑至少拥有此就业比例，则忽略雇用的现金储备覆盖规则 |
| BUILDING_MAX_PROFIT_TO_PAUSE_HIRES | 0.2 | # 如果建筑的利润低于收入的此比例，则可以暂停雇用 |
| PRICE_REPORT_MAX_ENTRIES | 10 |  |
| NUM_COIN_ICONS | 13 |  |
| COIN_ICON_PRICE_COMPARISON_STEP | 0.12 |  |
| NUM_PROFITABILITY_ICONS | 13 |  |
| PROFITABILITY_ICON_COMPARISON_STEP | 0.15 |  |
| EARNINGS_RATIO_HIGH_THRESHOLD | 1.5 | # 生产率超过平均值此倍数的建筑将被视为高生产率建筑 |
| EARNINGS_RATIO_LOW_THRESHOLD | 0.66 | # 生产率低于平均值此倍数的建筑将被视为低生产率建筑 |
| EARNINGS_ABSOLUTE_HIGH_THRESHOLD | 30 | # 生产率超过此数值的建筑将始终被视为高生产率建筑 |
| EARNINGS_ABSOLUTE_LOW_THRESHOLD | 3 | # 生产率低于此数值的建筑将永远被视为低生产率建筑 |
| SLAVE_BASKET_DEFAULT | 8 | # 建筑为其奴隶购买消费品等级的默认值 |
| SLAVE_BASKET_MIN | 1 | # 建筑为其奴隶购买消费品等级的最小值（取此值与 SLAVE_BASKET_SCALED_MIN 中的较高者） |
| SLAVE_BASKET_MAX | 12 | # 建筑为其奴隶购买消费品等级的最大值（取此值与 SLAVE_BASKET_SCALED_MAX 中的较低者） |
| SLAVE_BASKET_SCALED_MIN | 0.5 | # 乘以建筑中最低的非奴隶财富值 |
| SLAVE_BASKET_SCALED_MAX | 1 | # 乘以建筑中最低的非奴隶财富值 |
| SLAVE_BASKET_SUBSISTENCE_GOODS_MULT | 0.05 | # 自给建筑中奴隶消耗的商品乘以此系数 |
| COLONIAL_SLAVERY_ENSLAVEMENT_RATE | 0.005 | # 在殖民奴隶制下，每周最多可有此比例的州人口因债务被奴役 |
| COLONIAL_SLAVERY_ENSLAVEMENT_RATE_PER_POP | 0.15 | # 单个人口每周被奴役的比例不得超过此值 |
| COLONIAL_SLAVERY_ENSLAVEMENT_RATE_DROP_OFF_PER_WEALTH | 0.01 | # 每点财富使人口的最大奴役率降低此值 |
| COLONIAL_SLAVERY_MAX_STATE_SLAVE_FRACTION | 0.25 | # 若州人口的奴隶比例超过此百分比，殖民奴隶制下不再奴役更多人口 |
| COLONIAL_SLAVERY_ACCEPTANCE_THRESHOLD | 60 | # 在其所在州接纳度达到或超过此值的人口在殖民奴隶制下不会被奴役 |
| DEBT_SLAVERY_ENSLAVEMENT_RATE | 0.005 | # 在债务奴隶制下，每周最多可有此比例的州人口因债务被奴役 |
| DEBT_SLAVERY_ENSLAVEMENT_RATE_PER_POP | 0.1 | # 单个人口每周被奴役的比例不得超过此值 |
| DEBT_SLAVERY_ENSLAVEMENT_RATE_DROP_OFF_PER_WEALTH | 0.01 | # 每点财富使人口的最大奴役率降低此值 |
| DEBT_SLAVERY_MAX_STATE_SLAVE_FRACTION | 0.15 | # 若州人口的奴隶比例超过此百分比，债务奴隶制下不再奴役更多人口 |
| SLAVE_TRADE_MIN_VACANCIES_NEEDED_TO_IMPORT | 500 | # 建筑中需至少有此数量的（非自给的）可由奴隶填补的空缺职位，奴隶进口才会发生 |
| SLAVE_TRADE_MIN_POPULATION_TO_EXPORT | 100000 | # 州的人口需至少达到此数量，才能被选为或继续作为奴隶进口来源地 |
| SLAVE_TRADE_FULL_EXPORT_POPULATION_THRESHOLD | 250000 | # 州人口低于此数值时，出口的奴隶数量会乘以一个相对 SLAVE_TRADE_MIN_POPULATION_TO_EXPORT 缩放的系数（在两数中间点时系数为 0.5 倍，依此类推） |
| SLAVE_TRADE_POPULATION_FRACTION_WEIGHT | 100 | # 奴隶人口比例在奴隶进口标记选择中的权重 |
| SLAVE_TRADE_POPULATION_TOTAL_WEIGHT | 0.0002 | # 总人口在奴隶进口标记选择中的权重 |
| SLAVE_TRADE_TURMOIL_WEIGHT | 25 | # 奴隶动荡在奴隶进口标记选择中的权重 |
| SLAVE_TRADE_DISTANCE_WEIGHT | 1 | # 距离在奴隶进口标记选择中的反向权重（惩罚） |
| SLAVE_TRADE_OTHER_STATES_WEIGHT | 2 | # 拥有其他奴隶进口标记在奴隶进口标记选择中的反向权重（惩罚） |
| SLAVE_TRADE_EXISTING_STATE_CULTURE_WEIGHT_MULT | 10 | # 若从本国文化已存在于本州的其他州进口，该州的总分乘以此系数 |
| SLAVE_TRADE_NUMBER_EVALUATED_STATES | 10 | # 从权重最高的此数量个潜在目标中随机选择奴隶进口标记 |
| SLAVE_TRADE_BASE_SLAVES_PER_WEEK | 100 | # 每个标记每周交易的奴隶基础数量 |
| SLAVE_TRADE_ARABLE_LAND_EFFECT | 1 | # 进口州每单位可耕地使每周交易的奴隶数增加此值 |
| SLAVE_TRADE_ARABLE_LAND_EFFECT_MAX | 200 | # 可耕地可使每周交易奴隶数增加的最大值 |
| SLAVE_TRADE_RANDOM_MIN | 0.5 | # 每周交易的奴隶数会乘以一个随机数，此为该随机数的最小值 |
| SLAVE_TRADE_RANDOM_MAX | 1.5 | # 每周交易的奴隶数会乘以一个随机数，此为该随机数的最大值 |
| SLAVE_TRADE_MIN_MARKET_ACCESS | 0.1 | # 奴隶贸易的最低市场接入乘数，即即使在市场接入为 0 的市场，也会交易基础数量的这一比例 |
| BUILDING_FAILED_HIRE_COOLDOWN_WEEKS_WITHOUT_WAGE_RAISE | 4 | # 如果建筑雇用失败，需等待这么多周才会再次尝试，*除非*其在此期间提高了工资或调整了雇用率 |
| BUILDING_LAYOFFS_DECREASE_BY | 0.05 | # 裁员使就业减少的比率（例如 0.15 表示如果当前就业率为 57%，则降至 48.45%） |
| BUILDING_LAYOFF_HIRING_COOLDOWN_WEEKS | 4 | # 如果建筑进行裁员，至少这么多周内不再雇用新工人 |
| BUILDING_MINIMUM_HIRING_ADJUSTMENT_FRACTION | 0.001 | # 如果一次雇用或解雇转移的员工数少于所需员工的这一比例，则不执行 |
| BUILDING_CASH_RESERVES_HIGH_ROI | 0.25 | # 投资回报率（ROI）达到或高于此值被视为“高”。此处 ROI 指建筑收入相对支出的超出幅度。必须 >= BUILDING_CASH_RESERVES_MED_ROI。 |
| BUILDING_CASH_RESERVES_MED_ROI | 0.15 | # 投资回报率（ROI）恰好等于此值被视为“中”。此处 ROI 指建筑收入相对支出的超出幅度。必须 >= BUILDING_CASH_RESERVES_LOW_ROI。 |
| BUILDING_CASH_RESERVES_LOW_ROI | 0.05 | # 投资回报率（ROI）达到或低于此值被视为“低”。此处 ROI 指建筑收入相对支出的超出幅度。必须 > 0。 |
| BUILDING_CASH_RESERVES_FILL_TIME_HIGH_ROI | 26 | # ROI 为高时填满建筑现金储备的基础周数。若 ROI 介于中与高之间，最终周数按线性插值计算。必须 > 0。 |
| BUILDING_CASH_RESERVES_FILL_TIME_MED_ROI | 52 | # ROI 为中时填满建筑现金储备的基础周数。必须 > 0。 |
| BUILDING_CASH_RESERVES_FILL_TIME_LOW_ROI | 78 | # ROI 为低时填满建筑现金储备的基础周数。若 ROI 介于低与中之间，最终周数按线性插值计算。必须 > 0。 |
| BUILDING_CASH_RESERVES_MIN_DEPOSIT_PERCENT | 0.25 | # 建筑所有者尝试存入建筑现金储备的每周利润的最低百分比。必须 >= 0。 |
| BUILDING_CASH_RESERVES_MAX_DEPOSIT_PERCENT | 0.50 | # 建筑所有者尝试存入建筑现金储备的每周利润的最大百分比。必须 >= BUILDING_CASH_RESERVES_MIN_DEPOSIT_PERCENT |
| OWNERSHIP_BUILDING_CASH_RESERVES_MIN_DEPOSIT_PERCENT | 0.125 | # 对于拥有其他建筑的建筑，以此值替代 BUILDING_CASH_RESERVES_MIN_DEPOSIT_PERCENT |
| OWNERSHIP_BUILDING_CASH_RESERVES_MAX_DEPOSIT_PERCENT | 0.25 | # 对于拥有其他建筑的建筑，以此值替代 BUILDING_CASH_RESERVES_MAX_DEPOSIT_PERCENT |
| BUILDING_HIGH_CASH_RESERVES_THRESHOLD | 0.5 | # 如果现金储备超过最大值的这一比例，即使亏损，建筑也不会尝试削减开支 |
| EMPLOYMENT_DIVIDEND_ESTIMATE_MULT | 2.0 | # 在决定就业时高估分红，因为分红波动很大，我们确实不想把某人调到一份没有分红的工作上，结果反而更糟 |
| GOODS_DEFAULT_TRADE_QUANTITY | 10 | # 若商品类型中未另行指定，贸易中心交易的基础数量 |
| MIN_POPS_PER_PROFESSION | 3 | # 一座建筑在某个职业中至少可以雇佣这么多人口，即使可用人口少于该数量 |
| POPS_PER_PROFESSION_LOG_BASE | 10 | # 某职业的人口数量按此底数对雇员数取对数计算 |
| ESTABLISH_COLONY_PROVIDE_PORT | yes | # 建立殖民地时是否应为沿海殖民地修建港口，以便立即将其接入市场。 |
| ESTABLISH_COLONY_PORT_COST | 100000 | # 建立会修建港口的沿海殖民地所需的资金 |
| ESTABLISH_COLONY_PORT_LEVEL | 1 | # 建立沿海殖民地时获得的港口等级 |
| SHIPPING_LANE_MERCHANT_MARINE_COST_SCALING | 0.15 | # 超过预期距离后，每增加一倍预期距离为航运线路成本乘数增加的数值 |
| GOODS_DEFAULT_MERCHANT_MARINE_COST_MULTIPLIER | 1 | # 运输一单位商品的商船队成本（可在 defines 中覆盖） |
| OVERSEAS_INFRASTRUCTURE_MERCHANT_MARINE_COST_MULTIPLIER | 0.2 | # 海外州每点基础设施使用量对应港口连接航运线路的商船队成本 |
| MERCHANT_MARINE_GOODS_KEY | "merchant_marine" | # 用于商船队需求的商品键值 |
| SUPPLY_NETWORK_SHORTAGE_THRESHOLD | 0.5 | # 若商船队卖出/买入比率低于此值，开始施加补给网络强度惩罚 |
| SUPPLY_NETWORK_SHORTAGE_INCREASE_SPEED | 0.1 | # 补给网络短缺惩罚每周按目标值的此比例增加 |
| SUPPLY_NETWORK_SHORTAGE_DECREASE_SPEED | 0.1 | # 补给网络短缺惩罚每周按最大值的此比例减少 |
| SUPPLY_NETWORK_SHORTAGE_PENALTY_MIN | 0.05 | # 存在任何短缺时的最小补给网络短缺惩罚 |
| SUPPLY_NETWORK_SHORTAGE_PENALTY_MAX | 0.5 | # 最大补给网络短缺惩罚 |
| DEFAULT_EXPORT_TARIFFS | low_tariffs | # 历史设置中未指定时应用的默认出口关税等级 |
| DEFAULT_IMPORT_TARIFFS | low_tariffs | # 历史设置中未指定时应用的默认进口关税等级 |
| TARIFF_LEVEL_COOLDOWN_GRACE_PERIOD_DAYS | 7 | # 更改关税等级后，需经过这么多天冷却才会生效（给你反悔的机会） |
| TARIFF_LEVEL_COOLDOWN_MONTHS | 3 | # 更改关税等级后，必须等待这么久才能再次更改 |
| TARIFF_LEVEL_EFFECT_LOW | 0.25 | # 低等级下关税税率的应用比例 |
| TARIFF_LEVEL_EFFECT_HIGH | 0.5 | # 高等级下关税税率的应用比例 |
| TARIFF_LEVEL_EFFECT_MAXIMUM | 1.0 | # 最高等级下关税税率的应用比例 |
| SUBVENTION_LEVEL_EFFECT_LOW | 0.25 | # 低等级下补贴率的应用比例 |
| SUBVENTION_LEVEL_EFFECT_HIGH | 0.5 | # 高等级下补贴率的应用比例 |
| SUBVENTION_LEVEL_EFFECT_MAXIMUM | 1.0 | # 最高等级下补贴率的应用比例 |
| REINVESTMENT_SUBSISTENCE_FRACTION_REDUCTION | 0.5 | # 持有建筑的人口的再投资乘以（1 - 此值 × 所持等级中自给建筑所占份额） |
| COMPANY_OVER_LIMIT_BONUS_PENALTY_MIN | 0.33 | # 若国内公司数量超过上限，所有公司加成都会受到惩罚。惩罚与超限比例成比例（超限 100% 则加成减少 100%），且最小值为该数值 |
| COMPANY_PRODUCTIVITY_RATIO_HIGH_THRESHOLD | 1.25 | # 生产率超过全球平均值此倍数的公司将被视为高生产率公司 |
| COMPANY_PRODUCTIVITY_RATIO_LOW_THRESHOLD | 0.75 | # 生产率低于全球平均值此倍数的公司将被视为低生产率公司 |
| COMPANY_PRODUCTIVITY_ABSOLUTE_HIGH_THRESHOLD | 25 | # 生产率超过该值的公司将始终被视为高生产率公司 |
| COMPANY_PRODUCTIVITY_ABSOLUTE_LOW_THRESHOLD | 5 | # 生产率低于该值的公司将始终被视为低生产率公司 |
| COMPANY_PROSPERITY_MAX | 100 | # 公司繁荣度不能超过此值 |
| COMPANY_PROSPERITY_BONUS_ACTIVATION_THRESHOLD | 100 | # 繁荣度达到此值时，公司将开始提供其繁荣度加成 |
| COMPANY_PROSPERITY_BONUS_DEACTIVATION_THRESHOLD | 75 | # 繁荣度降至此值时，公司将停止提供其繁荣度加成 |
| COMPANY_PROSPERITY_PRODUCTIVITY_MULTIPLIER | 50 | # 公司从建筑生产率（相对全球平均水平，定义值为恰好达到平均水平时）获得的 目标繁荣度 |
| COMPANY_PROSPERITY_PRODUCTIVITY_MAX | 100 | # 来自生产率的目标繁荣度上限 |
| COMPANY_PROSPERITY_EMPLOYED_LEVELS_MULTIPLIER | 1 | # 公司从满员雇佣的建筑等级数量获得的 目标繁荣度 |
| COMPANY_PROSPERITY_EMPLOYED_LEVELS_MAX | 50 | # 来自满员雇佣建筑等级的目标繁荣度上限 |
| COMPANY_PROSPERITY_POPULARITY_MULTIPLIER | 0.1 | # 公司根据其高管的人气度按比例获得的 目标繁荣度 |
| COMPANY_PROSPERITY_POPULARITY_MAX | 10 | # 来自人气度的目标繁荣度上限 |
| COMPANY_PROSPERITY_POPULARITY_MIN | 0 | # 来自人气度的目标繁荣度下限 |
| COMPANY_PROSPERITY_WEEKLY_INCREASE_BASE | 0.2 | # 每周向目标值增长的繁荣度基础量 |
| COMPANY_PROSPERITY_WEEKLY_INCREASE_SCALED | 0.04 | # 公司每拥有一个满员雇佣的建筑等级，每周向目标值增长的繁荣度 |
| COMPANY_PROSPERITY_WEEKLY_INCREASE_SCALED_MAX | 0.8 | # 来自雇佣等级的每周繁荣度增长上限 |
| COMPANY_PROSPERITY_WEEKLY_DECREASE_BASE | -1.0 | # 每周向目标值下降的繁荣度基础量 |
| COMPANY_PROSPERITY_WEEKLY_DECREASE_SCALED | 0.02 | # 公司每拥有一个满员雇佣的建筑等级，每周向目标值下降的繁荣度 |
| COMPANY_PROSPERITY_WEEKLY_DECREASE_SCALED_MAX | 0.8 | # 来自雇佣等级的每周繁荣度下降的最小值 |
| COMPANY_COUNTRY_CONSTRUCTION_BONUS_MULT | 0.2 | # 公司所在国的建造加成乘数 |
| NATIONALIZATION_PER_LEVEL_COST | 500 | # 按每建造点数计算，将一个建筑等级国有化的成本 |
| PRIVATIZATION_PER_LEVEL_COST | 250 | # 按每建造点数计算，将一个建筑等级私有化的成本 |
| MIN_FAKE_CONSTRUCTION_COST | 100 | # 用于国有化与私有化计算的最小建造成本 |
| COMPANY_COUNT_OF_REGIONAL_HQ_TYPES | 3 | # 州内为特色公司保留的建筑类型数量 |
| COMPANY_MINIMUM_LEVELS_PER_HQ | 5 | # 建立或维持一家公司所需的每总部最低建筑等级 |
| BASE_REGIONAL_HQS | 1 | # 获得投资特许后公司可用的地区总部基础等级 |
| LEVELS_PER_REGIONAL_HQ | 50 | # 公司需要获取多少等级才能获得一个新的地区总部 |
| COMPANY_ON_ESTABLISH_COOLDOWN_MONTHS | 60 | # 建立公司后可以解散它的冷却时间（月） |
| COMPANY_ON_DISBAND_COOLDOWN_MONTHS | 48 | # 解散公司后可以重新建立它的冷却时间（月） |
| BUILDING_LEVEL_BUREAUCRACY_COST | 1 | # 拥有一个等级的政府建筑的行政力成本 |
| COLLECTIVIZATION_DEBT_RATIO | 0.5 | # 可用于集体化的国家最大债务比例 |
| MIN_COLLECTIVIZATION_BUDGET | 1000000 | # 集体化预算的最小规模 |
| DYNAMIC_INDUSTRY_CHARTER | no | # 我们是否要使用动态行业特许状来取代脚本化的特许状 |
| COMPANY_INFLUENCE_LEVEL_STEPS | { 10 50 100 250 500 1000 1500 2500 5000 10000 } |  |
| COMPANY_CHARTER_AUTHORITY_COST | 100 | # 设立公司特许状所需的影响力（权威力）成本 |
| # 目前仅用于本地化文本，不用于逻辑 |  |  |
| HARVEST_CONDITION_MIN_INTENSITY | 0.0 | # 收成状况可随机出的最低强度值（0 <= 此值 < max） |
| HARVEST_CONDITION_MAX_INTENSITY | 9.0 | # 收成状况可随机出的最高强度值（min < 此值） |
| COMPANY_MONOPOLY_COOLDOWN_MONTHS | 60 | # 设立公司垄断后，需经过此月数的冷却期才能撤销其垄断 |
| COUNTRY_MONOPOLY_MAX_COUNT | 5 | # 一个国家可拥有的国家级垄断的最大数量 |
| COUNTRY_MONOPOLY_AUTHORITY_COST | 100 | # 设立国家级垄断所需的权威力成本 |
| WORLD_MARKET_MONOPOLY_MIN_SHARE | 0.5 | # 一个市场若要被视为拥有世界市场垄断，其出口份额必须高于此值 |
| MONOPOLY_PRICE_IMPACT | 0.2 | # 根据被视为处于垄断下的供应量比例，商品价格按此乘数提升 |
| PRIVATIZATION_DISCOUNT_MONOPOLY | 0.2 | # 对于垄断该建筑类型的公司，建筑私有化成本乘以此值 |
| PRIVATIZATION_DISCOUNT_COMPANY_ONLY | 0.1 | # 当禁止非公司私有化时，公司私有化建筑的成本乘以此值（可与 PRIVATIZATION_DISCOUNT_MONOPOLY 叠加） |
| PRESTIGE_GOODS_INPUT_THROUGHPUT_BONUS | 0.2 | # 吞吐量加成，按投入商品基础价值中威望商品所占比例进行缩放 |
| TOLL_RATE_NO_TOLLS | 0.0 | # “免通行费”设置下的通行费率。该数值与跨越海峡的商品价值相乘 |
| TOLL_RATE_LOW_TOLLS | 0.10 | # “低通行费”设置下的通行费率。该数值与跨越海峡的商品价值相乘 |
| TOLL_RATE_MEDIUM_TOLLS | 0.20 | # “中通行费”设置下的通行费率。该数值与跨越海峡的商品价值相乘 |
| TOLL_RATE_HIGH_TOLLS | 0.40 | # “高通行费”设置下的通行费率。该数值与跨越海峡的商品价值相乘 |
| TOLL_RATE_MULTIPLIER_FULL_CONTROL | 2.0 | # 若一国控制海峡两岸，上述数值乘以此乘数 |
| STRAIT_FULL_CONTROL_TRADE_IMPORTANCE_MULT | 1.5 | # 当控制者控制海峡两岸时，海峡贸易重要性的乘数 |
| MAX_PIRATED_GOODS_PER_HUB | 0.25 | # 单条枢纽→枢纽连接中可被海盗劫掠的商品最大百分比 |
| PIRACY_SHIP_SPEED_TO_GOODS_RATIO | 0.003 | # 每单位舰船速度所窃取的商品贸易量百分比 |
| PIRATED_GOODS_SALE_DISCOUNT | 0.5 | # 被劫掠商品出售并转化为国家收入时所得的价值百分比 |
| PIRACY_SELL_ORDERS_MIN_GOODS | 0.1 | # 某种商品被劫掠的总量至少要达到此值才会被加入销售订单，否则将 100% 损失 |
### 军事

| Define | 默认值 | 开发者注释 |
|---|---|---|
| POWER_PROJECTION_DIVISOR | 1000 | # 进攻与防御的平均值乘以人力再除以此值，以确定一个单位的力量投射 |
| INITIAL_MANPOWER_COST_MULTIPLIER | 10 | # 训练新兵相比维持这些新兵有额外的成本 |
| MANPOWER_DIVISOR | 10000 | # 士兵所需的战略商品按此数量为一组计算 |
| ATTRITION_RISK_EXILED_ARMY_ADD | 0.2 | # 被放逐的编队损耗风险增加此值 |
| ATTRITION_RISK_ON_ENEMY_TERRITORY_ADD | 0.3 | # 位于敌方领土上的被放逐编队损耗风险额外增加此值 |
| MANPOWER_LOST_DUE_TO_ATTRITION_PER_WEEK_MIN | 0.04 | # 单位每周因损耗可能损失的人力的最小百分比 |
| MANPOWER_LOST_DUE_TO_ATTRITION_PER_WEEK_MAX | 0.12 | # 单位每周因损耗可能损失的人力的最大百分比 |
| ATTRITION_RECOVERY_RATE_BASE | 0.7 | # 未参与战斗但受损耗影响的单位的基础恢复率，例如恢复率为 0.7 时，伤亡由 70% 的伤员和 30% 的死亡组成 |
| ATTRITION_RECOVERY_RATE_RANDOM_RANGE | 0.1 | # 未参与战斗但受损耗影响的单位恢复率的随机范围 |
| MIN_VARIABLE_DISTRIBUTION_PER_POP | 0 |  |
| MAX_VARIABLE_DISTRIBUTION_PER_POP | 100 |  |
| BATTLE_LETHALITY_MIN | 0.001 |  |
| BATTLE_LETHALITY_MAX | 0.005 |  |
| BATTLE_RAW_MANPOWER_INFLICTED_CASUALTY_RATIO | 0.5 | # 应用于由部队原始数量（即不考虑进攻/防御）造成的伤亡数——提高此值会降低战斗效率（CE）的重要性并使战斗更致命 |
| BATTLE_COMBAT_EFFICIENCY_INFLICTED_CASUALTY_RATIO | 1.5 | # 应用于将进攻/防御也纳入考量后部队造成的伤亡数——提高此值会提高 CE 的重要性并使战斗更致命 |
| BATTLE_MAX_CASUALTY_DISADVANTAGE_PENALTY | 1.0 | # battle_casualty_disadvantage 静态 modifier 的上限。1.0 表示最多施加 100% 的惩罚。 |
| MAX_CE_ADVANTAGE | 1 |  |
| MIN_MANPOWER_CASUALTY_PER_ROUND | 5 | # 每回合最低人力损失 |
| MIN_USABLE_MANPOWER | 100 | # 参与一场战斗的最低人力下限（否则由战斗宽度决定） |
| COMBAT_UNITS_PER_LEVEL | 1 | # 每一级军事建筑可支持的作战单位数量。所有可征募建筑（兵营/征兵中心）必须相同 |
| BASE_MORALE_RECOVERED_PER_DAY | 0.03 | # 默认每天恢复 3% 的士气 |
|  |  | # 移动相关 |
| COMMANDER_TRAVEL_PIXELS_TO_DAYS_SCALE | 0.045 | # 用于将移动距离从像素转换为天数。示例：移动 500px 变为 500 * 0.05 = 25 天 |
| COMMANDER_TRAVEL_MIN | 3 | # 指挥官到达其新编队的最短移动时间 |
| COMMANDER_TRAVEL_MAX | 50 | # 将移动时间限制为 GENERAL_TRAVEL_MAX 天。 |
| EMBARKATION_MAX_DOCKED_FLEET_TRAVEL_DAYS | 30 | # 如果陆军前往停泊舰队港口的移动时间超过此天数，则改为寻找更近的沿海州 |
| FORMATION_TRAVEL_NETWORK_SPEED | 15 | # （临时）编队通过移动网络移动时的基础速度 |
| EMPTY_FLEET_MOVEMENT_SPEED | 100 | # 无船只舰队的移动速度，以便它们仍可被移动 |
| BATTLE_PLAN_ADVANCE_PROGRESS_TO_LAUNCH | 100 | # 发起进攻所需的累计推进进度 |
| BATTLE_BASE_MIN_PROVINCES_TAKEN | 4 |  |
| BATTLE_BASE_MAX_PROVINCES_TAKEN | 12 |  |
| BATTLE_PROVINCES_TAKEN_FRONT_PROVINCES_NUM_DIVISOR | 5 | # 进攻方额外占领（前线省份数量）除以此值，并限制在 BATTLE_BASE_MIN_PROVINCES_TAKEN 和 BATTLE_BASE_MAX_PROVINCES_TAKEN 之间 |
| BATTLE_PROVINCES_TAKEN_THEATER_PROVINCES_NUM_DIVISOR | 50 | # 进攻方额外占领的省份数为（战区省份数）除以此值，并被限制在 BATTLE_BASE_MIN_PROVINCES_TAKEN 与 BATTLE_BASE_MAX_PROVINCES_TAKEN 之间 |
| BATTLE_PROVINCES_TAKEN_ATTACKING_UNIT_SCALE | 0.02 | # 占领省份数乘以（1 + 此值 * 战斗结束时剩余的进攻方单位数量） |
| BATTLE_PROVINCES_TAKEN_MAX_DEPTH_MIN | 2 | # 进攻方可占领省份距战斗省份的最大距离（最小值） |
| BATTLE_PROVINCES_TAKEN_MAX_DEPTH_MAX | 10 | # 可占领省份距战斗省份的最大距离（最大值） |
| BATTLE_PROVINCES_TAKEN_MAX_DEPTH_FRONT_PROVINCES_NUM_DIVISOR | 50 | # 前线省份数除以此值，并加到进攻方可占领省份的最大纵深上 |
| BATTLE_PROVINCES_TAKEN_MAX_DEPTH_THEATER_PROVINCES_NUM_DIVISOR | 500 | # 战区省份数除以此值，并加到进攻方可占领省份的最大纵深上 |
| DEFENSIVE_PROVINCES_RETAKEN_MAX_DEPTH | 1 | # 防御战斗中可收复省份距战斗省份的最大距离 |
| BATTLE_PROVINCES_TAKEN_THEATER_UNIT_SCALE | 2 | # 占领省份数按 战区省份数 /（战区内单位数 * 此 define 值）进行缩放 |
| BATTLE_PROVINCES_TAKEN_MAX_EXTRA | 3 | # 如果所选省份会导致分割，则只要新战区包含至多 BATTLE_PROVINCES_TAKEN_MAX_EXTRA 个省份，即占领该新战区。这可能不会遵守距离限制（BATTLE_PROVINCES_TAKEN_MAX_DEPTH）。 |
| BATTLE_PROVINCES_TAKEN_THEATER_MIN_SCALE | 0.01 | # 由于 BATTLE_PROVINCES_TAKEN_THEATER_UNIT_SCALE 的作用，占领省份数所导致的缩放系数不得低于此值 |
| BATTLE_PROVINCES_TAKEN_ABSOLUTE_MIN | 1 | # 在应用所有缩放之后，一次成功推进中可占领省份的绝对最小数量 |
| CONVOY_RAIDING_STRENGTH_MULT | 0.3 | # 每点护航舰袭击（Convoy raiding）强度的强度值 |
| CONVOY_RAIDING_COOLDOWN_DAYS_MIN | 10 | # 该海域节点下一次护航舰袭击前的最少天数 |
| CONVOY_RAIDING_COOLDOWN_DAYS_MAX | 30 | # 该海域节点下一次护航舰袭击前的最多天数 |
| CONVOY_RAIDING_DAMAGE_MIN_RANDOM_FACTOR | 0.5 | # 实际护航舰袭击伤害会在 CONVOY_RAIDING_DAMAGE_MIN_RANDOM_FACTOR 与 CONVOY_RAIDING_DAMAGE_MAX_RANDOM_FACTOR 之间缩放，以提供一定的随机变化 |
| CONVOY_RAIDING_DAMAGE_MAX_RANDOM_FACTOR | 1.0 | # 实际护航舰袭击伤害会在 CONVOY_RAIDING_DAMAGE_MIN_RANDOM_FACTOR 与 CONVOY_RAIDING_DAMAGE_MAX_RANDOM_FACTOR 之间缩放，以提供一定的随机变化 |
| CONVOY_RAIDING_DEFENSE_MULT | 0.15 | # 巡逻舰船（舰船数 * 海军上将防御值）对护航舰袭击强度的削减程度 |
| CONVOY_RAIDING_MAX_DEFENSE | 0.90 | # 示例：防御方永远无法阻挡超过其当前所受护航伤害的 90% |
|  |  | # 遭袭后护航舰的恢复速率基于一个全局速率和一个本地速率，取两者中较低者 |
| CONVOY_RAIDING_GLOBAL_RECOVERY_RATE | 0.001 | # 受损护航舰每天被替换的速率，相对于遭袭国家已生产的护航舰总数 |
| CONVOY_RAIDING_LOCAL_RECOVERY_RATE | 0.01 | # 受损护航舰每天被替换的速率，相对于经过该海域节点的护航舰总数 |
| CONVOY_RAIDING_RECOVERY_RATE_PEACETIME_FACTOR | 4 | # 当国家处于和平时，护航舰的恢复速度会加快这么多倍 |
| MIN_OFFENSE_DEFENSE | 1 | # 单位可拥有的最低绝对进攻或防御值 |
| INTERCEPTION_DELAY_BASE_DAYS | 5 | # 每次海军上将拦截尝试之间至少间隔这么多天 |
| INTERCEPTION_DELAY_MAX_RANDOM_DAYS_FACTOR | 10 | # 每次海军上将拦截尝试之间最多额外增加这么多天 |
| INTERCEPTION_BASE_CHANCE | 0.1 | # 试图拦截敌方海军上将时的基础概率 |
| DEMOBILIZATION_TIME_DAYS | 90 | # 一支部队返回驻地后完全解除动员所需的天数 |
| MOBILIZATION_INFRASTRUCTURE_FACTOR | 0.01 | # 每点基础设施产生的动员量。一个营的动员需要整整一点动员量 |
| MIN_MOBILIZATION_PER_DAY | 0.05 | # 每个正在动员的营每天获得的最少动员量（一个州内最后获得动员量的部队可能只能获得剩余的部分） |
| MAX_MOBILIZATION_PER_DAY | 0.20 | # 每个正在动员的营每天获得的最多动员量 |
| FRONT_MARKER_ADVANTAGE_PREDICTION_MIN_COMBAT_POWER | 0.01 | # 计算前线优势时用作最小值 |
| BATTLE_CONDITION_MIN_TICKS_BETWEEN_UPDATE_DEFAULT | 40 | # 除非战斗条件类型另有说明，否则战斗条件在至少经过这么多 tick 之前不会更新 |
| BATTLE_CONDITION_CHANCE_TO_UPDATE_PER_EXTRA_TICK | 0.01 | # 超过最小 tick 数后，每经过一个 tick 便有此概率刷新战斗条件（即在最小值之后再过 13 个 tick，有 13% 的概率切换） |
| DEFAULT_ORDER | "advance" | # 将军的默认命令 |
| MILITARY_FORMATION_COMMAND_LIMIT_NO_COMMANDER | 20 | # 部队没有指挥官时的默认指挥上限 |
| LOW_COMMAND_LIMIT_GRACE_PERIOD_DAYS | 30 | # 部队单位超过其指挥上限后，经过多少天才会开始受到惩罚 |
| INVALID_NAVAL_MISSION_GRACE_PERIOD_DAYS | 10 | # 执行无效海军任务的舰队在返回港口前会等待的天数 |
| FORMATION_AUTO_MERGE_GRACE_PERIOD_DAYS | 3 | # 仅自动合并在此天数内创建的部队中的单位 |
| COMMANDER_SUFFICIENT_CAPACITY_MULT | 1.5 | # 若某类型指挥官的累计指挥上限至少达到该类型现役作战单位总数的这个倍数，则视为数量充足 |
| UNNECESSARY_PROMOTION_PENALTY_YEARS | 5 | # 不必要晋升所导致的利益集团好感惩罚持续的年数 |
| UNNECESSARY_PROMOTION_ARMED_FORCES_IG | "ig_armed_forces" | # 用于识别军队利益集团，该集团始终对不必要的晋升感到不满 |
| RECENTLY_PROMOTED_YEARS | 5 | # 最近晋升的指挥官获得的忠诚加成持续的年数 |
| MILITARY_FORMATION_ORGANIZATION_MIN | 0 | # 即使超过指挥上限，军事部队也始终保留的最低组织度 |
| MILITARY_FORMATION_ORGANIZATION_MAX | 100 | # 军事部队被视为满组织度所需的最高组织度 |
| MILITARY_FORMATION_ORGANIZATION_LOSS_RATE | 0.05 | # 军事部队一天内可损失当前组织度的百分比 |
| MILITARY_FORMATION_ORGANIZATION_LOSS_MIN | 1 | # 军事部队一天内可损失的最低组织度 |
| MILITARY_FORMATION_ORGANIZATION_GAIN_MIN | 0.1 | # 军事部队一天内可获得的最低组织度 |
| MILITARY_FORMATION_ORGANIZATION_SPECIAL_UNITS_ADD | -50 | # 特殊单位过多的军事部队获得此组织度惩罚：目标 = 目标 + ( 超出比例 * 此值 ) |
| MILITARY_FORMATION_ORGANIZATION_EXILE_MULT | -1 | # 被放逐的军事部队其目标组织度被调整为：目标 = 目标 * ( 1 + 此值 ) |
| MILITARY_FORMATION_ORGANIZATION_SUPPLY_SHORTAGE_EFFECT_THRESHOLD | 0.25 | # 补给降至低于此比例时开始受到组织度惩罚 |
| MILITARY_FORMATION_SHORTAGE_BATTALION_ORG_WEIGHT | 0.25 | # 所需商品完全短缺的营的组织度目标权重（1 = 无惩罚）；按该营的商品短缺严重程度进行插值 |
| MILITARY_FROMATION_MAX_RESUPPLY_RATIO_PER_WEEK | 0.1 | # 每周，一支军事编队可以补充其总补给需求量的这一比例 |
| MILITARY_FORMATION_MIN_RESUPPLY_PER_WEEK | 10 | # 每周，一支军事编队至少可以补充这一数量的补给需求 |
| MOBILIZATION_OPTION_DIFFERENCE_ORGANIZATION_IMPACT | 20 | # 合并采用不同动员选项的编队之间的单位时，每相差一级所受到的组织度惩罚 |
| FLEET_PRESENCE_GAIN_PER_DAY | 0.02 | # 舰队在任务区域内时每天获得的存在感数量 |
| FLEET_PRESENCE_DECAY_PER_DAY | 0.02 | # 舰队不在任务区域内时每天衰减的存在感数量 |
| FLEET_PRESENCE_TRANSPORTING_OR_INVADING | 1.0 | # 运送陆军或支援海上登陆的舰队被强制赋予的海上存在感 |
| FLEET_GUARANTEED_BATTLE_SIZE | 0.5 | # 无论海上存在感如何，保证有一半的舰船能够抵达战场 |
| FLEET_SPOT_BASE_CHANCE | 0.00005 | # 发现敌方舰队的基础概率，乘以侦察方的平均侦测能力和目标的平均可见度 |
| FLEET_SPOT_SCALING_MULTIPLIER | 0.01 | # 发现舰队时按舰船总数计算的缩放系数乘数 |
| MILITARY_FORMATION_WEEKLY_MAX_UNIT_UPGRADES_ARMY | 0.1 | # 每周一支已动员的陆军可以升级其单位总数的这一比例（0.0-1.0） |
| MILITARY_FORMATION_WEEKLY_MAX_UNIT_UPGRADES_FLEET | 0.05 | # 每周一支已动员的舰队可以升级其单位总数的这一比例（0.0-1.0） |
| MANPOWER_RATIO_REQUIRED_TO_CLEAR_DEFEATED_ADMIRALS | 0.75 | # 战败的舰队若当前/最大人力比例低于此值，将保持战败状态 |
| MILITARY_FORMATION_AUTO_DEPLOY_DISTANCE_LIMIT | 250 | # 陆军不会自动部署到距离其当前位置超过此像素距离的前线 |
| BASECAMP_WANTED_FORMATIONS_SCORE | 1.0 | # 需要加入营地的大本营编队越多，得分越高 |
| BASECAMP_DISTANCE_SCORE_THRESHOLD | 100 | # 与下方的惩罚相乘，然后从营地得分中扣除 |
| BASECAMP_DISTANCE_PENALTY | 0.4 | # 营地距离编队越远，得分越低 |
| BASECAMP_DISTANCE_TO_HOME_HQ_PENALTY | 0.2 | # 营地距离编队本土总司令部越远，得分越低 |
| BASECAMP_OWN_COUNTRY_SCORE | 0.2 | # 若营地所在州属于编队的国家，则加到营地得分上 |
| BASECAMP_STRATEGIC_OBJECT_SCORE | 1.1 | # 若营地靠近战略目标，则加到营地得分上 |
| BASECAMP_NUM_PROVINCES_SCORE | 0.05 | # 营地周边的省份越多，得分越高 |
| # 以下 defines 控制完全封锁一个州所需的封锁强度 # 基础目标强度等于 state_blockade_resistance_add 修正值 |  |  |
| BLOCKADE_TARGET_STRENGTH_MAXIMUM | 100000 | # 所需封锁强度不能高于此值 |
| BLOCKADE_TARGET_STRENGTH_PER_TRADED_UNIT | 0.1 | # 市场区域内每单位进出口基础值会使所需封锁强度增加此值（仅适用于世界市场枢纽） |
| BLOCKADE_TARGET_STRENGTH_PER_PRODUCED_UNIT | 0.15 | # 受封锁影响的建筑（如渔场和船坞）中每单位商品生产基础值会使所需封锁强度增加此值 |
| BLOCKADE_TARGET_STRENGTH_PER_MERCHANT_MARINE | 3 | # 每支经由该州港口的护航船队会使所需封锁强度增加此值 |
| BLOCKADE_WORLD_MARKET_ACCESS_IMPACT_SCALING | 0.75 | # 被封锁的世界市场枢纽的世界市场接入降低值，随封锁等级而变化 |
| BLOCKADE_SHIPPING_LANE_IMPACT_SCALING | 0.75 | # 被封锁航线的效率降低值，随起点或终点中封锁程度更高一方的封锁等级而变化 |
| BLOCKADE_THROUGHPUT_IMPACT_SCALING | 0.75 | # 受封锁影响的建筑的吞吐量减少幅度，随封锁等级变化 |
| BLOCKADE_SEA_PRESENCE_TRESHOLD | 0.5 | # 海上存在度达到何种水平时封锁生效 |
| BLOCKADE_FORCED_BATTLE_LEVEL = 1.0 # 从封锁等级至少达到该数值的州出港的舰队，将被强制与实施封锁的舰队进行一场战斗 |  |  |
|  |  | # 以下 defines 控制港口轰炸对敌方沿海州的效果 |
| BOMBARDMENT_DEVASTATION_MAX | 25.0 | # 港口轰炸可产生的最大毁灭度 |
| BOMBARDMENT_DEVASTATION_RATE | 0.20 | # 每日毁灭度增加量，随有效轰炸等级变化 |
| BOMBARDMENT_BUILDING_DAMAGE_BASE_CHANCE | 0.02 | # 每日随机降低一座沿海建筑等级的基础概率，随有效轰炸等级变化 |
| BOMBARDMENT_SEA_PRESENCE_THRESHOLD | 0.1 | # 海上存在度达到何种水平时港口轰炸生效 |
| OFFICERS_TO_SERVICEMEN_RATIO_THRESHOLD | 0.75 | # 如果某建筑的军官与水兵比例低于其理想比例的这一百分比，该建筑提供的作战单位将开始应用下方定义的有效性系数。阈值越高，有效性系数越晚生效（即在更缺军官时才生效）[>= 0 且 <= 1] |
| OFFICERS_TO_SERVICEMEN_RATIO_EFFECTIVENESS_FACTOR_MIN | -0.5 | # 对完全缺乏军官的建筑所提供单位施加的攻防有效性系数。-1 表示 -100%。总攻防不会低于 MIN_OFFENSE_DEFENSE。[>= -1 且 <= 0] |
| OFFICERS_TO_SERVICEMEN_RATIO_EFFECTIVENESS_FACTOR_MAX | 0 | # 对不缺军官的建筑所提供单位施加的攻防有效性系数。0 表示 -0%，因此由不缺军官的建筑提供的单位将在其条件允许的范围内以全部有效性作战 [>= OFFICERS_TO_SERVICEMEN_RATIO_EFFECTIVENESS_FACTOR_MIN 且 <= 0] |
| SAILORS_PER_ASSIGNMENT_SLOT | 100 | # 海军行政建筑每个舰船配备槽位的水兵数量 |
| SAILORS_PER_BUILDING_LEVEL | 1000 | # 海军行政建筑每级建筑等级的水兵数量 |
| ACTIVE_SHIP_LIVING_CREW_PERCENTAGE | 0.1 | # 如果舰船的存活船员比例不高于此百分比，该舰船将失去行动能力 |
| DESTROYED_SHIP_LIVING_CREW_PERCENTAGE | 0 | # 如果舰船的存活船员比例不高于此百分比，且不在港口中，该舰船将被摧毁 |
| MINIMUM_SHIP_CREW_PERCENTAGE_TO_DEPLOY | 0.1 | # 舰队中任何舰船的存活船员比例低于此百分比时，该舰队无法部署，且海上的此类舰队将被遣返重新补充船员 |
| SHIP_PARTICIPATE_IN_UPRISING_CREW_PERCENTAGE | 0.33 | # 如果舰船船员中至少有此比例来自叛乱的州，该舰船可以参与起义 |
| SHIP_MAINTENANCE_SHIPYARD_PREMIUM_FACTOR | 0.2 # 造船厂在维护成本上获得的利润率（商品成本 * (1 + 此值)） |  |
| SHIP_MAINTENANCE_GOODS_TO_CONSTRUCTION_GOODS_FACTOR | 0.002 | # 舰船维护商品成本与建造商品成本的比率。用于确定由造船厂支付维护时所需的商品数量 |
| SHIP_UPKEEP_GOODS_TO_CONSTRUCTION_GOODS_FACTOR | 0.002 | # 舰船保养商品成本与建造商品成本的比率。用于根据建造时所需的商品数量确定保养所需的商品数量 |
| SHIP_UPKEEP_GOODS_DOCKED_MULT | -0.8 | # 如果舰船停泊在港口，其保养商品成本将按此乘数值变化 |
| SHIP_CONSTRUCTION_COST_MODIFICATION_LEVEL_FACTOR | 1.05 | # 舰船的建造成本将乘以此值的（总改装等级）次方 |
| SHIP_TEMPLATE_DEFAULT_MODIFICATION_LEVEL | 2 | # 用于计算舰船商品平衡的每槽位默认改装等级的默认值 |
| LOGISTICS_CENTER_SUPPLY_PER_LEVEL | 10 | # 以该州作为补给枢纽的编队每消耗这么多基础补给，即生成一级新的后勤中心 |
| SUPPLY_SHIP_TYPE | "ship_type_supply_ship" # 代码侧被视为补给舰的舰船类型。修改此值极可能导致功能异常 |  |
| SUPPLY_SHIP_MAINTENANCE_COST_PER_SHIP | 1 | # 每艘补给舰的每周维护费用 |
| SHIP_CONSTRUCTION_MAINTENANCE_FRACTION | 0.0003 | # 舰船总建造成本中每周作为建造点数维护所消耗的比例 |
| SHIP_CONSTRUCTION_MAINTENANCE_PENALTY_THRESHOLD | 0.5 | # 满足率等于或低于该值时，维护惩罚达到100% |
| SHIP_CONSTRUCTION_MAINTENANCE_MAX_HP_PENALTY_FRACTION | 0.05 | # 满维护惩罚下舰船每周损失的总生命值最大比例 |
| SHIP_CONSTRUCTION_MAINTENANCE_DAMAGE_RATIO | 0.2 | # 每周随机选中承受维护损伤的舰船比例（0-1） |
| SUPPLY_SHIP_CONSTRUCTION_MAINTENANCE_FRACTION | 0.0003 | # 补给舰建造成本中每周作为建造点数维护所消耗的比例 |
| SUPPLY_SHIP_MAINTENANCE_STOCKPILE_REMOVAL_FRACTION | 0.05 | # 满维护惩罚下每周移除的补给舰最大比例 |
| FLEET_RESUPPLY_SURPLUS | 0.25 | # 舰队尝试提升补给等级时，获得的补给超过维护速率（即送达补给等于消耗补给）的幅度 |
| ARMY_RESUPPLY_SURPLUS | 0.25 | # 陆军尝试提升补给等级时，获得的补给超过维护速率（即送达补给等于消耗补给）的幅度 |
| FLEET_SUPPLY_REPLENISH_SHIP_MULT | 1.1 | # 补给储备未满时舰队请求的补给舰数量的额外倍率 |
| SHIP_POWER_PROJECTION_HULL_DAMAGE_MULTIPLIER | 0.33 | # 计算舰船威力投射时施加于船体损伤的乘数 |
| SHIP_POWER_PROJECTION_CREW_DAMAGE_MULTIPLIER | 0.33 | # 计算舰船威力投射时施加于船员损伤的乘数 |
| SHIP_POWER_PROJECTION_ARMOR_MULTIPLIER | 0.33 | # 计算舰船威力投射时施加于装甲的乘数 |
| SHIP_POWER_PROJECTION_HIT_POINTS_MULTIPLIER | 0.1 | # 计算舰船威力投射时施加于最大生命值的乘数 |
| SHIP_CREW_STARTING_VETERANCY_EXPERIENCE | 0 | # 舰船船员招募时的初始经验值 |
| SHIP_MAX_VETERANCY_EXPERIENCE | 1000 | # 舰船的经验上限。应高于最高资历等级的经验阈值。 |
| SHIP_VETERANCY_EXPERIENCE_DECAY_RATE | 0.01 | # 未执行任务时每周损失的经验百分比。 |
| SHIP_VETERANCY_EXPERIENCE_MIN_DECAY | 1 | # 因衰减每周损失的最小经验值（若适用衰减），与当前经验无关 |
| SHIP_VETERANCY_BASE_EXPERIENCE_GAIN_BATTLE_VICTORY | 5 | # 所在方取得战斗胜利时舰船获得的基础经验。 |
| SHIP_VETERANCY_BASE_EXPERIENCE_GAIN_BATTLE_DEFEAT | 2 | # 所在方战斗失败时舰船获得的基础经验。 |
| SHIP_VETERANCY_BASE_EXPERIENCE_GAIN_BATTLE_SUNK_ENEMY_SHIP | 1 | # 舰船在战斗中每击沉一艘舰船获得的基础经验。 |
| SHIP_COMBAT_POWER_HULL_DAMAGE_MULTIPLIER | 0.75 | # 计算舰船战斗威力时施加于船体损伤的乘数 |
| SHIP_COMBAT_POWER_CREW_DAMAGE_MULTIPLIER | 0.25 | # 计算舰船战斗威力时施加于船员损伤的乘数 |
| SHIP_COMBAT_POWER_SPEED_MULTIPLIER | 3.0 | # 计算舰船战斗威力时施加于速度的乘数 |
| COMBAT_UNIT_GROUP_MARINES_GROUP | "combat_unit_group_marines" | # 海军陆战队类型 |  |
| FLAGSHIP_CHANGE_COOLDOWN_MONTHS | 60 | # 更换旗舰后，需等待这么多个月才能再次更换 |
| FLAGSHIP_ON_WON_FAIR_COMBAT_POWER_RATIO_THRESHOLD | 0.5 | # 对方与旗舰一方战力之比至少达到此值，on_flagship_battle_won 才会触发 |
| NAVAL_MISSION_SUPPLY_COST_FACTOR_SCALING | 0.1 | # 海军任务中超出第一个之后的每个海域所额外产生的补给消耗（百分比，0-1） |
| NAVAL_MISSION_BASE_MAX_SEA_REGIONS | 2 | # 舰队任务可分配的海域基础最大数量（受修正影响前） |
| NAVAL_MISSION_TYPE_INTERCEPT | "naval_mission_type_intercept" |  |
| NAVAL_MISSION_TYPE_PROJECT_POWER | "naval_mission_type_project_power" |  |
| FRIENDLY_PORT_MAX_SUPPLY_DISTANCE_DISCOUNT | 0.5 | # 编队靠近友好港口时可获得的最大补给距离折扣（0-1） |
| FRIENDLY_PORT_MAX_DISTANCE | 2500 | # 友好港口折扣降为零时的交通网络距离 |
| AI_FIND_FLEET_EXPECTED_DISTANCE | 25000 | # 用于归一化舰队与陆军距离评分的预期地图距离 |
| DEFAULT_ARMY_COLOR | "army_color_6" |  |
| DEFAULT_FLEET_COLOR | "fleet_color_8" |  |

### 外交

| Define | 默认值 | 开发者注释 |
|---|---|---|
| DEFAULT_DIPLOMATIC_PLAY | "dp_default_treaty_article" |  |
| DEFAULT_WAR_GOAL_IS_HUMILIATION | yes | # 若此项为否，默认战争目标改为赔款转移 |
| DEFAULT_TRUCE_MONTHS | 60 |  |
| PEACE_DEAL_DURATION_IN_DAYS | 30 |  |
| PEACE_DEAL_COOLDOWN_IN_DAYS | 120 |  |
| PACT_REQUIRES_APPROVAL_MIN_FORCED_MONTHS | 12 | # 需要批准的外交条约在可撕毁前，至少有这段冷却期 |
| OBLIGATION_FORCED_PACT_MONTHS | 120 |  |
| SWAY_FORCED_PACT_MONTHS | 120 |  |
| EXPEL_DIPLOMATS_MONTHS | 60 |  |
| OBLIGATION_MONTHS | 120 |  |
| RECENTLY_CONQUERED_DURATION_MONTHS | 120 |  |
| RECENTLY_LIBERATED_DURATION_MONTHS | 120 |  |
| DIPLOMATIC_DEMAND_PENDING_APPROVAL_DAYS | 14 | # 天数，超过后需求自动被拒绝并开启外交博弈 |
| DIPLOMATIC_DEMAND_TIMEOUT_DAYS | 14 | # 天数，超过后被接受或拒绝的需求将被删除 |
| DIPLOMATIC_ACTION_COOLDOWN_DAYS | 0 | # 两次外交行动/提案之间必须等待的天数 |
| DIPLOMATIC_ACTION_PENDING_APPROVAL_DAYS | 30 | # 天数，超过后待定行动自动被拒绝 |
| TREATY_PROPOSAL_PENDING_APPROVAL_DAYS | 30 | # 天数，超过后待定条约提案自动被拒绝 |
| DIPLOMATIC_PACT_COST_DEFAULT | 0 | # 条约默认的影响力维持费用 |
| DIPLOMATIC_PACT_COST_MULT_FROM_INFAMOUS | 0.25 | # 恶名达到“声名狼藉”等级时，条约维持费用按此比例增加 |
| DIPLOMATIC_PACT_COST_MULT_FROM_NOTORIOUS | 0.50 | # 恶名达到“恶名昭彰”等级时，条约维持费用按此比例增加 |
| DIPLOMATIC_PACT_COST_MULT_FROM_PARIAH | 1.00 | # 恶名达到“众矢之的”等级时，条约维持费用按此比例增加 |
| DIPLOMATIC_PACT_COST_LOBBY_CLOUT_MULT | 0.01 | # 亲/反该国游说集团的每点政治力量，会按条约是否符合其目标而降低或提高与该国维持条约的影响力费用倍率 |
| DIPLOMATIC_PACT_COST_LOBBY_CLOUT_MAX | 0.5 | # 亲/反该国游说集团带来的费用倍率影响不能超过此值 |
| TREATY_ARTICLE_COST_LOBBY_CLOUT_MULT | 0.01 | # 亲/反该国游说集团的每点政治力量，会降低或提高与该国维持条约条款的影响力费用倍率 |
| TREATY_ARTICLE_COST_LOBBY_CLOUT_MAX | 0.5 | # 亲/反该国游说集团带来的费用倍率影响不能超过此值 |
| RIVALRY_BASE_SCALING | 0.25 | # 敌对关系至少提供此数值的影响力缩放 |
| RIVALRY_SCALING_PER_INTEREST_LEVEL | 0.25 | # 敌对关系为每个重叠的利益等级提供此数值的影响力缩放 |
| RIVALRY_MAX_SCALING | 2.0 | # 敌对关系的影响力缩放不能超过此数值 |
| RIVALRY_LOWER_RANK_SCALING_MULT | 0.5 |  |
| RIVALRY_SCALING_LOBBY_CLOUT_MULT | 0.01 | # 亲/反国家游说集团的每一点政治力量按此数值减少或增加敌对关系带来的影响力收益（反国家增加，亲国家减少） |
| RIVALRY_SCALING_LOBBY_CLOUT_MAX | 0.5 | # 亲/反国家游说集团对敌对关系影响力倍率的影响不能大于此数值 |
| MIN_RELATIONS | -100 |  |
| MAX_RELATIONS | 100 |  |
| START_RELATIONS | 0 |  |
| RELATIONS_THRESHOLD_FRIENDLY | 80 |  |
| RELATIONS_THRESHOLD_AMICABLE | 50 |  |
| RELATIONS_THRESHOLD_CORDIAL | 20 |  |
| RELATIONS_THRESHOLD_POOR | -20 |  |
| RELATIONS_THRESHOLD_COLD | -50 |  |
| RELATIONS_THRESHOLD_HOSTILE | -80 |  |
| REQUIRED_IMPROVE_RELATIONS_PROGRESS | 100 | # 将关系提升 1 点所需的关系改善进度 |
| REQUIRED_DAMAGE_RELATIONS_PROGRESS | -100 | # 将关系降低 1 点所需的关系损害进度 |
| INITIAL_LIBERTY_DESIRE | 50 | # 外交条约初始化时的独立倾向数值。 |
| WEEKLY_LIBERTY_DESIRE_FROM_SUPPORT_INDEPENDENCE_TOTAL_MAX | 0.5 | # 所有针对该国家的支持独立每周带来的独立倾向增长上限 |
| MIN_INFAMY | 0 | # 恶名不能低于此数值 |
| MAX_INFAMY | 1000 | # 恶名不能高于此数值 |
| START_INFAMY | 0 | # 这是国家开局时默认拥有的恶名值 |
| INFAMY_THRESHOLD_INFAMOUS | 25 | # 超过此数值，国家被视为声名狼藉并获得相关惩罚 |
| INFAMY_THRESHOLD_NOTORIOUS | 50 | # 超过此数值，国家被视为臭名昭著并获得相关惩罚 |
| INFAMY_THRESHOLD_PARIAH | 100 | # 超过此数值，国家被视为众矢之的并获得相关惩罚 |
| BASE_YEARLY_INFAMY_DECAY_RATE | 5.0 | # 恶名每年的衰减速率 |
|  |  | # 可殖民国家使用紧张度代替关系 |
| MIN_TENSION | 0 |  |
| MAX_TENSION | 100 |  |
| START_TENSION | 0 |  |
| TENSION_THRESHOLD_UNEASY | 25 |  |
| TENSION_THRESHOLD_TENSE | 50 |  |
| TENSION_THRESHOLD_VOLATILE | 75 |  |
| TENSION_DECAY_RATE | 5 | # 每年 |
| TENSION_INCREASE_MIN | 2.5 | # 殖民一个省份时紧张度至少增加此数值 |
| TENSION_INCREASE_MAX | 20.00 | # 殖民一个省份时紧张度至多增加此数值 |
| TENSION_NUM_PROVINCE_SCALING_BASE | 10 | # 当未开化国家的省份数低于此数值时，其省份被殖民会获得额外的紧张度 |
| TENSION_NUM_PROVINCE_SCALING_RATE | 2.0 | # 因仅拥有少量省份而导致每被夺取一个省份的紧张度增长倍率上限 |
| TENSION_INCREASE_RATE_ADJACENT | 0.5 | # 当被殖民的是邻国省份时，紧张度增长乘以此系数 |
| TENSION_UPRISING_CHANCE | 0.02 | # 爆发战争而非继续殖民下一个省份的概率（紧张度至少达到 TENSION_THRESHOLD_VOLATILE 时的基础值） |
| SWAY_OFFER_TIMEOUT_DAYS | 14 |  |
| SWAY_OFFER_REJECTED_COOLDOWN_DAYS | 7 | # 必须等待这么多天才能再次尝试拉拢拒绝过你上次拉拢的国家 |
| SWAY_OFFER_CALL_IN_OBLIGATION_MANEUVERS_COST | 10 |  |
| SWAY_OFFER_OWE_OBLIGATION_MANEUVERS_COST | 10 |  |
| SWAY_OFFER_CALL_ALLY_MANEUVERS_COST | 20 |  |
| SWAY_OFFER_TRANSFER_STATE_MANEUVERS_COST | 10 |  |
| SWAY_OFFER_TRANSFER_SUBJECT_MANEUVERS_COST | 10 |  |
| SWAY_OFFER_BECOME_SUBJECT_MANEUVERS_COST | 5 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_JOIN_POWER_BLOC | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_LEAVE_POWER_BLOC | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_COLONIZATION_RIGHTS | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_FORCE_NATIONALIZATION | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_HUMILIATION | 20 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_UNIFICATION_LEADERSHIP | 30 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_OPEN_MARKET | 20 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_REGIME_CHANGE | 8 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_ANNEX_COUNTRY | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_LIBERATE_COUNTRY | 30 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_MAKE_PROTECTORATE | 8 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_REDUCE_AUTONOMY | 5 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_INCREASE_AUTONOMY | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_MAKE_TRIBUTARY | 8 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_MAKE_DOMINION | 8 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_CONQUER_STATE | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_RETURN_STATE | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_REVOKE_CLAIM | 5 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_REVOKE_ALL_CLAIMS | 0 | # 无法被添加，仅用于特殊博弈 |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_CONTAIN_THREAT | 1000 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_TRANSFER_SUBJECT | 8 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_LIBERATE_SUBJECT | 20 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_UNIFICATION | 100 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_INDEPENDENCE | 20 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_SECESSION | 100 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_POPULATION_SCALING_FACTOR | 10000 | # 下方乘数所对应的人口数量 |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_POPULATION_SCALING_MULTIPLIER | 0.03 | # 一个国家/州每有 SWAY_OFFER_WARGOAL_MANEUVERS_COST_POPULATION_SCALING_FACTOR 人口，博弈点数花费便乘以此值 |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_POPULATION_SCALING_MULTIPLIER_MAX_PER_STATE | 2.5 | # 每个受影响州的博弈点数人口乘数不能高于此值 |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_POPULATION_SCALING_MULTIPLIER_MAX_TOTAL | 5 | # 无论受影响的州有多少个，博弈点数人口乘数总计不能高于此值 |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_HOMELAND_FACTOR | -0.25 | # 若被夺取/建立傀儡等的州是发起方的本土，博弈点数花费会按此值调整 |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_UNINCORPORATED_FACTOR | -0.5 | # 若被夺取/建立傀儡等的州是未合并州，博弈点数花费会按此值调整 |
| MAKE_WARGOAL_PRIMARY_DEMAND_MANEUVERS_COST | 0.5 | # 将战争目标转为主要诉求时，需支付该战争目标基础博弈点数花费的这一比例 |
| MAKE_WARGOAL_PRIMARY_DEMAND_INFAMY_AMOUNT | 0.5 | # 将战争目标转为主要诉求时，会累积该战争目标基础恶名的这一比例 |
| ALLY_WARGOAL_MAX_MANEUVERS_COST | 25 | # 当盟友在博弈中添加一个"免费"战争目标时，其博弈点数花费不能高于此值 |
| PERSONAL_UNION_ACTION_NAME | "personal_union" |  |
| INCREASE_AUTONOMY_OF_SELF_NAME | "da_increase_autonomy_of_self" |  |
| INCREASE_AUTONOMY_OF_SUBJECT_ACTION_NAME | "da_increase_autonomy_of_subject" |  |
| DECREASE_AUTONOMY_OF_SUBJECT_ACTION_NAME | "da_decrease_autonomy" |  |
| WAR_GOAL_TRANSFER_SUBJECT_TYPE | "transfer_subject" |  |
| WAR_GOAL_UNIFICATION_TYPE | "unification" |  |
| WAR_GOAL_CONTAIN_THREAT_TYPE | "contain_threat" |  |
| WAR_GOAL_INDEPENDENCE_TYPE | "independence" |  |
| WAR_GOAL_HUMILIATION_TYPE | "humiliation" |  |
| WAR_GOAL_ENFORCE_TREATY_ARTICLE_TYPE | "enforce_treaty_article" |  |
| WAR_GOAL_CONQUER_STATE_TYPE | "conquer_state" |  |
| WAR_GOAL_REVOKE_ALL_CLAIMS_TYPE | "revoke_all_claims" |  |
| WAR_GOAL_RETURN_STATE_TYPE | "return_state" |  |
| WAR_GOAL_OPEN_MARKET_TYPE | "open_market" |  |
| WAR_GOAL_FOREIGN_INVESTMENT_RIGHTS_TYPE | "foreign_investment_rights" |  |
| WAR_GOAL_JOIN_POWER_BLOC_TYPE | "join_power_bloc" |  |
| WAR_GOAL_REPARATIONS_MONTHS | 60 | # [>= 0] |
| WAR_GOAL_COLONIZATION_RIGHTS_PACT_TYPE | "colonization_rights" |  |
| WAR_GOAL_COLONIZATION_RIGHTS_MONTHS | 60 | # [>= 0] |
| WAR_GOAL_OPEN_MARKET_MONTHS | 60 | # [>= 0] |
| WAR_GOAL_HUMILIATION_PACT_TYPE | "humiliation" |  |
| WAR_GOAL_HUMILIATION_MONTHS | 60 | # [>= 0] |
| WAR_GOAL_CONTAIN_THREAT_MONTHS | 60 | # [>= 0] |
| WAR_GOAL_MAKE_PROTECTORATE_SUBJECT_TYPE | "subject_type_protectorate" |  |
| WAR_GOAL_MAKE_TRIBUTARY_SUBJECT_TYPE | "subject_type_tributary" |  |
| WAR_GOAL_MAKE_DOMINION_SUBJECT_TYPE | "subject_type_dominion" |  |
| WAR_GOAL_TREATY_PORT_BUILDING_LEVEL | 1 |  |
| WAR_GOAL_LIBERATE_COUNTRY_LIBERATOR_START_RELATIONS | 50 |  |
| WAR_GOAL_LIBERATE_COUNTRY_OPPRESSOR_START_RELATIONS | -50 |  |
| WAR_GOAL_CONTAIN_THREAT_YEARS_SINCE_CONQUEST | 10 |  |
| WAR_GOAL_REGIME_CHANGE_MONTHS | 60 | # 被强制改变政体的国家其政府将被锁定该月数 [>= 0] |
| WAR_GOAL_REGIME_CHANGE_MAX_IDEOLOGICAL_OPINION | -5 | # 若意识形态好感高于此值，则无法使用改变政体 |
| WAR_GOAL_REGIME_CHANGE_MIN_LAW_PROGRESSIVENESS_DIFFERENCE | 50 | # 若战争目标持有者在某一法律组中的法律差异未达到此值，则不将其作为改变政体的一部分进行更改 |
| WAR_GOAL_INCREASE_AUTONOMY_MIN_LIBERTY_DESIRE | 75 | # 附属国必须拥有至少此数值的独立倾向才能使用提升自治权战争目标 |
| WAR_GOAL_INDEPENDENCE_MIN_LIBERTY_DESIRE | 90 | # 附属国必须拥有至少此数值的独立倾向才能使用独立战争目标 |
| WAR_GOAL_INFAMY_POPULATION_SCALING_FACTOR | 10000 | # 下方系数所乘的人口数量 |
| WAR_GOAL_INFAMY_POPULATION_SCALING_MULTIPLIER | 0.03 | # 国家/州每拥有 WAR_GOAL_INFAMY_POPULATION_SCALING_FACTOR 人口，恶名便乘以此系数 |
| WAR_GOAL_INFAMY_POPULATION_SCALING_MULTIPLIER_MAX_PER_STATE | 5 | # 每个受影响的州的恶名人口乘数不能高于此值 |
| WAR_GOAL_INFAMY_POPULATION_SCALING_MULTIPLIER_MAX_TOTAL | 50 | # 无论受影响的州数量多少，恶名人口乘数均不能高于此值 |
| WAR_GOAL_INFAMY_HOMELAND_FACTOR | -0.25 | # 若夺取/使其成为傀儡国等的州是侵略者的本土，恶名按此值调整 |
| WAR_GOAL_INFAMY_UNINCORPORATED_FACTOR | -0.5 | # 若夺取/使其成为傀儡国等的州是未合并州，恶名按此值调整 |
| WAR_GOAL_INFAMY_REBELLING_SUBJECT_MULT | 0.25 | # 针对叛乱附属国的战争目标，恶名乘以此系数 |
| WAR_GOAL_INFAMY_LOW_LIBERTY_DESIRE_SUBJECT_MULT | 0.25 | # 针对独立倾向低于 WAR_GOAL_INFAMY_LOW_LIBERTY_DESIRE_THRESHOLD 的附属国的战争目标，恶名乘以此系数 |
| WAR_GOAL_INFAMY_LOW_LIBERTY_DESIRE_THRESHOLD | 25 | # WAR_GOAL_INFAMY_LOW_LIBERTY_DESIRE_SUBJECT_MULT 的阈值 |
| WAR_GOAL_INFAMY_RELATIONS_TARGET_IMPACT | -1 | # 事件产生的每一点恶名也会对与目标国家的关系产生此影响 |
| WAR_GOAL_INFAMY_RELATIONS_INTEREST_IMPACT | -0.5 | # 事件产生的每一点恶名也会对与对目标国家持有利益的国家的关系产生此影响 |
| WAR_GOAL_INFAMY_CONQUER_STATE | 5.0 |  |
| WAR_GOAL_INFAMY_RETURN_STATE | 2.0 |  |
| WAR_GOAL_INFAMY_MAKE_PROTECTORATE | 2.0 |  |
| WAR_GOAL_INFAMY_MAKE_TRIBUTARY | 2.0 |  |
| WAR_GOAL_INFAMY_MAKE_DOMINION | 2.0 |  |
| WAR_GOAL_INFAMY_REDUCE_AUTONOMY | 2.0 |  |
| WAR_GOAL_INFAMY_TRANSFER_SUBJECT | 2.0 |  |
| WAR_GOAL_INFAMY_ANNEX_COUNTRY | 5.0 |  |
| WAR_GOAL_INFAMY_REGIME_CHANGE | 0.5 |  |
| WAR_GOAL_INFAMY_FORCE_NATIONALIZATION | 5.0 |  |
| WAR_GOAL_INFAMY_DIPLO_PLAY_BACK_DOWN_REFUND | -0.75 | # 在外交博弈中因一方退让而被放弃的战争目标所返还的恶名（适用于发起方/目标方） |
| WAR_GOAL_INFAMY_DIPLO_PLAY_BACKER_REFUND | -1.00 | # 在外交博弈中因博弈未升级为战争或支持者倒戈而为其支持者放弃的战争目标所返还的恶名 |
| WAR_GOAL_INFAMY_PEACE_REFUND | -0.5 | # 因国家投降或未强制执行其战争目标即进行和谈而被放弃的战争目标所返还的恶名 |
| WAR_GOAL_INFAMY_REDUCTION_FOR_TARGET | -0.5 | # 当战争目标被强制加于目标方时，从目标方扣除的该战争目标恶名值 |
| WAR_OUTCOME_MIN_WARGOAL_IMPACT | 10 | # 计算战争结果时战争目标的最低影响值 |
| WAR_OUTCOME_VICTORY_RATIO | 2.0 | # 低于此强制执行战争目标影响之比时，胜利被视为有限胜利。若比值高于此但双方都强制执行了战争目标，则算作胜利。若一方强制执行了全部战争目标而另一方一个都没有执行，则为全面胜利。 |
| WAR_OUTCOME_VICTORY_MIN_ENFORCEMENT_RATIO | 0.5 | # 一方必须强制执行至少这一比例的战争目标总影响值才能算作胜利，否则为有限胜利 |
| DIPLOMATIC_PLAY_ABANDON_SUPPORT_RELATIONS_IMPACT | 50 |  |
| DIPLOMATIC_PLAY_ESCALATION_DAILY | 1 |  |
| DIPLOMATIC_PLAY_ESCALATION_PAUSE_FROM_ACTION | 5 | # 任一方采取行动时紧张度暂停的天数 |
| DIPLOMATIC_PLAY_ESCALATION_PAUSE_MAX | 20 | # 无论同时采取多少行动，紧张度暂停都不能超过此值 |
| DIPLOMATIC_PLAY_OPENING_PHASE_END | 21 | # 在此之前，防御方需设定其战争目标，且不能加入/拉拢 |
| DIPLOMATIC_PLAY_CLOSING_PHASE_START | 80 | # 在此之后，无法再加入/拉拢更多国家 |
| DIPLOMATIC_PLAY_ESCALATION_WAR_BREAKOUT | 100 |  |
| COLONY_PROVINCE_BASE_SCORE | 10 |  |
| COLONY_PROVINCE_COASTAL_SCORE | 60 | # 对拥有海岸线的省份，替代 COLONY_BASE_SCORE |
| COLONY_PROVINCE_ADJACENCY_SCORE | 25 | # 殖民地扩张时对与现有省份相邻的优先程度 |
| COLONY_PROVINCE_NO_ADJACENCY_MULT | 0.1 | # 若完全没有相邻时乘以此系数 |
| COLONY_PROVINCE_RANDOM_FACTOR | 1.5 | # 此值越高，殖民省份的选取越随机 |
| BASE_WAR_SUPPORT | 100 |  |
| MAX_WAR_SUPPORT | 100 |  |
| MIN_WAR_SUPPORT | -100 |  |
| # 所有由代码而非脚本调用的外交催化剂的定义 # 若这些内容被修改，也需要在数据库中进行相应修改，反之亦然 |  |  |
| DIPLOMATIC_CATALYST_TYPE_HISTORICAL_RELATIONS | "catalyst_historical_relationship" |  |
| DIPLOMATIC_CATALYST_TYPE_BECAME_RELEVANT | "catalyst_became_relevant" |  |
| DIPLOMATIC_CATALYST_TYPE_BECAME_IRRELEVANT | "catalyst_became_irrelevant" |  |
| DIPLOMATIC_CATALYST_TYPE_GAINED_LAND_BORDER | "catalyst_gained_land_border" |  |
| DIPLOMATIC_CATALYST_TYPE_LOST_LAND_BORDER | "catalyst_lost_land_border" |  |
| DIPLOMATIC_CATALYST_TYPE_MARKET_OPENED | "catalyst_market_opened" |  |
| DIPLOMATIC_CATALYST_TYPE_RELATIONS_INCREASED | "catalyst_relations_level_increased" |  |
| DIPLOMATIC_CATALYST_TYPE_RELATIONS_DECREASED | "catalyst_relations_level_decreased" |  |
| DIPLOMATIC_CATALYST_TYPE_DIPLOMATIC_DEMAND | "catalyst_diplomatic_demand" |  |
| DIPLOMATIC_CATALYST_TYPE_DIPLOMATIC_DEMAND_TARGET | "catalyst_diplomatic_demand_target" |  |
| DIPLOMATIC_CATALYST_TYPE_DIPLOMATIC_PLAY | "catalyst_diplomatic_play" |  |
| DIPLOMATIC_CATALYST_TYPE_DIPLOMATIC_PLAY_TARGET | "catalyst_diplomatic_play_target" |  |
| DIPLOMATIC_CATALYST_TYPE_AUTONOMY_INCREASED | "catalyst_autonomy_level_increased" |  |
| DIPLOMATIC_CATALYST_TYPE_AUTONOMY_DECREASED | "catalyst_autonomy_level_decreased" |  |
| DIPLOMATIC_CATALYST_TYPE_GAINED_INDEPENDENCE | "catalyst_gained_independence" |  |
| DIPLOMATIC_CATALYST_TYPE_BECAME_SUBJECT | "catalyst_became_subject" |  |
| DIPLOMATIC_CATALYST_TYPE_DIPLOMATIC_INCIDENT | "catalyst_diplomatic_incident" |  |
| DIPLOMATIC_CATALYST_TYPE_PACT_FORMED | "catalyst_pact_formed" |  |
| DIPLOMATIC_CATALYST_TYPE_PACT_BROKEN | "catalyst_pact_broken" |  |
| DIPLOMATIC_CATALYST_TYPE_ALLIANCE_FORMED | "catalyst_alliance_formed" |  |
| DIPLOMATIC_CATALYST_TYPE_ALLIANCE_BROKEN | "catalyst_alliance_broken" |  |
| DIPLOMATIC_CATALYST_TYPE_ALLIANCE_FORMED_WITH_RIVAL | "catalyst_alliance_with_rival" |  |
| DIPLOMATIC_CATALYST_TYPE_RIVAL_OF_RIVAL | "catalyst_rival_of_rival" |  |
| DIPLOMATIC_CATALYST_TYPE_INCREASED_RELATIONS_WITH_RIVAL | "catalyst_increased_relations_with_rival" |  |
| DIPLOMATIC_CATALYST_TYPE_DECREASED_RELATIONS_WITH_RIVAL | "catalyst_decreased_relations_with_rival" |  |
| DIPLOMATIC_CATALYST_TYPE_OPPOSED_IN_PLAY | "catalyst_opposed_in_play" |  |
| DIPLOMATIC_CATALYST_TYPE_ALLIES_IN_PLAY | "catalyst_allies_in_play" |  |
| DIPLOMATIC_CATALYST_TYPE_WARGOAL_ENFORCED | "catalyst_wargoal_enforced" |  |
| DIPLOMATIC_CATALYST_TYPE_STATE_CONQUERED | "catalyst_state_conquered" |  |
| DIPLOMATIC_CATALYST_TYPE_DIPLOMATIC_STRATEGY_CHANGED | "catalyst_diplomatic_strategy_changed" |  |
| DIPLOMATIC_CATALYST_TYPE_DECLARED_BANKRUPTCY | "catalyst_declared_bankruptcy" |  |
| DIPLOMATIC_CATALYST_TYPE_IDEOLOGICAL_DRIFT | "catalyst_ideological_drift" |  |
| DIPLOMATIC_CATALYST_TYPE_IDEOLOGICAL_ALIGNMENT | "catalyst_ideological_alignment" |  |
| DIPLOMATIC_CATALYST_TYPE_JOINED_SAME_BLOC | "catalyst_joined_same_bloc" |  |
| DIPLOMATIC_CATALYST_TYPE_JOINED_DIFFERENT_BLOC | "catalyst_joined_different_bloc" |  |
| DIPLOMATIC_CATALYST_TYPE_LEFT_POWER_BLOC | "catalyst_left_power_bloc" |  |
| DIPLOMATIC_CATALYST_TYPE_KICKED_OUT_OF_BLOC | "catalyst_kicked_out_of_bloc" |  |
| DIPLOMATIC_CATALYST_TYPE_JOURNAL_ENTRY | "catalyst_journal_entry" |  |
| DIPLOMATIC_CATALYST_TYPE_UNIFICATION_SUPPORT_ADDED | "catalyst_unification_support_added" |  |
| DIPLOMATIC_CATALYST_TYPE_UNIFICATION_SUPPORT_REMOVED | "catalyst_unification_support_removed" |  |
| DIPLOMATIC_CATALYST_TYPE_FRIENDLY_LOBBY_IN_GOVERNMENT | "catalyst_friendly_lobby_in_government" |  |
| DIPLOMATIC_CATALYST_TYPE_HOSTILE_LOBBY_IN_GOVERNMENT | "catalyst_hostile_lobby_in_government" |  |
| DIPLOMATIC_CATALYST_TYPE_NATIONALIZED_BUILDING | "catalyst_nationalized_building" |  |
| DIPLOMATIC_CATALYST_TYPE_OVERTAKEN_IN_PRESTIGE_RANK | "catalyst_overtaken_in_prestige_rank" |  |
| DIPLOMATIC_CATALYST_TYPE_REVOLUTION_SUCCESSFUL | "catalyst_revolution_successful" |  |
| DIPLOMATIC_CATALYST_TYPE_BECAME_RECOGNIZED | "catalyst_became_recognized" |  |
| DIPLOMATIC_CATALYST_TYPE_STRAIT_TOLL_HIGH = "catalyst_strait_toll_high" |  |  |
| DIPLOMATIC_CATALYST_TYPE_STRAIT_TOLL_REDUCED = "catalyst_strait_toll_reduced" |  |  |
| DIPLOMATIC_CATALYST_TYPE_STRAIT_NO_MILITARY = "catalyst_strait_no_military" |  |  |
| DIPLOMATIC_CATALYST_TYPE_STRAIT_CLOSED = "catalyst_strait_closed" |  |  |
| DIPLOMATIC_CATALYST_TYPE_STRAIT_OPENED = "catalyst_strait_opened" |  |  |
| DIPLOMATIC_CATALYST_TYPE_STRAIT_PARTIALLY_OPENED = "catalyst_strait_partially_opened" |  |  |
| DIPLOMATIC_CATALYST_MIN_SCORE_POSITION_FOR_OVERTAKE | 10 | # 如果国家的威望/排名分数位次不低于此值，才对其应用“排名被超越”类催化剂 |
| DIPLOMATIC_CATALYST_MIN_CHANGE_FOR_IDEOLOGICAL_DRIFT | -10 | # 上届政府与新政府之间的意识形态分数变化必须至少达到此值，才会产生意识形态漂移催化剂 |
| DIPLOMATIC_CATALYST_MIN_CHANGE_FOR_IDEOLOGICAL_ALIGNMENT | 10 | # 意识形态分数变化（前一届政府与新政府之间）必须至少达到此值才会产生意识形态结盟催化剂 |
| TOP_PRESTIGE_RANK_BONUS_THRESHOLD | 10 | # 开始应用 prestige_ranking_top 静态 modifier 的威望排名阈值 |
| TOP_PRESTIGE_RANK_BONUS_SCALE | 1.0 | # 威望排名第 1 时，prestige_ranking_top modifier 以（1 + 此乘数）的倍率应用，并随排名下降在阈值处缩放至 1 倍 |
| COUNTRY_TIER_CITY_STATE_PRESTIGE | 0 |  |
| COUNTRY_TIER_PRINCIPALITY_PRESTIGE | 5 |  |
| COUNTRY_TIER_GRAND_PRINCIPALITY_PRESTIGE | 10 |  |
| COUNTRY_TIER_KINGDOM_PRESTIGE | 15 |  |
| COUNTRY_TIER_EMPIRE_PRESTIGE | 25 |  |
| COUNTRY_TIER_HEGEMONY_PRESTIGE | 50 |  |
| PRESTIGE_FROM_COUNTRY_GDP_DIVISOR | 1000000 |  |
| PRESTIGE_FROM_COUNTRY_GDP | 3 | # 每 PRESTIGE_FROM_COUNTRY_GDP_DIVISOR 的 GDP |
| PRESTIGE_FROM_SUBJECT_GDP | 1.5 | # 附属国每 PRESTIGE_FROM_COUNTRY_GDP_DIVISOR 的 GDP |
| PRESTIGE_FROM_ARMY_POWER_PROJECTION | 0.03 | # 陆军战斗力每点力量投射 |
| PRESTIGE_FROM_NAVY_POWER_PROJECTION | 0.006 | # 海军战斗力每点力量投射 |
| PRESTIGE_FROM_SUBJECT_ARMY_POWER_PROJECTION | 0.0005 | # 附属国陆军战斗力每点力量投射 |
| PRESTIGE_FROM_SUBJECT_NAVY_POWER_PROJECTION | 0.01 | # 附属国海军战斗力每点力量投射 |
| PRESTIGE_FROM_PRESTIGE_GOODS_PRODUCTION | 3 | # 商品排行榜通常威望的乘数 |
| PRESTIGE_MIN_NUM_COUNTRIES | 100 | # 如果游戏中使用威望的国家数量少于该值，则会添加一些填充国家来调整平均威望水平 |
| FILLER_COUNTRY_PRESTIGE | 15 |  |
| DAYS_TO_LOSE_POWER_RANK | 365 |  |
| POWER_RANK_LOSS_THRESHOLD | 0.9 |  |
| ARMY_POWER_PROJECTION_MODIFIER_MAX_SCALING | 1000 | # 陆军力量投射超过此数值后，country_army_power_projection 静态 modifier 不再提供额外收益 |
| NAVY_POWER_PROJECTION_MODIFIER_MAX_SCALING | 1000 | # 陆军力量投射超过此数值后，country_navy_power_projection 静态 modifier 不再提供额外收益 |
| DEFAULT_STATES_REQUIRED_TO_RELEASE_COUNTRY | 0 | # 若 country_creation 中未指定，则应用此值 |
| DEFAULT_STATES_REQUIRED_TO_FORM_COUNTRY | 0.75 | # 若 country_formation 中未指定，则应用此值 |
| RELEASE_COUNTRY_AS_SUBJECT_RELATIONS_BOOST | 30 |  |
| RELEASE_COUNTRY_AS_INDEPENDENT_RELATIONS_BOOST | 50 |  |
| INTEREST_NUM_DAYS_CHANGE | 30 | INTEREST_MAX_INVOLVEMENT \|\| 10000 \|\| # 利益层级介入度分数的上限 |
| INTEREST_GROWTH_RATIO | 0.02 | # 每周，利益的当前介入度值按其当前介入度与目标介入度之差的该比例增长 |
| INTEREST_MIN_GROWTH | 10 | # 每周，利益的当前介入度值至少增长此数值 |
| INTEREST_DECAY_SPEED | 20 | # 每周，利益的当前介入度值衰减此数值 |
| INTEREST_CAPITAL_TARGET_INVOLVEMENT | 2500 | # 首都位于某战略区域时的目标介入度分数 |
| INTEREST_CAPITAL_NEIGHBOR_TARGET_INVOLVEMENT | 1500 | # 首都位于相邻战略区域时的目标介入度分数 |
| INTEREST_STATE_OR_CLAIM_TARGET_INVOLVEMENT | 7500 | # 拥有州或主张地区性时的目标介入度分数 |
| INTEREST_STATE_OR_CLAIM_MIN_TARGET_INVOLVEMENT | 1500 | # 在某区域拥有任何所有权或主张时保证的最低目标介入度 |
| INTEREST_CLAIM_LOCALITY_WEIGHT | 0.20 | # 每项主张贡献此数值的地区性权重（相当于拥有整个州区域的该比例） |
| INTEREST_GDP_TARGET_INVOLVEMENT | 2500 | # 某地区 GDP 份额换算为目标介入度（involvement）的乘数 |
| INTEREST_ARMY_TARGET_INVOLVEMENT | 0.33 | # 一个驻在国家的陆军进攻与防御总值有多少比例转换为目标介入度 |
| INTEREST_NAVY_TARGET_INVOLVEMENT | 0.33 | # 一个驻在国家的海军力量投射有多少比例转换为目标介入度 |
| INTEREST_NAVY_MISSION_MULTI_REGION_BONUS | 0.75 | # 海军任务覆盖的每个战略区域为舰队介入度生成提供的加成 |
| INTEREST_MIN_INVOLVEMENT_RATIO | 0.1 | # 每种条目类型或外交条约下，条目与条约最大介入度的最低比率 |
| REGION_LOCALITY_SHARE_THRESHOLD | 0.25 | # 如果你拥有某地区属地（locality）的至少这一份额，你即可获得该地区的本地利益 |
| REGION_LOCALITY_COUNTRY_INCORPORATED_SHARE_THRESHOLD | 0.25 # 如果你的已整合州中至少有这一份额位于某地区，你即可获得该地区的本地利益 |  |
| INTEREST_TIER_MIN_RELEVANT_RANK | 2 | # 利益层级（interest tier）被视为“相关”的最低等级 |
| INTEREST_TIER_MIN_VIOLATE_SOVEREIGNTY_RANK | 2 | # 国家成为“侵犯主权”（加入防御方并收到事件）的“利益相关方”所需的最低利益层级。设为 2 表示“介入”，3 表示“有影响力”； |
| INTEREST_ARMY_INVOLVEMENT_CAP | 5000 | # 陆军力量提供的介入度上限 |
| INTEREST_NAVY_INVOLVEMENT_CAP | 5000 | # 海军力量提供的介入度上限 |
| INTEREST_TREATY_PACT_INVOLVEMENT_CAP | 5000 | # 条约与盟约提供的介入度上限 |
| INTEREST_POWER_BLOC_MEMBER_TARGET_INVOLVEMENT | 2500 | # 每个非附属国强权集团成员为领袖生成的介入度 |
| INTEREST_TIER_REDUCTION_GRACE_PERIOD_DAYS | 30 | # 当一个国家提升其利益层级后，需经过这么多天该层级才能被降低 |
| STRAIT_MIN_INTEREST_TIER_FOR_CATALYST | 1 | # 海峡关闭转为军事通行问题时，国家获得催化剂所需的最低利益层级 |
| REGION_LOCALITY_STATES_WEIGHT | 1 | # 计算地区属地（locality）时，你在该地区拥有的州的比例的权重 |
| REGION_LOCALITY_POPULATION_WEIGHT | 1.25 | # 计算地区属地时，你在该地区拥有的人口的比例的权重 |
| RELATION_PENALTY_OVERLORD_KICK_BACKER_SUBJECT | -30 | # 当宗主国加入外交博弈时，若其附属国支持另一方，宗主国会强制该附属国转为中立；此为该情况发生时附属国与宗主国之间的关系惩罚 |
| ECONOMIC_DEPENDENCE_MIN | 0 |  |
| ECONOMIC_DEPENDENCE_MAX | 5 |  |
| ECONOMIC_DEPENDENCE_GDP_RATIO_BY_OTHER_FACTOR | 5 | # 例如：若你拥有另一国 15% 的 GDP，则换算为 +0.75 |
| ECONOMIC_DEPENDENCE_GDP_RATIO_BY_OTHER_MIN | 0 |  |
| ECONOMIC_DEPENDENCE_GDP_RATIO_BY_OTHER_MAX | 5 |  |
| ECONOMIC_DEPENDENCE_OTHER_GDP_RATIO_OWNED_FACTOR | 20 | # 若你的附属国反过来拥有你的产业，这比相反情况更难堪 |
| ECONOMIC_DEPENDENCE_OTHER_GDP_RATIO_OWNED_MIN | -5 | #此值为负 |
| ECONOMIC_DEPENDENCE_OTHER_GDP_RATIO_OWNED_MAX | 0 |  |
| ECONOMIC_DEPENDENCE_GDP_PERCENTAGE_FACTOR | 1 |  |
| ECONOMIC_DEPENDENCE_GDP_PERCENTAGE_MIN | 0 |  |
| ECONOMIC_DEPENDENCE_GDP_PERCENTAGE_MAX | 1 |  |
| ECONOMIC_DEPENDENCE_POP_GOODS_DEPENDENCE_ON_OTHER_FACTOR | 3 | # 另一国供应的商品总英镑价值与其 GDP 之比乘以此系数（即每 25% 的倍数产生 +0.75 经济依赖度） |
| ECONOMIC_DEPENDENCE_POP_GOODS_DEPENDENCE_ON_OTHER_MIN | 0 | # 最好情况下，一国对另一国的人口商品依赖度可低至 0 |
| ECONOMIC_DEPENDENCE_POP_GOODS_DEPENDENCE_ON_OTHER_MAX | 2 | # 最坏情况下，一国对另一国的人口商品依赖度可达 +2 |
| ECONOMIC_DEPENDENCE_OTHER_POP_GOODS_DEPENDENCE_FACTOR | 3 | # 该国供应另一国商品的总英镑价值相对于其 GDP 的百分比将乘以此系数 |
| ECONOMIC_DEPENDENCE_OTHER_POP_GOODS_DEPENDENCE_MIN | -2 | # 另一国对该国的人口商品依赖度最多可带来 -2 ED |
| ECONOMIC_DEPENDENCE_OTHER_POP_GOODS_DEPENDENCE_MAX | 0 | # 另一国对该国的人口商品依赖度最少可带来 0 ED |
| ECONOMIC_DEPENDENCE_TRADE_ROUTE_DEPENDENCE_FACTOR | 3 | # 当国家间贸易额占 GDP 的 100% 时所应用的系数 |
| ECONOMIC_DEPENDENCE_TRADE_ROUTE_DEPENDENCE_MIN | 0 |  |
| ECONOMIC_DEPENDENCE_TRADE_ROUTE_DEPENDENCE_MAX | 3 |  |
| RELATIONS_CHANGE_INVESTORS_MONOPOLY_CREATED | -10 | # 当一国建立垄断时，与拥有投资权的国家之间的关系变化 |
| # 条约签署地点的选择分两步进行 # 1. 从最多 6 个州中随机选择一个州，这 6 个州为： # - 首都（1 个） # - GDP 最高的州（1 个） # - GDP 第二高的州（0 或 1 个） # - 双方条约参与者各计上述州 # - 单州国家没有 GDP 第二高的州 # 2. 一旦随机选定一个州，再从该州所属的 # 州区域中随机选择一个枢纽（如适用，例如内陆 # 州区域没有港口） # 每次随机选择均按以下权重进行加权 |  |  |
| TREATY_SIGNING_STATE_WEIGHT_CAPITAL | 1 | # 随机选择条约签署地点时首都所在的州所拥有的权重 [>= 1] |
| TREATY_SIGNING_STATE_WEIGHT_HIGHEST_GDP | 1 | # 同上，适用于 GDP 最高的州 [>=1] |
| TREATY_SIGNING_STATE_WEIGHT_SECOND_HIGHEST_GDP | 1 | # 同上，适用于 GDP 第二高的州 [>=1] |
| TREATY_SIGNING_HUB_WEIGHT_CITY | 5 | # 随机选择条约签署地点时城市枢纽所拥有的权重 [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_PORT | 3 | # 同上，适用于港口枢纽 [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_FARM | 2 | # 同上，适用于农场枢纽 [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_MINE | 1 | # 同上，适用于矿山枢纽 [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_WOOD | 1 | # 同上，适用于木材枢纽 [>= 1] |
| MAX_TREATY_OBLIGATIONS_DELAY_DAYS | 3650 | # 作为条约一部分而承诺的义务将在约束期结束时生效，或在条约最初签署后经过该天数后生效，以先到者为准 [>= 0] |
| BINDING_PERIOD_THRESHOLD_TO_EFFECTUATE_TREATY_OBLIGATIONS_DAYS | 30 | # 当约束期剩余天数不多于此天数时，义务将生效 |
| TREATY_ARTICLE_MONEY_TRANSFER_ARTICLE_TYPE | "money_transfer" |  |
| TREATY_ARTICLE_TREATY_PORT_ARTICLE_TYPE | "treaty_port" |  |
| TREATY_ARTICLE_INVESTMENT_RIGHTS_ARTICLE_TYPE | "foreign_investment_rights" |  |
| TREATY_ARTICLE_LAW_COMMITMENT_ARTICLE_TYPE | "law_commitment" |  |
| DEFAULT_WAR_REPARATIONS_MONEY_TRANSFER | 0.1 |  |
| TREATY_PROPOSAL_COOLDOWN_DAYS | 7 | # 条约提案被拒绝后，需等待此天数才能再次提交另一份条约提案 |
| TREATY_DEFAULT_BINDING_DURATION_YEARS | 5 |  |
| TREATY_THREATEN_HOSTILITIES_DURATION_DAYS | 365 |  |
| THREATEN_NAVAL_HOSTILITIES_COOLDOWN_DAYS | 1825 | # 需过 5 年才能再次对同一国家威胁发动海上敌对行动 |
| NAVAL_HOSTILITIES_POINTS_MAX | 100 | # 单次海上敌对行动可造成的最大伤害点数 |
| NAVAL_VULNERABILITY_MAX | 1.0 | # 最大海上脆弱性评分。用于判定一国对海上敌对行动的忌惮程度。 |
| NAVAL_VULNERABILITY_TRADE_MULTIPLIER | 0.75 | # 来自贸易的脆弱性：该值 * (贸易基础成本 / GDP) = 脆弱性点数 |
| NAVAL_VULNERABILITY_COASTAL_GDP_MULTIPLIER | 0.5 | # 来自沿海 GDP 的脆弱性：该值 * (沿海 GDP / GDP) = 脆弱性点数 |
| NAVAL_VULNERABILITY_PRESTIGE_MULTIPLIER | 1.0 | # 来自海军威望的脆弱度：此值 * (海军威望 / 总威望) = 脆弱度点数 |
| NAVAL_HOSTILITIES_POINTS_SHIPS_SUNK_AT_FULL_FLEET | 500 | # 当一国舰队的建造费用 100% 被击沉时 awarded 的损伤点数 |
| NAVAL_HOSTILITIES_POINTS_BLOCKADE_GDP_WEEKLY | 20 | # 当一国 100% 的 GDP 被封锁时，每周的损伤点数 |
| NAVAL_HOSTILITIES_POINTS_PIRACY_GDP_WEEKLY | 20 | # 当一国 100% 的 GDP 的商品被海盗掠夺时，每周的损伤点数 |
| NAVAL_HOSTILITIES_POINTS_BOMBARDMENT_DEVASTATION | 20 | # 每单位荒芜度增加的损伤点数，按州 GDP / 受害国 GDP 缩放 |
| NAVAL_HOSTILITIES_POINTS_BOMBARDMENT_BUILDING_DESTROYED | 10 | # 每被炮击摧毁一级建筑的固定损伤点数 |
| PAST_TEMPORARY_HOSTILITIES_KEEP_YEARS | 20 | # 临时敌对数据过期后保留的年数 |
| PIRACY_DAMAGE_TRACKING_WEEKS | 26 | # 用于取平均值而保留的海盗伤害历史周数 |

### 强权集团（PowerBlocs）

| Define | 默认值 | 开发者注释 |
|---|---|---|
| MAX_PRINCIPLES | 4 | # 一个强权集团最多可拥有的信条数量 |
| INITIAL_PRINCIPLE_LEVELS | 1 | # 一个强权集团在组建期间最多可拥有的信条总等级 |
| FORMATION_COOLDOWN_MONTHS | 24 | # 两次尝试组建强权集团之间的冷却月数 |
| JOIN_COOLDOWN_MONTHS | 6 | # 如果一个国家离开强权集团，则在此月数内无法重新加入 |
| LEAVE_COOLDOWN_MONTHS | 6 | # 如果一个国家加入强权集团，则在此月数内无法离开 |
| MIN_MEMBERS | 2 | # 这是强权集团被视为活跃状态所需的最低成员数量。成员包括领袖。 |
| LEVERAGE_LOBBY_CLOUT_FACTOR | 500 | # 影响力集团（Lobby）的总政治力量 * 此值会增减筹码的获取 |
| INVITE_ACTION_NAME | "invite_to_power_bloc" |  |
| JOIN_ACTION_NAME | "join_power_bloc" |  |
| MAX_MANDATE_PROGRESS | 2000 | # 当委任进度达到此值时，强权集团获得一项委任 |
| MAX_MANDATES | 3 | # 这是一次可累积的最大委任数量 |
| PRINCIPLE_SELECTION_COOLDOWN_DAYS | 90 | # 一旦选定某项信条，在此天数内无法更改。升级不受冷却影响，但会重置冷却。 |
| POWER_STRUGGLE_PRESTIGE_THRESHOLD_START | 1.2 | # 如果强权集团某成员的威望超过领袖威望乘以此值——权力斗争开始，该成员成为竞争者 |
| POWER_STRUGGLE_PRESTIGE_THRESHOLD_FAIL | 1.15 | # 如果竞争者的威望低于领袖威望乘以此值——权力斗争失败 |
| POWER_STRUGGLE_DURATION_SUCCESS_MONTHS | 12 | # 权力斗争在此月数后成功 |
| POWER_STRUGGLE_DURATION_FACTOR_FOR_FOUNDER | 0.75 | # 如果竞争者是强权集团的创立者，权力斗争在此值 * POWER_STRUGGLE_DURATION_SUCCESS_MONTHS 后成功 |
| COHESION_WEEKLY_DRIFT_MAX | 1 | # 凝聚力每周最多漂移 +/- 此值 |
| COHESION_TARGET_MAX | 100 | # 凝聚力可达到的最高值 |
| POWER_BLOC_INFLUENCE_COST | 500 | # 组建/成为强权集团领袖所需的影响力消耗 |
| MAX_LEVERAGE | 1000 | # 可在各参与方（国家自身 + 每个强权集团）之间分配的“原始”筹码总量 |
| LEVERAGE_WEEKLY_DRIFT_FACTOR | 0.02 | # 当前筹码与目标筹码的差值将乘以此值，以确定每周的筹码漂移 |
| LEVERAGE_WEEKLY_DRIFT_MIN | 1 | # 筹码每周至少漂移 +/- 此值，直至目标值 |
| COUNTRY_POPULATION_LEVERAGE_RESISTANCE_MODIFIER_DIVISOR | 1000000 | # 人口除以此值后乘以 country_leverage_resistance_per_population，得出每百万人口提供的筹码抗性数量 |
| COUNTRY_POPULATION_LEVERAGE_RESISTANCE_MODIFIER_MAX_MULTIPLIER | 100 | # 人口提供的最大乘数。按上文的数值为 1 000 000 计算，这意味着影响力的抵抗上限为 100 000 000。 |

### 人口（Pops）

| Define | 默认值 | 开发者注释 |
|---|---|---|
| NUM_WEALTH_LEVELS | 99 |  |
| POP_WEIGHT_MODIFIER_MAX_SCALE | 100 | # 应用于人口画像上权重 modifier 的最大缩放值 |
| DEFAULT_POP_TYPE | "laborers" | # 使用场景：create_pop effect；迁移；受伤军人离开驻地；奴隶的默认职业等 |
| SLAVE_POP_TYPE | "slaves" | # 债务人将成为的人口类型 |
| ACADEMICS_POP_TYPE | "academics" | # 学者人口 |
| OFFICERS_POP_TYPE | "officers" | # 被视为军官的人口类型 |
| SERVICEMEN_POP_TYPE | "soldiers" | # 被视为军士的人口类型 |
| POP_SIZE_PACKAGE | 10000 | # “标准”人口规模，在计算诸如需购买的需求、需支付的工资等时用作人口数的除数 |
| WEALTH_PROGRESS_WANTED_BUFFER | 1.02 | # 人口至少要有这么多倍于下一等级购买组合成本的收入，才会想要提升其财富 |
| WEALTH_PROGRESS_ACCEPTABLE_DEFICIT | 0.98 | # 只要人口还能负担得起当前购买组合成本的这么多比例，就不会改变财富等级 |
| WEALTH_PROGRESS_INCREASE | 0.2 | # 当人口负担得起更高等级的购买组合时财富增长的速度。该系数会随收入与成本之间差距的大小而调整 |
| WEALTH_PROGRESS_DECREASE | 0.1 | # 当人口不再能负担其购买组合时财富下降的速度。该系数会随收入与成本之间差距的大小而调整 |
| WEALTH_PROGRESS_DECREASE_DEFICIT_MULT | 5 |  |
| LOYALTIES_GAIN_GRACE_PERIOD_SHORT | "1837.1.1" | # 在此日期之前，若应用“短”游戏规则，只有因生活水平变化而产生的一部分（按比例缩放）激进派和忠诚派会被实际计入 |
| LOYALTIES_GAIN_GRACE_PERIOD_LONG | "1841.1.1" | # 在此日期之前，若应用“长”游戏规则，只有因生活水平变化而产生的一部分（按比例缩放）激进派和忠诚派会被实际计入 |
| LOYALTIES_GAIN_GRACE_PERIOD_EXTRA_LONG | "1846.1.1" | # 在此日期之前，若应用“超长”游戏规则，只有因生活水平变化而产生的一部分（按比例缩放）激进派和忠诚派会被实际计入 |
| RADICALS_MAX_FROM_LOW_SOL | 0.15 | # 如果人口中激进派比例已达到此百分比，则不再因低生活水平而增加激进派（随实际生活水平与预期最低生活水平的差值缩放） |
| RADICALS_MAX_FROM_DISCRIMINATION | 0.5 | # 如果人口中激进派比例已达到此百分比，则不再因受歧视而增加激进派（随识字率缩放） |
| # 激进派月度值表示饥荒期间人口每月转化为激进派的比例 # 激进派上限表示在激进派达到该最大比例后不再因饥荒新增激进派 # 激进派增长/上限会随粮食安全度下降而在这些数值之间上升 |  |  |
| RADICALS_MONTHLY_FROM_STARVATION_BASE | 0.002 | # 粮食安全度 = 轻度阈值 |
| RADICALS_MONTHLY_FROM_STARVATION_MILD | 0.008 | # 粮食安全度 = 严重阈值 |
| RADICALS_MONTHLY_FROM_STARVATION_SEVERE | 0.02 | # 粮食安全度 = 0 |
| RADICALS_MAX_FROM_STARVATION_BASE | 0.15 | # 粮食安全度 = 轻度阈值 |
| RADICALS_MAX_FROM_STARVATION_MILD | 0.5 | # 粮食安全度 = 严重阈值 |
| RADICALS_MAX_FROM_STARVATION_SEVERE | 0.75 | # 粮食安全度 = 0 |
| ALLOW_ASSIMILATION_IN_HOMELANDS | no | # 居住在自己家园的人口能否被同化？ |
| ALLOW_ASSIMILATION_REQUIRE_HERITAGE_GROUP | no | # 人口能否被同化为不同传承群组的人口（较弱条件） |
| ALLOW_ASSIMILATION_REQUIRE_HERITAGE_TRAIT | no | # 人口能否被同化为不同传承特质的人口（较强条件） |
|# 若两者均被允许，遗产（heritage）特质要求优先 |  |  |
| ASSIMILATION_RATE | 0.002 | # 每月将发生同化（融入不同文化）的人口百分比（若符合条件） |
| MIN_ASSIMILATION | 1 | # 若存在任何同化，至少会有这么多人口发生同化 |
| ASSIMILATION_IN_HOMELAND_MULT | 0.75 | # 在本土（homeland）中同化速率乘以该系数 |
| CONVERSION_RATE | 0.002 | # 每月将改变宗教信仰（皈依不同宗教）的人口百分比（若符合条件） |
| CONVERSION_UNINCORPORATED_MULT | 0.1 | # 在非整合州中 CONVERSION_RATE 乘以该系数 |
| MIN_CONVERSION | 1 | # 若存在任何皈依，至少会有这么多人口改变信仰 |
| DEFAULT_OBSESSION_DEMAND_MIN | 0.5 | # 偏好商品（obsession）的最低相对需求（覆盖购买包商品类别中的最低需求），可在人口需求中覆盖 |
| DEFAULT_OBSESSION_DEMAND_MULT | 1.5 | # 偏好商品的需求乘以该系数，可在人口需求中覆盖 |
| MIN_POPS_FOR_NEW_OBSESSION | 50000 | # 某文化的至少这么多人口必须生活在一个市场中，才会对其商品产生偏好 |
| MIN_SUPPLY_LEVEL_FOR_NEW_OBSESSION | 0.5 | # 供给必须至少达到需求的这么多倍 |
| MIN_DEMAND_VALUE_FOR_NEW_OBSESSION | 500 | # 市场中必须存在这么多金额（单位数量 × 商品基础价格）的需求才会产生新的偏好 |
| MAX_NUM_OBSESSIONS | 3 | # 一种文化同时只能拥有这么多偏好商品 |
| OBSESSION_SPAWN_CHANCE | 0.5 | # 每年概率（1.0 = 1%），乘以商品供给与市场规模系数 |
| OBSESSION_SPAWN_CHANCE_MAX_SUPPLY_MULT | 3.0 | # 供给相对需求超过此值后不再计入生成概率 |
| OBSESSION_SPAWN_CHANCE_PRESTIGE_GOODS_MULT | 4.0 | # 新偏好商品的生成概率乘以（1 + 该值），按威望商品占商品供给的比例缩放 |
| TABOO_DEMAND_MULT | 0.5 | # 禁忌（taboo）商品的需求乘以该系数 |
| DEFAULT_PRESTIGE_GOODS_DEMAND_INCREASE | 0.5 | # 商品需求乘以（1 + 该值），按本地供给中威望商品的占比缩放，可在人口需求中覆盖 |
| MAX_DEMAND_ADJUSTMENT_BASE_AMOUNT | 0.01 | # 控制人口在单次更新中对可替代商品需求的最大调整量（基础值） |
| MAX_DEMAND_ADJUSTMENT_SCALED_AMOUNT | 0.09 | # 控制人口在单次更新中对可替代商品需求的最大调整量（缩放值） |
| MAX_DEMAND_ADJUSTMENT_SCALE | 1.0 | # 当目标需求与当前需求的差值达到此值时，应用最大需求调整比例 |
| PRESTIGE_GOOD_SOL_BONUS_SCALING | 0.4 | # 生活水平（SoL）的额外乘数，按人口购买包中威望商品的百分比缩放 |
| PRESTIGE_GOOD_SOL_MAX_BONUS | 0.2 | # 威望商品带来的生活水平加成乘数不能超过此值 |
| LOCAL_GOODS_SUBSTITUTION_SUPPLY_GDP_FACTOR | 0.25 | # 为使本地商品在大型市场中能与非本地商品正常竞争，我们将该本地商品在市场中的产量的一部分加入供给，其值等于（1 - 该州的 GDP 份额）× 该系数 # 这仅用于商品替代供给的计算，而*不*用于价格计算 |
| OBSESSION_POP_NEED_EXPENSE_MULT | 0.25 | # 含偏好在内的人口需求总支出按此值变化（按偏好数量缩放，资金从其他需求中给予或扣除） |
| TABOO_POP_NEED_EXPENSE_MULT | -0.25 | # 含禁忌在内的人口需求总支出按此值变化（按禁忌数量缩放，资金从其他需求中给予或扣除） |
| WORKING_ADULT_RATIO_BASE | 0.25 | # 劳动人口与被抚养人口的基础比例，可由人口类型定义和国家 modifier 覆盖。 |
| WORKING_ADULT_RATIO_SKEW_MAXIMUM | 2.0 | # 当劳动人口与被抚养人口比例失衡时，该比例会自行修正，此值限制其最大效果 |
| DEPENDENT_CONSUMPTION_RATIO | 0.5 | # 受抚养者相对于劳动成年人的需求消耗倍数 |
| LITERACY_DIEOFF_BIAS | 1.0 | # 因年老死亡的识字人口相对于当前识字率的百分比，该值越高，识字率下降时人口文盲化的速度越快 |
| DEFAULT_SOL_CHANGE_IMPACT_FACTOR | 0.03 | # 生活水平变化导致人口中多大比例转变为忠诚派或激进派，可在特定人口类型上覆盖此值 |
| SOL_CHANGE_IMPACT_FACTOR_REDUCTION_START | 15 | # 生活水平高于此值时，开始缩减因生活水平变化产生的忠诚派/激进派数量 |
| SOL_CHANGE_IMPACT_FACTOR_REDUCTION_END | 30 | # 生活水平达到此值时，对因生活水平变化产生的忠诚派/激进派应用最大缩减幅度 |
| SOL_CHANGE_IMPACT_FACTOR_REDUCTION_SCALE | 9 | # 在最大缩减幅度下，因生活水平变化产生的忠诚派/激进派数量除以（1 + 此值） |
| SOL_STARVING_THRESHOLD | 5 |  |
| SOL_STRUGGLING_THRESHOLD | 10 |  |
| LOW_POP_THRESHOLD | 5000 | # 若一个州每单位可耕地的人口少于此值，则应用低人口修正 |
| HIGH_POP_THRESHOLD | 100000 | # 若一个州每单位可耕地的人口多于此值，则应用高人口修正 |
| （wiki 编辑者注）以下 defines 在 `00_defines.txt` 中位于人口迁移 defines 之后、人口合并 defines 之前。 |  |  |
| COLONIZATION_RIGHTS_GROWTH_MULTIPLIER | 2.0 | # 若拥有殖民权利，殖民增长和最大殖民增长乘以此值 |
| COMPANY_COLONIZATION_GROWTH_MULTIPLIER | 1.2 | # 若拥有公司殖民权利，殖民增长和最大殖民增长乘以此值 |
| COLONIAL_GROWTH_BASE_FACTOR | 0.00001 | # 一个州产生的殖民增长为每 1000 人口此数值，并乘以该州的殖民增长修正 |
| MIN_BASE_COLONIAL_GROWTH | 0.005 | # 国家基于人口的基础殖民增长不会低于此值 |
| MAX_BASE_COLONIAL_GROWTH | 0.1 | # 国家基于人口的基础殖民增长不会高于此值 |
| MAX_COLONIAL_GROWTH | 0.02 | # 殖民地每日最多增长此数值 |
| COLONY_SPEED_PROVINCE_SIZE_STANDARD | 50 | # 为可殖民州区域的大小（以省份计）设定基准值 |
| COLONY_SPEED_PER_PROVINCE_DIFF_FROM_STANDARD | 0.02 | # 州区域的省份数每比 COLONY_SPEED_PROVINCE_SIZE_STANDARD 多或少一个，殖民速度即按此比率（百分比）增加或减少 |
| COLONY_SPEED_POPULATION_INCREMENT | 100000 | # 确定殖民州与被殖民州双方合计人口达到多少时应开始放缓殖民速率；设为 0 可禁用 |
| COLONY_SPEED_MALUS_PER_POPULATION_INCREMENT | 0.25 | # 自 COLONY_SPEED_THRESHOLD_FROM_POPULATION 人口数起，殖民地人口加上被殖民省份所在州超过 20 万的部分，按比例增加完成天数（例如：COLONY_SPEED_THRESHOLD_FROM_POPULATION = 20 万、此值为 0.5 时，总居民 30 万则增长乘以 1/1.25 = 0.8；居民 60 万则乘以 0.25） |
| INDIVIDUALS_PER_POP_INFRASTRUCTURE | 100000 | # 将 state_infrastructure_from_population_add 乘以此值，以确定来自人口的基础设施 |
| QUALIFICATIONS_UPDATE_FACTOR | 0.0003 | # 计算出的潜在数值乘以此值和人口的劳动力规模后，再累加到现有潜在值上 |
| QUALIFICATIONS_NUM_MONTHS_AT_START | 60 | # 游戏开始时为人口预置多少个月的资质？ |
| INDIVIDUALS_TAXED_PER_TAX_CAPACITY | 10000 | # 每点税收能力可高效征税多少人口 |
| EXPECTED_SOL_FROM_LITERACY_SUBSISTENCE_MULT | 0.25 | # 在自给建筑中工作的人口的基于识字率的预期生活水平乘以此值 |
| JOB_SATISFACTION_BASE | -130 | # 工作满意度基础值 |
| JOB_SATISFACTION_FOR_NEWLY_HIRED | 1000 | # 因刚被雇佣而获得的工作满意度，该状态持续到该人口（Pop）下次财富计算为止 |
| JOB_SATISFACTION_PER_SOL_ABOVE_EXPECTED_SOL | 3 | # 每超出预期生活水平一级所获得的工作满意度 |
| JOB_SATISFACTION_PER_SOL_ABOVE_STATE_STRATA_SOL | 2 | # 每超出所在州同阶层平均水平一级所获得的工作满意度 |
| JOB_SATISFACTION_PER_SOL_ABOVE_COUNTRY_STRATA_SOL | 1 | # 每超出国家同阶层平均水平一级所获得的工作满意度 |
| JOB_SATISFACTION_PER_PERCENT_WAGE_RATE_ABOVE_NORMAL | 1 | # 工作场所工资率（1 万名劳工的周薪）每高于国家正常水平一英镑所获得的工作满意度 |
| JOB_SATISFACTION_FROM_CAN_AFFORD_EXPENSES | 1000 | # 能够负担基本消费包（及税款）所获得的工作满意度 |
| JOB_SATISFACTION_FROM_CANNOT_AFFORD_EXPENSES | -100 | # 无法负担基本消费包（及税款）所获得的工作满意度 |
| JOB_SATISFACTION_PER_PERCENT_HIGHER_SOL_QUALIFICATION | -1 | # 劳动力中具备更高基础生活水平工作资质的百分比每增加 1% 所获得的工作满意度。注意，资质被假定为相互重叠，此计算使用最大的资质 |
| JOB_SATISFACTION_FROM_JOB_ATTRACTIVENESS | 100 | # 受雇时的工作满意度，乘以工作吸引力 |
| JOB_SATISFACTION_DIVIDENDS_MAX_MULT | 5 | # 人口分红与工资之比的最大乘数 |
| JOB_SATISFACTION_DIVIDENDS_BASE | 50 | # 与分红和工资之比相乘的基础值 |
| JOB_SATISFACTION_LOSSES_MIN_MULT | -5 | # 人口损失与工资之比的最小乘数（或者说最大幅度） |
| JOB_SATISFACTION_LOSSES_BASE | 50 | # 与损失和工资之比相乘的基础值 |
| JOB_SATISFACTION_GOVERNMENT | 50 | # 政府职位需要更多稳定性 |
| @starvation_threshold | 0.4 |  |
| @starvation_scaling_factor | @[1/starvation_threshold] |  |
| FOOD_SECURITY_MODERATE_THRESHOLD | 0.6 | # 若粮食安全低于此值，该人口被标记为粮食安全程度中等 |
| FOOD_SECURITY_STARVATION_THRESHOLD | @starvation_threshold | # 若粮食安全低于此值，该人口被视为处于饥饿状态 |
| FOOD_SECURITY_SEVERE_STARVATION_THRESHOLD | 0.2 | # 若粮食安全低于此值，该人口被视为处于严重饥饿状态 |
| STARVATION_EFFECTS_SCALING_FACTOR | @starvation_scaling_factor | # 作为将粮食安全转换为饥饿效果的缩放系数：饥饿值 = CLAMP( (饥饿阈值 - 粮食安全) * 缩放系数， 0, 1) |
| FAMINE_POPULATION_SHARE_IN_STARVATION | 0.35 | # 若处于饥饿状态的州人口比例至少达到此百分比，该州被视为发生饥荒 |
| FAMINE_POPULATION_SHARE_IN_SEVERE_STARVATION | 0.15 | # 若处于严重饥饿状态的州人口比例至少达到此百分比，该州被视为发生饥荒 |
#### 人口迁移

| Define | 默认值 | 注释 |
|---|---|---|
| ## General ## |  |  |
| MIGRATION_MIN_STATE_POPS | 20000 | # 人口少于此数的州不会产生向外移民 |
| MIGRATION_STATE_POPULATION_THRESHOLD | 100000 | # 人口少于此数的州会减少市场移民数量，以避免人口完全流失 |
| MIGRATION_MAX_PER_STATE_BASE | 500 | # 单周内迁出或迁入一个州的人数不会超过此数（基础值） |
| MIGRATION_MAX_PER_STATE_INFRASTRUCTURE | 5 | # 单周内迁出或迁入一个州的人数不会超过此数（随基础设施规模变化） |
| MIGRATION_MAX_EMIGRATION_AS_POPULATION_FRACTION | 0.005 | # 每周最大向外移民人数被限制为州人口乘以此比例 |
| MIGRATION_MAX_PER_STATE_UNEMPLOYMENT_ORIGIN_FRACTION | 0.05 | # 州内失业工人数乘以此值后，会增加到该州可迁出人数上限中（在经过 MIGRATION_MAX_EMIGRATION_AS_POPULATION_FRACTION 的限制之后） |
| MIGRATION_MAX_PER_STATE_UNEMPLOYMENT_TARGET_FRACTION | 0.05 | # 州内失业工人数乘以此值后，会从可迁入该州的人数上限中扣除（在经过 MIGRATION_MAX_EMIGRATION_AS_POPULATION_FRACTION 的限制之后） |
| # Migration Desire # |  |  |
| MIGRATION_DESIRE_FROM_JOB_SATISFACTION_FACTOR | -1.0 | # 人口的迁移意愿会因其工作满意度乘以此值而增加。 |
| # Acceptance # |  |  |
| MIN_ACCEPTANCE_VALUE | 0 | # 它既是人口可具有的最低接受度数值，也是为首个接受度状态脚本设定的明确阈值 [任意有符号 32 位数值] |
| MAX_ACCEPTANCE_VALUE | 100 | # 它既是人口可具有的最高接受度数值，也是最后一个接受度状态的（隐含）上限 [> MIN_ACCEPTANCE_VALUE] |
| ACCEPTANCE_FROM_HOMELAND_COMMUNITY | 0 | # 人口因居住在本土而获得的接受度，静态应用于其文化社区 |
| ACCEPTANCE_FROM_NOT_HOMELAND_COMMUNITY | 0 | # 人口因不居住在本土而获得的接受度，静态应用于其文化社区 |
| MIN_REQUIRED_ACCEPTANCE_FOR_MIGRATION | 30 | # 如果人口在目标州的接受度低于此值，就不会大规模迁移到那里 |
| EXPECTED_ACCEPTANCE_INCREASE_TO_MIGRATE | 10 | # 人口大规模迁移时会寻求将接受度提高此数值，但如果大规模迁移的吸引力差距足够大，也可能接受较低的值 |
| MAX_ACCEPTANCE_RATIO_MULT_MIGRATION | 5 | # 大规模迁移中来源地与目标地之间的接受度差异最多会导致迁移量增加此倍数 |
| BUCKET_MIGRATION_EXPIRATION_YEARS | 5 | # 迁移桶在被移除前会保留多久 |
| BUCKET_MIGRATION_THRESHOLD | 1000 | # 迁移桶中需要有多少人口才会执行迁移 |
| BUCKET_MIGRATION_MIN_LEFTOVER_THRESHOLD | 1000 | # 执行迁移桶迁移时，可留在原地而不被迁往其他州的最少人口数 |
| MIGRATION_PULL_CULTURE_VACANCIES_MODIFIER | 0.25 | # 如果有该人口文化可用的职位空缺，则修正其迁移拉力 |
| MIGRATION_PULL_CULTURE_NO_VACANCIES_MODIFIER | -0.5 | # 如果没有该人口文化可用的职位空缺，则修正其迁移拉力 |
| # Cultural Communities # |  |  |
| CULTURAL_COMMUNITY_LINGER_TIME_WEEKS | 3 | # 当某一文化的最后一个人口离开某州后，相应的文化社区将在此时长后被移除 |
| CULTURAL_COMMUNITY_MAX_PER_MONTH_CHANCE | 0.04 |  |
| CULTURAL_COMMUNITY_ACCEPTANCE_DELTA_ON_SPAWN | -0.3 | # 文化社区首次出现时，应作为增量加入的最大文化接受度百分比 |
| CULTURAL_COMMUNITY_ACCEPTANCE_DELTA_DECAY_PER_MONTH | 0.25 | # 每月衰减的接纳度差值数量 |
| # 文化狂热 # |  |  |
| CULTURAL_FERVOR_MAX | 100 | # 文化狂热的最大值 |
| CULTURAL_FERVOR_MIN | 0 | # 文化狂热的最小值 |
| CULTURAL_FERVOR_DRIFT | 0.01 | # 控制每月从当前狂热值向目标狂热值漂移的系数 |
| CULTURAL_FERVOR_DRIFT_MIN | 0.05 | # 狂热值向其目标值移动的最小量（除非会超出目标值） |
| CULTURAL_FERVOR_LITERACY_IMPACT | 35 | # 人口识字率对文化狂热的影响 |
| CULTURAL_FERVOR_WAR_IMPACT | 20 | # 战争对文化狂热的影响，未使用 |
| CULTURAL_FERVOR_CASUALTIES_IMPACT_MAX | 30 | # 战争与损耗伤亡对文化狂热的最大影响 |
| CULTURAL_FERVOR_CASUALTIES_RATIO_MAX | 0.1 | # 使伤亡对文化狂热产生最大影响的死亡人口与存活人口之比 |
| CULTURAL_FERVOR_ACADEMICS_IMPACT | 0.002 | # 人均教育接入度对文化狂热的影响（按人口计） |
| CULTURAL_FERVOR_ACADEMICS_IMPACT_CAP | 25 | # 学者影响的上限 |
| CULTURAL_FERVOR_ACCEPTANCE_IMPACT | -0.05 | # 人口接纳度对文化狂热的影响 |
| CULTURAL_FERVOR_NATIONALISM_IMPACT | 5 | # 民族主义对文化狂热的影响，若某文化的全部人口都生活在民族主义下，文化狂热将增加此数值，否则增加其一部分 |
| CULTURAL_FERVOR_PAN_NATIONALISM_IMPACT | 5 | # 泛民族主义对文化狂热的影响，若某文化的全部人口都生活在泛民族主义下，文化狂热将增加此数值，否则增加其一部分 |
| CULTURAL_FERVOR_PUBLIC_SCHOOLS_IMPACT | 10 | # 公立学校对文化狂热的影响，若某文化的全部人口都生活在公立学校下，文化狂热将增加此数值，否则增加其一部分 |
| CULTURAL_FERVOR_OTHER_CULTURES_RELEASED_IMPACT | 10 | # 对文化获得释放的国家中非主流文化的影响 |
| CULTURAL_FERVOR_NATIONAL_AWAKENING_THRESHOLD | 25 | # 文化有可能发生民族觉醒的狂热值阈值 |
| CULTURAL_NATIONAL_AWAKENING_CHANCE_INCREASE_PER_FERVOR | 0.01 | # 狂热值超过觉醒阈值后，每点狂热值增加的民族觉醒发生几率 |
| CULTURAL_FERVOR_NATIONAL_AWAKENING_IMPACT | 20 | # 发生民族觉醒对狂热值的影响 |
| CULTURAL_FERVOR_NATIONAL_AWAKENING_DEFAULT_LENGTH_MONTHS | 120 | # 民族觉醒的默认持续时长（月） |
| CULTURAL_FERVOR_ASSIMILATIOM_EFFECT | 0.01 | # 文化狂热对同化的影响，狂热值越高，同化难度增加此数值 |
| CULTURAL_FERVOR_WAR_SUPPORT_EFFECT | 0.01 | # 文化狂热对战争支持度的影响 |
| CULTURAL_FERVOR_CONQUEST_RADICILIZATION_IMPACT | -0.005 | # 当一个州被与其人口主流文化相同的国家的征服时，对人口激进化程度的修正 |
| # 奴隶制 # |  |  |
| MIGRATION_MIN_POP_AMOUNT | 1 | # 每周迁移的单一人口数量不得低于此值（前提是确实会发生迁移） |
| # UX/UI 标签 # |  |  |
| MIGRATION_PULL_HIGH_THRESHOLD | 1.25 | # 州的迁移拉力必须至少达到市场平均值 * 此值才能获得市场移民 |
| MIGRATION_PULL_LOW_THRESHOLD | 0.75 | # 州的迁移拉力必须小于或等于市场平均值 * 此值才会产生全额移民迁出 |
| # 条约港 # |  |  |
| TREATY_PORT_INITIAL_MIGRATION | 1000 | # 建立条约港时，从夺取国第一主流文化迁移至该条约港的人口数量 |
| ## 迁移吸引力 ## |  |  |
| MIGRATION_PULL_EMPTY_STATE | 100 | # 如果一个州完全没有人口，则给予其极高的迁移吸引力 |
| MIGRATION_PULL_FROM_LIVING_STANDARD | 2 | # 目标州平均生活水平每有一点带来的迁移吸引力 |
| MIGRATION_PULL_FROM_AVAILABLE_EMPLOYMENT | 30 | # 每 1 万个可用的非自给就业岗位增加的迁移吸引力 |
| MIGRATION_PULL_FROM_AVAILABLE_EMPLOYMENT_MAX | 30 | # 可用非自给就业岗位相对已就业非自给人次的百分比，乘以此数值，即为迁移吸引力的增量 |
| MIGRATION_PULL_FROM_AVAILABLE_SUBSISTENCE_EMPLOYMENT | 2 | # 可用自给就业岗位相对已就业非自给人次的百分比，乘以此数值，即为迁移吸引力的增量 |
| MIGRATION_PULL_FROM_AVAILABLE_SUBSISTENCE_EMPLOYMENT_MAX | 10 | # 来自可用自给就业岗位的迁移吸引力不能超过此值 |
| MIGRATION_PULL_REDUCTION_FROM_UNEMPLOYMENT | 50 | # 失业人次相对就业人次的百分比，乘以此数值，即为迁移吸引力的减量 |
| MIGRATION_PULL_REDUCTION_FROM_UNEMPLOYMENT_MAX | 50 | # 因失业导致的迁移吸引力减量不能超过此值 |
| ## 市场迁移 ## |  |  |
| # 市场迁移处理 # |  |  |
| MARKET_MIGRATION_STATE_ATTRACTION_FRACTION | 0.75 | # 迁移吸引力至少达到最具吸引力的州的这一比例的州才会接收迁移 |
| MARKET_MIGRATION_PER_WEEK_FACTOR | 5 | # 迁移吸引力每相差一点，每周按此数值迁移的人数 |
| MARKET_MIGRATION_PER_WEEK_PER_TOTAL_POPULATION | 100000 | # 此外，迁移吸引力每相差一点，总人口每达到此数值便额外迁移一人 |
| MARKET_MIGRATION_MIN_DIFFERENCE_IN_MIGRATION_ATTRACTION_TO_MOVE | 5 | # 如果人口的最佳选择的迁移吸引力差值低于此数值，则不会迁移 |
| MARKET_MIGRATION_MIN_POP_FRACTION_TO_MOVE | 0.05 | # 如果想要迁移的人占一个人口的比重低于此比例，则不会创建新的人口，他们也不会迁移。 |
| MIGRATION_PULL_MULT_FROM_NO_DISCRIMINATION | 0.5 | # 如果人口从受歧视迁移到不受歧视的地方，迁移吸引力乘数增加此值（不适用于大规模迁移目标） |
| MIGRATION_PULL_MULT_FROM_HOMELANDS | 0.2 | # 如果人口迁移到文化故土，迁移吸引力乘数增加此值（不适用于大规模迁移目标） |
| ## 大规模迁移 ## # 大规模迁移设置 # |  |  |
| MASS_MIGRATION_MIN_TRADE_VALUE_BETWEEN_MARKETS | 1 | # 两个市场之间必须至少有此金额的贸易往来才会发生大规模迁移。世界市场贸易与条约贸易均计入其中。 |
| MASS_MIGRATION_ORIGIN_MIN_TURMOIL | 0.15 | # 文化故土的动荡必须至少达到此值才能创建迁移目标 |
| MASS_MIGRATION_ORIGIN_MIN_EMIGRANTS | 100000 | # 一个国家必须至少有此数量的潜在移民才会触发大规模迁移 |
| MASS_MIGRATION_TARGET_MAX_TURMOIL | 0.30 | # 一个国家该文化的动荡必须不高于此值才能被选为大规模迁移目标 |
| MASS_MIGRATION_TARGET_MIN_ARABLE_LAND | 10 | # 一个州必须至少有此数量的可耕地才能成为大规模迁移目标 |
| MASS_MIGRATION_STATE_MIN_MARKET_ACCESS | 0.7 | # 一个州对其市场的市场接入必须至少达到此值才能成为大规模迁移目标或来源州 |
| MASS_MIGRATION_SPAWN_CHANCE | 2 | # 每个潜在大规模迁移的每周触发概率，随动荡而提升（1 = 1%） |
| MASS_MIGRATION_SPAWN_CHANCE_STRUGGLING_FACTOR | 0.2 | # 一个国家内某文化的生活水平每低于 10 一点，触发概率便增加此值 |
| MASS_MIGRATION_SPAWN_CHANCE_STARVING_FACTOR | 1 | # 某国某种文化的生活水平每低于 5 点一级，大规模迁移的生成概率就增加此值（叠加在挣扎系数之上） |
| MASS_MIGRATION_TARGET_COUNTRY_RANDOM_FACTOR | 0.5 | # 此值越高，大规模迁移目标国家的选择就越随机 |
| MASS_MIGRATION_TARGET_STATE_RANDOM_FACTOR | 0.5 | # 此值越高，目标国家内大规模迁移目标州的选择就越随机 |
| MASS_MIGRATION_DURATION_MONTHS | 12 | # 一次大规模迁移持续多少个月 |
| MASS_MIGRATION_COOLDOWN_MONTHS | 48 | # 同一文化从一国再次发起大规模迁移前需间隔多少个月 |
| MASS_MIGRATION_NUM_TARGET_STATES_FOR_NO_PENALTY | 4 | # 可能目标州数量至少达到此值的国家，其大规模迁移目标得分不会受到任何惩罚 |
| MASS_MIGRATION_FEW_TARGET_STATES_PENALTY | 0.2 | # 大规模迁移目标得分会按此值乘以少于 MASS_MIGRATION_NUM_TARGET_STATES_FOR_NO_PENALTY 的可能目标州数量所得的比例扣除。即 得分 = 得分 - 得分 * 此值 * 可能目标州差值 |
| # 大规模迁移处理 # |  |  |
| MASS_MIGRATION_PER_WEEK_FACTOR | 10 |  |
| MASS_MIGRATION_PER_WEEK_PER_TOTAL_POPULATION | 100000 |  |
| MASS_MIGRATION_MIN_DIFFERENCE_IN_MIGRATION_ATTRACTION_TO_MOVE | 10 |  |
|  |  | # 以下系数在迁移引力阈值判定*之后*应用，因此只影响某个州在迁移中所占的份额 |
| MIGRATION_PULL_MULT_FROM_MASS_MIGRATION_TARGET | 1.5 | # 目标州为大规模迁移目标时，迁移引力乘以此值 |
| MIGRATION_PULL_MULT_FROM_MASS_MIGRATION_TARGET_ADJACENCY | 1.1 | # 目标州与大规模迁移目标相邻时，迁移引力乘以此值 |
| MIGRATION_MAX_PER_STATE_MASS_EMIGRATION_MULT | 3.0 | # 大规模迁移时每周移民上限乘以此值（在 MIGRATION_MAX_EMIGRATION_AS_POPULATION_FRACTION 的钳制之后应用） |
| MIGRATION_MAX_PER_STATE_MASS_IMMIGRATION_MULT | 5.0 | # 大规模迁移时每周迁入上限乘以此值（在 MIGRATION_MAX_EMIGRATION_AS_POPULATION_FRACTION 的钳制之后应用） |
| MASS_MIGRATION_NEIGHBORING_TARGET_STATE_LIMIT_FRACTION | 0.5 | # 大规模迁移中，相邻州获得的限额相对于主目标州的比例 |

#### 人口合并（Pop consolidation）

这些 defines 与人口合并的游戏规则相关。
| 定义项 | 默认值 | 注释 |
|---|---|---|
| ### Pop Consolidation defines # Pop Consolidation identifies pops so small their impact on the economy and politics is insignificant, and merges them into other pops in the same building or state. # POP_MERGE_MAX_WORKFORCE_* 确定人口在劳动力方面需要多小才能有资格与同一建筑中的其他人口或失业人口池合并 # POP_MERGE_MIN_NUM_POPS_SAME_PROFESSION_*：如果同一建筑中同类型人口数量未达到此数，就业人口将不会与同一建筑中的其他人口合并 # WORKFORCE_RATIO_MAX_UNEMPLOYMENT_FACTOR_*：劳动力低于 POP_MERGE_MAX_WORKFORCE 且劳动力：受抚养人比例比理想值差出此倍数的失业人口，将全部转为受抚养人并合并回同一州的人口中 # 定义项名称的尾部对应同名的人口合并（Pop Consolidation）游戏规则。 # 当该游戏规则激活时，POP_MERGE_MAX_WORKFORCE 和 WORKFORCE_RATIO_MAX_UNEMPLOYMENT_FACTOR 所定义的值代表最小值，而最大值为上一档的值。 # POP_MERGE_START_POP 和 POP_MERGE_MAX_TARGET_POP 决定向上一档数值缩放的幅度。 # 例如，在中等合并下，POP_MERGE_START_POP = 50000 且 POP_MERGE_MAX_TARGET_POP = 100000，全球人口为 87560 个人口： # POP_MERGE_MAX_WORKFORCE 实际上为 45（从 30 到 50 的 75% 处），WORKFORCE_RATIO_MAX_UNEMPLOYMENT_FACTOR 实际上为 1.6244（从 2 到 1.5 的 75% 处） |  |  |
| POP_MERGE_MAX_WORKFORCE_MINOR_CONSOLIDATION | 10 |  |
| POP_MERGE_MIN_NUM_POPS_SAME_PROFESSION_MINOR_CONSOLIDATION | 5 |  |
| WORKFORCE_RATIO_MAX_UNEMPLOYMENT_FACTOR_MINOR_CONSOLIDATION | 2.5 |  |
| POP_MERGE_MAX_WORKFORCE_MODERATE_CONSOLIDATION | 30 |  |
| POP_MERGE_MIN_NUM_POPS_SAME_PROFESSION_MODERATE_CONSOLIDATION | 4 |  |
| WORKFORCE_RATIO_MAX_UNEMPLOYMENT_FACTOR_MODERATE_CONSOLIDATION | 2 |  |
| POP_MERGE_MAX_WORKFORCE_AGGRESSIVE_CONSOLIDATION | 50 |  |
| POP_MERGE_MIN_NUM_POPS_SAME_PROFESSION_AGGRESSIVE_CONSOLIDATION | 3 |  |
| WORKFORCE_RATIO_MAX_UNEMPLOYMENT_FACTOR_AGGRESSIVE_CONSOLIDATION | 1.5 |  |
| POP_MERGE_MAX_WORKFORCE_MAX_CONSOLIDATION | 100 |  |
| WORKFORCE_RATIO_MAX_UNEMPLOYMENT_FACTOR_MAX_CONSOLIDATION | 1 |  |
| POP_MERGE_START_POPS | 50000 |  |
| POP_MERGE_MAX_TARGET_POPS | 100000 |  |
| ### Pop Weights for Dependents Distribution # 格式：{ lower strata, middle strata, upper strata } # 这些权重影响因战场伤亡而产生的受抚养人分配到潜在目标人口时的权重 # 例如，我们希望受伤和阵亡士兵所在的人口个体大部分合并到较低阶层人口中 |  |  |
| DEFAULT_DEPENDENTS_DISTRIBUTION_WEIGHTS | { 1.0 0.5 0.1 } | # 用于合并小型人口时 |
| LOWER_STRATA_CASUALTY_DEPENDENTS_DISTRIBUTION_WEIGHTS | { 1.0 0.1 0.0 } | # 用于士兵受伤时 |
| MIDDLE_STRATA_CASUALTY_DEPENDENTS_DISTRIBUTION_WEIGHTS | { 0.25 1.0 0.1 } | 用于军官受伤时 |
| UPPER_STRATA_CASUALTY_DEPENDENTS_DISTRIBUTION_WEIGHTS | { 1.0 0.5 0.1 } | 未使用，供 mod 制作使用，请随意 |
#### 人口增长

人口增长的 defines 使用一系列已定义和派生的变量。

| 变量 | 默认值 | 说明 |
|---|---|---|
| ## 每月基础数值 |  |  |
| @min_birthrate | 0.00060 | # 每月最低基础出生率（在 POP_GROWTH_STABLE_SOL 时） |
| @max_birthrate | 0.00450 | # 每月最高基础出生率（在 SOL = 0 时） |
| @min_mortality | 0.00045 | # 每月最低基础死亡率（在 POP_GROWTH_STABLE_SOL 时） |
| @max_mortality | 0.00550 | # 每月最高基础死亡率（在 SOL = 0 时） |
| ## 生活水平阈值 |  |  |
| @pop_growth_equilibrium_sol | 5 | # 均衡点是人口停止饥饿、增长首次转正的生活水平 |
| @pop_growth_transition_sol | 10 | # 过渡点决定出生率在开始下降前"滞后"于死亡率多久。设为与均衡点相同则不会产生"滞后"（仅对出生率有影响） |
| @pop_growth_max_sol | 15 | # 增长峰值点是净增长通常最高时的生活水平（仅对死亡率有影响） |
| @pop_growth_stable_sol | 25 | # 稳定点是出生率和死亡率停止变化并达到其最小值时的生活水平 |
| ## 其他 |  |  |
| @transition_birthrate_mult | 1 | # 如果你希望出生率"滞后"达到比 max_birthrate 更高或更低的值。（你也可以直接在下方修改） |
| @max_growth_mortality_mult | 0.35 | # 在增长峰值点，死亡率应占 birthrate_at_growth_max 的比例。数值越高意味着增长越低 |
| ### 人口增长派生数值 # 一般来说，对于下面每一个派生数值，我们实际上只是在做以下三种运算之一（或其组合）：# - 计算一个点：sol * slope + start_value（x_at_y）# - 计算一个斜率：(start_value - end_value) / number_of_steps（x_slope）# - 计算一个截距：-slope*sol + end_value（x_intercept）# 只有对于不从 0 生活水平开始的线段才需要截距 |  |  |
| @birthrate_at_transition | @[max_birthrate*transition_birthrate_mult] |  |
| @rate_at_equilibrium | @[pop_growth_equilibrium_sol*((birthrate_at_transition-max_birthrate)/pop_growth_transition_sol)+max_birthrate] | # 同时决定死亡率和出生率 |
| ## 生活水平从 0 到 pop_growth_equilibrium_sol 的死亡率 |  |  |
| @mortality_starving_slope | @[(rate_at_equilibrium-max_mortality)/pop_growth_equilibrium_sol] |  |
| ## 生活水平从 0 到 pop_growth_transition_sol 的出生率 \|\| |  |  |
| @birthrate_pretransition_slope | @[(birthrate_at_transition-rate_at_equilibrium)/pop_growth_transition_sol] |  |
| ## 生活水平从 pop_growth_equilibrium_sol 到 pop_growth_max_sol 的死亡率 |  |  |
| @birthrate_at_growth_max | @[(pop_growth_max_sol-pop_growth_transition_sol)*((min_birthrate-birthrate_at_transition)/(pop_growth_stable_sol-pop_growth_transition_sol))+birthrate_at_transition] |  |
| @mortality_at_growth_max | @[birthrate_at_growth_max*max_growth_mortality_mult] |  |
| @mortality_equilibrium_to_growth_max_slope | @[(mortality_at_growth_max-rate_at_equilibrium)/(pop_growth_max_sol-pop_growth_equilibrium_sol)] |  |
| @mortality_equilibrium_to_growth_max_intercept | @[-mortality_equilibrium_to_growth_max_slope*pop_growth_equilibrium_sol+rate_at_equilibrium] |  |
| ## 生活水平从 pop_growth_transition_sol 到 pop_growth_stable_sol 的出生率 |  |  |
| @birthrate_transition_slope | @[(min_birthrate-birthrate_at_transition)/(pop_growth_stable_sol-pop_growth_transition_sol)] |  |
| @birthrate_transition_intercept | @[-birthrate_transition_slope*pop_growth_stable_sol+min_birthrate] |  |
| ## 生活水平从 pop_growth_max_sol 到 pop_growth_stable_sol 的死亡率 |  |  |
| @mortality_growth_max_to_stable_slope | @[(min_mortality-mortality_at_growth_max)/(pop_growth_stable_sol-pop_growth_max_sol)] |  |
| @mortality_growth_max_to_stable_intercept | @[-mortality_growth_max_to_stable_slope*pop_growth_stable_sol+min_mortality] |  |
| ### 用于确定基础死亡率/出生率的伪算法 |  |  |
| ## Mortality # if (sol < POP_GROWTH_EQUILIBRIUM_SOL) # { mortality = sol * POP_GROWTH_MORTALITY_STARVING_SLOPE + POP_GROWTH_MAX_MORTALITY } # else if (sol < POP_GROWTH_MAX_SOL) # { mortality = sol * POP_GROWTH_MORTALITY_EQUILIBRIUM_TO_GROWTH_MAX_SLOPE + POP_GROWTH_MORTALITY_EQUILIBRIUM_TO_GROWTH_MAX_INTERCEPT } # else if (sol < POP_GROWTH_STABLE_SOL) # { mortality = sol * POP_GROWTH_MORTALITY_GROWTH_MAX_TO_STABLE_SLOPE + POP_GROWTH_MORTALITY_GROWTH_MAX_TO_STABLE_INTERCEPT } # else { mortality = POP_GROWTH_MIN_MORTALITY } |  |  |
| ## Birthrate # if (sol < POP_GROWTH_EQUILIBRIUM_SOL) # { birthrate = sol * POP_GROWTH_BIRTHRATE_PRETRANSITION_SLOPE + POP_GROWTH_MAX_BIRTHRATE } # else if (sol < POP_GROWTH_TRANSITION_SOL) # { birthrate = sol * POP_GROWTH_BIRTHRATE_PRETRANSITION_SLOPE + POP_GROWTH_MAX_BIRTHRATE } # else if (sol < POP_GROWTH_STABLE_SOL) # { birthrate = sol * POP_GROWTH_BIRTHRATE_TRANSITION_SLOPE + POP_GROWTH_BIRTHRATE_TRANSITION_INTERCEPT } # else { birthrate = POP_GROWTH_MIN_BIRTHRATE } |  |  |

| Define（定义） | 默认值 | 注释 |
|---|---|---|
| ## 出生率 |  |  |
| POP_GROWTH_BIRTHRATE_PRETRANSITION_SLOPE | @birthrate_pretransition_slope |  |
| POP_GROWTH_BIRTHRATE_TRANSITION_SLOPE | @birthrate_transition_slope |  |
| POP_GROWTH_BIRTHRATE_TRANSITION_INTERCEPT | @birthrate_transition_intercept |  |
| ## 死亡率 |  |  |
| POP_GROWTH_MORTALITY_STARVING_SLOPE | @mortality_starving_slope |  |
| POP_GROWTH_MORTALITY_EQUILIBRIUM_TO_GROWTH_MAX_SLOPE | @mortality_equilibrium_to_growth_max_slope |  |
| POP_GROWTH_MORTALITY_EQUILIBRIUM_TO_GROWTH_MAX_INTERCEPT | @mortality_equilibrium_to_growth_max_intercept |  |
| POP_GROWTH_MORTALITY_GROWTH_MAX_TO_STABLE_SLOPE | @mortality_growth_max_to_stable_slope |  |
| POP_GROWTH_MORTALITY_GROWTH_MAX_TO_STABLE_INTERCEPT | @mortality_growth_max_to_stable_intercept |  |
| ## 基础数值 |  |  |
| POP_GROWTH_MIN_BIRTHRATE | @min_birthrate | # 每月最低基础出生率（在 POP_GROWTH_STABLE_SOL 时） |
| POP_GROWTH_MAX_BIRTHRATE | @max_birthrate | # 每月最高基础出生率（在 SOL = 0 时） |
| POP_GROWTH_MIN_MORTALITY | @min_mortality | # 每月最低基础死亡率（在 POP_GROWTH_STABLE_SOL 时） |
| POP_GROWTH_MAX_MORTALITY | @max_mortality | # 每月最高基础死亡率（在 SOL = 0 时） |
| ## 生活水平（SoL）阈值 |  |  |
| POP_GROWTH_EQUILIBRIUM_SOL | @pop_growth_equilibrium_sol | # 均衡点是指人口不再挨饿、增长首次转为正数的点 |
| POP_GROWTH_TRANSITION_SOL | @pop_growth_transition_sol | # 转折点决定出生率在开始下降之前“滞后”于死亡率多久。设为与均衡点相同则没有“滞后”（仅对出生率有影响） |
| POP_GROWTH_MAX_SOL | @pop_growth_max_sol | # 增长峰值点是指净增长通常达到最高值的点（仅对死亡率有影响） |
| POP_GROWTH_STABLE_SOL | @pop_growth_stable_sol | # 稳定点是指出生率和死亡率不再变化并达到其最小值的点 |
### 事件

| Define | 默认值 | 开发者注释 |
|---|---|---|
| DEFAULT_MONTHS_VALID | -1 | # 事件消失前持续的月数，-1 = 无限 |
| DEFAULT_GUI_WINDOW_TYPE | "event_window" | # 事件的默认 GUI 窗口类型 |
| NUM_DAYS_TO_AUTO_OPEN_EVENT | 30 | # 距离超时还剩多少天时自动弹出事件窗口 |

### 技术

| Define | 默认值 | 开发者注释 |
|---|---|---|
| TECH_SPREAD_RANDOM_RANGE | 0.5 | # 每周技术扩散的分布可以有多大波动 |
| TECH_AHEAD_OF_TIME_PENALTY_FACTOR | 0.25 | # 对于该类别中尚未研究的上一个时代的每项技术，按此倍数将其研究成本作为额外惩罚（乘以两项技术之间相隔的时代数） |
| NATIONALISM_TECHNOLOGY_TYPE | "nationalism" | # 民族主义技术的技术类型 |
| PAN_NATIONALISM_TECHNOLOGY_TYPE | "pan-nationalism" | # 泛民族主义技术的技术类型 |

### 人物

| Define | 默认值 | 开发者注释 |
|---|---|---|
| NUM_RANDOM_NAME_TRIES_FOR_UNIQUENESS | 3 | # 为人物生成随机姓名时，尝试在所在国家内寻找唯一姓名的次数 [>=1] |
| SET_RULER_NUM_OPTIONS | 3 | # 游戏开始时为一个国家生成的潜在统治者数量 |
| SET_RULER_POOL_SIZE | 7 | # 游戏开始时为一个国家生成的潜在统治者最大数量 |
| RULER_MIN_AGE_FOR_HEIR | 20 | # 低于此年龄时，不为统治者随机生成继承人 |
| RULER_AGE_FOR_HEIR_CHANCE_BOOST | 30 | # 超过此年龄一年后，开始提升继承人生成的概率 |
| RULER_HEIR_GENERATION_CHANCE | 0.001 | # 每日概率 |
| RULER_HEIR_CHANCE_BOOST_SCALE | 0.001 | # 超过 RULER_AGE_FOR_HEIR_CHANCE_BOOST 后每过一年加到 RULER_HEIR_CHANCE_BOOST 上的数值 |
| AGE_GENERATION_STARTVAL | 20 |  |
| AGE_GENERATION_DICE_ROLL_MAGNITUDE | 6 |  |
| AGE_GENERATION_NUM_DICE_ROLLS | 5 |  |
| RECRUIT_COMMANDER_NUM_OPTIONS | 3 |  |
| RECRUIT_COMMANDER_POOL_SIZE | 3 |  |
| RECRUIT_COMMANDER_VALUE_MARGINAL | -50 |  |
| RECRUIT_COMMANDER_VALUE_HISTORICAL | 50 | # 优先展示历史上的指挥官 |
| RECRUIT_COMMANDER_VALUE_AGE_MULT | 0.5 |  |
| RECRUIT_COMMANDER_VALUE_SAME_IGS | -40 |  |
| RECRUIT_COMMANDER_REMOVE_AGE | 55 | # 年满 55 岁时从招募池中移除 |
| COMMANDER_START_RANK | 1 |  |
| HIGHEST_PROMOTION_RANK | 5 |  |
| RULER_COMMANDER_START_RANK | 6 |  |
| MIN_POPULARITY | -100 |  |
| MAX_POPULARITY | 100 |  |
| POPULARITY_HATED_THRESHOLD | -50 |  |
| POPULARITY_DISLIKED_THRESHOLD | -25 |  |
| POPULARITY_LIKED_THRESHOLD | 25 |  |
| POPULARITY_LOVED_THRESHOLD | 50 |  |
| POPULARITY_AUTHORITY_FACTOR | 1 | # 统治者的声望转化为权威力时乘以此系数 |
| ROLE_RULER | "character_role_ruler" | # 分配给统治者人物的角色 |
| ROLE_HEIR | "character_role_heir" | # 分配给继承人人物的角色 |
| ROLE_IG_LEADER | "character_role_ig_leader" | # 分配给利益集团领袖人物的角色 |
| DEFAULT_CHARACTER_ROLE | "character_role_politician" | # 若已设置，未指定角色而生成的人物将默认获得此角色。留空则无默认角色。 |
| DEFAULT_TITLE_PREPOSITION | "PREP_IN" | # 若未定义头衔介词，则使用此介词 |
| CHARACTER_HOME_STATE_HOMELAND_MIN_WEIGHT | 1000 | # 为人物选择家乡州时，本土州在计算该文化人口时始终至少按此数量计入 |
| CHARACTER_HOME_STATE_TRY_EXCLUDE_STATE_WEIGHT | 0.001 | # 选择家乡州时主动尝试排除的州（例如在生成新的豪强时，该州已由一名豪强代表）其被选中概率乘以此值 |
| CHARACTER_HOME_STATE_CAPITAL_WEIGHT | 10.0 | # 首都被选为人物家乡州的概率乘以此值 |
| CHARACTER_TEMPLATE_CULTURE_ACCEPTED_THRESHOLD | 60 | # 使用 random_accepted 时，一种文化被视为“被接受”的最低文化接受度 |
| CHARACTER_TEMPLATE_RELIGION_ACCEPTED_THRESHOLD | 15 | # 使用 random_accepted 时，一种宗教被视为“被接受”的最低宗教接受度贡献值 |
| MAX_LOYALTY | 100 |  |
| LOYALTY_FROM_IG_APPROVAL | 5 | # 人物来自利益集团认可度的忠诚度以此为基准进行缩放 |
| LOYALTY_FROM_IG_APPROVAL_MIN | -50 | # 来自利益集团认可度的忠诚度影响不得低于此值 |
| LOYALTY_FROM_IG_APPROVAL_MAX | 50 | # 来自利益集团认可度的忠诚度影响不得高于此值 |
| LOYALTY_FROM_IDEOLOGY_ENACTED | 25 | # 人物因制定法律而获得的忠诚度增减以此为基准进行缩放 |
| LOYALTY_FROM_IDEOLOGY_ENACTING | 25 | # 人物因已制定法律而获得的忠诚度增减以此为基准进行缩放 |
| LOYALTY_FROM_IDEOLOGY_MIN | -50 | # 来自个人意识形态的忠诚度影响不得低于此值 |
| LOYALTY_FROM_IDEOLOGY_MAX | 50 | # 来自个人意识形态的忠诚度影响不得高于此值 |
| LOYALTY_UNCERTAIN_THRESHOLD | 25 |  |
| LOYALTY_NEUTRAL_THRESHOLD | 50 |  |
| LOYALTY_RELIABLE_THRESHOLD | 75 |  |
| LOYALTY_FAITHFUL_THRESHOLD | 100 |  |
| MAX_PROMINENCE | 100 |  |
| PROMINENCE_FROM_POPULARITY | 0.25 | # 声望的这一比例会转化为显赫度 |
| PROMINENCE_NOTEWORTHY_THRESHOLD | 10 |  |
| PROMINENCE_SIGNIFICANT_THRESHOLD | 25 |  |
| PROMINENCE_IMPORTANT_THRESHOLD | 50 |  |
| PROMINENCE_EMINENT_THRESHOLD | 75 |  |
| PROMINENCE_PREEMINENT_THRESHOLD | 100 |  |
| PROMINENCE_IG_MIN_MULTIPLIER | 0.05 | # 若人物的显赫度对 prominence_ig_modifier 的乘数低于此值，则将其设为此值 |
| HISTORICAL_CHARACTER_IDEOLOGY_LEADER_FACTOR | 2.0 # 选取利益集团领袖时，历史人物的显赫度权重乘以此系数，使其倾向于优先于随机生成的人物被选中 |  |
| HOLDING_TYPE_RANDOM_FACTOR | 1.0 # 此值越高，豪强选择持有类型时的随机性越大 |  |
| HOLDING_REVENUE_SCALING_GDP_DIVISOR | 1250 # 国家的国内生产总值除以此值，用于对持有的收入进行缩放并应用 character_holding_revenue 静态 modifier |  |
| HOLDING_REVENUE_SCALING_MIN | 0.2 | # 持有收入缩放永不低于此值 |
| HOLDING_REVENUE_SCALING_MAX | 1.0 | # 持有收入缩放永不高于此值 |
| AGITATOR_MOVEMENT_SUPPORT_LITERACY_WEIGHT | 0.75 | # 鼓动家额外支持度中按人口识字率缩放的比例 |
| AGITATOR_MOVEMENT_SUPPORT_IG_MEMBERSHIP_WEIGHT | 0.75 | # 鼓动家额外支持度中按同一利益集团成员比例缩放的比例 |
| AGITATOR_MOVEMENT_SUPPORT_BASE_FACTOR | 15 | # 鼓动家为其运动增加的吸引力（按识字率/利益集团成员比例缩放，基础值） |
| AGITATOR_MOVEMENT_SUPPORT_POPULARITY_FACTOR | 0.15 | # 鼓动家为其运动增加的吸引力（按识字率/利益集团成员比例缩放并乘以声望） |
| MIN_YEARS_OF_SERVICE_FOR_COMMANDER_IG_LEADER | 5 | # 服役年数少于此值的指挥官不会被考虑担任利益集团领袖 |
| # 以下数值用于控制何时应随机生成新的政客进入人物池 # 目标值是我们希望留作潜在新利益集团领袖的“无职位”政客数量 # 若无职位政客数量低于目标值，我们将尝试生成一名对该利益集团有效且代表未被代表意识形态的新政客 # 由模板生成的政客计入但不因此受上限约束 |  |  |
| TARGET_NUM_POOL_POLITICIANS_POWERFUL_IG | 3 |  |
| TARGET_NUM_POOL_POLITICIANS_INFLUENTIAL_IG | 2 |  |
| TARGET_NUM_POOL_POLITICIANS_MARGINAL_IG | 0 |  |
| CHILD_TRAIT | "trait_child" | # 该性格特质用于 16 岁以下的人物 |
| ADULT_AGE | 16 | # 低于此年龄的人物可选项更有限。例如他们不能成为军事领袖 [>= 0] |
| OLD_AGE | 60 | # 高于此年龄的人物可能获得某些特定特质和事件 [>= ADULT_AGE] |
| VOIDED_CHARACTER_DEFAULT_DURATION | 12 | # 人物在被删除前处于虚空（void）状态的默认月数 |
| INHERIT_RECESSIVE_GENE_CHANCE | 0.25 | # 隐性基因被选为继承人的显性/隐性基因的概率。仅用于肖像。 |
| AGITATOR_EXPECTED_SPAWN_INTERVAL_0_LITERACY | 12 | # 在识字率为 0% 时，某国预期每隔这么多年生成一位新鼓动家。（支持小数值） |
| AGITATOR_EXPECTED_SPAWN_INTERVAL_100_LITERACY | 2 | # 在识字率为 100% 时，某国预期每隔这么多年生成一位新鼓动家。（支持小数值） |
| ### 特质生成 # 每周，人物的“预期特质值”计量条会根据其角色和当前行为按下述指定数值增加（指挥官还会从其命令中获得活动等级的加成）# 每周，会针对（预期特质值计量条 − 当前特质值）掷一次百分位骰。若骰值低于当前值，则会添加一个新的随机特质（前提是存在有效的特质）。 |  |  |
| WEEKLY_CONDITION_CHANCE | 0.03 | # 人物每周获得一种状态（condition）的概率（1 = 1%） |
| MAX_EXPECTED_TRAIT_VALUE | 12.0 | # 人物在正常情况下可累积的特质值上限（注意：add_trait effect 不受此限制） |
| MAX_TRAITS_PERSONALITY | 2 | # 人物在正常情况下可获得性格特质的数量上限（注意：add_trait effect 不受此限制） |
| MAX_TRAITS_SKILL | 2 | # 人物在正常情况下可获得技能特质的数量上限（注意：add_trait effect 不受此限制） |
| MAX_TRAITS_CONDITION | 2 | # 人物在正常情况下可获得状态特质的数量上限（注意：add_trait effect 不受此限制） |
| TRAIT_GAIN_DIVISOR | 100.0 | # 最终特质获取值总是除以此数，这样就无需使用过多小数 |
| DEFAULT_TRAIT_GAIN | 0.25 | # 每个人物的预期特质计量条默认每周增加此数值 |
| TRAIT_GAIN_POLITICIAN_POWERFUL | 0.1 | # 权势政客的预期特质计量条每周额外增加此数值 |
| TRAIT_GAIN_RULER | 0.1 | # 统治者的预期特质计量条每周额外增加此数值 |
| TRAIT_GAIN_COMMANDER_RECRUITABLE | 0.05 | # 可招募指挥官的预期特质计量条每周增加此数值，覆盖所有其他因素 |
| TRAIT_GAIN_IN_EXILE_POOL | 0.1 | # 处于流亡池中的人物的预期特质计量条每周增加此数值，覆盖所有其他因素 |
| TRAIT_GAIN_VOIDED | 0.0 | # 处于虚空状态的人物的预期特质计量条每周增加此数值，覆盖所有其他因素 |
| # 以下参数决定人物预期寿命的计算方式。该计算基于正态分布，参数为：# µ = CHARACTER_LIFE_EXPECTANCY_BASE_YEARS # σ = CHARACTER_LIFE_EXPECTANCY_STDDEV_YEARS # # 虽然分布的均值是固定的，但结果会被人物的健康值修正。# 人物健康影响预期寿命的方式由公式 ((h / bh) - 1) * d 给出，其中：# - h 为人物健康值 # - bh 为基准健康值 # - d 为 CHARACTER_LIFE_EXPECTANCY_DELTA_YEARS 的值 # # (h / bh) - 1 即人物相对基准健康的“偏离距离”。每偏离基准一点，人物就会多活或少活 CHARACTER_LIFE_EXPECTANCY_DELTA_YEARS 年。# # 由于正态分布的定义域为 [-∞; +∞]，我们设定了由 CHARACTER_LIFE_EXPECTANCY_CUTOFF 定义的硬性截断。该值以 σ（即偏离均值的标准差数）表示。# 建议保持该值为 3，因为分布中 99.73% 的值都落在 [-3σ; +3σ] 范围内。# 由于上述原因，使用默认值时，健康值为 0 的人物将在 50 至 80 岁之间死亡，而健康值为 2 的人物将在 70 至 100 岁之间死亡。# # 注意：由于某些性能优化，即使热重载，修改这些数值也会无效或产生意外行为，直到重启游戏。 |  |  |
| MIN_CHARACTER_HEALTH | 0.0 | # 基准值为 1.0（即 100%），定义于 base_values modifier 中。0.0 表示比基准低 100%。[任意值] |
| MAX_CHARACTER_HEALTH | 2.0 | # 基准值为 1.0（即 100%），定义于 base_values modifier 中。2.0 表示比基准高 100%。[>= MIN_CHARACTER_HEALTH] |
| CHARACTER_LIFE_EXPECTANCY_BASE_YEARS | 75 | # 基准健康度下的预期寿命中位数（以年计）。它是正态分布的 µ 参数 [> 0] |
| CHARACTER_LIFE_EXPECTANCY_STDDEV | 5 | # 预期寿命分布的标准差。它是 σ 参数 [> 0] |
| CHARACTER_LIFE_EXPECTANCY_CUTOFF | 3 | # 我们将分布截断在双向各此数值的 σ 范围内。[-3σ; +3σ] 的区间涵盖了 99.73% 的数值。[> 0] |
| CHARACTER_LIFE_EXPECTANCY_DELTA_YEARS_BELOW_BASELINE | 30 | # 健康度每低于基准一个单位，预期寿命减少年数的随机基数 [>= 0] |
| CHARACTER_LIFE_EXPECTANCY_DELTA_YEARS_ABOVE_BASELINE | 15 | # 健康度每高于基准一个单位，预期寿命增加年数的随机基数 [>= 0] |
| # 预期寿命增减年数的随机基数会乘以 lerp(CHARACTER_LIFE_EXPECTANCY_DELTA_LERP_LOWER_BOUND, CHARACTER_LIFE_EXPECTANCY_DELTA_LERP_UPPER_BOUND) 范围内的一个随机值 |  |  |
| CHARACTER_LIFE_EXPECTANCY_DELTA_LERP_LOWER_BOUND | 0.5 |  |
| CHARACTER_LIFE_EXPECTANCY_DELTA_LERP_UPPER_BOUND | 1.5 |  |
| GUARANTEED_SURVIVABILITY_DAYS_MIN | 30 | # 停止 immortal 状态且本应随之死亡的人物，将至少存活这么多天，以避免诸如人物在远征结束时立即死亡的情况 [>= 0] |
| GUARANTEED_SURVIVABILITY_DAYS_MAX | 180 | # 同上，但为该范围的上限 [>= GUARANTEED_SURVIVABILITY_DAYS_MIN] |
|  |  | ## 互动 |
| INTERACTION_INVITE_EXILE | "invite_exile" |  |
|  |  | ## 生涯长度 |
| HISTORICAL_CAREER_LENGTH_MULT | 1.5 | # 历史人物的生涯长度乘以此倍率 |

### 战斗（Battle）

| 定义 | 默认值 | 开发者注释 |
|---|---|---|
| CASUALTY_MAJORITY_CULTURE_WEIGHT | 1.5 | # 多数文化的人口伤亡权重为 1.5 倍 |
| CASUALTY_ROLL_MIN | 50 | # 最小…… |
| CASUALTY_ROLL_MAX | 200 | # 每次掷骰对部队造成伤亡时，单个部队可承受的伤亡最大值 |
| SURVIVAL_RATE | 0.66 |  |
| DEPENDENTS_ROLL_MIN_PERCENT | 0.1 | # 最小…… |
| DEPENDENTS_ROLL_MAX_PERCENT | 0.3 | # 每次掷骰可转化为受扶养人口的人口规模最大百分比 |
| MIN_DEPENDENTS_PER_ROLL | 25 | # 每次掷骰添加到随机人口中的受扶养人口最低数量 |
| ESCAPE_PROGRESS_REQUIRED_MIN | 10.0 | # 一支部队脱离战斗所需的进度 |
| ESCAPE_PROGRESS_REQUIRED_PER_MANPOWER | 0.001 | # 每增加 1 个营或舰船，脱离所需进度增加此值 |
| ESCAPE_PROGRESS_GAIN_BASE | 1.0 | # 每个战斗回合进度增长的基础值 |
| ESCAPE_PROGRESS_GAIN_RANDOM_FACTOR | 2.5 | # 此值越高，每回合的进度变化越随机 |
| CHANCE_OF_POPULARITY_NARROW_VICTORY | 0.5 | # 险胜（开局兵力占优、结局兵力劣势）受声望影响的概率（0-1） |
| CHANCE_OF_POPULARITY_NORMAL_VICTORY | 0.1 | # 普通胜利（既非险胜也非英勇胜利的任何胜利）受声望影响的概率（0-1） |
| CHANCE_OF_POPULARITY_HEROIC_VICTORY | 1.0 | # 英勇胜利（开局面对威望更高国家时兵力处于劣势）受声望影响的概率（0-1） |
| POPULARITY_GAIN_NARROW_VICTORY | 10 | # 若随机概率判定为真，险胜获胜方获得的 commander_battle_end_victory modifier 的倍数 |
| POPULARITY_GAIN_NORMAL_VICTORY | 5 | # 若随机判定为真，普通胜利的获胜方应获得的 commander_battle_end_victory modifier 的倍数 |
| POPULARITY_GAIN_HEROIC_VICTORY | 20 | # 若随机判定为真，英勇胜利的获胜方应获得的 commander_battle_end_victory modifier 的倍数 |
| POPULARITY_GAIN_NARROW_LOSS | -10 | # 若随机判定为真，对方险胜时战败方应获得的 commander_battle_end_loss modifier 的倍数 |
| POPULARITY_GAIN_NORMAL_LOSS | -5 | # 若随机判定为真，对方普通胜利时战败方应获得的 commander_battle_end_loss modifier 的倍数 |
| POPULARITY_GAIN_HEROIC_LOSS | -20 | # 若随机判定为真，对方英勇胜利时战败方应获得的 commander_battle_end_loss modifier 的倍数 |
| POPULARITY_DECAY_MONTHS | 30 | # 战斗声望 modifier 经多少个月衰减 |
| SHIP_BATTLE_DAYS_BETWEEN_UPDATES | 5 | # 涉及单艘舰船的海战两次更新之间的天数 |
| SHIP_BATTLE_DESTROYED_SHIP_RATIO_RESIGN_THRESHOLD | 0.5 | # 使用单艘舰船时，舰队在被击毁舰船与初始参战舰船之比达到该值前退出战斗的阈值 |
| SHIP_REQUIRED_READINESS_TO_ACT | 100.0 | # 舰船需要达到多少战备度才能执行如攻击或撤退等行动 |
| SHIP_DEFAULT_READINESS_GAIN | 10 | # 若模板中未指定，则使用此默认战备度增量 |
| SHIP_INITIAL_READINESS | 0.0 | # 舰船在战斗开始时的战备度 |
| SHIP_ATTACK_BASE_MISS_CHANCE | 0.2 | # 舰船攻击另一艘舰船时的基础未命中概率。该值会进一步受舰船命中精度影响 |
| SHIP_ATTACK_MIN_MISS_CHANCE | 0.01 | # 舰船攻击时的最低未命中概率 |
| SHIP_WITHDRAW_BASE_CHANCE | 0.5 | # 舰船成功脱离战斗的基础概率。舰船的速度会加到该值上 |
| SHIP_WITHDRAW_SPEED_FACTOR | 1.0 | # 速度影响脱离概率时的系数 |
| ###### Withdraw Desire Calculation ###### ## Withdraw desire = ( Damage Desire + Zero Damage Hit Ratio Desire ) * ( 1 + Overwhelming Odds Desire + Exposed Desire + Raiding Desire ) # given that each term is applicable |  |  |
| SHIP_LIGHT_DAMAGE | 0.8 | # 舰船不同行为所对应的损伤阈值 |
| SHIP_MODERATE_DAMAGE | 0.5 |  |
| SHIP_SEVERE_DAMAGE | 0.25 |  |
| SHIP_WITHDRAW_DESIRE_LIGHT_DAMAGE | 0.05 | # 舰船基于所受损伤尝试脱离战斗的概率 |
| SHIP_WITHDRAW_DESIRE_MODERATE_DAMAGE | 0.20 |  |
| SHIP_WITHDRAW_DESIRE_SEVERE_DAMAGE | 0.80 |  |
| OVERWHELMING_ODDS_POWER_RATIO | 0.5 | # 实力比 = 我方实力 / 敌方实力。若实力比低于该阈值，则战斗被视为敌方具有压倒性优势，舰船更有可能脱离战斗 |
| SHIP_WITHDRAW_DESIRE_OVERWHELMING_ODDS_BASE | 0.1 | # 若我方实力比低于 OVERWHELMING_ODDS_POWER_RATIO，则开始为舰船的脱离意愿增加此数值。随着实力比降低，额外脱离意愿会线性插值增至 SHIP_WITHDRAW_DESIRE_OVERWHELMING_ODDS_MAX |
| SHIP_WITHDRAW_DESIRE_OVERWHELMING_ODDS_MAX | 0.5 | # 在理论实力比为 0 时，额外脱离意愿的最大值 |
| PRIORITY_SHIPS_EXPOSED_THRESHOLD | 0.5 | # 若战斗一方的总脆弱度 / 总护卫之比低于该值，则该方被视为其重点舰船处于暴露状态 |
| PRIORITY_SHIP_WITHDRAW_DESIRE_MULT_PRIORITY_SHIPS_EXPOSED | 0.2 | # 若我方重点舰船暴露，则我方重点舰船的脱离意愿乘以此系数 |
| SCREENING_SHIP_WITHDRAW_DESIRE_MULT_PRIORITY_SHIPS_EXPOSED | -0.2 # 若我方重点舰船暴露，则我方护卫舰船的脱离意愿乘以此系数 |  |
| PRIORITY_SHIPS_EXPOSED_FOR_RAIDING_THRESHOLD | 0.25 | # 对于袭击舰队，如果敌方的总脆弱度/总护航比值小于此值，则该方被视为暴露状态。 |
| RAIDING_SHIP_WITHDRAW_DESIRE_MULT_PRIORITY_SHIPS_EXPOSED | 0.25 | # 对于袭击舰队，如果敌方未处于暴露状态，将撤退意愿乘以此值 |
| ZERO_DAMAGE_HIT_RATIO_THRESHOLD | 0.5 | # 对于战斗的每一方，如果零伤害命中的数量占命中总数的比例超过此阈值，我们就会对撤退几率施加一个加成 |
| MIN_ATTACKS_ZERO_DAMAGE_HIT_PENALTY | 50 | ) |
| SHIP_WITHDRAW_DESIRE_HIGH_ZERO_DAMAGE_HIT_RATIO | 0.1 | # 如果我方造成的零伤害命中过多，则向撤退意愿增加此数值 |
| FLEET_UNCONNECTED_MISSION_AREA_TIMEOUT_DAYS | 30 | # 任务区域在被允许处于无效/未连接状态多少天后会被清理 |
| FLEET_INTERCEPT_CHANCE_BASE | 10.0 | # 舰队进行拦截的基础几率（0-100） |
| FLEET_RAID_SUPPLY_CHANCE_BASE | 10.0 | # 舰队进行补给袭击的基础几率（0-100） |
| NAVAL_BATTLE_LOG_INITIAL_SIZE_FACTOR | 8 | # 初始预留日志大小系数。该值乘以战斗中的舰船数量来估算所需的条目数。数值过大会分配过多数据，过小则需要多次扩展数组，速度较慢。 |
| NAVAL_BATTLE_LOG_ENTRIES_PER_PAGE | 20 | # 战斗日志界面中每页显示的海战日志条目数。 |
| NAVAL_BATTLE_CONDITION_DAMAGE_RANGE | 0.25 | # 当海战状况对一艘舰船施加伤害时，实际伤害将在 (1 - 此值) * 伤害 到 (1 + 此值) * 伤害 的范围内 |
| DEFAULT_NAVAL_BATTLE_CONDITION_TYPE | "naval_condition_calm_waters" | # 如果一场海战由于所有权重为 0 等原因无法选择有效的海战状况，则会覆盖选择结果并使用此海战状况。不过这只是备用方案，理想情况下所有海战状况都应有非零权重，并且应始终至少存在一种可能的状况 |
| HIGHLIGHTED_EVENT_INTERVAL_TURNS | 8 | # 重点事件重新评估之间的战斗回合数 |
| HIGHLIGHTED_EVENT_LOOKBACK_COUNT | 10 | # 每次评估所考虑的新日志条目最大数量 |
| HIGHLIGHTED_EVENT_WEIGHT_DAMAGE | 1.0 | # 对日志条目评分时乘以总伤害（船体 + 船员）的权重 |
| HIGHLIGHTED_EVENT_WEIGHT_FLAGSHIP | 500.0 | # 如果日志条目中涉及旗舰，则增加此额外权重 |
| HIGHLIGHTED_EVENT_WEIGHT_SINK | 100.0 | # 如果日志条目中有舰船被击沉，则增加此额外权重 |
### 战争

| Define | 默认值 | 开发者注释 |
|---|---|---|
| DEVASTATION_MAX | 100.0 |  |
| DEVASTATION_INCREASE_RATE | 0.1 | # 每日，随占领等级而变化 |
| DEVASTATION_DECAY_RATE | -0.0.25 | # 每日，在无占领时生效 |
| DEVASTATION_FROM_BATTLES | 0.1 | # 每场战斗 |
| AUTO_CAPITULATE_WAR_SUPPORT | -100 | # 当战争支持度低至此值时，国家将自动投降 |
| DAYS_BETWEEN_WAR_EXHAUSTION | 7 | # 每隔这么多天，战争支持度将按战争疲劳公式减少 |
| WAR_EXHAUSTION_BASE | 0.2 |  |
| WAR_EXHAUSTION_KIA_FACTOR | 4.0 | # 按伤亡相对总人力规模进行缩放 |
| WAR_EXHAUSTION_KIA_BASE_MULTIPLIER | 0.25 | # 来自伤亡的战争疲劳始终至少乘以该系数 |
| WAR_EXHAUSTION_KIA_BATTLES_LOST_MULTIPLIER | 0.75 | # 当我方 100% 的战斗失利时，来自伤亡的战争疲劳再乘以该系数 |
| WAR_EXHAUSTION_TURMOIL_FACTOR | 1.5 | # 在 100% 动荡时 |
| WAR_EXHAUSTION_CONTESTED_ENEMY_WARGOALS | 1.0 |  |
| WAR_EXHAUSTION_ANTI_WAR_LOBBY_CLOUT_FACTOR | 1.0 | # 在 100% 反对战争的游说集团政治力量时 |
| WAR_EXHAUSTION_PRO_WAR_LOBBY_CLOUT_FACTOR | -1.0 | # 在 100% 支持战争的游说集团政治力量时 |
| WAR_EXHAUSTION_MAX | 100 | # 战争疲劳永不会超过此值 |
| WAR_EXHAUSTION_MIN | 0 | # 战争疲劳永不会低于此值 |
| OCCUPATION_STATE_BASE_WEIGHT | 1 |  |
| OCCUPATION_STATE_POP_WEIGHT | 1 |  |
| OCCUPATION_STATE_INCORPORATED_WEIGHT | 10 |  |
| OCCUPATION_STATE_DEFENSIVE_BATTLE_VICTORY_SCORE | 50 | # 每个国家在赢得一场防御性战斗后获得的占领“点数” |
| OCCUPATION_STATE_CLEAR_OCCUPATION_FRACTION | 0.5 | # 用于清除本国州（若有）占领状况的占领分数比例。 |
| LAND_INVASION_TRAVEL_TIME_LIMIT_DAYS | 30 | # 部队编队进行陆上入侵最多可行进的天数 |
| LAND_INVASION_PREPARATION_DURATION_DAYS | 14 | # 自首支陆军抵达入侵前线起，需经过多少天才开始推进 |
| NAVAL_INVASION_PREPARATION_DURATION_DAYS | 14 | # 自首支陆军抵达海上入侵前线起，在海域未被敌方舰队封锁的情况下，需经过多少天才开始推进 |
| LAND_INVASION_MAX_LAND_BATTLE_DEFEATS_AT_ZERO_OCCUPATION | 3 | # 在零占领时陆战失利达到此次数，入侵即告失败 |
| NAVAL_INVASION_MAX_LAND_BATTLE_DEFEATS_AT_ZERO_OCCUPATION | 3 | # 在零占领时陆战失利达到此次数，海上入侵即告失败。 |
| NAVAL_INVASION_MIN_POWER_PROJECTION_RATIO_TO_BLOCK_LANDING | 0.25 | # 舰队需要达到何种实力才被视为“封锁”了海上入侵舰队 |
| STATE_CONQUEST_HOMELAND_AND_CLAIM_RADICALIZATION | 0.1 |  |
| STATE_CONQUEST_HOMELAND_AND_CLAIM_DEMILITARIZATION | 0.25 |  |
| STATE_CONQUEST_HOMELAND_OR_CLAIM_RADICALIZATION | 0.3 |  |
| STATE_CONQUEST_HOMELAND_OR_CLAIM_DEMILITARIZATION | 0.5 |  |
| STATE_CONQUEST_DEFAULT_RADICALIZATION | 0.5 |  |
| STATE_CONQUEST_DEFAULT_DEMILITARIZATION | 0.75 |  |
| STATE_PEACEFUL_ANNEXATION_RADICALIZATION_FACTOR | 0.25 | # 如果该州是因宗主国接受外交要求而被吞并的，则乘以此系数 |
| STATE_CONQUEST_KEEP_ALL | 0.0 |  |
| NUM_PROVINCES_FOR_ADVANCEMENT_SELECTION | 5 | # 在使用 front_battle_province_weight 为可能的推进省份计算权重后，仅保留权重最高的 X 个省份。此举是为了防止随机选中权重较低的元素。 |
### TravelNetwork

| Define | 默认值 | 开发者注释 |
|---|---|---|
| ARMY_CONNECTION_UNDEVELOPED_COST_MULT | 2.0 | # 未开发陆地连接的通行成本倍率 |
| ARMY_CONNECTION_UNDEVELOPED_HARSH_COST_MULT | 4.0 | # 恶劣环境（沙漠、山地等）中未开发陆地连接的通行成本倍率 |
| ARMY_CONNECTION_DIRT_ROAD_COST_MULT | 1.5 | # 土路陆地连接的通行成本倍率 |
| ARMY_CONNECTION_HARDENED_ROAD_COST_MULT | 1.25 | # 硬化道路陆地连接的通行成本倍率 |
| ARMY_CONNECTION_RAILWAY_COST_MULT | 1.0 | # 铁路陆地连接的通行成本倍率 |
| ARMY_CONNECTION_CHARTED_COST_MULT | 1.0 | # 海洋/近海水域连接的通行成本倍率 |
| ARMY_CONNECTION_CANAL_COST_MULT | 1.0 | # 运河水域连接的通行成本倍率 |
| ARMY_CONNECTION_STRAIT_CROSSING_COST_MULT | 4.0 | # 海峡跨越连接的通行成本倍率 |
| ARMY_DIRECT_CONNECTION_COST_MULT | 10.0 | # 在地图上从某位置直线路径往返（不经由通行节点连接）时的通行成本倍率 |
| ARMY_CONNECTION_DOCKING_COST | 300 | # 从港口节点前往码头节点的固定入坞/出坞成本（覆盖入坞连接长度） |
| ARMY_CONNECTION_STRAIT_CROSSING_COST | 100 | # 跨越海峡连接的固定额外成本 |
| FLEET_CONNECTION_UNDEVELOPED_COST_MULT | 100.0 | # 未开发陆地连接的通行成本倍率（舰队不使用） |
| FLEET_CONNECTION_UNDEVELOPED_HARSH_COST_MULT | 100.0 | # 恶劣环境（沙漠、山地等）中未开发陆地连接的通行成本倍率（舰队不使用） |
| FLEET_CONNECTION_DIRT_ROAD_COST_MULT | 100.0 | # 土路陆地连接的通行成本倍率（舰队不使用） |
| FLEET_CONNECTION_HARDENED_ROAD_COST_MULT | 100.0 | # 硬化道路陆地连接的通行成本倍率（舰队不使用） |
| FLEET_CONNECTION_RAILWAY_COST_MULT | 100.0 | # 铁路陆地连接的通行成本倍率（舰队不使用） |
| FLEET_CONNECTION_CHARTED_COST_MULT | 1.0 | # 海洋/近海水域连接的通行成本倍率 |
| FLEET_CONNECTION_CANAL_COST_MULT | 1.0 | # 运河水域连接的通行成本倍率 |
| FLEET_CONNECTION_STRAIT_CROSSING_COST_MULT | 100.0 | # 海峡跨越连接的通行成本倍率（舰队不使用） |
| FLEET_DIRECT_CONNECTION_COST_MULT | 4.0 | # 在地图上从某位置直线路径往返（不经由通行节点连接）时的通行成本倍率 |
| FLEET_CONNECTION_DOCKING_COST | 10 | # 从港口节点前往码头节点的固定入坞/出坞成本（覆盖入坞连接长度） |
| FLEET_CONNECTION_STRAIT_CROSSING_COST | 100 | # 跨越海峡连接的固定额外成本（舰队不使用） |
| DIRECT_CONNECTION_NODE_MAX_NODES | 10 | # 直线路径地图通行时，仅搜索最近的 X 个通行节点 |
| DIRECT_CONNECTION_NODE_SEARCH_DISTANCE | 1200 | # 从（起点/目标）地图点以直线路径寻路至某个通行节点所允许的默认距离（若未找到有效节点，则会扩大该距离） |
| DIRECT_CONNECTION_MAP_MAX_DISTANCE | 200 | # 起点与目标地图点之间以直线路径直接寻路所允许的最大距离 |
| STRAIT_CROSSING_NODE_CREATION_DISTANCE | 5 | # 考虑为海峡连接插入新的通行节点时，通行节点之间的最小距离 |
| FORMATION_REPATH_MAX_DAYS_EXTRA | 60 | # 编队自动重新寻路最多可耗费的天数（当通行中的通行权限发生变化时） |
| HARSH_ENVIRONMENT_TERRAIN_LABEL | "label_travel_harsh_environment" | # 将其中节点标记为处于恶劣环境的地形标签，会触发“UNDEVELOPED_HARSH”连接类型 |
| PAVED_ROAD_TECH | "paved_roads" | # 铺砌道路所需的技术 |
| PAVED_ROAD_MIN_INFRASTRUCTURE | 500.0 | # 铺砌道路的最低基础设施 |

### HarvestConditions（收获条件）

| Define | 默认值 | 开发者注释 |
|---|---|---|
| HARVEST_CONDITION_CHANCE_THRESHOLD | 0.2 | # 如果掷出的数值高于此值，我们会提前退出并跳过概率计算 |
| HARVEST_CONDITION_PERIOD | 3 | # 每隔多少个月检查每个州是否生成收获条件。1 = 每个月检查所有州，3 = 所有州在三个月内被检查一遍 |

### Text（文本）

| Define | 默认值 | 开发者注释 |
|---|---|---|
| DURATION_SHOW_YEARS_THRESHOLD | 1105 | # 持续时间至少达到这么多天时将以年显示 |
| DURATION_SHOW_MONTHS_THRESHOLD | 100 | # 持续时间至少达到这么多天时将以月显示 |
| DURATION_SHOW_WEEKS_THRESHOLD | 15 | # 持续时间至少达到这么多天时将以周显示 |

### Debug（调试）

| Define | 默认值 | 开发者注释 |
|---|---|---|
| CASUALTY_LOG_EXPIRE_TIME_DAYS | 30 | # 单位和建筑的伤亡日志将在这么多天之后被清理 |
| CASUALTY_LOG_NUM_LAST_ENTRIES_VISIBLE | 10 | # 伤亡日志列表中显示的伤亡事件最大数量 |
| OCCUPATION_TOOL_DELTA | 0.25 | # OccupationTool（占领工具）每次增加/减少的占领百分比 |

## 00_ai

### AI

影响 AI 行为的 defines。

| Define | 默认值 | 开发者注释 |
|---|---|---|
| DEFAULT_STRATEGY_STRING | "ai_strategy_default" |  |
| STRATEGY_RANDOM_FACTOR | 20.0 | # 此值越高，AI 策略选择的随机性越强 |
| TICKS_FOR_FULL_SPENDING_VARIABLES_UPDATE | 100 | # 此值越高，AI 完整刷新其支出变量的频率越低 |
| NUM_FAILED_MONEY_SPENDING_ATTEMPTS_FOR_UPDATE | 50 | # 在尝试更改金钱支出/建造政府建筑失败这么多次后，强制更新金钱支出优先级 |
| NUM_FAILED_AUTHORITY_SPENDING_ATTEMPTS_FOR_UPDATE | 20 | # 在尝试更改权威力支出失败这么多次后，强制更新权威力支出优先级 |
| # 当一个潜在的 AI 建筑支出完成其状态计算后，在这两个值之间随机设置一个 tick 数，作为下次更新的时间 # 在此 tick 数过去之前，除非有特定原因需要更新状态，我们只更新分数并保持状态不变 |  |  |
| MIN_TICKS_TO_UPDATE_BUILDING_SPENDING_STATE | 100 |  |
| MAX_TICKS_TO_UPDATE_BUILDING_SPENDING_STATE | 200 |  |
| MIN_SUBJECT_TYPE_VALUE | 1 | # 附属国类型的 ai_value 永不低于此值 |
| GOVERNMENT_MONEY_SPENDING_ENABLED | yes | # 如果此项设为 no，政府金钱支出的 AI 将被禁用 |
| GOVERNMENT_AUTHORITY_SPENDING_ENABLED | yes | # 如果此项设为 no，权威力支出的 AI 将被禁用 |
| TAX_LEVEL_CHANGES_ENABLED | yes | # 如果此项设为 no，AI 将不会更改其税收等级（但若 GOVERNMENT_AUTHORITY_SPENDING_ENABLED = yes，仍可能使用消费税） |
| PRODUCTION_BUILDING_CONSTRUCTION_ENABLED | yes | # 如果此项设为 no，国家层面的 AI 将不会建造任何生产建筑 |
| AUTONOMOUS_INVESTMENT_CONSTRUCTION_ENABLED | yes | # 如果此项设为 no，即使相应的游戏规则已启用，自主投资 AI 也不会建造任何东西 |
| CHANGE_STRATEGY_THRESHOLD | 100 | # 当“变更点”达到此阈值时，AI 将重新掷出新的策略 |
| CHANGE_STRATEGY_INCREASE_WEEKLY_CHANCE | 20 | # AI 每周获得一个用于掷出新策略的“变更点”的概率（1 = 1%） |
| CHANGE_STRATEGY_POLITICAL_NEW_RULER | 100 | # 当一个国家迎来新统治者时，每个策略增加多少“变更点” |
| CHANGE_STRATEGY_POLITICAL_REGIME_CHANGE | 100 | # 当一个国家成为政权更迭的目标时，为其每项战略增加多少“变更点数” |
| CHANGE_STRATEGY_POLITICAL_LAW_ENACTED | 25 | # 当一部法律颁布时，为政治战略增加多少“变更点数” |
| CHANGE_STRATEGY_DIPLOMATIC_STATE_GAINED_OR_LOST | 10 | # 当获得或失去一个州时，为外交战略增加多少“变更点数” |
| CHANGE_STRATEGY_DIPLOMATIC_UNIFICATION_CANDIDATE | 100 | # 当我们成为或不再是统一候选人时，为外交战略增加多少“变更点数” |
| CHANGE_STRATEGY_DIPLOMATIC_LIBERTY_DESIRE_CHANGE | 2 | # 当独立倾向变化时，为外交战略增加多少“变更点数”（乘以变化的幅度） |
| COUNTRY_GOAL_STRATEGIC_UPDATE_COUNT | 5 | # 每天有多少个 AI 设定其保护评分 |
| COUNTRY_GOAL_ADJUSTMENT_UPDATE_COUNT | 50 | # 每天有多少个 AI 调整其敌对/友好/威胁评分、邻国/相关性状态以及态度 |
| DECLARE_BANKRUPTCY_MIN_DAYS_IN_DEFAULT | 30 | # 在违约这么多天之后，AI 将宣布破产 |
| DECLARE_BANKRUPTCY_COOLDOWN_DAYS | 365 | # 如果 AI 宣布破产，在这些天内不会再次破产，因为连锁破产会使所有人都变成激进派 |
| BASE_AGGRESSION | 0.25 | # 每次检查目标时，AI 考虑发起外交博弈的基础概率（1 = 1%） |
| UNIFICATION_AGGRESSION_MULT_HIGHER_TIER | 20 | # 在计算 AI 是否应尝试发起统一/领导权博弈时，如果该国最终会建立一个更高等级的国家，其侵略性乘以该系数 |
| UNIFICATION_AGGRESSION_MULT_SAME_TIER | 0.1 | # 在计算 AI 是否应尝试发起统一/领导权博弈时，如果该国最终会建立一个相同等级的国家，其侵略性乘以该系数 |
| DIPLO_PROPOSAL_DAYS_LEFT_MAX | 28 | # 当剩余天数超过此数值时，AI 不会回应提案（应与 DIPLOMATIC_ACTION_PENDING_APPROVAL_DAYS 相对应） |
| DIPLO_PROPOSAL_DAYS_LEFT_MIN | 20 | # 当剩余天数不多于此数值时，AI 必定会回应提案（应与 DIPLOMATIC_ACTION_PENDING_APPROVAL_DAYS 相对应） |
| DIPLO_PROPOSAL_ANSWER_CHANCE | 5 | # AI 每次 tick 回应提案的概率（1 = 1%） |
| DIPLO_PROPOSAL_TO_PLAYER_COOLDOWN_MONTHS | 120 | # 在这么多个月内不会向玩家提出完全相同的提案 |
| DIPLO_PROPOSAL_LIKELY_NON_ACCEPTED_COOLDOWN_MONTHS | 120 | # 当 AI 掷骰决定是否尝试一个它认为会被拒绝的提案时，在此时间内不再尝试 |
| DIPLO_PROPOSAL_LIKELY_NON_ACCEPTED_TREATY_COOLDOWN_MONTHS | 12 | # 当 AI 向另一个 AI 提议条约失败时，等待这么长时间后才向同一国家再次尝试 |
| DIPLO_PROPOSAL_NO_OBLIGATION_COOLDOWN_MONTHS | 120 | # 如果 AI 决定不为某个提案提供义务，则记住该决定这么多个月 |
| DIPLO_PROPOSAL_ACCEPT_THRESHOLD | 1 | # 对于不带 uses_random_approval 标志的外交行动，接受度达到或超过此数值时，AI 对提案表示同意。每高出一点，接受带 uses_random_approval 标志或条约提案的概率就增加 |
| DIPLO_PROPOSAL_HALFWAY_RANDOM_ACCEPTANCE_THRESHOLD | 10 | # 对于带 uses_random_approval 标志的外交行动或条约提案，接受度达到或超过此数值时，AI 有 50% 的概率接受，并在提出该提案时将其视为会被接受 |
| DIPLO_PROPOSAL_GUARANTEED_RANDOM_ACCEPTANCE_THRESHOLD | 30 | # 对于带 uses_random_approval 标志的外交行动或条约提案，接受度达到或超过此数值时，AI 必定接受 |
| DIPLO_PROPOSAL_BREAK_THRESHOLD | -100 | # 接受度达到或低于此数值时，AI 会撕毁现有条约 |
| DIPLO_PROPOSAL_TRANSFER_PACT_RELUCTANCE | 25 | # 在转让条约提案中，将此值加到现有条约的接受值上 |
| OBLIGATION_RECENTLY_REPUDIATED_DESIRE_MULT | 0.1 | # 如果提供义务的国家近期曾拒不履行另一项义务，则将 AI 对该义务的渴望乘以此系数 |
| DIPLO_ACCEPTANCE_CALL_IN_OBLIGATION | 50 | # 在召唤履行义务时，将此接受值加到外交行动上 |
| DIPLO_ACCEPTANCE_CALL_IN_OBLIGATION_RECENTLY_REPUDIATED | 25 | # 如果本国近期曾拒不履行另一项义务，则在召唤履行义务时改用此接受值而非上述值 |
| DIPLO_BREAK_PACT_WEIGHT | 1000 |  |
| DIPLOMATIC_DEMAND_ALWAYS_ACCEPT_THRESHOLD | 100 | # 当接受值达到此数值时，AI 将始终屈服于外交要求。如果低于此值但高于 0，则按比例随机决定是否接受 |
| DIPLOMATIC_DEMAND_DAYS_LEFT_MAX | 13 | # 当剩余天数超过此数值时，AI 不会回应要求（应与 DIPLOMATIC_DEMAND_PENDING_APPROVAL_DAYS 对应） |
| DIPLOMATIC_DEMAND_DAYS_LEFT_MIN | 7 | # 当剩余天数不多于此数值时，AI 必定回应要求（应与 DIPLOMATIC_DEMAND_PENDING_APPROVAL_DAYS 对应） |
| DIPLOMATIC_DEMAND_ANSWER_CHANCE | 10 | # AI 每次刻度回应要求的概率（1 = 1%） |
| DIPLOMATIC_DEMAND_ACCEPTANCE_BASE | -50 |  |
| DIPLOMATIC_DEMAND_ACCEPTANCE_WARGOAL_IMPACT | -1 | # 随所要求战争目标的机动点数成本而缩放 |
| DIPLOMATIC_DEMAND_ACCEPTANCE_MILITARY_POWER_SCALE | 4.0 | # 当相对预期军力达到此数值时，DIPLOMATIC_DEMAND_ACCEPTANCE_MILITARY_POWER_FACTOR 的最大/最小值生效 |
| DIPLOMATIC_DEMAND_ACCEPTANCE_MILITARY_POWER_FACTOR | 100 | # 随提出要求国家在潜在博弈中的相对预期军力而缩放，最大为此值，最小为此值 * -1 |
| DIPLOMATIC_DEMAND_ACCEPTANCE_INCORPORATED_STATE_FACTOR | -25 | # 如果战争目标是要求对方割让一个已整合州，则将此值加到接受值上 |
| DIPLOMATIC_DEMAND_ACCEPTANCE_SUBJUGATION_FACTOR | 0.5 | # 如果战争目标是要求对方成为附属国，则将此系数乘以该国成为指定类型附属国的意愿 |
| DIPLOMATIC_DEMAND_ACCEPTANCE_ANNEXATION_FACTOR | -75 | # 如果战争目标是要求完全吞并对方，则将此值加到接受值上 |
| DIPLOMATIC_DEMAND_ACCEPTANCE_LOYAL_SUBJECT_FACTOR | 75 | # 宗主国向忠诚附属国提出要求时，将此值加到接受值上 |
| INFLUENCE_DEFICIT_RECOVER_INFLUENCE_BASE_VALUE | 50 | # 加到我们将要撕毁的条约或协约的评分上，以恢复影响力 |
| INFLUENCE_DEFICIT_RECOVER_INFLUENCE_RANDOM_FACTOR | 1.0 | # 此值越高，AI 因影响力赤字而撕毁协约/条约的行为越随机 |
| INFLUENCE_DEFICIT_RECOVER_INFLUENCE_OVER_SPENDING_LIMIT_MULT | 0.1 | # 处于影响力赤字时，AI 将超出其行动类型支出上限的协约价值乘以此系数 |
| MIN_AVAILABLE_LABOR_FOR_NEW_BUILDING | 5000 | # 如果州的可用劳动力低于此值，我们建造建筑的可能性应大幅降低（乘以 1 + 正在进行的建造数量） |
| # 编队单位数量少于以下三个值中最小者时，不应为其招募指挥官 |  |  |
| MIN_COMBAT_UNITS_FOR_COMMANDER_ABSOLUTE | 5 | # 作战单位的绝对数量 |
| MIN_COMBAT_UNITS_FOR_COMMANDER_ABSOLUTE_MARINES | 3 | # 海军陆战队标记编队中作战单位的绝对数量，小于等于上述值 |
| MIN_COMBAT_UNITS_FOR_COMMANDER_RELATIVE | 0.2 | # 作战单位相对于总陆军规模的数量 |
| # 编队单位数量至少达到以下两个值中较小者时，应始终拥有至少两名指挥官，以便动态拆分以覆盖多条前线 |  |  |
| MIN_COMBAT_UNITS_FOR_MULTIPLE_COMMANDERS_ABSOLUTE | 10 | # 作战单位的绝对数量 |
| MIN_COMBAT_UNITS_FOR_MULTIPLE_COMMANDERS_RELATIVE | 0.5 | # 相对陆军总规模的作战单位数量 |
| RETIRE_COMMANDER_INTERACTION_KEY | "retire_commander" | AI 会使用该人物互动来让多余的指挥官退役 |
| COMMANDER_DESIRED_RANK_DISPARITY_IN_ARMY | 1 | # 如果一支陆军中任意两位将军之间的军衔差距至少未达到此值，则优先晋升而非招募新指挥官 |
| COMMANDER_DESIRED_RANK_DISPARITY_IN_FLEET | 1 | # 如果一支舰队中任意两位海军上将之间的军衔差距至少未达到此值，则优先晋升而非招募新指挥官 |
| RECRUITABLE_COMMANDER_BASE_SCORE | 100 | # 分配给候选池中每名可招募指挥官的基础分数 |
| RECRUITABLE_COMMANDER_RANDOM_FACTOR | 3.0 | # 此值越高，AI 招募选择的随机性越大 |
| RECRUITABLE_COMMANDER_SKILL_TRAIT_SCORE | 25 | # 可招募指挥官的技能特质总价值乘以此系数 |
| RECRUITABLE_COMMANDER_PERSONALITY_TRAIT_SCORE | 0 | # 可招募指挥官的性格特质总价值乘以此系数 |
| RECRUITABLE_COMMANDER_CONDITION_TRAIT_SCORE | -25 | # 可招募指挥官的状态特质总价值乘以此系数 |
| RECRUITABLE_COMMANDER_FAVORED_IG_FACTOR | 1.5 | # 如果可招募指挥官来自 AI 偏好的利益集团（IG），分数乘以此系数 |
| RECRUITABLE_COMMANDER_DISFAVORED_IG_FACTOR | 0.5 | # 如果可招募指挥官来自 AI 厌恶的利益集团（IG），分数乘以此系数 |
| MOBILIZATION_OPTION_RANDOM_FACTOR | 0.5 | # 此值越高，AI 在选择激活哪些动员选项时越随机 |
| MOBILIZATION_OPTION_MONEY_COST_FACTOR | 20 | # 当判断 AI 是否应激活某动员选项时，将激活的金钱成本乘以此系数，并与 AI 评估价值比较以判断是否值得 |
| MOBILIZATION_OPTION_NUM_ACTIVE_OPTIONS_DIVISOR | 0.25 | # 将每个未激活动员选项的价值除以（1 + 已激活选项数量 * 此系数） |
| MOBILIZATION_OPTION_GOODS_SHORTAGE_MULT | 0.0 | # 若其任一输入商品存在短缺，将动员选项的价值乘以此系数 |
| MOBILIZATION_BASE_DESIRED_RATIO_TO_ENEMY | 0.5 | # AI 希望其动员陆军总战力等于敌方动员陆军战力 * 此系数 |
| MOBILIZATION_MAIN_ATTACKER_ADDED_RATIO | 1.0 | # 战争中主要进攻方在期望比例上加上此值 |
| MOBILIZATION_MAIN_DEFENDER_ADDED_RATIO | 1.0 | # 战争中主要防守方在期望比例上加上此值 |
| MOBILIZATION_LOYAL_SUBJECT_OF_MAIN_PARTICIPANT_ADDED_RATIO | 0.75 | # 战争中主要进攻方/防守方的忠诚附属国在期望比例上加上此值 |
| MOBILIZATION_PEACE_NEGOTIATOR_ADDED_RATIO | 0.5 | # 任何已经或将成为和谈谈判国（但非主要进攻方或防守方）的国家在期望比例上加上此值 |
| MOBILIZATION_LOCAL_FRONTS_ADDED_RATIO | 0.5 | # 任何拥有至少一条本土前线的国家在期望比例上加上此值 |
| MOBILIZATION_UNINCORPORATED_OCCUPATION_ADDED_RATIO | 0.5 | # 任何其非整合州正被占领的国家在期望比例上加上此值 |
| MOBILIZATION_INCORPORATED_OCCUPATION_ADDED_RATIO | 1.0 | # 任何其整合州正被占领的国家在期望比例上加上此值（覆盖非整合州被占领的系数） |
| MOBILIZATION_EXISTENTIAL_WAR_FACTOR | 2.0 | # 若 AI 处于存亡战争/外交博弈中（和谈后可能亡国），其期望动员比例加上此值 |
| MOBILIZATION_MINOR_ALLY_MAX_RELATIVE_POWER | 0.15 | # 若要被视为次要盟友，一个国家的战力必须小于等于同盟总战力的此比例，且不得拥有任何前线。 |
| MOBILIZATION_MINOR_ALLY_ADVANTAGE_TO_NOT_MOBILIZE | 2.0 | # 若某个次要盟友一方在不计入其军队的情况下已拥有至少这一数值的军力优势，则不必动员 |
| MOBILIZATION_MIN_ESCALATION_START | 50 | # 在博弈中的紧张度达到此数值之前，AI 仅会在敌方动员时作为回应进行动员（基础值） |
| MOBILIZATION_MIN_ESCALATION_BOLDNESS_FACTOR | 0.2 | # 果敢度乘以此数值后，从 MOBILIZATION_MIN_MOBILIZATION_ESCALATION_START 中减去 |
| MOBILIZATION_MIN_MOBILIZATION_PEACE_NEGOTIATOR | 0.15 | # 若 AI 是或将成为和谈谈判方，则始终至少动员这一数量的部队 |
| MOBILIZATION_MIN_MOBILIZATION_LOYAL_SUBJECT_OF_MAIN_PARTICIPANT | 0.15 | # 若 AI 是主要进攻方/防守方的忠诚附属国，则始终至少动员这一数量的部队 |
| MOBILIZATION_MIN_MOBILIZATION_TERRITORIAL_RISK | 0.15 | # 若 AI 可能因战争/博弈失去领土，则始终至少动员这一数量的部队 |
| MOBILIZATION_MIN_MOBILIZATION_UNINCORPORATED_OCCUPATION | 0.25 | # 若 AI 的非整合州被占领，则始终至少动员这一数量的部队 |
| MOBILIZATION_MIN_MOBILIZATION_INCORPORATED_OCCUPATION | 0.5 | # 若 AI 的整合州被占领，则始终至少动员这一数量的部队（覆盖非整合州被占领时的乘数） |
| MOBILIZATION_MIN_MOBILIZATION_LOCAL_FRONTS | 0.25 | # 若 AI 拥有任何本地前线，则始终至少动员这一数量的部队 |
| MOBILIZATION_MIN_MOBILIZATION_CONTAINMENT_WAR | 1.0 | # 若 AI 参与遏制战争，则始终至少动员这一数量的部队 |
| CONSCRIPTION_INSUFFICIENT_FORCES_FACTOR | 1 | # AI 每有 1% 的动员无法达成，就征募基础为 1% * 此数值的征召兵 |
| CONSCRIPTION_RELATIVE_CONSCRIPTED_COMBAT_POWER_DIVISOR | 1 | # 征召部队的战斗力占比乘以此数值，然后 CONSCRIPTION_INSUFFICIENT_FORCES_FACTOR 的结果除以（1 + 该结果） |
| CONSCRIPTION_SMALL_STANDING_ARMY_THRESHOLD | 0.75 | # 若 AI 的征召战斗力占总战斗力的比例高于此数值，则受以下系数影响 |
| CONSCRIPTION_SMALL_STANDING_ARMY_MIN_CONSCRIPTS_FACTOR | 0.02 | # 征召战斗力占比每超出 CONSCRIPTION_SMALL_STANDING_ARMY_THRESHOLD 1%，就始终至少征募这一比例的征召兵 |
| MIN_GOVERNMENT_LEGITIMACY | 25 | # 若合法性低于此数值，考虑将并不真正喜欢的利益集团纳入政府 |
| DESIRED_GOVERNMENT_LEGITIMACY | 50 | # 对拥有至少此数值合法性的政府给予加分 |
| REFORM_GOVERNMENT_MONTHS_BETWEEN_CHANGES | 30 | # 若 AI 国内没有选举，则不会以高于此频率的间隔考虑更改政府构成，以避免产生大量激进派 |
| REFORM_GOVERNMENT_NUM_OPTIONS_TO_CHECK | 5 | # AI 会考虑多少种合法性最高的可能政府组合 |
| REFORM_GOVERNMENT_STICKINESS | 1.25 | # 在考虑是否改组政府时，将当前政府的评分乘以此数值 |
| REFORM_GOVERNMENT_PRO_IG_CLOUT_FACTOR | 1.0 | # 在为利益集团入阁评分时，将其加入评分乘数（按政治力量加权） |
| REFORM_GOVERNMENT_ANTI_IG_CLOUT_FACTOR | 10.0 | # 在为利益集团入阁评分时，将其加入评分除数（按政治力量加权） |
| REFORM_GOVERNMENT_ABOVE_DESIRED_LEGITIMACY_FACTOR | 1.5 | # 将达到期望合法性阈值的政府评分乘以此数值 |
| REFORM_GOVERNMENT_BELOW_MIN_LEGITIMACY_FACTOR | 0.1 | # 若某个政府选项的合法性低于 MIN_GOVERNMENT_LEGITIMACY，则将其评分乘以此数值 |
| MAX_CANDIDATES_TO_COMBINE_FOR_GOVERNMENT_ALTERNATIVES | 8 | # 检查政府备选方案时可组合的利益集团或政党的最大数量。8 意味着 2^8=256 种可能的政府组合。更高的值会对性能产生指数级影响 |
| REGIME_CHANGE_NUM_GOVERNMENT_OPTIONS_TO_CHECK | 100 | # 在政权更迭期间尝试组建政府时取代 REFORM_GOVERNMENT_NUM_OPTIONS_TO_CHECK——由于很少执行，该值可以设得很高 |
| REGIME_CHANGE_MIN_GOVERNMENT_LEGITIMACY | 5 | # 在政权更迭中为政府评估利益集团时，取代 MIN_GOVERNMENT_LEGITIMACY |
| REGIME_CHANGE_REFORM_GOVERNMENT_STICKINESS | 0.1 | # 在政权更迭中为政府评估利益集团时，取代 REFORM_GOVERNMENT_STICKINESS |
| REGIME_CHANGE_REFORM_GOVERNMENT_CLOUT_FACTOR_MULTIPLIER | 100.0 | # 在政权更迭中为政府评估利益集团时，将支持/反对 AI 的政治力量因素乘以此值 |
| IDEOLOGICAL_OPINION_ACCEPTABLE_PROGRESSIVENESS_DIFFERENCE | 25 | # 若两个国家的进步度差异小于或等于此值，则增加正面意识形态观点，否则增加负面 |
| IDEOLOGICAL_OPINION_CURRENT_PROGRESSIVENESS_SAME_FACTOR | 2.5 | # 应用于当前进步度差异小于或等于 IDEOLOGICAL_OPINION_ACCEPTABLE_PROGRESSIVENESS_DIFFERENCE 的每个法律类别 |
| IDEOLOGICAL_OPINION_CURRENT_PROGRESSIVENESS_DIFF_FACTOR | -0.05 | # 在当前进步度差异高于 IDEOLOGICAL_OPINION_ACCEPTABLE_PROGRESSIVENESS_DIFFERENCE 时，每个类别中当前已颁布法律的进步度差异按此数值加权计入意识形态观点 |
| IDEOLOGICAL_OPINION_IDEAL_PROGRESSIVENESS_SAME_FACTOR | 2.5 | # 应用于当前进步度差异小于或等于 IDEOLOGICAL_OPINION_ACCEPTABLE_PROGRESSIVENESS_DIFFERENCE 的每个法律类别 |
| IDEOLOGICAL_OPINION_IDEAL_PROGRESSIVENESS_DIFF_FACTOR | -0.05 | # 在理想进步度差异高于 IDEOLOGICAL_OPINION_ACCEPTABLE_PROGRESSIVENESS_DIFFERENCE 时，每个类别中政府理想法律的进步度差异按此数值加权计入意识形态观点 |
| UNIFICATION_MIN_SUPPORT_SCORE | 50 | # 支持某一国家组建候选国的支持度需要至少比所有竞争者高出此值才支持统一 |
| UNIFICATION_BASE_VALUE | 0 |  |
| UNIFICATION_SUPPORT_INVALID_TARGET_FACTOR | -1000 | # 当国家不是统一博弈的有效目标时的统一支持度因素 |
| UNIFICATION_SUPPORTER_DEFAULT_RANK_VALUE | 4 | # 计算支持者等级因素时，等级值与此值比较 |
| UNIFICATION_SUPPORTER_RANK_FACTOR | -10 | # 乘以等级值与支持者默认等级之差 |
| UNIFICATION_CANDIDATE_DEFAULT_RANK_VALUE | 6 | # 计算候选者等级因素时，等级值与此值比较 |
| UNIFICATION_CANDIDATE_RANK_FACTOR | 10 | # 乘以等级值与候选者默认等级之差 |
| UNIFICATION_RELATIONS_HOSTILE_FACTOR | -50 |  |
| UNIFICATION_RELATIONS_COLD_FACTOR | -25 |  |
| UNIFICATION_RELATIONS_POOR_FACTOR | -10 |  |
| UNIFICATION_RELATIONS_CORDIAL_FACTOR | 10 |  |
| UNIFICATION_RELATIONS_AMICABLE_FACTOR | 25 |  |
| UNIFICATION_RELATIONS_FRIENDLY_FACTOR | 50 |  |
| UNIFICATION_ATTITUDE_DISINTERESTED_FACTOR | -25 |  |
| UNIFICATION_ATTITUDE_CAUTIOUS_FACTOR | -25 |  |
| UNIFICATION_ATTITUDE_CONCILIATORY_FACTOR | 0 |  |
| UNIFICATION_ATTITUDE_COOPERATIVE_FACTOR | 25 |  |
| UNIFICATION_ATTITUDE_GENIAL_FACTOR | 50 |  |
| UNIFICATION_ATTITUDE_WARY_FACTOR | -50 |  |
| UNIFICATION_ATTITUDE_BELLIGERENT_FACTOR | -100 |  |
| UNIFICATION_ATTITUDE_ANTAGONISTIC_FACTOR | -100 |  |
| UNIFICATION_ATTITUDE_LOYAL_FACTOR | 100 |  |
| UNIFICATION_ATTITUDE_ALOOF_FACTOR | 25 |  |
| UNIFICATION_ATTITUDE_DEFIANT_FACTOR | -50 |  |
| UNIFICATION_ATTITUDE_REBELLIOUS_FACTOR | -100 |  |
| UNIFICATION_ATTITUDE_PROTECTIVE_FACTOR | -50 |  |
| UNIFICATION_ATTITUDE_DOMINEERING_FACTOR | -100 |  |
| UNIFICATION_POWER_BLOC_FACTOR | 25 | # 若两国处于同一强权集团，则增加此数值的统一支持度 |
| STRATEGIC_REGION_STANCES_RANDOM_FACTOR | 1 |  |
| STRATEGIC_REGION_STANCES_STICKINESS | 2 | # 在检查是否改变立场时，乘以当前立场分数 |
| CHANGE_TAX_START_OF_GAME_DAYS_TO_WAIT | 30 | # 在书签初始化后的这段时间内不更改任何税收等级，以便经济状态有机会稳定下来 |
| CHANGE_TAX_SIGNIFICANT_DEBT_THRESHOLD | 0.1 | # 当债务与最大信贷的比值达到此数值时，下述“重大债务”逻辑开始生效 |
| RAISE_TAX_TO_DESIRED_INCOME_THRESHOLD | 1.25 | # 若收支比低于或等于此数值，且税收等级低于期望等级，则提高税收 |
| RAISE_TAX_ABOVE_DESIRED_INCOME_MAX_GOLD_RESERVES_THRESHOLD | 0.1 | # 若黄金储备至少达到此比例，则不将税收提高到期望等级以上 |
| RAISE_TAX_ABOVE_DESIRED_INCOME_NO_DEBT_THRESHOLD | 0.9 | # 若收支比低于或等于此数值，无债务或债务很少，且税收等级达到或高于期望等级，则提高税收 |
| RAISE_TAX_ABOVE_DESIRED_INCOME_WITH_DEBT_THRESHOLD | 1.1 | # 若收支比低于或等于此数值，存在重大债务，且税收等级达到或高于期望等级，则提高税收 |
| LOWER_TAX_TO_DESIRED_INCOME_NO_DEBT_THRESHOLD | 1.25 | # 若收支比高于或等于此数值，无债务或债务很少，且税收等级达到或高于期望等级，则降低税收 |
| LOWER_TAX_TO_DESIRED_INCOME_WITH_DEBT_THRESHOLD | 1.5 | # 若收支比高于或等于此数值，存在重大债务，且税收等级达到或高于期望等级，则降低税收 |
| LOWER_TAX_BELOW_DESIRED_INCOME_THRESHOLD | 2.0 | # 若收支比高于或等于此数值，且税收等级低于期望等级，则降低税收 |
| RAISE_TAX_HIGH_DEBT_OVERRIDE_RATIO | 0.5 | # 债务达到此数值时，可动用任意税收等级来应对 |
| CONSTRUCTION_MAX_NUM_PRODUCTION_BUILDING_CONSTRUCTIONS_BASE | 1 | # 若国家排队的生产建筑建造数量达到此数值，则不再添加（基础值） |
| CONSTRUCTION_MAX_NUM_PRODUCTION_BUILDING_CONSTRUCTIONS_SCALED | 0.05 | # 若国家排队的生产建筑建造数量达到此数值，则不再添加（按建造产出缩放） |
| CONSTRUCTION_MAX_NUM_PRODUCTION_BUILDING_CONSTRUCTIONS_SCALED_MAX | 999 | # CONSTRUCTION_MAX_NUM_PRODUCTION_BUILDING_CONSTRUCTIONS_SCALED 不能高于此数值 |
| CONSTRUCTION_MAX_NUM_GOVERNMENT_BUILDING_CONSTRUCTIONS_BASE | 1 | # 若国家排队的政府建筑建造数量达到此数值，则不再添加（基础值） |
| CONSTRUCTION_MAX_NUM_GOVERNMENT_BUILDING_CONSTRUCTIONS_SCALED | 0.05 | # 若国家排队的政府建筑建造数量达到此数值，则不再添加（按建造产出缩放） |
| CONSTRUCTION_MAX_NUM_GOVERNMENT_BUILDING_CONSTRUCTIONS_SCALED_MAX | 99 | # CONSTRUCTION_MAX_NUM_GOVERNMENT_BUILDING_CONSTRUCTIONS_SCALED 不能高于此数值 |
| CONSTRUCTION_RESERVES_NEW_CONSTRUCTIONS | 0.1 | # 若加入新建造费用后黄金储备低于此数值，则不将其加入队列 |
| CONSTRUCTION_DEBT_RESUME | 0.2 | # 若建造已暂停，当债务相对债务上限降低到此比例时恢复建造 |
| CONSTRUCTION_DEBT_PAUSE | 0.4 | # 若相对债务上限的债务达到此比例，暂停所有非关键建造 |
| CONSTRUCTION_DEBT_RESUME_CRITICAL_CONSTRUCTION | 0.95 | # 若关键建造已暂停，当债务相对上限降低到此比例时恢复建造 |
| CONSTRUCTION_DEBT_PAUSE_CRITICAL_CONSTRUCTION | 0.99 | # 若相对债务达到债务上限的这一比例，暂停所有紧急（critical）建造 |
| CONTAINMENT_PLAY_PARTICIPATION_RANK | 7 | # 排名达到或高于该等级的国家应热衷于加入遏制博弈以打压威胁 |
| START_DIPLO_PLAY_RANDOM_FACTOR | 2.0 | # 此值越高，AI 在发起外交博弈时选择目标越随机 |
| START_DIPLO_PLAY_ALLY_STRENGTH_WEIGHT | 0.75 | # 计算确定会加入某一方的参战国时，按此比例计入其军力 |
| START_DIPLO_PLAY_LIKELY_ALLY_STRENGTH_WEIGHT | 0.5 | # 计算很可能会加入某一方的参战国时，按此比例计入其军力 |
| DIPLO_PLAY_BACK_DOWN_CHANCE_THRESHOLD | 0 | # 若（信心 + 胆量）低于此值，考虑让步退让 |
| DIPLO_PLAY_BACK_DOWN_CHANCE_ESCALATION | 30 | # 升级度超过此值后，AI 会考虑退让 |
| DIPLO_PLAY_BACK_DOWN_INCREASE_CHANCE_THRESHOLD | -50 | # 若（信心 + 胆量）低于此值，提高退让的概率 |
| DIPLO_PLAY_BACK_DOWN_INCREASE_CHANCE_MULTIPLIER | 4.0 | # 若（信心 + 胆量）低于 DIPLO_PLAY_BACK_DOWN_INCREASE_CHANCE_THRESHOLD，按此倍数提高退让的概率 |
| DIPLO_PLAY_BACK_DOWN_GUARANTEED_THRESHOLD | -75 | # 若（信心 + 胆量）低于此值，必定在博弈开战前退让 |
| DIPLO_PLAY_BACK_DOWN_GUARANTEED_ESCALATION | 95 | # 升级度超过此值后，若 AI 本应退让，则必定退让 |
| DIPLO_PLAY_BACK_DOWN_CHANCE_LOW_ESCALATION | 0.4 | # 1.0 = 1%（每日概率）——用于对战争计时开始之前 |
| DIPLO_PLAY_BACK_DOWN_CHANCE_HIGH_ESCALATION | 2.0 | # 1.0 = 1%（每日概率）——用于对战争计时开始之后 |
| DIPLO_PLAY_BACK_DOWN_CHANCE_WAR_LOSSES_MULT | 1.5 | # 因额外战争目标要求而退让的概率乘以 1 +（额外战争目标的影响 / 原始战争目标的影响 * 此值） |
| DIPLO_PLAY_BACK_DOWN_CHANCE_WAR_LOSSES_MAX | 3.0 | # 额外战争目标要求的最大影响倍数（包含基础值 1） |
| DIPLO_PLAY_FREELY_ADD_WARGOALS_ESCALATION_THRESHOLD | 70 | # 升级度超过此值后，AI 将自由添加战争目标，而不再保留行动力用于拉拢 |
| DIPLO_PLAY_ADD_WARGOALS_THRESHOLD | 0.5 | # 若 AI 相对敌方的军力不足此值，在首个战争目标之后不再为自己添加更多战争目标 |
| DIPLO_PLAY_FORCE_DIPLOMATIC_PLAY_THRESHOLD | 2.0 | # 若 AI 认为自己相对敌方将拥有此等军力且想从对方获取多项利益，则不再费神发送外交要求 |
| DIPLO_PLAY_SWAY_THRESHOLD | 2.0 | # 若 AI 相对敌方拥有此等军力，则不再费神尝试拉拢任何国家 |
| DIPLO_PLAY_REVERSE_SWAY_THRESHOLD | 2.0 | # 若 AI 相对敌方拥有此等军力，则认为反向拉拢的价值较低 |
| DIPLO_PLAY_SWAY_LEANING_SIDE_MILITARY_STRENGTH_MULT | 0.25 | # 在计算相对敌方的军力时，将倾向某一方的未决国家按此比例的军力计入 |
| DIPLO_PLAY_DECIDE_ON_SUPPORT_ESCALATION | 30 | # 升级度超过此值后，即使未被拉拢，AI 也可能开始选边站（或宣布中立） |
| DIPLO_PLAY_TAKE_SIDES_MIN_BOLDNESS | 25 | # 胆量至少达到此值，AI 才会愿意无收益地选边站（列强参与遏制博弈时忽略此项） |
| DIPLO_PLAY_TAKE_SIDES_CHANCE | 0.004 | # 每个 tick 选边站的概率等于胆量乘以此值 |
| DIPLO_PLAY_DECLARE_NEUTRALITY_ESCALATION_MIN_BASE | 80 | # AI 可宣布中立的最低升级度，有立场偏好的 AI 在对战争计时开始前绝不会宣布中立 |
| DIPLO_PLAY_DECLARE_NEUTRALITY_IMPACT_OF_NEUTRALITY_SCORE | 0.5 | # AI 的中立评分 * 此值，所得结果会从 DIPLO_PLAY_DECLARE_NEUTRALITY_ESCALATION_MIN_BASE 中扣除 |
| DIPLO_PLAY_DECLARE_NEUTRALITY_IMPACT_OF_NEUTRALITY_SCORE_MAX | 50 | # DIPLO_PLAY_DECLARE_NEUTRALITY_IMPACT_OF_NEUTRALITY_SCORE 不能超过此值 |
| DIPLO_PLAY_DECLARE_NEUTRALITY_ESCALATION_MAX | 99 | # AI 可宣布中立的最高紧张度 |
| DIPLO_PLAY_ABANDON_SUPPORT_CHANCE | 0.1 | # 与负面支持评分相乘 |
| DIPLO_PLAY_SWAY_COUNTRIES_ESCALATION | 10 | # 紧张度超过此值后，AI 可能开始拉拢国家 |
| DIPLO_PLAY_REVERSE_SWAY_COUNTRIES_CHANCE_SCALED | 0.02 | # AI 每日尝试反向拉拢的概率（按果敢程度缩放） |
| DIPLO_PLAY_REVERSE_SWAY_COUNTRIES_CHANCE_MAX | 0.5 | # AI 每日尝试反向拉拢的最大概率 |
| DIPLO_PLAY_REVERSE_SWAY_LEANING_MULT | 5.0 | # 若被拉拢的国家已倾向某一方，则缩放概率和最大概率均乘以此值 |
| DIPLO_PLAY_SWAY_COUNTRIES_CHANCE_SCALED | 20 | # AI 每日尝试拉拢某国的概率（按双方相对实力缩放，1 = 1%） |
| DIPLO_PLAY_SWAY_COUNTRIES_CHANCE_MAX | 75 | # AI 每日尝试拉拢某国的最大概率 |
| DIPLO_PLAY_TIMED_WEIGHT_DURATION | 12 | # 当 AI 随机决定对博弈某一方的同情时，该权重持续的时间 |
| DIPLO_PLAY_PREFERENCE_THRESHOLD | 25 | # 差值达到此值时，视为该 AI 国家倾向博弈的某一方 |
| DIPLO_PLAY_WEAK_ABANDON_SUPPORT_THRESHOLD | -25 | # 若 AI 国家所支持一方的支持度跌破此值，考虑放弃支持 |
| DIPLO_PLAY_STRONG_ABANDON_SUPPORT_THRESHOLD | -50 | # 若 AI 国家所支持一方的支持度跌破此值，立即放弃支持 |
| DIPLO_PLAY_ABANDON_ALLY_OR_SUBJECT_MIN_ENEMY_STRENGTH | 0.75 | # 若敌方相对我方阵营的兵力未至少达到此比例，则绝不抛弃盟友或附属国 |
| DIPLO_PLAY_ABANDON_ALLY_RELUCTANCE | 50 | # 在考虑是否抛弃盟友时，将此值加到支持评分上 |
| DIPLO_PLAY_ABANDON_SUBJECT_RELUCTANCE | 100 | # 在考虑是否抛弃附属国时，将此值加到支持评分上 |
| DIPLO_PLAY_SWAY_DAYS_LEFT_MAX | 12 | # 剩余天数超过此值时，AI 不会回应拉拢提议（应与 SWAY_OFFER_TIMEOUT_DAYS 对应） |
| DIPLO_PLAY_SWAY_DAYS_LEFT_MIN | 8 | # 剩余天数不多于此值时，AI 必定回应拉拢提议（应与 SWAY_OFFER_TIMEOUT_DAYS 对应） |
| DIPLO_PLAY_SWAY_ANSWER_CHANCE | 75 | # AI 每日回应拉拢提议的概率（1 = 1%） |
| DIPLO_PLAY_WEAK_ARMY_THRESHOLD | 0.5 | # 若我方陆军实力与博弈参与各国平均值之比低于此值，将触发弱陆军效果 |
| DIPLO_PLAY_STRONG_ARMY_THRESHOLD | 1.0 | # 若我方陆军实力与博弈参与各国平均值之比至少达到此值，将开始触发强陆军效果 |
| DIPLO_PLAY_STRONG_ARMY_MAX | 3.0 | # 强陆军效果在此阈值达到最大 |
| DIPLO_PLAY_FORCE_BALANCE_SCALE | 4.0 | # 军事实力与敌方之比达到此值时，双方军力平衡带来的效果达到最大 |
| DIPLO_PLAY_FORCE_BALANCE_NAVY_FACTOR | 0.1 | # 在计算军事实力与敌方之比时，海军力量投射相对陆军力量投射的权重 |
| DIPLO_PLAY_FORCE_BALANCE_MOBILIZATION_FACTOR | 1.0 | # 出于信心等目的的考量，一个国家在博弈中的军事力量被视为按（1 + 此值 × 完全动员部队比例）增强 |
| DIPLO_PLAY_STATE_STABILITY_UNINCORPORATED_WEIGHT_MULT | 0.25 | # 未整合州的破坏度、激进派与忠诚派权重乘以此值 |
| DIPLO_PLAY_CONTAINMENT_PLAY_FACTOR | 100 | # 如果该国是列强，在遏制博弈中发起方的偏好值增加此数 |
| DIPLO_PLAY_SWAY_LOW_IMPACT_FACTOR | -100 | # 若一国几乎不会因敌方侧的战争目标而受损，其对反向拉拢的接受度所受的最大影响 |
| DIPLO_PLAY_SWAY_LOW_IMPACT_THRESHOLD | 50 | # 当敌方战争目标总影响低于或等于此值时，接受度最多减少 DIPLO_PLAY_SWAY_LOW_IMPACT_FACTOR（影响为 0 时达到最大） |
| DIPLO_PLAY_SWAY_NON_PRIMARY_DEMAND_IMPACT_MULT | 0.5 | # 次要诉求的影响在计算上述低影响系数时会乘以此因子 |
| DIPLO_PLAY_SWAY_SUBJECT_IMPACT_VALUE_DIVISOR | 500 | # 针对附属国的战争目标，其影响在计算上述低影响系数时会乘以（附属国对其宗主国的价值除以此数）（限定在 0-1 之间） |
| DIPLO_PLAY_SWAY_INCOME_TRANSFER_PACTS_OF_SAME_TYPE_FACTOR | -30 | # 目标国家每持有一项同类型收入转移协定（作为收款方），接受分数增加此数 |
| DIPLO_PLAY_SWAY_TOO_LOW_SUPPORT_DESIRE_THRESHOLD | -100 | # 若一国的支持意愿低于或等于此值，AI 不会费力评估针对它的拉拢 |
| DIPLO_PLAY_UNWANTED_SWAY_OFFER_MEMORY_DURATION_DAYS | 10 | # AI 会记住另一国对某项拉拢提议不感兴趣的天数 |
| DIPLO_PLAY_CALL_ALLY_PREFERENCE_SCORE = 1000 # 在决定 AI 想提供哪种拉拢时，“召唤盟友”的评分为此值 |  |  |
|  |  | # AI 使用这些数值来判断一个战争目标有多大“影响”，即它们有多不愿意让该战争目标被强加于己方等 |
| DIPLO_PLAY_WAR_GOAL_IMPACT_MANEUEVERS_MULT | 1 | # 战争目标的机动点数消耗乘以此数并计入影响 |
| DIPLO_PLAY_WAR_GOAL_IMPACT_INFAMY_MULT | 0.5 | # 战争目标产生的恶名乘以此数并计入影响 |
| DIPLO_PLAY_WAR_GOAL_IMPACT_CONQUEST_MULT | 2.0 | # 直接征服州或吞并整个国家的战争目标，其总影响乘以此数 |
| # 胆量（Boldness）决定 AI 在博弈中退让的信心阈值 # 每个单独的胆量系数都会乘以一个（x0 到 x1）的掷骰范围，得出每次博弈中的实际胆量值——胆量可能为负！# 胆量还用于判断未表态国家是否会主动加入博弈 # 基础胆量由该国的 AI 策略设定 |  |  |
| DIPLO_PLAY_BOLDNESS_FROM_RANK | 3 | # 乘以国家的等级值并加到胆量范围上 |
| DIPLO_PLAY_BOLDNESS_WEAK_ARMY_FACTOR | -25 | # 按我方相对兵力与 DIPLO_PLAY_WEAK_ARMY_THRESHOLD 的比较进行缩放 |
| DIPLO_PLAY_BOLDNESS_CONTAINMENT_PLAY | 100 | # 若处于遏制博弈中，增加此胆量值 |
| # 以下是一项特殊的胆量系数，在外交博弈中始终实时计算，不随机化，直接加到已保存的胆量分数上，因为主要诉求的数量可能增加 |  |  |
| DIPLO_PLAY_BOLDNESS_PRIMARY_DEMANDS | 1 | # 针对我方一侧的每点主要诉求战争目标影响，增加此数额的非随机胆量 |
|  |  | # 信心（Confidence）会加到胆量上，用于决定 AI 是否愿意退让 |
| DIPLO_PLAY_CONFIDENCE_FORCE_BALANCE_FACTOR | 75 | # 当相对敌方的兵力平衡达到 DIPLO_PLAY_FORCE_BALANCE_SCALE 时的信心水平，低于该值时按比例降低 |
| DIPLO_PLAY_CONFIDENCE_STRONG_ARMY_FACTOR | 15 | # 按我方相对兵力与 DIPLO_PLAY_STRONG_ARMY_MAX 的比较进行缩放 |
| DIPLO_PLAY_CONFIDENCE_CIVIL_WAR_OR_UPRISING | 75 | # 在内战或原住民起义中，博弈双方均增加此信心值 |
| DIPLO_PLAY_CONFIDENCE_EXISTENTIAL_PLAY | 50 | # 若退让将导致被吞并，则增加此信心值 |
| DIPLO_PLAY_CONFIDENCE_FROM_TURMOIL | -15 | # 当全国（按州人口加权）动荡达到 100% 时，减去该数值的信心 |
| DIPLO_PLAY_CONFIDENCE_FROM_LOYALISTS | 15 | # 当全国（按州人口加权）动荡达到 100% 时，增加该数值的信心 |
| DIPLO_PLAY_CONFIDENCE_FROM_DEVASTATION | -15 | # 当破坏度达到 100% 时，减去该数值的信心 |
| DIPLO_PLAY_CONFIDENCE_FROM_DEBT_LEVEL | -25 | # 当债务水平达到 100% 时，减去该数值的信心 |
| DIPLO_PLAY_CONFIDENCE_FROM_BANKRUPTCY | -25 | # 破产时减去该数值的信心 |
| DIPLO_PLAY_CONFIDENCE_FROM_GOLD_RESERVES | 15 | # 当黄金储备达到 100% 时，增加该数值的信心 |
| DIPLO_PLAY_CONFIDENCE_FROM_OWN_CONFLICTS | -25 | # 如果我们正处于另一场冲突中，且相对敌人的军事实力等于或高于 DIPLO_PLAY_FORCE_BALANCE_SCALE，则减去该数值的信心 |
| DIPLO_PLAY_CONFIDENCE_FROM_ENEMY_TURMOIL | 10 | # 当敌国全国（按州人口加权）动荡达到 100% 时，增加该数值的信心 |
| DIPLO_PLAY_CONFIDENCE_FROM_ENEMY_DEVASTATION | 10 | # 当敌方破坏度达到 100% 时，增加该数值的信心 |
| DIPLO_PLAY_CONFIDENCE_FROM_ENEMY_DEBT_LEVEL | 10 | # 当敌方债务水平达到 100% 时，增加该数值的信心 |
| DIPLO_PLAY_CONFIDENCE_FROM_ENEMY_BANKRUPTCY | 10 | # 如果敌方破产，增加该数值的信心 |
| DIPLO_PLAY_CONFIDENCE_FROM_ENEMY_CONFLICTS | 25 | # 如果对方正处于另一场冲突中，且相对其敌人的军事实力等于或高于 DIPLO_PLAY_FORCE_BALANCE_SCALE，则增加该数值的信心 |
| DIPLO_PLAY_CONFIDENCE_VERY_LOW_THRESHOLD | -50 | # 如果信心低于或等于该值，显示为极低 |
| DIPLO_PLAY_CONFIDENCE_LOW_THRESHOLD | -25 | # 如果信心低于或等于该值，显示为低 |
| DIPLO_PLAY_CONFIDENCE_HIGH_THRESHOLD | 25 | # 如果信心高于或等于该值，显示为高 |
| DIPLO_PLAY_CONFIDENCE_VERY_HIGH_THRESHOLD | 50 | # 如果信心高于或等于该值，显示为极高 |
| # 以下数据用于决定 AI 想加入外交博弈的哪一方（如果有的话）# 中立度是一个计算值，决定一个国家在多大程度上想要置身于外交博弈之外 # 一个国家要加入博弈，其一侧的偏好分数必须同时超过敌方的偏好分数和中立度分数 # 基础中立度由该国的 AI 策略设定 |  |  |
| DIPLO_PLAY_NEUTRALITY_MIN | 0 |  |
| DIPLO_PLAY_NEUTRALITY_PREFERENCE_DELTA_THRESHOLD | 50 | # 如果两侧之间的偏好差值小于该值，则将该差值与该值的差加到中立度分数上 |
| DIPLO_PLAY_NEUTRALITY_FROM_DEBT_LEVEL | 100 | # 当债务水平达到 100% 时，增加该数值的中立度分数 |
| DIPLO_PLAY_NEUTRALITY_FROM_BANKRUPTCY | 100 | # 破产时增加该数值的中立度分数 |
| DIPLO_PLAY_NEUTRALITY_FROM_DEVASTATION_LEVEL | 100 | # 当全国（按州人口加权）破坏度达到 100% 时，增加该数值的中立度分数 |
| DIPLO_PLAY_NEUTRALITY_FROM_TURMOIL | 100 | # 当全国（按州人口加权）动荡达到 100% 时，增加该数值的中立度分数 |
| DIPLO_PLAY_NEUTRALITY_IN_SUBJECT_CONFLICT | -50 | # 如果博弈中任意一方是附属国，减去该数值的中立度分数 |
| DIPLO_PLAY_NEUTRALITY_IN_NATIVE_UPRISING | 50 | # 原住民起义类型的冲突会增加该数值的中立度分数 |
| DIPLO_PLAY_NEUTRALITY_FROM_ONGOING_CONFLICTS | 200 | # 如果正处于一场冲突中，且相对敌人的军事实力等于或高于 DIPLO_PLAY_FORCE_BALANCE_SCALE，则增加该数值的中立度分数 |
| DIPLO_PLAY_NEUTRALITY_FROM_LOWER_RANK | 5 | # 对于我们与博弈中排名最低的参与者之间的每一个排名差值，如果我们排名高于对方 |
| DIPLO_PLAY_NEUTRALITY_FROM_NO_ARMY | 1000 | # 如果我们完全没有陆军，将此值加入中立度评分 |
| DIPLO_PLAY_NEUTRALITY_WEAK_ARMY_FACTOR | 100 | # 按我们相对军力与 DIPLO_PLAY_WEAK_ARMY_THRESHOLD 的比较结果进行缩放 |
| DIPLO_PLAY_NEUTRALITY_TRUCE_FACTOR | 50 | # 如果我们与任一主要参与方处于停战状态，且无同盟或附属国关系，并且这不是内战 |
| # 同情度会先加总，再乘以一个（DIPLO_PLAY_SYMPATHY_RANGE_MIN 到 DIPLO_PLAY_SYMPATHY_RANGE_MAX）范围内的随机掷值，使 AI 在特定博弈中对双方各有随机的倾向 # 大于 0 的同情度会直接加入加入该博弈一方的意愿 # 对某一方的同情度可以低于 0，但除了作为抵御同情度增加的缓冲外，没有其他额外效果 |  |  |
| DIPLO_PLAY_SYMPATHY_RANGE_MIN | 0.1 | # 初始同情度随机掷值的最小范围（博弈期间的加值完全随机） |
| DIPLO_PLAY_SYMPATHY_RANGE_MAX | 1.0 | # 初始同情度随机掷值的最大范围（博弈期间的加值完全随机） |
| DIPLO_PLAY_SYMPATHY_BASE_INITIATOR | 20 | # 外交博弈中进攻方随机同情度范围的基础大小 |
| DIPLO_PLAY_SYMPATHY_BASE_TARGET | 40 | # 外交博弈中防御方随机同情度范围的基础大小 |
| DIPLO_PLAY_SYMPATHY_ENEMY_OF_SUBJECT_INITIATOR | -100 | # 若敌对者是进攻方，从我们附属国的敌人的同情度范围中扣除 |
| DIPLO_PLAY_SYMPATHY_ENEMY_OF_SUBJECT_TARGET | -50 | # 若敌对者是防御方，从我们附属国的敌人的同情度范围中扣除 |
| DIPLO_PLAY_SYMPATHY_ENEMY_OF_ALLY_INITIATOR | -100 | # 若敌对者是进攻方，从我们盟友的敌人的同情度范围中扣除 |
| DIPLO_PLAY_SYMPATHY_ENEMY_OF_ALLY_TARGET | -50 | # 若敌对者是防御方，从我们盟友的敌人的同情度范围中扣除 |
| DIPLO_PLAY_SYMPATHY_ENEMY_OF_INFAMOUS_COUNTRY | 15 | # 加入恶名国家的敌人的同情度范围 |
| DIPLO_PLAY_SYMPATHY_ENEMY_OF_NOTORIOUS_COUNTRY | 30 | # 加入声名狼藉国家的敌人的同情度范围 |
| DIPLO_PLAY_SYMPATHY_ENEMY_OF_PARIAH_COUNTRY | 100 | # 加入众叛亲离国家的敌人的同情度范围 |
| DIPLO_PLAY_SYMPATHY_LENIENT_AI_GAME_RULE | 25 | # 使用宽容 AI 游戏规则时加入玩家的同情度范围 |
| DIPLO_PLAY_SYMPATHY_HARSH_AI_GAME_RULE | -25 | # 使用严厉 AI 游戏规则时从玩家的同情度范围中扣除 |
| DIPLO_PLAY_SYMPATHY_FROM_INITIAL_WARGOAL | 0.75 | # 目标的初始同情度最多增加此值 * 主要战争目标上累积的恶名 |
| DIPLO_PLAY_SYMPATHY_INCREASE_NEW_WARGOAL | 1 | # 对新增战争目标一方的敌人的同情度最多增加此值 * 累积恶名 |
| DIPLO_PLAY_SYMPATHY_INCREASE_SWAYED_WITH_WARGOAL | 0.75 | # 对通过拉拢新增战争目标一方的敌人的同情度最多增加此值 * 累积恶名 |
| DIPLO_PLAY_SWITCH_SIDES_FACTOR | -10 | # 如果 AI 已经选边站，加入 reluctance 以拒绝后续的拉拢提议 |
| DIPLO_PLAY_IDEOLOGICAL_OPINION_POSITIVE_FACTOR | 0.2 | # 正面的意识形态评价乘以此值后加入加入某一方的接受度 |
| DIPLO_PLAY_IDEOLOGICAL_OPINION_NEGATIVE_FACTOR | 1 | # 负面的意识形态评价乘以此值后加入加入某一方的接受度 |
| DIPLO_PLAY_IDEOLOGICAL_OPINION_REVOLUTION_MULT | 3 | # 在革命博弈中，DIPLO_PLAY_IDEOLOGICAL_OPINION_FACTOR 乘以此值 |
| DIPLO_PLAY_SECESSION_OWN_SECESSION_RISK_FACTOR | -100 | # 当某文化在 AI 本国拥有足够多的人口可以分裂时，为 AI 支持该文化的分裂加入此数值的不情愿度 |
| DIPLO_PLAY_NON_ALLY_UNRECOGNIZED_BASE_FACTOR | -25 | # 为 AI 支持非同盟的未认可政权对抗已认可政权增加此数值的 reluctance |
| DIPLO_PLAY_NON_ALLY_UNRECOGNIZED_INCONSEQUENTAL_ENEMY_DEMANDS_FACTOR | -50 | # 当已认可政权并未索要重大领土让步（征服/使其成为附属国等）时，为 AI 支持非同盟的未认可政权增加此数值的 reluctance |
| DIPLO_PLAY_NON_ALLY_UNRECOGNIZED_CONSEQUENTAL_DEMANDS_FACTOR | -100 | # 为 AI 支持非同盟的未认可政权的重大诉求增加此数值的 reluctance |
| DIPLO_PLAY_ALLY_INITIATOR_FACTOR | 25 | # 加入发起者的同盟加入其一方阵营的意愿附加值 |
| DIPLO_PLAY_ALLY_TARGET_FACTOR | 50 | # 加入目标者的同盟加入其一方阵营的意愿附加值 |
| DIPLO_PLAY_GUARANTEE_TARGET_FACTOR | 50 | # 加入目标者的担保国加入其一方阵营的意愿附加值 |
| DIPLO_PLAY_OVERLORD_INITIATOR_FACTOR | 25 | # 加入发起者的宗主国加入其一方阵营的意愿附加值 |
| DIPLO_PLAY_OVERLORD_TARGET_FACTOR | 50 | # 加入目标者的宗主国加入其一方阵营的意愿附加值 |
| DIPLO_PLAY_SAME_POWER_BLOC_INITIATOR_FACTOR | 15 | # 加入发起者的强权集团同僚加入其一方阵营的意愿附加值 |
| DIPLO_PLAY_SAME_POWER_BLOC_TARGET_FACTOR | 25 | # 加入目标者的强权集团同僚加入其一方阵营的意愿附加值 |
| # 外交博弈中针对关系等级的评分 |  |  |
| DIPLO_PLAY_RELATIONS_HOSTILE_FACTOR | -50 |  |
| DIPLO_PLAY_RELATIONS_COLD_FACTOR | -25 |  |
| DIPLO_PLAY_RELATIONS_POOR_FACTOR | -10 |  |
| DIPLO_PLAY_RELATIONS_CORDIAL_FACTOR | 10 |  |
| DIPLO_PLAY_RELATIONS_AMICABLE_FACTOR | 25 |  |
| DIPLO_PLAY_RELATIONS_FRIENDLY_FACTOR | 50 |  |
| # 外交博弈中针对态度（对主要参与者和支持者双方均计分）的评分 |  |  |
| DIPLO_PLAY_ATTITUDE_DISINTERESTED_FACTOR | 0 |  |
| DIPLO_PLAY_ATTITUDE_DISINTERESTED_BACKER_FACTOR | 0 |  |
| DIPLO_PLAY_ATTITUDE_CAUTIOUS_FACTOR | 0 |  |
| DIPLO_PLAY_ATTITUDE_CAUTIOUS_BACKER_FACTOR | 0 |  |
| DIPLO_PLAY_ATTITUDE_CONCILIATORY_FACTOR | 10 |  |
| DIPLO_PLAY_ATTITUDE_CONCILIATORY_BACKER_FACTOR | 5 |  |
| DIPLO_PLAY_ATTITUDE_COOPERATIVE_FACTOR | 15 |  |
| DIPLO_PLAY_ATTITUDE_COOPERATIVE_BACKER_FACTOR | 5 |  |
| DIPLO_PLAY_ATTITUDE_GENIAL_FACTOR | 25 |  |
| DIPLO_PLAY_ATTITUDE_GENIAL_BACKER_FACTOR | 10 |  |
| DIPLO_PLAY_ATTITUDE_WARY_FACTOR | -10 |  |
| DIPLO_PLAY_ATTITUDE_WARY_BACKER_FACTOR | -5 |  |
| DIPLO_PLAY_ATTITUDE_BELLIGERENT_FACTOR | -50 |  |
| DIPLO_PLAY_ATTITUDE_BELLIGERENT_BACKER_FACTOR | -25 |  |
| DIPLO_PLAY_ATTITUDE_ANTAGONISTIC_FACTOR | -50 |  |
| DIPLO_PLAY_ATTITUDE_ANTAGONISTIC_BACKER_FACTOR | -25 |  |
| DIPLO_PLAY_ATTITUDE_LOYAL_FACTOR | 100 |  |
| DIPLO_PLAY_ATTITUDE_LOYAL_BACKER_FACTOR | 25 |  |
| DIPLO_PLAY_ATTITUDE_ALOOF_FACTOR | 25 |  |
| DIPLO_PLAY_ATTITUDE_ALOOF_BACKER_FACTOR | 10 |  |
| DIPLO_PLAY_ATTITUDE_DEFIANT_FACTOR | -25 |  |
| DIPLO_PLAY_ATTITUDE_DEFIANT_BACKER_FACTOR | -10 |  |
| DIPLO_PLAY_ATTITUDE_REBELLIOUS_FACTOR | -100 |  |
| DIPLO_PLAY_ATTITUDE_REBELLIOUS_BACKER_FACTOR | -50 |  |
| DIPLO_PLAY_ATTITUDE_PROTECTIVE_FACTOR | 25 |  |
| DIPLO_PLAY_ATTITUDE_PROTECTIVE_BACKER_FACTOR | 10 |  |
| DIPLO_PLAY_ATTITUDE_DOMINEERING_FACTOR | -10 |  |
| DIPLO_PLAY_ATTITUDE_DOMINEERING_BACKER_FACTOR | 0 |  |
| DIPLO_PLAY_SWAY_RANDOM_FACTOR | 1.0 | # 该数值越高，AI 在选择优先拉拢哪些国家时的随机性越强 |
| DIPLO_PLAY_SWAY_UNWANTED_OFFER | -1000 | # 被提供不想要的东西时的数值 |
| DIPLO_PLAY_SWAY_CALL_IN_OBLIGATION | 100 | # 召唤履行义务时的数值 |
| DIPLO_PLAY_SWAY_MINIMUM_OBLIGATION_VALUE | 10 | # 价值低于此数值的义务会被拒绝 |
| DIPLO_PLAY_SWAY_CALL_ALLY_FACTOR | 25 | # “召唤同盟”拉拢方式的接受度附加值 |
| DIPLO_PLAY_SWAY_MINIMUM_PREFERENCE_FOR_SUBJUGATION | 1 | # AI 不会以“成为附属国”进行拉拢（sway）或反向拉拢，除非支持者对被支持方的偏好至少达到此值 |
| DIPLO_PLAY_SWAY_WARGOAL_WEAK_SWAYER_CONFIDENT_IN_OWN_ARMY_FACTOR | 0.25 | # 如果目标方相信自己能够独立实现该战争目标，则“弱小”拉拢方案的惩罚会被移除这么多 |
| DIPLO_PLAY_SWAY_WARGOAL_FACTOR | 1.0 | # 乘以战争目标的价值 |
| DIPLO_PLAY_SWAY_WARGOAL_THRESHOLD | 10 | # 战争目标需要至少此基础价值才能作为拉拢方案的一部分被接受 |
| DIPLO_PLAY_SWAY_WARGOAL_MINIMUM_SWAYER_MULTIPLIER_INITIATOR | 0.2 | # 如果来自发起方的战争目标拉拢方案因拉拢方实力弱小而低于其基础价值的此比例，则视为不想要的战争目标 |
| DIPLO_PLAY_SWAY_WARGOAL_MINIMUM_SWAYER_MULTIPLIER_TARGET | 0.05 | # 如果来自目标方的战争目标拉拢方案因拉拢方实力弱小而低于其基础价值的此比例，则视为不想要的战争目标 |
| DIPLO_PLAY_SWAY_LEANING_PLAYER_FACTOR | 100 | # 加到倾向于某一方的玩家身上的接受度，使 AI 更有可能拉拢他们 |
| DIPLO_PLAY_SWAY_BECOME_SUBJECT_VALUE_FACTOR | 1.0 | # 乘以 AI 对拉拢国成为其附属国的意愿 |
| DIPLO_PLAY_SWAY_TRANSFER_SUBJECT_VALUE_FACTOR | 1.0 | # 乘以 AI 对拉拢国提供的转让附属国使其成为附属国的意愿 |
| DIPLO_PLAY_SWAY_STATE_DESIRE_FACTOR | 2.0 | # 乘以 AI 对某个州的策略价值，以判断 AI 是否想要一个转让州的拉拢方案 |
| DIPLO_PLAY_SWAY_DIPLOMATIC_PACT_DESIRE_FACTOR | 1.0 | # 乘以外交行动的外交接受度评分，以判断 AI 是否想要一个外交行动拉拢方案 |
| # 决定 AI 如何基于反向拉拢会为其阵营增加的军事实力来评估其价值 # 如果该实力能够弥补“完全没有军事力量”与 DIPLO_PLAY_REVERSE_SWAY_THRESHOLD 之间的全部差距，则使用完整数值，否则按所弥补差距的比例进行缩放 # 例如，如果新支持者会将相对敌方的军事实力从 1.0x 提升到 2.0x，而 DIPLO_PLAY_REVERSE_SWAY_THRESHOLD 为 2.0，则应用此数值的一半 |  |  |
| DIPLO_PLAY_REVERSE_SWAY_ADDED_MILITARY_POWER_FACTOR | 50 |  |
| DIPLO_PLAY_REVERSE_SWAY_MIN_ADDED_MILITARY_POWER | 5 | # 如果增加的军事实力价值低于此值，则认为该国的帮助一文不值并拒绝方案 |
| # 将增加的军事实力系数乘以其当前被敌方压制的程度 # 即：在军事实力为敌方的 0x 时应用完整的此修正，在 0.5x 时应用其中一半，在 1x 及以上时不应用 |  |  |
| DIPLO_PLAY_REVERSE_SWAY_ADDED_MILITARY_POWER_OUTMATCHED_MULT | 4.0 |  |
| DIPLO_PLAY_REVERSE_SWAY_OUTMATCHING_FACTOR | -25.0 | # 如果 AI 一方压制敌方的幅度超过 DIPLO_PLAY_REVERSE_SWAY_THRESHOLD，则其军事实力比与 DIPLO_PLAY_REVERSE_SWAY_THRESHOLD 的差值乘以此值并加到接受度上 |
| DIPLO_PLAY_REVERSE_SWAY_BASE_FACTORS_MULT | 0.5 | # 以此乘数将关系、态度、意识形态观点等基础因素应用到反向拉拢上 |
| DIPLO_PLAY_REVERSE_SWAY_WARGOAL_VALUE_FACTOR | -2.0 | # 乘以 AI 假如自己持有该战争目标时对其的想要程度，并应用到反向拉拢接受度 |
| DIPLO_PLAY_REVERSE_SWAY_WARGOAL_IMPACT_FACTOR | -0.5 | # 乘以战争目标的行动点数花费（以判断其影响力大小），并应用到所请求战争目标的反向拉拢接受度上 |
| DIPLO_PLAY_REVERSE_SWAY_WARGOAL_INFAMY_FACTOR | -0.5 | # 乘以恶名影响，并应用到所请求战争目标的反向拉拢接受度上 |
| DIPLO_PLAY_REVERSE_SWAY_OFFER_OBLIGATION_MIN_VALUE | 5 | # AI 对义务（Obligation）的估值在考虑是否接受反向拉拢时绝不会低于此值 |
| DIPLO_PLAY_REVERSE_SWAY_OFFER_OBLIGATION_FACTOR | -6.0 | # 乘以 AI 在假设自己是提供支持的国家时对义务的估值，应用于以义务进行的反向拉拢接受度 |
| DIPLO_PLAY_REVERSE_SWAY_CALL_IN_OBLIGATION_FACTOR | -3.0 | # 乘以 AI 对其持有义务的估值，应用于要求兑现义务的反向拉拢接受度 |
| DIPLO_PLAY_REVERSE_SWAY_STATE_VALUE_FACTOR | -2.0 | # 乘以 AI 对己方州（State）的战略估值，以确定在反向拉拢中割让该州的抗拒程度 |
| DIPLO_PLAY_REVERSE_SWAY_BECOME_SUBJECT_VALUE_FACTOR | 1.0 | # 乘以 AI 想要成为拉拢目标的附属国（Subject）的程度 |
| DIPLO_PLAY_REVERSE_SWAY_TRANSFER_SUBJECT_VALUE_FACTOR | -1.0 | # 乘以 AI 对其提议转让给拉拢目标的附属国的估值 |
| DIPLO_PLAY_REVERSE_SWAY_CALL_ALLY_DESIRE | 25 | # 即使召唤盟友实际上并不适用于反向拉拢，也会将其加入 AI 对反向拉拢召唤盟友的评分中，以便与其他拉拢类型进行比较 |
| DIPLO_PLAY_ADD_WARGOAL_MIN_SCORE | 20 | # 战争目标（War goal）需要至少达到此值，AI 才会将其加入外交博弈 |
| LOW_AGGRESSION_BASE_EFFECT_MULT | 0.5 | # 低 AI 侵略性游戏规则对 AI 发起外交博弈频率的影响 |
| HIGH_AGGRESSION_BASE_EFFECT_MULT | 2.0 | # 高 AI 侵略性游戏规则对 AI 发起外交博弈频率的影响 |
| LOW_AGGRESSION_INFAMY_ACCEPTANCE_MULT | 0.5 | # 对于低侵略性 AI，其认为不合意/不可接受的恶名（Infamy）数量乘以此系数 |
| HIGH_AGGRESSION_INFAMY_ACCEPTANCE_MULT | 1.5 | # 对于低侵略性 AI，其认为不合意/不可接受的恶名数量乘以此系数 |
| AI_AGGRESSION_MAX_ACCEPTABLE_INFAMY | 100 | # 高侵略性不会使不合意/不可接受的恶名设置超过此值 |
| # 以下数据用于决定 AI 会选择哪些战争目标 |  |  |
| WAR_GOAL_RANDOM_FACTOR | 2.0 | # 此值越高，AI 的战争目标选择越随机 |
| WAR_GOAL_UNDESIRABLE_INFAMY_FACTOR | 0.5 | # 若战争目标会使国家超过不合意的恶名水平，其价值乘以此系数 |
| WAR_GOAL_UNACCEPTABLE_INFAMY_FACTOR | 0 | # 若战争目标会使国家超过不可接受的恶名水平，其价值乘以此系数 |
| WAR_GOAL_NOT_PRIMARY_DEMAND_FACTOR | 0.5 | # 若拉拢提议中的战争目标不会作为主要诉求添加，其价值乘以此系数 |
| # 不同海峡设置的不变度系数。数值越高，AI 越倾向于维持现有设置。 |  |  |
| STRAIT_ACCESS_STATUS_STICKYNESS | 1.25 |  |
| STRAIT_ACCESS_PERMISSIONS_STICKYNESS | 1.25 |  |
| STRAIT_TOLL_RATES_STICKYNESS | 1.25 |  |
| WAR_GOAL_MAKE_PRIMARY_DEMAND_SCORE_MULT | 0.75 | # 在决定是将其转为主要诉求还是添加新战争目标时，将现有战争目标的评分乘以此系数 |
| WAR_GOAL_MAKE_PRIMARY_DEMAND_RETURN_STATE_SCORE_MULT | 1.25 | # 对归还州的战争目标覆盖 WAR_GOAL_MAKE_PRIMARY_DEMAND_SCORE_MULT |
| WAR_GOAL_MIN_SCORE_TO_MAKE_PRIMARY_DEMAND | 30 | # 战争目标需要至少达到此评分（在应用 WAR_GOAL_MAKE_PRIMARY_DEMAND_SCORE_MULT 之前），AI 才会将其设为主要诉求 |
| # 以下数据用于决定 AI 会研究哪些技术 |  |  |
| TECH_RANDOM_FACTOR | 1.0 | # 此值越高，AI 的技术研究越随机 |
| TECH_COST_PENALTY_FACTOR | 5.0 | # AI 研究某项技术的倾向除以（1 + 此系数 × 超前惩罚 / 时代基础成本） |
| INCORPORATE_STATE_MAX_YEARS | 8.5 | # AI 整合一个州所允许的最长年数 |
| INCORPORATE_STATE_MIN_POPULATION | 200000 | # 以下数据用于决定 AI 应当整合哪些州 # AI 整合本土州所需的最低人口 |
| # 以下数据用于决定哪些州最重要、需要防守 |  |  |
| DEFEND_STATE_BARRACKS_WEIGHT | 1 | # 每级兵营 |
| DEFEND_STATE_BARRACKS_MAX_WEIGHT | 20 | # 每州 |
| DEFEND_STATE_NAVAL_ADMINISTRATION_WEIGHT | 0.5 | # 每级海军行政部 |
| DEFEND_STATE_NAVAL_ADMINISTRATION_MAX_WEIGHT | 10 | # 每州 |
| DEFEND_STATE_CAPITAL_WEIGHT | 25 |  |
| DEFEND_STATE_CAPITAL_WAR_NEGOTIATOR_WEIGHT | 100 |  |
| DEFEND_STATE_OWN_CAPITAL_WEIGHT_MULT | 5 |  |
| DEFEND_STATE_WARGOAL_WEIGHT | 100 |  |
| DEFEND_STATE_INCORPORATED_WEIGHT_MULT | 1.5 |  |
| # 以下数据用于决定哪些州最重要、需要进攻 |  |  |
| INVADE_STATE_BARRACKS_WEIGHT | 1 | # 每级兵营 |
| INVADE_STATE_BARRACKS_MAX_WEIGHT | 20 | # 每州 |
| INVADE_STATE_NAVAL_ADMINISTRATION_WEIGHT | 0.5 | # 每级海军行政部 |
| INVADE_STATE_NAVAL_ADMINISTRATION_MAX_WEIGHT | 10 | # 每州 |
| INVADE_STATE_CAPITAL_WEIGHT | 25 |  |
| INVADE_STATE_CAPITAL_WAR_NEGOTIATOR_WEIGHT | 100 |  |
| INVADE_STATE_OWN_CAPITAL_WEIGHT_MULT | 5 |  |
| INVADE_STATE_WARGOAL_WEIGHT | 100 |  |
| INVADE_STATE_INCORPORATED_WEIGHT_MULT | 1.5 |  |
| # 以下数据用于入侵： |  |  |
| LAND_INVASION_RANDOM_FACTOR | 0.5 | # 此值越高，AI 陆上入侵战区的选择越随机 |
| LAND_INVASION_MIN_RELATIVE_LOCAL_ARMY_STRENGTH | 0.5 | # AI 发动陆上入侵时，希望至少拥有防守方陆军实力的这一比例 |
| LAND_INVASION_MIN_SCORE | 100 | # AI 不会对总州分数低于此值的战区发动陆上入侵 |
| LAND_INVASION_MAX_LOCAL_FRONT_SCORE | 100 | # 如果存在至少达到此总分数的本地前线，则不发动陆上入侵 |
| LAND_INVASION_MAX_TRAVEL_TIME_DAYS | 30 | # 不要用距离该州超过此行军天数的陆军发动入侵 |
| LAND_INVASION_TRAVEL_TIME_PENALTY | 0.5 | # 陆军距离该州越远，分数越低：总分 = 战斗力 * (1 - 此值 * (行军时间 / LAND_INVASION_MAX_TRAVEL_TIME_DAYS)) |
| LAND_INVASION_MAX_AVAILABLE_ARMY_FRACTION | 0.5 | # 同时用于陆上入侵的可用陆军不得超过此比例 |
| LAND_INVASION_CANCEL_SCORE_THRESHOLD | 50 | # 若入侵分数低于此值则取消入侵 |
| NAVAL_INVASION_RANDOM_FACTOR | 0.5 | # 此值越高，AI 海上入侵战区的选择越随机 |
| NAVAL_INVASION_MIN_RELATIVE_LOCAL_ARMY_STRENGTH | 0.25 | # AI 发动海上入侵时，希望至少拥有防守方陆军实力的这一比例 |
| NAVAL_INVASION_MIN_RELATIVE_LOCAL_NAVY_STRENGTH | 0.5 | # AI 发动海上入侵时，希望至少拥有防守方海军实力的这一比例 |
| NAVAL_INVASION_MIN_RELATIVE_GLOBAL_NAVY_STRENGTH_ATTACKER | 0.25 | # 作为进攻方时，AI 发动海上入侵希望至少拥有整场战争中海军实力的这一比例 |
| NAVAL_INVASION_MIN_RELATIVE_GLOBAL_NAVY_STRENGTH_DEFENDER | 0.5 | # 作为防守方时，AI 发动海上入侵希望至少拥有整场战争中海军实力的这一比例 |
| NAVAL_INVASION_COOLDOWN_DAYS | 20 | # 发动一次海上入侵后，AI 至少等待此时长才会发动下一次 |
| NAVAL_INVASION_MIN_SCORE | 100 | # AI 不会对总州分数低于此值的战区发动海上入侵 |
| NAVAL_INVASION_INVADE_STATE_WARGOAL_WEIGHT | 500 | # 海上入侵目标选择的战争目标州权重（高于基于前线的 INVADE_STATE_WARGOAL_WEIGHT） |
| NAVAL_INVASION_MAX_TARGET_CANDIDATES | 5 | # 每次登陆作战考虑的候选目标州数量（按得分顺序尝试，直到有一个通过驻军检查） |
| NAVAL_INVASION_HIGH_VALUE_STATE_THRESHOLD | 100 | # 若目标州重要性至少达到此值，则在海军陆战队之外始终派遣正规陆军支援 |
| NAVAL_INVASION_MAX_LOCAL_FRONT_SCORE | 100 | # 若将军拥有的本地前线总得分至少达到此值，则不发动海上登陆 |
| NAVAL_INVASION_CANCEL_SCORE_THRESHOLD | 50 | # 若登陆作战得分低于此值，则取消该登陆 |
| NAVAL_INVASION_MAX_AVAILABLE_ARMY_FRACTION | 0.5 | # 同时用于海上登陆的可用陆军不得超过此比例 |
| NAVAL_INVASION_MAX_AVAILABLE_FLEET_FRACTION | 0.5 | # 同时用于海上登陆的可用舰队不得超过此比例 |
| SUPPLY_SHIP_STRAIN_START_RATIO | 0.75 | # 补给船使用率达到此值时开始施加得分惩罚（0.99x 乘数） |
| SUPPLY_SHIP_STRAIN_MAX_RATIO | 2.0 | # 补给船使用率达到此值时施加最大得分惩罚（0.05x 乘数） |
| SUPPLY_SHIP_STRAIN_MULT_AT_START | 0.99 | # 起始比率时的得分乘数 |
| SUPPLY_SHIP_STRAIN_MULT_AT_FULL | 0.75 | # 补给船使用率 100% 时的得分乘数 |
| SUPPLY_SHIP_STRAIN_MULT_AT_MAX | 0.05 | # 最大比率时的得分乘数 |
| MARINE_FORMATION_TAG_MIN_FRACTION | 0.5 | # 将编队标记为海军陆战队所需的海军陆战队单位最低比例 |
|  |  | # 造船相关 defines |
| SHIP_TEMPLATE_CREATION_MIN_SCORE_FACTOR | 1.5 | # AI 只有在新舰船模板的改装得分至少达到同类型现有最佳模板的此倍数时才会创建新模板 |
| SHIP_RETROFIT_MIN_SCORE_FACTOR | 2.0 | # AI 只有在目标模板的总得分至少达到当前模板得分的此倍数时才会改装舰船 |
| FLEET_RECALL_HULL_RATIO_WAR | 0.75 | # 处于战争或外交博弈时，平均船体值低于或等于此比率的舰队会被召回 |
| FLEET_RECALL_HULL_RATIO_PEACE | 1.0 | # 处于和平时，平均船体值低于此比率的舰队会被召回（1.0 = 召回任何受损舰队） |
| FLEET_RECALL_CREW_RATIO_WAR | 0.75 | # 处于战争或外交博弈时，平均船员值低于或等于此比率的舰队会被召回 |
| FLEET_RECALL_CREW_RATIO_PEACE | 1.0 | # 处于和平时，平均船员值低于此比率的舰队会被召回（1.0 = 召回任何人员不足的舰队） |
| FLEET_RECALL_MIN_MISSION_SCORE | 0.5 | # 最佳任务得分低于此阈值的舰队会被召回 |
| SHIP_DESIGN_MODIFICATION_RANDOM_FACTOR | 0.25 | # 设计时应用于 AI 改装权重的随机因子，用于产生国家间差异 |
| SHIP_CONSTRUCTION_WANTED_SHIPS_TO_BUILD_COST_FACTOR | 1.0 | # 该值乘以 AI 想要建造的舰船成本，以决定 AI 的建造意愿。该值越高，AI 越愿意在想要的舰船上花费 |
| SHIP_CONSTRUCTION_WANTED_BUILT_SHIPS_COST_FACTOR | 0.3 | # 该值乘以现有舰船的成本，以便为维修/改装分配额外建造点数 |
| SHIP_CONSTRUCTION_DEBT_RESUME | 0.1 | # 若舰船建造被暂停，当债务相对于债务上限降低到此比例时恢复建造 |
| SHIP_CONSTRUCTION_DEBT_PAUSE | 0.3 | # 若债务相对债务上限达到此比例，暂停所有舰船建造 |
| MIN_SHIPS_TO_TRANSFER | 5 | # 除非至少转移此数量的舰船，否则 AI 不会在舰队之间转移舰船 |
| SHIP_TRANSFER_BASE_VALUE_PER_CONSTRUCTION_POINT | 150 | # AI 舰船估值（例如舰船转移条约接受度）中每个建造点数的基础英镑值。高于经验性约 £40/CP 的重置成本，以确保目标方的接受得分在中型主力舰、多年期协定下能超过 int32 截断值 |
| DISBAND_OBSOLETE_SHIP_DAYS | 3650 | # 如果一艘舰船被 AI 标记为过时至少这么多天（约10年），且尚未被出售/转让，AI 会直接将其退役。与 ship_transfer 配套：理想情况下舰船会在此阈值触发前被出售。 |
| DISBAND_OBSOLETE_SHIP_CREW_RATIO | 0.8 | # 如果所需船员与最大可用水手数量的比例超过此值，无论舰船过时多久，AI 都会立即将其退役 |
| SHIP_CONSTRUCTION_BLOCK_CREW_RATIO | 1.0 | # 如果所需船员与最大可用水手数量的比例达到或超过此值，AI 将不会排队建造新舰船 |
| SUPPLY_SHIP_ALLOCATION_HIGH_RATIO | 0.5 | # 如果当前补给舰船数量低于所需数量的此比例，AI 使用高补给建造分配 |
| SUPPLY_SHIP_ALLOCATION_LOW_RATIO | 1.0 | # 如果当前补给舰船数量高于所需数量的此比例，AI 使用低补给建造分配 |
| SUPPLY_SHIP_ALLOCATION_VERY_LOW_RATIO | 1.5 | # 如果当前补给舰船数量高于所需数量的此比例，AI 使用极低补给建造分配 |
| DISBAND_EXCESS_SUPPLY_SHIPS_MIN_RATIO | 2.0 | # AI 只在可用补给舰船数量超过所需数量的此比例时才将其退役，然后降至所需数量 |
| DISBAND_EXCESS_SUPPLY_SHIPS_MAX_COUNT | 10 | # AI 每次更新时最多退役的超额补给舰船数量 |
| # 以下数据用于总司令命令： |  |  |
| HQ_DEFENSE_MIN_THEATER_SCORE | 100 | # 本地总部所在战区必须至少具有此重要性分数才会保有最低限度的驻军 |
| NUM_DAYS_TO_REMEMBER_FAILED_FRONT_OR_HQ_ASSIGNMENT | 10 | # AI 应记住将将军分配到前线或总部失败（从而不再尝试该前线）多少天 |
| NUM_DAYS_TO_REMEMBER_FAILED_SUPPLY_ROUTE | 30 | # AI 应记住某编队未能找到通往目标的补给路线多少天 |
| NUM_DAYS_TO_REMEMBER_FAILED_NAVAL_INVASION | 100 | # AI 应记住某常规编队未能发起海上登陆多少天 |
| FRONT_OR_HQ_IMPORTANCE_MIN_SCORE | 50 | # 如果一个前线的价值低于此值，AI 不会向其分配任何将军 |
| # 以下数据用于评估指挥官命令 |  |  |
| FRONT_IMPORTANCE_OWN_FRONT_WEIGHT | 2.0 | # 我们“拥有”的前线，其州的重要性会乘以此系数 |
| HQ_STATIONING_IMPORTANCE_NOT_OWN_HQ_WEIGHT_MULT | 0.25 | # 盟友的总部的重要性乘以此系数，因为 AI 更倾向于驻扎在自己的总部 |
| HQ_OR_FRONT_UNDEFENDED_ASSIGNMENT_WEIGHT | 2.0 | # 无防守的总部和前线在分配编队时通过此乘数获得优先权 |
| HQ_OR_FRONT_SPLIT_FORCE_BASE_FRACTION | 1.0 | # 如果分兵以掩护无防守的总部/前线，当两地的所需兵力差距相等且被考虑分兵的陆军原本不在场时，这是从源编队派出的比例 |
| HQ_OR_FRONT_SPLIT_FORCE_MIN_FRACTION | 0.1 | # 如果分兵以掩护无防守的总部/前线，派出或留下的兵力不得少于源编队的此比例 |
| HQ_OR_FRONT_SPLIT_FORCE_DEFENDED_LOCATION_MIN_FRACTION_TO_SEND | 0.33 | # 如果分兵以掩护无防守的总部/前线，若源编队分出的部队小于此比例，则不向已有防守的前线派出分出的部队 |
| # 如果没有舰队能够运送整支陆军进行海上运输，AI 会在此最优舰队至少能运载陆军此比例时将其分兵 |  |  |
| TRANSPORT_SPLIT_MIN_FLEET_CAPACITY_FRACTION | 0.2 |  |
| UNITS_PERCENTAGE_TO_BE_CONSIDERED_IN_DISADVANTAGE | 0.50 | # 一个百分比 [0.0, 1.0]，表示前线上的 AI 部队占双方（AI+敌方）总部队数的比例，用于决定何时开始应用 FRONT_IMPORTANCE_WEIGHT_WHEN_IN_DISADVANTAGE。 |
| # 在考虑是否将将军移动到某个特定位置时，新位置所需与当前单位之间的差值会除以 1 加上下方任何相关数值的总和 # 这样做是为了防止 AI 做出代价高昂却只能带来微小效率提升的移动 |  |  |
| FRONT_OR_HQ_UNIT_DISPARITY_FOR_MOVE_TRAVEL_TIME_FACTOR | 0.02 | # 每一天行程时间会向除数增加此数值 |
| FRONT_OR_HQ_ACTIVE_WAR_MOVE_FACTOR | 1.0 | # 如果将军处于活跃战争前线，则向除数增加此数值 |
| # 以下数值均在检查 FRONT_IMPORTANCE_MIN_SCORE *之后*应用，因此这些乘数不会影响 AI 对某条前线/总部（HQ）是否重视的资格判定 |  |  |
| FRONT_CAPITAL_HQ_IMPORTANCE_MULT | 2.0 | # 威胁到 AI 自身首都总部的 frontline，其重要性乘以此数值 |
| FRONT_NON_WAR_ZONE_IMPORTANCE_MULT | 1.0 | # 未受敌方争夺的前线，其重要性乘以此数值 |
| FRONT_WAR_ZONE_IMPORTANCE_MULT | 1.5 | # *正*受敌方争夺的前线，其重要性乘以此数值 |
| HQ_LANDLOCKED_IMPORTANCE_MULT | 0.0 | # 无海岸的友方总部，其重要性乘以此数值 |
| HQ_COASTAL_NON_WAR_ZONE_IMPORTANCE_MULT | 0.5 | # 有海岸且未遭受海上入侵的友方总部，其重要性乘以此数值 |
| HQ_COASTAL_WAR_ZONE_IMPORTANCE_MULT | 3.0 | # *正*遭受海上入侵的友方总部，其重要性乘以此数值 |
| FRONT_IN_DISADVANTAGE_FACTOR | 10.0 | # 如果将军处于劣势的活跃战争前线，则向除数增加此数值 |
| # AI 在战斗力与士气/组织度达到何种比例时才会发起进攻 |  |  |
| FRONT_MIN_OVERALL_STRENGTH_FACTOR_TO_ATTACK | 0.8 | # 前线上的总体力量投射必须至少达到敌方的此倍数，AI 才会想要进攻 |
| FRONT_MIN_INDIVIDUAL_ARMY_STRENGTH_FACTOR_TO_ATTACK | 0.95 | # 前线上同盟编队的平均力量投射必须至少达到此倍数，AI 才会想要进攻 |
| FRONT_MIN_MORALE_TO_ATTACK | 0.8 | # 以最高士气（1）为基准的比例 |
| FRONT_MIN_ORGANIZATION_TO_ATTACK | 0.4 | # 以编队最高组织度为基准的比例 |
| FRONT_NO_WARGOAL_MIN_STRENGTH_FACTOR_TO_ATTACK | 4.0 | # 如果敌方战区中没有仍未夺取的明确战争目标州，则需要至少达到此强度倍数才会推进 |
| # 以下数据用于海军上将命令（AdmiralOrders）： |  |  |
| BLOCKADE_STATE_TRADE_VOLUME_MILITARY_GOODS_WEIGHT | 5.0 | # 基于该州军用商品贸易量的州封锁评分权重 |
| BLOCKADE_STATE_TRADE_VOLUME_OTHER_GOODS_WEIGHT | 1.0 | # 基于该州其他商品贸易量的州封锁评分权重 |
| BLOCKADE_STATE_WEIGHT | 1 | # 基于总分的州封锁评分权重。此值越高，AI 越倾向于选择封锁该州而非该海域节点中的其他进攻性命令 |
| BLOCKADE_ORDER_LEVEL_DELTA_WEIGHT | 100 | # 基于该海军上将所提供封锁等级的海军上将命令评分权重 |
| BLOCKADE_ORDER_NAVY_STRENGTH_RATIO_MULT | 1 | # 海军强度比例按此值提高封锁命令评分：score = score * (1 + navy strength ratio * this) |
| FLEET_MISSION_INTERCEPT_WEIGHT | 1.5 | # 在海域中其他任务之间的拦截（保卫总部海岸）评分权重 |
| FLEET_MISSION_PROJECT_POWER_WEIGHT | 1.0 | # 在海域中其他任务之间的力量投射任务评分权重 |
| FLEET_MISSION_BLOCKADE_WEIGHT | 3.0 | # 在海域中其他任务之间的封锁评分权重 |
| FLEET_MISSION_RAID_SUPPLY_WEIGHT | 3.0 | # 在海域中其他任务之间的袭击军事补给评分权重 |
| FLEET_MISSION_PROTECT_SUPPLY_WEIGHT | 2.0 | # 在海域内各任务中，护航军事补给的任务评分权重 |
| FLEET_MISSION_PORT_BOMBARDMENT_WEIGHT | 1.0 | # 在海域内各任务中，炮击港口的任务评分权重 |
| FLEET_MISSION_PIRACY_WEIGHT | 1.0 | # 在海域内对中立国与敌国进行商业袭扰的任务评分权重 |
| FLEET_MISSION_PRIVATEER_WEIGHT | 1.0 | # 在海域内对敌国进行商业袭扰的任务评分权重 |
| FLEET_MISSION_HUNT_PIRATES_WEIGHT | 1.0 | # 在海域内防御商业袭扰的任务评分权重 |
| FLEET_MISSION_DEFEND_COAST_WEIGHT | 5.0 | # 防御海岸以免遭海上登陆与封锁的任务评分权重 |
| FLEET_TASK_ASSIGNMENT_RANDOM_SPICE | 0.5 | # 舰队任务选择的随机因子，同时决定任务黏性以防止任务来回切换 |
| FLEET_SEA_PROVINCE_ASSIGNMENT_STICKINESS | 1.5 | # 当舰队已被分配到某海域时，该舰队在该海域的评分会乘以该系数 |
| FLEET_SEA_PROVINCE_SETTLING_DAYS | 60 | # 驻留黏性倍率从最大值衰减到 1 倍所需的天数 |
| FLEET_SEA_PROVINCE_SETTLING_STICKINESS_MULT | 4.0 | # 刚被分配的舰队（第 0 天）的额外黏性倍率，会在 SETTLING_DAYS 内线性衰减到 1 倍 |
| FLEET_SEA_PROVINCE_HOME_HQ_SCORE | 0.5 | # 该值越高，舰队越倾向于防守其本土总司令部 |
| FLEET_SEA_PROVINCE_DISTANCE_SCORE | 1 | # 该值越高，到海域的距离对舰队任务评分的影响越大 |
| FLEET_SEA_PROVINCE_DISTANCE_SCORE_MAX_DISTANCE | 5000 | # 距离评分基于有效补给距离（以友方港口折扣进行寻路）从 0 到该值线性计算 |
| FLEET_RAID_CONVOYS_TASK_SCORE_FROM_STRENGTH | 2 | # 该值越高，护航队袭击强度高的舰队越倾向于执行护航队袭击任务 |
| FLEET_ESCORT_CONVOYS_TASK_SCORE_FROM_DEFENSE | 2 | # 该值越高，护航队护卫强度高的舰队越倾向于执行护航队护卫任务 |
| FLEET_PROJECT_INTEREST_TASK_SCORE_FROM_INTEREST_PROJECTION | 2 | # 该值越高，利益投射强度高的舰队越倾向于执行利益投射任务 |
| FLEET_DEFEND_FROM_CONVOY_RAID_TASK_SCORE_FROM_PROTECTION | 2 | # 按舰队所能保护的护航队数量进行缩放，并计入该任务的舰队评分 |
| FLEET_DEFEND_FROM_NAVAL_INVASION_TASK_SCORE_FROM_PROJECTION | 0.5 | # 该值越高，力量投射能力强的舰队越倾向于防御海上登陆并阻止敌方登陆 |
| FLEET_DEFEND_FROM_NAVAL_INVASION_TASK_SCORE_FROM_SHIPS | 0.1 | # 按舰队拥有的舰船数量进行缩放，并计入该任务的舰队评分 |
| FLEET_DEFEND_FROM_BLOCKADE_TASK_SCORE_FROM_STRENGTH | 1.5 | # 该值越高，舰船实力强的舰队越倾向于防御敌方封锁 |
| FLEET_BLOCKADE_TASK_SCORE_FROM_STRENGTH | 1.5 | # 该值越高，封锁强度高的舰队越倾向于封锁敌方州 |
| FLEET_BLOCKADE_TASK_SCORE_NO_HOSTILES | 0.5 | # 当不存在敌方时，给予优先度加成 |
| FLEET_BLOCKADE_TASK_SCORE_STRENGTH_RATIO_FACTOR | 1.5 # 敌方/友方之间的实力比对权重的影响程度 |  |
| FLEET_PORT_BOMBARDMENT_TASK_SCORE_NO_HOSTILES | 0.5 | # 当不存在敌方时，给予优先度加成 |
| FLEET_PORT_BOMBARDMENT_TASK_SCORE_STRENGTH_RATIO_FACTOR | 1.5 # 敌方/友方之间的实力比对权重的影响程度 |  |
| FLEET_INTERCEPT_TASK_SCORE_STRENGTH_RATIO_FACTOR | 3.0 # 敌方/友方之间的实力比对权重的影响程度 |  |
| FLEET_MISSION_MAX_SEA_REGIONS | 3 | # 舰队任务最多可由 AI 指定的海域数量 |
| RAID_CONVOYS_ORDER_SCORE | 30 | # 海军上将袭击运输船命令的分数 |
| INTERCEPT_ORDER_SCORE | 40 | # 海军上将拦截命令的分数 |
| SEA_NODE_OFFENSIVE_FLEET_SHIPPING_LANES_WEIGHT | 0.5 | # 基于总分的海域节点分数权重，用于 AI 袭击运输船。该值越高，AI 越优先选择有敌方运输船可袭击的海域节点 |
| SEA_NODE_OFFENSIVE_FLEET_STATE_BLOCKADE_WEIGHT | 0.5 | # 基于总分的海域节点分数权重，用于 AI 封锁州。该值越高，AI 越优先选择有可封锁州的海域节点 |
| RAID_CONVOYS_LANE_SIZE_FACTOR | 0.5 | # 乘以目标航运线路所使用的运输船数量 |
| ESCORT_CONVOYS_ABSOLUTE_LANE_SIZE_FACTOR | 0.1 | # 航线上每实际使用的运输船所获得的分数 |
| ESCORT_CONVOYS_LANE_SIZE_FACTOR_MAX | 200 | # 总线路规模系数不能超过此值 |
| ESCORT_CONVOYS_PORT_CONNECTION_WAR_MULT | 0.1 | # 战时支持海外港口的航运线路分数乘以此系数 |
| ESCORT_CONVOYS_PORT_CONNECTION_PEACE_MULT | 1.0 | # 非战时支持海外港口的航运线路分数乘以此系数 |
| # 以下数据用于决定应优先殖民哪些州 |  |  |
| NUM_GROWING_COLONIES_BASE | 1 | # AI 同时维持扩张的殖民地数量（基础值） |
| NUM_GROWING_COLONIES_SCALED | 0.01 | # 每达到此数量的殖民扩张点数，同时扩张的殖民地增加 1 个 |
| NUM_GROWING_COLONIES_MAX | 5 | # 无论殖民扩张点数有多少，同时扩张的殖民地数量不超过此值 |
| COLONY_BASE_WEIGHT | 50 |  |
| COLONY_POPULATION_WEIGHT | 0.2 | # 每 10000 人口 |
| COLONY_ARABLE_LAND_WEIGHT | 10 |  |
| COLONY_ADJACENT_WEIGHT_MULT | 10.0 |  |
| COLONY_UNCONTESTED_WEIGHT_MULT | 3.0 |  |
| COLONY_RANDOM_FACTOR | 2 |  |
| # 此项决定 AI 在应征兵员尚未被征召时，会尝试为其提供多少所需军用商品 |  |  |
| CONSCRIPTION_CENTER_MILITARY_SPENDING_TARGET_BASE | 0.05 | # 乘以国家应征兵员与常备军的比例 |
| CONSCRIPTION_CENTER_MILITARY_SPENDING_TARGET_MAX | 0.25 | # 支出目标不能超过此值 |
| # 以下数据用于决定 AI 如何投资机构 |  |  |
| INSTITUTION_INVESTMENT_RANDOM_FACTOR | 1.0 | # 该值越高，AI 的机构选择越随机 |
| INSTITUTION_CURRENT_INVESTMENT_DIVISOR | 0.25 | # 机构的分数除以 1 +（首级之后的当前等级数 * 此值） |
| MAX_INSTITUTION_SPENDING_BASE | 0.015 | # AI 在机构上的行政力支出不会超过此值（按每周 GDP 缩放） |
| MAX_INSTITUTION_SPENDING_PER_INSTITUTION | 0.005 | # 国家每拥有一个机构，便在 MAX_INSTITUTION_SPENDING_BASE 基础上增加此值 |
| INSTITUTION_SPENDING_INCREASE_SPENDING_RATIO | 1.0 | # 若当前机构支出加上新增机构支出小于或等于最大支出 * 此值，则尝试提升某些机构 |
| INSTITUTION_SPENDING_DECREASE_SPENDING_RATIO | 2.0 | # 若当前机构支出至少达到最大支出 * 此值，则尝试降级某些机构 |
| # 以下数据用于计算 AI 在分配每周货币收入时对不同事项赋予的权重 |  |  |
| MONEY_SPENDING_RANDOM_FACTOR | 2.0 | # 该值越高，AI 新的货币支出越随机 |
| MONEY_SPENDING_MAX_RATIO_TO_REMOVE_SHOULD_HAVE | 1.05 | # AI 的收入支出比需要低至何等程度，才会考虑削减"应有"（should-have）项目的支出 |
| MONEY_SPENDING_MAX_RATIO_TO_REMOVE_WANTS_TO_HAVE | 1.10 | # AI 的收入支出比需要低至何等程度，才会考虑削减"想要"（wants-to-have）项目的支出 |
| MONEY_SPENDING_MAX_RATIO_TO_REMOVE_NICE_TO_HAVE | 1.20 | # AI 的收入与支出比需要低到多少，才会考虑削减“可有可无”项目的支出 |
| MONEY_SPENDING_MIN_RATIO_TO_ADD_SHOULD_HAVE | 1.2 | # AI 在增加“应当拥有”项目的支出后，希望达到的收入与支出比 |
| MONEY_SPENDING_MIN_RATIO_TO_ADD_WANTS_TO_HAVE | 1.3 | # AI 在增加“想要拥有”项目的支出后，希望达到的收入与支出比 |
| MONEY_SPENDING_MIN_RATIO_TO_ADD_NICE_TO_HAVE | 1.4 | # AI 在增加“可有可无”项目的支出后，希望达到的收入与支出比 |
| MONEY_SPENDING_MIN_SURPLUS_TO_ADD_SHOULD_HAVE | 2000 | # AI 在增加“应当拥有”项目的支出后，希望拥有的绝对金额盈余 |
| MONEY_SPENDING_MIN_SURPLUS_TO_ADD_WANTS_TO_HAVE | 5000 | # AI 在增加“想要拥有”项目的支出后，希望拥有的绝对金额盈余 |
| MONEY_SPENDING_MIN_SURPLUS_TO_ADD_NICE_TO_HAVE | 10000 | # AI 在增加“可有可无”项目的支出后，希望拥有的绝对金额盈余 |
| MONEY_SPENDING_MIN_SURPLUS_TO_IGNORE_RATIO_FOR_SHOULD_HAVE | 15000 | # 如果 AI 拥有这笔绝对金额的盈余，那么无论收入比如何，增加“应当拥有”项目的支出总是可行的 |
| MONEY_SPENDING_MIN_SURPLUS_TO_IGNORE_RATIO_FOR_WANTS_TO_HAVE | 30000 | # 如果 AI 拥有这笔绝对金额的盈余，那么无论收入比如何，增加“想要拥有”项目的支出总是可行的 |
| MONEY_SPENDING_MIN_SURPLUS_TO_IGNORE_RATIO_FOR_NICE_TO_HAVE | 50000 | # 如果 AI 拥有这笔绝对金额的盈余，那么无论收入比如何，增加“可有可无”项目的支出总是可行的 |
| MONEY_SPENDING_ACCEPTABLE_WAR_DEBT | 0.5 | # 如果 AI 的债务占上限的比例低于此百分比，则在战时避免为“想要拥有”及以上等级的项目削减成本 |
| MONEY_SPENDING_MIN_RATIO_TO_CONSIDER_GOLD_RESERVES | 0.8 | # AI 的收入与支出比需要低到多少，才会无论黄金储备多么充足都尝试削减支出（在和平时） |
| MONEY_SPENDING_MIN_WEEKS_OF_GOLD_RESERVES_TO_NOT_REMOVE_SHOULD_HAVE | 20 | # 如果我们的黄金储备足以维持当前支出这么长时间，则不削减“应当拥有”项目的支出 |
| MONEY_SPENDING_MIN_WEEKS_OF_GOLD_RESERVES_TO_NOT_REMOVE_WANTS_TO_HAVE | 40 | # 如果我们的黄金储备足以维持当前支出这么长时间，则不削减“想要拥有”项目的支出 |
| MONEY_SPENDING_MIN_GOLD_RESERVE_FRACTION_TO_ADD_SHOULD_HAVE | 0.1 | 如果我们的黄金储备没有至少达到这个比例，则不增加“应当拥有”项目的支出 |
| MONEY_SPENDING_MIN_GOLD_RESERVE_FRACTION_TO_ADD_WANTS_TO_HAVE | 0.2 | # 如果我们的黄金储备没有至少达到这个比例，则不增加“想要拥有”项目的支出 |
| MONEY_SPENDING_MIN_GOLD_RESERVE_FRACTION_TO_ADD_NICE_TO_HAVE | 0.3 | # 如果我们的黄金储备没有至少达到这个比例，则不增加“可有可无”项目的支出 |
| MONEY_SPENDING_LAND_THREAT_THRESHOLD | 0.25 | # 如果一个敌对国家的陆军比 AI 大超过这个幅度，AI 就希望增加军事支出 |
| MONEY_SPENDING_NAVY_THREAT_THRESHOLD | 0.50 | # 如果一个敌对国家的海军比 AI 大超过这个幅度，AI 就希望增加军事支出 |
| MONEY_SPENDING_PRESTIGE_RIVAL_THRESHOLD | 0.5 | # 如果一个竞争对手的威望比 AI 高出这个幅度，AI 就希望增加美术学院（art academy）的支出 |
| MONEY_SPENDING_BELOW_CRITICAL_THRESHOLD_MULTIPLIER | 5.0 | # 将某些低于临界阈值的项目（如下方 CRITICAL_THRESHOLD defines 所指定）的支出评分乘以这个倍数 |
| MONEY_SPENDING_MILITARY_CRITICAL_THRESHOLD | 0.5 | # 如果兵营的实际数量与期望数量之比低于此值，AI 将不考虑进一步缩减兵营规模 |
| MONEY_SPENDING_MILITARY_EXCESSIVE_THRESHOLD | 2.0 | # 如果兵营的实际数量与期望数量之比高于此值，AI 会在需要削减开支时将其视为目标 |
| MONEY_SPENDING_MILITARY_WRONG_UNIT_TYPE_MULTIPLIER | 0.01 | # 对于缺乏我们想要解散的战斗单位类型的兵营，削减开支的评分乘数 |
| MONEY_SPENDING_FORTIFICATIONS_CRITICAL_THRESHOLD | 0.5 | # 如果防御工事的实际数量与期望数量之比低于此值，AI 会提高建造它们的优先级 |
| MONEY_SPENDING_CONSTRUCTION_TOO_LARGE_INVESTMENT_POOL_FACTOR | 0.75 | # 此值越高，当投资池相对于建造能力过大时，AI 就越会加大对建造的投资（上限为 1） |
| MONEY_SPENDING_CONSTRUCTION_CRITICAL_THRESHOLD | 0.75 | 如果建造的实际产出与期望产出之比低于此值，AI 会认为增加产出非常重要 |
| MONEY_SPENDING_CONSTRUCTION_EXCESSIVE_THRESHOLD | 1.05 | # 如果建造的实际产出与期望产出之比至少达到此值，AI 会认为有此产出更好 |
| MONEY_SPENDING_SHIP_CONSTRUCTION_CRITICAL_THRESHOLD | 0.75 | # 如果舰船建造的实际产出与期望产出之比低于此值，AI 会认为增加产出非常重要 |
| MONEY_SPENDING_SHIP_CONSTRUCTION_EXCESSIVE_THRESHOLD | 1.05 | # 如果舰船建造的实际产出与期望产出之比至少达到此值，AI 会认为有此产出更好 |
| MONEY_SPENDING_INNOVATION_DESIRED_THRESHOLD | 1.0 | # 如果创新产出相对于上限劣于此值，AI 会认为改进它很重要 |
| MONEY_SPENDING_INNOVATION_EXCESSIVE_THRESHOLD | 1.25 | CONSUMPTION_TAX_MAX_NUM_TAXED_GOODS_PER_MISSING_TAX_TYPE# 如果创新产出相对于上限至少达到此值，AI 会认为有此产出更好 |
| MONEY_SPENDING_SUPPLY_NETWORK_CRITICAL_THRESHOLD | 0.75 | # 如果补给网络劣于此值，AI 会认为改善它是当务之急 |
| MONEY_SPENDING_SUPPLY_NETWORK_DESIRED_THRESHOLD | 1.25 | # 如果补给网络劣于此值，AI 希望改善它 |
| MONEY_SPENDING_BUREAUCRACY_CRITICAL_THRESHOLD | 1.0 | # 如果行政力收支比劣于此值，AI 会认为改善它是当务之急 |
| MONEY_SPENDING_BUREAUCRACY_DESIRED_THRESHOLD | 1.20 | # 如果行政力收支比劣于此值，AI 希望改善它 |
| MONEY_SPENDING_BUREAUCRACY_EXCESSIVE_THRESHOLD | 1.30 | # 如果行政力收支比优于此值，AI 将不会改善它 |
| MONEY_SPENDING_INFRASTRUCTURE_CRITICAL_THRESHOLD | 0.80 | # 如果基础设施的产出与使用之比劣于此值，AI 会认为改善它是当务之急 |
| MONEY_SPENDING_INFRASTRUCTURE_DESIRED_THRESHOLD | 1.20 | # 如果基础设施的产出与使用之比劣于此值，AI 希望改善它 |
| # 以下数据用于计算 AI 对特定政府建筑的权重 |  |  |
| GOVERNMENT_BUILDING_BASE_VALUE | 1000 | # 如果建筑未脚本设定 ai_value |
| GOVERNMENT_BUILDING_FAVORED_GOODS_FACTOR | 0.25 | # 对于 AI 倾向于进口或出口的每个建筑产出，总权重乘以（1 + 此值） |
| GOVERNMENT_BUILDING_DISFAVORED_GOODS_FACTOR | -0.10 | # 对于 AI 不倾向的每个建筑产出商品，总权重乘以（1 + 此值） |
| GOVERNMENT_BUILDING_NO_AVAILABLE_WORKFORCE_FACTOR | 0.01 | # 如果该州缺乏足够的劳动力来填充该建筑的岗位，总权重乘以此值 |
|  |  | # 以下数据用于计算 AI 将新的政府建筑选址在何处 |
| GOVERNMENT_BUILDING_STATE_CAPITAL_FACTOR | 250 | # 对于特定类型的政府建筑位于首都时，加上此评分 |
| GOVERNMENT_BUILDING_STATE_MARKET_CAPITAL_FACTOR | 250 | # 位于市场首都的某些类型政府建筑加上此分数 |
| GOVERNMENT_BUILDING_STATE_ARMY_NON_ACCEPTED_POP_FACTOR | -250 | # 将此分数乘以该州受歧视人口的占比 |
| GOVERNMENT_BUILDING_STATE_ARMY_ACCEPTED_POP_FACTOR | 250 | # 将此分数乘以该州已接受人口的占比 |
| GOVERNMENT_BUILDING_STATE_NAVY_NON_ACCEPTED_POP_FACTOR | -250 | # 将此分数乘以该州受歧视人口的占比 |
| GOVERNMENT_BUILDING_STATE_NAVY_ACCEPTED_POP_FACTOR | 250 | # 将此分数乘以该州已接受人口的占比 |
| GOVERNMENT_BUILDING_STATE_UNINCORPORATED_MULT | 0.25 | # 若该州为非整合州，则将分数乘以此值 |
| GOVERNMENT_BUILDING_STATE_MISSING_QUALIFICATIONS_MULT | 0.10 | # 若缺乏足够的资质来为该建筑配置人员，则将分数乘以此值 |
| GOVERNMENT_BUILDING_STATE_MISSING_INFRASTRUCTURE_DIV | 0.50 | # 将分数除以（1 + 此值 * 新增该建筑后仍缺失的基础设施数量） |
| GOVERNMENT_BUILDING_STATE_POP_CONSTRUCTION_SECTOR_IMPORTANCE_THRESHOLD | 250000 | # 州人口超过此数量时，AI 认为在该州拥有一个建造部门十分重要 |
| GOVERNMENT_BUILDING_STATE_POP_CONSTRUCTION_SECTOR_IMPORTANCE_MULT | 1.5 | # 在为建造部门第一级评分时，若州 GDP 至少达到上述值，则将分数乘以此值 |
| # 以下数据用于计算 AI 对特定补贴的重视程度 |  |  |
| SUBSIDIZE_BASE_VALUE | 1000 |  |
| SUBSIDIZE_SHARE_OF_INFRA_FACTOR | 4000 | # 若某建筑提供了州区域 100% 的基础设施，其补贴价值有多高 |
| SUBSIDIZE_SHARE_OF_SUPPLY_FACTOR | 2000 | # 若某建筑提供了市场上某商品 100% 的卖出订单，其补贴价值有多高 |
| SUBSIDIZE_FAVORED_GOODS_MULT | 1.5 | # 对于 AI 希望高供给的商品，供给占比系数乘以此值 |
| SUBSIDIZE_DISFAVORED_GOODS_MULT | 0.75 | # 对于 AI 不青睐的商品，供给占比系数乘以此值 |
| # 以下数据用于计算 AI 对花费统治力的不同用途的重视程度 |  |  |
| AUTHORITY_SPENDING_RANDOM_FACTOR | 0.5 | # 此值越高，AI 新的统治力支出就越随机 |
| COMPANY_CHARTER_AUTHORITY_SPENDING_PERCENTAGE | 0.15 | # 我们希望国家将统治力开支用于此用途的比例 |
| PROMOTION_BASE_VALUE | 50 | # 以下数据用于计算 AI 对扶持某个利益集团的重视程度 |
| SUPPRESSION_BASE_VALUE | 75 | # 以下数据用于计算 AI 对压制某个利益集团的重视程度 |
| # 以下数据用于计算 AI 对消费税的重视程度 |  |  |
| CONSUMPTION_TAX_INCOME_VALUE | 10 | # 每一百分点州支出对应的税收价值（随后乘以该商品的相对统治力成本） |
| CONSUMPTION_TAX_STAPLE_MULT | 0.5 | # 对必需品征税的意愿乘以此值 |
| CONSUMPTION_TAX_LUXURY_MULT | 2.0 | # 对奢侈品征税的意愿乘以此值 |
| CONSUMPTION_TAX_LOW_INCOME_THRESHOLD | 1.25 | # 收入与支出之比低于此阈值时，消费税为必需品 |
| CONSUMPTION_TAX_HIGH_INCOME_THRESHOLD | 1.5 | # 收入与支出之比达到此阈值时应取消消费税（前提是取消后不会低于此值） |
| CONSUMPTION_TAX_MAX_NUM_TAXED_GOODS_BASE | 0 | # AI 希望征税的商品数量基础上限 |
| CONSUMPTION_TAX_MAX_NUM_TAXED_GOODS_PER_MISSING_TAX_TYPE | 2 | # AI 每缺少一种其他税收类型，其希望征税的商品数量上限便增加此值 |
| # 关于 AI 在何处建造贸易中心（Trade Center）的 GDP 限制——注意：降低这些数值可能对性能产生不利影响！ |  |  |
| TRADE_CENTER_MINIMUM_GDP_MARKET_CAPITAL | 100000 | # 针对市场首都州，年 GDP |
| TRADE_CENTER_MINIMUM_GDP_NON_MARKET_CAPITAL | 500000 | # 针对其他所有州，年 GDP |
| TRADE_CENTER_MINIMUM_GDP_NON_COASTAL_MULT | 2.0 | # 将非沿海州的 GDP 阈值乘以该系数（加法） |
| TRADE_CENTER_MINIMUM_GDP_UNRECOGNIZED_MULT | 2.0 | # 将未被承认国家的 GDP 阈值乘以该系数（加法） |
| TRADE_CENTER_MINIMUM_GDP_PASSED_YEARS_MULT | 0.02 | # 上述数值乘以 1 +（自游戏开始的年数 * 该系数）（加法） |
| # 以下数据用于计算 AI 对某生产建筑的权重 |  |  |
| PRODUCTION_BUILDING_RANDOM_FACTOR | 10.0 | # 该数值越高，AI 建造行为的随机性越强 |
| PRODUCTION_BUILDING_STATE_RANDOM_FACTOR | 0.5 | # 该数值越高，AI 在选择建造建筑类型的州时随机性越强 |
| PRODUCTION_BUILDING_STATE_NO_AVAILABLE_WORKFORCE_FACTOR | 0.05 | # 在选择建造州时，无可用劳动力的州的分数乘以该系数 |
| PRODUCTION_BUILDING_BASE_VALUE | 1000 | # 若建筑未脚本指定 ai_value 时使用 |
| PRODUCTION_BUILDING_NO_AVAILABLE_WORKFORCE_FACTOR | 0.25 | # 若州缺乏足够的劳动力来为建筑配备人员，总权重乘以该系数 |
| PRODUCTION_BUILDING_GOODS_PROFIT_FACTOR | 5000 | # 每英镑预测建筑利润（除以每级雇员数） |
| PRODUCTION_BUILDING_GOODS_DEFICIT_FACTOR | 10000 | # 每英镑预测建筑亏损（除以每级雇员数，并乘以一个负值） |
| PRODUCTION_BUILDING_GOODS_DEFICIT_SUBSIDIZE_FACTOR | 5000 | # 对受补贴的建筑，覆盖 PRODUCTION_BUILDING_GOODS_DEFICIT_FACTOR |
| PRODUCTION_BUILDING_PRODUCED_VALUE_FACTOR | 0.25 | # 每英镑基础价值的已生产商品 |
| PRODUCTION_BUILDING_PRODUCED_TRADE_CAPACITY_FACTOR | 10000 | # 每单位已生产的贸易能力，乘以该州的可用贸易潜力并除以州 GDP |
| PRODUCTION_BUILDING_PRODUCED_TRADE_CAPACITY_GDP_ADDED_FOR_DIVISOR | 10000 | # 在对 PRODUCTION_BUILDING_PRODUCED_TRADE_CAPACITY_FACTOR 进行除法时加到州 GDP 上 |
| PRODUCTION_BUILDING_PRODUCED_TRADE_CAPACITY_EXPECTED_REVENUE_PER_UNIT | 25 | # 每单位贸易能力大致预期产生约这么多收入，用于预测新贸易中心的收入 |
| PRODUCTION_BUILDING_INCORPORATED_INFRASTRUCTURE_USAGE_FACTOR | 0.05 | # 在已整合州中，总权重除以（1 + 该系数 * 建筑基础设施使用量） |
| PRODUCTION_BUILDING_UNINCORPORATED_INFRASTRUCTURE_USAGE_FACTOR | 1.0 | # 在未整合州中，总权重除以（1 + 该系数 * 建筑基础设施使用量） |
| PRODUCTION_BUILDING_INPUT_NO_LOCAL_PRODUCTION_FACTOR | -0.5 | # 建筑每消耗一单位货币价值的、本州不生产但市场内建筑*确实*生产的商品，就将该值加到该建筑上 |
| PRODUCTION_BUILDING_OUTPUT_NO_LOCAL_CONSUMPTION_FACTOR | -0.5 | # 建筑每生产一单位货币价值的、本州不消费但市场内建筑*确实*消费的商品，就将该值加到该建筑上 |
| PRODUCTION_BUILDING_OUTPUT_HIGH_PRICE_THRESHOLD | 1.25 | # 应用下方“高价”修正的基准价格下限阈值倍率 |
| PRODUCTION_BUILDING_OUTPUT_HIGH_PRICE_FACTOR | 0.25 | # 建筑每生产一单位货币价值的、价格超过高价阈值且高于基准价格的商品，就将该值加到该建筑上 |
| PRODUCTION_BUILDING_OUTPUT_HIGH_PRICE_WANTS_HIGH_SUPPLY_FACTOR | 0.75 | # 建筑每生产一单位货币价值的、价格超过高价阈值且我们希望其保持高供给的商品，就将该值加到该建筑上 |
| PRODUCTION_BUILDING_OUTPUT_HIGH_PRICE_LOCAL_CONSUMPTION_MULTIPLIER | 2.0 | # 若州内任意建筑消费该商品，所有高价相关系数都乘以该值 |
| PRODUCTION_BUILDING_OUTPUT_LOW_PRICE_THRESHOLD | 0.75 | # 适用下方“低价”修正的基础价格上限阈值乘数 |
| PRODUCTION_BUILDING_OUTPUT_LOW_PRICE_FACTOR | -0.5 | # 该建筑每产出 1 单位货币价值低于低价阈值的商品，即将此值加到该建筑上 |
| PRODUCTION_BUILDING_SUBSIDIZE_PRICE_FACTOR_MULT | 1.25 | # 对 AI 会考虑补贴的建筑，将其价格系数的效果乘以该值 |
| PRODUCTION_BUILDING_OUTPUT_NEW_GOODS_FACTOR | 100.0 | # 对市场上目前没有但 AI 希望优先获取的每 1 单位货币价值的商品，即将此值加到该建筑上 |
| PRODUCTION_BUILDING_OUTPUT_NEW_GOODS_STATE_INCORPORATED_POPULATION_THRESHOLD | 250000 | # 当 AI 在州而非市场层面（因地方商品原因）优先“新商品”时，只关注人口至少达到该数值的已合并州 |
| PRODUCTION_BUILDING_OUTPUT_NEW_GOODS_STATE_UNINCORPORATED_POPULATION_THRESHOLD | 1000000 | # 当 AI 在州而非市场层面（因地方商品原因）优先“新商品”时，只关注人口至少达到该数值的未合并州 |
| PRODUCTION_BUILDING_OUTPUT_WANTED_INDUSTRIAL_GOODS_FACTOR | 0.25 | # 对国内未生产过剩且被建筑使用的每 1 单位货币价值的工业商品，即将此值加到该建筑上 |
| PRODUCTION_BUILDING_OUTPUT_WANTED_MILITARY_GOODS_FACTOR | 0.25 | # 对国内未生产过剩且被建筑使用的每 1 单位货币价值的军事商品，即将此值加到该建筑上 |
| PRODUCTION_BUILDING_OUTPUT_NEEDED_INDUSTRIAL_GOODS_FACTOR | 0.5 | # 对国内生产不足且被建筑使用的每 1 单位货币价值的工业商品，即将此值加到该建筑上 |
| PRODUCTION_BUILDING_OUTPUT_NEEDED_MILITARY_GOODS_FACTOR | 0.5 | # 对国内生产不足且被建筑使用的每 1 单位货币价值的军事商品，即将此值加到该建筑上 |
| PRODUCTION_BUILDING_FAVORED_GOODS_FACTOR | 0.5 | # 对 AI 倾向的每 1 单位货币价值的建筑商品产出，即将此值加到该建筑上 |
| PRODUCTION_BUILDING_DISFAVORED_GOODS_FACTOR | -0.25 | # 对 AI 不倾向的每 1 单位货币价值的建筑商品产出，即将此值加到该建筑上 |
| PRODUCTION_BUILDING_MISSING_QUALIFICATIONS_MULT | 0.50 | # 若资质不足以满足该建筑的员工需求，分数乘以该值（目前已禁用） |
| PRODUCTION_BUILDING_DESIRED_INFRASTRUCTURE_SURPLUS | 2 | # 若州内基础设施“盈余”低于该值，AI 希望改善它 |
| PRODUCTION_BUILDING_FREE_INFRASTRUCTURE_TARGET_WHEN_LACKING_WORKFORCE | 5 | # 缺乏劳动力时，一旦可用基础设施不高于该值，AI 就会停止在该州进行建造 |
| PRODUCTION_BUILDING_EXCESSIVE_INFRASTRUCTURE_SURPLUS | 10 | # 若州内基础设施“盈余”至少达到该值，AI 不希望改善它 |
| PRODUCTION_BUILDING_REDUCE_SHORTAGE_MULT | 5 | # 若正在减少该州地区的短缺，分数乘以该值 |
| PRODUCTION_BUILDING_INCREASE_SHORTAGE_MULT | 0.01 | # 若正在增加该州地区的短缺，分数乘以该值 |
| PRODUCTION_BUILDING_OTHER_BUILDING_TYPES_UNDER_CONSTRUCTION_DIV | 0.5 | # 分数除以 (1 + 此值 × 该州排队中的其他建筑类型数量) |
| PRODUCTION_BUILDING_LONG_CONSTRUCTION_TIME_THRESHOLD | 40 |  |
| PRODUCTION_BUILDING_LONG_CONSTRUCTION_TIME_MULT | 0.5 | # 若在建造业满负荷运转下（忽略 MAX_WEEKLY_CONSTRUCTION_PROGRESS）建造时间会超过 PRODUCTION_BUILDING_LONG_CONSTRUCTION_TIME_THRESHOLD 周，分数乘以该值 |
| PRODUCTION_BUILDING_VERY_LONG_CONSTRUCTION_TIME_THRESHOLD | 60 |  |
| PRODUCTION_BUILDING_VERY_LONG_CONSTRUCTION_TIME_MULT | 0.25 | # 如果在建造业满负荷运转（忽略 MAX_WEEKLY_CONSTRUCTION_PROGRESS）时建造时间会超过 PRODUCTION_BUILDING_VERY_LONG_CONSTRUCTION_TIME_THRESHOLD 周，则分数乘以该值 |
| PRODUCTION_BUILDING_FOREIGN_INVESTMENT_HAS_RECENT_NATIONALIZATION_MULT | 0.1 | # 如果该建造是对一个近期国有化过投资国所持有建筑的国家的对外投资，则分数乘以该值 |
| PRODUCTION_BUILDING_FOREIGN_INVESTMENT_COMPANY_MULT | 1.5 | # 如果该建造是由至少拥有一家该建筑类型已成立公司的国家进行的对外投资，则分数乘以该值 |
| # 政府建造在决定于何处建造时，对本土州应用此乘数 |  |  |
| GOVERNMENT_CONSTRUCTION_DOMESTIC_INVESTMENT_BIAS | 2.0 |  |
| GOVERNMENT_CONSTRUCTION_SUBJECT_INVESTMENT_BIAS | 1.5 |  |
| # AI 在选择下一个计划成立的公司所对应的州时，更有可能选择满足 ai_construction_targets 条件的州 # 例如，在试图成立 company_lkab 时，它更有可能选择 Norrland # 以下数值分别决定政府投资与私人投资的确切权重 # 权重分为两组：一组作用于建筑类型整体（与其他建筑类型比较时），另一组仅在为该建筑类型选择州时应用 |  |  |
| GOVERNMENT_COMPANY_TARGET_BUILDING_TYPE_CONSTRUCTION_FACTOR | 5 |  |
| GOVERNMENT_COMPANY_TARGET_STATE_NO_BUILDING_CONSTRUCTION_FACTOR | 20 | # 当该州尚无目标建筑类型时应用 |
| GOVERNMENT_COMPANY_TARGET_STATE_WITH_BUILDING_CONSTRUCTION_FACTOR | 50 | # 当该州*已有*目标建筑类型时应用 |
| AUTONOMOUS_INVESTMENT_COMPANY_TARGET_BUILDING_TYPE_CONSTRUCTION_FACTOR | 5 |  |
| AUTONOMOUS_INVESTMENT_COMPANY_TARGET_STATE_NO_BUILDING_CONSTRUCTION_FACTOR | 20 | # 当该州尚无目标建筑类型时应用 |
| AUTONOMOUS_INVESTMENT_COMPANY_TARGET_STATE_WITH_BUILDING_CONSTRUCTION_FACTOR | 50 | # 当该州*已有*目标建筑类型时应用 |
| # 集体化比例中这么多的部分会转化为建筑自我投资的概率 # 在完全集体化下自我投资概率始终为 100% |  |  |
| AUTONOMOUS_INVESTMENT_SELF_INVESTMENT_CHANCE_FROM_COLLECTIVIZATION | 0.5 |  |
| PRODUCTION_BUILDING_TREATY_PORT_TRADE_CENTER_FACTOR | 5.0 | # 在选择建造地点时，条约港中贸易中心建筑的分数乘以该值 |
| PRODUCTION_BUILDING_TREATY_PORT_NON_TRADE_CENTER_FACTOR | 0.10 | # 在选择建造地点时，条约港中非贸易中心建筑的分数乘以该值 |
| # 以下系数仅应用于政府建造 |  |  |
| PRODUCTION_BUILDING_GOVERNMENT_CONSTRUCTION_MONOPOLY_MULT | 1.5 | # 如果我们在该建筑类型上拥有政府垄断，则分数乘以该值 |
| PRODUCTION_BUILDING_LOW_EMPLOYMENT_THRESHOLD | 0.8 | # AI 不会扩建就业低于此比例的建筑，除非这些建筑上周有雇佣 |
| # 以下系数仅应用于自主投资 |  |  |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_COMPANY_MULT | 2.0 | # 如果我们至少拥有一家该建筑类型的已成立公司，则分数乘以 1 + 该值，并按公司投资池占比相对公司历史投资量进行缩放 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_COMPANY_MONOPOLY_MULT | 3.0 | # 对有公司垄断的建筑，取代 PRODUCTION_BUILDING_COMPANY_MULT |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_COMPANY_CHARTERED_COUNTRY_MULT | 2.0 | # 若投资指向某公司的特许国家，则对上述公司权重施加的额外乘数 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_WANTED_COST_COVERAGE | 1 | # 若投资池中的资金低于此数值，则不进行任何自主建设 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_CONSTRUCTION_COST_DIVISOR_SCALING | 0.001 | # 自主投资池建设项目的价值除以（1 + 建设点数成本 × 此值） |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_RANDOM_FACTOR_MULT | 2.0 | # 对自主投资池建设项目，将 PRODUCTION_BUILDING_RANDOM_FACTOR 乘以此值 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_STATE_RANDOM_FACTOR_MULT | 1.5 | # 对自主投资池建设项目的州级随机因子，将 PRODUCTION_BUILDING_RANDOM_FACTOR 乘以此值 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PROFIT_FACTOR_MULT | 1.5 | # 对自主投资池建设项目，将 PRODUCTION_BUILDING_GOODS_PROFIT_FACTOR 乘以此值 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PROFIT_PRIVATIZE_FACTOR_MULT | 5.0 | # 对自主投资池建设项目，将 PRODUCTION_BUILDING_GOODS_PROFIT_FACTOR 乘以此值，提高有可私有化等级的建筑的权重 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PRODUCED_VALUE_FACTOR_MULT | 1.25 | # 对自主投资池建设项目，将 PRODUCTION_BUILDING_PRODUCED_VALUE_FACTOR 乘以此值 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PRODUCED_VALUE_PRIVATIZE_FACTOR_MULT | 0.5 | # 对自主投资池建设项目，将 PRODUCTION_BUILDING_PRODUCED_VALUE_FACTOR 乘以此值，提高有可私有化等级的建筑的权重 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PRODUCED_TRADE_CAPACITY_FACTOR_MULT | 1.5 | # 对自主投资池建设项目，将来自产出贸易能力的价值乘以此值 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PRODUCED_MODIFIER_FACTOR_MULT | 0.75 | # 对自主投资池建设项目，将来自产出修正器的价值乘以此值 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PRICE_COMPENSATION_FACTOR_MULT | 1.0 | # 对自主投资池建设项目，将高价/低价补偿因子乘以此值 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_BELOW_DESIRED_INFRASTRUCTURE_FACTOR_MULT | 0.25 | # 对自主投资池建设项目，将 PRODUCTION_BUILDING_BELOW_DESIRED_INFRASTRUCTURE_FACTOR 乘以此值 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_LOW_INVESTMENT_RESET_TIME | 12 | # 每隔此月数，重置各人口类型的历史建设数值，以确保系统能应对长期内的重大经济变化 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_MILITARY_GOODS_FACTOR_MULT | 1.5 | # 对自主投资池建设项目，将 PRODUCTION_BUILDING_OUTPUT_NEEDED_MILITARY_GOODS_FACTOR 和 PRODUCTION_BUILDING_OUTPUT_WANTED_MILITARY_GOODS_FACTOR 乘以此值 |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_INDUSTRIAL_GOODS_FACTOR_MULT | 4.0 | # 对自主投资池建设项目，将 PRODUCTION_BUILDING_OUTPUT_NEEDED_INDUSTRIAL_GOODS_FACTOR 和 PRODUCTION_BUILDING_OUTPUT_WANTED_INDUSTRIAL_GOODS_FACTOR 乘以此值 |
| # 当对外投资的累计价值超过对内投资的累计价值时，我们开始对国内自主建设项目的评分施加此偏向 # 计算公式为 1 + (（对外投资 / 对内投资 - 1）× AUTONOMOUS_INVESTMENT_DOMESTIC_INVESTMENT_BIAS) # 最终乘数的上限为 AUTONOMOUS_INVESTMENT_DOMESTIC_INVESTMENT_BIAS_MAX |  |  |
| AUTONOMOUS_INVESTMENT_DOMESTIC_INVESTMENT_BIAS | 2.0 |  |
| AUTONOMOUS_INVESTMENT_DOMESTIC_INVESTMENT_BIAS_MAX | 10.0 |  |
| # 每隔该月数，国内/国外投资的已保存数值会被重置为 0 # 这是为了确保游戏早期长期的国内投资不会产生过高的保存数值，以至于之后的任何投资都变得无关紧要 |  |  |
| AUTONOMOUS_INVESTMENT_DOMESTIC_INVESTMENT_BIAS_RESET_TIME_IN_MONTHS | 60 |  |
| # 投资池每流入该金额的资金，我们在每个 tick 执行一次自主投资更新（最少 1 次） # 这是为了确保即使是非常庞大的投资池也能被妥善利用 # 请谨慎设置此值，设置得过低可能严重影响性能 |  |  |
| AUTONOMOUS_INVESTMENT_UPDATE_COUNT_DIVISOR | 500000 |  |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PROFIT_PRIVATIZE_SELF_OWNED_BUILDING_MULT | 0.75 | # 将私有化自有建筑等级的总得分乘以该系数 |
| AUTONOMOUS_INVESTMENT_NUM_FAILED_INVESTMENTS_FOR_REFRESH_BASE | 150 | # 如果一个国家的投资池连续该 tick 数未能执行，我们会强制刷新所有自主投资优先级，以确保投资池不会永久卡死 |
| AUTONOMOUS_INVESTMENT_NUM_FAILED_INVESTMENTS_FOR_REFRESH_DYNAMIC | 50 | # 在上述数值上额外加入该范围内的随机量，以分散刷新的时机 |
| AUTONOMOUS_INVESTMENT_NUM_FAILED_INVESTMENTS_FOR_REFRESH_PLAYER | 20 | # 对玩家控制的国家，用该值取代上面的 defines |
| # 自主投资的 AI 权重会根据投资池中有多少资金来自某种所有制类型的建筑来调整建筑的权重 # 例如，如果投资池收入中有很大比例来自庄园宅邸，那么庄园宅邸对其具有高投资权重的建筑群组会被调高权重 # 这里我们对这一效果的上下限进行钳制，即权重允许达到的最低/最高值 |  |  |
| AUTONOMOUS_INVESTMENT_MIN_PROPORTIONAL_INVESTMENT_WEIGHT | 0.25 |  |
| AUTONOMOUS_INVESTMENT_MAX_PROPORTIONAL_INVESTMENT_WEIGHT | 1.0 |  |
| # 在为新投资评估所有权建筑时，始终认为其至少贡献了该比例的投资池 # 这是为了确保金融中心能够出现在缺乏它们的国家，等等 |  |  |
| AUTONOMOUS_INVESTMENT_MIN_OWNERSHIP_BUILDING_INVESTMENT_SHARE | 0.25 |  |
| AUTONOMOUS_INVESTMENT_PREVIOUS_INVESTMENT_LOG_SIZE | 20 | # 一个国家的投资日志中同时保留的以往投资的最大数量 |
| AUTONOMOUS_INVESTMENT_PREVIOUS_INVESTMENT_DURATION_DAYS | 365 | # 一条以往投资从日志中移除前的天数 |
| BUILDING_PRIVATIZATION_CHANCE | 50.0 | # AI 在评估现有建筑时，选择进行私有化而非新建建筑等级的概率 |
| # 投资 AI 的所有权建筑选址权重与乘数 |  |  |
| OWNER_BUILDING_LOCATION_BASE_SCORE | 1 | # 选择某州作为所有权建筑选址的基础得分 |
| OWNER_BUILDING_LOCATION_POPULATION_SCORE | 1 | # 每有 10000 人口，选择该州作为所有权建筑选址的得分增加此值 |
| OWNER_BUILDING_LOCATION_GDP_SCORE | 1 | # 每有 INVESTMENT_LOCATION_GDP_DIVISOR 的年度州 GDP，选择该州作为所有权建筑选址的得分增加此值 |
| OWNER_BUILDING_LOCATION_GDP_DIVISOR | 100000 |  |
| OWNER_BUILDING_LOCATION_HAS_OWNER_BUILDING_MULT | 2.0 | # 对于已拥有所需所有权建筑类型的州，将其选址得分乘以此系数 |
| OWNER_BUILDING_LOCATION_CAPITAL_MULT | 2.0 | # 对于我们的首都，将其选址得分乘以此系数 |
| OWNER_BUILDING_LOCATION_SAME_STATE_MULT | 4.0 | # 对于我们正在进行建筑建造/私有化的同一州，将其选址得分乘以此系数 |
| OWNER_BUILDING_LOCATION_NOT_HOMELANDS_MULT | 0.5 | # 若该州并非该国主流文化的本土，则将所有者建筑选址评分乘以此值 |
| OWNER_BUILDING_LOCATION_LOWER_GDP_MULT | 0.25 | # 对于 GDP 低于我们正在建造/私有化的州的任何州，将所有者建筑选址评分乘以此值 |
| OWNER_BUILDING_LOCATION_NO_AVAILABLE_WORKFORCE_MULT | 0.1 | # 若该州缺乏劳动力，则将所有者建筑选址评分乘以此值 |
| OWNER_BUILDING_LOCATION_NO_AVAILABLE_INFRASTRUCTURE_MULT | 0.1 | # 若该州缺乏基础设施，则将所有者建筑选址评分乘以此值 |
| OWNER_BUILDING_LOCATION_UNINCORPORATED_MULT | 0.01 | # 若该州未被整合，则将所有者建筑选址评分乘以此值 |
| OWNER_COMPANY_EXPANSION_CHANCE_MULTIPLIER | 0.5 | # 公司被选为属于其相关建筑类型的新投资所有者的基础概率，按公司投资池占历史公司投资量的比例进行缩放 |
| OWNER_COMPANY_PRIVATIZATION_CHANCE_MULTIPLIER | 0.75 | # 用于私有化以替代 OWNER_COMPANY_EXPANSION_CHANCE，采用相同的缩放方式 |
| OWNER_COMPANY_OWN_STATE_MULT | 100.0 | # 若建筑正在其总部所在州建造/投资，则将该公司（与其他公司相比）被选为建筑所有者的概率乘以此值 |
| # 以下数据用于计算 AI 在制定/废除法律时赋予的权重 |  |  |
| CHANGE_LAW_RANDOM_FACTOR | 1.0 | # 此值越高，AI 的法律制定就越随机 |
| CHANGE_LAW_PRO_IG_IDEOLOGIES_FACTOR | 100 | # 制定法律时，我们认可的每个利益集团意识形态匹配项的权重 |
| CHANGE_LAW_ANTI_IG_IDEOLOGIES_FACTOR | -25 | # 制定法律时，我们不认可的每个利益集团意识形态匹配项的权重 |
| CHANGE_LAW_POLITICAL_MOVEMENT_FACTOR | 1000 | # 针对每个会提高该法律通过概率的政治运动，按（支持度 * 激进度）进行缩放 |
| CHANGE_LAW_POTENTIAL_CIVIL_WAR_THRESHOLD | 0.70 | # 若旨在维持现状的政治运动达到至少此激进度，AI 会将其视为潜在内战诱因 |
| CHANGE_LAW_POTENTIAL_CIVIL_WAR_ENACT_CHANCE | 100 | # AI 继续推行可能引发内战的法律变更的基础概率——最终概率需从此值中减去革命规避度（1 = 1%） |
| CHANGE_LAW_POTENTIAL_CIVIL_WAR_MEMORY_DURATION | 24 | # AI 因内战风险而决定不制定某项法律后，应记住并坚持该决定的月数 |
| CHANGE_LAW_CIVIL_WAR_BOLDNESS_RANGE | 100 | # AI 对某项特定法律的胆量（革命规避度必须超过该分数才能取消制定）设定在 0 到此值的随机范围内 |
| CHANGE_LAW_CIVIL_WAR_BOLDNESS_TIMED_WEIGHT_DURATION | 24 | # 当 AI 随机设定其对某项特定法律的胆量时，该限时权重持续的月数 |
| CHANGE_LAW_CIVIL_WAR_AVERSION_MOVEMENT_SUPPORT_FACTOR | 0.005 | # AI 为避免内战而停止制定法律的概率乘以（1 + 最高革命性运动的支持度 * 此值） |
| CHANGE_LAW_CIVIL_WAR_AVERSION_SUBJECT_MULTIPLIER | 5 | # 对附属国而言，AI 为避免内战而停止制定法律的概率乘以此值 |
| CHANGE_LAW_CIVIL_WAR_AVERSION_LAW_DIRECTION_FLEXIBILITY | 2 | # 革命规避度乘以此值后，加到 AI 为避免革命而愿意容忍的最大进步/倒退幅度上 |
| DID_NOT_NEGOTIATE_WITH_IG_COOLDOWN_MONTHS | 24 | # 若 AI 决定不就某项法律制定与利益集团谈判，则记住该决定的月数 |
| # 以下数据用于计算 AI 在选择生产方式时赋予的权重 |  |  |
| PRODUCTION_METHOD_BASE_VALUE | 1000 |  |
| PRODUCTION_METHOD_PROFIT_FACTOR | 1 | # 每磅生产商品将产生的利润 |
| PRODUCTION_METHOD_DEFICIT_FACTOR | 1.5 | # 每磅生产商品将产生的亏损（乘以负值） |
| PRODUCTION_METHOD_PRODUCED_VALUE_FACTOR | 0.25 | # 每磅以基础价值计的生产商品 |
| PRODUCTION_METHOD_EMPLOYMENT_CHANGE_FACTOR | 2.0 | # 生产方式的总得分将乘以或除以 1 + ( 该值 * 变更所增加或节省的劳动力比例 ) |
| PRODUCTION_METHOD_REDUCE_OUTPUT_PENALTY_FACTOR | 10 | # 若正在减少建筑的产出惩罚，则方法得分乘以该值 |
| PRODUCTION_METHOD_INCREASE_OUTPUT_PENALTY_FACTOR | 0.01 | # 若正在增加建筑的产出惩罚，则方法得分乘以该值 |
| PRODUCTION_METHOD_FAVORED_GOODS_FACTOR | 0.25 | # 每单位 AI 偏好的生产商品的基础成本 * 数量（针对非军用商品） |
| NATIONALIZATION_DESIRE_NATIONALIZE_THRESHOLD | 1.0 | # 当国有化意愿（在 ai 策略与建筑类型中设定）达到或超过该值时，AI 将希望将生产建筑国有化 |
| NATIONALIZATION_DESIRE_PRIVATIZE_THRESHOLD | 0.0 | # 当国有化意愿（在 ai 策略与建筑类型中设定）达到或低于该值时，AI 将希望将生产建筑私有化 |
| # 国有化后若国内的激进派达到该百分比，AI 将避免进一步国有化 # 当该州为近期解放/征服所得时忽略此项 |  |  |
| NATIONALIZATION_RADICALS_THRESHOLD_TO_AVOID_NATIONALIZATION | 0.3 |  |
| NATIONALIZATION_RADICALS_THRESHOLD_TO_ALWAYS_COMPENSATE | 0.1 | # 国有化后若国内的激进派达到该百分比，AI 将始终使用有偿国有化 |
| # 当州拥有 recently_liberated_state/recently_conquered_state 修正时，增加国有化意愿 # 仅适用于外国所有的建筑，且不用于私有化考量 |  |  |
| NATIONALIZATION_DESIRE_FROM_RECENTLY_LIBERATED | 2.0 |  |
| NATIONALIZATION_DESIRE_FROM_RECENTLY_CONQUERED | 1.0 |  |
| NATIONALIZATION_GOLD_RESERVES_THRESHOLD | 0.5 | # 若使用补偿方式进行国有化，AI 将希望在国有化后至少保留该比例的黄金储备（以百分比计） |
| NATIONALIZATION_MAX_LEVELS_PER_UPDATE | 5 | # AI 在单次更新中对每种建筑进行国有化的最大建筑等级数 |
| PRODUCTION_METHOD_FAVORED_MILITARY_GOODS_FACTOR | 0.5 | # 每单位 AI 偏好的生产商品的基础成本 * 数量（针对军用商品） |
| PRODUCTION_METHOD_DISFAVORED_GOODS_FACTOR | -0.25 | # 每单位 AI 不偏好的生产商品的基础成本 * 数量 |
| PRODUCTION_METHOD_UNDESIRABLE_GOODS_PRICE_THRESHOLD | 1.5 | # 若使用“最高产能”逻辑的生产方式所使用的商品价格高于 ( 基础价格 * 该值 )，则降低其得分 |
| PRODUCTION_METHOD_UNDESIRABLE_GOODS_PRICE_FACTOR_TRADEABLE | -0.05 | # 每单位价格高于不合意价格阈值的商品的基础成本 * 数量（当该商品可从世界市场进口时） |
| PRODUCTION_METHOD_UNDESIRABLE_GOODS_PRICE_FACTOR_UNTRADEABLE | -0.25 | # 每单位价格高于不合意价格阈值的商品的基础成本 * 数量（当该商品无法从世界市场进口时） |
| PRODUCTION_METHOD_STICKINESS_UPGRADE | 0.95 | # 当非当前方式的总基础价值产出更高时，其得分乘以该值 |
| PRODUCTION_METHOD_STICKINESS_DOWNGRADE | 0.75 | # 当非当前方式的总基础价值产出更低（或相等）时，其得分乘以该值 |
| PRODUCTION_METHOD_CHANCE_TO_CHANGE | 0.1 | # AI 在评估生产方式时考虑更换生产方式的概率 |
| PRODUCTION_METHOD_LOW_POP_THRESHOLD | 50000 | # 如果一个州的人口少于此值，则对低人口生产方式使用下方的评分系数 |
| PRODUCTION_METHOD_LOW_POP_FACTOR | 100000 | # 如果一个州的人口少于 PRODUCTION_METHOD_LOW_POP_THRESHOLD，则为低人口生产方式加上此分数 |
| # 以下数据用于计算 AI 的求和意愿 |  |  |
| AI_PEACE_AGREEMENT_BASE_VALUE | -10 |  |
| AI_PEACE_AGREEMENT_WHITE_PEACE_BASE | 10 | # 如果双方均未被强制执行任何战争目标 |
| AI_PEACE_AGREEMENT_WHITE_PEACE_WAR_DURATION | 2 | # 战争每持续一个月，白和平的接受度增加此值 |
| AI_PEACE_AGREEMENT_WAR_SUPPORT_FACTOR | -1 |  |
| AI_PEACE_AGREEMENT_UNACCEPTABLE_WARGOAL_VALUE | -1000 | # 如果我方被强制执行一个不可接受的战争目标（如“裁减军备”），此固定战争目标数值将被加入和平接受度 |
| AI_PEACE_AGREEMENT_WARGOAL_VALUE_BASE | 10 | # AI 对每个战争目标的估值（基础值） |
| AI_PEACE_AGREEMENT_WARGOAL_VALUE_MIN | -1000 | # 战争目标数值不能低于此值 |
| AI_PEACE_AGREEMENT_WARGOAL_VALUE_MAX | 1000 | # 战争目标数值不能高于此值 |
| AI_PEACE_AGREEMENT_WARGOAL_VALUE_SCALED | 0.5 | # AI 对每个战争目标的估值（按机动点数消耗缩放） |
| AI_PEACE_AGREEMENT_ALLY_WARGOAL_MULT | 1 | # 我方盟友每主张一个战争目标，应用战争目标数值 × 此值 |
| AI_PEACE_AGREEMENT_SELF_WARGOAL_MULT | 3 | # 我方每有一个正在被主张的战争目标，应用战争目标数值 × 此值 |
| AI_PEACE_AGREEMENT_ENEMY_WARGOAL_SELF_MULT | -8 | # 敌方每对我方主张一个战争目标，应用战争目标数值 × 此值 |
| AI_PEACE_AGREEMENT_ENEMY_WARGOAL_ALLY_MULT | -1 | # 每有一个针对我方盟友主张的战争目标，应用战争目标数值 × 此值 |
| AI_PEACE_AGREEMENT_NON_CONTESTED_ENEMY_WARGOAL_MULT | 5 | # 敌方持有但未受争夺的战争目标数值乘以此值 |
| AI_PEACE_AGREEMENT_ACHIEVABLE_ALLY_WARGOAL | -1.5 | # 我方每持有一个未被主张、且目标会比持有者先耗尽战争支持的战争目标（乘以己方/盟友战争目标数值） |
| AI_PEACE_AGREEMENT_ACHIEVABLE_ENEMY_WARGOAL | -0.9 | # 敌方每持有一个（无论是否被主张）目标会比持有者先耗尽战争支持的战争目标（乘以己方/盟友的敌方战争目标数值） |
| AI_PEACE_AGREEMENT_WAR_SUPPORT_TO_HOLD_ON_TO_ACHIEVABLE_WARGOALS | 0 | # 战争支持度低于此值时，AI 在和谈中会更愿意把可实现的战争目标让给敌方 |
| AI_PEACE_AGREEMENT_PEACE_DESIRE_FACTOR | 1.0 | # 求和意愿加入和平协议接受度评分时乘以此值 |
| AI_CAPITULATE_COMPLETELY_DEFEATED | 1000 | # 如果整个盟方阵营被 100% 占领 |
| AI_CAPITULATE_BASE_VALUE | -25 |  |
| AI_CAPITULATE_WAR_LEADER_FACTOR | -25 | # 如果是战争领袖 |
| AI_CAPITULATE_WAR_SUPPORT_FACTOR | -1 |  |
| AI_CAPITULATE_SELF_WARGOAL_FACTOR | -5 | # 我方在战争中每持有一个战争目标 |
| AI_CAPITULATE_ENEMY_WARGOAL_FACTOR | -20 | # 战争中每有一个针对我方的战争目标 |
| AI_CAPITULATE_PEACE_DESIRE_FACTOR | 0.5 | # 求和意愿加入投降评分时乘以此值 |
| AI_MONTHS_OF_REDUCED_PEACE_DESIRE | 10 | # 在此月数之前，降低 AI 的求和意愿 |
| AI_PEACE_DESIRE_FROM_SHORT_WAR | -10 | # 在上述月数内减去此数值的求和意愿（乘以 AI_MONTHS_OF_REDUCED_PEACE_DESIRE - 战争持续月数） |
| AI_PEACE_DESIRE_FROM_TURMOIL | 25 | # 激进派达到 100% 时增加此数值的求和意愿 |
| AI_PEACE_DESIRE_FROM_DEVASTATION | 50 | # 荒废度达到 100% 时增加此数值的求和意愿 |
| AI_PEACE_DESIRE_FROM_LOYALISTS | -25 | # 忠诚派达到 100% 时减去此数值的求和意愿 |
| AI_PEACE_DESIRE_FROM_DEBT_LEVEL | 200 | # 在 100% 债务水平时增加此数值的和平意愿 |
| AI_PEACE_DESIRE_FROM_BANKRUPTCY | 200 | # 破产时增加此数值的和平意愿 |
| AI_PEACE_DESIRE_FROM_GOLD_RESERVES | -25 | # 在 100% 黄金储备时减少此数值的和平意愿 |
| AI_PEACE_DESIRE_FROM_FORCE_BALANCE | 50 | # 根据双方的 DIPLO_PLAY_FORCE_BALANCE_SCALE，最多增加或减少此数值的战争支持度 |
| AI_PEACE_DESIRE_FACTOR_FROM_ANNEXATION | 0.5 | # 如果达成和平将导致该国被吞并，则所有正的和平意愿因子将乘以此数值 |
| # AI 国家专属目标数据 |  |  |
| SECRET_GOAL_STICKINESS | 2.0 | # 此数值越高，AI 在重新计算时改变已确立的秘密目标的概率越低 |
| ATTITUDE_STRONG_GOAL_SCORE_THRESHOLD | 100 |  |
| ATTITUDE_WEAK_GOAL_SCORE_THRESHOLD | 50 |  |
| GOAL_THREAT_INFAMOUS_FACTOR | 25 |  |
| GOAL_THREAT_NOTORIOUS_FACTOR | 50 |  |
| GOAL_THREAT_PARIAH_FACTOR | 1000 |  |
| GOAL_THREAT_NEIGHBOR_FACTOR | 25 |  |
| GOAL_THREAT_SP_MAX_MULT | 2 |  |
| GOAL_THREAT_CUSTOMS_UNION_MULT | 0.5 | # 如果处于关税同盟中，邻国威胁分数减少此数值 |
| GOAL_ANTAGONIZE_POOR_RELATIONS_FACTOR | 25 |  |
| GOAL_ANTAGONIZE_COLD_RELATIONS_FACTOR | 50 |  |
| GOAL_ANTAGONIZE_HOSTILE_RELATIONS_FACTOR | 100 |  |
| GOAL_ANTAGONIZE_LIBERTY_DESIRE_FACTOR | 1 | # 附属国对其宗主国的分数乘以其独立倾向 |
| GOAL_ANTAGONIZE_CONQUER_SCORE_MULT | 1.0 | # 乘以我们想从对方夺取的州的总分 |
| GOAL_ANTAGONIZE_CONQUER_SCORE_MAX | 200 | # 我们想夺取的领土总分不能超过此数值 |
| GOAL_ANTAGONIZE_TREATY_PORT_SCORE_MULT | 0.5 | # 乘以我们想从对方夺取的条约港的总分 |
| GOAL_ANTAGONIZE_TREATY_PORT_SCORE_MAX | 100 | # 我们想夺取的条约港总分不能超过此数值 |
| GOAL_ANTAGONIZE_DOMINATE_SCORE_MULT | 1.0 | # 乘以我们想强加给对方的使对方成为附属国的战争目标总分 |
| GOAL_ANTAGONIZE_DOMINATE_SCORE_MAX | 200 |  |
| GOAL_ANTAGONIZE_RIVAL_FACTOR | 100 |  |
| GOAL_ANTAGONIZE_WAR_FACTOR | 1000 |  |
| GOAL_ANTAGONIZE_NATURAL_ENEMY_FACTOR | 75 |  |
| GOAL_BEFRIEND_CORDIAL_RELATIONS_FACTOR | 25 |  |
| GOAL_BEFRIEND_AMICABLE_RELATIONS_FACTOR | 50 |  |
| GOAL_BEFRIEND_FRIENDLY_RELATIONS_FACTOR | 100 |  |
| GOAL_BEFRIEND_PROTECTOR_THRESHOLD | 15 |  |
| GOAL_BEFRIEND_PROTECTOR_FACTOR | 1.0 |  |
| GOAL_BEFRIEND_PROTECTOR_RIVAL_MULT | 2.0 | # 如果对方能够保护我们免受对手威胁，分数乘以此数值 |
| GOAL_BEFRIEND_PROTECTOR_MAX_FACTOR | 100 |  |
| GOAL_BEFRIEND_PROTECTOR_SP_MAX_MULT | 2 |  |
| GOAL_BEFRIEND_SUBJECT_FACTOR | 25 |  |
| GOAL_BEFRIEND_ALLIANCE_FACTOR | 50 |  |
| GOAL_BEFRIEND_NATURAL_ALLY_FACTOR | 75 |  |
| GOAL_BEFRIEND_RECONCILE_FACTOR | 500 |  |
| GOAL_BEFRIEND_WAR_ALLY_FACTOR | 1000 |  |
| GOAL_BEFRIEND_WANTS_TO_PROTECT_FACTOR | 100 |  |
| FRIENDLY_AI_JOIN_DIPLO_PLAY_FACTOR | 100 |  |
| VIOLATE_SOVEREIGNTY_ACTION_NAME | "violate_sovereignty" |  |
| VIOLATE_SOVEREIGNTY_MIN_RELATIVE_STRENGTH | 2.0 | # 我们的 SP 必须达到对方陆军的此倍数才会想要侵犯其主权 |
| VIOLATE_SOVEREIGNTY_RANDOM_FACTOR | 2.0 | # 此数值越高，AI 在选择侵犯谁的主权时就越是随机 |
| VIOLATE_SOVEREIGNTY_MIN_THEATER_IMPORTANCE | 150 | # 一个战区的战争价值必须至少达到此数值，AI 才会考虑为了进入该战区而侵犯主权 |
| VIOLATE_SOVEREIGNTY_COOLDOWN_DAYS | 100 |  |
| EXPEL_DIPLOMATS_ACTION_NAME | "expel_diplomats" |  |
| AUTONOMOUS_TRADE_RANDOM_FACTOR | 0.5 | # 此数值越高，自主贸易在商品选择上的随机性就越强 |
| AUTONOMOUS_TRADE_STICKYNESS | 2.0 | # 当贸易容量被完全用尽时，新贸易路线必须产生至少这么多倍的收入才能取代旧贸易路线 |
| AUTONOMOUS_TRADE_WEEKS_BEFORE_TRADE_REDUCTION | 8 | # 在增加某商品的贸易之后的这么多周内，州不会减少该商品的贸易量，以便让商品替代等效果有时间发挥作用 |
| AUTONOMOUS_TRADE_MIN_DESIRABILITY_PER_QUANTITY_TO_MAINTAIN_TRADE | 25 | # 如果当前贸易路线的每基准贸易量期望值低于此值，则减少贸易量 |
| AUTONOMOUS_TRADE_MIN_DESIRABILITY_PER_QUANTITY_TO_INCREASE_TRADE | 50 | # 如果新贸易路线的每基准贸易量期望值低于此值，则不增加贸易量 |
| AUTONOMOUS_TRADE_MIN_DESIRABILITY_INITIALIZATION_MULTIPLIER | 0.75 | # 在存档书签初始化期间，贸易的期望值需求会乘以此系数 |
| AUTONOMOUS_TRADE_POTENTIAL_REVENUE_BASE_COST_FACTOR | 0.25 | # 在确定某州中某商品的贸易潜力时，每单位收入会以商品基准成本 * 此系数进行归一化，以反映收入会随贸易增加而下降这一事实 |
| # 影响贸易期望值的因素 # 贸易路线的基础期望值等于扣除关税和补贴后的每贸易量收入 |  |  |
| AUTONOMOUS_TRADE_DESIRE_SUBVENTIONS_FACTOR | 100 | # 贸易路线的期望值会增加（补贴百分比 * 此系数），这是在收入影响之外的额外因素。对于相反方向的补贴（即出口补贴降低进口期望值），该系数同样反向适用 |
| AUTONOMOUS_TRADE_DESIRE_SUBVENTIONS_FACTOR_NEW_GOODS_MULT | 20.0 | # 对于进口市场中尚不存在的商品，补贴对贸易期望值的影响会乘以此系数 |
| AUTONOMOUS_TRADE_DESIRE_TARIFFS_FACTOR | 25 | # 贸易路线的期望值会减少（关税百分比 * 此系数），这是在收入影响之外的额外因素 |
| AUTONOMOUS_TRADE_DESIRE_OPPOSITE_MARKET_SHARE_FACTOR | -1000 | # 贸易路线的期望值变化为此系数 * 该国在世界市场中反方向贸易所占的份额 |
| AUTONOMOUS_TRADE_DESIRE_SHORTAGE_FACTOR | 300 | # 进口短缺商品的期望值会增加此数值，并按短缺惩罚的严重程度进行缩放 |
| # 每当贸易中心成功执行一笔贸易时，会消耗其每周贸易次数中的一次 # 每当其*未能*执行一笔贸易时，会消耗其每周贸易总次数的这一比例 # 这是为了防止拥有数百次每周贸易次数的贸易中心反复尝试交易，白白消耗大量性能却毫无收益 |  |  |
| AUTONOMOUS_TRADE_WEEKLY_TRADES_FRACTION_USED_FOR_FAILED_TRADE = 0.2 |  |  |
| TRADE_VALUE_DELTA_FACTOR | 3.0 | # 在计算条约贸易价值时，生产/消费之间的差值权重是基础生产/消费值的这么多倍 |
| TRADE_VALUE_BASE_MULTIPLIER | 0.001 | # 仅基于生产和消费的条约贸易价值所应用的基础乘数 |
| TRADE_VALUE_RELATIVE_MULTIPLIER | 100 | # 应用于条约贸易价值的相对乘数，并除以市场中的总价值 |
| TRADE_VALUE_FAVORED_GOODS_DIRECTION_MULT | 1.25 | # 在确定 AI 贸易价值时，如果贸易方向与 AI 的商品立场一致，该商品的贸易潜力会乘以此系数 |
| TRADE_VALUE_DISFAVORED_GOODS_DIRECTION_MULT | 0.25 | # 在确定 AI 贸易价值时，如果贸易方向与 AI 的商品立场相反，该商品的贸易潜力会乘以此系数 |
| UNUSED_CAPPED_RESOURCE_RATIO_TO_START_DISCOURAGING_EXPORT | 0.5 | # 如果某国受资源上限限制的商品的未开发潜在产量未达到市场购买订单数 * 此系数，则切换为惩罚性出口关税 |
| UNUSED_CAPPED_RESOURCE_RATIO_TO_STOP_DISCOURAGING_EXPORT | 1.0 | # 若国内受资源上限限制的商品的未开发潜在产量至少达到市场购买订单数 * 该值，则停止施加惩罚性出口关税 |
| COMPANY_TYPE_DEFAULT_BASE_WEIGHT | 1 | # 公司的基础权重，可被数据库中的 ai_weight 覆盖 |
| COMPANY_TYPE_RANDOM_FACTOR | 1 | # 该值越高，AI 选择公司时的随机性越强 |
| COMPANY_TYPE_STICKYNESS | 3 | # AI 已计划创建的公司，其权重会乘以该值 |
| COMPANY_TYPE_STICKYNESS_DURATION_MONTHS | 60 | # 经过这么多个月后，AI 计划组建的公司的粘性将被移除 |
| COMPANY_TYPE_FORMABLE_FACTOR | 1.25 | # 若某公司可立即组建，其权重增加该值 |
| COMPANY_TYPE_FORMABLE_MULTIPLE_FREE_SLOTS_FACTOR | 5.0 | # 若国家拥有多于一个空闲公司席位，则用该值替代 COMPANY_TYPE_FORMABLE_FACTOR |
| COMPANY_TYPE_PRODUCTIVITY_FACTOR | 0.25 | # 公司的 AI 权重乘数增加 ( 该值 * 预测建筑生产力 ) |
| COMPANY_TYPE_PRODUCTIVITY_MAX | 4.0 | # COMPANY_TYPE_PRODUCTIVITY_FACTOR 的效果不会高于该值 |
| COMPANY_TYPE_BUILDING_LEVELS_FACTOR | 0.1 | # 公司的 AI 权重乘数增加 ( 该值 * 建筑等级数量 ) |
| COMPANY_TYPE_BUILDING_LEVELS_MAX | 2.0 | # COMPANY_TYPE_NUM_BUILDING_LEVELS_FACTOR 的效果不会高于该值 |
| COMPANY_TYPE_COMPETITION_FACTOR | 2 | # 公司的 AI 权重除数增加 1 + ( 现有公司中相互竞争的建筑类型数量 * 该值 ) |
| COMPANY_TYPE_BUILDING_GROUP_WEIGHT_IMPACT | 1.5 | # AI 对与该公司关联的建筑组的平均策略权重乘数会以该值向 1 调整，并应用于 AI 对该公司的偏好（例如：若该值为 0.5，则平均 AI 偏好与 1 之间的差值减半——1.5 变为 1.25，0.5 变为 0.75 等） |
| MILITARY_UNITS_PER_FORMATION_ARMY | 50 | # AI 旨在让陆军保持大致该规模，并据此在陆地总部创建新的编队 |
| MILITARY_UNITS_PER_FORMATION_FLEET | 100 | # AI 旨在让舰队保持大致该规模，并据此在海军总部创建新的编队 |
| MILITARY_UNITS_MIN_FOR_GARRISON_FORMATION | 15 | # 若某陆地总部拥有至少该数量的单位，我们会将编队最小数量设为 2，以确保存在一个驻防编队 |
| MILITARY_UNITS_MIN_FOR_GARRISON_FORMATION_IN_CAPITAL_HQ | 5 | # 针对首都陆地总部覆盖 MILITARY_UNITS_MIN_FOR_GARRISON_FORMATION，因为不使首都处于无防备状态至关重要 |
| MILITARY_UNITS_GARRISON_BATTALION_MULT | 0.33 | # 每个总部的驻防编队应获得其总营数的该比例 |
| MILITARY_UNITS_MIN_DELTA_TO_TRANSFER_UNITS | 0.05 | # 某编队想要的总部队占比与其现有占比之间必须至少存在该差值，AI 才会费心向其调入或调出单位 |
| MIN_RANK_TO_FORM_POWER_BLOC | 6 | # 等级值低于该值的 AI 永远不会尝试组建强权集团 |
| POWER_BLOC_IDENTITY_RANDOM_FACTOR | 1 | # 该值越高，AI 选择强权集团身份时的随机性越强 |
| POWER_BLOC_PRINCIPLE_RANDOM_FACTOR | 1 | # 该值越高，AI 选择强权集团原则时的随机性越强 |
| POWER_BLOC_STATUE_RANDOM_FACTOR | 1 | # 该值越高，AI 选择强权集团塑像时的随机性越强 |
| LEAVE_POWER_BLOC_SCORE_THRESHOLD | -100 | # 若评分低于该值则离开强权集团。评分是“invite_to_power_bloc”外交行动的接受度值 |
| POWER_BLOC_KICK_MEMBER_LOW_COHESION_THRESHOLD | 40 | # 若当前凝聚力低于此值，则视为低凝聚力并加上相应分数 |
| POWER_BLOC_KICK_MEMBER_LOW_COHESION_SCORE | 5 | # 当前凝聚力较低时开除成员（任何成员）的分数（乘以凝聚力与阈值的差值） |
| POWER_BLOC_KICK_MEMBER_COHESION_CHANGE_SCORE | 2 | # 凝聚力变化足够大时开除该成员的分数（乘以凝聚力变化） |
| POWER_BLOC_KICK_MEMBER_LEVERAGE_ADVANTAGE_SCORE | -0.1 | # 对其持有的主动杠杆足够高时开除该成员的分数（乘以主动杠杆） |
| POWER_BLOC_KICK_MEMBER_POOR_RELATIONS_SCORE | 25 | # 与该成员的关系为“恶劣”时开除该成员的分数，若为“冷淡”则乘以 2，若为“敌对”则乘以 3 |
| POWER_BLOC_KICK_MEMBER_HOSTILE_ATTITUDE_SCORE | 25 | # 对该成员的态度为“敌对”时开除该成员的分数，若为“极度敌对”则乘以 2 |
| POWER_BLOC_KICK_MEMBER_MARKET_SHARE_SCORE | -50 | # 根据该成员在集团中的市场份额开除该成员的分数（若强权集团拥有统一市场） |
| POWER_BLOC_KICK_MEMBER_HIGH_ARMY_MILITARY_STRENGTH_SCORE | -25 | # 该成员的陆军实力高于平均水平时开除该成员的分数（若强权集团为军事同盟） |
| POWER_BLOC_KICK_MEMBER_HIGH_NAVY_MILITARY_STRENGTH_SCORE | -15 | # 该成员的海军实力高于平均水平时开除该成员的分数（若强权集团为军事同盟） |
| POWER_BLOC_KICK_MEMBER_SCORE_THRESHOLD | 100 | # 总分低于此值时开除该成员 |
| POWER_BLOC_KICK_MEMBER_RANDOM_FACTOR | 0.5 | # 此值越高，AI 在选择将哪个成员开除出强权集团时越随机 |
| IMPOSE_LAW_NO_POTENTIAL_LAW_COOLDOWN_MONTHS | 24 | # 若 AI 找不到任何至少有机会强加于目标的法律，则在接下来的这么多月内不再检查该目标 |
| IMPOSE_LAW_RANDOM_FACTOR | 1 | # 此值越高，AI 在选择对哪个国家强加法律时越随机 |
| IMPOSE_LAW_MAX_IDEOLOGICAL_OPINION | 25 | # AI 对一个国家的意识形态评价必须不高于此值，才会考虑对其强加法律 |
| IMPOSE_LAW_MAX_LIBERTY_DESIRE | 50 | # AI 不会对独立倾向高于此值的附属国强加法律 |
| IMPOSE_LAW_MIN_ENACTMENT_CHANCE | 0.2 | # 若颁布机会低于此值，AI 不会对附属国强加法律 |
| EXILE_INTERACTION_FAILED_COOLDOWN_MONTHS | 24 | # 若某项人物互动对流亡人物无效，则在接下来的这么多月内不再检查该人物 |
| AI_INTERACTION_PROMINENCE_CHANCE_FACTOR | 1.0 | # 每一点声望提供此百分比的几率被纳入人物互动的考虑范围 |
| AI_INTERACTION_MIN_PROMINENCE_CHANCE | 10 | # 无论声望如何，被纳入考虑的最低百分比几率 |
| TREATY_FAIRNESS_BASE_SCORE | 10 | # 在考虑各国接受度之前条约公平性的基础分数，接受度差值小于此值的条约会被视为对双方公平 |
| REJECTED_TREATY_MEMORY_DURATION_DAYS | 365 | # AI 会记住被拒绝的条约多少天，并在此期间拒绝任何没有足够显著改善的条约 |
| REJECTED_TREATY_MIN_ACCEPTANCE_IMPROVEMENT_FOR_NEW_PROPOSAL | 10 | # 若 AI 最近刚拒绝过一项条约，新的提案必须比旧提案好这么多，AI 才有机会接受 |
| REJECTED_TREATY_UNDER_MIN_ACCEPTANCE_IMPROVEMENT_PENALTY | -1000 | # 在被拒条约记忆持续时间内，若条约提案的改善程度不足，则将此值加到接受度上 |
| # 条约 |  |  |
| TREATIES_RANDOM_FACTOR | 1.0 | # AI 在起草条约时选择条款的随机程度 |
| TREATIES_CHECK_CATEGORIES_WHEN_COMPOSING_TREATY | no | # AI 在收集初始条款后起草条约时是否关注条款类别 |
| TREATIES_NUMBER_CHECKED_CATEGORIES_TREATY_COMPOSER | 3 | # AI 在拟定条约时会尝试收集多少个类别来进行核对 |
| TREATIES_MINIMUM_ACCEPTANCE_TO_PROPOSE | 15 | # AI 要求对方达到多少接受度才会尝试发出提案？0 = 永不接受，30 = 总是接受，之间 = 随机概率 |
| TREATIES_MINIMUM_OWN_ACCEPTANCE_TO_PROPOSE | 10 | # AI 要求自身达到多少接受度才会发出提案？ |
| TREATIES_MAX_NUMBER_ARTICLES | 6 | # AI 在一条条约中最多会考虑多少项条款 |
| TREATIES_ACCEPTANCE_BASE | 0 | # 条约的基础接受度 |
| TREATIES_ACCEPTANCE_WITHDRAW_THRESHOLD | -50 | # 低于或等于该阈值时，AI 会在约束期之外退出条约 |
| TREATIES_ACCEPTANCE_WITHDRAW_BINDING_PERIOD_THRESHOLD | -10000 | # 低于或等于该阈值时，AI 会在条约仍具约束力时退出条约 |
| TREATIES_DEFAULT_LENGTH_YEARS | 5 | # AI 提议的条约时长 |
| COLONIZATION_VALUE_BASE | 25 | # AI 对其能够殖民的区域的基础估值 |
| COLONIZATION_VALUE_HAS_COLONY_MULTIPLIER | 2.0 | # 若 AI 在该区域已有一个正在扩张的殖民地，殖民估值乘以此系数 |
| COLONIZATION_VALUE_NO_PRESENCE_MULTIPLIER | 0.2 | # 若 AI 在该区域及其相邻区域均无存在，殖民估值乘以此系数 |
| TRANSIT_RIGHTS_BASE_DESIRE | 100 | # 对通行权（Transit Rights）的基础意愿，仅在其确实能帮助接收国连通某个市场区域时才生效 |
| TREATY_OBLIGATION_WE_OWE_THEM_ACCEPTANCE | -40 | # 若作为条约的一部分，国家 A 将欠国家 B 一项义务，A 对该条约的接受度如何变化。注意："WE"（我们）指的是进行评估的国家，而非玩家 |
| TREATY_OBLIGATION_THEY_OWE_US_ACCEPTANCE | 30 | # 若作为条约的一部分，国家 A 将获得国家 B 所欠的一项义务，A 对该条约的接受度如何变化。注意："US"（我们）指的是进行评估的国家，而非玩家 |
| TREATY_OBLIGATION_THEY_OWE_US_RECENTLY_REPUDIATED_ACCEPTANCE | 15 | # 同上，但若 B 近期曾拒绝履行义务则使用此值（因 B 的承诺价值下降，A 对其估值更低） |
| TREATY_OBLIGATION_THEY_CALL_US_IN_ACCEPTANCE | 30 | # 若 B 正在要求 A 履行其所欠的义务，A 对该条约的接受度如何变化。注意："US"（我们）指的是进行评估的国家，而非玩家 |
| TREATY_OBLIGATION_THEY_CALL_US_IN_RECENTLY_REPUDIATED_ACCEPTANCE | 15 | # 同上，但若 B 近期曾拒绝履行义务则使用此值（因 B 愿意无视协议，A 也更不倾向于遵守此类协议，估值更低） |
| PIRACY_HEAT_GAIN_PER_GOODS | 0.01 | # 与被海盗劫掠的商品贸易量相乘，以确定一条航线的“热度” |
| PIRACY_HEAT_DECAY | 0.01 | # 每次 AI 更新时海盗热度衰减的百分比 |
| RAID_HEAT_GAIN_PER_LOST_SUPPLY_SHIP | 0.01 | # 与一条补给路径上损失的补给船数量相乘 |
| RAID_HEAT_DECAY | 0.01 | # 每次 AI 更新时海盗热度衰减的百分比 |
| PROTECT_SUPPLY_OWN_PATH_SCORE_MULT | 2.0 | # 若补给路径属于自己，则补给路径得分乘以 1 + [Mult] |
| RAID_SUPPLY_SCORING_FLEET_AVG_SPEED_MULT | 0.05 | # 与舰队的平均速度相乘 |
| RAID_SUPPLY_SCORING_FLEET_DETECTION_VISIBILITY_RATIO_MULT | 1.5 # 与舰队的侦测与可见度之比相乘 |  |
| RAID_SUPPLY_SCORING_FLEET_SIZE_MULT | 2.0 | # 会计算此值 / 舰船数量并加到评分系数上，因此舰船越多评分越低 |
| RAID_SUPPLY_SCORING_FLEET_STRENGTH_RATIO_MULT | 3.0 | # 敌对/友好存在之间的实力之比要乘上多少 |
| PROTECT_SUPPLY_SCORING_FLEET_SCREENING_RATIO_MULT | 2.0 # 我们主要想使用护航比例高的舰队 |  |
| PROTECT_SUPPLY_SCORING_FLEET_SIZE_MULT | 0.005 | # 计算评分时对舰队规模的乘数 |
| PROTECT_SUPPLY_SCORING_FLEET_RAID_HEAT_MULT | 0.01 | # 计算评分时对该海域累积袭击热度的乘数 |
| PROTECT_SUPPLY_SCORING_FLEET_STRENGTH_RATIO_MULT | 3.0 | # 计算评分时对敌方/己方存在兵力强度比的乘数 |
| HUNT_PIRATES_SCORING_FLEET_PIRACY_HEAT_MULT | 0.01 | # 该海域累积海盗热度对缉私评分的加成 |
| HUNT_PIRATES_SCORING_FLEET_DETECTION_RATIO_MULT | 2.0 | # 缉私时偏好侦测能力高的舰队 |
| HUNT_PIRATES_SCORING_FLEET_SCREENING_RATIO_MULT | 1.0 | # 缉私巡逻时偏好护航比例高的舰队 |
| HUNT_PIRATES_MIN_HOSTILITY_MULT | 0.25 | # 交战期间缉私评分的最低乘数。防止 AI 在战争期间完全放弃缉私。 |
| HUNT_PIRATES_AT_WAR_MULT | 0.25 | # 处于战争状态时对缉私评分施加的额外乘数 |
| PIRACY_SCORING_FLEET_SPEED_VISIBILITY_RATIO_ADJUSTER | 1.0 | # 如果私掠评分似乎过高，调低此项 |
| PIRACY_SCORING_FLEET_SPEED_VISIBILITY_RATIO_MULT | 2.0 | # 私掠时偏好每单位能见度运载商品量高的舰队 |
| PIRACY_NO_HOSTILITIES_MULT | 1.0 | # 当前无交战时对航运线路评分的乘数 |
| PIRACY_HOSTILITIES_MULT | 0.5 | # 当前处于交战状态时对航运线路评分的乘数 |
| PRIVATEER_SCORING_FLEET_SPEED_VISIBILITY_RATIO_ADJUSTER | 1.0 | # 如果私掠舰评分似乎过高，调低此项 |
| PRIVATEER_SCORING_FLEET_SPEED_VISIBILITY_RATIO_MULT | 2.0 | # 私掠舰任务偏好每单位能见度运载商品量高的舰队 |
| PORT_BOMBARDMENT_NAVAL_HOSTILITIES_MULT | 2.0 | # 与海岸所有者处于海上交战状态时对海岸评分的乘数 |
| PORT_BOMBARDMENT_FULL_HOSTILITIES_MULT | 0.5 | # 与海岸所有者处于全面交战状态时对海岸评分的乘数 |
| BLOCKADE_WORLD_MARKET_HUB_MULT | 2.0 | # 对世界市场中心的海岸评分乘数 |
| BLOCKADE_NOT_WORLD_MARKET_HUB_MULT | 0.25 | # 对非世界市场中心的海岸评分乘数 |
| # AI 会计算一个“劣势比”来判断自己在海战中的处境有多糟。# 劣势比会与此值相乘并加到乘数上，用于评估选择哪种海军任务# 因此若此值为负，表示 AI 会回避这些任务；为正则优先选择这些任务。 |  |  |
| INTERCEPT_OUTCLASSED_MULT | -4.0 |  |
| POWER_PROJECTION_OUTCLASSED_MULT | -1.0 |  |
| POWER_PROJECTION_HOSTILE_NAVAL_RATIO_MAX | 0.25 | # 敌方/己方海军强度比达到该值时，力量投射评分将被完全压制。比率为 0 时无惩罚，并线性缩放至该比率时评分为 0 倍。 |
| INTERCEPT_HOSTILE_NAVAL_RATIO_FOR_FULL_SCORE | 0.25 | # 敌方/己方海军强度比达到该值时，拦截与防卫海岸任务获得满分。低于该比率时评分按线性缩减。 |
| INTERCEPT_ACCEPTABLE_DISTANCE | 1000 | # 有效补给距离低于该值时不受距离惩罚。高于该值时，评分除以（distance / acceptable_distance）。 |
| POWER_PROJECTION_ACCEPTABLE_DISTANCE | 2500 |  |
| BLOCKADE_ACCEPTABLE_DISTANCE | 1000 |  |
| RAID_SUPPLY_ACCEPTABLE_DISTANCE | 1000 |  |
| PROTECT_SUPPLY_ACCEPTABLE_DISTANCE | 1000 |  |
| PORT_BOMBARDMENT_ACCEPTABLE_DISTANCE | 1000 |  |
| HUNT_PIRATES_ACCEPTABLE_DISTANCE | 1000 |  |
| DEFEND_COAST_ACCEPTABLE_DISTANCE | 1000 |  |
| RAID_SUPPLY_OUTCLASSED_MULT | 2.0 |  |
| PROTECT_SUPPLY_OUTCLASSED_MULT | -1.0 |  |
| DEFEND_COAST_OUTCLASSED_MULT | -4.0 |  |
| BLOCKADE_OUTCLASSED_MULT | -4.0 |  |
| PORT_BOMBARDMENT_OUTCLASSED_MULT | -4.0 |  |
| PROTECT_SUPPLY_DOMINANCE_PENALTY | 0.75 | # 在压制敌方海军时，补给保护评分降低的幅度。达到完全优势时，评分会按此数值减少（例如 0.9 表示在完全优势下评分降至 10%）。 |
| PROTECT_SUPPLY_MIN_DOMINANCE_MULT | 0.1 | # 海军优势期间补给保护的最小乘数。防止 AI 完全忽视补给保护。 |
| BLOCKADE_DOMINANCE_BOOST | 3.0 | # 在压制敌方海军时，封锁评分的提升幅度。以乘数形式相加（例如 3.0 表示在完全优势下评分最高可达 4.0 倍）。 |
| PORT_BOMBARDMENT_DOMINANCE_BOOST | 3.0 | # 在压制敌方海军时，港口炮击评分的提升幅度。 |
| COMFORTABLE_HQ_NAVY_SIZE | 10 | # AI 认为要使一处总部被视为至关重要，至少希望在该总部驻扎的规模 |
| NAVAL_HQ_IMPORTANCE_MIN_SCORE | 2 | # 评分低于此数值的任何海军总部都会被忽略 |

## 00_audio

### 音频

| Define | 默认值 | 开发者注释 |
|---|---|---|
| DEFAULT_SELECT | "event:/SFX/UI/Global/select" |  |
| MAXIMAP_ACTIVATION | "event:/SFX/UI/MaxiMap/activate" |  |
| MAXIMAP_DEACTIVATION | "event:/SFX/UI/MaxiMap/deactivate" |  |
| MAP_LENS_political_lens | "event:/SFX/UI/MapLenses/political" |  |
| MAP_LENS_production_lens | "event:/SFX/UI/MapLenses/production" |  |
| MAP_LENS_diplomatic_lens | "event:/SFX/UI/MapLenses/diplomatic" |  |
| MAP_LENS_military_lens | "event:/SFX/UI/MapLenses/military" |  |
| MAP_CLICKSOUND | "event:/SFX/UI/Global/map_click" |  |
| MAP_HOVERSOUND | "event:/SFX/UI/Global/map_hover" |  |
| MAP_INTERACTION_INVALID_CLICKSOUND | "" |  |
| MAP_INTERACTION_HOVERSOUND | "event:/SFX/UI/Global/map_hover_interact" |  |
| DIPLOMATIC_ACTION_CONFIRMATION | "event:/SFX/UI/Global/confirm" |  |
| DIPLOMATIC_ACTION_REQUEST | "event:/SFX/UI/MapInteraction/diplomatic_action_request" |  |
| DIPLOMATIC_ACTION_HOSTILE | "event:/SFX/UI/MapInteraction/diplomatic_action_hostile" |  |
| DIPLOMATIC_ACTION_BENIGN | "event:/SFX/UI/MapInteraction/diplomatic_action_benign" |  |
| DIPLOMATIC_PLAY | "event:/SFX/UI/MapInteraction/diplomatic_play" |  |
| DIPLOMATIC_PLAY_EPIC | "event:/SFX/UI/MapInteraction/diplomatic_play_epic" |  |
| INFORMATION_PANEL_HIDE | "event:/SFX/UI/Global/panel_hide" |  |
| MILITARY_FORMATION_DRAG_SELECTION_ADDED | "event:/SFX/UI/Global/increment" |  |
| MILITARY_FORMATION_DRAG_SELECTION_REMOVED | "event:/SFX/UI/Global/decrement" |  |
| DEFAULT_NOTIFICATION_SOUND | "event:/SFX/UI/Alerts/Toasts/_transient" |  |
| POSITIVE_GAMEOVER_SOUND | "event:/MUSIC/Stingers/game_over/positive" |  |
| NEGATIVE_GAMEOVER_SOUND | "event:/MUSIC/Stingers/game_over/negative" |  |
## 00_graphics

### MapMode（地图模式）

| Define | 默认值 | 开发者注释 |
|---|---|---|
| # 使用不透明度 1 作为颜色默认值，并直接在地图模式中控制最终不透明度 #（或出于非常具体的原因进行非常特殊的调用以偏离此默认值） @opacity = 1 ### 交互式地图模式 ### |  |  |
| MAP_PAINTING_TEXTURE_TILING | 50 | # 地图模式纹理的平铺 |
| MAP_PAINTING_FLATMAP_TEXTURE_TILING | 30 | # 平面地图（flatmap）中地图模式纹理的平铺 |
| # 建造（Construction）会根据预期收益缩放其不透明度 # 这是最低的标量值（最低预期收益），以避免完全透明 |  |  |
| MAP_PAINTING_CONSTRUCTION_LOW_OPACITY | 0.4 |  |
| ### 热度图地图模式 ### |  |  |
| HEAT_MAP_COLOR_FROM | { 0.9 0.9 0.1 0.3 } |  |
| HEAT_MAP_COLOR_TO | { 0.1 0.4 0.2 1.5 } |  |
| HEAT_MAP_MIN_ALPHA | 0.4 | # 用于利益集团和市场地图模式 |
| ### 高亮 ### |  |  |
| HIGHLIGHT_COLOR | { 1 1 1 0.5 } | # 白色 |
| HIGHLIGHT_INTERACTION_COLOR | { 1 0.57 0.15 0.5 } | # 金色 |
| CAMERA_HEIGHT_START_FADING_HIGHLIGHT | 800 | # 相机高度达到多少时应开始淡出高亮？ |
| CAMERA_HEIGHT_FULLY_FADED_HIGHLIGHT | 0 | # 相机高度达到多少时应完全淡出？ |
| HIGHLIGHT_ALPHA | 0.2 | # 用于内战高亮 |
| ### 未集权 ### |  |  |
| COLOR_DECENTRALIZED_COUNTRY | { 0.88 0.83 0.72 1.0 } | # Alpha 可控制与国家颜色的混合 |
| ### 不可通行地形 ### |  |  |
| COLOR_IMPASSABLE_TERRAIN | { 0.0 0.0 0.0 0.5 } | # Alpha 可控制与地形颜色的混合 |
| IMPASSABLE_TERRAIN_TILING | 100 | # 纹理的平铺 |
| IMPASSABLE_TERRAIN_HEIGHT | 8 | # 视差效果的高度 |
| ### 近距离淡出 ### # 用于边界和不可通行地形 |  |  |
| DISTANCE_FADE_START | 100.0f | # 放大视角时开始淡出的高度 |
| DISTANCE_FADE_END | 30.0f | # 完全淡出的高度 |
| ### 战争 / 外交 ### |  |  |
| COLOR_WAR_SELF | { 0.11 0.46 0.05 @opacity } | # 绿色 |
| COLOR_WAR_ENEMY | { 0.5 0.04 0.02 @opacity } | # 红色 |
| COLOR_WAR_ALLY | { 0 0.2 0.5 @opacity } | # 蓝色 |
| COLOR_WAR_NEUTRAL | { 0 0 0 0 } | # 无颜色 |
| COLOR_DIPLO_PLAY_ALLY | { 0 0.2 0.5 0.25 } | # 非常淡的蓝色 |
| COLOR_DIPLO_PLAY_ENEMY | { 0.5 0.04 0.02 0.25 } | # 非常淡的红色 |
| COLOR_DIPLO_PLAY_UNDECIDED | { 0.85 0.85 0.08 0.1 } | # 极淡的黄色 |
| # 杂项 |  |  |
| STATE_REGION_COLOR_STRENGTH | 0.2 | # 在生产视角（Production Lens）中，州的颜色应有多少基于州颜色？ |
| MAP_COLOR_SATURATION_LOW | 0.25 | # 若地图颜色的饱和度低于 25% 则调高 |
| MAP_COLOR_SATURATION_HIGH | 0.75 | # 若地图颜色的饱和度高于 75% 则调低 |
| COLOR_COUNTRY_CREATE_IN | { 0.11 0.46 0.05 1 } | # 悬停释放国家时以绿色高亮地图上的州 |
| COLOR_COUNTRY_CREATE_NOT_IN | { 0.5 0.04 0.02 1 } | # 悬停释放国家时以红色高亮地图上的州 |
| # 外交 |  |  |
| COLOR_RELATIONS_MIN | { 0.5 0.04 0.02 @opacity } | # 红色（全不透明度，用于热度图） |
| COLOR_RELATIONS_MAX | { 0.11 0.46 0.05 @opacity } | # 绿色（全不透明度，用于热度图） |
| COLOR_INFAMY_MIN | { 0.5 0.04 0.02 0 } | # 红色（无透明度分量） |
| COLOR_INFAMY_MAX | { 0.5 0.04 0.02 @opacity } | # 红色（全不透明度，用于热度图） |
| # AI 态度地图颜色 @full = 1 @slightly = 0.75 @very_slightly = 0.5 |  |  |
| COLOR_DIPLOMACY_SELF | { 0 0.2 0.5 @slightly} | # 蓝色 |
| COLOR_BELLIGERENT | { 0.5 0.04 0.02 @full } | # 红色 |
| COLOR_DOMINEERING | { 0.5 0.04 0.02 @full } | # 红色 |
| COLOR_ANTAGONISTIC | { 0.5 0.04 0.02 @slightly } | # 略带红色 |
| COLOR_REBELLIOUS | { 0.5 0.04 0.02 @full } | # 红色 |
| COLOR_WARY | { 0.5 0.04 0.02 @very_slightly } | # 非常淡的红色 |
| COLOR_DISINTERESTED | { 1 1 1 0 } | # 无颜色 |
| COLOR_CAUTIOUS | { 0.85 0.85 0.08 0.5 } | # 黄色 |
| COLOR_CONCILIATORY | { 0.11 0.46 0.05 @very_slightly } | # 极少量绿色 |
| COLOR_COOPERATIVE | { 0.11 0.46 0.05 @very_slightly } | # 极少量绿色 |
| COLOR_LOYAL | { 0.11 0.46 0.05 @slightly } | # 略带绿色 |
| COLOR_PROTECTIVE | { 0.11 0.46 0.05 @slightly } | # 略带绿色 |
| COLOR_GENIAL | { 0.11 0.46 0.05 @full } | # 绿色 |
| COLOR_DEFIANT | { 0.11 0.46 0.05 @full } | # 绿色 |
| COLOR_ALOOF | { 0.85 0.85 0.08 0.5 } | # 黄色 |
| # 可置于“好-坏”刻度上的热力图 |  |  |
| HEAT_MAP_BAD | { 0.5 0.04 0.02 1 } | # 红色 |
| HEAT_MAP_GOOD | { 0.11 0.46 0.05 1 } | # 绿色 |
| HEAT_MAP_NEUTRAL | { 0.75 0.75 0.75 1 } | # 白色 |
| # 本地价格 |  |  |
| LOCAL_PRICE_MAP_HIGH | { 1.000 0.674 0.454 2 } | # 金色 |
| LOCAL_PRICE_MAP_LOW | { 0.410 0.670 0.740 2 } | # 蓝色 |
| LOCAL_PRICE_MAP_MID | { 0.75 0.75 0.75 1 } | # 白色 |
| # 激进派与忠诚派热力图颜色 |  |  |
| RADICALS_HEAT_BASE | { 0.5 0.04 0.02 0 } | # 红色，但透明度为零 |
| RADICALS_HEAT_MAX | { 0.5 0.04 0.02 1 } | # 红色 |
| RADICAL_PERCENTAGE_OF_POPULATION | 0.25 | # 在激进派地图模式中，如果某州的激进派数量超过 X，该州将以 RADICALS_HEAT_MAX 着色 |
| LOYALISTS_HEAT_BASE | { 0.11 0.46 0.05 0 } | # 绿色，但透明度为零 |
| LOYALISTS_HEAT_MAX | { 0.11 0.46 0.05 1 } | # 绿色 |
| LOYALIST_PERCENTAGE_OF_POPULATION | 0.25 | # 在忠诚派地图模式中，如果某州的忠诚派数量超过 X，该州将以 LOYALISTS_HEAT_MAX 着色 |
| # 宗教/文化地图模式参数 |  |  |
| RELIGION_SECOND_COLOR_CUTOFF | 0.3 | # 宗教2 /（宗教1+宗教2）的比例至少要达到该值才会显示 |
| RELIGION_THIRD_COLOR_CUTOFF | 0.1 | # 宗教3 /（宗教1+宗教2+宗教3）的比例至少要达到该值才会显示 |
| RELIGION_SECOND_COLOR_SCALING | 0.6 | # 在从颜色1插值到颜色2时，宗教2 /（宗教1+宗教2）的比例按此系数缩放 |
| RELIGION_THIRD_COLOR_SCALING | 0.5 | # 在从颜色1+2插值到颜色3时，宗教3 /（宗教1+宗教2+宗教3）的比例按此系数缩放 |
| CULTURE_SECOND_COLOR_CUTOFF | 0.4 | # 文化2 /（文化1+文化2）的比例至少要达到该值才会显示 |
| CULTURE_THIRD_COLOR_CUTOFF | 0.2 | # 文化3 /（文化1+文化2+文化3）的比例至少要达到该值才会显示 |
| CULTURE_SECOND_COLOR_SCALING | 0.6 | # 在从颜色1插值到颜色2时，文化2 /（文化1+文化2）的比例按此系数缩放 |
| CULTURE_THIRD_COLOR_SCALING | 0.5 | # 在从颜色1+2插值到颜色3时，文化3 /（文化1+文化2+文化3）的比例按此系数缩放 |
| RELIGION_MINORITY_COLOR_CUTOFF | 0.334 | # 少数宗教 /（多数宗教+少数宗教）的比例至少要达到该值才会显示 |
| CULTURE_MINORITY_COLOR_CUTOFF | 0.334 | # 少数文化 /（多数文化+少数文化）的比例至少要达到该值才会显示 |
| # 污染热力图颜色 |  |  |
| POLLUTION_HEAT_BASE | { 0.3 0.25 0.16 0 } |  |
| POLLUTION_HEAT_MAX | { 0.3 0.25 0.16 1 } |  |
| POLLUTION_COLOR_CEILING_VALUE | 0.6 | # 在污染地图模式中，某州的污染达到 POLLUTION_MAX 的该比例时将呈现 POLLUTION_HEAT_MAX |
| # 顽固度热力图颜色 |  |  |
| OBSTINANCE_HEAT_BASE | { 0.0 0.0 1.0 0 } |  |
| OBSTINANCE_HEAT_MAX | { 0.0 0.0 1.0 1 } |  |
| OBSTINANCE_COLOR_CEILING_VALUE | 0.6 | # 在顽固度地图模式中，某州的顽固度达到 OBSTINANCE_MAX 的该比例时将呈现 OBSTINANCE_HEAT_MAX |
| # 收成状况地图模式 |  |  |
| HARVEST_CONDITION_COLOR_MIN_ALPHA | 0.4 | # 省份的最小颜色为该收成状况类型的颜色（最大颜色）乘以此透明度 |
| # 受收成状况影响的省份颜色会根据该区域的最大强度进行缩放。# 该值定义了一个收成状况区域内部可以有多少种不同颜色。# 例如，4 将给出以下区间：0-0.25、0.25-0.5、0.5-0.75、0.75-1 |  |  |
| HARVEST_CONDITION_NUM_COLOR_BRACKETS | 5 |  |
| HARVEST_CONDITION_FADE_DURATION | 0.4 | # 收成状况地图模式在切换高亮类型时的淡入淡出时长 |
| #饥荒地图模式的颜色 |  |  |
| STARVATION_HEAT_BASE | { 0.6 0.25 0.08 0 } | # 饥荒地图模式的基础颜色 |
| STARVATION_ADDITIONAL_BASE_ALPHA | { 0.0 0.0 0.0 0.2 } | # 在人口混合之后，我们为颜色添加这么多 alpha 值，使低百分比的州更加可见 |
| MILD_STARVATION_HEAT_MAX | { 0.741 0.301 0.082 1} | # 轻度饥荒的最大颜色 |
| MILD_STARVATION_HEAT_WEIGHT | 1 | # 混合轻度与严重饥荒颜色时使用的权重 |
| SEVERE_STARVATION_HEAT_MAX | { 0.69 0.08 0.06 1 } | # 严重饥荒的最大颜色 |
| SEVERE_STARVATION_HEAT_WEIGHT | 3 | # 混合轻度与严重饥荒颜色时使用的权重 |
| STARVATION_COLOR_CEILING_VALUE | 0.8 | # 州人口饥饿比例达到多少百分比时达到最大颜色 |

### MapName

| Define | 默认值 | 开发者注释 |
|---|---|---|
| NAME_DRAW_DISTANCE | 4000.0 | # 超出此距离后移除名称 |
| NAME_FONT_NAME | "PlayfairDisplay" | # 绘制地图名称所使用的字体 |
| NAME_FONT_SIZE | 80 | # 绘制地图名称所使用的字号 |
| FADE_SPEED | 2.0 | # 名称淡入/淡出的速度 |
| MAX_OPACITY | 0.8 |  |
| MIN_OPACITY | 0.0 | # 最小不透明度。因绘制距离而被隐藏的名称仍会淡出至 0 |
| MIN_PROVINCES | 3 | # 生成一个名称所需的最少省份数量 |
| ZOOM_STEPS_VISIBLE_SCALES | { 0.0 0.0 # 0 0.0 0.0 # 1 0.0 0.0 # 2 0.0 0.0 # 3 0.0 0.05 # 4 0.0 0.1 # 5 0.0 0.2 # 6 0.0 1.0 # 7 Terrain map 0.0 1.0 # 8 0.0 2.0 # 9 0.0 5.0 # 10 Flatmap 0.0 5.0 # 11 0.0 5.0 # 12 0.0 5.0 # 13 No 2D UI on Map 0.0 5.0 # 14 0.0 5.0 # 15 } | # 每个地图名称都有一个比例。此列表包含每个缩放级别的最小值-最大值。如果名称的比例超出该范围，它将不可见 # min（隐藏过小的名称） # max（名称过大时将其隐藏） |

### JominiMapGraphics

| Define | 默认值 | 开发者注释 |
|---|---|---|
| MAP_OBJECT_CELL_COUNT | 100 |  |
| MAP_OBJECT_FADE_SPEED | 5.0 |  |
| COUNTRY_NAMES_TEST_LINES_SPACING | 3.0 |  |
| COUNTRY_NAMES_SCALE | 0.6 |  |
| COUNTRY_NAMES_SCALE_CAP_WIDTH | 0.9 |  |
| COUNTRY_NAMES_SCALE_CAP_HEIGHT | 0.6 |  |
| COUNTRY_NAMES_NUM_LINE_TESTS | 1 |  |
| COUNTRY_NAMES_MAX_STRETCH_FACTOR | 1.6 |  |
| COUNTRY_NAMES_STRIDE_SIZE | 8 |  |
| COUNTRY_NAMES_LOD_FACTOR | 0.05 | # 作为一种抗锯齿形式，名称会随着纹素/像素比的增加而变得更模糊。模糊量为 lod 因子 * 纹素/像素比 |
| COUNTRY_NAMES_THICKNESS_BIAS | 0.0 | # 偏置越大 = 地图名称越粗。可用于解决由细窄区域造成的伪影 |
### JominiGraphics

| Define | 默认值 | 开发者注释 |
|---|---|---|
| BLOOM_ITERATIONS | 6 | # 被 environment.txt 覆盖 |
| NULL_ENTITY | "test_object_entity" |  |
| NULL_MESH | "test_object_mesh" |  |

### JominiEars

| Define | 默认值 | 开发者注释 |
|---|---|---|
| RANGE_MIN | 10.0 |  |
| RANGE_MAX | 2000.0 |  |

### Graphics

| Define | 默认值 | 开发者注释 |
|---|---|---|
| # 渐变边界 |  |  |
| PROVINCE_BORDER_FADE_NEAR | 200 |  |
| PROVINCE_BORDER_FADE_FAR | 2000 |  |
| STATE_BORDER_FADE_NEAR | 200 |  |
| STATE_BORDER_FADE_FAR | 2000 |  |
| IMPASSABLE_BORDER_FADE_NEAR | 500 |  |
| IMPASSABLE_BORDER_FADE_FAR | 600 |  |
| DRAW_SHADOWS_CUTOFF | 400 |  |
| DRAW_SHADOWS_FADE_LENGTH | 50 |  |
| # 调整纸面地图的海岸线条纹 |  |  |
| SHORELINE_MASK_BLUR | 4.5 | # 建议范围 [1.0 - 10.0] 地形/海洋遮罩，遮罩越模糊可以让线条延伸得越远 |
| SHORELINE_EXTENT_STR | 8.0 | # 建议范围 [0.0 - 10.0] 线条的简单强度 |
| SHORELINE_ALPHA | 0.6 | # 建议范围 [0.0 - 5.0] 简单的透明度调整 |
| SHORELINE_UV_SCALE | 40 | # 建议范围 [10 - 100]（整数）UV 缩放越大线条越紧密 |
| # 覆盖层细节 |  |  |
| FLATMAP_FOLDS_COLOR | { 1.0 1.0 1.0 0.12 } | # 折痕的颜色与透明度 [ 红色通道 ] |
| FLATMAP_LINES_COLOR | { 0.0 0.0 0.0 0.4 } | # 线条的颜色与透明度 [ 绿色通道 ] |
| FLATMAP_FOLDS_COLOR | { 0.0 0.0 0.0 1.0 } | # 平面地图上陆地细节的不透明度 |
| FLATMAP_OVERLAY_LAND_OPACITY | 0.45 |  |
| FLATMAP_EQUATOR_POSITION | 0.58 | # 距顶部的位置偏移 [ 0.0 - 1.0 ] |
| FLATMAP_EQUATOR_TILING | 24.0 | # 赤道纹理的平铺比例（即实际大小） |
| # 底部网格着色渐变（全局应用于所有网格） |  |  |
| MESHTINT_HEIGHT_MIN | 0.0 | # 着色起点（自底部起） |
| MESHTINT_HEIGHT_MAX | 0.07 | # 着色终点 |
| MESHTINT_COLOR | { 0.20 0.14 0.06 1.0 } | # 着色的透明度与颜色（透明度为 0.0 时实际上被禁用） |
| # SSAO 修正项 |  |  |
| SSAO_TREE_ALPHA | 0.2 | # 树木上的 AO 透明度 |
| SSAO_TERRAIN_ALPHA | 0.85 | # 树木和建筑下方地形上的 AO 透明度 |
| SSAO_MESH_COLOR | { 0.20 0.14 0.06 0.0 } | # 建筑上的 AO 透明度与颜色（透明度未使用） |
| # 雾效摄像机修正项 |  |  |
| FOG_CLOSE_OFFSET | 10 | # 近距离缩放级别下的雾中心偏移 |
| FOG_FAR_OFFSET | 260 | # 远距离缩放级别下的雾中心偏移 |
| FOG_WIDTH_SCALE | 1.6 | # 雾宽度缩放 |
| # 饼图颜色 |  |  |
| PIE_CHART_TIMER_UNFILLED_COLOR | { 0.4 0.4 0.4 1.0 } |  |
| PIE_CHART_TIMER_FILLED_COLOR | { 0.85 0.72 0.44 1.0 } |  |
| # 地图标记 |  |  |
| MAP_MARKER_MERGE_DISTANCE_FOR_STACK | 10 | # 地图标记（中心点）之间形成堆叠的最大屏幕像素距离 |
| MAP_MARKER_MERGE_PROVINCES | 800.0 |  |
| MAP_MARKER_MERGE_STATES | 1600.0 |  |
| MAP_MARKER_MERGE_PROVINCES_STRATEGIC_REGION | 1600.0 |  |
| MAP_MARKER_FULL_UPDATE_FREQUENCY | 1.0 | #每 X 秒才执行地图标记的繁重计算部分 |
| FRONT_MARKER_ADVANTAGE_HIGH | 60 |  |
| FRONT_MARKER_ADVANTAGE_LOW | 25 |  |
| # 误差修正 |  |  |
| MINIMUM_PROVINCE_SIZE_IN_PIXELS | 0 | # 小于该尺寸的省份会让游戏无法正常进行。它不影响游戏，只会在 error.log 中提示 |
| # 平面地图专属 |  |  |
| FLAT_MAP_HEIGHT | 3.92 |  |
| FLAT_MAP_FADE_SPEED | 5.0 | # 淡入/淡出至平面地图状态的速度 |
| FLAT_MAP_ZOOM_STEP | 10 | # 在哪个缩放级别淡入为平面地图 |
| # 水体修正 |  |  |
| WATER_SHADOW_MULTIPLIER | 0.75 | # 控制水体阴影亮度（将环境立方体贴图乘以该值并作为光照加入阴影中） |
| # 商品颜色 |  |  |
| GOOD_CATEGORY_MILITARY | { 0.29 0.16 0.17 1 } |  |
| GOOD_CATEGORY_STAPLE | { 0.18 0.28 0.24 1 } |  |
| GOOD_CATEGORY_INDUSTRIAL | { 0.29 0.24 0.16 1 } |  |
| GOOD_CATEGORY_LUXURY | { 0.33 0.2 0.32 1 } |  |
| # 士气颜色 |  |  |
| MORALE_HIGH | { 0.14 0.60 0.2 1 } |  |
| MORALE_MEDIUM | { 0.7 0.5 0.1 1 } |  |
| MORALE_LOW | { 0.65 0.1 0.1 1 } |  |
| # 组织度颜色 |  |  |
| ORGANIZATION_HIGH | { 0.14 0.60 0.2 1 } |  |
| ORGANIZATION_MEDIUM | { 0.7 0.5 0.1 1 } |  |
| ORGANIZATION_LOW | { 0.65 0.1 0.1 1 } |  |
| # 忠诚度颜色 |  |  |
| LOYALTY_LOYALIST | { 0.39 0.67 0.33 1 } |  |
| LOYALTY_RADICAL | { 0.88 0.34 0.34 1 } |  |
| LOYALTY_NEUTRAL | { 0.7 0.7 0.7 1 } |  |
| UNIMPORTANT_ELEMENT_ALPHA | 0.3 |  |
| # 荒废度贴图 |  |  |
| DEVASTATION_MATERIAL_NAME | "DYNAMIC-Devastation_Mud_01" | # 来自 materials.settings 的材质名称 |
| POLLUTION_MATERIAL_NAME | "DYNAMIC-Pollution_01" | # 来自 materials.settings 的材质名称 |
| # 革命图层 |  |  |
| REVOLUTION_MAP_OBJECT_LAYER | "revolution_dynamic" |  |
| REVOLUTION_MAP_OBJECT_UPDATE_PROVINCES_PER_FRAME | 16 | # 每帧最多可更新的省份数量。 |
| REVOLUTION_MAP_OBJECT_UPDATE_MAX_TIME_PER_FRAME | 0.002 | # 每帧用于动态地形更新的最长时间（秒）。 |
| # 夜间地图物体 |  |  |
| NIGHT_MAP_OBJECT_LAYERS | { "night_dynamic" "night_effects" } | # 在夜间激活的图层 |
| DAY_MAP_OBJECT_LAYERS | { "day_dynamic" "day_effects" } | # 在白天激活的图层 |
| # 动态地图物体 |  |  |
| HIDDEN_MAP_OBJECT_LAYERS | { "mines_dynamic" "farms_dynamic" "forestry_dynamic" } | # 这些图层在游戏开始时默认隐藏 |
| DYNAMIC_MAP_OBJECT_LAYERS | { "semidynamic" "semidynamic_medium" "semidynamic_high" "mines_dynamic" "farms_dynamic" "forestry_dynamic" } | # 这些图层会被城市增长和道路裁剪 |
| DYNAMIC_MAP_OBJECT_MASK_THRESHOLD_SHOW | 0.1 | # 动态物体显示/隐藏时使用材质遮罩。该值决定遮罩在何种阈值下使物体显示/隐藏。 |
| DYNAMIC_MAP_OBJECT_MASK_THRESHOLD_HIDE | 0.05 |  |
| DYNAMIC_TERRAIN_ROAD_WIDTH | 2.5 | # 控制清除地图物体时道路被视为的宽度 |
| DYNAMIC_TERRAIN_LAZY_UPDATE_PROVINCES_PER_FRAME | 16 | # 每帧最多可更新的省份数量。 |
| DYNAMIC_TERRAIN_LAZY_UPDATE_MAX_TIME_PER_FRAME | 0.0012 | # 每帧用于动态地形更新的最长时间（秒）。 |
| # 路径样条修复 |  |  |
| ROUTE_GENERATION_NAV_MESH_DENSITY | 0.375 | # 控制用于生成道路系统的导航网格顶点密度 |
| # 旗帜 |  |  |
| FLAG_TEXT_ICON_FONT_SIZE | 16 |  |
| FLAG_TEXT_ICON_SIZE | { 21 14 } |  |
| FLAG_TEXT_ICON_RESOLUTION | { 48 32 } |  |
| FLAG_TEXT_ICON_OFFSET | { 0 1 } |  |
| POWER_BLOC_COA_TEXT_ICON_FONT_SIZE | 16 |  |
| POWER_BLOC_COA_TEXT_ICON_SIZE | { 22 22 } | # 此处与国家旗帜文本图标的高度相同。 |
| POWER_BLOC_COA_TEXT_ICON_RESOLUTION | { 128 128 } | # 此处使用较高分辨率，以免在大号文本或 GUI 缩放下变模糊。 |
| POWER_BLOC_COA_TEXT_ICON_OFFSET | { 0 4 } |  |
| COA_FLAGS_FRAMES_BETWEEN_UPDATES | 30 | # 每隔该帧数更新一次国家与强权集团纹章 |
| COA_FLAGS_UPDATES_BETWEEN_CLEANUP | 20 | # 每隔该更新次数清理一次未使用的纹章 |
| ALERTS_FRAMES_BETWEEN_UPDATES | 5 |  |
| # 纹章 |  |  |
| COUNTRY_COLOR_LIST_NAME | "country_color_list" | # 生成动态国家地图颜色时使用的纹章列表 |
| # 缩放距离粗糙度 |  |  |
| DISTANCE_ROUGHNESS_POSITION | 1.8 | # 开始混合的位置 |
| DISTANCE_ROUGHNESS_BLEND | 80.0 | # 混合范围 |
| DISTANCE_ROUGHNESS_SCALE | 0.5 | # 粗糙度乘数比例 |
| # 用于城市的网格单元格得分 |  |  |
| CELL_SCORE_BASE | 1.0 | # 100% 位于省份内的单元格将获得完整的基础分。省份外的单元格得 0 分。50/50 的单元格将获得约一半的基础分。 |
| CELL_SCORE_UNDER_WATER_PENALTY | 10.0 | # 每个水下深度单位的惩罚值。对单元格的每个角都累加 |
| CELL_SCORE_SLOPE_MIN | 0.075 | # 惩罚生效前允许的坡度量。数值对应坡度的 'k'，即 f(x)=kx+m 中的 k |
| CELL_SCORE_SLOPE_PENALTY | 6 | # 每超出限制一个 'k' 的惩罚值。与坡度角不成线性关系，因此调整起来可能比较棘手 |
| CELL_SCORE_RIVER_PENALTY | 10.0 | # 每个"距河过近”单位（单元格中心到河岸边缘的距离 − 偏移量）的惩罚值 |
| CELL_SCORE_ROAD_PENALTY | 10.0 |  |
| # 前线实体图形 |  |  |
| FRONT_ENTITIES_CUTOFF | 300 | # 隐藏所有前线实体的缩放级别 |
| FRONT_DIORAMA_GRID_WIDTH | 20 | # 省份内立体布景的网格宽度 |
| FRONT_DIORAMA_GRID_HEIGHT | 20 | # 省份内立体布景的网格高度 |
| FRONT_DIORAMA_GRID_SCALE | 1.1 | # 省份内立体布景的网格单元格缩放比例 |
| FRONT_DIORAMA_STATE_DEFAULT | "idle" | # 实体无动作时（战前）的动画状态名称 |
| FRONT_DIORAMA_STATE_NO_GENERAL | "defend" | # 无将军命令的实体的动画状态名称 |
| FRONT_DIORAMA_FLAT_MAP_ENTITY | "generic_flatmap_unit_entity" | # 在平面地图模式下代替前线实体显示的实体 |
| # 战斗实体图形 |  |  |
| BATTLE_ENTITIES_CUTOFF | 300 | # 隐藏所有战斗实体的缩放级别 |
| BATTLE_DIORAMA_GRID_WIDTH | 30 | # 省份内立体布景的网格宽度 |
| BATTLE_DIORAMA_GRID_HEIGHT | 40 | # 省份内立体布景的网格高度 |
| BATTLE_DIORAMA_GRID_SCALE | 1.1 | # 省份内立体布景的网格单元格缩放比例 |
| BATTLE_DIORAMA_ATTACKER_STATE | "advance" | # 进攻方的动画状态名称 |
| BATTLE_DIORAMA_DEFENDER_STATE | "defend" | # 防守方的动画状态名称 |
| BATTLE_DIORAMA_DEFEAT_STATE | "defeat" | # 战斗期间被击败实体的动画状态名称 |
| BATTLE_DIORAMA_VICTORY_SIDE_STATE | "victory" | # 战斗结束后获胜方实体的动画状态名称 |
| BATTLE_DIORAMA_DEFEATED_SIDE_STATE | "idle" | # 战斗结束后战败方实体的动画状态名称 |
| BATTLE_DIORAMA_DESTRUCTION_DELAY | 5 | # 战斗结束后继续显示立体布景实体的秒数 |
| BATTLE_DIORAMA_VFX_START_TIME | 0 | # 战斗结束后多少秒开始在战斗双方显示 VFX（必须 <= BATTLE_DIORAMA_DESTRUCTION_DELAY） |
| BATTLE_DIORAMA_VFX_VICTORY_SIDE | "battle_diorama_victory_entity" | # 战斗结束后经过 BATTLE_DIORAMA_VFX_START_TIME 秒在获胜方生成的实体 |
| BATTLE_DIORAMA_VFX_DEFEATED_SIDE | "battle_diorama_defeat_entity" | # 战斗结束后经过 BATTLE_DIORAMA_VFX_START_TIME 秒在战败方生成的实体 |
| DAYS_AFTER_BATTLE_TO_SHOW_ENTITY | 7 | # 战斗结束后显示战斗环境实体的天数 |
| MILITARY_ENTITIES_FLYING_ENTITY_HEIGHT | 1 | # 如果实体定位器高于此数值，则该实体被视为飞行实体，即不占用单元格，也不遮挡其下方的地图物件 |
| MILITARY_ENTITIES_TOGGLE_MAP_OBJECTS_IN_RADIUS | 2 | # 实体周围应有多少个单元格用于隐藏地图物件（树木） |
| MILITARY_ENTITIES_DITHER_DURATION | 1.0 | # 立体布景实体逐渐显现或消失所需的秒数。适用于所有立体布景：前线、陆上战斗、舰队以及海战立体布景 |
| OCCUPATION_ENTITY | "military_occupation_flag_entity" | # 占领国在被占领土上显示的实体 |
| OCCUPATION_ENTITY_DIRECTION | { 0.0 0.0 -1.0 } | # 占领实体的方向 |
| COUNTRY_COLOR_BUFFER_TEXTURE_RESERVE_SIZE | 700 | # 初始为多少个国家的缓冲数据分配空间。如果创建更多国家，缓冲区将调整大小以容纳它们。 |
| POWER_BLOC_BUFFER_TEXTURE_RESERVE_SIZE | 50 | # 初始为多少个强权集团的缓冲数据分配空间。如果创建更多强权集团，缓冲区将调整大小以容纳它们。 |
| POWER_BLOC_COLOR_UPDATE_NUM_FRAMES_BETWEEN | 30 | # 强权集团地图颜色更新之间等待的帧数 |
| # 收成状况图形 |  |  |
| HARVEST_CONDITION_ENTITIES_CUTOFF | 600 | # 隐藏所有收成状况实体的缩放级别 |
| HARVEST_CONDITION_ENTITIES_INTERVAL | 50 | # 受收成状况影响的区域上实体之间的间隔 |
| HARVEST_CONDITION_ENTITY | "harvest_condition_sound_entity" | # 在受收成状况影响的区域上生成的实体 |
| HARVEST_CONDITION_INTENSITY_MAX | 10 |  |
| # 地震镜头震动 |  |  |
| EARTHQUAKE_SHAKE_AMPLITUDE | 0.25 | # 振幅倍率 |
| EARTHQUAKE_SHAKE_DURATION | 10.0 | # 持续时间（秒） |
| EARTHQUAKE_SHAKE_DISTANCE_RADIUS | 250 | # 距离半径（游戏单位） |
| EARTHQUAKE_SHAKE_FREQUENCY | 2 | # 频率倍率 |
| EARTHQUAKE_SHAKE_EASE_IN_PORTION | 0.5 | # 地震持续时间中用于缓入的部分 |
| EARTHQUAKE_SHAKE_EASE_OUT_PORTION | 0.5 | # 地震持续时间中用于缓出的部分 |
| EARTHQUAKE_SHAKE_MIN_ZOOM_STEP | 0 | # 若缩放到比此缩放级别更近，地震将不会影响镜头 |
| EARTHQUAKE_SHAKE_MAX_ZOOM_STEP | 800 | # 若缩放到比此缩放级别更远，地震将不会影响镜头 |
| EARTHQUAKE_SHAKE_SMOOTHSTEP_A | 3.0 | # 用于缓入缓出的平滑插值幂次 |
| EARTHQUAKE_SHAKE_SMOOTHSTEP_B | 2.0 | # 用于缓入缓出的平滑插值幂次 |
| EARTHQUAKE_SHAKE_PHASE_SPEED_X | 28.0 | # X 方向相位移动速度 |
| EARTHQUAKE_SHAKE_PHASE_SPEED_Y | 22.0 | # Y 方向相位移动速度 |

### 前端

| Define | 默认值 | 开发者注释 |
|---|---|---|
| CAMERA_START_X | 4150.0 | # 主菜单中的初始位置 |
| CAMERA_START_Y | 1500 | # Y 为高度 |
| CAMERA_START_Z | 2700.0 |  |

### 镜头

| Define | 默认值 | 开发者注释 |
|---|---|---|
| FOV | 55 | # 视场角 |
| ZNEAR | 1 |  |
| ZFAR | 50000 |  |
| EDGE_SCROLLING_PIXELS | 10 | # 距离窗口边缘多少像素时触发边缘滚动 |
| SCROLL_SPEED | 0.045 | # 数值越高 = 镜头越快。注意，此项也可在设置中调节 |
| ZOOM_RATE | 0.2 | # 按住鼠标右键时的缩放 |
|  | # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 |  |
| ZOOM_STEPS | { 24 32 40 50 75 100 200 300 400 600 800 1000 1200 1500 2500 4500 } |  |
| ZOOM_STEPS_TILT | { 35 40 45 48.5 50 52.5 55 60 65 70 75 80 80 85 85 85 } |  |
| ZOOM_STEPS_MIN_TILT | { 35 35 35 35 35 38 40 40 45 50 50 50 50 50 50 50 } |  |
| ZOOM_STEPS_MAX_TILT | { 89 89 89 89 89 89 89 89 89 89 89 89 89 89 89 89 } |  |
| MAX_PAN_TO_ZOOM_STEP_EXTRA_CLOSE | 1 | # 平移到人物/省份等时，镜头将降低到此高度（仅当高于该高度时） |
| MAX_PAN_TO_ZOOM_STEP_CLOSE | 7 |  |
| MAX_PAN_TO_ZOOM_STEP_FAR | 10 |  |
| MAX_PAN_TO_ZOOM_STEP_EXTRA_FAR | 14 |  |
| # 调试 defines |  |  |
| DEBUG_GAMEPAD_LOWSPEED | 25.0 |  |
| DEBUG_GAMEPAD_NORMALSPEED | 100.0 |  |
| DEBUG_GAMEPAD_HIGHSPEED | 300.0 |  |
| DEBUG_GAMEPAD_SENSITIVITY | 2.0 |  |
### 城市

| 定义 | 默认值 | 开发者注释 |
|---|---|---|
| #选择一个省份并使用 "Cities.DrawDebugLines" 以便轻松调整 |  |  |
| NUM_GRID_LAYOUTS | 16 | # 城市可选择多少种不同的网格布局。网格布局是随机生成的，城市会随机选取它们 |
| GRID_SCALE | 1.1 |  |
| MESH_SCALE | 1.0 | #按此比例缩放所有网格 |
| MAX_ACTIVE_SOUND_EFFECTS | 5 |  |
| CITY_RIVER_DISTANCE_BIAS | 0.75 | # 数值越高 = 越倾向于避开河流 |
| FARM_RIVER_DISTANCE_BIAS | 0.75 |  |
| MINE_RIVER_DISTANCE_BIAS | 0.75 |  |
| PORT_RIVER_DISTANCE_BIAS | 0.75 |  |
| WOOD_RIVER_DISTANCE_BIAS | 0.75 |  |
| CITY_ROAD_DISTANCE_BIAS | -1.00 |  |
| FARM_ROAD_DISTANCE_BIAS | 0.25 |  |
| MINE_ROAD_DISTANCE_BIAS | 0.25 |  |
| PORT_ROAD_DISTANCE_BIAS | -1.00 |  |
| WOOD_ROAD_DISTANCE_BIAS | 0.25 |  |
| RICH_SOL | 20.0 | # 平均生活水平高于此值的建筑使用富裕模型 |
| MID_SOL | 10.0 | # 平均生活水平高于此值的建筑使用中产阶级模型 |
| RESIDENTIAL_CHANGE_DELAY | 5.0 | # 城市更新住宅建筑的间隔时间（另有 0-1 秒的随机浮动） |
| RESIDENTIAL_PROMOTE_ENTITY | "residential_promotion_entity" | # 因人口结构变化而升级的住宅建筑上生成的实体 |
| RESIDENTIAL_DEMOTE_ENTITY | "residential_demotion_entity" | # 因人口结构变化而降级的住宅建筑上生成的实体 |
| CITY_VFX_MAX_ENTITIES | 128 | # 可同时存在的 VFX 实例数量上限 |
| CITY_VFX_ZOOM_CUTOFF | 250 | # 缩放到该级别时隐藏所有城市 VFX |
| CITY_PARTICLES_ZOOM_CUTOFF | 200 | # 缩放到该级别时隐藏所有城市粒子效果（例如烟囱烟雾） |
| # 相机与城市之间的每个距离都对应一个城市可见建筑数量的剔除系数 # 如果距离小于第一个阶梯，则系数为 0，即所有建筑均可见 # 如果距离大于最后一个阶梯，则采用最后一个阶梯的系数 # 如果距离介于两个阶梯之间，则系数按线性计算 |  |  |
| CITY_BUILDINGS_CUTOFF_DISTANCES | { 300 400 600 } | # 相机到城市的距离阶梯，对应各自的剔除系数，必须从低到高排序 |
| CITY_BUILDINGS_CUTOFF_FACTORS | { 0 0.7 0.95 } | # 在特定距离阶梯上剔除的建筑比例，必须从低到高排序 |
| NIGHT_LIGHT_COLOR_DEFAULT | { 1.0 0.16 0.035 6.5 } | # 灯光颜色，Alpha 为最大强度 |
| NIGHT_LIGHT_FADE_TIME | 0.35 | # 单个灯光从激活时开始淡入/淡出的时间 |
| NIGHT_LIGHT_ACTIVATE_BEGIN | 0.3 | # 灯光开始激活的时间点，处于 0.0 - 1.0 的循环中，白天为 0.0，0.5 为昼夜之间的中点 |
| NIGHT_LIGHT_ACTIVATE_END | 0.75 | # 灯光完成激活的时间点 |
### 要塞

| 定义项 | 默认值 | 开发者注释 |
|---|---|---|
| GAME_OBJECT_LOCATOR | "fortification" | # 要塞实体所使用的定位器（locator）键名 |
| CONSTRUCTION_ENTITY | "building_construction_2x2_entity" | # 在要塞建造进行中的省份上生成的实体 |
| ENTITY_DEFAULT | "strait_fortification_tower_european_entity" | # 找不到特定文化对应的实体时使用的默认要塞实体 |
| ENTITY_FORMAT | "strait_fortification_tower_{}_entity" | # 要塞实体的格式，{} 会被替换为图形文化名称（european、arabic、asian、african、latin） |
| TOGGLE_MAP_OBJECTS_IN_RADIUS | 2 | # 要塞实体周围多少格范围内的地图物件（树木）应被隐藏 |

### 路线

| 定义项 | 默认值 | 开发者注释 |
|---|---|---|
| DIRTROAD_BRIDGES | { "dirtroad_bridge_01" } |  |
| RAILROAD_1_BRIDGES | { "railroad_bridge_01" "railroad_bridge_02" } |  |
| BRIDGE_SIZES | { "_small_mesh" "_medium_mesh" "_large_mesh" } |  |
| CARAVAN_DISTANCE_OPACITY_THRESHOLD | 0.75 | # 商队距相机的距离与截止距离之比，达到该比例时其实体开始变得透明 |
| LAND_ENTITIES_CUTOFF | 300 | # 陆地路线实体隐藏时距相机的距离 |
| NAVAL_ENTITIES_CUTOFF | 650 | # 海上路线实体隐藏时距相机的距离 |
| AIR_ENTITIES_CUTOFF | 450 | # 空中路线实体隐藏时的缩放级别 |
| LAND_ENTITIES_UPDATE_DISTANCE_RATIO | 0.0005 | # 商队行进距离与距相机距离之比，用于决定商队实体的更新频率。该值越高，更新频率越低 |
| NAVAL_ENTITIES_UPDATE_DISTANCE_RATIO | 0.00025 | # 商队行进距离与距相机距离之比，用于决定商队实体的更新频率。该值越高，更新频率越低 |

### 肖像

| 定义项 | 默认值 | 开发者注释 |
|---|---|---|
| GRACEFUL_AGING_START | 25 | # 超过此年龄后，增加的预期寿命会使人物看起来比实际年龄更年轻；越往后该效果越明显 |
| GRACEFUL_AGING_END | 70 | # 这是预期寿命不再延缓视觉衰老的表观年龄（此后每过一年，视觉上就老一岁） |
| MAX_AGE | 100.0 | # 达到此年龄时，肖像将满强度使用特殊的年龄基因 |
| PORTRAIT_MALE_ADULT_AGE | 18 | # 男孩→男性肖像的切换发生在此年龄 |
| PORTRAIT_FEMALE_ADULT_AGE | 18 | # 女孩→女性肖像的切换发生在此年龄 |
### ProvinceHighlight

| 定义 | 默认值 | 开发者注释 |
|---|---|---|
| TEXTURE_WIDTH | 2048 |  |
| TEXTURE_HEIGHT | 1024 |  |
| # 省份高亮使用泊松圆盘采样来创建渐变 # 泊松圆盘能以更少的采样点覆盖更宽的采样区域 |  |  |
| KERNEL_SCALE | 8 | # 采样区域的大小，以世界空间计 |
| SAMPLE_COUNT | 16 | # 使用的采样点数量（最大 16） |

### TravelNetwork

| 定义 | 默认值 | 开发者注释 |
|---|---|---|
| FORMATION_CATCHUP_DISTANCE | 40.0 | # 如果军事编队的 3D 车队落后于其应在位置这一距离，则以追赶速度加速 |
| FORMATION_CATCHUP_SPEED_MULTIPLIER | 1.5 | # “追赶”时将平均速度乘以此系数 |
| FORMATION_CATCHUP_MIN_SPEED | 15.0 | # 追赶的最低速度 |
| FORMATION_CATCHUP_MAX_SPEED | 250.0 | # 追赶的最高速度 |
| FORMATION_SMOOTHING_STEP_COUNT | 5 | # 用于平滑视觉移动速度，军事编队速度以 X 步的滚动平均值计算 |
| FORMATION_SMOOTHING_STEP_TIME | 1.0 | # 军事编队速度平滑的每一步时长 |
| FORMATION_SMOOTHING_SPEED_MULTIPLIER | 1.2 | # 应用于平滑测量的通用速度乘数（“领先”比“落后”更好） |
| FORMATION_ARROW_SAMPLING_STEP | 7.0 | # 样条网络的采样步长（以“地图像素”计），用于创建箭头 |
| FORMATION_ARROW_SAMPLING_STEP_FLATMAP | 30.0 | # 样条网络的采样步长（以“地图像素”计），用于在缩小视图（"flatmap"）时创建箭头 |

### PowerBlocCoa

| 定义 | 默认值 | 开发者注释 |
|---|---|---|
| PREVIEW_BACKGROUND_PATTERN | "pattern_solid.tga" | # 纹章预览中用作背景的图案 |
| PREVIEW_BACKGROUND_COLOR | { 0.0 0.0 0.0 0.0 } | # 背景图案的第一种颜色 |
| PREVIEW_SHIELD_PATTERN_COLOR_1 | "red" | # 盾面图案的第一种颜色 |
| PREVIEW_SHIELD_PATTERN_COLOR_2 | "black" | # 盾面图案的第二种颜色 |
| PREVIEW_CENTER_COLOR_1 | "yellow" | # 中心部件的第一种颜色 |
| PREVIEW_CENTER_COLOR_2 | "black" | # 中心部件的第二种颜色 |
| COLOR_LIST_NAME | "power_bloc_colors" | # 随机创建强权集团时从哪个列表获取颜色。列表位于 common/coat_of_arms/template_lists/color_lists.txt |
| # 各部件类型的位置与缩放。更新这些数值时，务必同步更新 03_random_power_bloc.txt |  |  |
| SHIELD_PATTERN_SCALE | { 0.72 0.72 } |  |
| SHIELD_FRAME_SCALE | { 0.9 0.9 } |  |
| CENTER_SCALE | { 0.45 0.45 } |  |
| LEFT_SIDE_SCALE | { 0.65 0.65 } |  |
| RIGHT_SIDE_SCALE | { 0.65 0.65 } |  |
| TOP_SCALE | { 0.7 0.7 } |  |
| SHIELD_PATTERN_POSITION | { 0.49 0.6 } |  |
| SHIELD_FRAME_POSITION | { 0.5 0.6 } |  |
| CENTER_POSITION | { 0.49 0.54 } |  |
| LEFT_SIDE_POSITION | { 0.155 0.55 } |  |
| RIGHT_SIDE_POSITION | { 0.82 0.55 } |  |
| TOP_POSITION | { 0.5 0.19 } |  |
| # 图层自下而上排列。如果更改此顺序，请记得同步更新 `game/common/coat_of_arms/coat_of_arms/03_random_power_bloc.txt` |  |  |
| PIECE_LAYERS_ORDER | { "shield_pattern" "top" "shield_frame" "center" "side" "side" } |  |
| PIECE_LAYER_INDEX_TO_FLIP | 5 |  |
### PowerBlocStatueCamera

| Define | 默认值 | 开发者注释 |
|---|---|---|
| CAMERA_START_ROTATION | -2.7 |  |
| CAMERA_MIN_DISTANCE | 15.0 |  |
| CAMERA_MAX_DISTANCE | 30 |  |
| CAMERA_START_DISTANCE | 23.0 |  |
| CAMERA_ANGLE | 0.3925 | # 弧度值，0.3925 即 PI/8 |
| CAMERA_ROTATION_SPEED | 0.15 |  |
| CAMERA_DISTANCE_SPEED | 0.7 |  |

### 海军

| Define | 默认值 | 开发者注释 |
|---|---|---|
| FLEET_DIORAMA_INTERVAL | 20 | # 海节点中舰队立体场景之间的间隔 |
| FLEET_DIORAMA_CUTOFF | 600 | # 隐藏所有舰队实体的缩放级别 |
| FLEET_DIORAMA_TERRAIN_OPACITY_BLEND_SPEED | 4.0 | # 显示/隐藏舰队立体场景实体时地形不透明度的混合速度 |
| DIORAMA_SELECTION_DITHER_DURATION | 0.5 | # 选中状态改变时，立体场景实体逐渐出现或消失所需的秒数。适用于舰队及海战立体场景 |
| DIORAMA_LAND_HEIGHT_OFFSET | 0.5 | # 判定立体场景中舰船位于陆地上的高度偏移 |
| WATER_ENTITY_HEIGHT | 0.25 | # 高于水面的高度 |
| SHIP_ENTITY_STATE_IDLE | "idle" | # 舰船处于闲置状态，例如停驻在海节点中或战斗胜利/失败后 |
| SHIP_ENTITY_STATE_MOVE | "move" | # 舰船在战斗中移动 |
| SHIP_ENTITY_STATE_MOVE_LOCAL | "move_local" | # 舰船在地图航线上移动 |
| SHIP_ENTITY_STATE_MOVE_SHIP_VIEWER | "move_ship_viewer" | # 舰船在舰船查看器中移动 |
| SHIP_ENTITY_STATE_DISENGAGED | "disengaged" | # 武器实体处于默认朝向 |
| SHIP_ENTITY_STATE_COMBAT | "combat" | # 武器实体旋转至开火角度 |
| SHIP_ENTITY_STATE_FIRE | "fire" | # 舰船在战斗中开火 |
| SHIP_ENTITY_STATE_MISS | "miss" | # 舰船在战斗中躲开了敌方射击 |
| SHIP_ENTITY_STATE_DAMAGE | "damage" | # 舰船在战斗中受损 |
| SHIP_ENTITY_STATE_DAMAGE_CRITICAL | "damage_critical" | # 舰船在战斗中受到严重损伤 |
| SHIP_ENTITY_STATE_DAMAGE_WEAK | "damage_weak" | # 舰船在战斗中受到轻微损伤 |
| SHIP_ENTITY_STATE_UNDAMAGED | "undamaged" | # 舰船无受损视觉效果 |
| SHIP_ENTITY_STATE_DAMAGED_LIGHT | "damaged_light" | # 舰船轻度受损 |
| SHIP_ENTITY_STATE_DAMAGED_LIGHT_LOCAL | "damaged_light_local" | # 舰船在地图航线上轻度受损 |
| SHIP_ENTITY_STATE_DAMAGED_HEAVY | "damaged_heavy" | # 舰船重度受损 |
| SHIP_ENTITY_STATE_DAMAGED_HEAVY_LOCAL | "damaged_heavy_local" | # 舰船在地图航线上重度受损 |
| SHIP_ENTITY_STATE_DESTROYED | "destroyed" | # 舰船在战斗中被摧毁，但尚未沉没 |
| SHIP_ENTITY_STATE_SINK | "sink" | # 舰船在战斗中被摧毁后正在下沉 |
| SHIP_DAMAGE_LIGHT_THRESHOLD | 0.25 | # 判定舰船轻度受损的伤害比例 |
| SHIP_DAMAGE_HEAVY_THRESHOLD | 0.6 | # 判定舰船重度受损的伤害比例 |
| SHIP_DAMAGE_DESTROYED_THRESHOLD | 1.0 | # 判定舰船被摧毁的伤害比例 |
| SHIP_SCALE_GENERAL_FACTOR | 0.5 | # 立体场景展开状态下所有舰船实体按此系数缩放 |
| SHIP_MIN_SCALE | 0.2 | # 舰队立体场景中舰船实体的最小缩放，例如立体场景收缩状态起始时的舰船缩放 |
| SHIP_MAIN_ENTITY_SCALE | 3.0 | # 立体场景收缩状态下主舰实体的缩放 |
| SHIP_ANIMATION_SPEED_EXPAND | 1.0 | # 舰队立体场景放大时舰船展开动画的速度倍率 |
| SHIP_ANIMATION_SPEED_SHRINK | 2.0 | # 舰队立体场景缩小时舰船收缩动画的速度倍率 |
| SHIP_ANIMATION_SCALE_DURATION | 0.8 | # 舰队立体场景放大/缩小时舰船缩放动画的持续秒数 |
| SHIP_ANIMATION_ZOOM_STEP_EXPAND | 4 | # 舰队实体播放展开动画的缩放级别，例如在缩放级别 <= 6 时 |
| SHIP_ANIMATION_ZOOM_STEP_SHRINK | 5 | # 舰队实体应播放缩小动画的缩放级别，例如缩放级别 >= 8 时 |
| SHIP_ANIMATION_ROTATE_ON_MOVEMENT_PROGRESS | 0.5 | # 舰船开始朝目标方向旋转时的移动进度（0.0 - 1.0） |
| SHIP_ANIMATION_MOVE_ON_ROTATION_PROGRESS | 0.5 | # 舰船开始朝目标方向旋转时的移动进度（0.0 - 1.0） |
| SHIP_ANIMATION_MOVE_SPEED | 4.5 | # 舰队立体场景（diorama）中舰船移动的速度倍率 |
| SHIP_ANIMATION_ROTATE_SPEED | 1.5 | # 舰队立体场景中舰船旋转的速度倍率 |
| SHIP_ANIMATION_DISTANCE_FOR_FULL_OPACITY | 5.0 | # 舰船实体完全不透明时与主舰的距离 |
| SHIP_ANIMATION_DISTANCE_FOR_FULL_SCALE | 1.5 | # 舰船实体完全缩放时与主舰的距离 |
| SHIP_ANIMATION_HEAVE_SPEED | 1.5 | # 舰船实体起伏（heave）动画的速度 |
| SHIP_ANIMATION_HEAVE_AMPLITUDE | 0.04 | # 舰船实体起伏动画的幅度 |
| SHIP_STATE_FIRE_TIME_RANGE | { 10.0 20.0 } | # 开火动画之间的时间间隔范围 |
| SHIP_STATE_FIRE_SHOT_TRAVEL_TIME | 0.2 | # 舰船开火到目标受到命中/未命中 effect 之间的延迟（秒） |
| SHIP_STATE_FIRE_TIME | 2.0 | # 射击动画的持续时间（秒） |
| SHIP_STATE_FIRE_IMPACT | 1.0 | # 射击动画强度的基准冲击倍率 |
| SHIP_STATE_FIRE_ROLL_PEAK | 3.0 | # 射击动画的峰值横摇角（度），随冲击力缩放 |
| SHIP_STATE_FIRE_BUMP_PEAK | 0.2 | # 射击动画期间横摇颠簸达到峰值的归一化时间（0-1） |
| SHIP_STATE_FIRE_HEAVE_AMPLITUDE | 0.02 | # 射击起伏动画的下沉幅度，随冲击力缩放 |
| SHIP_STATE_FIRE_HEAVE_PEAK | 0.15 | # 射击动画期间起伏下沉达到峰值的归一化时间（0-1） |
| SHIP_WEAPON_ENGAGE_SPEED | 45.0 | # 舰船武器转向瞄准的速度（度/秒） |
| SHIP_IDLE_ROLL_AMPLITUDE | 2.0 | # 舰船待机动画的横摇幅度（度） |
| SHIP_IDLE_ROLL_SPEED | 1.2 | # 待机横摇摆动的速度 |
| SHIP_IDLE_HEAVE_AMPLITUDE | 0.04 | # 舰船待机动画的垂直起伏幅度 |
| SHIP_IDLE_HEAVE_SPEED | 1.5 | # 待机起伏摆动的速度 |
| SHIP_MOVE_PITCH_AMPLITUDE | 1.0 | # 舰船移动动画的纵摇幅度（度） |
| SHIP_MOVE_PITCH_SPEED | 1.0 | # 移动纵摇摆动的速度 |
| SHIP_MOVE_ROLL_AMPLITUDE | 4.0 | # 舰船移动动画的横摇幅度（度） |
| SHIP_MOVE_ROLL_SPEED | 1.2 | # 移动横摇摆动的速度 |
| SHIP_MOVE_HEAVE_AMPLITUDE | 0.06 | # 舰船移动动画的垂直起伏幅度 |
| SHIP_MOVE_HEAVE_SPEED | 1.5 | # 移动起伏摆动的速度 |
| BATTLE_DIORAMA_CIRCLING_TIME_RANGE | { 3.0 5.0 } | # 舰船环绕盘旋的随机时间范围（秒） |
| BATTLE_DIORAMA_CRUISING_ANGLE | 45.0 | # 舰船在立体场景中巡航的角度长度（度） |
| BATTLE_DIORAMA_SINKING_ANGLE | 90.0 | # 用于计算战败目标位置的角度偏移（度）（半圆以实现平滑接近） |
| BATTLE_DIORAMA_SINK_ON_DEFEAT_PROGRESS | 0.75 | # 舰船开始下沉时的战败状态进度（0.0 - 1.0f） |
| BATTLE_DIORAMA_SINK_TIME | 5.0 | # 海战立体场景中舰船实体战败后沉没所需的时间（秒） |
| BATTLE_DIORAMA_SINK_ROLL_TARGET | 120.0 | # 海战立体场景中沉没动画的目标横摇角（度） |
| BATTLE_DIORAMA_SINK_DEPTH_TARGET | 0.0 | # 海战立体场景中舰船实体 Y 坐标应下沉至的目标深度 |
| BATTLE_DIORAMA_DESTOY_TIME | 4.0 | # 海战立体场景中舰船实体沉没后被销毁所需的时间 |
| BATTLE_DIORAMA_DESTOY_DEPTH_TARGET | 1.0 | # 海战立体场景中舰船实体 Y 坐标下沉的目标深度 |
| BATTLE_DIORAMA_CURVE_B1_MULT | 0.4 | # 海战立体场景中舰船移动动画所用 B1 曲线参数的乘数，该参数定义移动路径的曲率 |
| BATTLE_DIORAMA_CURVE_B2_MULT | 0.3 | # 海战立体场景中舰船移动动画所用 B2 曲线参数的乘数，该参数定义移动路径的曲率 |
| BATTLE_DIORAMA_SHIP_ANGULAR_SPEED | 0.1 | # 海战立体场景动画中舰船旋转的速度乘数 |
| BATTLE_DIORAMA_SHIP_SCALE | 1.0 | # 海战立体场景动画中舰船实体的缩放比例 |
| BATTLE_DIORAMA_RADIUS_DEFAULT | 10.0 | # 舰船所处圆形的默认半径，即与立体场景中心的距离 |
| BATTLE_DIORAMA_RADIUS_RATIO_OUTER | 1.2 | # 舰船所处圆形外半径的比例 |
| BATTLE_DIORAMA_RADIUS_RATIO_INNER | 0.7 | # 舰船所处圆形内半径的比例 |
| BATTLE_DIORAMA_RADIUS_RATIO_DEFEAT | 0.3 | # 战败半径的比例——舰船在战败时移动到这一缩小的半径处 |
| BATTLE_DIORAMA_RETREAT_ANGLE_DELTA | 45.0 | # 舰船在立体场景中撤退时转过的角度（度数） |
| BATTLE_DIORAMA_RETREAT_RADIUS_RATIO | 2.0 | # 撤退半径的比例——舰船在撤退时移动到这一更大的半径处 |
| BATTLE_DIORAMA_LENGTH_PER_SHIP | 3.0 | # 用于在圆周上布置舰船以避免重叠的舰船长度 |
| BATTLE_DIORAMA_ANGLE_PER_SIDE | 120.0 | # 立体场景中每一战斗方占据的角度（度数） |
| BATTLE_DIORAMA_ROTATION_BLEND_SPEED | 6.0 | # 在环绕与巡航状态之间切换时的旋转混合速度。越高越利落，越低越平滑 |
| BATTLE_DIORAMA_TERRAIN_OPACITY_BLEND_SPEED | 2.0 | # 显示/隐藏战斗立体场景实体时地形不透明度混合的速度 |
| BATTLE_DIORAMA_DITHER_DURATION | 3 | # 战斗结束后立体场景实体的显示秒数 |
| BATTLE_DIORAMA_ROUTE_ENTITY_FADE_RANGE | 3.5 | # 航线实体舰船靠近海战立体场景时，在立体场景半径之外淡出的世界单位距离 |
| SHIP_LENGTH_DEFAULT | 3.0 | # 舰船的默认长度，用于计算航线图形中舰船之间的间距 |
| ROUTE_SHIPS_MAX | 10 | # 一支舰队在地图航线上可见的舰船图形最大数量 |
| ROUTE_SHIPS_INTERVAL | 2.0 | # 地图航线上舰船图形之间的间隔 |
| ROUTE_SHIPS_INTERVAL_RANDOM | 1.0 | # 地图航线上舰船图形间隔附加的随机变化量 |
| SHIP_PROPULSION_LEVEL_PARAMETER | "propulsion_level" | # 附加到舰船基础实体上、用于推进声效的声音参数名称 |
| SHIP_PROPULSION_MODIFICATION_SLOT | "ship_mod_slot_propulsion" | # 舰船实体上推进改装槽位的名称，用于确定舰船的推进等级并相应地设置声音参数 |
### ShipViewer（舰船查看器）

| Define | 默认值 | 开发者注释 |  |
|---|---|---|---|
| AUDIO_DISTANCE_SCALE_FACTOR | 0.6 | # 相机与实体之间的距离会乘以此系数，用于计算监听器的基于距离的音频衰减。该值越低，监听器离注视位置越近 |  |
| CAMERA_PITCH_RANGE | { 20.0 45.0 } | # 单位为度 |  |
| CAMERA_DISTANCE_RANGE | { 15.0 75.0 } |  |  |
| CAMERA_START_LOOK_AT | { 0.0 2.75 0.0 } |  |  |
| CAMERA_START_YAW | -145.0 | # 单位为度 |  |
| CAMERA_START_PITCH | 24.35 | # 单位为度 |  |
| CAMERA_START_DISTANCE | 45.0 |  |  |
| CAMERA_ROTATION_SPEED | 0.001 |  |  |
| CAMERA_ROTATION_DAMPING | 15.0 |  |  |
| CAMERA_ZOOM_SPEED | 2.0 |  |  |
| CAMERA_ZOOM_DAMPING | 12.0 |  |  |
| CAMERA_PAN_SPEED | 0.01 |  |  |
| CAMERA_PAN_RANGE | { 2.5 1.5 2.5 } | # 距离起始偏移量的最大距离 { X, Y, Z } |  |
| CAMERA_RESET_TIME | 0.2 | # 相机回到默认位置所需的时间 |  |
| WATER_ENTITY | "ship_viewer_water_entity" |  |  |
| WATER_ENTITY_SPEED_DEFAULT | 17.0 | # 舰船查看器中水面动画的默认速度，即具有此速度的舰船显示为视觉速度 | 1.0 |
| BATTLE_VIEWPORT_CAMERA_ATTACKER_YAW | -31.0 | # 进攻方视口中相机的偏航角，单位为度 |  |
| BATTLE_VIEWPORT_CAMERA_DEFENDER_YAW | 149.9 | # 防守方视口中相机的偏航角，单位为度 |  |
| BATTLE_VIEWPORT_CAMERA_PITCH | 40.0 | # 两个战斗视口中相机的俯仰角，单位为度 |  |
| BATTLE_VIEWPORT_CAMERA_DISTANCE | 74.0 | # 两个战斗视口中相机到舰船的距离 |  |
| BATTLE_VIEWPORT_CAMERA_ATTACKER_TRANSLATION | { 2.0 0.0 -2.0 } | # 进攻方视口中相机目标的平移量 |  |
| BATTLE_VIEWPORT_CAMERA_DEFENDER_TRANSLATION | { -0.5 0.0 2.5 } | # 防守方视口中相机目标的平移量 |  |

## 00_interfaces

### 透镜（Lenses）

| Define | 默认值 | 开发者注释 |
|---|---|---|
| MAP_MARKER_ZOOM_THRESHHOLD_NEAR | 100 |  |
| MAP_MARKER_ZOOM_THRESHHOLD_FAR | 900 |  |
| MAP_MARKER_ZOOM_THRESHHOLD_MAX | 4000 |  |
| MAP_MARKER_ZOOM_CITIES_ALL_THRESHHOLD | 70 |  |
| MAP_MARKER_ZOOM_CITIES_REGION_CAPITALS_THRESHHOLD | 250 |  |
| MAP_MARKER_ZOOM_CITIES_STATE_CAPITALS_THRESHHOLD | 500 |  |
| MAP_MARKER_HEIGHT_OFFSET | 1.6 | # 将地图标记在 3D 空间中"向上"移动 |
| LINE_HEIGHT_OFFSET | 0.0 | # 可能会以相同的量向上移动线条，目前它们正好贴在地面上 |
| NUM_CONSTRUCTIONS_BEFORE_SUMMARY | 1 |  |
### 趋势

| Define | 默认值 | 开发者注释 |
|---|---|---|
| SMALL_ARROW_RELATIVE_THRESHOLD | 0.001 | # [0..1] 相对变化小于此值时不会显示小箭头 |
| BIG_ARROW_RELATIVE_THRESHOLD | 0.005 | # [0..1] 相对变化小于此值时不会显示大箭头 |

### 存档

| Define | 默认值 | 开发者注释 |
|---|---|---|
| EXIT_SAVE_NAME | "autosave_exit" |  |

### GUI

**注意**：该类别在文件中被拆分为多个小节，而非一个连续的完整小节。

| Define | 默认值 | 开发者注释 |
|---|---|---|
| ANCHORED_TOOLTIP_THRESHOLD | 150 |  |
| TABS | 4 | # UI 中制表符的空格数量 |
| NUM_INDENTS | 3 |  |
| MAX_BREAKDOWN_ITEMS | 10 |  |
| MAX_BREAKDOWN_ITEMS_SHORT_LIST | 5 |  |
| MAX_LENGTH_OF_ENTERED_TEXT | 50 | # 检查有效性时允许的最大文本长度 |
| MAX_CONSTRUCTION_BREAKDOWN_ITEMS | 24 |  |
| MAX_PAGES_IN_PAGED_LIST | 10 |  |
| MAX_CURRENTLY_CONSTRUCTING_ELEMENTS_SHOWN | 10 | # 活跃建造队列元素控件显示的条目数以此数字为上限 |
| TUTORIAL_STEP_INSTRUCTION_BUTTON_ID | "next" |  |
| DISMISS_TOAST_SHORTCUT_ACTION | "dismiss_toast" |  |
| CLOSE_WINDOW_SHORTCUT_ACTION | "close_window" |  |
| CENTER_CAPITAL_SHORTCUT_ACTION | "center_capital" |  |
| LESS_THAN_PERCENTAGE_COLLECT_AS_OTHER | 0.05 | # 在长列表中，占比低于 5% 的条目会归入列表末尾的特殊"其他"条目（目前适用于人口类型和利益集团支持度） |
| CONSTRUCTION_QUEUE_MAX_SHOWN_ELEMENTS | 12 |  |
| MAX_SUBJECTS_SHOWN_IN_TOOLTIP | 5 |  |
| PROMINENT_IG_REQUIRED_MEMBERSHIP | 0.1 | # 要在人口详情中显示为重要利益集团，至少需要这一比例的政治参与人口支持该利益集团 |
| IG_MEMBER_ATTRACTION_SAMPLES | 100 | # 为确定人口被该利益集团吸引的原因，最多采样的支持人口数量（按成员规模排序） |
| MIN_FRACTION_BELOW_EXPECTED_SOL_TO_SHOW | 0.01 |  |
| MIN_FRACTION_WELFARE_TO_SHOW | 0.01 |  |
| LENS_TOOLBAR_ITEM_WIDTH | 100 | # 透镜工具栏中每个条目的宽度 |
| LENS_TOOLBAR_MARGIN_LEFT | 53 | # 侧面板的宽度 |
| SCROLLBAR_WIDTH | 8 | # 滚动条的宽度 |
| LENS_TOOLBAR_MARGIN_RIGHT | 45; | # LENS_TOOLBAR_MARGIN_LEFT - SCROLLBAR_WIDTH |
| RADICALS_LOYALISTS_BREAKDOWN_NUM_ITEMS | 3 | # 激进派/忠诚派的细分数据中显示多少个数字，其余的归为"其他" |
| POP_NEEDS_SUMMARY_ITEMS | 3 | # 人口需求工具提示中，在细分数据上一级显示多少个条目 |
| RADICALS_LOYALISTS_SUMMARY_ITEMS | 2 |  |
| MIN_LOYALTY_CHART_FRACTION | 0.01; | # 低于此值的非零忠诚度比例在忠诚度饼图中仍会以此值显示 |
| STATE_OWNER_PIECHART_ALPHA | 0.5; |  |
| MIN_TRADE_QUANTITY_TO_SHOW | 0.1 | # 向某州/市场出口或进口的数量低于此值时，会被合并计入"额外出口/进口" |
| TREATY_GOODS_ARTICLE_DEFAULT_QUANTITY | 0.25 | # 用于预测商品转让条款的接受度；选中某商品时，数量也会设置为此值（作为最大值的乘数，并受最小值限制） |
| PLACEHOLDER_ICON | "gfx/interface/icons/war_goals/unused/placeholder.dds" |  |
| STRAIT_ACCESS_OPEN_ICON | "gfx/interface/icons/straits_icons/straits_access.dds" |  |
| STRAIT_ACCESS_NO_MILITARY_ICON | "gfx/interface/icons/straits_icons/straits_no_military.dds" |  |
| STRAIT_ACCESS_CLOSED_ICON | "gfx/interface/icons/straits_icons/straits_no_access.dds" |  |
| STRAIT_TOLL_NO_TOLLS_ICON | "gfx/interface/icons/straits_icons/straits_no_tolls.dds" |  |
| STRAIT_TOLL_LOW_ICON | "gfx/interface/budget/budget_set_very_low.dds" |  |
| STRAIT_TOLL_MEDIUM_ICON | "gfx/interface/budget/budget_set_medium.dds" |  |
| STRAIT_TOLL_HIGH_ICON | "gfx/interface/budget/budget_set_very_high.dds" |  |
| STRAIT_ALLOWED_NO_ENEMIES_ICON | "gfx/interface/icons/generic_icons/capitulate.dds" |  |
| STRAIT_ALLOWED_ONLY_ALLIES_ICON | "gfx/interface/icons/lens_toolbar_icons/alliance.dds" |  |
| NO_STARVATION_ICON | "gfx/interface/icons/map_mode_icons/harvest_conditions.dds" |  |
| MILD_STARVATION_ICON | "gfx/interface/icons/famine_icons/mild_starvation.dds" |  |
| SEVERE_STARVATION_ICON | "gfx/interface/icons/famine_icons/severe_starvation.dds" |  |
| # 饥荒饼图所用颜色，饼图包含不同饥荒类型（无、轻度、重度）下的人口比例 |  |  |
| NO_STARVATION_COLOR | { 0.7 0.7 0.7 1 } |  |
| MILD_STARVATION_COLOR | { 0.741 0.404 0.082 1 } | # 橙色 |
| SEVERE_STARVATION_COLOR | { 0.69 0.08 0.06 1 } | # 红色 |
| ALERT_COLOR_GREEN | { 0.54 0.78 0.33 1 } | # 绿色 |
| ALERT_COLOR_YELLOW | { 0.97 0.77 0.33 1 } | # 黄色 |
| ALERT_COLOR_RED | { 0.78 0.25 0.25 1 } | # 红色 |
| MESSAGE_COLOR_GOOD | { 0.54 0.78 0.33 1 } | # 绿色 |
| MESSAGE_COLOR_NEUTRAL | { 1 1 1 1 } | # 黄色 |
| MESSAGE_COLOR_BAD | { 0.78 0.25 0.25 1 } | # 红色 |
| MILITARY_COLOR_YOU | { 0.11 0.46 0.05 1 } | # 绿色 |
| MILITARY_COLOR_ALLY | { 0 0.2 0.5 1 } | # 蓝色 |
| MILITARY_COLOR_ENEMY | { 0.5 0.04 0.02 1 } | # 红色 |
| MILITARY_COLOR_NEUTRAL | { 0.5 0.5 0.5 1 } | # 灰色 |
| NAVAL_MISSION_HIGHLIGHT_FRIENDLY_COLOR | { 0.47 0.88 1.0 1 } | # 蓝色 - 用于高亮显示友方舰队执行海军任务的海域（与 round_highlight_blue 标记高亮相匹配） |
| NAVAL_MISSION_HIGHLIGHT_ENEMY_COLOR | { 1.0 0.30 0.30 1 } | # 红色 - 用于高亮显示敌方舰队执行海军任务的海域 |
| BIG_SWAY | 100 | # AI 在慷慨拉拢时可能获得的分数调整值，用于在外交博弈弹窗中为数字偏好值着色 |
| LIBERTY_DESIRE_TREND_INDICATOR_LIMIT | 0.05 |  |
| BUILDING_CONSIDERED_FULLY_EMPLOYED | 0.95 | # 若建筑的就业率超过 95%，则隐藏其就业条 |
| OUTLINER_ENTRY_DOUBLE_CLICK_TIME | 0.5 | # 将第二次左键点击解释为关闭面板前所需等待的时间（秒）。遗憾的是，该值与用于生成双击事件的操作系统/平台双击设置并不同步，但即使双击时间设置不同，0.5 秒对绝大多数人来说也足够了。 |
| # 这些数值需要与 coat_of_arms/options 中定义的图集相对应 |  |  |
| FLAG_FRAME_WIDTH_LARGE | 384 |  |
| FLAG_FRAME_HEIGHT_LARGE | 256 |  |
| FLAG_FRAME_WIDTH_MEDIUM | 96 |  |
| FLAG_FRAME_HEIGHT_MEDIUM | 64 |  |
| FLAG_FRAME_WIDTH_SMALL | 48 |  |
| FLAG_FRAME_HEIGHT_SMALL | 32 |  |
| FLAG_FRAME_WIDTH_MESH_ATLAS | 192 | # 仅用于网格旗帜（mesh flags）的图集 |
| FLAG_FRAME_HEIGHT_MESH_ATLAS | 128 | # 仅用于网格旗帜（mesh flags）的图集 |
| # 强权集团纹章为正方形 |  |  |
| POWER_BLOC_COA_FRAME_VERY_LARGE | 512 |  |
| POWER_BLOC_COA_FRAME_LARGE | 256 |  |
| POWER_BLOC_COA_FRAME_MEDIUM | 128 |  |
| POWER_BLOC_COA_FRAME_SMALL | 50 |  |
| POWER_BLOC_COA_FRAME_VERY_SMALL | 32 |  |
| TECH_TREE_PRODUCTION_INITIAL_POSITION | { -600 30 } |  |
| TECH_TREE_MILITARY_INITIAL_POSITION | { 150 30 } |  |
| TECH_TREE_SOCIETY_INITIAL_POSITION | { -400 30 } |  |
| TECH_TREE_INITIAL_ZOOM | 0.3 |  |
| TECH_TREE_MAX_UNLOCK_DISPLAY_COUNT | 5 |  |
| TECH_TREE_MODIFIER_UNLOCK_ICON | "gfx/interface/tech_tree/modifiers_generic_icon.dds" |  |
| TECH_TREE_RESEARCH_QUEUE_DISPLAY_COUNT | 5 |  |
| SWAY_OFFER_DEFAULT_ICON | "gfx/interface/icons/sways/obligation.dds" |  |
| SWAY_OFFER_OBLIGATION_ICON | "gfx/interface/icons/sways/obligation.dds" |  |
| SWAY_OFFER_WARGOAL_ICON | "gfx/interface/icons/sways/wargoal.dds" |  |
| SWAY_OFFER_ALLY_ICON | "gfx/interface/icons/sways/call_ally.dds" |  |
| SWAY_OFFER_BECOME_SUBJECT_ICON | "gfx/interface/icons/sways/subject.dds" |  |
| SWAY_OFFER_TRANSFER_SUBJECT_ICON | "gfx/interface/icons/sways/subject.dds" |  |
| SWAY_OFFER_TRANSFER_STATE_ICON | "gfx/interface/icons/sways/state.dds" |  |
| SWAY_OFFER_DIPLOMATIC_PACT_ICON | "gfx/interface/icons/sways/diplomatic_pact.dds" |  |
| DRAG_SENSITIVITY | 0.01 | # 该值以像素/分辨率为单位，即数值为 1 表示整个屏幕的长度 # 数值越大表示在一次点击期间允许更大的移动 |
| MESSAGE_FEED_DELAY | 1 | # 如果存在队列，消息源系统在添加下一条消息前等待的秒数 |
| MESSAGE_FEED_MAX_SHOWN | 10 | # 消息源中同时显示的最大消息数 |
| MESSAGE_FEED_NUMBER_OF_DAYS_SHOWN | 14 | # 通知在消息源中显示的天数，需要低于 DEAD_OBJ_UNDESTROYED_DAYS，以避免出现关于已死亡人物等的通知返回 null_objs 的风险。 |
| MESSAGE_FEED_DELETE_NOTIFICATION_ADVANCE | 0 | # 通知消息被提前标记为待删除的天数，在通知实际删除之前预留时间供消息源动画使用 |
| TOAST_MESSAGE_TIME_SHOWN | 11.0 | # 弹出提示（toast）显示的持续时间（秒）。使用小于 0 的值则需手动关闭。 |
| TOAST_MESSAGE_POST_HOVER_DELAY | 1.0 | # 当消息被鼠标悬停时不会消失，但上述超时计时仍在运行。当鼠标移开且计时已结束时，该消息仍会在屏幕上保留 TOAST_MESSAGE_POST_HOVER_DELAY 秒。 |
| MAP_TOOLTIP_MOUSE_OFFSET | { 20 20 } |  |
| TIME_INTERVAL_BETWEEN_MAP_NOTIFICATIONS | 4.5 | # 当一条通知因与另一条距离过近而被阻挡时的延迟 |
| DISTANCE_BETWEEN_MAP_NOTIFICATIONS | 25 | # 通知之间的最小距离，以避免相互重叠 |
| MAP_NOTIFICATIONS_MAX_ZOOM | 200 | # 显示地图通知的最大相机高度，除非在地图通知数据库中另行指定 |
| JOURNAL_ENTRY_ICON_DEFAULT | "gfx/interface/icons/event_icons/event_default.dds" | # 日志条目（日志和大纲）的默认图标 |
| SITUATION_EVENT_ICON_DEFAULT | "gfx/interface/icons/event_icons/event_default.dds" | # 局势事件（地图标记和大纲）的默认图标 |
| LAND_BATTLE_ICON | "gfx/interface/map_markers/battle_icon.dds" | # 陆地战斗地图标记的图标 |
| NAVAL_BATTLE_ICON | "gfx/interface/map_markers/naval_battle_icon.dds" | # 海上战斗地图标记的图标 |
| SOL_MODIFIER_POSITIVE | "gfx/interface/icons/timed_modifier_icons/modifier_flag_positive.dds" | # 为文化/宗教动态生成的生活水平修正的图标，正面版本 |
| SOL_MODIFIER_NEGATIVE | "gfx/interface/icons/timed_modifier_icons/modifier_flag_negative.dds" | # 为文化/宗教动态生成的生活水平修正的图标，负面版本 |
| NUMBER_OF_POP_PORTRAITS_STATE | 3 | # 从一个州的所有人口中抽样的人口画像数量 |
| NUMBER_OF_POP_PORTRAITS_BUILDING | 3 | # 从一个建筑的所有人口中抽样的人口画像数量 |
| GAME_CONCEPT_ICON_DEFAULT | "gfx/interface/icons/generic_icons/generic_concept_icon.dds" | # 游戏概念的默认图标 |
| # 以下条目决定当地图互动激活时出现的地图列表面板中各选项的排序方式。# 数值越小排在越上面。最小值为 0。多个条目可以拥有相同的排序值 |  |  |
| MAP_LIST_PANEL_INTERACTION_SORT_ORDER_CAN_ACTIVATE | 0 |  |
| MAP_LIST_PANEL_INTERACTION_SORT_ORDER_CAN_ACTIVATE_MORE | 0 |  |
| MAP_LIST_PANEL_INTERACTION_SORT_ORDER_CAN_DEACTIVATE | 1 |  |
| MAP_LIST_PANEL_INTERACTION_SORT_ORDER_CANNOT_ACTIVATE | 2 |  |
| MAP_LIST_PANEL_INTERACTION_SORT_ORDER_CANNOT_DEACTIVATE | 3 |  |
| MAP_LIST_PANEL_INTERACTION_SORT_ORDER_DOES_NOT_APPLY | 4 |  |
| NUM_RANKING_LEADERBOARD_ITEMS | 10 |  |
| POP_LIST_POPS_SHOWN_PER_TYPE | 256 |  |
| NUM_TOP_CONSUMPTION_GOODS_SHOWN | 5 |  |
| NUM_TOP_ASSETS_SHOWN_LONG | 6 |  |
| NUM_TOP_ASSETS_SHOWN_SHORT | 3 |  |
| NUM_TOP_OWNERS_SHOWN_LONG | 8 |  |
| NUM_TOP_OWNERS_SHOWN_SHORT | 5 |  |
| POLITICAL_MOVEMENT_SUPPORTING_AGITATORS_TOP_DATAMODEL_COUNT | 2 |  |
| ARMY_FORMATION_FLAG_COLOR_PREFIX | "army_color_" |  |
| FLEET_FORMATION_FLAG_COLOR_PREFIX | "fleet_color_" |  |
| BUILDING_OWNERSHIP_COLOR_PLAYER_GOVERNMENT | { 0.20 0.40 0.90 1 } |  |
| BUILDING_OWNERSHIP_COLOR_PLAYER_POPS | { 0.41 0.67 0.74 1 } |  |
| BUILDING_OWNERSHIP_COLOR_PLAYER_COMPANY | { 0.41 0.67 0.74 1 } |  |
| BUILDING_OWNERSHIP_COLOR_NON_PLAYER_COMPANY | { 1 0.674 0.454 1 } |  |
| BUILDING_OWNERSHIP_COLOR_LOCAL_NON_PLAYER_GOVERNMENT | { 0.9 0.50 0.2 1 } |  |
| BUILDING_OWNERSHIP_COLOR_LOCAL_NON_PLAYER_POPS | { 1 0.674 0.454 1 } |  |
| BUILDING_OWNERSHIP_COLOR_OTHER_COUNTRIES_GOVERNMENT | { 0.9 0.50 0.2 1 } |  |
| BUILDING_OWNERSHIP_COLOR_OTHER_COUNTRIES_POPS | { 1 0.674 0.454 1 } |  |
| OUTLINER_NUM_VISIBLE_NONEXPANDABLE_SUBENTRIES | 1 | # 父条目未展开时可见的大纲（outliner）条目数量 |
| SOCIETY_PANEL_DESIRED_REPRESENTATIVE_POPS | 3 | # 尝试获取这么多人口（pop）头像（如果只有 1 或 2 类人口则无法做到……） |
| # 用于决定使用对应本地化（localization）键的阈值。若剩余持续时间 >= 设定值，则使用该键 # 低于 VERY_LOW 时使用 LOWEST 键 # VERY_HIGH 设为 999 实际上是作为未使用的阈值，以防将来需要更多分级，但其功能仍然相同 # 数值以天数计 |  |  |
| HARVEST_CONDITION_DURATION_LABEL_VERY_LOW | 60 |  |
| HARVEST_CONDITION_DURATION_LABEL_LOW | 120 |  |
| HARVEST_CONDITION_DURATION_LABEL_MODERATE | 240 |  |
| HARVEST_CONDITION_DURATION_LABEL_HIGH | 480 |  |
| HARVEST_CONDITION_DURATION_LABEL_VERY_HIGH | 999 |  |
| COMPANY_TYPE_ICON_FONT | 230 |  |
| COMPANY_TYPE_ICON_OFFSET | { 0 40 } |  |
| MILITARY_FORMATION_FLAG_ICON_FONT | 95 |  |
| MILITARY_FORMATION_FLAG_ICON_OFFSET | { 0 30 } |  |
| IDEOLOGY_ICON_FONT | 230 |  |
| IDEOLOGY_ICON_OFFSET | { 0 40 } |  |
| ARTICLE_TYPE_ICON_FONT | 90 |  |
| ARTICLE_TYPE_ICON_OFFSET | { 0 20 } |  |
| WAR_GOAL_TYPE_ICON_FONT | 120 |  |
| WAR_GOAL_TYPE_ICON_OFFSET | { 0 32 } |  |
| NAVAL_BATTLE_CONDITION_TYPE_ICON_FONT | 120 |  |
| NAVAL_BATTLE_CONDITION_TYPE_ICON_OFFSET | { 0 64 } |  |
| RELIGION_ICON_FONT | 180 |  |
| RELIGION_ICON_OFFSET | { 0 60 } |  |
| INTEREST_TIER_TYPE_SMALL_ICON_FONT | 50 |  |
| INTEREST_TIER_TYPE_SMALL_ICON_OFFSET | { 0 12 } |  |
| INTEREST_TIER_TYPE_ICON_FONT | 90 |  |
| INTEREST_TIER_TYPE_ICON_OFFSET | { 0 20 } |  |
| AI_STRATEGIC_REGION_STANCE_TYPE_ICON_FONT | 230 |  |
| AI_STRATEGIC_REGION_STANCE_TYPE_ICON_OFFSET | { 0 40 } |  |
| SHIP_VETERANCY_LEVEL_ICON_FONT | 40 |  |
| SHIP_VETERANCY_LEVEL_ICON_OFFSET | { 0 10 } |  |
## 00_shaders

### ShadersCommon

| Define | 默认值 | 开发者注释 |
|---|---|---|
| PARALLAX_HEIGHT | 8 | # 视差效果的高度 |

### MapCoa

| Define | 默认值 | 开发者注释 |
|---|---|---|
| ANGLE | 0.0 | # 纹章在地图上的旋转角度。以弧度为单位 |
| SIZE | 25.0 | # 地图上单个纹章（CoA）的大小。以世界单位计 |
| SIZE_FLATMAP | 50.0 |  |
| BLEND | 0.65f | # 最小混合值。最终混合值为该值与渐变边界所用值中的较小者 |
| BLEND_FLATMAP | 0.8f |  |
| BLEND_STRIPES | 0.8f | # 占领条纹的混合/不透明度 |
| BLEND_STRIPES_FLATMAP | 1.0f |  |
| ROW_HORIZONTAL_OFFSET | 0.25 | # 纹章的每一行都可以水平偏移。此项以百分比控制偏移量 |
| ROW_COUNT | 4 | # 在重新从偏移 0 开始之前，需要偏移的行数 |
| STRIPE_SCALE | 1.0 | # 占领条纹的缩放 |
| STRIPE_SCALE_FLATMAP | 1.0 |  |

### MapmodeStripes

| Define | 默认值 | 开发者注释 |
|---|---|---|
| STRIPE_ROTATION | -2.0 | # 条纹的旋转（严格来说是对 UV 的剪切，因此也会影响宽度） |
| STRIPE_TILING | 120.0 | # 条纹的平铺 |
| STRIPE_WIDTH | 0.2 | # 条纹的宽度 |
| STRIPE_EDGE_WIDTH | 0.075 | # 条纹边缘的宽度 |
| STRIPE_EDGE_COLOR | 0.75 | # 条纹边缘的颜色乘数（1.0 = 与条纹同色，0.0 = 黑色） |
| STRIPE_HEIGHT_STEPS | 1200.0f | # 条纹平铺将从此高度开始，每当地图高度翻倍时平铺减半（避免从低于平面地图高度处开始） |

### EdgeOfWorld

| Define | 默认值 | 开发者注释 |
|---|---|---|
| # 地图上/下边缘的云层 # 有关纸质地图的焦外光斑场，参见着色器文件 |  |  |
| BASETILE | 20.0f |  |
| BASESCROLL | { 0.0055 0.00325 } |  |
| BASESTRENGTH | 1.0f |  |
| BASEPOSITION | 0.728 |  |
| BASECONTRAST | 1.08 |  |
| CLOUD1TILE | 2.0 |  |
| CLOUD1SCROLL | { 0.0015 -0.0015 } |  |
| CLOUD1STRENGTH | 1.0 |  |
| CLOUD1POSITION | 0.538 |  |
| CLOUD1CONTRAST | 1.0 |  |
| CLOUD2TILE | 3.0 |  |
| CLOUD2SCROLL | { -0.0075 0.00055 } |  |
| CLOUD2STRENGTH | 1.0 |  |
| CLOUD2POSITION | 0.158 |  |
| CLOUD2CONTRAST | 1.202 |  |
| HIGHCLOUDCOLOR | { 0.8 0.8 1.0 1.0 } |  |
| LOWCLOUDCOLOR | { 0.03 0.03 0.03 1.0 } |  |
| COLORMULTIPLY | 0.015 |  |
| FADEDISTANCE | 50 |  |

### GuiFlag

| Define | 默认值 | 开发者注释 |
|---|---|---|
| SMALL_WAVE_SCALE | 7.0 |  |
| WAVE_SCALE | 0.95 |  |
| ANIMATION_SPEED | 0.9 |  |
## 参考

Modding
返回顶部
| 文档 | defines • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
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

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|