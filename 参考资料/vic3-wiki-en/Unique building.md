---
title: Unique building
source: https://vic3.paradoxwikis.com/Unique_building
pageid: 3834
categories: [1.13, Pages_with_interwiki_links_to_Wikipedia, Pages_with_obsolete_template_parameters, Game_concepts, Economy]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

Economy
Buildings
List of buildings
•
Unique buildings
Companies
•
Flavored companies
Market
Goods
•
Needs
Production methods
List of production methods
Treasury
**Unique buildings** are special [buildings](Building.md) with only a single level and most are buildable only in specific states. Unique buildings typically have special effects and cost much more to construct than standard buildings. Unique buildings cannot be downsized or deleted. All unique buildings are government-funded.

## Canals

**Canals** are buildable unique buildings which connect certain sea nodes. There are three potential canals: Suez, Panama, and Kiel. Building the Suez or Panama canal requires surveying the isthmus and acquiring the state or at least the treaty port, while the Kiel Canal only requires researching the required technology and owning the entire state of Schleswig-Holstein.

Each canal costs 5000 construction and provides 100 urbanization. Canals have only a single production method, with the employment, input, and output listed in the table below. The primary benefit of each canal is the connection of sea nodes across their isthmus, which does not require the canal to be staffed. These connections greatly shorten the length of shipping lines for routes which can use them, thereby saving on convoys. Once either canal is built, all countries gain the benefit of the new connection, regardless of their relationship with the owner of the canal.

| Name | Required technology | Employees | Input | Output | State (Initial owner) |
|---|---|---|---|---|---|
| Panama Canal | [Civilizing Mission](Society technology.md) | +2000 Clerks +2500 Machinists +500 Bureaucrats | +10 Tools +15 Coal | +100 Prestige +20% Local migration attraction | Panama ( Colombia ) |
| Suez Canal | [Colonization](Society technology.md) | +2000 Clerks +2500 Machinists +500 Bureaucrats | +10 Tools +15 Coal | +100 Prestige +20% Local migration attraction | Sinai ( Egypt ) |
| Kiel Canal | [Ironclad](Military technology.md) | +2000 Clerks +2500 Machinists +500 Bureaucrats | +10 Tools +15 Coal | +100 Prestige +20% Local migration attraction | Schleswig-Holstein (Split between Holstein , Lübeck , and Schleswig ) |

The Suez and Panama canals each unlock an associated [company](Companies.md) which boosts Trade Centers, Ports, and potentially Shipyards.

| Name[wp 1] / Ownership | Buildings | Industry charters | Prestige goods | Prosperity bonus | Requirements |
|---|---|---|---|---|---|
| [Panama Canal Company](http://en.wikipedia.org/wiki/Panama_Canal_Company) Partial Bureaucrat | Port Trade Center | Shipyards | Swift Merchant Marine | +1 Free company charters +50,000 Tax Income +25% Trade advantage | Owns Panama with the Panama Canal at 50% employment Owns any state with 5 levels of Trade Center or Port |
| [Suez Canal Company](http://en.wikipedia.org/wiki/Suez_Canal_Company) Partial Bureaucrat | Port Trade Center | Shipyards | Swift Merchant Marine | +1 Free company charters +50,000 Tax Income +25% Trade advantage | Owns Sinai with the Suez Canal building at 50% employment Owns any state with 5 levels of Trade Center or Port |

### Canal scripted content

There is a series of decisions, events, and journal entries related to the Suez and Panama canals. The Kiel Canal has no associated scripted content; it can be built as soon as its technology is researched and its state is fully owned.

id
Survey the Suez Isthmus
Authorize a survey to map the potential of building a canal in across the Suez Isthmus
---

| Shown conditions: Has an interest in the Nile region Is not surveying the Suez isthmus No country has built and staffed the Suez Canal Is a Great Power or owns the state of Sinai | Useable conditions: Has researched Colonization Produces over 1000 bureaucracy |
|---|---|
| Effects: Adds the modifier Surveying Suez Isthmus Surveying Suez Isthmus Country modifier −1000 Bureaucracy Activates journal entry The Suez Survey |  |

id
The Suez Survey
Our engineers believe it may be possible to construct a canal linking the Mediterranean to the Red Sea. They are currently conducting a survey of the Isthmus of Suez to determine the feasibility of the project.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Decision Survey the Suez Isthmus | Effects when activated: None |
| Completion conditions: Entry is active for 18 months | Effects when completed: Remove modifier Surveying Suez Isthmus Surveying Suez Isthmus Country modifier −1000 Bureaucracy Trigger event Suez Isthmus Surveyed |
| Invalidation conditions: Is not surveying the Suez isthmus OR Another country has built and staffed the Suez Canal | Effects when invalid: Remove modifier Surveying Suez Isthmus Surveying Suez Isthmus Country modifier −1000 Bureaucracy |

id
Suez Isthmus Surveyed
Our survey of the Suez Isthmus is complete: it would be possible to construct a canal linking the Mediterranean to the Red Sea. Next we must acquire the land from [Sinai owner].
---

Flavor text:
"There has been a long held belief that the water levels on either side of the Suez Isthmus differed greatly. We have now proven that is not the case."
---

| Is triggered by: Journal entry The Suez Survey completion |
|---|
| Trigger conditions: None |
| Option conditions Enabled if: Does not own any part of Sinai We will make a suitable offer. Gain +10 relations with the owner of Sinai Enables decision Acquire Land in the Sinai Enabled if: Does not own any part of Sinai Coercion is the simplest form of persuasion. Gain a claim on Sinai Lose −20 relations with the owner of Sinai Enables decision Acquire Land in the Sinai Enabled if: Owns any part of Sinai We will build the Canal! No effect For all options: Activate journal entry Construct the Suez Canal |

id
Acquire Land in the Sinai
Initiate talks to discuss the possiblity of acquiring land in the Sinai to begin construction of a canal.
---

| Shown conditions: Unlocked decision in event Suez Isthmus Surveyed No country has purchased the Sinai treaty port No country has built the Suez Canal The owner of the Sinai treaty port has not completed The Suez Survey | Useable conditions: GDP is over £50M Has cordial or better with the owner of the Sinai treaty port |
|---|---|
| Effects: If owner of the Sinai treaty port is AI: That country gains modifier The Suez Sale The Suez Sale Country modifier +30000 Tax income for 10 years Gain ownership of the Sinai treaty port Gain modifier The Suez Purchase The Suez Purchase Country modifier +30000 Government expense for 10 years Else triggers event Request Land in Sinai |  |

id
Survey the Panama Isthmus
Authorize a survey to map the potential of building a canal in across the Panama Isthmus
---

| Shown conditions: Has an interest in the Central America region Is not surveying the Panama isthmus No country has built and staffed the Panama Canal Is a Great Power or owns the state of Panama | Useable conditions: Has researched Civilizing Mission Produces over 1000 bureaucracy |
|---|---|
| Effects: Adds the modifier Surveying Panama Isthmus Surveying Panama Isthmus Country modifier −1000 Bureaucracy Activates journal entry The Panama Survey |  |

id
The Panama Survey
Our engineers believe it may be possible to construct a canal linking the Atlantic and Pacific Oceans. They are currently conducting a survey of the Isthmus of Panama to determine the feasibility of the project.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Decision Survey the Panama Isthmus | Effects when activated: None |
| Completion conditions: Entry is active for 12 months | Effects when completed: Remove modifier Surveying Panama Isthmus Surveying Panama Isthmus Country modifier −1000 Bureaucracy Trigger event Panama Isthmus Surveyed |
| Invalidation conditions: Is not surveying the Panama isthmus OR Another country has built and staffed the Panama Canal | Effects when invalid: Remove modifier Surveying Panama Isthmus Surveying Panama Isthmus Country modifier −1000 Bureaucracy |

id
Panama Isthmus Surveyed
Our survey of the Panama Isthmus is complete. We have confirmed that it would be possible to construct a canal linking the Atlantic and Pacific Oceans. Next we must acquire the land from [Panama owner].
---

Flavor text:
"A faster route between the Atlantic and Pacific has long been sought, but now we shall make it ourselves."
---

| Is triggered by: Journal entry The Panama Survey completion |
|---|
| Trigger conditions: None |
| Option conditions Enabled if: Does not own any part of Panama We will make a suitable offer. Gain +10 relations with the owner of Panama Enables decision Acquire Land in Panama Enabled if: Does not own any part of Panama Coercion is the simplest form of persuasion. Gain a claim on Panama Lose −20 relations with the owner of Panama Enables decision Acquire Land in Panama Enabled if: Owns any part of Panama We will build the Canal! No effect For all options: Activate journal entry Construct the Panama Canal |

id
Acquire Land in Panama
Begin discussions regarding the possibility of acquiring land in Panama to begin construction of a canal.
---

| Shown conditions: Unlocked decision in event Panama Isthmus Surveyed No country has purchased the Panama treaty port No country has built the Panama Canal The owner of the Panama treaty port has not completed The Panama Survey | Useable conditions: GDP is over £50M Has cordial or better with the owner of the Panama treaty port |
|---|---|
| Effects: If owner of the Panama treaty port is AI: That country gains modifier The Panama Sale The Panama Sale Country modifier +30000 Tax income for 10 years Gain ownership of the Panama treaty port Gain modifier The Panama Purchase The Panama Purchase Country modifier +30000 Government expense for 10 years Else triggers event Request for a Land in Panama |  |

## Monuments

**Monuments** are unique buildings only available in specific states, each with its own 3D model on the map. Unlike most buildings, monuments do not output any goods, but instead they output national or local modifiers, including [capacities](https://vic3.paradoxwikis.com/Capacities) or effects on pops or buildings. The Vatican City, for instance, outputs Influence and Authority as well as increasing the political strength of the Devout interest group.

All monuments provide 20 urbanization and use 1 infrastructure. While most monuments are present at the start date, some, like the Eiffel Tower, must be constructed.

Monuments have only a single [production method](Production method.md) which cannot be manually switched. It is possible to turn off the effects of monuments via the [game rules](https://vic3.paradoxwikis.com/Game_rules) before starting a game, in which case they have only a cosmetic effect or provide a flat **25** prestige without hiring any pops.

The employees and output listed below assumes the game rule *Monument Effects* is set to *Enabled*.

### Starting monuments

The following monuments all exist at the start of the game.

| Name | Employees | Output | State (Initial owner) |
|---|---|---|---|
| Angkor Wat | +500 Clergymen | +25% Devout political strength +25 Prestige | Cambodia ( Cambodia ) |
| Forbidden City | +800 Bureaucrats +200 Clergymen | +20 Legitimacy from including the Head of State in Government +50 Authority +25 Prestige | Beijing ( China ) |
| Hagia Sophia | +200 Clergymen | +10% Devout pop attraction +25 Prestige | Eastern Thrace ( Ottoman Empire ) |
| Saint Basils Cathedral | +200 Clergymen | +10% Devout political strength +25 Prestige | Moscow ( Russia ) |
| Taj Mahal | +100 Bureaucrats | **+25** Prestige | Rajputana [1] ( East India ) |
| Vatican City | +500 Clergymen | If owner's state religion is Catholic: +25% Devout political strength +100 Influence +100 Authority | Lazio ( Papal States ) |
| — | If owner's state religion is not Catholic: +25 Prestige |  |  |
| White House | +500 Bureaucrats | **+20%** Local Government Administration throughput | District of Columbia ( USA ) |

### Buildable monuments

The following monuments do not exist at the start of the game but can be built at a cost of 2500 construction.

| Name | Requirements | Employees | Output | State (Initial owner) |
|---|---|---|---|---|
| Atocha Railway Station | Iberian Twilight DLC Steel-Frame Buildings | +200 Laborers +200 Machinists +100 Clerks | +50 Prestige +20% Railway throughput | New Castile ( Spain ) |
| Big Ben | — | +100 Machinists | +50 Prestige +1% Local building throughput | Home Counties ( Great Britain ) |
| Cristo Redentor | Pneumatic Tools State Atheism | +100 Clergymen | +50 Prestige +15% Devout political strength | Rio de Janeiro ( Brazil ) |
| Grand Theater of Havana | Iberian Twilight DLC Pneumatic Tools | +200 Academics | +10.0 Paper +5.0 Fine Art +25 Prestige | Western Cuba ( Cuba ) |
| Manila Cathedral | Iberian Twilight DLC | +100 Clergymen | +10% Devout political strength +25 Prestige | Luzón ( Philippines ) |
| Mosque of Djenne | — | +500 Clergymen | +10% Devout political strength +20% Local education access | Eastern Mali ( Massina ) |
| Statue of Liberty | [Steel-Frame Buildings](Society technology.md) | +100 Bureaucrats | +75 Prestige +25% Migration attraction | New York ( USA ) |
| The Eiffel Tower | Steel-Frame Buildings | +100 Machinists | **+100** Prestige | Île-de-France ( France ) |
| Victoria Terminus | Steel-Frame Buildings | +200 Laborers +200 Machinists +100 Clerks | +50 Prestige +20% Railway throughput | Bombay ( East India ) |
| Kaiserforum Built in multiple stages via a dedicated journal entry. | National Awakening DLC Reinforced Concrete | +100 Aristocrats +100 Academics +200 Bureaucrats | +25 Prestige +5 Legitimacy from including the Head of State in Government +50% Local migration attraction +20% Local Government Administration throughput [2] | Austria ( Austria ) |
| Sagrada Família Cathedral Built in multiple stages via a dedicated journal entry. | Iberian Twilight DLC Reinforced Concrete Pneumatic Tools | +400 Clergymen | +50 Prestige +10% Devout political strength | Catalonia ( Spain ) |
| Pena Palace | Iberian Twilight DLC Mechanical Tools | +100 Aristocrats +200 Bureaucrats | +25 Prestige +5 Legitimacy from including the Head of State in Government | Estremadura ( Portugal ) |

### Cosmetic monuments

There are a number of monuments that, regardless of settings, are always only cosmetic. All of the following are present at the start of the game.[wp 1]

- [Arg-e Bam](http://en.wikipedia.org/wiki/Arg-e_Bam) (Kerman)
- [Chichen Itza](http://en.wikipedia.org/wiki/Chichen_Itza) (Yucatán)
- [Easter Island Heads](http://en.wikipedia.org/wiki/Easter_Island_Heads) (Tahiti)
- [Eye of Sahara](http://en.wikipedia.org/wiki/Eye_of_Sahara) (Mauritania)
- [Giza Necropolis](http://en.wikipedia.org/wiki/Giza_Necropolis) (Lower Egypt)
- [Great Wall of China](http://en.wikipedia.org/wiki/Great_Wall_of_China) (North China region)
- [Khaju Bridge](http://en.wikipedia.org/wiki/Khaju_Bridge) (Isfahan)
- [Machu Picchu](http://en.wikipedia.org/wiki/Machu_Picchu) (Ica)
- [Petra](http://en.wikipedia.org/wiki/Petra) (Transjordan)
- ([AB](Downloadable content.md)) [Capitol Hill](http://en.wikipedia.org/wiki/United_States_Capitol) (District of Columbia)
- ([AB](Downloadable content.md)) [Central Park](http://en.wikipedia.org/wiki/Central_Park) (New York)
- [Greenwich Observatory](http://en.wikipedia.org/wiki/Greenwich_Observatory) (Home Counties)
- [Martand Sun Temple](http://en.wikipedia.org/wiki/Martand_Sun_Temple) (Kashmir)
- [Temple of Poseidon](http://en.wikipedia.org/wiki/Temple_of_Poseidon,_Sounion) (Attica)
- [Wat Arun](http://en.wikipedia.org/wiki/Wat_Arun) (Bangkok)

Additionally, the following cosmetic monument may appear by event when [fantastical content](Game rule.md) is turned on.

- [Castle Dracula](http://en.wikipedia.org/wiki/Castle_Dracula) (Northern Transylvania)

## Skyscrapers

**Skyscrapers** are buildable unique buildings that provide a boost to either Government Administration throughput or trade route volume. Unlike monuments and canals, each country can potentially build a single skyscraper. Skyscrapers cost 2500 construction to build, provide 20 urbanization, and use 1 infrastructure.

| Name | Required technology |  |  |  |
|---|---|---|---|---|
| Skyscraper | Steel-Frame Buildings Reinforced Concrete |  |  |  |
| PM Group | Production method | Employees | Input | Output |
| Skyscraper | Bureaucratic Nexus | +200 Laborers +500 Clerks +300 Bureaucrats | +25 Paper | **+25%** Local Government Administration throughput |
| Trade Nexus | +25% Trade route volume +25% Trade Advantage |  |  |  |
| Airships | No Airships | — | — | — |
| Airship Mooring Post | **+10** Prestige |  |  |  |

If a country acquires a state with a skyscraper, it cannot build a second one. However, if it has already built a skyscraper, it keeps any others gained.

### Skyscraper scripted content

There is a series of decisions, events, and journal entries related to building a skyscraper.

id
Survey a Skyscraper Site
Our architects believe that innovations involving steel frames and concrete would allow the construction of buildings taller than ever conceived before. They urge us to authorize a survey to identify the best possible site to lay the foundations.
---

| Shown conditions: Has researched Steel-Frame Buildings Has researched Reinforced Concrete Does not own any Skyscrapers Is not surveying for or building a skyscraper | Useable conditions: Fully owns an incorporated state with 20 or more levels of Urban Center Produces over 500 bureaucracy |
|---|---|
| Effects: Adds the modifier Skyscraper Survey Skyscraper Survey Country modifier −500 Bureaucracy for 2 years Activates journal entry Skyscraper Survey |  |

id
Skyscraper Survey
Our architects believe that innovations involving steel frames and concrete would allow the construction of buildings taller than ever conceived before. We have authorized a survey to identify the best possible site to lay the foundations.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Decision Survey a Skyscraper Site | Effects when activated: None |
| Completion conditions: Entry is active for 24 months Fully owns an incorporated state with 20 or more levels of Urban Center | Effects when completed: Remove modifier Skyscraper Survey Skyscraper Survey Country modifier −500 Bureaucracy Trigger event Skyscraper Site Identified |
| Invalidation conditions: Does not fully own an incorporated state with 20 or more levels of Urban Center | Effects when invalid: Remove modifier Skyscraper Survey Skyscraper Survey Country modifier −500 Bureaucracy |

id
Skyscraper Site Identified
Our architects and engineers have identified [City] in [State] as the optimal site to begin construction of a Skyscraper.
---

Flavor text:
"Gentlemen, we are going to erect the tallest building in the world. The foundation alone will need hundreds of men, more if they will not work twelve hour shifts. Every day we will need to transport thousands of bags of cement into the heart of a metropolis. We must secure an immense quantity of steel that must, like Atlas, hold the weight of a whole world. The task ahead of us is monumental."
---

| Is triggered by: Journal entry Skyscraper Survey completion |
|---|
| Trigger conditions: None |
| Immediate effects: A random fully owned incorporated state with 20 or more levels of Urban Center is selected as the skyscraper site, preferring the capital state. |
| We will make a suitable offer. The selected state gains the modifier Skyscraper Construction Site Skyscraper Construction Site State modifier +10% Construction Sector throughput Activates journal entry Construct a Skyscraper , with the selected state as its target |

id
Construct a Skyscraper
Having identified the optimal site for our skyscraper, we must set about the monumental task of its construction. When it is completed we expect this structure to be among the tallest in all the world.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Event Skyscraper Site Identified | Effects when activated: None |
| Completion conditions: The target state has a fully-constructed Skyscraper | Effects when completed: Target state loses modifier Skyscraper Construction Site Skyscraper Construction Site State modifier +10% Construction Sector throughput Trigger event Touching the Sky |
| Failure conditions: No owned state has the modifier Skyscraper Construction Site | Effects when failed: None |

id
Touching the Sky
Construction of the [City] Skyscraper in [State] is complete. Dominating the skyline, it inspires all who gaze upon it.
---

Flavor text:
"My skyscraper would not have been possible without the hard work and grit of the thousands of people who dedicated themselves to its construction. Of course as Chief Architect I had perhaps more impact than most. One might even say the lion's share of the credit is mine. In fact, this pinnacle of human achievement, this new Babel, was borne entirely from the machinations of my mind. Look upon my works all ye mighty, and despair!"
---

| Is triggered by: Journal entry Construct a Skyscraper completion |
|---|
| Trigger conditions: None |
| Option conditions Enabled if: Another country built the first skyscraper A magnificent achievement. Gain the modifier Touching the Sky Touching the Sky Country modifier +25 Prestige for 5 years Enabled if: This country built the first skyscraper [Country Adjective] architecture is second to none. Gain the modifier Touching the Sky Touching the Sky Country modifier +25 Prestige for 5 years Gain the modifier Architectural Pioneering Architectural Pioneering Country modifier +50 Prestige for 5 years |

## Power bloc statues

|  | Available only with the [Sphere of Influence](Sphere of Influence.md) DLC enabled. |
|---|---|

Members of [power blocs](Power bloc.md) can build *power bloc statues*, up to one level in each state at a cost of 2500 construction. Each central identity has a different effect for the statue if the game rule for monument effects is turned on. This effect automatically changes according to the owner's power bloc identity. If an empire not in a power bloc conquers the state, or the [game rule](Game rule.md) for monument effects is set to prestige only, power bloc statues provide **+3** prestige with no workforce. A power bloc statue provides 20 urbanization and uses 1 infrastructure.

| Central identity | Employees | Output |
|---|---|---|
| Ideological Union | +500 Bureaucrats | +3 Prestige +5 Influence +25% Local pop political strength |
| Military Treaty | +500 Servicemen | +3 Prestige +25% Local conscriptable battalions |
| Religious Convocation | +500 Clergymen | +3 Prestige +25% Local conversion −10% Effects from turmoil |
| Sovereign Empire | +500 Bureaucrats | +3 Prestige −25% Local decree cost |
| Trade League | +500 Clerks | +3 Prestige +10% Loyalists from movements +10% Infrastructure from population |

## References

1. ↑ The building's starting placement is scripted in Agra, but its buildable region restricts it to Rajputana.
2. ↑ Only for the penultimate stage of the monument, before the final *Kaisergelb* branch.

---

Wikipedia link references:

1. ↑ 1.0 1.1 Links to English Wikipedia article

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | [Government](Government.md) • [Capacities](Capacity.md) • [Characters](Character.md) • [Decrees](Decrees.md) • [Institutions](Institutions.md) • [Laws](Laws.md) • [Technology](Technology.md) |
|---|---|

| Politics | [Elections](Elections.md) • [Ideology](Ideology.md) • [Interest group](Interest group.md) • [Political lobby](Political lobby.md) • [Political movement](Political movement.md) • [Political party](Political party.md) • [Revolution](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| Economy | [Buildings](Building.md) • [Goods](Goods.md) • [Harvest condition](Harvest condition.md) • [Infrastructure](Infrastructure.md) • [Market](Market.md) • [Production methods](https://vic3.paradoxwikis.com/Production_methods) • [State](State.md) • [Treasury](Treasury.md) |
|---|---|

| Diplomacy | [Diplomacy](Diplomacy.md) • [Diplomatic action](https://vic3.paradoxwikis.com/Diplomatic_action) • [Diplomatic play](Diplomatic play.md) • [Power bloc](Power bloc.md) • [Ranks](Rank.md) • [Subjects](Subject.md) • [Treaties](Treaty.md) |
|---|---|

| Warfare | [Warfare](Warfare overview.md) • [Land warfare](Land warfare.md) • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
