---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Needs
source: https://vic3.paradoxwikis.com/Needs
pageid: 3163
categories: [1.13, Articles_with_potentially_outdated_sections, Articles_with_potentially_outdated_images, Economy]
fetched: 2026-10-27
---
本文已针对游戏当前 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行验证。

经济
建筑
建筑列表
•
独特建筑
公司
•
特色公司
市场
商品
•
需求
生产方式
生产方式列表
国库
人口
文化
•
宗教
职业
•
资质
生活水平
•
需求
迁移

**需求**表示[人口](Pops.md)对[商品](Goods.md)的消费。所需商品的种类和数量取决于每个人口的[财富等级](Standard of living.md)。大多数需求可以由多种不同的商品来满足，因此人口在应对商品过剩和短缺时有一定的灵活性。

为了满足需求，人口会持续购买商品，直到所购商品的数量乘以其[基础价格](Goods.md)达到该财富等级下各需求类型所设定的数值。因此，基础价格更高的商品只需更少的数量即可满足同样的需求——例如，10 单位肉类（基础价格 30 → 30 × 10 = 300 需求满足）与 15 单位谷物（基础价格 20 → 20 × 15 = 300 需求满足）满足的食物需求相同。

虽然购买商品的总数量取决于基础价格，但人口在选择购买哪些商品以及购买多少时，从不考虑商品的基础价格或市场价格。

## 需求类型

不同商品通常具有不同的权重。人口会结合这些权重与市场供给，来决定在某一需求类型下不同商品之间的购买分配。下表中的权重和供给份额上下限取自游戏文件[1]。最小和最大供给份额仅限制商品的相对权重，而非其最终消费占比。

如果某商品未在市场上出售，则除非该商品设有最小供给份额，否则人口不会购买它。如果某需求类别下的所有商品都未在市场上出售，人口会购买默认商品。

除非另有说明，下表所有商品的默认权重均为 1，最大供给份额为 1，最小供给份额为 0。各类别中的默认商品以**粗体**标示。

| 需求 | 财富等级 |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 赤贫 | 勉强度日 | 贫困 | 小康 | 安稳 | 富足 | 富裕 | 富豪 | 奢华 | 豪奢 |  |  |  |  |
| 1 – 4 | 5 | 6 – 9 | 10 – 14 | 15 – 19 | 20 – 24 | 25 – 29 | 30 | 31 – 39 | 40 – 44 | 45 – 49 | 50 – 59 | 60 + |  |
| 基本食物 | 谷物（20，权重 ×0.85，最大 0.9） 鱼类（20，最大 0.9） 肉类（30，最大 0.9） 水果（30，最大 0.9） 食品杂货（30，权重 ×1.15，最大 0.9） | — |  |  |  |  |  |  |  |  |  |  |  |
| 奢侈食物 | — | 肉类（30，权重 ×1.25，最小 0.1，最大 0.75） 水果（30，权重 ×0.75，最小 0.1，最大 0.75） 食品杂货（30，权重 ×1.5） 糖（30，权重 ×0.5，最大 0.5） |  |  |  |  |  |  |  |  |  |  |  |
| 普通衣物 | 布匹（20，最大 0.5） 衣物（30，权重 ×2） | — |  |  |  |  |  |  |  |  |  |  |  |
| 标准衣物 | — | **衣物**（30） | — |  |  |  |  |  |  |  |  |  |  |
| 粗制物品 | — | 木材（20，最大 0.5） 家具（30，权重 ×2） | — |  |  |  |  |  |  |  |  |  |  |
| 家居用品 | — | 家具（30，最小 0.1，最大 0.75） 玻璃（40，最大 0.5） 纸张（30，权重 ×0.5，最大 0.5） | — |  |  |  |  |  |  |  |  |  |  |
| 奢侈物品 | — | 丝绸（40，权重 ×0.5，最小 0.1，最大 0.25） 奢华衣物（60，最小 0.1，最大 0.5） 奢华家具（60，最小 0.1，最大 0.5） 瓷器（70，最小 0.1，最大 0.5） 收音机（80，最大 0.5） |  |  |  |  |  |  |  |  |  |  |  |
| 供暖 | 木材（20，权重 ×0.75，最大 0.5） 布匹（20，权重 ×0.25，最大 0.25） 煤炭（30，权重 ×2，最大 0.8） 石油（40，权重 ×3） 电力（30，权重 ×3） |  |  |  |  |  |  |  |  |  |  |  |  |
| 致醉品 | 酒类（30，最大 0.75） 烟草（40，权重 ×0.9，最大 0.75） 鸦片（50，权重 ×0.75，最大 0.75） 葡萄酒（50，权重 ×0.25，最大 0.25） |  |  |  |  |  |  |  |  |  |  |  |  |
| 提神品 | — | 糖（30，最大 0.75） 茶叶（50，权重 ×0.95，最大 0.75） 咖啡（50，权重 ×0.95，最大 0.75） 烟草（40，权重 ×0.8，最大 0.75） | — |  |  |  |  |  |  |  |  |  |  |
| 奢侈饮品 | — | 茶叶（50，最大 0.75） 咖啡（50，最大 0.75） 葡萄酒（50，权重 ×0.45，最大 0.33） |  |  |  |  |  |  |  |  |  |  |  |
| 服务 | — | **服务**（30） |  |  |  |  |  |  |  |  |  |  |  |
| 出行自由 | — | 运输（30，最大 0.75） 汽车（100，权重 ×1.25） |  |  |  |  |  |  |  |  |  |  |  |
| 通信 | — | 运输（30，最大 0.75） 电话（70，权重 ×2） |  |  |  |  |  |  |  |  |  |  |  |
| 休闲 | — | 服务（30，权重 ×0.1） 艺术品（200，权重 ×4） 轻武器（60，权重 ×0.75，最大 0.25） 飞机（80，最大 0.2） 汽车（100，最大 0.25） 收音机（80，最大 0.2） 鸦片（50，权重 ×0.5，最大 0.5） 快速帆船（60，最大 0.25） 蒸汽船（70，权重 ×0.75，最大 0.25） |  |  |  |  |  |  |  |  |  |  |  |
| 需求 | 1 – 4 | 5 | 6 – 9 | 10 – 14 | 15 – 19 | 20 – 24 | 25 – 29 | 30 | 31 – 39 | 40 – 44 | 45 – 49 | 50 – 59 | 60 + |
| 赤贫 | 勉强度日 | 贫困 | 小康 | 安稳 | 富足 | 富裕 | 富豪 | 奢华 | 豪奢 |  |  |  |  |
| 财富等级 |  |  |  |  |  |  |  |  |  |  |  |  |  |

## 购买包

一个人口消费的商品总量取决于其财富等级、其规模与劳动力占比，以及每种可替代[商品](Goods.md)的权重系数。

每个财富等级决定了该人口的*购买包*（buy packages），其定义为 10,000 名成年劳动力为满足各类需求所需花费的基础价格金额。这一信息列于 /Victoria 3/game/common/buy_packages/00_buy_packages.txt（另见 [需求#标准人口需求包](Needs.md)）。例如，财富等级 10 的购买包如下所示，并附有注释说明标准 10,000 名成年劳动力需要多少单位的默认商品来满足各项需求。

```
wealth_10 = {
	political_strength = 0.75
	goods = {
		popneed_simple_clothing = 41		# 2.05 units of fabric
		popneed_crude_items = 41		# 2.05 units of wood
		popneed_basic_food = 131		# 6.55 units of grain
		popneed_heating = 26			# 1.3 units of wood
		popneed_household_items = 7		# 0.23 units of furniture
		popneed_standard_clothing = 7		# 0.23 units of clothes
		popneed_services = 23			# 0.77 units of services
		popneed_intoxicants = 50		# 1.67 units of liquor
		popneed_free_movement = 3		# 0.1 units of transportation
		popneed_stimulants = 26			# 0.87 units of sugar
	}
}
```

购买包按人口规模缩放，因此拥有 20,000 名成年劳动力的人口购买的商品价值是拥有 10,000 名成年劳动力的人口的两倍。注意，被抚养人口在需求计算中仅算作半个成年劳动力，因此一个总规模为 10,000 的人口通常购买的商品少于标准购买包。

对于没有替代品的需——例如标准衣物——人口只需每周购买足够数量的商品来满足其购买包即可。

### 替代

本节提供简化示例。详细公式请参见
公式

对于存在替代品的需，人口为某需求购买各商品数量的主要决定因素，是这些商品在国内市场上卖出订单的相对数量，即*市场份额*。此外，某些商品在不同的需求下有不同的定义权重以及份额上下限。最后，基础价格更高的商品只需更少的数量即可满足购买包。例如，在财富等级 10 的供暖需求中，1.3 单位木材或 0.65 单位石油都可以满足需求，因为石油的基础价格是木材的两倍。比较不同商品时需要考虑这些因素。

举一个基本例子，看下面的奢侈饮品需求。它的三种商品具有相同的基础价格和定义权重。对于一个有 200 份茶叶、100 份葡萄酒和 100 份咖啡卖出订单的市场，人口预计会按 2:1:1 的相近比例购买这三种商品。因此在财富等级 22（要求价值 100 的奢侈饮品）时，一个人口会购买 1 份茶叶、0.5 份葡萄酒和 0.5 份咖啡，并按人口规模缩放。由于每种商品的最大份额为 75%，其市场权重被限制在 0.75，因此如果卖出订单为 400 份茶叶、50 份葡萄酒和 50 份咖啡，预计购买量约为 ~1.58 单位茶叶以及各 ~0.21 单位的葡萄酒和咖啡——而不是各 1.6 和 0.2。然而，如果市场上只出售一种奢侈饮品商品，它将被独家购买，因为没有任何一种商品设有最小份额。同样，如果市场上所有商品都未出售，则会独家购买默认商品——茶叶。

```
popneed_luxury_drinks = {
	default = tea
	entry = {
		goods = tea
		weight = 1
		max_supply_share = 0.75
		min_supply_share = 0.0
	}
	entry = {
		goods = coffee
		weight = 1
		max_supply_share = 0.75
		min_supply_share = 0.0
	}
	entry = {
		goods = wine
		weight = 1
		max_supply_share = 0.75
		min_supply_share = 0.0
	}
}
```

当商品具有不同的定义权重时，该权重会与市场份额相乘。例如，在一个有 200 份布匹和 100 份衣物卖出订单的市场中，人口会按相等比例购买这两种商品来满足普通衣物需求，因为衣物在该类别中权重为 ×2。不过，由于衣物的基础价格也更高，购买的单位数量会更少。但请注意，布匹的权重不能高于 0.5，因此实际上会购买更高比例的衣物。

设有最小份额的商品，例如奢侈物品中的奢华家具，即使该商品未在市场上出售也总是会被购买。

相对替代关系可以逐周变化，但每周的变化被限制在 1% 到 10% 之间[2]。这意味着某商品市场份额的大幅变动不会立即反映在人口消费上。

#### 偏好与禁忌

[文化偏好](Culture.md)和[宗教禁忌](Religion.md)会影响人口对相应商品的权重。偏好将商品的最小权重设为 1，并将其总权重乘以 ×2；禁忌则将商品的需求乘以 ×0.5。此外，偏好和禁忌都会使包含该商品的需总值变化 ±25%。例如，如果某文化偏好服务，那么在财富等级 10 时该文化的人口会购买价值 30 的服务，而不是基础的 24。类似地，如果某宗教对服务有禁忌，该宗教的人口会购买价值 18 的服务而非 24。这一修正后的数值会从其他需的价值中扣除或分配过来，以使该财富等级的总购买包保持不变。

在游戏过程中，文化有小概率发展出新的偏好。这要求该文化在某个[市场](Market.md)中拥有至少 50,000 人口，且该市场中此商品的供给至少达到需求的 50%，同时市场对该商品的需求至少为 £500（计算方式为数量 ∗ ∗ 基础价格 {\displaystyle {\text{number of units}}*{\text{base price}}} ![{\displaystyle {\text{number of units}}*{\text{base price}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/5db740e5ee1f6da09bdc84a38c62661286953f01)）。供给增加（最高至需求的 3 倍）以及市场规模增大会提高这一概率。可以利用贸易路线尝试让其他文化对玩家国家生产的商品产生偏好。某些事件也可能创造或消除偏好。

相比之下，禁忌是固定设定的，不会改变。

### 威望商品

威望商品会按其在市场中的份额直接成比例地增加该商品类型的权重。例如，如果某威望商品占市场份额的 50%，则其权重增加 50%。

### 农民

农民仅购买购买包数量的 5%。[3]这意在表现其自给自足的生活方式，他们转而通过一种称为“自给产出（subsistance Output）”的商品包获得报酬，该商品包不与更广泛的经济互动。

### 被抚养人口

要计算某人口的需求，必须分别知道其劳动力和被抚养人口的规模，而不仅仅是人口总规模。被抚养人口的消费量是成年劳动力的一半。被抚养人口与劳动力的默认比例为 3:1（75% 被抚养人口，25% 成年劳动力）[4]，但在游戏中会受到法律和其他因素的影响。举例来说，一个 10,000 人的人口默认有 2,500 名成年劳动力和 7,500 名被抚养人口[5]。在需求计算中，这等价于一个拥有 6,250 名成年劳动力且没有被抚养人口的人口。在这个例子中，成年劳动力占需求的 40%，而被抚养人口占 60%。

### 公式

购买包和替代的精确公式如下：

购买单位数 = 购买包价值 商品基础价格 ⋅ ⋅ 商品购买权重 ∑ ∑ 所有商品购买权重之和 ⋅ ⋅ 劳动力规模 + 被抚养人口规模 ⋅ ⋅ 0.5 10000 {\displaystyle {\text{num of units purchased}}={\frac {\text{buy package value}}{\text{base price of good}}}\cdot {\frac {\text{purchase weight of good}}{\sum {\text{purchase weight of all goods}}}}\cdot {\frac {{\text{workforce size}}+{\text{dependent size}}\cdot 0.5}{10000}}} ![{\displaystyle {\text{num of units purchased}}={\frac {\text{buy package value}}{\text{base price of good}}}\cdot {\frac {\text{purchase weight of good}}{\sum {\text{purchase weight of all goods}}}}\cdot {\frac {{\text{workforce size}}+{\text{dependent size}}\cdot 0.5}{10000}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/73a55bd06626f113e40df86f8ee1d5cf7431d046)

购买权重是某商品满足某需求的相对比例；这不是百分比，而是一个直接数值。最小和最大供给份额是对市场份额的限制，若市场份额超出该范围则不再产生影响。最终的购买百分比基于购买包中所有商品的总权重。

商品购买权重 = 权重 ⋅ ⋅ ( 最小供给份额 < 商品市场份额 < 最大供给份额 ) {\displaystyle {\text{purchase weight of good}}={\text{weight}}\cdot ({\text{min supply share}}<{\text{market share of good}}<{\text{max supply share}})} ![{\displaystyle {\text{purchase weight of good}}={\text{weight}}\cdot ({\text{min supply share}}<{\text{market share of good}}<{\text{max supply share}})}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/2737f7cadeeb23c4721b8e37f18c0b253e427aac)

市场份额由卖出订单数量减去非人口买入订单数量的一半来确定[6]。

商品市场份额 = 商品卖出订单 − − ( 非人口买入订单 ⋅ ⋅ 0.5 ) ∑ ∑ ( 该需求所有商品的卖出订单 − − ( 非人口买入订单 ⋅ ⋅ 0.5 ) ) {\displaystyle {\text{market share of good}}={\dfrac {{\text{sell orders of good}}-({\text{non-pop buy orders}}\cdot {0.5})}{\sum ({\text{sell orders of all goods for need}}-({\text{non-pop buy orders}}\cdot {0.5}))}}} ![{\displaystyle {\text{market share of good}}={\dfrac {{\text{sell orders of good}}-({\text{non-pop buy orders}}\cdot {0.5})}{\sum ({\text{sell orders of all goods for need}}-({\text{non-pop buy orders}}\cdot {0.5}))}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/93c5d8b00c64a0db1db9604ed86bce556db894a3)

仅限本地的商品会获得额外权重，等于 0.25 ⋅ ⋅ ( 1 − − 州占市场 GDP 百分比 ) {\displaystyle 0.25\cdot (1-{\text{State's percentage of market GDP}})} ![{\displaystyle 0.25\cdot (1-{\text{State's percentage of market GDP}})}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/55822280a569002acaef26166a71a3f0f8b7a475)。例如，在一个占市场 GDP 20% 的州中，本地商品会获得 0.2 的额外权重。

## 标准人口需求包

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新本节内容。本节最后针对版本 1.10 进行验证。 |
|---|---|

需求可根据人口财富绘制成图。总体而言，它们可分为三类：*临时需求*、*恒定需求*和*指数需求*。
### 临时需求

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助验证或更新此图片。它最后针对版本 1.10 进行过验证。 |
|---|---|

临时需求对应财富等级 1 - 60
临时需求在某个财富等级出现，增长到一定程度（通常呈线性），随后逐渐减少直至消失，或突然消失。

临时需求包括：

- **基本食物**（财富等级 1 时起始值为 90，在财富等级 19 达到最大值 168，财富等级 29 之后消失）
- **简朴衣物**（财富等级 1 时起始值为 23，在财富等级 9 达到最大值 43，财富等级 14 之后消失）
- **标准衣物**（财富等级 10 时起始值为 7，在财富等级 25-39 达到最大值 161，财富等级 39 之后消失）
- **粗糙制品**（财富等级 5 时起始值为 13，在财富等级 9 达到最大值 43，财富等级 14 之后消失）
- **家庭用品**（财富等级 10 时起始值为 7，在财富等级 31-44 达到最大值 238，财富等级 44 之后消失）
- **刺激性物品**（财富等级 6 时起始值为 7，在财富等级 23 达到最大值 56，财富等级 30 之后消失）

### 恒定需求

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助验证或更新此图片。它最后针对版本 1.10 进行过验证。 |
|---|---|

恒定需求对应财富等级 1 - 60
恒定需求在某个财富等级出现，增长到一定程度（相当线性），随后在所有更高的财富等级上保持其最大值不变。

恒定需求包括：

- **取暖**（财富等级 9 短暂达到峰值后，在财富等级 10 达到恒定值 26）
- **致醉品**（在财富等级 30 达到恒定值 216）

### 指数需求

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助验证或更新此图片。它最后针对版本 1.10 进行过验证。 |
|---|---|

指数需求对应财富等级 1 - 60
指数需求在某个财富等级出现并持续增长，起初缓慢，随后越来越快（即呈指数式）。

指数需求包括：

- **奢侈食物**（财富等级 20 起始值为 8，财富等级 60 达到 3,859）
- **奢侈品**（财富等级 15 起始值为 11，财富等级 60 达到 9,648）
- **奢侈饮品**（财富等级 15 起始值为 21，财富等级 60 达到 3,859）
- **服务**（财富等级 10 起始值为 24，财富等级 60 达到 6,561）
- **自由出行**（财富等级 10 起始值为 3，财富等级 60 达到 3,859）
- **通信**（财富等级 20 起始值为 16，财富等级 60 达到 3,859）
- **休闲**（财富等级 20 起始值为 16，财富等级 60 达到 9,648）

## 参考资料

1. ↑ /Victoria 3/game/common/pop_needs/00_pop_needs.txt
2. ↑ 参见 /Victoria 3/game/common/defines/00_defines.txt 中的 `MAX_DEMAND_ADJUSTMENT_BASE_AMOUNT`、`MAX_DEMAND_ADJUSTMENT_SCALED_AMOUNT` 和 `MAX_DEMAND_ADJUSTMENT_SCALE`。
3. ↑ /Victoria 3/game/common/pop_types/peasants.txt 中的 `consumption_mult`
4. ↑ /Victoria 3/game/common/defines/00_defines.txt 中的 `WORKING_ADULT_RATIO_BASE`
5. ↑ /Victoria 3/game/common/defines/00_defines.txt 中的 `DEPENDENT_CONSUMPTION_RATIO`
6. ↑ 公式中“非人口购买订单”这一要素由 Reddit 用户 banjo_martian 发现 [Reddit Post by u/banjo_martian in November '22](https://www.reddit.com/r/victoria3/comments/yudc80/pop_needs_consumer_good_substitution_and_why_oil/)

游戏概念
返回顶部
| 人口 | [人口](Pops.md) • [接受度](Acceptance.md) • [文化](Culture.md) • [迁移](Migration.md) • 需求 • [职业](Profession.md) • [宗教](Religion.md) • [生活水平](Standard of living.md) |
|---|---|

| 政府 | [政府](Government.md) • [能力](Capacity.md) • [人物](Character.md) • [法令](Decrees.md) • [机构](Institutions.md) • [法律](Laws.md) • [技术](Technology.md) |
|---|---|

| 政治 | [选举](Elections.md) • [意识形态](Ideology.md) • [利益集团](Interest group.md) • [政治游说](Political lobby.md) • [政治运动](Political movement.md) • [政党](Political party.md) • [革命](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| 经济 | [建筑](Building.md) • [商品](Goods.md) • [收成状况](Harvest condition.md) • [基础设施](Infrastructure.md) • [市场](Market.md) • [生产方式](https://vic3.paradoxwikis.com/Production_methods) • [州](State.md) • [国库](Treasury.md) |
|---|---|

| 外交 | [外交](Diplomacy.md) • [外交行动](https://vic3.paradoxwikis.com/Diplomatic_action) • [外交博弈](Diplomatic play.md) • [强权集团](Power bloc.md) • [等级](Rank.md) • [附属国](Subject.md) • [条约](Treaty.md) |
|---|---|

| 战争 | [战争](Warfare overview.md) • [陆战](Land warfare.md) • [海战](Naval warfare.md) • [战争目标](https://vic3.paradoxwikis.com/Wargoal) • [征兵](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| 其他 | [国家](Countries.md) • [决策](Decision.md) • [事件](Events.md) • [日志](Journal.md) • [目标](Objective.md) • [维基百科（Vickypedia）](Vickypedia.md) |
|---|---|