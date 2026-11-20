---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Production method
source: https://vic3.paradoxwikis.com/Production_method
pageid: 1645
categories: [1.13, Economy]
fetched: 2026-10-27
---
本文已针对游戏的当前 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

经济
建筑
建筑列表
•
独特建筑
公司
•
风味公司
市场
商品
•
需求
生产方式
生产方式列表
国库
建筑面板提供了玩家国家中建筑及其相关生产方式的详细概要。

**生产方式**（Production methods）代表[建筑](Building.md)的运作模式。生产方式决定了建筑需要和产出哪些[商品](Goods.md)与[容量](https://vic3.paradoxwikis.com/Capacities)）以及一般效果，还决定了建筑雇用多少以及哪些[职业](Profession.md)的人口。

许多生产方式代表生产建筑主要商品的更先进技术，但其他生产方式则代表替代性生产，例如奢侈品与大宗商品之分，或者组织方式之分，例如世俗行政人员与神职行政人员。

同一州中某建筑的所有等级必须使用相同的生产方式，但全国各地的不同建筑可以使用任意生产方式组合。在建筑标签页中可以一次性在全国范围内更改生产方式。

## 生产方式组

生产方式按照每种建筑的一个或多个组进行分类。每组对给定建筑始终只有一个激活的生产方式。在不同建筑之间，相似的组通常具有相同的图标颜色，但也有些生产方式组不遵循这一规律。以下是几种最常见的生产方式组类型：

- *基础*——棕色图标。决定建筑的主要投入和产出商品，通常也决定建筑的基础劳动力。更先进的基础生产方式通过技术解锁，会增加投入和产出商品，且通常还需要[受教育程度更高](https://vic3.paradoxwikis.com/Qualifications)的[工人](Profession.md)。某些建筑（如食品工业）拥有多个基础生产方式，可以显著增加主要商品的产出。
- *次级*——紫色图标。以减少主要产出为代价增加次级产出商品，也可能需要次级投入，还可能少量增加劳动力。
- *自动化*——绿色图标。以额外的投入商品为代价减少建筑的非技能劳动力。
- *组织*——蓝色图标。代表组织方式，决定政府和所有权建筑的大部分劳动力。
- *军事*——红色图标。决定兵营、征兵中心和海军基地使用的训练与学说。

### 生产方式需求

虽然每种建筑的每组生产方式至少有一个可用，但许多生产方式在满足特定条件之前处于锁定状态，无法使用。最常见的条件是研究某项[技术](Technology.md)，但也可能包括颁布某些[法律](Laws.md)，甚至激活另一个生产方式。有些生产方式甚至要求该州或市场中生产某些商品。

最后，[独特建筑](https://vic3.paradoxwikis.com/Unique_buildings)的生产方式由[游戏规则](https://vic3.paradoxwikis.com/Game_rules)定义，即独特建筑是开启、关闭还是设为"仅威望"模式。

如果激活的生产方式的需求不再满足，它会自动切换到同组中第一个有效的生产方式。

## 生产方式效果

每种生产方式都可以影响其所在建筑、建筑所在的州或整个国家。此外，效果可以是固定数值，也可以按建筑等级或雇用劳动力数量进行缩放。

等级缩放修正量随该建筑等级的提高而增强，与建筑的就业人数无关。例如，建筑的工人数量始终是等级缩放的建筑修正量，这意味着生产方式为建筑的每个等级增加一定数量的工人。

劳动力缩放修正量同时取决于建筑等级和就业率，通常还受[吞吐量](https://vic3.paradoxwikis.com/Throughput)影响，吞吐量会按额外百分比增强效果。投入和产出商品通常是劳动力缩放的建筑修正量。

非缩放修正量不随建筑等级或就业数量变化而变化。一个常见的例子是所有权份额。

### 污染

大多数生产方式都会产生污染，污染会降低州的迁移吸引力、人口的生活水平，并提高人口死亡率。重工业污染最重，农业污染最轻。每个州区域的污染影响每日向*污染影响目标*变化 0.255，公式如下：

Pollution impact target = Total pollution generation 50 + 1.5 ⋅ ⋅ Arable Land ⋅ ⋅ 1 255 {\displaystyle {\text{Pollution impact target}}={\dfrac {\text{Total pollution generation}}{50+1.5\cdot {\sqrt {\text{Arable Land}}}}}\cdot {\frac {1}{255}}} ![{\displaystyle {\text{Pollution impact target}}={\dfrac {\text{Total pollution generation}}{50+1.5\cdot {\sqrt {\text{Arable Land}}}}}\cdot {\frac {1}{255}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/7e8101452da56295469b45d9e710ffc14fd136a9)

每 **1%** 污染影响具有以下基础效果：

- **−0.25%** 迁移吸引力，
- **+0.5%** 干旱、洪水、野火和热浪影响，
- **−0.03** 生活水平，
- **+0.5%** 死亡率。

对生活水平和死亡率的影响可以通过卫生系统机构（每级 **−10%**；公共医疗保险 **−15%**）以及现代下水道技术（**−10%**）来降低。州区域还有一个最低污染目标，等于污染最重的相邻州区域污染目标的 25%。

污染适用于整个州区域。

## 管理生产方式

为了便于管理国家中不同的建筑（及其相关的生产方式），玩家可以参考[建筑面板](User interface.md)。

该面板提供了全国所有建筑的概览，让玩家可以一目了然地了解这些产业的财务状况。建筑按类型分组，可展开查看各州中的单个建筑，点击每座建筑可以深入了解其资产负债表和劳动力情况。此外，该面板还允许调整单个建筑的生产方式，或将全国范围内某一建筑类型的所有生产方式设置为特定配置。

预测性提示会解释生产、消费和工资需求变化对建筑收支的预期影响，以及就业变化（哪些新工作岗位将被创造、哪些将消失），这些变化随着时间的推移还可能影响国家政治。如果没有足够符合资质的人口来填补新创造的任何职业，系统会发出警告，因为这会限制建筑的招聘能力。

## 参考

游戏概念
返回顶部
| 人口 | [人口](Pops.md) • [接纳度](Acceptance.md) • [文化](Culture.md) • [迁移](Migration.md) • [需求](Needs.md) • [职业](Profession.md) • [宗教](Religion.md) • [生活水平](Standard of living.md) |
|---|---|

| 政府 | [政府](Government.md) • [容量](Capacity.md) • [人物](Character.md) • [法令](Decrees.md) • [机构](Institutions.md) • [法律](Laws.md) • [技术](Technology.md) |
|---|---|

| 政治 | [选举](Elections.md) • [意识形态](Ideology.md) • [利益集团](Interest group.md) • [政治游说](Political lobby.md) • [政治运动](Political movement.md) • [政党](Political party.md) • [革命](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| 经济 | [建筑](Building.md) • [商品](Goods.md) • [收成状况](Harvest condition.md) • [基础设施](Infrastructure.md) • [市场](Market.md) • [生产方式](https://vic3.paradoxwikis.com/Production_methods) • [州](State.md) • [国库](Treasury.md) |
|---|---|

| 外交 | [外交](Diplomacy.md) • [外交行动](https://vic3.paradoxwikis.com/Diplomatic_action) • [外交博弈](Diplomatic play.md) • [强权集团](Power bloc.md) • [等级](Rank.md) • [附属国](Subject.md) • [条约](Treaty.md) |
|---|---|

| 战争 | [战争](Warfare overview.md) • [陆战](Land warfare.md) • [海战](Naval warfare.md) • [战争目标](https://vic3.paradoxwikis.com/Wargoal) • [征兵](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| 其他 | [国家](Countries.md) • [决策](Decision.md) • [事件](Events.md) • [日志](Journal.md) • [目标](Objective.md) • [维基百科](Vickypedia.md) |
|---|---|