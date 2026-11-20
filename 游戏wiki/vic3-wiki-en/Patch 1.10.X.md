---
title: Patch 1.10.X
source: https://vic3.paradoxwikis.com/Patch_1.10.X
pageid: 8873
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
**Patch 1.10.X** are all patches beginning with 1.10.

## 1.10

Main article:
Patch 1.10

## 1.10.1

Patch 1.10.1 was released on 2025-09-25[1] with checksum *3093*.

### AI

- The Montenegro AI will now be much smarter about whether to increase or decrease raiding
- AI should no longer be allowed to move all ships out of a fleet and keep the admirals there

### Balance

- Increased Acceptance from being a Primary Culture under Subjecthood, and decreased acceptance from tradition traits
- Increased the chance of the "Pursue the Title of Eastern Rome" event firing for Greece during the Megali Idea Journal Entry

### Bugfixes

- Asked the Silesian Poles if they could hold off with protesting against the government until next week [implemented a temporary fix for a bug where Prussia would annex all of Austrian Silesia following a Polish uprising]
- Players can no longer modify other players military formation
- Fixed an issue where the Matter of Hungary acceptance condition could not tick under any circumstances
- Fixed an issue where Hungarian uprisings in foreign countries could cause the "Crisis on the Danube" event
- Fixed hotjoin Out of Sync caused by dead political movements keeping reference to pops
- Fixed a hotjoin Out of Sync caused by construction queued buildings that were just finished as player hotjoined
- Fixed an issue where Montenegrin Raiding would not be removed from states under some circumstances
- The Central Europe tag can no longer get the Case for Yugoslavia Journal Entry
- Fixed an issue where some characters couldn't be granted leadership under Multiculturalism
- Fixed an issue where Constitutional Pressure gain/loss from wargoals was reversed

## 1.10.2

Patch 1.10.2 was released on 2025-09-26[2] with checksum *750b*.

### Bugfixes

- Fixed fleet getting stuck in combat perpetually after war ending abruptly
- Fixed fleet getting stuck in combat perpetually after ending an invasion manually
- Fixed an issue where a movement disbanding would remove the "Movement Suppressed After Civil War" modifier, allowing it to reform and immediately revolt again
- Fixed an issue where the "Muster Conscripts" button for the Balkan League could have its modifier excessively multiplied

## 1.10.3

Patch 1.10.3 was released on 2025-10-01[3] with checksum *81b8*.

This patch contains many changes from the [GDFIX Day](https://forum.paradoxplaza.com/forum/index.php?threads/1858550) on 2025-09-12, indicated with "[GDFIX]".

### Improvements

- [GDFIX] Made colonization ignore population of source state when determining speed penalty (thank you Alxe for the suggestion)
- [GDFIX] Added option when releasing a nation to keep states considered homelands for your primary cultures (thank you Deutsches Kaiserreich for the suggestion)
- [GDFIX] Military wages now also affect the prestige gain from Navy power projection (thanks Tony for the suggestion)
- [GDFIX] When enforced as part of a peace agreement or capitulation during war, the Independence war goal now also automatically also nationalizes overlord-held building levels (thank you BamBam for the suggestion)
- [GDFIX] The 'September Convention' treaty name template now names the treaty dynamically after the month it was signed in instead of it always being September (thank you Martin Anward aka Wiz, for suggesting your own fix I suppose…)
- It is now possible for companies to 'privatize' buildings under Command Economy
- The Defend against Invasion button now works even if the invasion hasn't started yet. If the front for the invasion hasn't spawned, it will station the formation in the target HQ for the invasion, if the invasion has started and the front exists, it will deploy the formation directly to the front
- Generals will now also join defensive invasion battles and not simply send their troops if stationed as a garrison in an HQ
- Partial Shopkeeper/Academic-owned companies now pay 25% of their dividends to the workforce in their owned buildings
- Partial Bureaucrat-owned companies now pay 25% of their dividends to the government
- Reworked how Ideological Incoherence is calculated. You should now generally have an easier time forming single-party governments and governments which disagree on minor issues, and a harder time forming massive governments with strong and conflicting opinions
- Reworked the logic for cultural and religious secessions - states with low percentages of the relevant pops will be much less inclined to secede, unless their Obstinance or Turmoil is particularly high
- The South American National Identity Journal Entries now trigger a National Awakening for their respective cultures
- Adjusted demographics for the Baltic States, Lithuania, and Poland to reflect the historical makeup of their aristocracies
- Increased the Activism of the Polish National Movement in Russia whilst the Organic Statute of 1832 is active
- Adjusted demographics for Ireland to reflect the historical demography of its Aristocrats, Soldiers and Officers pops

### AI

- The AI will now be less inclined to conquer non-homeland or non-claimed states that it does not share a land border or strategic region with
- Reduced the AI's base desire to unify Germany and Italy in the early game
- The AI will be much more inclined to spend money on economic buildings when it has the Industrialise AI strategy, or during the Gründerzeit
- Brought the aggression of the Unify Italy diplomatic strategy into line with the Unify Germany strategy
- Added a new Montenegro AI strategy to ensure it keeps its trade centres subsidised

### Balance

- [GDFIX] Made colonization speed account for paused colonies (thank you Alxe for the suggestion)
- [GDFIX] Added a lot of Obsessions to various cultures (thanks Tony for the suggestion)
- [GDFIX] Political Movement support from Wealth now scales against the political strength from wealth levels, meaning that the support of a single wealthy individual is much more significant than support from a large number of poor individuals (thank you rskhm | BPM for the suggestion))
- [GDFIX] The 'Force Nationalization' wargoal now requires you to control all your own states instead of requiring you to occupy the enemy capital (thank you to BamBam for the suggestion)
- [GDFIX] GDP owned by your country in other countries now counts towards the reinvestment multiplier, so that a country with a massive investment pool from foreign holdings will not have it artificially boosted further (thank you to Blackpoolgo4it2 for the suggestion)
- [GDFIX] Machinists and Engineers now contribute to the Investment Pool under economic setups where they receive dividends (thank you to CaelReader for the suggestion)
- [GDFIX] Added Grocery taboo to Jewish religion to reflect their dietary restrictions (thanks nullpotato for the suggestion)
- [GDFIX] Added Rye throughput bonus to the Ursus Company (thanks germaniec7 for the suggestion)
- [GDFIX] The Launch Military Incursions decision in the Conquest of the Desert now requires Logistics instead of Civilizing Mission, and adds some infamy when taken (thank you Heinrich IV for the suggestion)
- [GDFIX] Haiti starts with Homesteading now (thank you immeska for the suggestion)
- [GDFIX] Changed the trigger of the United Fruit Company to allow foreign investment to fulfill forming conditions.
- [GDFIX] Removed Rice Farm potentials from Hokkaido (thank you to markus for the suggestion)
- [GDFIX] Increased Wood potentials throughout Sweden, Norway, Canada, and the Northern and Western United States (thank you to markus for the suggestion)
- [GDFIX] Increased Iron potentials for Norrland and Svealand (thank you to markus for the suggestion)
- [GDFIX] Added Vineyard potentials to Tyrol, Bavaria, and Delvidek (thank you to markus for the suggestion)
- [GDFIX] Added Tobacco potentials to Wisconsin, Indiana, New York, Pastaza, and Mosul(thank you to markus for the suggestion)
- [GDFIX] Removed Rye potentials from Oulu, Kola, and Yakutsk, and added Rye potential to Outer Manchuria (thank you to markus for the suggestion)
- [GDFIX] Added Iron and Sulphur potentials to Cyprus (thank you to markus for the suggestion)
- [GDFIX] Added Fruit potentials to Pastaza (thank you to markus for the suggestion)
- [GDFIX] Added Rubber potentials to Antioquia and Cauca (thank you to markus for the suggestion)
- [GDFIX] Added Coffee potential to Goias (thank you to markus for the suggestion)
- Austria is no longer able to revoke the Hungarian Twelve Points without pushback by using the Regime Change power bloc interaction
- Increased acceptance of primary cultures under Subjecthood to 100. This should fix cases of discrimination events firing for primary cultures under Subjecthood
- Peasants now get far fewer loyalists & radicals from Standard of Living changes
- The amount of radicals/loyalists gained from Standard of Living increases now starts scaling down after level 15, as each successive SoL level after that represents diminishing returns in actual impact on a pop's perceived quality of life, and it was previously far too easy to turn your entire upper class loyalist
- Buildings with foreign owners will now generally pay lower wages (relative to foreign-owned level fraction), as said foreign owners don't really care all that much if their wage dumping creates radicals in other nations
- Increased Movement Activism modifier from the Springtime of the Peoples Journal Entry from 25% to 35%, and added a -50% enactment time modifier to both Springtime of the Peoples and Red Summer Journal Entries
- Manorialism is now only enabled for Austrian Crown Land or Personal Union-type subjects
- Replaced the additional company slot from the canal companies with a free charter. The company slots often proved to be more of a curse than a blessing since when you lost the prosperity bonus, you could end up in a downward spiral. Additionally, the other bonuses they provide are so much more effective than the pre 1.9 competitiveness bonus that we believe they should still be viable with the addition of the charter. As always we'll keep an eye on feedback on this.
- Serbia now has Homesteading at game start
- Buildings are now more stingy with their wages when no minimum wages are set
- Made starting Hungarian revolutionaries immune to Memento Mori effects until 1856
- Increased starting Italian radicals for Austria
- Increased the attraction of Hungarian Aristocrats towards the Intelligentsia Interest Group and Liberal Movement whilst the Hungarian Revolution Journal Entry is active
- Reduced the maximum and minimum impacts of Fervour on attraction to various cultural movements
- Cultural Minority Movements under Subjecthood are no longer affected by base cultural acceptance. Instead, they are affected by average cultural acceptance of pops of the relevant culture
- Pop attraction to National Liberal movements is now affected by pop literacy
- Reduced the penalty to Devout attraction from literacy, as they were overly penalized in the late game
- Removed the max institution level increase from Secret Police/Guaranteed Liberties and put it behind Central Planning and Mass Surveillance techs instead, so that it isn't so easy to counter movement radicalism early on. The effects of National Guard were slightly reduced as this means National Guard can now be increased to level 5 in the late game
- Added additional Activism factors to National Liberal movements
- Increased the base attraction of Aristocrats, Clerks, and Academics to cultural minority movements, and reduced the base attraction of Clergymen
- Increased base political strength from votes to be more in line with the generally increased wealth levels across the game. Society techs that increase Authority now also increase voting power further
- Reduced the impact executives have on interest group political strength, and increased the number of building levels a company must own to get the maximum effect
- Removed an outdated supply increase modifier that came into effect when a formation was mobilized. This was invisible to the player, so we replaced it with higher good cost increases on the supply mobilization options. Overall values should remain largely the same
- The Age of Metternich Journal Entry now requires 25% revolution progress, or a successful Springtime of the Peoples revolution
- Various pro-slavery ideologies will now oppose enacting Colonial Slavery when a more slavery-friendly law is active
- Montenegro will need to learn to respect women before enacting advanced economy laws \[blocked the enactment of non-Traditionalism or Industry Banned economy laws whilst Women in the Fields is active\]
- The alternate complete condition of The Algerian Departments now requires the Amazigh and Maghrebi cultures to be above 40 average acceptance, and the Sunni religion to be above 15 average acceptance
- Building Minimum Wages modifier is now spread over multiple different institutions
- Moved max Social Security investment level modifiers from Welfare laws to tech
- Moved max Health System investment level modifiers from Health System laws to tech
- Reduced Individualist and Market Liberal ideologies' tolerance of the Right to Associate law
- Made the various variants of the Liberal ideology approve of National Guard, and disapprove of No Home Affairs
- Made the various variants of the Liberal ideology disapprove of Censorship, neutral towards Right of Assembly, and approve of Protected Speech
- Moved the "Sorbia is Serbia" achievement to the Hard achievements category
- Under Census Voting, pops can now vote from wealth 10 (down from 15)
- Under Wealth Voting, pops can now vote from wealth 20 (down from 25)
- Changed the arable land threshold for a state to be eligible for mass migration from 20 to 10
- Increased the base attraction of Officers and Soldiers to the Absolutist Movement
- Reduced the base attraction of Peasants to the Labour Movement
- Positivist characters may now support the Liberal Movement
- Clergymen are no longer affected by the literacy-related malus towards the Religious Majority and Minority Movements
- Increased starting Ottoman gold reserves
- Lahej now starts with a Trade Center exporting coffee
- The "Legacy of the Commonwealth" attraction modifier for Polish pops to cultural minority movements now only applies to Aristocrats
- Countries with Anarchy may no longer enact Extraction Economy

### Art

- Added DNA to Marshal Radetzky von Radetz, courtesy of Lord R of Morgenröte
- Improved the colouring of Serbian military caps

### Content

- [GDFIX] Added Yankee homelands to District of Columbia, Maryland, Delaware and West Virginia (thanks DonQuijote for the suggestion)
- [GDFIX] Added a chain of succession for all French dynasties (thanks The Watcher (F.E.) for the suggestion)
- [GDFIX] Changed Savoy and Piedmont's hub and state names to be Italian by default. They will switch to the french version once controlled by France (thanks Il Fop for the suggestion)
- Added the People of the Book law, a generic version of the Ottoman Millet System for Muslim countries (because this is too exciting to wait until 1.12 for)
- Added anti-overlord lobbies to Serbia and the Danubian Principalities
- Changed the Springtime of the Peoples and Divided Monarchists revolution events to be based on whether one's capital is going to join a Revolution
- Added pro- and anti-overlord lobbies to Hungary
- Added pro- and anti-Hungary lobbies to Transylvania
- Changed the non-Sardinia-Piedmont Italian states' Citizenship laws to Subjecthood
- Added additional flags for Montenegro, and corrected the starting flag
- Added Yemeni Highlands state trait to Yemen
- Added some missing German dynamic state names (e.g. Franconia is now called Franken if owned by German speaking population)

### Interface

- [GDFIX] Disabled spam of notifications for when someone joins a diplomatic play and they have tons of subjects (thank you Ilya for the suggestion)
- [GDFIX] Added a player countries map mode (thank you Drasp for the suggestion)
- [GDFIX] Fixed the state interface so we show correct goods contribution to gdp % (thank you balticšprott | IEX for the suggestion)
- [GDFIX] You can now see information about foreign GDP ownership in the GDP tooltip (thank you Blackpoolgo4it2 for the suggestion)
- [GDFIX] The pop list movement support display now provides an accurate number and a correct breakdown tooltip (thank you to rskhm | BPM for the suggestion)
- [GDFIX] Laws with/without government support are now sorted in order of highest chance to enact instead of lowest (thank you for the suggestion acranmer10)
- Tweaked the investment log tooltip layout for better readability
- Added the "Players" map mode to the map mode list in the Diplomacy panel
- Added a new National Awakening map marker tooltip to be clearer of what the map marker stands for
- Made the religion map mode automagically appear when you click the Religion tab on the Society panel
- Added a decimal to the infrastructure from population modifier on the basic Forestry company, so we can see the actual value (0.7) rather than 0
- Improved the tooltip for the simultaneous secession Activism factor
- Fixed the out of bounds text in the Culture tooltip and made sure no text is allowed to go out of bounds before line breaking
- Improved the tooltips for effects of pro- and anti-overlord lobbies on Liberty Desire
- Fixed the interface so we show correct icon in theme selector when theme is dynamic
- Fixed the Movement Suppressed After Civil War modifier icons being the wrong colours

### Modding

- Added country_block_government_reform_bool modifier which blocks a country from reforming their government
- remove_modifier now looks up the timed modifier for it's multiplier when building descriptions. This means we correctly describe the expedition budgets in the JE's failure/complete state descriptions.

### Bugfixes

- [GDFIX] Fixed an issue where various left-wing ideologies would not properly weight Serfdom in political party calculations (thank you CaesarVincens for the suggestion)
- [GDFIX] The Fascist leader ideology now requires Political Agitation instead of Mass Propaganda, to bring it in line with the requirements for the Fascist Movement (thank you CaelReader for the suggestion)
- [GDFIX] Fixed an issue where Moderniser characters could not support Moderniser movements (thank you to CaesarVincens for the suggestion)
- [GDFIX] Juan Silvano Godoi and Rafael Barrett will now correctly spawn for Paraguay (thank you to CaesarVincens for the suggestion)
- [GDFIX] Fixed an issue where releasing Russia or Belarus would give the Devout ideology redundant Moralist ideologies (thank you to CaesarVincens for the suggestion)
- [GDFIX] Fixed an issue where power bloc join calculations used an incorrect scope for assessing identity/principle scores (thank you to CaesarVincens for the suggestion)
- [GDFIX] Corrected Asa Thurston's culture to Yankee (thank you both Dryhad and CaesarVincens)
- [GDFIX] Fixed several issues with subject flags for United Tribes, Tibet, Jamaica, Bretagne, and Brunei (thank you to CaesarVincens for the suggestion)
- [GDFIX] Corrected localisation for the has_commander_order trigger to display the relevant order (thank you to CaesarVincens for the suggestion)
- [GDFIX] Fixed some japanese loc formatting to allow showing data (thanks maruta for the suggestion)
- [GDFIX] Fixed errors in the names of Pakubuwana IX and George Strickland Kingston (thank you to CaesarVincens for the suggestion)
- Fixed an Out of Sync from Scripted additional Radicalism for cultural movements
- Austrian Upper Silesian Poles have been properly instructed to go back to Austria when they lose their secession war (Fixed so Secession wars keep track of what provinces belonged to who for split states)
- Fixed an issue that caused Korean clothing to be overridden by Manchu and Han clothes
- Made Armies stationed at an HQ also be able to defend Fronts in the HQ's strategic region and made them visible in all relevant contexts like in the calculation for front advantage
- Fixed so we use all primary cultures shared heritage to calculate acceptance on cultures
- Pops part of a Secession are now redistributed when state is split back to original owners
- Buildings part of a seceding state are now given back to the original owners
- Fixed a crash caused by dead pops in political movements
- Fixed stuttering that occurred with too many countries existing on the map
- Fixed an issue where the Koreanic language trait group was unlocalised
- Fixed an issue where country-specific traits for the Petit-Bourgeoisie would be overridden by generic ones
- Fixed an issue where momentum set in history would not correctly impact historical elections, resulting in issues such as the Whigs incorrectly being calculated as having won the 1836 elections
- Fixed an issue where Serbia would gain Dynastic Loyalty from improved relations with the Ottomans, rather than the reverse
- Fixed improve/damage relations description being broken when the progress is exactly 0% due to opposing actions
- Gave the Labour Movement a stance on Labour Associations
- Fixed a bug that blocked acquiring the "David Slays Goliath" achievement as a Yugoslavia formed from Montenegro
- The "Prussia of the Balkans" achievement now accounts for the North German Confederation
- The Dual Monarchy will no longer annex a player Croatia upon formation
- Changed French movement stances to match those of their corresponding character ideologies
- Fixed an issue where the Positivist Movement would appear too early in the game, possibly causing a no-win scenario during the Springtime of the Peoples
- Fixed a bug in cross-country secessions where secondary targets of the uprising would get a 'Crush Secession' wargoal targeting the wrong country
- When 'inheriting' radicals from conquered states, this is now correctly shown as the reason for those radicals being added to your total amount
- Removed top hat from Dordije Petrović-Njegos
- The has_potential_resource and num_potential_resources triggers now work correctly for buildings that use arable land. This should fix some issues the AI had with establishing agricultural companies which use these trigger for their construction targets.
- Fixed and removed a jarring jumping around of the State Trait map markers in the Production map mode when you hover any Market
- Removed doubled Activism modifier from Springtime of the Peoples on Cultural Minority movements
- Fixed an issue where the Megali Idea Journal Entry could disappear before a completion criteria was selected
- The Reunify China Journal Entry will no longer appear for non-Chinese countries
- Fixed an issue where the Liberal Movement had incorrect stances on land reform
- Fixed a typo in a loc reference that resulted in company_category_bureaucrat_owned not showing its correct text
- Fixed an issue that interfered with the calculation of liberty desire from pro- and anti-overlord lobbies
- Alaska can no longer be sold more than once
- Fixed a bug on pop details panel showing two religion icons
- Removed one of the duplicated goods icons in the Pop Need fancy tooltip
- Owning all of Upper Silesia is no longer a requirement to form Czechoslovakia
- Corrected the country flavour text for Ogaden, Anuak, Borana, Omo, Hadiya, Wolaita, Qwara
- Fixed Hadiya's market using a placeholder
- Lobbies can no longer request diplomatic plays against revolutionary or secessionist countries
- Fixed an issue where the Great Eastern Crisis journal entry was visible to those who did not own National Awakening
- Fixed an issue that could cause subjects of the United Principalities to receive Bessarabia, rather than the United Principalities themselves
- Fixed Missing localization for RULER_TITLE_PREMIER
- Fixed an issue that could result in Orleanist monarchs for France not having the correct ideology (Voice of the People)
- Fixed an issue where "The Feminine Order of \[State\]" would incorrectly evaluate its trigger
- Fixed an issue where some battles would have just a loc key as their name
- Fixed a typo in defines which affected USE_NATIONALIZED_ECONOMY_OF_SCALE_PENALTY
- Fixed an issue where certain ideologies referred to non-existent laws in their IG leader chances
- Fixed a bug that could occasionally cause Maximilian von Habsburg to replace Franz Josef

## 1.10.4

Patch 1.10.4 was released on 2025-10-03[4] with checksum *6093*.

### Bugfixes

- Fixed a bug that applies subsistence farm penalty multiplier when calculating starting wage so the poor hardworking aristocrats don't starve
- Fixed a bug with on_election_campaign_end not being called

## 1.10.5

Patch 1.10.5 was released on 2025-10-09[5] with checksum *3087*.

### AI

- Fixed a bug where the AI would construct barracks/naval bases in some cases where they did not actually consider the construction affordable
- The AI is now much more willing to invest in construction sectors when they have insufficient construction capacity to drain their investment pool
- Fixed a bug where the AI would never use movement suppression or bolstering due to wrongly assigned priority
- Fixed a bug where AI spending on government construction could be blocked by wanting to disband units that could not be disbanded due to civil war
- AI Austria will now avoid enacting the United States of Greater Austria for as long as Franz Josef is Kaiser
- Fixed an issue where the AI would repeatedly activate and deactivate authority-costing spending items such as Consumption Taxes and Charters
- Made the AI more willing to try and ditch old-fashioned laws such as Traditionalism when they get to a certain level of tech

### Balance

- Incorporation speed is now slower for non-Homeland states, but increases with the Centralization line of society techs
- Farmers now pay Land Tax instead of Poll Tax, so long as they are employed in a building that uses arable land
- Reduced the requirement for the Age of Metternich Journal Entry's Policing and Home Affairs institutions to investment level 2

### Content

- Revised the failure requirements for the Federal Solution Journal Entry for Austria to only fail if a revolution or secession is taking place in Austria's core regions
- Hungary is now forbidden from signing the union with Transylvania whilst at war or committed to a diplomatic play

### Modding

- Added a trigger to political movement civil war data for whether specific IGs can join the civil war when it rises up or not

### Bugfixes

- Fixed a bug where a very accepted minority (>100 Acceptance) could override the primary culture's homeland bias
- Fixed a bug where capitalists were not receiving any dividends from certain company ownership structures
- Fixed an issue where Aristocrats/Capitalists would sometimes start with much lower Wealth than their income could afford due to their final wealth being calculated before final dividends were properly determined
- Fixed a bug where timed modifiers applied to Journal Entries would never actually time out
- Fixed an issue where the game could freeze when closing the Power Bloc principles window.
- Added a cooldown to the The Reckoning event for Serbia
- Fixed an issue where Austria could be annexed by Italy during Italian Unification if it was in the process of forming the United States of Greater Austria
- Fixed a crash to desktop that could occur when a secession failed and it was cleaning up a secession state that did not exist anymore
- Fixed an issue that caused almost all Unrecognized Nations in Africa outside of the Great Lakes to start with Isolationism when they should have Mercantilism instead
- Wounded Soldiers and War Widows will no longer be enslaved when they are ejected from the barracks (It would try and merge them with the largest pop which if you had slavery, are most likely slaves)
- Fixed an issue where Austria could be made a subject of Romania through the Unite the Principalities Journal Entry
- Dependents being merged into a different pop will try and merge into something sensible and not suddenly become aristocrats of a different culture/religion
- Fixed an issue where the German-led Austrian Aristocracy would occasionally join cultural minority movement secessions
- Fixed an edge case where Croatia could not be detected by the United States of Greater Austria
- Fixed front names being shown incorrectly for non-participants
- Fixed an issue where some subject flags would continue showing up despite the No Subject Flags gamerule being active
- Korean Clergy are now still appropriately traditionally dressed when Korea adopts westernized fashion

## 1.10.6

Patch 1.10.6 was released on 2025-10-13[6] with checksum *43af*.

### Bugfixes

- Fixed a bug where buildings would periodically reset their wages back to baseline, most noticeable as all buildings paying out the same wage at the start of the game
- Fixed a bug where construction of buildings monopolized by companies could be blocked by incorrect validation of who holds the monopoly
- Fixed a bug where autonomous construction could sometimes be blocked by the economy of scale factor overriding other, more critical factors such as whether there is actually workforce available in the state
- Fixed a bug where the ai_evaluate_autonomous_construction console command was partially printing data for government construction, resulting in incorrect values

## References

1. ↑ Forum: [Hotfix 1.10.1 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1860263), 2025-09-25.
2. ↑ Forum: [Hotfix 1.10.2 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1860447), 2025-09-26.
3. ↑ Forum: [Hotfix 1.10.3 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1861262), 2025-10-01.
4. ↑ Forum: [Hotfix 1.10.4 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1861603), 2025-10-03.
5. ↑ Forum: [Hotfix 1.10.5 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1862385), 2025-10-09.
6. ↑ Forum: [Hotfix 1.10.6 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1862911), 2025-10-13.
