---
title: Institutions
source: https://vic3.paradoxwikis.com/Institutions
pageid: 1635
categories: [1.13, Politics]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

Institution summary tab showing the institutions' level, the per-level-cost, and the total cost.
Institutions represent certain government services, offices, or departments. These include things like schools and workplace safety controls, as well as colonization, police, and poorhouses.

Institutions are established or abolished by [laws](Laws.md). Each institution can vary in cost and effect from level 1 to 5. When an institution is initially established by law, it is automatically set to level 1 and can only be removed by abolishing the law. The level of an institution multiplies both the effect and [bureaucracy](https://vic3.paradoxwikis.com/Bureaucracy) cost; thus a level 3 institution has three times the effect and cost as a level 1 institution. While [interest groups](https://vic3.paradoxwikis.com/Interest_groups) may take a stance on the laws establishing an institution, they never have an opinion on the magnitude of the institution itself. Laws may also add additional effects to an institution or increase the maximum possible investment.

Institutions only apply their effects, and bureaucracy cost, to incorporated states.

## Institution effects

There are seven institutions, most of which have a base effect. All institutions require a law which enables it; most laws enabling an institution also add additional effects per level and some laws enabling an institution have other effects related to the institution, such as increasing the max level of the institution or adding a related national effect.

For example, the home affairs institution's base effect reduces revolution and secession progression speed. If the current law is National Guard, then each level also increases conscription and reduces [political movement](Political movement.md) radicalism; while if the law is Guaranteed Liberties, each level instead also reduces radicals and increases loyalists from movements.

Some [power bloc](Power bloc.md) principles also modify institution effects.

| Institution | Base modifiers | Enabling law category | Additional Levels | Description |
|---|---|---|---|---|
| Colonial affairs | **+10%** Colonial growth generation | [Colonization](Economy laws.md) | [Colonization](Society technology.md) (2), [Quinine](Society technology.md), [Civilizing Mission](Society technology.md), [Malaria Prevention](Society technology.md) | The office handling the management of foreign colonial holdings. |
| Education | — | [Education system](Economy laws.md) | Rationalism , Empiricism , Dialectics Children's Rights laws (1-2) | The nation's school system, ensuring a growth in population literacy. |
| Health System | — | [Health system](Economy laws.md) | [Medical Degrees](Society technology.md), [Pharmaceuticals](Society technology.md), [Quinine](Society technology.md), [Malaria Prevention](Society technology.md), [Antibiotics](Society technology.md) | Keeping the spread of disease at bay. |
| Home affairs | **−10%** Revolution/Secession progression speed | [Internal security](Power structure laws.md) | [Centralization](Society technology.md), [Central Archives](Society technology.md), [Identification Documents](Society technology.md), [Central Planning](Society technology.md), [Mass Surveillance](Society technology.md) | Tasked with obstructing citizen revolts. |
| Law enforcement | **−10%** State penalties from turmoil | [Policing](Economy laws.md) | Bureaucracy (2), Law Enforcement Policing laws (2) | The national police force enforcing the nation's laws. |
| Social Security | +20% Welfare payments +2% Food security | [Welfare](Human rights laws.md) | [Democracy](Society technology.md) (2), [Egalitarianism](Society technology.md), [Human Rights](Society technology.md), [Feminism](Society technology.md) | A safety net for the old or infirm. |
| Workplace safety office | **−20%** Dangerous working conditions | [Labor rights](Human rights laws.md) | [Labor Movement](Society technology.md) (3), [Socialism](Society technology.md) (2) | The ministry controlling that labor laws are followed. |

## Institution levels

When an institution is enabled, the first level of the institution is automatically added, regardless of having sufficient [bureaucracy](https://vic3.paradoxwikis.com/Bureaucracy). The effects and cost of an institution are multiplied by its current level, so a level five institution has five times the effect and cost of a level one institution. Each institution has its own max level, based on enacted laws and researched technologies. Increasing the level of the institution, and thus its effects, requires both sufficient max institution level and sufficient available bureaucracy.

Increasing or decreasing an institution's level takes a base time of one year per level. During the implementation of another level, the bureaucracy cost changes proportionally over the year, but the desired effects only apply once the new level has been fully implemented. If available bureaucracy goes below 0 while increasing an institution's level, the institution pauses its increase until bureaucracy is positive again.

Each level of an institution costs a base of 1 bureaucracy per 100,000 population in incorporated states with a minimum cost of 10 bureaucracy, that is with less than 1 million pops in incorporated states. The law Elected Bureaucrats reduces the bureaucracy cost for all institutions by **−15%**.

Certain power bloc principles modify to time to change and cost of certain institutions.

## Strategy

### Colonial Affairs

Frontier Colonization is just a strictly worse law than Colonial Resettlement. The limits on where and how you can colonize is quite strict. The only reason to pick this is that it is not opposed by the Rural Folk, but instead endorsed meaning there is usually no actual opposition to this law.

Colonial Exploitation lowers wages and factory throughput in exchange for higher plantation and resource throughput in colonies. Since it is unlikely that it is beneficial to build any industry anyway, this is likely just a bonus to throughput.

### Education

Level 5 private and level 3 public schools cost the same total bureaucracy
Which education system is best depends largely on [Standard of living](Standard of living.md). Religious Schools is strictly worse than the other two. This is especially true late game because it cannot be increased past level 3. It does have its place though as it is easier to implement early in the game, both due to the typical early political situation with a strong Devout and weak/non-existent Trade Unions, Intelligentsia and Industrialists, the fact that it is the only option in countries with a State Religion, and the fact that it is unlocked by an earlier tech.

Private Schools or Public Schools can both be the best option, depending on circumstances. Private schools provide **0.5%** [education access](https://vic3.paradoxwikis.com/Education_access) per wealth per level, while public schools provide a flat **12.5%** to everyone per level. This means that for POPs with a [SoL](Standard of living.md) below 25, public schools provide more education per level, at 25 they are equivalent, and above 25 private schools provide more.

With an average SoL below 25, private schools can, however, still be better, as they are **40%** cheaper to implement, so it is possible to maintain a higher level for the same amount of Bureaucracy, assuming that bureaucracy is sparse and the current technologies allow another level. 3 levels of private school is **10%** cheaper than 2 levels of public schools, 4 levels of private school is **20%** cheaper than 3 levels of public school, and 5 levels of private school is **25%** cheaper than 4 levels of public school. In fact, level 5 private schools and level 3 public schools costs the exact same amount of bureaucracy.

Implementing 5 levels of private school compared to 3 levels of public school at the same cost is better for POPs with a SoL between 16 and 24, equivalent for POPs with a SoL at 15 and worse for POPs with a SoL below 15.

### Workplace Safety

The only difference between Regulatory Bodies and Workers' Protections is that the latter increases the minimum wage. Raising the minimum wage should not be done accidentally. Furthermore, for countries following the path of socialism, one of the options in the *A World To Win* event instantly enacts Regulatory Bodies, making it possible to focus on other laws.

## References

1. To update institutions modifiers see reference file /Victoria 3/game/common/institutions/00_institutions.txt
2. To update institutions flavor text see reference file /Victoria 3/game/localization/english/institutions_l_english.yml:

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | [Government](Government.md) • [Capacities](Capacity.md) • [Characters](Character.md) • [Decrees](Decrees.md) • Institutions • [Laws](Laws.md) • [Technology](Technology.md) |
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
