---
title: Interest group content
source: https://vic3.paradoxwikis.com/Interest_group_content
pageid: 7354
categories: [Potentially_outdated, 1.8, Scripted_content, Articles_with_potentially_outdated_infoboxes, Pages_with_obsolete_template_parameters, Journal, Events]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.8.

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
There are a number of journal entries and events related to [interest groups](Interest group.md).

## Coup content

|  | Available only with the [Voice of the People](Voice of the People.md) DLC enabled. |
|---|---|

Coups have a ~%1.2 chance of triggering each month while the event *To Plot a Coup* is valid. Coups seek to enact a certain law; either Autocracy or the preferred Governance Principles law.

id

### To Plot a Coup

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

[Coup leader] has grown discontent with the [Country] government's institutions. A conspiracy is forming among the [Coup IG] to launch a coup against the government and establish [Coup Law].
---

Flavor text:
"What did you make of [Coup leader]'s little speech back there?"
"It's a drastic proposal. But hard times call for great men to take charge."
"Will the people see it that way?"
"They must be made to see it that way."
---

| Is triggered by: Monthly pulse |
|---|
| Trigger conditions: This event has not occurred within 20 years Does not have active journal entry Coup! A powerful interest group in government has less than 0 approval Any of: Both: The country has neither Autocracy or Oligarchy The relevant interest group endorses Autocracy Both: The country has Council Republic The relevant interest group does not endorse Council Republic [1] Both: The country has either Presidential Republic or Parliamentary Republic The relevant interest group opposes either Presidential Republic or Parliamentary Republic Both: The country has Monarchy The relevant interest group opposes Monarchy |
| Immediate effects: Determines [Coup IG], and [Coup Law] based on the trigger condition as follows: If valid: Autocracy Else for overthrowing a Governance Principles law, the first endorsed law is chosen For Council Republic Presidential Republic Theocracy Monarchy Parliamentary Republic, fallback For Presidential Republic or Parliamentary Republic Theocracy Council Republic, if Socialism is researched Monarchy, fallback For Monarchy Presidential Republic Council Republic, if Socialism is researched Parliamentary Republic, fallback |
| Delightfully devilish Activate journal entry Coup! Progress bar starts at 25 [Coup IG] gains Coup Attempt Supported Coup Attempt Supported (Decaying) Interest group modifier +5% Political strength decaying over 10 years Keep a keen eye on [Coup leader]. Activate journal entry Coup! Progress bar starts at 10 [Coup IG] gains Coup Attempt Resisted Coup Attempt Resisted (Decaying) Interest group modifier −5% Political strength decaying over 10 years |

id

### Coup! (JE)

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

The [Coup IG] are planning a coup against our democratic institutions, aiming to seize control of the government and install a regime more amicable to their interests.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event To Plot a Coup |  |
| Completion conditions: [Coup IG] is powerful and has less than 0 approval The progress bar has reached 100 | Effects when completed: Triggers event Coup! If currently enacting any law and [Coup IG] prefers the current law, Cancel enactment In 30 days, randomly triggers one of: The Legacy of Democracy In Harsh Contrast National Discontent Sedition in Academia |
| Failure conditions: Any of: Progress bar is 0 or less [Coup IG] no longer endorses [Coup Law] [Coup IG] is not in government | Effects when failed: If progress bar is 0 or [Coup IG] no longer endorses [Coup Law], triggers event Coup Attempt Fizzles Out If [Coup IG] was removed from government, triggers event Coup Attempt Foiled If [Coup IG] left government, triggers event [Coup IG] Abandon Government |
| Invalidation conditions: Has enacted [Coup Law] |  |
| Each week: If [Coup IG] is not powerful or has 0 or more approval, reduce progress bar by 1 If [Coup IG] is powerful and has less than 0 approval, increase progress bar by 1 |  |
| Every month, the following random events can happen: (weight: 150) Nothing (weight: 10) General Accused of Plot (weight: 10) A Growing Split (weight: 10) Critical Support (weight: 10) Fear Amongst Investors (weight: 10) The Smoky Backroom (weight: 10) Crowded Streets (weight: 10) A Shot in the Dark (weight: 10) The Enemy's Enemy (weight: 10) The Informant (weight: 10) Up In Arms (weight: 25) For the Defense of [State] (weight: 25) State Figures Invited to Religious Service (weight: 25) Private Armies (weight: 25) The Levers of Power (weight: 25) A Cause Worth Supporting? (weight: 25) The New Prometheus (weight: 25) The Army of Labor (weight: 25) Sickles and Torches |  |

id

### Coup! (Event)

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

The below description is one of several available for this event.
The [Coup IG] have successfully orchestrated a coup against [Country] democracy. [Coup leader] has invoked a state of national emergency, allowing [him] to lead the country as an [Autocracy].
---

Flavor text:
"Quick, get inside! It's almost curfew." The door slammed shut just a little too loudly for his liking.
"You don't want to get caught out by [Coup leader]'s thugs. They see dissenters in a teapot." The sound of heavy marching grew closer, and they fought the urge to peek out of the window.
"They shot the old politicians you know, right up against the palace walls."
"Quiet! They're here. Put out that candle."
Shuffling boots and muffled voices came from behind the door. Thankfully, they did not linger long.
---

| Is triggered by: Completion of journal entry Coup! |
|---|
| Trigger conditions: None |
| Immediate effects: If overthrowing a Monarchy, activate journal entry Stamp Out Monarchism If any country supported the coup, it gains an obligation from this country Activates [Coup Law] [Coup IG] gains Unrivaled in Government Unrivaled in Government (Decaying) Interest group modifier +30% Political strength decaying over 10 years |
| Enabled if: Coup for Autocracy [Country] needs a strong leader. If not a Monarchy, [Coup leader] becomes the ruler If a Monarchy and the ruler does not support [Coup IG], If heir supports [Coup IG], kill ruler and heir becomes ruler, Otherwise, kill both heir and ruler, and create a new ruler supporting [Coup IG] Enabled if: Coup for Monarchy Long live the monarchy! Create a new ruler supporting [Coup IG] Activate Oligarchy If [Coup leader] has Orléanist, Legitimist, or Bonapartist, Set the ruler accordingly and activate journal entries Divided Monarchists and Cement the House of [Dynasty] Enabled if: Coup for Presidential or Parliamentary Republic Long live the Republic! [Coup leader] becomes the ruler If has researched Political Agitation, Activate Single-Party State Otherwise, activate Oligarchy Enabled if: Coup for Theocracy For the glory of [God]! [Coup leader] becomes the ruler Activate Oligarchy Enabled if: Coup for Council Republic Long live the dictatorship of the proletariat! [Coup leader] becomes the ruler If has researched Political Agitation, Activate Single-Party State Otherwise, activate Oligarchy |

id

### Coup Attempt Foiled

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

In one fell swoop, [Coup leader] has been decisively removed from power before [he] could execute [his] coup and institute [Coup Law]. Though democracy lives on for now, the [SCOPE.gsInterestGroup('coup_ig').GetName] have not taken kindly to their political exile.
---

Flavor text:
"I assume, since we're talking freely to one another, that the plan went off without a hitch?"
"Without a hitch?! Are you barmy? It was dead before it got off the ground. No thanks to you! Where the hell were you?"
"Oh, I simply couldn't make it. Urgent family matter, my aunt has the gout you see. But it sounds at least like things could have gone worse."
---

| Is triggered by: Failure of journal entry Coup! |
|---|
| Trigger conditions: [Coup IG] was removed from government |
| Enabled if: Has Censorship or Outlawed Dissent Has Secret Police, National Guard, Dedicated Police Force or Militarized Police Force Has level 3 or higher Law Enforcement or Home Affairs Have [Coup leader] arrested and executed. [Coup IG]: A new Moderate character becomes the leader Gains Prevented a Coup Prevented a Coup (Decaying) Interest group modifier −6 Approval decaying over 10 years Gains Failed Coup Failed Coup Interest group modifier −10% Political strength for 5 years 5% of supporting pops become more radical Enabled if: Any non-marginalized interest group opposes [Coup Law] Expose the [Coup IG] as traitors to [Country]. Every non-marginalized interest group that opposes [Coup Law]: Gains Prevented a Coup Prevented a Coup (Decaying) Interest group modifier +2 Approval decaying over 10 years [Coup IG]: Gains Prevented a Coup Prevented a Coup (Decaying) Interest group modifier −10 Approval decaying over 10 years 10% of supporting pops become more radical Always enabled: Avoid antagonising the [Coup IG] further. [Coup IG]: Gains Prevented a Coup Prevented a Coup (Decaying) Interest group modifier −4 Approval decaying over 10 years 5% of supporting pops become more radical |

id

### Coup Attempt Fizzles Out

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

The conspiracy against [Country] democracy has lost all momentum among the [Coup IG]. The plan to institute [Coup Law] has been abandoned.
---

Flavor text:
"The trouble with you, [Coup leader], is that just because you have succeeded in inducing a handful of half-wits to disfigure the [Capital City] scene by going about in black shorts, you think you're someone. You hear them shouting "Hail, [Coup leader]!" and you imagine it is the Voice of the People. That is where you make your bloomer. What the Voice of the People is saying is: "Look at that frightful ass [Coup leader] swanking about in footer bags! Did you ever in your puff see such a perfect perisher?"
---

| Is triggered by: Failure of journal entry Coup! |
|---|
| Trigger conditions: Progress bar reached 0 or [Coup IG] no longer endorsed [Coup Law] |
| Enabled if: [Coup IG is not powerful and still endorses [Coup Law] A humiliating blunder for [Coup leader]. [Coup IG] gains Failed Coup Failed Coup Interest group modifier −10% Political strength for 5 years [Coup leader] gains Bungled Coup Attempt Bungled Coup Attempt Character modifier −50 Popularity for 20 years Always enabled: They must bear with it, for the economy. Every non-marginalized interest group except [Coup IG] that opposes [Coup Law]: Gains Prevented a Coup Prevented a Coup (Decaying) Interest group modifier +2 Approval decaying over 10 years [Coup IG] gains Failed Coup Failed Coup Interest group modifier −10% Political strength for 5 years |

id

### [Coup IG] Abandon Government

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

The [Coup IG] have departed the government entirely. The institution of [Coup Law] is likely to be executed on the field of battle, rather than in the halls of government.
---

Flavor text:
"We see, therefore, that War is not merely a political act, but also a real political instrument, a continuation of political commerce, a carrying out of the same by other means. All beyond this which is strictly peculiar to War relates merely to the peculiar nature of the means which it uses."
---

| Is triggered by: Failure of journal entry Coup! |
|---|
| Trigger conditions: [Coup IG] left the government |
| The rats scatter once the light is shone on them. 5% of pops become more radical Every non-marginalized interest group except [Coup IG] that opposes [Coup Law]: Gains United Against Insurrection United Against Insurrection Interest group modifier +2 Approval for 5 years Gain Brewing Insurrection Brewing Insurrection Country modifier −10 Authority +15% State penalties from turmoil for 5 years [Coup leader] gains Bungled Coup Attempt Bungled Coup Attempt Character modifier −50 Popularity for 20 years Let [Coup leader], in defeat or not, forever be known as a turncoat. 2.5% of pops become more radical Every non-marginalized interest group except [Coup IG] that opposes [Coup Law]: Gains United Against Insurrection United Against Insurrection Interest group modifier +2 Approval for 5 years Gain Brewing Insurrection Brewing Insurrection Country modifier −10 Authority +15% State penalties from turmoil for 5 years [Coup leader] gains Insurrectionary Leader Insurrectionary Leader Character modifier −25 Popularity for 20 years |

---

The following events have a chance to trigger each month while the journal entry *Coup!* is active.

id

### General Accused of Plot

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

[General Name], a general associated with the [General IG], has been accused of grave disloyalty. [General Name] claims that this is nothing but a plot by subversive elements to remove a barrier to their rule.
---

Flavor text:
"I assure you, gentlemen, I have no knowledge of any of the actions detailed in these alleged letters of mine. If you must go through my personal effects to exonerate me, I welcome you to."
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within five years Any general: Has at least 0 popularity Is not a politician or the ruler |
| We cannot take chances with the loyalties of our generals. [General IG] gains Persecuted General Persecuted General Interest group modifier −2 Approval for 5 years [General Name] retires If [General IG] is also [Coup IG], the coup loses −15 progress Otherwise, if [General Name] opposes [Coup Law], the coup gains +15 progress This is clearly a false accusation. Gain Uncertain Military Loyalties Uncertain Military Loyalties Country modifier −5% Authority −10% Officers political strength for 5 years If [General IG] is also [Coup IG], the coup gains +15 progress Otherwise, if [General Name] opposes [Coup Law], the coup loses −15 progress |

id

### A Growing Split

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

The [Conflicted IG], despite being closely associated with the [Coup IG] in the [Conflicted party], object to the notion of installing [Coup Law].
---

Flavor text:
"What reason is there to continue our partnership? First you grow distant, and now there is talk of opposing the very foundations of state order itself. I request that you explain these allegations immediately, lest the next motion on the floor be my resignation."
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within five years Any party contains both: [Coup IG] An interest group that opposes [Coup Law] |
| Claiming good intentions can sway even the purest soul. [Conflicted IG] gains Reassured of Good Intentions Reassured of Good Intentions Interest group modifier −1 Approval −15% Political strength for 5 years The coup loses −15 progress Their love is unnecessary. Their compliance is all that matters. [Conflicted IG] gains Conflicted Loyalties Conflicted Loyalties Interest group modifier +1 Approval +15% Political strength for 5 years |

id

### Critical Support

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

A group representing the usual opposition forces of the [Critical IG], has approached the government to propose cooperation against "forces that would subvert the government in [Country]".
---

Flavor text:
"We must, indeed, all hang together or, most assuredly, we shall all hang separately."
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within five years Any interest group in opposition opposes [Coup Law] and has −9 or higher approval |
| Accept their well-wishes... for now. [Critical IG] gains Critical Support Critical Support Interest group modifier +3 Approval +20% Political strength for 2.5 years The coup loses −15 progress We will not embolden their own plot against us. [Critical IG] gains Critical Support Refused Critical Support Refused Interest group modifier −2 Approval for 5 years 2% of upper strata pops in the capital become more loyalist The coup gains +15 progress |

id

### Fear Amongst Investors

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

With concerns about national stability in [Country] spreading, investors affiliated with the [Investor IG] have threatened to withdraw their investments from several factories in [Capital state].
---

Flavor text:
Terror could be seen throughout the streets, spreading through the passersby like a poisonous fog. Their walks were brisk, their eyes furtive, their conversations quiet.
The man in the top hat turned to his colleague, who was still gazing out the window of the restaurant.
"This is no way to run a country, and no country to run a business in."
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within five years The capital state has any heavy or light industry The Industrialists are not [Coup IG] and not marginalized |
| Appease the [Investor IG] by accepting an interest rates increase. Gain Wary Investors Wary Investors Country modifier +15% Interest rate for 5 years The coup loses −10 progress If they were truly concerned, they would stand for [Country]. Two industry buildings in the capital gain Uncertain Investment Uncertain Investment Building modifier −50% Cash reserves −50% Throughput for one year The Industrialists gain Economic Instability Economic Instability Interest group modifier −2 Approval for 5 years The coup gains +10 progress |

id

### The Smoky Backroom

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

Figures representing the [Coup IG] have approached elements of the [Approached IG], looking for support in a hypothetical plot against the government.
---

Flavor text:
"I am well aware that our relations have been tense in the past, but I would hope that the radical threat facing our nation, and the need for decisive action, is enough to bring us together on this momentuous occasion..."
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within five years Any interest group in opposition does not oppose [Coup Law] |
| A partnership could be fruitful for both parties. [Approached IG] gains Partners in Crime Partners in Crime Interest group modifier +25% Political strength for 5 years The coup gains +15 progress The [Approached IG] are uninterested in these plots. The coup loses −10 progress |

id

### Crowded Streets

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

Protests supported by the [Democratic IG] have flooded the streets of [Capital state], condemning the presence of groups within the government that support [Coup Law].
---

Flavor text:
"Stand for your principles, you cowards, before you have nothing to hide behind!"
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within five years Any non-marginalized interest group opposes [Coup Law] |
| They have taken a position at the fore of justice. Gain Widespread Protests Widespread Protests Country modifier −5% Authority −5 Legitimacy for 5 years [Democratic IG] gains Vanguard Against Dictatorship Vanguard Against Dictatorship Interest group modifier +20% Political strength for 5 years The coup loses −15 progress A riotous morass of base humanity. [Democratic IG] gains Vanguard Against Dictatorship Vanguard Against Dictatorship Interest group modifier +20% Political strength for 5 years 5% of lower strata pops in the capital become more radical |

id

### A Shot in the Dark

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

A prominent functionary and supporter of the [Assassination IG] has been shot in broad daylight, on the streets of [Capital state]. The local police seem uninterested in investigating any further.
---

Flavor text:
The officer standing on the corner tried not to flinch as the shot split the air, and the screams of onlookers begun to resonate across the streets. In the end, he reassured himself, the new and hefty weight in his coin purse was more than enough to make up for any of his doubts.
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within five years Any interest group in government does not endorse [Coup Law] |
| Justice must be done. Gain Maze of Intrigue Maze of Intrigue Country modifier −10% Authority −5% Bureaucracy −5 Legitimacy for 2.5 years [Assassination IG] gains Investigating Assassination Investigating Assassination Interest group modifier +2 Approval for 2.5 years The coup loses −15 progress We stand above a chasm, and must not fall in. [Assassination IG] gains Covered Up Assassination Covered Up Assassination Interest group modifier −2 Approval for 2.5 years The coup gains +15 progress |

id

### The Enemy's Enemy

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

The [Coup IG]'s supporters in the diplomatic corps have offered to reach out to the [Coup sponsor] government for support in their bid for power, in return for certain future obligations.
---

Flavor text:
"They say nothing gets done around here without the [Coup sponsor] giving approval. I- like to think that isn't true. But if we want to ensure that things proceed as planned..."
The man in the suit gave a slow nod to the stuttering functionary.
"And what of their proposal?"
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within five years Any major or great power: Has an interest in [Country]'s capital region Has 0 or better relations Is not already sponsoring a coup Has their [Coup IG] in government |
| This arrangement is acceptable for the moment. If the coup succeeds, [Country] will owe [Coup sponsor] an obligation The coup gains +25 progress When has [Coup sponsor] meddling ever gone well? [Coup IG] gains Nationally Interested Nationally Interested Interest group modifier +10% Political strength for 5 years |

id

### The Informant

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

One of [Coup leader]'s assistants has fallen out of the window of a Government Administration in [State] and been severely injured on impact. He has offered the government information in exchange for safety.
---

Flavor text:
There was a yelp, a shriek, and the sound of something heavy hitting the cobbled road. In the hastily-opened window, one could almost see a shape turn and stalk away. Where before there had been only worn-down stones, now lay a figure in a pool of spreading crimson.
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within five years Any incorporated state has a Government Administration building |
| He could be an invaluable asset. [Coup leader] gains Blundered Defenestration Blundered Defenestration Character modifier −15% Popularity for 5 years The coup loses −15 progress He will not live to tell the tale. [Coup IG] gains Silenced Informant Silenced Informant Interest group modifier +15% Political strength for 5 years The coup gains +15 progress |

id

### Up In Arms

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

Barracks in [State] have been reporting a large amount of mysterious losses of firearms as of late.
---

Flavor text:
"The Army wastes enough ammunition to outfit a regiment on the range every day. What is a hundred rounds, compared to that monstrous expenditure? What is a thousand?"
"The difference is, on the range we can be sure it's not flying towards us."
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within five years Any incorporated state has a Barracks building |
| The Armed Forces have their own needs. The Barracks in [State] gains Disappearing Armaments Disappearing Armaments Building modifier −30% Throughput for 2.5 years The coup gains +10 progress This is clearly evidence of some sort of plot. The Armed Forces gain Accused of Corruption Accused of Corruption Interest group modifier −2 Approval for 2.5 years |

id

### For the Defense of [Capital state]

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

The [Coup IG], in light of recent unrest, have requested to carry out a series of unscheduled military exercises in [Capital state].
---

Flavor text:
The column of soldiers wound up and down the road, four shoulders wide and so long that the traveler could not see the end of it. An officer on a horse passed by, extending a baton with clear intent.
"This route has been closed for passage to [Capital state]!"
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within 10 years The Armed Forces are [Coup IG] The Armed Forces have more than 20% clout in any state The coup has 75 or more progress |
| They have no legitimate reason to be doing this. The Armed Forces gain War Against the Institutions War Against the Institutions Interest group modifier −5 Approval −30% Political strength for 10 years Every state with more than 20% clout for the Armed Forces: 5% of Servicemen and 2% of Officers become more radical Gain Forbid Military Exercises Forbid Military Exercises Country modifier −10% Authority +15% Military goods cost for 2.5 years The coup loses −50 progress The security of [Capital state] is paramount, even if this is irregular. The Armed Forces gain Unrivaled in Government Unrivaled in Government Interest group modifier +30% Political strength for 2.5 years Every other interest group in government gains Cowed by Power Play Cowed by Power Play Interest group modifier −2 Approval −10% Political strength for 2.5 years The coup gains +50 progress |

id

### State Figures Invited to Religious Service

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

Numerous prominent state figures have been invited to a special religious service administered by the [Coup IG]. This invitation has come suddenly, and disrupted several figures' schedules.
---

Flavor text:
"Every new and successful example therefore of a perfect separation between ecclesiastical and civil matters, is of importance. And I have no doubt that every new example, will succeed, as every past one has done, in shewing that religion and government will both exist in greater purity, the less they are mixed together."
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within 10 years The Devout are [Coup IG] The Devout have more than 20% clout in any state The coup has 75 or more progress |
| We have our own schedule, and will be adhering to it. The Devout gain War Against the Institutions War Against the Institutions Interest group modifier −5 Approval −30% Political strength for 10 years Every state with more than 20% clout for the Devout: 10% of Clergymen become more radical Gain Heretical Government Heretical Government Country modifier −10% Authority −5 Legitimacy for 2.5 years The coup loses −50 progress There can always be time made for worship. The Devout gain Unrivaled in Government Unrivaled in Government Interest group modifier +30% Political strength for 2.5 years Every other interest group in government gains Cowed by Power Play Cowed by Power Play Interest group modifier −2 Approval −10% Political strength for 2.5 years The coup gains +50 progress |

id

### Private Armies

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

Several members of the [Coup IG] have applied for permits to expand their armed security forces, citing increased crime and a risk of turmoil amongst their workers.
---

Flavor text:
"I pity that man who wants a coat so cheap that the man or woman who produces the cloth shall starve in the process."
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within 10 years The Industrialists are [Coup IG] The Industrialists have more than 20% clout in any state The coup has 75 or more progress |
| The state must possess a monopoly on violence. The Industrialists gain War Against the Institutions War Against the Institutions Interest group modifier −5 Approval −30% Political strength for 10 years Every state with more than 20% clout for the Industrialists: 10% of Capitalists become more radical Gain Industrial Security Reduced Industrial Security Reduced Country modifier −20% Trade route competiveness +10% Laborers political strength +10% Machinists political strength for 2.5 years The coup loses −50 progress Business is the sword and shield of [Country]. The Industrialists gain Unrivaled in Government Unrivaled in Government Interest group modifier +30% Political strength for 2.5 years Every other interest group in government gains Cowed by Power Play Cowed by Power Play Interest group modifier −2 Approval −10% Political strength for 2.5 years The coup gains +50 progress |

id

### The Levers of Power

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

The state bureaucracy, largely controlled by the [Coup IG], has been slowing down significantly as of late. The responsible parties have demanded assurances of the security of their positions.
---

Flavor text:
A sort of feverish energy existed in them, now, those sons of worthy families that filled the floor of the office. A solidarity existed between them that had never existed before, all forces of formerly competing privileges coalescing together in the name of the only thing that united them all.
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within 10 years The Landowners are [Coup IG] The Landowners have more than 20% clout in any state The coup has 75 or more progress Has Hereditary Bureaucrats |
| Unelected people should not be allowed this much influence over the state. The Landowners gain War Against the Institutions War Against the Institutions Interest group modifier −5 Approval −30% Political strength for 10 years Every state with more than 20% clout for the Landowners: 10% of Aristocrats become more radical Gain Jammed Levers of Power Jammed Levers of Power Country modifier +25% Trade route cost −15% Bureaucracy for 2.5 years The coup loses −50 progress They have demonstated [sic] that they are indispensable. The Landowners gain Unrivaled in Government Unrivaled in Government Interest group modifier +30% Political strength for 2.5 years Every other interest group in government gains Cowed by Power Play Cowed by Power Play Interest group modifier −2 Approval −10% Political strength for 2.5 years The coup gains +50 progress |

id

### A Cause Worth Supporting?

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

Numerous police officers have been seen supporting the political ambitions of the [Coup IG] whilst in uniform. Local police chiefs have gone so far as to call for restoration of order in the country by force if necessary.
---

Flavor text:
"Vice may triumph for a time, crime may flaunt its victories in the face of honest toilers, but in the end the law will follow the wrong-doer to a bitter fate, and dishonor and punishment will be the portion of those who sin."
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within 10 years The Petite Bourgeoisie are [Coup IG] The Petite Bourgeoisie have more than 20% clout in any state The coup has 75 or more progress |
| Their job is to uphold the law, not dictate it. The Petite Bourgeoisie gain War Against the Institutions War Against the Institutions Interest group modifier −5 Approval −30% Political strength for 10 years Every state with more than 20% clout for the Petite Bourgeoisie: 5% of Clerks and 2% of Shopkeepers become more radical Gain Faithless Police Services Faithless Police Services Country modifier +25% Decree cost −15% Authority for 2.5 years The coup loses −50 progress Who are we, if we do not even have the trust of our police? The Petite Bourgeoisie gain Unrivaled in Government Unrivaled in Government Interest group modifier +30% Political strength for 2.5 years Every other interest group in government gains Cowed by Power Play Cowed by Power Play Interest group modifier −2 Approval −10% Political strength for 2.5 years The coup gains +50 progress |

id

### The New Prometheus

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

[Coup leader], a prominent member of the [Coup IG], has released a political manifesto prophesizing the collapse of society in the near future, and the need for an enlightened regime to avert it.
---

Flavor text:
"The end of our foundation is the knowledge of causes, and secret motions of things; and the enlarging of the bounds of human empire, to the effecting of all things possible."
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within 10 years The Intelligentsia are [Coup IG] The Intelligentsia have more than 20% clout in any state The coup has 75 or more progress |
| [Coup leader] is no philosopher king, as much as he wishes he were. The Intelligentsia gain War Against the Institutions War Against the Institutions Interest group modifier −5 Approval −30% Political strength for 10 years Every state with more than 20% clout for the Intelligentsia: 10% of Academics become more radical Gain Rejected Enlightened Despotism Rejected Enlightened Despotism Country modifier −10% Technology spread −5% Research speed for 2.5 years The coup loses −50 progress In troubled times, we should be guarded by our most qualified. The Intelligentsia gain Unrivaled in Government Unrivaled in Government Interest group modifier +30% Political strength for 2.5 years Every other interest group in government gains Cowed by Power Play Cowed by Power Play Interest group modifier −2 Approval −10% Political strength for 2.5 years The coup gains +50 progress |

id

### The Army of Labor

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

Representatives of the [Coup IG] have announced their intentions for a general strike, if certain concessions are not made. These concessions involve repressions of their political opponents and numerous other concerning articles.
---

Flavor text:
"One thing, however, is clear — Nature does not produce on the one side owners of money or commodities, and on the other men possessing nothing but their own labor-power."
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within 10 years The Trade Unions are [Coup IG] The Trade Unions have more than 20% clout in any state The coup has 75 or more progress |
| Machines can be rebuilt, but the dead cannot be revived. The Trade Unions gain War Against the Institutions War Against the Institutions Interest group modifier −5 Approval −30% Political strength for 10 years Every state with more than 20% clout for the Trade Unions: 5% of Laborers and 2% of Machinists become more radical Gain Industrial Organisation Shaken Industrial Organisation Shaken Country modifier −5 Construction −15% Resource discovery chance for 2.5 years The coup loses −50 progress Concessions must be made to avert disaster. The Trade Unions gain Unrivaled in Government Unrivaled in Government Interest group modifier +30% Political strength for 2.5 years Every other interest group in government gains Cowed by Power Play Cowed by Power Play Interest group modifier −2 Approval −10% Political strength for 2.5 years The coup gains +50 progress |

id

### Sickles and Torches

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

Discontent amongst the [Coup IG] has grown to the point that there are open calls to carry out a march on [Capital state] to demand political concessions.
---

Flavor text:
"Look at them! The swollen pigs in the capital, issuing their dictates down to us like we're their slaves!"
The withered-looking old man turned his head to the passing carriage, a burning sort of contempt in his eyes.
"They tell us to vote them out if we don't like 'em, but what's the point of choosing between different people who all want us to starve?"
---

| Is triggered by: Monthly pulse of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within 10 years The Rural Folk are [Coup IG] The Rural Folk have more than 20% clout in any state The coup has 75 or more progress |
| Mob rule is not a substitute for proper society. The Rural Folk gain War Against the Institutions War Against the Institutions Interest group modifier −5 Approval −30% Political strength for 10 years Every state with more than 20% clout for the Trade Unions: 5% of Peasants and 2% of Farmers become more radical Gain The Dictatorship of the City The Dictatorship of the City Country modifier −5 Legitimacy −15% Capitalists political strength for 2.5 years The coup loses −50 progress The ones who feed us should be allowed to walk our streets as they wish. The Rural Folk gain Unrivaled in Government Unrivaled in Government Interest group modifier +30% Political strength for 2.5 years Every other interest group in government gains Cowed by Power Play Cowed by Power Play Interest group modifier −2 Approval −10% Political strength for 2.5 years The coup gains +50 progress |

---

One of the following events is randomly selected by the completion of the journal entry *Coup!* The selected event is triggered 30 days later if its trigger conditions are met.

id

### The Legacy of Democracy

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

A violent protest suspected to be arranged by the [Democracy IG] in [State] has broken out, demanding an end to [Coup leader]'s absolute rule, and the restoration of democracy in [Country].
---

Flavor text:
As she saw the square slowly filling with bright-eyed men and women who seemed to hold all of the hope and fury in the world, she could not help but feel a pit in her stomach.
How many of them would be left alive or unimprisoned at week's end?
---

| Is triggered by: Completion of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within five years Any non-marginalized interest group opposes [Coup Law] Owns a state besides the capital |
| Another holdout of a dead government to sweep aside. [Democracy IG] gains Martyrs for Democracy Martyrs for Democracy Interest group modifier −2 Approval +15% Political strength for 5 years [State]: 10% of pops become more radical Gains Epicentre of Vanquished Democracy Epicentre of Vanquished Democracy State modifier +20% State penalties from turmoil for 5 years They will burn themselves out quickly. Gain Legacy of the Democratic Regime Legacy of the Democratic Regime Country modifier −5 Legitimacy from head of state +5% Infamy generation for 5 years 5% of pops in [State] become more radical 5% of pops in the capital become more radical 5% of pops in an owned state neighboring the capital become more radical |

id

### In Harsh Contrast

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

A radical group representing the [Opposition IG], who initially
opposed our coup, have split from their former associates, condemning them as "beholden to a dead, illegitimate system". They have appealed to Coup leader] to let them assist [his] new government.
---

Flavor text:
"We, as loyal citizens who have been supporting your efforts since the beginning, would like to humbly request you accept our petition to allow us to assist this new, more righteous government."
As the messenger spoke those words, he tried to banish all memory of the documents he had seen quietly burned not a day earlier.
---

| Is triggered by: Completion of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within five years Any interest group in opposition does not oppose [Coup Law] |
| The sooner we return to a state of order, the better. [Opposition IG]: Gains Opportunistic Allies Opportunistic Allies Interest group modifier +2 Approval for 5 years The leader becomes Moderate Our government has no place for opportunists. [Opposition IG]: Gains Left Isolated Left Isolated Interest group modifier −2 Approval −25% Political strength for 5 years The leader becomes Reformer |

id

### National Discontent

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

A contingent of [Discontent culture] people in [State] have openly condemned the new, absolutist government of [Country] as a threat to the [Discontent culture] nation.
---

Flavor text:
"Our nation has met many hardships over the years of our subordination to the [Country] state. This new regime shall not extinguish our resolve to secure the rights of all [Discontent culture] people..."
---

| Is triggered by: Completion of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within five years Any owned state: Has a homeland culture with less than 80 base cultural acceptance Has 10% or more pops of that culture Any non-marginalized interest group opposes Multiculturalism |
| Their land is valuable, their opinions are not. [State]: Gains National Discontent National Discontent State modifier +20% State penalties from turmoil for 5 years 10% of [Discontent culture] pops become more radical Send a representative to reassure them. A random non-marginalized interest group that opposes Multiculturalism: Gains Folded to Minority Discontent Folded to Minority Discontent Interest group modifier −2 Approval for 5 years |

id

### Sedition in Academia

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

The faculty of the [State] University have allowed their students to release numerous pamphlets spreading slander and calling for "democratic revolution" against [Coup leader]'s government. The identities of these students has been obscured by the university staff.
---

Flavor text:
"Liberty cannot be preserved without a general knowledge among the people, who have a right... and a desire to know; but besides this, they have a right, and indisputable, unalienable, indefeasible, divine right to that most dreaded and envied kind of knowledge, I mean of the characters and conduct of their rulers."
---

| Is triggered by: Completion of journal entry Coup! |
|---|
| Trigger conditions: This event has not occurred within five years Has a University The Intelligentsia are in opposition and oppose [Coup Law] |
| Shutter the [State] University until the perpetrators come forward. [State]: University gains Classrooms Shuttered Classrooms Shuttered Building modifier +50% Throughput for 2.5 years 5% of Academics become more radical Confiscate the pamphlets wherever they are found. The Intelligentsia gain Emboldened Academia Emboldened Academia Interest group modifier +10% Political strength for 5 years Gain Circulating Sedition Circulating Sedition Country modifier −5% Authority for 5 years |

## Interest group suppression

id

### With Friends Like These...

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

The powerful clout that the [Suppressed IG] hold has become a menacing presence over our government. One of our agents has approached us suggesting a... less conventional solution.
---

Flavor text:
"The door has been opened without anyone noticing it until the wind spreads the documents resting on the wooden desk.
"Excuse me," a soothing voice announces, carefully picking them up, "I hope that my visit doesn't disrupt your important affairs. However, it has been observed that the [Suppressed IG] are in desperate need of a little guidance towards the right path, that will help both them and us."
---

| Is triggered by: Yearly pulse |
|---|
| Trigger conditions: Does not have active journal entry Securing the Power Has not dismissed or completed Securing the Power within 5 years Any powerful interest group in opposition has −5 or less approval Has Secret Police, National Guard, Censorship, or Outlawed Dissent |
| They surely need our guidance. Activate journal entry Securing the Power This is utterly immoral! Dismiss journal entry Securing the Power |

id

### Securing the Power

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

The [Suppressed IG] has become too powerful for their own good, given the opinion they hold of us, and are threatening our peaceful government.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event With Friends Like These... |  |
| Completion conditions: [Suppressed IG] is has 20% or less clout and is not in government | Effects when completed: Triggers the Event The Final Word |
| Failure conditions: [Suppressed IG] is in government | Effects when failed: None |
| Every month, the following random events can happen: (weight: 200) Nothing (weight: 10) Rumor Has It (weight: 10) A Surprise Visit (weight: 10) Self-Sabotage (weight: 10) An Unflattering Article (weight: 10) Friendly Encouragement (weight: 10) A Change in Leadership |  |

id

### The Final Word

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

Our efforts to undermine the [Suppressed IG]'s reputation have been extremely successful. With their influence now weakened it is time for us to attend to more important matters.
---

Flavor text:
"The door does not open this time. Minutes go by and nothing happens. It's almost a let down. There's a man in the hallway on the way out, though. He's wearing a velvet frock coat and you look at him expectantly. Another man goes to him and they leave together. Nothing happens."
---

| Is triggered by: Completion of journal entry Securing the Power |
|---|
| Trigger conditions: None |
| Always enabled: People will know who to respect. Gain Suppression Terror Suppression Terror Country modifier +5% Authority for 5 years Always enabled: We shall never let them forget who achieved this. Gain A Tranquil State A Tranquil State Country modifier +15 Legitimacy for 5 years Enabled if: Has Censorship or Outlawed Dissent A good moment to remind them about our laws. 50% chance to gain Suppression Terror Suppression Terror Country modifier +10% Authority for 5 years |

id

### Rumor Has It

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

Rumors about the sinful life of [Suppressed leader], of the [Suppressed IG], have been fabricated and are ready to be spread among the masses like wildfire.
---

Flavor text:
"That they did what to whom? This cannot be believed! Such scandalous behavior cannot be tolerated in this pious country! And then they followed that by what? I cannot bear to hear this anymore! Please, spare me this suffering! End it already, I beg you! I beg you!"
---

| Is triggered by: Monthly pulse of journal entry Securing the Power |
|---|
| Trigger conditions: Leader of [Suppressed IG] can die of natural causes This event has not occurred within 2.5 years |
| Enabled if: Has Secret Police or [Suppressed IG] is powerful Intelligentsia The best rumor can never be traced. [Suppressed IG] gains Undermined Interest Group Undermined Interest Group Interest group modifier −20% Pop attraction for 5 years Always enabled: This will feed more than one high-society ball. [Suppressed IG] gains Scandal Among the Upper Classes Scandal Among the Upper Classes Interest group modifier −1 Approval −20% Pop attraction for 5 years 50% chance to gain Undermining Plot Discovered Undermining Plot Discovered Country modifier −10 Legitimacy for 5 years Reduced chance with Censorship (~−10%) and Political Agitation (~−5%), increased chance without Dialectics (~+4%) Always enabled: People in the suburbs are avid for some social ammunition. [Suppressed IG] gains Scandal Among the Lower Classes Scandal Among the Lower Classes Interest group modifier −2 Approval −10% Pop attraction for 5 years 50% chance to gain Undermining Plot Discovered Undermining Plot Discovered Country modifier −10 Legitimacy for 5 years Reduced chance with Censorship (~−10%) and Labor Movement (~−5%), increased chance without Dialectics (~+4%) For all options : Trigger event Persuasion in 60 days |

id

### Persuasion

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

With the rumors about [his] way of life reaching all social strata and [his] reputation undermined, we can certainly persuade [Suppressed leader] to step down from [his] position as the leader of [Suppressed IG].
---

Flavor text:
"It was one of those days when the fires of the factories twinkled like little eyes through the windows, one of those days when [Suppressed leader] felt as if the whole city stared at [him], accusing, demanding. But it was not [his] fault! [he] knew it, [he] had done nothing wrong... It was the government, it was obviously the government, spreading lies, they never liked [him], did they? Oh, no, they never did.
"What are you looking at!?"
---

| Is triggered by: Event Rumor Has It |
|---|
| Trigger conditions: None |
| Always enabled: A little blackmailing never killed nobody. [Suppressed IG] gains Blackmailed Interest Group Blackmailed Interest Group Interest group modifier −2 Approval −20% Pop attraction for 5 years [Suppressed leader] retires Trigger event Coup de Grâce in 60 days Enabled if: Has researched Mass Propaganda or Mass Communication Maybe we just need to make the scandal even bigger. [Suppressed IG] gains Growing Scandal Growing Scandal Interest group modifier −20% Pop attraction for 5 years [Suppressed leader] Growing Scandal Growing Scandal Character modifier −20 Popularity for 5 years Always enabled: This has gone too far. If the Armed Forces are not [Suppressed IG], Armed Forces gain Backed Down in Suppression Backed Down in Suppression Interest group modifier −2 Approval for 5 years Otherwise, a random IG other than [Suppressed IG] Gains Backed Down in Suppression Backed Down in Suppression Interest group modifier +1 Approval for 5 years |

id

### Coup de Grâce

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

Even after the tenacious efforts to undermine [Suppressed leader]'s reputation, [he] has proved reluctant to step down. Harder measures need to be taken.
---

Flavor text:
The door is open again, this time there's no wind to alert you, no sound, no disturbance of life can be perceived in this safe room. But there he is again. The same soothing voice approaches you, "Excuse me," you recognize that tone, "I hope that my visit doesn't disturb your important affairs. However, our objective has proved to be somehow resistant to our persuasion, so there's only one option left."
"We cannot kill [him]!"
The agent casts a perplexed look at you, "Kill [him]? Oh, no, I'd never suggest that! I was only thinking that we have so many empty cells..."
---

| Is triggered by: Event Persuasion |
|---|
| Trigger conditions: None |
| Always enabled: May [his] body rot in jail. [Suppressed IG] gains Imprisoned Leader Imprisoned Leader Interest group modifier −3 Approval −30% Pop attraction for 5 years [Suppressed leader] retires If neither Censorship nor Militarized Police Force is enacted, Gain Political Leader Political Leader Country modifier +10% Authority −20 Legitimacy for 5 years Enabled if: [Suppressed leader] did not retire in event Persuasion [2] [He] just needs a little more convincing... [Suppressed IG] gains Growing Scandal Growing Scandal Interest group modifier −20% Pop attraction for 5 years [Suppressed leader] retires Always enabled: This has indeed gone too far! If the Armed Forces are not [Suppressed IG], Armed Forces gain Backed Down in Suppression Backed Down in Suppression Interest group modifier −2 Approval for 5 years Otherwise, a random IG other than [Suppressed IG] Gains Backed Down in Suppression Backed Down in Suppression Interest group modifier +1 Approval for 5 years |

id

### A Surprise Visit

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

We have heard that the [Suppressed IG] have been holding some very interesting meetings in their headquarters, which we happen to know extremely well. We could certainly pay them a visit.
---

Flavor text:
"Me? Oh, I was just passing by when I noticed such a little charming gathering you're having there, no? But it's not very friendly of you to have it restricted to your own group, one could even go as far as to say that that's a bit... sectarian, right?"
"Of course I'd never accuse you of such a thing, but maybe the best thing for everyone involved is that you kindly disperse this extremely illegal and filthy meeting at once."
---

| Is triggered by: Monthly pulse of journal entry Securing the Power |
|---|
| Trigger conditions: Any of: Has Militarized Police Force Has Secret Police Does not have Right of Assembly |
| Enabled if: Has Secret Police Our agents will discreetly deal with this. [Suppressed IG] gains Subtly Suppressed Meeting Subtly Suppressed Meeting Interest group modifier −15% Political strength for 5 years Enabled if: Has Militarized Police Force Break down that door! [Suppressed IG] gains Violent Suppressed Meeting Violent Suppressed Meeting Interest group modifier −25% Political strength −2 Approval for 5 years 5% of pops in the capital become more radical Enabled if: Does not have Right of Assembly Alas, if only they had a right of assembly... [Suppressed IG] gains Violent Suppressed Meeting Violent Suppressed Meeting Interest group modifier −25% Political strength −2 Approval for 5 years Always enabled: We don't need a reason to just disperse it. [Suppressed IG] gains Suppressed Meeting Suppressed Meeting Interest group modifier −15% Political strength −1 Approval for 5 years |

id

### Self-Sabotage

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

Rumors about the weak will of [Suppressed leader], of the [Suppressed IG], are more a fact than a suspicion. There are many ways in which one can take advantage of a weak opponent.
---

Flavor text:
"So there are two metals before you, as you can see, right? And then you can choose, this kindly offered gold or this sharp — but equally beautiful — steel, do you understand what I'm saying?"
---

| Is triggered by: Monthly pulse of journal entry Securing the Power |
|---|
| Trigger conditions: Any of: Has Militarized Police Force Has Secret Police Has Law Enforcement level 4 or higher |
| Toss a coin to your leader. Gain Self-Sabotage Bribe Self-Sabotage Bribe Country modifier 0.015% of GDP Expenses for 5 years [Suppressed IG] gains Self-Sabotage Self-Sabotage Interest group modifier −20% Pop attraction for 5 years [Suppressed leader] Self-Sabotage Self-Sabotage Character modifier −30 Popularity for 5 years There are other... cheaper methods. [Suppressed IG] gains Self-Sabotage Self-Sabotage Interest group modifier −20% Pop attraction for 5 years [Suppressed leader] Self-Sabotage Self-Sabotage Character modifier −30 Popularity for 5 years 5% of pops in the capital become more radical |

id

### An Unflattering Article

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

We have hired unscrupulous journalists to write damning articles about the [Suppressed IG], harming their reputation.
---

Flavor text:
The reporter for the [Country] [newspaper] twiddled his thumbs nervously, "Just one article and you'll pay off all my debts?"
"Just one article but it has to be on the front page and it has to eviscerate the [Suppressed IG]."
---

| Is triggered by: Monthly pulse of journal entry Securing the Power |
|---|
| Trigger conditions: This event has not occurred within 2.5 years |
| Always enabled: The pen is mightier. Gain Paying Journalist. Paying Journalist. Country modifier 0.015% of GDP Expenses for 2.5 years [Suppressed IG] gains Article Damages Reputation. Article Damages Reputation. Interest group modifier −15% Pop attraction for 2.5 years Always enabled: Shouldn't journalism include some ethics? If can research Democracy, gain 2500 progress towards Democracy; Otherwise, if can research Dialectics and has an Arts Academy, Gain 2500 progress towards Dialectics; Otherwise, a random IG other than [Suppressed IG] Gains Backed Down in Suppression Backed Down in Suppression Interest group modifier +1 Approval for 5 years Enabled if: Has Censorship or Outlawed Dissent Why pay when we own the newspaper? [Suppressed IG] gains Article Damages Reputation. Article Damages Reputation. Interest group modifier −15% Pop attraction for 5 years |

id

### Friendly Encouragement

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

By intimidating the members of the [Suppressed IG] we can make actively supporting them a much less appealing prospect.
---

Flavor text:
"Sure we might not dissuade the leaders, the ideological crusaders but the rank and file? They care much more about their wellbeing than some poxy cause."
---

| Is triggered by: Monthly pulse of journal entry Securing the Power |
|---|
| Trigger conditions: This event has not occurred within 2.5 years |
| Always enabled: If he can't walk how will he get to the polling station? Gain Intimidating Interest Group Members Intimidating Interest Group Members Country modifier −10% Authority for 5 years [Suppressed IG] gains Members Being Intimidated Members Being Intimidated Interest group modifier −1 Approval −20% Pop attraction for 5 years Enabled if: Has Secret Police We're well equipped for this sort of thing. [Suppressed IG] gains Members Being Intimidated Members Being Intimidated Interest group modifier −1 Approval −20% Pop attraction for 5 years Always enabled: This doesn't seem particularly moral. If can research Democracy, gain 2500 progress towards Democracy; Otherwise, if has researched Centralization and can research International Relations, Gain 2500 progress towards International Relations; Otherwise, a random IG other than [Suppressed IG] Gains Backed Down in Suppression Backed Down in Suppression Interest group modifier +1 Approval for 5 years |

id

### A Change in Leadership

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.8. |
|---|---|

---

By eliminating [Suppressed leader], the leader of the [Suppressed IG], we could stop their momentum in its tracks.
---

Flavor text:
"If you have one rabid dog, you don't let it spread it's disease. You put it down. The same concept applies here."
---

| Is triggered by: Monthly pulse of journal entry Securing the Power |
|---|
| Trigger conditions: Has Secret Police [Suppressed leader] can die of natural causes |
| We shall attempt it. 5% of pops in the capital become more radical 50% chance that [Suppressed leader] is killed Murder in the streets? Unthinkable. If the Armed Forces are not [Suppressed IG], Armed Forces gain Backed Down in Suppression Backed Down in Suppression Interest group modifier −2 Approval for 5 years Otherwise, a random IG other than [Suppressed IG] Gains Backed Down in Suppression Backed Down in Suppression Interest group modifier +1 Approval for 5 years |

## References

1. ↑ May be a bug, as the event trigger checks "oppose" and immediate effect checks "oppose or neutral"; all others check only "oppose"
2. ↑ Possible bug, this option is never available as the only way to receive this event is by forcing the leader to retire

Primary file references:

- /Victoria 3/game/common/journal_entries/01_coup.txt
- /Victoria 3/game/common/journal_entries/01_ig_suppression.txt
- /Victoria 3/game/events/agitators/coup_events.txt
- /Victoria 3/game/events/ig_suppression_events.txt
