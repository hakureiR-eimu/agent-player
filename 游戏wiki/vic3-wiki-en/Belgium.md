---
title: Belgium
source: https://vic3.paradoxwikis.com/Belgium
pageid: 5111
categories: [Pages_using_TabberTransclude_parser_tag, Potentially_outdated_countries, 1.11, Countries, Articles_with_potentially_outdated_infoboxes, Articles_with_potentially_outdated_sections, Pages_with_interwiki_links_to_Wikipedia, Articles_with_potentially_outdated_guides, Starting_countries]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.11.

Belgium
---

Capital
:
Flanders (Brussels)
---

Government Type
:
Constitutional Monarchy
---

Primary Cultures
:
Flemish, Wallonian
---

State Religion
:
Catholic
---

Country Tier
:
Kingdom
---

Country Type
:
Recognized
Belgium
---

Capital
:
Flanders (Brussels)
---

Gov. Type
:
Constitutional Monarchy
---

Prim. Cult.
:
Flemish, Wallonian
---

State Rel.
:
Catholic
---

C. Tier
:
Kingdom
---

C. Type
:
Recognized
*"In Belgium the industrial revolution is in full swing. The yoke of Dutch oppression was cast aside just six years ago and the country is bounding ahead of their former masters, with the construction of the first railroad in continental Europe. What does the future hold for them?"*

**Belgium** is a minor power in western Europe. It borders the [Netherlands](Netherlands.md) to the north, [Prussia](Prussia.md) and [Luxembourg](Luxembourg.md) to the east, [France](France.md) to the south and the English Channel to the west.

Belgium is able to form the [United Netherlands](United Netherlands.md) if it conquers the Netherlands and Luxembourg.

Belgium is one of the recommended countries for the *Learn the Game* [objective](Objective.md) along with [Sweden](Sweden.md), [New Granada](Colombia.md) and [Dai Nam](Dai Nam.md).

## Historical background

After the Belgian Revolution, Belgium became independent of the [Netherlands](Netherlands.md) in 1830. After independence, a parliamentary monarchy was established under King Leopold of Saxe-Coburg and Gotha.

## Scripted content

Belgium has a journal entry and events representing the London Conference of 1838. The events start at the beginning of 1838

id

### The Belgian Question

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.11. |
|---|---|

---

Since the secession of Belgium in 1830, Dutch efforts to reunify the country have all met with failure. Weary of the effects of the current, uneasy truce, many are now urging the king to commit to a final, negotiated settlement.
---

Flavor text:
"The revolution of 1830 is and will remain the greatest state error of this century, but our efforts to reclaim these lands by force have failed and our prospects are looking bleaker by the day.
We currently stand to gain more from arbitration than we do through force of arms. Sir, I implore you to dispatch a mission to Brussels as soon as humanly possible."
---

| Is triggered by: Monthly pulse |
|---|
| Trigger conditions: Is Netherlands Year is 1838 or later This event hasn't occured before |
| Agreed. Call for a conference to settle the matter at last. Triggers event The Hague Call for a Conference for Belgium We do not negotiate with rebels. Lose 80 relations with Belgium Belgium gains a negative event catalyst towards Netherlands Lose 40 relations with every great power in Europe |

id

### The Hague Call for a Conference

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.11. |
|---|---|

---

Weary of the uneasy truce existing between our two countries, the Dutch government has approached us with a proposal for a conference to resolve our current territorial and legal disputes.
---

Flavor text:
"So now the Dutch desire arbitration? No doubt they have their eyes firmly fixed on rightful Belgian soil. Though their ambition lie bare for all to see, we may have little choice in the matter. A refusal to compromise might harm our standing in Europe in ways we cannot easily amend."
---

| Is triggered by: Event The Belgian Question |
|---|
| Trigger conditions: None |
| Very well, agree to great power mediation. Activates journal entry London Conference for Netherlands and Belgium Participating Great Powers will vote on solution to be ratified by Belgium and Netherlands Every great power with a capital in Europe receives the event London Calling We shall not give an inch to the damned Dutch! Lose 80 relations with Netherlands Netherlands gains a negative event catalyst towards Belgium Lose 40 relations with every great power in Europe |

id

### London Calling

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.11. |
|---|---|

---

The unsettled nature of Belgian-Dutch relations have threatened European stability ever since 1830. A conference to settle the issue for good has now been called in London, with the great powers of Europe all invited to arbitrate.
---

Flavor text:
"For nearly a decade we have sought to bring these two parts to the table, and for nearly a decade we have been frustrated in our efforts. Now, be it by providence or by a stroke of luck we have them right where we want them. Let us not waste this opportunity, the stability of Europe depends on our success."
---

| Is triggered by: Event The Hague Call for a Conference |
|---|
| Trigger conditions: None |
| Let us settle this matter once and for all. Activates journal entry London Conference We have no interest in this squabble. Lose 20 relations with Netherlands and Belgium |

id

### London Conference

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.11. |
|---|---|

---

The great Powers have sent their delegations to London to decide on a solution to the unsolved border issue between Netherlands and Belgium.
[Number] of Great Powers are participating in the Conference. **Favour Belgium Claims** is backed by [Amount] total Prestige **Favour Dutch Claims** is backed by [Amount] total Prestige **Favour Twenty-Four Points** is backed by [Amount] total Prestige **Favour Alternate Partition** is backed by [Amount] total Prestige The conference will conclude in [6] months. The proposal with the most prestige supporting it will then be selected as the conference's official solution. **Result** [Result of the Conference]

We will automatically accept the outcome of the conference in [6] months.
---

| Visibility conditions: Only while active |  |
|---|---|
| Activated by: Either: Event The Hague Call for a Conference Event London Calling | Effects when activated: None |
| Entry buttons: Favour Belgian Claims Belgium is to receive the provinces of Limburg and Luxemburg in full. In order to compensate Netherlands for the loss of the two provinces, Belgium must assume the total public debt of the former United Kingdom of the Netherlands . Visible if: Is not Belgium or Netherlands Enabled if: Has not chosen a proposal Effects: Adds this country's prestige to this proposal Belgium gains 20 relations and a positive event catalyst with this country Netherlands loses 20 relations and gains a negative event catalyst with this country Favour Dutch Claims Netherlands is to receive the provinces of Limburg and Luxemburg in full. In order to compensate Belgium for the loss of the two provinces, Belgium must assume the total public debt of the former United Kingdom of the Netherlands . Visible if: Is not Belgium or Netherlands Enabled if: Has not chosen a proposal Effects: Adds this country's prestige to this proposal Netherlands gains 20 relations and a positive event catalyst with this country Belgium loses 20 relations and gains a negative event catalyst with this country Favour Twenty-Four Points The provinces of Limburg and Luxemburg will be partitioned between Belgium and Netherlands. In order to compenstate the German Federation for the loss of Western Luxemburg, Limbourg will be established as a Dutch subject and a nominal member of the German Confederation. Visible if: Is not Belgium or Netherlands Enabled if: Has not chosen a proposal Effects: Adds this country's prestige to this proposal Gain 10 relations with every German-speaking country in Germany and the Rhine regions Favour Alternate Partition Belgium will retain the entire province of Limburg, in exchange for Netherlands receiving the entirety of Luxemburg. Visible if: Is not Belgium or Netherlands Enabled if: Has not chosen a proposal Effects: Adds this country's prestige to this proposal Ratify the Treaty of London The agreed upon proposal is acceptable. Instruct our men in London to sign the document. Visible if: Is Belgium or Netherlands Enabled if: The London Conference has concluded. Effects: Ratifies the treaty. Should both Netherlands and Belgium agree, the treaty will then enter into effect. Refuse to sign This outcome does not serve [Country] interests. We will not put our names to this scrap of paper. Visible if: Is Belgium or Netherlands Enabled if: The London Conference has concluded. Effects: Lose 40 relations with every great power in Europe |  |
| *Belgium is to receive the provinces of Limburg and Luxemburg in full. In order to compensate Netherlands for the loss of the two provinces, Belgium must assume the total public debt of the former United Kingdom of the Netherlands .* |  |
| **Visible if:** Is not Belgium or Netherlands |  |
| **Enabled if:** Has not chosen a proposal |  |
| **Effects:** Adds this country's prestige to this proposal Belgium gains 20 relations and a positive event catalyst with this country Netherlands loses 20 relations and gains a negative event catalyst with this country |  |
| *Netherlands is to receive the provinces of Limburg and Luxemburg in full. In order to compensate Belgium for the loss of the two provinces, Belgium must assume the total public debt of the former United Kingdom of the Netherlands .* |  |
| **Visible if:** Is not Belgium or Netherlands |  |
| **Enabled if:** Has not chosen a proposal |  |
| **Effects:** Adds this country's prestige to this proposal Netherlands gains 20 relations and a positive event catalyst with this country Belgium loses 20 relations and gains a negative event catalyst with this country |  |
| *The provinces of Limburg and Luxemburg will be partitioned between Belgium and Netherlands. In order to compenstate the German Federation for the loss of Western Luxemburg, Limbourg will be established as a Dutch subject and a nominal member of the German Confederation.* |  |
| **Visible if:** Is not Belgium or Netherlands |  |
| **Enabled if:** Has not chosen a proposal |  |
| **Effects:** Adds this country's prestige to this proposal Gain 10 relations with every German-speaking country in Germany and the Rhine regions |  |
| *Belgium will retain the entire province of Limburg, in exchange for Netherlands receiving the entirety of Luxemburg.* |  |
| **Visible if:** Is not Belgium or Netherlands |  |
| **Enabled if:** Has not chosen a proposal |  |
| **Effects:** Adds this country's prestige to this proposal |  |
| *The agreed upon proposal is acceptable. Instruct our men in London to sign the document.* |  |
| **Visible if:** Is Belgium or Netherlands |  |
| **Enabled if:** The London Conference has concluded. |  |
| **Effects:** Ratifies the treaty. Should both Netherlands and Belgium agree, the treaty will then enter into effect. |  |
| *This outcome does not serve [Country] interests. We will not put our names to this scrap of paper.* |  |
| **Visible if:** Is Belgium or Netherlands |  |
| **Enabled if:** The London Conference has concluded. |  |
| **Effects:** Lose 40 relations with every great power in Europe |  |
| Completion conditions: Belgium and Netherlands have accepted the outcome of the Conference | Effects when completed: Trigger event London Conference Concludes |
| Failure conditions: Either: Either Belgium or Netherlands have rejected the outcome of the conference Hostilities have broken out between Belgium and Netherlands | Effects when failed: Triggers event Failure of the London Conference |
| After 6 months: The conference concludes Participating great powers that did not select a proposal select a random one The proposal with the most prestige backing it becomes the conference proposal Belgium and Netherlands are given 6 months to decide whether to ratify the proposal |  |
| 6 months after the conference concludes: Belgium and Netherlands automatically ratify the conference proposal if they did not reject it |  |

id

### London Conference Concludes

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.11. |
|---|---|

---

The conference has concluded, and [Result of the Conference].
---

Flavor text:
"European Powers Guarantee Peace and Stability. The newly ratified Treaty of London is a cornerstone of European peace; it solidifies Belgium`s neutrality and independence and marks a new chapter in European Diplomacy, one that prioritizes peace and mutual respect among nations. While the Dutch delegation... (cont. pp. 3-6)"
---

| Is triggered by: Completion of journal entry London Conference |
|---|
| Trigger conditions: None |
| For peace in our time, hurrah! Territory will be exchanged between Belgium and Netherlands in accordance with their treaty obligations. Belgium or Netherlands may take on the debt of the other, depending on outcome Every great power participant gains Guarantor of Peace Guarantor of Peace Country modifier +5% Influence for 5 years |

id

### Failure of the London Conference

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this infobox. It was last verified for version 1.11. |
|---|---|

---

With negotiations between Belgium and Netherlands having broken down in full, it would appear that a diplomatic solution to the Belgian question has eluded Europe once again.
---

Flavor text:
"As the delegation made their way of the Foreign Office and onto King Charles Street, the air of amicability that they so desperately tried to maintain could not even fool the doorman — much less each other. What this would mean for future Dutch-Belgian relation they could still not say, but that it would be bad? Now at last, there was something they could agree on."
---

| Is triggered by: Failure of the journal entry London Conference |
|---|
| Trigger conditions: None |
| What a waste of everybody`s time. 2% of pops become more radical |

## Formation

If Belgium ceases to exist, it can be released by any country that controls its capital, Flanders, and one of its other two core states: Wallonia and French Low Countries.

## Technology

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.11. |
|---|---|

Belgium is one of the most technologically advanced nations in the world. It begins with all era 1 technologies and several era 2 technologies researched.

| Production technology | Military technology | Society technology |
|---|---|---|
| Prospecting Intensive Agriculture Railways Distillation | Drydocks Screw Frigate Power of the Purse General Staff Napoleonic Warfare Percussion Cap | Law Enforcement Corporate Charters Central Banking Central Archives Colonization Egalitarianism Mass Communication Medical Degrees Dialectics Romanticism |

## Politics

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.11. |
|---|---|

Belgium is a constitutional monarchy, with King Leopold of Saxe-Coburg-Gotha supporting the Intelligentsia.

| Power Structure | Economy | Human Rights |  |  |  |
|---|---|---|---|---|---|
| Governance Principles | Monarchy | Economic System | Interventionism | Free Speech | Right of Assembly |
| Distribution of Power | Wealth Voting | Trade Policy | Mercantilism | Labor Rights | No Workers' Rights |
| Citizenship | Racial Segregation | Taxation | Per-Capita Taxation | Children's Rights | Child Labor Allowed |
| Church and State | Freedom of Conscience | Land Reform | Peasant Proprietorship | Rights of Women | Legal Guardianship |
| Bureaucracy | Elected Bureaucrats | Colonization | No Colonial Affairs | Welfare | No Social Security |
| Army Model | Professional Army | Policing | No Police | Migration | No Migration Controls |
| Navy Model | Merchant Navy | Education System | Religious Schools | Slavery | Slavery Banned |
| Internal Security | No Home Affairs | Health System | No Health System | Labor Associations | Anti-Strike Laws |

| Institution | Level |
|---|---|
| Education | 2 |

### Interest groups

Due to Belgium's
Wealth Voting law, the starting interest groups in
government can vary.
Belgium typically starts with the Intelligentsia and the Industrialists in government, as the Liberal Party. In opposition, the Catholic Church, Landowners, and Petite Bourgeoisie make up the Catholic Party, the Armed Forces the Patriotic Party, and the Rural Folk are unaffiliated with any party.

The Trade Unions are marginalized.

### Historical characters

| Name[wp 1] | Role | Interest Group | Ideology | Traits |
|---|---|---|---|---|
| [Leopold (I) of Saxe-Coburg-Gotha](http://en.wikipedia.org/wiki/Leopold_I_of_Belgium) | Ruler | Intelligentsia | Moderate | Tactful |
| [Leopold (II) of Saxe-Coburg-Gotha](http://en.wikipedia.org/wiki/Leopold_II_of_Belgium) | Heir | Petite Bourgeoisie | Royalist | Child |
| [Hippolyte Metdepenningen](http://en.wikipedia.org/wiki/Hippolyte_Metdepenningen) | Politician | Petite Bourgeoisie | Moderate | Political Operator, Cautious |
| [Barthélémy de Theux de Meylandt](http://en.wikipedia.org/wiki/Barth%C3%A9l%C3%A9my_de_Theux_de_Meylandt) | Politician | Catholic Church | Moderate | Experienced Political Operator, Cautious |
| [Charles de Brouckère](http://en.wikipedia.org/wiki/Charles_de_Brouck%C3%A8re) | Politician | Intelligentsia | Market Liberal | Master Bureaucrat, Literary |
| [Albert Joseph Goblet d'Alviella](http://en.wikipedia.org/wiki/Albert_Joseph_Goblet_d%27Alviella) | Politician | Armed Forces | Liberal | Celebrity Commander, Diplomat |
| [Félix de Muelenaere](http://en.wikipedia.org/wiki/F%C3%A9lix_de_Muelenaere) | Politician | Landowners | Moderate | Political Operator, Meticulous |
| [John Cockerill](http://en.wikipedia.org/wiki/John_Cockerill_(industrialist)) | Executive | Industrialists | Moderate | Ambitious, Political Operator, Basic Entrepreneur |

| Name[wp 1] | Role | Interest Group | Ideology | Traits | Rank |
|---|---|---|---|---|---|
| [André-Lambert Nypels](http://en.wikipedia.org/wiki/fr:Lambert_Nypels)[wp 2] | General | ![Undecided](/images/thumb/2/2d/Political_undecided.png/24px-Political_undecided.png) Random | ![Undecided](/images/thumb/2/2d/Political_undecided.png/24px-Political_undecided.png) Random | Open Terrain Commander, Cautious | Brigadier General |
| [Louis Évain](http://en.wikipedia.org/wiki/fr:Louis_%C3%89vain)[wp 2] | General | ![Undecided](/images/thumb/2/2d/Political_undecided.png/24px-Political_undecided.png) Random | ![Undecided](/images/thumb/2/2d/Political_undecided.png/24px-Political_undecided.png) Random | Trench Rat, Meticulous | Brigadier General |
| Joseph van Haverbeke | Admiral | Armed Forces | Moderate | Colonial Administrator, Brave | Commodore |

| Name[wp 1] | Type | Interest Group | Ideology | Traits | Conditions |
|---|---|---|---|---|---|
| [Albert-Florent-Joseph Prisse](http://en.wikipedia.org/wiki/Albert_Prisse) | General | Armed Forces | Reformer | Surveyor, Diplomat | Date between 1836.1.1 and 1855.1.1 |

### Diplomacy

Belgium and the [Netherlands](Netherlands.md) have a mutual rivalry, as well as a truce until May 1839. Belgium has a pro-country lobby towards Great Britain ().

Belgium's independence is guaranteed by [France](France.md) by the [treaty](Treaty.md) *Declaration of Liége*, which is bound for 10 years. Additionally, Belgium has a treaty with [Great Britain](Great Britain.md), the *Treaty of Reciprocity between Great Britain and Belgium*, where they have mutual trade priviliges, and () Great Britain has investment rights in Belgium. It is also bound for 10 years.

## Economy

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.11. |
|---|---|

| Statistic | Starting value |
|---|---|
| GDP | 3.0M |
| Population | 4.14M |
| Literacy | 41.6% |
| Standard of living | Impoverished (10.1) |

### States

| Name | Type | Homelands | Arable Land | Resources | State Traits |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Size | Uses |  |  |  |  |  |  |  |  |  |  |
| Flanders |  | Flemish | 90 | Wheat Farm Livestock Ranch | 23 | — | — | — | — | 5 |  |
| Wallonia |  | Wallonian | 55 | Wheat Farm Livestock Ranch | 17 | 80 | 60 | 30 | 30 | — | Borinage Coalfield +10% Coal Mines throughput |
| Gelre |  | Dutch | 40 | Rye Farm Livestock Ranch | 9 | 40 | — | — | — | — | Rhine River +20 Infrastructure +5% Market access price impact |

### Industry and resources

**Industry**

Belgium starts with a fairly developed industrial sector, including Steel Mills. As one of the most technologically advanced starting countries, several advanced industries and production methods are in use or available.

**Resources**

Belgium starts with a large amount of coal and iron and a moderate amount of lead and sulfur in Wallonia. However, Belgium has no starting access to any agricultural resources or .

### Companies

The following [companies](Companies.md) are associated with Belgium or its starting states:

| Name[wp 1] / Ownership | Buildings | Industry charters | Prestige goods | Prosperity bonus | Requirements |
|---|---|---|---|---|---|
| [Compagnie du Congo](http://en.wikipedia.org/wiki/Compagnie_du_Congo_pour_le_Commerce_et_l%27Industrie) Partial Aristocrat | Iron Mines Logging Camps Rubber Plantations | Livestock Ranches Railway | ![No](/images/thumb/0/04/No.png/24px-No.png) | +15% Prestige +20% Rubber Industry employee mortality | Has Wallonian primary culture Country or its subject owns a state in the Congo geographic region with 5 levels of Rubber Plantations |
| [Société anonyme John Cockerill](http://en.wikipedia.org/wiki/Soci%C3%A9t%C3%A9_anonyme_John_Cockerill) | Motor Industries Steel Mills Tooling Workshops | Iron Mines | Precision Tools | **+10%** Railway throughput | Belgium starts with this company established Wallonia or Flanders is incorporated with 5 levels of Steel Mills |
| [Société Franco-Belge](http://en.wikipedia.org/wiki/Soci%C3%A9t%C3%A9_Franco-Belge) | Motor Industries Railway | Steel Mills | ![No](/images/thumb/0/04/No.png/24px-No.png) | +5% Infrastructure | **Wallonia** or **Flanders** is incorporated with 5 levels of Motor Industries |

## Military

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this section. It was last verified for version 1.11. |
|---|---|

Belgium has the Professional Army law.

Belgium starts with 24 Battalions and can raise up to 13 Conscripts. All Barracks use General Training. The battalions comprise a single army.

| Army name | Battalions | Generals | HQ region |
|---|---|---|---|
| 1st Belgian Army | 15 Line Infantry 3 Cannon Artillery 1 Hussar, 2 Dragoons, 1 Cuirassier | André-Lambert Nypels Louis Évain | Rhine |

Belgium starts with 1 Flotilla. The Naval Base uses Power of the Purse.

| Navy name | Flotillas | Admirals | HQ region |
|---|---|---|---|
| Marine Royale | 1 Frigates | Joseph van Haverbeke | Rhine |

## Strategy and guides

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | Please help with verifying or updating this guide. It was last verified for version 1.11. |
|---|---|

The below is
one of many
player suggested strategies for
Belgium
. Bear in mind, due to the dynamic nature of the game, it may unfold differently for other players.

### General overview

Belgium starts out as one of the strongest Minor Powers in the game. It has the best technology in the game, even having access to Railways on game start. It has a number of urban industries such as Steel Mills and has ready access to every single non-discoverable resource in the game, all concentrated in one state (Wallonia, which is a contender for the best state in Europe). On top of that it already has established the company [John Cockerill](List of flavored companies.md), which is one of the best companies for kickstarting industrialization in the game. It starts out sandwiched next to three Great Powers, but with cordial relations with all three and very little likelihood of realistically being invaded.

Belgium also has one of the most liberal laws at game start, as well as a relatively weak landowners IG. It is very easy to move on to laws like Laissez-Faire and Proportional Taxation in the future with their political setup. Its military is relatively small, but large enough to establish a colonial empire by attacking smaller unrecognized countries, especially with the technological advantage.

Belgium is poised to be a strong player on continental Europe that can punch well above its weight, and can secure itself a large colonial empire in Africa and other continents.

### Early game diplomacy and the London Conference

Immediately declare rivalries on small, irrelevant German minors (or even [Spain](Spain.md)) and begin improving relations with the four Great Powers in your area – [Great Britain](Great Britain.md), [France](France.md), [Prussia](Prussia.md), and [Austria](Austria.md).

The London Conference will be convened around 1838. This is a journal event where the Great Powers will decide how to partition Luxembourg (the state of Wallonia) and Limburg (the state of Gelre). There are four potential outcomes, and only one of them (Belgian Claims) ends with you retaining both. However, the Great Power AIs are *heavily* weighted to select the other three options. This means that the only winning move is to **not play** - when the London Conference fires, immediately reject it. This will decrease relations with all the powers in the region, which is why it's important to improve relations with them. Some of them may flip their diplomatic attitude to Cautious because of the diplomatic catalyst, but as long as some of them (especially Great Britain) are still Protective or Genial, that's okay.

### France's natural borders

|  | Available only with the [Voice of the People](Voice of the People.md) DLC enabled. |
|---|---|

If France activates the [Natural Borders](French content.md) journal entry and accepts the event, it will receive claims on Flanders and Wallonia and may roll a Belligerent attitude towards you. Needless to say, this makes France extremely dangerous. It is advised to seek an ally or defensive pact with a GP rival of France (usually Great Britain). You can also reset France's diplomatic attitude towards you by siding with them on a Diplomatic Play (for example, when they try to invade an Algerian minor).

## Name and flag

Belgium has multiple [dynamic flags](List of flags.md) and a [dynamic name](Dynamic country names.md).

| Flag | Name | Governance Principles | Other Conditions |
|---|---|---|---|
|  | Belgium | Fallback |  |
|  | Monarchy | Autocracy or Single-Party State |  |
|  | United Belgian States | Either: Presidential Republic Parliamentary Republic Corporate State | — |
|  | Autocracy or Single-Party State |  |  |
|  | Autocracy, Oligarchy, or Single-Party State Corporate State, or ruler has Fascist or Integralist ideology |  |  |
|  | Belgium | Council Republic | — |

## References

---

Wikipedia link references:

1. ↑ 1.0 1.1 1.2 1.3 Links to English Wikipedia article
2. ↑ 2.0 2.1 Links to French Wikipedia article

Return to top
Countries
by Region
Tabber需要JavaScript才能使用。
| Balkans/Eastern Europe/Russia regions | [Chechnya](Chechnya.md) [Circassia](Circassia.md) [Croatia](Croatia.md) [Greece](Greece.md) [Hungary](Hungary.md) [Ionian Islands](Ionian Islands.md) [Krakow](Krakow.md) [Moldavia](Moldavia.md) [Montenegro](Montenegro.md) [Russia](Russia.md) [Serbia](Serbia.md) [Transylvania](Transylvania.md) [United Baltic Provinces](United Baltic Provinces.md) [Wallachia](Wallachia.md) |
|---|---|

| Central Europe region | [Anhalt](Anhalt.md) [Austria](Austria.md) [Baden](Baden.md) [Bavaria](Bavaria.md) [Bremen](Bremen.md) [Brunswick](Brunswick.md) [Frankfurt](Frankfurt.md) [Hamburg](Hamburg.md) [Hanover](Hanover.md) [Hesse](Hesse.md) [Hesse-Kassel](Hesse-Kassel.md) [Hohenzollern](Hohenzollern.md) [Holstein](Holstein.md) [Lippe](Lippe.md) [Lübeck](Lübeck.md) [Mecklenburg](Mecklenburg.md) [Mecklenburg-Strelitz](Mecklenburg-Strelitz.md) [Nassau](Nassau.md) [Oldenburg](Oldenburg.md) [Prussia](Prussia.md) [Saxe-Coburg-Gotha](https://vic3.paradoxwikis.com/Saxe-Coburg-Gotha) [Saxe-Meiningen](https://vic3.paradoxwikis.com/Saxe-Meiningen) [Saxe-Weimar](https://vic3.paradoxwikis.com/Saxe-Weimar) [Saxony](Saxony.md) [Schaumburg-Lippe](Schaumburg-Lippe.md) [Schleswig](Schleswig.md) [Schwarzburg](https://vic3.paradoxwikis.com/Schwarzburg) [Switzerland](Switzerland.md) [Waldeck](Waldeck.md) [Württemberg](Württemberg.md) |
|---|---|

| Northern/Western Europe regions | Belgium [Denmark](Denmark.md) [Finland](Finland.md) [France](France.md) [Great Britain](Great Britain.md) [Luxembourg](Luxembourg.md) [Netherlands](Netherlands.md) [Norway](Norway.md) [Sweden](Sweden.md) |
|---|---|

| Southern Europe region | [Lucca](Lucca.md) [Modena](Modena.md) [Papal States](Papal States.md) [Parma](Parma.md) [Portugal](Portugal.md) [Sardinia-Piedmont](Sardinia-Piedmont.md) [Spain](Spain.md) [Carlist Spain](Carlist Spain.md) [Tuscany](Tuscany.md) [Two Sicilies](Two Sicilies.md) |
|---|---|

| Formable | [Byzantium](Byzantium.md) [Central Europe](Central Europe.md) [Confederation of the Rhine](Confederation of the Rhine.md) [Czechoslovakia](Czechoslovakia.md) [Danubian State](Danubian State.md) [England](England.md) [Galicia-Lodomeria](Galicia-Lodomeria.md) [Germany](Germany.md) [Iberia](Iberia.md) [Ireland](Ireland.md) [Italy](Italy.md) [Poland](Poland.md) [Poland-Lithuania](Poland-Lithuania.md) [North German Federation](North German Federation.md) [Romania](Romania.md) [Scandinavia](Scandinavia.md) [South German Federation](South German Federation.md) [United Netherlands](United Netherlands.md) [Yugoslavia](Yugoslavia.md) |
|---|---|

| Central/Northern/Western Europe Releasable | [Bohemia](https://vic3.paradoxwikis.com/Bohemia) [Brittany](Brittany.md) [Cornwall](https://vic3.paradoxwikis.com/Cornwall) [Flanders](https://vic3.paradoxwikis.com/Flanders) [Greenland](Greenland.md) [Iceland](Iceland.md) [Jan Mayen](Jan Mayen.md) [Karelia](Karelia.md) [Pomerania](Pomerania.md) [Rhineland](https://vic3.paradoxwikis.com/Rhineland) [Sapmi](Sapmi.md) [Scania](https://vic3.paradoxwikis.com/Scania) [Scotland](Scotland.md) [Sorbia](Sorbia.md) [Ulster](https://vic3.paradoxwikis.com/Ulster) [Wales](Wales.md) [Wallonia](https://vic3.paradoxwikis.com/Wallonia) [Westphalia](Westphalia.md) |
|---|---|

| Balkans/Southern Europe Reasable | [Albania](Albania.md) [Andalusia](https://vic3.paradoxwikis.com/Andalusia) [Aragon](Aragon.md) [Asturias](Asturias.md) [Banat](Banat.md) [Bosnia-Herzegovina](https://vic3.paradoxwikis.com/Bosnia-Herzegovina) [Bulgaria](Bulgaria.md) [Castile](https://vic3.paradoxwikis.com/Castile) [Catalonia](Catalonia.md) [Corsica](Corsica.md) [Crete](Crete.md) [Galicia](Galicia.md) [León](León.md) [Lombardia](https://vic3.paradoxwikis.com/Lombardia) [Malta](Malta.md) [Navarra](Navarra.md) [Occitania](Occitania.md) [Savoy](Savoy.md) [Slovakia](https://vic3.paradoxwikis.com/Slovakia) [Slovenia](https://vic3.paradoxwikis.com/Slovenia) [Trieste](https://vic3.paradoxwikis.com/Trieste) [Venice](https://vic3.paradoxwikis.com/Venice) |
|---|---|

| Eastern Europe/Russia Releasable | [Bashkiria](Bashkiria.md) [Belarus](Belarus.md) [Chuvashia](Chuvashia.md) [Crimea](Crimea.md) [Dagestan](Dagestan.md) [Danzig](Danzig.md) [Don Cossack Host](Don Cossack Host.md) [Erzya-Moksha](Erzya-Moksha.md) [Estonia](https://vic3.paradoxwikis.com/Estonia) [Idel-Ural](Idel-Ural.md) [Kalmykia](Kalmykia.md) [Latvia](https://vic3.paradoxwikis.com/Latvia) [Lithuania](https://vic3.paradoxwikis.com/Lithuania) [Mari El](Mari El.md) [Mountain Republic](Mountain Republic.md) [Tatarstan](Tatarstan.md) [Udmurtia](Udmurtia.md) [Ukraine](Ukraine.md) |
|---|---|

Template:Country navbox/Africa
Template:Country navbox/MiddleEast
Template:Country navbox/India
Template:Country navbox/AsiaEast
Template:Country navbox/AmericaNorth
Template:Country navbox/Other
**Notes:** This table lists playable countries divided by superregion and region. Starting countries are listed by the region of their capital state, with formable and releasable countries not present at the start listed separately by superregion. Decentralized (non-playable) and special cases are listed separately.
