---
title: Treasury
source: https://vic3.paradoxwikis.com/Treasury
pageid: 3109
categories: [1.13, Economy]
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
Overview of the weekly treasury balance.
The country's **treasury** is its *gold reserve* or *loans*. It increases or decreases based on the country's **budget** which reflects its total sum of income and expenses each week.

The budget balance is updated automatically each Monday. Most regular income and expenses, such as [construction](https://vic3.paradoxwikis.com/Construction), are weekly. There are a handful of lump-sum gains or costs such as the Take on Debt treaty article, nationalization or privatization of buildings, and certain other effects.

Every [country](https://vic3.paradoxwikis.com/Country) (including [subjects](Subject.md)) has its own treasury and budget, and all money is nominalized as pounds for all countries. There are no direct inflationary effects over time; thus, a pound in 1836 is equal to a pound in 1936.

If a country ceases to exist, its debt or gold reserve simply disappears.

## Gold reserve

The gold reserve is a country's national stockpile of cash. While a country is debt-free, any budget surplus increases the gold reserve. Similarly, any budget deficit reduces the gold reserve.

A large gold reserve provides no direct benefit aside from allowing for extended deficit spending, such as during a costly war.

### Gold reserve limit

Each country has a gold reserve limit, which is a soft cap equal to 20% of its annual gross domestic product (GDP)[1], over which each surplus pound has diminishing returns on the gold reserve. For example, if a country has an enormous stockpile of gold, a surplus of £10K may only increase the stockpile by as little as £2K, meaning that the rest of the money has been wasted. Hence, a country that finds its gold reserves filling up may want to consider finding a way to reinvest some of that money to avoid such waste, or lower taxes to have the pops keep the money instead.

## Credit

| Additive sources | Amount |
|---|---|
| Base | **20%** |
| Banking | **−2%** |
| Central Banking | **−2%** |
| Mutual Funds | **−2%** |
| International Exchange Standards | **−2%** |
| Modern Financial Instruments | **−2%** |
| Multiplier sourcesThe sum of multipliers are applied to the sum of the additive interest rate, with a multiplier sum of 0 counting as ×1 | Amount |
| Great power | **−50%** |
| Major power | **−25%** |
| Laissez-Faire | **−25%** |
| Financial PrudenceFinancial PrudenceCountry modifier +5% Influence −25% Loan interest rate | **−25%** |
| Bulgarian RenaissanceBulgarian RenaissanceCountry modifier −20% Loan interest rate +20% Technology Spread +20% Aristocrats Investment Pool contribution efficiency +20% Capitalists Investment Pool contribution efficiency | **−20%** |
| Legacy of Regeneration (1) | **−20%** |
| Zaibatsu Oligopoly | **−20%** |
| National DividendsNational DividendsCountry modifier +20% Gold reserve limit −20% Loan interest rate | **−20%** |
| The Old Lady of Threadneedle Street | **−15%** |
| Treasury Bonds | **−10%** |
| Lines of Credit | **−10%** |
| Prominent Businessman | **−10%** |
| Yasuda | **−10%** |
| Enshrining the NewEnshrining the NewCountry modifier +10% Political Strength of Capitalists +10% Influence −10% Loan interest rate +20% Petite Bourgeoisie Pop Attraction +20% Political Movement Pop Attraction | **−10%** |
| Tempo of the Founding YearsTempo of the Founding YearsCountry modifier −10% Loan interest rate −20% Political Movement Pop Attraction +20% Capitalists Investment Pool contribution efficiency +20% Shopkeepers Investment Pool contribution efficiency | **−10%** |
| Legacy of Regeneration (2) | **−10%** |
| Secured Gold ReservesSecured Gold ReservesCountry modifier −10% Loan interest rate | **−10%** |
| Haute Finance | **−7.5%** |
| Declared Bankruptcy (decaying) | **+50%** |
| Revolutionaries Captured Gold ReservesRevolutionaries Captured Gold ReservesCountry modifier −25% Gold reserve limit +10% Loan interest rate | **+10%** |
| Bank RobberiesBank RobberiesCountry modifier +10% Loan interest rate | **+10%** |
| Wary InvestorsWary InvestorsCountry modifier +15% Loan interest rate | **+15%** |
| Insignificant power | **+25%** |
| Unrest in the Ministry of FinanceUnrest in the Ministry of FinanceCountry modifier +25% Loan interest rate −20% Tax Collection +10% Tax Waste | **+25%** |
| Unrecognized major power | **+50%** |
| Unrecognized regional power | **+75%** |
| Unrecognized power | **+100%** |

If the gold reserve is empty, then any budget deficit automatically results in taking on loans against its *national credit*. Loans incur a weekly *interest* expense based on the total principal borrowed and the country's annual interest rate; this expense is paid to pops with ownership shares. The annual interest rate of a country is determined primarily by [society technology](Society technology.md), [rank, and recognition status](Rank.md).

While a country has any loans, any budget surplus is automatically applied to pay down the principal. Additionally, another country can propose a Take on Debt treaty article. If the other country agrees, this transfers the entire principal to the initiating country.

As interest is paid to pops with ownership shares, maintaining loans can be a way of increasing the wealth, and thus political power, of certain professions based on the ownership [production methods](Production method.md) used. Additionally, deficit spending in order to construct new buildings or mobilize a country's army is often necessary. However, as the principal grows, the interest can become a larger and larger budget expense to the point that the country is unable to pay down the principal even when not spending on construction or mobilization.

### Credit limit

A country's credit limit is the maximum amount of principal it can borrow before going into *default*. This limit is based on its buildings' current *cash reserves* plus £100K plus 50% of its GDP[2]. Buildings start with a maximum cash reserves of £25k per level, except Trade Centers which have a maximum of £5k per level and ownership buildings which have a maximum of £10K per level. The technology Postal Savings increases the maximum by **+20%**. The actual cash reserve at any moment depends on a buildings profitability, but it tends to either the maximum for profitable buildings or zero for unprofitable buildings.

If a country's loan principal is 50% or more of its credit limit, then its economy is considered *unhealthy*.

If the country goes into default, all construction is paused and a **−5%** penalty to offense, defense, and [throughput](https://vic3.paradoxwikis.com/Throughput) is immediately applied, this penalty increase by **−1%** each week up to a maximum of **−50%**. If a country in default achieves a positive budget balance, whether by increasing income or reducing expenses, these penalties are removed.

While a country is in default, it can *declare bankruptcy* to erase its total debt and thereby exit default. Declaring bankruptcy cancels all buildings in the construction queue, wipes out the cash reserves of all buildings, sets all active [institutions](Institutions.md) to level 1. **10%** of pops become more radical and pops with ownership shares become an additional **+5%** more radical for each share they own. Additionally, the following penalties are applied, decaying over 10 years:

- **−75%** [Prestige](https://vic3.paradoxwikis.com/Prestige)
- **+50%** Loan interest rate
- **−75%** [Migration](Migration.md) attraction
- **−10%** [Market](Market.md) access price impact
- **−100%** Welfare payments
- **−95%** Institution size change speed
- **−75%** Leverage
- **−75%** Offense
- **−75%** Defense
- ![Warning](/images/thumb/c/cb/Warning.png/24px-Warning.png) Forces privatization of all nationalized buildings

## Investment pool

In addition to the national treasury, each country has access to an investment pool that represents certain [pops](Pops.md)' investment in the economy. The investment pool can be spent either on the construction of buildings or on privatizing nationally-owned or workforce-owned buildings, as determined by the country's [economic system](Economy laws.md).

Buildings constructed from the investment pool use a separate, private construction queue. When the investment pool is used for construction, it appears in the budget as a temporary income called *Investment Pool Transfer*. If investment pool contributions exceed expenses, the contributions accumulate and can be spent later. Note that the wages of construction sector employees are always paid by the national treasury.

If the investment pool privatizes a nationally-owned building, that cost is paid direct to the treasury, increasing the gold reserve or paying a portion of loan principal.

Under the Command Economy law, the investment pool is seized entirely as a lump sum income and all contributions are stopped, even if an eligible pop receives dividends.

### Contributions

The investment pool gains funds from pop contributions. These contributions are based on dividends paid to certain professions with ownership shares, namely aristocrats, bureaucrats, capitalists, clergymen, engineers, farmers, machinists, and shopkeepers; if another pop type has ownership shares, such as in a workforce-owned building, those pops do not contribute anything to the investment pool. Each type of pop contributes a percentage of its dividends to the investment pool. The default values for investment pool contribution, as well as when they are paid, are the following[3]:

- Farmers – **10%**
  - Through workforce-owned buildings.
- Machinists – **10%**
  - Through workforce-owned buildings.
- Bureaucrats – **15%**
  - Through financial districts with Government Run.
- Engineers – **15%**
  - Through workforce-owned buildings.
- Shopkeepers – **20%**
  - Through workforce-owned buildings.
  - Through shopkeeper-owned companies.
- Clergymen – **20%**
  - Through manor houses.
  - Through financial districts with Increased Clergy Oversight.
- Aristocrats – **20%**
  - Through manor houses.
  - Through aristocrat-owned companies.
- Capitalists – **30%**
  - Through financial districts.
  - Through capitalist-owned companies.

Industry Banned adds **+25%** contributions to aristocrats, for a total of **45%**.

Reinvestment from pops in ownership buildings that own subsistence buildings is multiplied by 0.5 ⋅ ⋅ the share of levels owned that are subsistence buildings {\displaystyle 0.5\cdot {\text{the share of levels owned}}{\text{ that are subsistence buildings}}} ![{\displaystyle 0.5\cdot {\text{the share of levels owned}}{\text{ that are subsistence buildings}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/c4ff14d7ea4fe1e29f08770204bfcec7cf98b8b4)

Factors that affect the size of dividends, and thus base contributions are as follows:

- Profitability – The gross profit (revenue − (wages + input costs)) of a building [owned](Building.md) by a contributing pop determines how much dividends are paid out.
- The [building's cash reserves](Building.md) – The abstracted stockpile of a building determines how much profit is used to expand the reserve instead of paying dividends. A full reserve means all of the profit is paid out to the owners.
- The [building's ownership](Building.md) – Each ownership type can make different pops owners. To get more investment pool, the pops with the highest contribution factor need to own the building.

These contributions can be boosted by increasing *investment pool contribution efficiency*; that is, the amount the pop contributes counts for more, rather than taking more from the pop. Factors that are affect investment pool contribution efficiency are:

- The [Economic System law](Economy laws.md) – Each law has a different set of efficiency modifiers.
- [Interest group](Interest group.md) traits – The Industrialists and Landowners have traits that increase the investment pool contribution efficiency for capitalists and aristocrats respectively, when they have high approval.
- Postal Savings [technology](Technology.md) – **+15%** Bureaucrats, engineers, farmers, machinists, and shopkeepers investment efficiency.

Note that the amount of dividend taxes has no direct influence on the investment pool because this contribution is done before taxes.

## Budget

A country's national budget is the sum total of its income and expenses.

There are many forms of income and expenses which are impacted by laws, diplomacy, and events.

### National income

The types of income are:

- *Taxes* – Income from pops, divided up by type as below.
- *Tariffs* – Income from imports and exports. The rate is determined by the current [trade policy](https://vic3.paradoxwikis.com/Trade_Policy) and market good policy.
- *Minting* – Income generated as a portion of GDP. Increased by technologies and by Gold Mines and Gold fields. Minting from GDP is calculated as 1/1000[4] of yearly GDP per week or 5.2%, capped at a base of 200K. Multipliers and other sources of minting are not capped.
- *Government Dividends* – Income paid to the national treasury from profits on government owned buildings.
- *Investment Pool Transfer* – Temporary income paid from the investment pool to offset the cost of construction goods during the construction of eligible buildings.
- *Diplomatic Pacts* – Income from other countries such as; [subjects](https://vic3.paradoxwikis.com/Subjects), [bankrolling](https://vic3.paradoxwikis.com/Bankrolling), or [war reparations](https://vic3.paradoxwikis.com/War_reparations).
- *Additional Income* – Income from events or other uncategorized sources.

#### Taxation

See also:
Economy laws#Taxation
Taxes are usually a country's primary income source. There are two general types of taxes and five common specific taxes: Consumption, Land, Per Capita, Income, and Dividend.

- *Poll taxes* are flat taxes levied on all pops of a certain type. Each pop liable to pay the tax pays the same amount, regardless of actual income, thus disproportionately affecting pops with lower income.[5]
  - *Land taxes* are levied exclusively on peasants and farmers working on subsistence farms.
  - *Per capita taxes* are levied on all pops except peasants and slaves.
  - *Heathen taxes* are levied on pops' whose religion is discriminated. Primarily, these are applied by the laws Millet System and People of the Book; [Caucasian Imamate](https://vic3.paradoxwikis.com/Caucasian_Imamate) can gain this as well by completing the *Gazawat* journal entry.
- *Percentage taxes* use a tax rate rather than a flat amount. This tends to bring more money from wealthier pops as they have higher wages and more expensive purchases.
  - *Consumption taxes* are levied on pops' purchases of specific goods. Levying a consumption tax costs authority. Every individual that buys the good pays the tax.
  - *Income taxes* are levied on pops' wages. Only wages are taxed; subsistence income is exempt.
  - *Dividend taxes* are levied on pops' dividends.

| Law | Taxation |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Type | Very low | Low | Medium | High | Very high |  |
| Under all Taxation laws | Consumption tax rate | **+15%** | **+20%** | **+25%** | **+30%** | **+35%** |
| Consumption-Based Taxation | Other effects | −25% Population bureaucracy cost −50% Consumption tax cost |  |  |  |  |
| Land-Based Taxation | Land tax | **+0.4** | **+0.55** | **+0.7** | **+0.85** | **+1** |
| Per-Capita Taxation | Land tax | **+0.2** | **+0.275** | **+0.35** | **+0.425** | **+0.5** |
| Per capita tax | **+0.4** | **+0.55** | **+0.7** | **+0.85** | **+1** |  |
| Income tax rate | **0 +5%** | **0 +7.5%** | **+10%** | **+12.5%** | **+15%** |  |
| Proportional Taxation | Income tax rate | **+10%** | **+15%** | **+20%** | **+25%** | **+30%** |
| Dividends tax rate | **0 +2.5%** | **0 +5%** | **+10%** | **+15%** | **+20%** |  |
| Graduated Taxation | Income tax rate | **+10%** | **+12.5%** | **+15%** | **+17.5%** | **+20%** |
| Dividends tax rate | **+10%** | **+15%** | **+20%** | **+25%** | **+30%** |  |
| Millet System People of the Book | Religious tax | **+0.4** | **+0.45** | **+0.5** | **+0.55** | **+0.6** |

There are no tax brackets, such that even Graduated Taxation – despite its name – applies the same tax rate to all pops regardless of income.

Regardless of taxation law, each tax level also carries additional effects for legitimacy, pop radicalism, and pop attraction for interest groups in government:

| Level | Very low | Low | Medium | High | Very high |  |
|---|---|---|---|---|---|---|
| Legitimacy | **+10 %** | **+5 %** | — | **−10 %** | **−20 %** |  |
| Radicals from political movements | **−20%** | **−10%** | — | **+50%** | **+100%** |  |
| Government IG pop attraction | — | — | — | **−10%** | **−20%** |  |
| Expected Standard of Living |  | **−1** | **−0.5** | — | **+1.5** | **+3** |
|  | **−2** | **−1.0** | — | **+2.5** | **+5** |  |
|  | **−3** | **−1.5** | — | **+3.5** | **+7** |  |

##### Unrealized taxes

Effective taxation relies on sufficient bureaucracy for the country and [taxation capacity](https://vic3.paradoxwikis.com/Taxation_capacity) in each state. Insufficient bureaucracy imposes a country-wide *tax waste*, which loses a percentage of taxes collected from pops to abstracted corruption or inefficiencies. Individual states can also gain tax waste from turmoil. Pops pay the full nominal tax rate, even when some portion of those taxes are lost to waste.

If taxation capacity is insufficient, the deficit percentage of tax is not collected and the pops keep that money. Tax collection can also be reduced by obstinance, up to **−10%** at **20%** obstinance (the maximum cap).

### National expenses

The types of expenses are:

- *Construction Goods* – The cost of goods required for current construction.
- *Government Wages* – The salary for pops in [government buildings](Building.md). Can be adjusted relative to the normal wage.
- *Government Slaves* – The upkeep of slaves working in government buildings.
- *Goods for Government Buildings* – The cost of goods for government buildings.
- *Military Wages* – The salary for pops serving in the [army and navy](https://vic3.paradoxwikis.com/Barracks). Can be adjusted relative to the normal wage.
- *Goods for Military Buildings* – The cost of goods for military buildings.
- *Welfare Payments* – The cost of subsidies paid to pops with wages below the threshold defined by the Social Security institution.
- *Subsidies* – The cost of subsidizing specific buildings to ensure they remain competitive.
- *Subventions* – Costs of subventing import or export of specific goods.
- *Diplomatic pacts* – Expenses paid to other countries such as; an [overlord](https://vic3.paradoxwikis.com/Overlord), [bankrolling](https://vic3.paradoxwikis.com/Bankrolling), or [war reparations](https://vic3.paradoxwikis.com/War_reparations).
- *Interest* – Interest charged on outstanding debt.
- *Additional Expenses* – Expenses from events or other uncategorized sources.

#### Government and military wages

In addition to setting the base wage, each level of government and military wages has additional effects on the country.

| Level | Very low | Low | Medium | High | Very high |
|---|---|---|---|---|---|
| Wage multiplier | **−30%** | **−15%** | — | **+15%** | **+30%** |
| Approval | **−2 %** | **−1 %** | — | **+1 %** | **+2 %** |
| Prestige | **−20%** | **−10%** | — | — | — |
| Authority | — | — | — | **+5%** | **+10%** |

| Level | Very low | Low | Medium | High | Very high |
|---|---|---|---|---|---|
| Wage multiplier | **−30%** | **−15%** | — | **+15%** | **+30%** |
| Approval | **−2 %** | **−1 %** | — | **+1 %** | **+2 %** |
| Prestige from army and navy | **−20%** | **−10%** | — | **+10%** | **+20%** |
| Training rate | **−75%** | **−50%** | — | — | — |
| Morale recovery | — | — | — | **+10%** | **+20%** |

## References

1. ↑ See /Victoria 3/game/common/defines/00_defines.txt `GOLD_RESERVE_LIMIT_FACTOR = 0.2`
2. ↑ See /Victoria 3/game/common/defines/00_defines.txt `COUNTRY_MIN_CREDIT_SCALED` and `COUNTRY_MIN_CREDIT_BASE`
3. ↑ See /Victoria 3/game/common/static_modifiers/00_code_static_modifiers.txt
4. ↑ COUNTRY_GDP_MODIFIER_DIVISOR
5. ↑ Poll taxes calculated as yearly rates on each individual. For example, with Land-Based Taxation at medium level, a pop of 5k peasants pays £67.3 land tax per week.

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | [Government](Government.md) • [Capacities](Capacity.md) • [Characters](Character.md) • [Decrees](Decrees.md) • [Institutions](Institutions.md) • [Laws](Laws.md) • [Technology](Technology.md) |
|---|---|

| Politics | [Elections](Elections.md) • [Ideology](Ideology.md) • [Interest group](Interest group.md) • [Political lobby](Political lobby.md) • [Political movement](Political movement.md) • [Political party](Political party.md) • [Revolution](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| Economy | [Buildings](Building.md) • [Goods](Goods.md) • [Harvest condition](Harvest condition.md) • [Infrastructure](Infrastructure.md) • [Market](Market.md) • [Production methods](https://vic3.paradoxwikis.com/Production_methods) • [State](State.md) • Treasury |
|---|---|

| Diplomacy | [Diplomacy](Diplomacy.md) • [Diplomatic action](https://vic3.paradoxwikis.com/Diplomatic_action) • [Diplomatic play](Diplomatic play.md) • [Power bloc](Power bloc.md) • [Ranks](Rank.md) • [Subjects](Subject.md) • [Treaties](Treaty.md) |
|---|---|

| Warfare | [Warfare](Warfare overview.md) • [Land warfare](Land warfare.md) • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
