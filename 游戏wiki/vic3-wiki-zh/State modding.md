---
translated: 2026-10-27
translator: machine (glm-5.3)
title: State modding
source: https://vic3.paradoxwikis.com/State_modding
pageid: 5744
categories: [Potentially_outdated, 1.9, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的部分。至少有一部分最后是在 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.9 下核实的。

[州](https://vic3.paradoxwikis.com/States)，或更准确地说州区域（state region），是游戏地图上被划分出的部分，包含人口和建筑，是地图上交互的主要层级。州区域定义于 map_data/state_regions。

## 州区域示例

州区域被定义为一个“省份”列表，外加若干特征。

```
STATE_SVEALAND = {
    id = 1
    subsistence_building = "building_subsistence_pastures"
    provinces = { "x0974E5" "x216569" "x24A2F1" "x298E7B" "x317138" "x36F523" "x3844C0" "x3E2C22" "x404643" "x41C729" "x432E07" "x45B6EF" "x4628A5" "x4836F2" "x4B02EB" "x4C9918" "x4FA424" "x604060" "x62D0D4" "x656512" "x6CF949" "x6E95C2" "x6F40EC" "x823263" "x8AC21D" "x90845E" "x93C3BC" "x93C76C" "x9686A5" "x9BBBE3" "xA001A0" "xA08021" "xA6C31B" "xA82FF7" "xA86C50" "xA9078A" "xB3F1FB" "xB90566" "xB9391F" "xBC0288" "xC0C0E0" "xC480A5" "xC8AEAF" "xCBFD28" "xCF16B1" "xD155CE" "xD702F7" "xD96FB9" "xE6C5FC" "xE7A6D6" "xE9B084" "xEA6A0F" "xEB5D5F" "xEFA14D" "xF08323" "xF48646" "xF8E400" "xFCCAFA" }
    traits = { "state_trait_bergslagen" "state_trait_scandinavian_forests" "state_trait_natural_harbors" }
    city = "x9686A5"
    port = "x93C3BC"
    farm = "xF48646"
    mine = "x6F40EC"
    wood = "x4C9918"
    arable_land = 30
    arable_resources = { "bg_rye_farms" "bg_livestock_ranches" }
    capped_resources = {
        bg_iron_mining = 36
        bg_lead_mining = 18
        bg_logging = 23
        bg_fishing = 11
    }
    resource = {
        type = "bg_oil_extraction"
        undiscovered_amount = 5
    }
    naval_exit_id = 3000
}
```

## 基础特征

每个州区域都以其唯一的脚本名称和唯一 ID 号定义。脚本名称同时充当 [localization](Localization.md)（本地化）键。

所有州区域必须包含 `provinces.png` 地图图像中的一个或多个“省份”图块。省份由该图像中的六位 [hex color](http://en.wikipedia.org/wiki/Web_colors#Hex_triplet)（十六进制颜色）定义，每个前缀字母 `x`，并可选地用双引号括起。

海洋州区域（用于定义 [sea nodes](Naval warfare.md)，即海洋节点）仅包含这些特征，别无其他。

海洋州区域示例：

```
STATE_BALTIC_SEA = {
    id = 3000
    provinces = { "x08FAFA" }
}
```

## 其他特征

陆地区域还有许多其他特征。

### 不可通行省份与黄金地段

州可以拥有不可通行省份和黄金地段省份的列表。二者都与分割州（split state）相关，因为它们影响分配给每个州的资源比例。不可通行省份不计入分割州比例，并且还会阻止军事前线的形成。黄金地段省份在分割州比例中拥有五倍的权重[1]。

这两个列表都只应包含为该州区域定义的省份，且不应互相包含对方的省份。

示例：

```
    provinces = { "x029E85" "x04BB3B" "x1C7417" "x2A3D46" "x42973E" "x4408AB" "x445D59" "x477680" "x4DD36E" "x56FE77" "x60FDC2" "x638173" "x6D4CDF" "x706E00" "x71D428" "x76E306" "x7FFBF0" "x8A69A7" "x939612" "x9910E9" "xA5A916" "xA67A6E" "xA6D36E" "xA91194" "xAD54BC" "xB7B05B" "xBC374E" "xC29C28" "xCF4105" "xD735DB" "xE02CB6" "xE3C4F2" "xF37396" "xF8375D" "xF9BDCB" "xFCFD83" "xFF8539" "xFFE074" }
    impassable = { "xA5A916" "xBC374E" "x04BB3B" "x9910E9" "xCF4105" "x477680" "x56FE77" }
    prime_land = { "xE02CB6" "x60FDC2" "x42973E" }
```

### 枢纽

枢纽是已定义的、代表州区域内一座城市的省份。在视觉上，每种枢纽的规模会随州区域内与其类型相关的建筑数量增长而出现和扩大。大多数枢纽除了通过其存在与否更新道路/铁路网络之外，没有游戏机制上的作用；港口枢纽则定义条约港的位置。

| 枢纽 | 建筑 |
|---|---|
| 城市 | 未被其他枢纽包含的所有建筑 |
| 农场 | 所有农业和种植园 |
| 矿场 | 所有矿山和石油钻井 |
| 港口 | 造船厂和军用造船厂、渔业和捕鲸业、港口和海军基地 |
| 木材 | 伐木场 |

枢纽可以重叠，即同一个省份可以是两个或更多枢纽；并非每个州区域都拥有每种枢纽，内陆州尤其没有港口枢纽。每个枢纽通过列出用于该枢纽的省份来定义。

### 州特质

一些州区域拥有已定义的 [state trait](https://vic3.paradoxwikis.com/State_trait)（州特质）。它们列在 `traits` 块中，每个特质以其脚本名称加引号列出。州特质定义于 common/state_traits。

州特质由唯一的脚本名称（同时充当本地化键）、一个图标以及通常一个 modifier（修正）定义。州特质还可以有一个使其修正失效的科技，或一个殖民所需科技，后者会阻止拥有该特质的州区域在研究出该科技之前被殖民。

州特质示例：

```
state_trait_severe_malaria = {
    icon = "gfx/interface/icons/state_trait_icons/severe_malaria.dds"
	
	required_techs_for_colonization = { "quinine" }
	disabling_technologies = { "malaria_prevention" }
	
	modifier = {
		state_non_homeland_colony_growth_speed_mult = -0.95
		state_non_homeland_mortality_mult = 0.25
	}
}
```

effect（游戏内效果脚本）也可以在游戏过程中为州区域添加或移除州特质。

### 资源

州区域中的资源分为几类：可耕地与耕地资源、有上限资源以及单独资源。在所有情况下，资源都定义为 [buildings](Building modding.md)（建筑），且许多资源特征由建筑本身的特征决定。

#### 可耕地

可耕地简单定义为一个整数，外加一个在州区域内使用可耕地的建筑列表。

示例：

```
    arable_land = 30
    arable_resources = { "building_rye_farm" "building_livestock_ranch" }
```

未被利用的可耕地总是被一个维持生存型建筑占用，每个州区域将其定义为特定类型的建筑，例如 `subsistence_building = "building_subsistence_pastures"`。

可耕地数量可以在游戏过程中通过 effect 改变。

#### 有上限资源

有上限资源是一个建筑块，每个建筑都定义了最大等级。这些资源从游戏开始时就是可见的。

示例：

```
    capped_resources = {
        building_iron_mine = 36
        building_lead_mine = 18
        building_logging_camp = 23
        building_fishing_wharf = 11
    }
```

州区域中有上限资源的数量或存在与否可以在游戏过程中改变。

#### 单独资源

单独资源与有上限资源类似，但每一个都在自己的块中定义。它们最常用于可发现的资源，这类资源在游戏中不会立即显示，而是在该州的所有者研究出所需技术后定期显现。此外，如果某建筑被设为可耗尽，此块可以定义其耗尽后替代它的建筑。

示例：

```
    resource = {
        type = "building_gold_field"
        depleted_type = "building_gold_mine"
        undiscovered_amount = 12
    }
    resource = {
        type = "building_rubber_plantation"
        discovered_amount = 10
        undiscovered_amount = 6
    }
    resource = {
        type = "building_oil_rig"
        undiscovered_amount = 5
    }
```

### 海洋出口

沿海州区域应有一个 `naval_exit_id`，即某个海洋区域的州区域 ID。它定义了哪个海洋区域/海洋节点与该州区域相邻，用于航运线路和海上入侵。

## 州历史

另见：
新州模组制作
州的初始所有权定义于 common/history/states。未修改的《维多利亚3》将所有州历史放在文件 `00_states.txt` 中，但 mod 可以将其拆分为多个文件。

州历史文件使用一个 `STATES` 块，其中包含若干州区域。

```
STATES = {
	s:STATE_LOWER_EGYPT = {
		create_state = {
			country = c:EGY
			owned_provinces = { x409060 x2050A0 x7ABE4B x50D0E0 x5011E0 x48E2A5 x6F13AD xD050E0 xF47AAA xA0D020 xC09060 xC37990 }
		}
		
		add_homeland = cu:misri
	}
    s:STATE_IONIAN_ISLANDS = {
		create_state = {
			country = c:ION
			owned_provinces = { x4B79CA x405060 }
		}	
		# Homelands and claims are defined on the state region, not for individual states
		add_homeland = cu:greek
		add_claim = c:GRE
	}
    s:STATE_BALUCHISTAN = {
		create_state = {
			country = c:OMA
			owned_provinces = { "xB7B2BD" }
		}
		create_state = {
			country = c:KAL
			owned_provinces = { "x0279A0" "x0BAF8C" "x1161D9" "x1D0224" "x2B7441" "x35754E" "x3C9B5F" "x43F4B8" "x4529BD" "x4B2EAD" "x4DC3FF" "x4F800F" "x556C63" "x56CF62" "x5CBA3C" "x61D696" "x626396" "x62BEAA"  "x6D6D6B" "x782112" "x7D60E7" "x8DC922" "x954C12" "x97C017" "xA3655B" "xB2AAA7" "xBAE3D2" "xBB836E" "xC6D9E8" "xCD77FD" "xD4EC50" "xD6DD8A" "xDEE571" "xDF30A0"  "xE7A309" "xE92A58" "xEC696F" "xF78D0D"  "x1EF53E" }
		}
		create_state = {
			country = c:MAK
			owned_provinces = { "x978421" "x4E09C5" "xF9577D" "x45F2DD" "x113E0B" "x7FE584" "xC070E0" "xC6E602" "xB0F79E" "x407060" "x951063" "x8ED831" "x2E7961" "xE87BBF" "x968562" "x675BCE" "x2FF46D" }
		}
		create_state = {
			country = c:KAN
			owned_provinces = { "xE712E1" "xF1414C" "x17D8AB" "x3EFD1E" "x109CC0" "x4070E0" "x9EED5C" "xA55509" "xD575B0" }
		}
		
		add_homeland = cu:baluchi
		add_homeland = cu:pashtun
	}
}
```

州区域通过 `s:<state region name>` 调用，并可被赋予故乡和国家的宣称。每个州区域必须至少从中创建一个州。

每个创建的州都通过 effect `create_state` 从一个州区域定义，需要所有者国家和一个省份列表。省份列表可以是州区域的一部分或全部。州还可以通过 `state_type` 定义，州默认为已合并，但也可定义为 `unincorporated`（未合并）。注意，无论州历史如何设定，一个国家的首都州都会自动且立即被合并。

开局即拥有殖民事务的国家，还会在每个同时毗邻去中心化国家的自有州区域中拥有殖民地。这些初始殖民地无视殖民宣称。

common/history/states 中定义的州会在 common/history/buildings 和 common/history/pops 中被引用，因此在更改初始设置时，注意更新所有相关文件。

## 州脚本文档

以下 [effects](Effect.md)、[event targets](Event target.md) 和 [triggers](Trigger.md) 可用于州或州区域 scope（作用域）。其中少数可用于任一作用域。

### 州作用域

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| activate_building | 激活州内的一座建筑 | activate_building = { building = building_key } |  |
| activate_production_method | 为国家/州内某类型的建筑激活指定生产方式 | activate_production_method = { building_type = building_key production_method = production_method_key } |  |
| add_acceptance | 为州内某一文化添加接受度变化 | add_acceptance = { culture = cu:romanian value = -10 } |  |
| add_cultural_community | 为作用域州内的目标文化添加文化社区 | scope:some_state = { add_cultural_community = cu:zulu } | culture |
| add_culture_standard_of_living_modifier | 为作用域州内的给定文化施加一个生活水平 modifier。除必需的 culture 参数外，此 effect 的语法与 add_modifier 相同 | add_culture_standard_of_living_modifier = { culture = culture_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } |  |
| add_loyalists_in_state | 为作用域州内的人口添加忠诚派。除 value 外所有参数均为可选 | value 是每个人口中转向忠诚主义的比例。若指定 interest_group，则人口根据其利益集团成员身份获得忠诚派。pop type 与 strata 互斥。 add_radicals_in_state = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } |  |
| add_modifier | 为作用域中的对象添加一个限时 modifier 效果 | add_modifier = { name = static_modifier_name days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay |  |
| add_radicals_in_state | 为作用域州内的人口添加激进派。除 value 外所有参数均为可选 | value 是每个人口中转向激进主义的比例。若指定 interest_group，则人口根据其利益集团成员身份获得激进派。pop type 与 strata 互斥。 add_radicals_in_state = { value = 0.2 interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> culture = <scope/cu:key> religion = <scope/rel:key> } |  |
| add_religion_standard_of_living_modifier | 为作用域州内的给定宗教施加一个生活水平 modifier。除必需的 religion 参数外，此 effect 的语法与 add_modifier 相同 | add_religion_standard_of_living_modifier = { religion = religion_scope days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent multiplier = value (optional) #multiplies the values of the static modifier is_decaying = yes (optional) #sets modifier to decay in strength over its duration } |  |
| cede_treaty_port | 将作用域州中的一个条约港割让给目标国家 | cede_treaty_port = scope/country | country |
| convert_population | 将不同宗教人口的 X% 转换为指定宗教 | convert_population = { target = rel:catholic value = 0.5 } |  |
| create_building | 在作用域州内创建一座建筑。支持的值有： | building = <building> activate_production_methods = { <production_methods> } subsidized = yes/no reserves = [0..1] (percentage of cash reserves the building should be created with) add_ownership = { (mutually exclusive with level) country = { (give ownership levels to a specific country) country = s:GBR (country script target) levels = 5 } country = { (give ownership levels to a specific building) type = building_financial_district (building type that will get ownership levels, should be self or other ownership type) region = STATE_SINAI (region where owning building is placed) country = s:GBR (country script target for a region) levels = 3 } } level = arable_land/integer(mutually exclusive with add_ownership) If level is arable_land, the building will be of the necessary level to exhaust all available arable land in the state. If level is an integer, the building will be of that level Please note: this effect works a little differently if there already is a building of the specified type in the state. If that happens: 1. the level will be the maximum between the scripted level and the level of the existing building 2. the cash reserves will be the maximum between the scripted value and the existing cash reserves |  |
| create_mass_migration | 发起某文化从来源国向作用域州的大规模迁移 | create_mass_migration = { origin = c:GBR culture = cu:english } |  |
| create_pop | 在作用域州内创建一个人口 |  |  |
| deactivate_building | 停用州内的一座建筑 | deactivate_building = { building = building_key } |  |
| every_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成状况 | every_harvest_condition = { limit = { <triggers> } #optional <effects> } | harvest_condition |
| every_neighbouring_state | 遍历与当前作用域相邻的所有州。注意使用英式拼写 | every_neighbouring_state = { limit = { <triggers> } #optional <effects> } | state |
| every_scope_building | 遍历以下作用域中的所有建筑：州、国家 | every_scope_building = { limit = { <triggers> } #optional <effects> } | building |
| every_scope_culture | 遍历作用域中的所有文化 | every_scope_culture = { limit = { <triggers> } #optional <effects> } | culture |
| every_scope_pop | 遍历以下作用域中的所有人口：国家、州、利益集团、文化 | every_scope_pop = { limit = { <triggers> } #optional <effects> } | pop |
| every_scope_strait | 遍历在作用域州或国家拥有陆地端点的所有海峡 | every_scope_strait = { limit = { <triggers> } #optional <effects> } | strait |
| every_sea_node_adjacent_state | 遍历与某州共享海洋节点的所有州 | every_sea_node_adjacent_state = { limit = { <triggers> } #optional <effects> } | state |
| force_resource_depletion | 强制触发州内的一次资源耗尽 | force_resource_depletion = bg_gold_mining |  |
| force_resource_discovery | 强制触发州内的一次资源发现 | force_resource_discovery = bg_gold_mining |  |
| kill_population_in_state | 杀死作用域州内人口中一定数量的个体。 | 除 percent 外所有参数均为可选。pop type 与 strata 不能同时使用。 kill_population = { value = <integer value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } |  |
| kill_population_percent_in_state | 杀死作用域州内人口的一个百分比。 | 除 percent 外所有参数均为可选。pop type 与 strata 不能同时使用。 kill_population_percent = { percent = <decimal value> culture = <scope/cu:key> religion = <scope/rel:key> interest_group = <scope/ig:key> pop_type = <scope/pop_type:key> strata = <key> } |  |
| liberate_slaves | 解放国家/州内的所有奴隶 | liberate_slaves = yes |  |
| ordered_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成状况 | ordered_harvest_condition = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | harvest_condition |
| ordered_neighbouring_state | 遍历与某州区域相邻的所有州 | ordered_neighbouring_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_province | 遍历作用域州内的所有省份 | ordered_province = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | province |
| ordered_scope_building | 遍历以下作用域中的所有建筑：州、国家 | ordered_scope_building = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | building |
| ordered_scope_culture | 遍历作用域中的所有文化 | ordered_scope_culture = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | culture |
| ordered_scope_pop | 遍历以下作用域中的所有人口：国家、州、利益集团、文化 | ordered_scope_pop = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | pop |
| ordered_scope_strait | 遍历在作用域州或国家拥有陆地端点的所有海峡 | ordered_scope_strait = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | strait |
| ordered_sea_node_adjacent_state | 遍历与某州共享海洋节点的所有州 | ordered_sea_node_adjacent_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| random_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成状况 | random_harvest_condition = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | harvest_condition |
| random_neighbouring_state | 遍历与某州区域相邻的所有州 | random_neighbouring_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| random_province | 遍历作用域州内的所有省份 | random_province = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | province |
| random_scope_building | 遍历某个州、国家中的所有建筑 | random_scope_building = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | building |
| random_scope_culture | 遍历 scope 中的所有文化 | random_scope_culture = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | culture |
| random_scope_pop | 遍历某个国家、州、利益集团、文化中的所有人口 | random_scope_pop = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | pop |
| random_scope_strait | 遍历在 scope 州或国家中拥有陆地端点的所有海峡 | random_scope_strait = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | strait |
| random_sea_node_adjacent_state | 遍历与某个州共享海上节点的所有州 | random_sea_node_adjacent_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| remove_building | 移除 scope 州中某建筑的所有等级 | remove_building = building_key |  |
| remove_modifier | 移除 scope 对象上的限时修正效果 | remove_modifier = static_modifier_name |  |
| remove_resource_potential | 从一个州区域的资源潜力中移除某建筑类型 | remove_resource_potential = building_iron_mine |  |
| reset_hub_names | 重置 scope 州中所有枢纽的名称 | reset_hub_names = yes |  |
| reset_state_name | 重置 scope 州的名称 | reset_state_name = yes |  |
| set_available_for_autonomous_investment | 将某建筑类型设为当前 scope 州中可进行自主投资的对象 | set_available_for_autonomous_investment = building type scope | building_type |
| set_devastation | 设定某州区域或州的破坏度 |  |  |
| set_hub_name | 将 scope 州中某枢纽的名称设为某个本地化字符串 | set_state_name = { type = city（可以是任意枢纽类型 city/port/farm/mine/wood） name = HUB_NAME_STATE_KIEV_city_ukrainian } |  |
| set_hub_names | 根据州区域名称、枢纽类型和指定后缀，将 scope 州中所有枢纽的名称设为对应的本地化字符串 | set_hub_names = ukrainian |  |
| set_state_name | 将 scope 州的名称设为某个本地化字符串 | set_state_name = STATE_KIEV_ukrainian |  |
| set_state_owner | 设定州的所有者 | set_state_owner = scope | country |
| set_state_type | 将某州设定为特定类型（已合并、未合并、条约港） |  |  |
| start_building_construction | 在 scope 州中开始以政府建设的方式建造某建筑 | start_building_construction = building_barracks |  |
| start_privately_funded_building_construction | 在 scope 州中开始以私人建设的方式建造某建筑 | start_privately_funded_building_construction = building_barracks |  |
| unset_available_for_autonomous_investment | 将某建筑类型设为当前 scope 州中不可进行自主投资的对象 | unset_available_for_autonomous_investment = building type scope | building_type |

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| any_harvest_condition | 遍历影响某个州、州区域、战略区域或国家的所有收成状况 | any_harvest_condition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | harvest_condition |
| any_neighbouring_state | 遍历与某个州区域相邻的所有州 | any_neighbouring_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| any_province | 遍历 scope 州中的所有省份 | any_province = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | province |
| any_scope_building | 遍历某个州、国家中的所有建筑 | any_scope_building = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | building |
| any_scope_culture | 遍历 scope 中的所有文化 | any_scope_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | culture |
| any_scope_pop | 遍历某个国家、州、利益集团、文化中的所有人口 | any_scope_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | pop |
| any_scope_strait | 遍历在 scope 州或国家中拥有陆地端点的所有海峡 | any_scope_strait = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | strait |
| any_sea_node_adjacent_state | 遍历与某个州共享海上节点的所有州 | any_sea_node_adjacent_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| arable_land | 检查州的可耕地数量 | arable_land > 10 | value |
| available_jobs | 检查州中非自给建筑的可用地工作岗位数量 | available_jobs > 10000 | value |
| blockade_level | 与州的封锁等级进行比较 | blockade_level > 0.1 | value |
| can_activate_production_method | 检查 scope 州中特定类型的建筑能否启用指定的生产方式 | can_activate_production_method = { building_type = <key> production_method = <key> } |  |
| can_construct_building | 检查 scope 州中能否建造 1 级 <building_type> | can_construct_building = <building_type> |  |
| check_area | 将对象的面积与另一对象进行比较 |  |  |
| cultural_acceptance_delta | 与 scope 州中某文化接受度的当前本地增量（修正值）进行比较 | cultural_acceptance_delta = { target = cu:romanian value < -10 } | value |
| culture_percent_state | 检查某州人口中特定文化是否占一定比例 | scope:example_state = { culture_percent_state = { target = cu:dixie value >= 0.2 } } | value |
| devastation | 比较给定州的破坏度 | devastation > 5 | value |
| free_arable_land | 检查州的空闲可耕地数量 | free_arable_land > 0 | value |
| has_active_building | 若州拥有某个处于活跃状态的建筑类型则为真 | has_active_building = building |  |
| has_assimilating_pops | 检查州中是否有正在同化的人口。 |  | boolean |
| has_building | 若州/市场/州区域/国家拥有某建筑类型则为真 | has_building = building |  |
| has_claim_by | 检查某州是否被某国家宣称 | any_state = { owner = root has_claim_by = c:MEX } | country |
| has_converting_pops | 检查州中是否有正在转教的人口。 |  | boolean |
| has_cultural_community | 检查某文化在 scope 州中是否有文化社区。 | has_cultural_community = <culture> |  |
| has_decree | 检查 scope 州是否拥有特定类型的法令 | has_decree = <key> |  |
| has_famine | 检查州或国家是否发生饥荒 | has_famine = yes/no | boolean |
| has_mobilizing_unit | 检查 scope 州中是否有建筑维持着当前正在动员的作战单位 | has_mobilizing_unit = bool | boolean |
| has_modifier | 检查受支持的 scope 是否拥有某个限时修正 | has_modifier = <key> |  |
| has_port_state | 检查 scope 州是否至少拥有一个港口 | has_port = yes/no | boolean |
| has_potential_resource | 检查指定的建筑组是否被允许在 scope 州中。用于检查某州是否有可能生产某种资源 | has_potential_resource = bg_rubber_plantations | building_group |
| has_state_trait | 检查 scope 州是否拥有某个特质 | has_state_trait = key |  |
| ig_state_pol_strength_share | 若 scope 中的利益集团在该州拥有指定的政治力量份额则为真 | ig_state_pol_strength_share = { target = scope:target_ig value = 0.3 } | value |
| incorporation_progress | 检查州的合并进度 | incorporation_progress > 0.25 | value |
| infrastructure | 比较给定州的基础设施值 | infrastructure > 10 | value |
| infrastructure_delta | 比较给定州的基础设施差额 | infrastructure_delta > 0 | value |
| infrastructure_usage | 比较给定州的基础设施使用量 | infrastructure_usage > 10 | value |
| is_being_bombarded | 检查某州当前是否正被敌方舰队炮击港口 |  | boolean |
| is_blockaded_by | 检查某州是否被某国家封锁 |  | country |
| is_capital | 检查州是否为其所有者的首都 = bool |  | boolean |
| is_coastal | 检查州是否临海（非不可通行海域） | is_coastal = yes/no | boolean |
| is_homeland_of_country_cultures | 检查州是否为目标国家任一主流文化的家园 | is_homeland_of_country_cultures = <country> | country |
| is_in_revolt | 检查州是否有机会分裂出一个革命或脱离的国家 | is_in_revolt = yes/no。 | boolean |
| is_incorporated | 检查州是否已合并 = bool |  | boolean |
| is_isolated_from_market | 检查州是否与其市场隔离 |  | boolean |
| is_largest_state_in_region | 检查州是否为所在州区域中最大的州 = bool |  | boolean |
| is_mass_migration_target | 大规模迁移的目标是州。 | is_mass_migration_target = yes | boolean |
| is_mass_migration_target_for_culture | scope 州是指定文化的大规模迁移目标。 | is_mass_migration_target_for_culture = scope:my_culture | culture |
| is_potential_treaty_port | 检查 scope 州是否有潜力成为目标国家的条约港 | is_potential_treaty_port = c:FRA | country |
| is_production_method_active | 检查 scope 州中特定类型的建筑是否已启用指定的生产方式 | is_production_method_active = { building_type = <key> production_method = <key> } |  |
| is_sea_adjacent | 检查州是否临海（普通或不可通行海域） | is_sea_adjacent = yes/no | boolean |
| is_slave_state | 检查州是否正在雇用或有可能雇用奴隶。 |  | boolean |
| is_split_state | 检查 scope 州是否为被分割的州。 | scope:example_state = { is_split_state = yes } | boolean |
| is_strategic_objective | 检查 scope 州是否为某国家的战略目标 | is_strategic_objective = <country> | country |
| is_target_of_wargoal | 检查州是否为涉及某国家的战争中任一战争目标的目标 | has_war_goal = <country> | country |
| is_treaty_port | 检查 scope 州是否为条约港 | is_treaty_port = yes/no | boolean |
| is_under_colonization | 检查州是否正在被殖民 | is_under_colonization = yes/no | boolean |
| is_world_market_hub | 检查州是否为世界市场枢纽 | is_world_market_hub = yes | boolean |
| literacy_rate | 检查人口、州或国家是否拥有一定的识字率 | literacy = value | value |
| loyalist_fraction | 比较州或国家中人口的忠诚派比例，除 value 外所有参数均为可选 | loyalist_fraction = { value = <script_value> pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> } | value |
| loyalists | 比较给定州的忠诚度，即忠诚派的比例 | loyalists > 0.2 | value |
| market_access | 检查 scope 州的市场接入 | market_access > 0.8 | value |
| most_prominent_revolting_interest_group | 检查 scope 州中最突出的叛乱利益集团是否为给定的利益集团类型。若 scope 州未处于叛乱状态则判定为假。 | most_prominent_revolting_interest_group = ig_landowners |  |
| num_cultural_communities | 检查州中的文化社区数量 | num_cultural_communities > 5 | value |
| obstinance | 比较州的顽固度 | obstinance > 0.5 | value |
| political_strength_share | 检查某人口类型、宗教或文化在国家或州中的政治力量份额。必须且只能指定 pop_type、religion 或 culture 其中之一。 | political_strength_share = { pop_type/religion/culture = <key/scope> value <compare operator> <value> } | value |
| pollution_generation | 比较州中所有建筑的总污染产生量 |  | value |
| pop_type_percent_state | 检查某州人口中特定人口类型是否占一定比例 | scope:example_state = { pop_type_percent_state = { target = pop_type:laborer value <= 0.8 } } | value |
| population_by_culture | 比较 scope 州中目标文化的当前人口 | population_by_culture = { target = cu:romanian value > 2500 } | value |
| primary_cultures_percent_state | 检查某州人口中该国主流文化是否占一定比例 | scope:example_state = { primary_cultures_percent_state >= 0.2 } | value |
| radical_fraction | 比较州或国家中人口的激进派比例，除 value 外所有参数均为可选 | radical_fraction = { value = <script_value> pop_type = <key> strata = <key> culture = <key/scope> religion = <key/scope> } | value |
| relative_infrastructure | 比较州的基础设施与其基础设施使用量 | relative_infrastructure > 1.1 | value |
| religion_percent_state | 检查某州人口中特定宗教是否占一定比例 | scope:example_state = { religion_percent_state = { target = rel:catholic value <= 0.8 } } | value |
| state_cultural_acceptance | 检查目标文化的人口在 scope 州中的接受度 | state_cultural_acceptance = { target = cu:french value >= 50 | value |
| state_exports | 比较从 scope 州出口到目标州（若已设定）或整体世界市场（若未指定州）的总商品单位数 | state_exports = { target = state scope (optional) goods = key (optional) value >= 100 } | value |
| state_has_building_group_levels | 检查州中某建筑组的建筑等级总和 | state_has_building_group_levels = { type = bg_heavy_industry value >= 100 } | value |
| state_has_building_levels | 检查州的建筑等级总和 | state_has_building_levels >= 10 | value |
| state_has_building_type_levels | 检查州中某建筑类型的建筑等级总和 | state_has_building_type_levels = { target = bt:building_barracks value >= 100 } | value |
| state_has_goods_shortage | 检查州的任何建筑输入是否出现商品短缺 | state_has_goods_shortage = yes/no | boolean |
| state_has_national_awakening | 检查 scope 州是否位于拥有活跃的民族觉醒地图标记的州区域中 | state_has_national_awakening = yes/no | boolean |
| state_imports | 比较从目标州进口到 scope 州的总商品单位数 | state_imports = { target = state scope (optional) goods = key (optional) value >= 100 } | value |
| state_is_eligible_as_mass_migration_target | 检查州是否完全能够接收大规模迁移。 | any_state = { state_is_eligible_as_mass_migration_target = yes } | boolean |
| state_population | 检查 scope 州的总人口 | state_population <= 250000 | value |
| state_religious_acceptance | 检查给定宗教的人口在 scope 州中的接受度 | state_religious_acceptance = { target = rel:catholic value >= 50 | value |
| state_trade | 比较 scope 州与目标州（若已设定）或整体世界市场（若未指定州）之间交易的总商品单位数 | state_trade = { target = state scope (optional) goods = key (optional) value >= 100 } | value |
| state_unemployment_rate | 检查 scope 州的失业率（百分比） | state_unemployment_rate > 0.1 | value |
| tax_capacity | 检查 scope 州的税收能力 | tax_capacity > 50 | value |
| tax_capacity_usage | 检查 scope 州的税收能力使用量 | tax_capacity_usage > 50 | value |
| total_urbanization | 比较给定州的总城镇化 | total_urbanization > 5 | value |
| turmoil | 比较给定州的动荡，即激进派的比例 | turmoil > 0.2 | value |
| wealth_share | 检查某人口类型、宗教或文化在国家或州中的财富政治力量份额。必须且只能指定 pop_type、religion 或 culture 其中之一。 | wealth_share = { pop_type/religion/culture = <key/scope> value <compare operator> <value> } | value |
| world_market_access | 检查 scope 州的世界市场接入 | world_market_access > 0.8 | value |
| Event target | 描述 | 目标 scope |
|---|---|---|
| ai_state_value | scope 到目标国家拥有该 scope 州的 AI 意愿值（示例：value = ai_state_value:root） | value |
| ai_treaty_port_value | scope 到目标国家想在该州拥有条约港的 AI 意愿值（示例：value = ai_treaty_port_value:root） | value |
| average_expected_sol | 获取该 scope 的平均预期生活水平 | value |
| average_sol | 获取该 scope 的平均生活水平 | value |
| b | scope 到该州中指定键值的建筑，示例：b:building_port | building |
| controller | scope 到该对象的控制者 | country |
| decree_cost | scope 到某州施行某项法令的消耗 authority > decree_cost:decree_road_maintaintenance | value |
| gdp | 获取 scope 国家的年度预测 GDP | value |
| land_controller_hq | 返回省份或州控制者的陆地总部 | hq |
| land_hq | 返回省份或州所有者的本地陆地总部 | hq |
| market | scope 到该对象的市场 | market |
| mass_migration_culture | scope 到某州大规模迁移的目标文化 | culture |
| migration_pull | 获取某州的迁移拉力或某国的大规模迁移拉力。 | value |
| modifier | scope 到当前对象拥有的指定键值的 modifier 类型数值，示例：modifier:country_influence_add | boolean, value |
| nf | scope 到应用于该州的指定键值的法令，示例：nf:decree_road_maintaintenance | decree |
| num_provinces | 获取 scope 实体当前的省份数量 | value |
| num_world_market_hub_trade_center_levels | 获取与 scope 世界市场中心州相关联的贸易中心等级总数 | value |
| owner | scope 到该对象的所有国 | country |
| population_below_expected_sol | scope 到该州人口中低于其预期生活水平的当前百分比（0-1） | value |
| region | scope 到该对象的战略区域！ | strategic_region |
| sg | 从某州 scope 到指定键值的 StateGoods，示例：sg:wood | state_goods |
| state_region | scope 到某州的州区域 | state_region |
| theater | 从 BattleSide 或州 scope 到其战区 | theater |
| world_market_hub | scope 到与 scope 州相关联的世界市场中心州 | state |

### 州区域 scope

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_arable_land | 在州区域中增加/移除可耕地 |  |  |
| add_claim | 将 scope 州区域添加为目标国家的宣称 | add_claim = scope/country | country |
| add_devastation | 在州区域中增加/移除荒废度 |  |  |
| add_homeland | 将 scope 州区域添加为目标文化的本土 | add_homeland = cu:culture | culture |
| add_pollution | 提高/降低 scope 州区域的污染等级 | add_pollution = 10 |  |
| add_state_trait | 在 scope 州区域中添加州特质 | add_state_trait = <state_trait_name> |  |
| create_state | 在州区域中创建一个州 |  |  |
| every_harvest_condition | 遍历所有影响某个州、州区域、战略区域或国家的收成状况 | every_harvest_condition = { limit = { <triggers> } #optional <effects> } | harvest_condition |
| every_neighbouring_state | 遍历所有与当前 scope 相邻的州 注意英式拼写 | every_neighbouring_state = { limit = { <triggers> } #optional <effects> } | state |
| every_scope_country | 遍历在受支持的 scope（目前包括：market、state_region、strategic region）中存在的所有国家 | every_scope_country = { limit = { <triggers> } #optional <effects> } | country |
| every_scope_interest_marker | 遍历以下对象中的所有利益标记：country、state_region、strategic region | every_scope_interest_marker = { limit = { <triggers> } #optional <effects> } | interest_marker |
| every_scope_state | 遍历包含以下对象省份的所有州：country、state_region、theater、front 或 strait | every_scope_state = { limit = { <triggers> } #optional <effects> } | state |
| finish_harvest_condition | 结束 scope 州区域中某种类型的收成状况 | finish_harvest_condition = <key> |  |
| ordered_harvest_condition | 遍历所有影响某个州、州区域、战略区域或国家的收成状况 | ordered_harvest_condition = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | harvest_condition |
| ordered_neighbouring_state | 遍历所有与某个州区域相邻的州 | ordered_neighbouring_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_scope_country | 遍历在受支持的 scope（目前包括：market、state_region、strategic region）中存在的所有国家 | ordered_scope_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_scope_interest_marker | 遍历以下对象中的所有利益标记：country、state_region、strategic region | ordered_scope_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | interest_marker |
| ordered_scope_state | 遍历包含以下对象省份的所有州：country、state_region、theater、front 或 strait | ordered_scope_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| random_harvest_condition | 遍历所有影响某个州、州区域、战略区域或国家的收成状况 | random_harvest_condition = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | harvest_condition |
| random_neighbouring_state | 遍历所有与某个州区域相邻的州 | random_neighbouring_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| random_scope_country | 遍历在受支持的 scope（目前包括：market、state_region、strategic region）中存在的所有国家 | random_scope_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_scope_interest_marker | 遍历以下对象中的所有利益标记：country、state_region、strategic region | random_scope_interest_marker = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | interest_marker |
| random_scope_state | 遍历包含以下对象省份的所有州：country、state_region、theater、front 或 strait | random_scope_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| remove_claim | 移除目标国家对 scope 州区域的宣称 | add_claim = scope/country | country |
| remove_homeland | 移除目标文化在 scope 州区域的本土 | remove_homeland = cu:culture | culture |
| remove_resource_potential | 从州区域的资源潜力中移除某种建筑类型 | remove_resource_potential = building_iron_mine |  |
| remove_state_trait | 在 scope 州区域中移除州特质 | remove_state_trait = <state_trait_name> |  |
| set_devastation | 设置某州区域或州的荒废度 |  |  |
| set_owner_of_provinces | 将州区域中的一组省份给予特定国家 | set_owner_of_provinces = { country = <scope> provinces = { <province list> } } |  |
| start_harvest_condition | 在 scope 州区域中启动某种类型的收成状况（如已存在则刷新） | start_harvest_condition = <key> |  |
| start_harvest_condition_with_params | 在 scope 州区域中启动某种类型的收成状况，可选择提供强度和持续时间（以天为单位） | start_harvest_condition_with_params = { type = flood intensity = 5 (optional) duration = 5 (optional) } |  |

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| any_harvest_condition | 遍历所有影响某个州、州区域、战略区域或国家的收成状况 | any_harvest_condition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | harvest_condition |
| any_neighbouring_state | 遍历所有与某个州区域相邻的州 | any_neighbouring_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| any_scope_country | 遍历在受支持的 scope（目前包括：market、strategic region）中存在的所有国家 | any_scope_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_scope_interest_marker | 遍历以下对象中的所有利益标记：country、strategic region | any_scope_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | interest_marker |
| any_scope_state | 遍历包含以下对象省份的所有州：country、state_region、theater、front 或 strait | any_scope_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| check_area | 比较两个对象的面积 |  |  |
| contains_capital_of | 检查 scope 州区域是否包含目标 tag 的首都 | contains_capital_of = country scope/tag |  |
| has_building | 若某州/市场/州区域/国家拥有某种建筑类型则为真 | has_building = building |  |
| has_harvest_condition | 检查 scope 州区域是否有某种类型的收成状况 | has_harvest_condition = drought |  |
| infrastructure | 比较某给定州的基础设施值 | infrastructure > 10 | value |
| infrastructure_delta | 比较某给定州的基础设施收支 | infrastructure_delta > 0 | value |
| infrastructure_usage | 比较某给定州的基础设施使用值 | infrastructure_usage > 10 | value |
| is_homeland | 检查 scope 州区域是否为目标文化的本土 | is_homeland = culture scope/name |  |
| is_state_region_land | 检查该州区域是否位于陆地上 |  | boolean |
| pollution_amount | 比较州区域污染 |  | value |
| remaining_undepleted | 检查某州中资源的剩余数量，例如金矿 | remaining_undepleted = { type = bg_gold_mining amount > 1 } | value |

| Event target | 描述 | 目标 scope |
|---|---|---|
| market | scope 到该对象的市场 | market |
| num_provinces | 获取 scope 实体当前的省份数量 | value |
| region | scope 到该对象的战略区域！ | strategic_region |
| region_state | scope 到目标国家拥有的州，（示例：region_state:BIC） | state |

### 州 modifier 类型

`state_` modifier 类型将其效果应用于州。当应用于某个国家时，会影响该国拥有的所有州；同样，当应用于某个州区域时，会应用于该区域内的所有州。

由于篇幅原因，本表不包含基于文化或宗教的生活水平 modifier 类型 `state_[type]_standard_of_living_add`。

| Modifier 类型 | 本地化文本 | 类型 | 格式 | 备注 |
|---|---|---|---|---|
| state_academics_investment_pool_contribution_add | 学者投资池贡献 | additive | percent, good |  |
| state_academics_investment_pool_efficiency_mult | 学者投资池贡献效率 | multiplicative | percent, good |  |
| state_academics_mortality_mult | 学者的死亡率 | multiplicative | percent, bad |  |
| state_allow_assimilation_in_homeland_bool | 允许在本土州同化 | boolean | good |  |
| state_allow_assimilation_without_presence_bool | 始终允许同化为主文化 | boolean | good |  |
| state_allow_conversion_without_presence_bool | 始终允许皈依为国教 | boolean | good |  |
| state_aristocrats_investment_pool_contribution_add | 贵族投资池贡献 | additive | percent, good |  |
| state_aristocrats_investment_pool_efficiency_mult | 贵族投资池贡献效率 | multiplicative | percent, good |  |
| state_aristocrats_mortality_mult | 贵族的死亡率 | multiplicative | percent, bad |  |
| state_assimilation_mult | 同化 | multiplicative | percent, good |  |
| state_birth_rate_mult | 出生率 | multiplicative | percent, good |  |
| state_blockade_resistance_add | 封锁抗性 | additive | good |  |
| state_building_barrack_max_level_add | 兵营最大等级 | additive | good |  |
| state_building_conscription_center_max_level_add | 最大征兵上限 | additive | good |  |
| state_building_construction_sector_max_level_add | 建设部门最大等级 | additive | good |  |
| state_building_naval_fortification_max_level_add | 海防要塞最大等级 | additive | good |  |
| state_bureaucracy_population_base_cost_factor_mult | 行政力人口成本倍率 | multiplicative | percent, bad |  |
| state_bureaucrats_investment_pool_contribution_add | 官僚投资池贡献 | additive | percent, good |  |
| state_bureaucrats_investment_pool_efficiency_mult | 官僚投资池贡献效率 | multiplicative | percent, good |  |
| state_buy_orders_ammunition_add | 弹药采购订单 | additive | neutral |  |
| state_buy_orders_artillery_add | 火炮采购订单 | additive | neutral |  |
| state_buy_orders_small_arms_add | 轻武器采购订单 | additive | neutral |  |
| state_capitalists_investment_pool_contribution_add | 资本家投资池贡献 | additive | percent, good |  |
| state_capitalists_investment_pool_efficiency_mult | 资本家投资池贡献效率 | multiplicative | percent, good |  |
| state_clergymen_investment_pool_contribution_add | 教士投资池贡献 | additive | percent, good |  |
| state_clergymen_investment_pool_efficiency_mult | 教士投资池贡献效率 | multiplicative | percent, good |  |
| state_clerks_investment_pool_contribution_add | 职员（Clerks）投资池贡献 | additive | percent, good |  |
| state_clerks_investment_pool_efficiency_mult | 职员（Clerks）投资池贡献效率 | multiplicative | percent, good |  |
| state_colony_growth_creation_factor | 殖民增长产生 | multiplicative | good |  |
| state_colony_growth_speed_mult | 殖民地增长速度 | multiplicative | percent, good |  |
| state_conscription_rate_add | 征兵率 | additive | percent, good |  |
| state_conscription_rate_mult | 可征募营 | multiplicative | percent, good |  |
| state_construction_mult | 州建设效率 | multiplicative | percent, good |  |
| state_contiguous_incorporation_speed_mult | 接壤整合速度 | multiplicative | percent, good |  |
| state_control_strait_bool | 控制海峡 | boolean | good |  |
| state_conversion_mult | 皈依 | multiplicative | percent, good |  |
| state_decree_cost_mult | 法令成本 | multiplicative | percent, bad |  |
| state_dependent_political_participation_add | 受养人参政权 | additive | percent, good |  |
| state_dependent_wage_add | 受养人年收入 | additive | good |  |
| state_dependent_wage_mult | 受养人收入 | multiplicative | percent, good |  |
| state_devastation_decay_mult | 荒废度恢复 | multiplicative | percent, good |  |
| state_disallow_incorporation_bool | 州整合被禁止 | boolean | bad |  |
| state_education_access_add | 教育普及度 | additive | percent, good |  |
| state_education_access_wealth_add | 教育普及度（基于财富） | additive | percent, good |  |
| state_engineers_investment_pool_contribution_add | 工程师投资池贡献 | additive | percent, good |  |
| state_engineers_investment_pool_efficiency_mult | 工程师投资池贡献效率 | multiplicative | percent, good |  |
| state_expected_sol_from_literacy | 识字率带来的最低预期生活水平 |  | bad |  |
| state_expected_sol_mult | 最低预期生活水平 | multiplicative | percent, bad |  |
| state_export_advantage_mult | 出口贸易优势 | multiplicative | percent, good |  |
| state_farmers_investment_pool_contribution_add | 农民投资池贡献 | additive | percent, good |  |
| state_farmers_investment_pool_efficiency_mult | 农民投资池贡献效率 | multiplicative | percent, good |  |
| state_farmers_mortality_mult | 农民的死亡率 | multiplicative | percent, bad |  |
| state_food_security_add | 粮食安全 | additive | percent, good |  |
| state_fortification_bombardment_resistance_add | 海防要塞炮击抗性 | additive | good |  |
| state_fortification_naval_battle_mult | 海防要塞战斗防御 | multiplicative | percent, good |  |
| state_fortification_naval_invasion_add | 海防要塞登陆防御 | additive | good |  |
| state_free_state_pop_support_movement_anti_slavery_mult | 非蓄奴州的废奴运动人口吸引力 | multiplicative | percent, neutral |  |
| state_harvest_condition_disease_outbreak_duration_mult | 疫病爆发收成状况持续时间 | multiplicative | percent, bad |  |
| state_harvest_condition_disease_outbreak_impact_mult | 疫病爆发收成状况影响 | multiplicative | percent, bad |  |
| state_harvest_condition_drought_duration_mult | 干旱收成状况持续时间 | multiplicative | percent, bad |  |
| state_harvest_condition_drought_impact_mult | 干旱收成状况影响 | multiplicative | percent, bad |  |
| state_harvest_condition_earthquake_duration_mult | 地震收成状况持续时间 | multiplicative | percent, bad |  |
| state_harvest_condition_earthquake_impact_mult | 地震收成状况影响 | multiplicative | percent, bad |  |
| state_harvest_condition_extreme_winds_duration_mult | 极端大风收成状况持续时间 | multiplicative | percent, bad |  |
| state_harvest_condition_extreme_winds_impact_mult | 极端大风收成状况影响 | multiplicative | percent, bad |  |
| state_harvest_condition_flood_duration_mult | 洪水收成状况持续时间 | multiplicative | percent, bad |  |
| state_harvest_condition_flood_impact_mult | 洪水收成状况影响 | multiplicative | percent, bad |  |
| state_harvest_condition_heatwave_duration_mult | 热浪收成状况持续时间 | multiplicative | percent, bad |  |
| state_harvest_condition_heatwave_impact_mult | 热浪收成状况影响 | multiplicative | percent, bad |  |
| state_harvest_condition_tsunami_duration_mult | 海啸收成状况持续时间 | multiplicative | percent, bad |  |
| state_harvest_condition_tsunami_impact_mult | 海啸收成状况影响 | multiplicative | percent, bad |  |
| state_harvest_condition_wildfire_duration_mult | 野火收成状况持续时间 | multiplicative | percent, bad |  |
| state_harvest_condition_wildfire_impact_mult | 野火收成状况影响 | multiplicative | percent, bad |  |
| state_import_advantage_mult | 进口贸易优势 | multiplicative | percent, good |  |
| state_incorporation_speed_mult | 整合速度 | multiplicative | percent, good |  |
| state_infrastructure_add | 基础设施 | additive | good |  |
| state_infrastructure_from_automobiles_consumption_add | 人口汽车消费带来的基础设施 | additive | good |  |
| state_infrastructure_from_population_add | 每 100.0K 人口的设施 | additive | good |  |
| state_infrastructure_from_population_max_add | 人口带来的最大基础设施 | additive | good |  |
| state_infrastructure_from_population_max_mult | 人口带来的最大基础设施 | multiplicative | percent, good |  |
| state_infrastructure_from_population_mult | 每 100.0K 人口的设施 | multiplicative | percent, good |  |
| state_infrastructure_mult | 基础设施 | multiplicative | percent, good |  |
| state_institution_impact_add | 机构的影响 | additive | percent, good |  |
| state_laborers_investment_pool_contribution_add | 劳工投资池贡献 | additive | percent, good |  |
| state_laborers_investment_pool_efficiency_mult | 劳工投资池贡献效率 | multiplicative | percent, good |  |
| state_laborers_mortality_mult | 劳工的死亡率 | multiplicative | percent, bad |  |
| state_literacy_growth_add | 识字率增长 | additive | percent, good |  |
| state_lower_strata_expected_sol_add | 下层阶级的最低预期生活水平 | additive | neutral |  |
| state_loyalism_increases_cultural_erasure_mult | 文化抹除状态下的忠诚度增长 | multiplicative | percent, good |  |
| state_loyalism_increases_full_acceptance_mult | 完全接纳状态下的忠诚度增长 | multiplicative | percent, good |  |
| state_loyalism_increases_open_prejudice_mult | 公开偏见状态下的忠诚度增长 | multiplicative | percent, good |  |
| state_loyalism_increases_second_rate_citizen_mult | 二等公民状态下的忠诚度增长 | multiplicative | percent, good |  |
| state_loyalism_increases_violent_hostility_mult | 暴力敌视状态下的忠诚度增长 | multiplicative | percent, good |  |
| state_loyalists_from_political_movements_mult | 来自政治运动的忠诚派 | multiplicative | percent, good |  |
| state_machinists_investment_pool_contribution_add | 机械师投资池贡献 | additive | percent, good |  |
| state_machinists_investment_pool_efficiency_mult | 机械师投资池贡献效率 | multiplicative | percent, good |  |
| state_machinists_mortality_mult | 机械师死亡率 | multiplicative | percent, bad |  |
| state_market_access_price_impact | 市场接入价格影响 |  | percent, neutral |  |
| state_max_trade_advantage_from_capacity_add | 容量带来的最大贸易优势 | additive | percent, good |  |
| state_middle_strata_expected_sol_add | 中等阶层最低预期生活水平 | additive | neutral |  |
| state_migration_pull_add | 迁移吸引力 | additive | good |  |
| state_migration_pull_mult | 迁移吸引力 | multiplicative | percent, good |  |
| state_migration_pull_unincorporated_mult | 未合并州的迁移吸引力 | multiplicative | percent, good |  |
| state_migration_quota_mult | 迁移配额 | multiplicative | percent, neutral |  |
| state_minimum_incorporated_subsistence_arable_land_add | 已合并州的最低自给土地份额 | additive | percent, neutral |  |
| state_mortality_mult | 死亡率 | multiplicative | percent, bad |  |
| state_mortality_turmoil_mult | 每点动荡的死亡率 | multiplicative | percent, bad |  |
| state_mortality_wealth_mult | 每点财富的死亡率 | multiplicative | percent, bad |  |
| state_non_contiguous_incorporation_speed_mult | 非接壤合并速度 | multiplicative | percent, good |  |
| state_non_homeland_colony_growth_speed_mult | 非本土州的殖民地增长速度 | multiplicative | percent, good |  |
| state_non_homeland_mortality_mult | 非本土州的死亡率 | multiplicative | percent, bad |  |
| state_officers_investment_pool_contribution_add | 军官投资池贡献 | additive | percent, good |  |
| state_officers_investment_pool_efficiency_mult | 军官投资池贡献效率 | multiplicative | percent, good |  |
| state_peasants_consumption_multiplier_add | 农民的物品消费 | additive | percent, bad |  |
| state_peasants_education_access_add | 农民的教育接入 | additive | percent, good |  |
| state_peasants_internal_migration_disallowed_bool | 禁止农民国内迁移 | boolean | bad |  |
| state_peasants_mass_migration_disallowed_bool | 禁止农民大规模迁移 | boolean | bad |  |
| state_peasants_mortality_mult | 农民死亡率 | multiplicative | percent, bad |  |
| state_political_strength_from_wealth_mult | 财富带来的政治力量 | multiplicative | percent, neutral |  |
| state_political_strength_from_welfare_mult | 领取福利时的政治力量 | multiplicative | percent, neutral |  |
| state_pollution_generation_add | 产生的污染 | additive | bad |  |
| state_pollution_reduction_health_mult | 污染健康影响削减 | multiplicative | percent, bad |  |
| state_pop_pol_str_add | 全体人口政治力量 | additive | neutral |  |
| state_pop_pol_str_mult | 全体人口政治力量 | multiplicative | percent, neutral |  |
| state_pop_qualifications_mult | 资质 | multiplicative | percent, good |  |
| state_pop_support_movement_anarchist_add | 无政府主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_anarchist_mult | 无政府主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_anti_slavery_add | 废奴主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_anti_slavery_mult | 废奴主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_bonapartist_add | 波拿巴主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_bonapartist_mult | 波拿巴主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_carlist_add | 卡洛斯主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_carlist_mult | 卡洛斯主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_communist_add | 共产主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_communist_mult | 共产主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_corporatist_add | 社团主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_corporatist_mult | 社团主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_cultural_majority_add | 文化多数派运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_cultural_majority_mult | 文化多数派运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_cultural_minority_add | 文化少数派运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_cultural_minority_mult | 文化少数派运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_fascist_add | 法西斯主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_fascist_mult | 法西斯主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_feminist_add | 女权主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_feminist_mult | 女权主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_german_national_add | 德意志民族主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_german_national_mult | 德意志民族主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_india_pan_national_add | 印度泛民族主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_india_pan_national_mult | 印度泛民族主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_italian_national_add | 意大利民族主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_italian_national_mult | 意大利民族主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_labor_add | 劳工运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_labor_mult | 劳工运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_land_reform_add | 农民运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_land_reform_mult | 农民运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_legitimist_add | 正统主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_legitimist_mult | 正统主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_liberal_add | 自由主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_liberal_mult | 自由主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_miguelist_add | 米格尔主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_miguelist_mult | 米格尔主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_modernizer_add | 现代化运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_modernizer_mult | 现代化运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_nihilist_add | 虚无主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_nihilist_mult | 虚无主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_orleanist_add | 奥尔良主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_orleanist_mult | 奥尔良主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_positivist_add | 实证主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_positivist_mult | 实证主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_pro_slavery_add | 拥奴主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_pro_slavery_mult | 拥奴主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_radical_add | 激进主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_radical_mult | 激进主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_reactionary_add | 反动主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_reactionary_mult | 反动主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_religious_majority_add | 宗教多数派运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_religious_majority_mult | 宗教多数派运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_religious_minority_add | 宗教少数派运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_religious_minority_mult | 宗教少数派运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_royalist_absolutist_add | 绝对君主主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_royalist_absolutist_mult | 绝对君主主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_royalist_constitutional_add | 君主立宪主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_royalist_constitutional_mult | 君主立宪主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_slave_revolt_add | 奴隶起义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_slave_revolt_mult | 奴隶起义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_socialist_add | 社会主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_socialist_mult | 社会主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_utilitarian_add | 功利主义运动人口吸引力 | additive | neutral |  |
| state_pop_support_movement_utilitarian_mult | 功利主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_pop_support_movement_yugoslav_national_add | state_pop_support_movement_yugoslav_national_add | additive | neutral |  |
| state_pop_support_movement_yugoslav_national_mult | 德意志民族主义运动人口吸引力 | multiplicative | percent, neutral |  |
| state_radicalism_increases_cultural_erasure_mult | 文化抹除状态下的激进派增长 | multiplicative | percent, bad |  |
| state_radicalism_increases_full_acceptance_mult | 完全接纳状态下的激进派增长 | multiplicative | percent, bad |  |
| state_radicalism_increases_open_prejudice_mult | 公开偏见状态下的激进派增长 | multiplicative | percent, bad |  |
| state_radicalism_increases_second_rate_citizen_mult | 二等公民状态下的激进派增长 | multiplicative | percent, bad |  |
| state_radicalism_increases_violent_hostility_mult | 暴力敌视状态下的激进派增长 | multiplicative | percent, bad |  |
| state_radicals_and_loyalists_from_sol_change_mult | 生活水平变化产生的激进派与忠诚派 | multiplicative | percent, neutral |  |
| state_radicals_from_political_movements_mult | 政治运动产生的激进派 | multiplicative | percent, bad |  |
| state_sell_orders_ammunition_add | 弹药卖出订单 | additive | neutral |  |
| state_sell_orders_artillery_add | 火炮卖出订单 | additive | neutral |  |
| state_sell_orders_grain_add | 谷物卖出订单 | additive | neutral |  |
| state_sell_orders_small_arms_add | 轻武器卖出订单 | additive | neutral |  |
| state_shopkeepers_investment_pool_contribution_add | 店主投资池贡献 | additive | percent, good |  |
| state_shopkeepers_investment_pool_efficiency_mult | 店主投资池贡献效率 | multiplicative | percent, good |  |
| state_slave_import_mult | 奴隶输入 | multiplicative | percent, good |  |
| state_slaves_mortality_mult | 奴隶死亡率 | multiplicative | percent, bad |  |
| state_soldiers_investment_pool_contribution_add | 军人投资池贡献 | additive | percent, good |  |
| state_soldiers_investment_pool_efficiency_mult | 军人投资池贡献效率 | multiplicative | percent, good |  |
| state_soldiers_mortality_mult | 军人死亡率 | multiplicative | percent, bad |  |
| state_standard_of_living_add | 生活水平 | additive | good |  |
| state_subvention_export_add | 最大出口补贴 | additive | percent, neutral |  |
| state_subvention_import_add | 最大进口补贴 | additive | percent, neutral |  |
| state_tariff_export_add | 最大出口关税 | additive | percent, neutral |  |
| state_tariff_import_add | 最大进口关税 | additive | percent, neutral |  |
| state_tax_capacity_add | 税收能力 | additive | good |  |
| state_tax_capacity_mult | 税收能力 | multiplicative | percent, good |  |
| state_tax_collection_mult | 税收征收 | multiplicative | percent, neutral |  |
| state_tax_waste_add | 税收损耗 | additive | percent, bad |  |
| state_trade_advantage_from_capacity_add | 容量带来的贸易优势 | additive | percent, good |  |
| state_trade_advantage_mult | 贸易优势 | multiplicative | percent, good |  |
| state_trade_advantage_same_religion_add | 与同宗教者的贸易优势 | additive | good |  |
| state_trade_capacity_add | 贸易容量 | additive | good |  |
| state_trade_capacity_mult | 贸易容量 | multiplicative | percent, good |  |
| state_trade_center_max_limit_add | 贸易中心最大等级 | additive | good |  |
| state_trade_quantity_mult | 贸易数量 | multiplicative | percent, good |  |
| state_turmoil_effects_mult | 动荡带来的州惩罚 | multiplicative | percent, bad |  |
| state_unincorporated_starting_wages_mult | 未合并州的初始工资 | multiplicative | percent, neutral |  |
| state_upper_strata_expected_sol_add | 上等阶层最低预期生活水平 | additive | neutral |  |
| state_urbanization_per_level_add | 每个城镇中心的城市化 | additive | neutral |  |
| state_urbanization_per_level_mult | 每个城镇中心的城市化 | multiplicative | percent, bad |  |
| state_weekly_trades_add | 每周贸易次数 | additive | good |  |
| state_welfare_payments_add | 福利支出 | additive | percent, neutral |  |
| state_welfare_payments_mult | 福利支出倍数 | multiplicative | percent, neutral |  |
| state_working_adult_ratio_add | 劳动力比例 | additive | percent, good |  |

### 州 GUI 脚本

主条目：
GUI 脚本
| 函数 | 参数 | 输出 | 描述 |
|---|---|---|---|
| AbandonColony |  | Command |  |
| AccessAllBuiltRuralBuildings |  | Unknown | 类别：const |
| AccessBuilding | BuildingType | Building | 类别：const |
| AccessBuildings |  | Unknown | 类别：const |
| AccessCappedRuralBuildings |  | Unknown | 类别：const |
| AccessDecrees |  | Unknown | 类别：const |
| AccessDevelopmentBuildings |  | Unknown | 类别：const |
| AccessMarket |  | Market | 类别：const |
| AccessModifier |  | Modifier | 类别：const |
| AccessOwner |  | Country | 类别：const |
| AccessPopCultures |  | Unknown | 类别：const |
| AccessPopInterestGroups |  | Unknown | 类别：const |
| AccessPopReligions |  | Unknown | 类别：const |
| AccessPopTypes |  | Unknown | 类别：const |
| AccessPopsList |  | PopList | 类别：const |
| AccessSelf |  | State | 类别：const |
| AccessShippingLanesFromThisState | Province | Unknown | 类别：const |
| AccessShippingLanesOnlyGoodsTransferFromThisState | Province | Unknown | 类别：const |
| AccessShippingLanesOnlyPortConnectionsFromThisState | Province | Unknown | 类别：const |
| AccessShippingLanesOnlySupplyRoutesFromThisState | Province | Unknown | 类别：const |
| AccessSubsistenceBuilding |  | Building | 类别：const |
| AccessUncappedRuralBuildings |  | Unknown | 类别：const |
| AccessUrbanBuildings |  | Unknown | 类别：const |
| CalcPopInstitutionBureaucracyCost |  | CFixedPoint |  |
| CalcSupplyToDemandRatio | Goods | CFixedPoint |  |
| CalcTaxCapacity |  | CFixedPoint |  |
| CalcTaxCapacityBalance |  | CFixedPoint |  |
| CalcTaxCapacityUsage |  | CFixedPoint |  |
| CalcTurmoil |  | CFixedPoint |  |
| GetAdditionalSOLFactorsDescAll |  | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescMiddle |  | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescPoor |  | CString | 类别：nonconst |
| GetAdditionalSOLFactorsDescRich |  | CString | 类别：nonconst |
| GetAnnualPopNetMigration |  | int64 | 类别：nonconst |
| GetArableLandCapacity |  | int32 | 类别：nonconst |
| GetAverageAnnualWage |  | CFixedPoint | 类别：nonconst |
| GetAverageAnnualWageDesc |  | CString | 类别：nonconst |
| GetAverageStandardOfLivingAll |  | CFixedPoint | 类别：nonconst |
| GetAverageStandardOfLivingMiddle |  | CFixedPoint | 类别：nonconst |
| GetAverageStandardOfLivingPoor |  | CFixedPoint | 类别：nonconst |
| GetAverageStandardOfLivingRich |  | CFixedPoint | 类别：nonconst |
| GetBaseBureaucracyCostRaw |  | CFixedPoint | 类别：nonconst |
| GetBasePopBureaucracyCostRaw |  | CFixedPoint | 类别：nonconst |
| GetBestTexture |  | Unknown | 类别：nonconst |
| GetBestTextureEffect |  | CString | 类别：nonconst |
| GetBlockadeEffectsDesc |  | CString | 类别：nonconst |
| GetBlockadeLevel |  | CFixedPoint | 类别：nonconst |
| GetBuilding | BuildingType | Building | 类别：nonconst |
| GetBuildingsWithGovernmentExpenses |  | Unknown | 类别：nonconst |
| GetBuildingsWithTaxationRevenue |  | Unknown | 类别：nonconst |
| GetBureaucracyCost |  | CFixedPoint | 类别：nonconst |
| GetBureaucracyCostDesc |  | CString | 类别：nonconst |
| GetCapitalEffectsDesc |  | CString | 类别：nonconst |
| GetCityHubName |  | CString | 类别：nonconst |
| GetClaimsDesc |  | CString | 类别：nonconst |
| GetColonizers | CString | CString | 类别：nonconst |
| GetColonyCompany |  | Company | 类别：nonconst |
| GetColonyGrowthDateDesc |  | CString | 类别：nonconst |
| GetColonyGrowthModifierDesc |  | CString | 类别：nonconst |
| GetColonyProgress |  | CFixedPoint | 类别：nonconst |
| GetColonyProgressAsDays |  | int32 | 类别：nonconst |
| GetColonyProgressAsFloat |  | float | 类别：nonconst |
| GetColonyProvinceProgressDesc |  | CString | 类别：nonconst |
| GetColonyTransferName |  | CString | 类别：nonconst |
| GetColor |  | CVector4f | 类别：nonconst |
| GetConscriptionLimit |  | int32 | 类别：nonconst |
| GetConscriptionLimitDesc |  | CString | 类别：nonconst |
| GetConstructionEfficiency |  | CFixedPoint | 类别：nonconst |
| GetConstructionEfficiencyForBuildingType | BuildingType | CFixedPoint | 类别：nonconst |
| GetConstructionEfficiencyForBuildingTypeTooltip | BuildingType | CString | 类别：nonconst |
| GetConstructionEfficiencyTooltip |  | CString | 类别：nonconst |
| GetController |  | Country | 类别：nonconst |
| GetCountry |  | Country | 类别：nonconst |
| GetCulturalCommunities |  | Unknown | 类别：nonconst |
| GetCurrentBlockadeStrength |  | CFixedPoint | 类别：nonconst |
| GetCustom | CustomLocalization | CString | 类别：nonconst |
| GetDailyColonyProgress |  | CFixedPoint | 类别：nonconst |
| GetDevastationDailyChange |  | CFixedPoint | 类别：nonconst |
| GetDevastationDailyChangeBreakdown |  | CString | 类别：nonconst |
| GetDevastationEffects |  | CString | 类别：nonconst |
| GetDevastationLevel |  | CFixedPoint | 类别：nonconst |
| GetEnemyWithHighestOccupation |  | Country | 类别：nonconst |
| GetExpectedSOLFactorsDescAll |  | CString | 类别：nonconst |
| GetExpectedSOLFactorsDescMiddle |  | CString | 类别：nonconst |
| GetExpectedSOLFactorsDescPoor |  | CString | 类别：nonconst |
| GetExpectedSOLFactorsDescRich |  | CString | 类别：nonconst |
| GetExpectedStandardOfLivingAll |  | CFixedPoint | 类别：nonconst |
| GetExpectedStandardOfLivingMiddle |  | CFixedPoint | 类别：nonconst |
| GetExpectedStandardOfLivingPoor |  | CFixedPoint | 类别：nonconst |
| GetExpectedStandardOfLivingRich |  | CFixedPoint | 类别：nonconst |
| GetExportRevenue | Goods | CFixedPoint | 类别：nonconst |
| GetExportedAmount | Goods | CFixedPoint | 类别：nonconst |
| GetExports |  | Unknown | 类别：nonconst |
| GetFamineDesc |  | CString | 类别：nonconst |
| GetFarmHubName |  | CString | 类别：nonconst |
| GetForestryHubName |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingAll |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingLabelAll |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingLabelMiddle |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingLabelPoor |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingLabelRich |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingMiddle |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingPoor |  | CString | 类别：nonconst |
| GetFormattedStandardOfLivingRich |  | CString | 类别：nonconst |
| GetFreeArableLandAfterInactiveQueuedEntry |  | CString | 类别：nonconst |
| GetGDPContribution |  | CFixedPoint | 类别：nonconst |
| GetGDPContributionPercentage |  | CFixedPoint | 类别：nonconst |
| GetGDPGoodsContribution | Unknown | CFixedPoint | 类别：nonconst |
| GetGDPGoodsContributionBreakdown |  | CString | 类别：nonconst |
| GetGDPGoodsContributionPercentage | Unknown | CFixedPoint | 类别：nonconst |
| GetGdpRatioOwnedBy | Unknown | CFixedPoint | 类别：nonconst |
| GetGdpRatioOwnedByDesc | Country | CString | 类别：nonconst |
| GetGoodsSortedByGDP |  | Unknown | 类别：nonconst |
| GetGovernmentExpenses |  | CFixedPoint | 类别：nonconst |
| GetHarvestConditions |  | Unknown | 类别：nonconst |
| GetHomelandsDesc |  | CString | 类别：nonconst |
| GetID |  | int32 | 类别：nonconst |
| GetIDString |  | CString | 类别：nonconst |
| GetImportRevenue | Goods | CFixedPoint | 类别：nonconst |
| GetImportedAmount | Goods | CFixedPoint | 类别：nonconst |
| GetImports |  | Unknown | 类别：nonconst |
| GetIncorporationPartialEffectsDesc |  | CString | 类别：nonconst |
| GetIncorporationProgress |  | CFixedPoint | 类别：nonconst |
| GetIncorporationTimeDesc |  | CString | 类别：nonconst |
| GetIncorporationTimeLeft |  | CString | 类别：nonconst |
| GetInfrastructure |  | CFixedPoint | 类别：nonconst |
| GetInfrastructureBalance |  | CFixedPoint | 类别：nonconst |
| GetInfrastructureDesc |  | CString | 类别：nonconst |
| GetInfrastructureUsage |  | CFixedPoint | 类别：nonconst |
| GetInfrastructureUsageDesc |  | CString | 类别：nonconst |
| GetInsufficientQualificationsForAvailablePositionsDesc |  | CString | 类别：nonconst |
| GetInvasions |  | Unknown | 类别：nonconst |
| GetJobseekersDesc |  | CString | 类别：nonconst |
| GetLiteracy |  | CFixedPoint | 类别：nonconst |
| GetMarket |  | Market | 类别：nonconst |
| GetMarketAccess |  | CFixedPoint | 类别：nonconst |
| GetMarketAccessDesc |  | CString | 类别：nonconst |
| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| GetMarketAccessStatus |  | CString | 类别：nonconst |
| GetMarketCapitalEffectsDesc |  | CString | 类别：nonconst |
| GetMassMigrationCulture |  | Culture | 类别：nonconst |
| GetMassMigrationEndDate |  | CString | 类别：nonconst |
| GetMassMigrationOriginCountry |  | Country | 类别：nonconst |
| GetMaxBattalions |  | int32 | 类别：nonconst |
| GetMaxImbalance |  | CFixedPoint | 类别：nonconst |
| GetMaxImbalanceScaledByBasePrice |  | CFixedPoint | 类别：nonconst |
| GetMaxPotentialFor | Building | int32 | 类别：nonconst |
| GetMigrationAndSlaveTradeDetailsDesc |  | CString | 类别：nonconst |
| GetMigrationDesc |  | CString | 类别：nonconst |
| GetMigrationDetailsDesc |  | CString | 类别：nonconst |
| GetMigrationLabel |  | CString | 类别：nonconst |
| GetMigrationPull |  | CFixedPoint | 类别：nonconst |
| GetMigrationPullDesc |  | CString | 类别：nonconst |
| GetMineHubName |  | CString | 类别：nonconst |
| GetModifier |  | Modifier | 类别：nonconst |
| GetName |  | CString | 类别：nonconst |
| GetNameNoFormatting |  | CString | 类别：nonconst |
| GetNameWithCountryFlag |  | CString | 类别：nonconst |
| GetNextColonyProvince |  | Province | 类别：nonconst |
| GetNonPotentialDiploPlays |  | Unknown | 类别：nonconst |
| GetNumArableLandReservedForSubsistence |  | int32 | 类别：nonconst |
| GetNumBaseFreeArableLand |  | int32 | 类别：nonconst |
| GetNumBuildingsAffectedByGoodsShortage |  | int32 | 类别：nonconst |
| GetNumColonizers |  | int32 | 类别：nonconst |
| GetNumConstructableUrbanBuildings |  | int32 | 类别：nonconst |
| GetNumConsumed | Goods | CFixedPoint | 类别：nonconst |
| GetNumFreeArableLand |  | int32 | 类别：nonconst |
| GetNumInactiveQueuedArableLandEntry |  | CString | 类别：nonconst |
| GetNumJobseekers |  | int64 | 类别：nonconst |
| GetNumLoyalists |  | int64 | 类别：nonconst |
| GetNumObstinanceSupporters |  | int64 | 类别：nonconst |
| GetNumOfObstinatePopsFromMovement | Unknown | int64 | 类别：nonconst |
| GetNumProduced | Goods | CFixedPoint | 类别：nonconst |
| GetNumProvinces |  | int32 | 类别：nonconst |
| GetNumRadicals |  | int64 | 类别：nonconst |
| GetNumSubsistenceWorkingAdults |  | int64 | 类别：nonconst |
| GetNumUnemployedWorkingAdults |  | int64 | 类别：nonconst |
| GetNumUsedArableLand |  | int32 | 类别：nonconst |
| GetNumUsedArableLandFullyBuilt |  | int32 | 类别：nonconst |
| GetNumUsedArableLandFullyBuiltEntry |  | CString | 类别：nonconst |
| GetNumUsedArableLandUnderConstruction |  | int32 | 类别：nonconst |
| GetNumUsedArableLandUnderConstructionEntry |  | CString | 类别：nonconst |
| GetNumberOfPopsMiddle |  | int64 | 类别：nonconst |
| GetNumberOfPopsPoor |  | int64 | 类别：nonconst |
| GetNumberOfPopsRich |  | int64 | 类别：nonconst |
| GetObstinance |  | CFixedPoint | 类别：nonconst |
| GetObstinanceDesc |  | CString | 类别：nonconst |
| GetObstinanceEffectScale |  | CFixedPoint | 类别：nonconst |
| GetObstinanceEffectsDesc |  | CString | 类别：nonconst |
| GetObstinanceFromMovement | Unknown | CFixedPoint | 类别：nonconst |
| GetOccupant |  | Country | 类别：nonconst |
| GetOccupantsTooltip |  | CString | 类别：nonconst |
| GetOccupationPiechartData |  | Unknown | 类别：nonconst |
| GetOwner |  | Country | 类别：nonconst |
| GetPlanInvasionDesc |  | CString | 类别：nonconst |
| GetPolStrForCulture | Culture | int64 | 类别：nonconst |
| GetPolStrForReligion | Religion | int64 | 类别：nonconst |
| GetPollutionGeneration |  | CFixedPoint | 类别：nonconst |
| GetPollutionGenerationDesc |  | CString | 类别：nonconst |
| GetPollutionHealthEffectsReduction |  | CFixedPoint | 类别：nonconst |
| GetPollutionHealthEffectsReductionDesc |  | CString | 类别：nonconst |
| GetPopBirthrate |  | CFixedPoint | 类别：nonconst |
| GetPopCultureDesc |  | CString | 类别：nonconst |
| GetPopCultureDescByIndex | Unknown | CString | 类别：nonconst |
| GetPopGrowthDesc |  | CString | 类别：nonconst |
| GetPopMortality |  | CFixedPoint | 类别：nonconst |
| GetPopNetGrowth |  | int64 | 类别：nonconst |
| GetPopReligionDesc |  | CString | 类别：nonconst |
| GetPopReligionDescByIndex | Unknown | CString | 类别：nonconst |
| GetPopTotalChange |  | int64 | 类别：nonconst |
| GetPops |  | Unknown | 类别：nonconst |
| GetPopulationForCulture | Culture | int64 | 类别：nonconst |
| GetPopulationForReligion | Religion | int64 | 类别：nonconst |
| GetPopulationRatioBelowExpectedStandardOfLiving |  | CFixedPoint | 类别：nonconst |
| GetPopulationSize |  | int64 | 类别：nonconst |
| GetPortHubName |  | CString | 类别：nonconst |
| GetPotentialDecrees |  | Unknown | 类别：nonconst |
| GetPotentialDiploPlays |  | Unknown | 类别：nonconst |
| GetPotentialLabor |  | int64 | 类别：nonconst |
| GetPotentialPopTypeQualificationsDesc |  | CString | 类别：nonconst |
| GetPotentialProductionForCountry | Goods Country | CFixedPoint | 类别：nonconst |
| GetPotentialProductionForCountryDesc | Goods Country | CString | 类别：nonconst |
| GetPotentialQualifications | PopType | int64 | 类别：nonconst |
| GetPotentialQualificationsBreakdown | PopType | CString | 类别：nonconst |
| GetPotentialQualificationsDesc |  | CString | 类别：nonconst |
| GetPotentialUrbanBuildings |  | Unknown | 类别：nonconst |
| GetProductionInfo |  | Unknown | 类别：nonconst |
| GetRequiredBlockadeStrength |  | CFixedPoint | 类别：nonconst |
| GetSamplePops |  | Unknown | 类别：nonconst |
| GetSlaveExportMarkersDesc |  | CString | 类别：nonconst |
| GetSlaveImportMarkerDesc |  | CString | 类别：nonconst |
| GetSlaveTradeDetailsDesc |  | CString | 类别：nonconst |
| GetStateRegion |  | StateRegion | 类别：nonconst |
| GetSubsistenceBuilding |  | Building | 类别：nonconst |
| GetTaxCapacityDesc |  | CString | 类别：nonconst |
| GetTaxCapacityEffectsDesc |  | CString | 类别：nonconst |
| GetTaxCapacityUsageDesc |  | CString | 类别：nonconst |
| GetTaxationRevenue |  | CFixedPoint | 类别：nonconst |
| GetTheater | Unknown | Theater | 类别：nonconst |
| GetTimedModifiers |  | Unknown | 类别：nonconst |
| GetTimedModifiersBreakdown |  | CString | 类别：nonconst |
| GetTooltipTag |  | CString | 类别：nonconst |
| GetTotalConsumption |  | CFixedPoint | 类别：nonconst |
| GetTotalConvoysFromShippingLanesViaState | Province | int32 | 类别：nonconst |
| GetTotalExportRevenue |  | CFixedPoint | 类别：nonconst |
| GetTotalExportedAmount |  | CFixedPoint | 类别：nonconst |
| GetTotalImportRevenue |  | CFixedPoint | 类别：nonconst |
| GetTotalImportedAmount |  | CFixedPoint | 类别：nonconst |
| GetTotalLabor |  | int64 | 类别：nonconst |
| GetTotalPolStr |  | int64 | 类别：nonconst |
| GetTotalPortConnectionsViaState | Province | int32 | 类别：nonconst |
| GetTotalProduction |  | CFixedPoint | 类别：nonconst |
| GetTradeCapacity |  | int32 | 类别：nonconst |
| GetTradeCapacityBalance |  | int32 | 类别：nonconst |
| GetTradeCapacityDesc |  | CString | 类别：nonconst |
| GetTradeCapacityUsage |  | int32 | 类别：nonconst |
| GetTradeCapacityUsageDesc |  | CString | 类别：nonconst |
| GetTradePotential |  | CFixedPoint | 类别：nonconst |
| GetTradePotentialDesc |  | CString | 类别：nonconst |
| GetTurmoilEffects |  | CString | 类别：nonconst |
| GetUrbanization |  | int32 | 类别：nonconst |
| GetUrbanizationBuildingsMaxLevelDesc |  | CString | 类别：nonconst |
| GetUrbanizationDesc |  | CString | 类别：nonconst |
| GetUrbanizationNeededPerLevelFormatted |  | CString | 类别：nonconst |
| GetUrbanizationNeededPerLevelRaw |  | int32 | 类别：nonconst |
| GetWeeklyEmigration |  | int64 | 类别：nonconst |
| GetWeeklyImmigration |  | int64 | 类别：nonconst |
| GetWeeklyPopNetMigration |  | int64 | 类别：nonconst |
| GetWeeklySlaveExport |  | int64 | 类别：nonconst |
| GetWeeklySlaveImport |  | int64 | 类别：nonconst |
| GetWorldMarketAccess |  | CFixedPoint | 类别：nonconst |
| GetWorldMarketAccessDesc |  | CString | 类别：nonconst |
| GetWorldMarketAccessFormatted |  | CString | 类别：nonconst |
| GetYearlyGDP |  | CFixedPoint | 类别：nonconst |
| GetYearsToIncorporate |  | CFixedPoint | 类别：nonconst |
| HasAnyGoodsShortage |  | bool |  |
| HasBuildingGoodsShortage | Unknown | bool |  |
| HasClaims |  | bool |  |
| HasConstructionQueued |  | bool |  |
| HasDevastation |  | bool |  |
| HasDiscoverableResources |  | bool |  |
| HasFamine |  | bool |  |
| HasGoodsShortage | Unknown | bool |  |
| HasHomelands |  | bool |  |
| HasInsufficientQualificationsForAvailablePositions |  | bool |  |
| HasOccupation |  | bool |  |
| HasPopGoodsShortage | Unknown | bool |  |
| HasSlaveExportMarkers |  | bool |  |
| HasTimedModifiers |  | bool |  |
| HasTurmoilEffects |  | bool |  |
| IncorporateState |  | Command |  |
| IsBeingColonized |  | bool |  |
| IsBeingHighlighted |  | bool |  |
| IsBeingTutorialHighlighted |  | bool |  |
| IsCapitalState |  | bool |  |
| IsCoastal |  | bool |  |
| IsColonizationPaused |  | bool |  |
| IsColonyProgressBlockedByInactiveInterest |  | bool |  |
| IsCompanyColony |  | bool |  |
| IsContested |  | bool |  |
| IsEligibleForMassMigration |  | bool |  |
| IsFullyOccupied |  | bool |  |
| IsGrowingColony |  | bool |  |
| IsImportingSlaves |  | bool |  |
| IsIncorporated |  | bool |  |
| IsIncorporating |  | bool |  |
| IsIsolatedFromMarket |  | bool |  |
| IsMarketCapital |  | bool |  |
| IsMassMigrationTarget |  | bool |  |
| IsOwner | Country | bool |  |
| IsPinnedInOutliner |  | bool |  |
| IsSlaveState |  | bool |  |
| IsSplitState |  | bool |  |
| IsStrategicObjective | Country | bool |  |
| IsTreatyPort |  | bool |  |
| IsUnincorporated |  | bool |  |
| IsValid |  | bool |  |
| IsValidInvasionTarget |  | bool |  |
| IsWorldMarketHub |  | bool |  |
| IsZoomingToCapital |  | bool |  |
| MakeScope |  | Scope |  |
| PanCamera |  | void |  |
| PredictBureaucracyCost |  | CFixedPoint |  |
| Self |  | State |  |
| SortBuildings | Unknown | void |  |
| SortBuildingsWithOrder | Unknown Unknown | void |  |
| TogglePauseColonization |  | Command |  |
| TogglePinInOutliner |  | void |  |
| UnincorporateState |  | Command |  |
| ZoomExtraCloseToCapital |  | void |  |
| ZoomToCapital |  | void |  |

| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessLargestStateOwner |  | Country | 类别：const |
| AccessSelf |  | StateRegion | 类别：const |
| AccessStrategicRegion |  | StrategicRegion | 类别：const |
| AccessTraits |  | Unknown | 类别：const |
| Colonize |  | Command |  |
| GetAdjacentLandStateRegionsDesc |  | CString | 类别：nonconst |
| GetAdjacentSeaStateRegionsDesc |  | CString | 类别：nonconst |
| GetCityHubName |  | CString | 类别：nonconst |
| GetColonizeTooltip |  | CString | 类别：nonconst |
| GetCustom | CustomLocalization | CString | 类别：nonconst |
| GetFarmHubName |  | CString | 类别：nonconst |
| GetForestryHubName |  | CString | 类别：nonconst |
| GetID |  | int32 | 类别：nonconst |
| GetLargestStateInRegion |  | State | 类别：nonconst |
| GetLargestStateOwner |  | Country | 类别：nonconst |
| GetMineHubName |  | CString | 类别：nonconst |
| GetName |  | CString | 类别：nonconst |
| GetNameNoFormatting |  | CString | 类别：nonconst |
| GetNavalExitStateRegionDesc |  | CString | 类别：nonconst |
| GetPollutionEffects |  | CString | 类别：nonconst |
| GetPollutionImpact |  | CFixedPoint | 类别：nonconst |
| GetPollutionImpactDailyChange |  | CFixedPoint | 类别：nonconst |
| GetPollutionImpactTargetLevel |  | CFixedPoint | 类别：nonconst |
| GetPollutionLevel |  | CFixedPoint | 类别：nonconst |
| GetPortHubName |  | CString | 类别：nonconst |
| GetSeaInfrastructure | Country | CFixedPoint | 类别：nonconst |
| GetSeaInfrastructureDesc | Country | CString | 类别：nonconst |
| GetStatesDesc |  | CString | 类别：nonconst |
| GetStrategicRegion |  | StrategicRegion | 类别：nonconst |
| GetTooltipTag |  | CString | 类别：nonconst |
| IsSplitState |  | bool |  |
| IsValid |  | bool |  |
| MakeScope |  | Scope |  |
| PanCamera |  | void |  |
| Self |  | StateRegion |  |

| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessSelf |  | StateTrait | 类别：const |
| GetCustom | CustomLocalization | CString | 类别：nonconst |
| GetModifiersDesc |  | CString | 类别：nonconst |
| GetName |  | CString | 类别：nonconst |
| GetTexture |  | Unknown | 类别：nonconst |
| GetTooltipTag |  | CString | 类别：nonconst |
| GetUnlocks |  | CString | 类别：nonconst |
| MakeScope |  | Scope |  |
| Self |  | StateTrait |  |

| Promote | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessBuilding | BuildingType | Building | 类别：const |
| AccessMarket |  | Market | 类别：const |
| AccessModifier |  | Modifier | 类别：const |
| AccessOwner |  | Country | 类别：const |
| AccessPopsList |  | PopList | 类别：const |
| AccessStateRegion |  | StateRegion | 类别：const |
| AccessSubsistenceBuilding |  | Building | 类别：const |
| GetBuilding | BuildingType | Building | 类别：nonconst |
| GetColonyCompany |  | Company | 类别：nonconst |
| GetController |  | Country | 类别：nonconst |
| GetCountry |  | Country | 类别：nonconst |
| GetEnemyWithHighestOccupation |  | Country | 类别：nonconst |
| GetFoodSecurity |  | FoodSecurity | 类别：nonconst |
| GetMarket |  | Market | 类别：nonconst |
| GetMassMigrationCulture |  | Culture | 类别：nonconst |
| GetMassMigrationOriginCountry |  | Country | 类别：nonconst |
| GetModifier |  | Modifier | 类别：nonconst |
| GetNextColonyProvince |  | Province | 类别：nonconst |
| GetOccupant |  | Country | 类别：nonconst |
| GetOwner |  | Country | 类别：nonconst |
| GetStateRegion |  | StateRegion | 类别：nonconst |
| GetSubsistenceBuilding |  | Building | 类别：nonconst |
| GetTheater | Country | Theater | 类别：nonconst |
| MakeScope |  | Scope |  |

| Promote | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessLargestStateOwner |  | Country | 类别：const |
| AccessStrategicRegion |  | StrategicRegion | 类别：const |
| GetLargestStateInRegion |  | State | 类别：nonconst |
| GetLargestStateOwner |  | Country | 类别：nonconst |
| GetStrategicRegion |  | StrategicRegion | 类别：nonconst |
| MakeScope |  | Scope |  |

| Promote | 参数 | 输出 | 描述 |
|---|---|---|---|
| MakeScope |  | Scope |  |

## 战略区域（Strategic region）

[战略区域](Strategic region.md)是州区域的集合。它们是外交利益和军事总部（HQ）的基础。战略区域定义于 common/strategic_regions 中。

每个战略区域由一个唯一的脚本名称定义，该名称同时作为本地化键（localization key），此外还包括首都省份、百分比 RGB 地图颜色、州的列表，以及可选的图形文化（graphical culture）。

示例：

```
strategic_region_name = {
	capital_province = province_id	# The province ID for the capital of the state, determines where the UI panel for the interest markers present appears
	map_color = { R% G% B% }		# The percentage of R G B colour for this region for the diplomatic map mode
	states = { state_key_list }		# The states included in this strategic region specified by key
	graphical_culture = "script_name" # Defines which style is used for on-map building models, "European/Western" is the "default" style and left undefined
}
```

每个州只能被包含在一个战略区域中。海军州区域也被纳入战略区域，每个州区域对应一个。这些海军战略区域没有首都省份、地图颜色或图形文化。
海军战略区域示例：

```
region_baltic_sea = {
	states = { STATE_BALTIC_SEA }
}
```

### Effect、event target 与 trigger

以下是可在战略区域 scope 中使用的 effect、event target 与 trigger。

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| every_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成条件 | every_harvest_condition = { limit = { <triggers> } #optional <effects> } | harvest_condition |
| every_neighbouring_state | 遍历与当前 scope 相邻的所有州 注意英式拼写 | every_neighbouring_state = { limit = { <triggers> } #optional <effects> } | state |
| every_scope_country | 遍历在受支持的 scope（目前为：market、state_region、战略区域）中存在的所有国家 | every_scope_country = { limit = { <triggers> } #optional <effects> } | country |
| every_scope_interest_marker | 遍历以下对象中的所有利益标记：country、state_region、战略区域 | every_scope_interest_marker = { limit = { <triggers> } #optional <effects> } | interest_marker |
| every_scope_state | 遍历以下对象中包含省份的所有州：country、state_region、theater、front 或 strait | every_scope_state = { limit = { <triggers> } #optional <effects> } | state |
| ordered_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成条件 | ordered_harvest_condition = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | harvest_condition |
| ordered_neighbouring_state | 遍历与一个州区域相邻的所有州 | ordered_neighbouring_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| ordered_scope_country | 遍历在受支持的 scope（目前为：market、state_region、战略区域）中存在的所有国家 | ordered_scope_country = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | country |
| ordered_scope_interest_marker | 遍历以下对象中的所有利益标记：country、state_region、战略区域 | ordered_scope_interest_marker = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | interest_marker |
| ordered_scope_state | 遍历以下对象中包含省份的所有州：country、state_region、theater、front 或 strait | ordered_scope_state = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | state |
| random_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成条件 | random_harvest_condition = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | harvest_condition |
| random_neighbouring_state | 遍历与一个州区域相邻的所有州 | random_neighbouring_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |
| random_scope_country | 遍历在受支持的 scope（目前为：market、state_region、战略区域）中存在的所有国家 | random_scope_country = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | country |
| random_scope_interest_marker | 遍历以下对象中的所有利益标记：country、state_region、战略区域 | random_scope_interest_marker = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | interest_marker |
| random_scope_state | 遍历以下对象中包含省份的所有州：country、state_region、theater、front 或 strait | random_scope_state = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | state |

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| any_harvest_condition | 遍历影响一个州、州区域、战略区域或国家的所有收成条件 | any_harvest_condition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | harvest_condition |
| any_neighbouring_state | 遍历与一个州区域相邻的所有州 | any_neighbouring_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| any_scope_country | 遍历在受支持的 scope（目前为：market、战略区域）中存在的所有国家 | any_scope_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | country |
| any_scope_interest_marker | 遍历以下对象中的所有利益标记：country、战略区域 | any_scope_interest_marker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | interest_marker |
| any_scope_state | 遍历以下对象中包含省份的所有州：country、state_region、theater、front 或 strait | any_scope_state = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | state |
| check_area | 将对象的面积与另一对象进行比较 |  |  |
| has_diplomatic_play | 检查战略区域是否存在外交博弈 |  | boolean |

| Event target | 描述 | 目标 scope |
|---|---|---|
| ai_colonization_value | 转到目标国家 AI 殖民某战略区域的意愿（示例：value = ai_colonization_value:root） | value |

### 战略区域 GUI 脚本

主条目：
GUI 脚本
| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessFirstDiplomaticPlay |  | DiplomaticPlay | 类别：const |
| AccessSelf |  | StrategicRegion | 类别：const |
| GetConvoyRaidsDesc |  | CString | 类别：nonconst |
| GetCustom | CustomLocalization | CString | 类别：nonconst |
| GetFirstDiplomaticPlay |  | DiplomaticPlay | 类别：nonconst |
| GetIndex |  | uint32 | 类别：nonconst |
| GetInterest | Unknown | Interest | 类别：nonconst |
| GetInterests |  | Unknown | 类别：nonconst |
| GetLastConvoyRaidingCountriesToTargetDesc | Country | CString | 类别：nonconst |
| GetLastConvoyRaidingDamageBy | Country | int32 | 类别：nonconst |
| GetLastConvoyRaidingDamageEnemyReductionDesc | Country | CString | 类别：nonconst |
| GetLastConvoyRaidingDamageReductionDesc | Country | CString | 类别：nonconst |
| GetLastConvoyRaidingDamageTo | Country | int32 | 类别：nonconst |
| GetLastConvoyRaidingTargetCountriesByAttackerDesc | Country | CString | 类别：nonconst |
| GetName |  | CString | 类别：nonconst |
| GetNameNoFormatting |  | CString | 类别：nonconst |
| GetTooltipTag |  | CString | 类别：nonconst |
| GetTotalGDP |  | CFixedPoint | 类别：nonconst |
| HasDiplomaticPlay |  | bool |  |
| IsLand |  | bool |  |
| IsValid |  | bool |  |
| MakeScope |  | Scope |  |
| Self |  | StrategicRegion |  |

| Promote | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessFirstDiplomaticPlay |  | DiplomaticPlay | 类别：const |
| GetFirstDiplomaticPlay |  | DiplomaticPlay | 类别：nonconst |
| GetInterest | Unknown | Interest | 类别：nonconst |
| MakeScope |  | Scope |  |

## 参考资料

1. ↑ 基于 define `SPLIT_STATE_PRIME_LAND_WEIGHT`

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effect](Effect.md) • [Event target](Event target.md) • [Scope](Scope.md) • [Trigger](Trigger.md) [宏](Macro.md) • [Modifier 类型](Modifier types.md) • [On action](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [决议](Decision modding.md) • [事件](Event modding.md) • [历史](History modding.md) • [日志](Journal modding.md) • [Modifier](Modifier modding.md) • 目标 • [脚本化 GUI](Scripted gui.md) |
|---|---|

| 脚本类型 | [建筑](Building modding.md) • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • 州 |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图片](Event images.md) • [图形资源](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [声音](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [Mod](Mod.md) • [Mod 兼容性](Mod compatibility.md) • [Mod 结构](Mod structure.md) • [脚本化测试](Scripted test.md) • [疑难解答](Troubleshooting.md) |
|---|---|

| 指南 | [Mod 翻译](Mod translation.md) • [新国家 Mod 制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州 Mod 制作指南](State modding guide.md) |
|---|---|