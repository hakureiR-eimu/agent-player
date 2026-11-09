---
title: Elections
source: https://vic3.paradoxwikis.com/Elections
pageid: 1633
categories: [1.13, Politics]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

See also:
Government
,
Political party
Election campaign summary showing the latest poll status and the involved parties.
**Elections** happen in countries where the [power structure laws](Power structure laws.md) allow them. Elections occur every 4 years with the election campaign beginning 6 months prior to the election date. It is not possible to call a snap electionExcept by scripted effect; however, when voting is introduced, an election campaign immediately begins.

Elections can be a powerful force for political change but also a source of government instability as [interest groups](https://vic3.paradoxwikis.com/Interest_groups) may change from one [political party](Political party.md) to another.

## Election process

At the beginning of the campaign, each [political party](Political party.md) is assigned a momentum value – a measure of the success of their campaign – which is a major factor in determining how many votes each party garners on election day. During the campaign, momentum fluctuates for each of the running political parties and impacts the final result. Momentum is affected by chance, [events](Events.md), and the popularity of [interest group](Interest group.md) leaders. Momentum is reset on each election cycle with no impact from previous elections. The main way the player can influence a party's momentum is through events.

When the election campaign ends, the votes come in and the results are set in place until the next election. Interest groups receive additional political strength from their party's votes, which is often a major factor determining the government's legitimacy and therefore its effectiveness. Elections do not actually change the makeup of the government; however, the post-election strength of the interest groups and parties may cause a major shift in legitimacy. Within six months after the election, the [government](Government.md) can be reformed once for free without radicalizing supporters of ousted interest groups. After six months or after the first reform, any further reforms cause radicalization as usual.

In countries with [presidential elective transfer of power](Government type.md), the leader of the interest group with the most clout becomes the ruler at each election, whether that interest group is in government or in opposition.

### Party affiliation

See also:
Political party
Each time an election campaign starts, interest groups may change parties or found new ones. If an interest group in opposition wants to join a party in government, or if an interest group in government wants to join a party in opposition, the interest group must wait until the next government reform, with the message *"Will join [Party] on next reform"*. While any interest group wants to join a party, any government reform must account for that, and only government reforms which unite all parties are valid. Interest groups may also change parties due to an event or other effect.

Additionally, once new parties are formed, the legitimacy penalty from differing views is reduced as the interest group with the most individual clout is considered the party's whip; the stances of all other interest groups in the party count half as much.[1]

Interest groups that are not affiliated with a party – including those marked as "will join [Party] on next reform" – cannot participate in elections and thus their pops typically do not vote, except those swayed by parties' momentum. For this reason, it can be advantageous to reform the government during the election campaign so that interest groups join their new parties in order to gain more votes for those parties, or conversely not reform in order to weaken those parties by preventing them from gaining those potential votes.

### Clout impact

While elections and votes provide a major source of clout, all interest groups still receive clout from their affiliated pops as normal. Thus, even if a single party receives most or all of the votes in an election, other parties or unaffiliated interest groups retain at least some clout.

## Voting laws

The following laws enable voting in a country – thus elections and parties – and determine how much power votes have and which pops can vote:

| Law | Voting effects |
|---|---|
| Landed Voting | +40 Legitimacy from votes +100 Political strength from Aristocrats' votes +50 Political strength from Capitalists' votes +50 Political strength from Clergymen's votes +50 Political strength from Officers' votes All other professions are disenfranchised |
| Wealth Voting | +65 Legitimacy from votes +50 Political strength from votes +20 Wealth threshold for voting |
| Census Suffrage | +85 Legitimacy from votes +50 Political strength from votes, multiplied by pop literacy +10 Wealth threshold for voting |
| Universal Suffrage | +110 Legitimacy from votes +50 Political strength from votes |
| Single-Party State | +100 Legitimacy from votes +50 Political strength from votes |

Additionally, the laws Presidential Republic, Parliamentary Republic, and Council Republic slightly increase the amount of legitimacy from votes.

All of these laws are compatible with any of the [Governance Principles](Power structure laws.md) laws. For instance, a country with the Monarchy law could be an absolute monarchy with no voting system at all, or it could have universal suffrage. Likewise, a "republic" might very well be an Autocracy.

Note that number of votes cast in an election is determined by "political strength from votes". For example, with Universal Suffrage, each voter casts 50 votes, though they cannot split their vote; this is likely many times more than the total population of the country. This system of voting is more impactful with Landed Voting or Census Suffrage where the strength from votes is not equal for all eligible voters.

### Disenfranchisement

There are three factors aside from laws that prevent pops from voting:

- *Discrimination* – Citizenship laws determine which acceptance statuses can vote in elections, and may further affect the vote strength of each acceptance status.
- *Living in an unincorporated state* – Only pops living in incorporated states can participate in elections. For example, pops living in a growing colony cannot vote.
- *Politically unaligned pops* – Regardless of whether they are otherwise eligible politically unaligned pops do not vote. These pops are not part of any interest group, and tend to have low literacy or standard of living. For instance, peasants working in subsistence farms are often politically unaligned.
  - This category also includes dependents. Dependents can become politically active with either Women's Suffrage or Old Age Pension.

## References

1. ↑ `country_party_whip_impact_add = 0.5` in /Victoria 3/game/common/static_modifiers/00_code_static_modifiers.txt base_values

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | [Government](Government.md) • [Capacities](Capacity.md) • [Characters](Character.md) • [Decrees](Decrees.md) • [Institutions](Institutions.md) • [Laws](Laws.md) • [Technology](Technology.md) |
|---|---|

| Politics | Elections • [Ideology](Ideology.md) • [Interest group](Interest group.md) • [Political lobby](Political lobby.md) • [Political movement](Political movement.md) • [Political party](Political party.md) • [Revolution](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| Economy | [Buildings](Building.md) • [Goods](Goods.md) • [Harvest condition](Harvest condition.md) • [Infrastructure](Infrastructure.md) • [Market](Market.md) • [Production methods](https://vic3.paradoxwikis.com/Production_methods) • [State](State.md) • [Treasury](Treasury.md) |
|---|---|

| Diplomacy | [Diplomacy](Diplomacy.md) • [Diplomatic action](https://vic3.paradoxwikis.com/Diplomatic_action) • [Diplomatic play](Diplomatic play.md) • [Power bloc](Power bloc.md) • [Ranks](Rank.md) • [Subjects](Subject.md) • [Treaties](Treaty.md) |
|---|---|

| Warfare | [Warfare](Warfare overview.md) • [Land warfare](Land warfare.md) • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
