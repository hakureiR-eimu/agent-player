---
title: Companies
source: https://vic3.paradoxwikis.com/Companies
pageid: 5397
categories: [1.13, Pages_with_obsolete_template_parameters, Economy]
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
This page discusses the mechanics of companies; for the power bloc principle, see
Power bloc § Companies
.
**Companies** represent particularly notable corporations or joint ventures. Each company is associated with one or several types of building in a country. The company can own and build levels of these buildings and provide bonuses to throughput and construction efficiency. Companies potentially provide additional national bonuses if the company is sufficiently productive.

## Establishment

| Source | Amt. |
|---|---|
| Corporate Charters | **+1** |
| Joint-Stock Companies | **+1** |
| Investment Banks | **+1** |
| Corporate Governance | **+1** |
| Macroeconomics | **+1** |
| Technocracy | **+1** |
| Companies III | **+1** |

Each country has a limited number of slots for companies. Slots are gained by researching certain [society technologies](https://vic3.paradoxwikis.com/Society_technologies), starting with Corporate Charters. Each Society technology directly following Corporate Charters adds **+1** additional company slot up to a maximum of 5 slots upon researching Macroeconomics. An additional company slot can be unlocked by enacting Technocracy or from the [power bloc](Power bloc.md) principle Companies III.

Each company has certain requirements before it can be established, typically building a minimum level of one of its associated buildings. Flavored companies tend to have stricter requirements, such as constructing the requisite building in a specific state. Additionally, 5 levels of an associated building in one state must be available to transfer to the company's ownership. This can be from private owners, nationally-owned, or a mix of both.

When a company is established, it cannot be disbanded for five years. Similarly, after a company is disbanded, it cannot be reestablished for four years. Companies which own a country cannot be disbanded.

### Company headquarter

Each company has an associated Company Headquarter building. This is an ownership building similar to Financial Districts and Manor Houses, but associated specifically with a particular company. When a company is established, its headquarter is immediately built in the state with enough eligible buildings and the highest productivity rating compared to other eligible states. The headquarter has as many levels as the company owns building levels; these are automatically added and removed. Company Headquarters have only a single production method – depending on the current law, power bloc principles and the company's ownership type, which have the effects listed below.

#### Regional headquarters

With the *investment rights* charter a company can establish a secondary regional HQ in a foreign country, which the country of origin has a Investment Rights [agreement](Treaty.md) with. The regional HQ will be established as soon as they own 5 buildings in the target country. The regional HQ will then be able to buy up, construct or expand buildings in that country using that country's own investment pool. The regional HQ will then send some of their earnings back to the main HQ's investment pool. On the other hand, the country where the regional HQ has been established, will get access to potential prestige goods as well as the company construction and throughput bonuses.

#### Building info

| Name | Values per level |  |  |  |
|---|---|---|---|---|
| (Regional) Company Headquarter | 0.1 Infrastructure usage 0. 5 Urbanization |  |  |  |
| Production method | Employees per level | Ownership shares | Ownership category | Requires |
| Privately Owned | +10 Capitalists +15 Clerks | 10 Capitalists shares | *This is added to each category below* | Not Divine Economics II Not Command Economy Not Cooperative Ownership |
| +15 Capitalists +10 Clerks |  | Full Capitalist Ownership |  |  |
| +15 Aristocrats +10 Clerks | 10 Aristocrats shares | Partial Aristocratic Ownership |  |  |
| +25 Shopkeepers | 05 Shopkeepers shares | Partial Shopkeeper Ownership |  |  |
| +25 Bureaucrats | 05 Bureaucrats shares | Partial Bureaucrat Ownership |  |  |
| +25 Academics | 05 Academics shares | Partial Academic Ownership |  |  |
| Increased Clergy Oversight | +10 Capitalists +25 Clergymen | 10 Capitalists shares 0 2 Clergymen shares | *This is added to each category below* | Divine Economics II Not Command Economy Not Cooperative Ownership |
| +15 Capitalists |  | Full Capitalist Ownership |  |  |
| +15 Aristocrats | 10 Aristocrats shares | Partial Aristocratic Ownership |  |  |
| +15 Shopkeepers | 05 Shopkeepers shares | Partial Shopkeeper Ownership |  |  |
| +15 Bureaucrats | 05 Bureaucrats shares | Partial Bureaucrat Ownership |  |  |
| +15 Academics | 05 Academics shares | Partial Academic Ownership |  |  |
| Government Run | +50 Clerks +50 Bureaucrats | 10 Bureaucrats shares 0 2 Clerks shares | Any | Command Economy |
| Worker Cooperative | +50 Clerks +50 Shopkeepers | 10 Shopkeepers shares 0 2 Clerks shares | Any | Cooperative Ownership |

### Executives

## Benefits

Buildings owned by an established company enjoy **+10%** throughput, and buildings constructed by a company have **+30%** construction efficiency. All countries also gain a scaled bonus based on their prestige rank, calculated as 10 ⋅ ⋅ ( 1 − − rank num of countries ) {\displaystyle 10\cdot (1-{\tfrac {\text{rank}}{\text{num of countries}}})} ![{\displaystyle 10\cdot (1-{\tfrac {\text{rank}}{\text{num of countries}}})}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/47bf5543d8272f1dedd4b78d10235587906db288). For example, [Kongo](Kongo.md) starts at rank 185, around the halfway point of all starting countriesincluding the "unranked" decentralized nations, and it has a starting prestige bonus of **+5%**. The top ten ranked countries always have **+10%**, as well as an additional **+1%** per rank up to **+10%** (**+20%** total) throughput and construction efficiency for the Rank #1 country.

The throughput bonus is scaled for a given building to the proportion of levels owned by companies. For example, a building with half of its levels owned by a company would receive **+5%** throughput – half of the base **+10%** throughput bonus – as well as half of the prestige bonus.

If a country has more established companies than slots, then each additional company adds a penalty to the throughput and construction efficiency bonuses, scaled to the overage ratio, with a minimum penalty of **×0.33**. For example, if a country has three companies but only two slots, it receives a companies slots − − 1 = 3 2 − − 1 = {\displaystyle {\tfrac {\text{companies}}{\text{slots}}}-1={\tfrac {3}{2}}-1=} ![{\displaystyle {\tfrac {\text{companies}}{\text{slots}}}-1={\tfrac {3}{2}}-1=}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/7b4e59112faabc017f0cd3516322624ce73e55ab) **×0.5** multiplier or 50% of the normal company bonuses. This also applies to the prestige bonus.

The power bloc principle Internal Trade II provides **+5%** company throughput and the principle Companies I provides **+10%** company throughput. This is additive with the base throughput and prestige rank bonus.

### Prosperity

Companies start with 0 prosperity. The current prosperity changes towards the target prosperity weekly by 0.2 to 1 depending on the number of fully employed building levels the company owns. With 20 or more fully employed levels, prosperity increases weekly by 1, and with 40 or more levels it decreases weekly by 0.2. These values scale down or up with fewer employed levels; for example, with only 10 fully employed levels, a company's prosperity would increase weekly by 0.6 or decrease by 0.8.

Target prosperity is set by a combination of company productivity, number of employed levels, and popularity of the executive. Productivity gives 50 times the companies relative productivity. This is equal to the average productivity of the companies owned building levels compared to the average productivity of all associated building levels not owned by the company. Each fully employed building level gives another 1, up to 50. Finally, each point of the executive's popularity gives 0.2, from −20 to 20. The maximum target cannot exceed 100, but it can be "buffered" if the total sum is over 100. For example, a company with a relative productivity of 1.5 (50% more productive than global average for its building types), with 10 employed levels and an executive with **−10** popularity would have a prosperity target of ( 50 ⋅ ⋅ 1.5 ) + 10 + ( 0.2 ⋅ ⋅ − − 10 ) = 75 + 10 − − 2 = 83 {\displaystyle (50\cdot 1.5)+10+(0.2\cdot -10)=75+10-2=83} ![{\displaystyle (50\cdot 1.5)+10+(0.2\cdot -10)=75+10-2=83}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/0a23de6fb60d52ff4e18d6ce5ce180a57e1fe7f4)

When a company reaches 100 current prosperity, its prosperity bonus activates. If the company later drops below 75 prosperity, its bonus deactivates. If a company is disbanded and later re-established, it starts with 0 prosperity again.

### Prestige goods

|  | Available only with the [Charters of Commerce](Charters of Commerce.md) DLC enabled. |
|---|---|

Many companies can produce [prestige goods](https://vic3.paradoxwikis.com/Prestige_goods). Companies producing flavored goods can do so immediately when prosperous, while companies producing generic goods require completing a journal entry first.

## Charters

| Source | Amt. |
|---|---|
| Corporate Charters | **+2** |
| Investment Banks | **+1** |
| Interventionism | **+1** |
| Agrarianism | **+1** |
| Industry Banned | **+1** |
| Laissez-Faire | **+2** |
| Cooperative Ownership | **+1** |
| Command Economy | **+1** |
| Technocracy | **+1** |
| Companies II | **+1** |
| Companies III | **+1** |
| Great power | **+1** |

Company charters unlock additional features for that company. There are five types of charters. Charters cost **100** authority each to maintain, unless the country has available *free charters*. Countries have a base of 1 free charter[1], with more gained as in the table on the right. Without Charters of Commerce, only Trade Rights can be granted.

| Charter | Requirements | Effects |
|---|---|---|
| Trade Rights |  | Allows company to build Trade Centers |
| The following require Charters of Commerce |  |  |
| Investment Rights |  | Allows construction of Regional Company Headquarters |
| Colonization Rights | Country can colonize a state Is not unrecognized | Company begins colonizing selected state, with a 20% speed bonus When the colony is completed, it creates a new company country, owned by this company. The new country is a chartered company of the company's owning country. |
| Industry Rights | Company does not already have industry rights Company has a selectable building to grant rights | Allows company to build and purchase the selected building type Revoking this charter does not remove ownership but does remove company bonuses |
| Monopoly Rights |  | Grants monopoly on the selected building type Company gains a −80% discount to privatizing monopolized buildings Private investment besides the company cannot construct monopolized buildings |

Monopoly rights and investment rights cannot be revoked within five years of being granted. Other charters can be revoked immediately. Trade rights cannot be revoked if the company owns any trade centers.

### Company countries

Countries created by the Colonization Rights charter are "owned" by that company and are chartered company subjects of the company's owning country. They get the construction efficiency and throughput benefits of the company, which apply to nationally owned buildings in addition to those owned by the company's HQ. For buildings associated with the company, these are the full benefits, though scaled to the company country's prestige, not the overlord's prestige. For other buildings, the benefits are reduced to only 1/5 of the full amount, but this applies to all buildings, even government funded buildings. If a company country becomes independent, it loses the connection to the owning company. Company countries can only be chartered companies and can only have chartered company subjects.

Newly established company countries have the following laws as well as the permanent modifier *Colonial Administration Colonial Administration Country modifier −50% Non-contiguous incorporation speed +100% Contiguous incorporation speed*:

| Power Structure | Economy | Human Rights |  |  |  |
|---|---|---|---|---|---|
| Governance Principles | Colonial Administration | Economic System | Extraction Economy | Free Speech | Censorship |
| Distribution of Power | Oligarchy | Trade Policy | Same as overlord | Labor Rights | No Workers' Rights |
| Citizenship | Subjecthood | Taxation | Same as overlord | Children's Rights | Child Labor Allowed |
| Church and State | Same as overlord | Land Reform | Same as overlord | Rights of Women | Same as overlord |
| Bureaucracy | Same as overlord | Colonization | Colonial Exploitation | Welfare | No Social Security |
| Army Model | Same as overlord | Policing | Same as overlord | Migration | Migration Controls |
| Navy Model | Same as overlord | Education System | No Schools | Slavery | Same as overlord |
| Internal Security | Same as overlord | Health System | No Health System | Labor Associations | Same as overlord |

At the start of the game, [East India Company](https://vic3.paradoxwikis.com/East_India_Company), [Hudson’s Bay Company](Hudson’s Bay Company.md), and [Russian-American Company](Alaska.md) are each owned by those respective companies. These are somewhat special as they don't have the same subject type restrictions and they do not start with the above laws or modifier.

## Basic companies

The following companies are available to all countries regardless of location or culture. Ownership is Full Capitalist Ownership unless specifically noted otherwise. These companies' names are dynamically generated and so are referred to by their designations in the game files here:

| Name / Ownership | Buildings | Industry charters | Prestige goods | Prosperity bonus | Requirements |
|---|---|---|---|---|---|
| Basic Agriculture 1 Partial Aristocrat | Wheat Farms Rye Farms | Maize Farms | Fine Grain | **+10%** Livestock Ranches throughput | Owns level 5 or higher Wheat Farms or Rye Farms |
| Basic Agriculture 2 Partial Aristocrat | Rice Farms Millet Farms Maize Farms | Rye Farms | Fine Grain | +10% Livestock Ranches throughput +10% Food Industries throughput | Owns level 5 or higher Rice Farms, Millet Farms or Maize Farms |
| Basic Fabrics Partial Aristocrat | Livestock Ranches Cotton Plantations | Textile Mills | Prime Meat | **+10%** Textile Mills throughput | Owns level 5 or higher Livestock Ranches or Cotton Plantations |
| Basic Colonial Plantations 1 Partial Aristocrat | Tea Plantations Opium Plantations | Tobacco Plantations | Pure Opium | **−10%** Radicals from movements | Owns level 5 or higher Opium Plantations or Tea Plantations |
| Basic Colonial Plantations 2 Partial Aristocrat | Coffee Plantations Sugar Plantations Tobacco Plantations | Tea Plantations | Reserve Coffee | **+10%** Colony growth speed | Owns level 5 or higher Coffee Plantations, Sugar Plantations or Tobacco Plantations |
| Basic Silk and Dye Partial Aristocrat | Silk Plantations Dye Plantations | Textile Mills | ![No](/images/thumb/0/04/No.png/24px-No.png) | +10% Influence +10% Textile Mills throughput | Owns level 5 or higher Silk Plantations or Dye Plantations |
| Basic Wine and Fruit Partial Aristocrat | Vineyard Banana Plantations | Sugar Plantations | ![No](/images/thumb/0/04/No.png/24px-No.png) | **+10%** Prestige | Owns level 5 or higher Vineyard or Banana Plantations |
| Basic Fishing | Fishing Wharves Whaling Stations | Shipyards | Select Fish | +10% Supply ships construction efficiency +5% Shipyards throughput | Owns level 5 or higher Fishing Wharves or Whaling Stations |
| Basic Forestry Partial Aristocrat | Logging Camps Rubber Plantations | Tooling Workshops | ![No](/images/thumb/0/04/No.png/24px-No.png) | +0.7 Infrastructure from population +15 Maximum infrastructure from population | Owns level 5 or higher Logging Camps or Rubber Plantations |
| Basic Oil | Oil Rigs | Coal Mines | ![No](/images/thumb/0/04/No.png/24px-No.png) | **+10%** State migration attraction | Owns level 5 or higher Oil Rigs |
| Basic Gold Mining | Gold Mines | Lead Mines | ![No](/images/thumb/0/04/No.png/24px-No.png) | +5% Minting +5% Loyalists from movements | Owns level 5 or higher Gold Mines |
| Basic Metal Mining | Iron Mines Lead Mines | Coal Mines | ![No](/images/thumb/0/04/No.png/24px-No.png) | +10% Steel Mills throughput +5% Pollution health effect impact | Owns level 5 or higher Iron Mines or Lead Mines |
| Basic Mineral Mining | Sulfur Mines Coal Mines | Iron Mines | ![No](/images/thumb/0/04/No.png/24px-No.png) | **+10%** Fertilizer Plants throughput | Owns level 5 or higher Sulfur Mines or Coal Mines |
| Basic Food Partial Aristocrat | Food Industries | Livestock Ranches Wheat Farms | Gourmet Groceries | **+5%** Birth rate | Owns level 5 or higher Food Industries |
| Basic Paper | Paper Mills | Logging Camps | Craft Paper | **+10%** Bureaucracy | Owns level 5 or higher Paper Mills |
| Basic Home Goods | Glassworks Furniture Manufacturies | Logging Camps Lead Mines | Stylish Furniture | **+7.5%** Loyalists from movements | Owns level 5 or higher Glassworks or Furniture Manufacturies |
| Basic Textiles | Textile Mills | Cotton Plantations Silk Plantations | Designer Clothes | **−10%** Radicals from movements | Owns level 5 or higher Textile Mills |
| Basic Steel | Steel Mills | Iron Mines Coal Mines | Refined Steel | **+5%** State construction efficiency | Owns level 5 or higher Steel Mills |
| Basic Metalworks | Tooling Workshops | Steel Mills | Precision Tools | **+5%** Manufacturing throughput | Owns level 5 or higher Tooling Workshops |
| Basic Shipyards | Shipyards | Logging Camps | ![No](/images/thumb/0/04/No.png/24px-No.png) | **+5%** Hull Attack Damage | Owns level 5 or higher Shipyards |
| Basic Chemicals | Fertilizer Plants Synthetics Plants | Sulfur Mines | Enriched Fertilizer | −5% Supply consumption +10% Fertilizer Plants throughput | Owns level 5 or higher Fertilizer Plants or Synthetics Plants |
| Basic Motors | Motor Industries Automotive Industries | Steel Mills | ![No](/images/thumb/0/04/No.png/24px-No.png) | +10% Army speed +10% Fleet speed | Owns level 5 or higher Motor Industries or Automotive Industries |
| Basic Munitions | Munition Plants Explosives Factory | Sulfur Mines Steel Mills | High-grade Explosives | **−10%** Military goods cost | Owns level 5 or higher Munition Plants or Explosives Factory |
| Basic Electrics | Electrics Industries | Iron Mines Rubber Plantations | ![No](/images/thumb/0/04/No.png/24px-No.png) | **+10%** Power Plant throughput | Owns level 5 or higher Electrics Industries |
| Basic Weapons | Arms Industries Artillery Foundry | Automotive Industries Steel Mills | High-powered Small Arms | +5% Army Offense +5% Army Defense | Owns level 5 or higher Arms Industries or Artillery Foundry |
| United Construction Conglomerate Partial Bureaucrat | Steel Mills Tooling Workshops Glassworks | Lead Mines | ![No](/images/thumb/0/04/No.png/24px-No.png) | **+20%** Construction sector throughput | Owns level 10 or higher Steel Mills, Tooling Workshops, or Glassworks Is in a power bloc with Construction III principle. |

## Flavored companies

Main article:
List of flavored companies
Many historical companies are represented as flavored companies. The AI is more likely to establish a flavored company over a basic one. These companies are typically tied to specific [states](State.md) or [cultures](Culture.md). As such they are heavily associated with certain [countries](Countries.md), but those tied to states are not technically limited to specific countries as in theory any country can conquer any state. The following are worth noting:

- If the (incorporated) state required does not specify full ownership, a split state will suffice.
- It is not possible for two countries to establish the same flavored company. It is always first come, first served.
- The required building levels must either be owned by the establishing country or its citizens (local workforce, Manor Houses, Financial Districts). Foreign ownership and rival (foreign) company ownership does not count.

## References

1. ↑ Technically 0, but most Economic System laws give +1

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
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
