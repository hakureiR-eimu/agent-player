---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Formable countries
source: https://vic3.paradoxwikis.com/Formable_countries
pageid: 3521
categories: [1.13, Countries, Formable_countries, Lists]
fetched: 2026-10-27
---
本文已针对游戏当前 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

部分[国家](Countries.md)可以在游戏开始后创建，还有一些国家在开局时即存在，但在灭亡后可以重新成立。国家成立通常通过日志界面的“国家成立”标签页完成。国家成立也被称为*统一*（unification）。部分可成立国家还可以被直接[释放](Releasable countries.md)，而非通过成立获得。

## 次要统一

对于大多数国家成立，其要求为：

- 该国目前不存在
- 拥有至少一个所需的主流文化之一
- 国家等级**低于**可成立国家
- 控制目标州区域的一定百分比

部分国家有额外要求，例如已研究民族主义或泛民族主义。

一旦满足要求，即可在“文化”标签页中按下成立国家的按钮。该国随之发生改变，更新主流文化和旗帜，并提升国家等级。

就控制州区域而言，自治领、君合国、傀儡国和附庸国可计入成立条件（朝贡国和保护国则不行）。如果附属国拥有可成立国家的某一主流文化，则在成立时会被整体吞并——无论其是否拥有任何所需州。拥有其他主流文化的附属国不会被吞并，但会在成立时将所有目标州区域割让给其宗主国。这些类型的间接附属国同样计入成立条件，但将成为统一者的附属国而非被吞并。

## 主要统一

主要统一与次要统一的基本要求相同，只是同等级国家也可以成立。此外，与次要统一不同，一个国家无需直接控制所需的州，而是可以作为*统一候选人*（unification candidate）获得拥有相同文化国家的支持。

大多数主要统一同时最多可有三名候选人，从拥有合格主流文化且威望最高的三个列强中选出。如果没有合格的列强，则主要政权有资格成为统一候选人。部分统一对成为统一候选人的最低等级可能有不同设定：就[斯堪的纳维亚](Scandinavia.md)和[意大利](Italy.md)而言，如果没有合格的主要政权或更高等级政权，则次要政权也将获得资格。统一候选人的资格不会因其等级跌至合格线以下而丧失。每个拥有合格主流文化的非候选国家可选择支持任一候选人或不支持任何候选人；AI 国家会根据由关系和态度得出的评分来选择支持哪个国家或不支持。附属国只能支持其直接宗主国。

当存在多名候选人时，任何人都无法成立该国。相反，每名统一候选人都可以发起一场*领导权博弈*（leadership play）迫使其他候选人放弃候选资格，各候选人的支持者会自动在博弈中支持己方。在领导权博弈中退让或失败的候选人将失去再次成为候选人的资格，且潜在候选人数目也相应减一。不过，被取消资格的候选人仍可通过直接控制所需州的常规成立流程来成立该国。

当仅剩一名候选人，且任何所需州不被支持者或盟友——或候选人、支持者或盟友的附属国——持有时，该国可以对持有所需州的其他所有国家（被取消资格的候选人和目标除外）发起*统一博弈*（unification play）。在为德国、意大利或斯堪的纳维亚发起统一博弈时，候选人会立即吞并所有支持者。支持者的任何附属国将成为候选人的附属国。统一博弈会将目标国家持有的每个所需州添加为主要诉求，而对方则使用“削减规模”，因此如果候选人退让或投降，被吞并的支持者将会恢复。统一博弈并非必需；只要足够的州由唯一候选人及其支持者控制，即可成立统一国家。统一博弈的吸引力在于它不会为统一候选人产生恶名，属于高风险、高回报。

除了其特殊机制外，领导权博弈和统一博弈在其他方面都是常规的[外交博弈](Diplomatic play.md)，其他国家可以加入或被拉拢，其他战争目标也可以照常添加。

目前，只有[安第斯联邦](Federation of the Andes.md)、[德国](Germany.md)、[意大利](Italy.md)、[斯堪的纳维亚](Scandinavia.md)和[南斯拉夫](Yugoslavia.md)属于主要统一。

## 特殊统一

某些统一拥有额外机制，例如特殊日志条目、决议或统一战争目标。

[加拿大](Canada.md)和[澳大利亚](Australia.md)殖民地可以通过共同的宗主国或殖民地自身通过一项特殊决议合并，但最终成立仍遵循常规规则。

[北德意志联邦](North German Federation.md)（NGF）和[南德意志联邦](South German Federation.md)（SGF）可通过对应文化国家的日志条目成立。当日志条目完成时，它们会自动转变为联邦国家[1]并收到一个给予影响力和威望的事件。与该国处于关税同盟中、或作为德国统一候选人支持它的同主流文化 AI 国家会被吞并；其他同主流文化国家则会收到一个事件，将其吞并或添加对其所有拥有州的宣称。列强不受这些事件影响。

[伊比利亚](Iberia.md)在“伊比利亚暮光”中有一个日志条目*伊比利亚联盟*，用以协助统一。

意大利统一也有一个日志条目，在其活跃期间，该国可能收到一个事件，用以吞并处于其关税同盟中、是其附属国或与其相邻的次要政权或无足轻重的政权，从而使统一更加轻松简单。

[秘鲁-玻利维亚](Peru-Bolivia.md)可由[玻利维亚](Bolivia.md)通过日志条目*秘鲁-玻利维亚邦联*成立。

除主要统一的特殊统一博弈外，以下国家拥有特殊的吞并博弈以支持其成立：[阿拉伯](Arabia.md)、[中国](China.md)、[埃塞俄比亚](Ethiopia.md)、[印度](India.md)（BHT）和[印度尼西亚](Indonesia.md)。除中国和埃塞俄比亚外，这些特殊博弈需要研究泛民族主义后才能使用。

[罗马尼亚](Romania.md)可由[摩尔达维亚](Moldavia.md)或[瓦拉几亚](Wallachia.md)通过日志条目成立，先将两国结为君合国，随后再成立罗马尼亚。

## 可成立国家列表

### 主要可成立国家

所有主要可成立国家都需要相关[地理区域](Geographic region.md)中一定百分比的州。注意，成立要求可能与候选人资格要求不同，此时可能无需成为候选人即可成立该国。但候选人资格要求也包含成立要求，因此无法在不满足成立条件的情况下成为候选人。

| 国家 | [主流文化](Culture.md) | 国家等级 | 要求 | 无效目标 | 地理区域 | 州百分比 |  |
|---|---|---|---|---|---|---|---|
| 常规 | 仅限候选人资格 |  |  |  |  |  |  |
| [安第斯联邦](Federation of the Andes.md) | 北安第斯 南安第斯 | 霸权 | 拥有日志条目“玻利瓦尔的野心” | 至少为主要政权 |  | 安第斯 | 80%（28/35） |
| [德国](Germany.md) | 北德意志 南德意志 | 帝国 | 满足其一：已研究泛民族主义 已完成“德意志民族认同”日志条目 莱茵邦联不存在 不具有二元君主制或三元君主制政体类型 非多瑙国家 | 至少为主要政权 | 具有二元君主制或三元君主制政体类型 | 大德意志 | 73%（23/31） |
| [意大利](Italy.md) | 北意大利 南意大利 | 帝国 | 非奥地利、中欧或多瑙国家 | 至少为次要政权 已获承认 所有意大利国家已研究民族主义 | 若拥有北意大利主流文化，不具有“联邦方案”日志条目 非中欧或多瑙国家 | 意大利 | 70%（12/17） |
| [斯堪的纳维亚](Scandinavia.md) | 瑞典 丹麦 挪威 冰岛 | 帝国 |  | 至少为次要政权 所有斯堪的纳维亚国家（不含芬兰主流文化者）已研究泛民族主义 |  | 斯堪的纳维亚 | 70%（11/15） |
| [南斯拉夫](Yugoslavia.md) | 塞尔维亚 克罗地亚 斯洛文尼亚 波斯尼亚 保加利亚 | 帝国 | 已研究泛民族主义 非奥地利、中欧或多瑙国家 非保加利亚，除非其推行大南斯拉夫主义 | 至少为主要政权 非中欧 非保加利亚，除非其推行大南斯拉夫主义 | 保加利亚（若其未推行大南斯拉夫主义） 若拥有克罗地亚、塞尔维亚或斯洛文尼亚主流文化，不具有“联邦方案”日志条目 非中欧或多瑙国家 | 南斯拉夫 | 75%（8/12） |

### 其他可成立国家

其他可成立国家有两种类型：

1. 需要一定百分比的文化本土与某一主流文化相符的州。这与主要可成立国家相同。
2. 需要一定百分比的来自指定列表的州。

| 国家 | [主流文化](Culture.md) | 国家等级 | 其他要求 | 所需州 | 州百分比 | 开局即存在 |
|---|---|---|---|---|---|---|
| [阿富汗](Afghanistan.md) | 普什图 塔吉克 | 王国 |  | 赫拉特 坎大哈 喀布尔斯坦 哈扎里斯坦 南突厥斯坦 普什图斯坦 圭塔 北俾路支 | 50% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [阿尔及利亚](Algeria.md) | 马格里布 阿马齐格 | 王国 |  | 阿尔及尔 君士坦丁 奥兰 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [美国](America.md) | 扬基 迪克西 | 帝国 |  | 文化本土 | 75% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| [安的列斯邦联](Antillean Confederation.md) | 加勒比 非洲加勒比 | 王国 | 泛民族主义 | 西古巴 中古巴 东古巴 圣多明各 波多黎各 | 80% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [奥特亚罗瓦](https://vic3.paradoxwikis.com/Aotearoa) | 毛利 | 王国 |  | 文化本土 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [阿拉伯](Arabia.md) | 马什里基 贝都因 米斯里 也门 | 帝国 | 泛民族主义 | 也门 阿曼 特鲁西尔海岸 内志 汉志 哈伊勒 巴格达 外约旦 巴勒斯坦 黎巴嫩 叙利亚 阿勒颇 摩苏尔 代尔祖尔 巴士拿 西奈 下埃及 中埃及 马特鲁 埃及沙漠 上埃及 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [澳大利亚](Australia.md) | 澳大利亚 | 王国 | 民族主义 | 文化本土 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [俾路支斯坦](Baluchistan.md) | 俾路支 | 王国 | 已研究民族主义 非印度或东印度 | 俾路支斯坦 北俾路支 班布尔 | 33% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [孟加拉](Bengal.md) | 孟加拉 | 王国 | 非印度或东印度 | 文化本土 | 50% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [巴西](Brazil.md) | 巴西 | 帝国 |  | 文化本土 | 80% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| [拜占庭](Byzantium.md) | 希腊 | 帝国 | 君主制 正在追求拜占庭的成立 可成立国家游戏规则：全部 | 东色雷斯 阿提卡 色萨利 马其顿 斯科普里 西色雷斯 北色雷斯 胡达文迪加 艾登 西爱琴群岛 东爱琴群岛 阿尔巴尼亚 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [加拿大](Canada.md) | 英裔加拿大 法裔加拿大 | 王国 | 民族主义 | 文化本土 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [卡纳蒂克](Carnatic.md) | 泰米尔 | 王国 | 非印度或东印度 | 文化本土 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [卡罗来纳](Carolina.md) | 迪克西 | 公国 | 可成立国家游戏规则：全部 满足其一： 北卡罗来纳 南卡罗来纳 | 北卡罗来纳 南卡罗来纳 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [中美洲](Central America.md) | 中美洲 | 王国 |  | 文化本土 | 50% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| [中欧](Central Europe.md) ![Information](/images/thumb/5/54/Information.png/24px-Information.png)AI 国家不会成立该国 | 北德意志 南德意志 捷克 荷兰 弗拉芒 瓦隆 阿勒曼尼 北意大利 斯洛文尼亚 | 霸权 | 可成立国家游戏规则：全部 首都位于欧洲 | 文化本土 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [中国](China.md) | 满洲 汉 | 帝国 |  | 文化本土 | 60% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| [哥伦比亚](Colombia.md) | 北安第斯 | 王国 |  | 文化本土 | 80% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| [莱茵邦联](Confederation of the Rhine.md) | 北德意志 南德意志 | 帝国 | 民族主义 不属于以下任一： 普鲁士 奥地利 北德意志联邦 南德意志联邦 | 黑森 萨克森 石勒苏益格-荷尔斯泰因 安哈尔特 法兰克尼亚 巴伐利亚 不伦瑞克 汉诺威 巴登 符腾堡 鲁尔 威斯特法伦 易北河 梅克伦堡 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [捷克斯洛伐克](Czechoslovakia.md) | 捷克 斯洛伐克 | 王国 | 非奥地利或多瑙国家 | 波希米亚 摩拉维亚 斯洛伐克 喀尔巴阡鲁塞尼亚 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [多瑙国家](Danubian State.md) | 南德意志 匈牙利 罗马尼亚 克罗地亚 捷克 斯洛伐克 斯洛文尼亚 | 帝国 | 泛民族主义 满足其一： 多元文化主义 属国地位 | 文化本土 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [达罗毗荼](Dravida Nadu.md) | 泰米尔 泰卢固 马拉雅拉姆 卡纳达 | 帝国 | 泛民族主义 非印度或东印度 | 文化本土 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [英格兰](England.md) | 英格兰 | 王国 |  | 内伦敦 中部 东盎格利亚 西部乡约克郡 兰开夏 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [埃塞俄比亚](Ethiopia.md) | 阿姆哈拉 奥罗莫 提格雷 | 帝国 |  | 贡德尔 阿姆哈拉 奥罗米亚 | 33% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [法国](France.md) | 法兰西 | 帝国 |  | 法兰西岛 普罗旺斯 诺曼底 朗格多克 罗讷 法属低地国家 皮卡第 阿尔萨斯-洛林 普瓦图-圣通日 圭耶纳 奥弗涅-利穆赞 布列塔尼 勃艮第 香槟 弗朗什-孔泰 洛林 阿基坦 奥尔良-贝里 | 75% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| [美利坚自由州](Free States of America.md) | 扬基 | 王国 | 奴隶制被禁止 | 文化本土 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [加利西亚-洛多梅里亚](Galicia-Lodomeria.md) | 波兰 乌克兰 | 公国 |  | 东加利西亚 西加利西亚 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [大哥伦比亚](Gran Colombia.md) | 北安第斯 | 帝国 |  | 昆迪纳马卡 厄瓜多尔 米兰达 安蒂奥基亚 瓜维亚雷 玻利瓦尔 苏利亚 考卡 | 85% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [大不列颠](Great Britain.md) | 英格兰 苏格兰 | 帝国 |  | 文化本土 | 75% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| [古吉拉特](Gujarat.md) | 古吉拉特 | 王国 | 已研究民族主义 非印度或东印度 | 文化本土 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [印度斯坦](Hindustan.md) | 印度斯坦 | 帝国 |  | 文化本土 | 100% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| [伊比利亚](Iberia.md) | 西班牙 加泰罗尼亚 葡萄牙 巴斯克 加利西亚 | 帝国 | 泛民族主义 若首都位于伊比利亚，伊比利亚的所有附属国独立倾向低于75% | 文化本土 | 90% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [印度](India.md) | 阿萨姆 奥德 俾路支 孟加拉 比哈尔 古吉拉特 卡纳达 马拉雅拉姆 马拉地 奥里亚 旁遮普 普什图 拉杰普特 信德 泰米尔 泰卢固 印度斯坦 本德里 帕哈里 贡德 巴盖利 恰蒂斯加尔 德干 | 霸权 | 泛民族主义 | 阿萨姆 奥德 俾路支斯坦 比哈尔 孟买 马尔瓦 锡兰 塞卡尔 斯 德里 东孟加拉 古吉拉特 海得拉巴 克什米尔 马德拉斯 迈索尔 中部省份 西孟加拉 奥里萨 普什图斯坦 旁遮普 拉杰普塔纳 信德 特拉凡哥尔 割让区 本德尔坎德 阿格拉 旁遮普山区 圭塔 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [印度尼西亚](Indonesia.md) | 巴厘 巴塔克 婆罗洲 达雅克 爪哇 马来 摩鹿加 苏门答腊 | 帝国 | 泛民族主义 | 亚齐 中爪哇 东婆罗洲 东爪哇 马来亚 摩鹿加 西里伯斯 北婆罗洲 北苏门答腊 南苏门答腊 巽他群岛 西婆罗洲 西新几内亚 西爪哇 | 65% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [爱尔兰](Ireland.md) | 爱尔兰 | 王国 |  | 文化本土 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [哈萨克斯坦](Kazakhstan.md) | 哈萨克 | 王国 | 民族主义 | 塞米巴拉金斯克 阿克莫林斯克 伊犁 乌拉尔斯克 阿克托别 锡尔河 | 50% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [吉尔吉斯斯坦](https://vic3.paradoxwikis.com/Kirgizia) | 吉尔吉斯 | 大公国 | 民族主义 | 吉尔吉斯 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [老挝](Laos.md) | 老挝 | 王国 |  | 老挝 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [利比亚](Libya.md) | 马格里布 | 王国 | 民族主义 首都位于某个所需州 | 昔兰尼加 费赞 的黎波里 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [马格里布](Maghreb.md) ![Information](/images/thumb/5/54/Information.png/24px-Information.png)AI 国家不会成立该国 | 马格里布 阿马齐格 比丹 | 帝国 | 泛民族主义 | 阿尔及尔 里夫 君士坦丁 昔兰尼加 东撒哈拉 非斯 费赞 内毛里塔尼亚 内摩洛哥 马拉喀什 马特鲁 毛里塔尼亚 奥兰 撒哈拉 的黎波里 突尼斯 西撒哈拉 | 50% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [马哈拉施特拉](Maharashtra.md) | 马拉地 | 王国 | 非印度或东印度 | 文化本土 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [马里](Mali.md) | 班巴拉 富尔贝 沃洛夫 曼德 | 王国 |  | 廷巴克图 西马里 东马里 塞内加尔 几内亚 沃尔特 | 50% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [墨西哥](Mexico.md) | 墨西哥 | 王国 |  | 文化本土 | 75% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| [北德意志联邦](North German Federation.md) | 北德意志 | 王国 | 民族主义 | 文化本土 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [奥里萨](Orissa.md) | 奥里亚 | 王国 | 已研究民族主义 非印度或东印度 | 文化本土 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [巴基斯坦](Pakistan.md) | 克什米尔 旁遮普 信德 俾路支 普什图 | 帝国 | 泛民族主义 逊尼派 | 俾路支斯坦 普什图斯坦 克什米尔 旁遮普 信德 圭塔 | 80% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [秘鲁](Peru.md) | 南安第斯 | 王国 |  | 利马 卡哈马卡 伊卡 阿雷基帕 塔拉帕卡 | 80% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [波兰](Poland.md) | 波兰 | 王国 | 非奥地利或多瑙国家 | 华沙 普沃茨克 卢布林 西加利西亚 东加利西亚 上西里西亚 波森 西普鲁士 | 55% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [波兰-立陶宛](Poland-Lithuania.md) | 波兰 立陶宛 | 帝国 |  | 格罗德诺 东加利西亚 华沙 卢布林 立陶宛 维尔纽斯 普沃茨克 波森 沃里尼亚 西加利西亚 西普鲁士 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [波利尼西亚](Polynesia.md) | 夏威夷 毛利 美拉尼西亚 波利尼西亚 密克罗尼西亚 原住民 | 帝国 | 泛民族主义 | 文化本土 | 70% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [普鲁士](Prussia.md) | 北德意志 | 王国 |  | 勃兰登堡 波美拉尼亚 西普鲁士 东普鲁士 下西里西亚 上西里西亚 波森 | 80% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| [旁遮普](Punjab.md) | 旁遮普 | 王国 | 非印度或东印度 | 文化本土 | 100% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| [拉杰普塔纳](Rajputana.md) | 拉杰普特 | 王国 | 已研究民族主义 非印度或东印度 | 文化本土 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [拉普拉塔河](Rio de la Plata.md) | 拉普拉塔 | 帝国 | 陆军力量投射至少500 | 文化本土 | 81% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [罗马尼亚](Romania.md) | 罗马尼亚 | 王国 | 非奥地利或多瑙国家 | 文化本土 | 37.5% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [俄罗斯](Russia.md) | 俄罗斯 | 帝国 |  | 文化本土 | 75% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| [南德意志联邦](South German Federation.md) | 南德意志 | 王国 |  | 文化本土 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [西班牙](Spain.md) | 西班牙 | 王国 |  | 文化本土 | 75% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| [瑞典](Sweden.md) ![Information](/images/thumb/5/54/Information.png/24px-Information.png)AI 国家不会成立该国 | 瑞典 | 王国 |  | 斯韦阿兰 约塔兰 斯科讷 诺尔兰 | 75% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| [塔吉克斯坦](https://vic3.paradoxwikis.com/Tajikistan) | 塔吉克 | 大公国 | 民族主义 | 塔吉克斯坦 南突厥斯坦 | 50% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [塔万廷苏尤](Tawantinsuyu.md) ![Information](/images/thumb/5/54/Information.png/24px-Information.png)AI 国家不会成立该国 | 克丘亚 | 王国 | 民族主义 | 文化本土 | 50% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [外高加索](Transcaucasia.md) | 阿塞拜疆 亚美尼亚 格鲁吉亚 | 帝国 | 泛民族主义 | 第比利斯 亚美尼亚 巴库 卡尔斯 埃利萨维特波尔 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [突厥斯坦](Turkestan.md) | 乌兹别克 吉尔吉斯 哈萨克 土库曼 塔吉克 维吾尔 | 帝国 | 泛民族主义 | 费尔干纳 乌兹别克 吉尔吉斯 花剌子模 梅尔夫 南突厥斯坦 塔吉克斯坦 土库曼尼亚 锡尔河 伊犁 塔里木盆地 准噶尔 塞米巴拉金斯克 阿克莫林斯克 阿克托别 乌拉尔斯克 | 40% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [波罗的联合省](United Baltic Provinces.md) | 拉脱维亚 爱沙尼亚 立陶宛 | 大公国 | 泛民族主义 | 文化本土 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [尼德兰联合](United Netherlands.md) | 荷兰 弗拉芒 瓦隆 | 帝国 |  | 荷兰 法兰德斯 瓦隆尼亚 弗里斯兰 海尔德兰 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [乌兹别克斯坦](https://vic3.paradoxwikis.com/Uzbekistan) | 乌兹别克 | 大公国 | 民族主义 | 费尔干纳 乌兹别克 花剌子模 | 66% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [西印度群岛](West Indies.md) | 非洲加勒比 | 王国 |  | 西印度群岛 牙买加 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [也门](Yemen.md) | 也门 贝都因 | 王国 |  | 也门 | 100% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| [津巴布韦](Zimbabwe.md) | 绍纳 恩古尼 | 王国 |  | 赞比西 | 75% | ![No](/images/thumb/0/04/No.png/24px-No.png) |
## 成立事件

大多数国家在首次成立时会收到一个事件，对于开局即存在的国家，则是重建时收到。某些国家拥有专属事件，其余国家则收到通用事件。

id

### [Country Adjective] 统一

[Country] 已在 [Capital Strategic Region] 崛起为一股新兴力量。
---

风味文本：
新的一天破晓，一个新国家登上世界舞台。[Country Adjective] 的荣光是不可回避的未来。
---

| 触发者：成立一个国家 |
|---|
| 触发条件：不属于以下任一国家：Arabia、Brazil、Byzantium、Central America、Central Europe、Confederation of the Rhine、Danubian State、Ethiopia、Federation of the Andes、Iberia、India、Indonesia、Italy、Germany、Gran Colombia、Kazakhstan、Laos、Mali、Peru-Bolivia、Rio de la Plata、Scandinavia、Turkestan、United Baltic Provinces、United Netherlands、Yemen、Yugoslavia |
| 光荣的联合。添加修正 National Unifier National Unifier 国家修正 +25 威望，持续 20 年 获得主要文化所有无主故乡的宣称 若所有故乡均已被拥有或已获得宣称，则改为 5% 的人口变得更加忠诚 |

## 参考

1. ↑ 仅适用于公国或王国等级的国家。

1. 可成立国家定义于 /Victoria 3/game/common/country_formation/00_formable_countries.txt
2. 重大统一国家定义于 /Victoria 3/game/common/country_formation/00_major_formables.txt 并带有 `is_major_formation = yes`
3. 与统一相关的外交博弈定义于 /Victoria 3/game/common/diplomatic_plays/00_diplomatic_plays.txt，以其前缀 `dp_unify` 或 `dp_leadership` 标识