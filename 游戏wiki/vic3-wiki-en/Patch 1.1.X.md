---
title: Patch 1.1.X
source: https://vic3.paradoxwikis.com/Patch_1.1.X
pageid: 3545
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
**Patch 1.1.X** are all patches beginning with 1.1.

## 1.1

Main article:
Patch 1.1

## 1.1.1

Patch 1.1.1 was released on 2022-12-08[1] with checksum *0455*.

### AI

- Fixed a bug where AI breaks off pacts to save Influence even when they're not the ones paying

### Localization

- Fixed a few unlocalized Russian custom loc strings (RU_CL...)

### Major Bugfixes

- Fixed a bug where the Capitalists, Shopkeepers and Bureaucrats had no default Interest Group attraction value, causing them to be Politically Inactive unless they worked in a Trade Center
- Fixed a bug that caused regressive political movements to be much more common than progressive ones
- Fixed a bug that caused Morale Loss to scale negatively with the number of troops in battle
- Fixed random crash on startup when reading in game data

## 1.1.2

Patch 1.1.2 was released on 2022-12-14[2] with checksum *4971*.

### Features

- Adds quick-select options for the three most Legitimate valid government combinations on the Reform Government panel

### Game Balance

- It is no longer possible to reliably max out Legitimacy by throwing every Interest Group in government together; Legitimacy penalty from conflicting Government ideologies is now calculated by determining, for each law group, the law (unlocked by tech) with the strongest compound feelings for or against it across all Interest Groups in government (even within the same party) ensuring every additional Interest Group potentially increases the total ideological incoherence
- Legitimacy penalty from size of government has been reintroduced, but in the form of a number of allowed Interest Groups or Parties in government with no penalty and a flat penalty for each entity in addition to that
- Legitimacy balance changes across Laws
- Angry Interest Groups can now be invited to the government, and will not leave the government voluntarily unless Insurrectionary
- Angry Interest Groups in government can now join Political Movements
- Insurrectionary Interest Groups in a government party will now leave the government and party, unless it is the last Interest Group in government
- Number of provinces won in smaller theaters with large numbers of defending mobilized Battalions is now reduced, ensuring they will take more battles to wipe out entirely

### AI

- Fixed bug that prevented the AI from sending their mobilized Generals to fronts under certain conditions
- Improved AI's ability to make smart investments in its port infrastructure in the mid- and late game
- Improved AI's ability to manage their total number of ports across a market region
- Increased AI priority for building ports in market areas that lack a port connection

### Bugfixes

- Ensured that overseas Generals will not travel to their home HQ if their front is resolved or invalidated. Generals whose front has been resolved or become invalid should now always travel to the closest active front to continue their campaign, even if this front is overseas. If no valid fronts exist, the General should remain on Stand By in the overseas HQ unless manually recalled home.
- Fixed a case of Generals skipping travel time and "teleporting" home if their source front's position is unknown
- Fixed issue where high Legitimacy Level would increase Radicals instead of Loyalists due to an outdated cache
- Fixed out-of-sync related to shipping lanes
- Fixed crash when running certain console commands, such as starting events through the console
- Fixed issue with flickering map names in culture panel
- Fixed missing market interaction texture
- Fixed two broken concept tooltips in Japanese localization and one in Polish localization

## References

1. ↑ [Victoria 3: Patch 1.1.1 is now LIVE!](https://forum.paradoxplaza.com/forum/index.php?threads/1561381)
2. ↑ [Victoria 3: Patch 1.1.2 is now LIVE!](https://forum.paradoxplaza.com/forum/index.php?threads/1562135)
