---
title: Patch 1.7.X
source: https://vic3.paradoxwikis.com/Patch_1.7.X
pageid: 6346
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
**Patch 1.7.X** are all patches beginning with 1.7.

## 1.7

Main article:
Patch 1.7

## 1.7.1

Patch 1.7.1 was released on 2024-06-27[1] with checksum *b087*.

### Improvements

- Added mandate generation from Unrecognized countries to all Identities
- Earning Recognition Journal Entry is now unlocked by Colonization rather than Civilizing Mission and only requires 50 relations with a Great Power to complete
- It is now possible to 'upgrade' an Investment Rights pact to a Mutual Investment Agreement, if the other part agrees to it
- Conquering a split state now applies the 'Recently Liberated' rather than 'Recently Conquered' modifier, as the latter ended up giving tax penalties to a state you already owned, which could be devastating for tiny nations
- Ranches no longer consume grain as a default good, but only if more advanced PMs are activated
- Regime Change Diplomatic Play can no longer be used against your own subjects since Law Imposition can be used for it instead
- Collectivized building levels, or buildings with levels that are undergoing collectivization, can no longer be nationalized
- Cuirassiers no longer consume iron, but use more small arms instead
- Sovereign Empire statues now provides a 25% Decree Cost discount to the state it is constructed in instead of applying it to the whole country
- The Boer States now start with National Militia and with their independence guaranteed by Britain

### AI

- The autonomous investment AI now keeps track of how much investment has gone into foreign/domestic states and biases future investment towards domestic states if an excessive amount has gone towards foreign investment, to ensure investment isn't all going overseas
- Fixed an issue where civil war countries and native uprisings would not recruit commanders for their armies due to incorrectly set AI tags for their formations
- Rebellious and Defiant subjects will no longer actively aid their overlord in diplomatic plays outside of what they consider necessary to defend their own territory
- Loyal subjects now mobilize a higher fraction of their troops to aid their overlords in diplomatic plays
- The AI is now able to reassign armies/navies that are traveling, preventing suboptimal naval invasions due to the best fleets not being 'available'
- The AI is now able to launch simultaneous naval invasions, but will generally avoid using all of its armies/fleets at once for this

### Balance

- Manor Houses no longer require infrastructure, as this caused major issues for highly populous countries with a lot of subsistence agriculture
- Reduced investment weights for Manor Houses on all non-agricultural buildings, as their tendency to invest into factories in countries like Japan would lead to an odd aristocrat-led industrialization
- Reduced the rate at which generic random events appear to compensate for increased overall event spawn rate due to prior bug fixes
- Reduced effect of Asceticism (Devout) trait from -50%/-100% to -15%/-30% reduction on radicals from changes to standard of living (sorry)
- Reduced effect of Secular Shrine Theory (Devout) trait from +20%/+40% to +15%/+30% conversion
- Reduced effect of Da Wat (Devout) trait from +50%/+100% to +20%/+40% conversion
- Reduced effect of Propagandists (Intelligentsia) trait from +25%/+50% to +15%/+30% migration attraction
- Decrees now have a minimum cost of 10% of its base cost, to prevent modifier stacking for free Decrees
- Imperious now provides a 20% rather than 25% Decree Cost discount
- Cruel trait now provides a 5% Authority boost rather than a Decree Cost discount

### Interface

- Map markers will now indicate where your foreign construction is happening
- Demand Force Nationalization wargoal will now display how many building levels and what fraction of GDP would be nationalized
- Fixed some issues with the 'failing to hire' tooltip for buildings where it would sometimes lack a reason for failing to hire and/or contain unnecessary whitespaces
- Added Bloc Leader interaction icon to differentiate it from Bloc Member actions
- Cursor will no longer flicker between the game cursor and operating system cursor while moving the mouse in the loading screen
- Removed duplicated Leverage Resistance description in tooltip
- Fixed long overlapping texts to not overlap anymore in the Trade States Diplomatic Action popup
- Max number of setbacks modifier will now be displayed as a whole value instead of a confusing percentage value

### Modding

- Fixed a bug where modders using a create_country effect in global history files would lead to blocs being disbanded during initialization
- Added mandate generation by rank modifiers for unrecognized major, unrecognized regional, unrecognized and insignificant powers
- Added new generic Power Bloc invite acceptance modifier
- Made Power Bloc invite acceptance by rank modifiers support arbitrary ranks defined in script
- Cost calculation for Decrees is now done on a per-state rather than per-country basis, permitting for differing costs dependent on the state the Decree is applied in
- decree_cost link now operates in state scope rather than country scope

### Bugfixes

- Fixed a crash related to CollectOwnAndAlliedLandHQs
- Fixed a bug where it was possible to make a diplomatic demand against a country you were already at war with
- The "Land of the Rising Sun" event for Persia now gives a claim on the correct Georgia (hint: not the one north of Florida)
- Fixed inverted values in Earning Recognition Journal Entry causing you to gain progress for low GDP/SoL and vice versa
- Fixed a bug where leaders of Military Treaty Power Blocs would not pay maneuvers for adding wargoals in diplomatic plays where they were a main participant
- Fixed a bug where formations with no commanders could not be mobilized due to incorrect 'all commanders are busy' error
- Fixed bug where cohesion for ideological union was inexplicably trending towards 0
- "Enemy of my Enemy" lobby event can no longer target your own country as the enemy in question, however amusing that might sound
- The Pamir Delimitation will no longer carry over script variables from previous attempts
- It is no longer possible to capture a state in less than 2 battles, as this could result in issues such naval invasions that were impossible to consolidate due to creating multiple fronts
- Fixed bug that made Pacifists only spawn in the Armed Forces rather than the other way around
- Fixed a bug where the -30 relations penalty with Power Bloc leaders for creating a Power Bloc was applied during history initialization, causing the Great Powers to have erroneously low relations with each other at game start
- Political Lobbies will no longer form targeting Revolutionary countries until they actually win the revolution, to avoid highly temporary lobbies forming and then disbanding
- Replaced the Power Bloc Statue throughput with a level scaling effect under the "Prestige Only" game rule to prevent it from granting the prestige while they are still in the construction queue
- Fixed an AI issue that could lead to incorrectly removing conscript units, leading to negative amount of conscripts in an army
- Fixed a bug when manor house levels weren't removed when subsistence farms were removed
- Fixed a bug where the "Add to Primary" button would show up on an Overlord's Wargoals for the Subject
- Resolved issue where Communism and Populism progress bars didn't properly retreat due to laws
- Fixed an issue when 100% worker-owned buildings can still be nationalized if the building is level 1
- Fixed an issue where exiling/inviting agitators would never create lobbies in their home countries
- Fixed a bug where a victorious revolution could end up with a political lobby targeting itself
- The East Indies' End event can no longer fire multiple times per game
- The Tibet Expedition will now properly cancel if at war with Tibet
- The "Can't Touch This" achievement can now be gained even if a country has (non-nationalizable) gold fields or subsistence farms
- Fixed an out-of-sync related to markets
- Fixed the amount of compensation in the notification when nationalizing foreign assets
- Replaced the University and Art Academy's "Increased Exchange" (unlocked by the Freedom of Movement Principle) Production Method's country modifier with a state modifier as originally intended. The former led to way higher migration attraction as it was stacking all states' effects where it was active.
- General Brusilov no longer requires owning the American state of Georgia to spawn
- Fixed a bug where accept/decline effects of reverse pact actions such as Request Knowledge Sharing and Request Support Regime were not correctly shown in tooltips
- The emergency hunger relief modifier from the Famine event chain is now applied only to states affected by famine
- Pink faces will no longer be submitted alongside several Diplomatic Action proposals
- Pink face and NULL_STATE will no longer briefly appear briefly after a building has finished construction in Foreign Queues
- Fixed Power Bloc formation tutorial to prevent player moving forward despite not having completed a necessary step
- The British aid button for Persia will no longer state that it adds the "Russian Military Mission" modifier
- Fixed some instances of missing loc in Tibet Expedition tooltips (English only, other languages will be translated for 1.7.2)
- Fixed missing localization for key catalyst_revolution_successful
- Moved Saint Basil's Cathedral back to Moscow (from Mazovia)
- Added missing text for Building Relationships map mode (English only, will be translated for 1.7.2)
- Fixed a description error in the Dominion concept that stated that they wouldn't need to join their overlords (English only, will be translated for 1.7.2)
- Fixed error spam in the "Britain Demands Withdrawal from Herat" event
- Event ig_revolutions.8 will no longer display [ROOT.GetCountry.GetRuler.GetTitle] instead of the ruler's actual title

## 1.7.2

Patch 1.7.2 was released on 2024-07-03[2] with checksum *0942*.

### Improvements

- Added an event for Persia or Afghanistan winning the Great Game
- Britain and France no longer start with a rivalry, as this doesn't really accurately reflect their relations in 1836
- Austria, Prussia and Russia now start the game with friendly attitudes towards each other, to represent the historical Holy Alliance
- Added a rivalry between Brazil and Argentina at the game start
- Added a rivalry between Britain and Russia at the game start
- The initial Meiji Restoration Journal Entry is now a lot easier to complete and simply requires keeping the Shogunate out of power while maintaining at least middling legitimacy for 10 years, but is failed if the Shogunate gets back into government
- The Impose State Religion bloc action now also converts 2% of the population in non-capital states
- Advanced Research, Colonial Offices and Police Coordination principles now allow bloc leader to impose their law in the education system, colonization and policing law groups respectively
- Advanced Research, Colonial Offices and Police Coordination principles now disallow members from having the base laws in their respective groups (no schools, etc)
- Added dynamic boolean modifiers for disallowing specific laws
- Advanced Research, Colonial Offices and Police Coordination now all reduce their respective institution costs by -10/25/50% and increase speed for changing institution levels by 25/40/50%
- Advanced Research 1 now has +5% Tech spread as a Schools institution modifier instead of the flat value
- Advanced Research 3 now has -5% Ahead of Time Research Penalty as a Schools institution modifier instead of the flat value
- Advanced Research 3 now has an increase of 15 to the weekly innovation cap as a Schools institution modifier instead of the flat value
- Police Coordination 2 now reduces political movement radicalism on the police institution instead of giving authority
- Colonial Offices 3 now adds a decrease of 7% to infamy generation against unrecognized countries to the colonization institution
- Choosing to leave a Power Bloc now results in a relations hit and negative catalyst with the other members
- Liberty desire levels now display what war goals they unlock.
- Unrecognized Major Powers can now form Power Blocs, but will suffer a greater Relations hit with Recognized Power Bloc leaders when doing so, and will only gain Leverage over Recognized countries at 10% the normal rate
- Added a check for establishing Trade Agreement Pacts that their market can actually be reached by your country. This will also prevent Lobbies from requesting the signature of a Trade Agreement which you could not fulfill.
- Added a port to Shaozhou so that Hong Kong starts with a port when taken as a Treaty Port
- Changed Hokkaido to have subsistence pastures instead of rice farms, to more accurately reflect its initial Ainu majority
- Added missing localisation for power bloc identity requirements for production methods
- Restored Asceticism as one of the Chinese Devout IG Traits
- Added the concept_unrecognized_major_power in all languages

### AI

- Added and tweaked many starting attitudes and relations of AI countries to better reflect the diplomatic situation in 1836 and/or encourage more historically plausible outcomes
- Increased AI tendency to build gold mines.
- AI recognized powers are now more aggressive against unrecognized powers when they have the Civilizing Mission technology and/or Colonial Officers principle
- Unrecognized powers are now generally more aggressive against each other, particularly in Africa
- Ethiopian princes and Chinese warlord states now make more concerted efforts to unify
- Greece now more aggressively pursues the Greek Nationalism JE where it has claims
- East India Company is now less gung-go about conquering Tibet, but more inclined to target its neighbors in India and Burma
- AI now has a stronger tendency to abolish slavery after Human Rights is researched
- The Great Powers now have a greater tendency to get involved in early Ottomans vs Egypt disputes
- USA and Britain now tend to seek to befriend each other when trying to resolve the Oregon Border Dispute
- France now sometimes chooses to not pursue the Natural Borders JE when given the option
- Fixed a bug where the AI was way too eager to grab treaty ports in places where they had no actual interest in a treaty port
- The US now more aggressively targets the states held by Mexico border it directly at the start, such as Colorado
- Fixed some issues with new attitude changing system that caused the AI to not open up Japan
- The AI now focuses more on befriending Great Powers when on track to complete Earning Recognition
- Added a bespoke strategy and more AI weights for Japan to try to complete the Meiji Restoration
- Fixed an issue where AIs would adopt a Domineering attitude but not actually act on it due to the strategy score calculation not resulting in them wanting any wargoals
- Made the AI more restrictive about mixing generally incompatible wargoals, such as investment rights and subjugation
- The AI no longer has an increased neutrality score in civil wars where they have a truce with the country having a civil war
- The AI is now less inclined to get involved in the German Leadership War so long as neither side starts demanding territory, in which case they will have increased support for the non-expansionist party
- The AI will now be more restrained with what additional wargoals they add in a Unification or Unification Leadership play if they are a primary participant
- Added catalysts for gaining and losing land borders with a country, used to make AI more belligerent when gaining borders with unrecognized powers
- The AI now scales its minimum mobilization level by the number of small conflicts it's involved in, so that it's better at dealing with simultaneous revolts in subjects
- Added a +50 AI acceptance bonus to investment rights proposals if the target country has recently declared bankruptcy. This also means that AI countries who had to declare bankruptcy will be more likely to offer other countries to invest in their country.
- Fixed a bug where the AI would not properly build up its military forces due to incorrect logic when validating its spending
- Subjects with a Defiant or Rebellious attitude towards their overlord now get an appropriate acceptance bonus when asked to support the independence of a fellow subject
- Fixed a bug where some larger countries such as Occitania would become independent when released as a subject
- Fixed a bug where the AI of newly released countries was not properly initialized, causing issues such as no autonomous investment happening

### Performance

- Improved frame rate when scrolling in the Building Registry

### Balance

- The Ottomans now get an increase to Intelligentsia approval & clout while pursuing the Tanzimat Reforms
- Reduced the required army size to complete Tanzimat Army Reforms from 150 to 100
- Reduced minting and output of gold mines by about a third
- Declining to pursue the Opium Wars now angers the British East India Company
- Literate Pops now tend to more strongly support movements to abolish slavery after Human Rights is researched
- Reduced military and war exhaustion bonuses given to Taiping as they currently tend to always defeat Qing
- Reduced the infamy generation against unrecognized reduction from Colonial Offices 3 from 50% to 25%
- Added infamy generation against unrecognized reductions to Colonization and Civilizing Mission techs
- Extended time you have to complete Tanzimat Reforms from 20 to 30 years, due to some of the JEs requiring several steps of law reform
- Tweaked army setup and military bonuses granted to Texas to give them a better chance to survive the Texan War of Independence
- Chartered Companies can no longer switch Government Principles
- Slavery laws no longer directly increase the clout of landowners, as they also do so in a very significant way indirectly
- Unification Leadership wargoal is now considered to be contested if any incorporated state is occupied by the enemy
- War Goals that previously required any state to be occupied to be contested (such as War Reparations) now requires any Incorporated state to be contested
- Increased aggression of Afghan countries towards Chitral
- Afghan minors can now request more aid from Great Powers twenty years after last receiving it
- Gave Maimana Tajik as a primary culture, enabling them to form Afghanistan.
- Non-Pashtun Afghan countries will now be more aggressive towards each other.
- Great Game passive drift now relies on the extent of a country's direct or indirect control over Central Asian and Persian states
- Declaring Bankruptcy now applies a decaying reduction in welfare payments, starting at 100%
- Declaring Bankruptcy now immediately resets all institution levels to 1
- Removed Poor Laws (and the government admins supporting it) from China, as it's no longer needed to 'balance' their budget and tends to result in chain bankruptcy
- Changed the requirements of Pacification of the Steppes to make the journal entry more feasible
- Subjects now require to have diplomatic autonomy in order to sign foreign investment rights and agreement pacts
- You now must be non-Isolationist in order to form a Power Bloc, and Power Bloc members cannot enact Isolationist trade policy
- Sovereign Empires now only half the Cohesion loss from having subjects with high Liberty Desire, and only from the Liberty Desire of the leader's own subjects, not subjects of other members
- Tweaked subsistence income and building throughput for decentralized nations so they don't end up with the highest SoL in the world in certain edge case scenarios
- Significantly reduced the Ericsson company's education access bonus.
- Reduced Leverage Resistance from Population by 50%, as it was too difficult to overcome in some cases even with a variety of leverage sources
- Having the Armed Forces or an Authoritarian leader in government is no longer sufficient to initiate the Natural Borders of France
- Reduced AI aggression from Natural Borders

### Interface

- Added a separate tooltip description for when a building loses employees due to emigration instead of just saying they were fired
- When inviting a prospective member to a Power Bloc you are now given a prediction of what that will do to your Cohesion
- There is now a confirmation box when pressing 'Leave Power Bloc'
- There is now a notification for other Power Bloc members when a non-leader country leaves the bloc
- Made the sortable column header buttons sticky at the top of the Market panel (Goods tab) when you scroll.
- Building Registry filters are now rows of buttons of icons instead of fold out menus

### Modding

- Added new trigger called army_power_projection
- Building groups can now be flagged as always_self_owning, which makes them always worker-owned

### Bugfixes

- Fixed an issue with foreign investment that could cause invalid elements to appear and stay around in the Construction Queue permanently, however this will only prevent the issue from appearing in new saves. We are planning to introduce a save-game validation fix for old saves in 1.7.3.
- The Pamir Delimitation JE tooltips no longer lags the game. A tooltip for the JE activation has been added for clarity.
- Tibet Expedition JE now ends when subjugation demand is refused by other countries.
- Fixed an issue that would cause Formations to sometimes travel towards a Front they cannot join.
- Fixed an issue in the code that handles the relationship between interest groups and political lobbies, which caused misleading error messages to be logged.
- Fixed a bug where using a create_country effect in global history files would lead to blocs being disbanded during initialization
- Unrecognized powers no longer get any benefit from infamy reduction against unrecognized modifier
- Fixed a bug where a number of AI countries (such as Greece) did not pursue their Journal Entries because the catalyst for Journal Entry was incorrectly firing on JE creation instead of JE activation
- Fixed a bug where Journal Entries that were created in an inactive state before the start of the game did not notify the player about their activation due to a rather bizarre (and entirely unnecessary) boolean set on creation
- Fixed column header broken loc in map list panel for inviting countries to your bloc
- Fixed a bug where half of the screen sometimes turned orange during the start of diplomatic plays.
- Fixed a crash that occurred when collecting unit distribution data
- Resolved an issue which caused null objects to occasionally appear in exiles events.
- Power bloc statues are now prevented from being transferred when states change hands to countries that shouldn't have them.
- Fixed a bug where employees would switch jobs without taking potential dividends into account
- Fixed a bug causing government owned buildings to have a hard time filling their employment
- Fixed a bug where the country religion link was referencing the country definition's religion instead of the country's state religion, resulting in the Impose State Religion bloc action being repeatable on the same country
- Remove the duplicated Overlord Actions button for Subjects that appeared when you are not a Power Bloc leader.
- Fixed a bug where cohesion for ideological unions was inexplicably trending towards 0
- Removed the placeholder Manul culture from the game.
- Fixed an issue where the relief option in the STATE Crop Failure event would apply the wrong modifiers.
- Conquering a split state now applies the 'State Liberated' rather than 'State Conquered' modifier, as the latter ended up giving tax penalties to a state you already owned, which could be devastating for tiny nations
- Amended the description for the I'm the Captain now achievement.
- Reduce the freeze during annexation caused by diplomatic catalysts
- Gold Fields are now always worker owned
- Fixed fleets being stuck in ally HQs after losing military access to them
- Fixed invalid travel destination options for formations after switching between interactions
- Fixed an issue that caused the game to try to localize the null country when showing the peace treaty popup when one of the displayed wargoals is a wargoal to conquer a split state and the winner is a country that has a different split state in the same region
- Fixed a bug where it was possible to accept a diplomatic proposal that had become invalid in the time between it was proposed and when it was accepted
- Removed Clergymen from Cotton Plantations' default Production Method and replaced them with Farmers.
- Blocs led by a major power which turns into a great power will now lose the weak bloc modifier as intended
- The Cohesion prediction when kicking a member out of your Power Bloc now takes the per-member modifier impact into account correctly
- Fixed a bug where the reinvestment fraction of Government Dividends was not correctly calculated for buildings unless they had 100% government ownership
- Persia and Afghanistan will now properly get the "Great Game, no re" achievement for winning the Great Game
- Fixed autonomous investment constructing too many levels of the same building
- Fixed a bug where the Commander Order tooltip was not showing requirements to activate orders
- Fixed a bug where the wrong production method for Power Bloc statues was shown in the UI
- Homesteading law now also affects the ranching category buildings in addition to agriculture buildings.
- Fixed a bug where the expedition cost in Tibet was still active after the journal entry ended.
- Fixed a construction queue tooltip to indicate that the constructing country is paying the cost
- Added a missing collectivization modifier to collectivized agriculture.
- Fixed a bug for Tibet Expedition Events so it doesn't result in the possibility of Tibet's diplomatic play against itself.
- Fixed a bug where sometimes Treaty Port status would get 'dropped' by markets, resulting in the Treaty Port having no effect despite showing up properly in the state
- Most hills in Japan, North China and Manchuria no longer display as jungle hills in the state panel
- Fixed an issue where Russia would start the game with three landlocked naval bases.
- Fixed a bug where the AI would not use certain actions such as grant own market due to a missing evaluation_chance value
- Fixed an issue with an unlocalized, dynamic name for Azerbaijan.
- Diplomatic Plays can no longer start if the initiator or the target country has no passable provinces
- Fixed an issue where throughput was not correctly updated during building initialization
- Academic caps and glasses are now restricted to characters with relevant traits, even within power blocs with the level III Advanced Research principle.
- Cuirasses are now restricted to characters with either a royal or military affiliation.
- Fixed a bug where it was possible to oppose the subjects of your allies in plays where it would not be possible to object the ally themselves
- Fixed the missing text for the currently enacting Law under the specific Law Group.
- Fixed an issue where the AI would sometimes not construct ports to connect isolated states to its market
- Fixed an issue in how some principle groups were displayed in the principle groups chooser window
- The indicators for what production method is selected in each category for buildings in your country no longer takes foreign buildings into account, so if all your domestic buildings use the same PM it will show that rather than the "mixed" indicator if some of your overseas buildings are using a different PM
- Fixed a rare crash when hosting in Multiplayer
- Fixed a major issue that would prevent upgrading power bloc principles under some circumstances

## 1.7.3

Patch 1.7.3 was released on 2024-07-04[3] with checksum *8769*.

### Bugfixes

- Fixed an issue where privatization was not correctly checked sometimes, resulting in money being spent to privatize building levels that were already privatized
- Fixed a rare Out of Sync caused by unsorted collecting from unordered map
- Fixed a major issue that would prevent upgrading power bloc principles under some circumstances

## 1.7.4

Patch 1.7.4 was released on 2024-07-10[4] with checksum *5775*.

### Content

- Added a journal entry for the reunification of China

### Improvements

- It is once again possible to start Reduce Autonomy & Annex Subject diplomatic play against subjects, even if their Liberty Desire is high. However, doing so will result in taking on the full infamy cost of the wargoal rather than the usual reduction for targeting subjects.
- Peasant Levies now simply prevents Conscripts from being raised as Cavalry or Artillery, as selective limits on which specific types of Infantry etc could be raised as conscripts do not work correctly
- Russia/Britain now start with a neutral attitude towards Persia, ensuring they don't immediately go for the throat until Persia does something to earn their ire
- Reduced the rate at which "The Russian-British Agreement" fires for player Afghanistan during the Pamir Delimitation
- Added Vilnius to the required states for Poland-Lithuania
- Renamed "Semireche" state to "Semiplatinsk"
- Removed Uighur homeland from Semiplatinsk
- Autonomous Investment is now able to execute multiple investments per tick for countries with extremely large (500k+ income) investment pools, so that even massive economies can continue to make full use of the investment pool
- Homesteading & Collectivized Agriculture now also impacts subsistence farms, causing them to be partially or fully self-owned and adding some Farmers to the Workforce
- Military Treaty Power Bloc leaders can no longer enact National Militia, and Religious Convocation Power Bloc leaders can no longer enact Total Separation or State Atheism
- The Cohesion in Military Treaty Power Blocs is now impacted for any member with the National Militia law, while the same goes (to a greater extent) for members of a Religious Convocation Power Bloc who has Total Separation or State Atheism
- Defensive Cooperation II now permits the Power Bloc leader to impose their Army Model law across the Bloc
- Treaty Ports are now only functional against a market if they are adjacent to an incorporated state from the market
- Moved or removed some military units from formations in the history setup so that they adhere to the law set in that country.
- The 'overlord compliance' AI strategy is now invalidated if the subject ends up opposing their overlord in a diplomatic play
- Power Bloc statues are now removed when leaving a Power Bloc
- The Autonomous Investment AI should now properly focus on Privatization when construction is blocked due to a lack of workforce or infrastructure
- Under Cooperative Ownership, buildings in foreign countries that are owned by local Manor Houses & Financial Districts will now be collectivized by the workforce in those countries over time

### Interface

- Added a new entry for "Your Leverage" to all country's details panel.
- Removed tooltips for some modifier values to reduce duplicated information

### Performance

- Improved Construction Lens performance after having opened it once before. Note that the first time will still be slow.

### Balance

- Restored the +clout modifiers to Landowners from slavery laws, as the Landowners ended up too weak in some countries after other related balance changes to subsistence farms
- Reduced Advanced Research 3 principle's max innovation gain per institution level from 15 to 10
- Political Movements to get rid of Traditionalism and Serfdom now attract more supporters from literate pops once Empiricism is researched (loosely representing enlightenment thinking)
- Increased the lobby appeasement impact of Support Regime
- Haiti now starts the game with debt instead of half-filled gold reserves
- Haitian independence payments now cost less each week but much more to pay off in increments
- Fix some setup issues in France that caused the July Monarchy to collapse too quickly due to unprofitable buildings and trade routes
- Improving Relations will now give leverage on yourself, and will not auto-break at 50 relations if the target is a Power Bloc leader
- When a civil war ends in victory for either side, a larger number of pops are now deradicalized to represent civil war fatigue and prevent a second civil war from immediately gaining steam
- Italian states with relations above 20 with Austria will no longer be able to spawn Italian radicals in it.
- Reduced Austrian radical gain from Italian minor powers.
- Divided Monarchists now requires 50% radicals in capital to fail (up from 25%)
- Reduced the number of radicals generated over time by Movements to Preserve
- Lowered the base and max weights for Wine in luxury drinks need, as adding it to Intoxicants made it overdemanded compared to other goods and hurt the demand for Tea/Coffee
- Take Treaty Port can no longer be added as a wargoal against a state without a port constructed, as this results in an inactive treaty port. However, demolishing the port after the wargoal is added will not invalidate the wargoal.

### AI

- The AI is now more inclined to accept requests for Support Regime and Knowledge Sharing under favorable conditions
- The military power score increase for accepting reverse-sways is now properly capped at 50, preventing the AI from accepting reverse-sways that they should be utterly unwilling to accept
- Rebalanced AI aggression. The base aggression (chance to start diplo plays) is lower, but the impact of the aggression game rule on it is higher. However, the impact of the AI aggression game rule on strategic desires was toned down, so that aggressive AIs still try to make strategic alliances etc.
- Fixed another bug causing the AI to take a bunch of Treaty Ports they should have no real interest in
- The AI is now significantly more likely to try to get rid of Traditionalism and Serfdom when not pursuing a conservative agenda or when there are movements present to change those laws
- Fixed the logic for when the AI carves up china to be more consistent in how and when it's applied to the AI's desire to take states there
- More tweaking of the AI for Egypt/Ottomans early conflicts to give the Ottomans a better chance of beating Egypt
- Fixed a bug where the AI would not correctly evaluate Placated political movements as able to start a revolution and would cancel laws that would result in a very powerful evolution to avoid a much weaker one
- The AI is now generally less willing to cede territory when Demand State is used when that is territory is important to its owner, even if it's owned by one of their other subjects
- Fixed some issues with AI strategy logic for isolationist countries which was inadvertently applied to non isolationist countries, causing the AI to generally avoid befriending other countries
- The AI will now never accept having 'cut down to size' pressed on them as part of a peace deal, but will have to be capitulated
- The AI will now try much harder to get rid of peasant levies unless they are very reactionary
- The AI will now make use of Enforce Military Access on its subjects to create fronts when needed in wars
- Fixed an issue where the AI was setting way too high targets for its army/navy size (partially caused by AI including investee countries in its population census)
- The AI is now far less willing to give up wargoals in peace deals unless those wargoals are actually being contested
- The AI will now instantly capitulate in a war where they and all their allies are 100% occupied
- The AI is now more likely to target their own domestic states and subjects with government-funded constructions, and less likely to target foreign states. This change does not impact autonomous investment, which has its own logic for domestic vs foreign

### Modding

- Added new trigger has_inactive_journal_entry
- Added scripted list war_participant (any_war_participant/every_war_participant etc)
- Added console command ai_evaluate_mobilization to print AI mobilization data

### Bug Fixes

- Fixed a crash that occurred in the MP lobby while the game was unpaused
- Fixed a bug where it was possible to use Demand State against your overlord's homelands
- Fixed a bug where if you saved the game on the exact tick when a country was annexed and then loaded that save, the country would never be properly removed causing diplomatic pacts with it etc to linger forever
- Fixed a bug where it was possible for foreign investors to buy worker-owned buildings in countries with Cooperative Ownership enacted
- Fixed the issue with invalid diplomatic pacts in the outliner
- Fixed a bug where Agitators who did not have a valid law from their ideology to support would almost always end up picking from just a tiny handful of laws to start a movement for (Homesteading and National Militia, for example)
- Fixed some issues with the changes to Honorable Restoration that made it too difficult to complete when not going the traditional market opening route and ensured it's always completed when you defeat the Shogunate in a civil war
- Fixed sorting trade routes by owner in the trade routes panel
- Fixed an Out of Sync related to diplomatic catalysts
- Fixed trade routes being incorrectly moved to another market after a market split
- Fixed some production methods being incorrectly considered unavailable in the building panel
- Fixed some issues with conscripts after states being transferred to another country
- Fixed a crash that could happened when showing modifier breakdowns
- Debts accrued just after declaring bankruptcy now count as debts rather than disappearing in a powerful bout of creative accounting
- Fixed some mobilization options not properly providing their benefits to combat units
- Fixed an issue causing predicted loyalist changes from successful enactment of political movement to not apply or apply incorrectly
- Savegames are now cleaned of broken construction queue items when loaded
- Fixed a bug where Pops that got all their income from dividends would not pay poll taxes (ie, Capitalists and Aristocrats now pay about 0.1% more taxes compared to before)
- Replaced the static english text for "Inactive Treaty Port" with a string that is translated into all languages
- It is no longer possible to sway-transfer subjects that are opposing their overlord in a play or war
- Fixed a bug where the 'Join Power Bloc' diplomatic play would not work correctly after a country declined an invite to a power bloc
- Fixed a bug where downsized military buildings would not properly remove the units from their formations
- Tanzimat JEs are now pinned by default.
- The Tibet Expedition decision will no longer spam errors when Tibet is annexed
- Power Bloc emblems are now properly centered
- Adjusted inconsistent conditions of Grant and Request own market. You can now only do these actions if the junior partner is either a direct subject (compared to indirect before) or if they are independent and you are the Power Bloc leader in a shared market.
- Removed the Liberty Desire impact display from the Grant Market interaction if the target is not actually a subject.
- The Disrupt the Russian Caucasus Great Game subgoal now fails properly if Circassia is defeated
- Updated descriptions for migration laws to reflect that they only limit migration in and out of the country
- Fixed a construction queue tooltip to indicate that the constructing country is paying the cost
- Rewrote the placeholder tooltips on the column headers when sending a Military Formation somewhere (Destination, Travel Time, Status).
- Fixed a bug that would lead to foreign investments in split states potentially leaving around NULL_OBJ constructions in the investor's queue; particularly visible when pursuing German unification.
- Fixed a bug where decreasing relations with your overlord would have a lesser impact on lobby appeasement than increasing it, making it possible to endlessly increase appeasement by alternating increasing and decreasing relations
- Resolved an edge case where the Strike: Labor Negotiations event could have no options.
- Removed Liberty Desire impact from insufficient supply if a land connection exists between subject and overlord
- Added impact on Ranching building group to Collectivized Agriculture law
- Amended the India collapse script to account for the Princely States being transferred to Britain
- Interface: Fixed a bug that was hiding lobby funding in the budget breakdowns
- It is now possible to add the Force Nationalization wargoal to an ongoing Diplomatic Play
- The "Secure Influence Over Persia" Great Game subgoal may now progress by annexing Persia
- Fixed a bug where the Weak Power Bloc penalty would not be applied after loading a save
- Fixed several issues with Cohesion factors not being correctly displayed in the Cohesion tooltip

## 1.7.5

Patch 1.7.5 was released on 2024-07-12[5] with checksum *6fe3*.

### Balance

- Reduced starting radicals for countries with historical radicals, such as Argentina and Central America
- Reduce the Infamy gained by Tibet's overlord if they refuse Tibet's subjugation in Tibet Expedition

### AI

- Fixed incomplete logic for AI evaluation of granting states to unrecognized and autonomous subjects, allowing USA to grant states to Indian Territory when it shouldn't

### Bug Fixes

- Fixed Private Investment Pool behaviour under cooperative ownership
- Aristocrats no longer starve due to Subsistence farms suddenly raising wages for peasants
- Infamy cost reduction for rebelling subjects is now properly applied to rebellious subjects not loyal subjects

## 1.7.6

Patch 1.7.6 was released on 2024-08-28[6] with checksum *4b8b*.

### Improvements

- Protectionism now has a +25% leverage resistance effect

### AI

- The AI will now prefer to first cancel constructions of government buildings over demolishing existing ones when trying to save money
- Reduced AI naval spending targets from having a large overseas empire, to prevent excessive British overspending on the navy

### Interface

- Added the prompt saying "CTRL + click to set the levels to a minimum/maximum" directly to the Nationalization popup for better visibility.

### Bug Fixes

- Fixed the bug when guarantee independence wouldn't join if the diplomatic play that was started outside of the current interests
- Fixed a bug where it was possible to Enforce Military Access on a subject who is opposing their overlord in a play or a war
- Fixed a bug where the AI would sometimes not merge back temporary formations into their parent formations, resulting in a large number of armies with few or no battalions in each
- Fixed a bug where the AI would not evaluate Investment Rights and Join Power Bloc wargoals correctly when calculating its desire to dominate another country, resulting in adopting a less aggressive attitude than intended
- Fixed CTD related to front distribution cache
- Fixed a bug where the AI would use 'Grant own Market' on subjects in cases where it did not make sense to do so, such as Austria granting Krakow their own market due to low supply network strength
- Fixed bug where Force Nationalization Wargoal would only take state-owned buildings from the target, ignoring private-owned ones
- Fixed the bug when government buildings couldn't promote employees
- (Mac CTD fix) Fix/potential stack overflow in cpdxguitextdata
- Fixed the bug when fleets in non-home HQs wouldn't recover from being defeated
- Fixed a bug where Military Formations could establish a new basecamp somewhere else when they already had a valid one.
- Fixed a crash to desktop that could happen upon enacting cooperative ownership
- Now subjects subjugated through power bloc action will properly update ports and markets

## 1.7.7

Patch 1.7.7 was released on 2024-10-31[7] with checksum *e2e5*.

### Additions

- Added new game rule to enable or disable fantastical/supernatural content. If this game rule is enabled, there is now a new character with some new events that can make an appearance during the real life months of October and November.

*And as a bit of information: You can change game rules mid-game by clicking switch country then changing the game rules in the select screen!*

## References

1. ↑ Forum, [Victoria 3: Hotfix 1.7.1 is now LIVE!](https://forum.paradoxplaza.com/forum/index.php?threads/1691816), 2024-06-27.
2. ↑ Forum, [Victoria 3: Hotfix 1.7.2 is now LIVE!](https://forum.paradoxplaza.com/forum/index.php?threads/1693479), 2024-07-03.
3. ↑ Forum, [Victoria 3: Hotfix 1.7.3 is now LIVE!](https://forum.paradoxplaza.com/forum/index.php?threads/1693700), 2024-07-04.
4. ↑ Forum, [Victoria 3: Hotfix 1.7.4 is now LIVE!](https://forum.paradoxplaza.com/forum/index.php?threads/1694727), 2024-07-10.
5. ↑ Forum, [Victoria 3: Hotfix 1.7.5 is now LIVE!](https://forum.paradoxplaza.com/forum/index.php?threads/1694991), 2024-07-12.
6. ↑ Forum, [Victoria 3: Hotfix 1.7.6 is now LIVE!](https://forum.paradoxplaza.com/forum/index.php?threads/1701215), 2024-08-28.
7. ↑ Steam, [Halloween Update 1.7.7 is now LIVE!](https://store.steampowered.com/news/app/529340/view/4478359995220492336?l=english), 2024-10-31.
