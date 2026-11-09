---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Decision
source: https://vic3.paradoxwikis.com/Decision
pageid: 5379
categories: [1.13, Scripted_content, Pages_with_obsolete_template_parameters, Articles_with_potentially_outdated_infoboxes, Game_concepts]
fetched: 2026-10-27
---
本文已针对游戏当前[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行验证。

维多利亚3
脚本内容
决议
•
事件
•
日志条目
通用内容页面
谷物法
•
内政
探险
•
意识形态内容
利益集团内容
•
喀拉喀托
日志条目事件
•
革命事件
生产与科技内容
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
殖民地群岛
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
**决议**（Decisions）表示在特定情况下可以采取的行动。决议可以在[日志](Journal.md)窗口的 *decision* 标签页中找到。

## 按国家划分

另见：
国家
特定国家的决议可以在相应的国家页面或本页顶部导航框中的内容页面找到。

## 禁止商品

id

### 解除鸦片禁令

如果外交或经济形势需要，解除鸦片禁令也许是明智之举。
---

| 显示条件：是市场领导者 正在禁止鸦片 没有进行中的日志条目 鸦片危机 | 可用条件：始终 |
|---|---|
| 效果：停止禁止鸦片 移除 modifier 鸦片禁令 鸦片禁令 国家修正 −20% 权威力 移除 modifier 鸦片恢复 鸦片恢复 国家修正 −2% 死亡率 −25% 来自政治运动的激进派 +25% 来自政治运动的忠诚派 |  |

id

### 禁酒

酒类的消费正在使我们的公民沦为欲望的奴隶。必须禁酒，以确保一个道德且文明的社会。
---

| 显示条件：是市场领导者 有进行中的日志条目 禁酒运动 没有禁止酒类 | 可用条件：没有自由贸易 |
|---|---|
| 效果：禁止酒类 添加 modifier 禁酒 禁酒 国家修正 −20% 权威力 永久生效 |  |

id

### 解除禁酒令

政治或经济形势可能要求我们解除禁酒令。
---

| 显示条件：是市场领导者 正在禁止酒类 | 可用条件：始终 |
|---|---|
| 效果：停止禁止酒类 移除 modifier 禁酒 禁酒 国家修正 −20% 权威力 |  |

## 外交

id

### 都灵条约

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助验证或更新此信息框。它最后针对版本1.9进行验证。 |
|---|---|

---

萨伏依省已成为我国与法国之间的争议焦点。如果我们愿意割让萨伏依，法国定然会认为自己欠我们一份人情。
---

| 显示条件：是独立国家 法国存在且尚未吞并萨伏依 完全拥有萨伏依 萨伏依不是首都 | 可用条件：处于和平状态 已研究民族主义 法国：是独立国家、处于和平状态且完全拥有罗讷 不欠该国义务 拥有友善或更好的关系 |
|---|---|
| 效果：法国：欠该国一项义务 收到事件 都灵条约 割让萨伏依以及（若拥有）普罗旺斯给法国 从萨伏依移除北意大利本土 |  |

## 探险

主条目：
探险
每次探险都通过一项决议启动。

## 通用

id

### 举办万国博览会

举办一场万国博览会，向全世界展示你的奇迹。你能展示的技术越多，博览会就越成功。
---

| 显示条件：尚未举办过万国博览会 | 可用条件：由玩家控制 处于和平状态 已研究国际关系 已研究铁路 任意拥有的艺术学院至少为10级 任意拥有的大学至少为10级 若拥有法兰西岛，已建造埃菲尔铁塔 否则，首都州的城市中心至少为20级 |
|---|---|
| 效果：激活日志条目 等待万国博览会 |  |

id

### 低地围海造田

通过多种技术的结合，可以排干低地的某些区域，将海洋变为可耕作的土地。
---

| 显示条件：完全拥有弗里斯兰和荷兰 全球围海造田进度计数器不存在，或已达到至少10 尚未在此围海造田（内部标志尚未设置） | 可用条件：已研究水管锅炉 拥有至少200行政力 |
|---|---|
| 效果：添加 modifier 围海造地 围海造地 国家修正 −200 行政力 激活日志条目 围海造田 |  |

id

### 大流行应对

致命的流感正在肆虐国土，我们必须采取行动保护公民。
---

| 显示条件：任意拥有的州拥有 modifier 流感大流行 | 可用条件：过去6个月内未更改大流行应对措施 |
|---|---|
| 效果：触发事件 [Country]流感：政府应对 |  |

## 独特建筑

主条目：
独特建筑
有决议可用于勘察巴拿马运河和苏伊士运河路线，并在勘察后购买所需土地，还有一项决议用于勘察摩天大楼选址。

## 参考

决议文件位于 /Victoria 3/game/common/decisions

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

| 其他 | [国家](Countries.md) • 决议 • [事件](Events.md) • [日志](Journal.md) • [目标](Objective.md) • [维基百科（游戏内）](Vickypedia.md) |
|---|---|