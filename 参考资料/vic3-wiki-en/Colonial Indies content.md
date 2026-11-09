---
title: Colonial Indies content
source: https://vic3.paradoxwikis.com/Colonial_Indies_content
pageid: 6666
categories: [Potentially_outdated, 1.9, Expand, Scripted_content, Articles_with_potentially_outdated_infoboxes, Pages_with_obsolete_template_parameters, 1.10, Events, Journal]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.9.

|  | Please help improve this article or section by [expanding it](https://vic3.paradoxwikis.com/index.php?title=Colonial_Indies_content&action=edit). |
|---|---|

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
[East India](East India.md) has the following country-specific [events](Events.md), [journal entries](https://vic3.paradoxwikis.com/Journal_entries), and [decisions](Decision.md). [East Indies](East Indies.md) shares some of these entries, as well.

## Doctrine of Lapse

[East India](East India.md) can annex one of its princely state subjects once every two years.

id

### Doctrine of Lapse Invoked

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

The below description is one of several available for this event.
The [British] Resident has invoked the Doctrine of Lapse, citing our ruler's advanced age and failure to produce a male heir. By [British] decree, the territory of [Country] is to be immediately annexed into the [Top Overlord].
---

Flavor text:
At one PM sharp, the Resident entered. At five past one, tea was served to the the [Ruler Title] and [his] interpreter. At ten past one, the dictate was served. At fifteen, there was no more [Country], and no more [Ruler Title]. The Resident departed, steam still rising from his untouched cup.
---

| Is triggered by: Invoke Doctrine of Lapse diplomatic action |
|---|
| Trigger conditions: None |
| There is no way that we might resist. East India annexes [country] East India gains any gold reserves of this country Summon our army, we make our stand here. Start an independence diplomatic play against East India |

## Sepoy Mutiny

[East India Company](https://vic3.paradoxwikis.com/East_India_Company) starts with the journal entry *The Unstable Raj*. Failing to complete the entry causes [Hindustan](Hindustan.md), [Kurnool](https://vic3.paradoxwikis.com/Kurnool) and other subjects to revolt.

Bengal presidency governs the Bengal, Central India, and Delhi regions, starting with 250 stability; Bombay presidency governs the Bombay region with 285 stability; Madras presidency governs the Madras region with 270 stability.

Each of the presidencies' stabilities are modified weekly as follows:

- For every state in the presidency's region with more than 10% radicals, **subtract** the percentage of turmoil in that state
- For every state in the presidency's region with more than 10% loyalists, **add** the percentage of loyalists in that state
- For every subject with more than 75 liberty desire in the presidency's region, **−0.01** per point of liberty desire
- For every subject with less than 25 liberty desire in the presidency's region, **+0.01** per point of liberty desire below 25
- **+1** if Zamindars, Bhadraloks, Civil Cervants, Trade Unions, Hindu Priesthood, or Ryots are in government
- **−2** if Zamindars are **angry**, **−1** if they are **unhappy**, **+1** if they are **happy**[1]
- **−1** from very low military wages, **−0.5** from low military wages, **+0.5** from high military wages, **+1** from very high military wages
- **+1** from very low taxes, **+0.5** from low taxes, **−0.5** from high taxes, **−1** from very high taxes
- **−1** if any government interest group has a Utilitarian leader
- **−2** if the [East India Company](https://vic3.paradoxwikis.com/East_India_Company) does not have Total Separation
- **−1** if the [East India Company](https://vic3.paradoxwikis.com/East_India_Company) does not have Professional Army
- **−1** if the **Indian Famines** journal entry is active

id

### The Unstable Raj

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

Unrest is brewing in the three presidencies of the East India Company.
Troubled by harsh taxation regimes, increasing disrespect for local customs and territorial expansion at the expense of native princes, Indian opposition to Company rule has been mounting in recent years.
Worse still, discord can be found even within the proud ranks of the native sepoy regiments, who resent any challenge to their traditional status and privileges.
Sepoy Mutiny
!
If the stability of any presidency is
medium
(225) or less for 100 months, India will erupt in
open rebellion
. Currently this has been true for X months.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Game start | Effects when activated: None |
| Completion conditions: Has completed journal entry Consolidate Colonial Rule Average Standard of Living is greater than 10 less than 10% of the population is radical | Effects when completed: Trigger event The Honorable Company |
| Failure conditions: The stability of any presidency has been 225 or less for 100 months | Effects when failed: The Imperialism of Promise journal entry will no longer be available Adds journal entry Sepoy Mutiny Trigger event Mutiny! |
| Times out after 9000 days with the following effects: Same as failed |  |
| Each month ~7% chance of triggering one of: A Matter of Taste Kala Pani Suspected Proselytism |  |

id

### The Honorable Company

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

The benevolent despotism of the
East India Company
has led to marked improvement in every aspect of public life. The immediate threat of native rebellion has been vanquished, and the Company's rule firmly cemented.
---

Flavor text:
"Few governments, even under far more favorable circumstances, have attempted so much for the good of their subjects, or carried so many of their attempts to a successful and beneficial issue. A government of foreigners, over a people most difficult to be understood, and still more difficult to be improved, has a right to take pride in itself for having accomplished so much; and most certainly cannot be reproached, by any existing Government or people, with not having effected more."
— John Stuart Mill,
Memorandum of the Improvements in the Administration of India during the Last Thirty Years
---

| Is triggered by: Completion of The Unstable Raj Journal Entry |
|---|
| Trigger conditions: None |
| By command of Executive and Parliament. Upgrade the modifier Company Rule Company Rule Country modifier +200% Industrialists Political strength +250% Bureaucrats Political strength +50% Capitalists Political strength +50% Officers Political strength −90% Aristocrats Political strength −50 Legitimacy +75 Legitimacy from including head of state in government +15% Trade Center throughput Let our rule never be threatened again. Research Central Archives if it is not researched yet Enact Secret Police Gain Indian Imperial Police Indian Imperial Police Country modifier +15% Authority −25% Revolution progression speed −10% radicals from political movements +5% Mortality per turmoil |

id

### Mutiny!

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

The breaking point has been reached. Across India, sepoys are striking their regimental colors and taking up arms against the Company. Joined by disaffected locals of all ranks, they have seized power in cities across the continent.
---

Flavor text:
As the sepoy from Poona fires at his captain, a Muslim lad hands him more bullets. A Sikh sepoy, bleeding out from his wounds, takes in the sight. What would their forefathers say if they saw them fighting together instead of against each other? And then, as the life leaves him, a more pressing thought occers to him; what will their grandchildren say of their actions today? Waheguru, will they be proud? Ashamed? Will they even remember?
---

| Is triggered by: Failure or time out of The Unstable Raj Journal Entry |
|---|
| Trigger conditions: None |
| Immediate effects: Hindustan will revolt in Delhi If the Bengal presidency stability is Low or worse and Bengal does not exist, it will revolt in East Bengal If the Bengal presidency stability is Low or worse and Punjab does not exist, it will revolt in Punjab Hills If the Bombay presidency stability is Medium or worse, Satara will revolt in Bombay If the year is between 1845 and 1870, Satara gets the event In the Name of the Peshwa If the Bombay presidency stability is Low or worse and Sindh does not exist, it will revolt in Sindh If the Bombay presidency stability is Low or worse and Gujarat does not exist, it will revolt in Gujarat Kurnool will revolt in Kurnool if it exists. If it does not exist and Madras presidency stability is Medium or worse, it will be created. If the Bombay presidency stability is Critical and Carnatic does not exist, it will revolt in Madras If the revolting country already existed, it becomes independent and EIC's power bloc loses 500 leverage in it If the revolting country did not exist, it activates Monarchy and Oligarchy laws All of the above revolters gain War for Independence War for Independence Country modifier +25% Conscriptable battalions for 5 years All disloyal princely states revolt, become independent and EIC's power bloc loses 500 leverage in them; princely states with medium liberty desire stay neutral. |
| Option conditions Always enabled: Muster all loyal troops. Strike these rebels down.! Continue playing as East India Company Enabled if: Hindustan is revolting [Mughals Ruler Name] Zindibad! Long live the rightful Emperor! Play as Hindustan Enabled if: Satara is revolting Har Har Mahadev! Advance the banner of the Chhatrapati! Play as Satara Enabled if: Bengal is revolting Vande Mataram! Drive the Lal Patan from our shores! Play as Bengal Enabled if: Punjab is revolting Khalsa Ji Di Sarkar! The Sikh Empire will rise again! Play as Punjab Enabled if: Kurnool is revolting Forward, let us cleanse the Deccan of the firangi scourge. Play as Kurnool For all options: The uprisings start |

id

### Sepoy Mutiny

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

Mutiny and rebellion has broken out against the Company. If we are to maintain our authority, it must be crushed completely.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Failing "The Unstable Raj" | Effects when activated: None |
| Completion conditions: If they revolted, Hindustan , Bengal , Satara , and Punjab do not exist No secession is at 30% or more progress Is at peace | Effects when completed: If East India is a subject of Great Britain and not already become the Raj, Great Britain receives event The Jewel in the Crown Otherwise East India gains Company Crushed Mutiny Company Crushed Mutiny Country modifier +15% Authority for 5 years |
| Failure conditions: Any of the following: Hindustan has revolted, is at peace with East India and owns Delhi and Agra Bengal has revolted, is at peace with East India and owns East and West Bengal Satara has revolted, is at peace with East India and owns Bombay Punjab has revolted, is at peace with East India and owns Punjab and Punjab Hills Kurnool has revolted, is at peace with East India and owns Madras | Effects when failed: Trigger the event The Final Blow |

id

### A Matter of Taste

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

Ever since the adoption of the new, standard-issue Enfield rifle-musket, soldiers across the presidency armies have been complaining that the new gunpowder cartridges taste disgusting.
---

Flavor text:
As the Lieutenant Colonel of the 13th Regiment of Bengal Native Infantry, I faced a conundrum. As the regiment leader, I expected my troops to follow orders as and when I gave them. But, I had bit into the new cartridge myself and barely suppressed a gag. Would it be right to punish them when even I could not rise up to the task?
---

| Is triggered by: Monthly pulse of journal entry The Unstable Raj |
|---|
| Trigger conditions: Has researched Rifling Has not had this event before |
| A soldier’s life is hard enough, research ammunition improvement. Trigger the event A Tasteful Solution in 60 days Lose −20 relations with Great Britain Gain Cartridge Grease Experiments Cartridge Grease Experiments Country modifier 0.05% of GDP as government expenses for 5 years If they can’t stomach this, how will suffer the trials of war? Trigger the event First Signs of Trouble in 90 days Presidency stability will decrease in all the three presidencies by 1 every month for 5 years |

id

### A Tasteful Solution

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

Beeswax has been suggested as an alternative to the grease used on the cartridges. The troops are happy with this change. However, some are asking what changed.
---

Flavor text:
The soldiers sat around the canteen that night, pleased that the company had provided them with better cartridges.
"So, if these new cartridges use beeswax" asked a sepoy, chewing his roti, "then what did the old ones use?"
"What does it matter" replied a young sepoy, "so long as they don’t smell like your mother, I’ll bite into them."
---

| Is triggered by: Event A Matter of Taste |
|---|
| Trigger conditions: None |
| Explain to the troops that beeswax replaced a factory-made grease. 75% chance of triggering the event First Signs of Trouble in 90 days Hindu and Sunni Servicemen become more radical: 75% chance that 2% of pops become more radical 25% that 5% of pops become more radical |

id

### First Signs of Trouble

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

Soldiers in the Bengal Presidency have heard rumors that the grease used on the cartridges is animal fat.
---

Flavor text:
The young subedar had not slept all night. He threw up again, panic twisting his gut, 'What if the rumors were true? Had he really bit into cow fat?
He looked at the temple across the road, 'Would he still be welcome there? What about home? What would happen to his wife? Their son? Or perhaps there was no cause for worry, the Captain had assured them it was just a chemical. The Captain wouldn’t lie to them!'
---

| Is triggered by: Event A Matter of Taste or A Tasteful Solution |
|---|
| Trigger conditions: None |
| Reassure the soldiers it is not animal fat. Presidency stability will decrease in the Bengal presidency by 2 every month for a year Advance the timer for The Unstable Raj by 5 months 75% chance that 2% of Hindu and Sunni Servicemen pops become more radical Trigger the event An Unavoidable Mess in 30 days Suggest soldiers use their hands to open the cartridges if the taste offends them. One of the following: 75% that presidency stability will decrease in the Bengal presidency by 2 every month for a year and the event An Unavoidable Mess will be triggered in 30 days 25% that presidency stability will decrease in the Bengal presidency by only 1 every month for a year and the event won't trigger Gain Alternative Cartridge Handling Alternative Cartridge Handling Country modifier −15% Offense for 5 years Gain Caved to Sepoy Demands Caved to Sepoy Demands Country modifier −10% Authority −10% Bureaucracy for 5 years |

id

### An Unavoidable Mess

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

The rumors have taken root and some soldiers believe the cartridges were, or are, an attempt at forced conversion. They are refusing to fire weapons during drills.
---

Flavor text:
The Captain was worried, he was sure he had seen some off-duty soldiers following him as he exited the church. A tense air hung over the camp, the native regiments had been acting odd, breaking curfew, sticking together in large groups, carrying their rifles off-duty, and apparently some had refused to follow orders.
He counted the other British officers in the camp, a fair number, could they hold their own if the natives rebelled? A nervous laugh escaped his mouth. No, if it came to that they would be dead before their first reload.
---

| Is triggered by: Event First Signs of Trouble |
|---|
| Trigger conditions: None |
| Punish soldiers with hard labor. Advance the timer for The Unstable Raj by 5 months Presidency stability will decrease in the Bengal presidency by 2 every month for a year Trigger the event The First Domino Falls in 7 days Relieve them of their duty but let the rest continue Gain Lapses of Discipline Lapses of Discipline Country modifier +20% Morale loss for 5 years Gain Rogue Regiments Rogue Regiments Country modifier −10% Authority for 5 years Presidency stability will decrease in all presidencies by 1 every month for 5 years |

id

### The First Domino Falls

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

On hearing that troops have been sentenced to hard labor, sepoys from other regiments have broken rank and attempted to break their fellow soldiers free.
---

Flavor text:
Cawnpore Garrison.
To General [General Last Name]
Urgent.
Some 50 sepoys have barred themselves in the ammunition hold and are firing at any officers that approach. Trouble began at midnight when they got drunk and attacked their superior officer. Remaining regiments have been disarmed and asked to stay in their barracks. The loyal among them have advised that the mutineers intend to free the troops sentenced to hard labor.
Please Advice!
---

| Is triggered by: Event An Unavoidable Mess |
|---|
| Trigger conditions: None |
| Punish all who participate. Advance the timer for The Unstable Raj by 5 months Presidency stability will decrease in the Bengal presidency by 2 every month for a year 2% of Hindu and Sunni Servicemen pops become more radical Punish all troops. Presidency stability will decrease in all presidencies by 2 every month for 5 years 5% of Hindu and Sunni Servicemen pops become more radical |

id

### Kala Pani

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

Due to proscriptions in the Hindu faith against crossing seas, soldiers have been allowed an exemption from overseas service in the past. Some administrators now argue that this exception should be removed.
---

Flavor text:
"While it may seem convenient to demand overseas service of every soldier, this has already been the cause of conflict in the past. In '24, several regiments in Bengal staged a mutiny over a planned march to Burma, fearing they would be sent by sea. If we want to recruit from the higher castes, we must understand how seriously they take this taboo."
---

| Is triggered by: Monthly pulse of journal entry The Unstable Raj |
|---|
| Trigger conditions: Has not had this event before Is at war Any Servicemen pop is Hindu |
| It is necessary to account for these local traditions. Presidency Armies gain Overseas Service Exemption for Hindus Overseas Service Exemption for Hindus Interest Group modifier −2 Approval for 5 years If a subject of Great Britain , lose −20 relations with them They must serve wherever they are needed! 10% of Hindu Officers and Servicemen pops become more radical Presidency stability will decrease in all the three presidencies by 1 every month for 5 years |

id

### Suspected Proselytism

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

The presence of [Protestant] Clergymen in [State] has caused some locals to suspect that [East India] is planning to attempt converting people to Christianity.
---

Flavor text:
"That the Company seeks to impose their own ideas of civilization on us is well known. Who is to say the next step is not mass conversions? They pretend to respect our faith to keep the peace, but have they not all along painted it as merely another cultural element inferior to their own? Surely they are just biding their time for the eventual project of forcing us all to adopt their beliefs."
---

| Is triggered by: Monthly pulse of journal entry The Unstable Raj |
|---|
| Trigger conditions: Has not had this event with 3 years Any state has both: A Hindu, Shiite, or Sunni pop A Christian Clergymen pop |
| It couldn't be further from the truth. [State] gains Promised No Proselytization Promised No Proselytization State modifier −100% Conversion for 10 years If Hindu Priesthood leader has Minoritarian Traditionalist, Hindu Priesthood gains Promised No Missionaries Promised No Missionaries Interest Group modifier −2 Approval for 5 years 5% of [Protestant] pops in [State] become more radical If they are there to promote their faith, they may do so. 2% of Hindu, Shiite, and Sunni pops in [State] become more radical 5% of [Protestant] pops in [State] become more loyalist Presidency stability will decrease in all the three presidencies by 1 every month for 5 years |

id

### The Jewel in the Crown

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

The rule of the [East India] has ended, and the [British] government will now take a greater role in Indian affairs. History shall mark this day as the inception of the British Raj.
---

Flavor text:
"As long as we rule India, we are the greatest power in the world. If we lose it, we shall drop straight away to a third-rate Power. Only through despotic methods can we extract from India what the Empire requires."
---

| Is triggered by: Either: Decision Proclaim the British Raj Completion of journal entry Sepoy Mutiny |
|---|
| Trigger conditions: Is Great Britain |
| Good riddance to Company rule. If East India is a chartered company, it becomes a colony East India: Disables Doctrine of Lapse action Activates Appointed Bureaucrats and Autocracy Activates law Caste System Codified, unless has Caste System Enforced Receives event End of the Company |

## Consolidate Colonial Rule

id

### Consolidate Colonial Rule

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

The frontier of our Indian territories has proven a consistent source of risk. We are surrounded by disorderly polities under arbitrary rulers which may threaten the integrity of our territory at any time. In order to ensure the security of our core holdings, those native sovereigns who still evade our rule must be brought to heel, and any hint of popular resistance crushed before it spirals out of control.
As we expand our administration across India, we will have the opportunity to establish new Princely States to aid our administration. Assuming direct rule over too much land will cause the liberty desire of our existing subjects to increase.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Game start | Effects when activated: None |
| Completion conditions: Has 120 or more months of progress No secession has above 50% progress 80% or more of the following state regions are completely owned by East India, its subjects, its top overlord, or its top overlord's subjects: Baluchistan Kashmir Mandalay Pashtunistan Pegu Punjab Punjab Hills Quetta Sagaing Shan States Sindh | Effects when completed: Triggers event A Solid Frontier Completes one objective of the journal entry The Unstable Raj |
| Failure conditions: Any of: Great Britain does not exist Is not a subject of Great Britain Is a Colony | Effects when failed: None |
| Each month without any secession above 30% progress Add one month of progress to completion |  |

id

### A Solid Frontier

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

A great Indian Subcontinent has been brought under East Indian rule. Those foolish princes who opposed us have either bent the knee or perished.
---

Flavor text:
"Colonial rule is held together by the collaboration of the Company and the Indian Princes. Over decades we have seduced the Indians with promises of wealth and prestige, of military ranks and noble titles. Their service has been rewarded, and by winning their favor the subcontinent is pacified."
---

| Is triggered by: Completion of Consolidate Colonial Rule Journal Entry |
|---|
| Trigger conditions: None |
| Loyal princes will keep the peace. Gain +30 relations with every princely state subject Capital will cement our rule. Industrialists gain Company Men Company Men Interest group modifier +3 Approval +20% Political strength for 10 years |

id

### The Baluchistan Agency

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

---

With our acquisition of Baluchistan, we have established the Baluchistan Agency to coordinate the governance of the region. Proposals have been put forth to return regions of Baluchistan to native rule.
---

Flavor text:
"A single state would increase our administrative responsibility. Let these small men rule their little pockets. Meanwhile we can focus on garrisoning our frontier. Ensure no Afghan, Persian, or Russian dreams of approaching us."
"Give five men five states to rule and you create five rulers who dream of uniting them all. India already has more princes than all of Europe, do you truly wish to add to that number?"
---

| Is triggered by: Monthly pulse |
|---|
| Trigger conditions: This event has not occured before Is British East India Company All of Baluchistan is owned by this country or a subject of this country's overlord A foreign treaty port is not counted Kalat does not exist |
| Option conditions Enabled if: Makran does not exist Distribute the Southern regions to our loyal princes. Create Kalat as a princely state subject Create Kharan as a princely state subject Create Las Bela as a princely state subject Create Makran as a princely state subject Always enabled: Partition the region, with Kalati authority over Makaran. Create Kalat as a princely state subject Create Kharan as a princely state subject Create Las Bela as a princely state subject Always enabled: Establish a nineteen gun salute state of Kalat. Create Kalat as a princely state subject Always enabled: The High Commissioner may take full control of the province. The liberty desire of every princely state will increase by 15 and relations will deteriorate by 10 |

id

### The Capture of Sindh

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

---

Prior to our acquisition of Sindh, the region was split between the various branches of the Talpur Dynasty. Proposals have been put forth to establish a princely state in Sindh, under compliant Talpur rulers.
---

Flavor text:
"Peccavi", the telegram said. The adjutant looked to his principal, and raised an eyebrow.
"Message follows: "Peccavi". A code phrase?"
The officer pulled his eyes upwards, away from the report he was reading. "I have sinned", he said.
"He has Sindh?"
"Yes, he has Sindh."
"I see."
---

| Is triggered by: Monthly pulse |
|---|
| Trigger conditions: This event has not occured before Is British East India Company All of Sindh is owned by this country or a subject of this country's overlord A foreign treaty port is not counted Sindh does not exist |
| Allow the Northern Talpur dynasty to remain in place. Create Khairpur as a princely state subject Establish all of Sindh as a nineteen gun salute state. Create Sindh as a princely state subject The High Commissioner may take full control of the province. The liberty desire of every princely state will increase by 15 and relations will deteriorate by 10 |

id

### The North-West Frontier

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

---

Our acquisition of Pashtunistan has brought our border to the Pamir Mountains. Proposals have been made to delegate the administration of this remote region to compliant native rulers.
---

Flavor text:
"Princely states so close to enemy borders? Irresponsible and foolhardy. We have won the territory, now let us keep it."
"Guarding territory and administering them are two different matters. Why expend men and resources running the state when we can let the locals rule and let their taxes fund our garrisons?"
---

| Is triggered by: Monthly pulse |
|---|
| Trigger conditions: This event has not occured before Is British East India Company All of Pashtunistan is owned by this country or a subject of this country's overlord Chitral does not exist |
| Distribute the Southern regions to our loyal princes. Create Chitral as a princely state subject Create Dir as a princely state subject Create Swat as a princely state subject Expand the territory of Chitral to the entire North. Create Chitral as a princely state subject The native rulers have proven to be unreliable. The liberty desire of every princely state will increase by 15 and relations will deteriorate by 10 |

id

### The Treaty of Amritsar

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

---

Our newly-acquired province of Kashmir was once a powerful kingdom in its own right. Proposals have been made to establish a new, powerful princely state to administer the region.
---

Flavor text:
"The Hindoos don't like the Mohammedan, the Mohammedan don't like the Sikhs and the Sikhs don't like anybody. What prince could possibly wrestle them all?"
"So instead of letting some foolhardy prince try to keep them all in check, you would make it our problem? Do you care so little for sleep?"
---

| Is triggered by: Monthly pulse |
|---|
| Trigger conditions: This event has not occured before Is British East India Company All of Kashmir is owned by this country or a subject of this country's overlord Kashmir does not exist |
| Establish Jammu and Kashmir as a twenty-one gun salute state. Create Kashmir as a princely state subject No such treaty is necessary. The liberty desire of every princely state will increase by 15 and relations will deteriorate by 10 |

id

### The Shan States

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

---

The newly acquired Shan States are organized as a complex patchwork of various Shan principalities. Proposals have been made to organize them as a confederation of princely states under their current forms of government, with a shared Resident.
---

Flavor text:
"These frontier areas are a great source of revenue but a nuisance to administer. Fragmented, and mountainous, it will be a while before our people are familiar with the terrain."
"Perhaps we can borrow a page from history. Bind the Shan Saophas under a federation. They can rule as they wish so long as the central fund gets its share. As time goes by, our collectors will learn the roads and we won't need for the Federation."
---

| Is triggered by: Monthly pulse |
|---|
| Trigger conditions: This event has not occured before Is British East India Company All of Shan States is owned by this country or a subject of this country's overlord Shan does not exist |
| Grant them autonomy under their own rulers, with a shared Resident.. Create Shan States as a princely state subject Incorporate them as a Shan District. The liberty desire of every princely state will increase by 15 and relations will deteriorate by 10 |

## Communal Divides

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

id

### Communal Divides

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

---

"Is it possible that two nations - the Mahomedans and the Hindoos - could sit on the same throne and remain equal in power?"
The history of Hindu-Muslim relations in India is both storied and complex, with episodes of collaboration and coexistence interwoven with ones of intolerance and cruelty. Nonetheless, for centuries, the two communities hobbled along under the auspices of their feudal masters. However, with the emergence of new, national identities and the increasing spread of ethno-religious nationalism, it is clear that the old ways must make way for the new. Few voices, however, agree upon what such new ways should entail. A nation in discord cannot hope to endure. In one way or another, unity must be achieved.

**The Two-Nation Theory**

Hinging on the belief neither Muslim nor Hindu can rule without oppressing the other, the so called two-nation theory has been gaining traction in recent years. As long as the Communal Divides Journal Entry is active, attraction to religious nationalist Political Movements will be increased.
---

| Visibility conditions: is East India has Nationalism has 5 or more indian homeland states with all of the following: sunni or shiite pops hindu pops |  |
|---|---|
| Activated by: Has researched Pan-nationalism Either: the hindu nationalist movement has greater than 5% support and greater than 50% radicalism the muslim nationalist movement has greater than 5% support and greater than 50% radicalism | Effects when activated: None |
| Entry buttons: Establish the Confederacy of India The conflict between Hindus and Muslims has become too deeply-rooted for half measures. Establishing two explicitly Muslim autonomous states in Bengal and the West will create regions where Muslims need not fear persecution, whilst presenting minimal risk to our territorial integrity. Enabled if: East India is at peace East Bengal is owned by East India or its subjects Punjab is owned by East India or its subjects Sindh is owned by East India or its subjects Kashmir is owned by East India or its subjects East India does not have any variant of State Religion enacted At least one of these: We have been granted Home Rule East India is not a Subject of another nation Effects: We will be known as the Confederacy of India Indusstan and Bengal will be established as autonomous Subjects within the framework of East India Company +10% hindu pops in East India Company become more Radical +5% sunni pops in East India Company become more Loyalist +2% shiite pops in East India Company become more Loyalist If we were to break our promise and forcefully reintegrate the Federation of Indusstan or the Federation of Bengal, we can expect massive unrest from our Muslim Pops. |  |
| *The conflict between Hindus and Muslims has become too deeply-rooted for half measures. Establishing two explicitly Muslim autonomous states in Bengal and the West will create regions where Muslims need not fear persecution, whilst presenting minimal risk to our territorial integrity.* |  |
| **Enabled if:** East India is at peace East Bengal is owned by East India or its subjects Punjab is owned by East India or its subjects Sindh is owned by East India or its subjects Kashmir is owned by East India or its subjects East India does not have any variant of State Religion enacted At least one of these: We have been granted Home Rule East India is not a Subject of another nation |  |
| **Effects:** We will be known as the Confederacy of India Indusstan and Bengal will be established as autonomous Subjects within the framework of East India Company +10% hindu pops in East India Company become more Radical +5% sunni pops in East India Company become more Loyalist +2% shiite pops in East India Company become more Loyalist If we were to break our promise and forcefully reintegrate the Federation of Indusstan or the Federation of Bengal, we can expect massive unrest from our Muslim Pops. |  |
| Entry modifiers: gain Heightened Intercommunal Tensions Heightened Intercommunal Tensions Country modifier +25% Radicalism increases for the Violent Hostility Status +25% Radicalism increases for the Cultural Erasure Status +25% Radicalism increases for the Open Prejudice Status |  |
| Completion conditions: At least one of these: The Muslim-majority provinces of India have been granted autonomy under a confederal system. All of these: At least one of these: The identifying Pop Support of the Muslim Nationalist Movement is less than 5% The Movement Activism of the Hindu Nationalist Movement is less than 25% At least one of these: The identifying Pop Support of the Muslim Nationalist Movement is less than 5% The Movement Activism of the Muslim Nationalist Movement is less than 25% All Indian Political Movements are not Insurrectionary | Effects when completed: Trigger event The One-Nation Theory |
| Failure conditions: East India or its Subjects have no States in the State Regions of East Bengal, Punjab, Sindh, and Kashmir. East India is at peace | Effects when failed: Trigger event The Great Divide |
| Each month ~7% chance of triggering one of: A Dangerous Idea An Eye for an Eye Our Way or No Way No Voice, No Right |  |

|  | Please help improve this article or section by [expanding it](https://vic3.paradoxwikis.com/index.php?title=Colonial_Indies_content&action=edit). |
|---|---|

## Dravidian Movement

id

### Dravidian Movement

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

---

The common people of
East India Company
have responded to the disproportionate representation and political power of Brahmins. After a series of anti-Brahmin conferences, the Dravidian Movement has formed and set a new agenda to oppose Brahmin dominance. They seek to remove caste distinctions from law and government administration.
---

| Visibility conditions: Does not have law Affirmative Action |  |
|---|---|
| Activated by: Has researched Human Rights Does not have law Affirmative Action | Effects when activated: Trigger event Unequal Opportunities |
| Completion conditions: At least one of these: Ryots in government Ryots are powerful At least one of these: has enacted any variant of Caste Not Enforced has enacted any variant of Affirmative Action | Effects when completed: Trigger event Equality At Last |
| Failure conditions: Ryots are Marginalized At least one of these: Has passed the Indian Home Rule Act is not a subject of another nation At least one of these: has enacted any variant of Caste System Enforced has enacted any variant of Caste System Codified | Effects when failed: Leader of Ryots steps down |
| Each month ~8% chance of triggering one of: The Non-Brahmin Manifesto Untouchables and Outcasts |  |

id

### Unequal Opportunities

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

Tension between castes has been more pronounced since a recent census revealed the disproportionate representation of Brahmins in government jobs and highlighted the limited qualifications for Non-Brahmins.
---

Flavor text:
"Praveen's resume, his two masters in economics and law, crumpled in his hands as he stormed away furiously from another rejection.
He knew he shouldn't be so angry or so surprised. He knew that when he moved to Calcutta, he would be far from the support of his forward-thinking university, and yet the blatant segregation shocked him. Despite his qualifications he was struggling to feed himself, while others, equally educated, enjoyed chai in manors. What infuriated him most was how the guards barred the way for him. As if they were any better than him in the eyes of the lords they so dearly guarded.

---

| Is triggered by: The Dravidian Movement Journal Entry |
|---|
| Trigger conditions: None |
| The Ryots will champion for change gain Against Brahmin Dominance Against Brahmin Dominance Country modifier 2.0 Ryots Approval for 5 years gain a Ryots Social Democrat atheist agitator of Tamil culture with traits Direct Brave Erudite Appeasement of British league of Loyalists changes by -1.0 Great Britain has their reasons to support this. gain Supported Brahmin Dominance Supported Brahmin Dominance Country modifier +5% Influence for 5 years gain a Ryots Social Democrat atheist agitator of Tamil culture with traits Direct Brave Erudite gain Overlord’s Agenda Overlord’s Agenda Country modifier -0.05 Weekly Liberty Desire for 5 years |

id

### The Non-Brahmin Manifesto

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

The Non-Brahmin Manifesto has been circulating in Calcutta, causing tension between the
Ryots and the
Civil Servants.
---

Flavor text:
"The two party leaders sat across from each other, and their aides listened intently as the two minds battled for the second hour now.
"Please, you must make the Justice Party see reason," the leader of the civil servants pleaded. "We must fight together, or we will fail!" "You will have us face the British lathis by your side, but tell me, when tomorrow comes, will you also have us govern by your side? The British have done me no more wrong than you have. Indeed, much of their deeds have been guided by your hands."

---

| Is triggered by: Monthly pulse of The Dravidian Movement Journal Entry |
|---|
| Trigger conditions: None |
| That manifesto is unpatriotic! Indian relations towards Great Britain improves by 10 Civil Servants gets Argument To Be Made Argument To Be Made Country modifier +10% Interest Group Political Strength for 5 year Perhaps the manifesto makes valid points. +5.0% of middle strata pops in the capital state become more loyalist Ryots gets Argument To Be Made Argument To Be Made Country modifier +10% Interest Group Political Strength for 5 year |

id

### Untouchables and Outcasts

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

To assert their rights, the Dalit community drank from a public water tank that they had been denied access to. This nonviolent protest was led by Bhimrao Ramji Ambedkar and, in turn, met with a protest by Brahmin priests.
---

Flavor text:
"The young Dalit girl, Meena, watched the procession from afar, hidden behind a large tree. She had come here the day before with her mother, and they had drank from the water tank. It had seemed like a big event, though she had just been to skip work that day. But what she saw now horrified her, these priests were pouring cow urine and dung into the water. Had Meena drunk cow urine water? Either way, she would never drink from this polluted tank again."
---

| Is triggered by: Monthly pulse of The Dravidian Movement Journal Entry |
|---|
| Trigger conditions: None |
| Immediate effects: gain a Ryots Social Democrat hindu agitator of marathi culture with traits Direct literary Expert Political Operator |
| The actions of the priests are unacceptable. The created agitator gets Oppositon To Untouchability Oppositon To Untouchability Country modifier +50 Popularity for 5 year +10% of clergymen pops become more radical Let them keep each other distracted. The created agitator gets Oppositon To Untouchability Oppositon To Untouchability Country modifier +25 Popularity for 5 year East India gets Polluted Water Tank Polluted Water Tank Country modifier +2 Cultrural Acceptance for the Kshatriyas social class +2 Cultrural Acceptance for the Vaishyas social class -5 Cultrural Acceptance for the Shudras social class -5 Cultrural Acceptance for the Dalit social class for 5 years |

id

### Equality At Last

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

The success of the Dravidian Movement's agenda has overseen the enactment of a new law and improved quality of life for non-Brahmins.
---

Flavor text:
"The battle was far from over, this Praveen Pallar knew. Yet he could not help but smile as he took his seat in the simple government office, the fan above him gently cooling the sweat of his back.
Across from him he saw a Mr. Iyer, and to his left sat a Mr. Agastya. High caste Brahmins both. And here he was, a Pallar, holding the same position and pay as them. Neither seemed to meet his eyes. Yes, there was still work to be done, but for today, this would do. He thanked his allies who had marched and protested with him and flipped open his first file."

---

| Is triggered by: Completion of The Dravidian Movement Journal Entry |
|---|
| Trigger conditions: None |
| The Ryots has proven their competence East India gets Tides of Change Tides of Change Country modifier +5 Cultrural Acceptance for the Kshatriyas social class +5 Cultrural Acceptance for the Vaishyas social class +10 Cultrural Acceptance for the Shudras social class +10 Cultrural Acceptance for the Dalit social class +1 qualification growth for the Kshatriyas social class +1 qualification growth for the Vaishyas social class +1 qualification growth for the Shudras social class +1 qualification growth for the Dalit social class for 10 years East India gets Proof of Power Proof of Power Country modifier +20% Ryots political stength +20% authority for 10 years The future for non-Brahmins is bright. East India gets Tides of Change Tides of Change Country modifier +5 Cultrural Acceptance for the Kshatriyas social class +5 Cultrural Acceptance for the Vaishyas social class +10 Cultrural Acceptance for the Shudras social class +10 Cultrural Acceptance for the Dalit social class +1 qualification growth for the Kshatriyas social class +1 qualification growth for the Vaishyas social class +1 qualification growth for the Shudras social class +1 qualification growth for the Dalit social class for 10 years East India gets Future Minds Future Minds Country modifier +1 educatian access for the Kshatriyas social class +1 educatian access for the Vaishyas social class +1 educatian access for the Shudras social class +1 educatian access for the Dalit social class for 10 years |

## Imperialism of Promise

id

### Imperialism of Promise

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version Please help with verifying or updating older sections of this article. At least some were last verified for version 1.10. . |
|---|---|

---

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

---

Oversee a Utilitarian approach to colonial administration in
East India
Company.
We have a duty to promote the common good by any means necessary. Basic liberties and equal opportunities play a central role in policymaking. A
Utilitarian approach to colonial administration promises a strong force for progress both in the
East India
Company and around the world.
---

| Visibility conditions: is East India is chartered company |  |
|---|---|
| Activated by: has primary culture English any agitator or leader has Utilitarian ideology | Effects when activated: Trigger event An Extrordinarily Demanding Vision |
| Completion conditions: Average Standard of Living of East India is greater than, or equal to 10 Bureaucracy is greater or equal to 0 and the country is not about to enter a Bureaucracy deficit does not have any variant of Legal Guardianship enacted has enacted any variant of Compulsory Primary School enacted any variant of Public Schools enacted any variant of Slavery Banned At least one of these: has enacted any variant of Proportional Taxation has enacted any variant of Graduated Taxation | Effects when completed: Trigger event Good Governance For All |
| Failure conditions: At least one of these: has an active Sepoy Mutiny Journal Entry East India is no longer a Subject A Cultural Minority Movement is Seceding | Effects when failed: Trigger event False Promises |
| Invalidation conditions: does not have primary culture English | Effects when invalid: None |
| Times out after 30 years with the following effects: Trigger event A Project Without Progress |  |
| Each year ~33% chance of triggering one of: Undue Influence Imperial Liabilities Strengthening Ties Delayed Decisions The Study of Indian Society |  |

id

### Good Governance For All

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version Please help with verifying or updating older sections of this article. At least some were last verified for version 1.10. . |
|---|---|

---

The principles of Utilitarian ideology now play a central role in Indian policymaking. The administration has been reformed to function like a well-oiled machine.
---

Flavor text:
The administration's commitment to Utilitarianism has deepened with this success in steering the East India Company's development. While some still question the value of this approach to colonial
administration, staunch supporters have stepped forward to advocate for a utilitarian approach.

As the people of India carry on with their lives, time will tell if the fruit of the administration's labor will be as lasting and far reaching as all hope. The success is a beacon for future reform.
---

| Is triggered by: Completion of Imperialism of Promise Journal Entry |
|---|
| Trigger conditions: None |
| The future looks happy and bright. East India gains the modifier Utilitarian Influence Utilitarian Influence Country modifier -0.10 Weekly Liberty Desire +10% Education Access for 10 years Every interest group with a Utilitarian politician or agitator gains the modifier Utilitarian success Utilitarian success Country modifier +25% Interest Group Political Strength +10% Interest Group Pop Attraction for 5 years The industrialists lose the Malthusian ideology and gain the Utilitarian ideology permanently if East India gains independence or home rule the Individualist ideology will be replaced by Utilitarian |

id

### A Project Without Progress

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version Please help with verifying or updating older sections of this article. At least some were last verified for version 1.10. . |
|---|---|

---

While a Utilitarian approach to colonial administration was promising, it did not take root here in East India Company.
---

Flavor text:
The administration's commitment to Utilitarianism has wavered as the project has lost its staunchest supporters.
For a quiet moment, one man reflects on the lessons of the whole endeavor. "Perhaps we must be more practical with how our principles inform our policymaking," he muses.
---

| Is triggered by: Time out of Imperialism of Promise Journal Entry |
|---|
| Trigger conditions: None |
| Our people will prosper regardless. East India gains the modifier Unfulfilled Promises Unfulfilled Promises Country modifier +0.05 Weekly Liberty Desire for 10 years Each of the following gives 1 to completion score Average Standard of Living of East India is greater than, or equal to 10 Bureaucracy is greater or equal to 0 and the country is not about to enter a Bureaucracy deficit does not have any variant of Legal Guardianship enacted has enacted any variant of Compulsory Primary School enacted any variant of Public Schools enacted any variant of Slavery Banned At least one of these: has enacted any variant of Proportional Taxation has enacted any variant of Graduated Taxation If completion score is equal to or greater than 1, Every interest group with a Utilitarian politician or agitator gains the modifier Partial Utilitarian Success Partial Utilitarian Success Country modifier +10% Interest Group Political Strength for 5 years If completion score is equal to or greater than 3, the industrialists lose the Malthusian ideology and gain the Utilitarian ideology permanently if East India gains independence or home rule the Individualist ideology will be replaced by Utilitarian |

id

### False Promises

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version Please help with verifying or updating older sections of this article. At least some were last verified for version 1.10. . |
|---|---|

---

The chaos engulfing the East India Company serves as a testament to the failure of the Utilitarian project. Its proponents have been accused of irreversibly destabilizing the administration.
---

Flavor text:
The promise of a Utilitarian approach to colonial administration has not come to fruition. The failure has left the project's staunchest supporters disillusioned with mocking remarks directed towards them.
"I always knew the project would fail. The whole approach was fundamentally flawed from the beginning. There is no space for such an absurd agenda."
---

| Is triggered by: Failure of the Imperialism of Promise Journal Entry |
|---|
| Trigger conditions: None |
| They have no utility here. East India gains the modifier Broken Promises Broken Promises Country modifier +0.05 Weekly Liberty Desire for 10 years Every interest group with a Utilitarian politician or agitator gains the modifier Utilitarian Failure Utilitarian Failure Country modifier -10% Interest Group Political Strength for 5 years |

|  | Please help improve this article or section by [expanding it](https://vic3.paradoxwikis.com/index.php?title=Colonial_Indies_content&action=edit). |
|---|---|

## British Dictates

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

|  | Please help improve this article or section by [expanding it](https://vic3.paradoxwikis.com/index.php?title=Colonial_Indies_content&action=edit). |
|---|---|

## Indian Home Rule

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

id

### India Home Rule

Across
East India
, national consciousness is rising amongst the native Indian population. Native Indians educated in British schools and employed by the colonial government have begun to agitate for equal status within imperial institutions, greater economic opportunity, and the eventual establishment of home rule for all of India.
Whilst this Journal Entry is active, we will have the opportunity to petition Great Britain for greater autonomy and other local reforms. The chance that these petitions will be accepted is dependent upon the status of the progress bar.
---

| Visibility conditions: Is East India Is a subject Has researched Pan-nationalism |  |
|---|---|
| Activation conditions: Is not a chartered company Has an Indian National Movement Is a subject No primary cultures have South Asian heritage | Effects when activated: Save the top overlord of East India as [overlord] Triggers the event The Indian National Movement (India) for East India Adds The Indian National Movement to the journal of [overlord] |
| Entry buttons: Request Government Reform The nationalist calls for self-governance have grown too loud to ignore. We must petition our suzerain for permission to provide needed concessions in this direction. If [Overlord] accepts, we will be able to enact Distribution of Power Laws Enabled if: The progress bar' s value is greater than or equal to 50 Any political movement of type Religious Minority, Cultural Minority, Indian National, Hindu Nationalist, or Muslim Nationalist has support greater than or equal to 10% Has not used this action in the last 5 years Effects: [Overlord] triggers the event Indian Administration Requests Government Reform |  |
| *The nationalist calls for self-governance have grown too loud to ignore. We must petition our suzerain for permission to provide needed concessions in this direction. If [Overlord] accepts, we will be able to enact Distribution of Power Laws* |  |
| **Enabled if:** The progress bar' s value is greater than or equal to 50 Any political movement of type Religious Minority, Cultural Minority, Indian National, Hindu Nationalist, or Muslim Nationalist has support greater than or equal to 10% Has not used this action in the last 5 years |  |
| **Effects:** [Overlord] triggers the event Indian Administration Requests Government Reform |  |
| Completion conditions: Is a Dominion or Protectorate of [overlord] This nation allows for voting in elections Has enacted any variant of Elected Bureaucrats Any South Asian culture has a base acceptance of 60 or above | Effects when completed: Triggers the event The Indian Home Rule Act |
| Failure conditions: At least one of these: Has seceding countries broken away Indian National Movement activism is greater or equal to 65% Any civil war progress is greater than or equal to 75% and is a revolution | Effects when failed: Triggers the event Martyrdom |
| Invalidation conditions: [Overlord] does not exist or East India is not a subject of [overlord] |  |
| Every month, the *Home Rule* progress bar will advance from 0 to 100 (starting at 25) based on the following factors: +1 from reformist subject government (does not have the Government of India nor Presidency Armies in government) −1 from aggressive suzerain government ([overlord] has a Jingoist, Jingoist, Fascist, or Ethno-Nationalist interest group in government and does not have a Pacifist interest group in government) +1 from pacifist suzerain government ([overlord] has a Pacifist interest group in government and does not have a Jingoist, Jingoist, Fascist, or Ethno-Nationalist interest group in government) [2] Relations / 50 from suzerain relations with subject (LD−50) / 50 from liberty desire −1 from having the Indian Famines journal entry |  |

id

### The Indian National Movement

Across the
East India
, national consciousness is rising amongst the native Indian population. Native Indians educated in [overlord] schools and employed by the colonial government have begun to agitate for equal status within imperial institutions, greater economic opportunity, and self-governance for India.
Whilst this journal entry is active, the [Indian] national movement will have the opportunity to petition us for greater autonomy and other local reforms. The repercussions for denying these petitions are dependent upon the status of the
progress bar
.
If the activism of the Indian national movement gets too high, the movement will shift its focus towards
full independence
.
---

| Visibility conditions: Is Great Britain |  |
|---|---|
| Activated by: Activation of East India journal entry India Home Rule | Effects when activated: None |
| Entry buttons: Authorize Indian Self-Governance Despotic rule in India is clearly unsustainable. In order to preserve our colonial government in the region, we must offer additional opportunities for Indians to participate in their own governance. Visible if: East India is a subject of us and does not allow for voting in elections nor has enacted any variant of Elected Bureaucrats This button has not been used before Enabled if: Is at peace Any interest group in government has a stance of greater than on at least one of No Colonial Affairs and Cultural Exclusion East India : Has researched Political Agitation Any political movement of type Religious Minority, Cultural Minority, Indian National, Hindu Nationalist, or Muslim Nationalist has support greater than or equal to 10% Effects: The East India will pass Wealth Voting and Elected Bureaucrats ( East India triggers the event The [Montagu]-[Chelmsford] Reforms ) Dispatch Statutory Commission Our earlier reforms to the Indian administration have proven insufficient in the eyes of many nationalists. Dispatching a commission to study further constitutional reform will serve as a show of our continued commitment to Indian self-governance. Visible if: East India is a subject of us This button has not been used before Enabled if: Is at peace Has authorized Indian self-government (Either chose the last two options in event Indian Administration Requests Government Reform or used the button Authorize Indian Self-Governance ) East India : Allows for voting in elections Has enacted any variant of Elected Bureaucrats Has researched Political Agitation Any political movement of type Religious Minority, Cultural Minority, Indian National, Hindu Nationalist, or Muslim Nationalist has support greater than or equal to 10% Effects: If this action is not taken, the Indian Statutory Commission will be dispatched in 120 months Triggers the event The Indian Statutory Commission |  |
| *Despotic rule in India is clearly unsustainable. In order to preserve our colonial government in the region, we must offer additional opportunities for Indians to participate in their own governance.* |  |
| **Visible if:** East India is a subject of us and does not allow for voting in elections nor has enacted any variant of Elected Bureaucrats This button has not been used before |  |
| **Enabled if:** Is at peace Any interest group in government has a stance of greater than on at least one of No Colonial Affairs and Cultural Exclusion East India : Has researched Political Agitation Any political movement of type Religious Minority, Cultural Minority, Indian National, Hindu Nationalist, or Muslim Nationalist has support greater than or equal to 10% |  |
| **Effects:** The East India will pass Wealth Voting and Elected Bureaucrats ( East India triggers the event The [Montagu]-[Chelmsford] Reforms ) |  |
| *Our earlier reforms to the Indian administration have proven insufficient in the eyes of many nationalists. Dispatching a commission to study further constitutional reform will serve as a show of our continued commitment to Indian self-governance.* |  |
| **Visible if:** East India is a subject of us This button has not been used before |  |
| **Enabled if:** Is at peace Has authorized Indian self-government (Either chose the last two options in event Indian Administration Requests Government Reform or used the button Authorize Indian Self-Governance ) East India : Allows for voting in elections Has enacted any variant of Elected Bureaucrats Has researched Political Agitation Any political movement of type Religious Minority, Cultural Minority, Indian National, Hindu Nationalist, or Muslim Nationalist has support greater than or equal to 10% |  |
| **Effects:** If this action is not taken, the Indian Statutory Commission will be dispatched in 120 months Triggers the event The Indian Statutory Commission |  |
| Completion conditions: We have elected to grant East India Home Rule ( East India has completed the journal entry India Home Rule ) |  |
| Failure conditions: East India is in a revolution |  |
| Invalidation conditions: East India does not exist or is not a subject of us |  |
| Each month, random chance of the following events: Weight 400: Nothing Weight 10: Event The India League Weight 10: Event The Condition of India |  |
| Every month, the *Home Rule* progress bar will advance from 0 to 100 (starting at 25) based on the following factors: See India Home Rule progress bar |  |

id

### The Indian Home Rule Act

Following a long period of reform and negotiation with native Indian leaders, the British Parliament has passed a law reorganizing the former Raj into the Dominion of India.
---

Flavor text:
"From this day forth, the colony of India, that was under Direct Crown Rule, will form the Dominion of India. This Dominion, under the crown of the United Kingdom of Great Britain, will have its own legislative authority. Insofar as it does not encroach, resist, or counter the authority of the crown itself."
---

| Is triggered by: Completion of JE Indian Home Rule |
|---|
| Trigger conditions: None |
| We have seized our opportunity. Becomes India (BHT) All South Asian cultures with homelands in our nation will become primary cultures If has not enacted State Atheism: Sunni becomes the state religion if greater than 50% of pops follows Sunni religion Else Hindu becomes the state religion Remove modifiers Crown Rule Crown Rule Country modifier −90% Political Strength of Aristocrats +250% Political Strength of Bureaucrats −35 Legitimacy +50 Legitimacy from including the Head of State In Government +200% Industrialists Political Strength , Company Rule Company Rule Country modifier −80% Political Strength of Aristocrats +200% Political Strength of Bureaucrats +50% Political Strength of Capitalists −50 Legitimacy +65 Legitimacy from including the Head of State In Government +50% Political Strength of Officers +200% Industrialists Political Strength , Company Rule Company Rule Country modifier +15% Trade Center building Throughput −90% Political Strength of Aristocrats +250% Political Strength of Bureaucrats +50% Political Strength of Capitalists −50 Legitimacy +75 Legitimacy from including the Head of State In Government +50% Political Strength of Officers +200% Industrialists Political Strength , and/or Indian Imperial Police Indian Imperial Police Country modifier +15% Authority +15% Bureaucracy −25% Revolution Progression Speed +0.5% Mortality per Turmoil −10% Radicals from Political Movements The Government of India is renamed to Industrialists If the Industrialists had Colonialist, they lose it and gain Laissez-Faire If the Industrialists had Malthusian, they lose it and gain Individualist If the Industrialists had Enclavist, they lose it and gain Plutocratic The Presidency Armies is renamed to Armed Forces If the Bhadraloks had Sovereignist, they lose it and gain Patriotic If the state religion has become Sunni, the Hindu Priesthood is renamed to Sunni Ulema It loses Hindu Moralist and Hindu Moralist (British) if it had them and gains Moralist Otherwise if the state religion has become Hindu: It loses Moralist and Hindu Moralist (British) if it had them and gains Hindu Moralist All pops will immediately reconsider their interest group support Will have an election in 6 months |

id

### Indian Administration Requests Government Reform

Facing pressure from the Indian national movement, the government of the
East India
has requested our approval to permit democratic elections to positions in the Indian administration.
---

Flavor text:
The request was met in the House of Lords with some amusement.
"To vote," one lord remarked, "one must be literate. How does the Indian administration, with its abysmal literacy rates, expect the people to differentiate between Raj and Ram?"
---

| Is triggered by: Use of JE India Home Rule button Request Government Reform |
|---|
| Trigger conditions: None |
| Always enabled: Indians are incapable of responsible government. Due to the current state of the The Indian National Movement progress bar : If the progress bar progress is less than 70 : Appeasement of Indian National Movement changes by −1 2% of South Asian pops become more radical Otherwise if the progress bar progress is greater than or equal to 70 and less than 90 : Appeasement of Indian National Movement changes by −3 5% of South Asian pops become more radical Otherwise if the progress bar progress is greater than or equal to 90 : Appeasement of Indian National Movement changes by −5 10% of South Asian pops become more radical The The Indian National Movement progress bar will retreat by 25 Always enabled: A necessary step for stabilizing our administration. East India will be able to change its Distribution of Power law Enabled if: Enactment success chance for Wealth Voting in East India is greater than 0 Draw up the reform ourselves, and order it enacted. East India will be able to change its Distribution of Power law Will start enacting Wealth Voting in East India |

id

### Martyrdom

Amidst a peaceful protest in [Amritsar] against our suppression of the Indian national movement, a East India Army unit headed by [General] [Reginald Dyer] has opened fire on the crowd. Hundreds of Indians have been killed, and thousands wounded.
---

Flavor text:
"The events in [Amritsar] may have quelled the rebellious sentiment in the city, but they have provoked a national outrage.
Everywhere I go, I see people protesting, united. They all repeat the same mantra, a single word, 'Azadi', 'Freedom'."
---

| Is triggered by: Failure of JE Indian Home Rule |
|---|
| Trigger conditions: None |
| Immediate effects: If owns Punjab Hills (state) , save it as [Jallianwala Bagh state] and its culture as [culture] Otherwise, save random owned state in India (geographic region) as [Jallianwala Bagh state] and its culture as [culture] If date between 1900.1.1 and 1924.1.1, create character Reginald Dyer Otherwise, create a English (culture) general belonging to the Presidency Armies with ideology Authoritarian and traits War Criminal, Cruel, and Plains Commander and save as [Dyer] |
| This must be covered up immediately. Any hopes for reconciliation between British authorities and Indian subjects have come to an end. 500 [culture] pops in [Jallianwala Bagh state] lose their lives 10% of [culture] pops in [Jallianwala Bagh state] become more radical If the Civil Servants had Constitutionalist, they lose it and gain Republican The Indian National Movement gains the Martyrs of India Martyrs of India Movement modifier +35% Political Movement Activism for 20 years (decaying) Trigger the event Downward Spiral in 2 days |

id

### Downward Spiral

Despite our efforts to contain the situation, the news of the massacre in [Amritsar] has spread across [Punjab Hills]. Riots have begun to break out in major cities as Indians protest the killings.
---

Flavor text:
In response to the suppression of the Amritsar rebellion this Sunday, the people of India have taken to rioting.
"Down with British imperialism! Down with British dirty dogs!", were the words hurled at British administrators as they made their way to their offices on Monday morning.
---

| Is triggered by: Event Martyrdom |
|---|
| Trigger conditions: None |
| Always enabled: Detain [Dyer], and promise that justice will be done. [Jallianwala Bagh state] gets 5 devastation 5% of European pops become more radical Triggers the event The Disorders Inquiry Committee in 3 months Always enabled: Dispatch the Army to pacify the riots. [Jallianwala Bagh state] gets 10 devastation Triggers the event The Disorders Inquiry Committee in 3 months Enabled if: Either we or our overlord has researched Military Aviation Deploy the Air Force to disperse the crowds. [Jallianwala Bagh state] gets 15 devastation 2% of European pops become more loyal Triggers the event The Disorders Inquiry Committee in 3 months |

id

### The Disorders Inquiry Committee

As outrage grows over the
Presidency Armies's actions, a government commission has assembled to investigate the massacre in [Amritsar]. An interview with [General] [Dyer] has revealed [his/her] claimed motive - to preserve [his/her] honor.
---

Flavor text:
"Do you think you could have dispersed the crowd without firing?"
"If I did disperse them without firing and they chose to come back, I would have seemed a fool. They would have laughed at me."
"Supposing the passage to the garden was sufficient to allow the armoured cars to go in, would you have opened fire with the machine guns?"
"I think probably, yes."
"In that case, the casualties would have been much higher?"
"Yes."
---

| Is triggered by: Event Downward Spiral |
|---|
| Trigger conditions: None |
| Recall [Dyer] to [London] posthaste. [Dyer] will be permitted to resign without penalty, and return to [Great Britain] with [his/her] honor intact Overlord triggers the event Homecoming in 1 month We must have this man disciplined. [Dyer] will be stripped of [his/her] rank and awards, and deported back to [Great Britain] Presidency Armies gets Disciplined Massacre Perpetrator Disciplined Massacre Perpetrator Interest group modifier −2 Interest Group Approval for 5 years Overlord triggers the event Homecoming in 1 month |

id

### Homecoming

The former Brigadier General [Dyer] has returned to [Great Britain], following the conclusion of the inquiry into the [Amritsar] massacre.
[He/she] returns home in disgrace, stripped of rank and awards.
/
[He/she] has been greeted with a gift of money and a sword of honor by pro-imperialist citizens.
---

Flavor text:
The barkeep had not expected his usual crowd to be so divided this Friday evening; for one, there was no game that day. Yet the subject of [Reginald Dyer] had everyone up in arms. Half the people there wanted him dishonourably discharged; the butcher of Poonjab they called him. The other half were passing around a hat for donations. They wished to chip in for the Sword of Honor and purse that some newspaper was planning to give [Dyer] next week.
---

| Is triggered by: Event The Disorders Inquiry Committee |
|---|
| Trigger conditions: None |
| Always enabled: We can consider this affair concluded. If [Dyer] was disciplined: [Reginald Dyer] will retire into obscurity Otherwise: Every interest group with ideology Patriotic gets Duty Over Consequence Duty Over Consequence Interest group modifier +1 Interest Group Approval +5% Interest Group Political Strength for 5 years Every interest group with ideology Pacifist, Communist, Anarchist, or Vanguardist gets Disgraceful Massacre Disgraceful Massacre Interest group modifier −1 Interest Group Approval for 5 years [Reginald Dyer] retires Enabled if: [Dyer] has not been disciplined A fundraiser and sword? How depraved are they? 2% of academics pops become more loyal [Reginald Dyer] retires |

id

### The Indian National Movement (India)

National consciousness in India is beginning to grow amongst [British]-educated
Civil Servants and
Bhadraloks who find their financial interests clashing with [British] businesses. Their demands range from greater self-governance to full independence.
---

Flavor text:
Walking to the warehouse, I found my path barred by all the workers. They did not attack me but their intent was clear, no work would be done today. Aware of my frailty, I stood aside and went to have a second cup of tea. Here I overheard two workers, men who had served under me.
"We asked for food, and they made us starve. We asked to be heard, and they silenced us with bullets. And yet they ask us to serve? To obey? Well, no more. Let us see what they make of India without Indians."
---

| Is triggered by: Activation of journal entry India Home Rule |
|---|
| Trigger conditions: None |
| Immediate effects: If none exist, a new Independence Lobby is created in East India , targeting the overlord The Civil Servants and Bhadraloks join it If such a lobby already exists, the Civil Servants and Bhadraloks join it if not already members |
| We must keep an eye on this. The [ Independence Lobby] has formed, favoring greater autonomy from [Britain] Civil Servants and Bhadraloks get Indian National Movement Indian National Movement Interest group modifier +10% Interest Group Pop Attraction for 5 years (decaying) Their demands may have some merit. The [ Independence Lobby] has formed, favoring greater autonomy from [Britain] Civil Servants and Bhadraloks get Indian National Movement Indian National Movement Interest group modifier +20% Interest Group Pop Attraction for 5 years (decaying) (⨉2 multiplier) Appeasement of [ Independence Lobby] changes by 1 |

id

### The Indian National Movement (Britain)

National consciousness in India is beginning to grow amongst our native
Civil Servants and
Bhadraloks who find their financial interests clashing with [British] businesses. Their demands range from self-governance to full independence.
---

Flavor text:
Indian Subjects turn Traitorous! Call for Complete Independence
While many bureaucrats remain loyal to the British government, the general public has turned treasonous. Many have justified their traitorous intent by claiming self-rule as a birthright.
The House of Lords debated the matter. Some believe that this is a natural escalation after the failed debates over Home Rule. Others argue that this is the work of a few rebellious instigators. A member who wished to remain anonymous said, "Civil Servants will not lead India to capable self-government. The British Raj must continue, firm and unshaken in its administration of justice to all men."
---

| Is triggered by: Activation of journal entry The Indian National Movement |
|---|
| Trigger conditions: None |
| Keep a close eye on this. As long as the The Indian National Movement journal entry is active, we may receive reform requests from the East India They revolt against responsible governance itself. As long as the The Indian National Movement journal entry is active, we may receive reform requests from the East India The The Indian National Movement progress bar will retreat by 10 |

id

### The [Montagu]-[Chelmsford] Reforms

In response to growing nationalist agitation against [British] rule, the [British] has
[sic]
authorized a series of government reforms in the
East India
. They establish several elected bodies to assist in the governance of India.
---

Flavor text:
"WHEREAS it is the declared policy of Parliament to provide for the increasing association of Indians in every branch of Indian administration, and for the gradual development of self-governing institutions, with a view to the progressive realization of responsible government in [British] India as an integral part of the empire:
And whereas progress in giving effect to this policy can only be achieved by successive stages, and it is expedient that substantial steps in this direction should now be taken..."
---

| Is triggered by: Use of JE The Indian National Movement button Authorize Indian Self-Governance |
|---|
| Trigger conditions: None |
| Immediate effects: The leader of a random [overlord] government interest group with stance on at least one of No Colonial Affairs and Cultural Exclusion > is saved as [Montagu] The East India ruler is saved as [Chelmsford] |
| Enabled if: The Indian National Movement's activism is <= 0.5 A show of beneficence. Enables laws Wealth Voting and Elected Bureaucrats In 10 years, a [British] government commission will assess the results of these reforms ([Overlord] triggers the event The Indian Statutory Commission in 10 years ) Enabled if: The Indian National Movement's activism is > 0.5 Too little, and too late. Enables laws Wealth Voting and Elected Bureaucrats Increases liberty desire by 5 In 10 years, a [British] government commission will assess the results of these reforms ([Overlord] triggers the event The Indian Statutory Commission in 10 years ) |

id

### The Indian Statutory Commission

![Event trigger.png](https://central.paradoxwikis.com/images/3/35/Event_trigger.png) **The below description is one of several available for this event.**

The government has made the decision to immediately dispatch a commission to the
East India
to discuss constitutional reform. Political divides have emerged over whether the commission should have Indian members.
---

Flavor text:
"How could you propose such a course? If we are to claim we wish them to govern themselves, we must give them an opportunity to prove themselves."
"You must see that if we include them, the entire purpose of the Commission will be compromised. It will become a disunified body, divided both by party and religion. If one places two Indians on any sort of governing body, they will return with three opinions and a black eye."
"The candidates I have assembled are all Oxford-educated, sir. If what you say is true, the blame lies with us alone."
---

| Is triggered by: The reforms have been in place for 10 years or [Overlord] has chosen to Dispatch Statutory Commission |
|---|
| Trigger conditions: This event has not happened before |
| Always enabled: They are [British] subjects, and they will have a [British] commission. An all-white commission will be dispatched to the East India to discuss constitutional reform ( East India triggers the event The [Simon] Commission ) Enabled if: Any interest group in government is either: Trade Unions The leader of this interest group has an ideology sympathetic to the Indian cause (The leader is either Pacifist, Progressive , or Socialist ) Indian people must have a role in their own governance. A joint [British]-Indian commission will be dispatched to the East India to discuss constitutional reform ( East India triggers the event The [Simon] Commission ) |

id

### The [Simon] Commission

![Event trigger.png](https://central.paradoxwikis.com/images/3/35/Event_trigger.png) **The below description is one of several available for this event.**

The [British] government has dispatched a commission to [New Delhi] to assess the need for further constitutional reform in India. Several local Indian leaders have been invited to sit on the commission.
---

Flavor text:
The [British] had sent seven men, three of them Indian. Many of the Congress-men had been shocked when the news reached [New Delhi]. The moderates hailed this as a victory, already conjuring visions of equal status under a parliamentary system of their own. The radicals raised the point that a token Indian presence on the Commission could only serve the ends of the government, reducing protest to manageable levels before stabbing the hopeful populace in the back. For the first time in some years, the approach to take seemed truly ambiguous.
---

| Is triggered by: Event The Indian Statutory Commission |
|---|
| Trigger conditions: None |
| Immediate effects: If the Simon commission contained Indian members: Save the leader of a random [overlord] interest group that is either the Trade Unions or has a leader either Progressive or Socialist as [Simon], prioitizing interest groups in government [3] Otherwise, save the leader of a random [overlord] interest group in government as [Simon] |
| Enabled if: The Simon commission did not contain Indian members Something may come of it yet. If has an active India Home Rule journal entry: Gets Welcomed Statutory Commission Welcomed Statutory Commission Country modifier +5 Legitimacy −5% Radicalism increases for the Cultural Erasure Status −5% Radicalism increases for the Open Prejudice Status −5% Radicalism increases for the Violent Hostility Status for 5 years If the India Home Rule progress bar progress is greater than 75 : Appeasement of Indian National Movement changes by +3 2% of South Asian pops become more radical Otherwise if the progress bar progress is greater than 50 and less than or equal to 75 : Appeasement of Indian National Movement changes by +1 2% of South Asian pops become more radical Otherwise if the progress bar progress is greater than 25 and less than or equal to 50 : Appeasement of Indian National Movement changes by −2 5% of South Asian pops become more radical Otherwise if the progress bar progress is less than or equal to 25 : Appeasement of Indian National Movement changes by −4 10% of South Asian pops become more radical Otherwise 2% of South Asian pops become more radical (If the in game date is greater than 1928.1.1, trigger the event [Simon] Go Back in 30 days ) Enabled if: The Simon commission did not contain Indian members Proclaim a boycott of this insulting spectacle. Gets Boycotted Statutory Commission Boycotted Statutory Commission Country modifier −10 Legitimacy +10% Radicalism increases for the Cultural Erasure Status +10% Radicalism increases for the Open Prejudice Status +10% Radicalism increases for the Violent Hostility Status for 5 years If has an active India Home Rule journal entry: Otherwise if the progress bar progress is greater than 25 and less than or equal to 50 : Appeasement of Indian National Movement changes by −2 5% of South Asian pops become more radical Otherwise if the progress bar progress is greater than 10 and less than or equal to 25 : Appeasement of Indian National Movement changes by −4 10% of South Asian pops become more radical Otherwise 2% of South Asian pops become more radical Otherwise 5% of South Asian pops become more radical (If the in game date is greater than 1928.1.1, trigger the event [Simon] Go Back in 30 days ) Enabled if: The Simon commission contained Indian members A positive step for [British]-Indian relations. If has an active India Home Rule journal entry: Gets Welcomed Statutory Commission Welcomed Statutory Commission Country modifier +10 Legitimacy −10% Radicalism increases for the Cultural Erasure Status −10% Radicalism increases for the Open Prejudice Status −10% Radicalism increases for the Violent Hostility Status for 5 years (⨉2 multiplier) If the India Home Rule progress bar progress is greater than 75 : Appeasement of Indian National Movement changes by +6 5% of South Asian pops become more loyal Otherwise if the progress bar progress is greater than 50 and less than or equal to 75 : Appeasement of Indian National Movement changes by +4 2% of South Asian pops become more loyal Otherwise if the progress bar progress is greater than 25 and less than or equal to 50 : Appeasement of Indian National Movement changes by +2 Otherwise if the progress bar progress is less than or equal to 25 : Appeasement of Indian National Movement changes by +1 Otherwise appeasement of Indian National Movement changes by +1 and 2% of South Asian pops become more loyal Enabled if: The Simon commission contained Indian members Will anything come of it? If has an active India Home Rule journal entry: If the India Home Rule progress bar progress is greater than 75 : Appeasement of Indian National Movement changes by +4 5% of South Asian pops become more loyal Otherwise if the progress bar progress is greater than 50 and less than or equal to 75 : Appeasement of Indian National Movement changes by +3 2% of South Asian pops become more loyal Otherwise if the progress bar progress is greater than 25 and less than or equal to 50 : Appeasement of Indian National Movement changes by +2 Otherwise if the progress bar progress is less than or equal to 25 : Appeasement of Indian National Movement changes by +1 Otherwise appeasement of Indian National Movement changes by +1 Enabled if: The Simon commission contained Indian members The India Home Rule progress bar progress is less than or equal to 15 We will settle for nothing but full independence! Gets Boycotted Statutory Commission Boycotted Statutory Commission Country modifier −10 Legitimacy +10% Radicalism increases for the Cultural Erasure Status +10% Radicalism increases for the Open Prejudice Status +10% Radicalism increases for the Violent Hostility Status for 5 years 5% of South Asian pops become more radical |

## Indian Nationalism

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

id

### The Indian Nation

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version Please help with verifying or updating older sections of this article. At least some were last verified for version 1.10. . |
|---|---|

---

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

---

The collapse of goodwill between moderate nationalist leaders and the British colonial government has led to radicalization of the Indian national movement towards full independence. Those few who remain committed to the mission of the
industrialistsGovernment of India fear that, barring extraordinary efforts, the
East India
will soon be rendered ungovernable.
---

| Visibility conditions: is East India has Pan-nationalism., is subject |  |
|---|---|
| Activated by: Indian National Movement Activism is greater or equal to 65% East India is a Subject None of our Primary Cultures have the trait South Asian | Effects when activated: Activate The Indian National Movement journal for Overlord |
| Completion conditions: At least one of these: The Indian National Movement has become politically irrelevant India has peacefully achieved independence | Effects when completed: |
| Failure conditions: East India is in a Revolution | Effects when failed: Overlord gets the Event The Anarchy Overlord may choose to abandon India |
| Each month ~4.7% chance of triggering: The Salt March |  |

|  | Please help improve this article or section by [expanding it](https://vic3.paradoxwikis.com/index.php?title=Colonial_Indies_content&action=edit). |
|---|---|

## Indian Non-Cooperation Movement

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

id

### The Non-Cooperation Movement

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version Please help with verifying or updating older sections of this article. At least some were last verified for version 1.10. . |
|---|---|

---

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

---

The national movement in
East India
is gaining momentum, and its leaders have come up with a new campaign with a clear aim: economic and political non-cooperation, spurning collaboration with British authorities. They hope to demonstrate their movement's power by crippling the British trade  with Dominion of India.
---

| Visibility conditions: is East India has Pan-nationalism., is subject |  |
|---|---|
| Activated by: Indian National Movement is causing obstinance East India is a Subject No primary culture has the trait South Asian Economic Dependence is greater than Entangled (2.5) Sell Orders for Ammunition in overlord market greater than 200 | Effects when activated: Trigger event The Non-Cooperation Movement |
| Entry modifiers: National Swadeshi Movement +10% Private Construction Allocation +20% Radicals from Political Movements +20% Loyalists from Political Movements |  |
| Completion conditions: Economic Dependence is less than Entangled (2.0) East India is producing greater than 50% of goods in the overlord market | Effects when completed: Trigger event The Victory of Satyagraha |
| Failure conditions: The Indian National Movement has become politically irrelevant | Effects when failed: The Indian National Movement progress bar will retreat by 25 Trigger event Insufficient Self-Sufficiency |
| Invalidation conditions: East India is not a subject | Effects when invalid: None |
| Times out after 10 years with the following effects: The Indian National Movement progress bar will retreat by 25 Trigger event Insufficient Self-Sufficiency |  |
| Each month ~66% chance of triggering one of on a 5 year cooldown: Hartal! Swadeshi Protests |  |

|  | Please help improve this article or section by [expanding it](https://vic3.paradoxwikis.com/index.php?title=Colonial_Indies_content&action=edit). |
|---|---|

## Indian Railway

This journal entry could technically appear for any country, but is most likely to appear for [East India](East India.md) or [India](India.md).

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

id

### Purveyor of Progress

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

---

A grand railway network shall connect us all. It will bring great progress to the country and shape the future of our nation!
Construct a grand railway network to connect India.
---

| Visibility conditions: Is a player In present in India |  |
|---|---|
| Activation conditions: Owns a state in North India Owns a state in South India Has researched Railways | Effects when activated: None |
| Completion conditions: All state regions in the Delhi-Calcutta line West Bengal Bihar Awadh Agra Delhi have a railway All state regions in the Allahabad-Bombay line Agra Bundelkhand Central Provinces Malwa Bombay have a railway All state regions in the Bombay-Madras line Bombay Hyderabad Kurnool Madras have a railway All state regions in the Gujarat-Bombay line Bombay Gujarat have a railway | Effects when completed: Triggers event Railways for Prosperity |
| Invalidation conditions: Is not present in India | Effects when invalid: None |
| Every month, the following weighted random events can happen: (100) Nothing (10) Train Robbery in [State] (10) Stealing from the Crown (10) A Regional Famine (10) First-Class Accoutrements |  |

id

### Railways for Prosperity

The grand railway project has finally been completed. The new railway opens up new opportunities for people to travel, work, and connect across the country.
---

Flavor text:
With the completion of this station, the Raj's future is secure. Our network of trains will be the backbone of our trade, our military, our very government. Steam and Coal will run in the veins of the empire.
And this beautiful station, named after our great [Ruler Title], will be its beating heart.
---

| Is triggered by: Completion of Purveyor of Progress Journal Entry |
|---|
| Trigger conditions: None |
| Magnificent. If a state in Bombay is owned: Bombay gains Great Connections Great Connections State modifier +50% Migration Attraction +15% Railway throughput for long time Otherwise the owned Indian state with the highest GDP gains Great Connections Great Connections State modifier +50% Migration Attraction +15% Railway throughput for long time |

id

### Train Robbery in [State]

International press has been reporting on a train robbery in [State] led by [Culture] agitators.
---

Flavor text:
"If they were dacoits, many more would have died. These young men were stealing OUR money back for US. They made mistakes but their intentions are noble."
"If they are so noble, then what were they doing waving guns at their fellow countrymen? Now an innocent man is dead. I will never forget the sound of his wife crying."
---

| Is triggered by: Purveyor of Progress Journal Entry is active Is a subject Liberty desire is above 25% Any state: Has a railway Has discriminated pop Has an accepted pop with anglophone language trait |
|---|
| Trigger conditions: None |
| Option conditions Deny our [Culture] guards were overpowered. Country gains Controlling the Press Controlling the Press Country modifier +1 government expenses for normal time No use covering up our losses. Country gains Bad Press Bad Press Country modifier +5% Infamy for short time |

id

### Stealing from the Crown

Deliberations have started in the train robbery trial where the accused revolutionaries are charged with robbery and murder.
---

Flavor text:
The roar of the crowd gathered outside the courtroom warms the hearts of the defendants. The same roar makes it hard to hear the prosecutor. Relentless, he strives on.
"Hijacking, possession of illegal firearms, and murder. These in itself are a terrible act your honor. But these shameless men did them all, only to commit an even more heinous crime. They tried to steal from the very crown that cares for them. The crowd outside would call them heroes, I believe the law would call them traitors."
---

| Is triggered by: Purveyor of Progress Journal Entry is active Is a subject Liberty desire is above 25% Any state: Has a railway A railway robbery has happened Has not had a railway trial Has discriminated pop |
|---|
| Trigger conditions: None |
| Option conditions Make an example - interrogate them. Country gains Authoritative Measures Authoritative Measures Country modifier +10% Authority for normal time Add large radicals to discriminated culture Follow due process and order. Country gains Bad Press Bad Press Country modifier +5 Legitimacy for normal time Add medium radicals to discriminated culture |

id

### A Regional Famine

Mass exports of grains and crops have left the people of [State] vulnerable during a regional famine.
---

Flavor text:
Dear Elizabeth,
I was escorting the Crown's collections across India the other day when I saw a most terrible sight. A man, thin as the stick he held, stood guard in front of his starving wife and two children. When I asked my mates, what he was guarding, they explained that the village had taken to cannibalism.
---

| Is triggered by: Purveyor of Progress Journal Entry is active Is a subject Any state: Has a railway Has discriminated pop Ongoing famine |
|---|
| Trigger conditions: None |
| Option conditions Use rail transport to supply food-surplus. We cannot afford such measures. |

id

### First-Class Accoutrements

While many people are now embracing rail travel, tensions between communities are high as segregation holds strong.
---

Flavor text:
Two boys lean out of the train door, the fierce wind cooling them against the hot miserable day.
"I've heard that first-class has ceiling fans, and beds and their chairs are stuffed with cotton so you can sit for hours!"
"Well, I heard they get their own toilets."
"Well you heard wrong, Sirs and Madams don't need toilets."
"Is that why our compartment doesn't have one either?"
---

| Is triggered by: Purveyor of Progress Journal Entry is active Is a subject Any state: Has a railway Has discriminated pop Has an accepted pop with anglophone language trait |
|---|
| Trigger conditions: None |
| Option conditions Social matters are not urgent. Add medium loyalists to accepted culture Country gains Rising Tensions Rising Tensions Country modifier +0.10 Liberty Desire for normal time More tea stalls will lessen the tension. Add medium loyalists to [Discriminated Culture] Add medium radicals to [Accepted Culture] |

## Indian Famines

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

|  | Please help improve this article or section by [expanding it](https://vic3.paradoxwikis.com/index.php?title=Colonial_Indies_content&action=edit). |
|---|---|

## Indian Federation

id

### The Federation of India

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version Please help with verifying or updating older sections of this article. At least some were last verified for version 1.10. . |
|---|---|

---

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

---

Per the terms of the Indian Home Rule Act, any Princely State may petition for accession into the Dominion of India.
Whilst this Journal Entry is active, Princely State Subjects with low Liberty Desire and high Relations will occasionally petition for accession into the Federation. The Privy Purse:

The former rulers of the Princely States will be entitled to a state pension as compensation for accession to the Federation. The Privy Purse payments will add National Expenses of £ 7.60K times the number of Princely States annexed using this Journal Entry.
---

| Visibility conditions: has a princely state subject Either: is India All of the following: is East India has or has completed Indian Home Rule journal entry |  |
|---|---|
| Activated by: Either: has completed Indian Home Rule journal entry India is not a subject | Effects when activated: None |
| Completion conditions: All Princly States have joined India | Effects when completed: Trigger event India Indivisable |
| Failure conditions: At least one of these: Infamy of India is greater or equal to 100 India has enacted Council Republic | Effects when failed: Trigger event No Compromise |
| Each year ~50% chance of triggering: Request Accession is triggered if other prerequisites are met |  |

|  | Please help improve this article or section by [expanding it](https://vic3.paradoxwikis.com/index.php?title=Colonial_Indies_content&action=edit). |
|---|---|

## Victoria Terminus

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

id

### Victoria Terminus

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

|  | Available only with the [Pivot of Empire](Pivot of Empire.md) DLC enabled. |
|---|---|

---

Affiliates of the [Industrialists] have raised funds for
the creation of a grand Terminus
in Bombay. This elegant Terminus with additional railway platforms and adminstrative offices promises to elevate public opinion of India.
---

| Visibility conditions: Can research or has researched Steel-Frame Buildings Has English primary culture Owns Bombay |  |
|---|---|
| Activation conditions: Has researched Steel-Frame Buildings Bombay has a Railway | Effects when activated: Trigger event A Terminus Like No Other |
| Completion conditions: Bombay has Victoria Terminus If the game rule Monument Effects is set to Enabled , Victoria Terminus has at least 50% occupancy | Effects when completed: Triggers event An Architectural Marvel |
| Invalidation conditions: Any of: Does not have English primary culture Has dismissed the Victoria Terminus project Does not own Bombay | Effects when invalid: None |

id

### A Terminus Like No Other

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

The [Industrialists] have submitted a proposal to construct a grand Terminus in [Bombay]. The group has collected a significant sum of money to be used in its construction.
---

Flavor text:
Pipe smoke fills the small office as a group of officials consider the designs for a new train terminus.
"This is setting up to be a rather costly affair. Is rebuilding the station, really the best use of our resources?"
"My dear fellow, it is the era of the locomotives. Our earnings are proportional to the rate of delivery. And our current rate of delivery is comparable to a horse drawn cart."
---

| Is triggered by: Activation of Victoria Terminus Journal Entry |
|---|
| Trigger conditions: None |
| Option conditions Enabled if: Does not have Command Economy Weekly income to investment pool before expenses is at least 1000 Begin construction immediately. Industrialists gain Accepted Terminus Construction Accepted Terminus Construction Interest group modifier +2 Approval +10% Political strength for 5 years Always enabled: This funding should be redirected where needed. The Victoria Terminus project will be dismissed Industrialists gain Rejected Terminus Construction Rejected Terminus Construction Interest group modifier −3 Approval −10% Political strength for 5 years |

id

### An Architectural Marvel

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

The completed Victoria Terminus is a fusion of architectural influences and marks a new chapter for both [Bombay] and India as a whole.
---

Flavor text:
Two British men in suits stand outside the newly built terminus while a coolie carries their luggage.
"Well if it wasn't for the months long ship ride, I would have thought we were back in London."
"And therein lies the genius of its design. Our fellow countrymen see it as an expansion of British culture. While the locals see it as a respectful continuation of their Mughal heritage. Everyone is happy and no one is offended and business, above all, booms."
---

| Is triggered by: Completion of Victoria Terminus Journal Entry |
|---|
| Trigger conditions: None |
| This Terminus will serve all of India well. Bombay gains New Urban Juncture New Urban Juncture State modifier +25% Migration Attraction +25% Urban Center throughput for 10 years The world will marvel at our novel achievement. Gain Emblematic Growth Emblematic Growth Country modifier +5% Prestige for 10 years |

## Reform the Indies

This journal entry is for [East Indies](East Indies.md)

id

### Reform the Indies

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

It has become clear to the Company that exploiting the East Indies through the antiquated continuation of agrarian feudalism and slavery is not a viable strategy. We must transform the economy thoroughly, so that exploitation can be achieved through private enterprise and investment instead.
---

| Visibility conditions: Is East Indies |  |
|---|---|
| Activation conditions: Any of: Has law Free Trade Has law Mercantilism Does not have law Land-Based Taxation Does not have law Serfdom | Effects when activated: Sets GDP target at 50% above current GDP |
| Completion conditions: Has reached GDP target Either: Has law Free Trade Has law Mercantilism Has law Slavery Banned Does not have law Land-Based Taxation Does not have law Serfdom | Effects when completed: Triggers event Reforming the Indies Completes one objective of the journal entry Avert Mutiny Adds journal entry The Ethical Policy |
| Invalidation conditions: Is independent | Effects when invalid: None |

id

### Reforming the Indies

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

The economy of the Indies has been transformed under our diligent rule. With slavery and feudalism abolished, our vast territories are ripe for exploitation through private enterprise.
---

Flavor text:
"Famines, uprisings, and epidemics have been a staple of life under [Country] rule. But we are resolved to change that; we have liberated the peasants from their quotas so that they are not forced to hand over the meager handful of rice they need to feed their families. By replacing these harsh regulations with private employment we are sure that the wealth will trickle down to the locals."
---

| Is triggered by: Reform the Indies Journal Entry |
|---|
| Trigger conditions: None |
| Investors are beginning to show interest. Adds journal entry The Ethical Policy Gain Investment in the Indies Investment in the Indies Country modifier +20% Capitalists investment contribution efficiency for 10 years We should make greater use of local labor. Adds journal entry The Ethical Policy Gain Local Labor Force Local Labor Force Country modifier +10% Qualifications for 10 years |

id

### The Ethical Policy

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

Previous colonial administrations have allowed the people under their rule to wallow in poverty and ignorance, laboring under a government interested only in what it can extract from them. We have a chance to do better; to provide for these huddled masses a basic education as well as sufficient means to feed and clothe themselves.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Game start | Effects when activated: None |
| Completion conditions: Literacy rate is greater than 50% Average Standard of Living is greater than 15 | Effects when completed: Triggers event The Ethical Policy |
| Invalidation conditions: Is independent | Effects when invalid: None |

id

### The Ethical Policy

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

The [Country] has superseded the old colonialism. The people under our rule now enjoy a high standard of living and have access to a solid education.
---

Flavor text:
"Fifty years ago such a policy would have been unthinkable. Colonial administrators were concerned only with what they could extract, typically through coercion, from the wretches with the misfortune to live within colonial borders. We can proudly say that we have done better, that we have enacted an ethical policy of rule."
---

| Is triggered by: The Ethical Policy Journal Entry |
|---|
| Trigger conditions: None |
| Option conditions Enabled if: Has Religious Schools We should teach them good [Protestant] values. Gain Converting the Indies Converting the Indies Country modifier +100% Conversion for 10 years Always enabled: This is a land of opportunity. Gain Land of Opportunity Land of Opportunity Country modifier +50% Migration attraction for 10 years Always enabled: Are we not merciful? Gain Well Fed Subjects Well Fed Subjects Country modifier +100% Loyalists from political movements for 10 years |

## Independence event

[East India](East India.md) and [East Indies](East Indies.md) each have an event that triggers if they become independent.

id

### The End of British Rule?

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

Rudderless and without the support of its colonial overlord, the [East India] is on the verge of collapse. It seems that English rule is at an end.
---

Flavor text:
"Abandoning our post? What post, what army? In a few hours this place will be swarming with Hindus, or on fire, or both. Now stop complaining and pick up that sack. Take anything of value that isn't nailed down, and I'll secure passage to London."
---

| Is triggered by: Monthly pulse |
|---|
| Trigger conditions: Is East India Is independent Is at peace This event has not fired before |
| Option conditions Always enabled: India will be divided between the Princes. All owned states that are not the capital or Bengali homelands: If neighbors any subject, is given to a neighboring random subject Become Bengal Set primary culture to Bengali and state religion to Sunni Activate Monarchy and Oligarchy Remove EIC-specific country modifiers Kill all British, Scottish, and Irish characters Enabled if: Has researched Pan-nationalism This is the birth of an Indian nation. Become India Set primary cultures to Bengali, Assamese, Avadhi, Bihari, Gujarati, Kannada, Malayalam, Marathi, Oria, Punjabi, Rajput, Sindi, Tamil, and Telegu If the country does not have State Atheism and a majority of pops are Hindu, it becomes the state religion, If the majority of pops are Sunni, it becomes the state religion, If neither Sunni nor Hindu are the majority religion, Hindu becomes the state religion Remove EIC-specific country modifiers Kill all British, Scottish, and Irish characters that aren't immortal Always enabled: British rule must be maintained at all costs. 20% of pops become more radical |

id

### The East Indies' End

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

Rendered without support by the withdrawal of its colonial overlord, the [East Indies]'s administration has begun to collapse across the Indonesian archipelago. It seems that colonial rule is at an end at last.
---

Flavor text:
Across the islands, the silence rose like a wave. Cut telegraph wires, deserting policemen, farms that would no longer report their harvests. And then, the silence broke, and with it came annihilation.
---

| Is triggered by: Monthly pulse |
|---|
| Trigger conditions: Is East Indies Is independent Is at peace This event has not fired before |
| Option conditions Always enabled: The peoples of the archipelago have seized their right. All owned states that are not the capital or Javan homelands: If neighbors any subject, is given to a neighboring random subject or Malay Culture country Become Java Enabled if: Has researched Pan-nationalism One motherland, one nation, one language! Become Indonesia Always enabled: We will rage against the storm until we are saved. 20% of pops become more radical |

## References

1. ↑ Bug, it is supposed to also have "**+2** if they are **loyal**", but the script is put in the wrong order so this cannot trigger
2. ↑ Currently bugged, checks for Jingoist leader instead of intended Pacifist one
3. ↑ Can fail to find a valid character since the preceding event also allows for Pacifist but not this event. Likely a bug
