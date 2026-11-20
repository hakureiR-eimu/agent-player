---
title: Greek content
source: https://vic3.paradoxwikis.com/Greek_content
pageid: 8877
categories: [1.13, Scripted_content, Pages_with_obsolete_template_parameters, Articles_with_potentially_outdated_infoboxes]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

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
[Greece](Greece.md) has the following unique [journal entries](https://vic3.paradoxwikis.com/Journal_entries) and [events](Events.md). Some of them are shared with other Greek-culture nations.

## Decisions

id

### Annex the Ionian Islands

The Ionian Islands changed hands multiple times throughout the Napoleonic Wars, and were not integrated into the Greek state upon their independence. If we can obtain the consent of both the Ionian people and the government of their protectors, we may be able to negotiate a peaceful transition of power.
---

| Shown conditions: Has Greek primary culture Hasn't used this decision before Is independent Ionian Islands Is a subject of another country Is AI Top overlord is AI | Useable conditions: Is at peace Has researched Nationalism Owns at least three Greek homeland states Ionian Islands Is at peace Has cordial or better with country Top overlord is at peace with and has cordial or better with country |
|---|---|
| Effects: Triggers the event The Treaty of [London] |  |

id

### The Treaty of [London]

Through careful negotiations, [Great Britain] has agreed to cede the Ionian Islands to [Greece].
---

Flavor text:
"To promote good will between our nations and to bolster the spirit of the [Greek] people, the [King] has graciously cede the Ionian Islands. Our amical protectorate, under which the Islands benefited from our true and just assistance, is deemed at an end and we trust that the people of these isles will prosper under the benevolent care of our trusted friends."
---

| Is triggered by: Annex the Ionian Islands decision |
|---|
| Trigger conditions: None |
| A most agreeable solution. Annex Ionian Islands |

id

### Revive the Olympic Games

Revive the ancient Olympic games for a new era.
---

| Shown conditions: Is Greece | Useable conditions: Has researched Organized Sports Hasn't used this decision before |
|---|---|
| Effects: Gain Olympic Games Olympic Games Country modifier +100 Prestige permanently Gain Reviving the Olympic Gamess Reviving the Olympic Gamess Country modifier −10% Bureaucracy for two and a half years |  |

## The Greek State

id

### The Megali Idea

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.11. |
|---|---|

---

"The Greek is not only he who inhabits the kingdom, but also he who lives in Janina, or Thessaloniki, or Seres, or Adrianople, or Constantinople, or Trebizone, or Crete, or Samos, or any other country of the Greek history or race..."
—Ioannis Kolettis
Despite the establishment of an independent Greek state, most Greeks still live under foreign rule. A concerted effort must be made, through both diplomatic and military means, to incorporate the Greek Homelands into our government.
---

| Visibility conditions: Has Greek primary culture and owns a Greek homeland |  |
|---|---|
| Activation conditions: Has researched Nationalism Owns at least three Greek homeland states Is independent Is not a committed participant in any diplomatic play | Effects when activated: Triggers event: The Greek State |
| Completion conditions: Is at peace Is independent Is at least a minor power Depending on the chosen path: By default, owns at least 7 Greek homelands and has no insurrectionary movements If has embraced the Megali idea, owns all 15 Greek homelands and has at least 50 legitimacy If has chosen to pursue the title of East Rome, has any variant of Monarchy, owns all 12 Byzantine core states, has formed Byzantium and has at least 50 legitimacy | Effects when completed: Triggers event: [Greece] Rises Again |
| Failure conditions: One of the following: Is a subject Is in debt and rank is less than minor power | Effects when failed: Triggers the event Untenable Project |
| Each month Trigger the event Pursue the Title of Eastern Rome |  |

id

### The Greek State

The rise of nationalism has created an irredentist desire among our citizens to incorporate all the lands of the Greek people under a single Greek state.
---

Flavor text:
"We have cast aside centuries of Ottoman rule to bring the Greek state into being. Yet it is not enough. Many of our countrymen still live under the oppressive yoke of foreign rule, yearning for a country they can call their own. This dream can only be realized through the annexation of all the Greek lands, which we will achieve with or without the consent of their occupiers."
---

| Is triggered by: Journal entry The Megali Idea activation |
|---|
| Trigger conditions: None |
| Our claim to this land is irrefutable. We will embrace the Megali idea, changing the completion conditions of The Megali Idea Gain claims on the following states: Macedonia Western Thrace East Aegean Islands Crete If Turkey fully owns any of the above states: Lose −20 relations with Turkey If Russia has a claim on any state in the Balkans: Gain +10 relations with Russia Gain 10 infamy Expansion is not a priority for now. If Turkey fully owns Macedonia, Western Thrace, East Aegean Islands, or Crete: Gain +20 relations with Turkey If Russia has a claim on any state in the Balkans: Lose −10 relations with Russia |

id

### Pursue the Title of Eastern Rome

The expansion of the Greek state has led some of the most fervent nationalists to propose an even more ambitious project: the restoration of the Byzantine Empire through the conquest of [Eastern Thrace] and [Aydin].
---

Flavor text:
"That which yesterday would have seemed an absurd pipe dream is now within our grasp. The purple phoenix will rise again!"
---

| Is triggered by: Journal entry The Megali Idea monthly pulse |
|---|
| Trigger conditions: This event has not fired before Has embraced the Megali idea in the event The Greek State Owns the Ionian Islands Does not have the game rule Formable Nations set to Plausible (has game rule Formable Nations: All ) Has any variant of Monarchy Government legitimacy is at least 75 |
| Byzantium will be restored. We will pursue the title of East Rome, allowing us to form Byzantium and changing the completion conditions of The Megali Idea If Turkey fully owns Macedonia, Western Thrace, East Aegean Islands, or Crete: Lose −20 relations with Turkey Gain claims on Eastern Thrace and Aydin If Eastern Thrace/Aydin is not owned by Turkey, create a 10-infamy diplomatic incident with its owner If Russia has a claim on any state in the Balkans: Gain +10 relations with Russia Gain 20 infamy Expansion is not a priority for now. If Russia has a claim on any state in the Balkans: Lose −15 relations with Russia Gain +15 relations with the owners of Eastern Thrace and Aydin If both of these states are owned by the same country, gain +30 relations with their owner |

id

### [Greece] Rises Again

![Event trigger.png](https://central.paradoxwikis.com/images/3/35/Event_trigger.png) **The below description is one of several available for this event.**

Our irredentist agenda has been a success. The people of [Greece] celebrate.
---

Flavor text:
The [Ruler] of [Greece] delivers a speech that will resonate in the hearts of all [Greek] people for generations to come:
"A nation, which by its fall enlightened many other nations, today stands up again, and not as before, when it was divided into many small states, but as a united state with its own government, religion and political existence forever guaranteed by the constitution."
---

| Is triggered by: Journal entry The Megali Idea completion |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: [Greece] will continue to flourish. If we have pursued the title of East Rome: Gain Strength of a Nation Strength of a Nation Country modifier +10% Bureaucracy +200 Authority +15 Legitimacy (decaying) for 20 years Else, if we have pursued the Megali idea: Gain Strength of a Nation Strength of a Nation Country modifier +10% Bureaucracy +200 Authority +10 Legitimacy (decaying) for 20 years Else: Gain Strength of a Nation Strength of a Nation Country modifier +5% Bureaucracy +100 Authority +5 Legitimacy (decaying) for 20 years Always enabled: [Greece] has earned the respect it deserves. If we have pursued the title of East Rome: Gain Greek Nationalism Greek Nationalism Country modifier +20% Prestige (decaying) for 20 years Gain Prosperous Legitimacy Prosperous Legitimacy Country modifier +10 Legitimacy from government clout (decaying) for 20 years Else, if we have pursued the Megali idea: Gain Greek Nationalism Greek Nationalism Country modifier +15% Prestige (decaying) for 20 years Gain Prosperous Legitimacy Prosperous Legitimacy Country modifier +10 Legitimacy from government clout (decaying) for 20 years Else: Gain Greek Nationalism Greek Nationalism Country modifier +10% Prestige (decaying) for 20 years Gain Prosperous Legitimacy Prosperous Legitimacy Country modifier +5 Legitimacy from government clout (decaying) for 20 years Enabled if: Did not pursue the title of East Rome and does not fully own all of Eastern Thrace Aydin Hudavendigar Trabzon Repatriate our people to [Greece]. Gain Prosperous Legitimacy Prosperous Legitimacy Country modifier +10 Legitimacy from government clout |

id

### Untenable Project

![Event trigger.png](https://central.paradoxwikis.com/images/3/35/Event_trigger.png) **The below description is one of several available for this event.**

The aggressive pursuit of [Greece]'s irredentist project is no longer tenable.
---

Flavor text:
The tension in the room is palpable. Politicians and advisors argue over the sustainability to pursue [Greece]'s ambitious agenda. Each demands a responsible party be held accountable for the mismanagement of [Greek] resources used in this irredentist endeavor that has failed to manifest.
---

| Is triggered by: Journal entry The Megali Idea failure |
|---|
| Trigger conditions: None |
| Our failure is an embarrassment. If we have pursued the title of East Rome: Gain Failed Agenda Failed Agenda Country modifier −20% Prestige (decaying) for 20 years Eastern Thrace, Aydin, Hudavendigar, and Trabzon, if not fully owned: Remove Greek homelands All Greek pops move to capital state Else, if we have pursued the Megali idea: Gain Failed Agenda Failed Agenda Country modifier −15% Prestige (decaying) for 20 years Else: Gain Failed Agenda Failed Agenda Country modifier −10% Prestige (decaying) for 20 years Every interest group in government gains Stagnating Attraction Stagnating Attraction Interest group modifier −20% Interest group pop attraction (decaying) for 20 years Every interest group in opposition that is not marginalized gains Newfound Traction Newfound Traction Interest group modifier +15% Interest group political strength (decaying) for 20 years [Ruler] must be held accountable. If we have pursued the title of East Rome: Ruler gains Unpopular Leadership Unpopular Leadership Character modifier -50 Popularity Gain Bureaucracy Bears the Blame Bureaucracy Bears the Blame Country modifier −10% Bureaucracy (decaying) for 20 years Eastern Thrace, Aydin, Hudavendigar, and Trabzon, if not fully owned: Remove Greek homelands All Greek pops move to capital state Else, if we have pursued the Megali idea: Ruler gains Unpopular Leadership Unpopular Leadership Character modifier -30 Popularity Gain Bureaucracy Bears the Blame Bureaucracy Bears the Blame Country modifier −10% Bureaucracy (decaying) for 20 years Else: Ruler gains Unpopular Leadership Unpopular Leadership Character modifier -25 Popularity Gain Bureaucracy Bears the Blame Bureaucracy Bears the Blame Country modifier −5% Bureaucracy (decaying) for 20 years Every interest group in government gains Stagnating Attraction Stagnating Attraction Interest group modifier −20% Interest group pop attraction (decaying) for 20 years Every interest group in opposition that is not marginalized gains Newfound Traction Newfound Traction Interest group modifier +15% Interest group political strength (decaying) for 20 years |

## Bavarocracy

|  | Available only with the [National Awakening](National Awakening.md) DLC enabled. |
|---|---|

id

### Bavarocracy

|  | Available only with the [National Awakening](National Awakening.md) DLC enabled. |
|---|---|

---

Ever since its establishment in 1832, the nascent Greek kingdom—the first truly independent Greek state since the days of Constantine XI—has been under the thumb of King Otto and his Bavarian regents.
If the young king wants to prove himself as a worthy ruler of the Hellenes, he will have to take bold steps to manage the Bavarocratic Ire of his new subjects.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activation conditions: Game start | Effects when activated: Bavarocratic Ire set to 10 |
| Entry buttons: Convert to Eastern Orthodoxy Despite Greece being a firmly Orthodox country, King Otto has steadfastly clung to his native Catholic faith, causing considerable consternation among his newfound subjects. If Othonian rule is to endure among the Greeks, perhaps some personal sacrifices must be made? Visible if: Ruler is Catholic Has not used this button before Enabled if: King Otto follows the Catholic creed Effects: Ruler becomes Orthodox Ruler gains Suspected Crypto Catholic ( −10 Popularity) (decaying) for 20 years . Ruler has 10% chance of getting Psychological Affliction Heir becomes Orthodox Add small loyalists to Orthodox Add medium radicals to Catholics Decreases Bavarocratic Ire by 10 Lose −30 relations with Bavaria Lose −30 relations with Papal States |  |
| *Despite Greece being a firmly Orthodox country, King Otto has steadfastly clung to his native Catholic faith, causing considerable consternation among his newfound subjects.* If Othonian rule is to endure among the Greeks, perhaps some personal sacrifices must be made? |  |
| **Visible if:** Ruler is Catholic Has not used this button before |  |
| **Enabled if:** King Otto follows the Catholic creed |  |
| **Effects:** Ruler becomes Orthodox Ruler gains Suspected Crypto Catholic ( −10 Popularity) (decaying) for 20 years . Ruler has 10% chance of getting Psychological Affliction Heir becomes Orthodox Add small loyalists to Orthodox Add medium radicals to Catholics Decreases Bavarocratic Ire by 10 Lose −30 relations with Bavaria Lose −30 relations with Papal States |  |
| Entry modifiers: Foreign Administration Foreign Administration Country modifier −5% Authority +5% Radicals from low Legitimacy +10% Political Movement Pop Attraction |  |
| Completion conditions: One of the following All of the following Has Autocracy Home Affairs institution is at level 1 or higher All of the following Has voting Has Elected Bureaucrats Has Right of Assembly or Protected Speech Has 75 Legitimacy Bavarocratic Ire is below 10 | Effects when completed: Triggers event: Civilizer-King of the Hellenes |
| Failure conditions: One of the following: Bavarocratic Ire has been at 80 or above for 50 months. Currently this has been true for [x] months. | Effects when failed: Triggers the event The Downfall of King Otto The Fall of King Otto may open up new political opportunities. The end of Bavarocracy will enable us to put a Danish prince on the throne, acceptable to the Great Powers, or to establish the Second Hellenic Republic France , Great Britain , or Russia owing us an obligation will cause them to ignore the stipulations of the London Conference of 1832 , and allow us to elect one of their Princes as King of the Hellenes. A potential foreign king will come with the following ideology: Danish: Reformer British: Market Liberal Russian: Royalist French Oreanist: Market Liberal French Legitimist: Traditionalist French Bonapartist: Jingoist |
| Each month: The Bavarocratic Ire changes as follows: +1 for every South German character in the country +1 if the ruler is not Orthodox +1 if the ruler is not married +1 if there is no heir +1 if there is no voting franchise +1 if army size is less than 10 +The turmoil of every Greek homeland in the country that has at least 10% turmoil +1 if the country recently lost a war −1 for every owned Greek homeland −The loyalists of every Greek homeland in the country that has at least 10% loyalists −1 if the country recently won a war −1 if any owned Greek homeland has a university −1 if army size is more than 20 |  |

id

### Civilizer-King of the Hellenes

Having successfully steered the country through its tumultuous early years, King Otto has now established himself as a capable statesman at the helm of a stable government.
---

Flavor text:
Sipping his coffee, King Otto looked over his morning correpondence[sic]. Reports of roadside brigands, corruption scandals, and factional disputes, as per usual. But among the usual dreary reports were also hints of change. The effects of the recent changes in policing policy, the establishment of intellectual institutions, and the stirrings of a modern bureaucratic apparatus. Much remained to be done, but year by year the King found his morning work just a touch more enjoyable."
---

| Is triggered by: Journal entry Bavarocracy success |
|---|
| Trigger conditions: None |
| A new Pericles! Gain Othonian Renaissance Othonian Renaissance Country modifier +10% Arts Academy building Throughput +10% University building Throughput +10% Prestige for 10 years Ruler loses traits Inexperienced and Political Appointee Ruler gains traits Erudite and Basic Political Operator A new Alexander! Gain Othonian Staff Reforms Othonian Staff Reforms Country modifier −10% Morale Loss +10% Offense for 10 years Ruler loses traits Inexperienced and Political Appointee Ruler gains traits Celebrity Commander and Basic Offensive Planner For both options: If we have Autocracy: As we completed the journal entry by embracing autocracy, we will get the following reward: Gain Hellenic Order Hellenic Order Country modifier +5% Authority −10% Suppression impact on Political Movement attraction for 10 years If we have voting: As we completed the journal entry by embracing democracy, we will get the following reward: Gain Hellenic Freedoms Hellenic Freedoms Country modifier +5% Influence +10% Loyalists from Political Movements for 10 years |

id

### The Downfall of King Otto

Fed up with the Bavarian clique, a popular insurrection has broken out in [Athens] and deposed King Otto, last seen boarding a foreign schooner bound northwards. With the old King gone, the people has been asked by the provisional government to vote on his successor.
---

Flavor text:
"No printed ballot papers? Is this some sort of joke?"
"No, sir. You will merely write the name of the man you would like on the throne and submit it to me within the hour."
---

| Is triggered by: Journal entry Bavarocracy failure |
|---|
| Trigger conditions: None |
| A Prince of Denmark A Danish Reformer Prince will become King of the Hellenes as George I Gain +10 relations with every great power with Monarchy Gain +30 relations with Denmark A Republic Activate law Presidential Republic All interests groups that approve of monarchy gain Opportunist Republicanism Opportunist Republicanism Country modifier −3 Interest Group Approval for 5 years All interests groups that disapprove of presidential republic (bug?) gain Architects of the Second Republic Architects of the Second Republic Country modifier +2 Interest Group Approval +10% Interest Group Pop Attraction for 5 years Lose -10 relations with every great power with Monarchy Enabled if: Great Britain is a monarchy and owes Greece an Obligation A British Prince Great Britain no longer owes an obligation to Greece A British Market Liberal Prince will become King of the Hellenes as George I Gain +30 relations with Great Britain Enabled if: France is a monarchy and owes Greece an Obligation A French Prince France no longer owes an obligation to Greece If France is not ruled by a Legitimist, a Orleanist or a Bonaparte A French Prince of the ruling dynasty will become King of the Hellenes as George I If France is ruled by a Legitimist A Legitimist Traditionalist Prince will become King of the Hellenes as George I If France is ruled by a Orleanist A Orleanist Market Liberal Prince will become King of the Hellenes as George I If France is ruled by a Bonaparte A Bonaparte Reformer Prince will become King of the Hellenes as George I Gain +30 relations with France Enabled if: Russia is a monarchy and owes Greece an Obligation An Imperial Prince of Russia Russia no longer owes an obligation to Greece A Russia Royalist Prince will become King of the Hellenes as George I Gain +30 relations with Russia Enabled if: Garibaldi is alive Garibaldi Guiseppe Garibaldi will become King of the Hellenes as Iosif I All interests groups that approve of monarchy gain The Phrygian Crown The Phrygian Crown Country modifier −5 Interest Group Approval for 5 years All interests groups that disapprove of presidential republic (bug?) gain Architects of the Second Republic Architects of the Second Republic Country modifier +2 Interest Group Approval +10% Interest Group Pop Attraction for 5 years Lose -30 relations with every great power with Monarchy For all options: King Otto and his Bavarian aides will go into exile |
