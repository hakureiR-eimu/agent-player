---
title: Subject
source: https://vic3.paradoxwikis.com/Subject
pageid: 3146
categories: [1.13, Articles_with_potentially_outdated_sections, Diplomacy]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

Diplomacy
Diplomatic actions
Diplomatic plays
Power blocs
Subjects
Treaties
A **subject** is a country which is subordinate to another country (the *overlord* or *suzerain*). They have internal autonomy with limited interference from their overlord. Subjects have their own budget, construction sector, [interest groups](https://vic3.paradoxwikis.com/Interest_groups), [laws](Laws.md), and institutions but are limited when conducting external diplomacy. All subject types automatically join their overlord's [market](Market.md) as a junior member.

## General mechanics

Subjects are a type of [diplomatic pact](https://vic3.paradoxwikis.com/Diplomatic_pact), and the overlord must pay an ongoing 10 influence cost to maintain them. All subject types except personal unions must be a lower [rank](Rank.md) than their overlord; no subject type can be a great power or major power. For example, [British East India Company](East India.md) is a minor power at the start of the game because they are a subject of [Great Britain](Great Britain.md), despite having more prestige than the [United States of America](America.md), a great power. Subjects of all kinds join and leave [power blocs](Power bloc.md) with their overlord.

Additionally, subjects have other restrictions or obligations, varying by type, such as paying a portion of their government income to the overlord, being unable to start their own diplomatic plays, or being forced to join the side of their overlord in [diplomatic plays](https://vic3.paradoxwikis.com/Diplomatic_plays). However, they also receive a degree of protection, as the overlord is automatically called into diplomatic plays targeting the subject. However, subjects are not protected by their overlord if they join a diplomatic play targeting another country.

Some subject types are autonomous, meaning they can engage in most diplomacy with nations other than their overlord and even have subjects of their own. The primary diplomatic restriction is that autonomous subjects and their overlords cannot use most war goals against each other. It is possible for an autonomous subject, such as a dominion, and its overlord to be at war with one another by backing opposing sides in a diplomatic play. Even in this case, the subject pact remains with all of its usual features. Provided independence was not demanded in the war, the subject and overlord return to normal relations after the war.

If the overlord initiates or is directly targeted by a diplomatic play, non-autonomous subjects and dominions automatically join the play. If the overlord joins another play, even when defending one of its subjects, its other subjects do not automatically join the play.

Overlords can initiate [law](https://vic3.paradoxwikis.com/Law) changes in their subjects, with all of the usual requirements to enact a law. Overlords also gain prestige from a portion of their subjects' GDP (50%), and army (1.67%) and navy (10%) power projection; this does not reduce the amount of prestige the subjects gain from those sources.

### Liberty desire

*Liberty desire* represents part of a subject's willingness to go along with their overlord's wishes or demands, or conversely its desire for greater autonomy or even independence.

Liberty desire ranges from 0 to 100, with three grouped levels: *low*, *moderate*, and *high*.

| Level | Low | Moderate | High |
|---|---|---|---|
| Range | 0 – 24.9 | 25 – 74.9 | 75 – 100 |
| Effects | −10% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility statuses +25% Loyalists from movements | — | +10% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility statuses +25% Radicals from movements |

An overlord can decrease autonomy for subjects with less than 25 liberty desire, as long as a less autonomous subject type is available.

Overlords can also increase autonomy of most subjects. Subjects with 75 or more liberty desire can also request an increase in autonomy. As with decreasing autonomy, there must be a more autonomous type available.

Certain subject types have additional requirements to change autonomy, namely that the requester has researched a specific technology:

- Personal Unions require *Nationalism*
- [Chartered Companies](Government type.md) require *Civilizing Mission*

Autonomy can only be changed once every 5 years.

Subjects denied an autonomy increase within the last 5 years can demand either to increase autonomy or attempt to gain independence as a [diplomatic play](Diplomatic play.md). Subjects at the highest autonomy can also demand independence at any time.

### Weekly liberty desire

Liberty desire changes each week according to the following factors. Multipliers are calculated after summing flat and scaling sources

| Source | Effect |
|---|---|
| Base | +0.1 |
| Relations are hostile | +0.5 |
| Relations are cold | +0.25 |
| Relations are poor | +0.1 |
| Relations are neutral | +0 |
| Relations are cordial | −0.025 |
| Relations are amicable | −0.05 |
| Relations are friendly | −0.1 |
| Overlord is infamous | +0.1 |
| Overlord is notorious | +0.25 |
| Overlord is pariah | +2.0 |
| Has Knowledge Sharing | −0.05 |
| Has Exempt from Service | −0.05 |
| Has Raise Payments | +0.1 |
| Has Decrease Payments | −0.05 |
| Has Support Regime | −0.1 |
| Is isolated from overlord's market | +1.0 |
| In power bloc with Sacred Civics II Has same religion as overlord | −0.1 |
| Overlord has less than 1 prestige | +1.0 |
| Subject has less than 1 prestige | −0.1 |
| Overlord has less than 1 army power projection | +1.0 |
| Subject has less than 1 army power projection | −0.25 |
| Weekly liberty desire modifiers | Varies |
| Is a Chartered Company | −0.2 |
| Is East Indies Overlord is Netherlands | −0.2 |
| Is a Zhuz Overlord has Pacify the Steppes journal entry | −0.2 |
| Overlord has Isolationism or a variant | +2.0 |

| Source | Formula |
|---|---|
| Does not have Subjecthood Shares no primary culture with overlord | − − 0.1 ≤ ≤ ± ± highest primary culture fervor − − 25 150 ≤ ≤ + 0.5 {\displaystyle -0.1\leq \pm {\tfrac {{\text{highest primary culture fervor}}-25}{150}}\leq +0.5} ![{\displaystyle -0.1\leq \pm {\tfrac {{\text{highest primary culture fervor}}-25}{150}}\leq +0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/fc9683cfc6198a4a266158f06239a23d09826f4e) |
| Shares all primary cultures with overlord | − − 0.2 ≤ ≤ − − primary culture fervor − − 25 150 ⋅ ⋅ num primary cultures ≤ ≤ − − 0.05 {\displaystyle -0.2\leq -{\tfrac {{\text{primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}\leq -0.05} ![{\displaystyle -0.2\leq -{\tfrac {{\text{primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}\leq -0.05}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/0c087b69568c1d6f10f14847474c19347b2f9ae3)[1] |
| Has Subjecthood Shares some primary cultures with overlord | − − 0.25 ≤ ≤ − − primary culture fervor − − 25 150 ⋅ ⋅ num primary cultures ≤ ≤ 0 {\displaystyle -0.25\leq -{\tfrac {{\text{primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}\leq 0} ![{\displaystyle -0.25\leq -{\tfrac {{\text{primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}\leq 0}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/387bff53dde0f52b86841796202015620a6d20e9)[1] |
| Does not have Subjecthood Shares some primary cultures with overlord | − − 0.25 ≤ ≤ + unshared primary culture fervor − − 25 150 ⋅ ⋅ num primary cultures − − shared primary culture fervor − − 25 150 ⋅ ⋅ num primary cultures ≤ ≤ + 0.5 {\displaystyle -0.25\leq +{\tfrac {{\text{unshared primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}-{\tfrac {{\text{shared primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}\leq +0.5} ![{\displaystyle -0.25\leq +{\tfrac {{\text{unshared primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}-{\tfrac {{\text{shared primary culture fervor}}-25}{150\cdot {\text{num primary cultures}}}}\leq +0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/038a618e1b961bde615833b29ae527cab75b00c8)[2] |
| Is a protectorate or tributary Overlord has more than 1.5 times more prestige | − − 0.05 ≤ ≤ − − overlord prestige subject prestige ⋅ ⋅ 150 ≤ ≤ − − 0.01 {\displaystyle -0.05\leq -{\tfrac {\text{overlord prestige}}{{\text{subject prestige}}\cdot 150}}\leq -0.01} ![{\displaystyle -0.05\leq -{\tfrac {\text{overlord prestige}}{{\text{subject prestige}}\cdot 150}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/f0df5c313c93b11abc8a57ea88be1bba5cec0bea) |
| Is a protectorate or tributary Overlord has less than 1.5 times more prestige | + overlord prestige subject prestige ⋅ ⋅ 1.5 3 ≤ ≤ + 2.5 {\displaystyle +{\tfrac {\text{overlord prestige}}{\text{subject prestige}}}\cdot {\tfrac {1.5}{3}}\leq +2.5} ![{\displaystyle +{\tfrac {\text{overlord prestige}}{\text{subject prestige}}}\cdot {\tfrac {1.5}{3}}\leq +2.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/10cf835c68b15a774e3b6ff90c06003f82120c42) |
| Is a dominion, personal union, or chartered company Overlord has more than 2 times more prestige | − − 0.05 ≤ ≤ − − overlord prestige subject prestige ⋅ ⋅ 200 ≤ ≤ − − 0.01 {\displaystyle -0.05\leq -{\tfrac {\text{overlord prestige}}{{\text{subject prestige}}\cdot 200}}\leq -0.01} ![{\displaystyle -0.05\leq -{\tfrac {\text{overlord prestige}}{{\text{subject prestige}}\cdot 200}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/6a19d037d6e12539e9b7172f649a2b11c91961e8) |
| Is a dominion, personal union, or chartered company Overlord has less than 2 times more prestige | + overlord prestige subject prestige ⋅ ⋅ 2 5 ≤ ≤ + 0.5 {\displaystyle +{\tfrac {\text{overlord prestige}}{\text{subject prestige}}}\cdot {\tfrac {2}{5}}\leq +0.5} ![{\displaystyle +{\tfrac {\text{overlord prestige}}{\text{subject prestige}}}\cdot {\tfrac {2}{5}}\leq +0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/a58d97c8e7ff0ce1947d4bdf0347b06760261e79) |
| Is an annexable subject Crown land, Puppet, Colony, or Vassal Overlord has more than 3 times more prestige | − − 0.1 ≤ ≤ − − overlord prestige subject prestige ⋅ ⋅ 300 ≤ ≤ − − 0.01 {\displaystyle -0.1\leq -{\tfrac {\text{overlord prestige}}{{\text{subject prestige}}\cdot 300}}\leq -0.01} ![{\displaystyle -0.1\leq -{\tfrac {\text{overlord prestige}}{{\text{subject prestige}}\cdot 300}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/8157831d958efe8485d895e8a10a5b99e4376616) |
| Is a annexable subject Crown land, Puppet, Colony, or Vassal Overlord has less than 3 times more prestige | + overlord prestige subject prestige ⋅ ⋅ 5 ≤ ≤ + 0.5 {\displaystyle +{\tfrac {\text{overlord prestige}}{{\text{subject prestige}}\cdot 5}}\leq +0.5} ![{\displaystyle +{\tfrac {\text{overlord prestige}}{{\text{subject prestige}}\cdot 5}}\leq +0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/e66b398a0ca5ae053ffb3b87b2305671e62bf434) |
| Is East India , East Indies , or Rajputana [3] Overlord has more than 10 times more army power projection | − − 0.1 ≤ ≤ − − overlord army power projection subject army power projection ⋅ ⋅ 250 ≤ ≤ − − 0.01 {\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 250}}\leq -0.01} ![{\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 250}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/8cad98cc39dcac8564c9630ad840069a44e6f358) |
| Is East India , East Indies , or Rajputana [3] Overlord has less than 10 times more army power projection | + subject army power projection ⋅ ⋅ 10 overlord army power projection ⋅ ⋅ 10 ≤ ≤ + 0.25 {\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 10}{{\text{overlord army power projection}}\cdot 10}}\leq +0.25} ![{\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 10}{{\text{overlord army power projection}}\cdot 10}}\leq +0.25}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/7b048b019217008051f1f7640078b5ea6315d29b) |
| Is a protectorate or tributary Overlord has more than 5 times more army power projection | − − 0.1 ≤ ≤ − − overlord army power projection subject army power projection ⋅ ⋅ 100 ≤ ≤ − − 0.01 {\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 100}}\leq -0.01} ![{\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 100}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/907ae94aa0b9e32ea32548d58e499a00a8026589) |
| Is a protectorate or tributary Overlord has less than 5 times more army power projection | + subject army power projection ⋅ ⋅ 5 overlord army power projection ⋅ ⋅ 10 ≤ ≤ + 0.5 {\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 5}{{\text{overlord army power projection}}\cdot 10}}\leq +0.5} ![{\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 5}{{\text{overlord army power projection}}\cdot 10}}\leq +0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/290b01ee7955755d4ccd4d36a9e513dafaf1ca8d) |
| Is a dominion, personal union, or chartered company Overlord has more than 7.5 times more army power projection | − − 0.1 ≤ ≤ − − overlord army power projection subject army power projection ⋅ ⋅ 175 ≤ ≤ − − 0.01 {\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 175}}\leq -0.01} ![{\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 175}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/0856a6a6cafd4d0587d1ba14f17a340c57db014b) |
| Is a dominion, personal union, or chartered company Overlord has less than 7.5 times more army power projection | + subject army power projection ⋅ ⋅ 7.5 overlord army power projection ⋅ ⋅ 10 ≤ ≤ + 0.5 {\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 7.5}{{\text{overlord army power projection}}\cdot 10}}\leq +0.5} ![{\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 7.5}{{\text{overlord army power projection}}\cdot 10}}\leq +0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/f1ff370a9fd5df7fe4c32b10ed5a1b5ed9ff7673) |
| Is an annexable subject Crown land, Puppet, Colony, or Vassal Overlord has more than 10 times more army power projection | − − 0.1 ≤ ≤ − − overlord army power projection subject army power projection ⋅ ⋅ 250 ≤ ≤ − − 0.01 {\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 250}}\leq -0.01} ![{\displaystyle -0.1\leq -{\tfrac {\text{overlord army power projection}}{{\text{subject army power projection}}\cdot 250}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/8cad98cc39dcac8564c9630ad840069a44e6f358) |
| Is a annexable subject Crown land, Puppet, Colony, or Vassal Overlord has less than 10 times more army power projection | + subject army power projection ⋅ ⋅ 10 overlord army power projection ⋅ ⋅ 10 ≤ ≤ + 0.5 {\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 10}{{\text{overlord army power projection}}\cdot 10}}\leq +0.5} ![{\displaystyle +{\tfrac {{\text{subject army power projection}}\cdot 10}{{\text{overlord army power projection}}\cdot 10}}\leq +0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/76968cf9eb9ef578d2dc11f117c9d9ec804bedad) |
| Overlord is a subject Overlord's overlord has more than 10 times more army power projection | − − 0.1 ≤ ≤ − − overlord's overlord army power projection subject army power projection ⋅ ⋅ 250 ≤ ≤ − − 0.01 {\displaystyle -0.1\leq -{\tfrac {\text{overlord's overlord army power projection}}{{\text{subject army power projection}}\cdot 250}}\leq -0.01} ![{\displaystyle -0.1\leq -{\tfrac {\text{overlord's overlord army power projection}}{{\text{subject army power projection}}\cdot 250}}\leq -0.01}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/3910eb8a21ff47b591f56e8e842e63f5aa6cea76) |
| Overlord's alliances and defensive pacts | − − 0.25 ≤ ≤ − − ∑ ∑ ( 0.1 ⋅ ⋅ num of great power allies ) ( num of major power allies ⋅ ⋅ 0.05 ) ( num of minor power allies ⋅ ⋅ 0.03 ) ( num of unrecognized major power allies ⋅ ⋅ 0.03 ) ( num of great power defensive pacts ⋅ ⋅ 0.05 ) ( num of major power defensive pacts ⋅ ⋅ 0.03 ) ≤ ≤ 0 {\displaystyle -0.25\leq -\sum {\begin{aligned}&(0.1\cdot {\text{num of great power allies}})\\&({\text{num of major power allies}}\cdot 0.05)\\&({\text{num of minor power allies}}\cdot 0.03)\\&({\text{num of unrecognized major power allies}}\cdot 0.03)\\&({\text{num of great power defensive pacts}}\cdot 0.05)\\&({\text{num of major power defensive pacts}}\cdot 0.03)\end{aligned}}\leq 0} ![{\displaystyle -0.25\leq -\sum {\begin{aligned}&(0.1\cdot {\text{num of great power allies}})\\&({\text{num of major power allies}}\cdot 0.05)\\&({\text{num of minor power allies}}\cdot 0.03)\\&({\text{num of unrecognized major power allies}}\cdot 0.03)\\&({\text{num of great power defensive pacts}}\cdot 0.05)\\&({\text{num of major power defensive pacts}}\cdot 0.03)\end{aligned}}\leq 0}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/142d662236cb210918493f29a55c28a5159ae857) |
| Clout of pro-overlord lobby members in government | − − clout ⋅ ⋅ 0.5 {\displaystyle -{\text{clout}}\cdot 0.5} ![{\displaystyle -{\text{clout}}\cdot 0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/453aca8d9bf23b4bcef63f2f359433956fdafd92) |
| Clout of pro-overlord lobby members in opposition | − − clout ⋅ ⋅ 0.25 {\displaystyle -{\text{clout}}\cdot 0.25} ![{\displaystyle -{\text{clout}}\cdot 0.25}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/42ab43f187c6a5be8a0cdb963dcc6eba5d17828d) |
| Clout of anti-overlord lobby members in government | + clout ⋅ ⋅ 0.5 {\displaystyle +{\text{clout}}\cdot 0.5} ![{\displaystyle +{\text{clout}}\cdot 0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/c0f8a49122aaf2a756f4b8e5c3b733bfad64181d) |
| Clout of anti-overlord lobby members in opposition | + clout ⋅ ⋅ 0.25 {\displaystyle +{\text{clout}}\cdot 0.25} ![{\displaystyle +{\text{clout}}\cdot 0.25}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/543c7d89e467b022af4ea36f87bea1294853b275) |
| Economic dependence of subject is more than 0 | ( 1 − − economic dependence ) ⋅ ⋅ 1 10 {\displaystyle (1-{\text{economic dependence}})\cdot {\tfrac {1}{10}}} ![{\displaystyle (1-{\text{economic dependence}})\cdot {\tfrac {1}{10}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/04454d232b82fc687a32671143bbfafc0b1a2f9e) |
| Economic dependence of subject is less than 0 | ( 1 − − economic dependence ) ⋅ ⋅ 1 3 {\displaystyle (1-{\text{economic dependence}})\cdot {\tfrac {1}{3}}} ![{\displaystyle (1-{\text{economic dependence}})\cdot {\tfrac {1}{3}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/15faf61f4513b3d0bc6d08bea60e765bbbfd6263) |
| Subject is part of overlord's market Subject has port Subject is not adjacent to overlord Overlord's supply network is less than 100% | 1 − − overlord supply network {\displaystyle 1-{\text{overlord supply network}}} ![{\displaystyle 1-{\text{overlord supply network}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/15957ce38f918de5eb0b40d4a59f7370647654fb) |

| Source | Formula |
|---|---|
| **Scaled multipliers**, *applied first* |  |
| Negative weekly liberty desire Liberty desire below 50 Cannot reduce weekly liberty desire below −0.01 | × × liberty desire 50 {\displaystyle \times {\frac {\text{liberty desire}}{50}}} ![{\displaystyle \times {\frac {\text{liberty desire}}{50}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/a7a7857b602f4f13f787fd042cee41ed86302726) |
| Positive weekly liberty desire Liberty desire above 50 Cannot reduce weekly liberty desire below +0.01 | × × 100 − − liberty desire 50 {\displaystyle \times {\frac {100-{\text{liberty desire}}}{50}}} ![{\displaystyle \times {\frac {100-{\text{liberty desire}}}{50}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/2784923acfa7e0100adb698f157243cf736c6b79) |
| **Modifier multipliers**, *applied second* |  |
| Positive weekly liberty desire Sum of liberty desire increase multipliers | Varies |
| Negative weekly liberty desire Sum of liberty desire decrease multipliers | Varies |
| **Truce multiplier**, *applied third* |  |
| Positive weekly liberty desire Subject has truce with overlord | × × 0.5 {\displaystyle \times 0.5} ![{\displaystyle \times 0.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/bada9ef0ee4f511b7f07c4d8453f8da35a35ecf3) |

In addition to the weekly changes, various actions and events can increase or decrease liberty desire directly.

### Annexation

Overlords can demand annexation of their puppets, colonies, vassals, and crown lands. If the subject has less than 25 liberty desire or is in rebellion, there is a **−75%** [infamy](https://vic3.paradoxwikis.com/Infamy) reduction for this demand.

Upon annexation of a subject, all other subjects will gain **+0.2** liberty desire for 5 years.

Puppets, vassals, crown lands, and personal unions are also annexed on unification if they share a primary culture with the unification.

### Independence

Protectorates and tributaries may demand independence from their overlord with a [diplomatic play](Diplomatic play.md), potentially leading to an independence war. Other subject types may also demand independence if they were denied a request to increase autonomy within 5 years. An overlord can also release a subject unilaterally, although it is a rare occurrence.

If a subject is targeted by a diplomatic play by another country and the subject's overlord fails to defend it, the subject automatically becomes independent when the war breaks out.

### Rebellion

Subjects may rebel against their overlord by initiating or joining a diplomatic play with an increase autonomy or independence wargoal. Subjects with high liberty desire are more likely to rebel. When a subject rebels, any wargoals from the overlord targeting that subject have a **−75%** reduction in infamy.

### Imposing laws

Overlords can impose laws on any subject except tributaries or protectorates. The law must be enactable by the subject, and certain laws have further restrictions. The imposed law goes through all regular enactment and may fail or cause a revolution as normal. Chartered companies, colonies, crown lands, and puppets have **+10%** enactment success chance for imposed laws.

## Subject types

There are nine subject types. Five types are non-autonomous, meaning they are unable to start any diplomatic plays, except for independence and increase autonomy, and they automatically join their overlord's [diplomatic plays](https://vic3.paradoxwikis.com/Diplomatic_plays). The other four are autonomous, meaning they may start or join diplomatic plays as normal and may have their own subjects; Colonies may also have their own subjects. Dominions and Chartered Companies are semi-autonomous as they automatically join their overlord's plays, while tributaries and protectorates are fully autonomous as they do not. Non-autonomous subjects can be made *Exempt from Service* which prevents them from automatically joining the overlord's plays.

Note that subjects do not automatically join their overlord in plays if the overlord did not initiate the play or was not the initial target. Therefore, a play targeting a subject country prevents the overlord's other non-autonomous subjects from joining unless the overlord uses *Enforce Military Access*. Autonomous subjects can still join as normal.

Most subject types pay a portion of their [tax, minting and other government income](Treasury.md) to their overlord (but not from tariffs, investment pool transfer, or diplomatic pact income). Subjects also give a percentage of their [convoys](https://vic3.paradoxwikis.com/Convoys) to their overlord as the market leader.

Some subject types count towards the states required for [unification](https://vic3.paradoxwikis.com/Unification) for the overlord. If the subject shares a primary [culture](Culture.md) of the formable country, it is annexed entirely on formation – whether they own any of the required states or not. Subjects with other primary cultures are not annexed, but do cede all relevant state regions to their overlord on formation.[4] Subjects can back only their direct overlord for major unifications, such as [Germany](Germany.md).

| Type | Autonomous | Reduce to | Increase to | Unifies | Income transfer | Maximum involvement | Overlord type | Subject type |
|---|---|---|---|---|---|---|---|---|
| Puppet | ![No](/images/thumb/0/04/No.png/24px-No.png) | Annexation | Protectorate | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 30% | 8000 | Recognized | Non-Colonial |
| Vassal | ![No](/images/thumb/0/04/No.png/24px-No.png) | Annexation | Tributary | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 30% | 5000 | Unrecognized | Any |
| Colony | ![No](/images/thumb/0/04/No.png/24px-No.png) | Annexation | Dominion | ![No](/images/thumb/0/04/No.png/24px-No.png) | 30% | 8000 | Recognized | Colonial/Company |
| Protectorate | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | Puppet | Independence | ![No](/images/thumb/0/04/No.png/24px-No.png) | — | 5000 | Recognized | Non-Colonial |
| Tributary | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | Vassal | Independence | ![No](/images/thumb/0/04/No.png/24px-No.png) | 20% | 2500 | Unrecognized | Any |
| Chartered company | ![Semi-autonomous](/images/thumb/5/54/Information.png/24px-Information.png) | Colony | Independence | ![No](/images/thumb/0/04/No.png/24px-No.png) | 30% | 5000 | Recognized | Colonial/Company |
| Dominion | ![Semi-autonomous](/images/thumb/5/54/Information.png/24px-Information.png) | Colony | Independence | ![No](/images/thumb/0/04/No.png/24px-No.png) | 25% | 8000 | Recognized | Colonial |
| Personal union | ![No](/images/thumb/0/04/No.png/24px-No.png) | Crown land Vassal | Independence | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | — | 5000 | Any | Any |
| Crown land | ![No](/images/thumb/0/04/No.png/24px-No.png) | Annexation | Personal union | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | 15% | 8000 | Recognized | Non-Colonial |

Company-type countries can only be chartered company or colony subjects.

### Personal union

Personal unions are a special subject type defined by the subject sharing their monarch with their overlord. Additionally, a personal union junior can be the same rank as – or even higher than – the overlord, though this is unlikely in regular gameplay. A personal union ends if the either partner ceases to be a Monarchy. A personal union junior's autonomy cannot be changed until *Nationalism* has been researched. The junior partner cannot change the [governance principle law](Power structure laws.md) to cease to be a monarchy.

Personal unions cannot be formed during gameplay except by effect or from crown land subjects increasing autonomy. Currently, there are a few such examples:

- The journal entry *Free State Question* creates a personal union with the [Free State](Free State.md) under the country that triggers the entry
- The journal entry *Unite the Principalities* can create a personal union between [Wallachia](Wallachia.md) and [Moldavia](Moldavia.md) – the United Principalities – as a prequel to becoming [Romania](Romania.md).
- The journal entry *All for One* can create a personal union of [Transylvania](Transylvania.md) under the United Principalities.
- The journal entry *London Conference* can create a personal union of [Limburg](https://vic3.paradoxwikis.com/Limburg) under [Netherlands](Netherlands.md)
- The journal entry *The Matter of Hungary* can create a personal union of [Hungary](Hungary.md) under [Austria](Austria.md)
- The decision *Issue a Trialist Manifesto* can create a personal union of [Croatia](Croatia.md) under [Austria](Austria.md)
- The journal entry *The United Kingdom* can create a personal union of [Brazil](Brazil.md) under [Portugal](Portugal.md)

All other personal unions exist at the start of the game:

- [Schleswig](Schleswig.md) and [Holstein](Holstein.md) under [Denmark](Denmark.md)
- [Hanover](Hanover.md) under [Great Britain](Great Britain.md) – ends with the death of King William soon after game start
- [Luxembourg](Luxembourg.md) under [Netherlands](Netherlands.md) – note that the two countries are separated from each other by [Belgium](Belgium.md) and [Prussia](Prussia.md).
- [Finland](Finland.md) under [Russia](Russia.md)
- [Norway](Norway.md) under [Sweden](Sweden.md)

The following crown lands exist at the game start, all subjects of [Austria](Austria.md)

- [Hungary](Hungary.md)
- [Croatia](Croatia.md)
- [Transylvania](Transylvania.md)

Additionally, [Banat](Banat.md) and [Slovakia](https://vic3.paradoxwikis.com/Slovakia) can become crown land subjects of Austria as part of the *Hungarian Revolution* journal entry.

### Chartered companies

Chartered companies are a special subject type, wherein a country is governed by one of the overlord's companies. A chartered company's autonomy cannot be reduced until *Civilizing Mission* has been researched.

Chartered companies cannot establish their own [companies](Companies.md), but all government owned buildings in such a country count as being owned by the company and benefit from the companies throughput and construction bonuses. If the building belongs to one of the company's associated industries, it receives the full throughput and construction bonuses, otherwise they are reduced to only 20%.

Throughput bonuses are only applied to nationally-owned buildings of the chartered company, and construction bonuses only to government construction. Buildings owned or being built by investors are not affected.

The following chartered companies exist at the start:

- [Hudson’s Bay Company](Hudson’s Bay Company.md) and [East India Company](https://vic3.paradoxwikis.com/East_India_Company) under [Great Britain](Great Britain.md)
- [Russian-American Company](Alaska.md) under [Russia](Russia.md)

New chartered companies can be created with the Charters of Commerce DLC, by granting Colonization Rights to a company. Once the company fully colonizes one state region, it will turn into a Chartered Company subject.

Alternatively, establishing a new [colonial administration](Colonization.md) gives an option to turn the subject into a chartered company. It that case, the country is a normal subject, with no additional mechanics or bonuses and no limits on its own companies or subject mechanics.

### Colonies

Colonies are a special subject type, representing overseas administrative units of colonial empires. Some countries, such as [Cuba](Cuba.md) or [Upper Canada](Ontario.md), exist as colonies from the start of the game; the only other way to gain colony subjects is through the [Establish Colonial Administration](Colonization.md) journal entry, active after researching *Civilizing Mission* and only available for African colonies.

The following colonies exist at the start:

- [British West Africa](Sierra Leone.md), [Cape Colony](South Africa.md), [Ceylon](Ceylon.md), [Columbia District](Oregon.md), [Lower Canada](Quebec.md), [New Brunswick](New Brunswick.md), [New South Wales](New South Wales.md), [Nova Scotia](Nova Scotia.md), [South Australia](South Australia.md), [Upper Canada](Ontario.md), [Van Diemen's Land](Tasmania.md) and [Western Australia](Western Australia.md) under [Great Britain](Great Britain.md)
- [Cuba](Cuba.md), [Puerto Rico](Puerto Rico.md) and the [Philippines](Philippines.md) under [Spain](Spain.md)

Colonies are always Colonial Administrations, and they cannot change that law unless they increase their autonomy. Furthermore, certain colonies – including the ones created by the [Establish Colonial Administration](Colonization.md) journal entry – have the Colonial Racialization () amendement to the Subjecthood law, which decreases the acceptance of cultures with no shared heritage traits, but in turn massively increases the acceptance of cultures that do share traits with the Primary Culture.

#### Colonial independence

If any country with the Colonial Administration law (whether they are Chartered companies, Dominions or Colonies) becomes independent (except for [East India Company](https://vic3.paradoxwikis.com/East_India_Company), [East Indies](East Indies.md), [Russian-American Company](Alaska.md), and any country established through the [Establish Colonial Administration](Colonization.md) journal entry, which have their own events) they receive the following event, allowing them to choose a new Governance Principles law.

id

### Independence Day

The old colonial structures which formerly governed our territory are woefully insufficient for an independent state. We must settle upon the foundations of a free and independent [Country].
---

Flavor text:
The Governor did not have time to pack up his furniture before he left. Half a dozen fine European chairs graced his dining room, surrounding a table that had hastily been stripped of the silverware and its silken cloth by the fleeing prior occupants. Those fine chairs now hosted six fine gentlemen. Some of them, fortunate enough to warrant an invitation to the Governor's dinners, had been here before. The remainder were rougher, newer. If any here would were inclined to present something bold, it would be one of them.
---

| Is triggered by: Becoming independent |
|---|
| Trigger conditions: Has enacted Colonial Administration None of: Is East India Company Is East Indies Is Russian American Company Was established through the Establish Colonial Administration journal entry |
| Option conditions Always enabled: The [Legislature] will be the supreme authority. Enact Parliamentary Republic Always enabled: We will have a Republic. Enact Presidential Republic Enabled if: The strongest government IG endorses Monarchy [Ruler] will have the Crown, if [he] wills it. Enact Monarchy Enabled if: The strongest government IG endorses Corporate State The union of classes will preserve our independence. Enact Corporate State Enabled if: The strongest government IG endorses Council Republic It was the proletariat that earned our victory. Enact Council Republic Enabled if: The strongest government IG endorses Theocracy [Country] will be guided by divine providence. Enact Theocracy For all options Become recognized, if not already |

## Establishing a subject

Countries can target other countries with a diplomatic play to make them a protectorate, dominion, or tributary as long as the initiating country is a higher rank and the targeted country is below (unrecognized) major power.

Subjects can also be created by [releasing](Releasable countries.md) a country from owned states, in which case the subject type depends on the recognition status of the releaser, and the type of the released country as in the table below.

| Country type | Overlord recognition |  |
|---|---|---|
| Recognized | Unrecognized |  |
| Recognized | Puppet | Vassal |
| Unrecognized |  |  |
| Colonial | Colony |  |

### Subject transfer

Subjects can change overlords in a few ways. Most often, one overlord targets the subject with the *Transfer Subject* wargoal. This wargoal cannot be used against personal unions[5]. Alternatively, if a country with subjects becomes a non-autonomous subject, their subjects are also transferred to the new overlord.

If an overlord changes from unrecognized to recognized or vice-versa – for example as a result of a country becoming recognized or subject transfer, the subject's type changes as in the table below.

| Subject type | New overlord |  |
|---|---|---|
| Recognized | Unrecognized |  |
| Puppet | — | Vassal |
| Colony |  |  |
| Crown Land |  |  |
| Dominion | — | Tributary[6] |
| Chartered Company |  |  |
| Protectorate | — | Tributary |
| Vassal | Puppet Colony[7] | — |
| Tributary | Protectorate Dominion[7] | — |

## Subject interactions

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.10. |
|---|---|

See also:
Diplomacy
The following actions and pacts are generally used between a subject and its overlord. Some actions can also be used by the leader of a power bloc with its members. Influence cost is only paid by the overlord or bloc leader unless otherwise noted.

| Pact | Cost | Conditions | Effects | Auto-break conditions |
|---|---|---|---|---|
| Raise Payments | 25 | Sphere of Influence is enabled Target is a subject of actor Target is not opposing actor in a diplomatic play Target has some form of income transfer with the actor Target is not a protectorate or personal union Target has less than 75 liberty desire Target is not in default Does not have Decrease Payments with target | Target gains +0.1 Liberty desire weekly Target's pays 10% more of its income Does not include tariffs or diplomatic pacts to overlord Target can break if liberty desire is 75 or more | Target is opposing actor in a diplomatic play Target does not have some form of income transfer with the actor |
| Decrease Payments | 0 | Sphere of Influence is enabled Target is a subject of actor Target is not opposing actor in a diplomatic play Target has some form of income transfer with the actor Target is not a protectorate or personal union Does not have Raise Payments with target | Target's pays 10% less of its income Does not include tariffs or diplomatic pacts to overlord Target's loses −0.05 liberty desire weekly Cannot break for one year If manually broken, Target gains +10 liberty desire | Target is opposing actor in a diplomatic play Target does not have some form of income transfer with the actor |
| Exempt from Service | 0 | Actor is overlord or bloc leader of target Target is not opposing actor in a diplomatic play Target is required to join actor's diplomatic plays | Target is not required to join actor's diplomatic plays If target is a subject of actor, −0.05 Liberty desire weekly Cannot break for one year If manually broken and target is subject of actor, Target gains +10 liberty desire | Actor is not overlord or bloc leader of target |
| Grant Own Market | 0 | Target is member of actor's market Target is not opposing actor in a diplomatic play Target is independent or a direct subject of actor | Target is given an independent market When granted, if target is subject of actor, liberty desire changes by +50 to −20 depending on economic dependence Cannot break for one year If manually broken and target is subject of actor, Target gains +25 liberty desire | Actor is not direct overlord or bloc leader of target |
| Knowledge Sharing | 50 | Sphere of Influence is enabled Actor is overlord or bloc leader of target Target is not opposing actor in a diplomatic play | Target gains +25% technology spread Actor loses −10% technology spread If target is subject of actor, Target gains −0.05 liberty desire weekly When started, changes appeasement of target's overlord lobbies by ±2 Cannot break for one year If manually broken, Target gains +10 liberty desire Changes appeasement of target's overlord lobbies by ±2 | Actor is not direct overlord or bloc leader of target Actor has not researched more technologies than target |
| Request Market Control | 0 | Actor is member of target's market Target is not opposing actor in a diplomatic play Actor is either: Independent A direct subject of target with 25 or more liberty desire Has not requested market control within 5 years | If target agrees, Gain +10 relations with target Actor is given an independent market If actor is a subject of target, lose −30 liberty desire If target declines, Lose −20 relations with target If actor is a subject of target, gain +10 liberty desire If broken, Lose −10 relations with target | Target is not direct overlord or bloc leader of actor |
| Evangelize | 25 | Sphere of Influence is enabled Actor's state religion is not Atheist Actor has State Religion Target is subject of actor Target has same state religion as actor Target is not opposing actor in a diplomatic play | Target gains +50% conversion When started, target gains +10 liberty desire unless target has any of: State Religion Devout in government Any interest group with a Traditionalist or Theocrat leader in government Then target loses −10 liberty desire Cannot break for one year If manually broken, Target gains ±10 liberty desire by reverse condition as when started |  |
| Support Regime | 50 | Target is not opposing actor in a diplomatic play Target's legitimacy is less than 75 Target is subject of actor | Target gains: +20 Legitimacy −10% Political movement activism −0.1 Liberty desire weekly Actor loses −10 legitimacy When started, changes appeasement of target's overlord lobbies by ±4 Cannot break for one year If manually broken, Target gains +10 liberty desire Changes appeasement of target's overlord lobbies by ±4 |  |

| Action | Conditions | Effects |
|---|---|---|
| Appoint Colonial Governor | Sphere of Influence is enabled Target is subject of actor Target is not opposing actor in a diplomatic play A new governor type has not been appointed nor requested within 5 years Target has enacted Colonial Administration If actor is unrecognized, target is a vassal If actor is recognized, target is unrecognized, or not a protectorate or personal union | Actor chooses a new ruler for target May choose out of the following options: • Influential Planter ( ) • Local Appointee, with the subject's Primary Culture and Religion (instead of the Overlord's) • Experienced Extractor ( ) • Prominent Businessman ( ) • Military Governor ( ) The Governor will rule for a term of 4 years, before being automatically replaced by a character with the same unique trait |
| Request Colonial Governor | Sphere of Influence is enabled Target is direct overlord of actor Target is not opposing actor in a diplomatic play A new governor type has not been appointed nor requested within 5 years Actor has enacted Colonial Administration If actor is a vassal, target is unrecognized Actor is not a protectorate or a personal union | Actor gains modifier Requested Colonial Governor Requested Colonial Governor Country modifier −0.1 Weekly Liberty Desire for 5 years Actor chooses a new ruler May choose out of the following options: • Influential Planter ( ) • Local Appointee, with the subject's Primary Culture and Religion (instead of the Overlord's) • Experienced Extractor ( ) • Prominent Businessman ( ) • Military Governor ( ) The Governor will rule for a term of 4 years, before being automatically replaced by a character with the same unique trait |
| Change Language of Administration | Sphere of Influence is enabled Target is subject of actor Target is not opposing actor in a diplomatic play Actor has enacted Colonial Administration None of target's Primary Cultures: Are the same as Overlord's Share a Language trait with Overlord's | 10% of previous Primary Cultures pops in the subject become more radical All previous Primary Cultures are removed from the target country The subject gains all Primary Cultures the Overlord has • If the country has its capital in the Canada region and overlord has the Francophone language trait • Change Primary Culture of subject to Franco-Canadian • If the country has its capital in the Canada region and overlord has the Anglophone language trait • Change Primary Culture of subject to Anglo-Canadian • If the country is South Africa and overlord has the Dutch language trait • Change Primary Culture of subject to Boer 5% of Bureaucrats in the subject's Capital change to new Primary CultureSubject gains Changed Language of Administration Changed Language of Administration Country modifier −20% Bureaucracy −25% Institution Size Change Speed (decaying) for 5 yearsSubject's Capital state gains Exchanging Administrators Exchanging Administrators State modifier +75% Assimilation (decaying) for 5 years |
| Decrease Autonomy | Target is direct subject of actor Target is not opposing actor in a diplomatic play Target has less than 25 liberty desire Target's autonomy can be reduced i.e., not a puppet or vassal Target is not a personal union or actor has researched Nationalism Target is not a Chartered Company or actor has researched Civilizing Mission Target's autonomy has not changed within 5 years | Target's autonomy is reduced by one step Target gains +50 liberty desire All other direct subjects of actor gain +10 liberty desire Create 5-year truce with target |
| Increase Autonomy | Target is direct subject of actor Target is not opposing actor in a diplomatic play Target's autonomy can be increased i.e., not a protectorate or tributary Target is not a personal union or actor has researched Nationalism Target is not a Chartered Company or actor has researched Civilizing Mission Target's autonomy has not changed within 5 years | Target's autonomy is increased by one step Target loses −30 liberty desire Create 5-year truce with target |
| Request Increase Autonomy | Target is direct overlord of actor Target is not opposing actor in a diplomatic play Actor has 75 or more liberty desire Actor's autonomy can be increased i.e., not a protectorate or tributary Actor is not a personal union or has researched Nationalism Actor is not a chartered company or has researched Civilizing Mission Actor's autonomy has not changed within 5 years Has not requested more autonomy within 5 years | If target agrees, Actor's autonomy is increased by one step Actor loses −30 liberty desire Creates a mutual 5-year truce with target Lose −20 relations with target If target refuses, Actor gains +10 liberty desire Lose −30 relations with target Actor gains ability to demand increased autonomy for 5 years |
| Request Support Regime | Target is not opposing actor in a diplomatic play Target is overlord of actor Has not requested support regime within 5 years | If target agrees, Target establishes Support Regime pact with actor If target declines, Lose −20 relations with target Gain +10 liberty desire |
| Request Knowledge Sharing | Sphere of Influence is enabled Target is overlord of actor Target is not opposing actor in a diplomatic play Has not requested knowledge sharing within 5 years | If target agrees, Target establishes Knowledge Sharing pact with actor If target declines, Lose −20 relations with target Gain +10 liberty desire |
| Grant State | Target is subject of actor Neither country is at war or committed in a diplomatic play Actor has a valid state State is not a capital or colony State is not an owned incorporated primary culture homeland Can be a state owned by another annexable subject Crown land, Puppet, Colony, or Vassal Either: State neighbors target State is a coastal homeland of target's primary culture and target owns a coastal state to grant | Target gains state Target loses between −5 and −50 liberty desire, depending on value of state If state was owned by another subject, That subject gains between +20 and +100 liberty desire, depending on value of state |
| Take State | Target is an annexable subject Crown land, Puppet, Colony, or Vassal of actor Target is not at war or committed in a diplomatic play Target has less than 25 liberty desire Target has a valid state to take: State is not a capital or colony State is not incorporated or target is not a dominion | Actor gains state Target gains between +20 and +100 Liberty Desire, depending on value of state Create incident with target with between 10 and 50 infamy, depending on value of state |
| Demand State | Target is overlord of actor Neither country is at war or committed in a diplomatic play Target has a valid state State is not a capital or colony State is not an incorporated state of target State is not a primary culture homeland of owner Can be a state owned by another annexable subject Crown land, Puppet, Colony, or Vassal of target Either: State neighbors actor State is a coastal homeland of actors's primary culture and actor owns a coastal state to grant | If target agrees, Actor gains state Actor loses between −5 and −50 liberty desire, depending on value of state If state was owned by another subject, That subject gains bewteen +20 and +100 liberty desire, depending on value of state |
| Enforce Military Access | Target is subject of actor Actor is at war Target is not opposing actor in a war or diplomatic play Target is not involved in every war of actor | Target joins every war of actor as ally Target gains +10 liberty desire If target is a protectorate or tributary, it gains +20 instead |
| Invoke Doctrine of Lapse | Is East India Has not received event End of the Company Is at peace Has not Invoked Doctrine of Lapse within two years Target is an AI subject princely state Target is not an empire tier country | Create an incident with 20 infamy on target Lose −10 relations with every princely state Every princely state gains up to 25 liberty desire, based on target's prestige Target receives event Doctrine of Lapse Invoked Can be annexed or fight for independence If annexed, transfers gold reserves to East India |

## References

1. ↑ 1.0 1.1 Bugged, always uses the lowest value
2. ↑ Bugged, cannot go below 0
3. ↑ 3.0 3.1 Bug, likely meant to be East India (BIC) or India (BHT) as British Raj
4. ↑ Currently, if the overlord and subjects are of different types, i.e. Recognized, Unrecognized, Colonial, or Company, the subjects are not annexed nor cede relevant states.
5. ↑ Unrecognized countries also cannot target protectorates, but this seems to be a bug.
6. ↑ Unclear due to lack of defined relation
7. ↑ 7.0 7.1 If the subject is Colonial country

1. /Victoria 3/game/common/subject_types/00_subject_types.txt
2. /Victoria 3/game/common/diplomatic_actions
3. /Victoria 3/game/common/diplomatic_plays

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | [Government](Government.md) • [Capacities](Capacity.md) • [Characters](Character.md) • [Decrees](Decrees.md) • [Institutions](Institutions.md) • [Laws](Laws.md) • [Technology](Technology.md) |
|---|---|

| Politics | [Elections](Elections.md) • [Ideology](Ideology.md) • [Interest group](Interest group.md) • [Political lobby](Political lobby.md) • [Political movement](Political movement.md) • [Political party](Political party.md) • [Revolution](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| Economy | [Buildings](Building.md) • [Goods](Goods.md) • [Harvest condition](Harvest condition.md) • [Infrastructure](Infrastructure.md) • [Market](Market.md) • [Production methods](https://vic3.paradoxwikis.com/Production_methods) • [State](State.md) • [Treasury](Treasury.md) |
|---|---|

| Diplomacy | [Diplomacy](Diplomacy.md) • [Diplomatic action](https://vic3.paradoxwikis.com/Diplomatic_action) • [Diplomatic play](Diplomatic play.md) • [Power bloc](Power bloc.md) • [Ranks](Rank.md) • Subjects • [Treaties](Treaty.md) |
|---|---|

| Warfare | [Warfare](Warfare overview.md) • [Land warfare](Land warfare.md) • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
