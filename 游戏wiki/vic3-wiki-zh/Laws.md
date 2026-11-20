---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Laws
source: https://vic3.paradoxwikis.com/Laws
pageid: 1592
categories: [1.13, Pages_with_obsolete_template_parameters, Laws, Game_concepts]
fetched: 2026-10-27
---
本文已针对游戏当前[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

法律
权力结构类法律
经济类法律
人权类法律
修正案
法国的起始法律。其中一些法律带有改变其效果的修正案。交叉箭头上方的数字表示该子类别下当前可颁布的替代法律数量。某些法律右下角的图标表示它们与特定机构相关联。
**法律**（Laws）代表一个[国家](https://vic3.paradoxwikis.com/Country)的法律改革，会影响其人口的政治、经济和社会状况。每个国家在每个已激活的法律类别中都始终有一项生效的法律。在游戏开始时，所有国家的法律都接近其 1836 年的实际情况。在游戏进程中，这些法律可能会在内部或外部压力下发生改变。利益集团根据自身及其领导人的[意识形态](Ideology.md)来支持或反对各种法律。[政治运动](Political movement.md)也会倡导或反对国家法律的变更。某些[外交博弈](Diplomatic play.md)也能够改变他国的法律。

法律以多种方式影响国家及其人口，其效果从简单的修正项（modifier）变化到治理体系等根本性内容各不相同。每个[机构](https://vic3.paradoxwikis.com/Institution)——如警察机构和殖民机构——都有一个法律类别，用于设立该机构并调整其效果。国家的法律为玩家提供了绝大部分可用的[权威力](https://vic3.paradoxwikis.com/Authority)，通常越专制的法律提供的权威力越多。

某些法律可能拥有**法律变体**（law variant）。例如“一口通商”（Canton System），它替代了[中国](China.md)的孤立主义。法律变体继承其母法律的所有意识形态立场，但效果可能截然不同。为清晰起见，游戏内查看时法律变体的名称后会在括号中标注其母法律的名称。

当前的法律集合以及潜在的法律变更可以在政治界面中查看。

## 颁布法律

在每个检查点，4 种结果之一（成功、辩论、推进、停滞）会发生。
颁布一项新法律是一个需要多个步骤的过程。

首先，一项法律需要获得支持才能被提出。这需要现任政府中的某个[利益集团](Interest group.md)、统治者，或一个支持该潜在变更的非被动[政治运动](Political movement.md)。如果[政府](Government.md)被视为*非法*（合法性低于 **25**），则完全无法通过任何法律——除非该法律得到某个非被动运动的支持。如果颁布过程已经开始后政府变为非法，则在政府合法性提升之前该法律不会取得任何进展。

接下来，被提出的法律会推进颁布进程，并周期性地有机会出现成功、推进、辩论或停滞。颁布过程分为三个阶段。当法律完成全部三个阶段后，即正式生效。

| 条件（首个适用者） | 阶段 1 | 阶段 2 | 阶段 3 |
|---|---|---|---|
| 技术官僚制 | 拟定 | 审议 | 实施 |
| 委员会共和制 | 讨论 | 修正 | 批准 |
| 独裁制 | 提出 | 审议 | 采纳 |
| / 共和制 除一党制国家外的任意投票权法律 | 发起 | 研究 | 投票 |
| 君主制 以下任意：财富投票制 有限选举权 普选制 | 交付 | 起草 | 投票 |
| 君主制 以下任意：寡头制 土地投票制 一党制国家 | 提出 | 审议 | 御准 |
| 默认 | 起草 | 修正 | 投票 |

### 法律支持

| 法律立场 |  |
|---|---|
| 强烈支持 | **+2** |
| 支持 | **+1** |
| 中立 | **0** |
| 反对 | **−1** |
| 强烈反对 | **−2** |
| 法律变更 |  |
| 一步 | **±5** |
| 两步 | **±10** |
| 三步或以上 | **±20** |

| 法律类别 | 倍率 |
|---|---|
| 治理原则 | **×2** |
| 奴隶制 | **×2** |
| 土地改革 | **×1.5** |

对某项法律的支持可以来自政府中的利益集团、一个至少拥有 **25** 积极性的非被动[政治运动](Political movement.md)，或直接来自[统治者的意识形态](Character ideology.md)。利益集团的意识形态及其领导人的意识形态决定了它们沿 5 级量表对法律的态度，从 ![Oppose](/images/thumb/6/65/Political_disapproval.png/24px-Political_disapproval.png) **强烈反对**到 ![Endorse](/images/thumb/3/37/Political_approval.png/24px-Political_approval.png) **强烈支持**。利益集团支持任何比现行法律更受其偏好的法律；同样，它们反对任何不如现行法律受偏好的法律。政府中支持被提出法律的利益集团提供初始成功率，而所有反对该法律的非边缘化利益集团提供初始停滞概率。持中立或更满意态度的反对利益集团只提供一半的停滞概率，持愤怒态度的利益集团则提供 50% 更多的停滞概率。非被动政治运动也按其支持度提供颁布概率，并根据其对该法律的立场决定是支持还是反对。统治者对某项法律的态度按其与现行法律的差异步数提供每步 **±5%** 的概率。

除了提供支持外，利益集团还会根据现行法律和提议的变更而获得或失去好感度。法律变更对好感度的影响约为通常的五倍，但该影响会在五年内衰减。因此，安抚一个不满或愤怒的利益集团的快速方法是提出一项它们支持的法律变更。即使并不打算真正颁布，这也可以为其他效果的消退或发生争取时间。某些法律类别——如右表所示——会放大法律变更对好感度的影响，但始终以 **±20** 为上限。

类似地，政治运动会根据现行法律和提议的变更而获得或失去积极性。

“法律承诺”条约条款也可以为颁布某项法律提供支持，承诺方每比条约对方低一个等级类别即提供 **+5%**。例如，一个主要政权（等级 6）向一个列强（等级 7）作出的法律承诺提供 +5% 成功率。一个次要政权（等级 4）则可获得 +15%，依此类推。

### 强加法律

宗主国可以向其非自治的君合国、王室领地、傀儡国、殖民地或附庸国[附属国](Subject.md)强加法律，并照常启动其颁布过程。附属国必须本身能够颁布该法律，宗主国才能将其强加。被强加的法律会经历全部常规颁布过程，也可能照常失败或引发革命。傀儡国、殖民地、王室领地和特许公司对被强加的法律获得 **+10%** 成功率。

某些[强权集团](Power bloc.md)的认同或原则允许集团领袖向集团成员强加特定法律。

强加法律会为被强加国启动一个日志条目，其中包含开始或拒绝颁布被强加法律的选项。在该日志条目处于活动状态时，其他任何法律都无法开始颁布，且被强加的法律只能通过该日志条目的按钮开始颁布。

id
Foreign Legal Imposition
Our [overlord] [imposer country] has declared it imperative that we enact [imposed law].
---

| 可见条件：仅活动时 |  |
|---|---|
| 激活方式：法律强加 | 激活时效果：无 |
| 条目按钮：接受强加 接受强加并开始颁布 [imposer country] 提出的法律。 可见条件：尚未拒绝颁布 [imposed law] 启用条件：尚未在颁布 [imposed law] Effects: 取消任何其他正在进行的法律颁布 开始颁布 [imposed law] Agreeable to Law Imposition Agreeable to Law Imposition 法律颁布修正项 +10% 颁布成功率 颁布过程无法手动取消 拒绝强加 放弃此事并通知 [imposer country]，表明你终究不会遵从他们的意愿。 可见条件：尚未拒绝颁布 [imposed law] Effects: 取消 [imposed law] 的颁布与强加 与 [imposer country] 关系 −50 如果是 [imposer country] 的附属国，独立倾向 +10 否则，如果处于 [imposer country] 领导的强权集团中，集团凝聚力 −10 针对 [imposer country] 的亲国家游说集团绥靖度 −2 |  |
| *接受强加并开始颁布 [imposer country] 提出的法律。* |  |
| **可见条件：**尚未拒绝颁布 [imposed law] |  |
| **启用条件：**尚未在颁布 [imposed law] |  |
| **效果：**取消任何其他正在进行的法律颁布 开始颁布 [imposed law] Agreeable to Law Imposition Agreeable to Law Imposition 法律颁布修正项 +10% 颁布成功率 颁布过程无法手动取消 |  |
| *放弃此事并通知 [imposer country]，表明你终究不会遵从他们的意愿。* |  |
| **可见条件：**尚未拒绝颁布 [imposed law] |  |
| **效果：**取消 [imposed law] 的颁布与强加 与 [imposer country] 关系 −50 如果是 [imposer country] 的附属国，独立倾向 +10 否则，如果处于 [imposer country] 领导的强权集团中，集团凝聚力 −10 针对 [imposer country] 的亲国家游说集团绥靖度 −2 |  |
| 完成条件：[Imposed law] 已颁布 | 完成时效果：与 [imposer country] 关系 +20 针对 [imposer country] 的游说集团绥靖度 ±1 获得 Enacted an Imposed Law Enacted an Imposed Law（衰减）国家修正项 +10 合法性，持续 5 年 |
| 失效条件：满足任一：已拒绝颁布 [imposed law] [Imposer country] 不再能对该国强加法律 | 失效时效果：取消 [imposed law] 的颁布 |

### 颁布过程

| 法律类别 | ![Time](/images/thumb/0/08/Time.png/24px-Time.png) |
|---|---|
| 治理原则 | **200** |
| 权力分配 经济体制 奴隶制 | **150** |
| 所有其他 | **100** |

一旦某项法律被选定颁布，它便开始向某个*检查点*推进。颁布过程可以随时取消，取消一次法律变更将导致两年内无法再次尝试该项特定法律。检查点之间的默认间隔为 ![Time](/images/thumb/0/08/Time.png/24px-Time.png) 100 天，并会受到多种因素（如[合法性](https://vic3.paradoxwikis.com/Legitimacy)或权威力盈余）以及临时修正项的增减影响。某些法律类别——如右表所示——拥有更长的基础时间。

在每个检查点，四种情况之一可能发生：*成功、推进、辩论*或*停滞*。[1]

- 成功意味着法律进入下一阶段；如果法律已处于最终阶段，则立即生效且过程结束。
- 推进触发某个正面[事件](https://vic3.paradoxwikis.com/Event)，通常会提高成功率，有时会在大幅提高成功率与中等提高成功率外加另一种奖励之间提供选择。
- 辩论触发的事件可正可负，往往提供某种权衡：付出代价以提高成功率，或降低成功率。
- 停滞触发的事件通常会降低成功率，有时可以选择接受较小的成功率降低外加另一种惩罚。

在整个过程中，法律可能遭遇*挫折*（setback）——即阻碍法律的事情。如果法律在整个过程中遭遇三次挫折，颁布即告失败，且该法律两年内无法再次提出。挫折会在颁布事件中发生，或在法律成功率降至 0% 时发生。

政府中支持该法律的利益集团和支持该法律的非被动[政治运动](Political movement.md)分别以其政治力量和支持度贡献*基础成功率*，而所有反对该法律的非边缘化利益集团和非被动[政治运动](Political movement.md)则贡献*停滞*概率。如果统治者对该法律持某种立场，则按被提出法律与现行法律之间的差异步数提供每步 **+5%** 的概率，用于支持或反对。

*推进*的初始概率为成功率的两倍减去停滞概率，*辩论*的概率为其余三项概率之和与 100% 的差值。如果辩论概率将低于 0%，则会应用*讨论终结*（end-of-discussion）系数来缩放成功率或停滞概率中较低的一项，使总概率保持 100%。

当法律从一个阶段进入下一阶段时，所有已累积的颁布成功影响——无论正负——都会延续到下一阶段。因此，在早期事件中选择 **+5%** 颁布成功率往往更好，这相当于为三个阶段各提供 **+5%** 奖励，而不是立即推进单个阶段。

如果国家的[政府](Government.md)合法性降至*非法*，则在合法性提升到至少*难以接受*之前无法继续颁布法律，除非该法律得到一个积极度至少为 **25** 的运动的支持。

#### 公式

基础成功率 = ∑ ∑ ( 支持该法律的政府中利益集团的政治力量 ) + ∑ ∑ ( 支持该法律的非被动政治运动的支持度 ) + 统治者的支持 {\displaystyle {\text{Base success chance}}=\sum ({\text{Clout of endorsing interest groups in government}})+\sum ({\text{Support of endorsing non-passive political movements}})+{\text{Ruler's endorsement}}} ![{\displaystyle {\text{Base success chance}}=\sum ({\text{Clout of endorsing interest groups in government}})+\sum ({\text{Support of endorsing non-passive political movements}})+{\text{Ruler's endorsement}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/08d8acee651df7ff65f132b9660d4bd66f6cd397)

基础停滞概率 = 0.5 ⋅ ⋅ ∑ ∑ ( 持中立或更满意态度的反对利益集团的政治力量 ) + ∑ ∑ ( 不满的反对利益集团的政治力量 ) + 1.5 ⋅ ⋅ ∑ ∑ ( 愤怒的反对利益集团的政治力量 ) + ∑ ∑ ( 反对该法律的非被动政治运动的支持度 ) + 统治者的反对 {\displaystyle {\text{Base stall chance}}=0.5\cdot \sum ({\text{Clout of neutral or happier opposing interest groups}})+\sum ({\text{Clout of unhappy opposing interest groups}})+1.5\cdot \sum ({\text{Clout of angry opposing interest groups}})+\sum ({\text{Support of opposing non-passive political movements}})+{\text{Ruler's opposition}}} ![{\displaystyle {\text{Base stall chance}}=0.5\cdot \sum ({\text{Clout of neutral or happier opposing interest groups}})+\sum ({\text{Clout of unhappy opposing interest groups}})+1.5\cdot \sum ({\text{Clout of angry opposing interest groups}})+\sum ({\text{Support of opposing non-passive political movements}})+{\text{Ruler's opposition}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/75f0606b12c018a2840a977ac96d896492c0ac66)

推进概率 = 2 ⋅ ⋅ 基础成功率 − − 基础停滞概率 {\displaystyle {\text{Advance chance}}=2\cdot {\text{Base success chance}}-{\text{Base stall chance}}} ![{\displaystyle {\text{Advance chance}}=2\cdot {\text{Base success chance}}-{\text{Base stall chance}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/25a03d21986df168250f557811795a10530d1d10)

辩论概率 = 100 − − ∑ ∑ ( 推进概率 + 基础成功率 + 基础停滞概率 ) {\displaystyle {\text{Debate chance}}=100-\sum ({\text{Advance chance}}+{\text{Base success chance}}+{\text{Base stall chance}})} ![{\displaystyle {\text{Debate chance}}=100-\sum ({\text{Advance chance}}+{\text{Base success chance}}+{\text{Base stall chance}})}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/3f2dae4ac1aef1286728ba8635d10043c25a3f80)

## 法律类别
法律分为三大类——权力结构（10 组）、经济（8 组）与人权（8 组）——每个类别下各包含三至九项具体法律。

许多法律需要特定技术才能解锁，还有许多要求其他某些法律已通过或未通过——例如，在实行奴隶贸易的国家无法通过多元文化。少数法律为特定文化所独有，通常带有一系列非常具体的要求。一般来说，如果国家拥有某项法律的独特变体，该变体会取代其基础法律。例如，中国的“广州体系”为拥有西广东的汉族国家所独有，并取代孤立主义。

### 权力结构法律

主条目：
权力结构法律
- *治理原则*（Governance Principles）——国家治理所依据的根本原则与权威。决定国家元首是谁。
- *权力分配*（Distribution of Power）——政治权力如何分配。决定国家元首向谁负责。
- *公民权*（Citizenship）——公民权利的扩展。
- *种姓霸权*（Caste Hegemony）——基于英属印度种姓制度对社会成员权利的剥夺。
- *江户身份制度*（Edo Status System）——江户身份制度的推行。
- *政教关系*（Church and State）——世俗统治者与精神统治者之间的关系。
- *官僚制*（Bureaucracy）——国家的行政管理方式。
- *陆军模式*（Army Model）——陆军的组织与规制方式。
-*海军模式*（Navy Model）——海军力量的组织与学说。
- *国内安全*（Internal Security）——维持国家事务的秩序。

### 经济法律

主条目：
经济法律
- *经济体制*（Economic System）——经济的根本原则。
- *贸易政策*（Trade Policy）——规范跨境贸易与商品交换的法律。
- *税收*（Taxation）——国家如何通过向公民征税来获取收入。
- *土地改革*（Land Reform）——规范农业用地及耕作者的法律。
- *殖民*（Colonization）——对建立殖民地以取代和征服无政府国家的立场。
- *治安*（Policing）——国家警察力量的优先事项。
- *教育制度*（Education System）——适用于孩子们扫完烟囱之后的教育安排。
- *医疗制度*（Health System）——关于政府是否参与为公民提供医疗服务的法律。

### 人权法律

主条目：
人权法律
- *言论自由*（Free Speech）——规范言论自由与公众集会权的法律。
-*劳工权利*（Labor Rights）——工人的权利。
- *儿童权利*（Children's Rights）——赋予儿童的权利与保护。
- *妇女权利*（Rights of Women）——对女性的法律规制。
- *福利*（Welfare）——政府对收入匮乏者的援助。
- *迁移*（Migration）——对人口流动的管控。
- *奴隶制*（Slavery）——将人作为财产。
- *劳工结社*（Labor Associations）——对工人与手工业者结社的规制。

## 参考文献

1. ↑ 游戏的随机数生成器（RNG）会根据存档种子、确切的游戏日期以及确切的概率来决定结果。重新读取存档不会改变其中任何一项，因此单靠读档无法得到不同结果。通过改变富余权威力来改变判定日期是改变结果最简单的方式。

---

1. 如需更新页面内容，请参阅 /Victoria 3/game/common/laws 文件夹中的参考文件：
  1. 每种法律类型都有各自的 `txt` 文件（以法律类型命名）。
2. 如需更新风味文本，请参阅 /Victoria 3/game/localization/english 文件夹中的参考文件：
  1. 法律风味文本见参考文件 laws_l_english.yml。
  2. 修正项风味文本见参考文件 modifiers_l_english.yml。
  3. 机构风味文本见参考文件 institutions_l_english.yml。
  4. 发明风味文本见参考文件 inventions_l_english.yml。

游戏概念
返回顶部
| 人口 | [人口](Pops.md) • [接受度](Acceptance.md) • [文化](Culture.md) • [迁移](Migration.md) • [需求](Needs.md) • [职业](Profession.md) • [宗教](Religion.md) • [生活水平](Standard of living.md) |
|---|---|

| 政府 | [政府](Government.md) • [能力](Capacity.md) • [人物](Character.md) • [法令](Decrees.md) • [机构](Institutions.md) • 法律 • [技术](Technology.md) |
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