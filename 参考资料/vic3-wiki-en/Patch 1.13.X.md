---
title: Patch 1.13.X
source: https://vic3.paradoxwikis.com/Patch_1.13.X
pageid: 9445
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
**Patch 1.13.X** are all patches beginning with 1.13.

## 1.13

Main article:
Patch 1.13

## 1.13.1

Patch 1.13.1 was released on 2026-04-29[1] with checksum *ccf2*.

### AI

- Fixed an issue where the AI would create a lot of tiny fleets. Also improved the behaviour for armies so AI should have less tiny armies
- Fixed a bug where the AI would not disband empty formations it did not have a use for
- Improved AI handling of obsolete ships, including cancelling obsolete ship constructions and more aggressive decommissioning of useless ships
- Fixed a bug where the AI would generate way more templates than it needed and did a general improvement pass on how the AI designs ships to produce more sensible templates
- Countries no longer start naval invasions using marines without a general
- Fixed a bug where the AI was constructing new ships they did not have the necessary crew for
- Added triggers for the AI to get rid of Merchant Navy if they have sufficiently high tech unlocked

### Balance

- Reduced Literacy growth from 0.5% per week to 0.1% per week, as it was way too fast previously
- Reverted the change to several Land Reform law such as Tenant Farmers that added minimum subsistence employment. We will experiment with bringing this back when the UI and mechanics support it properly.
- Reduced the armor values of late game Capital Ships, moderately increased the damage of late game Cruisers, as damage was far too outclassed by armor from Modern Ironclads onwards
- The fraction of Coup Strength formerly calculated off of the number of units commanded by a General or Admiral is now calculated off of that commander's rank divided by the sum of the ranks of all commanders of that type
- Added two textile mills to Ile de France at game start, to discourage French uprisings on account of their threadbare clothes they can’t afford to replace
- Reduced movement radicalism gain from the Geheime Staatskonferenz for Austria
- Reduced movement radicalism gain from the Divided Monarchists Journal Entry for France
- Increased the threshold for the Hungry Forties Journal Entry to fire

### Art

- More historical Japanese characters have had their specific character DNA for their appearances added
- Fixed an issue where pre-restoration Officers pops could wear peasant clothing pre-Restoration if the player had no DLCs
- Fixed blockade graphics not being shown on the map

### Interface

- Made the Strait map marker show up less frequently in the Default map mode
- Removed the broken commander buttons from the Naval Invasion planner, we are planning to improve the general functionality of this feature in future hotfixes
- Improved the missing crew alert by adding info that ships need to go to port to get new crew. This new part will be displayed in English only, until next week or so.

### Performance

- Significantly increased AI performance for handling diplomatic plays
- Improved AI performance for handling armies

### Bugfixes

- Fixed the stranding of armies due to fleets forgetting they were transporting them because they got merged with another fleet. As a backup and to fix saves, we teleport any currently stranded armies at sea to their supply hub.
- Fixed an issue that allowed countries to start or join diplomatic plays in a region even if they didn’t have the necessary interest tier level.
- Stopped drowning marines when you merge two fleets. Instead allowed them to be attached to the other fleet as it was intended.
- Fixed a bug where unraised irregular infantry could not gain any supplies
- Fixed a bug where fleets could return to their home HQ when stationed in other HQs or states
- Fixed ‘Abandon Piracy’ treaty not preventing ‘Piracy’ missions from still occurring
- Fixed an issue where buildings which only employed very small pops would ignore them and dump their wages making them unable to hire anyone
- Potentially fixed an issue that caused a rare bug which would cancel the construction of naval administration buildings
- Fixed an issue that could print errors when hovering characters in the "Honorable Restoration" Journal Entry
- Fixed Sweden owning Livestock Ranches in Kyoto
- Removed deprecated Man-o-War good from the USA-Texas starting treaty
- Removed the Armstrong Ironclad Prestige Good as it can no longer be produced
- Fixed a number of localization issues

## 1.13.2

Patch 1.13.2 was released on 2026-04-30[2] with checksum *45ca*.

### Improvements

- Military maintenance will now always be deducted before any other naval construction can happen, including supply ships. This avoids the issue of ships suffering maintenance penalties if you set the priority to allocate too little capacity for the category.

### AI

- The AI is no longer willing to just give away states that grant control over a strait
- Fixed several more cases where the AI could get blocked from launching naval invasions
- Made the AI less interested in hunting pirates while at war

### Balance

- Power bloc members now generate involvement the same way subjects do
- Moved Reinforced Fortification Production Method unlock for Naval Fortifications to Breech-Loading Artillery. Previously was on Concrete Fortifications.

### Interface

- Restructured the layout of the action buttons for Formations and what goes in the context menu and what goes outside of it
- Hid ship modifications tech unlocks without DLC enabled
- Supply ships should no longer count as military ships of a fleet while engaged in a battle
- You can no longer set strait access restrictions when you have the strait open to everybody. Previously this would reset when you changed settings.

### Bugfixes

- Fixed an issue where supply ships being raided would permanently join the raided fleet if the battle ended abnormally, inflating costs and power projection
- Fixed an issue causing the game to not tell the player why they or another country can't join a diplomatic play as a result of insufficient interest in the region
- Fixed an issue where exiling an agitator would not remove them as commander
- Getting a toll exemption treaty now only affects the target country rather than all
- Fixed a softlock in the Honourable Restoration Journal Entry caused by a non-Tokugawa shogun
- The Emperor abdicating will no longer break the Honourable Restoration Journal Entry
- Fixed an issue that prevented opium_wars.4 from ever firing
- Kameoka (Kyoto mining hub) is now properly placed, connected and localized

## 1.13.3

Patch 1.13.3 was released on 2026-04-30[3] with checksum *654a*.

### Improvements

- Ordering a fleet with insufficient capacity to transport an army will now have it make multiple trips to get the entire army to its destination. Moving any queued formations will result in them not being transported, while moving/giving a mission to the transporting fleet will cancel all further planned transportations.
- There is a known issue: if an army is transported to a state that becomes invalid (e.g. when a state changes occupation) - the fleet will get stuck mid-ocean. Sending the fleet on any mission to any sea node fixes the issue, and the fleet can be stationed in any state afterwards to disembark the transported army.

### Balance

- Cut the infamy cost of Threaten Naval Hostilities in half

## 1.13.4

Patch 1.13.4 was released on 2026-05-07[4] with checksum *7564*.

### Improvements

- When barrack levels are inherited from other countries, those units are no longer allowed to be merged into formations that have existed for more than a few days, and thus will no longer disrupt carefully managed unit compositions. Instead, they will form 1-2 new armies named after the country of their origin (so 'French Army' if you took barracks from France).
- When armies are auto-split for transport they will now be proportionally split along unit groups to prevent sudden org loss from unbalanced formation chunks
- Magnate noble titles will now only display if their country can reasonably be expected to have a titled nobility

### AI

- Fixed an issue where the AI was failing to merge fleets and marine units at sea, resulting in many tiny formations
- The AI should now properly calculate when its fleets need to return home to repair or take on crew
- The AI is now less keen on intercept and protect supply missions against enemies with inferior navies

### Balance

- Increased the base command limit for formations without commanders to 20, so to better handle multi-trip transport without organization crashing
- Merchant Marine input scaling and World Market Hub routing now correctly uses travel distance rather than number of sea nodes to calculate additional MM input and best trade route. This should fix the issue with no trade going through Suez and also significantly alleviate the over-demand of Merchant Marine making trade unprofitable.
- Reduced the time it takes to recover organization, 0% to 100% now takes 100 days (down from 200)
- Changed the minimum Supply threshold under which a formation receives penalties to 25%, was 50% before. This means formations can fight at full effectiveness for longer before running into trouble.
- Increased Supply Capacity for all land-based units significantly. This, together with the change above, should make them a bit less susceptible to fluctuations in Supply availability, e.g. while Supply Ships still need to be assigned to them.
- Signing a "Foreign Investment Rights" treaty now requires an interest tier level of 2 or higher
- Springtime of the Peoples revolutions will now require the capital to be in revolt, with at least 25% Revolution progress
- The Springtime of the Peoples will now require a European major power to have their capital in revolt, with at least 25% Revolution progress
- The Divided Monarchists Journal Entry will cause the Revolution clock to progress faster whilst it is active (Voice of the People)
- The Divided Monarchists Journal Entry for France now requires a civil war to make at least 25% progress before failing (Voice of the People)
- Revolution state selection is now more strongly targeted towards states with high clout from insurrectionary Interest Groups and high Turmoil

### Art

- Added model of Shibu Uchiwa (Japanese traditional paper fan) and updated idle poses for female characters
- Added child ideology icon

### Content

- Added Sinosphere Tradition to Ryukyuan Culture

### Interface

- The military panel interface is now far more compact and displays more information about units at a glance
- Grouped "Insufficient Ship Crew" alert into one
- Added missing text for when an agitator would not start or join a political movement if invited

### Bugfixes

- Fixed a bug where fleets could get stuck in the Bering Sea and Western Polynesian Sea
- Fixed a bug where transporting fleets could become 'stuck' at sea if the transport destination changed owner or controller, requiring a manual issuing of orders to get them moving again. They will now simply abort the mission and go home.
- Fixed an issue where formations could get stuck during a transport mission
- Fixed armies with a supply hub in Schleswig-Holstein not being able to build supply routes through the port
- Fixed an issue where the button to pause supply ship construction was disabled if there were no military ships in the queue
- Unraised conscripts no longer count against transport capacity. It is also no longer possible to raise conscripts (or continue raising conscripts being raised) when an army is overseas or in transit via ship, to prevent conscripts from suddenly appearing on the other side of the earth without needing transport.
- Fixed armies not being cross Sinar from East to West
- Fixed supply penalties from goods shortages not being applied
- Fixed a bug where market access price impact (MAPI) would not update after switching from traditionalism
- Fixed a bug where units could be recruited to and disbanded from formations being transported by fleets
- Clicking the back button after clicking a military formation in the military panel now re-opens the military panel
- Fix embarked armies not disembarking when target became invalid (for example state got occupied)
- Fixed world market access ignoring blockade penalties in some cases
- Fixed an issue that could prevent fleets from getting to resupply despite having enough supply ships
- Fixed ship construction queue entries getting stuck at 99.99% and "throttling down" before finishing
- Fixed a bug where you could be involved in a diplomatic play without having a high enough interest tier to join it
- Fixed an issue where armies would continue to advance the front despite having no advance order
- Fixed a case in which multiple characters could get the Emperor of Japan trait if one abdicated
- Fixed a bug where certain states cannot be fully colonized using frontier colonization, for instance Australia
- Added a sufficient amount of Naval Administrations to Russia
- Fixed a bug where company-owned buildings would not auto downsize despite standing empty for extended periods of time.
- Fixed an issue where ship models visually started travelling from their HQ to the current fleet location after loading a game
- Fixed the Retire from Office interaction possibly resulting in the same character promptly being set as the new leader
- Fixed an issue that could print errors when hovering characters in the "Honorable Restoration" Journal Entry
- Character career lengths are now in a random span of days, not years, so they don't retire in bulk on January 1st
- Fixed Abdicate Monarch failing to make heir the new ruler
- Fixed a possible null scope in coups that could appear if a commander was unassigned
- Fixed an issue in the trigger of "Discord within the [interest group]"
- Fixed an issue where an independent India could keep its colonial cultures in cases where her languages were changed
- Fixed a bug where the AI would be unable to build ships in some cases where it did not already have ships under construction[5]

## 1.13.5

Patch 1.13.5 was released on 2026-05-12[6] with checksum *547c*.

### Features

- Added Ship Crew Experience. Ships will now gain experience while out on a mission, while participating in battles and when sinking ships. Experience will decay over time if a fleet is sitting idle in port. By accruing enough experience ships will increase their Veterancy Rank, which provides a positive modifier to accuracy, critical hit chance and readiness gain, with higher ranks providing larger advantages. The baseline accuracy bonus and critical hit chance for all ship types has been adjusted downward to compensate.
- The "Jeune Ecole" and "Capital Fleet" Navy Model Laws now also provide a starting experience bonus to ships

### Improvements

- The supply ship allocation percentage is now a hard cap on how much ship construction is allowed to be allocated to supply ships
- Certain treaties now allow joining diplomatic plays again regardless of interest tier: alliance and support independence as well as guarantee independence and defensive pact when trying to join on the defense

- Added 'station in state' to right-click menu for military formations, also supports overseas stationing

### AI

- The AI is now less gung-ho on supply ships and will not drive their economies to ruin endlessly building them
- Made a substantial pass on AI ship construction logic to make them more proactive about replacing obsolete ships gradually, instead of all at once
- Added better logic for AI navy composition, governed in the AI strategies database files
- Fixed a bug where the AI would select far too small fleets to transport their armies, resulting in the army being split into a myriad tiny stacks
- Fixed an issue where the AI was unable to ever pass Jeune Ecole
- Made the AI less willing to select event options that would increase Movement Activism if it is threatened by a revolution
- Made the AI more inclined to expel agitators with traits that increase Movement Activism
- Fixed a bug where the AI could get stuck on very low authority while unable to reduce authority spending

### Balance

- Halved base literacy growth further, from 0.1% to 0.05%
- Abolishing the Edo Status System now requires Japan to abolish Subjecthood
- Public Schools now grant literacy growth per level of institution
- Philosophical Pragmatism, Central Planning and Analytical Philosophy technologies now grant literacy growth rate
- The Political Concessions amendment will now cost Authority proportional to its strength, and will not be available during negotiations if the country has insufficient Authority
- Bakufu is now required to enact Shinsengumi
- Made Iron-reinforced Hull consume some Iron instead of purely Hardwood
- Reduced the movement attraction impact caused by several pulse events - "The Flight of the Battleship [name]", "Antiquated Words", "Confusion and Delay", "Political Imprisonment", and "Cause Without a Rebel"
- Increased the Movement Activism effect of Political Concessions
- Ending Sakoku via the button in "The Locked Country" will now increase the Activism of the Sonnō Jōi movement equivalently to if the law was enacted normally
- Changed Itō Hirobumi's ideology from Market Liberal to Modernizer leader and interest group from Rural Folk to Intelligentsia
- Added a sufficient amount of Naval Administrations to Russia
- Reduced the immediate approval decrease from selecting the option to reconsider Sakoku in The Morrison Incident event

### Art

- Added traditional Japanese female clothing (haori) with additional patterns and color variations to the game
- Japanese characters with modernising ideologies will now adopt Western clothing prior to the Restoration
- Japanese characters without modernising ideologies will no longer adopt Western clothing if the Restoration concludes with a Bakufu victory

### Content

- Added Ansei Great Earthquakes event for Japan.
- Added events for the Taikyo Proclamation and finishing Shinbutsu Bunri and Elevate Buddhism
- Added a decision for Japan to found a modern secret police force based on the Shinsengumi
- Added a decision for Japan to abolish the Edo status system upon either concluding the Meiji Restoration or researching Human Rights
- Extended effects of and added custom tooltips for some Shinto conversion effects
- Added game concept tooltips for Japanese Religious concepts
- Made the Abolitionist ideology available to the Armed Forces
- Made the Devout ideology available to the Devout
- The Legitimist ideology is no longer available to the Petit-Bourgeoisie, and is now available to the Armed Forces
- Made the Social Democrat ideology available to the Petit-Bourgeoisie
- Added Sinosphere tradition to Ryukyuan culture
- Changed Jairam Shivji's ideology from Royalist to Moderate
- Changed Tomás Cipriano de Mosquera's ideology from Republican to Modernizer
- Changed Lúcio Mansilla's ideology from Radical to Republican
- Changed Hasan al-Alawi's ideology from Land Reformer to Moderniser
- Changed numerous Landowners character ideologies from Royalist to Moderate
- Changed Manuel Ignacio de Vivanco's ideology from Royalist to Authoritarian
- Changed José Relvas's ideology from Republican to Radical
- Changed Manuel Isidoro Belzú's interest group from Armed Forces to Rural Folk
- Changed Euclides da Cunha's ideology from Republican to Positivist, and interest group from Rural Folk to Intelligentsia
- Changed Custódio de Melo's ideology from Radical to Royalist
- Changed James Longstreet's ideology from Radical to Liberal
- Changed Arturo Fernández Vial's ideology from Social Democrat to Reformer
- Changed Flavio Alfaro's ideology from Radical to Liberal
- Changed Francisco Linares Alcántara's ideology from Radical to Liberal
- Changed Victor Bonaparte's interest group from Landowners to Petty Bourgeoisie
- Changed Gustave Cluseret's ideology from Radical to Republican
- Changed Otto von Bismarck's ideology from Royalist to Authoritarian
- Changed John French's ideology from Market Liberal to Moderate
- Changed numerous Armed Forces character ideologies from Jingoist to Moderate
- Changed Peregrine Maitland's ideology from Jingoist to Ethno-Nationalist
- Changed Teofil Lapinski's ideology from Radical to Republican
- Changed Santos Acosta's ideology from Radical to Liberal
- Changed Ricardo Gaitan's ideology from Jingoist to Liberal
- Changed Thomas Bugeaud's ideology from Orleanist to Authoritarian and his interest group from Rural Folk to Armed Forces
- Changed Felipe Salaverry's interest group from Armed Forces to Landowners
- Changed Rafaël Franco's ideology from Social Democrat to Corporatist
- Changed Jefferson Davis's interest group from Armed Forces to Landowners
- Changed Victor Hugo's ideology from Republican to Abolitionist
- Upon reforming the Daimyō into the Kazoku as Japan, new Daimyō will no longer be generated
- Changed Dayananda Saraswati's ideology from Feminist to Reformer
- Changed Heinrich Clam-Martinic's ideology from Royalist to Reformer
- French Legitimist, Bonapartist, and Orleanist revolutions will now have white, dark blue, and blue map colours respectively
- The Heavenly Kingdom will now change names if it's State Atheist or no longer a Kingdom
- Renamed "Restoration: End Sakoku" to "Restoration: Achieve Recognition", requiring Japan to become a Recognised Country

### Interface

- The Company panel has received an update, with added filters and an overall improved layout
- Moved the Previous Investments tooltip to be more visible under a label in the Construction panel
- Added a list of characters to the population tab of the state information panel containing the characters who call that state their home
- Matched the Army upkeep tooltip layout to the new Fleet upkeep tooltip
- Added subtabs to the Population tab on the State panel to reduce how much you have to scroll to see the Characters and Pops lists
- Added a proper Promote Commander tooltip to the promote button in the Character panel
- Grouped "Insufficient Ship Crew" alerts into one
- Added map notifications i.e. floating text messages when when ships are constructed/repaired/retrofit
- Updated flagship button tooltip to show reason why a ship cannot be designated
- Improved the tooltips of the Purveyor of Progress Journal Entry (Pivot of Empire)
- Added missing text for when an agitator would not start or join a political movement if invited
- Adjusted the tooltip of the "Everyone Disliked That" achievement to match its requirements

### Performance

- Optimized supply computation
- AI countries will recruit Commanders on-demand instead of keeping a pool of them around
- Optimized UpdatePartySupport ticktask
- Cached modifier names for re-use
- Country sea node range distance now updated in parallel
- Precomputed Ideology Law Stances
- Cached AI's willingness to prepare for war
- Cached some expensive Diplomatic Play variables for the AI
- Improved performance for AI evaluating Diplomatic Actions

### Modding

- Added new scopes to can_join_side_in_diplomatic_play and can_start_diplomatic_plays_against

### Bugfixes

- Fixed formations not receiving supply penalties from production shortages
- Fixed an issue where armies could get stuck in exile
- Fixed Market Access Price Impact (MAPI) not updating when incorporating a state, researching technology or switching from Traditionalism
- Fixed Carlist Spain missing supply centers for their armies
- Fixed a bug where the wrong character could get retired by the career end system, resulting in issues such as Metternich retiring before his JE is concluded and interest group leaders retiring shortly after assuming their new job
- Fixed an issue that prevented Chartered Company-type subjects from ever being able to be annexed or have their autonomy reduced
- Fixed armies getting stuck in some island states, including after invading certain island states
- Fixed fleets getting stuck at sea when their transport target becomes invalid
- Fixed a bug that could lead to the Iwakura Mission instantly unseating the Emperor by enacting Republic
- Fixed a bug where armies were unable to merge outside of its home countries borders
- Fixed a bug where, after the end of the war, the country could no longer track formation spam
- Fixed an issue causing the game to not tell the player why they or another country can't join a diplomatic play as a result of insufficient interest in the region
- Fixed a bug where the Japanese Daimyō could duplicate without limit upon a secession or revolution
- Fixed an issue where a coup could remain if the commander executing it ceased to exist
- Fixed a bug where Strait wargoals would invalidate when the strait province is occupied
- Fixed a bug where we allowed you to decommission ships when a revolution is brewing
- Fixed an issue where colonial countries could occasionally get the wrong primary cultures
- Fixed an issue where ship crews could still be assigned from a state after its owner had changed
- Fixed the Retire from Office interaction possibly resulting in the same character promptly being set as the new leader
- Fixed a bug where locality calculations could go over 100%
- Fixed a bug where a fleet sometimes could not deliver units to Circassia
- Fleets from Gibraltar now properly travels through Mediterranean sea, instead of phasing through land
- Fixed multiple instances of broken tooltips in the Iberian Union Journal Entry (Iberian Twilight)
- Restoring King Miguel now causes the Reign of the Devourers Journal Entry for Portugal to invalidate (Iberian Twilight)
- Federating Australia now properly includes New Zealand
- Fixed an issue where Miguelist Portugal would have a default name, and French Legitimist revolutions would purport to be Miguelist
- Fixed several issues in coups that could lead to visible null scopes
- Fixed supply routes sometimes not following spline network correctly
- Corrected the name order of several Japanese characters
- The tooltip of The Imperial Sanction will no longer possibly mislead the player as to its outcome
- Fixed an unlocalised string in the triggers for whether a country is a Crown Land or not
- Finally captured and eliminated Henry Ford's mischievous clone
- Fixed an issue where "The Voice of the Nation" could have a null scope in its flavour text

## 1.13.6

Patch 1.13.6 was released on 2026-05-20[7] with checksum *48a5*.

### Bugfixes

- Fixed an issue where tolls were only looking at trade going to a world market hub state and not to other trade centers in the market area
- Prestige goods bonuses now apply to units in combat
- Fixed Interest Group leaders disappearing on change of government

## 1.13.7

Patch 1.13.7 was released on 2026-05-27[8] with checksum *f369*.

### Features

- Added the Kiel Canal as a constructable canal

### Improvements

- You can now negotiate treaties with countries you cannot 'reach', fixing issues such as Spain being unable to complete Hispanoamerica due to not being able to 'reach' Paraguay
- Fixed multiple issues where countries could end up paying very inflated sums for port connection merchant marines (aka busted an embezzlement scheme by the port cartels). We now instead calculate how much each country’s market areas have to purchase from other market areas and attribute a portion of the port connection shipping lane costs proportional to that share to that country as a fee that is paid to the market owner.
- Supply Ships now have proper 3D graphics, using troopship graphics and visually changing over time as you unlock better tech

### AI

- The AI now composes fleets according to certain desired roles, such as a main battle fleet or a fleet for raiding/piracy. Different fleets have different ship compositions and sizes, for example main battle fleets tend to get most of the capital ships and to be much larger than other fleets. Fleets will now focus on missions fitting for their composition. Capital ships won't be used for pirating activities.
- Did a major improvement pass on AI fleet mission handling to make it use its fleets in a more logical fashion both during war and peace
- The AI is now better at prioritizing important regions with a high strategic region score for assignment of a stance over less important ones, and should focus its power projection efforts on regions needed to complete certain journal entries, for example
- Fixed a bug where the AI could create invalid templates for some ship classes, resulting in those ship classes never being used
- The AI is now willing to keep some very obsolete ships around if they have a low enough number of ships in the class compared to their desired amount
- The AI will now decommission a limited number of obsolete ships per tick, to avoid overly aggressive mass-disbanding actions
- The AI no longer always fills every utility slot but will make a determination based on utility weight vs number of empty utility slots
- Fixed a bug where the AI was unable to downsize barracks due to attempting to downsize marines that didn't exist.
- Fixed a bug where the AI would be unable to downsize barracks due to disbanding units not flagging their building spending priorities as in need of an update.
- The AI now treats shortages much more seriously when they lack the ability to trade in order to solve them.
- Improved AI fleet and army selection logic for naval invasions and transportation
- The AI now more actively merges small temporary formations in the same location
- Fixed a bug where the AI would abort a naval invasion against an occupied state when taking back the state due to no longer calculating it as a valid target
- The AI will now limit the mission area size of its fleets based on how large they are, with smaller fleets having smaller mission areas
- Fixed a bug where the AI would refuse to defend itself entirely in a war against a much weaker opponent because of incorrectly applied checks intended to keep it from overcommitting against far weaker enemies
- Encouraged the AI to always press the "Promote National Identity" button whenever available in the South American "The \[Primary Culture\] Nation" Journal Entry
- The AI will now wait 100 days after sending a peace deal to send another, giving the player time to propose their own peace deal if the AI's offer isn't to their liking
- Made the Japanese AI more likely to pursue colonial laws if Japan has claims on Korea
- Upon an AI Japan completing Honourable Restoration with either an Imperial or Taikunate victory, Japan will annex a non-player Ezochi

### Balance

- Made Anarchist movements less rabid about seceding and encouraged them more towards attempting outright revolution, additionally they will no longer try to secede from nations with less than 5 states altogether
- There is now a 6 month cooldown on changing tolls and strait access settings. Like tariffs and subventions, this cooldown has a grace period of 7 days after changing the setting before the actual cooldown lock is applied, during which you can freely revert to the previous setting.
- Slashed toll rates in half, as they were rather excessive, particularly with single strait controller
- Reduced Merchant Marine cost for port connections and goods transfer treaties to more reasonable levels
- Blockade Efficiency is now calculated as (total blockade strength) / (total blockade resistance of blockaded states) instead of simply blockade strength divided by number of states, meaning that states with tiny resistances won't eat up a large fraction of your blockade strength
- Added a timeout to the Short-Term Tax Cuts Amendment
- Garrisoned armies can now only defend against naval invasions targeting their state or a neighboring state
- Did a major balance pass on utility modules to ensure they all have some use.
- Did a major balance pass on accuracy. Accuracy is now compared against both speed and visibility to determine hit chance, and accuracy modifiers are actually impactful, so capital ships will have a hard time scoring hits on torpedo craft.
- Torpedo craft are now the fastest ship types of their era, rather than the slowest.
- The Ottoman Empire no longer receives 100% Maneuvers in every Diplomatic Play for the duration of the "Tanzimat: Reclaim Syria" Journal Entry, instead it receives extra maneuvers specifically for the war against Egypt in the "Reasserting Our Authority in Syria" Event
- Rebalanced blockade strength and resistance values to make blockades more viable in the mid to late game
- Restricted the headquarters of Witkowitzer Bergbau- und Hüttengewerkschaft to Moravia, and added an Iron Mines potential to this state
- Updated several Journal Entries and Events to account for non-leader Politicians in the National Cast
- Luxembourg now starts the game with all technologies that the Netherlands have access to
- Reduced the assimilation requirements for The Government of Chōsen Journal Entry
- Increased the minimum level of turmoil permitted in The Government of Chōsen Journal Entry

### Art

- Added traditional Japanese umbrella (Wagasa) for Japanese pops to the game
- Added a flag to Buganda
- Adjusted province borders in the Sinai to more closely follow the shape of the Canal
- Ainu characters and pops in non-Japanese countries will no longer wear Japanese clothing
- Made the Empire of Korea slightly less purple

### Content

- The Taming the North Journal Entry may now be completed by the Ezo Government/Ezo Republic
- Added two events about the Ezo Republic. During a civil war, defeated Shogunate forces may flee to the island of Hokkaido, from where they may attempt to negotiate with the government to establish a Tokugawa fiefdom.
- Removing Subjecthood is now a requirement to abolish the Edo System, for both the Meiji Restoration Journal Entry button and the Decision
- If the Sonnō Jōi movement has the Shōjōi ideology, its activism will now increase for every year that Japan does not expel foreigners, to a maximum of 50%
- If the Sonnō Jōi has the Daijōi ideology, it will gain Activism for Japan being Unrecognised
- In the Boshin War, the side not in control of Matsumae Domain will now gain a wargoal to annex Ezochi
- Made The Korean Rebellion into an International Situation Journal Entry
- Limited Shinbutsu Bunri completion criteria to starting Japanese Homelands and expanded the tooltip to list them individually
- The "Manifest Destiny" decision can now also be taken when 40% or more of the Great Plains strategic region are controlled by the United States as an alternative to having an interest in the Pacific Coast strategic region
- Added a system which will track who the Japanese Taikun is, assign them a permanent modifier, and ensure they are an Interest Group leader
- The Suez and Panama surveys will now be visible for all Great Powers by default
- The Texan Statehood Journal Entry for the USA is now pinned by default, and adds Involvement in the Pacific Coast upon completion
- Added a complete condition to The Oregon Border Dispute for the USA gaining Columbia District as a subject
- Gave Cherokee culture its traditional homelands in the US South East which are removed as part of the Trail of Tears
- Gave Caddoan culture homelands in Oklahoma, Kansas and Nebraska. Removed their homeland in Alabama.
- Gave Muskogean culture a homeland in Alabama
- Reworked Japan's political party names
- Fixed an issue where a Naval Administration building in Constantine, Algeria was owned by Morocco
- Created a starting treaty between the USA and Oregon, to give the USA some starting Involvement in the Pacific Coast
- Added an alternate political party system for the Taikunate
- Added a starting Port to Washington
- Added several more Japanese noble last names

### Interface

- The selected mapmode is now the default mapmode which the game will remember and return to after you close panels that change the mapmode. You can also click the globe button next to the mapmode to lock it, which makes that mapmode stay selected even when panels are open that would normally override it. This means you can properly select and stay in a mapmode of your choice instead of having it constantly reset.
- Added wages to the maintenance cost prediction in ship designer
- You can now see what contributes to a country's share of the cost of a shipping lane in a market
- Allowed assigning commanders to formations without units
- Added paged construction for Military and Supply ships
- Removed empty unit type buttons on Unit Groups in the Army panel when there are no available Unit Types in that Group and added a tooltip
- Made it so the military and supply ship queue no longer show maintenance points spent to increase clarity
- Made it so that when keeping a particular region's panel open, that region will be highlighted on the map
- Added proper grouping and breakdowns to toll income and expense tooltips
- Adjusted tooltips for National Cast and Companies Filters by removing unnecessary ones and adding new relevant ones
- Fixed the wrongly greyed out Army button in the Invasion Planner when you had selected an Army
- Filtered out foreign shipyards from ship construction menu
- Added dropdown menus to Strategic Region Tiers to improve overall navigation
- Blockade and Power projection missions now display more relevant information when active or being selected
- Made sure the tab structure and shortcuts to the tabs are correct on the Fleet panel
- Added a dropdown to group Diplomatic Plays in the Outliner
- The support separatism action now shows which movement is being supported in the outliner
- We now sort entries in various calculation breakdowns
- Removed company charter information from tooltips that snuck in for non-owners of Charters of Commerce
- Removed veterancy level from ship type tooltip
- Fixed an issue where supply routes were shown when HQs were highlighted
- Added concepts for Diplomatic Relevancy and Strategic Adjacency
- Fixed misaligned Ruler Selection panel layout when having a mix of politicians and commanders
- Fixed a couple of typos and other minor localization issues

### Performance

- "Highest on the Highveld" event uses more efficient triggers and effects

### Modding

- Added script support for Variable maps
- Added `fleet_compositions` to ai_strategy which allows you to greatly control how AI fleets will look and behave
- Allowed can_queue_building_levels to accept script values
- Added new diplomatic play scope effect add_maneuvers
- Added fastdetection console command which gives all fleets a 100% chance to spot enemies

### Bugfixes

- Fixed a bug where World Market Hubs were not fully deregistered upon destruction, which could lead to double toll payments
- Fixed a bug where the World Market Hub Trade Center would pay all tolls rather than toll costs being properly distributed per trade center
- Fixed a bug where unused supply ship construction points would be used for military construction points preventing supply ships from being built
- Fixed a bug where the company sorting buttons did not work
- Fixed convoy raiding not engaging army supply ships, preventing naval raids from disrupting land army supply lines
- Fixed an issue where an army could travel to a basecamp without a valid supply path
- Fixed an issue where fortifications were not affected by goods shortage
- We now disband all the troops when disbanding a formation instead of transferring them, which resulted in teleportation
- Fixed an issue where commanders could not be recruited to formations without units or ships
- Fixed a bug where non piracy agreement would not prevent your export routes from being pirated
- Fixed an issue where fronts could not advance against enemy allies
- Fixed the multiple unit panel always only showing the Advance order
- Removed the Age of Caudillos modifier from Iquichia
- Fixed an issue that caused Caribbean states to not use the Latin American building set
- The Social Monarchy law is now valid for forming Sovereign Empire power blocs
- Fixed a bug where after annexaction units could join the wrong armies
- Fixed an issue where Negotiations could request an impossible amount of trade centres
- The "Acquire Land in Panama" and "Acquire Land in the Sinai" decisions now give provinces on both sides of the canal to be
- Countries are now forced to actually pay the merchants shipping their treaty transferred goods
- Fixed refreshing army supply paths when military access changes
- Purchasing Alaska no longer transfers the Kuril Islands to the country that purchased Alaska
- Selling Alaska now dissolves the Russian-American Company
- When defending against naval invasions, we now strongly encourage the coward generals stationed in the attacked HQ to go alongside their units to defend
- Fixed Sakhalin having no arable resources
- Corrected a hub issue in Tenasserim, so troop movements from the port hub to the land do not teleport armies
- Fixed an issue with unraised conscripts being included in the calculation of the special unit ratio
- Fixed a bug where invasions with with both marines and regular troops could silently fail to start
- Fixed numerous cases where primary cultures could be culturally discriminated against
- Fixed a bug where ships in ports that take damage would not queue up any repairs
- Fixed a bug where ship repairs did not account for new damage once the repair was queued
- Moved the city of Suez to within Sinai state
- Fixed an Out Of Sync with Ship Templates serialization
- Fixed an Out Of Sync with AI evaluation of project interest on a sea region
- Fixed a bug where a companies HQ did not properly disband, this would prevent you from creating the company again
- Fixed an issue where pursuing the Andean Federation would give infamy to the wrong country
- Fixed an edge case where a non-Tokugawa character could become the Shogun of Japan
- Colonial countries formed through "Establish Colonial Administration" will now get all of the overlord's primary cultures
- Fixed a bug where using marines did result in not showing any 3D models on fronts or battles
- Fixed a crash that could occur when an invasion was cancelled
- Corrected DLC requirements for some clothing assets that were accidentally locked
- Chinese ship names will now display properly
- Fixed the Kuril Islands not having market access at game start
- Fixed a bug when Market Access Price Impact would not change after Flood has ended
- Fixed a bug where, when a country would become recognized, existing piracy missions would not be cancelled
- Abdicating the Japanese Emperor now fires the Imperial succession events (The Great Wave)
- The "The Opium Trade" Journal Entry now addicts a culture in a market which is importing opium, rather than exporting it
- Fixed a bug where liberate country would not be possible when the target country had no researched pan-nationalism
- Fixed an issue where Diogo Antônio Feijó could live forever with Colossus of the South active
- Struggle for the Highveld JE now has text when looking at South African countries in the lobby
- Fixed an avenue in which French royal claimants could duplicate themselves
- Removed a duplicate instance of Tōgō Heihachirō
- Fixed an event that, instead of transferring Napoleon III between countries, would kill him and make a clone
- Fixed a case in Divided Monarchists in which cementing the power of the ruling dynasty would kill and create a clone of the ruler
- Fixed a problem that could make the German flag fail to render in tooltips
- "A Strange Superstition" may no longer fire every year
- Fixed the wrong country having the Treaty of Singapore with Johore
- Fixed DLC icon and text in event windows
- Added localisation to the name of Ibibioland
- Fixed an inaccurate tooltip in the Strike! Journal Entry

## 1.13.8

Patch 1.13.8 was released on 2026-05-28[9] with checksum *ce22*.

### Interface

- Made it so fleets are not always shown as "too weak to fight” during naval invasions
- Fixed the pink placeholder face being shown as a mapmode icon in a building details screen

### Bugfixes

- Fixed a bug where naval battles did not spawn during naval invasions unless there was an explicit interception mission
- Fixed a bug where a fleet would drop an army in the sea and go back to port during naval invasion
- Fixed a bug where a naval invasion would get cancelled if an enemy fleet was blocking the sea node
- Fixed a bug where the AI could be blocked from conducting naval invasions related to the issues above

## 1.13.9

Patch 1.13.9 was released on 2026-06-25[10] with checksum *b2e3*.

### Features

- Added search bars in various places, including the Tech tree. It can be used to look for a specific unlock, for example if you want to find all technologies that provide a bonus to MAPI.
- Added fleet action to return a fleet to nearest friendly port for repairs, they will resume mission when they finish repairs
- Made it so Diplomatic Plays can be started over strait related war goals, rather than just having the option to add those to an existing Diplomatic Play

### Improvements

- All movement types will now have substantially reduced Activism following their defeat in a Civil War. Movement defeat status is stored per identity, and persists through movements being disbanded and refounded.
- Reworked Command Limit so that regulars or raised conscripts, whichever is higher, is compared against command limit rather than being added together. This removes the need to mass-promote commanders when you raise conscripts.
- Most instances of flat negative Authority and Bureaucracy modifiers, such as Political Concessions, are now treated as Authority or Bureaucracy costs
- Fronts now track which (if any) side has made gains in the last few months, and displays this in the Front panel
- Involvement level in a country's capital region now impacts leverage generation as follows: -50% at no interest, -25% at Observant, +25% at Pervasive and +50% at Hegemonic
- Added unique localisation to the Shogunate Regency, with "Shōgun Kōken-Shoku" as a title for the Regent
- Trade Centers now gain Trade Advantage from Prestige Good input (ie, Prestige Merchant Marine), up to 25% at 100% prestige input

### AI

- Fixed a bug where the AI would calculate the predicted construction sectors in their construction queue with the full cost of their input goods, leading to spontaneous and overzealous budgetary cuts in other spending areas
- Fixed an issue where the AI would queue more barracks than it actually wanted due to not correctly counting barracks already in the queue
- Countries will no longer break treaties that were signed before game start until their binding period ends
- Fixed another bug which was causing the AI to generate duplicate ship templates
- The AI now has reduced peace acceptance for the first year of a war, and then starts to accumulate white peace acceptance, instead of getting white peace acceptance from the very start
- The AI now considers war goals that are located on fronts where it is decisively advancing to be achievable, making them less interested in a peace which does not involve ceding that war goal
- Fixed a bug where the AI could disband its entire army because it was trying to get rid of unwanted marines that didn't exist
- Fixed a bug where AIs with Economic Imperialism would not try to open up non Japanese isolated markets due to incorrect script checks
- Fixed the AI underinvesting in innovation in .7
- Portuguese AI will be more likely to invest in Railways for as long as Regeneration: Public Works is active
- The AI is now much more eager to construct canals

### Balance

- Reduced output of Fruit Plantations by a fair bit, especially using slaves. We will keep an eye on the situation to see if we need to tweak this more.
- Law Enactment Time modifiers have been reworked into Law Enactment Speed modifiers to make it more difficult to stack them for instant or almost instant law enactment. A minimum of 10% speed has also been set so that it's not possible to negatively stack speed modifiers to 0% or below.
- The impact of Prominence and Movement Pressure is now additive rather than multiplicative on the ideology selection weight. This means that both will have a more consistent impact that neither overpowers all other factors nor simply becomes noise.
- Ship critical hits have been reworked. They now ignore 100% of the enemy target's armor. Reduced critical damage increases across the board in compensation.
- Adjusted technology requirements for Military Aviation and Seaplane Tenders to make them usable when built. The previous tech tree layout could lead to you developing them, while not being able to have airplanes in your market yet.
- Reduced some of the modifiers that rebellions get based off of their popular support
- War Goals that are considered contested if you control the enemy capital are now generally also considered contested if you control 50% of the enemy's incorporated states
- States which are at least 50% occupied are now considered occupied for the purposes of war goal control, rather than requiring full occupation.
- Added a check to breaking Ship Transfer treaties to ensure only ship receiving countries could get a penalty from breaking it early
- Supremacists movements will now gain up to 25% activism after researching "Nationalism" scaled by the number of primary culture homelands that are not owned by a nation of the same primary culture
- Readjusted Ship Gun Modules to be in roughly 25% bounds of each other relative to the base module, previously this was closer to 50%
- Increased the construction time and cost of capital ships, particularly the Dreadnought family significantly - up to two times as much on the highest end
- The Arc Welding and Concrete Dockyards technologies now grant a bonus to Capital Ships Max Construction Progress, meaning unlocking these techs will increase the speed at which capital ships are constructed
- Passive Electoral Confidence maluses will no longer apply below 25% Electoral Confidence
- Rio de la Plata no longer requires Patagonia to be formed
- Reduced activism gain from most sources for the Utilitarian Movement
- Provided School Supplies amendment now gives a small increase to dependent wages to simulate lower expenses for children
- Civil wars now split ships with construction points in mind to try and avoid them sinking
- Swapped the first and second level effects of the Construction Power Bloc principles
- Increased all 1 or 2-level Coal, Iron, Sulphur, or Lead potentials to 3 levels

### Art

- Added new visual effects for the Port Bombardment interaction (Requires The Great Wave)

### Content

- Gave Italian minors the Banking technology from the start
- Adjusted the Supply Network tutorial mission conditions to ensure it requires the player doing something to fix it
- The Companhia de Moçambique now has Millet Farms as a base building, rather than Wheat Farms
- Added dynamic hispanophone state and hub names for Puerto Rico
- Fixed and improved a few tooltips by clarifying the presented data and fixing typos
- John Stuart Mill is now always present in British India at game start
- Renamed Land Logistics Centers to Army Logistics Centers

### Interface

- Updated Ship Veterancy Tooltip to also show whether experience is gained or lost, as well as the weekly increase or decrease
- Updated supply information on the army panel to better showcase when there is a supply or goods shortage
- Supplies now show whether they are being sent from supply ships or via land route
- Added Supply to Logistic Centre outputs and made it easier to spot a shortage due to input goods shortage
- Multipliers are now accounted for in army supply breakdown
- Added icons for goods shortage to the army panel and the supply tooltip
- Added a building widget to the Fleet buildings tab
- The wargoal tooltip now shows much more clearly that a wargoal costs no maneuvers because it is the first wargoal
- Added more in-depth breakdowns of all Formation stats, especially connecting Commander Traits & Orders directly to the affected stats' tooltips
- Added right-click station formation in state back
- Added a tooltip for when you cannot decommission ships
- Changed supply text to show actual and maximum stockpile, rather than percentage
- Naval missions now show supply raiding/protection and port bombardment details directly in the fleet panel and tooltips
- The state devastation tooltip now reflects ongoing port bombardment and breaks the daily change down into recovery and bombardment
- The tooltip for forming a Power Bloc now shows a breakdown of requirements
- Added a repair icon to mission map markers and adjusted their visibility to highlight whenever a mission is paused due to the fleet being docked for repairs
- Army Battalions and Conscripts counts are now displayed separately against the Command Limit, making it clear the limit applies to whichever is higher rather than the two combined
- Added proper tooltips and explanations to Company Categories
- When filtering for companies by building type, the filter now also accounts for building types granted by company charters
- When filtering for companies by building type, the selected building type is now also highlighted in the company panel
- Updated Company Filters Button Order and adjusted descriptive texts
- Made it so we no longer show formations that are currently not mobilized in the naval invasion panel
- Added additional info to shipping lane efficiency and its tooltip, showing the current trend and reasons for reduced efficiency
- The precise interest tier required to colonize is now explained in the map tooltip
- Strategic Region Map Mode Tooltips now correctly generate at the mouse hover point
- Make it so when a magnate has 0 holdings we do not show the holdings
- Added Ship Modifications to Ship Panel and Ship Tooltip
- Hid the national cast button for foreign nations, it would open your own national cast before
- Added a new alert for Merchant Marine shortage which also explains impact on shipping lanes
- The number of idle generals and admirals is now visible on the assign leader panel
- Recruit general / admiral button now correctly disables when above the idle limit
- The Location Finder now has non-English characters searchable by corresponding basic ISO characters, so you can e.g. find Göteborg by typing Goteborg
- Naval Fortification buttons are now clickable and open the building detail panel
- Added sorting by assigned ships to the country supply ships tooltip
- Put strategic region involvement due to Power Bloc members into a paged sub-tooltip as that list can get quite large
- Added a go-to button with the name and logo of the company at the bottom of the character panel for executives
- Added clearer indication if a tooltip is locked and what button to press if you use Action Lock
- Flagged the colonial administrator change notifications as ruler group so they get correctly caught by the according notification settings
- Cost of market goods is now calculated in the breakdown of the cost of war
- Added custom icons to the Hidden Domain Journal Entry progress bar
- Building panel and tooltips now display if the building is the holding of a magnate
- Updated Bankruptcy button and added progress bar
- Added a missing icon reference for the Disgraced Technocrat modifier
- Remove extra line breaks in law endorsement tooltips

### Performance

- Reduced memory usage by around 7-10% and total allocations by 15%
- Various improvements to overall tickspeed

### Modding

- Added a new character role type "other" that groups special characters together in the outliner
- Added capacity cost modifiers for authority, bureaucracy and influence
- Added support for excluding specific states from being targeted in unification plays via a should_target_state_in_unification_play trigger in country formations
- Added new effect set_movement_defeated
- Added on action for when a commander is promoted
- Added new triggers days_since_movement_defeated and days_since_movement_type_defeated

### Bugfixes

- Fixed a bug where fleets whose supply ships were under attack would be considered 'in battle', preventing them from functioning normally
- Fixed a bug where sometime diplomatic actions (such as improve relations) that were not available would always be hidden instead of showing why they were not available (for example due to lacking mutual interests)
- Fixed piracy causing country relations to reset on save load
- Combat units now add supplies to their formation when mobilized based on availability from the logistics center. This fixes an issue where the supply ratio would drop dramatically for armies with large amounts of conscripts.
- Fixed a bug where you could decommission ships carrying formations, this would silently kill them
- Fixed a bug where supply lines would break due to straits blocking the passage, now it will try alternative routes
- Fixed slaves being freed when fired from their jobs
- Fixed a bug where 'make this work' could sometimes add mutually incompatible articles, such as Alliance and Guarantee Independence
- Prevented the AI from overflowing transport capacity during naval invasions
- Fixed where an event for loaning an army leader in exchange of an obligation would end up swapping the leaders without setting correct country causing broken fronts
- Switching from Social Monarchy to Monarchy will no longer end regencies
- Spain can no longer declare wars whilst fighting the Carlist War
- The Change Language of Administration and Spread Primary Culture interactions now covert pops to the actor country's most populous primary culture, rather than its least
- West Virginia will no longer join the Confederate States of America in the American Civil War
- Fixed issue where trade advantage in a local market could go haywire when privateering
- Fixed a bug where AI could use threaten naval hostilities when it should not be possible
- Fixed a bug where market goods sell orders from piracy would stack infinitely in states without trade centers
- Farmers should no longer be politically motivated twice by having a variant of peasant proprietorship active. They now get higher values by having either proprietorship or homesteading active.
- Fixed several events that could lead to a notification showing a new leader spawning with a null ideology. Affected events are as follows: "Freedom Without Distinction", "Mutual Aid", "A [Culture] Voice", "The Vanguard Advances", "From the Ground Up", "For Whom the Bell Tolls", "Joining Our Cause", "Open Succession", "The Blazing Chowki", "Tribal Gesture", "Nothing Ends", "Into Oblivion", "Condemnations of the Children", "The Wedge in the Academia", "A Revolutionary for Our Time", "The Interpretation of Dreams", "Indisposed", "The Yellow International", "The Weapon of the Enemy", "[Culture] Leadership", and "Society of the Godless".
- Fixed an issue in the calculation of port connection distances
- Fixed an issue where naval invasions targeting non-negotiating participants could be blocked
- Fixed an Out of Sync that could happen when playing cross-platform multiplayer
- Independence war goal is now controlled if the capital of the opposing country comes under control
- Fixed bug where a war being inherited (like after civil war) could cause hostilities to not be set correctly preventing naval invasions
- Law enactment speed now correctly reduces enactment time
- Frosts, Ice, Tropical Storms, and Heatwaves are now properly limited to their applicable geographic regions
- Fixed some cases in which France or Hungary could not have their pre-Springtime voting, free speech, and internal security laws reverted by a reactionary victory in Red Summer
- Fixed restriction for naval invasion defenders to the invaded and neighboring states
- Fixed a bug where you could not get an investment rights treaty with a country of equal rank in your power bloc when Foreign Investment III principle is active
- Fixed a bug where the invasion panel would display a NULL_OBJ
- Fixed an issue in the Manifest Destiny trigger for the USA
- Fixed an issue where Spain could never panicked-retreat from battle
- Fixed articles being added to a treaty as a part of a renegotiation not actually being applied when coming into force
- Fixed issue where rehoming an overseas army would not actually change home HQ
- Unincorporated state effects should now list all effects they have as intended. Previously some of their effects were tucked away in other categories, meaning they would only show in that wrong place.
- Fixed a bug where Power Projection check for naval invasions did not respect fleet transport capacity
- Fixed a bug where abandon piracy treaty would not cancel active piracy missions
- Fixed a bug where the player could embark multiple marine formations surpassing the marine fleet capacity if done at once
- Fixed a bug where merging fleets would give only the supplies of 1 fleet instead of merging the supplies too
- Fixed pure conscript armies being unable to re-station when there's a land connection
- Make this work' now works properly when renegotiating proposed treaties
- Fixed a bug where Treaty Ports ceded during war would not end up in the correct market
- Fixed issue where it would show N/A travel time when planning naval invasions
- Treaty Port treaties with China will no longer automatically break when the Heavenly Kingdom appears, only if they actually win
- Fixed an issue in Moroccan scripted succession, in which Muhammad V could not spawn due to a typo
- Fixed trigger descriptions for political_strength_share and wealth_share to show correct information
- Fixed a display issue in the state requirements for the Tashkent Railway company
- The Nederlandsche Handel-Maatschappij now has Coffee Plantations available by default, with Tobacco Plantations available as an additional industry
- Fixed some cases where wargoals in the Mutiny! event for the East India Company could invalidate
- Fixed a bug where commander career was considered to have started when they were spawned into the recruitment pool rather than when they were actually recruited
- Ship List Modifications now show the actual ship modifications, not those of the template
- Fixed AI using invalid fleets when evaluating what missions it can do
- Fixed AI evaluating ship transfer treaty with countries without a port
- Fixed an issue where loitering formations could not merge
- Fixed issue where it could appear as if foreign company was investing in their own land in your investor intents if you had treaty to let you invest in said company land
- Fixed bug where you could not privateer someone because you weren't at war with both importer and exporter
- Fixed a bug where a revolution would have a null_state in it preventing it from triggering a war
- Fixed a bug where revolutionary Interest Groups would become marginalized if a secession broke out
- Fixed a bug where Interest Groups could get stuck in a party they no longer wanted to be part of, resulting in high ideological incoherence
- Fixed a bug where parties that disband and reform would keep stale voting data from old elections, resulting in a sudden drop of legitimacy when they reformed
- Fixed a bug where IGs who want to leave parties outside of the election cycle would leave instantly instead of waiting for the next election
- Cancelling a naval invasion before the army has embarked onto the fleet will now no longer teleport the army to the fleet
- Marines transferred between ships will no longer perform minor miracles (walking on water, the occasional teleportation).
- Fix general swap not working between two armies
- The Legitimist Movement will no longer fail to recognise late-game Carlist claimants to the French throne as legitimate
- Removed randomly appearing and flickering thin vertical line on Army map markers
- Fixed the 'everyone disliked that' achievement to correctly only fire when a single promotion annoys every other interest group
- Fix issue where slave pops would immediately become employed on the first tick and break some history scripts
- Fixed several issues where unintended countries could get national unification content if given additional cultures through the Spread Primary Culture interaction
- Stop split armies from merging back while waiting to be transported
- Fixed a bug where the map context of the country panel would not switch when clicking around unless the diplomacy tab was open
- Fixed inheritable construction not working for civil wars
- Removed Arms Industries as a requirement for Rheinmetall
- Countries that cannot form the Japanese Zaibatsu will no longer see them in the Attainable/Potential Companies list
- Fixed the Chieftain of Ngāti Toa's home state being displayed as a null scope
- The Fundição Ipanema company for Brazil no longer requires iron mines in São Paulo
- Various pieces of narrative content that activate Republic laws will now activate Stamp Out Monarchism
- Fixed incorrect Utility Modification Icons being shown in panels and tooltips
- Fixed an issue where the Merge Formations button did not show the condition message
- Enacting isolationism will now update the average trading distance accordingly
- Fully assimilated cultures no longer remain in the culture list
- Fixed a bug where commanders marked busy were sometimes not unassigned from their formation
- Fixed a bug where canal straits were created during construction instead of after completion
- Fixed a null scope in "The Entrenched Front"
- Fixed several issues where unraised conscripts were counted as mobilized
- Added factoring in dividends when calculating wage rate
- Pinning the Emperor (of Japan) character will now correctly display it on the outliner
- Fixed a bug where the Unification play for Federation of the Andes could be started with no war goals due to only targeting countries which did not have valid states
- Fixed some ship modifiers not showing when hovering ship utility modifications
- Fixed a bug where null_obj could appear in the construction queue if you had foreign investments in a split state that got annexed
- Fixed an issue with merchant marine costs being truncated
- Fixed an overflow in Ulta's colour code
- Fixed an issue where "Doctrine of Lapse Invoked" could have no description
- Fixed a loc issue related to the Strait of Gibraltar in the Spanish Africa content

## 1.13.10

Patch 1.13.10 was released on 2026-08-11[11] with checksum *2964*.

### Improvements

- Ships built for a selected target fleet now spawn at the closest reachable shipyard to that fleet (by sea travel), falling back to the previous placement when none can reach it. A "Will be built in: <region>" line in the ship construction entry tooltip will tell you where a ship will appear.
- Added a button to pause construction on individual construction sectors
- A country that gains control, through revolution or conquest, of land hosting foreign treaty ports now inherits those treaty port agreements, and is given the choice to honor them or revoke them and reclaim the ports for itself. The affected foreign power is notified of the decision either way.
- When disbanding a company producing a generic prestige good the respective journal entry is reenabled so that it can be reapplied to a new company if needed

### AI

- Colonial powers are now more inclined to launch a diplomatic play to retake a treaty port from a country that recently revoked their treaty port agreement, until they have had their revenge
- The AI now decommissions excess Supply Ships it no longer needs
- The AI no longer proposes treaty articles that hand over its own subjects to itself

### Interface

- Added an alert that warns when a ship under construction is assigned to a target fleet it will not be able to reach, listing the affected fleet(s)
- Estimated interception effects are now shown while hovering to assign a fleet to intercept
- Estimated blockade effects are now shown while hovering to assign a fleet to blockade
- Hovering a naval fleet's mission marker now highlights the sea regions and routes it operates in, and enemy naval missions appear as their own markers below the sea node
- The interface will now state that a fleet can't reach a coastal state when there's a strait blocking the path there for a naval invasion
- Assigning a Protect Supply Lines mission now shows which supply ships and formations the sea region carries, and which hostile fleets are raiding there
- Interest tier tooltips on the map now name the strategic region they refer to
- Left-clicking a naval mission map marker now opens the fleet directly, or lists the fleets when several share the same mission
- Added detailed information to the fleet panel about any ongoing blockade by the currently selected fleet
- Port Bombardment now shows coastal-building markers and arrows on the map, indicating which coastal buildings are threatened and where the bombardment comes from
- Added a Naval Mission map marker for enemy Fleets
- Ship stat breakdowns now group multiplicative bonuses into a single hoverable entry so the listed values add up to the total
- Added a button in the Construction Panel's Ships tab to permanently decommission available Supply Ships
- Updated tooltips for sea nodes, Headquarters, and states to show target involvement changes when redeploying/stationing fleets and armies
- A sea region's tooltip for the project power naval mission now correctly shows the predictive involvement changes if the fleet would be deployed to that region
- Added a status line in the case a fleet is traveling to pick up an army during a naval invasion
- The fleet panel's Retrofit button now explains why the selected ships cannot be retrofitted
- The tooltip when editing a Naval Mission's Sea Regions now explains when Shift+Click would not work because the mission's area limit would be exceeded
- Naval mission markers collapse into small colour-coded dots when the map is zoomed far out, reducing clutter
- Added entry to importers state goods panel displaying how much is lost to piracy
- Fleets over their Command Limit now show the limit in red in the outliner and in fleet tooltips
- The outliner no longer shows a Command Limit warning for armies that are not over their Command Limit
- The Short-Term Tax Cuts amendment now shows how long it lasts and posts a notification when it expires
- Hovering a ship traded in a treaty now shows that ship's tooltip
- Hide the ship transfer options when making treaties with landlocked countries
- Made it so transfer subject treaty article is disabled when you have no subjects to transfer
- Updated the colors of the building ownership bars to make more sense, blue-ish colors are now "owned by you" while orange-ish colors represents other countries' ownership
- The Ship Transfer article no longer spills outside its frame on treaty tooltips
- Improved how ship prefixes (like HMS) are rendered in the ship panel
- Fixed a case where the transfer unit window would wrongly claim you were above the command limit when mixing conscripts and regulars

### Performance

- Fixed severe framerate drops when hovering or selecting fleets with very large numbers of ships

### Modding

- Added the on_treaty_ports_inherited on-action and the renege_treaty_ports_with country effect, used when a country inherits or gives up hosted treaty ports.
- Added script containers (see create_container)

### Bugfixes

- Reducing a fleet's visibility now makes it harder to spot instead of easier
- Admiral traits and naval missions that change a fleet's visibility or detection now affect whether enemy fleets spot it
- Fixed invasions getting stuck at 99% advancement due to states being left under the control of a country that no longer occupied them; affected saves are repaired on load
- Single good shortage no longer drains supply and instead lowers maximum organization
- Fixed armies being destroyed and their general killed when their transport fleet re-routed while the troops were traveling to embark for a naval invasion
- Fixed a bug where you could end up with no logistic centers in your country making your armies get no supplies
- Fixed a bug where unraised conscripts would not upgrade when you pressed the upgrade all button
- Private investment no longer endlessly expands railways that can never become profitable
- Fixed the same war goal being added twice to a diplomatic play when a country was swayed with a war goal that was already among its demands
- Fixed crash after loading a save with pops missing their social class
- Fixed crash when a country going bankrupt removes an unbuilt canal
- Fixed crash from dangling ship repair stuck after save load
- Fixed a bug where after cancelling a naval invasion the partial occupation would not disappear
- The confirmation popup for breaking a Ship Transfer or Support Independence treaty now lists the infamy and relations penalties
- Fixed a bug where naval invasion could sometimes get stuck
- Fixed an out-of-sync error in multiplayer that could occur when a revolution appointed new interest group leaders
- Fixed strait toll income dropping every time a save was loaded
- Ships can again be transferred between fleets while marines are attached, as long as one side of the transfer can still carry all of them
- Resolved an issue where the player was unable to change their tariffs or subvention levels freely within the grace period
- Ships traded in a treaty now show their utility modifications
- Strait toll income, the strait panel and trade center toll expenses now report the same trade amounts and no longer charge tolls for goods whose route does not pass through the strait
- Fixed an issue where movement radicalism from unowned homelands for Cultural Supremacy movements was not being calculated correctly
- The predicted change of involvement when adding a sea region to a fleet's orders now accounts for the areas those orders already cover
- Armies now need adequate supply ships to cover the journey when performing a naval invasion
- Fixes an issue that would cause "The River of Coffee" to fail upon a civil war taking the capital
- Promoting a commander no longer upsets interest groups whose commanders are all of a different type than the promoted one
- You can no longer send uncrewed ships on missions
- Ships can no longer be sent to retrofit while their fleet is transporting an army
- Ships sent for refitting now stay in the port where their fleet is docked instead of sailing to its home naval base
- Fleets sent to port for repairs are released again once they have all the crew that can currently be found
- Fixed the progress bars in Hidden Domain Journal Entry to properly display country names after either country had a victorious revolution
- Fixes an issue where an exiled army could get stuck in friendly territory
- Fixed an issue where treaty effects would still provide benefits even if the article is non-fulfilled
- Fixed being able to sign multiple treaties with identical terms with the same country, which allowed stacking leverage
- Fixed a bug where renegotiating an old treaty could instantly grant an obligation
- Shipyard wages are no longer paid twice
- Fixed a bug where you could exceed the carrying capacity by merging armies waiting to be embarked
- Treaty ports now properly reconnect to the new host's market when a treaty changes hands
- Fixed script errors from the AI evaluating the Ryukyu rivalry journal entry buttons
- Ships no longer lose experience while their fleet is transporting an army or carrying out a naval invasion
- Fixed some Japanese characters missing Japanese culture
- Cancelling the retrofit of a single ship now returns it to its original fleet instead of leaving it in the retrofit fleet
- Fixed a bug where a fleet that is retrofitting could still be sent on a naval mission without cancelling the retrofitting
- Fixed a bug where you could transfer a subject to itself
- Fixed issue where goods were not properly removed from importer during piracy
- Fixed a treaty port (such as Hong Kong) becoming permanently cut off from the World Market with 0% market access after a revolution or conquest replaced the country that had hosted it
- Fixed an issue with renegotiating treaties with duplicate articles

## 1.13.11

Patch 1.13.11 was released on 2026-08-19[12] with checksum *a47f*.

### Balance

- Adjusted the Banana Plantation output values. Removed 5 Fruit from the base and added 5 to the automated PM, as it was intended.
- Tweaked the outcome options for the "A Doctrine of Iron and Steel" event so that both, first and second, are more equally feasible

### Bugfixes

- Fixed a crash that happened at the turn of the month when sway offers were pending in a diplomatic play

## References

1. ↑ Forum: [Hotfix 1.13.1 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1919489), 2026-04-29.
2. ↑ Forum: [Hotfix 1.13.2 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1919767), 2026-04-30.
3. ↑ Forum: [Hotfix 1.13.3 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1919781), 2026-04-30.
4. ↑ Forum: [Hotfix 1.13.4 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1920992), 2026-05-07.
5. ↑ Forum: [Additions to the Patchnotes (08/05/2026)](https://forum.paradoxplaza.com/forum/index.php?posts/31278426), 2026-05-08
6. ↑ Forum: [Hotfix 1.13.5 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1922242), 2026-05-12.
7. ↑ Forum: [Hotfix 1.13.6 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1923815), 2026-05-20.
8. ↑ Forum: [Hotfix 1.13.7 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1925153), 2026-05-27.
9. ↑ Forum: [Hotfix 1.13.8 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1925346), 2026-05-28.
10. ↑ Forum: [Hotfix 1.13.9 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1931503), 2026-06-25.
11. ↑ Forum: [Hotfix 1.13.10 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1938098), 2026-08-11.
12. ↑ Forum: [Hotfix 1.13.11 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1938838), 2026-08-19.
