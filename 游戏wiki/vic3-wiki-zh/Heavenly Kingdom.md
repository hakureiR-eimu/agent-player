---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Heavenly Kingdom
source: https://vic3.paradoxwikis.com/Heavenly_Kingdom
pageid: 5261
categories: [Pages_using_TabberTransclude_parser_tag, 1.13, Countries, Articles_with_potentially_outdated_sections, Pages_with_obsolete_template_parameters, Articles_with_potentially_outdated_infoboxes, Pages_with_interwiki_links_to_Wikipedia, Articles_with_potentially_outdated_guides]
fetched: 2026-10-27
---
本文已针对游戏当前[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

太平天国
---

首都
：
南京，或以叛乱形式出现
---

政府类型
：
太平天国
---

主流文化
：
汉、客家
---

国教
：
新教
---

国家等级
：
帝国
---

国家类型
：
未开化
太平天国
---

首都
：
南京，或以叛乱形式出现
---

政体
：
太平天国
---

主流文化
：
汉、客家
---

国教
：
新教
---

等级
：
帝国
---

类型
：
未开化
*人民已经起来反抗大清的邪恶与腐败。清的统治必须被终结，为中国带来一个天下太平的新时代。*

**太平天国**（Heavenly Kingdom）是[中国](China.md)的一个特殊叛乱国。当中国未能完成日志条目*The Heavenly Kingdom*时它便会出现。太平天国叛乱时，会立即开启一个特殊外交博弈*Taiping Rebellion*（太平天国叛乱），若该博弈被强制执行，将吞并对立国家。

## 成立

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助核实或更新此章节。其最后核实版本为1.10。 |
|---|---|

未能完成日志条目*The Heavenly Kingdom*会导致太平天国生成。失败条件为：有四个州带有*God Worshipping Society God Worshipping Society State modifier +25% Radicals from political movements*修正，且存在一个这样的州：既含有宗教受到歧视的新教人口（该州对新教的接纳度小于等于10），又有至少15%的动荡（注意动荡通常在达到25%之前不会显示在UI中，因此追踪这类州需要额外功夫）。而这些条件又由日志条目*The Chinese Missions*引发的事件造成，其中许多事件不可避免地会使人口改信新教或增加激进程度。

*The Chinese Missions*在以下条件全部满足时激活：

- 中国输掉了鸦片战争，或其迁移法律不是封闭边界（Closed Borders）
- 任一相邻州是一个基督教国家的条约港（Treaty Port）
- 中国的经济系统法律不是孤立主义（Isolationism）或其变体（即广州体系）

*The Heavenly Kingdom*在以下条件全部满足时激活：

- 中国存在且不是其他国家的附属国
- 年份为1856年或之后；或者，如果*Missionary Works in [PROVINCE]*事件已触发至少5次，则为1846年或之后
- 中国境内任意一个已整合的、非首都的州，是汉或客家的本土，既含有新教人口，又有超过15%的动荡

如果*The Chinese Missions*被触发，那么*The Heavenly Kingdom*几乎必然会触发；但即使你阻止了前者，后者最终仍可能触发，因为在游戏版本1.8.6中，它只检查新教徒是否在中国**存在**，而不检查他们是否受到歧视。通过颁布政教完全分离（Total Separation）仍可避免该日志条目的失败条件，但即使政教完全分离也无法阻止该日志条目触发并带来麻烦。

## 脚本内容

id

### 天国革命

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助核实或更新此信息框。其最后核实版本为1.10。 |
|---|---|

---

人民已经起来反抗[中国]的邪恶与腐败。[中国人]的统治必须被终结，为中国带来一个天下太平的新时代。
---

| 可见条件：仅在激活时可见 |  |
|---|---|
| 激活方式：事件 The Heavenly Kingdom | 激活效果：无 |
| 完成条件：中国不存在或与太平天国停战 | 完成效果：触发事件 The Rise of Heaven 失败 The Taiping Rebellion The Taiping Rebellion 国家修正 −25% War exhaustion from casualties +5% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility pops 所有利益集团失去 Siblings In Revolution Siblings In Revolution 利益集团修正 +5 Approval +25% Pop attraction |

id

### 天朝崛起

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助核实或更新此信息框。其最后核实版本为1.10。 |
|---|---|

---

以下描述是该事件若干可用描述之一。
太平天国已扫除满清统治。我们的国家必须继续存续，将上帝的话语传遍全中国。
---

背景文本：
当世上之人不藏私财，将万物献于上帝供众人共用，则处处均分，人人饱暖。
---

| 触发方式：完成日志条目 The Heavenly Revolution |
|---|
| 触发条件：无 |
| 选项条件 始终可用：优先向人民传播上帝的话语。获得 The Conversion of China The Conversion of China 国家修正 +50% Conversion，持续10年 始终可用：《资政新篇》的改革将推动我们的国家前进。士人获得 Accepted the New Treatise Accepted the New Treatise 利益集团修正 +5 Approval +25% Political strength，持续5年 获得 A New Treatise on Aids to Administration A New Treatise on Aids to Administration 国家修正 +10% Bureaucracy +5% Taxation capacity +10% State construction efficiency，持续10年 满足条件时可用：中国存在 我们要准备再次与满清妖魔开战。武装力量的领袖获得沙文主义者（Jingoist）意识形态 武装力量获得 Hawkish Neighbor Relations Hawkish Neighbor Relations 利益集团修正 +3 Approval，持续5年 获得 Vigilance Against the Fallen Dynasty Vigilance Against the Fallen Dynasty 国家修正 +15% Barracks throughput +15% Arms Industry throughput +15% Artillery Foundry throughput +10% Assimilation，持续10年 始终可用：现在是与西方列强建立联系的时候了。与所有基督教列强获得 +10 关系 获得 Relations with the West Relations with the West 国家修正 +10% Influence +15% Trade route competitiveness，持续10年 |

## 技术

太平天国继承[中国](China.md)在叛乱时已解锁的所有技术。

## 政治

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助核实或更新此章节。其最后核实版本为1.10。 |
|---|---|

太平天国的初始法律通常与[中国](China.md)叛乱时相同，除了下述例外：

| 权力结构 | 经济 | 人权 |  |  |  |
|---|---|---|---|---|---|
| 治理原则 | 神权制（Theocracy） | 经济系统 | 与中国相同 | 言论自由 | 与中国相同 |
| 权力分配 | 与中国相同 | 贸易政策 | 与中国相同 | 劳工权利 | 无工人权利 |
| 公民权 | 民族至上 | 税收 | 与中国相同 | 儿童权利 | 与中国相同 |
| 国教与政权 | 国教 | 土地改革 | 农民土地制 | 女性权利 | 与中国相同 |
| 官僚体制 | 与中国相同 | 殖民 | 与中国相同 | 社会福利 | 与中国相同 |
| 陆军模式 | 农民征兵制 | 警务 | 与中国相同 | 迁移 | 无迁移管制 |
| 海军模式 | 与中国相同 | 教育系统 | 与中国相同 | 奴隶制 | 与中国相同 |
| 国内安全 | 与中国相同 | 医疗系统 | 与中国相同 | 劳工结社 | 与中国相同 |

太平天国虽然是一个神权制国家，但它使用特殊的[太平天国](Government type.md)神权制，且是世袭的。

### 利益集团

拜上帝会始终处于政府中，其他利益集团可以加入政府。

拜上帝会拥有独特的“拜上帝者”意识形态，取代了道德主义者。士人失去“反教权”意识形态。

### 历史人物

姓名按中文习惯给出：姓氏在前。
太平天国会根据叛乱发生的时间获得某些历史人物。

| 姓名[wp 1] | 类型 | 利益集团 | 意识形态 | 特质 | 军衔 | 条件 |
|---|---|---|---|---|---|---|
| [洪秀全](http://en.wikipedia.org/wiki/Hong_Xiuquan) | 统治者 | 拜上帝会 | 神权主义者 | 鼓舞人心的演说家、坚毅、精神疾患 | — | 日期在1880.1.1之前 没有其他国家拥有该人物 |
| [洪天贵福](http://en.wikipedia.org/wiki/Hong_Tianguifu) | 继承人 | 拜上帝会 | 温和派 | 内向 | — | 日期在1847.1.1至1880.1.1之间 没有其他国家拥有洪秀全 |
| [杨秀清](http://en.wikipedia.org/wiki/Yang_Xiuqing) | 政治家与将军 | 武装力量 | 神权主义者 | 骗子、老练的政治操盘手、野心勃勃、煽动家 | 中将 | 日期在1841.1.1至1880.1.1之间 |
| [萧朝贵](http://en.wikipedia.org/wiki/Xiao_Chaogui) | 政治家与将军 | 拜上帝会 | 神权主义者 | 鲁莽、魅力非凡、煽动家 | 准将 | 日期在1840.1.1至1880.1.1之间 |
| [洪仁玕](http://en.wikipedia.org/wiki/Hong_Rengan) | 政治家 | 士人 | 市场自由主义者 | 创新、坚毅、外交家 | — | 日期在1842.1.1至1880.1.1之间 |

洪秀全带有修正*Brother of Christ Brother of Christ Character modifier +50 Popularity*，持续10年。如果洪秀全没有生成，则会生成一个具有相同特质和修正的通用替代人物。

## 策略

以下内容是玩家为
太平天国
建议的众多策略
之一
。请注意，由于游戏的动态性质，其他玩家的体验可能有所不同。
| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助核实或更新此指南。其最后核实版本为1.10。 |
|---|---|

### 经济

作为动态生成的国家，经济情况变化很大；不过太平天国很可能仍拥有庞大的人口，毕竟它位于亚洲。不幸的是，它一开局就与一个对手陷入内战，而该对手很可能仍拥有（大约？需要出生地位置或各省触发事件概率的数据）中国北部和东部更有价值的资源与人口。

### 军事

作为中国分裂出来的国家，太平天国会征用世界最大的初始陆军（或至少是其兵营）中相当大的一部分。不幸的是，它很可能仍小于内战对手。玩家必须谨慎作战，否则会被压倒性的数量优势击垮。

你可能会继承一些舰船，但最值得注意的是，AI会立即用其手中的舰船袭扰护航船队或实施封锁。

### 扩张

唯一的目标可能就是吞并中国，聚焦于最有价值的省份，例如山西，强化自身的同时削弱竞争对手。

## 轶事

在《维多利亚2》中，中国从游戏开始时就被划分为多个子国，以便在当时引擎的限制下更好地模拟清王朝中央权威的瓦解以及各欧洲列强在中国不同地区施加的势力范围。中国的主体部分是这一子国集合中人口最多的部分，以东北部为核心，大致从浙江（靠近上海）到山西再到北方的北京。

只要出现动乱，太平天国就随时有机会生成。它被硬编码为只能在其历史地区生成，且不继承任何西方化进度。如果它赢得内战，将吞并整个中国；但战争开始时各子国会独立（包括脱离中国），玩家若想重新统一中国，就必须为战争寻找开战理由。

## 参考

---

维基百科链接参考：

1. ↑ 链接至英文维基百科条目

返回顶部
国家
按地区
Tabber需要JavaScript才能使用。
| 印度支那地区 | [缅甸](Burma.md) [柬埔寨](Cambodia.md) [占巴塞](https://vic3.paradoxwikis.com/Champasak) [清迈](Chiang Mai.md) [大南](Dai Nam.md) [柔佛](https://vic3.paradoxwikis.com/Johore) [琅勃拉邦](https://vic3.paradoxwikis.com/Luang_Prabang) [霹雳](https://vic3.paradoxwikis.com/Perak) [雪兰莪](https://vic3.paradoxwikis.com/Selangor) [暹罗](Siam.md) [掸邦](Shan.md) |
|---|---|

| 印度尼西亚地区 | [亚齐](https://vic3.paradoxwikis.com/Aceh) [巴厘](https://vic3.paradoxwikis.com/Bali) [班贾尔](https://vic3.paradoxwikis.com/Banjar) [文莱](https://vic3.paradoxwikis.com/Brunei) [布卢岸](https://vic3.paradoxwikis.com/Bulungan) [布顿](https://vic3.paradoxwikis.com/Buton) [东印度群岛](East Indies.md) [占碑](https://vic3.paradoxwikis.com/Jambi) [库泰](https://vic3.paradoxwikis.com/Kutai) [兰芳](Lanfang.md) [马京达瑙](Maguindanao.md) [菲律宾](Philippines.md) [坤甸](https://vic3.paradoxwikis.com/Pontianak) [三发](https://vic3.paradoxwikis.com/Sambas) [锡亚克](https://vic3.paradoxwikis.com/Siak) [新当](https://vic3.paradoxwikis.com/Sintang) [苏禄](Sulu.md) [梭罗](https://vic3.paradoxwikis.com/Surakarta) [蒂多雷](https://vic3.paradoxwikis.com/Tidore) [日惹](https://vic3.paradoxwikis.com/Yogyakarta) |
|---|---|

| 华北/华南/东北亚地区 | [中国](China.md) [虾夷地](Ezochi.md) [日本](Japan.md) [朝鲜](Korea.md) [琉球](Ryukyu.md) |
|---|---|

| 大洋洲地区 | [夏威夷](Hawaii.md) [考尔纳](Kaurna.md) [新南威尔士](New South Wales.md) [南澳大利亚](South Australia.md) [塔希提](Tahiti.md) [塔斯马尼亚](Tasmania.md) [联合部落](United Tribes.md) [西澳大利亚](Western Australia.md) |
|---|---|

| 可成立 | [奥塔罗阿](https://vic3.paradoxwikis.com/Aotearoa) [澳大利亚](Australia.md) [印度尼西亚](Indonesia.md) [老挝](Laos.md) [波利尼西亚](Polynesia.md) |
|---|---|

| 可释放 | [阿拉干](Arakan.md) [楚科奇](Chukotka.md) [勃固](Hathawaddy.md) [爪哇](https://vic3.paradoxwikis.com/Java) [克钦](Kachin.md) [加里曼丹](https://vic3.paradoxwikis.com/Kalimantan) [堪察加](Kamchatka.md) [克伦](Karen.md) [克木](Khmu.md) [满洲](Manchuria.md) [孟夸](https://vic3.paradoxwikis.com/Muang_Phuan) [新西兰](New Zealand.md) [多巴](https://vic3.paradoxwikis.com/Toba) [万象](https://vic3.paradoxwikis.com/Vientiane) |
|---|---|

| 中国可释放 | [安徽](https://vic3.paradoxwikis.com/Anhui) [大乘](https://vic3.paradoxwikis.com/Da_Cheng) [福尔摩沙](Formosa.md) [贵州](https://vic3.paradoxwikis.com/Guizhou) [湖南](https://vic3.paradoxwikis.com/Hunan) [蒙古](Mongolia.md) [黔](Qian.md) [山东](https://vic3.paradoxwikis.com/Shandong) [山西](https://vic3.paradoxwikis.com/Shanxi) [四川](https://vic3.paradoxwikis.com/Sichuan) [西北](https://vic3.paradoxwikis.com/Xibei) [原住民](https://vic3.paradoxwikis.com/Yuanzhumin) [粤](Yue.md) [云南](Yunnan.md) [直隶](https://vic3.paradoxwikis.com/Zhili) |
|---|---|

Template:Country navbox/Africa
Template:Country navbox/EuropeWest
Template:Country navbox/MiddleEast
Template:Country navbox/India
Template:Country navbox/AmericaNorth
Template:Country navbox/Other
**注释：**此表按超大区和地区列出可游玩国家。开局国家按其首都所在地区列出，开局不存在的可成立和可释放国家则按超大区单独列出。松散的（不可游玩）及特殊情况单独列出。