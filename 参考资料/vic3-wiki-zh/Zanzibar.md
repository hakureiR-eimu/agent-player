---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Zanzibar
source: https://vic3.paradoxwikis.com/Zanzibar
pageid: 8338
categories: [Pages_using_TabberTransclude_parser_tag, 1.13, Countries, Pages_with_interwiki_links_to_Wikipedia, Needs_strategy_guide, Releasable_countries]
fetched: 2026-10-27
---
本文已针对游戏当前[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核对。

桑给巴尔
---

首都
：
桑给巴尔
---

政府类型
：
释放时决定
---

主流文化
：
斯瓦希里
---

国教
：
逊尼派
---

国家层级
：
公国
---

国家类型
：
未受认可
桑给巴尔
---

首都
：
桑给巴尔
---

政府类型
：
释放时决定
---

主流文化
：
斯瓦希里
---

国教
：
逊尼派
---

国家层级
：
公国
---

国家类型
：
未受认可
**桑给巴尔**是东非的一个特殊国家，在 1836 年游戏开始时并不存在，但可以在[阿曼](Oman.md)统治者赛义德·本·苏尔坦去世后，经由[阿曼分裂](Oman.md)事件触发的[桑给巴尔的崛起](Oman.md)事件而出现。这些事件允许玩家选择继续扮演阿曼或桑给巴尔，并会将阿曼拥有的阿伊卡、林迪、肯尼亚或东非大裂谷各州的一部分割让给桑给巴尔，或者让桑给巴尔获得对这些州的[宣称](https://vic3.paradoxwikis.com/Claims)。在游戏开始时，阿曼实际只拥有桑给巴尔本岛以及肯尼亚的一部分。

如果桑给巴尔是通过*阿曼分裂*日志条目释放的，它将以贝都因人而非斯瓦希里人为主流文化，信奉伊巴德派而非逊尼派。

以贝都因人为主流文化时，桑给巴尔可以成立[阿拉伯](Arabia.md)。

## 脚本内容

id

### 泽之王

我们对非洲的控制与其说是真实的，不如说是名义上的，但鲜有其他国家意识到这一点。我们的首要任务应是巩固对大陆领土的控制，或通过外交周旋获得认可，或通过直接征服来扩大我们在该地区的实际存在。如果我们失败，整个桑给巴尔可能一夜之间土崩瓦解。
---

| 可见条件：仅激活时可见 |  |
|---|---|
| 激活条件：是桑给巴尔 | 激活时效果：无 |
| 完成条件：至少满足其一 桑给巴尔已受认可 满足全部条件： 桑给巴尔拥有整个东非大裂谷 桑给巴尔拥有整个坦噶尼喀 桑给巴尔拥有整个肯尼亚 桑给巴尔拥有整个桑给巴尔 桑给巴尔拥有整个鲁菲吉 | 完成时效果：触发事件 阿齐莎女王的后裔 若以下各州区域未被桑给巴尔完全拥有，桑给巴尔获得对其的宣称： 肯尼亚 东非大裂谷 桑给巴尔 坦噶尼喀 鲁菲吉 若这五个州区域全部由桑给巴尔控制，且贝都因为主流文化，桑给巴尔将成为贝都因人的本土 若这五个州区域全部由桑给巴尔控制，且斯瓦希里为主流文化，东非大裂谷、坦噶尼喀和鲁菲吉将成为斯瓦希里人的本土 |
| 失败条件：满足其一： 桑给巴尔是其他国家的附属国 任何首都位于非洲之外的国家拥有以下任一州的领土，或其附属国拥有以下任一州： 肯尼亚 东非大裂谷 桑给巴尔 坦噶尼喀 鲁菲吉 | 失败时效果：触发事件 失去威严的雄狮 将该州区域内除首都外的每个州割让给邻近的殖民列强（若存在），否则该州将成为独立的军阀国家。 |

id

### 失去威严的雄狮

[Non-African Country]的殖民地官员绕过了我们的前哨站，与我们长期宣称处于统治之下的内陆酋长们达成了协议。我们的东非霸权幻想随此举一夜崩塌，当地军阀和其他殖民列强正在迅速瓦解我们帝国的残余。
---

背景文本：
“[Non-African Country]军靴铿锵的步伐穿过桑给巴尔，惊醒了整座城市。士兵们向主广场行进时，越来越多的人聚集跟随其后。当他们升起[Country]的国旗时，人群倒吸一口凉气。这些人是谁？苏丹在哪里？桑给巴尔发生了什么？”
---

| 触发条件：日志条目 泽之王 失败 |
|---|
| 触发条件：是桑给巴尔 |
| 这是桑给巴尔最黑暗的时刻。[Non-African Country]夺取了我们的帝国，把我们压缩到只剩桑给巴尔一隅 若乌特特拉存在且为桑给巴尔的附属国： 乌特特拉脱离桑给巴尔独立 若 [Non-African Country] 是桑给巴尔的附属国：[Non-African Country] 脱离桑给巴尔独立 |

id

### 阿齐莎女王的后裔

凭借巧妙的外交与精湛的治国之道，我们已牢牢控制了泽之地。今天，桑给巴尔巍然屹立！
---

背景文本：
“一份新的小册子在桑给巴尔的咖啡馆与书商之间流传开来：《桑给巴尔真史》。这是一部民间史，讲述了温古贾岛在阿齐莎女王领导下辉煌的起源——这位神话般的人物几乎已被彻底遗忘。正如阿齐莎一样，桑给巴尔本身也已从阴影中走出，重新夺回聚光灯下的一席之地。每一张容光焕发的桑给巴尔面孔上，都能看到这种光芒——他们阅读着自己辉煌的过去，梦想着辉煌的未来。”
---

| 触发条件：日志条目 泽之王 完成 |
|---|
| 触发条件：无 |
| 对我们所有人来说都是辉煌的一天！ 若肯尼亚、东非大裂谷、桑给巴尔、坦噶尼喀和鲁菲吉被完全拥有： 若贝都因为主流文化： 桑给巴尔成为贝都因人的本土 若斯瓦希里为主流文化： 东非大裂谷、坦噶尼喀、鲁菲吉成为斯瓦希里人的本土 若尚未拥有，则获得对肯尼亚、东非大裂谷、桑给巴尔、坦噶尼喀和鲁菲吉的宣称 |

id

### 蒂普·蒂普

一位野心勃勃的奴隶与象牙商人哈马德·本·穆罕默德·穆尔贾比请求桑给巴尔支持一次殖民冒险。他提议在卢阿拉巴建立一个新政府。如果支持他，他的国家将成为我们的附属国，但列强会对此不满，并大幅推迟我们获得认可的进程。
---

背景文本：
“他们为什么叫你‘蒂普·蒂普’，哈马德？”大象商队开始涉水渡过另一条河时，外国人问道。

商人笑了。“这是因为我的枪声，你瞧——哦，糟了，快看！”

他冲向水边，向他的商队呼救。

“装满奴隶的船沉了！”他喊道。“真可惜！那可是条好独木舟。”
---

| 触发条件：日期晚于 1865.1.1 且早于 1890.1.1 |
|---|
| 触发条件：无 |
| 不能支持蒂普·蒂普，但我们也不敢谴责他。 乌特特拉将在卢阿拉巴建立 我们欢迎在刚果的这个立足点 乌特特拉将在卢阿拉巴建立，作为桑给巴尔的附属国 制止蒂普·蒂普，在其成势之前了结此事！ 哈马德·穆尔贾比将以传统主义者鼓动家身份出现在桑给巴尔 启用条件： 统治者拥有蓄奴主义者意识形态，或执政的任一利益集团拥有蓄奴主义者意识形态 让蒂普·蒂普相信，他可以在这里和我们更好地实现他的利益 哈马德·穆尔贾比将以将军身份出现在桑给巴尔 |

### 阿拉伯统治的终结？

[Zanzibar Ruler]的崛起标志着数百年阿拉伯统治的终结，这位著名的 [Zanzibar Ruler Culture] 人物备受瞩目。斯瓦希里领袖们要求利用这一历史性时刻，正式推翻贝都因人在桑给巴尔的主导地位。"
---

背景文本：
“桑给巴尔老石头城的街道空无一人。所有人都把自己关在家中，等待明天的到来。

起初，有些人曾欢呼庆祝，声称虽然一百个部族在数世纪前失去了自由，但一个国家在今天重新获得了自由。另一些人则望着这座白色沙滩与蔚蓝海水环绕的岛屿，担心如果今天无所作为，明天就会失去一切。他们都曾短暂地涌上街头，很快便彼此相遇。

太多人突然意识到自己的邻居对自己而言是陌生人，于是现在他们并肩而坐，独自等待。”
---

| 触发条件：统治者更替 |
|---|
| 触发条件：无 |
| 桑给巴尔属于斯瓦希里民族！ 斯瓦希里成为主流文化 逊尼派成为国教 贝都因不再是主流文化 20% 的贝都因人口变得更加激进 “一位斯瓦希里统治者无关紧要——桑给巴尔仍属于贝都因人。” 20% 的斯瓦希里人口变得更加激进 |

### 历史人物

| 姓名 | 类型 | 利益集团 | 意识形态 | 特质 | 条件 |
|---|---|---|---|---|---|
| [马吉德·布赛义迪](http://en.wikipedia.org/wiki/Majid_bin_Said_of_Zanzibar) | 统治者 | ![Undecided](/images/thumb/2/2d/Political_undecided.png/24px-Political_undecided.png) 随机 | ![Undecided](/images/thumb/2/2d/Political_undecided.png/24px-Political_undecided.png) 随机 | 内敛、机智、高尚、经验丰富的外交官 | *桑给巴尔的崛起*事件 |
| [巴尔加什·布赛义迪](http://en.wikipedia.org/wiki/Barghash_bin_Said_of_Zanzibar) | 继承人 | 地主 | 温和派 | 富有魅力、顺从 | *桑给巴尔的崛起*事件，1837.1.1 之后 |
| 苏莱曼·布赛义迪 | 政治家 | 地主 | 温和派 | 高尚、严谨、行政大师 | 日期在 1836.1.1 与 1870.1.1 之间 是桑给巴尔 |
| 穆希丁·卡赫塔尼 | 政治家 | 虔信派 | 少数派传统主义者 | 机智、虔诚、鼓舞人心的演说家 | 日期在 1836.1.1 与 1850.1.1 之间 是桑给巴尔 |
| [阿卜杜勒-阿齐兹·阿玛维](http://en.wikipedia.org/wiki/Abd_al_Aziz_al-Amawi) | 政治家 | 虔信派 | 少数派传统主义者 | 勇敢、虔诚、坚韧、文学 | 日期在 1854.1.1 与 1884.1.1 之间 是桑给巴尔 |
| [阿特金斯·哈默顿](http://en.wikipedia.org/wiki/Atkins_Hamerton) | 政治家 |  | 废奴主义者 | 审美家、富有魅力、体弱多病、政治任命 | 日期在 1836.1.1 与 1856.1.1 之间 是桑给巴尔 未废除奴隶制 未与英国敌对 |
| [理查德·沃特斯](http://en.wikipedia.org/wiki/East_India_Marine_Society) | 政治家 |  | 废奴主义者 | 虔诚、偏执、奢侈品味、殖民地行政官 | 日期在 1836.1.1 与 1845.1.1 之间 是桑给巴尔 未与美国敌对 |
| [杰拉姆·希夫吉](http://en.wikipedia.org/wiki/Jairam_Shivji) | 政治家 | 实业家 | 温和派 | 严谨、机智、行政大师 | 日期在 1836.1.1 与 1845.1.1 之间 是桑给巴尔 |
| 穆罕默德·本·艾哈迈德·阿拉维 | 政治家 | 乡民 | 保皇派 | 奢侈品味、残忍、顺从 | 日期在 1836.1.1 与 1855.8.6 之间 是桑给巴尔 |
| 赫里·本·朱马·马法齐 | 政治家 |  | 改革派 | 坚韧、创新、外交官 | 日期在 1860.1.1 与 1890.1.1 之间 是桑给巴尔 |
| 鼓动家 | 日期在 1870.1.1 与 1890.1.1 之间 是桑给巴尔或拥有桑给巴尔 |  |  |  |  |
| 阿明·本·阿里·马兹鲁伊 | 政治家 | 知识分子 | 激进派 | 虔诚、创新、文学 | 日期在 1910.1.1 与 1936.1.1 之间 满足其一： 是蒙巴萨 是桑给巴尔且蒙巴萨不存在 |
| [阿里·本·萨利姆·布赛义迪](http://en.wikipedia.org/wiki/Ali_bin_Salim_Al_Busaidi) | 政治家 | 地主 | 温和派 | 偏执、虔诚、顺从、博学 | 日期在 1909.1.1 与 1936.1.1 之间 是桑给巴尔且贝都因为主流文化 |
| 索拉比吉·达鲁卡纳瓦拉 | 政治家 | 工会 | 温和派 | 创新、机智、测量师 | 日期在 1880.1.1 与 1905.1.1 之间 是桑给巴尔 |
| 萨布里·本·萨菲尔 | 政治家 将军 | 军队 | 温和派 | 残忍、直率、严谨、政治操盘手 | 日期在 1850.1.1 与 1870.1.1 之间 是桑给巴尔 |
| [哈马德·穆尔贾比](http://en.wikipedia.org/wiki/Tippu_Tip) | 政治家 将军 | 地主 | 蓄奴主义者 | 富有魅力、威严、勇敢、探险家 | 由事件产生 若该国未废除奴隶制，意识形态转为传统主义者 |
| [萨拉玛·布赛义迪](http://en.wikipedia.org/wiki/Emily_Ruete) | 鼓动家 | 地主 | 改革派 | 勇敢、创新、浪漫、博学 | 日期在 1860.8.30 与 1894.8.30 之间 是桑给巴尔 |
| [巴希尔·本·萨利姆·哈尔西](http://en.wikipedia.org/wiki/Abushiri) | 鼓动家 |  | 激进派 | 傲慢、富有魅力、政治操盘手 | 日期在 1870.1.1 与 1900.1.1 之间 满足其一： 是桑给巴尔 首都在非洲之外且拥有桑给巴尔 |

## 经济

### 州

| 名称 | 类型 | 本土 | 区域 | 可耕地 | 资源 | 州特质 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| 规模 | 用途 |  |  |  |  |  |  |  |  |
| 桑给巴尔 |  | 湖班图人 斯瓦希里人 苏库马人 | 东非 | 70 | 小米农场 畜牧场 香蕉种植园 咖啡种植园 棉花种植园 染料种植园 糖料种植园 茶叶种植园 烟草种植园 | 8 | 10 | (16) | 天然良港 +10% 造船厂吞吐量 +10% 港口吞吐量 +5% 市场接入价格影响 +15% 贸易容量 疟疾 −90% 非本土州殖民增长速度 +15% 非本土州死亡率 |
| 肯尼亚 |  | 索马里人 基库尤人 湖班图人 斯瓦希里人 马赛人 | 东非 | 80 | 小米农场 畜牧场 香蕉种植园 咖啡种植园 棉花种植园 染料种植园 糖料种植园 茶叶种植园 烟草种植园 葡萄园 | 6 | 10 | (16) | 疟疾 −90% 非本土州殖民增长速度 +15% 非本土州死亡率 |

## 策略与指南

有桑给巴尔的优秀策略吗？
+
将其添加到本文
帮助其他玩家！
请注意
风格指南
和
示例页面
。

## 动态国旗

- 默认国旗
- 是共和制 共和制需要：● 企业国家、总统共和制、议会共和制或委员会共和制 ，没有斯瓦希里主流文化
- 是共和制 共和制需要：● 企业国家、总统共和制、议会共和制或委员会共和制 ，拥有斯瓦希里主流文化

## 参考

返回顶部
国家
按地区划分
Tabber需要JavaScript才能使用。
| 东非地区 | [阿尔西兰](https://vic3.paradoxwikis.com/Arsiland) [安戈谢](Angoche.md) [安科莱](https://vic3.paradoxwikis.com/Ankole) [奥萨](Aussa.md) [贝格姆迪尔](https://vic3.paradoxwikis.com/Begemder) [布干达](https://vic3.paradoxwikis.com/Buganda) [布尼奥罗](https://vic3.paradoxwikis.com/Bunyoro) [布隆迪](https://vic3.paradoxwikis.com/Burundi) [加沙](Gaza.md) [盖莱迪](Geledi.md) [戈贾姆](https://vic3.paradoxwikis.com/Gojjam) [哈迪亚](https://vic3.paradoxwikis.com/Hadiya) [哈勒尔](https://vic3.paradoxwikis.com/Harar) [伊萨克](Isaaq.md) [卡法](https://vic3.paradoxwikis.com/Kaffa) [卡拉格韦](https://vic3.paradoxwikis.com/Karagwe) [马达加斯加](Madagascar.md) [马吉尔廷](Majerteen.md) [蒙巴萨](Mombasa.md) [夸拉](https://vic3.paradoxwikis.com/Qwara) [卢旺达](https://vic3.paradoxwikis.com/Rwanda) [绍阿](Shewa.md) [锡达莫](https://vic3.paradoxwikis.com/Sidamo) [提格雷](https://vic3.paradoxwikis.com/Tigray) [通吉](Tungi.md) [瓦尔桑加利](Warsangali.md) [韦莱加](https://vic3.paradoxwikis.com/Welega) [维图](Witu.md) [沃莱塔](https://vic3.paradoxwikis.com/Wolaita) |
|---|---|

| 赤道非洲/南部非洲地区 | [巴吉尔米](Bagirmi.md) [巴苏陀兰](Basutoland.md) [加沙](Gaza.md) [格里夸兰](Griqualand.md) [刚果](Kongo.md) [奥兰治](Oranje.md) [菲利波利斯](Philippolis.md) [南非](South Africa.md) [斯威士兰](https://vic3.paradoxwikis.com/Swaziland) [德兰士瓦](Transvaal.md) [瓦达伊](Wadai.md) [祖鲁](Zulu.md) |
|---|---|

| 北非/尼罗河流域地区 | [艾特阿巴斯](https://vic3.paradoxwikis.com/Ait_Abbas) [君士坦丁](https://vic3.paradoxwikis.com/Constantine) [达尔富尔](https://vic3.paradoxwikis.com/Darfur) [埃及](Egypt.md) [费赞](Fezzan.md) [马斯卡拉](https://vic3.paradoxwikis.com/Mascara) [摩洛哥](Morocco.md) [图古尔特](https://vic3.paradoxwikis.com/Touggourt) [的黎波里塔尼亚](Tripolitania.md) [突尼斯](Tunis.md) |
|---|---|

| 西非地区 | [阿散蒂](Ashanti.md) [贝宁](Benin.md) [博尔古](https://vic3.paradoxwikis.com/Borgu) [博尔努](Bornu.md) [达荷美](Dahomey.md) [戈比尔](Gobir.md) [富塔贾隆](https://vic3.paradoxwikis.com/Futa_Jallon) [富塔托罗](https://vic3.paradoxwikis.com/Futa_Toro) [卡尔塔](https://vic3.paradoxwikis.com/Kaarta) [利比里亚](Liberia.md) [马西纳](https://vic3.paradoxwikis.com/Massina) [奥约](Oyo.md) [塞古](https://vic3.paradoxwikis.com/Segou) [塞拉利昂](Sierra Leone.md) [索科托](Sokoto.md) |
|---|---|

| 可成立 | [阿尔及利亚](Algeria.md) [埃塞俄比亚](Ethiopia.md) [利比亚](Libya.md) [马格里布](Maghreb.md) [马里](Mali.md) [津巴布韦](Zimbabwe.md) |
|---|---|

| 可释放 | [昔兰尼加](https://vic3.paradoxwikis.com/Cyrenaica) [霍比亚](Hobyo.md) [苏丹](https://vic3.paradoxwikis.com/Sudan) [韦洛](https://vic3.paradoxwikis.com/Wello) 桑给巴尔 |
|---|---|
Template:Country navbox/EuropeWest
Template:Country navbox/MiddleEast
Template:Country navbox/India
Template:Country navbox/AsiaEast
Template:Country navbox/AmericaNorth
Template:Country navbox/Other
**注：**本表按超级区域和区域列出可游玩的国家。开局国家按其首都所在的州所属区域列出，开局时不存在、可通过成立或释放获得的国家则按超级区域单独列出。松散型（不可游玩）国家及特殊情况另行列出。