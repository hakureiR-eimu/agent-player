---
title: Patch 1.6
source: https://vic3.paradoxwikis.com/Patch_1.6
pageid: 5760
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
**Patch 1.6**, aka "Blackcurrant", was released on 2024-03-06[1] with the checksum *ea2d*.

## New Features in Update 1.6

- Free: [Migration system rework](https://forum.paradoxplaza.com/forum/index.php?threads/1624226) with Cultural Communities limiting which states pops might consider moving to, as a measure to improve UX and late-game performance
- Free: Filterable and sortable fullscreen [Census Data](https://forum.paradoxplaza.com/forum/index.php?threads/1622790) panel, to give you more insight into your population than you ever thought you needed
- Voice of the People: Implemented additional content for abdicating during revolutions
- Voice of the People: Added resign from Office character interaction
- Voice of the People: Implemented additional character interactions for countries with Secret Police, allowing for the assassination of troublesome characters

## Improvements

- A newly spawned country that inherits a war goal from a war in progress will now be automatically targeted with a new war for those war goals by the holder of that war goal, at no additional infamy. A common issue addressed by this change is that revolutions no longer invalidate war goals.
- It is now possible to merge the entirety of a formation (A) that is itself the target of a merge into a different formation (B). This will retarget the formations that are traveling to merge with A so that they will instead travel to merge into B. Previously, this kind of merge was forbidden.
- The Art pop need category has been replaced with a new Leisure category, letting the very wealthiest among your people self-actualize in style. This need consists mostly of Fine Arts but also an assortment of other goods such as Clippers, Small Arms, Wine, Aeroplanes, etc. Services act as a low-weighted fallback if these other goods are exceptionally rare in your market.
- When a subject starts an Independence or Increase Autonomy diplomatic play, that play now takes place in the subject's capital rather than in the overlord's
- Overlords taking control of a play no longer get the option to switch sides
- Native Uprisings now have the native country as attacker rather than defender, and so no longer prevent the colonizing country from starting their own plays
- Added button to upgrade all units in a unit group
- The game will now warn you if you launch with mods that aren't marked as compatible with your current version. Pressing "ignore" will ignore this warning for the current version of the game.
- Garibaldi will no longer show up to defend countries against autocratic revolutions (e.g. Garibaldi should not be getting involved in Indian Peasant uprisings)
- Garibaldi will no longer show up to defend democratic countries against significantly weaker autocratic ones (e.g. Garibaldi should not be defending the USA against Native Americans)
- Garibaldi can now show up to fight for democratically inclined revolutions and secessions against autocratic countries
- Only fully occupied states now contribute towards war exhaustion, occupation progress has no effect
- Added new Mass Migration Attraction concept
- Updated migration concepts to be more representative of the current state of the game and be more interconnected
- Added mobilization and movement speed modifiers for formations and unit modifiers for formations
- Added a button to upgrade all upgradable units in a Military Formation, and one for all Military Formations owned by the player
- It is now possible for subjects to switch sides in a play if the other side has a Liberate Subject wargoal targeting them and haven't added any additional wargoals against them (the AI will do only do this if they are Rebellious)
- It is now possible to attempt to sway rebellious and human-controlled subjects by offering them Independence or Increase Autonomy as a wargoal. Reverse-swaying is also supported, so the subject can offer to side against their overlord in exchange for one of these wargoals.
- The effects of breaking manually vs auto-breaking a pact can now differ, auto-breaking an Alliance won't cause a relations hit but still creates a truce, for example
- Added more URLs for Historical Characters
- Canals now provide a bonus to migration attraction
- Mandatory baldness is no longer enforced on non-Buddhist Devout IG leaders
- The Pampas state trait now gives a bonus to ranching as well
- Mongolia is now only released in Outer Mongolia. A Greater Mongolian state will take some additional effort.
- Japan, Korea, Siam, Vietnam, Tibet, and Cambodia now start with the Sericulture technology
- Adjusted the population/arable land of Inner and Outer Mongolia to better reflect the situation in 1836
- Replaced the 'Gobi Desert' trait in Monan with 'Eastern Steppe'
- Renamed the 'Tianshan' state region to 'Tarim Basin'
- Added a Mongolian homeland to Dzungaria
- Updated the demographic data of Dzungaria and the Tarim Basin to better reflect the situation in 1836
- Revised Bulgarian and Corsican namelists
- Enacting Free Trade will now remove opium ban if you have it active as China
- Improved tooltips and performance in the Diplomatic Actions lens
- Decentralized nations now have their own logic for which attitude they display based on tension and whether there is an ongoing native uprising, and won't randomly display a friendly attitude that doesn't actually have mechanical significance
- Taiping states now require turmoil to be selected
- Baluchistan now requires Nationalism rather than Pan-Nationalism to form
- Moved a Dutch general from the character pool to the Dutch East Indies, where he will serve as a general and an IG leader.

## AI

- The military AI is now much better at organizing its formations in HQs, and will create, merge, split and rearrange its formations to have more balanced sizes
- The military AI can now split off temporary formations during wars in order to defend or advance on fronts it would not otherwise be able to properly cover. The temporary formations are merged back into their parent formation after the war is over.
- The AI is now less interested in subjugating themselves to foreign powers they do not have a good relationship with in diplomatic plays
- The military AI will now create explicit garrison formations in important HQs that will focus on defending that HQ and not travel too far away from it. Garrisons have their own separate mobilization logic and will usually be mobilized during war if there is a perceived threat to their HQ.
- The AI is now more reluctant to give up its subjects in diplomatic plays, particularly if they are of significant value
- The AI now places greater emphasis on defending their capital state, especially against backdoor naval invasions
- The AI now tends to use defensive orders for their generals if those generals are commanding below-average quality troops on the front, so as not to reverse the overall progress with failed attacks
- The AI now considers qualifications to be more of a factor when determining what buildings to build and PMs to change to

## Balance

- Capped the amount of of interests you can receive from Naval Power Projection
- Technologies can now increase the amount of max Interests
- Added another canning Production Method to Food Industries that allows you to pick between Fish or Meat as a consumption good
- Lowered Farm output of Grain from 30/50/90/140 to 20/40/80/120[2]
- Removed South Africa's starting navy.
- Added a cooldown to establishing and disbanding companies. A recently established company cannot be immediately disbanded and a recently disbanded one cannot be reestablished right away.[2]
- Pops will now consider their job satisfaction during employment updates.
- Reduced penalties on decentralized nations to prevent mass starvation
- Rebalanced the starting situations for most countries with Military Formations in the History files
- Hardwood Production and Focused Hardwood Production, Production Methods reduced Hardwood output to 10 and 20
- Decreased the amount of food from Subsistence Farms from 2.5 per level to 2[2]
- Agitators may now only participate in an election once every six months.
- Edited the starting Spanish, Hanseatic, East Indies, Luxembourgish, Portuguese, Prussian and Russian armies to better reflect the historical situation.
- Greener Grass Campaign has been rebalanced and now provides a flat migration attraction bonus along a lower multiplicative bonus.
- Downsizing a building level that isn't fully staffed now only generates a proportional number of radicals to its staffing, and no radicals at all if the level was not staffed at all
- Researching Paved Roads no longer adds any infrastructure from Pops
- Pop Consumption of Automobiles in a state now adds a small amount of infrastructure, which is increased when Paved Roads is researched
- Converting to State Atheism now gives you a larger number of immediate 'converts' in incorporated states
- Added combat penalties to Panicked Retreat
- Added morale damage penalties to Controlled and Panicked Retreat
- Added Straits between: Sumatra and Java, Java and Bali, Zealand and Jutland, and New Zealand
- Citrus Orchard Production Methods now don't consume all wheat
- Barbed Wire is now unlocked by Field Works
- Removed Serfdom and swapped Slave Trade for Legacy Slavery in Grao Para
- Companies that required 10 levels of Buildings now only require 3 levels
- Changed unlocking technologies for some Cavalry units[2]
- Consumer Goods Tutorial now looks at local prices instead of market prices for goods[2]
- Travel time for formations through different terrains has been lowered
- Stormtroopers Technology now gives Offense bonus to Trench, Squad and Mechanized Infantry[2]
- The Brazilian monarchy now benefits from Great Power status[2]
- China now starts with the Closed Borders law[2]
- Drastically increased the naval power projection requirement for Brazilian slave trade events.
- Job Satisfaction from being able to afford expenses now scales with the income / expenses ratio instead of being a flat value
- When a country is Cut Down to Size, it now receives a decaying prestige penalty and is unable to start any aggressive diplomatic plays for 5 years
- Pop need rebalancing between categories, especially in the Wealth 20+ range
- Hanyang Company now gives 20% attack bonus for Shrapnel Artillery
- Removed Impassable Terrain from Islands and other areas where it is blocking combat for no reason
- Reduced Rubber input for Elastics to 10
- Lowered Rubber input, and Tools output for Machined Steel Tools
- Reduced Engines input of Reinforced Wooden Ships Production Methods
- Increased Steamers output in Steam Ships Production method
- Lowered the modifier for Metropolitian Railway
- Lowered the Interception chance of Admirals on Convoy Escort missions
- Added Submarine Offense Modifier to Experienced and Expert Convoy Raider
- Added a Farm to Piratini, Warsangali and Isaaq
- Gone through and balanced some Companies to make Prosperity bonuses more valuable
- Reduced the amount of Infrastructure from Streetlights Production Methods by 50%
- Increased the attraction of middle/upper strata pops in military industries to the Armed Forces.
- Slightly reduced the military penalties from the Lost the Opium Wars modifier.
- Reduced radical gain from losing the Opium Wars.
- Added Dye potentials to South Carolina, Georgia, and Florida.[2]
- Mass Migration now consistently checks for turmoil or SoL specifically in the relevant states (e.g. homelands) and not as much in the whole country
- Removed Strait between Svealand and Åland
- Publicly Traded is now available at all levels of Motor Industry
- Removed the Artillery Foundry in Mexico because they have no consumption[2]
- Pollution is now on Meat Production Methods instead of Fabric Production Methods
- "Socialist Demagogue" will now spawn less often
- Puppeting Bolivia now makes the Peru-Bolivia journal entry fail
- Increased the requirements needed to form the Confederation of the Rhine[2]
- Characters that basically agree with the government can no longer be exiled.
- Elected Bureaucrats law now makes Bureaucrats more inclined to join the Petit-Bourgeoisie, rather than boosting raw PB political strength.[2]
- Hereditary Bureaucrats law now increases Aristocrats political strength rather than raw Landowners political strength.[2]
- Appointed Bureaucrats law now increases Bureaucrats political strength rather than raw Intelligentsia political strength.[2]
- Subsistence buildings under Collectivised Agriculture now employ fewer Clergymen.[2]
- The Monarchy law now increases the political strength of Aristocrats, rather than providing a flat bonus to Landowners clout.[2]
- Council Republics are now more inclined to enact progressive laws and develop industrially.
- Agitators no longer interfere in the enactment of laws they have no stance for.[2]
- Few states penalty to mass migration chance now works through a multiplicative modifier rather than division
- Rebalanced the value of the population factor for migration.
- Gave Montenegro and Nejd a Grain Import Trade Route[2]
- Compañía Sudamericana de Vapores now targets Shipyards instead of Ports so that it can be Prosperous
- Exiling interest group leaders now angers their interest group.
- Patronise Realism no longer requires so many Arts Academies[2]
- Reduced Bureaucracy penalty for Greece restoring the Olympics.[2]

## Art

- Tanks and Artillery now explode when defeated
- Added a representation of the Chemical Warfare mobilization option to battle dioramas when attacking
- Locomotive types are now spawned based on culture, political connections and market connections
- Added visuals to city buildings which to represent the Standards of Living in the area
- Added new first aid cart and field hospital 3D models to frontline graphics
- Fixed an issue with revolution flags appearing black, they are now correctly colored as the revolutionary interest group color
- Added new Flamethrower effects
- Added Maxim machinegun visual and audio effects
- Ships now splash when sunk
- Added new Vfx when battles end
- Fixed a bug where some of the Asian buildings would clip with each other
- Fixed a bug that causes the military flags to not be visible if the player did not have the Voice of The People DLC turned on
- Enhanced details on map units weaponry
- Reduced the range of the torpedo fired by the Submarine and Torpedo Boat
- Fixed lightmask on navy ships Frigate, Monitor and Submarine 3D model

## Interface

- Added manpower, organization, and morale bars to the Military Formation tooltip
- Added quick action buttons to move all or half of the units and commanders from one side to the other side in the Transfer Popup
- Added info about tariffs and consumption taxes to the Goods tooltip, and also added buttons to change them there directly
- Added a table of Undecided Countries in the "Start a Diplomatic Play" confirmation, showing Military Strength and how likely they are to join either side of the Play
- When there are multiple enemy/allied formations in the same location, they are now consolidated into a single map marker which shows a summarized view instead of forming a 'tower' of map markers. Clicking the consolidated map marker will open a selection list to let you select any one of the formations it contains. The player's formations still always get their own individual map markers.
- Building expansion tooltip now takes into account the impact of understaffed buildings and queued constructions and so no longer displays overly optimistic revenue estimates for a building that's mostly empty or which has a bunch of queued levels already
- Added current + expected number of a default unit type's units to their selection menu buttons.
- Added number of current + expected units in a Unit Type to the Unit Type tooltips in a Formation.
- Added a more detailed list item in the Construction Interaction list, showing Employment, State Traits, Production Methods and Local Prices
- !' is now removed from the production method after mouse hovers over it
- The tooltip for changing production methods should now show much more accurate information as to the building's production, consumption, revenue and employment immediately after the change takes effect
- The tooltip for showing an active production method now properly takes into account throughput, input and output multipliers such as economy of scale
- Revised the way qualifications are displayed so that for each pop type, qualifications are only shown if the qualifying pop would have a reasonable chance of actually taking the job, based on factors such as job satisfaction and pop type wage, meaning that the qualification numbers can now actually be trusted to tell you whether you have Pops that both qualify and would consider actually doing the job in question
- Added new Migration map mode that displays amount of migration to and from states
- Added new Mass Migration Attraction map mode that gives a rough idea of what countries mass migrations are likely to target
- Added new Mass Migration Potential Targets map mode that shows the migration attraction among the states that are eligible for mass migrations
- Added customize button for a Formation's name/icon to their right-click menu.
- Added groups for journal entries
- Added a short "label" and a "status" for a Country, describing who they are to you and your relationship.
- AI Strategies are now shown in the tooltip for a Country
- Character Interaction cooldown duration now shows as preview before interaction is triggered
- Buildings that are unwilling or unable to hire now show more detailed tooltips with the exact reason they are unwilling/unable
- Reworked the layout of formations on the Military Panel
- Reworked Migration Attraction map mode to only show states in your market to better indicate how intra-market migration works and better indicate where pops move in your market
- Migration tooltips now indicate if a state is eligible for mass migrations or not
- Cleaned up and sorted the interest group tooltip
- Added Infamy value to the topbar.
- Exposed a Country's preference for each side in the Diplomatic Play directly in the Sway panel without having to dig through several layers of nested tooltips
- The Government Interest Groups are now added to the tooltip for a Country
- The current direction (up/down) of your Relations in the tooltip for a Country is now visible
- Replaced "State Taxation Revenue" text list in with the same information as a table
- Removed the Ongoing Diplomatic Pacts Outliner section (replaced with pinnable Countries)
- When Fleets are zero, they will no longer appear in the Diplomatic Play Sway panel
- When Mobilization is zero, it will no longer appear in the Diplomatic Play Sway panel
- Lists within the panels on the left side of the UI no longer reset their position back to the top when you close the window and then reopen it. They also retain their old positions when switching between tabs.
- Added the companies icon to the sidebar button
- Fixed issue where NO_ORIGIN_FORMATION_SELECTED was shown as tooltip text in Transfer Popup.
- An army or fleet without a commanding officer can now be merged with another formation
- The tooltip for changing production methods now warns you if changing a PM would result in other PMs (such as ownership PMs) would be changed as a result, and includes the effects of those changes in its calculations of production, revenue etc
- Migration values are now displayed as weekly values rather than annual ones (with a few exceptions)
- Added a small Price graph to each Goods item in the Market panel
- The number of Conscripts is now visible in the Diplomatic Play Sway panel
- Added new icon for electric companies
- Map notification for Grant Independence shows valid text
- Fixed Slave pops mentioned in Slave State tooltip not having a tooltip
- The warning for insufficient qualifications now provides more information, such as how many months of current qualification growth the missing qualifications represent for the relevant pop types
- Alerts that a diplomatic pact is about to break now only show up if relations are actively trending towards the break point due to ongoing actions/pacts, not if they're just close to the break point but have no reason to up/go down further
- When a pact breaks or is about to break, the interface will now provide much clearer and more readable information about the reason for the break
- Devastation and Turmoil Effect Map Markers are now visible on mid zoom level if State is being highlighted
- Tweaked the layout for the Country Details panel to show AI Strategies without having to scroll
- Reordered things in the tooltip for countries to more closely reflect the order of importance
- The Subject Types a Country has is now shown in the tooltip for a country
- Exposed the Ranking Number for the stats on the Country details panel
- Replaced "Members" text list in the tooltip for parties with a table
- The "Attitude towards you" icon is now shown on each Country item in the Diplomatic Play Sway panel
- Sorted all lanes based on total Power Projection of the Country in the Diplomatic Play Sway panel
- Agitator number on hover shows tooltip on where the Agitator Slots comes from
- Tooltip for political strength shows reason for slaves not having political strength
- Generals who used to Advance on a front but have switched to Defend no longer contribute their old Advancement progress to the front side's combined Advancement meter (visual bug only)
- Added tooltips for the sort header buttons on the Local Price tab for a Good.
- Optimized the performance of the Outliner by flattening the layout hierarchy
- Made it possible to unpin Diplomatic Plays from the Outliner
- Made it possible to unpin Political Movements from the Outliner
- Added a Country Map Marker to the Diplomacy Map Mode, showing Attitude and Relations
- Cleaned up the layout on the Diplomatic Play Sway panel, generally made things more compact to give a better overview
- Added a setting for having the Notification Feed show up the left of the Outliner
- Added colors to Notifications (good/neutral/bad)
- Transfer formation popup now supports state and unit filters
- Added Military Formation breakdowns in Country battalion tooltips.
- Fixed issue where unit type icons would sometimes not show up in nested tooltips
- Will now show the reason for Commanders not being able to transfer sides in Transfer Pop up
- The text for loading game in both main menu & in-game menu now says 'Load Game' for consistency
- Fixed long country names in various places
- Fixed overlapping text in Lenses for different languages
- Increased time allowance for players to answer sway offers from 7 to 14 days. The AI should still answer them within a few days.
- Tooltip when attempting to Disband Formation with too many commanders is now more intelligible
- Tooltip for Diplomatic Actions that improve or damage relations have been reworded to be less confusing
- Added better tooltips for commander orders
- Added keyboard shortcuts for "Zoom to" (z) and "Pin in Outliner" (x)
- Hooked in "Go to details" keyboard shortcut in all Information Panel headers
- The Religion texture is now visible in the tooltip for Religion
- Made it possible to pin Countries to the Outliner
- Reworked all Outliner items to have more, and better, information
- Market Goods Shortage is no longer duplicated in the Notification settings panel.
- Combat Unit unlocks in the tech tree now has frame around it
- If Load game is not available, an in-game menu with show 'Load Game' text in italic for consistency will appear
- Changed Judaism's color to light blue[2]
- Fixed an issue where an empty army's mobilization status failed to display correctly.
- Changed the "Never" label for permanent Modifiers to "Permanent"
- Cultural turmoil now displays with consistent number rounding.
- Release subject option will be default option in Release-Subject tab in Diplomacy panel
- Added localization to sea node names
- Updated Attrition concept

## Performance

- Reworked how pops migrate to reduce the overall number of pops in the world, in order to improve late game performance
- Shortened load times when starting a new game
- Made AI spending updates more performant
- Reduced the size of several of the particle textures to improve performance
- Resolved a performance issue with the revolution update toggling all mesh objects off each frame even when unnecessary
- Reduced performance impacts of Diplomatic Plays by having the AI calculate when it wants to declare neutrality once per diplomatic play instead of checking each tick
- Optimized battle code to prevent unnecessary modifier recalculations
- Parallelize checks for battle condition updates
- Improved performance when iterating pops by reducing the object's memory footprint, leading to better cache utilization
- Improved the performance of unit morale calculations

## Modding

- Several migration defines have been renamed, restructured or removed
- Production Methods can now specify that they require access to particular goods to be able to be selected[2]
- New trigger (num_cultural_communities) to check how many cultural communities are present in a state implemented
- Added new trigger that checks if a given state is eligible for mass migrations
- Added functionality to create and add tables to tooltips
- Added script links for migration attraction to be able to check what a state or country's migration attraction is
- New event target links for formation to home_hq, formation to current_hq, hq to strategic region
- country_army_unit_type_fraction and formation_army_unit_type_fraction triggers check the fraction of a specific unit type in a country's army or in a specific formation
- country_navy_unit_type_fraction and formation_navy_unit_type_fraction triggers check the fraction of a specific unit type in a country's navy or in a specific formation
- army_mobilization_option_fraction trigger checks the fraction of units having a specific mobilization option in a country's army
- Added console command `enactment_checkpoint <type>`
- Removed `is_repairing` trigger, because it was untruthful

## Bugfixes

- Fixed a bug when combat unit modifiers from characters weren't applied in battle
- Improves checks to determine if a military formation can travel to a given location
- Armies that find themselves unable to path will preferentially be repositioned to their home headquarters rather than to their country's capital headquarters, if the former are available
- Military Formations should now more reliably pursue their wargoals and designated strategic objectives
- Fixed an issue that could lead to armies hanging around in non-owned territory
- Fixed intercontinental front merging. This fix stops e.g. French formations in Denmark winning a decisive battle deciding to go Kenya simply because there's also a Danish front there, rather than deploying to a different front that got opened in Denmark
- Fixed a crash caused by an issue that would allow the proposal of a peace deal in which a country would both be annexed and receive land as part of conflicting war goals
- Fixed an out of sync related to how the game would load travel node definitions from game files
- Fixed an occupation lifting issue whereupon provinces belonging to a subject whose overlord was being annexed would still be considered occupied by what would become their new overlord after the war ended
- Added missing information that demobilized armies in a Naval Invasion will mobilize automatically
- Fixed tooltip showing NULL_OBJ text for Increase/Reduce Autonomy diplomatic plays
- Fixed an order of operations issue that would try to find a new front to deploy a formation to, before the front was created. This fix stops e.g. French formations in Denmark winning a decisive battle deciding that "this was a nice battle boys, let's go home", rather than deploying to a different front that got opened in Denmark.
- Fixed an issue where Alliances/Defensive Pacts could auto-break during diplomatic plays if the ally remained neutral, even though Call Ally wasn't used
- Map mode locking now works as expected
- Fix OS-dependent out-of-sync caused by AI stationing formations in different headquarters on different operating systems
- Fixed a bug where temporary friendly occupation of states would add war exhaustion to the occupied ally
- Fix a bug where buildings would sometimes inaccurately calculate their productivity after hiring to be much lower than it would actually be, resulting in buildings not hiring even when they definitely should
- Fixed an issue where truces would not block Unification plays
- Fixed a bug where proposed peace deals could become invalid due to countries capitulating. Peace deal war goals are now revalidated when countries leave the war, and will be set as non-active if any war goals end up being invalidated and removed.
- Fixed an issue where the tooltip for propose peace deal would not display the reason an invalid peace deal cannot be proposed
- Fixed a bug that prevented advancing formations from borrowing units from friendly formations on the front
- It is now impossible to disband units or formations while a revolution or secession movement is brewing in your country, just like you cannot downsize buildings under those conditions
- Fixed military unit type icons missing in their tooltips.
- Removed the redundant demobilized status from Fleet unit's tooltips
- Removed conscripts info on Fleets in the Military panel - Navy tab
- Fixed an out of sync error caused by military formation movement
- Fixed a crash caused by combat unit modifier calculations
- Fixed a crash caused by occupation graphics
- Fixed an issue where save game items would show the wrong flag if the player had a high number of saves
- Fixed some issues with un-tooltippable modifiers in certain event options
- Fixed a bug where the Spanish Flu could spread to a non-existing state
- Fixed a crash which could occur during right-click on law buttons while the game is unpaused
- Fixed a crash which was caused by conscripts trying to be created in a dead state
- Fixed a bug that would cause formations to enter a confused state by using a formation that has other formations traveling to merge into it as part of a naval invasion. Thusly confused formations would then lead to other issues such as not being able to merge or properly reach headquarters
- Fixed an issue that would prevent stationing armies in headquarters of countries that are allied or on the same side in a diplomatic play
- Growing colonies are no longer removed temporarily during native uprisings or truces, but are simply put on hold instead
- Positive Job Satisfaction no longer blocks pops from getting hired into government or subsidized positions
- Booming Industries now gives correct modifier to Explosives Factory and not Chemical Plants
- There should no longer be any cases of political parties failing to form upon enacting Single-Party State
- Resolved faulty script which made Fascist, Integralist, and Bonapartist ideologies not show up properly for certain interest groups
- The Republican Proposal for Brazil now properly sets Pedro as the ruler of the country.
- Fixed an issue with the "Promote European Migration" interaction that would select a state not eligible for a mass migration leading to it getting immediately canceled
- Fixed a crash related to trade routes
- Fixed a bug where the special monuments building types where showing up in the outliner
- Fixed a bug where civilian ships were missing from the map
- Fixed a bug where subjects of customs union juniors would get erroneously capitulated when the customs union senior capitulated in a war
- Fixed a bug where the 'Universal Pop Political Strength' modifier from Anarchy wasn't being multiplied by the number of individuals, resulting it in doing very little at all
- Fixed some issues with how the future price of local goods was being estimated from ongoing constructions and unstaffed buildings
- Fixed an issue where goods substitution of Transportation need was excessively skewed in favor of automobiles, resulting in Pops going crazy for cars over trains even when car prices were maxed out
- It is now possible to grant leadership to agitators of any religion under State Atheism, so long as they are not Theocrats, Integralists or Traditionalists
- Home Offense/Defense modifiers applied to countries, states, or characters are now correctly applied to units fighting in home territory
- Trade States diplomatic action requests that uses Obligations are no longer delivered with a pink smiley face instead of an icon
- Decision to remove opium ban after winning the opium war now removes correct modifier
- Slaves are now affected by Dangerous Working Conditions
- Grao Para and Oranje should no longer start with Illegitimate Governments
- Fixed issue with last Hegemon objective not appearing
- Disabled the Traditionalist ideology for France, as it is supplanted by Legitimist
- Unifying Carolina no longer grants claims on all Dixie states
- Carolina no longer appears as a possible unification for Texas
- Russia no longer clones all of their commanders on startup[2]
- Resolved issue where Isabel would become President after Pedro's death
- Leader ideologies may now trigger Path to Liberalism properly
- Divided Monarchists can no longer revive Louis-Filippe from the dead
- Kazan now has the Sunni state religion[2]
- Prevented the re-animation of Louis-Philippe in the case of finishing Divided Monarchists after he dies
- The Sepoy Mutiny can no longer attempt to take a nonexistent state
- Fixed a bug where mass migrations could get into an invalid state if the origin country got annexed
- Fixed an issue where interest group modifiers would not affect some legitimacy calculations
- Fixed bug where sometimes supply routes don't show up in the Sea Region panel.
- Fixed a bug where the transfer All and Half buttons in the military formation transfer screen did not transfer commanders
- Fixed issue where upgrade all in group button would not correct identify and upgrade unraised conscripts
- Fixed some instances of the outliner scrolling its lists up or down when not intended
- Fixed a bug that allowed AI countries to sway themselves in diplomatic plays
- Fixed a bug where transfering units to an empty formation would result in an incorrect warning that you were about to disband a formation
- Fixed a bug where the transfer formation confirmation tooltip would show inaccurate information about unit transfers when transferring units from the right-hand to the left-hand side formation or in both directions at once
- Fixed a bug where Legitimacy effects from Ruler Character Traits were not being correctly applied
- Colonization of Homelands with Severe Malaria is no longer blocked by not having researched Quinine
- Tooltips for truces now references both countries involved in the truce, not just one of them
- Tooltip for Strategic Objective will now show the theater name even when the state is not controlled by its owner
- Journal Entries, events, and skill traits that relied on Production Method usage among a Commander's units now instead reference Combat Unit ratios in the Commander's formations (which fixes a bug with e.g. War in the Mud Journal Entry)
- "Piratini not Piratiny" is no longer a DLC locked Achievement
- Corn laws with Isolation is now possible to trigger and now requires Free Trade to complete
- Renamed Oldenburg to Osnabrück
- Subjects will now get a notification when their Overlord is imposing a law on them
- Panama Company no longer requires the State to be Incorporated
- Poor Visibility Battle condition now targets Unit Defense instead of Army Defense
- Fixed issue with Wolfpack Commander Order needing Destroyers instead of Submarines
- Replaced Puppet with Protectorate in Make Protectorate popup
- Fixed formations not being visually positioned at HQs when created
- The "Undeserved Blame" event will no longer spawn with a blank culture
- Added a failsafe event for cases where the ruling party in a single-party state becomes insurrectionary
- Loyalists no longer benefit the communist movement in "The Spectre Haunting the World" Journal Entry[2]
- Italian unification no longer requires Papal States to exist[2]
- Canadian colonies now transfer their claims to one another when merged by decision[2]
- The Metropolitan Railway now selects the correct state
- If the Treaty of Turin is signed, Italian unifiers will no longer seek to seize Savoy
- Fixed an issue where buildings would not validate their production methods correctly
- Fixed a bug where armies with only conscripts could not be raised
- Fixed a bug where dependents of dead and wounded soldiers did not move around the state looking for subsistence correctly
- Fixed a bug when combat unit modifiers from characters weren't applied in battle
- Impose law can now only be done on subservient subjects
- Fixed a bug where Decentralized nations could end up with Secessions
- Fixed a bug where some vassal-related tooltips could show a bunch of errors next to the name of the overlord
- Fix out-of-synch caused by AI iterating an unordered set of fronts
- Fixed one instance of a bug that would allow exceeding the formation commander limit by merging formations in a specific way
- "The Great Locomotive Chase" will stop firing decades after the end of the American Civil War, even though it's fun to steal trains even in peacetime.[2]
- One can no longer sway personal union subjects
- Paratini's Struggle for Independence Journal Entry now states that you need to enforce wargoals on Brazil to get the Event
- Skyscraper tooltip no longer shows that it is affected by Economy of Scale
- Missing loc string for Non-participant notification tooltip for Peace Signed
- Fixed formations being visually stuck after a successful naval invasion
- Fixed formations being stuck at null fronts or HQs
- Fixed battle dioramas not showing ground entity
- The "Thieves and Liars" event will no longer spawn with blank localization.
- The Red Scare will no longer continue firing events targeting a nation that no longer exists.
- Quechua and South Andean subjects are prevented from being annexed.[2]
- Isolationist countries will no longer get Steel and Paper import events.
- William Shubrick is now an admiral.
- Confederating Canada now incorporates states properly.[2]
- Event expedition_events.120 is no longer orphaned.
- Completing the Great Famine journal entry now clears modifiers as intended.
- Only either the struggling or starving define modifiers to migration will apply now, instead of both applying if the SoL is starving
- Fixed potential issues with precision while applying the population factor for migration
- Fixed a bug and made improvements to how disbanded empty armies with only commanders redistribute those commanders
- Fixed a crash where units were sent to invalid formations
- Fixed a bug where breaking a custom union pacts could create a transfer subject wargoal
- Fixed a bug in event description of wedding.3
- Fixed a bug where state selection widget in Trade States would show up for both sides even if only one side had states to trade
- Fixed Highlighting for Fix Unproductive Building tutorial
- Kuril Islands are all connected with adjacencies
- Removed unneeded text in Protectorate Concept
- Fixed flickering bug with mobilization and conscription Vfx
- Added a timeout to the "Renowned Playwright" modifier
- Domingo Sarmiento is now properly marked as born in 1811
- Historical interest group leaders should not spawn for interest groups that have chosen different ideologies.
- Switched the event options in the Hippopotamus event
- Fixed an issue with dynamic country names that would crash the game in non-graphics mode
- Fixed a typo on the description for Electrical Generation tech
- Removed `USE_TRAVEL_NETWORK` and `FORMATION_TRAVEL_SPEED` defines. The latter didn't do anything if the former was active (which is the default), and disabling the former would most likely cause unsavory results as it was meant as a debugging facility
- Buttons in the Exploiting the Amazon JE have clearer tooltips
- Fixed spelling of Ecuadorian culture[2]

## References

1. ↑ Forum: [Victoria 3: Update 1.6 "Blackcurrant" is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1626425), 2024-03-06.
2. ↑ 2.00 2.01 2.02 2.03 2.04 2.05 2.06 2.07 2.08 2.09 2.10 2.11 2.12 2.13 2.14 2.15 2.16 2.17 2.18 2.19 2.20 2.21 2.22 2.23 2.24 2.25 2.26 2.27 2.28 2.29 2.30 Patch note mistakenly added from 1.5, no change between 1.5 and 1.6
