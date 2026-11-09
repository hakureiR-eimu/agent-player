---
title: Market
source: https://vic3.paradoxwikis.com/Market
pageid: 3119
categories: [1.13, Expand, Articles_with_potentially_outdated_sections, Economy]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

Economy
Buildings
List of buildings
•
Unique buildings
Companies
•
Flavored companies
Market
Goods
•
Needs
Production methods
List of production methods
Treasury
A bird's eye view of the French market.
All transactions of [goods](Goods.md) by [pops](Pops.md) and [buildings](https://vic3.paradoxwikis.com/Buildings) take place within a **market**. Each country belongs to either its own market or another market as a member of a [customs union](Market.md). Countries can also import or export goods between markets via trade. Each market has its own prices for goods based on the total number of buy and sell orders in the market.

Markets also define the range for internal [migration](Migration.md).

## National market

The national market represents the sum of goods transactions within a country. By default, each country has its own national market, which has a Market Capital, typically the same state as its Government Capital. All states within the market have a measure of market access from **0%** to **100%**, which represents how well the state is connected to the national market. Market access depends primarily on a state's Infrastructure usage, while overseas states (those which are not in a contiguous region with the market capital) also require Ports and Convoys through a shipping lane.

### Customs union

Customs unions are joint markets led by a single country, the market owner. Customs unions come about in one of three ways:

1. All [subjects](Subject.md) automatically join their overlord's market.
2. Trade League [power blocs](Power bloc.md) are always customs unions, with the bloc leader as the market owner.
3. Other power blocs can become customs unions with Market Unification III, with the bloc leader as the market owner.

A customs union has only a single market capital, that of the market owner.

Members of a customs union can also be granted their own market: subjects by their direct overlord; bloc members by the bloc leader. This removes that country – and its subjects – from the union and creates a new market led by that country.

### Market adjacency

Markets are considered adjacent if they share a direct land border or connect to any shared sea node.

### Market price

See also:
Goods
All goods have a defined *base price*. This is the price if the number of buy orders equals the number of sell orders. The actual price of each good varies based on the total number of buy and sell orders across all states in a market. The price of goods can vary between 75% below to 75% above the base price. That is the final *market price* can vary from 25% to 175% of the base price.

The price of a good in a state or a market is given by the following formula:[1]

price = Base Price ∗ ∗ [ 1 + 0.75 ∗ ∗ clamp ( BUY − − SELL min ( BUY , SELL ) , ± 1 ) ] {\displaystyle {\text{price}}={\text{Base Price}}*\left[1+0.75*{\text{clamp}}\left({\dfrac {{\text{BUY}}-{\text{SELL}}}{\min({\text{BUY}},{\text{SELL}})}},{\text{±}}1\right)\right]} ![{\displaystyle {\text{price}}={\text{Base Price}}*\left[1+0.75*{\text{clamp}}\left({\dfrac {{\text{BUY}}-{\text{SELL}}}{\min({\text{BUY}},{\text{SELL}})}},{\text{±}}1\right)\right]}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/655addd66852785f0a0eaaca4a62e222ae137c3a)

For example, for a good with a base price of 20 such as wood, when there are 100 buy orders and 120 sell orders, its price will be:

price = 20 ∗ ∗ [ 1 + 0.75 ∗ ∗ clamp ( 100 − − 120 100 , ± 1 ) ] = 20 ∗ ∗ ( 1 − − 0.15 ) = 17 {\displaystyle {\text{price}}=20*\left[1+0.75*{\text{clamp}}\left({\dfrac {100-120}{100}},{\text{±}}1\right)\right]=20*(1-0.15)=17} ![{\displaystyle {\text{price}}=20*\left[1+0.75*{\text{clamp}}\left({\dfrac {100-120}{100}},{\text{±}}1\right)\right]=20*(1-0.15)=17}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/439709f5ef76c1f09ce16d457457d268519f99a1)

or 15% below base price, because there is more supply than demand.

It should be stressed that the amount of goods bought and sold in the market is not the same. All of the buy orders are bought and paid for by pops or industries, and all of the sell orders are sold with revenue received by industries. The difference between the two is created or destroyed by the simulation, along with the corresponding monetary value.

When there are more sell orders than buy orders, this effect creates extra value in the economy, with the local maximum of 20.87% sell orders times good base price achieved at market price of -39.56% below base, or 65.5% ratio of buy to sell orders and the absolute maximum of 25% sell orders times good base price achieved with no sell orders at all (theoretically at 100% MAPI, reduced by actual MAPI as described below).

Conversely, when there are more buy orders than sell orders, value in the economy is destroyed, since buyers pay more money in total than sellers receive.

Continuing with the example above, buyers would pay for 100 wood, and sellers would receive money for 120 wood, with the resulting difference of 17*(120-100)=£340 appearing in the economy, which makes up for 14.2% of 20*120=£2400 of the wood made available on the market.

### Market access

Main article:
Market access
Market access represents how well a state is connected to the national market. It starts as simple calculation of infrastructure over infrastructure usage. If the state has more infrastructure than infrastructure usage, its market access is **100%**, but if usage exceeds available infrastructure, market access is reduced by a proportional amount. For example, if a state has an infrastructure of **45** with a usage of **90**, its market access is at most **50%**. States which are overseas from the market capital also require [shipping lanes](https://vic3.paradoxwikis.com/Shipping_lanes) and convoys; therefore, market access in overseas states is also limited by the supply network strength and can be reduced despite a sufficient supply of infrastructure. Similarly, isolated states, whatever the reason, have 0 market access.

Market access affects how states interact with the national market in two ways: first by reducing a state's buy and sell orders added to the national market, and second by reducing the [Market Access Price Impact](https://vic3.paradoxwikis.com/Market_price) (MAPI) on local prices. Overall, low market access negatively impacts both local prices in a state as well as market prices on the national market. Thus, maintaining good market access in all states is important for a healthy economy.

### Local price

| Source | Amount |
|---|---|
| Base | **75%** |
| Unincorporated state | **−10%** |
| Traditionalism | **−15%** |
| Stock Exchange | **+10%** |
| Zeppelins | **+5%** |
| Macroeconomics | **+5%** |
| Some major rivers | **+5%** |

While market price reflects the general cost of goods across the market, each state has a separate *local price* for each good. As all transactions occur on the state level, excluding inter-market trades, the local price in each state is the actual amount each pop and building pays or gains. The local price is calculated as a proportion of the market price and the state price – calculated as though the state made its own market. The proportion is called *Market Access Price Impact* (MAPI), which is determined by laws, technology, and state traits and incorporation, then multiplied by the state's market access. For example, with a MAPI of 85%, the local price in a state is the weighted average of 85% of market price and 15% of the state price. As another example, isolated states have 0% market access (and so 0% MAPI) and so use 100% of the state price. Finally, local-only goods, services, transportation, and electricity always use only the state price.

The local price of a good is given by the following formula: local price = MAPI ∗ ∗ Market Price + ( 1 − − MAPI ) ∗ ∗ State Price {\displaystyle {\text{local price}}={\text{MAPI}}*{\text{Market Price}}+(1-{\text{MAPI}})*{\text{State Price}}} ![{\displaystyle {\text{local price}}={\text{MAPI}}*{\text{Market Price}}+(1-{\text{MAPI}})*{\text{State Price}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/6e89e8ff81e19fc6ff93bdc6f5519b8e00698d78)

For example, iron has a base price of **£40**; if the national market balance is 0, meaning buy and sell orders are equal, and the state produces iron but consumes none making it 75% below base price (£10), the formula for local price would be as follows when MAPI is at 85%[2]: local price = ( 0.85 ∗ ∗ 40 ) + ( 0.15 ∗ ∗ 10 ) = 34 + 1.5 = 35.5 {\displaystyle {\text{local price}}=(0.85*40)+(0.15*10)=34+1.5=35.5} ![{\displaystyle {\text{local price}}=(0.85*40)+(0.15*10)=34+1.5=35.5}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/15f9c5dbfe147d3c65b68f004d204b0d9b8cdd60) This is an 11% decrease from the market price meaning that iron mines are losing potential money as no iron is bought locally.

#### Oversupply and undersupply

In Victoria 3, transactions of goods are not directly from producer to consumer, but abstracted through the market. That is, producers can sell all of their goods and consumers can purchase all of their goods, even if the number of buy and sell orders for a good do not match. Mismatches in buy and sell orders results in price changes as noted above. For this reason, oversupply (more sell orders) and undersupply (more buy orders) of goods each impact the cash reserves of buildings and wealth of pops. Additionally, as market and local prices are capped at **75%** above or below base price, extreme over- or under-supply results in losses for the buyer or seller compared to an uncapped "true" value of the good.

The price effects of over- and under-supply are magnified by the effects of market access and MAPI. A state which only produces a good has an decreased price for that good compared to the national market and conversely a state that only consumes a good has an increased price. This can result in a loss of money between a producer's sell price and a consumer's buy price when they are in different states. If the producer and consumer are in the same state, this loss does not occur.

An oversupply is good for pops and buildings that purchase the good, as they have more cash remaining than typical, leading to standard of living increases and higher dividends. However, when a good is highly oversupplied, the buildings which produce that good are unlikely to make any profit, and thus they are unable to raise their workers' wages and may even fire workers to balance their budget. With fewer workers, the production of the good is reduced, thus bringing supply back to a healthier equilibrium, but fired workers become radicals and reduced production also reduces demand of input goods thus affecting the buildings producing them, so this is not typically an effective strategy. Government subsidies can keep production going, though often a great expense to the national treasury.

While an undersupply increases the profits of buildings producing that good – and the dividends of its ownership pops, a large undersupply of goods is almost never desirable. In particular, if buy orders are twice or more of sell orders, it results in a *shortage* for all buildings using that good as an input. While shortages can resolve themselves, this is often more damaging as a shortage of an input good for a building can lead to a shortage of its output goods. Additionally, high prices may reduce pops' standard of living. Thus, deliberate action to change the situation is recommended. This may include increasing production of the good, importing it from another market, or reducing its consumption.

#### Shortages

A *shortage* occurs when the buy orders of a good exceed sell orders by at least double. This is indicated by the shortage icon besides the good's icon. A shortage reduces the throughput of all buildings requiring the good as an input by **−5%** and increasing **−1%** per day up to a maximum of **−50%** (or **−75%** if the input good is missing entirely from local supply), depending on the severity of the shortage. When the shortage is resolved the modifier decreases by **1%** per day until it reaches **0** and is removed.

This effect is extremely damaging since buildings which already had one of their input goods at an extremely high price (+75%), now also receive a throughput malus. As the buildings lose throughput, fewer input goods are demanded and as the building becomes less profitable, workers might be fired, further reducing throughput and thus demand. Both effects reduce the demand for the good in shortage and slowly alleviate it, however this equilibrium could be found at a certain percentage of the shortage effect, still reducing the effectiveness of its buildings, so it still should demand the player's attention in fixing it.

## Trade

Countries in different markets can engage in trade between their markets. This is done automatically via the [world market](https://vic3.paradoxwikis.com/World_market) or manually through a [treaty](Treaty.md) using the *Goods Transfer Article*. Countries which have enacted Isolationism typically cannot engage in trade via the World Market, but can trade via Goods Transfer Articles. Additionally, unless a country has enacted Free Trade, it can gain national income from trade via tariffs. Trade via the world market is facilitated by Trade Centers, which can be nationally or privately built and owned.

### World market

The **world market** is conceptually located in the sea. To access it, a market area must either possess a Port or the country it belongs to must have a [treaty](Treaty.md) with another country that includes the *Transit Rights* article while the other country has an adjacent market area with a Port.

#### World market hub

A **world market hub** represents the primary trade center with the world market for a market area. Each market area with at least one Port has a single hub. If a market has more than one port, the location of the world market hub can change depending on Port levels and states' gross domestic product, but will generally remain relatively stable.

#### Blockades

During war, fleets can be given orders to Blockade a sea node, which reduces supply routes to and world market access for states adjacent to that sea node. A blockade is not immediately effective, but scale up over time to the maximum blockade strength.

Each type of [flotilla](https://vic3.paradoxwikis.com/Flotilla) has a certain Blockade strength, with capital ships generally having 10 times the blockade strength of equivalent light ships. The blockade strength determines the blockade level on a scale from 0% to 100%, which gives scalable deficits for the state(s) blockaded.

At 100% blockade level, the following effects are applied

- **−50%** [migration](Migration.md) attraction
- **−75%** efficiency for [shipping lanes](https://vic3.paradoxwikis.com/Shipping_lanes)
- **−75%** world market access
- **−75%** throughput for Fishing Wharves and Ports

#### Straits

**Straits** are connections between sea nodes that are controlled by neighbouring land provinces. All ships passing through a strait must obey the rules of the strait. The strait owners can decide whether or not the strait is open to military, what traffic may pass through the strait, and what tolls they enact. Tolls may be set to low, medium, or high. The tolls are paid for by the trade centres who are conducting trade through the strait. Trade centres may reroute to go around a strait if it's more profitable than going through a strait. Canals also function as straits when created.

#### Trade advantage

Trade advantage is a measure of how dominant a country is in the trade of a particular good. Trade advantage individually modifies the import price or export price for a good in a certain state. At 100%, trade advantage provides a **25%** better price. However, trade advantage is a zero-sum game, as the overall market price remains unchanged, meaning that gains for one country results in losses for others. Therefore, there are two values at play: *absolute* trade advantage and *relative* trade advantage. Relative trade advantage is a country's trade advantage as a percentage of global trade advantage.

The world market price has a monopoly bonus. If one market controls 100% of exports, the world market price is 20% higher. This higher price is scaled to the share of global trade owned by the largest trader, so if one country controls 50% of the market the price is 10% higher. In this scenario, trade advantage does not affect the price.

Trade advantage is made up of several factors:

- Base trade advantage: **100**
- **+2** for every percentage of the global production that is within the market area
- **+0.5** for every percentage of the production in a market area that is controlled by a [company](https://vic3.paradoxwikis.com/Company) with trade rights
- **+1** for every percentage of production that is prestige goods, for export advantage only
- **+1** for each percentage of trade going to a country that the trade center's owner has trade privileges with
- **+2** for each percentage of trade that is to a trade center in a treaty port
- **−0.5** for each percentage of trade that is going to a country that the trade center owner lacks an [interest](https://vic3.paradoxwikis.com/Interest) with. This is not applicable with External Trade III
- **−0.75** for each percentage of trade with a country that is at war with the trade center owner
- **−1** for each percentage of trade going to a country that is embargoing the trade center owner

There is also a list of flat bonuses that modify trade advantage:

- **+25%** for having External Trade I power bloc principle
- **+5%** for trade centers in the market capital
- **+25%** depending on the trade center owner's trade law.
- Up to **+0.5%** for every 100 trade capacity in the trade center (max +20% further modified by [banking](https://vic3.paradoxwikis.com/Banking) techs).

The following [Trade Policies](Economy laws.md) may modify trade advantage:

| Law | Effects |
|---|---|
| Mercantilism An export-focused economy with an emphasis on keeping a positive current account and competing with other nations. | −25% Trade Advantage for imports +25% Trade Advantage for exports |
| Protectionism Our industries must be protected from the depredations of foreign market actors. |  |
| Free Trade The free exchange of goods must not be impeded, as trade is for the benefit of all. | +25% Trade advantage |
| Isolationism An economy focused on supplying the nation's needs internally, while keeping out of the affairs of others. | Disable trade centers |
| Canton System A variant of Isolationism where trade is only permitted in a single coastal state. |  |

#### Trade capacity and traded quantity

| Production Method | Merchant Marine | Traded Quantity |
|---|---|---|
| [Small-Scale Trading](https://vic3.paradoxwikis.com/Small-Scale_Trading) | **+3.0** | **−50.0%** |
| [Regular Trading](https://vic3.paradoxwikis.com/Regular_Trading) | **+4.0** |  |
| [Bulk Trading](https://vic3.paradoxwikis.com/Bulk_Trading) | **+5.0** | **+50.0%** |
| [Mass-Scale Trading](https://vic3.paradoxwikis.com/Mass-Scale_Trading) | **+6.0** | **+100.0%** |

[Trade centers](https://vic3.paradoxwikis.com/Trade_centers) autonomously import or export an amount of goods each week up to a limit calculated from the center's **trade capacity**.

Each level of the trade center provides 10 trade capacity and consumes a certain amount of [Merchant Marine](https://vic3.paradoxwikis.com/Merchant_Marine). The unique [Skyscraper](https://vic3.paradoxwikis.com/Skyscraper) government building provides a production method called [Trade Nexus](https://vic3.paradoxwikis.com/Trade_Nexus) that increases trade capacity by **+25%**. Additionally, two East-Asian variant [Trade Policies](https://vic3.paradoxwikis.com/Trade_Policy) reduce trade capacity: [Canton System](https://vic3.paradoxwikis.com/Canton_System) (**−25%**) and [Sakoku](https://vic3.paradoxwikis.com/Sakoku) (**−75%**).

In the tables of [Goods](Goods.md), the **Traded Quantity** column is the base quantity of each good that 1 trade capacity can trade. The [power bloc](Power bloc.md) principle External trade I increases Traded Quantity by **+25%**. The various trade center [production methods](List of production methods.md) increase or decrease this Traded Quantity at the cost of [Merchant Marine](https://vic3.paradoxwikis.com/Merchant_Marine).

A trade center's **Weekly Trades** is the number of times per week that a trade center may increase or decrease trade volumes for better profit.

### Tariffs and subventions

| Type | Mercantilism | Canton System | Sakoku | Protectionism | Free Trade | Isolationism |
|---|---|---|---|---|---|---|
| Import Tariffs | 50% | 50% | 50% | 50% | — | — |
| Export Tariffs | 20% | 50% | 50% | 50% | — | — |
| Import Subventions | 20% | 20% | 20% | 50% | 50% | — |
| Export Subventions | 50% | 20% | 20% | 50% | 50% | — |

See also:
Trade Policy laws
Countries can impose tariffs or provide subventions on the import or export of specific goods, which can be set to **none**, **12.5%**, **25%**, or **50%**. The maximum percentage permitted is determined by the country’s current Trade Policy law. The tarrifs and subventions are paid by or to the Trade Centers which trade those goods.

Tariff percentages are calculated from a good's base price rather than its market price. Countries in a customs union – including subjects – split tariffs proportionally by their relative GDP, with the market owner receiving a minimum of 25% of the tariff income.

The power bloc principles Market Unification II and Internal Trade II each add an additional flat **+20%** tariffs on all trade routes with non-bloc members. These additional tariffs apply even for trade routes owned by countries within the bloc that have enacted Free Trade.

### Embargoes

A market owner can impose an embargo on another market owner to reduce that country's trade advantage for a base cost of **100** Influence. Embargoes are also automatically imposed at no cost whenever two countries are at war with each other; these automatic embargoes are removed when peace is signed. Embargoes decreases the trade advantage by **1%** for both countries on goods for each percentage of a bought good, that comes from the other party's market.

Members of a customs union or a power bloc with Market Unification I cannot embargo each other. The automatic embargo from war still applies in the case of a power bloc with Market Unification.

### Treaty ports

Treaty ports are a special type of state, based on the port province of a state region. They can be established by a diplomatic play or [treaty](Treaty.md) and allow the owner of the treaty port to bypass tariffs and embargoes by enabling the owner of the treaty port to build trade centers that buy and sell from the market that the treaty port resides in to the world market.

Treaty ports treaties can be withdrawn by the initiator at will and only be withdrawn by the market's owner if:

- The market's owner is of **greater** [rank](Rank.md)
- The market's owner is not unrecognized
- Treaty duration is over or 5 years has passed after the war if the treaty was forced via war

When the treaty, governing the treaty port is withdrawn, the former owner of the treaty port will still keep the province, but it will lose its status as a treaty port. If a treaty port is temporarily lost as a result of a secession or revolution, it will be reinstated after the rebels have been defeated, except in the case of special revolution tags like Heavenly Kingdom and similar due to a bug.

When a country gains control, through revolution or conquest, of land hosting foreign treaty ports, it inherits those treaty port agreements, and is given the choice to honor them or revoke them and reclaim the ports for itself. The affected foreign power is notified of the decision either way.

|  | Please help improve this article or section by [expanding it](https://vic3.paradoxwikis.com/index.php?title=Market&action=edit) with: What is the actual effect of *renege_treaty_ports_with*? Needs empirical testing. |
|---|---|

id

### An Inherited Concession

With the old regime swept aside, the treaty ports it once granted to [Target] have passed into our keeping. Their merchants still raise a foreign flag over our harbors under agreements we never signed. We may honor what we have inherited, or cast the foreigners out and reclaim these ports for [us].
---

Flavor text:
"The ink was dry long before we took power, yet the chains it forged are now ours to wear or to break."
---

| Is triggered by: On inheritance of treaty port |
|---|
| Trigger conditions: None |
| Honor the agreements AI weight: 55 +50 if relations greater than or equal to cordial -40 if relations less than hostile (Triggers the event Concessions Honored for [Target]) Reclaim our harbors AI weight: 45 -40 if relations greater than or equal to cordial +50 if relations less than hostile renege_treaty_ports_with: scope:target_country ([Target] shifts towards Economic Imperialism for 10 years) (Triggers the event Concessions Revoked for [Target]) |

id

### Concessions Honored

There has been an upheaval in the lands about our treaty ports. With the previous regime gone, [New Host] has chosen to honor the agreements struck with those who came before. Our merchants may continue to fly our flag over their harbors.
---

Flavor text:
"A change of masters, yet the same old bargain. How refreshingly reasonable."
---

| Is triggered by: Event An Inherited Concession |
|---|
| Trigger conditions: None |
| A wise decision No effect |

id

### Concessions Revoked

There has been an upheaval in the lands about our treaty ports. With the previous regime gone, [New Host] has torn up the agreements struck with those who came before. Our ports have been seized and our merchants turned out into the street. This insult shall not soon be forgotten.
---

Flavor text:
"They would deny us what was promised by those who came before. Let them remember that our guns have long memories."
---

| Is triggered by: Event An Inherited Concession |
|---|
| Trigger conditions: None |
| An outrage! No effect |

## Supply network

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.11. |
|---|---|

A country's supply network is the total of all of its shipping lanes. If a country does not have sufficient convoys to support its supply network, it suffers reduced market access for overseas states and the [supply](Land warfare.md) of overseas armies is reduced.

### Shipping lane

Shipping lanes are the connections between non-adjacent areas. Shipping lanes are used for intra-market connections to overseas states and regions, and supply routes for overseas armies. Each shipping lane has a required convoy usage. The amount required varies depending on the type of shipping lane and distance it travels.

When at war, a country's shipping lanes may be disrupted by an enemy navy using the Raid Convoys order. This directly reduces the efficiency of affected shipping lanes as well as reducing the number of convoys thus potentially impacting the market's overall supply network. A country can order its navy to Escort Convoys to reduce the effect of enemy raids.

### Convoys

Convoys are the capacity required for shipping lanes and the supply network. Convoys are produced by Ports, requiring either clippers or steamers as an input. [Subjects](Subject.md), as well as junior members of customs unions, transfer 50% or 75% of their convoys to the the market owner.

## References

1. ↑ The 0.75 is based on the define `PRICE_RANGE` which can be set between 0 and 1, and it scales based on the define `BUY_SELL_DIFF_AT_MAX_FACTOR`, which defines the maximum ratio of buy and sell orders beyond which prices do not change.
2. ↑ [Source of this example](https://www.reddit.com/r/victoria3/comments/166oilq/how_local_prices_work_in_victoria_15_beta_so_far/)

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | [Government](Government.md) • [Capacities](Capacity.md) • [Characters](Character.md) • [Decrees](Decrees.md) • [Institutions](Institutions.md) • [Laws](Laws.md) • [Technology](Technology.md) |
|---|---|

| Politics | [Elections](Elections.md) • [Ideology](Ideology.md) • [Interest group](Interest group.md) • [Political lobby](Political lobby.md) • [Political movement](Political movement.md) • [Political party](Political party.md) • [Revolution](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| Economy | [Buildings](Building.md) • [Goods](Goods.md) • [Harvest condition](Harvest condition.md) • [Infrastructure](Infrastructure.md) • Market • [Production methods](https://vic3.paradoxwikis.com/Production_methods) • [State](State.md) • [Treasury](Treasury.md) |
|---|---|

| Diplomacy | [Diplomacy](Diplomacy.md) • [Diplomatic action](https://vic3.paradoxwikis.com/Diplomatic_action) • [Diplomatic play](Diplomatic play.md) • [Power bloc](Power bloc.md) • [Ranks](Rank.md) • [Subjects](Subject.md) • [Treaties](Treaty.md) |
|---|---|

| Warfare | [Warfare](Warfare overview.md) • [Land warfare](Land warfare.md) • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
