---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Scope
source: https://vic3.paradoxwikis.com/Scope
pageid: 3458
categories: [Potentially_outdated, 1.10, Expand, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。至少部分内容最后一次验证是在 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10。

**scope**（作用域）是与大多数 [effect](Effect.md) 和 [trigger](Trigger.md) 配合使用的代码对象，代表国家、州、利益集团等游戏对象。当前 scope 是 trigger 求值和 effect 执行的上下文。

大多数脚本内容都有特定的 scope 作为其“基础”或 **root**（根）作用域，例如 `country` 或 `state`。各 scope 之间通过 **event target**（事件目标）相互链接，从而实现上下文切换。在 effect 和 trigger 中，迭代器和 [event target](Event target.md) 也可以设定 scope。

大多数 scope 是某个游戏对象的特定实例，在 scope 被调用时确定。某些 scope 引用的是游戏对象的*类型*；这些 scope 的脚本名称中通常带有 type 一词。

*可用 scope 类型的完整列表可在 ~/Paradox Interactive/logs/event_scopes.log 中找到*

## 概述

### 数据库 scope

*Scope* 通常指游戏数据库中定义的一个对象实例。数据库中的定义被称为该 scope 的**类型**。数据库 scope 通常具有以下三个特征：

- 脚本可以通过 [trigger](https://vic3.paradoxwikis.com/Triggers) 从中读取信息
- 脚本可以通过 [effect](https://vic3.paradoxwikis.com/Effects) 向其写入信息
- 脚本可以通过 [event target](https://vic3.paradoxwikis.com/Event_targets) 从一个 scope 切换到另一个 scope

大部分数据库 scope 在游戏初始加载时生成（如地图数据、法律、商品等），另一些则在历史执行期间生成（州、人口、市场等）。scope 也可以在运行时由代码创建（人物生成、国家叛乱、人口拆分等），或由脚本通过保存 scope 按需创建。

### 原始 scope

数字、布尔值（yes/no）和 flag 值（`flag:some_string`）是所谓的**原始 scope**（primitive scope）。它们无法被修改或访问，虽然“数字也是 scope”这一说法对新手来说可能令人困惑，但了解这一点有助于更好地理解一些高级功能或错误日志。

## scope 与脚本编写

*除非另有说明，“scope”一词均指数据库 scope。*

大多数脚本编写，无论 trigger 还是 effect，都是“在 scope 内”进行的。trigger 和 effect 只在特定的 scope 中起作用，因此调用它们的脚本必须处于正确的 scope 中，才能正确检查或影响游戏状态。

例如，`set_ideology` effect 必须在人物 scope 中运行：

类似地，`gold_reserves` trigger 必须在国家 scope 中运行：

某些 effect 和 trigger 可在多种 scope 类型中工作，另一些则完全不需要特定 scope，意味着它们几乎可以在任何地方使用。无 scope 的脚本有时被称为"global"、"any"或"none" scope。在 [effect](Effect.md)、[trigger](Trigger.md) 和 [event target](Event target.md) 的表格中，不需要特定 scope 的脚本以 `none` 标注。

### Root 作用域

脚本内容通常有一个由游戏引擎提供的“基础”scope，具体取决于其执行来源。这被称为 **root** 作用域。对大多数脚本内容而言，这是*国家 scope*。根据脚本来源，游戏引擎还可能提供其他已保存的 scope，例如 `scope:target` 或 `scope:first_country`。如果脚本由 on_action 启动，这种情况非常常见。

### Top 作用域

`top_scope` 是游戏为管理和显示 localization 或 GUI 中的信息而创建的一个临时抽象对象。

### 对象与类型

scope 一般是对象，即某个**类型**（type）的实例。

类型是全局定义，设定其对象的基础特征，例如国家定义中的默认主流文化和首都。例如，某座具体的建筑是一个对象，而该建筑的定义则是一个类型。大多数类型只有有限的 scope 功能或完全没有。某些对象没有独立的类型，或其本身就是类型，例如文化和宗教。类型通常只能在其 scope 中运行有限的 effect 和 trigger，且一般无法持有变量或静态 modifier。

## 访问与使用 scope

主条目：
Event target

### 切换 scope

**Event target**（也称为 *Scope Link*，作用域链接）允许我们从一个 scope 切换到另一个 scope（社区称之为"scoping"；程序员称之为“上下文切换”）。可以通过打开更多嵌套的脚本块来多次切换 scope。每打开一个新的块，缩进应增加一级；块关闭时，缩进应减少一级。保持整洁的缩进有助于一眼看清 [trigger](Trigger.md) 和 [effect](Effect.md) 在什么上下文中被解释。例如：

```
# This starts in the country scope
ruler = {
  interest_group = {
    add_modifier = modifier_failed_coup
  }
}
```

某些 event target 还**需要数据**才能起作用。例如：

```
# This is the country event target. In this case, the target scopes to a country with the GBR definition.
c:GBR = {}

# This is the state region target. In this case, the target scopes to the STATE_ATTICA state region.
s:STATE_ATTICA = {}

# This is the market goods target. In this case, the target scopes to the meat good within a market scope.
market = {
  mg:meat = {}
}
 
```

某些 event target 是**全局链接**，意味着它们可以从任何 scope 中调用。例如：

```
# This will always scope to a country with the definition "FRA"
c:FRA

# This will always scope to the "catholic" religion
rel:catholic

# This will always scope to the "liberal" ideology
ideology:ideology_liberal
```

scope 的 event target 分为两类：上下文型和指定型。

**上下文型 event target** 几乎总是必须在相关的 scope 中使用，因为它们引用的是与当前 scope 相关的 scope，例如国家的首都州或统治者。

| Event target | 描述 | 起始 scope | 目标 scope |
|---|---|---|---|
| active_law | 切换到当前 scope 国家在指定法律组中生效的法律（active_law:lawgroup_trade_policy） | country | law |
| ai_army_comparison | 切换到两国之间的陆军实力对比（示例：value = ai_army_comparison:root） | country | value |
| ai_colonization_value | 切换到目标国家 AI 对某战略区域的殖民意愿（示例：value = ai_colonization_value:root） | strategic_region | value |
| ai_gdp_comparison | 切换到两国之间的 GDP 对比（示例：value = ai_army_comparison:root） | country | value |
| ai_ideological_opinion | 切换到 AI 对 scope 国家就目标国家的意识形态看法（示例：value = ai_ideological_opinion:root） | country | value |
| ai_navy_comparison | 切换到两国之间的海军实力对比（示例：value = ai_navy_comparison:root） | country | value |
| ai_state_value | 切换到目标国家 AI 对拥有当前 scope 州的意愿（示例：value = ai_state_value:root） | state | value |
| ai_subject_value | 切换到目标国家 AI 想将当前 scope 国家作为附属国的意愿（示例：value = ai_subject_value:root） | country | value |
| ai_transit_rights_value | 切换到 AI 想获得通过目标国家过境权的意愿（示例：value = ai_transit_rights_value:root） | country | value |
| ai_treaty_export_value | 切换到目标国家 AI 通过条约出口当前 scope 市场商品的意愿（示例：value = ai_market_export_value:root） | market_goods | value |
| ai_treaty_fairness | 切换到 AI 对与目标国家现有条约条款（对双方而言）公平性的评估（示例：value = ai_treaty_fairness_score:root） | country | value |
| ai_treaty_import_value | 切换到目标国家 AI 通过条约进口当前 scope 市场商品的意愿（示例：value = ai_market_import_value:root） | market_goods | value |
| ai_treaty_port_value | 切换到目标国家 AI 想在当前 scope 州获得条约港的意愿（示例：value = ai_treaty_port_value:root） | state | value |
| ai_treaty_trade_value | 切换到目标国家 AI 进出口当前 scope 市场商品的意愿（示例：value = ai_market_trade_value:root） | market_goods | value |
| ai_treaty_value | 切换到 AI 对与目标国家现有条约条款对自身有利程度的评估（示例：value = ai_treaty_value:root） | country | value |
| amended_treaty | 切换到当前 scope 条约正在修订的条约 | treaty, treaty_options | treaty |
| army_size | 当前 scope 国家的营数量，不含已征召的征召兵 | country | value |
| army_size_including_conscripts | 当前 scope 国家的营数量，含已征召的征召兵 | country | value |
| army_size_including_raised_conscripts | 当前 scope 国家的营数量，含已征召但不含未征召的征召兵 | country | value |
| attached_law | 从修正案 scope 链接到该修正案所附的法律 | amendment | law |
| attacker_side | 从战斗切换到进攻方对应的 BattleSide | battle | battle_side |
| attacker_warleader | 切换到战争的进攻方战争领袖 | war | country |
| average_defense | 返回与国家同属一方的前线上单位的平均防御 | front | value |
| average_expected_sol | 获取当前 scope 的平均预期生活水平 | country, state | value |
| average_offense | 返回与国家同属一方的前线上单位的平均进攻 | front | value |
| average_progressiveness | 获取当前 scope 人物或利益集团的平均进步性 | character, interest_group | value |
| average_sol | 获取当前 scope 的平均生活水平 | country, state | value |
| b | 切换到州中指定键名的建筑，示例：b:building_port | state | building |
| base_price | 获取当前 scope 商品的基础价格 | goods | value |
| battle | 从战斗一方切换到战斗本身 | battle_side | battle |
| binding_period | 获取当前 scope 条约签署时的原始约束期（以天计） | treaty, treaty_options | value |
| building | 切换到相关建筑 | new_combat_unit | building |
| building_levels | 获取当前 scope 国家的非自给建筑总等级数 | country | value |
| cached_ai_coastal_population | 切换到 AI 支出变量中记录的沿海总人口（示例：value = cached_ai_coastal_population） | country | value |
| cached_ai_incorporated_coastal_population | 切换到 AI 支出变量中记录的已设为核心的沿海人口总量（示例：value = cached_ai_incorporated_coastal_population） | country | value |
| cached_ai_incorporated_population | 切换到 AI 支出变量中记录的已设为核心的人口总量（示例：value = cached_ai_incorporated_population） | country | value |
| cached_ai_overseas_subject_population | 切换到 AI 支出变量中记录的直接非相邻附属国人口总量（示例：value = cached_ai_overseas_subject_population） | country | value |
| cached_ai_subject_population | 切换到 AI 支出变量中记录的直接附属国人口总量（示例：value = cached_ai_subject_population） | country | value |
| cached_ai_total_population | 切换到 AI 支出变量中记录的人口总量（示例：value = cached_ai_total_population） | country | value |
| cached_ai_unincorporated_coastal_population | 切换到 AI 支出变量中记录的未设为核心的沿海人口总量（示例：value = cached_ai_unincorporated_coastal_population） | country | value |
| cached_ai_unincorporated_population | 切换到 AI 支出变量中记录的未设为核心的人口总量（示例：value = cached_ai_unincorporated_population） | country | value |
| capital | 切换到国家的首都州 | country | state |
| civil_war | 切换到由当前 scope（革命性）政治运动引发的内战 | political_movement | civil_war |
| civil_war_origin_country | 切换到内战国家的起源国 | country | country |
| colonial_growth_per_colony | 切换到国家的每殖民地殖民增长值（示例：colonial_growth_per_colony > 0） | country | value |
| combat_width | 切换到当前 scope 省份的战斗宽度乘数 | province | value |
| command_limit_num_units | 根据指挥上限，获取指挥官通常能从其军事编队获得的基准单位数量 | character | value |
| commander | 从军事编队切换到其指挥官人物 | military_formation | character |
| commander_military_formation | 切换到人物的军事编队 | character | military_formation |
| company | 切换到当前 scope 国家指定类型的公司（company:company_rheinmetall） | country | company |
| compare_complex_value | 一个比较 trigger，需要一个可解析的字符串参数，会在其使用的上下文中返回该值，例如：scope:root.number_of(armies) | varies | value |
| compare_value | 一个比较 trigger，会在其使用的上下文中返回该值，例如：root.gold | varies | value |
| controller | 切换到对象的控制者 | province, state | country |
| country | 从军事编队或舰船切换到其国家 | military_formation, ship | country |
| country_definition | 切换到国家的定义 | country | country_definition |
| credit | 切换到国家当前可承担的最大信贷额度 | country | value |
| culture | 切换到人口或人物的文化 | character, new_combat_unit, political_movement, pop | culture |
| current_hq | 返回当前 scope 军事编队当前的总部（若编队当前未驻扎在任何总部，则可能无效） | military_formation | hq |
| currently_active_law_in_group | 从某法律切换到该组中当前生效的法律 | law | law |
| currently_enacting_law | 从国家切换到其当前正在制定的法律 | country | law |
| decree_cost | 切换到州发布某法令的费用 authority > decree_cost:decree_road_maintaintenance | state | value |
| defender_side | 从战斗切换到防守方对应的 BattleSide | battle | battle_side |
| defender_warleader | 切换到战争的防守方战争领袖 | war | country |
| defense | 返回单位的防御评分（包括其指挥官的影响） | new_combat_unit | value |
| demoralized | 返回单位士气受损的人力数量 | new_combat_unit | value |
| detection | 从舰队 scope 链接到舰队中舰船的总侦察值 | military_formation | value |
| diplomatic_pact_expense_ratio | 切换到该国外交协定支出与收入之比，限制在 0-1 之间（示例：value = diplomatic_pact_expense_ratio） | country | value |
| diplomatic_pact_other_country | 切换到当前 scope 外交协定中的另一国，示例：diplomatic_pact_other_country(root) | diplomatic_pact | country |
| diplomatic_play | 从战争切换到其外交博弈 | war | diplomatic_play |
| enforced_on_country | 切换到被强制执行条约的 enforced_on_country | treaty | country |
| enforcer_country | 切换到被强制执行条约的 enforcer_country | treaty | country |
| executive | 从公司切换到其高管人物 | company | character |
| first_country | 切换到以下任意一项的 first_country：外交协定、条约、条约选项、条约条款的条约、条约条款选项（仅限双向条款类型） | diplomatic_pact, treaty, treaty_article, treaty_article_options, treaty_options | country |
| flagship | 获取当前 scope 国家的旗舰 | country | ship |
| front | 从多种 scope 切换到前线：从战斗切换到其发生的前线；从人物切换到其所在或正在前往的前线；从军事编队切换到其当前所在的前线；从省份切换到包含该省的前线；从入侵切换到入侵前线 | battle, character, invasion, military_formation, province | front |
| front_length | 返回前线中省份的数量 | front | value |
| gdp | 获取当前 scope 国家或州的年度预测 GDP | country, state | value |
| get_ruler_for | 从国家切换到在指定权力移交类型下将成为统治者的人物 get_ruler_for:parliamentary_elective = { effects... } | country | character |
| goal_value | 切换到日志条目的目标值 | journal_entry | value |
| goods | 从贸易路线的市场商品或州商品切换到其交易的商品 | market_goods, state_goods | goods |
| government_size | 获取当前 scope 国家政府中当前政党与独立利益集团的数量 | country | value |
| group | 从建筑对象或建筑类型切换到其所属组 | building, building_type | building_group |
| heir | 切换到国家的继承人 | country | character |
| home_country | 切换到流亡者的祖国 | character, pop | country |
| home_hq | 返回当前 scope 军事编队的驻地总部 | military_formation | hq |
| ideology | 双重用途：从名称切换到意识形态（ideology:ideology_anarchist）；切换到当前 scope 人物的意识形态 | character, none | ideology |
| ig | 切换到属于该国家的指定键名的利益集团，示例：ig:ig_armed_forces | country, political_movement | interest_group |
| imposed_law | 从国家切换到当前被强加于其的法律（无论是否正在制定） | country | law |
| imposer_of_law | 从国家切换到当前正向其强加法律的国家 | country, law | country |
| income | 获取当前 scope 国家的当前每周收入 | country | value |
| income_transfer_expenses | 切换到当前 scope 国家通过条约和协定向其他国家转移的资金数额（示例：income_transfer_expenses >= 100） | country | value |
| income_transfer_relative_expenses | 切换到国家通过条约和协定向其他国家转移的收入比例（示例：income_transfer_relative_expenses >= 0.2） | country | value |
| infamy | 切换到当前 scope 国家的恶名（示例：infamy >= 2） | country | value |
| initiator | 切换到对象的发起者 | diplomatic_play | country |
| input_building_type | 切换到条约条款中输入的建筑类型 | treaty_article, treaty_article_options | building_type |
| input_company | 切换到条约条款中输入的公司 | treaty_article, treaty_article_options | company |
| input_country | 切换到条约条款中输入的国家 | treaty_article, treaty_article_options | country |
| input_goods | 切换到条约条款中输入的商品 | treaty_article, treaty_article_options | goods |
| input_law | 切换到条约条款中输入的法律 | treaty_article, treaty_article_options | law_type |
| input_market_goods | 切换到条约条款中输入的市场商品（示例：input_market_goods:root） | treaty_article, treaty_article_options | market_goods |
| input_quantity | 切换到条约条款中输入的数量 | treaty_article, treaty_article_options | value |
| input_ship | 切换到条约条款中输入的舰船 | treaty_article, treaty_article_options | ship |
| input_state | 切换到条约条款中输入的州 | treaty_article, treaty_article_options | state |
| input_strategic_region | 切换到条约条款中输入的战略区域 | treaty_article, treaty_article_options | strategic_region |
| institution | 从名称切换到国家的机构（institution:institution_health_system） | country | institution |
| interest_group | 切换到人物的利益集团！ | character | interest_group |
| interest_group_type | 切换到当前 scope 人物的利益集团类型 | character | interest_group_type |
| invasion | 返回当前 scope 前线的入侵（若有） | front | invasion |
| invasion_attacker | 若在入侵 scope 中使用，切换到执行入侵的国家 | invasion | country |
| invasion_defender | 若在入侵 scope 中使用，切换到被攻击州的控制国 | invasion | country |
| investment | 切换到机构的当前投入等级（示例：investment < investment_max） | institution | value |
| investment_max | 切换到国家在机构中的当前最大投入等级（示例：investment < investment_max） | institution | value |
| investment_pool_income | 获取当前 scope 国家的当前每周投资池收入 | country | value |
| is_setup | 若游戏状态正在初始化，则切换到 true/false！ | none | boolean |
| je | 切换到属于该国家的指定键名的日志条目，示例：je:je_antarctica | country | journal_entry |
| je_tutorial | 切换到当前激活教程课程的日志条目（勿在教程之外使用） | none | journal_entry |
| land_controller_hq | 返回省份或州控制者的陆军总部 | province, state | hq |
| land_hq | 返回省份或州所有者的本地陆军总部 | province, state | hq |
| largest_exporting_market | 切换到当前 scope 市场商品向本地市场出口的最大出口市场 | market_goods | market |
| largest_importing_market | 切换到当前 scope 市场商品从本地市场进口的最大进口市场 | market_goods | market |
| law_type | 从名称切换到法律类型（law_type:law_protected_speech），或从当前 scope 的法律切换 | law, none | law_type |
| leader | 切换到利益集团的领袖 | interest_group | character |
| legitimacy | 切换到国家当前的合法性数值 | country | value |
| level | 切换到建筑的等级 | building | value |
| level_after_queued_constructions | 切换到所有排队建设完成后建筑的等级 | building | value |
| lobby_foreign_anti_clout | 切换到所有针对特定国家的反该国外交政策游说团的总政治力量（lobby_foreign_anti_clout:root >= 0.2） | country | value |
| lobby_foreign_pro_clout | 切换到所有针对特定国家的亲该国外交政策游说团的总政治力量（lobby_foreign_pro_clout:root >= 0.2） | country | value |
| lobby_in_government_foreign_anti_clout | 切换到执政的所有针对特定国家的反该国外交政策游说团的总政治力量（lobby_in_government_foreign_anti_clout:root >= 0.2） | country | value |
| lobby_in_government_foreign_pro_clout | 切换到执政的所有针对特定国家的亲该国外交政策游说团的总政治力量（lobby_in_government_foreign_pro_clout:root >= 0.2） | country | value |
| lobby_join_weight | 切换到利益集团加入特定游说团的加入权重（lobby_join_weight:root >= 5） | interest_group | value |
| lobby_war_opposition | 切换到所有反对当前 scope 战争的游说团的总政治力量（lobby_war_opposition:root >= 0.2） | country | value |
| lobby_war_support | 切换到所有支持当前 scope 战争的游说团的总政治力量（lobby_war_support:root >= 0.2） | country | value |
| manpower | 返回单位的人力 | new_combat_unit | value |
| market | 切换到对象的市场 | building, country, market, market_goods, province, state, state_goods, state_region | market |
| market_capital | 切换到国家的市场首都 | country | state |
| market_export_cap | 根据当前 scope 市场商品的产量获取该市场可出口的最大商品数量 | market_goods | value |
| market_import_cap | 基于所 scope 的 MarketGoods 的消费量，获取该市场可进口商品的最大数量 | market_goods | value |
| mass_migration_culture | 从一个州 scope 到大规模迁移的目标文化 | state | culture |
| mg | 从市场 scope 到具有指定键的 MarketGoods（示例：mg:tools） | market | market_goods |
| migration_pull | 获取一个州的迁移吸引力，或一个国家的大规模迁移吸引力。 | country, state | value |
| military_expenses | 获取所 scope 国家的当前军事开支（奴隶、工资和商品） | country | value |
| military_expenses_share | 获取所 scope 国家当前军事开支（奴隶、工资和商品）相对于其总开支的份额 | country | value |
| mobilization | 返回该单位的动员值，介于 0 和 1 之间 | new_combat_unit | value |
| modifier | scope 到当前对象所拥有的、具有指定键的修正类型值，示例：modifier:country_influence_add | battle_side, building, character, country, interest_group, market, power_bloc, state | boolean, value |
| momentum | 获取所 scope 政党的原始势头值 | party | value |
| morale | 返回该单位的士气 | new_combat_unit | value |
| most_desired_law | scope 到该政治运动最希望颁布的法律类型（如果有）。 | political_movement | law_type |
| mutual_trade_value_with_country | scope 到两个市场之间贸易路线中商品的总基础价值（示例：mutual_trade_value_with_country:root >= 1000） | country | value |
| named_script_value | 一个 script value（脚本值），会在其使用的上下文中计算并返回其值 | none | color, value |
| national_awakening_state_region | 从文化 scope 链接到该文化正处于民族觉醒状态的地域 | culture | state_region |
| naval_combat_power | scope 到该国的海军战力（示例：naval_combat_power > 100） | country | value |
| naval_controller_hq | 返回该省份或州的掌控方海军总部 | province | hq |
| naval_hostility_average_damage_dealt | scope 到该国在回顾期内其主动发起的海上敌对行动中造成的平均伤害。如果未找到敌对行动则返回 -1。 | country | value |
| naval_hq | 返回该省份或州拥有者的本地海军总部 | province | hq |
| naval_vulnerability | scope 到一国基于贸易依赖度和沿海 GDP 份额计算的海军脆弱度评分，上限为一个 defines 最大值 | country | value |
| navy_size | 所 scope 国家的分舰队数量。 | country | value |
| nf | scope 到应用于该州的具有指定键的法令，示例：nf:decree_road_maintaintenance | state | decree |
| num_active_interests | scope 到一国拥有的活跃利益数量 num_active_interests > 5 | country | value |
| num_active_natural_interests | scope 到一国拥有的活跃自然利益数量 num_active_natural_interests > 5 | country | value |
| num_active_plays | 获取所 scope 国家当前发起的活跃外交博弈数量 | country | value |
| num_active_ships | 获取一国、指挥官或军事编队的活跃舰船数量，或获取该省份内与指定国家结盟的军事编队的活跃舰船数量 | character, country, military_formation, province | value |
| num_active_ships_in_battle | 获取一国、指挥官或军事编队处于战斗中的活跃舰船数量，或获取该省份内与指定国家结盟的军事编队处于战斗中的活跃舰船数量 | character, country, military_formation, province | value |
| num_active_ships_not_in_battle | 获取一国、指挥官或军事编队未处于战斗中的活跃舰船数量，或获取该省份内与指定国家结盟的军事编队未处于战斗中的活跃舰船数量 | character, country, military_formation, province | value |
| num_admirals | scope 到该国的海军上将数量 | country | value |
| num_alliances | 获取所 scope 国家的同盟总数（示例：num_alliances:root >= 2） | country | value |
| num_alliances_and_defensive_pacts_with_allies | scope 到目标国家与所 scope 国家盟友之间的同盟数量（示例：num_alliances_and_defensive_pacts_with_allies:root >= 2） | country | value |
| num_alliances_and_defensive_pacts_with_rivals | scope 到目标国家与所 scope 国家竞争对手之间的同盟及防御条约数量（示例：num_alliances_and_defensive_pacts_with_rivals:root >= 2） | country | value |
| num_battalions | 返回一名指挥官麾下活跃营的数量 | character | value |
| num_characters | scope 到该国的人物数量 | country | value |
| num_colony_projects | 获取所 scope 国家当前未完成/进行中的殖民地项目数量 | country | value |
| num_commanderless_units | 一个军事编队中由于指挥官的指挥上限而当前没有指挥官的单位数量。注意：被击败的指挥官不指挥单位，即被击败的指挥官越多，无指挥官的单位越多。 | military_formation | value |
| num_commanders | scope 到该国的指挥官数量 | country | value |
| num_defending_battalions | 返回与该国同方在前线参战的单位总数，示例：num_defending_battalions(root) | front | value |
| num_defensive_pacts | scope 到目标国家拥有的防御条约总数（示例：num_defensive_pacts >= 2） | country | value |
| num_garrison_units | 返回驻扎在一个总部的单位数量 | hq | value |
| num_generals | scope 到该国的将军数量 | country | value |
| num_income_transfer_pacts | scope 到目标国家拥有的收入转移（向他人）条约总数（示例：num_income_transfer_pacts >= 2） | country | value |
| num_income_transfer_treaty_articles | scope 到目标国家拥有的收入转移（向他人）条约条款总数（示例：num_income_transfer_treaty_articles >= 2） | country | value |
| num_income_transfers | scope 到目标国家拥有的收入转移（向他人）条约及条约条款总数（示例：num_income_transfers >= 2） | country | value |
| num_incorporated_states | 获取所 scope 国家当前的已整合州数量 | country | value |
| num_interests | scope 到一国拥有的利益数量（包括未激活的）num_interests > 5 | country | value |
| num_mandates | scope 到所 scope 强权集团可用的托管数量（power_bloc.num_mandates > 0） | power_bloc | value |
| num_mobilized_battalions | 返回一名将军麾下已完全动员的单位数量 | character | value |
| num_natural_interests | scope 到一国拥有的自然利益数量（包括未激活的）num_natural_interests > 5 | country | value |
| num_non_destroyed_ships | 获取一国、指挥官或军事编队未被摧毁的舰船数量，或获取该省份内与指定国家结盟的军事编队未被摧毁的舰船数量 | character, country, military_formation, province | value |
| num_non_destroyed_ships_in_battle | 获取一国、指挥官或军事编队处于战斗中且未被摧毁的舰船数量，或获取该省份内与指定国家结盟的军事编队处于战斗中且未被摧毁的舰船数量 | character, country, military_formation, province | value |
| num_non_destroyed_ships_not_in_battle | 获取一国、指挥官或军事编队未处于战斗中且未被摧毁的舰船数量，或获取该省份内与指定国家结盟的军事编队未处于战斗中且未被摧毁的舰船数量 | character, country, military_formation, province | value |
| num_obligations_earned | 从一国 scope 到他国欠其（即其已挣得）的义务数量 | country | value |
| num_pending_events | scope 到所 scope 国家的待处理事件数量，可按一般情况或指定类别 num_pending_events > 0 num_pending_events:enactment > 0 | country | value |
| num_politicians | scope 到该国的政客数量 | country | value |
| num_positive_relations | 获取当前与所 scope 国家关系为正的国家数量 | country | value |
| num_provinces | 获取所 scope 对象当前的省份数量 | front, state, state_region | value |
| num_queued_constructions | scope 到目标国家排队的建筑总数（示例：num_queued_constructions >= 2） | country | value |
| num_queued_government_constructions | scope 到目标国家排队的政府建筑总数（示例：num_queued_government_constructions >= 2） | country | value |
| num_queued_private_constructions | scope 到目标国家排队的私人建筑总数（示例：num_queued_private_constructions >= 2） | country | value |
| num_rivals | scope 到目标国家的竞争对手总数（示例：num_rivals >= 2） | country | value |
| num_ruling_igs | 获取所 scope 国家当前政府中利益集团的数量 | country | value |
| num_shared_rivals | scope 到所 scope 国家与目标国家共同的竞争对手数量（示例：num_shared_rivals:root >= 2） | country | value |
| num_ships | 获取一国、指挥官或军事编队的舰船数量，或获取该省份内与指定国家结盟的军事编队的舰船数量 | character, country, military_formation, province | value |
| num_ships_in_battle | 获取一国、指挥官或军事编队处于战斗中的舰船数量，或获取该省份内与指定国家结盟的军事编队处于战斗中的舰船数量 | character, country, military_formation, province | value |
| num_ships_not_in_battle | 获取一国、指挥官或军事编队未处于战斗中的舰船数量，或获取该省份内与指定国家结盟的军事编队未处于战斗中的舰船数量 | character, country, military_formation, province | value |
| num_states | 获取所 scope 国家当前的州数量 | country | value |
| num_total_battalions | 返回与该国同方在前线上的单位总数，示例：num_total_battalions(root) | front | value |
| num_unincorporated_states | 获取所 scope 国家当前的未整合州数量 | country | value |
| num_units | 获取一名指挥官或军事编队的活跃单位数量 获取该省份内与指定国家结盟的军事编队的活跃单位数量 | character, military_formation, province | value |
| num_units_in_battle | 获取一名指挥官或军事编队处于战斗中的活跃单位数量 获取该省份内与指定国家结盟的军事编队处于战斗中的活跃单位数量 | character, military_formation, province | value |
| num_units_not_in_battle | 获取一名指挥官或军事编队未处于战斗中的活跃单位数量 获取该省份内与指定国家结盟的军事编队未处于战斗中的活跃单位数量 | character, military_formation, province | value |
| num_units_share | 一名指挥官在考虑其指挥上限后所获得的单位份额。示例：如果该人物拥有 30 指挥上限，舰队拥有 60 总指挥上限，编队拥有 50 个分舰队，那么该人物在其战斗中应获得 25 个分舰队） | character | value |
| num_world_market_hub_trade_center_levels | 获取与所 scope 世界市场枢纽州相关联的贸易中心等级总数 | state | value |
| offense | 返回该单位的进攻评分（包括其指挥官的影响） | new_combat_unit | value |
| opposing_commander | 从战斗中的人物 scope 到战斗另一侧的人物 | character | character |
| opposite_battle_side | 从一个战斗侧 scope 到其对立面 | battle_side | battle_side |
| overlord | scope 到所 scope 国家的直接宗主国 | country | country |
| owner | scope 到该对象的拥有国 | building, character, company, country, decree, institution, interest_group, interest_marker, journal_entry, law, market, market_goods, military_formation, new_combat_unit, political_movement, pop, province, state | country |
| owning_company | scope 到拥有所 scope 国家的公司 | country | company |
| parent_law_type | 从修正案 scope 链接到被视为该修正案母法的法律类型 | amendment | law_type |
| participants | 获取所 scope 市场中的参与国总数 | market | value |
| party | scope 到一个利益集团所支持的政党 | interest_group | party |
| pirated_trade_value_by | scope 到目标国家每周从该国劫掠的商品基础价值平均值（示例：pirated_trade_value_by:root >= 50） | country | value |
| player_owed_obligation_days_left | scope 到外交关系 scope 中一项义务的剩余天数（示例：obligation_days_left >= 2） | diplomatic_relations | value |
| political_movement | 如果在人物 scope 中使用，scope 到该人物支持的政治运动。如果在革命内战 scope 中使用，scope 到发起该革命的运动。如果在利益集团 scope 中使用，scope 到该集团的主导运动。 | character, civil_war | political_movement |
| pop_weight_modifier_scale | 获取该人口的权重修正倍率 | pop | value |
| popularity | 获取所 scope 人物的声望，通常介于 -100 到 +100 之间 | character | value |
| population_below_expected_sol | scope 到该州人口中低于其预期生活水平的百分比（0-1） | state | value |
| power_bloc | scope 到所 scope 国家的强权集团 | country | power_bloc |
| power_bloc_leader | scope 到所 scope 强权集团的领导国 | power_bloc | country |
| power_projection | 获取所 scope 编队、单位或舰船的强权投射值 | military_formation, new_combat_unit, ship | value |
| power_struggle_contender | 如果存在强权斗争，scope 到争夺国 | power_bloc | country |
| prev | 上一个 scope | none | varies |
| principal | 获取该国的当前债务本金 | country | value |
| prosperity | scope 到所 scope 公司的繁荣度（示例：prosperity >= 2） | company | value |
| province | 从一个战斗侧 scope 到战斗发生的省份 | battle_side | province |
| py | scope 到该国拥有的具有指定键的活跃政党，示例：py:communist_party | country | party |
| region | scope 到该对象的战略区域！ | building, diplomatic_play, hq, interest_marker, province, state, state_region | strategic_region |
| region_state | scope 到目标国家拥有的州（示例：region_state:BIC） | state_region | state |
| relations | scope 到两国之间的关系（示例：relations:root >= 2） | country | value |
| relations_change_rate | scope 到两国间关系进度的每日变化（示例：relations_change_rate:root > 0） | country | value |
| religion | scope 到国家或国家定义的主流宗教，或人口的宗教 | character, country, country_definition, political_movement, pop | religion |
| remaining_binding_period | 获取所 scope 条约当前剩余的约束期天数 | treaty, treaty_options | value |
| required_construction | 获取所 scope 建筑类型所需的建造量 | building_type | value |
| root | 当前顶层 scope 的头部，例如：事件的接收者、决议的执行者 | none | varies |
| ruler | scope 到一国的统治者 | country | character |
| scope_relations | scope 到外交关系 scope 中的关系值（示例：scope_relations >= 2） | diplomatic_relations | value |
| scope_tension | scope 到外交关系 scope 中的紧张度值（示例：scope_tension >= 2） | diplomatic_relations | value |
| screening | 从舰队 scope 链接到舰队中舰船的总掩护值 | military_formation | value |
| second_country | scope 到以下任意对象的 second_country：外交条约 条约选项 条约条款的条约 条约条款选项（仅限双向条款类型） | diplomatic_pact, treaty, treaty_article, treaty_article_options, treaty_options | country |
| sg | 从一个州 scope 到具有指定键的 StateGoods，示例：sg:wood | state | state_goods |
| ship_fleet | 从舰船 scope 链接到其所属舰队 | ship | military_formation |
| ship_group | 从一艘舰船 scope 到其所属分组，或按名称 scope 到一个舰船分组（ship_group:ship_group_capital_ships） | none, ship | ship_group |
| shipping_lane | scope 到该军事编队或条约条款（商品转移）的航运线 | military_formation, treaty_article | shipping_lanes |
| slaves_role | 从建筑类型 scope 到其奴隶角色的 pop 类型 | building_type | pop_type |
| source_country | scope 到以下任意对象的 source_country：条约条款（仅限单向条款类型）条约条款选项（仅限单向条款类型） | treaty_article, treaty_article_options | country |
| sponsor | 从修正案 scope 链接到资助该修正案的利益集团 | amendment | interest_group |
| state | scope 到该对象所在的州 | building, market, pop, province | state |
| state_region | scope 到一个州所在的地域 | state | state_region |
| target | scope 到该对象的目标 | diplomatic_catalyst, diplomatic_play, journal_entry, political_lobby | varies |
| target_country | scope 到以下任意对象的 target_country：条约条款（仅限单向条款类型）条约条款选项（仅限单向条款类型） | treaty_article, treaty_article_options | country |
| technology_being_researched | scope 到一国当前正在研究的技术 | country | technology |
| techs_researched | scope 到一国当前已研究的科技数量 | country | value |
| tension | scope 到两国之间的紧张度（示例：tension:root >= 2） | country | value |
| theater | 从战斗侧或州 scope 到其战区 | battle_side, state | theater |
| this | 当前 scope | none | varies |
| top_overlord | scope 到所 scope 国家的最上层宗主国 | country | country |
| total_crew_needed | 获取一国所有舰船所需的水手总数 | country | value |
| total_export_value | scope 到所 scope 国家向世界市场出口的总价值（示例：total_export_value >= 1000） | country | value |
| total_import_value | scope 到所 scope 国家从世界市场进口的总价值（示例：total_import_value >= 1000） | country | value |
| total_marine_capacity | 获取一国所有舰队的海军陆战队容量总数 | country | value |
| total_pirated_trade_value | scope 到外交关系 scope 中两国间通过海盗行为劫掠的商品每周基础价值总平均值（示例：total_pirated_trade_value >= 100） | diplomatic_relations | value |
| total_trade_value | scope 到所 scope 国家与世界市场贸易的总价值（示例：total_trade_value >= 1000） | country | value |
| trade_center | scope 到该市场的贸易中心州！ | market | state |
| training_rate | scope 到一栋建筑当前每周的最大训练速率 | building | value |
| treaty | scope 到条约条款所属的条约 | treaty_article | treaty |
| treaty_exports | 获取该商品向所 scope MarketGoods 市场出口的当前条约（非世界市场）出口数量 | market_goods | value |
| treaty_imports | 获取该商品向所 scope MarketGoods 市场进口的当前条约（非世界市场）进口数量 | market_goods | value |
| type | 从一个对象 scope 到其类型 | amendment, building, company, diplomatic_catalyst, diplomatic_play, harvest_condition_area, institution, interest_group, law, political_lobby, political_movement, ship, strait | amendment_type, building_type, company_type, diplomatic_play_type, harvest_condition_type, institution_type, interest_group_type, law_type, political_movement_type, ship_type, strait_type |
| value | 一个数字字面值，例如：1、5.2、-6 | none | value |
| var | 通过名称引用 scope 中先前设置的变量，例如：var:mortal_enemy | varies | varies |
| visibility | 从舰队 scope 链接到舰队中舰船的总可见度 | military_formation | value |
| vulnerability | 从舰队 scope 链接到舰队中舰船的总脆弱度 | military_formation | value |
| war | 从外交博弈 scope 到其战争 | diplomatic_play | war |
| weekly_prosperity_change | scope 到所 scope 公司的每周繁荣度变化（示例：weekly_prosperity_change >= 2） | company | value |
| workplace | scope 到一个人口的工作场所 | pop | building |
| world_market_hub | scope 到与所 scope 州相关联的世界市场枢纽州 | state | state |
**指定 event target** 通常无需 scope，因为它们指向一个特定对象。有些指定 event target 仍然需要特定 scope，因为它们指向某种类型的一个实例，而非唯一对象。指定 scope 的 event target 通常使用冒号 `:` 后跟一个脚本键（script key），例如建筑类型、国家 tag 或州区域。少数使用圆括号代替。

| Event target | 描述 | 来源 scope | 目标 scope |
|---|---|---|---|
| active_law | 转换到当前国家在指定法律组中的现行法律（active_law:lawgroup_trade_policy） | country | law |
| ai_army_comparison | 转换到两国之间的陆军实力对比（示例：value = ai_army_comparison:root） | country | value |
| ai_colonization_value | 转换到目标国家 AI 对殖民某战略区域的意愿（示例：value = ai_colonization_value:root） | strategic_region | value |
| ai_gdp_comparison | 转换到两国之间的 GDP 对比（示例：value = ai_army_comparison:root） | country | value |
| ai_ideological_opinion | 转换到 AI 对当前国家关于目标国家的意识形态看法（示例：value = ai_ideological_opinion:root） | country | value |
| ai_navy_comparison | 转换到两国之间的海军实力对比（示例：value = ai_navy_comparison:root） | country | value |
| ai_state_value | 转换到目标国家 AI 占有当前州的意愿（示例：value = ai_state_value:root） | state | value |
| ai_subject_value | 转换到 AI 希望目标国家将当前国家作为附属国的意愿（示例：value = ai_subject_value:root） | country | value |
| ai_transit_rights_value | 转换到 AI 希望获得穿越目标国家通行权的意愿（示例：value = ai_transit_rights_value:root） | country | value |
| ai_treaty_export_value | 转换到目标国家 AI 通过条约出口当前市场商品的意愿（示例：value = ai_market_export_value:root） | market_goods | value |
| ai_treaty_fairness | 转换到 AI 对与目标国家现有条约条款（对双方）公平程度的评估（示例：value = ai_treaty_fairness_score:root） | country | value |
| ai_treaty_import_value | 转换到目标国家 AI 通过条约进口当前市场商品的意愿（示例：value = ai_market_import_value:root） | market_goods | value |
| ai_treaty_port_value | 转换到目标国家 AI 在当前州获得条约港的意愿（示例：value = ai_treaty_port_value:root） | state | value |
| ai_treaty_trade_value | 转换到目标国家 AI 进出口当前市场商品的意愿（示例：value = ai_market_trade_value:root） | market_goods | value |
| ai_treaty_value | 转换到 AI 对与目标国家现有条约条款对自身有利程度的评估（示例：value = ai_treaty_value:root） | country | value |
| amendment_type | 根据名称转换到修正案类型（amendment_type:key） | none | amendment_type |
| array_define | 引用数组 define 中数值的值：array_define:Namespace\|Name\|Index。索引从 0 开始。 | none | value |
| average_defense | 返回与国家同属一方的前线（Front）上单位的平均防御 | front | value |
| average_offense | 返回与国家同属一方的前线（Front）上单位的平均进攻 | front | value |
| b | 转换到州中指定键的建筑，示例：b:building_port | state | building |
| bg | 根据名称转换到建筑组（bg:bg_logging） | none | building_group |
| bt | 转换到建筑类型，示例：bt:building_tooling_workshops | none | building_type |
| c | 转换到指定 tag 的国家，示例：c:GBR | none | country |
| catalyst_type | 根据名称转换到外交催化类型（catalyst_type:catalyst_relations_level_improved） | none | diplomatic_catalyst_type |
| cd | 转换到指定 tag 的国家定义，示例：cd:FRA | none | country_definition |
| company | 转换到当前国家指定公司类型的公司（company:company_rheinmetall） | country | company |
| company_type | 根据名称转换到公司类型（company_type:company_rheinmetall） | none | company_type |
| compare_complex_value | 一个需要可解析字符串参数的比较 trigger，会在其使用的上下文中返回该值，例如：scope:root.number_of(armies) | varies | value |
| cu | 转换到指定键的文化，示例：cu:welsh | none | culture |
| decree_cost | 转换到州发布某项法令的消耗 authority > decree_cost:decree_road_maintaintenance | state | value |
| define | 引用数值或颜色 define 的值：define:Namespace\|Name | none | value |
| diplomatic_pact_other_country | 转换到当前 scope 外交条约中的另一方国家，示例：diplomatic_pact_other_country(root) | diplomatic_pact | country |
| flag | 一个 localization 键，例如 flag:the_boss | none | flag |
| g | 转换到指定键的商品，示例：g:iron | none | goods |
| get_ruler_for | 从国家转换到在给定权力更迭类型下将成为统治者的人物 get_ruler_for:parliamentary_elective = { effects... } | country | character |
| global_productivity | 转换到全球生产力数值（示例：global_productivity:high_threshold） | none | value |
| global_var | 通过名称引用之前设置的全局变量，例如：global_var:important_thing | none | varies |
| harvest_condition_type | 根据名称转换到收获条件类型（harvest_condition_type:drought） | none | harvest_condition_type |
| i | 转换到指定键的意识形态，示例：i:ideology_patriarchal | none | ideology |
| identity | 根据名称转换到强权集团认同（identity:key） | none | power_bloc_identity |
| ideology | 双重用途：根据名称转换到一个意识形态（ideology:ideology_anarchist）；转换到当前 scope 人物的意识形态 | character, none | ideology |
| ig | 转换到属于该国家的指定键的利益集团，示例：ig:ig_armed_forces | country, political_movement | interest_group |
| ig_trait | 转换到指定键的利益集团特质，示例：ig_trait:ig_trait_xenophobia | none | interest_group_trait |
| ig_type | 转换到利益集团类型，示例：ig_type:ig_landowners | none | interest_group_type |
| infamy_threshold | 转换到用于比较的恶名等级阈值（infamy_threshold:infamous） | none | value |
| input_market_goods | 转换到条约条款中的市场商品输入（示例：input_market_goods:root） | treaty_article, treaty_article_options | market_goods |
| institution | 根据名称转换到国家的机构（institution:institution_health_system） | country | institution |
| je | 转换到属于该国家的指定键的日志条目，示例：je:je_antarctica | country | journal_entry |
| law_type | 根据名称（law_type:law_protected_speech）或从当前 scope 的法律转换到法律类型 | law, none | law_type |
| lobby_foreign_anti_clout | 转换到针对特定国家的所有反该国游说团体的总政治力量（lobby_foreign_anti_clout:root >= 0.2） | country | value |
| lobby_foreign_pro_clout | 转换到针对特定国家的所有亲该国游说团体的总政治力量（lobby_foreign_pro_clout:root >= 0.2） | country | value |
| lobby_in_government_foreign_anti_clout | 转换到针对特定国家的所有执政的反该国游说团体的总政治力量（lobby_in_government_foreign_anti_clout:root >= 0.2） | country | value |
| lobby_in_government_foreign_pro_clout | 转换到针对特定国家的所有执政的亲该国游说团体的总政治力量（lobby_in_government_foreign_pro_clout:root >= 0.2） | country | value |
| lobby_join_weight | 转换到利益集团加入特定游说团体的权重（lobby_join_weight:root >= 5） | interest_group | value |
| lobby_type | 根据名称转换到政治游说类型（lobby_type:lobby_pro_country） | none | political_lobby_type |
| lobby_war_opposition | 转换到反对当前战争的所有游说团体的总政治力量（lobby_war_opposition:root >= 0.2） | country | value |
| lobby_war_support | 转换到支持当前战争的所有游说团体的总政治力量（lobby_war_support:root >= 0.2） | country | value |
| local_var | 通过名称引用之前设置的局部变量，例如：local_var:person_of_interest | none | varies |
| mg | 从市场转换到指定键的市场商品（MarketGoods），（示例：mg:tools） | market | market_goods |
| mobilization_option | 根据名称转换到动员选项（mobilization_option:key） | none | mobilization_option |
| modifier | 转换到属于当前对象的指定键 modifier 类型的值，示例：modifier:country_influence_add | battle_side, building, character, country, interest_group, market, power_bloc, state | boolean, value |
| movement_type | 根据名称转换到政治运动类型（movement_type:movement_religious_majority） | none | political_movement_type |
| mutual_trade_value_with_country | 转换到两个市场之间贸易路线上贸易商品的总基础价值（示例：mutual_trade_value_with_country:root >= 1000） | country | value |
| naval_hostility_damage | 转换到该国在现行海军敌对行动中对另一国造成的伤害点数（示例：naval_hostility_damage:root >= 50） | country | value |
| nf | 转换到应用于该州的指定键的法令，示例：nf:decree_road_maintaintenance | state | decree |
| num_active_ships | 获取国家、指挥官或军事编队的现役船只数量，或获取该省中与指定国家结盟的军事编队的现役船只数量 | character, country, military_formation, province | value |
| num_active_ships_in_battle | 获取国家、指挥官或军事编队正在战斗中的现役船只数量，或获取该省中与指定国家结盟的军事编队正在战斗中的现役船只数量 | character, country, military_formation, province | value |
| num_active_ships_not_in_battle | 获取国家、指挥官或军事编队未在战斗中的现役船只数量，或获取该省中与指定国家结盟的军事编队未在战斗中的现役船只数量 | character, country, military_formation, province | value |
| num_alliances | 获取当前国家的同盟总数（示例：num_alliances:root >= 2） | country | value |
| num_alliances_and_defensive_pacts_with_allies | 转换到目标国家与当前国家盟友之间的同盟数量（示例：num_alliances_and_defensive_pacts_with_allies:root >= 2） | country | value |
| num_alliances_and_defensive_pacts_with_rivals | 转换到目标国家与当前国家竞争对手之间的同盟和防御条约数量（示例：num_alliances_and_defensive_pacts_with_rivals:root >= 2） | country | value |
| num_defending_battalions | 返回与国家同属一方的前线上正在战斗的单位总数，示例：num_defending_battalions(root) | front | value |
| num_non_destroyed_ships | 获取国家、指挥官或军事编队未被击毁的船只数量，或获取该省中与指定国家结盟的军事编队未被击毁的船只数量 | character, country, military_formation, province | value |
| num_non_destroyed_ships_in_battle | 获取国家、指挥官或军事编队正在战斗中的未被击毁船只数量，或获取该省中与指定国家结盟的军事编队正在战斗中的未被击毁船只数量 | character, country, military_formation, province | value |
| num_non_destroyed_ships_not_in_battle | 获取国家、指挥官或军事编队未在战斗中的未被击毁船只数量，或获取该省中与指定国家结盟的军事编队未在战斗中的未被击毁船只数量 | character, country, military_formation, province | value |
| num_pending_events | 转换到当前国家待处理事件的数量，可以是总体数量或指定类别的数量 num_pending_events > 0 num_pending_events:enactment > 0 | country | value |
| num_shared_rivals | 转换到当前国家与目标国家共有的竞争对手数量（示例：num_shared_rivals:root >= 2） | country | value |
| num_ships | 获取国家、指挥官或军事编队的船只数量，或获取该省中与指定国家结盟的军事编队的船只数量 | character, country, military_formation, province | value |
| num_ships_in_battle | 获取国家、指挥官或军事编队正在战斗中的船只数量，或获取该省中与指定国家结盟的军事编队正在战斗中的船只数量 | character, country, military_formation, province | value |
| num_ships_not_in_battle | 获取国家、指挥官或军事编队未在战斗中的船只数量，或获取该省中与指定国家结盟的军事编队未在战斗中的船只数量 | character, country, military_formation, province | value |
| num_ships_of_group | 当前国家或军事编队中指定船只编队的船只数量 | country, military_formation | value |
| num_total_battalions | 返回与国家同属一方的前线上的单位总数，示例：num_total_battalions(root) | front | value |
| num_units | 获取指挥官或军事编队的现役单位数量，或获取该省中与指定国家结盟的军事编队的现役单位数量 | character, military_formation, province | value |
| num_units_in_battle | 获取指挥官或军事编队正在战斗中的现役单位数量，或获取该省中与指定国家结盟的军事编队正在战斗中的现役单位数量 | character, military_formation, province | value |
| num_units_not_in_battle | 获取指挥官或军事编队未在战斗中的现役单位数量，或获取该省中与指定国家结盟的军事编队未在战斗中的现役单位数量 | character, military_formation, province | value |
| p | 转换到指定十六进制键的省份，示例：p:x1A6E5B | none | province |
| pirated_trade_value_by | 转换到目标国家每周从该国掠夺的商品基础价值的平均值（示例：pirated_trade_value_by:root >= 50） | country | value |
| play_type | 根据名称转换到外交博弈类型（play_type:dp_default_treaty_article） | none | diplomatic_play_type |
| pop_type | 根据名称转换到人口类型（pop_type:laborers） | none | pop_type |
| principle | 根据名称转换到强权集团原则（principle:key） | none | power_bloc_principle |
| principle_group | 根据名称转换到强权集团原则组（principle_group:key） | none | power_bloc_principle_group |
| py | 转换到属于该国家的指定键的活跃政党，示例：py:communist_party | country | party |
| rank_value | 转换到特定国家等级的等级值（rank_value:great_power） | none | value |
| region_state | 转换到目标国家拥有的州，（示例：region_state:BIC） | state_region | state |
| rel | 转换到指定键的宗教，示例：rel:catholic | none | religion |
| relations | 转换到两国之间的关系（示例：relations:root >= 2） | country | value |
| relations_change_rate | 转换到两国之间关系进展的每日变化（示例：relations_change_rate:root > 0） | country | value |
| relations_threshold | 转换到用于比较的关系阈值等级（relations_threshold:warm） | none | value |
| s | 转换到指定键的州区域，示例：s:STATE_UTAH | none | state_region |
| scope | 通过名称引用之前保存的 scope，例如：scope:target | none | varies |
| sg | 从州转换到指定键的州商品（StateGoods），示例：sg:wood | state | state_goods |
| ship_group | 从船只转换到其编队，或根据名称转换到船只编队（ship_group:ship_group_capital_ships） | none, ship | ship_group |
| ship_type | 根据名称转换到船只类型（ship_type:ship_type_frigate） | none | ship_type |
| sr | 转换到指定键的战略区域，示例：sr:region_persia | none | strategic_region |
| strait_trade_importance_by | 转换到该国经由目标国家控制的海峡所贸易商品的重要性。控制方控制海峡两侧时累计值会乘以 STRAIT_FULL_CONTROL_TRADE_IMPORTANCE_MULT（示例：strait_trade_importance_by:root >= 100） | country | value |
| strait_type | 根据名称转换到海峡类型（strait_type:key） | none | strait_type |
| tension | 转换到两国之间的紧张度（示例：tension:root >= 2） | country | value |
| tension_threshold | 转换到用于比较的紧张度等级阈值（tension_threshold:warm） | none | value |
| unit_type | 根据名称转换到作战单位类型（unit_type:key） | none | combat_unit_type |
| var | 通过名称引用当前 scope 中之前设置的变量，例如：var:mortal_enemy | varies | varies |
*可用的事件目标（event target）记录在 docs/event_targets.log 中，其中包括所支持的输入与输出 scope 的信息。*

### 链式 scope

scope 可以通过**点连接（dot linkage）**进行链式书写，例如：`a.b.c.` 这有时也被称为"scope 堆叠"或"点链"。它允许快速在各 scope 之间切换，而无需为每一层 scope 新建一个块。点连接不适用于迭代器（iterator）。

例如，要检查是否有任何国家的首都位于某个特定战略区域，以下两种写法返回相同的结果：

不使用点连接

```
any_country = {
    capital = {
        region = sr:<region_name>
    }
}

ruler = {
    interest_group = {
        ig_clout = #
    }
}
```

使用点连接

```
any_country = {
    capital.region = sr:<region_name>
}

ruler.interest_group.ig_clout = #
```

### Scope 断言

`?=` 是断言运算符。它会在尝试进行比较或进入某个 scope 执行脚本之前，先检查该 scope 对象是否存在。

例如，这段脚本：

```
capital ?= state_region.s:STATE_HOME_COUNTIES
```

在功能上与这段脚本完全相同：

```
exists = capital
capital = state_region.s:STATE_HOME_COUNTIES
```

这有助于避免因未设置/空（null）scope 而产生的错误，并使脚本更紧凑。但如果你确实*需要*在出现空 scope 时打印错误——例如在调试时——则应使用 `=` 来让错误正常输出。

### 特殊目标

`root` – 某个脚本实例的*起始 scope（origin scope）*。它取决于脚本从何处执行。虽然它通常是 country scope，但这既不是约定，也不总是一致。如果已提供了 root scope，脚本可以随时切换回该 scope，或将其用于比较。*注意：* *root scope 并不天然就是玩家或国家（country）scope，尽管情况常常如此。*

`prev` – 你的 scope 链中的*上一个 scope*。它可用于访问某个特定 scope 内可用的对象，并快速返回你原先的 scope。`prev` 目标可以链式使用以在 scope 链中"向后回溯"，即 `prev.prev = {}`，但不建议超过两步。

`this` – *当前 scope*。当你进入某个 scope 后，可用它来比较对象的同一性。它常与**迭代器（iterator）**一起使用，或用于你不确定当前 scope 对象是否就是你想要的那个对象的情况（例如，某个日志条目仅限定于单一国家）。

### 已保存的 scope

**已保存的 scope（saved scope）**是一个由脚本定义、指向特定 scope 的事件目标（event target）。已保存的 scope 仅在一条 **effect 链**（文档中称为事件链）的持续期间内存在。将一个对象保存到 scope 后，你就可以在脚本的下游进一步访问该 scope。必要时，也可以使用 `clear_saved_scope` effect 手动清除它们。

scope 使用 `save_scope_as` effect 保存，并通过 `scope:` 事件目标访问。例如：

```
# This effect saves a country with poor relations and then triggers a diplomatic incident with them.
random_country = {
  limit = {
    relations:root < relations_threshold:neutral
  }
  save_scope_as = unfriendly_country
}
create_diplomatic_incident = {
  target = scope:unfriendly_country
  value = 10
}
```

已保存的 scope 会**被转发给由脚本调用的事件和 effect**。已保存的 scope 会一直存在到 effect 链结束，届时即被丢弃。如果一条 effect 链由 on_action 或某些其他系统发起，游戏引擎有时会转发与该 on_action 相关的 scope，例如 `scope:target` 或 `scope:recipient`。只有在该 effect 被调用时可用的 scope 才会被转发。例如：

```
ruler = {
  save_scope_as = ruler_scope # this scope will be forwarded to ruler_event.1
}
trigger_event = ruler_event.1
capital = {
  save_scope_as = capital_scope # this scope was saved after the trigger_event effect, and thus will not be forwarded to ruler_event.1
}
 
```

已保存的 scope 可以通过 `AddScope` 从 UI 传递给 scripted GUI 或 script value/自定义 localization：

- `"[ScriptedGui.Execute( GuiScope.SetRoot( GetPlayer.MakeScope ).AddScope( 'target', CharacterWindow.GetCharacter.MakeScope ).End )]"`
- `"[GuiScope.SetRoot( GetPlayer.MakeScope ).AddScope( 'target', CharacterWindow.GetCharacter.MakeScope).ScriptValue('sval_name')|0]"`

### 数值型 trigger

某些 trigger 可用于数值比较型 trigger——这些 trigger 也可以作为返回 `value` scope 的 scope 链接使用，因此可以放在 scope 堆叠的末尾。

此类 trigger 的文档中通常会有如下一行：

`Traits: <, <=, =, !=, >, >=`

## 迭代器（Iterators）

**迭代器**——也称为列表（list）——是一类 [effect](Effect.md) 或 [trigger](Trigger.md)，会遍历某种类型的所有符合条件的 scope，并将其返回，用于检查 trigger 或执行 effect。

迭代器共有四种类型：一种用于 trigger，三种用于 effect。

| 前缀 | 说明 |
|---|---|
| any_<name> | Trigger scope，检查是否有任意一个返回的 scope 使其中包含的 trigger 为真。可以使用 count op value 或 percent op value 来检查指定的数量或比例；使用 count = all 或 percent = 1 时，则要求所有 scope 都为真；可以将 filter = { <triggers> } 与 count 或 percent 配合使用，以限制返回的 scope |
| every_<name> | Effect scope，对所有返回的 scope 执行 effect。可以使用 limit = { <triggers> } 来缩小返回的 scope 范围 |
| ordered_<name> | Effect scope，对返回的 scope 执行 effect，默认只返回排序中的第一个 scope。使用 order_by = value 来确定排序，从最大正值到最大负值排列。可以使用 limit = { <triggers> } 来缩小返回的 scope 范围。可以使用 position = int 来选择排序中的其他位置，从 0 开始计数。可以使用 min = int 和 max = value 来限制返回哪些以及多少个 scope。可以使用 check_range_bounds = no，以在返回的 scope 数量少于 min 与 max 之间的范围时避免输出错误日志 |
| random_<name> | Effect scope，对单个随机返回的 scope 执行 effect。可以使用 limit = { <triggers> } 来缩小返回的 scope 范围。可以使用 weight = { mtth_blocks } 来为随机选择加权 |

### Trigger 迭代器

另见：
Trigger
Trigger 迭代器均以 `any_` 开头，只要任意一个 scope 满足其中包含的 trigger 即返回真。这一行为可以通过参数 `count op int value` 或 `percent op value [0-1]` 改变，此时要求至少有指定数量或比例的 scope 满足其中包含的 trigger。它们使用常规的[比较运算符](Trigger.md)。

如果使用了 `count` 或 `percent`，还可以使用另一个参数 `filter` 来限定哪些 scope 会被纳入考虑。

取反时，trigger 迭代器的行为类似于默认设置了 `count = all`，即当没有 scope 满足其中包含的 trigger 时返回真；但若实际设置了 `count = all`，行为则会反转回：只要任意一个 scope 不满足其中包含的 trigger 即返回真。

| Trigger | 说明 | 示例 | Scope | 目标 |
|---|---|---|---|---|
| any_active_law | 遍历一个国家所有现行法律 | any_active_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | law |
| any_active_party | 遍历一个国家所有现行政党 | any_active_party = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | party |
| any_character | 遍历全球所有人物 | any_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | character |
| any_character_in_exile_pool | 遍历流亡池中的人物 | any_character_in_exile_pool = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | character |
| any_character_in_void | 遍历虚空（void）中的人物 | any_character_in_void = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | character |
| any_character_role | 遍历当前 scope 人物的所有角色 | any_character_role = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character | character_role |
| any_civil_war | 遍历与当前 scope 国家相关的所有内战 | any_civil_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | civil_war |
| any_cobelligerent_in_diplo_play | 遍历当前 scope 国家在所有外交博弈（包括战争）中的所有共同参战方 | any_cobelligerent_in_diplo_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_cobelligerent_in_war | 遍历当前 scope 国家在所有战争中的所有共同参战方 | any_cobelligerent_in_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_combat_unit | 遍历输入 scope 的所有作战单位 | any_combat_unit = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | battle, building, front, hq, military_formation | new_combat_unit |
| any_company | 遍历一个国家的所有公司 | any_company = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | company |
| any_country | 遍历全球所有国家 | any_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | country |
| any_country_in_<georegion_short_name> | 遍历指定地理区域内的所有国家 | any_country_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | country |
| any_country_strategic_region | 遍历包含当前 scope 国家所拥有州的所有战略区域 | any_country_strategic_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | strategic_region |
| any_decentralized_country | 遍历所有非中央集权的国家 | any_decentralized_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | country |
| any_diplomatic_catalyst | 遍历一个国家近期记忆中的所有外交催化剂 | any_diplomatic_catalyst = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | diplomatic_catalyst |
| any_diplomatic_play | 遍历全球所有外交博弈 | any_diplomatic_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | diplomatic_play |
| any_diplomatically_relevant_country | 遍历一个 country scope 的所有外交相关国家 | any_diplomatically_relevant_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_direct_subject | 层级中直接位于当前国家之下的任意国家 | any_direct_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_enemy_in_diplo_play | 遍历当前 scope 国家在所有外交博弈（包括战争）中的所有敌国 | any_enemy_in_diplo_play = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_enemy_in_war | 遍历当前 scope 国家在所有战争中的所有敌国 | any_enemy_in_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_harvest_condition | 遍历影响某个州、州区域、战略区域或国家的所有收成状况 | any_harvest_condition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state, state_region, strategic_region | harvest_condition |
| any_in_global_list | 遍历全局列表中的所有条目。 | any_in_global_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| any_in_hierarchy | 当前层级中的任意国家，包括当前国家自身 | any_in_hierarchy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_in_list | 遍历列表中的所有条目。 | any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| any_in_local_list | 遍历本地列表中的所有条目。 | any_in_local_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| any_influenced_interest_group | 遍历受某个政治运动影响的所有利益集团 | any_influenced_interest_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_movement | interest_group |
| any_interest_group | 遍历一个国家的所有利益集团 | any_interest_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | interest_group |
| any_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | any_key_in_global_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_key_in_local_variable_map | 遍历本地变量映射中的所有键。 | any_key_in_local_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_key_in_variable_map | 遍历变量映射中的所有键。 | any_key_in_variable_map = { variable = name filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | none |
| any_law | 遍历一个国家的所有法律 | any_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | law |
| any_lobby_member | 遍游说团（lobby）的所有利益集团成员 | any_lobby_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_lobby | interest_group |
| any_market | 遍历全球所有市场 | any_market = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | market |
| any_market_goods | 遍历一个市场中所有活跃的（市场）商品 | any_market_goods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | market | market_goods |
| any_member | 遍历一个政党的所有利益集团成员 | any_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | party | interest_group |
| any_military_formation | 遍历当前存在于输入 scope 的所有军事编队 | any_military_formation = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, hq | military_formation |
| any_neighbouring_state | 遍历与某个州区域相邻的所有州 | any_neighbouring_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state, state_region, strategic_region | state |
| any_overlord_or_above | 层级中位于当前国家之上的任意国家 | any_overlord_or_above = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_owned_country | 遍历当前 scope 公司拥有的所有国家 | any_owned_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | company | country |
| any_participant | 当前 scope 外交条约的双方参与者中的任意一方 | any_participant = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_pact | country |
| any_political_lobby | 遍历一个国家或利益集团中的所有政治游说团 | any_political_lobby = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, interest_group | political_lobby |
| any_political_movement | 遍历一个国家的所有政治运动 | any_political_movement = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | political_movement |
| any_possible_amendment_type | 遍历可添加到当前 scope 法律的修正案类型 | any_possible_amendment_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | law | amendment_type |
| any_potential_party | 遍历一个国家所有潜在的政党 | any_potential_party = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | party |
| any_power_bloc | 遍历所有强权集团 | any_power_bloc = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | power_bloc |
| any_power_bloc_member | 遍历当前 scope 强权集团的所有成员，包括领导者 | any_power_bloc_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | power_bloc | country |
| any_preferred_law | 遍历利益集团所在国家的所有现行及可能的法律，按其对该法律的偏好程度排序 | any_preferred_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | interest_group | law |
| any_primary_culture | 当前 scope 国家或国家定义的主文化 | any_primary_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, country_definition | culture |
| any_province | 遍历当前 scope 州中的所有省份 | any_province = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state | province |
| any_province_in_<georegion_short_name> | 遍历指定地理区域内的所有省份 | any_province_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | province |
| any_rival_country | 被 scope 中国家视为竞争对手的任意国家 | any_rival_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_rivaling_country | 视 scope 中国家为竞争对手的任意国家 | any_rivaling_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_scope_admiral | 遍历以下范围中的所有海军上将：国家、利益集团或军事编队 | any_scope_admiral = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_ally | 遍历一个国家的所有盟友 | any_scope_ally = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_scope_amendment | 遍历当前 scope 法律的修正案 | any_scope_amendment = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | law | amendment |
| any_scope_army | 遍历当前存在于输入 scope 的所有陆军 | any_scope_army = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, hq | military_formation |
| any_scope_article | 遍历当前 scope 条约的条款 | any_scope_article = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty | treaty_article |
| any_scope_article_option | 遍历当前 scope 条约或条约选项（treaty_options）的条款选项 | any_scope_article_option = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | treaty, treaty_options | treaty_article_options |
| any_scope_building | 遍历以下范围中的所有建筑：州、国家 | any_scope_building = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state | building |
| any_scope_character | 遍历以下范围中的所有人物：国家、利益集团或前线 | any_scope_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_country | 遍历在受支持的 scope（目前为：市场、战略区域）中存在的所有国家 | any_scope_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | market, state_region, strategic_region | country |
| any_scope_culture | 遍历 scope 中的所有文化 | any_scope_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state | culture |
| any_scope_diplomatic_pact | scope 中国家的任意外交条约 | any_scope_diplomatic_pact = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | diplomatic_pact |
| any_scope_fleet | 遍历当前存在于输入 scope 的所有舰队 | any_scope_fleet = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, hq | military_formation |
| any_scope_front | 遍历与当前 scope 战争相关的所有前线 | any_scope_front = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | war | front |
| any_scope_general | 遍历以下范围中的所有将军：国家、利益集团、前线或军事编队 | any_scope_general = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_held_interest_marker | 遍历一个国家持有的所有利益标记 | any_scope_held_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | interest_marker |
| any_scope_homeland_state | 遍历所有作为当前 scope 文化家园的州，或当前 scope 国家任一主文化家园的州 | any_scope_homeland_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | character, country | state |
| any_scope_initiator_ally | 遍历外交博弈中发起方的所有盟友 | any_scope_initiator_ally = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_play | country |
| any_scope_interest_marker | 遍历以下范围中的所有利益标记：国家、战略区域 | any_scope_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state_region, strategic_region | interest_marker |
| any_scope_je_involved | 遍历日志条目中的所有参与方 | any_scope_je_involved = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | journal_entry | country |
| any_scope_play_involved | 遍历外交博弈中的所有参与方 | any_scope_play_involved = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_play | country |
| any_scope_politician | 遍历以下范围中的所有政治家：国家或利益集团 | any_scope_politician = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, interest_group, military_formation | character |
| any_scope_pop | 遍历以下范围中的所有人口：国家、州、利益集团、文化 | any_scope_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, culture, interest_group, state | pop |
| any_scope_regional_hqs | 遍历范围公司的各地区总部 | any_scope_regional_hqs = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | company | building |
| any_scope_ship | 遍历国家或军事编队中的所有舰船 | any_scope_ship = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, military_formation | ship |
| any_scope_state | 遍历以下范围中包含省份的所有州：国家、州区域、战区、前线或海峡 | any_scope_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, front, state_region, strait, strategic_region, theater | state |
| any_scope_strait | 遍历在范围州或国家拥有陆地端点的所有海峡 | any_scope_strait = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country, state | strait |
| any_scope_target_ally | 遍历外交博弈中目标方的所有盟友 | any_scope_target_ally = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | diplomatic_play | country |
| any_scope_theater | 遍历国家中的所有战区 | any_scope_theater = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | theater |
| any_scope_treaty | 遍历约束范围国家的所有生效条约 | any_scope_treaty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | treaty |
| any_scope_violate_sovereignty_interested_parties | 遍历所有在范围国家主权遭到侵犯时会产生利害关系的国家 | any_scope_violate_sovereignty_interested_parties = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_scope_violate_sovereignty_wars | 遍历目标国家主权被范围国家侵犯时涉及的所有相关战争 | any_scope_violate_sovereignty_wars = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | war |
| any_scope_war | 遍历与该范围相关的所有战争 | any_scope_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | war |
| any_sea_node_adjacent_state | 遍历与某个州共享海上节点的所有州 | any_sea_node_adjacent_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state | state |
| any_state | 遍历全球所有州 | any_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state |
| any_state_in_<georegion_short_name> | 遍历指定地理区域中的所有州 | any_state_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state |
| any_state_region | 遍历所有州区域 | any_state_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state_region |
| any_state_region_in_<georegion_short_name> | 遍历指定地理区域中的所有州区域 | any_state_region_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | state_region |
| any_strategic_objective | 遍历范围国家的所有战略目标州 | any_strategic_objective = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | state |
| any_strategic_region | 遍历全球所有战略区域 | any_strategic_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | strategic_region |
| any_strategic_region_in_<georegion_short_name> | 遍历指定地理区域中的所有战略区域 | any_strategic_region_in_<georegion_short_name> = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | strategic_region |
| any_subject_of_subject | 层级中位于直接附属国之下的任意国家 | any_subject_of_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_subject_or_below | 层级中位于当前国家之下的任意国家 | any_subject_or_below = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | country |
| any_supporting_character | 遍历支持范围政治运动的所有人物 | any_supporting_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | political_movement | character |
| any_treaty | 遍历所有条约（包括生效条约和草案） | any_treaty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | none | treaty |
| any_valid_mass_migration_culture | 列出范围国家中适合大规模迁移的文化 | any_valid_mass_migration_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country | culture |
| any_war_participant | 遍历一场战争中的所有参与者 | any_war_participant = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | war | country |

### Effect 迭代器

另见：
Effect
effect（游戏内效果脚本）迭代器以 `every_`、`ordered_` 和 `random_` 开头。`every_` 迭代器将其 effect 应用于所有返回的 scope，`ordered_` 迭代器按值比较对返回的 scope 排序，并将 effect 应用于排序中的第一位，而 `random_` 迭代器将其 effect 应用于单个随机返回的 scope。

三者都可以使用参数 `limit` 来应用限制返回哪些 scope 的 trigger。如果这些限制 trigger 足够精确，只返回单个 scope，那么三种迭代器实际上完全相同。

`ordered_` 迭代器可以通过使用参数 `position = int`（从 0 开始索引）返回排序中除第一位以外的 scope。此外，参数 `min = int` 和 `max = value` 可用于限制排序中返回多少个以及哪些 scope。`min` 设定"顶部"位置，使用与 `position` 相同的从 0 开始的索引，而 `max` 决定返回的 scope 数量，取给定值的向下取整结果。如未指定，则 `min = 0` 且 `max = 1`。只设定 `min` 而不设定 `max` 时，`max` 视为等于迭代器列表的大小。使用 min 或 max 时可用 `check_range_bounds = no` 来避免错误日志，否则使用大于列表大小的 min 或 max 会产生错误。

| Effect | 描述 | 示例 | 范围 | 目标 |
|---|---|---|---|---|
| every_active_law | 遍历一个国家中的所有现行法律 | every_active_law = { limit = { <triggers> } #optional <effects> } | country | law |
| every_active_party | 遍历一个国家中的所有活跃政党 | every_active_party = { limit = { <triggers> } #optional <effects> } | country | party |
| every_character | 遍历全球所有人物 | every_character = { limit = { <triggers> } #optional <effects> } | none | character |
| every_character_in_exile_pool | 遍历流放池中的人物 | every_character_in_exile_pool = { limit = { <triggers> } #optional <effects> } | none | character |
| every_character_in_void | 遍历虚空（void）中的人物 | every_character_in_void = { limit = { <triggers> } #optional <effects> } | none | character |
| every_character_role | 遍历范围人物的所有角色 | every_character_role = { limit = { <triggers> } #optional <effects> } | character | character_role |
| every_civil_war | 遍历与范围国家相关的所有内战 | every_civil_war = { limit = { <triggers> } #optional <effects> } | country | civil_war |
| every_cobelligerent_in_diplo_play | 遍历范围国家在所有外交博弈（包括战争）中的所有共同交战国 | every_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional <effects> } | country | country |
| every_cobelligerent_in_war | 遍历范围国家在所有战争中的所有共同交战国 | every_cobelligerent_in_war = { limit = { <triggers> } #optional <effects> } | country | country |
| every_combat_unit | 遍历输入范围的所有作战单位 | every_combat_unit = { limit = { <triggers> } #optional <effects> } | battle, building, front, hq, military_formation | new_combat_unit |
| every_company | 遍历一个国家中的所有公司 | every_company = { limit = { <triggers> } #optional <effects> } | country | company |
| every_country | 遍历全球所有国家 | every_country = { limit = { <triggers> } #optional <effects> } | none | country |
| every_country_in_<georegion_short_name> | 遍历指定地理区域中的所有国家 | every_country_in_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | country |
| every_country_strategic_region | 遍历包含范围国家所拥有州的所有战略区域 | every_country_strategic_region = { limit = { <triggers> } #optional <effects> } | country | strategic_region |
| every_decentralized_country | 遍历所有非中央集权国家 | every_decentralized_country = { limit = { <triggers> } #optional <effects> } | none | country |
| every_diplomatic_catalyst | 遍历一个国家近期记忆中的所有外交催化剂 | every_diplomatic_catalyst = { limit = { <triggers> } #optional <effects> } | country | diplomatic_catalyst |
| every_diplomatic_play | 遍历全球所有外交博弈 | every_diplomatic_play = { limit = { <triggers> } #optional <effects> } | none | diplomatic_play |
| every_diplomatically_relevant_country | 遍历一个国家范围的所有外交相关国家 | every_diplomatically_relevant_country = { limit = { <triggers> } #optional <effects> } | country | country |
| every_direct_subject | 层级中直接位于当前国家之下的任意国家 | every_direct_subject = { limit = { <triggers> } #optional <effects> } | country | country |
| every_enemy_in_diplo_play | 遍历范围国家在所有外交博弈（包括战争）中的所有敌国 | every_enemy_in_diplo_play = { limit = { <triggers> } #optional <effects> } | country | country |
| every_enemy_in_war | 遍历范围国家在所有战争中的所有敌国 | every_enemy_in_war = { limit = { <triggers> } #optional <effects> } | country | country |
| every_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成状况 | every_harvest_condition = { limit = { <triggers> } #optional <effects> } | country, state, state_region, strategic_region | harvest_condition |
| every_in_global_list | 遍历全局列表中的所有项目。 | every_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| every_in_hierarchy | 当前层级中的任意国家，包括当前国家 | every_in_hierarchy = { limit = { <triggers> } #optional <effects> } | country | country |
| every_in_list | 遍历列表中的所有项目。 | every_in_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| every_in_local_list | 遍历局部列表中的所有项目。 | every_in_local_list = { list = name or variable = name limit = { <triggers> } (optional) <effects> } 对由 add_to_(temporary)_list 创建的列表使用 "list" 对由 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| every_influenced_interest_group | 遍历受一个政治运动影响的所有利益集团 | every_influenced_interest_group = { limit = { <triggers> } #optional <effects> } | political_movement | interest_group |
| every_interest_group | 遍历一个国家中的所有利益集团 | every_interest_group = { limit = { <triggers> } #optional <effects> } | country | interest_group |
| every_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | every_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | every_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_key_in_variable_map | 遍历变量映射中的所有键。 | every_key_in_variable_map = { variable = name of the map limit = { <triggers> } <effects> } | none |  |
| every_law | 遍历一个国家中的所有法律 | every_law = { limit = { <triggers> } #optional <effects> } | country | law |
| every_lobby_member | 遍历一个院外集团的所有利益集团成员 | every_lobby_member = { limit = { <triggers> } #optional <effects> } | political_lobby | interest_group |
| every_market | 遍历全球所有市场 | every_market = { limit = { <triggers> } #optional <effects> } | none | market |
| every_market_goods | 遍历一个市场中的所有活跃（市场）商品 | every_market_goods = { limit = { <triggers> } #optional <effects> } | market | market_goods |
| every_member | 遍历一个政党的所有利益集团成员 | every_member = { limit = { <triggers> } #optional <effects> } | party | interest_group |
| every_military_formation | 遍历输入范围当前存在的所有军事编队 | every_military_formation = { limit = { <triggers> } #optional <effects> } | country, front, hq | military_formation |
| every_neighbouring_state | 遍历与当前范围相邻的所有州 注意英式拼写 | every_neighbouring_state = { limit = { <triggers> } #optional <effects> } | country, state, state_region, strategic_region | state |
| every_overlord_or_above | 层级中位于当前国家之上的任意国家 | every_overlord_or_above = { limit = { <triggers> } #optional <effects> } | country | country |
| every_owned_country | 遍历范围公司拥有的所有国家 | every_owned_country = { limit = { <triggers> } #optional <effects> } | company | country |
| every_participant | 范围中外交协定的两个参与方中的任意一方 | every_participant = { limit = { <triggers> } #optional <effects> } | diplomatic_pact | country |
| every_political_lobby | 遍历一个国家或利益集团中的所有政治院外集团 | every_political_lobby = { limit = { <triggers> } #optional <effects> } | country, interest_group | political_lobby |
| every_political_movement | 遍历一个国家中的所有政治运动 | every_political_movement = { limit = { <triggers> } #optional <effects> } | country | political_movement |
| every_possible_amendment_type | 遍历可添加到范围法律的修正案类型 | every_possible_amendment_type = { limit = { <triggers> } #optional <effects> } | law | amendment_type |
| every_potential_party | 遍历一个国家中所有潜在的政党 | every_potential_party = { limit = { <triggers> } #optional <effects> } | country | party |
| every_power_bloc | 遍历所有强权集团 | every_power_bloc = { limit = { <triggers> } #optional <effects> } | none | power_bloc |
| every_power_bloc_member | 遍历范围强权集团的所有成员，包括领袖 | every_power_bloc_member = { limit = { <triggers> } #optional <effects> } | power_bloc | country |
| every_preferred_law | 遍历一个利益集团所在国家中所有现行及可能的法律，按其对该法律的偏好程度排序 | every_preferred_law = { limit = { <triggers> } #optional <effects> } | interest_group | law |
| every_primary_culture | 范围国家或国家定义的主流文化 | every_primary_culture = { limit = { <triggers> } #optional <effects> } | country, country_definition | culture |
| every_province | 遍历范围州中的所有省份 | every_province = { limit = { <triggers> } #optional <effects> } | province | state |
| every_province_in_<georegion_short_name> | 遍历指定地理区域中的所有省份 | every_province_in_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | province |
| every_rival_country | 被范围国家视为对手的任意国家 | every_rival_country = { limit = { <triggers> } #optional <effects> } | country | country |
| every_rivaling_country | 将范围国家视为对手的任意国家 | every_rivaling_country = { limit = { <triggers> } #optional <effects> } | country | country |
| every_scope_admiral | 遍历以下范围中的所有海军上将：国家、利益集团或军事编队 | every_scope_admiral = { limit = { <triggers> } #optional <effects> } | country, front, interest_group, military_formation | character |
| every_scope_ally | 遍历一个国家的所有盟友 | every_scope_ally = { limit = { <triggers> } #optional <effects> } | country | country |
| every_scope_amendment | 遍历范围法律的修正案 | every_scope_amendment = { limit = { <triggers> } #optional <effects> } | law | amendment |
| every_scope_army | 遍历输入范围当前存在的所有陆军 | every_scope_army = { limit = { <triggers> } #optional <effects> } | country, front, hq | military_formation |
| every_scope_article | 遍历范围条约的条款 | every_scope_article = { limit = { <triggers> } #optional <effects> } | treaty | treaty_article |
| every_scope_article_option | 遍历范围条约或 treaty_options 的 article_option | every_scope_article_option = { limit = { <triggers> } #optional <effects> } | treaty, treaty_options | treaty_article_options |
| every_scope_building | 遍历以下范围中的所有建筑：州、国家 | every_scope_building = { limit = { <triggers> } #optional <effects> } | country, state | building |
| every_scope_character | 遍历以下范围中的所有人物：国家、利益集团或前线 | every_scope_character = { limit = { <triggers> } #optional <effects> } | country, front, interest_group, military_formation | character |
| every_scope_country | 遍历在受支持的范围（当前为：市场、州区域、战略区域）中有存在的所有国家 | every_scope_country = { limit = { <triggers> } #optional <effects> } | market, state_region, strategic_region | country |
| every_scope_culture | 遍历该范围中的所有文化 | every_scope_culture = { limit = { <triggers> } #optional <effects> } | country, state | culture |
| every_scope_diplomatic_pact | 范围国家的任意外交协定 | every_scope_diplomatic_pact = { limit = { <triggers> } #optional <effects> } | country | diplomatic_pact |
| every_scope_fleet | 遍历输入范围当前存在的所有舰队 | every_scope_fleet = { limit = { <triggers> } #optional <effects> } | country, hq | military_formation |
| every_scope_front | 遍历与范围战争相关的所有前线 | every_scope_front = { limit = { <triggers> } #optional <effects> } | war | front |
| every_scope_general | 遍历以下范围中的所有将军：国家、利益集团、前线或军事编队 | every_scope_general = { limit = { <triggers> } #optional <effects> } | country, front, interest_group, military_formation | character |
| every_scope_held_interest_marker | 遍历一个国家持有的所有利益标记 | every_scope_held_interest_marker = { limit = { <triggers> } #optional <effects> } | country | interest_marker |
| every_scope_homeland_state | 遍历属于范围文化家园的所有州，或范围国家任一主流文化的家园的所有州 | every_scope_homeland_state = { limit = { <triggers> } #optional <effects> } | country, culture | state |
| every_scope_initiator_ally | 遍历外交博弈中发起方的所有盟友 | every_scope_initiator_ally = { limit = { <triggers> } #optional <effects> } | diplomatic_play | country |
| every_scope_interest_marker | 遍历以下范围中的所有利益标记：国家、州区域、战略区域 | every_scope_interest_marker = { limit = { <triggers> } #optional <effects> } | country, state_region, strategic_region | interest_marker |
| every_scope_je_involved | 遍历日志条目中的所有参与方 | every_scope_je_involved = { limit = { <triggers> } #optional <effects> } | journal_entry | country |
| every_scope_play_involved | 遍历外交博弈中的所有参与方 | every_scope_play_involved = { limit = { <triggers> } #optional <effects> } | diplomatic_play | country |
| every_scope_politician | 遍历以下范围中的所有政治家：国家或利益集团 | every_scope_politician = { limit = { <triggers> } #optional <effects> } | country, front, interest_group, military_formation | character |
| every_scope_pop | 遍历以下范围中的所有人口：国家、州、利益集团、文化 | every_scope_pop = { limit = { <triggers> } #optional <effects> } | country, culture, interest_group, state | pop |
| every_scope_regional_hqs | 遍历范围公司的各地区总部 | every_scope_regional_hqs = { limit = { <triggers> } #optional <effects> } | company | building |
| every_scope_ship | 遍历国家或军事编队中的所有舰船 | every_scope_ship = { limit = { <triggers> } #optional <effects> } | country, military_formation | ship |
| every_scope_state | 遍历以下 scope 中的所有州（含省份）：country、state_region、theater、front 或 strait | every_scope_state = { limit = { <triggers> } #optional <effects> } | country, front, state_region, strait, strategic_region, theater | state |
| every_scope_strait | 遍历在当前 scope 的州或国家中拥有陆地端点的所有海峡 | every_scope_strait = { limit = { <triggers> } #optional <effects> } | country, state | strait |
| every_scope_target_ally | 遍历外交博弈中某一目标的所有盟友 | every_scope_target_ally = { limit = { <triggers> } #optional <effects> } | diplomatic_play | country |
| every_scope_theater | 遍历一个国家中的所有战区 | every_scope_theater = { limit = { <triggers> } #optional <effects> } | country | theater |
| every_scope_treaty | 遍历对当前 scope 国家有约束力的所有生效条约 | every_scope_treaty = { limit = { <triggers> } #optional <effects> } | country | treaty |
| every_scope_violate_sovereignty_interested_parties | 遍历所有会在 scope 中的国家主权被侵犯时对其感兴趣的国家 | every_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional <effects> } | country | country |
| every_scope_violate_sovereignty_wars | 遍历目标国家被 scope 国家侵犯主权时会引发的所有相关战争 | every_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional <effects> } | country | war |
| every_scope_war | 遍历与该 scope 相关的所有战争 | every_scope_war = { limit = { <triggers> } #optional <effects> } | country | war |
| every_sea_node_adjacent_state | 遍历与某个州共享海洋节点的所有州 | every_sea_node_adjacent_state = { limit = { <triggers> } #optional <effects> } | state | state |
| every_state | 遍历全球所有州 | every_state = { limit = { <triggers> } #optional <effects> } | none | state |
| every_state_in_<georegion_short_name> | 遍历指定地理区域内的所有州 | every_state_in_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | state |
| every_state_region | 遍历所有州区域 | every_state_region = { limit = { <triggers> } #optional <effects> } | none | state_region |
| every_state_region_<georegion_short_name> | 遍历指定地理区域内的所有州区域 | every_state_region_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | state_region |
| every_strategic_objective | 遍历当前 scope 国家的所有战略目标州 | every_strategic_objective = { limit = { <triggers> } #optional <effects> } | country | state |
| every_strategic_region | 遍历全球所有战略区域 | every_strategic_region = { limit = { <triggers> } #optional <effects> } | none | strategic_region |
| every_strategic_region_in_<georegion_short_name> | 遍历指定地理区域内的所有战略区域 | every_strategic_region_in_<georegion_short_name> = { limit = { <triggers> } #optional <effects> } | none | strategic_region |
| every_subject_of_subject | 层级中位于直接附属国之下的任何国家 | every_subject_of_subject = { limit = { <triggers> } #optional <effects> } | country | country |
| every_subject_or_below | 层级中位于当前国家之下的任何国家 | every_subject_or_below = { limit = { <triggers> } #optional <effects> } | country | country |
| every_supporting_character | 遍历支持当前 scope 政治运动的所有人物 | every_supporting_character = { limit = { <triggers> } #optional <effects> } | political_movement | character |
| every_treaty | 遍历所有条约（包括生效条约与草案） | every_treaty = { limit = { <triggers> } #optional <effects> } | none | treaty |
| every_valid_mass_migration_culture | 列出当前 scope 国家中符合大规模迁移条件的文化 | every_valid_mass_migration_culture = { limit = { <triggers> } #optional <effects> } | country | culture |
| every_war_participant | 遍历一场战争中的所有参战方 | every_war_participant = { limit = { <triggers> } #optional <effects> } | war | country |
| ordered_active_law | 遍历一个国家中的所有现行法律 | ordered_active_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | law |
| ordered_active_party | 遍历一个国家中的所有活跃政党 | ordered_active_party = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | party |
| ordered_character | 遍历全球所有人物 | ordered_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | character |
| ordered_character_in_exile_pool | 遍历流亡者池中的人物 | ordered_character_in_exile_pool = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | character |
| ordered_character_in_void | 遍历虚无中（the void）的人物 | ordered_character_in_void = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | character |
| ordered_character_role | 遍历当前 scope 人物的所有角色 | ordered_character_role = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character | character_role |
| ordered_civil_war | 遍历与当前 scope 国家相关的所有内战 | ordered_civil_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | civil_war |
| ordered_cobelligerent_in_diplo_play | 遍历 scope 国家在所有外交博弈（包括战争）中的所有共同交战国 | ordered_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_cobelligerent_in_war | 遍历 scope 国家在所有战争中的所有共同交战国 | ordered_cobelligerent_in_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_combat_unit | 遍历输入 scope 的所有作战单位 | ordered_combat_unit = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | battle, building, front, hq, military_formation | new_combat_unit |
| ordered_company | 遍历一个国家中的所有公司 | ordered_company = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | company |
| ordered_country | 遍历全球所有国家 | ordered_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | country |
| ordered_country_in_<georegion_short_name> | 遍历指定地理区域内的所有国家 | ordered_country_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | country |
| ordered_country_strategic_region | 遍历所有包含 scope 国家所拥有州的战略区域 | ordered_country_strategic_region = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | strategic_region |
| ordered_decentralized_country | 遍历所有松散（非中央集权）国家 | ordered_decentralized_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | country |
| ordered_diplomatic_catalyst | 遍历一个国家近期记忆中的所有外交催化剂 | ordered_diplomatic_catalyst = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | diplomatic_catalyst |
| ordered_diplomatic_play | 遍历全球所有外交博弈 | ordered_diplomatic_play = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | diplomatic_play |
| ordered_diplomatically_relevant_country | 遍历一个国家 scope 的所有外交相关国家 | ordered_diplomatically_relevant_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_direct_subject | 层级中直接位于当前国家之下的任何国家 | ordered_direct_subject = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_enemy_in_diplo_play | 遍历 scope 国家在所有外交博弈（包括战争）中的所有敌国 | ordered_enemy_in_diplo_play = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_enemy_in_war | 遍历 scope 国家在所有战争中的所有敌国 | ordered_enemy_in_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_harvest_condition | 遍历影响某个州、州区域、战略区域或国家的所有收成状况 | ordered_harvest_condition = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state, state_region, strategic_region | harvest_condition |
| ordered_in_global_list | 遍历全局列表中的所有项目。list = name 或 variable = name | ordered_in_global_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_in_hierarchy | 当前层级中的任何国家，包括当前国家自身 | ordered_in_hierarchy = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_in_list | 遍历列表中的所有项目。 | ordered_in_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_in_local_list | 遍历局部列表中的所有项目。list = name 或 variable = name | ordered_in_local_list = { list = name or variable = name limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; minimum value of ordering comparison to consider max = script_value #optional, default inf; maximum value of ordering comparison to consider check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| ordered_influenced_interest_group | 遍历受某一政治运动影响的所有利益集团 | ordered_influenced_interest_group = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_movement | interest_group |
| ordered_interest_group | 遍历一个国家中的所有利益集团 | ordered_interest_group = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | interest_group |
| ordered_key_in_global_variable_map | 遍历全局变量映射中的所有键。 | ordered_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | ordered_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_key_in_variable_map | 遍历变量映射中的所有键。 | ordered_key_in_variable_map = { variable = name of the map limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> } | none |  |
| ordered_law | 遍历一个国家中的所有法律 | ordered_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | law |
| ordered_lobby_member | 遍历游说团体的所有利益集团成员 | ordered_lobby_member = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_lobby | interest_group |
| ordered_market | 遍历全球所有市场 | ordered_market = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | market |
| ordered_market_goods | 遍历一个市场中的所有活跃（市场）商品 | ordered_market_goods = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | market | market_goods |
| ordered_member | 遍历一个政党的所有利益集团成员 | ordered_member = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | party | interest_group |
| ordered_military_formation | 遍历当前存在于输入 scope 中的所有军事编队 | ordered_military_formation = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, hq | military_formation |
| ordered_neighbouring_state | 遍历与一个州地区相邻的所有州 | ordered_neighbouring_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state, state_region, strategic_region | state |
| ordered_overlord_or_above | 层级结构中位于当前国家之上的任何国家 | ordered_overlord_or_above = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_owned_country | 遍历 scope 中公司拥有的所有国家 | ordered_owned_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | company | country |
| ordered_participant | 一个 scope 中外交协议的两名参与方中的任意一方 | ordered_participant = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_pact | country |
| ordered_political_lobby | 遍历一个国家或利益集团中的所有政治游说团体 | ordered_political_lobby = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, interest_group | political_lobby |
| ordered_political_movement | 遍历一个国家中的所有政治运动 | ordered_political_movement = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | political_movement |
| ordered_possible_amendment_type | 遍历可被添加到 scope 中法律的所有修正案类型 | ordered_possible_amendment_type = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | law | amendment_type |
| ordered_potential_party | 遍历一个国家中所有潜在的政党 | ordered_potential_party = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | party |
| ordered_power_bloc | 遍历所有强权集团 | ordered_power_bloc = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | power_bloc |
| ordered_power_bloc_member | 遍历 scope 中强权集团的所有成员（包括领导者） | ordered_power_bloc_member = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | power_bloc | country |
| ordered_preferred_law | 遍历利益集团所在国家的所有现行及可能的法律，按其对该法律的偏好程度排序 | ordered_preferred_law = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | interest_group | law |
| ordered_primary_culture | scope 中国家或国家定义的主要文化 | ordered_primary_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, country_definition | culture |
| ordered_province | 遍历 scope 中州的所有省份 | ordered_province = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state | province |
| ordered_province_in_<georegion_short_name> | 遍历指定地理区域中的所有省份 | ordered_province_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | province |
| ordered_rival_country | 被 scope 中国家视为对手的任何国家 | ordered_rival_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_rivaling_country | 与 scope 中国家互为对手的任何国家 | ordered_rivaling_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_scope_admiral | 遍历以下 scope 中的所有海军上将：国家、利益集团或军事编队 | ordered_scope_admiral = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_ally | 遍历一个国家的所有盟友 | ordered_scope_ally = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_scope_amendment | 遍历 scope 中法律的修正案 | ordered_scope_amendment = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | law | amendment |
| ordered_scope_army | 遍历当前存在于输入 scope 中的所有陆军 | ordered_scope_army = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, hq | military_formation |
| ordered_scope_article | 遍历 scope 中条约的所有条款 | ordered_scope_article = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty | treaty_article |
| ordered_scope_article_option | 遍历 scope 中条约的条款选项或条约选项 | ordered_scope_article_option = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | treaty, treaty_options | treaty_article_options |
| ordered_scope_building | 遍历以下 scope 中的所有建筑：州、国家 | ordered_scope_building = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state | building |
| ordered_scope_character | 遍历以下 scope 中的所有人物：国家、利益集团或前线 | ordered_scope_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_country | 遍历在受支持的 scope（当前为：market、state_region、strategic region）中存在的所有国家 | ordered_scope_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | market, state_region, strategic_region | country |
| ordered_scope_culture | 遍历该 scope 中的所有文化 | ordered_scope_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state | culture |
| ordered_scope_diplomatic_pact | scope 中国家的任何外交协议 | ordered_scope_diplomatic_pact = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | diplomatic_pact |
| ordered_scope_fleet | 遍历当前存在于输入 scope 中的所有舰队 | ordered_scope_fleet = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, hq | military_formation |
| ordered_scope_front | 遍历与 scope 中战争相关的所有前线 | ordered_scope_front = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | war | front |
| ordered_scope_general | 遍历以下 scope 中的所有将军：国家、利益集团、前线或军事编队 | ordered_scope_general = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_held_interest_marker | 遍历一个国家持有的所有利益标记 | ordered_scope_held_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | interest_marker |
| ordered_scope_homeland_state | 遍历作为 scope 中文化的家园，或作为 scope 中国家任一主要文化家园的所有州 | ordered_scope_homeland_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, culture | state |
| ordered_scope_initiator_ally | 遍历以下 scope 中发起方的所有盟友：外交博弈 | ordered_scope_initiator_ally = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_play | country |
| ordered_scope_interest_marker | 遍历以下范围内的所有利益标记：country、state_region、strategic region | ordered_scope_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state_region, strategic_region | interest_marker |
| ordered_scope_je_involved | 遍历日志条目的所有相关方 | ordered_scope_je_involved = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | journal_entry | country |
| ordered_scope_play_involved | 遍历以下范围内的所有相关方：diplomatic play | ordered_scope_play_involved = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_play | country |
| ordered_scope_politician | 遍历以下范围内的所有政客：country 或 interest group | ordered_scope_politician = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, interest_group, military_formation | character |
| ordered_scope_pop | 遍历以下范围内的所有人口：country、state、interest group、culture | ordered_scope_pop = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, culture, interest_group, state | pop |
| ordered_scope_regional_hqs | 遍历该 scope 内公司的所有区域总部 | ordered_scope_regional_hqs = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | company | building |
| ordered_scope_ship | 遍历一个国家或军事编队中的所有舰船 | ordered_scope_ship = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, military_formation | ship |
| ordered_scope_state | 遍历以下范围内包含省份的所有州：country、state_region、theater、front 或 strait | ordered_scope_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, front, state_region, strait, strategic_region, theater | state |
| ordered_scope_strait | 遍历在该 scope 的州或国家中拥有陆地端点的所有海峡 | ordered_scope_strait = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country, state | strait |
| ordered_scope_target_ally | 遍历以下范围内某一目标的所有盟友：diplomatic play | ordered_scope_target_ally = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | diplomatic_play | country |
| ordered_scope_theater | 遍历以下范围内的所有战区：country | ordered_scope_theater = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | theater |
| ordered_scope_treaty | 遍历对该 scope 国家有约束力的所有生效条约 | ordered_scope_treaty = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | treaty |
| ordered_scope_violate_sovereignty_interested_parties | 遍历所有会因该 scope 内国家主权被侵犯而感兴趣的国家 | ordered_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_scope_violate_sovereignty_wars | 遍历目标国家主权被该 scope 国家侵犯时的所有相关战争 | ordered_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | war |
| ordered_scope_war | 遍历与该 scope 相关的所有战争 | ordered_scope_war = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | war |
| ordered_sea_node_adjacent_state | 遍历与某个州共享海洋节点的所有州 | ordered_sea_node_adjacent_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state | state |
| ordered_state | 遍历全球所有州 | ordered_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state |
| ordered_state_in_<georegion_short_name> | 遍历指定地理区域内的所有州 | ordered_state_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state |
| ordered_state_region | 遍历所有州区域 | ordered_state_region = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state_region |
| ordered_state_region_in_<georegion_short_name> | 遍历指定地理区域内的所有州区域 | ordered_state_region_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | state_region |
| ordered_strategic_objective | 遍历该 scope 国家的所有战略目标州 | ordered_strategic_objective = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | state |
| ordered_strategic_region | 遍历全球所有战略区域 | ordered_strategic_region = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | strategic_region |
| ordered_strategic_region_in_<georegion_short_name> | 遍历指定地理区域内的所有战略区域 | ordered_state_region_in_<georegion_short_name> = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | strategic_region |
| ordered_subject_of_subject | 层级中直接附属国之下的任何国家 | ordered_subject_of_subject = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_subject_or_below | 层级中当前国家之下的任何国家 | ordered_subject_or_below = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | country |
| ordered_supporting_character | 遍历支持该 scope 政治运动的所有人物 | ordered_supporting_character = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | political_movement | character |
| ordered_treaty | 遍历所有条约（包括生效条约和草案） | ordered_treaty = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | none | treaty |
| ordered_valid_mass_migration_culture | 列出该 scope 国家中适合大规模迁移的文化 | ordered_valid_mass_migration_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country | culture |
| ordered_war_participant | 遍历一场战争中的所有参战方 | ordered_war_participant = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | war | country |
| random_active_law | 遍历一个国家中所有生效的法律 | random_active_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | law |
| random_active_party | 遍历一个国家中所有活跃的政党 | random_active_party = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | party |
| random_character | 遍历全球所有人物 | random_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | character |
| random_character_in_exile_pool | 遍历流放者池中的人物 | random_character_in_exile_pool = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | character |
| random_character_in_void | 遍历虚空中的人物 | random_character_in_void = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | character |
| random_character_role | 遍历该 scope 人物的所有角色 | random_character_role = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character | character_role |
| random_civil_war | 遍历与该 scope 国家相关的所有内战 | random_civil_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | civil_war |
| random_cobelligerent_in_diplo_play | 遍历该 scope 国家在所有外交博弈（包括战争）中的所有共同交战国 | random_cobelligerent_in_diplo_play = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_cobelligerent_in_war | 遍历该 scope 国家在所有战争中的所有共同交战国 | random_cobelligerent_in_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_combat_unit | 遍历输入 scope 的所有作战单位 | random_combat_unit = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | battle, building, front, hq, military_formation | new_combat_unit |
| random_company | 遍历一个国家中的所有公司 | random_company = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | company |
| random_country | 遍历全球所有国家 | random_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | country |
| random_country_in_<georegion_short_name> | 遍历指定地理区域内的所有国家 | random_country_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | country |
| random_country_strategic_region | 遍历包含该 scope 国家所拥有州的所有战略区域 | random_country_strategic_region = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | strategic_region |
| random_decentralized_country | 遍历所有非中央集权的国家 | random_decentralized_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | country |
| random_diplomatic_catalyst | 遍历一个国家近期记忆中的所有外交催化剂 | random_diplomatic_catalyst = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | diplomatic_catalyst |
| random_diplomatic_play | 遍历全球所有外交博弈 | random_diplomatic_play = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | diplomatic_play |
| random_diplomatically_relevant_country | 遍历一个国家 scope 的所有外交相关国家 | random_diplomatically_relevant_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_direct_subject | 层级中直接位于当前国家之下的任何国家 | random_direct_subject = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_enemy_in_diplo_play | 遍历该 scope 国家在所有外交博弈（包括战争）中的所有敌人 | random_enemy_in_diplo_play = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_enemy_in_war | 遍历该 scope 国家在所有战争中的所有敌人 | random_enemy_in_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成状况 | random_harvest_condition = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state, state_region, strategic_region | harvest_condition |
| random_in_global_list | 遍历全局列表中的所有项目。 | random_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } 对 add_to_(temporary)_list 创建的列表使用 "list" 对 add_to_(global/local)_variable_list 创建的列表使用 "variable" | none |  |
| random_in_hierarchy | 当前层级体系中的任意国家，包括自身 | random_in_hierarchy = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_in_list | 遍历列表中的所有项目。 | random_in_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| random_in_local_list | 遍历本地列表中的所有项目。 | random_in_local_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } (optional) <effects> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list | none |  |
| random_influenced_interest_group | 遍历受某一政治运动影响的所有利益集团 | random_influenced_interest_group = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_movement | interest_group |
| random_interest_group | 遍历一个国家中的所有利益集团 | random_interest_group = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | interest_group |
| random_key_in_global_variable_map | 遍历全局变量映射（map）中的所有键。 | random_key_in_global_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_local_variable_map | 遍历局部变量映射中的所有键。 | random_key_in_local_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_key_in_variable_map | 遍历变量映射中的所有键。 | random_key_in_variable_map = { variable = name of the map limit = { <triggers> } weight = { mtth } (optional) <effects> } | none |  |
| random_law | 遍历一个国家中的所有法律 | random_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | law |
| random_lobby_member | 遍历一个游说集团的所有利益集团成员 | random_lobby_member = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_lobby | interest_group |
| random_market | 遍历全球所有市场 | random_market = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | market |
| random_market_goods | 遍历一个市场中所有处于活跃状态的（市场）商品 | random_market_goods = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | market | market_goods |
| random_member | 遍历一个政党的所有利益集团成员 | random_member = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | party | interest_group |
| random_military_formation | 遍历输入 scope 当前存在的所有军事编队 | random_military_formation = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, hq | military_formation |
| random_neighbouring_state | 遍历与一个州区域相邻的所有州 | random_neighbouring_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state, state_region, strategic_region | state |
| random_overlord_or_above | 层级体系中位于当前国家之上的任意国家 | random_overlord_or_above = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_owned_country | 遍历 scope 公司拥有的所有国家 | random_owned_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | company | country |
| random_participant | scope 中外交协定的两个参与方之一 | random_participant = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_pact | country |
| random_political_lobby | 遍历一个国家或利益集团中的所有政治游说集团 | random_political_lobby = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, interest_group | political_lobby |
| random_political_movement | 遍历一个国家中的所有政治运动 | random_political_movement = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | political_movement |
| random_possible_amendment_type | 遍历可添加到 scope 法律的修正案类型 | random_possible_amendment_type = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | law | amendment_type |
| random_potential_party | 遍历一个国家中所有潜在的政党 | random_potential_party = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | party |
| random_power_bloc | 遍历所有强权集团 | random_power_bloc = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | power_bloc |
| random_power_bloc_member | 遍历 scope 强权集团的所有成员，包括领导者 | random_power_bloc_member = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | power_bloc | country |
| random_preferred_law | 遍历利益集团所在国家中所有已生效及可能的法律，按其对该法律的偏好程度排序 | random_preferred_law = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | interest_group | law |
| random_primary_culture | scope 国家或国家定义的主流文化 | random_primary_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, country_definition | culture |
| random_province | 遍历 scope 州中的所有省份 | random_province = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state | province |
| random_province_in_<georegion_short_name> | 遍历指定地理区域中的所有省份 | random_province_in_<georegion_short_name>' = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | province |
| random_rival_country | 被 scope 国家视为竞争对手的任意国家 | random_rival_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_rivaling_country | 与 scope 国家互为竞争对手的任意国家 | random_rivaling_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_scope_admiral | 遍历以下对象中的所有海军上将：国家、利益集团或军事编队 | random_scope_admiral = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_ally | 遍历一个国家的所有盟友 | random_scope_ally = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_scope_amendment | 遍历 scope 法律的修正案 | random_scope_amendment = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | law | amendment |
| random_scope_army | 遍历输入 scope 当前存在的所有陆军 | random_scope_army = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, hq | military_formation |
| random_scope_article | 遍历 scope 条约的条款 | random_scope_article = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty | treaty_article |
| random_scope_article_option | 遍历 scope 条约或条约选项的条款选项 | random_scope_article_option = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | treaty, treaty_options | treaty_article_options |
| random_scope_building | 遍历以下对象中的所有建筑：州、国家 | random_scope_building = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state | building |
| random_scope_character | 遍历以下对象中的所有人物：国家、利益集团或前线 | random_scope_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_country | 遍历在支持的 scope（当前为：市场、州区域、战略区域）中有存在的所有国家 | random_scope_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | market, state_region, strategic_region | country |
| random_scope_culture | 遍历 scope 中的所有文化 | random_scope_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state | culture |
| random_scope_diplomatic_pact | scope 中国家的任意外交协定 | random_scope_diplomatic_pact = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | diplomatic_pact |
| random_scope_fleet | 遍历输入 scope 当前存在的所有舰队 | random_scope_fleet = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, hq | military_formation |
| random_scope_front | 遍历与 scope 战争相关的所有前线 | random_scope_front = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | war | front |
| random_scope_general | 遍历以下对象中的所有将军：国家、利益集团、前线或军事编队 | random_scope_general = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_held_interest_marker | 遍历一个国家持有的所有利益标记 | random_scope_held_interest_marker = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | interest_marker |
| random_scope_homeland_state | 遍历作为 scope 文化的本土，或 scope 国家任一主流文化本土的所有州 | random_scope_homeland_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, culture | state |
| random_scope_initiator_ally | 遍历以下对象中发起方的所有盟友：外交博弈 | random_scope_initiator_ally = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_play | country |
| random_scope_interest_marker | 遍历以下对象中的所有利益标记：国家、州区域、战略区域 | random_scope_interest_marker = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state_region, strategic_region | interest_marker |
| random_scope_je_involved | 遍历一个日志条目中的所有相关方 | random_scope_je_involved = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | journal_entry | country |
| random_scope_play_involved | 遍历以下对象中的所有相关方：外交博弈 | random_scope_play_involved = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_play | country |
| random_scope_politician | 遍历以下对象中的所有政客：国家或利益集团 | random_scope_politician = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, interest_group, military_formation | character |
| random_scope_pop | 遍历以下对象中的所有人口：国家、州、利益集团、文化 | random_scope_pop = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, culture, interest_group, state | pop |
| random_scope_regional_hqs | 遍历 scope 公司的地区总部 | random_scope_regional_hqs = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | company | building |
| random_scope_ship | 遍历一个国家或军事编队中的所有舰船 | random_scope_ship = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, military_formation | ship |
| random_scope_state | 遍历以下对象中包含省份在内的所有州：国家、州区域、战区、前线或海峡 | random_scope_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, front, state_region, strait, strategic_region, theater | state |
| random_scope_strait | 遍历在 scope 州或国家拥有陆上端点的所有海峡 | random_scope_strait = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country, state | strait |
| random_scope_target_ally | 遍历以下对象中目标的盟友：外交博弈 | random_scope_target_ally = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | diplomatic_play | country |
| random_scope_theater | 遍历一个国家中的所有战区 | random_scope_theater = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | theater |
| random_scope_treaty | 遍历约束 scope 国家的所有生效条约 | random_scope_treaty = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | treaty |
| random_scope_violate_sovereignty_interested_parties | 遍历所有在 scope 国家主权被侵犯时会表示关注的国家 | random_scope_violate_sovereignty_interested_parties = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_scope_violate_sovereignty_wars | 遍历目标国家被 scope 国家侵犯主权时会引发的所有相关战争 | random_scope_violate_sovereignty_wars = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | war |
| random_scope_war | 遍历与 scope 相关的所有战争 | random_scope_war = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | war |
| random_sea_node_adjacent_state | 遍历与一个州共享海域节点的所有州 | random_sea_node_adjacent_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state | state |
| random_state | 遍历全球所有州 | random_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state |
| random_state_in_<georegion_short_name> | 遍历指定地理区域中的所有州 | random_state_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state |
| random_state_region | 遍历所有州区域 | random_state_region = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state_region |
| random_state_region_in_<georegion_short_name> | 遍历指定地理区域中的所有州区域 | random_state_region_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | state_region |
| random_strategic_objective | 遍历 scope 国家的所有战略目标州 | random_strategic_objective = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | state |
| random_strategic_region | 遍历全球所有战略区域 | random_strategic_region = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | strategic_region |
| random_strategic_region_in_<georegion_short_name> | 遍历指定地理区域中的所有战略区域 | random_strategic_region_in_<georegion_short_name> = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | strategic_region |
| random_subject_or_below | 层级体系中位于当前国家之下的任意国家 | random_subject_or_below = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | country |
| random_supporting_character | 遍历支持 scope 政治运动的所有人物 | random_supporting_character = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | political_movement | character |
| random_treaty | 遍历所有条约（包括已生效的和草案） | random_treaty = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | none | treaty |
| random_valid_mass_migration_culture | 列出 scope 国家中适合大规模迁移的文化 | random_valid_mass_migration_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country | culture |
| random_war_participant | 遍历一场战争中的所有参与方 | random_war_participant = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | war | country |
#### 多个随机 scope

通常返回多个随机或半随机的 scope 会很有用。这可以通过几种不同的方式实现。最直接的方式是多次使用 `random_` 迭代器。为了确保同一个 scope 不会被返回两次，可以在每个 scope 的 effect 中设置一个变量，并检查该变量是否未被设置，以此作为返回下一个 scope 的条件。

```
random_country = {
    limit = {
        NOT = { has_variable = blocker_var }
        <other limit triggers>
    }
    set_variable = blocker_var
    <effects>
}
<repeat above as desired>
```

这种写法可以通过使用 [scripted effect](Macro.md) 或 [while](Effect.md) 循环变得更加简洁，这样实际的 effect 只需要定义一次。

另一种方法是使用单个带有半随机排序的 `ordered_` 迭代器。这能确保每个返回的 scope 都是唯一的，无需检查变量，同时还能将所用脚本的数量降到最低。它利用了 [script value](Script value.md) 的 `modulo` 函数来给出半随机的排序。

```
ordered_country = {
    limit = { } # if desired
    order_by = {
        value = gdp
        modulo = { 1 10 }
    }
    max = 10
    <effects>
}
```

这个例子返回 10 个国家，按 GDP 经过随机取模后的结果排序。`modulo` 的范围可以设置为任何想要的值，也可以使用 `fixed_range` 或 `integer_range` 来利用其他 script value，而且可以使用其他数值作为排序依据，例如总人口、威望或任何通常唯一的数值集合。

### 脚本化列表（Scripted lists）

脚本化列表是自定义的可复用迭代器。它们定义在 `/common/scripted_lists` 中。

其格式如下：

```
<list_name> = { # This is used for the custom iterator
    base = # one of the provided lists (country, scope_state, interest_group, etc)
    conditions = {
        <triggers> # The filters for the custom list
    }
}
```

原版游戏中的例子：

```
# Defined in /common/scripted_lists/victoria_scripted_lists.txt
princely_state = {
    base = country
    conditions = {
        is_princely_state = yes
    }
}

# Usage in je_federation_of_india
	complete = {
		custom_tooltip = {
			text = all_princely_states_have_acceded_to_the_federation_tt
			NOT = {
				any_princely_state = {
					exists = THIS
				}
			}
		}
	}
```

### 地理区域

主条目：
地理区域
地理区域通过地理区域的 short_key 提供脚本定义的迭代器。使用地理区域可以以性能更友好的方式遍历任何被包含的区域。

支持的迭代器如下：

- `{any|every|ordered|random}_country_in_<geographic_region_short_key>`
- `{any|every|ordered|random}_province_in_<geographic_region_short_key>`
- `{any|every|ordered|random}_state_in_<geographic_region_short_key>`
- `{any|every|ordered|random}_state_region_in_<geographic_region_short_key>`
- `{any|every|ordered|random}_strategic_region_in_<geographic_region_short_key>`

示例，来自 `je_springtime_of_the_peoples`：

```
 	possible = {
 		any_country_in_europe = {
 			has_technology_researched = egalitarianism
         }
 		custom_tooltip = {
 			text = peoples_springtime_underway_tt
 			has_global_variable = peoples_springtime_happening
 		}
 	}
```

*游戏开发者强烈推荐此方法，因为无界的 _country 和 _state 迭代器本身就开销很高。*

## scope 类型

|  | 请通过补充以下内容来帮助[扩充](https://vic3.paradoxwikis.com/index.php?title=Scope&action=edit)本条目或章节：定义与示例。 |
|---|---|

- battle
- battle_side
- boolean
- building
- building_type
- character
- civil_war
- color
- combat_unit_type
- company
- company_type
- country
- country_definition
- culture
- decree
- diplomatic_catalyst
- diplomatic_catalyst_type
- diplomatic_catalyst
- diplomatic_pact
- diplomatic_play
- diplomatic_play_type
- diplomatic_relations
- flag
- front
- goods
- harvest_condition_area
- harvest_condition_type
- hq
- ideology
- institution
- institution_type
- interest_group
- interest_group_trait
- interest_group_type
- interest_marker
- invasion
- journal_entry
- law
- law_type
- market
- market_goods
- military_formation
- mobilization_option
- new_combat_unit
- none
- party
- political_lobby
- political_lobby_type
- political_movement
- political_movement_type
- pop
- pop_type
- power_bloc
- power_bloc_identity
- power_bloc_principle
- power_bloc_principle_group
- province
- religion
- shipping_lanes
- state
- state_goods
- state_region
- strategic_region
- technology
- theater
- treaty
- treaty_article
- treaty_article
- treaty_article_options
- treaty_options
- value
- war

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • Scopes • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
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

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|