---
title: Acceptance
source: https://vic3.paradoxwikis.com/Acceptance
pageid: 7195
categories: [1.13, Game_concepts]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

**Acceptance** represents how a pop is treated and considered within a country. A pop's *acceptance status* is determined primarily from its [culture](Culture.md) and [religion](Religion.md) relative to the country's [Citizenship and Church and State laws](Power structure laws.md) (and in India, the British Caste System laws). When a new cultural community forms in a state, pops of that culture have a temporary acceptance penalty of **−30**, which decays by **0.25** each month towards **0**. [Events](Events.md) can also have an effect.

Each pop has an acceptance score between 0 and 100 that determines its status. Certain combinations of laws and modifiers can have the acceptance theoretically go below 0 or above 100, but this has no effect as acceptance is capped at those limits.

## Acceptance statuses

| Status | Score | Migration desire |
|---|---|---|
| Violent Hostility | 0-19 | 100 |
| Cultural Erasure | 20-39 | 100 |
| Open Prejudice | 40-59 | 50 |
| Second-class Citizen | 60-79 | 20 |
| Full Acceptance | 80-100 | 0 |

There are five status levels, from least accepted to most accepted.

The effects of each level of acceptance largely depends on the [Citizenship laws](Power structure laws.md), such as prohibiting voting or allowing assimilation, as well as modifiers to wages, political strength, which buildings they can work in, and loyalism and radicalism.

There are however some effects that apply regardless of laws.

Each acceptance status has a base migration desire, which generally decreases as the pop is more accepted. Pops with higher migration desire are more likely to emigrate, if allowed.

Pops killed in war, either by combat or attrition, affect war exhaustion based on their status. This affects both sides of the war relative to the acceptance in each country of the killed pops. This exhaustion is in addition to the exhaustion gained from casualties.

An agitator of a culture with less than Open Prejudice status cannot be invited to the country.

### Violent Hostility

*"People with this status are so openly despised, vilified and prosecuted that members of the general public would rather eradicate them off the face of the earth than waste energy and time integrating them in society."*

Pops in this status have 100 base migration desire. War casualties cause no additional exhaustion.

### Cultural Erasure

*"People with this status find themselves under the heel of the dominant society whose primary goal is to erase these people’s culture, traditions and belief system. Only then would the dominant group begin to explore the ways in which these people can be assimilated into mainstream society."*

Pops in this status have 100 base migration desire. War casualties cause no additional exhaustion.

### Open Prejudice

*"People with this status are allowed to live alongside other members of society. However, this seemingly neutral state of coexistence comes at the cost of having their own customs and belief system perpetually scrutinized and disapproved of by their higher-level counterparts."*

Pops in this status have 50 base migration desire. War casualties cause 50% as much exhaustion for their own country and none for the enemy country.

### Second-class Citizen

*"People with this status nominally enjoy a great deal of societal benefits. Despite this, they are still perceived and treated subordinately by society, and are oftentimes faced with discrimination, limited rights and restricted access to resources and opportunities."*

Pops in this status have 20 base migration desire. War casualties cause 150% as much exhaustion for their own country and 50% as much for the enemy country.

### Full Acceptance

*"People with this status are fully accepted members of society, benefiting from boundless social mobility and privileged stability. Their core values, belief system and socioeconomic reputation shape the very societal fabric which everyone else aspires towards."*

Pops in this status have 0 base migration desire. War casualties cause 300% as much exhaustion.

## Sources

### Citizenship laws

See also:
Power structure laws#Citizenship

#### Acceptance

| Law | Primary Culture | Shared Heritage trait | Shared Heritage trait group | No shared Heritage trait group | Shared Language trait | Shared Language trait group | No shared Language trait group | Tradition trait | Cultural homelands |  |
|---|---|---|---|---|---|---|---|---|---|---|
| **Subjecthood** | +100 | +20 | +15 | +0 | +20 | +15 | +0 | +25 | +30 |  |
| **Ethnostate** | +100 | +20 | +10 | −10 | +15 | +5 | +0 | +10 | +0 |  |
| **National Supremacy** | +100 | +40 | +20 | −10 | +30 | +15 | −5 | +15 | +0 |  |
| **Racial Segregation** | +100 | +60 | +50 | −20 | +30 | +15 | −5 | +20 | +0 |  |
| **Cultural Exclusion** | +100 | +60 | +50 | +10 | +50 | +25 | +10 | +25 | +0 |  |
| **Multiculturalism** | +100 | +60 | +50 | +20 | +50 | +30 | +20 | +10 | +0 |  |

#### Status Effects

| Law | Violent Hostility | Cultural Erasure | Open Prejudice | Second-class Citizen | Full Acceptance |
|---|---|---|---|---|---|
| Subjecthood | +20% Radicalism increases Cannot vote Cannot assimilate −40% Political strength −40% Wages −50% Qualifications growth Cannot work in military buildings Restricted jobs in government-funded buildings Cannot work Upper or Middle Strata jobs in government-funded buildings | +10% Radicalism increases Cannot vote −30% Political strength −30% Wages −30% Qualifications growth Restricted jobs in government-funded buildings Cannot work Upper or Middle Strata jobs in government-funded buildings | −25% Vote strength −20% Political strength −20% Wages −10% Qualifications growth | +5% Loyalism increases −10% Political Strength −10% Wages | +10% Loyalism increases |
| Ethnostate | +33% Radicalism increases Cannot vote Cannot assimilate −50% Political strength −50% Wages −50% Qualifications growth Cannot work in military buildings Restricted jobs in government-funded buildings Cannot work Upper or Middle Strata jobs in government-funded buildings | +20% Radicalism increases Cannot vote +5% Assimilation −40% Political strength −40% Wages −30% Qualifications growth Restricted jobs in government-funded buildings Cannot work Upper or Middle Strata jobs in government-funded buildings | Cannot vote +15% Assimilation −30% Political strength −25% Wages −10% Qualifications growth | +20% Loyalism increases −10% Radicalism increases −50% Vote strength −15% Political strength −15% Wages | +33% Loyalism increases −20% Radicalism increases +25% Political strength +25% Wages |
| National Supremacy | +20% Radicalism increases Cannot vote Cannot assimilate −40% Political strength −40% Wages −50% Qualifications growth Cannot work in military buildings Restricted jobs in government-funded buildings Cannot work Upper or Middle Strata jobs in government-funded buildings | +10% Radicalism increases Cannot vote +5% Assimilation −30% Political strength −30% Wages −30% Qualifications growth Restricted jobs in government-funded buildings Cannot work Upper or Middle Strata jobs in government-funded buildings | −50% Vote strength +15% Assimilation −20% Political strength −20% Wages −10% Qualifications growth | +10% Loyalism increases −25% Vote strength −10% Political strength −10% Wages | +20% Loyalism increases −10% Radicalism increases +20% Political strength +20% Wages |
| Racial Segregation | Cannot vote Cannot assimilate −30% Political strength −30% Wages −50% Qualifications growth Cannot work in military buildings Restricted jobs in government-funded buildings Cannot work Upper or Middle Strata jobs in government-funded buildings | Cannot vote +5% Assimilation −20% Political strength −20% Wages −30% Qualifications growth Restricted jobs in government-funded buildings Cannot work Upper or Middle Strata jobs in government-funded buildings | −25% Vote strength +15% Assimilation −10% Political strength −10% Wages −10% Qualifications growth | +10% Political strength +5% Wages | +10% Political strength +15% Wages |
| Cultural Exclusion | Cannot vote Cannot assimilate −30% Political strength −30% Wages −50% Qualifications growth Restricted jobs in government-funded buildings Cannot work Upper or Middle Strata jobs in government-funded buildings | −25% Vote strength +5% Assimilation −20% Political strength −20% Wages −30% Qualifications growth | +15% Assimilation −10% Political strength −10% Wages −10% Qualifications growth | +10% Political strength | +10% Political strength +5% Wages |
| Multiculturalism | Cannot assimilate −20% Wages | +5% Assimilation −10% Wages | +15% Assimilation −5% Wages |  |  |

### Church and State laws

See also:
Power structure laws#Church and State
| Law | Acceptance for | Related effects |  |  |  |
|---|---|---|---|---|---|
| State Religion | Shared Religious trait | Shared Religious trait group | No shared Religious trait group |  |  |
| **State Religion** | **+25** | **+0** | **−10** | **−25** | +10% Wages for state religion −10% Wages for other religions |
| **People of the Book** | **+25** | **+5** | **+5** | **−25** | −50% Conversion Adds Heathen Tax |
| **Millet System** | **+25** | **+10** | **+10** | **−25** | −50% Conversion Adds Heathen Tax |
| **Freedom of Conscience** | **+20** | **+15** | **+5** | **+0** | +5% Wages for state religion −5% Wages for other religions No conversion for accepted Full Acceptance and Second-class Citizen pops |
| **Total Separation** | **+15** | **+15** | **+15** | **+15** | No conversion |
| **State Atheism** | **+15** | **+0** | **−5** | **−10** | +25% Conversion |

### Colonization

**No Colonial Affairs** adds 10 acceptance to pops in their cultural homelands.

## Tips

### For Citizenship laws

- *Multiculturalism* could be the best citizenship Law for it provides at least **+40** acceptance at the level of *Open Prejudice*, especially for those nations with smaller populations, or those that have acquired numerous culturally distinct provinces through colonial expansion or conquest.
- However, *Multiculturalism* is difficult to adopt as it requires *Human Rights* and *Slavery Banned* as preconditions, and lacks the support of any [interest groups](https://vic3.paradoxwikis.com/Interest_groups) with initial [ideology](Ideology.md). At this situation, *Cultural Exclusion* presents itself as an alternative option with at least **+20** acceptance at the level of *Cultural Erasure*.
- *Subjecthood* might be a preferable choice in the **beginning** of the game when you have no chance to adopt *Cultural Exclusion* as an **unrecognized country** or a country **starting on Slave Trade or Legacy Slavery**, for it provides **+30** acceptance from cultural homelands.

### For Church and State laws

- *Total Separation* is **NOT** a good choice, for it only provide **+15** acceptance at the most that cannot raise a level of acceptance when *Multiculturalism* or *Cultural Exclusion.*
- *Freedom of Conscience* is often the superior choice, as it grants a **+20** acceptance to pops of the state's religion. Under *Multiculturalism*, this can at total achieve a base acceptance **+60** acceptance at the level of *Second-class Citizen*, and not impose penalties on pops of other faiths. Under *Cultural Exclusion*, the base acceptance to pops of the state's religion is **+40**. *Freedom of Conscience* also allows Conversion as well.
- *State Religion* is less effective than *Freedom of Conscience* as it is likely to push acceptance to *Violent Hostility* or *Cultural Erasure*, due to its causes a **−5** or **−25** acceptance penalty from most religions, and **+25** acceptance to pops of the state's religion cannot raise them to a higher acceptance class than *Freedom of Conscience*. On the other hand, *State Religion* permits Conversion for pops of any acceptance level, and should you be able to stack Conversion rate bonuses through multiple avenues such as Religious Convocation [Power bloc](Power bloc.md), *Religious Schools*, [Russian-American Company](https://vic3.paradoxwikis.com/Russian-American_Company), etc., *State Religion* proves a sound choice.
- *State Atheism* might be the worst choice for it provides only **+15** acceptance bonus at the most and causes **−10** acceptance penalty at the worst.

## References

Game concepts
Return to top
| Pops | [Pops](Pops.md) • Acceptance • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
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
