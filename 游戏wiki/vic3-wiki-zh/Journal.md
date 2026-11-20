---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Journal
source: https://vic3.paradoxwikis.com/Journal
pageid: 3220
categories: [Timeless, To_be_split, Scripted_content, Articles_with_potentially_outdated_infoboxes, Game_concepts, Journal]
fetched: 2026-10-27
---
本文为[长期有效](https://vic3.paradoxwikis.com/Category:Timeless)内容，适用于游戏的任何版本。

|  | **本文是拆分为多个页面的候选页面。** 请参与拟议拆分的[讨论](https://vic3.paradoxwikis.com/Talk:Journal)，帮助改进 wiki。 |
|---|---|

Victoria 3
脚本内容
决议
•
事件
•
日志条目
通用内容页面
谷物法
•
国内事务
探险
•
意识形态内容
利益集团内容
•
喀拉喀托
日志条目事件
•
革命事件
生产与技术内容
国家内容页面
美国
•
奥地利
•
巴尔干
•
巴西
英国
•
中国
•
殖民东印度
法国
•
德国
•
希腊
日本
•
朝鲜
•
黑山
菲律宾
•
葡萄牙
•
俄国
南部非洲
•
南美洲
西班牙
•
土耳其
特殊内容页面
万圣节
**日志**（journal）追踪一个国家正在进行的事件，用于模拟各类历史事件，无论真实还是假想。**日志条目**（journal entry）拥有一组可见条件、一组激活条件和一组完成条件。

日志条目的效果要么在激活期间生效，要么在完成时生效。许多日志条目在完成后提供加成，每一条目都有特定的激活条件，以及随后成功完成或失败的条件。有些条目有时间限制，而另一些则会保持开启直至完成。

大多数日志条目对满足条件的所有国家开放。特定国家的日志条目可在相应国家的页面或相关内容页面上找到。

## 按国家分类

另见：
国家
特定国家的日志条目可在相应国家页面或本页顶部导航框中的**国家内容页面**上找到。

- [阿富汗内容](Afghanistan.md)
- [美国内容](American content.md)
- [奥地利内容](Austrian content.md)
- [巴尔干内容](Balkan content.md)
- [玻利维亚内容](Bolivia.md)
- [巴西内容](Brazilian content.md)
- [英国内容](British content.md)
- [保加利亚内容](Bulgaria.md)
- [中国内容](Chinese content.md)
- [殖民东印度内容](Colonial Indies content.md)
- [埃塞俄比亚内容](Ethiopia.md)
- [法国内容](French content.md)
- [德国内容](German content.md)
- [希腊内容](Greek content.md)
- [夏威夷内容](Hawaii.md)
- [匈牙利内容](Hungary.md)
- [意大利内容](Italy.md)
- [日本内容](Japanese content.md)
- [朝鲜内容](Korean content.md)
- [黑山内容](Montenegrin content.md)
- [莫卧儿内容](Hindustan.md)
- [阿曼内容](Oman.md)
- [秘鲁-玻利维亚内容](Peru-Bolivia.md)
- [波兰内容](Poland.md)
- [旁遮普内容](Punjab.md)
- [罗马尼亚内容](Romania.md)
- [俄国内容](Russian content.md)
- 塞尔维亚内容
- [南美洲内容](South America content.md)
- [土耳其内容](Turkish content.md)

## 按主题分类

与某一主题或游戏机制相关的日志条目页面可在本页顶部导航框中的**通用内容页面**中找到。

## 重大局势

id

### 政府请愿

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助验证或更新此信息框。其最后验证版本为 1.5。 |
|---|---|

---

作为 [Ruler Title] 政府的忠实组成部分，[Interest Group] 正在请愿通过 [Law]。
如果 [Law] 成功通过，[Interest Group] 将大为满意，但如果这一请愿被无视，国家将面临惩罚，甚至 [Interest Group] 会退出政府。
---

| 可见条件：仅在激活期间 |  |
|---|---|
| 激活条件：以下皆非： 未在制定任何法律 任意利益集团： 在政府中 对任何可用法律的立场强于当前 以下皆非： 正处于革命中 正面临脱离 通过 'government_petition_events.100' 隐形年度脉冲事件触发 | 激活时效果： 触发事件 [Interest Group] 向政府请愿 |
| 完成条件：已通过 [Law] | 完成时效果： [Interest Group] 5% 的成员变为更倾向忠诚派 获得 Responsive Governance（衰减）10 年 +10 合法性 |
| 失败条件：[Interest Group] 不属于政府 | 失败时效果： [Interest Group] 获得 Failed Petition（衰减）10 年 −20 利益集团认可度 |
| 5 年（60 个月）后超时，效果如下： [Interest Group] 获得 Failed Petition（衰减）10 年 −15 利益集团认可度 |  |

id

### 大饥荒

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助验证或更新此信息框。其最后验证版本为 1.5。 |
|---|---|

---

一场严重的农作物歉收给我国人民带来了难以估量的苦难，他们恳求政府为此采取特别措施。
---

| 可见条件：非松散部族国家 |  |
|---|---|
| 激活条件：社会保障的投资等级低于 4。 至少满足其一： 任意已设州（Incorporated State） 平均生活水平低于 10 遭受过自然灾害 任意州 平均生活水平小于或等于 5 任意建筑： 为以下之一： 黑麦农场 小麦农场 稻米农场 玉米农场 小米农场 畜牧场 劳动力占用率大于或等于 10% 每周利润小于或等于 0.50 | 激活时效果： 触发事件 The Hard Times |
| 完成条件：等待饥荒结束，或将国家的生活水平提高 3 点。 | 完成时效果： 移除 Great Famine +50% 死亡率 |
| 5 年（60 个月）后超时，效果如下：无 |  |
| 每月可能发生以下随机事件： （权重：100）无事发生 （权重：10）Bread and Blood （权重：10）In Search of a Better Life （权重：10）events#famine_events.4 （权重：10）events#famine_political.1 （权重：10）events#famine_political.2 （权重：10）events#famine_political.3 （权重：10）events#famine_political.4 （权重：10）events#famine_political.5 |  |

id

### 诸民族的春天

对拿破仑战争后反动秩序的不满已爆发为席卷
欧洲
的激进情绪浪潮。自由派革命者高举三色旗，呼喊着自由、平等、博爱。
到街垒去！：
如果在此日志条目激活期间，一个自由派或社会主义政治运动在我国首都变得具有煽动性（Insurrectionary），革命力量可能试图夺取我国的政权。
---

| 可见条件：已研究平等主义 [Capital] 位于欧洲，即： 战略区域为以下之一： 西欧 南欧 中欧 北欧 巴尔干 俄罗斯 东欧 |  |
|---|---|
| 激活条件： 任意国家经历了自由派或激进派运动成为革命运动，或法国已宣布成立第二共和国 至少 5% 的人口为激进派 | 激活时效果： 触发事件 The Rise of Radicalism 如果该国为德意志国家，创建德意志民族运动；为意大利国家，创建意大利民族运动；两者皆非，则创建激进运动 创建自由派运动 |
| 条目修正：诸民族的春天 诸民族的春天 国家修正 +50% 立法速度 +500% 政治运动激进度增长 +35% 政治运动激进度 +25% 文化少数群体运动人口吸引力 +25% 德意志民族运动人口吸引力 +25% 意大利民族运动人口吸引力 +25% 自由派运动人口吸引力 +25% 激进派运动人口吸引力 +25% 德意志民族运动人口吸引力 |  |
| 完成条件：满足其一： 被激进化的运动强制通过了民主宪法 任意政府利益集团拥有自由派或激进派领袖 国家实行有限选举权或普选制 | 完成时效果： 触发事件 The Revolution Victorious |
| 失败条件： 在过去至少一年中，激进派、德意志民族、意大利民族或南斯拉夫民族运动在被镇压状态下支持率低于 10% 没有鼓动家且非边缘化的利益集团领袖持激进派意识形态。 | 失败时效果： 触发事件 The Revolution Vanquished |

id

### 红色恐慌

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助验证或更新此信息框。其最后验证版本为 1.5。 |
|---|---|

---

外国出现了一个强大的共产主义政权，这在部分人口中引发了恐惧，他们担心 [Country] 将是下一个倒向共产主义的国家。
带有左翼议程的国内政治潮流已受到反共产主义势力的审视，他们被指控为血腥革命的先兆和外国势力的代理人。
---

| 可见条件：我们在其拥有利益的任意次要政权以上的国家已研究劳工运动 |  |
|---|---|
| 激活条件： 我们在其拥有利益的任意次要政权以上的国家已通过委员会共和制法律 未实行委员会共和制 | 激活时效果： 触发事件 The Red Scare |
| 失败条件：至少满足其一： 已通过委员会共和制 任意革命进度大于 75% |  |
| 失效条件：我们在其拥有利益的次要政权以上的国家均未通过委员会共和制法律 |  |
| 10 年（120 个月）后超时，效果如下： 触发事件 A Subtler Terror |  |
| 每月可能发生以下随机事件： （权重：300）无事发生 （权重：10）：The Nationalization of Women （权重：10）：Communism Criminality （权重：10）：events#red_scare.4 （权重：10）：events#red_scare.5 （权重：10）：events#red_scare.6 （权重：10）：events#red_scare.7 （权重：10）：Marching Against Peace （权重：10）：In the Face of Revolution （权重：10）：The White Émigrés （权重：10）：Progressive Dilemmas （权重：10）：events#red_scare.12 （权重：10）：The Communist Ark （权重：10）：events#red_scare.15 |  |

## 国内事务

id

### 从农场到工厂

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助验证或更新此信息框。其最后验证版本为 1.5。 |
|---|---|

---

农民之国属于过去。如果我们的家园不过是农田，我们怎能指望进步走进这些家园？
---

| 可见条件：农民占总人口超过 60% |  |
|---|---|
| 激活条件： 未实行农奴制 未实行土地税制 | 激活时效果：无 |
| 完成条件： 农民占总人口低于 35% 未实行农奴制 未实行土地税制 实业家未被边缘化 | 完成时效果： 触发事件 Road to Progress |

id

### 城市化

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助验证或更新此信息框。其最后验证版本为 1.5。 |
|---|---|

---

未来并非像古老传说所说的那样非黑即白——它是灰色的！是那列让我们游历异国的火车的颜色！是那座让我们付得起旅费的工厂的颜色！是那，我的朋友，的颜色——

| 可见条件：任意已设州拥有城市中心 |  |
|---|---|
| 激活条件： 任意已设州拥有 5 级或以上的城市中心 未实行农本主义 | 激活时效果：无 |
| 完成条件： 至少 75% 的已设州拥有 5 级或以上的城市中心 任意已设州拥有 10 级或以上的城市中心 | 完成时效果： 触发事件 Winds of Change |

## 发展

### 艺术

id

#### 资助浪漫主义

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助验证或更新此信息框。其最后验证版本为 1.9。 |
|---|---|

---

浪漫主义艺术运动倡导辉煌的往昔：骑士、城堡、海盗、禁忌的自然与逝去的英雄。其动人的魅力必须迅速传播。
---

| 可见条件： 已研究理性主义 非未受承认国家 |  |
|---|---|
| 激活条件： 已研究浪漫主义 未研究现实主义 拥有城市中心 |  |
| 完成条件： 任意 2 级或以上的艺术学院 已激活传统艺术生产方式 劳动力占用率至少 90% | 完成时效果： 触发事件 Isn't It Romantic? |
| 失败条件：已研究现实主义 |  |
| 10 年（120 个月）后超时，效果如下：无 |  |

id

#### 资助现实主义艺术

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助验证或更新此信息框。其最后验证版本为 1.5。 |
|---|---|

---

艺术家们正从抽象、奇幻的艺术转向对具体题材的现实主义描绘。作为这一运动的赞助者，可能获益良多。
---

| 可见条件： 已研究浪漫主义 未研究照相机 非未受承认国家 |  |
|---|---|
| 激活条件： 已研究现实主义 拥有艺术学院 |  |
| 完成条件： 所有艺术学院： 劳动力占用率至少 90% 已激活现实主义艺术 | 完成时效果： 触发事件 The Realist Movement |
| 10 年（120 个月）后超时，效果如下：无 |  |

id

#### 确立摄影艺术

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助验证或更新此信息框。其最后验证版本为 1.9。 |
|---|---|

---

| 可见条件：已研究现实主义 未研究电影 非未受承认国家 |
|---|
| 激活条件：已研究照相机 拥有 3 级或以上的艺术学院 |

## 独特建筑

主条目：
独特建筑
运河和摩天大楼各自拥有与其建造相关的特殊日志条目。某些奇观也拥有相关的日志条目。

## 探险

主条目：
探险
探险代表欧洲历史上探索世界各地的努力，即美洲西北部、非洲的主要河流和南极洲，以及英国远征西藏。

## 参考资料

日志条目文件可在 /Victoria 3/game/common/journal_entries 中找到

游戏概念
返回顶部
| 人口 | [人口](Pops.md) • [接纳度](Acceptance.md) • [文化](Culture.md) • [迁移](Migration.md) • [需求](Needs.md) • [职业](Profession.md) • [宗教](Religion.md) • [生活水平](Standard of living.md) |
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

| 其他 | [国家](Countries.md) • [决策](Decision.md) • [事件](Events.md) • 日志 • [目标](Objective.md) • [维基百科（Vickypedia）](Vickypedia.md) |
|---|---|