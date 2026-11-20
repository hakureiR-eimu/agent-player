---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Subject
source: https://vic3.paradoxwikis.com/Subject
pageid: 3146
categories: [1.13, Articles_with_potentially_outdated_sections, Diplomacy]
fetched: 2026-10-27
---
本文已针对游戏当前 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行验证。

外交
外交行动
外交博弈
强权集团
附属国
条约

**附属国**（Subject）是从属于另一国家（即*宗主国*，overlord/suzerain）的国家。它们拥有内部自治权，宗主国的干预有限。附属国拥有自己的预算、建造部门、[利益集团](https://vic3.paradoxwikis.com/Interest_groups)、[法律](Laws.md)和机构，但在开展对外外交时受到限制。所有类型的附属国都会自动以次级成员身份加入其宗主国的[市场](Market.md)。

## 通用机制

附属国是[外交协议](https://vic3.paradoxwikis.com/Diplomatic_pact)的一种，宗主国必须持续支付 10 影响力来维持它们。除君合国外的所有附属国类型的[等级](Rank.md)都必须低于其宗主国；任何附属国类型都不能是列强或主要政权。例如，[不列颠东印度公司](East India.md)在游戏开始时是次要政权，因为它是[大不列颠](Great Britain.md)的附属国，尽管它的威望高于列强[美利坚合众国](America.md)。所有类型的附属国都会随其宗主国一起加入和退出[强权集团](Power bloc.md)。

此外，附属国还有其他限制或义务，因类型而异，例如向宗主国上缴部分政府收入、无法发起自己的外交博弈，或被迫在[外交博弈](https://vic3.paradoxwikis.com/Diplomatic_plays)中加入宗主国一方。不过，它们也获得一定程度的保护，因为宗主国会自动被召唤加入针对该附属国的外交博弈。但如果附属国加入针对另一国家的外交博弈，则不会受到宗主国的保护。

某些附属国类型是自治的，意味着它们可以与宗主国以外的国家进行大部分外交活动，甚至可以拥有自己的附属国。主要的外交限制在于，自治附属国与其宗主国之间不能互相使用大部分战争目标。自治附属国（如自治领）及其宗主国有可能通过在外交博弈中支持对立双方而彼此开战。即使在这种情况下，附属国协议仍然保留其所有常规特性。只要战争中未提出独立要求，附属国与宗主国在战后即恢复正常关系。

如果宗主国发起外交博弈或直接成为外交博弈的目标，非自治附属国和自治领会自动加入该博弈。如果宗主国加入另一场博弈——即使是防御其附属国——其其他附属国也不会自动加入该博弈。

宗主国可以在附属国中发起[法律](https://vic3.paradoxwikis.com/Law)变更，且需满足制定法律的全部常规要求。宗主国还从附属国的一部分 GDP（50%）、陆军（1.67%）和海军（10%）力量投射中获得威望；这不会减少附属国从这些来源获得的威望。

### 独立倾向

*独立倾向*（Liberty desire）表示附属国在多大程度上愿意顺从宗主国的意愿或要求，或者相反，表示其对更大自治甚至独立的渴望。

独立倾向的范围为 0 至 100，分为三个等级：*低*、*中等*和*高*。

| 等级 | 低 | 中等 | 高 |
|---|---|---|---|
| 范围 | 0 – 24.9 | 25 – 74.9 | 75 – 100 |
| 效果 | 受歧视人口的公开偏见、文化抹除和暴力敌视状态所导致的激进派增长 −10% 来自政治运动的忠诚派 +25% | — | 受歧视人口的公开偏见、文化抹除和暴力敌视状态所导致的激进派增长 +10% 来自政治运动的激进派 +25% |

独立倾向低于 25 的附属国，宗主国可以降低其自治度，前提是存在自治度更低的附属国类型可用。

宗主国也可以提高大多数附属国的自治度。独立倾向达到 75 或以上的附属国也可以请求提高自治度。与降低自治度一样，必须有自治度更高的类型可用。

某些附属国类型变更自治度有额外要求，即请求方须已研究特定技术：

- 君合国需要*民族主义*
- [特许公司](Government type.md)需要*文明开化使命*

自治度每 5 年只能变更一次。

在过去 5 年内被拒绝提高自治度的附属国，可以通过[外交博弈](Diplomatic play.md)要求提高自治度或试图获得独立。处于最高自治度的附属国也可以随时要求独立。

### 每周独立倾向

独立倾向每周根据以下因素变化。乘数在固定值和比例来源求和后计算。

| 来源 | 效果 |
|---|---|
| 基础值 | +0.1 |
| 关系为敌对 | +0.5 |
| 关系为冷淡 | +0.25 |
| 关系为不佳 | +0.1 |
| 关系为中立 | +0 |
| 关系为热忱 | −0.025 |
| 关系为友善 | −0.05 |
| 关系为亲密 | −0.1 |
| 宗主国恶名显著 | +0.1 |
| 宗主国恶名昭著 | +0.25 |
| 宗主国被排斥 | +2.0 |
| 拥有知识共享 | −0.05 |
| 拥有免除兵役 | −0.05 |
| 拥有提高上缴 | +0.1 |
| 拥有降低上缴 | −0.05 |
| 拥有支持政权 | −0.1 |
| 与宗主国市场隔绝 | +1.0 |
| 处于拥有神圣公民规范 II 的强权集团中，且与宗主国宗教相同 | −0.1 |
| 宗主国威望低于 1 | +1.0 |
| 附属国威望低于 1 | −0.1 |
| 宗主国陆军力量投射低于 1 | +1.0 |
| 附属国陆军力量投射低于 1 | −0.25 |
| 每周独立倾向修正值 | 不定 |
| 是特许公司 | −0.2 |
| 是东印度群岛，宗主国是尼德兰 | −0.2 |
| 是玉兹，宗主国拥有“平定草原”日志条目 | −0.2 |
| 宗主国实行孤立主义或其变体 | +2.0 |

| 来源 | 公式 |
|---|---|
| 不具有附属国身份，与宗主国无共同主流文化 | − − 0.1 ≤ ≤ ± ± highest primary culture fervor − − 25 150 ≤ ≤ + 0.5 {\displaystyle -0.1\leq \pm {\tfrac {{\text{highest primary culture fervor}}-25}{150}}\leq +0.5} ![{\displaystyle -0.1\leq \pm {\tfrac {{\text{highest primary culture fervor}}-25}{150}}\leq +0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/fc9683cfc6198a4a266158f06239a23d09826f4e) |
| 与宗主国共享所有主流文化 | − − 0.2 ≤ ≤ − − primary culture fervor − − 25 150 ⋅ ⋅ num primary cultures ≤ ≤ − − 0.05 {\displaystyle -0.2\leq -{\tfrac {{\text{primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}\leq -0.05} ![{\displaystyle -0.2\leq -{\tfrac {{\text{primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}\leq -0.05}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/0c087b69568c1d6f10f14847474c19347b2f9ae3)[1] |
| 具有附属国身份，与宗主国共享部分主流文化 | − − 0.25 ≤ ≤ − − primary culture fervor − − 25 150 ⋅ ⋅ num primary cultures ≤ ≤ 0 {\displaystyle -0.25\leq -{\tfrac {{\text{primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}\leq 0} ![{\displaystyle -0.25\leq -{\tfrac {{\text{primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}\leq 0}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/387bff53dde0f52b86841796202015620a6d20e9)[1] |
| 不具有附属国身份，与宗主国共享部分主流文化 | − − 0.25 ≤ ≤ + unshared primary culture fervor − − 25 150 ⋅ ⋅ num primary cultures − − shared primary culture fervor − − 25 150 ⋅ ⋅ num primary cultures ≤ ≤ + 0.5 {\displaystyle -0.25\leq +{\tfrac {{\text{unshared primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}-{\tfrac {{\text{shared primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}\leq +0.5} ![{\displaystyle -0.25\leq +{\tfrac {{\text{unshared primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}-{\tfrac {{\text{shared primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}\leq +0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/038a618e1b961bde615833b29ae527cab75b00c8)[2] |
| 是保护国或朝贡国，宗主国威望高出 1.5 倍以上 | − − 0.05 ≤ ≤ − − overlord prestige subject prestige ⋅ ⋅ 150 ≤ ≤ − − 0.01 {\displaystyle -0.05\leq -{\tfrac {\text{overlord prestige}}{{\text{subject prestige}}\cdot 150}}\leq -0.01} ![{\displaystyle -0.05\leq -{\tfrac {\text{overlord prestige}}{{\text{subject prestige}}\cdot 150}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/f0df5c313c93b11abc8a57ea88be1bba5cec0bea) |
| 是保护国或朝贡国，宗主国威望高出不足 1.5 倍 | + overlord prestige subject prestige ⋅ ⋅ 1.5 3 ≤ ≤ + 2.5 {\displaystyle +{\tfrac {\text{overlord prestige}}{\text{subject prestige}}}\cdot {\tfrac {1.5}{3}}\leq +2.5} ![{\displaystyle +{\tfrac {\text{overlord prestige}}{\text{subject prestige}}}\cdot {\tfrac {1.5}{3}}\leq +2.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/10cf835c68b15a774e3b6ff90c06003f82120c42) |
| 是自治领、君合国或特许公司，宗主国威望高出 2 倍以上 | − − 0.05 ≤ ≤ − − overlord prestige subject prestige ⋅ ⋅ 200 ≤ ≤ − − 0.01 {\displaystyle -0.05\leq -{\tfrac {\text{overlord prestige}}{{\text{subject prestige}}\cdot 200}}\leq -0.01} ![{\displaystyle -0.05\leq -{\tfrac {\text{overlord prestige}}{{\text{subject prestige}}\cdot 200}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/6a19d037d6e12539e9b7172f649a2b11c91961e8) |
| 是自治领、君合国或特许公司，宗主国威望高出不足 2 倍 | + overlord prestige subject prestige ⋅ ⋅ 2 5 ≤ ≤ + 0.5 {\displaystyle +{\tfrac {\text{overlord prestige}}{\text{subject prestige}}}\cdot {\tfrac {2}{5}}\leq +0.5} ![{\displaystyle +{\tfrac {\text{overlord prestige}}{\text{subject prestige}}}\cdot {\tfrac {2}{5}}\leq +0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/a58d97c8e7ff0ce1947d4bdf0347b06760261e79) |
| 是可吞并附属国（王领、傀儡国、殖民地或附庸国），宗主国威望高出 3 倍以上 | − − 0.1 ≤ ≤ − − overlord prestige subject prestige ⋅ ⋅ 300 ≤ ≤ − − 0.01 {\displaystyle -0.1\leq -{\tfrac {\text{overlord prestige}}{{\text{subject prestige}}\cdot 300}}\leq -0.01} ![{\displaystyle -0.1\leq -{\tfrac {\text{overlord prestige}}{{\text{subject prestige}}\cdot 300}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/8157831d958efe8485d895e8a10a5b99e4376616) |
| 是可吞并附属国（王领、傀儡国、殖民地或附庸国），宗主国威望高出不足 3 倍 | + overlord prestige subject prestige ⋅ ⋅ 5 ≤ ≤ + 0.5 {\displaystyle +{\tfrac {\text{overlord prestige}}{\text{subject prestige}}\cdot 5}\leq +0.5} ![{\displaystyle +{\tfrac {\text{overlord prestige}}{\text{subject prestige}}\cdot 5}\leq +0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/e66b398a0ca5ae053ffb3b87b2305671e62bf434) |
| 是东印度、东印度群岛或拉杰普塔纳 [3]，宗主国陆军力量投射高出 10 倍以上 | − − 0.1 ≤ ≤ − − overlord army power projection subject army power projection ⋅ ⋅ 250 ≤ ≤ − − 0.01 {\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 250}}\leq -0.01} ![{\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 250}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/8cad98cc39dcac8564c9630ad840069a44e6f358) |
| 是东印度、东印度群岛或拉杰普塔纳 [3]，宗主国陆军力量投射高出不足 10 倍 | + subject army power projection ⋅ ⋅ 10 overlord army power projection ⋅ ⋅ 10 ≤ ≤ + 0.25 {\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 10}{{\text{overlord army power projection}}\cdot 10}}\leq +0.25} ![{\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 10}{{\text{overlord army power projection}}\cdot 10}}\leq +0.25}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/7b048b019217008051f1f7640078b5ea6315d29b) |
| 是保护国或朝贡国，宗主国陆军力量投射高出 5 倍以上 | − − 0.1 ≤ ≤ − − overlord army power projection subject army power projection ⋅ ⋅ 100 ≤ ≤ − − 0.01 {\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 100}}\leq -0.01} ![{\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 100}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/907ae94aa0b9e32ea32548d58e499a00a8026589) |
| 是保护国或朝贡国，宗主国陆军力量投射高出不足 5 倍 | + subject army power projection ⋅ ⋅ 5 overlord army power projection ⋅ ⋅ 10 ≤ ≤ + 0.5 {\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 5}{{\text{overlord army power projection}}\cdot 10}}\leq +0.5} ![{\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 5}{{\text{overlord army power projection}}\cdot 10}}\leq +0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/290b01ee7955755d4ccd4d36a9e513dafaf1ca8d) |
| 是自治领、君合国或特许公司，宗主国陆军力量投射高出 7.5 倍以上 | − − 0.1 ≤ ≤ − − overlord army power projection subject army power projection ⋅ ⋅ 175 ≤ ≤ − − 0.01 {\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 175}}\leq -0.01} ![{\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 175}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/0856a6a6cafd4d0587d1ba14f17a340c57db014b) |
| 是自治领、君合国或特许公司，宗主国陆军力量投射高出不足 7.5 倍 | + subject army power projection ⋅ ⋅ 7.5 overlord army power projection ⋅ ⋅ 10 ≤ ≤ + 0.5 {\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 7.5}{{\text{overlord army power projection}}\cdot 10}}\leq +0.5} ![{\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 7.5}{{\text{overlord army power projection}}\cdot 10}}\leq +0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/f1ff370a9fd5df7fe4c32b10ed5a1b5ed9ff7673) |
| 是可吞并附属国（王领、傀儡国、殖民地或附庸国），宗主国陆军力量投射高出 10 倍以上 | − − 0.1 ≤ ≤ − − overlord army power projection subject army power projection ⋅ ⋅ 250 ≤ ≤ − − 0.01 {\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 250}}\leq -0.01} ![{\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 250}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/8cad98cc39dcac8564c9630ad840069a44e6f358) |
| 是可吞并附属国（王领、傀儡国、殖民地或附庸国），宗主国陆军力量投射高出不足 10 倍 | + subject army power projection ⋅ ⋅ 10 overlord army power projection ⋅ ⋅ 10 ≤ ≤ + 0.5 {\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 10}{{\text{overlord army power projection}}\cdot 10}}\leq +0.5} ![{\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 10}{{\text{overlord army power projection}}\cdot 10}}\leq +0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/76968cf9eb9ef578d2dc11f117c9d9ec804bedad) |
| 宗主国是附属国，宗主国的宗主国陆军力量投射高出 10 倍以上 | − − 0.1 ≤ ≤ − − overlord's overlord army power projection subject army power projection ⋅ ⋅ 250 ≤ ≤ − − 0.01 {\displaystyle -0.1\leq -{\tfrac {\text{overlord's overlord army power projection}}{{\text{subject army power projection}}\cdot 250}}\leq -0.01} ![{\displaystyle -0.1\leq -{\tfrac {\text{overlord's overlord army power projection}}{{\text{subject army power projection}}\cdot 250}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/3910eb8a21ff47b591f56e8e842e63f5aa6cea76) |
| 宗主国的同盟与防御条约 | − − 0.25 ≤ ≤ − − ∑ ∑ ( 0.1 ⋅ ⋅ num of great power allies ) ( num of major power allies ⋅ ⋅ 0.05 ) ( num of minor power allies ⋅ ⋅ 0.03 ) ( num of unrecognized major power allies ⋅ ⋅ 0.03 ) ( num of great power defensive pacts ⋅ ⋅ 0.05 ) ( num of major power defensive pacts ⋅ ⋅ 0.03 ) ≤ ≤ 0 {\displaystyle -0.25\leq -\sum {\begin{aligned}&(0.1\cdot {\text{num of great power allies}})\\&({\text{num of major power allies}}\cdot 0.05)\\&({\text{num of minor power allies}}\cdot 0.03)\\&({\text{num of unrecognized major power allies}}\cdot 0.03)\\&({\text{num of great power defensive pacts}}\cdot 0.05)\\&({\text{num of major power defensive pacts}}\cdot 0.03)\end{aligned}}\leq 0} ![{\displaystyle -0.25\leq -\sum {\begin{aligned}&(0.1\cdot {\text{num of great power allies}})\\&({\text{num of major power allies}}\cdot 0.05)\\&({\text{num of minor power allies}}\cdot 0.03)\\&({\text{num of unrecognized major power allies}}\cdot 0.03)\\&({\text{num of great power defensive pacts}}\cdot 0.05)\\&({\text{num of major power defensive pacts}}\cdot 0.03)\end{aligned}}\leq 0}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/142d662236cb210918493f29a55c28a5159ae857) |
| 政府中亲宗主国游说团成员的政治力量 | − − clout ⋅ ⋅ 0.5 {\displaystyle -{\text{clout}}\cdot 0.5} ![{\displaystyle -{\text{clout}}\cdot 0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/453aca8d9bf23b4bcef63f2f359433956fdafd92) |
| 在野的亲宗主国游说团成员的政治力量 | − − clout ⋅ ⋅ 0.25 {\displaystyle -{\text{clout}}\cdot 0.25} ![{\displaystyle -{\text{clout}}\cdot 0.25}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/42ab43f187c6a5be8a0cdb963dcc6eba5d17828d) |
| 政府中反宗主国游说团成员的政治力量 | + clout ⋅ ⋅ 0.5 {\displaystyle +{\text{clout}}\cdot 0.5} ![{\displaystyle +{\text{clout}}\cdot 0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/c0f8a49122aaf2a756f4b8e5c3b733bfad64181d) |
| 在野的反宗主国游说团成员的政治力量 | + clout ⋅ ⋅ 0.25 {\displaystyle +{\text{clout}}\cdot 0.25} ![{\displaystyle +{\text{clout}}\cdot 0.25}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/543c7d89e467b022af4ea36f87bea1294853b275) |
| 附属国的经济依附度大于 0 | ( 1 − − economic dependence ) ⋅ ⋅ 1 10 {\displaystyle (1-{\text{economic dependence}})\cdot {\tfrac {1}{10}}} ![{\displaystyle (1-{\text{economic dependence}})\cdot {\tfrac {1}{10}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/04454d232b82fc687a32671143bbfafc0b1a2f9e) |
| 附属国的经济依附度小于 0 | ( 1 − − economic dependence ) ⋅ ⋅ 1 3 {\displaystyle (1-{\text{economic dependence}})\cdot {\tfrac {1}{3}}} ![{\displaystyle (1-{\text{economic dependence}})\cdot {\tfrac {1}{3}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/15faf61f4513b3d0bc6d08bea60e765bbbfd6263) |
| 附属国属于宗主国市场，附属国拥有港口，附属国与宗主国不相邻，宗主国补给网络低于 100% | 1 − − overlord supply network {\displaystyle 1-{\text{overlord supply network}}} ![{\displaystyle 1-{\text{overlord supply network}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/15957ce38f918de5eb0b40d4a59f7370647654fb) |
| 来源 | 公式 |
|---|---|
| **比例乘数**，*最先应用* |  |
| 每周独立倾向为负 独立倾向低于 50 不能将每周独立倾向降至 −0.01 以下 | × × liberty desire 50 {\displaystyle \times {\frac {\text{liberty desire}}{50}}} ![{\displaystyle \times {\frac {\text{liberty desire}}{50}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/a7a7857b602f4f13f787fd042cee41ed86302726) |
| 每周独立倾向为正 独立倾向高于 50 不能将每周独立倾向降至 +0.01 以下 | × × 100 − − liberty desire 50 {\displaystyle \times {\frac {100-{\text{liberty desire}}}{50}}} ![{\displaystyle \times {\frac {100-{\text{liberty desire}}}{50}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/2784923acfa7e0100adb698f157243cf736c6b79) |
| **修正乘数**，*其次应用* |  |
| 每周独立倾向为正 独立倾向增加乘数之和 | 不定 |
| 每周独立倾向为负 独立倾向降低乘数之和 | 不定 |
| **休战乘数**，*第三应用* |  |
| 每周独立倾向为正 附属国与宗主国处于休战状态 | × × 0.5 {\displaystyle \times 0.5} ![{\displaystyle \times 0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/bada9ef0ee4f511b7f07c4d8453f8da35a35ecf3) |

除每周变化外，各种行动和事件也可以直接增加或减少独立倾向。

### 吞并（Annexation）

宗主国可以要求吞并其傀儡国、殖民地、附庸国和王室领地。如果附属国的独立倾向低于 25 或正处于叛乱状态，这一要求的[恶名](https://vic3.paradoxwikis.com/Infamy)将获得 **−75%** 的减免。

附属国被吞并后，所有其他附属国将在 5 年内获得 **+0.2** 独立倾向。

如果傀儡国、附庸国、王室领地和君合国与统一国家拥有相同的主文化，它们也会在统一时被吞并。

### 独立（Independence）

保护国和朝贡国可以通过[外交博弈](Diplomatic play.md)向宗主国要求独立，这有可能引发独立战争。其他类型的附属国如果在 5 年内被拒绝提高自治权的请求，也可以要求独立。宗主国也可以单方面释放附属国，不过这种情况很少见。

如果附属国成为另一国外交博弈的目标，而其宗主国未能保护它，该附属国将在战争爆发时自动独立。

### 叛乱（Rebellion）

附属国可以通过发起或加入以提高自治权或独立为战争目标的外交博弈来反叛宗主国。独立倾向高的附属国更有可能叛乱。当附属国叛乱时，宗主国针对该附属国的所有战争目标在恶名上获得 **−75%** 的减免。

### 强制推行法律

宗主国可以对除朝贡国和保护国以外的任何附属国强制推行法律。该法律必须能够被附属国制定，且某些法律还有进一步的限制。被强制的法律会经历正常的制定流程，可能失败，也可能像平常一样引发革命。特许公司、殖民地、王室领地和傀儡国在制定被强制的法律时拥有 **+10%** 的制定成功率。

## 附属国类型

共有九种附属国类型。其中五种是非自治的，即它们无法发起任何外交博弈（独立和提高自治权除外），并且会自动加入其宗主国的[外交博弈](https://vic3.paradoxwikis.com/Diplomatic_plays)。另外四种是自治的，即它们可以正常发起或加入外交博弈，也可以拥有自己的附属国；殖民地也可以拥有自己的附属国。自治领和特许公司属于半自治，因为它们会自动加入宗主国的博弈；而朝贡国和保护国则是完全自治的，不会自动加入。非自治附属国可以被设为*免于服役*，从而不自动加入宗主国的博弈。

请注意，如果宗主国不是博弈的发起者或最初目标，附属国不会自动加入其博弈。因此，针对某一附属国的博弈会阻止宗主国的其他非自治附属国加入，除非宗主国使用*强制军事通行*。自治附属国仍可正常加入。

大多数附属国类型会将其[税收、铸币及其他政府收入](Treasury.md)的一部分上缴给宗主国（但不包括关税、投资池转移或外交协议收入）。作为市场主导者，附属国还会将其[护航船队](https://vic3.paradoxwikis.com/Convoys)的一部分交给宗主国。

某些附属国类型会计入宗主国[统一](https://vic3.paradoxwikis.com/Unification)所需的州。如果该附属国与可成立国家共享主[文化](Culture.md)，它将在成立时被完全吞并——无论它是否拥有任何所需州。拥有其他主文化的附属国不会被吞并，但会在成立时将所有相关的州区域割让给宗主国。[4] 附属国只能支持其直接宗主国进行重大统一，例如[德国](Germany.md)。

| 类型 | 自治 | 降级为 | 升级为 | 可统一 | 收入转移 | 最大参与度 | 宗主国类型 | 附属国类型 |
|---|---|---|---|---|---|---|---|---|
| 傀儡国 | ![No](/images/thumb/0/04/No.png/24px-No.png) | 吞并 | 保护国 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 30% | 8000 | 受承认 | 非殖民 |
| 附庸国 | ![No](/images/thumb/0/04/No.png/24px-No.png) | 吞并 | 朝贡国 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 30% | 5000 | 未受承认 | 任意 |
| 殖民地 | ![No](/images/thumb/0/04/No.png/24px-No.png) | 吞并 | 自治领 | ![No](/images/thumb/0/04/No.png/24px-No.png) | 30% | 8000 | 受承认 | 殖民/公司 |
| 保护国 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 傀儡国 | 独立 | ![No](/images/thumb/0/04/No.png/24px-No.png) | — | 5000 | 受承认 | 非殖民 |
| 朝贡国 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 附庸国 | 独立 | ![No](/images/thumb/0/04/No.png/24px-No.png) | 20% | 2500 | 未受承认 | 任意 |
| 特许公司 | ![Semi-autonomous](/images/thumb/5/54/Information.png/24px-Information.png) | 殖民地 | 独立 | ![No](/images/thumb/0/04/No.png/24px-No.png) | 30% | 5000 | 受承认 | 殖民/公司 |
| 自治领 | ![Semi-autonomous](/images/thumb/5/54/Information.png/24px-Information.png) | 殖民地 | 独立 | ![No](/images/thumb/0/04/No.png/24px-No.png) | 25% | 8000 | 受承认 | 殖民 |
| 君合国 | ![No](/images/thumb/0/04/No.png/24px-No.png) | 王室领地 附庸国 | 独立 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | — | 5000 | 任意 | 任意 |
| 王室领地 | ![No](/images/thumb/0/04/No.png/24px-No.png) | 吞并 | 君合国 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 15% | 8000 | 受承认 | 非殖民 |

公司型国家只能作为特许公司或殖民地附属国存在。

### 君合国（Personal union）

君合国是一种特殊的附属国类型，其特点是附属国与宗主国共享君主。此外，君合国的从属方可以与宗主国同等级——甚至更高——尽管在正常游戏中这不太可能发生。如果任一方不再是君主制国家，君合国即告终结。在研究完成*民族主义*之前，君合国从属方的自治权无法更改。从属方不能更改[治理原则法律](Power structure laws.md)以脱离君主制。

除通过 effect 或由王室领地附属国提高自治权外，游戏中无法成立君合国。目前有以下几个例子：

- 日志条目*自由邦问题*会在触发该条目的国家之下建立一个与[自由邦](Free State.md)的君合国
- 日志条目*统一公国*可以在[瓦拉几亚](Wallachia.md)和[摩尔达维亚](Moldavia.md)之间建立君合国——即联合公国——作为成为[罗马尼亚](Romania.md)的前奏。
- 日志条目*人人为一*可以建立[特兰西瓦尼亚](Transylvania.md)隶属于联合公国的君合国。
- 日志条目*伦敦会议*可以建立[林堡](https://vic3.paradoxwikis.com/Limburg)隶属于[荷兰](Netherlands.md)的君合国
- 日志条目*匈牙利问题*可以建立[匈牙利](Hungary.md)隶属于[奥地利](Austria.md)的君合国
- 决议*发布三元制宣言*可以建立[克罗地亚](Croatia.md)隶属于[奥地利](Austria.md)的君合国
- 日志条目*联合王国*可以建立[巴西](Brazil.md)隶属于[葡萄牙](Portugal.md)的君合国

所有其他君合国在游戏开始时即存在：

- [丹麦](Denmark.md)之下的[石勒苏益格](Schleswig.md)和[荷尔斯泰因](Holstein.md)
- [大不列颠](Great Britain.md)之下的[汉诺威](Hanover.md)——游戏开始后不久随国王威廉的去世而终结
- [荷兰](Netherlands.md)之下的[卢森堡](Luxembourg.md)——注意这两国被[比利时](Belgium.md)和[普鲁士](Prussia.md)隔开。
- [俄罗斯](Russia.md)之下的[芬兰](Finland.md)
- [瑞典](Sweden.md)之下的[挪威](Norway.md)

游戏开始时存在以下王室领地，均为[奥地利](Austria.md)的附属国

- [匈牙利](Hungary.md)
- [克罗地亚](Croatia.md)
- [特兰西瓦尼亚](Transylvania.md)

此外，[巴纳特](Banat.md)和[斯洛伐克](https://vic3.paradoxwikis.com/Slovakia)可以作为*匈牙利革命*日志条目的一部分成为奥地利的王室领地附属国。

### 特许公司（Chartered companies）

特许公司是一种特殊的附属国类型，即国家由宗主国的一家公司治理。在研究完成*开化使命*之前，特许公司的自治权不能被降低。

特许公司不能建立自己的[公司](Companies.md)，但此类国家中所有政府拥有的建筑都被视为该公司所有，并受益于公司的吞吐量和建造加成。如果建筑属于该公司关联的产业之一，它将获得完整的吞吐量和建造加成，否则加成降至仅 20%。

吞吐量加成仅应用于特许公司的国有建筑，建造加成仅应用于政府建造。由投资者拥有或正在建造的建筑不受影响。

游戏开始时存在以下特许公司：

- [大不列颠](Great Britain.md)之下的[哈德逊湾公司](Hudson’s Bay Company.md)和[东印度公司](https://vic3.paradoxwikis.com/East_India_Company)
- [俄罗斯](Russia.md)之下的[俄美公司](Alaska.md)

通过 Charters of Commerce DLC，可以向一家公司授予殖民权利来建立新的特许公司。一旦该公司完全殖民一个州区域，它就会转变为特许公司附属国。

或者，建立新的[殖民行政机构](Colonization.md)时可以选择将该附属国转变为特许公司。在这种情况下，该国是一个普通附属国，没有额外的机制或加成，对其自己的公司或附属国机制也没有限制。

### 殖民地（Colonies）

殖民地是一种特殊的附属国类型，代表殖民帝国的海外行政单位。某些国家，如[古巴](Cuba.md)或[上加拿大](Ontario.md)，在游戏开始时即以殖民地形式存在；获得殖民地附属国的唯一其他途径是通过[建立殖民行政机构](Colonization.md)日志条目，该条目在研究完成*开化使命*后激活，且仅适用于非洲殖民地。

游戏开始时存在以下殖民地：

- [大不列颠](Great Britain.md)之下的[英属西非](Sierra Leone.md)、[开普殖民地](South Africa.md)、[锡兰](Ceylon.md)、[哥伦比亚地区](Oregon.md)、[下加拿大](Quebec.md)、[新不伦瑞克](New Brunswick.md)、[新南威尔士](New South Wales.md)、[新斯科舍](Nova Scotia.md)、[南澳大利亚](South Australia.md)、[上加拿大](Ontario.md)、[范迪门斯地](Tasmania.md)和[西澳大利亚](Western Australia.md)
- [西班牙](Spain.md)之下的[古巴](Cuba.md)、[波多黎各](Puerto Rico.md)和[菲律宾](Philippines.md)

殖民地始终采用殖民行政机构法律，除非提高自治权，否则不能更改该法律。此外，某些殖民地——包括通过[建立殖民行政机构](Colonization.md)日志条目建立的殖民地——拥有附属地位法律的殖民种族化（）修正案，该修正案降低对没有共享传承特质的文化接受度，但作为回报，大幅提高与主文化共享特质的文化接受度。

#### 殖民地独立

任何拥有殖民行政机构法律的国家（无论是特许公司、自治领还是殖民地）如果获得独立（[东印度公司](https://vic3.paradoxwikis.com/East_India_Company)、[东印度群岛](East Indies.md)、[俄美公司](Alaska.md)以及通过[建立殖民行政机构](Colonization.md)日志条目建立的任何国家除外，它们有各自的事件），都会收到以下事件，允许其选择新的治理原则法律。

id

### 独立日

昔日统治我们领土的旧殖民结构对一个独立国家来说远远不够。我们必须为一个自由独立的[国家]奠定基础。
---

背景文本：
总督离开前没来得及收拾他的家具。他的餐厅里摆放着六把精美的欧式椅子，围着一张桌子——逃跑的前任占用者匆忙地拿走了桌上的银器和丝绸桌布。如今那些精美的椅子上坐着六位体面的绅士。其中一些人曾有幸受邀参加总督的晚宴，以前来过这里。其余的人则更粗犷、更新来。如果这里有谁打算提出什么大胆的主张，那一定是他们中的一个。
---

| 触发条件：成为独立国家 |
|---|
| 触发条件：已制定殖民行政机构 以下均不满足：是东印度公司 是东印度群岛 是俄美公司 是通过建立殖民行政机构日志条目建立的 |
| 选项条件 始终可用：[立法机构]将是最高权威。制定议会共和制 始终可用：我们将建立一个共和制国家。制定总统共和制 满足条件时可用：最强政府利益集团支持君主制 [统治者]将戴上王冠，只要[他]愿意。制定君主制 满足条件时可用：最强政府利益集团支持企业国家 阶级联盟将维护我们的独立。制定企业国家 满足条件时可用：最强政府利益集团支持委员会共和制 是无产阶级为我们赢得了胜利。制定委员会共和制 满足条件时可用：最强政府利益集团支持神权制 [国家]将受神意指引。制定神权制 所有选项 若尚未受承认则成为受承认国家 |

## 建立附属国

国家可以通过外交博弈 targeting 其他国家，使其成为保护国、自治领或朝贡国，前提是发起国等级更高，且目标国低于（未受承认的）主要政权。

附属国也可以通过从拥有的州中[释放](Releasable countries.md)国家来创建，此时附属国类型取决于释放者的受承认状态以及被释放国家的类型，如下表所示。

| 国家类型 | 宗主国受承认状态 |  |
|---|---|---|
| 受承认 | 未受承认 |  |
| 受承认 | 傀儡国 | 附庸国 |
| 未受承认 |  |  |
| 殖民 | 殖民地 |  |

### 附属国转移

附属国可以通过几种方式更换宗主国。最常见的是某一宗主国以*转移附属国*战争目标 targeting 该附属国。该战争目标不能用于针对君合国[5]。另外，如果拥有附属国的国家成为非自治附属国，其附属国也会转移给新的宗主国。
如果宗主国从未被承认变为已承认，或反之——例如某国成为已承认国家或附属国转移的结果——附属国的类型将按下表变化。

| 附属国类型 | 新宗主国 |  |
|---|---|---|
|  | 已承认 | 未被承认 |
| 傀儡国 | — | 附庸国 |
| 殖民地 |  |  |
| 王室领地 |  |  |
| 自治领 | — | 朝贡国[6] |
| 特许公司 |  |  |
| 保护国 | — | 朝贡国 |
| 附庸国 | 傀儡国 殖民地[7] | — |
| 朝贡国 | 保护国 自治领[7] | — |

## 附属国互动

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助验证或更新此部分内容。其最后验证版本为 1.10。 |
|---|---|

参见：
外交
以下行动与条约通常用于附属国与其宗主国之间。其中部分行动也可由强权集团的领导者对其成员使用。除非另有说明，影响力花费仅由宗主国或集团领导者支付。

| 条约 | 花费 | 条件 | 效果 | 自动破裂条件 |
|---|---|---|---|---|
| 提高贡赋 | 25 | 启用“势力范围” 目标是行动者的附属国 目标未在外交博弈中对抗行动者 目标与行动者之间存在某种形式的收入转移 目标不是保护国或君合国 目标独立倾向低于 75 目标未违约 未与目标签订“降低贡赋” | 目标每周获得 +0.1 独立倾向 目标向宗主国缴纳的收入增加 10% 不包括关税或与宗主国的外交条约 目标可在独立倾向达到 75 或以上时破裂 | 目标在外交博弈中对抗行动者 目标与行动者之间不存在某种形式的收入转移 |
| 降低贡赋 | 0 | 启用“势力范围” 目标是行动者的附属国 目标未在外交博弈中对抗行动者 目标与行动者之间存在某种形式的收入转移 目标不是保护国或君合国 未与目标签订“提高贡赋” | 目标向宗主国缴纳的收入减少 10% 不包括关税或与宗主国的外交条约 目标每周 −0.05 独立倾向 一年内不可破裂 若手动破裂，目标获得 +10 独立倾向 | 目标在外交博弈中对抗行动者 目标与行动者之间不存在某种形式的收入转移 |
| 免除服役义务 | 0 | 行动者是目标的宗主国或集团领导者 目标未在外交博弈中对抗行动者 目标须加入行动者的外交博弈 | 目标不再须加入行动者的外交博弈 若目标是行动者的附属国，每周 −0.05 独立倾向 一年内不可破裂 若手动破裂且目标是行动者的附属国，目标获得 +10 独立倾向 | 行动者不再是目标的宗主国或集团领导者 |
| 授予独立市场 | 0 | 目标是行动者市场的成员 目标未在外交博弈中对抗行动者 目标是独立国家或行动者的直属附属国 | 目标获得独立市场 授予时，若目标是行动者的附属国，独立倾向变化 +50 至 −20，取决于经济依赖度 一年内不可破裂 若手动破裂且目标是行动者的附属国，目标获得 +25 独立倾向 | 行动者不再是目标的直属宗主国或集团领导者 |
| 知识共享 | 50 | 启用“势力范围” 行动者是目标的宗主国或集团领导者 目标未在外交博弈中对抗行动者 | 目标获得 +25% 技术扩散 行动者获得 −10% 技术扩散 若目标是行动者的附属国，目标每周获得 −0.05 独立倾向 开始时，目标的宗主国游说集团的绥靖度变化 ±2 一年内不可破裂 若手动破裂，目标获得 +10 独立倾向 目标的宗主国游说集团的绥靖度变化 ±2 | 行动者不再是目标的直属宗主国或集团领导者 行动者已研究的技术不多于目标 |
| 请求市场控制权 | 0 | 行动者是目标市场的成员 目标未在外交博弈中对抗行动者 行动者属于以下情况之一： 独立国家 目标的直属附属国且独立倾向达到 25 或以上 5 年内未请求过市场控制权 | 若目标同意，与目标获得 +10 关系 行动者获得独立市场 若行动者是目标的附属国，失去 −30 独立倾向 若目标拒绝，与目标失去 −20 关系 若行动者是目标的附属国，获得 +10 独立倾向 若破裂，与目标失去 −10 关系 | 目标不再是行动者的直属宗主国或集团领导者 |
| 传教 | 25 | 启用“势力范围” 行动者的国教不是无神论 行动者已制定“国教”法律 目标是行动者的附属国 目标与行动者有相同的国教 目标未在外交博弈中对抗行动者 | 目标获得 +50% 皈依速度 开始时，目标获得 +10 独立倾向，除非目标满足以下任一条件： 已制定“国教”法律 虔信派在政府中 任一利益集团由传统主义者或神权主义者领袖执政且在政府中 否则目标失去 −10 独立倾向 一年内不可破裂 若手动破裂，目标按开始时的反向条件获得 ±10 独立倾向 |  |
| 支持政权 | 50 | 目标未在外交博弈中对抗行动者 目标的合法性低于 75 目标是行动者的附属国 | 目标获得： +20 合法性 −10% 政治运动活跃度 每周 −0.1 独立倾向 行动者失去 −10 合法性 开始时，目标的宗主国游说集团的绥靖度变化 ±4 一年内不可破裂 若手动破裂，目标获得 +10 独立倾向 目标的宗主国游说集团的绥靖度变化 ±4 |  |

| 行动 | 条件 | 效果 |
|---|---|---|
| 任命殖民地总督 | 启用“势力范围” 目标是行动者的附属国 目标未在外交博弈中对抗行动者 5 年内未任命或请求过新总督类型 目标已制定“殖民管理”机构 若行动者是未被承认国家，目标是附庸国 若行动者是已承认国家，目标是未被承认国家，或不是保护国或君合国 | 行动者为目标选择一位新统治者 可从以下选项中选择： • 有影响力的种植园主（ ） • 本地任命官员，拥有该附属国的主流文化与宗教（而非宗主国的） • 经验丰富的榨取者（ ） • 杰出商人（ ）• 军事总督（ ） 总督任期为 4 年，之后自动由一名拥有相同独有特质的任务接替 |
| 请求殖民地总督 | 启用“势力范围” 目标是行动者的直属宗主国 目标未在外交博弈中对抗行动者 5 年内未任命或请求过新总督类型 行动者已制定“殖民管理”机构 若行动者是附庸国，目标是未被承认国家 行动者不是保护国或君合国 | 行动者获得 modifier：已请求殖民地总督 已请求殖民地总督 国家 modifier −0.1 每周独立倾向，持续 5 年 行动者选择一位新统治者 可从以下选项中选择： • 有影响力的种植园主（ ） • 本地任命官员，拥有该附属国的主流文化与宗教（而非宗主国的） • 经验丰富的榨取者（ ） • 杰出商人（ ） • 军事总督（ ） 总督任期为 4 年，之后自动由一名拥有相同独有特质的任务接替 |
| 更改行政语言 | 启用“势力范围” 目标是行动者的附属国 目标未在外交博弈中对抗行动者 行动者已制定“殖民管理”机构 目标的所有主流文化均不满足以下任一条件： 与宗主国的主流文化相同 与宗主国的文化共享语言特质 | 附属国中先前主流文化的人口有 10% 变得更加激进 所有先前的主流文化从目标国家中移除 该附属国获得宗主国的所有主流文化 • 若该国首都位于加拿大区域且宗主国拥有法语语言特质 • 将附属国的主流文化改为法裔加拿大人 • 若该国首都位于加拿大区域且宗主国拥有英语语言特质 • 将附属国的主流文化改为英裔加拿大人 • 若该国是南非且宗主国拥有荷兰语语言特质 • 将附属国的主流文化改为布尔人 附属国首都 5% 的官僚转变为新的主流文化附属国获得“已更改行政语言” 已更改行政语言 国家 modifier −20% 行政力 −25% 机构规模变更速度（衰减），持续 5 年附属国首都所在州获得“更换行政人员” 更换行政人员 州 modifier +75% 同化（衰减），持续 5 年 |
| 降低自治度 | 目标是行动者的直属附属国 目标未在外交博弈中对抗行动者 目标独立倾向低于 25 目标的自治度可以降低，即不是傀儡国或附庸国 目标不是君合国，或行动者已研究“民族主义” 目标不是特许公司，或行动者已研究“文明使命” 目标的自治度在 5 年内未发生变化 | 目标的自治度降低一级 目标获得 +50 独立倾向 行动者的所有其他直属附属国获得 +10 独立倾向 与目标建立 5 年休战 |
| 提升自治度 | 目标是行动者的直属附属国 目标未在外交博弈中对抗行动者 目标的自治度可以提升，即不是保护国或朝贡国 目标不是君合国，或行动者已研究“民族主义” 目标不是特许公司，或行动者已研究“文明使命” 目标的自治度在 5 年内未发生变化 | 目标的自治度提升一级 目标失去 −30 独立倾向 与目标建立 5 年休战 |
| 请求提升自治度 | 目标是行动者的直属宗主国 目标未在外交博弈中对抗行动者 行动者独立倾向达到 75 或以上 行动者的自治度可以提升，即不是保护国或朝贡国 行动者不是君合国，或已研究“民族主义” 行动者不是特许公司，或已研究“文明使命” 行动者的自治度在 5 年内未发生变化 5 年内未请求过提升自治度 | 若目标同意，行动者的自治度提升一级 行动者失去 −30 独立倾向 与目标建立相互 5 年休战 与目标失去 −20 关系 若目标拒绝，行动者获得 +10 独立倾向 与目标失去 −30 关系 行动者获得在 5 年内要求提升自治度的能力 |
| 请求支持政权 | 目标未在外交博弈中对抗行动者 目标是行动者的宗主国 5 年内未请求过支持政权 | 若目标同意，目标与行动者建立“支持政权”条约 若目标拒绝，与目标失去 −20 关系 获得 +10 独立倾向 |
| 请求知识共享 | 启用“势力范围” 目标是行动者的宗主国 目标未在外交博弈中对抗行动者 5 年内未请求过知识共享 | 若目标同意，目标与行动者建立“知识共享”条约 若目标拒绝，与目标失去 −20 关系 获得 +10 独立倾向 |
| 授予州 | 目标是行动者的附属国 双方均未处于战争或外交博弈承诺中 行动者拥有一个有效的州 该州不是首都或殖民地 该州不是已整合的主流文化故土 可以是另一可吞并附属国（王室领地、傀儡国、殖民地或附庸国）拥有的州 满足以下任一条件： 该州与目标相邻 该州是目标主流文化的沿海故土且目标拥有一个可供授予的沿海州 | 目标获得该州 目标失去 −5 至 −50 独立倾向，取决于该州的价值 若该州原属另一附属国，该附属国获得 +20 至 +100 独立倾向，取决于该州的价值 |
| 夺取州 | 目标是行动者的可吞并附属国（王室领地、傀儡国、殖民地或附庸国） 目标未处于战争或外交博弈承诺中 目标独立倾向低于 25 目标拥有一个可夺取的有效州： 该州不是首都或殖民地 该州未整合，或目标不是自治领 | 行动者获得该州 目标获得 +20 至 +100 独立倾向，取决于该州的价值 与目标制造事端，获得 10 至 50 恶名，取决于该州的价值 |
| 索取州 | 目标是行动者的宗主国 双方均未处于战争或外交博弈承诺中 目标拥有一个有效的州 该州不是首都或殖民地 该州不是目标的已整合州 该州不是拥有者主流文化的故土 可以是目标另一可吞并附属国（王室领地、傀儡国、殖民地或附庸国）拥有的州 满足以下任一条件： 该州与行动者相邻 该州是行动者主流文化的沿海故土且行动者拥有一个可供授予的沿海州 | 若目标同意，行动者获得该州 行动者失去 −5 至 −50 独立倾向，取决于该州的价值 若该州原属另一附属国，该附属国获得 +20 至 +100 独立倾向，取决于该州的价值 |
| 强制军事通行 | 目标是行动者的附属国 行动者处于战争中 目标未在战争或外交博弈中对抗行动者 目标未加入行动者的所有战争 | 目标作为盟友加入行动者的所有战争 目标获得 +10 独立倾向 若目标是保护国或朝贡国，则改为获得 +20 |
| 行使“丧失权利原则” | 是东印度公司 未触发事件“公司的终结” 处于和平状态 两年内未行使过“丧失权利原则” 目标是 AI 附属国土邦 目标不是帝国级国家 | 对目标制造事端，获得 20 恶名 与每个土邦失去 −10 关系 每个土邦获得最多 25 独立倾向，取决于目标的威望 目标触发事件“丧失权利原则被行使” 可选择被吞并或为独立而战 若被吞并，向东印度公司转移黄金储备 |

## 参考

1. ↑ 1.0 1.1 存在错误，始终使用最低值
2. ↑ 存在错误，无法低于 0
3. ↑ 3.0 3.1 存在错误，可能应为东印度公司（BIC）或作为英属印度统治的印度（BHT）
4. ↑ 目前，如果宗主国与附属国属于不同类型，即已承认、未被承认、殖民地或公司，附属国不会被吞并，也不会割让相关州。
5. ↑ 未被承认国家也无法以保护国为目标，但这似乎是一个错误。
6. ↑ 由于缺乏明确定义的关系，尚不明确
7. ↑ 7.0 7.1 若该附属国为殖民地国家

1. /Victoria 3/game/common/subject_types/00_subject_types.txt
2. /Victoria 3/game/common/diplomatic_actions
3. /Victoria 3/game/common/diplomatic_plays

游戏概念
返回顶部
| 人口 | [人口](Pops.md) • [接受度](Acceptance.md) • [文化](Culture.md) • [迁移](Migration.md) • [需求](Needs.md) • [职业](Profession.md) • [宗教](Religion.md) • [生活水平](Standard of living.md) |
|---|---|

| 政府 | [政府](Government.md) • [能力](Capacity.md) • [人物](Character.md) • [法令](Decrees.md) • [机构](Institutions.md) • [法律](Laws.md) • [技术](Technology.md) |
|---|---|

| 政治 | [选举](Elections.md) • [意识形态](Ideology.md) • [利益集团](Interest group.md) • [政治游说集团](Political lobby.md) • [政治运动](Political movement.md) • [政党](Political party.md) • [革命](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| 经济 | [建筑](Building.md) • [商品](Goods.md) • [收成状况](Harvest condition.md) • [基础设施](Infrastructure.md) • [市场](Market.md) • [生产方式](https://vic3.paradoxwikis.com/Production_methods) • [州](State.md) • [国库](Treasury.md) |
|---|---|

| 外交 | [外交](Diplomacy.md) • [外交行动](https://vic3.paradoxwikis.com/Diplomatic_action) • [外交博弈](Diplomatic play.md) • [强权集团](Power bloc.md) • [国家等级](Rank.md) • 附属国 • [条约](Treaty.md) |
|---|---|

| 战争 | [战争](Warfare overview.md) • [陆战](Land warfare.md) • [海战](Naval warfare.md) • [战争目标](https://vic3.paradoxwikis.com/Wargoal) • [征兵](https://vic3.paradoxwikis.com/Conscription) |
|---|---|
| 其他 | [国家](Countries.md) • [决议](Decision.md) • [事件](Events.md) • [日志](Journal.md) • [目标](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|