---
title: Land warfare
source: https://vic3.paradoxwikis.com/Land_warfare
pageid: 1659
categories: [1.13, Articles_with_potentially_outdated_sections, Military]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

See also:
Warfare overview
,
Naval warfare
**Land warfare** is the primary method to defeat an enemy in war, by defeating their armies and occupying wargoals. Maintaining a sizeable and modern army is important for a country to preserve its independence and territorial integrity against aggression, or to engage in imperialistic actions. Armies consist of Battalions and Conscripts led by a General. Even if intended only for defense, a large and modern military increases a nation's amongst the world's powers.

When a new [diplomatic play](Diplomatic play.md) starts, a front – to which armies can be assigned – is automatically created at every land boundary between the two sides involved. New fronts can be created as nations join the diplomatic play while it is in progress. If it comes to war, fronts are dynamically created and destroyed as fronts move, invasions are made, and nations [capitulate](https://vic3.paradoxwikis.com/Capitulate) and leave the war.

## Battalions

Land units are called *Battalions*; these can be *regulars* standing units constantly employed, or *Conscripts*, called up only during war. Both types are generated from buildings which must hire pops for the unit's manpower. Battalions are always organized into one or more formations called *Armies*.

### Barracks and Conscription centers

The number of conscripts each state can support depends mainly on the population of the state, and thus can vary substantially.
Barracks and Conscription Centers are the buildings that generate battalions. Barracks generate regulars while Conscription Centers generate conscripts. Barracks and Conscription Centers cannot be built manually, but are instead built by adding battalions to an army. The maximum level of barracks in a state depends on the [Army Model law](Power structure laws.md) of the country. Each level of building produces one battalion when it reaches full employment (1000 individuals per level).

While barracks are effectively regular buildings, conscription centers are typically inactive and require activation to begin hiring and thus generating battalions. During a diplomatic play or war, conscription centers can be activated army-by-army, and they hire more quickly than barracks. Conscription centers can hire pops away from other buildings, potentially impacting a country's economy significantly. The maximum level of conscription centers depends on the *conscription rate* and workforce size of a state as well as the Army Model law.

| [Army Model laws](Power structure laws.md) | Military effects |
|---|---|
| **Peasant Levies** | +10% Morale loss +25 Barracks max level +25 Conscription Center max level +4% Conscription rate −10% Military goods cost −25% Unit experience gain +25% Aristocrats political strength |
| **Warrior Caste** | Japan-only alternative to Peasant Levies (available only with the Japanese primary culture) −15% Morale loss +50 Barracks max level +10 Conscription Center max level +1% Conscription rate +25% Officers political strength −10% Military goods cost +25% Military wages Limits officer qualifications to the upper strata |
| **Professional Army** | −10% Morale loss +100 Barracks max level +50 Conscription Center max level +1% Conscription rate +100% Unit experience gain +50% Officers political strength |
| **National Militia** | −5% Morale loss +5 Barracks max level +100 Conscription Center max level +5% Conscription rate +50% Leverage resistance −25% Officers political strength |
| **Mass Conscription** | +5% Morale loss +100 Barracks max level +100 Conscription Center max level +3% Conscription rate +100% Training Rate (Scaled by building level) +25% Officers political strength |

| Source | Amount |
|---|---|
| Unincorporated state | **−50%** |
| Mandatory Service | **+20%** |
| Army Reserves | **+20%** |
| Logistics | **+20%** |
| Enlistment Offices | **+20%** |
| War Propaganda | **+20%** |

Conscription rate is multiplied against each state's workforce size to determine the number of conscripts that can be recruited in the state. In addition to the Army Model law, the decree
Enlistment Efforts
adds
+5%
(and also grants
+25%
Training Rate) and the law
National Guard adds
+0.3%
per level of
Home Affairs institution investment (capped at level 5). Together, this results in a maximum base conscription rate of
9.5%
under Mass Conscription. There are multiplicative modifiers as well, primarily from
military technology
, but also
unincorporated states and various event modifiers. Note that multiplicative modifiers are called
Conscriptable Battalions
and while both are given as percentages, the multiplicative modifiers modify the base conscription rate rather than add to it. For example, an unincorporated state in a country with Peasant Levies (and no military technology) would have a conscription rate of
2%
(base
4%
times multiplicative
−50%
); adding the Enlistment Efforts decree to that state would increase conscription to
4.5%
, not
7%
.

### Unit types

Land units are divided into four categories: Infantry, Artillery, Cavalry, and Marines. In general, Infantry are better at defense while Artillery are better at offense. Cavalry primarily increase provinces captured from battles. Marines are exempt from the naval invasion efficiency penalty other units suffer, making them the preferred unit for amphibious landings. Armies are expected to be comprised of at least **50%** Infantry units and suffer organization penalties if the ratio is lower than this. A country with Peasant Levies (or Warrior Caste) can only use Infantry, excluding Mechanized, and Marines for conscripts; this does not affect regulars.

| Type | Stats | Upkeep |
|---|---|---|
| **Irregular Infantry** Always unlocked Can upgrade from: None | 10 Offense 10 Defense 15 Morale loss | — |
| **Line Infantry** Unlocked by: Line Infantry Can upgrade from: Irregular Infantry | 20 Offense 25 Defense 10 Morale loss | **1** Small Arms |
| **Skirmish Infantry** Unlocked by: General Staff Can upgrade from: Any previous | 25 Offense 35 Defense 10 Morale loss | 2 Small Arms 1 Ammunition |
| **Trench Infantry** Unlocked by: Trench Works Can upgrade from: Any previous | 30 Offense 40 Defense 8 Morale loss | 3 Small Arms 2 Ammunition |
| **Squad Infantry** Unlocked by: NCO Training Can upgrade from: Any previous | 40 Offense 50 Defense 6 Morale loss | 3 Small Arms 3 Ammunition 1 Radios |
| Not allowed for conscripts by Peasant Levies |  |  |
| **Mechanized Infantry** Unlocked by: Mobile Armor Can upgrade from: Any previous | 50 Offense 60 Defense 4 Morale loss +10% Devastation | 3 Small Arms 3 Ammunition 1 Radios 1 Oil 1 Tanks |

| Not allowed for conscripts by Peasant Levies |  |  |
|---|---|---|
| Type | Stats | Upkeep |
| **Cannon Artillery** Unlocked by: Artillery Can upgrade from: None | 25 Offense 15 Defense 10 Morale loss +10% Kill rate +10% Devastation −20% Army mobilization speed [1] −20% Army movement speed [1] | **1** Artillery |
| **Mobile Artillery** Unlocked by: Napoleonic Warfare Can upgrade from: Cannon Artillery | 30 Offense 15 Defense 8 Morale loss +20% Kill rate +15% Devastation −20% Army mobilization speed [1] −20% Army movement speed [1] | **2** Artillery |
| **Shrapnel Artillery** Unlocked by: Breech-Loading Artillery Can upgrade from: Any previous | 45 Offense 25 Defense 6 Morale loss +30% Kill rate +15% Devastation −20% Army mobilization speed [1] −20% Army movement speed [1] | 3 Artillery 3 Ammunition |
| **Siege Artillery** Unlocked by: Defense in Depth Can upgrade from: Any previous | 55 Offense 30 Defense 6 Morale loss +25% Kill rate +20% Devastation −20% Army mobilization speed [1] −20% Army movement speed [1] | 4 Artillery 4 Ammunition 1 Radios |
| **Heavy Tanks** Unlocked by: Mobile Armor Can upgrade from: None | 70 Offense 35 Defense 4 Morale loss +15% Morale damage +25% Kill rate +20% Devastation −20% Army mobilization speed [1] −20% Army movement speed [1] | 4 Artillery 4 Ammunition 1 Radios 3 Oil 3 Tanks |

| Not allowed for conscripts by Peasant Levies |  |  |
|---|---|---|
| Type | Stats | Upkeep |
| **Hussars** Unlocked by: Standing Army Can upgrade from: None | 15 Offense 10 Defense 10 Morale loss +25% Army mobilization speed [1] +25% Army movement speed [1] | **1** Grain |
| **Dragoons** Unlocked by: Line Infantry Can upgrade from: Any except Light Tanks | 20 Offense 25 Defense 8 Morale loss +30% Battle occupation | 1 Grain 2 Small Arms |
| **Cuirassiers** Unlocked by: Line Infantry Can upgrade from: Any except Light Tanks | 25 Offense 20 Defense 8 Morale loss +30% Battle occupation | 2 Grain 1 Small Arms |
| **Lancers** Unlocked by: Napoleonic Warfare Can upgrade from: Any except Light Tanks | 30 Offense 20 Defense 6 Morale loss +30% Battle occupation +5% Kill rate +5% Morale loss | 2 Grain 2 Small Arms 2 Iron |
| **Light Tanks** Unlocked by: Mobile Armor Can upgrade from: None | 45 Offense 45 Defense 4 Morale loss +30% Battle occupation +10% Devastation +20% Army mobilization speed [1] | 2 Artillery 2 Ammunition 2 Radios 2 Oil 2 Tanks |

| Exempt from the **−25%** naval invasion penalty |  |  |
|---|---|---|
| Type | Stats | Upkeep |
| **Shipboard Marines** Unlocked by: Line Infantry Can upgrade from: None | 20 Offense 25 Defense 10 Morale loss | **1.5** Small Arms |
| **Landing Marines** Unlocked by: Power of the Purse Can upgrade from: Shipboard Marines | 25 Offense 35 Defense 10 Morale loss | 2.5 Small Arms 1.5 Ammunition |
| **Assault Marines** Unlocked by: Landing Craft Can upgrade from: Any previous | 30 Offense 40 Defense 8 Morale loss | 4 Small Arms 3 Ammunition |

### Veterancy

| Source | Amt. |
|---|---|
| Peasant Levies | **-25%** |
| Professional Army | **+100%** |
| Military Drill | **+5%** |
| Granting Military Assistance | **+25%** |
| Receiving Military Assistance | **+50%** |

Units gain experience weekly and when reaching certain thresholds attain higher veterancy with bonuses to offense and defense. Units gain a base of **0.5** experience weekly, with an additional **5**[2] experience weekly when in battle. Whenever a unit takes casualties, newly recruited manpower starts at **0** experience, effectively reducing the total experience of the unit by a proportional amount. Conscripts gain experience while raised, but as they are disbanded when demobilized, lose all experience then.

Upgrading a unit reduces its level of veterancy by 1 and resets its experience to 0.

| Veterancy level | Effects | Total exp. | Exp. to level |
|---|---|---|---|
| Recruit | — | 0 | 100 |
| Regular | +5% Offense +5% Defense | 100 | 100 |
| Seasoned | +10% Offense +10% Defense | 200 | 200 |
| Veteran | +15% Offense +15% Defense +25% Morale damage | 400 | 400 |
| Elite | +25% Offense +25% Defense +50% Morale damage | 800 | — |

## Mobilization

It is possible to mobilize armies all at once, or one at a time. Mobilizing armies individually provides an estimate of the cost to the budget for the army's mobilization options, but does not estimate the effect of increased base upkeep.
In order to give a army an order, it must be mobilized. Mobilization takes between 5 and 20 days depending on state infrastructure and other factors.

In contrast to armies, fleets are always active and do not require mobilization.

### Conscription

Similarly to mobilization, *conscript* battalions can be activated army-by-army during a diplomatic play or war. Conscripts are hired when activated, rather than being employed as a standing unit, and take some time to fully mobilize. Once activated, conscripts cannot return to civilian life while mobilized. The number of conscripts available depends primarily on a country's [Army Model laws](Power structure laws.md) and its states' population. Many factors affect the conscription rate, such as unincorporated states having **−50%** conscription.

### Demobilization

Armies can be manually demobilized at any time. Demobilizing an army this way incurs a 90 decaying expense equal to the mobilization cost of that army's units, and the army cannot be remobilized until after 90 days have passed. All armies are demobilized for free when a country is at peace and not involved in any diplomatic plays. A demobilized army automatically returns to its home HQ.

### Mobilization options

Armies can be further enhanced through activating *mobilization options* at the cost of extra goods consumption per unit. All armies are required to provide Basic Supplies. Some options can be stacked (*inclusive*), while others are mutually *exclusive* with each other and activating one requires deactivating any others others. All effects of the same type stack additively. Mobilization option cannot be activated if their required goods are not available in the market. Their costs, including Basic Supplies, only apply while the army is mobilized.

| Category | Name | Requirements | Cost per unit | Effect | Activation penalty | Deactivation penalty |
|---|---|---|---|---|---|---|
| Supplies (![Yes](/images/thumb/7/77/Yes.png/20px-Yes.png) Inclusive) | Basic Supplies |  | 0.75 Grain +50% Small arms +50% Artillery +50% Ammunition +50% Oil +50% Radios +50% Tanks |  |  |  |
| Extra Supplies | Army Reserves | 1.5 Groceries +25% Small arms +25% Artillery +25% Ammunition +25% Oil +25% Radios +25% Tanks | −5% Morale Loss +10% Offense +10% Defense |  | **−50%** Morale |  |
| Luxurious Supplies | Military Statistics Extra Supplies activated | 1.5 Meat 1.5 Wine +25% Small arms +25% Artillery +25% Ammunition +25% Oil +25% Radios +25% Tanks | −5% Morale Loss +10% Offense +10% Defense |  | **−50%** Morale |  |
| Supplements (![Yes](/images/thumb/7/77/Yes.png/20px-Yes.png) Inclusive) | Chocolate |  | **1** Sugar | **+10%** Morale Recovery |  | **−50%** Morale |
| Tobacco |  | **0.5** Tobacco | **+10%** Morale Recovery |  | **−50%** Morale |  |
| Liquor |  | **0.5** Liquor | **+10%** Morale Recovery |  | **−50%** Morale |  |
| Opium |  | **0.5** Opium | **+10%** Morale Recovery |  | **−50%** Morale |  |
| Transportation (![No](/images/thumb/0/04/No.png/20px-No.png) Exclusive) | Forced March |  |  | +10% Movement Speed +25% Mobilization Speed +10% Morale Loss | **−50%** Morale |  |
| Truck Transport | Combustion Engine | **0.5** Automobiles | +30% Movement Speed +40% Mobilization Speed | **−50%** Organization | **−50%** Organization |  |
| Rail Transport | Railways | **0.5** Engines | **+20%** Movement Speed | **−50%** Organization | **−50%** Organization |  |
| Special Weapons (![Yes](/images/thumb/7/77/Yes.png/20px-Yes.png) Inclusive) | Machine Gunners | Automatic Machine Guns | 1 Small Arms [3] 1 Ammunition [3] | +5 Offense +10 Defense | **−50%** Organization | **−50%** Organization |
| Chemical Weapons | Chemical Warfare | **2** Fertilizer | +20 Offense +50% Kill Rate −20% Recovery Rate | **−50%** Organization | **−50%** Organization |  |
| Flamethrowers | Flamethrowers | **1** Oil[3] | +15 Offense +50% Devastation +10% Morale Damage | **−50%** Organization | **−50%** Organization |  |
| Reconnaissance (![Yes](/images/thumb/7/77/Yes.png/20px-Yes.png) Inclusive) | Motorized Reconnaissance | Combustion Engine | 1 Automobiles 0.5 Oil [3] | +50% Battle Occupation +30% Movement Speed +50% Chance of Surprise Maneuver chance | **−50%** Organization | **−50%** Organization |
| Balloon Reconnaissance | Militarized Industry III | 2 Fabric 0.5 Oil [3] | +80% Battle Occupation +50% Chance of Charted Terrain −20% Attrition | **−50%** Organization | **−25%** Organization |  |
| Aerial Reconnaissance | Military Aviation | 1 Aeroplanes 0.5 Oil [3] | +100% Battle Occupation +100% Chance of Rapid Advance −50% Chance of Lost | **−50%** Organization | **−50%** Organization |  |
| Medic Support (![No](/images/thumb/0/04/No.png/20px-No.png) Exclusive) | First Aid | Triage | 1 Fabric 2 Liquor | **+20%** Recovery Rate | **−25%** Organization | −50% Morale −25% Organization |
| Field Hospitals | Modern Nursing | 2 Opium 1 Tools | **+40%** Recovery Rate | **−25%** Organization | −50% Morale −25% Organization |  |

## Orders

Generals can be given two types of orders: Advance and Defend. Each of these have several specialized versions that modify the effects.

| Order name | Effects | Requirements |
|---|---|---|
| Advance Front | +5 General advancement speed +10% Offense | — |
| Reckless Advance | +7 General advancement speed +15% Offense +10% Morale loss −10% Recovery rate +100% Aggressive Maneuver chance +150% Blunder chance | General has Reckless |
| Pillage | +4 General advancement speed +20% Morale damage +10% Kill rate +100% Devastation −20% Occupation gain | General has any of: Cruel Wrathful Pillager |
| Cautious Advance | +3 General advancement speed −5% Morale loss +10% Recovery rate +50% Careful Maneuver chance | General has Cautious |
| Heavy Barrage | +2 General advancement speed +15% Morale damage +25% Kill rate +75% Devastation −10% Occupation gain | General has any of: Artillery Commander Experienced Artillery Commander Expert Artillery Commander Army contains 20% or more of single type of Artillery or Heavy Tanks |
| Rapid Advance | +7 General advancement speed +15% Casualties taken +10% Offense +10% Morale damage +10% Occupation gain | Army contains 30% or more of one type of cavalry |
| Heavy Advance | +2 General advancement speed +15% Offense −5% Morale loss −10% Occupation gain | General has Innovative Army contains 30% or more of Heavy Tanks |

| Order name | Effects | Requirements |
|---|---|---|
| Defend Front | **+10%** Defense | — |
| Adamant Defense | +15% Defense +20% Supply consumption +100% Dug In chance | General has any of: Defensive Strategist Experienced Defensive Strategist Expert Defensive Strategist |
| Counter Charge | +20% Casualties taken +15% Morale damage +25% Kill rate +50% Surprise Maneuver chance +50% Aggressive Maneuver chance | General has Brave Army contains 50% or more of one type of non-tank cavalry |
| Last Stand | +30% Casualties taken +20% Defense | General has any of: Stalwart Defender Trench Rat Defense-in-Depth Specialist |
| Delaying Tactics | +10% Defense +10% Morale loss +100% Surprise Maneuver chance +200% Camouflaged chance | General has any of: Pillager Cruel Wrathful Bandit Social Bandit Army contains 80% or more of Irregular, Skirmish, or Squad Infantry |

- Advance orders direct the general to attempt to occupy enemy-held territory; while no battle is occurring on the front, progress towards the next advance accumulates daily. When 100 progress is reached, the army engages any opposing army or advances occupation if there is no opposition. If both sides are advancing, this typically results in alternating attacks. Generals with Advance orders still defend against advancing enemy armies.
- Defend orders direct the general to prevent enemy advances. Generals ordered to defend can recapture friendly territory, but never occupy enemy territory.

Orders have no effects if the general's army is not assigned to a front.

## Fronts and theaters

Clicking on a front brings up a detailed view of the front, showing the armies on each side and the orders they have been given.
Once a country is engaged in a diplomatic play or war, *fronts* appear at each border between allied and enemy territory. A front is created for each pair of *theaters* − contiguous territory controlled by one side of the conflict.

An "interruption" in the border such as a sea or neutral country, does not count if both sides continue around the interruption in a single country, as for example [Russia](Russia.md) and the [Ottoman Empire](https://vic3.paradoxwikis.com/Turkey) around the Black Sea. If the interruption divides different countries on the same side, such as might happen with [Brazil](Brazil.md) fighting against [Bolivia](Bolivia.md) and [Argentina](Argentina.md), then separate fronts are created. Potentially separate fronts are joined together, however, if there is only one state region separating them, even if this creates a joined front on opposite sides of the same state.

Fronts advance state-by-state. Each time a battle is won, the winning side gains *occupation* score. This score takes control of a percentage of a state along the front. When a state is fully occupied by one side, the front moves to incorporate that state. When this happens, fronts may merge, split or, disappear altogether. If a front ceases to exist, armies assigned to that front automatically travel to another front or return to an HQ, usually the nearest one.

### Movement between fronts

To move armies between fronts, select the army, then select *Send to Front*, and then select the front, either in the table on the left-hand side of the window or by clicking on the front on the map. Accessible fronts are colored in green, and inaccessible fronts in red. In order to be assigned to a front, the army must be able to draw a supply line from its home HQ to the front. This means that it is not typically possible to support a landlocked front until occupying friendly territory from the nearest coast is possible or with military access through a neutral country. If a front becomes cut-off from a supply line, by the enemy occupying all coast for example, any generals cut-off this way return to the nearest friendly HQ which has a supply line to their home HQ.

Once the new front has been assigned, the army begins travelling to the front – to see how long this is likely to take, mouse over the circle representing the front, or select the army, and an indication of how many days it will take is shown. If an army changes fronts while in battle, it continues to fight the battle and moves once the battle concludes. Armies cannot be interecepted when traveling between fronts on land.

#### Overseas transportation

To send an army overseas, it is necessary to have select a fleet to transport the army. If the selected fleet does not have sufficient capacity, the army is divided up into portions that can be transported and the fleet makes multiple trips to transport the entire army. An army traveling overseas on a fleet can be intercepted by an enemy fleet, and if the transporting fleet is sufficiently damaged or destroyed, the transported army is similarly damaged or destroyed.

### Invasion

See also:
Naval invasions
Land invasions require an army and military access through every neutral country along the way to be performed. It cannot be initiated if it takes more than 30 days for the army to travel from its current station to the destination (for long distances, it may first prove necessary to mobilize the army in order to benefit from any potential speed bonuses).

Once an invasion is planned, a front is created at the targeted state and both the defender and the attacker can assign additional armies to this front (the 30 days travel time rule does not apply anymore). Defender's armies stationed in the region HQ **do not participate** in the defense of a land invasion. Attacking armies assigned to a invasion cannot be removed, nor their battalions detached, until the invasion has ended or is canceled.

It takes two weeks for battles to begin once the first invading army arrives, this gives the defending side a chance to bring an army to the invasion.

If the attacker loses three battles while having 0% occupation of the targeted state's territory, the invasion is defeated and the invading army must return to a friendly HQ. Any defending armies will also return to their nearest friendly HQ.

One the targeted state is fully occupied, the invasion is successful and a new regular front is created.

## Battles

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.9. |
|---|---|

Battle conditions can be quite influential, in both directions, to the outcome. Here, Austria has received a 20% bonus to morale damage, on top of having twice as many troops as Russia
For each side of a front where at least one general has been assigned an Advance order, an *advancement progress* bar fills up until it reaches 100, at which point that side starts an offensive battle. A number of battalions from each side are involved in the battle and the battle commences.

In a battle, the side attacking uses its *Offense* value, while the side defending uses its *Defense* value. The battle UI contains two tabs, with the overview displaying these values, the generals in charge and any modifiers to either side in the battle. The details tab provides more information on the modifiers affecting both sides in the battle.

Battles continue until either side runs out of morale or manpower, at which point that side retreats, and the side that won advances the front in their favor.

### Preparations for battle

Combat width tooltip, illustrating how fighting in mountains mostly negates the advantage of large army sizes.
Each general advancing at a front has a personal advancement progress, and multiple attacks by different generals are possible on the same front in parallel. Once a battle begins, advancement progress is paused. Currently, the UI only reflects the highest current progress, and does not show individual generals' progress. On the defense side, an available general is chosen, if possible, with more weight given to higher command limit and defensive traits. Other traits (terrain, artillery, other combat bonuses) are not taken into account.

The calculation of how many battalions can join the battle for each side is complex, with several factors. First, the each side counts the total number of available battalions; namely, all battalions on the front. Next, a penalty for *"Low concentration of battalions across length of Front"* is applied to each side. The formula for this is ⌊ rand ( 0 , [ total battalions on front − − total battalions on front total provinces on front ] / 2 ) ⌋ {\displaystyle {\Big \lfloor }{\text{rand}}(0,[{\text{total battalions on front}}-{\frac {\text{total battalions on front}}{\text{total provinces on front}}}]/2){\Big \rfloor }} ![{\displaystyle {\Big \lfloor }{\text{rand}}(0,[{\text{total battalions on front}}-{\frac {\text{total battalions on front}}{\text{total provinces on front}}}]/2){\Big \rfloor }}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/572611bb6517b8713258a3d8ccf9e2d002da8406)

For example, if a front has 10 provinces on it and a side has 100 battalions, the penalty is ⌊ rand ( 0 , [ 100 − − 100 10 ] / 2 ) ⌋ = ⌊ rand ( 0 , 45 ) ⌋ {\displaystyle {\Big \lfloor }{\text{rand}}(0,[100-{\tfrac {100}{10}}]/2){\Big \rfloor }={\Big \lfloor }{\text{rand}}(0,45){\Big \rfloor }} ![{\displaystyle {\Big \lfloor }{\text{rand}}(0,[100-{\tfrac {100}{10}}]/2){\Big \rfloor }={\Big \lfloor }{\text{rand}}(0,45){\Big \rfloor }}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/8bd7ad5bc69cfba4a8f90fabd3748b5fb5622331). The effect of this formula potentially penalizes longer fronts heavily, though as a random factor and never more than **−50%**.

The available battalions value is then capped by the battle province's combat width, which is equal to ⌈ ( 5 + 0.5 ⋅ ⋅ state infrastructure ) ⋅ ⋅ province terrain multiplier ⌉ {\displaystyle {\Big \lceil }(5+0.5\cdot {\text{state infrastructure}})\cdot {\text{province terrain multiplier}}{\Big \rceil }} ![{\displaystyle {\Big \lceil }(5+0.5\cdot {\text{state infrastructure}})\cdot {\text{province terrain multiplier}}{\Big \rceil }}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/7b78416a28b743af4a00bf3c123a1425d1931f3f)[4]; this is displayed a subtractive value equal to the difference between the pre-combat width cap and the combat width amount.

Finally for battles besides naval invasions, the side with a larger number of battalions gains a random bonus between 0 and up to ×3. The high end is calculated as ⌈ ( total own battalions on front total enemy battalions on front − − 1 ) ⋅ ⋅ 1.5 + 1 ⌉ {\displaystyle {\Big \lceil }({\frac {\text{total own battalions on front}}{\text{total enemy battalions on front}}}-1)\cdot 1.5+1{\Big \rceil }} ![{\displaystyle {\Big \lceil }({\frac {\text{total own battalions on front}}{\text{total enemy battalions on front}}}-1)\cdot 1.5+1{\Big \rceil }}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/68c8dd0701c81c1ae8aa8f3c1dd8f4796df0ca01). This is maximized when one side has at least **x2.33** more battalions than the other.

The final number cannot exceed the total number of battalions, nor go below 1.

Full formula
[5]
pre-combat width cap = total battalions on front − − ⌊ rand ( 0 , [ total battalions on front − − total battalions on front total provinces on front ] / 2 ) ⌋ {\displaystyle {\text{pre-combat width cap}}={\text{total battalions on front}}-{\Big \lfloor }{\text{rand}}(0,[{\text{total battalions on front}}-{\frac {\text{total battalions on front}}{\text{total provinces on front}}}]/2){\Big \rfloor }} ![{\displaystyle {\text{pre-combat width cap}}={\text{total battalions on front}}-{\Big \lfloor }{\text{rand}}(0,[{\text{total battalions on front}}-{\frac {\text{total battalions on front}}{\text{total provinces on front}}}]/2){\Big \rfloor }}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/79ab6f064448d45b3077f7e60564936bd3af0da5)

pre-final size = min ( pre-combat width cap , ⌈ ( 5 + 0.5 ⋅ ⋅ state infrastructure ) ⋅ ⋅ province terrain multiplier ⌉ ) {\displaystyle {\text{pre-final size}}={\text{min}}{\Big (}{\text{pre-combat width cap}},{\big \lceil }(5+0.5\cdot {\text{state infrastructure}})\cdot {\text{province terrain multiplier}}{\big \rceil }{\Big )}} ![{\displaystyle {\text{pre-final size}}={\text{min}}{\Big (}{\text{pre-combat width cap}},{\big \lceil }(5+0.5\cdot {\text{state infrastructure}})\cdot {\text{province terrain multiplier}}{\big \rceil }{\Big )}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/a3ff447bcc9830dfd6dd6565a8d7392ab9d1b289)

final size = { absolute minimum , 1 default , pre-final size if larger side on non-naval invasion , pre-final size ⋅ ⋅ ⌈ rand ( 1 , [ total own battalions on front total enemy battalions on front − − 1 ] ⋅ ⋅ 1.5 + 1 ) ⌉ absolute maximum , total available battalions {\displaystyle {\text{final size}}={\begin{cases}{\text{absolute minimum}},&1\\{\text{default}},&{\text{pre-final size}}\\{\text{if larger side on non-naval invasion}},&{\text{pre-final size}}\cdot {\Big \lceil }{\text{rand}}(1,[{\frac {\text{total own battalions on front}}{\text{total enemy battalions on front}}}-1]\cdot 1.5+1){\Big \rceil }\\{\text{absolute maximum}},&{\text{total available battalions}}\end{cases}}} ![{\displaystyle {\text{final size}}={\begin{cases}{\text{absolute minimum}},&1\\{\text{default}},&{\text{pre-final size}}\\{\text{if larger side on non-naval invasion}},&{\text{pre-final size}}\cdot {\Big \lceil }{\text{rand}}(1,[{\frac {\text{total own battalions on front}}{\text{total enemy battalions on front}}}-1]\cdot 1.5+1){\Big \rceil }\\{\text{absolute maximum}},&{\text{total available battalions}}\end{cases}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/fa657a6b78b542e093cfff14e57082111195e734)

Generals prefer to bring the strongest battalions available *on the front* (that is, in any allied formation deployed to that front, unless that formation has "Disable unit lending and borrowing" toggled") in to battle. This is based on each battalion's current manpower, multiplied by its morale, mobilization, and offense or defense value depending on whether attacking or defending, and finally doubled if the battalions is in the general's own formation rather than another formation. Battalions below **20%** morale or **100** manpower are unable to fight. Note that at this stage, there is no restriction to bring a certain proportion of infantry like there is with formation composition. For example, if the attacking side has enough artillery battalions to fill the limit, it can bring just artillery. Nor does the command limit of a general have any bearing on the number of battalions he can lead to battle: even if the above formula results in there being more battalions deployed than the general in charge can command (that is, battalions being borrowed from other formations deployed on the same front), they will still be able to fight and suffer no penalty.

### Battle

During combat, every tick (4 times a day) both sides damage each other's manpower and morale. The exact mechanics of this are not documented, but it appears that combat width (based on terrain) again restricts how many units can fight effectively. No additional reinforcements are possible at this stage, and the player cannot order an early retreat either.

Eventually, all battalions on one side run out of morale or manpower and are forced to leave combat, with the other side emerging victorious.

### Occupation

The winner of a battle gains a certain amount of *occupation* based on various factors such as the terrain and infrastructure present in the state. Occupying a state always takes at least two victories, and never more than four consecutive victories.

Once a state is fully occupied, the frontline moves to reflect this. As long as the war is ongoing, occupation only matters in terms of controlling [war goals](https://vic3.paradoxwikis.com/War_goals). [Buildings](https://vic3.paradoxwikis.com/Buildings) continue to function and supply their domestic market, even while they are temporarily occupied by an enemy nation.

### Battle conditions

Battle conditions represent tactics, weather, and chance occurrences that modify each side's effectiveness in one or more ways. A weighted random valid condition is chosen by each side at the start of the battle. After 10 days, there is an increasing chance to select a new condition.

Each province has one or more terrain features (for instance, a mountain province is both elevated and hazardous), and the weight is added for each feature present. All weights are multiplied by the general's multiplier for that battle condition, and all conditions except pursuit and retreat require an assigned general.

| Battle condition | Requirements | Weight | Effect |
|---|---|---|---|
| Pursuit | Is not retreating Current manpower is greater than: Twice enemy manpower if Panicked Retreat Four times enemy manpower if Controlled Retreat Ten times enemy manpower if not retreating | 1 (instant) | −100% Morale loss +1000% Combat width |
| Panicked Retreat | Is not Controlled Retreat Enemy is not Panicked Retreat Current manpower is less than: 10% starting manpower if commander experience level is above 5 20% starting manpower if commander experience level is above 4 30% starting manpower otherwise | 1 (instant) | −50% Offense −50% Defense −1000% Morale damage +50% Morale loss −50% Recovery rate |
| Controlled Retreat | Is not Panicked Retreat Enemy is not retreating Commander experience level is above 5 Current manpower is less than 20% starting manpower | 1 (instant) | −75% Morale damage +200% Morale loss +25% Recovery rate |
| Aggressive Maneuver |  | 1 +2 Logistics Secured +2 Mud | +20% Casualties taken +25% Morale damage |
| Blunder |  | 0.5 +2 Rapid Advance | +20% Casualties taken +15% Morale loss |
| Careful Maneuver |  | 1 +2 Mud | −10% Casualties taken −10% Morale loss |
| Good Visibility | Is defending Not Poor Visibility | 1 | −5% Morale loss +25% Defense |
| Poor Visibility | Not Good Visibility | 0.5 | −25% Offense −25% Defense |
| Broken Supply Line | Not Logistics Secured | 0.5 +1 if Elevated or Hazardous +2 if Water | **+25%** Morale loss |
| Camouflaged | Is defending | 1 +1 if Flat and Open Terrain Commander +1 if Forested and Woodland Combat Expert +2 if Elevated and Mountain Combat Expert +2 Dug In | **+10%** Defense |
| Charted Terrain | Not Blunder | 1 | **+15%** Kill rate |
| Dug In | Is defending Not Aggressive Maneuver | 1 +2 Camouflaged +2 Charted Terrain | −10% Morale loss +20% Defense |
| Exhausted |  | 0.5 +1 if Elevated or Hazardous +2 Broken Supply Line +2 Blunder +2 Surprise Maneuver +2 Rapid Advance +2 Mud | **+15%** Morale loss |
| Logistics Secured | Is advancing Not Broken Supply Line | 1 +2 Careful Maneuver | **−20%** Morale loss |
| Lost | Is advancing | 0.5 +1 if Forest or Mountain +2 if Jungle or Desert +2 Poor Visibility | −10% Offense −25% Defense +20% Morale loss |
| Mud | Not Dug In | 0.5 +0.5 if Hills +1 if Plains, Desert, River, Pasture, or Farmlands +2 if Wetland | −20% Offense −10% Defense +10% Morale loss |
| Rapid Advance | Is advancing | 1 +2 if Flat and Open Terrain Commander +1 if Forested and Woodland Combat Expert +1 if Elevated and Mountain Combat Expert +2 Charted Terrain +2 Aggressive Maneuver | **+20%** Provinces captured[6] |
| Surprise Maneuver | Not Poor Visibility | 1 +2 Dug In +2 Charted Terrain +2 Rapid Advance +2 Good Visibility | **+20%** Morale damage |

Countries fighting in a [guerilla war](Spanish content.md) use the following conditions instead of the regular ones.

| Battle condition | Weight | Effect |
|---|---|---|
| Skirmish | 100 | −90% Casualties taken +50% Morale loss +50% Morale damage |
| Ambush | 25 | −90% Casualties taken +25% Morale loss +150% Morale damage |
| In Disarray | 50 | −90% Casualties taken +75% Morale loss +25% Morale damage |

### Morale recovery

After a battle has ended, battalions gradually recover morale over time. It is possible for an army's forces to begin another battle without having recovered their morale entirely.

## Supply

Formations fighting overseas rely on the [supply network](https://vic3.paradoxwikis.com/Supply_network) to keep them equipped and in supply. If enemy fleets raid the supply network, sinking convoys, this impacts on the supply of formations, which has a direct impact on the morale recovery of units. For example, if raiding has reduced a supply network's efficiency by 2%, then the morale recovery of units overseas is 98%. If supply is reduced beyond 95%, it applies an equal penalty to organization. For example, a unit with 80% supply would have a 20% penalty to maximum organization.

Additionally, [shortages](https://vic3.paradoxwikis.com/Shortage) for units' buildings reduce a formations supply to the same result.

### Attrition

All mobilized formations are subject to attrition, which leads to both wounded and killed pops. The impact of this can be substantial and can outstrip the number of wounded and killed from battle. Formations receive **−50%** less attrition while stationed at their home HQ.

Base attrition is **10%** and casualties from attrition can range from **4%** to **12%** weekly.

Battalions actively engaged in a battle temporarily do not suffer attrition.

## Devastation

See also:
State devastation
The impact on Wales of French occupation is at this stage relatively mild, but if the French remain in control the situation will continue to deteriorate.
Armies battling in and occupying a [state](State.md) cause devastation. Devastation increases based on the size and number of the battles in the state and the unit types and orders used by the armies, and also due to enemy occupation. Devastation can also be caused by natural disasters, such as volcanic eruptions or tsunamis or other [events](https://vic3.paradoxwikis.com/Event) such as terrorism.

Devastation has an impact on [migration](Migration.md) attraction, infrastructure, construction efficiency and mortality. Once the situation that caused the devastation has resolved, it can take a substantial amount of time – particularly for high levels of devastation – before it no longer has an impact on the state.

## References

1. ↑ 1.00 1.01 1.02 1.03 1.04 1.05 1.06 1.07 1.08 1.09 1.10 1.11 1.12 Scaled by percentage of army composition
2. ↑ Due to a bug, this modifier is applied twice, effectively resulting in **+10** experience gain
3. ↑ 3.0 3.1 3.2 3.3 3.4 3.5 This is also affected by the increased consumption from any Supplies mobilisation options that are applied. Since Basic Supplies is mandatory the actual consumption of these goods is always at least 50% higher than shown.
4. ↑ See /Victoria 3/game/common/terrain/01_terrain.txt for multipliers
5. ↑ For script details, see /Victoria 3/game/common/script_values/command_values.txt
6. ↑ Bug? Should be occupation gain?

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

| Warfare | [Warfare](Warfare overview.md) • Land warfare • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
