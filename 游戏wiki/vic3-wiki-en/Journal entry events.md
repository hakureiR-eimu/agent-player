---
title: Journal entry events
source: https://vic3.paradoxwikis.com/Journal_entry_events
pageid: 5725
categories: [1.13, Scripted_content, Expand, Articles_with_potentially_outdated_infoboxes, Events]
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
The following events are triggered by or start various [journal entries](https://vic3.paradoxwikis.com/Journal_entries).

|  | Please help improve this article or section by [expanding it](https://vic3.paradoxwikis.com/index.php?title=Journal_entry_events&action=edit). |
|---|---|

## Major situations

### Government Petition

id

#### [Interest group] Petition Government

Representing his constituents in the [Interest group], [Politician] has issued a formal petition to the [Country adjective] government to pass [Law].
---

Flavor text:
"Er, one last matter for the day, sir. Members of your constituency arrived this morning. They're... asking rather loudly and insistently... if you would meet with them about new legislation."
"Is that it? Goodness, you seem as if you've seen a ghost. I'm sure I can spare the last hours of light for them, can't I?"
"I-I believe so, sir. They weren't taking 'no' for an answer."
---

| Is triggered by: Activation Event for the Government Petition journal entry |
|---|
| Trigger conditions: None |
| We will see what we can do. No effect |

### The Krakatoa Eruption events

id

#### Days of Darkness

An eruption of unprecedented records has utterly destroyed the lives of many [Country pop] in the state of [State]. The explosion of the Krakatoa could be heard from hundreds of miles away and anything that had the ill fate of surrounding the island was immediately devastated.
---

Flavor text:
"And the day was made night. Those enormous waterfalls of fire cascading down the mountainside. A black cloud, gargantuan, all the birds have long abandoned this field.
Years from now I will sit by the fireplace and the light will disturb me no more."
---

| Is triggered by: Immediate effect of the events#krakatoa.1 Event. |
|---|
| Trigger conditions: Krakatoa is not part of [Country] |
| We shall help with all we have. Relations with [Krakatoa Country] improves by 30 Gains Krakatoa Humanitarian Help for 2 years +500 Government Expenses Nature is a capricious creature. Relations with [Krakatoa Country] deteriorates by 30 Relations Infamy increased by 5 For both options Activates The Krakatoa Eruption journal entry |

id

#### Nights of Waves

Waves taller than chimneys have ravaged the state of [State], a terrible consequence of the volcanic eruption.
---

Flavor text:
"I will never forget that silence."
---

| Is triggered by: Immediate effect of the events#krakatoa.1 Event. |
|---|
| Trigger conditions: Any Coastal State: Strategic Region is any of: Ethiopia Indochina Indonesia South China Japan Oceania Zanj Southern Africa South India |
| Immediate effects: One random qualifying coastal state is chosen and saved for the event |
| There are no words to describe this tragedy. The randomly chosen state gains a tsunami harvest condition An additional scripted effect is applied (not fully traced to its definition; needs in-game confirmation) |

id

#### Burning Ashes

The drop of temperature caused by the volcanic eruption has ruined the crops of all the nation and the farmers of [State] beg for help.
---

Flavor text:
"No food at home, sir, not a single root to be saved. Children ask questions, sir, the sky is always dark, always red. They're hungry, hungry and afraid, my lord - and so am I."
---

| Is triggered by: Pulse Event from the The Krakatoa Eruption journal entry |
|---|
| Trigger conditions: Any is a Farm or Plantation |
| Option conditions Always enabled: We can send them some food. The crop failure will also affect the rest of the world. Gains Volcanic Winter Relief Cost for 5 years +11200 Government Expenses Our states with farms or plantations will experience minor crop failures. Always enabled: There's nothing we can do. The crop failure will also affect the rest of the world. Our states with farms or plantations will experience minor crop failures. Enabled if: [State] has the Emergency Relief Decree Dummy Text |

id

#### Smoke Streams

Vivid red sunsets were reported for several months across the country. Fire engines were even called out in [State] to quench the apparent conflagration. Many artists and academics have expressed their interest in this phenomenon.
---

Flavor text:
"A blue and sometimes green moon, its inflammable luminescence igniting the night with unnatural intensity. White moonbeams shining through the clouds emerge purple, and sometimes also blue, green.
Lavender suns, noctilucent clouds, a distasteful fascination."
---

| Is triggered by: Pulse Event from the The Krakatoa Eruption journal entry |
|---|
| Trigger conditions: None |
| Only a painting could capture such beauty. [State] gets Sponsored Inspired Artists for 5 years +15% Arts Academy throughput Academics must ensure that we're prepared for the next eruption. Volcanic eruptions will be less damaging in the future. [State] gets Funded Volcanic Research for 5 years +15% University throughput |

### The Great Hunger events

Partially replaced by [Harvest conditions](Harvest condition.md) and [Food security](State.md) though famine_events.3 and famined_events.4 still exist.

### Springtime of the Peoples events

id

#### The Spark of Revolution

![Event trigger.png](https://central.paradoxwikis.com/images/3/35/Event_trigger.png) **The below description is one of several available for this event.**

The revolutionary events in [Country] are inspiring Radical sentiments across Europe.
---

Flavor text:
"I understand there is some concern that weaponry used in the [Country] revolution might find its way into neighboring countries and end up in the wrong hands. I fear not the gunpowder, but what might ignite it. Not every man desires power for its own sake, but if he is convinced he has been cheated out of his share, he may view it as his duty to claim it. What could be more dangerous than the idea that powder belongs to the people?"
---

| Is triggered by: The monthly country pulse, when the following conditions are fulfilled: Capital is in Europe Has researched Egalitarianism Country rank at least Major Power Either: Any "Springtime" (Liberal/Radical/Socialist) revolution has reached 25% progress Is France and has proclaimed the Third Republic |
|---|
| Trigger conditions: None |
| Who will lead [Country] to the future? Get Radical Sentiments Radical Sentiments Country modifier +50% Radical Movement Pop Attraction (Decaying) for 5 years 5% of Lower Strata pops become more radical 2% of Middle Strata pops become more radical [Radical Interest group Leader] gets Revolutionary Hero Revolutionary Hero Character modifier +50 Popularity for 5 years We will not let these ideals divide us! Get Radical Sentiments Radical Sentiments Country modifier +25% Radical Movement Pop Attraction (Decaying, weakened) for 5 years 2% of Lower Strata pops become more radical [Radical Interest group Leader] gets Treasonous Traitor Treasonous Traitor Character modifier −50 Popularity for 5 years |

id

#### The [Country] Revolution

Inspired by the revolutionary wave spreading across Europe, revolutionaries in [the capital city] have assembled to make demands of the [ruler title]. They call for Universal Suffrage, a democratic constitution, and the establishment of a National Guard.
---

Flavor text:
The crowd was spilling towards the [ruler]'s residence, now, kept back only by a thin wall of stone-faced soldiers. Insults and street detritus flew towards the row of bayonets and cannon, sending the horses' tails lashing. In the commercial districts, the retailers which had elected not to join the march were boarding up their shops. Further yet behind the impromptu lines, the workers had uprooted lamp-posts to batter down the city gates. The broken pipes cast an ominous half-glow over the streets.
---

| Is triggered by: Weekly pulse of the journal entry Springtime of the Peoples |
|---|
| Trigger conditions: Any "Springtime" (Liberal/Radical/Socialist) revolution has reached 25% progress Does not have the journal entry Divided Monarchists |
| We cannot risk a civil war. Get Revolutionary Cabinet Revolutionary Cabinet Country modifier +75 Legitimacy (Decaying) for 120 days If the country does not have Universal Suffrage, enact Universal Suffrage If the country does not have Right of Assembly, enact Right of Assembly If the country does not have National Guard, enact National Guard If the country has any variant of Serfdom, enact Tenant Farmers Every interest group that has the Liberal ideology or a Radical leader gets Off the Barricades Off the Barricades Country modifier +20 Interest Group Approval for 75 days Every interest group that does not have the Liberal ideology or a Radical leader gets Bloodless Revolution Bloodless Revolution Interest group modifier −90% Interest Group Political Strength (Decaying) for 12 months In 5 days, trigger a hidden event peoples_springtime.91 , which: Removes every interest group that does not have the Liberal ideology or a Radical leader Adds every interest group that has the Liberal ideology or a Radical leader to the Calls an election in 2 months Compromise on suffrage, but see this done. Get Revolutionary Cabinet Revolutionary Cabinet Country modifier +75 Legitimacy (Decaying) for 120 days If the country does not have Census Suffrage, enact Census Suffrage If the country does not have Right of Assembly, enact Right of Assembly If the country does not have National Guard, enact National Guard If the country has any variant of Serfdom, enact Tenant Farmers Every interest group that has the Liberal ideology or a Radical leader gets Off the Barricades Off the Barricades Country modifier +20 Interest Group Approval for 75 days Every interest group that does not have the Liberal ideology or a Radical leader gets Bloodless Revolution Bloodless Revolution Interest group modifier −90% Interest Group Political Strength (Decaying) for 12 months In 5 days, trigger a hidden event peoples_springtime.91 , which: Removes every interest group that does not have the Liberal ideology or a Radical leader Adds every interest group that has the Liberal ideology or a Radical leader to the Calls an election in 2 months Send in the Army immediately. A random revolution gets 15% progress |

### The Red Scare events

id

#### The Red Scare

The rise of the communist regime in [Communist Country] has spurred a sense of terror and mistrust across [Country] society. Many fear that [Communist Country] will be the next to fall to communism.
---

Flavor text:
Every newspaper on the stand bore a title more extreme than the last. Shrill newsboys hawked them on corners, sending competing claims of atrocity and terror across streets.
"Assassins and madmen claim power in [Communist Country]!" cried one of them. "Recovered "Red Bible" reveals agenda of world revolutionists!" shouts another. And amidst all of them marched ten thousand wide-opened ears, soaking up each sensational word as they hurried along to their stations.
---

| Is triggered by: Activation Event from the The Red Scare journal entry |
|---|
| Trigger conditions: None |
| It could happen here! 2% of Upper Strata pops become more Loyalist Every Interest group with either: Proletarian Ideology Stance on Council Republic is greater than Neutral [Interest group] gets The Red Scare (Decaying) for 10 years −20% Interest group political strength −3 Interest group Approval A panic would be wholly unwarranted. 2% of Lower Strata pops become more Loyalist Every Interest group with neither: Proletarian Ideology Stance on Council Republic is greater than Neutral [Interest group] gets Anti-Communist Fears (Decaying) for 10 years −5% Interest group political strength −3 Interest group Approval |

id

#### The Nationalization of Women

Following government hearings into the activities of the communist regime in [Communist Country], newspapers across [Country] have reported sensational stories about all adult women in [Communist Country] being nationalized as common property.
---

Flavor text:
"I saw it myself, before I fled. The Red authorities have mandated collective orgies, within which there is no respect for virtuous women. All women are forced to participate - the Ministry of Free Love registers every one of them, under threat of the bayonet."
"And you claim that, and I quote, "a girl, having reached her eighteenth year, is to become state property at one"?"
"Yes, yes. Their names are placed on a bulletin board in their towns, and all eligible men are permitted to marry them at will, as many as they wish..."
---

| Is triggered by: Pulse Event from the The Red Scare journal entry |
|---|
| Trigger conditions: Any non-marginalized Interest group is Anti-Communist : At least one of these: Is Industrialists Is Petite Bourgeoisie Is Landowners Is Devout Leader has any of: Traditionalist Fascist Integralist Ethno-Nationalist Theocrat Legitimist Luddite Corporatist Slaver Royalist Orléanist Bonapartist Stance on Council Republic is lower than Neutral |
| The Communists are coming for our women! Relations towards [Communist Country] deteriorates by 15 2% of [Anti-Communist Interest group] members become more Loyalist 2% of Lower Strata pops become more Radical This testimony seems highly suspect. Random [Anti-Communist Interest group]: Interest group gets Suspect Testimonies for 2 years −2 Interest group Approval |

id

#### Communism Criminality

Rumors about the atrocities of communists in [Communist Country] have reached the [Country] press, with reports about crimes against humanity and stacked corpses filling the front pages of newspapers.
---

Flavor text:
"Did you hear of the bombings the other day? This time it was a lawyer. One of the big ones advising the government."
"Another one? Heavens, that's the third this month. This is supposed to be a safe country."
"Safe? Bah, not with these Communist rats running around. They'll kill us all if we don't kneel down first."
---

| Is triggered by: Pulse Event from the The Red Scare journal entry |
|---|
| Trigger conditions: Any non-marginalized Interest group is Anti-Communist : At least one of these: Is Industrialists Is Petite Bourgeoisie Is Landowners Is Devout Leader has any of: Traditionalist Fascist Integralist Ethno-Nationalist Theocrat Legitimist Luddite Corporatist Slaver Royalist Orléanist Bonapartist Stance on Council Republic is lower than Neutral |
| Who knew that people could be so barbaric? Relations towards [Communist Country] deteriorates by 25 2% of Upper Strata pops become more Loyalist They had ought to publish something else, for once. Relations towards [Communist Country] deteriorates by 5 Random [Anti-Communist Interest group]: Interest group gets Mediocre Propaganda for 2 years −10% Interest group Attraction |

id

#### Marching Against Peace

Protestors inspired by the fierce rhetoric of [Progressive Leader] have carried out a march in [City], calling for military intervention against the communist regime in [Communist Country].
---

Flavor text:
What began as a few-dozen shouting men in the streets swelled to a corpus numbering the thousands. What began as a peaceful demonstration grew to chants of fire and fury, all baying for blood. What began as a show of fear transformed into a call for action.
Their demands were simple: tear out the [Communist Country Adjective] menace, no matter the cost.
---

| Is triggered by: Pulse Event from the The Red Scare journal entry |
|---|
| Trigger conditions: Any non-marginalized Interest group is Anti-Communist : Stance on Council Republic is lower than Neutral Any Character is Anti-Communist : None of these: Has the ideology Pacifist Has the ideology Anarchist Has the ideology Communist Has the ideology Vanguardist Is not a Ruler Is not an Heir |
| We must save the [Communist Country] people from themselves Relations towards [Communist Country] deteriorates by 20 Gains War Fever for 5 years +10 Maneuvers per Diplomatic Play −5% War Exhaustion from Casualties +5% Radicals from Standard of Living decreases 5% of Lower Strata pops in [State] become more Radical The people's energies are best spent on something more constructive. [Anti-Communist Leader] gets Dangerous Warmonger for 5 years −25 Popularity 5% of Upper Strata pops in [State] become more Radical |

id

#### In the Face of Revolution

Policemen chasing rumors of an allegedly planned communist uprising in [State] have stirred significant fear amongst the area's public. Local skeptics decry the disturbance as terrorism in itself.
---

Flavor text:
"Not sure I understand, superintendent. You want us to go to this block in the dead of the night, while everyone's asleep, to raid this warehouse on
suspicion
that it
might
be a communist meeting place?"
"That's exactly what I want you to do, sergeant. Now, might I count on you to carry out this task, or shall I volunteer some men for you?"
---

| Is triggered by: Pulse Event from the The Red Scare journal entry |
|---|
| Trigger conditions: Any Incorporated State has 15% or more turmoil Does not have No Police enacted |
| If it doesn't materialize, then we'll have done our jobs. [State] 2% of Upper Strata pops become more Loyalist 2% of Lower Strata pops become more Radical Gains Overpoliced State for 5 years +15% Radicals from Discrimination There is no reason to believe this is credible. Petite Bourgeoisie gets Risk of Revolution for 2 years −2 Interest group Approval |

id

#### The White Émigrés

A stream of wealthy [Communist Country Culture] émigrés feeling the communist regime in [Communist Country] have sought shelter in [Country], bringing with them tales of revolutionary terror and unbridled proletarian excess.
---

Flavor text:
"The worst was these new secret police, just like the old ones. They would round up people they didn't like, usually when all was dark and quiet. Sometimes the day too. And if we ever saw liquor trucks going to their offices... well, we never saw our neighbors again. We had to get out."
"Very brace. We'll take good care of you here. Anything for [Communist Country]'s most upstanding citizens."
---

| Is triggered by: Pulse Event from the The Red Scare journal entry |
|---|
| Trigger conditions: Red Scare Country: Does not have Closed Borders enacted At least one of these: Any Neighboring State: Has a Port |
| Give them a platform to tell their stories. An Agitator appears Agitator gets White Émigré for 5 years +15 Popularity −10% Character health [State] gets Émigrés Politics for 5 years +12% Migration Attraction −12.50% Council Republic Pop Support A tragic procession. [State] gets Émigrés Politics for 5 years +25% Migration Attraction −25% Council Republic Pop Support |

id

#### Progressive Dilemmas

The backlash against the policies of the [Communist Country Adjective] communists has led to mounting pressure on the progressive leaders of the [Progressive Interest group] to explicitly denounce the government of [Communist Country].
---

Flavor text:
They loomed over him, at least a half-dozen and all built to lift cisterns. At first, it was a courtesy call to the watering hole. Some boy fresh off the fields recognized him over a pint. Then the barmaid remembered his praise about [Communist Country]'s government. Now, it was a sizable crowd with six strongmen at the helm.
"Well... the thing with [Communist Country] is..."
---

| Is triggered by: Pulse Event from the The Red Scare journal entry |
|---|
| Trigger conditions: Any Interest group is Progressive : Leader has any of: Nihilist Radical Feminist Pacifist Social Democrat Humanitarian Enlightened Royalist Communist Vanguardist Anarchist |
| Option conditions Always enabled: For the [Leader Ideology] cause, not the [Communist Country] one! [Progressive Interest group] gets Compromised Party Line for 5 years −30% Interest group political strength Always enabled: This road leads to nothing but more extorted concessions. 2% of Upper Strata pops become more Radical [Progressive Interest group] gets Unbowed by Threats for 5 years −10% Interest group Attraction Enabled if: Any Interest group Leader is Socialist The socialist cause in [Country] is hopeless. [Socialist Interest group]: Leader: [Leader] will change ideology to Social Democrat [Leader] gets Traitor to the Revolution −35 Popularity [Interest group] gets Compromised Party Line for 5 years −15% Interest group political strength |

id

#### The [Communist Adj] Ark

With arrested communists beginning to stream into [Country] prisons, figures within the government have suggested deporting the noncitizens among them to [Communist Country] aboard a chartered cargo ship.
---

| Is triggered by: Pulse Event from the The Red Scare journal entry |
|---|
| Trigger conditions: Does not have Closed Borders enacted Any State has a Port Any Incorporated State 15% of Lower Strata pops is Radical Any Pop is Discriminated against Any [Communist Country] State has a Port |
| A wonderfully poetic suggestion. Laborers (Discriminated Pop) in [State] will move to [Communist Country State] 2% of Pops in [State] become more Loyalist They will serve their sentences on our soil. Petite Bourgeoisie gets Refused Deportation Proposal for 2 years 1 Interest group Approval |

id

#### A Subtler Terror

After years of competing propaganda and social mistrust, the Red Scare has ebbed to a more manageable level. Whilst many remain watchful for communist activity, the days of unmatched fear in [Country] have come to a relative end.
---

Flavor text:
"We have passed beyond the stage in political development when heresy-hunting is a permitted sport."
---

| Is triggered by: Timeout Event from the The Red Scare journal entry |
|---|
| Trigger conditions: None |
| Our nation will be made safe. Gains Anti-Communist Vigilance for 5 years' +10% Authority −5% Radicals from Standard of Living decreases −10% Political strength of Laborers Every Anti-Communist Interest group gets Anti-Communist Vigilance for 5 years +10% Interest group political strength +3 Interest group Approval We must repent for our own excesses. Gains Support for Civil liberties for 5 years +5% Loyalists from Standard of Living increases +10% Interest group political strength of Laborers −15% Censorship Pop Support Every Anti-Communist Interest group gets Weakened Anti-Communism for 5 years −5% Interest group political strength −2 Interest group Approval Anti-Communist conditions, either Has the Reactionary or Paternalistic ideology Leader has any of: Traditionalist Fascist Integralist Ethno-Nationalist Theocrat Legitimist Luddite Corporatist |

## Domestic Affairs events

### Other entries events

id

#### Winds of Change

[State] has come a long way since our attention was first brought to it, going from small houses and scattered farmlands to being on its way to become a blooming metropolis.
---

Flavor text:
The woman sighs, her old hands stop crocheting for a second. "When I was younger all of this was farmhands. Us kids would just play freely in the fields, not having to worry about getting hit by a cart or those criminals coming to get us. And we still had time to work!"
"Well grandma, now people will have even more places to work at."
---

| Is triggered by: Completion of the Urbanize Country journal entry |
|---|
| Trigger conditions: None |
| Finally, [State] shines like never before. [State] gets Heavily Urbanized for 2 years +25% Loyalists from Standard of Living increases This is not the end! [State] gets Urban Center Efficiency for 2 years +33% Urban Center throughput |

id

#### Road to Progress

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.12. |
|---|---|

---

The
Industrialists have expressed their satisfaction with the direction being taken by the country and its newly built factories.
---

Flavor text:
"There's only one possible direction: forward! Progress is like a train that doesn't stop, doesn't wait for anyone, you're either in or you're out."
---

| Is triggered by: Completion of the From Farms to Factories journal entry |
|---|
| Trigger conditions: None |
| We've done this for our people. [Country] gets Favored the People for 5 years +20% Loyalists from Political Movements And we shall support that train. Industrialists gets Favored the Industrialists for 5 years +2 Interest Group Approval +10% Interest Group Pop Attraction |

## Development events

### Resources events

id

#### A Dangerous Business

The efficiency our
Whaling Stations has proved to have a dangerous counterpart and death has become common to almost every voyage. It is a high price to pay, but the profit is equally high.
---

Flavor text:
The body of the whale lies as wide as the sky. Its head has been emptied and the barrels of oil are stained with blood.
A voice resounds throughout the wharf, "We lost a dozen of men," and then he starts to list them, and their towns; a few of them are from the capital, one of them has your brother's name.
The oil shimmers - the liquid gold-like blood of a siren, luring men to their deaths.
---

| Is triggered by: Completion of the The Whaling Industry journal entry |
|---|
| Trigger conditions: None |
| We need to ensure the safety of the sailors. Random Admiral gets Whaling Precautions for 5 years +25 Popularity [State] gets Whaling Precautions for 5 years −2% Whaling Stations Employee Mortality But it shines! [State] gets Whaling Boom for 5 years +33% Whaling Stations throughput |

id

#### The Atmospheric Engine

Through the widespread introduction of the atmospheric engine in the mining industry, productivity is at an all-time high.
---

Flavor text:
"When steam first began to pump and wheels go round at so many revolutions per minute, what are called business habits were intended to make the life of man run in harmony with the steam engine, and his movement rival the engine in punctuality."
---

| Is triggered by: Completion of The Atmospheric Engine journal entry |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: I'm sure we can squeeze a little more from these machines. Gains Utilizing the Atmospheric Engine for 5 years +33% Mines throughput Enabled if: Has researched Mechanical Tools Does not have Railways researched This has great implications for transport. Gains 3.50K progress on technology Railways Enabled if: Does not have Water-tube Boiler researched Perhaps there is an even better way. Gains 3.50K progress on technology Water-tube Boiler |

id

#### Rubber Boom

The recent expansion of the
Rubber Plantation in [State] has yielded extremely promising results. [Country] threatens to lead the world in rubber production.
---

Flavor text:
"The question is not what can be done with rubber, but rather what cannot be done. There is no end to its potential utilization, and it will surely become the foundational material of the modern world. Our finest minds are developing new applications for this versatile material."
---

| Is triggered by: Completion of Expand the Rubber Industry journal entry |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: We need more rubber! [State] gets Rubber Boom for 5 years +50% Migration Attraction +33% Rubber Plantation throughput Enabled if: Does not have Vulcanization researched What other uses could we find for rubber? Gains 4.15K progress on technology Vulcanization |

### Universities events

id

#### Higher Learning

The [Ruler Title] himself has officially opened the
University of [State]. Academia is beginning to flourish in [Country].
---

Flavor text:
Philosophy is the highest calling of mankind. Through philosophy we can overcome to understand the very foundations of metaphysics, the nature of the divine, and the essence of virtue. It stands to reason then, that only the most enlightened of wisdom-seekers are fit to hold power.
---

| Is triggered by: Completion of the Establish a University journal entry |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: Society should be ruled by philosopher-kings. Gains Philosopher-Kings for 5 years +25% University throughput +50% Political strength of Academics Enabled if: Does not have Empiricism researched Modern institutions should employ modern methods. Gains +3.50K progress on technology Empiricism Enabled if: Does not have Medical Degrees researched Formalize the medical profession. Gains +3.50K progress on technology Medical Degrees |

id

#### The Philosophy Department

We have secured funding for philosophy departments in all of our institutions of higher learning. The University of [State] has chosen to focus this funding on advancing Hegelian dialectics.
---

Flavor text:
"Now that we're more of less seated, we can begin. Everything you do at this institution begins and ends with this portmanteau: 'philo', meaning the love of, and 'sophia', meaning wisdom. The love of learning and thought is what Philosophy is. Underpinning Philosophy is the outlook by which we perceive life, the world, everything in essence. We can't necessarily teach you how to do a specific task here. What we can do is teach you how to learn, and how to think about learning on your own."
---

| Is triggered by: Completion of The Philosophy Department journal entry |
|---|
| Trigger conditions: None |
| Option conditions Enabled if: default Thesis, antithesis, synthesis Gains Synthesis! for 5 years +25% University throughput Enabled if: Has researched Labor Movement Has researched Dialectics Does not have Socialism researched Investigate dialectical materialism. Gains 4.15K progress on technology Socialism Enabled if: Has researched Psychiatry Does not have Philosophical Pragmatism researched We need a more pragmatic approach. Gains 4.15K progress on technology Philosophical Pragmatism |

### Infrastructure events

id

#### The Engines of Progress

The manufacture of steam engines has become a profitable industry thanks to our sound investment in locomotive technology. These engines are already being employed across new railway lines.
---

Flavor text:
"All aboard for [City]! Courtesy of the good folks at the [City] Steam Locomotive Company, getting out of [City] has never been easier. The dining cart is restricted to first-class passengers only, stowaways will be prosecuted!"
---

| Is triggered by: Completion of the Steam Engine Time journal entry |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: All aboard! Gains Railway Connections for 5 years +10% Railway throughput Always enabled: More engines! More locomotives! [State] gets Steam Engine Time for 5 years +15% Motor Industries throughput Enabled if: Does not have Steel Railway Cars researched We're on the track for innovation. Gains 4.15K progress on technology Steel Railway Cars |

id

#### Railroad Boom

The growth of branch lines along the main rail routes has been immensely valuable to the growth of our burgeoning rail industry.
---

Flavor text:
"A child has been arrested for picking up coal alongside newly-laid tracks. If the youth had been smart enough to steal the whole railroad, he would've been hailed as the Napoleon of industry."
---

| Is triggered by: Completion of the Branching Out journal entry |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: The railroads of [State] shall prosper. [State] gets Traffic Boom for 5 years +33% Railway throughput Enabled if: Has a Motor Industry The locomotive-builders of [State] should benefit from this boom. [State] gets Locomotive Boom for 5 years +33% Motor Industries throughput Enabled if: Can research Steel Railway Cars Let us not rest on our laurels, but anticipate the future! Gains 4.14K progress on technology Steel Railway Cars |

id

#### A Stable Supply of Power

The recent expansion of the
Power Plant has inspired faith in a future where all of [Country] is electrified.
---

Flavor text:
"Trapping the power of the roaring rivers and waterfalls by transforming it to the power of a thunderstorm must be a sign that we are approaching the final stage of man's mastery of nature. Are we ready? Morally, intellectually, spiritually? It matters not. It is coming."
---

| Is triggered by: Completion of the Expand Power Plants journal entry |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: Unlimited power! [State] gets Power Plant Pioneer for 5 years +33% Power Plant Throughput Enabled if: Does not have Electric Railways researched All technology must be leveraged towards better trains. Gains 6K progress on technology Electric Railways Enabled if: Does not have Steam Turbine researched There must be other ways to produce electricity. Gains 6K progress on technology Steam Turbine Enabled if: Does not have Shift Work researched With the light on around the clock, why should the work ever stop? Gains 6K progress on technology Shift Work |

### Bureaucracy events

id

#### Filing Cabinets

The use of filing cabinets in the
Government Administration has drastically increased the effectiveness of state bureaucracy.
---

Flavor text:
"The future isn't flying like a bird, nor roaring along in a train. No... the future is filing."
---

| Is triggered by: Completion of the Central Archives journal entry |
|---|
| Trigger conditions: None |
| Option conditions Always enabled: I love bureaucracy. Gains Horizontal Filing Cabinets Boost for 5 years +5% Bureaucracy Enabled if: Does not have Identification Documents researched Store information about our citizens. Gains 4.15K progress on technology Identification Documents |

### Art events

id

#### Isn't It Romantic?

The
Arts Academy in [State] has experienced an increasing interest in the Romantic movement, with some of our greatest artists producing genuine masterpieces.
---

Flavor text:
"In Xanadu did Kubla Khan
A stately pleasure-dome decree:
Where Alph, the sacred river, ran
Through caverns measureless to man
Down to a sunless sea."
---

| Is triggered by: Completion of the Patronize Romanticism journal entry |
|---|
| Trigger conditions: None |
| We will show the world how Romanticism is done! [State] gets Romantic Architecture for 5 years +20% Arts Academy throughput But could you make it a bit more... realistic? Gains 3.50K progress on technology Realism |

id

#### The Realist Movement

The
Arts Academy of [State] has become a major center of the Realist movement, producing some of the finest works of our generation.
---

Flavor text:
Realism depicts the world as it is, warts and all, rather than the world as we might like it to be. It seeks not only to be true to how objects appear to the eye, but also to be true to the everyday experiences of ordinary people.
---

| Is triggered by: Completion of the Patronize Realist Art journal entry |
|---|
| Trigger conditions: None |
| Finally, art we can all relate to. Gains Supporting the Realist Movement for 5 years +15% Arts Academy Throughput Can we capture reality even more perfectly? Gains 4.15K progress on technology Camera The world is grim and mundane. Gains Grim Realism for 5 years +15 Political strength of Capitalists |

### Military events

id

#### Industrial Boom

With the recent expansion in both the production and consumption of explosives in our country, there has been much debate on whether the Military or the Industrial Sector should have priority.
---

Flavor text:
"Why should we worry about how much dirt we can move when we should be thinking about how to defend our country?"
"All you care about is starting more wars, we should put this to use for our workers instead. They are more important."
---

| Is triggered by: Completion of the Booming Industries journal entry |
|---|
| Trigger conditions: None |
| Increased supply will lift all boats. Gains Explosives Production for 5 years +33% Fertilizer Plants throughput The industrial sector will make best use of it. Gains Mining Production for 5 years +20% Coal Mine throughput +20% Iron Mine throughput +20% Lead Mine throughput +20% Sulfur Mine throughput The military must have their cut. Gains Ammunition Production for 5 years +33% Munition Plants throughput |

id

#### Dealing in Arms

The establishment of
Munition Plants in [State] ensures an abundant supply of
Ammunition for [Country].
---

Flavor text:
"I resent the term 'arms dealer'. It implies that I am no more than a cynical profiteer, benefiting from the suffering of my fellow man. Nothing could be farther from the truth; what I do guarantees peace and security, not only in [Country] but throughout the civilized world."
---

| Is triggered by: Completion of The Munition Industry journal entry |
|---|
| Trigger conditions: None |
| If you want peace, prepare for war. [State] gets Munitions Mania for 5 years +15% Munition Plants throughput Let's see some rapid-fire gains in research. Gains 3.50K progress on technology Rifling |

id

#### Modernizing the Arsenal

The change in large-scale production from smoothbore muskets to rifles in the
Arms Industry in [State] has ushered in a new era for
Small Arms production in [Country].
---

Flavor text:
"Even from one thousand yards you can still take the shot.
Forward artillery positions can be harassed, bayonet charges stopped before they have even commenced.
The advantages are innumerable!
Unless we develop sufficient manufacturing capabilities to produce these weapons, we are bound to face disaster on the battlefield."
---

| Is triggered by: Completion of the Rifling journal entry |
|---|
| Trigger conditions: None |
| The [City] Arsenal shall be famed throughout the world. [State] gets Modern Rifle Arsenal for 10 years +20% Migration Attraction +20% Arms Industries throughput +20% Artillery Foundry throughput [Country] shall be at the forefront of military innovation. Gains 4.15K progress on technology Repeaters [State] gets Arsenal Proving Ground for 10 years +10% Migration Attraction +5% Arms Industries throughput +5% Artillery Foundry throughput |

id

#### A Doctrine of Iron and Steam

The introduction of vessels with metal-skinned hulls represents nothing less than a revolution in naval warfare. Near-impervious to traditional types of shot, Admiral [Admiral] assures us that [Country] dominion of the seas will be absolute.
---

Flavor text:
"While wooden ships with iron men might beat iron ships with wooden men, it sure does not hurt to have the armor on our side."
---

| Is triggered by: Completion Event of the Monitors journal entry |
|---|
| Trigger conditions: None |
| This will make our line of battle invincible. Gains Armored Line of Battle for 10 years +10% Navy Defense Metal bows? Metal Rams! What could go wrong? Gains Ram Craze for 10 years +20% Navy Offense −10% Navy Defense [Country] rules the waves! Gains Armored High Seas Fleet for 10 years +10% Prestige from Navy Power Projection |

id

#### The Shallow Draft Solution

Designed for coastal defense operations, what monitors lack in oceangoing capabilities they make up for in cost effectiveness. Admiral [Admiral] has informed the Admiralty in [City] that his fleet will keep any foes away from [Country] waters.
---

Flavor text:
"Sir, while it might indeed look like a "cheesebox on a raft", I assure you that the 15-inch guns she carries in that box of hers are no laughing matter."
---

| Is triggered by: Completion Event of the Monitors journal entry |
|---|
| Trigger conditions: None |
| Secure shores means secure commerce. Gains Safer Shores for 10 years +10% Trade Center throughput Let us orient our naval doctrine around them. Gains Defensive Naval Doctrine for 10 years +10% Navy Defense We don't win by having the best ships, we win by having the most. Gains Quantity Over Quality for 10 years −10% Navy Offense −10% Navy Defense +10% Shipyards throughput |

### War Wounded events

id

#### Medical Cleanliness

It has been suggested by some of the nurses working on the frontlines of the [War], that by adopting new cleanliness procedures we could reduce the number of deaths.
---

Flavor text:
"Keep the ward clean, keep your hands clean and most of all keep the wounds clean. Do even one of these and the results are frankly astounding."
---

| Is triggered by: Pulse Event from the War Wounded journal entry |
|---|
| Trigger conditions: Is at War Number of Dead is greater than 1000 Any deployed Formation: Has activated the First Aid or Field Hospitals Mobilization Option Is in an owned State |
| What an excellent idea. [State] gets Medical Hygiene Standards for 1 years +20% Recovery Rate This knowledge must be spread. Gains Medical Hygiene Standards for 1 years +10% Recovery Rate |

## References
