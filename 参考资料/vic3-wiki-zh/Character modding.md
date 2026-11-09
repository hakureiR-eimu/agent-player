---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Character modding
source: https://vic3.paradoxwikis.com/Character_modding
pageid: 6734
categories: [Potentially_outdated, 1.11, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。至少部分内容最后核实于 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.11。

人物
**游戏文件夹 该类型的文件存储所在文件夹。 ：** `common/character_templates`

---

**可注入 该类型是否可以使用 INJECT 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **可替换 该类型是否可以使用 REPLACE 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**相关游戏对象：** 人物特质、人物角色、意识形态

[人物](Character.md) 既可以通过 /common/character_templates/ 中的人物模板定义，也可以通过 `create_character` [effect](Effect.md) 定义。初始人物位于 /common/history/characters/，此外还有许多人物是在事件或其他 effect 中定义的。

人物模板可以配合 `create_character` effect 使用来生成人物；如果定义了 usage 块，它们也可以以半随机的方式出现。

## 人物模板

人物模板定义于 /common/character_templates/，示例如下：

```
usa_rockefeller_character_template = {
    first_name = John
    last_name = Rockefeller
    historical = yes
    dna = dna_john_d_rockefeller
    culture = cu:yankee
    female = no
    religion = rel:protestant
    ideology = ideology_moderate
    interest_group = ig_industrialists
    birth_date = 1839.6.8
    traits = {
        ambitious
        persistent
        basic_entrepreneur
    }
    executive_usage = {
      country_trigger = {
        exists = c:USA
        this = c:USA
      }
      company_trigger = {
        is_company_type = company_type:company_standard_oil
      }
      earliest_usage_date = 1875.1.1
      latest_usage_date = 1915.1.1
      chance = 100
    }
    commander_usage = {
      country_trigger = {
        exists = c:USA
        this = c:USA
      }
      role = general
      earliest_usage_date = 1836.1.1
      latest_usage_date = 1860.1.1
      chance = 75
    }
}
```

| 参数 | 功能 | 示例 | 必需 |
|---|---|---|---|
| template_key | 唯一的模板标识符 | usa_rockefeller_character_template | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| first_name | 人物的名，指向一个 localization 键。设为 culture 则从人物文化中随机取名 | first_name = John | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| last_name | 人物的姓，指向一个 localization 键。设为 culture 则从人物文化中随机取姓 | last_name = Rockefeller | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| historical | 标记该人物为历史人物 | historical = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| dna | 引用一个已定义的人物外观 | dna = dna_string | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| female | 将人物设为女性，默认为男性 | female = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| culture | 设定人物的文化。如果不使用特定文化，可使用 primary_culture 或 ig_before_primary_culture | culture = cu:yankee | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| religion | 设定人物的宗教。默认为人物文化的宗教 | religion = rel:protestant | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| age | 设定人物生成时的年龄 | age = 36 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| birth_date | 设定人物的出生日期，据此计算生成时的年龄。会覆盖 age | birth_date = 1812.1.1 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| interest_group | 设定所属利益集团 | interest_group = ig_devout | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| ideology | 设定人物的意识形态 | ideology = ideology_moderate | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| traits | 设定预定义的特质 | traits = { cautious } | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| trait_generation | 在人物生成时生成特质 | trait_generation = { effects } | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| commander_rank | 生成时设定指挥官的军衔。可使用 default 或脚本定义的军衔 | commander_rank = commander_rank_2 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| ruler | 生成时将人物设为统治者 | ruler = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| heir | 生成时将人物设为继承人 | heir = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| ig_leader | 生成时将人物设为利益集团领袖 | ig_leader = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| is_general | 生成时将人物设为将军 | is_general = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| is_admiral | 生成时将人物设为海军上将 | is_admiral = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| is_agitator | 生成时将人物设为鼓动家 | is_agitator = yes | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| on_created | 人物生成时对其运行 effect | on_created = { effects } | ![No](/images/thumb/0/04/No.png/24px-No.png) |

人物模板可以包含一个或多个 **usage** 块，使模板能够作为随机生成的人物使用，而不必通过 effect 生成人物。一旦模板已被某个 usage 块或 `create_character` 生成过，就不能再通过 usage 块生成。

| 主要参数 | 功能 |  |  |
|---|---|---|---|
| interest_group_leader_usage | 将人物设为潜在的随机生成的利益集团领袖 |  |  |
| agitator_usage | 将人物设为潜在的随机生成的鼓动家 |  |  |
| commander_usage | 将人物设为潜在的随机生成的指挥官 |  |  |
| executive_usage | 将人物设为潜在的随机生成的高管 |  |  |
| 子参数 | 所属主要参数 | 功能 | 必需 |
| country_trigger | 任意主要参数 | 国家（country）scope 下的 trigger，用于判断该 usage 是否有效 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| interest_group_trigger | interest_group_leader_usage agitator_usage | 利益集团（interest group）scope 下的 trigger，用于判断该 usage 是否有效 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| company_trigger | executive_usage | 公司（company）scope 下的 trigger，用于判断该 usage 是否有效 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| role | commander_usage | 决定角色类型，`admiral` 或 `general` | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| earliest_usage_date | 任意主要参数 | 设定该 usage 块生效的最早日期 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| latest_usage_date | 任意主要参数 | 设定该 usage 块生效的最早日期 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| chance | 任意主要参数 | 设定模板在下次有效生成时被使用的几率（0-100） | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |

### 人物姓名

另见：
本地化
**注意：** 所有呈现给玩家的文本*必须*通过 localization 键实现。未本地化的人物姓名默认使用人物文化中的随机姓名。

原版游戏的人物姓名定义于 /Victoria 3/game/localization/<language>/names_l_<language>.yml；新的人物姓名可以定义在任何 localization 文件中。人物姓名可以分配给 [文化](Culture modding.md)，也可以仅用于特定的人物模板。

### 统治者选择器

将人物添加到统治者选择器中可能有些棘手。需要 `is_for_ruler_selector = yes`。此外，如果你希望人物出现在选择器中，似乎还必须通过 `interest_group_leader_usage` 块将其设为利益集团领袖。

## 人物角色

待补充

## 创建人物 effect

[effect](Effect.md) `create_character` 可以使用已定义的人物模板，可以使用与人物模板相同的参数直接定义人物，也可以先使用模板再通过附加参数进行修改。

## 人物历史

初始人物位于 /common/history/characters/。它们可以通过模板创建，也可以在 `create_character` 中直接定义。

## 人物特质

人物特质
**游戏文件夹 该类型的文件存储所在文件夹。 ：** `common/character_traits`

---

**图标文件夹 该类型原版图标通常存放的文件夹。 ：** `gfx/interface/icons/character_trait_icons`

---

**可注入 该类型是否可以使用 INJECT 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **可替换 该类型是否可以使用 REPLACE 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**相关游戏对象：** 人物

人物特质定义于 /common/character_traits/

如果要添加 mod 的特质而非修改原版特质，请新建一个文件。

```
notorious = {
  type = condition                            # Can be one of personality, skill, or condition. Each category is limited by defines. Random traits can be applied based on a particular type.
  texture = "gfx/interface/icons/character_trait_icons/direct.dds"  # The trait's texture asset

  character_modifier = {                      # Applies to the Character regardless of role
    character_popularity_add = 25
  }

  command_modifier = {                        # Applies to the Character, their Military Formation, and any Combat Units under the Character's command, assuming the unit is fully Mobilized (or does not need to Mobilize)
    unit_kill_rate_mult = 0.1
  }
  
  country_modifier = {                        # Applies to the Character's Country if they are the Ruler of it
    state_turmoil_mult = 0.1
  }
  
  agitator_modifier = {
    political_movement_radicalism_add = 0.15  # Applies to the Character's Political Movement
  }
    
  interest_group_modifier = {                 # Applies to the Character's Interest Group if they are the Leader of it
    interest_group_pol_str_mult = -0.05
    interest_group_pop_attraction_mult = 0.1
  }

  executive_modifier = {                      # Applies to the Character's Company if they are the Executive of it
    building_cash_reserves_mult = -0.1
  }

  possible = {                                # Used to determine if this trait is a valid random choice
    popularity < 0                            # Does NOT impact the validity of the trait once it's acquired
  }

  weight = {                                  # Script value to determine how likely it is the character will randomly get this trait, compared to other traits in its category. Default 1
    value = popularity
    multiply = -1
  }

  replace = {                                 # When the character gains this trait, any traits they have in the following list are removed
    famous
    wicked
  }

  value = 2                                   # How much this trait is "worth" in experience levels traits. Default 1
                                              # Used to determine whether the character is owed more traits, and which trait category is overrepresented
}
```

### 特质本地化

另见：
本地化
特质会生成两个 localization 键：`<trait_name>` 和 `<trait_name>_desc`，分别用于名称和风味描述。

## 人物脚本文档

以下 [effect](Effect.md)、[event target](Event target.md) 和 [trigger](Trigger.md) 可用于人物（character）scope。

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_career_length | 增加人物当前某一角色的任职时长。角色可以是特定的数据库角色或角色类型（例如 general）。如果未指定角色，则应用于所有有任职结束日期的角色 | add_career_length = { role = role_key/role_type days/months/years = 5 random_range = { 0.8 1.2 } } |  |
| add_character_role | 为人物添加新角色，可用于原型角色或数据库角色 | add_character_role = general/character_role_general |  |
| add_commander_rank | 将人物晋升/降级若干军衔 | add_commander_rank = integer |  |
| add_experience | 为指挥官增加一定量的经验 | add_experience = 0.2 |  |
| add_modifier | 为 scope 中的对象添加限时 modifier 效果 | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_random_trait | 从指定类别中随机添加一个符合条件的特质 | add_random_trait = personality / skill / condition |  |
| add_trait | 为人物添加一个特质 | add_trait = trait |  |
| change_character_culture | 改变 scope 人物的文化 | change_character_culture = cu:colombian | culture |
| change_character_religion | 改变 scope 人物的宗教 | change_character_religion = rel:protestant | religion |
| disinherit_character | 剥夺 scope 人物在所有适用国家的继承人身份 | scope:larry = { disinherit_character = yes } |  |
| every_character_role | 遍历 scope 人物的所有角色 | every_character_role = { limit = { <triggers> } #optional <effects> } | character_role |
| exile_character | 将人物流放到流亡池 | exile_character = yes |  |
| free_character_from_void | 将人物从虚空中释放，如果设为 no 则人物会被删除 | free_character_from_void = yes |  |
| kill_character | 杀死一个人物 | kill_character = bool (yes - kill [by default], no - don't do anything) kill_character = { hidden = bool (yes - without notification; no - show notification [by default]) value = bool (yes - kill [by default], no - don't do anything) } |  |
| ordered_character_role | 遍历 scope 人物的所有角色 | ordered_character_role = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | character_role |
| place_character_in_void | 将人物放逐到虚空，duration 为人物被删除前保留的时长 | place_character_in_void = months |  |
| random_character_role | 遍历 scope 人物的所有角色 | random_character_role = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | character_role |
| remove_as_interest_group_leader | 将人物从利益集团领袖职位上移除 | remove_as_interest_group_leader = yes |  |
| remove_character_role | 移除人物的现有角色，可用于原型角色或数据库角色 | remove_character_role = general/character_role_general |  |
| remove_modifier | 移除 scope 对象上的限时 modifier 效果 | remove_modifier = static_modifier_name |  |
| remove_trait | 从人物身上移除一个特质 | remove_trait = trait |  |
| replace_character_roles | 用其他角色替换人物的现有角色，可用于原型角色或数据库角色 | replace_character_role = { add = { roles } remove = { roles } remove_all = no/yes } |  |
| set_as_adult | 如果 scope 人物尚未成年，则将其变为成年人 | set_as_adult = yes |  |
| set_as_interest_group_leader | 将人物设为利益集团领袖 | set_as_interest_group_leader = yes |  |
| set_career_length | 从当前时间起设定人物某一角色的任职时长。角色可以是特定的数据库角色或角色类型（例如 general）。如果未指定角色，则应用于所有有任职结束日期的角色 | set_career_length = { role = role_key/role_type days/months/years = 10 random_range = { 0.8 1.2 } } |  |
| set_character_as_ruler | 将 scope 人物设为其国家的统治者。 | scope:larry = { set_character_as_ruler = yes } CAUTION: Do not use this effect with chartered companies, as the character's country will be affected |  |
| set_character_busy_and_immortal | 将人物标记为忙碌且不朽，或清除该标记 | set_character_busy = bool |  |
| set_character_immortal | 设定 scope 人物是否不朽。 | scope:larry = { set_character_immortal = yes/no } |  |
| set_commander_rank | 将人物晋升/降级到指定的军衔数值 | set_commander_rank = 3 |  |
| set_first_name | 将人物的名更改为某个 loc 键 | set_first_name = loc_key |  |
| set_home_country | 设定人物的本国。这会使他们开始认为自己曾被流放，即对他们的 was_exiled 开始判定为 yes | set_home_country = c:FRA | country |
| set_home_country_definition | 直接以 tag 设定人物的本国，可用于避免确认该 tag 是否存在，这会使他们成为流亡者 | set_home_country_definition = cd:FRA | country_definition |
| set_home_state | 更改 scope 人物的故乡州 | set_home_state = <state scope> | state |
| set_ideology | 更改 scope 人物的意识形态 | set_ideology = ideology:<ideology key> | ideology |
| set_interest_group | 设定人物所属的利益集团 | set_interest_group = ruler.interest_group | interest_group |
| set_is_noble | 设定 scope 人物的贵族标记。 | set_is_noble = yes/no |  |
| set_last_name | 将人物的姓更改为某个 loc 键 | set_last_name = loc_key |  |
| transfer_character | 将当前 scope 人物转移到目标国家 | transfer_character = country | country |
| transfer_to_formation | 将 scope 人物转移到目标编队 | transfer_to_formation = scope:formation | military_formation |
| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| age | 比较人物年龄 | age > 20 | value |
| any_character_role | 遍历 scope 人物的所有角色 | any_character_role = { filter = { <triggers> }（可选）<count=num/all> / <percent=fixed_point>（可选）<triggers> } | character_role |
| any_scope_homeland_state | 遍历所有作为 scope 文化的故乡的州，或 scope 国家任一主流文化的故乡的州 | any_scope_homeland_state = { filter = { <triggers> }（可选）<count=num/all> / <percent=fixed_point>（可选）<triggers> } | state |
| can_agitate | 检查 scope 人物能否在目标国家进行鼓动 | can_agitate = <scope/c:TAG> | country |
| character_acceptance | 将 scope 人物在目标国家的接纳度与一个接纳度数值进行比较 | character_acceptance = { target = c:FRA value > 50 } | value |
| character_supports_political_movement | 检查 scope 人物是否支持某个政治运动 | character_supports_political_movement = yes/no | boolean |
| commander_is_available | 检查指挥官是否空闲 | commander_is_available = bool | boolean |
| commander_rank | 比较指挥官军衔 | commander_rank > 2 | value |
| could_support_political_movement | 检查人物是否有可能支持某个政治运动 | could_support_political_movement = <scope> |  |
| experience_level | 比较人物经验等级 | experience_level > 1 | value |
| has_commander_order | 检查 scope 人物是否正在执行给定的命令 | has_commander_order = order type key/order type scope |  |
| has_culture | 检查人物文化 | has_culture = culture scope or character scope |  |
| has_ideology | 检查 scope 人物或利益集团是否具有该意识形态 |  |  |
| has_military_formation | 检查人物是否拥有军事编队 | has_military_formation = bool | boolean |
| has_modifier | 检查受支持的 scope 是否具有某个限时 modifier | has_modifier = <key> |  |
| has_religion | 检查人物宗教 | has_religion = religion/character scope |  |
| has_role | 检查人物是否具有特定角色 | has_role = role |  |
| has_role_of_type | 检查人物是否具有指定原型的角色 | has_role_of_type = archetype |  |
| has_template | 检查人物是否由指定模板生成 | has_template = template_key |  |
| has_trait | 检查人物是否具有特定特质 | has_trait = trait |  |
| is_adult | 检查人物是否为成年人 | is_adult = bool | boolean |
| is_advancing_on_front | 检查指挥官是否正在某条前线推进 | is_advancing_on_front = <front scope> | front |
| is_attacker_in_battle | 检查指挥官或舰船是否为某场战斗中的进攻方 | is_attacker_in_battle = bool | boolean |
| is_busy | 检查人物是否忙碌 | is_busy = bool | boolean |
| is_character_alive | 检查 scope 人物是否存活 | is_character_alive = bool | boolean |
| is_defender_in_battle | 检查指挥官或舰船是否为某场战斗中的防守方 | is_defender_in_battle = bool | boolean |
| is_female | 检查人物是否为女性 | is_female = bool | boolean |
| is_heir_of_own_country | 检查 scope 人物是否为其所在国家的继承人 | is_heir_of_own_country = yes / no | boolean |
| is_historical | 检查人物是否为历史人物 | is_historical = yes/no | boolean |
| is_immortal | 检查 scope 人物是否不朽 | scope:abbath = { is_immortal = yes } | boolean |
| is_in_battle | 检查指挥官或舰船是否正在交战 | is_in_battle = bool | boolean |
| is_in_exile_pool | 检查 scope 人物是否处于流亡者池中 | is_in_exile_pool = yes/no | boolean |
| is_in_void | 检查人物是否处于虚空（void）中 | is_in_void = bool | boolean |
| is_interest_group_leader | 检查人物是否为其利益集团的领袖 | is_interest_group_leader = yes/no | boolean |
| is_interest_group_type | 检查利益集团是否属于某一类型，也可直接用于人物 | is_interest_group_type = x |  |
| is_monarch | 检查人物是否为实行世袭继承制的国家的君主 | is_monarch = bool | boolean |
| is_noble | 检查人物是否为贵族 | is_noble = bool | boolean |
| is_on_front | 检查人物或军事编队是否已被分配到某条前线并已抵达 | is_on_front = yes/no | boolean |
| is_ruler_of_any_country | 检查人物是否为任意国家的统治者/国家元首 | is_ruler_of_any_country = bool | boolean |
| is_ruler_of_other_country | 检查人物是否为其所居住国家以外的任意国家的统治者/国家元首 | is_ruler_of_other_country = bool | boolean |
| is_ruler_of_own_country | 检查人物是否为其所居住国家的统治者/国家元首 | is_ruler_of_own_country = bool | boolean |
| law_enactment_stance | 比较 scope 人物、运动或利益集团对制定指定法律相对于同组现行生效法律的立场 |  |  |
| law_stance | 比较 scope 人物、运动或利益集团对指定法律的基本立场，忽略同组现行生效的法律 |  |  |
| lifetime_piracy_income | 比较人物的终身海盗收入 | lifetime_piracy_income >= 1000000 | value |
| loyalty | 比较人物忠诚度 | loyalty > 1 | value |
| primary_role | 检查人物的主要角色是否为指定角色 | primary_role = role |  |
| prominence | 比较人物声望 | prominence > 1 | value |
| remaining_career_length | 检查人物的剩余职业生涯长度是否达到一个时长阈值。角色（role）可以是特定的数据库角色、角色类型，或省略以使用离职业生涯结束最远的角色 | remaining_career_length = { role = general years = 5 } | value |
| role_priority | 比较人物角色的优先级 | role_priority >= 10 | value |
| trait_value | 比较人物的特质总数值 | trait_value < experience_level | value |
| was_exiled | 检查 scope 人物是否曾被流放 | was_exiled = yes/no | boolean |
| years_of_service | 比较指挥官的服役年数 | years_of_service > 1 | value |

| Event target | 描述 | 目标 scope |
|---|---|---|
| average_progressiveness | 获取 scope 人物或利益集团的平均进步度 | value |
| command_limit_num_units | 根据指挥官的统率上限，获取其军事编队中通常可获得的基准单位数量 | value |
| commander_military_formation | 进入人物的军事编队 scope | military_formation |
| culture | 进入人口或人物的文化 scope | culture |
| front | 从多种 scope 进入前线 scope：从战斗进入其发生的前线；从人物进入其所在或正在前往的前线；从军事编队进入其当前所在的前线；从省份进入包含该省的前线；从入侵进入入侵前线 | front |
| home_country | 进入流亡者的祖国 scope | country |
| ideology | 双重用途：从意识形态名称进入其 scope（ideology:ideology_anarchist）；进入 scope 人物的意识形态 scope | ideology |
| interest_group | 进入该人物的利益集团 scope！ | interest_group |
| interest_group_type | 进入 scope 人物所属利益集团的类型 scope | interest_group_type |
| modifier | 进入当前对象拥有的指定键的 modifier 类型数值 scope，示例：modifier:country_influence_add | boolean, value |
| num_active_ships | 获取国家、指挥官或军事编队的活跃舰船数量；或获取省份内与指定国家结盟的军事编队的活跃舰船数量 | value |
| num_active_ships_in_battle | 获取国家、指挥官或军事编队的交战中活跃舰船数量；或获取省份内与指定国家结盟的军事编队的交战中活跃舰船数量 | value |
| num_active_ships_not_in_battle | 获取国家、指挥官或军事编队的未交战活跃舰船数量；或获取省份内与指定国家结盟的军事编队的未交战活跃舰船数量 | value |
| num_battalions | 返回指挥官麾下活跃营的数量 | value |
| num_mobilized_battalions | 返回将军麾下已完全动员单位数量 | value |
| num_non_destroyed_ships | 获取国家、指挥官或军事编队的未被摧毁舰船数量；或获取省份内与指定国家结盟的军事编队的未被摧毁舰船数量 | value |
| num_non_destroyed_ships_in_battle | 获取国家、指挥官或军事编队的交战中未被摧毁舰船数量；或获取省份内与指定国家结盟的军事编队的交战中未被摧毁舰船数量 | value |
| num_non_destroyed_ships_not_in_battle | 获取国家、指挥官或军事编队的未交战且未被摧毁舰船数量；或获取省份内与指定国家结盟的军事编队的未交战且未被摧毁舰船数量 | value |
| num_ships | 获取国家、指挥官或军事编队的舰船数量；或获取省份内与指定国家结盟的军事编队的舰船数量 | value |
| num_ships_in_battle | 获取国家、指挥官或军事编队的交战中舰船数量；或获取省份内与指定国家结盟的军事编队的交战中舰船数量 | value |
| num_ships_not_in_battle | 获取国家、指挥官或军事编队的未交战舰船数量；或获取省份内与指定国家结盟的军事编队的未交战舰船数量 | value |
| num_units | 获取指挥官或军事编队的活跃单位数量；获取省份内与指定国家结盟的军事编队的活跃单位数量 | value |
| num_units_in_battle | 获取指挥官或军事编队的交战中活跃单位数量；获取省份内与指定国家结盟的军事编队的交战中活跃单位数量 | value |
| num_units_not_in_battle | 获取指挥官或军事编队的未交战活跃单位数量；获取省份内与指定国家结盟的军事编队的未交战活跃单位数量 | value |
| num_units_share | 考虑指挥官统率上限后其所占单位份额。示例：若该人物拥有 30 统率上限，舰队总统率上限为 60，编队共有 50 支船队，则该人物在其战斗中应获得 25 支船队 | value |
| opposing_commander | 从战斗中的人物进入战斗另一方的人物 scope | character |
| owner | 进入对象所属国家的 scope | country |
| political_movement | 若在人物 scope 中使用，进入该人物所支持的政治运动 scope；若在革命内战 scope 中使用，进入发动革命的运动 scope；若在利益集团 scope 中使用，进入该集团的主导运动 scope | political_movement |
| popularity | 获取 scope 人物的名望，通常介于 -100 到 +100 之间 | value |
| religion | 进入国家或国家定义的主流宗教，或人口宗教的 scope | religion |

### 人物 modifier 类型

`character_` [modifier 类型](Modifier types.md) 将其效果作用于人物。

| Modifier 类型 | 本地化名称 | 类型 | 格式 | 备注 |
|---|---|---|---|---|
| character_advancement_speed_add | 将军晋升速度 | additive | good |  |
| character_advancement_speed_mult | 将军晋升速度 | multiplicative | percent, good |  |
| character_battle_condition_aggressive_maneuver_mult | 激进机动几率 | multiplicative | percent, neutral |  |
| character_battle_condition_blunder_mult | 失误几率 | multiplicative | percent, bad |  |
| character_battle_condition_broken_supply_line_mult | 补给线被切断几率 | multiplicative | percent, bad |  |
| character_battle_condition_camouflaged_mult | 伪装几率 | multiplicative | percent, good |  |
| character_battle_condition_careful_maneuver_mult | 谨慎机动几率 | multiplicative | percent, good |  |
| character_battle_condition_charted_terrain_mult | 勘察地形几率 | multiplicative | percent, good |  |
| character_battle_condition_death_from_below_mult | 水下突袭几率 | multiplicative | percent, good |  |
| character_battle_condition_dug_in_mult | 坚守阵地几率 | multiplicative | percent, good |  |
| character_battle_condition_exhausted_mult | 疲惫几率 | multiplicative | percent, bad |  |
| character_battle_condition_good_visibility_mult | 良好能见度几率 | multiplicative | percent, good |  |
| character_battle_condition_guerilla_ambush_mult | 伏击几率 | multiplicative | percent, good |  |
| character_battle_condition_logistics_secured_mult | 后勤有保障几率 | multiplicative | percent, good |  |
| character_battle_condition_lost_mult | 迷路几率 | multiplicative | percent, bad |  |
| character_battle_condition_mud_mult | 泥泞几率 | multiplicative | percent, bad |  |
| character_battle_condition_poor_visibility_mult | 能见度不良几率 | multiplicative | percent, bad |  |
| character_battle_condition_ramming_maneuver_mult | 撞击机动几率 | multiplicative | percent, neutral |  |
| character_battle_condition_rapid_advance_mult | 快速推进几率 | multiplicative | percent, good |  |
| character_battle_condition_rough_waters_mult | 波涛汹涌几率 | multiplicative | percent, neutral |  |
| character_battle_condition_strong_winds_mult | 强风几率 | multiplicative | percent, neutral |  |
| character_battle_condition_surprise_maneuver_mult | 突袭机动几率 | multiplicative | percent, good |  |
| character_blockade_mult | 海军上将封锁强度 | multiplicative | percent, good |  |
| character_command_limit_add | 统率上限 | additive | good |  |
| character_command_limit_mult | 统率上限 | multiplicative | percent, good |  |
| character_commander_loyalty_add | 指挥官忠诚度 | additive | good |  |
| character_convoy_protection_mult | 海军上将商船护航 | multiplicative | percent, good |  |
| character_convoy_raiding_mult | 海军上将商船袭击效率 | multiplicative | percent, good |  |
| character_coup_strength_add | 政变强度 | additive | neutral |  |
| character_coup_strength_mult | 政变强度 | multiplicative | percent, neutral |  |
| character_expedition_events_explorer_mult | 探险机遇 | multiplicative | percent, good |  |
| character_health_add | 人物健康 | additive | percent, good |  |
| character_interception_add | 海军上拦截几率 | additive | good |  |
| character_loyalty_add | 忠诚度 | additive | good |  |
| character_loyalty_mult | 忠诚度 | multiplicative | percent, good |  |
| character_max_offensive_battles_add | 最大进攻战斗数 | additive | good |  |
| character_naval_mission_area_add | 海军任务区域规模 | additive | good |  |
| character_piracy_goods_capacity_mult | 劫掠容量 | multiplicative | percent, good |  |
| character_popularity_add | 名望 | additive | good |  |
| character_prominence_add | 声望 | additive | neutral |  |
| character_raid_supply_add | 海军上将袭击补给几率 | additive | good |  |

### 人物 GUI 脚本

主条目：
GUI 脚本
| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessBattle |  | Battle | 类别：const |
| AccessCulture |  | Culture | 类别：const |
| AccessInterestGroup |  | InterestGroup | 类别：const |
| AccessOrders |  | Unknown | 类别：const |
| AccessPossibleSpecialOrders |  | Unknown | 类别：const |
| AccessReligion |  | Religion | 类别：const |
| AccessSelf |  | Character | 类别：const |
| AccessTraits |  | Unknown | 类别：const |
| AccessUnavailableOrders |  | Unknown | 类别：const |
| GetAcceptanceStatus |  | AcceptanceStatus | 类别：nonconst |
| GetAcceptanceStatusIn | Country | AcceptanceStatus | 类别：nonconst |
| GetAcceptanceValue |  | int32 | 类别：nonconst |
| GetAcceptanceValueDesc |  | CString | 类别：nonconst |
| GetAcceptanceValueDescIn | Country | CString | 类别：nonconst |
| GetAcceptanceValueIn | Country | int32 | 类别：nonconst |
| GetAge |  | int32 | 类别：nonconst |
| GetAgitatorSpawnedNotificationText |  | CString | 类别：nonconst |
| GetAllRoleNames |  | CString | 类别：nonconst |
| GetAnimatedPortrait | PortraitEnvironment PortraitCamera PortraitAnimation CVector2f | Unknown | 类别：nonconst |
| GetAssignedState |  | State | 类别：nonconst |
| GetBattle |  | Battle | 类别：nonconst |
| GetBirthday |  | CString | 类别：nonconst |
| GetCombatUnitsTypeIcon |  | CString | 类别：nonconst |
| GetCommandLimit |  | CString | 类别：nonconst |
| GetCommandLimitDesc |  | CString | 类别：nonconst |
| GetCommandLimitRaw |  | int32 | 类别：nonconst |
| GetCommanderDetails |  | CString | 类别：nonconst |
| GetCommanderRank |  | CommanderRank | 类别：nonconst |
| GetCountry |  | Country | 类别：nonconst |
| GetCulture |  | Culture | 类别：nonconst |
| GetCustom | CustomLocalization | CString | 类别：nonconst |
| GetDebugDesc |  | CString | 类别：nonconst |
| GetFirstName |  | CString | 类别：nonconst |
| GetFirstNameNoFormatting |  | CString | 类别：nonconst |
| GetFirstNamePossessive |  | CString | 类别：nonconst |
| GetFront |  | Front | 类别：nonconst |
| GetFullName |  | CString | 类别：nonconst |
| GetFullNameNoFormatting |  | CString | 类别：nonconst |
| GetFullNamePossessive |  | CString | 类别：nonconst |
| GetFullNameWithTitle |  | CString | 类别：nonconst |
| GetFullNameWithTitleNoFormatting |  | CString | 类别：nonconst |
| GetFullNameWithTitlePossessive |  | CString | 类别：nonconst |
| GetGender |  | CString | 类别：nonconst |
| GetGenderOpposite |  | CString | 类别：nonconst |
| GetHerHim |  | CString | 类别：nonconst |
| GetHerHimOpposite |  | CString | 类别：nonconst |
| GetHerHis |  | CString | 类别：nonconst |
| GetHerHisOpposite |  | CString | 类别：nonconst |
| GetHerselfHimself |  | CString | 类别：nonconst |
| GetHerselfHimselfOpposite |  | CString | 类别：nonconst |
| GetHistoricalUrl |  | CString | 类别：nonconst |
| GetHomeCountry |  | Country | 类别：nonconst |
| GetHomeCountryDefinition |  | CountryDefinition | 类别：nonconst |
| GetID |  | int32 | 类别：nonconst |
| GetIDString |  | CString | 类别：nonconst |
| GetIdeology |  | Ideology | 类别：nonconst |
| GetInfoTooltip |  | CString | 类别：nonconst |
| GetInteraction | Unknown | CharacterInteraction | 类别：nonconst |
| GetInteractions |  | Unknown | 类别：nonconst |
| GetInterestGroup |  | InterestGroup | 类别：nonconst |
| GetInvasion |  | Invasion | 类别：nonconst |
| GetLastName |  | CString | 类别：nonconst |
| GetLastNameNoFormatting |  | CString | 类别：nonconst |
| GetLastNamePossessive |  | CString | 类别：nonconst |
| GetMilitaryFormation |  | MilitaryFormation | 类别：nonconst |
| GetNextCommanderRank |  | CommanderRank | 类别：nonconst |
| GetNextCommanderRankBenefits |  | CString | 类别：nonconst |
| GetNextOrderType |  | CommanderOrderType | 类别：nonconst |
| GetNumUnitsThatWouldBeSplitOff |  | int32 | 类别：nonconst |
| GetOrderType |  | CommanderOrderType | 类别：nonconst |
| GetPoliticalMovement |  | PoliticalMovement | 类别：nonconst |
| GetPopularity |  | CFixedPoint | 类别：nonconst |
| GetPopularityDesc |  | CString | 类别：nonconst |
| GetPortrait | PortraitEnvironment PortraitCamera PortraitAnimation CVector2f | Unknown | 类别：nonconst |
| GetPrimaryRoleName |  | CString | 类别：nonconst |
| GetPrimaryRoleTitle |  | CString | 类别：nonconst |
| GetPromoteCommand |  | Command | 类别：nonconst |
| GetRankName |  | CString | 类别：nonconst |
| GetRankNameFor | CommanderRank | CString | 类别：nonconst |
| GetRankTitle |  | CString | 类别：nonconst |
| GetRankTitleFor | CommanderRank | CString | 类别：nonconst |
| GetRecruitCommand | MilitaryFormation | Command | 类别：nonconst |
| GetReligion |  | Religion | 类别：nonconst |
| GetRepairingTexture |  | Unknown | 类别：nonconst |
| GetSheHe |  | CString | 类别：nonconst |
| GetSheHeOpposite |  | CString | 类别：nonconst |
| GetStrengthPointsIcon |  | CString | 类别：nonconst |
| GetTimedModifiers |  | Unknown | 类别：nonconst |
| GetTooltipTag |  | CString | 类别：nonconst |
| GetTraitsDesc |  | CString | 类别：nonconst |
| GetWomanMan |  | CString | 类别：nonconst |
| GetWomanManOpposite |  | CString | 类别：nonconst |
| HasAdvancingOrder |  | bool |  |
| HasInvasionPlan |  | bool |  |
| HasMilitaryFormation |  | bool |  |
| HasOrder | Unknown | bool |  |
| HasUnavailableAdvanceOrders |  | bool |  |
| HasUnavailableDefendOrders |  | bool |  |
| IsAdmiral |  | bool |  |
| IsAgitator |  | bool |  |
| IsAtFront |  | bool |  |
| IsAttackingInBattle |  | bool |  |
| IsBeingHighlighted |  | bool |  |
| IsBeingTutorialHighlighted |  | bool |  |
| IsBusy |  | bool |  |
| IsCommander |  | bool |  |
| IsDefeated |  | bool |  |
| IsDefendingInBattle |  | bool |  |
| IsExecutive |  | bool |  |
| IsFemale |  | bool |  |
| IsGeneral |  | bool |  |
| IsHeir |  | bool |  |
| IsHistorical |  | bool |  |
| IsIGLeader |  | bool |  |
| IsInBattle |  | bool |  |
| IsInExilePool |  | bool |  |
| IsMaxRank |  | bool |  |
| IsOffer |  | bool |  |
| IsPinnedInOutliner |  | bool |  |
| IsPolitician |  | bool |  |
| IsRetired |  | bool |  |
| IsRuler |  | bool |  |
| IsValid |  | bool |  |
| IsZoomingToOrderTarget |  | bool |  |
| MakeScope |  | Scope |  |
| OpenHistoricalUrl |  | void |  |
| PredictMovementToJoin | Unknown | PoliticalMovement |  |
| PredictMovementTypeToStart | Unknown | PoliticalMovementType |  |
| RecruitCharacter | Unknown | void |  |
| SelectOrder | CommanderOrderType | Command |  |
| Self |  | Character |  |
| SplitIntoOwnFormation |  | Command |  |
| TogglePinInOutliner |  | void |  |
| WillJoinMovementIfInvited | Country | bool |  |
| WillStartMovementIfInvited | Country | bool |  |
| ZoomToLocation |  | void |  |
| ZoomToOrderTarget |  | void |  |
| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessSelf |  | CharacterInteraction | 类别：常量（const） |
| ExecuteCommand | Character | void |  |
| GetClickSound |  | Unknown | 类别：非常量（nonconst） |
| GetCommandDesc | Character | CString | 类别：非常量（nonconst） |
| GetCooldownDesc | Character | CString | 类别：非常量（nonconst） |
| GetCooldownDuration | Character | CString | 类别：非常量（nonconst） |
| GetCooldownRemaining | Character | CString | 类别：非常量（nonconst） |
| GetDesc |  | CString | 类别：非常量（nonconst） |
| GetEffects | Character | CString | 类别：非常量（nonconst） |
| GetIcon |  | Unknown | 类别：非常量（nonconst） |
| GetInfo |  | CString | 类别：非常量（nonconst） |
| GetName |  | CString | 类别：非常量（nonconst） |
| GetRequirements | Character | CString | 类别：非常量（nonconst） |
| GetTooltipTag |  | CString | 类别：非常量（nonconst） |
| HasCooldown | Unknown | bool |  |
| HasIcon |  | bool |  |
| IsCommandValid | Character | bool |  |
| IsOnCooldown | Character | bool |  |
| Self |  | CharacterInteraction |  |
| ShouldShowRequirements |  | bool |  |

| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessSelf |  | CharacterTrait | 类别：常量（const） |
| AccessUnlockedOrders |  | Unknown | 类别：常量（const） |
| GetDesc |  | CString | 类别：非常量（nonconst） |
| GetModifiers |  | CString | 类别：非常量（nonconst） |
| GetName |  | CString | 类别：非常量（nonconst） |
| GetNameNoFormatting |  | CString | 类别：非常量（nonconst） |
| GetTexture |  | Unknown | 类别：非常量（nonconst） |
| GetTooltipTag |  | CString | 类别：非常量（nonconst） |
| Self |  | CharacterTrait |  |

| Promote | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessBattle |  | Battle | 类别：常量（const） |
| AccessCountry |  | Country | 类别：常量（const） |
| AccessCulture |  | Culture | 类别：常量（const） |
| AccessInterestGroup |  | InterestGroup | 类别：常量（const） |
| AccessReligion |  | Religion | 类别：常量（const） |
| GetAcceptanceStatus |  | AcceptanceStatus | 类别：非常量（nonconst） |
| GetAcceptanceStatusIn | Country | AcceptanceStatus | 类别：非常量（nonconst） |
| GetAssignedState |  | State | 类别：非常量（nonconst） |
| GetBattle |  | Battle | 类别：非常量（nonconst） |
| GetCommanderRank |  | CommanderRank | 类别：非常量（nonconst） |
| GetCountry |  | Country | 类别：非常量（nonconst） |
| GetCulture |  | Culture | 类别：非常量（nonconst） |
| GetFront |  | Front | 类别：非常量（nonconst） |
| GetHomeCountry |  | Country | 类别：非常量（nonconst） |
| GetHomeCountryDefinition |  | CountryDefinition | 类别：非常量（nonconst） |
| GetIdeology |  | Ideology | 类别：非常量（nonconst） |
| GetInteraction | CharacterInteraction | CharacterInteraction | 类别：非常量（nonconst） |
| GetInterestGroup |  | InterestGroup | 类别：非常量（nonconst） |
| GetInvasion |  | Invasion | 类别：非常量（nonconst） |
| GetMilitaryFormation |  | MilitaryFormation | 类别：非常量（nonconst） |
| GetNextCommanderRank |  | CommanderRank | 类别：非常量（nonconst） |
| GetNextOrderType |  | CommanderOrderType | 类别：非常量（nonconst） |
| GetOrderType |  | CommanderOrderType | 类别：非常量（nonconst） |
| GetPoliticalMovement |  | PoliticalMovement | 类别：非常量（nonconst） |
| GetReligion |  | Religion | 类别：非常量（nonconst） |
| MakeScope |  | Scope |  |
| PredictMovementToJoin | Country | PoliticalMovement |  |
| PredictMovementTypeToStart | Country | PoliticalMovementType |  |

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [效果（Effects）](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [宏（Macros）](Macro.md) • [修改器类型](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [脚本值（Script value）](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [决议](Decision modding.md) • [事件](Event modding.md) • [历史](History modding.md) • [日志](Journal modding.md) • [修改器](Modifier modding.md) • 目标 • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [建筑](Building modding.md) • 人物 • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图片](Event images.md) • [图形资产](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [声音](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [Mod](Mod.md) • [Mod 兼容性](Mod compatibility.md) • [Mod 结构](Mod structure.md) • [脚本测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [Mod 翻译](Mod translation.md) • [新国家 Mod 制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州 Mod 制作指南](State modding guide.md) |
|---|---|