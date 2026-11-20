---
title: Political movement
source: https://vic3.paradoxwikis.com/Political_movement
pageid: 1621
categories: [1.13, Articles_with_potentially_outdated_images, Politics]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this image. It was last verified for version unknown. |
|---|---|

A law reform in progress and a movement to preserve the current law.
**Political movements** represent popular support for certain ideologies or cultural or religious identities. Political movements draw their strength from [pops](Pops.md) and may influence [interest groups](Interest group.md). This allows pops to push for reform, even when they are *disenfranchised*.

Radical political movements may turn into *revolutions* and seek to change the political system by force.

## Formation and disbanding

Political movements have a base X% chance of starting each PERIOD when checked. This is increased by X% per point of starting support the movement would have?. If there are any existing movements the chance is divided by 1 + ( 2 ⋅ ⋅ # # of active movements ) {\displaystyle 1+(2\cdot \#{\text{ of active movements}})} ![{\displaystyle 1+(2\cdot \#{\text{ of active movements}})}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/ece2a2c4dc6c3eb3940e95a72bca4327edd1050b).

A movement needs at least 2.5 support to start and disbands if it has less than 1 support; a movement cannot disband due to low support until 12 months have passed. After that time, there is a cumulative 0.04% chance for it to disband each month after the initial 12 months. The disband chance is divided by 1 + ( 0.01 ⋅ ⋅ movement support ) {\displaystyle 1+(0.01\cdot {\text{movement support}})} ![{\displaystyle 1+(0.01\cdot {\text{movement support}})}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/b0aa9e79c30ea8fb3c4c6caca37a953c696dc6ae). However, this does not apply to movements which have become *revolutionary*.

## Political movement categories

There are five general types of movements:

| Category | Support to | Identity based |  |
|---|---|---|---|
| Create | Maintain |  |  |
| Ideological | 5 | 2.5 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| Pan-national | 5 | 2.5 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| Cultural | 20 | 10 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| Cultural majority | 5 | 2.5 | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| Religious | 10 | 5 | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |

Cultural, Religious, and Pan-national movements might contribute to [Obstinance](https://vic3.paradoxwikis.com/Obstinance).

### Political movement types

Within each of these categories are one or more specific movement types. Each type of movement has a core ideology and may have a number of character ideologies that can be assigned to leaders of [interest groups](https://vic3.paradoxwikis.com/Interest_groups) that are pressured by the movement. Each movement type has certain conditions to be created and may have conditions which cause it to be disbanded. There are additional triggers and weights to determine agitator and pop support for a movement

| Cat. | Type | Core ideology | Character ideologies | Formation conditions | Disband conditions | Group(s) |
|---|---|---|---|---|---|---|
|  | Abolitionist | Anti-Slavery | Abolitionist Humanitarian | Does not have Slavery Banned Has researched Empiricism | Has Slavery Banned | Liberal |
|  | Pro-Slavery | Pro-Slavery | Slaver Jacksonian Democrat | Does not have Slavery Banned |  | Conservative |
|  | Absolutist | Absolutist | Royalist Authoritarian | Has Monarchy Does not have voting Is not France Does not have Bakufu | Either: Has voting, unless the country still has the possibility of completing The King-in-Parliament journal entry Has completed Stamp Out Monarchism journal entry | Conservative |
|  | Royalist | Royalist | Royalist Enlightened Royalist | Has Monarchy Has voting Is not France | Has completed Stamp Out Monarchism journal entry | Conservative |
|  | Labor | Proletarian | Radical Reformer Social Democrat Utopian | Has researched Labor Movement |  | Liberal |
|  | Socialist | Socialist | Anarchist Communist Social Democrat Vanguardist | Has researched Socialism Does not have any of: Isolationism Traditionalism Peasant Levies Serfdom (unless also Manorialism) | Selected an ideology Anarchist Character ideology Anarchist This leader seeks the abolishment of hierarchy, authority and the state, leaving people to govern themselves. Stance on Citizenship Strongly Oppose Ethnostate, National Supremacy and Subjecthood Oppose Racial Segregation Endorse Cultural Exclusion Strongly Endorse Multiculturalism Stance on Distribution of Power Strongly Oppose Technocracy, Oligarchy and Autocracy Oppose Census Suffrage, Wealth Voting, - Landed Voting and Single-Party State Neutral towards Universal Suffrage Strongly Endorse Anarchy Stance on Economic System Strongly Oppose Interventionism, Traditionalism, - Laissez-Faire and Extraction Economy Oppose Command Economy and Industry Banned Neutral towards Agrarianism Strongly Endorse Cooperative Ownership Stance on Free Speech Strongly Oppose Outlawed Dissent Oppose Censorship Endorse Right of Assembly Strongly Endorse Protected Speech Stance on Governance Principles Strongly Oppose Corporate State, Theocracy, - Monarchy and Social Monarchy Oppose Presidential Republic and Parliamentary Republic Strongly Endorse Council Republic Stance on Labor Associations Strongly Oppose Guild System and Corporatized Unions Oppose Combination Acts Neutral towards Anti-Strike Laws and Right to Associate Endorse Factory Councils Stance on Policing Strongly Oppose Militarized Police Force Oppose Local Police Force and Dedicated Police Force Endorse No Police , Communist Character ideology Communist This leader believes in the working class seizing political power through whatever means necessary. Stance on Church and State Strongly Oppose State Religion Oppose Freedom of Conscience Neutral towards Total Separation Endorse State Atheism Stance on Economic System Strongly Oppose Laissez-Faire, Industry Banned and Extraction Economy Oppose Agrarianism and Traditionalism Neutral towards Interventionism Strongly Endorse Command Economy and Cooperative Ownership Stance on Governance Principles Strongly Oppose Corporate State, Theocracy, - Monarchy and Social Monarchy Oppose Presidential Republic and Parliamentary Republic Strongly Endorse Council Republic Stance on Labor Associations Strongly Oppose Guild System and Corporatized Unions Oppose Combination Acts Neutral towards Anti-Strike Laws and Right to Associate Endorse Factory Councils Stance on Labor Rights Neutral towards No Workers' Rights Endorse Regulatory Bodies Strongly Endorse Workers' Protections Stance on Land Reform Strongly Oppose Serfdom Oppose Commercialized Agriculture and Tenant Farmers Neutral towards Peasant Proprietorship Endorse Collectivized Agriculture , or Vanguardist Character ideology Vanguardist This leader believes in achieving a socialist society through a vanguard party of dedicated radicals. Stance on Distribution of Power Strongly Oppose Oligarchy, Autocracy, - Census Suffrage, Wealth Voting and Landed Voting Oppose Anarchy and Universal Suffrage Endorse Technocracy Strongly Endorse Single-Party State Stance on Economic System Strongly Oppose Laissez-Faire, Industry Banned and Extraction Economy Oppose Agrarianism and Traditionalism Neutral towards Interventionism Endorse Cooperative Ownership Strongly Endorse Command Economy Stance on Governance Principles Strongly Oppose Corporate State, Theocracy, - Monarchy and Social Monarchy Oppose Presidential Republic and Parliamentary Republic Strongly Endorse Council Republic Stance on Labor Associations Strongly Oppose Guild System and Corporatized Unions Oppose Combination Acts Neutral towards Anti-Strike Laws and Right to Associate Endorse Factory Councils Stance on Land Reform Strongly Oppose Commercialized Agriculture and Serfdom Oppose Tenant Farmers Neutral towards Peasant Proprietorship Endorse Collectivized Agriculture Stance on Trade Policy Strongly Oppose Free Trade Oppose Mercantilism Endorse Protectionism and Isolationism in The Spectre Haunting the World | Socialist |
|  | Anarchist | Anarchist | Anarchist | Has researched Anarchism Does not have any of: Isolationism Traditionalism Peasant Levies Serfdom (unless also Manorialism) |  | Socialist |
|  | Communist | Communist | Communist Vanguardist | Has researched Socialism Does not have any of: Isolationism Traditionalism Peasant Levies Serfdom (unless also Manorialism) |  | Socialist |
|  | Fascist | Fascist | Corporatist Fascist Integralist | Has researched Political Agitation Does not have any of: Isolationism Traditionalism Peasant Levies Serfdom (unless also Manorialism) |  | Nationalist Conservative |
|  | Corporatist | Corporatist | Corporatist | Has researched Corporatism Does not have any of: Isolationism Traditionalism Peasant Levies Serfdom (unless also Manorialism) |  | Conservative |
|  | Liberal | Liberal | Liberal Humanitarian Market Liberal Radical Republican | Has researched Democracy Does not have any of: Isolationism Traditionalism Peasant Levies Serfdom (unless also Manorialism) |  | Liberal |
|  | Radical | Radical | Nihilist Radical | Has researched Egalitarianism Is not a republic A republic requires: ● Corporate State, Presidential Republic, Parliamentary Republic, or Council Republic |  | Liberal |
|  | Nihilist | Nihilist | Nihilist | Has researched Realism Has not researched both Anarchism and Socialism | Has researched both Anarchism and Socialism | Socialist |
|  | Positivist | Positivist | Positivist | Has researched Psychiatry Positivism has appeared in the world |  | Liberal |
|  | Peasant | Land Reformer | Land Reformer Luddite | Has researched Enclosure Does not have any variant of Peasant Proprietorship or Collectivized Agriculture More than 25% of pops are peasants |  |  |
|  | Feminist | Feminist | Feminist Humanitarian | Has researched Feminism |  | Liberal |
|  | Reactionary | Reactionary | Authoritarian Luddite Protectionist Traditionalist | Does not have any of: Isolationism Traditionalism Peasant Levies Serfdom (unless also Manorialism) Has Slavery Banned Has voting Does not have a Legitimist, Carlist, or Miguelist movement | Has a Legitimist, Carlist, or Miguelist movement | Conservative |
|  | Modernization | Modernizer | Modernizer Abolitionist Market Liberal Protectionist Reformer | Has researched Academia Intelligentsia are not marginalized Has any of: Isolationism Serfdom Peasant Levies Guild System Any of: Extraction Economy Traditionalism Industry Banned Any of: Consumption-Based Taxation Land-Based Taxation | Has none of: Isolationism Serfdom Peasant Levies Guild System No Schools Any of: Extraction Economy Traditionalism Industry Banned Any of: Consumption-Based Taxation Land-Based Taxation | Liberal Nationalist |
|  | Minority Rights | Pluralist (Cultural Exclusion version) | Reformer |  |  |  |
|  | Religious Majority | Traditionalist | Theocrat Traditionalist | Does not have State Atheism | Movement's religion is not the state religion | Conservative |
|  | Religious Minority | Minoritarian Traditionalist | Minoritarian Traditionalist | Either: Is not East India Has not researched Pan-nationalism | Either: Movement's religion is the state religion, and less than 8% of the country's population practices it Is East India and has researched Pan-nationalism |  |
|  | Cultural Majority | Ethno-Nationalist | Ethno-Nationalist |  |  | Nationalist Conservative |
|  | Cultural Minority | Pluralist | Reformer |  | Either: Movement's culture is a primary culture The culture has no state where it forms at least 18% of a homeland population, and either makes up 8% or less of the country's total population or has at least 20 Cultural Acceptance |  |
|  | Indian National | Sovereignist | Humanitarian Social Democrat Sovereignist | Is East India Is a subject A culture with South Asian Heritage has more than 10 fervor No primary culture has South Asian Heritage Has researched Pan-nationalism |  | Liberal |
|  | German National | National Liberal | Ethno-Nationalist Market Liberal Liberal Republican Radical | Capital is in the German Confederation Is a North or South German country except Germany Either North or South German culture has at least 10 fervor | Is [Germany](Germany.md) | Liberal Nationalist |
|  | Italian National | National Liberal | Ethno-Nationalist Market Liberal Liberal Republican Radical | Capital is in Italy Is a North or South Italian country except Austria , Danubian State , Central Europe , and Italy Either North or South Italian culture has at least 10 fervor | Is [Italy](Italy.md) | Liberal Nationalist |
|  | Yugoslav (Illyrian) National | National Liberal | Ethno-Nationalist Market Liberal Liberal Republican Radical | Capital is in the Balkans Either: Is a Croatian, Serbian, Bosniak, or Slovene country Is a Bulgarian country and has pursued Greater Yugoslavia Is not Yugoslavia Either Croatian, Serbian, Bosniak, or Slovene culture has at least 10 fervor | Is [Yugoslavia](Yugoslavia.md) | Liberal Nationalist |
|  | Dominican National | National Liberal | Ethno-Nationalist Market Liberal Liberal Republican Radical Reformer | Owns Santo Domingo Does not have Caribeño as a primary culture | Does not own Santo Domingo |  |
|  | Utilitarian | Utilitarian | Utilitarian | Has English, Anglo-Canadian, or Australian primary culture |  | Liberal |
|  | Orleanist | Orléanist | Orléanist | Is France or a French revolter Has not stamped out monarchy or cemented a different dynasty | Has stamped out monarchy or cemented a different dynasty | Conservative |
|  | Legitimist | Legitimist | Legitimist | Is France or a French revolter Has not stamped out monarchy or cemented a different dynasty | Has stamped out monarchy or cemented a different dynasty | Conservative |
|  | Bonapartist | Bonapartist | Bonapartist | Is France or a French revolter Has not stamped out monarchy or cemented a different dynasty | Has stamped out monarchy or cemented a different dynasty | Conservative |
|  | Carlist | Carlist | Carlist | Primary culture is Spanish, Catalan, or Basque Has not stamped out monarchy Capital is in Iberia | Either: Has stamped out monarchy Capital is not in Iberia | Conservative |
|  | Miguelist | Miguelist | Miguelist | Primary culture is Portuguese Has not stamped out monarchy Capital is in Iberia | Either: Has stamped out monarchy Capital is not in Iberia | Conservative |
|  | Restorationist | Shōjōi | Jingoist Protectionist Mitogaku Shōjōi | Primary culture is Japanese Has Bakufu Is Japan or a subject of Japan | Has stamped out monarchy Meiji reforms have been completed | Nationalist |
|  | Tokugawa Loyalist | Bakufu | Authoritarian | Primary culture is Japanese Has Bakufu Is Japan or a subject of Japan | Has stamped out monarchy The Emperor has been restored | Conservative |
|  | Hindu Nationalist | Minoritarian Traditionalist | Fascist Theocrat | Is East India or Hindustan Has researched Pan-nationalism Owns any state with an Indian culture homeland and a Hindu pop Owns at least five if Hindustan |  |  |
|  | Muslim Nationalist | Minoritarian Traditionalist | Social Democrat Theocrat | Is East India or Maharashtra Has researched Pan-nationalism Owns at least five states with an Indian culture homeland and a Sunni, Shiite, or Ibadi pop |  |  |
|  | Slave Revolt | Anti-Slavery | Abolitionist Humanitarian Radical | Does not have any variant of Slavery Banned Either: At least 15% of country's population is slaves At least 55% of any state's population is slaves | Has any variant of Slavery Banned |  |

### Starting movements

Every country starts with a number of movements depending on its starting circumstances. Certain countries have a specified set of movements instead of or in addition to these.

| Movement | Conditions | Excluded countries |
|---|---|---|
| Absolutist | Has Monarchy Does not have voting Does not have Bakufu | [France](France.md) [Portugal](Portugal.md) [Spain](Spain.md) [Carlist Spain](Carlist Spain.md) |
| Royalist | Has Monarchy Has voting or is Portugal | [France](France.md) |
| Pro-slavery | Has any kind of slavery except Colonial Slavery |  |
| Abolitionist | Has any kind of slavery Has researched Empiricism | [East India](East India.md) |
| Religious majority |  | [East India](East India.md) [France](France.md) [Spain](Spain.md) [Carlist Spain](Carlist Spain.md) [Portugal](Portugal.md) |
| Cultural majority |  | North and South German countries North and South Italian countries |
| Labor | Has researched Labor Movement |  |
| Liberal | Has voting Has researched Democracy | [France](France.md) |

| Country | Movements |
|---|---|
| [Cuba](Cuba.md) [Puerto Rico](Puerto Rico.md) | Slave Revolt (Afro-Caribeño) |
| [Brazil](Brazil.md) | Slave Revolt (Afro-Brazilian) |
| [France](France.md) | Bonapartist Legitimist Orleanist Radical |
| North and South German countries | German National |
| North and South Italian countries | Italian National |
| [Serbia](Serbia.md) [Croatia](Croatia.md) | Yugoslav/Illyrian National |
| [Austria](Austria.md) | Cultural minority (Polish) Cultural minority (Czech) Cultural minority (North Italian) Liberal (suppressed) |
| [Hungary](Hungary.md) | Cultural minority (Serbian) Liberal |
| Prussia Russia | Cultural minority (Polish) |
| [Haiti](Haiti.md) | Dominican National |
| [Spain](Spain.md) | Carlist (suppressed) Liberal |
| [Carlist Spain](Carlist Spain.md) | Carlist Liberal (suppressed) Cultural minority (Basque) |
| [Portugal](Portugal.md) | Miguelist (suppressed) Liberal |
| [Great Britain](Great Britain.md) | Cultural minority (Irish) |
| Ottoman Empire Paraguay Siam | Modernization |
| [East India](East India.md) | Utilitarian Religious minority (Hindu) Religious minority (Sunni) Cultural minority (Bengali) |
| [Ontario](Ontario.md) [Quebec](Quebec.md) | Radical |
| [Japan](Japan.md) | Restorationist Tokugawa Loyalist Land Reform |

## Support

A movement gains one third of its support each from the number of supporting [pops](Pops.md), number of supporting military personnel, and amount of supporting wealth.

- 0.34% for each percentage of country's population supporting the movement
- 0.33% for each percentage of military personnel supporting the movement
- 0.33% for each point raw pop political power supporting the movement

#### Bolstering and suppression

| Impact source |  |  |
|---|---|---|
| Outlawed Dissent | **+50%** | **−50%** |
| Censorship | **+40%** | **−40%** |
| Right of Assembly | **+30%** | **−30%** |
| Per Home Affairs level with Secret Police | — | **−5%** |

Political movements can be *bolstered* or *suppressed* to affect their pop attraction. It costs **200** Authority to bolster or suppress a political movement and the action can be cancelled at any time. The ability to bolster or suppress any interest group also depends on the country having bolstered or suppression *impact*. This comes from laws, institutions, or modifiers. If its value is 0%, movements cannot be bolstered or suppressed.

The bolster or suppress impact is a modifier to the pop attraction values.

## Activism

Movements gain activism based on its stances towards the country's current laws as well as various other factors depending the movement. Activism changes by 1% each week towards the target level.

| Source | Impact |
|---|---|
| Per enacted law Multiplied by stance direction and level | **±5** |
| Per recently enacted law Multiplied by stance direction and level | **±25** |
| Radical supporting pops Scaled by percent of all supporting pops | **+100** |
| Loyalist supporting pops Scaled by percent of all supporting pops | **−75** |

| Movement | Source | Impact |
|---|---|---|
| Abolitionist Movement | Leader or their interest group supports slavery | **+10%** |
| Is [America](America.md) and has *The Slavery Debate* active | **+20%** |  |
| Average Standard of Living of slave pops | **+50%** to **-25%** |  |
| Pro-Slavery Movement | Leader or their interest group opposes slavery | **+10%** |
| Is [America](America.md) and has *The Slavery Debate* active | **+20%** |  |
| Less than 50% of barracks located in slave states | **+50%** |  |
| Less than 50% of naval administrations located in slave states | **+25%** |  |
| Absolutist/Royalist Movement | Legitimacy above/below 50 | **±0.5%** per point, from **+25%** to **-25%** |
| Monarchy is being abolished | **+25%**[1] |  |
| Labor/Socialist/Communist Movement | Investment level in Workplace Safety and Social Security[2] | **+5%** for each level below 3, or **+10%** for no institution; **-5%** for each level above 3 |
| Socialist Movement | Standard of Living below 15 | **+3%** for each point of SoL under 15 |
| Socialist/Communist/Anarchist Movement | Factory Councils is being abolished | **+25%** |
| Anarchist Movement | Standard of Living below 15 | **+1.5%** for each point of SoL under 15 |
| Communist/Anarchist Movement | Movement support | **+0.5%** for each point of support, up to **+25%** |
| Fascist Movement | Movement support | **+1%** for each point of support, up to **+50%** |
| Claims | **+12.5%**, plus **+2.5%** for each claim up to a total of **+30%** |  |
| Liberal/Radical/Corporatist/Utilitarian Movement | Low Investment in Education | **+5%** for each level below 3, or **+10%** for no institution (**+5%** for no institution for the Utilitarian Movement) |
| Liberal Movement | Low Electoral Confidence | **+0.2%** for each percentage point of Electoral Confidence below 100%, once it falls below 90%; capped at **+20%** and scaled based on electoral confidence impact |
| Is [Portugal](Portugal.md) and has *Reign of the Devourers* active | **+20%** |  |
| Radical Movement | Low Electoral Confidence | **+0.2%** for each percentage point of Electoral Confidence below 100%, once it falls below 90%; capped at **+20%** |
| Investment in Law Enforcement | **+5%** for each level above 2, **-5%** for level 1, **-10%** for no institution |  |
| Lack of Universal Suffrage | **+15%** |  |
| Reactionary Movement | Percentage of radical pops | **+0.5%** per percentage point, up to **+50%** |
| Modernization Movement | War goal enforced against by a recognized power | **+10%** |
| Is unrecognized and has researched Nationalism | **+10%** |  |
| Cultural and Religious Majority Movements | ruler does not belong to the primary culture/religion | **+10%** |
| Neighboring revolutionary movement of the same culture/religion | **+15%** |  |
| Standard of Living below national average for pops of this culture/religion | **+5%** per point of SoL under national average, up to **+50%** |  |
| Poor relations with [Papal States](Papal States.md) (Catholic religion only) | Up to **+25%** at −100 relations |  |
| Cultural Majority Movement | Has researched Nationalism, and this culture has a homeland state not owned by any country with it as a primary culture | **+2.5%** per state, up to **+25%** |
| Cultural Minority Movement | Fervor of culture | **+0.25%** per point of fervor, unless the culture is at Full Acceptance |
| Low acceptance of culture | **+10%** to **+30%** |  |
| Cultural and Religious Minority Movements | Standard of Living below national average for pops of this culture | **+5%** per point of SoL under national average, up to **+50%** |
| Low support within identity | **-1%** per point of support under **50%** for religious movements, or **25%** for cultural movements |  |
| Poor relations with [Papal States](Papal States.md) (Catholic religious minorities only) | Up to **+25%** at −100 relations |  |
| Neighboring revolutionary movement of the same culture/religion | **+15%** |  |
| Support for other insurrectionary movements | **+0.25%** for percentage of pops supporting other movements, up to **+25%** |  |
| Indian National, Hindu Nationalist and Muslim Nationalist | Liberty desire | **+0.2%** per point, up to **+20%** |
| Is a subject (Indian National) | **+25%** (**+10%** if a dominion) |  |
| Is a subject (Hindu Nationalist, Muslim Nationalist) | **+15%** (**+5%** if a dominion) |  |
| German, Italian and Yugoslav National Movements | ruler does not belong to a primary culture | **+10%** |
| Has researched Nationalism and another country is a unification candidate | **+10%** |  |
| Has researched Pan-nationalism and does not own all core states | **+10%** |  |
| Average fervor of German, Italian or Yugoslav cultures | **+0.25%** per point, up to **+25%** |  |
| German National Movement | Has *The Schleswig-Holstein Question* active | **+10%** |
| French, Spanish and Portuguese Monarchists | Monarch is of a different dynasty | **+25%** |
| Legitimist, Carlist and Miguelist Movements | Poor relations with [Papal States](Papal States.md) | Up to **+25%** at −100 relations |
| Carlist Movement | [Spain](Spain.md) has the JE *The First Carlist War* active | **−95%** |
| Slave Revolt Movement | Leader or their interest group supports slavery | **+10%** |
| Average Standard of Living of slave pops | **+30%** to **-25%** |  |
| Slave population compared to Army Power Projection | **+75%** to **-50%** |  |

When starting or cancelling a law enactment, half of the new target activism is applied immediately, while the rest ticks up as usual.

Movements with less than 25% activism do not affect enactment success and failure chances. Additionally, while a law the movement has a stance on is being enacted, activism cannot drop below 25%.

Movements that have more than 50% activism become *obstinate .*

Movements that have more than 75% activism become *revolutionary*.

Movements that have more than 50 activism also increase pop radicalism. Each month between **0.5%** and **2.5%** of pops supporting the movement become more radical.

## Revolution

A revolutionary movement begins organizing towards starting a civil war. This is represented by a progress bar from 0% to 100%. If the bar reaches 100%, the revolution starts a [diplomatic play](Diplomatic play.md) to overthrow the country's current government. If this happens, the player can choose to play as either the government or the revolution. Revolutions can thus be used as a tool for political and social change in the player's country.

Revolution progress is based primarily on the movement's radicalism, but [certain events](Revolution events.md) can also increase or decrease progress. Revolution progress is updated periodically, with a base interval of 8 weeks. Each checkpoint also triggers a revolution event.

If the political movement disbands or has less than 50 radicalism, the revolution stops organizing immediately.

### Revolution progress

Each checkpoint, revolution progress changes towards the movement's radicalism value. The amount of change is capped between **−10%** and **+25%**. A movement with less than 100 radicalism never becomes a civil war unless an event tips the progress over 100%.

### Revolution states

While the revolution is organizing, hovering over it shows which states are likely to join the revolution. The proportion of states is equal to 1.5 times the movement's support, capped at 75% of the country's states. If the country has only a single state, the state is split, instead.

The chance of each state to join the revolution is based on the local clout of interest groups supporting the revolution with an additional bias for adjacent states to avoid a patchwork situation.

### Civil war

Once revolution progress reaches 100%, the revolution immediately forms a revolutionary country and starts a revolution [diplomatic play](Diplomatic play.md). During the *opening moves* phase, the player can choose to switch sides and play as the revolution rather than the government. Other countries may join the diplomatic play as normal, though not all sways are available.

The revolutionary country is based on the main country's definition, which means that changes during gameplay to recognition, primary cultures, and state religion are not copied. The revolutionary country does copy researched technology. Laws are all copied as well, except that the movement's desired law is enacted, plus up to two more laws that are preferred by the supporting interest groups. The original country keeps all diplomatic pacts, and the revolutionary country starts with none. All characters affiliated with the revolutionary interest groups switch to the new revolutionary country.

All radicals in pops supporting the rebelling interest groups become neutral when a civil war starts.

### End of the civil war

When the civil war ends, 50% of all radicals become neutral, with an additional 25% in pops that supported defeated interest groups and 50% in pops in that supported victorious interest groups.

Losing interest groups also suffer **−100%** political strength for 10 years.

## References

1. ↑ Supplants legitimacy modifier if the monarchy is being abolished
2. ↑ Only Workplace Safety for Communist Movement

1. See /Victoria 3/game/common/defines/00_defines.txt: `NPolitics` for defines related to political movements and revolutions

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | [Government](Government.md) • [Capacities](Capacity.md) • [Characters](Character.md) • [Decrees](Decrees.md) • [Institutions](Institutions.md) • [Laws](Laws.md) • [Technology](Technology.md) |
|---|---|

| Politics | [Elections](Elections.md) • [Ideology](Ideology.md) • [Interest group](Interest group.md) • [Political lobby](Political lobby.md) • Political movement • [Political party](Political party.md) • [Revolution](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| Economy | [Buildings](Building.md) • [Goods](Goods.md) • [Harvest condition](Harvest condition.md) • [Infrastructure](Infrastructure.md) • [Market](Market.md) • [Production methods](https://vic3.paradoxwikis.com/Production_methods) • [State](State.md) • [Treasury](Treasury.md) |
|---|---|

| Diplomacy | [Diplomacy](Diplomacy.md) • [Diplomatic action](https://vic3.paradoxwikis.com/Diplomatic_action) • [Diplomatic play](Diplomatic play.md) • [Power bloc](Power bloc.md) • [Ranks](Rank.md) • [Subjects](Subject.md) • [Treaties](Treaty.md) |
|---|---|

| Warfare | [Warfare](Warfare overview.md) • [Land warfare](Land warfare.md) • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
