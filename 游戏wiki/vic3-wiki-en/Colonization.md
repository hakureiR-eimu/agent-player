---
title: Colonization
source: https://vic3.paradoxwikis.com/Colonization
pageid: 1649
categories: [1.13, Pages_with_obsolete_template_parameters, Game_concepts]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

This page discusses the game mechanic of colonization. For the technology, see
Colonization (technology)
, and for further uses, see
Colonization (disambiguation)
Colonization is the process of acquiring land from [decentralized nations](Decentralized nation.md).

## Establishing colonies

Colonization requires the Colonial Affairs institution, which is enabled by enacting any [law](Laws.md) in the *Colonization* group except for No Colonial Affairs. These are unlocked by the Colonization [technology](Technology.md), an era 1 society technology, already researched by many recognized powers at the beginning of the game.

Colonies are established in states owned by [decentralized nations](Decentralized nation.md). The colonizing country must have an [interest](https://vic3.paradoxwikis.com/Interests) in the [strategic region](Strategic region.md) and the colony state must be coastal or adjacent to a state owned by the colonizer. A country can establish any number of colonies, though at most one per state region. When the colony is established, a single [province](https://vic3.paradoxwikis.com/Province) is immediately ceded to the colonizing country and the colony begins growing province by province. Coastal colonies cost 100K to establish and immediately build a single level of a port so that the colony is not isolated.

Any number of countries can colonize the same state, as long as there are eligible provinces to begin colonization.

Countries that start the game with Colonial Affairs also start with colonies in every owned state region that also contains a neighboring decentralized nation. These initial colonies ignore colonial claims.

### Frontier Colonization

The Frontier Colonization law restricts potential new colonies to state regions which are contiguous with the country's capital state or which share a sea zone with the capital state's contiguous area. This generally prevents any overseas colonization.

### Colonial claims

State regions that are claimed by one or more countries can only be colonized by those countries, unless all of the claiming countries do not have an active interest in the region. Once a colony has been started in a claimed state, it continues regularly, even if a claiming country can or does start its own colony afterward.

### Non-colonization agreement

|  | Available only with the [Charters of Commerce](Charters of Commerce.md) DLC enabled. |
|---|---|

Countries can negotiate non-colonization agreements which prevents starting new colonies in an agreed upon strategic region.

### Malaria

*Malaria* and *Severe Malaria* are [state traits](State traits.md), appearing mainly in Sub-Saharan Africa and Oceania. They decrease colonial growth speed by **−90%** and **−95%** respectively, as well as increasing mortality by **15%** and **25%** for pops of [cultures](https://vic3.paradoxwikis.com/Cultures) without a [homeland](https://vic3.paradoxwikis.com/Homeland) in the state.

States with severe malaria cannot be colonized at all until the country researches the society technology Quinine, which also disables the effects of non-severe malaria. The remaining effects of severe malaria are disabled by the society technology Malaria Prevention. The modifiers of malaria and severe malaria do not apply if any primary culture of the country considers the state its homeland; however, colonization is still blocked in states with severe malaria until Quinine is researched.

## Colonial states

Once a colony is established, the new [state](State.md) is a colony. This is a special type of unincorporated state that cannot be incorporated until the colony has completed. Colony states can be abandoned, returning the state to a [decentralized nation](Decentralized nation.md) in the state region. If a country starts colonizing a state region which already contains one of its unincorporated states, the unincorporated state becomes a colony until colonization is completed, then returns to being an unincorporated state. It is also possible to begin colonizing a state region which contains a country's incorporated state, in that case, the colony remains an incorporated state and it cannot be abandoned.

Colonization can also be paused in colonial states, though the potential growth is still deducted from other colonial states. Colonies are automatically paused if the colonizer loses or removes its interest in the strategic region or if the colony is isolated. Colonization completes if there are no more accessible decentralized nations in the state region.

### Colonial growth

| Level | Min population | Max population |
|---|---|---|
| 1 (0.1) | 5M | 100M |
| 2 (0.2) | 2.5M | 50M |
| 3 (0.3) | 1.67M | 33.3M |
| 4 (0.4) | 1.25M | 25M |
| 5 (0.5) | 1M | 20M |

The total rate of colonial growth is determined by the total incorporated population and colonial growth generation. Each level of the Colonial Affairs institution generates **+0.1%** per **1** million population[1]. Total growth generation is restricted to a range from **0.5%** to **10%**. The table to the right shows the minimum and maximum populations where scaling is capped for each level of colonial growth. With additional sources of colonial growth, such as Colonial Offices II or the [Companhia de Moçambique](List of flavored companies.md) or [Hudson’s Bay Company](List of flavored companies.md), these values change accordingly; to a potential range of ~526K to ~1.52M with both companies and Colonial Offices II.

Total colonial growth is equally split between all non-isolated colonies. This base growth can be modified across the entire country or locally in each colony, such as by events, a ruler with the Colonial Administrator trait, and particularly by Malaria.

Local colonial growth speed is modified in particular by the number of provinces in the state and the population in the state. States are given a baseline size of 50 provinces[2], and for each province in the state above this amount a **+2%** growth speed bonus is applied; similarly, for states with fewer provinces a scaling **−2%** penalty is applied. Additionally, state regions with more than 100K population between the colonizer and decentralized nation apply a scaling growth speed penalty[3]. This factor is calculated as follows:

1 1 + ( Population 100000 ⋅ ⋅ 0.25 ) {\displaystyle {\frac {1}{1+\left({\frac {\text{Population}}{100000}}\cdot 0.25\right)}}} ![{\displaystyle {\frac {1}{1+\left({\frac {\text{Population}}{100000}}\cdot 0.25\right)}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/1508d45ae73ab47c2c04c10a6c6d255444edd8a0)

This amount applies as soon as the combined population is above 100K. For some examples, at just over 100K, the penalty is 0.8; at 200K, it is 0.67; at 400K, it is 0.5; and at 800K, it is 0.33.

Colonial growth speed has a base maximum of **2%** per day. This is doubled by the *colonial rights* modifier, gained by defeating a native uprising. Additionally, the multipliers for state size and population increase or decrease this maximum as well as the rate.

Each time the colony reaches **100%** growth, another province in the state is ceded to the colonizer. If an impassible province is colonized, generally all contiguous impassible provinces are gained at the same time.

## Tension and native uprising

While a colony is growing, it generates *tension* with neighboring decentralized nations, between **2.5** and **20** for each province colonized. Tension decays at a base rate of **5** per year, but if a country is growing a colony, tension generally continues to increase.

If tension reaches **75** or more, the decentralized nation may begin a *native uprising* – a special [diplomatic play](Diplomatic play.md) – against the colonizing country to retake its homeland and expel the invaders. As a diplomatic play, other nations can support either side as normal. If the decentralized nation wins the play or war, they annex the colonizer's colony states in each state region they own part of, while if the colonizer wins, they gain the *colonial rights* modifier, doubling colonization speed against said decentralized nation for the duration of the truce – 5 years.

When a native uprising play starts, that decentralized nation's states cannot be colonized by any country; this pauses the growth of all colonies in its state regions unless the region is shared with another decentralized nation. When colonization is paused this way, colonial states "revert" to unincorporated states temporarily. This can cause a country's declared interest to be converted into an inherent interest. However, when the war concludes, the colony is automatically restarted – if it remains, removing the inherent interest and requiring a country to redeclare an interest in order to continue the colony.

## Colonial administration

Recognized countries with their capital outside of Africa can establish *Colonial Administration* subjects from their states in Africa after researching Civilizing Mission.

id

### Establish Colonial Administration

In order to best leverage our rule over our African holdings, a
Colonial Administration
may be established over a given region of the continent.
Colonial Administrations
will expand into neighboring Decentralized Nations on their own, and may be given jurisdiction over our other regional holdings.
The Scramble for Africa, so it is called, is underway in earnest. Every power worth a hoot is seeking slices of the great continent as more jewels in their crowns. Rich in untapped resources and filled with people yet to be put to work, power and prestige are the prizes for the victors. Make no mistake: blood will be spilled long before the scramble ends. Africa awaits.
---

| Visibility conditions: Is not unrecognized Capital is not in Africa Has an active interest in any of: Congo Ethiopia Niger Senegal Southern Africa Zanj |
|---|
| Activation conditions: Any owned state is in Africa Is independent Has researched Civilizing Mission |
| Entry buttons: Establish Colony in [Region] Visible if: Capital is not in Africa Any owned state is in [Region] Does not have any subject that is a colonial administration in [Region] Enabled if: Owns two or more states in [region] that are the largest in their state regions Has not established a colonial administration within three months Is not at war or committed to a side in a diplomatic play Effects: Creates a new country based on this country The new country becomes a colony of this country Country gains Colonial Administration Colonial Administration Country modifier −50% Non-Contiguous Incorporation Speed +100% Contiguous Incorporation Speed permanently Cede all owned states in [Region] to the new colonial administration Expand Our Colony in [Region] We currently hold lands in [Region] that would be better administered by our colonial subject. If we have more than one colonial Subject in this Strategic Region, they will be merged together. Visible if: Capital is not in Africa Has a subject that is a colonial administration in [Region] Enabled if: Either Owns any non-colony state in [Region] Has more than one colonial administration subject in [Region] Is not at war or committed to a side in a diplomatic play Has not expanded this region within 90 days Effects: One colonial administration subject in [Region] annexes another Cede all owned states in [Region] to the colonial administration |
| **Visible if:** Capital is not in Africa Any owned state is in [Region] Does not have any subject that is a colonial administration in [Region] |
| **Enabled if:** Owns two or more states in [region] that are the largest in their state regions Has not established a colonial administration within three months Is not at war or committed to a side in a diplomatic play |
| **Effects:** Creates a new country based on this country The new country becomes a colony of this country Country gains Colonial Administration Colonial Administration Country modifier −50% Non-Contiguous Incorporation Speed +100% Contiguous Incorporation Speed permanently Cede all owned states in [Region] to the new colonial administration |
| *We currently hold lands in [Region] that would be better administered by our colonial subject. If we have more than one colonial Subject in this Strategic Region, they will be merged together.* |
| **Visible if:** Capital is not in Africa Has a subject that is a colonial administration in [Region] |
| **Enabled if:** Either Owns any non-colony state in [Region] Has more than one colonial administration subject in [Region] Is not at war or committed to a side in a diplomatic play Has not expanded this region within 90 days |
| **Effects:** One colonial administration subject in [Region] annexes another Cede all owned states in [Region] to the colonial administration |

When a new colonial administration subject is established, it becomes a
colony of the establishing country. It has the same state religion and primary cultures as the establishing country, but is always colonial type and principality tier. Its capital is a random state in its region, preferring a state that has the
Greener Grass Campaign decree. Additionally, an event to decide the initial laws and focus of the new colonial administration is fired for the establishing country.
id

### The Nature of Administration

With the establishment of [New Colony], we must decide the direction of our new colonial administration.
---

Flavor text:
"Right, now take this down. And you remembered your pen this time? Ah, good. So it is in Darkest Africa, that we come to the now called [New Colony], where we can begin the beachhead of true civilization. From there, proper exploitation of resources for the glory of- My God, man, strike out me asking about your pen! This is for the annals!"
---

| Is triggered by: Establish Colony in [Region] button of Establish Colonial Administration |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: It will be administered by a chartered [new colony] Company. [New Colony] gains Colonial Enterprises Colonial Enterprises Country modifier +10% Plantations throughput +10% Mines throughput for 20 years [New Colony] becomes a Chartered Company Every non-marginalized interest group: If endorses any of: Laissez-Faire Free Trade Interventionism Gains Colonial Entrepreneurship Colonial Entrepreneurship Interest Group modifier +6 Approval for 5 years Enabled if: Has law State Religion or Freedom of Conscience The [state religion] missions will uplift the local populace. [New Colony] gains Religious Mission Stations Religious Mission Stations Country modifier +20% Conversion for 20 years Every non-marginalized interest groups: If endorses any of: State Religion Religious Schools Gains Civilizing Mission Civilizing Mission Interest Group modifier +6 Approval for 5 years Always enabled: In Darkest Africa, a new [establishing country] shall emerge. [New Colony] gains Colonial Settlement Campaigns Colonial Settlement Campaigns Country modifier +50% Migration attraction +10% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility pops for 20 years Every non-marginalized interest groups: If endorses Colonial Resettlement Gains Plus Ultra Plus Ultra Interest Group modifier +6 Approval for 5 years Enabled if: Any of: Has law No Workers' Rights Does not have law Slavery Banned Ruler has trait Cruel or Bigoted The whip shall crack, and the colony provide. [New Colony] gains Extraction at Any Cost Extraction at Any Cost Country modifier +20% Plantations throughput +20% Mines throughput +10% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility pops +20% mortality for 20 years Every non-marginalized interest groups: If endorses any of: No Workers' Rights Legacy Slavery Professional Army Gains Unbridled Profits Unbridled Profits Interest Group modifier +6 Approval for 5 years For all options except the third one Industrialists replace Laissez-Faire with Colonialist |

All colonial administrations begin with the following laws.

| Power Structure | Economy | Human Rights |  |  |  |
|---|---|---|---|---|---|
| Governance Principles | Colonial Administration | Economic System | *See below* | Free Speech | *See below* |
| Distribution of Power | *See below* | Trade Policy | Same as establisher | Labor Rights | No Workers' Rights |
| Citizenship | Subjecthood | Taxation | Same as establisher | Children's Rights | Child Labor Allowed |
| Church and State | *See below* | Land Reform | Same as establisher | Rights of Women | Same as establisher |
| Bureaucracy | Same as establisher | Colonization | *See below* | Welfare | No Social Security |
| Army Model | Same as establisher | Policing | Same as establisher | Migration | Migration Controls |
| Navy Model | Same as establisher | Education System | *See below* | Slavery | *See below* |
| Internal Security | Same as establisher | Health System | No Health System | Labor Associations | Same as establisher |

The Subjecthood law will be amended with Colonial Racialization (), which will decrease the acceptance of cultures with no shared heritage traits, but will in turn massively increase the acceptance of cultures that do share traits with the Primary Culture.

Furthermore, each option enacts a slightly different set of laws on the colonial administration as well.

| Power Structure | Economy | Human Rights |  |  |  |
|---|---|---|---|---|---|
| Distribution of Power | Oligarchy | Economic System | Extraction Economy | Free Speech | Censorship |
| Church and State | Same as establisher | Colonization | Colonial Exploitation | Slavery | Same as establisher |
|  |  | Education System | No Schools |  |  |

| Power Structure | Economy | Human Rights |  |  |  |
|---|---|---|---|---|---|
| Distribution of Power | Oligarchy | Economic System | Extraction Economy | Free Speech | Censorship |
| Church and State | State Religion | Colonization | Colonial Exploitation | Slavery | Same as establisher |
|  |  | Education System | Religious Schools |  |  |

| Power Structure | Economy | Human Rights |  |  |  |
|---|---|---|---|---|---|
| Distribution of Power | Oligarchy | Economic System | Agrarianism | Free Speech | Censorship |
| Church and State | Same as establisher | Colonization | Colonial Resettlement | Slavery | Same as establisher |
|  |  | Education System | No Schools |  |  |

| Power Structure | Economy | Human Rights |  |  |  |
|---|---|---|---|---|---|
| Distribution of Power | Autocracy | Economic System | Extraction Economy | Free Speech | Outlawed Dissent |
| Church and State | Same as establisher | Colonization | Colonial Exploitation | Slavery | Slave Trade |
|  |  | Education System | No Schools |  |  |

### List of colonial administrations

Each of the six regions that hold colonial administrations have a preset flag and name. While they are subjects, colonial administrations always prefix their overlord's adjective to their base name and adjective. For example, "British Congo" and "British Congolese". [Cape Colony](South Africa.md) begins as a Southern Africa colonial administration, but does not use the flag or name here while it is a subject of [Great Britain](Great Britain.md).

- Colonial administration flags and names
- Abyssinia Abyssinian
- Congo Congolese
- East Africa East African
- Niger Nigerien
- Senegal Senegalese
- South Africa Southern African

If one of these Colonial Administrations ever becomes independent from their Overlord, the following event will trigger:

id

### The Severed Limb

With our administrative ties to the metropole cut off, massive protests have erupted throughout [Country]. Protest that our understaffed colonial forces are hard pressed to handle.
---

Flavor text:
"[God] has created us free, and did not make us into heritage or estate. So by [God], we shall be bequeathed or enslaved no more."
---

| Is triggered by: Becoming independent as a Colonial Administration subject |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: May [God] preserve [Country]. Some pops with the European Heritage trait will evacuate to a Homeland state 80% of lower than Second-Class Citizen acceptance status pops become more radical Gain modifier Masterless Colony Masterless Colony Country modifier +35% Radicalism increases for the Cultural Erasure Status +35% Radicalism increases for the Open Prejudice Status +35% Radicalism increases for the Violent Hostility Status −40% Defense +80% Morale Loss −60% Offense for 10 years Enabled if: Has researched Nationalism Any of: Has enacted No Colonial Affairs Has enacted Multiculturalism Has enacted Council Republic Any Cultural Minority movement has at least 10% Support Colonial governance is no longer sustainable. We must have majority rule. Most pops with the European Heritage trait will evacuate to a Homeland state All African cultures with Homelands in [Capital state] become Primary Cultures All cultures with the European Heritage trait stop being Primary Cultures For all options Trigger event Independence Day |

## Company colonization

|  | Available only with the [Charters of Commerce](Charters of Commerce.md) DLC enabled. |
|---|---|

With the Colonization Rights charter, a colony gains **+20%** growth speed, and when it completes, the company takes control of the state and forms a new country owned by the company which is a Chartered Company subject of the company's owner with the permanent modifier *Colonial Administration Colonial Administration Country modifier +100% Contiguous Incorporation Speed −50% Non-Contiguous Incorporation Speed*. The Industrialists in the new country have the Colonialist ideology instead of Laissez-Faire. The new country has the same primary culture and state religion as its overlord and, it also inherits the technology and laws except for the following:

| Power Structure | Economy | Human Rights |  |  |  |
|---|---|---|---|---|---|
| Governance Principles | Colonial Administration | Economic System | Extraction Economy | Free Speech | Censorship |
| Distribution of Power | Oligarchy | Trade Policy | Same as establisher | Labor Rights | No Workers' Rights |
| Citizenship | Subjecthood | Taxation | Same as establisher | Children's Rights | Child Labor Allowed |
| Church and State | Same as establisher | Land Reform | Same as establisher | Rights of Women | Same as establisher |
| Bureaucracy | Same as establisher | Colonization | Colonial Exploitation | Welfare | No Social Security |
| Army Model | Same as establisher | Policing | Same as establisher | Migration | Migration Controls |
| Internal Security | Same as establisher | Education System | No Schools | Slavery | Same as establisher |
|  | Health System | No Health System | Labor Associations | Same as establisher |  |

## References

1. ↑ From /Victoria 3/game/common/defines/00_defines.txt: `COLONIAL_GROWTH_BASE_FACTOR = 0.00001`, applied per 1000 incorporated population in a country
2. ↑ From /Victoria 3/game/common/defines/00_defines.txt: `COLONY_SPEED_PROVINCE_SIZE_STANDARD`
3. ↑ From /Victoria 3/game/common/defines/00_defines.txt: `COLONY_SPEED_POPULATION_INCREMENT` and `COLONY_SPEED_MALUS_PER_POPULATION_INCREMENT`

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

| Diplomacy | [Diplomacy](Diplomacy.md) • [Diplomatic action](https://vic3.paradoxwikis.com/Diplomatic_action) • [Diplomatic play](Diplomatic play.md) • [Power bloc](Power bloc.md) • [Ranks](Rank.md) • [Subjects](Subject.md) • [Treaties](Treaty.md) |
|---|---|

| Warfare | [Warfare](Warfare overview.md) • [Land warfare](Land warfare.md) • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
