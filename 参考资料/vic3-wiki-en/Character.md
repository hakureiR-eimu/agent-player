---
title: Character
source: https://vic3.paradoxwikis.com/Character
pageid: 3388
categories: [1.13, Game_concepts]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

**Characters** are prominent individuals within a [country](https://vic3.paradoxwikis.com/Country). Depending on their role, they affect countries in various ways. Each character has an [interest group](Interest group.md) affiliation, a [personal ideology](Character ideology.md), a popularity value, a culture (determining their name and appearance) and which countries can invite them, a religion, and a number of character traits. Throughout the game, characters age and die, and are replaced by new characters.

## Character roles

There are six roles characters serve in a country: *rulers*, *interest group leaders*, *commanders* (generals and admirals), *executives*, *agitators*, and *magnates*. Rulers, heirs, and interest group leaders are also collectively referred to as **politicians**. It is possible for some characters to occupy two roles (most often commanders combined with another role) or to switch roles (most often non-politicians joining politics).

### Ruler

A Ruler is a country's head of state. Whether a hereditary monarch, an elected president, or a dictator, a ruler's traits affect the country as a whole. The governance principles and distribution of power laws affect the amount of government Legitimacy gained from including the ruler's interest group in the government. The ruler's popularity also translates to a boost or penalty of Authority. In monarchies, the country also has an Heir – a character that becomes the new ruler once the current one dies. If there is no heir yet, there is a daily chance to generate one if the ruler is at least 20 years old (with an increasing chance after they turn 30). A male ruler of a monarchy or dictatorship can also serve as a general.

### Interest group leader

Every interest group has a Leader, who greatly affects how the interest group functions. The leader's traits and popularity affect the interest group's [pop](https://vic3.paradoxwikis.com/Pop) attraction and political power, and even its approval. Furthermore, the leader's [personal ideology](Character ideology.md) becomes part of the interest group's ideologies for as long as they remain the leader. Many causes, such as communism or feminism, can only achieve support this way. Once a leader dies, if an existing commander or executive supports the same interest group and has at least **0** popularity, then the character with the highest popularity among the interest group's supporters has a chance to become its next leader. If no existing character meets both of these criteria, then a new character is generated and becomes leader.

### Commander

Generals and Admirals command the country's armies and fleets, respectively. Their traits can give various bonuses and penalties to the units under their command. The interest group that a commander supports receives extra political power, which increases with the commander's rank (which also raises their command limit and Bureaucracy cost). If their interest group is part of a [revolution](https://vic3.paradoxwikis.com/Revolution), the commander supports the revolution instead of the government. When a commander dies, a new one has to be manually recruited. They can also be retired early, at the cost of their interest group's approval.

### Executive

Executives lead [companies](https://vic3.paradoxwikis.com/Company). An executive's popularity increases their company's prosperity target and their traits may affect the company's owned buildings.

Executives increase their interest group's political strength by **+2%** based on the number of owned building levels up to a maximum of **+20%**.

| Owned building levels (>=) | 10 | 50 | 100 | 250 | 500 | 1000 | 1500 | 2500 | 5000 | 10000 |
|---|---|---|---|---|---|---|---|---|---|---|
| Added political strength | **+2%** | **+4%** | **+6%** | **+8%** | **+10%** | **+12%** | **+14%** | **+16%** | **+18%** | **+20%** |

### Magnate

Magnates are wealthy characters using their fortune to influence politics. They are tied to a holding in their home state, either Manor Houses or Financial Districts. The revenue of that holding increases the magnate's prominence, using the formula 50 ∗ ∗ R e v e n u e G D P / 1250 {\displaystyle 50*{\frac {Revenue}{GDP/1250}}} ![{\displaystyle 50*{\frac {Revenue}{GDP/1250}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/37f58606e9a39e1fe5007cf84c1349a3e266fc2f), with a minimum of 10 and a maximum of 50.[1][2].

### Agitator

Main article:
Agitator
Agitators support [political movements](Political movement.md) that align with their ideological goals in a country.

Agitators add **15** plus **0.15** times their popularity, whether positive or negative, to their movement's pop attraction. Each pop scales 75% of this attraction based on its literacy and membership percentage in the agitator's interest group.

## Popularity

Each character has a popularity score between **−100** and **+100**, reflecting how the general public views them. Popularity mostly comes from traits, though commanders can also gain or lose popularity temporarily by winning or losing battles. A character's popularity has different effects depending on their role:

- Ruler: Popularity provides a direct authority bonus or penalty – e.g. **+50** popularity gives **+50** authority.
- Interest Group Leader: Popularity affects interest group pop attraction by **0.25%** per point of popularity[3] – e.g. **+100** popularity improves interest group pop attraction by **+25%**. It also affects their party's momentum during elections by **0.05%** per point of popularity.
- Agitator: Popularity affects movement attraction by **0.15%** per point of popularity – e.g. **+50** popularity gives a **7.5%** boost to movement support.
- Executive: Popular executives may become leaders for their interest group once the current leader is removed. Popularity affects company prosperity by **0.2** per point of popularity – e.g. **+50** popularity increases the prosperity target by **10**.
- Commander: Popular commanders may become leaders for their interest group once the current leader is removed. If they have at least 10 or 30 popularity, they can also gain the Popular or Celebrity Commander trait respectively. Commanders may gain temporary popularity by winning battles and lose popularity for losing them.

## Prominence

Each character has a prominence score between **0** and **+100**, reflecting how influential they are in the country's political machine. Prominence mostly comes from traits and specific roles, for example rulers of a country will always have **+100** prominence.

Each point of prominence over Significant (25) increases the character's interest group strength, up to **+25%** at max prominence.

## Lifespan

Characters live until the age of 75 on average[4].

Character health is a percentage between **0%** and **200%**, with a baseline of **100%**. It increases or decreases from various traits and modifiers and is the primary determiner of life expectancy.

Characters are considered adults at age 16 and old at age 60.

Besides dying of old age, characters can die due to events or a regular annual pulse.

The annual pulse has a 50% chance of triggering if there is an eligible interest group. The pulse attempts to kill a leader of a random interest group, but cannot kill a ruler, heir, or otherwise immune character. The pulse can also not target the same interest group within 10 years. The pulse also has a 20% chance of killing an agitator, though not more than once every 5 years. It also has a 20% chance of killing an executive, though not more than once every 7 years and never a historical executive.

## Interest group affiliation

Aside from interest group leaders, generated characters have a weighted chance of being affiliated with each interest group, modified by each interest group's clout. Namely, these are rulers and heirs in [hereditary governments](Government type.md), agitators, executives, magnates, and commanders. Historical characters are not affected by this weighting unless they have a variable interest group affiliation.

| Interest group | Ruler/ Heir | Agitator | Executive | Magnate | Commander |
|---|---|---|---|---|---|
| Common modifiers | Interest group is marginalized: ×0.1 Interest group is powerful: ×2 | Interest group is marginalized: ×0 | — | — |  |
| Armed Forces | Base: 1 Modifiers: Has any of: ×2 Autocracy Oligarchy Single-Party State Has any of: ×0.5 Census Suffrage Universal Suffrage Has none of: ×0.5 Professional Army Mass Conscription | Base: **0.5** | Base: **0.2** | Base: **1** | Base: **5** |
| Devout | Base: 1 Modifiers: Has State Religion: ×2 Does not have State Religion: ×0.25 Has State Atheism: ×0 State religion is any of: ×2 Sunni Shiite Theravada | Base: **0.5** | Base: **1** | Base: **1** | Base: **1** |
| Industrialists | Base: 1 Modifiers: Has any of: ×2 Oligarchy Wealth Voting Has Laissez-Faire: ×1.25 Does not have Mutual Funds: ×0.5 Does not have Currency Standards: ×0 | Base: **0.25** | Base: **5** | Base: **2** | Base: **0.5** |
| Intelligentsia | Base: 1 Modifiers: Has Technocracy: ×3 Has Appointed Bureaucrats: ×1.5 Does not have Empiricism: ×0 | Base: **0.75** | Base: **2** | Base: **1** | Base: **1** |
| Landowners | Base: 1.5 Modifiers: Has any of: ×2 Serfdom Slave Trade Legacy Slavery Has any of: ×2 Autocracy Oligarchy Landed Voting | Base: **0.25** | Base: **0.25** | Base: **2** | Base: **2** |
| Petite Bourgeoisie | Base: 1 Modifiers: Has Elected Bureaucrats: ×1.5 Has Ethnostate: ×2 | Base: **1** | Base: **1.5** | Base: **0.25** | Base: **1** |
| Rural Folk | Base: 0.25 Modifiers: Has Homesteading: ×2 Has Serfdom: ×0 | Base: **1** | Base: **0.1** | Base: **0.25** | Base: **1** |
| Trade Unions | Base: 0.1 Modifiers: Has Workers' Protections: ×2 Has No Workers' Rights: ×0 | Base: **1** | Base: **0.2** | Base: **0.1** | Base: **0.5** |

## Character interactions

Character interactions are various actions that change a character's role or otherwise affect a certain character. Valid interactions are visible on a character's detail screen or context menu. Some interactions have a cooldown which applies to the entire country, not per character.

| Interaction | Roles | Conditions | Effects |
|---|---|---|---|
| Grant Command |  | Ruler is adult, and not a General or Admiral Ruler is male or country has Women's Suffrage Government has hereditary or dictatorial transfer of power | Adds General role to ruler |
| Retire from Command |  | Ruler is a General Ruler is not Mobilized | Removes General role from ruler |
| Seek Royal Marriage |  | Country is a Christian Monarchy Character is an adult and not married Another monarchy with the same state religion: Has a ruler over age 36 Is not the junior in a personal union Has not used this interaction for any character within last 5 years | Adds **+20** relations with the country chosen for marriage |
| Exile Dissident |  | Country does not have Protected Speech or Guaranteed Liberties If Character is an Agitator, their political movement is not revolutionary, Otherwise, character's IG is not in government, marginalized, or revolutionary Character's ideology is not too similar to ruler's ideology Has not used this interaction for any character within last 5 years | Character becomes an Agitator and loses all other roles Adds 2% to 7% radicals for the character's IG Character is exiled If character was an interest group leader, Interest group gains Exiled Leader Exiled Leader Interest group modifier −5 Interest Group Approval (decaying) over 5 years If character's ideology is Moderate or Pacifist, adopt a random ideology not condoned by the current ruler. |
| Promote |  | Character is not at max rank | Increases character's commander rank |
| Split Formation |  | Formation contains more than one commander Formation contains more than one unit | Creates new formation with approximate ratio of units compared to command limit. |
| Retire Commander |  | Character's IG is not revolutionary Character is not busy Character has served for at least one year | Removes commander role from character Character's IG has a five-year decaying approval penalty equal to the character's commander rank, multiplied by their positive popularity as a percent |
| Invite Exile |  | Country has a free agitator slot Country does not have Closed Borders If character supports Devout or country has State Religion (no variant), Character's religion matches country's state religion Character has more than 15 popularity Character has at least open prejudice status Character must be able to join a political movement Has not used this interaction for any character within last 5 years | Character joins country Character joins or starts a political movement Character is immune to random death for 5 years Creates diplomatic catalyst with character's home country |
| Repatriate Agitator |  | Character has no other roles Country has a rivalry with the character's home country Character's home country exists and has a free agitator slot Character can join or start a political movement in their home country Has not used this interaction for any character within last 2.5 years | Character returns to home country |
| Arrange Accident |  | Country has Secret Police Character's IG is not marginalized Has not used this interaction for any character within last 5 years | 25% chance character dies 50% chance of nothing 25% chance: Adds 20% radicals to Character's IG If character or their IG support a political movement, The movement gains Failed Assassination Attempt Failed Assassination Attempt Political movement modifier +15% Political Movement Activism for 10 years |
| Imprison Agitator |  | Pivot of Empire is enabled Country does not have Guaranteed Liberties Has not used this interaction for any character within last 2.5 years | Character is imprisoned for 3, 5, or 10 years |
| Patronize |  | Pivot of Empire is enabled Character is not the Heir Character has not previously been Patronized or Ostracized Character's ideology is not too dissimilar from the ruler's Fewer than 3 other characters are currently Patronized | Character gains a modifier increasing their popularity and, if a politician, their interest group's approval, scaling with Authority spent 10% chance to gain trait Expensive Tastes |
| Ostracize |  | Pivot of Empire is enabled Character is not the Heir Character has not previously been Patronized or Ostracized Character's ideology is not too similar to the ruler's Fewer than 3 other characters are currently Ostracized | Character gains a modifier decreasing their popularity and, if a politician, their interest group's approval, scaling with Authority spent 10% chance to gain trait Wrathful |
| Grant Peerage |  | Pivot of Empire is enabled Country has Monarchy Character is not already a noble, the Ruler, or the Heir Character's ideology is not too dissimilar from the ruler's | Character becomes a noble If the character's interest group does not disapprove of Monarchy, it gains an approval bonus |
| Retire Daimyō |  | Country is Japan with Bakufu Character is a Daimyō Character's loyalty is not neutral or higher Has not used this interaction within a set cooldown | Character is retired A random state under the character's domain gains radicals |
| Voice of the People exclusive actions |  |  |  |
| Abdicate the Throne |  | Country has Monarchy Ruler can die of natural causes Has an heir Unless an interest group is revolutionary, Heir is age 18 or older Any of: Ruler's IG is marginalized Ruler's popularity is −50 or less Ruler is age 75 or older Ruler has trait Psychological Affliction Any political movement is revolutionary and the ruler or their IG opposes the movement's preferred law Has not used this interaction within last 30 years | Ruler abdicates (dies) |
| Resign from Office |  | Country does not have Monarchy or Theocracy Unless an interest group is revolutionary, Heir is age 18 or older Any of: Ruler's IG is angry or marginalized Ruler's popularity is −50 or less Ruler has any trait of: Psychological Affliction Cancer Senile Wounded Any political movement is revolutionary and the ruler or their IG opposes the movement's preferred law Has not used this interaction for any character within last 15 years | Ruler abdicates (dies) |
| Grant Leadership |  | Character's IG is in government Character supports a political movement that pressures its IG If country has State Atheism, Character is Atheist or in second-class citizen status or better Character has none of: Integralist Theocrat Traditionalist Minoritarian Traditionalist Otherwise, if country has Multiculturalism and Total Separation, Character has open prejudice status or better Otherwise, character has second-class citizen status or better Character is male or Women's Suffrage is enacted Has not used this interaction for any character within last 5 years | Character loses Agitator role and becomes the Leader of their IG |
| Grant Command |  | Character is not a commander Character is an adult and male Has not used this interaction for any character within last 5 years | Adds General role to the character |

## Character traits

Characters gain traits based on their current traits and their *expected trait value* or *character experience level*. Expected trait value increases by a base of 0.25% each week, which means it increases by 1 after 400 weeks or about 7.7 years. This rate is increased by 0.1% for the ruler, heir, and leaders of powerful interest groups as well as for generals on fronts, rulers also gain an additional. Admirals gain 0.05% more while escorting convoys and 0.1% more while raiding convoys. Exiled agitators gain only 0.1% weekly and commanders in the hiring pool gain only 0.05% weekly.[5] The regular maximum expected trait value is 12, but effects can add additional traits beyond that.

Newly generated characters typically start with an expected trait value of 4, with one personality and one skill trait; historical characters typically have an expected trait value equal to their defined starting traits. Personality traits except Child always have a trait value of 3, and skill traits that don't level up typically have a value of 2; skill traits that level up have a value of 1 per level. Condition traits don't have a trait value.

When a character's current total trait value is less than their expected trait value, they have a chance each week of gaining a new trait. The new trait's value is not considered, but characters cannot randomly gain more than two traits of each type.

### Personality traits

All characters have at least one personality trait. Children (under age 16) have the trait Child which is replaced by another personality trait when they reach age 16.

| Trait | Effects |  |  |  |  |  |
|---|---|---|---|---|---|---|
| All Roles | As Ruler | As IG Leader | As Agitator | As Executive | As Commander |  |
| Child | −25 Popularity −25 Prominence | −15% Authority −5% Prestige | **−25%** IG Pop Attraction | — | — | — |
| Direct | **+15** Popularity | **+25%** Political Strength of Officers | −5% IG Political Strength +10% IG Pop Attraction | — | — | +10% Offense +5% Hull Attack Damage +5% Crew Attack Damage +5% Vulnerability +100% Aggressive Maneuver Chance |
| Persistent | **+20%** Character Health | **+25%** Political Strength of Bureaucrats | **−1** Opposition IG Approval | — | — | −15% Morale Loss +10% Screening |
| Cautious | +30% Character Health −5 Prominence | −100 Influence −20% Infamy Generation | −2% IG Political Strength +1 IG Approval | — | **−10%** Dangerous Working Conditions | −5% Morale loss +10% Screening +10 Accuracy -10% Critical Chance |
| Arrogant | −25 Popularity +5 Prominence | **−5** Legitimacy | +5% IG Political Strength −10% IG Pop Attraction | — | — | +25% Command Limit +10% Vulnerability |
| Bigoted | **−35** Popularity | +100 Authority −100 Influence +10% Radicalism increases for discriminated Open Prejudice, Cultural Erasure, and Violent Hostility statuses | −5% IG Pop Attraction +1 Government IG Approval | — | — | +5% Offense +5% Morale Loss |
| Reckless | +10 Popularity −20% Character Health | +20 Maneuvers per Diplomatic Play +20% Infamy Generation | **−2** Opposition IG Approval | — | — | −10% Recovery Rate −10% Coup Strength +20% Vulnerability +10% Critical Chance |
| Tactful | — | +20% Improve Relations Speed | +1 IG Approval +2% IG Pop Attraction | **−10%** Movement activism | — | +5 Defense −5% Morale Damage +100% Careful Maneuver Chance |
| Ambitious | **+10** Prominence | −25% Decree Cost +10% Navy Power Projection prestige +10% Army Power Projection prestige | **+10%** IG Political Strength | **+10%** Movement activism | **+5%** Building Throughput | +5% Offense −5% Recovery Rate +10% Critical Chance +20% Critical Damage +5% Coup Strength |
| Imperious | −35 Popularity +10 Prominence | −20% Decree Cost −20% Radicals from Political Movements +10% Loyalists from Political Movements | **+25%** IG Pop Attraction | — | — | −15% Morale Loss −15% Morale Recovery +100% Aggressive Maneuver Chance +5% Coup Strength |
| Wrathful | **−5%** Character Health | **+100** Authority | **−2** Opposition IG Approval | **+20%** Movement activism | — | +10% Morale Damage 5% Morale Loss +5% Hull Attack Damage +10% Crew Attack Damage +10% Vulnerability |
| Reserved | +5% Character Health −25 Popularity | — | — | — | — | −10% Morale Loss −10% Critical Chance +100% Careful Maneuver Chance [6] |
| Cruel | **−50** Popularity | −1 Standard of Living −1 Opposition IG Approval +10% Authority −25% Consumption Tax Cost | **+1** Government IG Approval | — | +5% Heavy Industry, Military Industry, Plantations, Mining, and Agriculture throughput +10% Heavy Industry, Military Industry, Plantations, Mining, and Agriculture mortality | **+10%** Kill Rate |
| Meticulous | **+5** Prominence | +5% Bureaucracy +25% Institution Size Change Speed | +5% IG Political Strength +5% IG Pop Attraction | — | **+5%** Building Throughput | +5% Offense +5% Defense +10% Recovery Rate +20 Accuracy +10% Critical Chance +50% Surprise Maneuver Chance +100% Careful Maneuver Chance |
| Charismatic | **+50** Popularity | **+5%** Influence | **+20%** IG Pop Attraction | — | — | **+10%** Morale Recovery |
| Romantic | — | **+25%** Political Strength of Aristocrats | — | — | **+5%** Arts Buildings throughput | −10% Offense −10% Morale Loss +10% Vulnerability +5% Hull Attack Damage |
| Brave | −5% Character Health +25 Popularity | +5% Navy Power Projection prestige +5% Army Power Projection prestige | — | — | — | −10% Morale Loss +25% Vulnerability +15% Critical Chance |
| Innovative | — | **+10%** Technology Spread | — | — | +5% Heavy Industry, Military Industry, Plantations, Mining, and Agriculture throughput | −15% Morale Loss +100% Surprise Maneuver Chance +10% Critical Chance +20% Critical Damage |
| Hedonist | **−15** Popularity | **−10%** Political Strength of Clergymen | **+1** Government IG Approval | — | — | +5% Morale Recovery +10% Supply Consumption −10% Supply Efficiency |
| Pious | — | **+10%** Political Strength of Clergymen | — | — | — | −25% Morale Loss +25% Morale Recovery −10% Kill Rate |
| Imposing | +100% Aggressive Maneuver Chance [6] +5 Prominence | **−25%** Infamy Decay | +1 Government IG Approval −1 Opposition IG Approval | — | — | **−10%** Morale Loss |
| Honorable | **+25** Popularity | **−2.5%** Piracy Income | **+50%** Government IG Attraction | — | −5% Heavy Industry, Military Industry, Mining, Plantations, and Agriculture throughput −10% Heavy Industry, Military Industry, Mining, Plantations, and Agriculture mortality | — |
| Ruthless | −15 Popularity +5 Prominence | +5% Authority +5% Piracy Income | **+15%** IG Political Strength | **+10%** Movement activism | +5% Heavy Industry, Military Industry, Mining, Plantations, and Agriculture throughput +10% Heavy Industry, Military Industry, Mining, Plantations, and Agriculture mortality | — |
| Compliant | **−5** Prominence | **−10%** Authority | −10% IG Political Strength +2 Government IG Approval | — | — | **−10%** Coup Strength |
| Aesthete | **+25** Popularity | +10% Influence +10% Political Strength of Academics | — | **+5%** Movement pop attraction | **+10%** Arts Buildings throughput | — |

### Conditions

Conditions can be acquired over the course of the game and are overall negative effects. Sometimes they may be lost via events. Most conditions cannot be gained until the character reaches age 26.

| Trait | Effects | Notes |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| All Roles | As Ruler | As IG Leader | As Agitator | As Executive | As Commander |  |  |
| Alcoholic | −10 Popularity −10% Character Health | **+2%** Influence | — | — | — | **−10%** Morale Damage |  |
| Opium Addict | −25 Popularity −10% Character Health | **+5%** Opium Plantations Throughput | — | — | — | — |  |
| Cocaine Addict | +20 Popularity −10% Character Health | — | — | — | — | — | Requires Pharmaceuticals |
| Cancer | **−80%** Character Health | — | — | — | — | — |  |
| Tuberculosis | **−60%** Character Health | — | — | — | — | — |  |
| Grifter | **−25** Popularity | +1% Tax Waste +5% Piracy Income | — | — | **−10%** Maximum Cash Reserves | +5% Supply Consumption -5% Supply Efficiency +50% Pirating Capacity |  |
| Scarred | +10 Popularity −10% Character Health | — | — | — | — | — | Replaces Wounded |
| Senile | −50 Popularity −25% Character Health | **−5%** Influence | — | — | — | +10% Morale Loss −25% Command Limit |  |
| Syphilis | **−50%** Character Health | **−10%** Influence | — | — | — | — |  |
| Shell Shock | −30 Popularity −20% Character Health | — | — | — | — | −20% Offense −20% Defense +20% Morale Loss | Is a commander |
| Wounded | **−40%** Character Health | — | — | — | — | **+10%** Morale Loss | May progress to Scarred |
| Psychological Affliction | −50 Popularity −20% Character Health | — | — | — | — | — |  |
| Expensive Tastes | **+25** Popularity | +5% Prestige +5% Tax Waste | — | — | **−10%** Maximum Cash Reserves | — |  |
| Kidney Stones | **−30%** Character Health | — | — | — | — | −10% Offense −10% Defense |  |
| Beetle Eared | **−30%** Character Health | — | — | — | — | — | Can only be acquired by events |
| War Criminal | **−50** Popularity | — | — | — | — | **+10%** Kill rate | Can only be acquired by events |
| Sickly | **−20%** Character Health | — | **−10%** IG Pop Attraction | — | — | — |  |

### Skill traits

Skill traits can appear and level up over the course of the game and are overall positive effects. Characters tend to acquire skill traits befitting their role.

| Trait | Role | Effects | Notes |  |
|---|---|---|---|---|
| Supply Requisitions Expert | General | −10% Supply Consumption +100% Logistics Secured Chance −90% Broken Supply Line Chance |  |  |
| Pillager | General | +25% Devastation +800% Ambush Chance −10 Popularity |  |  |
| Surveyor | General | +10% Home Offense +10% Home Defense +400% Ambush Chance +200% Charted Terrain Chance +100% Good Visibility Chance |  |  |
| Woodland Combat Expert | General | +400% Ambush Chance +25% Defense in Forested Terrain |  |  |
| Open Terrain Commander | General | **+25%** Offense in Flat Terrain |  |  |
| Mountain Combat Expert | General | +400% Ambush Chance +25% Defense in Elevated Terrain |  |  |
| Artillery Commander | General | +5% Artillery Offense +50% Mud Chance +100% Aggressive Maneuver Chance +5 Popularity | Requires Artillery Replaces Inexperienced |  |
| Experienced Artillery Commander | +10% Artillery Offense +50% Mud Chance +200% Aggressive Maneuver Chance +10 Popularity | Upgrades Artillery Commander |  |  |
| Expert Artillery Commander | +15% Artillery Offense +50% Mud Chance +300% Aggressive Maneuver Chance +20 Popularity | Upgrades Experienced Artillery Commander |  |  |
| Stalwart Defender | General | +10% Defense +5 Popularity | Requires Field Works |  |
| Trench Rat | +10 Defense +100% Surprise Maneuver Chance +100% Careful Maneuver Chance | Upgrades Stalwart Defender Requires Trench Works |  |  |
| Defense in Depth Specialist | +20 Defense +250% Surprise Maneuver Chance +250% Careful Maneuver Chance | Upgrades Trench Rat Requires Defense in Depth |  |  |
| Offensive Planner | General | +5% Offense +5 Popularity | Requires Napoleonic Warfare Replaces Inexperienced |  |
| Experienced Offensive Planner | +10% Offense +50% Surprise Maneuver Chance +10 Popularity | Upgrades Offensive Planner |  |  |
| Expert Offensive Planner | +20% Offense +150% Surprise Maneuver Chance +20 Popularity | Upgrades Experienced Offensive Planner |  |  |
| Defensive Strategist | General | +10% Defense +100% Dug In Chance +100% Camouflaged Chance +5 Popularity | Requires Military Drill Replaces Inexperienced |  |
| Experienced Defensive Strategist | +20% Defense +200% Dug In Chance +200% Camouflaged Chance +10 Popularity | Upgrades Defensive Strategist |  |  |
| Expert Defensive Strategist | +30% Defense +300% Dug In Chance +300% Camouflaged Chance +20 Popularity | Upgrades Experienced Defensive Strategist |  |  |
| Naval Commander | Admiral | +5% Hull Attack Damage −5% Vulnerability +5 Popularity | Requires Admiralty Replaces Inexperienced |  |
| Experienced Naval Commander | +10% Hull Attack Damage −10% Vulnerability +10 Popularity | Upgrades Naval Commander |  |  |
| Expert Naval Commander | +10% Hull Attack Damage +10% Screening −10% Vulnerability +10% Blockade Strength +20 Popularity | Upgrades Experienced Naval Commander |  |  |
| Convoy Raider | Admiral | −10% Visibility +5% Submarines Hull Attack Damage +5 Popularity | Requires Admiralty |  |
| Experienced Convoy Raider | +10% Detection −10% Visibility +5% Submarines Hull Attack Damage +10 Popularity | Upgrades Convoy Raider |  |  |
| Expert Convoy Raider | +5% Ship Speed +10% Detection −10% Visibility +10% Submarines Hull Attack Damage +20 Popularity | Upgrades Experienced Convoy Raider |  |  |
| Dockyard Organizer | Admiral | **+20%** Supply Efficiency |  |  |

| Trait | Role | Effects | Notes |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| All Roles | As Ruler | As IG Leader | As Agitator | As Executive | As Commander |  |  |  |
| Traditionalist Commander | Any | — | **+5%** Prestige | — | — | — | +10% Command Limit +20% Blockade Strength −20% Carriers Hull Attack Damage | Character's IG is one of: Devout Landowners Armed Forces Powerful |
| Popular Commander | — | **+10%** Prestige | **+2%** IG Political Strength | **+5%** Movement pop attraction | — | **+20%** Command Limit | Popularity above 10 OR Upgrades Traditionalist Commander and popularity above 0 |  |
| Celebrity Commander | **+30** Popularity | **+15%** Prestige | **+5%** IG Political Strength | **+10%** Movement pop attraction | — | **+30%** Command Limit | Upgrades Popular Commander Popularity above 30 |  |
| Diplomat | Any | **+10** Popularity | **+5%** Influence | — | — | — | **+25%** Morale Recovery | Replaces Inexperienced |
| Experienced Diplomat | **+25** Popularity | **+10%** Influence | **+50%** Morale Recovery | Upgrades Diplomat |  |  |  |  |
| Masterful Diplomat | **+50** Popularity | **+20%** Influence | **+100%** Morale Recovery | Upgrades Experienced Diplomat |  |  |  |  |
| Colonial Administrator | Ruler | — | **+10%** Colony Growth Speed | — | — | — | — | Requires an active colony Replaces Inexperienced |
| Experienced Colonial Administrator | **+20%** Colony Growth Speed | Upgrades Colonial Administrator |  |  |  |  |  |  |
| Expert Colonial Administrator | **+40%** Colony Growth Speed | Upgrades Experienced Colonial Administrator |  |  |  |  |  |  |
| Political Operator | Politician | **+5** Prominence | **+5%** Authority | **+5%** IG Political Strength | **+5%** Movement pop attraction | — | **+5%** Coup Strength | Replaces Inexperienced |
| Experienced Political Operator | **+10** Prominence | **+10%** Authority | **+10%** IG Political Strength | **+10%** Movement pop attraction | **+10%** Coup Strength | Upgrades Political Operator |  |  |
| Expert Political Operator | **+15** Prominence | **+20%** Authority | **+20%** IG Political Strength | **+15%** Movement pop attraction | **+15%** Coup Strength | Upgrades Experienced Political Operator |  |  |
| Inspirational Orator | Any | **+25** Popularity | — | +5% IG Political Strength +10% IG Pop Attraction | — | — | — |  |
| Demagogue | Any | **+35** Popularity | — | +10% IG Political Strength +15% IG Pop Attraction | — | — | — |  |
| Firebrand | Any | **+50** Popularity | — | +15% IG Political Strength +25% IG Pop Attraction | — | — | — |  |
| Explorer | Commander Ruler Heir | **+20** Popularity | +10 Prestige +50% Expedition Opportunity | — | — | — | **+200%** Expedition Opportunity |  |
| Bandit | Any | **−25** Popularity | −5% Prestige +100 Authority −50% Infamy Decay | +2 Government IG Approval −2 Opposition IG Approval | **+15** Movement activism | — | +10% Morale Damage +50% Pirating Capacity | Is either: Agitator Affiliated with Rural Folk or Trade Unions |
| Social Bandit | Any | **+25** Popularity | −5% Prestige +100 Authority −50% Infamy Decay +2.5% Piracy Income | +2 Government IG Approval −2 Opposition IG Approval | **+15** Movement activism | — | +10% Morale Damage +25% Pirating Capacity | Is either: Agitator Affiliated with Rural Folk or Trade Unions |
| Erudite | Any | — | +20% Political Strength of Academics +10% Political Strength of Bureaucrats | **−10%** IG Pop Attraction | — | — | −10% Command Limit | No trait value |
| Literary | Politician Agitator Executive | +10 Popularity +10 Prominence | +5% Prestige +25% Infamy Decay | **+10%** IG Pop Attraction | — | **+10%** Arts Buildings throughput | — | Replaces Inexperienced |
| Engineer | Any | — | +5 Construction +20% Political Strength of Engineers +10% Political Strength of Machinists | — | — | +10% Heavy Industry throughput +10% Military Industry throughput | +5% Ship Armor +100% Dug In Chance +100% Logistics Secured Chance | Trait value 3 |
| Master Bureaucrat | Any | — | +10% Bureaucracy +10% Political Strength of Bureaucrats | −5% IG Pop Attraction +5% IG Political Strength | — | **+5%** Building throughput | — | Replaces Inexperienced No trait value |
| Political Appointee | Any | **−10** Popularity | −5 Legitimacy −10% Government IG Pop Attraction | −5% IG Political Strength | — | — | **−25%** Coup Strength | Only gained by effect No trait value |
| Inept | Any | **−15** Popularity | −5 Legitimacy | −10% IG Political Strength | −10% Movement pop attraction | **−5%** Building throughput | −25% Morale recovery −10% Offense −10% Defense −10% Hull Attack Damage −10% Crew Attack Damage +10% Vulnerability −10% Coup Strength | No trait value |
| Inexperienced | Any | **+10** Popularity | **−5** Legitimacy | **−5%** IG Political Strength | **−5%** Movement pop attraction | — | −10% Morale recovery −5% Offense −5% Defense −5% Hull Attack Damage −5% Crew Attack Damage +5% Vulnerability | Is replaceable by several skill traits No trait value |
| Elder | Agitator Politician General | **+25** Popularity | +15% Political Strength of Peasants +10% Political Strength of Farmers −5% Prestige +100 Authority −50% Infamy Decay [7] | +2 Government IG Approval −2 Opposition IG Approval | **+10%** Movement pop attraction | — | −10% Supply Consumption +10% Home Offense +10% Home Defense | Trait value 1 Is neither the ruler nor the heir Country is decentralized or unrecognized If general and neither an agitator nor a politician, country must be an Unrecognized Power One of the following must be true: Affiliated with Rural Folk Affiliated with Landowners and country is an Unrecognized Power Affiliated with the Devout and culture's heritage is in the Indigenous American group |
| Basic Entrepreneur | Any | **+10** Popularity | — | **+2%** IG Political Strength | — | **+5%** Building throughput | — | Replaces Inexperienced |
| Experienced Entrepreneur | **+15** Popularity | +5% Company throughput +5% Influence | **+10%** IG Political Strength | **+7.5%** Building throughput | Upgrades Basic Entrepreneur |  |  |  |
| Expert Entrepreneur | **+25** Popularity | +10% Influence +1 Free Company Charters +10% Company throughput +10% Company construction bonus | **+15%** IG Political Strength | +10% Building throughput +10 Economy of Scale Building Level Cap | Upgrades Experienced Entrepreneur |  |  |  |

### Unique traits

Certain characters have or can gain unique traits.

| Trait | Effects | Notes |  |  |  |  |
|---|---|---|---|---|---|---|
| All Roles | As Ruler | As IG Leader | As Agitator | As Commander |  |  |
| President Pedro | **+30** Popularity | **+15** Legitimacy |  |  |  | Pedro de Bragança gains this on becoming president of [Brazil](Brazil.md) |
| Napoleon of the Americas | **+60** Popularity | **+10** Legitimacy from head of state |  |  | +10% Unit defense +5% Unit offense | Francisco Solano López |
| El Excelentísimo | **+40** Popularity | **+10** Legitimacy from head of state | **+20%** Armed Forces political strength |  |  | Carlos Antonio López |
| Tsar-Liberator | **+50** Popularity | **+10%** Loyalists from legitimacy |  |  |  | Option for Aleksandr (II) Romanov on completing the *Great Reformer* |
| German Unifier | **+50** Popularity | **+15%** Authority |  |  |  | Option for ruler of country that forms [Germany](Germany.md) |
| Restitutor Orbis | **+50** Popularity | **+10** Legitimacy |  |  |  | Option for ruler of [France](France.md) on completing the *Cement the House of [Dynasty]* |
| The Man from the River Lena | **+25** Popularity |  | **+15%** Interest group pop attraction |  |  | Vladimir Lenin |
| This Glorious Endeavor | **+20** Popularity |  | **+20%** IG Political Strength |  |  | John Brown |
| Professional Revolutionary | +25 Popularity +10% Coup Strength −10 Loyalty |  | **+10%** IG Political Strength |  |  | Louis Blanqui |
| Reactionary Icon | **+25** Popularity |  | **+20%** IG Political Strength |  |  | Charles Maurras |
| Napoleonic Return | +35 Popularity +10% Coup Strength |  | **+15%** IG Political Strength |  |  | Louis-Napoleon Bonaparte |
| Popular Radical | **+50** Popularity |  | **+10%** Interest group pop attraction |  |  | Giuseppe Mazzini |
| The Spirit of San Francisco | **+15** Popularity |  | **+20%** IG Political Strength |  |  | Joshua Norton |
| Nightingale Pledge | **+50** Popularity |  |  |  |  | Florence Nightingale |
| Général Revanche | **+50** Popularity |  | **+20%** IG Political Strength |  |  | Georges Boulanger |
| Passionate Theorist | **+40** Popularity |  |  |  |  | Georges Sorel |
| Agent of the Sovereign | **+10** Popularity |  |  |  |  | Ferdinand Lassalle |
| The Curly-Haired Orpheuse | **+25** Popularity |  |  | **+20%** Political movement pop attraction |  | Luís Gama |
| Untamed Revolutionary | +40 Popularity +25 Health |  |  | **+10%** Political movement activism |  | Rosa Luxemburg |
| Emperor of Japan | — | **+5** Legitimacy |  |  |  | Emperor of [Japan](Japan.md) following the Meiji Restoration |

### Colonial Administrator traits

These traits are only available to appointed heads of colonies.

| Trait | Effects | Notes |  |  |
|---|---|---|---|---|
| All Roles | As Ruler | As IG Leader | As Commander |  |
| Influential Planter |  | +10% Plantations and Ranching throughput +10% Colony Growth Speed | +5% IG Political Strength +10% IG Pop Attraction |  |
| Local Appointee | **+30** Popularity | −10% Radicals from political movements +10% Loyalists from political movements −0.05 Liberty Desire | +5% IG Political Strength +10% IG Pop Attraction |  |
| Experienced Extractor |  | +15% Extraction throughput +10% Colony Growth Speed +1% Mortality | +5% IG Political Strength +10% IG Pop Attraction |  |
| Prominent Businessman |  | +10% Supply ships construction efficiency +5% State construction efficiency −10% Loan interest | +5% IG Political Strength +10% IG Pop Attraction |  |
| Military Governor |  | Suppression impact on movement attraction −10% +10% Conscriptable Battalions +10% Authority | +5% IG Political Strength +10% IG Pop Attraction | **+20%** Command Limit |

## References

1. ↑ /Victoria 3/game/common/defines/00_defines.txt`HOLDING_REVENUE_SCALING_GDP_DIVISOR`
2. ↑ /Victoria 3/game/common/static_modifiers/00_code_static_modifiers.txt`holding_revenue_magnate_scale`
3. ↑ pop attraction effect = ( 0.0025 ∗ ∗ popularity ) {\displaystyle {\text{pop attraction effect}}=(0.0025*{\text{popularity}})} ![{\displaystyle {\text{pop attraction effect}}=(0.0025*{\text{popularity}})}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/9148fcfb12ae1085b1f0b8dc6102d7205068e2aa)
4. ↑ /Victoria 3/game/common/defines/00_defines.txt `NCharacters.CHARACTER_LIFE_EXPECTANCY_BASE_YEARS`
5. ↑ See [The Hidden Experience System For Generals](https://www.youtube.com/watch?v=whUTN4dFJRI) and /Victoria 3/game/common/defines/00_defines.txt `NCharacters` for details
6. ↑ 6.0 6.1 Appears under `character_modifier` instead of `command_modifier` in the entry in /Victoria 3/game/common/character_traits/personality_traits.txt. Unsure if this has any affect.
7. ↑ Only the first two modifiers seem to be intended to actually apply. However, Social Bandit modifiers are mistakenly copied under those.

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | [Government](Government.md) • [Capacities](Capacity.md) • Characters • [Decrees](Decrees.md) • [Institutions](Institutions.md) • [Laws](Laws.md) • [Technology](Technology.md) |
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
