---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Agitator
source: https://vic3.paradoxwikis.com/Agitator
pageid: 4994
categories: [1.13, Expand, Game_concepts, Lists]
fetched: 2026-10-27
---
本文已针对当前游戏[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

另见：
人物

**鼓动家**（Agitators）是身处正式政治舞台与行政体系之外的人物，他们支持与其[意识形态](Character ideology.md)或[利益集团](Interest group.md)一致的[政治运动](Political movement.md)，并提升这些运动对人口的吸引力。

## 鼓动家机制

| 来源 | 数量 |
|---|---|
| 基础 | **+1** |
| 主要政权或更高排名 | **+1** |
| Labor Movement | **+1** |
| Political Agitation | **+1** |
| Mass Propaganda | **+1** |

每个国家同一时间只能支持一定数量的鼓动家。所有国家的基础 *鼓动家席位* 为 1，每解锁一项以下技术即增加 1：Labor Movement、Political Agitation 和 Mass Propaganda。列强、主要政权与未受认可的主要政权额外拥有一个席位。

当一个国家有空余的鼓动家席位时，它可以邀请一位被流放的鼓动家，也可能随机生成新的鼓动家。某些事件和日志条目也能生成鼓动家。新鼓动家生成的概率取决于国家的全国识字率，识字率越高概率越大。[1] 例如，一个全国识字率为 50% 的国家大约每 7 年可期望生成一位新鼓动家。拥有更多空余席位并不会提高新鼓动家生成的概率。

当鼓动家出现在某个国家或被邀请到某个国家时，他们会加入与其[意识形态](Character ideology.md)或[利益集团](Interest group.md)相符的[政治运动](Political movement.md)。鼓动家为运动的吸引力增加 15 加上其声望（无论正负）乘以 0.15 的数值。如果鼓动家的政治运动解散，鼓动家将加入一个新的政治运动。如果鼓动家在当前国家无法支持任何政治运动，他们将被流放或退休。

随机生成的鼓动家通常持有与该国法律相对立的意识形态。他们也更常隶属于更具民粹色彩的利益集团，即小资产阶级、乡村民众和工会。鼓动家基于各政治运动的脚本因素加入其中。这通常意味着他们会加入与自己意识形态最契合的运动，但偶尔也会加入其他运动。

## 鼓动家互动

鼓动家拥有若干特殊的人物互动。特别是，在启用 Voice of the People DLC 时，鼓动家可以被任命为将军，或被提升为其所属利益集团的领袖。

| 互动 | 角色 | 条件 | 效果 |
|---|---|---|---|
| 流放异见者 |  | 国家没有 Protected Speech 或 Guaranteed Liberties 如果人物是鼓动家，其政治运动不是革命性的；否则，人物所属利益集团不在政府中、未被边缘化或不是革命性的 人物的意识形态与统治者的意识形态不过于相似 过去 5 年内未对任何人物使用过此互动 | 人物成为鼓动家并失去所有其他角色 为人物所属利益集团增加 2% 至 7% 的激进派 人物被流放 如果人物原为利益集团领袖，该利益集团获得“被流放的领袖” 被流放的领袖 利益集团 modifier：5 年内 −5 利益集团支持度（逐渐衰减） |
| 邀请流亡者 |  | 国家有空余的鼓动家席位 国家没有 Closed Borders 如果人物支持虔信派，或国家有 State Religion（无变体），人物的宗教与该国国教一致 人物声望超过 15 人物至少具有公开偏见地位 人物必须能够加入一个政治运动 过去 5 年内未对任何人物使用过此互动 | 人物加入该国 人物加入或发起一场政治运动 人物在 5 年内免疫随机死亡 与人物的母国产生外交事端 |
| 遣返鼓动家 |  | 人物没有其他角色 国家与人物的母国处于对抗关系 人物的母国存在且有空余的鼓动家席位 人物在其母国能够加入或发起一场政治运动 过去 2.5 年内未对任何人物使用过此互动 | 人物返回母国 |
| 监禁鼓动家 |  | 启用 Pivot of Empire 国家没有 Guaranteed Liberties 过去 2.5 年内未对任何人物使用过此互动 | 人物被监禁 3、5 或 10 年 |
| 资助 |  | 启用 Pivot of Empire 人物不是继承人 人物此前未被资助或排斥过 人物的意识形态与统治者的意识形态差异不过大 当前被资助的其他人物少于 3 名 | 人物获得一个提升其声望的 modifier，如果是政客，则同时提升其利益集团的支持度，效果随花费的权威力而增强 10% 概率获得特质 Expensive Tastes |
| 排斥 |  | 启用 Pivot of Empire 人物不是继承人 人物此前未被资助或排斥过 人物的意识形态与统治者的意识形态不过于相似 当前被排斥的其他人物少于 3 名 | 人物获得一个降低其声望的 modifier，如果是政客，则同时降低其利益集团的支持度，效果随花费的权威力而增强 10% 概率获得特质 Wrathful |
| 授予贵族爵位 |  | 启用 Pivot of Empire 国家为君主制 人物尚不是贵族、不是统治者或继承人 人物的意识形态与统治者的意识形态差异不过大 | 人物成为贵族 如果人物所属利益集团不反对君主制，该集团获得支持度加成 |
| 令大名退休 |  | 国家为幕府体制的日本 人物是大名 人物的忠诚度不是中立或更高 在设定的冷却时间内未使用过此互动 | 人物退休 人物领地下的一个随机州产生激进派 |
| Voice of the People 独占行动 |  |  |  |
| 授予领导权 |  | 人物所属利益集团在政府中 人物支持一个向其利益集团施压的政治运动 如果国家有 State Atheism，人物是无神论者或拥有二等公民地位或更好 否则，如果国家有 Multiculturalism 和 Total Separation，人物拥有公开偏见地位或更好 否则，人物拥有二等公民地位或更好 人物为男性，或已颁布 Women's Suffrage 过去 5 年内未对任何人物使用过此互动 | 人物失去鼓动家角色并成为其利益集团的领袖 |
| 授予指挥权 |  | 人物不是指挥官 人物是成年男性 过去 5 年内未对任何人物使用过此互动 | 为人物增加将军角色 |

## 历史鼓动家

|  | 请通过[扩充](https://vic3.paradoxwikis.com/index.php?title=Agitator&action=edit)以下内容来帮助改进本文或本节：更多历史鼓动家。 |
|---|---|

历史鼓动家通常是[DLC](https://vic3.paradoxwikis.com/DLC)独占内容，例如 Voice of the People 沉浸包；否则，鼓动家将随机生成。许多历史鼓动家通过与他们的事业相关的事件或日志条目产生，并锁定于特定国家或特定主流文化。

| 姓名 | 国家 | 利益集团 | 意识形态 | 特质 | 条件 | DLC |
|---|---|---|---|---|---|---|
| Frederick Douglass（非裔美国 新教） | 以下任一：America、Confederate States of America、New Africa | 以下任一：知识分子、乡村民众 | 废奴主义者 | Firebrand、Imposing、Persistent | 日期在 1840 至 1877 之间，知识分子与乡村民众并非都被边缘化，没有 Slavery Banned |  |
| Harriet Tubman（非裔美国 新教） | 以下任一：America、Confederate States of America、New Africa | 以下任一：福音派、知识分子 | 废奴主义者 | Brave、Charismatic、Direct | 日期在 1849 至 1896 之间 没有 Slavery Banned 福音派与知识分子并非都被边缘化 |  |
| Susan Anthony（扬基 新教） | 以下任一：America、New England | 以下任一：知识分子、小资产阶级 | 女权主义者 | Persistent、Demagogue、Honorable | 日期在 1851 至 1900 之间 知识分子与小资产阶级并非都被边缘化 |  |
| Eugene Debs（扬基 新教） | [America](America.md) | 工会 | 社会民主党人 | Demagogue、Charismatic、Honorable | 日期在 1893 至 1921 之间 工会未被边缘化 |  |
| William Du Bois（非裔美国 新教） | 以下任一：America、New England | 知识分子 | 社会民主党人 | Erudite、Literary、Charismatic | 日期在 1894 之后 知识分子未被边缘化 |  |
| Henry Ford（扬基 新教） | 以下任一：America、Free States of America、Michigan | 实业家 | 民族主义者 | Bigoted、Ambitious、Experienced Entrepreneur | 日期在 1908 之后 实业家未被边缘化 |  |
| John Brown（扬基 新教） | [America](America.md) | 福音派 | 废奴主义者 | Reserved、Firebrand、Reckless、This Glorious Endeavor [2] | 1840 至 1870 之间，没有美国内战，没有 Fugitive Slaves、Wilmot Proviso 或 Bleeding Kansas 变量 没有 Slavery Banned |  |
| Joshua Norton（英格兰 新教） | [America](America.md) | 小资产阶级 | 开明保皇派 | Charismatic、Honorable、Ambitious、The Spirit of San Francisco [2] | 1860 至 1880 之间 California 是已整合州 |  |
| Benjamin Tucker（扬基 新教） | [America](America.md) | 知识分子 | 虚无主义者 | Charismatic、Persistent | 在 1876 至 1930 之间激活“虚无主义运动”日志条目 |  |
| Vladimir Lenin（俄罗斯 无神论） | [Russia](Russia.md) | 工会 | 先锋队主义者 | Firebrand、Charismatic、Reckless、The Man from the River Lena [2] | 日期在 1890 之后，有 Political Agitation，没有 Council Republic 工会支持度为负且未被边缘化 |  |
| Leon Trotsky（阿什肯纳兹 无神论） | [Russia](Russia.md) | 军队 | 先锋队主义者 | Innovative、Charismatic、Persistent | 日期在 1898 至 1917 之间，有 Socialism，没有 Council Republic，任意乌克兰本土动荡超过 25% |  |
| Pyotr Kropotkin（俄罗斯 无神论） | [Russia](Russia.md) | 工会 | 无政府主义者 | Direct、Inspirational Orator | 日期在 1872 至 1917 之间，有 Anarchism，没有 Council Republic，工会未被边缘化 |  |
| Mikhail Bakunin（俄罗斯 无神论） | [Russia](Russia.md) | 工会 | 无政府主义者 | Firebrand、Persistent、Bigoted | 日期在 1863 至 1880 之间，有 Anarchism，没有 Council Republic 工会未被边缘化 |  |
| Nestor Makhno（乌克兰 无神论） | 以下任一：Russia、Ukraine | 乡村民众 | 无政府主义者 | Social Bandit、Imposing Celebrity Commander | 日期在 1910 之后 工会与乡村民众并非都被边缘化 |  |
| Aleksei Aladin（俄罗斯 东正教） | [Russia](Russia.md) | 乡村民众 | 社会民主党人 | C、Cautious、Inspirational Orator、Diplomat | 1892 至 1927 之间 乡村民众未被边缘化 |  |
| Maxim Gorky（俄罗斯 东正教） | [Russia](Russia.md) | 知识分子 | 共产主义者 | Bigoted、Literary、Charismatic | 日期在 1899 至 1921 之间 知识分子未被边缘化 |  |
| Dmitry Pisarev（俄罗斯 无神论） | 以下任一：Russia、Ukraine | 知识分子 | 虚无主义者 | Psychological Affliction、Literary、Inspirational Orator | 日期在 1858 之后 知识分子与工会并非都被边缘化 |  |
| Jarosław Dąbrowski（波兰 天主教） | 以下任一：Russia、Poland、Ukraine | 军队 | 激进主义者 | Persistent、Brave、Mountain Combat Expert | 日期在 1862 至 1896 之间，拥有 Volhynia 州，没有 Council Republic |  |
| Rosa Luxemburg（波兰 无神论） | 以下任一：Russia、Poland | 工会 | 共产主义者 | Firebrand、Brave、Romantic、Untamed Revolutionary [2] | 日期在 1889 之后，拥有 Lesser Poland 州，有 Socialism，没有 Council Republic |  |
| Varfolomey Zaitsev（俄罗斯 东正教） | Russia | 知识分子 | 虚无主义者 | Firebrand、Arrogant | 在 1862 至 1882 之间激活“虚无主义运动”日志条目 |  |
| Sergei Nechaev（俄罗斯 无神论） | [Russia](Russia.md) | 知识分子 | 虚无主义者 | Direct、Persistent、Demagogue | 日期在 1868 至 1880 之间 |  |
| Alexey Borovoy（俄罗斯 无神论） | [Russia](Russia.md) | 知识分子 | 虚无主义者 | Erudite、Brave、Inspirational Orator | 日期在 1899 之后 |  |
| Alexey Solonovich（俄罗斯 泛灵论）[3] | [Russia](Russia.md) | 知识分子 | 无政府主义者 | Literary、Inspirational Orator | 日期在 1909 之后 有 Anarchism |  |
| Olha Taratuta（乌克兰 无神论） | [Russia](Russia.md) | 工会 | 无政府主义者 | Brave、Ambitious | 日期在 1897 之后 有 Anarchism |  |
| Alexandra Kollontai（俄罗斯 无神论） | [Russia](Russia.md) | 工会 | 人道主义者 | Reckless、Firebrand、Basic Diplomat | 日期在 1899 之后 有 Feminism |  |
| Nikolai Tchaikovsky（俄罗斯 东正教） | [Russia](Russia.md) | 乡村民众 | 激进主义者 | Pious、Experienced Diplomat、Ambitious | 日期在 1872 至 1917 之间 |  |
| Pierre-Joseph Proudhon（法国 无神论） | [France](France.md) | 以下任一：知识分子、工会 | 无政府主义者 | Erudite、Ambitious、Persistent、Diplomat | 日期在 1840 至 1865 之间 有 Anarchism |  |
| Victor Hugo（法国 国教） | [France](France.md) | 知识分子 | 废奴主义者 | Direct、Brave、Literary | 日期在 1885 之前 有 Autocracy |  |
| Louis Charles Delescluze（法国 国教） | [France](France.md) | 工会 | 以下之一：激进主义者、共产主义者 | Literary、Inspirational Orator、Brave | 日期 1840 至 1880 没有 Council Republic |  |
| Louis Blanqui（法国 无神论） | [France](France.md) | 知识分子 | 以下之一：激进主义者、共产主义者 | Direct、Political Operator、Ambitious、Professional Revolutionary [2] | 日期 1840 至 1880，有 Egalitarianism，没有 Council Republic |  |
| Louis-Napoleon Bonaparte（法国 国教） | [France](France.md) | 小资产阶级 | 波拿巴主义者 | Ambitious、Charismatic、Demagogue、Experienced Political Operator、Napoleonic Return [2] |  |  |
| Charles Maurras（法国 国教） | [France](France.md) | 小资产阶级 | 以下任一：正统派、整体主义者、传统主义者 | Reserved、Reckless、Firebrand、Reactionary Icon [2] | 1894 之后 以下任一：有日志条目 The Dreyfus Affair、已完成日志条目 The Dreyfus Affair、有 Political Agitation |  |
| Louise Michel（法国 天主教） | [France](France.md) | 知识分子 | 女权主义者 | Brave、Firebrand、Persistent | 日期在 1869 至 1890 之间 知识分子与工会并非都被边缘化 |  |
| Georges Sorel（法国 无神论） | [France](France.md) | 知识分子 | 虚无主义者 | Erudite、Innovative Engineer、Passionate Theorist [2] | 日期 1905 至 1922，有 Socialism，有 Philosophical Pragmatism |  |
| Georges Boulanger（法国 天主教） | [France](France.md) | 军队 | 民族主义者 | Demagogue、Innovative、Romantic、Général Revanche | 日期 1880 至 1895 未拥有所有法国本土 有 Political Agitation |  |
| Jean Jaurès（法国 天主教） | 以下任一：France、Occitania | 知识分子 | 社会民主党人 | Firebrand、Erudite、Expert Political Operator | 1892 之后 工会与知识分子并非都被边缘化 |  |
| Alexis de Tocqueville（法国 天主教） | [France](France.md) | 地主 | 改革者 | Literary、Honorable、Political Operator | 日期在 1852 之前 地主与知识分子并非都被边缘化 |  |
| François-René de La Tour du Pin Chambly（法国 天主教） | [France](France.md) | 地主 | 正统派 | Celebrity Commander、Pious、Erudite | 日期在 1870 至 1900 之间 地主与军队并非都被边缘化 |  |
| Giuseppe Mazzini（北意大利 天主教） | [Sardinia-Piedmont](Sardinia-Piedmont.md) | 知识分子 | 激进主义者 | Firebrand、Persistent、Diplomat、Popular Radical [2] |  |  |
| Errico Malatesta（南意大利 无神论） | 以下任一：Italy、Two Sicilies | 工会 | 无政府主义者 | Persistent、Charismatic、Inspirational Orator | 日期 1872 至 1900 知识分子与工会并非都被边缘化 |  |
| Giovanni Gentile（南意大利 天主教） | 以下任一：Italy、Two Sicilies | 小资产阶级 | 法西斯主义者 | Literary、Charismatic、Erudite | 日期在 1922 之后 小资产阶级与知识分子并非都被边缘化 |  |
| Francesco Crispi（南意大利 天主教） | 以下任一：Italy、Two Sicilies | 小资产阶级 | 激进主义者 | Imperious、Ambitious、Experienced Diplomat | 日期在 1847 至 1893 之间 小资产阶级、知识分子与乡村民众并非都被边缘化 |  |
| Gabriele D'Annunzio（南意大利 天主教） | 以下任一：Italy、Two Sicilies | 小资产阶级 | 法西斯主义者 | Hedonist、Literary、Ambitious | 1899 至 1924 之间 地主、小资产阶级与知识分子并非都被边缘化 |  |
| Karl Heinrich Marx[4]（阿什肯纳兹 无神论） | 任意欧洲国家 | 工会 | 共产主义者 | Literary、Direct、Persistent | 有 Socialism |  |
| Max Stirner（南德意志 无神论） | 任意北德意志或南德意志国家（优先玩家） | 知识分子 | 虚无主义者 | Reserved | 在 1844 至 1866 之间激活“虚无主义运动”日志条目 |  |
| Ferdinand Lassalle（北德意志 新教） | 以下任一：Prussia、Germany | 小资产阶级 | 社会民主党人 | Inspirational Orator、Arrogant、Ambitious、Agent of the Sovereign | 日期 1848 至 1885 有 Dialectics 没有 Council Republic |  |
| Ernst Röhm（南德意志 新教） | 以下任一：Bavaria、South German Federation、Germany、Bolivia | 军队 | 法西斯主义者 | Ambitious、Bigoted、Direct | 日期在 1917 之后 军队与小资产阶级并非都被边缘化 |  |
| Alfred Hugenberg（北德意志 新教） | 以下任一：Hanover、North German Federation、Germany | 小资产阶级 | 法西斯主义者 | Direct、Literary、Master Bureaucrat | 日期在 1916 之后 小资产阶级未被边缘化 |  |
| Ludwik Mieroslawski（波兰 天主教） | Poland（若存在），否则为以下任一：Prussia、Germany、Russia | 小资产阶级 | 激进主义者 | Celebrity Commander、Inspirational Orator、Literary | 日期在 1871 之前 小资产阶级未被边缘化 |  |
| Albert Einstein（阿什肯纳兹 犹太教） | 以下任一：Prussia、Germany | 知识分子 | 乌托邦主义者 | Innovative、Ambitious、Literary | 日期在 1905.1.1 至 1955.4.18 之间 知识分子未被边缘化 |  |
| Karl Liebknecht（北德意志 新教） | 以下任一：Saxony、North German Federation、Germany | 知识分子 | 共产主义者 | Erudite、Experienced Political Operator、Charismatic | 日期在 1899 之后 知识分子与工会并非都被边缘化 |  |
| Florence Nightingale（英格兰 新教） | [Great Britain](Great Britain.md) | 知识分子 | 人道主义者 | Literary、Aesthete、Erudite、Nightingale Pledge [2] | 于 1850 年在[Great Britain](Great Britain.md)被创建并被流放 |  |
| Charles Dickens（英格兰 新教） | [Great Britain](Great Britain.md) | 知识分子 | 改革者 | Cautious、Literary、Persistent | 日期在 1870 之前 |  |
| John Stuart Mill（英格兰 新教） | 以下任一：Great Britain、England | 知识分子 | 功利主义者 | Erudite、Ambitious、Persistent | 日期在 1843 至 1865 之间 知识分子未被边缘化 |  |
| Emmeline Pankhurst（英格兰 新教） | [Great Britain](Great Britain.md) | 小资产阶级 | 女权主义者 | Persistent、Firebrand | 日期 1880 至 1928 有 Feminism 没有 Women's Suffrage |  |
| William Smith O'Brien（爱尔兰 新教） | 以下任一：Great Britain、Ireland | 小资产阶级 | 激进主义者 | Inspirational Orator、Direct、Persistent | 日期在 1856 之前 小资产阶级、知识分子与乡村民众并非都被边缘化 |  |
| Ada Lovelace（英格兰 新教） | Great Britain | 知识分子 | 温和主义者 | Romantic、Innovative、Literary、Cancer | 日期在 1840.1.1 至 1852.11.27 之间 知识分子未被边缘化 |  |
| George Holyoake（英格兰 新教） | Great Britain | 知识分子 | 虚无主义者 | Tactful | 在 1846 至 1906 之间激活“虚无主义运动”日志条目 |  |
| John Leno（英格兰 新教） | [Great Britain](Great Britain.md) | 工会 | 激进主义者 | Brave、Charismatic、Wrathful | 日期在 1848 至 1880 之间 工会未被边缘化 |  |
| Arthur Cook（英格兰 新教） | [Great Britain](Great Britain.md) | 工会 | 共产主义者 | Brave、Innovative、Inspirational Orator | 日期在 1910 至 1925 之间 有 Political Agitation 工会未被边缘化 |  |
| Albert Inkpin（英格兰 无神论） | [Great Britain](Great Britain.md) | 工会 | 先锋队主义者 | Inspirational Orator、Political Operator、Meticulous | 日期在 1910 至 1925 之间 有 Political Agitation 工会未被边缘化 |  |
| Friedrich Engels（北德意志 无神论） | [Great Britain](Great Britain.md) | 知识分子 | 共产主义者 | Literary、Hedonist、Charismatic | 日期在 1850 至 1890 之间 有 Socialism 知识分子未被边缘化 |  |
| Rotha Lintorn-Orman（英格兰 新教） | [Great Britain](Great Britain.md) | 小资产阶级 | 法西斯主义者 | Hedonist、Alcoholic、Demagogue | 日期在 1923 至 1933 年末之间 有 Political Agitation 小资产阶级未被边缘化 |  |
| Charles Scott（英格兰 新教） | [Great Britain](Great Britain.md) | 知识分子 | 改革者 | Literary、Meticulous、Basic Diplomat | 日期在 1872 至 1920 之间 知识分子未被边缘化 |  |
| Annie Besant（英格兰 印度教） | [Great Britain](Great Britain.md) | 知识分子 | 人道主义者 | Persistent、Firebrand | 日期在 1888 至 1933 之间 拥有 Home Counties 州 |  |
| Francesc Pi i Margall（加泰罗尼亚 天主教） | 以下任一：Spain、Catalonia | 小资产阶级 | 激进主义者 | Literary、Inspirational Orator、Direct | 日期在 1854 至 1893 之间 小资产阶级与知识分子并非都被边缘化 |  |
| Manuel Ruiz Zorrilla（西班牙 天主教） | [Spain](Spain.md) | 小资产阶级 | 激进主义者 | Ambitious、Political Operator、Persistent | 日期在 1866 至 1884 之间 小资产阶级与知识分子并非都被边缘化 |  |
| Juan Donoso Cortés（西班牙 天主教） | 以下任一：Spain、任何以西班牙文化为主流文化的其他国家 | 地主 | 传统主义者 | Basic Diplomat、Erudite、Pious | 日期在 1840 至 1853 之间 地主未被边缘化 |  |
| António Sardinha（葡萄牙 天主教） | [Portugal](Portugal.md) | 知识分子 | 法西斯主义者 | Direct、Bigoted、Ambitious | 日期在 1910 之后 小资产阶级与知识分子并非都被边缘化 |  |
| Sigmund Freud（阿什肯纳兹 犹太教） | 任意欧洲国家（非欧洲国家获得一个拥有相同利益集团、意识形态和特质的犹太人物） | 知识分子 | 虚无主义者 | Ambitious、Charismatic、Cocaine Addict | 已研究 Psychoanalysis 拥有一座 5 级或更高的大学，且其哲学系或分析哲学系生产方式处于激活状态 有空余的鼓动家席位 |  |
| Josef Peukert（南德意志 天主教） | [Austria](Austria.md) | 工会 | 无政府主义者 | Reckless、Wrathful、Firebrand | 日期在 1880 年 1 月 1 日至 1910 年 3 月 3 日之间 |  |
| Kossuth Lajos（匈牙利 新教） | Hungary（若存在），否则为 Austria | 小资产阶级 | 激进主义者 | Charismatic、Demagogue、Imperious | 日期在 1867 之前 小资产阶级未被边缘化 |  |
| Petőfi Sándor（匈牙利 新教） | [Hungary](Hungary.md) | 知识分子 | 激进主义者 | Literary、Romantic、Inspirational Orator | 日期在 1847 至 1860 之间 知识分子与小资产阶级并非都被边缘化 |  |
| Mihály Károlyi（南德意志 天主教） | [Hungary](Hungary.md) | 工会 | 激进主义者 | Reckless、Wrathful、Firebrand | 日期在 1899 之后 |  |
| Henrik Ibsen（挪威 新教） | Norway，或若 Norway 不存在，则拥有东西挪威的斯堪的纳维亚国家 | 知识分子 | 无政府主义者 | Romantic、Innovative、Literary | 日期在 1862 至 1906 之间 知识分子未被边缘化 |  |
| Bjornstjerne Bjornson（挪威 新教） | 以下任一：Norway、Scandinavia | 知识分子 | 激进主义者 | Literary、Inspirational Orator、Cautious | 日期在 1857 至 1894 之间 小资产阶级与知识分子并非都被边缘化 |  |
| 奥拉·雷曼（Orla Lehmann）丹麦人 新教 | 以下任一：丹麦 斯堪的纳维亚 | 小资产阶级 | 激进派 | 文学 煽动家 富有魅力 | 日期在 1863 年之前 小资产阶级、知识分子和乡村民众并非全部边缘化 |  |
| 维戈·霍鲁普（Viggo Horup）丹麦人 新教 | 以下任一：丹麦 斯堪的纳维亚 | 小资产阶级 | 激进派 | 文学 政治操盘手 富有魅力 | 日期在 1876 至 1900 年之间 小资产阶级和知识分子并非两者都边缘化 |  |
| 格奥尔格·勃兰兑斯（Georg Brandes）丹麦人 犹太教 | 以下任一：丹麦 斯堪的纳维亚 | 小资产阶级 | 激进派 | 博学 鼓舞人心的演说家 雄心勃勃 | 日期在 1871 至 1900 年之间 小资产阶级和知识分子并非两者都边缘化 |  |
| 亚历山德鲁·博格丹-皮泰什蒂（Alexandru Bogdan-Pitesti）罗马尼亚人 天主教 | 以下任一：罗马尼亚 瓦拉几亚 | 知识分子 | 无政府主义者 | 文学 富有魅力 享乐主义者 | 日期在 1894 至 1918 年之间 知识分子未边缘化 |  |
| 伊翁·德拉古米斯（Ion Dragoumis）希腊人 东正教 | [希腊](Greece.md) | 地主 | 法西斯主义者 | 资深外交官 文学 雄心勃勃 | 日期在 1907 年之后 地主和小资产阶级并非两者都边缘化 |  |
| 埃米利亚诺·萨帕塔（Emilano Zapata）墨西哥人 天主教 | [墨西哥](Mexico.md) | 乡村民众 | 无政府主义者 | 光荣 直率 名将 | 日期在 1909 年之后 工会和乡村民众并非两者都边缘化 |  |
| 弗朗西斯科·马德罗（Francisco Madero）墨西哥人 天主教 | [墨西哥](Mexico.md) | 小资产阶级 | 市场自由主义者 | 光荣 富有魅力 外交官 | 日期在 1903 年之后 知识分子和小资产阶级并非两者都边缘化 |  |
| 胡安·拉瓦列（Juan Lavalle）拉普拉塔人 天主教 | [阿根廷](Argentina.md) | 地主 | 威权主义者 | 威严 光荣 广受欢迎的指挥官 | 初始位于流亡鼓动家池中 |  |
| 胡安·包蒂斯塔·阿尔贝迪（Juan Bautista Alberdi）主流文化 天主教 | 以下任一：阿根廷 拉普拉塔 | 知识分子 | 激进派 | 博学 勇敢 文学 | 日期在 1837 至 1880 年之间 知识分子未边缘化 |  |
| 胡安·包蒂斯塔·拜罗莱托（Juan Bautista Bairoletto）主流文化 天主教 | 以下任一：阿根廷 拉普拉塔 | 乡村民众 | 无政府主义者 | 社会侠盗 富有魅力 勇敢 | 日期在 1920 年之后 乡村民众未边缘化 |  |
| 弗吉尼亚·博尔滕（Virginia Bolten）主流文化 无神论者 | 以下任一：阿根廷 拉普拉塔 | 工会 | 人道主义者 | 煽动家 坚韧 勇敢 | 日期在 1900 年之后 工会未边缘化 |  |
| 何塞·马蒂（José Martí）加勒比人 天主教 | [古巴](Cuba.md) | 知识分子 | 主权主义者 | 一丝不苟 文学 煽动家 |  |  |
| 卡洛斯·曼努埃尔·德·塞斯佩德斯（Carlos Manuel de Cespedes）加勒比人 天主教 | [古巴](Cuba.md) | 地主 | 废奴主义者 | 社会侠盗 光荣 博学 |  |  |
| 安东尼奥·马塞奥（Antonio Maceo）非洲裔加勒比人 天主教 | [古巴](Cuba.md) | 乡村民众 | 主权主义者 | 坚韧 勇敢 光荣 社会侠盗 | 在 1868 年 10 月 10 日至 1895 年 1 月 1 日之间 古巴是独立倾向高于 50 的殖民地 |  |
| 路易斯·加马（Luis Gama）非洲裔巴西人 天主教 | [巴西](Brazil.md) | 知识分子 | 废奴主义者 | 博学 一丝不苟 卷发俄耳甫斯 | 日期在 1865 至 1880 年之间 未废除奴隶制 |  |
| 若泽·杜·帕特罗西尼奥（José do Patrocinio）非裔美国人 天主教 | 以下任一：巴西 安哥拉 扬加 | 知识分子 | 废奴主义者 | 文学 坚韧 煽动家 | 日期在 1874 至 1893 年之间 未废除奴隶制 知识分子和乡村民众并非两者都边缘化 |  |
| 维尔古利诺·费雷拉·达席尔瓦（Virgulino Ferreira da Silva）东北部人 天主教 | [巴西](Brazil.md) | 乡村民众 | 土地改革者 | 社会侠盗 煽动家 雄心勃勃 | 事件“黑暗中的灯” 日期在 1920 年之后 |  |
| 热苏伊诺·阿尔维斯·德·梅洛·卡拉多（Jesuíno Alves de Melo Calado）东北部人 天主教 | [巴西](Brazil.md) | 乡村民众 | 土地改革者 | 社会侠盗 煽动家 光荣 | 事件“黑暗中的灯” 日期在 1871 至 1889 年之间 |  |
| 阿内西亚·考阿库（Anesia Cauacu）东北部人 天主教 | [巴西](Brazil.md) | 乡村民众 | 土地改革者 | 社会侠盗 富有魅力 雄心勃勃 | 事件“黑暗中的灯” 日期在 1913 至 1920 年之间 |  |
| 普利尼奥·萨尔加多（Plinio Salgado）巴西人 天主教 | [巴西](Brazil.md) | 天主教会 | 整体主义者 | 坚韧 煽动家 | 日期在 1925 年之后 |  |
| 安东尼奥·门德斯·马西埃尔（Antônio Mendes Maciel）东北部人 天主教 | 以下任一：巴西 赤道邦联 | 天主教会 | 土地改革者 | 虔诚 煽动家 坚韧 | 日期在 1877 至 1900 年之间 未实行自耕农土地制或集体化农业 |  |
| 若泽·奥伊蒂西亚（José Oiticia）巴西人 无神论者 | [巴西](Brazil.md) | 工会 | 无政府主义者 | 坚韧 煽动家 | 日期在 1912 至 1929 年之间 未同时实行委员会共和制和无政府状态 |  |
| 路易斯·卡洛斯·普雷斯特斯（Luis Carlos Prestes）主流文化 | [巴西](Brazil.md) | 军队 | 共产主义者 | 工程师 坚韧 | 日期在 1922 至 1928 年之间 |  |
| 安德烈斯·伊瓦涅斯（Andres Ibanez）主流文化 天主教 | 以下任一：玻利维亚 秘鲁-玻利维亚 | 知识分子 | 激进派 | 煽动家 勇敢 富有魅力 | 日期在 1868 至 1877 年之间 拥有拉巴斯州 知识分子未边缘化 |  |
| 华金·爱德华兹（Joaquin Edwards）主流文化 天主教 | 以下任一：智利 拉普拉塔 | 地主 | 法西斯主义者 | 文学 偏执 煽动家 | 日期在 1918 年之后 工会未边缘化 |  |
| 安布罗西奥·洛佩斯（Ambrosio Lopez）主流文化 天主教 | 以下任一：哥伦比亚 大哥伦比亚 安第斯联邦 | 小资产阶级 | 激进派 | 鼓舞人心的演说家 鲁莽 | 日期在 1845 至 1865 年之间 拥有昆迪纳马卡州 小资产阶级未边缘化 |  |
| 路易斯·特哈达（Luis Tejada）主流文化 天主教 | 以下任一：哥伦比亚 大哥伦比亚 安第斯联邦 | 知识分子 | 共产主义者 | 文学 创新 浪漫 | 日期在 1917 年之后 拥有昆迪纳马卡州 知识分子未边缘化 |  |
| 费尔南多·达基莱马（Fernando Daquilema）克丘亚人 天主教 | 以下任一：厄瓜多尔 大哥伦比亚 安第斯联邦 | 乡村民众 | 激进派 | 鼓舞人心的演说家 勇敢 | 日期在 1870 至 1885 年之间 拥有厄瓜多尔州 乡村民众未边缘化 |  |
| 佩德罗·巴勃罗·阿图斯帕里亚（Pedro Pablo Atusparia）克丘亚人 天主教 | 拥有建制的利马州 主体文化为以下任一：南安第斯 秘鲁 克丘亚 | 乡村民众 | 激进派 | 勇敢 煽动家 进攻规划者 | 日期在 1885 至 1895 年之间 乡村民众未边缘化 |  |
| 胡安·西尔维亚诺·戈多伊（Juan Silviano Godoi）主流文化 天主教 | 以下任一：智利 [5] 拉普拉塔 | 知识分子 | 激进派 | 资深 政治操盘手 勇敢 文学 | 日期在 1875 至 1895 年之间 知识分子未边缘化 |  |
| 拉斐尔·巴雷特（Rafael Barrett）主流文化 无神论者 | 以下任一：智利 [5] 拉普拉塔 | 知识分子 | 无政府主义者 | 坚韧 病弱 煽动家 | 日期在 1908 至 1920 年之间 知识分子未边缘化 |  |
| 安赫尔·穆尼斯（Angel Muniz）主流文化 天主教 | 以下任一：乌拉圭 拉普拉塔 | 地主 | 自由主义者 | 坚韧 光荣 | 日期在 1867 至 1881 年之间 没有任何投票权法律 地主未边缘化 |  |
| 保琳娜·路易西（Paulina Luisi）主流文化 天主教 | 以下任一：乌拉圭 拉普拉塔 | 知识分子 | 女权主义者 | 文学 资深外交官 富有魅力 | 日期在 1908 至 1930 年之间 知识分子未边缘化 |  |
| 弗朗西斯科·贝坦库尔特·索萨（Francisco Betancourt Sosa）主流文化 天主教 | 以下任一：委内瑞拉 大哥伦比亚 安第斯联邦 | 实业家 | 激进派 | 勇敢 浪漫 煽动家 | 日期在 1925 至 1935 年之间 拥有米兰达州 |  |
| 赫苏斯·法里亚（Jesús Faría）主流文化 无神论者 | 以下任一：委内瑞拉 大哥伦比亚 安第斯联邦 | 工会 | 先锋主义者 | 煽动家 坚韧 | 日期在 1929 年之后 拥有米兰达州 已研究政治鼓动 |  |
| 拉斐尔·西蒙·乌尔维纳（Rafael Simón Urbina）主流文化 天主教 | 以下任一：委内瑞拉 大哥伦比亚 安第斯联邦 | 乡村民众 | 社会民主主义者 | 林地作战专家 勇敢 骗子 | 日期在 1919 至 1935 年之间 拥有米兰达州 |  |
| 恩维尔帕夏（Enver Pasha）土耳其人 逊尼派 | [奥斯曼帝国](Ottoman Empire.md) | 军队 | 民族主义者 | 名将 雄心勃勃 直率 | 日期在 1906 至 1922 年之间 军队未边缘化 |  |
| 萨巴赫丁·奥斯曼奥卢（Sabahaddin Osmanoglu）土耳其人 逊尼派 | [奥斯曼帝国](Ottoman Empire.md) | 地主 | 改革者 | 雄心勃勃 文学 创新 | 日期在 1899 年之后，实行君主制 地主和知识分子并非两者都边缘化 |  |
| 布特鲁斯·布斯塔尼（Butrus al-Bustani）马什里基人 新教 | 以下任一：奥斯曼帝国 黎巴嫩 任何其他拥有黎巴嫩州的国家 | 知识分子 | 改革者 | 浪漫 创新 美学家 文学 | 日期在 1861 年 1 月 1 日至 1883 年 5 月 1 日之间 |  |
| 瓦尔达·亚齐吉（Warda al-Yaziji）马什里基人 天主教 | 以下任一：奥斯曼帝国 黎巴嫩 任何其他拥有黎巴嫩州的国家 | 知识分子 | 女权主义者 | 坚韧 美学家 博学 | 日期在 1867 至 1899 年之间 |  |
| 艾哈迈德·奥拉比（Ahmed Urabi）埃及人 逊尼派 | [埃及](Egypt.md) | 军队 | 民族主义者 | 名将 勇敢 直率 | 日期在 1876 至 1901 年之间 军队未边缘化 |  |
| 米尔扎·库奇克汗（Mirza Kuchik Khan）波斯人 国教 | [波斯](Persia.md) | 乡村民众 | 共产主义者 | 威严 虔诚 煽动家 | 日期在 1908 年之后 军队和乡村民众并非两者都边缘化 |  |
| 萨塔尔汗（Sattar Khan）波斯人 国教 | [波斯](Persia.md) | 小资产阶级 | 激进派 | 勇敢 虔诚 广受欢迎的指挥官 | 日期在 1904 年之后 小资产阶级、知识分子和乡村民众并非全部边缘化 |  |
| 莫罕达斯·甘地（Mohandas Gandhi）古吉拉特人 印度教 | [英属印度](East India.md) | 公务员 | 人道主义者 | 坚韧 鼓舞人心的演说家 富有魅力 | 手动生成 |  |
| 穆罕默德·阿里·真纳（Muhammad Ali Jinnah）古吉拉特人 逊尼派 | [英属印度](East India.md) | 公务员 | 社会民主主义者 | 直率 雄心勃勃 专家级政治操盘手 | 日期在 1896 年之后 公务员未边缘化 拥有古吉拉特邦州 |  |
| 比平·钱德拉·帕尔（Bipin Chandra Pal）孟加拉人 印度教 | [英属印度](East India.md) | 公务员 | 社会民主主义者 | 鼓舞人心的演说家 煽动家 | 日期在 1887 至 1932 年之间 公务员未边缘化 拥有古吉拉特邦州 |  |
| 巴尔·甘加达尔·提拉克（Bal Gangadhar Tilak）马拉地人 印度教 | [英属印度](East India.md) | 印度教祭司团 | 少数派传统主义者 | 煽动家 虔诚 偏执 | 日期在 1890 至 1920 年之间 印度教祭司团未边缘化 拥有孟买州 |  |
| 拉拉·拉杰帕特·拉伊（Lala Lajpat Rai）旁遮普人 印度教 | [英属印度](East India.md) | 巴德拉洛克 | 激进派 | 煽动家 虔诚 偏执 | 日期在 1886 至 1928 年之间 巴德拉洛克未边缘化 拥有旁遮普州 |  |
| 潘迪塔·拉玛拜（Pandita Ramabai）马拉地人 印度教 | [英属印度](East India.md) | 公务员 | 女权主义者 | 坚韧 直率 文学 | 日期在 1885 至 1922 年之间 公务员未边缘化 拥有孟买州 |  |
| 巴格特·辛格（Bhagat Singh）旁遮普人 无神论者 | [英属印度](East India.md) | 公务员 | 无政府主义者 | 勇敢 富有魅力 | 日期在 1926 年之后 公务员未边缘化 拥有旁遮普州 |  |
| 萨罗吉尼·奈杜（Sarojini Naidu）孟加拉人 印度教 | [英属印度](East India.md) | 公务员 | 女权主义者 | 鼓舞人心的演说家 政治操盘手 文学 | 日期在 1903 年之后 公务员未边缘化 直接或通过附属国拥有海得拉巴州 |  |
| 阿布尔·阿扎德（Abul Azad）普什图人 逊尼派 | [英属印度](East India.md) | 公务员 | 社会民主主义者 | 文学 虔诚 | 日期在 1911 年之后 公务员未边缘化 |  |
| 乌达姆·辛格（Udham Singh）旁遮普人 锡克教 | [英属印度](East India.md) | 工会 | 激进派 | 勇敢 鲁莽 | 日期在 1918 年之后 工会未边缘化 |  |
| 米图本·佩蒂特（Mithuben Petit）波斯人 泛灵论者[6] | [英属印度](East India.md) | 巴德拉洛克 | 改革者 | 勇敢 坚韧 富有魅力 | 日期在 1924 年之后 巴德拉洛克未边缘化 |  |
| 比姆拉奥·拉姆吉·安贝德卡尔（Bhimrao Ramji Ambedkar）马拉地人 印度教 | [英属印度](East India.md) | 赖约特 | 社会民主主义者 | 直率 文学 专家级政治操盘手 | 日期在 1916 年之后 赖约特未边缘化 通过事件生成 |  |
| 达莫达尔·哈里·查佩卡尔（Damodar Hari Chapekar）马拉地人 印度教 | [英属印度](East India.md) | 巴德拉洛克 | 主权主义者 | 勇敢 鲁莽 虔诚 | 日期在 1893 至 1910 年之间 巴德拉洛克未边缘化 |  |
| 乔治·汤普森（George Thompson）英格兰人 新教 | [印度斯坦](Hindustan.md) | 知识分子 | 废奴主义者 | 光荣 坚韧 鼓舞人心的演说家 | 由英国印度协会事件生成 |  |
| 孙中山（Sun Yat-Sen）汉族 新教 | 以下任一：中国 太平天国 | 小资产阶级 | 共和主义者 | 博学 坚韧 雄心勃勃 | 日期在 1888 至 1925 年之间，实行君主制或神权制，与条约港接壤 |  |
| 西乡隆盛（Saigo Takamori）日本人 神道教 | [日本](Japan.md) | 武士 | 水户学 | 煽动家 富有魅力 光荣 | 日期在 1868 至 1877 年之间 武士未边缘化 |  |
| 儒勒·布吕内（Jules Brunet）法国人 天主教 | [日本](Japan.md) | 军队 | 威权主义者 | 雄心勃勃 勇敢 外交官 | 日期在 1867 至 1892 年之间 军队和地主并非两者都边缘化 |  |
| 久米邦武（Kume Kunitake）日本人 大乘佛教 | 日本 | 知识分子 | 虚无主义者 | 直率 | 在 1878 至 1908 年之间激活“虚无主义运动”日志条目 |  |
| 大盐平八郎（Ōshio Heihachirō）日本人 大乘佛教 | [日本](Japan.md) | 兰学者 | 水户学 | 光荣 社会侠盗 虔诚 博学 | 由事件生成 |  |
| 高岛秋帆（Takashima Shūhan）日本人 大乘佛教 | [日本](Japan.md) | 武士 | 水户学 | 创新 坚韧 工程师 资深炮兵指挥官 | 由事件生成 |  |
| 坂本龙马（Sakamoto Ryōma）日本人 国教 | [日本](Japan.md) | 武士 | 正文义 | 勇敢 资深外交官 光荣 | 日期在 1860 至 1895 年之间 |  |
| 中江兆民（Nakae Chōmin）日本人 国教 | [日本](Japan.md) | 小资产阶级 | 激进派 | 坚韧 美学家 | 日期在 1874 至 1901 年之间 |  |
| 幸德传次郎（Kōtoku Denjirō）日本人 国教 | [日本](Japan.md) | 工会 | 无政府主义者 | 社会侠盗 美学家 | 日期在 1890 至 1911 年之间 |  |
| 井上馨（Inoue Kaoru）日本人 国教 | [日本](Japan.md) | 军队 | 现代化论者 | 圆滑 政治任命者 | 日期在 1863 至 1915 年之间 |  |
| 岸田俊子（Kishida Toshiko）日本人 国教 | [日本](Japan.md) | 小资产阶级 | 女权主义者 | 鼓舞人心的演说家 勇敢 | 日期在 1882 至 1901 年之间 |  |
| 平冢雷鸟（Hiratsuka Raichō）日本人 国教 | [日本](Japan.md) | 知识分子 | 人道主义者 | 鼓舞人心的演说家 坚韧 | 日期在 1910 年之后 |  |
| 与谢野晶子（Yosano Akiko）日本人 国教 | [日本](Japan.md) | 小资产阶级 | 女权主义者 | 鼓舞人心的演说家 直率 偏执 | 日期在 1900 年之后 |  |
| 樋口一叶（Higuchi Ichiyō）日本人 国教 | [日本](Japan.md) | 小资产阶级 | 现代化论者 | 文学 结核病 | 日期在 1883 至 1930 年之间 |  |
| 田中智学（Tanaka Chigaku）日本人 国教 | [日本](Japan.md) | 寺社 | 沙文主义者 | 富有魅力 鼓舞人心的演说家 虔诚 | 日期在 1884 年之后 |  |
| 贺川丰彦（Kagawa Toyohiko）日本人 国教 | [日本](Japan.md) | 工会 | 人道主义者 | 富有魅力 虔诚 | 日期在 1909 年之后 |  |
| 堺利彦（Sakai Toshihiko）日本人 国教 | [日本](Japan.md) | 工会 | 共产主义者 | 鼓舞人心的演说家 坚韧 | 日期在 1900 至 1933 年之间 |  |
| 崔济愚（Choe Je-u）朝鲜人 儒教 | [朝鲜](Korea.md) | 乡村民众 | 土地改革者 | 鼓舞人心的演说家 虔诚 | 日期在 1855 至 1880 年之间 |  |
| 佩德罗·佩拉埃斯（Pedro Peláez）菲律宾混血 天主教 | [菲律宾](Philippines.md) | 天主教会 | 主权主义者 | 虔诚 光荣 |  |  |
| 何塞·布尔戈斯（José Burgos）菲律宾混血 天主教 | [菲律宾](Philippines.md) | 天主教会 | 改革者 | 虔诚 博学 | 日期在 1864 至 1872 年之间 天主教会未边缘化 |  |
| 何塞·黎刹（José Rizal）菲律宾混血 天主教 | [菲律宾](Philippines.md) | 智识阶层 | 智识阶层 | 文学 博学 创新 | 日期在 1891 年之后 智识阶层未边缘化 |  |
| 威差衍·扎克里（Wichaichan Chakri）泰人 上座部佛教 | [暹罗](Siam.md) | 地主 | 传统主义者 | 工程师 雄心勃勃 鲁莽 | 日期在 1868 至 1885 年之间 地主未边缘化 |  |

## 参考资料

1. ↑ 参见 /Victoria 3/game/common/defines/00_defines.txt 中的 `AGITATOR_EXPECTED_SPAWN_INTERVAL_0_LITERACY` 和 `AGITATOR_EXPECTED_SPAWN_INTERVAL_100_LITERACY`
2. ↑ 2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 仅通过生成他们的事件中的特定选项
3. ↑ 代表神秘学信仰
4. ↑ 某些条件可以产生马克思的变体，这些变体可能拥有主流文化和国教
5. ↑ 5.0 5.1 缺陷，应为[巴拉圭](Paraguay.md)
6. ↑ 祆教的替代