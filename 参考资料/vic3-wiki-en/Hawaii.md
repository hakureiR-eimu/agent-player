---
title: Hawaii
source: https://vic3.paradoxwikis.com/Hawaii
pageid: 3599
categories: [Pages_using_TabberTransclude_parser_tag, Potentially_outdated_countries, 1.10, Countries, Articles_with_potentially_outdated_infoboxes, Articles_with_potentially_outdated_sections, Pages_with_interwiki_links_to_Wikipedia, Articles_with_potentially_outdated_guides, Starting_countries]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10.

Hawaii
---

Capital
:
Hawaiian Islands (Honolulu)
---

Government Type
:
Ali'i ki'eki'e
---

Primary Cultures
:
Hawaiian
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
Unrecognized
Hawaii
---

Capital
:
Hawaiian Islands (Honolulu)
---

Gov. Type
:
Ali'i ki'eki'e
---

Prim. Cult.
:
Hawaiian
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
Unrecognized
**Hawaii** is an unrecognized regional power in the center of the Pacific Ocean.

Hawaii is a young nation, fully unified only in 1810 under Kamehameha I, and now ruled by his second son, Kamehameha III.

Historically, the Kingdom of Hawaii was overthrown in 1893, replaced by a republican government until Hawaii was annexed by the [United States](America.md) in 1898.

Hawaii can form [Polynesia](Polynesia.md).

## Scripted content

Hawaii has a series of events regarding the potential annexation of the islands by a great power.

id

### Death of the King

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.10. |
|---|---|

---

With the death of the King, local business owners and foreign ministers seek to increase their influence in Hawaii.
---

Flavor text:
"We have maintained our independence for a while now, but the eyes of greater nations are staring at us hungrily, waiting for the moment to pounce. I fear that that time is rapidly approaching."
---

| Is triggered by: Ruler's death |
|---|
| Trigger conditions: Is Hawaii Has enacted Monarchy Has not triggered before |
| We must take steps to maintain our independence. Activate journal entry Foreign Interests Great powers can use decision Investing in Hawaii |

id

### Foreign Interests

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.10. |
|---|---|

---

Hawaii's position in the Pacific Ocean makes it extremely valuable for Trans Pacific Trade. We must be sure to placate the local businesses and dissuade any potential great power from wanting to take advantage of our islands.
---

| Visibility conditions: Is Hawaii |  |
|---|---|
| Activated by: Event Death of the King | Effects when activated: None |
| Completion conditions: Either: Is recognized All of the following: GDP at least 1M Navy size at least 25 Literacy at least 80% Has not enacted any of: Traditionalism No Police Land-Based Taxation Peasant Levies No Home Affairs | Effects when completed: Become recognized if not already Trigger event Strengthening Our Position |
| Failure conditions: Is a subject | Effects when failed: Triggers event A Foreign Coup |
| Times out after 20 years with the following effects: Triggers event A Foreign Coup |  |

id

### Strengthening Our Position

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.10. |
|---|---|

---

With our strength shown and local business owners placated, we can now look to increase our standing on the international stage.
---

Flavor text:
"We have shown our resolve towards those who would want nothing more than to take control of Hawaii. Even though we are stronger now, we are still not out of the woods."
---

| Is triggered by: Completion of journal entry Foreign Interests |
|---|
| Trigger conditions: None |
| The worst is behind us. All Incorporated states gain National Defense National Defense State modifier +25% Home Defense +25% Home Offense +50% Training Rate +10% Prestige +20% Conscriptable Battalions for 20 years Deport the disloyal. Adds modifier National Defense National Defense Country modifier +12.5% Home Defense +12.5% Home Offense +25% Training Rate +5% Prestige +10% Conscriptable Battalions for 10 years Industrialists: Adds modifier Businessmen Deported Businessmen Deported Interest Group modifier −5 Interest Group Approval −20% Interest Group Political Strength (decaying) for 10 years If the Industrialists leader is not Hawaiian, kill this character The Devout will now be known as Evangelicals Evangelicals lose the Laissez-Faire ideology If the Evangelicals leader is not Hawaiian, kill this character If the country is a Monarchy: The Democrats will now be known as Intelligentsia Intelligentsia replaces the Republican ideology with Constitutionalist Triggers event Deported Business Owners for great powers that took decision Investing in Hawaii |

id

### A Foreign Coup

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.10. |
|---|---|

---

Groups of protestors and local militia led by a coalition of business owners and ambassadors from [Coup Country] have successfully taken over the Government and are now petitioning to have the country annexed.
---

Flavor text:
"Our independence and freedom are now at risk. We lay helplessly at the feet of [Coup Country] and must accept the new reality we have been given. Our nation itself is being held hostage!"
---

| Is triggered by: Timeout of journal entry Foreign Interests |
|---|
| Trigger conditions: None |
| Immediate effects: If a subject, the overlord is selected as [Coup Country] Else, if part of a power bloc and not the leader, the bloc's leader is selected as [Coup Country] Else, a random country that took decision Investing in Hawaii is selected as [Coup Country] More likely to be selected if the country is America (even more likely if America is a player), has high relations with Hawaii, has investment rights, has trade privileges, and if the country is funding lobbies in Hawaii |
| How did it come to this? Activates laws Presidential Republic and Oligarchy The current ruler dies Triggers event The Territory of Hawaii for [Coup Country] |

id

### The Territory of Hawaii

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.10. |
|---|---|

---

Local business owners with the help of our ambassador to Hawaii have staged a coup against the local government and are requesting that we incorporate the islands before others take advantage of the situation.
---

Flavor text:
"Hawaii is the keystone of the Pacific Ocean. Now that we have control over its future, we now also have control over the ocean. We will be able to more easily facilitate trade throughout the region."
---

| Is triggered by: Event A Foreign Coup |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: Occupy the islands, but keep them autonomous. Hawaii becomes a Puppet of this country Creates an incident with 5 infamy Enabled if: Hawaii is not a player If we don't, someone else might. Annex Hawaii Creates an incident with 10 infamy Always enabled: We will not be a part of this coup. Gain +20 relations with Hawaii |

id

### Deported Business Owners

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.10. |
|---|---|

---

The Hawaiian Government has deported our citizens from their islands and seized their property. We must respond to this appropriately.
---

Flavor text:
"How dare they deport our citizens and take control of private business. Such a seizure of land is not only unprecedented, but unacceptable. We shall not tolerate this humiliation."
---

| Is triggered by: Event Strengthening Our Position |
|---|
| Trigger conditions: None |
| It was their own fault. Gain +20 relations with Hawaii This is unacceptable! Gain claims on Hawaiian Islands |

Great Powers can seek influence over Hawaii while the journal entry *Foreign Interests* is active.

id

### Influencing Hawaii

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.10. |
|---|---|

---

Recent developments in Hawaii have left an opening for the potential to secure the islands and thus bolster our influence in the region. If the Hawaiian Government cannot maintain control, we may be able to step in and secure the islands for ourselves.
---

| Visibility conditions: Is a great power Hawaii has the active journal entry Foreign Interests |  |
|---|---|
| Activation conditions: Has an interest in Oceania Is a great power | Effects when activated: None |
| Entry buttons: Investing in Hawaii With the death of the monarch in Hawaii, a power vacuum has been formed and now there is potential for us to exert more control over the islands. Enabled if: The journal entry does not have the Influence in Hawaii modifier Effects: The journal entry gains the Influence in Hawaii Influence in Hawaii Journal entry modifier −10% Influence modifier for 20 years |  |
| *With the death of the monarch in Hawaii, a power vacuum has been formed and now there is potential for us to exert more control over the islands.* |  |
| **Enabled if:** The journal entry does not have the Influence in Hawaii modifier |  |
| **Effects:** The journal entry gains the Influence in Hawaii Influence in Hawaii Journal entry modifier −10% Influence modifier for 20 years |  |
| Completion conditions: Either Hawaii is a subject of this country, the country owns the Hawaiian Islands, or the journal entry Foreign Interests has concluded |  |
| Invalidation conditions: Hawaii does not exist or the journal entry Foreign Interests has concluded |  |
| Times out after 20 years with the following effects: None |  |

## Technology

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.10. |
|---|---|

Hawaii starts with the following technologies.

| Production technology | Military technology | Society technology |
|---|---|---|
| Prospecting Steelworking Distillation | Drydocks Admiralty Military Drill Artillery | International Trade Centralization International Relations Egalitarianism Empiricism |

## Politics

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.10. |
|---|---|

The starting ruler of Hawaii is Ali'i Nui Kamehameha III Kamehameha, who supports the Democrats. If Hawaii becomes recognized, its monarchy is called Aupuni Mō'ī and its ruler's title becomes Mō'ī.

| Power Structure | Economy | Human Rights |  |  |  |
|---|---|---|---|---|---|
| Governance Principles | Monarchy | Economic System | Traditionalism | Free Speech | Right of Assembly |
| Distribution of Power | Autocracy | Trade Policy | Mercantilism | Labor Rights | No Workers' Rights |
| Citizenship | Subjecthood | Taxation | Land-Based Taxation | Children's Rights | Child Labor Allowed |
| Church and State | Freedom of Conscience | Land Reform | Tenant Farmers | Rights of Women | Propertied Women |
| Bureaucracy | Hereditary Bureaucrats | Colonization | No Colonial Affairs | Welfare | No Social Security |
| Army Model | Peasant Levies | Policing | No Police | Migration | No Migration Controls |
| Navy Model | Merchant Navy | Education System | Public Schools | Slavery | Slavery Banned |
| Internal Security | No Home Affairs | Health System | No Health System | Labor Associations | Guild System |

| Institution | Level |
|---|---|
| Education | 1 |

### Interest groups

Hawaii typically starts with the Democrats in government. The Ali'i, Armed Forces, Maka'āinana, Christian Missionaries, and Industrialists are in opposition. The Petite Bourgeoisie and Trade Unions are marginalized.

The Ali'i gain the Loyalist ideology, which overrides the stances of their Hierarchic ideology on taxation. The Christian Missionaries gain the Laissez-Faire ideology.

The Christian Missionaries and Industrialists may be led by Yankee, Dixie, and English characters in addition to Hawaiians. If Hawaii deports foreign business owners, normal rules for character culture selection will be used instead.

### Historical characters

| Name[1] | Type | Interest Group | Ideology | Traits |
|---|---|---|---|---|
| [Kamehameha III Kamehameha](http://en.wikipedia.org/wiki/Kamehameha_III) | Ruler | Democrats | Pacifist | Direct, Innovative |
| [Kamehameha IV Kamehameha](http://en.wikipedia.org/wiki/Kamehameha_IV) | Heir | Ali'i | Theocrat | Child |
| [Asa Thurston](http://en.wikipedia.org/wiki/Asa_Thurston) | Politician | Christian Missionaries | Theocrat | Reserved |

## Economy

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.10. |
|---|---|

| Statistic | Starting value |
|---|---|
| GDP | 85.6K |
| Population | 192K |
| Literacy | 31.2% |
| Standard of living | Struggling (8.5) |

### States

| Name | Type | Homelands | Arable Land | Resources | State Traits |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| Size | Uses |  |  |  |  |  |  |  |  |
| Hawaiian Islands |  | Hawaiian | 15 | Rice Farm Livestock Ranch Banana Plantation Coffee Plantation Cotton Plantation Sugar Plantation Tea Plantation Tobacco Plantation | 14 | 12 | 8 | 10 | Sandalwood Forestry +25% Hardwood output Volcanic Fertility +20% Agriculture throughput +20% Plantations throughput |

## Military

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.10. |
|---|---|

Hawaii has the Peasant Levies law.

Hawaii has no regular battalions or flotillas. Hawaii has two conscripts available.

## Strategies and guides

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this guide. It was last verified for version 1.10. |
|---|---|

The below is
one of many
player suggested strategies for
Hawaii
. Bear in mind, due to the dynamic nature of the game, it may unfold differently for other players.
A common strategy for a Hawaii player is that they should try to enact a [healthcare system](https://vic3.paradoxwikis.com/Institution), after that they should attempt to gain either [colonial resettlement or colonial exploitation](Economy laws.md) as a law, so that further islands can be colonized to gain more pops.

The best way to grow the economy to export tea or hardwood. [British](Great Britain.md) is probably the most lucrative buyer, so seeking [trade advantages](Treaty.md) with them is a good idea. Due to the low population, Hawaii probably needs to import clothes, liquor and furniture, which Great Britain can provide.

## References

1. ↑ Links to Wikipedia page

Return to top
Countries
by Region
Tabber需要JavaScript才能使用。
| Indochina region | [Burma](Burma.md) [Cambodia](Cambodia.md) [Champasak](https://vic3.paradoxwikis.com/Champasak) [Chiang Mai](Chiang Mai.md) [Dai Nam](Dai Nam.md) [Johore](https://vic3.paradoxwikis.com/Johore) [Luang Prabang](https://vic3.paradoxwikis.com/Luang_Prabang) [Perak](https://vic3.paradoxwikis.com/Perak) [Selangor](https://vic3.paradoxwikis.com/Selangor) [Siam](Siam.md) [Shan](Shan.md) |
|---|---|

| Indonesia region | [Aceh](https://vic3.paradoxwikis.com/Aceh) [Bali](https://vic3.paradoxwikis.com/Bali) [Banjar](https://vic3.paradoxwikis.com/Banjar) [Brunei](https://vic3.paradoxwikis.com/Brunei) [Bulungan](https://vic3.paradoxwikis.com/Bulungan) [Buton](https://vic3.paradoxwikis.com/Buton) [East Indies](East Indies.md) [Jambi](https://vic3.paradoxwikis.com/Jambi) [Kutai](https://vic3.paradoxwikis.com/Kutai) [Lanfang](Lanfang.md) [Maguindanao](Maguindanao.md) [Philippines](Philippines.md) [Pontianak](https://vic3.paradoxwikis.com/Pontianak) [Sambas](https://vic3.paradoxwikis.com/Sambas) [Siak](https://vic3.paradoxwikis.com/Siak) [Sintang](https://vic3.paradoxwikis.com/Sintang) [Sulu](Sulu.md) [Surakarta](https://vic3.paradoxwikis.com/Surakarta) [Tidore](https://vic3.paradoxwikis.com/Tidore) [Yogyakarta](https://vic3.paradoxwikis.com/Yogyakarta) |
|---|---|

| North China/South China/Northeast Asia regions | [China](China.md) [Ezochi](Ezochi.md) [Japan](Japan.md) [Korea](Korea.md) [Ryukyu](Ryukyu.md) |
|---|---|

| Oceania region | Hawaii [Kaurna](Kaurna.md) [New South Wales](New South Wales.md) [South Australia](South Australia.md) [Tahiti](Tahiti.md) [Tasmania](Tasmania.md) [United Tribes](United Tribes.md) [Western Australia](Western Australia.md) |
|---|---|

| Formable | [Aotearoa](https://vic3.paradoxwikis.com/Aotearoa) [Australia](Australia.md) [Indonesia](Indonesia.md) [Laos](Laos.md) [Polynesia](Polynesia.md) |
|---|---|

| Releasable | [Arakan](Arakan.md) [Chukotka](Chukotka.md) [Hathawaddy](Hathawaddy.md) [Java](https://vic3.paradoxwikis.com/Java) [Kachin](Kachin.md) [Kalimantan](https://vic3.paradoxwikis.com/Kalimantan) [Kamchatka](Kamchatka.md) [Karen](Karen.md) [Khmu](Khmu.md) [Manchuria](Manchuria.md) [Muang Phuan](https://vic3.paradoxwikis.com/Muang_Phuan) [New Zealand](New Zealand.md) [Toba](https://vic3.paradoxwikis.com/Toba) [Vientiane](https://vic3.paradoxwikis.com/Vientiane) |
|---|---|

| Chinese releasable | [Anhui](https://vic3.paradoxwikis.com/Anhui) [Da Cheng](https://vic3.paradoxwikis.com/Da_Cheng) [Formosa](Formosa.md) [Guizhou](https://vic3.paradoxwikis.com/Guizhou) [Hunan](https://vic3.paradoxwikis.com/Hunan) [Mongolia](Mongolia.md) [Qian](Qian.md) [Shandong](https://vic3.paradoxwikis.com/Shandong) [Shanxi](https://vic3.paradoxwikis.com/Shanxi) [Sichuan](https://vic3.paradoxwikis.com/Sichuan) [Xibei](https://vic3.paradoxwikis.com/Xibei) [Yuanzhumin](https://vic3.paradoxwikis.com/Yuanzhumin) [Yue](Yue.md) [Yunnan](Yunnan.md) [Zhili](https://vic3.paradoxwikis.com/Zhili) |
|---|---|

Template:Country navbox/Africa
Template:Country navbox/EuropeWest
Template:Country navbox/MiddleEast
Template:Country navbox/India
Template:Country navbox/AmericaNorth
Template:Country navbox/Other
**Notes:** This table lists playable countries divided by superregion and region. Starting countries are listed by the region of their capital state, with formable and releasable countries not present at the start listed separately by superregion. Decentralized (non-playable) and special cases are listed separately.
