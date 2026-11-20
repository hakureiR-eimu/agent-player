---
title: Revolution events
source: https://vic3.paradoxwikis.com/Revolution_events
pageid: 5674
categories: [1.13, Scripted_content, Events]
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
The following events can be triggered during a [revolution](https://vic3.paradoxwikis.com/Revolution).

## List of events

id

### Membership Lists Discovered

A surprise police raid has uncovered a list of radicals associated with the [Interest Group]. There are several ways this list can be used to the government's advantage.
---

Flavor text:
"They came for us too quickly! We had no time to hide everything!"
"Thanks to that, now we need time to hide every
one
!"
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Revolution Progress is under 34% Does not have No Police enacted Any Interest Group is Insurrectionary |
| Option conditions Always enabled: Hunt down every member on that list. Change progress of Civil War by −10% Always enabled: Pubicly expose the connections between the [IG] and the radicals. [Interest Group] gains Membership Arrested Membership Arrested Interest group modifier −25% Interest Group Political Strength for 2 years Enabled if: Any Insurrectionary Interest Group has an Agitator There's only one name on this list we need: [Agitator] Equal chance of either: [Agitator] gains On the Run On the Run Agitator modifier −10 Popularity for 2 years [Agitator] gains Cleared of Charges Cleared of Charges Agitator modifier +25 Popularity for 2 years |

id

### Anger at the Front

Climbing losses at the front have led to murmurs of mutiny spreading among the soldiery. If action isn't taken soon, the situation may become critical.
---

Flavor text:
"Sir, have you heard the new threatening chant in the barracks? 'Light out! Knife out! Let him have it!' It's getting ugly, sir. I fear the front itself no longer believes in success."
---

| Is triggered by: Generic Pulse Event from Revolution or Secession |
|---|
| Trigger conditions: Any War has War Support below 10 |
| Immediate effects: A random War with War Support below 10 is saved as Anger at Front War |
| Arrest the grumblers and fight on. 33% chance of: War Exhaustion in Anger at Front War increases by 10 33% chance of: Change progress of Civil War by −10% 33% chance of: Gets Collapsing Army Morale Collapsing Army Morale Country modifier +25% War Exhaustion from Casualties +10% Morale Loss for 2 years We cannot afford to detain any soldiers. War Exhaustion in Anger at Front War increases by 10 50% chance of: Change progress of Civil War by 10% 50% chance of: Gets Collapsing Army Morale Collapsing Army Morale Country modifier +25% War Exhaustion from Casualties +10% Morale Loss for 2 years We must stop and let the men rest. 2% of Officers pops become more Radical Gets Recovering Army Morale Recovering Army Morale Country modifier −10% Morale Recovery −10% Offense for 2 years Change progress of Civil War by −10% |

id

### Publishing Committee Prosecutions

A committee of publishers, associated with the [Interest Group], that produce incendiary pamphlets has been brought before the courts.
---

Flavor text:
"This agglomeration of dangerous men must be stopped! We must take from them the means of provoking the mob, and reduce these arrogant fools to their true proportions, to their real role as little more than obscure conspirators and criminals!"
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Revolution Progress is under 34% Any Interest Group is Insurrectionary |
| Option conditions Always enabled: Push for their trial in the courts. Change progress of Civil War by −5% [Interest Group] gains Publicized Court Proceedings Publicized Court Proceedings Interest group modifier +10% Interest Group Pop Attraction for 2 years Enabled if: Does not have Protected Speech enacted Quietly muzzle these publishers. Change progress of Civil War by −10% [Interest Group] gains Muzzled Activists Muzzled Activists Interest group modifier −10% Interest Group Political Strength for 2 years Always enabled: Let them go. They're harmless. Equal chance of one of: Change progress of Civil War by 5% Change progress of Civil War by 10% [Interest Group] gains Poorly-Worded Pamphlets Poorly-Worded Pamphlets Interest group modifier −10% Interest Group Pop Attraction for 2 years |

id

### The Infernal Machine

An attempt on the life of the [Ruler] has killed many, but spared our ruler. A complex device, itself damaged in the attack, is the only trace of the revolutionary left at the site of the attack.
---

Flavor text:
"It's hard to say what happened. I heard a slow explosion, like a ragged platoon fire, and there was smoke and chaos all around. The people to my right and left were cut down where they stood, but I was untouched. I looked off towards the [Ruler], and there was just as suddenly a bloody void surrounding him.
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Revolution Progress is between 34% and 66% Any Character is an Agitator |
| Limit [Ruler]'s public appearances for a while. [Ruler] gains Withdrawn from the Public Withdrawn from the Public Ruler modifier −25 Popularity for 5 years This crime is obviously the fault of [Agitator] One of 3 options will happen: 33% chance of: Change progress of Civil War by −10% 33% chance of: [Agitator] gains On the Run On the Run Agitator modifier −10 Popularity for 2 years 33% chance of: [Agitator] gains Cleared of Charges Cleared of Charges Agitator modifier +25 Popularity for 2 years Change progress of Civil War by 10% |

id

### Ersatz Food

Struggling people in [State] have been desperately trying to get their hands on any food they can. Dire warnings of a 'Turnip Winter' have been spreading throughout the region.
---

Flavor text:
"Last week, all we could get was pig's feed. This week... I'm not actually sure what this stuff is. Is that sawdust?"
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Any Incorporated State has average Standard of Living less than 10 |
| At least food substitutes fill people's stomachs. [State] gains Risky Food Substitutes Risky Food Substitutes State modifier +2.5% Mortality for 5 years Try to increase local food production by any means. Change progress of Civil War by −10% [State] gains Farming Incentives Farming Incentives State modifier −33% Agriculture Tax Income +10% Agriculture Throughput +10% Plantations Throughput for 5 years We cannot do anything for [State] Change progress of Civil War by 10% [State] gains Collapsing Agricultural Sector Collapsing Agricultural Sector State modifier −25% Agriculture Throughput −25% Plantations Throughput for 5 years |

id

### The Sacred Union

With war consuming the nation, we can and must try to bury our differences. A call to defend our nation may do much to calm down the unrest at home, although we will have to offer something to our opponents to get them to fully buy in.
---

Flavor text:
"In our great struggle, the nation calls upon all her sons to step forth and defend their families, and calls for all party leaders to come forward and pledge that we shall strive on together until the day of victory. This sacred union will not falter, will not break, in the face of hardship and hostility!"
---

| Is triggered by: Generic Pulse Event from Revolution or Secession |
|---|
| Trigger conditions: Revolution Progress is lower than 34% [Country] is at war |
| In war, we shall find peace. [Country] gains Sacred Union Sacred Union Country modifier +3 Opposition Interest Group Approval for 2 years Every Interest Group not in government: Gains Castle Peace Castle Peace Interest group modifier +10% Interest Group Political Strength for 2 years There is no reason to embolden our opponents with empty promises. Change progress of Civil War by 10% Every Interest group not in government: Interest group gains Marginalized by War Marginalized by War Interest group modifier −10% Interest Group Political Strength for 2 years |

id

### The Waffling Revolutionary

[General], an associate of the revolutionary [Interest Group], is known to have some doubts about his convictions. It may be possible to use that hesitancy to the government's advantage.
---

Flavor text:
"Friends! I-it's not that I don't want the uprising to happen, I'm concerned about, you know. It's. I, uh. I'm in a good position, just... oh, what do I do? What do I do?"
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Any Interest Group is Insurrectionary Any Character: At least one of these: Character is a General Character is an Admiral Interest Group is Insurrectionary Is not busy |
| Option conditions Always enabled: Press the General to support the government. One of 2 options will happen: 50% chance of: [Interest Group] gains Fence-Sitter Encourages Reconciliation Fence-Sitter Encourages Reconciliation Interest group modifier +3 Interest Group Approval for 2 years Change progress of Civil War by −10% 50% chance of: [Interest Group] gains Fence-Sitter Sides with Revolutionaries Fence-Sitter Sides with Revolutionaries Interest group modifier +10% Interest Group Pop Attraction for 2 years Enabled if: Does not have Secret Police enacted [General] cannot be trusted. Arrest him! One of 2 options will happen: 50% chance of: [General] dies 50% chance of: Change progress of Civil War by 10% [General] gains On the Run On the Run General modifier −10 Popularity for 2 years Enabled if: Has enacted Secret Police Dummy text One of 2 options will happen: 66% chance of: [General] dies 33% chance of: Change progress of Civil War by 10% [General] gains On the Run On the Run General modifier −10 Popularity for 2 years |

id

### Sailors Stay Ashore

Sailors in [State] have refused to embark for any voyages out of port. The scope of the mutiny calls for a delicate approach to the situation.
---

Flavor text:
"It's very simple. We have demands. We don't sail until those demands are met."
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: [Country] is at War Any Incorporated State is Coastal Any Interest Group is Insurrectionary |
| Detain the men and keep the incident contained to [State]. [State] +5% of Officers Pops in [State] become more loyalist +20% of Servicemen Pops in [State] become more radical Force the men onto their ships. +5% of Servicemen Pops in [Country] become more radical Try to talk it out with the sailors. +5% of Officers Pops in [Country] become more radical |

id

### Endangered Gold Reserves

With revolutionary support growing in [Capital State], it's been suggested that the national gold reserves be moved out to [State], where it will be unlikely the rebels can seize the money.
---

Flavor text:
"We do this now, or we lose our last good chance to maintain a stable financial footing should everything come to blows. Yes, I know there's a chance they'll catch us in the act, but that's a chance we have to take."
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Capital State has over 33% turmoil Any Incorporated State has under 33% turmoil |
| Try to smuggle the gold reserves out of the capital. 66% chance of: Gets Secured Gold Reserves Secured Gold Reserves Country modifier −10% Loan interest rate for 5 years 33% chance of: Change progress of Civil War by 10% Gets Revolutionaries Captured Gold Reserves Revolutionaries Captured Gold Reserves Country modifier −25% Gold reserve limit +10% Loan interest rate for 5 years Leave the gold reserves in the capital. 33% chance of: Change progress of Civil War by −5% Gets Untouched Gold Untouched Gold Country modifier +10% Gold reserve limit for 5 years 66% chance of: Change progress of Civil War by 10% Gets Revolutionaries Captured Gold Reserves Revolutionaries Captured Gold Reserves Country modifier −25% Gold reserve limit +10% Loan interest rate for 5 years |

id

### Fleeing the Capital

The number of revolutionaries in [Capital State] have made members of the government nervous, and provoked proposals to temporarily move the organs of the state to somewhere friendlier, like [State].
---

Flavor text:
"Every day I jump at the shadows on my way to the office. I see people staring at me as I go down the street, and I swear I see daggers in their eyes. I can't handle it here anymore! Please, we need to be safe
somewhere
!"
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Revolution progress is higher than 66% Capital State has over 33% turmoil Any Incorporated State has under 33% turmoil |
| Move some government functions to [State]. [Country] gets Moving Government Functions Moving Government Functions Country modifier −10% Bureaucracy for 2 years 5% of Pops in [State] become more loyalist 66% chance of: Gets Secure Government Secure Government Country modifier +5% Authority for 2 years 33% chance of: Change progress of Civil War by 10% Gets Abandoned Capital Abandoned Capital Country modifier −10 Legitimacy for 2 years Show confidence in the cause by staying in [Capital State]. 33% chance of: Change progress of Civil War by -10% 5% of pops in [Capital State] become more loyalist 66% chance of: Gets Revolutionaries at the Gates Revolutionaries at the Gates Country modifier −10% Authority for 2 years |

id

### The Rebel's Doctor

A doctor in [State] has been caught aiding wounded dissidents and revolutionaries. His aid isn't just helping his patients, but it's emboldening the entire rebel movement
---

Flavor text:
The doctor's defense attorney leaned back, nursing a small headache. The medical man had proven impossible to work with-his attempts at defense had just dug a deeper hole for himself. His waffling was painful, and his refusal to trust his counsel or even his kinfolk had ruined his chances of getting a lighter sentence. His persistent denials had served to only make his name mud.
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Revolution Progress is less than 66% Any Incorporated State has Academics |
| Investigate the medical profession in [State] for sympathizers. If does not have No Police enacted Then Change progress of Civil War by −5% Else Change progress of Civil War by +5% +20% of Academics Pops in [State] become more Radical The one doctor was obviously a lone wolf-there's no need to follow up on this. Change progress of Civil War by −5% +2% of Academics Pops in [Country] become more Radical |

id

### A Fort in a Sea of Anger

Mobs have surrounded an arsenal in [State], threatening to seize the arms and munitions stored within. While the guards are staving off attacks for now, if no relief is sent then the arsenal will fall to insurrectionists.
---

Flavor text:
"I couldn't sleep last night. The commander refuses to accept terms, and firing continues from both the arsenal and the emplacements that now surround it. After one loud blast, I sprung out of bed and went onto my knees to pray, pray as I've never prayed before."
---

| Is triggered by: Generic Pulse Event from Revolution or Secession |
|---|
| Trigger conditions: Any State is revolting and has a Barracks |
| A relief column could escalate tensions a little, but it's necessary. +5% of Servicemen Pops in [State] become more Radical One of 2 options will happen: 66% chance of: Change progress of Civil War by −5% 33% chance of: Change progress of Civil War by 10% The mob could be emboldened by a surrender, but we need to take that risk. +5% of Officers Pops in [State] become more Radical One of 2 options will happen: 33% chance of: Change progress of Civil War by −10% 66% chance of: Change progress of Civil War by 5% |

id

### The Mob Approaches

Belligerent crowds have been getting increasingly provocative when confronted by troops in [State]. Hardliners in government are demanding tougher responses, while doves are calling for troops to stand down as the first hopeful step in de-escalation.
---

Flavor text:
"A 'whiff of grapeshot' saved the day once, and it can be done again-I'm telling you, we need to show strength right now!"
"Strength? Hah! Bullets are an admission of weakness. We need to talk, show that we're not afraid. That's how we'll get them."
---

| Is triggered by: Generic Pulse Event from Revolution or Secession |
|---|
| Trigger conditions: None |
| Disperse the crowds by force. One of 2 options will happen: 50% chance of: +5% of Pops in [State] become more Radical 50% chance of: Change progress of Civil War by −10% Order the troops to stand down. One of 2 options will happen: 50% chance of: +2% of Pops in [State] become more Loyalist 50% chance of: Change progress of Civil War by 5% |

id

### The Procession of Provocations

Dissidents in [State] have announced plans for a major march around government offices in the near future. While they profess peaceful intentions and claim everyone will be unarmed, the march itself will obviously serve as a rallying point for those unhappy with the government.
---

| Is triggered by: Generic Pulse Event from Revolution or Secession |
|---|
| Trigger conditions: Any State has more than 25% of Lower Strata Pops as Radicals |
| Always enabled: Stop that march by any means necessary! One of 3 options will happen: 33% chance of: +2% of Pops in [State] become more Radical 33% chance of: +10% of Lower Strata Pops in [State] become more Radical Change progress of Civil War by 5% 33% chance of: Change progress of Civil War by −5% Always enabled: Let the procession go ahead. +5% of Lower Strata Pops in [State] become more Radical One of 2 options will happen: 50% chance of: Change progress of Civil War by −10% 50% chance of: Change progress of Civil War by 10% Enabled if: Any of: Has Militarized Police Force enacted State has the Violent Suppression Cost: 100 Violent Suppression Use the nation's national guard to control the angry mobs Requires: Standing Army Owner does not have the law Guaranteed Liberties Turmoil in state is at least 25% Modifiers: −50% State penalties from turmoil +2% Mortality per turmoil decree Proclaim a curfew and make sure it's strictly enforced. [State] gets Enforced Strict Curfew Enforced Strict Curfew State modifier −25% State Penalties from Turmoil for 2 years One of 2 options will happen: 66% chance of: Change progress of Civil War by −5% 33% chance of: Change progress of Civil War by −10% |

id

### When You Have A Hammer

[General], noting severe unrest in [State], has proposed using the army to suppress agitation in the area. While his political allies support him, there is a heavy risk of following his plan.
---

Flavor text:
"It's simple-we have an army, and there is the enemy. Let me deploy my men and do what is needed, and the enemy shall be vanquished. That's all there is to it!"
---

| Is triggered by: Generic Pulse Event from Revolution or Secession |
|---|
| Trigger conditions: Any character is General |
| Always enabled: Reprimand the [General] and reject the plan. [General] is demoted to [Lower Rank] [General's IG] gains Our General Is Disrespected Our General Is Disrespected Interest group modifier −2 Interest Group Approval for 5 years Always enabled: We must use the tools we have to solve the problems we have. One of 2 options will happen: 33% chance of: Change progress of Civil War by −5% 66% chance of: Change progress of Civil War by 5% Enabled if: Has the trait Honorable Does not have the trait Pillager, Bandit, or Wrathful Perhaps the general can consider a kinder plan? Change progress of Civil War by −5% Enabled if: Does not have the trait Honorable Has the trait Pillager, Bandit, or Wrathful Brute force may be the best option here. One of 2 options will happen: 50% chance of: Change progress of Civil War by −5% 50% chance of: Change progress of Civil War by 10% |

id

### The Streetside Standoff

Troops in [State] have reported more and more confrontations with belligerent mobs. Fighting will likely break out soon even if nothing is ordered. There's only two ways to control the situation: Either pull the troops back, or tell them to engage.
---

Flavor text:
The soldier shuffled nervously where he stood, shifting the weight of his gun back and forth as he stared at the crowd stirring far too close by. He thought he recognized some of those faces-or he would have, if they weren't twisted in utter loathing for him and his uniform. What was he even doing? Was he standing with the right people here?
---

| Is triggered by: Generic Pulse Event from Revolution or Secession |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: Order a withdrawal from [State]. [State] gains Void of Law Void of Law State modifier +25% State Penalties from Turmoil for 2 years One of 2 options will happen: 50% chance of: Change progress of Civil War by 5% 50% chance of: Change progress of Civil War by −5% Enabled if: Has enacted Peasant Levies or Mass Conscription Order our men to advance on the mob. [State] gains Violent Confrontations Violent Confrontations State modifier +2% Mortality per Turmoil for 2 years One of 2 options will happen: 33% chance of: Change progress of Civil War by 10% 66% chance of: Change progress of Civil War by −5% One of 2 options will happen: 50% chance of: Gains Troop Loyalty Shaken Troop Loyalty Shaken Country modifier −15% Morale Loss −50% Morale Recovery for 2 years 50% chance of: Nothing happens Enabled if: Has enacted Professional Army Our men are professionals! They can maintain discipline where they are. [State] gains Violent Confrontations Violent Confrontations State modifier +1% Mortality per Turmoil for 2 years One of 2 options will happen: 33% chance of: Change progress of Civil War by 5% 66% chance of: Change progress of Civil War by −5% Enabled if: Has enacted National Militia The army and the people are one and the same! Let them talk it out. One of 2 options will happen: 33% chance of: +10% of Servicemen become more radical Change progress of Civil War by 5% 66% chance of: +2% of Pops in [State] become more loyalist Change progress of Civil War by −5% |

id

### National Self-Defense

With violent sentiment rising amongst the [Country Adj] [Interest Group], several [Discriminated Culture] communities have begun to form armed militias to keep their populations safe.
---

Flavor text:
"The soul of the ancient [Discriminated Culture] heroes, wandering in the world of chaos, has finally found its place."
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Revolution is between 34% and 66% progress Revolutionary Movement is Reactionary Any insurrectionary Interest Group: At least one of these: Is Neutral , Endorses , or Strongly Endorses National Supremacy Leader has any of: Ethno-Nationalist Fascist Is not Marginalized Any incorporated state: Has discriminated pops not in a homeland |
| The authorities have far more important things to worry about. Change progress of Civil War by −5% [Revolutionary Movement] gains Armed Minorities Armed Minorities Political movement modifier +5% Political Movement Activism for 5 years Every Interest Groups that: At least one of these: Endorses , or Strongly Endorses National Supremacy Leader has any of: Ethno-Nationalist Fascist Interest Groups get Ethnic Self-Defense Tolerated Ethnic Self-Defense Tolerated Interest group modifier −3 Interest Group Approval for 5 years Gains Legitimized Ethnic Self-Defense Legitimized Ethnic Self-Defense Country modifier −10% Authority −5% State Penalties from Turmoil for 5 years The [Discriminated Culture] are out of line, and must be disciplined. Change progress of Civil War by 5% Add −2 Standard of Living Modifier for [Discriminated Culture Pop] to [State] |

id

### Stochastic Terror

Following a recent bombing carried out by radical supporter of the [Interest group] in [State], a copy of the works of [Agitator] has been found in the possession of the responsible parties.
---

Flavor text:
"...and if the tragic hour strikes and we must give ourselves up to it, the consciousness of this will support and strengthen us. We do not merely say "no" but from the depth of our hearts we declare ourselves ready to sacrifice everything."
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Any Incorporated State has 25% or more turmoil Any Agitator: [Political Movement] is Revolutionary [Interest Group] is insurrectionary Revolution progress is lower than 34% |
| The [Interest Group] represent a menace to civil society. Change progress of Civil War by −10% [Political Movement] gains Negative Associations Negative Associations Political movement modifier +5% Political Movement Activism for 5 years [Interest Group] gains Accused of Terrorism Accused of Terrorism Interest group modifier −2 Interest Group Approval for 5 years Publicize this incident as [Agitator] calling for terrorism against innocents. Change progress of civil war by −5% [Political Movement] gains Terrorism Accusations Terrorism Accusations Political movement modifier −50% Political Movement Pop Attraction for 5 years [Agitator] gains Terroristic Reputation Terroristic Reputation Agitator modifier −25 Popularity for 5 years [State] gains 3% devastation |

id

### The Common Soldiery

The
Servicemen of the [State]
Barracks have begun organizing into a council in order to advocate for higher wages and better treatment. The
Armed Forces views this as an active threat to their legitimacy.
---

Flavor text:
Slipping the handwritten pamphlet out of the pocket of his uniform coat, he handed it to his comrade.
"The Sergeant and I have talked about the pay we're getting-and I know you feel the same way. How are we supposed to do our jobs if the generals are feeding all the money we're owed to their nice white horses?"
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Armed Forces are not marginalized Military Wages are lower than Medium Any Incorporated state has a Barracks Revolution progress is lower than 34% |
| Discipline them all, and bring in replacements from other regions. Change progress of civil war by −5% +5% of Servicemen pops in [State] become more radical Barracks gains Soldier Council Replaced Soldier Council Replaced Building modifier −25% Barracks building Throughput for 2 years Our Servicemen should be able to stand for their own interests. Change progress of civil war by 5% |

id

### The People's Wealth

A group of revolutionaries have carried out a robbery of a [Country] state bank in [State]. A significant amount of money had been stolen, and redirected into the revolutionaries' coffers.
---

Flavor text:
A shot rang out, and the marble ceiling was marred with a new crack. The screams of the bank officials accompanied dust and splinters hitting the floor.
"In the name of the revolutionary executive committee, I declare everyone under arrest! Hands up! Otherwise, everyone will be killed!"
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: At least one of these: Revolution Movement is Socialist Revolution Movement is Liberal At least one of these: Revolution Progress is under 34% Revolution Progress is between 34% and 66% |
| Option conditions Always enabled: Order increased security around banks across [Country] Gains Bank Robbery Compensation Bank Robbery Compensation Country modifier +1 Government Expenses for 2 years Always enabled: Rely upon the locals to report those suspected of the robbery. Change progress of Civil War by 5% Gains Bank Robbery Compensation Bank Robbery Compensation Country modifier +1 Government Expenses for 1 year Enabled if: Investment Level for Home Affairs greater than 2 Has enacted Secret Police Dispatch the Secret Police to apprehend these criminals. Change progress of Civil War by −5% |

id

### Covert Agitation

Revolutionary sympathizers have begun to agitate for anti-government causes in the
Barracks in [State].
---

Flavor text:
"The state has forsaken every right it has to order your blood shed, you must realize this. Even beyond [State], people like you and I are organizing to demand an end to this nightmare."
"And it starts with you and I! Us common soldiers, the ones they trust to do their will... what will happen, when they finally see that no one will stand behind them?"
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Armed Forces: Is not Insurrectionary Is not Marginalized Revolution Progress is under 34% Any [Country] Building is Barracks |
| The Armed Forces must be loyal to the state above all else. Change progress of Civil War by −5% Armed Forces gains Opposed Agitation Opposed Agitation Interest group modifier +2 Interest Group Approval for 2 years Those who control the soldiers control the nation. Change progress of Civil War by 5% +5% of Servicemen Pops in [State] become more Radical Barracks gains Hotbed of Agitation Hotbed of Agitation Building modifier −10% Throughput for 2 years |

id

### Assassination Attempt on the [Ruler Title]

At an event to commemorate the opening of an ornamental garden in [Capital City], a revolutionary detonated an explosive device near [Ruler]. The [Ruler Title] survived, but the assassin died of his wounds before testifying.
---

Flavor text:
As soon as the bomb detonated and the explosion split the air, the crowd was already on the would-be assassin, heedless of their own wounds, bearing him down, beating him with their bags and fists.
"People of [Country]! Id did it for you!", shouted the assassin, but it was to no avail.
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Revolution is Liberal Revolution is Socialist Any insurrectionary, non-marginalized Interest group: Stance on Monarchy is less than Neutral [Country] has enacted Monarchy Revolution Progress is above 66% |
| Option conditions Always enabled: Vengeance upon all traitors and murderers! Change progress of Civil War by 10% [Country] gains Aftermath of Assassination Attempt Aftermath of Assassination Attempt Country modifier −10% Authority −5 Legitimacy (Decaying) for 5 years Enabled if: Investment Level for Home Affairs greater 3 or more Dummy Text Change progress of Civil War by −15% Random insurrectionary, non-marginalized Interest group that: Stance on Monarchy is less than Neutral [Leader] dies [Interest group] gains Surgical Reprisals Surgical Reprisals Interest group modifier −25% Interest Group Political Strength for 5 years For both options [Ruler] gains trait Scarred |

id

### Sedition Amongst the Devout

Prominent members of the Devout have been found to be using their privileged position in society to encourage radically anti-government activities.
---

Flavor text:
"[Country] is split between two irreconcilable camps", said the priest. "One of them pursues a policy of anti-[Country Adj] and anti-religious terror! The other side pursues a policy of respect for God, and seeks to restore national order.
With this in mind... who else could any good-hearted person stand behind?"
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Any insurrectionary, non-marginalized Interest group: Stance on State Religion is greater than Neutral Does not have State Religion enacted Revolution progress is between 34% and 66% |
| They are not sacrosanct, as long as they continue to meddle in politics. Devout gains Anti-Clerical Regime Anti-Clerical Regime Interest group modifier −5 Interest Group Approval −15% Interest Group Political Strength for 5 years +5% of Clergymen pops in [Country] become more radical Change progress of civil war by −5% We cannot become known as executioners of priests. Change progress of civil war by 10% Devout gains Clerical Political Activities Clerical Political Activities Interest group modifier +15% Interest Group Political Strength for 5 years |

id

### Crime and Divinity

The reactionary leanings of many Clergymen affiliated with the Devout have given rise to demands to curb the political influence of [Country Adjective] religious organizations.
---

Flavor text:
"I have made my opinions on this clear. All of the monasteries in [Capital] are not worth the life of a single [Culture] citizen."
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Any insurrectionary, non-marginalized Interest Group: Stance on State Religion is either Endorse or Strongly Endorse Revolution Progress is less than 66% |
| They are holy men and women, and they can say what they will. Change progress of Civil War by +10% [Political Movement] gains Clerical Support Clerical Support Political movement modifier +10% Political Movement Pop Attraction for 5 years Bolt their temples shut, and arrest clergy who resist. Change progress of Civil War by −5% +5% of Devout members of Pops in [Country] become more Radical Enabled if: Devout is not insurrectionary Civil War progress is between 34% and 66% A righteous nation is best found through the revolutionary path. Devout becomes insurrectionary |

id

### Martial Laws

Mass mutinies in [State] within the Armed Forces under [Politician]'s watch have led to officers marching for a new government.
---

Flavor text:
What began as a few disgruntled supply officers and colonels'-in-laws swept through the ranks. Whether strong-armed by their leaders or willing accomplices, entire brigades have joined the mutiny. Their oaths lie trampled in the mud with any who stand in their way.
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Revolution Progress is above 66% Armed Forces is insurrectionary Does not have Mass Conscription enacted Is not at war Any Incorporated State has a Barracks |
| Arrest the traitors. Change progress of Civil War by 5% +5% of Officers Pops in [State] become more Radical Gains Arrested Mutineers Arrested Mutineers Country modifier −15% Morale Loss for 2 years Send them home. Remind them of their duty. Change progress of Civil War by −5% Armed Forces gains Mutineers Sent Home Mutineers Sent Home Interest group modifier +3 Government Interest Group Approval −10% Interest Group Pop Attraction for 2 years Shoot every tenth man. Change progress of Civil War by 10% [State] 20% of Servicemen Pops lose their lives +10% of Servicemen become more Radical |

id

### Troubles of the Commons

Every tenancy of the Landowners in [State] has rental prices beyond reasonable limits. Their tenants direct their ire at the government for not protecting them.
---

Flavor text:
Humans have two reactions in times of strife: seek culpability for their woes, and address it accordingly. A sign of strength, or fatal stupidity - philosophers could debate until the end of days. They do agree it is not a sign of intelligence. The blame can be shifted, and those culpable profit most of all.
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Revolution Progress is above 66% Landowners is insurrectionary Does not have Council Republic enabled Is at peace Any State is Incorporated |
| Seize the ringleaders! Change progress of Civil War by 10% +5% of Aristocrats Pops in [State] become more Radical Landowners gains Detained Landlords Detained Landlords Interest group modifier −10% Interest Group Political Strength for 5 years They ought to be charged with extortion. Change progress of Civil War by 5% Gains Charged Landlords with Extortion Charged Landlords with Extortion Country modifier −10% Plantations Throughput +2 Rural Folk Approval for 5 years Rent needs a stern limit. Change progress of Civil War by −5% [State] +2% of Aristocrats Pops become more Radical [State] gains Light Rent Controls Light Rent Controls State modifier +1 Standard of Living for the Lower Strata for 5 years |

id

### Buried in Red Tape

Falsified reports from every private and public arm in [State] have set the government against itself. [Petite Bourgeoisie Leader] has a simple demand: hand over government to the people who know how to get things done.
---

Flavor text:
Not all resistance is based on applying a cudgel to a skull, or a torch to a machine. An effective means is to simply not honor the gentleman's agreement that is legal bookkeeping. A few fudged numbers here, some out-of-order submissions there; all innocent mistakes in the eyes of a supervisor. When taken together, it may be read as a brainless error or measured destruction.
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Revolutionary Progress is above 66% Petite Bourgeoisie is Insurrectionary [Country] is not at War Any Incorporated state has a Government Administration |
| We must replace these reports. Change progress of civil war by 10% [Country] gains Replacing False Reports Replacing False Reports Country modifier +3 Industrialists Approval +3 Intelligentsia Approval +10% Radicals from Political Movements for 2 years They ought to be charged with fraud! Change progress of civil war by −5% [Petite Bourgeoisie Leader] gains trait Arrogant [Country] gains Fraudulent Reports Fraudulent Reports Country modifier −5% Bureaucracy for 2 years Restart from these falsified numbers. Change progress of civil war by −10% [Country] gains Restarting Bureaucratic Reports Restarting Bureaucratic Reports Country modifier −10% Manufacturing Industries Throughput −10% Urban Center Tax Income for 2 years |

id

### Rot Of the Vine

With a rich harvest in [State], [Politician] has a delivery report - zero everything - with a stern ultimatum: a new order that serves the Rural Folk, or mass starvation.
---

Flavor text:
"We're bloody starving. The rats are starving too. Can't even go out and hunt rabbits."
"Look at all that fruit... it's just sitting there, winking at us. Waiting to be picked."
"Why won't the government do something? Rather take my chances with them than Old Man Jenkins' shotgun."
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Revolutionary Progress is above 66% Rural Folk is Insurrectionary Does not have Collectivized Agriculture enacted [Country] is not at war with any other Country Any neighboring State is not owned by [Country] Any owned State is incorporated |
| Seize every farm complicit in this. Change progress of civil war by 10% [State] gains Local Farm Shutdowns Local Farm Shutdowns State modifier −30% Agriculture Throughput −30% Plantations Throughput −30% Ranches Throughput for 2 years Armed Forces gains Farm Seizures Farm Seizures Interest group modifier +2 Interest Group Approval for 2 years Send for supplies from [Country]. Change progress of civil war by −5% [State] gains Local Farm Shutdowns Local Farm Shutdowns State modifier −30% Agriculture Throughput −30% Plantations Throughput −30% Ranches Throughput for 2 years [Country] gains Foreign Food Aid Foreign Food Aid Country modifier +2 Industrialists Approval +10% Trade Capacity for 2 years Sell seeds and guides for at-home cultivation. Change progress of civil war by 5% [State] gains Local Farm Shutdowns Local Farm Shutdowns State modifier −15% Agriculture Throughput −15% Plantations Throughput −15% Ranches Throughput +10% Subsistence Output +15% Radicals from Political Movements for 2 years |

id

### Under No Pretext

After raiding army barracks in [State], the Trade Unions under [Politician] have begun turning their weapons against the government of [Country].
---

Flavor text:
"See, that's just the thing with this nationalist saber-rattling. Most believe their guns only come from this particular law. But what the book's saying is that the Unions aren't going for your guns. In fact, it says to get more."
"You know you can't read!"
"It's Engels, you get credit for trying."
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Revolution Progress is greater than 66% Trade Unions are Insurrectionary [Country] has not enacted No Police [Country] is not at war with another Country Any Incorporated State has a Barracks |
| Option conditions Always enabled: Concentrate on defending the cities. Change progress of civil war by 10% Barracks gains Barracks Damaged Barracks Damaged Building modifier −60% Defense −60% Offense for 5 years One of 3 options will happen: 33% chance of: Armed Forces Leader gains trait Cautious 33% chance of: Armed Forces Leader gains trait Wrathful 33% chance of: Armed Forces Leader gains trait Wounded Enabled if: 1 or more empty Agitator slots Chase them into the hills. Change progress of civil war by −10% +2% of Laborers pops in [Country] become more radical A Trade Unions Agitator will appear in [Country] with character traits Social Bandit and Popular Commander 2% of Servicemen pops in [State] lose their lives Always enabled: The constabulary must be better armed! Change progress of civil war by 5% [Country] gains Militarized Police Force Militarized Police Force Country modifier +3 Armed Forces Approval +10% Mortality per Turmoil +20% Fascist Movement Pop Attraction −35% State Penalties from Turmoil for 5 years +5% of Lower Strata pops in [State] become more radical |

id

### Vultures Upon a Carcass

Opportunistic members of [Interest Group] have defected to the [Insurrectionary Interest Group]'s cause.
---

Flavor text:
Carrion crows pluck from fresh deaths, no matter the cause. Some, however, sense when a still-living beast is about to die. The creature will wait, however long it takes, for said meal to die. But better to be the first there with the choicest pick of meat, than hoping for scraps.
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Any non-insurrectionary, non-marginalized Interest Group is in opposition Any Interest Group is Insurrectionary |
| So be it. [Insurrectionary Interest Group] gains Defectors Supporting Defectors Supporting Interest group modifier +20% Interest Group Pop Attraction for 2 years [Interest Group] gains Defected to Revolutionaries Defected to Revolutionaries Interest group modifier −20% Interest Group Pop Attraction for 2 years Try to coax some back. [Insurrectionary Interest Group] gains Defectors Supporting Defectors Supporting Interest group modifier +10% Interest Group Pop Attraction for 2 years [Interest Group] gains Defected to Revolutionaries Defected to Revolutionaries Interest group modifier −10% Interest Group Pop Attraction for 2 years Gains Support Salvaged Support Salvaged Country modifier −5% Bureaucracy for 2 years |

id

### Heavy Handedness

[Ruler] mistook an enemy in the [Interest Group]. After accusing them with false charges, moderates in [interest Group] defected to the [Interest Group]'s cause.
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Any non-insurrectionary, non-marginalized Interest Group is in opposition Any Interest Group is Insurrectionary |
| Their bedfellows may not be so accommodating. Change progress of Civil War by 5% One of 2 options will happen: 50% chance of: [Neutral Interest Group] gains Positive Partnership Positive Partnership Interest group modifier +5% Interest Group Political Strength +10% Interest Group Pop Attraction for 2 years [Insurrectionary Interest Group] gains Positive Partnership Positive Partnership Interest group modifier +5% Interest Group Political Strength +10% Interest Group Pop Attraction for 2 years 50% chance of: [Neutral IG Leader] gains Defection Backfired Defection Backfired Leader modifier −50 Popularity −15% Interest Group Pop Attraction for 2 years [Ruler] should stand down. Change progress of Civil War by −5% [Ruler] gains Failures of Judgement Failures of Judgement Ruler modifier −30 Popularity for 2 years |

id

### In the Interest of the Nation

Stressing the importance of staying up to date with recent military advancements, the government has proposed sending [Politician] on a military fact finding mission to [Country] - a thinly veiled plot to distance the quarrelsome general from his increasingly insurgent supporters.
---

Flavor text:
At the approximate moment when the steam lifted away from the mirror, it dawned on him that the government might as well have asked him to find snow in a desert. Had that realization come earlier, he might have had the good sense to just say, 'No.' Saying so now would only make him out to be a fool.
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Revolutionary Movement is Reactionary Revolution Progress is under 34% Any insurrectionary, non-marginalized Interest Group: At least one of these: Interest Group is Armed Forces Interest Group Leader is a General Any great or major power has at least Neutral relations with Event Source |
| Have him pack his bags. Actually, pack them for him. Change progress of Civil War by −5% [Political Movement] gains Shipped Off Opposition Leader Shipped Off Opposition Leader Political movement modifier +20% Political Movement Activism for 5 years Armed Forces gains Insidious Fact Finding Mission Insidious Fact Finding Mission Interest group modifier −2 Interest Group Approval for 5 years [Politician] is sent off on a year-long fact finding mission. [Politician] drops all assignments and becomes busy. Funding him to gallavant around [Country Capital]? No thank you. Armed Forces gains Amassing Strength Amassing Strength Interest group modifier +10% Interest Group Political Strength for 5 years One of 2 options will happen: 80% chance of: Change progress of Civil War by 5% 20% chance of: Change progress of Civil War by 10% |

id

### An Officer and a Gentleman

Returning from the fact finding mission to [Country] with a head full of ideas and a suitcase full of expensive liquor, [Politician] is once again free to pursue his domestic ambitions.
---

Flavor text:
If one chases a wild goose for long enough, one is bound to learn a few things: firstly, that most beasts tire before a human will. And secondly, there's more than just the one thing to hunt. In this case, everything asked for and more upon a silvery platter.
And with a splash of the right drink, any sensible leader would want to hear of these new and terrible wonders.
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: None |
| For better or for worse, [Politician] is back. [Politician] is no longer busy Gains Results of the Fact Finding Mission Results of the Fact Finding Mission Country modifier +10% Military Research Speed for 5 years If Revolutionary Movement is Reactionary Then One of 2 options will happen: 50% chance of: Change Progress of Civil War by 5% 50% chance of: Armed Forces gains Amassing Strength Amassing Strength Interest group modifier +10% Interest Group Political Strength for 5 years One of between 0 to 7 options will happen: 20% chance of: [Politician] gains trait Innovative 20% chance of: [Politician] gains trait Meticulous 20% chance of: [Politician] gains trait Charismatic 10% chance of: [Politician] gains trait Syphilis 10% chance of: [Politician] gains trait Cocaine Addiction 10% chance of: [Politician] gains trait Expensive Tastes 10% chance of: [Politician] gains trait Bigoted |

id

### Scrips Scrap Ravish [State]

Protesting the payment of wages in the form of scrips - credit only exchangeable at a company store - workers of the major [Building] in [State] have commenced a riot, torching the controversial store and marching on the company's main offices, demanding the institution of cash wages.
---

Flavor text:
"You load 16 tons, what do you get?
Another day older and deeper in debt
St. Peter, don't you call me 'cause I can't go
I owe my soul to the company store"
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: At least one of these: Revolution is from Socialist Movement Both: Revolution is from Liberal Movement Does not have Council Republic Revolution Progress is under 34% Any Incorporated State with 10% or more Turmoil: Any level 3 or higher Building with 50% or more employment: At least one of these: Is Industry Building Is Heavy Industry Building Is Raw Industry Building Industrialists are not Marginalized |
| The nature of payments is a company matter, break up the riot. +5% of Laborers Pops in [State] become more Radical Industrialists gains Sided with Industrialists in Credit Matter Sided with Industrialists in Credit Matter Interest group modifier +2 Interest Group Approval for 5 years One of 3 options will happen: 20% chance of: Gains Bloody Suppressions Bloody Suppressions Political movement modifier +10% Political Movement Activism for 5 years 50% chance of: Change progress of Civil War by 5% 30% chance of: Nothing happens Let us not fan the flames. There is merit to the workers' demands. Enact legislation banning the substitution of cash wages with company credit. +2% of Capitalists Pops in [Country] become more Radical Industrialists gains Sided with Workers in Credit Matter Sided with Workers in Credit Matter Interest group modifier −2 Interest Group Approval for 5 years [Political Movement] gains Abolished Scrip Wages Abolished Scrip Wages Political movement modifier −25% Political Movement Activism for 5 years |

id

### [City] Garrison Refuses Order

Ordered to violently suppress a popular riot in [City], a battalion of the [State] garrison have refused their orders, claiming that the execution of such a command would run contrary to the laws of men and God alike.
---

Flavor text:
"Patriotism? I will gladly raise my rifle against the enemies of [Country]. Should the [Neighboring Country] come knocking, I will do my duty, as shall we all.
But to raise arms against kin? Against brothers in blood and faith? Si, this, this we cannot do."
---

| Is triggered by: Generic Pulse Event from Revolution or Secession |
|---|
| Trigger conditions: Revolution Progress is 34% or more Any Incorporated State: Turmoil is greater than, or equal to 25% Level 3 or more Barracks with 30% or more employment [Country] has a Rival |
| Insubordination! String up the ringleaders, and jail the rest. [State] +10% of Servicemen Pops become more Radical +2% of Officers Pops become more Loyalist [State] gains 10% Devastation Change progress of Civil War by −5% Hush this down. We shall rotate the garrison eventually. Change progress of Civil War by 5% Barracks gains Seditious Garrison Seditious Garrison Building modifier −20% Training Rate for 2 years Armed Forces gains Furious About Government Cowardice Furious About Government Cowardice Interest group modifier −5 Interest Group Approval for 2 years |

id

### In the Hands of the State

Did he smash his head into the cell wall? Was he tortured to death? The official story that the [Insurrectionist Interest Group]-affiliated revolutionary died from cholera convinces only the gullible and the willfully blind. Only one thing is for certain: his supporters are livid, and they are out for blood.
---

Flavor text:
"It was the freemasons, I tell you. I've heard it from the butcher down the road that the warden's a member of that accursed cabal. It's them or the [Culture]. Or both. The [Ruler] is one too, it's why they offed him."
"The [Ruler] is [Culture]?
"Listen, kid." he says, blowing a cloud of thick smoke into the dimly lit room."There's a lot of things they don't teach you in school."
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Revolutionary Movement is Revolution Revolution Progress is 34% or more Any Interest Group is Insurrectionary Any Incorporated State has 20% or more Turmoil Any Incorporated State has Discriminated pops |
| "Murderers", cries the crowd. Change progress of Civil War by 10% [Insurrectionary Interest Group] gains The Death of a Martyr The Death of a Martyr Interest group modifier −1 Interest Group Approval +5% Interest Group Political Strength for 5 years Only God and the warden know for sure. Let us kindly ask the latter. [Political Movement] gains Prison Stormed by Crowd Prison Stormed by Crowd Political movement modifier +10% Political Movement Activism for 5 years [State] gains 3% Devastation |

## Cultural secession events

id

### Secessionist Manifesto

A manifesto laying out the arguments for [Culture] independence has started to spread in [Country].
---

Flavor text:
"Should this sort of thing be illegal? It's not arguing for an armed revolution. [Culture] independence could be an entirely peaceful process. However, I will say this: if such a revolution comes, this is what they'll be shouting from the barricades."
---

| Is triggered by: Generic Pulse Event from Secession |
|---|
| Trigger conditions: Any Cultural Minority Movement is Insurrectionary Civil War progress is under 30% |
| Option conditions Always enabled: Start a propaganda campaign to counter these arguments. [Cultural Minority Movement] gets Refuting Secessionist Manifesto Refuting Secessionist Manifesto Political movement modifier −10% Political Movement Pop Attraction −5% Political Movement Activism for 5 years Change progress of Civil War by -10% [Country] gets Refuting Secessionist Manifesto Refuting Secessionist Manifesto Country modifier −10% Authority for 5 years Enabled if: Has Censorship or Outlawed Dissent enacted Ban the manifesto. [Cultural Minority Movement] gets Censored Secessionist Manifesto Censored Secessionist Manifesto Political movement modifier −20% Political Movement Pop Attraction +5% Political Movement Activism for 5 years Change progress of Civil War by -15% [Country] gets Suppressing Secessionist Manifesto Suppressing Secessionist Manifesto Country modifier −5% Authority for 5 years Always enabled: Pay it no mind. [Cultural Minority Movement] gets Circulating Secessionist Manifesto Circulating Secessionist Manifesto Political movement modifier +10% Political Movement Pop Attraction for 5 years Change progress of Civil War by 10% |

id

### Official Translations

The government has received requests from the [Culture] to provide translations of some official documents into their language.
---

Flavor text:
"When you speak of the [Culture] as uneducated, you are seemingly referring to those of us who do not speak two languages, but only one — like you."
---

| Is triggered by: Generic Pulse Event from Secession |
|---|
| Trigger conditions: Any Cultural Minority Movement is Insurrectionary Civil War progress is under 30% |
| It is important that these documents are accessible to all! 5% of [Culture] pops in [Country] become more loyal [Country] gets Translating Official Documents Translating Official Documents Country modifier −10% Bureaucracy for 5 years They should learn the official language. 5% of [Culture] pops in [Country] become more radical |

id

### [Culture] Leadership

A [Culture] politician with secessionist sympathies has risen to prominence in the [Interest Group].
---

Flavor text:
"Have you heard who spoke at their last rally? To think that the opposition gives credence to [Culture] propaganda now! The sitting government would never host a speaker like that. Which, incidentally, was the exact argument made in the speech itself."
---

| Is triggered by: Generic Pulse Event from Secession |
|---|
| Trigger conditions: Any Cultural Minority Movement is Insurrectionary Civil War progress is under 30% |
| Immediate effects: Create a Sovereignist character with Charismatic and Basic Political Operator of the relevant culture representing an Interest Group not in government |
| A [Culture] political leader? Unthinkable! 2% of [Culture] Pops in [Country] become more radical Character becomes an agitator Change progress of Civil War by -10% Anyone can make it in [Country]. Character becomes leader of respective Interest Group |

id

### Secessionists Protest

Proponents of the [Culture] secession movement have gathered for a public protest.
---

Flavor text:
As the crowd began to gather, a tension seemed apparent among onlookers and passers-by, more than that which would be expected at the sight of a political rally. Perhaps the agenda of national independence stirred up thoughts about a civil war, or perhaps—more likely—it was simply the unfamiliar feeling of finding themselves outnumbered even momentarily by [Culture] people.
---

| Is triggered by: Generic Pulse Event from Secession |
|---|
| Trigger conditions: Any Cultural Minority Movement is Insurrectionary Civil War progress is between 30% and 70% |
| Break it up. [Country] gets Suppressing Secessionist Protest Suppressing Secessionist Protest country modifier −10% Authority for 5 years Changes progress of Civil War by -10% If has Right of Assembly or Protected Speech enacted, Every Interest Group endorsing either law gets Curtailed Free Speech Curtailed Free Speech interest group modifier −3 Interest Group Approval for 5 years Let them be heard. [Cultural Minority Movement] gets Secessionist Rallies Secessionist Rallies political movement modifier +20% Political Movement Pop Attraction (Decaying) for 5 years |

id

### [Culture] Politician Speaks Out

[IG Leader], leader of the [Interest Group], one of our nation's most prominent [Culture] figures, has spoken out in favor of an independent [Culture] nation.
---

Flavor text:
"My political goals may have been shaped by my upbringing, but I have never let my [Culture] background define them. However, it looks like increasingly it is the only criteria by which [Country] intends to define me."
---

| Is triggered by: Generic Pulse Event from Secession |
|---|
| Trigger conditions: Any Cultural Minority Movement is Insurrectionary Civil War progress is between 30% and 70% Any Interest Group's leader belongs to secessionist culture |
| Immediate effects: Save secessionist culture IG leader as Secessionist leader Save leader's IG as Secessionist IG |
| Tell the [Interest Group] to keep this traitor in check! [Interest group] gets Secessionist Leader Threatened Secessionist Leader Threatened Interest group modifier −4 Interest Group Approval for 5 years [Cultural Minority Movement] gets Suppressed Secessionist Leader Suppressed Secessionist Leader Political movement modifier −10% Political Movement Pop Attraction +5% Political Movement Activism for 5 years Change progress of Civil War by -10% Ignore these pointless ramblings. [IG leader] gets Inconsequential Speech Inconsequential Speech Interest group leader modifier −25 Popularity for 5 years [Interest group] gets Secessionist Leader Ignored Secessionist Leader Ignored Interest group modifier −2 Interest Group Approval for 5 years Perhaps it's time that this movement is heard. [Cultural Minority Movement] gets Tolerated Secessionist Leader Tolerated Secessionist Leader Political movement modifier +20% Political Movement Pop Attraction −10% Political Movement Activism for 5 years |

id

### Nationalist Opera

The performance of an opera with nationalist revolutionary themes at an upcoming festival is being openly associated with the [Culture] secession movement by its proponents.
---

Flavor text:
"Monday, the 23rd, fireworks; Tuesday, the 24th, illuminations; Wednesday, the 25th, revolution."
---

| Is triggered by: Generic Pulse Event from Secession |
|---|
| Trigger conditions: Any Cultural Minority Movement is Insurrectionary Civil War progress is above 70% |
| Cancel the fireworks. 2% of [Culture] pops in [Country] become more radical Cancel the illuminations. 5% of [Culture] pops in [Country] become more radical [Country] gets modifier Illuminations Canceled Illuminations Canceled Country modifier −5% Bureaucracy for 5 years Changes progress of Civil War by -10% Cancel the revolution. [Country] gets modifier Revolution Canceled Revolution Canceled Country modifier −10% Authority for 5 years Changes progress of Civil War by -15% |

id

### Secessionists Bomb Building

The militant wing of the [Culture] secession movement have claimed responsibility for an explosion at a government building, annoucning that the time for open war is rapidly approaching.
---

Flavor text:
"Perhaps we cannot decide if there will be a war. Perhaps we cannot even decide when there will be a war. But perhaps our decisions, while trying to exercise control over these issues, will determine who will be on our side when war comes."
---

| Is triggered by: Generic Pulse Event from Secession |
|---|
| Trigger conditions: Any Cultural Minority Movement is Insurrectionary Civil War progress is above 70% Any state has a Government Administration |
| Immediate effects: Save random state with Government Administration as Terrorist Attack State |
| Our very nation is threatened by the [Culture] menace. 10% of [Culture] pops in [Country] become more radical Changes progress of Civil War by -15% [State] gets 15% devastation We will not let this loathsome act ruin the fragile peace we have. Every Interest Group endorsing National Supremacy gets Soft on Minorities Soft on Minorities Interest group modifier −3 Interest Group Approval for 5 years Changes progress of Civil War by -10% [State] gets 15% devastation |

id

### [Culture] Horrors

|  | Available only with the [National Awakening](National Awakening.md) DLC enabled. |
|---|---|

---

Newspapers around the world are reporting about war crimes committed by our soldiers during our recent conflict with the [Culture] rebels.
---

Flavor text:
The number of children killed in these massacres is something enormous. They were often spitted on bayonets, and we have several stories of eye-witnesses who saw the little babes carried about the streets, both here and at Olluk-Kni, on the points of bayonets.
—J. A. MacGahan,
The Daily News.
---

| Is triggered by: Random pulse from crushing cultural secession |
|---|
| Trigger conditions: This event has not happened before Average acceptance of secession culture is under 40 |
| Immediate effects: Save random general as Scapegoat Save random seceding state as Rebel state |
| Option conditions Always enabled: These are horrific lies! [Country] infamy increased by 20 Enabled if: "Scapegoat" general is alive Publicly hang [General] for these crimes. [Country] infamy increased by 10 [General] dies [General's IG] gets Scapegoated Scapegoated Interest group modifier −4 Interest Group Approval (Decaying) for 10 years Enabled if: Highest relations with a great power are at least 20 Our contacts in [Friendly GP] will vouch for us. [Country] infamy increased by 10 [Country] relations towards [Friendly GP] decrease by 30 Always enabled: The next rebels will get much worse. [Country] infamy increased by 30 [Country] gets Terrified Dissidents Terrified Dissidents Country modifier −20% Suppression impact on Political Movement attraction −20% Political Movement Activism (Decaying) for 10 years For all options: [Rebel state] gets 20 devastation [Rebel state] gets Horrific Reprisals Horrific Reprisals State modifier −30% Migration Attraction +10% Mortality −2 Standard of Living (Decaying) for 10 years 10% of [Culture] pops in [Rebel state] lose their lives |

## Interest group revolutionary events

id

### Landowners Have Demands!

The Landowners are on the precipice of revolt, threatening to join the revolution if certain demands are not met.
---

Flavor text:
"Control of [Country] is slipping through the fingers of this weak and listless government. Someone must reclaim it. We know how to rule, but if you will not heed our advice, the cause is lost."
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Any Interest Group is Insurrectionary Landowners: Are not Revolutionary Are not in the Government Are not Marginalized Approval is between −1 and −8 |
| Option conditions Always enabled: Whatever satisfies their so-called 'dignity', let them have it. Landowners gains Concessions and Appeasement for 2 years +10% Political Strength +5 Approval Always enabled: Ridiculous! They have no right to ask for anything. Landowners: Becomes insurrectionary Gains Unappeased for 2 years −7 Approval Enabled if: Has enacted Dedicated Police Force or Militarized Police Force They can be dignified in handcuffs. Landowners gains Mass Arrests for 1 year −15 Political Strength −10 Approval |

id

### Rural Folk Are Sowing Discord!

The Rural Folk are furious with the government, and it seems that they may join the current revolution if we cannot appease them.
---

Flavor text:
"We know better than any the cost of war, the devastation of burned fields and ransacked cottages. We would not take up arms unless we had no other recourse. Do not use this as an excuse to test our patience - without us, [Country] starves."
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Any Interest Group is Insurrectionary Rural Folk: Are not Revolutionary Are not in the Government Are not Marginalized Approval is between −1 and −8 |
| Option conditions Always enabled: Let us hope concessions now can be the seed of peace for the future. Rural Folk gains Concessions and Appeasement for 2 years +10% Political Strength +5 Approval Always enabled: They will get nothing from us! Rural Folk: Becomes insurrectionary Gains Unappeased for 2 years −7 Approval Enabled if: Has enacted Dedicated Police Force or Militarized Police Force If they sow the wind, then they can reap the whirlwind! Rural Folk gains Mass Arrests for 1 year −15 Political Strength −10 Approval |

id

### Armed Forces Are Getting Bellicose!

Officers associated strongly with the Armed Forces have publicly issued a list of grievances, and demand immediate action from the government. Dark rumors suggest they may join the revolution if they are not satisfied.
---

Flavor text:
"We are sworn to defend [Country], but we must ask ourselves at which point the government itself is the greatest threat to the integrity of the nation it is governing. There is a war coming. Trust me, you will want the real soldiers on your side."
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Any Interest Group is Insurrectionary Armed Forces: Are not Revolutionary Are not in the Government Are not Marginalized Approval is between −1 and −8 |
| Option conditions Always enabled: We salute the sacrifices our soldiers have made and recognize their need for support. Armed Forces gains Concessions and Appeasement for 2 years +10% Political Strength +5 Approval Always enabled: Here's some orders for you: Get out! Armed Forces: Becomes insurrectionary Gains Unappeased for 2 years −7 Approval Enabled if: Has enacted Dedicated Police Force or Militarized Police Force Dummy Text Armed Forces gains Mass Arrests for 1 year −15 Political Strength −10 Approval |

id

### Industrialists Are Steaming!

A disgruntled consortium of Industrialists, unhappy with the government, are demanding 'compensation'. If we refuse, they threaten to throw in their lot with the Revolution.
---

Flavor text:
"An insurrection would be a setback, a stall on [Country]'s road to becoming a modern nation, but perhaps an inevitable one. If there is to be a war, it would certainly be better for it to be quick. Could you make it quick?"
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Any Interest Group is Insurrectionary Industrialists: Are not Revolutionary Are not in the Government Are not Marginalized Approval is between −1 and −8 |
| Option conditions Always enabled: Let's settle for this deal. Industrialists gains Concessions and Appeasement for 2 years +10% Political Strength +5 Approval Always enabled: Let's pass - their price is too high. Industrialists: Becomes insurrectionary Gains Unappeased for 2 years −7 Approval Enabled if: Has enacted Dedicated Police Force or Militarized Police Force They make a strong case for their own imprisonment. Industrialists gains Mass Arrests for 1 year −15 Political Strength −10 Approval |

id

### Intelligentsia Have Issued Demands!

The Intelligentsia have written a manifesto, demanding the government make certain concessions in order to protect the public welfare and preserve liberty. If not, they hint that more drastic actions may be taken.
---

Flavor text:
"We prefer to win with words, but words can implore reason or extol action. Praxis follows theory. If you need ideas, we have them, if not, someone else is surely in need."
---

| Is triggered by: Generic Pulse Event from Revolution |
|---|
| Trigger conditions: Any Interest Group is Insurrectionary Intelligentsia: Are not Revolutionary Are not in the Government Are not Marginalized Approval is between −1 and −8 |
| Option conditions Always enabled: They make a strong case for concessions. Intelligentsia gains Concessions and Appeasement for 2 years +10% Political Strength +5 Approval Always enabled: They make a strong case for nothing at all. Intelligentsia: Becomes insurrectionary Gains Unappeased for 2 years −7 Approval Enabled if: Has enacted Dedicated Police Force or Militarized Police Force They make a strong case for their own imprisonment. Intelligentsia gains Mass Arrests for 1 year −15 Political Strength −10 Approval |

## References
