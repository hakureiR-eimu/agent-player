---
title: Profession
source: https://vic3.paradoxwikis.com/Profession
pageid: 1671
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
Recent employee changes in the steel mill building.
**Professions** reflect the types of jobs that [pops](Pops.md) carry out in the [buildings](Building.md) where they work. A pop's profession determines its social stratum and affects its base wage, what other professions it might qualify for, and particularly which political [interest groups](Interest group.md) it's prone to supporting. Investing in industries that provide job opportunities for the professions the player wants to encourage in their country is key to the "society building" gameplay of Victoria 3.

## Profession types

There are 15 pop professions (and an unemployed status). These professions are divided into *social classes* which belong to different strata depending on the *social hierarchy* in the country.

|  | Profession | Base SoL | Wage multiplier | Dependent income | Special |
|---|---|---|---|---|---|
|  | Academics | 10 | 4 | 0.5 | **+50%** Education access |
|  | Aristocrats | 20 | 5 | 0.0 | 20% Base workforce ratio 20% Base investment pool contribution Not paid wages outside government-funded buildings |
|  | Bureaucrats | 10 | 4 | 0.5 | 15% Base investment pool contribution +50% Education access |
|  | Capitalists | 20 | 5 | 0.0 | 30% Base investment pool contribution Not paid wages outside government-funded buildings |
|  | Clergymen | 10 | 3 | 0.5 | +50% Education access 20% Base investment pool contribution |
|  | Clerks | 7 | 1.5 | 0.5 | **+25%** Education access |
|  | Engineers | 10 | 3 | 0.5 | 15% Base investment pool contribution +25% Education access |
|  | Farmers | 10 | 2 | 0.5 | **10%** Base investment pool contribution |
|  | Laborers | 5 | 1 | 0.5 | Default pop type Can always be hired (i.e. no qualifications) |
|  | Machinists | 7 | 1.5 | 0.5 | **10%** Base investment pool contribution |
|  | Officers | 10 | 5 | 0.5 | Ignores employment proportionality +200% More political power [1] |
|  | Peasants | 5 | 0.2 | 0.25 | Loyalism/Radicalism from Standard of Living changes multiplied by ×0.01 [2] Consumption multiplied by ×0.05 before adding to state consumption Cannot become unemployed (changes to Laborers instead) Ignores employment proportionality |
|  | Servicemen | 7 | 1.5 | 0.5 | Can always be hired (i.e. no qualifications) Ignores employment proportionality +50% More political power [3] |
|  | Shopkeepers | 10 | 3 | 0.5 | **20%** Base investment pool contribution |
|  | Slaves | 1 | 0 | 0 | 50% Base workforce ratio Needs are purchased by workplace Cannot change profession or workplace Cannot migrate |

## Social hierarchies

*Social hierarchy* determines which professions or pops belong to which *social classes*, and the classes in turn to which *social strata*. There are currently three social hierarchies. Various effects and modifiers can be applied to each social class and strata, in addition to professions directly.

### Base Hierarchy

This is the default social hierarchy, which applies when no other social hierarchy does.

| Stratum | Lower | Middle | Upper |
|---|---|---|---|
| Class | Lower Class | Middle Class | Upper Class |
| Professions | Clerks Laborers Machinists Peasants Servicemen Slaves | Academics Bureaucrats Clergymen Engineers Farmers Officers Shopkeepers | Aristocrats Capitalists |

### British Indian Caste System

See also:
Caste Hegemony laws
In countries with this social hierarchy, Hindu pops with a South Asian Heritage culture use an alternate set of social classes, non-Hindu and non-South Asian Heritage pops use the Base Hierarchy. At the start of the game, this hierarchy is used only by [East India](East India.md) and the Princely States. Other countries can gain this hierarchy if they have a South Asian Heritage primary culture, 50% or more Hindu pops, and are a subject of [Great Britain](Great Britain.md). Countries with this hierarchy lose it if they have fewer than 10% Hindu pops.

| Stratum | Lower | Middle | Upper |  |  |
|---|---|---|---|---|---|
| Class | Dalit | Shudras | Vaishyas | Kshatriyas | Brahmins |
| Professions | Slaves | Laborers Machinists Servicemen Peasants | Clerks Farmers Shopkeepers | Aristocrats Capitalists Engineers Officers | Academics Bureaucrats Clergymen |

Countries with this hierarchy have an additional law group: *Caste Hegemony*

### Edo Status System

| Stratum | Lower | Middle | Upper |  |  |  |
|---|---|---|---|---|---|---|
| Class | Eta-Hinin | Chōnin | Hyakusho | Jisha | Lower Samurai | Upper Samurai |
| Professions | Slaves | Capitalists Clerks Engineers Machinists Shopkeepers | Farmers Laborers Peasants | Clergymen | Bureaucrats Servicemen | Academics Aristocrats Officers |

## Qualifications

List of potentially qualified engineers in the state of Lower Egypt.
Qualifications represent individuals' ability to occupy a specific profession, when they want to change. Each pop has a qualification level for each other type of profession. Qualifications are gained each month based on various factors in proportion to a pop's size, such that larger pops may gain many qualified individuals each month, while smaller pops may even take several months before a single individual gains qualification.[4] Qualifications can be lost either by individuals dying, changing to another pop, or through decay in some cases. When individuals in a pop change profession or otherwise change pops, they take their percentage of qualifications with them. Additionally, they take qualifications for their previous profession into their new profession.

Qualifications for each profession depend on a number of factors, often wealth and literacy, but current profession and [acceptance](Acceptance.md) play a role as well. The table below lists the factors to gain qualifications towards the list profession; *literacy* is the percentage literacy rate of the pop which is converted to a decimal for qualifications; wealth is the base standard of living of the pop, before any modifiers affecting standard of living. The modifier factors only apply when gaining qualifications, not if they are decaying. Additionally, Universities provide an additional boost to qualification gains, based on their production method and throughput.

| Profession | Base qualification factor | Modifier factors |
|---|---|---|
| Academics | If above 20% literacy, +(Literacy−20%)×20 +Wealth/10 −1 otherwise | ×5 is Aristocrats or Clerks ×0.1 has less than +60 cultural acceptance ×0 is Peasants under Serfdom |
| Aristocrats | If 15 wealth or higher, +(Wealth−14)/20 +(Wealth-20)/5 (min +0) ×(0.5+Literacy/2) −2 otherwise | ×2 is Bureaucrats ×3 is Officers ×5 is Farmers or Clergymen ×0.1 has less than +60 cultural acceptance ×0 is Peasants under Serfdom |
| Bureaucrats | If above 20% literacy, +(Literacy−20%)×20 −1 otherwise | ×2 is Full Acceptance ×1.5 is Second-class Citizen ×5 is Clerks or Clergymen ×0.1 has less than +60 cultural acceptance ×0 is Peasants under Serfdom |
| Capitalists | If above 10 wealth, +(Wealth−10)/5 +Literacy×2 −2 otherwise | ×5 is Engineers or Shopkeepers ×0.1 has less than +60 cultural acceptance ×0 is Peasants under Serfdom |
| Clergymen | If above 20% literacy, +(Literacy−20%)×20 −1 otherwise | ×5 is Academics or Aristocrats ×0.5 under Total Separation ×0.2 has less than +15 religious acceptance ×0.1 is Atheist ×0.1 is Peasants under Serfdom |
| Clerks | +Literacy×20 | ×2 is Laborers ×0.1 is Peasants under Serfdom |
| Engineers | If above 20% literacy, +(Literacy−20%)×10 +Wealth/20 −2 otherwise | ×5 is Machinists ×4 is Clerks ×0 is Peasants under Serfdom |
| Farmers | If above 10 wealth, +Wealth/2 (max +15) −2 otherwise | ×2 is Laborers or Peasants ×0.2 is Peasants under Serfdom |
| Laborers | N/A | N/A |
| Machinists | +(Literacy-10%)×20 (min +0) | ×2 is Laborers ×0.05 is Peasants under Serfdom |
| Officers | If above +60 cultural acceptance or Servicemen, +(Literacy-20%)×10 (min +0) +0 otherwise | ×5 is Aristocrats ×5 is deployed Servicemen ×0.1 is under Peasant Levies and not Aristocrats ×0 is Peasants under Serfdom |
| Peasants | N/A | N/A |
| Shopkeepers | +Wealth−5 (min +0) | ×5 is Clerks ×4 is Farmers ×0 is Peasants under Serfdom |
| Servicemen | Minimum **+20** cultural acceptance | N/A |
| Slaves | N/A | N/A |

## Job satisfaction

All pops have a job satisfaction score which represents their willingness to find new work. Pops with a positive job satisfaction are less likely to change workplaces or migrate, and pops with negative satisfaction are more likely to do so.

| Source | Amount |
|---|---|
| Base | **−130** |
| Employed | **+100** |
| Employed in government building | **+50** |
| Recently hired | **+1000** |
| Income is above expenses | **+1000** |
| Income is below expenses | **−100** |
| Per difference between standard of living and: Expected standard of living Average state standard of living for strata Average country standard of living for strata | — ±3 ±2 ±1 |
| Per percentage above or below [normal wage](Vickypedia.md) | **±1** |
| Per percentage qualification for higher strata | **−1** |
| Dividends base Multiplied by percentage ratio compared to wages Dividends min Dividends max | +50 — +0 +250 |

## Hiring process

Individuals are hired for available jobs based on their current profession as well as any profession they are qualified for. Pops which cannot be hired by any building are *unemployed*. Buildings cannot hire pops who do not have the qualifications for the profession in question.

Except for unemployed pops, in order to move to another building a member of a pop must be offered at least a **10%** higher wage than the wage they are currently getting from their current employment. If the new position is a different profession, they must also be qualified for that profession.

Professions are kept (roughly) proportional, so for example, a building cannot hire a full slate of laborers unless it can also hire at least 90% of each of the other professions it requires[5]. Equivalently, if a building would lose a large chunk of its e.g. machinists, it must start firing all other professions until the proportion fits again. Certain buildings are allowed to ignore proportional hiring, namely, ownership buildings. Certain professions also ignore proportionality, namely peasants, officers, and servicemen.

Buildings can be subsidized (depending on the current *Economic System* law) to prevent pops from being fired due to lack of profit.

### Wages

The base wage is an absolute crucial value, as it dictates how much money the employed workers receive – and therefore get to spend, how high the SoL is, and thereby also affect migration attraction, how much money is made as a profit, how much the produced goods costs.

Each building has a *base wage*, which is multiplied by each profession's wage multiplier. Thus, with a base wage of £1, a building pays its laborers £1, its machinists £1.5, its engineers £3, etc. As a building can only adjust its base wage, all professions maintain the same ratio. Additionally, pops may be paid more or less based on their [acceptance status](Acceptance.md) depending on which *Citizenship* and *Church and State* laws are enacted.

Buildings raise their base wage primarily to attract employees when it cannot otherwise fill empty positions. Very profitable buildings may also raise wages if the employees are below the expected standard of living as long as they are accepted; conversely, unprofitable and moderately profitable buildings decrease wages to restore profitability. Thus states with a large, well-qualified population tend to have lower wages, at least until the buildings in the state have employed all of the pops. States with a limited number of qualified workers have higher wages on average.

The country-wide average of base wages in incorporated states is called the *normal wage*. This is used as the base wage of government-funded buildings as well as the baseline for welfare payments and minimum wage.

It is perfectly possible, that

- a good is in high demand,
- there are ample buildings to produce it,
- there are enough qualified workers (even unemployed ones),

and yet the building is not hiring, because the base wage is too high. In such a situation, the player can either wait until equilibrium is achieved again automatically, which can take a long time, or choose to subsidize the building, which can be expensive and does not solve the underlying issue.

## References

1. ↑ Inherent ×3 multiplier
2. ↑ `sol_change_impact` in `Victoria 3\game\common\pop_types\peasants.txt` override `DEFAULT_SOL_CHANGE_IMPACT_FACTOR`, it don't apply on top of it.
3. ↑ Inherent ×1.5 multiplier
4. ↑ See /Victoria 3/game/common/defines/00_defines.txt `QUALIFICATIONS_UPDATE_FACTOR`
5. ↑ See /Victoria 3/game/common/defines/00_defines.txt `EMPLOYMENT_PROPORTIONALITY_LIMIT`

- To update page content see reference files in folder /Victoria 3/game/common/pop_types:
  - Each profession has its own `txt` file (named after the profession).

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • Professions • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
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
