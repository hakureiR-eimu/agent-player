---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Building modding
source: https://vic3.paradoxwikis.com/Building_modding
pageid: 5328
categories: [Potentially_outdated, 1.9, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。其中至少有一部分最后是针对 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.9 核实的。

建筑
**游戏文件夹 用于存储此类文件的文件夹。 ：** `folder/path/after_game`

---

**图标文件夹 原版游戏此类图标通常存放的文件夹。 ：** `gfx/interface/icons/building_icons`

---

**可注入（Injectable） 能否对此类型使用 INJECT 数据库函数？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **可替换（Replaceable） 能否对此类型使用 REPLACE 数据库函数？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**相关游戏对象：** 建筑组、生产方式组

[建筑](https://vic3.paradoxwikis.com/Buildings)是《维多利亚3》的基础支柱之一。因此，许多 mod 都会想为游戏添加新建筑。此外，[生产方式](Production method.md)对建筑的运作至关重要，因此本页还包含对如何修改生产方式的说明。

## 建筑组

建筑组
**游戏文件夹 用于存储此类文件的文件夹。 ：** `folder/path/after_game`

---

**可注入（Injectable） 能否对此类型使用 INJECT 数据库函数？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **可替换（Replaceable） 能否对此类型使用 REPLACE 数据库函数？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**相关游戏对象：** 建筑

每座建筑都属于某个*建筑组*（building group）。建筑组定义于 /Victoria 3/game/common/building_groups，遵循以下基本格式：

```
[building_group]= {
	category = [urban/rural/development]
	
	economy_of_scale = [yes/no]
	
	cash_reserves_max = [integer]
	
	should_auto_expand = { 
		[trigger]
	}
	
	economy_of_scale_ai_factor = [float]
}
```

每个建筑组都需要自己独有的脚本名；按照惯例写作 `bg_[script_name]`。建筑组还可以有父组（parent group），从父组继承特性，也可以覆盖父组特性。例如：

```
bg_manufacturing = {
	category = urban

	always_possible = yes
	
	economy_of_scale = yes
	
	cash_reserves_max = 25000
	
	should_auto_expand = { 
		default_auto_expand_rule = yes
	}
	
	economy_of_scale_ai_factor = 4.0
}

bg_light_industry = {
	parent_group = bg_manufacturing

	lens = light_industry
	
	urbanization = 20
	infrastructure_usage_per_level = 2
}
```

子组会继承父组的所有值，但也可以自行定义更多特性，并覆盖父组的特性。建筑本身则可以进一步覆盖甚至其所属类别的值。

| 特性 | 默认值 | 说明 | 原版组示例 |
|---|---|---|---|
| parent_group = [parent_group_key] | 未设置 | 该组被视为指定组的子组。 | 大多数 |
| category = urban/rural/development | 未设置 | 建筑出现在 UI 的哪个部分 | 顶层组 |
| always_possible = yes/no | no | 无论州内资源如何，该组中的建筑始终允许建造。 | 制造业、政府建筑 |
| economy_of_scale = yes/no | no | 该组中的非自给建筑每级获得一个规模经济吞吐量修正。 | 大多数 |
| is_subsistence = yes/no | no | 该组中的建筑被视为遵循特殊规则的自给建筑。 | 自给农场 |
| is_government_funded = yes/no | no | 该组中的建筑的开支由政府支付。 | 政府建筑、港口 |
| default_building = [building_type_key] | 未设置 | 指定默认建造的建筑类型，除非州另行指定。 | 大多数农村建筑 |
| lens = [lens_key] | 未设置 | 决定该组中的建筑归入哪个镜头（lens）分类。 | 所有建筑 |
| auto_place_buildings = yes/no | no | 该组中的建筑会自动创建 | 城市中心、金矿田、自给建筑 |
| capped_by_resources = yes/no | no | 该组中的建筑数量受州资源上限限制。参见：[资源上限与农场类型](Building modding.md) | 油井、捕鲸站、橡胶种植园、伐木营等资源建筑 |
| discoverable_resource = yes/no | no | 该组中的建筑使用州的可发现资源条目。参见：[资源上限与农场类型](Building modding.md) | 油井、橡胶、金矿田 |
| depletable_resource = yes/no | no | 该组中的建筑使用州的资源枯竭条目。参见：[资源上限与农场类型](Building modding.md) | 金矿田 |
| can_use_slaves = yes/no | no | 该组中的建筑可以“雇佣”奴隶 | 农业、矿业、建造业 |
| land_usage = urban/rural | 未设置 | 建筑使用哪种州资源：urban = 城市化，rural = 可耕地。 | 城市中心使用 urban，农业使用可耕地 |
| cash_reserves_max = [integer] | 0 | 该组中的建筑每级可存入现金储备的英镑（£）上限。若设为 0，则使用父组的值。 | 所有非政府建筑 |
| inheritable_construction = yes/no | no | 该建筑组的在建工程在州易手或分裂州合并时会保留 | 奇迹与运河 |
| stateregion_max_level = yes/no | no | 该组中任何具有 has_max_level 属性的建筑类型，其等级限制以州区域（state region）而非州为单位 | 公共基础设施 |
| urbanization = [integer] | 0 | 该组中的建筑每级提供的城市化数量 | 农村为 5，城市工业和行政为 20，矿山为 10，运河为 100 |
| should_auto_expand = [trigger] | 未设置 | 在开启自动扩张时，该组中的建筑应在何种条件下自动扩张（更具体的组或建筑类型上的 trigger 会覆盖此项）。只要此 trigger 有任何内容，游戏就会认为该建筑可能可以自动扩张，因此不要在这里写永远不可能为真的 trigger | 几乎所有建筑都使用 scripted trigger "default_auto_expand_rule = yes" |
| min/max_hiring_rate = [float] | define 值 NDefines::NEconomy::DEFAULT_MIN_HIRING_RATE/DEFAULT_MAX_HIRING_RATE | 建筑的编制在一周内可以雇佣的比例 | 所有权建筑使用 "hiring_rate = 1.0" |
| proportionality_limit = [float] | define 值 NDefines::NEconomy::EMPLOYMENT_PROPORTIONALITY_LIMIT | 建筑对人口类型比例失衡的容忍度有多高？ | 所有权建筑使用 "proportionality_limit = 1.0" |
| hires_unemployed_only = yes/no | no | 该组中的建筑只能从失业人口池中雇佣。 | 自给建筑 |
| fired_pops_become_radical = no | yes | 被解雇的人口（例如因降级）不会变成激进派。用于会自动降级的建筑，如自给农场。 | 征兵中心、自给建筑 |
| is_military = yes | no | 该组中的建筑被视为军事建筑 | 军事建筑 |
| subsidized = yes | no | 该组的建筑在游戏开始时默认获得补贴（在战役开始后无效果） | 私营基础设施 |
| ignores_productivity_when_hiring = yes | no | 用于自给农业和所有权建筑，即使没有生产力也允许雇佣 | 自给农业、所有权建筑 |
| economy_of_scale_ai_factor = 1.5 | 未设置 | 影响 AI 对在同一州集中建造该组建筑以获得高规模经济加成的重视程度 | 各类资源建筑为 2.0，其他为 1.5，政府为 5.0 |
| foreign_investment_ai_factor = 1.5 | 未设置 | 影响 AI 对在其他国家投资该组建筑的重视程度 | 资源建筑平均 1.0；其他平均 0.5 |

## 建筑

建筑定义于 /Victoria 3/game/common/buildings，遵循以下基本格式：

```
[building] = {
	building_group = [building_group]
	icon = [path]
	city_type = none
	levels_per_mesh = 5

	production_method_groups = {
		[production_method_groups]
	}

	required_construction = [int]
	
}
```

每座建筑都需要自己独有的脚本名；按照惯例写作 `building_[script_name]`。大多数建筑还有若干其他特性。

| 特性 | 默认值 | 说明 | 原版建筑示例 |
|---|---|---|---|
| building_group = [bg_key] | 未设置 | 引用建筑组，建筑组定义了同类建筑的共同属性 | 所有建筑 |
| icon = "path/to/texture" | 未设置 | 建筑图标 | 所有建筑 |
| buildable = yes/no | yes | 该建筑是否可以手动建造 | 金矿田、奇迹、城市中心等均为 "no" |
| expandable = yes/no | yes | 该建筑是否可以手动扩建 | 金矿田、奇迹、城市中心 |
| downsizeable = yes/no | yes | 该建筑是否可以手动缩减 | 金矿田、奇迹、城市中心 |
| unique = yes/no | no | 该建筑类型全世界只能建一级，且私人投资者永远不会建造 | 奇迹 |
| has_max_level = yes/no | no | 必须定义一个 modifier 来决定最大等级 | 港口、建造业、军事 |
| ignore_stateregion_max_level = yes | no | 如果建筑所属的组设有 stateregion_max_level = yes，则该建筑类型覆盖此项。用于港口，使分裂州的每个拥有者各自有独立的限额。 | 港口 |
| enable_air_connection = yes/no | no | 建造了该建筑的区域会被纳入空中旅行考虑。仅用于装饰性的齐柏林飞艇 | 摩天大楼 |
| port = yes/no | no | 该建筑可以连接不同的市场区域 | 港口 |
| unlocking_technologies = { [technology] } | 未设置 | 建造该建筑所需的（任意一项即可的）技术列表 | 合成材料厂，以及基本上所有建筑 |
| can_build_government = { [trigger] } | 未设置 | 政府建造要求的自定义 trigger（state 作用域） | 仅鸦片种植园（检查鸦片是否被禁止） |
| can_build_private = { [trigger] } | 未设置 | 私人投资者建造要求的自定义 trigger（state 作用域） | 仅鸦片种植园（检查鸦片是否被禁止） |
| construction_points = [int32] | 未设置 | 建造所需的建造点数。为便于引用，可使用 /Victoria 3/game/common/script_values/building_values.txt 中的预置变量名 | construction_cost_high、construction_cost_very_low、construction_cost_medium 等 |
| construction_modifier = { [modifier_definition] } | 未设置 | 以每周建造产出 / construction_points 的比例应用于建造营地。常用于添加额外建造消耗成本，在建造期间逐步消耗 | 未使用 |
| owners = [pop_type_key] | 未设置 | 分红与投资池，若未设置则由建筑组或生产方式决定 | 未使用 |
| ownership_type = no_ownership/self/other | 未设置 | 建筑所有权类型：no_ownership——不能拥有其他建筑，分红（若有）支付给国家；self——只能拥有自身，向拥有它的建筑支付分红；other——可以拥有其他建筑，只向自己的人口支付分红 | 大多数使用 self |
| economic_contribution = 0.0-1.0 | 1.0 | 该建筑税收/GDP 的乘数，0.0 表示不计入税收/GDP | 未使用 |
| min_raise_to_hire = [fixed_point] | define 值 NEconomy.MIN_RAISE_TO_HIRE | 员工转到该工作场所所需的最低涨薪幅度 | 自给农场 |
| naval = yes/no | no | 海军还是陆军，默认 no，仅适用于军事建筑，由建筑组决定 | 海军基地 |
| canal = [canal_type_key] | 未设置 | 引用运河类型，若设置则将该建筑标记为运河 | 运河 |
| ai_value = [script_value] | define 值 NAI.BUILDING_BASE_VALUE 或 NAI.GOVERNMENT_BUILDING_BASE_VALUE | AI 价值 | 工具工坊、铁路、金矿 |
| ai_subsidies_weight = [script_value] | 1.0 | AI 认为补贴该建筑的重要性 | 未使用 |
| slaves_role = [pop_type_key] | define 值 NPops.DEFAULT_POP_TYPE | 定义奴隶可以替代哪种职业。 | 自给农场（其他建筑在其类别中设置） |
| production_methods = { [production_method_groups] } | 未设置 | 该建筑拥有哪些生产方式组。参见[生产方式](Building modding.md)章节 | 所有建筑 |
| possible = { [trigger] } | 未设置 | 决定建筑是否可建造的条件。 | 渔港检查是否临海，工业检查是否未通过禁工业主义法律 |
| should_auto_expand = { [trigger] } | 未设置 | 在开启自动扩张时应自动扩张的条件（若存在则覆盖建筑组）。只要此 trigger 有任何内容，游戏就会认为该建筑可能可以自动扩张，因此不要在这里写永远不可能为真的 trigger。 | 政府行政、铁路 |
| city_type = none (city/farm/mine/port/wood) | none | 该建筑在图形上影响哪种类型的枢纽 | 所有建筑 |
| generates_residences = yes/no | yes | 该建筑是否为城市添加图形化的住宅 | 未使用 |
| terrain_manipulator = [terrain_manipulator_key] | 未设置 | 由建筑更新的图形地形操纵器 | 农场、林业、矿山、港口 |
| levels_per_mesh = [int32] | 未设置 | 需要多少级才会在地图上增加 1 座额外建筑，默认 1，大多数为 5 | 所有建筑 |
| residence_points_per_level = [int32] | 1 | 该建筑每级为其枢纽增加多少总“住宅点数”，用于决定生成的住宅建筑 | 城市中心和兵营为 0 |
| statue = yes | no | 用于强权集团雕像的特殊建筑类型 | 强权集团雕像 |
| meshes = { [meshes] } | 未设置 | 用于动态地形放置的网格（mesh）列表 | 未使用 |
| entity_not_constructed = { [meshes] } | 未设置 | 特殊建筑在未建造时可以显示一个实体 | 格林尼治天文台 |
| entity_under_construction = { [meshes] } | 未设置 | 覆盖特殊建筑在建时的实体 | 各类奇迹，如圣索菲亚大教堂 |
| entity_constructed = { [meshes] } | 未设置 | 覆盖特殊建筑建成后使用的实体 | 各类奇迹，如圣索菲亚大教堂 |
| locator = [locator_type] | 未设置 | 特殊建筑的定位器类型 | 每个奇迹和运河 |
| lens = [infrastructure] | 未设置 | 覆盖该建筑类型显示在哪个镜头中，否则由建筑组指定 | 贸易中心 |
| background = "path/to/texture" | 未设置 | 建筑注册表条目的背景纹理 |  |
| company_headquarter = yes | 未设置 | 建筑作为公司的总部运作 | 公司总部 |

### 资源上限与农场类型

受限建筑的数量通常基于[州区域定义](State modding.md)设限。例如：

```
STATE_CALIFORNIA = {
    id = 326
    subsistence_building = "building_subsistence_farm"
    provinces = { list of provinces }
    traits = { "state_trait_central_valley" "state_trait_northern_california_coastal_forests" }
    city = "x5EF8F5"
    port = "x1116AA"
    farm = "x7A5DA6"
    mine = "x4C2D30"
    wood = "x607BA8"
    arable_land = 300
    arable_resources = { "building_wheat_farm" "building_livestock_ranch" "building_cotton_plantation" "building_vineyard" }
    capped_resources = {
        building_iron_mine = 33
        building_sulfur_mine = 40
        building_logging_camp = 13
        building_fishing_wharf = 14
    }
    resource = {
        type = "building_gold_field"
        depleted_type = "building_gold_mine"
        undiscovered_amount = 12
    }
    resource = {
        type = "building_oil_rig"
        undiscovered_amount = 50
    }
    naval_exit_id = 3153
}
```

以下州区域特性与建筑相关：

| subsistence_building | 默认自给类型使用哪座建筑，必须是定义为自给建筑的建筑。 |
|---|---|
| arable_land | 设置该州可用的可耕地数量。所有 `land_usage = rural` 的建筑都使用并共享此上限。 |
| arable_resources | 可用该州可耕地建造的建筑列表。 |
| capped_resources | 每种类型可建造的建筑数量，用于建筑设有 `capped_by_resources = yes` 时。 |
| undiscovered_amount | 与另一类资源上限类似，但对玩家并非立即可见，需要科技和时间才能揭示。建筑需设有 `discoverable_resource = yes.` |
| discovered_amount | 类似 undiscovered_amount，但已被发现。基本上是指从游戏开始时该类型建筑可建造的数量，但适用于设有 `discoverable_resource = yes` 的建筑。 |
| depleted_type | 用于设有 `depletable_resource = yes` 的建筑。当该资源在此州枯竭时（基于 [Defines](Defines.md) 中定义的各种随机判定，或通过 `force_resource_depletion` effect），将初始类型的建筑替换并删除为第二类型，数量作为新的上限。 |
#### 发现与枯竭

资源发现与枯竭使用 [Defines](Defines.md) 中 [NEconomy](Defines.md) 下的数值。

| Define | 默认值 | 开发者注释 |
|---|---|---|
| BASE_RESOURCE_DISCOVER_CHANCE | 0.02 | # 每天（1.0 = 1%） |
| EMPLOYMENT_RESOURCE_DEPLETE_CHANCE | 0.005 | # 乘以该建筑满员运转的等级数 |
| RESOURCE_DISCOVER_MIN_FRACTION | 0.2 | # 每次成功判定时可被发现的资源最小比例 |
| RESOURCE_DISCOVER_MAX_FRACTION | 0.5 | # 每次成功判定时可被发现的资源最大比例 |
| FULLY_DISCOVERED_RESOURCE_DEPLETE_CHANCE_MULT | 1.0 | # 当资源已全部被发现时，资源枯竭概率乘以此值 |
| RESOURCE_DEPLETE_MIN_AMOUNT | 2 | # 每次成功判定时枯竭的资源最小数量 |
| RESOURCE_DEPLETE_MAX_AMOUNT | 5 | # 每次成功判定时枯竭的资源最大数量 |

虽然这些数值大多不言自明，但发现与枯竭的许多具体细节在游戏中仍然隐藏不露。以下是一些补充信息供参考，其中部分来自测试。[但还需要更多测试或信息]

一旦某国发现了允许建造使用 `discoverable_resource = yes` 的建筑的技术，游戏就会开始为该国每个仍留有“未发现建筑”的州进行该资源的发现判定。该判定每天进行一次，使用 `BASE_RESOURCE_DISCOVER_CHANCE` 的数值，默认为每个州每天 0.02% 的概率。若判定成功，剩余 `undiscovered_amount` 中 20% 到 50% 的资源将可供建造。此外，每个对该州宣布了利益的国家都会收到通知。

还有一些与发现相关的事件会使用命令 `force_resource_discovery`。例如，某国研究出抽油机（Pumpjacks）技术后，会自动在其中一个州免费且即时地发现石油。类似地，（相对常见的）橡胶事件会强制在你所在的州或相邻州发现橡胶。

如果建筑带有 `depletable_resource = yes`，游戏会在每个州对该建筑进行枯竭判定。基础概率为每天 0.005%，乘以每个满员运转的等级。因此，如果一个金矿场有 8 个等级且全部满员，该建筑每天就有 0.04% 的概率通过枯竭判定。若判定成功，该建筑 2-5 个等级上限将被移除，并替换为该资源 `depleted_type` 条目中相应建筑的同等等级。

## 生产方式

### 生产方式组

生产方式组
**游戏文件夹 存储该类型文件的文件夹。 ：** `folder/path/after_game`

---

**图标文件夹 原版游戏该类型图标通常存放的文件夹。 ：** `gfx/interface/icons/generic_icons`

---

**可注入 能否对该类型使用 INJECT 数据库函数？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **可替换 能否对该类型使用 REPLACE 数据库函数？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**相关游戏对象：** 建筑物，生产方式

生产方式组是某个建筑可使用的相互排斥的生产方式的集合，例如面包店、甜味剂、发酵粉。

生产方式组定义于 /Victoria 3/game/common/production_method_groups，遵循以下基本格式：

```
[production_method_group] = {
	texture = [path]
	production_methods = {
		[production_method]
	}
}
```

每个生产方式组都需要自己独一无二的脚本名称；按惯例为 `pmg_[script_name]`。一个组内可以有任意数量的生产方式，但同一时间只能激活一个。

| 特性 | 默认值 | 描述 |
|---|---|---|
| is_hidden_when_unavailable = yes/no | no | 当该组中的生产方式当前无法切换时，是否完全不可见。用于纪念建筑。 |
| ai_selection = most_productive | most_profitable | 影响 AI 如何在生产方式之间进行选择。当前选项：most_profitable、most_productive。most_productive 适用于政府行政或港口之类。 |
| texture = "path/to/texture" | unset | 当多个同类建筑拥有不同生产方式时（如混合自动化），在建筑标签页中显示的图标。 |

### 生产方式

生产方式
**游戏文件夹 存储该类型文件的文件夹。 ：** `folder/path/after_game`

---

**图标文件夹 原版游戏该类型图标通常存放的文件夹。 ：** `gfx/interface/icons/production_method_icons`

---

**可注入 能否对该类型使用 INJECT 数据库函数？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **可替换 能否对该类型使用 REPLACE 数据库函数？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**相关游戏对象：** 生产方式组，[商品](Goods modding.md)

生产方式决定建筑的投入与产出，因此对游戏影响极大。生产方式定义于 /Victoria 3/game/common/production_methods，遵循以下基本格式：

```
[production_method] = {
	texture = [path]
	
	building_modifiers = {
		workforce_scaled = {
			[modifiers]
		}

		level_scaled = {
			[modifiers]
		}
	}
}
```

每个生产方式都需要自己独一无二的脚本名称；按惯例通常为 `pm_[script_name]`，且往往包含建筑名称以区分相关变体。以上只是最常见的设置，实际还有许多特性和选项。

| 特性 | 默认值 | 描述 | 示例 |
|---|---|---|---|
| texture = [path] | unset | 图标 |  |
| is_default = yes/no | no | 是否为该组的默认生产方式？若组内没有生产方式被指定为默认，则第一个定义的生产方式被视为默认。PRCAL-9862：某些函数会将名为 pm_default 或 default 的生产方式视为默认。 |  |
| required_input_goods = [key] | unset | 列出的商品须在本地可供获取才能激活该生产方式。用于检查本地商品是否存在。 | 所有使用电力的生产方式都带有 `required_input_goods = electricity` |
| unlocking_laws = { [laws] } | unset | 激活该生产方式所需的（任一）法律列表 | 工人合作社所有制 unlocking_laws = { law_cooperative_ownership } |
| disallowing_laws = { [laws] } | unset | 阻止使用该生产方式的法律。 | 公开交易 disallowing_laws = { law_command_economy law_cooperative_ownership } |
| unlocking_technologies = { [technologies] } | unset | 激活该生产方式所需的（任一）技术列表。大多数生产方式由此解锁。 | 公开交易 unlocking_technologies = { mutual_funds } |
| unlocking_production_methods = { [production_methods] } | unset | 激活该生产方式所需的（任一）生产方式列表。这些必须指向同一建筑上的生产方式键。主要用于自动化方式同时要求更先进的“主要”生产。 | 火炮铸造厂的公开交易 unlocking_production_methods = { pm_smoothbores pm_breech_loaders pm_recoiled_barrels } |
| unlocking_global_technologies = { [technologies] } | unset | 需要世界范围内发明出来才能激活该生产方式的（任一）技术列表。 | 原版未使用 |
| unlocking_principles = { [principles] } | unset | 激活该生产方式所需的（任一）强权集团原则列表。 | 高效罐装实践 |
| unlocking_identity = [power_bloc_identity] | unset | 启用该生产方式的强权集团认同 | 强权集团纪念建筑方式 |
| replacement_if_valid = [production_method] | unset | 若所列生产方式可用，则自动从当前方式切换至该方式 | 真空包装 |
| is_hidden_when_unavailable = yes | no | 在生产方式不可选择时将其隐藏 | 高效罐装实践 |
| ai_weight = [integer] | 1.0 | AI 基础权重 | 原版未使用 |
| pollution_generation = [float] | 0 | 该生产方式激活时，该建筑为其所在地区添加多少污染（地区总污染按可耕地面积缩放） | 所有“生产”类生产方式都使用此项，从农业到工业皆是。多数生产方式从 5 开始，随生产方式进步增至 10 再到 15。多数农业在 5 左右，多数工业在 10-15，而炼油发电等则高达 75 污染。 |

生产方式的效果通常通过 [modifiers](Modifier types.md) 表达，它们可作用于国家、州或建筑，并可按建筑等级、就业百分比缩放，或不缩放。

| 特性 | 描述 | 示例 |
|---|---|---|
| country_modifiers = { [modifiers] } | 该生产方式激活时，这些 modifier 作用于国家。 | 政府行政的立式档案柜 country_modifiers = { workforce_scaled = { country_bureaucracy_add = 65 } } |
| state_modifiers = { [modifiers] } | 该生产方式激活时，这些 modifier 作用于州。 | 铁路的蒸汽机车 state_modifiers = { workforce_scaled = { state_infrastructure_add = 25 } } |
| building_modifiers = { [modifiers] } | 该生产方式激活时，这些 modifier 作用于建筑。这是最常见的 modifier，因为商品的投入与产出通常就在这里定义。 | 政府行政的立式档案柜 building_modifiers = { workforce_scaled = { goods_input_paper_add = 20 } level_scaled = { building_employment_clerks_add = 4000 } } |
| timed_modifiers = { [scripted modifiers] } | 生产方式变更后，这些脚本化 modifier 作用于建筑。持续时间为 BUILDING_TIMED_MODIFIER_WEEKS。最常见且唯一地用于切换军事生产方式以造成暂时性减益。 | 兵营的步兵班 timed_modifiers = { pm_offense_defense_readjustment_minor } 1.5 版本后未再使用。 |
| workforce_scaled = { [modifiers] } | 这些 modifier 先乘以建筑等级，再按该建筑就业水平百分比缩放。最常用于商品的投入与产出。 | 家具工业的精密工具 workforce_scaled = { # 投入商品 goods_input_hardwood_add = 25 goods_input_tools_add = 10 goods_input_wood_add = -25 # 产出商品 goods_output_furniture_add = -55 goods_output_luxury_furniture_add = 55 } |
| level_scaled = { [modifiers] } | 这些 modifier 乘以建筑的等级。最常用于就业等级。 | 家具工业的精密工具 level_scaled = { building_employment_shopkeepers_add = 1000 } |
| unscaled = { [modifiers] } | 这些 modifier 在任何等级或就业百分比下保持不变。主要用于所有权份额之类，或用于死亡率。 | 矿山的硝化甘油炸药 unscaled = { building_laborers_mortality_mult = 0.3 building_machinists_mortality_mult = 0.2 building_engineers_mortality_mult = 0.1 } |

关于如何将新的自定义商品实现为投入与产出，参见 [Goods modding#Building use](Goods modding.md)。类似流程也可用于添加其他新效果，例如自定义职业。

## 地图模型

觉得这篇文章缺少了什么？
+
将其添加到本文中，
帮助其他玩家！
请注意
样式指南
。

## 建筑脚本文档

### 建筑作用域

以下 [effects](Effect.md)、[event targets](Event target.md) 和 [triggers](Trigger.md) 可在建筑作用域中使用。

| Effect | 描述 | 示例 | 目标 |
|---|---|---|---|
| add_modifier | 为作用域中的对象添加定时 modifier 效果 | add_modifier = { name = static_modifier_name days/weeks/months/years = value（可选）#可使用脚本值，负值为永久 multiplier = value（可选）#乘以静态 modifier 的数值 is_decaying = yes（可选）#设为 modifier 在持续期间强度衰减 } add_modifier = static_modifier_name #设为无倍率且不衰减的永久 modifier |  |
| every_combat_unit | 遍历输入作用域中的所有战斗单位 | every_combat_unit = { limit = { <triggers> } #可选 <effects> } | new_combat_unit |
| ordered_combat_unit | 遍历输入作用域中的所有战斗单位 | ordered_combat_unit = { limit = { <triggers> } #可选 order_by = script_value #通过比较确定作用域的排序 position = int #可选，默认为 0；按排序选取作用域，从 0 开始计数 min = int #可选，默认为 0；设定返回的“顶部”位置，从 0 开始计数 max = script_value #可选，默认为 1/inf；返回的作用域数量，未指定 min 时为 1，指定时为 inf check_range_bounds = no #可选；若列表小于 min/max 时不希望记录错误 <effects> } | new_combat_unit |
| random_combat_unit | 遍历输入作用域中的所有战斗单位 | random_combat_unit = { limit = { <triggers> } #可选 weight = { <mtth blocks> } #可选 <effects> } | new_combat_unit |
| remove_modifier | 移除作用域中对象的定时 modifier 效果 | remove_modifier = static_modifier_name |  |
| set_subsidized | 设置建筑是否受补贴 | set_subsidized = yes/no |  |

| Trigger | 描述 | 示例 | 目标 |
|---|---|---|---|
| any_combat_unit | 遍历输入作用域中的所有战斗单位 | any_combat_unit = { filter = { <triggers> }（可选）<count=num/all> / <percent=fixed_point>（可选）<triggers> } | new_combat_unit |
| building_has_goods_shortage | 检查建筑是否有任何投入商品短缺 | building_has_goods_shortage = yes/no | boolean |
| can_queue_building_levels | 检查建筑所有者是否可在不触及等级或资源潜力上限的情况下排队建造指定数量的额外等级 | can_queue_building_levels = number |  |
| cash_reserves_available | 评估生产建筑的可用现金储备 | cash_reserves_available > 25000 | value |
| cash_reserves_ratio | 评估生产建筑的可用现金储备相对于其上限的比例。若建筑没有现金储备上限则返回 1 | cash_reserves_ratio > 0.2 | value |
| country_ownership_fraction | 比较该建筑的等级中被某国拥有的比例 | country_ownership_fraction > 0.5 | value |
| earnings | 比较建筑当前每名雇员的年收入 | earnings >= 10 | value |
| fraction_of_levels_owned_by_country | 比较某国或该国投资者拥有建筑总等级的比例 | fraction_of_levels_owned_by_country = { target = c:GBR value > 0.5 } | value |
| has_active_production_method | 检查作用域建筑是否激活了指定的生产方式 | has_active_production_method = key |  |
| has_deployed_units | 检查建筑是否支持任何已部署到本土总部之外的单位 | has_deployed_units = yes/no | boolean |
| has_employee_slots_filled | 检查某一 pop 类型的雇员数量是否高于或低于建筑当前可雇用总量的给定百分比。即例如某建筑的店主雇用是否达到当前雇用容量的 80%（以 0.8 表示）。 | has_employee_slots_filled = { pop_type = <pop type> percent = <0-1 value> } |  |
| has_failed_hires | 检查建筑上周是否雇人失败 | has_failed_hires = yes/no | boolean |
| has_modifier | 检查支持的作用域是否有某个定时 modifier | has_modifier = <key> |  |
| is_buildable | 检查建筑是否 buildable = yes（默认） | is_buildable = yes/no | boolean |
| is_building_group | 若作用域为属于给定组的建筑则为真 | building_group = building |  |
| is_building_type | 若作用域为给定类型的建筑则为真 | is_building_type = building |  |
| is_government_funded | 检查建筑是否 is_government_funded | is_government_funded = yes/no | boolean |
| is_subsidized | 检查建筑是否正在接受补贴 | is_subsidized = yes/no | boolean |
| is_subsistence_building | 检查建筑是否为自给建筑 | is_subsistence_building = yes/no | boolean |
| is_under_construction | 检查建筑是否在建 | is_under_construction = bool | boolean |
| levels_owned_by_country | 比较某国或该国投资者在建筑中拥有的等级数 | levels_owned_by_country = { target = c:GBR value >= 1 } | value |
| occupancy | 评估建筑当前的占用率 | occupancy < 0.25 | value |
| private_ownership_fraction | 比较该建筑的等级中私人拥有的比例 | private_ownership_fraction > 0.5 | value |
| self_ownership_fraction | 比较该建筑的等级中被建筑自身拥有的比例 | self_ownership_fraction > 0.5 | value |
| weekly_profit | 检查建筑本周获得的利润是否高于或低于给定值 | weekly_profit >= 20.0 | value |
| Event target | 描述 | 目标 scope |
|---|---|---|
| group | 从建筑对象或建筑类型切换到其所属组的 scope | building_group |
| level | 切换到建筑等级的 scope | value |
| level_after_queued_constructions | 切换到所有排队中的建造完工后建筑等级的 scope | value |
| market | 切换到该对象所在市场的 scope | market |
| modifier | 切换到当前对象所拥有的、指定键的 modifier 类型数值的 scope，示例：modifier:country_influence_add | boolean, value |
| owner | 切换到该对象所有者国家的 scope | country |
| region | 切换到该对象所在战略区域的 scope！ | strategic_region |
| state | 切换到该对象所在州的 scope | state |
| training_rate | 切换到建筑当前每周最大训练速率的 scope | value |
| type | 从对象切换到其类型的 scope | amendment_type, building_type, company_type, diplomatic_play_type, harvest_condition_type, institution_type, interest_group_type, law_type, political_movement_type, ship_type, strait_type |

### 建筑 modifier 类型

`building_` [modifier 类型](Modifier types.md) 将其效果应用于建筑。应用于国家时，会影响该国拥有的所有建筑；同理，应用于州时，会影响该州内的所有建筑。

| Modifier 类型 | 本地化名称 | 类型 | 格式 | 备注 |
|---|---|---|---|---|
| building_academics_job_attractiveness_mult | 学者的职业吸引力 | 乘法 | percent, good |  |
| building_academics_mortality_mult | 学者的死亡率 | 乘法 | percent, bad |  |
| building_academics_shares_add | 学者人口持股份额 | 加法 | neutral |  |
| building_academics_standard_of_living_add | 学者的生活水平 | 加法 | good |  |
| building_aristocrats_job_attractiveness_mult | 贵族的职业吸引力 | 乘法 | percent, good |  |
| building_aristocrats_shares_add | 贵族人口持股份额 | 加法 | neutral |  |
| building_aristocrats_standard_of_living_add | 贵族的生活水平 | 加法 | good |  |
| building_arms_industry_throughput_add | 军火工业建筑吞吐量 | 加法 | percent, good |  |
| building_art_academy_throughput_add | 艺术学院建筑吞吐量 | 加法 | percent, good |  |
| building_artillery_foundry_throughput_add | 火炮铸造厂建筑吞吐量 | 加法 | percent, good |  |
| building_automotive_industry_throughput_add | 汽车工业建筑吞吐量 | 加法 | percent, good |  |
| building_barrack_throughput_add | 兵营建筑吞吐量 | 加法 | percent, good |  |
| building_bureaucrats_job_attractiveness_mult | 官僚的职业吸引力 | 乘法 | percent, good |  |
| building_bureaucrats_shares_add | 官僚人口持股份额 | 加法 | neutral |  |
| building_bureaucrats_standard_of_living_add | 官僚的生活水平 | 加法 | good |  |
| building_capitalists_job_attractiveness_mult | 资本家的职业吸引力 | 乘法 | percent, good |  |
| building_capitalists_shares_add | 资本家人口持股份额 | 加法 | neutral |  |
| building_capitalists_standard_of_living_add | 资本家的生活水平 | 加法 | good |  |
| building_cash_reserves_mult | 最大现金储备 | 乘法 | percent, good |  |
| building_chemical_plant_throughput_add | 化肥厂建筑吞吐量 | 加法 | percent, good |  |
| building_clergymen_job_attractiveness_mult | 教士的职业吸引力 | 乘法 | percent, good |  |
| building_clergymen_shares_add | 教士人口持股份额 | 加法 | neutral |  |
| building_clergymen_standard_of_living_add | 教士的生活水平 | 加法 | good |  |
| building_clerks_job_attractiveness_mult | 职员（Clerks）的职业吸引力 | 乘法 | percent, good |  |
| building_clerks_shares_add | 职员人口持股份额 | 加法 | neutral |  |
| building_clerks_standard_of_living_add | 职员的生活水平 | 加法 | good |  |
| building_coal_mine_throughput_add | 煤矿建筑吞吐量 | 加法 | percent, good |  |
| building_coffee_plantation_throughput_add | 咖啡种植园建筑吞吐量 | 加法 | percent, good |  |
| building_company_government_dividends_add | 公司政府分红 | 加法 | percent, neutral |  |
| building_company_worker_dividends_add | 公司劳动力分红 | 加法 | percent, neutral |  |
| building_construction_sector_throughput_add | 建造部门建筑吞吐量 | 加法 | percent, good |  |
| building_cotton_plantation_throughput_add | 棉花种植园建筑吞吐量 | 加法 | percent, good |  |
| building_dye_plantation_throughput_add | 染料种植园建筑吞吐量 | 加法 | percent, good |  |
| building_economy_of_scale_level_cap_add | 规模经济建筑等级上限 | 加法 | good |  |
| building_electrics_industry_throughput_add | 电力工业建筑吞吐量 | 加法 | percent, good |  |
| building_employment_academics_add | 每等级学者数量 | 加法 | neutral |  |
| building_employment_aristocrats_add | 每等级贵族数量 | 加法 | neutral |  |
| building_employment_bureaucrats_add | 每等级官僚数量 | 加法 | neutral |  |
| building_employment_capitalists_add | 每等级资本家数量 | 加法 | neutral |  |
| building_employment_clergymen_add | 每等级教士数量 | 加法 | neutral |  |
| building_employment_clerks_add | 每等级职员数量 | 加法 | neutral |  |
| building_employment_engineers_add | 每等级工程师数量 | 加法 | neutral |  |
| building_employment_farmers_add | 每等级农民数量 | 加法 | neutral |  |
| building_employment_laborers_add | 每等级劳工数量 | 加法 | neutral |  |
| building_employment_machinists_add | 每等级机械师数量 | 加法 | neutral |  |
| building_employment_officers_add | 每等级军官数量 | 加法 | neutral |  |
| building_employment_peasants_add | 每等级自给农数量 | 加法 | neutral |  |
| building_employment_shopkeepers_add | 每等级店主数量 | 加法 | neutral |  |
| building_employment_slaves_add | 每等级奴隶数量 | 加法 | neutral |  |
| building_employment_soldiers_add | 每等级服役人员数量 | 加法 | neutral |  |
| building_engineers_job_attractiveness_mult | 工程师的职业吸引力 | 乘法 | percent, good |  |
| building_engineers_mortality_mult | 工程师的死亡率 | 乘法 | percent, bad |  |
| building_engineers_shares_add | 工程师人口持股份额 | 加法 | neutral |  |
| building_engineers_standard_of_living_add | 工程师的生活水平 | 加法 | good |  |
| building_explosives_factory_throughput_add | 炸药工厂建筑吞吐量 | 加法 | percent, good |  |
| building_farmers_job_attractiveness_mult | 农民的职业吸引力 | 乘法 | percent, good |  |
| building_farmers_standard_of_living_add | 农民的生活水平 | 加法 | good |  |
| building_fishing_wharf_throughput_add | 渔港建筑吞吐量 | 加法 | percent, good |  |
| building_food_industry_throughput_add | 食品工业建筑吞吐量 | 加法 | percent, good |  |
| building_furniture_manufactory_throughput_add | 家具制造厂建筑吞吐量 | 加法 | percent, good |  |
| building_glassworks_throughput_add | 玻璃厂建筑吞吐量 | 加法 | percent, good |  |
| building_gold_field_throughput_add | 金矿区建筑吞吐量 | 加法 | percent, good |  |
| building_gold_mine_throughput_add | 金矿建筑吞吐量 | 加法 | percent, good |  |
| building_goods_input_mult | 商品投入 | 乘法 | percent, bad |  |
| building_government_administration_throughput_add | 政府行政建筑吞吐量 | 加法 | percent, good |  |
| building_iron_mine_throughput_add | 铁矿建筑吞吐量 | 加法 | percent, good |  |
| building_job_attractiveness_mult | 职业吸引力 | 乘法 | percent, good |  |
| building_laborers_job_attractiveness_mult | 劳工的职业吸引力 | 乘法 | percent, good |  |
| building_laborers_mortality_mult | 劳工的死亡率 | 乘法 | percent, bad |  |
| building_laborers_shares_add | 劳工人口持股份额 | 加法 | neutral |  |
| building_laborers_standard_of_living_add | 劳工的生活水平 | 加法 | good |  |
| building_lead_mine_throughput_add | 铅矿建筑吞吐量 | 加法 | percent, good |  |
| building_level_bureaucracy_cost_add | 建筑等级行政力成本 | 加法 | bad |  |
| building_livestock_ranch_throughput_add | 畜牧场建筑吞吐量 | 加法 | percent, good |  |
| building_machinists_job_attractiveness_mult | 机械师的职业吸引力 | 乘法 | percent, good |  |
| building_machinists_mortality_mult | 机械师的死亡率 | 乘法 | percent, bad |  |
| building_machinists_shares_add | 机械师人口持股份额 | 加法 | neutral |  |
| building_machinists_standard_of_living_add | 机械师的生活水平 | 加法 | good |  |
| building_maize_farm_throughput_add | 玉米农场建筑吞吐量 | 加法 | percent, good |  |
| building_millet_farm_throughput_add | 小米农场建筑吞吐量 | 加法 | percent, good |  |
| building_minimum_incorporated_subsistence_employment_add | 已整合州受保护的自给就业 | 加法 | percent, neutral |  |
| building_minimum_wage_mult | 建筑工资目标 | 乘法 | percent, neutral |  |
| building_mobilization_cost_mult | 动员商品需求 | 乘法 | percent, bad |  |
| building_motor_industry_throughput_add | 发动机工业建筑吞吐量 | 加法 | percent, good |  |
| building_munition_plant_throughput_add | 弹药厂建筑吞吐量 | 加法 | percent, good |  |
| building_nationalization_cost_mult | 国有化补偿 | 乘法 | percent, bad |  |
| building_nationalization_investment_return_add | 国有化投资回报 | 加法 | percent, good |  |
| building_nationalization_radicals_mult | 国有化产生的激进派 | 乘法 | percent, bad |  |
| building_naval_administration_hiring_rate_mult | 海军行政雇佣速度 | 乘法 | percent, good |  |
| building_naval_administration_throughput_add | 海军行政建筑吞吐量 | 加法 | percent, good |  |
| building_naval_administration_training_rate_add | 海军行政训练速率 | 加法 | good |  |
| building_naval_administration_training_rate_mult | 海军行政训练速率 | 乘法 | percent, good |  |
| building_officers_job_attractiveness_mult | 军官的职业吸引力 | 乘法 | percent, good |  |
| building_officers_shares_add | 军官人口持股份额 | 加法 | neutral |  |
| building_officers_standard_of_living_add | 军官的生活水平 | 加法 | good |  |
| building_opium_plantation_throughput_add | 鸦片种植园建筑吞吐量 | 加法 | percent, good |  |
| building_paper_mill_throughput_add | 造纸厂建筑吞吐量 | 加法 | percent, good |  |
| building_peasants_job_attractiveness_mult | 自给农的职业吸引力 | 乘法 | percent, good |  |
| building_peasants_standard_of_living_add | 自给农的生活水平 | 加法 | good |  |
| building_port_throughput_add | 港口建筑吞吐量 | 加法 | percent, good |  |
| building_power_plant_throughput_add | 发电厂建筑吞吐量 | 加法 | percent, good |  |
| building_railway_throughput_add | 铁路建筑吞吐量 | 加法 | percent, good |  |
| building_rice_farm_throughput_add | 稻米农场建筑吞吐量 | 加法 | percent, good |  |
| building_rubber_plantation_throughput_add | 橡胶种植园建筑吞吐量 | 加法 | percent, good |  |
| building_rye_farm_throughput_add | 黑麦农场建筑吞吐量 | 加法 | percent, good |  |
| building_self_investment_chance_add | 建筑自主投资几率 | 加法 | percent, neutral |  |
| building_shipyard_throughput_add | 造船厂建筑吞吐量 | 加法 | percent, good |  |
| building_shopkeepers_job_attractiveness_mult | 店主的职业吸引力 | 乘法 | percent, good |  |
| building_shopkeepers_shares_add | 店主人口持股份额 | 加法 | neutral |  |
| building_shopkeepers_standard_of_living_add | 店主的生活水平 | 加法 | good |  |
| building_silk_plantation_throughput_add | 丝绸种植园建筑吞吐量 | 加法 | percent, good |  |
| building_slaves_mortality_mult | 奴隶的死亡率 | 乘法 | percent, bad |  |
| building_slaves_standard_of_living_add | 奴隶的生活水平 | 加法 | good |  |
| building_soldiers_job_attractiveness_mult | 服役人员的职业吸引力 | 乘法 | percent, good |  |
| building_soldiers_shares_add | 服役人员人口持股份额 | 加法 | neutral |  |
| building_soldiers_standard_of_living_add | 服役人员的生活水平 | 加法 | good |  |
| building_steel_mill_throughput_add | 钢厂建筑吞吐量 | 加法 | percent, good |  |
| building_subsistence_farm_throughput_add | 自给农场建筑吞吐量 | 加法 | percent, good |  |
| building_subsistence_output_add | 自给产出 | 加法 | neutral |  |
| building_subsistence_output_mult | 自给产出 | 乘法 | percent, neutral |  |
| building_sugar_plantation_throughput_add | 糖类种植园建筑吞吐量 | 加法 | percent, good |  |
| building_sulfur_mine_throughput_add | 硫磺矿建筑吞吐量 | 加法 | percent, good |  |
| building_synthetics_plant_throughput_add | 合成材料厂建筑吞吐量 | 加法 | percent, good |  |
| building_tea_plantation_throughput_add | 茶叶种植园建筑吞吐量 | 加法 | percent, good |  |
| building_textile_mill_throughput_add | 纺织厂建筑吞吐量 | 加法 | percent, good |  |
| building_throughput_add | 吞吐量 | 加法 | percent, good |  |
| building_tobacco_plantation_throughput_add | 烟草种植园建筑吞吐量 | 加法 | percent, good |  |
| building_tooling_workshop_throughput_add | 工具作坊建筑吞吐量 | 加法 | percent, good |  |
| building_trade_center_throughput_add | 贸易中心建筑吞吐量 | 加法 | percent, good |  |
| building_training_rate_add | 训练速率 | 加法 | good |  |
| building_training_rate_mult | 训练速率 | 乘法 | percent, good |  |
| building_unincorporated_subsistence_output_mult | 未整合州自给产出 | 乘法 | percent, good |  |
| building_unincorporated_throughput_add | 未整合州吞吐量 | 加法 | percent, good |  |
| building_university_throughput_add | 大学建筑吞吐量 | 加法 | percent, good |  |
| building_urban_center_throughput_add | 城镇中心建筑吞吐量 | 加法 | percent, good |  |
| building_vineyard_throughput_add | 葡萄园建筑吞吐量 | 加法 | percent, good |  |
| building_whaling_station_throughput_add | 捕鲸站建筑吞吐量 | 加法 | percent, good |  |
| building_wheat_farm_throughput_add | 小麦农场建筑吞吐量 | 加法 | percent, good |  |
| building_working_conditions_mult | 危险工作条件 | 乘法 | percent, bad |  |

### 建筑组 modifier 类型

`building_group_` [modifier 类型](Modifier types.md) 将其效果应用于该组内的所有建筑。应用于国家时，会影响该国拥有的该组内所有建筑；同理，应用于州时，会影响该州内该组的所有建筑。
| Modifier type | 本地化文本 | Type | Format | Notes |
|---|---|---|---|---|
| building_group_bg_agriculture_allowed_collectivization_add | 农业建筑最低工人自有等级 | additive | percent, good |  |
| building_group_bg_agriculture_construction_efficiency_add | 农业建造效率 | additive | percent, good |  |
| building_group_bg_agriculture_employee_mult | 农业雇员数量 | multiplicative | percent, bad |  |
| building_group_bg_agriculture_farmers_mortality_mult | 农业中受雇农民的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_agriculture_infrastructure_usage_mult | 农业建筑的基础设施使用量 | multiplicative | percent, bad |  |
| building_group_bg_agriculture_laborers_mortality_mult | 农业中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_agriculture_mortality_mult | 农业雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_agriculture_self_investment_chance_add | 农业建筑自主投资几率 | additive | percent, neutral |  |
| building_group_bg_agriculture_standard_of_living_add | 农业雇员生活水平 | additive | good |  |
| building_group_bg_agriculture_tax_mult | 农业税收收入 | multiplicative | percent, neutral |  |
| building_group_bg_agriculture_throughput_add | 农业吞吐量 | additive | percent, good |  |
| building_group_bg_arts_allowed_collectivization_add | 艺术类建筑最低工人自有等级 | additive | percent, good |  |
| building_group_bg_arts_throughput_add | 艺术类建筑吞吐量 | additive | percent, good |  |
| building_group_bg_construction_infrastructure_usage_mult | 建造部门建筑的基础设施使用量 | multiplicative | percent, bad |  |
| building_group_bg_construction_laborers_mortality_mult | 建造业中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_extraction_allowed_collectivization_add | 采掘业建筑最低工人自有等级 | additive | percent, good |  |
| building_group_bg_extraction_construction_efficiency_add | 采掘业建造效率 | additive | percent, good |  |
| building_group_bg_extraction_self_investment_chance_add | 采掘业建筑自主投资几率 | additive | percent, neutral |  |
| building_group_bg_extraction_throughput_add | 采掘业吞吐量 | additive | percent, good |  |
| building_group_bg_fishing_employee_mult | 渔业雇员数量 | multiplicative | percent, bad |  |
| building_group_bg_fishing_engineers_mortality_mult | 渔业码头中受雇工程师的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_fishing_laborers_mortality_mult | 渔业码头中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_fishing_machinists_mortality_mult | 渔业码头中受雇技工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_fishing_mortality_mult | 渔业雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_fishing_standard_of_living_add | 渔业雇员生活水平 | additive | good |  |
| building_group_bg_fishing_tax_mult | 渔业税收收入 | multiplicative | percent, neutral |  |
| building_group_bg_fishing_throughput_add | 渔业吞吐量 | additive | percent, good |  |
| building_group_bg_government_construction_efficiency_add | 政府建筑建造效率 | additive | percent, good |  |
| building_group_bg_government_employee_mult | 政府雇员数量 | multiplicative | percent, bad |  |
| building_group_bg_government_mortality_mult | 政府雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_government_standard_of_living_add | 政府雇员生活水平 | additive | good |  |
| building_group_bg_government_tax_mult | 政府税收收入 | multiplicative | percent, neutral |  |
| building_group_bg_government_throughput_add | 政府建筑吞吐量 | additive | percent, good |  |
| building_group_bg_heavy_industry_allowed_collectivization_add | 重工业建筑最低工人自有等级 | additive | percent, good |  |
| building_group_bg_heavy_industry_construction_efficiency_add | 重工业建造效率 | additive | percent, good |  |
| building_group_bg_heavy_industry_engineers_mortality_mult | 重工业中受雇工程师的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_heavy_industry_laborers_mortality_mult | 重工业中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_heavy_industry_machinists_mortality_mult | 重工业中受雇技工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_heavy_industry_mortality_mult | 重工业雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_heavy_industry_throughput_add | 重工业吞吐量 | additive | percent, good |  |
| building_group_bg_infrastructure_construction_efficiency_add | 基础设施建造效率 | additive | percent, good |  |
| building_group_bg_infrastructure_employee_mult | 基础设施雇员数量 | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_engineers_mortality_mult | 基础设施中受雇工程师的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_laborers_mortality_mult | 基础设施中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_machinists_mortality_mult | 基础设施中受雇技工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_mortality_mult | 基础设施雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_infrastructure_self_investment_chance_add | 基础设施建筑自主投资几率 | additive | percent, neutral |  |
| building_group_bg_infrastructure_standard_of_living_add | 基础设施雇员生活水平 | additive | good |  |
| building_group_bg_infrastructure_tax_mult | 基础设施税收收入 | multiplicative | percent, neutral |  |
| building_group_bg_infrastructure_throughput_add | 基础设施吞吐量 | additive | percent, good |  |
| building_group_bg_light_industry_allowed_collectivization_add | 轻工业建筑最低工人自有等级 | additive | percent, good |  |
| building_group_bg_light_industry_construction_efficiency_add | 轻工业建造效率 | additive | percent, good |  |
| building_group_bg_light_industry_laborers_mortality_mult | 轻工业中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_light_industry_machinists_mortality_mult | 轻工业中受雇技工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_light_industry_throughput_add | 轻工业吞吐量 | additive | percent, good |  |
| building_group_bg_logging_employee_mult | 伐木业雇员数量 | multiplicative | percent, bad |  |
| building_group_bg_logging_engineers_mortality_mult | 伐木业中受雇工程师的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_logging_laborers_mortality_mult | 伐木业中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_logging_machinists_mortality_mult | 伐木业中受雇技工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_logging_mortality_mult | 伐木业雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_logging_slaves_mortality_mult | 伐木业中受雇奴隶的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_logging_standard_of_living_add | 伐木业雇员生活水平 | additive | good |  |
| building_group_bg_logging_tax_mult | 伐木业税收收入 | multiplicative | percent, neutral |  |
| building_group_bg_logging_throughput_add | 伐木业吞吐量 | additive | percent, good |  |
| building_group_bg_logging_unincorporated_throughput_add | 未整合州的林场吞吐量 | additive | percent, good |  |
| building_group_bg_manor_houses_aristocrats_standard_of_living_add | 庄园宅邸中受雇贵族的生活水平 | additive | good |  |
| building_group_bg_manufacturing_allowed_collectivization_add | 制造业建筑最低工人自有等级 | additive | percent, good |  |
| building_group_bg_manufacturing_employee_mult | 制造业雇员数量 | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_engineers_mortality_mult | 制造业中受雇工程师的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_engineers_standard_of_living_add | 制造业中受雇工程师的生活水平 | additive | good |  |
| building_group_bg_manufacturing_laborers_mortality_mult | 制造业中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_laborers_standard_of_living_add | 制造业中受雇劳工的生活水平 | additive | good |  |
| building_group_bg_manufacturing_machinists_mortality_mult | 制造业中受雇技工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_machinists_standard_of_living_add | 制造业中受雇技工的生活水平 | additive | good |  |
| building_group_bg_manufacturing_mortality_mult | 制造业雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_manufacturing_self_investment_chance_add | 制造业建筑自主投资几率 | additive | percent, neutral |  |
| building_group_bg_manufacturing_standard_of_living_add | 制造业雇员生活水平 | additive | good |  |
| building_group_bg_manufacturing_tax_mult | 制造业税收收入 | multiplicative | percent, neutral |  |
| building_group_bg_manufacturing_throughput_add | 制造业吞吐量 | additive | percent, good |  |
| building_group_bg_manufacturing_unincorporated_throughput_add | 未整合州的制造业吞吐量 | additive | percent, good |  |
| building_group_bg_military_construction_efficiency_add | 军事建筑建造效率 | additive | percent, good |  |
| building_group_bg_military_industry_allowed_collectivization_add | 军工业建筑最低工人自有等级 | additive | percent, good |  |
| building_group_bg_military_industry_construction_efficiency_add | 军工业建造效率 | additive | percent, good |  |
| building_group_bg_military_industry_engineers_mortality_mult | 军工业中受雇工程师的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_military_industry_laborers_mortality_mult | 军工业中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_military_industry_machinists_mortality_mult | 军工业中受雇技工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_military_industry_mortality_mult | 军工业雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_military_industry_throughput_add | 军工业吞吐量 | additive | percent, good |  |
| building_group_bg_military_throughput_add | 军事建筑吞吐量 | additive | percent, good |  |
| building_group_bg_mining_allowed_collectivization_add | 矿场建筑最低工人自有等级 | additive | percent, good |  |
| building_group_bg_mining_employee_mult | 采矿业雇员数量 | multiplicative | percent, bad |  |
| building_group_bg_mining_engineers_mortality_mult | 矿场中受雇工程师的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_mining_engineers_standard_of_living_add | 矿场中受雇工程师的生活水平 | additive | good |  |
| building_group_bg_mining_laborers_mortality_mult | 矿场中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_mining_laborers_standard_of_living_add | 矿场中受雇劳工的生活水平 | additive | good |  |
| building_group_bg_mining_machinists_mortality_mult | 矿场中受雇技工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_mining_machinists_standard_of_living_add | 矿场中受雇技工的生活水平 | additive | good |  |
| building_group_bg_mining_mortality_mult | 采矿业雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_mining_slaves_mortality_mult | 矿场中受雇奴隶的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_mining_standard_of_living_add | 采矿业雇员生活水平 | additive | good |  |
| building_group_bg_mining_tax_mult | 采矿业税收收入 | multiplicative | percent, neutral |  |
| building_group_bg_mining_throughput_add | 矿场吞吐量 | additive | percent, good |  |
| building_group_bg_mining_unincorporated_throughput_add | 未整合州的矿场吞吐量 | additive | percent, good |  |
| building_group_bg_oil_extraction_employee_mult | 石油业雇员数量 | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_engineers_mortality_mult | 石油开采中受雇工程师的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_laborers_mortality_mult | 石油开采中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_machinists_mortality_mult | 石油开采中受雇技工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_mortality_mult | 石油业雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_oil_extraction_standard_of_living_add | 石油业雇员生活水平 | additive | good |  |
| building_group_bg_oil_extraction_tax_mult | 石油业税收收入 | multiplicative | percent, neutral |  |
| building_group_bg_oil_extraction_throughput_add | 油井吞吐量 | additive | percent, good |  |
| building_group_bg_plantations_allowed_collectivization_add | 种植园建筑最低工人自有等级 | additive | percent, good |  |
| building_group_bg_plantations_construction_efficiency_add | 种植园建造效率 | additive | percent, good |  |
| building_group_bg_plantations_employee_mult | 种植园雇员数量 | multiplicative | percent, bad |  |
| building_group_bg_plantations_farmers_mortality_mult | 种植园中受雇农民的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_plantations_infrastructure_usage_mult | 种植园的基础设施使用量 | multiplicative | percent, bad |  |
| building_group_bg_plantations_laborers_mortality_mult | 种植园中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_plantations_mortality_mult | 种植园雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_plantations_self_investment_chance_add | 种植园建筑自主投资几率 | additive | percent, neutral |  |
| building_group_bg_plantations_slaves_mortality_mult | 种植园中受雇奴隶的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_plantations_standard_of_living_add | 种植园雇员生活水平 | additive | good |  |
| building_group_bg_plantations_tax_mult | 种植园税收收入 | multiplicative | percent, neutral |  |
| building_group_bg_plantations_throughput_add | 种植园吞吐量 | additive | percent, good |  |
| building_group_bg_plantations_unincorporated_throughput_add | 未整合州的种植园吞吐量 | additive | percent, good |  |
| building_group_bg_power_allowed_collectivization_add | 发电厂建筑最低工人自有等级 | additive | percent, good |  |
| building_group_bg_power_self_investment_chance_add | 发电厂建筑自主投资几率 | additive | percent, neutral |  |
| building_group_bg_private_infrastructure_allowed_collectivization_add | 私营基础设施建筑最低工人自有等级 | additive | percent, good |  |
| building_group_bg_ranching_allowed_collectivization_add | 牧场建筑最低工人自有等级 | additive | percent, good |  |
| building_group_bg_ranching_construction_efficiency_add | 牧场建造效率 | additive | percent, good |  |
| building_group_bg_ranching_farmers_mortality_mult | 畜牧业中受雇农民的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_ranching_infrastructure_usage_mult | 牧场的基础设施使用量 | multiplicative | percent, bad |  |
| building_group_bg_ranching_laborers_mortality_mult | 畜牧业中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_ranching_mortality_mult | 畜牧业雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_ranching_self_investment_chance_add | 牧场建筑自主投资几率 | additive | percent, neutral |  |
| building_group_bg_ranching_standard_of_living_add | 畜牧业雇员生活水平 | additive | good |  |
| building_group_bg_ranching_tax_mult | 畜牧业税收收入 | multiplicative | percent, neutral |  |
| building_group_bg_ranching_throughput_add | 牧场吞吐量 | additive | percent, good |  |
| building_group_bg_rubber_employee_mult | 橡胶业雇员数量 | multiplicative | percent, bad |  |
| building_group_bg_rubber_laborers_mortality_mult | 橡胶种植园中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_rubber_mortality_mult | 橡胶业雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_rubber_slaves_mortality_mult | 橡胶种植园中受雇奴隶的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_rubber_standard_of_living_add | 橡胶业雇员生活水平 | additive | good |  |
| building_group_bg_rubber_tax_mult | 橡胶业税收收入 | multiplicative | percent, neutral |  |
| building_group_bg_rubber_throughput_add | 橡胶种植园吞吐量 | additive | percent, good |  |
| building_group_bg_rubber_unincorporated_throughput_add | 未整合州的橡胶种植园吞吐量 | additive | percent, good |  |
| building_group_bg_service_employee_mult | 城市中心雇员数量 | multiplicative | percent, bad |  |
| building_group_bg_service_mortality_mult | 城市中心雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_service_standard_of_living_add | 城市中心雇员生活水平 | additive | good |  |
| building_group_bg_service_tax_mult | 城市中心税收收入 | multiplicative | percent, neutral |  |
| building_group_bg_service_throughput_add | 服务业吞吐量 | additive | percent, good |  |
| building_group_bg_subsistence_agriculture_allowed_collectivization_add | 自给农业建筑最低工人自有等级 | additive | percent, good |  |
| building_group_bg_subsistence_agriculture_peasants_standard_of_living_add | 自给农业中受雇农奴的生活水平 | additive | good |  |
| building_group_bg_subsistence_ranching_allowed_collectivization_add | 自给畜牧业建筑最低工人自有等级 | additive | percent, good |  |
| building_group_bg_subsistence_ranching_peasants_standard_of_living_add | 自给畜牧业中受雇农奴的生活水平 | additive | good |  |
| building_group_bg_whaling_employee_mult | 捕鲸业雇员数量 | multiplicative | percent, bad |  |
| building_group_bg_whaling_laborers_mortality_mult | 捕鲸站中受雇劳工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_whaling_machinists_mortality_mult | 捕鲸站中受雇技工的死亡率 | multiplicative | percent, bad |  |
| building_group_bg_whaling_mortality_mult | 捕鲸业雇员死亡率 | multiplicative | percent, bad |  |
| building_group_bg_whaling_standard_of_living_add | 捕鲸业雇员生活水平 | additive | good |  |
| building_group_bg_whaling_tax_mult | 捕鲸业税收收入 | multiplicative | percent, neutral |  |
| building_group_bg_whaling_throughput_add | 捕鲸业吞吐量 | additive | percent, good |  |
### 建筑 GUI 脚本

主条目：
GUI script
| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessConsumedGoods |  | Unknown | Category: const |
| AccessModifier |  | Modifier | Category: const |
| AccessOwnerPopsList |  | PopList | Category: const |
| AccessPopsList |  | PopList | Category: const |
| AccessProducedGoods |  | Unknown | Category: const |
| AccessProductionMethod | ProductionMethodGroup | ProductionMethod | Category: const |
| AccessProductionMethodGroups |  | Unknown | Category: const |
| AccessSelf |  | Building | Category: const |
| AccessShortageGoods |  | Unknown | Category: const |
| AccessState |  | State | Category: const |
| AccessStateRegion |  | StateRegion | Category: const |
| CalcInfrastructureUsage |  | CFixedPoint |  |
| CalcInputAvailabilityOutputMult |  | CFixedPoint |  |
| CalcInputGoodsShortageTargetPenalty |  | CFixedPoint |  |
| CalcInputGoodsShortageTargetPenaltyFromGoods | Unknown | CFixedPoint |  |
| CalcUrbanizationProvided |  | int32 |  |
| CanBeAffectedByInputShortage | ModifierEntry | bool |  |
| CanBePrivatized |  | bool |  |
| CancelConstruction |  | Command |  |
| Downsize |  | Command |  |
| GetAdjustHiringTargetDesc |  | CString | Category: nonconst |
| GetAllEmployeesTransferDesc |  | CString | Category: nonconst |
| GetAllFailedHiresDesc |  | CString | Category: nonconst |
| GetArmyManpower |  | int64 | Category: nonconst |
| GetArmyReadinessStatusDesc |  | CString | Category: nonconst |
| GetAutoDownsizeTooltip |  | CString | Category: nonconst |
| GetAutoExpandTooltip |  | CString | Category: nonconst |
| GetAutoExpandTriggers |  | CString | Category: nonconst |
| GetAverageAnnualEarningsPerEmployee |  | CFixedPoint | Category: nonconst |
| GetAverageAnnualEarningsPerEmployeeFormatted |  | CString | Category: nonconst |
| GetAverageAnnualWage |  | CFixedPoint | Category: nonconst |
| GetAverageAnnualWageBreakdown |  | CString | Category: nonconst |
| GetAverageAnnualWageBreakdownForPopType | PopType | CString | Category: nonconst |
| GetAverageAnnualWageForPopType | PopType | CFixedPoint | Category: nonconst |
| GetAverageAnnualWageForPopTypeDesc | Unknown | CString | Category: nonconst |
| GetAverageAnnualWageSubsidies |  | CFixedPoint | Category: nonconst |
| GetAverageStandardOfLiving |  | CFixedPoint | Category: nonconst |
| GetBalance |  | CFixedPoint | Category: nonconst |
| GetBalanceDesc |  | CString | Category: nonconst |
| GetBuildingAssets |  | Unknown | Category: nonconst |
| GetBuildingGroupName |  | CString | Category: nonconst |
| GetBuildingOwnerships |  | Unknown | Category: nonconst |
| GetBuildingType |  | BuildingType | Category: nonconst |
| GetCancelConstructionTooltip |  | CString | Category: nonconst |
| GetCappedAssetsLong |  | Unknown | Category: nonconst |
| GetCappedAssetsLongRest |  | Unknown | Category: nonconst |
| GetCappedAssetsShort |  | Unknown | Category: nonconst |
| GetCappedAssetsShortRest |  | Unknown | Category: nonconst |
| GetCappedOwnersLong |  | Unknown | Category: nonconst |
| GetCappedOwnersLongRest |  | Unknown | Category: nonconst |
| GetCappedOwnersShort |  | Unknown | Category: nonconst |
| GetCappedOwnersShortRest |  | Unknown | Category: nonconst |
| GetCashReservesTrend |  | DataTrend | Category: nonconst |
| GetCasualtiesDesc |  | CString | Category: nonconst |
| GetChangeProductionMethodPopQualificationsWarningBreakdown | ProductionMethod | CString | Category: nonconst |
| GetCombatUnitCapacity |  | int32 | Category: nonconst |
| GetCombatUnitCapacityDesc |  | CString | Category: nonconst |
| GetCombatUnitProduction |  | CString | Category: nonconst |
| GetCombatUnitProductionBreakdown |  | CString | Category: nonconst |
| GetCombatUnitTypes |  | Unknown | Category: nonconst |
| GetCombatUnits |  | Unknown | Category: nonconst |
| GetCombatUnitsIcon |  | CString | Category: nonconst |
| GetCombatUnitsInFormation | MilitaryFormation | Unknown | Category: nonconst |
| GetCompany |  | Company | Category: nonconst |
| GetConstructionProgressPercentage |  | float | Category: nonconst |
| GetConstructionRemainingWeeksDesc |  | CString | Category: nonconst |
| GetConstructionSpeedPerWeek |  | CFixedPoint | Category: nonconst |
| GetConstructionSpeedPerWeekDesc |  | CString | Category: nonconst |
| GetConsumption | Goods | CFixedPoint | Category: nonconst |
| GetConsumptionDesc | Goods | CString | Category: nonconst |
| GetConsumptionValue | Goods | CFixedPoint | Category: nonconst |
| GetCurrentCashReserves |  | CFixedPoint | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetDebugTooltip |  | CString | Category: nonconst |
| GetDefaultOutputGoods |  | Goods | Category: nonconst |
| GetDownsizeTooltip |  | CString | Category: nonconst |
| GetEarnings |  | CFixedPoint | Category: nonconst |
| GetEarningsPerEmployeeTrend |  | DataTrend | Category: nonconst |
| GetEmployeeCap |  | int64 | Category: nonconst |
| GetEmployeesBreakdown |  | CString | Category: nonconst |
| GetEmployeesTransferDesc | PopType | CString | Category: nonconst |
| GetEmploymentPercentage |  | CFixedPoint | Category: nonconst |
| GetEmploymentTooltip |  | CString | Category: nonconst |
| GetEstablishmentDate |  | CString | Category: nonconst |
| GetExpansionLevel |  | int32 | Category: nonconst |
| GetExpansionLevelBreakdown |  | CString | Category: nonconst |
| GetExpansionLevelBreakdownDesc |  | CString | Category: nonconst |
| GetExpansionLevelDesc |  | CString | Category: nonconst |
| GetExpansionLevelsInQueue |  | int32 | Category: nonconst |
| GetFailedHiresDesc | PopType | CString | Category: nonconst |
| GetGoodsShortageListDesc |  | CString | Category: nonconst |
| GetGovernmentExpenses |  | CFixedPoint | Category: nonconst |
| GetGovernmentExpensesDesc |  | CString | Category: nonconst |
| GetHQ |  | Hq | Category: nonconst |
| GetID |  | int32 | Category: nonconst |
| GetIDString |  | CString | Category: nonconst |
| GetIcon |  | Unknown | Category: nonconst |
| GetInfrastructureUsageBreakdown |  | CString | Category: nonconst |
| GetInputMult |  | CFixedPoint | Category: nonconst |
| GetInputMultDesc |  | CString | Category: nonconst |
| GetInputOutputTooltip |  | CString | Category: nonconst |
| GetInputShortagePenalty |  | CFixedPoint | Category: nonconst |
| GetLastIncome |  | CFixedPoint | Category: nonconst |
| GetLastMaterialExpenses |  | CFixedPoint | Category: nonconst |
| GetLastMaterialExpensesDesc |  | CString | Category: nonconst |
| GetLastRevenue |  | CFixedPoint | Category: nonconst |
| GetLastRevenueBalancedSI | CFixedPoint int32 | CString | Category: nonconst |
| GetLastSlaveBasket |  | int32 | Category: nonconst |
| GetLastSlaveBasketDesc |  | CString | Category: nonconst |
| GetLastSlaveUpkeep |  | CFixedPoint | Category: nonconst |
| GetLastSlaveUpkeepDesc |  | CString | Category: nonconst |
| GetLastWagesExpenses |  | CFixedPoint | Category: nonconst |
| GetLastWagesExpensesDesc |  | CString | Category: nonconst |
| GetManpowerCapacity |  | int64 | Category: nonconst |
| GetMaxCashReserves |  | CFixedPoint | Category: nonconst |
| GetMaxPopSize | PopType | int64 | Category: nonconst |
| GetMaxPopSizeDesc | PopType | CString | Category: nonconst |
| GetMilitaryFormations |  | Unknown | Category: nonconst |
| GetMobilizationRatio |  | CFixedPoint | Category: nonconst |
| GetModifier |  | Modifier | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetNationalizeBuildingNoCompensationDesc | Unknown | CString | Category: nonconst |
| GetNationalizeBuildingWithCompensationDesc | Unknown | CString | Category: nonconst |
| GetNavyManpower |  | int64 | Category: nonconst |
| GetNoLevelsCanBeNationalizedDesc |  | CString | Category: nonconst |
| GetNoOfEmployed |  | int64 | Category: nonconst |
| GetNotHiringReasonDesc |  | CString | Category: nonconst |
| GetNumActiveUnitsProvidedToFormation | MilitaryFormation | int32 | Category: nonconst |
| GetNumEmployeesOfType | PopType | int64 | Category: nonconst |
| GetNumLevelsCanBeNationalized |  | int32 | Category: nonconst |
| GetNumOwnedLevels |  | int32 | Category: nonconst |
| GetNumUnitsOfCombatUnitType | CombatUnitType | int32 | Category: nonconst |
| GetNumUnitsOfCombatUnitTypeProvidedToFormation | Unknown Unknown | int32 | Category: nonconst |
| GetNumberOfCombatUnits |  | int32 | Category: nonconst |
| GetNumberOfFullyMobilizedBattalions |  | int32 | Category: nonconst |
| GetOutputPercentage | Goods | CFixedPoint | Category: nonconst |
| GetOutputRatio |  | CFixedPoint | Category: nonconst |
| GetOwner |  | Country | Category: nonconst |
| GetPopTypeFullyReplacedDesc | PopType | CString | Category: nonconst |
| GetPopTypeReplacementDesc | PopType | CString | Category: nonconst |
| GetPrivatizationTooltip |  | CString | Category: nonconst |
| GetProducedModifiers |  | Modifier | Category: nonconst |
| GetProduction | Goods | CFixedPoint | Category: nonconst |
| GetProductionDesc | Goods | CString | Category: nonconst |
| GetProductionMethodGroup | Unknown | ProductionMethodGroup | Category: nonconst |
| GetProductionValue | Goods | CFixedPoint | Category: nonconst |
| GetProfitability |  | CString | Category: nonconst |
| GetProfitabilityCompareIcon |  | CString | Category: nonconst |
| GetProfitabilityCompareIconInType |  | CString | Category: nonconst |
| GetProfitabilityInType |  | CString | Category: nonconst |
| GetProfitabilityInTypeTrend |  | DataTrend | Category: nonconst |
| GetProfitabilityRank |  | int32 | Category: nonconst |
| GetProfitabilityRankInType |  | int32 | Category: nonconst |
| GetProfitabilityTrend |  | DataTrend | Category: nonconst |
| GetQueueConstructionPopQualificationsWarningBreakdown |  | CString | Category: nonconst |
| GetQueueConstructionTooltip |  | CString | Category: nonconst |
| GetQueueMilitaryConstructionTooltip | MilitaryFormation CombatUnitType | CString | Category: nonconst |
| GetResetProductionMethodsToStandardTooltip |  | CString | Category: nonconst |
| GetSamplePops |  | Unknown | Category: nonconst |
| GetSizeTooltip |  | CString | Category: nonconst |
| GetState |  | State | Category: nonconst |
| GetStateRegion |  | StateRegion | Category: nonconst |
| GetStatusDesc |  | CString | Category: nonconst |
| GetSubsidies |  | CFixedPoint | Category: nonconst |
| GetSubsidiesDesc |  | CString | Category: nonconst |
| GetSubsidizeTooltip |  | CString | Category: nonconst |
| GetSubsistenceOutput |  | CFixedPoint | Category: nonconst |
| GetSubsistenceOutputDesc |  | CString | Category: nonconst |
| GetSubventions |  | CFixedPoint | Category: nonconst |
| GetTariffsPaid |  | CFixedPoint | Category: nonconst |
| GetTaxationRevenue |  | CFixedPoint | Category: nonconst |
| GetTaxationRevenueTooltip |  | CString | Category: nonconst |
| GetThroughputBonusCurrent |  | CFixedPoint | Category: nonconst |
| GetThroughputBonusTarget |  | CFixedPoint | Category: nonconst |
| GetThroughputDesc |  | CString | Category: nonconst |
| GetTimedModifiers |  | Unknown | Category: nonconst |
| GetTogglePrivatizationTooltip |  | CString | Category: nonconst |
| GetTooltip |  | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetTotalConsumptionValue |  | CFixedPoint | Category: nonconst |
| GetTotalExpenses |  | CFixedPoint | Category: nonconst |
| GetTotalExpensesBalancedSI | CFixedPoint int32 | CString | Category: nonconst |
| GetTotalProductionValue |  | CFixedPoint | Category: nonconst |
| GetTradeRevenue |  | CFixedPoint | Category: nonconst |
| GetTrainingRate |  | int64 | Category: nonconst |
| GetTrainingRateDesc |  | CString | Category: nonconst |
| GetUnitsProvidedToFormationBreakdown | MilitaryFormation | CString | Category: nonconst |
| GetUrbanizationProvidedBreakdown |  | CString | Category: nonconst |
| GetWageRate |  | CFixedPoint | Category: nonconst |
| GetWorstGoodsShortage |  | Goods | Category: nonconst |
| HasAnyInputShortage |  | bool |  |
| HasConstructionQueued |  | bool |  |
| HasFailedHires |  | bool |  |
| HasGovernmentConstructionQueued |  | bool |  |
| HasInputGoods |  | bool |  |
| HasInputShortage | Goods | bool |  |
| HasMaximumInputShortage | Goods | bool |  |
| HasOutputGoods |  | bool |  |
| HasPrivateConstructionQueued |  | bool |  |
| HasReachedLevelCap |  | bool |  |
| HasSlaves |  | bool |  |
| HasTradeRevenue |  | bool |  |
| IsActive |  | bool |  |
| IsActiveStr |  | CString |  |
| IsAutoDownsizing |  | bool |  |
| IsAutoExpanding |  | bool |  |
| IsBeingHighlighted |  | bool |  |
| IsBeingTutorialHighlighted |  | bool |  |
| IsBuildingType | BuildingType | bool |  |
| IsCappedBuilding |  | bool |  |
| IsCurrentlyUnderConstruction |  | bool |  |
| IsDownsizeable |  | bool |  |
| IsExpandable |  | bool |  |
| IsGovernmentFunded |  | bool |  |
| IsMilitaryBuilding |  | bool |  |
| IsOwner | Country | bool |  |
| IsPinnedInOutliner |  | bool |  |
| IsPotentialQueueConstruction |  | bool |  |
| IsRoleFullyReplacedByAnotherPopType | PopType | bool |  |
| IsSelfFunded |  | bool |  |
| IsSubsidized |  | bool |  |
| IsSubsistenceBuilding |  | bool |  |
| IsUrbanCenter |  | bool |  |
| IsValid |  | bool |  |
| MakeScope |  | Scope |  |
| NationalizeBuildingLevels | int32 | Command |  |
| ProvidesUrbanization |  | bool |  |
| QueueConstruction |  | Command |  |
| QueueMilitaryConstruction | MilitaryFormation CombatUnitType | Command |  |
| ResetProductionMethodsToStandard |  | Command |  |
| Self |  | Building |  |
| ShouldShowAsHiring |  | bool |  |
| ShouldShowAsUnableToHire |  | bool |  |
| ShouldShowAsUnwillingToHire |  | bool |  |
| ShowLevelAndMaxLevel |  | bool |  |
| SortBuildings | CString | void |  |
| ToggleAutoExpand |  | Command |  |
| ToggleAutoExpandOff |  | Command |  |
| ToggleAutoExpandOn |  | Command |  |
| TogglePinInOutliner |  | void |  |
| TogglePrivatization |  | Command |  |
| ToggleSubsidies |  | Command |  |
| ToggleSubsidiesOff |  | Command |  |
| ToggleSubsidiesOn |  | Command |  |
| UsesInfrastructure |  | bool |  |

| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessSelf |  | BuildingGroup | Category: const |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| IsBuildingGroup | BuildingGroup | bool |  |
| MakeScope |  | Scope |  |
| Self |  | BuildingGroup |  |

| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessProductionMethodGroups |  | Unknown | Category: const |
| AccessSelf |  | BuildingType | Category: const |
| ActivateExpansionLens |  | void |  |
| CanBeAutoExpanded |  | bool |  |
| CanBeSubsidized |  | bool |  |
| CanSwitchOwner |  | bool |  |
| CreatedByUrbanization |  | bool |  |
| FiredPopsBecomeRadical |  | bool |  |
| GetBackground |  | Unknown | Category: nonconst |
| GetBuildingGroup |  | BuildingGroup | Category: nonconst |
| GetBuildingGroupName |  | CString | Category: nonconst |
| GetBuildingKindDesc | Country | CString | Category: nonconst |
| GetBuildingModifier |  | Modifier | Category: nonconst |
| GetConstructionCosts |  | CString | Category: nonconst |
| GetCountryModifier |  | Modifier | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetDiscoveredResourceName |  | CString | Category: nonconst |
| GetExpansionMissingQualificationsDesc | Unknown Unknown | CString | Category: nonconst |
| GetExpansionProductivityDesc | Unknown Unknown | CString | Category: nonconst |
| GetExpansionProductivityImpact | Building State | CFixedPoint | Category: nonconst |
| GetExpansionProductivityImpactDesc | Building State | CString | Category: nonconst |
| GetExpansionRevenueImpact | Building State | CFixedPoint | Category: nonconst |
| GetExpansionRevenueImpactDesc | Building State | CString | Category: nonconst |
| GetID |  | int32 | Category: nonconst |
| GetIDString |  | CString | Category: nonconst |
| GetIcon |  | Unknown | Category: nonconst |
| GetKey |  | CString | Category: nonconst |
| GetModifierEffectsAsString |  | CString | Category: nonconst |
| GetMonopolyCompanyIn | Unknown | Company | Category: nonconst |
| GetMonopolyCountryIn | Unknown | Country | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetNumAvailableStatesForBuilding |  | int32 | Category: nonconst |
| GetNumLevelsInCountryFormatted | Country | CString | Category: nonconst |
| GetNumLevelsInCountryRaw | Country | int32 | Category: nonconst |
| GetNumLevelsOwnedByCompanyFormatted | Company | CString | Category: nonconst |
| GetNumLevelsOwnedByCompanyRaw | Company | int32 | Category: nonconst |
| GetProductivitySpanDesc | Country | CString | Category: nonconst |
| GetRequiredConstruction |  | CFixedPoint | Category: nonconst |
| GetResetProductionMethodsToStandardTooltip |  | CString | Category: nonconst |
| GetStandardProductionMethodDesc | Unknown | CString | Category: nonconst |
| GetStateModifier |  | Modifier | Category: nonconst |
| GetTabName |  | CString | Category: nonconst |
| GetToggleMonopolyEffectDesc |  | CString | Category: nonconst |
| GetTooltip |  | CString | Category: nonconst |
| GetTooltipForBuilding | Building | CString | Category: nonconst |
| GetTooltipForState | Unknown | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetUrbanizationProvidedBreakdown |  | CString | Category: nonconst |
| HasCompanyMonopoly | Unknown | bool |  |
| HasCountryMonopoly |  | bool |  |
| HasInputGoods |  | bool |  |
| HasMonopoly |  | bool |  |
| HasOutputGoods |  | bool |  |
| HasRequiredPrinciplesInCountry | Country | bool |  |
| HasRequiredTechnologiesInCountry | Country | bool |  |
| IsAlwaysSelfOwning |  | bool |  |
| IsBeingHighlighted |  | bool |  |
| IsBeingTutorialHighlighted |  | bool |  |
| IsBuildable |  | bool |  |
| IsBuildableInAnyState | Country | bool |  |
| IsCappedBuilding |  | bool |  |
| IsDownsizeable |  | bool |  |
| IsExpandable |  | bool |  |
| IsGovernmentFunded |  | bool |  |
| IsMilitaryBuilding |  | bool |  |
| IsRural |  | bool |  |
| IsSelfFunded |  | bool |  |
| IsSubsistenceBuilding |  | bool |  |
| IsUnique |  | bool |  |
| IsUrban |  | bool |  |
| IsUsingArableLand |  | bool |  |
| IssDevelopment |  | bool |  |
| MakeScope |  | Scope |  |
| ProvidesUrbanization |  | bool |  |
| RecruitsCombatUnits |  | bool |  |
| ResetProductionMethodsToStandard |  | Command |  |
| Self |  | BuildingType |  |
| ToggleMonopoly |  | Command |  |
| UsesInfrastructure |  | bool |  |
| Promote | Arguments | Output | Description |
|---|---|---|---|
| AccessModifier |  | Modifier | 类别：const |
| AccessOwnerPopsList |  | PopList | 类别：const |
| AccessPopsList |  | PopList | 类别：const |
| AccessProductionMethod | ProductionMethodGroup | ProductionMethod | 类别：const |
| AccessState |  | State | 类别：const |
| AccessStateRegion |  | StateRegion | 类别：const |
| GetBuildingType |  | BuildingType | 类别：nonconst |
| GetCompany |  | Company | 类别：nonconst |
| GetDefaultOutputGoods |  | Goods | 类别：nonconst |
| GetHQ |  | Hq | 类别：nonconst |
| GetModifier |  | Modifier | 类别：nonconst |
| GetOwner |  | Country | 类别：nonconst |
| GetProducedModifiers |  | Modifier | 类别：nonconst |
| GetProductionMethodGroup | Unknown | ProductionMethodGroup | 类别：nonconst |
| GetState |  | State | 类别：nonconst |
| GetStateRegion |  | StateRegion | 类别：nonconst |
| GetWorstGoodsShortage |  | Goods | 类别：nonconst |
| MakeScope |  | Scope |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| MakeScope |  | Scope |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| GetBuildingGroup |  | BuildingGroup | 类别：nonconst |
| GetBuildingModifier |  | Modifier | 类别：nonconst |
| GetCountryModifier |  | Modifier | 类别：nonconst |
| GetMonopolyCompanyIn | Unknown | Company | 类别：nonconst |
| GetMonopolyCountryIn | Country | Country | 类别：nonconst |
| GetStateModifier |  | Modifier | 类别：nonconst |
| MakeScope |  | Scope |  |

## 本地化（Localization）

主条目：
本地化（Localization）
每个建筑组、建筑、生产方式组和生产方式都必须在 mod 的 localization 文件夹内的 .yml 文件中进行本地化。

```
[building]: "X"
[building]_lens_option: "Expand X"
[building_group]: "X"
[production_method_group]: "X"
[production_method]: "X"
```

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [效果](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [修改器类型](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [脚本值](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [决议](Decision modding.md) • [事件](Event modding.md) • [历史](History modding.md) • [日志](Journal modding.md) • [修改器](Modifier modding.md) • 目标 • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | 建筑 • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [可自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图像](Event images.md) • [图形资产](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [音效](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [mod 兼容性](Mod compatibility.md) • [mod 结构](Mod structure.md) • [脚本测试](Scripted test.md) • [疑难解答](Troubleshooting.md) |
|---|---|

| 指南 | [Mod 翻译](Mod translation.md) • [新国家 mod 制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州 mod 制作指南](State modding guide.md) |
|---|---|