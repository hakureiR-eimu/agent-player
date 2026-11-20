---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Capacity
source: https://vic3.paradoxwikis.com/Capacity
pageid: 1639
categories: [1.13, Game_concepts]
fetched: 2026-10-27
---
本文已针对游戏当前 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

容量（Capacities），即游戏的“货币”，显示在国旗附近的左上角。
**容量**（Capacities）是游戏中四种主要“货币”中的三种（第四种是金钱）。每种容量代表国家治理能力的一个特定领域，并仅用于与该领域相关的事务。

## 生成与消耗

容量并非 pooled 类型的资源，而是持续地生成与消耗。不同容量的生成方式与用途各不相同，详见以下各节。一般来说，某些[社会技术](Society technology.md)会提供容量百分比的提升，某些满意度高的利益集团、某些[奇观](https://vic3.paradoxwikis.com/Monuments)以及一些事件修正（modifier）也会提供加成。所有国家每种容量的基础值为 **+100**。

除了直接用途之外，若生成超过消耗（即*盈余*），每种容量都会提供收益；若消耗超过生成（即*赤字*），则会带来惩罚。盈余的收益或赤字的惩罚会按其相对于该容量总生成量的比例进行缩放：当消耗为生成量的一半或以下时收益达到最大，当消耗为生成量的两倍或以上时惩罚达到最大。例如，一个生成量为 **100** 的容量，当消耗为 **50** 或以下时达到完全盈余；反之，当消耗为 **200** 或以上时达到完全赤字。

大多数需要一定容量的行动，只有在当前拥有足额容量时才能执行；不过，大多数行动不会因赤字而被自动取消。

## 容量类型

### 行政力

行政力（Bureaucracy）代表国家征税、运营机构以及雇用将军和海军上将的能力。它由[政府行政](https://vic3.paradoxwikis.com/Government_administration)建筑生成。小资产阶级的*中层管理者*特质可提供额外 **+10%**，若其势力强大则为 **+20%**。

行政力的用途如下：

- 已整合州（Incorporated states）——基础 **10**，每 25,000 人口额外 **1**；整合州时也会产生此项消耗，即使整合的全部收益尚未生效。
- [机构](Institutions.md)——已整合州中每 100,000 人口每级 **1**，每级最低为 **10**。
- [建筑](https://vic3.paradoxwikis.com/Buildings)——每国有等级 **1**。
- [将军](https://vic3.paradoxwikis.com/Generals)和[海军上将](https://vic3.paradoxwikis.com/Admirals)——基础 **10**，每晋升一级 **5**，上限 **30**。
- 以及某些[日志条目](https://vic3.paradoxwikis.com/Journal_entries)或事件，例如[勘测苏伊士运河](Unique building.md)。

行政力赤字称为*行政超载*（Administrative Overburden），完全赤字时的效果上限为：

- +100% 政府分红浪费
- +100% 税收浪费

行政力盈余称为*高效行政*（Efficient Bureaucracy），完全盈余时的效果上限为：

- +10% 本州建造效率

### 权威力

权威力（Authority）代表国家元首通过法令在 国内实施变革的个人权力与能力。它由国家的[法律](Laws.md)生成——一般来说，国家越是压制性与威权性强，生成的权威力就越多。国家的统治者也会按其声望生成或削减权威力（例如声望为 50 的统治者在任期间生成 +50 权威力）。

通过[社会技术](Society technology.md)可获得额外 **+50%** 权威力（大众传播、民族主义、泛民族主义、政治鼓动和大众宣传各提供 **+10%**）。虔信派的高满意度特质*君权神授*也提供 **+10%** 权威力，若其势力强大则为 **+20%**。

**影响权威力的法律**

| 治理原则 |  |
|---|---|
| 君主制 | **+200** |
| 神权制 | **+200** |
| 酋长制 | **+100** |
| 社会君主制 | **+100** |
| 法团国家 | **+100** |
| 总统共和制 | **+100** |
| 殖民地行政 | **+100** |
| 议会共和制 | **0** |
| 委员会共和制 | **0** |

| 权力分配 |  |
|---|---|
| 一党制国家 | **+250** |
| 新绝对主义 | **+250** |
| 独裁制 | **+200** |
| 长老议事会 | **+200** |
| 幕府 | **+200** |
| 技术官僚制 | **+100** |
| 寡头制 | **+100** |
| 有机规制 | **+100** |
| 土地投票制 | **+100** |
| 财富投票制 | **+100** |
| 有限选举权 | **+50** |
| 普选制 | **0** |
| 无政府状态 | **−50%** |

| 政教关系 |  |
|---|---|
| 国教 | **+200** |
| 米勒特制 | **+200** |
| 圣典之民 | **+200** |
| 国家无神论 | **+200** |
| 信仰自由 | **+100** |
| 政教完全分离 | **0** |

| 公民权 |  |
|---|---|
| 单一民族国家 | **+200** |
| 民族至上 | **+150** |
| 种族隔离 | **+100** |
| 臣属制 | **+100** |
| 文化排斥 | **+50** |
| 多元文化主义 | **0** |

| 经济体制 |  |
|---|---|
| 计划经济 | **+25%** |
| 其他经济法律 | — |

| 贸易政策 |  |
|---|---|
| 孤立主义 | **+50%** |
| 锁国 | **+25%** |
| 广州体制 | **+25%** |
| 其他贸易法律 | — |

| 言论自由 |  |
|---|---|
| 异见非法 | **+200** |
| 审查制度 | **+100** |
| 集会权利 | **+50** |
| 言论受保护 | **0** |

权威力的用途如下：

- 颁布[法令](Decrees.md)——大多数为 **100**
- 支持或压制[政治运动](Political movement.md)——**200**
- 设立消费税——视商品不同为 **100** 至 **500**。
- 在超过特许上限时授予[公司特许状](Companies.md)——**100**
- 对某建筑设立国家专营——**100**

权威力赤字称为*政治失能*（Political Dysfunction），完全赤字时的效果上限为：

- −10 反对派利益集团支持度
- +20% 政治运动产生的激进派

权威力盈余称为*立法效率*（Legislative Efficiency），完全盈余时的效果上限为：

- +25% 立法速度

### 影响力

影响力（Influence）代表国家开展[外交](Diplomacy.md)的能力。它主要来自国家的[等级](Rank.md)。竞争关系、某些[奇观](https://vic3.paradoxwikis.com/Monuments)以及[日志条目](https://vic3.paradoxwikis.com/Journal_entries)也会生成影响力。土地寡头的高满意度特质*家族纽带*也提供 **+10%** 影响力，若其势力强大则为 **+20%**。

每个等级提供一定数量的影响力，并会改变外交协定的消耗。

| 等级 | 影响力 | 外交协定消耗 |  |
|---|---|---|---|
|  | 列强 | 1000 | **+100%** |
|  | 主要政权 | 750 | **+50%** |
| 未受认可的主要政权 | 750 | **+0%** |  |
|  | 次要政权 | 600 | **+0%** |
| 未受认可的区域政权 | 600 | **−25%** |  |
|  | 无足轻重的政权 | 500 | **+0%** |
| 未受认可的政权 | 500 | **−50%** |  |

影响力用于建立和维持[外交协定](https://vic3.paradoxwikis.com/Diplomatic_pacts)。

影响力赤字称为*外交过度扩张*（Diplomatic Overreach），完全赤字时的效果上限为：

- −50% 威望

影响力盈余称为*外交缓冲*（Diplomatic Mitigation），完全盈余时的效果上限为：

- +25% 恶名衰减
- +25% 杠杆获取

## 参考

游戏概念
返回顶部
| 人口 | [人口](Pops.md) • [接受度](Acceptance.md) • [文化](Culture.md) • [迁移](Migration.md) • [需求](Needs.md) • [职业](Profession.md) • [宗教](Religion.md) • [生活水平](Standard of living.md) |
|---|---|

| 政府 | [政府](Government.md) • 容量 • [人物](Character.md) • [法令](Decrees.md) • [机构](Institutions.md) • [法律](Laws.md) • [技术](Technology.md) |
|---|---|

| 政治 | [选举](Elections.md) • [意识形态](Ideology.md) • [利益集团](Interest group.md) • [政治游说](Political lobby.md) • [政治运动](Political movement.md) • [政党](Political party.md) • [革命](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| 经济 | [建筑](Building.md) • [商品](Goods.md) • [收成状况](Harvest condition.md) • [基础设施](Infrastructure.md) • [市场](Market.md) • [生产方式](https://vic3.paradoxwikis.com/Production_methods) • [州](State.md) • [国库](Treasury.md) |
|---|---|

| 外交 | [外交](Diplomacy.md) • [外交行动](https://vic3.paradoxwikis.com/Diplomatic_action) • [外交博弈](Diplomatic play.md) • [强权集团](Power bloc.md) • [等级](Rank.md) • [附属国](Subject.md) • [条约](Treaty.md) |
|---|---|

| 战争 | [战争](Warfare overview.md) • [陆战](Land warfare.md) • [海战](Naval warfare.md) • [战争目标](https://vic3.paradoxwikis.com/Wargoal) • [征兵](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| 其他 | [国家](Countries.md) • [决议](Decision.md) • [事件](Events.md) • [日志](Journal.md) • [目标](Objective.md) • [维基百科（Vickypedia）](Vickypedia.md) |
|---|---|