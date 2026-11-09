---
title: Patch 1.5
source: https://vic3.paradoxwikis.com/Patch_1.5
pageid: 5392
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
**Patch 1.5**, aka "Chimarrão", was released on 2023-11-14[1] with the checksum *4aef*. It was released alongside the [Colossus of the South](Colossus of the South.md) region pack. It was originally released as an open beta[2] (patches 1.5.0 to 1.5.6) with patch 1.5.7 being the first official public release in the 1.5.X branch.

## Major features in update 1.5

- Military Formations: Armies and Fleets can now be created and disbanded. You assign both commanders and units of specific types to them. All military configuration and control like unit hiring, upgrading and disbanding (including Conscription battalions) is now done through Military Formations, rather than through buildings (like barracks) and individual commanders. Disbanding units recognizes keyboard modifiers (shift/ctrl); note the tooltip is not updated to reflect this yet. Military Formations have an Organization score, which impacts Recovery Rate, Offense/Defense, and Morale Gain, and a Supply score which impacts Morale recovery. Also we added icons and colors for the customization of a Military Formation's visual identity.
- Mobilization Options: A tab available on Army formations lets you configure how much extra goods you want your armies to consume when mobilized, with benefits provided to all units in the formation at a goods cost per unit.
- Travel Network: Created a travel network based on state hubs and ocean nodes. Added functionality for 3D models to move over the travel network for formations. Added graphical arrows for formation travel. Military Formations will update their travel path costs/speed if connections on their route change. When a Formation fails to find a Travel Network path, it will now notify and station Formation at the closest accessible HQ/Sea Node.
- Frontline and Battle Graphics: Rather than a single battle diorama across the front when a battle is happening, you can now see your own and enemy armies spread out across the frontline at all times. Detailed battle dioramas will spawn when battles break out in a state. Units will wear uniforms indicating which country they belong to and will be wielding weapons and other accessories (artillery, horses, etc) suitable for their type. Mobilization Options such as air surveillance can also have a strong visual impact.
- Multiple Simultaneous Battles: Generals on a Front now each advances independently of the others and can start multiple simultaneous battles on a Front, one per state, deeper and deeper into the state as occupation is gained
- Shared fronts and State-based Battles: Fronts adjacent to two or more allies in the same war will now be contiguous, preventing the proliferation of fronts that could result in unmanageable gameplay. Furthermore, fronts now only move when a sufficient number of battles have been won to completely occupy an entire state, making front movement a lot more predictable.
- Companies: Each country now has a number of company slots which increases from technology and laws. A company has a number of associated building types, and improves the throughput and construction speed of those building types in its country. If a company's buildings have high productivity compared to the global average, the company will gain Prosperity over time and unlock a special bonus modifier. There are a number of basic companies that are available to all countries which can construct their associated building types, and about 100 special flavored (mostly historical) companies which are generally upgraded variants of basic companies and may be available due to factors such as culture or which states you own. A small number of countries start with a predefined historic company at game start.
- Local Prices: The degree to which the Market can influence the price on goods in a State is now capped by the Market Access Price Impact modifier. This means that local production and consumption will now always matter when determining the price of a good in a state, creating the opportunity for local synergies and supply chains. Unincorporated States have -10% state access price impact.
- Reverse Sways: It is now possible for a participant in a diplomatic play to offer support to either side in exchange for a desired sway
- Trade States: Implemented 'Trade States' diplomatic action that allows a country to either give away a state, request a state from another country, or offer to trade one state for another state
- Alert Settings: You can now customize which Alert types should appear inside / outside the Important Actions ball. Added a message settings tab for Alerts and Important Actions in the Message Settings window.
- Pollution: now has mechanical effects and is fully exposed in State and Building panels: high pollution now gives a malus to mortality, standard of living and migration attraction. This malus can be counteracted by the health insurance institution. Also added a map mode for pollution.
- Unit Experience: Added experience gain and veterancy levels to units. Experience is gained over time, more during battles and lost when reinforcing after taking losses.
- Commander orders: You can now always adjust Commander Orders to whatever you like at any time. If they cannot switch to it immediately (because they're in battle) they will do so at the earliest opportunity. Orders have been streamlined and indicate how the Commander should behave now, which is detached from any sort of target location. Several new Orders have been added as well, most of them unlocked by having specific Commander Traits and Military Formation composition. The default General Order has been changed to Advance, in order to make Armies at a Front active instead of passive by default.
- Naval Invasion Planner / Panel: New interfaces and mechanics for improved control and insight into your naval invasions. The Stand By and Naval Invasion commander orders have been removed. You now start Naval Invasions via Military Lens or Formations.
- Implemented a feature where each time an Admiral loses a battle, he's marked as defeated. When a fleet is composed of only defeated admirals, it's forced to return to its home HQ. Once reaching the HQ all defeated flags are cleared.
- Fleets now have a Presence in a Sea Node which affects the effectiveness of Admiral Orders in that Sea Node. Presence is reset whenever a Fleet moves.
- Naval Orders in a Sea Node are now visualized on an emblem surrounding the node
- Fleets and ongoing wars are now listed in Sea Region Panel
- Animations for both Army and Fleet Battle dioramas have been added to indicate Defeat and Victory
- Added an Impose Law on Subject feature with interface for overlords to force their subjects to change laws
- The "Start Diplomatic Play" interaction has been changed into "Make Diplomatic Demand". This allows one country to demand a single war goal from another, which if rejected will start a diplomatic play for that wargoal. It is possible to bypass the demand phase and start a diplomatic play right away (useful if you want to make multiple demands for example).
- Services, Electricity and Transportation are now local goods whose prices are fully set based on local production and consumption and whose market price plays no role at all
- Added new Frontier Colonization Law
- Units can be upgraded over time to the currently selected Default Unit Type for their group (infantry, artillery, cavalry) by pressing the according button.
- Barracks and Conscription Centers PMs that dealt with unit types have been removed for the most part. A new Training category has been added instead.
- Added a commander right-click option to quickly split a single commander into their own formation, bringing a fraction and composition of units commensurate with their command limit when compared to the overall command limit of the formation as a whole
- Added a bi-directional transfer popup to exchange units and commanders between Military Formations
- Armies can now be demobilized during wars, leading to them returning to the closest HQ and gradually reducing their mobilization consumption over 3 months
- Pursuit, Panicked Retreat, and Controlled Retreat battle conditions have been added to ensure very lopsided battles end quickly
- Added tutorial lessons for establishing a Company and creating a Formation
- Replaced Chile with New Granada as Recommended Country for the "Learn the Game" Objective
- Prussia, United States, Mexico, Texas, Russia, Ottomans, Egypt, Austria, Brazil, France, Sikh Empire, Great Britain, British East India Company, and China now start with Historical Formations
- Added new formable countries - the Holy Roman Empire/United States of Europe, United Netherlands, Rio de la Plata, the Confederation of the Rhine, Maghreb, Pakistan, and Turtle Island
- Added a new pop property called Job Satisfaction. Pops will now evaluate their satisfaction with their current job and factor this into their employment decisions.
- Reworked Revolutions to properly support Commanders, Units and Formations to defect to the revolutionary side
- There are now explicit Demands/Plays/Wargoals for increasing or reducing the autonomy of a subject. The autonomy scale for subjects goes Protectorate -> Dominion -> Puppet, Tributary -> Vassal, while a Personal Union can be turned into a Puppet/Vassal/Protectorate/Tributary if autonomy is increased/decreased
- Added new Vineyards building and Wine growing potential for states, particularly in Europe and Middle East. Removed Wine production from Farms.
- Added new Explosives Factory building
- Split Arms Industries into two buildings, Artillery Foundry now produces Artillery exclusively
- Radical pops are now more drawn to opposition interest groups, and Loyalist pops are more drawn to government interest groups
- Added "Foster National Agitation" character interaction for friendly agitators, allowing nations to use them to stir turmoil in cultural homelands owned by foreign powers
- Production methods can now specify that they require access to particular goods to be able to be activated
- Adjacent states without potential travel connections now get auto-generated 'undeveloped' crossing connections

## Improvements

- Added native Apple Silicon CPU support
- Army and Navy formations now get a generated name based on numerals and country adjective. Moreover, the player can now rename each individual formation.
- It is now possible for the player to rename companies
- Added the Call Ally sway which can be used to sway an ally (Alliance if initiator, Alliance or Defensive Pact if target) to your side in a diplomatic play. This sway offers no additional acceptance score but also doesn't promise anything to the ally.
- Added the Become Subject sway which allows you to offer to become the Subject of a country (and consequently offer a country to become your Subject) in exchange for Diplomatic Play support
- Added the Transfer Subject sway which allows you to transfer one of your Subjects (and consequently offer a country to transfer their Subject to you) in exchange for Diplomatic Play support
- Added the Transfer State sway which allows you to transfer one of your State (and consequently offer a country to transfer their state to you) in exchange for Diplomatic Play support
- Added the Diplomatic Pact sway which allows you to offer certain Diplomatic Pacts such as Trade Agreements, Customs Unions and Bankrolling to a country in exchange for Diplomatic Play support, with a forced duration of 5 years if accepted. Bankroll pacts resulting from this do not generate any Obligations while their forced duration is in effect.
- Adding a wargoal against a neutral enemy subject to a play now also forces the targeted subject to become part of the enemy side in the play so the wargoal can be properly contested
- Added a slew of resource potentials to Persian states, including tobacco, dye, iron, coal, wine, silk, and cotton. Big thanks to Samitte for all the wonderful data and ideas!
- Added additional homelands to Iranian states to account for the country's Arab, Kurdish and Turkmen communities
- Added 28 new state traits to the game, and reworked some existing ones
- Added progress bars and attack/defense stats to Front panel and Sea Node Panel
- Interest Groups will now only launch Petitions for laws that are potentially able to be supported by a political movement
- It is now possible to start Liberate Country Diplomatic Plays, with the country to be liberated being picked from a selection list in the confirmation popup
- It is now only possible to demand annexation of a Puppet or Vassal
- Buildings will no longer raise their wages to try and hire additional employees unless they can maintain a decent profitability after accounting for the increased employment
- Buildings will no longer 'snipe' employees from other buildings unless they have a high enough productivity compared to the target building to ensure this doesn't result in an endless back-and-forth wage race between the two buildings
- Buildings will no longer hire employees if doing so would result in them becoming unprofitable after accounting for wage and production changes
- Wargoals are now only considered to be contested when a state is fully occupied, partial occupation does not count
- Added a new state penalty to birth rate proportional to the unemployment rate in that state
- Added a new pop penalty to birth rate proportional to the literacy of that pop
- Updated the music system so that all tracks have a “relaxed” mode
- Redistributed resource potentials for coal, iron, and lead in Brazil, and moved the Serra dos Carajás modifier to Para
- The suzerain of one of the primary participants in a diplomatic play can now take sides before the closing phase. Previously they could not join the diplomatic play after the end of the initial phase.
- Battles were detached from the front line border and can now happen in other provinces within the state
- Added historical naval setups for all major and minors naval powers
- Added historical army setup for all German and Italian minors, and Scandinavia
- Subjects are now blocked from backing a side in a diplomatic play if their overlord is backing the other side. When backing a side in a diplomatic play as an overlord any subjects of yours on the other side will now be forced to become neutral, taking a relations hit in the process.
- Added Severe Malaria State Trait icon, modified Malaria State Trait icon
- Changed Military map mode colors to match the colors for Military related map markers
- Removed field promotions, as they are no longer relevant in the context of military formations
- It is now possible to decline a sway offer that is calling in an obligation, though doing so will repudiate the obligation with all associated penalties
- Allies are no longer automatically added as backers in Diplomatic Plays, but have an increased support score towards their ally
- Illegitimate governments may now only enact laws that have support from a Political Movement rather than being blocked from enactment altogether
- Countries now have a certain number of 'free' trade routes before additional routes start costing bureaucracy to maintain. Trade Routes that are free due to Trade Agreements do not count towards this cap.
- Diplomatic Play/Demand/Wargoal Make Puppet was changed into Make Protectorate, Make Vassal was changed into Make Tributary, and Make Dominion was removed
- Power Projection is now a calculated value based on the total average Offense & Defense of army/naval units (multiplied by manpower), and provides a largely accurate measure of a country or formation's total combat power. Modifiers that used to increase Power Projection now instead increase Prestige from Army/Navy Power Projection.
- Number of maximum commanders per country is now removed, in favor of a limitation of max 4 per Formation
- Command Limit is now aggregated on the Formation level, with a soft penalty (Organization limit) for exceeding it
- Government Administration, Power Plants, Universities, and Skyscrapers are now Development buildings
- Replaced anachronistic 1955 hammer and sickle design with more period-appropriate design in the vast majority of cases
- [Voice of the People] Reworked the Paris Commune to create a more interactive and competitive experience against the AI
- Health Insurance laws now have a few more varied effects (e.g. higher standard of living for different strata, increased Petite Bourgeoisie political strength)
- Added functionality for Formations that cannot find a path to always try to station at nearest HQ or Sea Node
- Improved Map Interaction for adding Conscripts
- Adjusted Army Laws to the new system. Peasant Levies will have a limited set of units which are allowed to be recruited under them.
- [Voice of the People] The Paris Commune now inherits the Journal Entries and variables of France if it ends up winning
- German/Italian unification candidate now inherit the incorporation status of any countries they annex as part of the unification event chains (but not the wargoal)
- Removed diplomatic actions to become/demand subject and ask for independence (these are now done through diplomatic demands instead)
- AI now takes more factors into account when deciding how many construction sectors to aim for. Countries with large investment pool incomes in particular will focus more on expanding their construction potential.
- Regime change now changes all laws in Governance Principles to match the wargoal holder's law, assuming the two laws differ too much ideologically and that the law change is not blocked by technology or other laws that are not being changed
- Engineer and Master Bureaucrat character traits now have new effects for agitators
- Women's Suffrage is now available under Anarchy
- A new building's wage rate is now initialized to whatever the average needed wage would be to sustain wealth levels in the state
- Buildings now evaluate wages more frequently when they're unprofitable
- It is now possible to select already mobilized armies for naval invasions
- If a military formation has more combined special units (e.g. artillery, cavalry) than it has default units (e.g. infantry) its Organization Limit is now penalized
- Failed naval invasions now clear all occupation by that country unless there is an active front against the invaded state in the same war
- Mass migration targets now always receive some amount of migrants, with the rate determined by secondary factors
- Decreased the amount of food from Subsistence Farms from 2.5 per level to 2
- Allowed Russia to initiate the Alaska Purchase
- Gave Japan the Frontier Colonisation law
- Changed the on map color for "on the fence" and "leaning" countries in a Diplomatic Play to orange from blue
- Updated the military lens to show formation/hq markers at all zoom levels
- Added notifications for canceled travel paths towards Fronts/HQs/Sea Nodes/Tracked Formations
- Undeveloped travel connections from/to harsh environments (mountains, deserts, jungle, etc) received the 'harsh undeveloped' type, which is extra slow
- Added military marker movement smoothing for player formations, while on the spline network
- Added four new Persian state traits, the Alborz and Baluchi mountains, the Hyrcanian Forests, and the Bam-Narmashiri Oasis
- Replaced a bunch of anachronistic Persian city and regional names with more appropriate ones
- Increased Iranian arable land across the board
- Disbanding a unit now selects the least experienced unit
- Adjusted various Military related tutorial lessons to the new system. Note that a lot of steps do not have custom button highlighting and other support you might usually expect yet.
- Liberate Country now gives the releasing country claims on any incorporated states that are lost
- Base rate of Conversion and Assimilation is now reduced by the ratio of radicals in the pop (so a pop with 50% radicals gets only half conversion/assimilation)
- Navy Power Projection now directly contributes to a country's max declared interests, instead of max declared interests coming from naval bases
- Combat Units now always recover Morale outside of combat, but at a slower rate if they're above Formation Supply
- You can now toggle mobilization options on or off even while mobilized, but in some cases at a cost to Organization or Morale
- You now suffer a temporary Organization penalty when transferring units between armies with different Mobilization Options
- Prevented creating empty AI formations by creating a unit with it
- Kazan now has the Sunni state religion
- Transferred the state of Ceylon from the East India Company to Great Britain
- Fertilizer from Ranches is now produced as a byproduct of Sheep Ranch PMs rather than meat-producing PMs, and require Intensive Agriculture for Ranch fertilizer production to be possible
- The amount of slaves imported each week by a state now depends on some additional factors such as arable land and the population of the exporting state
- When two formations merge, the resulting formation inherits any custom naming
- Improve Access to Consumer Goods is no longer required to complete the tutorial
- Rice Farms now have double the Employment and Production
- Government Run Production Method for Plantations now gives Government Shares
- Vacuum Canning is now called Meat Packaging and consumes meat and fish instead of just fish
- The Trail of Tears now directly kills affected Native pops
- Liberia is now an American protectorate from game start
- Canadian colonies now transfer their claims to one another when merged by decision
- Gave Daniel Webster the Republican ideology
- Certain subjects, such as the East India Company and East Indies, now take the first part of their name from their overlord so that if they end up under a different overlord you get 'German East Indies' or 'French East India Company', etc.
- Removed Vineyards Production Method from Wheat and Maize Farms
- Added railway connection between Fort Douglas,Sudbury and Val-d'Or
- Added dirt road connection between Val-d'Or/Chicoutimi and Quebec/Fredericton
- City of Bona position moved to be within French-owned territory
- Added alternate colors for Spain, Communist Austria, and Austria-Hungary
- Changed Communist Germany's color to dark red
- Changed Judaism's color to light blue
- Added custom localisation and ideology to the American Rural Folk

## AI

- The AI is now more likely to offer support to a side in a diplomatic play if they are already leaning towards that side
- The AI is now more likely to attempt to sway an undecided country in a diplomatic play if that country is already leaning towards their side
- The AI will now actively attempt to sway countries that are already committed participants on the opposite side into switching sides
- Fix an issue where the AI would activate anchorages over proper ports due to overvaluing the workforce reduction they provided
- Fix an issue where the AI was calculating its gold reserve and income surplus targets incorrectly for some types of spending
- AI should now be better at setting up trade routes for goods that are important for their economy to import or export
- AI should now be better at importing key industrial goods like rubber if they don't have those goods in their market
- AI countries with a very high GDP, such as China, are now much less willing to join Customs Unions
- AI now sends fleets to different sea nodes if at war
- China will no longer be willing to join Customs Unions whilst it is still a major or great power
- The AI now places more value on holding obligations on diplomatically relevant powerful countries, even if they're just Wary towards them
- The AI will now be less likely to use restrictive export tariffs on goods which they have substantial unused potential for in their country, and less likely to use restrictive import tariffs on goods which they do not have substantial unused potential for in their country
- AI Great Powers are now much more keen on launching and joining Cut Down to Size diplomatic plays against Pariah countries
- AI is now less inclined to jump into diplomatic plays to gain new subjects unless they are domineering towards those potential new subjects
- AI is now less willing to give away its subjects for support in a play
- AIs are now less inclined to gain sympathy for a side in a diplomatic play just because they are facing overwhelming odds unless those overwhelming odds also come with harsh demands
- AI now takes the infamy of the starting wargoal more into account when determining whether to be sympathetic towards the target of a play
- AIs are now less inclined to back a country in a diplomatic play just because it's facing a country with relatively high infamy (that isn't a Pariah)
- AI is now very reluctant to remove declared interests that are supporting growing colonies
- AI now does less concentration of industries in a few states if this doesn't make sense to do due to local price situation
- AI now properly checks whether the target/target's overlord of a wargoal is able to capitulate when considering whether the wargoal can be achieved through capitulation
- Russia will now be more aggressive towards Central Asian subjects
- Fixed an issue where some AI strategies did not work correctly due to a bad is_adjacent check against states
- AI is now generally less willing to trigger revolutions when enacting laws unless they are doing so to avoid another revolution
- The AI is now willing to enact laws with a lower chance of success if those laws have a revolutionary movement or government petition behind them
- Fixed inconsistent triggers in government petitions that were creating problems for the AI in following through on them
- AI now prioritizes universities more unless it is very close to its innovation cap
- The AI is now less keen to get involved in plays when they have a truce with either primary participant
- Liberate Country now has the liberated country start with a friendly AI strategic desire towards the releaser, and an antagonistic one towards their former oppressor
- Fixed a bug where the AI would start and then immediately cancel bankrolling
- AIs with Economic Imperialism are now more likely to take a Treaty Port instead of demanding Open Market against an aggressive isolationist country
- Economic Imperialism AIs now only care about opening up the market of countries with at least 5 million GDP
- AI Austria will now annex Krakow properly
- Added three new AI strategies tailored for Council Republics
- Council Republics are now more inclined to enact progressive laws and develop industrially
- AI Council Republics may now dissolve their colonial institutions

## Balance

- Adjusted some Commander Trait values to balance the addition of the new Orders
- Made high tech tier countries gain the new Corporate Charters technology at game start
- Colonial exploitation law now lowers manufacturing throughput in unincorporated states by 10%, but boosts throughput of mining, plantations, rubber and logging by 20%
- Diplomatic Demands/Plays that do not involve taking territory (such as changing autonomy or law changes) now generally are not blocked by having high relations
- Added Machined Steel Tools Production Method to Tooling Workshops that can be unlocked with Vulcanization technology
- Agitators no longer interfere in the enactment of laws they have no stance for
- Rebalanced starting situation for several countries to minimize unprofitable buildings at game start
- Rebalanced pop growth leading to more evenly spread growth between SoL 5-20
- Removed the Equipment Adjustment Modifier from switching Training PMs
- Adjusted a couple of important countries's starting building in relation to Military goods production
- Reduced overall level of service production (as well as input goods) on urban centers
- Revised modifiers & state traits that affect agriculture throughput to also affect ranching and plantations where appropriate
- Manufacturing, Government and Military buildings now have lowered throughput in Unincorporated States
- Reduced technology cost for era 3, 4 and 5 techs
- Extensive revisions to Wallachia and Moldavian populations and building setup have been made
- The new Joint-Stock Companies, Investment Banks, and Corporate Governance techs now progressively reduces the amount of Urbanization needed to spawn a new Urban Center
- Readjusted Secondary Production Methods on Chemical Plants, Furniture Manufactories, Glassworks, and Textile Mills so that they would be more profitable to select
- Split up Shipyards into two separate buildings, that produce either just Civilian or Military ships
- Lowered Farm output of Grain from 30/50/90/140 to 20/40/80/120
- Lowered the amount of Grain lost on Potatoes and Apple Orchards Production Method from 20 to 15
- Strengthened Sardinia-Piedmont's starting economy
- Agitators may now only participate in an election once every six months
- Reduced the Health Insurance mortality reduction
- Gave the technology Military Statistics a new purpose (improves Formation Organization gain rate)
- Changed Mud and Lost Battle Conditions to have modifiers affecting offense, defense and morale loss instead of the overhauled province capture
- Reduced urbanization from heavy industry to cut down on excessive Services production in industrialized states
- Art Academies were changed to have a 5k workforce so as not to differ so much from other urban buildings
- Passenger carriage PMs for trains no longer reduce infrastructure when activated
- Ranching is now a fully separate building group from Agriculture, just like Plantations
- Persia now starts with Traditionalism rather than Interventionism as their economic law
- Increase starting relations between Britain and Lower/Upper Canada to avoid Britain immediately trying to annex them
- Peasant Levies was increased from 2% to 4% conscription rate, but still has a maximum of 25 conscripted Battalions per state, so it is most useful for countries with numerous but relatively sparsely populated states
- Defend order now boosts Defense a lot less, while Advance order also boosts Offense a little
- Added Focused Hardwood Production production method for Logging camps
- Added experimental trains PM to railways
- Balanced Prussia's, France's, Great Britain's and USA's starting buildings, Production Methods and Trade Routes so that they aren't immediately unprofitable after State Market Access Price Impact changes
- Readjusted pop needs so that pops are less likely to buy basic goods when better goods are available
- Livestock Ranches now produce Meat as a base Production Method, Fabric and Fertilizer is now a secondary Production Method
- Public Trams and Public Motor Carriages Production Methods for Urban Centers now produce Transportation
- Increased Arable land in states with high unemployment and low Standard of Living
- Auto Expand Building now requires employment to be above 95% to expand
- All South American countries now start with the Empiricism technology
- Elected Bureaucrats law now makes Bureaucrats more inclined to join the Petit-Bourgeoisie, rather than boosting raw PB political strength
- Removed two Explosives trade routes from History setup that were trading zero goods
- Increased the number of states required to form Germany to 23, which means Prussia needs to either take a state from France or Austria in addition to the various minor countries
- Anchorages now produce only 20 convoys (down from 50)
- Korea now starts with Sulfur deposits in Yangho and Gwanbuk
- Base rate of Conversion and Assimilation is now reduced by 90% in unincorporated states
- Reduced minimum monthly rate of conversion/assimilation from 10 to 1 so smaller pops don't convert at unreasonable rates (they may still end up assimilated through pop consolidation game rule though)
- Mass Conscription conscription rate was reduced from 4% to 3%
- Basic Supplies Mobilization Option now enforces +25% consumption of military goods
- A lower rate of Attrition is now applied when a Formation is in their home HQ
- Attrition is now always applied when Armies are Mobilized or, for Fleets, when countries are at war
- Rebalanced Hardwood Production Method for Logging Camp
- Rebalanced Small Arms Production Methods for Arms Industries
- Steam Engines are now unlocked by the Steel Railway Cars technology and have been renamed to Standardized Trains
- Electric and Diesel Trains now give higher infrastructure, but also have higher input costs
- Lowered input goods of Coal and Engines for Railways
- Lowered the amount of alcohol that subsistence buildings produce
- Increased rubber plantation potentials in South America
- Added Dye potentials to South Carolina, Georgia, and Florida
- Increased Logging potential in Amazons, Congo and Siberia
- Increased the amount of Fabric Livestock Ranches can produce
- Added Recoil Mechanics production method to Artillery Foundry
- Rebalanced Artillery Production Methods for Artillery Foundry
- Gave Greece a starting interest in Italy
- Interest Group Trait modifiers have been lowered so they are no longer as powerful or damaging
- Increased additional aggression against communists from 0.5 to 5
- Switched Two Sicilies from Interventionism to Traditionalism
- Whilst Slavery is still in effect, Dixie leaders will be more inclined to join the American Conservative party, and likewise for Yankees and the Liberal party
- Anarchist flags will now take priority over Council Republic ones
- Poor pops in agricultural buildings can now be attracted to Trade Unions under Commercialised or Collectivised Agriculture
- The Monarchy law now increases the political strength of Aristocrats, rather than providing a flat bonus to Landowners clout
- Hereditary Bureaucrats law now increases Aristocrats political strength rather than raw Landowners political strength
- The historical coal-mining region of Asturias now has coal potential, while Navarra has had its reduced
- Streetlights now produce a small amount of infrastructure when enabled
- Dongola and Blue Nile now have the Nile River state trait
- Puerto Rico now has the 'Natural Harbors' state trait
- Readjusted Brazilian population figures in a couple of states
- Mexico now has a starting claim on Central American Chiapas
- Nursing events will no longer fire in wars with less than 1000 deaths
- Gave Bavaria Intensive Agriculture technology at game start
- Lowered the cost to build Shipyards
- Gave Montenegro and Nejd a Grain Import Trade Route
- American interest groups will be more inclined to form a two-party system, unless they have ideologies outside of the mainstream
- Capitalists, Engineers, and Shopkeepers will be slightly more attracted to Industrialists as their wealth increases
- Limited pops that can join Intelligentsia to Academics, Aristocrats, Bureaucrats, Capitalists, Clergymen, Clerks, and Engineers
- The Homesteading law now increases the political participation of Farmers
- Increased the political participation of pops in trade buildings
- Revisited Chilean arable land and resources
- Reduced Bureaucracy penalty for Greece restoring the Olympics
- Subsistence buildings under Collectivised Agriculture now employ fewer Clergymen
- Appointed Bureaucrats law now increases Bureaucrats political strength rather than raw Intelligentsia political strength
- The Crop Failure event is now better tied to agricultural productivity
- Added silk potential to Moldova
- Removed Sahara desert penalties from Dongola
- Reduced the amount of Infrastructure from Streetlights Production Methods by 50%
- Removed consumption of Small Arms from Irregular Infantry
- Added a Farm to Piratini, Warsangali and Isaaq
- The Homesteading and Commercialized Agriculture laws now permit middle-strata rural pops to become Petty Bourgeoisie
- Increased Farmer wage weight, and granted them Middle-strata status
- The Homesteading law now grants increased political power for Farmers, rather than the Rural Folk Interest Group
- Engineers now have a much higher preference for the Petty Bourgeoisie
- Made Soldiers pops more likely to support the Armed Forces if their wages are high, vice versa if low
- Non-discriminated pops in unincorporated states are more likely to support the Armed Forces
- The Professional Army law now increases Soldiers pop attraction to Armed Forces, and decreases non-military pop attraction
- The Peasant Levies law now increases Aristocrats pop attraction to Armed Forces
- Officers are now slightly more attracted to Armed Forces
- Clergymen are now slightly more attracted to Devout
- State Religion, Religious Schools, and Freedom of Conscience now increase pop attraction to the Devout
- Capitalists are now slightly more attracted to Industrialists
- Academics and Bureaucrats are now slightly more attracted to Intelligentsia
- Clerks are now slightly less attracted to Intelligentsia
- Aristocrats are now slightly less attracted to Intelligentsia by default, with Hereditary Bureaucrats slightly increasing their attraction
- Increased Intelligentsia attraction for Aristocrat/Capitalist/Clergymen pops in urban centers, government administrations, universities, and arts academies
- Farmers will now be more attracted to Landowners as their wealth increases
- Decreased base attraction of non-urban pops to Petty Bourgeoisie
- Shopkeepers are now slightly more attracted to Petty Bourgeoisie
- Clerks are now slightly more attracted to Petty Bourgeoisie
- Decreased middle-strata pops' attraction to Trade Unions
- Papal Landowners and Devout now both support Theocracy
- Columbia District now starts with Frontier Colonisation law
- Bureaucrats, Clerks, and Engineers now have higher base education access
- Reduced throughput modifier for the Hell on Earth event
- Slave States will now increase Farmers attraction to Landowners and decrease attraction to Petty Bourgeoisie

## Art

- Added Low, Mid and High Tier infantry military uniforms for European, Arabic, South East Asian, East Asian, and African units
- Added infantry general uniforms for European, Arabic, South East Asian, East Asian, and African units
- Added icons for historical and non-historical companies
- Added icons for Diplomatic Sways
- Added 7 New Achievement Icons
- A number of historical characters from the Americas now look more like you would expect them to. Thanks to Galactic Cactus, creator of the Americas Character DNA mod for offering up your work!
- Added the heavy tank frontline asset
- Added the base camp frontline asset
- Added planes to the frontline dioramas
- Added companies icon to the sidebar button
- Added South Asian Military Unit Illustrations
- Added building icons for Artillery Foundry building and Explosives Factory building
- Changed the production method colors of Artillery Foundry and Explosives Factory to match the base production methods colors of other buildings
- Added new icon for Conscript Battalions
- Added East Asian military unit illustrations
- Added icons for wargoals 'Increase Autonomy' and 'Reduce Autonomy'
- Added Naval military unit illustrations
- Added a Naval Invasion Map Marker and Icon
- Added production method icons for Sheep Ranching
- Added Arabic military unit illustrations
- Added map visuals for Naval orders on sea nodes
- Updated production method icon colors for Naval bases to red to make it consistent with Barracks production method colors
- Added Leader ideology icon for 'Despotic Utopian Leader'
- Added Leader ideology icon for 'Humanitarian Royalist'
- Added cavalry icons for African military units, hussars, dragoons, cuirassiers and lancers
- Added firing and explosion VFX for the light tank
- Added new ship effects
- Added a uniform for the Native American Low Tier infantry unit
- Added African military infantry unit icons
- Added updated historical character frames to distinguish between characters with and without Info (Wikipedia) links
- Added visuals to city building to represent the Standard of Living in the area
- Arranged position of companies and maplist buttons
- Added sway, trade agreement and custom union icons
- Added new art for state conscription and mobilization
- Added new Alert icons for' Forming a Company' and 'Company Losing Prosperity', as well as a Concept icon for 'Company'
- Added a proposal icon for 'Diplomatic Demand'
- Added special clothing for Brazilian characters and pops
- Mobilization VFX is now present in city hubs where units are mobilizing
- Added Frontline graphics for all types of units and cultures
- Added new conscription and mobilization effects
- Added idle foam VFX for the monitor, frigate and submarine
- Added a new siege firing and explosion effect
- Added idle, firing and temporary moving effects for the military naval ships
- Created a new scaled down version of the battle-end VFX
- Three new Battle Condition icons for Pursuit, Panicked Retreat, and Controlled Retreat
- New icons for company-related technologies: corporate management, joint stock companies, business banks and corporate charters
- Brazilian soldiers now wear mid-century uniforms
- Turkish characters now have a greater variety of appearances
- Added the Infantry Train cart 3D art asset
- Added the Artillery Siege and Field Gun 3D art assets
- Added the Armored Train 3D art asset
- Added the Mechanized Tank Gun 3D art asset
- Added the Submarine 3D art asset
- Added Weapon 3D art assets for Infantry: Blunderbuss, Brown Bess, Dreyse Needle Gun, Mauser 98, Chauchat, Tommy Gun
- Added Weapon 3D art assets for Cavalry: Lance, Saber, Sword
- Added the Carrier 3D art asset
- Added the Destroyer 3D art asset
- Added the Torpedo 3D art asset
- Added new new dreyse needle gun particles and textures
- Added a new mouser 98 weapon particles and textures
- Added a chauchat weapon effect
- Added a Tommygun weapon VFX
- Added new canon artillery VFX
- Added new artillery VFX
- Added a firing and impact VFX for the military shrapnel artillery
- Added new military heavy tank VFX
- Added a torpedo splash and a torpedo trail VFX
- Added artillery cannon 3D art asset for frontlines and battles
- Added artillery mobile cannon 3D art asset for frontlines and battles
- Added R17 (light tank) 3D art asset for frontlines and battles
- Added frigate military ship 3D art asset for fleet operations
- Added monitor military ship 3D art asset for fleet operations
- Added dreadnought military ship 3D art asset for fleet operations
- Added scout cruiser military ship 3D art asset for fleet operations
- Two new building icons, one for the vineyard and and another for the military shipyard
- Added new occupation graphics, countries will now place occupation flags in partially occupied states
- Generals, admirals, and officers of the Ottoman Empire now wear historical uniforms
- Added the Infantry Horse cart 3D art asset
- Updated the artillery effects
- Deploying and stationing armies and fleets now have 3D graphics showing the formation traveling from where they are stationed to their destination
- Military caravans will now travel on roads in countries at war
- Added new alert icon for Standard of Living
- Added simple visualization of frontline units to the flatmap
- Changed the Production Method colors on these icons to refining goods(purple): no_public_transport, public_trams, public_motor_carriages
- Reworked the urban Latin America state-image VFX to fit the new state-picture
- Lowered the frequency of the smoke on the Taino statue
- Added six new battle dioramas
- Added multiple new fleet and naval battle dioramas displaying ships on sea node occupation and in naval battles

## Interface

- Improved flag resolution and scaling for flag icons, preserving more details (configurable in Graphics options)
- Added portrait resolution upscaling setting for sharper portrait details (configurable in Graphics options)
- Implemented Mobilization Option Groups in the Military Formation Panel - Mobilization tab
- Colored the different Military Map Markers based on their allegiance towards you (You / Ally / Enemy / Neutral)
- Added 'zoom to front' button on the front panel
- Improved UX for selected but disabled themes
- Tweaked the layout of the unit numbers around conscription to make more sense
- Added more useful values and columns to the Activate Conscripts map interaction map list
- Exposed Naval Invasion failure conditions to the Naval Invasion map marker tooltip
- Added a Shipping Lane tooltip
- Changed the Available Labour numbers throughout the game into one showing *all* Jobseekers, not just Peasants and Unemployed
- Improved the tooltip for Available Labour from only including Peasants, Unemployed, and Qualifications into one showing all Jobseekers broken down by Pop Types (and with nested tooltips listing all individual Pops), the number of them who are Unemployed, and Qualifications
- Added functionality to be able to expand Buildings and change their Production Methods on the State tab of the Goods panel
- Alerts now have a color (green / yellow / red)
- Grouped Journal Entries into categories (National Agenda, Major Situations, Domestic/Foreign Affairs and Development)
- Improved military formation front interaction panel
- In the Military Formation customization popup you can now change if the units in the formation should base their name on their country culture or origin state name
- Added fIcons for the Formation actions Transfer, Upgrade, Station, Deploy to sea node
- Predictions for which country will lean towards supporting what side in the Diplomatic Play should now always be accurate (instead of intentionally unreliable), and takes the relations impact of the initial wargoal into account, though leaning towards a side is still not a guarantee of actually supporting that side
- Made the Military Formation map markers appear at the top of the stack whenever it is in the same position as any other map marker
- Added Conscript numbers to the Military panel and Formation panel
- Added Occupation breakdown chart to the State Panel
- Added Election information to the Party Fancy tooltip
- Made smaller versions of the different Military Map Markers to be used when zoomed out
- Made Map Markers stay more compact one more zoom step to reduce clutter
- Added buttons to mobilize or demobilize all possible armies with a single click
- Two new Important Action types signal when Organization is impacted somehow
- The defender in a naval invasion is now given an Alert while the invasion is ongoing
- Added 3 x new UI events audio cues
- Improved the Diplomatic Demands liberate country popup
- Added Fleets and player Wars to the Sea Region panel - Navy tab
- Made the activated/deactivated state clearer for the Mobilization options in the Mobilization tab for Formations
- Added hints of where to change orders to relevant tooltips
- Added the mobilization status of individual combat units in their tooltip and as a background progressbar to the list items on the Formation panel
- Added job satisfaction to the pop tooltip and the pop details panel
- Mirrored and rotated all pie charts to start from the top, being filled clockwise with the largest piece first
- Made multiple minor changes to the End of Battle Panel that should make the numbers add up more clearly
- Tweaked the "Ended Battles" item to more clearly signal the outcome of the Battle
- Now showing Goods Shortage information in more places for State Shortages
- Added a text notifying the player if they have available actions in a pinned Journal Entry in the Outliner
- Now showcasing the current Distribution of Power Law in the Election panel
- Reworded several tooltips related to Votes and Political Strength to more clearly communicate how the two of them interact
- Re-added Production Information to the Expand Building tooltip to expose Local Prices more in this context
- Now showing Goods icons on Alerts related to Goods
- Added Fancy Tooltip for Journal Entries
- Reworked the way the sidebar in the Main HUD is structured
- Added Experience Rank Icons
- Fixed overlapping text in German for Interest Group panel
- The tooltip and confirmation box for making a Diplomatic Demand/starting a Diplomatic Play now shows more consolidated and useful information for the potential sides and supporters in the Play
- Mobilization and Conscription notifications are now only sent to countries that are committed participants in a play
- Generals on a Front now show which state they're targeting in their tooltip
- Combat Unit Types are now tooltippable so you can find out what their attributes, upkeep, and unlock conditions are
- It is now possible to see a list of Unavailable Orders and the reasons for them being Unavailable for any particular Commander
- Made the recruit plus-button on Unit Groups always visible so that you may check the map interaction at any time even if there are no options, but you can then see why
- Made the Attrition tooltip on Military Formations more readable
- Added player names to the state and country Attitude and Relations on-map tooltips in multiplayer games
- Removed the incorrect unit lists from the battle panel to set it up for future improvements with the new Military system
- Improved the Occupation Won tooltip to give clearer information
- Exposed which HQ a Military Building belongs to in the Building details panel, the Expand Building tooltip and the Map Interaction list
- Added Map Markers to Goods Production / Consumption and Potential Map Modes
- Now only showing Past Battle Map Marker if that Battle is being highlighted to reduce map clutter
- Added icons to the Current Situation list items
- Tooltip for participants in diplomatic plays now shows which countries are blocked from joining one side or another due to truces, alliances, obligations and so on
- Journal Entry buttons that can be pressed and remain "selected" now appear as such, to distinguish them from buttons you don't qualify to press
- The Hegemon final objective now displays how much of a share of the global population you currently control
- Units and Mobilization Options that are unlocked by tech now appear in the tech tree
- Confirmation popup dialogue if toggling a Mobilization Option would result in a penalty has been added
- Political movements has tooltip breakdown for population support
- Added several audio events in the military formation panel
- Improved the tooltips when swaying countries or offering support to countries
- Added what stance a country has in a Diplomatic Play to their respective tooltips in the Sway Countries tab
- Added a go-to-details button at the top right corner of more tooltips
- Added a Fancy tooltip for Military Formations
- Made the demobilization button less pronounced, but more convenient to use
- Made the transfer units popup handle transfers both ways
- Added sliders and textboxes for selecting number of units to transfer in the transfer popup
- Added a more permanent Discord button in the main menu
- Make it clearer why you cannot impose a Law on a Country in the Country panel - Domestic tab
- Added collapsible sections for Active Fronts and Ended Battles on the War Panel
- Added sorting to the the Active Fronts list on the War Panel
- Improved layout of the Goods panel header
- Added money symbol on the axis of Price charts
- Tweaked the layout of Formation, Battle, Front, and War Map Markers to be clearer and more compact
- Added Manpower bar to zoomed in Battle Map Markers
- Added Manpower bar to Battle list items
- Added "Zoom to Battle" button on the Battle details panel
- Added Organization And Morale icons + text icon
- Removed state details in market panel if accessed through state
- Added new breakdown tooltips for Military Units on all military related panels
- Made the Journal Entries a bit smaller in height in the outliner
- Updated the tooltips and buttons around orders to accommodate for "next order"
- Added ongoing Battles to the Military Formation panel and Commander panel
- The capitulation desire tooltip no longer displays an unnecessary line about annexation
- Improved the tooltips for assimilation and conversion to show more consistent numbers
- Added a new Naval Invasion panel
- Added a new Naval Invasion map marker
- Added a warning and tooltip telling you when a Formation has too many special units (cavalry, artillery, or capital ships)
- Properly center aligned the buttons in the Lenses
- Military UI panel audio files added to script
- Updated audio mix and sounds for military units and UI
- Updated night ambience sounds

## Narrative content

- Added the Establish Colonial Administration Journal Entry, which allows you to set up and expand custom colonial nations in Africa
- Reworked the 'Exploiting the Amazon' Journal Entry and added 8 new events associated with it
- Swapped in unique approval-activated traits for Interest Groups in several countries
- Created outfits for Russian military leaders
- Added a decision to Korea to declare the Korean Empire
- Added events, Journal Entries, and decisions centered around Romanian unification
- Added country formation events that trigger upon forming a country. Typically they add claims on unowned/unclaimed homeland states.
- Added Journal Entry for Poland-Lithuania to expand into Ruthenia
- Added several new state traits to Brazil and the rest of South America
- More historical characters have been added to all South American nations
- Added a colony exchange button to the Scramble for Africa Journal Entry, to exchange colonies with another country
- Added a "The Nations of Turtle Island" Journal Entry for indigenous countries in North America
- Reworked the Peru-Bolivian Confederation content, and added content for Argentina and Chile reacting to it
- Reworked and reframed the "Path to Socialism" journal entry into "The Spectre Haunting the World"
- Added several American interest group leaders tied to the new Companies mechanic
- [Voice of the People] A new Journal Entry for France to establish and expand the Confederation of the Rhine as a puppet state
- Added a Journal Entry and associated events dealing with Polish unification. Playing as Krakow should now be more viable!
- Added Bahia as a releasable nation
- Added a new flag for the Joseon Dynasty
- Added a small Journal Entry for Central American Reunification. Completion allows a less awkward restoration of the UCA tag.
- Added Journal Entry for Brazilian minors to win their independence wars
- Added a victory event for the CSA/Slaver USA that lets you reintroduce the slave trade following the American Civil War
- Japanese characters and pops will now transition to more European fashions after the Meiji Restoration is completed
- Added numerous historical monarchs for Russia, with events for their accession to the throne, and deaths of heirs
- Reworked Italian unification
- Added a journal entry to Japan to represent the nation's historically high literacy rate
- Added the Enlightened Royalist ideology, which is a fusion between Royalist and Humanitarian
- Indonesia and Turkestan now require fewer states to form
- Los Altos now also gains independence if and when Central America dissolves
- Added new Corporatism technology and ideology, which serve to strengthen and modify the Devout in the mid-game
- Added a button to the Conquest of the Desert journal entry, to enable faster colonization
- Renamed Egypt's Rural Folk Interest Group to "Fellahin"

## Performance

- Building meshes in the city will now add as a square root of the previous mesh per level linear progression to improve late-game performance and looks of the cities (to make them more distinct on the map)
- Improved performance of building earnings/employment caches by filtering out government/subsidized buildings that always want to hire and removing unnecessary goods substitution impact predictions
- Improved the performance when running the game with the Sea Region panel open
- Optimized the list of Trade Routes in the Market panel Trade Route tab
- Buildings that want to hire more employees but do not succeed will now wait 4 weeks before trying again. If a building in hiring cooldown raises its wages, it will reset the cooldown.
- Improved performance of updates to Input Goods Shortages by excluding states that have no shortages from running the full update logic
- Fixed a bug when conscription VFX over cities could spawn indefinitely

## Modding

- Added an in-game script profiler for modders, to allow measuring script performance and find bottlenecks
- Implemented create_dynamic_country effect which allows the creation of brand new countries with custom-defined country type, culture, religion, tier, colors and states
- Added a generic type for highlighting text on hover in the UI
- Added add_state_trait effect that adds a state trait to a state region
- Added support for diplomatic actions to target and select states. Selected states are persisted in any pact created from the action. Diplomatic actions that are used in sways or function as subject-type pacts cannot include state selection.
- War Exhaustion is now a script value that can be scripted with any factors and conditions
- Pop growth defines are now more flexible allowing for more kinds of curves
- Added an effect to create military formations
- Added remove_state_trait effect that removes a state trait from a state region
- Removed `allows_advance` property from commander order types, and `protects_convoys_from_damage` property from commander order types
- The AI now uses explicit script values for state and subject value in their strategies that they always consider when deciding whether and how much they want to gain or hold on to a state
- All modifier types "building_input_" and "building_output_" are now renamed to "goods_input_" and "goods_output_"
- Added compare triggers country_turmoil, enemy_occupation, enemy_contested_wargoals, size_weighted_lost_battles_fraction, additional_war_exhaustion
- Added modifiers state_urbanization_per_level_add and state_urbanization_per_level_mult to affect the amount of Urbanization needed for a new Urban Center
- add_morale effect for combat units has been added
- Several pop growth defines have been renamed or replaced with new clearer ones
- Added a new effect to copy all the laws of a country (copy_laws)
- Added a pair of new effects to deploy or teleport formations to fronts
- Added new effects mobilize_army and fully_mobilize_army
- Added a new history step to deploy military formations
- Added a mass_migration_culture link that scopes to a mass migration target culture of a state
- Added a trigger to compare a country's naval_power_projection
- Added a law type on_impose effect for laws that are imposed on a subject by an overlord
- Added a law type can_impose trigger for laws that are imposed on a subject by an overlord
- Now temporary global variables will be updated and expire as all other saved variables
- Enabled bookmark generation for map editor since map graphics now require gamestate data to function
- Replaced `[CommanderOrderType.GetNameGerund]` with `[CommanderOrderType.GetName( 'gerund' )]` to allow for moddable suffixes that make more sense for different languages or mods
- Added AI strategy weights for how much the AI desires to have a country as a subject or become a country's subject
- New compare triggers global_population, total_population_share, total_population_including_subjects, and total_population_including_subjects_share have been added
- Added organization and max_organization compare triggers on Military Formation scopes
- add_organization effect can now be run in Military Formation scope
- Added Formation modifier support for units
- Added battle side unit modifier support for units
- Profession-specific modifiers for Education Access can now be granted
- New instant_switch trigger added to battle conditions that determine whether a battle condition should be switched to at the first possible opportunity
- There are now on-actions for on_company_created and on_company_disbanded
- Debug command Logging.PopWealth is now called Logging.PopStats and tracks a lot more data
- Added an on-action for country formation
- Added an effect to mark a country as immune to revolutions (set_immune_to_revolutions) along with a matching trigger to check this mark (is_immune_to_revolutions)
- Added a new trigger called 'attainable' to the company types database to better control which companies appear in which category in the interface
- Added is_mass_migration_origin_of_culture that checks if a country is the origin of a certain culture
- Added is_mass_migration_origin that checks if a country is the origin of any mass migration
- Added country_army_unit_type_fraction to check the fraction of a specific unit type in a country's army
- Added formation_army_unit_type_fraction to check the fraction of a specific unit type in army formation
- Added country_navy_unit_type_fraction to check the fraction of a specific unit type in a country's navy
- Added formation_navy_unit_type_fraction to check the fraction of a specific unit type in a country's navy formation
- Added army_mobilization_option_fraction to check the fraction of units having a specific mobilization option in a country's army
- Added an change_character_culture effect that changes the culture of a character
- Implemented scriptlist any_sea_node_adjacent_state/every_sea_node_adjacent_state/random_sea_node_adjacent_state which fetches all states that share a sea node with the scoped state
- Added new rules modifiers country_government_buildings_protected and country_all_buildings_protected to compliment country_private_buildings_protected, all three protect certain buildings from being downsized
- Added War-Diplomatic Play link
- scope_general and scope_admiral scriptlists can now be used in Military Formation scope
- Added military_formation scriptlist
- Added an opposite_battle_side link for battle side scopes
- Added current_manpower and starting_manpower compare triggers for battle side scopes
- Added new modifier type battle_combat_width_mult
- has_unit_type trigger was added for combat unit scopes
- combat_units scriptlist (e.g. any_combat_units) is now called combat_unit, to prevent headaches from poor script grammar
- The `front` link can now also be used in province scope
- Added state_has_building_levels trigger that checks the sum of building levels in a state
- Added state_has_building_type_levels trigger that checks the sum of building levels of a certain type in a state
- Added state_has_building_group_levels trigger that checks the sum of building levels in a certain group in a state
- Added country_has_building_levels trigger that checks the sum of building levels in a country
- Added country_has_building_type_levels trigger that checks the sum of building levels of a certain type in a country
- Added country_has_building_group_levels trigger that checks the sum of building levels in a certain group in a country
- Added country_can_have_mass_migration_to trigger that checks if the country can have mass migration to a specific country
- Added culture_can_have_mass_migration_to trigger that checks if a culture mass migrate to a specific country
- Added a valid_mass_migration_culture lists for cultures valid for mass migration in a country
- Added a has_mobilization_option trigger that checks if a formation has a mobilization option
- Made the error log provide more information when event options are incorrectly scripted
- Added new triggers has_political_movement = <law type> and can_potentially_get_political_movement = <law type>
- Added modifier state_slave_import_mult that increases the number of slaves a state can import each week under Slave Trade
- Implemented new value links ai_state_value and ai_subject_value that returns how much the AI desires a state/subject
- Added new triggers state_goods_production, state_goods_consumption, state_goods_delta, state_goods_pricier, state_goods_cheaper
- Added scope switch sg:goods to state goods from state (for example sg:coal)
- Added scope switch to highest_ranked_commander from Military Formation
- URBANIZATION_PER_BUILDING define has been removed in favor of the new modifier-driven values
- Added character_is_discriminated = yes/no trigger
- Added a console command Logging.MarketGoodsShortages for logging Market Goods Shortages
- Replaced deprecated "country_trade_route_exports_add" and "country_trade_route_imports_add" modifiers

## Bugfixes

- Fixed mesh-on-mesh shadows appearing darker than intended
- Fixed a bug where buildings that were doing poorly could get stuck in a loop of firing employees, only to then raise wages to attract more employees which they then would fire again, leading to absurdly high wages and an unviable building
- Fixed a bug where AI (and autonomous investment) would expand buildings that were not fully employed even though those buildings were unable to hire any more employees due to lack of workforce/qualifications, low productivity, or similar reasons
- Buildings can no longer be queued past the level limit (third time's the charm)
- Fixed crash in CConstructionQueue caused by a race condition
- Moved the tooltip for building details to only appear on icon instead of the entire area where the icon and the building levels are at
- Fixed a typo that caused soldiers to be 100x more likely to be loyal to armed forces if they were paid low wages
- Fixed an issue where trade route competitiveness share was not correctly calculated for trade routes that had been around for a while, leading to trade routes shrinking for no sensible reason
- Fixed a bug where capitulation and peace agreement notifications would sometimes be blank instead of showing which wargoals were enforced
- Player controlling a junior country in a market can now import and export correctly again
- [Voice of the People] The Paris Commune now inherits the Journal Entries and variables of France if it ends up winning
- Fixed that the flags in the save game menu would be scrambled when there are too many flags
- Fixed an issue where revolutionary progress could exceed the radicalism of the movement and cause unexpected revolutions
- Notifications for broken diplomatic pacts should now be more informative
- Fixed a crash where an invalid country would be added to the Diplomatic Relations and, as a side effect, could block players from loading save files which had such issues
- Map markers will no longer be flickering when hovering over them
- Literacy concept now correctly refers to Pops in incorporated states, rather than unincorporated ones
- Agitators that are culturally or religiously discriminated against can no longer be promoted to become Interest Group leaders
- Female agitators can no longer be promoted to Interest Group leaders unless you have Women's Suffrage
- Modifiers on Journal Entries now propagate properly to countries regardless of modifier type
- Fixed instance to avoid multiple mass migrations to one state
- Confederating Canada now incorporates states properly
- Fixed the name of an event name file, re-enabling the song England 1850 to play in the Music Player
- Updated the concepts for Mobilization and Generals to not reference the old military system anymore
- Fixed an issue where interest group modifiers would not affect some legitimacy calculations
- Fixed an issue where some effects of character traits would not be applied immediately
- Fixed several clipping issues on base game character outfits
- Updated the crash reporter to address report sending failures on Mac and Linux
- Implemented support for moving the naval invading army to the newly created front on a successful naval invasion
- Prevented multiple naval invasions from targeting the same state
- Fixed a crash which was caused by calling events for recreated countries
- Fix a crash in the creation of diplomatic relations
- Fixed a crash caused by construction elements pointing to a state that was merged into another
- Wars concluding in peace will no longer end twice
- Battle modifiers now immediately update when battle conditions change
- Fixed long usernames displacing the UI when signing in to the Paradox account
- Changed the Unit Recruitment text to Unit Details in the Sub header
- Adjusted the Land Tax progression so that it is consistent
- Fixed "Breaking the strike" event option b applying its modifier to the wrong Interest Group
- Expiring Obligations will now show the number of days until it expires in Brazilian Portuguese
- Fixed some event localization where the supporting and opposing agitators got mixed up
- Recontextualized several agitator law events to fit better with their position as populist figures
- Improvements to various expedition flavor texts
- Fixed a number of typos in Concepts, Events and Technologies
- Fixed multiple typos in different languages
- Replaced placeholder loc string in Philosophy events
- [Voice of the People] Fixed Paris Commune subjects' flags not showing the Paris Commune overlord canton
- Fixed an issue where trade routes would sometimes set their level targets incorrectly when you had multiple trade routes for the same good
- The maximum potential imports & exports of trade routes in a market is now multiplied by the BUY_SELL_DIFF_AT_MAX_FACTOR define, so that exported/imported goods with no local consumption/production aren't always stuck around base price
- Fixed a bug where randomization functions in the history database were not working correctly, primarily impacting starting AI strategies
- Fixed an issue that made it so AI starting strategic desires from history DB were sometimes not correctly set
- Fixed an issue where Productivity was sometimes being calculated based on max employee count instead of current employee count, resulting in misleading information being displayed in the interface
- Fixed an issue where earnings prediction tooltips were not taking all produced/consumed goods into account, resulting in incorrect earnings estimates
- Fixed an issue where caches not being updated resulted in earnings prediction breakdown for expanding buildings being inaccurate
- Fixed an issue where unification wars were unable to end due to secondary participants not being able to capitulate
- Made Turkey only grant independence to subjects of it directly, not independent subjects
- You can no longer move Fleets without Admirals, nor can you transfer all Admirals out of a Fleet without also transfering all of its Flotillas
- Fixed instance where events dependent on election were ending prematurely
- German National Identity Journal Entry will now be unlocked at start to prevent it from being completed before The Schleswig-Holstein Question Journal Entry, and blocking further progression of German Unification content
- Nations can no longer build statues of child monarchs
- The Opium Wars Journal Entry now requires that the target country have ports
- Completing the Great Famine journal entry now clears modifiers as intended
- Event expedition_events.120 is no longer orphaned
- Revolutionary countries now inherit the Socialist ideology for Trade Unions
- Italian unification no longer requires Papal States to exist
- Fixed several errors that may arise as a result of Discrimination events
- Fixed overlapping text for several languages in the Population panel and the Message Settings window
- Fixed the tooltip for scripted buttons to show the effects at the bottom
- Made the enactment chances (Success, Advance, Debate, Stall) breakdown tooltips better structured
- Fixed an issue where the lobby would always appear to be public for clients
- Fixed a bug where agitators got lost in the void
- Bougie, Algeria now starts under French control
- Fixed a crash in CCityGraphics::CreateNewBuilding caused by incorrectly modded buildings
- Fixed a crash that occurred when mods had invalid cultures
- Fixed a crash that occurred when mods had no building models assigned to a building type
- Fixed a crash that occurred when mods attempted to use concepts in the loading screen
- Fixed a crash when transferring revolutionary characters
- Fixed an out-of-sync caused by updating gamestate data at an inopportune time
- When a state is annexed, building levels under construction are now only transferred to the new owner if those levels have made some progress
- When a revolution is defeated, the original country no longer inherits Journal Entries and variables from them, as this could cause some Journal Entries to break. Victorious revolutions still inherit from the original country.
- Demobilizing Armies early (while still at war) now always enforces the penalty, and automatically returns them to their home HQ
- Fixed interest group tooltips to show the correct political strength value
- Agitator Legal Events 3 no long scopes to the wrong target
- Changed French Republic head of state to President rather than Chancellor
- Removed several placeholder Interest Group descriptions
- Labour Negotiations event can no longer fire without options
- Resolved errors in the German Confederation event
- The Sepoy Mutiny can no longer attempt to take a nonexistent state
- Historical interest group leaders should not spawn for interest groups that have chosen different ideologies
- The Metropolitan Railway now selects the correct state
- The Junta government type now requires the Armed Forces in government
- [Voice of the People] French Orleanist/Bonapartist/Legitimist revolutions will no longer generate incorrect dynastic rulers
- Fixed state_has_goods_shortage trigger not working properly
- Fixed an issue that caused the player to receive fleet notifications from other countries
- Frederick Douglass can no longer spawn as a Rural Folk Interest Group leader
- Royal heirs that belong to the devout Interest Group can no longer wear priest garbs
- Now showing the Military graphics around the Lens toolbar if you are at War or involved in a Diplomatic Play
- Restored "Keypad +" as the secondary default keybind for "increase speed"
- Fixed an instance where player controlling a junior country in market can now import and export
- Fixed a bug where Conscripts added after Raising Conscripts did not get recruited
- Fixed various small issues like missing highlights in tutorial, wrong tooltips etc.
- Fixed a bug where the Trade Route Competitiveness bonus from excessive convoys was not being correctly applied
- Fixed a bug where players would sometimes get notified about trade routes they themselves created
- Wargoals to turn a country into a subject are now converted into Transfer Subject wargoal if the target becomes the subject of another country (for instance by offering it as a sway) instead of being invalidated
- Fixed an issue where starting Diplomatic Plays targeting a whole country through the right-click menu sometimes would be incorrectly blocked by not having an Interest in a non-capital region of the target country
- You can no longer restation, deploy, or mobilize formations with no units
- It is now possible to start a naval invasion even when the fleet is already in the appropriate sea node
- Fixed localization for light and heavy industries throughput modifiers
- Obligation Alert will now display the correct country in all situations
- Fixed loc issues for building throughput modifiers
- Fixed issue with Unrecognized Countries not getting the final Hegemony Journal Entry
- Allowed for Tributaries and Vassals to be counted in the Maintain Subjects Hegemony Journal Entry
- Fixed error spam related to Communism events
- Added cooldowns for all Reconstruction events for the USA
- Gave Pedro II a proper age
- Switched the event options in the Hippopotamus event
- William Shubrick is now an admiral
- Leader ideologies may now trigger Path to Liberalism properly
- Foreign Emulation will no longer spawn as a Stall event
- [Voice of the People] paris_commune.2 event can now fire properly again
- [Voice of the People] Resolved issue where French Algerian states would be raided by null countries
- Fixed an issue with dynamic country names that would crash the game in non-graphics mode
- Fixed an issue where a battle would be displayed as if it had happened on a nameless front
- Added a check to Expand Building Tutorial to check that the the building can be expanded by 1 level
- Belle Époque achievement description now matches the unlocking triggers
- Fixed localization issue with Coup Journal Entry
- Theocratic coups no longer display loc for Council Republics, and vice versa
- character_events.100 will no longer spawn NULL_OBJ notifications
- revolution_pulse1_events.18 can no longer add permanent interest group approval maluses
- Government petitions no longer fire for countries that cannot enact laws
- "The Party Favourites" will now correctly choose interest groups
- Adjusted impact of pop loyalists/radicals on interest groups to ensure they don't spawn support from nowhere
- Devout interest group leaders will no longer be Atheist if spawned in a State Atheist country
- Atheist pops can no longer join the Devout
- Isolationist countries will no longer get Steel and Paper import events
- "Lugwig" is no longer a German regal name
- The Social Democratic party in Germany is now properly called SPD
- Resolved issue of missing loc for the North and South Philippines Sea

## References

1. ↑ Forum: [Update 1.5 and Colossus of the South Region Pack, now available!](https://forum.paradoxplaza.com/forum/index.php?threads/1609767), 2023-11-14.
2. ↑ Forum: [Dev Diary #95 - Open Beta 1.5.0 changelog](https://forum.paradoxplaza.com/forum/index.php?threads/1597818), 2023-08-31.
