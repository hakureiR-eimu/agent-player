---
title: Migration
source: https://vic3.paradoxwikis.com/Migration
pageid: 2986
categories: [1.13, Game_concepts]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

Pops
Culture
•
Religion
Profession
•
Qualifications
Standard of Living
•
Needs
Migration
Migration change and migration attraction on the state population screen.
**Migration** is the movement of [pops](Pops.md) between [states](https://vic3.paradoxwikis.com/States). There are two types of migration in Victoria 3: *intra-market migration* and *mass migration*.

## Migration types

There are two types of migration in Victoria 3:

- *Intra-market migration* is the movement of pops between two states that are part of the same [market](Market.md).

- *Mass migration* is a mechanic that models the migration of large amounts of people to places such as the USA, Brazil, and Australia in the 19th century. Mass migration can happen when a particular culture experiences turmoil, which is a product of having a large number of radicalized pops.

## Migration attraction

Migration attraction represents how likely a pop is to move to or from a state. It is a summary of various factors including available jobs and average standard of living. Pops generally immigrate to states with the highest attraction and emigrate from states with the lowest attraction.

Migration attraction is calculated according to the following factors:

| Reason | Factor |
|---|---|
| Available non-subsistence jobs, as a % of employed non-subsistence pops | **+30** per 100%, max **+30** |
| Available subsistence jobs, as a % of employed non-subsistence pops | **+2** per 100%, max **+10** |
| Unemployed pops, as a % of employed pops | **−50** per 100%, max **−50** |

Additionally, many [state traits](State traits.md) and other modifiers affect migration attraction, often multiplying the sum of the above factors.

Migration attraction applies to both intra-market migration and mass migration.

For intra-market migration only, migration attraction of a target state is increased for a particular pop by **+50%** if it is discriminated in its current state and would be accepted in the target state; similarly, the attraction is increased by **+20%** if the target state is a cultural homeland for the pop.

## Migration law

See also:
Human rights laws#Migration
The [Migration law](Human rights laws.md) of a country determines whether a pop can migrate to or from other countries, determined by base cultural [acceptance](Acceptance.md):

| Law | Valid migrant status |
|---|---|
| No Migration Controls | Any acceptance |
| Migration Controls | At least 60 cultural acceptance |
| Closed Borders | No acceptance |

The [Land Reform law](Economy laws.md) also affects the migration of peasants:

| Law | Peasants migration |
|---|---|
| Serfdom | None |
| Tenant Farmers | Mass migration only |
| All others | Any |

If a pop is moving between countries, the migration laws of both countries are considered. Religious discrimination does not affect migration ability, though it might affect a pop's choice of target.

## Intra-market migration

Most migration is intra-market migration, where pops migrate between states within the same market. There are several thresholds that must be met in order for a pop to migrate within a market. These include the presence of a cultural community in the target, a pop's *migration desire*, and its discrimination and the migration laws in both the source and target.

### Migration desire

| Status | Score | Migration desire |
|---|---|---|
| Violent Hostility | 0-19 | 100 |
| Cultural Erasure | 20-39 | 100 |
| Open Prejudice | 40-59 | 50 |
| Second-class Citizen | 60-79 | 20 |
| Full Acceptance | 80-100 | 0 |

A pop's migration desire determines how likely a pop is to migrate. It is based on the inverse of the pop's [job satisfaction](https://vic3.paradoxwikis.com/Job_satisfaction) and increased by discriminated statuses. Thus highly satisfied pops are very unlikely to migrate, and less accepted pops are more likely to migrate than more accepted pops.

### Cultural communities

In order for a pop to migrate within a market, the target state must have a matching cultural community. Cultural communities are present in each state that contains one or more pops of that culture. Additionally, each month, a new cultural community can appear in any state as long as that culture is present in the market. If a state has no pops of a given culture, that cultural community disappears after three weeks.[1]

The chance for a new cultural community to appear in a state has the following factors. This chance is calculated individually for each culture present in the market. If a state has 50 or more devastation, 60 or more turmoil, or is isolated, it cannot gain a new cultural community. The maximum chance is 4% for each culture for each state.

| Condition | Factor |
|---|---|
| Base | +0.1% |
| State has a Port building | +0.1% |
| State has a Trade Center building | +0.1% |
| State is coastal | +0.1% |
| State has more than 20 unused arable land | +0.1% |
| State has a " river" state trait Not including the Angara, Don, Irtysh, Kapuas, Missouri, Sarawak, St. Lawrence, or Yenisei rivers | +0.1% |
| State has Greener Grass CampaignCost: 100Greener Grass Campaign Promote the state as a desirable place to migrate toRequires: RomanticismState is not isolatedModifiers:+20 Migration attraction +25% Migration attraction decree | +0.5% |
| State is a colony | +0.5% |
| Condition | Factor |
| State is capital | ×1.1 |
| Culture is a primary culture | ×2.5 |
| Has any of:Good Soils Natural Harbors London Docklands New York Harbor Halifax Harbor Newark Harbor | ×1.2 |
| State has Violent SuppressionCost: 100Violent Suppression Use the nation's national guard to control the angry mobsRequires: Standing ArmyOwner does not have the law Guaranteed Liberties Turmoil in state is at least 25%Modifiers: −50% State penalties from turmoil +2% Mortality per turmoil decree | ×0.5 |
| State has 20 or more devastation | ×0.5 |
| State has 30 or more turmoil | ×0.5 |
| State has 10% or more unemployment | ×0.5 |
| Country is at war | ×0.5 |
| State may join a revolution or secession | ×0.5 |
| State has a shortage | ×0.8 |
| ×(Market access as decimal) |  |
| State is a slave state Culture does not share a heritage with any primary culture | ×0.1 |
| State has Malaria Country has not researched Quinine | ×0.5 |
| State has Severe Malaria Country has not researched Malaria Prevention | ×0.3 |
| Culture has Violent Hostility status in country | ×0.1 |
| Culture has Cultural Erasure status in country | ×0.3 |
| Culture has Open Prejudice status in country | ×0.5 |
| Culture has Second-Class Citizen status in country | ×0.7 |
| State has 5 or more cultural communities | ×0.5 |
| State has 10 or more cultural communities | ×0.3 |
| State has 15 or more cultural communities | ×0.1 |

When a new cultural community first appears, it adds a **−30** local acceptance penalty to its culture. This penalty decays each month by **+25**.

### Target and size

In order for a state to be selected for immigration, it must have at least **25%** higher migration attraction than the average in the entire market. Similarly, for a state to be selected for emigration, it must have at least **25%** lower migration attraction than the average in the entire market. Finally, all eligible states with at least **75%** of the migration attraction of the most attractive state receive some immigration. Pops do not migrate if their current state and target state are within 5 points of migration attraction.

Once it is determined that one or more pops will migrate, the number of individuals that migrate is 5 times the difference in migration attraction plus 1 more per point per 100K population in a state. For any given pop, at least 5% of that pop must migrate or no part of the pop does.

Each week a state that experiences migration can have no more than 500 + ( 5 ∗ ∗ Infrastructure ) {\displaystyle 500+(5*{\text{Infrastructure}})} ![{\displaystyle 500+(5*{\text{Infrastructure}})}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/04609c291a30b61c723c54ca5f10ea82584e0e01) individuals migrate in or out of the state. Additionally, no more than 0.5% of a state's population can emigrate per week. These limits are scaled down in states with less than 100K population to zero emigration below 20K population. Finally, 5% of the unemployment size of a state is added to its max emigration and removed its max immigration.

Depending on relative migration attraction between states in a country, the same state may receive immigrants and send out emigrants in the same week.

### Power blocs

Intra-market migration can occur within power blocs that are Trade Leagues or have the principle Market Unification II or Freedom of Movement III.

The Freedom of Movement principle also increases the amount of migration by **+25%** (from tier 1) and the attraction for mass migration by **+50%** (from tier 2).

## Mass migration

A *Mass Migration* occurs when a culture is radical enough for pops to leave their homeland. Unlike intra-market migration, mass migrations are always between different countries and they often occur between markets, though they can occur within a market as well. Assuming Migration laws do not prevent their movement, pops of that culture migrate over a period of 12 months and the same culture cannot mass migrate from the same country again for another 48 months. A country is eligible to become the source of a mass migration if it has:

- at least 15% turmoil in a culture whose homelands its owns
- at least 100,000 potential emigrants

Pops that do not have a cultural homeland (such as Ashkenazi) can never mass migrate.

The chance of a mass migration starting each week for each combination of eligible culture and country is 2% times the cultural turmoil plus another 0.2% per point of average standard of living for the culture below 10 and finally plus another 1% per point of average SoL for the culture below 5. For example, a culture with 30% turmoil has a 60% chance of starting a mass migration, if the average standard of living for that culture is 4, that rises to 62.2%.

### Migration target

Once a country meets the origin requirements, the mass migration searches for an eligible migration target state. A state is eligible if:

- it is incorporated
- its owner has 30% or less turmoil in the migrating culture
- it has 10 or more arable land
- it has at least 70% market access

Each country has an attraction score which equals the average migration attraction of all its eligible states. Countries with fewer than 4 eligible states receive a penalty of 20% for each fewer state, up to 60% penalty for a country with only one eligible state. A country is semi-randomly chosen, with higher attraction scores more likely to be chosen, then a semi-random eligible state within that country is chosen as the migration target. The source and target countries must be trading with each other on the [world market](https://vic3.paradoxwikis.com/World_market).

The culture affected by mass migration must also have at least 30 acceptance in the target country under its Citizenship laws. The culture also seeks to increase its acceptance by at least 10 from its current country, but may mass migrate for less if attraction is high enough. Increased acceptance in the target can result in up to five times as much migration, depending on the ratio of acceptance between origin and target.

Pops that mass migrate arrive either in the migration target or its neighboring states. With each neighboring state receiving approximately half as many individuals as the main target, scaled by the various factors.

## Slavery

Slaves are never allowed to migrate, even with No Migration Controls. Countries with the Slave Trade law can 'import' slaves, even when they have Closed Borders. These newly imported slaves can arrive in any state with available jobs that can be filled by slaves.

## References

1. ↑ `CULTURAL_COMMUNITY_LINGER_TIME_WEEKS` in /Victoria 3/game/common/defines/00_defines.txt

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • Migration • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
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

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
