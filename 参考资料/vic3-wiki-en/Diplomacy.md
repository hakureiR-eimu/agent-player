---
title: Diplomacy
source: https://vic3.paradoxwikis.com/Diplomacy
pageid: 3126
categories: [1.13, Articles_with_potentially_outdated_sections, Pages_with_obsolete_template_parameters, Diplomacy]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

Diplomacy
Diplomatic actions
Diplomatic plays
Power blocs
Subjects
Treaties
**Diplomacy** is the relationship and interactions between countries. In Victoria 3, there are four major factors affecting diplomacy: *attitude, relations, infamy,* and *interests*. These factors impact which *diplomatic actions* are available and how likely an AI country is to accept them.

## Attitude

Each AI controlled country has an *attitude* towards every other country that influences what diplomatic actions it is likely to take. A country's attitude is based on its strategic desire towards another country as well as the relations value, infamy, military size, and diplomatic pacts of the other country. The various attitudes and the likely impact on AI behavior are detailed below from a perspective towards a country. Note that attitudes are only one of several factors that determine the actual AI behavior.

| Positive attitudes | **Protective** | **Genial** | **Cooperative** | **Conciliatory** |
|---|---|---|---|---|
| Likely Behavior | Side with country in diplomatic plays Offer country subject status | Improve relations with country Seek a defensive pact or alliance with country | Improve relations with country Accept diplomatic pacts from country | Improve relations with country End rivalry with country |
| Neutral attitudes | **Cautious** | **Disinterested** | **Human** |  |
| Likely Behavior | No effect | No effect | No effect |  |
| Negative attitudes | **Wary** | **Antagonistic** | **Belligerent** | **Domineering** |
| Likely Behavior | Reject diplomatic pacts from country Seek out alliances to defend from country | Side against country in diplomatic plays Seek out alliances with country's enemies | Target country in diplomatic plays | Subjugate country if it is independent Integrate country if it is a subject |
| Subject attitudes | **Loyal** | **Aloof** | **Defiant** | **Rebellious** |
| Likely Behavior | Agree to overlord demands | Maintain status quo | Seek greater autonomy from overlord | Seek independence from overlord |

## Relations

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.10. |
|---|---|

Relations is a bilateral value between **−100** and **+100** that determines the overall diplomatic standing between two countries. Relations are categorized into seven levels, based on the current relations score.

| Score | **−100** - **−80** | **−79** - **−50** | **−49** - **−20** | **−19** - **+19** | **+20** - **+49** | **+50** - **+79** | **+80** - **+100** |
|---|---|---|---|---|---|---|---|
| Relation level | **Hostile** | **Cold** | **Poor** | **Neutral** | **Cordial** | **Amicable** | **Friendly** |

Many diplomatic actions are blocked if relations are above or below a certain level, and starting diplomatic plays generally requires neutral or worse relations. Additionally, the relation score, along with attitude, impacts AI's acceptance of diplomatic actions and its willingness to join a side in diplomatic plays.

The primary way to change relations is through the *Improve Relations* and *Damage Relations* ongoing diplomatic actions, but most diplomatic actions and pacts affect relations, as do diplomatic incidents and various events.

## Infamy

Infamy represents a country's perceived aggression in the world. Infamy begins at **0** and can reach a maximum of **1000**. Infamy primarily increases from diplomatic plays but certain other actions and [events](Events.md) can add infamy. Infamy decays yearly at a base of **−5** and can be increased to **−6.25** from 100% excess influence.

### Infamy gain

Diplomatic demands generate infamy according to the formula : Infamy = Base value ⋅ ⋅ (1 + Pop multiplier) ⋅ ⋅ State multiplier ⋅ ⋅ ( 1 + Initiator modifier + Target modifier ) ⋅ ⋅ Subject multiplier ⋅ ⋅ Unrecognized target modifier ⋅ ⋅ Other modifiers {\displaystyle {\text{Infamy}}={\text{Base value}}\cdot {\text{(1 + Pop multiplier)}}\cdot {\text{State multiplier}}\cdot (1+{\text{Initiator modifier}}+{\text{Target modifier}})\cdot {\text{Subject multiplier}}\cdot {\text{Unrecognized target modifier}}\cdot {\text{Other modifiers}}} ![{\displaystyle {\text{Infamy}}={\text{Base value}}\cdot {\text{(1 + Pop multiplier)}}\cdot {\text{State multiplier}}\cdot (1+{\text{Initiator modifier}}+{\text{Target modifier}})\cdot {\text{Subject multiplier}}\cdot {\text{Unrecognized target modifier}}\cdot {\text{Other modifiers}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/2d57ab24fa2633088ed0b9a591bc764e929b010f) with :

| Rank | Initiator | Target |  |
|---|---|---|---|
|  | Great power | **+20%** | **+20%** |
|  | Major power | **+10%** | **+10%** |
| Unrecognized major power | **+50%** | **−30%** |  |
|  | Minor power | **+0%** | **+0%** |
| Unrecognized regional power | **+40%** | **−40%** |  |
|  | Insignificant power | **−10%** | **−10%** |
| Unrecognized power | **+30%** | **−50%** |  |

- **Base value** depends on the [war goal](Diplomatic play.md) used.
- **Pop multiplier** is 3 ∗ ∗ Population {\displaystyle 3*{\text{Population}}} ![{\displaystyle 3*{\text{Population}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/276feb9bf4ab304126bb5a0bd3e9853cf7c38162), where *Population* is the targeted population in millions. This multiplier is capped at 5 500% per targeted state and 50 5000% overall.[1]
- **State multipliers** reduce the infamy cost of targeted states if they are unincorporated (**−50%**) or homelands of the initiator's primary cultures (**−25%**). These apply separately to each state targeted and can stack.[2]
- **Initiator and target modifiers** depend on the rank and recognition status of both countries as shown in the table.
- **Subject multiplier** is 0.25 −75% if target a subject of the initiator and has less than 25 liberty desire or is opposing the initiator in a diplomatic play, **1** otherwise.
- **Unrecognized target modifier** only affects infamy generation by recognized countries against unrecognized countries; this is obtained by researching the Colonization (**−10%**) and Civilizing Mission (**−25%**) technologies. The principle Colonial Offices III also adds **−5%** per level of Colonial Affairs
- **Interest tier modifier** is **+25%** if initiator has None or Observant interest in the target's strategic regions, **+10%** if initiator has Engaged interest in the target's strategic regions, or **-20%** if initiator has Hegemonic interest in the target's strategic regions
- **Other modifiers** include Multilateral Alliances (**−25%**), and rulers with the character traits Cautious (**−20%**) and Reckless (**+20%**), and various country modifiers from events.

### Infamy levels

The amount of infamy a country has is categorized into four levels, and each affects how AI countries view and interact with the country. Each infamy level also increases the cost of maintaining diplomatic pacts and actions and increases subject liberty desire and radicals from gained conquest.

| Level | Infamy | Pact cost |
|---|---|---|
| ![Reputable](/images/thumb/1/17/Attitude_disinterested.png/24px-Attitude_disinterested.png) Reputable | 0 to 24.9 | 0 |
| ![Infamous](/images/thumb/7/73/Infamy_infamous.png/24px-Infamy_infamous.png) Infamous | 25 to 49.9 | **+25%** |
| ![Notorious](/images/thumb/8/8c/Infamy_notorious.png/24px-Infamy_notorious.png) Notorious | 50 to 99.9 | **+50%** |
| ![Pariah](/images/thumb/9/9b/Infamy_pariah.png/24px-Infamy_pariah.png) Pariah | 100 and above | **+100%** |

In particular, if a country reaches Pariah status, great powers can use theCut Down to Size diplomatic play, which returns conquests and releases subjects gained in previous 10 years and nullifies all war goals in any ongoing wars at the time this demand is conceded.

### Diplomatic incidents

Infamy is tied to the diplomatic incident mechanic. In the vast majority of cases, any diplomatic action a country takes – such as demanding land in a diplomatic play or violating a neutral country's sovereignty during war – that increases infamy also creates a diplomatic incident localized in a particular strategic region on the map. This adds a relation penalty to all countries with an interest in the region, based on the amount of infamy gained in the incident.

## Interests

Not to be confused with interest paid from
treasury
loans
| Tier | Involvement | Trade advantage | Wargoal infamy | Leverage | Colonize | Stake claims | Diplomatic plays | Establish Missions | Allowed pacts | Effects in region |
|---|---|---|---|---|---|---|---|---|---|---|
| None | 0-100 | **−50** (export only) | **+25%** | **−50%** | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |  |  |
| Observant | 100-1000 | 0 | **+25%** | **−25%** | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |  |  |
| Engaged | 1000-2500 | **+10** | **+10%** | +0% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |  |  |
| Influential | 2500-5000 | **+25** | +0% | +0% | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |  | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |  |  |
| Pervasive | 5000-9000 | **+50** | +0% | **+25%** | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |  |  |
| Hegemonic | 9000-10000 | **+100** | **−20%** | **+50%** | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |  | **−20%** Decree cost |

Interests represent a country's diplomatic engagement with a region of the world. Interests are divided into 5 tiers depending on how much involvement a country has accumulated in the given strategic region, plus an additional tier for little to no involvement. A country can also engage in diplomacy with its immediate neighbors, even without a specific interest in that region.

In order to start or join a diplomatic play, a country typically must have an interest in the region where the play is located. This can be used advantageously when attacking a country with states in many regions, as the initial demand can be targeted to a region where the country's rivals have no interest and thus cannot join the play.

Additionally, [colonization](Colonization.md) requires the colonizing nation to have an Engaged level of interest in the region.

Lacking interests in foreign markets reduces the country's [trade advantage](https://vic3.paradoxwikis.com/Trade) only when exporting to them, whereas having interests increases the trade advantage for both export and import, depending on their tier. For [power bloc](Power bloc.md) leaders, the tier of interest in a country's capital region also influences the amount of leverage gained by their power bloc over this country.

Involvement naturally moves to its target value every week, which can be modified in the following ways:

- **+2500** for regions where the country's capital is located
- **+1500** for regions adjacent to the capital's region
- Owning or having claims on states in the strategic region, from a minimum of **+1500** to a maximum of **+7500**
- Up to **+2500** depending on the GDP generated by the country in this region
- Up to **+5000** for having armies stationed in the strategic region, depending on their [power projection](https://vic3.paradoxwikis.com/Power_projection)
- Up to **+5000** for having navies performing the Project Power mission in sea zones adjacent to the region or being stationed in the strategic region, depending on their [power projection](https://vic3.paradoxwikis.com/Power_projection)
- Up to **+5000** from various [treaty](Treaty.md) articles and [diplomatic pacts](https://vic3.paradoxwikis.com/Diplomatic_pact), as well as [subjects](Subject.md) and [power bloc](Power bloc.md) juniors that are local to the region

## Diplomatic catalysts

Diplomatic catalysts represent various occurrences such as one country taking an action towards another, changes in relation levels, or even certain internal political events. Each catalyst can have various effects, such as prompting a [political lobby](Political lobby.md) to form or causing an AI country to reconsider its attitude towards another country.

## Diplomatic actions

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.10. |
|---|---|

Diplomatic actions are one form of diplomatic engagement.[3] Each diplomatic action can be categorized by whether it requires the target to accept and whether it happens immediately or establishes an ongoing pact. Diplomatic actions can be found in the *diplomatic actions* tab of the diplomacy lens or the *interactions* tab of a country's info window. Possible diplomatic actions are also shown when right-clicking on countries on the map. Most actions cannot be used with revolution countries; exceptions are noted below.

Some diplomatic actions can be offered as a sway in a diplomatic play or be negotiated as a part of a [diplomatic treaty](https://vic3.paradoxwikis.com/Diplomatic_treaty). Such offers, if accepted, cannot be broken for 10 years.

### Obligations

An *obligation* is a promise that a country can use to convince another country to agree to their proposal. A country can offer an obligation as a sway in [diplomatic plays](Diplomatic play.md) or as an extra incentive in diplomatic agreements. Obligations can also be gained as part of a [treaty](Treaty.md). Obligations from a treaty are gained when the binding period ends or after 10 years, whichever comes first.

Once an obligation has been obtained, it can be used to increase acceptance of a diplomatic offer or treaty, or to sway a country to join a diplomatic play. If a country rejects a proposal when an obligation has been used, it gains *Repudiated Obligation Repudiated Obligation (Decaying) Country modifier −25% Prestige −25% Infamy decay* for 5 years as well as losing **−50** relations with the offering country and **−30** relations with all other countries that it owes an obligation. Rejecting another obligation resets the modifier, but does not increase it.

An obligation is valid for ten years, after which it expires. While a country owes an obligation, it cannot oppose the country owed the obligation in diplomatic plays.

Obligations can be absolved for a boost of **+30** relations.

### Instant actions

The following actions happen immediately. Unless otherwise noted, the actor and target must be at peace with each other and have an interest in the same region.

| Action | Requires approval | Conditions | Effects |
|---|---|---|---|
| Expel Diplomats | ![No](/images/thumb/0/04/No.png/24px-No.png) | Is not improving relations with target Has not expelled target's diplomats within the last five years Not subject of the target or has 75 or more liberty desire | Lose −30 relations with target Target's diplomats are expelled for five years preventing improve relations action Reduce leverage generation up to ×0.3 if target is power bloc leader If the target is Supporting Separatism in the actor, it is cancelled Gain up to 10 infamy based on target's rank: 10 for great powers and major powers 7.5 for minor powers and unrecognized major powers 5 for insignificant powers and unrecognized regional powers 2.5 for unrecognized powers |
| Redeem Obligation | ![No](/images/thumb/0/04/No.png/24px-No.png) | Target owes actor an obligation Can be done while at war with target or without overlapping interests | Gain +30 relations with target Absolves target's obligation |
| Trade States | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | Neither country is committed in a diplomatic play Has greater than Poor relations Actor is not a subject Action can be used to demand or gift a state Either country has a valid state State is not a capital or colony States are not in same state region Other country can access potential traded state to trade | Each country gains control of the other's traded state |
| Violate Sovereignty | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | Is at war Target is not in war or at war with actor Target is not subject of actor Has less than Amicable relations Target borders both warleaders through one contiguous region. Can be used towards or by revolutionary countries | If target accepts: Create diplomatic incident with 15 infamy Target joins actor's side in war If target declines: Create diplomatic incident with 10 infamy Target joins enemy side in actor's war Other countries may join enemy side in actor's war |
| Join Power Bloc | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | Is independent Target leads a power bloc Has lower rank or less prestige than target Not at war war or opposing any power bloc member Power bloc has 200 or more leverage advantage on actor | If target accepts: Join target's power bloc If target declines: Lose −30 relations with target Set leverage advantage to 0 |
| Invite to Power Bloc | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | Leads a power bloc Target has lower rank or less prestige than target Target is not at war war or opposing any power bloc member Power bloc has 200 or more leverage advantage on target Target has not declined within 2 years | If target accepts: Target joins power bloc If target declines: Lose −50 relations with target |
| Stake Colonial Claim | ![No](/images/thumb/0/04/No.png/24px-No.png) | Target is either country type decentralized or unrecognized Cannot take this action again for 5 years Actor either: Is not on the same continent as target Does not have No Colonial Affairs Is country type company or colonial Target is either not a subject or overlord is not recognized Valid target state: Either: Target is decentralized and actor has at least influential interest in state's strategic region Target is unrecognized and actor has at least pervasive interest in state's strategic region Actor is adjacent to target state or target state is coastal and actor has an active port Actor does not have a claim on state | Actor gains a claim on target state Actor creates diplomatic incident with base 5 infamy in target state |

#### Bloc leader actions

The following actions can only be done by power bloc leaders of blocs with the specified central identity. The target must be a member of the power bloc for at least 5 years.

| Action / Bloc identity | Other conditions | Effects |
|---|---|---|
| Subjugate Sovereign Empire | Power bloc has 50 or more cohesion Target is independent Target is below major power Target is not at war or committed in a diplomatic play Has 5 times or more prestige than the target | Target becomes a protectorate or tributary, as appropriate Target starts with 80 liberty desire Create a 5-year truce with the target Power bloc loses 20 cohesion Loses additional 10 cohesion for each rank level With unrecognized power as 1, insignificant power as 2, etc. of target If the target is unrecognized, lose 1/3 as much |
| Force Regime Change Ideological Union | Power bloc has 10 or more cohesion At least 50 total difference in progressiveness between either: Target and bloc leader's Governance Principles laws Target and bloc leader's Distribution of Power laws Has 3 times or more prestige than the target | Target's Governance Principles and Distribution of Power laws are changed to be in line with bloc leader's Target gains Installed Regime Installed Regime Country modifier +20% Imposed enactment success chance for 5 years Power bloc loses 5 cohesion Loses additional 2.5 cohesion for each rank level With unrecognized power as 1, insignificant power as 2, etc. of target If the target is a great power, lose 7.5 more |
| Impose State Religion Religious Convocation | Power bloc has 50 or more cohesion Target does not have bloc leader's state religion Has 3 times or more prestige than the target | Target's state religion changes to bloc leader's 5% of pops in target's capital convert to new religion 2% of pops in target's other states convert to new religion Power bloc loses 5 cohesion Loses additional 2.5 cohesion for each rank level With unrecognized power as 1, insignificant power as 2, etc. of target If the target is a great power, lose 7.5 more |
| Spread Primary Culture Cultural Commonwealth | Power bloc has 50 or more cohesion Target does not share a primary culture with bloc leader. One of target's primary cultures shares a language trait or language trait group with one of bloc leader's primary cultures. Target has been in power bloc for 5 years. Has 3 times or more prestige than the target | Target gains whichever one of bloc leader's primary cultures is the largest in bloc leader. 5% of pops in target that share a language or language trait group with the new primary culture assimilate to it. Power bloc loses 20 cohesion Loses additional 10 cohesion for each rank level With unrecognized power as 1, insignificant power as 2, etc. of target If the target is unrecognized, lose 1/3 as much |

### Ongoing actions

The following actions are ongoing; they never require approval and can be ended any time by the actor. Most cost influence to maintain, modified by the target's [rank](Rank.md), actor's infamy, and clout of any pro-country lobby or anti-country lobby towards the target. All costs below are unmodified base costs. All of the following automatically end if any of their conditions are false.

| Action | Cost | Conditions | Effects |
|---|---|---|---|
| Improve Relations | 150 | At peace with target Is not damaging relations with target Neither country has expelled the other's diplomats Has less than Amicable relations Can be used towards or by revolutionary countries | Gain +0.03 relations with target daily, to a max of +50 |
| Damage Relations | 100 | Is not improving relations with target Has greater than Cold relations Can be used towards or by revolutionary countries | Lose −0.03 relations with target daily, to a max of −50 |
| Rivalry | — | Neither country is a non-autonomous subject Personal union, Crown land, Puppet, Colony, or Vassal or subject of the other Target is within one rank category of actor Target has the same recognition as actor Has less than Cordial relations | Changes appeasement of relevant lobbies in actor by ±4 Lose −0.01 relations with target daily, to a max of −20 Gain +200 influence ×0.5 if target's absolute rank is lower than actor's +50% for each overlapping interest, max +400 Modified by lobby clout, up to ±100 If actor is power bloc leader, adds −90% leverage generation on target Cannot manually break for 1 year If broken, changes appeasement of relevant lobbies in both countries by ±4 If autobroken and target has lower rank, anti-lobbies instead gain +2 |
| Embargo | 100 | Has researched International Trade Does not have Investment Rights in target Neither country has any variant of Isolationism enacted Neither country is a junior member of a customs union Neither country is a non-autonomous subject Personal union, Crown land, Puppet, Colony, or Vassal or subject of the other Target does not have an active treaty port towards actor Has Poor or lower relations | Changes appeasement of relevant lobbies in actor by ±2 Deactivates all trade routes between actor and target Lose −0.01 relations with target daily If target is a bloc leader, adds −50% leverage generation from target If broken, changes appeasement of relevant lobbies in both countries by ±2 |
| Fund Lobbies | 100 | Sphere of Influence is enabled Has researched Central Banking Has greater than Poor relations At peace with target Has higher rank than target Not in default | Fully Accepted pops in target receive money equal to 20% of its income Does not include tariffs or diplomatic pacts from actor Payment cannot exceed 10% of actor's income +25% pop attraction for interest groups in pro-lobbies towards actor −25% pop attraction for interest groups in anti-lobbies towards actor Interest groups in target more likely to join lobbies beneficial for actor pro toward actor; anti towards actor's rivals Interest groups in target less likely to join lobbies detrimental for actor anti toward actor; pro towards actor's rivals If no pro-country lobby exists in target towards the actor: Weekly chance of 0.25%–1% of creating a pro-country lobby Weekly chance of 2% of creating a pro-overlord lobby |
| Support Separatism | 100 | Has researched Nationalism Is independent or an autonomous subject Protectorate, Tributary, Chartered Company, or Dominion Has not had diplomats expelled by target Has less than Amicable relations Does not share any primary cultures with target Target owns a state with at least 10% population of a primary culture and a primary culture homeland of actor At peace with target | Lose −0.01 relations with target daily, to a max of −25 Increases pop attraction and activism of cultural minority movements of the actor's primary cultures in the target |
| Orchestrate Coup | 100 | Target: Does not have an active Coup JE Country rank is lower than actor country rank Has a pro-country or pro-overlord lobby which endorses actor Any admiral or general is part of an interest group in a friendly lobby and has less than 25 loyalty Commander coup strength is greater than or equal to country coup resistance Is not at war with target | Changes appeasement of relevant lobbies in actor by ±4 The aforementioned commander will begin a coup to install a pro-actor government in target Gain up to 15 infamy based on target's rank 15 for great powers and major powers 10 for minor powers and unrecognized major powers 7.5 for insignificant powers and unrecognized regional powers 5 for unrecognized powers Fully Accepted pops in target receives money equal to 25% of its income Does not include tariffs or diplomatic pacts, limited to at most 15% of actor's income from actor Will be canceled if at war with target, actor is not higher country rank than target, or coup is not ongoing |

### Subject actions and pacts

See also:
Subject
The following actions and pacts are generally used between a subject and its overlord. Some actions can also be used by the leader of a power bloc with its members. Influence cost is only paid by the overlord or bloc leader unless otherwise noted.

| Pact | Cost | Conditions | Effects | Auto-break conditions |
|---|---|---|---|---|
| Raise Payments | 25 | Sphere of Influence is enabled Target is a subject of actor Target is not opposing actor in a diplomatic play Target has some form of income transfer with the actor Target is not a protectorate or personal union Target has less than 75 liberty desire Target is not in default Does not have Decrease Payments with target | Target gains +0.1 Liberty desire weekly Target's pays 10% more of its income Does not include tariffs or diplomatic pacts to overlord Target can break if liberty desire is 75 or more | Target is opposing actor in a diplomatic play Target does not have some form of income transfer with the actor |
| Decrease Payments | 0 | Sphere of Influence is enabled Target is a subject of actor Target is not opposing actor in a diplomatic play Target has some form of income transfer with the actor Target is not a protectorate or personal union Does not have Raise Payments with target | Target's pays 10% less of its income Does not include tariffs or diplomatic pacts to overlord Target's loses −0.05 liberty desire weekly Cannot break for one year If manually broken, Target gains +10 liberty desire | Target is opposing actor in a diplomatic play Target does not have some form of income transfer with the actor |
| Exempt from Service | 0 | Actor is overlord or bloc leader of target Target is not opposing actor in a diplomatic play Target is required to join actor's diplomatic plays | Target is not required to join actor's diplomatic plays If target is a subject of actor, −0.05 Liberty desire weekly Cannot break for one year If manually broken and target is subject of actor, Target gains +10 liberty desire | Actor is not overlord or bloc leader of target |
| Grant Own Market | 0 | Target is member of actor's market Target is not opposing actor in a diplomatic play Target is independent or a direct subject of actor | Target is given an independent market When granted, if target is subject of actor, liberty desire changes by +50 to −20 depending on economic dependence Cannot break for one year If manually broken and target is subject of actor, Target gains +25 liberty desire | Actor is not direct overlord or bloc leader of target |
| Knowledge Sharing | 50 | Sphere of Influence is enabled Actor is overlord or bloc leader of target Target is not opposing actor in a diplomatic play | Target gains +25% technology spread Actor loses −10% technology spread If target is subject of actor, Target gains −0.05 liberty desire weekly When started, changes appeasement of target's overlord lobbies by ±2 Cannot break for one year If manually broken, Target gains +10 liberty desire Changes appeasement of target's overlord lobbies by ±2 | Actor is not direct overlord or bloc leader of target Actor has not researched more technologies than target |
| Request Market Control | 0 | Actor is member of target's market Target is not opposing actor in a diplomatic play Actor is either: Independent A direct subject of target with 25 or more liberty desire Has not requested market control within 5 years | If target agrees, Gain +10 relations with target Actor is given an independent market If actor is a subject of target, lose −30 liberty desire If target declines, Lose −20 relations with target If actor is a subject of target, gain +10 liberty desire If broken, Lose −10 relations with target | Target is not direct overlord or bloc leader of actor |
| Evangelize | 25 | Sphere of Influence is enabled Actor's state religion is not Atheist Actor has State Religion Target is subject of actor Target has same state religion as actor Target is not opposing actor in a diplomatic play | Target gains +50% conversion When started, target gains +10 liberty desire unless target has any of: State Religion Devout in government Any interest group with a Traditionalist or Theocrat leader in government Then target loses −10 liberty desire Cannot break for one year If manually broken, Target gains ±10 liberty desire by reverse condition as when started |  |
| Support Regime | 50 | Target is not opposing actor in a diplomatic play Target's legitimacy is less than 75 Target is subject of actor | Target gains: +20 Legitimacy −10% Political movement activism −0.1 Liberty desire weekly Actor loses −10 legitimacy When started, changes appeasement of target's overlord lobbies by ±4 Cannot break for one year If manually broken, Target gains +10 liberty desire Changes appeasement of target's overlord lobbies by ±4 |  |

| Action | Conditions | Effects |
|---|---|---|
| Appoint Colonial Governor | Sphere of Influence is enabled Target is subject of actor Target is not opposing actor in a diplomatic play A new governor type has not been appointed nor requested within 5 years Target has enacted Colonial Administration If actor is unrecognized, target is a vassal If actor is recognized, target is unrecognized, or not a protectorate or personal union | Actor chooses a new ruler for target May choose out of the following options: • Influential Planter ( ) • Local Appointee, with the subject's Primary Culture and Religion (instead of the Overlord's) • Experienced Extractor ( ) • Prominent Businessman ( ) • Military Governor ( ) The Governor will rule for a term of 4 years, before being automatically replaced by a character with the same unique trait |
| Request Colonial Governor | Sphere of Influence is enabled Target is direct overlord of actor Target is not opposing actor in a diplomatic play A new governor type has not been appointed nor requested within 5 years Actor has enacted Colonial Administration If actor is a vassal, target is unrecognized Actor is not a protectorate or a personal union | Actor gains modifier Requested Colonial Governor Requested Colonial Governor Country modifier −0.1 Weekly Liberty Desire for 5 years Actor chooses a new ruler May choose out of the following options: • Influential Planter ( ) • Local Appointee, with the subject's Primary Culture and Religion (instead of the Overlord's) • Experienced Extractor ( ) • Prominent Businessman ( ) • Military Governor ( ) The Governor will rule for a term of 4 years, before being automatically replaced by a character with the same unique trait |
| Change Language of Administration | Sphere of Influence is enabled Target is subject of actor Target is not opposing actor in a diplomatic play Actor has enacted Colonial Administration None of target's Primary Cultures: Are the same as Overlord's Share a Language trait with Overlord's | 10% of previous Primary Cultures pops in the subject become more radical All previous Primary Cultures are removed from the target country The subject gains all Primary Cultures the Overlord has • If the country has its capital in the Canada region and overlord has the Francophone language trait • Change Primary Culture of subject to Franco-Canadian • If the country has its capital in the Canada region and overlord has the Anglophone language trait • Change Primary Culture of subject to Anglo-Canadian • If the country is South Africa and overlord has the Dutch language trait • Change Primary Culture of subject to Boer 5% of Bureaucrats in the subject's Capital change to new Primary CultureSubject gains Changed Language of Administration Changed Language of Administration Country modifier −20% Bureaucracy −25% Institution Size Change Speed (decaying) for 5 yearsSubject's Capital state gains Exchanging Administrators Exchanging Administrators State modifier +75% Assimilation (decaying) for 5 years |
| Decrease Autonomy | Target is direct subject of actor Target is not opposing actor in a diplomatic play Target has less than 25 liberty desire Target's autonomy can be reduced i.e., not a puppet or vassal Target is not a personal union or actor has researched Nationalism Target is not a Chartered Company or actor has researched Civilizing Mission Target's autonomy has not changed within 5 years | Target's autonomy is reduced by one step Target gains +50 liberty desire All other direct subjects of actor gain +10 liberty desire Create 5-year truce with target |
| Increase Autonomy | Target is direct subject of actor Target is not opposing actor in a diplomatic play Target's autonomy can be increased i.e., not a protectorate or tributary Target is not a personal union or actor has researched Nationalism Target is not a Chartered Company or actor has researched Civilizing Mission Target's autonomy has not changed within 5 years | Target's autonomy is increased by one step Target loses −30 liberty desire Create 5-year truce with target |
| Request Increase Autonomy | Target is direct overlord of actor Target is not opposing actor in a diplomatic play Actor has 75 or more liberty desire Actor's autonomy can be increased i.e., not a protectorate or tributary Actor is not a personal union or has researched Nationalism Actor is not a chartered company or has researched Civilizing Mission Actor's autonomy has not changed within 5 years Has not requested more autonomy within 5 years | If target agrees, Actor's autonomy is increased by one step Actor loses −30 liberty desire Creates a mutual 5-year truce with target Lose −20 relations with target If target refuses, Actor gains +10 liberty desire Lose −30 relations with target Actor gains ability to demand increased autonomy for 5 years |
| Request Support Regime | Target is not opposing actor in a diplomatic play Target is overlord of actor Has not requested support regime within 5 years | If target agrees, Target establishes Support Regime pact with actor If target declines, Lose −20 relations with target Gain +10 liberty desire |
| Request Knowledge Sharing | Sphere of Influence is enabled Target is overlord of actor Target is not opposing actor in a diplomatic play Has not requested knowledge sharing within 5 years | If target agrees, Target establishes Knowledge Sharing pact with actor If target declines, Lose −20 relations with target Gain +10 liberty desire |
| Grant State | Target is subject of actor Neither country is at war or committed in a diplomatic play Actor has a valid state State is not a capital or colony State is not an owned incorporated primary culture homeland Can be a state owned by another annexable subject Crown land, Puppet, Colony, or Vassal Either: State neighbors target State is a coastal homeland of target's primary culture and target owns a coastal state to grant | Target gains state Target loses between −5 and −50 liberty desire, depending on value of state If state was owned by another subject, That subject gains between +20 and +100 liberty desire, depending on value of state |
| Take State | Target is an annexable subject Crown land, Puppet, Colony, or Vassal of actor Target is not at war or committed in a diplomatic play Target has less than 25 liberty desire Target has a valid state to take: State is not a capital or colony State is not incorporated or target is not a dominion | Actor gains state Target gains between +20 and +100 Liberty Desire, depending on value of state Create incident with target with between 10 and 50 infamy, depending on value of state |
| Demand State | Target is overlord of actor Neither country is at war or committed in a diplomatic play Target has a valid state State is not a capital or colony State is not an incorporated state of target State is not a primary culture homeland of owner Can be a state owned by another annexable subject Crown land, Puppet, Colony, or Vassal of target Either: State neighbors actor State is a coastal homeland of actors's primary culture and actor owns a coastal state to grant | If target agrees, Actor gains state Actor loses between −5 and −50 liberty desire, depending on value of state If state was owned by another subject, That subject gains bewteen +20 and +100 liberty desire, depending on value of state |
| Enforce Military Access | Target is subject of actor Actor is at war Target is not opposing actor in a war or diplomatic play Target is not involved in every war of actor | Target joins every war of actor as ally Target gains +10 liberty desire If target is a protectorate or tributary, it gains +20 instead |
| Invoke Doctrine of Lapse | Is East India Has not received event End of the Company Is at peace Has not Invoked Doctrine of Lapse within two years Target is an AI subject princely state Target is not an empire tier country | Create an incident with 20 infamy on target Lose −10 relations with every princely state Every princely state gains up to 25 liberty desire, based on target's prestige Target receives event Doctrine of Lapse Invoked Can be annexed or fight for independence If annexed, transfers gold reserves to East India |

## Treaties

Main article:
Treaty
Diplomatic treaties are bilateral agreements between two countries. They contain one or more articles – commitments from either party – which are binding for a specified period of time. Parties to a treaty can also renegotiate or withdraw from it after it is initially ratified. When an offer is received, it is possible to send a counter-offer. When signed, it will be agreed how long the treaty is binding for.

### Mutual articles

| Name | Requirements | Effect | Upkeep | Relations | Max involvement |
|---|---|---|---|---|---|
| Alliance | Mutually exclusive with Defensive Pact and Guarantee Independence International Relations Relations are at least amicable Highest overlapping interests tier is not less than influential Does not have a subject relationship with each other Neither of the two countries is a subject without diplomatic autonomy Must have Multilateral Alliances to sign more than one per country None of the two countries is Support Independence of a subject of either country | [First country] forms an alliance with [second country] Establishes an alliance between two countries Both countries may march their armies through the territory of their ally | 150 | **+1** every 66 days up to **80** | 3000 |
| Defensive Pact | Mutually exclusive with Alliance and Guarantee Independence International Relations Relations are at least cordial Highest overlapping interests tier is not less than engaged Does not have a subject relationship with each other Neither of the two countries is a subject without diplomatic autonomy | [First country] enters into a defensive pact with [second country] Establishes a defensive pact between two countries | 100 | **+1** every 100 days up to **80** | 2000 |

### Directional articles

Directional articles have a source, the country "giving" the article's effects, and often a target, the country "receiving" the article's effects.

| Name | Requirements | Effect | Input type | Upkeep | Relations | Max involvement |  |  |
|---|---|---|---|---|---|---|---|---|
| Source | Target | Source | Target |  |  |  |  |  |
| Guarantee Independence | Mutually exclusive with Alliance and Defensive Pact International Relations Source rank is higher than target rank Relations are above poor Source is not a subject Target is not a subject Highest overlapping interests tier is not less than engaged | [Target] is guaranteed by [source] An agreement established by one country targeting another, where the second country is able to call the first to aid it in any diplomatic play where they are the defender. | ![No](/images/thumb/0/04/No.png/24px-No.png) | 50 | 0 | **+1** every 100 days up to **80** | 0 | 1000 |
| Support Independence | International Relations Source does not have a subject relationship with target Target is a subject Source liberty desire must be at least 25 , share the same overlord, or not be a subject Source must be the same or greater rank to target, or share the same overlord Highest overlapping interests tier is not less than influential Source does not have an Alliance or Defensive Pact with target's overlord | [Target] is supported by [source] An agreement established by one country targeting another, where the first country commits to supporting a subject in a diplomatic demand for independence Diplomatic plays with wargoals: Independence Increase Autonomy Annex Subject Hungarian Revolution Sepoy Mutiny from its overlord. | ![No](/images/thumb/0/04/No.png/24px-No.png) | 50 | 0 | **+1** every 100 days up to **80** | 0 | 1000 |
| Take on Debt | Central Banking Is not unrecognized Target has debt Has sufficient capacity to take on debt This treaty does not have a Money Transfer article from target to source | [Source] takes over [target]'s loans Establishes a deal where one country takes over the other country's loans | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 0 | — | 0 | 0 |
| Money Transfer | Central Banking Is not in default | [Source] transfers money to [target] every week Establishes a deal between two countries where one country agrees to send a fixed sum of money to the other country on a weekly basis. | Quantity | 0 | 25 | — | 0 | 0 |
| State Transfer | Source has at least 2 states Valid states: Is not capital Is not under colonization Either is adjacent to source or is coastal and source has an active port | [Source] transfers a state to [target] Establishes an agreement between two countries where one country officially cedes a state to the other country | State | 0 | 0 | — | 0 | 0 |
| Investment Rights | Stock Exchange Source is not a subject of target If source is a subject, target does not have a treaty with this article with source's top overlord If source and target are in the same power bloc which has Foreign Investment Tier III, source rank is not lower than target rank Highest overlapping interests tier is not less than engaged | Allows [target] to build in [source] Establishes unilateral foreign investment rights in a country allowing it to construct buildings in the other country. | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 25 | **+1** every 200 days up to **50** | 0 | 0 |
| Join Power Bloc | Source is not a subject nor a power bloc leader Source has lower prestige or rank than the target Target is the leader of a power bloc Target's power bloc has sufficient leverage on source to invite Source is not already in target's power bloc Source is not opposing any target's power bloc members in a diplomatic play | [Source] joins [target]'s power bloc An agreement where one country officially joins another country's power bloc | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 0 | — | 0 | 0 |
| Power Bloc Embassy | International Relations Source and target are not in the same power bloc Source is not a power bloc leader Target is a power bloc leader | [Source] hosts a [target] [power bloc embassy](https://vic3.paradoxwikis.com/Power_bloc_embassy) Formally establishes a power bloc embassy in a another country | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 25 | **+1** every 200 days up to **20** | 2000 | 0 |
| Offer Embassy | Source is a Great Power and relations with target are above poor Target is unrecognized, has JE Earning Recognition , and has not requested an embassy from source | [Target] establishes an embassy in [source] Establishes an agreement between two countries where one country formally establishes an embassy in an unrecognized power | ![No](/images/thumb/0/04/No.png/24px-No.png) | 25 | 0 | **+1** every 200 days up to **20** | 2000 | 0 |
| Military Assistance | General Staff Source's army power projection is greater than target's Source rank is higher than target rank | [Source] grants military assistance to [Target] A military agreement between two countries where one country grants military assistance to another country, aiding them with enhanced training and military expertise Source gains: +10% Military Goods Cost +25% Weekly Experience Gain for Armies & Navies Target gains: −10% Military Goods Cost +50% Weekly Experience Gain for Armies & Navies +20% Training Rate +300 Leverage Generation from Treaty +10% Technology Spread for Military | ![No](/images/thumb/0/04/No.png/24px-No.png) | 25 | 0 | **+1** every 200 days up to **50** | 0 | 1000 |
| Goods Transfer | International Trade Neither country is a junior member in a customs union The target market is reachable for trade by the source via land adjacency or a shipping lane Source's Supply Network strength is greater than or equal to 75% or is adjacent to target | [Source] transfers goods to [target] every week Establishes a deal between two countries where one country agrees to send a fixed sum of goods to the other country on a weekly basis The source buys an amount of a specific good on their own market and sells it on the targets market [4] | Quantity Goods | 10 | 0 | — | 0 | 0 |
| Treaty Port | Colonization Source is not revolutionary and has a coastal state that contains a valid treaty port Target is not a subject of source To maintain: either target or its revolutionary or secessionist civil war country controls the state Source rank is not higher than target rank | [Source] cedes a [treaty port](https://vic3.paradoxwikis.com/Treaty_port) to [target] An agreement between two countries where one country officially cedes a treaty port to the other country | State | 0 | 50 | **−1** every 200 days down to **0** | 3000 | 0 |
| Military Access | International Relations | [Target] can march armies through [source] Establishes a military agreement between two countries where one country is allowed to march its armies through the territory of the other country | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 25 | **+1** every 200 days up to **20** | 1000 | 0 |
| Non-Colonization Agreement | Civilizing Mission Source must have a source of colonial growth Valid Strategic Regions: If source has Frontier Colonization, source has a state in the region Target has an interest Any country is decentralized in the region | [Source] agrees to **not** colonize a [strategic region](Strategic region.md) Establishes an agreement between two countries where one country is not allowed to colonize the agreed upon strategic region | Region | 0 | 10 | **−1** every 400 days down to **0** | 0 | 0 |
| Prohibit Trade with World Market | International Trade Source does not have Isolationism or Sakoku [5] and is not a junior member in a customs union Target is not a subject of source Valid goods: Sell orders for good in source market not less than 10 Is tradable | [Source] will **not** trade a good on the [world market](https://vic3.paradoxwikis.com/World_market) The country may not trade a specific good with the world market | Goods | 0 | 25 | **−1** every 200 days down to **0** | 0 | 0 |
| Company Monopoly | Corporate Charters Source is not revolutionary Target has any company established Either: If source is a subject, target has Investment Rights with source's top overlord Target has Investment Rights with source Source is a subject of target Source and target are in the same power bloc which has Foreign Investment Tier III and target rank is higher than source rank | [Source] grants a company monopoly to [target] Establishes an agreement between two countries that establishes a company monopoly of a building in the other country. | Company | 0 | 25 | — | 1000 | 0 |
| Law Commitment | International Relations Source is not a subject of target Target is of equal or higher rank to source | [Source] commits to passing a [law](https://vic3.paradoxwikis.com/Law) Establishes an agreement between two countries where one country commits to passing or retaining a specific law. | Law | 0 | 25 | — | 0 | 0 |
| No Tariffs | International Trade Neither country is a junior member in a customs union nor has Isolationism or Sakoku [5] Target is not revolutionary Valid goods: Sell orders for good in source market not less than 10 Is tradable | [Source] will **not** impose [tariffs](https://vic3.paradoxwikis.com/Tariffs) on a good Establishes an agreement between two countries where one country agrees to not impose tariffs on a specific good. | Goods | 0 | 10 | **−1** every 400 days down to **0** | 0 | 0 |
| Transit Rights | International Relations Neither country is a junior member in a customs union Target has a strategic adjacency to source via itself or another Transit Rights treaty | [Target] can trade through [source] Establishes an agreement between two countries where one country is granted the right to handle its trade through the world market hubs of the other country. [6] | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 50 | **+1** every 200 days up to **20** | 1000 | 0 |
| Trade Privileges | International Relations Neither country is a junior member in a customs union nor has Isolationism | [Target] receives [trade privileges](Market.md) from [source] Establishes trade privileges between two countries where one country grants favorable conditions to the traders of the other country. | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 50 | **+1** every 200 days up to **20** | 1000 | 0 |
| No Subventions | International Trade Neither country is a junior member in a customs union nor has Isolationism or Sakoku [5] Target is not revolutionary Source does not have any variant of Free Trade Valid goods: Sell orders for good in source market not less than 10 Is tradable | [Source] will **not** grant [subventions](https://vic3.paradoxwikis.com/Subventions) on a good Establishes an agreement where one country agrees to not grant subventions on a specific good. | Goods | 0 | 10 | **−1** every 400 days down to **0** | 0 | 0 |
| Amend Succession | Is Brazil Target is Portugal with active JE The United Kingdom Source is not revolutionary, has enacted Monarchy, and does not have a regency Target has enacted Monarchy | [Source] will permit [target]'s candidates to succeed to its throne Establishes an agreement where one country agrees to reincorporate another country's ruling family into their line of succession. Fires the event Back in Order if never before, otherwise Portugal 's ruler is set as Brazil 's heir | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 25 | **+1** every 200 days up to **25** | 0 | 0 |
| Recognize Independence | Source is Spain Target has modifier Independence Not Recognized by Spain Independence Not Recognized by Spain Country modifier −10% Influence Source is not at war | [Source] will formally recognize the independence of [target] An agreement where Spain will formally recognize the independence of her formal colony | ![No](/images/thumb/0/04/No.png/24px-No.png) | 25 | 0 | — | 0 | 0 |
| Transfer Subject | Source has at least 1 subject Valid subjects: Can be transferred as a subject to target Either is adjacent to target or both it and target have an active port | [Source] transfers a [subject](Subject.md) to [target] Establishes an agreement between two countries where one country officially cedes a subject to the other country | Country | 0 | 0 | — | 0 | 0 |
| Ship Transfer | Source is not revolutionary Source has any available ships for transfer Target has an active port Valid ships: Not in battle | [Source] transfers a ship to [target] Establishes an agreement between two countries where one country transfers ownership of a ship to the other country | Ship | 0 | 0 | — | 0 | 0 |
| Toll Exemption | International Relations Source has control over any strait | Exempts [target] from paying [tolls](https://vic3.paradoxwikis.com/Tolls) to [source] Exempts a country from paying tolls to the other country. | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 10 | **+1** every 200 days up to **20** | 0 | 250 |
| No Tolls | International Relations Source has control over any strait | [Source] will **not** impose tolls on any straits it controls Establishes an agreement between two countries where one country agrees to not impose tolls on any straits it controls. | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 25 | **+1** every 200 days up to **20** | 500 | 0 |
| Strait Access | International Relations Source has control over any strait | [Target] is granted access through straits controlled by [source] Establishes an agreement between two countries where one country is granted full access through straits controlled by the other country | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 10 | **+1** every 200 days up to **20** | 250 | 0 |
| No Strait Closure | International Relations Source has control over any strait | [Source] will **not** restrict access to straits it controls Establishes an agreement between two countries where one country agrees to not restrict access to any straits it controls. | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 25 | **+1** every 200 days up to **20** | 0 | 500 |
| Non-Piracy Agreement | International Relations Sourcce is unrecognized Source either is not a subject or its overlord is unrecognized | [Source] stops engaging in piracy against [target] An agreement where one country stops engaging in piracy against the other country | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 10 | — | 250 | 0 |
| Abandon Piracy | International Relations Sourcce is unrecognized Source either is not a subject or its overlord is unrecognized | [Source] abandons piracy An agreement where one country abandons piracy | ![No](/images/thumb/0/04/No.png/24px-No.png) | 0 | 25 | — | 0 | 500 |

## References

1. ↑ See /Victoria 3/game/common/defines/00_defines.txt: WAR_GOAL_INFAMY_POPULATION_SCALING_FACTOR WAR_GOAL_INFAMY_POPULATION_SCALING_MULTIPLIER WAR_GOAL_INFAMY_POPULATION_SCALING_MULTIPLIER_MAX_PER_STATE WAR_GOAL_INFAMY_POPULATION_SCALING_MULTIPLIER_MAX_TOTAL
2. ↑ See /Victoria 3/game/common/defines/00_defines.txt: `WAR_GOAL_INFAMY_HOMELAND_FACTOR` and `WAR_GOAL_INFAMY_UNINCORPORATED_FACTOR`
3. ↑ The script files can be found in the folder /Victoria 3/game/common/diplomatic_actions
4. ↑ If the market price of the good is lower in the target's market than the market price in the source's market, the source will make a loss. Vice versa, and they will make a profit. Goods transfer uses convoys of the source. The amount of used convoys scales proportionally with the amount of the good and the convoy cost multiplier of the good.
5. ↑ 5.0 5.1 5.2 Canton System is exempt
6. ↑ This is useful for landlocked countries that cannot access the world market otherwise

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

| Diplomacy | Diplomacy • [Diplomatic action](https://vic3.paradoxwikis.com/Diplomatic_action) • [Diplomatic play](Diplomatic play.md) • [Power bloc](Power bloc.md) • [Ranks](Rank.md) • [Subjects](Subject.md) • [Treaties](Treaty.md) |
|---|---|

| Warfare | [Warfare](Warfare overview.md) • [Land warfare](Land warfare.md) • [Naval warfare](Naval warfare.md) • [Wargoals](https://vic3.paradoxwikis.com/Wargoal) • [Conscription](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| Others | [Countries](Countries.md) • [Decisions](Decision.md) • [Events](Events.md) • [Journal](Journal.md) • [Objectives](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|
