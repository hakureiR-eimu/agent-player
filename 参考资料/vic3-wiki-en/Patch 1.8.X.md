---
title: Patch 1.8.X
source: https://vic3.paradoxwikis.com/Patch_1.8.X
pageid: 6981
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
**Patch 1.8.X** are all patches beginning with 1.8.

## 1.8

Main article:
Patch 1.8

## 1.8.1

Patch 1.8.1 was released on 2024-11-21[1] with checksum *affa*.

### Balance

- Reduced the stability gain from low liberty desire subjects in the Unstable Raj Journal Entry by 50%
- Buildings will no longer include the impact of taxes on expected Standard of Living when setting wages, so that increased taxes don't automatically lead to increased wages (or vice versa)

### Bugfixes

- Subsistence farms will now set much lower wages and aim to return as much profit to their owners as possible (this was causing world starting GDP and GDP growth to be significantly depressed compared to 1.7)

## 1.8.2

Patch 1.8.2 was released on 2024-11-22[2] with checksum *1fc5*.

### Bugfixes

- Fixed a crash that would consistently happen for some users when launching the game
- Fixed a bug that would happen if the game rule "Loyalties Grace Period" was activated. There would be no gains for Loyalists or Radicals after the period ends.
- Fixed a crash that could happen when a Company was removed

## 1.8.3

Patch 1.8.3 was released on 2024-11-28[3] with checksum *b4be*.

### Improvements

- Cultures will now seek to mass migrate somewhere where their acceptance is improved somewhat. This isn't a hard requirement, if the potential migration target has high enough migration attraction, that can offset the sought acceptance, meaning cultures might move somewhere they are less accepted as long as the target migration attraction is sufficiently higher than the origin one.
- The ratio between acceptance at the origin and at the target will now scale how many pops actually move in a mass migration per week. If the target acceptance is lower than the origin one, less pops will move. If it's higher, more pops will move.
- Presidency Stability game concept now explains conditions that affect the Unstable Raj Journal Entry progress bars
- Updated tooltips to explain conditions that affect the Sikh Sovereignty Journal Entry's 'Empire Stability' and 'Court Intrigue' progress bars
- Imperialism of Promise Journal Entry will no longer fail from civil wars, except secessions
- Power Blocs can now invite Revolutionary nations
- When recruiting a new commander, historical characters will now be displayed more often

### AI

- The AI East India Company should now be more cautious with regards to events that decrease its stability
- Slightly decreased the AIs desire to construct Power Bloc Statues
- The aggression of colonial empires towards Unrecognized Nations now starts off slightly lower and ramps up more significantly as the game progresses
- Britain will no longer ignore the Boer states because they happen to be Recognized Nations when the time to clean up Africa has come

### Balance

- Britain is now a part of the Indian Uprising diplomatic plays by default
- Reduced the income transfer of Chartered Company subjects to their overlords from 40% to 30%
- Rebalanced Indian Presidency stability from a scale of 100 to a scale of 300
- Gave the East India Company claims on much of its historical western frontier from game start
- Reduced the flat liberty desire growth in subjects from annexing low-prestige subjects
- Added 5 years of Memento Mori immunity to all starting leaders and agitators
- Reduced the impact from high/very high taxes on Expected Standard of Living, as the values were a bit overtuned
- Made the British East India Company start with high military wages
- Fixed Portugals conquer weights, it should now correctly prioritize annexing Gaza once the time comes
- Bumped Portugal's starting colonial affairs level from 1 to 2

### Art

- The optimal sunlight positive harvest condition effect is now less intense, appearing colder at nighttime to illustrate moon light rather than sunlight.
- Reduced the effect and strength of wind effects
- Added disease outbreak particle effects
- Adjusted moderate rainfall vfx
- Resolved an issue where the parasol held by pops sometimes clips out in the portrait view

### Content

- The "The Conquest of Algeria" Journal Entry now also grants France a claim on Western Sahara

### Interface

- Political Movements are now sorted by type, and alphabetically within the same type
- The Harvest Condition map marker is now clickable and opens the Food Security tab on the Market panel
- Made the Harvest Condition map marker show up in the default and diplo play map modes on the nearest zoom
- Made the list of movements impacted by enacting or cancelling a law into a paged list so it doesn't take as much screen space in situations where there are a lot of movements
- Made it so when enacting or cancelling a law, movements where nothing is happening to their activism won't be listed
- Added the Acceptance Status icon in front of the status name in modifiers based on player feedback.
- Fixed a bug where localization did not have proper values for decaying civil war progress
- Added a go-to button for the active Movement on an Agitator's Character panel

### Modding

- Added trigger can_pressure_interest_group to political movements, this must evaluate true for an IG to be able to be pressured by a movement, in addition to the already existing supporting clout requirements (Requested by Better Politics Mod for their 1.8 compatch)
- add_loyalists and add_radicals effects now support negative numbers (ie, add_radicals with a value of -0.5 will remove 50% of radicals)
- Scripted progress bars can be marked as inverted so that progress is defined as making progress values smaller

### Bugfixes

- Fixed a bug where civil wars (particularly secessions) could be created without any viable states, resulting in the civil war continually starting and then being cancelled
- For a new insurrectionary movement to 'overtake' the currently active civil war, it now needs to have at least 10% higher activism, fixing an issue where you could have 'ping-ponging' between two civil wars with very similar activism levels
- Likely finally fixed the long-standing bug where battles do not end because the last few soldiers refuse to die or get demoralized
- Fixed an issue that would incorrectly clear occupations of a country that was occupying states belonging to a country that got annexed by losing an insurrection diplomatic play
- Fixed an issue where princely states were unable to be annexed by independent India, citing available Doctrine of Lapse
- Cultures will now require at least 30 general cultural acceptance to mass migrate somewhere. This general acceptance can then be reduced when the pops actually migrate due to things like Cultural Community Acceptance, but as a baseline there shouldn't be cultures moving somewhere they will for sure be Violently Oppressed.
- Government/Subsidized buildings are now able to override the usual hiring restrictions when hiring from ownership buildings, if the new job is equal or better to the old one (ie, government administrations can hire Aristocrats from Manor Houses to be aristocrats in government administration, but can't hire them to be clerks)
- Annexing states through events (such as Canadian Federation, Risorgimento etc) no longer generates radicals as though those states were conquered
- Fixed an issue where only passable provinces are counted towards bonuses to colonization speed. Also fixed a separate issue found with counting impassible provinces in state regions
- Fixed a bug where revolutionary or colonization AI wouldn't merge it's army formations
- Made it so that the Treaty of London Journal Entry will automatically select a response after six months
- Fixed bug where civil war progress would reset on save/load
- Fixed a bug where ideological incompatibility was applied to the countries that don't use a caste system
- Fixed a bug where the popup for agitators would not show which movement they created or joined due to the movement being created after the popup is fired
- When opening the game in debug mode, fixed the error spam related to ig_suppression
- Fixed the cooldown for the "The Contagious Diseases Acts" event so it does not fire if any of its modifiers are still in effect
- Reinvestment value is now calculated from each country's investment laws and tech instead of averaged over the building
- Total building reinvestment income now applies reinvestment efficiency
- The "Construct the Suez Canal" Journal Entry now correctly completes when building the Suez Canal
- Fixed a bug where countries created via create_country effect would get the wrong cultures
- Fixed a bug where heathen tax was applied for all of the religions, now it doesn't apply to religions with a positive acceptance effect
- Fixed a bug for The Positive Stage journal entry progress bar
- Fixed a bug where the Liberal Movement could not be created if the Radical Movement already existed, resulting in weird behaviors such as Market Liberal agitators not having a movement to join when finishing the Corn Laws
- Fixed some start up errors relating to character history
- Fixed a bug where chance of stalling during enactment was not predicted correctly in the law enactment tooltip
- Fixed scoping issue that could result from revolutions in British East India Company
- Sacred Civics II now properly lowers liberty desire for subjects with the same state religion
- Fixed a bug where Azadi Achievement sometimes became unavailable after loading a save
- Fixed a crash in harvest conditions
- Added cooldown to Italian Unification's Pan-Nationalist Radicals event
- Fixed a crash in map graphics
- Fixed a bug where after changing the land border adjacencies for the markets were not properly recalculated
- Fixed an issue where the Rani of Jhansi would not make use of her custom DNA
- Fixed a bug where nationally owned buildings built in other nation's states did not grant the part of their balance going to reinvestments to anyone
- Fixed a rare crash when resyncing a game
- Fixed cancellation trigger for "The Rise of Radicalism" event
- Added military shipyards and whaling stations to influence 3d center model in the port city
- Fixed a bug where ports in split states wouldn't show wharfs and fisheries from time to time
- The "The Scramble for Africa" Journal Entry now also accounts for states controlled by subjects
- Fixed a bug where certain Danish, British, and Portuguese Indian possessions would start as incorporated
- Historical figures now use their intended clothing assets
- Fixed very small countries having their armies stuck in their home HQ when at war
- Fixed wrong reference to Elections concept in factors attracting pops to Radical movement
- Fixed formatting for the "The Integration of the Nordestinos" event
- Fixed a bug where French Company Billboards appeared where they shouldn't appear
- Fixed a bug where the literacy tooltip would flicker

## 1.8.4

Patch 1.8.4 was released on 2024-12-05[4] with checksum *1a3e*.

### Features

- Made the "Exempt from Service" subject interaction accessible to all

### Improvements

- Changed companies so that if they own at least one level of a building, any new level that is built in it by local private investors will be company owned
- Made companies much more likely to be the one privatizing buildings if the building fits their type
- The East India Company now gains annex wargoals against rebellious princely states in the Indian Uprising
- Doctrine of Lapse now transfers the contents of the target's treasury to the East India Company
- Collectivization now only ever targets privately owned levels and is the number of levels to collectivize is calculated as a fraction of privately owned levels, so nationally owned levels are not subject to it, meaning that countries with Cooperative Ownership/Collectivized Agriculture can now also have a public sector and make proper use of public sector foreign investment
- The "Emergency Relief" Decree will no longer auto-cancel as long as least 20% of the population experience some form of starvation
- An independent Ceylon now automatically becomes Sri Lanka
- Improved the clarity of Unstable Raj tooltips

### AI

- Russia/Britain now start neutral towards Mexico, so they don't block US westward expansion by default
- The AI now makes more of an effort to reach its desired level of construction and innovation generation
- The AI will now never accept being cut down to size as part of a peace deal and have to be capitulated to enforce this specific wargoal

### Balance

- Removed restriction that you could not assimilate if you lived in homeland
- Removed restriction that you can only assimilate to cultures with which you share a cultural heritage trait
- A political movement with 100% militancy can now always 'replace' another movement with less than 100% militancy for the purposes of getting to start a civil war, even if they don't meet the usual 10% higher requirement
- Removed the restriction for conversion on the Violent Hostility acceptance status
- Allowed several revolution events to fire for secessions as well
- The efficiency bonus to private investment now applies all the way up to 50 million GDP, up from 10 million, to make the private sector more able to keep up with intense early game government investment
- Declaring Bankruptcy now radicalizes a minimum of 25% of the country population, with shares in buildings owned adding to that minimum
- Bankruptcy no longer increases the amount of loyalists & radicals gained on SoL changes
- Bankruptcy now reduces leverage gain, migration attraction and MAPI (the latter representing the general shock to the national economy causing business to become more localized)
- Bankruptcy now drastically increases the time it takes to change institution levels (all institutions are still reset to level 1 when declaring bankruptcy)
- Ownership buildings that own subsistence building levels now contribute less money to the investment pool relative to how large a part of their portfolio is subsistence
- Increased base wage and dividends weight for Shopkeepers
- Manor Houses can no longer invest in mines & power plants, and are much less likely to invest in logging & rubber
- Buildings will now lay off employees rather than lower wages if wages are already so low that the employees are going to be rapidly radicalized
- Subsidized buildings will no longer lower wages to increase profitability if wages are already so low that the employees are going to be rapidly radicalized
- Adjusted provinces in the Carnatic so that Pudukottai can't be cut off entirely from the EIC in rare cases
- "Secret Police" Political Movement Activism reduction per level has been reduced from 10% to 5%
- The impact of number of claims on the Fascist Movement pop attraction has been reduced by 50%
- The Fascist movement will now attract more middle and upper class pops if there are any powerful leftist movements in the country, it will now also more proactively poach from the Cultural Majority and Reactionary Movements
- Increased the movement pop attraction for Leftists and Social Democrats moderately, increased even further if certain conditions are met depending on the movement type
- Anarchist movements will now be a slightly less upset on average
- Extraction Economy will no longer destroy Power Plants when enacted
- Buildings are now a bit more willing to raise wages if their workers are being radicalized by low SoL
- Honorable Restoration now instantly fails if you declare bankruptcy
- The conscription rate added to revolutions/secessions from popular support & clout has been reduced and capped at +10%

### Art

- Added locust swarm harvest condition effect
- Added optimal sunlight harvest condition effect
- Tweaked color of heatwave and disease outbreak ground effect

### Interface

- Updated how the affected movements are displayed in the tooltip when enacting Laws
- Added information about the significant threshold of 25% Movement Activism to relevant concept tooltips

### Modding

- Added new trigger to check for the percentage of the population in a state or country that belongs to any of the primary cultures in that country
- Added an effect to set the interest group of a character
- Added modular data functions to retrieve the data model for movements impacted by changes in law enactment as well as getting the values for how much they are impacted

### Bugfixes

- Fixed a bug where political movement success chance wasn't applied until the law started being enacted
- Secessions of Cultural Minority Movements now require their culture to make up at least 5% of the population for the homeland state to be a valid target for secessions
- Fixed a bug with the Turtle Island Journal Entry buttons that left them unable to target relevant nations
- Fixed an impassible terrain colonization bug, where a country could proceed colonizing impassible terrain it had no land access to
- Civil Wars that have no valid uprising states (for instance, secessions from cultures with no homelands in your country) are no longer able to start
- Extraction economy now correctly applies multiplicative investment modifiers instead of additive ones
- Fixed a bug where buildings at low profit levels could 'yo-yo', hiring employees one week and firing them the next week
- Cultural majority movements should now properly select states weighted by how much population belonging to primary cultures are in those states
- Fixed a bug where some buildings could have an owner in the null object state after annexation
- The "Declaration of Independence" achievement can no longer be triggered by switching controlled country to an independent one
- Fixed a bug where Texas became the wrong kind of subject in the Texan War of Independence content
- The Journal Entry "A New National Identity" now allows for assimilation of fully accepted pops into the country's new, South American culture
- Resolved an issue that prevented rulers from abdicating when they should be able to
- Fixed a bug where capitulating countries in wars with more than 2 participants could cause war goals to stick around
- Fixed a bug where we didn't spawn civil war events
- Fixed an issue where Italian radicals would not get removed when annexed as a part of Risorgimento Pan-Nationalism, potentially resulting in the annexing country being annexed in turn due to inheriting all those radicals
- Fixed a bug where colonization would be seemingly stuck due to ghost occupation
- Fixed a bug where players could see a subsidize button on canals and government buildings
- Fixed issue that prevented Consolidate Colonial Rule from detecting British subject states
- Fixed Earning Recognition not advancing when a country has high SoL
- Fixed a crash related to trade routes and shipping lanes
- Alaskan Industrialists no longer lack IG traits
- Pressing the "Promote European Migration" button in the "Populating the Americas" Journal Entries now correctly spawns a migration target
- Fixed tooltip for the Imperialism of Promise Journal Entry's fail conditions
- Cancellation of colonization of incorporated states is now prevented when that will annex the colonizer
- The "Pro-Slavery" Movement will no longer be extremely upset about the lack of Barracks or Naval Bases in slave states if Slavery is completely abolished
- Fixed map mode interaction tooltip for establishing colonization where multiple error messages were written
- Fixed issue that occasionally assigned exiled characters ideologies which made no sense

## 1.8.6

Patch 1.8.6 was released on 2024-12-11[5] with checksum *9358*. Patch 1.8.5 was released only as a beta.[6]

### Improvements

- Insurrectionary countries are now allowed to reform their government, so that they don't get stuck at low legitimacy
- Herat historical characters now have Pashtun culture and Sunni religion

### AI

- The AI will now generally avoid declaring bankruptcy while at war, as the effect of doing so is often worse than staying in default
- Fixed an issue where the AI would overvalue labor savings on PMs, resulting in it keeping those PMs active even when they resulted in shortages
- Fixed an issue where the AI would sometimes fail to reform to the government they wanted

### Balance

- Reverted the change that allowed cultures to assimilate in their homelands, as this resulted in far too much ahistorical assimilation in places like British India. We plan to revisit this in the future to see where it makes sense to allow it, but for now we have added defines to allow modders to re-enable it if so desired
- The "Total Separation" law now correctly blocks all conversion again
- The "Freedom of Conscience" law no longer allows for conversion of pops of Acceptance levels 4 and 5
- Britain will no longer force successful player East India Companies to become the Raj
- After a civil war ends, there is now a 6 month grace period before another one can start, to give the deradicalization impact of civil war ending a chance to take effect on movement activism
- Reduced the construction needed to build gov. admin buildings, to make it easier to fix otherwise unresolvable ADM shortages
- Reduced the base number of individuals radicalized when declaring bankruptcy
- Reactionary movements can no longer appear at the same time as Legitimist movements in France
- Enabled Enlightened Royalists to agitate for more causes
- Reduced the impact of country turmoil on activism of the Reactionary movement
- Reduced the impact of active laws on activism of the Anarchist and Fascist movements, to compensate for the large number of law groups those ideologies care about

### Modding

- Whether cultures can assimilate into different heritages is now controlled by the ALLOW_ASSIMILATION_ACROSS_HERITAGES define
- Whether cultures can assimilate in their homelands is now controlled by a the ALLOW_ASSIMILATION_IN_HOMELANDS define

### Bugfixes

- Fixed a bug where a player could not disband units after civil war has broken out
- Fixed a bug where occupation weren't flipped back after enemy occupation
- Fixed a bug where armies defending against naval invasion on occupied land would not get any units participating in the land battle
- Fixed an issue where Interest Groups could end up rebelling together with Political Movements despite being significantly ideologically opposed to those movements
- Fixed a bug where the country budget showed the wrong income value
- Fixed another crash during updating shipping lanes
- Fixed a random crash when closing or switching lenses
- Fixed Literacy tooltip data missing in Russian localization
- Fixed an instance of Error spam occurring in Spanish localization in the Movement tabs related to concept_political_movement_pressured_short
- Removed an old string in STATE tooltips in Russian localization
- Fixed inverted modifier causing bankruptcy to increase institution change speed instead of decreasing it
- The beginning of Reconstruction will no longer unincorporate Washington D.C
- Researching Pan-Nationalism no longer blocks Religious Minority movements from spawning everywhere instead of just British India
- Fixed an issue where inappropriate events could fire and immediately cancel during secessions
- Fixed a bug where political movement success chance wasn't applied until the law started being enacted
- Fixed a bug that could result in a Lobby Demand targeting the wrong country
- The Fascist movement can now correctly attract Agitators to its cause
- Fixed an issue where abdication could cause enacting a null law if a revolutionary tag already existed
- Fixed an issue where natural interests from subjects would not properly propagate to overlords of overlords
- Fixed a bug where abdicating the throne during a civil war could cause a ruler switcheroo with the insurrectionary country due to the heir joining the insurrection but remaining heir to the loyalists
- Divided Monarchists coups no longer incorrectly occur at 75% progress
- Fixed an issue where religion wage discrimination modifiers weren't being applied.
- Characters sent on the Tibetan Expedition will now return to service properly
- Fixed a bug where a player could get multiple lobbies against the same country after independence war
- Fixed the radicalism prediction for movements tooltip being incorrect when starting or canceling the enactment of a law
- Fixed a bug where the Sacred Civics III principle did not give the reduction to Liberty Desire unlocked in Sacred Civics II
- Fixed an issue where abdicating the throne could result in ending up in a personal union with a civil war country
- Added Quetta to the formable India
- Fixed an issue affecting the way interest groups and movements calculated relative stances on ideologies, resulting in problems such as the law_enactment_stance trigger not returning correct results and insurrectionary countries selecting the wrong laws
- Fixed princely state characters with child traits
- Fixed an issue where the Extradition events could not fire due to secessions
- Fixed an issue, which occurred in the Opt in Beta 1.8.5, where the ALLOW_ASSIMILATION_ACROSS_HERITAGES define wasn't working correctly when disabled
- Fixed an issue where Joshua Norton could be unable to agitate, causing null scopes in his event
- Removed an old Culture string in Russian Localization in the Culture Tooltip

## 1.8.7

Patch 1.8.7 was released on 2025-03-31[7] with checksum *7c15*.

### Art

- New trade ship models for [Trade Ships Bonus Pack](https://vic3.paradoxwikis.com/Trade_Ships_Bonus_Pack)

## References

1. ↑ Forum, [Hotfix 1.8.1 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1716458), 2024-11-21.
2. ↑ Forum, [Hotfix 1.8.2 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1716906), 2024-11-22.
3. ↑ Forum, [Hotfix 1.8.3 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1718089), 2024-11-28.
4. ↑ Forum, [Hotfix 1.8.4 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1719561), 2024-12-05.
5. ↑ Forum, [Hotfix 1.8.6 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1720396), 2024-12-11.
6. ↑ Forum, [Victoria 3 | Opt in Beta 1.8.5](https://forum.paradoxplaza.com/forum/index.php?threads/1719727), 2024-12-06.
7. ↑ [Post by PDX_H4n1baL](https://forum.paradoxplaza.com/forum/index.php?posts/30264668), 2025-03-31
