---
title: Government
source: https://vic3.paradoxwikis.com/Government
pageid: 4725
categories: [1.13, Politics, Game_concepts]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

For government flavor names and conditions of transfer of power, see
Government type
The numbers in green refer to the number of alternative laws currently available to be enacted in that sub-category.
The **government** is composed of the [interest groups](Interest group.md) in power. The interest groups in government generally determine which [laws](Laws.md) can be enacted. All interest groups not in government make up the *opposition*. All eight interest groups can potentially be put in government together, although this is inadvisable due to the low legitimacy that would result.

*Marginalized* interest groups cannot be added to the government. Similarly, *insurrectionary* interest groups supporting a [revolutionary movement](Political movement.md) cannot be added to the government.

Removing an interest group from the government radicalizes **25%** of [pops](Pops.md) supporting that interest group, except immediately following an election.

## Enacting laws

At the checkpoint, one of the 4 options (success, debate, advance, stall) happens.
Main article:
Laws
To begin enacting a law, an interest group in the current government or the ruler needs to be in favor of the proposed law, or there has to be an active movement supporting the law. An *illegitimate* government (below **25** legitimacy) cannot pass any laws except those supported by a movement; if an enactment process has already started, it makes no progress while the government is illegitimate.

## Legitimacy

*Legitimacy* is the measure of the balance of power of interest groups that compose the government. It ranges from 0 to 100, divided into levels at certain thresholds. Each level has discrete benefits or penalties, as well as scaling pop loyalty effects.

| Level | Value | Enactment | Opposition approval | Radicals and Loyalists |  |  |
|---|---|---|---|---|---|---|
| Able | Time | from Movements | per Month |  |  |  |
| Illegitimate | **25<** | ![Only with a supporting political movement](/images/thumb/c/cb/Warning.png/24px-Warning.png) |  | **−3** | **+50%** | **+3.0%** – **+1.56%** |
| Unacceptable | **25-49** | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | **+50%** | **−2** | **+25%** | **+1.5%** – **+0.06%** |
| Contested | **50-74** | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |  | **−1** |  |  |
| Legitimate | **75-89** | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |  |  | **+25%** | **+0.05%** – **+0.75%** |
| Righteous | **90+** | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | **−25%** |  | **+33%** | **+0.80%** – **+1.30%** |

### Legitimacy sources

| Power Structure | Economy | Human Rights |  |  |  |
|---|---|---|---|---|---|
| Governance Principles | ×2 | Economic System | ×2 | Free Speech | ×0.5 |
| Distribution of Power | ×2 | Trade Policy | ×1 | Labor Rights | ×0.5 |
| Citizenship | ×1 | Taxation | ×0.5 | Children's Rights | ×0.25 |
| Caste Hegemony | ×0.5 | Land Reform | ×1 | Rights of Women | ×0.5 |
| Church and State | ×1 | Colonization | ×0 | Welfare | ×0.25 |
| Bureaucracy | ×0.25 | Policing | ×0.25 | Migration | ×0.25 |
| Army Model | ×0.25 | Education System | ×0.25 | Slavery | ×2 |
| Navy Model | ×0.25 | Health System | ×0.25 | Labor Associations | ×0.5 |
| Internal Security | ×0.5 |  |  |  |  |
| Edo Status System | ×0.5 |  |  |  |  |

Legitimacy comes primarily from the total clout of the interest groups in government and – in countries with elections – from their vote share in the last election. Certain laws, such as Monarchy, also add legitimacy from including the ruler's interest group in government. Legitimacy is reduced by **20** for each interest group or party in government above the *government size allowance*, which has a base of **1**. Legitimacy is also reduced when the interest groups in government are ideologically opposed on law preferences, scaling by how opposed they are. For each law, a base penalty of **−5** is added per step of difference in stances. Only the largest difference is counted, so if three or more interest groups are in government, there is no double penalty for lesser or equal disagreements. Some law groups have multipliers to the ideology penalty, either increasing or decreasing the effect of differences. The final values are always shown as rounded values, so 2.5 displays as 3, 1.25 as 1, and so on.

The Governance Principles and Distribution of Power laws determine most legitimacy effects; however, tax levels and event modifiers can also add bonuses or penalties to legitimacy, either directly or one of the sources.

| Law | Legitimacy from | Government size allowance | Ideology penalty |  |  |
|---|---|---|---|---|---|
| Clout | Votes | Ruler |  |  |  |
| Monarchy | — | — | **+20** | — | **+10%** |
| Presidential Republic | — | **+10** | **+10** | — | **+20%** |
| Parliamentary Republic | — | **+20** | — | **+1** | — |
| Theocracy | — | — | **+20** | — | **+10%** |
| Council Republic | — | **+10** | — | **+1** | **−10%** |
| Corporate State | — | — | — | **+2** | **−25%** |
| Social Monarchy | — | — | **+10** | **+1** | **−10%** |

| Law | Legitimacy from | Government size allowance | Ideology penalty |  |  |
|---|---|---|---|---|---|
| Clout | Votes | Ruler |  |  |  |
| Autocracy | **+120** | — | **+30** | — | **+50%** |
| Oligarchy | **+120** | — | **+10** | **+2** | **−10%** |
| Technocracy | **+120** | — | **+10** | **+2** | **−10%** |
| Anarchy | **+100** | — | — | **+2** | — |
| Landed Voting | **+100** | **+40** | — | **+1** | **+20%** |
| Wealth Voting | **+75** | **+65** | — | **+1** | **+20%** |
| Census Suffrage | **+55** | **+85** | — | **+1** | **+10%** |
| Universal Suffrage | **+25** | **+110** | — | **+1** | — |
| Single-Party State | — | **+100** | — | — | **−25%** |

The legitimacy from clout and from votes is divided proportionally across interest groups and parties. For example, in a country with Oligarchy, if its government interest groups have **50%** of the total clout, then the legitimacy from clout would equal **+60**. Similarly, in a country with Universal Suffrage, if its government parties have **50%** of the total votes, then the legitimacy from votes would equal **+55**.

Subjects under 75 legitimacy can request or be granted the diplomatic pact Support Regime, which gives the subject **+20** legitimacy at the cost of **−10** legitimacy for the overlord.

## Reforming government

Government can be reformed at any time by adding or removing interest groups. Any group in opposition can be added freely, but removing a group in government radicalizes **25%** of its member pops. In countries with voting, elections provide an opportunity to reform the government without angering interest groups' members – the first reform within six months after an election does not radicalize members of interest groups removed from government.

There is a quick reform option which presents the three highest legitimacy options available, but note that this does not include the current government nor does it take radicalization from removing interest groups into account. Otherwise, all possible combinations of non-marginalized interest groups and parties can be freely explored before confirming or resetting any changes.

## Political parties and elections

Main articles:
Political party
,
Elections
If the [Distribution of Power law](Power structure laws.md) enables voting, interest groups may found and join parties. Parties cannot be split between government and opposition when reforming the government: adding a party to the government adds all interest groups in the party; likewise for removing a party from government. A political party counts as a single interest group for the purposes of government size, regardless of how many interest groups have joined that party. Secondary interest groups in a partyAll except the highest clout interest group in the party also have a **−50%** reduced opposing ideology penalty to legitimacy.

With voting also come elections. Elections occur every four years, with a six-month campaigning period leading up to the actual election. An election (with the campaign) also occurs when replacing a non-voting law with a voting law.

## References

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | Government • [Capacities](Capacity.md) • [Characters](Character.md) • [Decrees](Decrees.md) • [Institutions](Institutions.md) • [Laws](Laws.md) • [Technology](Technology.md) |
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
