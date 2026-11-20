---
title: State
source: https://vic3.paradoxwikis.com/State
pageid: 3134
categories: [1.13, Game_concepts]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

Infrastructure and market access on the state overview screen.
**States** are the main political-geographical unit of Victoria 3, where pops live and buildings are built. Most economic actions involve interacting with states. States are based upon *state regions*, predefined parts of the map which can be subdivided into multiple *split states*; however it is common for a state to be coterminous with its state region.

## State region

See also:
List of state regions
State regions are defined areas of the map made up of a number of tiles or *provinces*. Each state is a state region or a part of a state region owned by a single country. States inherit all of their state region's traits.

### Inheritable features

See also:
State traits
States inherit certain features from their state regions, including:

- *State Traits*: These represent a wide variety of geographical features that have an impact on the economy, infrastructure, or population of the entire state region.
- *Claims*: A state region can be claimed by a country that does not currently own it but are broadly considered to have a legitimate reason to.
- *Homelands*: Every [culture](Culture.md) has one or more state regions that it considers to be its natural homeland. Cultural homelands impact migration, assimilation, and incorporation and are very important for [nation formations](Formable countries.md) and cultural secessions.
- Which [flavored companies](List of flavored companies.md) can be established by owning a specific state

### Hubs

Hubs are defined provinces that represent a city within the state region. Visually, each type of hub appears and grows based on the number of buildings related to its type in the state region. Most hubs have no game mechanic interaction aside from updating the road/rail network by their presence or absence; port hubs define the location of treaty ports.

| Hub | Buildings |
|---|---|
| City | Everything not included in other hubs |
| Farm | All agriculture and plantations |
| Mine | All mines and oil rigs |
| Port | Shipyards and Military Shipyards Fishing and Whaling Industries Ports and Naval Bases |
| Wood | Logging Camps |

Hubs can overlap, such that the same province is two or more hubs, and not every state region has every type of hub, notably inland states have no port hub.

### Split state

A split state is a subdivision of a state region, where two or more countries each own a portion of the state region. Split states divide up limited resources, such as lumber, mining, and arable land, based on their share of provinces from the state region. The specific formula is as follows:[1]

S h a r e = r e g u l a r n + ( 5 ⋅ ⋅ p r i m e n ) r e g u l a r t + ( 5 ⋅ ⋅ p r i m e t ) {\displaystyle Share={\dfrac {regular_{n}+(5\cdot prime_{n})}{regular_{t}+(5\cdot prime_{t})}}} ![{\displaystyle Share={\dfrac {regular_{n}+(5\cdot prime_{n})}{regular_{t}+(5\cdot prime_{t})}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/80627192a8987a9d388e8e9c0704acaf61816ce5)

Additional explanation
Specifically, the number of regular and "prime" provinces in the split state (sub n) divided by the number of regular and prime provinces in the state region (sub t); impassable provinces are not counted at all. Additionally, sea-based resources or buildings – fishing, whaling, ports and naval bases – are not available to a split state which does not contain at least one coastal province, but the fishing and whaling resources are still divided out to the split state, reducing their availability to other split states.

Split states can be created during gameplay in three ways: [treaty ports](https://vic3.paradoxwikis.com/Treaty_port), [colonization](https://vic3.paradoxwikis.com/Colonization_(mechanic)), or certain effects – including revolutions, [releasing](Releasable countries.md) certain countries, or events.

#### Split states naming conventions

Split states are typically named by their owner's adjective plus the state region name, e.g. Bavarian Rhineland; a split state which controls more than half of the state region is given the state region name, and a split state owned by a one-state country is typically given the country's name. If a country only owns a single hub province in a state, its portion of the state typically takes that hub's name. If an entire country at the start of the game is comprised of a split state, the state usually takes the name of the country. This also applies to countries that lose all their other states during the game; for example if [Denmark](Denmark.md) loses all of its states except for Danish Togo, the latter will be referred to simply as "Denmark".

### Resource limits

Each state region has a certain amount of arable land and resources. This limits how many and which agriculture and resource industry (rural) [buildings](https://vic3.paradoxwikis.com/Buildings) a state can support. As noted above, arable land and resources are divided among split states proportionally, except for fishing and whaling, which only goes to coastal provinces. In addition to resources present from the start of the game, certain resources ( gold, rubber, and oil) may be discovered during gameplay, unlocked by certain [technologies](https://vic3.paradoxwikis.com/Technologies). State regions always indicate if there are discoverable resources present, even before the unlocking technologies have been researched.

### Strategic region

See also:
Strategic region
Each state region belongs to a *strategic region*, a larger geographic area that is the basis for [interests](https://vic3.paradoxwikis.com/Interests) and [HQs](Warfare overview.md). There are 36 strategic regions, each containing between 6 and 47 state regions with an average of around 19 state regions per strategic region.

## State status

In addition to ownership, there are a number of conditions that apply to a state and affect the local population and economy.

### Incorporation status

| Cultural Homeland | ![Time](/images/thumb/0/08/Time.png/24px-Time.png) Time |
|---|---|
| Primary culture | 2 years |
| Shared heritage and language trait | 5 years |
| Shared heritage or language trait | 10 years |
| Shared heritage or language group | 15 years |
| No shared heritage nor language group | 25 years |

Incorporation status represents a state's political status within the country that owns it. The different incorporation statuses are as follows:

- *Incorporated state*: A state that is a fully integrated political unit in the country. These states incur full bureaucracy costs, pay all forms of [taxes](https://vic3.paradoxwikis.com/Taxes) required by the government, and benefit from all national [institutions](Institutions.md).
- *Unincorporated state*: A state that is owned but only very lightly administered by the country, such as frontier states. Unincorporated states do not incur any bureaucracy costs and their pops pay no taxes; however, nationally owned buildings still pay dividends which is recorded as taxes. Unincorporated states receive no benefits from national institutions and have reduced infrastructure.
- *Colony state*: A state undergoing active colonization. This is typically the same as an unincorporated state except that, as long as colonization is ongoing, it cannot begin incorporation. It is not possible to trade them via [treaties](Treaty.md) either. In certain circumstances, it is possible for a country to colonize the same state region that contains one of its incorporated states (e.g. [Argentina](Argentina.md) colonizing Buenos Aires).

Unincorporated states can be incorporated as long as there is a bureaucracy surplus equal to or more than the total cost to administer the state. The benefits of incorporation are phased in over the incorporation process, which takes between 2 to 25 years depending on cultural homelands present in the state; there are five society techs that when researched increased incorporation speed by **5%** each. It is not possible to unincorporate a state, except by losing ownership of it to another country then recapturing it or having the state revolt. Additionally, a country automatically gains a claim if it loses an incorporated state due to a diplomatic play or war. Conquering a claimed state automatically incorporates it when it contains a primary culture's homeland.

Unincorporated states have the following modifier:

- **−25%** infrastructure
- **−10%** market access price impact
- **−50%** conscriptable battalions
- **−50%** Pop political strength
- **−33%** Expected standard of living.
- **−10%** Throughput for manufacturing, government structure, and military building groups
- Reduced construction efficiency for certain building groups:
  - **−20%** Infrastructure and extraction
  - **−30%** Light industry and government structures
  - **−50%** Heavy industry

Additionally, subsistence buildings in unincorporated states have **−20%** subsistence output and starting wages are reduced by **−20%**. These effects remain in full until the state is completely incorporated.

### Infrastructure and market access

Main article:
Infrastructure
Infrastructure determines the [market access](https://vic3.paradoxwikis.com/Market_access) of a state. Unless a state is isolated – entirely unable to access the [market capital](https://vic3.paradoxwikis.com/Market_capital), its market access is primarily a percentage based on infrastructure and infrastructure usage. States which are not connected to the market capital by land – that is, overseas – also require convoys and [shipping lanes](https://vic3.paradoxwikis.com/Shipping_lanes) for their market access; a lack of which can reduce the market access even with sufficient infrastructure. Infrastructure is gained mainly from railways and ports; however, there are other sources and several modifiers which increase or decrease infrastructure as well.

Market access reflects how connected the state is with the rest of the market. Low market access means the state's economy operates more "independently" and prices of goods in the state may differ greatly from the wider market. There are no "regional markets", such that overseas states cannot support each other unless they can access the market capital. Market areas apply only to trade centers, and states disconnected from the market capital cannot buy or sell from other states within the same national market.

### Taxation capacity

See also:
Treasury#Unrealized taxes
Incorporated states require sufficient *taxation capacity* in order to effectively collect taxes from the pops living in the state. A state requires 1 point of taxation capacity per 10,000 population to achieve full tax efficiency. This is calculated against all population, not just against the workforce — a state with a population of 2.8 million requires 280 points of taxation capacity no matter how many are dependents, peasants, etc. States have a base taxation capacity of 100 and some techs increase that base, but taxation capacity primarily comes from government administration buildings. More advanced production methods for these buildings greatly increase the amount of taxation capacity provided, and like most things buildings produce, their output of taxation capacity is affected by throughput and economy-of-scale bonuses.

If taxation capacity is insufficient for the population of the state, a percentage of the pops' taxes are not collected; for example if a state has **−50%** taxation capacity, pops in that state pay only 50% of the usual tax. This contrasts with *tax waste* which discards the waste percentage of taxes for the entire country. Tax waste is caused by a country exceeding its [Bureaucracy](Capacity.md) capacity.

Tax collection can also be reduced by other sources, such as recently conquered states, obstinance, or events.

### Capital state

Each country has a *capital state*, where the seat of government is. The capital state has **+25%** taxation capacity, **+10%** infrastructure per 100K population, **+20** max infrastructure from population, and gives **+25%** political strength to pops living there. Occupying an enemy country's capital state is one way to force their [capitulation](https://vic3.paradoxwikis.com/Capitulation) during war, and certain war goals require occupying the capital state.

While not at war or involved in a diplomatic play, the capital state can be changed to any other incorporated state that is a primary culture's homeland once every 5 years. Moving the capital adds a 5-year decaying **−10%** penalty to bureaucracy, authority, and influence. If the capital is forced to move by an event or by losing the previous capital in war, the new capital is automatically incorporated.

### Market capital

See also:
Market
Each market owner has a *market capital*, which is used for determining market access and isolated states. The market capital adds **+25%** infrastructure and **+5%** trade advantage to its state. While not at war or involved in a diplomatic play, the market capital can be changed to any other incorporated state once every 5 years. Moving the market capital adds a 5-year decaying **−10%** penalty to throughput for all buildings.

### Cultural communities

Cultural communities reflect the [cultures](https://vic3.paradoxwikis.com/Cultures) of all pops living in a state. Pops cannot [migrate](https://vic3.paradoxwikis.com/Migrate) to states without a cultural community matching their culture; however, there is a small chance each month for a cultural community to form in a state without any pops of that culture. If a culture is not present in a state, its cultural community disappears after one week. Cultural communities are not required for [mass migrations](https://vic3.paradoxwikis.com/Mass_migration).

### Turmoil

| Turmoil amount | Tax Waste | Migr. Attr. | Cons. eff. |
|---|---|---|---|
| Moderate (25%) | **+25%** | **−15%** | **−33%** |
| High (50%) | **+50%** | **−25%** | **−50%** |
| Extreme (75%) | **+75%** | **−50%** | **−75%** |

A state where a large percentage of the population are radical experiences turmoil in increasing severity. A state with turmoil suffers penalties in the form of increased tax waste and reduced construction efficiency and migration attraction. Turmoil applies by thresholds, with each level requiring that percentage or more of the state's population to be radical.

These penalties can be reduced by investing into the Law Enforcement institution or by enacting the Violent Suppression decree.

Each level of law enforcement decreases the effects of turmoil by **15%** (**20%** with Local Police Force) in incorporated states. This effect scales up with the progression of incorporation when incorporating a state. Violent suppression decreases the effects by **50%**, but also increases the mortality of the state by **2%** per point of turmoil.

### Obstinance

See also:
Political movement
Obstinance represents civil disobedience, the formation of para-state structures, and refusal to comply with state institutions among excluded communities in certain regions. Each state has an obstinance value which gives scaling penalties to the state. Obstinance is distinct from turmoil – radicals of a certain culture may contribute to activism, but a pop does not need to be radical in order to contribute to obstinance.

[Cultural, Religious, and Pan-national movements](Political movement.md) can contribute to obstinance. When a movement reaches **50%** activism (**Protesting**) it starts contributing to obstinance. The amount of obstinance generated by a movement is based on the number of supporters in each state; obstinance equals the percentage of the state's [workforce](https://vic3.paradoxwikis.com/Workforce) that are members of a movement. Any applicable movement that is insurrectionist is also necessarily obstinate, weakening the state in the buildup to full rebellion. Multiple movements at the same time are capable of causing obstinance, in which case, the total amount of obstinance is the sum of each movement.

Obstinance can also be increased by foreign countries using the Support Separatism interaction, as that increases pop attraction and radicalism for separatist movements.

A state's level of obstinance scales from **0%** to **20%**, even if more of the state's workforce supports an obstinate movement.

Each percentage of obstinance in a state gives:

- **−0.05%** Tax collection (max **−10%**)
- **−0.05%** Assimilation (max **−10%**)
- **−0.05%** Conversion (max **−10%**)
- **−0.075%** Conscriptable battalions (max **−15%**)
- **−0.10%** Impact of [institutions](Institutions.md) (max **−20%**)

### Devastation

States that are occupied during war or damaged by [events](Events.md) gain devastation. Devastation in occupied states increases by **+0.1** each day. Additionally, each battle that occurs in a state add **0.1** devastation, multiplied by the formation's devastation modifiers. Each point of devastation adds **−1%** infrastructure, **−0.5%** construction efficiency, **−2%** migration attraction, **+1%** pop mortality, and **−0.25%** throughput.[2]

Unoccupied states lose **−0.025** devastation per day (**−9.125** per year). There is no way to change the rate of removing devastation, neither for good or bad.

Devastation applies to the entire state region, regardless of source.

### Harvest conditions

Main article:
Harvest condition
*Harvest conditions* gives a throughput bonus to various [agricultural buildings](List of buildings.md), either positive or negative. They initially affect all states in a state region, but each state receives its own duration and so may lose the harvest conditions at different times. Additionally, each state has a different impact from the harvest condition.

### Food security

See also:
Needs
,
Pops
*Food security* represents how easily pops in a given state can afford their basic food needs. It is primarily determined by supply of food goods, but also by their price. Food Security is a value between 0 and 100%, where at 0% the pop is in a state of severe starvation and at 100% the pop has full and easy access to all the food it requires. What determines a Pop’s food security is mainly a combination of two factors:

- How much the Basic Food Pop Need is in shortage in the state in question
- How much money the pop is spending on Basic Food compared to their whole buy package at base price

*Example: Food Security starts at 100% and is reduced by the two values above. If a pop spends 70% of their income on Basic Foods, and food is also in a 20% shortage, the food security for the pop in question will be 100% - 70% - 20% = 10%.*

Additionally, the Emergency Relief [decree](https://vic3.paradoxwikis.com/Decree) increases food security by **5%**. Each level of Charity Hospitals increases food security by **2%**. Each level of Social Security increases food security by **2%** with Old Age Pension increasing it by an additional **1%** per level.

Pops with less than 40% food security are considered to be in *mild starvation*, while pops with less than 20% are considered to be in *severe starvation*. If more than 35% of a state's pop are in mild starvation and more than 15% are in severe starvation, that state is considered to be in a famine.

Starving POPs has a severely increased mortality and decreased birth rate. Famines is a primarily political classification, and thus don’t have any direct effects on your pops. It act as a starting point for narrative content surrounding famines and how to deal with them. Famines also act as a warning signal for the player. They tell you how long they’ve lasted, how many people are affected as well as estimations for how many deaths and unrealized births the famine has led to.

#### Starvation

Starving pops have a penalty to their birth rate and mortality, scaled by their food security.

- Mild starvation scales up to **−35%** birth rate and **+30%** mortality
- Severe starvation scales up to **−90%** birth rate and **+100%** mortality

### Pollution

Pollution is generated by most production methods and reduces the state's migration attraction and pops' standard of living and increases pop mortality. Heavy industry pollute the most, while agricultural pollute the least. Pollution impact changes daily by 0.255 in each state region towards the *pollution impact target* to the following formula:

Pollution impact target = Total pollution generation 50 + 1.5 ⋅ ⋅ Arable Land ⋅ ⋅ 1 255 {\displaystyle {\text{Pollution impact target}}={\dfrac {\text{Total pollution generation}}{50+1.5\cdot {\sqrt {\text{Arable Land}}}}}\cdot {\frac {1}{255}}} ![{\displaystyle {\text{Pollution impact target}}={\dfrac {\text{Total pollution generation}}{50+1.5\cdot {\sqrt {\text{Arable Land}}}}}\cdot {\frac {1}{255}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/7e8101452da56295469b45d9e710ffc14fd136a9)

Each **1%** of pollution impact has the following base effects:

- **−0.25%** migration attraction,
- **+0.5%** drought, flood, wildfire, and heatwave impact,
- **−0.03** standard of living,
- **+0.5%** mortality.

The effects on standard of living and mortality can be reduced by the Health System institution (**−10%** per level; **−15%** with Public Health Insurance) and the technology Modern Sewerage (**−10%**). State regions also have a minimum pollution target equal to 25% of the most polluted neighboring state region.

Pollution applies to the entire state region.

### Event modifiers

[Events](Events.md) and [journal entries](https://vic3.paradoxwikis.com/Journal_entries) can apply various modifiers to a state, providing various bonuses or maluses either temporarily or permanently.

### Decrees

Main article:
Decrees
**Decrees** are effects that can be applied to individual states to improve them in many ways. Multiple decrees can be used simultaneously on the same state, with the exception of the three decrees encouraging certain industries which are mutually exclusive. Nearly all decrees require a certain [technology](Technology.md) to have been researched in order to be used. Decrees can be applied either by right-clicking on a province or through the political lens.

Decrees cost a base of **100** [authority](https://vic3.paradoxwikis.com/Authority) each to be applied, except Emergency Relief which costs **50**. A ruler with the [character traits](https://vic3.paradoxwikis.com/Character_trait) *Ambitious* and *Imperious* reduces the cost of decrees by **−25%** and **−20%** respectively. Certain [events](Events.md) can also reduce the cost. Decree cost reductions are capped at a minimum **10%** of the base cost, even if modifiers would reduce the cost more.

### Slave states / Free states

Under Legacy Slavery, the country is divided into Free States and Slave States. In Free States, slavery is illegal and essentially functions exactly as if the country had the Slavery Banned law, while Slave States function as though they had the Slave Trade law with the notable exception that new slaves cannot be imported from abroad.

Free states can be turned into slave states either via [events](Events.md) or via implementing Slave Trade, which effectively turns all states into slave states.

Under Colonial Slavery, unincorporated states are treated as if they had the Debt Slavery law, while incorporated states are treated as free states.

## References

1. ↑ Discovered/reverse-engineered by gawquon of the unofficial converters team
2. ↑ See /Victoria 3/game/common/modifiers/00_static_modifiers.txt `state_region_devastation`

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | [Government](Government.md) • [Capacities](Capacity.md) • [Characters](Character.md) • [Decrees](Decrees.md) • [Institutions](Institutions.md) • [Laws](Laws.md) • [Technology](Technology.md) |
|---|---|

| Politics | [Elections](Elections.md) • [Ideology](Ideology.md) • [Interest group](Interest group.md) • [Political lobby](Political lobby.md) • [Political movement](Political movement.md) • [Political party](Political party.md) • [Revolution](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| Economy | [Buildings](Building.md) • [Goods](Goods.md) • [Harvest condition](Harvest condition.md) • [Infrastructure](Infrastructure.md) • [Market](Market.md) • [Production methods](https://vic3.paradoxwikis.com/Production_methods) • State • [Treasury](Treasury.md) |
|---|---|

| Diplomacy | [Diplomacy](Diplomacy.md) • [Diplomatic action](https://vic3.paradoxwikis.com/Diplomatic_action) • [Diplomatic play](Diplomatic play.md) • [Power bloc](Power bloc.md) • [Ranks](Rank.md) • [Subjects](Subject.md) • [Treaties](Treaty.md) |
|---|---|

| Warfare | [Warfare](Warfare overview.md) • [Land warfare](Land warfare.md) • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
