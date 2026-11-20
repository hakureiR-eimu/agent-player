---
title: Production and technology content
source: https://vic3.paradoxwikis.com/Production_and_technology_content
pageid: 9888
categories: [1.13, Expand, Scripted_content, Journal, Events]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

|  | Please help improve this article or section by [expanding it](https://vic3.paradoxwikis.com/index.php?title=Production_and_technology_content&action=edit). |
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
The following journal entries and events are related to production methods, technological advancement, and industrial development.

## Production method events

id

### Dangerous Equipment

The [Building] in [State] have seen an increase in workplace injuries due to increased mechanization and poor safety regulations.
---

Flavor text:
Accidents have always happened, but I felt like I used to have time to react. Not this time. I grabbed his arm to pull him out of the way, but I'd barely got hold of his wrist before the arm was all I held onto.
---

| Is triggered by: None |
|---|
| Trigger conditions: At least one of these: Has enacted No Workers' Rights Has enacted Serfdom Any State: Has an Industrialized Production Method Has any building using the following production methods: Textile Mills Mechanized Looms Automatic Power Looms Furniture Manufacturies Mechanized Workshops Water-tube Boiler Rotary Valve Engine Assembly Lines Tooling Workshops Water-tube Boiler Rotary Valve Engine Assembly Lines Paper Mills, Steel Mills, or Motor Industries Water-tube Boiler Rotary Valve Engine Neither of: Has modifier Industrial Safety Slowdowns Industrial Safety Slowdowns State modifier −10% Manufacturing Industries Throughput Has modifier Lacking Industrial Safety Regulations Lacking Industrial Safety Regulations State modifier +2% Mortality of Engineers employed in Manufacturing +4% Mortality of Laborers employed in Manufacturing +4% Mortality of Machinists employed in Manufacturing |
| Immediate effects: Saves eligible building (see trigger) as [building] and its state as [state] |
| Slow down production while the staff adjusts to this new machinery. [State] gets Industrial Safety Slowdowns Industrial Safety Slowdowns State modifier −10% Manufacturing Industries Throughput for 5 years Every interest group which has a stance on Regulatory Bodies that is less than neutral: Gets Slowed Down Production Slowed Down Production Interest group modifier −2 Interest Group Approval for 5 years We cannot pull the brakes on the engines of progress! [State] gets Lacking Industrial Safety Regulations Lacking Industrial Safety Regulations State modifier +2% Mortality of Engineers employed in Manufacturing +4% Mortality of Laborers employed in Manufacturing +4% Mortality of Machinists employed in Manufacturing for 5 years Every interest group which has a stance on Regulatory Bodies that is greater than neutral: Gets Ignored Safety Concerns Ignored Safety Concerns Interest group modifier −2 Interest Group Approval for 5 years |

id

### Untrained Hands

Children working in the [Building] in [State] have suffered injuries trying to operate the machinery used in production.
---

Flavor text:
After examining the boy's hand, the doctor sat back down, turned to the mother and sighed deeply.
"Well, I'm afraid your son is never going to become a great musician," he said, "but then again, perhaps that was never one of his more likely prospects."
---

| Is triggered by: None |
|---|
| Trigger conditions: Has enacted Child Labor Allowed Any state: Has an Industrialized Production Method Has any building using the following production methods: Textile Mills Mechanized Looms Automatic Power Looms Furniture Manufacturies Mechanized Workshops Water-tube Boiler Rotary Valve Engine Assembly Lines Tooling Workshops Water-tube Boiler Rotary Valve Engine Assembly Lines Paper Mills, Steel Mills, or Motor Industries Water-tube Boiler Rotary Valve Engine |
| Immediate effects: Saves eligible building (see trigger) as [building] and its state as [state] |
| Keep children off the factory floor! [State] gets Child Labor Restrictions Child Labor Restrictions State modifier −10% Dependents Income for 5 years These new industries need all the employees they can get. [State] gets Dangerous Child Labor Dangerous Child Labor State modifier +2% Mortality of Laborers employed in Manufacturing for 5 years Every interest group which has a stance on Child Labor Allowed that is less than neutral: Gets Child Crushing Machines Child Crushing Machines Interest group modifier −3 Interest Group Approval for 5 years |

id

### Eternal Vigilance

Protesters from the Temperance movement are objecting to the production of liquor in [State].
---

Flavor text:
"They say that it was weakness of character that killed my husband, like any man who takes to the bottle. I can live with the shame of these accusations, but why must my children grow up hearing such things about their father when those who fill the bottles are utterly unashamed of ruining so many families and lives?"
---

| Is triggered by: None |
|---|
| Trigger conditions: Any state: Has a Food Industry using the Pot Stills or Patent Stills production method Does not have Liquor Production Ban Liquor Production Ban State modifier −100% Building Liquor output or Liquor Production Restrictions Liquor Production Restrictions State modifier −50% Building Liquor output Devout does not have Permitted Limited Liquor Production Permitted Limited Liquor Production Interest group modifier −1 Interest Group Approval nor Permitted Unrestricted Liquor Production Permitted Unrestricted Liquor Production Interest group modifier −3 Interest Group Approval |
| Immediate effects: Saves random state with eligible building (see trigger) as [state] |
| We must stop distilling this poison! [State] gets Liquor Production Ban Liquor Production Ban State modifier −100% Building Liquor output for 5 years If JE The Temperance Movement is active: This will greatly increase the progress in the Temperance Movement Journal Entry. ( +5 ) Let us cease production of the strongest spirits. [State] gets Liquor Production Restrictions Liquor Production Restrictions State modifier −50% Building Liquor output for 5 years Devout gets Permitted Limited Liquor Production Permitted Limited Liquor Production Interest group modifier −1 Interest Group Approval for 5 years If JE The Temperance Movement is active: This will increase the progress in the Temperance Movement Journal Entry. ( +2 ) [State] should take pride in its liquors! Devout gets Permitted Unrestricted Liquor Production Permitted Unrestricted Liquor Production Interest group modifier −3 Interest Group Approval for 5 years If JE The Temperance Movement is active: This will decrease the progress in the Temperance Movement Journal Entry. ( -5 ) |

id

### War Profiteering

Pacifists led by [Character] are protesting against the weapons manufacturing in [State]
---

Flavor text:
"Some may tell you that [Country] is at peace," [Character] told the crowd. Then [he] gestured towards the workshop and with genuine anger in [his] voice, continued:
"I tell you, as long as these rifles are fired in any country in this world, we are not at peace! The blood of these wars is also on our hands and will not be washed clean before we cease to make these instruments of death."
---

| Is triggered by: None |
|---|
| Trigger conditions: Is not at war Any Interest Group: Leader has Pacifist ideology Any state: Has an Arms Industries |
| Immediate effects: Saves random state with eligible building (see trigger) as [State] |
| Halt production of the rifles until this settles down. [State] gets Arms Manufacturing Ban Arms Manufacturing Ban State modifier −100% Building Small Arms output for 5 years Significantly reduce weapon production as a compromise. [State] gets Arms Manufacturing Restrictions Arms Manufacturing Restrictions State modifier −50% Building Small Arms output for 5 years Every IG whose leader is Pacifist gets Permitted Limited Arms Manufacturing Permitted Limited Arms Manufacturing Interest group modifier −1 Interest Group Approval for 5 years We shall not be shamed for our good craftsmanship! Every IG whose leader is Pacifist gets Permitted Unrestricted Arms Manufacturing Permitted Unrestricted Arms Manufacturing Interest group modifier −3 Interest Group Approval for 5 years |

id

### A Good Vintage

The wine produced in [State] has been lauded by sommeliers as outstanding.
---

Flavor text:
"When people say that something ages like wine, they don't always make the distinction between wine and
wine
. So let me make that distinction. If you can get your hands on a bottle from [State], that bottle can be more than just a good time—it can be an investment."
---

| Is triggered by: None |
|---|
| Trigger conditions: Any state: Has a Vineyards |
| Immediate effects: Saves random state with eligible building (see trigger) as [State] |
| Make this an exclusive product for export. [Country] gets Exclusive Wine Exclusive Wine Country modifier +5% Prestige for 5 years Increase production to meet the booming demands. [State] gets Popular Wine Popular Wine State modifier +35% Building Wine output for 5 years |

## Industrial accident events

id

### The Great Garment Factory Fire

A deadly fire has killed many workers in [State], due in part to dangerous working conditions and locked emergency exits. It has been revealed that [guilty factory owner], a prominent member of the [guilty factory owner IG], was the owner of the now-scorched factory.
---

Flavor text:
One of the men who tried to put out the fire testified at the inquiry. "I thought the room was just full of charred machinery," he said, "but then I stepped on something soft."
---

| Is triggered by: None |
|---|
| Trigger conditions: Has not enacted Workers' Protections nor Regulatory Bodies Cannot happen again for 51 months Any character: Is a Politician but not a Ruler Is valid for events [1] Is not busy Interest Group: Is not insurrectionary or marginalized Is one of Petite Bourgeoisie, Landowners, Industrialists, or Armed Forces Any state: Has a Textile Mills which does not have the Handsewn Clothes Production Method active |
| Immediate effects: Random valid character (see trigger) is saved as [guilty factory owner] His/her interest group is saved as [guilty factory owner IG] Random valid state (see trigger) is saved as [state] |
| This is just the price of progress. 5% of Lower Strata pops in [State] become more radical [Guilty factory owner IG] gets Gaining Support Gaining Support Interest group modifier +1 Interest Group Approval +15% Interest Group Political Strength for 5 years [Guilty factory owner] must be held responsible for these deaths! [Guilty factory owner] will be arrested and removed from his position of power. [Guilty factory owner IG] gets Power Challenged Power Challenged Interest group modifier −3 Interest Group Approval −10% Interest Group Political Strength for 5 years |

id

### Dyeworks Accident

Several workers dyed today at the [State] dyeworks, when an industrial-sized tub of hot dye accidentally spilled out over the workshop floor and the unsuspecting workers.
---

Flavor text:
Locals are upset about the incident, claiming that the poor safety regulations in the hot and dangerous workplace are to blame for the accident, and are urging the government to take action. As rescue workers left the scene, several workshop employees were left dyeing.
---

| Is triggered by: None |
|---|
| Trigger conditions: Any state: Has a Textile Mills Does not have Regulatory Bodies or Workers' Protections enacted Cannot happen again for 5 years |
| Immediate effects: Saves random state with eligible building (see trigger) as [State] |
| Always enabled: We shall all dye sooner or later. [State] gets Dyeworks Accident Dyeworks Accident State modifier +4% Mortality of Laborers employed in Manufacturing for 5 years 5% of Laborers pops in [State] become more radical Enabled if: Trade Unions are not revolutionary They shall not have dyed in vain! [State] gets Dyeworks Accident Dyeworks Accident State modifier +4% Mortality of Laborers employed in Manufacturing for 5 years Trade Unions get Gaining Support Gaining Support Interest group modifier +1 Interest Group Approval +15% Interest Group Political Strength for 5 years |

id

### The Brave Engineer

A railroad accident in [State] only narrowly avoided heavy fatalities due to the quick thinking of the train's engineer, who perished in the crash. Only a few people died, but the wreckage will still take some time to clear.
---

Flavor text:
"Come all you rounders, if you want to hear a story all about a brave engineer..."
---

| Is triggered by: None |
|---|
| Trigger conditions: Any state: Has a Railway Cannot happen again for 5 years |
| Immediate effects: Saves random state with eligible building (see trigger) as [State] |
| Always enabled: Thank goodness for quick-thinking engineers! [State] gets Death of a Railman Death of a Railman State modifier −5 Infrastructure for 5 years Enabled if: Trade Unions are not revolutionary Railmen should get more than a song for dying on the job. [State] gets Death of a Railman Death of a Railman State modifier −5 Infrastructure for 5 years Trade Unions get Gaining Support Gaining Support Interest group modifier +1 Interest Group Approval +15% Interest Group Political Strength for 5 years |

id

### The Great Molasses Flood

A storage tank full to the brim with molasses intended for rum distillation has burst, flooding the streets of [City]'s commercial center, killing dozens and injuring hundreds of bystanders.
---

Flavor text:
"The molasses, waist-deep, covered the streets and swirled and bubbled about the wreckage. Here and there struggled a form... whether it was animal or human being was impossible to tell. Only an upheaval, a thrashing about in the sticky mass, showed where any life was."
---

| Is triggered by: None |
|---|
| Trigger conditions: Any state: Has a Food Industries Does not have the No Distillery Production Method active Cannot happen again for 5 years |
| Immediate effects: Saves random state with eligible building (see trigger) as [State] |
| Close the distilleries while the wreckage gets cleared. [State] gets Diminished Rum Production Diminished Rum Production State modifier −50% Food Industries building Throughput for ' 5 years One tragedy must not stop progress! 5% of Machinists, Engineers, Clerks, and Shopkeepers pops in [State] become more radical |

id

### Boiler Explosion

A factory in [State] has been rocked by a tremendous boiler explosion, with dozens dead or injured. The story of this tragedy has quickly become a national event.
---

Flavor text:
"The scalding steam rushed out of the burst boiler and into the faces of the men on the shop floor. If the blast itself or the flying debris didn't get them, then the steam surely did."
---

| Is triggered by: None |
|---|
| Trigger conditions: Any state: Has the Water-tube Boiler active Cannot happen again for 5 years |
| Immediate effects: Saves random state with eligible building (see trigger) as [State] |
| These events are simply the price of progress. 5% of Lower Strata pops in [State] become more radical Industrialists get Gaining Support Gaining Support Interest group modifier +1 Interest Group Approval +15% Interest Group Political Strength for 2.5 years Workers should not be exploited and forced into such conditions. 5% of Upper Strata pops in [State] become more radical Trade Unions get Gaining Support Gaining Support Interest group modifier +1 Interest Group Approval +15% Interest Group Political Strength for 5 years Machines are dangerous! Industry itself is a cancer. 5% of Middle Strata pops in [State] become more radical Rural Folk get Gaining Support Gaining Support Interest group modifier +1 Interest Group Approval +15% Interest Group Political Strength for 5 years |

id

### Mining Accident

A mine in [State] has collapsed, trapping miners within the dark shafts below. The scale of the accident has made the tragedy a story across [State] and the nation.
---

Flavor text:
"They dug me out, but left my friend behind."
That was all the foreman was able to get out of the wretched boy. Sooty rags clung to him like wispy strands of a torn funeral jacket. Whether he held back his tears for fear of a beating, or to keep strong, the foreman did not know. He was spent for the day. The foreman hoped the manager had a mind for mercy.
---

| Is triggered by: None |
|---|
| Trigger conditions: Any state: Has an Coal Mines, Iron Mines, Lead Mines, or Sulfur Mines Does not have Regulatory Bodies or Workers' Protections enacted |
| Immediate effects: Saves random state with eligible building (see trigger) as [State] |
| This is a small price to pay for the march of industry. 5% of Lower Strata pops in [State] become more radical Industrialists get Gaining Support Gaining Support Interest group modifier +1 Interest Group Approval +15% Interest Group Political Strength for 5 years This outrageous abuse of the common man cannot continue! 5% of Upper Strata pops in [State] become more radical Trade Unions get Gaining Support Gaining Support Interest group modifier +1 Interest Group Approval +15% Interest Group Political Strength for 5 years These mines are a blight upon man and countryside alike. 5% of Middle Strata pops in [State] become more radical Rural Folk get Gaining Support Gaining Support Interest group modifier +1 Interest Group Approval +15% Interest Group Political Strength for 5 years |

## Technology events

id

### Unregulated Automobiles

Due to a spate of accidents, there have been calls to regulate automobiles.
---

Flavor text:
It is being reported that [an automobile accident occurred.] "Faster than a horse and twice as heavy. If people don't see why that's dangerous, I don't know what to tell you."
---

| Is triggered by: Yearly random pulse |
|---|
| Trigger conditions: Has researched Combustion Engine This event has not happened before Buy orders for Automobiles in our market is greater than 200 |
| Stricter laws make safer streets. Gets Automobile Safety Regulations Automobile Safety Regulations Country modifier −10% Motor Industries building Throughput for 5 years Industrialists get Disapprove of cars being restricted. Disapprove of cars being restricted. Interest group modifier −1 Interest Group Approval for 5 years People merely need to adjust. Industrialists get Approve of cars being unrestricted. Approve of cars being unrestricted. Interest group modifier +2 Interest Group Approval for 5 years Automobiles should have the right of way. 5% of lower strata pops become more radical |

id

### International Telephone Exchange

It has been suggested that by establishing a cross border telephone exchange with [Neighbor], we could improve relations more easily.
---

Flavor text:
"It certainly cuts down on misunderstandings when we can just pick up the telephone and work out what's going on across the border."
---

| Is triggered by: Yearly random pulse |
|---|
| Trigger conditions: Has researched Telephone The owner of any neighboring state: Is not controlled by a player Relations with us are greater than or equal to neutral Has researched Telephone This event has not marked them before |
| Immediate effects: Saves eligible country (see trigger) as [neighbor] Marks them as inelgible to be the participant of this event again |
| Sounds like a great idea. Relations towards [neighbor] improves by 20 I don't think so. No effect |

id

### Fireside Chat

[Title] [Ruler] has decided to use the new and exciting radio technology to connect more directly with the people.
---

Flavor text:
"It's like [he/she] is there in the room with me. It is hard not to be convinced."
---

| Is triggered by: Yearly random pulse |
|---|
| Trigger conditions: Has researched Radio This event has not happened before |
| Always enabled: It should express authority Gets Authoritarian Radio Announcements Authoritarian Radio Announcements Country modifier +15% Authority for 5 years Always enabled: It should make us look good. [Ruler IG] gets Good Radio Publicity Good Radio Publicity Interest group modifier +2 Interest Group Approval for 5 years Enabled if: [Ruler] has the trait Opium Addict Let me tell you about this new wonder drug. Gets Opium Endorsement Opium Endorsement Country modifier +25% Opium Plantations building Throughput +2.5% Mortality for 5 years |

id

### Weapons of War

An article has been published by the [Country] [Newspaper] about some of the weapons which our country uses in the ongoing [War] war.
---

Flavor text:
[The article focuses on the machine gun, a terrifying weapon which tears through flesh and bone at an almost inhuman rate./The article focuses on the use of chlorine gas, a terrifying weapon.] Members of the public are calling for the use of such weapons to be restricted.
"Such foul instruments of pain and torment have no place on earth."
---

| Is triggered by: Yearly random pulse |
|---|
| Trigger conditions: Has researched at least one of Automatic Machine Guns and Chemical Warfare Is at war This event has not happened before |
| Immediate effects: Save random ongoing war as [war] |
| Don't restrict them. War support in [War] decreases by 10 Intelligentsia gets Disapproves of No Weapon Restrictions Disapproves of No Weapon Restrictions Interest group modifier −1 Interest Group Approval for 5 years Coverup their usage. Gets Covering Up Controversial Weapon Use Covering Up Controversial Weapon Use Country modifier −25% Authority for 5 years |

id

### Photographs of [Country]

It has been suggested that we take and distribute some pictures of our country's most famous landmarks.
---

Flavor text:
"So many wonderful places all across our country! It just seems right that the world gets to see them too."
---

| Is triggered by: Yearly random pulse |
|---|
| Trigger conditions: Has researched Camera This event has not happened before |
| We should distribute them internationally. Gets Internationally-Distributed Photographs Internationally-Distributed Photographs Country modifier +5% Prestige for 5 years We should distribute them domestically. Gets Domestically-Distributed Photographs Domestically-Distributed Photographs Country modifier +20 Legitimacy for 5 years |

id

### Can-Do Attitude

Soldiers are complaining that they have no way to open their canned food.
---

Flavor text:
"Sure the food's a bit better, but what's the point if we can't get at it, eh? Some lads use rocks, others knives. The only reliable thing is how bloody annoying it is to eat."
---

| Is triggered by: Yearly random pulse |
|---|
| Trigger conditions: Has researched Canneries This event has not happened before |
| Spend some money to develop a way. Gets Developing Can Opener Developing Can Opener Country modifier +1 Government Expenses ( 0.015% of GDP ) for 5 years They'll figure it out. Armed Forces gets Lack of Can Opening Technology Lack of Can Opening Technology Interest group modifier −2 Interest Group Approval for 5 years |

## References

1. ↑ Is not the Emperor of Japan (does not have role character_role_emperor_of_japan ) Is not plotting a coup (does not have variable golpista_var ) Is an adult
