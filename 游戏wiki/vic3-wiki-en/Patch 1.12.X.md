---
title: Patch 1.12.X
source: https://vic3.paradoxwikis.com/Patch_1.12.X
pageid: 9046
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
**Patch 1.12.X** are all patches beginning with 1.12.

## 1.12

Main article:
Patch 1.12

## 1.12.1

Patch 1.12.1 was released on 2025-12-12[1] with checksum *9124*.

### Bugfixes

- Fixed a bug where buildings that do not use slaves would always be hiring regardless of whether they were losing money
- Fixed a bug where having a high level of welfare would cause building owners to wage dump to extreme levels and let the government pick up the entire tab. Now they only wage dump to a moderate level and let the government pick up a smaller tab.
- Fixed a bug when power bloc trade capacity modifiers weren't applied
- The Cultural Commonwealth power bloc and the associated Shared Canon principle now only requires ownership of Iberian Twilight

## 1.12.2

Patch 1.12.1 was released on 2025-12-18[2] with checksum *55b6*.

### Improvements

- Increased the culling of agitators in the exile pool as it was easily possible to have +300 agitators at any given time sitting around in a café in Switzerland by the mid-game. This scales off character popularity and will target non-historical agitators first.
- Elections now show you the actual number of voters and voter turnout in addition to political strength shares from votes
- Removed the Filipino Mestizo Standard of Living requirement from the Advancements in the Archipelago Journal Entry (Iberian Twilight)

### AI

- Allow Regulars to move home and temporary AI formations to merge if they are not involved in a significant war. Helps late game global empires where their armies would get stuck in far away possessions.
- Changed how the AI tags armies to make sure always one army is tagged as garrison in a HQ. Helps with late game global empires which will slowly have eroded away all their garrison to be active armies.
- Added a simplistic version of army movement for peace time to just move armies back home. Another source of why armies would get stuck in literally nowhere.
- The Carlists will now fully focus their attacks on capturing Madrid upon the start of the Royal Expedition
- Fixed an issue that made the construction AI sometimes unable to correctly detect goods shortages, resulting in not appropriately prioritizing fixing those shortages
- The AI will no longer incorporate states when they already have a bureaucracy deficit
- Added a small debug tooltip for armies which is available in debug mode

### Balance

- Reduced the base Sugar output from Sugar Plantations from 50 to 25
- Reduced the Sugar output from the "Automatic Irrigation" production method from 80 to 50
- Reduced the Sugar output from the "Vacuum Pans" production method from 20 to 5 and the Coal input from 3 to 1
- Reduced the Sugar output from the "Steam-Powered Mills" production method from 40 to 15 and the Coal input from 5 to 2
- Reduced the Sugar output from the "Centrifugal Machines" production method from 70 to 30, the Engines input from 2 to 1 and the Coal input from 10 to 4
- Reduced the Sugar output from the "Violent Treatment" production method from 50 to 40
- The Molds PM for Tobacco Plantations now requires some iron input and machinists and isn't always strictly better than hand-rolled
- Added a modifier to Spain's reestablished American colonies that increases their incorporation speed by 20%. This is also retroactively added to existing save games (Iberian Twilight).
- Interest Groups will no longer be willing to negotiate if their stance on the enactment would be worse than Strongly Oppose
- Reduced the requirements to complete The Two Spains to 80% progress in favor of either liberals or conservatives (Iberian Twilight)
- It is now possible for buildings to 'hire' slaves from a non-subsistence building if the slaves are disproportionate in number to other employed professions
- Reduced the Automobiles output of the "Mass Production" production method from 60 to 50
- The "National Guard Preoccupied" modifier no longer gets removed upon start of the Royal Expedition in the Carlist War
- The "Support Emperor Pedro" interaction for Portugal now increases the progress of the Brazilian Magnanimous Monarch Journal Entry by 20%
- All "Violent Treatment" plantation production methods have had their "Slave Imports" modifier increased to 10% and no longer increase for each additional building level
- Reduced the Standard of Living bonus for Slaves from the "Factory Radios" production method from 2 to 1
- The Loyalists/Radicals from Political Movements modifier from "Factory Radios" production method has been increased to 5% and no longer increases for each additional building level
- The "Lectors" production method for Tobacco Plantations now also increases the conversion rate in the state by 10%, reduced the Standard of Living bonus for Slaves from 1 to 0.5
- The "Assembly Line" production method for Automotive Industry no longer removes 500 Machinists
- Colony-type subjects must now become Dominions in order to reform out of Colonial Administration law
- Fascist movements now gain Activism proportional to their Support
- In 1.12.0 we increased the amount of blockade strength required to fully blockade a state by a substantial margin, however we also overshot a bit with our original changes. In this hotfix we are reducing the amount of blockade strength required per value of traded unit by 33%.
- Each level of Naval Base now increases blockade resistance in its state
- Reduced the amount of Fervor required by the "Integrating the Brazilian Nation" Journal Entry to 65
- The "Second Amendment" Amendment now increases mortality by 1% in non-homeland states and 0.5% per level of turmoil instead of increasing mortality by 1% in all cases
- Required Blockade Strength is now capped at 100k, to prevent late-game scaling from making it impossible to blockade some states
- The event "Carlism on the Frontier" now also adds devastation to Andalusia
- Anarchist and Communist movements now gain Activism proportional to half of their Support
- Enabled gaining more intense variants of Political Concessions in non-Collaborative Negotiations
- Increased attraction of middle- and upper-class pops to Fascist movements proportionally to the sum of the Activism of all non-marginal Labor, Communist, Socialist, Anarchist, and Nihilist movements in the country
- Increased base legitimacy gain from the Geheime Staatskonferenz, and removed the time limit on repealing it
- Loyalist pops are now substantially less attracted to Communist and Anarchist movements
- Reduced base pop attraction to Fascist movements
- The Anarchist movement no longer has a malus to urban pop attraction
- Disabled the options for Cuba to merge with Spain or Iberia in the "La Siempre Fiel Isla de Cuba" event if Spain is a player (Iberian Twilight)
- Enabled the option for Cuba to become a dominion in the "La Siempre Fiel Isla de Cuba" if Spain is controlled by the AI (Iberian Twilight)

### Art

- Updated the Portuguese and Italian communist flags with period-appropriate symbology
- Updated the communist flags of Sardinia-Piedmont, Lucca, Modena, Two Sicilies, Tuscany, and Parma to use period-appropriate symbology
- Added medals to Spanish generals and the late-game Russian Tsar outfit

### Content

- Added movement activism values to most amendments, enabling movements to gain or lose activism based on the presence of amendments
- Two Sicilies and Portugal now start with the Latifundias law
- Added a starting Portuguese claim to Southern Angola
- The "Propose the Pink Map", "Incorporate Goa" and "Invest in Macao" decisions are now available for Iberia (Iberian Twilight)
- The "The Glorious Revolution", "Eye for an Eye", "A Saharan Twilight", "The Internacionalistas", "Equatorial Foothold", "Maghreb's Garden", "Além-mar Africano", and "The Pink Map" Journal Entries are now available for Iberia (Iberian Twilight)
- Iberia may now get the "Our Fortunate Regeneration" or "Economic Regeneration" Journal Entries, depending on whether it was formed by Portugal or Spain (Iberian Twilight)
- Kaurna now starts the game with the Homesteading and Consumption-Based Taxation laws
- Increased the fishing and rubber potential of Senegal and Guinea to account for the removal of Gambia
- Repealing the "Reinstated Fueros" Amendment will now immediately radicalize some Basque pops

### Interface

- Made sure amendments show up on other country's Law's tooltips
- Undeveloped and available arable land are now both shown in the state panel, to avoid the mistaken impression that countries with Serfdom lost a lot of arable land
- Made a clearer separation between "Delete save" and "Delete all saves" buttons to reduce misclicks
- Fixed an issue where the acceptance score displayed for sway offers for a war goal to enforce a treaty article with an input, would ignore the input in question, giving the impression that the AI would accept a sway when they wouldn't
- Fixed an issue where completely unavailable laws would be listed in the law imposition screen
- The Latifundias law is no longer visible if one has Tenant Farmers enacted
- Made sure the correct buildings are listed in the Heavy Industry and Light Industry building group tooltips
- Added the right country's player name if that country is played by a player to the send proposal button tooltip in treaties
- Made the header texts in fancy tooltips fit better within the tooltip frame

### Modding

- The has_amendment trigger now correctly checks for the amendment_type scope instead of amendment key
- The amendments on_activate effect will now correctly fire when added to an already active law
- Added a data function to check if the player has any potential sways against undecided countries

### Bugfixes

- Fixed a crash related to IG support after civil wars
- Fixed a bug where a front could get stuck if it was in a state region shared between two countries and you were at war with both but one of them capitulated
- Fixed a bug where graphs displayed a flat line after 10 years
- Fixed two more cases where autonomous investment would insensibly spam the same building in the same location, one caused by incorrect evaluation of available workforce and the second caused by incorrect evaluation of already queued levels
- The Magnanimous Monarch journal entry will now invalidate if Portugal uses the "Restore Kingdom of Brazil" decision whilst it is active
- Fixed an issue preventing the Age of Caudillos journal entry from completing
- Fixed a bug where it was possible for insurrectionary IGs to join a party in government. They are now correctly blocked from doing so, but will not be kicked out of governing parties until the civil war starts.
- Fixed a bug where Regime Change could end up not actually changing the laws
- Fixed a bug where the revolutionary party would never disband in Single Party countries
- Fixed an issue where the expenses for buying Cuba weren't listed in the balance tooltip (Iberian Twilight)
- Fixed an issue for ‘Means of Independence’ where a modifier for Liberty Desire was at +20, reduced it to +0.2 (Iberian Twilight)
- Fixed some missing infamy calculations when targeting your own subjects with a war goal
- Spain and Carlist Spain are now properly immune to coups for the duration of the Carlist War
- Fixed an issue where Haiti would get Afro-Caribbean instead of Afro-Caribeño as a primary culture when completing the One and Indivisible Journal Entry (Iberian Twilight)
- Conservative victory in the Red Summer Journal Entry now fires "The Revolution Vanquished" event
- Fixed an issue where the dynastic coup decision would not have any effect if the monarch-to-be was already in the relevant country
- Succeeding into a personal union will no longer kill the country's sitting monarch
- Forming Iberia will no longer remove restore default clothing to Spanish and Portuguese pops and characters
- Jean/Juan III de Borbon may now spawn at the correct time, upon Henri de Borbon acceding to the French throne
- Fixed an issue with negotiations where the Lower Taxes pledge would break if you completed another pledge while it was active. Issue may still persist in affected saves.
- Fixed a bug when the army would return to the home HQ despite another front being nearby
- Fixed a bug where an annexed country could remove amendments in another one
- Fixed a bug where sometimes buildings were visually placed in the sea
- Fixed a crash that could occur when starting a game in ironman
- Fixed a bug where interest groups wanting to switch parties would sometimes become marginalized at the start of an election instead of joining their new party
- Fixed an issue that caused the "Secured Vital Port" modifier to not be applied properly in the "The Siege of Bilbao" event (Iberian Twilight)
- Central American countries will now properly gain the Age of Caudillos modifier
- Fixed an order-of-operations issue that granted the "The Most United Kingdom" achievement even if Brazil is to be couped (Iberian Twilight)
- Forming Iberia now conserves any cultures gained through the Status of the Vernacular (Iberian Twilight)
- The Portuguese culture now properly gains the Lusitanian tradition trait in the Pluricontinental event
- Historical Moroccan heirs spawn as heirs rather than rulers
- Fixed a bug where impossible amendments would appear in the negotiation events
- Fixed an issue where if a secession country would clear occupation of an invading force, it could cause errors to the control in the area making progress not possible anymore
- Fixed an issue where you could access a subject's sway offer panel even if they were not above 75 liberty desire
- Fixed a bug where a null object could stay in the construction queue when we had a construction in one country and the target state got conquered by a third party
- Fixed a bug where spawning a civil war in a country targeted by war would generate infamy
- Electoral Confidence now initializes slightly later, fixing an issue where newly-released democratic countries would start with 100% Electoral Confidence due to a divide-by-zero
- Fixed an issue in Abdication where the heir's scripted heir could succeed to the throne rather than the heir
- Fixed an issue that would prevent Portugal's ruler from becoming the Brazilian heir if the Amend Succession Laws Treaty Article was cancelled and reinstated
- Fixed an issue where the Além-mar Africano Journal Entry could fire for any country
- The Russian royal family will no longer wear infantrymen's coats after researching General Staff
- If Cuba is purchased and not annexed by the United States in the "The \[American\] Acquisition\" event, she will become a dominion rather than a protectorate (Iberian Twilight)
- Switching dynasties as France whilst the heir is a child will no longer create a permanent regency (Voice of the People)
- Fixed an issue that could lead to the "The Most United Kingdom" achievement being unlocked in the tick between Brazil becoming a personal union and it being couped by republicans (Iberian Twilight)
- Fixed very wide naval invasion planner popup appearing when you had several generals on defend order
- Fixed an issue where, when having the ruler selector game rule enabled, exiling characters on day one could spawn in unintended replacements
- If Cuba forms the Antillean Confederation while still a subject of Spain, the Independencia JE will correctly reference its new tag (Iberian Twilight)
- Fixed an issue with the Kaiserforum alternative color not lighting up during night
- Reduced flickering on Carlist Beret (Iberian Twilight)
- Added missing localization key for company regional HQ building group
- Fixed a bug where the last non-slave employees could be hired away from a building, leaving only slaves working there
- Fixed some modifiers not being properly cleared upon the end of the Carlist War
- Countries that have abolished elections will now lose modifiers that increase voting power
- Cultural movements may no longer discriminate against themselves in the "Thieves and Liars" event
- Fixed an edge-case where Negotiation could display a null amendment
- Fixed an incorrect event image in the "The Other Course" event for Austria
- Fixed an issue where the requirements for accepting cultures in the Status of the Vernacular referred to cultural acceptance rather than pop acceptance (Iberian Twilight)
- Option 3 in the La Siempre Fiel Isla de Cuba event now promotes Cuba to a Dominion
- Fixed a bug where conquering the capital could disable other global wargoals
- The Meiji Restoration will now clear the Shogun's regency
- Fixed an issue where you would lose access to the monument Journal Entries if there was a revolution in the relevant states
- Fixed a case in which using the "Restore the Kingdom of Brazil" decision could make Brazil an independent republic
- When a law is activated by an effect, such as in the case of abdication or resignation, any currently enacting law incompatible with the activated law will have its enactment canceled
- Fixed a scoping issue preventing Fascist characters from spawning
- Fixed a bug where the party to join could persist being shown in the government screen though the country doesn't have elections anymore
- Corrected loc keys in Technocracy JE and Medical Cleanliness event
- Fixed an issue that would cause the add_devastation effect to not show which state was affected
- Fixed an edge-case where an inappropriate country could get the Status of the Vernacular Journal Entry
- Fixed an issue where Leopold Kunschak was defined with an invalid ideology
- Fixed an issue where the Solitude event for Peru-Bolivia could attempt to switch Peru-Bolivia to an illegal tag
- The Great Eastern Crisis will no longer be visible to those without an interest in Anatolia, Danubia, or the Balkans
- Fixed an issue with the Torrent of Gin and Beer event where the same party could be identified as both the pro- and anti-prohibition party
- Fixed issue where again Bavarocracy JE would always make Otto psychologically afflicted
- Drastically reduced the population of Portuguese Senegal
- Switched the stances of the Carlist movement on Distribution of Power to match the Carlist leader ideology
- Peasant movements no longer count as being liberal
- Fixed the Intense to Relaxed transition for Songs of the Homeland Music (Songs of the Homeland)
- Fixed an Out of Sync in battles province weighting on Mac
- Fixed broken tooltip for add_contextless_journal_entry effect
- "The Provisional Government" and "The French Revolution" can no longer appear simultaneously
- Fixed an issue where female regents in a Sultanate could have no title
- Fixed several instances of duplicate fields in historical character templates
- Fixed an issue with oil related events that could result in a NULL_STATE if the state was transferred to a subject
- The "Magnanimous Monarch" Journal Entry will no longer get stuck if Pedro dies whilst the progress bar is at exactly 50% (Colossus of the South)
- The Philippines will now only use its war flag if either independent or in an independence war
- The "Nativist Labor Regulations" amendment will no longer benefit discriminated pops at the expense of fully accepted pops
- "Harka" modifiers are now correctly removed when the "Bilaad al-Siba" Journal Entry is finished or otherwise closed
- Fixed a misspelling in the description of the "One More Time" achievement (Iberian Twilight)
- Fixed a null scope in the goldrush.4 event
- Fixed a repeating error in The Opium Trade Journal Entry
- Fixed a spelling issue in the Jeffersonian ideology
- Removed a duplicate instance of Sándor Petőfi
- Fixed a typo in the Turanian Scourge event

## 1.12.3

Patch 1.12.3 was released on 2026-01-20[3] with checksum *8825*. Patch 1.12.3 was originally released as an opt-in beta on 2025-12-19[4].

### Improvements

- Upon researching Corporatism, the stances of the Carlist and Miguelist ideologies will change to support Agrarianism and Interventionism, and less intensely disapprove of non-Autocracy distribution of power laws
- The Two Spains Journal Entry may now be retained after forming Iberia as Spain
- Carlist, Miguelist, Legitimist, Catholic Fundamentalist, and Catholic Rights movements will now experienced increased Activism if their owner country has poor relations with the Papal States
- Reinstating the Basque Fueros as the Carlists will now add a Basque primary culture to Spain. Revoking this amendment will remove the primary culture.
- The "Ausgleich" event for Austria will no longer annex a player Transylvania without warning; rather, it will make Transylvania into a Hungarian subject
- The Spanish State Religion law at game start now has the State Anti-Clericalism amendment

### AI

- Fixed an issue where the AI would sometimes not deploy garrisons to fronts in adjacent HQs, even if failing to do so threatens the overall theater they are stationed in
- AI Liberal Spain will be now be much less willing to pursue the Reconquista

### Balance

- The Claim Greater Khorasan button for Persia will now add claims on Turkmenia and Merz
- When Interest Groups want to leave a party, they will no longer do so instantly but rather at the start of the next election, except in cases where their membership is no longer valid (for instance due to law restrictions)
- The traits of Interest Groups whose clout would make them marginalized will now only have half the effect if they remain Influential for non-clout reasons (such as being in a party)
- Interest Groups that are supported by less than 2% of the population and whose clout would make them marginal will now leave any party they are part of (and thus become properly marginal)
- The "The Good Mother" event for Portugal now typically fires in November of 1853, rather than January
- Moved the point at which Carlists and Miguelists become willing to participate in electoral politics from Political Agitation to Corporatism
- Removed negative tax revenue modifier from the Individual Redemption Payments amendment
- Pursuing the Reconquista of the New World as liberal Spain will now cost more infamy

### Content

- Added a new event and wargoal for Portugal to restore the Union with Brazil in the case of a Republican coup
- After completion of the Carlist War Journal Entry, we now also move the market capital to Madrid
- Added Antônio Carlos Ribeiro de Andrada as a starting Intelligentsia leader for Brazil

### Interface

- Goods expenses for construction is now split into private and government construction
- Fixed issue where UI was lying that goods from modifier (like the Carlist small arms) were available in market even though market access of state was zero
- Fixed issue where UI would list buy orders as sell orders in interface for goods from modifiers
- Building options in the production lens are now always fully alphabetically sorted
- Confirmation tooltips for actions that could cause a coup will now longer go off screen

### Bugfixes

- Fixed the infamy reduction for transfer money article enforcement that could result in 0 infamy against big nations (Thanks to player Gaspote)
- Fixed a bug when battles could be unable to start
- Fixed an issue where infamy values for Regime Change were calculated incorrectly, resulting in too low values
- Fixed an issue that caused several war goals to default to their infamy minimum value
- Fixed the Unstable Raj timer not updating upon Presidency Stability declining below 225
- Characters will no longer launch coups against law enactments that they support
- Fixed an issue where a coupist general could create a government with no Interest Groups
- Fixed a bug where the Revoke All Claims wargoal would be instantly invalidated, resulting in the wrong wargoal being used for secessions
- Fixed a bug where requirements for repealing amendments had disappeared.
- Emperor Pedro of Brazil now only starts the game as immortal if Colossus of the South is active
- Fixed a bug where agricultural buildings such as farms and ranches would not get cash reserves
- Fixed a bug where it was not possible to nationalize without compensation unless you had the money for compensation on hand
- Added trigger localization to the amendment_geheime_staatskonferenz amendment that was missing
- Fixed an issue that would cause the Modernisation Movement to pre-emptively switch ideologies, possibly locking AI countries into Peasant Levies
- Fixed an issue that led to the Yankee and Dixie cultures losing their Small Arms obsession upon the monthly tick
- Fixed a bug where adding a Liberate Country wargoal made the Conquer State wargoal unavailable even when not targeting conflicting states
- Fixed an issue where the ruling party would continually reform and disband under Single Party State
- Fixed a bug where Financial Districts and Manor Houses under Cooperative Ownership would pointlessly invest into foreign buildings that would then get collectivized
- Meiji Restoration events for Japan will no longer select Japan as the relevant foreign country
- Fixed a bug where buildings would sometimes try to pointlessly privatize themselves under conditions where they are able to self invest (such as Guild System)
- The "The Emperor's Regency" event for Brazil will now properly fire at game start
- Fixed a bug where unraised conscripts in a formation counted towards maximum manpower
- Fixed a possible NULL_OBJ in the Abdication and Resignation tooltip
- Fixed a crash during the disbanding of a company with a colonization charter
- Fixed a random crash when calculating a political strength of a pop
- Fixed a misplaced variable that could erroneously grant the Regeneration achievement if the Economic Regeneration journal entry timed out without making use of any creative accounting
- The Carlist Movement for Spain will no longer launch a second Carlist War whilst the first is still ongoing
- Fixed an issue where the african beard gene could get duplicated causing error spam and fps drop
- Fixed a bug where Treaty Port status would not get cleared correctly when a Treaty Port is annexed, leaving a state with 0% market access behind
- Fixed the abandon_revolution effect so that it properly removes targeted IG from a growing revolution
- Fixed a bug where sometimes the independence war goal wouldn't save in the game
- Timing out the "Bilaad al-Siba" Journal Entry for Morocco now removes the State of Anarchy state modifiers
- Fixed a bug where the cut down to size diplomatic demand was not possible to start through the interface
- Fixed a bug in the Carlist/Legitimist succession script which could spawn multiple clones of the same claimant, rather than a single claimant capable of inheriting both thrones
- Fix a bug where Trade Potential could sometimes incorrectly show up as a negative value when constructing Trade Centers
- Fixed a bug where the wrong alliances would be broken when declaring neutrality
- Fixed a bug where the election fraud event would not fire on the first election
- Added STATE_ENTRE_DOURO_E_MINHO, STATE_OLD_CASTILE and STATE_MURCIA to iberian_treaty_ports, requirements missing for The Western Protectorate achievement
- Fixed several events that couldn't fire due to incorrect trigger scopes
- Prevented the "Independence Day" event from briefly popping up as Cuba if the Carlists win the Carlist War
- Fixed a bug where oncreate effects for create_character could sometimes run twice
- Fixed an issue that caused Jose Rizal to be unable to spawn (Iberian Twilight)
- Fixed an issue where Pedro of Portugal could erroneously die if made the heir to Brazil in 1853
- Fixed an issue that caused stacking of multiple iterations of the "Setting Up Election System" modifier upon switching between Distribution of Power laws
- Fixed a bug where it was not possible to sign a renegotiated treaty if the can_ratify check failed for old, unamended articles, making it look like the AI was declining the renegotiation
- Fixed a misplaced adjacency line between Zulia and the Dutch Caribbean
- Fixed an issue in "The Status of the Vernacular", which incorrectly radicalised French pops for Spain
- Fixed a bug where having enacted/not having enacted NULL_OBJ could show up in law enactment tooltips due to checking against law groups that are not valid for the country (such as caste system)
- Fixed a bug where localization was missing in the map tooltip for diplomatic actions involving making subjects
- Fixed a bug where place holder text was shown to the player in the market panel
- Secessionist Interest Groups can no longer launch a coup
- Fixed a possible repeating error in military formation script

## 1.12.4

Patch 1.12.4 was released on 2026-01-29[5] with checksum *19ff*.

### Content

- Reverted the ability for Iberia to inherit the "The Old Empire" Journal Entry on account of requiring substantial changes to work properly, we will look into an appropriate solution for 1.13

### Bugfixes

- Fixed a save game crash caused by trying to show invalid revolution map objects, which could also result in corrupted save files
- Fixed an issue with Windows "Smart App Control" blocking game executable
- Infamy discount modifiers for diplomatic plays against unrecognized countries no longer apply for countries that are unrecognized themselves
- Fixed an issue where infamy from war goals was refunded twice in certain conditions when capitulating
- Fixed an issue where a war goal targeting a country would not be removed when that country switched sides in a diplomatic play
- Fixed a bug where some commanders didn't count their units towards Two Spains JE Liberal/Conservative progress

## 1.12.5

Patch 1.12.5 was released on 2026-03-12[6] with checksum *c274*.

### Content

- [Warships Bonus Pack](https://vic3.paradoxwikis.com/Warships_Bonus_Pack) content added

## References

1. ↑ Forum: [Hotfix 1.12.1 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1888125), 2025-12-12
2. ↑ Forum: [Victoria 3 – Dev Diary #172 – Seasons greetings & Hotfix 1.12.2](https://forum.paradoxplaza.com/forum/index.php?threads/1889676), 2025-12-18
3. ↑ Forum: [Hotfix 1.12.3 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1895957), 2026-01-20
4. ↑ Forum: [Victoria 3 | Opt in Beta 1.12.3](https://forum.paradoxplaza.com/forum/index.php?threads/1890213), 2025-12-19
5. ↑ Forum: [Hotfix 1.12.4 is now LIVE! - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1897870), 2026-01-29.
6. ↑ Forum: [Victoria 3 – Dev Diary #174 – The Great Wave & Volume 3](https://forum.paradoxplaza.com/forum/index.php?posts/31167189), 2026-03-12.
