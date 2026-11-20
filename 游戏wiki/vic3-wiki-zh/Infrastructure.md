---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Infrastructure
source: https://vic3.paradoxwikis.com/Infrastructure
pageid: 2922
categories: [1.13, Game_concepts]
fetched: 2026-10-27
---
本文已针对当前游戏[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行验证。

关于跨海运送商品的消耗，参见
convoys
。
州概览界面上的基础设施与市场接入。
**基础设施**模拟了陆路运输商品的成本，以及为支撑大规模工业化所需打造的基础条件。

要实现一个州的工业化，仅仅建造重工业并拥有可供雇佣的人口是不够的。玩家还需要确保有足够的基础设施来支撑这些产业。

基础设施与多种机制相关联，例如市场接入、军事后勤以及迁移等。

## 基础设施来源

基础设施由众多来源提供和修正。所有州都拥有 **+3** 点基础基础设施。

### 人口

| 来源 | 数量 | 上限 |
|---|---|---|
| 首都 | **+0.1** | **+20** |
| 沿海州 | **+0.05** | **+10** |
| 城市化 | **+2** | **+40** |
| 城市规划 | **+1** | **+20** |
| 现代下水道 | **+1** | **+20** |
| 钢框架建筑 | **+1** | **+20** |
| 电梯 | **+1** | **+20** |
| 道路养护 | **+1** | **+20** |
| 运输基础设施 I | **+33%** | **+33%** |
| 贸易联盟的强权集团雕像 | **+10%** | — |
| 各类[公司](Companies.md)的繁荣加成 | 不定 | 不定 |

一旦研究了特定的[社会技术](https://vic3.paradoxwikis.com/Society_technologies)，所有州都会从本州人口规模中获得一些基础设施。相关技术位于社会技术树中以城市化开端的分支。以这种方式获得的基础设施数量可以在州面板信息标签页中基础设施数值的工具提示里查看，在那里被称为*"每 10 万人口提供的基础设施"*。它基于居住在该州的人口个体数量（包括[受抚养者](Pops.md)，并受到同样这些技术的上限约束，公式为：[1]

State Infra. from Pop. = min ( population size ⋅ ⋅ Infra. per 100K Pop. (modifier) 100,000 , Max Infra. from Pop. ) {\textstyle {\text{State Infra. from Pop.}}=\min({\dfrac {{\text{population size}}\cdot {\text{Infra. per 100K Pop. (modifier)}}}{\text{100,000}}},{\text{Max Infra. from Pop.}})} ![{\textstyle {\text{State Infra. from Pop.}}=\min({\dfrac {{\text{population size}}\cdot {\text{Infra. per 100K Pop. (modifier)}}}{\text{100,000}}},{\text{Max Infra. from Pop.}})}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/2389a91f0bc26c8bd897d94c9ba75128e3883014)

几乎所有国家（包括许多未中央集权化国家）在开局时都已研究至少第一项相关技术，因此都拥有一定来自人口的基础设施。注意，州的 UI 工具提示中显示的确切数值会向下取整到一位小数。

### 汽车消费

人口每消费一单位汽车，就为该州提供 **+0.25** 点基础设施。研究铺装道路后，这一数值提升至每消费一单位共 **+0.5** 点。

### 州修正

参见：
州特质
如上所述，沿海州能增加来自人口的基础设施，并拥有建造港口的能力。对于分裂州而言，仅该州区域是沿海的还不够，分裂出的部分必须包含至少一个可通行的沿海省份。[2] 湖泊不计入沿海，因此毗邻美国/加拿大五大湖、里海、咸海，或者——按游戏内说法——哈德逊湾的州也不被视为沿海州。

许多州拥有增加或减少基础设施的特质。拥有重要水道的州，例如密西西比河或莱茵河流域，获得固定的基础设施加成；而地形崎岖的州，例如山脉、沙漠或显著森林地区，则受到百分比的基础设施惩罚。

*道路养护*法令额外提供 **+1** 来自人口的基础设施和 **+20** 来自人口的基础设施上限，这有助于抵消动荡或破坏带来的临时惩罚，或在建造更多铁路之前补充基础设施。

未合并州受到 **−25%** 的基础设施惩罚。破坏会按其存在的比例相应减少基础设施。尤其是在未合并州或拥有减少基础设施特质的州中，这可能导致 **100%** 的基础设施惩罚，实际上使该州与更广阔的市场隔绝。

一国的首都如上所述会增加来自人口的基础设施，且其市场首都所在的州获得 **+25%** 基础设施。

### 建筑

某些建筑为其所在的州提供基础设施。所提供的基础设施数量随建筑等级和就业规模而变化。

**港口**

港口除第一种[生产方式](Production method.md)外，都能提供少量基础设施。在游戏早期铁路出现之前，这有助于在沿海州获得一些额外的基础设施，但其提供量与铁路相比较低，每等级至多 **+5**，且这并非港口的主要用途，因此效率不高，尤其是在铁路可用之后。

**铁路**

铁路是提升州基础设施的首要且最高效的方式。除基础设施外，铁路还生产运输服务，用于某些生产方式，同时也是一种[人口需求](Needs.md)。最初，铁路每等级提供 **+20** 点基础设施，通过更先进的列车生产方式，这一数值可提升至每等级 **+40**，或者在使用由强权集团原则“运输基础设施 III”解锁的联合柴油列车生产方式时达到每等级 **+55**。

**城市中心**

城市中心可以产出极少量的基础设施，每等级仅 **+1** 或 **+2**；不过，这比铁路或港口更廉价，只需要少量的煤炭或电力，而非更昂贵的发动机、快速帆船或轮船，且不需要建造时间。

### 其他

某些事件会提供基础设施的加成或惩罚——通常是临时的；若干[公司](Companies.md)的繁荣加成也会提供额外的直接基础设施；乡民的忠诚特质“农夫市场”在所有拥有的州提供 **+10%** 基础设施；强权集团原则市场统一 I 与内部贸易 I 各自在所有集团成员的州提供 **+10%** 基础设施。

## 基础设施使用量

一个州的基础设施使用量由该州建筑的类型和等级决定。一般来说，建筑越是城市化、专业化，每等级使用的基础设施就越多。例如，化肥厂每等级使用 3 点基础设施，而黑麦农场每等级仅使用 1 点。

同一大类下的大多数建筑有典型的基础设施使用量：

- [农业建筑、种植园](Building.md)以及除矿山外的[资源建筑](Building.md)每等级使用 **1** 点，金矿场除外，它不使用基础设施。
- [政府行政](https://vic3.paradoxwikis.com/Government_Administration)、[大学](https://vic3.paradoxwikis.com/University)和纪念碑每等级使用 **1** 点。
- [矿山](https://vic3.paradoxwikis.com/Mines)和油井每等级使用 **2** 点。
- [工厂](https://vic3.paradoxwikis.com/Factories)每等级使用 **1.5**（轻工业）、**2**（军事工业）或 **2.5**（重工业）点。
- 发电厂每等级使用 **2** 点。
- [军事建筑](Building.md)每等级使用 **0.2** 点，陆军与海军后勤中心除外，它们每等级使用 **0.1** 点。
- [建造部门](https://vic3.paradoxwikis.com/Construction_sectors)每等级使用 **2** 点基础设施。

[城市中心](https://vic3.paradoxwikis.com/Urban_centers)不使用基础设施，游戏早期平均使用量倾向于每等级约 **1** 点，随着更多重工业建成，会趋向于每等级约 **2** 点。

## 市场接入

参见：
市场价格
市场接入表示一个州与本国市场连接的顺畅程度。它最初由基础设施除以基础设施使用量简单计算得出。如果该州的基础设施高于基础设施使用量，其市场接入为 **100%**，但如果使用量超过可用基础设施，市场接入将按比例减少。例如，如果一个州的基础设施为 **45**，使用量为 **90**，则其市场接入至多为 **50%**。在市场首府海外（隔海相望）的州还需要[航运线](https://vic3.paradoxwikis.com/Shipping_lanes)和护航舰队；因此，海外州的市场接入也受补给网络强度限制，即便基础设施充足也可能下降。类似地，因任何原因而被隔绝的州，市场接入为 0。

市场接入以两种方式影响州与本国市场的互动：首先，减少该州加入本国市场的买卖订单量；其次，降低对本地价格的[市场接入价格影响](https://vic3.paradoxwikis.com/Market_price)（MAPI）。总体而言，低市场接入对州内的本地价格以及本国市场的市场价格都有负面影响。因此，在所有州维持良好的市场接入对健康的经济十分重要。

举例说明，假设某州生产 **100** 单位铁和 **0** 单位工具，消费 **0** 单位铁和 **50** 单位工具。在 **50%** 市场接入下，只有 **50** 单位铁的卖出订单和 **25** 单位工具的买入订单会加入本国市场。此外，铁的“绝对”本地价格将是基础价格（£10）的 25%，工具则是基础价格（£70）的 175%。MAPI 通过采用一定百分比的市场价格和剩余百分比的绝对本地价格来缓和这一影响。然而，MAPI 本身也要乘以市场接入，因此在 **50%** 市场接入下，只有通常价格缓和效果的 50% 会生效。

## 其他影响

一个州的基础设施数量还会影响其他一些游戏机制。

### 迁移

参见：
迁移
基础设施低的州迁移潜力（无论是迁入还是迁出）降低。具体而言，每点基础设施每周最多只能有 5 个个体迁入或迁出该州。[3]

### 战斗宽度

战斗宽度受州的基础设施（以及省份地形）限制，公式为 Max width = ( 5 + Infrastructure 2 ) ∗ ∗ Terrain multiplier {\displaystyle {\text{Max width}}=(5+{\tfrac {\text{Infrastructure}}{2}})*{\text{Terrain multiplier}}} ![{\displaystyle {\text{Max width}}=(5+{\tfrac {\text{Infrastructure}}{2}})*{\text{Terrain multiplier}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/70172ebd1ed6e7959a8ccf49592c616a1eed5138)[4]。

例如，在一个拥有 20 点基础设施的州，森林省份（0.6 修正系数）的最大战斗宽度为 ( 5 + 20 2 ) ∗ ∗ 0.6 = 15 ∗ ∗ 0.6 = 9 {\displaystyle (5+{\tfrac {20}{2}})*0.6=15*0.6=9} ![{\displaystyle (5+{\tfrac {20}{2}})*0.6=15*0.6=9}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/5c4d45c2f85f2906a350905b866e8fcc749c04a7)。

### 占领进度

每点基础设施*使用量*都会影响战斗后获得的占领进度，其方式是限制危险、森林和高原地形对占领成本的影响[5]。

## 参考

1. ↑ 100000 是 /Victoria 3/game/common/defines/00_defines.txt 中定义的值：`INDIVIDUALS_PER_POP_INFRASTRUCTURE`。
2. ↑ 例如西伯利亚诸州和加拿大北极诸州拥有不可通行的沿海省份。
3. ↑ 来自 /Victoria 3/game/common/defines/00_defines.txt：`MIGRATION_MAX_PER_STATE_INFRASTRUCTURE = 5`
4. ↑ 公式参见 /Victoria 3/game/common/script_values/command_values.txt 中的 `province_terrain_infrastructure_force_limit`，地形修正系数参见 /Victoria 3/game/common/terrain/01_terrain.txt
5. ↑ 详情参见 /Victoria 3/game/common/script_values/occupation_values.txt

游戏概念
返回顶部
| 人口 | [人口](Pops.md) • [接受度](Acceptance.md) • [文化](Culture.md) • [迁移](Migration.md) • [需求](Needs.md) • [职业](Profession.md) • [宗教](Religion.md) • [生活水平](Standard of living.md) |
|---|---|

| 政府 | [政府](Government.md) • [容量](Capacity.md) • [人物](Character.md) • [法令](Decrees.md) • [机构](Institutions.md) • [法律](Laws.md) • [技术](Technology.md) |
|---|---|

| 政治 | [选举](Elections.md) • [意识形态](Ideology.md) • [利益集团](Interest group.md) • [政治游说](Political lobby.md) • [政治运动](Political movement.md) • [政党](Political party.md) • [革命](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| 经济 | [建筑](Building.md) • [商品](Goods.md) • [收成状况](Harvest condition.md) • 基础设施 • [市场](Market.md) • [生产方式](https://vic3.paradoxwikis.com/Production_methods) • [州](State.md) • [国库](Treasury.md) |
|---|---|

| 外交 | [外交](Diplomacy.md) • [外交行动](https://vic3.paradoxwikis.com/Diplomatic_action) • [外交博弈](Diplomatic play.md) • [强权集团](Power bloc.md) • [等级](Rank.md) • [附属国](Subject.md) • [条约](Treaty.md) |
|---|---|

| 战争 | [战争](Warfare overview.md) • [陆地战争](Land warfare.md) • [海战](Naval warfare.md) • [战争目标](https://vic3.paradoxwikis.com/Wargoal) • [征兵](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| 其他 | [国家](Countries.md) • [决议](Decision.md) • [事件](Events.md) • [日志](Journal.md) • [目标](Objective.md) • [维多利亚百科](Vickypedia.md) |
|---|---|