---
title: South America content
source: https://vic3.paradoxwikis.com/South_America_content
pageid: 6062
categories: [Potentially_outdated, 1.12, Scripted_content, Articles_with_potentially_outdated_infoboxes, Journal, Events]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.12.

Victoria 3
Scripted content
Decisions
•
Events
•
Journal entries
General content pages
Corn Laws
•
Domestic affairs
Expeditions
•
Ideology content
Interest group content
•
Krakatoa
Journal entry events
•
Revolution events
Production and technology content
Country content pages
American
•
Austrian
•
Balkan
•
Brazilian
British
•
Chinese
•
Colonial Indies
French
•
German
•
Greek
Japanese
•
Korean
•
Montenegrin
Philippine
•
Portuguese
•
Russian
Southern Africa
•
South America
Spanish
•
Turkish
Special content pages
Halloween
Hispanophone countries in South America have access to the following [journal entries](https://vic3.paradoxwikis.com/Journal_entries), [decisions](Decision.md), and [events](Events.md). Certain content is restricted only to certain countries, while other content is shared. For Brazilian content see [Brazilian content](Brazilian content.md).

## The Age of Caudillos

The following journal entry and events represent the the struggle between Caudillos and supporters of democratic governance. This journal entry also is present for [Mexico](Mexico.md) and [Central America](Central America.md).

id

### The Age of Caudillos

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

The status of the
Progress Bar
will be determined by various positive or negative conditions. The
Progress Bar
reaching
100
will cement the power of military strongmen in [Country]. Next month, the
Progress Bar
will change by [caudillo progress].
Depleting the progress bar and keeping the Armed Forces out of government will destroy
Caudillismo
in the Armed Forces and end the threat of military strongmen in the country.
Whilst this Journal Entry is active, our nation will have an elevated chance for a Coup, and any Voting law enacted
[1]
will gain the
Electoral Clientism
amendment
.
Following our independence from Spain, a power vacuum was left in the place of the dismantled colonial governments, which was quickly filled by charismatic military leaders. These "caudillos" have come to define much of South American politics.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event The Age of Caudillos |  |
| Entry buttons: Rule by Decree The leader of our nation should not be burdened by bothersome governmental process, whether bureaucratic or democratic. If the nation is ordered to jump, it should ask "how high?" Enabled if: The Armed Forces are powerful and in government Does not have the modifier Rule by Decree Effects: Advance the progress bar by 100 points 8.33% Gain Rule by Decree Rule by Decree Country modifier −5 Opposition Interest Group Approval −50% Decree Cost for 5 years: |  |
| *The leader of our nation should not be burdened by bothersome governmental process, whether bureaucratic or democratic. If the nation is ordered to jump, it should ask "how high?"* |  |
| **Enabled if:** The Armed Forces are powerful and in government Does not have the modifier Rule by Decree |  |
| **Effects:** Advance the progress bar by 100 points 8.33% Gain Rule by Decree Rule by Decree Country modifier −5 Opposition Interest Group Approval −50% Decree Cost for 5 years: |  |
| Completion conditions: Progress bar is empty 0 or less The Armed Forces are not in government | Effects when completed: Triggers event The Last Caudillos The Armed Forces lose Caudillismo Remove modifier Age of Caudillos Age of Caudillos Country modifier +250% Political Strength of Officers +50% Armed Forces Political Strength +10% Armed Forces Pop Attraction |
| Failure conditions: Progress bar is full 1200 or more The Armed Forces are in government | Effects when failed: Triggers event The Fist Clenches Double effect of modifier Age of Caudillos Age of Caudillos Country modifier +500% Political Strength of Officers +100% Armed Forces Political Strength +20% Armed Forces Pop Attraction |
| Each week, calculate Caudillo Progress +1 for each of: Armed Forces are powerful Armed Forces are in government Any general or admiral has 50 or more popularity Ruler is Authoritarian Has enacted any of: Autocracy Oligarchy Technocracy Single-Party State −1 for each of: Armed Forces are marginalized Armed Forces are not in government Has enacted either: Census Suffrage Universal Suffrage All of: No general has 50 or more popularity Any politician that: Is not a general Has 50 or more popularity Their interest group is powerful and has has the following stances: Does not approve of Autocracy Does not disapprove of Oligarchy [2] Does not disapprove of Technocracy [2] Does not disapprove of Single-Party State [2] |  |
| Each month Add Caudillo Progress to progress bar Chance of: (weight 120): No event (weight 10): Event Continuismo (weight 25): Event Leadership Challenge |  |

id

### The Age of Caudillos

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

Following [Country] independence from Spain, a power vacuum was left in place of the colonial government, which was quickly filled by charismatic [Armed Forces] leaders. These "caudillos" have come to define much of South American politics.
---

Flavor text:
There was, once, a decree that all colonies would submit to the rule of their mother country. That all its goods and words would pass through her doors, and that she would judge them fairly. That she alone would be all they needed.
Then there was Bonaparte, and the mother country made his puppet. Perhaps time had come for the children to fly. And fly they would, under a father's mailed fist. But this tale is yet to end.
---

| Is triggered by: Monthly event pulse |
|---|
| Trigger conditions: This event has not happened for this country Armed Forces have the ideology Caudillismo Has a General |
| Might makes right. Activates journal entry The Age of Caudillos Sets progress bar to 600 points 50% If Chile , instead sets bar to 400 points 33% If Paraguay , also activates journal entry I, the Supreme |

id

### The Last Caudillos

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

The age of caudillo politics is, at long last, at an end in [Country]. The Armed Forces have assumed their rightful place of service to the legitimate government.
---

Flavor text:
And so the father has become, like all men, too old and too tired to continue. Now, dear child, the country is ready to take its first, true steps forward. We live without our mother's eye, and without our father's switch. Everyone makes their choices today. And your grandchildren will look at us and say, 'and they lived happy and ate partridges.'
---

| Is triggered by: Completion of journal entry The Age of Caudillos |
|---|
| Trigger conditions: None |
| A great day for order and discipline. The Armed Forces lose Caudillismo Remove modifier Age of Caudillos Age of Caudillos Country modifier +250% Political Strength of Officers +50% Armed Forces Political Strength +10% Armed Forces Pop Attraction |

id

### The Fist Clenches

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

[Country] has become fully immersed in caudillo politics. The fate of the nation is governed by the whims of the most influential members of the Armed Forces.
---

Flavor text:
"But mama, what about the parade in [Capital state]? Will we be there in time to see Alfonso?
"Seems I'll never finish the story. Fine, yes, I promise we will be there on time. But what will you do if you cannot march with your brother when you grow up? Milk cows?"
"Mama, I know [Ruler name] will have me. I'm going to be strong for [Country]!"
---

| Is triggered by: Failure of journal entry The Age of Caudillos |
|---|
| Trigger conditions: None |
| The sword is mightier than the pen. Double effect of modifier Age of Caudillos Age of Caudillos Country modifier +500% Political Strength of Officers +100% Armed Forces Political Strength +20% Armed Forces Pop Attraction |

id

### Continuismo

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

According to the [Country] Constitution, [Ruler Name]'s term is over and a new [Ruler Title] must be appointed. Of course, the Constitution can always be ammended, or perhaps the role should go to his protégé [Successor Name].
---

Flavor text:
"Your term in office is over. The laws of [Country]-"
"I am the law in [Country]!"
---

| Is triggered by: Monthly pulse of journal entry The Age of Caudillos |
|---|
| Trigger conditions: It has been 10 years since The Age of Caudillos was activated or this event happened The Ruler supports or leads the Armed Forces Has enacted Presidential Republic Has enacted either Autocracy or Oligarchy Either: The leader of the Armed Forces is not the Ruler Any commander who supports the Armed Forces is not the Ruler |
| Immediate effects: Sets a valid trigger character as the [Successor] |
| Extend the [Ruler Title]'s term. Advance the Age of Caudillos progress bar by 200 points 16.6% The Armed Forces gain Continuismo Continuismo Interest group modifier +20% Interest Group Political Strength for 5 years The [Ruler Title] must step down. [Ruler] retires Reduce the Age of Caudillos progress bar by 200 points 16.6% The Armed Forces gain Constitutional Reappointment Constitutional Reappointment Interest group modifier −20% Interest Group Political Strength for 5 years A chance for [Successor Name] to show his quality. The [Successor] becomes the Ruler Advance the Age of Caudillos progress bar by 100 points 8.33% |

id

### Kingmaker

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

As leader of the Armed Forces, [Kingmaker] must decide whether the military will back the [Liberal Party] or the [Conservative Party].
---

Flavor text:
Supplicants. That was the word [Kingmaker] thought when the representatives addressed him. Flattery, gifts, appeals to family, veiled consequences: as much in lockstep as him parading troops. But the question was this: which served him best?
---

| Is triggered by: The Armed Forces' Leader's death or retirement |
|---|
| Trigger conditions: The former leader was not a [Kingmaker] The Armed Forces are not marginalized Country has elections No election is ongoing Either: The Age of Caudillos journal entry is active Has Age of Caudillos Age of Caudillos Country modifier +250% Political Strength of Officers +50% Armed Forces Political Strength +10% Armed Forces Pop Attraction modifier |
| Immediate effects: Sets the current Armed Forces' Leader as [Kingmaker] |
| Option conditions Always enabled: The army protects the interests of the elites. Advance the Age of Caudillos progress bar by 100 points 8.33% The Armed Forces will support the [Conservative Party] under the leadership of [Kingmaker] Always enabled: Reform will come at the barrel of a gun. Advance the Age of Caudillos progress bar by 100 points 8.33% The Armed Forces will support the [Liberal Party] under the leadership of [Kingmaker] Enabled if: The Communist Party is active The army will struggle alongside the people. Advance the Age of Caudillos progress bar by 100 points 8.33% The Armed Forces will support the [Communist Party] under the leadership of [Kingmaker] Enabled if: The Fascist Party is active The military stands for order above all. Advance the Age of Caudillos progress bar by 100 points 8.33% The Armed Forces will support the [Fascist Party] under the leadership of [Kingmaker] |

id

### Leadership Challenge

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

[Commander] [Challenger Name], a popular military commander, has begun to challenge the civilian leadership of the [Challenger IG] under [Politician Name]. The [Commander]'s ambitions threaten to expand caudillo rule to yet another sector of society.
---

Flavor text:
New Martial Offensive: Civil Offices Under Fire!
A peculiar clarion sounded this morning as [Commander] [Challenger Name] announced his intentions to introduce sweeping reforms amongst the current polity under [Politician Name]. Whispers from [Capital City]'s streets about [Politician Name]'s leadership have become cries to step down, rising in chorus with denouncements against [Commander] [Challenger Name]. (Cont. Pg. 3)
---

| Is triggered by: Monthly pulse of journal entry The Age of Caudillos |
|---|
| Trigger conditions: This event has not occured within 5 years The Age of Caudillos journal entry is active Any General or Admiral: Has more popularity than the leader of their interest group Does not have Reserved or Cautious Is not a Politician The interest group leader is not a general or admiral |
| Immediate effects: Sets a valid trigger character as the [Challenger] Sets the interest group leader as [Politician] |
| Trust in the heroism of [Commander] [Challenger Name]. If there is a free Agitator slot, [Politician] becomes an agitator Otherwise, [Politician] retires [Challenger] becomes the new leader of their interest group Advance the Age of Caudillos progress bar by 100 points 8.33% The Armed Forces gain Continuismo Continuismo Interest group modifier +20% Interest Group Political Strength for 5 years The [Challenger IG] must remain under civilian control. Reduce the Age of Caudillos progress bar by 100 points 8.33% |

## Conquest of the Desert

The following journal entry and events deal with the colonization of Patagonia – typically, by [Argentina](Argentina.md) and [Chile](Chile.md).

id

### The Conquest of the Desert

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

The southern reaches of the continent remain outside of the control of any nation. Though the native population will certainly not make it easy, it is imperative that we secure this territory before it falls into the hands of our rivals.
---

| Visibility conditions: Neighbors Mapuche Has Platinean or South Andean primary culture |  |
|---|---|
| Activation conditions: Does not have No Colonial Affairs enacted |  |
| Entry buttons: Launch Military Excursions The Patagonian natives continue to resist our efforts to colonize the land. It will take the use of military force to pacify them. Enabled if: Has researched Logistics Has at least 10 Battalions The Armed Forces are not marginalized Is colonizing Araucania, Mendoza, or Patagonia Does not have modifier Patagonian Campaign Effects: Infamy increases by 15.00 Gain Patagonian Campaign Patagonian Campaign Country modifier +75% Colony Growth Speed for 10 years |  |
| *The Patagonian natives continue to resist our efforts to colonize the land. It will take the use of military force to pacify them.* |  |
| **Enabled if:** Has researched Logistics Has at least 10 Battalions The Armed Forces are not marginalized Is colonizing Araucania, Mendoza, or Patagonia Does not have modifier Patagonian Campaign |  |
| **Effects:** Infamy increases by 15.00 Gain Patagonian Campaign Patagonian Campaign Country modifier +75% Colony Growth Speed for 10 years |  |
| Completion conditions: If Chile : Owns all of Araucania If Argentina : Owns all of Mendoza and Patagonia | Effects when completed: Triggers event The Conquest of the Desert |
| Each month, chance of: (weight 40): No event (weight 10): Event Arming the Natives (weight 7): Event An Unlikely Kingdom |  |

id

### The Conquest of the Desert

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

We have completed our long campaign to conquer the Patagonian south. Settlers are beginning to seek out promising sites from which to establish new towns and exploit the region's natural resources.
---

Flavor text:
"The Mapuche fought long and hard for centuries to protect their country. Now at last they are defeated, and that land belongs to us. To the victor, the spoils. Now we must set ourselves to the task of populating and governing what we have won."
---

| Is triggered by: Completion of journal entry The Conquest of the Desert |
|---|
| Trigger conditions: None |
| Immediate effects: If Araucania is fully owned, it is set as the relevant state, Otherwise, Patagonia is set as the relevant state |
| At last, the south belongs to us. Add a primary culture homeland to the relevant state Checking in order, South Andean, Platinean, Argentine, Chilean The relevant state gains Patagonian Settlement Patagonian Settlement State modifier +100% Migration Attraction for 10 years. |

id

### Arming the Natives

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

We have discovered that our rivals in [Rival Country] have been arming the [Native Country] natives in [Native State]. This is likely to impede our efforts to conquer the region.
---

Flavor text:
"The [Native Country] natives have never welcomed our presence, but without the means to mount a truly effective resistance we have paid little heed to their objections. The addition of [Rival Country] munitions into the equation comes with the frightening possibility that we must face them on equal terms."
---

| Is triggered by: Any of: Monthly pulse of journal entry The Conquest of the Desert Monthly pulse of journal entry Scramble for Africa Yearly pulse |
|---|
| Trigger conditions: This event has not occured within 50 years An unincorporated state neighbors a decentralized nation Any country has rivaled this country |
| We should de-escalate the situation. [Native State] gains Colonial De-Escalation Colonial De-Escalation State modifier −50% Colony Growth Speed for 5 years. Lose −50 tension with [Native Country] If they want a fight, they'll get one. Lose −20 relations with [Rival Country] Gain +25 tension with [Native Country] |

id

### An Unlikely Kingdom

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

Several [Patagonia Country] chiefs have accepted the Frenchman [Patagonia Ruler] as King in the desperate hope that this will invite international recognition and an end to the colonization of their homeland.
---

Flavor text:
"At this moment, the peoples who have acclaimed me not only as their king, but also as their saviour, are only awaiting my return among them to rise en masse and follow me on the great path of progress. My Estates are open to me from all sides and my peoples call me through the voice of their caciques."
---

| Is triggered by: Monthly pulse of journal entry The Conquest of the Desert ' |
|---|
| Trigger conditions: This event has not occurred before Neighbors a decentralized nation with Patagonian Primary Culture |
| Absolutely ridiculous. Gain +50 tension with [Patagonia Country] Recognize them in exchange for loyalty. [Patagonia Country] becomes unrecognized and enacts Monarchy [Patagonia Country] becomes a Puppet of this country. |

## Populating the Americas

This journal entry simulates the large number of European immigrants to the Americas in the 19th century.

id

### Populating the Americas

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

[Country] is a vast and fortunate land, though it is sparsely populated. We must look beyond the seas, particularly to troubled Europe, for potential settlers to work our fields and factories.
---

| Visibility conditions: Either [3] : Capital is in South America geographic region Capital is in the Mexico or Central America strategic regions Capital is in North or Central America geographic regions and has any state in the Pacific Coast or Great Plains strategic regions Primary culture has the European Heritage trait |  |
|---|---|
| Activation conditions: Has researched Civilizing Mission Is minor power or higher rank Average Standard of Living is at least 10 Is at peace Is not a subject of another nation Has enacted any of: Racial Segregation Cultural Exclusion Multiculturalism Has not enacted Closed Borders or Isolationism If journal is Populating the American West , also: Has at least 3 Incorporated states in either the Pacific Coast or Great Plains strategic regions | Effects when activated: Triggers event Populating the Americas |
| Entry buttons: Promote European Migration By offering generous grants of land and guarantees of work, we can promote our nation as a prime location for our European cousins to settle. Enabled if: Has not used this action in the last 5 years Average Standard of Living is at least 10 Any major power or lower rank country in Europe: Has same state religion as journal country Average Standard of Living is less than journal country's Any primary culture can migrate to journal country Has 3 or more incorporated states in Europe Has an incorporated state in South America, Central America or the American West that can be a Migration Target Has enacted any of: Racial Segregation Cultural Exclusion Multiculturalism Has not enacted Closed Borders or Isolationism Effects: Triggers event Come to [Country] , with the effects: Highest attraction valid state gains a Migration Target from a random valid country Gains Attracting European Migrants Attracting European Migrants Country modifier +100 Authority Cost −25% Influence |  |
| *By offering generous grants of land and guarantees of work, we can promote our nation as a prime location for our European cousins to settle.* |  |
| **Enabled if:** Has not used this action in the last 5 years Average Standard of Living is at least 10 Any major power or lower rank country in Europe: Has same state religion as journal country Average Standard of Living is less than journal country's Any primary culture can migrate to journal country Has 3 or more incorporated states in Europe Has an incorporated state in South America, Central America or the American West that can be a Migration Target Has enacted any of: Racial Segregation Cultural Exclusion Multiculturalism Has not enacted Closed Borders or Isolationism |  |
| **Effects:** Triggers event Come to [Country] , with the effects: Highest attraction valid state gains a Migration Target from a random valid country Gains Attracting European Migrants Attracting European Migrants Country modifier +100 Authority Cost −25% Influence |  |
| Completion conditions: Total population equals 1.5M per incorporated target state | Effects when completed: Triggers event Multitudinous , with the effect Gain Populated Nation Populated Nation Country modifier +25 Prestige permanently |
| Invalidation conditions: Rejected promoting migration | Effects when invalid: None |

id

### Populating the Americas

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

[Country] is a vast and fortunate land, though it is sparsely populated. We must look beyond the seas, particularly to troubled Europe, for potential settlers to work our fields and factories.
---

Flavor text:
The Federal Government will encourage European immigration, and it will not restrict, limit or burden with any taxes the entrance into [Country Adjective] territory of foreigners who come with the goal of working the land, improving the industries and teach the sciences and the arts.
---

| Is triggered by: Activation of journal entry Populating the Americas |
|---|
| Trigger conditions: None |
| Give me your tired, your poor, your huddled masses. Every incorporated state in South America gains Coming to America Coming to America State modifier +25% Migration Attraction for 10 years. We're doing fine on our own. Invalidates the journal entry Populating the Americas |

id

### Multitudinous

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

Great masses of people now inhabit the [Country Adjective] nation, thanks to our efforts to attract migrants and grow our population.
---

Flavor text:
"Peculiar accent you have there. Ah, not to worry: I’m Belgian, myself. I’m sure our hosts don’t care to know as much either."
"Saxon. My friend is a Tuscan. We came over with a Spaniard."
"Thought my ears were burning. Apologies, I was fishing the Irishman from the well. Caught him pondering the immortality of a crab. You wouldn’t care for a drink later, would you, Belgian?"
---

| Is triggered by: Completion of journal entry Populating the Americas |
|---|
| Trigger conditions: None |
| Our words are the voice of a multitude. Gain modifier Populated Nation Populated Nation Country modifier +25 Prestige permanently |

id

### Come to [Country]

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

Tempted by generous offers of land and work, [Migration Culture] people from [Migration Country] have begun to migrate to [Migration Target].
---

Flavor text:
SILVER LININGS IN EVERY CLOUD
Vast tracts of fertile land!
Fields wanting workers!
Factories needing strong arms!
[Country] encourages all European immigrants to begin a new life. No taxes, tariffs or other financial burdens upon arrival. Enough work for everyone.
---

| Is triggered by: Promote European Migration button of journal entry Populating the Americas |
|---|
| Trigger conditions: None |
| Welcome to [Country]! Highest attraction valid state gains a Migration Target from a random valid country Gains Attracting European Migrants Attracting European Migrants Country modifier +100 Authority Cost −25% Influence for 5 years |

## The New Nation

These journal entries represent the changing culture of the Hispanophone countries in South America, from a larger regional identity to more specific national identities.

id

### The [New Culture] Nation

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

The independence of [Country] from Spain has given rise to rumblings of nationalism across the nation. As our nation advances into the future, our intellectuals seek to formulate a new identify, one that is distinctly and solely [New Culture].
The following conditions will benefit the process of developing our
national identity
:
- Patriotic or Liberal interest groups that are in government or have high clout
- Ongoing wars with high war support
- University, Arts Academy, and Government Administration buildings with high occupancy
- High national prestige
- **Not** owning non-[Old Culture] homelands

*The progress of this national awakening is expected to progress by [variable progress] next month. Completing this journal entry will exclude [Country] from pursuing greater pan-national ambitions*

---

| Visibility conditions: Capital is in the South America geographic region Language of Primary Culture is Hispanophone The primary culture is not Central American or Caribeño Is none of: Gran Colombia Peru-Bolivia Federation of the Andes Rio de la Plata |  |
|---|---|
| Activation conditions: Has researched Nationalism Has not completed or failed this journal entry previously | Effects when activated: Triggers event A Nation of Our Own |
| Completion conditions: National Identity progress has reached 100% | Effects when completed: Triggers event National Foundations [New Culture] becomes a primary culture [Old Culture] stops being a primary culture A National Awakening starts for [National culture] lasting 10 years |
| Failure conditions: Is any of: Gran Colombia Peru-Bolivia Federation of the Andes Rio de la Plata | Effects when failed: None |
| Each week, calculate National Identity progress from Clout of Patriotic or Liberal interest groups that are in government Ongoing wars with positive war support University, Arts Academy, and Government Administration buildings with high occupancy High prestige Reduced by owning states without primary culture homelands |  |
| Each month Add National Identity progress |  |

id

### A Nation of Our Own

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

The legacy of our nation's independence from Spain has spurred the beginnings of a developed national identity. Conflicts have begun between the vision of a unique and independent [Country], and the dream of an indivisible Latin America.
---

Flavor text:
For centuries, the guns had fired, first turned on those who resisted conquest, and then those who sought to chain the nation to its former master. An informal peace had come with the flight of the Spanish armies - but they had never truly stopped. They remain shouldered, pointed inwards and outwards - waiting for the end of this momentary confusion, and a single target to pursue.
---

| Is triggered by: Activation of journal entry The [New Culture] Nation |
|---|
| Trigger conditions: None |
| Our homeland takes another step towards freedom. 10% of [Old Culture] pops become more loyal We are but one nation amongst many. 5% of [Old Culture] middle strata pops become more radical Slows the progress of the new National Identity |

id

### National Foundations

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

A national awakening in our country has led to the emergence of a distinct [New Culture] identity among leading nationalists.
---

Flavor text:
"Our sacred cry is ours and ours alone! Hear the sound of broken chains, and see a sacred temple raised to law, peace, and union! How blue is the sky, how glorious is the fatherland!"
---

| Is triggered by: Completion of journal entry The [New Culture] Nation |
|---|
| Trigger conditions: None |
| [Old Culture] no more—we are now the [New Culture] people! Replaces [Old Culture] as Primary Culture with [New Culture] The capital replaces [Old Culture] homelands with [New Culture] homelands A National Awakening starts for [National culture] lasting 10 years Activates journal entry A New National Identity 75% of [Old Culture] Upper Strata pops in the capital become [New Culture] |

id

### A New National Identity

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

Although once part of a greater continuum, sharing a common colonial government and common leadership with our neighbors, we have diverged considerably since we won our independence. It is time we fully assumed a new [New Culture] identity.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: The event National Foundations | Effects when activated: None |
| Entry buttons: Promote National Identity Begins a campaign to push the integration of our new national culture across the nation, granting new [New Culture] homelands in our [Old Culture] incorporated states. Enabled if: Has not used this button within 5 years Any incorporated state: Has an [Old Culture] homeland Neighbors any state with a [New Culture] homeland that either: Is the capital Has 25% or more [New Culture] culture pops Either: Has 5 or more levels of Universities, Urban Center, or Government Administration Has 15 or more total levels of Barracks or Naval Base Effects: All states that match the enable conditions: Replaces [Old Culture] homelands with [New Culture] homelands 75% of [Old Culture] Upper Strata pops become [New Culture] |  |
| *Begins a campaign to push the integration of our new national culture across the nation, granting new [New Culture] homelands in our [Old Culture] incorporated states.* |  |
| **Enabled if:** Has not used this button within 5 years Any incorporated state: Has an [Old Culture] homeland Neighbors any state with a [New Culture] homeland that either: Is the capital Has 25% or more [New Culture] culture pops Either: Has 5 or more levels of Universities, Urban Center, or Government Administration Has 15 or more total levels of Barracks or Naval Base |  |
| **Effects:** All states that match the enable conditions: Replaces [Old Culture] homelands with [New Culture] homelands 75% of [Old Culture] Upper Strata pops become [New Culture] |  |
| Entry modifiers: Blossoming National Identity Blossoming National Identity Country modifier Assimilation to Primary Culture Always Allowed +50% Assimilation +10% Radicalism increases for the Cultural Erasure Status +10% Radicalism increases for the Open Prejudice Status +10% Radicalism increases for the Violent Hostility Status |  |
| Completion conditions: No owned state has an [Old Culture] homeland | Effects when completed: Triggers event The [New Culture] Nation 10% of [New Culture] pops become more loyal |

id

### The [New Culture] Nation

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

From every corner of the land, people speak of their [New Culture] homeland. The [Old Culture] identity is no more.
---

Flavor text:
The flag flapped in the central square, as a procession marched around, trumpets blaring and drums beating in unison. "May the sun renounce its light before we ever break the solemn vow we made to our home!" the crowd roared, more sincerely than they ever had before.
---

| Is triggered by: Completion of journal entry A New National Identity |
|---|
| Trigger conditions: None |
| Glory to the [New Culture] people! Every owned pop of [Old Culture] immediately assimilates to [New Culture] |

## The Old Metropole

This journal entry represents international recognition of the new nations (specifically from [Spain](Spain.md)), and also appears for [Mexico](Mexico.md) and [Central America](Central America.md).

id

### The Old Metropole

*While [Country] both appears and acts as a fully sovereign nation, our standing in the eyes of the world will forever remain uncertain as long as our former overlords withhold recognition. We should strive to establish good relations with Madrid, or present such a mighty visage to the world that none may dare to question our legitimacy.* **Formal Recognition** While Spain's former colonies in the Americas achieved *de facto* independence following the **Spanish American Wars of Independence** in the early 19th century, no *de jure* recognition of this new status followed.

Until Spain formally recognizes the independence of her former colonies using the
Recognize Independence
treaty article, bilateral diplomatic relations will remain
severely hindered
.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Game start. Disregard Spain The moon does not heed the barking of dogs. If we were to show the world that the might of the New World surpasses that of the Old, the judgement of our old, neglectful motherland would be of no consequence. Enabled if: One of the following must be true: Spain does not exist Effects: Lose Independence Not Recognized by Spain Independence Not Recognized by Spain Country modifier −10% Influence Gain A Display of Strength A Display of Strength Country modifier +10% Prestige from Army Power Projection +10% Prestige from Navy Power Projection | Effects when activated: None |
| *The moon does not heed the barking of dogs. If we were to show the world that the might of the New World surpasses that of the Old, the judgement of our old, neglectful motherland would be of no consequence.* |  |
| **Enabled if:** One of the following must be true: Spain does not exist |  |
| **Effects:** Lose Independence Not Recognized by Spain Independence Not Recognized by Spain Country modifier −10% Influence Gain A Display of Strength A Display of Strength Country modifier +10% Prestige from Army Power Projection +10% Prestige from Navy Power Projection |  |
| Completion conditions: Does not have Independence Not Recognized by Spain Independence Not Recognized by Spain Country modifier −10% Influence Should Spain pursue the idea of an American Reconquista , she will disgrace herself in the eyes of the international community, and we will lose this modifier. | Effects when completed: Trigger event Recognition Gain Renewed Diplomatic Efforts Renewed Diplomatic Efforts Country modifier +5% Influence +10% Mass Migration Attraction If our relations with Spain are equal to or greater than 80, it will start a Spanish mass migration of to our nation |

id

### Recognition

With the legal status of [Country] no longer in question, the country's presence on the international stage is bound to increase.
---

Flavor text:
While true independence was won at the point of a bayonet by the valiant fighters of the wars of liberation, it was through the labors of men of letters like himself that [Country] legal sovereignty would be secured.
*As glorious as a heroic defense or a glorious charge? Perhaps not.*

The squares and plazas of [Capital] would likely never bear his name, yet he took great comfort in knowing that in the storied history of [Country]
he
had left a mark.
---

| Is triggered by: Journal Entry The Old Metropole |
|---|
| Trigger conditions: None |
| This date will go down in [Country] history. Gain Renewed Diplomatic Efforts Renewed Diplomatic Efforts Country modifier +5% Influence +10% Mass Migration Attraction If our relations with Spain are equal to or greater than 80, it will start a Spanish mass migration of to our nation |

## War of the Confederation

This journal entry represents the historical War of the Confederation between [Bolivia](Bolivia.md) and [Chile](Chile.md) and [Argentina](Argentina.md) over the fate of [Peru](Peru.md).

id

### The Capture of Salaverry

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

With the capture of the self-proclaimed Supreme Chief of Peru, President Andrés de Santa Cruz has finally consolidated his control over both Peru and Bolivia. Salaverry's capture represents the final act of the Peruvian civil war."
---

Flavor text:
Brought before the President, manacled and with charged bayonets at either side, Salaverry held his head as high as he could. Execution was all but guaranteed now.
Santa Cruz, however, saw opportunity. A fresh chance at a confederation was at hand with Salaverry defeated. The only question was what path would bring Peru into the fold the quickest.
---

| Is triggered by: 45 days after game start for Bolivia |
|---|
| Trigger conditions: North Peru is a subject of Bolivia |
| The penalty for his treason is death. Salaverry dies 5% of pops in North Peru become more radical He will never be permitted to return to Peru. Salaverry is exiled as an agitator 2% of pops in North Peru become more radical For both options: Every centralized country in South America that is not a member of the Confederation receives the event The Fall of Salaverry in 7 days |

id

### The Fall of Salaverry

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

The defeat of Felipe Salaverry's coup attempt has led to complete consolidation of Bolivian domination over Peru. [Supreme Protector] [Andrés de Santa Cruz] has declared the imminent formation of a Confederation between the two nations.
---

Flavor text:
"So that's that, then? Then the Confederation is guaranteed."
"We already have one gluttonous neighbor. God help us all if they both come for us."
"So we will go for the Confederation first. Send word to our friends, and tell them to fix bayonets."
---

| Is triggered by: The event The Capture of Salaverry |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: This Confederation must disappear forever. Becomes involved in the journal entry The Peru-Bolivian Confederation Gain modifier Against the Confederation Against the Confederation Country modifier +25% Training Rate +50 Maneuvers per Diplomatic Play +25% Conscriptable Battalions for 5 years Always enabled: There is yet potential for a fruitful partnership. Becomes involved in the journal entry The Peru-Bolivian Confederation Gain +15 relations with Bolivia Enabled if: Is not Chile or Argentina We have no interest in this affair. Invalidate journal entry The Peru-Bolivian Confederation |

id

### The Peru-Bolivian Confederation

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

The Bolivian intervention into the Peruvian civil war of 1835 has led to the territories of Peru falling under the control of the [Ruler] of
Bolivia
. Bolivia seeks to preserve this fragile Confederation, so that a true and complete union between her subjects might become possible.
The ambitions of the
Peru-Bolivian Confederation
can be averted by forcing them to release their
Subjects
before the Progress Bar reaches
100%
.
Whilst
Bolivia
seek to consolidate the
Confederation'
s rule, she will be subject to increased aggression from her neighbors.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: The event The Fall of Salaverry | Effects when activated: None |
| Completion conditions: To achieve a Confederation victory: Bolivia has successfully maintained her South Andean and Quechua Subjects whilst keeping legitimacy over 50 for 10 years Bolivia is at peace At least one of the following is a subject of Bolivia : South Peru North Peru Iquicha Peru No South Andean or Quechua Subject is in a Civil War | Effects when completed: On a Confederation victory: The Confederation will unify into Peru-Bolivia Bolivia gets the event The Pact of Arequipa Involved countries that did not try to befriend the Confederation get the event The Triumph of the Confederation |
| Failure conditions: To achieve a Restorer victory: At least one of the following must be true: Bolivia does not exist None of the following is a subject of Bolivia South Peru North Peru Iquicha Peru Bolivia is a Subject | Effects when failed: On a Restorer victory: The member of the Confederation controlled by the player or the one with the highest GDP will get the event The Fall of the Confederation Otherwise, involved countries that: Have Amicable relations with Bolivia Either have an Alliance, a Defensive Pact or are in the same Market as Bolivia Will get the event Reigning Peace Otherwise, will get the event Scattered to the Winds |

id

### Scattered to the Winds

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

With the dissolution of the Peru-Bolivian Confederation, a nascent rival to [Country] interests in the Andes has been defeated. The balance of power in South America has been set right once more.
---

Flavor text:
Santa Cruz Capitulates: Confederation Crumbles!
The confederacy along our northern border, so bedeviled in its intended birth that God Himself ordained its capitulation, has at last fallen. A champion's welcome in [Capital City] awaits those brave men who slayed it.
---

| Is triggered by: Completion of journal entry The Peru-Bolivian Confederation with a Restorer victory while opposing the Confederation |
|---|
| Trigger conditions: None |
| A terrible thing has been smothered in its crib. Gain Triumph of the Nation Triumph of the Nation Country modifier +15% Prestige +10% Loyalists from Political Movements for 5 years |

id

### Reigning Peace

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

With the establishment of lasting diplomatic ties with the rising Peru-Bolivian Confederation, the mutual security of both [Country] and the Confederation has been ensured.
---

Flavor text:
"Now we make
peace
with the Confederation? And what of our trade? Two burgeoning neighbors? A consolidated threat on the northern border?"
"Someone has decreed that their trade does not threaten us, and their armies are more comforting than the British. Ah, there are the first wagons of cocoa. Perhaps you’ll think better of them with chocolate in your belly?"
---

| Is triggered by: Completion of journal entry The Peru-Bolivian Confederation with a Restorer victory while trying to befriend the Confederation |
|---|
| Trigger conditions: None |
| Will the arrangement hold? Gain Peace in the Andes Peace in the Andes Country modifier +5% Influence +10% Prestige for 5 years |

id

### The Triumph of the Confederation

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

The Peru-Bolivia has successfully consolidated its power, stabilizing its politics and passing a constitution. Standing against the burgeoning titan appears to soon be futile.
---

Flavor text:
Spies sent letters — furious, defeated, and horrified alike — that any tumult within the new confederation was long since spent. Without lingering resentments to stoke, uncertainties to raise, or division between its legislatures, the people of Peru-Bolivia would see [Country] only as one thing: jealous invaders.
---

| Is triggered by: Bolivia has completed the journal entry The Peru-Bolivian Confederation with a Confederation victory while this country opposed the Confederation |
|---|
| Trigger conditions: None |
| We are forced to face a new rival. 2% of pops become more radical Gain modifier Lost in the Shade Lost in the Shade Country modifier −10% Prestige +10% Morale Loss (decaying) for 5 years |

## Paraguayan content

See also:
Paraguay
[Paraguay](Paraguay.md) has a number of events and journal entries detailing its unique situation in the 1800s, as well as

id

### I, The Supreme

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

|  | Available only with the [Colossus of the South](Colossus of the South.md) DLC enabled. |
|---|---|

---

The eccentric and uncompromising reign of the Supreme and Perpetual Dictator of Paraguay, Doctor José Gaspar Rodriguez de Francia, has dominated most of Paraguay's post-independence period. With the support of his Secret Police, the dreaded
Pyraguës
, Doctor Francia has ruled the country with a firm hand, exchanging his silken glove for an iron fist whenever needed.
But the Perpetual Dictator's age is starting to show. And thus, in Asunción there are whispers. Whispers that Francia's vision of an isolationist, Rousseauian paradise, may not survive the good Doctor himself.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: The event The Age of Caudillos | Effects when activated: None |
| Completion conditions: José Gaspar Rodriguez de Francia is no longer the ruler of Paraguay | Effects when completed: Remove modifier Pyraguës Pyraguës Country modifier +10% Authority −10% Enactment Success Chance −80% Devout Political Strength +200% Intelligentsia Political Strength −20% Radicals from Political Movements Trigger event A Meeting in Asunción |

id

### A Meeting in Asunción

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

With the death of Doctor Francia, all of Asunción is in motion, with civilian and military cliques maneuvering to secure for themselves the reins of power.
---

Flavor text:
"That's it? The paranoid wreck is finally dead?"
"As dead as El Cid and my grandmother, both. God rest their souls."
"About time. The underserving have had their day. Now, the right people can steer Paraguay back to glory."
---

| Is triggered by: Completion of journal entry I, the Supreme |
|---|
| Trigger conditions: None |
| The Asunción garrison secures the city for [Carlos Antonio López]. By siding with the reformers, the Despotic Utopian ideology will forever fade from Paraguayan politics, and characters will no longer generate with it. Remove Guarani as a Primary Culture The leader of the Armed Forces becomes the Ruler Carlos Antonio López gains El Excelentísimo The Armed Forces join the government All other Interest Groups are removed from government If Isolationism is active, activate Protectionism If Secret Police is active, activate National Guard Policarpo Patiño dies Activate journal entry The Heart of America Sr. Patiño, the unloved secretary of Francia, clings to power. Paraguay will continue Francia's legacy The leader of the Armed Forces dies 10% of pops become more radical Gain Restructured Pyraguës Restructured Pyraguës Country modifier +5% Authority −40% Devout Political Strength +100% Intelligentsia Political Strength −10% Radicals from Political Movements for 10 years: |

id

### The Heart of America

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

|  | Available only with the [Colossus of the South](Colossus of the South.md) DLC enabled. |
|---|---|

---

Long did the nation of Paraguay languish under the arbitrary rule of Francia. But where the old tyrant wanted Paraguay to retreat from the world stage, [Ruler Title] [Ruler Name] instead desires for Paraguay to shine on it.
Concerned about the nation's precarious military and economic situation, [Ruler Name] has instigated an ambitious program to modernize and expand its armed forces. After all, only they may truly safeguard the interests of the nation, wherever they may lie.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: The event A Meeting in Asunción | Effects when activated: None |
| Entry buttons: Build the Fortress of Humaitá Our best military engineers have suggested that a major fortress be erected at a horseshoe bend near the mouth of the river Paraguay. The proposed fortress, having a garrison of near 20,000 men, a chain boom, and some 400 cannon mounted on barbettes, casemates, and earthworks, would ensure that any hostile powers attempting to invade our lands upriver are stopped dead in their tracks. Visible if: Owns all of Bajo Paraguay Enabled if: Bajo Paraguay has a Construction Sector of at least size 2 Effects: Triggers event The Sebastopol of South America Gain modifier Fortress of Humaitá Fortress of Humaitá Country modifier +40% Home Defense +10 Prestige for 20 years Establish the Rosada Foundry Strategically located near Paraguay's major iron ore deposits, and surrounded by wood ideal for charcoal production, the Arroyo of Ybycuí is a perfect site for the establishment of a major, modern iron foundry. By inviting foreign experts to assist with the foundry's construction and operation, we can ensure the Paraguayan armed forces will not want for native, high quality iron in the event of war. Visible if: Owns all of Bajo Paraguay Enabled if: Bajo Paraguay has at least size 3 Iron Mines at 50% occupancy Bajo Paraguay has at least size 2 Logging Camps at 50% occupancy Bajo Paraguay has at least size 2 Arms Industry at 50% occupancy Effects: Triggers event The Ruhr of the Tropics Stimulate Population Growth For centuries, the Paraguayan people have relied on traditional healers for medical ailments, with diseases like the pox wreaking havoc on the population, hitting poorer districts especially hard. If Paraguay is to modernize and its population is to grow to meet the demands of the state, Western-educated doctors must be invited to Asunción and a new medical system must be established. Visible if: Owns all of Bajo Paraguay Enabled if: Bajo Paraguay has an Urban Center of at least size 2 Has enacted any of: Charity Hospitals Private Health Insurance Public Health Insurance Has at least 50 relations with any Great Power Effects: Trigger event What the Doctor Ordered Gain modifier Rural Vaccination Programs Rural Vaccination Programs Country modifier −50% Mortality for 20 years Reform the Paraguayan Army We find outselves [sic] surrounded on all sides by potential enemies, whose total populations outnumber ours by orders of magnitude. If Paraguay is to safeguard its independence and interests, drastic measures must be taken to expand and modernize the army. Visible if: Owns all of Bajo Paraguay Enabled if: Has enacted any of: Professional Army Mass Conscription Bajo Paraguay has at least size 20 Barracks at 50% occupancy Effects: Trigger event To Win or to Die |  |
| *Our best military engineers have suggested that a major fortress be erected at a horseshoe bend near the mouth of the river Paraguay. The proposed fortress, having a garrison of near 20,000 men, a chain boom, and some 400 cannon mounted on barbettes, casemates, and earthworks, would ensure that any hostile powers attempting to invade our lands upriver are stopped dead in their tracks.* |  |
| **Visible if:** Owns all of Bajo Paraguay |  |
| **Enabled if:** Bajo Paraguay has a Construction Sector of at least size 2 |  |
| **Effects:** Triggers event The Sebastopol of South America Gain modifier Fortress of Humaitá Fortress of Humaitá Country modifier +40% Home Defense +10 Prestige for 20 years |  |
| *Strategically located near Paraguay's major iron ore deposits, and surrounded by wood ideal for charcoal production, the Arroyo of Ybycuí is a perfect site for the establishment of a major, modern iron foundry. By inviting foreign experts to assist with the foundry's construction and operation, we can ensure the Paraguayan armed forces will not want for native, high quality iron in the event of war.* |  |
| **Visible if:** Owns all of Bajo Paraguay |  |
| **Enabled if:** Bajo Paraguay has at least size 3 Iron Mines at 50% occupancy Bajo Paraguay has at least size 2 Logging Camps at 50% occupancy Bajo Paraguay has at least size 2 Arms Industry at 50% occupancy |  |
| **Effects:** Triggers event The Ruhr of the Tropics |  |
| *For centuries, the Paraguayan people have relied on traditional healers for medical ailments, with diseases like the pox wreaking havoc on the population, hitting poorer districts especially hard. If Paraguay is to modernize and its population is to grow to meet the demands of the state, Western-educated doctors must be invited to Asunción and a new medical system must be established.* |  |
| **Visible if:** Owns all of Bajo Paraguay |  |
| **Enabled if:** Bajo Paraguay has an Urban Center of at least size 2 Has enacted any of: Charity Hospitals Private Health Insurance Public Health Insurance Has at least 50 relations with any Great Power |  |
| **Effects:** Trigger event What the Doctor Ordered Gain modifier Rural Vaccination Programs Rural Vaccination Programs Country modifier −50% Mortality for 20 years |  |
| *We find outselves [sic] surrounded on all sides by potential enemies, whose total populations outnumber ours by orders of magnitude. If Paraguay is to safeguard its independence and interests, drastic measures must be taken to expand and modernize the army.* |  |
| **Visible if:** Owns all of Bajo Paraguay |  |
| **Enabled if:** Has enacted any of: Professional Army Mass Conscription Bajo Paraguay has at least size 20 Barracks at 50% occupancy |  |
| **Effects:** Trigger event To Win or to Die |  |
| Completion conditions: Achieve a GDP of [double current GDP] Build the Fortress of Humaitá Establish the Rosado foundry Reform the Paraguayan army Stimulate population growth | Effects when completed: Trigger event The [Ruler Title]'s Dream Adds Journal Entry Si Vis Pacem, Fac Bellum |
| Monthly 10% chance to trigger event '' Napoleon of the Americas |  |

id

### Napoleon of the Americas

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

The below description is one of several available for this event.
Francisco Solano López has enjoyed a meteoric rise through the ranks of the Paraguayan army. Ambitious to a fault, the young general will stop at nothing to advance the cause of Paraguay: no matter the cost.
---

Flavor text:
Francisco Solano López: Napoleon of Asunción!
A commander of dizzying talent has emerged in our beloved Paraguay. His talent with guns, big and small, has seen our borders become unconquerable walls. Modelling his very strategies on the great Napoleon Bonaparte, [General] López may lead the Paraguayan army to similar greatness.
---

| Is triggered by: The Heart of America monthly pulse |
|---|
| Trigger conditions: Date is after 1850.1.1 This event has not occurred before |
| One day, this 'Napoleon' shall lead Paraguay to greatness. Francisco Solano López: Becomes a General Becomes leader of the Armed Forces Gains the trait Napoleon of the Americas The effects of this modifier will double should General López become Ruler of Paraguay. A general should know his station, and his is the barracks alone. Francisco Solano López: Becomes a General Gains the trait Napoleon of the Americas The effects of this modifier will double should General López become Ruler of Paraguay. There's something off about that man, have him dismissed. Francisco Solano López dies |

id

### The Sebastopol of South America

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

Commanding a hairpin bend in the River Paraguay, the formidable fortress of Humaitá has been established as the well-guarded key to Asunción and the upper rivers.
---

Flavor text:
"Sixteen ominous apertures pointed their gloom, and whatever else they may contain, upon us; and, like the eyes of the figure in the picture, seemed to follow the vessel's motion ... These apertures are those of the casemate battery, constructed of brick, but very deep, and defended by the very formidable battery of sixteen eight inch guns."
---

| Is triggered by: The Heart of America journal entry button Build the Fortress of Humaitá! |
|---|
| Trigger conditions: None |
| ¡No pasarán! Bajo Paraguay gains Fortress of Humaitá Fortress of Humaitá State modifier +40% Home Defense +10 Prestige for 20 years |

id

### The Ruhr of the Tropics

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

With great fanfare, [Ruler Title] [Ruler Name] has officially inaugurated the new industrial complex at Ybycuí, stressing the site's modernity and tremendous industrial potential to the assembled crowd.
---

Flavor text:
Directors Log: On the Iron Works of Ybycuí
!
The iron thus produced has proven of the best quality, and, for some time past no other iron has been used for the public works. Iron smelted with charcoal is, as is well known, much stronger and better than iron smelted with coal.
There is reason to hope that when the mines of Paraguay are properly exploited and worked on a suitable scale, she will be able to supply La Plata with the best quality of iron at a cheaper rate than is now paid for an inferior quality imported from Europe..."
---

| Is triggered by: The Heart of America journal entry button Establish the Rosada Foundry |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: Its charcoal smelters shall ensure the highest quality of iron. Bajo Paraguay gains El Rosado Iron Works El Rosado Iron Works State modifier +20% Iron Mines building Throughput +10% Building Artillery output +20% Building Small Arms output for 20 years Always enabled: Iron is all well and good, but the future belongs to steel. If Bajo Paraguay already has a Steel mills building, Bajo Paraguay gains El Rosado Steel Mill El Rosado Steel Mill State modifier +15% Steel Mills building Throughput +15% Building Artillery output +15% Building Small Arms output for 20 years Otherwise, Create level 2 Steel Mills Bajo Paraguay gains El Rosado Steel Mill El Rosado Steel Mill State modifier +10% Steel Mills building Throughput +10% Building Artillery output +10% Building Small Arms output for 20 years Enabled if: Has enacted No Workers' Rights Our prisons are full of purposeless men, let us 'offer' them one. Bajo Paraguay gains El Rosado Forced Labor Camps El Rosado Forced Labor Camps State modifier +10% Mining Employee Mortality +10% Iron Mines building Throughput +15% Building Artillery output +30% Building Small Arms output for 20 years 2% of pops in Bajo Paraguay become more radical |

id

### What the Doctor Ordered

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

For too long have diseases like the pox robbed our nation of its men and women. While it may continue to do so for decades to come, the establishment of vaccination programs led by foreign doctors will lessen the severity of future outbreaks.
---

Flavor text:
"She was riddled with ringed scars. Forever-wounds and forget-me-nots left by smallpox. It claimed her two eldest, and they breathed their last, rattling gasps in her arms. Her youngest, untouched by the plague, may yet survive it's next incursion. All from just one, little needle."
---

| Is triggered by: The Heart of America journal entry button Stimulate Population Growth |
|---|
| Trigger conditions: None |
| Health is wealth. Bajo Paraguay gains Rural Vaccination Programs Rural Vaccination Programs State modifier −50% Mortality for 20 years |

id

### To Win or to Die

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

Wearing their distinctive red and white uniforms, the men of [Ruler Title] [Ruler Name]'s new battalions march proudly on Asunción's Plaza de Armas. Meanwhile, their generals bicker incessantly amongst themselves about how best to actually use them.
---

Flavor text:
"You may support the motion to use cannons upon high ground, but we have neither the cannons nor the high ground for it."
"As if we do not have the means to make either. Perhaps your lip has grown as weak as your chin?"
"Not any softer than your dome. We promise what we don't have."
---

| Is triggered by: The Heart of America journal entry button Reform the Paraguayan Army |
|---|
| Trigger conditions: None |
| Matter over mind. Gain Simple Designs Simple Designs Country modifier −50% Supply Consumption for 20 years Mind over matter. Gain Fearless Troops Fearless Troops Country modifier +20% Defense +20% Offense for 20 years |

id

### The [Ruler Title]'s Dream

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

Years of arduous labor has born fruit. With the Paraguayan army stronger than ever, and with the backing of native industrial might, Paraguay stands ready to seize its destiny as one of South America's principal powers.
---

Flavor text:
"Good people of  Asunción, and Paraguayans abroad, I, [Ruler Title] [Ruler Name], come bearing a sword in one hand and scales in the other. Today, I speak of a dream for Paraguay: a golden future, one free of the yoke of imperialist neighbors. By hammer, by musket, and by the will of these brave men, our people will take our rightful place upon the world's stage!"
---

| Is triggered by: Completion of journal entry The Heart of America |
|---|
| Trigger conditions: None |
| ¡Adelante! Activate journal entry Si Vis Pacem, Fac Bellum Gain War Fervor War Fervor Country modifier −10% Morale Loss +20% Morale Recovery for 10 years Gain a claim on Corrientes |

id

### Si Vis Pacem, Fac Bellum

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

|  | Available only with the [Colossus of the South](Colossus of the South.md) DLC enabled. |
|---|---|

---

"If you want peace, make war."
A contradiction to some perhaps, but to [Ruler Title] [Ruler Name] it is a statement of fact. Around us, our neighbors maneuver and scheme, plotting to wrest control of our sacred lands from us.
Should then, we meekly wait for the enemy to make the first move? Or pray to the Almighty they never do?
No. As our forefathers before us, we must make our own luck. If war must come to Paraguay, let it come on our terms.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: The event The [Ruler Title]'s Dream | Effects when activated: None |
| Completion conditions: Paraguay fully owns Corrientes Paraguay or its subjects fully own at least one of: Uruguay Santa Fe Paraná Rio Grande do Sul | Effects when completed: Trigger event Peace and Justice |
| Failure conditions: Paraguay has recently lost a war | Effects when failed: Trigger event The Battle of Cerro Corá Bajo Paraguay loses the modifiers: El Rosado Forced Labor Camps El Rosado Forced Labor Camps State modifier +10% Mining Employee Mortality +10% Iron Mines building Throughput +15% Building Artillery output +30% Building Small Arms output El Rosado Iron Works El Rosado Iron Works State modifier +20% Iron Mines building Throughput +10% Building Artillery output +20% Building Small Arms output El Rosado Steel Mill El Rosado Steel Mill State modifier +10% Steel Mills building Throughput +10% Building Artillery output +10% Building Small Arms output Fortress of Humaitá Fortress of Humaitá State modifier +40% Home Defense +10 Prestige Rural Vaccination Programs Rural Vaccination Programs State modifier −50% Mortality Simple Designs Simple Designs Country modifier −50% Supply Consumption Fearless Troops Fearless Troops Country modifier +20% Defense +20% Offense Carlos Antonio López dies Francisco Solano López dies Bajo Paraguay gains The Sack of Asunción The Sack of Asunción State modifier −20% Throughput −20% Innovation +200% Mortality for 10 Years Gain A Broken Land A Broken Land Country modifier −20 Legitimacy −20% Defense −20% Offense for 10 Years |
| Invalidation conditions: Is a subject | Effects when invalid: None |

id

### Peace and Justice

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

|  | Available only with the [Colossus of the South](Colossus of the South.md) DLC enabled. |
|---|---|

---

Like David struck down Goliath, Paraguay has triumphed over her neighbors, with a Paraguayan peace now enforced from the arid Chaco to the shores of the Atlantic.
---

Flavor text:
[Ruler Name] sat at his desk, lit by a single, ensconced candle. Beside a filled inkwell and a clean pen was an untouched victory drink. Libations could wait, as could the hollering men and swooning women outside.
Paraguay needed a rousing address. But where to start?
---

| Is triggered by: Completion of journal entry Si Vis Pacem, Fac Bellum |
|---|
| Trigger conditions: None |
| Give salutes, to that invincible bastion of heroism... Gain Bastion of Heroism Bastion of Heroism Country modifier +20% Prestige −10% Morale Loss +20% Morale Recovery for 10 years ... the magnificent Eden of riches. Gain Earthly Eden Earthly Eden Country modifier +30% Prestige for 10 years 10% of pops become more loyal |

id

### The Battle of Cerro Corá

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

|  | Available only with the [Colossus of the South](Colossus of the South.md) DLC enabled. |
|---|---|

---

Personally leading the ragtag remains of the Paraguayan army, [Ruler] has been killed in action, having refused all calls to surrender.
---

Flavor text:
It was not hard to find the wake of the [Ruler]: the path of looted villages and slaughtered cattle heads ended in a shoddy fortification. The enemy soldiers approached on all sides unhindered. The battle was over barely after it started; an inglorious end to the [Ruler] of Paraguay.
---

| Is triggered by: Failure of journal entry Si Vis Pacem, Fac Bellum |
|---|
| Trigger conditions: None |
| And with [his] death, so dies [his] dream of a Greater Paraguay. Bajo Paraguay loses the modifiers: El Rosado Forced Labor Camps El Rosado Forced Labor Camps State modifier +10% Mining Employee Mortality +10% Iron Mines building Throughput +15% Building Artillery output +30% Building Small Arms output El Rosado Iron Works El Rosado Iron Works State modifier +20% Iron Mines building Throughput +10% Building Artillery output +20% Building Small Arms output El Rosado Steel Mill El Rosado Steel Mill State modifier +10% Steel Mills building Throughput +10% Building Artillery output +10% Building Small Arms output Fortress of Humaitá Fortress of Humaitá State modifier +40% Home Defense +10 Prestige Rural Vaccination Programs Rural Vaccination Programs State modifier −50% Mortality Simple Designs Simple Designs Country modifier −50% Supply Consumption Fearless Troops Fearless Troops Country modifier +20% Defense +20% Offense Carlos Antonio López dies Francisco Solano López dies If the Ruler is neither character, kill the Ruler Bajo Paraguay gains The Sack of Asunción The Sack of Asunción State modifier −20% Throughput −20% Innovation +200% Mortality for 10 Years Gain A Broken Land A Broken Land Country modifier −20 Legitimacy −20% Defense −20% Offense for 10 Years |

### The Paraguayan War

This journal entry exists to motivate other South American countries to deter Paraguayan expansionism. It represents the historical [Paraguayan War](https://en.wikipedia.org/wiki/Paraguayan_War).

id

### The Paraguayan War

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

|  | Available only with the [Colossus of the South](Colossus of the South.md) DLC enabled. |
|---|---|

---

Having amassed significant military might under [Paraguayan Ruler],
Paraguay
now stands poised to strike [Paraguayan Target] in a bid for greatness. It seems only ready muskets may temper Paraguayan ambitions now.
---

Flavor text:
"Sir, word from the Paraguayan borders. Banners raised and cannons entrenched."
"So quickly? Do they plan to-"
"Attack now, yes, sir. The captains are already organising their men."
---

| Is triggered by: Paraguay : Has active journal entry Si Vis Pacem, Fac Bellum Has initiated a Diplomatic Play targeting one of the following states: Corrientes Uruguay Santa Fe Paraná Rio Grande do Sul The Diplomatic Play in question has one of the following Demands: Conquer State Return State Make Protectorate |
|---|
| Trigger conditions: [Country]: Is not Paraguay Has not sided with Paraguay in a Diplomatic Play Is not at war with Paraguay Capital is in the South America geographic region Is involved in the Diplomatic Play initiated by Paraguay specified above |
| We must act. Activate journal entry The Paraguayan War |

id

### The Paraguayan War

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

|  | Available only with the [Colossus of the South](Colossus of the South.md) DLC enabled. |
|---|---|

---

The
Paraguay
an serpent has reared its ugly head. [Paraguayan Ruler] has laid out [his] ambitions for the world to see, ambitions that would greatly upset the South American balance of power.
The consensus is clear, only an armed response will deter [Paraguayan Ruler] now. The only question is, should we offer one?"
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: The event The Paraguayan War | Effects when activated: None |
| Completion conditions: Country has won a War against Paraguay Either: Paraguay does not exist Paraguay does not have any of the following states: Mato Grosso Corrientes Chaco | Effects when completed: Trigger event Sic Semper Tyrannis |
| Failure conditions: Country has lost a War against Paraguay Paraguay owns Corrientes and at least one of the following states: Uruguay Santa Fe Paraná Rio Grande do Sul | Effects when failed: Trigger event Paraguay Triumphant |

id

### Sic Semper Tyrannis

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

|  | Available only with the [Colossus of the South](Colossus of the South.md) DLC enabled. |
|---|---|

---

Arrayed against impossible odds, Paraguay has found itself defeated by our might. The watching world powers have already drafted fresh maps.
---

Flavor text:
*
- If [Argentina](Argentina.md):

*"My people, children of Argentina: a golden dawn rides the sky this day. Our border is secured; our people may sleep a littler sounder this eve. The Paraguayan upstart has been shown an iron heel for its hubris. Already, its people cry out for our soldiery to save it from its fate. And we must, and we shall!"*

- If [Brazil](Brazil.md):

*Paraguayan Pest Put to Rest The Paraguayan brute and his legions lie vanquished on the field of battle. Whatever upstart ambitions they had died with them, and Paraguay is returned to its natural insignificance once more. (cont'd pg. 4)*

- If [Uruguay](Uruguay.md):

*The runt of the litter. The weakest link in the chain. The straw among steel. And yet, it outlasted its neighbor. Not for want of steel or soldiers or scholars, but for simple survival it succeeded. Perhaps, with time and patience, it would thrive long into the night.*

- For all other countries:

Paraguay crushed; an island swallowed on all sides. The tides claimed it from all sides, and the life harbored in the water devoured it amongst the myriad young. The message to the smallest nations was clear: expand and be crushed, or hide and be swallowed.
---

| Is triggered by: Completion of journal entry The Paraguayan War |
|---|
| Trigger conditions: None |
| Glory to the heroes of the fatherland! Gain modifier The Plundering of Paraguay The Plundering of Paraguay Country modifier +5000 Tax Income for 5 years Gain modifier Victory Over Paraguay Victory Over Paraguay Country modifier +10% Prestige for 10 years Paraguay : Gain modifier A Broken Land A Broken Land Country modifier −20 Legitimacy −20% Defense −20% Offense for 10 years Bajo Paraguay gains modifier The Sack of Asunción The Sack of Asunción State modifier −20% Throughput +200% Mortality for 10 years (no matter who owns it) |

id

### Paraguay Triumphant

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

|  | Available only with the [Colossus of the South](Colossus of the South.md) DLC enabled. |
|---|---|

---

Our armies routed,
Paraguay
has done what few observers initially thought possible. It has won the war. The international press is already reporting on a new South American balance of power.
---

Flavor text:
Generals and admirals reached for cues. For every man they pulled away, ten thousand men had died. For every ship they pulled away, a squadron sank with most, if not all, hands lost. Paraguay, an ant who fought the sun. Paraguay, a wolverine who fought jaguars and serpents. Paraguay, the new colossus of South America.
---

| Is triggered by: Failure of journal entry The Paraguayan War |
|---|
| Trigger conditions: None |
| God have mercy. Gain modifier Shaken by Defeat Shaken by Defeat Country modifier −10% Prestige +10% Morale Loss −10% Morale Recovery for 10 years 10% of pops become more radical |

## References

1. ↑ Excluding Single-Party State
2. ↑ 2.0 2.1 2.2 Likely bug, comparison sign >= instead of <=
3. ↑ Technically, there are three different journal entries: **je_south_america_migration**, **je_central_america_migration**, and **je_american_west_migration** respectively. Everything about them is the same except for the trigger conditions and the ids. They are all on /Victoria 3/game/common/journal_entries/02_south_america_migration.txt

---

Primary reference files:
- /Victoria 3/game/common/journal_entries/00_patagonia.txt
- /Victoria 3/game/common/journal_entries/02_caudillo.txt
- /Victoria 3/game/common/journal_entries/02_paraguay.txt
- /Victoria 3/game/common/journal_entries/02_peru_bolivia.txt
- /Victoria 3/game/common/journal_entries/02_south_america_migration.txt
- /Victoria 3/game/common/journal_entries/02_south_american_national_identity.txt
- /Victoria 3/game/events/brazil/caudillo.txt
- /Victoria 3/game/events/brazil/culture_south_america.txt
- /Victoria 3/game/events/brazil/paraguay.txt
- /Victoria 3/game/events/brazil/patagonia_events.txt
- /Victoria 3/game/events/brazil/peru_bolivia.txt
- /Victoria 3/game/events/brazil/south_america_migration.txt
- /Victoria 3/game/events/patagonia.txt
