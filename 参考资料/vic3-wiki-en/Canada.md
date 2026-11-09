---
title: Canada
source: https://vic3.paradoxwikis.com/Canada
pageid: 4812
categories: [Pages_using_TabberTransclude_parser_tag, 1.13, Countries, Articles_with_potentially_outdated_infoboxes, Pages_with_interwiki_links_to_Wikipedia, Releasable_countries, Formable_countries]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

Canada
---

Capital
:
Ontario, or as formed
---

Government Type
:
As formed
---

Primary Cultures
:
Anglo-Canadian, Franco-Canadian
---

State Religion
:
Protestant
---

Country Tier
:
Kingdom
---

Country Type
:
Colonial
Canada
---

Capital
:
Ontario, or as formed
---

Gov. Type
:
As formed
---

Prim. Cult.
:
Anglo-Canadian, Franco-Canadian
---

State Rel.
:
Protestant
---

C. Tier
:
Kingdom
---

C. Type
:
Colonial
**Canada** is a [formable country](https://vic3.paradoxwikis.com/Formable_country) in North America. It can be formed by any nation with Anglo-Canadian or Franco-Canadian primary culture. All its constituent parts start as [subjects](Subject.md) in the [British Empire](Great Britain.md), and it is very likely that a fully formed Canada will also be a subject of the British crown.

## Scripted content

All Canadian countries have access to the following journal entry and decision. Note that none of these actually form Canada, which must be formed manually through the usual mechanics.

id

### Confederate Canada

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

The dream of Canadian Confederation must be realized. By becoming economically dominant over our fellow colonies while maintaining good relations with the central government, we can propose the annexation of one of our neighbors.
---

| Visibility conditions: Is a subject Has Anglo-Canadian or Franco-Canadian primary culture |  |
|---|---|
| Activation conditions: Has researched Nationalism |  |
| Entry buttons: Confederate Canada The dream of Canadian Confederation must be realized. By becoming economically dominant over our fellow colonies while maintaining good relations with the central government, we can propose the annexation of one of our neighbors. Enabled if: Has not used this button within 2.5 years Is at peace Has researched Nationalism Does not have modifier Canadian Unifier Has Amicable or better with Overlord Any neighboring country: Has Anglo-Canadian or French-Canadian as a Primary Culture Is subject of the same Overlord Has Amicable or better Has a lower GDP Effects: The two Canadian colonies will be unified Trigger event Confederation with [Country] Gain modifier Canadian Unifier Canadian Unifier Country modifier +50 Prestige |  |
| *The dream of Canadian Confederation must be realized. By becoming economically dominant over our fellow colonies while maintaining good relations with the central government, we can propose the annexation of one of our neighbors.* |  |
| **Enabled if:** Has not used this button within 2.5 years Is at peace Has researched Nationalism Does not have modifier Canadian Unifier Has Amicable or better with Overlord Any neighboring country: Has Anglo-Canadian or French-Canadian as a Primary Culture Is subject of the same Overlord Has Amicable or better Has a lower GDP |  |
| **Effects:** The two Canadian colonies will be unified Trigger event Confederation with [Country] Gain modifier Canadian Unifier Canadian Unifier Country modifier +50 Prestige |  |
| Completion conditions: Fully owns nine of the 11 core states of Canada | Effects when completed: Trigger event Canadian Confederation If Ontario is owned, rename the capital of Ontario to Ottawa |
| Invalidation conditions: Is not a subject |  |

id

### Canadian Confederation

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

The unification of Canada is complete. The various colonial governments have been integrated into one, under the administration of [Country] and with the enthusiastic approval of [Overlord].
---

Flavor text:
The dream of a united Canada has finally been achieved. From humble beginnings as a small colony in the vast and unknown north, the settlers have grown and adapted. They have become a people. They have forged a nation.
---

| Is triggered by: Completion of journal entry Confederate Canada |
|---|
| Trigger conditions: None |
| The True North strong and free! Gain modifier Canadian Confederation Canadian Confederation Country modifier +20% Prestige for 5 years If not already a Dominion, become one. |

id

### Confederation with [Country]

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

[Overlord Ruler] has signed into law the confederation between [Country] and [Neighboring Colony]. This marks a great victory in our goal of unifying all of Canada.
---

Flavor text:
With every document signed and stamped, we come one step closer to building a nation. The colonies haven't always seen eye-to-eye, but the people of Canada are resolute in their determination to see this through.
---

| Is triggered by: {{{triggered by}}} |
|---|
| Trigger conditions: None |
| God save the [Overlord]! Annex [Neighboring Colony] and inherit all their claims. |

id

### The Canadian Pacific Railway

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

A railway spanning from the Atlantic to the Pacific coast would open up new opportunities for settlement in Western Canada.
---

| Visibility conditions: Owns any of the following states: Quebec Ontario Manitoba Saskatchewan Alberta British Columbia |  |
|---|---|
| Activation conditions: Has researched Railways Owns all of the following states: Quebec Ontario Manitoba Saskatchewan Alberta British Columbia | Effects when activated: None |
| Completion conditions: All of the following states have Railways: Quebec Ontario Manitoba Saskatchewan Alberta British Columbia | Effects when completed: Trigger event The Last Spike |
| Invalidation conditions: Is not a subject | Effects when invalid: None |

id

### The Last Spike

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

The Canada Pacific Railway has finally been completed, connecting the Atlantic and Pacific coasts. The new railway opens up new opportunities for settlement across the Western Provinces.
---

Flavor text:
"The stroke released the trigger for a burst.
Of sound which stretched the gamut of the air.
The shouts of engineers and dynamiters,
Of locomotive-workers and explorers,
Flanking the rails, were but a tuning up.
For a massed continental chorus."
---

| Is triggered by: Completion of journal entry The Canadian Pacific Railway |
|---|
| Trigger conditions: None |
| The coast holds the most promise. British Columbia: Adds modifier Western Canadian Settlement Western Canadian Settlement State modifier +30% Railway building Throughput +200% Migration Attraction for 5 years There is great potential in the Prairies. Manitoba, Saskatchewan and Alberta: Adds modifier Western Canadian Settlement Western Canadian Settlement State modifier +15% Railway building Throughput +100% Migration Attraction for 5 years |

## Formation

Eight of the 11 core states are needed in order to form Canada
Canada can be formed by the following nations when they control at least eight of its 11 core states and have researched Nationalism. Canada can also be released by any country which controls its capital and three other core states.

| Country | Capital | Primary Cultures | State Religion | Tier | Type | Core States | E |
|---|---|---|---|---|---|---|---|
| **Hudson’s Bay Company** | Manitoba | Anglo-Canadian | Protestant | Principality | Colonial | — | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| **New Brunswick** | New Brunswick | Anglo-Canadian Franco-Canadian | Protestant | Principality | Colonial | Split state in Maritimes | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| **Newfoundland** | Newfoundland | Anglo-Canadian | Protestant | Principality | Colonial | Newfoundland | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| **Nova Scotia** | New Brunswick | Anglo-Canadian | Protestant | Principality | Colonial | Split state in Maritimes | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| **Upper Canada** | Ontario | Anglo-Canadian | Protestant | Principality | Colonial | Ontario | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| **British Columbia** | Oregon | Yankee Anglo-Canadian | Protestant | Principality | Colonial | Oregon Washington Idaho British Columbia | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| Lower Canada | Quebec | Franco-Canadian | Catholic | Principality | Colonial | Quebec | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |

Newfoundland does not exist at the start, and except for Hudson’s Bay Company, all are releasable by any country which controls their capital. If Canada is formed by Quebec (Lower Canada), its state religion remains Catholic rather than changing to the default Protestant.

### Core states

Canada uses Anglo-Canadian and Franco-Canadian's homelands as its core states. These comprise the Canada strategic region as well as northern states in the New England, Great Plains and Pacific Coast strategic regions.

| Name | Core of | Homelands | Region | Arable Land | Resources | State Traits |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Size | Uses |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ontario |  | Anglo-Canadian Iroquoian Algonquian | Canada | 200 | Wheat Farm Livestock Ranch Tobacco Plantation Vineyard | 90 | — | — | — | 48 | — | — | — | (60) | Great Lakes +15 Infrastructure Niagara Falls +20% Electricity output Hudson Bay −20% Port throughput −20% Shipyards throughput |
| Manitoba |  | Métis Anglo-Canadian | Canada | 60 | Wheat Farm Livestock Ranch | 32 | — | — | — | — | 5 | — | — | (30) | Canadian Prairie +20% Agriculture throughput −10% Infrastructure Hudson Bay −20% Port throughput −20% Shipyards throughput |
| Newfoundland |  | Anglo-Canadian | Canada | 20 | Livestock Ranch | 24 | — | 24 | 24 | — | 10 | 6 | — | — | Grand Banks Fisheries +20% Fishing Industry throughput |
| Northwest Territories |  | Anglo-Canadian Athabaskan | Canada | 20 | Livestock Ranch | 40 | — | 18 | — | — | — | — | — | — | Northern Canadian Terrain −20% Agriculture throughput −20% State construction efficiency −20% Infrastructure −50% Migration attraction |
| Nunavut |  | Inuit Anglo-Canadian | Canada | 20 | Livestock Ranch | 8 | — | — | — | — | — | — | — | — | Northern Canadian Terrain −20% Agriculture throughput −20% State construction efficiency −20% Infrastructure −50% Migration attraction Hudson Bay −20% Port throughput −20% Shipyards throughput |
| Quebec |  | Franco-Canadian | Canada | 200 | Wheat Farm Livestock Ranch Tobacco Plantation | 100 | — | 60 | — | — | 8 | 4 | — | — | St Lawrence River +15 Infrastructure |
| Maritimes |  | Anglo-Canadian Franco-Canadian | Atlantic Coast | 40 | Livestock Ranch | 30 | 44 | — | 54 | — | 8 | — | — | — | Halifax Harbor +10% Shipyards throughput +10% Port throughput +5% Market access price impact +15% Trade capacity |
| Alberta |  | Cree Métis Anglo-Canadian Athabaskan | Canada | 80 | Wheat Farm Livestock Ranch | 70 | 48 | — | — | 32 | — | — | — | (80) | Rocky Mountains −20% State construction efficiency −20% Infrastructure |
| Saskatchewan |  | Cree Métis Anglo-Canadian Athabaskan | Canada | 60 | Wheat Farm Livestock Ranch | 40 | 40 | — | — | — | — | — | — | (30) | Canadian Prairie +20% Agriculture throughput −10% Infrastructure |
| Northern Columbia |  | Anglo-Canadian Athabaskan Salish | Pacific Coast | 40 | Wheat Farm Livestock Ranch | 90 | 28 | — | — | 36 | 9 | 6 | (8) | — | Rocky Mountains −20% State construction efficiency −20% Infrastructure Columbia River +20 Infrastructure |
| Yukon Territory |  | Anglo-Canadian Athabaskan | Pacific Coast | 20 | Livestock Ranch | 25 | — | 15 | — | — | — | — | (12) | — | Northern Canadian Terrain −20% Agriculture throughput −20% State construction efficiency −20% Infrastructure −50% Migration attraction |

### Formation event

id
[Country Adjective] Unification
Canada has emerged as a rising power in [Capital Strategic Region].
---

Flavor text:
A new day dawns, and a new nation rises to the world stage. [Country Adjective] glory is the inevitable future.
---

| Is triggered by: Forming Canada |
|---|
| Trigger conditions: None |
| A glorious union. Adds modifier National Unifier National Unifier Country modifier +25 Prestige for 20 years Gain claims on all unowned homelands of primary cultures If all homelands are already owned or claimed, Instead 5% of pops become more loyal |

## Historical characters

The following characters may appear in Canada:

| Name[wp 1] | Type | Interest Group | Ideology | Traits | Conditions |
|---|---|---|---|---|---|
| [John Macdonald](http://en.wikipedia.org/wiki/John_A._Macdonald) | Politician | or | Protectionist | Charismatic, Tactful, Ambitious, Experienced Political Operator | Date between 1844.10.15 and 1887.2.22 Is not decentralized Ontario is an incorporated state Average acceptance of Anglo-Canadian pops is at least Second-class Citizen Relevant interest group is not marginalized |
| [George-Étienne Cartier](http://en.wikipedia.org/wiki/George-%C3%89tienne_Cartier) | Politician | Any of: | Protectionist | Tactful, Cautious, Expert Political Operator | Date between 1848.1.18 and 1867.9.20 Is not decentralized Quebec is an incorporated state Average acceptance of Franco-Canadian pops is at least Second-class Citizen Relevant interest group is not marginalized |
| [George Brown](http://en.wikipedia.org/wiki/George_Brown_(Canadian_politician)) | Politician | or | Market Liberal | Tactful, Sickly, Persistent, Literary | Date between 1854.1.1 and 1874.1.1 Is not decentralized Ontario is an incorporated state Average acceptance of Scottish pops is at least Second-class Citizen Relevant interest group is not marginalized |
| [Allan MacNab](http://en.wikipedia.org/wiki/Allan_MacNab) | Politician | Landowners | Moderate | Grifter, Persistent, Direct, Experienced Political Operator | Date between 1838.1.1 and 1854.9.11 Is not decentralized Ontario is an incorporated state Average acceptance of Anglo-Canadian pops is at least Second-class Citizen Landowners are not marginalized |
| [Augustin-Norbert Morin](http://en.wikipedia.org/wiki/Augustin-Norbert_Morin) | Politician | or | Liberal | Persistent, Imposing, Cautious, Erudite | Date between 1841.2.10 and 1855.1.27 Is not decentralized Quebec is an incorporated state Average acceptance of Franco-Canadian pops is at least Second-class Citizen Relevant interest group is not marginalized |
| [Alexandre-Antonin Taché](http://en.wikipedia.org/wiki/Alexandre-Antonin_Tach%C3%A9) | Politician | Devout if state religion is Catholic Rural Folk otherwise | Humanitarian | Honorable, Tactful, Pious, Diplomat | Date between 1853.6.7 and 1879.1.1 Is not decentralized Owns Manitoba Is Métis or average acceptance of Franco-Canadian pops is at least Second-class Citizen |
| [Adams George Archibald](http://en.wikipedia.org/wiki/Adams_George_Archibald) | Politician | Any of: | Market Liberal | Arrogant, Imperious, Persistent, Political Operator | Date between 1851.1.1 and 1867.9.20 Is not decentralized Is Nova Scotia , or New Brunswick is an incorporated state, or is Canada and owns Manitoba Average acceptance of Franco-Canadian pops is at least Second-class Citizen |
| [Wilfrid Laurier](http://en.wikipedia.org/wiki/Wilfrid_Laurier) | Politician | Any of: | Market Liberal | Charismatic, Imperious, Tactful, Demagogue | Date between 1874.1.22 and 1908.10.26 Is not decentralized Quebec is incorporated Average acceptance of Franco-Canadian pops is at least Second-class Citizen |
| [Robert Borden](http://en.wikipedia.org/wiki/Robert_Borden) | Politician | Any of: | Protectionist | Ambitious, Imperious, Imposing, Experienced Diplomat | Date between 1896.6.23 and 1917.12.17 Is not decentralized Is Nova Scotia or New Brunswick is an incorporated state Average acceptance of Anglo-Canadian pops is at least Second-class Citizen |
| [Henri Bourassa](http://en.wikipedia.org/wiki/Henri_Bourassa) | Politician | Rural Folk | Radical | Reckless, Imperious, Ambitious, Inspirational Orator | Date between 1896.6.23 and 1936.1.1 Is not decentralized Quebec is an incorporated state Average acceptance of Franco-Canadian pops is at least Second-class Citizen |
| Agitator | Date between 1899.10.18 and 1936.1.1 Does not have Franco-Canadian as a primary culture Owns Quebec |  |  |  |  |
| [James Shaver Woodsworth](http://en.wikipedia.org/wiki/James_Shaver_Woodsworth) | Politician | Devout | Social Democrat | Pious, Persistent, Honorable, Inspirational Orator | Date between 1919.5.15 and 1936.1.1 Is not decentralized Manitoba or Ontario is an incorporated state Average acceptance of Anglo-Canadian pops is at least Second-class Citizen |
| Agitator | Date between 1919.5.15 and 1936.1.1 Is not decentralized Manitoba or Ontario is an incorporated state |  |  |  |  |
| [Louis Riel](http://en.wikipedia.org/wiki/Louis_Riel) | Agitator | Rural Folk | Sovereignist | Imperious, Reckless, Charismatic, Firebrand | Date between 1868.7.26 and 1885.5.15 Owns Manitoba and is not decentralized |

## Companies

The following [companies](Companies.md) are associated with Canada, its constituent countries or its homeland states:

| Name[wp 1] / Ownership | Buildings | Industry charters | Prestige goods | Prosperity bonus | Requirements |
|---|---|---|---|---|---|
| [Massey-Harris Limited](http://en.wikipedia.org/wiki/Massey_Ferguson) | Motor Industries Tooling Workshops | Iron Mines | Precision Tools | **+15%** Agriculture throughput | Has researched Railways Ontario is incorporated state with 5 levels of Motor Industries |

## Flags

Canada has several [dynamic flags](List of flags.md) depending on the type of government.

| Flag | Governance Principles | Other Conditions |
|---|---|---|
|  | Default |  |
|  | Theocracy | — |
|  | Monarchy | Autocracy or Single-Party State |
|  | Either: Presidential Republic Parliamentary Republic Corporate State | — |
|  | Oligarchy |  |
|  | Autocracy or Single-Party State |  |
|  | Autocracy, Oligarchy, or Single-Party State Corporate State, or ruler has Fascist or Integralist ideology |  |
|  | Council Republic | — |

## References

---

Wikipedia link references:

1. ↑ 1.0 1.1 Links to English Wikipedia article

Return to top
Countries
by Region
Tabber需要JavaScript才能使用。
| Atlantic Coast/Great Plains regions | [America](America.md) [Indian Territory](Indian Territory.md) [New Brunswick](New Brunswick.md) [Nova Scotia](Nova Scotia.md) [Texas](Texas.md) |
|---|---|

| Brazil/La Plata regions | [Argentina](Argentina.md) [Brazil](Brazil.md) [Chile](Chile.md) [Grão-Pará](Grão-Pará.md) [Paraguay](Paraguay.md) [Piratini](Piratini.md) [Uruguay](Uruguay.md) |
|---|---|

| Canada/Pacific Coast regions | [Alaska](Alaska.md) [Hudson’s Bay Company](Hudson’s Bay Company.md) [Ontario](Ontario.md) [Oregon](Oregon.md) [Quebec](Quebec.md) |
|---|---|

| Central America region | [Central America](Central America.md) [Cuba](Cuba.md) [Haiti](Haiti.md) [Mexico](Mexico.md) [Miskitia](Miskitia.md) [Puerto Rico](Puerto Rico.md) |
|---|---|

| Gran Colombia/The Andes regions | [Bolivia](Bolivia.md) [Colombia](Colombia.md) [Ecuador](Ecuador.md) [Iquicha](Iquicha.md) [North Peru](North Peru.md) [South Peru](South Peru.md) [Venezuela](Venezuela.md) |
|---|---|

| Formable | [Antillean Confederation](Antillean Confederation.md) Canada [Carolina](Carolina.md) [Federation of the Andes](Federation of the Andes.md) [Free States of America](Free States of America.md) [Gran Colombia](Gran Colombia.md) [Peru](Peru.md) [Rio de la Plata](Rio de la Plata.md) [Tawantinsuyu](Tawantinsuyu.md) [West Indies](West Indies.md) |
|---|---|

| North America Releasable | [California](California.md) [Cherokee](Cherokee.md) [Confederate States of America](Confederate States of America.md) [Deseret](Deseret.md) [Florida](https://vic3.paradoxwikis.com/Florida) [Georgia (GRG)](https://vic3.paradoxwikis.com/Georgia_(GRG)) [Haudenosaunee](https://vic3.paradoxwikis.com/Haudenosaunee) [Louisiana](Louisiana.md) [Métis](https://vic3.paradoxwikis.com/M%C3%A9tis) [Michigan](Michigan.md) [New Africa](New Africa.md) [New England](New England.md) [Newfoundland](https://vic3.paradoxwikis.com/Newfoundland) [North Carolina](https://vic3.paradoxwikis.com/North_Carolina) [Nunavut](https://vic3.paradoxwikis.com/Nunavut) [Pueblo](https://vic3.paradoxwikis.com/Pueblo) [South Carolina](https://vic3.paradoxwikis.com/South_Carolina) |
|---|---|

| Central/South America Releasable | [Amazonia](Amazonia.md) [Anahuac](Anahuac.md) [Angola Janga](Angola Janga.md) [Aymara](Aymara.md) [Bahamas](https://vic3.paradoxwikis.com/Bahamas) [Bahia](Bahia.md) [Confederation of the Equator](Confederation of the Equator.md) [Costa Rica](https://vic3.paradoxwikis.com/Costa_Rica) [El Salvador](https://vic3.paradoxwikis.com/El_Salvador) [Guatemala](https://vic3.paradoxwikis.com/Guatemala) [Honduras](https://vic3.paradoxwikis.com/Honduras) [Jamaica](https://vic3.paradoxwikis.com/Jamaica) [Los Altos](https://vic3.paradoxwikis.com/Los_Altos) [Maya](Maya.md) [Minas Gerais](https://vic3.paradoxwikis.com/Minas_Gerais) [Nicaragua](https://vic3.paradoxwikis.com/Nicaragua) [Panama](Panama.md) [Paulistânia](Paulistânia.md) [Río Grande](https://vic3.paradoxwikis.com/R%C3%ADo_Grande) [Santa Catarina](https://vic3.paradoxwikis.com/Santa_Catarina) [Santo Domingo](Santo Domingo.md) [Yucatán](https://vic3.paradoxwikis.com/Yucat%C3%A1n) |
|---|---|

Template:Country navbox/Africa
Template:Country navbox/EuropeWest
Template:Country navbox/MiddleEast
Template:Country navbox/India
Template:Country navbox/AsiaEast
Template:Country navbox/Other
**Notes:** This table lists playable countries divided by superregion and region. Starting countries are listed by the region of their capital state, with formable and releasable countries not present at the start listed separately by superregion. Decentralized (non-playable) and special cases are listed separately.
