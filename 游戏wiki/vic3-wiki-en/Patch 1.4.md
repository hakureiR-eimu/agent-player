---
title: Patch 1.4
source: https://vic3.paradoxwikis.com/Patch_1.4
pageid: 5201
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
**Patch 1.4**, aka "Irish Breakfast", was released on the 2023-08-28[1] with the checksum *165c*. It was released alongside the [Dawn of Wonder](https://vic3.paradoxwikis.com/Dawn_of_Wonder) art pack.

## DLC features

- Day/Night cycle, configurable from the Theme Selector
- Lighting effects added to many new and existing gfx entities
- Night time soundscape now differs from daytime
- Festive clothing added for pops celebrating Carnival, Midsummer, Diwali, and royal weddings in Eastern Europe
- New Day/Night UI Theme added
- Day/Night themed paper map with zodiac illustrations
- Greenwich Observatory, Wat Arun, Temple of Poseidon, and Martand Sun Temple added as map decorations
- Pocketwatch, Candle, Atabey statue, and Hongshan statue added as table decorations
- Day/Night themed stagecoach
- New loading screen art

## Improvements

- Fixed some issues with goods substitution that was causing certain goods (such as oil in the early game) to not be demanded in correct amounts
- Subjects no longer remain in their overlord's market during an independence play/war
- Subjects no longer pay taxes to their overlord during an independence play/war
- Garibaldi will now stick around in minor Italian cultured nations, even in peacetime
- The American Civil war will now only ever happen as a result of a revolution to preserve, expand or abolish slavery
- Admirals with Escort Convoys orders now reduce the amount of damage done to convoys under their protection, scaling with the defensive combat stats of their ships
- Added strait adjacency to Vancouver Island
- Replaced all technology cost modifiers with technology speed modifiers, as these scale better and work properly with temporary modifiers such as from Interest Group traits
- Convoy Raiding damage is now partially randomized
- Randomly generated characters will now get up to 3 attempts to find a name that is unique among their country's characters
- Added a Portuguese admiral active in 1836
- Added Wikipedia links for some historical leaders of popular and recommended nations

## Balance

- Loyalists are now gained much slower due to high Legitimacy levels
- Standard of Living improvements now create more Loyalists while at the highest Legitimacy level
- Construction Sectors now use 3 infrastructure instead of 0.2
- Belgium no longer starts with an illegitimate government
- Fine Art can no longer be fully substituted by purchasing Services instead
- Added Dye Plantation potential to Haiti and Santo Domingo states
- Slowed the progress of Cement the Rightful Dynasty for all legitimacy values below 90.
- Removed extra starting Arts Academy in Austria from history files
- Lanfang now starts with the Academia technology
- Papal State starting trade route for Art now goes to Spain instead of Austria

## AI

- The AI (and autonomous construction) will now stop constructing in states with no workforce once the current available infrastructure is mostly used up, to avoid an endless cycle of constructing unused building levels
- The AI is now less likely to accept peace deals or capitulate if the whole country will be annexed
- The AI will no longer change who it is supporting for a Unification when at war or committed to a side in a diplomatic play, except to remove support for a country they are at war with (fixes an exploit with abusing temporary attitude changes from diplomatic plays to gain supporters)
- The AI for countries with the Economic Imperialism strategy is now more keen on opening up Japan's market
- The AI is no longer incorrectly biased to use only Anchorage PM in Ports
- The AI is now less inclined to support unrecognized powers against fellow recognized powers unless they have a strong reason to do so
- The AI will now take the decision to reduce Haitian debt.
- The AI will now take the decision to annex Kraków as Austria.

## Performance

- Performance when playing with mods that add Interest Groups has been improved
- Added a setting to cull distant buildings
- Optimized the memory consumption by building particles
- Optimized the trade routes panel
- Performance improvements for character rendering
- Particle Optimization
- Optimized the graphics for the day and night cycles
- Reduced the number of cars spawning on roads late-game

## Interface

- Added a Theme Selector to the main menu and ingame menu
- Buildings can now be pinned to the outliner
- Added a new read out to the war panel that exposes an AI controlled country's willingness to capitulate in a war
- The player now gets a notification if a country that they are at war with (either as a co-belligerent or as an enemy) goes into default, making them more likely to capitulate or accept peace
- Amended the character panel with a zoom-to button that orients the map to the location of the character and a location to the panel subtitle
- Show Strategic Region names instead of Country names in the Declare Interest Map Mode
- The cost tooltip for technologies now explains the penalty for unresearched technologies in earlier eras
- Add flavor description to the Interest Groups' tooltips
- Added a toast message indicating new and old ruler when they are changed.
- Hide the "Trade Routes" section in the Goods Details panel for non-Tradeable Goods.
- Add shortcut to the Goods details panel in Goods right-click menu
- Sea Node tooltip now tells you how many of your convoys are passing through the node
- Change the default keybind for Decisions from F12 to F11
- Zoom-to buttons are now disabled when you are already where they would take you
- Remove the support value shown on Agitators on the Political Movement panel since Agitators now give a multiplier and not a flat support bonus to the movement
- Show all potential Diplomatic Actions in the right-click menu for another Country instead of only showing the currently possible.
- The Agitator concept now has more information included
- Add functionality to instantly create a Trade Route to your Market when looking at the details for a Good in a foreign Market
- Add more actionable information to the "Establish Import/Export Route" tooltips (Price, Balance, Sell/Buy Orders)
- Make the back button the Sway Offer always go back one step, instead of going back two when a Offer type is selected.
- Added a list of IG icons after the name of the Party in a few places throughout the UI
- Add enactment cooldown to the setback concept tooltip
- Added information about the new leader and ideology to the "IG Leader Retired" Notification
- The Hegemon final objective now displays how much of a share of the global population you currently control
- Removed confusing checkmark boxes from Healthy Economy Game Concept
- Diplomatic Action map interactions will now display the correct cursor
- Moved "Cut Off Buildings" setting to advanced graphics section (renamed to "Cull Distant Buildings")
- Long graphic card names no longer displays out-of-bounds in settings menu

## Art

- Vancouver Island isn't connected to British Columbia by land anymore
- Map borders now blends better with the map
- Updated the look and feel of the New Game Screen
- Fixed text and scale on VotP map (VotP)
- Fixed the issue were the equator was gone on VotP map (VotP)
- Blue flag event marker is now scaled better
- Tweaked "Forbidden City" texture values to closer match the rest of the adjacent buildings.
- All port buildings now start as "small" size
- War Machine factories should no longer cause clipping issues in cities

## Modding

- Added 'kill_population' and 'kill_population_in_state' effects
- Character templates can now define a command HQ and rank
- New compare triggers 'global_population', 'total_population_share', 'total_population_including_subjects', and 'total_population_including_subjects_share'
- Added a 'pop_type_percent_state' trigger that checks whether the scoped state has X% of its population belonging to the specified pop type
- Added an 'ignore_battle_conditions' console command
- Added a 'noshortages' console command that prevents penalties for supply shortages in Buildings
- Added a 'fastincorporate' console command that incorporates states immediately
- Added a 'nosupportloss' console command that prevent countries from losing war support
- Added a 'month' compare trigger to check the current game month (useful for seasonal dress-up)
- Adds console command 'Logging.PopGrowth' to print the birthrate and mortality rates for each Standard of Living level

## Bugfixes

- Added workaround for crashes related to Intel high end CPUs
- Unique interest groups are now calculated on creation, rather than in a country's history, allowing revolutionary countries etc. to inherit their parents' unique interest groups
- Fixed localisation errors related to France's Natural Borders
- Fixed various scope issues in agitator law events
- Fixed erroneous scoping in "A Clause is Coming to Town" event
- Fixed a spline network crash
- Fixed an issue where colonization would be prohibited by other countries with claims even if they had no access to what you were trying to colonize
- Fixed a bug that allowed combat units to have more demoralized soldiers than actual soldiers in the unit
- Improved MP stability by resolving Out of Syncs resulting from flawed cache operations
- Fixed a bug where it was possible to use the 'Transfer Subject' wargoal on Customs Unions and Personal Unions
- Fixed an issue where trade route levels would alternate between increasing and decreasing every week due to inconsistencies in profitability calculations
- All countries that can create Interests now gain an active Interest in their capital region with no delay
- The Vox Diaboli event will no longer fire in atheist countries
- Fixed a bug where the zoom button to an Admiral raiding convoys got hung-up on zooming.
- Buildings can no longer be queued past the level limit while they are in the private construction queue
- Only show savegame incompatibility warning popup when the save is incompatible
- Fixed a bug that would prevent the reform government mode from closing when confirming a government with low legitimacy, potentially leading to one or more IGs being visually duplicated
- Children no longer experience early hair loss
- Fixed an issue in diplomatic play clean up for dying countries
- Generated heirs are now subject to the default character template like all other characters
- Fixed a bug where the game would keep trying to spawn a Civil War without any uprising States
- Fixed a bug where the player as observer without country could still receive notifications
- Fixed agitator home country tooltip displaying NULL_OBJ
- Fixed a bug where the Buildings Panel would have clickable buttons under "Potential Buildings", for buildings that cannot be built
- Fixed notification saying that country was swayed by itself when it was swayed by one of its subject countries
- Added a long cooldown to the DEI breakup event, so that choosing option c (continue to exist as DEI) will not cause the event to spam endlessly.
- Fixed the bug when becoming non-independent for two neighboring countries in the same state region didn't allow to set up trade routes
- Fixed the bug when a low number of convoys due to convoy raiding would not apply to excess convoy calculation
- Fixed a bug that would cause error log spam when hovering over the acceptance indicator when proposing wargoals to sway a country in a diplomatic play
- Fixed a localization error in the trigger description for is_unification_candidate
- Fixed some cases where relations with overlord and top overlord were not being checked when starting diplomatic plays like Conquer State against subjects
- Fixed issue with Increase Relations Tutorial not triggering
- Reduced spawn rate of certain African colonial events
- Fix notification names overflowing in the Message Settings
- Fixed an OOS due to the construction queue validation erroneously running during cache recalculation
- Fixed a bug related to fetching the ruler title from the government type in an effect splitting up on_government_type_change into two parts, putting the setting of ruler into a second effect on_post_government_type_change
- Fixed notification for new Trade Route mistakenly predicting it to "shrink to level -1"
- Fixed a bug when sometimes rank loss couldn't be stopped by increasing the prestige
- Fixed a bug when newly released country manpower in barracks wasn't properly updated and country had an empty armies that doesn't refill
- Fixed the bug when died recruitable characters created field promotions
- Construction queue duration estimate is now more accurate
- Subject country name is now correctly displayed in 'join side' diplomatic play notifications
- Fixed an UX issue that would cause a lone X to appear in tooltips for character interactions that cannot be executed
- Fixed an issue that could cause tooltips for `add_modifier`, `add_enactment_modifier`, `remove_modifier`, and `remove_modifier` effects from displaying incorrectly when the modifier has an apostrophe in the name
- Obligation Alert will now display the correct country in all situations
- Removed repeat economic law stance in anarchist ideology
- Legitimist monarchs no longer kill each other in rapid succession when generated
- Limited rate of African colonization event spawn
- Giovanni Gentile will now advocate for fascism in Italy rather than Siam, and Ernst Röhm is now a protestant
- Fixed CTD which happen while new state was spawned after another state had been removed
- Fixed a bug when "Oil Rush" effects or similar wouldn't increase employee count in a building
- Fixed CTD when stateless building tried to access impossible array size
- Fixed CTD which happen while new state was spawned after another state had been removed
- Map interactions involving HQ's will no longer contain duplicate UI entries
- Diplomatic Action map interactions no longer allow clicking on invalid interactions
- Changing shader quality to low should no longer cause rendering of the map to display in water.
- Fixed OOS related to Player Data
- Added entries for some missing modifier localization
- Infante Alfonso Carlos, Duke of San Jaime will no longer spawn as a Legitimist ruler before 1931 (VotP)
- Fixed crash when switching the graphics settings in the main menu after returning to it from the game
- Fixed an issue that prevented the Alaska Purchase from firing if the USA had a higher GDP than Russia
- Improved script for Government Petitions Journal Entries so it only looks if the Interest Group is powerful or not
- Lowered pop needs max supply share for Services and increased weight for Art
- Fixed issue with unlocalized Sea Node in the Atlantic Ocean
- The tutorial now explain why you can join a customs union
- Fixed incorrect text in additional income and additional expenses
- Declare Interest Tutorial will now select a region for you to declare an interest in instead of looking for available interests
- Removed potential for duplicate Bismarcks
- French heirs will now have the proper ideologies
- Bohemia can now form Czechoslovakia
- The Belle Époque no longer invalidates erroneously
- Revolutionary events will no longer occur in unincorporated states
- Ships should no longer disappear at the edge of the camera view

## References

1. ↑ Forum, [Victoria 3: Update 1.4 Checksum [165c]](https://forum.paradoxplaza.com/forum/index.php?threads/1597475), 2023-08-28.
