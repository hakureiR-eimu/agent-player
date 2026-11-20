---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Religion
source: https://vic3.paradoxwikis.com/Religion
pageid: 3478
categories: [1.13, Game_concepts]
fetched: 2026-10-27
---
本文已针对游戏当前[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

**宗教（Religion）**是[国家](Countries.md)和[人口](Pops.md)的一项特性。每个国家都有一个*国教*，它只能通过 effect（游戏内效果脚本）改变（例如[日本](Japan.md)有一个[决策](Decision.md)可以将其国教从大乘佛教改为神道教），或者通过宗教会议[强权集团](Power bloc.md)外交行动“强加国教”来改变。宗教也是人口的一项决定性特征，但人口中的个体可以根据[接纳度](Acceptance.md)等级改信其他宗教。

## 通用机制

### 接纳度

[政教关系法律](Power structure laws.md)通过将人口的宗教与国家的国教进行比较，决定每个人口从其宗教获得的[接纳度](Acceptance.md)。这些法律还决定哪些接纳度状态的人口可以改教以获得更高的接纳度。只有当州内存在接纳度更高的宗教时，人口才可以改教。通过颁布“宗教学校”法令或“弘扬国家价值观”法令可以提高改教速度。

### 禁忌

某些宗教拥有一个或多个*禁忌*。如果可以通过商品替代来满足某一[需求](Needs.md)的其他[商品](Goods.md)可供购买，那么信奉该宗教的人口购买的禁忌商品数量只有其他人口的一半，即使禁忌商品相对更便宜。与[痴迷](https://vic3.paradoxwikis.com/Obsessions)不同，禁忌是固定的，不会在游戏过程中改变。

### 虔信者利益集团

虔信者利益集团通常只能得到信奉国家国教的人口的支持。此外，虔信者的名称、[特质](Interest group.md)和[意识形态](Ideology.md)往往反映该国家的国教，例如逊尼派乌理玛或东正教会。

### 无神论

如果颁布了国家无神论法律，国家的国教将变为无神论，该国[已合并](https://vic3.paradoxwikis.com/Incorporated)州中 10% 的人口立即改信无神论，并且所有其他宗教获得**−10** 接纳度。如果之后颁布了其他政教关系法律，国教将重置为该国的默认国教。无神论人口无法支持虔信者。

除了万圣节彩蛋[伊甸](Eden.md)之外，没有本质上的无神论国家。

### 宗教会议

|  | 仅在启用[势力范围](Sphere of Influence.md) DLC 时可用。 |
|---|---|

宗教会议与宗教紧密交织，宗教会议的领袖可以将其国教强加给强权集团的成员。

## 传承

共有四个传承组，每组包含一至三种传承：

| 亚伯拉罕系 | 东方系 | 自然崇拜系 | 非精神系 |
|---|---|---|---|
| 基督教 伊斯兰教 犹太教 | 达摩系 道教系 | 原住民信仰 | 唯物主义 |

根据[政教关系法律](Power structure laws.md)的不同，同一传承组内的不同宗教所获得的宗教接纳度略高。

### 宗教接纳度

另见：
接纳度
| 法律 | 接纳对象 | 相关效果 |  |  |  |
|---|---|---|---|---|---|
| 国教 | 共享宗教特质 | 共享宗教特质组 | 无共享宗教特质组 |  |  |
| **国教** | **+25** | **+0** | **−10** | **−25** | 国教人口工资 +10% 其他宗教人口工资 −10% |
| **圣典之民** | **+25** | **+5** | **+5** | **−25** | 改教速度 −50% 增加异教税 |
| **米勒特制** | **+25** | **+10** | **+10** | **−25** | 改教速度 −50% 增加异教税 |
| **信仰自由** | **+20** | **+15** | **+5** | **+0** | 国教人口工资 +5% 其他宗教人口工资 −5% 完全接纳和二等公民人口不进行改教 |
| **政教完全分离** | **+15** | **+15** | **+15** | **+15** | 不进行改教 |
| **国家无神论** | **+15** | **+0** | **−5** | **−10** | 改教速度 +25% |

## 宗教列表

| 亚伯拉罕系 |  |  |
|---|---|---|
| 基督教传承 宗教 禁忌 天主教 — 新教 — 东正教 — 东方正统教会 — 伊斯兰教传承 宗教 禁忌 逊尼派 酒类 葡萄酒 什叶派 酒类 葡萄酒 伊巴德派 酒类 葡萄酒 犹太教传承 宗教 禁忌 犹太教 杂货 |  |  |
|  | 宗教 | 禁忌 |
|  | 天主教 | — |
|  | 新教 | — |
|  | 东正教 | — |
|  | 东方正统教会 | — |
|  | 宗教 | 禁忌 |
|  | 逊尼派 | 酒类 葡萄酒 |
|  | 什叶派 | 酒类 葡萄酒 |
|  | 伊巴德派 | 酒类 葡萄酒 |
|  | 宗教 | 禁忌 |
|  | 犹太教 | 杂货 |

| 东方系 |  |  |
|---|---|---|
| 达摩系传承 宗教 禁忌 格鲁派 — 大乘佛教 — 上座部 — 印度教 肉类 锡克教 — 道教系传承 宗教 禁忌 儒教 — 神道教 — |  |  |
|  | 宗教 | 禁忌 |
|  | 格鲁派 | — |
|  | 大乘佛教 | — |
|  | 上座部 | — |
|  | 印度教 | 肉类 |
|  | 锡克教 | — |
|  | 宗教 | 禁忌 |
|  | 儒教 | — |
|  | 神道教 | — |

| 自然崇拜系 |  |  |
|---|---|---|
| 原住民传承 宗教 禁忌 泛灵论 — |  |  |
|  | 宗教 | 禁忌 |
|  | 泛灵论 | — |

| 非精神系 |  |  |
|---|---|---|
| 唯物主义传承 宗教 禁忌 无神论 — |  |  |
|  | 宗教 | 禁忌 |
|  | 无神论 | — |

## 参考

游戏概念
返回顶部
| 人口 | [人口](Pops.md) • [接纳度](Acceptance.md) • [文化](Culture.md) • [迁移](Migration.md) • [需求](Needs.md) • [职业](Profession.md) • 宗教 • [生活水平](Standard of living.md) |
|---|---|

| 政府 | [政府](Government.md) • [能力](Capacity.md) • [人物](Character.md) • [法令](Decrees.md) • [机构](Institutions.md) • [法律](Laws.md) • [技术](Technology.md) |
|---|---|

| 政治 | [选举](Elections.md) • [意识形态](Ideology.md) • [利益集团](Interest group.md) • [政治游说](Political lobby.md) • [政治运动](Political movement.md) • [政党](Political party.md) • [革命](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| 经济 | [建筑](Building.md) • [商品](Goods.md) • [收成状况](Harvest condition.md) • [基础设施](Infrastructure.md) • [市场](Market.md) • [生产方式](https://vic3.paradoxwikis.com/Production_methods) • [州](State.md) • [国库](Treasury.md) |
|---|---|

| 外交 | [外交](Diplomacy.md) • [外交行动](https://vic3.paradoxwikis.com/Diplomatic_action) • [外交博弈](Diplomatic play.md) • [强权集团](Power bloc.md) • [等级](Rank.md) • [附属国](Subject.md) • [条约](Treaty.md) |
|---|---|

| 战争 | [战争](Warfare overview.md) • [陆地战争](Land warfare.md) • [海战](Naval warfare.md) • [战争目标](https://vic3.paradoxwikis.com/Wargoal) • [征兵](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| 其他 | [国家](Countries.md) • [决策](Decision.md) • [事件](Events.md) • [日志](Journal.md) • [目标](Objective.md) • [维基百科](Vickypedia.md) |
|---|---|