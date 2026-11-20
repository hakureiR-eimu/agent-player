---
title: Journal
source: https://vic3.paradoxwikis.com/Journal
pageid: 3220
categories: [Timeless, To_be_split, Scripted_content, Articles_with_potentially_outdated_infoboxes, Game_concepts, Journal]
fetched: 2026-10-27
---
This article is [timeless](https://vic3.paradoxwikis.com/Category:Timeless) and should be accurate for any version of the game.

|  | **This article is a candidate for splitting into multiple pages.** Please help to improve the wiki by taking part in the [discussion](https://vic3.paradoxwikis.com/Talk:Journal) of the proposed splitting. |
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
The **journal** tracks ongoing events in a country and is used to simulate various historical events, real or counter-factual. A **journal entry** has a set of visibility conditions, a set of activation conditions and a set of completion conditions.

The effects of a journal entry are in place either during activation or at completion. Many journal entries provide bonuses upon completion and each has certain conditions for activation and then successful completion or failure. Some entries are time limited while others remain open until they are completed.

Most journal entries are available to all countries meeting the conditions. Country-specific journal entries can be found on those country's pages or related content pages.

## By country

See also:
Countries
Country-specific journal entries can be found on the relevant country page or on the **country content pages** in the navbox at the top of the page.

- [Afghanistan Content](Afghanistan.md)
- [American Content](American content.md)
- [Austrian Content](Austrian content.md)
- [Balkan Content](Balkan content.md)
- [Bolivian Content](Bolivia.md)
- [Brazilian Content](Brazilian content.md)
- [British Content](British content.md)
- [Bulgarian Content](Bulgaria.md)
- [Chinese Content](Chinese content.md)
- [Colonial Indies Content](Colonial Indies content.md)
- [Ethiopian Content](Ethiopia.md)
- [French Content](French content.md)
- [German Content](German content.md)
- [Greek Content](Greek content.md)
- [Hawaiian Content](Hawaii.md)
- [Hungarian Content](Hungary.md)
- [Italian Content](Italy.md)
- [Japanese Content](Japanese content.md)
- [Korean Content](Korean content.md)
- [Montenegrin Content](Montenegrin content.md)
- [Mughal Content](Hindustan.md)
- [Omani Content](Oman.md)
- [Peru-Bolivian Content](Peru-Bolivia.md)
- [Poland Content](Poland.md)
- [Punjabi Content](Punjab.md)
- [Romanian Content](Romania.md)
- [Russian Content](Russian content.md)
- Serbian Content
- [South America Content](South America content.md)
- [Turkish Content](Turkish content.md)

## By theme

Pages for journal entries that related to a certain theme or game mechanic can be found in **general content pages** in the navbox at the top of the page.

## Major situations

id

### Government Petition

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.5. |
|---|---|

---

As a loyal component of the [Ruler Title]'s government, the [Interest Group] are petitioning for [Law] to pass.
If [Law] is successfully passed, the [Interest Group] will be greatly pleased, but if this petition is ignored, the nation will face penalties, up to the [Interest Group]'s resignation from government.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activation conditions: Not all of these: Is not enacting any law Any Interest Group: Is in Government Stance on any available law is greater than current None of these: Is in a Revolution Is facing a Secession Triggers through the 'government_petition_events.100' invisible Yearly Pulse Event | Effects when activated: Triggers the Event [Interest Group] Petition Government |
| Completion conditions: Has enacted [Law] | Effects when completed: 5% of [Interest Group] members become more Loyalist Gets Responsive Governance (Decaying) for 10 years +10 Legitimacy |
| Failure conditions: [Interest Group] are not part of the government | Effects when failed: [Interest Group] gets Failed Petition (Decaying) for 10 years −20 Interest Group Approval |
| Times out after 5 years (60 months) with the following effects: [Interest Group] gets Failed Petition (Decaying) for 10 years −15 Interest Group Approval |  |

id

### The Great Hunger

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.5. |
|---|---|

---

A great crop failure has brought immeasurable suffering to our people, who beg for our government to take special measures in this matter.
---

| Visibility conditions: Is not a Decentralized Nation |  |
|---|---|
| Activation conditions: Investment level for Social Security is less than 4 . At least one of these: Any Incorporated State Average Standard of Living is less than 10 Has suffered a Natural Disaster Any State Average Standard of Living is less than, or equal to 5 Any Building: Is any of: Rye Farm Wheat Farm Rice Farm Maize Farm Millet Farm Livestock Ranches The Workforce Occupancy is greater than, or equal to 10% Weekly Profit is less than, or equal to 0.50 | Effects when activated: Triggers the event The Hard Times |
| Completion conditions: Wait for the famine to expire or raise the Standard of Living in your nation by 3 points. | Effects when completed: Removes Great Famine +50% mortality |
| Times out after 5 years (60 months) with the following effects: None |  |
| Every month, the following random events can happen: (weight:100) Nothing happens (weight:10) Bread and Blood (weight:10) In Search of a Better Life (weight:10) events#famine_events.4 (weight:10) events#famine_political.1 (weight:10) events#famine_political.2 (weight:10) events#famine_political.3 (weight:10) events#famine_political.4 (weight:10) events#famine_political.5 |  |

id

### Springtime of the Peoples

Discontent with the post-Napoleonic reactionary order has exploded into a tidal wave of radical sentiment across
Europe
. Liberal revolutionaries hoist tricolor flags, and cry out for liberty, equality, and fraternity.
To the Barricades!:
If a Liberal or Socialist Political Movement becomes Insurrectionary in our Capital whilst this Journal Entry is active, revolutionary forces may attempt to seize power over our country.
---

| Visibility conditions: Has researched Egalitarianism [Capital] is in Europe, meaning: Strategic region is any of: Western Europe Southern Europe Central Europe Northern Europe Balkans Russia Eastern Europe |  |
|---|---|
| Activation conditions: Any country has experienced either the Liberal or the Radical movement being revolutionary, or France has proclaimed the Second Republic At least 5% of pops are radical | Effects when activated: Triggers the Event The Rise of Radicalism Creates a German National Movement if the country is German, an Italian National Movement if the country is Italian, and a Radical movement if the country is neither Creates a Liberal Movement |
| Entry modifiers: Springtime of the Peoples Springtime of the Peoples Country modifier +50% Enactment Speed +500% Political Movement Activism Growth +35% Political Movement Activism +25% Cultural Minority Movement Pop Attraction +25% German National Movement Pop Attraction +25% Italian National Movement Pop Attraction +25% Liberal Movement Pop Attraction +25% Radical Movement Pop Attraction +25% German National Movement Pop Attraction |  |
| Completion conditions: Either: Has been forced to enact a democratic constitution by a radicalized movement Any government interest group has a Liberal or Radical leader Country has Census Suffrage or Universal Suffrage | Effects when completed: Triggers the event The Revolution Victorious |
| Failure conditions: The Radical, German National, Italian Nationa, or Yugoslav National movement has been having less than 10% support while being suppressed for at least the past year No agitators nor non-marginalized IG leaders have the Radical ideology. | Effects when failed: Triggers the event The Revolution Vanquished |

id

### The Red Scare

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.5. |
|---|---|

---

The emergence of a powerful communist regime in a foreign country has aroused fear amongst certain segments of the population that [Country] will be next to fall to communism.
Domestic political currents with left-wing agendas have fallen under the scrutiny of anti-communist forces, as they are accused of being harbingers of bloody revolution, and agents of foreign powers.
---

| Visibility conditions: Any Country above Minor Power that we have an Interest in has researched Labor Movement |  |
|---|---|
| Activation conditions: Any Country above Minor Power that we have an Interest in has enacted the Council Republic Law Does not have Council Republic enacted | Effects when activated: Triggers the Event The Red Scare |
| Failure conditions: At least one of these: Has enacted Council Republic Any revolution progress is greater than 75% |  |
| Invalidation conditions: No Country above Minor Power that we have an Interest in has enacted the Council Republic Law |  |
| Times out after 10 years (120 months) with the following effects: Triggers the Event A Subtler Terror |  |
| Every month, the following random events can happen: (weight:300) Nothing happens (weight:10): The Nationalization of Women (weight:10): Communism Criminality (weight:10): events#red_scare.4 (weight:10): events#red_scare.5 (weight:10): events#red_scare.6 (weight:10): events#red_scare.7 (weight:10): Marching Against Peace (weight:10): In the Face of Revolution (weight:10): The White Émigrés (weight:10): Progressive Dilemmas (weight:10): events#red_scare.12 (weight:10): The Communist Ark (weight:10): events#red_scare.15 |  |

## Domestic affairs

id

### From Farms to Factories

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.5. |
|---|---|

---

A nation of peasants is a nation of the past. How can we expect progress to arrive in our homes if those homes are no more than farms?
---

| Visibility conditions: Peasants is more than 60% of total population |  |
|---|---|
| Activation conditions: Does not have Serfdom enacted Does not have Land-Based Taxation enacted | Effects when activated: None |
| Completion conditions: Peasants is less than 35% of total population Does not have Serfdom enacted Does not have Land-Based Taxation enacted Industrialists are not Marginalized | Effects when completed: Triggers the Event Road to Progress |

id

### Urbanize

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.5. |
|---|---|

---

The future is not white or black, like the old tales say - it's gray! The color of the train that lets us visit foreign lands! The color of the factory that lets us pay for such travel! The color, my friend, of
---

| Visibility conditions: Any Incorporated State has an Urban Center |  |
|---|---|
| Activation conditions: Any Incorporated State has a level 5 or more Urban Center Does not have Agrarianism enacted | Effects when activated: None |
| Completion conditions: At least 75% of all Incorporated States have a level 5 or more Urban Center Any Incorporated State has a level 10 or more Urban Center | Effects when completed: Triggers the event Winds of Change |

## Development

### Art

id

#### Patronize Romanticism

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

The Romantic artistic movement advocates for the glorious past: knights, castles, pirates, forbidden nature and lost heroes. Its appealing nature must be swiftly spread.
---

| Visibility conditions: Has researched Rationalism Is not Unrecognized |  |
|---|---|
| Activation conditions: Has researched Romanticism Does not have Realism researched Has an Urban Center |  |
| Completion conditions: Any level 2 or higher Arts Academy Has activated Traditional Art Production Method The workforce Occupancy is at least 90% | Effects when completed: Triggers the Event Isn't It Romantic? |
| Failure conditions: Has researched Realism |  |
| Times out after 10 years (120 months) with the following effects: None |  |

id

#### Patronize Realist Art

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.5. |
|---|---|

---

Artists are moving away from abstract, fantastical art and towards realistic portrayals of a concrete subject matter. As patrons of this movement there could be much to gain.
---

| Visibility conditions: Has researched Romanticism Does not have Camera researched Is not Unrecognized |  |
|---|---|
| Activation conditions: Has researched Realism Has an Arts Academy |  |
| Completion conditions: All Arts Academy: The workforce Occupancy is at least 90% Has activated Realist Art | Effects when completed: Triggers the Event The Realist Movement |
| Times out after 10 years (120 months) with the following effects: None |  |

id

#### Establish the Photographic Arts

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.9. |
|---|---|

---

| Visibility conditions: Has researched Realism Does not have Film researched Is not Unrecognized |
|---|
| Activation conditions: Has researched Camera Has a level 3 or higher Arts Academy |

## Unique buildings

Main article:
Unique buildings
Canals and skyscrapers each have special journal entries related to their construction. Certain monuments also have related journal entries.

## Expeditions

Main article:
Expeditions
Expeditions represent historical European endeavors to explore various parts of the world, namely the American northwest, Africa's major rivers, and Antarctica, as well as the British expedition to Tibet.

## References

Journal entry files can be found in /Victoria 3/game/common/journal_entries

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | [Government](Government.md) • [Capacities](Capacity.md) • [Characters](Character.md) • [Decrees](Decrees.md) • [Institutions](Institutions.md) • [Laws](Laws.md) • [Technology](Technology.md) |
|---|---|

| Politics | [Elections](Elections.md) • [Ideology](Ideology.md) • [Interest group](Interest group.md) • [Political lobby](Political lobby.md) • [Political movement](Political movement.md) • [Political party](Political party.md) • [Revolution](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| Economy | [Buildings](Building.md) • [Goods](Goods.md) • [Harvest condition](Harvest condition.md) • [Infrastructure](Infrastructure.md) • [Market](Market.md) • [Production methods](https://vic3.paradoxwikis.com/Production_methods) • [State](State.md) • [Treasury](Treasury.md) |
|---|---|

| Diplomacy | [Diplomacy](Diplomacy.md) • [Diplomatic action](https://vic3.paradoxwikis.com/Diplomatic_action) • [Diplomatic play](Diplomatic play.md) • [Power bloc](Power bloc.md) • [Ranks](Rank.md) • [Subjects](Subject.md) • [Treaties](Treaty.md) |
|---|---|

| Warfare | [Warfare](Warfare overview.md) • [Land warfare](Land warfare.md) • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • Journal • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
