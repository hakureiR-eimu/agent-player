---
translated: 2026-10-28
translator: machine (glm-4.5-air/glm-4.7)
title: Chinese content
source: https://vic3.paradoxwikis.com/Chinese_content
pageid: 7339
categories: [Potentially_outdated, 1.10, Expand, Scripted_content, Articles_with_potentially_outdated_infoboxes, Pages_with_obsolete_template_parameters, Events, Journal]
fetched: 2026-10-27
---
请协助验证或更新本文的较旧章节。其中至少有一部分内容最后验证于 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10。

|  | 请协助[扩充](https://vic3.paradoxwikis.com/index.php?title=Chinese_content&action=edit)本文或该章节。 |
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
俄罗斯
南部非洲
•
南美洲
西班牙
•
土耳其
特殊内容页面
万圣节
[中国](China.md)拥有以下国家专属的[事件](Events.md)、[日志条目](https://vic3.paradoxwikis.com/Journal_entries)和[决议](Decision.md)。

## 脆弱的统一

如果太多事情出了差错，中国有机会分裂成众多较小的国家，即未能避免或承受各种曾导致历史上清朝崩溃的历史事件。

以下每个事件都会从进度条上移除一点，进度条耗尽时会触发*中国破碎*事件。可重复事件只在首次发生时移除进度。

- 输掉鸦片战争
- [太平天国](Heavenly Kingdom.md)的出现
- 未能击败太平天国
- 未能击败义和团叛乱
- 承担**任何**贷款
- 发生内战
- 成为[附属国](Subject.md)
- 废除君主制

以下情况可以逆转此进度条的进度：

- 赢得鸦片战争
- 成为[受认列强](https://vic3.paradoxwikis.com/Recognized_power)
- 完成*根除君主主义*日志条目
- 击败义和团叛乱

id

### 脆弱的统一

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。其内容最后验证于版本 1.10。 |
|---|---|

---

根据特定条件，进度条的状态会前进或后退。进度条到达 0% 将导致中央政府完全失去控制，专制的地方势力夺取政权。
尽管在雍正和乾隆皇帝治下曾有一段短暂的稳定时期，中国已在叛乱、治理不善和外部压力之下开始了稳步滑向崩溃的进程。如果中央政府的权威被充分削弱，[大清]内部的地方军事势力就有可能将国家撕成零碎的封地。
---

| 可见性条件：仅在激活期间 |  |
|---|---|
| 激活方式：游戏开始 | 激活时效果：无 |
| 完成条件：成功完成义和团叛乱 [1] 日志条目 已受认 成功完成根除君主主义日志条目 | 完成时效果：触发事件 百年凯旋 |
| 失败条件：进度条已达 0% | 失败时效果：触发事件 中国破碎 |

id

### 中国破碎

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。其内容最后验证于版本 1.10。 |
|---|---|

---

清朝的覆灭终结了中国长期的帝制统治，开启了一个军阀混战的新时代。
---

风味文本：
“帝国如梦，由无形之物构成，脆弱至极，随时可能在毫无预兆的情况下终结。然而它们同样有着疯狂的魅力。即使缝合其裂口的线是看不见的，每道缝线之下都藏着伤口。
数千年的帝制统治，顷刻之间宣告终结。”
---

| 触发来源：日志条目脆弱的统一失败 |
|---|
| 触发条件：无 |
| 立即效果：按顺序释放以下中国小国（若其首都州在其控制之下）：湖南 ， 湖南 大成 ， 广西 安徽 ， 皖南 直隶 ， 河北 满洲 ， 吉林南部 山西 ， 山西 回疆 ， 塔里木盆地 云南 ， 云南 贵州 ， 贵州 越 ， 广东西部 四川 ， 四川 山东 ， 山东 西北 ， 宁夏 蒙古 ， 乌里雅苏台（同时获得库伦） 图瓦 ， 图瓦 阿尔泰 ， 阿尔泰 每释放一个：从中国复制技术和法律 激活独裁制、总统共和制和农民征召兵 若不是蒙古、图瓦和阿尔泰，设为"军阀国家" 一名随机中国指挥官成为统治者 若首要文化不是汉或满，获得汉作为首要文化 若有单一民族国家或民族至上，失去藏族或维吾尔族作为首要文化 每个人物有 20% 概率获得土匪特质 所有附属国独立 最多选出四个随机军阀国家 |
| 我们必须挽救这一局面。将非首都州随机分配给邻近的军阀国家 更改国家代码为 Beiyang [统治者头衔][姓名]将再造中华！将中国的非首都州随机分配给邻近的军阀国家 中国更改为 Beiyang 扮演选定的军阀国家 |

id

### 百年凯旋

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。其内容最后验证于版本 1.10。 |
|---|---|

---

一段勤勉的现代化与中央集权努力终于终结了小军阀分裂国家的风险。尽管内外敌人百般阻挠，[中国]依然昂首屹立、团结统一。
---

风味文本：
在地平线的尽头，夕阳的余晖中，是最后几艘外国船只。它们的旗帜降了半桅，这分明是它们夹着尾巴逃走的铁证。而在海上与之相对的，是一面高高飘扬的中国旗帜，矗立在中国的土地上。给世界的信息很清楚：中国的天命仍掌握在自己手中。唯有中国人民将开创自己的未来。
---

| 触发来源：日志条目脆弱的统一完成 |
|---|
| 触发条件：无 |
| 一个延续至时间尽头的国家。获得 百年凯旋 百年凯旋 国家修正 +25 合法性 −25% 法令花费 持续 10 年 10% 的人口变得更 我们人民的天才智慧将引领我们不断前行。获得 百年凯旋 百年凯旋 国家修正 +25% 研究速度 +50% 技术扩散 持续 10 年 10% 的人口变得更 |

## 鸦片战争

此内容表现了 19 世纪初清帝国的鸦片危机。它有可能为任何首要文化拥有鸦片[痴迷](https://vic3.paradoxwikis.com/Obsession)的大型未受认国家触发。汉文化开局即拥有此种痴迷，因此此内容通常在游戏早期为[中国](China.md)触发。

id

### 鸦片危机（日志条目）

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。其内容最后验证于版本 1.10。 |
|---|---|

---

我民中有大批人沦为鸦片瘾君子。这是必须紧急处理的国耻。
---

| 可见性条件：仅在激活期间 |  |
|---|---|
| 激活方式：事件 鸦片危机 | 激活时效果：无 |
| 条目按钮：禁止鸦片贸易 摧残我们国家的鸦片危机必须被制止。政府必须对鸦片贸易实行全面禁令，限制进口和国内生产。可见条件：是市场所有者 未禁止鸦片 启用条件：未颁布自由放任 未输掉鸦片战争 效果：禁止鸦片 获得 鸦片禁令 鸦片禁令 国家修正 −20% 权威力 解除鸦片禁令 如果外交或经济形势需要，解除鸦片禁令可能是恰当的。可见条件：是市场所有者 正在禁止鸦片 效果：解禁鸦片 移除 鸦片禁令 鸦片禁令 国家修正 −20% 权威力 |  |
| *摧残我们国家的鸦片危机必须被制止。政府必须对鸦片贸易实行全面禁令，限制进口和国内生产。* |  |
| **可见条件：** 是市场所有者 未禁止鸦片 |  |
| **启用条件：** 未颁布自由放任 未输掉鸦片战争 |  |
| **效果：** 禁止鸦片 获得 鸦片禁令 鸦片禁令 国家修正 −20% 权威力 |  |
| *如果外交或经济形势需要，解除鸦片禁令可能是恰当的。* |  |
| **可见条件：** 是市场所有者 正在禁止鸦片 |  |
| **效果：** 解禁鸦片 移除 鸦片禁令 鸦片禁令 国家修正 −20% 权威力 |  |
| 完成条件：以下条件须累计满足 60 个月 正在禁止鸦片 处于和平状态 | 完成时效果：触发事件 瘾患终结 |
| 失败条件：以下任意一条： 已颁布自由放任 任何拥有鸦片战争日志条目的国家与此国拥有条约港或投资权利 | 失败时效果：触发事件 鸦片战争：败北 |
| 10 年后超时，效果如下：获得 泛滥的鸦片瘾 泛滥的鸦片瘾 国家修正 −50% 来自陆军力量投送的威望 +100% 来自伤亡的战争疲惫 −1 生活水平 +1% 死亡率 +25% 来自政治运动的激进派 −25% 来自政治运动的忠诚派 −50% 进攻 −50% 防御 +75% 士气损失 再持续 10 年 10% 的人口变得更激进 将脆弱的统一的进度减少 1 |  |
| 每月：100：无事件 10：鸦片走私贩 5：戒除瘾患 5：鸦片成瘾 |  |

id

### 鸦片战争（日志条目）

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。其内容最后验证于版本 1.10。 |
|---|---|

---

我们必须通过确保鸦片贸易继续进行来保护我们的经济利益。
---

| 可见性条件：仅在激活期间 |  |
|---|---|
| 激活方式：事件 鸦片战争 | 激活时效果：无 |
| 完成条件：与[中国]拥有条约港或投资权利 | 完成时效果：触发事件 鸦片战争：胜利 |
| 失败条件：[中国]的任何首要文化都没有鸦片痴迷 | 失败时效果：无 |
| 失效条件：[中国]不存在 | 失效时效果：无 |
| 5 年后超时，效果如下：无 |  |

id

### 鸦片危机（事件）

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。其内容最后验证于版本 1.10。 |
|---|---|

---

鸦片成瘾正在摧残[中国]。大批[汉]人沦为鸦片瘾君子，引发了一波犯罪、贫困与游手好闲的浪潮。尽管危害显而易见，[英国]仍在继续向市场倾销。
---

风味文本：
家家户户都有卧床不起的鸦片瘾君子，街头巷尾都有鸦片烟馆，每个港口都迎接着[英国]商人，他们把堆积如山的鸦片灌进任何一个肯付钱的人的喉咙里。
---

| 触发来源：每月脉冲 |
|---|
| 触发条件：之前未收到过此事件 任何首要文化拥有鸦片痴迷 是未受认国家 人口超过 500 万 在任意州拥有贸易中心 是独立国家 没有自由放任 没有国家是鸦片战争的目标 一个主要政权或列强：与此国没有条约港或投资权利 此国的鸦片进口中超过 25% 来自该国市场 没有泛滥的鸦片瘾 泛滥的鸦片瘾 国家修正 −50% 来自陆军力量投送的威望 +100% 来自伤亡的战争疲惫 −1 生活水平 +1% 死亡率 +25% 来自政治运动的激进派 −25% 来自政治运动的忠诚派 −50% 进攻 −50% 防御 +75% 士气损失 |
| 我们必须做点什么！激活日志条目 鸦片危机 获得 泛滥的鸦片瘾 泛滥的鸦片瘾 国家修正 −50% 来自陆军力量投送的威望 +100% 来自伤亡的战争疲惫 −1 生活水平 +1% 死亡率 +25% 来自政治运动的激进派 −25% 来自政治运动的忠诚派 −50% 进攻 −50% 防御 +75% 士气损失 持续 10 年 一个随机的相关主要政权或列强：收到事件 鸦片战争 我们不能冒触怒[英国]的风险。获得 泛滥的鸦片瘾 泛滥的鸦片瘾 国家修正 −50% 来自陆军力量投送的威望 +100% 来自伤亡的战争疲惫 −1 生活水平 +1% 死亡率 +25% 来自政治运动的激进派 −25% 来自政治运动的忠诚派 −50% 进攻 −50% 防御 +75% 士气损失 持续 20 年 5% 的人口变得更激进 将脆弱的统一的进度减少 1 |
id

### 鸦片战争（事件）

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助核实或更新此信息框。此信息框最后核实于 1.10 版本。 |
|---|---|

---

[Chinese] 政府已宣布打算终结 [China] 的鸦片贸易。由于 [Country] 是主要的鸦片出口国，这是一个重大的经济关切问题。
---

风味文本：
"有人谴责鸦片贸易所谓的道德罪恶；我要对他们说，你们凭什么阻挡自由贸易和消费者的自由选择？需求就在那里，我们便提供供给——即便不是我们，也会有别的国家靠 [Han] 鸦片瘾君子的痛苦发财致富。难道仅仅因为一些不负责任的蠢货滥食鸦片，就要剥夺所有人的鸦片吗？难道要让每一个 [Country] 家庭都失去鸦片为我国带来的财富吗？"
---

| 触发方式：事件 Opium Crisis |
|---|
| 触发条件：无 |
| 他们会乖乖吸食鸦片并乐在其中！激活以 [China] 为目标的日志条目 Opium Wars 与 [China] 关系 −30 在 South China 区域获得 2500 参与度 我们还有别的事要处理。与 [China] 关系 +50 每个拥有鸦片种植园的直接附属国：与 [Country] 关系 −50 独立倾向 +50 |

id

### 戒除毒瘾

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助核实或更新此信息框。此信息框最后核实于 1.10 版本。 |
|---|---|

---

以下描述是此事件可选描述之一。
我们凭借顽强的毅力打破了 [Han] 对鸦片的依赖。即使是 [Great Britain] 的阴谋诡计也无法阻止我们让 [China] 重归健康与繁荣。
---

风味文本：
正如瘾君子会戒除毒瘾、从懒惰的床榻上站起来一样，我们的国家也将挣脱外国影响的可憎枷锁，以主权国家之姿重新崛起。不再被鸦片淹没的我们，河流中将流淌白银，人民将回归有德行的生活。
---

| 触发方式：日志条目 Opium Crisis 完成 |
|---|
| 触发条件：无 |
| 立即效果：失去 Widespread Opium Addiction Widespread Opium Addiction 国家修正 −50% Prestige from army power projection +100% War exhaustion from casualties −1 Standard of Living +1% Mortality +25% Radicals from political movements −25% Loyalists from political movements −50% Offense −50% Defense +75% Morale loss 禁止鸦片 Fragile Unity 进度 +1 [China] 的主权是绝对的。所有主流文化失去 opium obsession 获得 Sovereignty Asserted Sovereignty Asserted 国家修正 +20% 权威力 +20% 影响力 合法性 +20，持续 20 年 和谐将重回 [China]。所有主流文化失去 opium obsession 获得 Opium Recovery Opium Recovery 国家修正 −2% Mortality −25% Radicals from political movements +25% Loyalists from political movements，持续 20 年 |

id

### 鸦片战争：战败

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助核实或更新此信息框。此信息框最后核实于 1.10 版本。 |
|---|---|

---

以下描述是此事件可选描述之一。
我们在 [Country] 手中蒙受的屈辱战败迫使我们割让 [State] 的港口。不仅鸦片的流入将继续不受阻碍，我们的主权也遭到侵犯，民众怒火中烧。
---

风味文本：
那个统治和谐之土数百年的国家在哪里？我们是鸦片的奴隶，任凭外国贪婪摆布。我们无法控制自己的港口，外国人对我们的 [Ruler Title] 毫无敬意，家家户户不满的低语日益高涨。黑暗的日子即将来临；天命或许已经到了尽头。
---

| 触发方式：日志条目 Opium Crisis 失败 |
|---|
| 触发条件：50 年内未发生过 |
| 他们可能预示着 [China] 的终结。失去 Widespread Opium Addiction Widespread Opium Addiction 国家修正 −50% Prestige from army power projection +100% War exhaustion from casualties −1 Standard of Living +1% Mortality +25% Radicals from political movements −25% Loyalists from political movements −50% Offense −50% Defense +75% Morale loss Fragile Unity 进度 −1 10% 的人口变得更加激进 解除鸦片禁令 移除 Opium Ban Opium Ban 国家修正 −20% 权威力 |

id

### 鸦片战争：胜利

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助核实或更新此信息框。此信息框最后核实于 1.10 版本。 |
|---|---|

---

以下描述是此事件可选描述之一。
我们迫使 [China] 在 [State] 割让了一处条约港，确保了鸦片贸易在今后多年得以延续。
---

风味文本：
"结束了，大使。告诉你的 [Ruler Title] 在条约上签字，否则后果会非常严重。你们将向我们开放港口，你们将在一切贸易事务上与我国官员合作，你们将支付目前正在蹂躏你们土地与人民的士兵的工资。你们将屈服。"
---

| 触发方式：日志条目 Opium Wars 完成 |
|---|
| 触发条件：无 |
| [Country] 统治海浪！获得 Opium Wars: Rule the Waves Opium Wars: Rule the Waves 国家修正 +20% Morale damgage，持续 5 年 让他们去吃鸦片吧。获得 Opium Wars: Masters of Trade Opium Wars: Masters of Trade 国家修正 +10% Trade route competitiveness，持续 5 年 |

id

### 鸦片走私犯

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助核实或更新此信息框。此信息框最后核实于 1.10 版本。 |
|---|---|

---

[Chinese] 巡逻队抓获了一批向 [China] 走私鸦片的 [Country] 走私犯。这是 [Country] 企图绕过鸦片禁运的公然行径。
---

风味文本：
"走私犯？根本不是！我们是诚实的商人，正合法地把货物运往你们美丽的国家。"
"我们当然有正式的文件。你要我们接受船只检查？恐怕这不可能。货舱里有一窝可怕的……呃……食人獾。"
"我向你保证这全是误会！把你的手拿开！我要求见 [Country] 大使！"
---

| 触发方式：日志条目 Opium Crisis 每月脉冲 |
|---|
| 触发条件：正在禁止鸦片 任一国家拥有日志条目 Opium Wars 没有 modifier Executing Opium Smugglers Executing Opium Smugglers 国家修正 +10% 权威力 或 Humiliated Opium Smugglers Humiliated Opium Smugglers 国家修正 +10% 影响力 50 年内未发生过 |
| 处决走私犯。获得 Executing Opium Smugglers Executing Opium Smugglers 国家修正 +10% 权威力，持续 2.5 年 与 [Country] 关系 −20 给他们戴上镣铐送回去。获得 Humiliated Opium Smugglers Humiliated Opium Smugglers 国家修正 +10% 影响力，持续 2.5 年 与 [Country] 关系 −10 |

id

### 戒瘾康复

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助核实或更新此信息框。此信息框最后核实于 1.10 版本。 |
|---|---|

---

[China] 为应对鸦片危机所采取的措施正在见效。[State] 的公民已完全康复，整个地区也都能观察到类似的进展。
---

风味文本：
"我曾麻木于一切思想与感受，卧床不起、浑浑噩噩。如今又能活动、思考、感受，并去爱这世界所提供的一切欢乐……然而我仍感到它的诱惑。我必须抵抗。"
---

| 触发方式：日志条目 Opium Crisis 每月脉冲 |
|---|
| 触发条件：正在禁止鸦片 拥有 modifier Widespread Opium Addiction Widespread Opium Addiction 国家修正 −50% Prestige from army power projection +100% War exhaustion from casualties −1 Standard of Living +1% Mortality +25% Radicals from political movements −25% Loyalists from political movements −50% Offense −50% Defense +75% Morale loss 任一拥有的州：没有 modifier Love for the State Love for the State 州修正 +50% Loyalists from political movements 或 Addiction Recovery Addiction Recovery 州修正 −2.5% Mortality +1 Standard of living 拥有 opium obsession 的人口 5 年内未发生过 |
| 加倍专注于照料病患。[State] 获得 Addiction Recovery Addiction Recovery 州修正 −5% Mortality +2 Standard of living 他们对鸦片的爱将被对 [China] 的爱所取代。[State] 获得 Love for the State Love for the State 州修正 +50% Loyalists from political movements，持续 5 年 35% 的人口变得更加忠诚 |

id

### 鸦片成瘾

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助核实或更新此信息框。此信息框最后核实于 1.10 版本。 |
|---|---|

---

以下描述是此事件可选描述之一。
[Culture] 人正遭受鸦片成瘾的严重后果。该物质的使用与滥用已在 [State] 蔓延。
---

风味文本：
食鸦片者卧于梦魇与梦淫妖的重压之下；他眼睁睁看着自己渴望完成的一切却无能为力，正如一个因弛缓性疾病致命的疲惫而被强禁于床榻之人，被迫目睹最亲爱之物遭受伤害或凌辱：他诅咒将他锁在原地无法动弹的魔咒；只要能起身行走，他宁愿舍弃性命；但他却如婴儿般软弱无力，甚至无法尝试起身。
---

| 触发方式：任一：日志条目 Opium Crisis 每月脉冲 年度事件脉冲 |
|---|
| 触发条件：任一拥有的州：没有 modifier Opium Addiction Opium Addiction 州修正 +3% Mortality 拥有 opium obsession 的人口 5 年内未发生过 |
| 选项条件 启用条件：Health System 等级低于 2 悲剧！[State]：获得 Opium Addiction Opium Addiction 州修正 +3% Mortality，持续 5 年 获得 −2 standard of living（对 [Culture]），持续 10 年 启用条件：Health System 等级 2 或更高 或许我们可以把这个问题当作医疗事务处理。[State] 获得 −1 standard of living（对 [Culture]），持续 10 年 |

id

### 解除鸦片禁令

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助核实或更新此信息框。此信息框最后核实于 1.10 版本。 |
|---|---|

---

如果外交或经济形势需要，解除鸦片禁令或许是明智之举。
---

| 显示条件：是市场所有者 正在禁止鸦片 没有日志条目 Opium Crisis | 可用条件：正在禁止鸦片 |
|---|---|
| 效果：解除鸦片禁令 移除 Opium Ban Opium Ban 国家修正 −20% 权威力 移除 Opium Recovery Opium Recovery 国家修正 −20% Mortality −25% Radicals from political movements +25% Loyalists from political movements |  |

## 义和团运动

义和团运动是一个日志条目，要求中国拥有 Pan-Nationalism 技术、任何属于 Han 文化故土的州区域中存在一个并非完全由中国拥有的州（通常是 [Portugal](Portugal.md) 在 Western Guangdong 的条约港），并且该州至少有 10% 的激进 Han 人口。如果中国完全拥有所有作为 Han 文化故土的州区域，则该日志条目成功。成功会带来大幅的忠诚派提升以及小幅的稳定度提升，并满足解决 Fragile Unity 日志条目的条件之一。失败则会使 Fragile Unity 日志条目更有可能失败，并导致激进主义大幅增加，和/或失去 Manchu 作为主流文化。
id

### 义和团运动

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。该内容最后一次验证针对的版本为 1.10。 |
|---|---|

---

将中国土地屈辱地割让给外国"蛮夷"，催生了众多以武术为号召的民团组织，他们矢志清除国内一切外国势力。
若未能实现民团的愿景，可能产生剧烈的后果，波及 [China]。
---

| 可见条件：是中国 已研究民族主义 拥有满族作为主体文化 |  |
|---|---|
| 激活条件：已研究泛民族主义 任意州： 是汉族故土 不属于中国 | 激活时效果：触发事件 义和团运动 |
| 完成条件：所有汉族故土均由中国拥有，且不是分裂州。 | 完成时效果：触发事件 天命 |
| 5 年（60 个月）后超时，效果如下：触发事件 清与汉 |  |

id

### 义和团运动

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。该内容最后一次验证针对的版本为 1.10。 |
|---|---|

---

对 [China] 境内日益增长的外国势力深感愤怒，[Han] 臣民正在组织反外民团，决心将"蛮夷"赶回大海。如今许多人敦促 [Ruler Title] [Ruler] 支持这场运动，以免他们的怒火转向 [Manchu] 统治。
---

风味文本：
"洋人传教时，口称劝人为善，实则乱我朝政、扰我制度、毁我风俗、骗我子民——也就是说，他们要让中国人变成蛮夷。"
---

| 触发方式：日志条目 义和团运动 激活 |  |
|---|---|
| 触发条件：无 | |
| 复兴大清！消灭洋人！ 与所有拥有汉族故土的国家关系 −100 [China] 内 [Protestant] 人口 +20% 变得更激进 [China] 内天主教人口 +20% 变得更激进 [China] 内东正教人口 +20% 变得更激进 [China] 内汉族人口 +10% 变得更激进 这些狂热分子会给我们带来灭顶之灾。 与所有拥有汉族故土的国家关系 +20 [China] 内汉族人口 +20% 变得更激进 | |

id

### 天命

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。该内容最后一次验证针对的版本为 1.10。 |
|---|---|

---

黄龙旗再一次飘扬在中原大地所有城市的屋顶上。从南三角洲沿线的璀璨明珠，到东海之滨的繁华都会，帝国主义的污迹已从我们的海岸上被洗刷一净。
---

风味文本：
"当洋鬼子最终
被尽数逐出国门，
[China] 团结一心，
将为我神州大地带来太平。"
---

| 触发方式：日志条目 义和团运动 完成 |  |
|---|---|
| 触发条件：无 | |
| 愿 [Ruler Title] [Ruler] 万岁千秋！ [China] 内汉族人口 +20% 变得更忠诚派 获得 Revere the Emperor Revere the Emperor 国家修正 动荡造成的州惩罚 −20%，持续 10 年 Fragile Unity 日志条目的进度条 +1 愿 [China] 国祚万年！ [China] 内汉族人口 +20% 变得更忠诚派 获得 United in Righteousness United in Righteousness 国家修正 政治运动产生的激进派 −20% Violent Hostility 状态的激进主义 −10% Cultural Erasure 状态的激进主义 −10% Open Prejudice 状态的激进主义 −10%，持续 10 年 Fragile Unity 日志条目的进度条 +1 | |

id

### 清与汉

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。该内容最后一次验证针对的版本为 1.10。 |
|---|---|

---

昔日"复兴大清"的热切呼喊回荡之处，如今已被反 [Manchu] 的口号所取代。我们未能实现义和团的愿景，已不可挽回地割裂了我们与 [Han] 臣民的纽带。
---

风味文本：
"我不厌其烦地一再重申：对内我们是满人的奴隶，饱受其暴政之苦；对外我们受列强侵扰，遭受双重奴役。"
---

| 触发方式：日志条目 义和团运动 超时 |  |
|---|---|
| 触发条件：无 | |
| 这些屈辱何时才是尽头？ Fragile Unity 日志条目的进度条 −1 [China] 内汉族人口 +20% 变得更激进 [Capital] 驻军叛乱，攻入紫禁城。现任统治者和继承人被杀 若年份早于 1862：Fanhao Kong 成为统治者 Xiangke Kong 成为继承人 若年份为 1862 年或之后、1876 年之前：Xiangke Kong 成为统治者 Lingyi Kong 成为继承人 若年份为 1876 年或之后、1920 年之前：Lingyi Kong 成为统治者 Teh Cheng Kong 成为继承人 若年份为 1920 年或之后：Teh Cheng Kong 成为统治者 Fragile Unity 日志条目的进度条 −1 若施行的公民权法律不是附属身份或单一民族国家，则将其改为包容程度低一级的法律。（例如文化排斥改为种族隔离） 移除满族作为主体文化 [China] 内满族人口 +75% 变得更激进 | |

id

### 清朝的覆灭

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。该内容最后一次验证针对的版本为 1.10。 |
|---|---|

---

落笔之间，两个世纪的帝制统治宣告终结。当最后一位满族皇帝被护送出紫禁城，全世界的目光转向东方。这个新时代将为 [China] 带来什么？
---

风味文本：
"要恢复我们民族的独立，必先恢复中华民族。要恢复中华民族，必先驱逐满族蛮夷回长白山。要驱逐蛮夷，必先推翻当今残暴独裁、丑陋腐朽的清政府。"
---

| 触发方式：中国未启用君主制 |  |
|---|---|
| 触发条件：无 | |
| 满族的枷锁终于终结。 Fragile Unity 日志条目的进度条 −1 移除满族作为主体文化 [China] 内满族人口 +20% 变得更激进 现在是和解之时。 [China] 内汉族人口 +20% 变得更激进 | |

## 天国

WIP

## 重新统一中国

id

### 军阀时代

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。该内容最后一次验证针对的版本为 1.12。 |
|---|---|

---

中央政府权威的崩溃，导致各地竞相崛起的军事势力遍及中国。若想从废墟中重建中国，我们必须确立自己超越又一个
Warlord State（军阀国家）
的地位。
在此日志条目激活期间，势力较弱的军阀国家将更倾向于互相援助，对抗更强大的国家。
---

| 可见条件：仅在激活时 |  |
|---|---|
| 激活条件：中国未通过 Fragile Unity 日志条目 满足以下至少一项： 汉族是国内主体文化 满族是国内主体文化 | 激活时效果：无 |
| 条目修正：Warlord Era Warlord Era 国家修正 军官政治力量 +75% 军队政治力量 +30% 军队人口吸引力 +10% |  |
| 完成条件：每个以汉、满、粤、彝或客家为主体文化的国家已被吞并或成为我们的附属国 满足以下至少一项：ROOT 拥有全部南京 ROOT 拥有全部北京 已组建中华国家 ROOT 未施行任何变体的农民征召兵 | 完成时效果：触发事件 中国重新统一 |

id

### 中国重新统一

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。该内容最后一次验证针对的版本为 1.12。 |
|---|---|

---

凭借人民的勤勉和士兵的英勇，最后的军阀军队已被击败或归顺。
中国
重新统一，比以往任何时候都更强大。
---

风味文本：
她从未见过天空中如此多的光芒。红、黄、粉三色的火花汇成海洋，把黑夜照成白昼，其间还夹杂着更多烟花的爆响。在她家楼下的街道上，邻居们放飞了一群群闪亮的灯笼，在烟花绽放的高处与之相会。
节日终会结束——毕竟补给有限，人们也需要睡眠——但它所象征的时刻却不会。中国重归一统——不可分割、主权独立、永恒长存。
---

| 触发方式：日志条目 军阀时代 完成 |  |
|---|---|
| 触发条件：无 | |
| 我们的国家必须永远不可分割。 中国内人口 +10% 变得更忠诚派 中国获得对所有尚未拥有的汉、满、藏、维吾尔、图瓦和蒙古故土州区域的宣称 让我们倾尽全力投入重建。 中国获得 Reunified China Reunified China 国家修正 权威力 +200 行政力 +10% 合法性 +15，持续 5 年 | |

id

### 砸西瓜

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。该内容最后一次验证针对的版本为 1.12。 |
|---|---|

---

[General] [SCOPE.sCharacter('prisoner_killing_warlord').GetFullName] 以用刀劈碎囚犯头颅取乐一事，正面临人尽皆知的风险。
---

风味文本：
"你知道为什么有人叫我老八十六吗？那是因为我的……"
[General] 的余下话语被惨叫和骨裂声淹没，[he/she] 将刀劈向一名囚犯的头顶。'
"……整整八十六块墨西哥银元。"
---

| 触发方式：年度脉冲 |  |
|---|---|
| 触发条件：ROOT 的统治者具有残忍特质 ROOT 有激活中的军阀时代日志条目 | |
| 人民应当知道。 首都州人口 +20% 变得更激进 最好把这事掩盖过去。 ROOT 获得 Prisoner Murder Covered Up Prisoner Murder Covered Up 国家修正 权威力 −15%，持续 5 年 | |

id

### [Yan Xishan] 思想

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此信息框。该内容最后一次验证针对的版本为 1.12。 |
|---|---|

---

我们伟大的 [General] 设计了一套精心构思的新意识形态，旨在统一国家。它博采众家之长，体系复杂，可能难以向大众传达。
---

风味文本：
"我们光辉的新意识形态包罗万象，融合了军国主义、民族主义、无政府主义、民主主义、资本主义、共产主义、个人主义、帝国主义、普世主义、家长主义和乌托邦主义的一切可取之处。"
---

| 触发方式：年度脉冲 |  |
|---|---|
| 触发条件：ROOT 有激活中的军阀时代日志条目 ROOT 施行了独裁制的任意变体 ROOT 已研究大众宣传 统治者的利益集团尚未拥有 Unifying Thought Unifying Thought 国家修正 权威力 +10% 利益集团人口吸引力 +20% 或 Confusionism Confusionism 国家修正 权威力 −10% 利益集团人口吸引力 −10% 国家未拥有 State Legitimacy State Legitimacy 国家修正 合法性 +10 修正 | |
| 传播 [SCOPE.sCharacter('yan_xishan_thinker').GetFullName] 的思想！ 将发生 2 个选项之一： 权重 50 若任一拥有的大学启用了哲学系则权重 +25 若政府合法性 > 75 则权重 +25 概率触发：获得 Unifying Thought Unifying Thought 国家修正 权威力 +10% 利益集团人口吸引力 +20%，无限期 权重 50 若政府合法性 < 50 则权重 +25 概率触发：获得 Confusionism Confusionism 国家修正 权威力 −10% 利益集团人口吸引力 −10%，持续 10 年 这完全讲不通。 还是专注于巩固国家合法性吧。 ROOT 获得 State Legitimacy State Legitimacy 国家修正 合法性 +10，持续 10 年 | |
## 参考资料

1. ↑ 提示框中将 "Boxer Rebellion" 误拼为 "Boxer Rebelion"

主要参考文件：

- /Victoria 3/game/common/journal_entries/00_boxer_rebellion.txt
- /Victoria 3/game/common/journal_entries/00_opium_wars.txt
- /Victoria 3/game/common/journal_entries/00_reunify_china.txt
- /Victoria 3/game/common/journal_entries/00_taiping.txt
- /Victoria 3/game/common/journal_entries/00_warlord_china.txt
- /Victoria 3/game/events/boxer_rebellion_events.txt
- /Victoria 3/game/events/heavenly_kingdom_events.txt
- /Victoria 3/game/events/opium_wars_events.txt
- /Victoria 3/game/events/warlord_china_events.txt