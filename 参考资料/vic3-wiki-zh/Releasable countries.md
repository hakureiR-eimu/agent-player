---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Releasable countries
source: https://vic3.paradoxwikis.com/Releasable_countries
pageid: 3882
categories: [1.13, Countries, Releasable_countries, Lists]
fetched: 2026-10-27
---
本文已针对游戏当前[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

一些在游戏开始前或游戏过程中已彻底消亡的国家可以被*释放*并重返历史舞台。国家可以通过两种方式释放：在自己拥有的州上通过外交界面释放，或通过“解放国家”（Liberate Country）外交博弈从他国的州上释放。释放国家的条件通常与[国家成立](Formable countries.md)类似，有些国家在不存在的状态下既可以被成立也可以被释放。

## 外交释放

要通过外交方式释放一个国家，需要满足以下条件：

- 被释放的国家当前不存在
- 控制被释放国家的首都州，包括通过附属国间接控制
- 释放国的首都与被释放国家的首都不在同一个州
- 控制被释放国家足够数量的*核心*州（全部或部分）
- 部分国家有额外的释放条件

*注意：*释放国家**不**要求处于和平状态。

条件满足后，即可在“外交”标签页中点击释放该国的按钮。被释放的国家可以作为独立国家，也可以作为释放国的[附属国](Subject.md)，两种情况下玩家都可以选择切换去游玩这个新释放的国家。释放国还可以选择是否保留自己的本土州。被释放的国家获得释放国手中的所有核心州，但不包括释放国附属国手中的州，也不包括释放国的首都州。所有被释放的州对被释放国家而言都是整合州。

被释放的国家初始采用与释放国相同的法律。

以附属国形式释放时，新国家的附属类型取决于释放国的受承认地位以及被释放国家的类型。此外，无足轻重的政权和未受承认的政权不能将国家作为附属国释放。[1]

| 国家类型 | 宗主国受承认地位 |  |  |
|---|---|---|---|
|  | 已受承认 | 未受承认 |  |
| 已受承认 | 傀儡国 | 附庸国 |  |
| 未受承认 |  |  |  |
| 殖民地 | 殖民地 |  |  |

## 解放国家战争目标

“解放国家”战争目标的对象必须直接持有被解放国家的首都州，且该首都州必须位于行动国家已声明利益的区域。此外，目标国家必须自身有能力释放该国。添加此战争目标需要消耗 30 点机动。如果该战争目标被强制执行，被解放的国家与解放者获得 **+50** 关系，与被迫释放它的国家获得 **−50** 关系。

## 事件释放

某些[事件](Events.md)可以释放国家，少数国家只能以这种方式出现。

## 释放时

当一个国家通过任何方式被释放时，会发生以下情况：

- 如果[保加利亚](Bulgaria.md)作为独立国家被释放，它会激活日志条目[巴尔干的普鲁士](Bulgaria.md)并触发事件[终于自由](Bulgaria.md)
  - 无论保加利亚由谁释放，如果[俄罗斯](Russia.md)没有日志条目“危机与机遇”，则[俄罗斯](Russia.md)触发事件“南斯拉夫人的保护者”[2]
- 如果[南斯拉夫](Yugoslavia.md)被释放，它失去保加利亚主流文化
- 如果[新英格兰](New England.md)被释放，一位随机生成的卢德派意识形态人物接管其乡村民众利益集团
- 如果被释放国家的主流文化为阿什肯纳兹犹太文化（目前仅[以色列](Israel.md)，而巴勒斯坦（州）不是本土，则巴勒斯坦（州）获得塞法迪和阿什肯纳兹本土文化
- 如果被释放的国家是独立国家，拥有非洲流散文化（非裔加勒比、非裔安的列斯、非裔美洲、非裔加勒比尼奥或非裔巴西）且实行遗留奴隶制、殖民奴隶制或奴隶贸易之一，则触发事件[自由宪法](New Africa.md)
- 如果某个欧洲区域的国家作为[奥地利](Austria.md)的附属国被释放且为君主制，其附属类型改为王室领地
- 如果释放的是特许公司，它获得以下法律：

- 殖民行政
- 寡头制
- 附属地位
- 榨取型经济
- 殖民剥削
- 无学校
- 无卫生系统
- 审查制度
- 无工人权利
- 允许童工
- 无社会保障
- 迁移管制

## 可释放国家列表

可释放国家可以按几种方式分类：

1. 按核心州：
  1. 拥有明确定义核心州列表的国家
  2. 以文化本土为核心州的国家
  3. 拥有明确定义拆分州的国家
2. 按必要州：
  1. 仅需首都州
  2. 首都州加上一定最低数量的其他州

AI 从不通过外交方式释放国家，但可能在外交博弈中使用解放国家战争目标。

### 不存在的国家

以下国家在游戏开始时不存在。

| 国家 | 首都 | 必需数量 | 核心州 | 其他条件 |  |
|---|---|---|---|---|---|
| [阿富汗](Afghanistan.md) | 喀布尔斯坦 | 4 | 喀布尔斯坦、赫拉特、坎大哈、哈扎拉斯坦 | 已研究泛民族主义 |  |
| [阿尔巴尼亚](Albania.md) | 阿尔巴尼亚 | 1 | 阿尔巴尼亚 |  |  |
| [阿尔及利亚](Algeria.md) | 君士坦丁 | 1 | 君士坦丁、阿尔及尔、奥兰、撒哈拉、东撒哈拉 |  |  |
| [阿尔泰](Altai.md) | 阿尔泰 | 1 | 阿尔泰 |  |  |
| [亚马孙](Amazonia.md) | 亚马孙 | 1 | 文化本土 |  |  |
| [阿纳瓦克](Anahuac.md) | 墨西哥 | 1 | 文化本土 |  |  |
| [安达卢西亚](https://vic3.paradoxwikis.com/Andalusia) | 下安达卢西亚 | 1 | 下安达卢西亚、上安达卢西亚 |  |  |
| [安戈拉·扬加](Angola Janga.md) | 伯南布哥 | 2 | 伯南布哥、北里奥格兰德、帕拉伊巴、巴伊亚 |  |  |
| [安徽](https://vic3.paradoxwikis.com/Anhui) | 皖南 | 1 | 皖南、皖北 |  |  |
| [安的列斯联盟](Antillean Confederation.md) | 圣多明各 | 1 | 文化本土 |  |  |
| [阿拉干](Arakan.md) | 阿拉干 | 1 | 阿拉干 |  |  |
| [阿拉贡](Aragon.md) | 阿拉贡 | 1 | 阿拉贡 |  |  |
| [亚美尼亚](https://vic3.paradoxwikis.com/Armenia) | 亚美尼亚 | 1 | 亚美尼亚、埃尔祖鲁姆、卡尔斯、伊利沙白波尔 |  |  |
| [阿萨姆](Assam.md) | 阿萨姆 | 1 | 阿萨姆 |  |  |
| [亚述](Assyria.md) | 摩苏尔 | 1 | 摩苏尔、代尔祖尔 | 已研究民族主义 |  |
| [阿斯图里亚斯](Asturias.md) | 阿斯图里亚斯 | 1 | 阿斯图里亚斯 |  |  |
| [澳大利亚](Australia.md) | 新南威尔士 | 1 | 文化本土 |  |  |
| [艾马拉](Aymara.md) | 拉巴斯 | 1 | 文化本土 |  |  |
| [阿塞拜疆](https://vic3.paradoxwikis.com/Azerbaijan) | 巴库 | 1 | 巴库、伊利沙白波尔 |  |  |
| [巴哈马](https://vic3.paradoxwikis.com/Bahamas) | 巴哈马 | 1 | 巴哈马 |  |  |
| [巴伊亚](Bahia.md) | 巴伊亚 | 1 | 巴伊亚 | ![否](/images/thumb/0/04/No.png/24px-No.png) 东北部文化尚未被整合 |  |
| [俾路支斯坦](Baluchistan.md) | 俾路支斯坦 | 1 | 俾路支斯坦 |  |  |
| [巴纳特](Banat.md) | 巴纳特 | 1 | 巴纳特 |  |  |
| [巴什基尔](Bashkiria.md) | 乌法 | 1 | 乌法 |  |  |
| [白俄罗斯](Belarus.md) | 明斯克 | 2 | 文化本土 |  |  |
| [孟加拉](Bengal.md) | 东孟加拉 | 1 | 东孟加拉、西孟加拉 |  |  |
| [比哈尔](https://vic3.paradoxwikis.com/Bihar) | 比哈尔 | 1 | 比哈尔 | 已研究民族主义 |  |
| [波希米亚](https://vic3.paradoxwikis.com/Bohemia) | 波希米亚 | 1 | 波希米亚、摩拉维亚 |  |  |
| [波斯尼亚-黑塞哥维那](https://vic3.paradoxwikis.com/Bosnia-Herzegovina) | 波斯尼亚 | 1 | 文化本土 |  |  |
| [布列塔尼](Brittany.md) | 布列塔尼 | 1 | 文化本土 |  |  |
| [保加利亚](Bulgaria.md) | 北色雷斯 | 1 | 北色雷斯、保加利亚、多布罗加 |  |  |
| [布里亚特](Buryatia.md) | 布里亚特 | 1 | 布里亚特 |  |  |
| [加利福尼亚](California.md) | 加利福尼亚 | 1 | 加利福尼亚 |  |  |
| [加拿大](Canada.md) | 安大略 | 4 | 文化本土 |  |  |
| [卡罗来纳](Carolina.md) | 北卡罗来纳 | 1 | 北卡罗来纳、南卡罗来纳 | ![是](/images/thumb/7/77/Yes.png/24px-Yes.png) 可释放国家游戏规则设为*全部* |  |
| [卡斯蒂利亚](https://vic3.paradoxwikis.com/Castile) | 新卡斯蒂利亚 | 1 | 新卡斯蒂利亚、旧卡斯蒂利亚 |  |  |
| [加泰罗尼亚](Catalonia.md) | 加泰罗尼亚 | 2 | 文化本土 |  |  |
| [切罗基](Cherokee.md) | 阿肯色 | 1 | 文化本土 |  |  |
| [楚科奇](Chukotka.md) | 楚科奇 | 1 | 楚科奇 |  |  |
| [楚瓦什](Chuvashia.md) | 切博克萨雷 | 1 | 切博克萨雷 |  |  |
| [科西嘉](Corsica.md) | 科西嘉 | 1 | 科西嘉 |  |  |
| [美利坚联盟国](Confederate States of America.md) | 弗吉尼亚 | 5 | 文化本土 | ![是](/images/thumb/7/77/Yes.png/24px-Yes.png) 已发生美国内战 |  |
| [赤道邦联](Confederation of the Equator.md) | 伯南布哥 | 1 | 伯南布哥、北里奥格兰德、塞阿拉、皮奥伊、帕拉伊巴、马拉尼昂 | ![否](/images/thumb/0/04/No.png/24px-No.png) 东北部文化尚未被整合 |  |
| [康沃尔](https://vic3.paradoxwikis.com/Cornwall) | 西部乡村 | 1 | 西部乡村的拆分州 | ![是](/images/thumb/7/77/Yes.png/24px-Yes.png) 可释放国家游戏规则设为*全部* |  |
| [哥斯达黎加](https://vic3.paradoxwikis.com/Costa_Rica) | 哥斯达黎加 | 1 | 哥斯达黎加 |  |  |
| [克里特](Crete.md) | 克里特 | 1 | 克里特 |  |  |
| [克里米亚](Crimea.md) | 克里米亚 | 1 | 克里米亚 |  |  |
| [昔兰尼加](https://vic3.paradoxwikis.com/Cyrenaica) | 昔兰尼加 | 1 | 昔兰尼加 |  |  |
| [塞浦路斯](Cyprus.md) | 塞浦路斯 | 1 | 塞浦路斯 |  |  |
| [捷克斯洛伐克](Czechoslovakia.md) | 波希米亚 | 3 | 文化本土 | 已研究泛民族主义 |  |
| [大乘](https://vic3.paradoxwikis.com/Da_Cheng) | 广西 | 1 | 广西 |  |  |
| [达吉斯坦](Dagestan.md) | 达吉斯坦 | 1 | 达吉斯坦 |  |  |
| [但泽](Danzig.md) | 西普鲁士 | 1 | 西普鲁士的拆分州 |  |  |
| [德撒律](Deseret.md) | 犹他 | 1 | 犹他 |  |  |
| [顿河哥萨克军](Don Cossack Host.md) | 罗斯托夫 | 1 | 罗斯托夫、库班、斯塔夫罗波尔 |  |  |
| [萨尔瓦多](https://vic3.paradoxwikis.com/El_Salvador) | 圣萨尔瓦多 | 1 | 圣萨尔瓦多 |  |  |
| [外约旦埃米尔国](https://vic3.paradoxwikis.com/Emirate_of_Transjordan) | 外约旦 | 1 | 外约旦 |  |  |
| [英格兰](England.md) | 内伦敦各郡 | 3 | 内伦敦各郡、米德兰、东盎格利亚、西部乡村、约克郡、兰开夏 |  |  |
| [埃尔西亚-莫克沙](Erzya-Moksha.md) | 坦波夫 | 1 | 坦波夫 |  |  |
| [爱沙尼亚](https://vic3.paradoxwikis.com/Estonia) | 塔林 | 1 | 塔林、北利沃尼亚 |  |  |
| [埃塞俄比亚](Ethiopia.md) | 贡德尔 | 1 | 文化本土 |  |  |
| [远东](Far East.md) | 赤塔 | 1 | 鄂霍次克、堪察加、楚科奇、吉林北部、萨哈林、赤塔、黑龙江北部、布里亚特 |  |  |
| [法兰德斯](https://vic3.paradoxwikis.com/Flanders) | 法兰德斯 | 1 | 文化本土 |  |  |
| [佛罗里达](https://vic3.paradoxwikis.com/Florida) | 佛罗里达 | 1 | 佛罗里达 | ![是](/images/thumb/7/77/Yes.png/24px-Yes.png) 可释放国家游戏规则设为*全部* |  |
| [福尔摩沙](Formosa.md) | 福尔摩沙 | 1 | 福尔摩沙 |  |  |
| [加利西亚](Galicia.md) | 加利西亚 | 1 | 加利西亚 |  |  |
| [加利西亚-洛多梅里亚](Galicia-Lodomeria.md) | 东加利西亚 | 1 | 东加利西亚、西加利西亚 |  |  |
| [格鲁吉亚（高加索）](https://vic3.paradoxwikis.com/Georgia_(GEO)) | 提弗利斯 | 1 | 提弗利斯 |  |  |
| [格鲁吉亚（美国）](https://vic3.paradoxwikis.com/Georgia_(GRG)) | 佐治亚 | 1 | 佐治亚 | ![是](/images/thumb/7/77/Yes.png/24px-Yes.png) 可释放国家游戏规则设为*全部* |  |
| [格陵兰](Greenland.md) | 格陵兰 | 1 | 格陵兰 |  |  |
| [危地马拉](https://vic3.paradoxwikis.com/Guatemala) | 危地马拉 | 1 | 危地马拉 |  |  |
| [贵州](https://vic3.paradoxwikis.com/Guizhou) | 贵州 | 1 | 贵州 |  |  |
| [哈萨瓦底](Hathawaddy.md) | 勃固 | 1 | 勃固 |  |  |
| [豪德诺索尼](https://vic3.paradoxwikis.com/Haudenosaunee) | 纽约 | 1 | 纽约的拆分州 |  |  |
| [哈扎拉贾特](Hazarajat.md) | 哈扎拉斯坦 | 1 | 哈扎拉斯坦 |  |  |
| [霍比奥](Hobyo.md) | 索马里兰 | 1 | 索马里兰的拆分州 |  |  |
| [洪都拉斯](https://vic3.paradoxwikis.com/Honduras) | 洪都拉斯 | 1 | 洪都拉斯 |  |  |
| [湖南](https://vic3.paradoxwikis.com/Hunan) | 湖南 | 1 | 湖南 |  |  |
| [冰岛](Iceland.md) | 冰岛 | 1 | 冰岛 |  |  |
| [伊德尔-乌拉尔](Idel-Ural.md) | 喀山 | 1 | 喀山、乌法、萨马拉、车里雅宾斯克、切博克萨雷 |  |  |
| [伊拉克](https://vic3.paradoxwikis.com/Iraq) | 巴格达 | 1 | 巴格达、摩苏尔、巴士拉 |  |  |
| [爱尔兰](Ireland.md) | 伦斯特 | 2 | 文化本土 |  |  |
| [以色列](Israel.md) | 巴勒斯坦 | 1 | 巴勒斯坦 | 已研究泛民族主义 |  |
| [牙买加](https://vic3.paradoxwikis.com/Jamaica) | 牙买加 | 1 | 牙买加 |  |  |
| [扬马延](Jan Mayen.md) | 北挪威 | 1 | 北挪威的拆分州 | ![是](/images/thumb/7/77/Yes.png/24px-Yes.png) 可释放国家游戏规则设为*全部* |  |
| [爪哇](https://vic3.paradoxwikis.com/Java) | 西爪哇 | 1 | 文化本土 |  |  |
| [克钦](Kachin.md) | 实皆 | 1 | 实皆 |  |  |
| [加里曼丹](https://vic3.paradoxwikis.com/Kalimantan) | 西婆罗洲 | 1 | 西婆罗洲、东婆罗洲、北婆罗洲 |  |  |
| [卡尔梅克](Kalmykia.md) | 卡尔梅克 | 1 | 卡尔梅克 |  |  |
| [堪察加](Kamchatka.md) | 堪察加 | 1 | 堪察加 |  |  |
| [汉特-曼西](Kanty-Mansi.md) | 苏尔古特 | 1 | 苏尔古特、鄂毕 |  |  |
| [卡累利阿](Karelia.md) | 东卡累利阿 | 1 | 东卡累利阿 |  |  |
| [克伦](Karen.md) | 丹那沙林 | 1 | 丹那沙林 |  |  |
| [克什米尔](Kashmir.md) | 克什米尔 | 1 | 克什米尔 |  |  |
| [哈萨克](Kazakhstan.md) | 塞米巴拉金斯克 | 1 | 文化本土 |  |  |
| [克木](Khmu.md) | 老挝 | 1 | 老挝 |  |  |
| [吉尔吉斯](https://vic3.paradoxwikis.com/Kirgizia) | 吉尔吉斯 | 1 | 吉尔吉斯 |  |  |
| [库尔德斯坦](Kurdistan.md) | 摩苏尔 | 1 | 摩苏尔、代尔祖尔、埃尔祖鲁姆、乌尔米耶、波斯库尔德斯坦、迪亚巴克尔 | 已研究民族主义 |  |
| [老挝](Laos.md) | 老挝 | 1 | 老挝 |  |  |
| [拉脱维亚](https://vic3.paradoxwikis.com/Latvia) | 南利沃尼亚 | 1 | 南利沃尼亚、库尔兰 |  |  |
| [黎巴嫩](https://vic3.paradoxwikis.com/Lebanon) | 黎巴嫩 | 1 | 黎巴嫩 |  |  |
| [莱昂](León.md) | 莱昂 | 1 | 莱昂、埃斯特雷马杜拉 |  |  |
| [利比亚](Libya.md) | 的黎波里 | 1 | 的黎波里、昔兰尼加、费赞 |  |  |
| [立陶宛](https://vic3.paradoxwikis.com/Lithuania) | 考纳斯 | 1 | 考纳斯、维尔纽斯 |  |  |
| [伦巴第](https://vic3.paradoxwikis.com/Lombardia) | 伦巴第 | 1 | 伦巴第 |  |  |
| [洛斯阿尔托斯](https://vic3.paradoxwikis.com/Los_Altos) | 危地马拉 | 1 | 恰帕斯的拆分州 |  |  |
| [路易斯安那](Louisiana.md) | 路易斯安那 | 1 | 路易斯安那 |  |  |
| [卢里斯坦](Luristan.md) | 卢里斯坦 | 1 | 卢里斯坦 |  |  |
| [马耳他](Malta.md) | 马耳他 | 1 | 文化本土 |  |  |
| [满洲](Manchuria.md) | 吉林南部 | 1 | 吉林南部、黑龙江南部、吉林北部、盛京、黑龙江北部 |  |  |
| [马里埃尔](Mari El.md) | 切博克萨雷 | 1 | 切博克萨雷 |  |  |
| [玛雅](Maya.md) | 尤卡坦 | 1 | 文化本土 |  |  |
| [马赞德兰](Mazandaran.md) | 马赞德兰 | 1 | 马赞德兰 |  |  |
| [密歇根](Michigan.md) | 密歇根 | 1 | 密歇根 | ![是](/images/thumb/7/77/Yes.png/24px-Yes.png) 可释放国家游戏规则设为*全部* |  |
| [米纳斯吉拉斯](https://vic3.paradoxwikis.com/Minas_Gerais) | 米纳斯吉拉斯 | 1 | 米纳斯吉拉斯、戈亚斯 | 拥有日志条目*整合巴西民族* |  |
| [蒙古](Mongolia.md) | 乌里雅苏台 | 1 | 乌里雅苏台、库伦 |  |  |
| [山地共和国](Mountain Republic.md) | 北高加索 | 1 | 北高加索 |  |  |
| [孟番](https://vic3.paradoxwikis.com/Muang_Phuan) | 老挝 | 1 | 老挝的拆分州 |  |  |
| [梅蒂人](https://vic3.paradoxwikis.com/M%C3%A9tis) | 马尼托巴 | 1 | 文化本土 |  |  |
| [纳瓦拉](Navarra.md) | 巴斯克 | 1 | 巴斯克 |  |  |
| [新阿非利加](New Africa.md) | 佐治亚 | 1 | 佐治亚、路易斯安那、南卡罗来纳、密西西比、亚拉巴马、佛罗里达 |  |  |
| [新英格兰](New England.md) | 马萨诸塞 | 1 | 马萨诸塞、新罕布什尔、缅因、康涅狄格、罗得岛、佛蒙特 |  |  |
| [新西兰](New Zealand.md) | 北岛 | 1 | 北岛、南岛 |  |  |
| [纽芬兰](https://vic3.paradoxwikis.com/Newfoundland) | 纽芬兰 | 1 | 纽芬兰 |  |  |
| [尼加拉瓜](https://vic3.paradoxwikis.com/Nicaragua) | 尼加拉瓜 | 1 | 尼加拉瓜 |  |  |
| [北卡罗来纳](https://vic3.paradoxwikis.com/North_Carolina) | 北卡罗来纳 | 1 | 北卡罗来纳 | ![是](/images/thumb/7/77/Yes.png/24px-Yes.png) 可释放国家游戏规则设为*全部* |  |
| [努纳武特](https://vic3.paradoxwikis.com/Nunavut) | 努纳武特 | 1 | 文化本土 |  |  |
| [奥克西塔尼亚](Occitania.md) | 阿基坦 | 1 | 文化本土 |  |  |
| [巴勒斯坦](https://vic3.paradoxwikis.com/Palestine) | 巴勒斯坦 | 1 | 巴勒斯坦、外约旦 | 已研究民族主义 |  |
| [巴拿马](Panama.md) | 巴拿马 | 1 | 巴拿马 |  |  |
| [保利斯塔尼亚](Paulistânia.md) | 圣保罗 | 1 | 文化本土 | ![否](/images/thumb/0/04/No.png/24px-No.png) 保利斯塔文化尚未被整合 |  |
| [秘鲁](Peru.md) | 利马 | 1 | 利马、卡哈马卡、伊卡、阿雷基帕、塔拉帕卡 |  |  |
| [波兰](Poland.md) | 华沙 | 3 | 文化本土 |  |  |
| [波美拉尼亚](Pomerania.md) | 波美拉尼亚 | 1 | 波美拉尼亚 |  |  |
| [普韦布洛](https://vic3.paradoxwikis.com/Pueblo) | 新墨西哥 | 1 | 文化本土 |  |  |
| [黔](Qian.md) | 粤西 | 1 | 文化本土 |  |  |
| [莱茵兰](https://vic3.paradoxwikis.com/Rhineland) | 北莱茵 | 2 | 北莱茵、莱茵兰、鲁尔 |  |  |
| [里奥格兰德](https://vic3.paradoxwikis.com/R%C3%ADo_Grande) | 里奥格兰德 | 1 | 以下两州的拆分州：里奥格兰德、得克萨斯 |  |  |
| [罗马尼亚](Romania.md) | 瓦拉几亚 | 3 | 文化本土 |  |  |
| [圣卡塔琳娜](https://vic3.paradoxwikis.com/Santa_Catarina) | 圣卡塔琳娜 | 1 | 圣卡塔琳娜 | ![否](/images/thumb/0/04/No.png/24px-No.png) 苏利斯塔文化尚未被整合 |  |
| [圣多明各](Santo Domingo.md) | 圣多明各 | 1 | 圣多明各 |  |  |
| [萨普米](Sapmi.md) | 北挪威 | 1 | 文化本土 |  |  |
| [萨伏依](Savoy.md) | 萨伏依 | 1 | 萨伏依、罗讷 |  |  |
| [斯科讷](https://vic3.paradoxwikis.com/Scania) | 斯科讷 | 1 | 斯科讷 | ![是](/images/thumb/7/77/Yes.png/24px-Yes.png) 可释放国家游戏规则设为*全部* |  |
| [苏格兰](Scotland.md) | 低地 | 1 | 低地、高地 |  |  |
| [山东](https://vic3.paradoxwikis.com/Shandong) | 山东 | 1 | 山东 |  |  |
| [山西](https://vic3.paradoxwikis.com/Shanxi) | 山西 | 1 | 山西 |  |  |
| [西伯利亚](Siberia.md) | 托木斯克 | 4 | 托木斯克、雅库茨克、伊尔库茨克、赤塔、鄂霍次克、楚科奇、上叶尼塞、堪察加、科雷马、阿尔泰、克拉斯诺亚尔斯克、图瓦、布里亚特、鄂毕、苏尔古特、托博尔斯克、乌拉尔、车里雅宾斯克 | 已研究泛民族主义 |  |
| [四川](https://vic3.paradoxwikis.com/Sichuan) | 四川 | 1 | 四川 |  |  |
| [斯洛伐克](https://vic3.paradoxwikis.com/Slovakia) | 西斯洛伐克 | 1 | 文化本土 |  |  |
| [斯洛文尼亚](https://vic3.paradoxwikis.com/Slovenia) | 斯洛文尼亚 | 1 | 文化本土 |  |  |
| [索布](Sorbia.md) | 萨克森 | 1 | 萨克森 |  |  |
| [南卡罗来纳](https://vic3.paradoxwikis.com/South_Carolina) | 南卡罗来纳 | 1 | 南卡罗来纳 | ![是](/images/thumb/7/77/Yes.png/24px-Yes.png) 可释放国家游戏规则设为*全部* |  |
| [斯里兰卡](https://vic3.paradoxwikis.com/Sri_Lanka) | 锡兰 | 1 | 锡兰 |  |  |
| [苏丹](https://vic3.paradoxwikis.com/Sudan) | 青尼罗 | 1 | 青尼罗、科尔多凡、栋古拉 |  |  |
| [叙利亚](https://vic3.paradoxwikis.com/Syria) | 叙利亚 | 1 | 叙利亚、阿勒颇、黎巴嫩、巴勒斯坦、外约旦、代尔祖尔 |  |  |
| [塔吉克](https://vic3.paradoxwikis.com/Tajikistan) | 塔吉克 | 1 | 塔吉克 |  |  |
| [鞑靼斯坦](Tatarstan.md) | 喀山 | 1 | 喀山 |  |  |
| [塔万廷苏尤](Tawantinsuyu.md) | 利马 | 1 | 文化本土 |  |  |
| [多巴](https://vic3.paradoxwikis.com/Toba) | 北苏门答腊 | 1 | 北苏门答腊 |  |  |
| [外高加索](Transcaucasia.md) | 提弗利斯 | 3 | 提弗利斯、亚美尼亚、卡尔斯、巴库、伊利沙白波尔 | 已研究泛民族主义 |  |
| [的里雅斯特](https://vic3.paradoxwikis.com/Trieste) | 伊斯特利亚 | 1 | 伊斯特利亚 |  |  |
| [通古斯](Tungus.md) | 上叶尼塞 | 1 | 上叶尼塞 |  |  |
| [突厥斯坦](Turkestan.md) | 乌兹别克 | 5 | 乌兹别克、费尔干纳、吉尔吉斯、花剌子模、梅尔夫、南突厥斯坦、塔吉克、土库曼、锡尔河、伊犁 |  |  |
| [土库曼](https://vic3.paradoxwikis.com/Turkmenistan) | 土库曼 | 1 | 土库曼、梅尔夫 |  |  |
| [图瓦](Tuva.md) | 图瓦 | 1 | 图瓦 |  |  |
| [乌德穆尔特](Udmurtia.md) | 维亚特卡 | 1 | 维亚特卡 |  |  |
| [乌克兰](Ukraine.md) | 基辅 | 3 | 基辅、东加利西亚、敖德萨、沃里尼亚、亚历山德罗夫斯克、哈尔科夫、克里米亚、切尔尼戈夫 |  |  |
| [阿尔斯特](https://vic3.paradoxwikis.com/Ulster) | 阿尔斯特 | 1 | 阿尔斯特 |  |  |
| [乌拉尔](Ural.md) | 乌拉尔 | 1 | 乌拉尔、车里雅宾斯克、彼尔姆、乌法 |  |  |
| [畏兀儿斯坦](https://vic3.paradoxwikis.com/Uyghuristan) | 塔里木盆地 | 1 | 塔里木盆地、准噶尔、伊犁 |  |  |
| [乌兹别克](https://vic3.paradoxwikis.com/Uzbekistan) | 费尔干纳 | 1 | 费尔干纳、乌兹别克、花剌子模 |  |  |
| [威尼斯](https://vic3.paradoxwikis.com/Venice) | 威尼西亚 | 1 | 威尼西亚 |  |  |
| [万象](https://vic3.paradoxwikis.com/Vientiane) | 老挝 | 1 | 老挝 |  |  |
| [威尔士](Wales.md) | 威尔士 | 1 | 威尔士 |  |  |
| [瓦隆](https://vic3.paradoxwikis.com/Wallonia) | 瓦隆 | 1 | 文化本土 |  |  |
| [韦洛](https://vic3.paradoxwikis.com/Wello) | 阿姆哈拉 | 1 | 贡德尔的拆分州 |  |  |
| [西印度](West Indies.md) | 西印度 | 2 | 西印度、牙买加 |  |  |
| [威斯特伐利亚](Westphalia.md) | 威斯特伐利亚 | 2 | 威斯特伐利亚、北莱茵、鲁尔 |  |  |
| [西北](https://vic3.paradoxwikis.com/Xibei) | 宁夏 | 1 | 宁夏 |  |  |
| [雅库特](Yakutia.md) | 雅库茨克 | 1 | 雅库茨克、科雷马 |  |  |
| [也门](Yemen.md) | 也门 | 1 | 也门 | 已研究民族主义 |  |
| [原住民](https://vic3.paradoxwikis.com/Yuanzhumin) | 福尔摩沙 | 1 | 福尔摩沙 |  |  |
| [尤卡坦](https://vic3.paradoxwikis.com/Yucat%C3%A1n) | 尤卡坦 | 1 | 尤卡坦 |  |  |
| [粤](Yue.md) | 粤西 | 1 | 文化本土 |  |  |
| [南斯拉夫](Yugoslavia.md) | 北塞尔维亚 | 3 | 文化本土 | 已研究泛民族主义 |  |
| [云南](Yunnan.md) | 云南 | 1 | 文化本土 |  |  |
| [直隶](https://vic3.paradoxwikis.com/Zhili) | 河北 | 1 | 河北 |  |  |
| [津巴布韦](Zimbabwe.md) | 赞比西亚 | 1 | 赞比西亚 |  |  |
### 已存在的国家

以下国家在游戏开始时即已存在，但若其消亡则可被释放。

| 国家 | 首都 | 所需数量 | 核心州 | 其他要求 |
|---|---|---|---|---|
| [亚齐](https://vic3.paradoxwikis.com/Aceh) | 亚齐 | 1 | 亚齐 |  |
| [阿伊努莫西里](https://vic3.paradoxwikis.com/Ainu_Mosir) | 北海道 | 1 | 文化故乡 |  |
| [艾特阿巴斯](https://vic3.paradoxwikis.com/Ait_Abbas) | 君士坦丁 | 1 | 君士坦丁的分割州 |  |
| [阿拉斯加](Alaska.md) | 阿拉斯加 | 1 | 阿拉斯加 |  |
| [阿尔瓦尔](https://vic3.paradoxwikis.com/Alwar) | 拉杰普塔纳 | 1 | 拉杰普塔纳的分割州 |  |
| [美国](America.md) | 哥伦比亚特区 | 10 | 文化故乡 |  |
| [安哈尔特](Anhalt.md) | 安哈尔特 | 1 | 安哈尔特 |  |
| [阿拉比斯坦](https://vic3.paradoxwikis.com/Arabistan) | 阿拉比斯坦 | 1 | 阿拉比斯坦 |  |
| [阿根廷](Argentina.md) | 布宜诺斯艾利斯 | 1 | 文化故乡 |  |
| [阿散蒂](Ashanti.md) | 加纳 | 1 | 加纳 |  |
| [奥地利](Austria.md) | 奥地利 | 2 | 文化故乡 |  |
| [阿瓦德](Awadh.md) | 奥德 | 1 | 奥德的分割州 |  |
| [阿扎勒](Azal.md) | 也门 | 1 | 也门的分割州 |  |
| [巴登](Baden.md) | 巴登 | 1 | 巴登 |  |
| [巴林](https://vic3.paradoxwikis.com/Bahrain) | 特鲁西尔海岸 | 1 | 特鲁西尔海岸的分割州 |  |
| [巴哈瓦尔布尔](Bahawalpur.md) | 旁遮普 | 1 | 旁遮普的分割州 |  |
| [巴厘](https://vic3.paradoxwikis.com/Bali) | 巽他群岛 | 1 | 巽他群岛的分割州 |  |
| [班贾尔](https://vic3.paradoxwikis.com/Banjar) | 东婆罗洲 | 1 | 东婆罗洲的分割州 |  |
| [巴罗达](https://vic3.paradoxwikis.com/Baroda) | 古吉拉特 | 1 | 古吉拉特的分割州 |  |
| [巴斯塔](https://vic3.paradoxwikis.com/Bastar) | 那格浦尔 | 1 | 那格浦尔的分割州 |  |
| [巴伐利亚](Bavaria.md) | 巴伐利亚 | 1 | 巴伐利亚 法兰克尼亚 |  |
| [贝根德](https://vic3.paradoxwikis.com/Begemder) | 贡德尔 | 1 | 贡德尔的分割州 |  |
| [比利时](Belgium.md) | 法兰德斯 | 2 | 文化故乡 |  |
| [巴夫那加尔](https://vic3.paradoxwikis.com/Bhavnagar) | 古吉拉特 | 1 | 古吉拉特的分割州 |  |
| [博帕尔](https://vic3.paradoxwikis.com/Bhopal) | 马尔瓦 | 1 | 马尔瓦的分割州 |  |
| [不丹](Bhutan.md) | 东喜马拉雅 | 1 | 东喜马拉雅的分割州 |  |
| [比卡内尔](https://vic3.paradoxwikis.com/Bikaner) | 拉杰普塔纳 | 1 | 拉杰普塔纳的分割州 |  |
| [玻利维亚](Bolivia.md) | 拉巴斯 | 1 | 拉巴斯 圣克鲁斯 波托西 阿克里 安托法加斯塔 |  |
| [巴西](Brazil.md) | 里约热内卢 | 1 | 文化故乡 |  |
| [不来梅](Bremen.md) | 易北 | 1 | 易北的分割州 |  |
| [文莱](https://vic3.paradoxwikis.com/Brunei) | 北婆罗洲 | 1 | 北婆罗洲 |  |
| [不伦瑞克](Brunswick.md) | 不伦瑞克 | 1 | 不伦瑞克 |  |
| [布哈拉](https://vic3.paradoxwikis.com/Bukhara) | 乌兹别克 | 1 | 乌兹别克 |  |
| [缅甸](Burma.md) | 曼德勒 | 1 | 文化故乡 |  |
| [布通](https://vic3.paradoxwikis.com/Buton) | 西里伯斯 | 1 | 西里伯斯 |  |
| [柬埔寨](Cambodia.md) | 柬埔寨 | 1 | 文化故乡 |  |
| [中美洲](Central America.md) | 圣萨尔瓦多 | 3 | 文化故乡 |  |
| [占巴塞](https://vic3.paradoxwikis.com/Champassak) | 老挝 | 1 | 老挝的分割州 |  |
| [车臣](Chechnya.md) | 北高加索 | 1 | 北高加索 |  |
| [清迈](Chiang Mai.md) | 清迈 | 1 | 清迈 |  |
| [智利](Chile.md) | 圣地亚哥 | 1 | 圣地亚哥 洛斯里奥斯 |  |
| [中国](China.md) | 北京 | 5 | 文化故乡 |  |
| [切尔克斯亚](Circassia.md) | 库班 | 1 | 库班 |  |
| [克罗地亚](Croatia.md) | 克罗地亚 | 2 | 克罗地亚 斯拉沃尼亚 达尔马提亚 |  |
| [科钦](https://vic3.paradoxwikis.com/Cochin) | 马拉巴尔 | 1 | 马拉巴尔的分割州 |  |
| [哥伦比亚](Colombia.md) | 昆迪纳马卡 | 3 | 昆迪纳马卡 安蒂奥基亚 考卡 瓜维亚雷 |  |
| [君士坦丁](https://vic3.paradoxwikis.com/Constantine) | 君士坦丁 | 1 | 君士坦丁 |  |
| [库奇比哈尔](https://vic3.paradoxwikis.com/Cooch_Behar) | 西孟加拉 | 1 | 西孟加拉的分割州 |  |
| [古巴](Cuba.md) | 西古巴 | 1 | 西古巴 中古巴 东古巴 |  |
| [达荷美](Dahomey.md) | 达荷美 | 1 | 达荷美 |  |
| [大南](Dai Nam.md) | 东京 | 1 | 文化故乡 |  |
| [达尔富尔](https://vic3.paradoxwikis.com/Darfur) | 达尔富尔 | 1 | 达尔富尔 |  |
| [丹麦](Denmark.md) | 西兰 | 2 | 文化故乡 |  |
| [达兰普尔](https://vic3.paradoxwikis.com/Dharampur) | 古吉拉特 | 1 | 古吉拉特的分割州 |  |
| [敦达尔](https://vic3.paradoxwikis.com/Dhundhar) | 拉杰普塔纳 | 1 | 拉杰普塔纳的分割州 |  |
| [厄瓜多尔](Ecuador.md) | 厄瓜多尔 | 1 | 厄瓜多尔 帕斯塔萨 |  |
| [埃及](Egypt.md) | 下埃及 | 3 | 文化故乡 |  |
| [虾夷地](Ezochi.md) | 虾夷 | 1 | 虾夷 |  |
| [费赞](Fezzan.md) | 费赞 | 1 | 费赞 |  |
| [芬兰](Finland.md) | 新地 | 2 | 新地 奥斯特博滕尼亚 西卡累利阿 库奥皮奥 奥卢 |  |
| [法国](France.md) | 法兰西岛 | 1 | 法兰西地区 法兰西岛 诺曼底 法属低地国家 皮卡第 普瓦图 布列塔尼 勃艮第 香槟 弗朗什-孔泰 洛林 奥尔良 曼恩-安茹 普罗旺斯 朗格多克 罗讷 阿尔萨斯-洛林 吉耶讷 奥弗涅-利穆赞 阿基坦 |  |
| [法兰克福](Frankfurt.md) | 黑森 | 1 | 黑森的分割州 |  |
| [戈贾姆](https://vic3.paradoxwikis.com/Gojjam) | 贡德尔 | 1 | 贡德尔的分割州 |  |
| [格拉-帕拉](Grão-Pará.md) | 帕拉 | 1 | 帕拉 亚马逊 阿克里 |  |
| [大不列颠](Great Britain.md) | 内伦敦 | 6 | 文化故乡 |  |
| [希腊](Greece.md) | 阿提卡 | 2 | 文化故乡 |  |
| [瓜廖尔](https://vic3.paradoxwikis.com/Gwalior) | 马尔瓦 | 1 | 以下两州的分割州：马尔瓦 拉杰普塔纳 |  |
| [海地](Haiti.md) | 海地 | 1 | 海地 |  |
| [汉堡](Hamburg.md) | 易北 | 1 | 易北的分割州 |  |
| [汉诺威](Hanover.md) | 汉诺威 | 1 | 汉诺威 |  |
| [汉志](https://vic3.paradoxwikis.com/Hedjaz) | 汉志 | 1 | 汉志 |  |
| [黑森](Hesse.md) | 黑森 | 1 | 黑森 |  |
| [黑森-卡塞尔](Hesse-Kassel.md) | 黑森 | 1 | 黑森的分割州 |  |
| [霍亨索伦](Hohenzollern.md) | 符腾堡 | 1 | 符腾堡的分割州 |  |
| [荷尔斯泰因](Holstein.md) | 石勒苏益格-荷尔斯泰因 | 1 | 石勒苏益格-荷尔斯泰因的分割州 |  |
| [匈牙利](Hungary.md) | 大匈牙利平原 | 2 | 文化故乡 |  |
| [海得拉巴](Hyderabad.md) | 海得拉巴 | 1 | 海得拉巴 |  |
| [伊达尔](https://vic3.paradoxwikis.com/Idar) | 古吉拉特 | 1 | 古吉拉特的分割州 |  |
| [印第安领地](Indian Territory.md) | 俄克拉荷马 | 1 | 俄克拉荷马 |  |
| [印多尔](https://vic3.paradoxwikis.com/Indore) | 马尔瓦 | 1 | 以下两州的分割州：马尔瓦 拉杰普塔纳 |  |
| [爱奥尼亚群岛](Ionian Islands.md) | 爱奥尼亚群岛 | 1 | 爱奥尼亚群岛 |  |
| [沙马尔](https://vic3.paradoxwikis.com/Jabal_Shammar) | 海勒 | 1 | 海勒 |  |
| [杰伊萨尔梅尔](https://vic3.paradoxwikis.com/Jaisalmer) | 拉杰普塔纳 | 1 | 拉杰普塔纳的分割州 |  |
| [占碑](https://vic3.paradoxwikis.com/Jambi) | 北苏门答腊 | 1 | 北苏门答腊的分割州 |  |
| [日本](Japan.md) | 关西 | 3 | 文化故乡 |  |
| [杰伊普尔](https://vic3.paradoxwikis.com/Jeypore) | 北萨尔卡 | 1 | 北萨尔卡的分割州 |  |
| [焦特布尔](https://vic3.paradoxwikis.com/Jodhpur) | 拉杰普塔纳 | 1 | 拉杰普塔纳的分割州 |  |
| [柔佛](https://vic3.paradoxwikis.com/Johore) | 马来亚 | 1 | 马来亚 |  |
| [朱纳格特](https://vic3.paradoxwikis.com/Junagadh) | 古吉拉特 | 1 | 古吉拉特的分割州 |  |
| [卡拉特](https://vic3.paradoxwikis.com/Kalat) | 俾路支 | 1 | 俾路支 |  |
| [考尔纳](Kaurna.md) | 南澳大利亚 | 1 | 南澳大利亚 |  |
| [卡蒂里](https://vic3.paradoxwikis.com/Kathiri) | 也门 | 1 | 也门的分割州 |  |
| [希瓦](https://vic3.paradoxwikis.com/Khiva) | 花剌子模 | 1 | 花剌子模 土库曼 |  |
| [科尔哈普尔](https://vic3.paradoxwikis.com/Kolhapur) | 孟买 | 1 | 孟买的分割州 |  |
| [浩罕](https://vic3.paradoxwikis.com/Kokand) | 费尔干纳 | 1 | 吉尔吉斯 塔吉克斯坦 |  |
| [朝鲜](Korea.md) | 京畿 | 1 | 文化故乡 |  |
| [科塔](https://vic3.paradoxwikis.com/Kotah) | 拉杰普塔纳 | 1 | 拉杰普塔纳的分割州 |  |
| [克拉科夫](Krakow.md) | 西加利西亚 | 1 | 西加利西亚的分割州 |  |
| [库尔努尔](https://vic3.paradoxwikis.com/Kurnool) | 割让区 | 1 | 割让区的分割州 |  |
| [卡奇](https://vic3.paradoxwikis.com/Kutch) | 古吉拉特 | 1 | 古吉拉特的分割州 |  |
| [拉赫季](https://vic3.paradoxwikis.com/Lahej) | 也门 | 1 | 也门的分割州 |  |
| [兰芳](Lanfang.md) | 西婆罗洲 | 1 | 西婆罗洲的分割州 |  |
| [利比里亚](Liberia.md) | 利比里亚 | 1 | 利比里亚 |  |
| [利珀](Lippe.md) | 威斯特伐利亚 | 1 | 威斯特伐利亚的分割州 |  |
| [琅勃拉邦](https://vic3.paradoxwikis.com/Luang_Prabang) | 老挝 | 1 | 老挝的分割州 |  |
| [卢卡](Lucca.md) | 艾米利亚 | 1 | 艾米利亚的分割州 |  |
| [卢森堡](Luxembourg.md) | 瓦隆 | 1 | 瓦隆的分割州 |  |
| [吕贝克](Lübeck.md) | 石勒苏益格-荷尔斯泰因 | 1 | 石勒苏益格-荷尔斯泰因的分割州 |  |
| [马达加斯加](Madagascar.md) | 北马达加斯加 | 1 | 文化故乡 |  |
| [马赫拉](https://vic3.paradoxwikis.com/Mahra) | 也门 | 1 | 也门的分割州 |  |
| [马克兰](https://vic3.paradoxwikis.com/Makran) | 俾路支 | 1 | 俾路支的分割州 |  |
| [曼尼普尔](Manipur.md) | 阿萨姆 | 1 | 阿萨姆的分割州 |  |
| [马尔瓦尔](https://vic3.paradoxwikis.com/Marwar) | 拉杰普塔纳 | 1 | 拉杰普塔纳的分割州 |  |
| [马斯卡拉](https://vic3.paradoxwikis.com/Mascara) | 奥兰 | 1 | 奥兰 |  |
| [马尤尔班杰](https://vic3.paradoxwikis.com/Mayurbhanj) | 奥里萨 | 1 | 奥里萨的分割州 |  |
| [梅克伦堡](Mecklenburg.md) | 梅克伦堡 | 1 | 梅克伦堡 |  |
| [梅克伦堡-施特雷利茨](Mecklenburg-Strelitz.md) | 梅克伦堡 | 1 | 梅克伦堡的分割州 |  |
| [梅瓦尔](https://vic3.paradoxwikis.com/Mewar) | 拉杰普塔纳 | 1 | 拉杰普塔纳的分割州 |  |
| [墨西哥](Mexico.md) | 墨西哥 | 1 | 文化故乡 |  |
| [米斯基蒂亚](Miskitia.md) | 尼加拉瓜 | 1 | 尼加拉瓜的分割州 |  |
| [摩德纳](Modena.md) | 艾米利亚 | 1 | 艾米利亚的分割州 |  |
| [摩尔达维亚](Moldavia.md) | 摩尔达维亚 | 1 | 摩尔达维亚 |  |
| [黑山](Montenegro.md) | 黑山 | 1 | 黑山 |  |
| [摩洛哥](Morocco.md) | 非斯 | 3 | 非斯 马拉喀什 里夫 内摩洛哥 |  |
| [迈索尔](https://vic3.paradoxwikis.com/Mysore) | 迈索尔 | 1 | 迈索尔 |  |
| [那格浦尔](https://vic3.paradoxwikis.com/Nagpur) | 中部省份 | 1 | 中部省份 |  |
| [纳辛格普尔](https://vic3.paradoxwikis.com/Narsinghpur) | 奥里萨 | 1 | 奥里萨的分割州 |  |
| [拿骚](Nassau.md) | 黑森 | 1 | 黑森的分割州 |  |
| [纳瓦讷格尔](https://vic3.paradoxwikis.com/Nawanagar) | 古吉拉特 | 1 | 古吉拉特的分割州 |  |
| [内志](Nejd.md) | 内志 | 1 | 内志 |  |
| [尼泊尔](Nepal.md) | 西喜马拉雅 | 1 | 西喜马拉雅 |  |
| [尼德兰](Netherlands.md) | 荷兰 | 1 | 文化故乡 |  |
| [新不伦瑞克](New Brunswick.md) | 滨海诸省 | 1 | 滨海诸省的分割州 |  |
| [挪威](Norway.md) | 东挪威 | 2 | 文化故乡 |  |
| [新斯科舍](Nova Scotia.md) | 滨海诸省 | 1 | 滨海诸省的分割州 |  |
| [奥尔登堡](Oldenburg.md) | 汉诺威 | 1 | 汉诺威的分割州 |  |
| [阿曼](Oman.md) | 阿曼 | 1 | 阿曼 |  |
| [安大略](Ontario.md) | 安大略 | 1 | 安大略 |  |
| [奥尔恰](Orchha.md) | 本德尔坎德 | 1 | 本德尔坎德的分割州 |  |
| [俄勒冈](Oregon.md) | 俄勒冈 | 1 | 俄勒冈 南哥伦比亚 爱达荷 北哥伦比亚 |  |
| [奥里萨](Orissa.md) | 奥里萨 | 1 | 奥里萨 |  |
| [帕兰普尔](https://vic3.paradoxwikis.com/Palanpur) | 古吉拉特 | 1 | 古吉拉特的分割州 |  |
| [巴拉圭](Paraguay.md) | 下巴拉圭 | 1 | 下巴拉圭 上巴拉圭 |  |
| [帕尔马](Parma.md) | 艾米利亚 | 1 | 艾米利亚的分割州 |  |
| [帕蒂亚拉](Patiala.md) | 旁遮普丘陵 | 1 | 以下两州的分割州：旁遮普丘陵 德里 |  |
| [巴特那](https://vic3.paradoxwikis.com/Patna) | 奥里萨 | 1 | 奥里萨的分割州 |  |
| [霹雳](https://vic3.paradoxwikis.com/Perak) | 马来亚 | 1 | 马来亚的分割州 |  |
| [波斯](Persia.md) | 伊拉克阿杰米 | 4 | 文化故乡 |  |
| [菲律宾](Philippines.md) | 吕宋 | 2 | 吕宋 米沙鄢 棉兰老 |  |
| [皮拉蒂尼](Piratini.md) | 南里奥格兰德 | 1 | 南里奥格兰德 | ![No](/images/thumb/0/04/No.png/24px-No.png) 苏利斯塔文化尚未被整合 |
| [坤甸](https://vic3.paradoxwikis.com/Pontianak) | 西婆罗洲 | 1 | 西婆罗洲的分割州 |  |
| [葡萄牙](Portugal.md) | 埃斯特雷马杜拉 | 1 | 文化故乡 |  |
| [普鲁士](Prussia.md) | 勃兰登堡 | 3 | 勃兰登堡 波美拉尼亚 西普鲁士 东普鲁士 下西里西亚 上西里西亚 波森 |  |
| [普杜科泰](https://vic3.paradoxwikis.com/Pudukottai) | 卡纳蒂克 | 1 | 卡纳蒂克的分割州 |  |
| [波多黎各](Puerto Rico.md) | 波尔图黎各 | 1 | 波尔图黎各 |  |
| [旁遮普](Punjab.md) | 旁遮普 | 1 | 文化故乡 |  |
| [魁北克](Quebec.md) | 魁北克 | 1 | 文化故乡 |  |
| [夸拉](https://vic3.paradoxwikis.com/Qwara) | 贡德尔 | 1 | 贡德尔的分割州 |  |
| [雷瓦](Rewah.md) | 本德尔坎德 | 1 | 本德尔坎德的分割州 |  |
| [罗马](https://vic3.paradoxwikis.com/Rome) | 拉齐奥 | 1 | 拉齐奥 |  |
| [俄罗斯](Russia.md) | 英格里亚 | 5 | 文化故乡 |  |
| [三发](https://vic3.paradoxwikis.com/Sambas) | 西婆罗洲 | 1 | 西婆罗洲的分割州 |  |
| [撒丁-皮埃蒙特](Sardinia-Piedmont.md) | 皮埃蒙特 | 2 | 皮埃蒙特 撒丁 萨伏依 |  |
| [萨塔拉](https://vic3.paradoxwikis.com/Satara) | 孟买 | 1 | 孟买的分割州 |  |
| [萨克森-科堡-哥达](https://vic3.paradoxwikis.com/Saxe-Coburg-Gotha) | 萨克森 | 1 | 萨克森的分割州 |  |
| [萨克森-迈宁根](https://vic3.paradoxwikis.com/Saxe-Meiningen) | 萨克森 | 1 | 萨克森的分割州 |  |
| [萨克森-魏玛](https://vic3.paradoxwikis.com/Saxe-Weimar) | 萨克森 | 1 | 萨克森的分割州 |  |
| [萨克森](Saxony.md) | 萨克森 | 1 | 萨克森 |  |
| [绍姆堡-利珀](Schaumburg-Lippe.md) | 威斯特伐利亚 | 1 | 威斯特伐利亚的分割州 |  |
| [石勒苏益格](Schleswig.md) | 石勒苏益格-荷尔斯泰因 | 1 | 石勒苏益格-荷尔斯泰因的分割州 |  |
| [施瓦茨堡](https://vic3.paradoxwikis.com/Schwarzburg) | 萨克森 | 1 | 萨克森的分割州 |  |
| [雪兰莪](https://vic3.paradoxwikis.com/Selangor) | 马来亚 | 1 | 马来亚的分割州 |  |
| [塞尔维亚](Serbia.md) | 西塞尔维亚 | 1 | 西塞尔维亚 东塞尔维亚 黑山 科索沃 |  |
| [锡亚克](https://vic3.paradoxwikis.com/Siak) | 北苏门答腊 | 1 | 北苏门答腊的分割州 |  |
| [暹罗](Siam.md) | 曼谷 | 1 | 文化故乡 |  |
| [锡金](Sikkim.md) | 东喜马拉雅 | 1 | 东喜马拉雅的分割州 |  |
| [信德](Sindh.md) | 信德 | 1 | 信德 |  |
| [新当](https://vic3.paradoxwikis.com/Sintang) | 西婆罗洲 | 1 | 西婆罗洲的分割州 |  |
| [南非](South Africa.md) | 开普殖民地 | 1 | 开普殖民地 北开普 东开普 |  |
| [西班牙](Spain.md) | 新卡斯蒂利亚 | 2 | 文化故乡 |  |
| [苏禄](Sulu.md) | 棉兰老 | 1 | 棉兰老的分割州 |  |
| [梭罗](https://vic3.paradoxwikis.com/Surakarta) | 中爪哇 | 1 | 中爪哇的分割州 |  |
| [苏尔古贾](Surguja.md) | 本德尔坎德 | 1 | 本德尔坎德的分割州 |  |
| [瑞典](Sweden.md) | 斯韦阿兰 | 2 | 斯韦阿兰 约塔兰 斯科讷 诺尔兰 |  |
| [瑞士](Switzerland.md) | 西瑞士 | 1 | 西瑞士 东瑞士 |  |
| [得克萨斯](Texas.md) | 得克萨斯 | 1 | 得克萨斯 |  |
| [西藏](Tibet.md) | 拉萨 | 1 | 文化故乡 |  |
| [蒂多雷](https://vic3.paradoxwikis.com/Tidore) | 摩鹿加 | 1 | 摩鹿加 |  |
| [提格雷](https://vic3.paradoxwikis.com/Tigray) | 贡德尔 | 1 | 贡德尔的分割州 |  |
| [特兰西瓦尼亚](Transylvania.md) | 南特兰西瓦尼亚 | 1 | 南特兰西瓦尼亚 北特兰西瓦尼亚 |  |
| [特拉凡哥尔](https://vic3.paradoxwikis.com/Travancore) | 特拉凡哥尔 | 1 | 特拉凡哥尔 |  |
| [的黎波里塔尼亚](Tripolitania.md) | 的黎波里 | 1 | 的黎波里 |  |
| [特鲁西尔诸国](Trucial States.md) | 特鲁西尔海岸 | 1 | 特鲁西尔海岸 |  |
| [突尼斯](Tunis.md) | 突尼斯 | 1 | 突尼斯 |  |
| [土耳其](https://vic3.paradoxwikis.com/Turkey) | 东色雷斯 | 5 | 文化故乡 |  |
| [托斯卡纳](Tuscany.md) | 托斯卡纳 | 1 | 托斯卡纳 |  |
| [两西西里](Two Sicilies.md) | 坎帕尼亚 | 1 | 西西里 |  |
| [波罗的海联合省](United Baltic Provinces.md) | 南利沃尼亚 | 3 | 考纳斯 维尔纽斯 雷瓦尔 北利沃尼亚 南利沃尼亚 库尔兰 | 已研究泛民族主义 |
| [乌拉圭](Uruguay.md) | 乌拉圭 | 1 | 乌拉圭 |  |
| [委内瑞拉](Venezuela.md) | 米兰达 | 1 | 米兰达 玻利瓦尔 苏利亚 |  |
| [瓦达伊](Wadai.md) | 瓦达伊 | 1 | 瓦达伊 乍得 |  |
| [瓦尔代克](Waldeck.md) | 黑森 | 1 | 黑森的分割州 |  |
| [瓦拉几亚](Wallachia.md) | 瓦拉几亚 | 1 | 瓦拉几亚 |  |
| [符腾堡](Württemberg.md) | 符腾堡 | 1 | 符腾堡的分割州 |  |
| [日惹](https://vic3.paradoxwikis.com/Yogyakarta) | 中爪哇 | 1 | 中爪哇的分割州 |  |
### 事件国家

以下国家只能通过[事件](https://vic3.paradoxwikis.com/Event)出现。

| 国家 | 事件 | 备注 |
|---|---|---|
| [阿布哈兹](Abkhazia.md) | *高加索的大灾难* | 由[俄罗斯](Russia.md)日志条目*高加索战争*触发 |
| [自由邦](Free State.md) | *[自由邦]* | 由通用日志条目*自由邦问题*触发 |
| [天国](Heavenly Kingdom.md) | *天国* | 由[中国](China.md)日志条目*天国*触发 |
| [印度斯坦](https://vic3.paradoxwikis.com/Indusstan) | *建立印度邦联* | [印度](East India.md)日志条目*社群分裂*的按钮 |
| [林堡](https://vic3.paradoxwikis.com/Limburg) | *伦敦会议落幕* | 由[荷兰](Netherlands.md)日志条目*伦敦会议*触发 |
| [巴黎公社](https://vic3.paradoxwikis.com/Paris_Commune) | *巴黎公社* | 由[法国](France.md)日志条目*巴黎公社*触发 |
| [桑给巴尔](Zanzibar.md) | *桑给巴尔的崛起！* | 由[阿曼](Oman.md)日志条目*分裂的阿曼*触发 |

#### 土邦

|  | 仅在启用[帝国之枢](Pivot of Empire.md) DLC 时可用。 |
|---|---|

许多土邦只能通过事件被释放。这些事件也可能释放开局即存在或可通过其他方式出现的国家。

| *俾路支事务* |  |
|---|---|
| [卡拉特](https://vic3.paradoxwikis.com/Kalat) | 开局即存在 |
| [马克兰](https://vic3.paradoxwikis.com/Makran) |  |
| [哈兰](https://vic3.paradoxwikis.com/Kharan) | 仅通过此事件 |
| [拉斯贝拉](https://vic3.paradoxwikis.com/Las_Bela) |  |

| *攻占信德* |  |
|---|---|
| [海尔布尔](https://vic3.paradoxwikis.com/Khairpur) | 仅通过此事件 |
| [信德](Sindh.md) | 开局即存在 |

| *西北边境* |  |
|---|---|
| [奇特拉尔](Chitral.md) | 开局即存在 |
| [迪尔](https://vic3.paradoxwikis.com/Dir) | 仅通过此事件 |
| [斯瓦特](https://vic3.paradoxwikis.com/Swat) |  |

| *阿姆利则条约* |  |
|---|---|
| [克什米尔](Kashmir.md) | 开局即存在 |

| *掸邦* |  |
|---|---|
| [掸](Shan.md) | 开局即存在 |

## 参考

1. ↑ 释放与释放者同等级的国家通常会立即打破附属条约，而不是降低被释放国家的等级。
2. ↑ 该事件也会在日志条目完成时触发，这确保了玩家操控的俄罗斯始终能够切换游玩保加利亚

- 可释放国家定义于 /Victoria 3/game/common/country_creation/00_releasable_countries.txt
- 释放时的 on_action 定义于 /Victoria 3/game/common/on_actions/00_code_on_actions.txt