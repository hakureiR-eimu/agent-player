---
title: Patch 1.0.X
source: https://vic3.paradoxwikis.com/Patch_1.0.X
pageid: 3222
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
**Patch 1.0.X** are all patches beginning with 1.0.

## 1.0.3

1.0.3 was the release version, and as such had no changelog. The game was released on 2022-10-25.

## 1.0.4

Patch 1.0.4 was released on 2022-11-02[1] with the checksum *328c*.

### Game Balance

#### Economy

- Petit-Bourgeoisie now also care about government wages
- Slashing government wages will now reduce prestige
- Slashing military wages will now reduce training rate
- Debt slavery can now enslave pops up to wealth level 9, in reduced numbers for each point of wealth
- Reduce the max number of pops enslaved each week by debt slavery from 5% to 0.5% of state population
- Debt slavery will no longer enslave additional pops when slaves is 20% or more of the state population
- Tweak subsistence production in decentralized nations so African pops don't start at starvation levels

#### Politics

- Increased the chance of progressive political movements appearing over the course of the game
- Movements to Preserve now have a larger effect on the chance for a law to stall, making it harder to pass laws opposed by powerful groups
- Political Movements for or against changes in Slavery and Government principles laws will now be more radical
- Reduced base effect of Propagandists Intelligentsia trait from 50% to 25%
- Reduced effect of guaranteed liberties on loyalists and radicals growth

#### Colonization

- Native Uprisings now get a significant bonus to their combat capabilities, mainly on the defensive
- Reduced the chance of Native Uprisings occuring when provinces are colonized

### AI

#### Diplomacy

- AI is now a bit less likely to back down in diplomatic plays
- AI is now a bit more likely to get involved in diplomatic plays
- Make the AI more keen on swaying countries to its side if outmatched in a diplomatic play

#### War

- AI is now a lot more focused on taking land-adjacent states and conquering contiguous land areas in general
- Increase AI aggression against Unrecognized countries after unlocking Civilizing Mission

#### Colonization

- Increased AI tendency to get involved in Native Uprisings slightly

### Interface

#### Tooltips

- Improve revenue predictions when constructing buildings to show more accurate and useful data

### Bugfixes

- Flotillas now regain Morale as intended after naval battles
- Fixed a bug where capitulating in one war could cause your generals in another war to standby
- Added additional check to prevent monuments from being targeted in tutorial
- Added a check to the Declare Interest Tutorial that was miscounting the maximum amount of Declared Interests possible.
- Fix issue where Investment Pool could be used for disallowed building types
- Fix issue where predicted price for goods after goods substitution would sometimes show the wrong value
- Political movements can now start organizing a revolution at 50 radicalism rather than 100 (100 is needed for the revolution to actually begin though)
- Fixed typos in several defines
- Fix pop attraction reasons tooltip CTD in Asian languages
- Fixed a CTD caused by trying to create a shipping lane between two market areas with at least one of them being only nominally coastal due to the entire coast being impassable
- Fixed a CTD that could be triggered when clicking on the "mobilize all" button"
- Fixed late game CTD when transferring troops
- Fix CTD when hovering sell orders after having country join your market (__chkstk (chkstk.asm: 109))
- Fix CTD in NPdxParticle2Internal::SParticlePool::GetActive
- Fix CTD in CJominiSplineNetworkGraphics::GetStripLengthInternal

## 1.0.5

Patch 1.0.5 was released on 2022-11-04[2] with the checksum *a899*.

### Game Balance

- Changed so that Trade Centers cost 1 infrastructure per 10 levels instead of 1 infrastructure per level

## 1.0.6

Patch 1.0.6 was released on 2022-11-14[3] with the checksum *e384*.

### Game Balance

- Reduced the number of monthly radicals from political movements to enact and restore

### Performance

- Reduced the number of pops in the mid- to late-game by merging very small pops back into the general population
- Reduced the number of pops in the mid- to late-game by forcing unemployed pops to switch profession when sufficiently poor
- Improved performance of updating trends for political movements
- Improved performance of enumerating Liberation war goals

### AI

- Increased AI tendency to stick by its allies and subjects in conflicts
- Fixed AI acceptance for 'powerful protectors' factor to appear in virtually any alliance/customs union
- Fixed AI confidence and peace desire from gold reserves not being capped to 100% reserves
- Fixed AI incorrectly calculating how much an ongoing war or diplomatic play should add to their neutrality, making them abandon allies due to involvement in small conflicts
- Fixed AI involvement in a diplomatic play shown as an empty string in their neutrality calculation

### Bugfixes

- Fixed settings (such as in-game language) not being saved correctly when path contains non-latin characters
- Properly fixed flotillas not recovering morale
- Fixes "Pass a Law that enables an Institution" tutorial challenge being impossible to complete or writing to the error log under certain circumstances
- Fixed issue where a placated Political Movement might still trigger a revolution
- Fixed issue with American Territory Achievement using an incorrect trigger
- Fixed issue with not being able to get Berlin Conference Achievement
- Star Swarmed Banner no longer requires exactly 100 states exactly to get the achievement, but rather 100 or more
- Fixed issue with placeholder image being used for flamethrower event modifiers
- Fixed CTD in CPdxTerrain::CreateEffect
- Fixed CTD in CWarGoal::IsAdjacent
- Fixed CTD in CBuildingType destructor

## References

1. ↑ Forum, [Patch notes for 1.0.4](https://forum.paradoxplaza.com/forum/index.php?threads/1553580), written on 2022-11-01, but the notes and the patch were only published on 2022-11-02.
2. ↑ Steam, [Patch notes for 1.0.5](https://store.steampowered.com/news/app/529340/view/3407563246856257033), 2022-11-04.
3. ↑ Forum, [Patch notes for 1.0.6](https://forum.paradoxplaza.com/forum/index.php?threads/1557300), 2022-11-14
