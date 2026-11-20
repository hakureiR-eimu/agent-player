---
title: Russian content
source: https://vic3.paradoxwikis.com/Russian_content
pageid: 6704
categories: [1.13, Scripted_content, Pages_with_obsolete_template_parameters, Events, Journal]
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
[Russia](Russia.md) has the following country-specific [events](Events.md), [journal entries](https://vic3.paradoxwikis.com/Journal_entries), and [decisions](Decision.md). Many of these require Sphere of Influence to be enabled.

## The Tunguska Event

This event is technically available to any country, but is most likely to appear for Russia given the requirements.

id

### The Tunguska Event

A massive explosion resounds across the region of Tunguska in [Upper Yeniseysk]. Scientists believe that a celestial object has collided with the Earth.
---

Flavor text:
"I lost my senses for a moment, but then my wife ran out and led me to the house. After that such noise came, as if rocks were falling or cannons were firing, the Earth shook, and when I was on the ground, I pressed my head down, fearing rocks would smash it. When the sky opened up, hot wind raced between the houses, like from cannons, which left traces in the ground like pathways, and it damaged some crops."
---

| Is triggered by: Yearly event pulse |
|---|
| Trigger conditions: Date is after 1 January 1908 Owns any part of Upper Yeniseysk This event has not been triggered for any country before |
| Always enabled: Fascinating, but irrelevant. No additional effect Enabled if: The Intelligentsia is in government This warrants scientific investigation. Gain Tunguska Scientific Expedition Tunguska Scientific Expedition Country modifier +5% Production Research Speed for 2.5 years Enabled if: The Devout are in government It is an omen! The Devout gain Tunguska Omen Tunguska Omen Interest group modifier +5% Interest group pop attraction for 2.5 years Enabled if: The Industrialists are in government Can we mine it? Upper Yeniseysk gains Tunguska Mining Expedition Tunguska Mining Expedition State modifier +10% Mines throughput for 2.5 years For all options Upper Yeniseysk gains 20% devastation |

## Trans-Siberian Railway

This journal entry is technically available to any country, but is most likely to appear for Russia given the requirements

id

### The Trans-Siberian Railway

Siberia is rich in resources but poor in infrastructure. We must build a great railway that will traverse the vast distance between Moscow and the Pacific!
---

| Visibility conditions: Owns Moscow Owns 80% of the states of the East Siberia and West Siberia regions No country has completed this entry |  |
|---|---|
| Activation conditions: Has researched Railways | Effects when activated: None |
| Completion conditions: Has a Railway in each of: Moscow Yaroslavl Nizhny Novgorod Cheboksary Kazan Ufa Chelyabinsk Ural Tobolsk Tomsk Krasnoyarsk Irkutsk Buryatia Chita Has a Railway in Yakutsk or Okhotsk Has a Railway in Amur or Primorye | Effects when completed: Trigger event The Trans-Siberian Railway |

id

### The Trans-Siberian Railway

"An extensive railway line now connects Moscow to [Okhotsk/Primorye]. The riches of Siberia are ours for the taking!"
---

Flavor text:
"This is a triumph for the [Russian] nation. [Russian] trains shall carry [Russian] coal, [Russian] sulfur, and [Russian] iron across the vast expanse of Eurasia!"
---

| Is triggered by: Completion of journal entry The Trans-Siberian Railway |
|---|
| Trigger conditions: None |
| Mine, boys! Every owned state in Siberia and Northeast Asia with a Railway gains Riches of Siberia Riches of Siberia State modifier +25% Coal Mines building Throughput +25% Iron Mines building Throughput +25% Sulfur Mines building Throughput +200% Migration Attraction for 5 years All aboard! Every owned state in Siberia and Northeast Asia with a Railway gains Siberian Railways Siberian Railways State modifier +25% Railway building Throughput +200% Migration Attraction for 5 years |

## Ruler of the East

This journal entry represents several of the treaties between Russia and China in the 1800s, which defined the borders between the two countries, mainly to Russia's advantage.

id

### The Ruler of the East

Our ambitions of becoming a Pacific naval power, and our colonial agenda in Central Asia, require that we resolve our long-standing border disputes with Great Qing in a manner favorable to Russia.
---

| Visibility conditions: Is Russia Is not a subject |  |
|---|---|
| Activation conditions: Has researched Nationalism Does not fully own Primorye, Ili, Tomsk, and Kirghizia | Effects when activated: Add claims to Amur, Primorye, Ili, Altai, and Kirghizia |
| Entry buttons: Present the Treaty of Aigun The territory of Amur is effectively isolated from the rest of China, and ripe for settlement. A military buildup in eastern Siberia should present enough of a threat for the Chinese government to surrender the territory without conflict. Visible if: Does not fully own Amur Hasn't taken this decision before Owns a state in both Chita and Okhotsk Any unrecognized AI country: Fully owns Amur, which is not the capital Has Manchu or Han primary culture Enabled if: Any country which is independent or a subject of Russia has any of: [1] Is at war and is not at war against Russia Owes an obligation to Russia Has 3 or fewer progress points in the Fragile Unity journal entry Has lower rank than unrecognized major power Russia is a great power Has an army with 20 or more battalions stationed in East Siberia or is AI Effects: Selects the unrecognized AI country that: Fully owns Amur, which is not the capital Has Manchu or Han primary culture If Russia is not overlord of or owed an obligation by that country, Create an incident with that country for 10 infamy Trigger event The Treaty of Aigun Press Claims on Primorye The Primorye region presents an opportunity to construct a warm-water Pacific port, greatly increasing our power projection potential. We could arrange a treaty to secure the territory by capitalizing on China's weakness. Visible if: Does not fully own Primorye Hasn't taken this decision before Owns a state in both Chita and Okhotsk Any unrecognized AI country: Fully owns Primorye, which is not the capital Has Manchu or Han primary culture Enabled if: Neighbors Primorye Any country with Manchu or Han primary culture: [2] Is independent or a subject of Russia Either Has 3 or fewer progress points in the Fragile Unity journal entry Has lower rank than unrecognized major power If unrecognized major power or higher rank, either: Is at war and is not at war against Russia Owes an obligation to Russia Russia is a great power Effects: Selects the unrecognized AI country that: Fully owns Primorye, which is not the capital Has Manchu or Han primary culture If Russia is not overlord of or owed an obligation by that country, Create an incident with that country for 10 infamy Trigger event The Beijing Treaty Issue the Chuguchak Protocol The acquisition of additional territories in Central Asia is a priority of the Russian government. With China in turmoil, an opportunity exists to expand into contested regions. Visible if: Does not fully own Altai, Ili, and Kirghizia Russia or a Russian subject fully owns both Semipalatinsk and Akmolinsk Hasn't taken this decision before Any unrecognized AI country: Owns any part of Altai, Ili or Kirghizia, which is not the capital Has Manchu or Han primary culture Enabled if: Any country with Manchu or Han primary culture: [3] Is independent or a subject of Russia Either Has 3 or fewer progress points in the Fragile Unity journal entry Has lower rank than unrecognized major power If unrecognized major power or higher rank, either: Is at war and is not at war against Russia Owes an obligation to Russia Effects: Selects the unrecognized AI country that: Owns any part of Altai, Ili or Kirghizia, which is not the capital Has Manchu or Han primary culture If Russia is not overlord of or owed an obligation by that country, Create an incident with that country for 15 infamy Trigger event The Chuguchak Protocol |  |
| *The territory of Amur is effectively isolated from the rest of China, and ripe for settlement. A military buildup in eastern Siberia should present enough of a threat for the Chinese government to surrender the territory without conflict.* |  |
| **Visible if:** Does not fully own Amur Hasn't taken this decision before Owns a state in both Chita and Okhotsk Any unrecognized AI country: Fully owns Amur, which is not the capital Has Manchu or Han primary culture |  |
| **Enabled if:** Any country which is independent or a subject of Russia has any of: [1] Is at war and is not at war against Russia Owes an obligation to Russia Has 3 or fewer progress points in the Fragile Unity journal entry Has lower rank than unrecognized major power Russia is a great power Has an army with 20 or more battalions stationed in East Siberia or is AI |  |
| **Effects:** Selects the unrecognized AI country that: Fully owns Amur, which is not the capital Has Manchu or Han primary culture If Russia is not overlord of or owed an obligation by that country, Create an incident with that country for 10 infamy Trigger event The Treaty of Aigun |  |
| *The Primorye region presents an opportunity to construct a warm-water Pacific port, greatly increasing our power projection potential. We could arrange a treaty to secure the territory by capitalizing on China's weakness.* |  |
| **Visible if:** Does not fully own Primorye Hasn't taken this decision before Owns a state in both Chita and Okhotsk Any unrecognized AI country: Fully owns Primorye, which is not the capital Has Manchu or Han primary culture |  |
| **Enabled if:** Neighbors Primorye Any country with Manchu or Han primary culture: [2] Is independent or a subject of Russia Either Has 3 or fewer progress points in the Fragile Unity journal entry Has lower rank than unrecognized major power If unrecognized major power or higher rank, either: Is at war and is not at war against Russia Owes an obligation to Russia Russia is a great power |  |
| **Effects:** Selects the unrecognized AI country that: Fully owns Primorye, which is not the capital Has Manchu or Han primary culture If Russia is not overlord of or owed an obligation by that country, Create an incident with that country for 10 infamy Trigger event The Beijing Treaty |  |
| *The acquisition of additional territories in Central Asia is a priority of the Russian government. With China in turmoil, an opportunity exists to expand into contested regions.* |  |
| **Visible if:** Does not fully own Altai, Ili, and Kirghizia Russia or a Russian subject fully owns both Semipalatinsk and Akmolinsk Hasn't taken this decision before Any unrecognized AI country: Owns any part of Altai, Ili or Kirghizia, which is not the capital Has Manchu or Han primary culture |  |
| **Enabled if:** Any country with Manchu or Han primary culture: [3] Is independent or a subject of Russia Either Has 3 or fewer progress points in the Fragile Unity journal entry Has lower rank than unrecognized major power If unrecognized major power or higher rank, either: Is at war and is not at war against Russia Owes an obligation to Russia |  |
| **Effects:** Selects the unrecognized AI country that: Owns any part of Altai, Ili or Kirghizia, which is not the capital Has Manchu or Han primary culture If Russia is not overlord of or owed an obligation by that country, Create an incident with that country for 15 infamy Trigger event The Chuguchak Protocol |  |
| Completion conditions: Fully owns Amur, Primorye, Ili, and Altai Fully owns or has subject who fully owns Kirghizia | Effects when completed: Trigger event The Ruler of the East |

id

### The Treaty of Aigun

An intense military buildup in Siberia has spurred negotiations between diplomats representing the Russian and [Country] states. A treaty has been constructed which will ensure mutual navigation rights on the Amur River, and transfer the territory of Amur to Russia.
---

Flavor text:
"The left bank of the Amur River, starting from the Argun River to the mouth of the Amur River, shall be the possession of the Russian state, and the right bank, downstream to the Ussuri River, shall be the possession of the [Country] state.
The areas and lands from the Ussuri River to the sea, until the determination of the boundary between the two states, shall be jointly owned by the [Country] and Russian states. Only vessels of the [Country] and Russian states may navigate the Amur, Sungari, and Ussuri rivers; vessels of all other foreign states shall not navigate these rivers..."
---

| Is triggered by: Ruler of the East journal button |
|---|
| Trigger conditions: None |
| Immediate effects: Selects the unrecognized AI country that: Fully owns Amur, which is not the capital Has Manchu or Han primary culture |
| Let this be carried out exactly and inviolably, for eternity. Amur is transferred to Russia [4] |

id

### The Beijing Treaty

"With our present leverage over the [Country] government, we have proposed a treaty to draw a formal border in Manchuria, formally transferring Primorye to Russia."
---

Flavor text:
"The articles of this treaty will come into force from the day they are exchanged by the representatives of one and the other state, and must be performed for all eternity sacredly and inviolably."
---

| Is triggered by: Ruler of the East journal button |
|---|
| Trigger conditions: None |
| Immediate effects: Selects the unrecognized AI country that: Fully owns Primorye, which is not the capital Has Manchu or Han primary culture |
| Open the territories to greater settlement. Absolves any obligation from [Country] to Russia Primorye is transferred to Russia Primorye gains The Settlement of Manchuria The Settlement of Manchuria State modifier +50% Migration attraction for 10 years There must be no delay in the expansion of our ports. Absolves any obligation from [Country] to Russia Primorye is transferred to Russia Primorye gains The Settlement of Manchuria The Settlement of Manchuria State modifier +25% Migration attraction +25% Port throughput +10% State construction efficiency for 10 years |

id

### The Chuguchak Protocol

We have begun to negotiate with representatives of [Country], in order to define a border between our nations in the West. There is much opportunity for territorial gains in the Central Asian region.
---

Flavor text:
It is our imperative to ensure that the lands of the Kyrgyz and Kazakhs, those loyal subjects of Russia, are united under a nation which is capable of providing security from the present state of banditry and petty theft within the region.
---

| Is triggered by: Ruler of the East journal button |
|---|
| Trigger conditions: None |
| Immediate effects: Selects the unrecognized AI country that: Owns any part of Altai, Ili or Kirghizia, which is not the capital Has Manchu or Han primary culture Selects a random subject of Russia with Kyrgyz primary culture |
| Option conditions Always enabled: Altai and Ili will be sufficient. Absolves any obligation from [Country] to Russia Altai and Ili are transferred to Russia Enabled if: Russia has a state in Kirghizia The territory of Kirghizia is also a necessary acquisition. Absolves any obligation from [Country] to Russia Altai, Ili, and Kirghizia are transferred to Russia Enabled if: A Russian Subject has Kyrgyz as a primary culture [Kyrgyz subject] territory will be made whole under our protectorate. Absolves any obligation from China to Russia [5] Altai and Ili are transferred to Russia Kirghizia is transferred to a random Russian subject with Kyrgyz as a primary culture |

id

### The Ruler of the East

By securing Primorye, the dream of Russia naval dominion over the Pacific has come closer to reality. The city of Vladivostok will become our new primary port in the East.
---

Flavor text:
This port can be considered the best of all. It reminds many of Olga, but only smaller than it, warmer and more pleasant. However, there are the same oaks all around, and the same picturesque mountains. In the lowlands the rivers murmur; there are many springs on the banks. Our post set up the other day, with its white tents, looks good in a group of oak trees that have not yet been cut down and have only just been cleared.
---

| Is triggered by: Completion of journal entry The Ruler of the East |
|---|
| Trigger conditions: None |
| Rebase the Siberian flotillas, with all due haste. If Primorye does not have a Naval Administration, immediately create a Level 2 Naval Administration Primorye gains The Ruler of the East The Ruler of the East Country modifier +15% Shipyards building Throughput +5% Armed Forces Political Strength permanently Gain Pacific Power Projection Pacific Power Projection Country modifier +10% Prestige from Navy Power Projection for 5 years The port of Vladivostok shall be the finest in our nation. If Primorye does not have a Port, immediately create a Level 2 Port Primorye gains The Ruler of the East The Ruler of the East Country modifier +15% Port building Throughput +15% Shipyards building Throughput +5% Industrialists Political Strength permanently 10% of upper strata pops in Primorye become more loyal |

## Caucasian War

|  | Available only with the [Sphere of Influence](Sphere of Influence.md) DLC enabled. |
|---|---|

This journal entry represents the Caucasian War.

id

### The Caucasian War

|  | Available only with the [Sphere of Influence](Sphere of Influence.md) DLC enabled. |
|---|---|

---

Our territorial ambitions in the Caucasus Mountains are being set back by fierce local resistance. We must crush all remaining resistance in order to secure our Southern border, and open the territories up for settlement.
Once the
Rifling
and
Logistics
technologies are researched, it will be possible to
escalate the war
, and launch a full-scale invasion of the rebellious states.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Game start | Effects when activated: Russian Kuban, North Caucasus, and Dagestan gain The Caucasian War The Caucasian War State modifier +20% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility pops +50% Tax waste +10% Mortality −3 Standard of living for Circassian pops −2 Standard of living for North Caucasian pops |
| Entry buttons: Escalate the Caucasian War With new and improved methods of protecting our supplies and waging war, we are finally capable of crushing the Caucasian rebels with the full force of our army. Visible if: Is independent Owns part but not all of Kuban, North Caucasus, and Dagestan Has a truce with either Circassia or Caucasian Imamate Has not used this button before Enabled if: Is a great power Circassia or Caucasian Imamate own part of Kuban, North Caucasus, and Dagestan Has researched Rifling and Logistics Effects: Removes the truce with Circassia and Caucasian Imamate |  |
| *With new and improved methods of protecting our supplies and waging war, we are finally capable of crushing the Caucasian rebels with the full force of our army.* |  |
| **Visible if:** Is independent Owns part but not all of Kuban, North Caucasus, and Dagestan Has a truce with either Circassia or Caucasian Imamate Has not used this button before |  |
| **Enabled if:** Is a great power Circassia or Caucasian Imamate own part of Kuban, North Caucasus, and Dagestan Has researched Rifling and Logistics |  |
| **Effects:** Removes the truce with Circassia and Caucasian Imamate |  |
| Completion conditions: Circassia does not exist Caucasian Imamate does not exist Kuban, North Caucasus, and Dagestan: Are fully owned by Russia Have 25% or less turmoil | Effects when completed: Trigger events The Fall of Circassia and The Imamate's End |
| Failure conditions: Owns no part of Kuban, North Caucasus, or Dagestan | Effects when failed: Triggers event Catastrophe in the Caucasus Kuban, North Caucasus, and Dagestan lose The Caucasian War The Caucasian War State modifier +20% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility pops +50% Tax waste +10% Mortality −3 Standard of living for Circassian pops −2 Standard of living for North Caucasian pops |
| Each month, weighted chance of: 200: no event 10: Failed Incursion into [Adversary] 10: Caucasian Supply Convoy Raided 10: Successful Incursion into [Adversary] 10: [Defector] Tribe Swears Fealty 50: Defections to the Caucasian Imamate |  |

id

### The Fall of Circassia

With the conclusion of our campaign in Kuban, the entirety of the former Circassian territories have fallen under our control. The land is now available for settlement by the Don Cossacks.
---

Flavor text:
"In this year, a deed has been accomplished almost without precedent in history: not one of the mountaineer inhabitants remains on their former places of residence, and measures are being taken to cleanse the region in order to prepare it for the new Russian population."
---

| Is triggered by: Weekly pulse or completion of journal entry The Caucasian War |
|---|
| Trigger conditions: Circassia does not exist This event has not triggered before |
| Option conditions Enabled if: Kuban has The Milyutin Memorandum The Milyutin Memorandum State modifier −15 Standard of living for Circassian pops +10% Kill rate +25% Devastation from battles +10% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility pops +25% Emigration push +10% Mortality The deportations will continue until the land is clear. 5% of Russian and Ukrainian pops become more loyalist Kuban gains Settlers’ Privileges Settlers’ Privileges (Decaying) State modifier +2 Standard of living for Russian pops +2 Standard of living for Ukrainian pops +50% Migration attraction +10% Mortality for 5 years (decaying) If Circassian culture is discriminated Open Prejudice, Cultural Erasure, and Violent Hostility , Activate journal entry Expulsion of Circassians Enabled if: Kuban does not have The Milyutin Memorandum The Milyutin Memorandum State modifier −15 Standard of living for Circassian pops +10% Kill rate +25% Devastation from battles +10% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility pops +25% Emigration push +10% Mortality Begin the process of integrating the Circassian peoples. Shared effect only For both options Kuban: Loses The Caucasian War The Caucasian War State modifier +20% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility pops +50% Tax waste +10% Mortality −3 Standard of living for Circassian pops −2 Standard of living for North Caucasian pops Gains The Caucasian War The Caucasian War (Decaying) State modifier −5 Standard of living for Circassian pops −5 Standard of living for North Caucasian pops for 5 years (decaying) Gains Russian and Ukrainian homeland |

id

### The Imamate's End

With the occupation of Dagestan and the surrender or defection of many of the former Caucasian naibs, the leader of the Imamate has finally surrendered to the Russian army, upon the request of the wives and children of his last followers.
---

Flavor text:
"The whole world knows about your exploits, and their glory will not fade. If you, submitting to the power of fate, go out today to the commander-in-chief and surrender to the generosity of the sovereign Tsar, you will save a thousand people who are alive and loyal to you from death. Complete your glorious deeds with an act of prudence and generosity, and the sardar will petition the sovereign to ensure the future of you and your family."
---

| Is triggered by: Weekly pulse or completion of journal entry The Caucasian War |
|---|
| Trigger conditions: Caucasian Imamate does not exist This event has not triggered before |
| Peace has been found in Chechnya at last. Dagestan and North Caucasus: 5% of pops become more loyalist Lose The Caucasian War The Caucasian War State modifier +20% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility pops +50% Tax waste +10% Mortality −3 Standard of living for Circassian pops −2 Standard of living for North Caucasian pops Gain The Caucasian War The Caucasian War (Decaying) State modifier −5 Standard of living for Circassian pops −5 Standard of living for North Caucasian pops for 2.5 years (decaying) Gain The Legacy of the Imamate The Legacy of the Imamate State modifier −85% Conversion −85% Assimilation +5% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility pops permanently There will be no peace whilst Shamil is still revered. Dagestan and North Caucasus: 20% of North Caucasian pops become more radical Lose The Caucasian War The Caucasian War State modifier +20% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility pops +50% Tax waste +10% Mortality −3 Standard of living for Circassian pops −2 Standard of living for North Caucasian pops Gain The Caucasian War The Caucasian War (Decaying) State modifier −5 Standard of living for Circassian pops −5 Standard of living for North Caucasian pops for 5 years (decaying) |

id

### Catastrophe in the Caucasus

The collapse of our rule in the Kuban and Dagestan regions has led to the severance of the Georgian Military Highway, and the end of the ability of the Russian state to exert power in the southern Caucasus.
---

Flavor text:
There is nothing left for us in these forsaken mountains but to be trapped between the Turks and the highlanders. Nothing is with us, any longer - God is high above, and the Tsar is far away.
---

| Is triggered by: Failure of journal entry The Caucasian War |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: Militarize the remaining garrisons, and hold at all costs! 5% of Officers become more loyalist 80% of pops in Russian-owned Tiflis, Baku, Elizavetpol, Armenia, and Kars become more radical Always enabled: Leave the region to the local warlords' mercy. If Russia owns Tiflis, Georgia becomes owner of Tiflis If Russia owns Elizavetpol, Georgia becomes owner of Elizavetpol Abkhazia becomes owner of a split state in Tiflis If Russia owns Baku, Azerbaijan becomes owner of Baku If Russia owns Armenia, Armenia becomes owner of Armenia If Russia owns Kars, Armenia becomes owner of Kars Armenia gains a split state in Elizavetpol If Georgia exists, it gains a split state in Armenia All released countries become unrecognized Enabled if: Has researched Nationalism Withdraw in the face of the nascent Caucasian states. If Russia owns Tiflis, Georgia becomes owner of Tiflis If Russia owns Baku, Azerbaijan becomes owner of Baku If Russia owns Armenia, Armenia becomes owner of Armenia If Russia owns Kars, Armenia becomes owner of Kars Elizavetpol is randomly given to Armenia or Azerbaijan Enabled if: Has researched Pan-nationalism Fully owns Tiflis, Baku, and Armenia Abandon the mountains to the Transcaucasian intelligentsia. Transcaucasia becomes owner of Tiflis, Baku, and Armenia If Russia owns Kars or Elizavetpol, they are given to Transcaucasia Transcaucasia enacts Presidential Republic and puts the Intelligentsia in government. |

id

### Failed Incursion into [Adversary]

An incursion we have launched from [State] into the territory claimed by [Adversary] has failed. The units dispatched have withdrawn, after suffering heavy losses amongst the rough Caucasian terrain.
---

Flavor text:
"They were in the trees - they had to have been warned before we began. They waited for us to be engulfed in that damned forest, before opening fire on us... the Major fell first, and our horses were cut down. How are we to manage this, sir? How are we to take this land, when we cannot say we control any land outside that shadowed by our own feet?"
---

| Is triggered by: Monthly pulse of journal entry The Caucasian War |
|---|
| Trigger conditions: Circassia or Caucasian Imamate exist |
| Immediate effects: Randomly selects Dagestan, North Caucasus, or Kuban as [State] Selects the other owner of [State] as [Adversary] |
| Cover the retreat with fire and cannon. [State]: Gains Failed Incursion Failed Incursion State modifier +15% Servicemen mortality for 2.5 years 5% of Circassian pops become more radical Gains 15% Devastation Withdraw the forces and quietly regroup. [State]: Gains Failed Incursion Failed Incursion State modifier +15% Servicemen mortality for 2.5 years 5% of Russian Officers become more radical Gains 5% Devastation If [State] has a Barracks, 2% of Russian Officers become more radical Armed Forces gain Ineffectual Incursion Ineffectual Incursion Interest Group modifier −2 Approval for 13 months |

id

### Caucasian Supply Convoy Raided

A convoy dispatched to provide needed ammunition and supplies to our forces in [State] has been ambushed by the forces of [Adversary]. In the struggle, much of its cargo was lost.
---

Flavor text:
By the time the relief force had arrived, the bodies had already begun to rot, men and horses entangled where they had fallen, their belongings stripped and carried away by enterprising hands. As they lay there, the highway was not been a territory of Russia, nor of any man at all - for its subjects were maggots, and its sovereign the Lord of the Flies.
---

| Is triggered by: Monthly pulse of journal entry The Caucasian War |
|---|
| Trigger conditions: Circassia or Caucasian Imamate exist |
| Immediate effects: Randomly selects Dagestan, North Caucasus, or Kuban as [State] Selects the other owner of [State] as [Adversary] |
| Seize resources from the locals to make up the deficit. [State]: Gains Raided Supply Train Raided Supply Train State modifier +5% Servicemen mortality −20% Infrastructure for 13 months Gains 10% Devastation Hold fast, and wait for a better-protected convoy. [State] gains Raided Supply Train Raided Supply Train State modifier +7.5% Servicemen mortality −30% Infrastructure for 13 months |

id

### Successful Incursion into [Adversary]

An incursion we have launched into the territory claimed by [Adversary] has succeeded, with several villages controlled by the mountaineers burnt to the ground, and the enemy fleeing.
---

Flavor text:
In the evening, the soldiers entered a town nestled between two mountains - humble, but prosperous, surrounded by fields of hardy crops.
In the morning, they left behind nothing but charred-black skeletons, surrounded by a desolate ring of ash.
---

| Is triggered by: Monthly pulse of journal entry The Caucasian War |
|---|
| Trigger conditions: Circassia or Caucasian Imamate exist |
| Immediate effects: Randomly selects Circassia or Caucasian Imamate as [Adversary] Randomly selects a split state owned by [Adversary] as [State] |
| Let none survive our scrutiny. [State]: Gains Villages Burned Villages Burned State modifier +7.5% Mortality −1.5 Standard of living −15% Agriculture throughput for 13 months Gains 15% Devastation 2% of pops in a neighboring Russian state become more radical We have made them inclined enough to submit. [State]: Gains Villages Burned Villages Burned State modifier +5% Mortality −1 Standard of living −10% Agriculture throughput for 13 months Gains 5% Devastation |

id

### [Defector] Tribe Swears Fealty

Cowed by our forces and unwilling to fight any longer, a [Defector] tribe formerly loyal to [Adversary] has sworn fealty to Russia.
---

Flavor text:
I, the below named, promise and swear by Almighty God, on His Holy Gospels, that I am in awe of, and bound to his Imperial Majesty, my true and innate most gracious great sovereign Emperor [Ruler], Autocrat of All the Russias, and to His Imperial Highness' lawful heir to the throne of All the Russias.
---

| Is triggered by: Monthly pulse of journal entry The Caucasian War |
|---|
| Trigger conditions: Circassia or Caucasian Imamate does not have a truce with Russia |
| Immediate effects: Randomly selects Circassia or Caucasian Imamate as [Adversary] Randomly selects a split state owned by [Adversary] as [State] Randomly selects a primary culture of [Adversary] as [Defector] |
| It is a pity that they did not decide this sooner. [Adversary] gains Tribal Defections Tribal Defections Country modifier −10% Authority −10% Conscriptable battalions for 2.5 years Permit their settlement in our controlled territories. [Adversary] gains Tribal Defections Tribal Defections Country modifier −10% Authority −10% Conscriptable battalions for 2.5 years A random Russian state neighboring [State]: Gains [Defector] Standard of living [Defector] Standard of living State modifier +2 Standard of living for [Defector] pops for 2.5 years 2% of Russian Officers become more radical |

id

### The Milyutin Memorandum

The newly-promoted Lieutenant General Dmitri Milyutin has issued a memorandum to the Tsar, speaking in favor of expelling or exterminating the entire Circassian population of the Caucasus.
---

Flavor text:
"The fulfillment of this thought would have a triple or fourth goal: firstly, to rid the Caucasian plateau of the always hostile population and thereby open beautiful and fertile places for our Cossack population; secondly, to give the natives themselves a better position, to ensure their future, which they now do not have, because, as they arrived in Turkey, they were left to fend for themselves..."
---

| Is triggered by: Monthly pulse |
|---|
| Trigger conditions: Is Russia Circassia exists and does not have a truce with Russia Circassian culture is discriminated Open Prejudice, Cultural Erasure, and Violent Hostility or has State Religion Owns any part of Kuban This event has not triggered before |
| Immediate effects: Dmitri Milyutin becomes a general and leader of the Armed Forces |
| Endorse the memorandum, and escalate the expulsions. Kuban: Gains The Milyutin Memorandum The Milyutin Memorandum State modifier −15 Standard of living for Circassian pops +10% Kill rate +25% Devastation from battles +10% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility pops +25% Emigration push +10% Mortality for 10 years 20% of Circassian pops become more radical Dmitri Milyutin gains War Criminal This measure will make the mountains forever ungovernable. Armed Forces gain Refused Milyutin Memorandum Refused Milyutin Memorandum Interest Group modifier −5 Approval for 5 years 20% of Russian Officers become more radical Dmitri Milyutin gains Experienced Colonial Administrator |

id

### Defections to the Caucasian Imamate

The multi-national nature of [Shamil Murid]'s imamate has proven irresistable to many of our subjects in [State]. Officers and landowners alike have reported numerous defections to the Imamate.
---

Flavor text:
The mistreatment of our military deserters by the Chechens kept many unreliable soldiers, and especially the Poles, from running away; but if now they find out that Shamil gives freedom to deserters, then I'm afraid that the runs will increase. I would think to keep the soldiers from escaping the first captured deserters to be shot. I, together with this, ordered all private commanders to aggravate supervision of unreliable soldiers and report to me immediately about those who make an escape.
---

| Is triggered by: Monthly pulse of journal entry The Caucasian War |
|---|
| Trigger conditions: Caucasian Imamate exists |
| Immediate effects: Randomly selects North Caucasus or Dagestan as [State] |
| Tighten security in the region, to avert further defections. Caucasian Imamate gains Receiving Russian Deserters Receiving Russian Deserters Country modifier −10% Servicemen mortality +35% Conscriptable battalions +25% Training rate for 2.5 years [State]: Gains Rampant Desertion Rampant Desertion State modifier −35% Conscriptable battalions −10% Morale recovery and North Caucasian Standard of living North Caucasian Standard of living State modifier −2 Standard of living for North Caucasian pops for 2.5 years 5% of Servicemen become more radical We will not build further bad will amongst the people. Caucasian Imamate gains Receiving Russian Deserters Receiving Russian Deserters Country modifier −10% Servicemen mortality +35% Conscriptable battalions +25% Training rate for 2.5 years [State] gains Rampant Desertion Rampant Desertion State modifier −35% Conscriptable battalions −10% Morale recovery for 2.5 years Armed Forces gain Caucasian Desertions Caucasian Desertions Interest Group modifier −2 Approval −10% Pop attraction for 2.5 years |

## Expulsion of Circassians

id

### Expulsion of Circassians

|  | Available only with the [Sphere of Influence](Sphere of Influence.md) DLC enabled. |
|---|---|

---

The government's ambition to settle the former territory of Circassia with loyal Cossacks has led to a ruthless campaign to evict the region's Circassian population by any means necessary.
Whilst this journal entry is active, Circassian pops will be deported from our borders, at the cost of enormous loss of life.
---

| Visibility conditions: Accepted the Milyutin Memorandum |  |
|---|---|
| Activation conditions: Circassia does not exist Fully owns Kuban Circassian is discriminated Open Prejudice, Cultural Erasure, and Violent Hostility Alternatively, added by event The Fall of Circassia | Effects when activated: A country that has an incorporated state in Eastern Thrace, Kastamonu, or Trabzon receives event Russia Requests Migration Treaty |
| Entry buttons: Halt Expulsions The continued deportation of the Circassians is no longer in the interest of the government. We will order the deportations cease immediately. Enabled if: An interest group that opposes National Supremacy is in government An interest group that opposes State Religion is in government Has not already halted expulsions Effects: Closes journal entry The Armed Forces and each interest group that has a Jingoist or endorses National Supremacy gains Halted Circassian Expulsion Efforts Halted Circassian Expulsion Efforts Interest group modifier −5 Approval for 5 years |  |
| *The continued deportation of the Circassians is no longer in the interest of the government. We will order the deportations cease immediately.* |  |
| **Enabled if:** An interest group that opposes National Supremacy is in government An interest group that opposes State Religion is in government Has not already halted expulsions |  |
| **Effects:** Closes journal entry The Armed Forces and each interest group that has a Jingoist or endorses National Supremacy gains Halted Circassian Expulsion Efforts Halted Circassian Expulsion Efforts Interest group modifier −5 Approval for 5 years |  |
| Completion conditions: All owned states in the Caucasus strategic region: Have 5% or less Circassian population | Effects when completed: None |
| Failure conditions: Either: Halted expulsions Circassian is accepted Full Acceptance and Second-class Citizen | Effects when failed: None |
| Every three months: Event Across the Sea |  |
| Each month: 10% chance for another country that owns any of Eastern Thrace, Kastamonu, or Trabzon to receive event An Ocean of Blood |  |

id

### Across the Sea

Waves of chartered refugee vessels and merchant craft holding thousands of Circassian deportees have departed across the Black Sea towards their destination. Outbreaks of disease and malnourishment have decimated the crowds.
---

Flavor text:
On the shore, thousands of people crowded together to share in the bare minimum of shelter and food. All of them were pale and hungry. The marks of pox and typhus wracked many of them. Dozens lay dying, on the brink of joining the piles of corpses which had been placed wherever there was space.
Off the coast, the decks of the transport vessels overflowed with the dying and already dead.
---

| Is triggered by: Monthly pulse of journal entry Expulsion of Circassians |
|---|
| Trigger conditions: Journal entry Expulsion of Circassians Any owned state in the Caucasus strategic region has a Circassian pop Has not hidden this event |
| Immediate effects: Selects a random state Caucasusian state as the [expulsion state] Selects one of Eastern Thrace, Kastamonu, or Trabzon as [destination state] |
| Another wave will soon replace them. If the [destination state] owner refused refugees: Kill 6% of Circassian pops in [expulsion state] Otherwise, Kill 4% of Circassian pops in [expulsion state] A Lower, Middle, and Upper strata Circassian pop move to [destination state] Permit the distribution of foreign aid. Kill 1% of Circassian pops in [expulsion state] A Lower or Middle, and a Middle or Upper strata Circassian pop move to [destination state] We have other things to focus on. Hides this event in the future and repeats the following effect each three months: If the [destination state] owner refused refugees: Kill 6% of Circassian pops in [expulsion state] Otherwise, Kill 4% of Circassian pops in [expulsion state] A Lower, Middle, and Upper strata Circassian pop move to [destination state] |

id

### Russia Requests Migration Treaty

Russian officials have approached the government, requesting permission to deport up to fifty thousand Circassian people to our territory. Observers of Russian conduct in the Caucasus warn that the deportations may be much greater in scale.
---

Flavor text:
"The proposed commission provides for the transportation of up to ten thousand families. Transportation at five roubles per head, two to be paid by the migrants themselves, with incentives to private actors." That was the Russian line. The official had his doubts, but he could not speak them. There was a war on to the North - not a formal one, but a war nonetheless. A far greater exodus was a certainty, and its conditions were certain to be much less orderly than was accounted for."
---

| Is triggered by: Activation of journal entry Expulsion of Circassians |
|---|
| Trigger conditions: None |
| They would do well to populate our East. Gain +10 relations with Russia Circassian culture gains the Rumelian tradition trait This treaty threatens to be destabilizing. Refuse refugees Lose −5 relations with Russia Russia receives a negative diplomatic catalyst with this country |

id

### An Ocean of Blood

The flow of Circassian deportees arriving on our Northern shore has spiraled into a humanitarian catastrophe. Local authorities have become overwhelmed by the number of refugees, many of whom are starving and diseased.
---

Flavor text:
Dense masses of ragged men, women, and children covered the seashore. All looked wan and hungry. Many were all but naked. Several lay dying. Off the coast, more vessels approached, transformed into floating graveyards by the disease which had ravaged their human cargo. Occasionally, more bodies washed up ashore, rendered unrecognizable by the attention of crabs and seagulls. Some of the bodies had their hands tied.
---

| Is triggered by: Monthly pulse of journal entry Expulsion of Circassians |
|---|
| Trigger conditions: None |
| Demand that the Russian government cease these atrocities. Lose −30 relations with Russia Russia receives a negative diplomatic catalyst with this country There is nothing we can do. Lose 20% of Circassian pops become more radical |

## Pacification of the Steppes

|  | Available only with the [Sphere of Influence](Sphere of Influence.md) DLC enabled. |
|---|---|

id

### The Ride of Kenesary

A Cossack-escorted caravan moving across the steppes of Akmolinsk has been assaulted by a large and well-trained band of Kazakh rebels, led by the aristocrat Kenesary Kasymuly.
---

Flavor text:
They came in the night, descending upon the camp from all sides, a contingent of horsemen hundreds strong and so sudden in appearance that it was as if they had been birthed from the seas of grass which surrounded the tents. They slaughtered the pickets within moments, blades clashing and gunshots exchanged between standardized muskets produced in the weapon shops of Tula, and a bewildering array of firearms sourced from half of a continent's leftovers.
It only took moments for the cacaphony to fade and the riders to vanish, leaving behind only smoldering cloth, and two dozen scarred survivors.
---

| Is triggered by: 690 days after game start for Russia , if Sphere of Influence is enabled. |
|---|
| Trigger conditions: None |
| Place the border lines on alert. Activate journal entry Pacification of the Steppes |

id

### Pacification of the Steppes

|  | Available only with the [Sphere of Influence](Sphere of Influence.md) DLC enabled. |
|---|---|

---

Despite nominal Russian control over the Kazakh steppe since the 18th century, banditry and disloyalty plagues the territory. Kazakh rebels, led by the aristocrat Kenesary Kasymuly, have begun striking again and again against our supply convoys and fortresses in the region.
Only with the final pacification of the steppe may the Tsar truly be said to be the sovereign of Kazakhstan.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event after game start | Effects when activated: None |
| Completion conditions: All of our Kazakh subjects are Puppets and have no more than 25 liberty desire | Effects when completed: Trigger event The Silent Steppes |
| Failure conditions: One of the following: Any civil war has reached 75% progress Country rank is below Great Power Either Kishi Zhuz , Uly Zhuz , or Orta Zhuz has at least 80 liberty desire | Effects when failed: Triggers event The Kazakh Revolt |
| Invalidation conditions: No Zhuz is a subject of Russia | Effects when invalid: None |
| Times out after 10 years with the following effects: Triggers event The Kazakh Revolt |  |
| Each month, weighted chance of: For other countries: 200: no event 10: random Kazakh subject of our gets the event Loyal Auls Slaughtered 10: random Kyrgyz, Uzbek, Turkmen, or Uyghur country with an interest in Central Asia and non-positive relations with us that has not aligned itself with Kenesary yet gets the event The Khan's Correspondence For Russia : 200: no event 10: Cossack Patrol Attacked 10: Border Fortress Raided 10: Kazakh Raid Repelled |  |

id

### The Kazakh Revolt

Rebellious representatives of the Kazakh Zhuzes have proclaimed the restoration of a unified Kazakhstan, under the Khan Kenesary Kasymuly. The uprising threatens our interests across the entire Central Asian steppe.
---

Flavor text:
Twenty thousand men from three hundred tribes stand astride their horses in the East, prepared to ride against their invaders.
And at their head, the Khan Kenesary, raised upon white felts by his loyalists in three Zhuzes, pledges that he shall never return to his home whilst the Tsar dares call his lands his property.
---

| Is triggered by: Failing or timing out the Pacification of the Steppes journal entry |
|---|
| Trigger conditions: None |
| Immediate effects: If Uly Zhuz exists, it becomes an independent Kazakhstan and ends the truce with Russia Else, the part of Syrdarya owned by Russia becomes Kazakhstan Kazakhstan : Kenesary Kasymuly becomes ruler Activates the Oligarchy and Peasant Levies laws Sets goverment interest groups to Landowners and Devout Gain The Revolt of Kenesary Khan The Revolt of Kenesary Khan (Decaying) Country modifier +90% Defense -90% Morale loss +100% Conscriptable Battalions -75% Provinces lost +50% Home Offense +50% Home Defense for 5 years (decaying) Create an army composed of 5 Irregular Infantry and 5 Hussars in the capital Gain claims on Akmolinsk, Uralsk, Khiva, Aktobe, and Syrdarya |
| Rally the loyal sultans, and crush this revolt! Activate The Last Kazakh Khan journal entry All parts of Syrdarya and Semireche owned by Russia and its subjects become part of Kazakhstan Kazakhstan annexes all Zhuzes with more than 60 liberty desire If the Zhuz is a player, they will switch to playing as Kazakhstan Start a diplomatic play for Kazakhstan : If Orta Zhuz and Kishi Zhuz exist, primary war goal is annex Orta Zhuz and secondary is annex Kishi Zhuz If Orta Zhuz exists, but not Kishi Zhuz , primary war goal is annex Orta Zhuz and secondary is return the state of Uralsk from Russia If Kishi Zhuz exists, but not Orta Zhuz , primary war goal is annex Kishi Zhuz and secondary is return the state of Akmolinsk from Russia Else, primary war goal is return the state of Akmolinsk and secondary is return the state of Uralsk from Russia For Russia , primary war goal is always Make Protectorate Every country that has supported Kenesary: Join Kazakhstan in its diplomatic play Gain 50 relations with Kazakhstan Every Kazakh subject of Russia : 10% of Kazakh pops become more radical Gain Ungovernable Steppes Ungovernable Steppes (Decaying) Country modifier +20% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility statuses -95% Captured provinces +50% Tax waste +10% Mortality +25% Morale loss for 10 years (decaying) (Hidden) Every Kazakh state: Gain Rebelling Armies Rebelling Armies Country modifier +1000 Training rate x2 Training rate for 6 months The Kazakh people will never submit to invaders! Switch to play as Kazakhstan , with same effects as in the previous option. |

id

### The Silent Steppes

With the pacification of the rebel Khanate and the execution of Kenesary Khan, the Russian state may now uncontestedly project power through the entirety of the Kazakh lands.
---

Flavor text:
Stones, weep! Silence, dawn!
Collapse, proud cliffs!
Be still, merry song of the brook!
There is no Kenesary, the messenger of heaven-
He is dead, now.
---

| Is triggered by: Completing the Pacification of the Steppes journal entry |
|---|
| Trigger conditions: None |
| We must drive ever further into Turkestan. Annex all our Kazakh subjects Russia gains claims on all states in Central Asia not owned by Manchu or Han countries Consolidate our gains here, before proceeding. Annex all our Kazakh subjects Every Kazakh homeland gets Pacified Steppes Pacified Steppes State modifier -25% Radicals from conquest −10% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility statuses -5% Mortality from turmoil -50% Pentalties from turmoil for 5 years |

id

### Cossack Patrol Attacked

A detachment of Siberian cossacks in [Raid State] has been ambushed and slaughtered by a band of rebel Kazakh horsemen flying the banner of Kenesary Kasymuly.
---

Flavor text:
"Everywhere, there is disorder. It comes partly from an unforgivable oversight and partly of the cowardice of the Cossacks, who vainly try to inflate the warring forces in words, to justify to some extent their condemnable carelessness."
---

| Is triggered by: Pacification of the Steppes journal entry monthly pulse |
|---|
| Trigger conditions: Any state is owned by a Kazakh subject of ours |
| Immediate effects: One of our Kazakh subject's states is saved as [Raid State] |
| Provide recompense to the Agha-Sultan for the caravan. Gain Relief for Raided Convoys Relief for Raided Convoys Country modifier +1500 Government expenses -20% Bureaucracy for 2.5 years Owner of [Raid State]: Gain Raided Trade Convoys Raided Trade Convoys Country modifier -15% Infrastructure -25% Trade capacity for 5 years Lose 5 Liberty desire It is the responsibility of the Kazakhs to secure their own lands. Owner of [Raid State]: Gain Raided Trade Convoys Raided Trade Convoys Country modifier -30% Infrastructure -50% Trade capacity for 5 years Gain 15 Liberty desire |

id

### Border Fortress Raided

One of our fortresses in the steppes of [Raid State] has been raided by a group of Kazakh rebels under Kenesary Kasymuly. After capturing the fortress and scattering the garrison, the rebels have mercilessly razed the nearest Russian settlements.
---

Flavor text:
As the scout's horse sidled up to what had been the gate, he beheld what was left behind. A layer of ash still covered the ruin, deposited by the fire that had charred and blackened the timbers and earthworks that formed the walls. There had been no rain since the fortress had been burned, leaving the ash to preserve what was left.
Where there had been a fortress, there was now a tomb. Where there had been a garrison, there was now only the enduring stench of smoke.
---

| Is triggered by: Pacification of the Steppes journal entry monthly pulse |
|---|
| Trigger conditions: Any state is owned by a Kazakh subject of ours |
| Immediate effects: One of our Kazakh subject's states is saved as [Raid State] |
| The locals are solely responsible for this disaster. Owner of [Raid State]: Gain 15 Liberty desire [Raid State]: Gain Russian Fortress Raided Russian Fortress Raided State modifier -4 Standard of Living for Russians pops -50% Conscriptable Batalions for 5 years We must dedicate more resources to protecting our interests. Gain Reinforcing Kazakh Fortresses Reinforcing Kazakh Fortresses Country modifier -5% Bureaucracy for 5 years [Raid State]: Gain Russian Fortress Raided Russian Fortress Raided State modifier -2 Standard of Living for Russians pops -25% Conscriptable Batalions for 5 years |

id

### Loyal Auls Slaughtered

The rebel forces of Kenesary Kasymuly have raided a group of loyal auls in [Raid State], spreading terror amongst those Kazakh people who remain loyal to Senior Sultan [Kazakh Ruler Name]'s administration.
---

Flavor text:
"How are we to claim loyalty to you, who pockets the Russians' coin, hiding behind Russian guards, in a town built by Russians? Why should we feel the fear that you so rightfully do?"
---

| Is triggered by: Pacification of the Steppes journal entry monthly pulse |
|---|
| Trigger conditions: Any state is owned by a Kazakh subject of ours |
| Immediate effects: One of our Kazakh subject's states is saved as [Raid State] |
| He brings desolation upon his own people. [Raid State]: Gain Loyal Auls Raided Loyal Auls Raided State modifier -4 Standard of Living -40% Agriculture throughput for 5 years We must request further assistance from the [Russian ruler title]. [Raid State]: Gain Loyal Auls Raided Loyal Auls Raided State modifier -2 Standard of Living -20% Agriculture throughput for 5 years Gain Excessive Reliance on Russia Excessive Reliance on Russia Country modifier -10 Legitimacy -10% Authority for 5 years Lose 5 Liberty desire |

id

### The Khan's Correspondence

The would-be Khan of the Kazakhs, Kenesary Kasymuly, has sent a correspondence to [Ruler Name], requesting an alliance with [Country] against his rivals in Russia and Kazakhstan.
---

Flavor text:
"Time after time, I have requested peacefulness and friendship from the Russian Tsar and his subjects, and yet they have demonstrated no pure intentions. Their desire to dominate our homes grows year by year - for this year it will be Russian fortresses on the river Irtysh, but the next it will be the Sarysu."
---

| Is triggered by: Pacification of the Steppes journal entry monthly pulse |
|---|
| Trigger conditions: Primary culture is Kyrgyz, Uzbek, Turkmen, or Uyghur Has an interest in Central Asia Relations with Russia are poor or worse Has not aligned with Kenesary |
| The Russians and their vassals are a threat to us all. Country aligns itself with Kenesary We will not have a part in his struggle. Increase relations with Russia by 5 |

id

### Kazakh Raid Repelled

A Kazakh insurgent force loyal to Kenesary Kasymuly has attempted to launch a raid on a Russian fortress in [Raid State], before being repelled by the local garrison.
---

Flavor text:
When the riders crested the horizon, the garrison was already in position. In disciplined rows atop the walls, a hail of musket fire met the devastating initial charge, and cossack horsemen joined the lethal dance in its wake.
When the terror was over, men and horses alike were left screaming, the steppe grass watered with the blood of its sons.
---

| Is triggered by: Pacification of the Steppes journal entry monthly pulse |
|---|
| Trigger conditions: Any state is owned by a Kazakh subject of ours |
| Immediate effects: One of our Kazakh subject's states is saved as [Raid State] Random general leading an army stationed in Central Asia is saved as [CAsia General] |
| Commend the soldiers for their brave defense. Armed Forces gain Supporting Kazakh Garrisons Supporting Kazakh Garrisons Interest group modifier +3 Interest group approval for 5 years Owner of [Raid State] gains Successes Against Kenesary Successes Against Kenesary Country modifier +10% Authority +5 Legitimacy for 2.5 years General [CAsia General] deserves the credit for his actions. [CAsia General]: Gains Open Terrain Commander trait if he doesn't have one already Gains Heroic Defensive Actions Heroic Defensive Actions Character modifier +25 Popularity +10% Interest group pop attraction |

id

### The Last Kazakh Khan

|  | Available only with the [Sphere of Influence](Sphere of Influence.md) DLC enabled. |
|---|---|

---

Proclaimed by representatives of the three Zhuzes to be the Khan of a reunified Kazakhstan, Kenesary Kasymuly has openly risen against Russian rule. In order to secure the Kazakh territories once and for all, the rebel Khanate must be destroyed.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: The Kazakh Revolt event after failing Pacification of the Steppes | Effects when activated: None |
| Completion conditions: Kazakhstan does not exist or is a subject of Russia | Effects when completed: Trigger event The Silent Steppes |
| Failure conditions: Kazakhstan has a truce with us and is not our subject | Effects when failed: None |

## The Conquest of Turkestan

|  | Available only with the [Sphere of Influence](Sphere of Influence.md) DLC enabled. |
|---|---|

id

### The Conquest of Turkestan

|  | Available only with the [Sphere of Influence](Sphere of Influence.md) DLC enabled. |
|---|---|

---

To secure our Southern border, counter British power in India, and open routes through which we may extend Russian influence into the Middle East, the [Rutler Title]'s government has issued the prerogative to establish protectorates across Central Asia, and expand our empire into Turkestan proper.
---

| Visibility conditions: Sphere of Influence is enabled. Is Russia Is independent Owns any part of Uralsk and Syrdarya Fully owns the states of Aktobe, Akmolinsk, and Semipalatinsk |  |
|---|---|
| Activation conditions: Has researched Civilizing Mission Owns any part of Uralsk and Syrdarya Fully owns the states of Aktobe, Akmolinsk, and Semipalatinsk | Effects when activated: Trigger the event The Conquest of Turkestan |
| Entry buttons: Pacify the Turkmens To our south, unruly [Turkmenian] tribes defy our authority by raiding our lands, refusing to recognize the authority of any officer, tsar, or khan, and not paying a coin in taxes to anyone — ever while squatting on rightful Russian lands. Let us kill two birds with one stone and force these bandits to heel. Visible if: Any neighbouring state is Merv, Turkmenia, or Uralsk and is owned by a decentralized country Has not used this button before Enabled if: Has researched Colonization Has at least 10 barracks in any state in Central Asia or is AI Effects: Trigger event The Turkmen Scourge |  |
| *To our south, unruly [Turkmenian] tribes defy our authority by raiding our lands, refusing to recognize the authority of any officer, tsar, or khan, and not paying a coin in taxes to anyone — ever while squatting on rightful Russian lands. Let us kill two birds with one stone and force these bandits to heel.* |  |
| **Visible if:** Any neighbouring state is Merv, Turkmenia, or Uralsk and is owned by a decentralized country Has not used this button before |  |
| **Enabled if:** Has researched Colonization Has at least 10 barracks in any state in Central Asia or is AI |  |
| **Effects:** Trigger event The Turkmen Scourge |  |
| Completion conditions: Fully owns the states of Syrdarya, Uzbekia, Kirghizia, Chorasmia, Turkmenia, Tajikistan, Fergana, and Merv | Effects when completed: Trigger event The Great Game |

id

### The Conquest of Turkestan

South of the Kazakh steppe lies the khanates of Central Asia, the next set of barriers arresting Russian power projection into India and the Middle East. By any means necessary, the [Ruler Title]'s government intends to bring them into our fold.
---

Flavor text:
"It is neither ambitious plans and nor selfish calculations that guide Russia in its forward movement into Central Asia, but only the desire to pacify that region, give an impetus to its productive forces, and open the shortest route for the sale of the products of Turkestan to the European part of Russia."
---

| Is triggered by: The Conquest of Turkestan journal entry activation |
|---|
| Trigger conditions: None |
| It is best to take a more honeyed approach. Gain Influencing Central Asia Influencing Central Asia Country modifier 0.05% of GDP as government expenses Every country with its capital in the Central Asia region: Gain 10 relations with Russia Gain Gifts from Russia Gifts from Russia Country modifier +3500 Tax Income for 5 years Countries with this modifier will be more likely to back down in diplomatic plays against Russia Turkestan must submit to the [Ruler Title], by peace or by war. Every country with its capital in the Central Asia region that is not a subject of Russia loses 20 relations with it |

id

### The Great Game

With the opening of Central Asian trade avenues to [India's overlord] India and the Middle East, these routes remain impeded only by the state of [Kabul owner]. Several hawkish figures in the [hawkish_ig] have proposed the state as a potential protectorate.
---

Flavor text:
It is my fear that the acquisition of these vast lands will only spur more terror into the hearts of the [India's overlord], and that yet more wars may be ignited over those nations which cling to their status as buffers between our empires. Peace between us must be reached - but it by treaty, or by their total capitulation.
---

| Is triggered by: The Conquest of Turkestan journal entry completion |
|---|
| Trigger conditions: None |
| Enabled if: Afghanistan exists Kabul, too, will be Russian one day Russia loses 20 relations with every European country that owns or whose subject owns at least 3 of the following 5 states: Punjab, Bombay, Madras, Central India, Bengal Create a 20 infamy diplomatic incident with Afghanistan Russia gains claims on all Pashtun homelands We would better be served by a more subtle approach. Gain Suzerain of Central Asia Suzerain of Central Asia Country modifier +10% Prestige +15% Influence +10% Trade Capacity for 10 years Gain 20 relations with the owner of Kabul |

id

### The Turkmen Scourge

Despite the general recognition of our suzerainty over Turkestan by most peoples in the region, [Turkmenian] tribes to our south continue to raid our lands without fear of reprisals and refuse to submit to our authority. To rectify this injustice, [Ruler Title] [Ruler First Name] has announced the start of a great expedition into Turkmen lands.
---

Flavor text:
Jabbing his finger at the map laid out on the table between them all, the general sneered. "There!" he thundered, "There is where we strike! That nest of
robbery
! and
destruction
!! It has been a hindrance to our ambitions and our grace for far too long." He waved towards the mass of men and guns just beyond the fabric walls of the tent. "Prepare the horses. We move at dawn's light tomorrow."
---

| Is triggered by: Pacify the Turkmens button |
|---|
| Trigger conditions: None |
| Let us show these raiders Russian steel. If the Frontier Colonization law is not active: Activate the Frontier Colonization law Gain Turkmen Pacification Campaigns Turkmen Pacification Campaigns Country modifier +40% Colony Growth Speed for 5 years Else: Gain Turkmen Pacification Campaigns Turkmen Pacification Campaigns Country modifier +80% Colony Growth Speed for 5 years Gain Turanian Logistics Turanian Logistics Country modifier 0.5% of GDP as government expenses for 5 years 5% of Turkmen pops become more radical 2% of Russian pops in Central Asian states become more loyal |

## Historical rulers

Russia has a series of events regarding its historical tsars. Several set historical heirs upon succession of the current tsar. For details on the characters, see [Russia's historical character templates](Russia.md).

id

### The Illness of Nikolai Romanov

The difficulties facing the Russian nation have weighed heavily on Tsar Nikolai Romanov. He has fallen severely ill of pneumonia, and is refusing treatment.
---

Flavor text:
"He will not hear our objections. He has traveled to survey his soldiers, through more and more severe frost. He has fallen ill the first and second times, and yet refuses to rest. He can be found in his study, or on the field."
The doctor's eyes flicked to the side, untrusting of the confidence of the hallway.
"This- this is worse than death - I fear that this is suicide!"
---

| Is triggered by: Yearly pulse |
|---|
| Trigger conditions: Is Russia The ruler is Nikolai (I) Romanov Either: The game date is after 1853.1.1, and has declared bankruptcy within 10 years, is in default, or is at war with a great power The game date is after 1860.1.1 |
| There is no time to waste lying on a sick-bed. Nikolai Romanov dies Cajole him into seeking treatment. Nikolai Romanov gains Sickly |

id

### The Accession of Alexander II

With the end of Nicholas I's reign, Aleksandr Romanov has ascended to the Russian throne as Alexander II, Tsar of all the Russias. His reign is hoped by many liberal bureaucrats to hail a new era of reform.
---

Flavor text:
"In the face of God invisibly co-present with us, we accept the sacred vow to always have the welfare of our Fatherland as one goal.
Yes, guided, patronized by the Providence that called us to this great service, let us establish Russia at the highest level of power and glory, may the constant desires and views of our august predecessors, blessed and unforgettable, be fulfilled through us."
---

| Is triggered by: New ruler character |
|---|
| Trigger conditions: Is Russia Has Monarchy The new ruler is Aleksandr (II) Romanov |
| Long live the Tsar! If the game date is after 1843.9.8, (Tsesarevich) Nikolai Romanov becomes heir Gain The Great Reformer The Great Reformer Country modifier +10% Aristocrats political strength +10% Bureaucrats political strength +10% Bureaucracy for 20 years Market Liberals are more likely to appear during Aleksandr's reign Creates a Modernizer Movement if one does not exist Activates the following journal entries: The Great Reformer Great Reforms: Peasant Reform Great Reforms: Military Reform Great Reforms: Bureaucratic Reform |

id

### A Bout of Weakness

Whilst on holiday, Tsesarevich Nikolai Romanov has been struck by a bout of rapidly worsening health. Doctors fear for the life of the rapidly weakening Tsesarevich.
---

Flavor text:
He had been beset by illness whilst traveling amidst the shore of the Mediterranean, betrayed by the salt winds which had been praised for their medicinal nature. He lay wrapped in blankets, shivering despite the sweat that dripped from his brow and soaked the pillow beneath him.
The nurse standing by the bed could hear his words, squeezed through convulsing lips, but could make no sense of them at all.
---

| Is triggered by: Yearly pulse |
|---|
| Trigger conditions: Is Russia The game date is after 1848.1.1 The heir is (Tsesarevich) Nikolai Romanov |
| Option conditions Always enabled: His last days must be made warm and comfortable. Nikolai Romanov dies and Aleksandr (III) Romanov becomes heir Enabled if: Has researched Modern Nursing Treat him with our most innovative medicine. Nikolai Romanov survives |

id

### The Accession of Nicholas II

The former Tsesarevich Nikolai Romanov has ascended to the Russian throne as Nicholas II. The new Tsar's former tutors have praised his erudite outlook, which promises a liberal and enlightened reign.
---

Flavor text:
"Lord God of our fathers, and King of Kings, who created all things by Thy word, may there be with us the wisdom which belongs to Thy throne; send it from Thy Holy Heaven, that we may know what is well-pleasing in Thy sight, and what is right according to Thy commandment."
---

| Is triggered by: New ruler character |
|---|
| Trigger conditions: Is Russia Has Monarchy The new ruler is (Tsesarevich) Nikolai Romanov |
| For our guardians of truth, God, do save them! Gain The Crown of Perfection The Crown of Perfection Country modifier +15% Academics political strength −10% Enactment time for 20 years |

id

### The Accession of Alexander III

Tsesarevich by virtue of the tragic death of his elder brother, Aleksandr Romanov has ascended to the Russian throne as Alexander III. His reign is expected to mark an age of fierce patriotism and anti-revolutionary conservatism.
---

Flavor text:
"Amidst our great sorrow, the voice of God commands us to stand up cheerfully for the work of the Government in the hope of Divine Providence, with faith in the strength and truth of our power, which we are called to affirm and protect for the good of the people from any enroachments
[sic]
on it."
---

| Is triggered by: New ruler character |
|---|
| Trigger conditions: Is Russia Has Monarchy The new ruler is Aleksandr (III) Romanov |
| To the subduer of the proud, grant everything! If the game date is after 1869.1.1, Nikolai (II) Romanov becomes heir Gain The Peace-Maker The Peace-Maker Country modifier +10% Aristocrats political strength +10% Clergymen political strength +10% Authority for 20 years Traditionalists are more likely to appear during Aleksandr's reign |

id

### The Accession of Nikolai II

Nikolai Romanov has succeeded his father as the Tsar of Russia. The reign of the newly enthroned Nicholas II is anticipated to bring both economic modernization, political centralization, and reinforcement of the power of the monarchy.
---

Flavor text:
"Let everyone know that, devoting all my strength to the good of the people, we will protect the foundation of our rule as firmly and unswervingly as our unforgettable, late parent guarded it. May the merciful Lord God help us in our task, may he strengthen us, and may he bless us for a long and fruitful life."
---

| Is triggered by: New ruler character |
|---|
| Trigger conditions: Is Russia Has Monarchy The new ruler is Nikolai (II) Romanov |
| God save the Tsar, and Orthodox Russia! If the game date is between 1871.1.1 and 1895.1.1, Georgy Romanov becomes heir If the game date is between 1895.1.1 and 1904.8.12, Mikhail Romanov becomes heir If the game date is after 1904.8.12, Alexei Romanov becomes heir Gain The Tsar Out of Time The Tsar Out of Time Country modifier +10% Aristocrats political strength +10% Capitalists political strength +10% Influence for 20 years |

id

### The Birth of Alexei

The wife of Tsar Nikolai Romanov has birthed a son at last. The newborn Alexei Romanov will be raised as the new Tsesarevich of Russia.
---

Flavor text:
"The baby lay on a pillow of cloth of gold, slung to the Princess's shoulders by a broad gold band. He was covered with the heavy cloth-of-gold mantle, lined with ermine, worn by the heir to the crown. He wept loudly, as might any ordinary baby, when old Father Yanishev dipped him in the font."
---

| Is triggered by: Yearly pulse |
|---|
| Trigger conditions: Is Russia This event has not occurred before The game date is after 1904.8.12 The ruler is Nikolai (II) Romanov |
| A Tsar is born. Alexei Romanov becomes heir |

id

### A Terminal Ride

Tsesarevich Georgy Romanov, known for his sickly constitution, has disappeared into the countryside astride his motor-cycle. The household staff fear for his health.
---

Flavor text:
The sound of the engine grew fainter and fainter as the bike summitted one of the rolling hills, and vanished behind it. Into the green abyss disappeared the Tsesarevich, racing to escape the slow, warm trickles of pain in his chest.
---

| Is triggered by: Yearly pulse |
|---|
| Trigger conditions: Is Russia The heir is Georgy Romanov The game date is after 1895.1.1 |
| Option conditions Always enabled: Find him, and return him home. Georgy Romanov dies and Mikhail Romanov becomes heir Enabled if: Has researched Antibiotics Have him rushed to our new hospitals. 50% chance: Georgy Romanov dies and Mikhail Romanov becomes heir 50% chance: Georgy Romanov survives |

id

### The Accession of George I

With the end of Nicholas II's reign, Georgy Romanov has ascended to the throne of Russia. Despite his perpetually ill health, the newly enthroned George I has seen fit to firmly advocate for scientific advancement and modernist reform.
---

Flavor text:
"Lord God, who created all things by Thy word, and by Thy wisdom has made man, that he should walk uprightly and rule righteously over Thy world; Thou hast chosen us as Tsar and judge over Thy people. We acknowledge Thy unsearchable purpose towards us, and bow in thankfulness before Thy Majesty."
---

| Is triggered by: New ruler character |
|---|
| Trigger conditions: Is Russia Has Monarchy The new ruler is Georgy Romanov |
| May he be granted long days. Gain Starry-Eyed Sovereign Starry-Eyed Sovereign Country modifier +10% Engineers political strength +10% Academics political strength +10% Prestige from naval power projection for 20 years |

id

### The Accession of Michael II

The end of Nicholas II's reign has brought Mikhail Romanov to succeed his elder brother as Tsar of Russia. The reserved Michael II's reign is anticipated to herald cautious constitutional reform and responsible governance.
---

Flavor text:
"Inspired, in common with the whole people, by the belief that the welfare of our country be set above everything else, we call upon the Russian people the blessing of God, and accept the sacred vow to protect our Fatherland through the power invested in us."
---

| Is triggered by: New ruler character |
|---|
| Trigger conditions: Is Russia Has Monarchy The new ruler is Mikhail Romanov |
| To the keeper of the weak, grant everything! Gain The Troubled Patriot The Troubled Patriot Country modifier +15% Bureaucrats political strength −10% Radicals from political movements for 20 years |

id

### The Accession of Alexei II

With the end of Nicholas II's reign, his first and only son, Alexei Romanov has ascended to the Russian throne as Alexei II. The young and militant Tsar has declared his intention to expand the long rolls of Russian military glory.
---

Flavor text:
"Lord God of our fathers, may our heart be in Thy hand, to accomplish all that is to the profit of the people committed to our charge and to Thy glory, that so in the day of Thy judgment we may give Thee account of my stewardship without blame."
---

| Is triggered by: New ruler character |
|---|
| Trigger conditions: Is Russia Has Monarchy The new ruler is Alexei Romanov |
| He will drive away the unworthy, and grant us strength! Gain The Warrior-Tsar The Warrior-Tsar Country modifier +15% Officers political strength +5% Authority +5% Prestige from army power projection for 20 years Jingoists are more likely to appear during Alexei's reign |

## The Great Reformer

This journal entry represents the reforms undertaken by Tsar Alexander Romanov

id

### The Great Reformer

The accession of Tsar Alexander Romanov to the Russian throne has been hailed by many reformers as a chance to completely remodel the antiquated structures of the Russian state. The reform-minded Tsar has created a multitude of commissions to study and implement various reform proposals. If these "Great Reforms" can succeed, a reinvigorated Russia may surpass any other European power.
For the duration of Tsar Alexander Romanov's reign, Market Liberal characters will be much more likely to appear in Russia.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event The Accession of Alexander II | Effects when activated: None |
| Completion conditions: Complete all three Great Reform journal entries | Effects when completed: Trigger event The Great Reformer |
| Failure conditions: Aleksandr (II) Romanov is not the ruler | Effects when failed: None |

id

### Great Reforms: Peasant Reform

Discontent with the practice of Serfdom has long existed within reformist circles. Liberal Aristocrats have criticized the practice for tying up vast sums of capital in owning unproductive serfs, limiting the ability of the aristocracy to invest in more productive spheres. So long as this practice continues, it will serve as a burden upon the potential of the state to undergo economic modernization.
In order to match the economic progress of Western Europe, the serfs must be emancipated, and the economy reoriented towards more productive ends.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event The Accession of Alexander II | Effects when activated: None |
| Completion conditions: Has Tenant Farmers or Commercialized Agriculture Does not have Traditionalism | Effects when completed: Advance journal entry The Great Reformer |
| Failure conditions: Aleksandr (II) Romanov is not the ruler | Effects when failed: None |

id

### Great Reforms: Military Reform

The
Imperial Russian Army
, largely made up of poorly-trained Peasant Levies, has fallen further and further behind the more professional military forces of Europe as time has passed. To make up for these defects, the quality of the Army's armaments and training must be improved, and conscription reformed to produce a larger pool of experienced military personnel.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event The Accession of Alexander II | Effects when activated: None |
| Completion conditions: Has researched Rifling Has Mass Conscription 50% or more Battalions are the most advanced infantry type available, at least Skirmish Infantry No barracks has No Organized Training or any shortage Has a level 3 or higher Munition Plants | Effects when completed: Advance journal entry The Great Reformer |
| Failure conditions: Aleksandr (II) Romanov is not the ruler | Effects when failed: None |

id

### Great Reforms: Bureaucratic Reform

Despite the efforts of the previous Tsar to strengthen the state bureaucracy, the Russian state apparatus remains overly reliant upon arbitrary and antiquated local bodies. In order to see through our other reforms with the greatest efficacy, the equal rule of law and authority of the state must be ensured across our vast territories.
The taxation system, currently dependent upon local landowners collecting taxes from peasants, must be brought into the hands of the state. Likewise, local administrators must be made accountable, and the administrative privileges of the nobility reduced.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event The Accession of Alexander II | Effects when activated: None |
| Completion conditions: Has Appointed Bureaucrats Has Per-Capita Taxation, Proportional Taxation, or Graduated Taxation Has a positive Bureaucracy balance Is not about to enter a Bureaucracy deficity | Effects when completed: Advance journal entry The Great Reformer |
| Failure conditions: Aleksandr (II) Romanov is not the ruler | Effects when failed: None |

id

### The Great Reformer

The most crucial of Tsar Alexander Romanov's reforms have been passed. The liberal bureaucrats celebrate them as paving the way for modernity in Russia.
---

Flavor text:
"In the most remote towns, where until now all of the vital interests have consisted of cards, vodka, bribes, and gossip, public libraries, magazines, and newspapers have appeared. Intellectual life has been awakened and revived everywhere."
---

| Is triggered by: Completion of journal entry The Great Reformer |
|---|
| Trigger conditions: None |
| The Tsar must be honored for his work. Aleksandr (II) Romanov gains Tsar-Liberator After reform, revolution. Gain Great Reforms Completed Great Reforms Completed Country modifier +20% Intelligentsia political strength +10% Bureaucracy +25% Radicals from political movements +25% Loyalists from political movements for 5 years |

## References

1. ↑ Bug: Does not actually check that this country owns Amur
2. ↑ Bug: Does not actually check that this country owns Primorye
3. ↑ Bug: Does not actually check that this country owns any of Altai, Ili or Kirghizia
4. ↑ Bug: Does not absolve any owed obligation
5. ↑ Bug: This should be checking the set country, in case it is not China

Primary reference files:

- /Victoria 3/game/common/journal_entries/00_major_railroads.txt
- /Victoria 3/game/common/journal_entries/03_russia.txt
- /Victoria 3/game/common/scripted_buttons/04_russia_buttons.txt
- /Victoria 3/game/events/major_railways.txt
- /Victoria 3/game/events/russia_events.txt
- /Victoria 3/game/events/russo_chinese_events.txt
- /Victoria 3/game/events/00_ep1_kazakh_events.txt
