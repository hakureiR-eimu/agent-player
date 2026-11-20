---
title: Patch 1.1
source: https://vic3.paradoxwikis.com/Patch_1.1
pageid: 3544
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
**Patch 1.1.0**, aka "Earl Grey", was released on the 2022-12-05[1] with the checksum *0d2e*.

## Features

- Reworked Morale to inflict a base loss for every round of battle, modified by the difference in casualties inflicted between the sides as well as various other modifiers
- Reworked Legitimacy to provide bonuses and penalties to countries at different Legitimacy levels
- Added a new Legitimacy modifier based on Votes in Government
- Replaced Legitimacy Penalty from Government Size with a Legitimacy Penalty from Ideological incoherence
- Treaty Ports will no longer function if the owner's Power Rank isn't greater than the market owner's, ensuring Great Powers cannot use them to get access to the markets of other Great Powers

## Balance

- Rebalanced Legitimacy across all Laws
- Added Authority bonus to High and Very High Government Wages
- Added Morale Recovery and Power Projection bonus to High and Very High Military Wages
- Added Power Projection penalty to Low and Very Low Military Wages
- Lowered Training Rate penalty for Very Low Military Wages
- Lowered the positive and negative approval from Government/Military Wages
- Buildings will now only raise wages if they are either competing for wages or are below their minimum wage target; the target is based on employees' Expected Standard of Living to prevent too much active radicalization
- Building wage targets are lowered in unincorporated states (e.g. colonies) and for discriminated pops
- Laws that restrict cultural / religious tolerance now give a decrease to radicals and increase to loyalists from accepted cultures / religions * the more restrictive the law, the higher the effect
- Pops in Unincorporated States now have their voting power reduced according to current Incorporation level
- Mass migration now only targets incorporated states, to avoid colonies being the main target of mass migration rather than e.g. the New World
- Unincorporated states now have a lower expected standard of living than incorporated states
- Rebalanced potential Oil and Rubber deposits around the world
- Rebalanced Power Plant production method
- Reduced the impact of Artillery Commander traits
- Rebalanced Port production methods to (generally) increase Convoy production
- Rebalanced technology unlocks for potential Port levels to increase sizes over time
- Replaced Cape Colony with Persia as a recommendation for the Learn the Game objective
- USA no longer immediately starts losing its Interest in the Great Plains on game start
- Additional production Rubber Irrigation PM added
- Revolutions will now always lose some amount of war support, even when they're out of troops, so they cannot go on forever

## AI

- AI will not begin unifying Canada or Australia until Pan-Nationalism is researched
- Australian and Canadian confederation no longer forces the annexation of a player
- AI acceptance for white peace now increases over time the longer a war goes on
- AI is now less inclined to pursue annexation of subjects with whom they have good relations
- AI is now more willing to settle wars that are going nowhere with a white peace
- AI now also takes into account bankruptcy when considering peace desire, neutrality and confidence, not just debt level
- AI will now properly stop enacting a law to avoid revolution if it calculates this to be in its best interest
- AI will now properly use its investment pool when it can cover the entire construction cost, despite being in deficit
- Fixed native uprisings not mobilizing due to not being able to calculate their conscripts' power projection
- Improve the AI's understanding of when it should produce more military goods of a certain type
- Make the AI more interested in switching to more productive PMs, and less interested in switching to less productive ones unless there is a very good reason to do so
- Great Powers are much more likely to declare an interest in Arabia while the Ottomans are trying to reclaim Syria
- Liberia now begins independent, to discourage US colonization of Africa and to better reflect Liberia's de facto situation
- Changed incorrect check in Powerful Protectors that compared army size to country rank instead of army size
- Fixed some cases where the AI would use the wrong define for computing heuristics

## UI

- Improves the Pop Details Panel with tabs and Consumed Goods
- Added a Good's current Trade Routes to the Goods Panel's Market tab
- Added a delay to opening map tooltips. The amount of delay is controlled by a new setting.
- Added pop consumption goods needs display to Economy and Consumption pop tabs
- Added "show more" button to the Population panel to display all categories, inspired by the "Complete Pop List" mod by Ron Swanson
- Make the Construction Queue building list items say their State as well as making the list items smaller, inspired by the "Construction Queue with States" mod by Seppiya
- Multiple changes to which notification types display as Toasts (middle of the screen) versus Feed (bottom right)
- Show usable manpower involved on each side of a battle in addition to the number of battalions
- The volume for Music Stingers and Background Music can now be adjusted independently in the Audio Settings screen
- Inactive Treaty Ports are now displayed as such, with a tooltip explaining why
- Active Production Methods are now non-clickable and more distinguishable from the rest
- Game rules are now visible even before you select a Player Objective in the New Game Interface
- Moved the Timed Modifiers higher up in the change Production Method tooltip
- The amount of unrealized taxes are now displayed in the country budget tooltip
- Transfer of Power information is now displayed better
- The outliner now shows the number of currently active unpinned Player Objective challenges and Journal Entries
- Update to the construction queue’s page buttons visuals
- Establish Trade Route Map List Panel can now sort markets alphabetically by name
- Updated text for convoy raiding order to better represent information to the player
- Right-align the Consumption tax cost in the add Consumption tax menu for better readability
- Removes decimals from Legitimacy modifier types

## Content

- Added decision to cancel surveys of Panama/Suez
- Added event greatly weakening the Shogunate if Japan is forced to open its market
- Skyscraper now has a Trade Nexus base PM as an option for Bureaucratic Nexus
- Changed the requirement for completing the Reading Campaign to only require 95% literacy.
- Made several repeating events fire less often
- Fixed various issues in 1848 content
- Expanded the name lists for North German, South German, North Italian, South Italian, and Thai cultures
- Added some variant unifier flags for Germany and Italy
- Germany's default flag is now the Black-Red-Gold tricolor
- Italy's default flag is now the Green-White-Red tricolor without the House of Savoy's coat of arms
- Conservative IGs such as the Landowners, Devout and Rural Folk now tend to be significantly stronger at the start of the game in most countries
- Fixed the large starting unemployment in several Decentralized Countries
- Reduced Hokkaido's population to historical levels
- Made events that strengthen abolitionism rarer in the USA
- Manifest Destiny decision now requires an Interest in the Pacific Coast
- Manifest Destiny now provide claims on the colonized split states of Mexico
- Alaska Purchase decision now has significantly easier requirements
- American West Expedition is now significantly easier to complete
- "The Dream" event for gold rushes no longer has one unequivocally better option
- Sub-Saharan African states now have more cultural homelands assigned to them
- Amended Great Qing flavor text to better fit its historical situation
- Reduced the urban center requirements for the Underground Railway Journal Entry from 30 to 20, and made the completion goal valid for cases where the country's capital and the country's market capital are in different states
- People's Springtime is now correctly triggered by a powerful Radical IG, not only through insurrection
- tanzimat_events.10 now requires Napoleonic Warfare
- migration_laws.6 now displays pop names correctly
- "A Tale of Hope" event no longer targets a null state
- "An Economic Prison" event no longer applies trade route effects to isolationist countries
- "Devout Scandal" no longer has a sentence starting with a lowercase letter
- "Elevating Our Situation" journal entry has been made less convoluted
- "Expand the East Indies Administration" is now visible whenever the Dutch East Indies exists
- "Mutually Beneficial" event now applies the correct popularity modifiers.
- "The Rogue Imperialist" event can no longer cause a diplomatic incident with yourself
- Austrian-formed Germany no longer has the Matter of Hungary Journal Entry
- Fixed many issues in cultural_homelands_events
- China now re-incorporates the states of the Heavenly Kingdom upon defeating the rebellion.
- Commanders can no longer cheat with their own spouses
- Defeat in the Opium Wars will now remove opium bans and opium ban Authority cost
- Countries with the Free Trade law can now remove trade bans but not add them
- Doctrine of Lapse decision for the British East India Company now has a proper cooldown of two years
- Elitist ideology now has a stance on theocracy
- Ethiopia now requires at least two fully controlled states to form
- Poland now requires only 5 Polish states to form rather than 7
- Event "Campaign Financing" now requires active parties to fire
- Expand Productive Building tutorial challenge now tests if the player can actually expand the target building an additional level before selecting it as a target building
- Italian nations classified as minor powers may now participate in Risorgimento
- Efficient Home Affairs modifier is now actually efficient
- Made the "Good Word of the Revolution" event less spammy
- Mustard Gas no longer permanently applies modifiers to states
- North German Federation, South German Federation, and Italy are now formable if all completion requirements are achieved before Nationalism is researched
- Numerous law enaction events will now fire properly, and not auto-cancel
- Paying for school supplies now costs bureaucracy instead of benefiting it
- Philip Sheridan's birth date is now correct
- Presidents in Republics now die less frequently
- Railway research bonus in the Atmospheric Engine tech event now requires all railway prereqs to be unlocked
- Resolved edge case where native_resettlement.4 has no options
- Resolved issue with error spam when China was annexed
- The Free States of America's name now shows up in its secession event
- The Ripper can no longer be a child or toddler
- Tooltip for "How to Reform your Government" tutorial will no longer flood the error log
- West America expedition now removes event tracking variables properly
- Bureaucracy tech no longer uses the same localization key as bureaucracy concept

## Modding

- Cleaned up defines to remove unused ones
- Renamed some defines to be more precise about what they do
- Exposed several parameters of character life expectancy calculation as defines

## Major Bugfixes

- Fixed font atlas not notifying the map system when textures where recycled, leading to garbled map names especially frequent in Chinese, Japanese, and Korean languages
- Enabled new logging system that prevents log files from growing too large
- Fixed overflows in politics related math that could lead to weird values for political strength of pops, or amount of votes in elections, and other such things
- Fixed an issue that led to most characters having a natural lifespan in excess of 90 years
- Fixed computation error that made it possible to have two highly profitable routes trading the same good back and forth between two markets
- Fixed an issue that made the "force open market" and "ban slavery" wargoals forbid the affected country from changing policy for 60 years instead of 60 months
- Fixed an overflow in gold reserves limit
- Fixed a bug that would cause garrison units to not recover morale
- Ensures that angry IGs always leave the government if able to do so, even when in a party
- Fixed an issue where tariffs would incorrectly be paid out to market owner from tariff-exempt trade routes
- Revolutionary and seceding countries can no longer engage in colonization until the civil war is over
- Discriminated Pops now have their Political Strength reduced by 90% as intended
- Pops in Unincorporated States now get a 50% penalty to Political Strength as intended
- Battalions are now assigned to battles in order of descending usable manpower (including Morale)
- Countries can no longer make progress on colonies in regions without maintaining an active Interest there
- Subjects no longer have to ratify a peace deal if their overlord does, even if they have diplomatic autonomy
- Expedition leaders are now always properly returned to service upon expedition conclusion
- Expeditions no longer automatically fail after turning back on the Niger River
- Expedition modifier for expedition taxes now removed upon expedition end
- Fixed general travel exploit that would allow to teleport generals by alternating orders towards the same destination
- Fixed a general travel duration exploit that was possible when giving several orders targeting different destinations, causing GENERAL_TRAVEL_OVERSEAS_SCALE to sometimes not be applied
- Fixed a bug where making a general return to a previous location during travel would sometimes apply GENERAL_TRAVEL_OVERSEAS_SCALE
- Military buildings are now unable to provide more Battalions or Flotillas than their level can support
- Fixed the bug when Cut Down To Size wargoal would liberate conquered states regardless of when they were acquired
- Fixed a bug that would cause only one admiral to be able to defend against naval invasions
- Fixed a bug that allowed an admiral to be able to naval invade a state that has no passable coastal provinces controlled by the enemy
- Fixed an issue that caused secessionist countries to not being able to be targeted by diplomatic plays even after they win the secession war
- Fixed a bug where Treaty Ports could give you access to markets in states outside the same state region
- Fixed bug where market access was not updated in states split due to ceding a Treaty Port or gaining independence
- Fixed the bug when status of convoy raiding wasn't displayed on the map nodes
- Combat unit allocation between commanders is now recomputed if a commander loses their role
- Failed or timed out Journal Entries won't be triggered by an Objective again unless marked as repeatable
- Fixed an error that caused the building tooltip to display incorrectly and produce error log spam when the building was built in a state with an apostrophe in its name
- Fixed commonly occuring crash caused by offscreen GUI VFX not being cleaned up properly
- Fixed crash when running out of cloud storage space for save files
- Fixed OOS for Elections when hot-joining
- Fixed a crash that would happen when the same peace deal is accepted at the same time in multiple wars
- Fixed crash when listing saves
- Fixed crash arising from cultural_homeland_events.1
- Fixed crash during commander generation
- Rebellions/uprisings and civil war countries no longer have rebellions

## Minor Bugfixes

- Fixed issue with displaying country names for civil war countries
- Ensures the correct number of Battalions are reported for both Regulars and Conscripts on various panels and tooltips
- Death notifications no longer fire upon the retirement of a politician
- Fixed an issue in prediction tooltips where Peasant goods consumption was incorrectly calculated, causing price predictions to be wrong for certain goods
- Fixed an issue where price predictions for pop-consumed goods would get increasingly inaccurate the longer the game went on due to old data not being properly cleared
- Fixed flickering map mode in the culture panel
- Fixed front map markers not showing up correctly in Observer Mode
- Fixed overlapping text of the options in the Sway Country Panel
- Fixed overlapping text on the Nation Formation panel to not overlap
- Fixed text overlapping and alignment issues on the War Panel
- Fixed the Diplomatic Play title text to not overlap the flags when very long
- Fixed 'You' label being visible for other players in the War Panel in a Multiplayer game
- Fixed invalid diplomatic relations expandable tooltip
- Fixed wrong scope provided to on_sway_offer_rejected
- Added missing localization for is_direct_subject_of
- Fixed a missing texture that would appear in the war tooltip when the initiator of a diplomatic play had obtained all of their declared war goals
- Fixed an issue that made it possible to change government or military wage rates when the country wasn't actually paying any government / military wages
- Fixed incorrect text that would appear in the war tooltip when either side of a diplomatic play had obtained all of their declared wargoals
- Fixed notifications accidentally appearing twice when closed
- Fixed typo in Pop Properties tutorial lesson
- Fixed missing text for Annex Subject Diplomatic Play Tooltip
- Korean officers now wear clothes
- Male Academics and Capitalist pops no longer carry parasols
- Dinka slave pops are now properly naked
- The final fallback for character clothing is now peasant's clothes instead of a birthday suit
- The Confederate States of America should now always be called such during the American Civil War
- Taiping Rebellion war name is now properly localized
- Corrected spelling issues with Australian hubs and Theodore Roosevelt
- Commanders-in-Chief now use the correct Character background on their Character Panel
- Fixed unlocalized string in the load game button in the multiplayer game over screen
- Resolved several typos in the country flavor text for Parma, Modena, and Krakow
- Fixed spelling of "Van Diemen's Land", "Concepción", and "Legazpi"
- Return State Goal now utilizes correct infamy define

## References

1. ↑ Forum, [Victoria 3 Update 1.1 "Earl Grey"](https://forum.paradoxplaza.com/forum/index.php?threads/1560487)
