---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Political movement
source: https://vic3.paradoxwikis.com/Political_movement
pageid: 1621
categories: [1.13, Articles_with_potentially_outdated_images, Politics]
fetched: 2026-10-27
---
本文已针对游戏当前[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行验证。

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此图片。它上次验证的版本未知。 |
|---|---|

一场正在进行的法律改革以及一场维护现行法律的运动。

**政治运动（Political movement）**代表民众对特定意识形态或文化、宗教身份的支持。政治运动的力量来源于[人口](Pops.md)，并可能影响[利益集团](Interest group.md)。这让人口即便被*剥夺了选举权*，也能够推动改革。

激进的政治运动可能演变为*革命*，并试图以武力改变政治体制。

## 形成与解散

政治运动在每次检测时有一个基础的 X% 概率在每段周期（PERIOD）内发起。如果该运动发起时的支持度每有一点，这个概率会增加 X%？。如果已存在任何运动，该概率会除以 1 + ( 2 ⋅ ⋅ # # of active movements ) {\displaystyle 1+(2\cdot \#{\text{ of active movements}})} ![{\displaystyle 1+(2\cdot \#{\text{ of active movements}})}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/ece2a2c4dc6c3eb3940e95a72bca4327edd1050b)。

一个运动至少需要 2.5 的支持度才能发起，若支持度低于 1 则会解散；但在成立满 12 个月之前，运动不会因支持度过低而解散。在此之后，从最初的 12 个月起，每个月累计增加 0.04% 的解散概率。解散概率会除以 1 + ( 0.01 ⋅ ⋅ movement support ) {\displaystyle 1+(0.01\cdot {\text{movement support}})} ![{\displaystyle 1+(0.01\cdot {\text{movement support}})}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/b0aa9e79c30ea8fb3c4c6caca37a953c696dc6ae)。不过，这一规则不适用于已变成*革命性*的运动。

## 政治运动类别

运动共有五种大类：

| 类别 | 支持对象 | 基于身份认同 |  |
|---|---|---|---|
| 建立 | 维持 |  |  |
| 意识形态型 | 5 | 2.5 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 泛民族型 | 5 | 2.5 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 文化型 | 20 | 10 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| 文化多数型 | 5 | 2.5 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| 宗教型 | 10 | 5 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |

文化型、宗教型和泛民族型运动可能会累积[顽固性（Obstinance）](https://vic3.paradoxwikis.com/Obstinance)。

### 政治运动类型

在每个类别之下都有一种或多种具体的运动类型。每种运动都有一个核心意识形态，并可能有若干人物意识形态，可分配给受该运动施压的[利益集团](https://vic3.paradoxwikis.com/Interest_groups)的领袖。每种运动类型都有特定的成立条件，并可能有其解散条件。此外还有额外的 trigger（触发条件）和权重，用于决定鼓动家和人口对某个运动的支持。

| 类别 | 类型 | 核心意识形态 | 人物意识形态 | 成立条件 | 解散条件 | 所属集团 |
|---|---|---|---|---|---|---|
|  | Abolitionist | Anti-Slavery | Abolitionist Humanitarian | 未实行 Slavery Banned 已研究 Empiricism | 已实行 Slavery Banned | 自由派 |
|  | Pro-Slavery | Pro-Slavery | Slaver Jacksonian Democrat | 未实行 Slavery Banned |  | 保守派 |
|  | Absolutist | Absolutist | Royalist Authoritarian | 实行君主制 没有投票权 不是法国 没有 Bakufu | 满足其一：拥有投票权，除非该国仍可能完成 The King-in-Parliament 日志条目 已完成 Stamp Out Monarchism 日志条目 | 保守派 |
|  | Royalist | Royalist | Royalist Enlightened Royalist | 实行君主制 拥有投票权 不是法国 | 已完成 Stamp Out Monarchism 日志条目 | 保守派 |
|  | Labor | Proletarian | Radical Reformer Social Democrat Utopian | 已研究 Labor Movement |  | 自由派 |
|  | Socialist | Socialist | Anarchist Communist Social Democrat Vanguardist | 已研究 Socialism 未实行以下任一项：孤立主义、传统主义、Peasant Levies、农奴制（除非同时实行 Manorialism） | 选定了一种意识形态 Anarchist Character ideology Anarchist This leader seeks the abolishment of hierarchy, authority and the state, leaving people to govern themselves. Stance on Citizenship Strongly Oppose Ethnostate, National Supremacy and Subjecthood Oppose Racial Segregation Endorse Cultural Exclusion Strongly Endorse Multiculturalism Stance on Distribution of Power Strongly Oppose Technocracy, Oligarchy and Autocracy Oppose Census Suffrage, Wealth Voting, - Landed Voting and Single-Party State Neutral towards Universal Suffrage Strongly Endorse Anarchy Stance on Economic System Strongly Oppose Interventionism, Traditionalism, - Laissez-Faire and Extraction Economy Oppose Command Economy and Industry Banned Neutral towards Agrarianism Strongly Endorse Cooperative Ownership Stance on Free Speech Strongly Oppose Outlawed Dissent Oppose Censorship Endorse Right of Assembly Strongly Endorse Protected Speech Stance on Governance Principles Strongly Oppose Corporate State, Theocracy, - Monarchy and Social Monarchy Oppose Presidential Republic and Parliamentary Republic Strongly Endorse Council Republic Stance on Labor Associations Strongly Oppose Guild System and Corporatized Unions Oppose Combination Acts Neutral towards Anti-Strike Laws and Right to Associate Endorse Factory Councils Stance on Policing Strongly Oppose Militarized Police Force Oppose Local Police Force and Dedicated Police Force Endorse No Police , Communist Character ideology Communist This leader believes in the working class seizing political power through whatever means necessary. Stance on Church and State Strongly Oppose State Religion Oppose Freedom of Conscience Neutral towards Total Separation Endorse State Atheism Stance on Economic System Strongly Oppose Laissez-Faire, Industry Banned and Extraction Economy Oppose Agrarianism and Traditionalism Neutral towards Interventionism Strongly Endorse Command Economy and Cooperative Ownership Stance on Governance Principles Strongly Oppose Corporate State, Theocracy, - Monarchy and Social Monarchy Oppose Presidential Republic and Parliamentary Republic Strongly Endorse Council Republic Stance on Labor Associations Strongly Oppose Guild System and Corporatized Unions Oppose Combination Acts Neutral towards Anti-Strike Laws and Right to Associate Endorse Factory Councils Stance on Labor Rights Neutral towards No Workers' Rights Endorse Regulatory Bodies Strongly Endorse Workers' Protections Stance on Land Reform Strongly Oppose Serfdom Oppose Commercialized Agriculture and Tenant Farmers Neutral towards Peasant Proprietorship Endorse Collectivized Agriculture , or Vanguardist Character ideology Vanguardist This leader believes in achieving a socialist society through a vanguard party of dedicated radicals. Stance on Distribution of Power Strongly Oppose Oligarchy, Autocracy, - Census Suffrage, Wealth Voting and Landed Voting Oppose Anarchy and Universal Suffrage Endorse Technocracy Strongly Endorse Single-Party State Stance on Economic System Strongly Oppose Laissez-Faire, Industry Banned and Extraction Economy Oppose Agrarianism and Traditionalism Neutral towards Interventionism Endorse Cooperative Ownership Strongly Endorse Command Economy Stance on Governance Principles Strongly Oppose Corporate State, Theocracy, - Monarchy and Social Monarchy Oppose Presidential Republic and Parliamentary Republic Strongly Endorse Council Republic Stance on Labor Associations Strongly Oppose Guild System and Corporatized Unions Oppose Combination Acts Neutral towards Anti-Strike Laws and Right to Associate Endorse Factory Councils Stance on Land Reform Strongly Oppose Commercialized Agriculture and Serfdom Oppose Tenant Farmers Neutral towards Peasant Proprietorship Endorse Collectivized Agriculture Stance on Trade Policy Strongly Oppose Free Trade Oppose Mercantilism Endorse Protectionism and Isolationism in The Spectre Haunting the World | 社会主义者 |
|  | Anarchist | Anarchist | Anarchist | 已研究 Anarchism 未实行以下任一项：孤立主义、传统主义、Peasant Levies、农奴制（除非同时实行 Manorialism） |  | 社会主义者 |
|  | Communist | Communist | Communist Vanguardist | 已研究 Socialism 未实行以下任一项：孤立主义、传统主义、Peasant Levies、农奴制（除非同时实行 Manorialism） |  | 社会主义者 |
|  | Fascist | Fascist | Corporatist Fascist Integralist | 已研究 Political Agitation 未实行以下任一项：孤立主义、传统主义、Peasant Levies、农奴制（除非同时实行 Manorialism） |  | 民族主义者 保守派 |
|  | Corporatist | Corporatist | Corporatist | 已研究 Corporatism 未实行以下任一项：孤立主义、传统主义、Peasant Levies、农奴制（除非同时实行 Manorialism） |  | 保守派 |
|  | Liberal | Liberal | Liberal Humanitarian Market Liberal Radical Republican | 已研究 Democracy 未实行以下任一项：孤立主义、传统主义、Peasant Levies、农奴制（除非同时实行 Manorialism） |  | 自由派 |
|  | Radical | Radical | Nihilist Radical | 已研究 Egalitarianism 不是共和制 共和制要求：● Corporate State、Presidential Republic、Parliamentary Republic 或 Council Republic |  | 自由派 |
|  | Nihilist | Nihilist | Nihilist | 已研究 Realism 尚未同时研究 Anarchism 和 Socialism | 已同时研究 Anarchism 和 Socialism | 社会主义者 |
|  | Positivist | Positivist | Positivist | 已研究 Psychiatry 实证主义已出现在世界中 |  | 自由派 |
|  | Peasant | Land Reformer | Land Reformer Luddite | 已研究 Enclosure 未实行任何变体的 Peasant Proprietorship 或 Collectivized Agriculture 超过 25% 的人口是农民 |  |  |
|  | Feminist | Feminist | Feminist Humanitarian | 已研究 Feminism |  | 自由派 |
|  | Reactionary | Reactionary | Authoritarian Luddite Protectionist Traditionalist | 未实行以下任一项：孤立主义、传统主义、Peasant Levies、农奴制（除非同时实行 Manorialism） 已实行 Slavery Banned 拥有投票权 没有 Legitimist、Carlist 或 Miguelist 运动 | 存在 Legitimist、Carlist 或 Miguelist 运动 | 保守派 |
|  | Modernization | Modernizer | Modernizer Abolitionist Market Liberal Protectionist Reformer | 已研究 Academia 知识分子阶层未被边缘化 实行以下任一项：孤立主义、农奴制、Peasant Levies、Guild System 实行以下任一项：Extraction Economy、传统主义、禁工业主义 实行以下任一项：Consumption-Based Taxation、Land-Based Taxation | 均不实行：孤立主义、农奴制、Peasant Levies、Guild System、No Schools 实行以下任一项：Extraction Economy、传统主义、禁工业主义 实行以下任一项：Consumption-Based Taxation、Land-Based Taxation | 自由派 民族主义者 |
|  | Minority Rights | Pluralist（Cultural Exclusion 版本） | Reformer |  |  |  |
|  | Religious Majority | Traditionalist | Theocrat Traditionalist | 未实行国家无神论 | 运动的宗教不再是国教 | 保守派 |
|  | Religious Minority | Minoritarian Traditionalist | Minoritarian Traditionalist | 满足其一：不是东印度公司 未研究 Pan-nationalism | 满足其一：运动的宗教是国教，且信奉者不足该国人口的 8% 是东印度公司且已研究 Pan-nationalism |  |
|  | Cultural Majority | Ethno-Nationalist | Ethno-Nationalist |  |  | 民族主义者 保守派 |
|  | Cultural Minority | Pluralist | Reformer |  | 满足其一：运动的文化是主流文化 该文化没有任何一个国家使其占某本土人口至少 18%，且要么占该国总人口不超过 8%，要么拥有至少 20 的文化接受度 |  |
|  | Indian National | Sovereignist | Humanitarian Social Democrat Sovereignist | 是东印度公司 是附属国 某个南亚传承的文化拥有超过 10 热忱 没有任何主流文化属于南亚传承 已研究 Pan-nationalism |  | 自由派 |
|  | German National | National Liberal | Ethno-Nationalist Market Liberal Liberal Republican Radical | 首都位于德意志邦联 是除德国以外的北德意志或南德意志国家 北德意志或南德意志文化至少拥有 10 热忱 | 是[德国](Germany.md) | 自由派 民族主义者 |
|  | Italian National | National Liberal | Ethno-Nationalist Market Liberal Liberal Republican Radical | 首都位于意大利 是除奥地利、多瑙联邦、中央欧洲和意大利以外的北意大利或南意大利国家 北意大利或南意大利文化至少拥有 10 热忱 | 是[意大利](Italy.md) | 自由派 民族主义者 |
|  | Yugoslav (Illyrian) National | National Liberal | Ethno-Nationalist Market Liberal Liberal Republican Radical | 首都位于巴尔干 满足其一：是克罗地亚、塞尔维亚、波斯尼亚或斯洛文尼亚国家 是保加利亚国家且已推行大南斯拉夫 不是南斯拉夫 克罗地亚、塞尔维亚、波斯尼亚或斯洛文尼亚文化至少拥有 10 热忱 | 是[南斯拉夫](Yugoslavia.md) | 自由派 民族主义者 |
|  | Dominican National | National Liberal | Ethno-Nationalist Market Liberal Liberal Republican Radical Reformer | 拥有圣多明各 主流文化不是 Caribeño | 不再拥有圣多明各 |  |
|  | Utilitarian | Utilitarian | Utilitarian | 主流文化为英格兰、英裔加拿大或澳大利亚文化 |  | 自由派 |
|  | Orleanist | Orléanist | Orléanist | 是法国或法国叛乱国 尚未消灭君主制或确立其他王朝 | 已消灭君主制或确立其他王朝 | 保守派 |
|  | Legitimist | Legitimist | Legitimist | 是法国或法国叛乱国 尚未消灭君主制或确立其他王朝 | 已消灭君主制或确立其他王朝 | 保守派 |
|  | Bonapartist | Bonapartist | Bonapartist | 是法国或法国叛乱国 尚未消灭君主制或确立其他王朝 | 已消灭君主制或确立其他王朝 | 保守派 |
|  | Carlist | Carlist | Carlist | 主流文化为西班牙、加泰罗尼亚或巴斯克文化 尚未消灭君主制 首都位于伊比利亚 | 满足其一：已消灭君主制 首都不在伊比利亚 | 保守派 |
|  | Miguelist | Miguelist | Miguelist | 主流文化为葡萄牙文化 尚未消灭君主制 首都位于伊比利亚 | 满足其一：已消灭君主制 首都不在伊比利亚 | 保守派 |
|  | Restorationist | Shōjōi | Jingoist Protectionist Mitogaku Shōjōi | 主流文化为日本文化 有 Bakufu 是日本或日本的附属国 | 已消灭君主制 明治维新已完成 | 民族主义者 |
|  | Tokugawa Loyalist | Bakufu | Authoritarian | 主流文化为日本文化 有 Bakufu 是日本或日本的附属国 | 已消灭君主制 天皇已复位 | 保守派 |
|  | Hindu Nationalist | Minoritarian Traditionalist | Fascist Theocrat | 是东印度公司或印度斯坦 已研究 Pan-nationalism 拥有任何一个属于印度文化本土且有印度教人口的州 如果是印度斯坦则至少拥有五个 |  |  |
|  | Muslim Nationalist | Minoritarian Traditionalist | Social Democrat Theocrat | 是东印度公司或马哈拉施特拉 已研究 Pan-nationalism 拥有至少五个属于印度文化本土且有逊尼派、什叶派或伊巴德派人口的州 |  |  |
|  | Slave Revolt | Anti-Slavery | Abolitionist Humanitarian Radical | 未实行任何变体的 Slavery Banned 满足其一：该国至少 15% 的人口是奴隶 某个州至少 55% 的人口是奴隶 | 已实行任何变体的 Slavery Banned |  |

### 开局运动

每个国家根据其开局情形会以若干运动开局。某些国家会拥有另行指定的一组运动，以取代或补充上述运动。
| 运动 | 条件 | 排除的国家 |
|---|---|---|
| 绝对主义者 | 为君主制 无投票权 无幕府 | [法国](France.md) [葡萄牙](Portugal.md) [西班牙](Spain.md) [卡洛斯派西班牙](Carlist Spain.md) |
| 保皇派 | 为君主制 有投票权或为葡萄牙 | [法国](France.md) |
| 支持奴隶制 | 有除殖民奴隶制以外的任意奴隶制 |  |
| 废奴主义 | 有任意奴隶制 已研究经验主义 | [东印度](East India.md) |
| 宗教多数派 |  | [东印度](East India.md) [法国](France.md) [西班牙](Spain.md) [卡洛斯派西班牙](Carlist Spain.md) [葡萄牙](Portugal.md) |
| 文化多数派 |  | 北德与南德国家 北意与南意国家 |
| 劳工运动 | 已研究劳工运动 |  |
| 自由派 | 有投票权 已研究民主 | [法国](France.md) |

| 国家 | 运动 |
|---|---|
| [古巴](Cuba.md) [波多黎各](Puerto Rico.md) | 奴隶起义（非洲-加勒比） |
| [巴西](Brazil.md) | 奴隶起义（非洲-巴西） |
| [法国](France.md) | 波拿巴主义 正统派 奥尔良派 激进派 |
| 北德与南德国家 | 德意志民族 |
| 北意与南意国家 | 意大利民族 |
| [塞尔维亚](Serbia.md) [克罗地亚](Croatia.md) | 南斯拉夫/伊利里亚民族 |
| [奥地利](Austria.md) | 文化少数派（波兰） 文化少数派（捷克） 文化少数派（北意） 自由派（被镇压） |
| [匈牙利](Hungary.md) | 文化少数派（塞尔维亚） 自由派 |
| 普鲁士 俄罗斯 | 文化少数派（波兰） |
| [海地](Haiti.md) | 多米尼加民族 |
| [西班牙](Spain.md) | 卡洛斯派（被镇压） 自由派 |
| [卡洛斯派西班牙](Carlist Spain.md) | 卡洛斯派 自由派（被镇压） 文化少数派（巴斯克） |
| [葡萄牙](Portugal.md) | 米格尔派（被镇压） 自由派 |
| [英国](Great Britain.md) | 文化少数派（爱尔兰） |
| 奥斯曼帝国 巴拉圭 暹罗 | 现代化 |
| [东印度](East India.md) | 功利主义 宗教少数派（印度教） 宗教少数派（逊尼派） 文化少数派（孟加拉） |
| [安大略](Ontario.md) [魁北克](Quebec.md) | 激进派 |
| [日本](Japan.md) | 维新派 德川效忠派 土地改革 |

## 支持

一项运动的支持度各占三分之一地来自支持它的[人口](Pops.md)数量、支持它的军事人员数量以及支持它的财富数量。

- 国家人口中每有 1% 支持该运动，支持度增加 0.34%
- 军事人员中每有 1% 支持该运动，支持度增加 0.33%
- 人口原始政治力量中每有一点支持该运动，支持度增加 0.33%

#### 扶持与镇压

| 影响来源 |  |  |
|---|---|---|
| 禁止异见 | **+50%** | **−50%** |
| 新闻审查 | **+40%** | **−40%** |
| 集会权 | **+30%** | **−30%** |
| 秘密警察下每级内政机构 | — | **−5%** |

政治运动可以被*扶持*或*镇压*，以影响其人口吸引力。扶持或镇压一项政治运动需要消耗 **200** 权威力，且该行动可随时取消。能否扶持或镇压任意利益集团还取决于国家是否拥有扶持或镇压*影响*。这来自法律、机构或 modifier（修正项）。如果其数值为 0%，则无法扶持或镇压运动。

扶持或镇压影响是对人口吸引力数值的修正。

## 激进度

运动基于其对国家当前法律的态度以及该运动的其他各种因素获得激进度。激进度每周向目标值变动 1%。

| 来源 | 影响 |
|---|---|
| 每项已颁布的法律 乘以态度方向与等级 | **±5** |
| 每项近期颁布的法律 乘以态度方向与等级 | **±25** |
| 支持的激进派人口 按占所有支持人口的比例缩放 | **+100** |
| 支持的忠诚派人口 按占所有支持人口的比例缩放 | **−75** |

| 运动 | 来源 | 影响 |
|---|---|---|
| 废奴运动 | 领袖或其利益集团支持奴隶制 | **+10%** |
| 为[美国](America.md)且*奴隶制辩论*处于激活状态 | **+20%** |  |
| 奴隶人口的平均生活水平 | **+50%** 至 **-25%** |  |
| 支持奴隶制运动 | 领袖或其利益集团反对奴隶制 | **+10%** |
| 为[美国](America.md)且*奴隶制辩论*处于激活状态 | **+20%** |  |
| 位于蓄奴州的兵营不足 50% | **+50%** |  |
| 位于蓄奴州的海军行政署不足 50% | **+25%** |  |
| 绝对主义者/保皇派运动 | 合法性高于/低于 50 | 每点 **±0.5%**，从 **+25%** 至 **-25%** |
| 君主制正在被废除 | **+25%**[1] |  |
| 劳工/社会主义/共产主义运动 | 职场安全与社会保障的机构投入等级[2] | 低于 3 级时每级 **+5%**，或无机构时 **+10%**；高于 3 级时每级 **-5%** |
| 社会主义运动 | 生活水平低于 15 | 生活水平每低于 15 一点 **+3%** |
| 社会主义/共产主义/无政府主义运动 | 工厂委员会正在被废除 | **+25%** |
| 无政府主义运动 | 生活水平低于 15 | 生活水平每低于 15 一点 **+1.5%** |
| 共产主义/无政府主义运动 | 运动支持度 | 每点支持度 **+0.5%**，最高 **+25%** |
| 法西斯运动 | 运动支持度 | 每点支持度 **+1%**，最高 **+50%** |
| 领土主张 | **+12.5%**，每项主张再 **+2.5%**，总计最高 **+30%** |  |
| 自由派/激进派/社团主义/功利主义运动 | 教育投入过低 | 低于 3 级时每级 **+5%**，或无机构时 **+10%**（功利主义运动无机构时为 **+5%**） |
| 自由派运动 | 选举信心过低 | 选举信心一旦跌破 90%，每低于 100% 一个百分点 **+0.2%**；上限 **+20%**，并按选举信心影响缩放 |
| 为[葡萄牙](Portugal.md)且*吞噬者统治*处于激活状态 | **+20%** |  |
| 激进派运动 | 选举信心过低 | 选举信心一旦跌破 90%，每低于 100% 一个百分点 **+0.2%**；上限 **+20%** |
| 执法投入 | 高于 2 级时每级 **+5%**，1 级 **-5%**，无机构 **-10%** |  |
| 缺少普选制 | **+15%** |  |
| 反动运动 | 激进派人口比例 | 每个百分点 **+0.5%**，最高 **+50%** |
| 现代化运动 | 被一个受承认的政权强制执行战争目标 | **+10%** |
| 未受承认且已研究民族主义 | **+10%** |  |
| 文化与宗教多数派运动 | 统治者不属于主流文化/宗教 | **+10%** |
| 相同文化/宗教的邻近革命运动 | **+15%** |  |
| 该文化/宗教人口的生活水平低于全国平均 | 每低于全国平均一点 **+5%**，最高 **+50%** |  |
| 与[教宗国](Papal States.md)关系不佳（仅限天主教） | 在关系为 −100 时最高 **+25%** |  |
| 文化多数派运动 | 已研究民族主义，且该文化拥有一块不属于任何以其为主流文化的国家的本土州 | 每州 **+2.5%**，最高 **+25%** |
| 文化少数派运动 | 文化狂热度 | 每点狂热度 **+0.25%**，除非该文化处于完全接纳状态 |
| 文化接纳度低 | **+10%** 至 **+30%** |  |
| 文化与宗教少数派运动 | 该文化人口的生活水平低于全国平均 | 每低于全国平均一点 **+5%**，最高 **+50%** |
| 认同内部支持度过低 | 宗教运动支持度每低于 **50%**、文化运动每低于 **25%** 一点 **-1%** |  |
| 与[教宗国](Papal States.md)关系不佳（仅限天主教宗教少数派） | 在关系为 −100 时最高 **+25%** |  |
| 相同文化/宗教的邻近革命运动 | **+15%** |  |
| 支持其他起义运动 | 支持其他运动的人口每有 1% **+0.25%**，最高 **+25%** |  |
| 印度民族、印度教民族主义与穆斯林民族主义 | 独立倾向 | 每点 **+0.2%**，最高 **+20%** |
| 为附属国（印度民族） | **+25%**（自治领为 **+10%**） |  |
| 为附属国（印度教民族主义、穆斯林民族主义） | **+15%**（自治领为 **+5%**） |  |
| 德意志、意大利与南斯拉夫民族运动 | 统治者不属于主流文化 | **+10%** |
| 已研究民族主义且另一国为统一候选国 | **+10%** |  |
| 已研究泛民族主义且未拥有全部核心州 | **+10%** |  |
| 德意志、意大利或南斯拉夫文化的平均狂热度 | 每点 **+0.25%**，最高 **+25%** |  |
| 德意志民族运动 | *什勒斯维希-霍尔斯坦问题*处于激活状态 | **+10%** |
| 法国、西班牙与葡萄牙君主派 | 君主属于不同王朝 | **+25%** |
| 正统派、卡洛斯派与米格尔派运动 | 与[教宗国](Papal States.md)关系不佳 | 在关系为 −100 时最高 **+25%** |
| 卡洛斯派运动 | [西班牙](Spain.md)的日志条目*第一次卡洛斯战争*处于激活状态 | **−95%** |
| 奴隶起义运动 | 领袖或其利益集团支持奴隶制 | **+10%** |
| 奴隶人口的平均生活水平 | **+30%** 至 **-25%** |  |
| 奴隶人口相对陆军力量投射 | **+75%** 至 **-50%** |  |

开始或取消法律颁布时，新目标激进度的一半会立即生效，其余部分则照常逐步变动。

激进度低于 25% 的运动不影响颁布的成功与失败几率。此外，当运动对其持有态度的法律正在颁布时，激进度不会降到 25% 以下。

激进度超过 50% 的运动变得*顽固*。

激进度超过 75% 的运动变得*革命性*。

激进度超过 50 的运动还会增加人口激进度。每月有 **0.5%** 到 **2.5%** 支持该运动的人口变得更加激进。

## 革命

革命性运动开始组织发动内战。这以一条从 0% 到 100% 的进度条表示。如果进度条达到 100%，革命将发起一场[外交博弈](Diplomatic play.md)以推翻国家现政府。如果发生这种情况，玩家可以选择扮演政府或革命一方。因此革命可以被玩家用作国家政治与社会变革的工具。

革命进度主要基于运动的激进度，但[某些事件](Revolution events.md)也能增加或减少进度。革命进度会定期更新，基础间隔为 8 周。每个检查点还会触发一个革命事件。

如果政治运动解散或激进度低于 50，革命立即停止组织。

### 革命进度

每个检查点，革命进度向运动的激进度数值变动。变动量限制在 **−10%** 到 **+25%** 之间。激进度低于 100 的运动绝不会引发内战，除非某个事件使进度超过 100%。

### 革命州

在革命组织期间，悬停其上可看到哪些州可能加入革命。州的比例等于运动支持度的 1.5 倍，上限为国家州数的 75%。如果国家只有一个州，则该州将被分割。

每个州加入革命的概率基于支持革命的利益集团在当地的政治力量，并对相邻州有额外偏向，以避免出现犬牙交错的情况。

### 内战

一旦革命进度达到 100%，革命立即成立一个革命国家并发起一场革命[外交博弈](Diplomatic play.md)。在*开局行动*阶段，玩家可以选择倒戈，扮演革命一方而非政府。其他国家可以照常加入该外交博弈，但并非所有拉拢选项都可用。

革命国家基于本国的定义，这意味着游戏过程中对承认状态、主流文化和国教的更改不会被复制。革命国家确实会复制已研究的技术。法律也会全部复制，但运动期望的法律会被颁布，外加支持运动的利益集团偏好的至多两项法律。原国家保留所有外交协议，而革命国家从零开始。所有隶属于革命利益集团的人物都会转投新的革命国家。

内战爆发时，支持叛乱利益集团的人口中的所有激进派都变为中立。

### 内战结束

内战结束时，所有激进派中的 50% 变为中立，支持战败利益集团的人口中额外有 25%、支持战胜利益集团的人口中额外有 50% 变为中立。

失败的利益集团还会承受 **−100%** 政治力量，持续 10 年。

## 参考

1. ↑ 若君主制正在被废除，则取代合法性修正
2. ↑ 共产主义运动仅涉及职场安全

1. 参见 /Victoria 3/game/common/defines/00_defines.txt：与政治运动和革命相关的 defines 见 `NPolitics`

游戏概念
返回顶部
| 人口 | [人口](Pops.md) • [接纳度](Acceptance.md) • [文化](Culture.md) • [迁移](Migration.md) • [需求](Needs.md) • [职业](Profession.md) • [宗教](Religion.md) • [生活水平](Standard of living.md) |
|---|---|

| 政府 | [政府](Government.md) • [能力](Capacity.md) • [人物](Character.md) • [法令](Decrees.md) • [机构](Institutions.md) • [法律](Laws.md) • [技术](Technology.md) |
|---|---|

| 政治 | [选举](Elections.md) • [意识形态](Ideology.md) • [利益集团](Interest group.md) • [政治游说](Political lobby.md) • 政治运动 • [政党](Political party.md) • [革命](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| 经济 | [建筑](Building.md) • [商品](Goods.md) • [收成状况](Harvest condition.md) • [基础设施](Infrastructure.md) • [市场](Market.md) • [生产方式](https://vic3.paradoxwikis.com/Production_methods) • [州](State.md) • [国库](Treasury.md) |
|---|---|

| 外交 | [外交](Diplomacy.md) • [外交行动](https://vic3.paradoxwikis.com/Diplomatic_action) • [外交博弈](Diplomatic play.md) • [强权集团](Power bloc.md) • [等级](Rank.md) • [附属国](Subject.md) • [条约](Treaty.md) |
|---|---|

| 战争 | [战争](Warfare overview.md) • [陆战](Land warfare.md) • [海战](Naval warfare.md) • [战争目标](https://vic3.paradoxwikis.com/Wargoal) • [征兵](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| 其他 | [国家](Countries.md) • [决策](Decision.md) • [事件](Events.md) • [日志](Journal.md) • [目标](Objective.md) • [游戏内百科](Vickypedia.md) |
|---|---|