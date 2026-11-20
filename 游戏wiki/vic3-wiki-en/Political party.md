---
title: Political party
source: https://vic3.paradoxwikis.com/Political_party
pageid: 1622
categories: [1.13, Politics]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

See also:
Government
,
Elections
An in-government political party and the opposition parties with some election details.
A **political party** is an alliance between [interest groups](Interest group.md). Parties appear only in countries that have [elections](Elections.md), adding a extra political factor when forming a government. Many countries have specific party names that reflect historical parties, such as the *Whigs* and *Tories* in [Great Britain](Great Britain.md).

Each political party acts as a bloc for the interest groups that comprise it; it is not possible to reform the government and split the interest groups in a party between the government and opposition. Additionally, all interest groups within a party gain clout from the votes cast for that party in the previous election.

## Party types

There are 12 archetypes for political parties that interest groups can join. Many of these parties are aligned primarily around a particular interest group's core ideologies, and other interest groups may join under the right circumstances. Other parties are aligned more strongly with leader ideologies that emerge throughout the game, such as the Communist Party and the Radical Party. The Revolutionary Party is a special case, only available to interest groups that are currently revolutionary.

At any given time, any combination of these parties may exist or none at all. Parties emerge and disband dynamically, so the political landscape can be very different between countries and playthroughs.

The following parties can emerge throughout the game:

- Agrarian Party
- Anarchist Society
- Communist Party
- Conservative Party
- Fascist Party
- Faith Party
- Free Trade Party
- Liberal Party
- Patriotic Party
- Radical Party
- Revolutionary Party
- Social Democratic Party

The different party types have no mechanical differences, other than influencing how and which interest groups may ally with others. For instance, the Liberal Party is the natural home of the Intelligentsia due to their liberal ideology, but the Intelligentsia may join other parties under various circumstances.

*Note:* Each of these parties has a variety of dynamic names based on national, cultural, and religious factors. For example, in [Great Britain](Great Britain.md) the Conservative Party is localized as the *Tory Party*, while in the [United States](https://vic3.paradoxwikis.com/USA) they are known as the *Democratic Party*. The Faith Party is often named after the country's state religion.

## Party mechanics

Political parties are tied to elections. Each time an election starts, all non-marginalized interest groups re-evaluate which party they wish to join, if any. Additionally, interest groups gain clout from the votes cast for their party in an election. Interest groups that are unaffiliated with a political party do not gain any clout from votes. Clout from votes is tied to parties specifically, which can cause a temporary loss of legitimacy when an election starts as parties may disband or even be replaced by "new" parties of the same members.

Interest groups can also change parties between elections due to events or other similar effects. The party that an interest group chooses is based on the attraction factors below.

The interest group with the most individual clout in each party is considered the party's *whip*; the stances of all other interest groups in the party count half as much for the ideology penalty to legitimacy.

### Bloc

Political parties must be added or removed from government as a single bloc, which forces strategic decisions about the makeup of the government. For example, the Liberal party may contain both the Intelligentsia and the Industrialists, who both back plans to move toward a free market economy but diverge on the issue of child labor.

If an interest group in opposition decides that it wants to join a party currently in government (or vice versa), the interest group leaves its old party – if any – and is marked as *"wants to join"* the new party. This does not force any interest group into or out of government, but if the player decides to reform the government in this circumstance, the party must be unified, bringing all member interest groups into or out of government as a single bloc. If multiple interest groups are marked as "wants to join", all interest groups must be united with their parties in order to reform the government.

### Single-Party State

The Single-Party State law sets up a single party as the only valid party for a country. Which party is chosen depends on whether the country has political parties or not when the law is enacted. If the country already has parties, the chosen party is always the ruler's current party – the party their interest group is a member of. If the country does not already have parties, the chosen party is the ruler's preferred party – the party their interest group would join.

### Party requirements

The following are requirements for an interest group to form or join a party. If the formation requirements are later false, the party is not automatically disbanded.

| Party | Requirements to form | Requirements to join |
|---|---|---|
| Agrarian | Rural Folk are **not** marginalized | None |
| Anarchist | Has researched Anarchism Any non-marginalized IG's leader has Anarchist ideology | Leader has Anarchist ideology |
| Communist | Has researched Socialism Any IG's leader's ideology is any of: Communist Vanguardist Anarchist | Not Industrialists or Landowners Leader's ideology is none of : Bonapartist Carlist Corporatist Ethno-Nationalist Fascist Integralist Legitimist Market Liberal Orléanist Royalist Theocrat Traditionalist |
| Conservative | Devout, Landowners, and Petite Bourgeoisie are **not** all marginalized | **Not** Trade Unions |
| Fascist | Has researched Mass Propaganda Any IG's leader's ideology is any of: Corporatist Ethno-Nationalist Fascist Integralist | None |
| Faith | None | None |
| Free Trade | Has researched Stock Exchange Either: Industrialists are not marginalized Any non-marginalized IG's leader has Market Liberal ideology | None |
| Liberal | Has researched Empiricism Intelligentsia are not marginalized | IG's leader's ideology is none of : Anarchist Communist Ethno-Nationalist Fascist Integralist Vanguardist |
| Patriotic | Armed Forces are **not** marginalized | None |
| Radical | Has researched Egalitarianism Either: Any non-marginalized IG's leader has Radical ideology Trade Unions are not marginalized and do not have Socialist ideology | Not Landowners or Devout IG's leader's ideology is none of : Bonapartist Ethno-Nationalist Fascist Integralist Legitimist Orléanist Royalist Slaver Theocrat Traditionalist |
| Social Democrats | Has researched Labor Movement Either: Trade Unions are not marginalized Any non-marginalized IG's leader has Social Democrat ideology | Not Landowners or Industrialists IG's leader's ideology is none of : Bonapartist Ethno-Nationalist Fascist Integralist Legitimist Orléanist Royalist Theocrat Traditionalist |

### Party attraction

The following is a list of all party attraction modifiers. An interest group must have at least +1 attraction to join a party and always joins the party it has the highest attraction to. Multiplicative modifiers apply after summing all additive modifiers.

| Modifier | Condition | Tooltip |
|---|---|---|
| ×2 | Is influential and only one other member in party | Influential group in supporting role |
| ×0.5 | Two other members in party | Two other party members |
| ×0.05 | Three other members in party | Three other party members |
| ×0.0 | More than three other members in party | More than three other party members |

| Modifier | Interest group condition | Country condition | Tooltip |
|---|---|---|---|
| −5 | Base value |  | Base Value |
| +10 | Is powerful and has Agrarian ideology |  | Is Powerful |
| +10 | Is not powerful and opposes Serfdom | Has Serfdom | Powerful Farmers |
| +10 | Is Rural Folk or Intelligentsia | Has heritage trait *Nordic* | Scandinavian Primary Culture |
| +6 | Leader has Pacifist ideology | Does not have No Colonial Affairs | From Pertinent Pacifist Ideology |
| +6 | Has Isolationist, Populist or Reactionary ideology | Has No Migration Controls | No Migration Controls Law |
| −10 | Is Rural Folk | Has Landed Voting or Wealth Voting | Limited Suffrage for Rural Folk |
| −5 | Is Rural Folk | Has Census Suffrage | Limited Suffrage for Rural Folk |
| +6 | Has Liberal or Particularist ideology | Has Local Police Force or Militarized Police Force | Local or Militarized Police Law |
| +6 | Has Meritocratic or Agrarian ideology or leader has Social Democrat ideology | Has Land-Based Taxation | Land-Based Taxation Law |
| +6 | Has Proletarian, Agrarian, Paternalistic, or Magnatial ideology Leader does not have Market Liberal ideology | Has Free Trade | Free Trade Law |
| +6 | Either: Has Proletarian or Agrarian ideology Leader has Protectionist ideology Leader does not have Market Liberal ideology | Has Laissez-Faire | Free Trade Law |
| +6 | Either: Has Jingoist, Particularist, or Sikh Moralist ideology Leader has Fascist, Anarchist, Pacifist, or Jingoist ideology | Has Peasant Levies | Peasant Levies Law |
| +10 | Either: Has Egalitarian, Anti-Slavery, Laissez-Faire, or Particularist ideology Leader has Abolitionist, Social Democrat, Communist, or Vanguardist ideology | Has Serfdom | Serfdom Law |
| +10 | Has Anti-Slavery ideology or leader has Abolitionist ideology | Has Debt Slavery | Debt Slavery Law |
| −100 | Is Industrialists or Armed Forces | Is subject [East India](East India.md) and has Crown Rule or Company Rule modifier | Colonial Governors |
| −10 |  | Capital is in South America and primary culture has language trait *Hispanophone* | South American Two-Party Dominance |
| −10 |  | Capital is in North America Yankee or Dixie primary culture Has Presidential Republic | American Two-Party System |
| −10 |  | Has Brazilian primary culture Has not researched Socialism, Corporatism, or Anarchism | From Conservative-Liberal System |
| −20 | Rural Folk are not members of the party |  | Lack of Rural Folk Backing |
| ×2 | Is Rural Folk and powerful |  | Natural party member |

| Modifier | Interest group condition | Country condition | Tooltip |
|---|---|---|---|
| −5 | Base value |  | Base Value |
| +6 | Leader has Anarchist ideology |  | Anarchist Leader Ideology |
| +10 | Is powerful and leader has Anarchist ideology |  | Is Powerful |
| +10 | Leader has Anarchist ideology | Has Council Republic and ruler has Vanguardist ideology | From Vanguardist Ruler with Council Republic |
| +5 | Leader has Anarchist ideology No non-marginalized interest group's leader has Communist or Vanguardist ideology |  | Sole leftist Interest Group |
| +3 | Leader has Anarchist or Radical ideology | Has Outlawed Dissent or Censorship | Restricted Free Speech Laws |
| +3 | Has Liberal or Egalitarian ideology or leader has Humanitarian ideology | Has Outlawed Dissent | Outlawed Dissent Law |
| +3 | Has Meritocratic or Agrarian ideology or leader has Social Democrat ideology | Has Land-Based Taxation | Land-Based Taxation Law |
| +3 | Has Anti-Clerical ideology or leader has Nihilist ideology | Has State Religion | State Religion Law |
| +3 | Either: Has Jingoist, Particularist, or Sikh Moralist ideology Leader has Anarchist or Pacifist ideology | Has Peasant Levies | Peasant Levies Law |
| +5 | Has Anti-Slavery ideology or leader has Abolitionist ideology | Has Legacy Slavery, Slave Trade, or Colonial Slavery | Slavery Laws |
| +5 | Either: Has Egalitarian, Anti-Slavery, Laissez-Faire or Particularist ideology Leader has Abolitionist, Social Democrat, Communist, or Vanguardist ideology | Has Serfdom | Serfdom Law |
| −100 | Is Industrialists or Armed Forces | Is subject [East India](East India.md) and has Crown Rule or Company Rule modifier | Colonial Governors |

| Modifier | Interest group condition | Country condition | Tooltip |
|---|---|---|---|
| −5 | Base value |  | Base Value |
| +10 | Leader has Communist, Vanguardist or Anarchist ideology |  | Leftist Leader Ideology |
| +10 | Is powerful and leader has Communist, Vanguardist or Anarchist ideology |  | Is Powerful |
| +6 | Is not powerful and leader has Social Democrat or Radical ideology Any powerful interest group has Communist, Vanguardist or Anarchist ideology |  | Stronger leftist Interest Group |
| −10 | Leader has Anarchist ideology | Has Council Republic and ruler has Vanguardist ideology | From Vanguardist Ruler with Council Republic |
| −3 | Has Reactionary ideology |  | Reactionary Ideology |
| +2 | Is Trade Unions |  | Trade Union Interest Group |
| −3 | Leader has Moderate ideology |  | Moderate Leader Ideology |
| +3 | Has Meritocratic or Agrarian ideology or leader has Social Democrat ideology | Has Land-Based Taxation | Land-Based Taxation Law |
| +3 | Has Anti-Clerical ideology or leader has Nihilist ideology | Has State Religion | State Religion Law |
| +3 | Has Socialist or Agrarian ideology and leader does not have Market Liberal ideology | Has Free Trade | Free Trade Law |
| +3 | Either: Has Socialist or Agrarian ideology Leader has Protectionist ideology Leader does not have Market Liberal ideology | Has Laissez-Faire | Laissez-Faire Law |
| +3 | Has Proletarian ideology or leader has Social Democrat Ideology | Does not have Graduated Taxation | Support for Graduated Taxation Law |
| +3 | Has Loyalist ideology | Does not have Per-Capita Taxation, Proportional Taxation or Graduated Taxation | Support for Graduated Taxation Law |
| +5 | Either: Has Egalitarian, Anti-Slavery, Laissez-Faire or Particularist ideology Leader has Abolitionist, Social Democrat, Communist, or Vanguardist ideology | Has Serfdom | Serfdom Law |
| +5 | Has Anti-Slavery ideology or leader has Abolitionist ideology | Has Legacy Slavery, Slave Trade, or Colonial Slavery | Slavery Laws |
| −100 | Is Industrialists or Armed Forces | Is subject [East India](East India.md) and has Crown Rule or Company Rule modifier | Colonial Governors |
| +20 | Is Armed Forces | Chose the Communist Party in the Caudillo event *Kingmaker* | Caudillo Kingmaker |

| Modifier | Interest group condition | Country condition | Tooltip |
|---|---|---|---|
| −5 | Base value |  | Base Value |
| −20 | Leader has Communist, Vanguardist, Anarchist, Social Democrat, Radical or Nihilist ideology |  | Leftist Leader Ideology |
| +5 | Leader has Traditionalist, Royalist, Theocrat, Slaver, Corporatist, Orléanist, Bonapartist, or Legitimist ideology |  | Conservative Leader Ideology |
| +5 | Has Paternalistic, Magnatial, Hierarchic, Patriarchal, Moralist or Corporatist ideology |  | Conservative Ideology |
| +5 | Is Armed Forces and powerful party member's leader has Jingoist ideology |  | Jingoist Party Leader |
| +5 | Is Landowners and clout is at least 15% |  | Is Powerful |
| −5 | Leader has Feminist, Pacifist, Reformer, Humanitarian, or Enlightened Royalist ideology |  | Progressive Leader Ideology |
| +3 | Has Reactionary Ideology |  | Reactionary Ideology |
| −20 | Leader has Abolitionist ideology | Does not have Slavery Banned | Pertinent Anti-Slavery Ideology |
| +5 | Has Patriotic or Military Absolutist ideology |  | Patriotic Ideology |
| +5 | Has Plutocratic, Magnatial or Paternalistic ideology | Has Universal Suffrage | Universal Suffrage Law |
| +2 | Has Plutocratic or Hierarchic ideology | Has Graduated Taxation | Graduated Taxation Law |
| +2 | Has Individualist ideology | Has Public Health Insurance | Public Health Insurance Law |
| +2 | Has Individualist or Pious ideology | Has Public Schools | Public Schools Law |
| +5 | Has Moralist ideology | Has Total Separation | Total Separation Law |
| +3 | Has Moralist ideology | Has Freedom of Conscience | Freedom of Conscience Law |
| +3 | Has Patriarchal ideology | Has Women's Suffrage | Women’s Suffrage Law |
| +2 | Has Patriarchal ideology | Has Women in the Workplace | Women in the Workplace Law |
| +2 | Has Reactionary ideology | Has Multiculturalism | Multiculturalism Law |
| +3 | Has Patriotic or Military Absolutist ideology or leader has Authoritarian ideology | Does not have No Home Affairs or Guaranteed Liberties | From Guaranteed Liberties Law |
| +3 | Has Patriarchal, Patriotic ideology, or Military Absolutist or leader has Authoritarian ideology | Has researched Law Enforcement and has Right of Assembly or Protected Speech | Free Speech Laws |
| +3 | Has Moralist, Magnatial or Paternalistic ideology | Does not have Monarchy or Theocracy | Republican Governance Principles |
| +5 | Has Hierarchic or Laissez-Faire ideology | Has Regulatory Bodies or Workers' Protections | Labor Rights Laws |
| +5 | Has Hierarchic or Individualist ideology | Has Wage Subsidies or Old Age Pension | Welfare Laws |
| +3 | Has Paternalististic, Scholar-Gentry, Junker, Baronial, Patriotic, or Military Absolutist ideology | Has researched Law Enforcement and has No Police | No Police Law |
| +5 | Is Devout and leader does not have any liberal, progressive, or socialist ideology | Is [Austria](Austria.md) | Christian Social Traditions |
| +10 | Has Corporatist ideology or leader has Corporatatist ideology | Is [Austria](Austria.md) | Corporatism |
| +100 | Leader has Slaver ideology | Has active journal entry *The Slavery Debate* | Leader is a Slaver |
| −100 | Leader has Abolitionist ideology | Has active journal entry *The Slavery Debate* | Leader is an Abolitionist |
| −100 | Is Industrialists or Armed Forces | Is subject [East India](East India.md) and has Crown Rule or Company Rule modifier | Colonial Governors |
| −5 | Leader has Bonapartist, Legitimist or Orléanist ideology Any powerful party member's leader has a different dynasty ideology |  | Powerful Rival Monarchists |
| +10 | Is Armed Forces and leader has none of Democrat, Republican, Radical, Communist, or Vanguardist ideologies | Is [France](France.md) and has Monarchy | Monarchist Leanings |
| +2000 | Leader has Jacksonian Democrat ideology |  | From Jacksonian Democrat |
| +10 | Is Landowners | Has active journal entry *Coffee with Milk* or *Populist Unrest* | From the Milk-Coffee System |
| +10 | Is Petite Bourgeoisie | Has active journal entry *Populist Unrest* | From Populist Unrest |
| +10 | Is Landowners or Devout | Capital is in South America and primary culture has language trait *Hispanophone* | South American Two-Party Dominance |
| +20 | Is Armed Forces | Chose the Conservative Party in the Caudillo event *Kingmaker* | Caudillo Kingmaker |
| −5 | Leader has Yankee culture | Has Yankee or Dixie primary culture Either: Has modifier Missouri Compromise Does not have Slavery Banned | From Northern Interests |
| +3 | Leader has Dixie culture | Has Yankee or Dixie primary culture Either: Has modifier Missouri Compromise Does not have Slavery Banned | From Southern Interests |
| ×2 | Is Landowners and powerful |  | Natural party member |

| Modifier | Interest group condition | Country condition | Tooltip |
|---|---|---|---|
| −5 | Base value |  | Base Value |
| +10 | Leader has Fascist, Ethno-Nationalist, or Integralist ideology |  | Fascist Leader Ideology |
| +10 | Is powerful and leader has Fascist or Integralist ideology |  | Is Powerful |
| +5 | Has Reactionary ideology |  | Reactionary Ideology |
| +5 | Is not powerful and is Landowners, Devout, Petite Bourgeoisie, Industrialists or Armed Forces Any powerful interest group's leader has Fascist or Integralist ideology |  | Stronger Fascist Interest Group |
| −20 | Leader has Communist, Vanguardist, Anarchist, Social Democrat, Radical, or Nihilist ideology |  | Leftist Leader Ideology |
| −10 | Leader has Nihilist, Feminist, Reformer, Abolitionist, Pacifist, Humanitarian, or Enlightened Royalist ideology |  | Progressive Leader Ideology |
| −2 | Is Trade Unions |  | Trade Union Interest Group |
| −2 | Leader has Market Liberal ideology |  | Market Liberal Leader Ideology |
| −3 | Leader has Moderate ideology |  | Moderate Leader Ideology |
| +5 | Has Corporatist ideology or leader has Corporatist ideology Any powerful interest group's leader has Fascist or Integralist ideology |  | Corporatist Ideology |
| +4 | Has Patriotic or Military Absolutist ideology |  | Patriotic Ideology |
| +5 | Has Isolationist ideology | Has No Migration Controls | Pertinent Isolationist Ideology |
| +3 | Has Paternalistic, Scholar-Gentry, Junker, Baronial, Patriotic, or Military Absolutist ideology | Has researched Law Enforcement and has No Police | No Police Law |
| +3 | Either: Has Jingoist, Particularist, or Sikh Moralist ideology Leader has Fascist or Jingoist ideology | Has Peasant Levies | Peasant Levies Law |
| +3 | Has Meritocratic ideology | Does not have Proportional Taxation or Per-Capita Taxation | Support for Proportional or Per Capita Taxation Laws |
| +3 | Has Loyalist ideology | Does not have Graduated Taxation, Proportional Taxation or Per-Capita Taxation | Support for Proportional or Per Capita Taxation Laws |
| +3 | Leader has Authoritarian ideology |  | Authoritarian Leader Ideology |
| −100 | Is Industrialists or Armed Forces | Is subject [East India](East India.md) and has Crown Rule or Company Rule modifier | Colonial Governors |
| −5 | Leader has Bonapartist, Legitimist or Orléanist ideology Any powerful party member's leader has a different dynasty ideology |  | Powerful Rival Monarchists |
| +20 | Is Armed Forces | Chose the Fascist Party in the Caudillo event *Kingmaker* | Caudillo Kingmaker |

| Modifier | Interest group condition | Country condition | Tooltip |
|---|---|---|---|
| −5 | Base value |  | Base Value |
| −5 | Is Landowners and is not marginalized | Has not researched Corporatism | From Significant Landowners |
| +5 | Is Devout | Has Theocracy | From Theocracy |
| −20 | Devout are not members of the party |  | Lack of Clerical Backing |
| +10 | Is Devout and is powerful |  | Is Powerful |
| +10 | Is not powerful and leader has Traditionalist, Theocrat, or Corporatist ideology and Devout are powerful |  | Religious Leader Ideology |
| −15 | Has Anti-Clerical ideology or leader has Nihilist ideology |  | Anti-Religious Ideology |
| +10 | Has Corporatist ideology or leader has Corporatist ideology | Is not [Austria](Austria.md) | Corporatist Ideology |
| +3 | Has Patriarchal ideology | Has Women's Suffrage | Women’s Suffrage Law |
| −10 |  | Capital is in South America and primary culture has language trait *Hispanophone* | South American Two-Party Dominance |
| −10 |  | Capital is in North America Yankee or Dixie primary culture Has Presidential Republic | American Two-Party System |
| −100 | Is Industrialists or Armed Forces | Is subject [East India](East India.md) and has Crown Rule or Company Rule modifier | Colonial Governors |
| ×2 | Is Devout and powerful | Is not [Austria](Austria.md) | Natural party member |
| −5 | Leader has Bonapartist, Legitimist or Orléanist ideology Any powerful party member's leader has a different dynasty ideology |  | Powerful Rival Monarchists |

| Modifier | Interest group condition | Country condition | Tooltip |
|---|---|---|---|
| −5 | Base value |  | Base Value |
| +2 | Has Laissez-Faire ideology or leader has Market Liberal ideology | Has Laissez-Faire or Interventionism | Enacted Liberal Economy Laws |
| +1 | Has Laissez-Faire ideology or leader has Market Liberal ideology | Has Free-Trade or Protectionism | Enacted Liberal Economy Laws |
| +1 | Has Laissez-Faire ideology or leader has Market Liberal ideology | Has Tenant Farmers or Commercialized Agriculture | Enacted Liberal Economy Laws |
| +1 | Has Laissez-Faire ideology or leader has Market Liberal ideology | Has Slavery Banned | Enacted Liberal Economy Laws |
| +10 | Is powerful and has Laissez-Faire ideology or leader has Market Liberal ideology | Does not have Universal Suffrage | Has the Laissez-Faire Ideology and is Powerful |
| +5 | Is not powerful and leader has Market Liberal ideology and Industrialists are powerful |  | Stronger Industrialist Interest Group |
| +5 | Has Hierarchic or Laissez-Faire ideology | Has Regulatory Bodies or Workers' Protections | Labor Rights Laws |
| +5 | Has Hierarchic or Individualist ideology | Has Wage Subsidies or Old Age Pension | Welfare Laws |
| +3 | Has Laissez-Faire ideology or leader has Market Liberal ideology | Does not have Child Labor Allowed | Support for Child Labor |
| +3 | Has Laissez-Faire ideology or leader has Market Liberal ideology | Does not have Free Trade | Support for Free Trade Law |
| +3 | Has Plutocratic ideology | Does not have Oligarchy or Wealth Voting | Support for Oligarchy or Wealth Voting |
| +3 | Has Republican ideology | Has Autocracy | Opposition to Autocracy Law |
| +3 | Has Paternalistic or Magnatial ideology or leader has Fascist or Integralist ideology | Has Universal Suffrage | Universal Suffrage Law |
| +3 | Has Plutocratic or Meritocratic ideology | Has researched Currency Standards Does not have Per-Capita Taxation or Consumption-Based Taxation | Support for Per-Capita Taxation Law |
| +3 | Has Plutocratic, Meritocratic or Hierarchic ideology | Has Graduated Taxation | Graduation Taxation Law |
| +3 | Has Agrarian or Hierarchic ideology | Does not have Per-Capita Taxation or Consumption-Based Taxation | Support for Consumption-Based Taxation Law |
| +3 | Has Paternalistic, Magnatial, Laissez-Faire, or Agrarian ideology or leader has Market Liberal ideology | Has researched Central Planning and has Command Economy | Command Economy Law |
| +3 | Has Individualist or Anti-Clerical ideology | Has researched Academia and has No Schools or Religious Schools | Support for Private Schools |
| −10 | Leader has Protectionist ideology |  | Protectionist Leader Ideology |
| −10 | Is Industrialists and less than 3 party members | Has Universal Suffrage | Extensive Suffrage |
| −5 | Is Industrialists and less than 3 party members | Has Census Suffrage | Extensive Suffrage |
| −10 |  | Capital is in South America and primary culture has language trait *Hispanophone* | South American Two-Party Dominance |
| −10 |  | Capital is in North America Yankee or Dixie primary culture Has Presidential Republic | American Two-Party System |
| −100 | Is Industrialists or Armed Forces | Is subject [East India](East India.md) and has Crown Rule or Company Rule modifier | Colonial Governors |
| ×2 | Is Industrialists and powerful |  | Natural party member |
| −5 | Leader has Bonapartist, Legitimist or Orléanist ideology Any powerful party member's leader has a different dynasty ideology |  | Powerful Rival Monarchists |
| −10 |  | Has Brazilian primary culture Has not researched Socialism, Corporatism, or Anarchism | From Conservative-Liberal System |

| Modifier | Interest group condition | Country condition | Tooltip |  |  |  |  |
|---|---|---|---|---|---|---|---|
| −5 | Base value |  | Base Value |  |  |  |  |
| +10 | Leader has Reformer ideology |  | Liberal Leader Ideology |  |  |  |  |
| +5 | Leader has Market Liberal ideology |  | Liberal Leader Ideology |  |  |  |  |
| +3 | Leader has Republican or Radical ideology |  | Liberal Leader Ideology |  |  |  |  |
| +3 | Leader has Radical ideology |  | Leader has Radical Ideology |  |  |  |  |
| +5 | Has Liberal or Laissez-Faire Ideology |  | Liberal or Laissez-Faire Ideology |  |  |  |  |
| +5 | Leader has Feminist, Abolitionist, Pacifist, Social Democrat, Humanitarian, or Enlightened Royalist ideology |  | Progressive Leader Ideology |  |  |  |  |
| −5 | Leader has Traditionalist, Royalist, Theocrat, Slaver, Authoritarian, Orléanist, Bonapartist, or Legitimist ideology |  | Conservative Leader Ideology |  |  |  |  |
| +3 | Has Meritocratic or Anti-Clerical ideology | Has Hereditary Bureaucrats | Hereditary Bureaucrats Law |  |  |  |  |
| +5 | Is Armed Forces and any powerful party member's leader has Jingoist ideology |  | Jingoist Party Leader |  |  |  |  |
| +5 | Is not powerful, and has Laissez-Faire ideology or leader has Market Liberal ideology |  | Has the Laissez-Faire Ideology, or Leader has the Market Liberal Ideology |  |  |  |  |
| +2 | Is not Devout or Landowners, and has Laissez-Faire ideology or leader has Market Liberal ideology | Landowners are powerful | Powerful Traditional Interest Groups |  |  |  |  |
| +2 | Is not Devout or Landowners, and has Laissez-Faire ideology or leader has Market Liberal ideology | Devout are powerful | Powerful Traditional Interest Groups |  |  |  |  |
| +3 | Has Individualist or Proletarian ideology | Has No Schools or Religious Schools | No Schools or Religious Schools Laws |  |  |  |  |
| +3 | Has Liberal or Egalitarian ideology or leader has Feminist ideology | Has Legal Guardianship | Legal Guardianship Law |  |  |  |  |
| +3 | Has Liberal ideology or leader has Reformer, Humanitarian, or Enlightened Royalist ideology | Has Ethnostate, National Supremacy or Racial Segregation | Exclusionary Citizenship Laws |  |  |  |  |
| +3 | Has Liberal or Egalitarian ideology or leader has Humanitarian or Enlightened Royalist ideology | Has Outlawed Dissent | Outlawed Dissent Law |  |  |  |  |
| +3 | Has Liberal or Particularist ideology | Has Local Police Force or Militarized Police Force | Local or Militarized Police Law |  |  |  |  |
| +3 | Has Anti-Clerical ideology or leader has Nihilist ideology | Has State Religion | State Religion Law |  |  |  |  |
| +3 | Has Republican or Populist ideology or leader has Nihilist, Republican, or Radical ideology | Has Monarchy or Theocracy | Non-Republican Governance Principles |  |  |  |  |
| +5 | Has Particularist ideology or leader has Abolitionist ideology | Has Debt Slavery | Debt Slavery Law |  |  |  |  |
| +5 | Has Anti-Slavery ideology or leader has Abolitionist ideology | Has Legacy Slavery, Slave Trade, or Colonial Slavery | Slavery Laws |  |  |  |  |
| +5 | Either: Has Egalitarian, Anti-Slavery, Laissez-Faire, or Particularist ideology Leader has Abolitionist, Social Democrat, Communist, or Vanguardist ideology | Has Serfdom | Serfdom Law |  |  |  |  |
| +10 | Leader has Modernizer ideology |  | From Modernizers |  |  |  |  |
| +5 | Is Trade Unions, not powerful, and does not have Socialist ideology | Has Census Suffrage | Trade Unions Lacking Suffrage |  |  |  |  |
| +10 | Is Trade Unions, not powerful, and does not have Socialist ideology | Has Landed Voting or Wealth Voting | Trade Unions Lacking Suffrage |  |  |  |  |
| +100 | Leader has Abolitionist ideology | Has active journal entry *The Slavery Debate* | Leader is an Abolitionist |  |  |  |  |
| −100 | Leader has Slaver ideology | Has active journal entry *The Slavery Debate* | Leader is a Slaver |  |  |  |  |
| −5 | Leader has Bonapartist, Legitimist or Orléanist ideology Any powerful party member's leader has a different dynasty ideology |  | Powerful Rival Monarchists | +10 | Has Liberal or Populist ideology or leader has Republican, Radical, Positivist, or Nihilist ideology | Is [France](France.md) and has Monarchy | July Monarchy |
| +3 | Leader has Yankee culture | Has Yankee or Dixie primary culture Either: Has modifier Missouri Compromise Does not have Slavery Banned | From Northern Interests |  |  |  |  |
| −10 | Leader is Robert Rantoul | From Northern Democrats |  |  |  |  |  |
| −5 | Leader has Dixie culture | Has Yankee or Dixie primary culture Either: Has modifier Missouri Compromise Does not have Slavery Banned | From Southern Interests |  |  |  |  |
| +10 | Is Intelligentsia or Rural Folk | Capital is in South America and primary culture has language trait *Hispanophone* | South American Two-Party Dominance |  |  |  |  |
| +3 | Leader does not have a *reactionary*, *conservative* or *socialist* ideology | Capital is in North America Yankee or Dixie primary culture Has Presidential Republic | American Two-Party System |  |  |  |  |
| −100 | Is Industrialists or Armed Forces | Is subject [East India](East India.md) and has Crown Rule or Company Rule modifier | Colonial Governors |  |  |  |  |
| +20 | Is Armed Forces | Chose the Liberal Party in the Caudillo event *Kingmaker* | Caudillo Kingmaker |  |  |  |  |
| ×2 | Is Intelligentsia and powerful |  | Natural party member |  |  |  |  |

| Modifier | Interest group condition | Country condition | Tooltip |
|---|---|---|---|
| −5 | Base value |  | Base Value |
| −20 | Armed Forces are not members of the party |  | Lack of Military Backing |
| +10 | Is Armed Forces and powerful |  | Is Powerful |
| +10 | Leader has Jingoist ideology |  | Jingoist Leader Ideology |
| +3 | Has Paternalistic, Scholar-Gentry, Junker, Baronial, Patriotic, or Military Absolutist ideology | Has researched Law Enforcement and has No Police | No Police Law |
| +3 | Either: Has Jingoist, Particularist, or Sikh Moralist ideology Leader has Fascist, Anarchist, Pacifist, or Jingoist ideology | Has Peasant Levies | Peasant Levies Law |
| +3 | Has Proletarian or Loyalist ideology or leader has Social Democrat ideology | Does not have Per-Capita Taxation, Proportional Taxation or Graduated Taxation | Support for Graduated Taxation Law |
| +3 | Has Meritocratic ideology | Does not have Per-Capita Taxation or Proportional Taxation | Support for Proportional or Per Capita Taxation Laws |
| +3 | Has Loyalist ideology | Does not have Per-Capita Taxation, Proportional Taxation or Graduated Taxation | Support for Graduated Taxation Law |
| +3 | Has Patriotic ideology or Military Absolutist or leader has Authoritarian ideology | Does not have No Home Affairs or Guaranteed Liberties | From Guaranteed Liberties Law |
| +3 | Has Patriarchal, Patriotic, or Military Absolutist ideology or leader has Authoritarian ideology | Has researched Law Enforcement and has Right of Assembly or Protected Speech | Free Speech Laws |
| +5 | Leader has Authoritarian ideology |  | Authoritarian Leader Ideology |
| −10 |  | Capital is in South America and primary culture has language trait *Hispanophone* | South American Two-Party Dominance |
| −10 |  | Capital is in North America Yankee or Dixie primary culture Has Presidential Republic | American Two-Party System |
| −5 | Leader has Bonapartist, Legitimist or Orléanist ideology Any powerful party member's leader has a different dynasty ideology |  | Powerful Rival Monarchists |
| −10 | Leader has none of Democrat, Republican, Radical, Communist, or Vanguardist ideologies | Is [France](France.md) and has Monarchy | Monarchist Leanings |
| −100 | Is Industrialists or Armed Forces | Is subject [East India](East India.md) and has Crown Rule or Company Rule modifier | Colonial Governors |
| ×2 | Is Armed Forces and powerful |  | Natural party member |

| Modifier | Interest group condition | Country condition | Tooltip |
|---|---|---|---|
| −5 | Base value |  | Base Value |
| +10 | Leader has Radical ideology |  | Leader has Radical Ideology |
| +15 | Is powerful and leader has Radical Ideology |  | Is Powerful |
| −5 | Is not powerful and leader has Radical ideology and any powerful interest group has Liberal ideology |  | Stronger Liberal Interest Group |
| +10 | Is not powerful and has Liberal ideology and any powerful interest group's leader has Radical ideology |  | Stronger Radical Interest Group Leader |
| +10 | Is not powerful and leader has Communist, Vanguardist or Anarchist ideology Any powerful interest group's leader has Radical ideology | Does not have Council Republic | Stronger Radical Interest Group Leader |
| +10 | Leader has Feminist, Abolitionist, Social Democrat, Republican, Nihilist, or Humanitarian ideology |  | Progressive Leader Ideology |
| +10 | Has Populist ideology or leader has Nihilist, Republican, or Radical ideology | Has Monarchy or Theocracy | Non-Republican Governance Principles |
| +3 | Has Particularist ideology | Has Serfdom or Debt Slavery | Pertinent Particularist Ideology |
| −3 | Leader has Moderate ideology |  | Moderate Leader Ideology |
| +5 | Has Populist ideology or leader has Radical, Social Democrat, or Humanitarian ideology | Does not have Universal Suffrage | Lack of Universal Suffrage Law |
| +3 | Leader has Radical, Anarchist, or Humanitarian ideology | Has Outlawed Dissent or Censorship | Restricted Free Speech Laws |
| +6 | Has Liberal or Egalitarian ideology or leader has Humanitarian ideology | Has Outlawed Dissent | Outlawed Dissent Law |
| +6 | Has Liberal ideology or leader has Radical or Humanitarian ideology | Has Secret Police | Authoritarian Internal Security Laws |
| +3 | Has Anti-Slavery ideology or leader has Abolitionist ideology | Has Legacy Slavery, Slave Trade, or Colonial Slavery | Slavery Laws |
| +5 | Either: Has Egalitarian, Anti-Slavery, Laissez-Faire, or Particularist ideology Leader has Abolitionist, Social Democrat, Communist, or Vanguardist ideology | Has Serfdom | Serfdom Law |
| +5 | Is Trade Unions and does not have Socialist ideology and has another party member | Has Census Suffrage | Trade Unions Lacking Suffrage |
| +10 | Is Trade Unions and does not have Socialist ideology and has another party member | Has Landed Voting or Weath Voting | Trade Unions Lacking Suffrage |
| −10 |  | Capital is in South America and primary culture has language trait *Hispanophone* | South American Two-Party Dominance |
| −10 |  | Capital is in North America Yankee or Dixie primary culture Has Presidential Republic | American Two-Party System |
| −100 | Is Industrialists or Armed Forces | Is subject [East India](East India.md) and has Crown Rule or Company Rule modifier | Colonial Governors |

| Modifier | Interest group condition | Country condition | Tooltip |
|---|---|---|---|
| −5 | Base value |  | Base Value |
| +5 | Leader has Social Democrat ideology |  | Leader has the Social Democrat Ideology |
| +5 | Leader has Social Democrat ideology and is powerful |  | Is Powerful |
| −5 | Is not powerful and leader has Social Democrat ideology Any powerful interest group's leader has Communist, Vanguardist or Anarchist ideology |  | Stronger leftist Interest Group |
| +6 | Is not powerful and leader has Communist, Vanguardist or Anarchist ideology Any powerful interest group's leader has Social Democrat ideology | Does not have Council Republic | Stronger Social Democrat Interest Group Leader |
| +5 | Has Liberal ideology and is not powerful and any powerful interest group's leader has Social Democrat ideology |  | Weak Liberals, Powerful Social Democrats |
| +5 | Leader has Feminist, Abolitionist, Pacifist, Radical, Reformer, Republican, Nihilist, Humanitarian, or Enlightened Royalist ideology |  | Progressive Leader Ideology |
| −5 | Leader has Market Liberal ideology |  | Leader has Market Liberal Ideology |
| +5 | Is Trade Unions and is powerful and leader does not have Communist, Vanguardist or Anarchist ideology |  | Powerful Trade Unions |
| +3 | Has Liberal or Egalitarian ideology or leader has Humanitarian or Humanitarian Royalist ideology | Has Outlawed Dissent | Outlawed Dissent Law |
| +3 | Has Meritocratic or Agrarian ideology or leader has Social Democrat ideology | Has Land-Based Taxation | Land-Based Taxation Law |
| +3 | Has Loyalist ideology | Has Consumption-Based Taxation | Pertinent Loyalist Ideology |
| +3 | Has Republican or Populist ideology or leader has Nihilist, Republican, or Radical ideology | Has Monarchy or Theocracy | Non-Republican Governance Principles |
| +3 | Has Individualist or Proletarian ideology | Has No Schools or Religious Schools | No Schools or Religious Schools Laws |
| +3 | Has Proletarian, Agrarian, Magnatial, or Paternalistic ideology and leader does not have Market Liberal ideology | Has Free Trade | Free Trade Law |
| +3 | Either: Has Proletarian or Agrarian ideology Leader has Protectionist ideology Leader does not have Market Liberal ideology | Has Laissez-Faire | Laissez-Faire Law |
| +3 | Has Proletarian ideology or leader has Social Democrat ideology | Does not have Graduated Taxation | Support for Graduated Taxation Law |
| +3 | Has Loyalist ideology | Does not have Per-Capita Taxation, Proportional Taxation or Graduated Taxation | Support for Graduated Taxation Law |
| +5 | Either: Has Egalitarian, Anti-Slavery, Laissez-Faire, or Particularist ideology Leader has Abolitionist, Social Democrat, Communist, or Vanguardist ideology | Has Serfdom | Serfdom Law |
| +5 | Has Anti-Slavery ideology or leader has Abolitionist ideology | Has Legacy Slavery, Slave Trade, or Colonial Slavery | Slavery Laws |
| +5 | Is Trade Unions, not powerful, and does not have Socialist ideology |  | Populist Trade Unions |
| +5 | Has Socialist or Isolationist ideology | Has Free Trade |  |
| +3 | Either: Has Socialist or Agrarian ideology Leader has Protectionist, Vanguardist or Luddite ideology | Has Laissez-Faire | Laissez-Faire Law |
| −100 | Is Industrialists or Armed Forces | Is subject [East India](East India.md) and has Crown Rule or Company Rule modifier | Colonial Governors |
| ×2 | Is Trade Unions and powerful |  | Natural party member |

## References

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | [Government](Government.md) • [Capacities](Capacity.md) • [Characters](Character.md) • [Decrees](Decrees.md) • [Institutions](Institutions.md) • [Laws](Laws.md) • [Technology](Technology.md) |
|---|---|

| Politics | [Elections](Elections.md) • [Ideology](Ideology.md) • [Interest group](Interest group.md) • [Political lobby](Political lobby.md) • [Political movement](Political movement.md) • Political party • [Revolution](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| Economy | [Buildings](Building.md) • [Goods](Goods.md) • [Harvest condition](Harvest condition.md) • [Infrastructure](Infrastructure.md) • [Market](Market.md) • [Production methods](https://vic3.paradoxwikis.com/Production_methods) • [State](State.md) • [Treasury](Treasury.md) |
|---|---|

| Diplomacy | [Diplomacy](Diplomacy.md) • [Diplomatic action](https://vic3.paradoxwikis.com/Diplomatic_action) • [Diplomatic play](Diplomatic play.md) • [Power bloc](Power bloc.md) • [Ranks](Rank.md) • [Subjects](Subject.md) • [Treaties](Treaty.md) |
|---|---|

| Warfare | [Warfare](Warfare overview.md) • [Land warfare](Land warfare.md) • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
