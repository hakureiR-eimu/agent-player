---
title: Patch 1.9.X
source: https://vic3.paradoxwikis.com/Patch_1.9.X
pageid: 7517
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
**Patch 1.9.X** are all patches beginning with 1.9.

## 1.9

Main article:
Patch 1.9

## 1.9.1

Patch 1.9.1 was released on 2025-06-18[1] with checksum *317f*.

### Improvements

- The "Company Monopoly" article now correctly checks whether you have the prerequisite Foreign Investment Rights from the other country

### Balance

- Slashed Maneuvers base cost for enforced articles across the board
- Removed the bi-directional trade advantage penalty
- Applied a reduction of trade desire based on amount of trade in the other direction
- Applied a reduction of trade desire based on opposite direction subventions
- Limited imports/exports by available volume (based on amount of opposite trade in world market not coming from the same market)

### Interface

- Changed display of Authority, Influence and Bureaucracy gains to display one decimal to account for certain use-cases like Power Bloc Principles

### Bugfixes

- Fixed a bug where naval invasions could get stuck when invading small split states
- Fixed an issue where formations could be deployed to the naval invasion front before a successful landing
- Fixed an issue where Trade Advantage from Treaty Ports was being multiplied by the wrong value, causing it to potentially go into the thousands
- Fixed a bug when a chartered company wouldn't remove company ties when reducing/increasing autonomy
- Fixed a bug where reducing charted company autonomy would put the company CEO as a leader of the overlord country
- Fixed an issue where it was possible for a dominant market to use subventions to create an infinite spiral of circular trade far exceeding production volumes
- Fixed an incorrect AI trigger for the investment charter
- Fixed an issue that resulted in the "The Schleswig-Holstein Question" Journal Entry not being resolved properly by the AI
- Fixed an instance of errors printing in the "German National Identity" Journal Entry
- Fixed unlocalized string WARGOAL_CONTESTED_OR_NOT_DESC in war support tooltip

## 1.9.2

Patch 1.9.2 was released on 2025-06-19[2] with checksum *4d33*.

### Improvements

- Improved the force-refresh logic for stuck investment pools, which should ensure the investment pool can never get permanently stuck again but will always unstuck itself after a while if there are valid investments to do
- Withdrawing from a treaty with Guarantee Independence or Support Independence will now create a truce

### Balance

- The United Fruit Company now has a more sensible preferred HQ and formation trigger
- The levels_owned_by_country and fraction_of_levels_owned_by_country triggers now look at all ownerships originating from entities in the country instead of just direct national ownership

### Bugfixes

- Fixed an issue where war goals wouldn't be executed properly after a war goal that removed a participant from the war (by making them your subject or annexing or something) ended up removing other war goals and disabling the rest of the peace deal
- Fixed a bug where some wargoals (most notable Revoke Claim) would incorrectly not be considered controlled, resulting in stalemated wars
- Fixed a bug that caused the population of some countries to be incorrectly lower than it was on the 1.8 version
- The game will now correctly fallback to valid renderer settings if it is somehow given incorrect settings e.g. DX11 on Mac/Linux
- Fixed a bug where the tariffs value in the market screen would not be cleared before being added to each week, resulting in an endlessly growing number
- Fixed a bug where companies with a preferred HQ would sometimes be unable to be formed if it wasn't possible to get their building types in the preferred HQ state
- The levels_owned_by_country and fraction_of_levels_owned_by_country triggers now look at all ownerships originating from entities in the country instead of just direct national ownership
- Fixed an Out of Sync issue in multiplayer related to "PoliticalMovement CivilWars"
- Fixed an issue where religious minority movements failed to correctly trigger secession
- Fixed a bug that would cause the average_sol_for_religion trigger to always return the wrong value, causing activism of religious traditionalists movements to be wildly inflated
- Receiving Foreign Investment Rights now properly generates Leverage
- Its now possible to properly add a Company Monopoly in the same treaty that also requests the prerequisite Foreign Investment Rights
- Fixed a bug where the effect of military prestige goods was being scaled by all input goods instead of just input of military goods
- Fixed an issue where landlocked states would keep their world market access even after cancelling the transit rights treaty that gave it to them.

## 1.9.3

Patch 1.9.3 was released on 2025-06-25[3] with checksum *87ce*.

### Improvements

- Changed assimilation for slaves so that they can assimilate to cultures of the same heritage
- Its now possible to properly add a Company Monopoly in the same treaty that also requests the prerequisite Foreign Investment Rights
- Expanded the Goods Transfer treaty article non-fulfillment conditions to include checks on supply network strength and good price on source market
- Expanded the Goods Transfer treaty article validation conditions to include checks on supply network strength on and good price on source market
- Reworked the max script value on the quantity input for the Goods Transfer treaty article to take the source market into consideration and generally be more sensible
- Changed it so that when the game checks for a highly specific law (such as Slave Trade) it usually also checks for a variant law, meaning that for instance Slave Trade variants will now automatically enable slave import in the same way the parent does
- Deployment of additional invading armies is now disallowed for invader allies
- It is no longer possible to accidentally begin the Panama or Suez Canal surveys if they would instantly invalidate

### AI

- The AI is now more active in proposing and creating treaties and will propose new treaties when low on influence if there are less valued existing treaties it would be OK with replacing
- Fixed a bug where when the British AI would try to construct a port in a state which lacked one, instead of actually constructing the port in that state, they would instead construct it in Tasmania (actually a more general issue making the AI misconstruct ports in general, but most visible in Tasmania)
- Fixed a bug where the AI would sometimes to fail to subsidize Ports and other critical buildings, resulting in their Supply Network Strength/Infrastructure collapsing
- Fixed an issue where AI generals would not advance on invasion fronts
- Fixed an exploit where you could renegotiate a State Transfer to get additional states in exchange for the same articles all over again
- Made the AI and autonomous investment more likely to build Trade Centers in Treaty Ports, and less likely to construct other types of economic buildings there
- The AI now factors how fair they consider existing treaties to be to them when deciding whether to accept a new treaty
- Fixed an issue where AI was sometimes calculating Foreign Investment Rights acceptance wrong
- Fixed an exploit where it was possible to block the AI from withdrawing from a treaty if you revoked your interest in their country and they didn't have one in yours

### Balance

- Countries will now be far less willing to cede incorporated states and homelands in particular
- Diplomatic demands for ban slavery, investment rights, and take treaty port now generate infamy even when the diplomatic demand is rejected
- Tweaked the influence cost of a number of articles, lowering the cost of less significant articles and increasing the cost of Treaty Ports
- Technologies that increase Influence now increase it significantly more, particularly in Era V
- The AI is generally more stingy now when it comes to parting with its money
- Recognized Nations are now significantly less likely to agree to an Alliance or Defensive Pact with an Unrecognized Nation
- Trade Centers will now auto-downsize privately owned levels if they have at least 20 or 10% unused Trade Capacity, whichever is higher
- Isolationist Countries are now far less willing to agree to certain trade related articles
- Nerfed AI acceptance gain from Lobby Opportunity bonuses
- Nerfed AI acceptance gain from Mutual Trade Value
- There can now only ever be one Law Commitment active per treaty
- Reduced the Law Enactment Chance gain from Law Commitment from 25% to 15%
- Political parties will now almost never have more than 3 members, and never have more than 4
- Changed the East India Company's randomly generated company executive rulers to have the industrialists interest group when possible
- Great Powers are now more reluctant to grant the Offer Embassy article
- Becoming Unification Candidate for Italy/Scandinavia now only requires Minor Power rank rather than Major Power
- Offer Embassy no longer grants an instant 20 points to the Journal Entry, instead each instance of Offer Embassy that the country has signed will grant a ticking +1 score
- Reduced the legitimacy incoherence penalty for secondary members of political parties
- Trade Centers are no longer subsidized by default
- Made it easier to make Atheist minority characters into IG leaders under State Atheism

### Content

- Added a couple more Executive modifiers to character traits that were missing them and updated some to include missing industries
- Added Thomas Edison DNA
- Added Samuel Colt DNA & character template (Charters of Commerce)
- Added Charles Frederick Worth DNA & character template (Charters of Commerce)
- Added Robert E. Lee Wilson DNA & character template (Charters of Commerce)
- Added Michael Thonet DNA & character template (Charters of Commerce)
- Added John Maple DNA & character template (Charters of Commerce)
- Added Cecil Rhodes DNA & character template (Charters of Commerce)
- Added Sam Eyde DNA & character template (Charters of Commerce)
- Added John Holt DNA & character template (Charters of Commerce)
- The "Königliche Porzellan-Manufaktur Meissen" Company is now correctly located in Saxony, not Brandenburg
- Japan now starts with two new treaties with China and the Netherlands respectively

### Interface

- Added potential buildings to the company type tooltip
- Added info about the free number of Company Charters the player can grant to more relevant places
- Added a compact version of the remaining binding period number on the Treaties pinned in the outliner
- The treaty proposal tooltip now lists mutual effects of the treaty
- Added an explanation to the tooltip of the company construction bonus for non-company-specific building types
- Added the owing/using obligation icon to active treaties if one is owed/used
- Added an acceptance label to all the Treaty Draft Acceptance values in all Article Draft tooltips
- Added Free charters information into Charter tooltips
- When the checkbox to owe an obligation as part of a treaty is disabled, the tooltip now tells you why that is
- When the button to remove an article from a renegotiation is disabled, the tooltip now tells you why that is
- Productivity of subsidized buildings is now always clearly visible in the state panel
- Increased the speed of the outliner show and hide animations.
- Changed the acceptance breakdown in Treaty Drafts to be written in a more consistent format in English (will be localized for other languages in Hotfix 1.9.5)
- Added a tooltip explaining why the Article quantity slider and editbox is disabled when the min and max amount is the same
- Fixed a bug where opening a window for the first time wouldn't show the company icon
- Country Leaders on the right side of the Treaty UI now face the correct direction
- Fixed breakdowns for goods exports and imports showing outdated values in the world market panel
- Fixed a trigger in the Prestige Goods journal entries that displayed an incorrect definition of "prosperous"
- The "Privatize | None | Monopolize" right-click menu now will close automagically when you click any option eliminating that unnecessary extra click to close the menu
- Fixed null object localization for goods being present in a market in the mobilization panel
- Updated the lens tutorial text to say four lenses instead of five

### Modding

- Implemented savegames.delete_all and savegames.delete_cloud console command
- Added requirement_to_maintain support for articles, in the same way that already exists for diplomatic actions. Individual articles can now be invalidated if they fail their requirement_to_maintain check, this will post a notification and also destroy the treaty if the treaty is left without articles. Just like with pacts, you can script conditions under which to warn the player that the article is about to break.
- Added new trigger has_law_or_variant, which works like has_law but also evaluates true if the country has a variant of the specified law
- Replaced the recipient_pays_maintenance property on diplomatic action types with a maintenance_paid_by = first_country | second_country property
- Replaced the recipient_pays_maintenance flag on treaty article types with a maintenance_paid_by = source_country | target_country property
- It is now possible to specify in a trigger which exact conditions (such as rank) is required to become a unification candidate for a specific tag
- Journal entry timeout is now a script value, and will dynamically recalculate if changed after the JE activates
- Law icon parts are separated out into different image files so modders can more easily use them to create new Law icons
- Added new country value link principal, which returns the current debt principal
- Added new treaty trigger is_equal_exchange, it checks if a treaty has the same types of articles on both sides

### Bugfixes

- Fixed an issue where backing down would execute the wargoals of your backers, rather than the other side's backers
- Fixed a bug where a company monopoly treaty could block the construction of the building type by the target country
- Fixed a bug where the total state-to-state export volumes could greatly exceed the actual volume exported from the state, potentially resulting in massively inflated Trade Advantage values
- Fixed crash in building privatization from the building having an invalid country as an owner
- Fixed some issues where Risorgimento events could result in stagnant split countries
- Fixed an issue where a Pops support for Interest Groups could never drop
- Fixed an issue where accepting a diplomatic demand that should result in a treaty (i.e. through ban slavery, take treaty port or investment rights) wouldn't do anything.
- Fixed a bug when reducing charted company autonomy would put company CEO as a leader of overlord country
- Fixed a bug when chartered company wouldn't remove company ties when reducing/increasing autonomy
- Articles that are straight up invalid (for instance support independence against a non subject) will now be removed with a notification instead of eternally non-fulfilled
- Fixed cases where company executives would randomize interest groups as if they were monarchs and monarchs would randomize interest groups as if they were executives
- Fixed a bug where other companies already owning building levels in a state were prioritized over monopoly companies for privatization
- Fixed a bug where no migration took place between a treaty port state and its owning country
- Fixed a bug when after disbanding a HQ null object HQ could start buying levels
- Fixed a bug where regional HQ wouldn't apply prestige goods if original company HQ was present
- Achievements Banana Republic and ProleCorp now each have a trigger of prosperity >= 100 instead of the previous 200
- Fixed an issue that made the things described by the withdraw from treaty tooltip not actually happen
- Fixed support independence not being available between subjects of the same overlord
- Fixed a bug where you could end up blockading friendly shipping lanes, potentially ruining your own army supply
- The Suez Canal decisions now correctly evaluate the Suez canal instead of the Panama Canal
- Fixed an issue in the invasion panel that caused some invading formations to not be listed
- Fixed naval invasions failing to start due to impassable sea provinces
- Fixed an issue where exiled formations could become stuck in certain situations
- Fixed an issue with the Goods Transfer treaty article where it would keep adding the income/expenses from the article even if at 0% shipping lane efficiency. The income/expenses now scales with shipping lane efficiency.
- Fixed a bug where the trade center could start trading before construction was finished
- Fixed a bug that would make the tooltip explaining the maintenance cost of articles lie about which country would be paying said maintenance
- Fixed a bug that would cause some tooltips to incorrectly claim that articles part of enforced treaties have an effect on relationship gain or loss (they don't)
- Fixed an issue where Romania was not formable through its Journal Entries
- Fixed a crash related to pops when loading certain save games
- Fixed a crash related to formation splitting
- Fixed an issue where the AI could sometimes not accept a treaty, leaving the request unanswered
- Fixed an issue with the Goods Transfer treaty article where it would in some situations incorrectly look at the targets convoys instead of the source's when determining how many goods could be sent.
- Fixed an issue with the Goods Transfer treaty article where it would keep sending goods even if the article was not fulfilled.
- Fixed a bug where annexed countries did not properly transfer company CEOs and establishment dates
- Fixed a savegame integrity corruption and a potential crash to desktop caused by treaty article cleanup not being properly performed in all cases
- Countries with Frontier Colonization can no longer offer to not colonize regions at the other end of the world
- Fixed an issue that allowed a country to offer multiple instances of Transit Rights to the other country
- Fixed an Out of Sync issue in multiplayer related to "Countries" and the power bloc principle "Exploitation of Members"
- Fixed an Out of Sync issue in multiplayer related to "Fronts"
- Fixed an issue where invasions could continue after a war had ended
- Auto-expand tooltip text regarding market access now shows greater than instead of less than
- Fixed a small lifetime issue causing the on_entered_into_force effect of non-renegotiatable treaty articles to nevertheless (and incorrectly) be executed when a renegotiated treaty enters into force
- Fixed a bug where Unification Candidates who stopped qualifying to be candidates (in ways other than a leadership play) would not be removed from the candidate list
- Fixed a bug where the import/export value in the Trade Surplus tooltip would endlessly increase each week
- Texas now actually receives Military Assistance from the United States
- Fixed pathfinding issues in colonized states
- Fixed an issue where formations couldn't find a valid path to some split states
- Fixed an issue where the Newsletter bonus map would be unselected after restarting the game
- Fixed eliding mobilization percentage numbers in the diplomatic play panel
- Fixed some typos in the broken treaty notification text
- Fixed an instance of broken localization in the Treaty Broken Catalyst notification
- Helmuth von Moltke (the Elder) no longer rolls random Ideologies and IGs
- Fixed an issue where Power Bloc map textures appeared black after loading save games
- Fixed an issue where the AI could capitulate in the wrong war
- Fixed an issue where the Korean Empire pop clothes had the wrong colours and textures
- Fixed overlapping text for Company panel headers in Polish language
- Fixed a bug where gold (the good) was displayed on the market panel
- Fixed an issue where defeated fleets failed to return home for repairs when another admiral died

## 1.9.4

Patch 1.9.4 was released on 2025-06-26[4] with checksum *8df9*.

### AI

- AI is now more interested in composing treaties with alliances and defensive pacts when they do not already have allies
- The AI will no longer break treaties with allies if both are involved in the same diplomatic play
- The AI will now never declare neutrality before Countdown to War if doing so would void an alliance or defensive pact
- The AI is now a bit less deterministic about which articles they include in treaties
- Fixed a bug where the AI would sometimes not correctly send a composed treaty if they were trying to make it more fair first

### Balance

- Alliance/Defensive pact treaties are no longer automatically broken by being opponents in a diplomatic play but only if it actually goes to war

### Bugfixes

- Fixed an issue where the article inputs would not update if you opened the draft treaty panel with more than one country in a row without letting the game tick in between.
- Enforce Treaty Article wargoals now follow the same inclusion limitation rules as normal treaty articles
- Fixed an issue where the original treaty was removed before a renegotiation was actually accepted, meaning it would be gone if the renegotiation was declined.

## 1.9.5

Patch 1.9.5 was released on 2025-06-27[5] with checksum *a209*.

### AI

- Fixed a bug where the 'fairness of current treaties' value was being wrongly calculated, resulting in major penalties for quite fair treaties
- Fixed a bug where the 'fairness of current treaties' value was being applied during renegotiation
- Fixed a bug that made the AI unwilling to get foreign investment rights in smaller economies instead of being unwilling to *give* foreign investment rights to smaller economies

## 1.9.6

Patch 1.9.6 was released on 2025-07-10[6] with checksum *442e*. It was first released as an opt-in beta on 2025-07-02.[7]

### Improvements

- Deployment of additional invading armies is now disallowed for invader allies
- It is now possible to request the other party to owe you an obligation as part of treaty negotiations
- Consuming Prestige Goods now increases the Standard of Living of Pops, based on how large a percent of the value of their buy package is Prestige Goods
- Land invasions are now disallowed if it would take too long for armies to reach the target state
- The cost of a treaty article now scales depending on existing lobbies and on the ranks of involved countries
- Resetting a treaty (either full reset or either side) when renegotiating an existing treaty will now restore the treaty to the original treaty being amended instead of removing all articles (this also happens to fix an issue where you could remove non-renegotiable articles from treaties by resetting them during renegotiation)
- Treaty Articles can now be flagged as either hostile or friendly and will be considered neutral if neither flag is set. Anti-Country Lobbies will increase the cost of friendly articles (such as Alliance) and reduce the cost of hostile ones (such as Treaty Port), while Pro-Country Lobbies have the opposite effect. Neutral articles are not impacted by lobbies.
- The Indian Railway in the Purveyor of Progress JE can now be completed without owning the states, or indeed the railways. It is available to any Indian country that becomes large enough to have a state in each of the listed strategic regions.
- Industrialists in newly created Company Countries now start off with the Colonialist Ideology
- The 'Earning Recognition' Journal Entry now gives advancement for being in the top #10 GDP rankings, and only retreats when you are not in the top #30 GDP rankings rather than retreating based on SoL or GDP per capita. It also retreats if you have Isolationism or a variant thereof.
- Western Guangdong now has the 'Natural Harbors' state trait

### AI

- Fixed a bug that was preventing the AI (and autonomous investment) from investing in more than a single level of certain buildings (most prominently Power Plants), caused by using the wrong profitability calculation
- Fixed a bug that was preventing the AI from constructing Trade Centers in states that did not already have a Trade Center
- Subjects are now far more likely to accept when having a Law imposed upon them by their Overlord as long as they are loyal
- The AI now values states that it has not incorporated yet but can incorporate much higher
- The AI now only cares about non-colonization agreements in regions that could be plausibly colonized by both countries
- Fixed a bug where the AI would sometimes not withdraw from war reparations treaties after the binding period was up, even if they had no reason to keep the treaty active
- The AI will now be a bit more keen on reaching its spending targets for innovation and construction when they can afford to
- The AI will now aim to have larger, more effective fleets instead of splitting its navy into tons of tiny fleets
- AI Britain will now properly prioritize taking a treaty port in Hong Kong when resolving the Opium Wars
- The AI logic for acceptance from gifting articles and equal exchange has been reworked to be more consistent and to look at the entire treaty instead of only specific articles. The AI now also only considers articles it actually wants to be gifts.
- Fixed an issue where the AI would spam ports in foreign states that were lacking infrastructure
- Improved the AI's ability to perform specific constructions for the purpose of company formation
- Fixed a bug where the AI would sometimes break a treaty they had just enforced through a wargoal

### Balance

- The impact of obsessions & prestige goods on goods substitution now varies for different pop needs, with a reduced effect on food in particular as over-focusing on a single food can cause starvation
- Increased the demand for grain, fruit and groceries slightly
- The enactment chance from Law Commitment now scales with how much higher rank the committed-to country is compared to the committer. If the countries are of equal rank there is no bonus at all.
- Humiliation is now the default war goal instead of money transfer, can be used against non-rivals, and only requires you to control any enemy state (including unincorporated ones) but has less impact on leverage. A define can be toggled to change the default war goal back to money transfer.
- Most wargoals that require any enemy state to be controlled now require any incorporated state to be occupied, so that for instance Money Transfer can't be extracted by occupying a random African colony
- The 'Dangerous Gunsmiths' event no longer lowers infamy for the arms exporter, so that you can no longer continually maintain 0 infamy just by exporting guns
- The Capital State of a country now generates some more baseline Infrastructure from number of Pops than regular states
- Silk is now purchased as part of pop Luxury Item needs, though with a low weight compared to other goods in the category
- Reduced the construction cost of Power Plants from 800 to 400
- Money Transfer articles are now capped to a total combined 50% of country income
- The events 'Disrespecting our Maps' and 'A Dubious Claim' no longer give infamy, but instead just reduce relations between the squabbling colonial powers
- Financial Districts, Manor Houses and in particular Company Headquarters now employ less people
- States now lose market access relative to % of enemy occupation, and become isolated if fully occupied
- Pop movement attraction base value impact from Suppressing has been reduced by half
- Law Commitment to "Slavery Banned" now also increases pop attraction of the Abolitionist Movement
- Revoke Claim now only requires you to control any enemy state (including unincorporated ones) when targeting a state neither side owns
- Military Access, Transit Rights, No Tariffs, No Subventions, Foreign Investment Rights and Trade Privileges now only requires you to control any enemy state (including unincorporated ones) when used as a wargoal
- Removed the pop birth rate penalty from high population relative to arable land, as there are now other mechanics to handle this
- The 'Rogue Prince' modifier now gives Tewdoros II +5 offense and +5 defense instead of the quite ludicrous +30 it used to give
- Tewdoros II now starts with 'Experienced Offensive Planner' instead of 'Expert Offensive Planner'
- AI acceptance for Company Monopoly articles now also takes resource potentials into account
- Trade Capacity is now only reduced by 25% under Canton System (down from 50%)
- Market Capitals now also provide 25% Trade Advantage
- The "Equality for All" Journal Entry now checks for base cultural acceptance
- Increased Arts Academy profitability on all PMs
- Western Guangdong now starts with a larger Trade Center, Port and Shipyards and a lot more Silk/Tea exports
- The "Bremerhaven" state trait now also grants 5% MAPI
- Added Rye Farms as possible extension building type to the Russian Vodka company and Guinness
- The state region of Hebei now starts with 5 Coal potential instead of 4
- Invented a few thousand more residents of British Ceylon so that the state can actually somewhat function
- Confédération générale des vignerons now requires Joint-Stock Companies instead of Central Planning, so Champagne can be produced earlier

### Content

- Added 7 new Prestige Goods. 6 of them are generic Prestige Goods so that they are a bit more widely available, no matter which country you play. Among them are notably a version of Small Arms and Artillery.
- Added a new generic Military goods company producing Small Arms and Artillery. They can produce the new generic Small Arms Prestige Good. Also note that we have shifted around the icon from the Munitions company to this new company and have instead created a more fitting icon for the company producing Munitions and Explosives.
- The 'Age of Princes' Journal Entry (and associated 'Unify Ethiopia' diplomatic play) will now only activate once Centralization is researched
- Tossing out your current ruler to enthrone Tewdoros II will now generate radicals, and refusing to enthrone him will generate loyalists, so that the event is only 99% a no-brainer instead of 100%
- Ensured that the Bombay Burmah company also checks for overlord's treaties. The tooltip looks a bit funky for the moment, but it works. This will be fixed in a future update with custom localization.
- Located about 3.5 million Nepalese hiding in cave systems under the Himalayas and dragged them out into the light (or: Nepal is no longer drastically underpopulated compared to best-guess historical population studies, and has received adjustments to arable land and resources as well)
- Added historical clothing to William of Hanover
- Nepali culture now has the Indo-Aryan culture trait

### Interface

- Moved the Nation Formation tab to the Diplomacy panel (was on the Journal panel before)
- The Treaty Drafts now hides the AI Acceptance icons and values of Articles if the other country is another player
- The goods transfer article now allows filtering goods with the usual categories found in the market panel
- The goods transfer article now allows sorting the visible goods by any of: name, price, buy / sell orders balance, buy orders, or sell orders. The sorting can be applied in reference to the market of either of the two countries involved
- When a treaty proposal is declined, that treaty will now be used as the basis for negotiation the next time you go to draft a treaty with the declining country (this does not persist over save games, however).
- Infamy generation and maneuvers cost breakdowns for enforced treaty article wargoals now display the scripted factors that participate in the calculation
- Added a proper tooltip for non-fulfillment conditions for Military Assistance treaty article
- Added an empty state for Political Movements in the Pop Details panel
- Added paging for Articles in the Treaty fancy tooltip when there are more than 10 Articles on one side
- Generic Prestige Goods in historical companies should now correctly show the requirement to fulfill the according Journal Entry to unlock it
- Added the "Religions Overview" map mode to the list of map modes accessible through the Society panel
- Made sure the Treaty UIs are not allowed to expand too much horizontally to avoid a horizontal scrollbar appearing in some cases
- Moved the Front map marker tooltip to the side to make sure it never displays over the front marker when it grows too large
- Changed the default map mode for the Power Bloc panel to be the Power Bloc Leverage map mode
- Added information about who is using/owing obligations directly to the Treaty Proposal tooltip when received
- Fixed a whole bunch of overlapping texts in various panels
- Made the acceptance text in the Send Proposal button tooltip be allowed to multiline so all languages with longer texts can see the acceptance chance percentage

### Modding

- Added new value link gdp_ranking
- Added a trigger for controlling whether a company charter is possible to grant or not
- Added new trigger num_potential_resources
- Treaty article visible trigger now takes scope:other_country so that visibility can take both countries into account
- Treaty article goods input triggers now takes scope:other_market_goods for the good in other country's market
- Fixed a bug where set_country_type effect would not work when changing from decentralized country type
- Added a trigger for controlling whether a monopoly can be made with a given building type
- Added new value link ai_colonization_value
- Fixed a bug causing crashes on startup if the map spline network referenced invalid state regions
- Added years_to_incorporate state trigger

### Bugfixes

- Fixed an issue where armies were automatically deployed to naval invasion fronts and became locked to it this way
- Fixed a bug where the AI (and autonomous investment) was calculating the profitability of constructions for all current levels of existing buildings, resulting in it being very reluctant to construct new buildings
- Fixed an issue where predicted earnings for buildings were being badly miscalculated, resulting in numerous issues such as no privatization of buildings and no construction of Trade Centers
- Fixed a bug where other companies already owning building levels in a state were prioritized over monopoly companies for privatization
- Fixed a bug where disbanding a company could lock an industry from being monopolized by another company
- ports now produce much less infrastructure, coastal states instead start with a bonus to infrastructure from population
- Fixed an issue where the AI would send too many units to a naval invasion front, causing themselves penalties
- Fixed a bug where the AI would treat State Transfers as being worth nothing when giving states away due to an incorrectly set flag. This could also cause the AI to sometimes refuse treaties they were clearly shown to accept.
- Fixed a bug where pops were unlikely to migrate to a treaty port where their culture had low acceptance
- Fixed an issue where sway proposals weren't being sent to players
- Fixed a bug where sometimes articles could get randomly invalidated for no reason when a lot of articles were being invalidated globally on the same update (most prominent when BIC dissolved)
- Fixed an issue where wargoals would not be enforced if a Make Protectorate war goal was included and there was a mix of war goal holders
- Fixed an issue where the peace deal notification wouldn't include all war goals if you capitulated and the "Make Protectorate" war goal was executed
- Treaties will now have all their articles be frozen if the two countries in the treaty are at war with each other.
- Fixed a bug that was blocking Treaty wargoals from being properly used in Sways
- Fixed an issue where invasions could continue after a war had ended
- Fixed an issue when battles couldn't occur on the front due to incorrect occupation data
- Fixed an issue when generals couldn't advance due to missing state assignments
- Fixed a bug where if you had a regional HQ in the annexing country and all your property was in the annexed country, your company would destroy its own HQ and move it to the annexing country
- Fixed an issue where power blocs' current leverage wouldn't decrease if all power blocs had a predicted leverage lower than their current leverage
- It is no longer possible to incorrectly promise an obligation to a country that already owes you an obligation, when drafting a treaty
- Fixed an issue where naval invading formations lacked a supply route
- Fixed an issue where formations without a valid supply route still received full supply
- Fixed a bug where pops working in Private Infrastructure and Financial Districts were not able to join the Petit-Bourgeoisie due to missing workplace checks
- Fixed a bug where subjects whose overlords were on the same side in a war could sometimes become war leaders and/or peace negotiators
- It is no longer possible for Great Qing to construct Trade Centers in other countries under Canton System
- Fixed a bug where some military buildings could have more levels than units they supplied
- Landlocked countries can now only use Goods Transfer articles with neighbors
- Fixed an issue where defeated fleets failed to return home for repairs when another admiral died
- Fixed an issue where the AI could capitulate in the wrong war
- Fixed a bug where after disbanding an HQ, a null object HQ could start buying levels
- Fixed an issue when occupation could persist after a war ended
- Unrecognized Nations can no longer grant Companies Colonial Charters as they are not allowed to have the Chartered Company type of Subject
- Fixed a case where countries not owned by a company would replace their ruler unnecessarily when becoming independent
- Fixed an accidentally missing functionality whereupon a country that repudiates an obligation will see obligations they owe or call in in treaties be worth less acceptance score
- Fixed an issue where formations couldn't be deployed to fronts with split theaters
- Proposals that are let expired/timed out are now considered declined, therefore it is no longer possible to skirt around an obligation being called in during a treaty negotiation by pretending nobody's home
- Fixed the number of available options reported for some articles during treaty negotiations
- Fixed a bug where some buildings were setting wages too high relative to profitability targets, resulting in low dividends for ownership buildings
- Article types whose `visible` trigger returns false are no longer visible in the list of articles shown when drafting treaties
- Fixed a caching issue leading to formations sometimes being incorrectly considered to be on a front they were not on
- Fixed a bug where conscripts would never upgrade to armies
- When setting inputs for an added Treaty wargoal, acceptances are no longer shown
- Fixed an Out of Sync issue in multiplayer related to fronts
- Alliance articles now correctly check if either side can still have an alliance or have researched Multilateral Alliances
- Fixed an issue where the goods producer rank could be evaluated incorrectly
- Treaties that are only drafts no longer affect daily relations gain/loss progress
- Fixed ruler traits not working for company executive rulers
- Fixed an issue where the law commitment article would give a bonus to enactment chance to both countries, instead of just one of them
- Fixed a bug that would cause new conscription centers associated with a mobilized army during war to be created in an inactive state
- Fixed a bug in the AI calculation for constructing Trade Centers where it was applying a nonsense profitability score instead of only looking at Trade Potential
- Fixed a bug where the Alliance treaty article would be unavailable without explanation in the tooltip (the reason was already having an Alliance and lacking Multilateral Alliances)
- Fixed a bug where annexing a state or a country sometimes did not correctly remove the Regional HQ in it
- Fixed a bug where the acceptance tooltip for subject actions contained a NULL_OBJ due to missing scope
- Fixed a bug where some 'request' diplomatic actions (such as request knowledge sharing) could not be used
- Fixed a bug where Treaty Ports were not correctly considered part of a Market when calculating its average Trade Advantage, resulting in (among other things) inconsistent Advantage numbers in the UI
- Fixed an issue where formations could be auto-deployed to distant fronts
- Fixed a bug where the world_market_access trigger was returning market access instead
- Fixed an issue where the influence cost of treaties wouldn't display correctly when looking at a signed treaty
- Fixed an issue where the influence cost in the treaty draft panel would display an incorrect value when resetting either side
- Fixed an issue where the influence cost of treaties would display as 0 when renegotiating a treaty
- Fixed an issue where the article numbering wouldn't display correctly in some situations
- Fixed a bug where pops would sometimes start with a much lower standard of living than their income could afford
- Fixed a bug where the game would show "units are too different" when checking the upgrade for the top line unit
- Fixed a bug with the has_subject_relation_with trigger which caused it to evaluate false if checked from the overlord's perspective
- A bunch of references to Isolationism now also take the Canton System into account
- Fixed a bug that would cause enforce treaty article wargoals used as part of sways to change allegiance during a diplomatic play to fail to allow the player to actually select the desired inputs
- Fixed some instances in which alliances and defensive pacts were not always correctly taken into consideration for various operations
- Fixed a number of events (such as lobby_events.15, 'Good, not Foreign') that were checking for foreign investment rights in either direction instead of checking for it in a specific direction
- Fixed an issue where the popup when you attempted to revoke a Trade Rights company charter incorrectly claimed it would nationalize buildings
- Right-clicking on a treaty proposal now declines it, rather than effectively ghosting the opposite party forever
- Fixed a graphics bug where black squares would appear during revolutions due to a particle issue
- Fixed an issue where tooltip with effects for breaking a treaty would show misleading information, either in the form of effects that would not be applied or by hiding effects that would be
- Fixed an issue where barracks could merge incorrectly during the annexation of split states
- Fixed a bug where changing resolution when using vulkan would sometimes offset the positions of your mouse and some gui elements
- Fixed a bug where Agitators would join a different movement from the predicted one when being invited from the exile pool
- Fixed a bug where the population census data would fail to display a pop's interest group
- Fixed a bug where the 'disqualified unification candidate' status would be reset if a country had a successful revolution
- Fixed a crash to desktop caused by supply routes and formation caches disagreeing after an unknown condition
- Fixed a visual-only bug causing the balance tooltip to list money transfer incomes / expenses twice: once as part of diplomatic pacts incomes / expenses, and once as temporary incomes / expenses
- Fixed a display issue in the migration tooltip where it would show you the wrong market in case of a treaty port
- Requesting Military Assistance in the "The Eastern Frontier" Journal Entry no longer creates duplicate treaties
- Fixed the *_scope_ally scriptlist not working correctly (blocked establishing the Anglo-Persian Oil Company, among other things)
- Fixed the num_defensive_pacts link not working correctly
- Transfer state treaty articles that transfer a split state that stops existing after the treaty enters into force are now removed from the treaty. If this causes the treaty to have no more articles, the treaty will dissolve without any effect or penalty. This fixes a bug were using a transfer state article to transfer a split state could lead to the article referring to the null state.
- Fixed a crash that could happen when using the markets map mode
- Fixed a visual bug that would lead to incorrect influence maintenance costs displayed when drafting treaties after removing directed articles originating from the non-player country
- Fixed an issue where total and per-market exports/imports would not add up correctly
- Fixed micro freezes related to Coat of Arms and text icons
- Fixed an issue where in some cases the notification for a treaty proposal being declined would display the wrong country if the treaty was a renegotiation
- Fixed a (visual only) bug where all buildings appeared to have privatization disabled under Laissez-Faire
- Fixed an issue that caused a crash when hovering the Innovation breakdown when playing the game in German
- Added description for when there are no units to be upgraded
- Auto-expand tooltip text regarding market access now shows greater than instead of less than. This time for real.
- Fixed the description text for the "Returned from Exile" notification
- Fixed an issue that caused Law tooltips to omit certain effects
- Fixed a (visual only) bug where the wrong country would sometimes be shown as getting infamy when withdrawing from a treaty
- Fixed an instance in Money Transfer AI acceptance where the text would sometimes refer to the wrong country
- Added STATE_ASTURIAS & STATE_CORSICA in treaty_ports scripted triggers for Western Protectorate achievement
- Fixed a source of error spam in the power bloc panel

## 1.9.7

Patch 1.9.7 was released on 2025-07-17[8] with checksum *1741*. It was first released as an opt-in beta on 2025-07-15.[9]

### AI

- Fixed a bug where autonomous investment would not update its state target for a building type but instead construct the same building in the same state over and over
- Fixed a bug where the AI would not construct a sufficient number of ports to fix critical convoy shortages
- Fixed a bug which was preventing the AI from establishing new military formations in some cases
- Fixed another issue that was preventing the AI from withdrawing from enforced treaties
- The AI is now fine with building Railways in states that have sufficient Infrastructure, if those Railways would be profitable
- Improved the AI's ability to prioritize spending on government buildings when its current spending is far below its desired targets

### Balance

- The Boer States now start out guaranteed by Britain as per the Anti-Cheese Treaties of 1836
- Gaza now starts with an army

### Interface

- Treaties now get their own budget entry in the budget tooltip, rather than being nested under the Diplomatic Pacts entry

### Bugfixes

- Fixed a crash that would sometimes occur when viewing a state's population tab
- Fixed a bug when the regional HQ kept investing despite a broken foreign investment pact
- Fixed a bug where an overlord capitulating would sometimes not enforce wargoals targeting their subjects in the same play
- Fixed a bug where the winning revolutionary side would disband all original country companies instead of transferring them
- Fixed a bug that would cause enforced money transfer articles to not be properly accounted for when capitulating
- Fixed a bug that would cause money transfer articles to transfer twice the stated amount
- Fixed a bug that would cause money transfer and goods transfer articles to not be properly frozen when the two bound countries get involved in a war on opposite sides
- Fixed the wrong country being shown for diplomatic stance acceptance factor for existing treaties

## 1.9.8

Patch 1.9.8 was released on 2025-08-12[10] with checksum *0724*. It was first released as an opt-in beta on 2025-07-22.[11]

### Features

- Added a new Multiplayer Lobby Game Setting to change file transfer speed. Significantly increased default speed. Higher speeds may or may not cause issues for some clients connecting; in that case try lowering the speed.
  - The file speed transfer settings are not in 1.9.8 and may result in errors, but will not affect functionality otherwise. This will be resolved in 1.10 when it releases on the 23rd of September, and we are sorry it was not implemented fully in this hotfix as we announced earlier today.[12]

### Improvements

- You can now promise obligations while renegotiating a long-standing treaty where obligations hadn’t already been promised. (only available in new saves or for new treaties in old saves)
- Regional HQs are now flagged as owned by foreign investors
- Improved the hiring logic for military buildings so they always try to hire as much as their training rate allows
- Combat units whose building is lacking enough officers to properly support the amount of servicemen employed by said building will receive a multiplicative malus to their offense and defense, scaling by how badly the building is lacking officers
- When a revolution has a democratic form of government, the revolutionary IGs will now join a special Revolutionary Party which is the only one eligible for votes, to ensure democratic revolutions are not stuck at zero legitimacy. If the revolutionaries win, the Revolutionary Party will dissolve at the next election
- Finishing the "The Conquest of Algeria" Journal Entry now also grants a modifier to those states that increases the speed of incorporation
- Treaty Ports will no longer invalidate if temporarily lost as a result of a secession or revolution and will be reinstated after the rebels have been defeated
- Subjects can no longer establish Colonial Administrations as this would cause their relationship to break instantly
- Improved labels for the progress bars in France's "Divided Monarchists" Journal Entry
- There are no longer default tariffs on imports for goods a country does not domestically produce, or on exports for goods a country does not domestically consume
- Treaty Ports are no longer invalidated if the treaty port becomes isolated from the host country as a result of an ongoing civil war or secession
- Added more initial Government Administration levels to Persia, Mascara and Sokoto so that they do not start in a deep bureaucracy deficit
- The Government Administrations in Argentina and Mexico now start with Filing Cabinets active to resolve their initial bureaucracy shortages
- When Germany turns into a generic republican dictatorship it no longer defaults to the Fascist flag, instead it now uses one of two new alternatives depending on whether it was formed by Prussia or not

### AI

- The AI will now care more about economy of scale and constructing buildings where they already exist for certain building types, particularly for heavy industry
- Fixed a bug where the AI would get stuck trying to form a specific company which was not formable due to circumstances such as another company already dominating their target state, resulting in them forming no companies at all
- The AI will no longer slap unnecessary tariffs on imports for goods they do not domestically produce, or exports for goods they do not domestically consume
- Adding a giftable article that the AI wants to a treaty will no longer remove the 'Equal Exchange' bonus to acceptance from an otherwise balanced treaty
- The AI is no longer artificially capped in how much construction, army size and navy size it will aim to have
- The AI is now usually disinterested in being swayed into a play with the Humiliation war goal, as they simply don't consider it valuable enough to potentially go to war over

### Balance

- The construction penalty for Unincorporated States now varies per building group, with heavier penalties for manufacturing and no penalties at all for agriculture
- Added a new "Tsunami" Harvest Condition Type, currently only triggered as a result of the Krakatoa Eruption
- The effects of Devastation have been toned down by a moderate amount to compensate for the additional strain that is now caused by occupation affecting Market Access
- The "Industrialists" and "Christian Missionaries (Devout)" Interest Groups of Hawaii may now also generate Westerners as leaders unless deported and barred from leadership in the "Strengthening our Position" Event
- The Krakatoa Eruption now results in a randomly rolled 0.5 to 1.5°C temperature drop that recovers over a period of five years and increases the chance for certain bad Harvest Conditions to be triggered in the meantime and can be tracked in the Journal Entry at all times (it even comes with a little thermometer)
- France is now much more eager to use the "Greener Grass Campaign" Decree for the duration of the "The Algerian Departments" Journal Entry
- Countries in the Americas are now much more eager to use the "Greener Grass Campaign" Decree for the duration of their "Migration" Journal Entries
- The Devastation caused as a result of the volcano and subsequent tsunami can be recovered faster by employing the Emergency Relief Decree
- Added level 1 ports to Danish holdings in Greenland and Carnatic so they can function better

### Content

- The "The Krakatoa Eruption" Journal Entry and its associated content has received an update
- The Hawaii related Journal Entries "Foreign Interests" and "Influencing Hawaii" have received an update
- The "Investing in Hawaii" Decision has been moved to the "Influencing Hawaii" Journal Entry

### Interface

- The "Readmit the Secessionist States" Journal Entry now lists the exact states need to be reintegrated into the Union and which conditions they currently fulfill
- The checkboxes to owe / use / ask for an obligation are now disabled (with an explanation in the tooltip) during a treaty renegotiation if the renegotiated treaty has been in force long enough for the promised obligations to become effective obligations
- The tooltip shown for article types in the context of drafting a treaty draft will now also report who the maintenance cost of the resulting article would apply to
- The "Send Proposal" button in the treaty draft window is now able to provide information about why it's disabled under more circumstances
- Added more information to the Popularity tooltip
- Improved the localisation of production_tech_events.102 \[formerly "Industrial Boom"\].

### Modding

- Added support for per-building group construction speed modifiers
- Removed the `CASUALTY_MULTIPLIER_FOR_HIGHEST_PAID` define because it's no longer used as part of casualty distribution
- Added the `OFFICERS_TO_SERVICEMEN_RATIO_THRESHOLD` define to tune when the lack-of-officers malus starts having an effect. Setting this define to zero will disable the malus entirely
- Added the `OFFICERS_TO_SERVICEMEN_RATIO_EFFECTIVENESS_FACTOR_MIN` and `OFFICERS_TO_SERVICEMEN_RATIO_EFFECTIVENESS_FACTOR_MAX` defines to determine the range of the lack-of-officers malus at edge conditions
- Added new trigger controls_treaty_port_province
- It is now possible to specify a center province for state regions where the calculated center ends up in a bizarre position, such as in the middle of the ocean

### Bugfixes

- Fixed "Transfer Subject" and "Liberate Subjects" wargoals not being enforced when the overlord capitulates (as opposed to accepting a peace offer, or giving in before war breaks out)
- Fixed an issue with occupation that caused to invasions to fail to launch
- Fixed a bug that would cause the acceptance score shown during a treaty renegotiation to be incorrect if enough time had passed since the original signing date and obligations were involved either originally or during the renegotiation
- Fixed an issue where loyalists and radicals trends would become useless after one year (might require a new game)
- Fixed an issue where formations had no supply in certain situations
- Fixed an issue where companies could purchase building levels owned by foreign investors
- Potentially fixed an instance in Multiplayer games where players would be unable to start a game if they were running multiple mods
- Fixed a bug causing `LibertyDesireLevel.IsActive()` to return false at maximum liberty desire. This fixes, among other potential issues, a bug in which the tooltip for the last liberty desire level in the subject's liberty desire progress bar would stop displaying the weekly liberty desire change once liberty desire reached its maximum.
- Fixed a case where you were sometimes unable to fully colonize a region (such as Alaska) because of how impassable provinces were handled during colonization
- Fixed a crash that would sometimes happen if a company charter wasn't fully removed from a dead company
- Fixed an issue that stopped the "The Chinese Missions" Journal Entry and Taiping Rebellion content from being set into motion
- Fixed an issue that caused the Opium Wars to not resolve properly
- Fixed a bug where the trigger of the Broken Promises achievement could not account for diplomatic play initiators or targets
- Renegotiating a treaty now only requires to have enough influence available to cover the difference in cost between the old treaty and the renegotiated one, rather than the full cost of the new treaty
- Fixed the way casualties are distributed to be proportional to employment, this way it will no longer be the case that as soon as a battle starts all officers die first
- It is no longer possible to incorrectly tick both the "owe obligation" and the "ask for obligation" checkboxes when drafting a treaty
- Power Bloc leaders can no longer abandon their own bloc by joining another
- Fixed an issue where units could be transferred to a foreign military formation during annexation
- Fixed an issue where the "Nationalize All Buildings" war goal wasn't fulfilled after capturing the enemy capital
- Fixed an issue where the "Trade Rights" charter worked incorrectly for Suez and Panama companies
- Fixed a bug when the regional HQ kept investing despite having a broken foreign investment pact
- Fixed a visual-only bug causing the balance tooltip to list money transfer incomes / expenses twice: once as part of diplomatic pacts incomes / expenses, and once as temporary incomes / expenses.
- Fixed an issue where transfer money and transfer goods articles that were frozen due to wars breaking out would not be correctly unfrozen after the war(s)
- Treaty articles no longer cost influence to maintain while frozen
- Fixed a bug where Treaty Port articles would get instantly invalidated if they became frozen or non-fulfilled
- Fixed a bug where Anti-Country Lobbies were always applying the maximum influence cost penalty on friendly treaty articles instead of scaling by clout
- Fixed a case where pops created at game start would get the wrong initial working adult ratio
- Fixed an issue where states could sometimes have -0 Infrastructure
- Fixed a bug that sometimes caused France to not get a claim on Western Sahara when completing the "The Conquest of Algeria" Journal Entry
- Fixed an issue where armies could land-invade via sea
- Fixed "Liberate Country" button being disabled in the country panel
- Fixed an issue where the "Independence" war goal was removed after being transformed from "Liberate Subject"
- Fixed an issue where civil wars could reset the colonization progress of companies
- Fixed one of the root causes where the naval bases would not produce ships
- It is no longer possible to add multiple copies of single-use articles in treaty drafts by quickly clicking on the article while the hardware is subject to particularly high load
- Fixed an Out-of-sync related to tariffs and subventions
- Fixed the working_adult_ratio parameter in the create_pop effect not working
- Fixed an issue that sometimes caused female politicians in West Africa to be naked
- Fixed an exploit that allowed countries, most notably Mexico, to double dip into the migration attraction bonuses granted by the "Populating the Americas" Event
- Fixed a wrongly referenced country in one of the lobby events in German translation (thanks to philliefiffla!)
- Fixed an issue that would cause fluctuating goods prices to not be reflected in the amount of money transferred via goods transfer articles
- Fixed the location of several map markers that were offset in a weird way, most notably for Kyushu
- Fixed the description for the war goal "Leave Power Bloc"
- East and West Micronesia no longer have their state map markers positioned in the middle of the Sulu Sea

## References

1. ↑ Forum: [Hotfix 1.9.1 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1788517), 2025-06-18.
2. ↑ Forum: [Hotfix 1.9.2 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1791382), 2025-06-19.
3. ↑ Forum: [Hotfix 1.9.3 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1806851), 2025-06-25.
4. ↑ Forum: [Hotfix 1.9.4 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1808146), 2025-06-26.
5. ↑ Forum: [Hotfix 1.9.5 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1809263), 2025-06-27.
6. ↑ Forum: [Hotfix 1.9.6 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1836294), 2025-07-10.
7. ↑ Forum: [Victoria 3 | Opt in Beta 1.9.6](https://forum.paradoxplaza.com/forum/index.php?threads/1823373), 2025-07-02.
8. ↑ Forum: [Hotfix 1.9.7 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1848832), 2025-07-17.
9. ↑ Forum: [Victoria 3 | Opt in Beta 1.9.7](https://forum.paradoxplaza.com/forum/index.php?threads/1844037), 2025-07-15.
10. ↑ Forum: [Hotfix 1.9.8 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1854928), 2025-08-12.
11. ↑ Forum: [Victoria 3 | Opt in Beta 1.9.8](https://forum.paradoxplaza.com/forum/index.php?threads/1851538), 2025-07-22.
12. ↑ [Correction post by Pelly](https://forum.paradoxplaza.com/forum/index.php?posts/30673955)
