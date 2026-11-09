---
title: Patch 1.3.X
source: https://vic3.paradoxwikis.com/Patch_1.3.X
pageid: 4968
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
**Patch 1.3.X** are all patches beginning with 1.3.

## 1.3

Main article:
Patch 1.3

## 1.3.1

Patch 1.3.1 was released on 2023-05-23[1] with checksum *302c*.

### Bugfixes

- Fixed an issue with new lines not working properly in the Chinese localization

## 1.3.2

Patch 1.3.2 was released on 2023-05-30[2] with checksum *4a4c*.

### Bugfixes

- Fixed an issue where Divided Monarchists events could keep firing even after reaching 100 progress
- Fixed an issue where events could give you a second Napoleon III after already having one Napoleon III
- Reduced the impact of Agitator Popularity on Political Movement Support
- Safeguards added to hopefully prevent an issue where some mods could cause buildings to get duplicated in split states
- The “Shut the Door Behind You” achievement no longer requires Voice of the People to unlock
- Fixed the Anarchist ideology having duplicated stances on Economic System laws
- Fixed a texture streaming issue that caused the border between the paper map and the table to look blurry when zoomed out
- The Vox Populi achievement should now work properly
- Fixed an issue where Agitators would sometimes not join the correct Political Movement
- Fixed an issue where agitator supported political movements could repeatedly form and disband
- Agitator support tooltip is now shown correctly for Agitators with 0 popularity
- Radicalism of revolutionary political movements is now shown correctly in the outliner
- Fixed a bug where civil wars could break the Divided Monarchists Journal Entry due to incorrectly setting a variable
- The Paris Commune now inherits the Journal Entries and variables of France if it ends up victorious and annexes France
- Fixed NULL_OBJ being shown in event ‘Pébrine Outbreak’
- Fixed a typo in the event ‘When You Have a Hammer’
- Fixed incorrectly formatted text in the event ‘Devout Call For Intervention’
- Fixed an issue where the German Unification chain of Journal Entries did not work correctly for Lübeck
- Fixed an issue where the Schleswig-Holstein Question Journal Entry would incorrectly resolve without taking Holstein
- Fixed an issue where the German National Identity Journal Entry could complete before the Schleswig-Holstein Question Journal Entry, potentially breaking the whole German Unification chain
- Fixed an issue where Max Stirner could end up spawning multiple times
- Fixed an issue where NULL_STATE entries could appear in the Construction Queue due to revolutions/secessions splitting states
- The AI now correctly understands how to resolve the Government Petition Journal Entry
- Fixed a localization issue with numerous triggers relating to unification where the name of the unification would not be shown
- Fixed an issue where some sound effects for free features such as Exile Agitator were incorrectly DLC locked
- Fixed an issue where exiling an Agitator would not remove their support from the Political Movement they were a part of
- Fixed a crash to desktop issue in the virtual file system
- It is no longer possible to colonize inland states that you do not border just because the state region they are a part of is coastal
- Fixed an issue where saving the game was blocked in certain languages when playing as a revolution due to country name formatting

## 1.3.3

Patch 1.3.3 was released on 2023-06-09[3] with checksum *66d6*.

### Bugfixes

- Fixed a crash caused by dead or foreign agitators supporting political movements that then break out into a revolution.

## 1.3.5

Patch 1.3.5 was released on 2023-06-26[4] with checksum *4986*. Patch 1.3.4 was released only as a beta[5]

### Voice of the People

These changes were made to the [Voice of the People](Voice of the People.md) DLC

#### Improvements

- Reworked the Divided Monarchists journal entry to improve depth and player involvement
- Added decision for France to purchase Luxembourg
- After France declares it natural borders, nations on their war path receive an event warning them of French aggression and adding a conscription modifier to relevant states
- Successful coups now cancel a law being enacted if they do not prefer it to the current one
- A socialist revolution in France will now lead to a Commune which starts as a Council Republic
- Adjusted the Cement the Rightful Dynasty journal entry to require maintaining legitimacy as said dynasty
- Lets the French player Sway any character other than rulers or heirs (including Generals, Admirals, and Agitators) to their dynastic ideology of choice
- Players will receive relevant information on the Garibaldi and Indochina events as they happen
- Enacting Monarchy as a republican France will now prompt the player to choose a historical candidate to enthrone

#### Interface

- Added notification when France declares its natural borders
- Improved usability of Divided Monarchy and Cementing the Rightful Dynasty Journal Entries
- Several triggers relating to Sway to French dynastic ideologies should now be much more legible
- All Algerian Journal Entry tooltips have been cleaned up and the requirements for The Algerian Departments Journal Entry will no longer reference Provence

#### Balance

- New Republican Unrest modifier on Divided Monarchy Journal Entry increases Radicals from low Legitimacy, decreases Loyalists from high Legitimacy, increases Legitimacy penalty for having mixed ideologies in government, and increases the Radicalism of Political Movements while the dynastic crisis is ongoing
- Increases difficulty and Approval penalties for preventing a coup by removing an Interest Group from government
- Reduces the Sway to dynastic Ideology cooldown from 5 years to 2 years
- Longer cooldowns to some events associated with Divided Monarchy

#### AI

- Adjusted French AI weights for default strategies and for individual admin, diplomatic and political strategies, dependent on dynastic control of France
- Legitimists and Bonapartists have additional weights towards having a Protect attitude towards the Papal States if it is a theocracy (i.e., they will want to protect the Pope more)
- Legitimists have an additional weight to Befriend Spain if Spain is a monarchy
- France is more likely to demand the relevant Algerian territory in a peace deal
- The French AI will more consistently strive to conquer Algeria, as long as the Conquest of Algeria Journal Entry is active.
- France is more likely to take an appropriate diplomatic stance (conquest) towards Algerian minors

#### Bugfixes

- Fixed a bug where many events from Voice of the People did not play sounds
- Ensures on_pulse events for Divided Monarchy won't continue while the dynasty is cementing its rule
- Garibaldi now becomes an agitator when exiled by event
- Removes the event option for Death of Charles X event that gives Legitimist progress while Cementing the Rightful Dynasty is active
- Fixed case where March on Versailles event can trigger twice
- Restrictions on french_pretenders_pulse.3 event trigger should now ensure the immediate effect always has a chance to save its scope
- All historical members of the d'Orleans dynasty are now properly tracked as being "orleanist_leaders" for the purpose of triggering events
- Removes superfluous cooldown on Death of Charles X event since it can only occur once regardless

### Base game

#### Improvements

- New character interaction to demobilize a general while still at war. Generals must have been mobilized for at least 6 months, and their mobilization cost will remain but decay for up to 4 months after they have been ordered to demobilize.
- Added the starting Journal Entry 'An Odious Debt' to Haiti, as well as associated events, dealing with the Haitian indemnity/debt crisis.
- Moved the decision for Haiti to cancel its French indemnities into the Journal Entry
- Unification plays now target all countries that hold states that are relevant for the unification, and are not supporters, allies or subjects of the initiator
- Unification plays will no longer target disqualified Unification candidates, but can target Great Powers, so Italian unification will tend to target Austria for Lombardy/Venetia and German unification will tend to target France for Alsace-Lorraine
- Unification plays now spawn individual wargoals for each relevant state instead of one umbrella wargoal
- When a unification play is launched, all unification supporters of the initiator are now annexed by them
- The opposing side in a unification play now gets a 'Cut Down to Size' wargoal against the initiator
- Active Interest Group Traits will no longer deactivate until Approval is sufficiently different from the cutoff, to make them more sticky and prevent notification spam
- Petitions should no longer trigger while a law is enacted that the government already likes
- Added flag canton definitions for Germany, the Dutch East Indies, and the Paris Commune

#### Interface

- Add the Political Movement an Agitator is supporting or will start/join when invited to the character panel.
- Added a toast notification when an agitator appears in the player's country
- Exiled characters now send notification to all diplomatically relevant countries
- Added important action to alert when characters can be demobilized early
- Countries are now notified when a claim is gained in a region they have land in
- Make an Exiles notification group and add it to the Message Settings.
- Infrastructure derived from the population of a state now displays its cap properly in the tooltip
- Character Interactions now display their cooldown time without having to go into the tooltip
- Fixed an issue with revolution animations in the outliner.
- Added 2 missing modifier icons
- Low Training Rate alert at war now triggers based on actual negative training rate modifier and not the military budget level itself
- Add empty states in the tooltips for State Infrastructure and Usage

#### Balance

- Agitator Popularity now amplifies existing Support of Political Movements rather than generate Support from scratch
- Significantly improved the Industry Banned law. Halved tech penalties and made them exclusive to Production tech. Added 50% private construction allocation. Added 10% agriculture throughput in all states. Added -10% expected SoL for all pops
- Reduced army training rate to 20 per level for all PMs, except 10 for Irregular
- Reduced demand for Fine Art, especially by richer pops
- Increased demand for Services, especially by richer pops
- Fixes a typo in pop needs script that made Services much less substitutable for Fine Art than intended
- The reduced impact of the Petition Journal Entry timing out if you're already in the process of enacting the law is now scaled by how far you've gotten; no reduction if still at the initial phase, -5 Approval reduction in the second phase, and -10 Approval reduction in the third phase

#### Performance

- Optimization of building particle graphics
- Scales pop consolidation parameters by the current number of pops in the world, which could help late game performance
- Added a Game Rule to let you control what degree of pop consolidation you want

#### Modding

- Journal Entries now support modifiers, which propagate to their countries while active
- Adds prefers_law trigger (returns if a character or interest group prefers one law over another)
- Interest Groups can now be given unique Traits per country, both at startup and during play, using the set_ig_trait effect
- Adds currently_active_law_in_group event target link (from one law to currently active law in same group)
- Modifier types for Radicals/Loyalist gain at low/high Legitimacy added
- Added on_actions for on_mobilized_general and on_demobilized_general
- Added demobilize effect for character scopes
- Added mobilization_cost compare trigger for character scopes
- Journal Entry database types now have modifiers_while_active functionality to specify modifiers to automatically apply on activation
- New direct link ig_trait implemented

#### Bugfixes

- Fixed a bug that caused newly released countries to not have any Journal Entries
- Fix a bug where released countries would always take the state religion of the releaser, instead of this only being the case for revolutions as intended
- Fixed a bug that prevented secessions that can't progress above 0% from disbanding
- Fixed CTD when switching the graphics settings in the main menu after returning to it from the game
- Liberate Country wargoals are now only mutually exclusive if they have conflicting released states
- Autocracies will now properly transition into single-party states
- Agitators exiled by AI should now always end up in the Exile pool
- Fixed a bug where movements could in rare cases become revolutionary without any Interest Group support
- Fixed hidden map objects exposing themselves after changing the graphics settings in the main menu
- Coups are no longer inheritable by revolutionary countries
- Fixed a bug in the prediction of which political movement exiles would start, causing it to incorrectly say they wouldn't start a movement.
- Fixed a bug that caused revolutionary political movements to stay revolutionary when their radicalism dropped. Revolutionary movements whose radicalism drops too low are now turned back into regular political movements.
- Springtime of the People Journal Entry is no longer inheritable by revolutionary countries
- Agitators now leave political movements when given roles incompatible with the agitator character role.
- Fixed scope error in In the Hands of the State and Agitator events
- The leaders of French republics will now properly be called the President
- Submarines and Carriers now have a per-level training rate penalty instead of unscaled
- Make the tooltip for Law Enactment say that there is a chance the Law will pass on the next checkpoint when on the last phase
- Added a check to Expand Building Tutorial to ensure the building selected can actually be expanded
- Head of States in Parliamentary Republics are now selected based on their Interest Group's Clout (including Voting Power) rather than raw Political Strength
- Fixed case where Officer and a Gentleman event could target a character who had not been sent away
- Fixed an edge case in government petitions which could cause error log spam
- Fixed an issue where exiles events would cause error log spam
- Error log no longer spams with [RandomizableValueFloat.GetValue] while in MP
- John French can now be recruited as a General starting only in the year he begun his military career, not as a tiny baby

## 1.3.6

Patch 1.3.6 was released on 2023-06-29[6] with checksum *1ff8*.

### Bugfixes

- Overlord will no longer annex the rebellious states from subjects after the civil war
- Countries that don't exist can no longer start uprisings
- Divided Monarchies no longer stalls and fails to transition into the next phase if more than 1 dynasty reaches 360 Progress at the same time
- It is no longer possible to queue agriculture buildings over the Arable Land limit
- Countries about to get annexed no longer get Claims (and trigger notifications for those Claims) for each state annexed
- Belle Époque achievement description now correctly states that you need the highest Innovation and GDP generation in the world, not GDP per capita
- [Turkish] Shortcut button tooltips no longer show long strings of script

### Balance

- Fine Art can no longer be fully substituted by purchasing Services instead

## References

1. ↑ [Victoria 3: Update 1.3 + Hotfix 1.3.1 is now LIVE! Checksum [302c] Updated May 23rd](https://forum.paradoxplaza.com/forum/index.php?threads/1586208)
2. ↑ [Victoria 3: Patch 1.3.2 is now LIVE! - Checksum [4a4c]](https://forum.paradoxplaza.com/forum/index.php?threads/1587760)
3. ↑ [Victoria 3: Hotfix 1.3.3 is now LIVE! - Checksum [66d6] - Not for Problem Reports!](https://forum.paradoxplaza.com/forum/index.php?threads/1589410)
4. ↑ [Victoria 3: Patch 1.3.5 is now LIVE! - Checksum [4986]](https://forum.paradoxplaza.com/forum/index.php?threads/1591803)
5. ↑ [Victoria 3: 1.3.4 Live Test Steam Beta Branch](https://forum.paradoxplaza.com/forum/index.php?threads/1591173)
6. ↑ [Victoria 3: Hotfix 1.3.6 is now LIVE! - Checksum [1ff8]](https://forum.paradoxplaza.com/forum/index.php?threads/1592184)
