---
title: Patch 1.5.X
source: https://vic3.paradoxwikis.com/Patch_1.5.X
pageid: 5491
categories: [Patches]
fetched: 2026-10-27
---
Victoria 3
Version history
The Great Wave
1.13
•
1.13.1
•
1.13.2
•
1.13.3
1.13.4
•
1.13.5
•
1.13.6
•
1.13.7
1.13.8
•
1.13.9
•
1.13.10
•
1.13.11
Iberian Twilight
1.12
•
1.12.1
•
1.12.2
1.12.3
•
1.12.4
•
1.12.5
National Awakening
1.11
•
1.11.1
1.10
•
1.10.1
•
1.10.2
•
1.10.3
1.10.4
•
1.10.5
•
1.10.6
Charters of Commerce
1.9
•
1.9.1
•
1.9.2
•
1.9.3
•
1.9.4
1.9.5
•
1.9.6
•
1.9.7
•
1.9.8
Pivot of Empire
1.8
•
1.8.1
•
1.8.2
•
1.8.3
1.8.4
•
1.8.6
•
1.8.7
Sphere of Influence
1.7
•
1.7.1
•
1.7.2
•
1.7.3
1.7.4
•
1.7.5
•
1.7.6
•
1.7.7
Colossus of the South
1.6
•
1.6.1
•
1.6.2
1.5
•
1.5.8
•
1.5.9
•
1.5.10
1.5.11
•
1.5.12
•
1.5.13
Voice of the People
1.4
•
1.4.1
•
1.4.2
1.3
•
1.3.1
•
1.3.2
•
1.3.3
•
1.3.5
•
1.3.6
Base game
1.2
•
1.2.7
1.1
•
1.1.1
•
1.1.2
1.0.3
•
1.0.4
•
1.0.5
•
1.0.6
**Patch 1.5.X** are all patches beginning with 1.5.

## 1.5

Main article:
Patch 1.5
The main 1.5 patch had the version number 1.5.7, because earlier patches were released as an open beta.

## 1.5.8

Patch 1.5.8 was released on 2023-11-16[1] with checksum *064f*.

### Bugfixes

- Fixed a crash in CCombatUnit::GetModifierValueImpl
- Fixed a crash in the military formations manager
- Fixed a bug that would sometimes cause Transfer Subject war goals to not resolve as promised when a peace is signed or when a party gives in during a Diplomatic Play
- Imposing laws on your subjects now forces them to start enactment of that law as intended
- The Country panel's Domestic tab UI will no longer break when that country is in the process of enacting a law
- Fixed bug that prevented Quechua and South Andean subjects from being annexed
- Fixed a bug where military flags weren't visible if the Voice of The People DLC was not enabled

### Interface

- Added a player-configurable toggle for which Workforce number to show in the Expand Building Map Interaction (Jobseekers / Peasants / Unemployed)

### Modding

- Added a start_enactment effect
- Added an on_action for on_impose_law that will be overridden by on_impose if specified on the law type

## 1.5.9

Patch 1.5.9 was released on 2023-11-17[2] with checksum *08c8*.

### Bugfixes

- Fixed a crash that happened during formation calculations.

### Performance

- Disabled AI convoy raiding temporarily as a short-term fix for a critical performance issue that could stall the game. A proper fix is in progress and will be deployed ASAP.

## 1.5.10

Patch 1.5.10 was released on 2023-11-29[3] with checksum *608a*.

### Improvements

- Convoy Raiding mechanics have been rewritten to operate on a sea-node-per-sea-node basis, triggering intermittent attacks on convoys from local raiders, which is reduced by fleets defending convoys in that node
- Military Formations can now start moving away from a front even if some of their units are in battle
- Your and your allies' formations can now borrow/lend troops from one another even for offensives if the "Allow borrowing and lending troops" toggle is set under Formation Settings
- Pops that get paid dividends or have investment losses will now be more or less satisfied with their jobs accordingly
- Disband Formation button with an informative tooltip of what will happen to Commanders and Units in the formation when disbanded
- Peasants will no longer feel satisfied with their job just because the aristocrats and clergy that own their lands are paid on average more than the rest of the country, as a consequence peasants are now more likely to go work somewhere else
- Buildings that fail to hire will now adjust down their hiring target and attempt to hire a smaller number of people next week (down to a minimum), while buildings that successfully hire will raise their targets instead (up to a maximum). This should address the cases where limited market sell/buy orders would make a building at 10% employment not hire because it would be unprofitable at 20%, even though there is a shortage of the goods it produces and it would still be very profitable at 15%.
- Added a button to voluntarily cancel a Naval Invasion in progress for the invading player on the Naval Invasion panel
- Defeated Admirals are no longer fully ready to return to battle as soon as they arrive at their home HQ, but require at least 50% manpower before they can set sail again
- Job satisfaction term for pops feeling overqualified has been reduced
- Job satisfaction term for pops comparing the wage rate in their building with the national wage rate has been reduced
- Added a new journal entry to China, covering foreign missionary activities
- The Feminism technology will now change the stances of Liberal and Egalitarian Interest Groups on women's rights
- Buildings now fire a smaller number of people each time it does layoffs, but will do more frequent layoffs instead.
- Colonies no longer grow if the State is occupied or has any occupation progress by an enemy
- Extra Supplies and Luxurious Supplies mobilization options now also increase the overall goods consumption of units but grant them stronger combat bonuses
- Establishing and disbanding companies now have a cooldown; a recently established company cannot be immediately disbanded and a recently disbanded one cannot be reestablished right away
- Added entity visualization for off-road travel for armies
- Input Good Shortages in military buildings now affect Formation Supply
- Liberate Country wargoal is now considered contested if all the states that it would release are occupied by the holder or their allies
- Regular battalions under Peasant Levies no longer have any limitations on what unit type they can be, but conscripts are limited to only Irregulars and Hussars
- Forming Turtle Island now has additional requirements
- You can no longer use Disband Formation if this would result in Commanders being dismissed
- It is now possible to transfer all Admirals out of a fleet in a sea node, resulting in the original fleet automatically returning home
- Rehoming a formation now also causes it to travel to the new home headquarters
- It is no longer possible to construct unit types whose upkeep goods you have no access to in the target state
- Added formation mobilization and movement speed modifiers to military units
- Demobilization cooldown is now triggered for armies demobilized during diplomatic plays as well as after the war has broken out
- Armies can only be rehomed when demobilized; fleets can be rehomed at will
- Cavalry other than Hussars now require Military Drill to recruit
- Jobseekers metric now correctly excludes employees working in government or subsidized buildings (they were already excluded in logic, this just make it clearer what employees are actually available)
- Only Great Powers may now establish the Confederation of the Rhine
- Rivalries can no longer be immediately removed after being declared, you have to wait 5 years to do so
- Historical starting Companies now have establishment dates
- Adjusted the building groups that affect the Canal companies and their bonuses so they can achieve profitability
- "The Great Locomotive Chase" will now stop firing some decades after the end of the American Civil War, even though it's fun to steal trains even in peacetime
- Starting Chinese and Russian commanders have been assigned to relevant formations
- Added more dynamic country names in South America

### AI

- AI will now correctly identify whether it can or cannot borrow troops from other formations on the front and use that in its advancement decision making
- AI will now Convoy Raid again (previously disabled due to a performance-related bug in 1.5.9)
- AI will no longer advance with small armies if there are other larger armies on the front that could attack instead
- AI is now more likely to back down in plays where they are outmatched and the demands against them are not particularly harsh, particularly if by doing so they can avoid harsher secondary demands
- AI is now less likely to back down in plays where they have a large quantity of harsh primary demands being pressed against them, particularly if those demands include taking states
- AI will no longer advance with armies that have low morale or organization
- AI is now more likely to agree to an alliance or defensive pact if you have rivals in common with them
- Fixed an issue where the AI would be reluctant to mobilize too much of their army due to powerful allies even when they were in the process of losing the conflict and being occupied
- Fixed an issue where the AI would never upgrade its training production methods for barracks
- AI is now much less interested in offers of support that wouldn't contribute a meaningful amount of military power to their side in the play
- AI is now much less interested in offers of support if they already have overwhelming military power on their side in the play
- AI is now less keen on bankrolling countries in exchange for diplo play support if it would be a significant expense
- Added a new AI strategy for France, which assists it in gaining natural borders
- Fixed an issue in the AI where Britain would not start the Opium Wars due to their desire for treaty port not being correctly applied to their conquest attitude score
- AI will now never cancel trade routes with countries whom they have a trade agreement with unless those routes are at level 1 and unproductive, since those routes cost no BUR to maintain
- Fixed an issue where AI countries trying to open Japan would do so in a rather overly aggressive way, starting with treaty ports instead of using it as a defensive wargoal if attacked by Japan or outright annexing states alongside Open Market
- The AI's choices in the Fall of Salaverry event now properly impacts their diplomatic relations with the Federation

### Balance

- Increased migration values across the board (to account for a general decrease caused by fixing a migration bug that enforced a minimum per pop)
- More advanced unit types now consume far more goods, particularly advanced naval units
- Somewhat reduced Persian resource potentials (primarily iron, suplhur, and coal) due to balance and historicity issues
- Stormtroopers Technology now gives Offense bonus to Trench, Squad and Mechanized Infantry
- Updated Trade routes so that nations are not missing artillery at game start
- Rebalanced the combat stats for many of the previously less useful unit types, particularly Submarines and Carriers
- Increased the chance of wealthy lower-strata pops joining the Petit-Bourgeoisie
- Industry Banned now gives a throughput bonus to plantations
- Removed de Francia's starting health bonus, making the Perpetual Dictator a little less... perpetual
- The South Atlantic Slave Trade Journal Entry for Britain now times out after 50 years, as opposed to 20 months
- Shopkeepers pops in resource buildings now may join the Petit-Bourgeoisie
- The Brazilian monarchy now benefits from Great Power status
- China now starts with the Closed Borders law
- Replaced some company prosperity modifiers with the new formation speed modifiers
- Reduced the enactment chance penalty for the starting Pyragües modifier, and removed it entirely for the follow-up one
- Reduced Brazil's starting army size to ensure all starting war participants can at least achieve a white peace
- The Strike event no longer reduces the productivity of the entire country
- The Taiping Heavenly Kingdom will now be much more of a credible threat
- Paddle Steamer tech now gives a small combat bonus to navies instead of extra convoys
- Patronise Realism no longer requires so many Arts Academies
- Removed the Artillery Foundry in Mexico because they have no consumption
- Removed starting Portuguese claims in Africa
- Slightly adjusted the population makeup of Mesopotamia
- Tweaked revolution_pulse2_events.5 to be less severe

### Art

- Added flamethrower representation in battles when attacking
- Added a new victory and defeat battle end vfx
- Military troops will now start marching around your states when you mobilize your formations
- New audio events for flamethrowers, battle victory/defeat, rowboat, cancel naval invasion button
- Added backgrounds to the Company list items, based on Company Type
- Added Electric company icon for generic electric companies
- Updated some Alert icons
- Turned down revolution effect brightness during night-time

### Interface

- Added a "Mobilization" tab to the Military panel in order to make it easier to change and get an overview of each Formation's Mobilization Options
- Added a new confirmation for switching production methods that is shown if any of the affected buildings is predicted to have a low productivity after the change
- Added functionality to expand Buildings from the Goods Local Prices
- Buildings that are choosing not to hire due to concerns about lowered productivity will now show a different status icon from buildings that are trying but failing to hire
- Added support to plan naval invasions by right-clicking a State
- The reasons given when hiring fails should now be more indicative of the actual fail reason
- Added ongoing Naval invasions to the corresponding State, War, Battle, and Sea Region panels
- Added functionality to recruit Units to a Formation directly from the Military panel
- Effects of unit veterancy is now displayed in the unit rank tooltip
- Added a new alert if your growing colony is isolated from your market
- Added naval invasions display to the war panel, sea region panel, state panel and battle panel
- Names for historical military formations are now localized
- Naval Invasions now always display the reason they are not currently progressing, such as waiting for traveling formations or being stalled due to admirals having the wrong orders
- The notifications for when a Rivalry, Humiliation or War Reparations pact expires are now far more readable
- Added number of available options to deploy/station military formation buttons
- Added a list for which Special Orders a Commander can take to the Recruit Commander window
- Added an alert for when a naval invasion is stalled due to none of its admirals having orders that let them battle opposing fleets
- Added a warning to the transfer units button and to its tooltip when a transfer would result in a military formation being sent back to their home HQ
- Military Formation panel is automatically opened when creating a new Formation or when merging a Formation into another one
- Made all default Unit Types visible on the Formation panel even though there might not exist any unlocked Unit Types in that Unit Group
- Made the warning for "too many special units" make more sense
- Effects of units on battle victory score is now displayed in the breakdown
- Early Demobilization now has a confirmation box that explains the consequences
- Added "Units Under Recruitment" information to Formations
- Added warnings in the naval invasion planner when the selected fleet has no admiral with an intercept order, or the selected army has no general with an advance order
- Added the raise conscripts button the the Army right-click menu
- Implemented disband tooltip descriptions for different units (and button will now be grayed out if you have 0 units of this type)
- Added indicators of monthly progress to the Matter of Slavery and the Age of Caudillos
- When a Diplomatic Play escalates to War, the Diplomatic Play panel will now replace itself with the resulting War panel
- Added the raise conscript button to the Army list items on the Military panel
- Slaves are now included in the "jobseekers" metric for construction interactions
- More status descriptions were added for military formations
- Show Military Formation Icon in Military Formation Alerts
- Companies now display their establishment dates
- Added a warning to changing default unit type on a formation if the change would cancel some units from upgrading
- Added a reminder to the Fleet concept that they take a long time to build and can get outdated
- Combat unit tooltips are now more likely to show the correct unit icon for its culture
- Sorted the "Expand Building" Map Interaction list by number of Levels by default
- Adjusted the error message for not being able to upgrade a unit with the information that the types are too different
- The colony map markers are now shown when you are part of an ongoing diplomatic play
- Removed Rank Icon from portrait_mini
- Commander concept now refers to Generals, Admirals and Formations
- Combat Unit unlocks in the tech tree now has a more visually pleasing frame around it

### Modding

- All defines for Job Satisfaction now allow for decimals to be used
- Added a gui macros file ("data_binding/gui_macros.txt") and added an IsZero and NotZero function
- The is_mobilized trigger no longer supports a character scope, and now only works in a military formation scope
- Added a new effect to set the establishment date of a company
- Added separate AI strategy script value, value link and debug console command for AI desire for treaty ports
- Added a Logging.MilitaryFormations console command to print the current properties of all formations
- Several defines related to GOVERNMENT_STICKYNESS have been renamed to GOVERNMENT_STICKINESS

### Bugfixes

- Fixed a crash related to CPdxSpan
- Fixed a crash that could happen during convoy raiding calculations
- Fixed a crash related to elections
- Fixed crash in "Poland not lost" event after a button click in Christ of Nations Journal Entry
- Fixed a crash where the Heavenly Kingdom would always attempt to create a formation in South China HQ even if it doesn't have states there
- Fixed a crash related to transferring units between formations
- Fixed a deadlock that could happen when the player got notifications in parallel code
- Fixed a rare crash that could happen if the Heavenly Kingdom ceases to exist
- Fixed a random crash that could occur when starting freshly loaded savegame
- Fix crash that could happen after production method switching while time was ticking
- Fixed a bug with earnings predictions where sometimes buildings would not accurately predict their earnings after hiring, resulting in them hiring even though it craters their earnings
- Enemy fleets with no remaining manpower are no longer able to block a naval invasion
- Fixed a bug where fleets with Escort Convoys style orders were not able to intercept enemy fleets despite having interception chance in their modifiers
- Fixed a bug where unification would annex colonial subjects
- Fixed an issue where the amount of goods buildings were producing and consuming would lag behind employment changes by a week, resulting in incorrect market sell/buy orders and buildings making incorrect decisions about whether to hire/fire based on outdated data
- Dependents created from casualties in war are now distributed amongst the state population again, to prevent military buildings getting filled up with dependents
- You can no longer use Disband Formation on a Commander-in-Chief to "reroll" your Ruler
- Naval battles that occur as part of naval invasions are no longer subject to a "Landing Penalty"
- Fixed a front update issue that would cause front destruction, causing armies to unexpectedly go home
- You can no longer transfer more commanders into a formation than what it can fit
- Fixed bug where sometimes supply routes would not show up in Sea Region panel
- Combat Units are now again listed in the Battle Panel
- Fixed bug that caused the light tank to not be represented in dioramas
- Added missing tooltip on conscript numbers in the recruit conscripts map interaction
- Fixed demobilization cooldown not being removed after diplomatic plays and wars are over
- Fixed an issue where the completion trigger for the strike Journal Entry required more angry workers as opposed to less
- Local Goods can now never be in shortage on an entire Market (only in their local State) as this created misleading alerts
- Fixed an Out-of-Sync that happened when playing with different languages
- Fixed an issue that would sometimes prevent valid fronts from being created when impassable provinces were involved
- Demobilization cooldown is now properly calculated when transferring units between formations
- It is no longer possible to demobilize armies that are actively involved in a naval invasion
- Fixed an issue that was causing the obligation chance from bankroll to not appear in the bankroll tooltip
- Fixed issue with last Hegemon objective not appearing
- Prevented from auto moving military formation when its front splits if doing so would leave that front side empty
- Fixed issue where conscript numbers did not add up in the Military Formation panel
- Restricts candidates for Romanian unification to ones that can actually have subjects themselves, to prevent event spam
- The La Plata event will no longer give claims on state regions that contain uncolonized states, thus blocking colonization for other nations
- Several tweaks to ambient audio effects (volume, mixing, etc)
- Fixed audio layering issue on the Carrier fleet model
- Fixed cannon fuse audio attenuation issue that would cause cannons to be audible even on the paper map
- Update to soundbanks to fix 3D hub ambience issue and vehicles/movement pausing audio issues
- Ambient sound associated with horse carts and rowboat is now reduced in volume
- Loyalists no longer benefit the communist movement in "The Spectre Haunting the World" Journal Entry
- Military formations now cannot split during a naval invasion
- Fixed a bug when flags would flicker in diplomatic play menus
- Ensured that a formation that is rehomed is also able to be stationed in the headquarters that it is being rehomed to
- Cost of War is now displayed for all war participants in the tooltip
- The Hell on Earth event should now be significantly less spammy
- New conscription limits are now properly enforced when switching laws
- Fixed an issue during the merging of two states where some pops would lose their jobs
- Fixed a bug where, when moving a military formation from a front that had moved, the formation would get teleported to the initial front location
- Rubber plantations can now use slaves as workforce
- Removed the native warbands modifier for a decentralized nation that becomes a puppet or Argentina (no more Patagonian Super Soldiers)
- Increase/Reduce Autonomy' diplomatic plays now only display in the 'Unavailable plays' list if there is a subject relation
- Unification diplomatic plays will no longer appear in the 'Unavailable Plays targeting state' list
- Fixed an issue where the hiring fail reason due to low qualifications would incorrectly display more qualifications being available than needed
- Fixed an issue where a subject would get no market access in their states that require a port connection during an independence war
- Fixed an exploit where it was possible to upgrade units to types they were not allowed to be upgraded to
- Consumer Goods Tutorial now looks at local prices instead of market prices for goods
- Land and Naval HQ map markers are now separate map markers with different positions on the map
- Fixed an issue where some state regions had incorrectly defined provinces
- Fixed the bug when local consumption breakdowns were incorrect
- Resolved issue where famines would fire in null states
- Added localisation for from_free_trade in the Social-Democratic Party modifiers
- Resolved issue where the Coluna Prestes would fire an empty notification
- Fixed a localization bug with the Catarinense Republic's adjective
- Russia no longer clones all of their commanders on startup
- Allowed Power Plants to be automatically expanded again
- Replaced a broken Paraguayan fertility modifier with a working mortality reduction one
- Fixed rotation of ships in naval battles to fire in the right direction
- Fixed a localization error with the portrait render scale setting
- Fixed an edge case where the game didn't consider employment a requirement for a pop to be satisfied which led to unlocalized strings
- Fixed some incorrect calculations relating to mobilization
- Fixed the broken conditions for the Ottoman Tobacco Company
- Fixed bug causing all the battle dioramas to have their units placed incorrectly
- Algerian nations will no longer employ five year old girls as generals
- Fixed flickering bug with the conscription vfx
- Added country descriptions to some European and Arabian countries that lacked them
- Fixed bug that cause the military flags to not be visible if the player did not have the Voice of The People DLC turned on
- Fixed additional issues with exiles' clothing and the Meiji Restoration
- Excluded units from other formations in the units breakdown from "Building for Formations"
- Fixed an issue where an empty army's mobilization status failed to display correctly
- Replaced placeholder icons for Mobilization Options Groups' tooltips
- The Red Scare will no longer continue firing events targeting a nation that no longer exists
- Domingo Sarmiento is now properly born in 1811
- The Paris Commune no longer creates two wargoals that do the same thing
- Removes unused defines: DIPLO_PLAY_SWAY_COUNTRIES_LEANING_MULT, WAR_GOAL_INFAMY_UNIFICATION, DIRECT_CONNECTION_COST_MULT
- The Rule by Decree modifier no longer uses a placeholder icon
- Fixed spelling of Ecuadorian culture
- Fixed one instance where one trigger was incorrectly localized with a duplicate error status indicator

## 1.5.11

Patch 1.5.11 was released on 2023-12-13[4] with checksum *b0c6*.

### Improvements

- Formations that are merging into a formation that is destroyed will now try to merge into the closest available formation to the one that got destroyed
- After completing the Opium Crisis Journal Entry, it is now possible to unban opium through a decision, but doing so will remove the reward modifier granted from winning the opium wars
- Resolving the Opium Crisis now gives a much stronger reward modifier for a longer time
- Refusing to address the Opium Crisis now gives a negative modifier for a longer time and adds progress towards shattering china
- There is now a 10 year limit to complete the Opium Crisis Journal Entry, after which it will fail with similar effects to refusing to address the crisis
- The Tibet-India border is now only passable in a couple places, so that a frontline won't be created in the Himalayas between India and China in the Opium Wars
- Power Plants now have the same structure of ownership PMs as Railway, and can use the Government Owned PM under most economic systems
- Power Plants can now be subsidized under laws that allow subsidies for critical infrastructure, such as Laissez-Faire
- Naval HQs are no longer created in regions with only impassable coastal provinces or sea regions

### AI

- The AI is now properly able to understand the need to construct Power Plants in each relevant state to 'seed' those states with electricity
- The AI now considers subsidies for critical infrastructure (power plants, trade centers & railways) a must-have due to the potential economic armageddon that can be created if they are removed

### Balance

- Reduced Attrition values from an average 2% per week to 0.8%, through a combination of reducing the chance and also the min and max casualties of Attrition
- Increased the average time between convoy raids in a node from 15 to 20 days
- Convoy recovery is now 4x higher during peacetime
- Capital Ships are now only 50% as effective as other ships at Convoy Raiding, as a scaler to Offense
- Naval bases now recruit new manpower somewhat faster
- Front advancement speed bonuses has been replaced with equivalent character (general) advancement speed modifiers
- Changed unlocking technologies for some Cavalry units
- Increased the requirements needed to form the Confederation of the Rhine

### Art

- Replaced the background graphics of historic companies with more fitting ones

### Interface

- The disband formation button will now mention that there are formations that are traveling to merge into the formation that is being disbanded, if any such formation exists
- Updated the Special Unit Group concept tooltip to list the correct Special Unit groups

### Performance

- Improved the performance and thread utilization of supply network updates
- Small optimization in respawning unit entities

### Modding

- It is no longer possible to target fronts with timed modifiers, or to make new modifier types that target fronts

### Bugfixes

- Fixed a CTD when create_military_formation was run in an invalid HQ
- Fixed a CTD when one tried to add characters to a non existing formation
- Fixed an OOS causing error in the Characters category
- Fixed a bug that would multiply Convoy Raiding strength for every hostile country that held shipping lanes in a node
- Defeated Admirals are no longer able to contribute to convoy raiding
- Fixed an exploit that would allow ship-less fleets to be deployed to a sea node, blocking naval invasions
- Fixed a bug where Native Uprisings would not mobilize their armies properly
- Fixed an issue where AI attitudes were not correctly initialized on game start, causing most countries to have the 'Cautious' attitude regardless of strategic considerations
- Removed non-functional and misleading "enemy advancement speed penalty" modifier on the Defend order
- Commanders will now properly inherit relevant modifiers from active Mobilization Options (while mobilized) or timed modifiers on their formation
- Fixed a bug where state occupation percentages were not properly cleared when a country is leaving the war
- Fixed an issue where modifiers to war exhaustion from casualties would affect all sources of war exhaustion and not just from casualties
- Fixed a bug that could cause fronts to largely overlap one another
- Fixed a bug where the navy would travel to a node via land as a horse caravan when traveling through the land nodes was available
- Fixed a bug where adding conscripts to navies was not explicitly blocked, causing some very strange AI navies to occasionally appear
- Fixed a bug where the cost of construction queue items would sometimes not be properly calculated when the entire construction queue capacity wasn't used, which could cause private investment to over- or underuse the investment pool
- Autonomous Investment is now properly re-evaluated when a state is ceded, to prevent invalid constructions from being added in states a country no longer owns
- The Republican Proposal for Brazil now properly sets Pedro as the ruler of the country
- Fixed a bug where Paraguay's starting leader and traits would never go away in non-CotS versions of the game
- Fixed Mobilization speed modifier
- Fixed incorrect modifier for Truck Transport mobilization option
- Fixed Chocolate Mobilization not reducing 50% morale when removed from mobilized army
- Armies are no longer leaving a front for an HQ just because a participant left the Diplomatic Play that is still ongoing
- Fixed an issue that made it so AI countries with the relevant Journal Entry would not liberate subjects of Peru-Bolivia unless they had high infamy
- Fixed a bug where naval invasions could get stuck and never proceed to landing phase if the attached army's supply was not at 100%
- Fixed a bug that could cause Naval Invasions not to end properly
- Fixed a bug that would display irrelevant shipping lanes that didn't intersect the selected sea node
- Fixed an issue in the military formation notification for being restationed
- Audio soundbanks updated which fixes a couple of audio bugs like sounds appearing when zoomed out
- It is no longer possible to switch sides or declare neutrality in a diplomatic play where one of your subjects is targeted by Transfer Subject (this could be exploited to get subjects through sways and then invalidate the enemy wargoal by declaring neutrality)
- Fixed a bug where a Transfer Subject wargoal could cause subjects to not capitulate along with their overlord, resulting in strange lingering wars
- Fixed a bug where the overlord of a peace negotiating country in a war would sometimes not be considered a peace negotiator themselves, which could block peace entirely
- Fixed a bug where it was impossible to support allies against their subjects due to having an alliance with them
- Fixed a bug where an alliance with your market owner could block starting plays against your subjects
- Fixed a bug where Customs Union leader was considered to be the overlord of subjects of countries in their market, leading to incorrect diplomatic blocks and AI behavior
- Fixed a bug where only one 'liberate country' wargoal would show up for each target when adding wargoals
- Fixed a bug that prevented mobilization of armies with only non raised conscripts
- Mult modifiers can no longer reduce a value below the fixedpoint resolution limit (0.0001)
- Fixed a bug where the player got alerts for shortages for other countries in their market
- Fixed a bug that caused the notification for a repaired fleet to fire multiple times
- Fixes an issue in the naval invasion tooltip
- Fixed missing Loc for Subsidizing Power Plants
- Removed unnecessarily eliding label for job satisfaction in the Pop Details panel

## 1.5.12

Patch 1.5.12 was released on 2023-12-14[5] with checksum *8fd2*.

### Bugfixes

- Fixed OOS in AI related to headquarters when a client has a different operating system than the host
- Fixed OOS in AI related to fronts

## 1.5.13

Patch 1.5.13 was released on 2024-01-29[6] with checksum *9584*.

### Bugfixes

- Fixed a crash caused by peace deals allowing to-be-annexed countries to press conquer state wargoals.
- Fixed an out-of-bounds access crash related to Military Path Arrows
- Fixed a crash related to Military Path Arrow length

## References

1. ↑ Forum, [Victoria 3: Hotfix 1.5.8 is now LIVE!](https://forum.paradoxplaza.com/forum/index.php?threads/1610645), 2023-11-16.
2. ↑ Forum, [Victoria 3: Hotfix 1.5.9 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1611060), 2023-11-17.
3. ↑ Forum, [Victoria 3: Hotfix 1.5.10 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1614063), 2023-11-29.
4. ↑ Forum, [Victoria 3: Hotfix 1.5.11 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1616621), 2023-12-13.
5. ↑ Forum, [Victoria 3: Hotfix 1.5.12 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1617019), 2023-12-14.
6. ↑ Forum, [Victoria 3: Hotfix 1.5.13 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1622612), 2024-01-29.
