---
title: Victoria 3 to Hearts of Iron IV converter
source: https://vic3.paradoxwikis.com/Victoria_3_to_Hearts_of_Iron_IV_converter
pageid: 7391
categories: [Mods]
fetched: 2026-10-27
---
Game modification
: Victoria 3 to Hearts of Iron IV converter
Victoria 3 to Hearts of Iron IV converter
---

Type
Tool
---

Author(s)
Idhrendur
---

Status
Compatible with Vic3 1.10-1.11 and HoI4 1.16
---

Forum
Paradox Plaza Thread
Victoria 3 to Hearts of Iron IV converter
---

Type
Tool
---

Author(s)
Idhrendur
---

Status
Compatible with Vic3 1.10-1.11 and HoI4 1.16
---

Forum
Paradox Plaza Thread
The Vic3 to HoI4 converter is a [tool](https://vic3.paradoxwikis.com/Mods) that takes a Victoria 3 save and generates an HoI4 scenario from it. It can be downloaded from [this forum thread](https://forum.paradoxplaza.com/forum/index.php?threads/1475076). It is compatible with outputs from other converters, allowing the player to play a continuous *megacampaign* from [Imperator](https://imperator.paradoxwikis.com/) to [HoI4](http://hoi4.paradoxwikis.com/).

This is a continuation of the [Vic2 to HoI4 Converter project](http://hoi4.paradoxwikis.com/Victoria_2_to_Hearts_of_Iron_IV_converter).

## Versions

### Recent versions and changelogs

- 0.8 - [Halsey](https://forum.paradoxplaza.com/forum/index.php?posts/31203633)
- 0.7 - [de Gaulle](https://forum.paradoxplaza.com/forum/index.php?posts/30818490)
- 0.6 - [Fioravanzo](https://forum.paradoxplaza.com/forum/index.php?posts/30081735)
- 0.5 - [Eisenhower](https://forum.paradoxplaza.com/forum/index.php?posts/29884682)
- 0.4 - [Doorman](https://forum.paradoxplaza.com/forum/index.php?posts/29492477)
- 0.3 - [Chen](https://forum.paradoxplaza.com/forum/index.php?posts/29285130)
- 0.2 - [Blamey](https://forum.paradoxplaza.com/forum/index.php?posts/29165292)
- 0.1 - [Anders](https://forum.paradoxplaza.com/forum/index.php?posts/28891729)

## Features and conversion mechanics

Here is a general list of Converter capabilities and conversion mechanic explanations. For more information feel free to ask for clarifications on forums or take a peek at the code. **Note:** The converter includes a *configurables/* folder that contains all data files with rules it uses during conversion. These files are there for a reason - so the user can view them and modify them according to specific needs. Do not be shy to hack away and change them so the conversion fits expected goals.

#### Requirements

- Victoria 3, latest version. DLCs are optional.
- Hearts of Iron 4, latest version. DLCs are optional.

#### Incoming savegames

- Converter supports compressed save games.
- Ironman saves are supported.

#### Outgoing mod

- Converter will produce a Hearts of Iron 4 mod.
- On Windows, and using the front-end, the mod will be copied to Hoi4 mod/ directory.
- Without front-end (running the converter manually) or on other OS-es, mod will be exported to converter's output/ folder, and will have to be moved by user.

#### Bookmarks

- Converted mod supports one bookmark: 1936.
- Conversion-date bookmarks can be quite early, chaining converters from CK2 onward, one can play a 769 game in Hoi4 engine, though aside for the novelty that is a horrible idea.
- Converting earlier than 1936 will cause penalties in manpower levels, industrial footprint, and converted technologies, and is not recommended.

#### Countries

- Countries are converted in a basic fashion. They preserve their name, color, and leader.
- Governments are converted by determining ideological support for the various laws and applying this support to HoI4 ideologies using the rules in configurables/ideology_mappings.txt
- Technologies are converted according to configurables/tech_mappings.txt.
- Flags are converted by finding all flags in HoI4 and blank_mod/gfx/flags/ and applying them to countries that match the appropriate tag. Particular flags can be blocked by editing configuratbles/flag_mapper_config.txt.

#### States

- States are converted from Vic3's states, but islands and other disconnected provinces may be split into their own states. Wastelands are split into separate states.
- Resources are distributed according to configurables/resources.txt.
- Victory points are assigned to the highest-value significant province defined by Vic3. The point values are determined by the type of significant province.
- Manpower is simply the Vic3 population.
- Industry is converted as one factory per 175,000 sold goods value. If there are more than twelve factories in a state, they will be given to the owner's next state so that they don't go beyond HoI4's maximum.
- The smallest state category that can handle the number of converted factories is assigned.

#### Militaries

- Militaries are converted by turning Vic3 units into HoI4 battalions then using those battalions to fill out division templates.

#### Wars

- Wars are converted.
- Occupied territory is not converted.

#### Other mods

- The converter is designed to work with Vic3 mods, including games [converted from EU4 to Vic3](EU4 To Vic3 Converter.md). Other mods may also work.
- There may be future support for combining the converter's output with other HoI4 mods. But this will be a low priority, and currently this is completely untested.

## FAQ

Q: I used a mod, will the converter work with it? A: It depends on what the mod changed. Your best bet is to simply try (and let us know how it went). As far as we can tell, it does work well with games converted from EU4.

Q: The converter says "Saving Configuration: Failed!" How do I fix it? A: Disable your antivirus or allowlist the converter.

## Helping with development

If you wish to help with development, there are plenty of ways to do so. Descriptions of needs follow.

*Programmers:*

We can always use more programmers. The converter itself is in C++, and the tools that go with it are also in C++. Other converters are in C++, C#, Java, and Python.

*Map-staring experts*:

Province mappings always need more work. The order that HoI4 provinces are linked make a difference for where things like VPs end up, so if you can update province mappings (and send me the file) for areas you know, that'd be helpful.

*Testers:*

Catching bugs and oddities earlier means they get fixed earlier. I try to release test versions of the converter on the forum for testing, so running those and looking things over is helpful. And if you have professional experience in testing, well, I'm sure we could be doing things far better. Tell me how!

*Modders:*

We can always use help figuring out how things work, and how we can do them better. If you know how to mod HoI4, we can use your help figuring it out. As well, there's always more room for flavor events, decisions, and the like.

*Everyone:*

We can always handle more discussion on how things are converted over on the forum thread. And your encouragement helps more than you know.
