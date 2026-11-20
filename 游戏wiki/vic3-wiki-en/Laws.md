---
title: Laws
source: https://vic3.paradoxwikis.com/Laws
pageid: 1592
categories: [1.13, Pages_with_obsolete_template_parameters, Laws, Game_concepts]
fetched: 2026-10-27
---
This article has been verified for the current [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) (1.13) of the game.

Laws
Power structure laws
Economy laws
Human rights laws
Amendments
France's starting laws. Some of them have amendments that alter their effects. The numbers above the crossing arrows refer to the number of alternative laws currently available to be enacted in that sub-category. The icon at the bottom right of certain laws indicate that they are tied to a specific institution.
**Laws** represent legal reforms in a [country](https://vic3.paradoxwikis.com/Country) that affect the political, economic, and social conditions of its population. Each country always has one active law in each active law group. At the start of the game, all countries have laws close to the actual situation in those countries in 1836. Over the course of the game, those laws may be changed under internal or external pressure. Interest groups endorse or disapprove of various laws based on their and their leaders' [ideologies](Ideology.md). [Political movements](Political movement.md) also advocate for or against changes to a country's laws. Certain [diplomatic plays](Diplomatic play.md) can change another country's laws as well.

Laws affect the country and its population in various ways, with effects ranging from a simple change in modifiers to fundamentals such as the system of governance. Each [institution](https://vic3.paradoxwikis.com/Institution), such as policing and colonization, has a law category that establishes the institution and modifies its effects. The laws of the country provide the largest the amount of [authority](https://vic3.paradoxwikis.com/Authority) available to the player, with more authoritarian laws generally providing more authority.

Some laws may have **law variants**. An example is Canton System, which replaces Isolationism for [China](China.md). A law variant inherits all ideological stances from its parent, but may have vastly different effects. For clarity, names of law variants are followed by names of their parent laws in parentheses when viewed in-game.

The current set of laws and potential changes to laws can be found in the politics tab.

## Enacting laws

At each checkpoint, one of the 4 options (success, debate, advance, stall) occurs.
Enacting a new law is a process that takes several steps.

First, a law needs support to be chosen. This requires an [interest group](Interest group.md) in the current government, the ruler, or a non-passive [political movement](Political movement.md) that endores the potential change. If the [government](Government.md) is considered *illegitimate* (below **25** legitimacy), it is completely unable to pass any law – except those endorsed by a non-passive movement. If the enactment process has already started and the government then becomes illegitimate, the law makes no progress until the government's legitimacy increases.

Next, the proposed law progresses through enactment with a periodic chance for success, advancement, debate, or stalling. There are three phases of enactment. When the law has progressed through all three phases, it is officially in effect.

| Condition (first valid) | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|
| Technocracy | Formulation | Review | Implementation |
| Council Republic | Discussion | Amendment | Approval |
| Autocracy | Introduction | Consideration | Adoption |
| / Republic Any voting except Single-Party State | Sponsorship | Study | Voting |
| Monarchy Any of: Wealth Voting Census Suffrage Universal Suffrage | Referral | Drafting | Voting |
| Monarchy Any of: Oligarchy Landed Voting Single-Party State | Introduction | Consideration | Assent |
| Fallback | Drafting | Amendment | Voting |

### Law support

| Law Stances |  |
|---|---|
| Strongly Approves | **+2** |
| Approves | **+1** |
| Neutral | **0** |
| Disapproves | **−1** |
| Strongly Disapproves | **−2** |
| Law Changes |  |
| One step | **±5** |
| Two steps | **±10** |
| Three or more steps | **±20** |

| Law group | Mult. |
|---|---|
| Governance Principles | **×2** |
| Slavery | **×2** |
| Land Reform | **×1.5** |

Support for a law can come from an interest group in government, a non-passive [political movement](Political movement.md)Has at least **25** activism, or directly from the [ruler's ideology](Character ideology.md). Interest groups' ideologies and their leaders' ideologies affect which laws they support along a 5-point scale from ![Oppose](/images/thumb/6/65/Political_disapproval.png/24px-Political_disapproval.png) **strongly oppose** to ![Endorse](/images/thumb/3/37/Political_approval.png/24px-Political_approval.png) **strongly endorse**. Interest groups support any law that is preferred over the current one; similarly, they oppose any law that is less preferred than the current one. Interest groups in government that support the proposed law provide the initial success chance, while all non-marginal interest groups that oppose it provide the initial stall towards enactment. Opposing interest groups that have neutral or happier approval provide only half as much stall chance, interest groups that are angry provide 50% more stall chance. Non-passive political movements also provide enactment chance equal to their support, either endorsing or opposing based on their stance toward the law. The ruler's stance on a law provides **±5%** chance per step of difference from the current law.

Aside from providing support, interest groups gain or lose approval based on current laws and proposed changes. Changes have approximately five times the effect on approval, but that effect decays over five years. Thus, a quick way to appease an unhappy or angry interest group is to propose a change to a law they approve of. Even without the intention to actually enact it, it can provide time for other effects to wear off or take place. Certain law groups – as noted on the right – multiply the effect of law changes on approval, but this is always capped at **±20**.

Similarly, political movements gain or lose activism based on current laws and proposed changes.

Law Commitment treaty articles can also provide support to enact a law, with **+5%** per rank category the other party in the treaty has over the country committing to the law. For example, a law commitment by a major power (rank 6) to a great power (rank 7) gives +5% success chance. A minor power (rank 4) would get +15%, and so on.

### Imposing laws

Overlords can impose laws on their non-autonomous Personal union, Crown land, Puppet, Colony, or Vassal [subjects](Subject.md), starting their enactment as usual. It must be possible for the subject to enact the law in order for the overlord to impose it. The imposed law goes through all regular enactment and may fail or cause a revolution as normal. Puppets, Colonies, Crown Lands, and Chartered Companies receive a **+10%** success chance for imposed laws.

Certain [power bloc](Power bloc.md) identities or principles allow the power bloc leader to impose certain laws on the members of their bloc.

Imposing a law starts a journal entry for the imposed country, with an option to begin or refuse enacting the imposed law. While the journal is active, no other law can begin enactment, and the imposed law can only begin enactment through the journal entry's buttons.

id
Foreign Legal Imposition
Our [overlord] [imposer country] has declared it imperative that we enact [imposed law].
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Law imposition | Effects when activated: None |
| Entry buttons: Accept Imposition Accept the imposition and begin enacting the law proposed by [imposer country]. Visible if: Has not rejected enacting [imposed law] Enabled if: Is not already enacting [imposed law] Effects: Cancels any other active law enactment Begins enacting [imposed law] Agreeable to Law Imposition Agreeable to Law Imposition Law enactment modifier +10% Enactment success chance Enactment cannot be manually cancelled Reject Imposition Abandon this venture and notify [imposer country] that you will not be adhering to their wishes after all. Visible if: Has not rejected enacting [imposed law] Effects: Cancels enactment and imposition of [imposed law] Lose −50 relations with [imposer country] If a subject of [imposer country], gain +10 liberty desire Otherwise, if in a power bloc lead by [imposer country], the bloc loses −10 cohesion Pro-country lobbies towards [imposer country] lose −2 appeasement |  |
| *Accept the imposition and begin enacting the law proposed by [imposer country].* |  |
| **Visible if:** Has not rejected enacting [imposed law] |  |
| **Enabled if:** Is not already enacting [imposed law] |  |
| **Effects:** Cancels any other active law enactment Begins enacting [imposed law] Agreeable to Law Imposition Agreeable to Law Imposition Law enactment modifier +10% Enactment success chance Enactment cannot be manually cancelled |  |
| *Abandon this venture and notify [imposer country] that you will not be adhering to their wishes after all.* |  |
| **Visible if:** Has not rejected enacting [imposed law] |  |
| **Effects:** Cancels enactment and imposition of [imposed law] Lose −50 relations with [imposer country] If a subject of [imposer country], gain +10 liberty desire Otherwise, if in a power bloc lead by [imposer country], the bloc loses −10 cohesion Pro-country lobbies towards [imposer country] lose −2 appeasement |  |
| Completion conditions: [Imposed law] is enacted | Effects when completed: Gain +20 relations ±1 Appeasement for lobbies targeting [imposer country] Gain Enacted an Imposed Law Enacted an Imposed Law (Decaying) country modifier +10 Legitimacy for 5 years |
| Invalidation conditions: Either: Rejected enactment of [imposed law] [Imposer country] can no longer impose laws on this country | Effects when invalid: Cancel enactment of [imposed law] |

### Enactment process

| Law group | ![Time](/images/thumb/0/08/Time.png/24px-Time.png) |
|---|---|
| Governance Principles | **200** |
| Distribution of Power Economic System Slavery | **150** |
| All others | **100** |

Once a law is chosen for enactment, it begins progressing towards a *checkpoint*. Enactment can be cancelled at any time, and cancelling a law change prevents attempting that specific law again for two years. The default time between checkpoints is ![Time](/images/thumb/0/08/Time.png/24px-Time.png) 100 days, and this is increased or decreased by various factors, such as [legitimacy](https://vic3.paradoxwikis.com/Legitimacy) or surplus authority, as well as temporary modifiers. Certain law groups – as noted on the right – have longer base times.

At each checkpoint, one of the four things can happen: *Success, Advance, Debate,* or *Stall*.[1]

- Success means that the law progresses to the next phase; if the law is already in the final phase, it immediately comes into effect and the process ends.
- Advance triggers some kind of a positive [event](https://vic3.paradoxwikis.com/Event) that usually increases success chance and sometimes offers a choice between a high increase of success chance and a medium increase in success chance plus a different bonus.
- Debate triggers an event that can be either a positive or a negative, often offering some kind of a trade-off between increasing the success chance for a price or decreasing the success chance.
- Stall triggers an event that usually reduces the success chance, sometimes with an option to take a smaller reduction and a different penalty.

During the entire progress, the law can meet a *setback* – something that hinders the law. If the law has three setbacks over the course of the entire process, the enactment fails, and that law cannot be proposed again for two years. Setbacks occur during enactment events or if the law reaches 0% success chance.

Interest groups in government and non-passive [political movements](Political movement.md) that support the law contribute their clout and support, respectively, to the *base success chance*, while all non-marginalized interest groups and non-passive [political movements](Political movement.md) who oppose the law contribute to *stall* chance. If the ruler has a stance on the law, they provide **+5%** chance per step of difference between the proposed law and the current law, either to support or oppose.

The chance for *advance* starts at twice the chance for success minus the stall chance, and the chance for *debate* is the difference between the other three options and 100%. If the chance of debate would go to less than 0%, instead an *end-of-discussion* factor is applied to scale the lower of success or stall chances so the sum chance remains 100%.

When a law progresses from one phase to the next, all accumulated effects on enactment success – both positive and negative – carry over to the next phase. Therefore, it is often better to choose a **+5%** Enactment Success Chance out of an early event, which is effectively a **+5%** bonus to each of the three phases instead of immediately progressing a single phase.

If the country's [government](Government.md) legitimacy falls to *Illegitimate*, it cannot continue law enactment until the legitimacy is raised to at least *Unacceptable*, unless the law is endorsed by a movement with at least **25** activism.

#### Formulas

Base success chance = ∑ ∑ ( Clout of endorsing interest groups in government ) + ∑ ∑ ( Support of endorsing non-passive political movements ) + Ruler's endorsement {\displaystyle {\text{Base success chance}}=\sum ({\text{Clout of endorsing interest groups in government}})+\sum ({\text{Support of endorsing non-passive political movements}})+{\text{Ruler's endorsement}}} ![{\displaystyle {\text{Base success chance}}=\sum ({\text{Clout of endorsing interest groups in government}})+\sum ({\text{Support of endorsing non-passive political movements}})+{\text{Ruler's endorsement}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/08d8acee651df7ff65f132b9660d4bd66f6cd397)

Base stall chance = 0.5 ⋅ ⋅ ∑ ∑ ( Clout of neutral or happier opposing interest groups ) + ∑ ∑ ( Clout of unhappy opposing interest groups ) + 1.5 ⋅ ⋅ ∑ ∑ ( Clout of angry opposing interest groups ) + ∑ ∑ ( Support of opposing non-passive political movements ) + Ruler's opposition {\displaystyle {\text{Base stall chance}}=0.5\cdot \sum ({\text{Clout of neutral or happier opposing interest groups}})+\sum ({\text{Clout of unhappy opposing interest groups}})+1.5\cdot \sum ({\text{Clout of angry opposing interest groups}})+\sum ({\text{Support of opposing non-passive political movements}})+{\text{Ruler's opposition}}} ![{\displaystyle {\text{Base stall chance}}=0.5\cdot \sum ({\text{Clout of neutral or happier opposing interest groups}})+\sum ({\text{Clout of unhappy opposing interest groups}})+1.5\cdot \sum ({\text{Clout of angry opposing interest groups}})+\sum ({\text{Support of opposing non-passive political movements}})+{\text{Ruler's opposition}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/75f0606b12c018a2840a977ac96d896492c0ac66)

Advance chance = 2 ⋅ ⋅ Base success chance − − Base stall chance {\displaystyle {\text{Advance chance}}=2\cdot {\text{Base success chance}}-{\text{Base stall chance}}} ![{\displaystyle {\text{Advance chance}}=2\cdot {\text{Base success chance}}-{\text{Base stall chance}}}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/25a03d21986df168250f557811795a10530d1d10)

Debate chance = 100 − − ∑ ∑ ( Advance chance + Base success chance + Base stall chance ) {\displaystyle {\text{Debate chance}}=100-\sum ({\text{Advance chance}}+{\text{Base success chance}}+{\text{Base stall chance}})} ![{\displaystyle {\text{Debate chance}}=100-\sum ({\text{Advance chance}}+{\text{Base success chance}}+{\text{Base stall chance}})}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/3f2dae4ac1aef1286728ba8635d10043c25a3f80)

## Law categories

There are three major categories of laws – Power structure (10 groups), Economy (8 groups), and Human rights (8 groups) – which then contain between three and nine specific laws each.

Many laws require a specific technology to be unlocked, and many require certain other laws to be enacted or not enacted – for example, it is not possible to enact Multiculturalism while the country practices Slave Trade. A few laws are unique to a certain culture, and typically have a set of very specific requirements. Generally, if a country has a unique law variant, it will replace that variant's base law. For example, the Chinese Canton System is unique to Han Chinese countries that own Western Guangdong and replaces Isolationism.

### Power structure laws

Main article:
Power structure laws
- *Governance Principles* – The foundational principles and authority by which the country is governed. Determines who the Head of State is.
- *Distribution of Power* – How political power is distributed. Determines who the Head of State is accountable to.
- *Citizenship* – Extending the rights of citizenship.
- *Caste Hegemony* – Erasure of rights among members of society based on the British Indian Caste System.
- *Edo Status System* – Enforcement of the Edo Status System.
- *Church and State* – The relationship between physical and spiritual governors.
- *Bureaucracy* – How the country is administered.
- *Army Model* – How the army is organized and regulated.
- *Navy Model* – Organization and doctrine of the naval forces.
- *Internal Security* – Keeping the country's affairs in order.

### Economy laws

Main article:
Economy laws
- *Economic System* – The fundamental principles of the economy.
- *Trade Policy* – Laws governing trade and the exchange of goods across borders.
- *Taxation* – How the state raises revenue by taxing its citizens.
- *Land Reform* – The laws governing agricultural land and the people who work it.
- *Colonization* – The stance on establishing colonies to supplant and conquer decentralized nations.
- *Policing* – The priorities of the national police force.
- *Education System* – For when the children are done with chimney sweeping chores.
- *Health System* – Laws about the government's involvement (or lack thereof) in providing healthcare for its citizens.

### Human rights laws

Main article:
Human rights laws
- *Free Speech* – Laws regulating free speech and right to public assembly.
- *Labor Rights* – The rights of workers.
- *Children's Rights* – The rights and protections afforded to children.
- *Rights of Women* – The legal regulations of the fairer sex.
- *Welfare* – Government assistance for the income deprived.
- *Migration* – Controlling the flow of people.
- *Slavery* – People as property.
- *Labor Associations* – Regulations placed upon worker's and craftsmen's associations.

## References

1. ↑ The game's RNG determines the outcome based on the save seed, the exact game day, and the exact chances. Reloading a save does not change any of these and so cannot give a different outcome alone. Changing the checkpoint day by changing surplus authority is the easiest way to change the outcome.

---

1. To update page content see reference files in folder /Victoria 3/game/common/laws:
  1. Each law type has its own `txt` file (named after the law type).
2. To update flavor text see reference files in folder /Victoria 3/game/localization/english:
  1. For laws flavor text see reference file laws_l_english.yml.
  2. For modifiers flavor text see reference file modifiers_l_english.yml.
  3. For institutions flavor text see reference file institutions_l_english.yml.
  4. For inventions flavor text see reference file inventions_l_english.yml.

Game concepts
Return to top
| Pops | [Pops](Pops.md) • [Acceptance](Acceptance.md) • [Culture](Culture.md) • [Migration](Migration.md) • [Needs](Needs.md) • [Professions](Profession.md) • [Religion](Religion.md) • [Standard of living](Standard of living.md) |
|---|---|

| Government | [Government](Government.md) • [Capacities](Capacity.md) • [Characters](Character.md) • [Decrees](Decrees.md) • [Institutions](Institutions.md) • Laws • [Technology](Technology.md) |
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
