---
title: Infrastructure
source: https://vic3.paradoxwikis.com/Infrastructure
pageid: 2922
categories: [1.13, Game_concepts]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

For the cost of transporting goods over sea, see
convoys
.
Infrastructure and market access on the state overview screen.
**Infrastructure** simulates the cost of transporting goods over land and creating the necessary foundation to support wide-scale industrialization.

To industrialize a state, it is not simply enough to build heavy industries and have the pops available to work in them. The player also needs to ensure that there is sufficient infrastructure to support those industries.

Infrastructure ties into several mechanics, such as market access, military logistics, and migration, among others.

## Infrastructure sources

Infrastructure is provided and modified by numerous sources. All states have a base of **+3** infrastructure.

### Population

| Source | Amount | Max |
|---|---|---|
| Capital | **+0.1** | **+20** |
| Coastal state | **+0.05** | **+10** |
| Urbanization | **+2** | **+40** |
| Urban Planning | **+1** | **+20** |
| Modern Sewerage | **+1** | **+20** |
| Steel-Frame Buildings | **+1** | **+20** |
| Elevators | **+1** | **+20** |
| Road Maintenance | **+1** | **+20** |
| Transportation Infrastructure I | **+33%** | **+33%** |
| Power bloc statue for Trade Leagues | **+10%** | — |
| Various [companies](Companies.md)' prosperity bonus | Varies | Varies |

All states gain some infrastructure from the size of the state's population once certain [Society technologies](https://vic3.paradoxwikis.com/Society_technologies) have been researched. The relevant technologies are in the branch of the Society technology tree beginning with Urbanization. The amount of infrastructure gained in this way can be viewed in the tooltip for the Infrastructure value in the Information tab of the State panel, where it is called *"Infrastructure per 100K Population"*. It is based on the number of individuals (including [dependents](Pops.md)) living in the state and capped by the same technologies, using the formula:[1]

State Infra. from Pop. = min ( population size ⋅ ⋅ Infra. per 100K Pop. (modifier) 100,000 , Max Infra. from Pop. ) {\textstyle {\text{State Infra. from Pop.}}=\min({\dfrac {{\text{population size}}\cdot {\text{Infra. per 100K Pop. (modifier)}}}{\text{100,000}}},{\text{Max Infra. from Pop.}})} ![{\textstyle {\text{State Infra. from Pop.}}=\min({\dfrac {{\text{population size}}\cdot {\text{Infra. per 100K Pop. (modifier)}}}{\text{100,000}}},{\text{Max Infra. from Pop.}})}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/2389a91f0bc26c8bd897d94c9ba75128e3883014)

Almost all countries (including many decentralized ones) start the game with at least the first relevant technology researched, and so have some infrastructure from population. Note that the precise value shown in the state's UI tooltip is rounded down to one decimal place.

### Automobile consumption

Each unit of automobiles consumed by pops provides **+0.25** infrastructure to a state. Researching Paved Roads increases this to a total of **+0.5** per unit consumed.

### State modifiers

See also:
State traits
Coastal states increase infrastructure from population as noted above, as well as the ability to build ports. For split states, it is not enough for the state region to be coastal, but the split portion must contain at least one passable coastal province.[2] Lakes are not included as coastal, so states bordering the US/Canadian Great Lakes, the Caspian or Aral Sea, or – in game terms – the Hudson Bay are also not considered coastal.

Many states have a trait which adds or reduces infrastructure. States with important waterways, such as the Mississippi or Rhine rivers, receive a flat bonus to infrastructure; while states with difficult terrain, such as mountain ranges, deserts, or notable forests, receive a percentage penalty to infrastructure.

The *Road Maintenance* decree provides an additional **+1** Infrastructure from Pops and **+20** Max Infrastructure from Pops, which is useful to offset temporary penalties from turmoil or devastation, or supplement infrastructure until more railways can be built.

Unincorporated states receive a **−25%** penalty to infrastructure. Devastation reduces infrastructure in equal percentage to the amount of devastation present. Particularly in unincorporated states or states with traits that reduce infrastructure, this can result in **100%** penalty to infrastructure, effectively isolating the state from the wider market.

A country's capital increases infrastructure from population as noted above and its market capital state gains **+25%** infrastructure.

### Buildings

Certain buildings provide infrastructure to their state. The amount of infrastructure provided scales with building level and employment.

**Ports**

Ports provide a small amount of infrastructure with all but the first [production methods](Production method.md). This can be useful in the early game before railways to gain some extra infrastructure in coastal states, but the amount provided is low compared to railways, at most **+5** per level, and this is not the primary purpose of ports, so it is not as efficient, especially once railways are available.

**Railways**

Railways are the primary and most efficient method of increasing a state's infrastructure. In addition to infrastructure, railways also produce transportation, which is used for some production methods and also as a [pop need](Needs.md). Initially, railways produce **+20** infrastructure per level, and with more advanced train production methods, this can be increased up to **+40** per level, or **+55** per level with the Joint Diesel Trains production method unlocked by the Transportation Infrastructure III power bloc principle.

**Urban Centers**

Urban Centers can produce a very small amount of infrastructure, only **+1** or **+2** per level; however, this is provided more cheaply than railways or ports, requiring only a small amount of coal or electricity instead of the more costly engines, clippers, or steamers, as well as not requiring construction time.

### Other

Certain events provide bonuses or penalties to infrastructure – usually temporary; several [companies](Companies.md)' prosperity bonuses also provide additional direct infrastructure; the Rural Folk's loyal trait Farmer's Markets provides **+10%** infrastructure in all owned states; and the power bloc principles Market Unification I and Internal Trade I each provide **+10%** infrastructure in all bloc members' states.

## Infrastructure usage

The infrastructure usage of a state is determined by the types and levels of buildings in the state. Generally, the more urban and specialized the building, the more infrastructure it uses per level. For example, Fertilizer Plants use three infrastructure per level, while rye farms use only one per level.

Most buildings within the same general type have a typical infrastructure usage:

- [Agricultural buildings, plantations](Building.md), and [resource buildings](Building.md) other than mines use **1** per level, except Gold Fields, which use no infrastructure.
- [Government Administration](https://vic3.paradoxwikis.com/Government_Administration), [Universities](https://vic3.paradoxwikis.com/University), and monuments use **1** per level.
- [Mines](https://vic3.paradoxwikis.com/Mines) and oil rigs use **2** per level.
- [Factories](https://vic3.paradoxwikis.com/Factories) use **1.5** (light industry), **2** (military industry), or **2.5** (heavy industry) per level.
- Power Plants use **2** per level.
- [Military buildings](Building.md) use **0.2** per level, except Army and Naval Logistics Centers, which use **0.1** per level.
- [Construction sectors](https://vic3.paradoxwikis.com/Construction_sectors) use **2** infrastructure per level.

[Urban centers](https://vic3.paradoxwikis.com/Urban_centers) do not use infrastructure, and average usage tends to around **1** per level in the early game and to around **2** per level as more heavy industry is built.

## Market access

See also:
Market price
Market access represents how well a state is connected to the national market. It starts as simple calculation of infrastructure over infrastructure usage. If the state has more infrastructure than infrastructure usage, its market access is **100%**, but if usage exceeds available infrastructure, market access is reduced by a proportional amount. For example, if a state has an infrastructure of **45** with a usage of **90**, its market access is at most **50%**. States which are overseas from the market capital also require [shipping lanes](https://vic3.paradoxwikis.com/Shipping_lanes) and convoys; therefore, market access in overseas states is also limited by the supply network strength and can be reduced despite a sufficient supply of infrastructure. Similarly, isolated states, whatever the reason, have 0 market access.

Market access affects how states interact with the national market in two ways: first by reducing a state's buy and sell orders added to the national market, and second by reducing the [Market Access Price Impact](https://vic3.paradoxwikis.com/Market_price) (MAPI) on local prices. Overall, low market access negatively impacts both local prices in a state as well as market prices on the national market. Thus, maintaining good market access in all states is important for a healthy economy.

As an illustration, take a state which produces **100** iron and **0** tools and consumes **0** iron and **50** tools. With **50%** market access, only **50** iron sell orders and **25** tools buy orders are added to the national market. Additionally, the "absolute" local price for iron would be 25% of base price (£10) and for tools 175% of base price (£70). MAPI moderates this by using a percentage of the market price and the remaining percentage of the absolute local price. However, MAPI is also multiplied by market access, thus at **50%** market access, only 50% of the usual price moderation applies.

## Other impacts

The amount of infrastructure in a state impacts some other game mechanics.

### Migration

See also:
Migration
States with low infrastructure have reduced migration potential (both immigration and emigration). Namely, no more than 5 individuals per infrastructure can migrate to or from a state each week.[3]

### Combat width

Combat width is limited by a state's infrastructure (and province's terrain) according to the formula Max width = ( 5 + Infrastructure 2 ) ∗ ∗ Terrain multiplier {\displaystyle {\text{Max width}}=(5+{\tfrac {\text{Infrastructure}}{2}})*{\text{Terrain multiplier}}} ![{\displaystyle {\text{Max width}}=(5+{\tfrac {\text{Infrastructure}}{2}})*{\text{Terrain multiplier}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/70172ebd1ed6e7959a8ccf49592c616a1eed5138)[4].

For example, in a state with 20 infrastructure, a forest province (0.6 modifier) would have a maximum combat width of ( 5 + 20 2 ) ∗ ∗ 0.6 = 15 ∗ ∗ 0.6 = 9 {\displaystyle (5+{\tfrac {20}{2}})*0.6=15*0.6=9} ![{\displaystyle (5+{\tfrac {20}{2}})*0.6=15*0.6=9}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/5c4d45c2f85f2906a350905b866e8fcc749c04a7).

### Occupation gain

Each point of infrastructure *usage* impacts occupation gained after a battle, by limiting the effect of hazardous, forested, and elevated terrain on the occupation cost[5].

## References

1. ↑ 100000 is the defined value from /Victoria 3/game/common/defines/00_defines.txt: `INDIVIDUALS_PER_POP_INFRASTRUCTURE`.
2. ↑ The Siberian states and Arctic Canadian states have impassable coastal provinces for example.
3. ↑ From /Victoria 3/game/common/defines/00_defines.txt: `MIGRATION_MAX_PER_STATE_INFRASTRUCTURE = 5`
4. ↑ See /Victoria 3/game/common/script_values/command_values.txt `province_terrain_infrastructure_force_limit` for formula, and /Victoria 3/game/common/terrain/01_terrain.txt for terrain multipliers
5. ↑ See /Victoria 3/game/common/script_values/occupation_values.txt for details

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | [Government](Government.md) • [Capacities](Capacity.md) • [Characters](Character.md) • [Decrees](Decrees.md) • [Institutions](Institutions.md) • [Laws](Laws.md) • [Technology](Technology.md) |
|---|---|

| Politics | [Elections](Elections.md) • [Ideology](Ideology.md) • [Interest group](Interest group.md) • [Political lobby](Political lobby.md) • [Political movement](Political movement.md) • [Political party](Political party.md) • [Revolution](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| Economy | [Buildings](Building.md) • [Goods](Goods.md) • [Harvest condition](Harvest condition.md) • Infrastructure • [Market](Market.md) • [Production methods](https://vic3.paradoxwikis.com/Production_methods) • [State](State.md) • [Treasury](Treasury.md) |
|---|---|

| Diplomacy | [Diplomacy](Diplomacy.md) • [Diplomatic action](https://vic3.paradoxwikis.com/Diplomatic_action) • [Diplomatic play](Diplomatic play.md) • [Power bloc](Power bloc.md) • [Ranks](Rank.md) • [Subjects](Subject.md) • [Treaties](Treaty.md) |
|---|---|

| Warfare | [Warfare](Warfare overview.md) • [Land warfare](Land warfare.md) • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
