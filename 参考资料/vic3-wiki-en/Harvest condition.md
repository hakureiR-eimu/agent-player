---
title: Harvest condition
source: https://vic3.paradoxwikis.com/Harvest_condition
pageid: 7196
categories: [1.13, Game_concepts, Lists]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

**Harvest conditions** are temporary phenomena that affect one or more state regions, primarily impacting agriculture, but they can also impact pops or other aspects of a state.

## Harvest condition mechanics

Each month approximately one third of state regions are checked for a harvest condition. If one is rolled, it sets the state as the *epicenter* and then affects neighboring states up to the random *range* away. If a state is already affected by a harvest condition, incompatible conditions cannot start in or affect that state, but are replaced by conditions which are not mutually incompatible.

A harvest condition lasts for a number of weeks, within its random *duration*. While a condition affects a state region, its effects are applied, multiplied by the harvest condition's *intensity*. Each affected state has its own duration and intensity.

Most harvest conditions can only affect relevant states, with a number of strategic regions or state regions specifically excluded for that condition.

### Regional restrictions

The following lists indicate state and strategic regions that are exempt from certain harvest conditions. Some regions are excluded from multiple conditions.

| Not vulnerable to Droughts All states in any of: Arctic Russia Baltic Canada Eastern Europe Finland Himalayas North Sea Coast Pacific Coast East Siberia West Siberia Urals The following states are vulnerable: Arizona California Connaught Highlands Leinster Lowlands Munster Nevada Ulster Utah |
|---|
| IS vulnerable to Earthquakes All states in any of: Anatolia Andes Balkans Bengal Caribbean Caucasus Central America East Siberia Ethiopia Gran Colombia Himalayas Iberia Indochina Indonesia Italy Japan La Plata Mexico Nile North Africa North China Oceania Pacific Coast Persia South China Zanj |
| Not vulnerable to Floods All states in any of: Anatolia Arabia Canada Caucasus Central Asia Ethiopia Great Plains La Plata Niger North Africa Oceania Persia Senegal Southern Africa |
| Not vulnerable to Frosts or Hailstorms All states in any of: Anatolia Arabia Bengal Bombay Brazil Caribbean Central America Central India Congo Dixie Ethiopia Gran Colombia Indochina Indonesia Madras Mexico Niger Nile North Africa Oceania Persia Punjab Senegal South China Southern Africa Zanj |
| Not vulnerable to Wildfires State has a Desert trait Does not include Sertão |
| IS vulnerable to Locust Swarms All states in any of: Andes Arabia Bengal Bombay Brazil Central India Ethiopia Gran Colombia Great Plains La Plata Madras Niger Nile North Africa Persia Punjab Senegal |
| Not vulnerable to Torrential Rains or Moderate Rainfall All states in any of: Anatolia Arabia Congo Ethiopia Niger Nile North Africa Oceania Persia Senegal Southern Africa Zanj |

## List of harvest conditions

| Condition | Incompatible with | Replaces | Range | Duration | Intensity | Effects | Chance |
|---|---|---|---|---|---|---|---|
| Disease Outbreak A desperate proliferation of rot and disease across crops, worrying farmers about the upcoming harvest. |  | Pollinator Surge | 1 | 36-96 | 3-11+ 3-7 base Plus value of Krakatoa temperature drop +2 during the Hungry Forties +2 more if an Irish homeland | −5% Urban Center throughput −5% Agriculture throughput −5% Plantations throughput −5% Ranching throughput +3% Peasants goods consumption | 0.0008 ×25 if 1840s, in Europe, and not the Hungry Forties ×100 if in Europe, the Hungry Forties, and has not had a disease outbreak within a year ×(1.5 plus five times Krakatoa temperature drop) +5 more if in Europe, North America, Central Asia, or East Asia |
| Drought A prolonged period of time devoid of rainfall which leaves the affected land in an arid and barren state. | Earthquake Flood Frost Hailstorm Moderate Rainfall Torrential Rains Tsunami | Heatwave Pollinator Surge Optimal Sunlight | 1-2 | 36-104 | 2-6 | −5% Agriculture throughput −5% Plantations throughput −5% Ranching throughput +10% Agriculture infrastructure usage +10% Plantations infrastructure usage +10% Ranching infrastructure usage +2.5% Peasants goods consumption | 0.0025 ×1.2 if ×1.5 if |
| Earthquake A violent, abrupt shaking of the Earth's surface that leaves ruin and devastation in its wake. | Tsunami | Drought Flood Frost Hailstorm Wildfire | 1-2 | 24-48 | 1-6 2-6 in the Ring of Fire geographic region 2-4 in the Alpide Belt geographic region 1-3 in the Great Rift Valley geographic region 1-2 otherwise | −5% Infrastructure −5% Market access price impact −5% Urban Center throughput −5% Agriculture throughput −5% Plantations throughput −5% Ranching throughput −5% Extraction throughput +2.5% Peasants goods consumption +5% Mortality | 0.0015 ×1.1 in the Great Rift Valley geographic region ×1.4 in the Alpide Belt geographic region ×1.5 in the Ring of Fire geographic region ×1.5 in Luzón |
| Extreme Winds A violent tempest that ravages the lands it passes through and is best avoided. |  | Pollinator Surge Locust Swarm | 1-2 | 36-104 | 2-5 | −5% Agriculture throughput −5% Plantations throughput | 0.0025 |
| Flood A stark reminder of nature's might, rising waters animated by incessant rainfall lay waste to the land and settlements alike. | Drought Earthquake Frost Tsunami Wildfire | Moderate Rainfall Optimal Sunlight Pollinator Surge Torrential Rains | 1-2 | 36-104 | 3-6 | −5% Infrastructure −5% Market access price impact −5% Agriculture throughput −5% Plantations throughput −5% Ranching throughput −5% Extraction throughput +3% Peasants goods consumption | 0.0025 ×1.2 if or ×1.1 if ×1.5 if |
| Frost A thin layer of ice that cloaks the lands in a delicate frozen blanket, as deceitfully beautiful from afar as it is devastating to the harvests underneath it. | Drought Earthquake Flood Heatwave Moderate Rainfall Optimal Sunlight Torrential Rains Tsunami Wildfire | Locust Swarm Pollinator Surge | 1 | 24-96 | 2-4+ 2-4 base Plus value of Krakatoa temperature drop | −5% Agriculture throughput −5% Plantations throughput +3% Peasants goods consumption | 0.0025 ×1.5 if |
| Hailstorm A form of precipitation in which falling lumps of ice inevitably damage crops and occasionally cause a bruise or two to anyone unlucky enough to get hit. | Drought Earthquake Heatwave Optimal Sunlight Tsunami Wildfire | Locust Swarm Moderate Rainfall Pollinator Surge | 1 | 24-96 | 2-4+ 2-4 base Plus value of Krakatoa temperature drop | −5% Agriculture throughput −5% Plantations throughput −5% Ranching throughput −5% Logging throughput | 0.0025 ×1.3 if or |
| Heatwave A suffocating mantle of abnormally hot weather where the ground sizzles like a scorching pan and the air overflows with oppressive heat. | Drought Frost Hailstorm Wildfire | Optimal Sunlight Pollinator Surge | 1-2 | 36-104 | 2-4 | −5% Agriculture throughput −5% Plantations throughput −5% Ranching throughput −5% Rubber Plantations throughput −5% Logging throughput | 0.0025 ×1.4 if |
| Locust Swarm A surge of flying insects that take to the skies pillaging crops in their wake. | Extreme Winds Frost Hailstorm Torrential Rains Wildfire | Pollinator Surge | 1-2 | 36-96 | 3-5 | −5% Agriculture throughput −5% Plantations throughput −5% Ranching throughput +3% Peasants goods consumption | 0.0015 |
| Torrential Rains A prolonged period of rainfall so heavy that even one's sturdiest umbrella cannot protect against the deluge. | Drought Flood Frost Wildfire | Locust Swarm Moderate Rainfall Optimal Sunlight Pollinator Surge | 1-2 | 36-104 | 2-5+ 2-5 base Plus value of Krakatoa temperature drop | −5% Agriculture throughput −5% Plantations throughput −3% Ranching throughput −3% Extraction throughput −10% Infrastructure +2.5% Peasants goods consumption | 0.003 ×1.3 if or |
| Wildfire A capricious and destructive fire whose wild flames lay waste to the land it roams. | Earthquake Flood Frost Hailstorm Moderate Rainfall Torrential Rains Tsunami | Heatwave Locust Swarm Optimal Sunlight Pollinator Surge | 1-2 | 24-94 | 4-8 | −5% Agriculture throughput −5% Plantations throughput −5% Ranching throughput −5% Extraction throughput +10% Agriculture infrastructure usage +10% Plantations infrastructure usage +10% Ranching infrastructure usage −5% Infrastructure +3% Peasants goods consumption | 0.0008 ×1.2 if ×1.3 if ×1.4 if |

| Condition | Incompatible with | Range | Duration | Intensity | Effects | Chance |
|---|---|---|---|---|---|---|
| Moderate Rainfall A joyous event that breathes life into land below, from which eager crops rise to greet the drops falling from above. | Drought Flood Frost Hailstorm Torrential Rains Wildfire | 1-2 | 36-104 | 2-4 | +5% Agriculture throughput +5% Plantations throughput +3% Ranches throughput −1% Peasants goods consumption | 0.003 |
| Optimal Sunlight An occasion that is neither too warm nor cold, emanating with such delight the ideal amount of brightness that one cannot help but smile as a result. | Drought Flood Frost Hailstorm Heatwave Torrential Rains Wildfire | 1-2 | 36-104 | 2-5 | +5% Agriculture throughput +5% Plantations throughput −1% Peasants goods consumption | 0.003 |
| Pollinator Surge A life-affirming frenzy of fragrances, nectar and vigor, set in motion by busy bees and other small insects dancing from flower to flower. | Disease Outbreak Drought Extreme Winds Flood Frost Hailstorm Heatwave Locust Swarm Torrential Rains Wildfire | 1 | 36-96 | 1-4 | +10% Plantations throughput +5% Fruit output | 0.0025 |

### Tsunami

Tsunami is a special harvest condition that is triggered only by the [Krakatoa](Krakatoa.md) eruption.

| Condition | Range | Duration | Intensity | Effects |
|---|---|---|---|---|
| Tsunami An unstoppable force of water flattening and subsuming anything where it meets the land | 1-5 | 36-78 | 3-6 for Indonesia, Indochina, and Oceania regions 1-3 otherwise | −5% Infrastructure −5% Market access price impact −5% Agriculture throughput −5% Plantations throughput −5% Ranching throughput −5% Extraction throughput +5% Peasants goods consumption +5% Mortality |

## References

- Harvest conditions are defined in /Victoria 3/game/common/harvest_condition_types/00_harvest_condition_types.txt
- Regional restrictions are defined in /Victoria 3/game/common/scripted_triggers/00_geography_triggers.txt

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | [Government](Government.md) • [Capacities](Capacity.md) • [Characters](Character.md) • [Decrees](Decrees.md) • [Institutions](Institutions.md) • [Laws](Laws.md) • [Technology](Technology.md) |
|---|---|

| Politics | [Elections](Elections.md) • [Ideology](Ideology.md) • [Interest group](Interest group.md) • [Political lobby](Political lobby.md) • [Political movement](Political movement.md) • [Political party](Political party.md) • [Revolution](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| Economy | [Buildings](Building.md) • [Goods](Goods.md) • Harvest condition • [Infrastructure](Infrastructure.md) • [Market](Market.md) • [Production methods](https://vic3.paradoxwikis.com/Production_methods) • [State](State.md) • [Treasury](Treasury.md) |
|---|---|

| Diplomacy | [Diplomacy](Diplomacy.md) • [Diplomatic action](https://vic3.paradoxwikis.com/Diplomatic_action) • [Diplomatic play](Diplomatic play.md) • [Power bloc](Power bloc.md) • [Ranks](Rank.md) • [Subjects](Subject.md) • [Treaties](Treaty.md) |
|---|---|

| Warfare | [Warfare](Warfare overview.md) • [Land warfare](Land warfare.md) • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
