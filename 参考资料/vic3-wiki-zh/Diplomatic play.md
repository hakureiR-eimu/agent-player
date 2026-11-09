---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Diplomatic play
source: https://vic3.paradoxwikis.com/Diplomatic_play
pageid: 3131
categories: [1.13, Articles_with_potentially_outdated_sections, Expand, Diplomacy]
fetched: 2026-10-27
---
本文已针对游戏当前[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

外交
外交行动
外交博弈
强权集团
附属国
条约

**外交博弈**（diplomatic play）代表一国对另一国提出的要求。其范围从索取领土或使其屈服，到强迫另一国更改法律。一旦外交博弈开始，其他国家可以加入任意一方，或被*拉拢*（swayed）。外交博弈往往会演变为战争，但*发起方*可以*退让*，或*目标方*可以*屈服*，从而避免战争，但须将所有主要要求让与对方。

## 发起外交博弈

除少数由事件发起的外交博弈外，外交博弈在一国向另一国提出要求（例如割让某个州）时开始。除游戏开始时已在进行中的战争外，《维多利亚3》中所有战争都始于一场外交博弈，即便是革命和分裂也是如此。发起外交博弈的国家是*发起方*，收到要求的国家是*目标方*；两者是*主要参与者*。许多要求需要在要求目标（被索取的州或目标国的首都）所在的[战略区域](Strategic region.md)拥有有效的[利益](https://vic3.paradoxwikis.com/Interest)。此后该博弈将与此战略区域相关联。

除了需要有有效利益外，视外交博弈类型而定，通常无法对以下国家发起外交博弈：

- 与发起国关系为友好或更高，
- 发起国对其负有义务，
- 曾羞辱过发起国，
- 与发起国处于停战状态，
- 是发起国的附属国或宗主国（包括直接和间接）。

发起外交博弈会引发一次[外交事件](Diplomacy.md)，这会按所选战争目标产生的[恶名](https://vic3.paradoxwikis.com/Infamy)比例，降低与所有在目标区域拥有利益的国家的[关系](https://vic3.paradoxwikis.com/Relations)。博弈开始时在目标区域拥有有效利益的所有国家都是*潜在参与者*，此外还包括目标方或发起方的任何盟友、非自治附属国、宗主国、目标方的防御条约伙伴，以及为目标方提供独立保证的国家。一国能否实际加入博弈的某一方，取决于诸如其是否为自治附属国、或对目标方或发起方负有义务等因素。

[非自治附属国](Subject.md)通常不能发起任何外交博弈。它们会自动参与其宗主国的博弈；而当其成为博弈的目标时，宗主国会自动接管该博弈，并在大多数用途下成为目标方。

[自治附属国](Subject.md)只有在符合潜在参与者条件时（例如在博弈发生的战略区域拥有利益）才能参与博弈。如果某项要求是解放它们，它们会自动加入**宗主国**的一方参战，除非它们处于反叛状态，此时它们会加入对手一方。

支持某附属国独立的国家，会自动加入该国的独立博弈。

### 周旋

*周旋*（Maneuvers）代表一国影响外交博弈的能力，可通过添加额外要求或拉拢潜在参与者支持己方。只有主要参与者可以使用周旋。可用的周旋量主要取决于国家的等级。一系列与哲学相关的技术（经验主义、精神病学、哲学实用主义、精神分析）各增加 **+25%** 周旋，最终技术行为主义增加 **+50%**。周旋还有其他来源，例如奥斯曼的[日志条目](https://vic3.paradoxwikis.com/Journal_entry)[坦志麦特：收复叙利亚](https://vic3.paradoxwikis.com/Tanzimat:_Reclaim_Syria)。

| 等级 |  |  |
|---|---|---|
|  | 列强 | 100 |
|  | 主要政权 | 75 |
| 未承认的主要政权 | 75 |  |
|  | 次要政权 | 60 |
| 未承认的区域政权 | 60 |  |
|  | 无足轻重的政权 | 50 |
| 未承认的政权 | 50 |  |
| 分散政权 | 30 |  |

### 恶名

参见：
恶名

外交要求按以下公式产生恶名：恶名 = 基础值 ⋅ ⋅ (1 + 人口乘数) ⋅ ⋅ 州乘数 ⋅ ⋅ ( 1 + 发起方修正 + 目标方修正 ) ⋅ ⋅ 附属国乘数 ⋅ ⋅ 未承认目标修正 ⋅ ⋅ 其他修正 {\displaystyle {\text{Infamy}}={\text{Base value}}\cdot {\text{(1 + Pop multiplier)}}\cdot {\text{State multiplier}}\cdot (1+{\text{Initiator modifier}}+{\text{Target modifier}})\cdot {\text{Subject multiplier}}\cdot {\text{Unrecognized target modifier}}\cdot {\text{Other modifiers}}} ![{\displaystyle {\text{Infamy}}={\text{Base value}}\cdot {\text{(1 + Pop multiplier)}}\cdot {\text{State multiplier}}\cdot (1+{\text{Initiator modifier}}+{\text{Target modifier}})\cdot {\text{Subject multiplier}}\cdot {\text{Unrecognized target modifier}}\cdot {\text{Other modifiers}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/2d57ab24fa2633088ed0b9a591bc764e929b010f) 其中：

| 等级 | 发起方 | 目标方 |  |
|---|---|---|---|
|  | 列强 | **+20%** | **+20%** |
|  | 主要政权 | **+10%** | **+10%** |
| 未承认的主要政权 | **+50%** | **−30%** |  |
|  | 次要政权 | **+0%** | **+0%** |
| 未承认的区域政权 | **+40%** | **−40%** |  |
|  | 无足轻重的政权 | **−10%** | **−10%** |
| 未承认的政权 | **+30%** | **−50%** |  |

- **基础值**取决于所使用的[战争目标](Diplomatic play.md)。
- **人口乘数**为 3 ∗ ∗ 人口 {\displaystyle 3*{\text{Population}}} ![{\displaystyle 3*{\text{Population}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/276feb9bf4ab304126bb5a0bd3e9853cf7c38162)，其中*人口*为被目标人口数（以百万计）。该乘数在每个目标州上限为 5 500%，总计上限为 50 5000%。[1]
- **州乘数**在被目标州为未整合州（**−50%**）或发起国主体文化的本土（**−25%**）时降低其恶名成本。这些修正分别适用于每个被目标的州，并可叠加。[2]
- **发起方与目标方修正**取决于两国的等级与承认状态，如上表所示。
- **附属国乘数**在目标为发起国的附属国、且独立倾向低于 25 或正在外交博弈中对抗发起国时为 0.25 −75%，否则为 **1**。
- **未承认目标修正**仅影响被承认国家对未承认国家产生的恶名；该修正通过研究殖民（**−10%**）与文明使命（**−25%**）技术获得。原则“殖民事务 III”还会按殖民事务等级每级额外增加 **−5%**。
- **利益层级修正**：若发起方在目标战略区域的利益为无或关注，为 **+25%**；为介入，为 **+10%**；为霸权，为 **-20%**。
- **其他修正**包括多边同盟（**−25%**）、拥有谨慎（**−20%**）与鲁莽（**+20%**）人物特质的统治者，以及各种来自事件的国家修正。

### 主要要求与次要要求

要求分为两类：*主要要求*与*次要要求*。主要要求在战争爆发前对方退让或屈服时即可强制执行。次要要求只能在战争爆发后通过和平协议或目标国投降来强制执行。这促使较弱的一方在胜算渺茫时不会为战而战。

发起博弈的初始要求以及目标方的第一个要求自动为主要要求。此外，若第三方国家被以针对发起方或目标方的要求拉拢，该要求为主要要求。若一国被以针对某支持者的要求拉拢，则该要求为次要要求。

各方的主要参与者可以将要求从次要提升为主要。此举需额外花费 **50%** 周旋，并额外产生初始要求成本 **50%** 的[恶名](https://vic3.paradoxwikis.com/Infamy)。只有针对主要对手的要求可以提升。

一旦提出要求，就无法移除，也无法将要求“降级”。

未被坚持（无论何种原因）的要求所产生的一部分或全部恶名会被退还，但对关系的负面影响不会逆转。若防御方退让博弈、将（产生恶名的）战争目标让与进攻方，进攻方可获得 **75%** 的恶名退还。

## 外交博弈阶段

外交博弈分为三个阶段，以*升级度*为基础——该值在博弈开始后每天增加：

1. 开局行动 – 20 天
2. 外交周旋 – 60 天
3. 战争倒计时 – 20 天

每当发起方或目标方添加要求或拉拢一国时，每个行动会使升级暂停 5 天，若一次采取四个以上行动，最多暂停 20 天。因此，如果双方都不退让，在战争爆发前，一场外交博弈的持续时间可以显著超过 100 天。

### 开局行动阶段

第一阶段是*开局行动*。目标方可以免费设置其第一个要求。双方都可以添加更多要求，并将其提升为主要要求。

在此阶段，只有发起方和目标方的宗主国与非自治附属国会加入任何一方。自治附属国的宗主国不会自动加入其附属国一方，且只能在此阶段加入。其他国家可以通过*倾向*（leaning）表明其对某一方的偏好。

在此阶段双方都不能退让，从而允许在任何一方退让之前提出更多主要要求。

### 外交周旋阶段

当升级度达到 20 时，开局行动阶段结束，外交博弈的“主”阶段——*外交周旋*开始。若目标方未设置第一个要求，将自动获得一个（通常为羞辱）。

在此阶段，潜在参与者可以对某一方设定立场；他们可以无需拉拢或通过*反向拉拢*加入一方，倾向某一方，或保持中立。尚未加入任何一方的国家也可以*宣布中立*。这会使该国完全退出博弈，且无法重新加入谈判。这使该国可以自由参与其他外交博弈或行动。

此外，两个主要参与者可以使用周旋将潜在参与者拉拢到己方。

在此阶段任一方都可能退让，如果主要要求不算苛刻且军事失败的 likelihood 较高，尽早退让可能是有利的。

#### 拉拢

拉拢（Sway）是向潜在参与者提供的某些利益或机会，以换取其在外交博弈和潜在战争中的支持。AI 国家在义务被要求兑现时只要可行总会同意，但除此之外会权衡为获得其支持而提供的义务或要求的价值。中立国家也可以主动提出拉拢以加入某一方，通常称为“反向拉拢”。

| 类型 | 周旋 |
|---|---|
| 提供义务 | 10 |
| 要求兑现义务 | 10 |
| 召唤盟友 | 20 |
| 成为附属国 | 5 |
| 转移附属国 | 10 |
| 转移州 | 10 |
| 战争目标 | 与战争目标相同 |

以战争目标拉拢潜在参与者时，只有与潜在参与者拥有利益的战略区域相关的战争目标可用。

拉拢接受度由每个参与者特有的一组数值决定：对各方的偏好以及中立度。

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助核实或更新此章节。其最后核实版本为 1.9。 |
|---|---|

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请帮助核实或更新此章节。其最后核实版本为 1.9。 |
|---|---|

在外交博弈界面中，每个潜在参与者显示的是**相对**偏好值。每方的相对偏好值计算方法为：该方偏好值减去对方偏好值或中立度中的较高者。

要被拉拢，潜在参与者需要有正的**接受分数**，即：所提供拉拢的价值 + 相对偏好值。对于潜在参与者不感兴趣或认为不可实现的提议，会施加 -1000 修正。

[自治附属国](Subject.md)的拉拢逻辑被覆盖，只能以解放附属国战争目标拉拢。而该拉拢只有在附属国态度为反叛时才可用。如果通过“添加战争目标”按钮选择解放附属国战争目标而附属国**并非**反叛状态，无论其实际偏好如何，它都会自动加入宗主国一方（尽管外交博弈界面上会显示其偏好，具有误导性）。

一旦某国支持了一方（无论是否被拉拢），它可以选择背弃该方或改换阵营。这可能是因为该国与主要参与者的关系恶化，或另一方提供了更好的拉拢。若一国背弃一方，向其提供的任何要求都会被取消。背弃一方会导致与该方国家的**−50**关系惩罚。

### 战争倒计时阶段

外交博弈的最后 20% 是*战争倒计时*阶段。在战争倒计时期间，双方被锁定，各国无法再宣布或放弃对任何一方的支持，也无法添加新的要求或拉拢。此阶段唯一可能的行动是*退让*或*屈服*，这也是最有可能有一方如此做的阶段。

双方往往都可能希望博弈升级为战争，以同时获得主要和次要要求。若升级计量达到 **100**，外交博弈结束，[战争](Warfare overview.md)爆发。

## 战争目标与外交博弈列表

除由事件或特殊机制触发者外，外交博弈由发起国的行动发起。在以下列表中，*发起方*指从战争目标中获益的国家。各方（包括博弈开始时添加的第一个要求）的第一个要求不消耗周旋。宗主国也可以在外交博弈中代表支持己方的附属国添加某些类型的战争目标（如征服/归还州），此时恶名归于添加战争目标的宗主国。

每个战争目标都有与之关联的目标。达成目标会更快降低敌方的战争支持度，且如果针对该敌人存在未达成的战争目标，其战争支持度不会降至 0 以下。占领一国首都视为达成针对该国或其附属国的所有战争目标的目标。

| 优先级 | 名称 | 条件 | 目标类型 | 争夺类型 | 周旋修正 | 恶名基础值 (最低)修正 |
|---|---|---|---|---|---|---|
| 80 | 吞并国家 完全吞并另一国。 | 绝不能添加到现有外交博弈中 | 国家 | 控制目标国至少 50% 的已整合州或目标国首都 | 10 目标人口 | 5 (5) 目标人口 未承认/分散 忠诚/反叛附属国 利益层级 |
| — | 废除奴隶制 通过制定“禁止奴隶制”，强迫另一国废除其落后而不人道的奴隶制习俗。 | 绝不能添加到现有外交博弈中 目标国尚未制定任何版本的“禁止奴隶制” 发起国已制定任意版本的“禁止奴隶制” | 条约条款 | 控制目标国首都 | 2.5 目标人口 | 0.5 (5) 目标人口 未承认/分散 忠诚/反叛附属国 利益层级 |
| 15 | 殖民权利 加快对分散国家的殖民。 | 绝不能添加到现有外交博弈中 可以目标分散国家 | 国家 | 控制目标国至少一个州 | 0 | 0 |
| 69 | 征服州 从另一国征服一个州。 | 可代表其他参与国添加 在相关战略区域拥有利益 目标州不是条约港 与针对同一目标的解放国家冲突 与针对同一目标的归还州、夺取条约港和统一冲突 对目标州没有宣称 | 州 | 控制目标州 | 10 州人口 | 5 (5) 州人口 本土 未整合 未承认/分散 忠诚/反叛附属国 利益层级 |
| 60 | 削减至规模 强迫一个构成威胁的国家交出其近期的征服成果。迫使目标国释放在过去 10 年中通过征服获得的所有州和附属国。 | 绝不能添加到现有外交博弈中 | 国家 | 控制目标国至少 50% 的已整合州或目标国首都 | 0 | 0 |
| — | 强制执行条约条款 强迫一国签署包含特定条款的条约。 |  | 条约条款 | 控制目标国首都 | 取决于具体条款 |  |
| 17 | 强制国有化 一项战争目标，将目标国在我国拥有的所有建筑等级国有化，并撤销其外国投资权。 | 可代表其他参与国添加 | 国家 | 保持控制发起国所有州 | 10 | 5 (5) 未承认/分散 忠诚/反叛附属国 利益层级 |
| — | 投资权 一项向目标国强制推行外国投资权的战争目标。目标国还必须制定自由贸易。 | 绝不能添加到现有外交博弈中 等级不低于目标国 尚未制定任何版本的孤立主义 | 条约条款 | 控制目标国首都 | 2.5 目标人口 | 0.25 (0.25) 目标人口 未承认/分散 忠诚/反叛附属国 利益层级 |
| 18 | 羞辱 羞辱另一国。被羞辱的国在 60 个月内无法对其被羞辱的国家发起任何外交博弈。这 60 个月内的额外效果：被对手羞辱 被对手羞辱 国家修正 −25% 施压点数获取 −25% 威望。 |  | 国家 | 控制目标国至少一个州 | 20 | 0 |
| 40 | 提升自治度 将持有者的附属国类型改为自治度更高的一种。 | 此战争目标后存在有效的附属关系 目标国为发起国的宗主国 | 国家 | 保持控制发起国所有州或控制目标国首都 | 10 | 0 |
| 100 | 独立 强迫你的宗主国授予你的国家独立，并强制国有化其拥有的所有建筑等级。 | 可代表其他参与国添加 目标国为发起国的宗主国 | 国家 | 保持控制发起国所有州或控制目标国首都 | 20 | 0 |
| 30 | 加入强权集团 一项迫使目标国加入持有者的强权集团的战争目标。 | 与针对同一目标的建立自治领、建立保护国、建立朝贡国、降低自治度和恢复联合冲突 是强权集团的领袖 | 国家 | 控制目标国至少 50% 的已整合州或控制目标国首都 | 10 | 0 |
| 98 | 退出强权集团 强迫强权集团领袖允许一个成员国退出。 | 不是附属国 目标国为当前强权集团的领袖 | 国家 | 保持控制发起国所有州 | 10 | 0 |
| 90 | 解放国家 强迫一国授予另一国家独立。 | 在相关战略区域拥有利益 与针对同一目标的征服州、归还州、夺取条约港和统一冲突 与针对同一目标的吞并国家冲突 与针对同一目标的解放附属国和转移附属国冲突 | 潜在国家 | 控制目标国至少一个可作为战争目标释放的州 | 30 | 0 |
| 58 | 解放附属国 强迫一国授予其某一附属国独立。 | 将战争目标的利益相关方视为宗主国而非目标国 在相关战略区域拥有利益 与针对同一目标的加入强权集团、建立自治领、建立保护国、建立朝贡国、降低自治度和恢复联合冲突 | 国家 | 控制目标国至少 50% 的已整合州或目标国首都 | 20 | 0 |
| 14 | 建立自治领 强迫另一国成为自治领。 | 可代表其他参与国添加 在相关战略区域拥有利益 此战争目标后存在有效的附属关系 与针对同一目标的加入强权集团、建立保护国、建立朝贡国、降低自治度和恢复联合冲突 | 国家 | 控制目标国至少 50% 的已整合州或目标国首都 | 10 目标人口 | 2 (2) 目标人口 未承认/分散 忠诚/反叛附属国 利益层级 |
| 12 | 建立保护国 强迫另一国成为保护国。 | 可代表其他参与国添加 在相关战略区域拥有利益 此战争目标后存在有效的附属关系 与针对同一目标的加入强权集团、建立自治领、建立朝贡国、降低自治度和恢复联合冲突 | 国家 | 控制目标国至少 50% 的已整合州或目标国首都 | 10 目标人口 | 2 (2) 目标人口 未承认/分散 忠诚/反叛附属国 利益层级 |
| 13 | 建立朝贡国 强迫另一国成为朝贡国。 | 可代表其他参与国添加 在相关战略区域拥有利益 此战争目标后存在有效的附属关系 与针对同一目标的加入强权集团、建立自治领、建立保护国、降低自治度和恢复联合冲突 | 国家 | 控制目标国至少 50% 的已整合州或目标国首都 | 10 目标人口 | 2 (2) 目标人口 未承认/分散 忠诚/反叛附属国 利益层级 |
| 19 | 开放市场 强迫另一国开放市场。 | 目标国已制定孤立主义且不是关税同盟的次级成员 发起国尚未制定孤立主义 | 国家 | 控制目标国至少一个已整合州 | 20 | 0.1 (0.1) 目标人口 未承认/分散 忠诚/反叛附属国 利益层级 |
| 39 | 降低自治度 将附属国类型改为自治度更低的一种。 | 此战争目标后存在有效的附属关系 与针对同一目标的加入强权集团、建立自治领、建立保护国、建立朝贡国和恢复联合冲突 目标国为发起国的附属国 | 国家 | 控制目标国至少一个已整合州 | 10 | 2 (2) 目标人口 未承认/分散 忠诚/反叛附属国 利益层级 |
| 20 | 政权更迭 强迫另一国更改其政府与权力结构法律，使其与己方更为相似 |  | 国家 | 控制目标国至少 50% 的已整合州或目标国首都 | 10 | 0.5 (0.5) 目标人口 未承认/分散 忠诚/反叛附属国 利益层级 |
| 70 | 归还州 强迫其归还一个属于我们合法宣称的州。 | 可代表其他参与国添加 在相关战略区域拥有利益 目标州不是条约港 与针对同一目标的解放国家冲突 与针对同一目标的征服州、夺取条约港和统一冲突 对目标州拥有宣称 | 州 | 控制目标州 | 10 州人口 | 2 (2) 州人口 未承认/分散 忠诚/反叛附属国 利益层级 |
| 50 | 撤销所有声索 强迫一个国家撤销其对我方州区域的全部声索。 | 可代表其他参战国添加 绝不能添加到已存在的外交博弈中 | 国家 | 控制目标国家的全部声索 | 0 | 0 |
| 49 | 撤销声索 强迫一个国家撤销其对某个州区域的声索。 | 可代表其他参战国添加 | 国家 | 保持对被声索州的控制 | 5 | 0 |
| 99 | 脱离 试图从一个国家中脱离出去。 | 绝不能添加到已存在的外交博弈中 | 国家 | 控制至少一个目标的已合并州 | 0 | 0 |
| — | 夺取条约港 强迫另一个国家割让某个州内的条约港。 | 可代表其他参战国添加 在相关战略区域拥有利益 与针对同一目标的征服州、归还州和统一冲突 发起方不拥有目标州所在州区域的任何部分 发起方未制定任何形式的孤立主义 目标州对发起方存在潜在条约港 | 州 | 控制目标的首都 | 5 州人口 | 2 (2) 州人口 未开化/松散政权 忠诚/叛乱的附属国 利益层级 |
| 59 | 转移附属国 使我方成为其某一附属国的宗主。 | 该战争目标的利益相关方被视为宗主国而非目标国家 可代表其他参战国添加 在此战争目标之后存在有效的附属国关系 与针对同一目标的加入强权集团、建立自治领、建立保护国、建立朝贡国、降低自治度和恢复君合同冲突 与针对同一目标的解放附属国冲突 可以目标不在外交博弈中的国家 目标国家是附属国，且其宗主国是利益相关方而非发起方 | 国家 | 控制目标至少 50% 的已合并州，或控制目标的首都 | 8 | 2 (2) 目标人口 未开化/松散政权 忠诚/叛乱的附属国 利益层级 |
| 200 | 统一 吞并统一支持者、附属国或盟友所不拥有的、统一所需的全部州。 | 绝不能添加到已存在的外交博弈中 发起方是唯一的统一候选国 与针对同一目标的解放国家冲突 与针对同一目标的征服州、归还州和夺取条约港冲突 | 州 | 控制目标州 | 10 州人口 | 0 |
| 29 | 统一领导权 强迫另一个国家放弃其统一民族的野心。 | 发起方和目标都是统一的候选国 | 国家 | 控制至少一个目标的已合并州 | 30 | 0 |
| 12 | 恢复君合 强迫另一个国家恢复我方统治者在其王位上的统治。 | 在相关战略区域拥有利益 与针对同一目标的加入强权集团、建立自治领、建立保护国、建立朝贡国、降低自治度和恢复君合同冲突 已制定君主制 是寻求恢复君合的葡萄牙 [3] 目标是巴西 | 国家 | 控制目标至少 50% 的已合并州，或控制目标的首都 | 10 目标人口 | 0.5 (2) 目标人口 利益层级 |
|  | 海峡通行权 强迫目标国家准许军事通行通过其控制的任何海峡的战争目标。 | 绝不能添加到已存在的外交博弈中 目标拥有一个带海峡的省份，并拥有任意等级的海峡控制权 发起方无法通行目标拥有的任何海峡 | 条约条款 | 控制目标的首都 | 1 目标人口 | 0.1 目标人口 |
|  | 免除通行费 强迫目标国家让持有者免除其控制的任何海峡所征收的通行费的战争目标。 | 绝不能添加到已存在的外交博弈中 目标控制一条通行费率为低或更高的海峡 发起方未被免除目标征收的海峡通行费 | 条约条款 | 控制目标的首都 | 1 目标人口 | 0.1 目标人口 |
|  | 取消通行费 强迫目标国家停止在其控制的任何海峡上征收通行费的战争目标。 | 绝不能添加到已存在的外交博弈中 目标控制一条通行费率为低或更高的海峡，且被允许在其控制的海峡上征收通行费 | 条约条款 | 控制目标的首都 | 1 目标人口 | 0.25 目标人口 |
|  | 不得封锁海峡 强迫目标国家保持其控制的任何海峡开放的战争目标。 | 绝不能添加到已存在的外交博弈中 目标拥有一个带海峡的省份，拥有任意等级的海峡控制权，且被允许封锁其控制的海峡 | 条约条款 | 控制目标的首都 | 1 目标人口 | 0.25 目标人口 |

| 外交博弈 | 初始战争目标 | 其他要求 | 需要利益？ | 发起方必须自治？ | 可以是松散政权？ | 可对附属国/宗主国使用？ | 被热忱或更好关系阻止？ | 可添加额外战争目标？ | 初始恶名？ |
|---|---|---|---|---|---|---|---|---|---|
| 开放市场将初始战争目标设为强迫目标国家将其贸易政策法律改为自由贸易，并向对外贸易开放其市场。 | 开放市场 |  | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 政权更迭将初始战争目标设为政权更迭。强迫目标将其政府更改为与执行方相似的政府，并立即制定至多 # 项新政权所偏好的法律。 | 政权更迭 |  | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 废除奴隶制将初始战争目标设为强迫目标国家通过将其奴隶制法律改为禁止奴隶制来废除奴隶制 | 废除奴隶制 |  | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| 征服州将初始战争目标设为强迫目标国家割让一个特定州由你控制。 | 征服州 |  | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 归还州将初始战争目标设为强迫目标国家将指定州归还给你。 | 归还州 |  | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | 附属国 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 解放附属国将初始战争目标设为强迫目标国家准许其某一附属国独立。 | 解放附属国 | 目标是（某一其他国家的）附属国 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png)（与宗主国） | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 解放国家将初始战争目标设为强迫目标国家准许一个拥有家园州但被其占领的国家独立。 | 解放国家 |  | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 独立将初始战争目标设为强迫目标国家准许你独立。 | 独立 | 满足其一： 不能成为自治程度更高的附属国类型 我方在过去 5 年内被拒绝提升自治度 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | 宗主国 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 退出强权集团将初始战争目标设为退出由目标国家领导的强权集团。 | 退出强权集团 |  | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 提升自治将初始战争目标设为将你的附属国类型变更为自治程度更高的类型。 | 提升自治 | 我方在过去 5 年内被拒绝提升自治度 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | 宗主国 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 降低自治将初始战争目标设为降低目标附属国的自治度。 | 降低自治 | 若目标是君合国附属国类型，已研究民族主义 若目标是特许公司附属国类型，已研究文明使命 目标不是“隐匿之域”活跃时的琉球 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | 附属国 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 夺取条约港将初始战争目标设为强迫目标国家割让目标州区域内的一个条约港。 | 夺取条约港 |  | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 迫使成为朝贡国将初始战争目标设为强迫目标国家成为你的朝贡国。 | 迫使成为朝贡国 | 目标不享有保障中立 保障中立 国家修正 不可被征服 +15% 影响力 +15% 威望 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 迫使成为自治领将初始战争目标设为强迫目标国家成为你的自治领。 | 迫使成为自治领 | 目标不享有保障中立 保障中立 国家修正 不可被征服 +15% 影响力 +15% 威望 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 迫使成为保护国将初始战争目标设为强迫目标国家成为你的保护国。 | 迫使成为保护国 | 目标不享有保障中立 保障中立 国家修正 不可被征服 +15% 影响力 +15% 威望 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 转移附属国将初始战争目标设为强迫目标国家将其对目标附属国的控制权转移给你。 | 转移附属国 | 目标是（某一其他国家的）附属国 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png)（与宗主国） | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 吞并附属国将初始战争目标设为完全吞并目标国家。 | 吞并国家 | 若为东印度 ，处于和平状态，可使用失权原则，且目标是非玩家的非帝国层级土邦附属国，则改为使用援引失权原则 目标是发起方类型为殖民地、傀儡国、附庸国或王领的附属国 当发起方参与秘鲁-玻利维亚邦联事务时，目标不是以克丘亚或南安第斯为主文化的国家 当发起方参与“隐匿之域”时，目标不是琉球 若发起方为日本 ，则不实行农奴制 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | 直接附属国 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 革命将初始战争目标设为镇压目标革命。 | 吞并国家 | 总是自动触发 禁止谈判和平 镜像战争目标 在卷入判定上同时考虑发起方和目标的首都 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 脱离将初始战争目标设为粉碎目标的脱离行动，并迫使其归还从我们这里脱离出去的所有州。 | 脱离 | 总是自动触发 在卷入判定上同时考虑发起方和目标的首都 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 遏制威胁将初始战争目标设为强迫目标国家释放其在过去 10 年中通过征服获得的所有州和附属国。此外，其在其他进行中的外交博弈和战争中持有的任何战争目标都将被移除。 | 遏制威胁 | 必须是列强才能发起此外交博弈 目标的恶名等级必须达到国际弃儿 所有列强均会卷入 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | 目标 | 发起方 |
| 太平天国运动 | 吞并国家 | 总是自动触发 镜像战争目标 在卷入判定上同时考虑发起方和目标的首都 目标是天朝 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 加入强权集团将初始战争目标设为强迫目标国家加入我们的强权集团 | 加入强权集团 | 发起方是某个强权集团的领袖 目标必须最近拒绝过加入我们强权集团的邀请 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 强制国有化 将初始战争目标设为强迫目标国家放弃其在我方州内的一切财产所有权 | 强制国有化 |  | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 投资权利 将初始战争目标设为强迫目标国家给予你外国投资权利。若对方制定的是孤立主义法律，则其必须改为制定自由贸易。 | 投资权利 |  | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| 原住民起义 | 殖民权利 |  | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 吞并国家 | 吞并国家 | 目标等级不高于无足轻重的政权 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 统一德国将初始战争目标设为吞并其他国家持有的全部德意志家园州。 | 统一 | 总是自动触发（通过外交面板中的行动） 德意志不存在 已研究泛民族主义 莱茵邦联不存在 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 统一意大利将初始战争目标设为吞并其他国家持有的全部意大利家园州。 | 统一 | 总是自动触发（通过外交面板中的行动） 意大利不存在 已研究民族主义 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 统一斯堪的纳维亚将初始战争目标设为吞并其他国家持有的全部斯堪的纳维亚家园州。 | 统一 | 总是自动触发（通过外交面板中的行动） 斯堪的纳维亚不存在 已研究泛民族主义 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 统一埃塞俄比亚将初始战争目标设为吞并所有较为弱小的埃塞俄比亚国家。 | 吞并国家 | 拥有日志条目“诸王时代” 埃塞俄比亚不是附属国 目标国家可以成立埃塞俄比亚 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 统一中国将初始战争目标设为吞并所有较为弱小的中国政权。 | 吞并国家 | 满足其一： 拥有日志条目“军阀时代” 是中国崩溃后的北洋政府 是中国 不是附属国 目标国家满足其一： 拥有日志条目“军阀时代” 是中国崩溃后的北洋政府 以汉族或满族为主文化 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 统一阿拉伯将初始战争目标设为吞并所有较为弱小的阿拉伯国家。 | 吞并国家 | 可以成立阿拉伯 阿拉伯不存在 已研究泛民族主义 不是附属国 目标国家可以成立阿拉伯 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 统一印度将初始战争目标设为吞并所有较为弱小的印度国家。 | 吞并国家 | 可以成立或即为印度 已研究泛民族主义 不是附属国 目标国家可以成立印度，或属于印度地理宗教组且拥有“印度”主文化 阿萨姆、阿瓦德、俾路支、孟加拉、比哈尔、古吉拉特、卡纳达、马拉雅拉姆、马拉地、奥里亚、旁遮普、普什图、拉杰普特、信德、泰米尔、泰卢固、印度斯坦、邦德尔、帕哈里、冈德、巴盖利、恰蒂斯加尔、德干 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 统一群岛将初始战争目标设为吞并所有较为弱小的印度尼西亚国家。 | 吞并国家 | 可以成立印度尼西亚 印度尼西亚不存在 已研究泛民族主义 不是附属国 目标国家可以成立印度尼西亚 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 统一安第斯将初始战争目标设为吞并所有较为弱小的安第斯国家。 | 统一 | 总是自动触发（通过外交面板中的行动） 安第斯邦联不存在 已研究泛民族主义 不是附属国 可以成立安第斯邦联 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 德意志领导权将初始战争目标设为将目标国家从德意志重大统一的统一候选国中除名。 | 统一领导权 | 镜像战争目标 总是自动触发（通过外交面板中的行动） 已研究民族主义 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 意大利领导权（Italian Leadership）设定发起方的战争目标为将目标国家踢出意大利大统一（Italian major unification）的统一候选国。 | 统一领导权（Unification Leadership） | 镜像战争目标 总是自动触发（通过外交面板的行动） 已研究民族主义 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 斯堪的纳维亚领导权（Scandinavian Leadership）设定发起方的战争目标为将目标国家踢出斯堪的纳维亚大统一的统一候选国。 | 统一领导权 | 镜像战争目标 总是自动触发（通过外交面板的行动） 已研究泛民族主义 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 安第斯领导权（Andean Leadership）设定发起方的战争目标为将目标国家踢出安第斯大统一的统一候选国。 | 统一领导权 | 镜像战争目标 总是自动触发（通过外交面板的行动） 已研究泛民族主义 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 羞辱（Humiliation）设定发起方的战争目标为降低目标国家的威望，并使其在 5 年内无法在外交博弈中反对你。 | 羞辱 |  | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 印度兵变（Sepoy Mutiny）设定发起方的战争目标为完全吞并目标国家。 | 吞并国家（Annex Country） | 总是自动触发 禁止谈判和平 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 巴尔干战争（The Balkan War） | 羞辱 | 总是自动触发 禁止谈判和平 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | 目标方 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 强制推行三元制宣言（Enforce Trialist Manifesto） | 羞辱 | 总是自动触发 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 统一南斯拉夫（Unify Yugoslavia） | 统一 | 总是自动触发（通过外交面板的行动） 南斯拉夫不存在 非附属国 已研究泛民族主义 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 南斯拉夫领导权（Yugoslavian Leadership） | 统一领导权 | 镜像战争目标 总是自动触发（通过外交面板的行动） 已研究民族主义 | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |
| 匈牙利革命（Hungarian Revolution） | 吞并国家 | 总是自动触发 禁止谈判和平 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | 目标方 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 恢复君合（Restore Union）设定发起方的战争目标为强制目标国家恢复发起方统治者的王位。 | 恢复君合 | 发起方拥有法律君主制，且为寻求恢复君合的葡萄牙 [3] 只能使用一次 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 发起方 |

|  | 请通过[扩充以下内容](https://vic3.paradoxwikis.com/index.php?title=Diplomatic_play&action=edit)来帮助改进本条目或章节：巨浪（Great Wave）新增的四个外交博弈。 |
|---|---|

## 参考

1. ↑ 参见 /Victoria 3/game/common/defines/00_defines.txt：WAR_GOAL_INFAMY_POPULATION_SCALING_FACTOR WAR_GOAL_INFAMY_POPULATION_SCALING_MULTIPLIER WAR_GOAL_INFAMY_POPULATION_SCALING_MULTIPLIER_MAX_PER_STATE WAR_GOAL_INFAMY_POPULATION_SCALING_MULTIPLIER_MAX_TOTAL
2. ↑ 参见 /Victoria 3/game/common/defines/00_defines.txt：`WAR_GOAL_INFAMY_HOMELAND_FACTOR` 和 `WAR_GOAL_INFAMY_UNINCORPORATED_FACTOR`
3. ↑ 3.0 3.1 从技术上讲，拥有变量 `por_seeking_restore_union_var`