---
title: Defines
source: https://vic3.paradoxwikis.com/Defines
pageid: 3688
categories: [1.13, Modding]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

**Defines** are variables used by the engine. They regulate basic game behaviors and settings that are not opened to scripting (IG approval thresholds, camera field-of-view, etc.).

Defines are static and global: they apply to the whole game and cannot be changed dynamically.

Vanilla values are configured in the folder /Victoria 3/game/common/defines, primarily in `00_defines.txt`.

Each of the lists on this represents a section of the defines; in the defines files, these sections are all prefixed with `N`, for example `NCountry`.

## Define modding

Defines can be modified individually or in batches without overwriting an entire defines file. This better preserves compatibility and makes it easier to keep up with changes in future patches.

To modify a define, create a new file in <mod>/common/defines/ that loads after the base game files such as `01_mod_defines.txt`. In that file, add a block for each set of defines to be modified and include the modified defines in those blocks, for example

```
NCountry = {
	INCORPORATION_TIME_NO_MATCH = 100	# Base game 20 years; Years if the state's Homeland cultures have nothing in common with the country's primary cultures
}

NDiplomacy = {
	COUNTRY_TIER_HEGEMONY_PRESTIGE = 150	# Base game 50
}
```

In the case of multiple mods modifying the same define, the mod with the last loaded filename determines the final value of the define.

## 00_defines

### Game

| Define | Default Value | Dev Comment |
|---|---|---|
| START_DATE | "1836.1.1" |  |
| END_DATE | "1936.1.1" |  |
| SAVE_VERSION | 0 |  |
| MP_LAG_TICKS_BOUNDS | 28 | # Host will advance up to a week ahead of players ( 7 * 4 ) |
| DEAD_OBJ_UNDESTROYED_DAYS | 22 | # number of days "killed"/removed objects will persist in memory before ultimately destroyed as they are referenced by events etc |
| MAX_NUMBER_OF_AUTOSAVES | 5 | # The game will only keep the MAX_NUMBER_OF_AUTOSAVES latest autosaves. |

### JominiMap

| Define | Default Value | Dev Comment |
|---|---|---|
| WORLD_EXTENTS_X | 8192 |  |
| WORLD_EXTENTS_Y | 24 | #This determines the max height of the world. Original settings = 25.5 |
| WORLD_EXTENTS_Z | 3615 |  |
| WATERLEVEL | 1.74 | #Original Settings 3.7 |

### Country

| Define | Default Value | Dev Comment |
|---|---|---|
| DEFAULT_COUNTRY_TYPE | "recognized" |  |
| COMPANY_COUNTRY_TYPE | "company" |  |
| COMPANY_FALLBACK_COUNTRY_TYPE | "colonial" |  |
| DEFAULT_MAX_NUM_COUNTRY_FORMATION_CANDIDATES | 3 | # If nothing is specified in the country formation, this is used |
| COUNTRY_FORMATION_CANDIDATE_MIN_RANK | 6 | # countries with a lower rank value than this cannot be formation candidates |
| MOVE_CAPITAL_COOLDOWN_YEARS | 5 |  |
| MOVE_MARKET_CAPITAL_COOLDOWN_YEARS | 5 |  |
| MAX_POWER_EFFECT | 1.0 | # The max by which a power excess/deficiency modifier can scale |
| GREAT_POWER_RANK_KEY | "great_power" |  |
| MAJOR_POWER_RANK_KEY | "major_power" |  |
| MINOR_POWER_RANK_KEY | "minor_power" |  |
| SPLIT_STATE_DOMINANT_LAND_SHARE_THRESHOLD | 0.5 | # States with more land share than this can use the region's name |
| SPLIT_STATE_PRIME_LAND_WEIGHT | 5.0 |  |
| CAPITAL_CULTURE_CORE_WEIGHT | 10 |  |
| CAPITAL_NON_INCORPORATED_WEIGHT | 0.001 |  |
| DEFAULT_SUBSISTENCE_BUILDING | "building_subsistence_farm" |  |
| CONSTRUCTION_CAMP_BUILDING | "building_construction_sector" |  |
| BARRACKS_BUILDING | "building_barrack" |  |
| NAVAL_ADMINISTRATION_BUILDING | "building_naval_administration" |  |
| NAVAL_FORTIFICATION_BUILDING | "building_naval_fortification" |  |
| PORT_BUILDING | "building_port" |  |
| URBAN_CENTER_BUILDING | "building_urban_center" |  |
| CONSCRIPTION_CENTER_BUILDING | "building_conscription_center" |  |
| NAVAL_LOGISTICS_CENTER_BUILDING | "building_naval_logistics_center" |  |
| LAND_LOGISTICS_CENTER_BUILDING | "building_land_logistics_center" |  |
| CONSCRIPTION_CENTER_LEVEL_POPULATION_DIVISOR | 1000 | # Civilian population is divded by this amount to calculate maximum conscription center level [>=1] |
| TRADE_CENTER_BUILDING | "building_trade_center" |  |
| MANOR_HOUSE_BUILDING | "building_manor_house" |  |
| FINANCIAL_DISTRICT_BUILDING | "building_financial_district" |  |
| RAILWAY_BUILDING | "building_railway" |  |
| POWER_BLOC_STATUE_BUILDING | "building_power_bloc_statue" |  |
| COMPANY_HEADQUARTER_BUILDING | "building_company_headquarter" |  |
| COMPANY_REGIONAL_HEADQUARTER_BUILDING | "building_company_regional_headquarter" |  |
| CONSTRUCTION_QUEUE_INCREMENT_SHIFT | 5 | # Increment/Decrement used for buildings construction queue when holding down Shift |
| CONSTRUCTION_QUEUE_INCREMENT_CONTROL | 10 | # Increment/Decrement used for buildings construction queue when holding down Ctrl |
| WEEKS_TO_STORE_LOYALIST_RADICAL_STATISTICS | 52 | # Number of weeks of statistics for loyalists/radicals that is stored and shown |
| INCORPORATION_TIME_SAME_CULTURE | 2 | # Years if the state is a Homeland of one of the country's primary cultures |
| INCORPORATION_TIME_SAME_HERITAGE_AND_LANGUAGE | 5 | # Years if the state is a Homeland of a culture that matches of one of the country's primary cultures' Heritage and Language traits |
| INCORPORATION_TIME_SAME_HERITAGE_OR_LANGUAGE | 10 | # Years if the state is a Homeland of a culture that matches of one of the country's primary cultures' Heritage traits |
| INCORPORATION_TIME_SAME_TRAIT_GROUP | 15 | # Years if the state is a Homeland of a culture with any trait in common with a country's primary cultures |
| INCORPORATION_TIME_NO_MATCH | 25 | # Years if the state's Homeland cultures have nothing in common with the country's primary cultures |
| INCORPORATION_TIME_MIN_MULTIPLIER | 0.1 | # Incorporation speed cannot be reduced below this by modifiers |
| JOURNAL_ENTRY_UPDATE_ACTIVE | 4 | # Number of ticks between each update of Active (Possible) Journal Entries, can be overriden on journal entry type |
| JOURNAL_ENTRY_UPDATE_INACTIVE | 14 | # Number of ticks between each update of Inactive Journal Entries, can be overriden on journal entry type |
| MAX_TRADITION_TRAITS_PER_CULTURE | 4 | # How many tradition traits a culture is allowed to have at most |

### Politics

| Define | Default Value | Dev Comment |
|---|---|---|
| GOVERNANCE_PRINCIPLES_GROUP | "lawgroup_governance_principles" | # Law from this group is used for the power_bloc_worst_progressiveness_difference_government_type trigger to represent the Governance Principle |
| DISTRIBUTION_OF_POWER_GROUP | "lawgroup_distribution_of_power" | # Law from this group is used for the power_bloc_worst_progressiveness_difference_government_type trigger to represent the Distribution of Power |
| TARIFF_LAW_GROUP | "lawgroup_trade_policy" | # Law from this group is shown to player as their tariff law |
| TAX_LAW_GROUP | "lawgroup_taxation" | # Law from this group is shown to player as their tax law |
| NUM_TIMES_TO_LOOP_THROUGH_LAWS | 3 | # When creating a law set, how many times do we loop through all law groups? This is done more than once in order to allow laws that are unlocked by other laws to be changed |
| DEFAULT_IDEOLOGY | "ideology_moderate" | # Used as a fallback if an ideology cannot be selected for a character |
| CHILD_IDEOLOGY | "ideology_child" | # Children use this ideology, which is swapped out once they turn 16 |
| MIN_POP_NUMBER_JOIN_OR_LEAVE_IG | 10 | # Min for maximum amount of pops/support that will change IG in a single update (overrides below max fraction) |
| MAX_POP_FRACTION_JOIN_OR_LEAVE_IG | 0.05 | # Maximum amount of a pop that can change IGs in a single update (for each IG) |
| MIN_POP_NUMBER_JOIN_OR_LEAVE_MOVEMENT | 10 | # Min for maximum amount of pops/support that will change political movements in a single update (overrides below max fraction) |
| MAX_POP_FRACTION_JOIN_OR_LEAVE_MOVEMENT | 0.1 | # Maximum amount of a pop that can change political movements in a single update (for each movement) |
| MOVEMENT_POP_SUPPORT_ATTRACTION_CAP | 0.01 | # The fraction of individuals in a pop that will support a movement is capped at ( movement attraction * this ) so that movements with low attraction but no competition won't attract every single pop in the country |
| # For a movement with a cultural/religious identity to spawn, the culture/religion must meet at least one of the two thresholds below: |  |  |
| MOVEMENT_IDENTITY_MIN_INDIVIDUALS_ABSOLUTE_THRESHOLD | 200000 | # Absolute number of individuals |
| MOVEMENT_IDENTITY_MIN_INDIVIDUALS_RELATIVE_THRESHOLD | 0.2 | # Number of individuals relative to country population |
| MOVEMENT_DEFAULT_MIN_SUPPORT_TO_CREATE | 0.025 | # Default support (as calculated value) required to create a political movement, can be overriden in database |
| MOVEMENT_DEFAULT_MIN_SUPPORT_TO_MAINTAIN | 0.01 | # Default support (as actual value) required to maintain a political movement, can be overriden in database |
| MOVEMENT_FAILED_MOVEMENT_DURATION_DAYS | 365 | # For how long do we remember that a political movement failed to be created and do not try again for that exact same movement |
| MOVEMENT_MIN_SUPPORT_GRACE_MONTHS | 12 | # A political movement cannot disband due to low support for this many months after its creation |
| MOVEMENT_AGITATOR_STICKYNESS | 2.0 | # Agitators apply this multiplier to the score for a movement they are already backing when considering whether to switch movements |
| # The three defines below should add up to 1.0 |  |  |
| MOVEMENT_SUPPORT_POPULAR_SUPPORT_FRACTION | 0.34 | # This fraction a political movement's total support comes from its popular support |
| MOVEMENT_SUPPORT_MILITARY_SUPPORT_FRACTION | 0.33 | # This fraction a political movement's total support comes from its military support |
| MOVEMENT_SUPPORT_WEALTH_SUPPORT_FRACTION | 0.33 | # This fraction a political movement's total support comes from its wealth support |
| MOVEMENT_WEEKLY_RADICALISM_CHANGE | 0.01 | # How much does a movement's radicalism change towards its calculated target each week |
| MOVEMENT_MONTHLY_RADICALS_THRESHOLD | 0.5 | # At this level of radicalism, movement supporters start being radicalized each month at an amount scaled by the radicalism value |
| MOVEMENT_MONTHLY_RADICALS_SCALING_MIN | 0.005 | # The minimum % of supporters radicalized each month when above the radicalization threshold |
| MOVEMENT_MONTHLY_RADICALS_SCALING_MAX | 0.025 | # The maximum % of supporters radicalized each month when above the radicalization threshold |
| MOVEMENT_LOYALISTS_ON_APPROVED_ENACTMENT | 0.25 | # The % of supporters who become more loyal when a law the movement approves of is enacted |
| # Movements with less radicalism than this do not impact law enactment chances # Additionally, movement radicalism won't drop lower than than this when enactment of a law they care about is underway, so lowered radicalism from enactment doesn't end up counterproductive |  |  |
| MOVEMENT_MIN_RADICALISM_FOR_LAW_ENACTMENT_IMPACT | 0.25 |  |
| MOVEMENT_IMMEDIATE_RADICALISM_FROM_ENACTMENT | 0.5 | # This multiplier of target radicalism impact from law enactment is applied immediately on start of enactment |
| MOVEMENT_IMMEDIATE_RADICALISM_FROM_CANCELLATION | -0.5 | # This multiplierof target radicalism impact from law enactment is applied immediately on cancellation of enactment |
| MOVEMENT_RADICALISM_FROM_ACTIVE_LAW_STANCE | -0.05 | # Multiplied by a movement's stance on each active law (positive stance = negative radicalism) |
| MOVEMENT_RADICALISM_FROM_ENACTED_LAW_STANCE | -0.25 | # Multiplied by a movement's comparative stance on currently or recently enacted law (positive stance = negative radicalism) |
| MOVEMENT_RADICALISM_FROM_RADICAL_SUPPORTERS | 1.0 | # Scales against fraction of radicals among movement supporters |
| MOVEMENT_RADICALISM_FROM_LOYALIST_SUPPORTERS | -0.75 | # Scales against fraction of loyalists among movement supporters |
| MOVEMENT_RADICALISM_FROM_SUPPRESSION | 0.0 | # Suppressed movements become this much more radical |
| MOVEMENT_RADICALISM_FROM_BOLSTERING | 0.0 | # Bolstered movements become this much less radical |
| MOVEMENT_PRESSURE_IDEOLOGY_FACTOR | 4.0 | # The chance for a character from an IG to pick an ideology is increased with the amount of pressure exerted from movements espousing that ideology # At 100% pressure, the weight for the ideology is multiplied by ( 1 + this ) |
| colspan=3 | # The chance for the next leader of the IG to follow an ideology is increased with the total prominence of potential leaders espousing that ideology # Unlike movement pressure this effect is not applied when generating ideology for other characters from that IG # This value is also affected by role-specific weights on IGs, such as commander_leader_weight for prominence from commanders # The multiplier is ( 1 + ( this * total prominence multiplied by role weights ) ) |  |
| CHARACTER_PROMINENCE_AND_ROLE_LEADER_IDEOLOGY_FACTOR | 0.04 |  |
| IG_MAX_INFLUENCING_MOVEMENTS | 3 | # An interest group cannot have more than this number of influencing movements |
| IG_SUPPORTING_MOVEMENT_MIN_SUPPORTING_CLOUT | 0.05 | # A movement must be supported by at least this % of the clout in an IG to be shown as a supporting IG for the movement |
| IG_INFLUENCING_MOVEMENT_MIN_SUPPORTING_CLOUT | 0.10 | # A movement must be supported by at least this % of the clout in an IG to be a influencing movement for the IG |
| IG_INFLUENCING_MOVEMENT_STICKYNESS | 1.25 | # Multiply supporting clout of the currently influencing movement in an IG by this for the purposes of determining whether it stays influencing |
| # The values below determine how ideologically divergent an IG can be from an insurrectionary political movement and still join on the civil war side, based on their level of approval # Happy/Loyal IGs will never join civil wars |  |  |
| IG_MAX_IDEOLOGICAL_DELTA_TO_JOIN_CIVIL_WAR_NEUTRAL | 1 |  |
| IG_MAX_IDEOLOGICAL_DELTA_TO_JOIN_CIVIL_WAR_UNHAPPY | 1.5 |  |
| IG_MAX_IDEOLOGICAL_DELTA_TO_JOIN_CIVIL_WAR_ANGRY | 2 |  |
| # Laws that the IG leader's ideology has an opinion has this multiplier for their impact on ideological divergence for joining civil wars |  |  |
| IG_MAX_IDEOLOGICAL_DELTA_TO_JOIN_CIVIL_WAR_LEADER_FACTOR | 2.0 |  |
| BASE_IG_APPROVAL | 0 | # Baseline IG approval |
| MIN_IG_APPROVAL | -20 | # Minimum IG approval |
| MAX_IG_APPROVAL | 20 | # Maximum IG approval |
| MIN_IG_APPROVAL_FROM_LAWS | -5 | # IG cannot have approval lower than this as a total from laws 'on the book' |
| MAX_IG_APPROVAL_FROM_LAWS | 5 | # IG cannot have approval higher than this as a total from laws 'on the book' |
| IG_APPROVAL_FROM_LOYALISTS | 15 | # If 100% of the political strength of the IG is loyalist, change approval by this amount |
| IG_APPROVAL_FROM_RADICALS | -15 | # If 100% of the political strength of the IG is radical, change approval by this amount |
| IG_LAW_DESIRE_RADICAL_CHANGE_THRESHOLD | 2 | # A difference in positions this or higher is considered radical |
| IG_LAW_DESIRE_EXTREME_CHANGE_THRESHOLD | 3 | # A difference in positions this or higher is considered extreme |
| IG_APPROVAL_FROM_LAW | 1 | # IG approval/disapproval for laws that are for/against their ideologies |
| IG_APPROVAL_FROM_LAW_STRONG_STANCE | 2 | # IG approval/disapproval for laws that are strongly for/against their ideologies |
| IG_APPROVAL_FROM_LAW_CHANGE | 5 | # IG approval/disapproval for changing to another law |
| IG_APPROVAL_FROM_RADICAL_LAW_CHANGE | 10 | # IG approval/disapproval for changing to another law, if the change is a major one |
| IG_APPROVAL_FROM_EXTREME_LAW_CHANGE | 20 | # IG approval/disapproval for changing to another law, if the change is extreme |
| IG_IN_GOVERNMENT_APPROVAL | 0 | # Added if IG is in government |
| IG_IN_OPPOSITION_APPROVAL | 0 | # Added if IG is in opposition (and not powerful) |
| IG_POWERFUL_IN_OPPOSITION_APPROVAL | -1 | # Added if powerful IG in opposition |
| STARTUP_MIN_LEGITIMACY_IG_BARRIER | 40 | # Min legitimacy when on startup we allow to remove IGs from goverment that decrease legitimacy |
| APPROVAL_THRESHOLD_ANGRY | -10 | # At this or below approval, IG is considered angry |
| APPROVAL_THRESHOLD_UNHAPPY | -5 | # At this or below approval, IG is considered unhappy |
| APPROVAL_THRESHOLD_HAPPY | 5 | # At this or above approval, IG is considered happy |
| APPROVAL_THRESHOLD_LOYAL | 10 | # At this or above approval, IG is considered loyal |
| CHANGED_LAW_APPROVAL_MONTHS | 60 | # How many months does the approval/disapproval for a law change linger after said law chain |
| # If the difference in progressiveness between the currently active law and an alternative law is this, then it's considered a radical petition # Radical petitions will only happen if there isn't a less extreme alternative that the government could petition for instead |  |  |
| GOVERNMENT_RADICAL_PETITION_THRESHOLD | 100 |  |
| LAW_ENACTMENT_MIN_TOTAL_DAYS | 1 | # Minimum number of total days that an enactment checkpoint can take [>=1] |
| LAW_ENACTMENT_DEFAULT_BASE_DAYS | 100 | # Default number of base days required to reach an enactment checkpoint [>=1] |
| LAW_ENACTMENT_COOLDOWN_DAYS | 730 | # When an enactment fails, or is manually stopped after at least one checkpoint, that law can't be tried to be enacted for this many days [>=0] |
| LAW_ENACTMENT_ADVANCE_FACTOR | 2 | # The _base_ advance chance is the success chance multiplied by this factor [>=1] |
| LAW_ENACTMENT_RULER_IDEOLOGY_EFFECT | 0.05 | # Ruler ideology has this impact on a law's chance to pass or stall depending on relative approval |
| LAW_ENACTMENT_LAW_COMMITMENT_EFFECT | 0.05 | # Committing to enacting a law via treaty adds this much to pass chance, scaled by the number of ranks the country the comittee has on the committer |
| LAW_ENACTMENT_MOVEMENT_SUPPORT_PASS_EFFECT | 1.0 | # Movement support has this impact on a law's chance to pass |
| LAW_ENACTMENT_MOVEMENT_SUPPORT_STALL_EFFECT | 1.0 | # Movement support has this impact on a law's chance to stall |
| LAW_ENACTMENT_IG_CLOUT_STALL_EFFECT | 1.0 | # Opposing IG clout has this base impact on a law's chance to stall |
| LAW_ENACTMENT_IG_NEUTRAL_MULT | 0.5 | # Stall effect of opposing IG is multiplied by this for neutral IGs |
| LAW_ENACTMENT_IG_UNHAPPY_MULT | 1.0 | # Stall effect of opposing IG is multiplied by this for unhappy IGs |
| LAW_ENACTMENT_IG_ANGRY_MULT | 1.5 | # Stall effect of opposing IG is multiplied by this for angry IGs |
| LAW_ENACTMENT_MAX_PHASES | 3 | # Law enactment is successfully completed when it advances to this phase |
| LAW_MIN_SUCCESS_CHANCE | 0.01 | # Law must have at least this minimum chance to be considered. |
| STATE_BUREAUCRACY_BASE_COST | 10 | # The base cost per incorporated state |
| STATE_BUREAUCRACY_POP_BASE_COST | 4 | # The base BUR multiplier per population multiple |
| STATE_BUREAUCRACY_POP_MULTIPLE | 100000 | # Number of people BUR cost is based on |
| MINIMUM_INVESTMENT_COST | 10 | # The absolute minimum cost in BUR per investment level |
| POWERFUL_IG_THRESHOLD | 0.20 | # Interest groups with more Clout than this are considered to be influential |
| POWERFUL_IG_CUTOFF | 0.18 | # Powerful interest groups with less Clout than this will stop being influential |
| POWERFUL_IG_TRAIT_BONUS | 1 | # The effects of all trait modifiers from influential IGs are increased by this, 1 = +100% |
| IG_TRAIT_STICKINESS | 2 | # If an IG trait is already active, this is the amount of Approval difference required to deactivate it |
| MARGINAL_IG_THRESHOLD | 0.05 | # Interest Groups with Clout above this value are considered relevant while those below are marginal (if not also In Government) |
| MARGINAL_IG_CUTOFF | 0.04 | # Interest Groups who are already relevant will only become marginal again if they drop below this value. |
| MARGINAL_IG_JOIN_PARTY_POPULATION_THRESHOLD | 0.025 | # Marginal IGs that are supported by at least this % of the population are able to join parties and become non-marginal |
| MIN_AMENABILITY | 0 |  |
| MAX_AMENABILITY | 100 |  |
| MIN_AMENABILITY_TENSE_NEGOTIATION | 25 |  |
| MIN_AMENABILITY_NORMAL_NEGOTIATION | 50 |  |
| MIN_AMENABILITY_FRIENDLY_NEGOTIATION | 75 |  |
| RECENT_PARTY_DAYS | 14 | # Party is considered recently formed if activated within RECENT_PARTY_DAYS days range |
| MAX_GOVERNMENT_ALTERNATIVES_TO_CONSIDER_AI | 64 | # When evaluating government reform options (for AI), only consider this many constellations (sorted by average clout, descending) [>=1] |
| MAX_GOVERNMENT_ALTERNATIVES_TO_CONSIDER_PLAYER | 256 | # When evaluating government reform options (the 3 suggested to the player in the UI), only consider this many constellations (sorted by average clout, descending) [>=3] |
| MAX_GOVERNMENT_ALTERNATIVES_OPTIONS_WANTED_FOR_VALIDATION | 8 | # When evaluating government reform options during government validation stage |
| MAX_GOVERNMENT_ALTERNATIVES_TO_CONSIDER_FOR_VALIDATION | 256 | # When evaluating government reform options during government validation stage |
| DEFAULT_LAW_ACTIVATION_DATE | "1836.1.1" |  |
| CIVIL_WAR_COOLDOWN_MONTHS | 9 | # After a civil war concludes, it takes this long before another one can start |
| FAILED_CIVIL_WAR_START_COOLDOWN_MONTHS | 3 | # If a movement fails to get any supporting states or (for revolutions) supporting army units when trying to start a civil war, wait this long before trying again |
| # If there are multiple civil wars that could start, and the current active one has lower activism, it can potentially be replaced by a more viable civil war # This is the minimum delta required for another civil war to replace the active one |  |  |
| MIN_ACTIVISM_DELTA_TO_REPLACE_OTHER_CIVIL_WAR | 0.1 |  |
| # The values below are used to calculate the target number of states that rise up when a civil war without an explicit target_fraction_of_states begins # This is just a target value - the end result may end up different based on state weights defined in the civil war scripting |  |  |
| CIVIL_WAR_UPRISING_STATES_DEFAULT_CLOUT_FACTOR | 1.0 | # Fraction of total states in country, multiplied by revolutionary IG clout |
| CIVIL_WAR_UPRISING_STATES_DEFAULT_POPULAR_SUPPORT_FACTOR | 0.5 | # Fraction of total states in country, multiplied by movement popular support |
| CIVIL_WAR_UPRISING_STATES_DEFAULT_MILITARY_SUPPORT_FACTOR | 0.25 | # Fraction of total states in country, multiplied by movement military support |
| CIVIL_WAR_UPRISING_STATES_DEFAULT_WEALTH_SUPPORT_FACTOR | 0.25 | # Fraction of total states in country, multiplied by movement wealth support |
| CIVIL_WAR_UPRISING_STATES_DEFAULT_MIN_FRACTION | 0.10 | # Min fraction of total states in country that will try to rise up |
| CIVIL_WAR_UPRISING_STATES_DEFAULT_MAX_FRACTION | 0.75 | # Max fraction of total states in country that will try to rise up |
| CIVIL_WAR_POTENTIAL_UPRISING_STATE_MIN_MULTIPLIER | 0.01 | # The weight for an uprising state cannot be reduced below this by local clout/identity share of population |
| CIVIL_WAR_UPRISING_STATE_RANDOM_FACTOR | 0.5 | # The higher this is, the more random uprising state selection will be |
| CIVIL_WAR_UPRISING_STATE_CONNECTIONS_FACTOR | 1.0 | # The score of an uprising state is multiplied by ( 1 + this number * the number of other uprising states it connects to ) |
| CIVIL_WAR_UPRISING_STATE_NON_CONNECTED_SECESSION_FACTOR | 0.01 | # The score of an uprising state is multiplied by this for seceding states that are not connected to any other rebel states in the same area |
| CIVIL_WAR_UPRISING_ISOLATED_STATE_FACTOR | 100.0 | # The score of an uprising state is multiplied by this if it's isolated from the most loyalist state by uprising states |
| CIVIL_WAR_NON_CONTIGUOUS_UPRISING_STATE_FACTOR | 0.25 | # The score of an uprising state is multiplied by this if it would end up cutting off a number of loyalist states greater than the remaining number of states that should rebel |
| CIVIL_WAR_UPRISING_ARMY_TARGET_DELTA_FACTOR | 10.0 | # How heavily are states weighted towards or against rising up based on how their defection will affect the ideal number of army units that should be rebelling |
| CIVIL_WAR_UPRISING_NAVY_TARGET_DELTA_FACTOR | 5.0 | # How heavily are states weighted towards or against rising up based on how their defection will affect the ideal number of navy units that should be rebelling |
| # Overseas areas of the country that are considered colonial will either be fully loyal or fully rebellious, as determined by the logic below |  |  |
| CIVIL_WAR_UPRISING_STATES_OVERSEAS_HIGH_UNINCORPORATED_FRACTION | 0.5 | # At this % of unincorporated states or above in non capital area, it will be considered 'colonial' even if it has a close sea adjancency to capital |
| CIVIL_WAR_COLONIAL_UPRISING_MIN_CHANCE | 0.25 | # If the chance for a colonial area to rebel is below this, it will always stay loyal |
| CIVIL_WAR_COLONIAL_UPRISING_CHANCE_WEALTH_SUPPORT_FACTOR | 2.0 | # Chance for each colonial area to rebel, multiplied by insurrectionary movement wealth support |
| CIVIL_WAR_COLONIAL_UPRISING_CHANCE_CLOUT_FACTOR | 1.0 | # Chance for each colonial area to rebel, multiplied by insurrectionary IG clout in the area |
| CIVIL_WAR_UPRISING_STATE_EXCESSIVE_ARMY_FRACTION | 0.5 | # If a state contains at least this much of the area's army |
| CIVIL_WAR_UPRISING_ARMY_FRACTION_MILITARY_SUPPORT_FACTOR | 0.75 | # Target fraction of the army that should rebel, multiplied by insurrectionary movement military support |
| CIVIL_WAR_UPRISING_ARMY_FRACTION_CLOUT_FACTOR | 0.25 | # Target fraction of the army that should rebel, multiplied by insurrectionary IG clout in the area |
| CIVIL_WAR_UPRISING_NAVY_FRACTION_MILITARY_SUPPORT_FACTOR | 0.75 | # Target fraction of the navy that should rebel, multiplied by insurrectionary movement military support |
| CIVIL_WAR_UPRISING_NAVY_FRACTION_CLOUT_FACTOR | 0.25 | # Target fraction of the navy that should rebel, multiplied by insurrectionary IG clout in the area |
| # Insurrectionary countries receive an injection of military goods in their capital, below values control which goods and in which quantities # Multiplies are based on the states assigned to the civil war and the pre-civil war market sell & buy orders |  |  |
| CIVIL_WAR_STOCKPILE_SMALL_ARMS_GOODS_TYPE | "small_arms" |  |
| CIVIL_WAR_STOCKPILE_SMALL_ARMS_MULTIPLIER | 0.80 |  |
| CIVIL_WAR_STOCKPILE_AMMUNITION_GOODS_TYPE | "ammunition" |  |
| CIVIL_WAR_STOCKPILE_AMMUNITION_MULTIPLIER | 0.80 |  |
| CIVIL_WAR_STOCKPILE_ARTILLERY_GOODS_TYPE | "artillery" |  |
| CIVIL_WAR_STOCKPILE_ARTILLERY_MULTIPLIER | 0.65 |  |
| CIVIL_WAR_MAX_PROGRESS_AT_CHECKPOINT | 0.25 | # A civil war can advance at most this amount per checkpoint, regardless of radicalism |
| MIN_RADICALISM_FOR_CIVIL_WAR_PROGRESSION | 0.75 | # A political movement must have this much radicalism for a civil war to start organizing |
| MIN_RADICALISM_FOR_CIVIL_WAR_START | 1.0 | # Allow a civil war to start at this amount of radicalism or more |
| CIVIL_WAR_PROGRESS_DECAY | 0.1 | # The progress of civil wars with insufficient support decays at this rate |
| CIVIL_WAR_PROGRESS_RADICALISM_WEIGHT | 0.2 | # civil wars gain progress based on the movement's radicalism, multiplied by this weight (may be affected by modifiers) |
| CIVIL_WAR_CHECKPOINT_INTERVAL_BASE_WEEKS | 8 | # civil war progress will be updated every this many weeks (may be affected by modifiers) |
| CIVIL_WAR_CHECKPOINT_INTERVAL_MAXIMUM_WEEKS | 52 | # This serves as a limit, to protect modifiers from reducing the progress speed to zero |
| CIVIL_WAR_CONSCRIPTION_RATE_POPULAR_SUPPORT_MULTIPLIER | 0.25 | # At 100% popular support, insurrectionary states gain this multiplier of civil_war_conscription modifier |
| CIVIL_WAR_CONSCRIPTION_RATE_CLOUT_MULTIPLIER | 0.05 | # At 100% clout from supporting IGs, insurrectionary states gain this multiplier of civil_war_conscription modifier |
| CIVIL_WAR_CONSCRIPTION_RATE_MAX_MULTIPLIER | 0.1 | # Total multiplier of civil_war_conscription modifier cannot exceed this number (this is intentionally much lower than the possible maximum scaling above, as movements very rarely have >10-20% popular support) |
| CIVIL_WAR_LOSER_IG_AND_MOVEMENT_DEBUFF_YEARS | 20 | # Debuff duration in years for IG that looses in a revolution |
| SECESSION_WON_LOYALISTS_INCREASED_PERCENTAGE | 0.5 | # This percentage of pops in the secession country of the seceded culture will become more loyal after a secession is victorious |
| SECESSION_START_RADICALS_REDUCED_PERCENTAGE | 1.0 | # The number of radicals of pops of the seceded culture in states that seceded will decrease by this amount when a secession war begins |
| SECESSION_LOST_RADICALS_REDUCED_PERCENTAGE | 1.0 | # The number of radicals of pops of the seceded culture in states that seceded will decrease by this amount when a secession is crushed |
| REVOLUTION_START_REBEL_IG_RADICALS_REDUCED_PERCENTAGE | 1.0 | # The number of radicals of pops will decrease by this amount when a revolution starts (relative to membership in insurrectionist IGs) |
| REVOLUTION_ENDED_RADICAL_BASE_REMOVAL_PERCENTAGE | 0.5 | # When a revolution ends, this base fraction of radicals is removed from all pops regardless of IG membership to represent 'civil war fatigue' |
| REVOLUTION_LOST_REBEL_IG_RADICALS_REDUCED_PERCENTAGE | 0.25 | # The number of radicals of pops will additionally decrease by this amount when a revolution is crushed (relative to membership in defeated IGs) |
| REVOLUTION_WON_LOYAL_IG_RADICALS_REDUCED_PERCENTAGE | 0.5 | # The number of radicals of pops will additionally decrease by this amount when a revolution is crushed (relative to membership in victorious IGs) |
| IG_SUPPRESSION_COST | 200 | # The amount of AUT it costs to Suppress an IG |
| IG_BOLSTER_COST | 200 | # The amount of AUT it costs to Bolster an IG |
| DEFAULT_GOODS_TAX_COST | 100 | # The amount of AUT it costs to tax a good by default |
| TURMOIL_STATE_EFFECTS_THRESHOLD | 0.25 | # How much turmoil a state needs to have before it gets any state-wide effects |
| TURMOIL_STATE_HIGH_EFFECTS_THRESHOLD | 0.50 | # Above this turmoil, add a harsher modifier |
| TURMOIL_STATE_EXTREME_EFFECTS_THRESHOLD | 0.75 | # Above this turmoil, add the harshest modifier |
| OBSTINANCE_MAX | 0.2 | # Maximum amount of obstinance a state can have (when at max the state will get 100% effect of the obstinance modifier) |
| OBSTINANCE_MOVEMENT_REQUIRED_RADICALISM | 0.5 | # Minimum amount of radicalism/activism required for a movement to contribute to a state's obstinance |
| MIN_INSTITUTION_INVESTMENT | 1 | # Lowest Investment Level for active Institutions (modifier is clamped to this) |
| MAX_INSTITUTION_INVESTMENT | 5 | # Highest Investment Level for active Institutions (modifier is clamped to this) |
| DAILY_INSTITUTION_SIZE_CHANGE | 0.0028 | # Percent increase / decrease in Institution Size per day (0.0028 ~ 1/365) |
| INITIAL_MOMENTUM_MIN | 0.5 | # Minimum randomly assigned Momentum at the start of the election period |
| INITIAL_MOMENTUM_MAX | 1.5 | # Maximum randomly assigned Momentum at the start of the election period |
| POPULARITY_MOMENTUM_FACTOR | 0.005 | # How much Momentum does a party gain or lose from their leader's popularity |
| ELECTION_INTERVAL_YEARS | 4 | # How many years normally pass between elections |
| CAMPAIGN_PERIOD_MONTHS | 6 | # How long the Campaign Period before the election is |
| MIN_AFFILIATION_TO_STAY_IN_PARTY | 0 | # An IG must have this much affiliation with a party to want to stay in it |
| MIN_AFFILIATION_TO_JOIN_PARTY | 1 | # An IG must have this much affiliation with a party to want to join it |
| MAX_ELECTORAL_CONFIDENCE | 1.0 | # Electoral confidence can never be higher than this |
| INITIAL_ELECTORAL_CONFIDENCE | 1.0 | # Starting electoral confidence at start of game or when elections are first introduced |
| REFORM_GOVERNMENT_PERIOD | 6 | # How many months after election you can reform government for free |
| REFORM_GOVERNMENT_RADICALIZATION_RATE | 0.25 | # How many percent of a IG's supporters that will get radicalized when removed from government. |
| RADICALISM_AGITATING_THRESHOLD | 0.25 |  |
| RADICALISM_PROTESTING_THRESHOLD | 0.50 |  |
| RADICALISM_MILITANT_THRESHOLD | 0.75 |  |
| SUPPORT_RELEVANT_THRESHOLD | 0.05 |  |
| SUPPORT_SIGNIFICANT_THRESHOLD | 0.25 |  |
| SUPPORT_DOMINANT_THRESHOLD | 0.5 |  |
| SUPPORT_UNIVERSAL_THRESHOLD | 0.75 |  |
| INCOHERENCE_FACTOR | 5 | # The amount to multiply the approval value with to get an incoherence score for legitimacy |
| LEGITIMACY_PENALTY_FOR_EACH_EXCESS_ENTITY | 20 | # How much Legitimacy is lost for each group in government above the allowance determined by country_legitimacy_govt_size_add |
| SHOW_CONFIRMATION_BELOW_LEGITIMACY | 25 |  |
| POLITICAL_LOBBY_BASELINE_DECAY_FACTOR_KEY | "appeasement_baseline_decay" | # If changing the name of this appeasement factor in the database, it must be changed here and vice versa |
| # If the number of IG members of a newly created political lobby is below POLITICAL_LOBBY_DESIRED_MEMBERS, join weight of IGs for this lobby will be multiplied by 1 + (number of members needed to reach POLITICAL_LOBBY_DESIRED_MEMBERS * POLITICAL_LOBBY_OVER_DESIRED_MEMBERS_JOIN_FACTOR) # If the number of IG members of a newly created political lobby is above POLITICAL_LOBBY_DESIRED_MEMBERS, join weight of IGs for this lobby will be divided by 1 + (number of members needed to reach POLITICAL_LOBBY_DESIRED_MEMBERS * POLITICAL_LOBBY_OVER_DESIRED_MEMBERS_JOIN_FACTOR) # Number of IG members of a newly created political lobby should never exceed POLITICAL_LOBBY_CREATION_MAX_MEMBERS # These factors are *only* applied during lobby creation |  |  |
| POLITICAL_LOBBY_CREATION_DESIRED_MEMBERS | 2 |  |
| POLITICAL_LOBBY_CREATION_DESIRED_MEMBERS_JOIN_FACTOR | 0.5 |  |
| POLITICAL_LOBBY_CREATION_MAX_MEMBERS | 3 |  |
| POLITICAL_LOBBY_MIN_NON_MARGINALIZED_MEMBERS | 1 | # At least this many non-marginalized IGs must be willing to join a lobby for it to be created |
| POLITICAL_LOBBY_MINIMUM_JOIN_WEIGHT_THRESHOLD | 50 | # At this join weight, an IG has a chance to join a lobby when it forms |
| POLITICAL_LOBBY_GUARANTEED_JOIN_WEIGHT_THRESHOLD | 100 | # At this join weight, an IG will always join a lobby when it forms. If below this but above POLITICAL_LOBBY_MINIMUM_JOIN_WEIGHT_THRESHOLD, they have a random chance to join based on their join weight. |
| # An interest group cannot be part of more than this number of political lobbies of the same category # If an IG wants to join a lobby but is at the limit, it may leave one of its current lobby if the new lobby scores higher on IG attraction |  |  |
| MAX_NUM_POLITICAL_LOBBIES_OF_SAME_CATEGORY_PER_IG | 1 |  |
| # If a newly created lobby has a join weight equal to or greater than the join weight of one of their current lobbies of the same type times this, they will join the new lobby and leave the old one # This only applied if they are capped on number of lobbies to join due to MAX_NUM_POLITICAL_LOBBIES_OF_SAME_TYPE_PER_IG |  |  |
| POLITICAL_LOBBY_JOIN_WEIGHT_REPLACEMENT_THRESHOLD | 1.25 |  |
| POLITICAL_LOBBY_APPEASEMENT_APPROVAL_AVERAGED | no | # If set to yes, approval from lobby appeasement is averaged out between lobbies instead of summed in total |
| POLITICAL_LOBBY_MIN_APPEASEMENT | -10 | # Appeasement cannot be lower than this |
| POLITICAL_LOBBY_MAX_APPEASEMENT | 10 | # Appeasement cannot be greater than this |
| POLITICAL_LOBBY_STARTING_APPEASEMENT | 0 | # Lobbies start with this amount of appeasement |
| POLITICAL_LOBBY_BASELINE_APPEASEMENT | 0 | # Appeasement will naturally decay towards this value over time |
| POLITICAL_LOBBY_APPEASEMENT_DECAY_TIME | 1025 | # It takes this many days for a lobby's appeasement value to decay by 1 towards baseline |
| POLITICAL_LOBBY_APPEASEMENT_APPROVAL_IMPACT | 1.0 | # Each point of lobby appeasement translates into this amount of approval for the IGs that are part of the lobby |
| MIN_DECREE_COST | 0.1 | # The cost of a decree cannot drop below this fraction of the base cost, regardless of how many modifier discounts you have |

### Economy

| Define | Default Value | Dev Comment |
|---|---|---|
| MIN_CONSTRUCTION_EFFICIENCY | 0.05 | # Construction efficiency cannot go below this amount |
| NUM_TIMES_TO_INITIALIZE_WEALTH | 10 | # The more times you run this the more accurate setup will be for Pop wealth compared to income |
| NUM_TIMES_TO_UPDATE_TRADE_DURING_INITIALIZATION | 10 | # Extra times that separate trade update step is run |
| COUNTRY_GDP_MODIFIER_DIVISOR | 1000 | # Scale the country_gdp static modifier by this GDP divisor |
| COUNTRY_GDP_MODIFIER_MAX_MULTIPLIER | 200000 | # The country_gdp modifier multiplier cannot be higher than this |
| COUNTRY_GDP_CONSTRUCTION_MODIFIER_DIVISOR | 2000000 | # Scale the country_gdp_construction static modifier by this GDP divisor |
| COUNTRY_GDP_CONSTRUCTION_MODIFIER_BASE_MULTIPLIER | 0.2 | # Always added to the country_gdp_construction multiplier, regardless of GDP |
| COUNTRY_GDP_CONSTRUCTION_MODIFIER_SCALED_MULTIPLIER | 0.8 | # The country_gdp_construction modifier multiplier is scaled against this |
| COUNTRY_GDP_CONSTRUCTION_MODIFIER_MAX_MULTIPLIER | 1.0 | # The country_gdp_construction modifier multiplier cannot be higher than this |
| ECONOMY_OF_SCALE_START_LEVEL | 1 | # Level at which buildings start getting economy of scale bonuses. Levels lower than this value provide no bonus [>=1] |
| USE_NATIONALIZED_ECONOMY_OF_SCALE_PENALTY | no | # Whether ECONOMY_OF_SCALE_NATIONALIZED_FRACTION_MULT should be applied to economy of scale modifier for buildings with nationalized levels |
| ECONOMY_OF_SCALE_NATIONALIZED_FRACTION_MULT | 0.5 | # Non-government building economy of scale modifier if multiplied by (1 - the fraction of nationalized levels * this) |
| IN_DEFAULT_MINIMUM_PENALTY_SCALE | 0.1 | # This amount of the 'in default' throughput penalty is applied right away |
| IN_DEFAULT_DAYS_TO_FULL_PENALTY | 365 | # How many days of being in default does it take to get the full throughput penalty |
| DECLARE_BANKRUPTCY_PENALTY_DURATION_YEARS | 10 | # How many years does it take for penalties from declaring bankruptcy to fully decay |
| DECLARE_BANKRUPTCY_RADICALIZATION_BASE_FACTOR | 0.1 | # Radicalize this percentage of all pops when declaring bankruptcy |
| DECLARE_BANKRUPTCY_RADICALIZATION_SHARES_FACTOR | 0.05 | # For each per-pop shares in their building, radicalize this percentage of a pop on declaring bankruptcy |
| FIRED_POP_RADICALIZATION_FRACTION | 0.1 | # This percentage of a pop becomes radicalized when they lose their job, for instance due to a building being downsized |
| # When a building is nationalized, pops are radicalized in one of two ways: # 1: Pops that work in the building get radicalized based on number of levels nationalized based on fraction of levels of the building that are self-owned # 2: Pops that own shares in ownership-type building (ie, Manor Houses/Financial Districts) anywhere in the country get radicalized based on number of privately held levels nationalized and the investment score of their building towards the nationalized building type |  |  |
| NATIONALIZE_BUILDING_SELF_OWNED_RADICALIZATION_FACTOR | 0.25 | # Multiplied by fraction of self-owned levels |
| NATIONALIZE_BUILDING_PRIVATELY_OWNED_RADICALIZATION_FACTOR | 0.01 | # Multiplied by number of levels owned by another building (clamped to NATIONALIZE_BUILDING_OWNING_POP_TYPE_RADICALIZATION_MAX_MULTIPLIER) |
| NATIONALIZE_BUILDING_PRIVATELY_OWNED_RADICALIZATION_MAX_MULTIPLIER | 20 |  |
| NATIONALIZE_BUILDING_PRIVATELY_OWNED_RADICALIZATION_SCORE_DIVISOR | 1 | # Number of radicalized ownership-type pops is multiplied by their building's investment, then divided by this |
| NATIONALIZE_BUILDING_OTHER_COUNTRY_OWNED_RELATIONS_IMPACT | -2 | # Nationalizing a building that is owned by the government of another country results in this relations impact per building level nationalized |
| NATIONALIZE_BUILDING_OTHER_COUNTRY_POP_OWNED_RELATIONS_IMPACT | -1 | # Nationalizing a building that is owned by the pops of another country results in this relations impact per building level nationalized |
| NATIONALIZE_BUILDING_NO_COMPENSATION_IMPACT_MULT | 3.0 | # Multiplier to number of radicals & relations hits from nationalization if done without monetary compensation |
| AUTO_DOWNSIZE_BUILDING_MIN_EMPTY_PRIVATE_LEVELS | 1.0 | A (non Trade Center) building must be missing at least this many privately held levels of employment to start considering auto-downsizing (both this and the below requirement are applied) |
| AUTO_DOWNSIZE_BUILDING_MIN_EMPTY_FRACTION | 0.1 | # A (non Trade Center) building must be missing at least this many levels of employment (in relative numbers) to start considering auto-downsizing (both this and the above requirement are applied) |
| AUTO_DOWNSIZE_BUILDING_MIN_UNUSED_TRADE_CAPACITY_FRACTION | 0.1 | # A Trade Center must have at least this much unused Trade Capacity (as a fraction of the whole) to consider auto downsizing |
| AUTO_DOWNSIZE_BUILDING_MIN_UNUSED_TRADE_CAPACITY | 20 | # A Trade Center must have at least this much unused Trade Capacity (in absolute numbers) to consider auto downsizing |
| AUTO_DOWNSIZE_BUILDING_MONTHS_TO_WAIT | 6 | # After a building decides to start auto-downsizing, wait this many months before actually starting to downsize, in case conditions change |
| # Pollution Impact = (GeneratedPollution (StateRegion) / (DIVISOR_BASE + DIVISOR_ARABLE_LAND_MULT * SQRT(ArableLand (State Region)))/POLLUTION_MAX |  |  |
| POLLUTION_TARGET_DIVISOR_BASE | 50 | # Base value to divide total pollution generation by for calculating state region pollution target level |
| POLLUTION_TARGET_DIVISOR_ARABLE_LAND_MULT | 1.5 | # Amount per arable land to add to pollution divisor |
| POLLUTION_CHANGE_SPEED | 0.255 | # Each day, pollution in state region changes by this amount towards target |
| POLLUTION_MAX | 255 |  |
| POLLUTION_SPREAD_TO_NEIGHBOR | 0.25 | # Adjacent state regions always have at least this much of their neighbor's pollution level |
| GOODS_LEADERBOARD_SIZE | 10 | # How many spots there are on each goods leaderboard |
| MIN_SPOT_PRESTIGE_AWARD | 3 | # How many spots on the goods leaderboard get awarded Prestige |
| GOODS_LEADERBOARD_GLOBAL_GDP_SCALING | 10000000000 | # At this amount of global yearly GDP, max scaling to top goods producer prestige is applied |
| GOODS_LEADERBOARD_PRESTIGE_BASE | 0.25 | # This multiplier of prestige from being top goods producer is always awarded |
| GOODS_LEADERBOARD_PRESTIGE_SCALED | 2.75 | # This multiplier of prestige from being top goods producer is scaled against global GDP |
| MIN_GOODS_PRICE | 1 | # A good cannot have a lower base price than this |
| PRICE_RANGE | 0.75 | # min price of a good is base * (1 - PRICE_RANGE), Max price is base * (1 + PRICE_RANGE), PRICE_RANGE is locked to [0-1] |
| BUY_SELL_DIFF_AT_MAX_FACTOR | 2 | # the difference between buy/consumption and sell/production at min/max pricing, e.g. if set to 4 then if buy orders are 4x sell orders price is maxed |
| GOODS_SHORTAGE_PENALTY_THRESHOLD | 0.5 | # If supply / demand is lower than this, start applying output penalties, by default this should be ( 1 / BUY_SELL_DIFF_AT_MAX_FACTOR ) |
| GOODS_SHORTAGE_PENALTY_INCREASE_SPEED | 0.01 | # Goods shortage penalty increases by this fraction of the target each day |
| GOODS_SHORTAGE_PENALTY_DECREASE_SPEED | 0.01 | # Goods shortage penalty goes down by this fraction of GOODS_SHORTAGE_PENALTY_MAX each day |
| GOODS_SHORTAGE_PENALTY_MIN | 0.05 | # Goods shortage penalty can't be lower than this if there is any shortage |
| GOODS_SHORTAGE_PENALTY_MAX | 0.5 | # Goods shortage penalty can't be higher than this, so long as all the input goods exist in some quantity |
| GOODS_SHORTAGE_PENALTY_MISSING_INPUTS | 0.75 | # This penalty is applied when an input good is missing entirely from local supply |
| GOODS_SHORTAGE_PENALTY_MILITARY_BUILDING_SPEED_MULT | 5.0 | # Shortage penalties increase and decrease at this multiplier rate for military buildings |
| POP_NEED_BASIC_FOOD | "popneed_basic_food" |  |
| MINIMUM_GOODS_TRADED_QUANTITY | 0.5 | # Traded quantity for a good can never be lower than this |
| WORLD_MARKET_GOODS_DEMAND_BUFFER | 10 | # The below value exists to ensure the world market imports are seeded with 'new' goods by adding the trade quantity of the good * times this to world market demand # This is so that it's always profitable to be the first country exporting something |
| WORLD_MARKET_HUB_SCORE_STICKYNESS | 3.0 | # If a state is a World Market Hub, another state needs to exceed its hub score by this factor to replace it as the new hub |
| WORLD_MARKET_HUB_SCORE_PORT_FACTOR | 10 | # Applied to hub score for each level of port present |
| WORLD_MARKET_HUB_SCORE_GDP_FACTOR_DIVISOR | 100000 | # 1 hub score is added for each this amount of GDP in the state |
| WORLD_MARKET_HUB_SCORE_TRADE_CAPACITY_FACTOR | 0.1 | # Applied to hub score for each Trade Capacity in the state |
| WORLD_MARKET_HUB_SCORE_MARKET_CAPITAL_FACTOR | 100 | # This amount of hub score is added for the market capital |
| WORLD_MARKET_LOCATION | "x9137A4" | # This province is used for the purpose of determining if a state has access to the world market or not. The province itself is not exposed to the player directly. |
| NON_TRADE_CENTER_STATE_TRADE_POTENTIAL_UPDATE_FREQUENCY | 30 | # How many days must pass between updating trade potential in states that do not have a Trade Center # The lower this is the more recent data the AI will have for evaluating new Trade Center construction, but performance will be impacted |
| TRADE_CENTER_ADVANTAGE_PRICE_MULTIPLIER | 0.25 | # This much of relative advantage translates into a multiplier on price # Applied to the delta between relative advantage and 1 # For example, if TRADE_CENTER_ADVANTAGE_PRICE_MULTIPLIER is 0.5 and relative advantage is 2, then the price multiplier is 1 + ( ( 2 - 1 ) * 0.5 ) = 1.5 |
| TRADE_CENTER_ADVANTAGE_BASE | 100 | # Base amount of advantage that Trade Centers have |
| TRADE_CENTER_ADVANTAGE_MARKET_AREA_PRODUCTION_FACTOR | 200 | # Trade Centers get this amount of export advantage for market area production (scaled against global production/consumption, multiplied by Market Access) |
| TRADE_ADVANTAGE_COMPANY_CHARTER_FACTOR | 50 | # Company charters get this amount of export advantage for market production |
| TRADE_CENTER_ADVANTAGE_MARKET_PRESTIGE_GOOD_FACTOR | 100 | # Trade Centers get this amount of export advantage based on the fraction of goods production in their market that is prestige goods (prestige goods have no effect on import advantage) |
| TRADE_CENTER_ADVANTAGE_TRADE_AGREEMENT_FACTOR | 100 | # Trade Centers get this amount of export/import advantage, scaled against % of opposite-direction trade is from markets covered by trade agreements |
| TRADE_CENTER_ADVANTAGE_TREATY_PORT_FACTOR | 200 | # Trade Centers get this amount of export/import advantage, scaled against % of opposite-direction trade from Treaty Ports owned by their parent country |
| # Only one of the penalties below is ever applied, in the following priority order: Embargo, War |  |  |
| TRADE_CENTER_ADVANTAGE_EMBARGO_FACTOR | -100 | # Trade Centers lose this amount of export/import advantage, scaled against % of opposite-direction trade is from markets where the owner is embargoed by the market controller |
| TRADE_CENTER_ADVANTAGE_AT_WAR_FACTOR | -75 | # Trade Centers lose this amount of export/import advantage, scaled against % of opposite-direction trade is from markets where the owner is at war with the market controller |
| # Weights for Trade Center preference in importing/exporting to other specific Trade Centers |  |  |
| TRADE_CENTER_PREFERENCE_BASE | 1 | # Base weight in preference for each other Trade Center |
| TRADE_CENTER_PREFERENCE_SAME_POWER_BLOC_MULTIPLIER | 0.5 | # Added to weight multiplier if both Trade Centers are part of the same Power Bloc |
| TRADE_CENTER_PREFERENCE_TRADE_AGREEMENT_MULTIPLIER | 4.0 | # Added to weight multiplier for each Trade Agreement between the two countries |
| TRADE_CENTER_PREFERENCE_EMBARGO_DIVISOR | 2.0 | # Added to weight divisor for each Embargo between the two countries |
| TRADE_CENTER_PREFERENCE_NO_INTEREST_DIVISOR | 0.25 | # Added to weight divisor for each side that lacks an Interest in the other's market |
| TRADE_CENTER_PREFERENCE_DISTANCE_DIVISOR | 0.25 | # Added to weight divisor per multiple of expected distance between the two Trade Centers' hubs |
| TRADE_CENTER_PREFERENCE_TOLL_DIVISOR | 0.05 | # Weight is divided by 1 + ( toll rate in whole percent * this ) for strait tolls along the route between two Trade Centers' hubs |
| SEA_DISTANCE_EXPECTED_TRAVEL_DISTANCE | 1000 | # Expected sea travel distance - distances below this do not apply any scaling, distances above scale linearly |
| MAX_TRADE_ROUTE_ALTERNATIVES | 3 | # Maximum number of alternate sea paths calculated between world market hubs |
| MARKET_SHARE_FROM_GDP | 1.0 | # Get this many points of market share per pound of GDP in states |
| MARKET_SHARE_MARKET_CONTROLLER_FACTOR | 1.33 | # Market controller's market points count for this much more |
| MARKET_SHARE_MARKET_ACCESS_BASE | 0.5 | # How much of market points is always gained regardless of market access |
| MARKET_SHARE_MARKET_ACCESS_SCALED | 0.5 | # How much of market points is gained based on market access |
| COUNTRY_MIN_CREDIT_BASE | 100000 | # Added to the total Building Cash Reserves to determine credit limit (base) |
| COUNTRY_MIN_CREDIT_SCALED | 0.5 | # Added to the total Building Cash Reserves to determine credit limit (multiplied by GDP) |
| CREDIT_RATIO_MAX_OVERRUN | 0.01 | # Countries can accumulate this percentage more of a debt "hole" than their credit limit when in default |
| GOLD_RESERVE_RATIO_AT_START | 0.25 | # Unless a country history's 'treasury' parameter is set to a non-zero value, countries start with this ratio of their gold reserve in gold |
| BUILDING_INITIAL_WAGE_WEEKS | 2 | # A building will not adjust its wages for the first this many weeks of its existence |
| MAX_WAGE_STEP_CHANGE | 0.1 | # Wage rates can change at most this much each week |
| SUBSIDIES_MIN_GAIN | 0 | # If a building is subsidized, it will always collect enough subsidies to ensure at least this weekly cash reserve growth |
| DEFAULT_MIN_HIRING_RATE | 0.01 | # Default weekly min hiring limit applied in a building per profession as a ratio of full employment |
| DEFAULT_MAX_HIRING_RATE | 0.1 | # Default weekly max hiring limit applied in a building per profession as a ratio of full employment |
| HIRING_RANGE_WEEKLY_CHANGE | 0.01 | # Weekly hiring range of a building is decreased or increased by this based on whether it is failing to hire at its current rate or not |
| EMPLOYMENT_PROPORTIONALITY_LIMIT | 0.1 | # A building cannot have a difference of ratio of full employment between any two professions greater than this limit |
| MINIMUM_EMPLOYEES | 10 | # If a building has fewer employees than this, it will always attempt to hire |
| BUILDING_WAGES_DIVIDEND_INCOME_FACTOR | 0.5 | # A pop with dividend income has its wealth multiplied by 1 - ( the fraction of their income that is dividends * this ) to ensure buildings don't start wage dumping just because all employees are getting dividends |
| BUILDING_WAGES_WELFARE_INCOME_FACTOR | 0.8 | # A pop with welfare income has its wealth multiplied by 1 - ( the fraction of their income that is welfare * this ) to ensure buildings don't start wage dumping just because all employees are getting welfare |
| BUILDING_WAGES_OWNERSHIP_BUILDING_FACTOR | 0.75 | # Buildings that own other buildings multiply their target wages by this to ensure profitability |
| BUILDING_WAGES_MIN_RELEVANT_POP_SIZE | 50 | # Pops with less workforce than this are ignored when checking whether a profitable building should raise wages because of radicalizing workers |
| BUILDING_WAGES_MIN_EMPLOYEES_FOR_RELEVANT_POP_SIZE_CHECK | 200 | # For the BUILDING_WAGES_MIN_RELEVANT_POP_SIZE to be checked, the buildings must have at least this many employees to avoid small buildings wage dumping |
| BUILDING_RAISE_WAGES_TARGET_WEALTH_MULT | 0.9 | # Buildings will consider raising wages if any significant pops working in them have this or lower * the target wealth to expected SoL ratio |
| BUILDING_LOWER_WAGES_TARGET_WEALTH_MULT | 1.2 | # Buildings will consider lowering wages if all significant pops working in them have this or higher * the target wealth to expected SoL ratio |
| BUILDING_WAGES_AVERAGE_PRODUCTIVITY_THRESHOLD | 0.5 | # At which ratio to average productivity does BUILDING_WAGES_AVERAGE_PRODUCTIVITY_FACTOR start kicking in (average tends to be high due to ownership buildings & trade centers, so this value should be fairly low) |
| BUILDING_WAGES_AVERAGE_PRODUCTIVITY_FACTOR | 0.5 | # How much more generous will buildings with high productivity compared to average for the building type be about wages, so long as they are turning an OK profit |
| BUILDING_WAGES_AVERAGE_PRODUCTIVITY_FACTOR_MAX | 2.5 | # Beyond this ratio of productivity compared to average, the effects of BUILDING_WAGES_AVERAGE_PRODUCTIVITY_FACTOR will be capped |
| BUILDING_PREFER_LAYOFFS_TARGET_WEALTH_MULT | 0.66 | # Buildings will prefer laying off pops if any significant pops working in them have this * the target wealth to expected SoL ratio or below |
| BUILDING_FOREIGN_OWNERSHIP_WAGE_FACTOR | -0.25 | # Buildings with foreign owners will have their wage targets adjusted by this amount (multiplied by foreign owned fraction), as the owners are less likely to care about radicals generated by low wages |
| BUILDING_DEFAULT_MIN_EARNINGS_TO_HIRE_EMPLOYEES | 3 | # Non-subsidized buildings will not hire if it would result in their annual earnings/employee falling below this threshold (default value, can be overridden for building group) |
| BUILDING_PROFIT_TARGET_TO_RAISE_WAGES | 0.25 | # Required profit margin to consider raising wages towards expected minimum, with BUILDING_WEEKS_BETWEEN_PAY_RAISES weeks cooldown |
| BUILDING_PROFIT_TARGET_TO_LOWER_WAGES | 0.15 | # If profit margin is this or below, buildings should lower their wages, with BUILDING_WEEKS_BETWEEN_PAY_CHANGES weeks cooldown |
| BUILDING_PROFIT_TARGET_TO_WITHDRAW_CASH | 0.15 | # If profit margin is this or below, buildings should withdraw money from the cash reserves to make up the difference |
| BUILDING_PROFIT_TARGET_TO_HIRE_EMPLOYEES | 0.25 | # If profit margin is this or above, buildings should try to hire new workers |
| OWNERSHIP_BUILDING_PROFIT_TARGET_TO_RAISE_WAGES | 0.5 | # Overrides BUILDING_PROFIT_TARGET_TO_RAISE_WAGES for buildings that own other buildings |
| OWNERSHIP_BUILDING_PROFIT_TARGET_TO_LOWER_WAGES | 0.3 | # Overrides BUILDING_PROFIT_TARGET_TO_LOWER_WAGES for buildings that own other buildings |
| OWNERSHIP_BUILDING_PROFIT_TARGET_TO_WITHDRAW_CASH | 0.3 | # Overrides BUILDING_PROFIT_TARGET_TO_WITHDRAW_CASH for buildings that own other buildings |
| OWNERSHIP_BUILDING_PROFIT_TARGET_TO_HIRE_EMPLOYEES | 0.5 | # Overrides BUILDING_PROFIT_TARGET_TO_HIRE_EMPLOYEES for buildings that own other buildings |
| SUBSISTENCE_BUILDING_PROFIT_TARGET_TO_RAISE_WAGES | 0.7 | # Overrides BUILDING_PROFIT_TARGET_TO_RAISE_WAGES for subsistence buildings |
| SUBSISTENCE_BUILDING_PROFIT_TARGET_TO_LOWER_WAGES | 0.5 | # Overrides BUILDING_PROFIT_TARGET_TO_LOWER_WAGES for subsistence buildings |
| SUBSISTENCE_BUILDING_PROFIT_TARGET_TO_WITHDRAW_CASH | 0.5 | # Overrides BUILDING_PROFIT_TARGET_TO_WITHDRAW_CASH for subsistence buildings |
| BUILDING_MAX_EMPLOYMENT_FRACTION_TO_RAISE_WAGES | 0.5 | # If the employment fraction of a building is above this, don't raise wages just to try and snipe employees from other buildings |
| BUILDING_WEEKS_BETWEEN_PAY_CHANGES | 0 | # Cooldown between changes in pay, so buildings don't overcompensate for a temporary change in circumstances. If the building is unprofitable it uses BUILDING_WEEKS_BETWEEN_PAY_CHANGES_WHEN_UNPROFITABLE instead. |
| BUILDING_WEEKS_BETWEEN_PAY_CHANGES_WHEN_UNPROFITABLE | 0 | # Cooldown between changes in pay, so buildings don't overcompensate for a temporary change in circumstances. Only used when unprofitable. |
| MIN_RAISE_TO_HIRE | 0.10 | # The minimum required increase in wages for an employee to switch jobs (1.0 = +100% = x2) |
| MIN_JOB_ATTRACTIVENESS | 0.10 | # Job attractiveness cannot be lower than this from stacking modifiers |
| BASE_RESOURCE_DISCOVER_CHANCE | 0.02 | # Per day (1.0 = 1%) |
| EMPLOYMENT_RESOURCE_DEPLETE_CHANCE | 0.005 | # Multiplied by number of fully employed levels of the building |
| RESOURCE_DISCOVER_MIN_FRACTION | 0.2 | # Min fraction of resources that will be discovered for each successful roll |
| RESOURCE_DISCOVER_MAX_FRACTION | 0.5 | # Max fraction of resources that will be discovered for each successful roll |
| FULLY_DISCOVERED_RESOURCE_DEPLETE_CHANCE_MULT | 1.0 | # The chance of a resource depleting is multiplied by this when all of the resource has been discovered |
| RESOURCE_DEPLETE_MIN_AMOUNT | 2 | # Min amount of resources that will be depleted for each successful roll |
| RESOURCE_DEPLETE_MAX_AMOUNT | 5 | # Max amount of resources that will be depleted for each successful roll |
| QUALITY_OF_LIFE_MIN | 1 |  |
| QUALITY_OF_LIFE_MAX | 100 |  |
| SUBSISTENCE_OUTPUT_AVERAGE_WAGE_RATE_FACTOR | 150 | # Each 1.0 of subsistence output counts as this much wage rate when setting normal wages |
| PEASANT_STARTING_WAGE_RATE_FACTOR | 1.0 | # For the sake of calculating starting normal wages, treat peasants as having this pop type wage multiplier |
| STARTING_WAGE_RATE_MULTIPLIER | 1.0 | # Starting wage rate is multiplied by this (for easy balancing) |
| STARTING_WAGE_RATE_SUBSISTENCE_MULTIPLIER | 0.5 | # STARTING_WAGE_RATE_MULTIPLIER is further multiplied by this for subsistence buildings |
| NORMAL_WAGE_RATE_FALLBACK | 500.0 | # If it's impossible to compute a normal wage rate (e.g. if every incorporated pop works in government buildings) set it to this (weekly £ per POP_SIZE_PACKAGE employees) |
| MINIMUM_WAGE_RATE | 10.0 | # The wage rate can never drop below this, no matter what (weekly £ per POP_SIZE_PACKAGE employees) |
| MAXIMUM_WAGE_RATE | 100000.0 | # The absolute maximum that a building's wage rate can be increased to. |
| CREDIT_RATIO_HEALTH_THRESHOLD | 0.5 | # If the principal is smaller than this ratio of the total credit, the economy is considered to be healthy |
| GOLD_RESERVE_MIN | 1000 | # If Gold Reserves are computed to be lower than this, it's instead set to this |
| GOLD_RESERVE_LIMIT_FACTOR | 0.2 | # The base factor of annual GDP that should be provided as a Gold Reserve |
| GOLD_RESERVE_RETURNS_FACTOR | 1 | # How rapidly diminishing returns will cause gold reserves to drop off after the limit has been reached (higher value increases penalty) |
| RETOOLING_WEEKS | 0 | # How long it takes for a building to get back up to full production after switching a production method |
| BUILDING_TIMED_MODIFIER_WEEKS | 52 | # Duration of a timed modifier which is applied after switching a production method |
| BUILDING_PAUSE_HIRES_CASH_RESERVES_THRESHOLD | 0.75 | # If cash reserves are higher than this, and employment fraction is below BUILDING_MAX_EMPLOYMENT_FRACTION_TO_CONSIDER_CASH_RESERVES, then allow hiring even if profits are low |
| BUILDING_MIN_EMPLOYMENT_FRACTION_TO_PAUSE_HIRES | 0.1 | # If building has at least this employment, it's OK to pause hiring |
| BUILDING_MAX_EMPLOYMENT_FRACTION_TO_CONSIDER_CASH_RESERVES | 0.5 | # If a building has at least this employment fraction, then ignore the cash reserves override for hiring |
| BUILDING_MAX_PROFIT_TO_PAUSE_HIRES | 0.2 | # If building is making less than this fraction of revenue in profit, it's OK to pause hiring |
| PRICE_REPORT_MAX_ENTRIES | 10 |  |
| NUM_COIN_ICONS | 13 |  |
| COIN_ICON_PRICE_COMPARISON_STEP | 0.12 |  |
| NUM_PROFITABILITY_ICONS | 13 |  |
| PROFITABILITY_ICON_COMPARISON_STEP | 0.15 |  |
| EARNINGS_RATIO_HIGH_THRESHOLD | 1.5 | # Buildings whose productivity exceeds this factor of the average will be considered high-productivity buildings |
| EARNINGS_RATIO_LOW_THRESHOLD | 0.66 | # Buildings whose productivity is below this factor of the average will be considered low-productivity buildings |
| EARNINGS_ABSOLUTE_HIGH_THRESHOLD | 30 | # Buildings whose productivity exceeds this amount will ALWAYS be considered high-productivity buildings |
| EARNINGS_ABSOLUTE_LOW_THRESHOLD | 3 | # Buildings whose productivity is below this amount will ALWAYS be considered low-productivity buildings |
| SLAVE_BASKET_DEFAULT | 8 | # Default level of consumer goods that a building will buy for its slaves |
| SLAVE_BASKET_MIN | 1 | # Min level of consumer goods that a building will buy for its slaves (the highest of this and SLAVE_BASKET_SCALED_MIN is used) |
| SLAVE_BASKET_MAX | 12 | # Max level of consumer goods that a building will buy for its slaves (the lowest of this and SLAVE_BASKET_SCALED_MAX is used) |
| SLAVE_BASKET_SCALED_MIN | 0.5 | # Multiplied by lowest non-slave wealth in the building |
| SLAVE_BASKET_SCALED_MAX | 1 | # Multiplied by lowest non-slave wealth in the building |
| SLAVE_BASKET_SUBSISTENCE_GOODS_MULT | 0.05 | # Goods consumed for slaves in subsistence buildings are multiplied by this |
| COLONIAL_SLAVERY_ENSLAVEMENT_RATE | 0.005 | # Under colonial slavery up to this much of a state's populace can be enslaved for their debts each week |
| COLONIAL_SLAVERY_ENSLAVEMENT_RATE_PER_POP | 0.15 | # No more than this fraction of a single pop can be enslaved each week |
| COLONIAL_SLAVERY_ENSLAVEMENT_RATE_DROP_OFF_PER_WEALTH | 0.01 | # Each point of wealth reduces max enslavement rate on a pop by this |
| COLONIAL_SLAVERY_MAX_STATE_SLAVE_FRACTION | 0.25 | # If more than this % of a state's population are slaves, do not enslave any more pops under colonial slavery |
| COLONIAL_SLAVERY_ACCEPTANCE_THRESHOLD | 60 | # Pops with this or more acceptance in their state do not get enslaved under colonial slavery |
| DEBT_SLAVERY_ENSLAVEMENT_RATE | 0.005 | # Under debt slavery up to this much of a state's populace can be enslaved for their debts each week |
| DEBT_SLAVERY_ENSLAVEMENT_RATE_PER_POP | 0.1 | # No more than this fraction of a single pop can be enslaved each week |
| DEBT_SLAVERY_ENSLAVEMENT_RATE_DROP_OFF_PER_WEALTH | 0.01 | # Each point of wealth reduces max enslavement rate on a pop by this |
| DEBT_SLAVERY_MAX_STATE_SLAVE_FRACTION | 0.15 | # If more than this % of a state's population are slaves, do not enslave any more pops under debt slavery |
| SLAVE_TRADE_MIN_VACANCIES_NEEDED_TO_IMPORT | 500 | # There needs to be at least this many (non-subsistence) vacancies in buildings that can be filled by slaves in order for slave import to happen |
| SLAVE_TRADE_MIN_POPULATION_TO_EXPORT | 100000 | # There needs to be at least this many people in the state in order for it to be selected, or remain valid, as a slave import target |
| SLAVE_TRADE_FULL_EXPORT_POPULATION_THRESHOLD | 250000 | # Below this amount of state population, the number of slaves exported is reduced by a multiplier scaled against SLAVE_TRADE_MIN_POPULATION_TO_EXPORT (at the halfway point between the two numbers the multiplier is 0.5x, etc) |
| SLAVE_TRADE_POPULATION_FRACTION_WEIGHT | 100 | # Weight of slave population ratio in slave import marker selection |
| SLAVE_TRADE_POPULATION_TOTAL_WEIGHT | 0.0002 | # Weight of total population in slave import marker selection |
| SLAVE_TRADE_TURMOIL_WEIGHT | 25 | # Weight of slave turmoil in slave import marker selection |
| SLAVE_TRADE_DISTANCE_WEIGHT | 1 | # Inverse weight (penalty) for distance in slave import marker selection |
| SLAVE_TRADE_OTHER_STATES_WEIGHT | 2 | # Inverse weight (penalty) for having other slave import markers |
| SLAVE_TRADE_EXISTING_STATE_CULTURE_WEIGHT_MULT | 10 | # Total score of state is multiplied by this if importing from states whose homeland cultures are already present in this state |
| SLAVE_TRADE_NUMBER_EVALUATED_STATES | 10 | # Slave import marker is selected randomly from this many potential targets with highest weight |
| SLAVE_TRADE_BASE_SLAVES_PER_WEEK | 100 | # Base number of slaves that will be traded per marker per week |
| SLAVE_TRADE_ARABLE_LAND_EFFECT | 1 | # Slaves traded per week is increased by this for each arable land in the importing state |
| SLAVE_TRADE_ARABLE_LAND_EFFECT_MAX | 200 | # Maximum that arable land can increase slaves traded per week |
| SLAVE_TRADE_RANDOM_MIN | 0.5 | # Slaves traded per week is multiplied by a random number, minimum of this |
| SLAVE_TRADE_RANDOM_MAX | 1.5 | # Slaves traded per week is multiplied by a random number, maximum of this |
| SLAVE_TRADE_MIN_MARKET_ACCESS | 0.1 | # Minimum market access multiplier for slave trade, i.e. even at a marker with 0 market access, this fraction of the base number will be traded |
| BUILDING_FAILED_HIRE_COOLDOWN_WEEKS_WITHOUT_WAGE_RAISE | 4 | # If a building fails to hire, it waits this many weeks before trying again *unless* it has since raised wages or adjusted its hiring rate |
| BUILDING_LAYOFFS_DECREASE_BY | 0.05 | # The ratio that layoffs will reduce employment by (e.g. 0.15 means if you're currently 57% employed, reduce that to 48.45%) |
| BUILDING_LAYOFF_HIRING_COOLDOWN_WEEKS | 4 | # If a building does layoffs, don't hire anymore workers for at least this amount of weeks |
| BUILDING_MINIMUM_HIRING_ADJUSTMENT_FRACTION | 0.001 | # If a hiring or firing wouldn't result in at least this amount of the wanted employees being transfered, don't bother |
| BUILDING_CASH_RESERVES_HIGH_ROI | 0.25 | # A ROI (return on investment) at or above this value is considered "high". In this context ROI means how much more money a building makes compared to how much it spends. Must be >= BUILDING_CASH_RESERVES_MED_ROI. |
| BUILDING_CASH_RESERVES_MED_ROI | 0.15 | # A ROI (return on investment) at exactly this value is considered "medium". In this context ROI means how much more money a building makes compared to how much it spends. Must be >= BUILDING_CASH_RESERVES_LOW_ROI. |
| BUILDING_CASH_RESERVES_LOW_ROI | 0.05 | # A ROI (return on investment) at or below this value is considered "low". In this context ROI means how much more money a building makes compared to how much it spends. Must be > 0. |
| BUILDING_CASH_RESERVES_FILL_TIME_HIGH_ROI | 26 | # Base number of weeks to fill a building's cash reserves when ROI is high. Final number of weeks is directly interpolated if ROI is between medium and high. Must be > 0. |
| BUILDING_CASH_RESERVES_FILL_TIME_MED_ROI | 52 | # Base number of weeks to fill a building's cash reserves when ROI is medium. Must be > 0. |
| BUILDING_CASH_RESERVES_FILL_TIME_LOW_ROI | 78 | # Base number of weeks to fill a building's cash reserves when ROI is low. Final number of weeks is directly interpolated if ROI is between low and medium. Must be > 0. |
| BUILDING_CASH_RESERVES_MIN_DEPOSIT_PERCENT | 0.25 | # The minimum percentage of weekly profits that building owners will try to deposit into a building's cash reserves. Must be >= 0. |
| BUILDING_CASH_RESERVES_MAX_DEPOSIT_PERCENT | 0.50 | # The maximum percentace of weekly profits that building owners will try to deposit into a building's cash reserves. Must be >= BUILDING_CASH_RESERVES_MIN_DEPOSIT_PERCENT |
| OWNERSHIP_BUILDING_CASH_RESERVES_MIN_DEPOSIT_PERCENT | 0.125 | # Replaces BUILDING_CASH_RESERVES_MIN_DEPOSIT_PERCENT for buildings that own other buildings |
| OWNERSHIP_BUILDING_CASH_RESERVES_MAX_DEPOSIT_PERCENT | 0.25 | # Replaces BUILDING_CASH_RESERVES_MAX_DEPOSIT_PERCENT for buildings that own other buildings |
| BUILDING_HIGH_CASH_RESERVES_THRESHOLD | 0.5 | # If cash reserves are above this fraction of max, buildings won't try to reduce expenses even if they are losing money |
| EMPLOYMENT_DIVIDEND_ESTIMATE_MULT | 2.0 | # When deciding employment overestimate dividends since they vary a lot and we really dont want to move someone to a job without a dividend that then turns out worse |
| GOODS_DEFAULT_TRADE_QUANTITY | 10 | # Base quantity traded by trade centers if not otherwise specified in goods type |
| MIN_POPS_PER_PROFESSION | 3 | # A building can hire at least this many pops in a profession, even if it has fewer than this number of pops available |
| POPS_PER_PROFESSION_LOG_BASE | 10 | # The number of pops in a profession is calculated as logarithm of employees count with this base |
| ESTABLISH_COLONY_PROVIDE_PORT | yes | # If establishing a colony should build a port for coastal colonies in order to immediately connect them to the market. |
| ESTABLISH_COLONY_PORT_COST | 100000 | # How much money it costs to establish a coastal colony that builds a port |
| ESTABLISH_COLONY_PORT_LEVEL | 1 | # What level port you get when establishing a coastal colony |
| SHIPPING_LANE_MERCHANT_MARINE_COST_SCALING | 0.15 | # Added to shipping lane cost multiplier for each multiple of expected distance beyond the first |
| GOODS_DEFAULT_MERCHANT_MARINE_COST_MULTIPLIER | 1 | # The merchant marine cost of shipping a single unit of goods (can be overridden in defines) |
| OVERSEAS_INFRASTRUCTURE_MERCHANT_MARINE_COST_MULTIPLIER | 0.2 | # Merchant marine cost for each infrastructure usage in overseas state for port connection shipping lanes |
| MERCHANT_MARINE_GOODS_KEY | "merchant_marine" | # The goods key used for merchant marine demand |
| SUPPLY_NETWORK_SHORTAGE_THRESHOLD | 0.5 | # If merchant marine sell/buy ratio is lower than this, start applying supply network strength penalties |
| SUPPLY_NETWORK_SHORTAGE_INCREASE_SPEED | 0.1 | # Supply network shortage penalty increases by this fraction of the target each week |
| SUPPLY_NETWORK_SHORTAGE_DECREASE_SPEED | 0.1 | # Supply network shortage penalty decreases by this fraction of MAX each week |
| SUPPLY_NETWORK_SHORTAGE_PENALTY_MIN | 0.05 | # Minimum supply network shortage penalty when any shortage exists |
| SUPPLY_NETWORK_SHORTAGE_PENALTY_MAX | 0.5 | # Maximum supply network shortage penalty |
| DEFAULT_EXPORT_TARIFFS | low_tariffs | # The default export tariff level that is applied when nothing is set in history |
| DEFAULT_IMPORT_TARIFFS | low_tariffs | # The default import tariff level that is applied when nothing is set in history |
| TARIFF_LEVEL_COOLDOWN_GRACE_PERIOD_DAYS | 7 | # After changing a tariff level, it takes this many days before the cooldown activates (to give you a chance to change your mind) |
| TARIFF_LEVEL_COOLDOWN_MONTHS | 3 | # After changing a tariff level, you must wait this long to change it again |
| TARIFF_LEVEL_EFFECT_LOW | 0.25 | # The fraction of tariff rate applied at low level |
| TARIFF_LEVEL_EFFECT_HIGH | 0.5 | # The fraction of tariff rate applied at high level |
| TARIFF_LEVEL_EFFECT_MAXIMUM | 1.0 | # The fraction of tariff rate applied at maximum level |
| SUBVENTION_LEVEL_EFFECT_LOW | 0.25 | # The fraction of subvention rate applied at low level |
| SUBVENTION_LEVEL_EFFECT_HIGH | 0.5 | # The fraction of subvention rate applied at high level |
| SUBVENTION_LEVEL_EFFECT_MAXIMUM | 1.0 | # The fraction of subvention rate applied at maximum level |
| REINVESTMENT_SUBSISTENCE_FRACTION_REDUCTION | 0.5 | # Reinvestment from pops in ownership buildings is multiplied by ( 1 - this * the share of levels owned that are subsistence buildings ) |
| COMPANY_OVER_LIMIT_BONUS_PENALTY_MIN | 0.33 | # If the number of companies in the country exceeds the limit, all company bonuses get penalty. The penalty is scaled proportionally to the limit (exceeding the limit by 100% reduces bonuses by 100%) and the minimum value is this |
| COMPANY_PRODUCTIVITY_RATIO_HIGH_THRESHOLD | 1.25 | # Companies whose productivity exceeds this factor of the global average will be considered high-productivity companies |
| COMPANY_PRODUCTIVITY_RATIO_LOW_THRESHOLD | 0.75 | # Companies whose productivity is below this factor of the global average will be considered low-productivity companies |
| COMPANY_PRODUCTIVITY_ABSOLUTE_HIGH_THRESHOLD | 25 | # Companies whose productivity exceeds this amount will ALWAYS be considered high-productivity companies |
| COMPANY_PRODUCTIVITY_ABSOLUTE_LOW_THRESHOLD | 5 | # Companies whose productivity is below this amount will ALWAYS be considered low-productivity companies |
| COMPANY_PROSPERITY_MAX | 100 | # Company prosperity cannot be higher than this |
| COMPANY_PROSPERITY_BONUS_ACTIVATION_THRESHOLD | 100 | # At this amount of prosperity, a company will start providing its prosperity bonuses |
| COMPANY_PROSPERITY_BONUS_DEACTIVATION_THRESHOLD | 75 | # At this amount of prosperity, a company will stop providing its prosperity bonuses |
| COMPANY_PROSPERITY_PRODUCTIVITY_MULTIPLIER | 50 | # Companies gain this much target prosperity from productivity of buildings compared to global average (defined value is at exactly average) |
| COMPANY_PROSPERITY_PRODUCTIVITY_MAX | 100 | # Max target prosperity from productivity |
| COMPANY_PROSPERITY_EMPLOYED_LEVELS_MULTIPLIER | 1 | # Companies gain this much target prosperity from number of fully employed building levels |
| COMPANY_PROSPERITY_EMPLOYED_LEVELS_MAX | 50 | # Max target prosperity from fully employed building levels |
| COMPANY_PROSPERITY_POPULARITY_MULTIPLIER | 0.1 | # Companies gain this much target prosperity, scaled by the popularity of its executive |
| COMPANY_PROSPERITY_POPULARITY_MAX | 10 | # Max target prosperity from popularity |
| COMPANY_PROSPERITY_POPULARITY_MIN | 0 | # Min target prosperity from popularity |
| COMPANY_PROSPERITY_WEEKLY_INCREASE_BASE | 0.2 | # Base amount of prosperity increase towards target value each week |
| COMPANY_PROSPERITY_WEEKLY_INCREASE_SCALED | 0.04 | # Prosperity increase towards target value each week, for each fully employed building level the company has |
| COMPANY_PROSPERITY_WEEKLY_INCREASE_SCALED_MAX | 0.8 | # Max value for weekly prosperity increase from employed levels |
| COMPANY_PROSPERITY_WEEKLY_DECREASE_BASE | -1.0 | # Base amount of prosperity decrease towards target value each week |
| COMPANY_PROSPERITY_WEEKLY_DECREASE_SCALED | 0.02 | # Prosperity decrease towards target value each week, for each fully employed building level the company has |
| COMPANY_PROSPERITY_WEEKLY_DECREASE_SCALED_MAX | 0.8 | # Min value for weekly prosperity decrease from employed levels |
| COMPANY_COUNTRY_CONSTRUCTION_BONUS_MULT | 0.2 | # Multiplier for company countries |
| NATIONALIZATION_PER_LEVEL_COST | 500 | # How much it costs to nationalize one level of a building per construction point |
| PRIVATIZATION_PER_LEVEL_COST | 250 | # How much it costs to privatize one level of a building per construction point |
| MIN_FAKE_CONSTRUCTION_COST | 100 | # Min construction cost for the matters of nationalization and privatization |
| COMPANY_COUNT_OF_REGIONAL_HQ_TYPES | 3 | # Count of building types in state reserved for flavored companies |
| COMPANY_MINIMUM_LEVELS_PER_HQ | 5 | # Minimum building levels per HQ required to establish or maintain a company |
| BASE_REGIONAL_HQS | 1 | # Base level of regional HQs available to a company after granted investment charter |
| LEVELS_PER_REGIONAL_HQ | 50 | # How many levels company needs to aquire to get a new regional HQ |
| COMPANY_ON_ESTABLISH_COOLDOWN_MONTHS | 60 | # Cooldown in months after establishing a company before you can disband it |
| COMPANY_ON_DISBAND_COOLDOWN_MONTHS | 48 | # Cooldown in months after disbanding a company before you can re-establish it |
| BUILDING_LEVEL_BUREAUCRACY_COST | 1 | # Cost of owning one level of the goverment building |
| COLLECTIVIZATION_DEBT_RATIO | 0.5 | # Ratio of the country max debt can be used for collectivizing |
| MIN_COLLECTIVIZATION_BUDGET | 1000000 | # Min size of a collectivizing budget |
| DYNAMIC_INDUSTRY_CHARTER | no | # Do we want to use dynamic industry charter instead of scripted ones |
| COMPANY_INFLUENCE_LEVEL_STEPS | { 10 50 100 250 500 1000 1500 2500 5000 10000 } |  |
| COMPANY_CHARTER_AUTHORITY_COST | 100 | # Cost of establishing a company charter |
| # Currently only used in loc, not logic |  |  |
| HARVEST_CONDITION_MIN_INTENSITY | 0.0 | # Lowest intensity value a harvest condition can roll ( 0 <= this < max) |
| HARVEST_CONDITION_MAX_INTENSITY | 9.0 | # Highest intensity value a harvest condition can roll (min < this) |
| COMPANY_MONOPOLY_COOLDOWN_MONTHS | 60 | # Cooldown in months after establishing a companies monopoly before you can revoke its monopoly |
| COUNTRY_MONOPOLY_MAX_COUNT | 5 | # Maximum number of country monopolies a country can have |
| COUNTRY_MONOPOLY_AUTHORITY_COST | 100 | # Cost of establishing a country monopoly |
| WORLD_MARKET_MONOPOLY_MIN_SHARE | 0.5 | # For a market to be considered to have a world market monopoly, it has to control a greater share of exports than this |
| MONOPOLY_PRICE_IMPACT | 0.2 | # The price of a good is increased by this multiplier based on how much of its supply is considered to be under a monopoly |
| PRIVATIZATION_DISCOUNT_MONOPOLY | 0.2 | # The cost of privatizing a building is multiplied by this for companies with a monopoly on that building type |
| PRIVATIZATION_DISCOUNT_COMPANY_ONLY | 0.1 | # The cost of a company privatizing a building is multiplied by this when non company privatization is forbidden (cumulative with PRIVATIZATION_DISCOUNT_MONOPOLY) |
| PRESTIGE_GOODS_INPUT_THROUGHPUT_BONUS | 0.2 | # Bonus to throughput, scaled against proportion of input goods base value that is prestige goods |
| TOLL_RATE_NO_TOLLS | 0.0 | # Toll rate on No Tolls setting. Value is multiplied with goods value crossing a strait |
| TOLL_RATE_LOW_TOLLS | 0.10 | # Toll rate on Low Tolls setting. Value is multiplied with goods value crossing a strait |
| TOLL_RATE_MEDIUM_TOLLS | 0.20 | # Toll rate on Medium Tolls setting. Value is multiplied with goods value crossing a strait |
| TOLL_RATE_HIGH_TOLLS | 0.40 | # Toll rate on High Tolls setting. Value is multiplied with goods value crossing a strait |
| TOLL_RATE_MULTIPLIER_FULL_CONTROL | 2.0 | # Multiplie on the above value if a country controls both sides of a strait |
| STRAIT_FULL_CONTROL_TRADE_IMPORTANCE_MULT | 1.5 | # Multiplier on strait trade importance when the controller controls both sides of the strait |
| MAX_PIRATED_GOODS_PER_HUB | 0.25 | # Max % of goods that can be pirated in one Hub->Hub connection |
| PIRACY_SHIP_SPEED_TO_GOODS_RATIO | 0.003 | # The % of goods trade quantity that are stolen per speed of a ship. |
| PIRATED_GOODS_SALE_DISCOUNT | 0.5 | # How much % value goods we get when being sold and turned into income for the country |
| PIRACY_SELL_ORDERS_MIN_GOODS | 0.1 | # The total amount of a good pirated needs to be at least this much to add it to sell orders, otherwise it's 100% lost |

### Military

| Define | Default Value | Dev Comment |
|---|---|---|
| POWER_PROJECTION_DIVISOR | 1000 | # Average of Offense and Defense is multiplied by manpower and divided by this to determine a unit's power projection |
| INITIAL_MANPOWER_COST_MULTIPLIER | 10 | # there is an extra cost for training new recruits, compared to maintenence of said recruits |
| MANPOWER_DIVISOR | 10000 | # the strategic goods needed by soldiers are counted in sets of |
| ATTRITION_RISK_EXILED_ARMY_ADD | 0.2 | # Exiled formation has attrition risk increased by this |
| ATTRITION_RISK_ON_ENEMY_TERRITORY_ADD | 0.3 | # Exiled formation on enemy territory has attrition risk additionally increased by this |
| MANPOWER_LOST_DUE_TO_ATTRITION_PER_WEEK_MIN | 0.04 | # The minimum percentage of manpower a unit can lose each week due to attrition |
| MANPOWER_LOST_DUE_TO_ATTRITION_PER_WEEK_MAX | 0.12 | # The maximum percentage of manpower a unit can lose each week due to attrition |
| ATTRITION_RECOVERY_RATE_BASE | 0.7 | # Base recovery rate for units not participating in battles affected by attrition, e.g. casualties with 0.7 recovery rate would consist of 70% wounded and 30% deaths |
| ATTRITION_RECOVERY_RATE_RANDOM_RANGE | 0.1 | # Randomness range for recovery rate for units not participating in battles affected by attrition |
| MIN_VARIABLE_DISTRIBUTION_PER_POP | 0 |  |
| MAX_VARIABLE_DISTRIBUTION_PER_POP | 100 |  |
| BATTLE_LETHALITY_MIN | 0.001 |  |
| BATTLE_LETHALITY_MAX | 0.005 |  |
| BATTLE_RAW_MANPOWER_INFLICTED_CASUALTY_RATIO | 0.5 | # applied to the number of casualties caused by raw number of troops, ie without considering Offense/Defense - increasing this makes CE less important and battles more lethal |
| BATTLE_COMBAT_EFFICIENCY_INFLICTED_CASUALTY_RATIO | 1.5 | # applied to the number of casualties caused by troops with Offense/Defense also factored in - increasing this makes CE more important and battles more lethal |
| BATTLE_MAX_CASUALTY_DISADVANTAGE_PENALTY | 1.0 | # a limit for the battle_casualties_disadvantage static modifier. 1.0 means a maximum of 100% penalty is applied. |
| MAX_CE_ADVANTAGE | 1 |  |
| MIN_MANPOWER_CASUALTY_PER_ROUND | 5 | # Minimum manpower losses per round |
| MIN_USABLE_MANPOWER | 100 | # Lowest manpower engaged in a battle limit (otherwise determined by combat width) |
| COMBAT_UNITS_PER_LEVEL | 1 | # Number of combat units each level of military building can support. Must be the same for all recruitable buildings (barracks/conscription centers) |
| BASE_MORALE_RECOVERED_PER_DAY | 0.03 | # Default morale recovered is 3% per day |
|  |  | # Travel related |
| COMMANDER_TRAVEL_PIXELS_TO_DAYS_SCALE | 0.045 | # Used to convert a travel distance from pixels to days. Example: a travel of 500px becomes 500 * 0.05 = 25 days |
| COMMANDER_TRAVEL_MIN | 3 | # Minimum travel time for commander to reach their new formation |
| COMMANDER_TRAVEL_MAX | 50 | # Limits the travel time to GENERAL_TRAVEL_MAX days. |
| EMBARKATION_MAX_DOCKED_FLEET_TRAVEL_DAYS | 30 | # If the army's travel to a docked fleet's port exceeds this many days, search for a closer coastal state instead |
| FORMATION_TRAVEL_NETWORK_SPEED | 15 | # (Temp) base speed of formations when they travel via the travel network |
| EMPTY_FLEET_MOVEMENT_SPEED | 100 | # Movement speed of fleets with no ships, so they can still be moved |
| BATTLE_PLAN_ADVANCE_PROGRESS_TO_LAUNCH | 100 | # required accumulated advance progress to launch |
| BATTLE_BASE_MIN_PROVINCES_TAKEN | 4 |  |
| BATTLE_BASE_MAX_PROVINCES_TAKEN | 12 |  |
| BATTLE_PROVINCES_TAKEN_FRONT_PROVINCES_NUM_DIVISOR | 5 | # Attacker takes (num provinces in front) divided by this as extra, clamped to BATTLE_BASE_MIN_PROVINCES_TAKEN and BATTLE_BASE_MAX_PROVINCES_TAKEN |
| BATTLE_PROVINCES_TAKEN_THEATER_PROVINCES_NUM_DIVISOR | 50 | # Attacker takes (num provinces in theater) divided by this as extra, clamped to BATTLE_BASE_MIN_PROVINCES_TAKEN and BATTLE_BASE_MAX_PROVINCES_TAKEN |
| BATTLE_PROVINCES_TAKEN_ATTACKING_UNIT_SCALE | 0.02 | # Multiply provinces taken by ( 1 + this * number of attacking units left at end of battle) |
| BATTLE_PROVINCES_TAKEN_MAX_DEPTH_MIN | 2 | # Maximum distance from battle provinces that provinces can be taken by attacker (minimum) |
| BATTLE_PROVINCES_TAKEN_MAX_DEPTH_MAX | 10 | # Maximum distance from battle provinces that provinces can be taken (maximum) |
| BATTLE_PROVINCES_TAKEN_MAX_DEPTH_FRONT_PROVINCES_NUM_DIVISOR | 50 | # Num provinces in front is divided by this and added to maximum depth attacker can take provinces at |
| BATTLE_PROVINCES_TAKEN_MAX_DEPTH_THEATER_PROVINCES_NUM_DIVISOR | 500 | # Num provinces in theater is divided by this and added to maximum depth attacker can take provinces at |
| DEFENSIVE_PROVINCES_RETAKEN_MAX_DEPTH | 1 | # Maximum distance from battle provinces that provinces can be retaken in defensive battle |
| BATTLE_PROVINCES_TAKEN_THEATER_UNIT_SCALE | 2 | # Scales number of provinces captured by theater-provinces / ( units-in-theater * this-define ) |
| BATTLE_PROVINCES_TAKEN_MAX_EXTRA | 3 | # If the selected provinces will cause split, capture the new theater as long as it has up to BATTLE_PROVINCES_TAKEN_MAX_EXTRA provinces. This might not respect the distance limit (BATTLE_PROVINCES_TAKEN_MAX_DEPTH). |
| BATTLE_PROVINCES_TAKEN_THEATER_MIN_SCALE | 0.01 | # Number of provinces captured cannot result in a lower scaling factor than this due to BATTLE_PROVINCES_TAKEN_THEATER_UNIT_SCALE |
| BATTLE_PROVINCES_TAKEN_ABSOLUTE_MIN | 1 | # The absolute least number of provinces that can be captured in a successful advance, after all scaling has been applied |
| CONVOY_RAIDING_STRENGTH_MULT | 0.3 | # How strong each Convoy raiding point is |
| CONVOY_RAIDING_COOLDOWN_DAYS_MIN | 10 | # Min days until the next convoy raiding in the sea node |
| CONVOY_RAIDING_COOLDOWN_DAYS_MAX | 30 | # Max days until the next convoy raiding in the sea node |
| CONVOY_RAIDING_DAMAGE_MIN_RANDOM_FACTOR | 0.5 | # Actual convoy raiding damage is scaled between CONVOY_RAIDING_DAMAGE_MIN_RANDOM_FACTOR and CONVOY_RAIDING_DAMAGE_MAX_RANDOM_FACTOR to provide some random variability |
| CONVOY_RAIDING_DAMAGE_MAX_RANDOM_FACTOR | 1.0 | # Actual convoy raiding damage is scaled between CONVOY_RAIDING_DAMAGE_MIN_RANDOM_FACTOR and CONVOY_RAIDING_DAMAGE_MAX_RANDOM_FACTOR to provide some random variability |
| CONVOY_RAIDING_DEFENSE_MULT | 0.15 | # How much is Convoy raiding strength reduced by patrolling ships ( num ships * ce defense ) |
| CONVOY_RAIDING_MAX_DEFENSE | 0.90 | # Example: the defender can never block more than 90% of the convoy damage they're currently taking |
|  |  | # Convoy recovery rate after being raided is based on a global and a local rate, using whichever is lower |
| CONVOY_RAIDING_GLOBAL_RECOVERY_RATE | 0.001 | # The rate at which damaged convoys are replaced each day, relative to total number of produced convoys in the raided country |
| CONVOY_RAIDING_LOCAL_RECOVERY_RATE | 0.01 | # The rate at which damaged convoys are replaced each day, relative to total number of convoys passing through the sea node |
| CONVOY_RAIDING_RECOVERY_RATE_PEACETIME_FACTOR | 4 | # While a country is at peace, convoys will be restored this much faster |
| MIN_OFFENSE_DEFENSE | 1 | # The absolute lowest Offense or Defense a unit can have |
| INTERCEPTION_DELAY_BASE_DAYS | 5 | # atleast this many days between each admiral interception attempt |
| INTERCEPTION_DELAY_MAX_RANDOM_DAYS_FACTOR | 10 | # up to this many extra days between each admiral interception attempt |
| INTERCEPTION_BASE_CHANCE | 0.1 | # base chance when trying to intercept enemy admirals |
| DEMOBILIZATION_TIME_DAYS | 90 | # Number of days it takes to fully demobilize after a formation has returned home |
| MOBILIZATION_INFRASTRUCTURE_FACTOR | 0.01 | # amount of mobilization generated per point of infrastructure. one battalion takes one full point of mobilization to mobilize |
| MIN_MOBILIZATION_PER_DAY | 0.05 | # minimum mobilization gained per day by each mobilizing battalion (the last unit to gain mobilization in a state might have to do with whatever is left) |
| MAX_MOBILIZATION_PER_DAY | 0.20 | # maximum mobilization gained per day by each mobilizing battalion |
| FRONT_MARKER_ADVANTAGE_PREDICTION_MIN_COMBAT_POWER | 0.01 | # Used as a minimum value when calculating the Front Advantage |
| BATTLE_CONDITION_MIN_TICKS_BETWEEN_UPDATE_DEFAULT | 40 | # Unless otherwise specified on the battle condition type, battle conditions will not update until at least this many ticks has passed |
| BATTLE_CONDITION_CHANCE_TO_UPDATE_PER_EXTRA_TICK | 0.01 | # For each tick that has passed since the minimum number of ticks, this chance to refresh battle conditions (i.e. 13 ticks after min, there's 13% chance of switching) |
| DEFAULT_ORDER | "advance" | # Default order for generals |
| MILITARY_FORMATION_COMMAND_LIMIT_NO_COMMANDER | 20 | # Default command limit if formation has no commander |
| LOW_COMMAND_LIMIT_GRACE_PERIOD_DAYS | 30 | # How many days will it take for a formation whose units exceeds its command limit to start suffering penalties |
| INVALID_NAVAL_MISSION_GRACE_PERIOD_DAYS | 10 | # How many days a fleet with an invalid naval mission will wait before going back to port |
| FORMATION_AUTO_MERGE_GRACE_PERIOD_DAYS | 3 | # Only auto-merge units into formations created within this many days |
| COMMANDER_SUFFICIENT_CAPACITY_MULT | 1.5 | # Commanders of a type are considered sufficient if their cumulative command limit is at least this times the total active combat units of that type |
| UNNECESSARY_PROMOTION_PENALTY_YEARS | 5 | # Duration in years of the interest group approval penalty for unnecessary promotions |
| UNNECESSARY_PROMOTION_ARMED_FORCES_IG | "ig_armed_forces" | # Used to identify the armed forces IG, who are always upset by unnecessary promotions |
| RECENTLY_PROMOTED_YEARS | 5 | # Duration in years of the loyalty bonus for recently promoted commanders |
| MILITARY_FORMATION_ORGANIZATION_MIN | 0 | # The minimum amount of Organization a Military Formation will always retain despite exceeding their Command Limit |
| MILITARY_FORMATION_ORGANIZATION_MAX | 100 | # The maximum amount of Organization a Military Formation requires to be considered at full Organization |
| MILITARY_FORMATION_ORGANIZATION_LOSS_RATE | 0.05 | # The percentage of current Organization a Military Formation can lose in a day |
| MILITARY_FORMATION_ORGANIZATION_LOSS_MIN | 1 | # The minimum amount of Organization a Military Formation can lose in a day |
| MILITARY_FORMATION_ORGANIZATION_GAIN_MIN | 0.1 | # The minimum amount of Organization a Military Formation can gain in a day |
| MILITARY_FORMATION_ORGANIZATION_SPECIAL_UNITS_ADD | -50 | # Military Formation with too many special units gain this Organization penalty: Target = Target + ( excess ratio * this ) |
| MILITARY_FORMATION_ORGANIZATION_EXILE_MULT | -1 | # Exiled Military Formation has its Target Organization modified: Target = Target * ( 1 + this ) |
| MILITARY_FORMATION_ORGANIZATION_SUPPLY_SHORTAGE_EFFECT_THRESHOLD | 0.25 | # Organization penalty starts when supply drops below this ratio |
| MILITARY_FORMATION_SHORTAGE_BATTALION_ORG_WEIGHT | 0.25 | # Organization-target weight of a battalion whose required goods are fully in shortage (1 = no penalty); interpolated by the battalion's goods shortage severity |
| MILITARY_FROMATION_MAX_RESUPPLY_RATIO_PER_WEEK | 0.1 | # Each week, a military formation can resupply this fraction of its total supply need |
| MILITARY_FORMATION_MIN_RESUPPLY_PER_WEEK | 10 | # Each week, a military formation can resupply at least this amount of its supply need |
| MOBILIZATION_OPTION_DIFFERENCE_ORGANIZATION_IMPACT | 20 | # The penalty to Organization gained for each difference by merging units between Formations with different Mobilization Options |
| FLEET_PRESENCE_GAIN_PER_DAY | 0.02 | # The amount of Presence a Fleet gains per day while in Mission Area |
| FLEET_PRESENCE_DECAY_PER_DAY | 0.02 | # The amount of Presence a Fleet decays per day while not in Mission Area |
| FLEET_PRESENCE_TRANSPORTING_OR_INVADING | 1.0 | # Sea Presence forced on fleets transporting armies or supporting a naval invasion |
| FLEET_GUARANTEED_BATTLE_SIZE | 0.5 | # It's guaranteed that half of the ships arrive regardless of sea presence |
| FLEET_SPOT_BASE_CHANCE | 0.00005 | # Base chance to spot an enemy fleet, multiplied by the spotter's average Detection and the target's average Visibility |
| FLEET_SPOT_SCALING_MULTIPLIER | 0.01 | # Scaling factor multiplier per total ship count when spotting a fleet |
| MILITARY_FORMATION_WEEKLY_MAX_UNIT_UPGRADES_ARMY | 0.1 | # Each week a mobilized army can upgrade this (0.0-1.0) fraction of its total number of units. |
| MILITARY_FORMATION_WEEKLY_MAX_UNIT_UPGRADES_FLEET | 0.05 | # Each week a mobilized fleet can upgrade this (0.0-1.0) fraction of its total number of units. |
| MANPOWER_RATIO_REQUIRED_TO_CLEAR_DEFEATED_ADMIRALS | 0.75 | # A Defeated fleet without at least this ratio of current/max manpower will remain Defeated |
| MILITARY_FORMATION_AUTO_DEPLOY_DISTANCE_LIMIT | 250 | # Armies are not auto-deployed to fronts that are located further than this pixel-distance from the army's current position |
| BASECAMP_WANTED_FORMATIONS_SCORE | 1.0 | # The more formations we need to add to the basecamp the higher the score |
| BASECAMP_DISTANCE_SCORE_THRESHOLD | 100 | # Is multiplied with penalties below and then is subtracted from the basecamp score |
| BASECAMP_DISTANCE_PENALTY | 0.4 | # The further basecamp is from the formation the lower the score |
| BASECAMP_DISTANCE_TO_HOME_HQ_PENALTY | 0.2 | # The further basecamp is from the formation's home HQ the lower the score |
| BASECAMP_OWN_COUNTRY_SCORE | 0.2 | # Is added to the basecamp score if its state belongs to the formation's country |
| BASECAMP_STRATEGIC_OBJECT_SCORE | 1.1 | # Is added to the basecamp score if it's near a strategic objective |
| BASECAMP_NUM_PROVINCES_SCORE | 0.05 | # The more provinces around basecamp the higher the score |
| # Defines below control how much blockade strength is required to fully blockade a state # The base target strength is equal to the state_blockade_resistance_add modifier |  |  |
| BLOCKADE_TARGET_STRENGTH_MAXIMUM | 100000 | # Required blockade strength cannot be higher than this |
| BLOCKADE_TARGET_STRENGTH_PER_TRADED_UNIT | 0.1 | # Each base value of imports/exports in the market area increases required blockade strength by this (only for world market hubs) |
| BLOCKADE_TARGET_STRENGTH_PER_PRODUCED_UNIT | 0.15 | # Each base value of goods produced in buildings affected by blockades (such as fisheries and shipyards) increases required blockade strength by this |
| BLOCKADE_TARGET_STRENGTH_PER_MERCHANT_MARINE | 3 | # Each convoy passing through the state's port increases required blockade strength by this |
| BLOCKADE_WORLD_MARKET_ACCESS_IMPACT_SCALING | 0.75 | # Reduction of world market access for blockaded world market hubs, scales against blockade level |
| BLOCKADE_SHIPPING_LANE_IMPACT_SCALING | 0.75 | # Reduction of efficiency for blockaded shipping lanes, scales against blockade level of either start or end point, whichever is most blockaded |
| BLOCKADE_THROUGHPUT_IMPACT_SCALING | 0.75 | # Reduction of throughput for buildings affected by blockades, scales against blockade level |
| BLOCKADE_SEA_PRESENCE_TRESHOLD | 0.5 | # At what level of sea presence is the blockade effective |
| BLOCKADE_FORCED_BATTLE_LEVEL = 1.0 # A fleet undocking from a state with at least this blockade level will be forced into a battle with the blockading fleet |  |  |
|  |  | # Defines below control port bombardment effects on enemy coastal states |
| BOMBARDMENT_DEVASTATION_MAX | 25.0 | # Maximum devastation that can be generated by port bombardment |
| BOMBARDMENT_DEVASTATION_RATE | 0.20 | # Per day devastation increase, scales with effective bombardment level |
| BOMBARDMENT_BUILDING_DAMAGE_BASE_CHANCE | 0.02 | # Base daily chance to reduce the level of a random coastal building, scales with effective bombardment level |
| BOMBARDMENT_SEA_PRESENCE_THRESHOLD | 0.1 | # At what level of sea presence is the port bombardment effective |
| OFFICERS_TO_SERVICEMEN_RATIO_THRESHOLD | 0.75 | # If the officer to servicemen ratio falls below this percentage from its ideal ratio for a building, the combat units provided by that building will start applying the effectiveness factor defined below. A threshold value means the effectiveness factor kicks in in later (when lacking more officers) [>= 0 and <= 1] |
| OFFICERS_TO_SERVICEMEN_RATIO_EFFECTIVENESS_FACTOR_MIN | -0.5 | # The effectiveness factor to offense and defense applied to units provided by a building that completely lacks officers. -1 means -100%. Total offense and defence cannot drop below MIN_OFFENSE_DEFENCE. [>= -1 and <= 0] |
| OFFICERS_TO_SERVICEMEN_RATIO_EFFECTIVENESS_FACTOR_MAX | 0 | # The effectiveness factor to offense and defense applied to units provided by a building that doesn't lack any officer. 0 means -0%, therefore units supplied by buildings that don't lack officers will fight at their full effectiveness allowed by their circumstances [>= OFFICERS_TO_SERVICEMEN_RATIO_EFFECTIVENESS_FACTOR_MIN and <= 0] |
| SAILORS_PER_ASSIGNMENT_SLOT | 100 | # The number of sailors per ship assignment slot on Naval Administration buildings |
| SAILORS_PER_BUILDING_LEVEL | 1000 | # The number of sailors per building level of Naval Administration |
| ACTIVE_SHIP_LIVING_CREW_PERCENTAGE | 0.1 | # If a ship has this percentage of living crew or less, it is rendered inactive |
| DESTROYED_SHIP_LIVING_CREW_PERCENTAGE | 0 | # If a ship has this percentage of living crew or less, it is destroyed while not in port |
| MINIMUM_SHIP_CREW_PERCENTAGE_TO_DEPLOY | 0.1 | # A fleet cannot be deployed while any of its ships has less than this percentage of living crew, and at-sea fleets with such ships are sent home to re-crew |
| SHIP_PARTICIPATE_IN_UPRISING_CREW_PERCENTAGE | 0.33 | # If at least this ratio of a ship's crew is from a rebelling state, the ship can participate in an uprising |
| SHIP_MAINTENANCE_SHIPYARD_PREMIUM_FACTOR | 0.2 # The profit margin shipyards get on maintenance costs (GoodsCost * (1 + this)) |  |
| SHIP_MAINTENANCE_GOODS_TO_CONSTRUCTION_GOODS_FACTOR | 0.002 | # The ratio of maintenance goods cost to construction goods cost for ships. Used to determine how many goods are needed for maintenance paid by shipyards |
| SHIP_UPKEEP_GOODS_TO_CONSTRUCTION_GOODS_FACTOR | 0.002 | # The ratio of upkeep goods cost to construction goods cost for ships. Used to determine how many goods are needed for upkeep based on how many were needed for construction |
| SHIP_UPKEEP_GOODS_DOCKED_MULT | -0.8 | # If the ship is docked, its upkeep goods cost is changed by this mult value |
| SHIP_CONSTRUCTION_COST_MODIFICATION_LEVEL_FACTOR | 1.05 | # The construction cost of a ship is multiplied by this^(total modification levels) |
| SHIP_TEMPLATE_DEFAULT_MODIFICATION_LEVEL | 2 | # Default modification level per slot used to calculate the default level cost for ship goods balancing |
| LOGISTICS_CENTER_SUPPLY_PER_LEVEL | 10 | # Spawn a new level of logistics center for each this much base supply consumption from formations using this state as a supply hub |
| SUPPLY_SHIP_TYPE | "ship_type_supply_ship" # What ship type is code-side treated as the supply ship type. Changing this will very likely break things |  |
| SUPPLY_SHIP_MAINTENANCE_COST_PER_SHIP | 1 | # Weekly maintenance cost per supply ship |
| SHIP_CONSTRUCTION_MAINTENANCE_FRACTION | 0.0003 | # Fraction of a ship's total construction cost consumed weekly as construction point maintenance |
| SHIP_CONSTRUCTION_MAINTENANCE_PENALTY_THRESHOLD | 0.5 | # Fulfillment ratio at or below which the maintenance penalty reaches 100% |
| SHIP_CONSTRUCTION_MAINTENANCE_MAX_HP_PENALTY_FRACTION | 0.05 | # Max fraction of a ship's total HP lost per week at full maintenance penalty |
| SHIP_CONSTRUCTION_MAINTENANCE_DAMAGE_RATIO | 0.2 | # Fraction of ships randomly selected to receive maintenance damage each week (0-1) |
| SUPPLY_SHIP_CONSTRUCTION_MAINTENANCE_FRACTION | 0.0003 | # Fraction of supply ship construction cost consumed weekly as construction point maintenance |
| SUPPLY_SHIP_MAINTENANCE_STOCKPILE_REMOVAL_FRACTION | 0.05 | # Max fraction of supply ships removed per week at full maintenance penalty |
| FLEET_RESUPPLY_SURPLUS | 0.25 | # How much above the maintenance rate (where delivered supply equals consumed supply) will a fleet get supplied when attempting to increase it's supply level |
| ARMY_RESUPPLY_SURPLUS | 0.25 | # How much above the maintenance rate (where delivered supply equals consumed supply) will an army get supplied when attempting to increase it's supply level |
| FLEET_SUPPLY_REPLENISH_SHIP_MULT | 1.1 | # How much more supply ships requested by fleets when under max supply stockpile |
| SHIP_POWER_PROJECTION_HULL_DAMAGE_MULTIPLIER | 0.33 | # The multiplier applied to a ship's hull damage in calculating its power projection |
| SHIP_POWER_PROJECTION_CREW_DAMAGE_MULTIPLIER | 0.33 | # The multiplier applied to a ship's crew damage in calculating its power projection |
| SHIP_POWER_PROJECTION_ARMOR_MULTIPLIER | 0.33 | # The multiplier applied to a ship's armor in calculating its power projection |
| SHIP_POWER_PROJECTION_HIT_POINTS_MULTIPLIER | 0.1 | # The multiplier applied to a ship's max hit points in calculating its power projection |
| SHIP_CREW_STARTING_VETERANCY_EXPERIENCE | 0 | # The amount of experience crew for a ship starts with when recruited |
| SHIP_MAX_VETERANCY_EXPERIENCE | 1000 | # Experience cap for a ship. Should be higher than the highest veterancy level experience threshold. |
| SHIP_VETERANCY_EXPERIENCE_DECAY_RATE | 0.01 | # Percentage of experience lost per week when not on a mission. |
| SHIP_VETERANCY_EXPERIENCE_MIN_DECAY | 1 | # Minimum amount of experience lost per week due to decay (if decay applies), regardless of current experience |
| SHIP_VETERANCY_BASE_EXPERIENCE_GAIN_BATTLE_VICTORY | 5 | # Base experience gain for a ship that was in a battle that was won by its side. |
| SHIP_VETERANCY_BASE_EXPERIENCE_GAIN_BATTLE_DEFEAT | 2 | # Base experience gain for a ship that was in a battle that was lost by its side. |
| SHIP_VETERANCY_BASE_EXPERIENCE_GAIN_BATTLE_SUNK_ENEMY_SHIP | 1 | # Base experience gain for a ship for each ship it has sunk in battle. |
| SHIP_COMBAT_POWER_HULL_DAMAGE_MULTIPLIER | 0.75 | # The multiplier applied to a ship's hull damage in calculating its combat power |
| SHIP_COMBAT_POWER_CREW_DAMAGE_MULTIPLIER | 0.25 | # The multiplier applied to a ship's crew damage in calculating its combat power |
| SHIP_COMBAT_POWER_SPEED_MULTIPLIER | 3.0 | # The multiplier applied to a ship's speed in calculating its combat power |
| COMBAT_UNIT_GROUP_MARINES_GROUP | "combat_unit_group_marines" # Marines type |  |
| FLAGSHIP_CHANGE_COOLDOWN_MONTHS | 60 | # After changing flagship, you have to wait this many months before changing it again |
| FLAGSHIP_ON_WON_FAIR_COMBAT_POWER_RATIO_THRESHOLD | 0.5 | # The ratio between the combat power of the opposing side and the flagship's side needs to be at least this for on_flagship_battle_won to trigger |
| NAVAL_MISSION_SUPPLY_COST_FACTOR_SCALING | 0.1 | # Additional supply cost (percent, 0-1) incurred per sea region beyond the first in a naval mission |
| NAVAL_MISSION_BASE_MAX_SEA_REGIONS | 2 | # Base max number of sea regions that can be assigned to a fleet mission (before modifiers) |
| NAVAL_MISSION_TYPE_INTERCEPT | "naval_mission_type_intercept" |  |
| NAVAL_MISSION_TYPE_PROJECT_POWER | "naval_mission_type_project_power" |  |
| FRIENDLY_PORT_MAX_SUPPLY_DISTANCE_DISCOUNT | 0.5 | # Maximum supply distance discount (0-1) when a formation is near a friendly port |
| FRIENDLY_PORT_MAX_DISTANCE | 2500 | # Travel network distance at which the friendly port discount reaches zero |
| AI_FIND_FLEET_EXPECTED_DISTANCE | 25000 | # Expected map distance for normalizing fleet-to-army distance scoring |
| DEFAULT_ARMY_COLOR | "army_color_6" |  |
| DEFAULT_FLEET_COLOR | "fleet_color_8" |  |

### Diplomacy

| Define | Default Value | Dev Comment |
|---|---|---|
| DEFAULT_DIPLOMATIC_PLAY | "dp_default_treaty_article" |  |
| DEFAULT_WAR_GOAL_IS_HUMILIATION | yes | # If this is false, default war goal is instead money transfer |
| DEFAULT_TRUCE_MONTHS | 60 |  |
| PEACE_DEAL_DURATION_IN_DAYS | 30 |  |
| PEACE_DEAL_COOLDOWN_IN_DAYS | 120 |  |
| PACT_REQUIRES_APPROVAL_MIN_FORCED_MONTHS | 12 | # Diplomatic pacts that require approval always have at least this cooldown period before they can be broken |
| OBLIGATION_FORCED_PACT_MONTHS | 120 |  |
| SWAY_FORCED_PACT_MONTHS | 120 |  |
| EXPEL_DIPLOMATS_MONTHS | 60 |  |
| OBLIGATION_MONTHS | 120 |  |
| RECENTLY_CONQUERED_DURATION_MONTHS | 120 |  |
| RECENTLY_LIBERATED_DURATION_MONTHS | 120 |  |
| DIPLOMATIC_DEMAND_PENDING_APPROVAL_DAYS | 14 | # Number of days before a demand is auto-declined and a diplomatic play starts |
| DIPLOMATIC_DEMAND_TIMEOUT_DAYS | 14 | # Number of days before an accepted or rejected demand is deleted |
| DIPLOMATIC_ACTION_COOLDOWN_DAYS | 0 | # Number of days you must wait between diplomatic actions/proposals |
| DIPLOMATIC_ACTION_PENDING_APPROVAL_DAYS | 30 | # Number of days before a pending action is auto-declined |
| TREATY_PROPOSAL_PENDING_APPROVAL_DAYS | 30 | # Number of days before a pending treaty proposal is auto-declined |
| DIPLOMATIC_PACT_COST_DEFAULT | 0 | # The default maintenance in Influence for a pact |
| DIPLOMATIC_PACT_COST_MULT_FROM_INFAMOUS | 0.25 | # Maintenance cost of a pact is increased by this when at Infamous level of infamy |
| DIPLOMATIC_PACT_COST_MULT_FROM_NOTORIOUS | 0.50 | # Maintenance cost of a pact is increased by this when at Notorious level of infamy |
| DIPLOMATIC_PACT_COST_MULT_FROM_PARIAH | 1.00 | # Maintenance cost of a pact is increased by this when at Pariah level of infamy |
| DIPLOMATIC_PACT_COST_LOBBY_CLOUT_MULT | 0.01 | # Each point of clout from pro/anti-country lobbies reduces or increases the influence cost multiplier of maintaining pacts with them by this amount, depending on whether the pact matches their goals |
| DIPLOMATIC_PACT_COST_LOBBY_CLOUT_MAX | 0.5 | # Cost multiplier impact of pro/anti-country lobbies cannot be greater than this |
| TREATY_ARTICLE_COST_LOBBY_CLOUT_MULT | 0.01 | # Each point of clout from pro/anti-country lobbies reduces or increases the influence cost multiplier of maintaining treaty articles with them by this amount |
| TREATY_ARTICLE_COST_LOBBY_CLOUT_MAX | 0.5 | # Cost multiplier impact of pro/anti-country lobbies cannot be greater than this |
| RIVALRY_BASE_SCALING | 0.25 | # Rivalry always gives at least this amount of influence scaling |
| RIVALRY_SCALING_PER_INTEREST_LEVEL | 0.25 | # Rivalry gives this amount of influence scaling for each overlapping interest level |
| RIVALRY_MAX_SCALING | 2.0 | # Rivalry influence scaling cannot exceed this number |
| RIVALRY_LOWER_RANK_SCALING_MULT | 0.5 |  |
| RIVALRY_SCALING_LOBBY_CLOUT_MULT | 0.01 | # Each point of clout from pro/anti-country lobbies reduces or increases the influence gain from rivalry by this amount (anti increases, pro decreases) |
| RIVALRY_SCALING_LOBBY_CLOUT_MAX | 0.5 | # Rivalry influence multiplier impact of pro/anti-country lobbies cannot be greater than this |
| MIN_RELATIONS | -100 |  |
| MAX_RELATIONS | 100 |  |
| START_RELATIONS | 0 |  |
| RELATIONS_THRESHOLD_FRIENDLY | 80 |  |
| RELATIONS_THRESHOLD_AMICABLE | 50 |  |
| RELATIONS_THRESHOLD_CORDIAL | 20 |  |
| RELATIONS_THRESHOLD_POOR | -20 |  |
| RELATIONS_THRESHOLD_COLD | -50 |  |
| RELATIONS_THRESHOLD_HOSTILE | -80 |  |
| REQUIRED_IMPROVE_RELATIONS_PROGRESS | 100 | # How much change relations progress is needed to increase relations by 1 point |
| REQUIRED_DAMAGE_RELATIONS_PROGRESS | -100 | # How much change relations progress is needed to decrease relations by 1 point |
| INITIAL_LIBERTY_DESIRE | 50 | # Liberty Desire value which the Diplomatic Pact gets initialized to. |
| WEEKLY_LIBERTY_DESIRE_FROM_SUPPORT_INDEPENDENCE_TOTAL_MAX | 0.5 | # Maximum weekly increase in liberty desire from all Support Independence targeting the country |
| MIN_INFAMY | 0 | # Infamy can't be lower than this |
| MAX_INFAMY | 1000 | # Infamy can't be higher than this |
| START_INFAMY | 0 | # This is the default amount of infamy countries start with |
| INFAMY_THRESHOLD_INFAMOUS | 25 | # Above this, countries are considered infamous and get related penalties |
| INFAMY_THRESHOLD_NOTORIOUS | 50 | # Above this, countries are considered notorious and get related penalties |
| INFAMY_THRESHOLD_PARIAH | 100 | # Above this, countries are considered pariah and get related penalties |
| BASE_YEARLY_INFAMY_DECAY_RATE | 5.0 | # Decay rate of infamy per year |
|  |  | # Tension is used instead of relations by colonizable countries |
| MIN_TENSION | 0 |  |
| MAX_TENSION | 100 |  |
| START_TENSION | 0 |  |
| TENSION_THRESHOLD_UNEASY | 25 |  |
| TENSION_THRESHOLD_TENSE | 50 |  |
| TENSION_THRESHOLD_VOLATILE | 75 |  |
| TENSION_DECAY_RATE | 5 | # Per year |
| TENSION_INCREASE_MIN | 2.5 | # Tension increases by a min of this when a province is colonized |
| TENSION_INCREASE_MAX | 20.00 | # Tension increases by a max of this when a province is colonized |
| TENSION_NUM_PROVINCE_SCALING_BASE | 10 | # Below this amount of provinces a decentralized country gets additional tension when their provinces are colonized |
| TENSION_NUM_PROVINCE_SCALING_RATE | 2.0 | # Max multiplier increase in tension per province taken from having only a few provinces |
| TENSION_INCREASE_RATE_ADJACENT | 0.5 | # Multiplied to tension increase when it is neighboring countries' provinces that are colonized |
| TENSION_UPRISING_CHANCE | 0.02 | # Chance of war breaking out instead of the next province being colonized (base when tension is at least TENSION_THRESHOLD_VOLATILE) |
| SWAY_OFFER_TIMEOUT_DAYS | 14 |  |
| SWAY_OFFER_REJECTED_COOLDOWN_DAYS | 7 | # Must wait this many days before trying to sway a country that rejected your previous sway |
| SWAY_OFFER_CALL_IN_OBLIGATION_MANEUVERS_COST | 10 |  |
| SWAY_OFFER_OWE_OBLIGATION_MANEUVERS_COST | 10 |  |
| SWAY_OFFER_CALL_ALLY_MANEUVERS_COST | 20 |  |
| SWAY_OFFER_TRANSFER_STATE_MANEUVERS_COST | 10 |  |
| SWAY_OFFER_TRANSFER_SUBJECT_MANEUVERS_COST | 10 |  |
| SWAY_OFFER_BECOME_SUBJECT_MANEUVERS_COST | 5 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_JOIN_POWER_BLOC | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_LEAVE_POWER_BLOC | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_COLONIZATION_RIGHTS | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_FORCE_NATIONALIZATION | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_HUMILIATION | 20 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_UNIFICATION_LEADERSHIP | 30 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_OPEN_MARKET | 20 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_REGIME_CHANGE | 8 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_ANNEX_COUNTRY | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_LIBERATE_COUNTRY | 30 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_MAKE_PROTECTORATE | 8 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_REDUCE_AUTONOMY | 5 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_INCREASE_AUTONOMY | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_MAKE_TRIBUTARY | 8 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_MAKE_DOMINION | 8 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_CONQUER_STATE | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_RETURN_STATE | 10 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_REVOKE_CLAIM | 5 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_REVOKE_ALL_CLAIMS | 0 | # Can't be added, only for special plays |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_CONTAIN_THREAT | 1000 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_TRANSFER_SUBJECT | 8 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_LIBERATE_SUBJECT | 20 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_UNIFICATION | 100 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_INDEPENDENCE | 20 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_SECESSION | 100 |  |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_POPULATION_SCALING_FACTOR | 10000 | # The amount of population by which the factor below is multiplied |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_POPULATION_SCALING_MULTIPLIER | 0.03 | # For each SWAY_OFFER_WARGOAL_MANEUVERS_COST_POPULATION_SCALING_FACTOR population in a country/state, multiply maneuvers cost by this |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_POPULATION_SCALING_MULTIPLIER_MAX_PER_STATE | 2.5 | # Maneuvers population multiplier can't be higher than this for each state affected |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_POPULATION_SCALING_MULTIPLIER_MAX_TOTAL | 5 | # Maneuvers population multiplier can't be higher than this, regardless of number of states affected |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_HOMELAND_FACTOR | -0.25 | # Maneuvers cost is adjusted by this if the states taken/puppeted etc are Homelands of the aggressor |
| SWAY_OFFER_WARGOAL_MANEUVERS_COST_UNINCORPORATED_FACTOR | -0.5 | # Maneuvers cost is adjusted by this if the states taken/puppeted etc are unincorporated |
| MAKE_WARGOAL_PRIMARY_DEMAND_MANEUVERS_COST | 0.5 | # Fraction of the wargoal's base maneuver cost that it costs to turn it into a primary demand |
| MAKE_WARGOAL_PRIMARY_DEMAND_INFAMY_AMOUNT | 0.5 | # Fraction of the wargoal's base infamy that is accured when you turn it into a primary demand |
| ALLY_WARGOAL_MAX_MANEUVERS_COST | 25 | # When an ally adds a 'free' wargoal in a play, it cannot have a maneuvers cost higher than this |
| PERSONAL_UNION_ACTION_NAME | "personal_union" |  |
| INCREASE_AUTONOMY_OF_SELF_NAME | "da_increase_autonomy_of_self" |  |
| INCREASE_AUTONOMY_OF_SUBJECT_ACTION_NAME | "da_increase_autonomy_of_subject" |  |
| DECREASE_AUTONOMY_OF_SUBJECT_ACTION_NAME | "da_decrease_autonomy" |  |
| WAR_GOAL_TRANSFER_SUBJECT_TYPE | "transfer_subject" |  |
| WAR_GOAL_UNIFICATION_TYPE | "unification" |  |
| WAR_GOAL_CONTAIN_THREAT_TYPE | "contain_threat" |  |
| WAR_GOAL_INDEPENDENCE_TYPE | "independence" |  |
| WAR_GOAL_HUMILIATION_TYPE | "humiliation" |  |
| WAR_GOAL_ENFORCE_TREATY_ARTICLE_TYPE | "enforce_treaty_article" |  |
| WAR_GOAL_CONQUER_STATE_TYPE | "conquer_state" |  |
| WAR_GOAL_REVOKE_ALL_CLAIMS_TYPE | "revoke_all_claims" |  |
| WAR_GOAL_RETURN_STATE_TYPE | "return_state" |  |
| WAR_GOAL_OPEN_MARKET_TYPE | "open_market" |  |
| WAR_GOAL_FOREIGN_INVESTMENT_RIGHTS_TYPE | "foreign_investment_rights" |  |
| WAR_GOAL_JOIN_POWER_BLOC_TYPE | "join_power_bloc" |  |
| WAR_GOAL_REPARATIONS_MONTHS | 60 | # [>= 0] |
| WAR_GOAL_COLONIZATION_RIGHTS_PACT_TYPE | "colonization_rights" |  |
| WAR_GOAL_COLONIZATION_RIGHTS_MONTHS | 60 | # [>= 0] |
| WAR_GOAL_OPEN_MARKET_MONTHS | 60 | # [>= 0] |
| WAR_GOAL_HUMILIATION_PACT_TYPE | "humiliation" |  |
| WAR_GOAL_HUMILIATION_MONTHS | 60 | # [>= 0] |
| WAR_GOAL_CONTAIN_THREAT_MONTHS | 60 | # [>= 0] |
| WAR_GOAL_MAKE_PROTECTORATE_SUBJECT_TYPE | "subject_type_protectorate" |  |
| WAR_GOAL_MAKE_TRIBUTARY_SUBJECT_TYPE | "subject_type_tributary" |  |
| WAR_GOAL_MAKE_DOMINION_SUBJECT_TYPE | "subject_type_dominion" |  |
| WAR_GOAL_TREATY_PORT_BUILDING_LEVEL | 1 |  |
| WAR_GOAL_LIBERATE_COUNTRY_LIBERATOR_START_RELATIONS | 50 |  |
| WAR_GOAL_LIBERATE_COUNTRY_OPPRESSOR_START_RELATIONS | -50 |  |
| WAR_GOAL_CONTAIN_THREAT_YEARS_SINCE_CONQUEST | 10 |  |
| WAR_GOAL_REGIME_CHANGE_MONTHS | 60 | # Government in country with forced regime change is locked in for this number of months [>= 0] |
| WAR_GOAL_REGIME_CHANGE_MAX_IDEOLOGICAL_OPINION | -5 | # If ideological opinion is above this, regime change can't be used |
| WAR_GOAL_REGIME_CHANGE_MIN_LAW_PROGRESSIVENESS_DIFFERENCE | 50 | # If the difference between the target wargoal holder's laws in a law group are not at least this, don't change it as part of regime change |
| WAR_GOAL_INCREASE_AUTONOMY_MIN_LIBERTY_DESIRE | 75 | # A subject must have at least this much LD to use the increase autonomy wargoal |
| WAR_GOAL_INDEPENDENCE_MIN_LIBERTY_DESIRE | 90 | # A subject must have at least this much LD to use the independence wargoal |
| WAR_GOAL_INFAMY_POPULATION_SCALING_FACTOR | 10000 | # The amount of population by which the factor below is multiplied |
| WAR_GOAL_INFAMY_POPULATION_SCALING_MULTIPLIER | 0.03 | # For each WAR_GOAL_INFAMY_POPULATION_SCALING_FACTOR population in a country/state, multiply infamy by this |
| WAR_GOAL_INFAMY_POPULATION_SCALING_MULTIPLIER_MAX_PER_STATE | 5 | # Infamy population multiplier can't be higher than this for each state affected |
| WAR_GOAL_INFAMY_POPULATION_SCALING_MULTIPLIER_MAX_TOTAL | 50 | # Infamy population multiplier can't be higher than this, regardless of number of states affected |
| WAR_GOAL_INFAMY_HOMELAND_FACTOR | -0.25 | # Infamy is adjusted by this if the states taken/puppeted etc are Homelands of the aggressor |
| WAR_GOAL_INFAMY_UNINCORPORATED_FACTOR | -0.5 | # Infamy is adjusted by this if the states taken/puppeted etc are unincorporated |
| WAR_GOAL_INFAMY_REBELLING_SUBJECT_MULT | 0.25 | # Infamy is multiplied by this for wargoals targeting a rebellious subject |
| WAR_GOAL_INFAMY_LOW_LIBERTY_DESIRE_SUBJECT_MULT | 0.25 | # Infamy is multiplied by this for wargoals targeting a subject whose LD is below WAR_GOAL_INFAMY_LOW_LIBERTY_DESIRE_THRESHOLD |
| WAR_GOAL_INFAMY_LOW_LIBERTY_DESIRE_THRESHOLD | 25 | # Threshold for WAR_GOAL_INFAMY_LOW_LIBERTY_DESIRE_SUBJECT_MULT |
| WAR_GOAL_INFAMY_RELATIONS_TARGET_IMPACT | -1 | # Each point of infamy generated by an incident also has this impact on relations with the target |
| WAR_GOAL_INFAMY_RELATIONS_INTEREST_IMPACT | -0.5 | # Each point of infamy generated by an incident also has this impact on relations with countries that have an interest in the target |
| WAR_GOAL_INFAMY_CONQUER_STATE | 5.0 |  |
| WAR_GOAL_INFAMY_RETURN_STATE | 2.0 |  |
| WAR_GOAL_INFAMY_MAKE_PROTECTORATE | 2.0 |  |
| WAR_GOAL_INFAMY_MAKE_TRIBUTARY | 2.0 |  |
| WAR_GOAL_INFAMY_MAKE_DOMINION | 2.0 |  |
| WAR_GOAL_INFAMY_REDUCE_AUTONOMY | 2.0 |  |
| WAR_GOAL_INFAMY_TRANSFER_SUBJECT | 2.0 |  |
| WAR_GOAL_INFAMY_ANNEX_COUNTRY | 5.0 |  |
| WAR_GOAL_INFAMY_REGIME_CHANGE | 0.5 |  |
| WAR_GOAL_INFAMY_FORCE_NATIONALIZATION | 5.0 |  |
| WAR_GOAL_INFAMY_DIPLO_PLAY_BACK_DOWN_REFUND | -0.75 | # Refund of infamy for war goals that are dropped due to one side backing down in a diplo play (applied to initiator/target) |
| WAR_GOAL_INFAMY_DIPLO_PLAY_BACKER_REFUND | -1.00 | # Refund of infamy for war goals that are dropped for backers in a diplo play (due to play not escalating to war or backer switching sides) |
| WAR_GOAL_INFAMY_PEACE_REFUND | -0.5 | # Refund of infamy for war goals that are dropped due to a country capitulating or negotating peace without enforcing their wargoal |
| WAR_GOAL_INFAMY_REDUCTION_FOR_TARGET | -0.5 | # This much of a war goal's infamy value is removed from the target when target has it enforced on them |
| WAR_OUTCOME_MIN_WARGOAL_IMPACT | 10 | # Minimum impact value for a wargoal when calculating war outcomes |
| WAR_OUTCOME_VICTORY_RATIO | 2.0 | # Below this ratio of enforced wargoal impact, a victory is considered to be limited. If ratio is above this but both sides still enforced wargoals, it's a victory. If one side enforced all its wargoals and the other side enforced none, it's a total victory. |
| WAR_OUTCOME_VICTORY_MIN_ENFORCEMENT_RATIO | 0.5 | # A side must enforce at least this fraction of their total wargoal impact to qualify for a victory, otherwise it is a limited victory |
| DIPLOMATIC_PLAY_ABANDON_SUPPORT_RELATIONS_IMPACT | 50 |  |
| DIPLOMATIC_PLAY_ESCALATION_DAILY | 1 |  |
| DIPLOMATIC_PLAY_ESCALATION_PAUSE_FROM_ACTION | 5 | # Number of days that escalation pauses when either side takes an action |
| DIPLOMATIC_PLAY_ESCALATION_PAUSE_MAX | 20 | # Escalation pause can't be longer than this no matter how many actions are taken at once |
| DIPLOMATIC_PLAY_OPENING_PHASE_END | 21 | # Before this, defender needs to set their wargoal and you can't join/sway |
| DIPLOMATIC_PLAY_CLOSING_PHASE_START | 80 | # After this, it isn't possible to join/sway further countries |
| DIPLOMATIC_PLAY_ESCALATION_WAR_BREAKOUT | 100 |  |
| COLONY_PROVINCE_BASE_SCORE | 10 |  |
| COLONY_PROVINCE_COASTAL_SCORE | 60 | # Replaces COLONY_BASE_SCORE for provinces with a coastline |
| COLONY_PROVINCE_ADJACENCY_SCORE | 25 | # How much will colonies prioritize adjacency to existing provinces when growing the colony |
| COLONY_PROVINCE_NO_ADJACENCY_MULT | 0.1 | # Multiply by this if no adjacencies at all |
| COLONY_PROVINCE_RANDOM_FACTOR | 1.5 | # The higher this is, the more random colonization province picking will be |
| BASE_WAR_SUPPORT | 100 |  |
| MAX_WAR_SUPPORT | 100 |  |
| MIN_WAR_SUPPORT | -100 |  |
| # Definitions for all the diplomatic catalysts that are called from code instead of script # If these are changed, they also need to be changed in the database and vice versa |  |  |
| DIPLOMATIC_CATALYST_TYPE_HISTORICAL_RELATIONS | "catalyst_historical_relationship" |  |
| DIPLOMATIC_CATALYST_TYPE_BECAME_RELEVANT | "catalyst_became_relevant" |  |
| DIPLOMATIC_CATALYST_TYPE_BECAME_IRRELEVANT | "catalyst_became_irrelevant" |  |
| DIPLOMATIC_CATALYST_TYPE_GAINED_LAND_BORDER | "catalyst_gained_land_border" |  |
| DIPLOMATIC_CATALYST_TYPE_LOST_LAND_BORDER | "catalyst_lost_land_border" |  |
| DIPLOMATIC_CATALYST_TYPE_MARKET_OPENED | "catalyst_market_opened" |  |
| DIPLOMATIC_CATALYST_TYPE_RELATIONS_INCREASED | "catalyst_relations_level_increased" |  |
| DIPLOMATIC_CATALYST_TYPE_RELATIONS_DECREASED | "catalyst_relations_level_decreased" |  |
| DIPLOMATIC_CATALYST_TYPE_DIPLOMATIC_DEMAND | "catalyst_diplomatic_demand" |  |
| DIPLOMATIC_CATALYST_TYPE_DIPLOMATIC_DEMAND_TARGET | "catalyst_diplomatic_demand_target" |  |
| DIPLOMATIC_CATALYST_TYPE_DIPLOMATIC_PLAY | "catalyst_diplomatic_play" |  |
| DIPLOMATIC_CATALYST_TYPE_DIPLOMATIC_PLAY_TARGET | "catalyst_diplomatic_play_target" |  |
| DIPLOMATIC_CATALYST_TYPE_AUTONOMY_INCREASED | "catalyst_autonomy_level_increased" |  |
| DIPLOMATIC_CATALYST_TYPE_AUTONOMY_DECREASED | "catalyst_autonomy_level_decreased" |  |
| DIPLOMATIC_CATALYST_TYPE_GAINED_INDEPENDENCE | "catalyst_gained_independence" |  |
| DIPLOMATIC_CATALYST_TYPE_BECAME_SUBJECT | "catalyst_became_subject" |  |
| DIPLOMATIC_CATALYST_TYPE_DIPLOMATIC_INCIDENT | "catalyst_diplomatic_incident" |  |
| DIPLOMATIC_CATALYST_TYPE_PACT_FORMED | "catalyst_pact_formed" |  |
| DIPLOMATIC_CATALYST_TYPE_PACT_BROKEN | "catalyst_pact_broken" |  |
| DIPLOMATIC_CATALYST_TYPE_ALLIANCE_FORMED | "catalyst_alliance_formed" |  |
| DIPLOMATIC_CATALYST_TYPE_ALLIANCE_BROKEN | "catalyst_alliance_broken" |  |
| DIPLOMATIC_CATALYST_TYPE_ALLIANCE_FORMED_WITH_RIVAL | "catalyst_alliance_with_rival" |  |
| DIPLOMATIC_CATALYST_TYPE_RIVAL_OF_RIVAL | "catalyst_rival_of_rival" |  |
| DIPLOMATIC_CATALYST_TYPE_INCREASED_RELATIONS_WITH_RIVAL | "catalyst_increased_relations_with_rival" |  |
| DIPLOMATIC_CATALYST_TYPE_DECREASED_RELATIONS_WITH_RIVAL | "catalyst_decreased_relations_with_rival" |  |
| DIPLOMATIC_CATALYST_TYPE_OPPOSED_IN_PLAY | "catalyst_opposed_in_play" |  |
| DIPLOMATIC_CATALYST_TYPE_ALLIES_IN_PLAY | "catalyst_allies_in_play" |  |
| DIPLOMATIC_CATALYST_TYPE_WARGOAL_ENFORCED | "catalyst_wargoal_enforced" |  |
| DIPLOMATIC_CATALYST_TYPE_STATE_CONQUERED | "catalyst_state_conquered" |  |
| DIPLOMATIC_CATALYST_TYPE_DIPLOMATIC_STRATEGY_CHANGED | "catalyst_diplomatic_strategy_changed" |  |
| DIPLOMATIC_CATALYST_TYPE_DECLARED_BANKRUPTCY | "catalyst_declared_bankruptcy" |  |
| DIPLOMATIC_CATALYST_TYPE_IDEOLOGICAL_DRIFT | "catalyst_ideological_drift" |  |
| DIPLOMATIC_CATALYST_TYPE_IDEOLOGICAL_ALIGNMENT | "catalyst_ideological_alignment" |  |
| DIPLOMATIC_CATALYST_TYPE_JOINED_SAME_BLOC | "catalyst_joined_same_bloc" |  |
| DIPLOMATIC_CATALYST_TYPE_JOINED_DIFFERENT_BLOC | "catalyst_joined_different_bloc" |  |
| DIPLOMATIC_CATALYST_TYPE_LEFT_POWER_BLOC | "catalyst_left_power_bloc" |  |
| DIPLOMATIC_CATALYST_TYPE_KICKED_OUT_OF_BLOC | "catalyst_kicked_out_of_bloc" |  |
| DIPLOMATIC_CATALYST_TYPE_JOURNAL_ENTRY | "catalyst_journal_entry" |  |
| DIPLOMATIC_CATALYST_TYPE_UNIFICATION_SUPPORT_ADDED | "catalyst_unification_support_added" |  |
| DIPLOMATIC_CATALYST_TYPE_UNIFICATION_SUPPORT_REMOVED | "catalyst_unification_support_removed" |  |
| DIPLOMATIC_CATALYST_TYPE_FRIENDLY_LOBBY_IN_GOVERNMENT | "catalyst_friendly_lobby_in_government" |  |
| DIPLOMATIC_CATALYST_TYPE_HOSTILE_LOBBY_IN_GOVERNMENT | "catalyst_hostile_lobby_in_government" |  |
| DIPLOMATIC_CATALYST_TYPE_NATIONALIZED_BUILDING | "catalyst_nationalized_building" |  |
| DIPLOMATIC_CATALYST_TYPE_OVERTAKEN_IN_PRESTIGE_RANK | "catalyst_overtaken_in_prestige_rank" |  |
| DIPLOMATIC_CATALYST_TYPE_REVOLUTION_SUCCESSFUL | "catalyst_revolution_successful" |  |
| DIPLOMATIC_CATALYST_TYPE_BECAME_RECOGNIZED | "catalyst_became_recognized" |  |
| DIPLOMATIC_CATALYST_TYPE_STRAIT_TOLL_HIGH = "catalyst_strait_toll_high" |  |  |
| DIPLOMATIC_CATALYST_TYPE_STRAIT_TOLL_REDUCED = "catalyst_strait_toll_reduced" |  |  |
| DIPLOMATIC_CATALYST_TYPE_STRAIT_NO_MILITARY = "catalyst_strait_no_military" |  |  |
| DIPLOMATIC_CATALYST_TYPE_STRAIT_CLOSED = "catalyst_strait_closed" |  |  |
| DIPLOMATIC_CATALYST_TYPE_STRAIT_OPENED = "catalyst_strait_opened" |  |  |
| DIPLOMATIC_CATALYST_TYPE_STRAIT_PARTIALLY_OPENED | "catalyst_strait_partially_opened" |  |
| DIPLOMATIC_CATALYST_MIN_SCORE_POSITION_FOR_OVERTAKE | 10 | # If country's prestige/rank score position isn't at least this, don't apply any 'overtaken in rank' catalysts to it |
| DIPLOMATIC_CATALYST_MIN_CHANGE_FOR_IDEOLOGICAL_DRIFT | -10 | # Ideological score change between previous and new government must be at least this high to create an ideological drift catalyst |
| DIPLOMATIC_CATALYST_MIN_CHANGE_FOR_IDEOLOGICAL_ALIGNMENT | 10 | # Ideological score change between previous and new government must be at least this high to create an ideological alignment catalyst |
| TOP_PRESTIGE_RANK_BONUS_THRESHOLD | 10 | # Prestige rank threshold at which the prestige_ranking_top static modifier starts being applied |
| TOP_PRESTIGE_RANK_BONUS_SCALE | 1.0 | # At prestige rank 1, the prestige_ranking_top modifier is applied with ( 1 + this multiplier ), scaling down to 1x at threshold |
| COUNTRY_TIER_CITY_STATE_PRESTIGE | 0 |  |
| COUNTRY_TIER_PRINCIPALITY_PRESTIGE | 5 |  |
| COUNTRY_TIER_GRAND_PRINCIPALITY_PRESTIGE | 10 |  |
| COUNTRY_TIER_KINGDOM_PRESTIGE | 15 |  |
| COUNTRY_TIER_EMPIRE_PRESTIGE | 25 |  |
| COUNTRY_TIER_HEGEMONY_PRESTIGE | 50 |  |
| PRESTIGE_FROM_COUNTRY_GDP_DIVISOR | 1000000 |  |
| PRESTIGE_FROM_COUNTRY_GDP | 3 | # Per PRESTIGE_FROM_COUNTRY_GDP_DIVISOR GDP |
| PRESTIGE_FROM_SUBJECT_GDP | 1.5 | # Per PRESTIGE_FROM_COUNTRY_GDP_DIVISOR GDP in subjects |
| PRESTIGE_FROM_ARMY_POWER_PROJECTION | 0.03 | # Per point of power projection from army combat power |
| PRESTIGE_FROM_NAVY_POWER_PROJECTION | 0.006 | # Per point of power projection from navy combat power |
| PRESTIGE_FROM_SUBJECT_ARMY_POWER_PROJECTION | 0.0005 | # Per point of power projection from army combat power in subjects |
| PRESTIGE_FROM_SUBJECT_NAVY_POWER_PROJECTION | 0.01 | # Per point of power projection from navy combat power in subjects |
| PRESTIGE_FROM_PRESTIGE_GOODS_PRODUCTION | 3 | # Multiplier on usual prestige from goods leaderboards |
| PRESTIGE_MIN_NUM_COUNTRIES | 100 | # If there's less countries using prestige than this in the game, we add some filler countries to adjust average prestige levels |
| FILLER_COUNTRY_PRESTIGE | 15 |  |
| DAYS_TO_LOSE_POWER_RANK | 365 |  |
| POWER_RANK_LOSS_THRESHOLD | 0.9 |  |
| ARMY_POWER_PROJECTION_MODIFIER_MAX_SCALING | 1000 | # Above this amount of army power projection, the country_army_power_projection static modifier provides no further benefit |
| NAVY_POWER_PROJECTION_MODIFIER_MAX_SCALING | 1000 | # Above this amount of army power projection, the country_navy_power_projection static modifier provides no further benefit |
| DEFAULT_STATES_REQUIRED_TO_RELEASE_COUNTRY | 0 | # Applied if nothing is specified in country_creation |
| DEFAULT_STATES_REQUIRED_TO_FORM_COUNTRY | 0.75 | # Applied if nothing is specified in country_formation |
| RELEASE_COUNTRY_AS_SUBJECT_RELATIONS_BOOST | 30 |  |
| RELEASE_COUNTRY_AS_INDEPENDENT_RELATIONS_BOOST | 50 |  |
| INTEREST_NUM_DAYS_CHANGE | 30 | INTEREST_MAX_INVOLVEMENT \|\| 10000 \|\| # Max involvement score for the interest tiers |
| INTEREST_GROWTH_RATIO | 0.02 | # Each week, an interest's current involvement value grows by this proportion of the difference between its current involvement and target involvement |
| INTEREST_MIN_GROWTH | 10 | # Each week, an interest's current involvement value grows by at least this much |
| INTEREST_DECAY_SPEED | 20 | # Each week, an interest's current involvement value decays by this amount |
| INTEREST_CAPITAL_TARGET_INVOLVEMENT | 2500 | # Target involvement score for having your capital in a strategic region |
| INTEREST_CAPITAL_NEIGHBOR_TARGET_INVOLVEMENT | 1500 | # Target involvement score for having your capital in a neighboring strategic region |
| INTEREST_STATE_OR_CLAIM_TARGET_INVOLVEMENT | 7500 | # Target involvement score for state or claim locality |
| INTEREST_STATE_OR_CLAIM_MIN_TARGET_INVOLVEMENT | 1500 | # Minimum target involvement guaranteed when having any ownership or claims in a region |
| INTEREST_CLAIM_LOCALITY_WEIGHT | 0.20 | # Each claim contributes this much locality weight (equivalent to owning this fraction of the whole state region) |
| INTEREST_GDP_TARGET_INVOLVEMENT | 2500 | # Target involvement score multiplier for GDP share in a region |
| INTEREST_ARMY_TARGET_INVOLVEMENT | 0.33 | # How much of army offense and defense is converted into target involvement for a present country |
| INTEREST_NAVY_TARGET_INVOLVEMENT | 0.33 | # How much of navy power projection is converted into target involvement for a present country |
| INTEREST_NAVY_MISSION_MULTI_REGION_BONUS | 0.75 | # Bonus to fleet involvement generation for each strategic region covered by a naval mission |
| INTEREST_MIN_INVOLVEMENT_RATIO | 0.1 | # Minimum ratio of the article and pacts max involvement per article type or diplomatic pact |
| REGION_LOCALITY_SHARE_THRESHOLD | 0.25 | # If you have at least this share of a region's locality, you get the local interest in the region |
| REGION_LOCALITY_COUNTRY_INCORPORATED_SHARE_THRESHOLD | 0.25 # If at least this share of your total incorporated states are in a region, you get the local interest in the region |  |
| INTEREST_TIER_MIN_RELEVANT_RANK | 2 | # Min rank of an interest tier to be considered relevant |
| INTEREST_TIER_MIN_VIOLATE_SOVEREIGNTY_RANK | 2 | # Min interest tier rank for a country to be an "interested party" for Violate Sovereignty (receive event to join defender). Use 2 for engaged or 3 for influential; |
| INTEREST_ARMY_INVOLVEMENT_CAP | 5000 | # Max involvement from army strength |
| INTEREST_NAVY_INVOLVEMENT_CAP | 5000 | # Max involvement from navy strength |
| INTEREST_TREATY_PACT_INVOLVEMENT_CAP | 5000 | # Max involvement from treaties and pacts |
| INTEREST_POWER_BLOC_MEMBER_TARGET_INVOLVEMENT | 2500 | # Involvement generated by each non-subject power bloc member for the leader |
| INTEREST_TIER_REDUCTION_GRACE_PERIOD_DAYS | 30 | # When a country increases its interest tier, this many days must pass before the tier can be reduced |
| STRAIT_MIN_INTEREST_TIER_FOR_CATALYST | 1 | # Minimum interest tier required for a country to get a catalyst from strait closing to military access |
| REGION_LOCALITY_STATES_WEIGHT | 1 | # Weight of the proportion of states you own in a region when calculating region locality |
| REGION_LOCALITY_POPULATION_WEIGHT | 1.25 | # Weight of the proportion of population you own in a region when calculating region locality |
| RELATION_PENALTY_OVERLORD_KICK_BACKER_SUBJECT | -30 | # When an overlord joins a diplomatic play they will force any subjects of theirs to become neutral if they are supporting the other side, this is a penalty to relations between the subject and overlord when that happens |
| ECONOMIC_DEPENDENCE_MIN | 0 |  |
| ECONOMIC_DEPENDENCE_MAX | 5 |  |
| ECONOMIC_DEPENDENCE_GDP_RATIO_BY_OTHER_FACTOR | 5 | # Ex. if you own 15% of the other country's GDP, that works out to +0.75 |
| ECONOMIC_DEPENDENCE_GDP_RATIO_BY_OTHER_MIN | 0 |  |
| ECONOMIC_DEPENDENCE_GDP_RATIO_BY_OTHER_MAX | 5 |  |
| ECONOMIC_DEPENDENCE_OTHER_GDP_RATIO_OWNED_FACTOR | 20 | #More embarrassing if your subjects own your stuff than the other way round |
| ECONOMIC_DEPENDENCE_OTHER_GDP_RATIO_OWNED_MIN | -5 | #This value is negative |
| ECONOMIC_DEPENDENCE_OTHER_GDP_RATIO_OWNED_MAX | 0 |  |
| ECONOMIC_DEPENDENCE_GDP_PERCENTAGE_FACTOR | 1 |  |
| ECONOMIC_DEPENDENCE_GDP_PERCENTAGE_MIN | 0 |  |
| ECONOMIC_DEPENDENCE_GDP_PERCENTAGE_MAX | 1 |  |
| ECONOMIC_DEPENDENCE_POP_GOODS_DEPENDENCE_ON_OTHER_FACTOR | 3 | # The total % of the £ value goods supplied by the other country compared to its GDP is multiplied by this (i.e. every multiple of 25% yields +0.75 ED) |
| ECONOMIC_DEPENDENCE_POP_GOODS_DEPENDENCE_ON_OTHER_MIN | 0 | # At best, a country's pop goods dependence on another can reach 0 |
| ECONOMIC_DEPENDENCE_POP_GOODS_DEPENDENCE_ON_OTHER_MAX | 2 | # At worst, a country's pop goods dependence on another can reach +2 |
| ECONOMIC_DEPENDENCE_OTHER_POP_GOODS_DEPENDENCE_FACTOR | 3 | # The total % of the £ value goods supplied by another country by this compared to their GDP is multiplied by this |
| ECONOMIC_DEPENDENCE_OTHER_POP_GOODS_DEPENDENCE_MIN | -2 | # At best, another country's pop goods dependence on this can yield -2 ED |
| ECONOMIC_DEPENDENCE_OTHER_POP_GOODS_DEPENDENCE_MAX | 0 | # At worst, another country's pop goods dependence on this can yield 0 ED |
| ECONOMIC_DEPENDENCE_TRADE_ROUTE_DEPENDENCE_FACTOR | 3 | # This is the factor applied when value of trade volume between countries represents 100% of GDP |
| ECONOMIC_DEPENDENCE_TRADE_ROUTE_DEPENDENCE_MIN | 0 |  |
| ECONOMIC_DEPENDENCE_TRADE_ROUTE_DEPENDENCE_MAX | 3 |  |
| RELATIONS_CHANGE_INVESTORS_MONOPOLY_CREATED | -10 | # Relations change towards countries with investment rights when a country creates a monopoly |
| # selection for the signing location of a treaty happens in two steps # 1. a state is randomly selected among up to 6, those 6 being: # - the capital (1) # - the state with higest gdp (1) # - the state with the second highest gdp (0 or 1) # - for both treaty participants # - single-state countries don't have a second highest gdp state # 2. once a state is randomly selected, a hub is randomly selected in the # state region that the state belongs to (if it applies, e.g. no ports # in landlocked state regions) # every random selection is weighted via the following weights |  |  |
| TREATY_SIGNING_STATE_WEIGHT_CAPITAL | 1 | # weight that states have when randomly chosing a signing place for a treaty [>= 1] |
| TREATY_SIGNING_STATE_WEIGHT_HIGHEST_GDP | 1 | # as above, for the state with the highest gdp [>=1] |
| TREATY_SIGNING_STATE_WEIGHT_SECOND_HIGHEST_GDP | 1 | # as above, for the state with the second highest gdp [>=1] |
| TREATY_SIGNING_HUB_WEIGHT_CITY | 5 | # weight that city hubs have when randomly chosing a signing place for a treaty [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_PORT | 3 | # as above, for port hubs [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_FARM | 2 | # as above, for farm hubs [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_MINE | 1 | # as above, for mine hubs [>= 1] |
| TREATY_SIGNING_HUB_WEIGHT_WOOD | 1 | # as above, for wood hubs [>= 1] |
| MAX_TREATY_OBLIGATIONS_DELAY_DAYS | 3650 | # obligations promised as part of treaties take effect on binding period end, or once this amount of days has passed since the treaty was originally signed, whichever comes first [>= 0] |
| BINDING_PERIOD_THRESHOLD_TO_EFFECTUATE_TREATY_OBLIGATIONS_DAYS | 30 | # When binding period is this many days or less, obligations are effectuated |
| TREATY_ARTICLE_MONEY_TRANSFER_ARTICLE_TYPE | "money_transfer" |  |
| TREATY_ARTICLE_TREATY_PORT_ARTICLE_TYPE | "treaty_port" |  |
| TREATY_ARTICLE_INVESTMENT_RIGHTS_ARTICLE_TYPE | "foreign_investment_rights" |  |
| TREATY_ARTICLE_LAW_COMMITMENT_ARTICLE_TYPE | "law_commitment" |  |
| DEFAULT_WAR_REPARATIONS_MONEY_TRANSFER | 0.1 |  |
| TREATY_PROPOSAL_COOLDOWN_DAYS | 7 | # The number of days before you can send another treaty proposal after having one rejected |
| TREATY_DEFAULT_BINDING_DURATION_YEARS | 5 |  |
| TREATY_THREATEN_HOSTILITIES_DURATION_DAYS | 365 |  |
| THREATEN_NAVAL_HOSTILITIES_COOLDOWN_DAYS | 1825 | # 5 years before you can threaten naval hostilities against the same country again |
| NAVAL_HOSTILITIES_POINTS_MAX | 100 | # Maximum damage points that can be inflicted in a single instance of naval hostilities |
| NAVAL_VULNERABILITY_MAX | 1.0 | # Maximum naval vulnerability score. This is used to determine how afraid a country should be of naval hostilities. |
| NAVAL_VULNERABILITY_TRADE_MULTIPLIER | 0.75 | # Vulnerability from trade: this value * (trade base cost / GDP) = vulnerability points |
| NAVAL_VULNERABILITY_COASTAL_GDP_MULTIPLIER | 0.5 | # Vulnerability from coastal GDP: this value * (coastal GDP / GDP) = vulnerability points |
| NAVAL_VULNERABILITY_PRESTIGE_MULTIPLIER | 1.0 | # Vulnerability from naval prestige: this value * (navy prestige / total prestige) = vulnerability points |
| NAVAL_HOSTILITIES_POINTS_SHIPS_SUNK_AT_FULL_FLEET | 500 | # Damage points awarded when 100% of a country's fleet construction cost is sunk |
| NAVAL_HOSTILITIES_POINTS_BLOCKADE_GDP_WEEKLY | 20 | # Damage points per week when 100% of a country's GDP is blockaded |
| NAVAL_HOSTILITIES_POINTS_PIRACY_GDP_WEEKLY | 20 | # Damage points per week when 100% of a country's GDP in goods is seized via piracy |
| NAVAL_HOSTILITIES_POINTS_BOMBARDMENT_DEVASTATION | 20 | # Damage points per unit of devastation added, scaled by state GDP / victim GDP |
| NAVAL_HOSTILITIES_POINTS_BOMBARDMENT_BUILDING_DESTROYED | 10 | # Fixed damage points per building level destroyed by bombardment |
| PAST_TEMPORARY_HOSTILITIES_KEEP_YEARS | 20 | # Number of years to keep temporary hostilities data after expiry |
| PIRACY_DAMAGE_TRACKING_WEEKS | 26 | # Number of weeks of piracy damage history to keep for averaging |

### PowerBlocs

| Define | Default Value | Dev Comment |
|---|---|---|
| MAX_PRINCIPLES | 4 | # Max number of principles that a Power Bloc can have |
| INITIAL_PRINCIPLE_LEVELS | 1 | # Max total levels of principles that a Power Bloc can have during formation |
| FORMATION_COOLDOWN_MONTHS | 24 | # Cooldown in months between the attempts to form Power Blocs |
| JOIN_COOLDOWN_MONTHS | 6 | # If a Country leaves a Power Bloc they cannot re-join before X months |
| LEAVE_COOLDOWN_MONTHS | 6 | # If a Country joins a Power Bloc they cannot leave within X months |
| MIN_MEMBERS | 2 | # This is the minimum number of members that the bloc needs to have to be considered active. Members include the leader. |
| LEVERAGE_LOBBY_CLOUT_FACTOR | 500 | # Leverage gain is increased or decreased by the Lobby's total Clout * this factor |
| INVITE_ACTION_NAME | "invite_to_power_bloc" |  |
| JOIN_ACTION_NAME | "join_power_bloc" |  |
| MAX_MANDATE_PROGRESS | 2000 | # When mandate progress reaches this value, the power bloc gains one mandate |
| MAX_MANDATES | 3 | # This is the maximum number of mandates that can be accumulated at once |
| PRINCIPLE_SELECTION_COOLDOWN_DAYS | 90 | # Once a principle is selected, it cannot be changed for this many days. Upgrading is unaffected by the cooldown, but resets it. |
| POWER_STRUGGLE_PRESTIGE_THRESHOLD_START | 1.2 | # If a power bloc member has more prestige than leader's prestige X this - power struggle starts with the member becoming contender |
| POWER_STRUGGLE_PRESTIGE_THRESHOLD_FAIL | 1.15 | # If a contender has less prestige than leader's prestige X this - power struggle fails |
| POWER_STRUGGLE_DURATION_SUCCESS_MONTHS | 12 | # Power struggle succeeds after this months |
| POWER_STRUGGLE_DURATION_FACTOR_FOR_FOUNDER | 0.75 | # Power struggle succeeds after this X POWER_STRUGGLE_DURATION_SUCCESS_MONTHS if the contender is the founder of the power bloc |
| COHESION_WEEKLY_DRIFT_MAX | 1 | # At most, Cohesion will drift by +/- this value each week |
| COHESION_TARGET_MAX | 100 | # The highest value Cohesion can reach |
| POWER_BLOC_INFLUENCE_COST | 500 | # Cost in Influence to form / be the leader of a Power Bloc |
| MAX_LEVERAGE | 1000 | # How much "raw" Leverage can be split between parties (the country itself + each Power Bloc) |
| LEVERAGE_WEEKLY_DRIFT_FACTOR | 0.02 | # The delta between current Leverage and Target Leverage will be multiplied by this to determine the weekly Leverage drift |
| LEVERAGE_WEEKLY_DRIFT_MIN | 1 | # At minimum, Leverage will drift by +/- this value each week, up/down to the target |
| COUNTRY_POPULATION_LEVERAGE_RESISTANCE_MODIFIER_DIVISOR | 1000000 | # Population divided by this is multiplied by country_leverage_resistance_per_population to give a certain amount of leverage per million people |
| COUNTRY_POPULATION_LEVERAGE_RESISTANCE_MODIFIER_MAX_MULTIPLIER | 100 | # Max multiplier given by population. With the value above at 1 000 000, this means the cap for leverage resistance is at 100 000 000. |

### Pops

| Define | Default Value | Dev Comment |
|---|---|---|
| NUM_WEALTH_LEVELS | 99 |  |
| POP_WEIGHT_MODIFIER_MAX_SCALE | 100 | # The maximum scale applied to weight modifiers on the pop portrait |
| DEFAULT_POP_TYPE | "laborers" | # Used by: create_pop effects; migration; injured military leaving their outposts; slaves default employment role; etc. |
| SLAVE_POP_TYPE | "slaves" | # This is the type of pop that debtors will become |
| ACADEMICS_POP_TYPE | "academics" | # Academic pops |
| OFFICERS_POP_TYPE | "officers" | # This is the type of pop that is considered military officers |
| SERVICEMEN_POP_TYPE | "soldiers" | # This is the type of pop that is considered military servicemen |
| POP_SIZE_PACKAGE | 10000 | # "Normal" pop size used as a divisor on population when determining e.g. Needs to buy, wages to pay, etc |
| WEALTH_PROGRESS_WANTED_BUFFER | 1.02 | # A pop wants at least as much income as this x the next level buy package costs to increase its wealth |
| WEALTH_PROGRESS_ACCEPTABLE_DEFICIT | 0.98 | # A pop won't change wealth level if they can still afford this much of their current buy package costs |
| WEALTH_PROGRESS_INCREASE | 0.2 | # How fast wealth increases when a pop has money for higher grade buy packages. This factor is modified by how large the difference between income and cost is |
| WEALTH_PROGRESS_DECREASE | 0.1 | # How fast wealth decrease when a pop can no longer afford its buy package. This factor is modified by how large the difference between income and cost is |
| WEALTH_PROGRESS_DECREASE_DEFICIT_MULT | 5 |  |
| LOYALTIES_GAIN_GRACE_PERIOD_SHORT | "1837.1.1" | # Until this date, only a scaling part of the Radicals and Loyalists gained from SOL changes will be applied if the Short game rule is applied |
| LOYALTIES_GAIN_GRACE_PERIOD_LONG | "1841.1.1" | # Until this date, only a scaling part of the Radicals and Loyalists gained from SOL changes will be applied if the Long game rule is applied |
| LOYALTIES_GAIN_GRACE_PERIOD_EXTRA_LONG | "1846.1.1" | # Until this date, only a scaling part of the Radicals and Loyalists gained from SOL changes will be applied if the Extra Long game rule is applied |
| RADICALS_MAX_FROM_LOW_SOL | 0.15 | # If pop is already this % radical, don't add more radicals from low SOL (Scales by delta between SoL and expected min SoL) |
| RADICALS_MAX_FROM_DISCRIMINATION | 0.5 | # If pop is already this % radical, don't add more radicals from discrimination (Scales by literacy) |
| # Radicals Monthly indicates what fraction of the pop turns radical every month while starving # Radicals max indicates at what max fraction of radicals we stop adding new ones due to starvation # Radical growth/max increases between these values as Food Security decreases |  |  |
| RADICALS_MONTHLY_FROM_STARVATION_BASE | 0.002 | # Food Security = Mild Threshold |
| RADICALS_MONTHLY_FROM_STARVATION_MILD | 0.008 | # Food Security = Severe Threshold |
| RADICALS_MONTHLY_FROM_STARVATION_SEVERE | 0.02 | # Food Security = 0 |
| RADICALS_MAX_FROM_STARVATION_BASE | 0.15 | # Food Security = Mild Threshold |
| RADICALS_MAX_FROM_STARVATION_MILD | 0.5 | # Food Security = Severe Threshold |
| RADICALS_MAX_FROM_STARVATION_SEVERE | 0.75 | # Food Security = 0 |
| ALLOW_ASSIMILATION_IN_HOMELANDS | no | # Can pops assimilate when living in their homelands? |
| ALLOW_ASSIMILATION_REQUIRE_HERITAGE_GROUP | no | # Can pops assimilate into pops of a different heritage group (weaker condition) |
| ALLOW_ASSIMILATION_REQUIRE_HERITAGE_TRAIT | no | # Can pops assimilate into pops of a different heritage trait (stronger condition) |
| #in case if both are allowed, heritage trait requirement takes precedence |  |  |
| ASSIMILATION_RATE | 0.002 | # Percentage of pops who will Assimilate into a different Culture each month, if eligible |
| MIN_ASSIMILATION | 1 | # If there is any assmiliation at least this many people will assimilate |
| ASSIMILATION_IN_HOMELAND_MULT | 0.75 | # Assimilation rate is multiplied by this in homelands |
| CONVERSION_RATE | 0.002 | # Percentage of pops who will Convert into a different Religion each month, if eligible |
| CONVERSION_UNINCORPORATED_MULT | 0.1 | # CONVERSION_RATE is multiplied by this in unincorporated states |
| MIN_CONVERSION | 1 | # If there is any conversion at least this many people will convert |
| DEFAULT_OBSESSION_DEMAND_MIN | 0.5 | # The minimum relative demand of an obsession (overrides min demand in buy package goods categories), can be overriden in pop need |
| DEFAULT_OBSESSION_DEMAND_MULT | 1.5 | # Demand of an obsession is multiplied by this, can be overriden in pop need |
| MIN_POPS_FOR_NEW_OBSESSION | 50000 | # At least this many pops of a culture must live in a market to get an obsession from its goods |
| MIN_SUPPLY_LEVEL_FOR_NEW_OBSESSION | 0.5 | # Supply needs to be at least this times the demand |
| MIN_DEMAND_VALUE_FOR_NEW_OBSESSION | 500 | # At this amount of (number of units * goods base price) needs to be demanded in a market to create a new obsession |
| MAX_NUM_OBSESSIONS | 3 | # A culture can only have this number of obsessions at the same time |
| OBSESSION_SPAWN_CHANCE | 0.5 | # Per year (1.0 = 1%), multiplied by goods supply and market size mult |
| OBSESSION_SPAWN_CHANCE_MAX_SUPPLY_MULT | 3.0 | # Supply relative to demand above this isn't factored into spawn chance |
| OBSESSION_SPAWN_CHANCE_PRESTIGE_GOODS_MULT | 4.0 | # Chance for a new obsession to spawn is multiplied by 1 + this, scaled by fraction of the goods supply that is prestige goods |
| TABOO_DEMAND_MULT | 0.5 | # Demand of a taboo is multiplied by this |
| DEFAULT_PRESTIGE_GOODS_DEMAND_INCREASE | 0.5 | # Demand for goods is multiplied by ( 1 + this ), scaled by how much of the local supply is prestige goods, can be overriden in pop need |
| MAX_DEMAND_ADJUSTMENT_BASE_AMOUNT | 0.01 | # Controls how much a pop can change demand of a substituable goods in a single update (base) |
| MAX_DEMAND_ADJUSTMENT_SCALED_AMOUNT | 0.09 | # Controls how much a pop can change demand of a substituable goods in a single update (scaled) |
| MAX_DEMAND_ADJUSTMENT_SCALE | 1.0 | # At this delta between target and current demand, apply max demand adjustment scale |
| PRESTIGE_GOOD_SOL_BONUS_SCALING | 0.4 | # Added multiplier to SoL, scales with % of pop buy package that is prestige goods |
| PRESTIGE_GOOD_SOL_MAX_BONUS | 0.2 | # Added multiplier to SoL from prestige goods cannot be higher than this |
| LOCAL_GOODS_SUBSTITUTION_SUPPLY_GDP_FACTOR | 0.25 | # To allow local goods to properly compete with non-local ones in large markets, we add a fraction of the market production of the local good that is equal to ( 1 - the state's GDP share ) * this # This is only done for the purposes of goods substitution supply and *not* for price calculations |
| OBSESSION_POP_NEED_EXPENSE_MULT | 0.25 | # Total spent on pop needs including obsessions is changed by this (scaled by number of obsessions, money is given or taken from other needs) |
| TABOO_POP_NEED_EXPENSE_MULT | -0.25 | # Total spent on pop needs including taboos is changed by this (scaled by number of taboos, money is given or taken from other needs) |
| WORKING_ADULT_RATIO_BASE | 0.25 | # Base ratio of working adults to dependents, this can be overridden by pop type definition and country modifiers. |
| WORKING_ADULT_RATIO_SKEW_MAXIMUM | 2.0 | # When the ratio of working adults to dependents is skewed, it tends to correct itself, this value clamps the maximum effect of this |
| DEPENDENT_CONSUMPTION_RATIO | 0.5 | # Dependents consume this multiple of Needs compared to Working Adults |
| LITERACY_DIEOFF_BIAS | 1.0 | # Percentage of literate pops who die of old age compared to the current literacy rate, the higher this value the faster the population becomes illiterate when literacy suffers |
| DEFAULT_SOL_CHANGE_IMPACT_FACTOR | 0.03 | # How large part of a pop become more loyalist or radical as a result of a change in standard of living, can be overriden on specific pop types |
| SOL_CHANGE_IMPACT_FACTOR_REDUCTION_START | 15 | # Above amount of SoL, we start scaling down loyalists/radicals from SoL changes |
| SOL_CHANGE_IMPACT_FACTOR_REDUCTION_END | 30 | # At this amount of SoL, we apply maximum scaling down of loyalists/radicals from SoL changes |
| SOL_CHANGE_IMPACT_FACTOR_REDUCTION_SCALE | 9 | # Loyalists/radicals from SoL changes is divided by ( 1 + this ) at maximum scaling |
| SOL_STARVING_THRESHOLD | 5 |  |
| SOL_STRUGGLING_THRESHOLD | 10 |  |
| LOW_POP_THRESHOLD | 5000 | # If a state has less than this amount of pops per arable land, apply the low pop modifier |
| HIGH_POP_THRESHOLD | 100000 | # If a state has more than this amount of pops per arable land, apply the high pop modifier |
| (wiki editor's note) The following defines come after the pop migration defines but before the pop consolidation defines in `00_defines.txt`. |  |  |
| COLONIZATION_RIGHTS_GROWTH_MULTIPLIER | 2.0 | # Colonial growth AND max colonial growth are multiplied by this if you have colonization rights |
| COMPANY_COLONIZATION_GROWTH_MULTIPLIER | 1.2 | # Colonial growth AND max colonial growth are multiplied by this if you have company colonization rights |
| COLONIAL_GROWTH_BASE_FACTOR | 0.00001 | # Colonial growth generated by a state is this amount per 1000 population, multiplied by the Colonial Growth modifier in the state |
| MIN_BASE_COLONIAL_GROWTH | 0.005 | # Country base colonial growth from population cannot be lower than this |
| MAX_BASE_COLONIAL_GROWTH | 0.1 | # Country base colonial growth from population cannot be higher than this |
| MAX_COLONIAL_GROWTH | 0.02 | # Colonies can grow by this much at most per day |
| COLONY_SPEED_PROVINCE_SIZE_STANDARD | 50 | # Sets a baseline for how large (in provinces) a colonizable state region is |
| COLONY_SPEED_PER_PROVINCE_DIFF_FROM_STANDARD | 0.02 | # For every province the state region has above or below COLONY_SPEED_PROVINCE_SIZE_STANDARD, increase or decrease colonization speed by this rate (as a percentage) |
| COLONY_SPEED_POPULATION_INCREMENT | 100000 | # Determines the number of people across both colonizing and colonized states that should start slowing down the rate of colonization; set to 0 to disable |
| COLONY_SPEED_MALUS_PER_POPULATION_INCREMENT | 0.25 | # Starting at COLONY_SPEED_THRESHOLD_FROM_POPULATION inhabitants, increase the number of days to complete by this amount proportional to population in the colony + state of province being colonized above 200K (e.g. at COLONY_SPEED_THRESHOLD_FROM_POPULATION = 200K, this set to 0.5, and at 300K total inhabitants, multiply growth by 1/1.25 = 0.8; at 600K inhabitants, multiply by 0.25) |
| INDIVIDUALS_PER_POP_INFRASTRUCTURE | 100000 | # Multiply state_infrastructure_from_population_add by this to determine infra from population |
| QUALIFICATIONS_UPDATE_FACTOR | 0.0003 | # Calculated potential values are multiplied by this value and the workforce size of the pop before being added to the existing potentials |
| QUALIFICATIONS_NUM_MONTHS_AT_START | 60 | # How many months of qualifications should be seeded to pops at start of game? |
| INDIVIDUALS_TAXED_PER_TAX_CAPACITY | 10000 | # How many pops can be taxed efficiently for each tax capacity |
| EXPECTED_SOL_FROM_LITERACY_SUBSISTENCE_MULT | 0.25 | # Expected SoL from literacy is multiplied by this for Pops working in subsistence buildings |
| JOB_SATISFACTION_BASE | -130 | # Base job satisfaction |
| JOB_SATISFACTION_FOR_NEWLY_HIRED | 1000 | # Job satisfaction gained due to having been newly hired, this state lasts until the pop's next wealth calculation |
| JOB_SATISFACTION_PER_SOL_ABOVE_EXPECTED_SOL | 3 | # Job satisfaction gained per level of SoL above your expected SoL |
| JOB_SATISFACTION_PER_SOL_ABOVE_STATE_STRATA_SOL | 2 | # Job satisfaction gained per level of SoL above the state average for your strata |
| JOB_SATISFACTION_PER_SOL_ABOVE_COUNTRY_STRATA_SOL | 1 | # Job satisfaction gained per level of SoL above the country average for your strata |
| JOB_SATISFACTION_PER_PERCENT_WAGE_RATE_ABOVE_NORMAL | 1 | # Job satisfaction gained per pound of workplace wage rate (weekly wage of 10k laborers) above country normal |
| JOB_SATISFACTION_FROM_CAN_AFFORD_EXPENSES | 1000 | # Job satisfaction gained from being able to afford your bug package (and taxes) |
| JOB_SATISFACTION_FROM_CANNOT_AFFORD_EXPENSES | -100 | # Job satisfaction gained from not being able to afford your bug package (and taxes) |
| JOB_SATISFACTION_PER_PERCENT_HIGHER_SOL_QUALIFICATION | -1 | # Job satisfaction gained per percent of workforce qualified for a job with a higher base standard of living. Note that qualifications are assumed to overlap and the largest qualification is used in this calculation |
| JOB_SATISFACTION_FROM_JOB_ATTRACTIVENESS | 100 | # Job satisfaction when employed, multiplied by job attractiveness |
| JOB_SATISFACTION_DIVIDENDS_MAX_MULT | 5 | # Max multiplier from the ratio between pop dividends and wages |
| JOB_SATISFACTION_DIVIDENDS_BASE | 50 | # Base value to be multiplied by the ratio between dividends and wages |
| JOB_SATISFACTION_LOSSES_MIN_MULT | -5 | # Min multiplier from the ratio between pop losses and wages (or if you will, max magnitude) |
| JOB_SATISFACTION_LOSSES_BASE | 50 | # Base value to be multiplied by the ratio between losses and wages |
| JOB_SATISFACTION_GOVERNMENT | 50 | # Government jobs need a bit more stability |
| @starvation_threshold | 0.4 |  |
| @starvation_scaling_factor | @[1/starvation_threshold] |  |
| FOOD_SECURITY_MODERATE_THRESHOLD | 0.6 | # If Food Security is lower than this, the pop is marked as having moderate food security |
| FOOD_SECURITY_STARVATION_THRESHOLD | @starvation_threshold | # If Food Security is lower than this, the pop is considered to be in a starving state |
| FOOD_SECURITY_SEVERE_STARVATION_THRESHOLD | 0.2 | # If Food Security is lower than this, the pop is considered to be in a severe starving state |
| STARVATION_EFFECTS_SCALING_FACTOR | @starvation_scaling_factor | # Acts as a scaling factor when converting food security to starvation effects: StarvationValue = CLAMP( (StarvationThreshold - FoodSecurity) * ScalingFactor, 0, 1) |
| FAMINE_POPULATION_SHARE_IN_STARVATION | 0.35 | # If at least this % of state population is in starvation, the state is considered to have a famine |
| FAMINE_POPULATION_SHARE_IN_SEVERE_STARVATION | 0.15 | # If at least this % of state population is in severe starvation, the state is considered to have a famine |

#### Pop migration

| Define | Default Value | Comment |
|---|---|---|
| ## General ## |  |  |
| MIGRATION_MIN_STATE_POPS | 20000 | # A state with less population than this will not get emigration |
| MIGRATION_STATE_POPULATION_THRESHOLD | 100000 | # States with less pops than this have reduced market emigration numbers to avoid total depopulation |
| MIGRATION_MAX_PER_STATE_BASE | 500 | # No more than this amount of people can move from or to a state in a single week (base) |
| MIGRATION_MAX_PER_STATE_INFRASTRUCTURE | 5 | # No more than this amount of people can move from or to a state in a single week (scales with infrastructure) |
| MIGRATION_MAX_EMIGRATION_AS_POPULATION_FRACTION | 0.005 | # Max emigration per week is clamped to this fraction of a state's population |
| MIGRATION_MAX_PER_STATE_UNEMPLOYMENT_ORIGIN_FRACTION | 0.05 | # The amount of unemployed workers in a state * this value is added to how many people can move from it (after clamping from MIGRATION_MAX_EMIGRATION_AS_POPULATION_FRACTION) |
| MIGRATION_MAX_PER_STATE_UNEMPLOYMENT_TARGET_FRACTION | 0.05 | # The amount of unemployed workers in a state * this value is removed from how many people can move to it (after clamping from MIGRATION_MAX_EMIGRATION_AS_POPULATION_FRACTION) |
| # Migration Desire # |  |  |
| MIGRATION_DESIRE_FROM_JOB_SATISFACTION_FACTOR | -1.0 | # A pop's desire to migrate will be increased by its job satisfaction multiplied by this value. |
| # Acceptance # |  |  |
| MIN_ACCEPTANCE_VALUE | 0 | # It is both the minimum acceptance value a pop can have as well as the explicit threshold scripted for the first acceptance status [any signed 32 bit value] |
| MAX_ACCEPTANCE_VALUE | 100 | # It is both the maximum acceptance value a pop can have as well as the (implied) upper bound of the last acceptance status [> MIN_ACCEPTANCE_VALUE] |
| ACCEPTANCE_FROM_HOMELAND_COMMUNITY | 0 | # The amount of acceptance a pop gets from living in their homeland, applied statically on their Cultural Community |
| ACCEPTANCE_FROM_NOT_HOMELAND_COMMUNITY | 0 | # The amount of acceptance a pop gets from not living in their homeland, applied statically on their Cultural Community |
| MIN_REQUIRED_ACCEPTANCE_FOR_MIGRATION | 30 | # If a pop would have less than this much acceptance in a target state, they won't mass migrate there |
| EXPECTED_ACCEPTANCE_INCREASE_TO_MIGRATE | 10 | # A pop will look to increase their acceptance by this much when mass migrating, but might accept less if mass migration attraction difference is high enough |
| MAX_ACCEPTANCE_RATIO_MULT_MIGRATION | 5 | # A difference in acceptance between source and target in mass migrations will result in at most this much increased migration |
| BUCKET_MIGRATION_EXPIRATION_YEARS | 5 | # How long a migration bucket will be kept before it is removed |
| BUCKET_MIGRATION_THRESHOLD | 1000 | # How many pops need to be in a bucket before it is executes migration |
| BUCKET_MIGRATION_MIN_LEFTOVER_THRESHOLD | 1000 | # Minimum number of pops that can stay without being moved over to another state when a bucket migration is executed |
| MIGRATION_PULL_CULTURE_VACANCIES_MODIFIER | 0.25 | # Modifies migration pull for pop if there is vacancies available for the pop culture |
| MIGRATION_PULL_CULTURE_NO_VACANCIES_MODIFIER | -0.5 | # Modifies migration pull for pop if there is no vacancies available for the pop culture |
| # Cultural Communities # |  |  |
| CULTURAL_COMMUNITY_LINGER_TIME_WEEKS | 3 | # When the last pop of a given culture leaves a state, the corresponding cultural community will be removed after this long |
| CULTURAL_COMMUNITY_MAX_PER_MONTH_CHANCE | 0.04 |  |
| CULTURAL_COMMUNITY_ACCEPTANCE_DELTA_ON_SPAWN | -0.3 | # The percentage of the maximum cultural acceptance that should be added as a delta to the cultural community when it first appears |
| CULTURAL_COMMUNITY_ACCEPTANCE_DELTA_DECAY_PER_MONTH | 0.25 | # The amount of acceptance delta that will decay each month |
| # Cultural Fervor # |  |  |
| CULTURAL_FERVOR_MAX | 100 | # The maximum value of cultural fervor |
| CULTURAL_FERVOR_MIN | 0 | # The minimum value of cultural fervor |
| CULTURAL_FERVOR_DRIFT | 0.01 | # Factor to control the monthly drift from current to target Fervor |
| CULTURAL_FERVOR_DRIFT_MIN | 0.05 | # The minimum amount fervor will move towards its target (unless it would overshoot) |
| CULTURAL_FERVOR_LITERACY_IMPACT | 35 | # The impact of pops literacy on the cultural fervor |
| CULTURAL_FERVOR_WAR_IMPACT | 20 | # The impact of a war on the cultural fervor, unused |
| CULTURAL_FERVOR_CASUALTIES_IMPACT_MAX | 30 | # The maximum impact of casualties from war and attrition on the cultural fervor |
| CULTURAL_FERVOR_CASUALTIES_RATIO_MAX | 0.1 | # The ratio of dead to living that gives the maximum casualty impact on the cultural fervor |
| CULTURAL_FERVOR_ACADEMICS_IMPACT | 0.002 | # The impact of pops education access on the cultural fervor per person |
| CULTURAL_FERVOR_ACADEMICS_IMPACT_CAP | 25 | # Cap for the academics impact |
| CULTURAL_FERVOR_ACCEPTANCE_IMPACT | -0.05 | # The impact of a pops acceptance on the cultural fervor |
| CULTURAL_FERVOR_NATIONALISM_IMPACT | 5 | # The impact of nationalism on the cultural fervor, if all pops of a culture lives under nationalsim, then the cultural fervor will increase by this amount, else a fraction of it |
| CULTURAL_FERVOR_PAN_NATIONALISM_IMPACT | 5 | # The impact of pan-nationalism on the cultural fervor, if all pops of a culture lives under pannationalsim, then the cultural fervor will increase by this amount, else a fraction of it |
| CULTURAL_FERVOR_PUBLIC_SCHOOLS_IMPACT | 10 | # The impact of public schools on the cultural fervor, if all pops of a culture lives under public schools, then the cultural fervor will increase by this amount, else a fraction of it |
| CULTURAL_FERVOR_OTHER_CULTURES_RELEASED_IMPACT | 10 | # The impact on non-primary cultures in country where a culture gets released |
| CULTURAL_FERVOR_NATIONAL_AWAKENING_THRESHOLD | 25 | # The fervor threshold over which it is possible for a culture to have a national awakening |
| CULTURAL_NATIONAL_AWAKENING_CHANCE_INCREASE_PER_FERVOR | 0.01 | # The increase in chance per point of fervor of a national awakening happening once fervor is above the awakening threshold |
| CULTURAL_FERVOR_NATIONAL_AWAKENING_IMPACT | 20 | # The impact on fervor from having a national awakening |
| CULTURAL_FERVOR_NATIONAL_AWAKENING_DEFAULT_LENGTH_MONTHS | 120 | # The default length of a national awakening in months |
| CULTURAL_FERVOR_ASSIMILATIOM_EFFECT | 0.01 | # The effect cultural fervor has on assimilation, it makes it this much harder to assimilate with higher fervor |
| CULTURAL_FERVOR_WAR_SUPPORT_EFFECT | 0.01 | # The effect cultural fervor has on war support |
| CULTURAL_FERVOR_CONQUEST_RADICILIZATION_IMPACT | -0.005 | # This modifies the radicialization of pops in a state when it is conquered by a country with a primary culture the same as the pops |
| # Slavery # |  |  |
| MIGRATION_MIN_POP_AMOUNT | 1 | # No less than this amount of a pop can migrate each week (if any migration at all should happen) |
| # UX/UI Labeling # |  |  |
| MIGRATION_PULL_HIGH_THRESHOLD | 1.25 | # State must have a migration pull of at least market average * this to get market immigration |
| MIGRATION_PULL_LOW_THRESHOLD | 0.75 | # State must have a migration pull of less or equal than market average * this to get full amount of emigration |
| # Treaty Ports # |  |  |
| TREATY_PORT_INITIAL_MIGRATION | 1000 | # This is the amount of people of the taker country's first primary culture to migrate to a treaty port upon establishment |
| ## Migration Attraction ## |  |  |
| MIGRATION_PULL_EMPTY_STATE | 100 | # If a state has no pops at all, give it a huge migration pull |
| MIGRATION_PULL_FROM_LIVING_STANDARD | 2 | # Migration pull from each point of average living standard in target state |
| MIGRATION_PULL_FROM_AVAILABLE_EMPLOYMENT | 30 | # Migration pull is increased by for each 10k available non subsistence jobs |
| MIGRATION_PULL_FROM_AVAILABLE_EMPLOYMENT_MAX | 30 | # Migration pull is increased by the % of available non subsistence jobs compared to employed non subsistence pops, multiplied by this |
| MIGRATION_PULL_FROM_AVAILABLE_SUBSISTENCE_EMPLOYMENT | 2 | # Migration pull is increased by the % of available subsistence jobs compared to employed non subsistence pops, multiplied by this |
| MIGRATION_PULL_FROM_AVAILABLE_SUBSISTENCE_EMPLOYMENT_MAX | 10 | # Migration pull from available subsistence jobs cannot exceed this |
| MIGRATION_PULL_REDUCTION_FROM_UNEMPLOYMENT | 50 | # Migration pull is reduced by the % of unemployed pops compared to employed pops, multiplied by this |
| MIGRATION_PULL_REDUCTION_FROM_UNEMPLOYMENT_MAX | 50 | # Migration pull reduction from unemployment cannot exceed this |
| ## Market Migrations ## |  |  |
| # Market Migration Processing # |  |  |
| MARKET_MIGRATION_STATE_ATTRACTION_FRACTION | 0.75 | # States with at least this fraction of the most attractive state's migration attraction will receive migration |
| MARKET_MIGRATION_PER_WEEK_FACTOR | 5 | # This number of individuals will migrate for each point of difference in migration pull |
| MARKET_MIGRATION_PER_WEEK_PER_TOTAL_POPULATION | 100000 | # Additionally, one more individual will migrate per this number of population for each point of difference in migration pull |
| MARKET_MIGRATION_MIN_DIFFERENCE_IN_MIGRATION_ATTRACTION_TO_MOVE | 5 | # Pops will not migrate if their best option is to a state with a lower delta in migration pull than this number |
| MARKET_MIGRATION_MIN_POP_FRACTION_TO_MOVE | 0.05 | # If the people wanting to migrate constitues less than this fraction of a pop, no new pop will be created and they won't migrate. |
| MIGRATION_PULL_MULT_FROM_NO_DISCRIMINATION | 0.5 | # Migration pull multiplier increased by this if pop is moving from discrimination to no discrimination (not applied to mass migration targets) |
| MIGRATION_PULL_MULT_FROM_HOMELANDS | 0.2 | # Migration pull multiplier increased by this if pop is moving to cultural homelands (not applied to mass migration targets) |
| ## Mass Migrations ## # Mass Migration Setup # |  |  |
| MASS_MIGRATION_MIN_TRADE_VALUE_BETWEEN_MARKETS | 1 | # At least this much monetary value of trade must be happening between two markets for mass migration to occur between them. This counts both world market trade and treaty trade. |
| MASS_MIGRATION_ORIGIN_MIN_TURMOIL | 0.15 | # Must have at least this much turmoil in cultural homelands to create a migration target |
| MASS_MIGRATION_ORIGIN_MIN_EMIGRANTS | 100000 | # A country must have at least this many possible migrants to trigger a mass migration |
| MASS_MIGRATION_TARGET_MAX_TURMOIL | 0.30 | # Must have this or less turmoil among the culture for a country to be picked as a mass migration target |
| MASS_MIGRATION_TARGET_MIN_ARABLE_LAND | 10 | # A state must have at least this much arable land to be a mass migration target |
| MASS_MIGRATION_STATE_MIN_MARKET_ACCESS | 0.7 | # A state must have at least this much market access to their market to be a mass migration target or origin state |
| MASS_MIGRATION_SPAWN_CHANCE | 2 | # Per week for each potential mass migration, scales with turmoil (1 = 1%) |
| MASS_MIGRATION_SPAWN_CHANCE_STRUGGLING_FACTOR | 0.2 | # Chance increases by this for each point of SoL below 10 for a culture in a country |
| MASS_MIGRATION_SPAWN_CHANCE_STARVING_FACTOR | 1 | # Chance increases by this for each point of SoL below 5 for a culture in a country (added on top of struggling factor) |
| MASS_MIGRATION_TARGET_COUNTRY_RANDOM_FACTOR | 0.5 | # The higher this is, the more random the selection of mass migration country targets will be |
| MASS_MIGRATION_TARGET_STATE_RANDOM_FACTOR | 0.5 | # The higher this is, the more random the selection of mass migration state targets in the target country will be |
| MASS_MIGRATION_DURATION_MONTHS | 12 | # How long does a mass migration last in months |
| MASS_MIGRATION_COOLDOWN_MONTHS | 48 | # How many months before the same culture can mass migrate from a country again |
| MASS_MIGRATION_NUM_TARGET_STATES_FOR_NO_PENALTY | 4 | # Countries with at least this number of possible target states do not receive any penalty to their mass migration target score |
| MASS_MIGRATION_FEW_TARGET_STATES_PENALTY | 0.2 | # Mass migration target score is reduced by a fraction of itself equal to this times number of possible target states less than MASS_MIGRATION_NUM_TARGET_STATES_FOR_NO_PENALTY. Or Score = Score - Score * this * PossibleStatesDiff |
| # Mass Migration Processing # |  |  |
| MASS_MIGRATION_PER_WEEK_FACTOR | 10 |  |
| MASS_MIGRATION_PER_WEEK_PER_TOTAL_POPULATION | 100000 |  |
| MASS_MIGRATION_MIN_DIFFERENCE_IN_MIGRATION_ATTRACTION_TO_MOVE | 10 |  |
|  |  | # The below factors are applied *after* migration pull threshold checks, so they only impact how large a share of migration a state gets |
| MIGRATION_PULL_MULT_FROM_MASS_MIGRATION_TARGET | 1.5 | # Migration pull multiplied by this from target state being a mass migration target |
| MIGRATION_PULL_MULT_FROM_MASS_MIGRATION_TARGET_ADJACENCY | 1.1 | # Migration pull multiplied by this from target state being next to a mass migration target |
| MIGRATION_MAX_PER_STATE_MASS_EMIGRATION_MULT | 3.0 | # Weekly emigration caps are multiplied by this amount by this for mass migrations (after clamping from MIGRATION_MAX_EMIGRATION_AS_POPULATION_FRACTION) |
| MIGRATION_MAX_PER_STATE_MASS_IMMIGRATION_MULT | 5.0 | # Weekly immigration caps are multiplied by this amount by this for mass migrations (after clamping from MIGRATION_MAX_EMIGRATION_AS_POPULATION_FRACTION) |
| MASS_MIGRATION_NEIGHBORING_TARGET_STATE_LIMIT_FRACTION | 0.5 | # Fraction of the limit a neighboring state gets compared to the main target state in a mass migration |

#### Pop consolidation

These defines relate to the game rule for pop consolidation.

| Define | Default Value | Comment |
|---|---|---|
| ### Pop Consolidation defines # Pop Consolidation identifies pops so small their impact on the economy and politics is insignificant, and merges them into other pops in the same building or state. # # POP_MERGE_MAX_WORKFORCE_*: determines how small the pop needs to be in terms of Workforce in order to qualify to be merged with others in their same building or the unemployment pool # POP_MERGE_MIN_NUM_POPS_SAME_PROFESSION_*: employed pops will not get merged with others in their same building if there aren't at least this many pops of the same type in the building # WORKFORCE_RATIO_MAX_UNEMPLOYMENT_FACTOR_*: unemployed Pops with less than POP_MERGE_MAX_WORKFORCE and a Workforce:Dependent ratio that's this much worse than the ideal will be all turned into Dependents and merged back into pops in the same state # # The tail of the define name corresponds to a Pop Consolidation Game Rule with the same name. # When that Game Rule is active, the defined values for POP_MERGE_MAX_WORKFORCE and WORKFORCE_RATIO_MAX_UNEMPLOYMENT_FACTOR represent the minimum values, while the maximum are that of the level above it. # POP_MERGE_START_POP and POP_MERGE_MAX_TARGET_POP determines how high to scale the values towards the level above it. # For example, at Moderate Consolidation, POP_MERGE_START_POP = 50000 and POP_MERGE_MAX_TARGET_POP = 100000, and a global population of 87560 pops: # POP_MERGE_MAX_WORKFORCE will effectively be 45 (75% of the way from 30 to 50) and WORKFORCE_RATIO_MAX_UNEMPLOYMENT_FACTOR will effectively be 1.6244 (75% of the way from 2 to 1.5) |  |  |
| POP_MERGE_MAX_WORKFORCE_MINOR_CONSOLIDATION | 10 |  |
| POP_MERGE_MIN_NUM_POPS_SAME_PROFESSION_MINOR_CONSOLIDATION | 5 |  |
| WORKFORCE_RATIO_MAX_UNEMPLOYMENT_FACTOR_MINOR_CONSOLIDATION | 2.5 |  |
| POP_MERGE_MAX_WORKFORCE_MODERATE_CONSOLIDATION | 30 |  |
| POP_MERGE_MIN_NUM_POPS_SAME_PROFESSION_MODERATE_CONSOLIDATION | 4 |  |
| WORKFORCE_RATIO_MAX_UNEMPLOYMENT_FACTOR_MODERATE_CONSOLIDATION | 2 |  |
| POP_MERGE_MAX_WORKFORCE_AGGRESSIVE_CONSOLIDATION | 50 |  |
| POP_MERGE_MIN_NUM_POPS_SAME_PROFESSION_AGGRESSIVE_CONSOLIDATION | 3 |  |
| WORKFORCE_RATIO_MAX_UNEMPLOYMENT_FACTOR_AGGRESSIVE_CONSOLIDATION | 1.5 |  |
| POP_MERGE_MAX_WORKFORCE_MAX_CONSOLIDATION | 100 |  |
| WORKFORCE_RATIO_MAX_UNEMPLOYMENT_FACTOR_MAX_CONSOLIDATION | 1 |  |
| POP_MERGE_START_POPS | 50000 |  |
| POP_MERGE_MAX_TARGET_POPS | 100000 |  |
| ### Pop Weights for Dependents Distribution # Format: { lower strata, middle strata, upper strata } # These impact the weight assigned to potential target pops for receiving dependents as a result of battlefield injuries # For example, we want injuried and widowed soldier pop individuals to be mostly merged to lower strata pops |  |  |
| DEFAULT_DEPENDENTS_DISTRIBUTION_WEIGHTS | { 1.0 0.5 0.1 } | # For when merging small pops |
| LOWER_STRATA_CASUALTY_DEPENDENTS_DISTRIBUTION_WEIGHTS | { 1.0 0.1 0.0 } | # For when soldiers are wounded |
| MIDDLE_STRATA_CASUALTY_DEPENDENTS_DISTRIBUTION_WEIGHTS | { 0.25 1.0 0.1 } | For when officers are wounded |
| UPPER_STRATA_CASUALTY_DEPENDENTS_DISTRIBUTION_WEIGHTS | { 1.0 0.5 0.1 } | Not used, for modding, enjoy |

#### Pop growth

Pop growth defines use a number of defined and derived variables.

| Variable | Default Value | Comment |
|---|---|---|
| ## Base Values per month |  |  |
| @min_birthrate | 0.00060 | # Minimum base birthrate per month (at POP_GROWTH_STABLE_SOL) |
| @max_birthrate | 0.00450 | # Maximum base birthrate per month (at SOL = 0) |
| @min_mortality | 0.00045 | # Minimum base mortality per month (at POP_GROWTH_STABLE_SOL) |
| @max_mortality | 0.00550 | # Maximum base mortality per month (at SOL = 0) |
| ## SoL Thresholds |  |  |
| @pop_growth_equilibrium_sol | 5 | # Equilibrium is pops stop starving and where growth first becomes positive |
| @pop_growth_transition_sol | 10 | # Transition determines how long birthrate "lags" behind mortality before starting to drop. Setting to same as equilibrium leads to no "lag" (only matters for birthrate) |
| @pop_growth_max_sol | 15 | # Growth Max is where net growth generally is at it's highest (only matters for mortality) |
| @pop_growth_stable_sol | 25 | # Stable is where birthrate and mortality stop changing and hit their minimum values |
| ## Others |  |  |
| @transition_birthrate_mult | 1 | # If you want the birthrate "lag" to go to a higher or lower value than max_birthrate. (you can also just change it directly below) |
| @max_growth_mortality_mult | 0.35 | # What proportion of birthrate_at_growth_max mortality should be at. Higher means lower growth |
| ### Pop Growth Derived values # Generally, for each one of these derived values below we're really just doing one of three operations (or combination of them): # - Calculate a Point: sol * slope + start_value (x_at_y) # - Calculate a Slope: (start_value - end_value) / number_of_steps (x_slope) # - Calculate an Intercept: -slope*sol + end_value (x_intercept) # Intercepts are only needed for line segments that don't start at 0 SoL |  |  |
| @birthrate_at_transition | @[max_birthrate*transition_birthrate_mult] |  |
| @rate_at_equilibrium | @[pop_growth_equilibrium_sol*((birthrate_at_transition-max_birthrate)/pop_growth_transition_sol)+max_birthrate] | # determines both mortality and birthrate |
| ## Mortality from 0 to pop_growth_equilibrium_sol |  |  |
| @mortality_starving_slope | @[(rate_at_equilibrium-max_mortality)/pop_growth_equilibrium_sol] |  |
| ## Birthrate from 0 to pop_growth_transition_sol \|\| |  |  |
| @birthrate_pretransition_slope | @[(birthrate_at_transition-rate_at_equilibrium)/pop_growth_transition_sol] |  |
| ## Mortality from pop_growth_equilibrium_sol to pop_growth_max_sol |  |  |
| @birthrate_at_growth_max | @[(pop_growth_max_sol-pop_growth_transition_sol)*((min_birthrate-birthrate_at_transition)/(pop_growth_stable_sol-pop_growth_transition_sol))+birthrate_at_transition] |  |
| @mortality_at_growth_max | @[birthrate_at_growth_max*max_growth_mortality_mult] |  |
| @mortality_equilibrium_to_growth_max_slope | @[(mortality_at_growth_max-rate_at_equilibrium)/(pop_growth_max_sol-pop_growth_equilibrium_sol)] |  |
| @mortality_equilibrium_to_growth_max_intercept | @[-mortality_equilibrium_to_growth_max_slope*pop_growth_equilibrium_sol+rate_at_equilibrium] |  |
| ## Birthrate from pop_growth_transition_sol to pop_growth_stable_sol |  |  |
| @birthrate_transition_slope | @[(min_birthrate-birthrate_at_transition)/(pop_growth_stable_sol-pop_growth_transition_sol)] |  |
| @birthrate_transition_intercept | @[-birthrate_transition_slope*pop_growth_stable_sol+min_birthrate] |  |
| ## Mortality from pop_growth_max_sol to pop_growth_stable_sol |  |  |
| @mortality_growth_max_to_stable_slope | @[(min_mortality-mortality_at_growth_max)/(pop_growth_stable_sol-pop_growth_max_sol)] |  |
| @mortality_growth_max_to_stable_intercept | @[-mortality_growth_max_to_stable_slope*pop_growth_stable_sol+min_mortality] |  |
| ### Pseudo algorithm to determine base Mortality / Birthrate |  |  |
| ## Mortality # if (sol < POP_GROWTH_EQUILIBRIUM_SOL) # { mortality = sol * POP_GROWTH_MORTALITY_STARVING_SLOPE + POP_GROWTH_MAX_MORTALITY } # else if (sol < POP_GROWTH_MAX_SOL) # { mortality = sol * POP_GROWTH_MORTALITY_EQUILIBRIUM_TO_GROWTH_MAX_SLOPE + POP_GROWTH_MORTALITY_EQUILIBRIUM_TO_GROWTH_MAX_INTERCEPT } # else if (sol < POP_GROWTH_STABLE_SOL) # { mortality = sol * POP_GROWTH_MORTALITY_GROWTH_MAX_TO_STABLE_SLOPE + POP_GROWTH_MORTALITY_GROWTH_MAX_TO_STABLE_INTERCEPT } # else { mortality = POP_GROWTH_MIN_MORTALITY } |  |  |
| ## Birthrate # if (sol < POP_GROWTH_EQUILIBRIUM_SOL) # { birthrate = sol * POP_GROWTH_BIRTHRATE_PRETRANSITION_SLOPE + POP_GROWTH_MAX_BIRTHRATE } # else if (sol < POP_GROWTH_TRANSITION_SOL) # { birthrate = sol * POP_GROWTH_BIRTHRATE_PRETRANSITION_SLOPE + POP_GROWTH_MAX_BIRTHRATE } # else if (sol < POP_GROWTH_STABLE_SOL) # { birthrate = sol * POP_GROWTH_BIRTHRATE_TRANSITION_SLOPE + POP_GROWTH_BIRTHRATE_TRANSITION_INTERCEPT } # else { birthrate = POP_GROWTH_MIN_BIRTHRATE } |  |  |

| Define | Default Value | Comment |
|---|---|---|
| ## Birthrate |  |  |
| POP_GROWTH_BIRTHRATE_PRETRANSITION_SLOPE | @birthrate_pretransition_slope |  |
| POP_GROWTH_BIRTHRATE_TRANSITION_SLOPE | @birthrate_transition_slope |  |
| POP_GROWTH_BIRTHRATE_TRANSITION_INTERCEPT | @birthrate_transition_intercept |  |
| ## Mortality |  |  |
| POP_GROWTH_MORTALITY_STARVING_SLOPE | @mortality_starving_slope |  |
| POP_GROWTH_MORTALITY_EQUILIBRIUM_TO_GROWTH_MAX_SLOPE | @mortality_equilibrium_to_growth_max_slope |  |
| POP_GROWTH_MORTALITY_EQUILIBRIUM_TO_GROWTH_MAX_INTERCEPT | @mortality_equilibrium_to_growth_max_intercept |  |
| POP_GROWTH_MORTALITY_GROWTH_MAX_TO_STABLE_SLOPE | @mortality_growth_max_to_stable_slope |  |
| POP_GROWTH_MORTALITY_GROWTH_MAX_TO_STABLE_INTERCEPT | @mortality_growth_max_to_stable_intercept |  |
| ## Base Values |  |  |
| POP_GROWTH_MIN_BIRTHRATE | @min_birthrate | # Minimum base birthrate per month (at POP_GROWTH_STABLE_SOL) |
| POP_GROWTH_MAX_BIRTHRATE | @max_birthrate | # Maximum base birthrate per month (at SOL = 0) |
| POP_GROWTH_MIN_MORTALITY | @min_mortality | # Minimum base mortality per month (at POP_GROWTH_STABLE_SOL) |
| POP_GROWTH_MAX_MORTALITY | @max_mortality | # Maximum base mortality per month (at SOL = 0) |
| ## SoL Thresholds |  |  |
| POP_GROWTH_EQUILIBRIUM_SOL | @pop_growth_equilibrium_sol | # Equilibrium is pops stop starving and where growth first becomes positive |
| POP_GROWTH_TRANSITION_SOL | @pop_growth_transition_sol | # Transition determines how long birthrate "lags" behind mortality before starting to drop. Setting to same as equilibrium leads to no "lag" (only matters for birthrate) |
| POP_GROWTH_MAX_SOL | @pop_growth_max_sol | # Growth Max is where net growth generally is at it's highest (only matters for mortality) |
| POP_GROWTH_STABLE_SOL | @pop_growth_stable_sol | # Stable is where birthrate and mortality stop changing and hit their minimum values |

### Events

| Define | Default Value | Dev Comment |
|---|---|---|
| DEFAULT_MONTHS_VALID | -1 | # months until it disappears, -1 = infinite |
| DEFAULT_GUI_WINDOW_TYPE | "event_window" | #Default gui window type for events |
| NUM_DAYS_TO_AUTO_OPEN_EVENT | 30 | # number of days before timeout to pop up the event window |

### Technology

| Define | Default Value | Dev Comment |
|---|---|---|
| TECH_SPREAD_RANDOM_RANGE | 0.5 | # How much can distribution of tech spread vary each week |
| TECH_AHEAD_OF_TIME_PENALTY_FACTOR | 0.25 | # For every tech in a previous era not already researched in this category, take this multiple of the cost as an additional penalty (multiplied by number of eras between the techs) |
| NATIONALISM_TECHNOLOGY_TYPE | "nationalism" | # Technology type for nationalism techs |
| PAN_NATIONALISM_TECHNOLOGY_TYPE | "pan-nationalism" | # Technology type for pan-nationalism techs |

### Characters

| Define | Default Value | Dev Comment |
|---|---|---|
| NUM_RANDOM_NAME_TRIES_FOR_UNIQUENESS | 3 | # When generating random names for characters, try this many times to find a unique name within the country [>=1] |
| SET_RULER_NUM_OPTIONS | 3 | # The number of potential rulers to generate for a country at game start |
| SET_RULER_POOL_SIZE | 7 | # The max number of potential rulers to generate for a country at game start |
| RULER_MIN_AGE_FOR_HEIR | 20 | # Before this age, don't randomly generate heirs for rulers |
| RULER_AGE_FOR_HEIR_CHANCE_BOOST | 30 | # A year after this age start boosting chance of heir generation |
| RULER_HEIR_GENERATION_CHANCE | 0.001 | # Per day |
| RULER_HEIR_CHANCE_BOOST_SCALE | 0.001 | # Added to RULER_HEIR_CHANCE_BOOST for each year after RULER_AGE_FOR_HEIR_CHANCE_BOOST |
| AGE_GENERATION_STARTVAL | 20 |  |
| AGE_GENERATION_DICE_ROLL_MAGNITUDE | 6 |  |
| AGE_GENERATION_NUM_DICE_ROLLS | 5 |  |
| RECRUIT_COMMANDER_NUM_OPTIONS | 3 |  |
| RECRUIT_COMMANDER_POOL_SIZE | 3 |  |
| RECRUIT_COMMANDER_VALUE_MARGINAL | -50 |  |
| RECRUIT_COMMANDER_VALUE_HISTORICAL | 50 | # Prioritize showing historical commanders |
| RECRUIT_COMMANDER_VALUE_AGE_MULT | 0.5 |  |
| RECRUIT_COMMANDER_VALUE_SAME_IGS | -40 |  |
| RECRUIT_COMMANDER_REMOVE_AGE | 55 | # removed from the recruit pool when they reach 55 years |
| COMMANDER_START_RANK | 1 |  |
| HIGHEST_PROMOTION_RANK | 5 |  |
| RULER_COMMANDER_START_RANK | 6 |  |
| MIN_POPULARITY | -100 |  |
| MAX_POPULARITY | 100 |  |
| POPULARITY_HATED_THRESHOLD | -50 |  |
| POPULARITY_DISLIKED_THRESHOLD | -25 |  |
| POPULARITY_LIKED_THRESHOLD | 25 |  |
| POPULARITY_LOVED_THRESHOLD | 50 |  |
| POPULARITY_AUTHORITY_FACTOR | 1 | # Popularity of ruler is multiplied by this when turned into Authority |
| ROLE_RULER | "character_role_ruler" | # Role that is assigned to ruler characters |
| ROLE_HEIR | "character_role_heir" | # Role that is assigned to heir characters |
| ROLE_IG_LEADER | "character_role_ig_leader" | # Role that is assigned to IG leader characters |
| DEFAULT_CHARACTER_ROLE | "character_role_politician" | # If set, characters that are generated without a role will get this role by default. Leave empty to have no default role. |
| DEFAULT_TITLE_PREPOSITION | "PREP_IN" | # If no title preposition is defined, this one is used |
| CHARACTER_HOME_STATE_HOMELAND_MIN_WEIGHT | 1000 | # A homeland state is always counted as having at least this amount of people of the culture when picking home states for characters |
| CHARACTER_HOME_STATE_TRY_EXCLUDE_STATE_WEIGHT | 0.001 | # States that we actively try to exclude when selecting a home state (for instance due to already being represented by a magnate when we are generating a new magnate) have their chance multiplied by this value |
| CHARACTER_HOME_STATE_CAPITAL_WEIGHT | 10.0 | # The capital's chance of being selected as the home state for a character is multiplied by this value |
| CHARACTER_TEMPLATE_CULTURE_ACCEPTED_THRESHOLD | 60 | # Minimum culture acceptance for a culture to be considered 'accepted' when using random_accepted |
| CHARACTER_TEMPLATE_RELIGION_ACCEPTED_THRESHOLD | 15 | # Minimum religion acceptance contribution for a religion to be considered 'accepted' when using random_accepted |
| MAX_LOYALTY | 100 |  |
| LOYALTY_FROM_IG_APPROVAL | 5 | # Characters loyalty from IG approval scales against this |
| LOYALTY_FROM_IG_APPROVAL_MIN | -50 | # Loyalty impact from IG approval cannot be below this |
| LOYALTY_FROM_IG_APPROVAL_MAX | 50 | # Loyalty impact from IG approval cannot be above this |
| LOYALTY_FROM_IDEOLOGY_ENACTED | 25 | # Character loyalty gain/loss from enacting law scales against this |
| LOYALTY_FROM_IDEOLOGY_ENACTING | 25 | # Character loyalty gain/loss from enacted laws scales against this |
| LOYALTY_FROM_IDEOLOGY_MIN | -50 | # Loyalty impact from personal ideology cannot be below this |
| LOYALTY_FROM_IDEOLOGY_MAX | 50 | # Loyalty impact from personal ideology cannot be above this |
| LOYALTY_UNCERTAIN_THRESHOLD | 25 |  |
| LOYALTY_NEUTRAL_THRESHOLD | 50 |  |
| LOYALTY_RELIABLE_THRESHOLD | 75 |  |
| LOYALTY_FAITHFUL_THRESHOLD | 100 |  |
| MAX_PROMINENCE | 100 |  |
| PROMINENCE_FROM_POPULARITY | 0.25 | # This much of popularity is converted into prominence |
| PROMINENCE_NOTEWORTHY_THRESHOLD | 10 |  |
| PROMINENCE_SIGNIFICANT_THRESHOLD | 25 |  |
| PROMINENCE_IMPORTANT_THRESHOLD | 50 |  |
| PROMINENCE_EMINENT_THRESHOLD | 75 |  |
| PROMINENCE_PREEMINENT_THRESHOLD | 100 |  |
| PROMINENCE_IG_MIN_MULTIPLIER | 0.05 | # If the multiplier from a character's prominence on prominence_ig_modifier is lower than this, set it to this |
| HISTORICAL_CHARACTER_IDEOLOGY_LEADER_FACTOR | 2.0 # When selecting IG leaders, multiply the weight from prominence for historical characters by this so they tend to get selected over randomly generated ones |  |
| HOLDING_TYPE_RANDOM_FACTOR | 1.0 # The higher this is, the more random holding type selection for magnates will be |  |
| HOLDING_REVENUE_SCALING_GDP_DIVISOR | 1250 # Country GDP is divided by this for purposes of scaling against the holding's revenue and applying the character_holding_revenue static modifier |  |
| HOLDING_REVENUE_SCALING_MIN | 0.2 | # Holding revenue scaling is never less than this |
| HOLDING_REVENUE_SCALING_MAX | 1.0 | # Holding revenue scaling is never more than this |
| AGITATOR_MOVEMENT_SUPPORT_LITERACY_WEIGHT | 0.75 | # The fraction of the agitator's added support that is scaled by the literacy rating of the pop |
| AGITATOR_MOVEMENT_SUPPORT_IG_MEMBERSHIP_WEIGHT | 0.75 | # The fraction of the agitator's added support that is scaled against fraction of members of the same IG in the pop |
| AGITATOR_MOVEMENT_SUPPORT_BASE_FACTOR | 15 | # Agitators add this much attraction to their movements (scaled by literacy/ig membership, base) |
| AGITATOR_MOVEMENT_SUPPORT_POPULARITY_FACTOR | 0.15 | # Agitators add this much attraction to their movements (scaled by literacy/ig membership and multiplied by popularity) |
| MIN_YEARS_OF_SERVICE_FOR_COMMANDER_IG_LEADER | 5 | # Commanders with less years of service than this will not be considered for IG leadership |
| # The below values are used to control when new politicians should be randomly generated into the character pool # The target value is the number of 'unemployed' politicians we want to hang around as potential new IG leaders # If the number of politician bums is below the target, we will try to create a new politician with an unrepresented ideology valid for the IG # Politicians generated from templates count towards but are not capped by these values |  |  |
| TARGET_NUM_POOL_POLITICIANS_POWERFUL_IG | 3 |  |
| TARGET_NUM_POOL_POLITICIANS_INFLUENTIAL_IG | 2 |  |
| TARGET_NUM_POOL_POLITICIANS_MARGINAL_IG | 0 |  |
| CHILD_TRAIT | "trait_child" | # This personality trait is used for characters below the age of 16 |
| ADULT_AGE | 16 | # Characters under this age have more limited options. For example they cannot become military leaders [>= 0] |
| OLD_AGE | 60 | # Characters above this age may get some specific traits and events [>= ADULT_AGE] |
| VOIDED_CHARACTER_DEFAULT_DURATION | 12 | # Default months a character will be in the void before being deleted |
| INHERIT_RECESSIVE_GENE_CHANCE | 0.25 | # Probability of a recessive gene being picked as an heir's dominant/recessive gene. Only used for portraits. |
| AGITATOR_EXPECTED_SPAWN_INTERVAL_0_LITERACY | 12 | # At 0% literacy, a new agitator is expected to spawn in a given country once every this many years. (supports decimal values) |
| AGITATOR_EXPECTED_SPAWN_INTERVAL_100_LITERACY | 2 | # At 100% literacy, a new agitator is expected to spawn in a given country once every this many years. (supports decimal values) |
| ### TRAIT GENERATION # Every week, a character's Expected Trait Value meter increases by the specified amount below depending on their role and what they're doing (Commanders also gain the Activity Level from their Orders) # Every week, a percentile die is rolled against ( Expected Trait Value meter - Current Trait Value . If the die rolls under the current value, a new random trait will be added, if a valid one exists. |  |  |
| WEEKLY_CONDITION_CHANCE | 0.03 | # The chance that a character will get a condition each week (1 = 1%) |
| MAX_EXPECTED_TRAIT_VALUE | 12.0 | # The maximum amount of Trait Value a character can develop normally (note: not adhered to by add_trait effect) |
| MAX_TRAITS_PERSONALITY | 2 | # The max amount of Personality Traits a character can develop normally (note: not adhered to by add_trait effect) |
| MAX_TRAITS_SKILL | 2 | # The max amount of Skill Traits a character can develop normally (note: not adhered to by add_trait effect) |
| MAX_TRAITS_CONDITION | 2 | # The max amount of Condition Traits a character can develop normally (note: not adhered to by add_trait effect) |
| TRAIT_GAIN_DIVISOR | 100.0 | # Final trait gain is always divided by this so we don't have to use all the decimals |
| DEFAULT_TRAIT_GAIN | 0.25 | # Every character's Expected Traits meter increases by this much per week by default |
| TRAIT_GAIN_POLITICIAN_POWERFUL | 0.1 | # Powerful Politicians Expected Traits meter increases by this much *extra* each week |
| TRAIT_GAIN_RULER | 0.1 | # Rulers Expected Traits meter increases by this much *extra* each week |
| TRAIT_GAIN_COMMANDER_RECRUITABLE | 0.05 | # Recruitable offer commanders Expected Traits meter increases by this much per week, overrides all other factors |
| TRAIT_GAIN_IN_EXILE_POOL | 0.1 | # Characters in the exile pool Expected Traits meter increases by this much per week, overrides all other factors |
| TRAIT_GAIN_VOIDED | 0.0 | # Voided characters Expected Traits meter increases by this much per week, overrides all other factors |
| # The following parameters determine how character life expectancy is calculated. The calculation is based on a normal distribution with parameters: # µ = CHARACTER_LIFE_EXPECTANCY_BASE_YEARS # σ = CHARACTER_LIFE_EXPECTANCY_STDDEV_YEARS # # While the mean of the distribution is fixed, the result is modified by the health value of the character. # The way character health affects the life expectancy is given by the formula ((h / bh) - 1) * d, where: # - h is the character health # - bh is the baseline health # - d is the value of CHARACTER_LIFE_EXPECTANCY_DELTA_YEARS # # (h / bh) - 1 is the "distance to baseline health" of the character. For each point of distance away from baseline, a character will live CHARACTER_LIFE_EXPECTANCY_DELTA_YEARS more or less. # # Since the domain of the normal distribution is [-∞; +∞], we establish a hard cutoff defined by CHARACTER_LIFE_EXPECTANCY_CUTOFF. This value is expressed in σ, or standard deviations away from the mean. # It is recommended to leave that value to 3, as 99.73% of values of the ditribution fall in the range [-3σ; +3σ]. # Because of the above, with default values a character with 0 health will die between the ages of 50 and 80, while a character with 2 health will die between the ages of 70 and 100. # # NOTE: due to some performance optimizations, changing these values will either have no effect or unexpected behaviour until the game is restarted, even if they are hot reloaded. |  |  |
| MIN_CHARACTER_HEALTH | 0.0 | # Baseline is 1.0 (meaning 100%), defined in the base_values modifier. 0.0 means -100% from baseline. [any value] |
| MAX_CHARACTER_HEALTH | 2.0 | # Baseline is 1.0 (meaning 100%), defined in the base_values modifier. 2.0 means +100% from baseline. [>= MIN_CHARACTER_HEALTH] |
| CHARACTER_LIFE_EXPECTANCY_BASE_YEARS | 75 | # The median life expecancy in years at baseline health. It's the µ parameter of the normal distribution [> 0] |
| CHARACTER_LIFE_EXPECTANCY_STDDEV | 5 | # The standard deviation for the life expectancy distribution. It's the σ parameter [> 0] |
| CHARACTER_LIFE_EXPECTANCY_CUTOFF | 3 | # We clamp the distribution between this amount of σ in both directions. A range of [-3σ; +3σ] accounts for 99.73% of values. [> 0] |
| CHARACTER_LIFE_EXPECTANCY_DELTA_YEARS_BELOW_BASELINE | 30 | # Random base for years that life expectancy is decreased by, for every point of distance below baseline health [>= 0] |
| CHARACTER_LIFE_EXPECTANCY_DELTA_YEARS_ABOVE_BASELINE | 15 | # Random base for years that life expectancy is increased by, for every point of distance above baseline health [>= 0] |
| # Random base for life expectancy delta yearsis multiplied by a random range of lerp(CHARACTER_LIFE_EXPECTANCY_DELTA_LERP_LOWER_BOUND, CHARACTER_LIFE_EXPECTANCY_DELTA_LERP_UPPER_BOUND) |  |  |
| CHARACTER_LIFE_EXPECTANCY_DELTA_LERP_LOWER_BOUND | 0.5 |  |
| CHARACTER_LIFE_EXPECTANCY_DELTA_LERP_UPPER_BOUND | 1.5 |  |
| GUARANTEED_SURVIVABILITY_DAYS_MIN | 30 | # A character that stops being immortal and that should have died when it happens will instead live at least this amount of days, to avoid situations like a character dieing immediately upon finishing an expedition [>= 0] |
| GUARANTEED_SURVIVABILITY_DAYS_MAX | 180 | # As above, but the upper limit of the range [>= GUARANTEED_SURVIVABILITY_DAYS_MIN] |
|  |  | ## Interactions |
| INTERACTION_INVITE_EXILE | "invite_exile" |  |
|  |  | ## Career Length |
| HISTORICAL_CAREER_LENGTH_MULT | 1.5 | # Historical characters have this multiplier on career length |

### Battle

| Define | Default Value | Dev Comment |
|---|---|---|
| CASUALTY_MAJORITY_CULTURE_WEIGHT | 1.5 | # Majority culture pops will be weighted to take 1.5x more casualties |
| CASUALTY_ROLL_MIN | 50 | # min ... |
| CASUALTY_ROLL_MAX | 200 | # max amount of casualties a unit can take each roll when applying casualties to units |
| SURVIVAL_RATE | 0.66 |  |
| DEPENDENTS_ROLL_MIN_PERCENT | 0.1 | # min ... |
| DEPENDENTS_ROLL_MAX_PERCENT | 0.3 | # max percentage of Pops Size it can take as Dependents each roll |
| MIN_DEPENDENTS_PER_ROLL | 25 | # Minimum amount of dependents to added to a random pop |
| ESCAPE_PROGRESS_REQUIRED_MIN | 10.0 | # How much progress is needed for a formation to escape from battle |
| ESCAPE_PROGRESS_REQUIRED_PER_MANPOWER | 0.001 | # 1 battalion or ship increases the needed progress to escape by this |
| ESCAPE_PROGRESS_GAIN_BASE | 1.0 | # How much progress is increased per each battle round as base value |
| ESCAPE_PROGRESS_GAIN_RANDOM_FACTOR | 2.5 | # The higher this is, the more random progress changer will be per round |
| CHANCE_OF_POPULARITY_NARROW_VICTORY | 0.5 | # The chance (0-1) to be affected by popularity for a narrow victory (start with numeric advantage, end with numeric disadvantage) |
| CHANCE_OF_POPULARITY_NORMAL_VICTORY | 0.1 | # The chance (0-1) to be affected by popularity for a normal victory (any victory that's not narrow or heroic) |
| CHANCE_OF_POPULARITY_HEROIC_VICTORY | 1.0 | # The chance (0-1) to be affected by popularity for a heroic victory (start with numeric disadvantage against a more prestigious nation) |
| POPULARITY_GAIN_NARROW_VICTORY | 10 | # Multiple of commander_battle_end_victory modifier the winner should get for a narrow victory if the random chance roll is true |
| POPULARITY_GAIN_NORMAL_VICTORY | 5 | # Multiple of commander_battle_end_victory modifier the winner should get for a normal victory if the random chance roll is true |
| POPULARITY_GAIN_HEROIC_VICTORY | 20 | # Multiple of commander_battle_end_victory modifier the winner should get for a heroic victory if the random chance roll is true |
| POPULARITY_GAIN_NARROW_LOSS | -10 | # Multiple of commander_battle_end_loss modifier the loser should get for a narrow victory for the other side if the random chance roll is true |
| POPULARITY_GAIN_NORMAL_LOSS | -5 | # Multiple of commander_battle_end_loss modifier the loser should get for a normal victory for the other side if the random chance roll is true |
| POPULARITY_GAIN_HEROIC_LOSS | -20 | # Multiple of commander_battle_end_loss modifier the loser should get for a heroic victory for the other side if the random chance roll is true |
| POPULARITY_DECAY_MONTHS | 30 | # The number of months battle popularity modifiers decay over |
| SHIP_BATTLE_DAYS_BETWEEN_UPDATES | 5 | # The number of days between updates of a naval battle involving individual ships |
| SHIP_BATTLE_DESTROYED_SHIP_RATIO_RESIGN_THRESHOLD | 0.5 | # The ratio of destroyed to originally active ships before a fleet resigns, when using individual ships |
| SHIP_REQUIRED_READINESS_TO_ACT | 100.0 | # How much readiness a ship needs to get up to before it can e.g. attack or withdraw |
| SHIP_DEFAULT_READINESS_GAIN | 10 | # Default gain if not specified on template |
| SHIP_INITIAL_READINESS | 0.0 | # What readiness a ship has at the start of combat |
| SHIP_ATTACK_BASE_MISS_CHANCE | 0.2 | # Base chance for a ship to miss its attack against another ship. This is further modified by a ship's accuracy |
| SHIP_ATTACK_MIN_MISS_CHANCE | 0.01 | # Minimum miss chance when a ship attacks |
| SHIP_WITHDRAW_BASE_CHANCE | 0.5 | # Base chance for a ship to successfully escape. The ship's speed is added to this. |
| SHIP_WITHDRAW_SPEED_FACTOR | 1.0 | # Factor on speed when it's modifying withdraw chance. |
| ###### Withdraw Desire Calculation ###### ## Withdraw desire = ( Damage Desire + Zero Damage Hit Ratio Desire ) * ( 1 + Overwhelming Odds Desire + Exposed Desire + Raiding Desire ) # given that each term is applicable |  |  |
| SHIP_LIGHT_DAMAGE | 0.8 | # Damage thresholds on ships for different behaviors |
| SHIP_MODERATE_DAMAGE | 0.5 |  |
| SHIP_SEVERE_DAMAGE | 0.25 |  |
| SHIP_WITHDRAW_DESIRE_LIGHT_DAMAGE | 0.05 | # Chance for the ship to attempt withdrawing from a battle based on damage taken |
| SHIP_WITHDRAW_DESIRE_MODERATE_DAMAGE | 0.20 |  |
| SHIP_WITHDRAW_DESIRE_SEVERE_DAMAGE | 0.80 |  |
| OVERWHELMING_ODDS_POWER_RATIO | 0.5 | # Power Ratio = Our Power / Enemy Power. If Power Ratio is below this threshold, the battle is considered to have overwhelming odds for the enemy and makes ships more likely to withdraw from battle |
| SHIP_WITHDRAW_DESIRE_OVERWHELMING_ODDS_BASE | 0.1 | # If our power ratio is lower than OVERWHELMING_ODDS_POWER_RATIO, we start adding this much to the ship's desire to withdraw. As the power ratio gets lower, we lerp the added withdraw desire up to SHIP_WITHDRAW_DESIRE_OVERWHELMING_ODDS_MAX |
| SHIP_WITHDRAW_DESIRE_OVERWHELMING_ODDS_MAX | 0.5 | # The maximum added withdraw desire at a theoretical 0 power ratio |
| PRIORITY_SHIPS_EXPOSED_THRESHOLD | 0.5 | # If the battle side's ratio of total vulnerability / total screening is less than this, the side is considered to have it's priority ships exposed |
| PRIORITY_SHIP_WITHDRAW_DESIRE_MULT_PRIORITY_SHIPS_EXPOSED | 0.2 | # If our priority ships are exposed, multiply the desire to withdraw by this for our priority ships |
| SCREENING_SHIP_WITHDRAW_DESIRE_MULT_PRIORITY_SHIPS_EXPOSED | -0.2 # If our priority ships are exposed, multiply the desire to withdraw by this for our screening ships |  |
| PRIORITY_SHIPS_EXPOSED_FOR_RAIDING_THRESHOLD | 0.25 | # For raiding fleets, if the enemy's ratio of total vulnerability / total screening is less than this, the side is considered exposed. |
| RAIDING_SHIP_WITHDRAW_DESIRE_MULT_PRIORITY_SHIPS_EXPOSED | 0.25 | # For raiding fleets, if the enemy is not exposed, multiply the desire to withdraw by this |
| ZERO_DAMAGE_HIT_RATIO_THRESHOLD | 0.5 | # For each side of the battle, if the number of hits that deal zero damage through the total number of hits ratio exceeds this threshold, we apply a bonus to the withdrawal chance |
| MIN_ATTACKS_ZERO_DAMAGE_HIT_PENALTY | 50 | ) |
| SHIP_WITHDRAW_DESIRE_HIGH_ZERO_DAMAGE_HIT_RATIO | 0.1 | # If too many zero damage hits are being dealt by our side, add this much to the withdraw desire |
| FLEET_UNCONNECTED_MISSION_AREA_TIMEOUT_DAYS | 30 | # Number of days that a mission area is allowed to be invalid/unconnected before it gets cleaned up |
| FLEET_INTERCEPT_CHANCE_BASE | 10.0 | # The chance (0-100) that a fleet will intercept as a base |
| FLEET_RAID_SUPPLY_CHANCE_BASE | 10.0 | # The chance (0-100) that a fleet will raid supply as a base |
| NAVAL_BATTLE_LOG_INITIAL_SIZE_FACTOR | 8 | # Initial reserved log size factor. This is multiplied by the number of ships in a battle to estimate number of entries needed. Too large a value and you allocate too much data, too little and you need to expand the array multiple times which is slow. |
| NAVAL_BATTLE_LOG_ENTRIES_PER_PAGE | 20 | # Number of naval battle log entries shown per page in the battle log UI. |
| NAVAL_BATTLE_CONDITION_DAMAGE_RANGE | 0.25 | # When a naval battle condition applies damage to a ship, the actual damage will be in a range from (1 - this) * damage to (1 + this) * damage |
| DEFAULT_NAVAL_BATTLE_CONDITION_TYPE | "naval_condition_calm_waters" | # If a naval battle is not able to select a valid condition due to all weights being 0 or something, it will override the selection to use this battle condition. This is a backup though and ideally all battle conditions should have a non-zero weight and there should always be at least one possible condition |
| HIGHLIGHTED_EVENT_INTERVAL_TURNS | 8 | # Battle turns between highlighted event re-evaluations |
| HIGHLIGHTED_EVENT_LOOKBACK_COUNT | 10 | # Max number of new log entries to consider per evaluation |
| HIGHLIGHTED_EVENT_WEIGHT_DAMAGE | 1.0 | # Weight multiplied by total damage (hull + crew) when scoring log entries |
| HIGHLIGHTED_EVENT_WEIGHT_FLAGSHIP | 500.0 | # Bonus weight added if a flagship is involved in the log entry |
| HIGHLIGHTED_EVENT_WEIGHT_SINK | 100.0 | # Bonus weight added if a ship was sunk in the log entry |

### War

| Define | Default Value | Dev Comment |
|---|---|---|
| DEVASTATION_MAX | 100.0 |  |
| DEVASTATION_INCREASE_RATE | 0.1 | # Per day, scales with level of occupation |
| DEVASTATION_DECAY_RATE | -0.0.25 | # Per day, when there are no occupations |
| DEVASTATION_FROM_BATTLES | 0.1 | # For each battle |
| AUTO_CAPITULATE_WAR_SUPPORT | -100 | # When war support is this low, the country will auto capitulate |
| DAYS_BETWEEN_WAR_EXHAUSTION | 7 | # Every this many days war support will be reduced by the war exhaustion formula |
| WAR_EXHAUSTION_BASE | 0.2 |  |
| WAR_EXHAUSTION_KIA_FACTOR | 4.0 | # Scaled by casualties compared to total manpower |
| WAR_EXHAUSTION_KIA_BASE_MULTIPLIER | 0.25 | # War Exhaustion from casualties is always multiplied by at least this |
| WAR_EXHAUSTION_KIA_BATTLES_LOST_MULTIPLIER | 0.75 | # At 100% of battles lost by our side, War Exhaustion from casualties is further multiplied by this |
| WAR_EXHAUSTION_TURMOIL_FACTOR | 1.5 | # At 100% turmoil |
| WAR_EXHAUSTION_CONTESTED_ENEMY_WARGOALS | 1.0 |  |
| WAR_EXHAUSTION_ANTI_WAR_LOBBY_CLOUT_FACTOR | 1.0 | # At 100% lobby clout opposed to the war |
| WAR_EXHAUSTION_PRO_WAR_LOBBY_CLOUT_FACTOR | -1.0 | # At 100% lobby clout supporting to the war |
| WAR_EXHAUSTION_MAX | 100 | # War Exhaustion can never exceed this |
| WAR_EXHAUSTION_MIN | 0 | # War Exhaustion can never go below this |
| OCCUPATION_STATE_BASE_WEIGHT | 1 |  |
| OCCUPATION_STATE_POP_WEIGHT | 1 |  |
| OCCUPATION_STATE_INCORPORATED_WEIGHT | 10 |  |
| OCCUPATION_STATE_DEFENSIVE_BATTLE_VICTORY_SCORE | 50 | # How many occupation "points" each country receives after winning a defensive battle |
| OCCUPATION_STATE_CLEAR_OCCUPATION_FRACTION | 0.5 | # Fraction of occupation score dedicated to clear occupation from your own States (if any). |
| LAND_INVASION_TRAVEL_TIME_LIMIT_DAYS | 30 | # How many days formation can travel at most for a land invasion |
| LAND_INVASION_PREPARATION_DURATION_DAYS | 14 | # How many days should pass since the first army arrived to the invasion front to start advancing it |
| NAVAL_INVASION_PREPARATION_DURATION_DAYS | 14 | # How many days should pass since the first army arrived to the naval invasion front to start advancing it without the sea node being blocked by enemy fleet |
| LAND_INVASION_MAX_LAND_BATTLE_DEFEATS_AT_ZERO_OCCUPATION | 3 | # At this number of land defeats with zero occupation you fail the invasion |
| NAVAL_INVASION_MAX_LAND_BATTLE_DEFEATS_AT_ZERO_OCCUPATION | 3 | # At this number of land defeats with zero occupation you fail the naval invasion. |
| NAVAL_INVASION_MIN_POWER_PROJECTION_RATIO_TO_BLOCK_LANDING | 0.25 | # How powerful a fleet must be to be considered as "blocking" a naval invading flee |
| STATE_CONQUEST_HOMELAND_AND_CLAIM_RADICALIZATION | 0.1 |  |
| STATE_CONQUEST_HOMELAND_AND_CLAIM_DEMILITARIZATION | 0.25 |  |
| STATE_CONQUEST_HOMELAND_OR_CLAIM_RADICALIZATION | 0.3 |  |
| STATE_CONQUEST_HOMELAND_OR_CLAIM_DEMILITARIZATION | 0.5 |  |
| STATE_CONQUEST_DEFAULT_RADICALIZATION | 0.5 |  |
| STATE_CONQUEST_DEFAULT_DEMILITARIZATION | 0.75 |  |
| STATE_PEACEFUL_ANNEXATION_RADICALIZATION_FACTOR | 0.25 | # If the state was annexed due to an accepted diplomatic demand by the overlord, multiply by this |
| STATE_CONQUEST_KEEP_ALL | 0.0 |  |
| NUM_PROVINCES_FOR_ADVANCEMENT_SELECTION | 5 | # After having computed weights for possible advancement provinces using front_battle_province_weight, filter out all but the X top weighted provinces. This is done to prevent randomly selecting an element that had a low weight. |

### TravelNetwork

| Define | Default Value | Dev Comment |
|---|---|---|
| ARMY_CONNECTION_UNDEVELOPED_COST_MULT | 2.0 | # Travel cost multiplier for undeveloped land connections |
| ARMY_CONNECTION_UNDEVELOPED_HARSH_COST_MULT | 4.0 | # Travel cost multiplier for undeveloped land connections in harsh environments (deserts, mountains, etc) |
| ARMY_CONNECTION_DIRT_ROAD_COST_MULT | 1.5 | # Travel cost multiplier for dirt road land connections |
| ARMY_CONNECTION_HARDENED_ROAD_COST_MULT | 1.25 | # Travel cost multiplier for hardened road land connections |
| ARMY_CONNECTION_RAILWAY_COST_MULT | 1.0 | # Travel cost multiplier for railway land connections |
| ARMY_CONNECTION_CHARTED_COST_MULT | 1.0 | # Travel cost multiplier for ocean/coastal water connections |
| ARMY_CONNECTION_CANAL_COST_MULT | 1.0 | # Travel cost multiplier for channel water connections |
| ARMY_CONNECTION_STRAIT_CROSSING_COST_MULT | 4.0 | # Travel cost multiplier for strait-crossing connection |
| ARMY_DIRECT_CONNECTION_COST_MULT | 10.0 | # Travel cost multiplier for traveling in a direct line from/to a position on the map (without a travel node connection) |
| ARMY_CONNECTION_DOCKING_COST | 300 | # Fixed docking/undocking cost for going from a harbor node to a port node (overrides docking connection length) |
| ARMY_CONNECTION_STRAIT_CROSSING_COST | 100 | # Fixed additional cost for crossing a strait connection |
| FLEET_CONNECTION_UNDEVELOPED_COST_MULT | 100.0 | # Travel cost multiplier for undeveloped land connections (unused by fleets) |
| FLEET_CONNECTION_UNDEVELOPED_HARSH_COST_MULT | 100.0 | # Travel cost multiplier for undeveloped land connections in harsh environments (deserts, mountains, etc) (unused by fleets) |
| FLEET_CONNECTION_DIRT_ROAD_COST_MULT | 100.0 | # Travel cost multiplier for dirt road land connections (unused by fleets) |
| FLEET_CONNECTION_HARDENED_ROAD_COST_MULT | 100.0 | # Travel cost multiplier for hardened road land connections (unused by fleets) |
| FLEET_CONNECTION_RAILWAY_COST_MULT | 100.0 | # Travel cost multiplier for railway land connections (unused by fleets) |
| FLEET_CONNECTION_CHARTED_COST_MULT | 1.0 | # Travel cost multiplier for ocean/coastal water connections |
| FLEET_CONNECTION_CANAL_COST_MULT | 1.0 | # Travel cost multiplier for channel water connections |
| FLEET_CONNECTION_STRAIT_CROSSING_COST_MULT | 100.0 | # Travel cost multiplier for strait-crossing connection (unused by fleets) |
| FLEET_DIRECT_CONNECTION_COST_MULT | 4.0 | # Travel cost multiplier for traveling in a direct line from/to a position on the map (without a travel node connection) |
| FLEET_CONNECTION_DOCKING_COST | 10 | # Fixed docking/undocking cost for going from a harbor node to a port node (overrides docking connection length) |
| FLEET_CONNECTION_STRAIT_CROSSING_COST | 100 | # Fixed additional cost for crossing a strait connection (unused by fleets) |
| DIRECT_CONNECTION_NODE_MAX_NODES | 10 | # Only search the closest X travel nodes for direct line map travel |
| DIRECT_CONNECTION_NODE_SEARCH_DISTANCE | 1200 | # Default distance allowed to pathfind in a direct line from a (start/target) map point to a travel node (if no valid are found, it is expanded) |
| DIRECT_CONNECTION_MAP_MAX_DISTANCE | 200 | # Maximum distance allowed to pathfind in a direct line between start and target map points directly |
| STRAIT_CROSSING_NODE_CREATION_DISTANCE | 5 | # Minimum distance between travel nodes, when considering to insert a new travel node for strait-connection |
| FORMATION_REPATH_MAX_DAYS_EXTRA | 60 | # Maximum nr of days an automatic formation re-pathing may take (when travel access changes in ongoing travel) |
| HARSH_ENVIRONMENT_TERRAIN_LABEL | "label_travel_harsh_environment" | # Terrain label which marks nodes in them as being in harsh environment, triggering 'UNDEVELOPED_HARSH' connection type |
| PAVED_ROAD_TECH | "paved_roads" | # Technology required for paved roads |
| PAVED_ROAD_MIN_INFRASTRUCTURE | 500.0 | # Minimum infrastructure for paved roads |

### HarvestConditions

| Define | Default Value | Dev Comment |
|---|---|---|
| HARVEST_CONDITION_CHANCE_THRESHOLD | 0.2 | # If the rolled value is higher than that we early out and skip the chance calculations |
| HARVEST_CONDITION_PERIOD | 3 | # At what period in months do we check each state to spawn harvest conditions. 1 = all states are checked every month, 3 = all states are checked over three months |

### Text

| Define | Default Value | Dev Comment |
|---|---|---|
| DURATION_SHOW_YEARS_THRESHOLD | 1105 | # Duration will show as years if it's at least this many days |
| DURATION_SHOW_MONTHS_THRESHOLD | 100 | # Duration will show as months if it's at least this many days |
| DURATION_SHOW_WEEKS_THRESHOLD | 15 | # Duration will show as weeks if it's at least this many days |

### Debug

| Define | Default Value | Dev Comment |
|---|---|---|
| CASUALTY_LOG_EXPIRE_TIME_DAYS | 30 | # Casualty log for units and buildings will be cleaned after this amount of days |
| CASUALTY_LOG_NUM_LAST_ENTRIES_VISIBLE | 10 | # Max amount of casualty events that are shown in casualty log lists |
| OCCUPATION_TOOL_DELTA | 0.25 | # How much occupation percentage is increased/decreased by OccupationTool |

## 00_ai

### AI

Defines affecting AI behavior.

| Define | Default Value | Dev Comment |
|---|---|---|
| DEFAULT_STRATEGY_STRING | "ai_strategy_default" |  |
| STRATEGY_RANDOM_FACTOR | 20.0 | # The higher this is, the more random AI strategy selection will be |
| TICKS_FOR_FULL_SPENDING_VARIABLES_UPDATE | 100 | # The higher this is, the less often AIs will fully refresh their spending variables |
| NUM_FAILED_MONEY_SPENDING_ATTEMPTS_FOR_UPDATE | 50 | # After this many failed attempts to change money spending/construct government buildings, force an update of money spending priorities |
| NUM_FAILED_AUTHORITY_SPENDING_ATTEMPTS_FOR_UPDATE | 20 | # After this many failed attempts to change authority spending, force an update of authority spending priorities |
| # When a potential AI building spending has its state calculcated, add a randomly set number of ticks between these two values for when to update it again # Before this amount of ticks has passed, unless there is a specific reason to update the state, we only update the score and keep the state the same |  |  |
| MIN_TICKS_TO_UPDATE_BUILDING_SPENDING_STATE | 100 |  |
| MAX_TICKS_TO_UPDATE_BUILDING_SPENDING_STATE | 200 |  |
| MIN_SUBJECT_TYPE_VALUE | 1 | # ai_value for a subject type is never below this |
| GOVERNMENT_MONEY_SPENDING_ENABLED | yes | # If this is set to no, the AI for government money spending will be disabled |
| GOVERNMENT_AUTHORITY_SPENDING_ENABLED | yes | # If this is set to no, the AI for authority spending will be disabled |
| TAX_LEVEL_CHANGES_ENABLED | yes | # If this is set to no, the AI will not change its tax levels (but might still use consumption taxes if GOVERNMENT_AUTHORITY_SPENDING_ENABLED = yes) |
| PRODUCTION_BUILDING_CONSTRUCTION_ENABLED | yes | # If this is set to no, the country-level AI will not construct any production buildings |
| AUTONOMOUS_INVESTMENT_CONSTRUCTION_ENABLED | yes | # If this is set to no, the autonomous investment AI won't construct anything even if the game rule for it is enabled |
| CHANGE_STRATEGY_THRESHOLD | 100 | # At this threshold of 'change points', the AI will roll a new strategy |
| CHANGE_STRATEGY_INCREASE_WEEKLY_CHANCE | 20 | # Chance per week of AI gaining a 'change point' towards rolling a new strategy (1 = 1%) |
| CHANGE_STRATEGY_POLITICAL_NEW_RULER | 100 | # How many 'change points' are added to each strategy when a country gets a new ruler |
| CHANGE_STRATEGY_POLITICAL_REGIME_CHANGE | 100 | # How many 'change points' are added to each strategy when a country is the target of a regime change |
| CHANGE_STRATEGY_POLITICAL_LAW_ENACTED | 25 | # How many 'change points' are added to politics strategy when a law is enacted |
| CHANGE_STRATEGY_DIPLOMATIC_STATE_GAINED_OR_LOST | 10 | # How many 'change points' are added to diplomatic strategy when a state is acquired or lost |
| CHANGE_STRATEGY_DIPLOMATIC_UNIFICATION_CANDIDATE | 100 | # How many 'change points' are added to diplomatic strategy when we become or stop being a unification candidate |
| CHANGE_STRATEGY_DIPLOMATIC_LIBERTY_DESIRE_CHANGE | 2 | # How many 'change points' are added to diplomatic strategy when liberty desire changes (multiplied by size of the change) |
| COUNTRY_GOAL_STRATEGIC_UPDATE_COUNT | 5 | # How many AIs have their protector scores set every day |
| COUNTRY_GOAL_ADJUSTMENT_UPDATE_COUNT | 50 | # How many AIs have their antagonize/befriend/threat scores, neighbor/relevance status and attitude adjusted each day |
| DECLARE_BANKRUPTCY_MIN_DAYS_IN_DEFAULT | 30 | # After this many days in default, the AI will declare bankruptcy |
| DECLARE_BANKRUPTCY_COOLDOWN_DAYS | 365 | # If AI declares bankruptcy, don't do it again for this many days as chain bankruptcies will radicalize everyone |
| BASE_AGGRESSION | 0.25 | # Base chance that AI will consider starting a diplo play each time the goal is checked (1 = 1%) |
| UNIFICATION_AGGRESSION_MULT_HIGHER_TIER | 20 | # AI aggression is multiplied by this for calculating whether they should try to start a unification/leadership play, if the country would end up forming a nation of a higher tier |
| UNIFICATION_AGGRESSION_MULT_SAME_TIER | 0.1 | # AI aggression is multiplied by this for calculating whether they should try to start a unification/leadership play, if the country would end up forming a nation of the same tier |
| DIPLO_PROPOSAL_DAYS_LEFT_MAX | 28 | # AI will not answer a proposal when it has more than this amount of days left (should map to DIPLOMATIC_ACTION_PENDING_APPROVAL_DAYS) |
| DIPLO_PROPOSAL_DAYS_LEFT_MIN | 20 | # AI will always answer a proposal when it has this or less amount of days left (should map to DIPLOMATIC_ACTION_PENDING_APPROVAL_DAYS) |
| DIPLO_PROPOSAL_ANSWER_CHANCE | 5 | # Chance per tick of AI answering a proposal (1 = 1%) |
| DIPLO_PROPOSAL_TO_PLAYER_COOLDOWN_MONTHS | 120 | # Do not make the same exact proposal to the player for this amount of months |
| DIPLO_PROPOSAL_LIKELY_NON_ACCEPTED_COOLDOWN_MONTHS | 120 | # When AI rolls the dice on whether or not to attempt a proposal it thinks will be rejected, don't try again for this time |
| DIPLO_PROPOSAL_LIKELY_NON_ACCEPTED_TREATY_COOLDOWN_MONTHS | 12 | # When AI fails to propose a treaty to another AI, wait this long before trying again with the same country |
| DIPLO_PROPOSAL_NO_OBLIGATION_COOLDOWN_MONTHS | 120 | # If the AI decides not to offer an obligation for a proposal, remember that decision for this many months |
| DIPLO_PROPOSAL_ACCEPT_THRESHOLD | 1 | # At this or more acceptance on a diplomatic action without uses_random_approval flag, AI says yes to a proposal. Each point above it increases chance to accept a uses_random_approval or treaty proposal |
| DIPLO_PROPOSAL_HALFWAY_RANDOM_ACCEPTANCE_THRESHOLD | 10 | # At this or more acceptance on a diplomatic action with uses_random_approval flag or treaty proposal, the AI has 50% chance to accept it and considers it to be accepted for the purpose of proposing it |
| DIPLO_PROPOSAL_GUARANTEED_RANDOM_ACCEPTANCE_THRESHOLD | 30 | # At this or more acceptance on a diplomatic action or treaty proposal with uses_random_approval flag, the AI will always accept it |
| DIPLO_PROPOSAL_BREAK_THRESHOLD | -100 | # At this or less acceptance, AI breaks off an existing pact |
| DIPLO_PROPOSAL_TRANSFER_PACT_RELUCTANCE | 25 | # Add this to acceptance value for existing pact in transfer-pact proposals |
| OBLIGATION_RECENTLY_REPUDIATED_DESIRE_MULT | 0.1 | # Multiply AI's desire for an obligation by this if the offering country has recently repudiated another obligation |
| DIPLO_ACCEPTANCE_CALL_IN_OBLIGATION | 50 | # Add this acceptance to diplo action when calling in an obligation |
| DIPLO_ACCEPTANCE_CALL_IN_OBLIGATION_RECENTLY_REPUDIATED | 25 | # Add this acceptance instead of the above to diplo action when calling in an obligation if we've recently repudiated another obligation |
| DIPLO_BREAK_PACT_WEIGHT | 1000 |  |
| DIPLOMATIC_DEMAND_ALWAYS_ACCEPT_THRESHOLD | 100 | # At this amount of acceptance, the AI will always give in to diplomatic demands. If it's less than this but above 0, there is a scaled random chance of accepting. |
| DIPLOMATIC_DEMAND_DAYS_LEFT_MAX | 13 | # AI will not answer a demand when it has more than this amount of days left (should map to DIPLOMATIC_DEMAND_PENDING_APPROVAL_DAYS) |
| DIPLOMATIC_DEMAND_DAYS_LEFT_MIN | 7 | # AI will always answer a demand when it has this or less amount of days left (should map to DIPLOMATIC_DEMAND_PENDING_APPROVAL_DAYS) |
| DIPLOMATIC_DEMAND_ANSWER_CHANCE | 10 | # Chance per tick of AI answering a demand (1 = 1%) |
| DIPLOMATIC_DEMAND_ACCEPTANCE_BASE | -50 |  |
| DIPLOMATIC_DEMAND_ACCEPTANCE_WARGOAL_IMPACT | -1 | # Scales with maneuver cost of demanded wargoal |
| DIPLOMATIC_DEMAND_ACCEPTANCE_MILITARY_POWER_SCALE | 4.0 | # At this amount of relative expected military power, max/min value of DIPLOMATIC_DEMAND_ACCEPTANCE_MILITARY_POWER_FACTOR is applied |
| DIPLOMATIC_DEMAND_ACCEPTANCE_MILITARY_POWER_FACTOR | 100 | # Scales with relative expected military power of the demanding country in a potential play, maximum is this value and minimum is this value * -1 |
| DIPLOMATIC_DEMAND_ACCEPTANCE_INCORPORATED_STATE_FACTOR | -25 | # Added to acceptance if the wargoal is demanding they cede an incorporated state |
| DIPLOMATIC_DEMAND_ACCEPTANCE_SUBJUGATION_FACTOR | 0.5 | # Multiplied by country's desire to become a subject of the specified type if the wargoal is demanding subjugation |
| DIPLOMATIC_DEMAND_ACCEPTANCE_ANNEXATION_FACTOR | -75 | # Added to acceptance if the wargoal is demanding their full annexation |
| DIPLOMATIC_DEMAND_ACCEPTANCE_LOYAL_SUBJECT_FACTOR | 75 | # Added to acceptance for demands by overlords against loyal subjects |
| INFLUENCE_DEFICIT_RECOVER_INFLUENCE_BASE_VALUE | 50 | # Added to score for the treaty or pact we're breaking to recover influence |
| INFLUENCE_DEFICIT_RECOVER_INFLUENCE_RANDOM_FACTOR | 1.0 | # The higher this is, the more random AI pact/treaty breaking due to influence deficit will be |
| INFLUENCE_DEFICIT_RECOVER_INFLUENCE_OVER_SPENDING_LIMIT_MULT | 0.1 | # AI multiplies the value of pacts that are over their action-type spending limit by this when in an Influence deficit |
| MIN_AVAILABLE_LABOR_FOR_NEW_BUILDING | 5000 | # If state has less than this in available labor, we should be much less likely to build something (multiplied by 1 + number of ongoing constructions) |
| # Formations with fewer units than whichever is smaller of these three values should not have a commander recruited for them |  |  |
| MIN_COMBAT_UNITS_FOR_COMMANDER_ABSOLUTE | 5 | # Absolute number of combat units |
| MIN_COMBAT_UNITS_FOR_COMMANDER_ABSOLUTE_MARINES | 3 | # Absolute number of combat units in a marine-tagged formation, less than or equal to the above |
| MIN_COMBAT_UNITS_FOR_COMMANDER_RELATIVE | 0.2 | # Number of combat units relative to total army size |
| # Formations with at least the number of units than whichever is smaller of these two values should always have at least two commanders, so they can be dynamically split to cover multiple fronts |  |  |
| MIN_COMBAT_UNITS_FOR_MULTIPLE_COMMANDERS_ABSOLUTE | 10 | # Absolute number of combat units |
| MIN_COMBAT_UNITS_FOR_MULTIPLE_COMMANDERS_RELATIVE | 0.5 | # Number of combat units relative to total army size |
| RETIRE_COMMANDER_INTERACTION_KEY | "retire_commander" | The AI will use this character interaction to retire excessive commanders |
| COMMANDER_DESIRED_RANK_DISPARITY_IN_ARMY | 1 | # Prefer promoting over recruiting new commanders if there isn't at least this rank disparity between any two generals in an army |
| COMMANDER_DESIRED_RANK_DISPARITY_IN_FLEET | 1 | # Prefer promoting over recruiting new commanders if there isn't at least this rank disparity between any two admirals in a fleet |
| RECRUITABLE_COMMANDER_BASE_SCORE | 100 | # The base score assigned to each recruitable commander in the pool |
| RECRUITABLE_COMMANDER_RANDOM_FACTOR | 3.0 | # The higher this is, the more random AI recruitment selection will be |
| RECRUITABLE_COMMANDER_SKILL_TRAIT_SCORE | 25 | # A recruitable commander's total value of skill traits is multiplied by this |
| RECRUITABLE_COMMANDER_PERSONALITY_TRAIT_SCORE | 0 | # A recruitable commander's total value of personality traits is multiplied by this |
| RECRUITABLE_COMMANDER_CONDITION_TRAIT_SCORE | -25 | # A recruitable commander's total value of condition traits is multiplied by this |
| RECRUITABLE_COMMANDER_FAVORED_IG_FACTOR | 1.5 | # If a recruitable commander comes from an IG the AI likes, multiply score by this |
| RECRUITABLE_COMMANDER_DISFAVORED_IG_FACTOR | 0.5 | # If a recruitable commander comes from an IG the AI dislikes, multiply score by this |
| MOBILIZATION_OPTION_RANDOM_FACTOR | 0.5 | # The higher this is, the more random AI is about which mobilization options to activate |
| MOBILIZATION_OPTION_MONEY_COST_FACTOR | 20 | # When checking whether the AI should activate a mobilization option, the monetary cost of activation is multiplied by this and compared against AI value to determine if it's worth it |
| MOBILIZATION_OPTION_NUM_ACTIVE_OPTIONS_DIVISOR | 0.25 | # Divide the value of each non-activated mobilization option by ( 1 + number of already active options * this ) |
| MOBILIZATION_OPTION_GOODS_SHORTAGE_MULT | 0.0 | # Multiply value of mobilization option by this if there is a goods shortage of any of its input goods |
| MOBILIZATION_BASE_DESIRED_RATIO_TO_ENEMY | 0.5 | # AI wants to have a total amount of mobilized army power that is equal to enemy mobilized army power * this |
| MOBILIZATION_MAIN_ATTACKER_ADDED_RATIO | 1.0 | # Add this to desired ratio for the main attacker in the war |
| MOBILIZATION_MAIN_DEFENDER_ADDED_RATIO | 1.0 | # Add this to desired ratio for the main defender in the war |
| MOBILIZATION_LOYAL_SUBJECT_OF_MAIN_PARTICIPANT_ADDED_RATIO | 0.75 | # Add this to desired ratio for loyal subjects of main attacker/defender in the war |
| MOBILIZATION_PEACE_NEGOTIATOR_ADDED_RATIO | 0.5 | # Add this to desired ratio for any country that is or would become a peace negotiator (but isn't main attacker or defender) |
| MOBILIZATION_LOCAL_FRONTS_ADDED_RATIO | 0.5 | # Add this to desired ratio for any country that has least one local front |
| MOBILIZATION_UNINCORPORATED_OCCUPATION_ADDED_RATIO | 0.5 | # Add this to desired ratio for any country whose unincorporated states are being occupied |
| MOBILIZATION_INCORPORATED_OCCUPATION_ADDED_RATIO | 1.0 | # Add this to desired ratio for any country whose incorporated states are being occupied (overrides multiplier for unincorporated occupation) |
| MOBILIZATION_EXISTENTIAL_WAR_FACTOR | 2.0 | # If the AI is in an existential war/diplo play (could cease to exist after peace), add this to its desired mobilization ratio |
| MOBILIZATION_MINOR_ALLY_MAX_RELATIVE_POWER | 0.15 | # To be counted as a minor ally, a country must have equal or less than this amount of the alliance's total combat power. It must also have no fronts. |
| MOBILIZATION_MINOR_ALLY_ADVANTAGE_TO_NOT_MOBILIZE | 2.0 | # If a minor ally's side in the conflict has at least this army power advantage when their forces are not counted in, don't bother mobilizing |
| MOBILIZATION_MIN_ESCALATION_START | 50 | # Before this amount of escalation in a play, AI will only mobilize as a response to the enemy mobilizing (base) |
| MOBILIZATION_MIN_ESCALATION_BOLDNESS_FACTOR | 0.2 | # Boldness is multiplied by this and subtracted from MOBILIZATION_MIN_MOBILIZATION_ESCALATION_START |
| MOBILIZATION_MIN_MOBILIZATION_PEACE_NEGOTIATOR | 0.15 | # AI will always mobilize at least this amount of forces if they are or would become a peace negotiator |
| MOBILIZATION_MIN_MOBILIZATION_LOYAL_SUBJECT_OF_MAIN_PARTICIPANT | 0.15 | # AI will always mobilize at least this amount of forces if they are a loyal subject of main attacker/defender |
| MOBILIZATION_MIN_MOBILIZATION_TERRITORIAL_RISK | 0.15 | # AI will always mobilize at least this amount of forces if they might lose territory from the war/play |
| MOBILIZATION_MIN_MOBILIZATION_UNINCORPORATED_OCCUPATION | 0.25 | # AI will always mobilize at least this amount of forces if their unincorporated states are occupied |
| MOBILIZATION_MIN_MOBILIZATION_INCORPORATED_OCCUPATION | 0.5 | # AI will always mobilize at least this amount of forces if their incorporated states are occupied (overrides the multiplier for unincorporated occupation) |
| MOBILIZATION_MIN_MOBILIZATION_LOCAL_FRONTS | 0.25 | # AI will always mobilize at least this amount of forces if they have any local fronts |
| MOBILIZATION_MIN_MOBILIZATION_CONTAINMENT_WAR | 1.0 | # AI will always mobilize at least this amount of forces if fighting in a containment war |
| CONSCRIPTION_INSUFFICIENT_FORCES_FACTOR | 1 | # For each 1% of mobilization the AI isn't able to meet, raise a base of 1% * this conscripts |
| CONSCRIPTION_RELATIVE_CONSCRIPTED_COMBAT_POWER_DIVISOR | 1 | # Conscripted forces fraction of combat power is multiplied by this, then the result of CONSCRIPTION_INSUFFICIENT_FORCES_FACTOR is divided by (1 + the result) |
| CONSCRIPTION_SMALL_STANDING_ARMY_THRESHOLD | 0.75 | # An AI whose conscripted combat power is above this fraction of total combat power is affected by the below factor |
| CONSCRIPTION_SMALL_STANDING_ARMY_MIN_CONSCRIPTS_FACTOR | 0.02 | # For each 1% the conscripted combat power fraction above CONSCRIPTION_SMALL_STANDING_ARMY_THRESHOLD, always raise at last this fraction of conscripts |
| MIN_GOVERNMENT_LEGITIMACY | 25 | # If legitimacy is below this, consider adding IGs we don't really like to the government |
| DESIRED_GOVERNMENT_LEGITIMACY | 50 | # Apply a bonus to the score of governments which have at least this much legitimacy |
| REFORM_GOVERNMENT_MONTHS_BETWEEN_CHANGES | 30 | # If the AI doesn't have elections, it won't consider changing government composition more often than this to avoid lots of radicals |
| REFORM_GOVERNMENT_NUM_OPTIONS_TO_CHECK | 5 | # How many top legitimacy possible government constellations will the AI consider |
| REFORM_GOVERNMENT_STICKINESS | 1.25 | # Multiply score of the current government by this when checking whether to reform the government |
| REFORM_GOVERNMENT_PRO_IG_CLOUT_FACTOR | 1.0 | # When scoring IGs for putting in government, add to the score multiplier (scaled by clout) |
| REFORM_GOVERNMENT_ANTI_IG_CLOUT_FACTOR | 10.0 | # When scoring IGs for putting in government, add to the score divisor (scaled by clout) |
| REFORM_GOVERNMENT_ABOVE_DESIRED_LEGITIMACY_FACTOR | 1.5 | # Multiply score of governments that meet the desired legitimacy threshold by this |
| REFORM_GOVERNMENT_BELOW_MIN_LEGITIMACY_FACTOR | 0.1 | # If a government option has less than MIN_GOVERNMENT_LEGITIMACY, multiply its score by this |
| MAX_CANDIDATES_TO_COMBINE_FOR_GOVERNMENT_ALTERNATIVES | 8 | # Max number of interest groups or parties to combine when checking government alternatives. 8 will give 2^8=256 possible governments. Higher values will affect performance exponentially |
| REGIME_CHANGE_NUM_GOVERNMENT_OPTIONS_TO_CHECK | 100 | # Replaces REFORM_GOVERNMENT_NUM_OPTIONS_TO_CHECK when attempting to form a government during a regime change - it's fine for this value to be very high as it's executed rarely |
| REGIME_CHANGE_MIN_GOVERNMENT_LEGITIMACY | 5 | # Replaces MIN_GOVERNMENT_LEGITIMACY when scoring IGs for government in a regime change |
| REGIME_CHANGE_REFORM_GOVERNMENT_STICKINESS | 0.1 | # Replaces REFORM_GOVERNMENT_STICKINESS when scoring IGs for government in a regime change |
| REGIME_CHANGE_REFORM_GOVERNMENT_CLOUT_FACTOR_MULTIPLIER | 100.0 | # When scoring IGs for government in a regime change, multiply pro/anti AI clout factors by this |
| IDEOLOGICAL_OPINION_ACCEPTABLE_PROGRESSIVENESS_DIFFERENCE | 25 | # If progressiveness difference between two countries is this or less, add positive ideological opinion, otherwise add negative |
| IDEOLOGICAL_OPINION_CURRENT_PROGRESSIVENESS_SAME_FACTOR | 2.5 | # Applied for each law group where current progressiveness difference is less than or equal to IDEOLOGICAL_OPINION_ACCEPTABLE_PROGRESSIVENESS_DIFFERENCE |
| IDEOLOGICAL_OPINION_CURRENT_PROGRESSIVENESS_DIFF_FACTOR | -0.05 | # Progressiveness difference of currently enacted law in each group is weighted by this amount for ideological opinion where current progressiveness difference is above IDEOLOGICAL_OPINION_ACCEPTABLE_PROGRESSIVENESS_DIFFERENCE |
| IDEOLOGICAL_OPINION_IDEAL_PROGRESSIVENESS_SAME_FACTOR | 2.5 | # Applied for each law group where current progressiveness difference is less than or equal to IDEOLOGICAL_OPINION_ACCEPTABLE_PROGRESSIVENESS_DIFFERENCE |
| IDEOLOGICAL_OPINION_IDEAL_PROGRESSIVENESS_DIFF_FACTOR | -0.05 | # Progressiveness difference of government's ideal law in each group is weighted by this amount for ideological opinion where ideal progressiveness difference is above IDEOLOGICAL_OPINION_ACCEPTABLE_PROGRESSIVENESS_DIFFERENCE |
| UNIFICATION_MIN_SUPPORT_SCORE | 50 | # Support for one country-formation candidate needs to be at least this much above all competitors to support unification |
| UNIFICATION_BASE_VALUE | 0 |  |
| UNIFICATION_SUPPORT_INVALID_TARGET_FACTOR | -1000 | # Unification support factor when country isn't a valid target for the unification play |
| UNIFICATION_SUPPORTER_DEFAULT_RANK_VALUE | 4 | # Rank value is compared to this value for computing supporter rank factor |
| UNIFICATION_SUPPORTER_RANK_FACTOR | -10 | # Multiplied by rank value delta to supporter default rank |
| UNIFICATION_CANDIDATE_DEFAULT_RANK_VALUE | 6 | # Rank value is compared to this value for computing candidate rank factor |
| UNIFICATION_CANDIDATE_RANK_FACTOR | 10 | # Multiplied by rank value delta to candidate default rank |
| UNIFICATION_RELATIONS_HOSTILE_FACTOR | -50 |  |
| UNIFICATION_RELATIONS_COLD_FACTOR | -25 |  |
| UNIFICATION_RELATIONS_POOR_FACTOR | -10 |  |
| UNIFICATION_RELATIONS_CORDIAL_FACTOR | 10 |  |
| UNIFICATION_RELATIONS_AMICABLE_FACTOR | 25 |  |
| UNIFICATION_RELATIONS_FRIENDLY_FACTOR | 50 |  |
| UNIFICATION_ATTITUDE_DISINTERESTED_FACTOR | -25 |  |
| UNIFICATION_ATTITUDE_CAUTIOUS_FACTOR | -25 |  |
| UNIFICATION_ATTITUDE_CONCILIATORY_FACTOR | 0 |  |
| UNIFICATION_ATTITUDE_COOPERATIVE_FACTOR | 25 |  |
| UNIFICATION_ATTITUDE_GENIAL_FACTOR | 50 |  |
| UNIFICATION_ATTITUDE_WARY_FACTOR | -50 |  |
| UNIFICATION_ATTITUDE_BELLIGERENT_FACTOR | -100 |  |
| UNIFICATION_ATTITUDE_ANTAGONISTIC_FACTOR | -100 |  |
| UNIFICATION_ATTITUDE_LOYAL_FACTOR | 100 |  |
| UNIFICATION_ATTITUDE_ALOOF_FACTOR | 25 |  |
| UNIFICATION_ATTITUDE_DEFIANT_FACTOR | -50 |  |
| UNIFICATION_ATTITUDE_REBELLIOUS_FACTOR | -100 |  |
| UNIFICATION_ATTITUDE_PROTECTIVE_FACTOR | -50 |  |
| UNIFICATION_ATTITUDE_DOMINEERING_FACTOR | -100 |  |
| UNIFICATION_POWER_BLOC_FACTOR | 25 | # Added to the unification support if both countries are in the same power bloc |
| STRATEGIC_REGION_STANCES_RANDOM_FACTOR | 1 |  |
| STRATEGIC_REGION_STANCES_STICKINESS | 2 | # Multiplied by current stance score when checking whether to change stance |
| CHANGE_TAX_START_OF_GAME_DAYS_TO_WAIT | 30 | # Don't change any tax levels for this amount of days after bookmark initialization, so that economic state has a chance to stabilize |
| CHANGE_TAX_SIGNIFICANT_DEBT_THRESHOLD | 0.1 | # At this amount of debt to max credit ratio, the logic for 'significant debt' outlined below kicks in |
| RAISE_TAX_TO_DESIRED_INCOME_THRESHOLD | 1.25 | # If income to expenses ratio is this or below, and tax level is below desired level, raise taxes |
| RAISE_TAX_ABOVE_DESIRED_INCOME_MAX_GOLD_RESERVES_THRESHOLD | 0.1 | # If gold reserves are at least this full, don't raise taxes above desired level |
| RAISE_TAX_ABOVE_DESIRED_INCOME_NO_DEBT_THRESHOLD | 0.9 | # If income to expenses ratio is this or below, there is no or little debt, and tax level is at or above desired level, raise taxes |
| RAISE_TAX_ABOVE_DESIRED_INCOME_WITH_DEBT_THRESHOLD | 1.1 | # If income to expenses ratio is this or below, there is significant debt, and tax level is at or above desired level, raise taxes |
| LOWER_TAX_TO_DESIRED_INCOME_NO_DEBT_THRESHOLD | 1.25 | # If income to expenses ratio is this or above, there is no or little debt, and tax level is at or above desired level, raise taxes |
| LOWER_TAX_TO_DESIRED_INCOME_WITH_DEBT_THRESHOLD | 1.5 | # If income to expenses ratio is this or above, there is significant debt, and tax level is at or above desired level, raise taxes |
| LOWER_TAX_BELOW_DESIRED_INCOME_THRESHOLD | 2.0 | # If income to expenses ratio is this or above and tax level below desired level, raise taxes |
| RAISE_TAX_HIGH_DEBT_OVERRIDE_RATIO | 0.5 | # At this amount of debt, any level of tax is OK to deal with it |
| CONSTRUCTION_MAX_NUM_PRODUCTION_BUILDING_CONSTRUCTIONS_BASE | 1 | # If country has this number of production building constructions queued, don't add anymore (base) |
| CONSTRUCTION_MAX_NUM_PRODUCTION_BUILDING_CONSTRUCTIONS_SCALED | 0.05 | # If country has this number of production building constructions queued, don't add anymore (scaled by construction production) |
| CONSTRUCTION_MAX_NUM_PRODUCTION_BUILDING_CONSTRUCTIONS_SCALED_MAX | 999 | # CONSTRUCTION_MAX_NUM_PRODUCTION_BUILDING_CONSTRUCTIONS_SCALED can't be higher than this |
| CONSTRUCTION_MAX_NUM_GOVERNMENT_BUILDING_CONSTRUCTIONS_BASE | 1 | # If country has this number of government building constructions queued, don't add anymore (base) |
| CONSTRUCTION_MAX_NUM_GOVERNMENT_BUILDING_CONSTRUCTIONS_SCALED | 0.05 | # If country has this number of government building constructions queued, don't add anymore (scaled by construction production) |
| CONSTRUCTION_MAX_NUM_GOVERNMENT_BUILDING_CONSTRUCTIONS_SCALED_MAX | 99 | # CONSTRUCTION_MAX_NUM_GOVERNMENT_BUILDING_CONSTRUCTIONS_SCALED can't be higher than this |
| CONSTRUCTION_RESERVES_NEW_CONSTRUCTIONS | 0.1 | # If gold reserves are less than this after adding the cost of a new construction, don't queue it |
| CONSTRUCTION_DEBT_RESUME | 0.2 | # If constructions are paused, resume once debt is this low relative to ceiling |
| CONSTRUCTION_DEBT_PAUSE | 0.4 | # If in this much relative debt to debt ceiling, pause all non-critical constructions |
| CONSTRUCTION_DEBT_RESUME_CRITICAL_CONSTRUCTION | 0.95 | # If critical constructions are paused, resume once debt is this low relative to ceiling |
| CONSTRUCTION_DEBT_PAUSE_CRITICAL_CONSTRUCTION | 0.99 | # If in this much relative debt to debt ceiling, pause all critical constructions |
| CONTAINMENT_PLAY_PARTICIPATION_RANK | 7 | # Ranks of this value or above should be keen on joining containment plays to beat down threats |
| START_DIPLO_PLAY_RANDOM_FACTOR | 2.0 | # The higher this is, the more random AI will be on where to target when starting diplo plays |
| START_DIPLO_PLAY_ALLY_STRENGTH_WEIGHT | 0.75 | # Consider participants that will for sure join a side with this amount of their forces |
| START_DIPLO_PLAY_LIKELY_ALLY_STRENGTH_WEIGHT | 0.5 | # Consider participants that will likely to join a side with this amount of their forces |
| DIPLO_PLAY_BACK_DOWN_CHANCE_THRESHOLD | 0 | # If ( confidence + boldness ) is less than this, consider backing down |
| DIPLO_PLAY_BACK_DOWN_CHANCE_ESCALATION | 30 | # Above this escalation, AI will consider backing down |
| DIPLO_PLAY_BACK_DOWN_INCREASE_CHANCE_THRESHOLD | -50 | # If ( confidence + boldness ) is less than this, increase the chance of backing down |
| DIPLO_PLAY_BACK_DOWN_INCREASE_CHANCE_MULTIPLIER | 4.0 | # If ( confidence + boldness ) is less than DIPLO_PLAY_BACK_DOWN_INCREASE_CHANCE_THRESHOLD, increase the chance of backing down by this factor |
| DIPLO_PLAY_BACK_DOWN_GUARANTEED_THRESHOLD | -75 | # If ( confidence + boldness ) is less than this, always back down before the play goes to war |
| DIPLO_PLAY_BACK_DOWN_GUARANTEED_ESCALATION | 95 | # Above this escalation, AI will always back down if it's supposed to |
| DIPLO_PLAY_BACK_DOWN_CHANCE_LOW_ESCALATION | 0.4 | # 1.0 = 1% (chance each day) - used before countdown to war starts |
| DIPLO_PLAY_BACK_DOWN_CHANCE_HIGH_ESCALATION | 2.0 | # 1.0 = 1% (chance each day) - used after countdown to war starts |
| DIPLO_PLAY_BACK_DOWN_CHANCE_WAR_LOSSES_MULT | 1.5 | # Multiply chance of backing down due to additional wargoal demands by 1 + ( impact of additional wargoals / impact of original wargoal * this ) |
| DIPLO_PLAY_BACK_DOWN_CHANCE_WAR_LOSSES_MAX | 3.0 | # Max multiplier for impact of additional wargoal demands (including the base of 1) |
| DIPLO_PLAY_FREELY_ADD_WARGOALS_ESCALATION_THRESHOLD | 70 | # After this amount of escalation, the AI will freely add wargoals instead of reserving manuevers for swaying |
| DIPLO_PLAY_ADD_WARGOALS_THRESHOLD | 0.5 | # If AI doesn't have at least this much military strength compared to enemy, don't add more wargoals for themselves after the first |
| DIPLO_PLAY_FORCE_DIPLOMATIC_PLAY_THRESHOLD | 2.0 | # If the AI believes it will have this much military strength compared to enemy and wants multiple things from them, then don't bother sending a diplomatic demand |
| DIPLO_PLAY_SWAY_THRESHOLD | 2.0 | # If AI has this much military strength compared to enemy, don't bother trying to sway anyone |
| DIPLO_PLAY_REVERSE_SWAY_THRESHOLD | 2.0 | # If AI has this much military strength compared to enemy, consider reverse sways to have less value |
| DIPLO_PLAY_SWAY_LEANING_SIDE_MILITARY_STRENGTH_MULT | 0.25 | # When determining strength compared to enemy, add in undecided countries leaning towards a side with this part of their strength |
| DIPLO_PLAY_DECIDE_ON_SUPPORT_ESCALATION | 30 | # Above this escalation, AI will potentially start taking sides (or declare neutrality) even if not swayed |
| DIPLO_PLAY_TAKE_SIDES_MIN_BOLDNESS | 25 | # Boldness must be at least this for AI to want to take a side with no gain (ignored for Great Powers in containment plays) |
| DIPLO_PLAY_TAKE_SIDES_CHANCE | 0.004 | # Multiplied by boldness for chance of taking sides each tick |
| DIPLO_PLAY_DECLARE_NEUTRALITY_ESCALATION_MIN_BASE | 80 | # Lowest escalation at which AI can declare neutrality, AIs with a preference will never declare neutrality before countdown to war |
| DIPLO_PLAY_DECLARE_NEUTRALITY_IMPACT_OF_NEUTRALITY_SCORE | 0.5 | # AI's neutrality score * this is subtracted from DIPLO_PLAY_DECLARE_NEUTRALITY_ESCALATION_MIN_BASE |
| DIPLO_PLAY_DECLARE_NEUTRALITY_IMPACT_OF_NEUTRALITY_SCORE_MAX | 50 | # DIPLO_PLAY_DECLARE_NEUTRALITY_IMPACT_OF_NEUTRALITY_SCORE cannot be higher than this |
| DIPLO_PLAY_DECLARE_NEUTRALITY_ESCALATION_MAX | 99 | # Highest escalation at which AI can declare neutrality |
| DIPLO_PLAY_ABANDON_SUPPORT_CHANCE | 0.1 | # Multiplied with negative support score |
| DIPLO_PLAY_SWAY_COUNTRIES_ESCALATION | 10 | # Above this escalation, AI will potentially start swaying countries |
| DIPLO_PLAY_REVERSE_SWAY_COUNTRIES_CHANCE_SCALED | 0.02 | # Chance each day that the AI will try to reverse-sway (scaled by boldness) |
| DIPLO_PLAY_REVERSE_SWAY_COUNTRIES_CHANCE_MAX | 0.5 | # Max chance each day that the AI will try to reverse-sway |
| DIPLO_PLAY_REVERSE_SWAY_LEANING_MULT | 5.0 | # Applied to both scaled and max chance if the swaying country is already leaning towards a side |
| DIPLO_PLAY_SWAY_COUNTRIES_CHANCE_SCALED | 20 | # Chance each day that the AI will try to sway someone (scaled by relative strength of the two sides, 1 = 1%) |
| DIPLO_PLAY_SWAY_COUNTRIES_CHANCE_MAX | 75 | # Max chance each day that the AI will try to sway someone |
| DIPLO_PLAY_TIMED_WEIGHT_DURATION | 12 | # When AI randomly determines sympathy for one side of a diplo play, how long does that weight stay |
| DIPLO_PLAY_PREFERENCE_THRESHOLD | 25 | # At this delta, an AI country is considered to have a preference for that side of the diplo play |
| DIPLO_PLAY_WEAK_ABANDON_SUPPORT_THRESHOLD | -25 | # If support for the side an AI country is backing drops below this, consider abandoning it |
| DIPLO_PLAY_STRONG_ABANDON_SUPPORT_THRESHOLD | -50 | # If support for the side an AI country is backing drops below this, abandon it immediately |
| DIPLO_PLAY_ABANDON_ALLY_OR_SUBJECT_MIN_ENEMY_STRENGTH | 0.75 | # If the enemy doesn't have at least this amount of troops compared to our side, never abandon an ally or subject |
| DIPLO_PLAY_ABANDON_ALLY_RELUCTANCE | 50 | # Added to support score when considering whether to abandon an ally |
| DIPLO_PLAY_ABANDON_SUBJECT_RELUCTANCE | 100 | # Added to support score when considering whether to abandon a subject |
| DIPLO_PLAY_SWAY_DAYS_LEFT_MAX | 12 | # AI will not answer a sway offer when it has more than this amount of days left (should map to SWAY_OFFER_TIMEOUT_DAYS) |
| DIPLO_PLAY_SWAY_DAYS_LEFT_MIN | 8 | # AI will always answer a sway offer when it has this or less amount of days left (should map to SWAY_OFFER_TIMEOUT_DAYS) |
| DIPLO_PLAY_SWAY_ANSWER_CHANCE | 75 | # Chance per day of AI answering a sway offer (1 = 1%) |
| DIPLO_PLAY_WEAK_ARMY_THRESHOLD | 0.5 | # If our army strength compared to the average for each country involved in the play is less than this, weak army effects will apply |
| DIPLO_PLAY_STRONG_ARMY_THRESHOLD | 1.0 | # If our army strength compared to the average for each country involved in the play is at least than this, strong army effects will start to apply |
| DIPLO_PLAY_STRONG_ARMY_MAX | 3.0 | # Maximum strong army effects apply at this threshold |
| DIPLO_PLAY_FORCE_BALANCE_SCALE | 4.0 | # At this military-strength-to-enemies ratio, max effects from the balance of the two sides' militaries is applied |
| DIPLO_PLAY_FORCE_BALANCE_NAVY_FACTOR | 0.1 | # Naval power projection counts for this much compared to army power projection when determining military strength to enemies |
| DIPLO_PLAY_FORCE_BALANCE_MOBILIZATION_FACTOR | 1.0 | # A country's military forces are considered to be ( 1 + this * fully mobilized unit ratio ) much stronger in a play for purposes of confidence, etc |
| DIPLO_PLAY_STATE_STABILITY_UNINCORPORATED_WEIGHT_MULT | 0.25 | # Weight for devastation, radicals & loyalists in unincorporated states is multiplied by this |
| DIPLO_PLAY_CONTAINMENT_PLAY_FACTOR | 100 | # Added to preference for initiator in a containment play if the country is a Great Power |
| DIPLO_PLAY_SWAY_LOW_IMPACT_FACTOR | -100 | # Maximum effect applied to acceptance of a reverse-sway if a country has little to lose from the enemy side's wargoals |
| DIPLO_PLAY_SWAY_LOW_IMPACT_THRESHOLD | 50 | # At this total enemy wargoal impact or below, acceptance is reduced by up to DIPLO_PLAY_SWAY_LOW_IMPACT_FACTOR (at 0 impact) |
| DIPLO_PLAY_SWAY_NON_PRIMARY_DEMAND_IMPACT_MULT | 0.5 | # Secondary demands have their impact multiplied by this factor for the purpose of measuring the low impact factor above |
| DIPLO_PLAY_SWAY_SUBJECT_IMPACT_VALUE_DIVISOR | 500 | # Wargoals on subjects have their impact multiplied by (the subject's value for overlord divided by this) for the purpose of measuring the low impact factor above (clamped to 0-1) |
| DIPLO_PLAY_SWAY_INCOME_TRANSFER_PACTS_OF_SAME_TYPE_FACTOR | -30 | # Added to acceptance score for each income transfer pact the target country has of the same type (where they are the receiver of the money) |
| DIPLO_PLAY_SWAY_TOO_LOW_SUPPORT_DESIRE_THRESHOLD | -100 | # If a country has this or less support desire, don't bother evaluating sways against them |
| DIPLO_PLAY_UNWANTED_SWAY_OFFER_MEMORY_DURATION_DAYS | 10 | # The AI will remember another country not being interested in a particular sway offer for this many days |
| DIPLO_PLAY_CALL_ALLY_PREFERENCE_SCORE = 1000 # When determining which sway the AI wants to offer, score Call Ally this highly |  |  |
|  |  | # AI uses these values to determine how 'impactful' a wargoal is, ie how much they would like to avoid having it enforced on them etc |
| DIPLO_PLAY_WAR_GOAL_IMPACT_MANEUEVERS_MULT | 1 | # Maneuvers cost of a wargoal is multiplied by this and added to impact |
| DIPLO_PLAY_WAR_GOAL_IMPACT_INFAMY_MULT | 0.5 | # Infamy generation of a wargoal is multiplied by this and added to impact |
| DIPLO_PLAY_WAR_GOAL_IMPACT_CONQUEST_MULT | 2.0 | # Wargoals that outright conquer states or annex whole countries have their overall impact multiplied by this |
| # Boldness determines the confidence threshold at which the AI will back down in a play # Each individual boldness factor is multiplied a dice roll range of (x0 to x1) for actual boldness value in each play - boldness can end up negative! # Boldness also plays a role for determining whether undecided countries will join a play unprompted # Base boldness is set by the country's AI strategies |  |  |
| DIPLO_PLAY_BOLDNESS_FROM_RANK | 3 | # Multiplied by country's rank value and added to boldness range |
| DIPLO_PLAY_BOLDNESS_WEAK_ARMY_FACTOR | -25 | # Scaled by our relative forces compared to DIPLO_PLAY_WEAK_ARMY_THRESHOLD |
| DIPLO_PLAY_BOLDNESS_CONTAINMENT_PLAY | 100 | # Add this boldness if in a containment play |
| # The below is a special boldness factor in diplomatic plays that is always calculated on the spot, not randomized and added to saved boldness score, as the amount of primary demands can grow |  |  |
| DIPLO_PLAY_BOLDNESS_PRIMARY_DEMANDS | 1 | # Add this amount of non-randomized boldness for each wargoal impact point of primary demands against our side |
|  |  | # Confidence is added to boldness to determine whether the AI is willing to back down |
| DIPLO_PLAY_CONFIDENCE_FORCE_BALANCE_FACTOR | 75 | # Confidence level if force balance to the enemy is at DIPLO_PLAY_FORCE_BALANCE_SCALE, scaled down if lower |
| DIPLO_PLAY_CONFIDENCE_STRONG_ARMY_FACTOR | 15 | # Scaled by our relative forces compared to DIPLO_PLAY_STRONG_ARMY_MAX |
| DIPLO_PLAY_CONFIDENCE_CIVIL_WAR_OR_UPRISING | 75 | # Add this confidence to both sides in a civil war or native uprising |
| DIPLO_PLAY_CONFIDENCE_EXISTENTIAL_PLAY | 50 | # Add this confidence if backing down would result in annexation |
| DIPLO_PLAY_CONFIDENCE_FROM_TURMOIL | -15 | # At 100% turmoil across the country (weighted by state population), subtract this amount of confidence |
| DIPLO_PLAY_CONFIDENCE_FROM_LOYALISTS | 15 | # At 100% turmoil across the country (weighted by state population), add this amount of confidence |
| DIPLO_PLAY_CONFIDENCE_FROM_DEVASTATION | -15 | # At 100% devastation, subtract this amount of confidence |
| DIPLO_PLAY_CONFIDENCE_FROM_DEBT_LEVEL | -25 | # At 100% debt level, subtract this amount of confidence |
| DIPLO_PLAY_CONFIDENCE_FROM_BANKRUPTCY | -25 | # Subtract this amount of confidence when bankrupt |
| DIPLO_PLAY_CONFIDENCE_FROM_GOLD_RESERVES | 15 | # At 100% gold reserves, add this amount of confidence |
| DIPLO_PLAY_CONFIDENCE_FROM_OWN_CONFLICTS | -25 | # If we are in another conflict where military strength compared to our enemies is equal to or above DIPLO_PLAY_FORCE_BALANCE_SCALE, subtract this amount of confidence |
| DIPLO_PLAY_CONFIDENCE_FROM_ENEMY_TURMOIL | 10 | # At 100% turmoil across the enemy country (weighted by state population), add this amount of confidence |
| DIPLO_PLAY_CONFIDENCE_FROM_ENEMY_DEVASTATION | 10 | # At 100% devastation for enemy, add this amount of confidence |
| DIPLO_PLAY_CONFIDENCE_FROM_ENEMY_DEBT_LEVEL | 10 | # At 100% debt level for enemy, add this amount of confidence |
| DIPLO_PLAY_CONFIDENCE_FROM_ENEMY_BANKRUPTCY | 10 | # If enemy is bankrupt, add this amount of confidence |
| DIPLO_PLAY_CONFIDENCE_FROM_ENEMY_CONFLICTS | 25 | # If the other side is in another conflict where military strength compared to their enemies is equal to or above DIPLO_PLAY_FORCE_BALANCE_SCALE, add this amount of confidence |
| DIPLO_PLAY_CONFIDENCE_VERY_LOW_THRESHOLD | -50 | # If confidence is this or below, show it as very low |
| DIPLO_PLAY_CONFIDENCE_LOW_THRESHOLD | -25 | # If confidence is this or below, show it as low |
| DIPLO_PLAY_CONFIDENCE_HIGH_THRESHOLD | 25 | # If confidence is this or above, show it as high |
| DIPLO_PLAY_CONFIDENCE_VERY_HIGH_THRESHOLD | 50 | # If confidence is this or above, show it as very high |
| # Below data is used to determine which side the AI wants to join a diplo play, if any # Neutrality is a calculated value that determines how much a country wants to stay out of a diplo play # In order for a country to join, their side preference score must beat out both the enemy's side preference score AND the neutrality score # Base neutrality is set by the country's AI strategies |  |  |
| DIPLO_PLAY_NEUTRALITY_MIN | 0 |  |
| DIPLO_PLAY_NEUTRALITY_PREFERENCE_DELTA_THRESHOLD | 50 | # If the preference delta between the two sides is less than this, add the difference between the delta and this value to neutrality score |
| DIPLO_PLAY_NEUTRALITY_FROM_DEBT_LEVEL | 100 | # At 100% debt level, add this amount of neutrality score |
| DIPLO_PLAY_NEUTRALITY_FROM_BANKRUPTCY | 100 | # When bankrupt, add this amount of neutrality score |
| DIPLO_PLAY_NEUTRALITY_FROM_DEVASTATION_LEVEL | 100 | # At 100% devastation across the country (weighted by state population), add this amount of neutrality score |
| DIPLO_PLAY_NEUTRALITY_FROM_TURMOIL | 100 | # At 100% turmoil across the country (weighted by state population), add this amount of neutrality score |
| DIPLO_PLAY_NEUTRALITY_IN_SUBJECT_CONFLICT | -50 | # If either side in the play is a subject, subtract this amount of neutrality score |
| DIPLO_PLAY_NEUTRALITY_IN_NATIVE_UPRISING | 50 | # Added to neutrality score for native uprising type conflicts |
| DIPLO_PLAY_NEUTRALITY_FROM_ONGOING_CONFLICTS | 200 | # If in a conflict where military strength compared to the enemy is equal to or above DIPLO_PLAY_FORCE_BALANCE_SCALE, add this amount of neutrality score |
| DIPLO_PLAY_NEUTRALITY_FROM_LOWER_RANK | 5 | # For each rank value difference between us and the lowest ranked participant in the play, if we're higher rank than them |
| DIPLO_PLAY_NEUTRALITY_FROM_NO_ARMY | 1000 | # If we have no army at all, add this to neutrality score |
| DIPLO_PLAY_NEUTRALITY_WEAK_ARMY_FACTOR | 100 | # Scaled by our relative forces compared to DIPLO_PLAY_WEAK_ARMY_THRESHOLD |
| DIPLO_PLAY_NEUTRALITY_TRUCE_FACTOR | 50 | # If we have a truce with either primary participant and no alliance or subject relationship, and it's not a civil war |
| # Sympathy is added together and then multiplied by a dice roll range of (DIPLO_PLAY_SYMPATHY_RANGE_MIN to DIPLO_PLAY_SYMPATHY_RANGE_MAX) to give the AI a random preference for each side in a particular play # Sympathy above 0 is added directly to the willingness to join that side in the play # Sympathy for a side can be below 0, but has no additional effect other than acting as a buffer against sympathy increases |  |  |
| DIPLO_PLAY_SYMPATHY_RANGE_MIN | 0.1 | # The minimum range for the initial sympathy random roll (additions during play are fully random) |
| DIPLO_PLAY_SYMPATHY_RANGE_MAX | 1.0 | # The maximum range for the initial sympathy random roll (additions during play are fully random) |
| DIPLO_PLAY_SYMPATHY_BASE_INITIATOR | 20 | # The base size of the random sympathy range for attacker in diplomatic play |
| DIPLO_PLAY_SYMPATHY_BASE_TARGET | 40 | # The base size of the random sympathy range for defender in diplomatic play |
| DIPLO_PLAY_SYMPATHY_ENEMY_OF_SUBJECT_INITIATOR | -100 | # Subtracted from sympathy range for enemies of our subjects if the enemy is the attacker |
| DIPLO_PLAY_SYMPATHY_ENEMY_OF_SUBJECT_TARGET | -50 | # Subtracted from sympathy range for enemies of our subjects if the enemy is the defender |
| DIPLO_PLAY_SYMPATHY_ENEMY_OF_ALLY_INITIATOR | -100 | # Subtracted from sympathy range for enemies of our allies if the enemy is the attacker |
| DIPLO_PLAY_SYMPATHY_ENEMY_OF_ALLY_TARGET | -50 | # Subtracted from sympathy range for enemies of our allies if the enemy is the defender |
| DIPLO_PLAY_SYMPATHY_ENEMY_OF_INFAMOUS_COUNTRY | 15 | # Added to sympathy range for enemy of infamous country |
| DIPLO_PLAY_SYMPATHY_ENEMY_OF_NOTORIOUS_COUNTRY | 30 | # Added to sympathy range for enemy of notorious country |
| DIPLO_PLAY_SYMPATHY_ENEMY_OF_PARIAH_COUNTRY | 100 | # Added to sympathy range for enemy of pariah country |
| DIPLO_PLAY_SYMPATHY_LENIENT_AI_GAME_RULE | 25 | # Added to sympathy range for player when using lenient AI game rule |
| DIPLO_PLAY_SYMPATHY_HARSH_AI_GAME_RULE | -25 | # Subtracted to sympathy range for player when using harsh AI game rule |
| DIPLO_PLAY_SYMPATHY_FROM_INITIAL_WARGOAL | 0.75 | # Initial sympathy for target is increased by up to this amount * accured infamy on the primary wargoal |
| DIPLO_PLAY_SYMPATHY_INCREASE_NEW_WARGOAL | 1 | # Sympathy is increased by up to this amount * accured infamy for enemy of a side which adds a new wargoal |
| DIPLO_PLAY_SYMPATHY_INCREASE_SWAYED_WITH_WARGOAL | 0.75 | # Sympathy is increased by up to this amount * accured infamy for enemy of a side which adds a new wargoal through swaying |
| DIPLO_PLAY_SWITCH_SIDES_FACTOR | -10 | # If AI has already picked a side, add reluctance to accept further sway offers |
| DIPLO_PLAY_IDEOLOGICAL_OPINION_POSITIVE_FACTOR | 0.2 | # Positive ideological opinion is multiplied by this and added to acceptance to join a side |
| DIPLO_PLAY_IDEOLOGICAL_OPINION_NEGATIVE_FACTOR | 1 | # Negative ideological opinion is multiplied by this and added to acceptance to join a side |
| DIPLO_PLAY_IDEOLOGICAL_OPINION_REVOLUTION_MULT | 3 | # DIPLO_PLAY_IDEOLOGICAL_OPINION_FACTOR is multiplied by this in a revolution play |
| DIPLO_PLAY_SECESSION_OWN_SECESSION_RISK_FACTOR | -100 | # Add this amount of reluctance for AI to back a secession of a culture that has enough pops in their own country to secede |
| DIPLO_PLAY_NON_ALLY_UNRECOGNIZED_BASE_FACTOR | -25 | # Add this amount of reluctance for AI to back a non-allied unrecognized power against a recognized one |
| DIPLO_PLAY_NON_ALLY_UNRECOGNIZED_INCONSEQUENTAL_ENEMY_DEMANDS_FACTOR | -50 | # Add this amount of reluctance for AI to back a non-allied unrecognized power against a recognized power that isn't demanding significant territorial concessions (conquer/make subject etc) |
| DIPLO_PLAY_NON_ALLY_UNRECOGNIZED_CONSEQUENTAL_DEMANDS_FACTOR | -100 | # Add this amount of reluctance for AI to back significant demands from a non-allied unrecognized power |
| DIPLO_PLAY_ALLY_INITIATOR_FACTOR | 25 | # Added to desire for ally of initiator to join their side |
| DIPLO_PLAY_ALLY_TARGET_FACTOR | 50 | # Added to desire for ally of target to join their side |
| DIPLO_PLAY_GUARANTEE_TARGET_FACTOR | 50 | # Added to desire for guarantor of target to join their side |
| DIPLO_PLAY_OVERLORD_INITIATOR_FACTOR | 25 | # Added to desire for overlord of initiator to join their side |
| DIPLO_PLAY_OVERLORD_TARGET_FACTOR | 50 | # Added to desire for overlord of target to join their side |
| DIPLO_PLAY_SAME_POWER_BLOC_INITIATOR_FACTOR | 15 | # Added to desire for fellow power bloc member of initiator to join their side |
| DIPLO_PLAY_SAME_POWER_BLOC_TARGET_FACTOR | 25 | # Added to desire for fellow power bloc member of target to join their side |
| # Diplo play scoring for relations levels |  |  |
| DIPLO_PLAY_RELATIONS_HOSTILE_FACTOR | -50 |  |
| DIPLO_PLAY_RELATIONS_COLD_FACTOR | -25 |  |
| DIPLO_PLAY_RELATIONS_POOR_FACTOR | -10 |  |
| DIPLO_PLAY_RELATIONS_CORDIAL_FACTOR | 10 |  |
| DIPLO_PLAY_RELATIONS_AMICABLE_FACTOR | 25 |  |
| DIPLO_PLAY_RELATIONS_FRIENDLY_FACTOR | 50 |  |
| # Diplo play scoring for attitudes (with scoring against both primary and backers) |  |  |
| DIPLO_PLAY_ATTITUDE_DISINTERESTED_FACTOR | 0 |  |
| DIPLO_PLAY_ATTITUDE_DISINTERESTED_BACKER_FACTOR | 0 |  |
| DIPLO_PLAY_ATTITUDE_CAUTIOUS_FACTOR | 0 |  |
| DIPLO_PLAY_ATTITUDE_CAUTIOUS_BACKER_FACTOR | 0 |  |
| DIPLO_PLAY_ATTITUDE_CONCILIATORY_FACTOR | 10 |  |
| DIPLO_PLAY_ATTITUDE_CONCILIATORY_BACKER_FACTOR | 5 |  |
| DIPLO_PLAY_ATTITUDE_COOPERATIVE_FACTOR | 15 |  |
| DIPLO_PLAY_ATTITUDE_COOPERATIVE_BACKER_FACTOR | 5 |  |
| DIPLO_PLAY_ATTITUDE_GENIAL_FACTOR | 25 |  |
| DIPLO_PLAY_ATTITUDE_GENIAL_BACKER_FACTOR | 10 |  |
| DIPLO_PLAY_ATTITUDE_WARY_FACTOR | -10 |  |
| DIPLO_PLAY_ATTITUDE_WARY_BACKER_FACTOR | -5 |  |
| DIPLO_PLAY_ATTITUDE_BELLIGERENT_FACTOR | -50 |  |
| DIPLO_PLAY_ATTITUDE_BELLIGERENT_BACKER_FACTOR | -25 |  |
| DIPLO_PLAY_ATTITUDE_ANTAGONISTIC_FACTOR | -50 |  |
| DIPLO_PLAY_ATTITUDE_ANTAGONISTIC_BACKER_FACTOR | -25 |  |
| DIPLO_PLAY_ATTITUDE_LOYAL_FACTOR | 100 |  |
| DIPLO_PLAY_ATTITUDE_LOYAL_BACKER_FACTOR | 25 |  |
| DIPLO_PLAY_ATTITUDE_ALOOF_FACTOR | 25 |  |
| DIPLO_PLAY_ATTITUDE_ALOOF_BACKER_FACTOR | 10 |  |
| DIPLO_PLAY_ATTITUDE_DEFIANT_FACTOR | -25 |  |
| DIPLO_PLAY_ATTITUDE_DEFIANT_BACKER_FACTOR | -10 |  |
| DIPLO_PLAY_ATTITUDE_REBELLIOUS_FACTOR | -100 |  |
| DIPLO_PLAY_ATTITUDE_REBELLIOUS_BACKER_FACTOR | -50 |  |
| DIPLO_PLAY_ATTITUDE_PROTECTIVE_FACTOR | 25 |  |
| DIPLO_PLAY_ATTITUDE_PROTECTIVE_BACKER_FACTOR | 10 |  |
| DIPLO_PLAY_ATTITUDE_DOMINEERING_FACTOR | -10 |  |
| DIPLO_PLAY_ATTITUDE_DOMINEERING_BACKER_FACTOR | 0 |  |
| DIPLO_PLAY_SWAY_RANDOM_FACTOR | 1.0 | # The higher this is, the more random the AI will be about which countries it tries to sway first |
| DIPLO_PLAY_SWAY_UNWANTED_OFFER | -1000 | # For being offered something they don't want |
| DIPLO_PLAY_SWAY_CALL_IN_OBLIGATION | 100 | # When calling in an obligation |
| DIPLO_PLAY_SWAY_MINIMUM_OBLIGATION_VALUE | 10 | # Obligations worth less than this are rejected |
| DIPLO_PLAY_SWAY_CALL_ALLY_FACTOR | 25 | # Added to acceptance for Call Ally sway |
| DIPLO_PLAY_SWAY_MINIMUM_PREFERENCE_FOR_SUBJUGATION | 1 | # The AI will not sway or reverse-sway with 'become subject' unless the supporter's preference for the supported is at least this |
| DIPLO_PLAY_SWAY_WARGOAL_WEAK_SWAYER_CONFIDENT_IN_OWN_ARMY_FACTOR | 0.25 | # This much of the penalty for a 'weak' sway offer is removed if the target believes they can achieve the wargoal themselves |
| DIPLO_PLAY_SWAY_WARGOAL_FACTOR | 1.0 | # Multiplied by wargoal value |
| DIPLO_PLAY_SWAY_WARGOAL_THRESHOLD | 10 | # A wargoal needs at least this base value to be wanted as part of sway offer |
| DIPLO_PLAY_SWAY_WARGOAL_MINIMUM_SWAYER_MULTIPLIER_INITIATOR | 0.2 | # If a wargoal sway offer from initiator is less than this fraction of its base value due to weakness of the swayer, consider it an unwanted wargoal |
| DIPLO_PLAY_SWAY_WARGOAL_MINIMUM_SWAYER_MULTIPLIER_TARGET | 0.05 | # If a wargoal sway offer from target is less than this fraction of its base value due to weakness of the swayer, consider it an unwanted wargoal |
| DIPLO_PLAY_SWAY_LEANING_PLAYER_FACTOR | 100 | # Added to acceptance for players leaning towards a side to make AI more likely to sway them |
| DIPLO_PLAY_SWAY_BECOME_SUBJECT_VALUE_FACTOR | 1.0 | # Multiplies AI desire for the swaying country to become their subject |
| DIPLO_PLAY_SWAY_TRANSFER_SUBJECT_VALUE_FACTOR | 1.0 | # Multiplies AI desire for the swaying country's offered transfer of subject to become their subject |
| DIPLO_PLAY_SWAY_STATE_DESIRE_FACTOR | 2.0 | # Multiplies AI strategy value for a state to determine if AI wants a transfer state sway |
| DIPLO_PLAY_SWAY_DIPLOMATIC_PACT_DESIRE_FACTOR | 1.0 | # Multiplies diplomatic acceptance score for the diplomatic action to determine if AI wants a diplomatic action sway |
| # Determines how much the AI values a reverse-sway based on the military power it would add to their side # If that power would make up the full difference between no military at all and DIPLO_PLAY_REVERSE_SWAY_THRESHOLD, use the full value, otherwise scale it against the amount of the difference made up # For example, if the new supporter would bring military power compared to enemy from 1.0x to 2.0x, and DIPLO_PLAY_REVERSE_SWAY_THRESHOLD is 2.0, we would apply half this value |  |  |
| DIPLO_PLAY_REVERSE_SWAY_ADDED_MILITARY_POWER_FACTOR | 50 |  |
| DIPLO_PLAY_REVERSE_SWAY_MIN_ADDED_MILITARY_POWER | 5 | # If the added military power value is below this, consider the country's help to not be worth anything and reject the offer |
| # Multiply added military power factor by the amount they are currently outmatched against the enemy # IE; at 0x enemy military power this full modifier gets applied, at 0.5x military power half of it is applied, and at 1x+ none of it is |  |  |
| DIPLO_PLAY_REVERSE_SWAY_ADDED_MILITARY_POWER_OUTMATCHED_MULT | 4.0 |  |
| DIPLO_PLAY_REVERSE_SWAY_OUTMATCHING_FACTOR | -25.0 | # If the AI's side is outmatching the enemy by more than DIPLO_PLAY_REVERSE_SWAY_THRESHOLD, the difference between their military power ratio and DIPLO_PLAY_REVERSE_SWAY_THRESHOLDis multiplied by this and added to acceptance |
| DIPLO_PLAY_REVERSE_SWAY_BASE_FACTORS_MULT | 0.5 | # Apply basic factors such as relations, attitude, ideological opinion etc to reverse-sway with this multiplier |
| DIPLO_PLAY_REVERSE_SWAY_WARGOAL_VALUE_FACTOR | -2.0 | # Multiply by how much the AI wants a requested wargoal themselves if they were the holder and apply to reverse-sway acceptance |
| DIPLO_PLAY_REVERSE_SWAY_WARGOAL_IMPACT_FACTOR | -0.5 | # Multiply by wargoal maneuvers cost (to determine how impactful it is) and apply to reverse-sway acceptance for a requested wargoal |
| DIPLO_PLAY_REVERSE_SWAY_WARGOAL_INFAMY_FACTOR | -0.5 | # Multiply by infamy impact and apply to reverse-sway acceptance for a requested wargoal |
| DIPLO_PLAY_REVERSE_SWAY_OFFER_OBLIGATION_MIN_VALUE | 5 | # AI value for an obligation is never lower than this when it's considering whether to accept a reverse-sway |
| DIPLO_PLAY_REVERSE_SWAY_OFFER_OBLIGATION_FACTOR | -6.0 | # Multiply by how much the AI would value the obligation if it was the country offering support and apply to reverse-sway acceptance for an obligation |
| DIPLO_PLAY_REVERSE_SWAY_CALL_IN_OBLIGATION_FACTOR | -3.0 | # Multiply by how much the AI values the obligation it holds and apply to reverse-sway acceptance for calling in obligation |
| DIPLO_PLAY_REVERSE_SWAY_STATE_VALUE_FACTOR | -2.0 | # Multiplied by AI strategy value for owned state to determine reluctance to cede it in a reverse-sway |
| DIPLO_PLAY_REVERSE_SWAY_BECOME_SUBJECT_VALUE_FACTOR | 1.0 | # Multiplied by how much the AI wants to become a subject of the sway target |
| DIPLO_PLAY_REVERSE_SWAY_TRANSFER_SUBJECT_VALUE_FACTOR | -1.0 | # Multiplied by how much the AI values the subject they're offering to transfer to the sway target |
| DIPLO_PLAY_REVERSE_SWAY_CALL_ALLY_DESIRE | 25 | # Added to AI scoring for reverse sway call ally even though call ally isn't actually valid for reverse-sways, so they can score it against other sway types |
| DIPLO_PLAY_ADD_WARGOAL_MIN_SCORE | 20 | # A wargoal needs at least this value for AI to add it to the play |
| LOW_AGGRESSION_BASE_EFFECT_MULT | 0.5 | # The impact of low ai aggression game rule on how often the AI starts diplomatic plays |
| HIGH_AGGRESSION_BASE_EFFECT_MULT | 2.0 | # The impact of high ai aggression game rule on how often the AI starts diplomatic plays |
| LOW_AGGRESSION_INFAMY_ACCEPTANCE_MULT | 0.5 | # The amount of infamy the AI considers undesirable/unacceptable is multiplied by this for low aggression AI |
| HIGH_AGGRESSION_INFAMY_ACCEPTANCE_MULT | 1.5 | # The amount of infamy the AI considers undesirable/unacceptable is multiplied by this for low aggression AI |
| AI_AGGRESSION_MAX_ACCEPTABLE_INFAMY | 100 | # Undesirable/unacceptable infamy will not be set above this from high aggression |
| # Below data is used to determine which wargoals the AI will pick |  |  |
| WAR_GOAL_RANDOM_FACTOR | 2.0 | # The higher this is, the more random AI wargoal selection will be |
| WAR_GOAL_UNDESIRABLE_INFAMY_FACTOR | 0.5 | # Wargoal value is multiplied by this if it would bring the country above undesirable infamy levels |
| WAR_GOAL_UNACCEPTABLE_INFAMY_FACTOR | 0 | # Wargoal value is multiplied by this if it would bring the country above unacceptable infamy levels |
| WAR_GOAL_NOT_PRIMARY_DEMAND_FACTOR | 0.5 | # Wargoal value for sway offers is multiplied by this if it would not be added as a primary demand |
| # Stickness factors for the different strait settings. Higher values means the AI is more likely to stick to their existing setting. |  |  |
| STRAIT_ACCESS_STATUS_STICKYNESS | 1.25 |  |
| STRAIT_ACCESS_PERMISSIONS_STICKYNESS | 1.25 |  |
| STRAIT_TOLL_RATES_STICKYNESS | 1.25 |  |
| WAR_GOAL_MAKE_PRIMARY_DEMAND_SCORE_MULT | 0.75 | # Multiply score of an existing wargoal by this when determining whether to make it into a primary demand instead of adding a new wargoal |
| WAR_GOAL_MAKE_PRIMARY_DEMAND_RETURN_STATE_SCORE_MULT | 1.25 | # Overrides WAR_GOAL_MAKE_PRIMARY_DEMAND_SCORE_MULT for return state wargoals |
| WAR_GOAL_MIN_SCORE_TO_MAKE_PRIMARY_DEMAND | 30 | # A wargoal needs to have at least this much score (before applying WAR_GOAL_MAKE_PRIMARY_DEMAND_SCORE_MULT) for AI to make it a primary demand |
| # Below data is used to determine which techs the AI will research |  |  |
| TECH_RANDOM_FACTOR | 1.0 | # The higher this is, the more random AI tech research will be |
| TECH_COST_PENALTY_FACTOR | 5.0 | # AI tendency to research a tech is divided by ( 1 + this * ahead of time penalty / era base cost ) |
| INCORPORATE_STATE_MAX_YEARS | 8.5 | # Max years that incorporation is allowed to take for the AI to incorporate a state |
| INCORPORATE_STATE_MIN_POPULATION | 200000 | # Below data is used to determine which states the AI should incorporate # Min population in a homeland state for the AI to incorporate it |
| # Below data is used to determine which states are most important to defend |  |  |
| DEFEND_STATE_BARRACKS_WEIGHT | 1 | # Per level of barracks |
| DEFEND_STATE_BARRACKS_MAX_WEIGHT | 20 | # Per state |
| DEFEND_STATE_NAVAL_ADMINISTRATION_WEIGHT | 0.5 | # Per level of naval admin |
| DEFEND_STATE_NAVAL_ADMINISTRATION_MAX_WEIGHT | 10 | # Per state |
| DEFEND_STATE_CAPITAL_WEIGHT | 25 |  |
| DEFEND_STATE_CAPITAL_WAR_NEGOTIATOR_WEIGHT | 100 |  |
| DEFEND_STATE_OWN_CAPITAL_WEIGHT_MULT | 5 |  |
| DEFEND_STATE_WARGOAL_WEIGHT | 100 |  |
| DEFEND_STATE_INCORPORATED_WEIGHT_MULT | 1.5 |  |
| # Below data is used to determine which states are most important to invade |  |  |
| INVADE_STATE_BARRACKS_WEIGHT | 1 | # Per level of barracks |
| INVADE_STATE_BARRACKS_MAX_WEIGHT | 20 | # Per state |
| INVADE_STATE_NAVAL_ADMINISTRATION_WEIGHT | 0.5 | # Per level of naval admin |
| INVADE_STATE_NAVAL_ADMINISTRATION_MAX_WEIGHT | 10 | # Per state |
| INVADE_STATE_CAPITAL_WEIGHT | 25 |  |
| INVADE_STATE_CAPITAL_WAR_NEGOTIATOR_WEIGHT | 100 |  |
| INVADE_STATE_OWN_CAPITAL_WEIGHT_MULT | 5 |  |
| INVADE_STATE_WARGOAL_WEIGHT | 100 |  |
| INVADE_STATE_INCORPORATED_WEIGHT_MULT | 1.5 |  |
| # Below data is used for invasions: |  |  |
| LAND_INVASION_RANDOM_FACTOR | 0.5 | # The higher this is, the more random AI land invasion theater selection will be |
| LAND_INVASION_MIN_RELATIVE_LOCAL_ARMY_STRENGTH | 0.5 | # AI wants at least this fraction of defending army strength to risk at a land invasion |
| LAND_INVASION_MIN_SCORE | 100 | # AI won't bother launching land invasions against theaters with a lower total state score than this |
| LAND_INVASION_MAX_LOCAL_FRONT_SCORE | 100 | # Don't launch a land invasion if there is a local front of at least this total score for the army |
| LAND_INVASION_MAX_TRAVEL_TIME_DAYS | 30 | # Don't invade with an army that is this far away from the state |
| LAND_INVASION_TRAVEL_TIME_PENALTY | 0.5 | # The further army is from the state, the lower the score: total = combat power * (1 - this * (travel time / LAND_INVASION_MAX_TRAVEL_TIME_DAYS)) |
| LAND_INVASION_MAX_AVAILABLE_ARMY_FRACTION | 0.5 | # No more than this fraction of available armies can be used in land invasions at the same time |
| LAND_INVASION_CANCEL_SCORE_THRESHOLD | 50 | # Cancel invasion if its score is less than this |
| NAVAL_INVASION_RANDOM_FACTOR | 0.5 | # The higher this is, the more random AI naval invasion theater selection will be |
| NAVAL_INVASION_MIN_RELATIVE_LOCAL_ARMY_STRENGTH | 0.25 | # AI wants at least this fraction of defending army strength to risk a naval invasion |
| NAVAL_INVASION_MIN_RELATIVE_LOCAL_NAVY_STRENGTH | 0.5 | # AI wants at least this fraction of defending naval strength to risk a naval invasion |
| NAVAL_INVASION_MIN_RELATIVE_GLOBAL_NAVY_STRENGTH_ATTACKER | 0.25 | # AI wants at least this fraction of naval strength in the overall war to risk a naval invasion as the attacking war side |
| NAVAL_INVASION_MIN_RELATIVE_GLOBAL_NAVY_STRENGTH_DEFENDER | 0.5 | # AI wants at least this fraction of naval strength in the overall war to risk a naval invasion as the defending war side |
| NAVAL_INVASION_COOLDOWN_DAYS | 20 | # After launching a naval invasion, the AI will wait at least this long before launching another |
| NAVAL_INVASION_MIN_SCORE | 100 | # AI won't bother launching naval invasions against theaters with a lower total state score than this |
| NAVAL_INVASION_INVADE_STATE_WARGOAL_WEIGHT | 500 | # Wargoal state weight for naval invasion target selection (higher than front-based INVADE_STATE_WARGOAL_WEIGHT) |
| NAVAL_INVASION_MAX_TARGET_CANDIDATES | 5 | # Number of candidate target states to consider per invasion (tries in score order until one passes garrison checks) |
| NAVAL_INVASION_HIGH_VALUE_STATE_THRESHOLD | 100 | # If target state importance is at least this, always send regular army support alongside marines |
| NAVAL_INVASION_MAX_LOCAL_FRONT_SCORE | 100 | # Don't launch a naval invasion if there is a local front of at least this total score for the general |
| NAVAL_INVASION_CANCEL_SCORE_THRESHOLD | 50 | # Cancel invasion if its score is less than this |
| NAVAL_INVASION_MAX_AVAILABLE_ARMY_FRACTION | 0.5 | # No more than this fraction of available armies can be used in naval invasions at the same time |
| NAVAL_INVASION_MAX_AVAILABLE_FLEET_FRACTION | 0.5 | # No more than this fraction of available fleets can be used in naval invasions at the same time |
| SUPPLY_SHIP_STRAIN_START_RATIO | 0.75 | # Supply ship usage ratio where scoring penalty begins (0.99x mult) |
| SUPPLY_SHIP_STRAIN_MAX_RATIO | 2.0 | # Supply ship usage ratio where max scoring penalty applies (0.05x mult) |
| SUPPLY_SHIP_STRAIN_MULT_AT_START | 0.99 | # Score multiplier at start ratio |
| SUPPLY_SHIP_STRAIN_MULT_AT_FULL | 0.75 | # Score multiplier at 100% supply ship usage |
| SUPPLY_SHIP_STRAIN_MULT_AT_MAX | 0.05 | # Score multiplier at max ratio |
| MARINE_FORMATION_TAG_MIN_FRACTION | 0.5 | # Min fraction of marine units to tag a formation as Marine |
|  |  | # Shipbuilding defines |
| SHIP_TEMPLATE_CREATION_MIN_SCORE_FACTOR | 1.5 | # AI will only create a new ship template if its modification score is at least this many times better than the best existing template of the same type |
| SHIP_RETROFIT_MIN_SCORE_FACTOR | 2.0 | # AI will only retrofit ships if the target template's total score is at least this many times the current template's score |
| FLEET_RECALL_HULL_RATIO_WAR | 0.75 | # At war or in a diplomatic play, recall fleets with average hull at or below this ratio |
| FLEET_RECALL_HULL_RATIO_PEACE | 1.0 | # At peace, recall fleets with average hull below this ratio (1.0 = recall any damaged fleet) |
| FLEET_RECALL_CREW_RATIO_WAR | 0.75 | # At war or in a diplomatic play, recall fleets with average crew at or below this ratio |
| FLEET_RECALL_CREW_RATIO_PEACE | 1.0 | # At peace, recall fleets with average crew below this ratio (1.0 = recall any undermanned fleet) |
| FLEET_RECALL_MIN_MISSION_SCORE | 0.5 | # Recall fleets whose best mission score is below this threshold |
| SHIP_DESIGN_MODIFICATION_RANDOM_FACTOR | 0.25 | # Random factor applied to AI modification weights when designing ships, creating per-country variance |
| SHIP_CONSTRUCTION_WANTED_SHIPS_TO_BUILD_COST_FACTOR | 1.0 | # This is multiplied by the cost of the ships the AI wants to build to determine how much the AI wants to build them. The higher this is, the more the AI is willing to spend on wanted ships |
| SHIP_CONSTRUCTION_WANTED_BUILT_SHIPS_COST_FACTOR | 0.3 | # This is multiplied by the cost of the existing ships, so that it allocates extra construction points for repairs/retrofitting |
| SHIP_CONSTRUCTION_DEBT_RESUME | 0.1 | # If ship constructions are paused, resume once debt is this low relative to ceiling |
| SHIP_CONSTRUCTION_DEBT_PAUSE | 0.3 | # If in this much relative debt to debt ceiling, pause all ship constructions |
| MIN_SHIPS_TO_TRANSFER | 5 | # AI will not transfer ships between fleets unless at least this many are being transferred |
| SHIP_TRANSFER_BASE_VALUE_PER_CONSTRUCTION_POINT | 150 | # Base £ per construction point used for AI ship valuation (e.g. ship_transfer treaty acceptance). Above the empirical ~£40/CP replacement cost so that target-side acceptance scores clear int32 truncation for mid-tier capital ships at multi-year bindings. |
| DISBAND_OBSOLETE_SHIP_DAYS | 3650 | # If a ship has been marked obsolete by the AI for at least this many days (~10 years) and hasn't been sold/transferred away, the AI decommissions it outright. Paired with ship_transfer: ships will ideally be sold before this threshold fires. |
| DISBAND_OBSOLETE_SHIP_CREW_RATIO | 0.8 | # If the ratio of crew needed to max available sailors exceeds this value, the AI will immediately decommission obsolete ships regardless of how long they've been obsolete |
| SHIP_CONSTRUCTION_BLOCK_CREW_RATIO | 1.0 | # If the ratio of crew needed to max available sailors is at or above this value, the AI will not queue new ship constructions |
| SUPPLY_SHIP_ALLOCATION_HIGH_RATIO | 0.5 | # If current supply ships are below this ratio of wanted, AI uses High supply construction allocation |
| SUPPLY_SHIP_ALLOCATION_LOW_RATIO | 1.0 | # If current supply ships are above this ratio of wanted, AI uses Low supply construction allocation |
| SUPPLY_SHIP_ALLOCATION_VERY_LOW_RATIO | 1.5 | # If current supply ships are above this ratio of wanted, AI uses Very Low supply construction allocation |
| DISBAND_EXCESS_SUPPLY_SHIPS_MIN_RATIO | 2.0 | # AI only decommissions available supply ships when they exceed this ratio of wanted, then goes down to wanted |
| DISBAND_EXCESS_SUPPLY_SHIPS_MAX_COUNT | 10 | # Maximum number of excess supply ships the AI will decommission per update |
| # Below data is used for General Orders: |  |  |
| HQ_DEFENSE_MIN_THEATER_SCORE | 100 | # Theater of local HQ must have at least this importance score to have a minimum garrison |
| NUM_DAYS_TO_REMEMBER_FAILED_FRONT_OR_HQ_ASSIGNMENT | 10 | # For how many days should the AI remember failing to assign a general to a front or HQ (and thus not try with that front again) |
| NUM_DAYS_TO_REMEMBER_FAILED_SUPPLY_ROUTE | 30 | # For how many days should the AI remember that a formation failed to find a supply route to a target |
| NUM_DAYS_TO_REMEMBER_FAILED_NAVAL_INVASION | 100 | # For how many days should the AI remember that a regular formation failed to launch a naval invasion |
| FRONT_OR_HQ_IMPORTANCE_MIN_SCORE | 50 | # If a front is worth less than this, the AI will not assign any generals to it |
| # Below data is for evaluating Commander Orders |  |  |
| FRONT_IMPORTANCE_OWN_FRONT_WEIGHT_MULT | 2.0 | # Fronts that we 'own' have the importance of their states multiplied by this |
| HQ_STATIONING_IMPORTANCE_NOT_OWN_HQ_WEIGHT_MULT | 0.25 | # HQs of allies have their importance multiplied by this as the AI prefers stationing in its own HQs |
| HQ_OR_FRONT_UNDEFENDED_ASSIGNMENT_WEIGHT | 2.0 | # Undefended HQs and Fronts are given preference by this multiplier for assignment of formations there |
| HQ_OR_FRONT_SPLIT_FORCE_BASE_FRACTION | 1.0 | # If splitting a force to cover undefended HQs/fronts, this is the fraction of the source formation that is sent when the two locations have an equal disparity in needed forces IF the army considered for splitting was not present |
| HQ_OR_FRONT_SPLIT_FORCE_MIN_FRACTION | 0.1 | # If splitting a force to cover undefended HQs/fronts, never send or leave behind less than this fraction of the source formation |
| HQ_OR_FRONT_SPLIT_FORCE_DEFENDED_LOCATION_MIN_FRACTION_TO_SEND | 0.33 | # If splitting a force to cover undefended HQs/fronts, don't send splinter armies to already defended fronts if the split of the source formation ends up smaller than this |
| # If no fleet can carry an entire army for naval transport, the AI will split the army if the best fleet can carry at least this fraction of the army |  |  |
| TRANSPORT_SPLIT_MIN_FLEET_CAPACITY_FRACTION | 0.2 |  |
| UNITS_PERCENTAGE_TO_BE_CONSIDERED_IN_DISADVANTAGE | 0.50 | # A percentage [0.0, 1.0] representing how many AI units are on a front out of the total (AI's + Enemy's) units, used to determine when to start applying FRONT_IMPORTANCE_WEIGHT_WHEN_IN_DISADVANTAGE. |
| # When considering whether to move a general to a particular location, the disparity between wanted and current units of the new location is divided 1 + any relevant values below # This is done to prevent the AI from making costly moves that would only result in small efficiency increases |  |  |
| FRONT_OR_HQ_UNIT_DISPARITY_FOR_MOVE_TRAVEL_TIME_FACTOR | 0.02 | # Each day of travel time adds this much to the divisor |
| FRONT_OR_HQ_ACTIVE_WAR_MOVE_FACTOR | 1.0 | # If a general is in an active war front, add this value to the divisor |
| # The values below are all applied *after* FRONT_IMPORTANCE_MIN_SCORE is checked, so a front/HQ isn't going to be qualified or disqualified for AI actually caring about it by these multipliers |  |  |
| FRONT_CAPITAL_HQ_IMPORTANCE_MULT | 2.0 | # Fronts that threaten the AI's own capital HQ have their importance multiplied by this |
| FRONT_NON_WAR_ZONE_IMPORTANCE_MULT | 1.0 | # Fronts that are not being contested by the enemy have their importance multiplied by this |
| FRONT_WAR_ZONE_IMPORTANCE_MULT | 1.5 | # Fronts that *are* being contested by the enemy have their importance multiplied by this |
| HQ_LANDLOCKED_IMPORTANCE_MULT | 0.0 | # Friendly HQs without a coast have their importance multiplied by this |
| HQ_COASTAL_NON_WAR_ZONE_IMPORTANCE_MULT | 0.5 | # Friendly HQs with a coast that are not under naval invasion have their importance multiplied by this |
| HQ_COASTAL_WAR_ZONE_IMPORTANCE_MULT | 3.0 | # Friendly HQs that *are* under naval invasion have their importance multiplied by this |
| FRONT_IN_DISADVANTAGE_FACTOR | 10.0 | # If a general is in an active war front with disadvantage, add this value to the divisor |
| # At what fraction of combat strength and morale/org will the AI attack |  |  |
| FRONT_MIN_OVERALL_STRENGTH_FACTOR_TO_ATTACK | 0.8 | # Must have at least this multiplier of overall power projection on the front compared to the enemy's to want to attack |
| FRONT_MIN_INDIVIDUAL_ARMY_STRENGTH_FACTOR_TO_ATTACK | 0.95 | # Must have at least this multiplier of average power projection of allied formations on the front to want to attack |
| FRONT_MIN_MORALE_TO_ATTACK | 0.8 | # As a fraction of max morale (1) |
| FRONT_MIN_ORGANIZATION_TO_ATTACK | 0.4 | # As a fraction of formation's max organization |
| FRONT_NO_WARGOAL_MIN_STRENGTH_FACTOR_TO_ATTACK | 4.0 | # If no explicit wargoal states remain uncaptured in enemy theater, require at least this strength multiplier to advance |
| # Below data is used for Admiral Orders: |  |  |
| BLOCKADE_STATE_TRADE_VOLUME_MILITARY_GOODS_WEIGHT | 5.0 | # Score weight for state blockade based on the trade volume of military goods in the state |
| BLOCKADE_STATE_TRADE_VOLUME_OTHER_GOODS_WEIGHT | 1.0 | # Score weight for state blockade based on the trade volume of other goods in the state |
| BLOCKADE_STATE_WEIGHT | 1 | # Score weight for state blockade based on the total score. The higher this is the more likely AI will choose to blockade the state rather than other offensive orders in the sea node |
| BLOCKADE_ORDER_LEVEL_DELTA_WEIGHT | 100 | # Score weight for admiral order based on how much blockade level this admiral provides |
| BLOCKADE_ORDER_NAVY_STRENGTH_RATIO_MULT | 1 | # Navy strength ratio increases the blockade order score by this: score = score * (1 + navy strength ratio * this) |
| FLEET_MISSION_INTERCEPT_WEIGHT | 1.5 | # Score weight for interception (defend HQ coasts) among other tasks in the sea province |
| FLEET_MISSION_PROJECT_POWER_WEIGHT | 1.0 | # Score weight for project power task among other tasks in the sea province |
| FLEET_MISSION_BLOCKADE_WEIGHT | 3.0 | # Score weight for blockade among other tasks in the sea province |
| FLEET_MISSION_RAID_SUPPLY_WEIGHT | 3.0 | # Score weight for raid military supply among other tasks in the sea province |
| FLEET_MISSION_PROTECT_SUPPLY_WEIGHT | 2.0 | # Score weight for escorting military supply among other tasks in the sea province |
| FLEET_MISSION_PORT_BOMBARDMENT_WEIGHT | 1.0 | # Score weight for port bombardment among other tasks in the sea province |
| FLEET_MISSION_PIRACY_WEIGHT | 1.0 | # Score weight for commercial raiding against neutrals & hostiles in the sea province |
| FLEET_MISSION_PRIVATEER_WEIGHT | 1.0 | # Score weight for commercial raiding against hostiles in the sea province |
| FLEET_MISSION_HUNT_PIRATES_WEIGHT | 1.0 | # Score weight for defending against commercial raiding in the sea province |
| FLEET_MISSION_DEFEND_COAST_WEIGHT | 5.0 | # Score weight for defending the coast against naval invasion & blockades |
| FLEET_TASK_ASSIGNMENT_RANDOM_SPICE | 0.5 | # Random factor for fleet mission selection, also determines stickiness to prevent flip-flopping |
| FLEET_SEA_PROVINCE_ASSIGNMENT_STICKINESS | 1.5 | # Fleet-to-sea-province score is multiplied by this when the fleet is already assigned to that province |
| FLEET_SEA_PROVINCE_SETTLING_DAYS | 60 | # Days for the settling stickiness multiplier to decay from max to 1x |
| FLEET_SEA_PROVINCE_SETTLING_STICKINESS_MULT | 4.0 | # Extra stickiness multiplier for recently assigned fleets (at day 0), linearly decays to 1x over SETTLING_DAYS |
| FLEET_SEA_PROVINCE_HOME_HQ_SCORE | 0.5 | # The higher this is the more likely fleets would defend their home HQs |
| FLEET_SEA_PROVINCE_DISTANCE_SCORE | 1 | # The higher this is the more the distance to the sea province matters for fleet task score |
| FLEET_SEA_PROVINCE_DISTANCE_SCORE_MAX_DISTANCE | 5000 | # Distance score is calculated linearly from 0 to this using effective supply distance (pathfinding with friendly port discount) |
| FLEET_RAID_CONVOYS_TASK_SCORE_FROM_STRENGTH | 2 | # The higher this is the more likely fleets with high convoy raiding strength would do the convoy raiding task |
| FLEET_ESCORT_CONVOYS_TASK_SCORE_FROM_DEFENSE | 2 | # The higher this is the more likely fleets with high convoy escorting strength would do the convoy escorting task |
| FLEET_PROJECT_INTEREST_TASK_SCORE_FROM_INTEREST_PROJECTION | 2 | # The higher this is the more likely fleets with high project interest strength would do the project interest task |
| FLEET_DEFEND_FROM_CONVOY_RAID_TASK_SCORE_FROM_PROTECTION | 2 | # Is scaled by the amount of convoys that the fleet would protect and counts towards the fleet score for the task |
| FLEET_DEFEND_FROM_NAVAL_INVASION_TASK_SCORE_FROM_PROJECTION | 0.5 | # The higher this is the more likely fleets with high power projection would defend from naval invasion and block enemies from landing |
| FLEET_DEFEND_FROM_NAVAL_INVASION_TASK_SCORE_FROM_SHIPS | 0.1 | # Is scaled by the amount of ships that the fleet has and counts towards the fleet score for the task |
| FLEET_DEFEND_FROM_BLOCKADE_TASK_SCORE_FROM_STRENGTH | 1.5 | # The higher this is the more likely fleets with stronger ships would defend from enemy blockades |
| FLEET_BLOCKADE_TASK_SCORE_FROM_STRENGTH | 1.5 | # The higher this is the more likely fleets with high blockade strength would blockade enemy states |
| FLEET_BLOCKADE_TASK_SCORE_NO_HOSTILES | 0.5 | # Gives a boost to priority if there are no hostiles present |
| FLEET_BLOCKADE_TASK_SCORE_STRENGTH_RATIO_FACTOR | 1.5 # How much the strength ratio between hostiles/friendlies affect the weighting |  |
| FLEET_PORT_BOMBARDMENT_TASK_SCORE_NO_HOSTILES | 0.5 | # Gives a boost to priority if there are no hostiles present |
| FLEET_PORT_BOMBARDMENT_TASK_SCORE_STRENGTH_RATIO_FACTOR | 1.5 # How much the strength ratio between hostiles/friendlies affect the weighting |  |
| FLEET_INTERCEPT_TASK_SCORE_STRENGTH_RATIO_FACTOR | 3.0 # How much the strength ratio between hostiles/friendlies affect the weighting |  |
| FLEET_MISSION_MAX_SEA_REGIONS | 3 | # Max sea regions a fleet mission can be assigned to by the AI |
| RAID_CONVOYS_ORDER_SCORE | 30 | # Score for admiral order to raid convoys |
| INTERCEPT_ORDER_SCORE | 40 | # Score for admiral order to intercept |
| SEA_NODE_OFFENSIVE_FLEET_SHIPPING_LANES_WEIGHT | 0.5 | # Score weight for sea node based on the total score for AI to raid convoys. The higher this is the higher AI will prioritize sea nodes with enemy convoys to raid |
| SEA_NODE_OFFENSIVE_FLEET_STATE_BLOCKADE_WEIGHT | 0.5 | # Score weight for sea node based on the total score for AI to blockade states. The higher this is the higher AI will prioritize sea nodes with potential states to blockade |
| RAID_CONVOYS_LANE_SIZE_FACTOR | 0.5 | # Multiplied by the number of convoys that the target shipping lane uses |
| ESCORT_CONVOYS_ABSOLUTE_LANE_SIZE_FACTOR | 0.1 | # Apply this score per actual convoy used by the route |
| ESCORT_CONVOYS_LANE_SIZE_FACTOR_MAX | 200 | # Total lane size factor cannot be above this |
| ESCORT_CONVOYS_PORT_CONNECTION_WAR_MULT | 0.1 | # Score for shipping lanes supporting overseas ports multiplied by this while at war |
| ESCORT_CONVOYS_PORT_CONNECTION_PEACE_MULT | 1.0 | # Score for shipping lanes supporting overseas ports multiplied by this while not at war |
| # Below data is used to determine which states should be colonized first |  |  |
| NUM_GROWING_COLONIES_BASE | 1 | # How many colonies will the AI keep growing at once (base amount) |
| NUM_GROWING_COLONIES_SCALED | 0.01 | # 1 extra colony at once per this amount of colonial growth points |
| NUM_GROWING_COLONIES_MAX | 5 | # No more than this amount of growing colonies at once, regardless of amount of colonial growth points |
| COLONY_BASE_WEIGHT | 50 |  |
| COLONY_POPULATION_WEIGHT | 0.2 | # Per 10000 pops |
| COLONY_ARABLE_LAND_WEIGHT | 10 |  |
| COLONY_ADJACENT_WEIGHT_MULT | 10.0 |  |
| COLONY_UNCONTESTED_WEIGHT_MULT | 3.0 |  |
| COLONY_RANDOM_FACTOR | 2 |  |
| # This determines how much of their potential conscripts' needed military goods the AI will try to supply even when those conscripts are not raised |  |  |
| CONSCRIPTION_CENTER_MILITARY_SPENDING_TARGET_BASE | 0.05 | # Multiplied by the country's ratio of conscripts to regular troops |
| CONSCRIPTION_CENTER_MILITARY_SPENDING_TARGET_MAX | 0.25 | # Spending target cannot exceed this amount |
| # Below data is used to determine how the AI invests into institution |  |  |
| INSTITUTION_INVESTMENT_RANDOM_FACTOR | 1.0 | # The higher this is, the more random AI institution selection will be |
| INSTITUTION_CURRENT_INVESTMENT_DIVISOR | 0.25 | # Score for institution is divided by 1 + ( current levels after the first * this ) |
| MAX_INSTITUTION_SPENDING_BASE | 0.015 | # AI will not spend more BUR than this on institutions (scaled by weekly GDP) |
| MAX_INSTITUTION_SPENDING_PER_INSTITUTION | 0.005 | # Added to MAX_INSTITUTION_SPENDING_BASE for each institution a country has |
| INSTITUTION_SPENDING_INCREASE_SPENDING_RATIO | 1.0 | # If current + additional institution spending is equal or less than max spending * this, try to improve some institutions |
| INSTITUTION_SPENDING_DECREASE_SPENDING_RATIO | 2.0 | # If current institution spending is at least max spending * this, try to degrade some institutions |
| # Below data is used to calculate how much weight the AI places on different things it can spend its weekly money income on |  |  |
| MONEY_SPENDING_RANDOM_FACTOR | 2.0 | # The higher this is, the more random new AI money spending will be |
| MONEY_SPENDING_MAX_RATIO_TO_REMOVE_SHOULD_HAVE | 1.05 | # How low of a income-to-expenses ratio does the AI need to have to consider reducing spending on a 'should-have' |
| MONEY_SPENDING_MAX_RATIO_TO_REMOVE_WANTS_TO_HAVE | 1.10 | # How low of a income-to-expenses ratio does the AI need to have to consider reducing spending on a 'wants-to-have' |
| MONEY_SPENDING_MAX_RATIO_TO_REMOVE_NICE_TO_HAVE | 1.20 | # How low of a income-to-expenses ratio does the AI need to have to consider reducing spending on a 'nice-to-have' |
| MONEY_SPENDING_MIN_RATIO_TO_ADD_SHOULD_HAVE | 1.2 | # How much of a income-to-expenses ratio does AI want to have after increasing spending for a 'should-have' project |
| MONEY_SPENDING_MIN_RATIO_TO_ADD_WANTS_TO_HAVE | 1.3 | # How much of a income-to-expenses ratio does AI want to have after increasing spending for a 'wants-to-have' project |
| MONEY_SPENDING_MIN_RATIO_TO_ADD_NICE_TO_HAVE | 1.4 | # How much of a income-to-expenses ratio does AI want to have after increasing spending for a 'nice-to-have' project |
| MONEY_SPENDING_MIN_SURPLUS_TO_ADD_SHOULD_HAVE | 2000 | # How much of a surplus in absolute money does AI want to have after increasing spending for a 'should-have' project |
| MONEY_SPENDING_MIN_SURPLUS_TO_ADD_WANTS_TO_HAVE | 5000 | # How much of a surplus in absolute money does AI want to have after increasing spending for a 'wants-to-have' project |
| MONEY_SPENDING_MIN_SURPLUS_TO_ADD_NICE_TO_HAVE | 10000 | # How much of a surplus in absolute money does AI want to have after increasing spending for a 'nice-to-have' project |
| MONEY_SPENDING_MIN_SURPLUS_TO_IGNORE_RATIO_FOR_SHOULD_HAVE | 15000 | # If AI has this surplus in absolute money, it's always fine to increase spending on a 'should-have' project, regardless of income ratio |
| MONEY_SPENDING_MIN_SURPLUS_TO_IGNORE_RATIO_FOR_WANTS_TO_HAVE | 30000 | # If AI has this surplus in absolute money, it's always fine to increase spending on a 'wants-to-have' project, regardless of income ratio |
| MONEY_SPENDING_MIN_SURPLUS_TO_IGNORE_RATIO_FOR_NICE_TO_HAVE | 50000 | # If AI has this surplus in absolute money, it's always fine to increase spending on a 'nice-to-have' project, regardless of income ratio |
| MONEY_SPENDING_ACCEPTABLE_WAR_DEBT | 0.5 | # If the AI has less than this % debt to ceiling, avoid doing cost-cutting at war for 'wants to have' and above |
| MONEY_SPENDING_MIN_RATIO_TO_CONSIDER_GOLD_RESERVES | 0.8 | # How low of a income-to-expenses ratio does the AI need to have to try to cut spending regardless of how plentiful its gold reserves are (when at peace) |
| MONEY_SPENDING_MIN_WEEKS_OF_GOLD_RESERVES_TO_NOT_REMOVE_SHOULD_HAVE | 20 | # If we have enough gold reserves to maintain our current spending for this long, don't decrease spending on a 'should-have' |
| MONEY_SPENDING_MIN_WEEKS_OF_GOLD_RESERVES_TO_NOT_REMOVE_WANTS_TO_HAVE | 40 | # If we have enough gold reserves to maintain our current spending for this long, don't decrease spending on a 'wants-to-have' |
| MONEY_SPENDING_MIN_GOLD_RESERVE_FRACTION_TO_ADD_SHOULD_HAVE | 0.1 | If we don't have at least this fraction of gold reserves, don't increase spending on a 'should-have' |
| MONEY_SPENDING_MIN_GOLD_RESERVE_FRACTION_TO_ADD_WANTS_TO_HAVE | 0.2 | # If we don't have at least this fraction of gold reserves, don't increase spending on a 'wants-to-have' |
| MONEY_SPENDING_MIN_GOLD_RESERVE_FRACTION_TO_ADD_NICE_TO_HAVE | 0.3 | # If we don't have at least this fraction of gold reserves, don't increase spending on a 'nice-to-have' |
| MONEY_SPENDING_LAND_THREAT_THRESHOLD | 0.25 | # If a hostile country has a more than this much larger army than AI does, it wants to increase military spending |
| MONEY_SPENDING_NAVY_THREAT_THRESHOLD | 0.50 | # If a hostile country has a more than this much larger navy than AI does, it wants to increase military spending |
| MONEY_SPENDING_PRESTIGE_RIVAL_THRESHOLD | 0.5 | # If a rival has this much more prestige than AI does, it wants to increase spending on art academies |
| MONEY_SPENDING_BELOW_CRITICAL_THRESHOLD_MULTIPLIER | 5.0 | # Increase scoring for money spending of certain items that are below critical thresholds by this (as specified by CRITICAL_THRESHOLD defines below) |
| MONEY_SPENDING_MILITARY_CRITICAL_THRESHOLD | 0.5 | # If actual-to-wanted number of barracks is below this, AI will not consider downsizing them further |
| MONEY_SPENDING_MILITARY_EXCESSIVE_THRESHOLD | 2.0 | # If actual-to-wanted number of barracks is above this, AI considers it a target for cutting spending when needed |
| MONEY_SPENDING_MILITARY_WRONG_UNIT_TYPE_MULTIPLIER | 0.01 | # Score multiplier for decreasing spending on barracks that lack combat units of the type we want to disband |
| MONEY_SPENDING_FORTIFICATIONS_CRITICAL_THRESHOLD | 0.5 | # If actual-to-wanted number of fortifications is below this, AI increases priority to construct them |
| MONEY_SPENDING_CONSTRUCTION_TOO_LARGE_INVESTMENT_POOL_FACTOR | 0.75 | # The higher this is, the more the AI will invest into construction when their investment pool has grown too large for their construction capacity (capped at 1) |
| MONEY_SPENDING_CONSTRUCTION_CRITICAL_THRESHOLD | 0.75 | If actual-to-wanted construction production is below this, AI considers it very important to get more |
| MONEY_SPENDING_CONSTRUCTION_EXCESSIVE_THRESHOLD | 1.05 | # If actual-to-wanted construction production is at least this, AI considers it nice to have |
| MONEY_SPENDING_SHIP_CONSTRUCTION_CRITICAL_THRESHOLD | 0.75 | # If actual-to-wanted ship construction production is below this, AI considers it very important to get more |
| MONEY_SPENDING_SHIP_CONSTRUCTION_EXCESSIVE_THRESHOLD | 1.05 | # If actual-to-wanted ship construction production is at least this, AI considers it nice to have |
| MONEY_SPENDING_INNOVATION_DESIRED_THRESHOLD | 1.0 | # If innovation production compared to cap is worse than this, AI considers it important to improve |
| MONEY_SPENDING_INNOVATION_EXCESSIVE_THRESHOLD | 1.25 | CONSUMPTION_TAX_MAX_NUM_TAXED_GOODS_PER_MISSING_TAX_TYPE# If innovation production compared to cap is at least this, AI considers it nice to have |
| MONEY_SPENDING_SUPPLY_NETWORK_CRITICAL_THRESHOLD | 0.75 | # If supply network is worse than this, AI considers it critical to improve it |
| MONEY_SPENDING_SUPPLY_NETWORK_DESIRED_THRESHOLD | 1.25 | # If supply network is worse than this, AI wants to improve it |
| MONEY_SPENDING_BUREAUCRACY_CRITICAL_THRESHOLD | 1.0 | # If bureaucracy income to expenses is worse than this, AI considers it critical to improve it |
| MONEY_SPENDING_BUREAUCRACY_DESIRED_THRESHOLD | 1.20 | # If bureaucracy income to expenses is worse than this, AI wants to improve it |
| MONEY_SPENDING_BUREAUCRACY_EXCESSIVE_THRESHOLD | 1.30 | # If bureaucracy income to expenses is better than this, AI will not improve it |
| MONEY_SPENDING_INFRASTRUCTURE_CRITICAL_THRESHOLD | 0.80 | # If infra production to usage is worse than this, AI considers it critical to improve it |
| MONEY_SPENDING_INFRASTRUCTURE_DESIRED_THRESHOLD | 1.20 | # If infra production to usage is worse than this, AI wants to improve it |
| # Below data is used to calculate how much weight the AI places on specific government buildings |  |  |
| GOVERNMENT_BUILDING_BASE_VALUE | 1000 | # If no ai_value is scripted in the building |
| GOVERNMENT_BUILDING_FAVORED_GOODS_FACTOR | 0.25 | # Total weight is multiplied by ( 1 + this ) for each building output that the AI favors for either import or export |
| GOVERNMENT_BUILDING_DISFAVORED_GOODS_FACTOR | -0.10 | # Total weight is multiplied by ( 1 + this ) for each building output good that the AI disfavors |
| GOVERNMENT_BUILDING_NO_AVAILABLE_WORKFORCE_FACTOR | 0.01 | # Total weight is multiplied by this if the state lacks enough workforce to staff the building |
|  |  | # Below data is used to calculate where the AI will locate new government buildings |
| GOVERNMENT_BUILDING_STATE_CAPITAL_FACTOR | 250 | # Add this score for certain types of government buildings in the capital |
| GOVERNMENT_BUILDING_STATE_MARKET_CAPITAL_FACTOR | 250 | # Add this score for certain types of government buildings in the market capital |
| GOVERNMENT_BUILDING_STATE_ARMY_NON_ACCEPTED_POP_FACTOR | -250 | # Multiply this score by fraction of discriminated Pops in the state |
| GOVERNMENT_BUILDING_STATE_ARMY_ACCEPTED_POP_FACTOR | 250 | # Multiply this score by fraction of accepted Pops in the state |
| GOVERNMENT_BUILDING_STATE_NAVY_NON_ACCEPTED_POP_FACTOR | -250 | # Multiply this score by fraction of discriminated Pops in the state |
| GOVERNMENT_BUILDING_STATE_NAVY_ACCEPTED_POP_FACTOR | 250 | # Multiply this score by fraction of accepted Pops in the state |
| GOVERNMENT_BUILDING_STATE_UNINCORPORATED_MULT | 0.25 | # Multiply score by this if the state is unincorporated |
| GOVERNMENT_BUILDING_STATE_MISSING_QUALIFICATIONS_MULT | 0.10 | # Multiply score by this if there's not enough qualifications to staff the building |
| GOVERNMENT_BUILDING_STATE_MISSING_INFRASTRUCTURE_DIV | 0.50 | # Divide score by ( 1 + this * number of missing infrastructure after adding this building ) |
| GOVERNMENT_BUILDING_STATE_POP_CONSTRUCTION_SECTOR_IMPORTANCE_THRESHOLD | 250000 | # Above this amount of state population, AI considers it important to have a construction sector in the state |
| GOVERNMENT_BUILDING_STATE_POP_CONSTRUCTION_SECTOR_IMPORTANCE_MULT | 1.5 | # Multiply score by this if state GDP is at least the above value for purposes of scoring the first level of construction sector |
| # Below data is used to calculate how much weight the AI places on specific subsidies |  |  |
| SUBSIDIZE_BASE_VALUE | 1000 |  |
| SUBSIDIZE_SHARE_OF_INFRA_FACTOR | 4000 | # How highly is subsidization of a building valued if it provides 100% of the infrastructure in the state region |
| SUBSIDIZE_SHARE_OF_SUPPLY_FACTOR | 2000 | # How highly is subsidization of a building valued if it provides 100% of the sell orders for a good in the market |
| SUBSIDIZE_FAVORED_GOODS_MULT | 1.5 | # Share of supply factor is multiplied by this for a good that the AI wants a high supply of |
| SUBSIDIZE_DISFAVORED_GOODS_MULT | 0.75 | # Share of supply factor is multiplied by this for a good that the AI disfavors |
| # Below data is used to calculate how much weight the AI places on different things it can spend its authority on |  |  |
| AUTHORITY_SPENDING_RANDOM_FACTOR | 0.5 | # The higher this is, the more random new AI authority spending will be |
| COMPANY_CHARTER_AUTHORITY_SPENDING_PERCENTAGE | 0.15 | #Ratio of authority expenses that we want country to spend on authority |
| PROMOTION_BASE_VALUE | 50 | # Below data is used to calculate how much weight the AI places on promoting an IG |
| SUPPRESSION_BASE_VALUE | 75 | # Below data is used to calculate how much weight the AI places on suppressing an IG |
| # Below data is used to calculate how much weight the AI places on consumption taxes |  |  |
| CONSUMPTION_TAX_INCOME_VALUE | 10 | # Per percent of state expenses in taxable value (this is then multiplied by relative authority cost of the good) |
| CONSUMPTION_TAX_STAPLE_MULT | 0.5 | # Multiply desire to tax staple goods by this |
| CONSUMPTION_TAX_LUXURY_MULT | 2.0 | # Multiply desire to tax luxury goods by this |
| CONSUMPTION_TAX_LOW_INCOME_THRESHOLD | 1.25 | # Income-to-expenses threshold below which consumption taxes are a must-have |
| CONSUMPTION_TAX_HIGH_INCOME_THRESHOLD | 1.5 | # Income-to-expenses threshold at which consumption taxes should be removed (if removal would not put us below this) |
| CONSUMPTION_TAX_MAX_NUM_TAXED_GOODS_BASE | 0 | # Base max number of goods AI wants to tax |
| CONSUMPTION_TAX_MAX_NUM_TAXED_GOODS_PER_MISSING_TAX_TYPE | 2 | # Added to max number of goods AI wants to tax for each other type of tax it does not collect |
| # GDP limiters on where the AI will construct Trade Centers - note that decreasing these can adversely affect performance! |  |  |
| TRADE_CENTER_MINIMUM_GDP_MARKET_CAPITAL | 100000 | # For market capital states, yearly GDP |
| TRADE_CENTER_MINIMUM_GDP_NON_MARKET_CAPITAL | 500000 | # For all other states, yearly GDP |
| TRADE_CENTER_MINIMUM_GDP_NON_COASTAL_MULT | 2.0 | # Multiplies the GDP threshold for non-coastal states (additive) |
| TRADE_CENTER_MINIMUM_GDP_UNRECOGNIZED_MULT | 2.0 | # Multiplies the GDP threshold for unrecognized countries (additive) |
| TRADE_CENTER_MINIMUM_GDP_PASSED_YEARS_MULT | 0.02 | # Above values are multiplied by 1 + ( number of years since game start * this ) (additive) |
| # Below data is used to calculate how much weight the AI places on a production building |  |  |
| PRODUCTION_BUILDING_RANDOM_FACTOR | 10.0 | # The higher this is, the more random AI construction will be |
| PRODUCTION_BUILDING_STATE_RANDOM_FACTOR | 0.5 | # The higher this is, the more random AI state selection for building types will be |
| PRODUCTION_BUILDING_STATE_NO_AVAILABLE_WORKFORCE_FACTOR | 0.05 | # Score for states with no available workforce is multiplied by this when selecting a state to build in |
| PRODUCTION_BUILDING_BASE_VALUE | 1000 | # If no ai_value is scripted in the building |
| PRODUCTION_BUILDING_NO_AVAILABLE_WORKFORCE_FACTOR | 0.25 | # Total weight is multiplied by this if the state lacks enough workforce to staff the building |
| PRODUCTION_BUILDING_GOODS_PROFIT_FACTOR | 5000 | # Per pound of predicted building profit (divided by employee count per level) |
| PRODUCTION_BUILDING_GOODS_DEFICIT_FACTOR | 10000 | # Per pound of predicted building deficit (divided by employee count per level and multiplies a negative value) |
| PRODUCTION_BUILDING_GOODS_DEFICIT_SUBSIDIZE_FACTOR | 5000 | # Overrides PRODUCTION_BUILDING_GOODS_DEFICIT_FACTOR for subsidized buildings |
| PRODUCTION_BUILDING_PRODUCED_VALUE_FACTOR | 0.25 | # Per pound of produced goods in base value |
| PRODUCTION_BUILDING_PRODUCED_TRADE_CAPACITY_FACTOR | 10000 | # Per produced trade capacity, multiplied by the available potential for trade in the state and divided by state GDP |
| PRODUCTION_BUILDING_PRODUCED_TRADE_CAPACITY_GDP_ADDED_FOR_DIVISOR | 10000 | # Added to state GDP when dividing PRODUCTION_BUILDING_PRODUCED_TRADE_CAPACITY_FACTOR |
| PRODUCTION_BUILDING_PRODUCED_TRADE_CAPACITY_EXPECTED_REVENUE_PER_UNIT | 25 | # Each trade capacity is loosely expected to generate about this much revenue, used when predicting revenue from new TCs |
| PRODUCTION_BUILDING_INCORPORATED_INFRASTRUCTURE_USAGE_FACTOR | 0.05 | # Total weight is divided by ( 1 + this * building infrastructure usage ) in incorporated states |
| PRODUCTION_BUILDING_UNINCORPORATED_INFRASTRUCTURE_USAGE_FACTOR | 1.0 | # Total weight is divided by ( 1 + this * building infrastructure usage ) in unincorporated states |
| PRODUCTION_BUILDING_INPUT_NO_LOCAL_PRODUCTION_FACTOR | -0.5 | # Add this value to a building for each unit of money worth of goods consumed that are not produced in the state but *are* produced by buildings in the market |
| PRODUCTION_BUILDING_OUTPUT_NO_LOCAL_CONSUMPTION_FACTOR | -0.5 | # Add this value to a building for each unit of money worth of goods produced that are not consumed in the state but *are* consumed by buildings in the market |
| PRODUCTION_BUILDING_OUTPUT_HIGH_PRICE_THRESHOLD | 1.25 | # Lower threshold multiplier of base price for applying 'high price' modifier below |
| PRODUCTION_BUILDING_OUTPUT_HIGH_PRICE_FACTOR | 0.25 | # Add this value to a building for each unit of money worth of goods above high price threshold that this building produces |
| PRODUCTION_BUILDING_OUTPUT_HIGH_PRICE_WANTS_HIGH_SUPPLY_FACTOR | 0.75 | # Add this value to a building for each unit of money worth of goods above high price threshold that this building produces and which we want a high supply of |
| PRODUCTION_BUILDING_OUTPUT_HIGH_PRICE_LOCAL_CONSUMPTION_MULTIPLIER | 2.0 | # All factors for high prices are multiplied by this value if any buildings in the state consume the good in question |
| PRODUCTION_BUILDING_OUTPUT_LOW_PRICE_THRESHOLD | 0.75 | # Upper threshold multiplier of base price for applying 'low price' modifier below |
| PRODUCTION_BUILDING_OUTPUT_LOW_PRICE_FACTOR | -0.5 | # Add this value to a building for each unit of money worth of goods below low price threshold that this building produces |
| PRODUCTION_BUILDING_SUBSIDIZE_PRICE_FACTOR_MULT | 1.25 | # Multiply the effects of price factors on buildings that the AI will consider subsidizing |
| PRODUCTION_BUILDING_OUTPUT_NEW_GOODS_FACTOR | 100.0 | # Add this value to a building for each unit of money worth of goods that currently isn't available in our market but the AI wants to prioritize |
| PRODUCTION_BUILDING_OUTPUT_NEW_GOODS_STATE_INCORPORATED_POPULATION_THRESHOLD | 250000 | # When the AI prioritizes 'new goods' in a state rather than a market (because of local goods) it only cares about incorporated states with at least this much population |
| PRODUCTION_BUILDING_OUTPUT_NEW_GOODS_STATE_UNINCORPORATED_POPULATION_THRESHOLD | 1000000 | # When the AI prioritizes 'new goods' in a state rather than a market (because of local goods) it only cares about unincorporated states with at least this much population |
| PRODUCTION_BUILDING_OUTPUT_WANTED_INDUSTRIAL_GOODS_FACTOR | 0.25 | # Add this value to a building for each unit of money worth of industrial goods that aren't overproduced in the country and are used by buildings |
| PRODUCTION_BUILDING_OUTPUT_WANTED_MILITARY_GOODS_FACTOR | 0.25 | # Add this value to a building for each unit of money worth of military goods that aren't overproduced in the country and are used by buildings |
| PRODUCTION_BUILDING_OUTPUT_NEEDED_INDUSTRIAL_GOODS_FACTOR | 0.5 | # Add this value to a building for each unit of money worth of industrial goods that are underproduced in the country and are used by buildings |
| PRODUCTION_BUILDING_OUTPUT_NEEDED_MILITARY_GOODS_FACTOR | 0.5 | # Add this value to a building for each unit of money worth of military goods that are underproduced in the country and are used by buildings |
| PRODUCTION_BUILDING_FAVORED_GOODS_FACTOR | 0.5 | # Add this value to a building for each unit of money worth of building goods output that the AI favors |
| PRODUCTION_BUILDING_DISFAVORED_GOODS_FACTOR | -0.25 | # Add this value to a building for each unit of money worth of building goods output that the AI disfavors |
| PRODUCTION_BUILDING_MISSING_QUALIFICATIONS_MULT | 0.50 | # Multiply score by this if there's not enough qualifications to staff the building (disabled for now) |
| PRODUCTION_BUILDING_DESIRED_INFRASTRUCTURE_SURPLUS | 2 | # If infrastructure 'surplus' in state is less than this, AI wants to improve it |
| PRODUCTION_BUILDING_FREE_INFRASTRUCTURE_TARGET_WHEN_LACKING_WORKFORCE | 5 | # When lacking workforce, the AI will stop building in the state once available infrastructure is this or less |
| PRODUCTION_BUILDING_EXCESSIVE_INFRASTRUCTURE_SURPLUS | 10 | # If infra 'surplus' in state is at least this, AI doesn't want to improve it |
| PRODUCTION_BUILDING_REDUCE_SHORTAGE_MULT | 5 | # Multiply score by this if we're reducing the state region's shortages |
| PRODUCTION_BUILDING_INCREASE_SHORTAGE_MULT | 0.01 | # Multiply score by this if we're increasing the state region's shortages |
| PRODUCTION_BUILDING_OTHER_BUILDING_TYPES_UNDER_CONSTRUCTION_DIV | 0.5 | # Divide score by (1 + this * number of other building types queued in the state) |
| PRODUCTION_BUILDING_LONG_CONSTRUCTION_TIME_THRESHOLD | 40 |  |
| PRODUCTION_BUILDING_LONG_CONSTRUCTION_TIME_MULT | 0.5 | # Multiply score by this if construction time would take more than PRODUCTION_BUILDING_LONG_CONSTRUCTION_TIME_THRESHOLD weeks at full construction industry usage (ignores MAX_WEEKLY_CONSTRUCTION_PROGRESS) |
| PRODUCTION_BUILDING_VERY_LONG_CONSTRUCTION_TIME_THRESHOLD | 60 |  |
| PRODUCTION_BUILDING_VERY_LONG_CONSTRUCTION_TIME_MULT | 0.25 | # Multiply score by this if construction time would take more than PRODUCTION_BUILDING_VERY_LONG_CONSTRUCTION_TIME_THRESHOLD weeks at full construction industry usage (ignores MAX_WEEKLY_CONSTRUCTION_PROGRESS) |
| PRODUCTION_BUILDING_FOREIGN_INVESTMENT_HAS_RECENT_NATIONALIZATION_MULT | 0.1 | # Multiply score by this if the construction is a foreign investment into a country that has recently nationalized buildings held by investor country |
| PRODUCTION_BUILDING_FOREIGN_INVESTMENT_COMPANY_MULT | 1.5 | # Multiply score by this if the construction is a foreign investment by the country that has at least one established company for the building type |
| # Government construction applies this multiplier to domestic states when determining where to construct |  |  |
| GOVERNMENT_CONSTRUCTION_DOMESTIC_INVESTMENT_BIAS | 2.0 |  |
| GOVERNMENT_CONSTRUCTION_SUBJECT_INVESTMENT_BIAS | 1.5 |  |
| # The AI is much more likely to select a state that fulfills the ai_construction_targets criteria for the next company it's planning to form # For example, when trying to form company_lkab it is much more likely to select Norrland as the # Values below determine the exact weight for this for government vs private investment # There are two sets of weights: One applied for the building type as a whole (when compared to other building types), and a second applied only when selecting the state for the building type |  |  |
| GOVERNMENT_COMPANY_TARGET_BUILDING_TYPE_CONSTRUCTION_FACTOR | 5 |  |
| GOVERNMENT_COMPANY_TARGET_STATE_NO_BUILDING_CONSTRUCTION_FACTOR | 20 | # Applied when the state does not already have the target building type |
| GOVERNMENT_COMPANY_TARGET_STATE_WITH_BUILDING_CONSTRUCTION_FACTOR | 50 | # Applied when the state *does* already have the target building type |
| AUTONOMOUS_INVESTMENT_COMPANY_TARGET_BUILDING_TYPE_CONSTRUCTION_FACTOR | 5 |  |
| AUTONOMOUS_INVESTMENT_COMPANY_TARGET_STATE_NO_BUILDING_CONSTRUCTION_FACTOR | 20 | # Applied when the state does not already have the target building type |
| AUTONOMOUS_INVESTMENT_COMPANY_TARGET_STATE_WITH_BUILDING_CONSTRUCTION_FACTOR | 50 | # Applied when the state *does* already have the target building type |
| # This much of collectivization fraction translates into self-investment chance for a building # Under total collectivization self investment chance is always 100% |  |  |
| AUTONOMOUS_INVESTMENT_SELF_INVESTMENT_CHANCE_FROM_COLLECTIVIZATION | 0.5 |  |
| PRODUCTION_BUILDING_TREATY_PORT_TRADE_CENTER_FACTOR | 5.0 | # Score for Trade Center buildings in Treaty Ports is multiplied by this when selecting state for a construction |
| PRODUCTION_BUILDING_TREATY_PORT_NON_TRADE_CENTER_FACTOR | 0.10 | # Score for non Trade Center buildings in Treaty Ports is multiplied by this when selecting state for a construction |
| # The factors below are only applied to government constructions |  |  |
| PRODUCTION_BUILDING_GOVERNMENT_CONSTRUCTION_MONOPOLY_MULT | 1.5 | # Multiply score by this if we have a government monopoly for the buildng type |
| PRODUCTION_BUILDING_LOW_EMPLOYMENT_THRESHOLD | 0.8 | # The AI will not expand buildings with less than this employment unless those buildings hired last week |
| # The factors below are only applied to autonomous investments |  |  |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_COMPANY_MULT | 2.0 | # Multiply score by 1 + this if we have at least one established company for the building type, scales by fraction of investment pool coming from companies compared to historical amount of investment by companies |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_COMPANY_MONOPOLY_MULT | 3.0 | # Replaces PRODUCTION_BUILDING_COMPANY_MULT for buildings on which a company has a monopoly |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_COMPANY_CHARTERED_COUNTRY_MULT | 2.0 | # Additional multiplier to company weights above if the investment is targeting a company's chartered country |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_WANTED_COST_COVERAGE | 1 | # If investment pool has less money than this in it, don't do any autonomous construction |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_CONSTRUCTION_COST_DIVISOR_SCALING | 0.001 | # Value for autonomous investment pool constructions is divided by ( 1 + construction point cost * this ) |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_RANDOM_FACTOR_MULT | 2.0 | # Multiplies PRODUCTION_BUILDING_RANDOM_FACTOR for autonomous investment pool constructions |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_STATE_RANDOM_FACTOR_MULT | 1.5 | # Multiplies PRODUCTION_BUILDING_RANDOM_FACTOR for autonomous investment pool constructions |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PROFIT_FACTOR_MULT | 1.5 | # Multiplies PRODUCTION_BUILDING_GOODS_PROFIT_FACTOR for autonomous investment pool constructions |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PROFIT_PRIVATIZE_FACTOR_MULT | 5.0 | # Multiplies PRODUCTION_BUILDING_GOODS_PROFIT_FACTOR for autonomous investment pool constructions, gives higher weight to buildings that have levels to privatize |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PRODUCED_VALUE_FACTOR_MULT | 1.25 | # Multiplies PRODUCTION_BUILDING_PRODUCED_VALUE_FACTOR for autonomous investment pool constructions |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PRODUCED_VALUE_PRIVATIZE_FACTOR_MULT | 0.5 | # Multiplies PRODUCTION_BUILDING_PRODUCED_VALUE_FACTOR for autonomous investment pool constructions, gives higher weight to buildings that have levels to privatize |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PRODUCED_TRADE_CAPACITY_FACTOR_MULT | 1.5 | # Multiplies value from produced trade capacity for autonomous investment pool constructions |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PRODUCED_MODIFIER_FACTOR_MULT | 0.75 | # Multiplies value from produced modifiers for autonomous investment pool constructions |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PRICE_COMPENSATION_FACTOR_MULT | 1.0 | # Multiplies high/low price compensation factors for autonomous investment pool constructions |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_BELOW_DESIRED_INFRASTRUCTURE_FACTOR_MULT | 0.25 | # Multiplies PRODUCTION_BUILDING_BELOW_DESIRED_INFRASTRUCTURE_FACTOR for autonomous investment pool constructions |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_LOW_INVESTMENT_RESET_TIME | 12 | # Every this number of months, reset the historical construction values for each pop type to ensure system can handle significant economic changes over time |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_MILITARY_GOODS_FACTOR_MULT | 1.5 | # Multiplies PRODUCTION_BUILDING_OUTPUT_NEEDED_MILITARY_GOODS_FACTOR & PRODUCTION_BUILDING_OUTPUT_WANTED_MILITARY_GOODS_FACTOR for autonomous investment pool constructions |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_INDUSTRIAL_GOODS_FACTOR_MULT | 4.0 | # Multiplies PRODUCTION_BUILDING_OUTPUT_NEEDED_INDUSTRIAL_GOODS_FACTOR & PRODUCTION_BUILDING_OUTPUT_WANTED_INDUSTRIAL_GOODS_FACTOR for autonomous investment pool constructions |
| # When the amount of saved value for foreign investment exceeds saved value for domestic investment, we start applying this bias to score for domestic autonomous constructions # This is calculated as 1 + ( ( foreign investment / domestic investment - 1 ) * AUTONOMOUS_INVESTMENT_DOMESTIC_INVESTMENT_BIAS ) # The resulting multiplier is capped at AUTONOMOUS_INVESTMENT_DOMESTIC_INVESTMENT_BIAS_MAX |  |  |
| AUTONOMOUS_INVESTMENT_DOMESTIC_INVESTMENT_BIAS | 2.0 |  |
| AUTONOMOUS_INVESTMENT_DOMESTIC_INVESTMENT_BIAS_MAX | 10.0 |  |
| # Every this number of months, the saved values for domestic/foreign investment are reset to 0 # This is to ensure that a prolonged period of domestic investment early game doesn't produce such high saved numbers that anything that comes after it doesn't matter |  |  |
| AUTONOMOUS_INVESTMENT_DOMESTIC_INVESTMENT_BIAS_RESET_TIME_IN_MONTHS | 60 |  |
| # For each this amount of money going into the investment pool, we execute one autonomous investment update per tick (minimum of 1) # This is to ensure that even very large investment pools can be properly utilized # Be careful with this value as setting it too low can badly impact performance |  |  |
| AUTONOMOUS_INVESTMENT_UPDATE_COUNT_DIVISOR | 500000 |  |
| PRODUCTION_BUILDING_AUTONOMOUS_INVESTMENT_PROFIT_PRIVATIZE_SELF_OWNED_BUILDING_MULT | 0.75 | # Multiply the total score for privatizing self-owned building levels by this |
| AUTONOMOUS_INVESTMENT_NUM_FAILED_INVESTMENTS_FOR_REFRESH_BASE | 150 | # If a country's investment pool fails to execute for this number of ticks, we force a refresh of all autonomous investment priorities to ensure investment pool isn't permanently stuck |
| AUTONOMOUS_INVESTMENT_NUM_FAILED_INVESTMENTS_FOR_REFRESH_DYNAMIC | 50 | # A random amount of this is added to the above to spread out refreshes |
| AUTONOMOUS_INVESTMENT_NUM_FAILED_INVESTMENTS_FOR_REFRESH_PLAYER | 20 | # Replaces above defines for player controlled countries |
| # The AI for autonomous investment weights alters the weights for buildings based on how much of the investment pool originates from a certain ownership type building # For example, if a high proportion of investment pool income is from Manor Houses, the building groups that manor houses have high investment weights for are weighted up # Here we clamp the bounds for this effect, ie how low/high is the weight allowed to get |  |  |
| AUTONOMOUS_INVESTMENT_MIN_PROPORTIONAL_INVESTMENT_WEIGHT | 0.25 |  |
| AUTONOMOUS_INVESTMENT_MAX_PROPORTIONAL_INVESTMENT_WEIGHT | 1.0 |  |
| # When scoring an ownership building for a new investment, always consider them to be contributing a minimum of this amount of the investment pool # This is to ensure that financial centers can appear in countries that lack them, etc |  |  |
| AUTONOMOUS_INVESTMENT_MIN_OWNERSHIP_BUILDING_INVESTMENT_SHARE | 0.25 |  |
| AUTONOMOUS_INVESTMENT_PREVIOUS_INVESTMENT_LOG_SIZE | 20 | # Maximum number of previous investments that a country will have in its investment log at the same time |
| AUTONOMOUS_INVESTMENT_PREVIOUS_INVESTMENT_DURATION_DAYS | 365 | # Number of days before a previous investment is removed from the log |
| BUILDING_PRIVATIZATION_CHANCE | 50.0 | # Chance for ai to do privatization instead of building a new building level when evaluating an existing building |
| # Investment AI owner building location selection weights and multipliers |  |  |
| OWNER_BUILDING_LOCATION_BASE_SCORE | 1 | # Base score for selecting state as owner building location |
| OWNER_BUILDING_LOCATION_POPULATION_SCORE | 1 | # For each 10000 population, increase score for selecting state as owner building location by this |
| OWNER_BUILDING_LOCATION_GDP_SCORE | 1 | # For each INVESTMENT_LOCATION_GDP_DIVISOR yearly state gdp, increase score for selecting state as owner building location by this |
| OWNER_BUILDING_LOCATION_GDP_DIVISOR | 100000 |  |
| OWNER_BUILDING_LOCATION_HAS_OWNER_BUILDING_MULT | 2.0 | # Multiply owner building location score by this for any state which already has the requisite owner building type |
| OWNER_BUILDING_LOCATION_CAPITAL_MULT | 2.0 | # Multiply owner building location score by this for our capital |
| OWNER_BUILDING_LOCATION_SAME_STATE_MULT | 4.0 | # Multiply owner building location score by this for the same state we're building/privatizing in |
| OWNER_BUILDING_LOCATION_NOT_HOMELANDS_MULT | 0.5 | # Multiply owner building location score by this if the state isn't a homeland of the country's primary cultures |
| OWNER_BUILDING_LOCATION_LOWER_GDP_MULT | 0.25 | # Multiply owner building location score by this for any state that has lower GDP than the state we're building/privatizing in |
| OWNER_BUILDING_LOCATION_NO_AVAILABLE_WORKFORCE_MULT | 0.1 | # Multiply owner building location score by this if the state lacks workers |
| OWNER_BUILDING_LOCATION_NO_AVAILABLE_INFRASTRUCTURE_MULT | 0.1 | # Multiply owner building location score by this if the state lacks infrastructure |
| OWNER_BUILDING_LOCATION_UNINCORPORATED_MULT | 0.01 | # Multiply owner building location score by this if the state is unincorporated |
| OWNER_COMPANY_EXPANSION_CHANCE_MULTIPLIER | 0.5 | # Base chance for a company to be selected as the owner of a new investment of one of their relevant building types, scales by fraction of investment pool coming from companies compared to historical amount of investment by companies |
| OWNER_COMPANY_PRIVATIZATION_CHANCE_MULTIPLIER | 0.75 | # Used instead of OWNER_COMPANY_EXPANSION_CHANCE for privatization, uses the same scaling |
| OWNER_COMPANY_OWN_STATE_MULT | 100.0 | # Multiply the chance for a company to be selected as the owner of a building (compared to other companies) if it's being built/invested in their HQ state |
| # Below data is used to calculate how much weight the AI places on enacting/revoking a law |  |  |
| CHANGE_LAW_RANDOM_FACTOR | 1.0 | # The higher this is, the more random AI law enactment will be |
| CHANGE_LAW_PRO_IG_IDEOLOGIES_FACTOR | 100 | # For enacting laws, per ideology match for IGs we approve of |
| CHANGE_LAW_ANTI_IG_IDEOLOGIES_FACTOR | -25 | # For enacting laws, per ideology match for IGs we disapprove of |
| CHANGE_LAW_POLITICAL_MOVEMENT_FACTOR | 1000 | # Scales against ( support * radicalism ) for each movement that would increase the law's chance to be enacted |
| CHANGE_LAW_POTENTIAL_CIVIL_WAR_THRESHOLD | 0.70 | # If a political movement to preserve would have at least this much radicalism, AI considers it a potential civil war cause |
| CHANGE_LAW_POTENTIAL_CIVIL_WAR_ENACT_CHANCE | 100 | # Base chance that the AI will proceed with a law change that could cause a civil war - revolution aversion is subtracted from this value for final chance (1 = 1%) |
| CHANGE_LAW_POTENTIAL_CIVIL_WAR_MEMORY_DURATION | 24 | # Number of months after deciding not to enact a law due to civil war risk that the AI should remember and stick to this decision |
| CHANGE_LAW_CIVIL_WAR_BOLDNESS_RANGE | 100 | # AI boldness (the score that revolution aversion must beat to cancel enactment) for a particular law is set on a random range of 0 - this |
| CHANGE_LAW_CIVIL_WAR_BOLDNESS_TIMED_WEIGHT_DURATION | 24 | # When the AI randomly sets its boldness for a particular law, how many months does that timed weight last |
| CHANGE_LAW_CIVIL_WAR_AVERSION_MOVEMENT_SUPPORT_FACTOR | 0.005 | # Chance that the AI will stop enacting a law to avoid a civil war is multiplied by ( 1 + highest revolutionary movement support * this ) |
| CHANGE_LAW_CIVIL_WAR_AVERSION_SUBJECT_MULTIPLIER | 5 | # Chance that AI stops enacting a law to avoid a civil war is multiplied by this for subjects |
| CHANGE_LAW_CIVIL_WAR_AVERSION_LAW_DIRECTION_FLEXIBILITY | 2 | # Revolution aversion is multiplied by this and added to the max progressiveness/regressiveness the AI is willing to stomach to avoid a revolution |
| DID_NOT_NEGOTIATE_WITH_IG_COOLDOWN_MONTHS | 24 | # If the AI decided not to negotiate with an IG for a law enactment, remember that decision for this many months |
| # Below data is used to calculate how much weight the AI places on a production method |  |  |
| PRODUCTION_METHOD_BASE_VALUE | 1000 |  |
| PRODUCTION_METHOD_PROFIT_FACTOR | 1 | # Per pound of profit the produced goods would generate |
| PRODUCTION_METHOD_DEFICIT_FACTOR | 1.5 | # Per pound of deficit the produced goods would generate (multiplies a negative value) |
| PRODUCTION_METHOD_PRODUCED_VALUE_FACTOR | 0.25 | # Per pound of produced goods in base value |
| PRODUCTION_METHOD_EMPLOYMENT_CHANGE_FACTOR | 2.0 | # The total score of a PM will be multiplied or divided by 1 + ( this * the proportion of labor that is added or saved by the change ) |
| PRODUCTION_METHOD_REDUCE_OUTPUT_PENALTY_FACTOR | 10 | # Multiply method score by this if we're reducing the building's output penalties |
| PRODUCTION_METHOD_INCREASE_OUTPUT_PENALTY_FACTOR | 0.01 | # Multiply method score by this if we're increasing the building's output penalties |
| PRODUCTION_METHOD_FAVORED_GOODS_FACTOR | 0.25 | # Per base cost * units of goods produced that the AI favors (for non military goods) |
| NATIONALIZATION_DESIRE_NATIONALIZE_THRESHOLD | 1.0 | # At this amount or above of Nationalization Desire (set in ai strategies & building type), the AI will want to nationalize production buildings |
| NATIONALIZATION_DESIRE_PRIVATIZE_THRESHOLD | 0.0 | # At this amount or below of Nationalization Desire (set in ai strategies & building type), the AI will want to privatize production buildings |
| # At this % of radicals in the country after a nationalization, AI will avoid further nationalization # Ignored when the state is recently liberated/conquered |  |  |
| NATIONALIZATION_RADICALS_THRESHOLD_TO_AVOID_NATIONALIZATION | 0.3 |  |
| NATIONALIZATION_RADICALS_THRESHOLD_TO_ALWAYS_COMPENSATE | 0.1 | # At this % of radicals in the country after a nationalization, AI always uses compensated nationalization |
| # Added to nationalization desire when a state has the recently_liberated_state/recently_conquered_state modifiers # Only applied to foreign-owned buildings and not considered for privatization |  |  |
| NATIONALIZATION_DESIRE_FROM_RECENTLY_LIBERATED | 2.0 |  |
| NATIONALIZATION_DESIRE_FROM_RECENTLY_CONQUERED | 1.0 |  |
| NATIONALIZATION_GOLD_RESERVES_THRESHOLD | 0.5 | # AI will want at least this much of its gold reserves remaining (as a percentage) after nationalizing if using compensation |
| NATIONALIZATION_MAX_LEVELS_PER_UPDATE | 5 | # The max number of building levels the AI will nationalize of each building in a single update |
| PRODUCTION_METHOD_FAVORED_MILITARY_GOODS_FACTOR | 0.5 | # Per base cost * units of goods produced that the AI favors (for military goods) |
| PRODUCTION_METHOD_DISFAVORED_GOODS_FACTOR | -0.25 | # Per base cost * units of goods produced that the AI disfavors |
| PRODUCTION_METHOD_UNDESIRABLE_GOODS_PRICE_THRESHOLD | 1.5 | # If a PM using the 'most productive' logic makes use of a good whose price is above ( base * this ), reduce the score |
| PRODUCTION_METHOD_UNDESIRABLE_GOODS_PRICE_FACTOR_TRADEABLE | -0.05 | # Per base cost * units of goods whose price is above undesirable price threshold (when the goods can be imported from the world market) |
| PRODUCTION_METHOD_UNDESIRABLE_GOODS_PRICE_FACTOR_UNTRADEABLE | -0.25 | # Per base cost * units of goods whose price is above undesirable price threshold (when the goods cannot be imported from the world market) |
| PRODUCTION_METHOD_STICKINESS_UPGRADE | 0.95 | # Score of non-current method is multiplied by this when it produces more goods base value in total |
| PRODUCTION_METHOD_STICKINESS_DOWNGRADE | 0.75 | # Score of non-current method is multiplied by this when it produces less (or equal) goods base value in total |
| PRODUCTION_METHOD_CHANCE_TO_CHANGE | 0.1 | # Chance that the AI will consider changing a production method when evaluating methods |
| PRODUCTION_METHOD_LOW_POP_THRESHOLD | 50000 | # If a state's population is less than this, use the scoring factor below for low-pop PMs |
| PRODUCTION_METHOD_LOW_POP_FACTOR | 100000 | # If a state's population is less than PRODUCTION_METHOD_LOW_POP_THRESHOLD, add this score for low-pop PMs |
| # Below data is used to calculate AI's desire for peace |  |  |
| AI_PEACE_AGREEMENT_BASE_VALUE | -10 |  |
| AI_PEACE_AGREEMENT_WHITE_PEACE_BASE | 10 | # If no wargoals are being enforced on either side |
| AI_PEACE_AGREEMENT_WHITE_PEACE_WAR_DURATION | 2 | # For each month the war goes on add this to the acceptance for a white peace |
| AI_PEACE_AGREEMENT_WAR_SUPPORT_FACTOR | -1 |  |
| AI_PEACE_AGREEMENT_UNACCEPTABLE_WARGOAL_VALUE | -1000 | # Fixed wargoal value that will be added to peace acceptance if an unacceptable wargoal (such as cut down to size) is being enforced on us |
| AI_PEACE_AGREEMENT_WARGOAL_VALUE_BASE | 10 | # How much does the AI value each wargoal (base) |
| AI_PEACE_AGREEMENT_WARGOAL_VALUE_MIN | -1000 | # Wargoal value cannot be lower than this |
| AI_PEACE_AGREEMENT_WARGOAL_VALUE_MAX | 1000 | # Wargoal value cannot be higher than this |
| AI_PEACE_AGREEMENT_WARGOAL_VALUE_SCALED | 0.5 | # How much does the AI value each wargoal (scaled with maneuver cost) |
| AI_PEACE_AGREEMENT_ALLY_WARGOAL_MULT | 1 | # For each wargoal that our allies are pressing, apply wargoal value * this |
| AI_PEACE_AGREEMENT_SELF_WARGOAL_MULT | 3 | # For each wargoal we have that's being pressed, apply wargoal value * this |
| AI_PEACE_AGREEMENT_ENEMY_WARGOAL_SELF_MULT | -8 | # For each wargoal that the enemy is pressing against us, apply wargoal value * this |
| AI_PEACE_AGREEMENT_ENEMY_WARGOAL_ALLY_MULT | -1 | # For each wargoal that's being pressed against our allies, apply wargoal value * this |
| AI_PEACE_AGREEMENT_NON_CONTESTED_ENEMY_WARGOAL_MULT | 5 | # Value of wargoals held by enemy that aren't being contested is multiplied by this |
| AI_PEACE_AGREEMENT_ACHIEVABLE_ALLY_WARGOAL | -1.5 | # For each wargoal our side holds that isn't being pressed where the target will run out of war support before the holder does (multiplies self/ally wargoal value) |
| AI_PEACE_AGREEMENT_ACHIEVABLE_ENEMY_WARGOAL | -0.9 | # For each wargoal the enemy side holds (pressed or not) where the target will run out of war support before the holder does (multiplies self/ally enemy wargoal value) |
| AI_PEACE_AGREEMENT_WAR_SUPPORT_TO_HOLD_ON_TO_ACHIEVABLE_WARGOALS | 0 | # Below this war support an AI will be much more open to ceding achievable wargoals to the enemy in a peace deal |
| AI_PEACE_AGREEMENT_PEACE_DESIRE_FACTOR | 1.0 | # Peace desire is multiplied by this when added to peace agreement acceptance score |
| AI_CAPITULATE_COMPLETELY_DEFEATED | 1000 | # If entire allied side is 100% occupied |
| AI_CAPITULATE_BASE_VALUE | -25 |  |
| AI_CAPITULATE_WAR_LEADER_FACTOR | -25 | # If warleader |
| AI_CAPITULATE_WAR_SUPPORT_FACTOR | -1 |  |
| AI_CAPITULATE_SELF_WARGOAL_FACTOR | -5 | # For each wargoal we hold in the war |
| AI_CAPITULATE_ENEMY_WARGOAL_FACTOR | -20 | # For each wargoal targeting us in the war |
| AI_CAPITULATE_PEACE_DESIRE_FACTOR | 0.5 | # Peace desire is multiplied by this when added to capitulation score |
| AI_MONTHS_OF_REDUCED_PEACE_DESIRE | 10 | # Before this amount of months, reduce AI peace desire |
| AI_PEACE_DESIRE_FROM_SHORT_WAR | -10 | # Subtract this amount of peace desire for the above number of months (multiplied by AI_MONTHS_OF_REDUCED_PEACE_DESIRE - months of war duration) |
| AI_PEACE_DESIRE_FROM_TURMOIL | 25 | # Add this amount of peace desire at 100% radicals |
| AI_PEACE_DESIRE_FROM_DEVASTATION | 50 | # Add this amount of peace desire at 100% devastation |
| AI_PEACE_DESIRE_FROM_LOYALISTS | -25 | # Subtract this amount of peace desire at 100% loyalists |
| AI_PEACE_DESIRE_FROM_DEBT_LEVEL | 200 | # Add this amount of peace desire at 100% debt level |
| AI_PEACE_DESIRE_FROM_BANKRUPTCY | 200 | # Add this amount of peace desire when bankrupt |
| AI_PEACE_DESIRE_FROM_GOLD_RESERVES | -25 | # Subtract this amount of peace desire at 100% gold reserves |
| AI_PEACE_DESIRE_FROM_FORCE_BALANCE | 50 | # Up to this amount is added or subtracted from war support based on DIPLO_PLAY_FORCE_BALANCE_SCALE of the two sides |
| AI_PEACE_DESIRE_FACTOR_FROM_ANNEXATION | 0.5 | # If peace will cause the country to be annexed then all positive peace desire factors will be multiplied by this value |
| # AI country-specific goal data |  |  |
| SECRET_GOAL_STICKINESS | 2.0 | # The higher this is, the less likely the AI is to change an established secret goal during recalculation |
| ATTITUDE_STRONG_GOAL_SCORE_THRESHOLD | 100 |  |
| ATTITUDE_WEAK_GOAL_SCORE_THRESHOLD | 50 |  |
| GOAL_THREAT_INFAMOUS_FACTOR | 25 |  |
| GOAL_THREAT_NOTORIOUS_FACTOR | 50 |  |
| GOAL_THREAT_PARIAH_FACTOR | 1000 |  |
| GOAL_THREAT_NEIGHBOR_FACTOR | 25 |  |
| GOAL_THREAT_SP_MAX_MULT | 2 |  |
| GOAL_THREAT_CUSTOMS_UNION_MULT | 0.5 | # Reduce neighbor threat score by this if in a customs union |
| GOAL_ANTAGONIZE_POOR_RELATIONS_FACTOR | 25 |  |
| GOAL_ANTAGONIZE_COLD_RELATIONS_FACTOR | 50 |  |
| GOAL_ANTAGONIZE_HOSTILE_RELATIONS_FACTOR | 100 |  |
| GOAL_ANTAGONIZE_LIBERTY_DESIRE_FACTOR | 1 | # Multiplied by liberty desire for subjects against their overlords |
| GOAL_ANTAGONIZE_CONQUER_SCORE_MULT | 1.0 | # Multiplied by the total score of the states we want to take from them |
| GOAL_ANTAGONIZE_CONQUER_SCORE_MAX | 200 | # Total score of territory we want to take cannot exceed this |
| GOAL_ANTAGONIZE_TREATY_PORT_SCORE_MULT | 0.5 | # Multiplied by the total score of the treaty ports we want to take from them |
| GOAL_ANTAGONIZE_TREATY_PORT_SCORE_MAX | 100 | # Total score of treaty ports we want to take cannot exceed this |
| GOAL_ANTAGONIZE_DOMINATE_SCORE_MULT | 1.0 | # Multiplied by the total score of make-subject wargoals we want to enforce on them |
| GOAL_ANTAGONIZE_DOMINATE_SCORE_MAX | 200 |  |
| GOAL_ANTAGONIZE_RIVAL_FACTOR | 100 |  |
| GOAL_ANTAGONIZE_WAR_FACTOR | 1000 |  |
| GOAL_ANTAGONIZE_NATURAL_ENEMY_FACTOR | 75 |  |
| GOAL_BEFRIEND_CORDIAL_RELATIONS_FACTOR | 25 |  |
| GOAL_BEFRIEND_AMICABLE_RELATIONS_FACTOR | 50 |  |
| GOAL_BEFRIEND_FRIENDLY_RELATIONS_FACTOR | 100 |  |
| GOAL_BEFRIEND_PROTECTOR_THRESHOLD | 15 |  |
| GOAL_BEFRIEND_PROTECTOR_FACTOR | 1.0 |  |
| GOAL_BEFRIEND_PROTECTOR_RIVAL_MULT | 2.0 | # Score multiplied by this if they can protect against our rival |
| GOAL_BEFRIEND_PROTECTOR_MAX_FACTOR | 100 |  |
| GOAL_BEFRIEND_PROTECTOR_SP_MAX_MULT | 2 |  |
| GOAL_BEFRIEND_SUBJECT_FACTOR | 25 |  |
| GOAL_BEFRIEND_ALLIANCE_FACTOR | 50 |  |
| GOAL_BEFRIEND_NATURAL_ALLY_FACTOR | 75 |  |
| GOAL_BEFRIEND_RECONCILE_FACTOR | 500 |  |
| GOAL_BEFRIEND_WAR_ALLY_FACTOR | 1000 |  |
| GOAL_BEFRIEND_WANTS_TO_PROTECT_FACTOR | 100 |  |
| FRIENDLY_AI_JOIN_DIPLO_PLAY_FACTOR | 100 |  |
| VIOLATE_SOVEREIGNTY_ACTION_NAME | "violate_sovereignty" |  |
| VIOLATE_SOVEREIGNTY_MIN_RELATIVE_STRENGTH | 2.0 | # We must have their army x this in SP to want to violate their sovereignty |
| VIOLATE_SOVEREIGNTY_RANDOM_FACTOR | 2.0 | # The higher this is, the more random the AI will be about who it violates the sovereignty of |
| VIOLATE_SOVEREIGNTY_MIN_THEATER_IMPORTANCE | 150 | # A theater must have at least this much war value for AI to consider violating sovereignty to get access to it |
| VIOLATE_SOVEREIGNTY_COOLDOWN_DAYS | 100 |  |
| EXPEL_DIPLOMATS_ACTION_NAME | "expel_diplomats" |  |
| AUTONOMOUS_TRADE_RANDOM_FACTOR | 0.5 | # The higher this is, the more random autonomous trade will be in goods selection |
| AUTONOMOUS_TRADE_STICKYNESS | 2.0 | # A new trade has to generate at least this many times more revenue to replace an older trade when trade capacity is fully used up |
| AUTONOMOUS_TRADE_WEEKS_BEFORE_TRADE_REDUCTION | 8 | # For this many weeks after increasing trade in a good, a state won't reduce the trade volume for that same good, so that effects such as goods substitution have time to kick in |
| AUTONOMOUS_TRADE_MIN_DESIRABILITY_PER_QUANTITY_TO_MAINTAIN_TRADE | 25 | # If a current trade has lower desirability than this per base traded quantity, decrease trade volume |
| AUTONOMOUS_TRADE_MIN_DESIRABILITY_PER_QUANTITY_TO_INCREASE_TRADE | 50 | # If a new trade has lower desirability than this per base traded quantity, don't increase trade volume |
| AUTONOMOUS_TRADE_MIN_DESIRABILITY_INITIALIZATION_MULTIPLIER | 0.75 | # During bookmark initialization, desirability requirements for trade are multiplied by this |
| AUTONOMOUS_TRADE_POTENTIAL_REVENUE_BASE_COST_FACTOR | 0.25 | # When determining trade potential for a good in a state, the revenue per unit is normalized against the good base cost * this, to account for the fact that revenue will drop as trades increase |
| # Factors that impact desirability for trades # The base desirability of a trade is equal to revenue per traded quantity after tariffs and subventions |  |  |
| AUTONOMOUS_TRADE_DESIRE_SUBVENTIONS_FACTOR | 100 | # Desire for a trade is increased by ( subventions as percentage * this ), this is an additional factor on top of the impact on revenue. This is also applied in reverse for subventions in the opposite direction (ie, export subventions reduce desire for imports) |
| AUTONOMOUS_TRADE_DESIRE_SUBVENTIONS_FACTOR_NEW_GOODS_MULT | 20.0 | # The subventions impact on desire for a trade is multiplied by this for importing goods that don't exist in the market |
| AUTONOMOUS_TRADE_DESIRE_TARIFFS_FACTOR | 25 | # Desire for a trade is decreased by ( tariffs as percentage * this ), this is an additional factor on top of the impact on revenue |
| AUTONOMOUS_TRADE_DESIRE_OPPOSITE_MARKET_SHARE_FACTOR | -1000 | # Desire for a trade is changed by this * the share of opposite-direction trade in the world market coming from the country |
| AUTONOMOUS_TRADE_DESIRE_SHORTAGE_FACTOR | 300 | # Desire to import goods in shortage is increased by this, scaled by the severity of the shortage penalty |
| # Whenever a Trade Center successfully excecutes a trade, it uses up one of its weekly trades # Whenever it *fails* to execute a trade, it uses up this fraction of its total amount of weekly trades # This is so that Trade Centers with hundreds of weekly trades do not try and trade over and over again, using up tons of performance for no gain |  |  |
| AUTONOMOUS_TRADE_WEEKLY_TRADES_FRACTION_USED_FOR_FAILED_TRADE = 0.2 |  |  |
| TRADE_VALUE_DELTA_FACTOR | 3.0 | # When calculating treaty trade value, the delta between production/consumption counts for this much more than base production/consumption values |
| TRADE_VALUE_BASE_MULTIPLIER | 0.001 | # Base multiplier applied to the value for treaty trade based purely on production & consumption |
| TRADE_VALUE_RELATIVE_MULTIPLIER | 100 | # Relative multiplier applied to the value for treaty trade and divided by the total value in the market |
| TRADE_VALUE_FAVORED_GOODS_DIRECTION_MULT | 1.25 | # Potential for trading a good is multiplied by this when determining AI trade value, if the trade direction matches the AI's goods stance |
| TRADE_VALUE_DISFAVORED_GOODS_DIRECTION_MULT | 0.25 | # Potential for trading a good is multiplied by this when determining AI trade value, if the trade direction is opposite of the AI's goods stance |
| UNUSED_CAPPED_RESOURCE_RATIO_TO_START_DISCOURAGING_EXPORT | 0.5 | # If the untapped potential production of a resource-capped good in the country is not at least market buy orders * this, switch to punitive export tariffs |
| UNUSED_CAPPED_RESOURCE_RATIO_TO_STOP_DISCOURAGING_EXPORT | 1.0 | # If the untapped potential production of a resource-capped good in the country is at least market buy orders * this, stop applying punitive export tariffs |
| COMPANY_TYPE_DEFAULT_BASE_WEIGHT | 1 | # Base weight for companies, can be overriden by ai_weight in database |
| COMPANY_TYPE_RANDOM_FACTOR | 1 | # The higher this is, the more random AI selection of companies will be |
| COMPANY_TYPE_STICKYNESS | 3 | # The weight for the company the AI is already planning to create is multiplied by this |
| COMPANY_TYPE_STICKYNESS_DURATION_MONTHS | 60 | # After this many months, the stickyness for the company the AI is planning to form is removed |
| COMPANY_TYPE_FORMABLE_FACTOR | 1.25 | # Increase weight for a company by this if it's instantly formable |
| COMPANY_TYPE_FORMABLE_MULTIPLE_FREE_SLOTS_FACTOR | 5.0 | # Replaces COMPANY_TYPE_FORMABLE_FACTOR if the country has more than one free company slot |
| COMPANY_TYPE_PRODUCTIVITY_FACTOR | 0.25 | # Multiplier for AI weight of companies is increased by ( this * predicted building productivity ) |
| COMPANY_TYPE_PRODUCTIVITY_MAX | 4.0 | # Effects of COMPANY_TYPE_PRODUCTIVITY_FACTOR cannot be higher than this |
| COMPANY_TYPE_BUILDING_LEVELS_FACTOR | 0.1 | # Multiplier for AI weight of companies is increased by ( this * num building levels ) |
| COMPANY_TYPE_BUILDING_LEVELS_MAX | 2.0 | # Effects of COMPANY_TYPE_NUM_BUILDING_LEVELS_FACTOR cannot be higher than this |
| COMPANY_TYPE_COMPETITION_FACTOR | 2 | # Divisor for AI weight of companies is increased by 1 + ( number of building types on existing companies that compete * this ) |
| COMPANY_TYPE_BUILDING_GROUP_WEIGHT_IMPACT | 1.5 | # The AI's average strategy weight mult for the building groups associated with this company is modulated towards 1 by this value and applied to AI preference for the company (ie; if this is 0.5, then the difference between the average AI preference and 1 is halved - 1.5 becomes 1.25, 0.5 becomes 0.75 etc) |
| MILITARY_UNITS_PER_FORMATION_ARMY | 50 | # The AI aims to have armies of roughly this size, and will create new formations in land HQs accordingly |
| MILITARY_UNITS_PER_FORMATION_FLEET | 100 | # The AI aims to have fleets of roughly this size, and will create new formations in naval HQs accordingly |
| MILITARY_UNITS_MIN_FOR_GARRISON_FORMATION | 15 | # If a land HQ has at least this number of units we set the minimum number of formations to 2, so that there will be a garrison formation present |
| MILITARY_UNITS_MIN_FOR_GARRISON_FORMATION_IN_CAPITAL_HQ | 5 | # Overrides MILITARY_UNITS_MIN_FOR_GARRISON_FORMATION for the capital land HQ, since not leaving the capital undefended is extremely critical |
| MILITARY_UNITS_GARRISON_BATTALION_MULT | 0.33 | # The garrison formation in each HQ should receive this portion of its total number of battalions |
| MILITARY_UNITS_MIN_DELTA_TO_TRANSFER_UNITS | 0.05 | # There must be at least this delta between the fraction of a HQ's units that a formation wants and the fraction that it has to bother with transfering units to/from it |
| MIN_RANK_TO_FORM_POWER_BLOC | 6 | # AIs with a lower rank value than this will never try to form power blocs |
| POWER_BLOC_IDENTITY_RANDOM_FACTOR | 1 | # The higher this is, the more random AI selection of power bloc identities will be |
| POWER_BLOC_PRINCIPLE_RANDOM_FACTOR | 1 | # The higher this is, the more random AI selection of power bloc principles will be |
| POWER_BLOC_STATUE_RANDOM_FACTOR | 1 | # The higher this is, the more random AI selection of power bloc statues will be |
| LEAVE_POWER_BLOC_SCORE_THRESHOLD | -100 | # Leave the power bloc if score is less than this. Score is the acceptance value for 'invite_to_power_bloc' diplomatic action |
| POWER_BLOC_KICK_MEMBER_LOW_COHESION_THRESHOLD | 40 | # If current cohesion is less than this consider it low and add the corresponding score |
| POWER_BLOC_KICK_MEMBER_LOW_COHESION_SCORE | 5 | # Score to kick a member (which is anyone) if current cohesion is low (multiplied by delta between cohesion and threshold) |
| POWER_BLOC_KICK_MEMBER_COHESION_CHANGE_SCORE | 2 | # Score to kick the member if cohesion change is high enough (multiplied by cohesion chance) |
| POWER_BLOC_KICK_MEMBER_LEVERAGE_ADVANTAGE_SCORE | -0.1 | # Score to kick the member if active leverage on them is high enough (multiplied by active leverage) |
| POWER_BLOC_KICK_MEMBER_POOR_RELATIONS_SCORE | 25 | # Score to kick the member if relations with the member are Poor, x2 if Cold, x3 if Hostile |
| POWER_BLOC_KICK_MEMBER_HOSTILE_ATTITUDE_SCORE | 25 | # Score to kick the member if attitude towards them is Hostile, x2 if Very Hostile |
| POWER_BLOC_KICK_MEMBER_MARKET_SHARE_SCORE | -50 | # Score to kick the member based on their market share in the bloc (if PB has a unified market) |
| POWER_BLOC_KICK_MEMBER_HIGH_ARMY_MILITARY_STRENGTH_SCORE | -25 | # Score to kick the member if their army strength is above average (if PB is a military alliance) |
| POWER_BLOC_KICK_MEMBER_HIGH_NAVY_MILITARY_STRENGTH_SCORE | -15 | # Score to kick the member if their navy strength is above average (if PB is a military alliance) |
| POWER_BLOC_KICK_MEMBER_SCORE_THRESHOLD | 100 | # Kick the member if the total score is less than this |
| POWER_BLOC_KICK_MEMBER_RANDOM_FACTOR | 0.5 | # The higher this is, the more random AI will be about which member to kick from the power bloc |
| IMPOSE_LAW_NO_POTENTIAL_LAW_COOLDOWN_MONTHS | 24 | # If the AI doesn't find any law with at least a chance to be imposed on a target, don't check them again for this number of months |
| IMPOSE_LAW_RANDOM_FACTOR | 1 | # The higher this is, the more random the AI is about which country to try and impose a law on |
| IMPOSE_LAW_MAX_IDEOLOGICAL_OPINION | 25 | # The AI's ideological opinion of a country must be this or below to consider imposing a law on them |
| IMPOSE_LAW_MAX_LIBERTY_DESIRE | 50 | # The AI will not impose laws on subjects with LD higher than this |
| IMPOSE_LAW_MIN_ENACTMENT_CHANCE | 0.2 | # The AI will not impose laws on subjects if the enactment chance is less than this |
| EXILE_INTERACTION_FAILED_COOLDOWN_MONTHS | 24 | # If a character interaction was invalid against an exiled character, don't check them again for this amount of months |
| AI_INTERACTION_PROMINENCE_CHANCE_FACTOR | 1.0 | # Each point of prominence gives this % chance of being considered for character interactions |
| AI_INTERACTION_MIN_PROMINENCE_CHANCE | 10 | # Minimum % chance of being considered regardless of prominence |
| TREATY_FAIRNESS_BASE_SCORE | 10 | # The base score for treaty fairness before country acceptances are considered, treaties with an acceptance delta smaller than this will be considered fair to both parts |
| REJECTED_TREATY_MEMORY_DURATION_DAYS | 365 | # For how many days does the AI remember a rejected treaty and refuse any treaties that aren't a significant enough improvement on it |
| REJECTED_TREATY_MIN_ACCEPTANCE_IMPROVEMENT_FOR_NEW_PROPOSAL | 10 | # For the AI to have a chance to accept a treaty proposal after recently having rejected a treaty, the new proposal must be this much better than the old one |
| REJECTED_TREATY_UNDER_MIN_ACCEPTANCE_IMPROVEMENT_PENALTY | -1000 | # Added to accepance when a treaty proposal isn't sufficiently improved upon within the rejected treaty memory duration |
| # Treaties |  |  |
| TREATIES_RANDOM_FACTOR | 1.0 | # How random should the AI be regarding article selection when composing treaties? |
| TREATIES_CHECK_CATEGORIES_WHEN_COMPOSING_TREATY | no | # Does the AI care about categories when composing a treaty after gathering the initial article? |
| TREATIES_NUMBER_CHECKED_CATEGORIES_TREATY_COMPOSER | 3 | # How many categories does the AI try to gather to check against when composing a treaty |
| TREATIES_MINIMUM_ACCEPTANCE_TO_PROPOSE | 15 | # How much acceptance does the AI require the other side to have for it to try sending a proposal? 0 = never accept, 30 = always accept, in between = random chance |
| TREATIES_MINIMUM_OWN_ACCEPTANCE_TO_PROPOSE | 10 | # How much own acceptance does the AI require to have itself for it to send a proposal? |
| TREATIES_MAX_NUMBER_ARTICLES | 6 | # How many articles in a treaty the AI will consider at most |
| TREATIES_ACCEPTANCE_BASE | 0 | # Base Acceptance for Treaties |
| TREATIES_ACCEPTANCE_WITHDRAW_THRESHOLD | -50 | # Threshold at or under which AI will withdraw from treaties outside of their binding period |
| TREATIES_ACCEPTANCE_WITHDRAW_BINDING_PERIOD_THRESHOLD | -10000 | # Threshold at or under which AI will withdraw from treaties while they are still binding |
| TREATIES_DEFAULT_LENGTH_YEARS | 5 | # How long treaties the AI will propose |
| COLONIZATION_VALUE_BASE | 25 | # Base AI value for a region they are able to colonize |
| COLONIZATION_VALUE_HAS_COLONY_MULTIPLIER | 2.0 | # Colonization value is multiplied by this if the AI has a growing colony in the region |
| COLONIZATION_VALUE_NO_PRESENCE_MULTIPLIER | 0.2 | # Colonization value is multiplied by this if the AI has no presence in the region or adjacent regions |
| TRANSIT_RIGHTS_BASE_DESIRE | 100 | # Base desire for Transit Rights, only applied if they would actually help connect a market area for the receiving country |
| TREATY_OBLIGATION_WE_OWE_THEM_ACCEPTANCE | -40 | # How country A's acceptance of a treaty changes if A would owe B an obligation as part of the treaty. Note: "WE" is the country doing the evaluation, not the player |
| TREATY_OBLIGATION_THEY_OWE_US_ACCEPTANCE | 30 | # How country A's acceptance of a treaty changes if A would be owed an obligation by B as part of the treaty. Note: "US" is the country doing the evaluation, not the player |
| TREATY_OBLIGATION_THEY_OWE_US_RECENTLY_REPUDIATED_ACCEPTANCE | 15 | # Same as above, but use this if B has recently repudiated an obligation (A values it less because B's word is not worth as much) |
| TREATY_OBLIGATION_THEY_CALL_US_IN_ACCEPTANCE | 30 | # How country A's acceptance of a treaty changes if B is calling in an obligation that A owes B. Note: "US" is the country doing the evaluation, not the player |
| TREATY_OBLIGATION_THEY_CALL_US_IN_RECENTLY_REPUDIATED_ACCEPTANCE | 15 | # Same as above, but use this if B has recently repudiated an obligation (A values it less because they're less inclined to follow honor agreements that B is willing to ignore) |
| PIRACY_HEAT_GAIN_PER_GOODS | 0.01 | # Multiplied with the trade quantity of pirated goods to determine how "hot" a shipping lane is |
| PIRACY_HEAT_DECAY | 0.01 | # How many percent the piracy heat decays with each ai update |
| RAID_HEAT_GAIN_PER_LOST_SUPPLY_SHIP | 0.01 | # Multiplied with the amount of supply ships lost in a supply path |
| RAID_HEAT_DECAY | 0.01 | # How many percent the piracy heat decays with each ai update |
| PROTECT_SUPPLY_OWN_PATH_SCORE_MULT | 2.0 | # 1 + [Mult] is multiplied with the supply path score if it belongs to you |
| RAID_SUPPLY_SCORING_FLEET_AVG_SPEED_MULT | 0.05 | # Is multiplied with the average speed of the fleet when |
| RAID_SUPPLY_SCORING_FLEET_DETECTION_VISIBILITY_RATIO_MULT | 1.5 # Is multiplied with the ratio between detection and visibility for the fleet |  |
| RAID_SUPPLY_SCORING_FLEET_SIZE_MULT | 2.0 | # Will calculate this value / num ships and add to the scoring mult, so more ships means less scoring |
| RAID_SUPPLY_SCORING_FLEET_STRENGTH_RATIO_MULT | 3.0 | # How much we multiply the ratio of strength between hostile/friendly presence |
| PROTECT_SUPPLY_SCORING_FLEET_SCREENING_RATIO_MULT | 2.0 # We want to primarily use fleets with high screening |  |
| PROTECT_SUPPLY_SCORING_FLEET_SIZE_MULT | 0.005 | # How much we multiply the size of the fleet with for scoring |
| PROTECT_SUPPLY_SCORING_FLEET_RAID_HEAT_MULT | 0.01 | # How much we multiply the accumulated raid heat in the sea province for scoring |
| PROTECT_SUPPLY_SCORING_FLEET_STRENGTH_RATIO_MULT | 3.0 | # How much we multiply the ratio of strength between hostile/friendly presence |
| HUNT_PIRATES_SCORING_FLEET_PIRACY_HEAT_MULT | 0.01 | # How much accumulated piracy heat in the sea province boosts hunt pirates scoring |
| HUNT_PIRATES_SCORING_FLEET_DETECTION_RATIO_MULT | 2.0 | # Favor fleets with high detection for hunting pirates |
| HUNT_PIRATES_SCORING_FLEET_SCREENING_RATIO_MULT | 1.0 | # Favor fleets with high screening ratio for pirate hunting patrols |
| HUNT_PIRATES_MIN_HOSTILITY_MULT | 0.25 | # Minimum multiplier for hunt pirates scoring during hostilities. Prevents AI from completely abandoning pirate hunting during war. |
| HUNT_PIRATES_AT_WAR_MULT | 0.25 | # Additional multiplier applied to hunt pirates scoring when at war |
| PIRACY_SCORING_FLEET_SPEED_VISIBILITY_RATIO_ADJUSTER | 1.0 | # If the score seems to end up being too high for piracy, lower this oen |
| PIRACY_SCORING_FLEET_SPEED_VISIBILITY_RATIO_MULT | 2.0 | # Favor fleets with as much goods per visibility for pirates |
| PIRACY_NO_HOSTILITIES_MULT | 1.0 | # Multiplied with shipping lane score when we have no hostilities currently |
| PIRACY_HOSTILITIES_MULT | 0.5 | # Multiplied with shipping lane score when we have hostilities currently |
| PRIVATEER_SCORING_FLEET_SPEED_VISIBILITY_RATIO_ADJUSTER | 1.0 | # If the score seems to end up being too high for privateer, lower this oen |
| PRIVATEER_SCORING_FLEET_SPEED_VISIBILITY_RATIO_MULT | 2.0 | # Favor fleets with as much goods per visibility for privateers |
| PORT_BOMBARDMENT_NAVAL_HOSTILITIES_MULT | 2.0 | # Multiplied with coast score when we are in naval hostilities with coast owner |
| PORT_BOMBARDMENT_FULL_HOSTILITIES_MULT | 0.5 | # Multiplied with coast score when we are in full hostilities with coast owner |
| BLOCKADE_WORLD_MARKET_HUB_MULT | 2.0 | # Multiplied with coast score for world market hub |
| BLOCKADE_NOT_WORLD_MARKET_HUB_MULT | 0.25 | # Multiplied with coast score for non-world market hub |
| # The AI calculates an "Outclassed ratio" to determien how screwed it is on the naval engagement. # The outclassed ratio will be multiplied with this and added to the mult when scoring what naval mission to pick # So if this below is negative it means it will avoid doing those missions, positive it will prioritize those. |  |  |
| INTERCEPT_OUTCLASSED_MULT | -4.0 |  |
| POWER_PROJECTION_OUTCLASSED_MULT | -1.0 |  |
| POWER_PROJECTION_HOSTILE_NAVAL_RATIO_MAX | 0.25 | # Hostile-to-friendly naval strength ratio at which power projection score is fully suppressed. At 0 ratio there is no penalty, linearly scales to 0x score at this ratio. |
| INTERCEPT_HOSTILE_NAVAL_RATIO_FOR_FULL_SCORE | 0.25 | # Hostile-to-friendly naval strength ratio at which intercept and defend coast reach full score. Below this ratio the scores are scaled down linearly. |
| INTERCEPT_ACCEPTABLE_DISTANCE | 1000 | # Effective supply distance below which there is no distance penalty. Above this, score is divided by (distance / acceptable_distance). |
| POWER_PROJECTION_ACCEPTABLE_DISTANCE | 2500 |  |
| BLOCKADE_ACCEPTABLE_DISTANCE | 1000 |  |
| RAID_SUPPLY_ACCEPTABLE_DISTANCE | 1000 |  |
| PROTECT_SUPPLY_ACCEPTABLE_DISTANCE | 1000 |  |
| PORT_BOMBARDMENT_ACCEPTABLE_DISTANCE | 1000 |  |
| HUNT_PIRATES_ACCEPTABLE_DISTANCE | 1000 |  |
| DEFEND_COAST_ACCEPTABLE_DISTANCE | 1000 |  |
| RAID_SUPPLY_OUTCLASSED_MULT | 2.0 |  |
| PROTECT_SUPPLY_OUTCLASSED_MULT | -1.0 |  |
| DEFEND_COAST_OUTCLASSED_MULT | -4.0 |  |
| BLOCKADE_OUTCLASSED_MULT | -4.0 |  |
| PORT_BOMBARDMENT_OUTCLASSED_MULT | -4.0 |  |
| PROTECT_SUPPLY_DOMINANCE_PENALTY | 0.75 | # How much to reduce protect supply scoring when dominating the enemy navy. At full dominance, score is reduced by this amount (e.g. 0.9 means score goes to 10% at full dominance). |
| PROTECT_SUPPLY_MIN_DOMINANCE_MULT | 0.1 | # Minimum multiplier for protect supply during naval dominance. Prevents AI from completely ignoring supply protection. |
| BLOCKADE_DOMINANCE_BOOST | 3.0 | # How much to boost blockade scoring when dominating the enemy navy. Added as a multiplier (e.g. 3.0 means score can reach 4.0x at full dominance). |
| PORT_BOMBARDMENT_DOMINANCE_BOOST | 3.0 | # How much to boost port bombardment scoring when dominating the enemy navy. |
| COMFORTABLE_HQ_NAVY_SIZE | 10 | # What the AI will want to at least station in an HQ to consider the HQ vital |
| NAVAL_HQ_IMPORTANCE_MIN_SCORE | 2 | # Any naval HQ with score less than this gets ignored |

## 00_audio

### Audio

| Define | Default Value | Dev Comment |
|---|---|---|
| DEFAULT_SELECT | "event:/SFX/UI/Global/select" |  |
| MAXIMAP_ACTIVATION | "event:/SFX/UI/MaxiMap/activate" |  |
| MAXIMAP_DEACTIVATION | "event:/SFX/UI/MaxiMap/deactivate" |  |
| MAP_LENS_political_lens | "event:/SFX/UI/MapLenses/political" |  |
| MAP_LENS_production_lens | "event:/SFX/UI/MapLenses/production" |  |
| MAP_LENS_diplomatic_lens | "event:/SFX/UI/MapLenses/diplomatic" |  |
| MAP_LENS_military_lens | "event:/SFX/UI/MapLenses/military" |  |
| MAP_CLICKSOUND | "event:/SFX/UI/Global/map_click" |  |
| MAP_HOVERSOUND | "event:/SFX/UI/Global/map_hover" |  |
| MAP_INTERACTION_INVALID_CLICKSOUND | "" |  |
| MAP_INTERACTION_HOVERSOUND | "event:/SFX/UI/Global/map_hover_interact" |  |
| DIPLOMATIC_ACTION_CONFIRMATION | "event:/SFX/UI/Global/confirm" |  |
| DIPLOMATIC_ACTION_REQUEST | "event:/SFX/UI/MapInteraction/diplomatic_action_request" |  |
| DIPLOMATIC_ACTION_HOSTILE | "event:/SFX/UI/MapInteraction/diplomatic_action_hostile" |  |
| DIPLOMATIC_ACTION_BENIGN | "event:/SFX/UI/MapInteraction/diplomatic_action_benign" |  |
| DIPLOMATIC_PLAY | "event:/SFX/UI/MapInteraction/diplomatic_play" |  |
| DIPLOMATIC_PLAY_EPIC | "event:/SFX/UI/MapInteraction/diplomatic_play_epic" |  |
| INFORMATION_PANEL_HIDE | "event:/SFX/UI/Global/panel_hide" |  |
| MILITARY_FORMATION_DRAG_SELECTION_ADDED | "event:/SFX/UI/Global/increment" |  |
| MILITARY_FORMATION_DRAG_SELECTION_REMOVED | "event:/SFX/UI/Global/decrement" |  |
| DEFAULT_NOTIFICATION_SOUND | "event:/SFX/UI/Alerts/Toasts/_transient" |  |
| POSITIVE_GAMEOVER_SOUND | "event:/MUSIC/Stingers/game_over/positive" |  |
| NEGATIVE_GAMEOVER_SOUND | "event:/MUSIC/Stingers/game_over/negative" |  |

## 00_graphics

### MapMode

| Define | Default Value | Dev Comment |
|---|---|---|
| # Use opacity 1 as the default for colors and control the final opacity directly in the # Map Modes (or make a very specific call to step away from this for a very specific reasons) @opacity = 1 ### INTERACTIVE MAP MODE ### |  |  |
| MAP_PAINTING_TEXTURE_TILING | 50 | # Tiling of mapmodes textures |
| MAP_PAINTING_FLATMAP_TEXTURE_TILING | 30 | # Tiling of mapmodes textures in flatmap |
| # Construction scales its opacity based on predicted earnings # This is the lowest scalar value (lowest predicted earnigns) to avoid full transparency |  |  |
| MAP_PAINTING_CONSTRUCTION_LOW_OPACITY | 0.4 |  |
| ### HEAT MAP MAP MODE ### |  |  |
| HEAT_MAP_COLOR_FROM | { 0.9 0.9 0.1 0.3 } |  |
| HEAT_MAP_COLOR_TO | { 0.1 0.4 0.2 1.5 } |  |
| HEAT_MAP_MIN_ALPHA | 0.4 | # Used in the Interest Group and Market Map Mode |
| ### HIGHLIGHT ### |  |  |
| HIGHLIGHT_COLOR | { 1 1 1 0.5 } | # White |
| HIGHLIGHT_INTERACTION_COLOR | { 1 0.57 0.15 0.5 } | # Golden |
| CAMERA_HEIGHT_START_FADING_HIGHLIGHT | 800 | # At what camera height should we start fading out the highlight? |
| CAMERA_HEIGHT_FULLY_FADED_HIGHLIGHT | 0 | # At what camera height should it be fully faded? |
| HIGHLIGHT_ALPHA | 0.2 | # Used for the Civil War highlight |
| ### DECENTRALIZED ### |  |  |
| COLOR_DECENTRALIZED_COUNTRY | { 0.88 0.83 0.72 1.0 } | # Alpha can control blend with country color |
| ### IMPASSABLE TERRAIN ### |  |  |
| COLOR_IMPASSABLE_TERRAIN | { 0.0 0.0 0.0 0.5 } | # Alpha can control blend with terrain color |
| IMPASSABLE_TERRAIN_TILING | 100 | # Tiling of texture |
| IMPASSABLE_TERRAIN_HEIGHT | 8 | # Height of parallax effect |
| ### CLOSE DISTANCE FADE ### # Used for borders and impassable terrain |  |  |
| DISTANCE_FADE_START | 100.0f | # Height at which to start fading out when zooming in |
| DISTANCE_FADE_END | 30.0f | # Height at which to be fully faded out |
| ### WAR / DIPLOMACY ### |  |  |
| COLOR_WAR_SELF | { 0.11 0.46 0.05 @opacity } | # Green |
| COLOR_WAR_ENEMY | { 0.5 0.04 0.02 @opacity } | # Red |
| COLOR_WAR_ALLY | { 0 0.2 0.5 @opacity } | # Blue |
| COLOR_WAR_NEUTRAL | { 0 0 0 0 } | # No color |
| COLOR_DIPLO_PLAY_ALLY | { 0 0.2 0.5 0.25 } | # Very faded Blue |
| COLOR_DIPLO_PLAY_ENEMY | { 0.5 0.04 0.02 0.25 } | # Very faded Red |
| COLOR_DIPLO_PLAY_UNDECIDED | { 0.85 0.85 0.08 0.1 } | # Extremely faded Yellow |
| # MISC |  |  |
| STATE_REGION_COLOR_STRENGTH | 0.2 | # In the Production Lens, how much should the color of the State be based of the State Color? |
| MAP_COLOR_SATURATION_LOW | 0.25 | # Push up the saturation of Map Colors if below 25% |
| MAP_COLOR_SATURATION_HIGH | 0.75 | # Push down the saturation of Map Colors if above 75% |
| COLOR_COUNTRY_CREATE_IN | { 0.11 0.46 0.05 1 } | # Green highlight States on the map when hovering it to release |
| COLOR_COUNTRY_CREATE_NOT_IN | { 0.5 0.04 0.02 1 } | # Red highlight States on the map when hovering it to release |
| # DIPLOMACY |  |  |
| COLOR_RELATIONS_MIN | { 0.5 0.04 0.02 @opacity } | # Red (full alpha, use for heatmap) |
| COLOR_RELATIONS_MAX | { 0.11 0.46 0.05 @opacity } | # Green (full alpha, use for heatmap) |
| COLOR_INFAMY_MIN | { 0.5 0.04 0.02 0 } | # Red (no alpha) |
| COLOR_INFAMY_MAX | { 0.5 0.04 0.02 @opacity } | # Red (full alpha, use for heatmap) |
| # AI ATTITUDE MAP COLORS @full = 1 @slightly = 0.75 @very_slightly = 0.5 |  |  |
| COLOR_DIPLOMACY_SELF | { 0 0.2 0.5 @slightly} | # Blue |
| COLOR_BELLIGERENT | { 0.5 0.04 0.02 @full } | # Red |
| COLOR_DOMINEERING | { 0.5 0.04 0.02 @full } | # Red |
| COLOR_ANTAGONISTIC | { 0.5 0.04 0.02 @slightly } | # Slightly Red |
| COLOR_REBELLIOUS | { 0.5 0.04 0.02 @full } | # Red |
| COLOR_WARY | { 0.5 0.04 0.02 @very_slightly } | # Very little red |
| COLOR_DISINTERESTED | { 1 1 1 0 } | # No color |
| COLOR_CAUTIOUS | { 0.85 0.85 0.08 0.5 } | # Yellow |
| COLOR_CONCILIATORY | { 0.11 0.46 0.05 @very_slightly } | # Very little green |
| COLOR_COOPERATIVE | { 0.11 0.46 0.05 @very_slightly } | # Very little green |
| COLOR_LOYAL | { 0.11 0.46 0.05 @slightly } | # Slightly Green |
| COLOR_PROTECTIVE | { 0.11 0.46 0.05 @slightly } | # Slightly Green |
| COLOR_GENIAL | { 0.11 0.46 0.05 @full } | # Green |
| COLOR_DEFIANT | { 0.11 0.46 0.05 @full } | # Green |
| COLOR_ALOOF | { 0.85 0.85 0.08 0.5 } | # Yellow |
| # HEAT MAP THAT CAN BE PLACED ON A GOOD - BAD SCALE |  |  |
| HEAT_MAP_BAD | { 0.5 0.04 0.02 1 } | # Red |
| HEAT_MAP_GOOD | { 0.11 0.46 0.05 1 } | # Green |
| HEAT_MAP_NEUTRAL | { 0.75 0.75 0.75 1 } | # White |
| # LOCAL PRICES |  |  |
| LOCAL_PRICE_MAP_HIGH | { 1.000 0.674 0.454 2 } | # Gold |
| LOCAL_PRICE_MAP_LOW | { 0.410 0.670 0.740 2 } | # Blue |
| LOCAL_PRICE_MAP_MID | { 0.75 0.75 0.75 1 } | # White |
| # COLORS FOR RADICALS AND LOYALISTS HEAT MAP |  |  |
| RADICALS_HEAT_BASE | { 0.5 0.04 0.02 0 } | # Red, but zero alpha |
| RADICALS_HEAT_MAX | { 0.5 0.04 0.02 1 } | # Red |
| RADICAL_PERCENTAGE_OF_POPULATION | 0.25 | # In the Radicals Map Mode, if the amount of radicals in a state is above X the state will be colored with RADICALS_HEAT_MAX |
| LOYALISTS_HEAT_BASE | { 0.11 0.46 0.05 0 } | # Green, but zero alpha |
| LOYALISTS_HEAT_MAX | { 0.11 0.46 0.05 1 } | # Green |
| LOYALIST_PERCENTAGE_OF_POPULATION | 0.25 | # In the Loyalists Map Mode, if the amount of loyalists in a state is above X the state will be colored with LOYALISTS_HEAT_MAX |
| #RELIGION/CULTURE MAPMODE PARAMETERS |  |  |
| RELIGION_SECOND_COLOR_CUTOFF | 0.3 | # Ratio of Rel2 / (Rel1+Rel2) has to be at least this much to be shown |
| RELIGION_THIRD_COLOR_CUTOFF | 0.1 | # Ratio of Rel3 / (Rel1+Rel2+Rel3) has to be at least this much to be shown |
| RELIGION_SECOND_COLOR_SCALING | 0.6 | # Ratio of Rel2 / (Rel1+Rel2) is scaled by this when lerping Color1 to Color2 |
| RELIGION_THIRD_COLOR_SCALING | 0.5 | # Ratio of Rel3 / (Rel1+Rel2+Rel3) is scaled by this much when lerping Color1+2 to Color 3 |
| CULTURE_SECOND_COLOR_CUTOFF | 0.4 | # Ratio of Cult2 / (Cult1+Cult2) has to be at least this much to be shown |
| CULTURE_THIRD_COLOR_CUTOFF | 0.2 | # Ratio of Cult3 / (Cult1+Cult2+Cult3) has to be at least this much to be shown |
| CULTURE_SECOND_COLOR_SCALING | 0.6 | # Ratio of Cult2 / (Cult1+Cult2) is scaled by this when lerping Color1 to Color2 |
| CULTURE_THIRD_COLOR_SCALING | 0.5 | # Ratio of Cult3 / (Cult1+Cult2+Cult3) is scaled by this much when lerping Color1+2 to Color 3 |
| RELIGION_MINORITY_COLOR_CUTOFF | 0.334 | # Ratio of Minority / (Majority+Minority) has to be at least this much to be shown |
| CULTURE_MINORITY_COLOR_CUTOFF | 0.334 | # Ratio of Minority / (Majority+Minority) has to be at least this much to be shown |
| #COLORS FOR POLLUTION HEAT MAP |  |  |
| POLLUTION_HEAT_BASE | { 0.3 0.25 0.16 0 } |  |
| POLLUTION_HEAT_MAX | { 0.3 0.25 0.16 1 } |  |
| POLLUTION_COLOR_CEILING_VALUE | 0.6 | # In the Pollution map mode a state will reach POLLUTION_HEAT_MAX at this fraction of POLLUTION_MAX |
| #COLORS FOR OBSTINANCE HEAT MAP |  |  |
| OBSTINANCE_HEAT_BASE | { 0.0 0.0 1.0 0 } |  |
| OBSTINANCE_HEAT_MAX | { 0.0 0.0 1.0 1 } |  |
| OBSTINANCE_COLOR_CEILING_VALUE | 0.6 | # In the Obstinance map mode a state will reach OBSTINANCE_HEAT_MAX at this fraction of OBSTINANCE_MAX |
| # Harvest condition map mode |  |  |
| HARVEST_CONDITION_COLOR_MIN_ALPHA | 0.4 | # Min color of the province is the color of the harvest condition type (max color) with this alpha |
| # The color of the province affected by a harvest condition is scaled based on the max intensity in the area. # This value defines how many different colors a harvest condition area can have inside. # E.g. 4 will give the following brackets: 0-0.25, 0.25-0.5, 0.5-0.75, 0.75-1 |  |  |
| HARVEST_CONDITION_NUM_COLOR_BRACKETS | 5 |  |
| HARVEST_CONDITION_FADE_DURATION | 0.4 | # Fade duration of the harvest condition map mode when changing highlighted types |
| #Colors for the starvation map mode |  |  |
| STARVATION_HEAT_BASE | { 0.6 0.25 0.08 0 } | #Base color for starvation map mode |
| STARVATION_ADDITIONAL_BASE_ALPHA | { 0.0 0.0 0.0 0.2 } | #After the population blending we add this much alpha to the color so low % states are more visible |
| MILD_STARVATION_HEAT_MAX | { 0.741 0.301 0.082 1} | #Max color for Mild Starvation |
| MILD_STARVATION_HEAT_WEIGHT | 1 | #Weight used when blending Mild and Severe starvation colors |
| SEVERE_STARVATION_HEAT_MAX | { 0.69 0.08 0.06 1 } | #Max color for Severe Starvation |
| SEVERE_STARVATION_HEAT_WEIGHT | 3 | #Weight used when blending Mild and Severe starvation colors |
| STARVATION_COLOR_CEILING_VALUE | 0.8 | #At what % of state population starving do we reach the max color |

### MapName

| Define | Default Value | Dev Comment |
|---|---|---|
| NAME_DRAW_DISTANCE | 4000.0 | # Remove names beyond this distance |
| NAME_FONT_NAME | "PlayfairDisplay" | # Font used for drawing the map names |
| NAME_FONT_SIZE | 80 | # Font size used for drawing the map names |
| FADE_SPEED | 2.0 | # How fast names fade in/out |
| MAX_OPACITY | 0.8 |  |
| MIN_OPACITY | 0.0 | # minimum opacity. Names hidden by draw distance will still fade to 0 |
| MIN_PROVINCES | 3 | # minimum number of provinces for a name to be generated |
| ZOOM_STEPS_VISIBLE_SCALES | { 0.0 0.0 # 0 0.0 0.0 # 1 0.0 0.0 # 2 0.0 0.0 # 3 0.0 0.05 # 4 0.0 0.1 # 5 0.0 0.2 # 6 0.0 1.0 # 7 Terrain map 0.0 1.0 # 8 0.0 2.0 # 9 0.0 5.0 # 10 Flatmap 0.0 5.0 # 11 0.0 5.0 # 12 0.0 5.0 # 13 No 2D UI on Map 0.0 5.0 # 14 0.0 5.0 # 15 } | # Each map-name has a scale. This list contains min-max values for each zoom step. If a name's scale is outside that range it will not be visible # min (hides names that are too small) # max (hides names when they get to large) |

### JominiMapGraphics

| Define | Default Value | Dev Comment |
|---|---|---|
| MAP_OBJECT_CELL_COUNT | 100 |  |
| MAP_OBJECT_FADE_SPEED | 5.0 |  |
| COUNTRY_NAMES_TEST_LINES_SPACING | 3.0 |  |
| COUNTRY_NAMES_SCALE | 0.6 |  |
| COUNTRY_NAMES_SCALE_CAP_WIDTH | 0.9 |  |
| COUNTRY_NAMES_SCALE_CAP_HEIGHT | 0.6 |  |
| COUNTRY_NAMES_NUM_LINE_TESTS | 1 |  |
| COUNTRY_NAMES_MAX_STRETCH_FACTOR | 1.6 |  |
| COUNTRY_NAMES_STRIDE_SIZE | 8 |  |
| COUNTRY_NAMES_LOD_FACTOR | 0.05 | # As a form of AA, Names get blurrier as the texel/pixel ratio increases. Blur amount will be lod factor * texel/pixel ratio |
| COUNTRY_NAMES_THICKNESS_BIAS | 0.0 | # More bias = thicker map names. Can be used to solve artifacts caused by thin areas |

### JominiGraphics

| Define | Default Value | Dev Comment |
|---|---|---|
| BLOOM_ITERATIONS | 6 | # Overwritten by environment.txt |
| NULL_ENTITY | "test_object_entity" |  |
| NULL_MESH | "test_object_mesh" |  |

### JominiEars

| Define | Default Value | Dev Comment |
|---|---|---|
| RANGE_MIN | 10.0 |  |
| RANGE_MAX | 2000.0 |  |

### Graphics

| Define | Default Value | Dev Comment |
|---|---|---|
| # Gradient Borders |  |  |
| PROVINCE_BORDER_FADE_NEAR | 200 |  |
| PROVINCE_BORDER_FADE_FAR | 2000 |  |
| STATE_BORDER_FADE_NEAR | 200 |  |
| STATE_BORDER_FADE_FAR | 2000 |  |
| IMPASSABLE_BORDER_FADE_NEAR | 500 |  |
| IMPASSABLE_BORDER_FADE_FAR | 600 |  |
| DRAW_SHADOWS_CUTOFF | 400 |  |
| DRAW_SHADOWS_FADE_LENGTH | 50 |  |
| # Tweaks the papermap shoreline stripes |  |  |
| SHORELINE_MASK_BLUR | 4.5 | # Recommended Range [1.0 - 10.0] The terrain/sea mask, blurrier mask can make the lines extend more |
| SHORELINE_EXTENT_STR | 8.0 | # Recommended Range [0.0 - 10.0] Simple strength of the lines |
| SHORELINE_ALPHA | 0.6 | # Recommended Range [0.0 - 5.0] Simple alpha tweaking |
| SHORELINE_UV_SCALE | 40 | # Recommended Range [10 - 100] (integer) Larger UV scale gives tighter lines |
| # Overlay details |  |  |
| FLATMAP_FOLDS_COLOR | { 1.0 1.0 1.0 0.12 } | # Color and Alpha of Folds [ Red channel ] |
| FLATMAP_LINES_COLOR | { 0.0 0.0 0.0 0.4 } | # Color and Alpha of Lines [ Green channel ] |
| FLATMAP_FOLDS_COLOR | { 0.0 0.0 0.0 1.0 } | # Opacity of flatmap details on land |
| FLATMAP_OVERLAY_LAND_OPACITY | 0.45 |  |
| FLATMAP_EQUATOR_POSITION | 0.58 | # Position offset from top [ 0.0 - 1.0 ] |
| FLATMAP_EQUATOR_TILING | 24.0 | # Tiling scale of equator texture (Effectively size) |
| # Bottom mesh tint gradient (Applied globally to all meshes) |  |  |
| MESHTINT_HEIGHT_MIN | 0.0 | # Tint begin (from bottom) |
| MESHTINT_HEIGHT_MAX | 0.07 | # Tint end |
| MESHTINT_COLOR | { 0.20 0.14 0.06 1.0 } | # Tint Alpha and Color (effectitvely disabled with alpha 0.0) |
| # SSAO modifiers |  |  |
| SSAO_TREE_ALPHA | 0.2 | # AO Alpha on trees |
| SSAO_TERRAIN_ALPHA | 0.85 | # AO Alpha on the terrain under trees and buildings |
| SSAO_MESH_COLOR | { 0.20 0.14 0.06 0.0 } | # AO Alpha and color on buildings (alpha unused) |
| # Fog camera modifiers |  |  |
| FOG_CLOSE_OFFSET | 10 | # Fog center offset at close zoom level |
| FOG_FAR_OFFSET | 260 | # Fog center offset at far zoom level |
| FOG_WIDTH_SCALE | 1.6 | # Fog width scaling |
| # Piechart colors |  |  |
| PIE_CHART_TIMER_UNFILLED_COLOR | { 0.4 0.4 0.4 1.0 } |  |
| PIE_CHART_TIMER_FILLED_COLOR | { 0.85 0.72 0.44 1.0 } |  |
| # Map markers |  |  |
| MAP_MARKER_MERGE_DISTANCE_FOR_STACK | 10 | # The max screen distance in pixels between map markers (center points) for them to form a stack |
| MAP_MARKER_MERGE_PROVINCES | 800.0 |  |
| MAP_MARKER_MERGE_STATES | 1600.0 |  |
| MAP_MARKER_MERGE_PROVINCES_STRATEGIC_REGION | 1600.0 |  |
| MAP_MARKER_FULL_UPDATE_FREQUENCY | 1.0 | #Do the heavy parts of the map markers only every X seconds |
| FRONT_MARKER_ADVANTAGE_HIGH | 60 |  |
| FRONT_MARKER_ADVANTAGE_LOW | 25 |  |
| # Error adjustment |  |  |
| MINIMUM_PROVINCE_SIZE_IN_PIXELS | 0 | # Provinces that are smaller than that are just making the game unplayable. It doesn't affect the game, just informs in the error.log |
| # Flat map specific |  |  |
| FLAT_MAP_HEIGHT | 3.92 |  |
| FLAT_MAP_FADE_SPEED | 5.0 | # How fast to fade to/from flat map state |
| FLAT_MAP_ZOOM_STEP | 10 | # At which zoom step to fade to flat map |
| # Water fixes |  |  |
| WATER_SHADOW_MULTIPLIER | 0.75 | # Controls water shadow brightness ( multiplies the environment cubemap by this value and adds it to the shadow as light ) |
| # Goods colors |  |  |
| GOOD_CATEGORY_MILITARY | { 0.29 0.16 0.17 1 } |  |
| GOOD_CATEGORY_STAPLE | { 0.18 0.28 0.24 1 } |  |
| GOOD_CATEGORY_INDUSTRIAL | { 0.29 0.24 0.16 1 } |  |
| GOOD_CATEGORY_LUXURY | { 0.33 0.2 0.32 1 } |  |
| # Morale colors |  |  |
| MORALE_HIGH | { 0.14 0.60 0.2 1 } |  |
| MORALE_MEDIUM | { 0.7 0.5 0.1 1 } |  |
| MORALE_LOW | { 0.65 0.1 0.1 1 } |  |
| # Organization colors |  |  |
| ORGANIZATION_HIGH | { 0.14 0.60 0.2 1 } |  |
| ORGANIZATION_MEDIUM | { 0.7 0.5 0.1 1 } |  |
| ORGANIZATION_LOW | { 0.65 0.1 0.1 1 } |  |
| # Loyalty colors |  |  |
| LOYALTY_LOYALIST | { 0.39 0.67 0.33 1 } |  |
| LOYALTY_RADICAL | { 0.88 0.34 0.34 1 } |  |
| LOYALTY_NEUTRAL | { 0.7 0.7 0.7 1 } |  |
| UNIMPORTANT_ELEMENT_ALPHA | 0.3 |  |
| # Devastation texture |  |  |
| DEVASTATION_MATERIAL_NAME | "DYNAMIC-Devastation_Mud_01" | # Material name from materials.settings |
| POLLUTION_MATERIAL_NAME | "DYNAMIC-Pollution_01" | # Material name from materials.settings |
| # Revolution layer |  |  |
| REVOLUTION_MAP_OBJECT_LAYER | "revolution_dynamic" |  |
| REVOLUTION_MAP_OBJECT_UPDATE_PROVINCES_PER_FRAME | 16 | # Max number of provinces that may be updated per frame. |
| REVOLUTION_MAP_OBJECT_UPDATE_MAX_TIME_PER_FRAME | 0.002 | # Max time per frame to spend on dynamic terrain updates in seconds. |
| # Night map objects |  |  |
| NIGHT_MAP_OBJECT_LAYERS | { "night_dynamic" "night_effects" } | # Layers that activate at night |
| DAY_MAP_OBJECT_LAYERS | { "day_dynamic" "day_effects" } | # Layers that activate at day |
| # Dynamic map objects |  |  |
| HIDDEN_MAP_OBJECT_LAYERS | { "mines_dynamic" "farms_dynamic" "forestry_dynamic" } | # These layers are hidden by default when the game starts |
| DYNAMIC_MAP_OBJECT_LAYERS | { "semidynamic" "semidynamic_medium" "semidynamic_high" "mines_dynamic" "farms_dynamic" "forestry_dynamic" } | # These layers are cut by city growth and roads |
| DYNAMIC_MAP_OBJECT_MASK_THRESHOLD_SHOW | 0.1 | # When dynamic objects are being shown/hidden they use the material mask. This value determines the point at which the mask will make the objects to show/hide. |
| DYNAMIC_MAP_OBJECT_MASK_THRESHOLD_HIDE | 0.05 |  |
| DYNAMIC_TERRAIN_ROAD_WIDTH | 2.5 | # Controls how wide roads are considered to be when clearing map objects |
| DYNAMIC_TERRAIN_LAZY_UPDATE_PROVINCES_PER_FRAME | 16 | # Max number of provinces that may be updated per frame. |
| DYNAMIC_TERRAIN_LAZY_UPDATE_MAX_TIME_PER_FRAME | 0.0012 | # Max time per frame to spend on dynamic terrain updates in seconds. |
| # Route Spline fix |  |  |
| ROUTE_GENERATION_NAV_MESH_DENSITY | 0.375 | # Controls the density of vertexes in the navmesh used to generate the road system |
| # Flags |  |  |
| FLAG_TEXT_ICON_FONT_SIZE | 16 |  |
| FLAG_TEXT_ICON_SIZE | { 21 14 } |  |
| FLAG_TEXT_ICON_RESOLUTION | { 48 32 } |  |
| FLAG_TEXT_ICON_OFFSET | { 0 1 } |  |
| POWER_BLOC_COA_TEXT_ICON_FONT_SIZE | 16 |  |
| POWER_BLOC_COA_TEXT_ICON_SIZE | { 22 22 } | # same height as country flags text icons here. |
| POWER_BLOC_COA_TEXT_ICON_RESOLUTION | { 128 128 } | # somewhat high resolution here, so it doesn't get blurry in large text nor with GUI scaling. |
| POWER_BLOC_COA_TEXT_ICON_OFFSET | { 0 4 } |  |
| COA_FLAGS_FRAMES_BETWEEN_UPDATES | 30 | # Update country and power bloc Coat of Arms every this number of frames |
| COA_FLAGS_UPDATES_BETWEEN_CLEANUP | 20 | # Remove unused Coat of Arms every this number of updates |
| ALERTS_FRAMES_BETWEEN_UPDATES | 5 |  |
| # Coa |  |  |
| COUNTRY_COLOR_LIST_NAME | "country_color_list" | # The Coat-of-Arms list to use when generating dynamic country map colors |
| # Scaled Distance Roughness |  |  |
| DISTANCE_ROUGHNESS_POSITION | 1.8 | # Position to start blend |
| DISTANCE_ROUGHNESS_BLEND | 80.0 | # Blend range |
| DISTANCE_ROUGHNESS_SCALE | 0.5 | # Roughness multiplier scale |
| # Grid cell scores used for cities |  |  |
| CELL_SCORE_BASE | 1.0 | # A cell that is 100% within the province will get the full base score. A cell outside the province will get 0. A 50/50 cell will get approximately half base score. |
| CELL_SCORE_UNDER_WATER_PENALTY | 10.0 | # penalty per depth-units under water. Added for each corner of the cell |
| CELL_SCORE_SLOPE_MIN | 0.075 | # amount of slope allowed before penalty kicks in. value corresponds to the slope's 'k' in f(x)=kx+m |
| CELL_SCORE_SLOPE_PENALTY | 6 | # penalty per 'k' above the limit. Does not scale linearly with slope angle so might be tricky to tweak |
| CELL_SCORE_RIVER_PENALTY | 10.0 | # Penalty per "to-close-to-river"-units (distance-from-cell-center-to-river-edge - bias) |
| CELL_SCORE_ROAD_PENALTY | 10.0 |  |
| # Front entities graphics |  |  |
| FRONT_ENTITIES_CUTOFF | 300 | # Zoom at which we hide all front entities |
| FRONT_DIORAMA_GRID_WIDTH | 20 | # Grid width of a diorama inside a province |
| FRONT_DIORAMA_GRID_HEIGHT | 20 | # Grid height of a diorama inside a province |
| FRONT_DIORAMA_GRID_SCALE | 1.1 | # Grid cell scale of a diorama inside a province |
| FRONT_DIORAMA_STATE_DEFAULT | "idle" | # Animation state name for entities when they do nothing (before war) |
| FRONT_DIORAMA_STATE_NO_GENERAL | "defend" | # Animation state name for entities without a general's order |
| FRONT_DIORAMA_FLAT_MAP_ENTITY | "generic_flatmap_unit_entity" | # The entity that is visible in the flat map mode instead of front entities |
| # Battle entities graphics |  |  |
| BATTLE_ENTITIES_CUTOFF | 300 | # Zoom at which we hide all battle entities |
| BATTLE_DIORAMA_GRID_WIDTH | 30 | # Grid width of a diorama inside a province |
| BATTLE_DIORAMA_GRID_HEIGHT | 40 | # Grid height of a diorama inside a province |
| BATTLE_DIORAMA_GRID_SCALE | 1.1 | # Grid cell scale of a diorama inside a province |
| BATTLE_DIORAMA_ATTACKER_STATE | "advance" | # Animation state name for the attacker side |
| BATTLE_DIORAMA_DEFENDER_STATE | "defend" | # Animation state name for the defender side |
| BATTLE_DIORAMA_DEFEAT_STATE | "defeat" | # Animation state name for defeated entities during the battle |
| BATTLE_DIORAMA_VICTORY_SIDE_STATE | "victory" | # Animation state name for entities on the winning battle side after the battle |
| BATTLE_DIORAMA_DEFEATED_SIDE_STATE | "idle" | # Animation state name for entities on the defeated battle side after the battle |
| BATTLE_DIORAMA_DESTRUCTION_DELAY | 5 | # How many seconds we show diorama entities after the battle is over |
| BATTLE_DIORAMA_VFX_START_TIME | 0 | # After how many seconds we show VFX on battle sides after the battle is over (must be <= BATTLE_DIORAMA_DESTRUCTION_DELAY) |
| BATTLE_DIORAMA_VFX_VICTORY_SIDE | "battle_diorama_victory_entity" | # Entity that spawns after BATTLE_DIORAMA_VFX_START_TIME seconds after the battle end on the victory side |
| BATTLE_DIORAMA_VFX_DEFEATED_SIDE | "battle_diorama_defeat_entity" | # Entity that spawns after BATTLE_DIORAMA_VFX_START_TIME seconds after the battle end on the defeated side |
| DAYS_AFTER_BATTLE_TO_SHOW_ENTITY | 7 | # For how long to show battle environment entities after the battle |
| MILITARY_ENTITIES_FLYING_ENTITY_HEIGHT | 1 | # If entity locator is higher than this value, then the entity is considered as flying i.e. doesn't occupy a cell and doesn't hide map objects beneath |
| MILITARY_ENTITIES_TOGGLE_MAP_OBJECTS_IN_RADIUS | 2 | # How many cells around entities should be used for hiding map objects (trees) |
| MILITARY_ENTITIES_DITHER_DURATION | 1.0 | # How many seconds it takes for diorama entities to gradually appear or disappear. Applies to all dioramas: front, land battle, fleet, and naval battle dioramas |
| OCCUPATION_ENTITY | "military_occupation_flag_entity" | # Entity that appears on occupied territory by occupying nation |
| OCCUPATION_ENTITY_DIRECTION | { 0.0 0.0 -1.0 } | # Direction of occupation entity |
| COUNTRY_COLOR_BUFFER_TEXTURE_RESERVE_SIZE | 700 | # How many countries buffer data is allocated for initially. If more countries are created, the buffer will be resized to accommodate them. |
| POWER_BLOC_BUFFER_TEXTURE_RESERVE_SIZE | 50 | # How many power blocs buffer data is allocated for initially. If more power blocs are created, the buffer will be resized to accommodate them. |
| POWER_BLOC_COLOR_UPDATE_NUM_FRAMES_BETWEEN | 30 | # Number of frames to wait between powerbloc mapcolor updates |
| # Harvest condition graphics |  |  |
| HARVEST_CONDITION_ENTITIES_CUTOFF | 600 | # Zoom at which we hide all harvest condition entities |
| HARVEST_CONDITION_ENTITIES_INTERVAL | 50 | # Interval between entities on areas affected by harvest conditions |
| HARVEST_CONDITION_ENTITY | "harvest_condition_sound_entity" | # Entity that spawns on areas affected by harvest conditions |
| HARVEST_CONDITION_INTENSITY_MAX | 10 |  |
| # Earthquake camera shake |  |  |
| EARTHQUAKE_SHAKE_AMPLITUDE | 0.25 | # Amplitude multiplier |
| EARTHQUAKE_SHAKE_DURATION | 10.0 | # Duration in seconds |
| EARTHQUAKE_SHAKE_DISTANCE_RADIUS | 250 | # Distance radius in game units |
| EARTHQUAKE_SHAKE_FREQUENCY | 2 | # Frequency multiplier |
| EARTHQUAKE_SHAKE_EASE_IN_PORTION | 0.5 | # Portion of the earthquake duration used for easing in |
| EARTHQUAKE_SHAKE_EASE_OUT_PORTION | 0.5 | # Portion of the earthquake duration used for easing out |
| EARTHQUAKE_SHAKE_MIN_ZOOM_STEP | 0 | # The earthquake will not affect the camera if zoomed in closer than this zoom step |
| EARTHQUAKE_SHAKE_MAX_ZOOM_STEP | 800 | # The earthquake will not affect the camera if zoomed out further than this zoom step |
| EARTHQUAKE_SHAKE_SMOOTHSTEP_A | 3.0 | # Smoothstep power for easing in and out |
| EARTHQUAKE_SHAKE_SMOOTHSTEP_B | 2.0 | # Smoothstep power for easing in and out |
| EARTHQUAKE_SHAKE_PHASE_SPEED_X | 28.0 | # Speed of phase movement in X direction |
| EARTHQUAKE_SHAKE_PHASE_SPEED_Y | 22.0 | # Speed of phase movement in Y direction |

### Frontend

| Define | Default Value | Dev Comment |
|---|---|---|
| CAMERA_START_X | 4150.0 | # Initial position in main menu |
| CAMERA_START_Y | 1500 | # Y is height |
| CAMERA_START_Z | 2700.0 |  |

### Camera

| Define | Default Value | Dev Comment |
|---|---|---|
| FOV | 55 | # Field-of-View |
| ZNEAR | 1 |  |
| ZFAR | 50000 |  |
| EDGE_SCROLLING_PIXELS | 10 | # how many pixels from window edge that will trigger edge scrolling |
| SCROLL_SPEED | 0.045 | # higher values = faster camera. NOTE that this is tweakables from settings as well |
| ZOOM_RATE | 0.2 | # Zoom when right-mouse down |
|  | # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 |  |
| ZOOM_STEPS | { 24 32 40 50 75 100 200 300 400 600 800 1000 1200 1500 2500 4500 } |  |
| ZOOM_STEPS_TILT | { 35 40 45 48.5 50 52.5 55 60 65 70 75 80 80 85 85 85 } |  |
| ZOOM_STEPS_MIN_TILT | { 35 35 35 35 35 38 40 40 45 50 50 50 50 50 50 50 } |  |
| ZOOM_STEPS_MAX_TILT | { 89 89 89 89 89 89 89 89 89 89 89 89 89 89 89 89 } |  |
| MAX_PAN_TO_ZOOM_STEP_EXTRA_CLOSE | 1 | # The camera will lower to this height (but only if above it) when panning to characters/provinces etc. |
| MAX_PAN_TO_ZOOM_STEP_CLOSE | 7 |  |
| MAX_PAN_TO_ZOOM_STEP_FAR | 10 |  |
| MAX_PAN_TO_ZOOM_STEP_EXTRA_FAR | 14 |  |
| # Debug defines |  |  |
| DEBUG_GAMEPAD_LOWSPEED | 25.0 |  |
| DEBUG_GAMEPAD_NORMALSPEED | 100.0 |  |
| DEBUG_GAMEPAD_HIGHSPEED | 300.0 |  |
| DEBUG_GAMEPAD_SENSITIVITY | 2.0 |  |

### Cities

| Define | Default Value | Dev Comment |
|---|---|---|
| #Select a province and use the "Cities.DrawDebugLines" for easy tweaking |  |  |
| NUM_GRID_LAYOUTS | 16 | # How many different grid layouts are available for a city to choose. Grid layouts are randomly generated and cities select them randomly |
| GRID_SCALE | 1.1 |  |
| MESH_SCALE | 1.0 | #scale all meshes by this |
| MAX_ACTIVE_SOUND_EFFECTS | 5 |  |
| CITY_RIVER_DISTANCE_BIAS | 0.75 | # Higher values = more river avoidance |
| FARM_RIVER_DISTANCE_BIAS | 0.75 |  |
| MINE_RIVER_DISTANCE_BIAS | 0.75 |  |
| PORT_RIVER_DISTANCE_BIAS | 0.75 |  |
| WOOD_RIVER_DISTANCE_BIAS | 0.75 |  |
| CITY_ROAD_DISTANCE_BIAS | -1.00 |  |
| FARM_ROAD_DISTANCE_BIAS | 0.25 |  |
| MINE_ROAD_DISTANCE_BIAS | 0.25 |  |
| PORT_ROAD_DISTANCE_BIAS | -1.00 |  |
| WOOD_ROAD_DISTANCE_BIAS | 0.25 |  |
| RICH_SOL | 20.0 | # Buildings above this average SoL use the rich model |
| MID_SOL | 10.0 | # Buildings above this average SoL use the middleclass model |
| RESIDENTIAL_CHANGE_DELAY | 5.0 | # Time between updating the residential buildings of a city ( + 0-1 second for some random variance ) |
| RESIDENTIAL_PROMOTE_ENTITY | "residential_promotion_entity" | # Entity that is spawned on a residential building that is promoted due to demographics changes |
| RESIDENTIAL_DEMOTE_ENTITY | "residential_demotion_entity" | # Entity that is spawned on a residential building that is demoted due to demographics changes |
| CITY_VFX_MAX_ENTITIES | 128 | # The limit of how many VFX instances can exist at the same time |
| CITY_VFX_ZOOM_CUTOFF | 250 | # zoom at which we hide all city VFXes |
| CITY_PARTICLES_ZOOM_CUTOFF | 200 | # zoom at which we hide all city particle effects (for example chimney smoke) |
| # For each camera distance to the city there is a cut-off factor for the amount of visible buildings in the city # if the distance is lower than the first step, then the factor is 0, i.e. all buildings are visible # if the distance is higher than the last step, then the factor from the last step is taken # if the distance is between steps, then the factor is calculated linearly |  |  |
| CITY_BUILDINGS_CUTOFF_DISTANCES | { 300 400 600 } | # steps of distances from camera to city to which apply corresponding cut-off factors, must be sorted from low to high |
| CITY_BUILDINGS_CUTOFF_FACTORS | { 0 0.7 0.95 } | # which share of buildings to cut off at a certain distance step, must be sorted from low to high |
| NIGHT_LIGHT_COLOR_DEFAULT | { 1.0 0.16 0.035 6.5 } | # Lights color, Alpha is max intensity |
| NIGHT_LIGHT_FADE_TIME | 0.35 | # Time for indiviual lights to fade in/out from when they activate |
| NIGHT_LIGHT_ACTIVATE_BEGIN | 0.3 | # Time at which lights start to activate, on a 0.0 - 1.0 cycle where day is at 0.0 and 0.5 is the midpoint between day and night |
| NIGHT_LIGHT_ACTIVATE_END | 0.75 | # Time at which lights finish activating |

### Fortifications

| Define | Default Value | Dev Comment |
|---|---|---|
| GAME_OBJECT_LOCATOR | "fortification" | # Key of the locator used for fortification entities |
| CONSTRUCTION_ENTITY | "building_construction_2x2_entity" | # Entity that spawns on provinces with fortification construction in progress |
| ENTITY_DEFAULT | "strait_fortification_tower_european_entity" | # Default fortification entity to use if the culture-specific one is not found |
| ENTITY_FORMAT | "strait_fortification_tower_{}_entity" | # Format of the fortification entities, with {} being replaced by the graphical culture name (european, arabic, asian, african, latin) |
| TOGGLE_MAP_OBJECTS_IN_RADIUS | 2 | # How many cells around fortification entities should be used for hiding map objects (trees) |

### Routes

| Define | Default Value | Dev Comment |
|---|---|---|
| DIRTROAD_BRIDGES | { "dirtroad_bridge_01" } |  |
| RAILROAD_1_BRIDGES | { "railroad_bridge_01" "railroad_bridge_02" } |  |
| BRIDGE_SIZES | { "_small_mesh" "_medium_mesh" "_large_mesh" } |  |
| CARAVAN_DISTANCE_OPACITY_THRESHOLD | 0.75 | # Ratio of the caravan distance to camera and cut-off distance at which its entities start to become transparent |
| LAND_ENTITIES_CUTOFF | 300 | # Distance to camera at which land route entities hide |
| NAVAL_ENTITIES_CUTOFF | 650 | # Distance to camera at which naval route entities hide |
| AIR_ENTITIES_CUTOFF | 450 | # Zoom at which air route entities hide |
| LAND_ENTITIES_UPDATE_DISTANCE_RATIO | 0.0005 | # Ratio of traveled distance of the caravan and the distance to camera which defines the update frequency of caravan entities. The higher it is the less frequently they update |
| NAVAL_ENTITIES_UPDATE_DISTANCE_RATIO | 0.00025 | # Ratio of traveled distance of the caravan and the distance to camera which defines the update frequency of caravan entities. The higher it is the less frequently they update |

### Portrait

| Define | Default Value | Dev Comment |
|---|---|---|
| GRACEFUL_AGING_START | 25 | # After this age, added life expectancy will make a character look younger than they are; the effect grows the further past this point one goes |
| GRACEFUL_AGING_END | 70 | # This is the apparent age at which life expectancy stops slowing down visual aging (each year onwards ages you visually 1 year) |
| MAX_AGE | 100.0 | # At this age portraits will use the special age gene at full strength |
| PORTRAIT_MALE_ADULT_AGE | 18 | # The boy -> male portrait change happens at this age |
| PORTRAIT_FEMALE_ADULT_AGE | 18 | # The girl -> female portrait change happens at this age |

### ProvinceHighlight

| Define | Default Value | Dev Comment |
|---|---|---|
| TEXTURE_WIDTH | 2048 |  |
| TEXTURE_HEIGHT | 1024 |  |
| # Province highlights use poisson disc sampling to create a gradient # Poisson disc allows for a wider sample are with fewer samples |  |  |
| KERNEL_SCALE | 8 | # Size of the sample area, in world space |
| SAMPLE_COUNT | 16 | # How many samples to use (max 16) |

### TravelNetwork

| Define | Default Value | Dev Comment |
|---|---|---|
| FORMATION_CATCHUP_DISTANCE | 40.0 | # If a military formation 3D caravan is this distance behind where it is supposed to be, accelerate with catch-up speed |
| FORMATION_CATCHUP_SPEED_MULTIPLIER | 1.5 | # Accelerate averaged speed by this multiplied when 'catching up' |
| FORMATION_CATCHUP_MIN_SPEED | 15.0 | # Minimum speed for catching up |
| FORMATION_CATCHUP_MAX_SPEED | 250.0 | # Maximum speed for catching up |
| FORMATION_SMOOTHING_STEP_COUNT | 5 | # For smoothing visual movement speed, military formation speed is measured as a rolling average over X steps |
| FORMATION_SMOOTHING_STEP_TIME | 1.0 | # Each step for the military formation speed smoothing is this long |
| FORMATION_SMOOTHING_SPEED_MULTIPLIER | 1.2 | # General speed multiplier applied to the smoothing measurement (it's better to be "ahead" than "behind") |
| FORMATION_ARROW_SAMPLING_STEP | 7.0 | # Size of the sampling step (in "map pixels") of the spline network, used when creating arrows |
| FORMATION_ARROW_SAMPLING_STEP_FLATMAP | 30.0 | # Size of the sampling step (in "map pixels") of the spline network, used when creating arrows, when zoomed out ("flatmap") |

### PowerBlocCoa

| Define | Default Value | Dev Comment |
|---|---|---|
| PREVIEW_BACKGROUND_PATTERN | "pattern_solid.tga" | # Pattern to use as background in coat of arms previews |
| PREVIEW_BACKGROUND_COLOR | { 0.0 0.0 0.0 0.0 } | # First color for the background pattern |
| PREVIEW_SHIELD_PATTERN_COLOR_1 | "red" | # First color for shield patterns |
| PREVIEW_SHIELD_PATTERN_COLOR_2 | "black" | # Second color for shield patterns |
| PREVIEW_CENTER_COLOR_1 | "yellow" | # First color for the center piece |
| PREVIEW_CENTER_COLOR_2 | "black" | # Second color for the center piece |
| COLOR_LIST_NAME | "power_bloc_colors" | # Which list to get colors from when randomly creating a power bloc. Lists are located in common/coat_of_arms/template_lists/color_lists.txt |
| # Positions and scales for each piece type. When updating these make sure to update them in 03_random_power_bloc.txt |  |  |
| SHIELD_PATTERN_SCALE | { 0.72 0.72 } |  |
| SHIELD_FRAME_SCALE | { 0.9 0.9 } |  |
| CENTER_SCALE | { 0.45 0.45 } |  |
| LEFT_SIDE_SCALE | { 0.65 0.65 } |  |
| RIGHT_SIDE_SCALE | { 0.65 0.65 } |  |
| TOP_SCALE | { 0.7 0.7 } |  |
| SHIELD_PATTERN_POSITION | { 0.49 0.6 } |  |
| SHIELD_FRAME_POSITION | { 0.5 0.6 } |  |
| CENTER_POSITION | { 0.49 0.54 } |  |
| LEFT_SIDE_POSITION | { 0.155 0.55 } |  |
| RIGHT_SIDE_POSITION | { 0.82 0.55 } |  |
| TOP_POSITION | { 0.5 0.19 } |  |
| # Layers from bottom to top. If we ever change this, remember to also update `game/common/coat_of_arms/coat_of_arms/03_random_power_bloc.txt` |  |  |
| PIECE_LAYERS_ORDER | { "shield_pattern" "top" "shield_frame" "center" "side" "side" } |  |
| PIECE_LAYER_INDEX_TO_FLIP | 5 |  |

### PowerBlocStatueCamera

| Define | Default Value | Dev Comment |
|---|---|---|
| CAMERA_START_ROTATION | -2.7 |  |
| CAMERA_MIN_DISTANCE | 15.0 |  |
| CAMERA_MAX_DISTANCE | 30 |  |
| CAMERA_START_DISTANCE | 23.0 |  |
| CAMERA_ANGLE | 0.3925 | # in radians, 0.3925 is PI/8 |
| CAMERA_ROTATION_SPEED | 0.15 |  |
| CAMERA_DISTANCE_SPEED | 0.7 |  |

### Navy

| Define | Default Value | Dev Comment |
|---|---|---|
| FLEET_DIORAMA_INTERVAL | 20 | # Interval between fleet dioramas in a sea node |
| FLEET_DIORAMA_CUTOFF | 600 | # Zoom at which we hide all fleet entities |
| FLEET_DIORAMA_TERRAIN_OPACITY_BLEND_SPEED | 4.0 | # Speed at which terrain opacity blends when showing/hiding fleet diorama entities |
| DIORAMA_SELECTION_DITHER_DURATION | 0.5 | # How many seconds it takes for diorama entities to gradually appear or disappear from selection change. Applies to dioramas: fleet and naval battle dioramas |
| DIORAMA_LAND_HEIGHT_OFFSET | 0.5 | # Height offset to consider a ship on land in the diorama |
| WATER_ENTITY_HEIGHT | 0.25 | # Height above water |
| SHIP_ENTITY_STATE_IDLE | "idle" | # Ship is idling, e.g. stationed in a sea node or after battle victory/defeat |
| SHIP_ENTITY_STATE_MOVE | "move" | # Ship is moving in a battle |
| SHIP_ENTITY_STATE_MOVE_LOCAL | "move_local" | # Ship is moving on map routes |
| SHIP_ENTITY_STATE_MOVE_SHIP_VIEWER | "move_ship_viewer" | # Ship is moving in the ship viewer |
| SHIP_ENTITY_STATE_DISENGAGED | "disengaged" | # Weapon entities are in default orientation |
| SHIP_ENTITY_STATE_COMBAT | "combat" | # Weapon entities rotate to fire angle |
| SHIP_ENTITY_STATE_FIRE | "fire" | # Ship fires during battle |
| SHIP_ENTITY_STATE_MISS | "miss" | # Ship evaded the enemy shot during battle |
| SHIP_ENTITY_STATE_DAMAGE | "damage" | # Ship takes damage during battle |
| SHIP_ENTITY_STATE_DAMAGE_CRITICAL | "damage_critical" | # Ship takes critical damage during battle |
| SHIP_ENTITY_STATE_DAMAGE_WEAK | "damage_weak" | # Ship takes weak damage during battle |
| SHIP_ENTITY_STATE_UNDAMAGED | "undamaged" | # Ship has no damage VFX |
| SHIP_ENTITY_STATE_DAMAGED_LIGHT | "damaged_light" | # Ship is lightly damaged |
| SHIP_ENTITY_STATE_DAMAGED_LIGHT_LOCAL | "damaged_light_local" | # Ship is lightly damaged on map routes |
| SHIP_ENTITY_STATE_DAMAGED_HEAVY | "damaged_heavy" | # Ship is heavily damaged |
| SHIP_ENTITY_STATE_DAMAGED_HEAVY_LOCAL | "damaged_heavy_local" | # Ship is heavily damaged on map routes |
| SHIP_ENTITY_STATE_DESTROYED | "destroyed" | # Ship is destroyed during battle, but not yet sunk |
| SHIP_ENTITY_STATE_SINK | "sink" | # Ship is sinking after being destroyed during battle |
| SHIP_DAMAGE_LIGHT_THRESHOLD | 0.25 | # Damage ratio at which ship is considered lightly damaged |
| SHIP_DAMAGE_HEAVY_THRESHOLD | 0.6 | # Damage ratio at which ship is considered heavily damaged |
| SHIP_DAMAGE_DESTROYED_THRESHOLD | 1.0 | # Damage ratio at which ship is considered destroyed |
| SHIP_SCALE_GENERAL_FACTOR | 0.5 | # All ship entities at the diorama's expanded state are scaled with this factor |
| SHIP_MIN_SCALE | 0.2 | # Minimum scale for ship entities in fleet dioramas, e.g. ship scale at the diorama's shrunken state start |
| SHIP_MAIN_ENTITY_SCALE | 3.0 | # Scale for the main ship entity in fleet dioramas at the diorama's shrunken state |
| SHIP_ANIMATION_SPEED_EXPAND | 1.0 | # Speed multiplier for ship expanding animation when fleet diorama zooms in |
| SHIP_ANIMATION_SPEED_SHRINK | 2.0 | # Speed multiplier for ship shrinking animation when fleet diorama zooms out |
| SHIP_ANIMATION_SCALE_DURATION | 0.8 | # Duration in seconds of ship scaling animation when fleet diorama zooms in/out |
| SHIP_ANIMATION_ZOOM_STEP_EXPAND | 4 | # Zoom step at which fleet entities should play expanding animation, e.g. at zoom steps <= 6 |
| SHIP_ANIMATION_ZOOM_STEP_SHRINK | 5 | # Zoom step at which fleet entities should play shrinking animation, e.g. at zoom steps >= 8 |
| SHIP_ANIMATION_ROTATE_ON_MOVEMENT_PROGRESS | 0.5 | # Progress of ship movement (0.0 - 1.0) at which ship starts rotating towards the target direction |
| SHIP_ANIMATION_MOVE_ON_ROTATION_PROGRESS | 0.5 | # Progress of ship movement (0.0 - 1.0) at which ship starts rotating towards the target direction |
| SHIP_ANIMATION_MOVE_SPEED | 4.5 | # Speed multiplier for ship movement in fleet dioramas |
| SHIP_ANIMATION_ROTATE_SPEED | 1.5 | # Speed multiplier for ship rotation in fleet dioramas |
| SHIP_ANIMATION_DISTANCE_FOR_FULL_OPACITY | 5.0 | # Distance to the main ship at which ship entities are fully opaque |
| SHIP_ANIMATION_DISTANCE_FOR_FULL_SCALE | 1.5 | # Distance to the main ship at which ship entities are fully scaled |
| SHIP_ANIMATION_HEAVE_SPEED | 1.5 | # Speed of the heave animation for ship entities |
| SHIP_ANIMATION_HEAVE_AMPLITUDE | 0.04 | # Amplitude of the heave animation for ship entities |
| SHIP_STATE_FIRE_TIME_RANGE | { 10.0 20.0 } | # Range of time interval between fire animations |
| SHIP_STATE_FIRE_SHOT_TRAVEL_TIME | 0.2 | # Delay in seconds between a ship firing and the target receiving the hit/miss effect |
| SHIP_STATE_FIRE_TIME | 2.0 | # Duration in seconds of the shoot animation |
| SHIP_STATE_FIRE_IMPACT | 1.0 | # Base impact multiplier for the shoot animation intensity |
| SHIP_STATE_FIRE_ROLL_PEAK | 3.0 | # Peak roll angle in degrees for the shoot animation, scaled by impact |
| SHIP_STATE_FIRE_BUMP_PEAK | 0.2 | # Normalized time (0-1) at which the roll bump peaks during the shoot animation |
| SHIP_STATE_FIRE_HEAVE_AMPLITUDE | 0.02 | # Depth dip amplitude for the shoot heave animation, scaled by impact |
| SHIP_STATE_FIRE_HEAVE_PEAK | 0.15 | # Normalized time (0-1) at which the heave dip peaks during the shoot animation |
| SHIP_WEAPON_ENGAGE_SPEED | 45.0 | # Speed in degrees per second at which the ship's weapon engages |
| SHIP_IDLE_ROLL_AMPLITUDE | 2.0 | # Roll amplitude in degrees for idle ship animation |
| SHIP_IDLE_ROLL_SPEED | 1.2 | # Speed of the idle roll oscillation |
| SHIP_IDLE_HEAVE_AMPLITUDE | 0.04 | # Vertical heave amplitude for idle ship animation |
| SHIP_IDLE_HEAVE_SPEED | 1.5 | # Speed of the idle heave oscillation |
| SHIP_MOVE_PITCH_AMPLITUDE | 1.0 | # Pitch amplitude in degrees for move ship animation |
| SHIP_MOVE_PITCH_SPEED | 1.0 | # Speed of the move pitch oscillation |
| SHIP_MOVE_ROLL_AMPLITUDE | 4.0 | # Roll amplitude in degrees for move ship animation |
| SHIP_MOVE_ROLL_SPEED | 1.2 | # Speed of the move roll oscillation |
| SHIP_MOVE_HEAVE_AMPLITUDE | 0.06 | # Vertical heave amplitude for move ship animation |
| SHIP_MOVE_HEAVE_SPEED | 1.5 | # Speed of the move heave oscillation |
| BATTLE_DIORAMA_CIRCLING_TIME_RANGE | { 3.0 5.0 } | # Range of random time in seconds that ships spend circling around |
| BATTLE_DIORAMA_CRUISING_ANGLE | 45.0 | # How long in angle degrees ships cruise in the diorama |
| BATTLE_DIORAMA_SINKING_ANGLE | 90.0 | # Angle offset in degrees for calculating defeat target position (half circle for smooth approach) |
| BATTLE_DIORAMA_SINK_ON_DEFEAT_PROGRESS | 0.75 | # Progress of the defeat state (0.0 - 1.0f) at which ship starts to sink |
| BATTLE_DIORAMA_SINK_TIME | 5.0 | # Time in seconds it takes for ship entities to sink in naval battle diorama after they are defeated |
| BATTLE_DIORAMA_SINK_ROLL_TARGET | 120.0 | # Target roll angle in degrees for sinking animation in naval battle diorama |
| BATTLE_DIORAMA_SINK_DEPTH_TARGET | 0.0 | # Target depth to which Y-coordinate of ship entities should sink in naval battle diorama |
| BATTLE_DIORAMA_DESTOY_TIME | 4.0 | # Time it takes for ship entities to be destroyed after sinking in naval battle diorama |
| BATTLE_DIORAMA_DESTOY_DEPTH_TARGET | 1.0 | # Target depth to which Y-coordinate of ship entities should sink in naval battle diorama |
| BATTLE_DIORAMA_CURVE_B1_MULT | 0.4 | # Multiplier for the B1 curve parameter used for ship movement animation in naval battle dioramas, which defines the curvature of the movement path |
| BATTLE_DIORAMA_CURVE_B2_MULT | 0.3 | # Multiplier for the B2 curve parameter used for ship movement animation in naval battle dioramas, which defines the curvature of the movement path |
| BATTLE_DIORAMA_SHIP_ANGULAR_SPEED | 0.1 | # Speed multiplier for ship rotation during naval battle diorama animations |
| BATTLE_DIORAMA_SHIP_SCALE | 1.0 | # Scale for ship entities during naval battle diorama animations |
| BATTLE_DIORAMA_RADIUS_DEFAULT | 10.0 | # Default radius of the circle on which ships are positioned, in other words distance from the center of the diorama |
| BATTLE_DIORAMA_RADIUS_RATIO_OUTER | 1.2 | # Ratio for the outer radius of the circle on which ships are positioned |
| BATTLE_DIORAMA_RADIUS_RATIO_INNER | 0.7 | # Ratio for the inner radius of the circle on which ships are positioned |
| BATTLE_DIORAMA_RADIUS_RATIO_DEFEAT | 0.3 | # Ratio for the defeat radius - ships move to this reduced radius when defeated |
| BATTLE_DIORAMA_RETREAT_ANGLE_DELTA | 45.0 | # How long in angle degrees ships retreat in the diorama |
| BATTLE_DIORAMA_RETREAT_RADIUS_RATIO | 2.0 | # Ratio for the retreat radius - ships move to this outer radius when retreating |
| BATTLE_DIORAMA_LENGTH_PER_SHIP | 3.0 | # Length of a ship which is used to locate ships the circle to avoid intersections |
| BATTLE_DIORAMA_ANGLE_PER_SIDE | 120.0 | # Angle in degrees that each battle side occupies in the diorama |
| BATTLE_DIORAMA_ROTATION_BLEND_SPEED | 6.0 | # Speed of rotation blending when transitioning between circling and cruising states. Higher = snappier, lower = smoother |
| BATTLE_DIORAMA_TERRAIN_OPACITY_BLEND_SPEED | 2.0 | # Speed at which terrain opacity blends when showing/hiding battle diorama entities |
| BATTLE_DIORAMA_DITHER_DURATION | 3 | # For how many seconds we show diorama entities after the battle is over |
| BATTLE_DIORAMA_ROUTE_ENTITY_FADE_RANGE | 3.5 | # Distance in world units beyond the diorama radius over which route entity ships fade out when near a naval battle diorama |
| SHIP_LENGTH_DEFAULT | 3.0 | # Default length of a ship, used for calculating spacing between ships in route graphics |
| ROUTE_SHIPS_MAX | 10 | # Max number of ship graphics that can be visible on map routes for one fleet |
| ROUTE_SHIPS_INTERVAL | 2.0 | # Interval between ship graphics on map routes |
| ROUTE_SHIPS_INTERVAL_RANDOM | 1.0 | # Random variation added to the interval between ship graphics on map routes |
| SHIP_PROPULSION_LEVEL_PARAMETER | "propulsion_level" | # Name of the sound parameter that is attached to the ship base entity for the propulsion sound |
| SHIP_PROPULSION_MODIFICATION_SLOT | "ship_mod_slot_propulsion" | # Name of the propulsion modification slot on the ship entity, which is used to determine the propulsion level of the ship and set the sound parameter accordingly |

### ShipViewer

| Define | Default Value | Dev Comment |  |
|---|---|---|---|
| AUDIO_DISTANCE_SCALE_FACTOR | 0.6 | # The distance between the camera and the entity is multiplied by this factor for calculating the distance-based audio attenuation for the listener. The lower this is the closer the listener is to the look-at position |  |
| CAMERA_PITCH_RANGE | { 20.0 45.0 } | # In degrees |  |
| CAMERA_DISTANCE_RANGE | { 15.0 75.0 } |  |  |
| CAMERA_START_LOOK_AT | { 0.0 2.75 0.0 } |  |  |
| CAMERA_START_YAW | -145.0 | # in degrees |  |
| CAMERA_START_PITCH | 24.35 | # in degrees |  |
| CAMERA_START_DISTANCE | 45.0 |  |  |
| CAMERA_ROTATION_SPEED | 0.001 |  |  |
| CAMERA_ROTATION_DAMPING | 15.0 |  |  |
| CAMERA_ZOOM_SPEED | 2.0 |  |  |
| CAMERA_ZOOM_DAMPING | 12.0 |  |  |
| CAMERA_PAN_SPEED | 0.01 |  |  |
| CAMERA_PAN_RANGE | { 2.5 1.5 2.5 } | # Max distance from the starting offset { X, Y, Z } |  |
| CAMERA_RESET_TIME | 0.2 | # Time it takes for the camera to return to default position |  |
| WATER_ENTITY | "ship_viewer_water_entity" |  |  |
| WATER_ENTITY_SPEED_DEFAULT | 17.0 | # Default speed for water animation in ship viewer, i.e. ships with this speed have visual speed | 1.0 |
| BATTLE_VIEWPORT_CAMERA_ATTACKER_YAW | -31.0 | # The yaw of the camera in the attacker viewport in degrees |  |
| BATTLE_VIEWPORT_CAMERA_DEFENDER_YAW | 149.9 | # The yaw of the camera in the defender viewport in degrees |  |
| BATTLE_VIEWPORT_CAMERA_PITCH | 40.0 | # The pitch of the camera in both battle viewports in degrees |  |
| BATTLE_VIEWPORT_CAMERA_DISTANCE | 74.0 | # The distance of the camera to the ships in both battle viewports |  |
| BATTLE_VIEWPORT_CAMERA_ATTACKER_TRANSLATION | { 2.0 0.0 -2.0 } | # The amount to translate the camera target by in the attacker viewport |  |
| BATTLE_VIEWPORT_CAMERA_DEFENDER_TRANSLATION | { -0.5 0.0 2.5 } | # The amount to translate the camera target by in the defender viewport |  |

## 00_interfaces

### Lenses

| Define | Default Value | Dev Comment |
|---|---|---|
| MAP_MARKER_ZOOM_THRESHHOLD_NEAR | 100 |  |
| MAP_MARKER_ZOOM_THRESHHOLD_FAR | 900 |  |
| MAP_MARKER_ZOOM_THRESHHOLD_MAX | 4000 |  |
| MAP_MARKER_ZOOM_CITIES_ALL_THRESHHOLD | 70 |  |
| MAP_MARKER_ZOOM_CITIES_REGION_CAPITALS_THRESHHOLD | 250 |  |
| MAP_MARKER_ZOOM_CITIES_STATE_CAPITALS_THRESHHOLD | 500 |  |
| MAP_MARKER_HEIGHT_OFFSET | 1.6 | # Move Map Markers "up" in 3D space |
| LINE_HEIGHT_OFFSET | 0.0 | # Potentially move the Lines up the same amount, right now they go to exactly to the ground |
| NUM_CONSTRUCTIONS_BEFORE_SUMMARY | 1 |  |

### Trend

| Define | Default Value | Dev Comment |
|---|---|---|
| SMALL_ARROW_RELATIVE_THRESHOLD | 0.001 | # [0..1] relative changes less than this will not have a small arrow |
| BIG_ARROW_RELATIVE_THRESHOLD | 0.005 | # [0..1] relative changes less than this will not have a big arrow |

### Saves

| Define | Default Value | Dev Comment |
|---|---|---|
| EXIT_SAVE_NAME | "autosave_exit" |  |

### GUI

**Note**: this category is split into several sections in the file, rather than one contiguous section.

| Define | Default Value | Dev Comment |
|---|---|---|
| ANCHORED_TOOLTIP_THRESHOLD | 150 |  |
| TABS | 4 | # Number of spaces for tabs in ui |
| NUM_INDENTS | 3 |  |
| MAX_BREAKDOWN_ITEMS | 10 |  |
| MAX_BREAKDOWN_ITEMS_SHORT_LIST | 5 |  |
| MAX_LENGTH_OF_ENTERED_TEXT | 50 | # The max allowed text length when checking for validity |
| MAX_CONSTRUCTION_BREAKDOWN_ITEMS | 24 |  |
| MAX_PAGES_IN_PAGED_LIST | 10 |  |
| MAX_CURRENTLY_CONSTRUCTING_ELEMENTS_SHOWN | 10 | # active construction queue elements widget is capped to this number of items |
| TUTORIAL_STEP_INSTRUCTION_BUTTON_ID | "next" |  |
| DISMISS_TOAST_SHORTCUT_ACTION | "dismiss_toast" |  |
| CLOSE_WINDOW_SHORTCUT_ACTION | "close_window" |  |
| CENTER_CAPITAL_SHORTCUT_ACTION | "center_capital" |  |
| LESS_THAN_PERCENTAGE_COLLECT_AS_OTHER | 0.05 | # In long lists, make items that with less than 5% appear under a special "Other" item at the end of the list (Pop Types and IG support atm) |
| CONSTRUCTION_QUEUE_MAX_SHOWN_ELEMENTS | 12 |  |
| MAX_SUBJECTS_SHOWN_IN_TOOLTIP | 5 |  |
| PROMINENT_IG_REQUIRED_MEMBERSHIP | 0.1 | # In order to be displayed as a prominent Interest Group in Pop details, at least this fraction of the politically engaged population must support the IG |
| IG_MEMBER_ATTRACTION_SAMPLES | 100 | # The max number of supporting Pops that will be sampled (in order of membership size) to determine the reasons they're attracted to this IG |
| MIN_FRACTION_BELOW_EXPECTED_SOL_TO_SHOW | 0.01 |  |
| MIN_FRACTION_WELFARE_TO_SHOW | 0.01 |  |
| LENS_TOOLBAR_ITEM_WIDTH | 100 | # The width of each item in the Lens Toolbar |
| LENS_TOOLBAR_MARGIN_LEFT | 53 | # The width of the side panel |
| SCROLLBAR_WIDTH | 8 | # The width of the scroll bar |
| LENS_TOOLBAR_MARGIN_RIGHT | 45; | # LENS_TOOLBAR_MARGIN_LEFT - SCROLLBAR_WIDTH |
| RADICALS_LOYALISTS_BREAKDOWN_NUM_ITEMS | 3 | # How many numbers to show in the breakdown for Radicals/Loyalists before collecting the rest as "other" |
| POP_NEEDS_SUMMARY_ITEMS | 3 | # How many items from the Pop Needs tooltip to show one level above the breakdown |
| RADICALS_LOYALISTS_SUMMARY_ITEMS | 2 |  |
| MIN_LOYALTY_CHART_FRACTION | 0.01; | # A non-zero loyalty fraction below this value will still appear as this value in the loyalty pie chart |
| STATE_OWNER_PIECHART_ALPHA | 0.5; |  |
| MIN_TRADE_QUANTITY_TO_SHOW | 0.1 | # Exporters/importers to a state/market with less volume than this are consolidated into 'additional exports/imports' |
| TREATY_GOODS_ARTICLE_DEFAULT_QUANTITY | 0.25 | # Used for predicting acceptance of goods transfer articles, when a good is selected the quantity is also set to this (as a multiplier of max, clamped by min) |
| PLACEHOLDER_ICON | "gfx/interface/icons/war_goals/unused/placeholder.dds" |  |
| STRAIT_ACCESS_OPEN_ICON | "gfx/interface/icons/straits_icons/straits_access.dds" |  |
| STRAIT_ACCESS_NO_MILITARY_ICON | "gfx/interface/icons/straits_icons/straits_no_military.dds" |  |
| STRAIT_ACCESS_CLOSED_ICON | "gfx/interface/icons/straits_icons/straits_no_access.dds" |  |
| STRAIT_TOLL_NO_TOLLS_ICON | "gfx/interface/icons/straits_icons/straits_no_tolls.dds" |  |
| STRAIT_TOLL_LOW_ICON | "gfx/interface/budget/budget_set_very_low.dds" |  |
| STRAIT_TOLL_MEDIUM_ICON | "gfx/interface/budget/budget_set_medium.dds" |  |
| STRAIT_TOLL_HIGH_ICON | "gfx/interface/budget/budget_set_very_high.dds" |  |
| STRAIT_ALLOWED_NO_ENEMIES_ICON | "gfx/interface/icons/generic_icons/capitulate.dds" |  |
| STRAIT_ALLOWED_ONLY_ALLIES_ICON | "gfx/interface/icons/lens_toolbar_icons/alliance.dds" |  |
| NO_STARVATION_ICON | "gfx/interface/icons/map_mode_icons/harvest_conditions.dds" |  |
| MILD_STARVATION_ICON | "gfx/interface/icons/famine_icons/mild_starvation.dds" |  |
| SEVERE_STARVATION_ICON | "gfx/interface/icons/famine_icons/severe_starvation.dds" |  |
| # Colors for the starvation pie chart which contains population ratios in different starvation types: no, mild, severe |  |  |
| NO_STARVATION_COLOR | { 0.7 0.7 0.7 1 } |  |
| MILD_STARVATION_COLOR | { 0.741 0.404 0.082 1 } | # Orange |
| SEVERE_STARVATION_COLOR | { 0.69 0.08 0.06 1 } | # Red |
| ALERT_COLOR_GREEN | { 0.54 0.78 0.33 1 } | # Green |
| ALERT_COLOR_YELLOW | { 0.97 0.77 0.33 1 } | # Yellow |
| ALERT_COLOR_RED | { 0.78 0.25 0.25 1 } | # Red |
| MESSAGE_COLOR_GOOD | { 0.54 0.78 0.33 1 } | # Green |
| MESSAGE_COLOR_NEUTRAL | { 1 1 1 1 } | # Yellow |
| MESSAGE_COLOR_BAD | { 0.78 0.25 0.25 1 } | # Red |
| MILITARY_COLOR_YOU | { 0.11 0.46 0.05 1 } | # Green |
| MILITARY_COLOR_ALLY | { 0 0.2 0.5 1 } | # Blue |
| MILITARY_COLOR_ENEMY | { 0.5 0.04 0.02 1 } | # Red |
| MILITARY_COLOR_NEUTRAL | { 0.5 0.5 0.5 1 } | # Gray |
| NAVAL_MISSION_HIGHLIGHT_FRIENDLY_COLOR | { 0.47 0.88 1.0 1 } | # Blue - highlight for sea regions where friendly fleets are on a naval mission (matches the round_highlight_blue marker highlight) |
| NAVAL_MISSION_HIGHLIGHT_ENEMY_COLOR | { 1.0 0.30 0.30 1 } | # Red - highlight for sea regions where enemy fleets are on a naval mission |
| BIG_SWAY_VALUE | 100 | # The score adjustment the AI could possibly get for a generous sway, for coloring the numeric preference values in Diplomatic Play popup |
| LIBERTY_DESIRE_TREND_INDICATOR_LIMIT | 0.05 |  |
| BUILDING_CONSIDERED_FULLY_EMPLOYED | 0.95 | # Hide Employment bar for Building if more than 95% employed |
| OUTLINER_ENTRY_DOUBLE_CLICK_TIME | 0.5 | # Time in seconds before we allow the interpretation of the second left click as a close of the panel. This is unfortunately not synced with OS/platform double click setting used for the creation of the doubleclick event, but 0.5 s should work for the vast majority of people even when they have a different doubleclick time. |
| # these values need to correspond with the atlas defined in coat_of_arms/options |  |  |
| FLAG_FRAME_WIDTH_LARGE | 384 |  |
| FLAG_FRAME_HEIGHT_LARGE | 256 |  |
| FLAG_FRAME_WIDTH_MEDIUM | 96 |  |
| FLAG_FRAME_HEIGHT_MEDIUM | 64 |  |
| FLAG_FRAME_WIDTH_SMALL | 48 |  |
| FLAG_FRAME_HEIGHT_SMALL | 32 |  |
| FLAG_FRAME_WIDTH_MESH_ATLAS | 192 | # Atlas used for mesh flags only |
| FLAG_FRAME_HEIGHT_MESH_ATLAS | 128 | # Atlas used for mesh flags only |
| # Power Bloc CoAs are squares |  |  |
| POWER_BLOC_COA_FRAME_VERY_LARGE | 512 |  |
| POWER_BLOC_COA_FRAME_LARGE | 256 |  |
| POWER_BLOC_COA_FRAME_MEDIUM | 128 |  |
| POWER_BLOC_COA_FRAME_SMALL | 50 |  |
| POWER_BLOC_COA_FRAME_VERY_SMALL | 32 |  |
| TECH_TREE_PRODUCTION_INITIAL_POSITION | { -600 30 } |  |
| TECH_TREE_MILITARY_INITIAL_POSITION | { 150 30 } |  |
| TECH_TREE_SOCIETY_INITIAL_POSITION | { -400 30 } |  |
| TECH_TREE_INITIAL_ZOOM | 0.3 |  |
| TECH_TREE_MAX_UNLOCK_DISPLAY_COUNT | 5 |  |
| TECH_TREE_MODIFIER_UNLOCK_ICON | "gfx/interface/tech_tree/modifiers_generic_icon.dds" |  |
| TECH_TREE_RESEARCH_QUEUE_DISPLAY_COUNT | 5 |  |
| SWAY_OFFER_DEFAULT_ICON | "gfx/interface/icons/sways/obligation.dds" |  |
| SWAY_OFFER_OBLIGATION_ICON | "gfx/interface/icons/sways/obligation.dds" |  |
| SWAY_OFFER_WARGOAL_ICON | "gfx/interface/icons/sways/wargoal.dds" |  |
| SWAY_OFFER_ALLY_ICON | "gfx/interface/icons/sways/call_ally.dds" |  |
| SWAY_OFFER_BECOME_SUBJECT_ICON | "gfx/interface/icons/sways/subject.dds" |  |
| SWAY_OFFER_TRANSFER_SUBJECT_ICON | "gfx/interface/icons/sways/subject.dds" |  |
| SWAY_OFFER_TRANSFER_STATE_ICON | "gfx/interface/icons/sways/state.dds" |  |
| SWAY_OFFER_DIPLOMATIC_PACT_ICON | "gfx/interface/icons/sways/diplomatic_pact.dds" |  |
| DRAG_SENSITIVITY | 0.01 | # this value is in terms of pixels/resolution, i.e. a value of 1 means the whole length of the screen # a larger value means that a larger movement is allowed during a click |
| MESSAGE_FEED_DELAY | 1 | # Number of seconds between the feed systems wait before adding another message if there's a queue |
| MESSAGE_FEED_MAX_SHOWN | 10 | # Maximum number of messages shown simultaneously in the feed |
| MESSAGE_FEED_NUMBER_OF_DAYS_SHOWN | 14 | # Number of days we show the Notifications in the feed, needs to be lower than DEAD_OBJ_UNDESTROYED_DAYS in order to not risk notifications regarding dead people etc returning null_objs. |
| MESSAGE_FEED_DELETE_NOTIFICATION_ADVANCE | 0 | # Number of days that a notification message will be marked to be deleted in advance of the notification being deleted in order to make time for message feed animations |
| TOAST_MESSAGE_TIME_SHOWN | 11.0 | # Duration in seconds for how long to show a toast. Use < 0 to require manual dismissal. |
| TOAST_MESSAGE_POST_HOVER_DELAY | 1.0 | # When a message is hovered it doesn't disappear, but the above timeout still runs. When leaving with the mouse and the time has run out, leave the message on the screen for TOAST_MESSAGE_POST_HOVER_DELAY seconds. |
| MAP_TOOLTIP_MOUSE_OFFSET | { 20 20 } |  |
| TIME_INTERVAL_BETWEEN_MAP_NOTIFICATIONS | 4.5 | # Delay when a notification is blocked by being too close to another one |
| DISTANCE_BETWEEN_MAP_NOTIFICATIONS | 25 | # Min distance between notifications to avoid their intersections |
| MAP_NOTIFICATIONS_MAX_ZOOM | 200 | # Max camera height to show on-map notifications unless otherwise specified in the map notification database |
| JOURNAL_ENTRY_ICON_DEFAULT | "gfx/interface/icons/event_icons/event_default.dds" | # Default icon for Journal Entries (journal and outliner) |
| SITUATION_EVENT_ICON_DEFAULT | "gfx/interface/icons/event_icons/event_default.dds" | # Default icon for Situation Events (map marker and outliner) |
| LAND_BATTLE_ICON | "gfx/interface/map_markers/battle_icon.dds" | # Icon for Land Battle map markers |
| NAVAL_BATTLE_ICON | "gfx/interface/map_markers/naval_battle_icon.dds" | # Icon for Naval Battle map markers |
| SOL_MODIFIER_POSITIVE | "gfx/interface/icons/timed_modifier_icons/modifier_flag_positive.dds" | # Icon for dynamically generated standard of living modifier for cultures/religion, positive version |
| SOL_MODIFIER_NEGATIVE | "gfx/interface/icons/timed_modifier_icons/modifier_flag_negative.dds" | # Icon for dynamically generated standard of living modifier for cultures/religion, negative version |
| NUMBER_OF_POP_PORTRAITS_STATE | 3 | # Number of pops sampled from all the pops on a state |
| NUMBER_OF_POP_PORTRAITS_BUILDING | 3 | # Number of pops sampled from all the pops on a building |
| GAME_CONCEPT_ICON_DEFAULT | "gfx/interface/icons/generic_icons/generic_concept_icon.dds" | # Default icon for Game Concepts |
| # These dictate how the options in the map list panels that appear when a map interaction is active are sorted. #Lower numbers are sorted on top of higher numbers. The minimum is 0. Multiple entries can have the same sort order |  |  |
| MAP_LIST_PANEL_INTERACTION_SORT_ORDER_CAN_ACTIVATE | 0 |  |
| MAP_LIST_PANEL_INTERACTION_SORT_ORDER_CAN_ACTIVATE_MORE | 0 |  |
| MAP_LIST_PANEL_INTERACTION_SORT_ORDER_CAN_DEACTIVATE | 1 |  |
| MAP_LIST_PANEL_INTERACTION_SORT_ORDER_CANNOT_ACTIVATE | 2 |  |
| MAP_LIST_PANEL_INTERACTION_SORT_ORDER_CANNOT_DEACTIVATE | 3 |  |
| MAP_LIST_PANEL_INTERACTION_SORT_ORDER_DOES_NOT_APPLY | 4 |  |
| NUM_RANKING_LEADERBOARD_ITEMS | 10 |  |
| POP_LIST_POPS_SHOWN_PER_TYPE | 256 |  |
| NUM_TOP_CONSUMPTION_GOODS_SHOWN | 5 |  |
| NUM_TOP_ASSETS_SHOWN_LONG | 6 |  |
| NUM_TOP_ASSETS_SHOWN_SHORT | 3 |  |
| NUM_TOP_OWNERS_SHOWN_LONG | 8 |  |
| NUM_TOP_OWNERS_SHOWN_SHORT | 5 |  |
| POLITICAL_MOVEMENT_SUPPORTING_AGITATORS_TOP_DATAMODEL_COUNT | 2 |  |
| ARMY_FORMATION_FLAG_COLOR_PREFIX | "army_color_" |  |
| FLEET_FORMATION_FLAG_COLOR_PREFIX | "fleet_color_" |  |
| BUILDING_OWNERSHIP_COLOR_PLAYER_GOVERNMENT | { 0.20 0.40 0.90 1 } |  |
| BUILDING_OWNERSHIP_COLOR_PLAYER_POPS | { 0.41 0.67 0.74 1 } |  |
| BUILDING_OWNERSHIP_COLOR_PLAYER_COMPANY | { 0.41 0.67 0.74 1 } |  |
| BUILDING_OWNERSHIP_COLOR_NON_PLAYER_COMPANY | { 1 0.674 0.454 1 } |  |
| BUILDING_OWNERSHIP_COLOR_LOCAL_NON_PLAYER_GOVERNMENT | { 0.9 0.50 0.2 1 } |  |
| BUILDING_OWNERSHIP_COLOR_LOCAL_NON_PLAYER_POPS | { 1 0.674 0.454 1 } |  |
| BUILDING_OWNERSHIP_COLOR_OTHER_COUNTRIES_GOVERNMENT | { 0.9 0.50 0.2 1 } |  |
| BUILDING_OWNERSHIP_COLOR_OTHER_COUNTRIES_POPS | { 1 0.674 0.454 1 } |  |
| OUTLINER_NUM_VISIBLE_NONEXPANDABLE_SUBENTRIES | 1 | # Num outliner entries that can be visible when the parent entry is not expanded |
| SOCIETY_PANEL_DESIRED_REPRESENTATIVE_POPS | 3 | # Try to get this many pop portraits (not possible if there are only 1 or 2 pops...) |
| # Thresholds for when the corresponding loc keys are used. If remaining duration >= defined value, we use that key # Below VERY_LOW we use the LOWEST loc key # VERY HIGH is set to 999 essentially as an unused threshold in case we need more in the future, it still works the same though # Values are in number of days |  |  |
| HARVEST_CONDITION_DURATION_LABEL_VERY_LOW | 60 |  |
| HARVEST_CONDITION_DURATION_LABEL_LOW | 120 |  |
| HARVEST_CONDITION_DURATION_LABEL_MODERATE | 240 |  |
| HARVEST_CONDITION_DURATION_LABEL_HIGH | 480 |  |
| HARVEST_CONDITION_DURATION_LABEL_VERY_HIGH | 999 |  |
| COMPANY_TYPE_ICON_FONT | 230 |  |
| COMPANY_TYPE_ICON_OFFSET | { 0 40 } |  |
| MILITARY_FORMATION_FLAG_ICON_FONT | 95 |  |
| MILITARY_FORMATION_FLAG_ICON_OFFSET | { 0 30 } |  |
| IDEOLOGY_ICON_FONT | 230 |  |
| IDEOLOGY_ICON_OFFSET | { 0 40 } |  |
| ARTICLE_TYPE_ICON_FONT | 90 |  |
| ARTICLE_TYPE_ICON_OFFSET | { 0 20 } |  |
| WAR_GOAL_TYPE_ICON_FONT | 120 |  |
| WAR_GOAL_TYPE_ICON_OFFSET | { 0 32 } |  |
| NAVAL_BATTLE_CONDITION_TYPE_ICON_FONT | 120 |  |
| NAVAL_BATTLE_CONDITION_TYPE_ICON_OFFSET | { 0 64 } |  |
| RELIGION_ICON_FONT | 180 |  |
| RELIGION_ICON_OFFSET | { 0 60 } |  |
| INTEREST_TIER_TYPE_SMALL_ICON_FONT | 50 |  |
| INTEREST_TIER_TYPE_SMALL_ICON_OFFSET | { 0 12 } |  |
| INTEREST_TIER_TYPE_ICON_FONT | 90 |  |
| INTEREST_TIER_TYPE_ICON_OFFSET | { 0 20 } |  |
| AI_STRATEGIC_REGION_STANCE_TYPE_ICON_FONT | 230 |  |
| AI_STRATEGIC_REGION_STANCE_TYPE_ICON_OFFSET | { 0 40 } |  |
| SHIP_VETERANCY_LEVEL_ICON_FONT | 40 |  |
| SHIP_VETERANCY_LEVEL_ICON_OFFSET | { 0 10 } |  |

## 00_shaders

### ShadersCommon

| Define | Default Value | Dev Comment |
|---|---|---|
| PARALLAX_HEIGHT | 8 | # Height of parallax effects |

### MapCoa

| Define | Default Value | Dev Comment |
|---|---|---|
| ANGLE | 0.0 | # Rotation of the coat of arms on the map. In radians |
| SIZE | 25.0 | # Size of one CoA on the map. In world-units |
| SIZE_FLATMAP | 50.0 |  |
| BLEND | 0.65f | # Minimum blend value. Final blend value will be the minimum of this and whatever the gradient borders use |
| BLEND_FLATMAP | 0.8f |  |
| BLEND_STRIPES | 0.8f | # Blend/Opacity of occupation stripes |
| BLEND_STRIPES_FLATMAP | 1.0f |  |
| ROW_HORIZONTAL_OFFSET | 0.25 | # Each row of coat of arms can be offset horizontally. This controls by how much in percentages |
| ROW_COUNT | 4 | # How many rows to offset before starting over with an offset of 0s |
| STRIPE_SCALE | 1.0 | # Scale of occupation stripes |
| STRIPE_SCALE_FLATMAP | 1.0 |  |

### MapmodeStripes

| Define | Default Value | Dev Comment |
|---|---|---|
| STRIPE_ROTATION | -2.0 | # Rotation of the stripes ( Technically a sheer of the UVs, so it affects the width as well ) |
| STRIPE_TILING | 120.0 | # Tiling of the stripes |
| STRIPE_WIDTH | 0.2 | # Width of the stripes |
| STRIPE_EDGE_WIDTH | 0.075 | # Width of stripe edges |
| STRIPE_EDGE_COLOR | 0.75 | # Color multiplier of the stripe edges ( 1.0 = same color as stripe, 0.0 = black ) |
| STRIPE_HEIGHT_STEPS | 1200.0f | # The stripe tiling will start from this height and halve every time the height doubles ( Avoid starting lower than the flatmap height ) |

### EdgeOfWorld

| Define | Default Value | Dev Comment |
|---|---|---|
| # Cloudfield at the edge of map top/bottom # For papermap table bokehfield, see shader file |  |  |
| BASETILE | 20.0f |  |
| BASESCROLL | { 0.0055 0.00325 } |  |
| BASESTRENGTH | 1.0f |  |
| BASEPOSITION | 0.728 |  |
| BASECONTRAST | 1.08 |  |
| CLOUD1TILE | 2.0 |  |
| CLOUD1SCROLL | { 0.0015 -0.0015 } |  |
| CLOUD1STRENGTH | 1.0 |  |
| CLOUD1POSITION | 0.538 |  |
| CLOUD1CONTRAST | 1.0 |  |
| CLOUD2TILE | 3.0 |  |
| CLOUD2SCROLL | { -0.0075 0.00055 } |  |
| CLOUD2STRENGTH | 1.0 |  |
| CLOUD2POSITION | 0.158 |  |
| CLOUD2CONTRAST | 1.202 |  |
| HIGHCLOUDCOLOR | { 0.8 0.8 1.0 1.0 } |  |
| LOWCLOUDCOLOR | { 0.03 0.03 0.03 1.0 } |  |
| COLORMULTIPLY | 0.015 |  |
| FADEDISTANCE | 50 |  |

### GuiFlag

| Define | Default Value | Dev Comment |
|---|---|---|
| SMALL_WAVE_SCALE | 7.0 |  |
| WAVE_SCALE | 0.95 |  |
| ANIMATION_SPEED | 0.9 |  |

## References

Modding
Return to top
| Documentation | Defines • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| Map | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • [States](State modding.md) |
|---|---|

| Interface | [Interface](Interface modding.md) • [GUI script](GUI script.md) • [Localization](Localization.md) • [Customizable localization](Localization.md) • [Script localization](Script localization.md) |
|---|---|

| Graphics | [3D Models](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|

| Audio | Music • [Sound](Sound modding.md) |
|---|---|

| Other | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| Guides | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|
