---
title: Treaty
source: https://vic3.paradoxwikis.com/Treaty
pageid: 8102
categories: [1.13, Diplomacy]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

Diplomacy
Diplomatic actions
Diplomatic plays
Power blocs
Subjects
Treaties
**Diplomatic treaties** are bilateral agreements between two countries. They contain one or more articles – commitments from either party – which are binding for a specified period of time. Parties to a treaty can also renegotiate or withdraw from it after it is initially ratified. When an offer is received, it is possible to send a counter-offer. When signed, it will be agreed how long the treaty is binding for.

The possible options are 5, 10, 15, 25 or 99 years. It is possible to withdraw from a treaty, before the binding period has expired, but doing so incur [infamy](https://vic3.paradoxwikis.com/Infamy), loss of [relations](https://vic3.paradoxwikis.com/Relations) and establish a [truce](https://vic3.paradoxwikis.com/Truce) between the two countries. Once the binding period has run out, either party can withdraw freely. If neither party chooses to do so, the agreement will continue until one part does. Alternatively, a treaty can be enforced by the *enforce treaty* [war goal](https://vic3.paradoxwikis.com/War_goal).

When a treaty is signed, a party can propose to change the content, which if the other party agrees to it, then takes effect instead. If the other party declines the renegotiated treaty, the existing treaty will continue uninterrupted. When a renegotiated treaty is signed, a new binding period will be agreed upon, which takes precedence. This can potentially also lower the binding period of an existing treaty.

[Obligations](https://vic3.paradoxwikis.com/Obligations) can be used to sway the other side or be demanded for signing a treaty.

## Articles

**Articles** are the core part of treaties that define what they actually do. Articles have a few different classifications. On a fundamental level, articles can be either *mutual* or *directional*. This indicates whether the article is something that affects both sides equally or not. An example mutual article is an *alliance*: both sides are involved equally. On the other hand, *transfer goods* is a directional article: one side (the source) is sending the goods and the other (the target) is receiving them. Directional articles can be proposed by either party, specifying either themself or the other country as the source or target of the article.

Most articles have an influence cost for one or both of the parties.

Some articles have required inputs and others do not. *Transfer goods* requires specifiying the actual transferred goods as well as the amount transferred.

## Non-fulfillment

When a treaty is broken, one of two things happens depending on what articles are not being fulfilled: if it is a serious breach, like not answering the call of an alliance, that breaks the whole treaty and the party at fault receives all the penalties tied to an early withdrawal – if the treaty is binding.

For less serious breaches, the other side of the treaty is inactive until the breach is addressed, at which point the treaty resumes as usual.

## AI acceptance

Each proposed article has an acceptance score, depending on if the AI Country actually wants said article or not. The exact same article can, depending on circumstances, result in both a positive or negative acceptance score. If the total acceptance score of the entire treaty is above **+30**, the AI always accepts the treaty. If it is at 0 or below, the AI always declines. If the acceptance score is between 0 and **29**, acceptance is chance based.

Offering or calling in an obligation increases the acceptance by **+30**. Demanding an obligation reduces the acceptance by **−40**.

## List of articles

### Mutual articles

| Name | Requirements | Effect | Upkeep | Relations | Max involvement |
|---|---|---|---|---|---|
| Alliance | Mutually exclusive with Defensive Pact and Guarantee Independence International Relations Relations are at least amicable Highest overlapping interests tier is not less than influential Does not have a subject relationship with each other Neither of the two countries is a subject without diplomatic autonomy Must have Multilateral Alliances to sign more than one per country None of the two countries is Support Independence of a subject of either country | [First country] forms an alliance with [second country] Establishes an alliance between two countries Both countries may march their armies through the territory of their ally | 150 | **+1** every 66 days up to **80** | 3000 |
| Defensive Pact | Mutually exclusive with Alliance and Guarantee Independence International Relations Relations are at least cordial Highest overlapping interests tier is not less than engaged Does not have a subject relationship with each other Neither of the two countries is a subject without diplomatic autonomy | [First country] enters into a defensive pact with [second country] Establishes a defensive pact between two countries | 100 | **+1** every 100 days up to **80** | 2000 |

### Directional articles

Directional articles have a source, the country "giving" the article's effects, and often a target, the country "receiving" the article's effects.

| Name | Requirements | Effect | Input type | Upkeep | Relations | Max involvement |  |  |
|---|---|---|---|---|---|---|---|---|
| Source | Target | Source | Target |  |  |  |  |  |
| Guarantee Independence | Mutually exclusive with Alliance and Defensive Pact International Relations Source rank is higher than target rank Relations are above poor Source is not a subject Target is not a subject Highest overlapping interests tier is not less than engaged | [Target] is guaranteed by [source] An agreement established by one country targeting another, where the second country is able to call the first to aid it in any diplomatic play where they are the defender. | ![No](/images/thumb/0/04/No.png/24px-No.png) | 50 | 0 | **+1** every 100 days up to **80** | 0 | 1000 |
| Support Independence | International Relations Source does not have a subject relationship with target Target is a subject Source liberty desire must be at least 25 , share the same overlord, or not be a subject Source must be the same or greater rank to target, or share the same overlord Highest overlapping interests tier is not less than influential Source does not have an Alliance or Defensive Pact with target's overlord | [Target] is supported by [source] An agreement established by one country targeting another, where the first country commits to supporting a subject in a diplomatic demand for independence Diplomatic plays with wargoals: Independence Increase Autonomy Annex Subject Hungarian Revolution Sepoy Mutiny from its overlord. | ![No](/images/thumb/0/04/No.png/24px-No.png) | 50 | 0 | **+1** every 100 days up to **80** | 0 | 1000 |
| Take on Debt | Central Banking Is not unrecognized Target has debt Has sufficient capacity to take on debt This treaty does not have a Money Transfer article from target to source | [Source] takes over [target]'s loans Establishes a deal where one country takes over the other country's loans | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 0 | — | 0 | 0 |
| Money Transfer | Central Banking Is not in default | [Source] transfers money to [target] every week Establishes a deal between two countries where one country agrees to send a fixed sum of money to the other country on a weekly basis. | Quantity | 0 | 25 | — | 0 | 0 |
| State Transfer | Source has at least 2 states Valid states: Is not capital Is not under colonization Either is adjacent to source or is coastal and source has an active port | [Source] transfers a state to [target] Establishes an agreement between two countries where one country officially cedes a state to the other country | State | 0 | 0 | — | 0 | 0 |
| Investment Rights | Stock Exchange Source is not a subject of target If source is a subject, target does not have a treaty with this article with source's top overlord If source and target are in the same power bloc which has Foreign Investment Tier III, source rank is not lower than target rank Highest overlapping interests tier is not less than engaged | Allows [target] to build in [source] Establishes unilateral foreign investment rights in a country allowing it to construct buildings in the other country. | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 25 | **+1** every 200 days up to **50** | 0 | 0 |
| Join Power Bloc | Source is not a subject nor a power bloc leader Source has lower prestige or rank than the target Target is the leader of a power bloc Target's power bloc has sufficient leverage on source to invite Source is not already in target's power bloc Source is not opposing any target's power bloc members in a diplomatic play | [Source] joins [target]'s power bloc An agreement where one country officially joins another country's power bloc | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 0 | — | 0 | 0 |
| Power Bloc Embassy | International Relations Source and target are not in the same power bloc Source is not a power bloc leader Target is a power bloc leader | [Source] hosts a [target] [power bloc embassy](https://vic3.paradoxwikis.com/Power_bloc_embassy) Formally establishes a power bloc embassy in a another country | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 25 | **+1** every 200 days up to **20** | 2000 | 0 |
| Offer Embassy | Source is a Great Power and relations with target are above poor Target is unrecognized, has JE Earning Recognition , and has not requested an embassy from source | [Target] establishes an embassy in [source] Establishes an agreement between two countries where one country formally establishes an embassy in an unrecognized power | ![No](/images/thumb/0/04/No.png/24px-No.png) | 25 | 0 | **+1** every 200 days up to **20** | 2000 | 0 |
| Military Assistance | General Staff Source's army power projection is greater than target's Source rank is higher than target rank | [Source] grants military assistance to [Target] A military agreement between two countries where one country grants military assistance to another country, aiding them with enhanced training and military expertise Source gains: +10% Military Goods Cost +25% Weekly Experience Gain for Armies & Navies Target gains: −10% Military Goods Cost +50% Weekly Experience Gain for Armies & Navies +20% Training Rate +300 Leverage Generation from Treaty +10% Technology Spread for Military | ![No](/images/thumb/0/04/No.png/24px-No.png) | 25 | 0 | **+1** every 200 days up to **50** | 0 | 1000 |
| Goods Transfer | International Trade Neither country is a junior member in a customs union The target market is reachable for trade by the source via land adjacency or a shipping lane Source's Supply Network strength is greater than or equal to 75% or is adjacent to target | [Source] transfers goods to [target] every week Establishes a deal between two countries where one country agrees to send a fixed sum of goods to the other country on a weekly basis The source buys an amount of a specific good on their own market and sells it on the targets market [1] | Quantity Goods | 10 | 0 | — | 0 | 0 |
| Treaty Port | Colonization Source is not revolutionary and has a coastal state that contains a valid treaty port Target is not a subject of source To maintain: either target or its revolutionary or secessionist civil war country controls the state Source rank is not higher than target rank | [Source] cedes a [treaty port](https://vic3.paradoxwikis.com/Treaty_port) to [target] An agreement between two countries where one country officially cedes a treaty port to the other country | State | 0 | 50 | **−1** every 200 days down to **0** | 3000 | 0 |
| Military Access | International Relations | [Target] can march armies through [source] Establishes a military agreement between two countries where one country is allowed to march its armies through the territory of the other country | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 25 | **+1** every 200 days up to **20** | 1000 | 0 |
| Non-Colonization Agreement | Civilizing Mission Source must have a source of colonial growth Valid Strategic Regions: If source has Frontier Colonization, source has a state in the region Target has an interest Any country is decentralized in the region | [Source] agrees to **not** colonize a [strategic region](Strategic region.md) Establishes an agreement between two countries where one country is not allowed to colonize the agreed upon strategic region | Region | 0 | 10 | **−1** every 400 days down to **0** | 0 | 0 |
| Prohibit Trade with World Market | International Trade Source does not have Isolationism or Sakoku [2] and is not a junior member in a customs union Target is not a subject of source Valid goods: Sell orders for good in source market not less than 10 Is tradable | [Source] will **not** trade a good on the [world market](https://vic3.paradoxwikis.com/World_market) The country may not trade a specific good with the world market | Goods | 0 | 25 | **−1** every 200 days down to **0** | 0 | 0 |
| Company Monopoly | Corporate Charters Source is not revolutionary Target has any company established Either: If source is a subject, target has Investment Rights with source's top overlord Target has Investment Rights with source Source is a subject of target Source and target are in the same power bloc which has Foreign Investment Tier III and target rank is higher than source rank | [Source] grants a company monopoly to [target] Establishes an agreement between two countries that establishes a company monopoly of a building in the other country. | Company | 0 | 25 | — | 1000 | 0 |
| Law Commitment | International Relations Source is not a subject of target Target is of equal or higher rank to source | [Source] commits to passing a [law](https://vic3.paradoxwikis.com/Law) Establishes an agreement between two countries where one country commits to passing or retaining a specific law. | Law | 0 | 25 | — | 0 | 0 |
| No Tariffs | International Trade Neither country is a junior member in a customs union nor has Isolationism or Sakoku [2] Target is not revolutionary Valid goods: Sell orders for good in source market not less than 10 Is tradable | [Source] will **not** impose [tariffs](https://vic3.paradoxwikis.com/Tariffs) on a good Establishes an agreement between two countries where one country agrees to not impose tariffs on a specific good. | Goods | 0 | 10 | **−1** every 400 days down to **0** | 0 | 0 |
| Transit Rights | International Relations Neither country is a junior member in a customs union Target has a strategic adjacency to source via itself or another Transit Rights treaty | [Target] can trade through [source] Establishes an agreement between two countries where one country is granted the right to handle its trade through the world market hubs of the other country. [3] | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 50 | **+1** every 200 days up to **20** | 1000 | 0 |
| Trade Privileges | International Relations Neither country is a junior member in a customs union nor has Isolationism | [Target] receives [trade privileges](Market.md) from [source] Establishes trade privileges between two countries where one country grants favorable conditions to the traders of the other country. | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 50 | **+1** every 200 days up to **20** | 1000 | 0 |
| No Subventions | International Trade Neither country is a junior member in a customs union nor has Isolationism or Sakoku [2] Target is not revolutionary Source does not have any variant of Free Trade Valid goods: Sell orders for good in source market not less than 10 Is tradable | [Source] will **not** grant [subventions](https://vic3.paradoxwikis.com/Subventions) on a good Establishes an agreement where one country agrees to not grant subventions on a specific good. | Goods | 0 | 10 | **−1** every 400 days down to **0** | 0 | 0 |
| Amend Succession | Is Brazil Target is Portugal with active JE The United Kingdom Source is not revolutionary, has enacted Monarchy, and does not have a regency Target has enacted Monarchy | [Source] will permit [target]'s candidates to succeed to its throne Establishes an agreement where one country agrees to reincorporate another country's ruling family into their line of succession. Fires the event Back in Order if never before, otherwise Portugal 's ruler is set as Brazil 's heir | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 25 | **+1** every 200 days up to **25** | 0 | 0 |
| Recognize Independence | Source is Spain Target has modifier Independence Not Recognized by Spain Independence Not Recognized by Spain Country modifier −10% Influence Source is not at war | [Source] will formally recognize the independence of [target] An agreement where Spain will formally recognize the independence of her formal colony | ![No](/images/thumb/0/04/No.png/24px-No.png) | 25 | 0 | — | 0 | 0 |
| Transfer Subject | Source has at least 1 subject Valid subjects: Can be transferred as a subject to target Either is adjacent to target or both it and target have an active port | [Source] transfers a [subject](Subject.md) to [target] Establishes an agreement between two countries where one country officially cedes a subject to the other country | Country | 0 | 0 | — | 0 | 0 |
| Ship Transfer | Source is not revolutionary Source has any available ships for transfer Target has an active port Valid ships: Not in battle | [Source] transfers a ship to [target] Establishes an agreement between two countries where one country transfers ownership of a ship to the other country | Ship | 0 | 0 | — | 0 | 0 |
| Toll Exemption | International Relations Source has control over any strait | Exempts [target] from paying [tolls](https://vic3.paradoxwikis.com/Tolls) to [source] Exempts a country from paying tolls to the other country. | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 10 | **+1** every 200 days up to **20** | 0 | 250 |
| No Tolls | International Relations Source has control over any strait | [Source] will **not** impose tolls on any straits it controls Establishes an agreement between two countries where one country agrees to not impose tolls on any straits it controls. | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 25 | **+1** every 200 days up to **20** | 500 | 0 |
| Strait Access | International Relations Source has control over any strait | [Target] is granted access through straits controlled by [source] Establishes an agreement between two countries where one country is granted full access through straits controlled by the other country | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 10 | **+1** every 200 days up to **20** | 250 | 0 |
| No Strait Closure | International Relations Source has control over any strait | [Source] will **not** restrict access to straits it controls Establishes an agreement between two countries where one country agrees to not restrict access to any straits it controls. | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 25 | **+1** every 200 days up to **20** | 0 | 500 |
| Non-Piracy Agreement | International Relations Sourcce is unrecognized Source either is not a subject or its overlord is unrecognized | [Source] stops engaging in piracy against [target] An agreement where one country stops engaging in piracy against the other country | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 10 | — | 250 | 0 |
| Abandon Piracy | International Relations Sourcce is unrecognized Source either is not a subject or its overlord is unrecognized | [Source] abandons piracy An agreement where one country abandons piracy | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 25 | — | 0 | 500 |

## References

1. ↑ If the market price of the good is lower in the target's market than the market price in the source's market, the source will make a loss. Vice versa, and they will make a profit. Goods transfer uses convoys of the source. The amount of used convoys scales proportionally with the amount of the good and the convoy cost multiplier of the good.
2. ↑ 2.0 2.1 2.2 Canton System is exempt
3. ↑ This is useful for landlocked countries that cannot access the world market otherwise

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

| Diplomacy | [Diplomacy](Diplomacy.md) • [Diplomatic action](https://vic3.paradoxwikis.com/Diplomatic_action) • [Diplomatic play](Diplomatic play.md) • [Power bloc](Power bloc.md) • [Ranks](Rank.md) • [Subjects](Subject.md) • Treaties |
|---|---|

| Warfare | [Warfare](Warfare overview.md) • [Land warfare](Land warfare.md) • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
