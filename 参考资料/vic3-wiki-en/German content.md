---
title: German content
source: https://vic3.paradoxwikis.com/German_content
pageid: 8604
categories: [1.13, Scripted_content, Pages_with_obsolete_template_parameters, Articles_with_potentially_outdated_infoboxes, Journal, Events]
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
German countries have access to the following [journal entries](https://vic3.paradoxwikis.com/Journal_entries) and [events](Events.md).

## Schleswig-Holstein Question

This journal entry represents the issue of Danish control over Schleswig and Holstein

id

### The Schleswig-Holstein Question

The Schleswig-Holstein Question is currently occupying the thoughts and energies of the German nationalists. In order for Germany to progress towards national unification, the German people of Holstein must first be liberated from their Danish overlords.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activation conditions: Primary culture is North German or South German No country has completed this journal entry |  |
| Completion conditions: For Holstein or Schleswig , Is not a subject For Lübeck , Fully owns Schleswig-Holstein For all others, if Denmark exists, Owns part of Schleswig-Holstein No part of Schleswig-Holstein is owned by a country that either: Is a subject of Denmark Does not have North German or South German primary culture | Effects when completed: Gain Resolved the Schleswig-Holstein Question Resolved the Schleswig-Holstein Question Country modifier +25% Prestige for 10 years |
| Failure conditions: Another country has completed this journal entry |  |

## German National Identity

These journals represent the rising national consciousness of the German people.

id

### German National Identity

The ideas of nationalism are spreading like wildfire among the German people. Once these ideals have reached a critical mass of followers in the disparate states of the German Confederation, there is bound to be a push for national unification.
---

| Visibility conditions: Primary culture is North German or South German |  |
|---|---|
| Activation conditions: Any country has completed the journal entry The Schleswig-Holstein Question |  |
| Completion conditions: 75% of countries with North German or South German primary culture have researched Nationalism | Effects when completed: Trigger event: German National Identity |

id

### German National Identity

![Event trigger.png](https://central.paradoxwikis.com/images/3/35/Event_trigger.png) **The below description is one of several available for this event.**

The ideals of Nationalism and National Unification have gained many supporters throughout the German Confederation. They look to the more powerful German powers such as ourselves in the hope that we will champion the cause of German unity on the greater European stage.
---

Flavor text:
"The German Confederation? The Confederation is a joke, a relic of a bygone era, a foreign imposition! For the German people to prosper and assume our rightful place in Europe, we must have a true German Nation!"
---

| Is triggered by: Journal entry German National Identity completion |
|---|
| Trigger conditions: None |
| Momentous times are ahead of us. If North German, activate North German Confederation journal entry If South German, activate South German Federation journal entry |

id

### North German Confederation

The age of nationalism is upon us, and the German people seek unification. We must strive to be the foremost power in northern Germany, so that the people look to us as champions of the cause.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event German National Identity | Effects when activated: None |
| Completion conditions: Has researched Nationalism Is a unification candidate for Germany No other country is a unification candidate for Germany | Effects when completed: Triggers event: German Leadership |
| On Monthly Trigger event The Iron Chancellor |  |

id

### South German Federation

The age of nationalism is upon us, and the German people seek unification. We must strive to be the foremost power in southern Germany, so that the people look to us as champions of the cause.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event German National Identity | Effects when activated: None |
| Completion conditions: Has researched Nationalism Is a unification candidate for Germany No other country is a unification candidate for Germany | Effects when completed: Triggers event: German Leadership |

id

### German Leadership

With [Country] now seen as the sole realistic option for German Unification, many North/South German states have opted to join our banner. Hopes are high that this will soon lead to a federation of all the Germanies.
---

Flavor text:
From the scattered fiefdoms of the Holy Roman Empire to the chaos of Napoleon's wake, Germany has never truly been united. What the [country adjective] state has achieved today is a step towards the impossible and the inevitable.
---

| Is triggered by: Completion of journal entry: South German Federation or North German Confederation |
|---|
| Trigger conditions: None |
| Immediate effects: Set journal entry German Unification as visible for this country All countries with same primary culture below great power rank: If AI and either supporting this country as unification candidate for Germany or in its customs union Annexed by this country Otherwise receive event: Confederation with [German unifier] |
| The statesmen responsible are national heroes. The leader of each IG in government gains German Unifier German Unifier Character modifier +50 Popularity for 10 years The world will know of our achievement. Gain German Unifier German Unifier Country modifier +5% Prestige +10% Influence for 5 years For both options, if the country is Kingdom or Principality Tier: If North German primary culture, become North German Federation If South German primary culture, become South German Federation |

id

### Confederation with [German unifier]

With [German unifier] now seen as the sole realistic option for German Unification, many minor German states have opted to join their banner. Should we give up our independence for the sake of greater German unity?
---

Flavor text:
"By joining this confederation with [German unifier], we may be surrendering [country adjective] sovereignty, but by doing so, we help to secure German sovereignty. The spirit of the times is undeniable; the German people desire unity, and the [German Unifier adjective] seems set to be the ones to make it happen. To oppose the coming together of the German people would be utter folly."
---

| Is triggered by: Event German Leadership |
|---|
| Trigger conditions: None |
| Option conditions Enabled if: Independent or a subject of [German unifier] For Germany! [German unifier] annexes this country Always enabled: Our sovereignty is inviolable. 5% of North German and South German pops become more radical Lose −50 relations with [German unifier] [German unifier] gains claims on all owned states |

id

### The Iron Chancellor

A nobleman named Otto von Bismarck has risen to a prominent position among the [country adjective] Junkers. Advocating for German national unity and political pragmatism, he offers his services to the state.
---

Flavor text:
"I shall soon be compelled to undertake the conduct of the [country adjective] Government. My first care will be to reorganize the army, with or without the help of the Landtag. As soon as the army shall have been brought into such a condition as to inspire respect, I shall seize the first best pretext to declare war against Austria, dissolve the German Diet, subdue the minor States, and give national unity to Germany under [country adjective] leadership."
---

| Is triggered by: Journal entry pulse North German Confederation |
|---|
| Trigger conditions: No country has received this event Landowners are powerful and in government Is a unification candidate for Germany Has researched Nationalism Date is between 1846 and 1898 |
| Immediate effects: Create the character Otto von Bismarck leading the Landowners |
| Appoint Bismarck as Chancellor. Otto von Bismarck gains Bismarck Favored Bismarck Favored Character modifier +75 Popularity Gain Triumph of Realpolitik Triumph of Realpolitik Country modifier +20% Infamy decay for five years Realpolitik is not the right policy. Otto von Bismarck gains Bismarck Disfavored Bismarck Disfavored Character modifier −50 Popularity Gain Realpolitik Condemned Realpolitik Condemned Country modifier +50% Damage relations speed for five years |

## German Unification

id

### German Unification

The time has come to make a decisive push for German unification. As one of the foremost German states, it is our duty to bring about this goal.
---

| Visibility conditions: Completed either North German Confederation or South German Federation journal entry |  |
|---|---|
| Activation conditions: Is at least a major power Has researched Pan-nationalism Is independent | Effects when activated: None |
| Completion conditions: Is Germany | Effects when completed: None |
| Invalidation conditions: Has the Dual Monarchy government type | Effects when invalid: None |

## The Seventy Million Reich

This event fires when [Germany](Germany.md) is formed while incorporating the entire former Austrian Empire, addressing the question of non-German populations in a Greater Germany.

id

### The Seventy Million Reich

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version Prussian content . |
|---|---|

---

The below description is one of several available for this event.
The incorporation of the entire former Austrian Empire into [Country] has caused great alarm amongst North German nationalists. Many demand that these territories be granted independence, lest Germans become a minority in their own state.
---

Flavor text:
"You must understand", said the Prussian delegate, "that the people fear. They fear that the some forty millions of former Austria will dilute the character of our nation, and they fear that their inclusion will render Germany nothing more than a greater Austria."
The Austrian shook his head. "They are good Catholic subjects, docile unless stirred by foreign agitation. I assure you that these fears are entirely unfounded."
"That is the trouble, no? This is not the Catholic Empire."
---

| Is triggered by: Formation of Germany while incorporating Austrian territories |
|---|
| Trigger conditions: Any of: Owns any North Italian homeland except for Istria and South Tyrol Owns any Hungarian homeland Owns any Romanian homeland Owns any Croatian homeland except for Istria |
| Grant the non-German regions independence. Non-German nations are released as independent states Every great power loses −10 relations with Germany Release the non-German regions as dependencies. Non-German nations are released as puppets Every great power loses −20 relations with Germany Creates a diplomatic incident for 40 infamy Stay the course of the Seventy Million Plan. If has Subjecthood: 20% of North German pops and 5% of South German pops become more radical If does not have Subjecthood: 20% of non-Germanophone pops over 2% of population become more radical Every great power loses −30 relations with Germany Creates a large diplomatic incident for 70 infamy |

## Gründerzeit

|  | Available only with the [National Awakening](National Awakening.md) DLC enabled. |
|---|---|

This journal entry represents the period of rapid industrial expansion in the German lands during the mid-to-late 19th century. It is a shared journal entry that affects all members of the German Confederation.

id

### Gründerzeit

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version Prussian content . |
|---|---|

---

|  | Available only with the [National Awakening](National Awakening.md) DLC enabled. |
|---|---|

---

Spurred on by innovations in financial law and the proliferation of the railway, the German lands are abuzz with activity, with new companies and business ventures springing up like toadstools. To maintain investor confidence, the combined GDP of all German countries must grow by 2% per quarter.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: 75% or more of all German countries in Europe have researched Mutual Funds and have at least one level of Railway | Effects when activated: None |
| Entry modifiers: Tempo of the Founding Years Tempo of the Founding Years Country modifier −20% Political movement pop attraction −10% Loan interest rate +20% Capitalists investment pool efficiency +20% Shopkeepers investment pool efficiency |  |
| Completion conditions: (This journal entry does not have a completion condition; it times out after 30 years) | Effects when completed: None |
| Failure conditions: The Progress Bar has reached 0 | Effects when failed: Triggers event Gründerkrach for all involved countries |
| Times out after 30 years with the following effects: Triggers event Thirty Years of Progress for all involved countries |  |
| Every 3 months: If the combined GDP of all German countries has grown by 2% since last quarter: progress bar increases by 1 (max 4 ) If the combined GDP has not met the target: progress bar decreases by 1 |  |

id

### The Age of Entrepreneurs

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version Prussian content . |
|---|---|

---

|  | Available only with the [Sphere of Influence](Sphere of Influence.md) DLC enabled. |
|---|---|

---

Spurred on by innovations in financial law and the proliferation of the railway, the German lands are abuzz with activity, with new companies and business ventures springing up like toadstools.
---

Flavor text:
The foreman cracks his whip again, driving the exhausted team of horses forward. They had made decent progress today—most of the sand had been carried off the site. But decent is not good. And even good is hardly sufficient. The whip cracks out again. The foreman feels a pang of guilt for the poor creatures, but quickly pushes the thought away. Mercy will not transform this site into a new factory. Determination will.
---

| Is triggered by: Activation of Gründerzeit journal entry |
|---|
| Trigger conditions: None |
| Buy! Invest! Expand! The Gründerzeit journal entry bonuses will be stronger, but so too will any subsequent crash Full Tempo of the Founding Years Tempo of the Founding Years Country modifier −10% Loan interest rate −20% Political Movement Pop Attraction +20% Capitalists Investment Pool contribution efficiency +20% Shopkeepers Investment Pool contribution efficiency modifier is applied Let us not get too carried away. The Gründerzeit journal entry bonuses will be weaker, but so too will any subsequent crash Half-strength Tempo of the Founding Years Tempo of the Founding Years Country modifier −10% Loan interest rate −20% Political Movement Pop Attraction +20% Capitalists Investment Pool contribution efficiency +20% Shopkeepers Investment Pool contribution efficiency modifier is applied (all effects halved) |

id

### Gründerkrach

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version Prussian content . |
|---|---|

---

|  | Available only with the [Sphere of Influence](Sphere of Influence.md) DLC enabled. |
|---|---|

---

Years of optimism and financial growth have come to a screeching halt, with blood-red numbers reported across German stock exchanges as banks and speculative companies collapse like dominos.
---

Flavor text:
Bank Run in [Capital]! The announcement of the liquidation of a series of prominent companies triggered an avalanche, sweeping away not only small investors but also well-known financiers. All day, telegram couriers have been frantically dashing through crowds, and merchants were seen burning their worthless stock certificates.
---

| Is triggered by: Failure of the Gründerzeit journal entry (progress bar reaches 0) |
|---|
| Trigger conditions: None |
| Speculators and rampant economic liberalism is to blame. Lose Tempo of the Founding Years Tempo of the Founding Years Country modifier −10% Loan interest rate −20% Political Movement Pop Attraction +20% Capitalists Investment Pool contribution efficiency +20% Shopkeepers Investment Pool contribution efficiency If high commitment: Gain Gründerkrise Gründerkrise Country modifier +20% Political movement pop attraction −20% Capitalists investment pool efficiency −20% Shopkeepers investment pool efficiency for 5 years, plus small radicals If low commitment: Gain Gründerkrise at half strength for 5 years Every interest group approving Free Trade gains Free Trade Discredited Free Trade Discredited Interest Group modifier −2 Approval −10% Political strength for 5 years (halved if low commitment) This is the work of predatory agents in our midst. Lose Tempo of the Founding Years Tempo of the Founding Years Country modifier −10% Loan interest rate −20% Political Movement Pop Attraction +20% Capitalists Investment Pool contribution efficiency +20% Shopkeepers Investment Pool contribution efficiency If high commitment: Gain Gründerkrise for 5 years, plus small radicals If low commitment: Gain Gründerkrise at half strength for 5 years Gain Financial Conspiracy Theories Financial Conspiracy Theories Country modifier +5% Radicalism increases for violently hostile pops +5% Radicalism increases for cultural erasure pops +5% Radicalism increases for open prejudice pops for 5 years (halved if low commitment) Every interest group approving Ethnostate gains Proliferation of Antisemitic Literature Proliferation of Antisemitic Literature Interest Group modifier +5% Pop attraction for 5 years (halved if low commitment) |

id

### Thirty Years of Progress

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version Prussian content . |
|---|---|

---

|  | Available only with the [Sphere of Influence](Sphere of Influence.md) DLC enabled. |
|---|---|

---

Following decades of economic prosperity, the intense drive and activity that defined them has now somewhat abated. These years will go down in [Adjective] history as some of her most glorious.
---

Flavor text:
"And they called it a bubble, pah! A bubble!? Only a fool would invest their spouse's inheritance in something like that, and I will tell you one thing, liebchen!, I am no fool."
---

| Is triggered by: Timeout of the Gründerzeit journal entry (30 years pass without crashing) |
|---|
| Trigger conditions: None |
| Three cheers to man's indomitable entrepreneurial spirit! Lose Tempo of the Founding Years Tempo of the Founding Years Country modifier −10% Loan interest rate −20% Political Movement Pop Attraction +20% Capitalists Investment Pool contribution efficiency +20% Shopkeepers Investment Pool contribution efficiency If high commitment: Gain Spirit of the Glorious Thirty Spirit of the Glorious Thirty Country modifier +10% Capitalists investment pool efficiency +10% Shopkeepers investment pool efficiency for 5 years If low commitment: Gain Spirit of the Glorious Thirty at half strength for 5 years May these decades merely be the first of many. Lose Tempo of the Founding Years Tempo of the Founding Years Country modifier −10% Loan interest rate −20% Political Movement Pop Attraction +20% Capitalists Investment Pool contribution efficiency +20% Shopkeepers Investment Pool contribution efficiency If high commitment: Gain Glamour of the Glorious Thirty Glamour of the Glorious Thirty Country modifier +5% Prestige for 5 years If low commitment: Gain Glamour of the Glorious Thirty at half strength for 5 years |

## References

Primary reference files:

- /Victoria 3/game/common/journal_entries/00_german_unification.txt
- /Victoria 3/game/common/journal_entries/05_grunderzeit.txt
- /Victoria 3/game/events/german_unification.txt
