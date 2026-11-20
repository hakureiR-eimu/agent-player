---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Country modding
source: https://vic3.paradoxwikis.com/Country_modding
pageid: 4805
categories: [Potentially_outdated, 1.10, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。至少有部分内容最后验证于 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10。

国家定义（Country definitions）
**游戏文件夹 存储此类文件的游戏文件夹。 ：** `common/country_definitions`

---

**可注入（Injectable） 能否对此类型使用 INJECT 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **可替换（Replaceable） 能否对此类型使用 REPLACE 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**相关游戏对象：** 国家创建（Country creation）、国家组建（Country formation）

《维多利亚3》中的[国家](Countries.md)由少量基础特性定义，其中大多数可以在游戏中通过脚本或玩家操作进行调整；但基础特性始终保持在脚本中定义的样子。

## 国家定义

国家定义于 /common/country_definitions/；每个国家定义都有必填和可选元素：

| 特性 | 用途 | 示例 | 是否必填？ |
|---|---|---|---|
| TAG | 内部脚本 ID，始终为三个字母，用于创建定义块 | GER | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| color | 基础地图颜色：以 RGB、hsv 或 hsv360 色彩空间表示 | color = { 147 130 110 } | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| country_type | 初始外交类型，定义于 common/country_types | country_type = recognized | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| tier | 威望等级，目前是一个硬编码的[列表](Rank.md) | tier = empire | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| cultures | 主文化，一个或多个 | cultures = { north_german south_german } | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| religion | 国教，若与第一个主文化的默认宗教不同 | religion = protestant | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| capital | 默认首都州，严格来说是可选的 | capital = STATE_BRANDENBURG | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| is_named_from_capital | 为分裂州覆盖通常的州命名机制 | is_named_from_capital = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| valid_as_home_country_for_separatists | 分离主义者能否为该国家叛乱 | valid_as_home_country_for_separatists = { triggers } | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| social_hierarchy | 为该国家设置一个社会等级制度 | social_hierarchy = british_indian_caste_system | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| <order>_unit_color | 设置固定的单位模型颜色（RGB）；`primary、secondary 或 tertiary` | primary_unit_color = { 20 20 120 } | ![No](/images/thumb/0/04/No.png/24px-No.png) |

完整的定义通常类似于以下示例：

```
GER = {
	color = { 147 130 110 }
	
	country_type = recognized

	tier = empire
	
	cultures = { north_german south_german }
	capital = STATE_BRANDENBURG
}
```

补充说明：

- `color` 默认按 rgb 处理，除非设为 hsv 或 hsv360：
  - 因此 `color = { 147 130 110 }` 按 rgb 读取（0-255 取值）
  - 而 `color = hsv{ 0.99 0.7 0.9 }` 使用百分比 HSV
  - `color = hsv360{ 20 80 80 }` 使用 0-360 的色相（Hue）以及 0-100 的饱和度（Saturation）和明度（Value）。
- 可以通过脚本修改的特性——如类型、文化和宗教——如果该国家在游戏过程中消亡，之后又被释放或重新组建，则会重置为定义值。

### 国家组建

国家组建（Country formations）
**游戏文件夹 存储此类文件的游戏文件夹。 ：** `common/country_formation`

---

**可注入（Injectable） 能否对此类型使用 INJECT 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **可替换（Replaceable） 能否对此类型使用 REPLACE 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**相关游戏对象：** 国家创建、国家定义

国家组建——即[统一](Formable countries.md)——定义于 /common/country_formation/。每次组建必须基于一个已存在的国家定义。组建沿两个维度定义：主要（major）与次要（minor），以及文化本土与定义的州列表。

所有组建都需要一个州列表，要么显式定义，要么使用 `use_culture_states = yes`，将该国任一主文化的本土所在的所有州作为其州列表。

| 特性 | 用途 | 示例 | 说明 |
|---|---|---|---|
| TAG | 内部脚本 ID，用于创建定义块 | LAO | 必须匹配已定义的国家 |
| states | 已定义的州列表，一个或多个 | states = { STATE_LAOS } | 不要与 `use_culture_states` 同时使用 |
| use_culture_states | 使用该国所有文化的全部文化本土 | use_culture_states = yes | 不要与 `states` 同时使用 |
| required_states_fraction | 组建所需的州比例 | required_states_fraction = 0.75 | 若省略则默认为 0.75 |
| ai_will_do | AI 决定组建该国家的条件 | ai_will_do = { triggers } | 原版主要使用 `always = yes` |
| possible | 组建的额外要求 | possible = { triggers } | 原版主要使用 `has_technology_researched = (pan-)nationalism` |
| max_num_formation_candidates | 覆盖组建候选者的默认数量 | max_num_formation_candidates = 1 | 默认为 3 |
| can_be_formation_candidate | 成为主要组建候选者的额外要求 | can_be_formation_candidate = { triggers } | 候选者还必须满足 possible 块 |
| can_be_unification_target | 成为统一博弈有效目标的额外要求 | can_be_unification_target = { triggers } |  |

一个使用已定义州列表的示例：

```
LAO = {
	states = {
		STATE_LAOS
	}

	required_states_fraction = 1.0
	
	ai_will_do = { always = yes }
}
```

一个使用 `use_culture_states = yes` 的示例

```
UBD = {
	use_culture_states = yes

	required_states_fraction = 1
	
	ai_will_do = { always = yes }

	possible = {
		has_technology_researched = pan-nationalism
	}
}
```

主要组建通过添加 `is_major_formation = yes` 来声明。主要组建还拥有两个[外交博弈](Diplomacy modding.md) `unification_play` 和 `leadership_play`，它们应与现有的外交博弈相匹配，分别带有 `unification` 和 `unification_leadership` 的战争目标。

一个主要组建的示例：

```
ITA = {
	use_culture_states = yes

	is_major_formation = yes

	unification_play = dp_unify_italy
	leadership_play = dp_leadership_italy

	required_states_fraction = 0.7

	ai_will_do = { has_technology_researched = nationalism }

	possible = {
		OR = {
			country_has_primary_culture = cu:north_italian
			country_has_primary_culture = cu:south_italian
		}
	}
	
	max_num_formation_candidates = 3
	can_be_formation_candidate = {
		country_rank >= rank_value:minor_power
		any_country = {
			filter = {
				OR = {
					country_has_primary_culture = cu:north_italian
					country_has_primary_culture = cu:south_italian
				}
			}
			has_technology_researched = nationalism
			percent = 1
		}
	}
}
```

组建国家只需满足 possible 块，而统一候选者机制则需要同时满足 possible 块和 can_be_formation_candidate 块。

### 国家创建

国家创建（Country creation）
**游戏文件夹 存储此类文件的游戏文件夹。 ：** `common/country_creation`

---

**可注入（Injectable） 能否对此类型使用 INJECT 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **可替换（Replaceable） 能否对此类型使用 REPLACE 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**相关游戏对象：** 国家定义、国家组建

国家创建——即[解放](Releasable countries.md)——定义于 /common/country_creation/。每次创建必须基于一个已存在的国家定义。创建由文化本土、已定义的州列表或已定义的省份列表来定义。注意，国家定义的首都实际上总是包含在所需州或文化州的列表中，即使它没有被显式加入该列表或不是文化本土。

| 特性 | 用途 | 示例 | 说明 |
|---|---|---|---|
| TAG | 内部脚本 ID，用于创建定义块 | JAM | 必须匹配已定义的国家 |
| provinces | 已定义的省份列表，一个或多个 | provinces = { xC08061 x68BE66 } | 不要与 `use_culture_states` 或 `states` 同时使用 省份不必属于同一个州 |
| states | 已定义的州列表，一个或多个 | states = { STATE_JAMAICA } | 不要与 `use_culture_states` 或 `provinces` 同时使用 |
| use_culture_states | 使用该国所有文化的全部文化本土 | use_culture_states = yes | 不要与 `states` 或 `provinces` 同时使用 |
| required_num_states | 释放所需的州数量 | required_num_states = 2 | 若省略则默认为 0（实际上是 1） |
| ai_will_do | AI 决定释放该国家的条件 | ai_will_do = { triggers } | 原版总是使用 `always = no` |
| possible | 释放的额外要求 | possible = { triggers } | 原版主要使用 `has_technology_researched = (pan-)nationalism` |

一个国家释放定义的示例

```
PHI = {
	states = { 
		STATE_MINDANAO
		STATE_LUZON
		STATE_VISAYAS
	}
	required_num_states = 2
	ai_will_do = { always = no }
}
```

## 本地化

动态国家名称
**游戏文件夹 存储此类文件的游戏文件夹。 ：** `common/dynamic_country_names`

---

**可注入（Injectable） 能否对此类型使用 INJECT 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **可替换（Replaceable） 能否对此类型使用 REPLACE 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

国家会根据其 tag 自动生成[localization](Localization.md)（本地化）键：TAG 和 TAG_ADJ，分别定义国家的名称和形容词。

动态名称可以在 common/dynamic_country_names 中定义，其中有一个任何国家都可使用的 `DEFAULT` 块，以及特定于各 tag 的 TAG 块。

```
TAG = {
	dynamic_country_name = {
		name = string # 可以通过使用 TAG 作为字符串来设为默认名称
		adjective = string # 可以通过使用 TAG_ADJ 作为字符串来设为默认形容词

		is_revolutionary = yes # 默认 no，若为 yes 则仅用于叛乱
        
		is_main_tag_only = yes # 默认 no，若为 yes 则只有该定义的主要国家才能使用此名称（即波兰，而非动态叛乱的波兰）
        
		priority = 0 # 默认 0，若有多个名称的 trigger 均有效，则使用优先级较高的。若优先级相同，则使用文件中靠前的
		
		# Scripted trigger, country-scope
		trigger = {
		}
	}	
}
```

## 地图颜色

动态国家颜色
**游戏文件夹 存储此类文件的游戏文件夹。 ：** `common/dynamic_country_map_colors`

---

**可注入（Injectable） 能否对此类型使用 INJECT 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **可替换（Replaceable） 能否对此类型使用 REPLACE 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**相关游戏对象：** 命名颜色

国家的默认地图颜色如上所定义，但动态颜色可以在 common/dynamic_country_map_colors 中编写脚本。将使用第一个返回 true 的动态颜色，除非[游戏规则](Game rule.md)“附属国的地图颜色”开启且该国是一个附属国。

```
kalmar_union = { #这只是一个任意的脚本名称，动态颜色中应保持唯一
	color = "kalmar_orange" # 一个在 common/named_colors 中定义的"命名颜色"

	possible = { # Scripted trigger, country-scope
		exists = c:SCA
		THIS = c:SCA
		has_law = law_type:law_monarchy
		ruler = {
			has_culture = cu:danish
		}
	}
}
```

命名颜色（Named colors）的定义方式与国家的默认颜色相同，声明一个 hsv360 或 rgb 颜色，只是与一个脚本名称绑定。命名颜色可用于动态地图颜色以及旗帜颜色。

## 旗帜

主条目：
旗帜修改（Flag modding）

没有定义旗帜的国家会动态生成旗帜；否则它们使用脚本中定义的旗帜。

### 旗帜颜色与单位模型颜色

游戏中的单位模型的颜色取自国家定义的单位颜色，或当前使用的纹章颜色。

单位模型颜色可以在国家定义中这样定义：

```
    primary_unit_color = { 20 20 120 }
    secondary_unit_color  = { 150 190 210 }
    tertiary_unit_color = { 5 5 90 }
```

否则，为纹章定义的前三个基础/图案颜色将决定单位模型颜色，即使这些颜色并未出现在旗帜上。为徽记定义的颜色永远不会被考虑。

## 国家历史

参见：
历史修改（History modding）

/common/history/countries/ 包含游戏开始时已存在的国家的初始政治设置。这些是 effect 块（游戏内效果脚本），其中若干 effect 被设置为 scripted effect（脚本化效果），用于统一常见的法律和技术组合。

其中一个 effect 块是 `effect_starting_politics_conservative = yes`，它给予以下法律：

| 君主制 | 国家干预 | 限制出版 |
|---|---|---|
| 寡头制 | 重商主义 | 无工人权利 |
| 民族至上 | 人头税 | 允许童工 |
| 国教 | 佃农制 | 法定监护 |
| 任命官僚 | 无殖民事务 | 无社会保障 |
| 职业陆军 | 地方警察部队 | 迁移管制 |
| 无内政事务 | 宗教学校 | 废除奴隶制 |
|  | 无医疗系统 | 结社法案 |

如果某个法律组没有定义法律，那么该组中的“默认”法律在游戏开始时生效。这些通常是在法律文件中第一个编写的法律，除非国家不满足该法律的要求。

**技术**

你可以为一个国家解锁单独一项技术，例如养蚕业（Sericulture），方法是编写 `add_technology_researched = sericulture`。技术层级（technology tier）是一组技术，可以像 `effect_starting_technology_tier_6_tech = yes` 这样用单行代码分配给一个国家，以便于使用。共有 6 个层级，第 5 层包含第 6 层，第 4 层包含第 5 层，第 3 层包含第 4 层，依此类推。下表展示了相邻层级之间的技术差异。最佳做法是为国家分配一个层级，然后以保持科技树连通的方式分配所分配层级不包含的特定技术。

| 生产 | 军事 | 社会 |
|---|---|---|
| 圈地 | 常备军 | 城市化 |

| 生产 | 军事 | 社会 |
|---|---|---|
| 手工工场 竖井开采 | 航海术 军事操练 | 理性主义 官僚体制 |

| 生产 | 军事 | 社会 |
|---|---|---|
| 勘探 炼钢 蒸馏 | 干船坞 海军部 枪械制造 火炮 | 国际贸易 中央集权 国际关系 民主制 |

| 生产 | 军事 | 社会 |
|---|---|---|
| 轧棉机 | 义务兵役 线列步兵 陆军预备役 | 执法 货币标准 殖民 学术界 医学学位 浪漫主义 |

| 生产 | 军事 | 社会 |
|---|---|---|
| 车床 大气式蒸汽机 机械工具 | 明轮船 陆军预备役 拿破仑战术 | 证券交易所 公司特许经营 银行业 平等主义 大众传播 经验主义 辩证法 |

| 生产 | 军事 | 社会 |
|---|---|---|
| 铁路 | 螺旋桨护卫舰 赋税权力 总参谋部 火帽 | 中央银行 中央档案馆 |

这些预设的 scripted effect 可以通过在 scripted effect 调用之后定义其他法律或额外技术来修改。

其他国家的初始状况在其他 history 文件夹中定义，例如外交关系、拥有的州以及人物。

## 国家脚本文档
以下 [effect](Effect.md)、[event target](Event target.md) 和 [trigger](Trigger.md) 可用于 country scope。

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| activate_law | 为国家激活一项法律，不应用 `when_enacted` effect | activate_law = law_type:<law_key> | law_type |
| activate_production_method | 为国家/州中某一类型的建筑激活指定的生产方式 | activate_production_method = { building_type = building_key production_method = production_method_key } |  |
| add_banned_goods | 为国家添加对某种商品的全面禁令 | add_banned_goods = <goods key/scope> | goods |
| add_change_relations_progress | 增加两国之间改变关系的进度 | add_change_relations_progress = { country = country scope/tag value = amount } |  |
| add_company | 将公司类型添加到国家的公司中 | add_company = company_type:key | company_type |
| add_country_monopoly | 向 country scope 添加垄断 | add_country_monopoly = bt:building_textile_mills | building_type |
| add_culture_acceptance_modifier | 在 scope 国家为给定文化应用文化接受度修正。除必需的 culture 参数外，此 effect 语法与 add_modifier 相同 | add_culture_acceptance_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } |  |
| add_enactment_modifier | 为 scope 中的对象添加与立法相关的限时修正效果 | add_enactment_modifier = { name = modifier_key } |  |
| add_enactment_phase | 将 scope 国家当前的法律制定阶段增加指定数值。结果会被限制在 0 与 NPolitics::LAW_ENACTMENT_MAX_PHASES 之间。若结果等于 NPolitics::LAW_ENACTMENT_MAX_PHASES，正在制定的法律将通过 |  |  |
| add_enactment_setback | 将 scope 国家当前的法律制定挫折数增加指定数值。结果会被限制在 0 与 country_law_max_setbacks_add 之间。若结果等于 country_law_max_setbacks_add，法律制定将失败 |  |  |
| add_era_researched | 在 country scope 中将指定时代标记为已研究 | add_era_researched = era |  |
| add_fervor_target_modifier | 在 scope 国家为给定文化应用狂热目标修正。除必需的 culture 参数外，此 effect 语法与 add_modifier 相同 | add_fervor_target_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } |  |
| add_investment_pool | 直接向投资池注入资金 | add_investment_pool = 50 |  |
| add_journal_entry | 将日志条目添加到 scope 国家的日志中，可选保存 scope 目标 | add_journal_entry = { type = <key> target = <scope> } |  |
| add_law_progress | 为当前正在通过的法律的当前检查点增加 x% 进度（范围为 [0, 1]，0.1 表示 10 个百分点） | add_law_progress = 0.1 / -0.1 |  |
| add_liberty_desire | 为附属国增加独立倾向。若 scope 国家不是某项外交条约中的附属国，则无效果 | add_liberty_desire = -5 |  |
| add_loyalists | 为 scope 国家的人口添加忠诚派。除 value 外所有参数均为可选 | value 为每个人口中转向忠诚主义的人口百分比。若指定了 interest_group，则人口根据其所属利益集团获得忠诚派。pop type 与 strata 互斥。add_radicals = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } |  |
| add_modifier | 为 scope 中的对象添加限时修正效果 | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_primary_culture | 将一种文化添加为国家的主要文化 | add_primary_culture = <culture> | culture |
| add_radicals | 为 scope 国家的人口添加激进派。除 value 外所有参数均为可选 | value 为每个人口中转向激进主义的人口百分比。若指定了 interest_group，则人口根据其所属利益集团获得激进派。pop type 与 strata 互斥。add_radicals = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } |  |
| add_taxed_goods | 为国家添加对某种商品的消费税 | add_taxed_goods = <goods key/scope> | goods |
| add_technology_progress | 增加技术进度 | add_technology_progress = { progress = <script_value> technology = <technology key> } |  |
| add_technology_researched | 在 country scope 中研究指定技术 | add_technology_researched = technology |  |
| add_treasury | 为国家增加/扣除资金 | add_treasury = fixed point |  |
| annex | 吞并一个国家 | annex = scope | country |
| annex_as_civil_war | 吞并一个国家，并附带内战中获胜一方的全部继承效果 | annex_as_civil_war = scope | country |
| annex_with_incorporation | 吞并一个国家，继承其各州的整合状态 | annex_with_incorporation = scope | country |
| call_election | 将国家的下一次选举日期设定为 N 个月后 | call_election = { months = 6 } |  |
| cancel_enactment | 停止制定国家当前正在制定的法律 | cancel_enactment = yes |  |
| change_infamy | 更改 scope 国家的恶名 | change_infamy = amount |  |
| change_institution_investment_level | 增加/减少机构的投资等级 | change_institution_investment_level = { institution = institution_police investment = -1 } |  |
| change_relations | 更改两国之间的关系 | change_relations = { country = country scope/tag value = amount } |  |
| change_subject_type | 更改 scope 国家的附属国类型，同时保留当前的独立倾向数值 | change_subject_type = subject_type_dominion |  |
| change_tag | 更改 scope 国家的 tag | c:GBR = { change_tag = FRA } |  |
| change_tension | 更改两国之间的紧张度 | change_tension = { country = country scope/tag value = amount } |  |
| clear_debt | 清除国家贷款 = bool |  |  |
| clear_enactment_modifier | 清除 scope 国家的所有当前法律制定修正 |  |  |
| clear_scaled_debt | 清除相当于目标最大信用额度乘以指定倍数的债务 | clear_scaled_debt = value |  |
| complete_objective_subgoal | 完成一个目标子目标 | complete_objective_subgoal = <key> |  |
| copy_laws | 复制目标国家 scope 的宪法 | 警告：这会中止任何正在进行的立法。copy_laws = scope | country |
| create_bidirectional_truce | 在两国之间创建双向休战 | create_bidirectional_truce = { country = country scope/tag months = integer } |  |
| create_character | 创建一个人物，任何选项都可以省略 | create_character = { name = loc_key or alternatively first_name and last_name separately culture = culture_tag religion = religion scope (if omitted, it's defined by the character's culture religion) female = bool or character scope (gets the same value from the character) noble = bool or character scope (gets the same value from the character) ruler = bool heir = bool historical = bool age = integer, range, or character scope (gets the age from a character) ideology = ideology key or scope interest_group = interest group key or scope template = base template to generate the character from on_created = effect save_scope_as = scope name trait_generation = effect hq = HQ scope or strategic region scope } |  |
| create_diplomatic_catalyst | 创建一个新的外交催化剂 | create_diplomatic_catalyst = { type = catalyst_relations_level_increased arget = <country scope> } |  |
| create_diplomatic_pact | 在两国之间创建外交条约，scope 国家为发起方 | create_diplomatic_pact = { country = country scope/tag first_state = state scope/tag second_state = state scope/tag type = diplomatic action type } |  |
| create_diplomatic_play | 以 scope 对象为发起方创建一场外交博弈。add_initiator_backers、add_target_backers 和 add_war_goal 可以作为直接 effect 包含在内 | create_diplomatic_play = { name = loc_key escalation = integer between 0 and 100 target_country = country scope/tag type = diplomatic play type annex_as_civil_war = yes/no add_initiator_backers = { list of country scopes/tags } add_target_backers = { list of country scopes/tags } add_war_goal = { holder = country scope/tag war_goal = <war goal key> target_state = <state scope> (if required) target_country = <country scope> (if required) target_region = <region scope> (if required) } } |  |
| create_incident | 创建一个产生恶名的外交事件，目标国家为受害方 | create_incident = { country = country scope/tag value = infamy amount } |  |
| create_military_formation | 创建一支军事编队 | create_military_formation = { # Optional name name = name # type defaults to army type = army/fleet hq_region = sr:region_russia # Optional, overrides the automatic supply hub selection supply_hub = s:STATE_MOSCOW # Add as many combat_unit specifications as necessary combat_unit = { type = unit_type:combat_unit_type_irregular_infantry # service_type defaults to regular and conscript is not applicable for fleets service_type = regular/conscript state_region = s:STATE_MOSCOW count = 5 } # mobilization_options are not applicable for fleets mobilization_options = { mobilization_option:mobilization_option_basic_supplies mobilization_option:mobilization_option_truck_transport } } |  |
| create_political_lobby | 创建一个新的政治游说团 | create_political_lobby = { type = lobby_pro_country arget = <country scope> add_interest_group = <ig scope 1> add_interest_group = <ig scope 2> add_interest_group = <ig scope 3> } |  |
| create_political_movement | 在国家中创建指定类型的政治运动，culture/religion 为可选 | create_political_movement = { movement_type = x religion = <scope> (if relevant) culture = <scope> (if relevant) } |  |
| create_power_bloc | 以 scope 对象为领袖创建一个强权集团 | create_power_bloc = { name = loc_key map_color = { R G B } or hsv{ H S V } founding_date = yyyy.mm.dd, optional identity = power bloc identity key principle = power bloc principle key, can be repeated member = country scope, can be repeated } |  |
| create_ship | 在 scope 国家中创建一艘舰船 | create_ship = { type = ship_type:key # Type of ship to create fleet = scope:fleet # Fleet to assign the created ship to save_scope_as = scope_name # If specified, saves the created ship in the given scope name name = loc_key # Optional name for the ship } |  |
| create_unidirectional_truce | 为一个国家创建针对另一国的单向休战 | create_unidirectional_truce = { country = country scope/tag months = integer } |  |
| deactivate_law | 为国家停用一项法律 |  | law_type |
| deactivate_parties | 停用 scope 国家中的政党 | deactivate_parties = yes |  |
| decrease_autonomy | 将国家的附属国类型更改为自治程度更低的一种 | decrease_autonomy = yes |  |
| end_truce | 结束两国之间的任何休战 | end_truce = country_scope | country |
| every_active_law | 遍历国家中所有生效的法律 | every_active_law = { limit = { <triggers> } #optional <effects> } | law |
| every_active_party | 遍历国家中所有活跃的政党 | every_active_party = { limit = { <triggers> } #optional <effects> } | party |
| every_civil_war | 遍历与 scope 国家相关的所有内战 | every_civil_war = { limit = { <triggers> } #optional <effects> } | civil_war |
| every_cobelligerent_in_diplo_play | 遍历 scope 国家在所有外交博弈（包括战争）中的所有共同交战国 | every_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional <effects> } | country |
| every_cobelligerent_in_war | 遍历 scope 国家在所有战争中的所有共同交战国 | every_cobelligerent_in_war = { limit = { <triggers> } #optional <effects> } | country |
| every_company | 遍历国家中所有公司 | every_company = { limit = { <triggers> } #optional <effects> } | company |
| every_country_strategic_region | 遍历包含 scope 国家所拥有的州的全部战略区域 | every_country_strategic_region = { limit = { <triggers> } #optional <effects> } | strategic_region |
| every_diplomatic_catalyst | 遍历国家近期记忆中的所有外交催化剂 | every_diplomatic_catalyst = { limit = { <triggers> } #optional <effects> } | diplomatic_catalyst |
| every_diplomatically_relevant_country | 遍历某个 country scope 的所有外交相关国家 | every_diplomatically_relevant_country = { limit = { <triggers> } #optional <effects> } | country |
| every_direct_subject | 层级中直接位于当前国家之下的任何国家 | every_direct_subject = { limit = { <triggers> } #optional <effects> } | country |
| every_enemy_in_diplo_play | 遍历 scope 国家在所有外交博弈（包括战争）中的所有敌国 | every_enemy_in_diplo_play = { limit = { <triggers> } #optional <effects> } | country |
| every_enemy_in_war | 遍历 scope 国家在所有战争中的所有敌国 | every_enemy_in_war = { limit = { <triggers> } #optional <effects> } | country |
| every_harvest_condition | 遍历影响某个州、地区区域、战略区域或国家的所有收成状况 | every_harvest_condition = { limit = { <triggers> } #optional <effects> } | harvest_condition |
| every_in_hierarchy | 当前层级中的任何国家，包括当前国家 | every_in_hierarchy = { limit = { <triggers> } #optional <effects> } | country |
| every_interest_group | 遍历国家中所有利益集团 | every_interest_group = { limit = { <triggers> } #optional <effects> } | interest_group |
| every_law | 遍历国家中所有法律 | every_law = { limit = { <triggers> } #optional <effects> } | law |
| every_military_formation | 遍历输入 scope 当前存在的所有军事编队 | every_military_formation = { limit = { <triggers> } #optional <effects> } | military_formation |
| every_neighbouring_state | 遍历与当前 scope 相邻的所有州 注意英式拼写 | every_neighbouring_state = { limit = { <triggers> } #optional <effects> } | state |
| every_overlord_or_above | 层级中位于当前国家之上的任何国家 | every_overlord_or_above = { limit = { <triggers> } #optional <effects> } | country |
| every_political_lobby | 遍历国家或利益集团中的所有政治游说团 | every_political_lobby = { limit = { <triggers> } #optional <effects> } | political_lobby |
| every_political_movement | 遍历国家中所有政治运动 | every_political_movement = { limit = { <triggers> } #optional <effects> } | political_movement |
| every_potential_party | 遍历国家中所有潜在政党 | every_potential_party = { limit = { <triggers> } #optional <effects> } | party |
| every_primary_culture | scope 国家或国家定义的主要文化 | every_primary_culture = { limit = { <triggers> } #optional <effects> } | culture |
| every_rival_country | 被 scope 国家视为竞争对手的任何国家 | every_rival_country = { limit = { <triggers> } #optional <effects> } | country |
| every_rivaling_country | 将 scope 国家视为竞争对手的任何国家 | every_rivaling_country = { limit = { <triggers> } #optional <effects> } | country |
| every_scope_admiral | 遍历以下 scope 中的所有海军上将：国家、利益集团或军事编队 | every_scope_admiral = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_ally | 遍历一个国家的所有盟友 | every_scope_ally = { limit = { <triggers> } #optional <effects> } | country |
| every_scope_army | 遍历输入 scope 当前存在的所有陆军 | every_scope_army = { limit = { <triggers> } #optional <effects> } | military_formation |
| every_scope_building | 遍历以下 scope 中的所有建筑：州、国家 | every_scope_building = { limit = { <triggers> } #optional <effects> } | building |
| every_scope_character | 遍历以下 scope 中的所有人物：国家、利益集团或前线 | every_scope_character = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_culture | 遍历 scope 中的所有文化 | every_scope_culture = { limit = { <triggers> } #optional <effects> } | culture |
| every_scope_diplomatic_pact | scope 国家的任何外交条约 | every_scope_diplomatic_pact = { limit = { <triggers> } #optional <effects> } | diplomatic_pact |
| every_scope_fleet | 遍历输入 scope 当前存在的所有舰队 | every_scope_fleet = { limit = { <triggers> } #optional <effects> } | military_formation |
| every_scope_general | 遍历以下 scope 中的所有将军：国家、利益集团、前线或军事编队 | every_scope_general = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_held_interest_marker | 遍历一个国家持有的所有利益标记 | every_scope_held_interest_marker = { limit = { <triggers> } #optional <effects> } | interest_marker |
| every_scope_homeland_state | 遍历作为 scope 文化家园的所有州，或 scope 国家任一主要文化家园的所有州 | every_scope_homeland_state = { limit = { <triggers> } #optional <effects> } | state |
| every_scope_interest_marker | 遍历以下 scope 中的所有利益标记：国家、地区区域、战略区域 | every_scope_interest_marker = { limit = { <triggers> } #optional <effects> } | interest_marker |
| every_scope_politician | 遍历以下 scope 中的所有政客：国家或利益集团 | every_scope_politician = { limit = { <triggers> } #optional <effects> } | character |
| every_scope_pop | 遍历以下 scope 中的所有人口：国家、州、利益集团、文化 | every_scope_pop = { limit = { <triggers> } #optional <effects> } | pop |
| every_scope_ship | 遍历国家或军事编队中的所有舰船 | every_scope_ship = { limit = { <triggers> } #optional <effects> } | ship |
| every_scope_state | 遍历以下 scope 中包括省份在内的所有州：国家、地区区域、战区、前线或海峡 | every_scope_state = { limit = { <triggers> } #optional <effects> } | state |
| every_scope_strait | 遍历在 scope 州或国家境内拥有陆上端点的所有海峡 | every_scope_strait = { limit = { <triggers> } #optional <effects> } | strait |
| every_scope_theater | 遍历一个国家中的所有战区 | every_scope_theater = { limit = { <triggers> } #optional <effects> } | theater |
| every_scope_treaty | 遍历约束 scope 国家的所有生效条约 | every_scope_treaty = { limit = { <triggers> } #optional <effects> } | treaty |
| every_scope_violate_sovereignty_interested_parties | 遍历在 scope 国家主权被侵犯时会表示关切的所有国家 | every_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional <effects> } | country |
| every_scope_violate_sovereignty_wars | 遍历若目标国家被 scope 国家侵犯主权时会引发的所有相关战争 | every_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional <effects> } | war |
| every_scope_war | 遍历与 scope 相关的所有战争 | every_scope_war = { limit = { <triggers> } #optional <effects> } | war |
| every_strategic_objective | 遍历 scope 国家的所有战略目标州 | every_strategic_objective = { limit = { <triggers> } #optional <effects> } | state |
| every_subject_of_subject | 层级中位于直接附属国之下的任何国家 | every_subject_of_subject = { limit = { <triggers> } #optional <effects> } | country |
| every_subject_or_below | 层级中位于当前国家之下的任何国家 | every_subject_or_below = { limit = { <triggers> } #optional <effects> } | country |
| every_valid_mass_migration_culture | 列出 scope 国家中适合大规模迁移的文化 | every_valid_mass_migration_culture = { limit = { <triggers> } #optional <effects> } | culture |
| increase_autonomy | 将国家的附属国类型更改为自治程度更高的一种 | increase_autonomy = yes |  |
| join_power_bloc | scope 国家加入目标 scope 国家的强权集团 | join_power_bloc = c:USA | country |
| kill_population | 杀死 scope 国家人口中一定数量的个体 | 除 percent 外所有参数均为可选。pop type 与 strata 不能同时使用。kill_population = { value = <integer value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } |  |
| kill_population_percent | 杀死 scope 国家人口中的一定百分比 | 除 percent 外所有参数均为可选。pop type 与 strata 不能同时使用。kill_population_percent = { percent = <decimal value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } |  |
| liberate_slaves | 解放国家/州中的所有奴隶 | liberate_slaves = yes |  |
| liberate_slaves_in_incorporated_states | 解放国家已整合州中的所有奴隶 | liberate_slaves_in_incorporated_states = yes |  |
| liberate_slaves_in_unincorporated_states | 解放国家未整合州中的所有奴隶 | liberate_slaves_in_unincorporated_states = yes |  |
| make_independent | 使一个国家独立 | make_independent = bool |  |
| ordered_active_law | 遍历国家中所有生效的法律 | ordered_active_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | law |
| ordered_active_party | 遍历国家中所有活跃的政党 | ordered_active_party = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | party |
| ordered_civil_war | 遍历与 scope 国家相关的所有内战 | ordered_civil_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | civil_war |
| ordered_cobelligerent_in_diplo_play | 遍历 scope 国家在所有外交博弈（包括战争）中的全部共同交战国 | ordered_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_cobelligerent_in_war | 遍历 scope 国家在所有战争中的全部共同交战国 | ordered_cobelligerent_in_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_company | 遍历一个国家的所有公司 | ordered_company = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | company |
| ordered_country_strategic_region | 遍历包含 scope 国家所拥有的州的所有战略区域 | ordered_country_strategic_region = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | strategic_region |
| ordered_diplomatic_catalyst | 遍历一个国家近期记忆中的所有外交催化剂 | ordered_diplomatic_catalyst = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_catalyst |
| ordered_diplomatically_relevant_country | 遍历一个国家 scope 的所有外交相关国家 | ordered_diplomatically_relevant_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_direct_subject | 在层级中直接位于当前国家之下的任何国家 | ordered_direct_subject = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_enemy_in_diplo_play | 遍历 scope 国家在所有外交博弈（包括战争）中的全部敌国 | ordered_enemy_in_diplo_play = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_enemy_in_war | 遍历 scope 国家在所有战争中的全部敌国 | ordered_enemy_in_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成状况 | ordered_harvest_condition = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | harvest_condition |
| ordered_in_hierarchy | 当前层级中的任何国家，包括当前国家自身 | ordered_in_hierarchy = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_interest_group | 遍历一个国家中的所有利益集团 | ordered_interest_group = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | interest_group |
| ordered_law | 遍历一个国家中的所有法律 | ordered_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | law |
| ordered_military_formation | 遍历当前位于输入 scope 的所有军事编队 | ordered_military_formation = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | military_formation |
| ordered_neighbouring_state | 遍历与一个州区域相邻的所有州 | ordered_neighbouring_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_overlord_or_above | 在层级中位于当前国家之上的任何国家 | ordered_overlord_or_above = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_political_lobby | 遍历一个国家或利益集团中的所有政治游说团体 | ordered_political_lobby = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_lobby |
| ordered_political_movement | 遍历一个国家中的所有政治运动 | ordered_political_movement = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_movement |
| ordered_potential_party | 遍历一个国家中所有潜在的政党 | ordered_potential_party = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | party |
| ordered_primary_culture | scope 国家或国家定义的主流文化 | ordered_primary_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | culture |
| ordered_rival_country | 被 scope 中的国家视为竞争对手的任何国家 | ordered_rival_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_rivaling_country | 正在与 scope 中的国家竞争的任何国家 | ordered_rivaling_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_scope_admiral | 遍历以下 scope 中的所有海军上将：国家、利益集团或军事编队 | ordered_scope_admiral = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_ally | 遍历一个国家的所有同盟国 | ordered_scope_ally = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_scope_army | 遍历当前位于输入 scope 的所有陆军 | ordered_scope_army = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | military_formation |
| ordered_scope_building | 遍历以下 scope 中的所有建筑：州、国家 | ordered_scope_building = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | building |
| ordered_scope_character | 遍历以下 scope 中的所有人物：国家、利益集团或前线 | ordered_scope_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_culture | 遍历 scope 中的所有文化 | ordered_scope_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | culture |
| ordered_scope_diplomatic_pact | scope 中的国家的任何外交条约 | ordered_scope_diplomatic_pact = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_pact |
| ordered_scope_fleet | 遍历当前位于输入 scope 的所有舰队 | ordered_scope_fleet = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | military_formation |
| ordered_scope_general | 遍历以下 scope 中的所有将军：国家、利益集团、前线或军事编队 | ordered_scope_general = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_held_interest_marker | 遍历一个国家持有的所有利益标记 | ordered_scope_held_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | interest_marker |
| ordered_scope_homeland_state | 遍历所有作为 scope 文化的本土，或 scope 国家任一主流文化本土的州 | ordered_scope_homeland_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_scope_interest_marker | 遍历以下 scope 中的所有利益标记：国家、州区域、战略区域 | ordered_scope_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | interest_marker |
| ordered_scope_politician | 遍历以下 scope 中的所有政客：国家或利益集团 | ordered_scope_politician = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character |
| ordered_scope_pop | 遍历以下 scope 中的所有人口：国家、州、利益集团、文化 | ordered_scope_pop = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | pop |
| ordered_scope_ship | 遍历一个国家或军事编队中的所有船只 | ordered_scope_ship = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | ship |
| ordered_scope_state | 遍历以下 scope 中包含地区的所有州：国家、州区域、战区、前线或海峡 | ordered_scope_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_scope_strait | 遍历在 scope 州或国家拥有陆地端点的所有海峡 | ordered_scope_strait = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | strait |
| ordered_scope_theater | 遍历一个国家（country）的所有战区（theater）| ordered_scope_theater = { limit = { <triggers> } #可选 order_by = script_value #通过比较确定作用域的排序 position = int #可选，默认 0；从排序中选择作用域，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的作用域数量，若未指定 min 则为 1，若指定则为 inf。 check_range_bounds = no #可选；如果列表小于 min/max 且不希望在日志中记录错误，则使用此项 <effects> } | theater |
| ordered_scope_treaty | 遍历约束作用域国家的生效条约 | ordered_scope_treaty = { limit = { <triggers> } #可选 order_by = script_value #通过比较确定作用域的排序 position = int #可选，默认 0；从排序中选择作用域，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的作用域数量，若未指定 min 则为 1，若指定则为 inf。 check_range_bounds = no #可选；如果列表小于 min/max 且不希望在日志中记录错误，则使用此项 <effects> } | treaty |
| ordered_scope_violate_sovereignty_interested_parties | 遍历在作用域国家的主权被侵犯时会表示关注的所有国家 | ordered_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #可选 order_by = script_value #通过比较确定作用域的排序 position = int #可选，默认 0；从排序中选择作用域，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的作用域数量，若未指定 min 则为 1，若指定则为 inf。 check_range_bounds = no #可选；如果列表小于 min/max 且不希望在日志中记录错误，则使用此项 <effects> } | country |
| ordered_scope_violate_sovereignty_wars | 若目标国家的主权被作用域国家侵犯，遍历所有相关的战争 | ordered_scope_violate_sovereignty_wars = { limit = { <triggers> } #可选 order_by = script_value #通过比较确定作用域的排序 position = int #可选，默认 0；从排序中选择作用域，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的作用域数量，若未指定 min 则为 1，若指定则为 inf。 check_range_bounds = no #可选；如果列表小于 min/max 且不希望在日志中记录错误，则使用此项 <effects> } | war |
| ordered_scope_war | 遍历与作用域相关的所有战争 | ordered_scope_war = { limit = { <triggers> } #可选 order_by = script_value #通过比较确定作用域的排序 position = int #可选，默认 0；从排序中选择作用域，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的作用域数量，若未指定 min 则为 1，若指定则为 inf。 check_range_bounds = no #可选；如果列表小于 min/max 且不希望在日志中记录错误，则使用此项 <effects> } | war |
| ordered_strategic_objective | 遍历作用域国家的所有战略目标（Strategic Objective）州 | ordered_strategic_objective = { limit = { <triggers> } #可选 order_by = script_value #通过比较确定作用域的排序 position = int #可选，默认 0；从排序中选择作用域，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的作用域数量，若未指定 min 则为 1，若指定则为 inf。 check_range_bounds = no #可选；如果列表小于 min/max 且不希望在日志中记录错误，则使用此项 <effects> } | state |
| ordered_subject_of_subject | 层级中直属附属国以下的任何国家 | ordered_subject_of_subject = { limit = { <triggers> } #可选 order_by = script_value #通过比较确定作用域的排序 position = int #可选，默认 0；从排序中选择作用域，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的作用域数量，若未指定 min 则为 1，若指定则为 inf。 check_range_bounds = no #可选；如果列表小于 min/max 且不希望在日志中记录错误，则使用此项 <effects> } | country |
| ordered_subject_or_below | 层级中当前国家以下的任何国家 | ordered_subject_or_below = { limit = { <triggers> } #可选 order_by = script_value #通过比较确定作用域的排序 position = int #可选，默认 0；从排序中选择作用域，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的作用域数量，若未指定 min 则为 1，若指定则为 inf。 check_range_bounds = no #可选；如果列表小于 min/max 且不希望在日志中记录错误，则使用此项 <effects> } | country |
| ordered_valid_mass_migration_culture | 列出作用域国家中适合大规模迁移的文化 | ordered_valid_mass_migration_culture = { limit = { <triggers> } #可选 order_by = script_value #通过比较确定作用域的排序 position = int #可选，默认 0；从排序中选择作用域，从 0 开始索引 min = int #可选，默认 0；设置要返回的“顶部”位置，从 0 开始索引 max = script_value #可选，默认 1/inf；要返回的作用域数量，若未指定 min 则为 1，若指定则为 inf。 check_range_bounds = no #可选；如果列表小于 min/max 且不希望在日志中记录错误，则使用此项 <effects> } | culture |
| play_as | 更改作用域国家的玩家将扮演的国家 | play_as = <scope> | country |
| random_active_law | 遍历一个国家的所有生效法律 | random_active_law = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | law |
| random_active_party | 遍历一个国家的所有活跃政党 | random_active_party = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | party |
| random_civil_war | 遍历与作用域国家相关的所有内战 | random_civil_war = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | civil_war |
| random_cobelligerent_in_diplo_play | 遍历作用域国家在所有外交博弈（包括战争）中的所有共同交战国 | random_cobelligerent_in_diplo_play = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | country |
| random_cobelligerent_in_war | 遍历作用域国家在所有战争中的所有共同交战国 | random_cobelligerent_in_war = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | country |
| random_company | 遍历一个国家的所有公司 | random_company = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | company |
| random_country_strategic_region | 遍历包含作用域国家所拥有的州的所有战略区域 | random_country_strategic_region = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | strategic_region |
| random_diplomatic_catalyst | 遍历一个国家近期记忆中的所有外交催化剂 | random_diplomatic_catalyst = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | diplomatic_catalyst |
| random_diplomatically_relevant_country | 遍历一个国家作用域的所有外交相关国家 | random_diplomatically_relevant_country = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | country |
| random_direct_subject | 层级中直接位于当前国家之下的任何国家 | random_direct_subject = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | country |
| random_enemy_in_diplo_play | 遍历作用域国家在所有外交博弈（包括战争）中的所有敌国 | random_enemy_in_diplo_play = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | country |
| random_enemy_in_war | 遍历作用域国家在所有战争中的所有敌国 | random_enemy_in_war = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | country |
| random_harvest_condition | 遍历影响一个州、地区（state region）、战略区域或国家的所有收成状况 | random_harvest_condition = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | harvest_condition |
| random_in_hierarchy | 当前层级中的任何国家，包括当前国家 | random_in_hierarchy = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | country |
| random_interest_group | 遍历一个国家的所有利益集团 | random_interest_group = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | interest_group |
| random_law | 遍历一个国家的所有法律 | random_law = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | law |
| random_military_formation | 遍历当前存在于输入作用域的所有军事编队 | random_military_formation = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | military_formation |
| random_neighbouring_state | 遍历与一个地区（state region）相邻的所有州 | random_neighbouring_state = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | state |
| random_overlord_or_above | 层级中当前国家之上的任何国家 | random_overlord_or_above = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | country |
| random_political_lobby | 遍历一个国家或利益集团中的所有政治游说团 | random_political_lobby = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | political_lobby |
| random_political_movement | 遍历一个国家的所有政治运动 | random_political_movement = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | political_movement |
| random_potential_party | 遍历一个国家的所有潜在政党 | random_potential_party = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | party |
| random_primary_culture | 作用域国家或国家定义的主要文化 | random_primary_culture = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | culture |
| random_rival_country | 任何与作用域国家处于竞争关系的国家 | random_rival_country = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | country |
| random_rivaling_country | 任何正在竞争作用域国家的国家 | random_rivaling_country = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | country |
| random_scope_admiral | 遍历以下作用域中的所有海军上将：国家、利益集团或军事编队 | random_scope_admiral = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | character |
| random_scope_ally | 遍历一个国家的所有盟友 | random_scope_ally = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | country |
| random_scope_army | 遍历当前存在于输入作用域的所有陆军 | random_scope_army = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | military_formation |
| random_scope_building | 遍历以下作用域中的所有建筑：州、国家 | random_scope_building = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | building |
| random_scope_character | 遍历以下作用域中的所有人物：国家、利益集团或前线 | random_scope_character = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | character |
| random_scope_culture | 遍历作用域中的所有文化 | random_scope_culture = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | culture |
| random_scope_diplomatic_pact | 作用域国家的任何外交协议 | random_scope_diplomatic_pact = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | diplomatic_pact |
| random_scope_fleet | 遍历当前存在于输入作用域的所有舰队 | random_scope_fleet = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | military_formation |
| random_scope_general | 遍历以下作用域中的所有将军：国家、利益集团、前线或军事编队 | random_scope_general = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | character |
| random_scope_held_interest_marker | 遍历一个国家持有的所有利益标记 | random_scope_held_interest_marker = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | interest_marker |
| random_scope_homeland_state | 遍历作为作用域文化家园的所有州，或作用域国家任何主要文化家园的所有州 | random_scope_homeland_state = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | state |
| random_scope_interest_marker | 遍历以下作用域中的所有利益标记：国家、地区（state_region）、战略区域 | random_scope_interest_marker = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | interest_marker |
| random_scope_politician | 遍历以下作用域中的所有政治家：国家或利益集团 | random_scope_politician = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | character |
| random_scope_pop | 遍历以下作用域中的所有人口：国家、州、利益集团、文化 | random_scope_pop = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | pop |
| random_scope_ship | 遍历一个国家或军事编队中的所有舰船 | random_scope_ship = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | ship |
| random_scope_state | 遍历以下作用域中包括省份在内的所有州：国家、地区（state_region）、战区、前线或海峡 | random_scope_state = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | state |
| random_scope_strait | 遍历在作用域州或国家拥有陆地端点的所有海峡 | random_scope_strait = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | strait |
| random_scope_theater | 遍历一个国家的所有战区 | random_scope_theater = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | theater |
| random_scope_treaty | 遍历约束作用域国家的生效条约 | random_scope_treaty = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | treaty |
| random_scope_violate_sovereignty_interested_parties | 遍历在作用域国家的主权被侵犯时会表示关注的所有国家 | random_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | country |
| random_scope_violate_sovereignty_wars | 若目标国家的主权被作用域国家侵犯，遍历所有相关的战争 | random_scope_violate_sovereignty_wars = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | war |
| random_scope_war | 遍历与作用域相关的所有战争 | random_scope_war = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | war |
| random_strategic_objective | 遍历作用域国家的所有战略目标州 | random_strategic_objective = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | state |
| random_subject_of_subject | 层级中直属附属国以下的任何国家 | random_subject_of_subject = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | country |
| random_subject_or_below | 层级中当前国家以下的任何国家 | random_subject_or_below = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | country |
| random_valid_mass_migration_culture | 列出作用域国家中适合大规模迁移的文化 | random_valid_mass_migration_culture = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | culture |
| recalculate_pop_ig_support | 重新计算并更新一个国家的人口利益集团成员身份 = bool |  |  |
| regime_change | 由作用域国家对目标国家执行政权更迭。| regime_change = scope:upstart_country | country |
| remove_active_objective_subgoal | 移除一个活跃的目标子目标 | remove_active_objective_subgoal = <key> |  |
| remove_banned_goods | 移除一个国家对某商品的全面禁令 | remove_banned_goods = <goods key/scope> | goods |
| remove_company | 从一个国家的公司中移除指定类型的公司 | remove_company = company_type:key | company_type |
| remove_diplomatic_pact | 移除两个国家之间的外交协议，作用域国家为发起方 | remove_diplomatic_pact = { country = country scope/tag type = diplomatic action type } |  |
| remove_enactment_modifier | 移除作用域对象上与立法相关的定时修正效果 |  |  |
| remove_modifier | 移除作用域对象上的定时修正效果 | remove_modifier = static_modifier_name |  |
| remove_monopoly | 在一个国家作用域中移除特定建筑的垄断 | remove_monopoly = bt:building_textile_mills | building_type |
| remove_primary_culture | 从一个国家的主要文化中移除一种文化 | remove_primary_culture = <culture> | culture |
| remove_taxed_goods | 移除一个国家对某商品的消费税 | remove_taxed_goods = <goods key/scope> | goods |
| seize_investment_pool | 将投资池收归国库，并将所有私人建设队列中的项目转移到政府队列 = bool |  |  |
| set_capital | 在一个国家作用域中设置首都所在州 | set_capital = <state_region key> |  |
| set_country_type | 设置一个国家的国家类型，用于历史文件 |  |  |
| set_diplomats_expelled | 在作用域国家中驱逐目标国家的外交官 | set_diplomats_expelled = scope:target_country | country |
| set_export_tariff_level | 设置作用域国家某商品的出口关税等级 | set_export_tariff_level = { goods = g:iron level = max_tariffs } |  |
| set_government_wage_level | 设置作用域国家的政府工资等级 | set_government_wage_level = very_low/low/medium/high/very_high |  |
| set_heir | 将作用域国家的继承人设置为指定的人物作用域 | set_heir = scope_victoria | character |
| set_immune_to_revolutions | 使一个国家免受革命影响或移除此种免疫。| set_immune_to_revolutions = yes/no |  |
| set_import_tariff_level | 设置作用域国家某商品的进口关税等级 | set_import_tariff_level = { goods = g:iron level = max_tariffs } |  |
| set_institution_investment_level | 设置一个机构的投入等级 | set_institution_investment_level = { institution = <key> level = x } |  |
| set_market_capital | 在一个国家作用域中设置市场首都 | set_market_capital = <state_region key> |  |
| set_military_wage_level | 设置作用域国家的军队工资等级 | set_military_wage_level = very_low/low/medium/high/very_high |  |
| set_mutual_secret_goal | 为作用域国家和目标国家设置相互的秘密 AI 目标 | set_mutual_secret_goal = { country = country scope/tag secret_goal = secret goal type } |  |
| set_next_election_date | 设置一个国家的下一次选举日期 | set_next_election_date = year.month.day |  |
| set_only_legal_party_from_ig | 设置一个国家中唯一合法的政党，用于一党制国家法律。| set_only_legal_party_from_ig = ruler.interest_group | interest_group |
| set_owes_obligation_to | 设置一个国家是否对另一个国家负有义务 | set_owes_obligation = { country = country scope/tag setting = yes/no } |  |
| set_relations | 设置两个国家之间的关系 | set_relations = { country = country scope/tag value = amount } |  |
| set_ruling_interest_groups | 从一组利益集团中为作用域国家组建政府 | set_ruling_interest_groups = { ig_tag1 ig_tag2 } |  |
| set_secret_goal | 为作用域国家设置针对另一个国家的秘密 AI 目标 | set_secret_goal = { country = country scope/tag secret_goal = secret goal type } |  |
| set_social_hierarchy | 设置作用域国家的社会等级制 | set_social_hierarchy = <key> |  |
| set_state_religion | 将该国的国教更改为指定宗教 | set_state_religion = <religion_scope | religion |
| set_strategy | 为作用域国家设置 AI 战略 | set_strategy = <key> |  |
| set_tax_level | 设置作用域国家的总体税收等级 | set_tax_level = very_low/low/medium/high/very_high |  |
| set_tension | 设置两个国家之间的紧张度 | set_tension = { country = country scope/tag value = amount } |  |
| start_enactment | 开始为作用域国家制定指定的法律类型 | start_enactment = law_type:law_multicultural | law_type |
| start_national_awakening | 开始一场文化觉醒 | start_national_awakening = { culture = cu:british # 将发生民族觉醒的文化 months = 12 # 觉醒持续的月数 state_region = s:STATE_HOME_COUNTIES # 可选，若未指定则使用该文化识字率最高的地区 } |  |
| start_research_random_technology | 作用域国家开始研究其可研究的任意随机技术 | start_research_random_technology = yes |  |
| take_on_scaled_debt | 转移相当于目标国家最大信贷额度乘以指定乘数的债务 | take_on_scaled_debt = { who = <country scope> value = <0-1 value> } |  |
| try_form_government_with | 尝试以提供的利益集团组建新政府，若无法达到指定的合法性，则尽可能多地将利益集团纳入政府 | try_form_government_with = { value = 30 interest_group_type = ig_armed_forces interest_group_type = ig_devout interest_group_type = ig_landowners } |  |
| unset_only_legal_party | 使该国回到非一党制国家状态，在其它法律允许的情况下可存在多个政党 | unset_only_legal_party = yes |  |
| update_party_support | 更新作用域国家的政党支持度。| update_party_support = yes |  |
| validate_subsidies | 验证一个国家所有建筑的补贴。原版游戏无使用 | validate_subsidies = bool |  |
| violate_sovereignty_join | 作用域国家加入战争，支持侵犯方或目标方 | violate_sovereignty_accept = { violator = <country scope> target = <country scope> join_violator = yes/no } |  |
| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| additional_war_exhaustion | 比较作用域国家从目标外交博弈中的脚本事件累积的额外战争厌倦度 | additional_war_exhaustion = { target = scope:war.diplomatic_play value > 1.0 } | value |
| aggressive_diplomatic_plays_permitted | 若国家独立或被允许发起自己的外交博弈则为真 | aggressive_diplomatic_plays_permitted = bool | boolean |
| ai_ship_value | AI 对一艘舰船的估值（以英镑计），等于当前模板版本的建造成本乘以 NAI::SHIP_TRANSFER_BASE_VALUE_PER_CONSTRUCTION_POINT | ai_ship_value >= 5000 | value |
| any_active_law | 遍历一个国家所有现行法律 | any_active_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | law |
| any_active_party | 遍历一个国家所有现行政党 | any_active_party = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | party |
| any_civil_war | 遍历与作用域国家相关的所有内战 | any_civil_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | civil_war |
| any_cobelligerent_in_diplo_play | 遍历作用域国家在所有外交博弈（包括战争）中的所有共同交战国 | any_cobelligerent_in_diplo_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_cobelligerent_in_war | 遍历作用域国家在所有战争中的所有共同交战国 | any_cobelligerent_in_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_company | 遍历一个国家的所有公司 | any_company = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | company |
| any_country_strategic_region | 遍历包含作用域国家所拥有州的所有战略区域 | any_country_strategic_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | strategic_region |
| any_diplomatic_catalyst | 遍历一个国家近期记忆中的所有外交催化剂 | any_diplomatic_catalyst = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_catalyst |
| any_diplomatically_relevant_country | 遍历一个国家作用域的所有外交相关国家 | any_diplomatically_relevant_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_direct_subject | 层级中直接位于当前国家之下的任何国家 | any_direct_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_enemy_in_diplo_play | 遍历作用域国家在所有外交博弈（包括战争）中的所有敌国 | any_enemy_in_diplo_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_enemy_in_war | 遍历作用域国家在所有战争中的所有敌国 | any_enemy_in_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成状况 | any_harvest_condition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | harvest_condition |
| any_in_hierarchy | 当前层级中的任何国家，包括当前国家本身 | any_in_hierarchy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_interest_group | 遍历一个国家的所有利益集团 | any_interest_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | interest_group |
| any_law | 遍历一个国家的所有法律 | any_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | law |
| any_military_formation | 遍历当前存在于输入作用域中的所有军事编队 | any_military_formation = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | military_formation |
| any_neighbouring_state | 遍历与一个州区域相邻的所有州 | any_neighbouring_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| any_overlord_or_above | 层级中位于当前国家之上的任何国家 | any_overlord_or_above = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_political_lobby | 遍历一个国家或利益集团中的所有政治游说团 | any_political_lobby = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_lobby |
| any_political_movement | 遍历一个国家的所有政治运动 | any_political_movement = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_movement |
| any_potential_party | 遍历一个国家所有潜在的政党 | any_potential_party = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | party |
| any_primary_culture | 作用域国家或国家定义的主流文化 | any_primary_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | culture |
| any_rival_country | 被作用域国家视为宿敌的任何国家 | any_rival_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_rivaling_country | 视作用域国家为宿敌的任何国家 | any_rivaling_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_scope_admiral | 遍历以下作用域中的所有海军上将：国家、利益集团或军事编队 | any_scope_admiral = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_ally | 遍历一个国家的所有盟友 | any_scope_ally = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_scope_army | 遍历当前存在于输入作用域中的所有陆军 | any_scope_army = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | military_formation |
| any_scope_building | 遍历以下作用域中的所有建筑：州、国家 | any_scope_building = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | building |
| any_scope_character | 遍历以下作用域中的所有人物：国家、利益集团或前线 | any_scope_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_culture | 遍历作用域中的所有文化 | any_scope_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | culture |
| any_scope_diplomatic_pact | 作用域国家的任何外交条约 | any_scope_diplomatic_pact = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_pact |
| any_scope_fleet | 遍历当前存在于输入作用域中的所有舰队 | any_scope_fleet = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | military_formation |
| any_scope_general | 遍历以下作用域中的所有将军：国家、利益集团、前线或军事编队 | any_scope_general = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_held_interest_marker | 遍历一个国家持有的所有利益标记 | any_scope_held_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | interest_marker |
| any_scope_homeland_state | 遍历作为作用域文化家园的所有州，或作用域国家任一主流文化家园的所有州 | any_scope_homeland_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| any_scope_interest_marker | 遍历以下作用域中的所有利益标记：国家、战略区域 | any_scope_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | interest_marker |
| any_scope_politician | 遍历以下作用域中的所有政客：国家或利益集团 | any_scope_politician = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character |
| any_scope_pop | 遍历以下作用域中的所有人口：国家、州、利益集团、文化 | any_scope_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | pop |
| any_scope_ship | 遍历一个国家或军事编队中的所有舰船 | any_scope_ship = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | ship |
| any_scope_state | 遍历以下作用域中包括地区的所有州：国家、州区域、战区、前线或海峡 | any_scope_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| any_scope_strait | 遍历在作用域州或国家拥有陆地端点的所有海峡 | any_scope_strait = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | strait |
| any_scope_theater | 遍历一个国家的所有战区 | any_scope_theater = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | theater |
| any_scope_treaty | 遍历约束作用域国家的所有生效条约 | any_scope_treaty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty |
| any_scope_violate_sovereignty_interested_parties | 遍历在作用域国家主权被侵犯时会表示关注的所有国家 | any_scope_violate_sovereignty_interested_parties = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_scope_violate_sovereignty_wars | 遍历若目标国家被作用域国家侵犯主权时会产生的所有相关战争 | any_scope_violate_sovereignty_wars = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | war |
| any_scope_war | 遍历与作用域相关的所有战争 | any_scope_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | war |
| any_strategic_objective | 遍历作用域国家的所有战略目标州 | any_strategic_objective = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| any_subject_of_subject | 层级中位于直属附属国之下的任何国家 | any_subject_of_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_subject_or_below | 层级中位于当前国家之下的任何国家 | any_subject_or_below = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_valid_mass_migration_culture | 列出作用域国家中适合大规模迁移的文化 | any_valid_mass_migration_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | culture |
| approaching_bureaucracy_shortage | 检查国家的机构是否最终会出现行政力短缺 |  | boolean |
| arable_land_country | 比较*所有*州的可耕地面积 | arable_land_country > 10 | value |
| army_mobilization_option_fraction | 检查一个国家的陆军是否有特定比例的单位使用了特定动员选项 | scope:country = { army_mobilization_option_fraction = { target = mobilization_option:key value >= 0.2 } } | value |
| army_power_projection | 与一个国家的陆军总力量投射比较 | scope:example_country = { army_power_projection < root.army_power_projection } | value |
| authority | 比较作用域国家的可用权威力 |  | value |
| authority_usage | 比较作用域国家已消耗的权威力 |  | value |
| average_country_infrastructure | 检查作用域国家所拥有所有州的平均基础设施 | average_country_infrastructure = 3 | value |
| average_incorporated_country_infrastructure | 检查作用域国家所拥有已整合州的平均基础设施 | average_incorporated_country_infrastructure = 3 | value |
| average_sol_for_culture | 比较目标文化在该国的平均生活水平 | average_sol_for_culture = { target = cu:polish value > 10 } | value |
| average_sol_for_primary_cultures | 比较主流文化的平均生活水平 |  | value |
| average_sol_for_religion | 比较目标宗教在该国的平均生活水平 | average_sol_for_religion = { target = rel:catholic value > 10 } | value |
| average_sol_for_slaves | 比较被奴役人口的平均生活水平 |  | value |
| bureaucracy | 比较作用域国家的可用行政力 |  | value |
| bureaucracy_usage | 比较作用域国家已消耗的行政力 |  | value |
| can_afford_diplomatic_action | 检查作用域国家是否能承担指定外交行动（条约或持续性行动）所需的影响力 | can_afford_diplomatic_action = { target = <country scope> type = <diplomatic action key> } |  |
| can_break_diplomatic_pact | 检查与目标国家是否存在指定类型且可被作用域国家废除的外交条约 | can_break_diplomatic_pact = { target = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> } |  |
| can_create_diplomatic_pact | 检查与另一个国家建立某种外交条约是否有效 | can_create_diplomatic_pact = { target = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> } |  |
| can_decrease_autonomy | 检查一个附属国是否能成为自主性更低的附属国类型 | can_increase_autonomy = yes | boolean |
| can_establish_company | 检查该国能否建立一家新公司 |  | boolean |
| can_form_nation | 检查目标国家是否有可能成立某个民族国家 | can_form_nation = <tag> |  |
| can_have_as_subject | 检查一个国家能否将另一个国家作为特定类型的附属国 | can_have_as_subject = { who = <country scope> type = <subject type key> } |  |
| can_have_subjects | 检查该国能否拥有自己的附属国 |  | boolean |
| can_increase_autonomy | 检查一个附属国是否能成为自主性更高的附属国类型 | can_increase_autonomy = yes | boolean |
| can_leave_power_bloc | 检查作用域国家能否离开当前强权集团（若国家不在强权集团中则返回假） | can_leave_power_bloc = yes | boolean |
| can_lobbies_target | 检查目标国家是否是作用域国家游说团的有效目标 | can_lobbies_target = <target country scope> | country |
| can_own_autonomy_be_decreased | 检查作用域国家的自主性能否被降低 | can_own_autonomy_be_decreased = yes/no | boolean |
| can_research | 若国家能研究某项技术则为真 | can_research = technology |  |
| can_send_diplomatic_action | 检查作用域国家向目标国家发送某项外交行动是否有效 | can_send_diplomatic_action = { target = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> } |  |
| can_take_on_scaled_debt | 检查作用域国家能否从另一个国家承担一定数量的比例债务 | can_take_on_scaled_debt = { who = <country scope> value = <0-1 value> } |  |
| can_trigger_event | 检查国家能否触发指定事件 | can_trigger_event = key |  |
| check_area | 将对象的面积与另一个对象比较 |  |  |
| construction_queue_duration | 比较所有队列中完成建造所需的极粗略估计剩余周数的最大值 | construction_queue_duration < 52 | value |
| construction_queue_government_duration | 比较政府队列中完成建造所需的极粗略估计剩余周数 | construction_queue_government_duration < 52 | value |
| construction_queue_num_queued_government_levels | 比较建造队列中政府建造的建筑等级数量 |  | value |
| construction_queue_num_queued_levels | 比较建造队列中的建筑等级数量 |  | value |
| construction_queue_num_queued_private_levels | 比较建造队列中私人建造的建筑等级数量 |  | value |
| construction_queue_private_duration | 比较私人队列中完成建造所需的极粗略估计剩余周数 | construction_queue_private_duration < 52 | value |
| country_army_unit_type_fraction | 检查一个国家是否有特定比例的某种陆军单位类型 | scope:example_formation = { country_military_unit_type_fraction = { target = unit_type:key value >= 0.2 } } | value |
| country_average_cultural_acceptance | 将一个国家中某文化的平均接受度与一个数值比较 | country_average_cultural_acceptance = { target = cu:french value >= 50 } | value |
| country_average_religious_acceptance | 将一个国家中某宗教的平均接受度与一个数值比较 | country_average_religious_acceptance = { target = rel:catholic value >= 50 } | value |
| country_can_have_mass_migration_to | 检查作用域国家能否向目标国家进行大规模迁移 | can_have_mass_migration_to = c:country | country |
| country_fervor_primary_culture | 与一个国家主流文化的最高狂热度比较 | country_fervor_primary_culture > 0.2 | value |
| country_has_building_group_levels | 检查一个国家中某建筑群组的建筑等级总和 | country_has_building_group_levels = { type = bg_heavy_industry value >= 100 } | value |
| country_has_building_levels | 检查一个国家的建筑等级总和 | country_has_building_levels >= 10 | value |
| country_has_building_type_levels | 检查一个国家中某建筑类型的建筑等级总和 | country_has_building_type_levels = { target = bt:building_barracks value >= 100 } | value |
| country_has_building_type_monopoly | 检查作用域国家是否垄断了指定的建筑类型 | country_has_building_type_monopoly = bt:building_food_industry | building_type |
| country_has_country_monopoly | 检查作用域国家是否拥有任何国家垄断 |  | boolean |
| country_has_primary_culture | 检查某文化是否是该国家的主流文化之一 | country_has_primary_culture = <culture> | culture |
| country_has_state_religion | 检查某宗教是否是该国家的国教 | country_has_accepted_religion = <religion> | religion |
| country_innovation | 检查一个国家每周产生的创新数量 | country_innovation <= 200 | value |
| country_or_subject_owns_entire_state_region | 检查作用域国家或其任一附属国是否拥有整个指定的州区域 | country_or_subject_owns_entire_state_region = key |  |
| country_rank | 比较一个国家的强权等级 | country_rank < rank_value:major_power | value |
| country_ship_type_fraction | 检查一个国家是否有特定比例的某种舰船类型 | scope:example_formation = { country_ship_type_fraction = { target = unit_type:key value >= 0.2 } } | value |
| country_tier | 比较国家标签的层级 | country_tier = x |  |
| country_turmoil | 比较该国按人口加权的动荡程度 | country_turmoil > 0.2 | value |
| cultural_acceptance_base | 将作用域国家中某文化因共享文化特质而获得的接受度与一个接受度数值比较 | cultural_acceptance_base = { target = cu:french value > 50 } | value |
| culture_percent_country | 检查一个国家的人口中是否含有特定比例的某种文化 | scope:example_country = { culture_percent_country = { target = cu:dixie value >= 0.2 } } | value |
| discriminates_religion | 检查作用域国家是否歧视给定的宗教（键） | discriminates_religion = <religion key/scope> | religion |
| economic_dependence | 比较作用域国家对目标国家的依赖程度。**注意：这是一个开销较大的 trigger** | economic_dependence = { target = scope:other_country value > 2.2 } | value |
| empty_agitator_slots | 检查一个国家空的鼓动家槽位数量 | empty_agitator_slots >= 1 | value |
| enacting_any_law | 检查该国是否正在制定任何法律。 | enacting_any_law = bool | boolean |
| enactment_chance | 比较作用域国家当前的立法通过几率，包括来自立法修正值的数值 |  | value |
| enactment_chance_for_law | 比较作用域国家针对给定法律当前的立法通过几率，包括来自立法修正值的数值 | enactment_chance_for_law = { target = scope:my_lawtype value > 0.2 } | value |
| enactment_chance_for_law_without_enactment_modifier | 比较作用域国家针对给定法律当前的立法通过几率，不包括来自立法修正值的数值 | enactment_chance_for_law_without_enactment_modifier = { target = scope:my_lawtype value > 0.2 } | value |
| enactment_chance_without_enactment_modifier | 比较作用域国家当前的立法通过几率，不包括来自立法修正值的数值 |  | value |
| enactment_phase | 比较作用域国家当前的立法阶段。 |  | value |
| enactment_setback_count | 比较作用域国家当前的立法受挫次数。 |  | value |
| enemy_contested_wargoals | 判定战争中敌方目前正在争夺的战争目标的比例 | enemy_contested_wargoals = { target = scope:war value > 0.4 } | value |
| enemy_occupation | 判定一个国家的（加权）敌方占领分数 | enemy_occupation > 0.2 | value |
| expanding_institution | 检查机构是否正在扩张 | expanding_institution = <scope/key> |  |
| gdp_ownership_ratio | 比较指定国家在作用域国家拥有的 GDP 比例 | gdp_ownership_ratio = { target = scope:owner_country value > 0.1 } | value |
| gdp_per_capita_ranking | 比较一个国家的人均 GDP 排名（位次） | gdp_per_capita_ranking > 42 | value |
| global_country_ranking | 比较一个国家的强权排名（位次） | global_country_ranking > 42 | value |
| gold_reserves | 该国是否拥有所需数量的黄金储备 | gold_reserves > 500 | value |
| gold_reserves_limit | 比较该国的黄金储备上限 | gold_reserves > gold_reserves_limit | value |
| goods_production_rank | 与国家某种商品的生产排行榜排名进行比较 | "goods_production_rank(g:luxury_clothes)" < 10 | value |
| government_legitimacy | 比较合法性 |  | value |
| government_transfer_of_power | 检查国家政府的权力交接方式 | government_transfer_of_power = key | value |
| government_wage_level | 比较 scope 国家的政府工资水平。`very_low, low, medium, high, very_high`；返回与 government_wage_level_value trigger 相同的数值 | government_wage_level = <level_term> | value |
| government_wage_level_value | 比较 scope 国家的政府工资水平数值。`0, 1, 2, 3, 4` | government_wage_level_value = <level_num> | value |
| has_active_peace_deal | 若国家所处的战争中存在已提出的和平协议则为真 | has_active_peace_deal = bool | boolean |
| has_any_law_commitment | 检查国家是否有制定任何法律的承诺 | has_any_law_commitment = yes | boolean |
| has_any_naval_only_hostilities | 检查国家是否与任何未处于战争状态的国家存在海上敌对 | has_any_naval_only_hostilities = yes | boolean |
| has_any_secessionists_broken_out | 检查国家是否有已爆发的分裂主义者 |  | boolean |
| has_any_secessionists_growing | 检查国家是否有正在壮大的分裂主义者 |  | boolean |
| has_any_strait_control | 检查 scope 国家是否拥有带海军要塞的海峡省份 | has_any_strait_control = yes | boolean |
| has_any_strait_province | 检查 scope 国家是否拥有任意海峡省份 | has_any_strait_province = yes | boolean |
| has_any_subventions_on | 检查 scope 国家是否对某种商品启用了任意等级的补贴 | scope:country = { has_any_subventions_on = <goods scope> } | goods |
| has_any_tariffs_on | 检查 scope 国家是否对某种商品设置了任意等级的关税 | scope:country = { has_any_tariffs_on = <goods scope> } | goods |
| has_attitude | 检查 scope 国家对另一国家是否持特定态度 | has_attitude = { who = <country scope> attitude = <attitude key> } |  |
| has_building | 若州/市场/州区域/国家拥有某类建筑则为真 | has_building = building |  |
| has_civil_war_from_movement_type | 检查国家是否正经历由特定运动类型引发的内战 | has_civil_war_from_movement_type = <political_movement_type scope> | political_movement_type |
| has_claim | 检查 scope 中的国家是否对某州/州区域/国家有宣称 | has_claim = <scope> |  |
| has_company | 检查 scope 国家中是否存在指定类型的公司 | has_company = <company_type scope> | company_type |
| has_completed_subgoal | 检查 scope 国家是否已完成某个子目标 | has_completed_subgoal = subgoal_key |  |
| has_consumption_tax | 检查国家是否对目标商品征收消费税。 | c:FRA = { has_consumption_tax = <goods scope> } | goods |
| has_convoys_being_sunk | 检查国家是否有护航船队正因袭击护航船队而被击沉 |  | boolean |
| has_diplomatic_pact | 检查两国之间是否有生效的指定类型外交协定 | has_diplomatic_pact = { who = <country scope> type = <diplomatic action key> is_initiator = yes/no } is_initiator 为可选参数，用于检查 scope 国家是否为该协定的最初发起方/目标方 |  |
| has_diplomatic_relevance | 检查目标国家对 scope 国家是否具有外交相关性 | has_diplomatic_relevance = <scope> | country |
| has_diplomats_expelled | 检查 scope 中的国家最近是否驱逐过 event target 的外交官 | has_diplomats_expelled = country | country |
| has_famine | 检查州或国家是否发生饥荒 | has_famine = yes/no | boolean |
| has_free_government_reform | 检查国家是否有一次免费（无激进派产生）的政府改革 | has_free_government_reform = <yes/no> | boolean |
| has_global_highest_gdp | 检查 scope 国家的 GDP 是否为全球最高 | has_global_highest_gdp = yes/no | boolean |
| has_global_highest_innovation | 检查 scope 国家的每周创新是否为全球最高 | has_global_highest_innovation = yes/no | boolean |
| has_government_clout | 检查国家政府是否拥有必要的总政治力量 |  | value |
| has_government_type | 检查国家政府类型是否为指定类型 | has_government_type = key |  |
| has_healthy_economy | 检查国家经济是否健康 |  | boolean |
| has_inactive_journal_entry | 检查国家是否拥有至少一个指定类型的未激活日志条目 | has_inactive_journal_entry = key |  |
| has_institution | 检查 scope 国家是否拥有特定类型的机构 | has_institution = <scope/key> |  |
| has_insurrectionary_interest_groups | 检查国家是否有处于叛乱状态的利益集团 |  | boolean |
| has_interest_marker_in_region | 若 scope 国家在目标区域有利益标记则为真 | has_interest_marker_in_region = region scope/tag |  |
| has_journal_entry | 检查国家是否拥有至少一个指定类型的已激活日志条目 | has_journal_entry = key |  |
| has_law | 检查国家是否已颁布某项法律 |  | law_type |
| has_law_commitment | 检查国家是否有制定某项法律的承诺 |  | law_type |
| has_law_imposition_rights | 检查 scope 国家是否拥有必要许可，可要求另一国家制定某项法律 | has_law_imposition_rights = { target_country = <country scope> type = <law type scope> } |  |
| has_law_or_variant | 检查国家是否已颁布某项法律或其任一变体法律 |  | law_type |
| has_modifier | 检查受支持的 scope 是否拥有某个限时 modifier | has_modifier = <key> |  |
| has_objective | 检查 scope 国家是否拥有某个目标类型 | has_objective = objective_type_key |  |
| has_overlapping_interests | 检查 scope 中的国家是否与目标国家的任意利益存在重叠的利益标记 | has_overlapping_interests = <scope> | country |
| has_port_country | 检查 scope 国家是否拥有至少一个港口 | has_port_country = yes/no | boolean |
| has_possible_decisions | 检查国家是否有任何可行的决议 | has_possible_decisions = yes | boolean |
| has_potential_to_form_country | 检查目标国家是否有朝一日能够成立该民族国家 | has_potential_to_form_country = <tag> |  |
| has_power_struggle | 检查 scope 强权集团是否正处于权力斗争 | has_power_struggle = yes/no | boolean |
| has_region_stance | 检查 scope 国家的人工智能对某个战略区域是否持指定立场 | region_stance = { region = sr:some_region stance = <conquer_region> } |  |
| has_researchable_technology | 检查国家是否还有任何可研究的技术。 |  | boolean |
| has_revolution | 检查国家是否发生革命起义 |  | boolean |
| has_ruling_interest_group | 检查国家政府是否包含指定的利益集团 |  |  |
| has_ruling_interest_group_count | 检查国家政府是否由指定数量的利益集团组成 |  | value |
| has_secret_goal | 检查 scope 国家对另一国家是否持特定秘密目标 | has_secret_goal = { who = <country scope> secret_goal = <secret_goal key> } |  |
| has_social_hierarchy | 检查 scope 国家是否采用了特定的社会等级制度 | has_social_hierarchy = <key> |  |
| has_state_in_state_region | 检查国家是否在州区域内拥有州 | has_state_in_state_region = key |  |
| has_strategic_adjacency | 检查 scope 中的国家与目标州/国家是否有战略相邻（直接/沿海/战争目标相邻） | has_strategic_adjacency = <scope> |  |
| has_strategic_land_adjacency | 检查 scope 中的国家与目标州/国家是否有战略相邻（仅限直接陆上接壤或战争目标相邻） | has_strategic_adjacency = <scope> |  |
| has_strategic_region_interest_tier | 检查 scope 国家在特定战略区域的利益层级排名 | has_strategic_region_interest_tier = { strategic_region = sr:target_region value >= 3 } |  |
| has_strategy | 检查 scope 中的国家是否采用特定的人工智能战略 | has_strategy = <key> |  |
| has_subject_relation_with | 检查 scope 中的国家是 event target 的附属国或宗主国 | has_subject_relation_with = country | country |
| has_sufficient_construction_capacity_for_investment | 检查国家是否有足够的建造能力来用尽所有流入投资池的资金。 |  | boolean |
| has_technology_progress | 检查国家的某项技术是否达到所需进度 | has_technology_progress = { technology = <technology key> progress = <0-1 value> } | value |
| has_technology_researched | 若国家已研究出某项技术则为真 | has_technology_researched = <scope/key> |  |
| has_treaty_port_in_market | 检查 scope 国家是否在目标市场中拥有条约港 | c:POR = { has_treaty_port_in_market = c:CHI.market } | market |
| has_truce_with | 检查国家是否与另一目标国家处于休战状态 | has_truce_with = c:GBR | country |
| has_war_with | 检查 scope 中的国家是否与 event target 处于战争状态 | has_war_with = country | country |
| has_wasted_construction | 检查国家是否正在浪费其产出的建造点数。 |  | boolean |
| highest_overlapping_interest_tier | 比较（scope 国家）在两国均有利益的各战略区域中最高的利益层级排名。 | highest_overlapping_interest_tier = { target = c:GBR value >= 2 } | value |
| highest_secession_progress | 比较某国内任何分裂运动的最高分裂进度 | highest_secession_progress > 0.7 | value |
| in_default | 检查国家当前是否处于违约状态 |  | boolean |
| in_election_campaign | 检查国家是否处于竞选活动期间 | in_election_campaign = <yes/no> | boolean |
| influence | 比较 scope 国家的可用影响力 |  | value |
| influence_usage | 比较 scope 国家已消耗的影响力 |  | value |
| institution_investment_level | 比较对某机构的投资等级 | institution_investment_level = { institution = <key> value = <comparator value> } | value |
| investment_pool | 检查国家投资池中是否有该数额的存款 | investment_pool > 1000 | value |
| investment_pool_gross_income | 检查国家投资池的总收入（支出前的收入）是否达到该数额 | investment_pool_gross_income > 1000 | value |
| investment_pool_net_income | 检查国家投资池的净收入（支出后的收入）是否达到该数额 | investment_pool_net_income > 1000 | value |
| is_adjacent_to_country | 检查 scope 中的国家是否与目标国家接壤 | is_adjacent_to_country = <scope> | country |
| is_adjacent_to_state | 检查 scope 中的国家是否与目标州接壤 | is_adjacent_to_state = <state scope> | state |
| is_ai | 若国家 scope 由人工智能控制则为真 | is_ai = bool | boolean |
| is_at_war | 检查国家是否处于战争状态 |  | boolean |
| is_banning_goods | 检查国家是否正在禁运某种商品 | is_banning_goods = <goods key/scope> |  |
| is_considered_adjacent_due_to_wargoals | 检查 scope 国家是否因在已表态的外交博弈中持有与目标国家相邻的战争目标，而被视为与目标国家相邻 | is_considered_adjacent_due_to_wargoals = <target country scope> | country |
| is_construction_paused | 检查某州的建造是否已暂停。 |  | boolean |
| is_country_alive | 检查 scope 国家是否存续，即是否在地图上拥有至少一个州且可与之交互 | is_country_alive = yes/no | boolean |
| is_country_type | 检查国家的类型 | is_country_type = country type |  |
| is_diplomatic_play_ally_of | 检查 scope 中的国家是否与 event target 处于同一外交博弈的同一方 | is_diplomatic_play_ally_of = country | country |
| is_diplomatic_play_committed_participant | 若国家是任一外交博弈的已表态参与方则为真 | is_diplomatic_play_participant = bool | boolean |
| is_diplomatic_play_enemy_of | 检查 scope 中的国家是否在外交博弈中与 event target 敌对 | is_diplomatic_play_enemy_of = country | country |
| is_diplomatic_play_initiator | 若国家是任一外交博弈的发起者则为真 | is_diplomatic_play_initiator = bool | boolean |
| is_diplomatic_play_involved_with | 检查 scope 中的国家是否与 event target 卷入同一外交博弈 | is_diplomatic_play_involved_with = country | country |
| is_diplomatic_play_participant_with | 检查 scope 中的国家是否与 event target 是同一外交博弈中的已表态参与方 | is_diplomatic_play_participant_with = country | country |
| is_diplomatic_play_target | 若国家是任一外交博弈的目标则为真 | is_diplomatic_play_target = bool | boolean |
| is_diplomatic_play_undecided_participant | 若国家是任一外交博弈的未表态参与方则为真 | is_diplomatic_play_participant = bool | boolean |
| is_direct_subject_of | 检查 scope 中的国家是否是 event target 的直接附属国（不含附属国的附属国） | is_direct_subject_of = country | country |
| is_enacting_law | 检查 scope 国家是否正在制定特定类型的法律。 | is_enacting_law = law_type:law_conscription | law_type |
| is_expanding_institution | 是否正在扩张某个机构 | is_expanding_institution = <yes>/<no> | boolean |
| is_forced_to_join_plays | 检查 scope 国家是否被迫加入目标国家的外交博弈 | is_forced_to_join_plays = c:country | country |
| is_home_country_for | 检查国家是否为目标国家的母国 |  | country |
| is_immune_to_revolutions | 检查国家是否已通过 set_immune_to_revolutions 被设为对革命免疫 警告：此项不检查国家是否因自身原因（例如本身即革命国家）而天然对革命免疫，仅针对 set_immune_to_revolutions 的效果。 is_immune_to_revolutions = yes/no | boolean |
| is_in_customs_union | 检查国家是否属于某个关税同盟 |  | boolean |
| is_in_customs_union_with | 检查国家是否与 scope 国家处于同一关税同盟 | is_in_customs_union_with = c:FRA | country |
| is_in_power_bloc | 检查国家是否属于某个强权集团 | is_in_power_bloc = yes/no | boolean |
| is_in_same_power_bloc | 检查 scope 国家是否与目标 scope 国家属于同一强权集团 | is_in_same_power_bloc = c:GBR | country |
| is_in_war_together | 检查 scope 中的国家是否与 event target 处于战争同一方 | is_in_war_together = country | country |
| is_indirect_subject_of | 检查 scope 中的国家是否是 event target 的间接附属国（附属国的附属国） | is_indirect_subject_of = country | country |
| is_insurrectionary | 检查国家、运动或利益集团是否处于叛乱状态 |  | boolean |
| is_junior_in_customs_union | 若国家是关税同盟中的从属国则为真 | is_junior_in_customs_union = bool | boolean |
| is_local_player | 若国家 scope 为玩家则为真 | is_local_player = bool | boolean |
| is_losing_power_rank | 检查国家是否正处于等级排名下降的过程中 |  | boolean |
| is_market_reachable_for_trade | 检查 scope 国家在贸易层面能否到达指定的市场 scope | is_market_reachable_for_trade = scope:my_market_scope | market |
| is_mass_migration_origin | 检查 scope 国家是否为大迁移的起源地 | is_mass_migration_origin = yes | boolean |
| is_mass_migration_origin_of_culture | 检查 scope 国家是否是特定文化大迁移的起源地 | is_mass_migration_origin_of_culture = cu:example_culture | culture |
| is_owed_obligation_by | 检查 scope 国家是否对目标国家持有义务 | is_owed_obligation_by = c:FRA | country |
| is_player | 若国家 scope 为玩家则为真 | is_player = bool | boolean |
| is_power_bloc_leader | 检查国家是否是某个强权集团的领袖 | is_power_bloc_leader = yes/no | boolean |
| is_researching_technology | 检查国家是否正在积极研究某项技术 | is_researching_technology = <scope/key/any> |  |
| is_researching_technology_category | 检查国家是否正在积极研究某个技术类别 | is_researching_technology_category = <key/any> |  |
| is_revolutionary | 检查国家、运动或利益集团是否具有革命性 |  | boolean |
| is_secessionist | 检查国家、运动或利益集团是否具有分裂性 |  | boolean |
| is_subject | 若国家是附属国则为真 | is_subject = bool | boolean |
| is_subject_of | 检查 scope 中的国家是否是 event target 的附属国（含附属国的附属国） | is_subject_of = country | country |
| is_subject_type | 检查国家的附属国类型 | is_subject_type = subject type |  |
| is_supporting_unification_candidate | 检查 scope 国家是否支持特定国家统一候选者 | is_supporting_unification_candidate = { who = c:PRU country_formation = GER } |  |
| is_taxing_goods | 检查国家是否对某种商品征税 | has_embargo = <goods key/scope> |  |
| is_unification_candidate | 检查 scope 国家是否是某国家 tag 的统一候选者 | is_unification_candidate = GER |  |
| is_violating_sovereignty_of | 检查 scope 国家是否侵犯目标国家的主权 | is_violating_sovereignty_of = c:GBR | country |
| isolated_states | 比较孤立州的数量 |  | value |
| leading_producer_of | 检查国家是否是某种商品的最大生产国 | leading_producer_of = g:luxury_clothes | goods |
| leads_customs_union | 检查是否有其他国家加入该国的关税同盟 | leads_customs_union = bool | boolean |
| liberty_desire | 比较 scope 国家独立倾向数值的 trigger。 | liberty_desire > 50 | value |
| liberty_desire_weekly_progress | 比较 scope 国家每周独立倾向进度的 trigger。 | liberty_desire_weekly_progress > 0 | value |
| liberty_desire_weekly_progress_from_support_independence | 比较 scope 国家因获得独立支持而产生的每周独立倾向进度的 trigger。 | liberty_desire_weekly_progress_from_support_independence > 0 | value |
| literacy_rate | 检查人口、州或国家是否拥有一定的识字率 | literacy = value | value |
| loyalist_fraction | 比较州或国家中忠诚派在人口中的比例，除 value 外所有参数均为可选 | loyalist_fraction = { value = <script_value> pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> } | value |
| max_law_enactment_setbacks | 比较国家在立法失败前可遭受的最大挫折次数 |  | value |
| max_num_companies | scope 国家允许拥有的公司数量上限 | num_num_companies > 0 | value |
| military_ship_maintenance_fulfillment | 比较国家军舰维护的满足比率 | military_ship_maintenance_fulfillment = <value> | value |
| military_wage_level | 比较 scope 国家的军队工资水平。`very_low, low, medium, high, very_high`；返回与 military_wage_level_value trigger 相同的数值 | military_wage_level = <level_term> | value |
| military_wage_level_value | 比较 scope 国家的军队工资水平数值。`0, 1, 2, 3, 4` | military_wage_level_value = <level_num> | value |
| nationalization_cost | 比较 scope 国家境内由目标国家的政府或人口所拥有的全部建筑的总国有化成本 | nationalization_cost = { target = scope:other_country value > 100000 } | value |
| naval_power_projection | 与国家的海军总力量投射进行比较 | scope:example_country = { naval_power_projection < root.naval_power_projection } | value |
| neighbors_any_power_bloc | 检查 scope 国家是否与任意强权集团相邻。注意：scope 国家不被视为与其所属强权集团（若有）相邻 | neighbors_any_power_bloc = yes/no | boolean |
| neighbors_member_of_same_power_bloc | 检查 scope 国家是否与属于同一强权集团的其他国家相邻 | neighbors_member_of_same_power_bloc = yes/no | boolean |
| neighbors_power_bloc | 检查 scope 国家是否与目标强权集团相邻。注意：scope 国家不被视为与其所属强权集团（若有）相邻 | neighbors_power_bloc = c:PRU.power_bloc | power_bloc |
| num_companies | scope 国家拥有的公司数量 | num_companies > 0 | value |
| num_diplomatic_pacts | 与国家指定类型的外交协定数量进行比较 | num_diplomatic_pacts = { type = <key> value < 10 } | value |
| num_investments_of_type | 检查 scope 国家在境外拥有的指定类型建筑等级数量。 | num_investments_of_type = { type = building_oil_rig value > 5 } | value |
| num_political_lobbies | 比较 scope 国家或利益集团中政治游说团的数量 | num_political_lobbies > 0 | value |
| num_subjects | 比较 scope 国家的附属国数量 | num_subjects = <value> | value |
| num_taxed_goods | 比较 scope 国家征收消费税的商品数量 | num_taxed_goods = <value> | value |
| number_of_claims | 该国家对非本国州拥有的宣称数量 | number_of_claims > 0 | value |
| number_of_possible_decisions | 国家可采取的可行决议数量 | number_of_possible_decisions > 0 | value |
| overlord_can_decrease_subject_autonomy | 检查宗主国是否可以降低附属国的自治度 | overlord_can_decrease_subject_autonomy = bool | boolean |
| owes_obligation_to | 检查 scope 中的国家是否欠 event target 一项义务 | owes_obligation_to = country | country |
| owns_entire_state_region | 检查国家是否拥有整个区域 | owns_entire_state_region = key |  |
| owns_treaty_port_in | 检查国家是否拥有指定州区域内的条约港 | owns_treaty_port_in = key |  |
| play_participant_has_war_goal_of_type_against | 检查 scope 国家在任一外交博弈中是否持有针对特定国家的特定类型战争目标 | play_participant_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } |  |
| play_side_has_war_goal_of_type_against | 检查在任一外交博弈中与 scope 国家同方的任何国家是否持有针对特定国家的特定类型战争目标 | play_side_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } |  |
| political_strength_share | 检查某人口类型、宗教或文化在国家或州中的政治力量份额。必须且只能指定 pop_type、religion、culture 三者之一。 | political_strength_share = { pop_type/religion/culture = <key/scope> value <compare operator> <value> } | value |
| politically_involved_ratio | 比较国家中参与政治的人口百分比 | politically_involved_ratio > 0.25 | value |
| pop_type_percent_country | 检查 scope 国家是否有 <percent> 的人口属于指定人口类型 | scope:example_country = { pop_type_percent_country = { pop_type = <pop_type> percent <compare operator (<,>,= and so on)> <percent> } } | value |
| potential_diplomatic_play_power_ratio | 检查在一场潜在外交博弈中 scope 国家一方与目标国家一方之间的预期实力比 尝试预测相关参与方将（在何种程度上）加入哪一方，因此并非只比较“起始实力” potential_diplomatic_play_power_ratio = { type = dp_open_market target = c:BEL state = c:BEL.capital value > 1.0 } state 与 type 为可选项，默认为在目标首都的 dp_open_market | value |
| potential_income | 比较国家的潜在收入（每周收入加上税收损耗） | potential_income > 1000 | value |
| power_bloc_share_gdp | 将 scope 中国家的 GDP 份额与其强权集团所有当前成员进行比较，若不在强权集团中则返回 -1 | power_bloc_share_gdp > 0.2 | value |
| power_bloc_share_gdp_with | 将 scope 中国家的 GDP 份额与其强权集团所有成员加上一个额外国家进行比较，若不在强权集团中则返回 -1 | "power_bloc_share_gdp_with(scope:country) > 0.2" | value |
| power_bloc_share_gdp_without | 将 scope 中国家的 GDP 份额与其强权集团所有成员减去其中一个成员进行比较，若不在强权集团中则返回 -1 | "power_bloc_share_gdp_without(scope:country) > 0.2" | value |
| power_bloc_share_power_projection | 将 scope 中国家的强权投射份额与其强权集团所有成员进行比较，若不在强权集团中则返回 -1 | power_bloc_share_power_projection > 0.2 | value |
| power_bloc_share_power_projection_with | 将 scope 中国家的强权投射份额与其强权集团所有成员加上一个额外国家进行比较，若不在强权集团中则返回 -1 | "power_bloc_share_power_projection_with(scope:country) > 0.2" | value |
| power_bloc_share_power_projection_without | 将 scope 中国家的强权投射份额与其强权集团所有成员减去其中一个成员进行比较，若不在强权集团中则返回 -1 | "power_bloc_share_power_projection_without(scope:country) > 0.2" | value |
| power_bloc_share_prestige | 将 scope 中国家的威望份额与其强权集团所有成员进行比较，若不在强权集团中则返回 -1 | power_bloc_share_prestige > 0.2 | value |
| power_bloc_share_prestige_with | 将 scope 中国家的威望份额与其强权集团所有成员加上一个额外国家进行比较，若不在强权集团中则返回 -1 | "power_bloc_share_prestige_with(scope:country) > 0.2" | value |
| power_bloc_share_prestige_without | 将 scope 中国家的威望份额与其强权集团所有成员减去其中一个成员进行比较，若不在强权集团中则返回 -1 | "power_bloc_share_prestige_without(scope:country) > 0.2" | value |
| prestige | 比较威望 |  | value |
| primary_cultures_percent_country | 检查一个国家的人口中有一定比例属于该国的主要文化 | scope:example_country = { primary_cultures_percent_country >= 0.2 } | value |
| produced_authority | 比较 scope 中国家产出的统治力 |  | value |
| produced_bureaucracy | 比较 scope 中国家产出的行政力 |  | value |
| produced_influence | 比较 scope 中国家产出的影响力 |  | value |
| radical_fraction | 比较州或国家人口中的激进派比例，除 value 外所有参数均为可选 | radical_fraction = { value = <script_value> pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> } | value |
| radical_population_fraction | 比较给定国家人口中激进派的比例 | radical_population_fraction > 0.2 | value |
| region_score | 在国家 scope 中比较指定战略区域的 AI 策略区域总分。若该国由玩家控制则返回 0 | region_score = { strategic_region = sr:region_key value >= 300 } "region_score(sr:region_key)" >= 300 | value |
| relative_authority | 比较 scope 中国家统治力的未使用比例 |  | value |
| relative_bureaucracy | 比较 scope 中国家行政力的未使用比例 |  | value |
| relative_influence | 比较 scope 中国家影响力的未使用比例 |  | value |
| religion_percent_country | 检查一个国家的人口中有一定比例属于特定宗教 | scope:example_country = { religion_percent_country = { target = rel:catholic value <= 0.8 } } | value |
| ruler_can_have_command | 检查该国的政府类型是否允许其统治者拥有指挥权 | ruler_can_have_command = yes/no | boolean |
| scaled_debt | 将数值与该国相对于债务上限的债务进行比较 | scaled_debt = value | value |
| scaled_gold_reserves | 将数值与该国相对于储备上限的黄金储备进行比较 | scaled_gold_reserves = value | value |
| ship_modification_market_demand_ratio | 目标船只改装所需建造商品的商品加权买/卖比，针对国家 scope 的市场进行评估。 | "ship_modification_market_demand_ratio(scope:ship_modification_type) > 1.25" | value |
| should_set_wargoal | 检查该国在其参与的任一外交博弈中是否缺少主要战争目标 |  | boolean |
| shrinking_institution | 检查该机构是否正在收缩 | expanding_institution = <scope/key> |  |
| size_weighted_lost_battles_fraction | 判定目标国家在目标战争中战败战斗的比例，按战争中所有战斗的人力规模加权 | size_weighted_lost_battles_fraction = { target = scope:war value > 0.3 } add = "size_weighted_lost_battles_fraction(scope:war)" | value |
| sol_ranking | 比较一个国家的生活水平排名（名次） | sol_ranking > 42 | value |
| subject_can_increase_autonomy | 检查一个附属国能否提升其自治度 | subject_can_increase_autonomy = bool | boolean |
| supply_network_strength | 比较该国的补给网络强度（可超过 1） | supply_network_strength > 1.1 | value |
| supply_ship_maintenance_fulfillment | 比较一个国家补给船维护的满足比例 | supply_ship_maintenance_fulfillment < 1 | value |
| taking_loans | 检查该国当前是否存在每周赤字并借取贷款以弥补 |  | boolean |
| tax_level | 比较 scope 中国家的总体税收等级。`very_low, low, medium, high, very_high`；返回与 tax_level_value trigger 相同的数值 | tax_level = <level_term> | value |
| tax_level_value | 比较 scope 中国家总体税收等级的整数值。`0, 1, 2, 3, 4` | income_tax_level_value = <level_num> | value |
| tax_waste | 比较该国的税收损耗 | tax_waste > 100 | value |
| tenure_in_current_power_bloc_days | 比较 scope 中国家作为其当前强权集团成员的天数 | tenure_in_current_power_bloc_days > 720 | value |
| tenure_in_current_power_bloc_months | 比较 scope 中国家作为其当前强权集团成员的（整）月数 | tenure_in_current_power_bloc_months > 20 | value |
| tenure_in_current_power_bloc_weeks | 比较 scope 中国家作为其当前强权集团成员的（整）周数 | tenure_in_current_power_bloc_weeks > 12 | value |
| tenure_in_current_power_bloc_years | 比较 scope 中国家作为其当前强权集团成员的（整）年数 | tenure_in_current_power_bloc_years > 5 | value |
| total_population | 比较给定国家的总人口 | total_population > 100000 | value |
| total_population_including_subjects | 比较 scope 国家及其附属国的总人口 | total_population_including_subjects > 40000000 | value |
| total_population_including_subjects_share | 比较 scope 国家及其附属国总人口占全球人口的比例 | total_population_including_subjects_share > 0.4 | value |
| total_population_share | 比较给定国家总人口占全球人口的比例 | total_population_share > 0.02 | value |
| transfer_money_gross_income | 该国是否通过资金转让条约拥有该数额的总收入（扣除支出前的收入） | transfer_money_gross_income > 1000 | value |
| transfer_money_net_income | 该国是否通过资金转让条约拥有该数额的净收入（扣除支出后的收入） | transfer_money_net_income > 1000 | value |
| war_participant_has_war_goal_of_type_against | 检查 scope 国家在任一战争中是否持有针对特定国家的特定类型的战争目标 | war_participant_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } |  |
| war_side_has_war_goal_of_type_against | 检查在任一战争中与 scope 国家同阵营的任一国家是否持有针对特定国家的特定类型的战争目标 | war_side_has_war_goal_of_type_against = { type = <wargoal type key> target = <country scope> } |  |
| was_formed_from | 检查一个成立的国家此前是否具有特定的定义 | was_formed_from = <tag> |  |
| wealth_share | 检查一个国家或州中某人口类型、宗教或文化的财富政治力量份额。必须且只能指定 pop_type、religion 或 culture 中的一项。 | wealth_share = { pop_type/religion/culture = <key/scope> value <compare operator> <value> } | value |
| would_accept_diplomatic_action | 检查一个国家是否会接受另一个国家提出的外交行动 | would_accept_diplomatic_action = { actor = <country scope> type = <action type key> first_state = <state scope, optional> second_state = <state scope, optional> modify_acceptance = <script value, optional> } 若设置了 modify_acceptance，其数值将被加到对方的接受分数上，以便检查例如对方是否会附带一项义务接受等 |  |

| Event target | 描述 | To scope |
|---|---|---|
| active_law | scope 到 scope 国家在指定法律组中的现行法律（active_law:lawgroup_trade_policy） | law |
| ai_army_comparison | scope 到两个国家之间的陆军实力对比（示例：value = ai_army_comparison:root） | value |
| ai_gdp_comparison | scope 到两个国家之间的 GDP 对比（示例：value = ai_army_comparison:root） | value |
| ai_ideological_opinion | scope 到 AI 对目标国家的意识形态看法（以 scope 国家视角）（示例：value = ai_ideological_opinion:root） | value |
| ai_navy_comparison | scope 到两个国家之间的海军实力对比（示例：value = ai_navy_comparison:root） | value |
| ai_subject_value | scope 到目标国家希望将 scope 国家作为附属国的 AI 意愿值（示例：value = ai_subject_value:root） | value |
| ai_transit_rights_value | scope 到希望获得途经目标国家通行权的 AI 意愿值（示例：value = ai_transit_rights_value:root） | value |
| ai_treaty_fairness | scope 到 AI 对与目标国家之间现有条约条款公平性（对双方而言）的评估（示例：value = ai_treaty_fairness_score:root） | value |
| ai_treaty_value | scope 到 AI 对与目标国家之间现有条约条款对自身有利程度的评估（示例：value = ai_treaty_value:root） | value |
| army_size | scope 国家的营数量，不含当前已征召的征召兵。 | value |
| army_size_including_conscripts | scope 国家的营数量，含当前已征召的征召兵。 | value |
| army_size_including_raised_conscripts | scope 国家的营数量，含当前已征召的征召兵但不含未征召的征召兵。 | value |
| average_expected_sol | 获取 scope 的平均预期生活水平 | value |
| average_sol | 获取 scope 的平均生活水平 | value |
| building_levels | 获取 scope 国家的非自给建筑总等级数 | value |
| cached_ai_coastal_population | scope 到 AI 支出变量中记录的沿海人口总数（示例：value = cached_ai_coastal_population） | value |
| cached_ai_incorporated_coastal_population | scope 到 AI 支出变量中记录的已整合沿海人口总数（示例：value = cached_ai_incorporated_coastal_population） | value |
| cached_ai_incorporated_population | scope 到 AI 支出变量中记录的已整合人口总数（示例：value = cached_ai_incorporated_population） | value |
| cached_ai_overseas_subject_population | scope 到 AI 支出变量中记录的直接非邻近附属国人口总数（示例：value = cached_ai_overseas_subject_population） | value |
| cached_ai_subject_population | scope 到 AI 支出变量中记录的直接附属国人口总数（示例：value = cached_ai_subject_population） | value |
| cached_ai_total_population | scope 到 AI 支出变量中记录的总人口（示例：value = cached_ai_total_population） | value |
| cached_ai_unincorporated_coastal_population | scope 到 AI 支出变量中记录的未整合沿海人口总数（示例：value = cached_ai_unincorporated_coastal_population） | value |
| cached_ai_unincorporated_population | scope 到 AI 支出变量中记录的未整合人口总数（示例：value = cached_ai_unincorporated_population） | value |
| capital | scope 到一个国家的首都州 | state |
| civil_war_origin_country | scope 到一个内战国家的起源国 | country |
| colonial_growth_per_colony | scope 到该国的每块殖民地殖民增长值（示例：colonial_growth_per_colony > 0） | value |
| company | scope 到 scope 国家指定公司类型的公司（company:company_rheinmetall） | company |
| country_definition | scope 到国家的定义 | country_definition |
| credit | scope 到该国当前可借取的最大信贷额度 | value |
| currently_enacting_law | 从一个国家 scope 到其当前正在制定的法律 | law |
| diplomatic_pact_expense_ratio | scope 到该国外交条约支出与收入之比，限制在 0-1 之间（示例：value = diplomatic_pact_expense_ratio） | value |
| flagship | 获取 scope 国家的旗舰 | ship |
| gdp | 获取 scope 国家的年度预测 GDP | value |
| get_ruler_for | 在给定权力移交类型下，从国家 scope 到将成为统治者的人物 get_ruler_for:parliamentary_elective = { effects... } | character |
| government_size | 获取 scope 国家当前政府中政党与独立利益集团的数量 | value |
| heir | scope 到一个国家的继承人 | character |
| ig | scope 到属于该国的指定键值的利益集团，示例：ig:ig_armed_forces | interest_group |
| imposed_law | 从一个国家 scope 到当前被强加于其的法律（无论是否正在制定） | law |
| imposer_of_law | 从一个国家 scope 到当前对其强加法律的国家 | country |
| income | 获取 scope 国家当前的每周收入 | value |
| income_transfer_expenses | scope 到 scope 国家通过条约与协定向其他国家转让的资金数额（示例：income_transfer_expenses >= 100） | value |
| income_transfer_relative_expenses | scope 到该国通过条约与协定向其他国家转让的资金占其收入的比例（示例：income_transfer_relative_expenses >= 0.2） | value |
| infamy | scope 到 scope 国家的恶名（示例：infamy >= 2） | value |
| institution | 通过名称 scope 到一个国家的机构（institution:institution_health_system） | institution |
| investment_pool_income | 获取 scope 国家当前的每周投资池收入 | value |
| je | scope 到属于该国的指定键值的日志条目，示例：je:je_antarctica | journal_entry |
| legitimacy | scope 到国家当前的合法性数值 | value |
| lobby_foreign_anti_clout | scope 到针对特定国家的所有反该国外交政策游说团的总政治力量（lobby_foreign_anti_clout:root >= 0.2） | value |
| lobby_foreign_pro_clout | scope 到针对特定国家的所有亲该国外交政策游说团的总政治力量（lobby_foreign_pro_clout:root >= 0.2） | value |
| lobby_in_government_foreign_anti_clout | scope 到针对特定国家、处于政府中的所有反该国外交政策游说团的总政治力量（lobby_in_government_foreign_anti_clout:root >= 0.2） | value |
| lobby_in_government_foreign_pro_clout | scope 到针对特定国家、处于政府中的所有亲该国外交政策游说团的总政治力量（lobby_in_government_foreign_pro_clout:root >= 0.2） | value |
| lobby_war_opposition | scope 到反对 scope 战争的所有游说团的总政治力量（lobby_war_opposition:root >= 0.2） | value |
| lobby_war_support | scope 到支持 scope 战争的所有游说团的总政治力量（lobby_war_support:root >= 0.2） | value |
| market | scope 到该对象所在的市场 | market |
| market_capital | scope 到一个国家的市场首都 | state |
| migration_pull | 获取一个州的迁移吸引力或一个国家的大规模迁移吸引力。 | value |
| military_expenses | 获取 scope 国家当前的军费开支（奴隶、工资和商品） | value |
| military_expenses_share | 获取 scope 国家当前军费开支（奴隶、工资和商品）相对总开支的比例 | value |
| modifier | scope 到属于当前对象的指定键值的 modifier 类型数值，示例：modifier:country_influence_add | boolean, value |
| mutual_trade_value_with_country | scope 到两个市场之间贸易路线上交易商品的总基础价值（示例：mutual_trade_value_with_country:root >= 1000） | value |
| naval_combat_power | scope 到该国的海军战斗力（示例：naval_combat_power > 100） | value |
| naval_hostility_average_damage_dealt | scope 到该国在回顾期内由其发起的海上敌对行动中造成的平均伤害。若未找到敌对行动则返回 -1。 | value |
| naval_hostility_damage | scope 到该国在当前海上敌对行动中对另一国造成的伤害点数（示例：naval_hostility_damage:root >= 50） | value |
| naval_vulnerability | scope 到基于贸易依赖度和沿海 GDP 份额计算的国家海军脆弱度分数，上限为一个 define 最大值 | value |
| navy_size | scope 国家的分舰队数量。 | value |
| num_active_interests | scope 到一个国家拥有的活跃利益数量 num_active_interests > 5 | value |
| num_active_natural_interests | scope 到一个国家拥有的活跃天然利益数量 num_active_natural_interests > 5 | value |
| num_active_plays | 获取 scope 国家当前发起的活跃外交博弈数量 | value |
| num_active_ships | 获取一个国家、指挥官或军事编队的活跃船只数量，或获取该省份内与指定国家结盟的军事编队的活跃船只数量 | value |
| num_active_ships_in_battle | 获取一个国家、指挥官或军事编队战斗中的活跃船只数量，或获取该省份内与指定国家结盟的军事编队战斗中的活跃船只数量 | value |
| num_active_ships_not_in_battle | 获取一个国家、指挥官或军事编队非战斗中的活跃船只数量，或获取该省份内与指定国家结盟的军事编队非战斗中的活跃船只数量 | value |
| num_admirals | scope 到该国的海军上将数量 | value |
| num_alliances | 获取 scope 国家的同盟总数（示例：num_alliances:root >= 2） | value |
| num_alliances_and_defensive_pacts_with_allies | scope 到目标国家与 scope 国家盟友之间的同盟数量（示例：num_alliances_and_defensive_pacts_with_allies:root >= 2） | value |
| num_alliances_and_defensive_pacts_with_rivals | scope 到目标国家与 scope 国家竞争对手之间的同盟与防御条约数量（示例：num_alliances_and_defensive_pacts_with_rivals:root >= 2） | value |
| num_characters | scope 到该国的人物数量 | value |
| num_colony_projects | 获取 scope 国家当前未完成/进行中的殖民地项目数量 | value |
| num_commanders | scope 到该国的指挥官数量 | value |
| num_defensive_pacts | scope 到目标国家拥有的防御条约总数（示例：num_defensive_pacts >= 2） | value |
| num_generals | scope 到该国的将军数量 | value |
| num_income_transfer_pacts | scope 到目标国家拥有的（向他国）转让收入的协定总数（示例：num_income_transfer_pacts >= 2） | value |
| num_income_transfer_treaty_articles | scope 到目标国家拥有的（向他国）转让收入的条约条款总数（示例：num_income_transfer_treaty_articles >= 2） | value |
| num_income_transfers | scope 到目标国家拥有的（向他国）转让收入的协定与条约条款总数（示例：num_income_transfers >= 2） | value |
| num_incorporated_states | 获取 scope 国家当前的已整合州数量 | value |
| num_interests | scope 到一个国家拥有的利益数量（含非活跃）num_interests > 5 | value |
| num_natural_interests | scope 到一个国家拥有的天然利益数量（含非活跃）num_natural_interests > 5 | value |
| num_non_destroyed_ships | 获取一个国家、指挥官或军事编队的未沉没船只数量，或获取该省份内与指定国家结盟的军事编队的未沉没船只数量 | value |
| num_non_destroyed_ships_in_battle | 获取一个国家、指挥官或军事编队战斗中的未沉没船只数量，或获取该省份内与指定国家结盟的军事编队战斗中的未沉没船只数量 | value |
| num_non_destroyed_ships_not_in_battle | 获取一个国家、指挥官或军事编队非战斗中的未沉没船只数量，或获取该省份内与指定国家结盟的军事编队非战斗中的未沉没船只数量 | value |
| num_obligations_earned | 从一个国家 scope 到他国欠其的义务数量（即其已赢得的义务） | value |
| num_pending_events | scope 到 scope 国家待处理事件的数量，可按总体或指定类别 num_pending_events > 0 num_pending_events:enactment > 0 | value |
| num_politicians | scope 到该国的政治家数量 | value |
| num_positive_relations | 获取当前与 scope 国家关系为正的国家数量 | value |
| num_queued_constructions | scope 到目标国家排队中建造项目的总数（示例：num_queued_constructions >= 2） | value |
| num_queued_government_constructions | scope 到目标国家排队中政府建造项目的总数（示例：num_queued_government_constructions >= 2） | value |
| num_queued_private_constructions | scope 到目标国家排队中私人建造项目的总数（示例：num_queued_private_constructions >= 2） | value |
| num_rivals | scope 到目标国家拥有的竞争对手总数（示例：num_rivals >= 2） | value |
| num_ruling_igs | 获取 scope 国家当前政府中利益集团的数量 | value |
| num_shared_rivals | scope 到 scope 国家与目标国家共有的竞争对手数量（示例：num_shared_rivals:root >= 2） | value |
| num_ships | 获取一个国家、指挥官或军事编队的船只数量，或获取该省份内与指定国家结盟的军事编队的船只数量 | value |
| num_ships_in_battle | 获取一个国家、指挥官或军事编队战斗中的船只数量，或获取该省份内与指定国家结盟的军事编队战斗中的船只数量 | value |
| num_ships_not_in_battle | 获取一个国家、指挥官或军事编队非战斗中的船只数量，或获取该省份内与指定国家结盟的军事编队非战斗中的船只数量 | value |
| num_ships_of_group | 所选国家或军事编队中指定舰船组的舰船数量 | value |
| num_states | 获取所选国家当前的州数量 | value |
| num_unincorporated_states | 获取所选国家当前未整合州的数量 | value |
| overlord | 转到所选国家的直接宗主国 | country |
| owner | 转到该对象的所有者国家 | country |
| owning_company | 转到拥有所选国家的公司 | company |
| pirated_trade_value_by | 转到目标国家每周从该国掠夺商品的基础价值的平均值（示例：pirated_trade_value_by:root >= 50） | value |
| power_bloc | 转到所选国家所在的强权集团 | power_bloc |
| principal | 获取该国当前的债务本金 | value |
| py | 转到该国具有指定键值的活跃政党，示例：py:communist_party | party |
| relations | 转到两国之间的关系（示例：relations:root >= 2） | value |
| relations_change_rate | 转到两国关系进展的每日变化（示例：relations_change_rate:root > 0） | value |
| religion | 转到国家或国家定义的主要宗教，或人口的宗教 | religion |
| ruler | 转到一国的统治者 | character |
| strait_trade_importance_by | 转到该国经由目标国家控制的海峡进行贸易的商品贸易重要度。若控制者控制海峡两侧，累计值会乘以 STRAIT_FULL_CONTROL_TRADE_IMPORTANCE_MULT（示例：strait_trade_importance_by:root >= 100） | value |
| technology_being_researched | 转到一国当前正在研究的技术 | technology |
| techs_researched | 转到一国当前已研究技术的数量 | value |
| tension | 转到两国之间的紧张度（示例：tension:root >= 2） | value |
| top_overlord | 转到所选国家的最高宗主国 | country |
| total_crew_needed | 获取一国所有舰船所需的水手总数 | value |
| total_export_value | 转到所选国家向世界市场出口的总价值（示例：total_export_value >= 1000） | value |
| total_import_value | 转到所选国家从世界市场进口的总价值（示例：total_import_value >= 1000） | value |
| total_marine_capacity | 获取一国所有舰队的海军陆战队容量总和 | value |
| total_trade_value | 转到所选国家与世界市场贸易的总价值（示例：total_trade_value >= 1000） | value |

### 国家（Country）modifier 类型

以 `country_` 为前缀的 [modifier 类型](Modifier types.md) 将其效果应用于国家。

由于篇幅原因，基于文化的 modifier 类型 `country_[culture]_cultural_acceptance_add` 和 `country_fervor_target_[culture]_add` 未予收录。

| Modifier 类型 | 本地化文本 | 类型 | 格式 | 备注 |
|---|---|---|---|---|
| country_academics_pol_str_mult | 学者的政治力量 | 乘法 | 百分比，中性 |  |
| country_academics_voting_power_add | 学者选票带来的政治力量 | 加法 | 中性 | 基于对象 启用选举 |
| country_acceptance_homeland_add | 来自本土的接纳度 | 加法 | 良好 |  |
| country_acceptance_no_shared_heritage_trait_add | 来自无共享传承特质的接纳度 | 加法 | 良好 |  |
| country_acceptance_no_shared_language_trait_add | 来自无共享语言特质的接纳度 | 加法 | 良好 |  |
| country_acceptance_no_shared_religious_trait_add | 来自无共享宗教特质的接纳度 | 加法 | 良好 |  |
| country_acceptance_no_shared_tradition_trait_add | 来自无共享传统特质的接纳度 | 加法 | 良好 |  |
| country_acceptance_not_homeland_add | 来自非本土的接纳度 | 加法 | 良好 |  |
| country_acceptance_primary_culture_add | 来自主流文化的接纳度 | 加法 | 良好 |  |
| country_acceptance_shared_heritage_trait_add | 来自共享传承特质的接纳度 | 加法 | 良好 |  |
| country_acceptance_shared_heritage_trait_group_add | 来自共享传承特质组的接纳度 | 加法 | 良好 |  |
| country_acceptance_shared_language_trait_add | 来自共享语言特质的接纳度 | 加法 | 良好 |  |
| country_acceptance_shared_language_trait_group_add | 来自共享语言特质组的接纳度 | 加法 | 良好 |  |
| country_acceptance_shared_religious_trait_add | 来自共享宗教特质的接纳度 | 加法 | 良好 |  |
| country_acceptance_shared_religious_trait_group_add | 来自共享宗教特质组的接纳度 | 加法 | 良好 |  |
| country_acceptance_shared_tradition_trait_add | 来自共享传统特质的接纳度 | 加法 | 良好 |  |
| country_acceptance_state_religion_add | 来自国教的接纳度 | 加法 | 良好 |  |
| country_admiral_rank_impact_mult | 海军上将军衔影响 | 乘法 | 百分比，良好 |  |
| country_agitator_slots_add | 潜在鼓动家数量 | 加法 | 良好 |  |
| country_ahead_of_time_research_penalty_mult | 超前研究惩罚 | 乘法 | 百分比，有害 |  |
| country_all_buildings_protected_bool | 禁止缩减所有建筑 | 布尔值 | 有害 |  |
| country_allow_assimilation_cultural_erasure_bool | 允许“文化抹除”状态的人口同化 | 布尔值 | 中性 |  |
| country_allow_assimilation_full_acceptance_bool | 允许“完全接纳”状态的人口同化 | 布尔值 | 中性 |  |
| country_allow_assimilation_open_prejudice_bool | 允许“公开偏见”状态的人口同化 | 布尔值 | 中性 |  |
| country_allow_assimilation_second_rate_citizen_bool | 允许“二等公民”状态的人口同化 | 布尔值 | 中性 |  |
| country_allow_assimilation_violent_hostility_bool | 允许“激烈敌意”状态的人口同化 | 布尔值 | 中性 |  |
| country_allow_conversion_cultural_erasure_bool | 允许“文化抹除”状态的宗教皈依 | 布尔值 | 中性 |  |
| country_allow_conversion_full_acceptance_bool | 允许“完全接纳”状态的宗教皈依 | 布尔值 | 中性 |  |
| country_allow_conversion_open_prejudice_bool | 允许“公开偏见”状态的宗教皈依 | 布尔值 | 中性 |  |
| country_allow_conversion_second_rate_citizen_bool | 允许“二等公民”状态的宗教皈依 | 布尔值 | 中性 |  |
| country_allow_conversion_violent_hostility_bool | 允许“激烈敌意”状态的宗教皈依 | 布尔值 | 中性 |  |
| country_allow_enacting_decrees_in_subject_bool | 允许在附属国州颁布法令 | 布尔值 | 良好 |  |
| country_allow_multiple_alliances_bool | 允许多重同盟 | 布尔值 | 良好 |  |
| country_allow_voting_cultural_erasure_bool | 给予“文化抹除”状态投票权 | 布尔值 | 中性 |  |
| country_allow_voting_full_acceptance_bool | 给予“完全接纳”状态投票权 | 布尔值 | 中性 |  |
| country_allow_voting_open_prejudice_bool | 给予“公开偏见”状态投票权 | 布尔值 | 中性 |  |
| country_allow_voting_second_rate_citizen_bool | 给予“二等公民”状态投票权 | 布尔值 | 中性 |  |
| country_allow_voting_violent_hostility_bool | 给予“激烈敌意”状态投票权 | 布尔值 | 中性 |  |
| country_amenability_add | 国家顺从度 | 加法 | 良好 |  |
| country_aristocrats_pol_str_mult | 贵族的政治力量 | 乘法 | 百分比，中性 |  |
| country_aristocrats_voting_power_add | 贵族选票带来的政治力量 | 加法 | 中性 | 基于对象 启用选举 |
| country_assimilation_cultural_erasure_mult | “文化抹除”状态的同化 | 乘法 | 百分比，中性 |  |
| country_assimilation_delta_threshold_add | 文化同化阈值 | 加法 | 良好 |  |
| country_assimilation_full_acceptance_mult | “完全接纳”状态的同化 | 乘法 | 百分比，中性 |  |
| country_assimilation_open_prejudice_mult | “公开偏见”状态的同化 | 乘法 | 百分比，中性 |  |
| country_assimilation_second_rate_citizen_mult | “二等公民”状态的同化 | 乘法 | 百分比，中性 |  |
| country_assimilation_violent_hostility_mult | “激烈敌意”状态的同化 | 乘法 | 百分比，中性 |  |
| country_authority_add | 权威力 | 加法 | 良好 |  |
| country_authority_cost_add | 权威力消耗 | 加法 | 有害 |  |
| country_authority_mult | 权威力 | 乘法 | 百分比，良好 |  |
| country_authority_per_subject_add | 每个附属国提供的权威力 | 加法 | 良好 |  |
| country_bg_manufacturing_require_subsidies_bool | 制造业强制补贴 | 布尔值 | 有害 |  |
| country_block_government_reform_bool | 阻止政府改革 | 布尔值 | 中性 |  |
| country_bolster_attraction_factor | 扶持对政治运动吸引力的加成 | 乘法 | 百分比，中性 |  |
| country_bolster_cost_mult | 扶持消耗 | 乘法 | 百分比，有害 |  |
| country_brahmins_acceptance_min_add | 婆罗门社会阶层的最低接纳度 | 加法 | 良好 |  |
| country_brahmins_qualification_growth_other_class_mult | 婆罗门在婆罗门社会阶层以外的资质增长 | 乘法 | 百分比，良好 |  |
| country_brahmins_qualification_growth_same_class_mult | 婆罗门社会阶层内部的资质增长 | 乘法 | 百分比，良好 |  |
| country_bureaucracy_add | 行政力 | 加法 | 良好 |  |
| country_bureaucracy_cost_add | 行政力消耗 | 加法 | 有害 |  |
| country_bureaucracy_investment_cost_factor_mult | 行政力机构成本倍率 | 乘法 | 百分比，有害 |  |
| country_bureaucracy_mult | 行政力 | 乘法 | 百分比，良好 |  |
| country_bureaucrats_pol_str_mult | 官僚的政治力量 | 乘法 | 百分比，中性 |  |
| country_bureaucrats_voting_power_add | 官僚选票带来的政治力量 | 加法 | 中性 | 基于对象 启用选举 |
| country_can_form_construction_company_bool | 可成立建筑类公司 | 布尔值 | 中性 |  |
| country_can_impose_same_lawgroup_army_model_in_power_bloc_bool | **强制**集团成员采用相同陆军模式法律 | 布尔值 | 良好 |  |
| country_can_impose_same_lawgroup_church_and_state_in_power_bloc_bool | **强制**集团成员采用相同政教关系法律 | 布尔值 | 良好 |  |
| country_can_impose_same_lawgroup_citizenship_in_power_bloc_bool | **强制**集团成员采用相同公民权法律 | 布尔值 | 良好 |  |
| country_can_impose_same_lawgroup_colonization_in_power_bloc_bool | **强制**集团成员采用相同殖民法律 | 布尔值 | 良好 |  |
| country_can_impose_same_lawgroup_distribution_of_power_in_power_bloc_bool | **强制**集团成员采用相同权力分配法律 | 布尔值 | 良好 |  |
| country_can_impose_same_lawgroup_education_system_in_power_bloc_bool | **强制**集团成员采用相同教育体制法律 | 布尔值 | 良好 |  |
| country_can_impose_same_lawgroup_governance_principles_in_power_bloc_bool | **强制**集团成员采用相同治理原则法律 | 布尔值 | 良好 |  |
| country_can_impose_same_lawgroup_policing_in_power_bloc_bool | **强制**集团成员采用相同治安法律 | 布尔值 | 良好 |  |
| country_can_only_conscript_peasants_bool | 仅允许征召步兵营 | 布尔值 | 良好 |  |
| country_cannot_be_subjugated_bool | 不能被臣属 | 布尔值 | 中性 |  |
| country_cannot_be_target_for_law_imposition_bool | 不能成为法律强制的目标 | 布尔值 | 良好 |  |
| country_cannot_cancel_law_enactment_bool | 禁止}} 取消法律颁布 | 布尔值 | 有害 |  |
| country_cannot_enact_laws_bool | 禁止}} 颁布法律 | 布尔值 | 有害 |  |
| country_cannot_join_power_bloc_bool | 不能加入强权集团 | 布尔值 | 中性 |  |
| country_cannot_start_law_enactment_bool | 禁止}} 开始法律颁布 | 布尔值 | 有害 |  |
| country_capitalists_pol_str_mult | 资本家的政治力量 | 乘法 | 百分比，中性 |  |
| country_capitalists_voting_power_add | 资本家选票带来的政治力量 | 加法 | 中性 | 基于对象 启用选举 |
| country_clergymen_pol_str_mult | 神职人员的政治力量 | 乘法 | 百分比，中性 |  |
| country_clergymen_voting_power_add | 神职人员选票带来的政治力量 | 加法 | 中性 | 基于对象 启用选举 |
| country_clerks_pol_str_mult | 职员的政治力量 | 乘法 | 百分比，中性 |  |
| country_clerks_voting_power_add | 职员选票带来的政治力量 | 加法 | 中性 | 基于对象 启用选举 |
| country_company_construction_efficiency_bonus_add | 公司建筑加成 | 加法 | 百分比，良好 |  |
| country_company_throughput_bonus_add | 公司吞吐量加成 | 加法 | 百分比，良好 |  |
| country_construction_add | 建造力 | 加法 | 良好 |  |
| country_construction_goods_cost_mult | 建造商品成本 | 乘法 | 百分比，有害 |  |
| country_consumption_tax_cost_mult | 消费税成本 | 乘法 | 百分比，有害 |  |
| country_conversion_delta_threshold_add | 宗教皈依阈值 | 加法 | 良好 |  |
| country_coup_resistance_add | 政变抗性 | 加法 | 中性 |  |
| country_coup_resistance_mult | 政变抗性 | 乘法 | 百分比，中性 |  |
| country_dalit_acceptance_max_add | 达利特社会阶层的最高接纳度 | 加法 | 有害 |  |
| country_dalit_cultural_acceptance_mult | 达利特社会阶层的文化接纳度 | 乘法 | 百分比，良好 |  |
| country_dalit_education_access_add | 达利特社会阶层的教育机会 | 加法 | 良好 |  |
| country_dalit_education_access_mult | 达利特社会阶层的教育机会 | 乘法 | 百分比，良好 |  |
| country_dalit_qualification_growth_add | 达利特社会阶层的资质增长 | 加法 | 良好 |  |
| country_dalit_qualification_growth_mult | 达利特社会阶层的资质增长 | 乘法 | 百分比，良好 |  |
| country_dalit_qualification_growth_other_class_mult | 达利特在达利特社会阶层以外的资质增长 | 乘法 | 百分比，良好 |  |
| country_dalit_qualification_growth_same_class_mult | 达利特社会阶层内部的资质增长 | 乘法 | 百分比，良好 |  |
| country_damage_relations_speed_mult | 损害关系速度 | 乘法 | 百分比，良好 |  |
| country_diplomatic_play_maneuvers_add | 每次外交博弈的博弈点数 | 加法 | 良好 |  |
| country_diplomatic_play_maneuvers_mult | 每次外交博弈的博弈点数 | 乘法 | 百分比，良好 |  |
| country_diplomatic_reputation_add | 外交声誉 | 加法 | 良好 |  |
| country_disable_investment_pool_bool | 禁用投资池（公司除外） | 布尔值 | 有害 |  |
| country_disable_nationalization_bool | 禁用国有化 | 布尔值 | 有害 |  |
| country_disable_nationalization_without_compensation_bool | 禁用无补偿国有化 | 布尔值 | 有害 |  |
| country_disable_non_company_privatization_bool | 禁用私有化（公司除外） | 布尔值 | 有害 |  |
| country_disallow_aggressive_plays_bool | 禁止侵略性外交博弈 | 布尔值 | 中性 |  |
| country_disallow_agitator_invites_bool | 禁止邀请流亡者 | 布尔值 | 中性 |  |
| country_disallow_government_work_cultural_erasure_bool | 禁止“文化抹除”状态的上层与中层阶层在政府建筑工作 | 布尔值 | 中性 |  |
| country_disallow_government_work_full_acceptance_bool | 禁止“完全接纳”状态的上层与中层阶层在政府建筑工作 | 布尔值 | 中性 |  |
| country_disallow_government_work_open_prejudice_bool | 禁止“公开偏见”状态的上层与中层阶层在政府建筑工作 | 布尔值 | 中性 |  |
| country_disallow_government_work_second_rate_citizen_bool | 禁止“二等公民”状态的上层与中层阶层在政府建筑工作 | 布尔值 | 中性 |  |
| country_disallow_government_work_violent_hostility_bool | 禁止“激烈敌意”状态的上层与中层阶层在政府建筑工作 | 布尔值 | 中性 |  |
| country_disallow_law_no_colonial_affairs_bool | 禁止“无殖民事务”法律 | 布尔值 | 有害 |  |
| country_disallow_law_no_police_bool | 禁止“无警察”法律 | 布尔值 | 有害 |  |
| country_disallow_law_no_schools_bool | 禁止“无学校”法律 | 布尔值 | 有害 |  |
| country_disallow_military_work_cultural_erasure_bool | 禁止“文化抹除”状态的人口在军事建筑工作 | 布尔值 | 中性 |  |
| country_disallow_military_work_full_acceptance_bool | 禁止“完全接纳”状态的人口在军事建筑工作 | 布尔值 | 中性 |  |
| country_disallow_military_work_open_prejudice_bool | 禁止“公开偏见”状态的人口在军事建筑工作 | 布尔值 | 中性 |  |
| country_disallow_military_work_second_rate_citizen_bool | 禁止“二等公民”状态的人口在军事建筑工作 | 布尔值 | 中性 |  |
| country_disallow_military_work_violent_hostility_bool | 禁止“激烈敌意”状态的人口在军事建筑工作 | 布尔值 | 中性 |  |
| country_disallow_trade_bool | 禁用贸易中心 | 布尔值 | 有害 |  |
| country_disallow_trade_outside_canton_bool | 禁用广东以外地区的贸易中心 | 布尔值 | 有害 | 仅限脚本 |
| country_disallow_trade_outside_kyushu_bool | 禁用九州以外地区的贸易中心 | 布尔值 | 有害 |  |
| country_economic_dependence_on_overlord_add | 对宗主国的经济依附 | 加法 | 有害 |  |
| country_education_fervor_add | 教育机构狂热度 | 加法 | 中性 |  |
| country_electoral_confidence_impact_mult | 选举信心影响 | 乘法 | 百分比，中性 |  |
| country_electoral_confidence_over_time | 每月选举信心变化 |  | 百分比，良好 |  |
| country_enactment_speed_law_anarchy_mult | country_enactment_speed_law_anarchy_mult | 乘法 | 百分比，良好 |  |
| country_enactment_speed_law_autocracy_mult | country_enactment_speed_law_autocracy_mult | 乘法 | 百分比，良好 |  |
| country_enactment_speed_law_oligarchy_mult | country_enactment_speed_law_oligarchy_mult | 乘法 | 百分比，良好 |  |
| country_enactment_speed_law_public_schools_mult | 公立学校的颁布速度 | 乘法 | 百分比，良好 |  |
| country_enactment_speed_law_single_party_state_mult | country_enactment_speed_law_single_party_state_mult | 乘法 | 百分比，良好 |  |
| country_enactment_speed_law_technocracy_mult | 技术官僚制的颁布速度 | 乘法 | 百分比，良好 |  |
| country_enactment_success_chance_law_anarchy_add | 无政府状态的颁布成功几率 | 加法 | 百分比，良好 |  |
| country_enactment_success_chance_law_autocracy_add | 独裁制的颁布成功几率 | 加法 | 百分比，良好 |  |
| country_enactment_success_chance_law_oligarchy_add | 寡头制的颁布成功几率 | 加法 | 百分比，良好 |  |
| country_enactment_success_chance_law_public_schools_add | 公立学校的颁布成功几率 | 加法 | 百分比，良好 |  |
| country_enactment_success_chance_law_single_party_state_add | 一党制国家的颁布成功几率 | 加法 | 百分比，良好 |  |
| country_enactment_success_chance_law_technocracy_add | 技术官僚制的颁布成功几率 | 加法 | 百分比，良好 |  |
| country_engineers_pol_str_mult | 工程师的政治力量 | 乘法 | 百分比，中性 |  |
| country_engineers_voting_power_add | 工程师选票带来的政治力量 | 加法 | 中性 | 基于对象 启用选举 |
| country_expedition_events_explorer_mult | 远征机会 | 乘法 | 百分比，良好 |  |
| country_expenses_add | 政府开支 | 加法 | 有害 |  |
| country_farmers_pol_str_mult | 农场主的政治力量 | 乘法 | 百分比，中性 |  |
| country_farmers_voting_power_add | 农场主选票带来的政治力量 | 加法 | 中性 | 基于对象 启用选举 |
| country_financial_districts_buy_farms_likelihood | 金融区对种植园、牧场和农业的投资 |  | 百分比，良好 |  |
| country_flagship_interest_gain_mult | 旗舰参与度增长 | 乘法 | 百分比，良好 |  |
| country_forbid_electoral_fraud_bool | 禁止选举舞弊 | 布尔值 | 中性 |  |
| country_forbid_monopoly_bool | 禁止垄断 | 布尔值 | 有害 |  |
| country_force_privatization_bool | 强制私有化 | 布尔值 | 中性 |  |
| country_foreign_collectivization_bool | 外国集体化 | 布尔值 | 中性 |  |
| country_frankenstein_company_bool | 实验性模块可运行 | 布尔值 | 中性 |  |
| country_free_charters_add | 免费公司特许状 | 加法 | 良好 |  |
| country_general_rank_impact_mult | 将领军衔影响 | 乘法 | 百分比，良好 |  |
| country_gold_reserve_limit_mult | 黄金储备上限 | 乘法 | 百分比，良好 |  |
| country_government_buildings_protected_bool | 禁止缩减政府建筑 | 布尔值 | 有害 |  |
| country_government_dividends_efficiency_add | 政府分红效率 | 加法 | 百分比，良好 |  |
| country_government_dividends_reinvestment_add | 政府分红再投资 | 加法 | 百分比，中性 |  |
| country_government_dividends_waste_add | 政府分红浪费 | 加法 | 百分比，有害 |  |
| country_government_wages_mult | 政府工资 | 乘法 | 百分比，中性 |  |
| country_higher_diplomatic_acceptance_same_religion_bool | 对相同宗教国家更高的外交提案接受度 | 布尔值 | 良好 |  |
| country_higher_leverage_from_economic_dependence_bool | 提升来自经济依附的影响力筹码 | 布尔值 | 良好 |  |
| country_improve_relations_speed_mult | 改善关系速度 | 乘法 | 百分比，良好 |  |
| country_infamy_decay_mult | 恶名衰减 | 乘法 | 百分比，良好 |  |
| country_infamy_generation_against_unrecognized_mult | 对未开化政权的恶名产生 | 乘法 | 百分比，有害 |  |
| country_infamy_generation_mult | 恶名产生 | 乘法 | 百分比，有害 |  |
| country_influence_add | 影响力 | 加法 | 良好 |  |
| country_influence_cost_add | 影响力消耗 | 加法 | 有害 |  |
| country_influence_mult | 影响力 | 乘法 | 百分比，良好 |  |
| country_initiator_war_goal_maneuver_cost_mult | 外交博弈发起者的战争目标博弈点数消耗 | 乘法 | 百分比，有害 |  |
| country_institution_colonial_affairs_max_investment_add | 殖民事务机构最大投入 | 加法 | 良好 |  |
| country_institution_cost_institution_colonial_affairs_mult | 殖民事务的行政力成本 | 乘法 | 百分比，有害 |  |
| country_institution_cost_institution_health_system_mult | 卫生系统的行政力成本 | 乘法 | 百分比，有害 |  |
| country_institution_cost_institution_home_affairs_mult | 内政的行政力成本 | 乘法 | 百分比，有害 |  |
| country_institution_cost_institution_police_mult | 执法的行政力成本 | 乘法 | 百分比，有害 |  |
| country_institution_cost_institution_schools_mult | 教育的行政力成本 | 乘法 | 百分比，有害 |  |
| country_institution_cost_institution_social_security_mult | 社会保障的行政力成本 | 乘法 | 百分比，有害 |  |
| country_institution_health_system_max_investment_add | 卫生系统机构最大投入 | 加法 | 良好 |  |
| country_institution_home_affairs_max_investment_add | 内政机构最大投资 | additive | good |  |
| country_institution_impact_institution_health_system_mult | 医疗系统的影响 | multiplicative | percent, good |  |
| country_institution_police_max_investment_add | 执法机构最大投资 | additive | good |  |
| country_institution_schools_max_investment_add | 教育机构最大投资 | additive | good |  |
| country_institution_size_change_speed_institution_colonial_affairs_mult | 殖民事务的机构规模变化速度 | multiplicative | percent, good |  |
| country_institution_size_change_speed_institution_police_mult | 执法的机构规模变化速度 | multiplicative | percent, good |  |
| country_institution_size_change_speed_institution_schools_mult | 教育的机构规模变化速度 | multiplicative | percent, good |  |
| country_institution_size_change_speed_mult | 机构规模变化速度 | multiplicative | percent, good |  |
| country_institution_social_security_max_investment_add | 社会保障机构最大投资 | additive | good |  |
| country_institution_workplace_safety_max_investment_add | 劳动安全局机构最大投资 | additive | good |  |
| country_je_korea_action_cost | country_je_korea_action_cost |  | percent, bad |  |
| country_join_power_bloc_member_in_defensive_plays_bool | 可在**防御性**外交博弈中通过召集盟友拉拢强权集团成员 | boolean | neutral |  |
| country_join_power_bloc_member_in_plays_bool | 可在**所有**外交博弈中通过召集盟友拉拢强权集团成员 | boolean | neutral |  |
| country_kshatriyas_acceptance_max_add | 刹帝利社会阶层的接受度上限 | additive | bad |  |
| country_kshatriyas_acceptance_min_add | 刹帝利社会阶层的接受度下限 | additive | good |  |
| country_kshatriyas_cultural_acceptance_mult | 刹帝利社会阶层的文化接受度 | multiplicative | percent, good |  |
| country_kshatriyas_education_access_add | 刹帝利社会阶层的教育机会 | additive | good |  |
| country_kshatriyas_education_access_mult | 刹帝利社会阶层的教育机会 | multiplicative | percent, good |  |
| country_kshatriyas_qualification_growth_add | 刹帝利社会阶层的资质增长 | additive | good |  |
| country_kshatriyas_qualification_growth_mult | 刹帝利社会阶层的资质增长 | multiplicative | percent, good |  |
| country_kshatriyas_qualification_growth_other_class_mult | 刹帝利在其他社会阶层的资质增长 | multiplicative | percent, good |  |
| country_kshatriyas_qualification_growth_same_class_mult | 刹帝利社会阶层内部的资质增长 | multiplicative | percent, good |  |
| country_laborers_pol_str_mult | 劳工的政治力量 | multiplicative | percent, neutral |  |
| country_laborers_voting_power_add | 来自劳工选票的政治力量 | additive | neutral | Object-based Enables elections |
| country_law_enactment_imposition_success_add | 强加法律的通过成功率 | additive | percent, good |  |
| country_law_enactment_max_setbacks_add | 法律制定最大挫折次数 | additive | good |  |
| country_law_enactment_speed_mult | 法律制定速度 | multiplicative | percent, good |  |
| country_law_enactment_stall_add | 法律停滞几率 | additive | percent, bad |  |
| country_law_enactment_stall_mult | 法律停滞几率 | multiplicative | percent, bad |  |
| country_law_enactment_success_add | 法律通过成功率 | additive | percent, good |  |
| country_leader_has_law_enactment_success_mult | 强权集团法律协同 | multiplicative | percent, good |  |
| country_legitimacy_base_add | 合法性 | additive | good |  |
| country_legitimacy_govt_leader_clout_add | 基于政府领导人政治力量的合法性 | additive | good |  |
| country_legitimacy_govt_size_add | 政府规模上限 | additive | good |  |
| country_legitimacy_govt_total_clout_add | 基于政府政治力量的合法性 | additive | good |  |
| country_legitimacy_govt_total_votes_add | 基于选票的合法性 | additive | good |  |
| country_legitimacy_headofstate_add | 国家元首加入政府带来的合法性 | additive | good |  |
| country_legitimacy_ideological_incoherence_mult | 意识形态不兼容带来的合法性惩罚 | multiplicative | percent, bad |  |
| country_legitimacy_min_add | 最低合法性 | additive | neutral |  |
| country_leverage_generation_add | 影响力杠杆获取 | additive | good |  |
| country_leverage_generation_mult | 影响力杠杆获取 | multiplicative | percent, good |  |
| country_leverage_resistance_add | 影响力杠杆抗性 | additive | neutral |  |
| country_leverage_resistance_mult | 影响力杠杆抗性 | multiplicative | percent, neutral |  |
| country_liberty_desire_add | 每周独立倾向 | additive | neutral |  |
| country_liberty_desire_decrease_mult | 每周独立倾向下降 | multiplicative | percent, neutral |  |
| country_liberty_desire_increase_mult | 每周独立倾向上升 | multiplicative | percent, neutral |  |
| country_liberty_desire_of_subjects_add | 所有附属国的每周独立倾向 | additive | neutral |  |
| country_limit_officers_qualifications_to_upper_strata | 军官资质仅限上层阶层 | boolean | neutral |  |
| country_loan_interest_rate_add | 贷款利率 | additive | percent, bad |  |
| country_loan_interest_rate_mult | 贷款利率 | multiplicative | percent, bad |  |
| country_lobby_leverage_generation_mult | 来自政治游说集团的影响力杠杆获取 | multiplicative | percent, good |  |
| country_lobby_support | 游说集团支持 |  | good |  |
| country_loyalism_increases_cultural_erasure_mult | 文化抹除状态下忠诚派的增长 | multiplicative | percent, good |  |
| country_loyalism_increases_full_acceptance_mult | 完全接纳状态下忠诚派的增长 | multiplicative | percent, good |  |
| country_loyalism_increases_open_prejudice_mult | 公开偏见状态下忠诚派的增长 | multiplicative | percent, good |  |
| country_loyalism_increases_second_rate_citizen_mult | 二等公民状态下忠诚派的增长 | multiplicative | percent, good |  |
| country_loyalism_increases_violent_hostility_mult | 暴力敌视状态下忠诚派的增长 | multiplicative | percent, good |  |
| country_loyalists_from_legitimacy_mult | 高合法性带来的忠诚派 | multiplicative | percent, good |  |
| country_machinists_pol_str_mult | 机械师的政治力量 | multiplicative | percent, neutral |  |
| country_machinists_voting_power_add | 来自机械师选票的政治力量 | additive | neutral | Object-based Enables elections |
| country_mass_migration_attraction_mult | 大规模迁移吸引力 | multiplicative | percent, good |  |
| country_max_companies_add | 公司数量上限 | additive | good |  |
| country_max_unassigned_admirals_add | 闲置海军上将上限 | additive | good |  |
| country_max_unassigned_generals_add | 闲置将军上限 | additive | good |  |
| country_max_weekly_construction_progress_add | 每周最大建造进度 | additive | good |  |
| country_migration_restrictiveness_add | 迁移限制程度 | additive | neutral |  |
| country_military_goods_cost_mult | 军用商品成本 | multiplicative | percent, bad |  |
| country_military_tech_research_speed_mult | 军事研究速度 | multiplicative | percent, good |  |
| country_military_tech_spread_mult | 军事技术扩散 | multiplicative | percent, good |  |
| country_military_wages_mult | 军队工资 | multiplicative | percent, neutral |  |
| country_minting_add | 铸币 | additive | good |  |
| country_minting_mult | 铸币 | multiplicative | percent, good |  |
| country_must_have_movement_to_enact_laws_bool | 制定法律必须有政治运动 | boolean | bad |  |
| country_nationalization_cost_non_members_mult | 国有化成本 | multiplicative | percent, bad |  |
| country_navy_goods_cost_mult | 海军商品成本 | multiplicative | percent, bad |  |
| country_no_advantage_loss_from_lack_of_interest_bool | 无视因缺少利益带来的贸易优势惩罚 | boolean | good |  |
| country_non_state_religion_wages_mult | 非国教人口的工资 | multiplicative | percent, neutral |  |
| country_officers_pol_str_mult | 军官的政治力量 | multiplicative | percent, neutral |  |
| country_officers_voting_power_add | 来自军官选票的政治力量 | additive | neutral | Object-based Enables elections |
| country_opposition_ig_approval_add | 反对党利益集团支持度 | additive | good |  |
| country_overlord_income_transfer_mult | 宗主国收入转移 | multiplicative | percent, bad |  |
| country_pact_leverage_generation_add | 来自外交协定的影响力杠杆获取 | additive | good |  |
| country_pact_leverage_generation_mult | 来自外交协定的影响力杠杆获取 | multiplicative | percent, good |  |
| country_party_whip_impact_add | 政党党鞭对意识形态不协调的影响 | additive | percent, good |  |
| country_peasants_pol_str_mult | 农民的政治力量 | multiplicative | percent, neutral |  |
| country_peasants_voting_power_add | 来自农民选票的政治力量 | additive | neutral | Object-based Enables elections |
| country_piracy_income_add | 海盗收入 | additive | percent, good |  |
| country_political_strength_cultural_erasure_mult | 文化抹除状态下的政治力量 | multiplicative | percent, good |  |
| country_political_strength_full_acceptance_mult | 完全接纳状态下的政治力量 | multiplicative | percent, good |  |
| country_political_strength_open_prejudice_mult | 公开偏见状态下的政治力量 | multiplicative | percent, good |  |
| country_political_strength_second_rate_citizen_mult | 二等公民状态下的政治力量 | multiplicative | percent, good |  |
| country_political_strength_violent_hostility_mult | 暴力敌视状态下的政治力量 | multiplicative | percent, good |  |
| country_port_connection_cost_mult | 港口连接的商船队成本 | multiplicative | percent, bad |  |
| country_prestige_add | 威望 | additive | good |  |
| country_prestige_from_army_power_projection_mult | 来自陆军力量投射的威望 | multiplicative | percent, good |  |
| country_prestige_from_navy_power_projection_mult | 来自海军力量投射的威望 | multiplicative | percent, good |  |
| country_prestige_mult | 威望 | multiplicative | percent, good |  |
| country_primary_culture_fervor_from_laws_add | 法律带来的主流文化热忱 | additive | neutral |  |
| country_private_construction_allocation_mult | 私人建造分配 | multiplicative | percent, neutral |  |
| country_production_tech_research_speed_mult | 生产研究速度 | multiplicative | percent, good |  |
| country_production_tech_spread_mult | 生产技术扩散 | multiplicative | percent, good |  |
| country_qualification_growth_cultural_erasure_mult | 文化抹除状态下的资质提升 | multiplicative | percent, good |  |
| country_qualification_growth_full_acceptance_mult | 完全接纳状态下的资质提升 | multiplicative | percent, good |  |
| country_qualification_growth_open_prejudice_mult | 公开偏见状态下的资质提升 | multiplicative | percent, good |  |
| country_qualification_growth_second_rate_citizen_mult | 二等公民状态下的资质提升 | multiplicative | percent, good |  |
| country_qualification_growth_violent_hostility_mult | 暴力敌视状态下的资质提升 | multiplicative | percent, good |  |
| country_radicalism_increases_cultural_erasure_mult | 文化抹除状态下激进派的增长 | multiplicative | percent, bad |  |
| country_radicalism_increases_full_acceptance_mult | 完全接纳状态下激进派的增长 | multiplicative | percent, bad |  |
| country_radicalism_increases_open_prejudice_mult | 公开偏见状态下激进派的增长 | multiplicative | percent, bad |  |
| country_radicalism_increases_second_rate_citizen_mult | 二等公民状态下激进派的增长 | multiplicative | percent, bad |  |
| country_radicalism_increases_violent_hostility_mult | 暴力敌视状态下激进派的增长 | multiplicative | percent, bad |  |
| country_radicals_from_conquest_mult | 征服带来的激进派 | multiplicative | percent, bad |  |
| country_radicals_from_legitimacy_mult | 低合法性带来的激进派 | multiplicative | percent, bad |  |
| country_reduced_liberty_desire_same_religion_bool | 同宗教独立倾向降低 | boolean | good |  |
| country_resource_depletion_chance_mult | 资源枯竭几率 | multiplicative | percent, bad |  |
| country_resource_discovery_chance_mult | 资源发现几率 | multiplicative | percent, good |  |
| country_revolution_clock_time_add | 革命时钟时间 | additive | neutral |  |
| country_revolution_progress_add | 革命进展速度 | additive | percent, bad |  |
| country_revolution_progress_mult | 革命进展速度 | multiplicative | percent, bad |  |
| country_sailors_max_add | 水手上限 | additive | good |  |
| country_secession_clock_time_add | 脱离时钟时间 | additive | neutral |  |
| country_secession_progress_add | 脱离进展速度 | additive | percent, bad |  |
| country_secession_progress_mult | 脱离进展速度 | multiplicative | percent, bad |  |
| country_ship_construction_add | 舰船建造 | additive | good |  |
| country_ship_construction_efficiency_add | 舰船建造效率 | additive | percent, good |  |
| country_ship_construction_goods_cost_mult | 舰船建造成本 | multiplicative | percent, bad |  |
| country_ship_construction_progress_max_add | 舰船最大建造进度 | additive | good |  |
| country_ship_crew_starting_veterancy_experience_add | 舰船船员初始经验 | additive | good |  |
| country_ship_crew_starting_veterancy_experience_mult | 舰船船员初始经验 | multiplicative | percent, good |  |
| country_ship_group_capital_ships_construction_efficiency_add | 主力舰建造效率 | additive | percent, good |  |
| country_ship_group_capital_ships_construction_progress_max_add | 主力舰最大建造进度 | additive | good |  |
| country_ship_group_capital_ships_construction_progress_max_mult | 主力舰最大建造进度 | multiplicative | percent, good |  |
| country_ship_group_cruisers_construction_efficiency_add | 巡洋舰建造效率 | additive | percent, good |  |
| country_ship_group_cruisers_construction_progress_max_add | 巡洋舰最大建造进度 | additive | good |  |
| country_ship_group_cruisers_construction_progress_max_mult | 巡洋舰最大建造进度 | multiplicative | percent, good |  |
| country_ship_group_supply_ships_construction_efficiency_add | 补给舰建造效率 | additive | percent, good |  |
| country_ship_group_torpedo_craft_construction_efficiency_add | 雷击舰建造效率 | additive | percent, good |  |
| country_ship_group_torpedo_craft_construction_progress_max_add | 雷击舰最大建造进度 | additive | good |  |
| country_ship_group_torpedo_craft_construction_progress_max_mult | 雷击舰最大建造进度 | multiplicative | percent, good |  |
| country_ship_type_armored_cruiser_construction_efficiency_add | 装甲巡洋舰建造效率 | additive | percent, good |  |
| country_ship_type_light_cruiser_construction_efficiency_add | 轻巡洋舰建造效率 | additive | percent, good |  |
| country_ship_type_protected_cruiser_construction_efficiency_add | 防护巡洋舰建造效率 | additive | percent, good |  |
| country_ship_type_troop_ship_construction_efficiency_add | 运兵船建造效率 | additive | percent, good |  |
| country_shopkeepers_pol_str_mult | 店主的政治力量 | multiplicative | percent, neutral |  |
| country_shopkeepers_voting_power_add | 来自店主选票的政治力量 | additive | neutral | Object-based Enables elections |
| country_shudras_acceptance_max_add | 首陀罗社会阶层的接受度上限 | additive | bad |  |
| country_shudras_cultural_acceptance_mult | 首陀罗社会阶层的文化接受度 | multiplicative | percent, good |  |
| country_shudras_education_access_add | 首陀罗社会阶层的教育机会 | additive | good |  |
| country_shudras_education_access_mult | 首陀罗社会阶层的教育机会 | multiplicative | percent, good |  |
| country_shudras_qualification_growth_add | 首陀罗社会阶层的资质增长 | additive | good |  |
| country_shudras_qualification_growth_mult | 首陀罗社会阶层的资质增长 | multiplicative | percent, good |  |
| country_shudras_qualification_growth_other_class_mult | 首陀罗在其他社会阶层的资质增长 | multiplicative | percent, good |  |
| country_shudras_qualification_growth_same_class_mult | 首陀罗社会阶层内部的资质增长 | multiplicative | percent, good |  |
| country_slaves_voting_power_add | 来自奴隶选票的政治力量 | additive | neutral | Object-based Enables elections |
| country_society_tech_research_speed_mult | 社会研究速度 | multiplicative | percent, good |  |
| country_society_tech_spread_mult | 社会技术扩散 | multiplicative | percent, good |  |
| country_soldiers_pol_str_mult | 军人的政治力量 | multiplicative | percent, neutral |  |
| country_soldiers_voting_power_add | 来自军人选票的政治力量 | additive | neutral | Object-based Enables elections |
| country_standard_of_living_cultural_erasure_add | 文化抹除状态下的生活水平 | additive | good |  |
| country_standard_of_living_full_acceptance_add | 完全接纳状态下的生活水平 | additive | good |  |
| country_standard_of_living_open_prejudice_add | 公开偏见状态下的生活水平 | additive | good |  |
| country_standard_of_living_second_rate_citizen_add | 二等公民状态下的生活水平 | additive | good |  |
| country_standard_of_living_violent_hostility_add | 暴力敌视状态下的生活水平 | additive | good |  |
| country_state_religion_wages_mult | 国教人口的工资 | multiplicative | percent, neutral |  |
| country_strata_commoners_peasants_acceptance_max_add | 百姓（农民）社会阶层的接受度上限 | additive | bad |  |
| country_strata_commoners_peasants_acceptance_min_add | 百姓（农民）社会阶层的接受度下限 | additive | good |  |
| country_strata_commoners_peasants_cultural_acceptance_mult | 百姓（农民）社会阶层的文化接受度 | multiplicative | percent, good |  |
| country_strata_commoners_peasants_education_access_add | 百姓（农民）社会阶层的教育机会 | additive | good |  |
| country_strata_commoners_peasants_education_access_mult | 百姓（农民）社会阶层的教育机会 | multiplicative | percent, good |  |
| country_strata_commoners_peasants_qualification_growth_add | 百姓（农民）社会阶层的资质增长 | additive | good |  |
| country_strata_commoners_peasants_qualification_growth_mult | 百姓（农民）社会阶层的资质增长 | multiplicative | percent, good |  |
| country_strata_commoners_peasants_qualification_growth_other_class_mult | 百姓（农民）在其他社会阶层的资质增长 | multiplicative | percent, good |  |
| country_strata_commoners_peasants_qualification_growth_same_class_mult | 百姓（农民）社会阶层内部的资质增长 | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_acceptance_max_add | 町人社会阶层的接受度上限 | additive | bad |  |
| country_strata_commoners_townspeople_acceptance_min_add | 町人社会阶层的接受度下限 | additive | good |  |
| country_strata_commoners_townspeople_cultural_acceptance_mult | 町人社会阶层的文化接受度 | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_education_access_add | 町人社会阶层的教育机会 | additive | good |  |
| country_strata_commoners_townspeople_education_access_mult | 町人社会阶层的教育机会 | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_qualification_growth_add | 町人社会阶层的资质增长 | additive | good |  |
| country_strata_commoners_townspeople_qualification_growth_mult | 町人社会阶层的资质增长 | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_qualification_growth_other_class_mult | 町人在其他社会阶层的资质增长 | multiplicative | percent, good |  |
| country_strata_commoners_townspeople_qualification_growth_same_class_mult | 町人社会阶层内部的资质增长 | multiplicative | percent, good |  |
| country_strata_outcastes_acceptance_max_add | 秽非社会阶层的接受度上限 | additive | bad |  |
| country_strata_outcastes_acceptance_min_add | 秽非社会阶层的接受度下限 | additive | good |  |
| country_strata_outcastes_cultural_acceptance_mult | 秽非社会阶层的文化接受度 | multiplicative | percent, good |  |
| country_strata_outcastes_education_access_add | 秽非社会阶层的教育机会 | additive | good |  |
| country_strata_outcastes_education_access_mult | 秽非社会阶层的教育机会 | multiplicative | percent, good |  |
| country_strata_outcastes_qualification_growth_add | 秽非社会阶层的资质增长 | additive | good |  |
| country_strata_outcastes_qualification_growth_mult | 秽非社会阶层的资质增长 | multiplicative | percent, good |  |
| country_strata_outcastes_qualification_growth_other_class_mult | 秽非在其他社会阶层的资质增长 | multiplicative | percent, good |  |
| country_strata_outcastes_qualification_growth_same_class_mult | 秽非社会阶层内部的资质增长 | multiplicative | percent, good |  |
| country_strata_religious_acceptance_max_add | 寺社社会阶层的接受度上限 | additive | bad |  |
| country_strata_religious_acceptance_min_add | 寺社社会阶层的接受度下限 | additive | good |  |
| country_strata_religious_cultural_acceptance_mult | 寺社社会阶层的文化接受度 | multiplicative | percent, good |  |
| country_strata_religious_education_access_add | 寺社社会阶层的教育机会 | additive | good |  |
| country_strata_religious_education_access_mult | 寺社社会阶层的教育机会 | multiplicative | percent, good |  |
| country_strata_religious_qualification_growth_add | 寺社社会阶层的资质增长 | additive | good |  |
| country_strata_religious_qualification_growth_mult | 寺社社会阶层的资质增长 | multiplicative | percent, good |  |
| country_strata_religious_qualification_growth_other_class_mult | 寺社在其他社会阶层的资质增长 | multiplicative | percent, good |  |
| country_strata_religious_qualification_growth_same_class_mult | 神职（Jisha）社会阶层内部的资质增长 | multiplicative | 百分比，有益 |  |
| country_strata_samurai_high_acceptance_max_add | 上级武士社会阶层的最大接纳度 | additive | 有害 |  |
| country_strata_samurai_high_acceptance_min_add | 上级武士社会阶层的最小接纳度 | additive | 有益 |  |
| country_strata_samurai_high_cultural_acceptance_mult | 上级武士社会阶层的文化接纳度 | multiplicative | 百分比，有益 |  |
| country_strata_samurai_high_education_access_add | 上级武士社会阶层的教育接入 | additive | 有益 |  |
| country_strata_samurai_high_education_access_mult | 上级武士社会阶层的教育接入 | multiplicative | 百分比，有益 |  |
| country_strata_samurai_high_qualification_growth_add | 上级武士社会阶层的资质增长 | additive | 有益 |  |
| country_strata_samurai_high_qualification_growth_mult | 上级武士社会阶层的资质增长 | multiplicative | 百分比，有益 |  |
| country_strata_samurai_high_qualification_growth_other_class_mult | 上级武士在上级武士社会阶层之外的资质增长 | multiplicative | 百分比，有益 |  |
| country_strata_samurai_high_qualification_growth_same_class_mult | 上级武士社会阶层内部的资质增长 | multiplicative | 百分比，有益 |  |
| country_strata_samurai_low_acceptance_max_add | 下级武士社会阶层的最大接纳度 | additive | 有害 |  |
| country_strata_samurai_low_acceptance_min_add | 下级武士社会阶层的最小接纳度 | additive | 有益 |  |
| country_strata_samurai_low_cultural_acceptance_mult | 下级武士社会阶层的文化接纳度 | multiplicative | 百分比，有益 |  |
| country_strata_samurai_low_education_access_add | 下级武士社会阶层的教育接入 | additive | 有益 |  |
| country_strata_samurai_low_education_access_mult | 下级武士社会阶层的教育接入 | multiplicative | 百分比，有益 |  |
| country_strata_samurai_low_qualification_growth_add | 下级武士社会阶层的资质增长 | additive | 有益 |  |
| country_strata_samurai_low_qualification_growth_mult | 下级武士社会阶层的资质增长 | multiplicative | 百分比，有益 |  |
| country_strata_samurai_low_qualification_growth_other_class_mult | 下级武士在下级武士社会阶层之外的资质增长 | multiplicative | 百分比，有益 |  |
| country_strata_samurai_low_qualification_growth_same_class_mult | 下级武士社会阶层内部的资质增长 | multiplicative | 百分比，有益 |  |
| country_subject_income_transfer_heathen_mult | 来自异教附属国的收入转移 | multiplicative | 百分比，有益 |  |
| country_subject_income_transfer_mult | 来自附属国的收入转移 | multiplicative | 百分比，有益 |  |
| country_supply_ship_construction_progress_max_add | 补给船最大建造进度 | additive | 有益 |  |
| country_supply_ship_construction_progress_max_mult | 补给船最大建造进度 | multiplicative | 百分比，有益 |  |
| country_supply_ship_construction_ratio_add | 补给船建造比例 | additive | 百分比，有益 |  |
| country_support_independence_weekly_liberty_desire_add | 支持独立的每周独立倾向 | additive | 中性 |  |
| country_support_separatism_resistance_mult | 分离主义抵抗支持度 | multiplicative | 百分比，有益 |  |
| country_support_separatism_strength_mult | 分离主义强度支持度 | multiplicative | 百分比，有益 |  |
| country_suppression_attraction_factor | 压制对政治运动吸引力的影响 | multiplicative | 百分比，有害 |  |
| country_suppression_cost_mult | 压制成本 | multiplicative | 百分比，有害 |  |
| country_tax_income_add | 税收收入 | additive | 有益 |  |
| country_tech_group_research_speed_mult | 集团的技术研究速度 | multiplicative | 百分比，有益 |  |
| country_tech_research_speed_mult | 技术研究速度 | multiplicative | 百分比，有益 |  |
| country_tech_spread_add | 技术扩散 | additive | 有益 |  |
| country_tech_spread_mult | 技术扩散 | multiplicative | 百分比，有益 |  |
| country_tension_decay_mult | 紧张度衰减 | multiplicative | 百分比，有益 |  |
| country_treaty_leverage_generation_add | 来自条约的影响力（Lverage）产生 | additive | 有益 |  |
| country_treaty_leverage_generation_mult | 来自条约的影响力产生 | multiplicative | 百分比，有益 |  |
| country_two_spains_conservative_drift_add | **两个西班牙**保守派进度 | additive | 有益 |  |
| country_two_spains_liberal_drift_add | **两个西班牙**自由派进度 | additive | 有益 |  |
| country_vaishyas_acceptance_max_add | 吠舍（Vaishyas）社会阶层的最大接纳度 | additive | 有害 |  |
| country_vaishyas_acceptance_min_add | 吠舍社会阶层的最小接纳度 | additive | 有益 |  |
| country_vaishyas_cultural_acceptance_mult | 吠舍社会阶层的文化接纳度 | multiplicative | 百分比，有益 |  |
| country_vaishyas_education_access_add | 吠舍社会阶层的教育接入 | additive | 有益 |  |
| country_vaishyas_education_access_mult | 吠舍社会阶层的教育接入 | multiplicative | 百分比，有益 |  |
| country_vaishyas_qualification_growth_add | 吠舍社会阶层的资质增长 | additive | 有益 |  |
| country_vaishyas_qualification_growth_mult | 吠舍社会阶层的资质增长 | multiplicative | 百分比，有益 |  |
| country_vaishyas_qualification_growth_other_class_mult | 吠舍在吠舍社会阶层之外的资质增长 | multiplicative | 百分比，有益 |  |
| country_vaishyas_qualification_growth_same_class_mult | 吠舍社会阶层内部的资质增长 | multiplicative | 百分比，有益 |  |
| country_voting_power_base_add | 每张选票的政治力量 | additive | 中性 | 硬编码 启用选举 |
| country_voting_power_cultural_erasure_mult | 文化灭绝状态下的政治力量投票贡献 | multiplicative | 百分比，中性 |  |
| country_voting_power_from_literacy_add | 来自有识字人口选票的政治力量 | additive | 中性 | 硬编码 启用选举 |
| country_voting_power_full_acceptance_mult | 完全接纳状态下的政治力量投票贡献 | multiplicative | 百分比，中性 |  |
| country_voting_power_mult | 每张选票的政治力量 | multiplicative | 百分比，中性 |  |
| country_voting_power_open_prejudice_mult | 公开偏见状态下的政治力量投票贡献 | multiplicative | 百分比，中性 |  |
| country_voting_power_second_rate_citizen_mult | 二等公民状态下的政治力量投票贡献 | multiplicative | 百分比，中性 |  |
| country_voting_power_violent_hostility_mult | 暴力敌意状态下的政治力量投票贡献 | multiplicative | 百分比，中性 |  |
| country_voting_power_wealth_threshold_add | 投票的财富门槛 | additive | 中性 | 硬编码 启用选举 |
| country_wage_cultural_erasure_mult | 文化灭绝状态下的工资 | multiplicative | 百分比，有益 |  |
| country_wage_full_acceptance_mult | 完全接纳状态下的工资 | multiplicative | 百分比，有益 |  |
| country_wage_open_prejudice_mult | 公开偏见状态下的工资 | multiplicative | 百分比，有益 |  |
| country_wage_second_rate_citizen_mult | 二等公民状态下的工资 | multiplicative | 百分比，有益 |  |
| country_wage_violent_hostility_mult | 暴力敌意状态下的工资 | multiplicative | 百分比，有益 |  |
| country_war_exhaustion_casualties_mult | 来自伤亡的厌战度 | multiplicative | 百分比，有害 |  |
| country_weekly_innovation_add | 创新 | additive | 有益 |  |
| country_weekly_innovation_max_add | 最大创新投入 | additive | 有益 |  |
| country_weekly_innovation_mult | 创新 | multiplicative | 百分比，有益 |  |
| country_yankee_and_dixie_cultures_obsessed_with_guns | 扬基与迪克西文化获得对轻武器的痴迷 | boolean | 中性 |  |

### 国家 GUI 脚本

主条目：
GUI 脚本
| 函数 | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessActiveDiplomaticPactTypes |  | Unknown | 类别：const |
| AccessActiveDiplomaticPacts | ContextualDiplomaticActionType | Unknown | 类别：const |
| AccessActiveDiplomaticPlays |  | Unknown | 类别：const |
| AccessActiveEconomyLaws |  | Unknown | 类别：const |
| AccessActiveHumanRightsLaws |  | Unknown | 类别：const |
| AccessActiveInterestGroups |  | Unknown | 类别：const |
| AccessActiveJournalEntries |  | Unknown | 类别：const |
| AccessActiveLawFromGroup | LawGroup | Law | 类别：const |
| AccessActiveNonPlayerObjectiveJournalEntries |  | Unknown | 类别：const |
| AccessActiveOtherLaws |  | Unknown | 类别：const |
| AccessActiveParties |  | Unknown | 类别：const |
| AccessActivePinnedNonPlayerObjectiveJournalEntries |  | Unknown | 类别：const |
| AccessActivePinnedPlayerObjectiveJournalEntries |  | Unknown | 类别：const |
| AccessActivePlayerObjectiveJournalEntries |  | Unknown | 类别：const |
| AccessActivePowerStructureLaws |  | Unknown | 类别：const |
| AccessAdmirals |  | Unknown | 类别：const |
| AccessAdmiralsOffer |  | Unknown | 类别：const |
| AccessAllInterestGroups |  | Unknown | 类别：const |
| AccessCapital |  | State | 类别：const |
| AccessCivilWars |  | Unknown | 类别：const |
| AccessConstructionQueue |  | Unknown | 类别：const |
| AccessCurrentlyResearchedTechnology |  | Technology | 类别：const |
| AccessDefinition |  | CountryDefinition | 类别：const |
| AccessFirstMarket |  | Market | 类别：const |
| AccessFormableCountries |  | Unknown | 类别：const |
| AccessGenerals |  | Unknown | 类别：const |
| AccessGeneralsOffer |  | Unknown | 类别：const |
| AccessGovernment |  | GovernmentType | 类别：const |
| AccessGovernmentConstructionQueue |  | Unknown | 类别：const |
| AccessHeaviestJournalEntry |  | JournalEntry | 类别：const |
| AccessHeir |  | Character | 类别：const |
| AccessInactiveJournalEntries |  | Unknown | 类别：const |
| AccessInstitutions |  | Unknown | 类别：const |
| AccessInterestGroupsInGovernment |  | Unknown | 类别：const |
| AccessInterestGroupsInOpposition |  | Unknown | 类别：const |
| AccessInterests |  | Unknown | 类别：const |
| AccessLandHQs |  | Unknown | 类别：const |
| AccessLastElectionParties |  | Unknown | 类别：const |
| AccessLawBeingEnacted |  | Law | 类别：const |
| AccessLawsWithGovernmentOrMovementSupport |  | Unknown | 类别：const |
| AccessLawsWithoutGovernmentOrMovementSupport |  | Unknown | 类别：const |
| AccessMarginalInterestGroups |  | Unknown | 类别：const |
| AccessModifier |  | Modifier | 类别：const |
| AccessNavalHQs |  | Unknown | 类别：const |
| AccessNonRevolutionaryPoliticalMovements |  | Unknown | 类别：const |
| AccessNumResearchableTechnologies |  | int32 | 类别：const |
| AccessOverlord |  | Country | 类别：const |
| AccessPagedGovernmentConstructionQueue | int32 Unknown | Unknown | 类别：const |
| AccessPagedPrivateConstructionQueue | int32 Unknown | Unknown | 类别：const |
| AccessPoliticalMovements |  | Unknown | 类别：const |
| AccessPopCultures |  | Unknown | 类别：const |
| AccessPopCulturesSortedByPolStr |  | Unknown | 类别：const |
| AccessPopCulturesSortedByPopulation |  | Unknown | 类别：const |
| AccessPopReligionsSortedByPolStr |  | Unknown | 类别：const |
| AccessPopReligionsSortedByPopulation |  | Unknown | 类别：const |
| AccessPopTypes |  | Unknown | 类别：const |
| AccessPopTypesSortedOnPolStr |  | Unknown | 类别：const |
| AccessPopTypesSortedOnPopulation |  | Unknown | 类别：const |
| AccessPowerBloc |  | PowerBloc | 类别：const |
| AccessPrivateConstructionQueue |  | Unknown | 类别：const |
| AccessReleasableCountries |  | Unknown | 类别：const |
| AccessResearchableTechnologiesMilitary |  | Unknown | 类别：const |
| AccessResearchableTechnologiesOther |  | Unknown | 类别：const |
| AccessResearchableTechnologiesProduction |  | Unknown | 类别：const |
| AccessResearchableTechnologiesSociety |  | Unknown | 类别：const |
| AccessRuler |  | Character | 类别：const |
| AccessSecessions |  | Unknown | 类别：const |
| AccessSelf |  | Country | 类别：const |
| AccessShippingLanes |  | Unknown | 类别：const |
| AccessShippingOriginStates | Province | Unknown | 类别：const |
| AccessShownCurrentlyConstructingGovernmentQueue |  | Unknown | 类别：const |
| AccessShownCurrentlyConstructingPrivateQueue |  | Unknown | 类别：const |
| AccessShownCurrentlyConstructingQueue |  | Unknown | 类别：const |
| AccessStateReligion |  | Religion | 类别：const |
| AccessStates |  | Unknown | 类别：const |
| AccessStrategies |  | Unknown | 类别：const |
| AccessTopOverlord |  | Country | 类别：const |
| AccessTruces |  | Unknown | 类别：const |
| AccessVioSovInterestedCountries | Country | Unknown | 类别：const |
| AccessVioSovWars | Country | Unknown | 类别：const |
| AccessVisibleJournalEntries |  | Unknown | 类别：const |
| AccessWars |  | Unknown | 类别：const |
| CalcBaseConstructionSpeed |  | CFixedPoint |  |
| CalcConscriptableBattalions |  | int32 |  |
| CalcCulturalTurmoil | Culture | CFixedPoint |  |
| CalcLibertyDesireLevel |  | LibertyDesireLevel |  |
| CalcMaxNumDeclaredInterests |  | int32 |  |
| CalcNumStatesInTurmoil |  | int32 |  |
| CalcRelativeUsedGovernmentConstruction |  | CFixedPoint |  |
| CalcRelativeUsedPrivateConstruction |  | CFixedPoint |  |
| CalcTurmoil |  | CFixedPoint |  |
| CalcUnusedConstruction |  | CFixedPoint |  |
| CalcUsedConstruction |  | CFixedPoint |  |
| CalcUsedGovernmentConstruction |  | CFixedPoint |  |
| CalcUsedPrivateConstruction |  | CFixedPoint |  |
| CanBuildingTypeBeMonopolized | BuildingType | bool |  |
| CanSignTreatyWith | Country | bool |  |
| CanTradeGoods | Unknown | bool |  |
| CreateCompany | CompanyType | Command |  |
| DeclareBankruptcy |  | Command |  |
| DeclareInterest | StrategicRegion | Command |  |
| DemobilizeAllArmies |  | Command |  |
| EstimatedConstructionQueueDuration |  | int32 |  |
| EstimatedGovernmentConstructionQueueDuration |  | int32 |  |
| EstimatedPrivateConstructionQueueDuration |  | int32 |  |
| Exists |  | bool |  |
| GetAIStrategiesDesc |  | CString | 类别：nonconst |
| GetActiveConstructionProjectsDesc |  | CString | 类别：nonconst |
| GetActiveLawFrom | Unknown | Law | 类别：nonconst |
| GetActiveLawFromGroup | CString | Law | 类别：nonconst |
| GetActivePeaceDealDesc |  | CString | 类别：nonconst |
| GetAdditionalExpensesTrend |  | DataTrend | 类别：nonconst |
| GetAdditionalIncomeTrend |  | DataTrend | 类别：nonconst |
| GetAdditionalSOLFactorsDescAll |  | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescMiddle |  | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescPoor |  | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescRich |  | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescWithCulture | Culture | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescWithCultureMiddle | Culture | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescWithCulturePoor | Culture | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescWithCultureRich | Culture | CString | 类别：nonconst |
| GetAdjective |  | CString | 类别：nonconst |
| GetAdjectiveNoFlag |  | CString | 类别：nonconst |
| GetAdjectiveNoFormatting |  | CString | 类别：nonconst |
| GetAllAcceptanceStatusSegments |  | Unknown | 类别：nonconst |
| GetAllGeneralDiploActions |  | Unknown | 类别：nonconst |
| GetAllOverlordDiploActions |  | Unknown | 类别：nonconst |
| GetAllPowerBlocLeaderDiploActions |  | Unknown | 类别：nonconst |
| GetAllPowerBlocMemberDiploActions |  | Unknown | 类别：nonconst |
| GetAllSubjectDiploActions |  | Unknown | 类别：nonconst |
| GetAllianceLikeTreatiesBrokenDesc | Country | CString | 类别：nonconst |
| GetAllianceLikeTreatiesBrokenFromPlayDesc | DiplomaticPlay | CString | 类别：nonconst |
| GetAllianceLikeTreatiesBrokenOnWarDesc | Country | CString | 类别：nonconst |
| GetAllianceLikeTreatiesList | Unknown | CString | 类别：nonconst |
| GetAltAdjective | CString | CString | 类别：nonconst |
| GetAltAdjectiveNoFlag | CString | CString | 类别：nonconst |
| GetAltAdjectiveNoFormatting | CString | CString | 类别：nonconst |
| GetAltName | CString | CString | 类别：nonconst |
| GetAltNameNoFlag | CString | CString | 类别：nonconst |
| GetAltNameNoFormatting | CString | CString | 类别：nonconst |
| GetArableLand |  | int32 | 类别：nonconst |
| GetArableLandDesc |  | CString | 类别：nonconst |
| GetArmiesBreakdown |  | CString | 类别：nonconst |
| GetArmyPowerProjection |  | CFixedPoint | 类别：nonconst |
| GetArmyPowerProjectionDesc |  | CString | 类别：nonconst |
| GetArmyReadinessStatusDesc |  | CString | 类别：nonconst |
| GetAttainableCompanies |  | Unknown | 类别：nonconst |
| GetAttitudeColor | Unknown | CVector4f | 类别：nonconst |
| GetAttitudeTowards | Country | AIAttitude | 类别：nonconst |
| GetAvailableCompanies |  | Unknown | 类别：nonconst |
| GetAvailableGeneralDiploActions |  | Unknown | 类别：nonconst |
| GetAvailableOverlordDiploActions |  | Unknown | 类别：nonconst |
| GetAvailablePowerBlocLeaderDiploActions |  | Unknown | 类别：nonconst |
| GetAvailablePowerBlocMemberDiploActions |  | Unknown | 类别：nonconst |
| GetAvailableSubjectDiploActions |  | Unknown | 类别：nonconst |
| GetAverageExpectedStandardOfLivingWithCultureMiddle | Unknown | CFixedPoint | 类别：nonconst |
| GetAverageExpectedStandardOfLivingWithCulturePoor | Unknown | CFixedPoint | 类别：nonconst |
| GetAverageExpectedStandardOfLivingWithCultureRich | Unknown | CFixedPoint | 类别：nonconst |
| GetAverageSoLByPoliticalStrength |  | CFixedPoint | 类别：nonconst |
| GetAverageSoLByPopulation |  | CFixedPoint | 类别：nonconst |
| GetAverageSoLByPopulationTrend |  | DataTrend | 类别：nonconst |
| GetAverageSoLByPopulationWithCulture | Unknown | CFixedPoint | 类别：nonconst |
| GetAverageSoLLowerTrend |  | DataTrend | 类别：nonconst |
| GetAverageSoLMiddleTrend |  | DataTrend | 类别：nonconst |
| GetAverageSoLUpperTrend |  | DataTrend | 类别：nonconst |
| GetAverageStandardOfLivingMiddle |  | CFixedPoint | 类别：nonconst |
| GetAverageStandardOfLivingPoor |  | CFixedPoint | 类别：nonconst |
| GetAverageStandardOfLivingRich |  | CFixedPoint | 类别：nonconst |
| GetAverageStandardOfLivingWithCultureMiddle | Unknown | CFixedPoint | 类别：nonconst |
| GetAverageStandardOfLivingWithCulturePoor | Unknown | CFixedPoint | 类别：nonconst |
| GetAverageStandardOfLivingWithCultureRich | Unknown | CFixedPoint | 类别：nonconst |
| GetAverageStateTaxCollectionMult |  | CFixedPoint | 类别：nonconst |
| GetAverageStateTaxCollectionMultBreakdown |  | CString | 类别：nonconst |
| GetAverageTaxWaste |  | CFixedPoint | 类别：nonconst |
| GetAverageTaxWasteBreakdown |  | CString | 类别：nonconst |
| GetBalanceTrend |  | DataDynamicTrend | 类别：nonconst |
| GetBaseConstructionSpeedDesc |  | CString | 类别：nonconst |
| GetBaseWeeklyTechnologySpread |  | CFixedPoint | 类别：nonconst |
| GetBaseWeeklyTechnologySpreadForTech | Unknown | CFixedPoint | 类别：nonconst |
| GetBattalions |  | int32 | 类别：nonconst |
| GetBattalionsDesc |  | CString | 类别：nonconst |
| GetBattalionsMobilizing |  | int32 | 类别：nonconst |
| GetBattalionsRanking |  | CString | 类别：nonconst |
| GetBolsterDesc |  | CString | 类别：nonconst |
| GetBolsteringCostDesc |  | CString | 类别：nonconst |
| GetCanBuildingTypeBeMonopolizedDesc | BuildingType | CString | 类别：nonconst |
| GetCanSignTreatyWithDesc | Country | CString | 类别：nonconst |
| GetCapital |  | State | 类别：nonconst |
| GetColonialGrowthDetails |  | CString | 类别：nonconst |
| GetCompanies |  | Unknown | 类别：nonconst |
| GetCompanyConstructionEfficiencyBonusFormatted |  | CString | 类别：nonconst |
| GetCompanyThroughputBonusFormatted |  | CString | 类别：nonconst |
| GetConscriptedBattalions |  | int32 | 类别：nonconst |
| GetConscriptionRatio |  | CFixedPoint | 类别：nonconst |
| GetConstructionGoodsExpenseTrend |  | DataTrend | 类别：nonconst |
| GetConstructionGoodsExpenses |  | CFixedPoint | 类别：nonconst |
| GetConstructionGoodsExpensesByGoodsDesc | Unknown | CString | 类别：nonconst |
| GetConstructionGoodsExpensesDesc |  | CString | 类别：nonconst |
| GetConstructionQueueDesc |  | CString | 类别：nonconst |
| GetConstructionsInCountry | Country | Unknown | 类别：nonconst |
| GetConsumptionTaxIncome |  | CFixedPoint | 类别：nonconst |
| GetConsumptionTaxTrend |  | DataTrend | 类别：nonconst |
| GetConsumptionTaxesDesc |  | CString | 类别：nonconst |
| GetConvoyEffectDesc |  | CString | 类别：nonconst |
| GetCountriesWithTreaties |  | Unknown | 类别：nonconst |
| GetCountryScorePosition |  | int32 | 类别：nonconst |
| GetCountryScorePositionDesc |  | CString | 类别：nonconst |
| GetCreditRatio |  | CFixedPoint | 类别：nonconst |
| GetCreditTooltip |  | CString | 类别：nonconst |
| GetCulturePolStrAsPercentage | Culture | CFixedPoint | 类别：nonconst |
| GetCulturePopulation | Culture | int64 | 类别：nonconst |
| GetCurrentLeverage | Unknown | CFixedPoint | 类别：nonconst |
| GetCurrentLeverageShare | PowerBloc | CFixedPoint | 类别：nonconst |
| GetCurrentPowerStruggleMonth |  | int32 | 类别：nonconst |
| GetCurrentlyResearchedTechnology |  | Technology | 类别：nonconst |
| GetCurrentlySpreadingTechsDesc |  | CString | 类别：nonconst |
| GetCustom | CustomLocalization | CString | 类别：nonconst |
| GetDailyRelationsProgress | Country | CFixedPoint | 类别：nonconst |
| GetDaysUntilElection |  | int32 | 类别：nonconst |
| GetDaysUntilRankLoss |  | int32 | 类别：nonconst |
| GetDecisions |  | Unknown | 类别：nonconst |
| GetDeclareBankruptcyDesc |  | CString | 类别：nonconst |
| GetDecreasingInterestsDesc |  | CString | 类别：nonconst |
| GetDeficitConvoyRatio |  | CFixedPoint | 类别：nonconst |
| GetDeficitConvoyRatioForProgressBar |  | CFixedPoint | 类别：nonconst |
| GetDeficitPowerRatio | Unknown | CFixedPoint | 类别：nonconst |
| GetDeficitPowerRatioForProgressBar | CString | CFixedPoint | 类别：nonconst |
| GetDefinition |  | CountryDefinition | 类别：nonconst |
| GetDependents |  | int64 | 类别：nonconst |
| GetDiplomaticAction | Unknown Unknown | DiplomaticAction | 类别：nonconst |
| GetDiplomaticActionWithStates | Unknown Unknown Unknown Unknown | DiplomaticAction | 类别：nonconst |
| GetDiplomaticPactsExpenseTrend |  | DataTrend | 类别：nonconst |
| GetDiplomaticPactsIncomeTrend |  | DataTrend | 类别：nonconst |
| GetDiplomaticStatusColor | Country | CVector4f | 类别：nonconst |
| GetDividendsTaxTrend |  | DataTrend | 类别：nonconst |
| GetDomesticallyOwnedGDP |  | CFixedPoint | 类别：nonconst |
| GetDomesticallyOwnedGDPFraction |  | CFixedPoint | 类别：nonconst |
| GetDraftTreaties |  | Unknown | 类别：nonconst |
| GetDraftTreatiesWith | Unknown | Unknown | 类别：nonconst |
| GetEconomicDependenceOn | Country | CString | 分类：nonconst |
| GetEconomicDependenceOnDesc | Unknown | CString | 分类：nonconst |
| GetEconomicDependenceOnRaw | Unknown | CFixedPoint | 分类：nonconst |
| GetElection |  | Election | 分类：nonconst |
| GetElectionPollTooltip |  | CString | 分类：nonconst |
| GetElectoralConfidence |  | CFixedPoint | 分类：nonconst |
| GetElectoralConfidenceEffectDesc |  | CString | 分类：nonconst |
| GetEmployedWorkingAdults |  | int64 | 分类：nonconst |
| GetEmptyAgitatorSlots |  | int32 | 分类：nonconst |
| GetEnemyOccupation |  | CFixedPoint | 分类：nonconst |
| GetEnforcedTreaties |  | Unknown | 分类：nonconst |
| GetEnforcedTreatiesWith | Country | Unknown | 分类：nonconst |
| GetEnforcedTreatiesWithDesc | Unknown | CString | 分类：nonconst |
| GetEventsByCategory | CString | Unknown | 分类：nonconst |
| GetExcessConvoyRatio |  | CFixedPoint | 分类：nonconst |
| GetExcessConvoyRatioForProgressBar |  | CFixedPoint | 分类：nonconst |
| GetExcessPowerRatio | Unknown | CFixedPoint | 分类：nonconst |
| GetExcessPowerRatioForProgressBar | CString | CFixedPoint | 分类：nonconst |
| GetExpectedSOLFactorsDescAll |  | CString | 分类：nonconst |
| GetExpectedSOLFactorsDescMiddle |  | CString | 分类：nonconst |
| GetExpectedSOLFactorsDescPoor |  | CString | 分类：nonconst |
| GetExpectedSOLFactorsDescRich |  | CString | 分类：nonconst |
| GetExpectedSOLFactorsDescWithCulture | Unknown | CString | 分类：nonconst |
| GetExpectedSoLByPopulation |  | CFixedPoint | 分类：nonconst |
| GetExpectedStandardOfLivingMiddle |  | CFixedPoint | 分类：nonconst |
| GetExpectedStandardOfLivingPoor |  | CFixedPoint | 分类：nonconst |
| GetExpectedStandardOfLivingRich |  | CFixedPoint | 分类：nonconst |
| GetExpensesBreakdown |  | CString | 分类：nonconst |
| GetExportSubventionsDescHigh | Goods | CString | 分类：nonconst |
| GetExportSubventionsDescLow | Goods | CString | 分类：nonconst |
| GetExportSubventionsDescMax | Goods | CString | 分类：nonconst |
| GetExportTariffsDescHigh | Goods | CString | 分类：nonconst |
| GetExportTariffsDescLow | Goods | CString | 分类：nonconst |
| GetExportTariffsDescMax | Goods | CString | 分类：nonconst |
| GetExportTariffsDescNone | Goods | CString | 分类：nonconst |
| GetExportedAmount | Unknown | CFixedPoint | 分类：nonconst |
| GetExports |  | Unknown | 分类：nonconst |
| GetFirstPrimaryCulture |  | Culture | 分类：nonconst |
| GetFlag |  | CoatOfArms | 分类：nonconst |
| GetFlagTextIcon |  | CString | 分类：nonconst |
| GetFlavorText |  | CString | 分类：nonconst |
| GetFleetsBreakdown |  | CString | 分类：nonconst |
| GetFlotillasRanking |  | CString | 分类：nonconst |
| GetForeignOwnedGDP |  | CFixedPoint | 分类：nonconst |
| GetForeignOwnedGDPDesc |  | CString | 分类：nonconst |
| GetForeignOwnedGDPFraction |  | CFixedPoint | 分类：nonconst |
| GetFormattedStandardOfLivingAll |  | CString | 分类：nonconst |
| GetFormattedStandardOfLivingAllWithCulture | Culture | CString | 分类：nonconst |
| GetFormattedStandardOfLivingLabelAll |  | CString | 分类：nonconst |
| GetFormattedStandardOfLivingLabelAllWithCulture | Culture | CString | 分类：nonconst |
| GetFormattedStandardOfLivingLabelMiddle |  | CString | 分类：nonconst |
| GetFormattedStandardOfLivingLabelMiddleWithCulture | Culture | CString | 分类：nonconst |
| GetFormattedStandardOfLivingLabelPoor |  | CString | 分类：nonconst |
| GetFormattedStandardOfLivingLabelPoorWithCulture | Culture | CString | 分类：nonconst |
| GetFormattedStandardOfLivingLabelRich |  | CString | 分类：nonconst |
| GetFormattedStandardOfLivingLabelRichWithCulture | Culture | CString | 分类：nonconst |
| GetFormattedStandardOfLivingMiddle |  | CString | 分类：nonconst |
| GetFormattedStandardOfLivingMiddleWithCulture | Culture | CString | 分类：nonconst |
| GetFormattedStandardOfLivingPoor |  | CString | 分类：nonconst |
| GetFormattedStandardOfLivingPoorWithCulture | Culture | CString | 分类：nonconst |
| GetFormattedStandardOfLivingRich |  | CString | 分类：nonconst |
| GetFormattedStandardOfLivingRichWithCulture | Culture | CString | 分类：nonconst |
| GetFreeArableLand |  | int32 | 分类：nonconst |
| GetGDP |  | CFixedPoint | 分类：nonconst |
| GetGDPOwnedInForeignCountries |  | CFixedPoint | 分类：nonconst |
| GetGDPOwnedInForeignCountriesDesc |  | CString | 分类：nonconst |
| GetGDPPerCapita |  | CFixedPoint | 分类：nonconst |
| GetGDPPerCapitaRanking |  | CString | 分类：nonconst |
| GetGDPRanking |  | CString | 分类：nonconst |
| GetGDPTrend |  | DataTrend | 分类：nonconst |
| GetGDPWithOwnershipsInForeignCountries |  | CFixedPoint | 分类：nonconst |
| GetGameOverDateString |  | CString | 分类：nonconst |
| GetGdpRatioOwnedBy | Unknown | CString | 分类：nonconst |
| GetGdpRatioOwnedByDesc | Unknown | CString | 分类：nonconst |
| GetGdpRatioOwnedByRaw | Unknown | CFixedPoint | 分类：nonconst |
| GetGoldProgressDesc |  | CString | 分类：nonconst |
| GetGoldReserveLimit |  | CFixedPoint | 分类：nonconst |
| GetGoldReserveLimitDesc |  | CString | 分类：nonconst |
| GetGoldReserveRatio |  | CFixedPoint | 分类：nonconst |
| GetGoldReserves |  | CFixedPoint | 分类：nonconst |
| GetGoldReservesTrend |  | DataDynamicTrend | 分类：nonconst |
| GetGoodsLeaderboardDesc |  | CString | 分类：nonconst |
| GetGovernment |  | GovernmentType | 分类：nonconst |
| GetGovernmentConstructionGoodsExpenses |  | CFixedPoint | 分类：nonconst |
| GetGovernmentConstructionGoodsExpensesByGoodsDesc |  | CString | 分类：nonconst |
| GetGovernmentGoodsExpenseTrend |  | DataTrend | 分类：nonconst |
| GetGovernmentGoodsExpenses |  | CFixedPoint | 分类：nonconst |
| GetGovernmentGoodsExpensesByGoodsDesc |  | CString | 分类：nonconst |
| GetGovernmentGoodsExpensesDesc |  | CString | 分类：nonconst |
| GetGovernmentIGsDesc |  | CString | 分类：nonconst |
| GetGovernmentInterestGroupsDesc |  | CString | 分类：nonconst |
| GetGovernmentInterestGroupsPopulationDesc |  | CString | 分类：nonconst |
| GetGovernmentLegitimacy |  | int32 | 分类：nonconst |
| GetGovernmentLegitimacyDesc |  | CString | 分类：nonconst |
| GetGovernmentLegitimacyLevel |  | LegitimacyLevel | 分类：nonconst |
| GetGovernmentSelfDebt |  | CFixedPoint | 分类：nonconst |
| GetGovernmentSelfDebtFraction |  | CFixedPoint | 分类：nonconst |
| GetGovernmentShareDividendsTrend |  | DataTrend | 分类：nonconst |
| GetGovernmentShareLossesTrend |  | DataTrend | 分类：nonconst |
| GetGovernmentSlavesExpenseTrend |  | DataTrend | 分类：nonconst |
| GetGovernmentSlavesExpenses |  | CFixedPoint | 分类：nonconst |
| GetGovernmentSlavesExpensesDesc |  | CString | 分类：nonconst |
| GetGovernmentWageLevelDescHigh |  | CString | 分类：nonconst |
| GetGovernmentWageLevelDescLow |  | CString | 分类：nonconst |
| GetGovernmentWageLevelDescMedium |  | CString | 分类：nonconst |
| GetGovernmentWageLevelDescVeryHigh |  | CString | 分类：nonconst |
| GetGovernmentWageLevelDescVeryLow |  | CString | 分类：nonconst |
| GetGovernmentWagesExpenseTrend |  | DataTrend | 分类：nonconst |
| GetGovernmentWagesExpenses |  | CFixedPoint | 分类：nonconst |
| GetGovernmentWagesExpensesDesc |  | CString | 分类：nonconst |
| GetGroupsForActiveJournalEntries |  | Unknown | 分类：nonconst |
| GetGroupsForInActiveJournalEntries |  | Unknown | 分类：nonconst |
| GetGrowingCivilWars |  | Unknown | 分类：nonconst |
| GetHeir |  | Character | 分类：nonconst |
| GetHighestPossibleRank |  | CString | 分类：nonconst |
| GetID |  | int32 | 分类：nonconst |
| GetIDString |  | CString | 分类：nonconst |
| GetIGApprovalFromLoyalistsBreakdown |  | CString | 分类：nonconst |
| GetIGApprovalFromRadicalsBreakdown |  | CString | 分类：nonconst |
| GetImportSubventionsDescHigh | Goods | CString | 分类：nonconst |
| GetImportSubventionsDescLow | Goods | CString | 分类：nonconst |
| GetImportSubventionsDescMax | Goods | CString | 分类：nonconst |
| GetImportTariffsDescHigh | Goods | CString | 分类：nonconst |
| GetImportTariffsDescLow | Goods | CString | 分类：nonconst |
| GetImportTariffsDescMax | Goods | CString | 分类：nonconst |
| GetImportTariffsDescNone | Goods | CString | 分类：nonconst |
| GetImportedAmount | Unknown | CFixedPoint | 分类：nonconst |
| GetImports |  | Unknown | 分类：nonconst |
| GetInDefaultEffectsDesc |  | CString | 分类：nonconst |
| GetInForceTreaties |  | Unknown | 分类：nonconst |
| GetInactiveConstructionProjectsDesc |  | CString | 分类：nonconst |
| GetInactivePopulation |  | int64 | 分类：nonconst |
| GetInactivePopulationDesc |  | CString | 分类：nonconst |
| GetIncomeBreakdown |  | CString | 分类：nonconst |
| GetIncomeTaxIncome |  | CFixedPoint | 分类：nonconst |
| GetIncorporatedLiteracyRanking |  | CString | 分类：nonconst |
| GetIncorporatedLiteracyRate |  | CFixedPoint | 分类：nonconst |
| GetIncorporatedLiteracyTrend |  | DataTrend | 分类：nonconst |
| GetIncorporatedPopulation |  | int64 | 分类：nonconst |
| GetIncorporatedStatesLawCostDesc |  | CString | 分类：nonconst |
| GetIndependentInterestGroupsInGovernment |  | Unknown | 分类：nonconst |
| GetIndependentInterestGroupsInOpposition |  | Unknown | 分类：nonconst |
| GetInfamy |  | CFixedPoint | 分类：nonconst |
| GetInfamyColor |  | CVector4f | 分类：nonconst |
| GetInfamyDesc |  | CString | 分类：nonconst |
| GetInfamyIconTexture |  | Unknown | 分类：nonconst |
| GetInfamyLabel |  | CString | 分类：nonconst |
| GetInstitutionInvestment |  | CFixedPoint | 分类：nonconst |
| GetInstitutionInvestmentBureaucracyCost |  | CFixedPoint | 分类：nonconst |
| GetInstitutionInvestmentBureaucracyCostDesc |  | CString | 分类：nonconst |
| GetInstitutionInvestmentBureaucracyFactor |  | CFixedPoint | 分类：nonconst |
| GetInstitutionInvestmentBureaucracyFactorDesc |  | CString | 分类：nonconst |
| GetInstitutionInvestmentDesc |  | CString | 分类：nonconst |
| GetInstitutionsSummary |  | CString | 分类：nonconst |
| GetInsurrectionaryIGsDesc |  | CString | 分类：nonconst |
| GetInterestExpenseTrend |  | DataTrend | 分类：nonconst |
| GetInterestGroupOfType | Unknown | InterestGroup | 分类：nonconst |
| GetInterestPayment |  | CFixedPoint | 分类：nonconst |
| GetInterestRateTooltip |  | CString | 分类：nonconst |
| GetInvestmentFundTrend |  | DataTrend | 分类：nonconst |
| GetInvestmentGdpFractionInCountry | Country | CFixedPoint | 分类：nonconst |
| GetInvestmentIncome |  | CFixedPoint | 分类：nonconst |
| GetInvestmentIncomeTrend |  | DataTrend | 分类：nonconst |
| GetInvestmentLevelsInCountry | Country | int32 | 分类：nonconst |
| GetInvestmentPool |  | CFixedPoint | 分类：nonconst |
| GetInvestmentPoolChange |  | CFixedPoint | 分类：nonconst |
| GetInvestmentPoolChangeFromConstructionDesc |  | CString | 分类：nonconst |
| GetInvestmentPoolChangeFromInvestmentBreakdown |  | CString | 分类：nonconst |
| GetInvestmentPoolChangeFromInvestmentDesc |  | CString | 分类：nonconst |
| GetInvestmentPoolPredictedNextBuildingDesc |  | CString | 分类：nonconst |
| GetJournalEntry | Unknown | JournalEntry | 分类：nonconst |
| GetKillRateNavy |  | CFixedPoint | 分类：nonconst |
| GetLabel | Country | CString | 分类：nonconst |
| GetLackOfAutonomousInvestmentReasonDesc |  | CString | 分类：nonconst |
| GetLastCatalystExpiryDate | Country DiplomaticCatalyst | CString | 分类：nonconst |
| GetLastElectionResultsTooltip |  | CString | 分类：nonconst |
| GetLawBeingEnacted |  | Law | 分类：nonconst |
| GetLawBeingEnactedFromGroup | Unknown | Law | 分类：nonconst |
| GetLawEnactmentProgress |  | CFixedPoint | 分类：nonconst |
| GetLawEnactmentProgressDesc |  | CString | 分类：nonconst |
| GetLeaderReligionPercentage |  | CFixedPoint | 分类：nonconst |
| GetLeverageAdvantage | PowerBloc | CFixedPoint | 分类：nonconst |
| GetLeverageAdvantageTarget | PowerBloc | CFixedPoint | 分类：nonconst |
| GetLeverageBreakdown |  | CString | 分类：nonconst |
| GetLeverageComparisonDesc | PowerBloc | CString | 分类：nonconst |
| GetLeverageGain | PowerBloc | CFixedPoint | 分类：nonconst |
| GetLeverageGainBreakdown | PowerBloc | CString | 分类：nonconst |
| GetLeverageResistance |  | CFixedPoint | 分类：nonconst |
| GetLeverageTarget | PowerBloc | CFixedPoint | 分类：nonconst |
| GetLeverageTooltip |  | CString | 分类：nonconst |
| GetLibertyDesireLevelLabel |  | CString | 分类：nonconst |
| GetLibertyDesireRaw |  | CFixedPoint | 分类：nonconst |
| GetLimitedMassMigrationCountryAttraction |  | CFixedPoint | 分类：nonconst |
| GetLobbyJournalEntries |  | Unknown | 分类：nonconst |
| GetLowerStrataPopulationTrend |  | DataTrend | 分类：nonconst |
| GetLoyalistsChangeSummary |  | CString | 分类：nonconst |
| GetLoyalistsDecreaseBreakdown |  | CString | 分类：nonconst |
| GetLoyalistsIncreaseBreakdown |  | CString | 分类：nonconst |
| GetLoyalistsOrRadicalsGainedFromLegitimacy |  | int64 | 分类：nonconst |
| GetLoyalistsOrRadicalsGainedFromLegitimacyModifierDescription | Unknown | CString | 分类：nonconst |
| GetLoyalistsSummaryDesc |  | CString | 分类：nonconst |
| GetLoyalistsTrend |  | DataTrend | 分类：nonconst |
| GetLoyaltiesGain |  | CFixedPoint | 分类：nonconst |
| GetMapColor |  | CVector4f | 分类：nonconst |
| GetMarginalAndInactivePopulationInCountryAsPercentage |  | float | 分类：nonconst |
| GetMarginalCloutInCountryAsPercentage |  | float | 分类：nonconst |
| GetMarginalInterestGroupsDesc |  | CString | 分类：nonconst |
| GetMarginalInterestGroupsPopulationDesc |  | CString | 分类：nonconst |
| GetMarket |  | Market | 分类：nonconst |
| GetMarketOwnerName |  | CString | 分类：nonconst |
| GetMassMigrationAttractionBreakdown |  | CString | 分类：nonconst |
| GetMassMigrationAttractionDesc |  | CString | 分类：nonconst |
| GetMaxCloutOrPopulationPercentage |  | float | 分类：nonconst |
| GetMaxCredit |  | CFixedPoint | 分类：nonconst |
| GetMaxFreeCharters |  | int32 | 分类：nonconst |
| GetMaxLawEnactmentSetbacks |  | int32 | 分类：nonconst |
| GetMaxNumCompanies |  | int32 | 分类：nonconst |
| GetMaxNumCompaniesDesc |  | CString | 分类：nonconst |
| GetMaxNumDeclaredInterestsBreakdown |  | CString | 分类：nonconst |
| GetMaxPowerStruggleMonth |  | int32 | 分类：nonconst |
| GetMaxWeeklyTechnologyProgressForTech | Unknown | CFixedPoint | 分类：nonconst |
| GetMaxWeeklyTechnologySpread |  | CFixedPoint | 分类：nonconst |
| GetMaxWeeklyTechnologySpreadForTech | Unknown | CFixedPoint | 分类：nonconst |
| GetMiddleStrataPopulationTrend |  | DataTrend | 分类：nonconst |
| GetMilitaryFormationsArmy |  | Unknown | 分类：nonconst |
| GetMilitaryFormationsFleet |  | Unknown | 分类：nonconst |
| GetMilitaryGoodsExpenseTrend |  | DataTrend | 分类：nonconst |
| GetMilitaryGoodsExpenses |  | CFixedPoint | 分类：nonconst |
| GetMilitaryGoodsExpensesByGoodsDesc |  | CString | 分类：nonconst |
| GetMilitaryGoodsExpensesDesc |  | CString | 分类：nonconst |
| GetMilitaryInterfaceColor |  | CVector4f | 分类：nonconst |
| GetMilitarySlavesExpenseTrend |  | DataTrend | 分类：nonconst |
| GetMilitarySlavesExpenses |  | CFixedPoint | 分类：nonconst |
| GetMilitarySlavesExpensesDesc |  | CString | 分类：nonconst |
| GetMilitaryWageLevelDescHigh |  | CString | 分类：nonconst |
| GetMilitaryWageLevelDescLow |  | CString | 分类：nonconst |
| GetMilitaryWageLevelDescMedium |  | CString | 分类：nonconst |
| GetMilitaryWageLevelDescVeryHigh |  | CString | 分类：nonconst |
| GetMilitaryWageLevelDescVeryLow |  | CString | 分类：nonconst |
| GetMilitaryWagesExpenseTrend |  | DataTrend | 分类：nonconst |
| GetMilitaryWagesExpenses |  | CFixedPoint | 分类：nonconst |
| GetMilitaryWagesExpensesDesc |  | CString | 分类：nonconst |
| GetMinWeeklyTechnologyProgressForTech | Technology | CFixedPoint | 分类：nonconst |
| GetMinWeeklyTechnologySpread |  | CFixedPoint | 分类：nonconst |
| GetMinWeeklyTechnologySpreadForTech | Unknown | CFixedPoint | 分类：nonconst |
| GetMintingTrend |  | DataTrend | 分类：nonconst |
| GetMobilizationRatio |  | CFixedPoint | 分类：nonconst |
| GetModifier |  | Modifier | 分类：nonconst |
| GetMoveCapitalEffectsDesc |  | CString | 分类：nonconst |
| GetMoveMarketCapitalEffectsDesc |  | CString | 分类：nonconst |
| GetName |  | CString | 分类：nonconst |
| GetNameNoFlag |  | CString | 分类：nonconst |
| GetNameNoFormatting |  | CString | 分类：nonconst |
| GetNavyPowerProjection |  | CFixedPoint | 分类：nonconst |
| GetNavyPowerProjectionDesc |  | CString | 分类：nonconst |
| GetNegotiatingInterestGroup |  | InterestGroup | 分类：nonconst |
| GetNextElectionDate |  | CString | 分类：nonconst |
| GetNextRank |  | CString | 分类：nonconst |
| GetNextRankDesc |  | CString | 分类：nonconst |
| GetNextRankNumber |  | int32 | 分类：nonconst |
| GetNextStartOfCampaignDate |  | CString | 分类：nonconst |
| GetNonPotentialDiploPlays |  | Unknown | 分类：nonconst |
| GetNonSubjectDiplomaticPactsWith | Country | Unknown | 分类：nonconst |
| GetNumActiveConstructionQueueElements |  | int32 | 分类：nonconst |
| GetNumActiveGovernmentConstructionQueueElements |  | int32 | 分类：nonconst |
| GetNumActivePrivateConstructionQueueElements |  | int32 | 分类：nonconst |
| GetNumActiveShownConstructionQueueElements |  | int32 | 分类：nonconst |
| GetNumActiveShownGovernmentConstructionQueueElements |  | int32 | 分类：nonconst |
| GetNumActiveShownPrivateConstructionQueueElements |  | int32 | 分类：nonconst |
| GetNumAvailableCompanies |  | int32 | 分类：nonconst |
| GetNumAvailableConvoys |  | int32 | 分类：nonconst |
| GetNumAvailableNegotiations |  | int32 | 分类：nonconst |
| GetNumBattalions |  | int32 | 分类：nonconst |
| GetNumBuildingsInConstructionQueueInState | State | int32 | 分类：nonconst |
| GetNumBuildingsUnderConstructionInState | State | int32 | 分类：nonconst |
| GetNumCombatUnits |  | int32 | 分类：nonconst |
| GetNumCompanies |  | int32 | 分类：nonconst |
| GetNumConvoys |  | int32 | 分类：nonconst |
| GetNumConvoysDamagedDesc |  | CString | 分类：nonconst |
| GetNumConvoysDesc |  | CString | 分类：nonconst |
| GetNumDamagedConvoys |  | int32 | 分类：nonconst |
| GetNumDeclaredInterests |  | int32 | 分类：nonconst |
| GetNumFlotillas |  | int32 | 分类：nonconst |
| GetNumGovernmentConstructionsInQueue |  | int32 | 分类：nonconst |
| GetNumInactiveAndNonShownGovernmentConstructionQueueElements |  | int32 | 分类：nonconst |
| GetNumInactiveAndNonShownPrivateConstructionQueueElements |  | int32 | 分类：nonconst |
| GetNumInactiveConstructionQueueElements |  | int32 | 分类：nonconst |
| GetNumInactiveGovernmentConstructionQueueElements |  | int32 | 分类：nonconst |
| GetNumInactivePrivateConstructionQueueElements |  | int32 | 分类：nonconst |
| GetNumIncorporatedLiteratePops |  | int64 | 分类：nonconst |
| GetNumIncorporatedStates |  | int32 | 分类：nonconst |
| GetNumIncorporatedStatesDesc |  | CString | 分类：nonconst |
| GetNumInsufficientTaxCapacityStates |  | int32 | 分类：nonconst |
| GetNumInterestGroupMembers |  | int64 | 分类：nonconst |
| GetNumIsolatedStates |  | int32 | 分类：nonconst |
| GetNumLowMarketAccessStates |  | int32 | 分类：nonconst |
| GetNumLoyalists |  | int64 | 分类：nonconst |
| GetNumNeutrals |  | int64 | 分类：nonconst |
| GetNumPoliticallyInactiveLoyalists |  | int64 | 分类：nonconst |
| GetNumPoliticallyInactiveNeutrals |  | int64 | 分类：nonconst |
| GetNumPoliticallyInactiveRadicals |  | int64 | 分类：nonconst |
| GetNumPrivateConstructionsInQueue |  | int32 | 分类：nonconst |
| GetNumRadicals |  | int64 | 分类：nonconst |
| GetNumStatesThatCanBeIncorporated |  | int32 | 分类：nonconst |
| GetNumStatesWithConstruction |  | int32 | 分类：nonconst |
| GetNumStatesWithoutConstruction |  | int32 | 分类：nonconst |
| GetNumTotalLiteratePops |  | int64 | 分类：nonconst |
| GetNumTurmoilStates |  | int32 | 分类：nonconst |
| GetNumUnincorporatedStates |  | int32 | 分类：nonconst |
| GetNumUnincorporatedStatesDesc |  | CString | 分类：nonconst |
| GetNumUsableConvoys |  | int32 | 分类：nonconst |
| GetNumberOfActiveConscriptionCenters |  | int32 | 分类：nonconst |
| GetNumberOfInactiveConscriptionCenters |  | int32 | 分类：nonconst |
| GetObjective |  | Objective | 分类：nonconst |
| GetObligationFromExpirationDate | Country | CString | 分类：nonconst |
| GetObligationFromExpirationDesc | Country | CString | 分类：nonconst |
| GetObligationToExpirationDate | Country | CString | 分类：nonconst |
| GetObligationToExpirationDesc | Country | CString | 分类：nonconst |
| GetObligationsOwedFrom |  | Unknown | 分类：nonconst |
| GetObligationsOwedTo |  | Unknown | 分类：nonconst |
| GetOppositionInterestGroupsDesc |  | CString | 分类：nonconst |
| GetOppositionInterestGroupsPopulationDesc |  | CString | 分类：nonconst |
| GetOtherPowerBlocWithHighestLeverage | Unknown | PowerBloc | 分类：nonconst |
| GetOverlord |  | Country | 分类：nonconst |
| GetOwningCompany |  | Company | 分类：nonconst |
| GetPartiesInGovernment |  | Unknown | 分类：nonconst |
| GetPartiesInOpposition |  | Unknown | 分类：nonconst |
| GetPeopleAbroad |  | int64 | 分类：nonconst |
| GetPlayedByDesc |  | CString | 分类：nonconst |
| GetPlayer |  | Player | 分类：nonconst |
| GetPoliticalLobbies |  | Unknown | 分类：nonconst |
| GetPoliticallyInvolvedPercentage |  | CFixedPoint | 分类：nonconst |
| GetPoliticallyInvolvedPopulation |  | int64 | 分类：nonconst |
| GetPoliticallyInvolvedPopulationDesc |  | CString | 分类：nonconst |
| GetPollTaxIncome |  | CFixedPoint | 分类：nonconst |
| GetPollTaxTrend |  | DataTrend | 分类：nonconst |
| GetPopConsumptionDependenceOn | Unknown | CString | 分类：nonconst |
| GetPopConsumptionDependenceOnDesc | Unknown | CString | 分类：nonconst |
| GetPopConsumptionDependenceOnRaw | Unknown | CFixedPoint | 分类：nonconst |
| GetPopGrowthDesc |  | CString | 分类：nonconst |
| GetPopReligions |  | Unknown | 分类：nonconst |
| GetPopulationRanking |  | CString | 分类：nonconst |
| GetPopulationTrend |  | DataTrend | 分类：nonconst |
| GetPotentialCompanies |  | Unknown | 分类：nonconst |
| GetPotentialDiploPlays |  | Unknown | 分类：nonconst |
| GetPotentialGeneralDiploActions |  | Unknown | 分类：nonconst |
| GetPotentialInvestors |  | Unknown | 分类：nonconst |
| GetPotentialLabor |  | int64 | 分类：nonconst |
| GetPotentialOverlordDiploActions |  | Unknown | 分类：nonconst |
| GetPotentialPowerBlocLeaderDiploActions |  | Unknown | 分类：nonconst |
| GetPotentialPowerBlocMemberDiploActions |  | Unknown | 分类：nonconst |
| GetPotentialSubjectDiploActions |  | Unknown | 分类：nonconst |
| GetPowerBloc |  | PowerBloc | 分类：nonconst |
| GetPowerBlocExpenseDesc |  | CString | 分类：nonconst |
| GetPowerBlocExpenseRaw |  | CFixedPoint | 分类：nonconst |
| GetPowerBlocExpenseTrend |  | DataTrend | 分类：nonconst |
| GetPowerBlocIncomeDesc |  | CString | 分类：nonconst |
| GetPowerBlocIncomeRaw |  | CFixedPoint | 类别：非常量 |
| GetPowerBlocIncomeTrend |  | DataTrend | 类别：非常量 |
| GetPowerBlocNonMemberCountryTooltip |  | CString | 类别：非常量 |
| GetPowerBlocWithHighestLeverage |  | PowerBloc | 类别：非常量 |
| GetPowerBlocsTotalLeverageShare |  | CFixedPoint | 类别：非常量 |
| GetPowerBlocsWithLeverage |  | Unknown | 类别：非常量 |
| GetPowerDelta | CString | CFixedPoint | 类别：非常量 |
| GetPowerDeltaIcon | CString | CString | 类别：非常量 |
| GetPowerExpensesString | CString | CString | 类别：非常量 |
| GetPowerIncome | CString | CFixedPoint | 类别：非常量 |
| GetPowerIncomeString | CString | CString | 类别：非常量 |
| GetPowerTooltip | CString | CString | 类别：非常量 |
| GetPredictedBalanceFromBankruptcy |  | CFixedPoint | 类别：非常量 |
| GetPrestige |  | int32 | 类别：非常量 |
| GetPrestigeDesc |  | CString | 类别：非常量 |
| GetPrestigeForCurrentRank |  | int32 | 类别：非常量 |
| GetPrestigeForNextRank |  | int32 | 类别：非常量 |
| GetPrestigeGoodsLeaderboardDesc |  | CString | 类别：非常量 |
| GetPrestigeToMaintainRank |  | int32 | 类别：非常量 |
| GetPrestigeTrend |  | DataTrend | 类别：非常量 |
| GetPreviousAttitudeTowards | Unknown | AIAttitude | 类别：非常量 |
| GetPreviousAutonomousInvestmentsDesc |  | CString | 类别：非常量 |
| GetPreviousRank |  | CString | 类别：非常量 |
| GetPriceReportDesc |  | CString | 类别：非常量 |
| GetPrimaryCulturesDesc |  | CString | 类别：非常量 |
| GetPrincipal |  | CFixedPoint | 类别：非常量 |
| GetPrivateConstructionGoodsExpenses |  | CFixedPoint | 类别：非常量 |
| GetPrivateConstructionGoodsExpensesByGoodsDesc |  | CString | 类别：非常量 |
| GetPrivateConstructionQueueDesc |  | CString | 类别：非常量 |
| GetRadicalizationFromBankruptcy |  | int64 | 类别：非常量 |
| GetRadicalsChangeSummary |  | CString | 类别：非常量 |
| GetRadicalsDecreaseBreakdown |  | CString | 类别：非常量 |
| GetRadicalsIncreaseBreakdown |  | CString | 类别：非常量 |
| GetRadicalsLoyalistsChangeStartDate |  | CString | 类别：非常量 |
| GetRadicalsSummaryDesc |  | CString | 类别：非常量 |
| GetRadicalsTrend |  | DataTrend | 类别：非常量 |
| GetRank |  | CString | 类别：非常量 |
| GetRankDesc |  | CString | 类别：非常量 |
| GetRankIconIndex |  | int32 | 类别：非常量 |
| GetRankModifier |  | Modifier | 类别：非常量 |
| GetRankNumber |  | int32 | 类别：非常量 |
| GetRankProgress |  | float | 类别：非常量 |
| GetRankTooltip |  | CString | 类别：非常量 |
| GetRecentPartiesDesc |  | CString | 类别：非常量 |
| GetRegularBattalions |  | int32 | 类别：非常量 |
| GetReinforcementRateArmy |  | CFixedPoint | 类别：非常量 |
| GetReinforcementRateNavy |  | CFixedPoint | 类别：非常量 |
| GetRelationsColor | Unknown | CVector4f | 类别：非常量 |
| GetRelationsIconTexture | Country | Unknown | 类别：非常量 |
| GetRelationsProgress | Unknown | CFixedPoint | 类别：非常量 |
| GetRelationsProgressDesc | Unknown | CString | 类别：非常量 |
| GetRelationsTooltip | Country | CString | 类别：非常量 |
| GetRelationsWith | Country | int32 | 类别：非常量 |
| GetRelationsWithDesc | Country | CString | 类别：非常量 |
| GetRelativePrestige | Country | CFixedPoint | 类别：非常量 |
| GetRemainingCredit |  | CFixedPoint | 类别：非常量 |
| GetRemainingDaysForFreeGovernmentReformRaw |  | int32 | 类别：非常量 |
| GetRequiredConvoys |  | int32 | 类别：非常量 |
| GetRequiredConvoysBreakdown |  | CString | 类别：非常量 |
| GetResearchQueueBottom |  | Unknown | 类别：非常量 |
| GetResearchQueueTop |  | Unknown | 类别：非常量 |
| GetRuler |  | Character | 类别：非常量 |
| GetRulingIGsDesc |  | CString | 类别：非常量 |
| GetSOLDescForAllStratas |  | CString | 类别：非常量 |
| GetSalariedWorkingAdults |  | int64 | 类别：非常量 |
| GetSeaNodesMightBeConvoyRaidedInDesc |  | CString | 类别：非常量 |
| GetSelectedLaw |  | Law | 类别：非常量 |
| GetSocialHierarchy |  | SocialHierarchy | 类别：非常量 |
| GetSpecialSocialHierarchy |  | SocialHierarchy | 类别：非常量 |
| GetStandardOfLivingRanking |  | CString | 类别：非常量 |
| GetStateOwnedBuildingsBureaucracyCostForLevels | int32 | CFixedPoint | 类别：非常量 |
| GetStateReligion |  | Religion | 类别：非常量 |
| GetStatesInTurmoilBreakdown |  | CString | 类别：非常量 |
| GetStatus | Country | CString | 类别：非常量 |
| GetStrategicObjectives |  | Unknown | 类别：非常量 |
| GetStrategicRegions |  | Unknown | 类别：非常量 |
| GetSubjectOrPowerBlocHierarchyLabel | Country | CString | 类别：非常量 |
| GetSubjectPact |  | DiplomaticPact | 类别：非常量 |
| GetSubjectType |  | SubjectType | 类别：非常量 |
| GetSubjectTypeName |  | CString | 类别：非常量 |
| GetSubjects |  | Unknown | 类别：非常量 |
| GetSubjectsOfType | SubjectType | Unknown | 类别：非常量 |
| GetSubsidiesExpenseTrend |  | DataTrend | 类别：非常量 |
| GetSubsidiesExpenses |  | CFixedPoint | 类别：非常量 |
| GetSubsidiesExpensesDesc |  | CString | 类别：非常量 |
| GetSubsistingWorkingAdults |  | int64 | 类别：非常量 |
| GetSubventionsExpenseTrend |  | DataTrend | 类别：非常量 |
| GetSubventionsExpenses |  | CFixedPoint | 类别：非常量 |
| GetSubventionsExpensesDesc |  | CString | 类别：非常量 |
| GetSupplyNetworkNumSeaNodes |  | int32 | 类别：非常量 |
| GetSupplyNetworkNumSeaNodesDesc |  | CString | 类别：非常量 |
| GetSupplyNetworkStrength |  | CFixedPoint | 类别：非常量 |
| GetSuppressionCostDesc |  | CString | 类别：非常量 |
| GetSuppressionDesc |  | CString | 类别：非常量 |
| GetTagName |  | CString | 类别：非常量 |
| GetTargetLeverage | Unknown | CFixedPoint | 类别：非常量 |
| GetTargetLeverageShare | PowerBloc | CFixedPoint | 类别：非常量 |
| GetTargetRank |  | CString | 类别：非常量 |
| GetTariffTrend |  | DataTrend | 类别：非常量 |
| GetTaxIncomeFor | Unknown | CFixedPoint | 类别：非常量 |
| GetTaxIncomeTrend |  | DataTrend | 类别：非常量 |
| GetTaxLevelDescHigh |  | CString | 类别：非常量 |
| GetTaxLevelDescLow |  | CString | 类别：非常量 |
| GetTaxLevelDescMedium |  | CString | 类别：非常量 |
| GetTaxLevelDescVeryHigh |  | CString | 类别：非常量 |
| GetTaxLevelDescVeryLow |  | CString | 类别：非常量 |
| GetTensionIconTexture | Country | Unknown | 类别：非常量 |
| GetTensionTooltip | Country | CString | 类别：非常量 |
| GetTensionWith | Country | int32 | 类别：非常量 |
| GetTensionWithDesc | Country | CString | 类别：非常量 |
| GetTimeUntilTargetReachedArmy |  | CString | 类别：非常量 |
| GetTimeUntilTargetReachedNavy |  | CString | 类别：非常量 |
| GetTimedModifierDurationRemaining | Modifier | CString | 类别：非常量 |
| GetTimedModifiers |  | Unknown | 类别：非常量 |
| GetTooltipTag |  | CString | 类别：非常量 |
| GetTopOverlord |  | Country | 类别：非常量 |
| GetTotalAgitatorSlots |  | int32 | 类别：非常量 |
| GetTotalExpensesTrend |  | DataTrend | 类别：非常量 |
| GetTotalExportedAmount |  | CFixedPoint | 类别：非常量 |
| GetTotalForeignConstructions |  | int32 | 类别：非常量 |
| GetTotalGovernmentClout |  | CFixedPoint | 类别：非常量 |
| GetTotalImportedAmount |  | CFixedPoint | 类别：非常量 |
| GetTotalIncomeTrend |  | DataTrend | 类别：非常量 |
| GetTotalLeverageFactors |  | CFixedPoint | 类别：非常量 |
| GetTotalLeverageFactorsBreakdown |  | CString | 类别：非常量 |
| GetTotalLeverageFactorsWithResistance |  | CFixedPoint | 类别：非常量 |
| GetTotalLeverageFactorsWithResistanceBreakdown |  | CString | 类别：非常量 |
| GetTotalLiteracyRanking |  | CString | 类别：非常量 |
| GetTotalLiteracyRate |  | CFixedPoint | 类别：非常量 |
| GetTotalMarginalClout |  | CFixedPoint | 类别：非常量 |
| GetTotalNumLoyalistsChange |  | int64 | 类别：非常量 |
| GetTotalNumLoyalistsDecrease |  | int64 | 类别：非常量 |
| GetTotalNumLoyalistsIncrease |  | int64 | 类别：非常量 |
| GetTotalNumRadicalsChange |  | int64 | 类别：非常量 |
| GetTotalNumRadicalsDecrease |  | int64 | 类别：非常量 |
| GetTotalNumRadicalsIncrease |  | int64 | 类别：非常量 |
| GetTotalOppositionClout |  | CFixedPoint | 类别：非常量 |
| GetTotalPopulation |  | int64 | 类别：非常量 |
| GetTotalUrbanization |  | int32 | 类别：非常量 |
| GetTreatiesBrokenFromNeutralityDesc | DiplomaticPlay | CString | 类别：非常量 |
| GetTreatiesExpenseTrend |  | DataTrend | 类别：非常量 |
| GetTreatiesIncomeTrend |  | DataTrend | 类别：非常量 |
| GetTreatiesWith | Country | Unknown | 类别：非常量 |
| GetTreatiesWithDesc | Country | CString | 类别：非常量 |
| GetTruceDate | Country | CString | 类别：非常量 |
| GetUnclaimedLeverage |  | CFixedPoint | 类别：非常量 |
| GetUnclaimedLeverageFormatted |  | CString | 类别：非常量 |
| GetUnclaimedLeverageShare |  | CFixedPoint | 类别：非常量 |
| GetUnclaimedLeverageShareTarget |  | CFixedPoint | 类别：非常量 |
| GetUnclaimedLeverageTarget |  | CFixedPoint | 类别：非常量 |
| GetUnemployedWorkingAdults |  | int64 | 类别：非常量 |
| GetUnenforcedTreaties |  | Unknown | 类别：非常量 |
| GetUnenforcedTreatiesWith | Country | Unknown | 类别：非常量 |
| GetUnenforcedTreatiesWithDesc | Unknown | CString | 类别：非常量 |
| GetUnrealizedTaxes |  | CFixedPoint | 类别：非常量 |
| GetUpperStrataPopulationTrend |  | DataTrend | 类别：非常量 |
| GetUsedAgitatorSlots |  | int32 | 类别：非常量 |
| GetUsedFreeCharters |  | int32 | 类别：非常量 |
| GetWarships |  | int32 | 类别：非常量 |
| GetWeeklyBalance |  | CFixedPoint | 类别：非常量 |
| GetWeeklyCostArmy |  | CFixedPoint | 类别：非常量 |
| GetWeeklyCostNavy |  | CFixedPoint | 类别：非常量 |
| GetWeeklyExpenses |  | CFixedPoint | 类别：非常量 |
| GetWeeklyFixedExpenses |  | CFixedPoint | 类别：非常量 |
| GetWeeklyGDP |  | CFixedPoint | 类别：非常量 |
| GetWeeklyIncome |  | CFixedPoint | 类别：非常量 |
| GetWeeklyInnovation |  | CFixedPoint | 类别：非常量 |
| GetWeeklyInnovationDesc |  | CString | 类别：非常量 |
| GetWeeklyInterestRate |  | CFixedPoint | 类别：非常量 |
| GetWeeklyLeverageGain | PowerBloc | CFixedPoint | 类别：非常量 |
| GetWeeklyLibertyDesireChange |  | CFixedPoint | 类别：非常量 |
| GetWeeklyLibertyDesireChangeDesc |  | CString | 类别：非常量 |
| GetWeeklyLibertyDesireChangeFromSupportIndependence |  | CFixedPoint | 类别：非常量 |
| GetWeeklyLibertyDesireChangeFromSupportIndependenceDesc |  | CString | 类别：非常量 |
| GetWeeklyMaxInnovation |  | CFixedPoint | 类别：非常量 |
| GetWeeklyMaxInnovationDesc |  | CString | 类别：非常量 |
| GetWeeklyRawInnovation |  | CFixedPoint | 类别：非常量 |
| GetWeeklyResearchSpeed |  | CFixedPoint | 类别：非常量 |
| GetWeeklyResearchSpeedDesc |  | CString | 类别：非常量 |
| GetWeeklyTechnologyProgressDescForTech | Technology | CString | 类别：非常量 |
| GetWeeklyTechnologySpreadBreakdown |  | CString | 类别：非常量 |
| GetWeeklyTechnologySpreadDesc |  | CString | 类别：非常量 |
| GetWeeklyTechnologySpreadForTechDesc | Technology | CString | 类别：非常量 |
| GetWeeklyTemporaryExpenses |  | CFixedPoint | 类别：非常量 |
| GetWeeklyTemporaryIncome |  | CFixedPoint | 类别：非常量 |
| GetWelfarePaymentsExpenses |  | CFixedPoint | 类别：非常量 |
| GetWelfarePaymentsTrend |  | DataTrend | 类别：非常量 |
| GetWorkingAdults |  | int64 | 类别：非常量 |
| GetYearlyInterestRate |  | CFixedPoint | 类别：非常量 |
| GetYouOrCountryName |  | CString | 类别：非常量 |
| GetZeroBalancePlotPoints |  | Unknown | 类别：非常量 |
| GetZeroMoneyPlotPoints |  | Unknown | 类别：非常量 |
| HasActiveDiplomacy |  | bool |  |
| HasAnyAllianceLikeTreatiesWith | Unknown | bool |  |
| HasAnySlavery |  | bool |  |
| HasAnyTaxes |  | bool |  |
| HasConstructionQueued |  | bool |  |
| HasCurrentlyResearchedTechnology |  | bool |  |
| HasDamagedConvoys |  | bool |  |
| HasDeclaredInterest | Unknown | bool |  |
| HasDecreasingInterests |  | bool |  |
| HasDiplomaticPactWith | Unknown Unknown | bool |  |
| HasElectionTrendData |  | bool |  |
| HasElections |  | bool |  |
| HasExportSubventionsHigh | Goods | bool |  |
| HasExportSubventionsLow | Goods | bool |  |
| HasExportSubventionsMax | Goods | bool |  |
| HasExportTariffsHigh | Goods | bool |  |
| HasExportTariffsLow | Goods | bool |  |
| HasExportTariffsMax | Goods | bool |  |
| HasExportTariffsNone | Goods | bool |  |
| HasForeignInvestmentRights | Country | bool |  |
| HasGovernmentWages |  | bool |  |
| HasHeir |  | bool |  |
| HasHigherUnclaimedLeverage |  | bool |  |
| HasHigherUnclaimedLeverageTarget |  | bool |  |
| HasIGApprovalFromLoyalists |  | bool |  |
| HasIGApprovalFromRadicals |  | bool |  |
| HasImportSubventionsHigh | Goods | bool |  |
| HasImportSubventionsLow | Goods | bool |  |
| HasImportSubventionsMax | Goods | bool |  |
| HasImportTariffsHigh | Goods | bool |  |
| HasImportTariffsLow | Goods | bool |  |
| HasImportTariffsMax | Goods | bool |  |
| HasImportTariffsNone | Goods | bool |  |
| HasInterestIn | StrategicRegion | bool |  |
| HasMilitaryWages |  | bool |  |
| HasNewProductionMethodInGroup | ProductionMethodGroup | bool |  |
| HasNewProductionMethodInSameGroup | BuildingType ProductionMethod | bool |  |
| HasObjective |  | bool |  |
| HasOverlappingInterestsWith | Unknown | bool |  |
| HasOwningCompany |  | bool |  |
| HasProgressingLawEnactment |  | bool |  |
| HasRuler |  | bool |  |
| HasSelectedLaw |  | bool |  |
| HasSpecialSocialHierarchy |  | bool |  |
| InDefault |  | bool |  |
| IsAI |  | bool |  |
| IsAIOrOtherPlayer |  | bool |  |
| IsAlliedInDiploPlayWith | Country | bool |  |
| IsAnySubjectOf | Unknown | bool |  |
| IsAtWar |  | bool |  |
| IsAtWarWith | Country | bool |  |
| IsBeingHighlighted |  | bool |  |
| IsBeingTutorialHighlighted |  | bool |  |
| IsColonizable |  | bool |  |
| IsCommittedInDiplomaticPlay |  | bool |  |
| IsConscripting |  | bool |  |
| IsConstructionPaused |  | bool |  |
| IsDead |  | bool |  |
| IsDiplomaticallyRelevantCountry | Unknown | bool |  |
| IsEconomyHealthy |  | bool |  |
| IsEconomyHealthyDesc |  | CString |  |
| IsEnactingLaw |  | bool |  |
| IsHighestRank |  | bool |  |
| IsIgnoringCountryFormation | CountryFormation | bool |  |
| IsIgnoringDecision | Decision | bool |  |
| IsInElectionCampaignPeriod |  | bool |  |
| IsInPowerBloc |  | bool |  |
| IsInsurrectionary |  | bool |  |
| IsInvolvedInActiveConflict |  | bool |  |
| IsLocalPlayer |  | bool |  |
| IsLowestRank |  | bool |  |
| IsMobilized |  | bool |  |
| IsNegotiating |  | bool |  |
| IsNeighborsWith | Unknown | bool |  |
| IsNewProductionMethod | ProductionMethod | bool |  |
| IsObjectiveIdle |  | bool |  |
| IsOtherPlayer |  | bool |  |
| IsPinnedInOutliner |  | bool |  |
| IsPlayer |  | bool |  |
| IsPowerBlocLeader |  | bool |  |
| IsPowerStruggling |  | bool |  |
| IsRank | Unknown | bool |  |
| IsRevolutionary |  | bool |  |
| IsSecessionist |  | bool |  |
| IsSubject |  | bool |  |
| IsSubjectOf | Country | bool |  |
| IsTaxingAnyGood |  | bool |  |
| IsValid |  | bool |  |
| LeavePowerBloc |  | Command |  |
| MakeScope |  | Scope |  |
| MobilizeAllArmies |  | Command |  |
| OwesObligationTo | Unknown | bool |  |
| PauseConstruction |  | Command |  |
| PauseConstructionTooltip |  | CString |  |
| PredictBalanceWithoutTemporaryIncomeAndExpenses |  | CFixedPoint |  |
| PredictConsumptionTaxes |  | CFixedPoint |  |
| PredictDiplomaticPactsExpenses |  | CFixedPoint |  |
| PredictDiplomaticPactsExpensesDesc |  | CString |  |
| PredictDiplomaticPactsIncome |  | CFixedPoint |  |
| PredictDiplomaticPactsIncomeDesc |  | CString |  |
| PredictDividendsTaxes |  | CFixedPoint |  |
| PredictDividendsTaxesDesc |  | CString |  |
| PredictEconomyHealthDesc |  | CString |  |
| PredictGovernmentShareDividends |  | CFixedPoint |  |
| PredictGovernmentShareDividendsDesc |  | CString |  |
| PredictGovernmentShareLosses |  | CFixedPoint |  |
| PredictGovernmentShareLossesDesc |  | CString |  |
| PredictGovernmentWagesExpenses |  | CFixedPoint |  |
| PredictMaxWeeklyTechnologyProgressForTech | Unknown | CFixedPoint |  |
| PredictMilitaryWagesExpenses |  | CFixedPoint |  |
| PredictMinWeeklyTechnologyProgressForTech | Unknown | CFixedPoint |  |
| PredictMinting |  | CFixedPoint |  |
| PredictMintingDesc |  | CString |  |
| PredictTariffs |  | CFixedPoint |  |
| PredictTariffsDesc |  | CString |  |
| PredictTotalMilitaryExpenses |  | CFixedPoint |  |
| PredictTreatyExpenses |  | CFixedPoint |  |
| PredictTreatyExpensesDesc |  | CString |  |
| PredictTreatyIncome |  | CFixedPoint |  |
| PredictTreatyIncomeDesc |  | CString |  |
| PredictWeeklyBalance |  | CFixedPoint |  |
| PredictWeeklyBalanceWithEconomyHealthHint |  | CString |  |
| PredictWeeklyFixedIncome |  | CFixedPoint |  |
| PredictWeeklyIncome |  | CFixedPoint |  |
| RemoveCompany | CompanyType | Command |  |
| ResumeConstruction |  | Command |  |
| ResumeConstructionTooltip |  | CString |  |
| Self |  | Country |  |
| SetExportSubventionsHigh | Goods | Command |  |
| SetExportSubventionsLow | Goods | Command |  |
| SetExportSubventionsMax | Goods | Command |  |
| SetExportTariffsHigh | Goods | Command |  |
| SetExportTariffsLow | Goods | Command |  |
| SetExportTariffsMax | Goods | Command |  |
| SetExportTariffsNone | Goods | Command |  |
| SetGovernmentWageLevelHigh |  | Command |  |
| SetGovernmentWageLevelLow |  | Command |  |
| SetGovernmentWageLevelMedium |  | Command |  |
| SetGovernmentWageLevelVeryHigh |  | Command |  |
| SetGovernmentWageLevelVeryLow |  | Command |  |
| SetImportSubventionsHigh | Goods | Command |  |
| SetImportSubventionsLow | Goods | Command |  |
| SetImportSubventionsMax | Goods | Command |  |
| SetImportTariffsHigh | Goods | Command |  |
| SetImportTariffsLow | Goods | Command |  |
| SetImportTariffsMax | Goods | Command |  |
| SetImportTariffsNone | Goods | Command |  |
| SetMilitaryWageLevelHigh |  | Command |  |
| SetMilitaryWageLevelLow |  | Command |  |
| SetMilitaryWageLevelMedium |  | Command |  |
| SetMilitaryWageLevelVeryHigh |  | Command |  |
| SetMilitaryWageLevelVeryLow |  | Command |  |
| SetTaxLevelHigh |  | Command |  |
| SetTaxLevelLow |  | Command |  |
| SetTaxLevelMedium |  | Command |  |
| SetTaxLevelVeryHigh |  | Command |  |
| SetTaxLevelVeryLow |  | Command |  |
| ShowInvestmentPoolPredictedNextBuilding |  | bool |  |
| SortCompanies | Unknown | void |  |
| SortCultures | CString | void |  |
| SortReligions | CString | void |  |
| SortStates | Unknown | void |  |
| SortSubjects | CString | void |  |
| StartNegotiationWith | InterestGroup | Command |  |
| ToggleIgnoreCountryFormation | CountryFormation | Command |  |
| ToggleIgnoreDecision | Decision | Command |  |
| TogglePinInOutliner |  | void |  |
| TryGetOverlordTooltipEntry |  | CString |  |
| TryGetSubjectsTooltipEntry |  | CString |  |
| 函数 | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessSelf |  | CountryDefinition | 类别：const |
| GetAdjective |  | CString | 类别：nonconst |
| GetBaseFlag |  | CoatOfArms | 类别：nonconst |
| GetColor |  | CVector4f | 类别：nonconst |
| GetCustom | CustomLocalization | CString | 类别：nonconst |
| GetFlag | CString | CoatOfArms | 类别：nonconst |
| GetName |  | CString | 类别：nonconst |
| GetPrimaryCulture |  | Culture | 类别：nonconst |
| GetPrimaryCultureName |  | CString | 类别：nonconst |
| GetTier |  | CString | 类别：nonconst |
| GetTooltipTag |  | CString | 类别：nonconst |
| IsValid |  | bool |  |
| MakeScope |  | Scope |  |
| Self |  | CountryDefinition |  |

| 函数 | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessFormationCandidates |  | Unknown | 类别：const |
| AccessFormationCultureCountries |  | Unknown | 类别：const |
| AccessFormationStateRegions |  | Unknown | 类别：const |
| AccessSelf |  | CountryFormation | 类别：const |
| CanFormCountry | Unknown | bool |  |
| CanLaunchLeadershipPlay | Country | bool |  |
| CanLaunchUnificationPlay |  | bool |  |
| ControlsStateRegion | Country StateRegion | bool |  |
| FormCountry | Country | Command |  |
| GetAdjective |  | CString | 类别：nonconst |
| GetControlsStateRegionDesc | Country StateRegion | CString | 类别：nonconst |
| GetCustom | CustomLocalization | CString | 类别：nonconst |
| GetDefinition |  | CountryDefinition | 类别：nonconst |
| GetFormDesc | Country | CString | 类别：nonconst |
| GetName |  | CString | 类别：nonconst |
| GetNumControlledStates | Country | int32 | 类别：nonconst |
| GetNumRequiredStates |  | int32 | 类别：nonconst |
| GetNumSupportingCountries | Country | int32 | 类别：nonconst |
| GetSupportCandidateDesc | Country Country | CString | 类别：nonconst |
| GetSupportForAllCandidatesDesc | Country | CString | 类别：nonconst |
| GetSupportForCandidateBreakdown | Unknown Unknown | CString | 类别：nonconst |
| GetSupportedCandidateCountry | Unknown | Country | 类别：nonconst |
| GetSupportingCountriesDesc | Country | CString | 类别：nonconst |
| GetTooltipTag |  | CString | 类别：nonconst |
| GetTotalNumStates |  | int32 | 类别：nonconst |
| GetTriggerLeadershipPlayDesc | Country Country | CString | 类别：nonconst |
| GetTriggerUnificationPlayDesc | Country | CString | 类别：nonconst |
| IsCandidateForFormation | Unknown | bool |  |
| IsMajorFormation |  | bool |  |
| IsSupportingAnyCandidate | Unknown | bool |  |
| IsSupportingCandidate | Unknown Unknown | bool |  |
| ListCultures |  | CString |  |
| ListRequiredStates | Country | CString |  |
| MakeScope |  | Scope |  |
| Self |  | CountryFormation |  |
| ShowLeadershipPlayConfirmation | Unknown | void |  |
| ShowUnificationPlayConfirmation |  | void |  |
| SupportCandidate | Unknown Unknown | Command |  |

| 提升 | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessActiveLawFromGroup | LawGroup | Law | 类别：const |
| AccessCapital |  | State | 类别：const |
| AccessCurrentlyResearchedTechnology |  | Technology | 类别：const |
| AccessDefinition |  | CountryDefinition | 类别：const |
| AccessFirstMarket |  | Market | 类别：const |
| AccessGovernment |  | GovernmentType | 类别：const |
| AccessHeaviestJournalEntry |  | JournalEntry | 类别：const |
| AccessHeir |  | Character | 类别：const |
| AccessLawBeingEnacted |  | Law | 类别：const |
| AccessModifier |  | Modifier | 类别：const |
| AccessOverlord |  | Country | 类别：const |
| AccessPowerBloc |  | PowerBloc | 类别：const |
| AccessRuler |  | Character | 类别：const |
| AccessStateReligion |  | Religion | 类别：const |
| AccessTopOverlord |  | Country | 类别：const |
| CalcLibertyDesireLevel |  | LibertyDesireLevel |  |
| GetActiveLawFrom | Unknown | Law | 类别：nonconst |
| GetActiveLawFromGroup | LawGroup | Law | 类别：nonconst |
| GetAttitudeTowards | Country | AIAttitude | 类别：nonconst |
| GetCapital |  | State | 类别：nonconst |
| GetCurrentlyResearchedTechnology |  | Technology | 类别：nonconst |
| GetDefinition |  | CountryDefinition | 类别：nonconst |
| GetDiplomaticAction | Unknown Unknown | DiplomaticAction | 类别：nonconst |
| GetDiplomaticActionWithStates | Unknown Unknown Unknown Unknown | DiplomaticAction | 类别：nonconst |
| GetElection |  | Election | 类别：nonconst |
| GetFirstPrimaryCulture |  | Culture | 类别：nonconst |
| GetFlag |  | CoatOfArms | 类别：nonconst |
| GetFoodSecurity |  | FoodSecurity | 类别：nonconst |
| GetGovernment |  | GovernmentType | 类别：nonconst |
| GetGovernmentLegitimacyLevel |  | LegitimacyLevel | 类别：nonconst |
| GetHeir |  | Character | 类别：nonconst |
| GetInterestGroupOfType | InterestGroup | InterestGroup | 类别：nonconst |
| GetJournalEntry | Unknown | JournalEntry | 类别：nonconst |
| GetLawBeingEnacted |  | Law | 类别：nonconst |
| GetLawBeingEnactedFromGroup | Unknown | Law | 类别：nonconst |
| GetMarket |  | Market | 类别：nonconst |
| GetModifier |  | Modifier | 类别：nonconst |
| GetMonopolyCountryOnBuildingType | BuildingType | Country | 类别：nonconst |
| GetNegotiatingInterestGroup |  | InterestGroup | 类别：nonconst |
| GetObjective |  | Objective | 类别：nonconst |
| GetOtherPowerBlocWithHighestLeverage | Unknown | PowerBloc | 类别：nonconst |
| GetOverlord |  | Country | 类别：nonconst |
| GetOwningCompany |  | Company | 类别：nonconst |
| GetPlayer |  | Player | 类别：nonconst |
| GetPowerBloc |  | PowerBloc | 类别：nonconst |
| GetPowerBlocWithHighestLeverage |  | PowerBloc | 类别：nonconst |
| GetPreviousAttitudeTowards | Country | AIAttitude | 类别：nonconst |
| GetRankModifier |  | Modifier | 类别：nonconst |
| GetRuler |  | Character | 类别：nonconst |
| GetSampleLowerStrataPop |  | Pop | 类别：nonconst |
| GetSampleLowerStrataPopForCulture | Unknown | Pop | 类别：nonconst |
| GetSampleMiddleStrataPop |  | Pop | 类别：nonconst |
| GetSampleMiddleStrataPopForCulture | Unknown | Pop | 类别：nonconst |
| GetSampleUpperStrataPop |  | Pop | 类别：nonconst |
| GetSampleUpperStrataPopForCulture | Unknown | Pop | 类别：nonconst |
| GetSelectedLaw |  | Law | 类别：nonconst |
| GetSocialHierarchy |  | SocialHierarchy | 类别：nonconst |
| GetSpecialSocialHierarchy |  | SocialHierarchy | 类别：nonconst |
| GetStateReligion |  | Religion | 类别：nonconst |
| GetSubjectPact |  | DiplomaticPact | 类别：nonconst |
| GetSubjectType |  | SubjectType | 类别：nonconst |
| GetTopOverlord |  | Country | 类别：nonconst |
| MakeScope |  | Scope |  |

| 提升 | 参数 | 输出 | 描述 |
|---|---|---|---|
| GetBaseFlag |  | CoatOfArms | 类别：nonconst |
| GetFlag | CString | CoatOfArms | 类别：nonconst |
| GetPrimaryCulture |  | Culture | 类别：nonconst |
| MakeScope |  | Scope |  |

| 提升 | 参数 | 输出 | 描述 |
|---|---|---|---|
| GetDefinition |  | CountryDefinition | 类别：nonconst |
| GetSupportedCandidateCountry | Country | Country | 类别：nonconst |
| MakeScope |  | Scope |  |

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • Countries • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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