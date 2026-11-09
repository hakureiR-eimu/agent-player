---
title: Law modding
source: https://vic3.paradoxwikis.com/Law_modding
pageid: 6770
categories: [Potentially_outdated, 1.10, Modding]
fetched: 2026-10-27
---
Please help with verifying or updating older sections of this article. At least some were last verified for [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10.

[Laws](Laws.md) in Victoria 3 provide for making major changes to a country. Modding laws typically involves modifying several related concepts.

## Law group definition

Law groups provide certain basic details for laws, such as enactment time and chance of movements. For each law group, only a single law can be active at a time.

Law groups are defined in /Victoria 3/game/common/law_groups. The basic definition is a script name, category, and movement chances. For example:

```
lawgroup_taxation = {
	law_group_category = economy
	
	progressive_movement_chance = 1.5
	regressive_movement_chance = 0.15
}
```

The three categories are `power_structure`, `economy`, and `human_rights`. Script names can be anything and the script name also generates localization keys: `[script name]` and `[script_name]_desc`. The law group is used for ideologies as well as triggers, so a clear, but unique name is good to use.

The movement chances are multipliers to the base chance for a movement to form related to laws in this group.

Additional characteristics can be scripted for each law group:

| Characteristic | Description | Value type |
|---|---|---|
| base_enactment_days | Changes the default number of days between enactment checks Default amount is set by define: LAW_ENACTMENT_DEFAULT_BASE_DAYS | integer |
| enactment_approval_mult | Changes the amount of approval affected by law changes in this group | float |
| affected_by_regime_change | Laws in this group are changed by the regime change effect | boolean |
| change_allowed_trigger | Trigger block that must return true to allow manual law changes in this group | trigger block |
| linked_social_hierarchy | Laws in this group only appear for countries with the specified social hierarchy | social hierarchy |

## Law definition

Laws are defined in /Victoria 3/game/common/laws. Each law has certain required elements and a number of optional elements. A basic definition requires the following: a script name, a group, an icon, a progressiveness score, a pop support value block, an ai_will_do trigger block, and an ai_enact_weight_modifier value block

```
law_no_health_system = {
	group = lawgroup_health_system
	icon = "gfx/interface/icons/law_icons/no_health_system.dds"
	
	progressiveness = 0
	
	# AI shouldn't try to abolish institutions
	ai_will_do = {
		always = no
	}

	ai_enact_weight_modifier = { #Petitions
		value = 0
		
		if = {
			limit = { ai_has_enact_weight_modifier_journal_entries = yes }
			add = 750
		}
	}
}
```

Like law groups, the script name can be anything and generates the localization keys `[script_name]` and `[script_name]_desc`

Laws may have additional blocks and elements as well:

| Element | Description |
|---|---|
| group | which law group this law belongs to |
| icon | Path to a .dds image file |
| progressiveness | an integer that rates laws relative to each other; used for other script |
| modifier | a modifier block added by the law |
| institution | [institution](Institution modding.md) enabled by the law |
| institution_modifier | a modifier block added to the institution enabled by the law |
| unlocking_technologies | a list of [technologies](Technology modding.md) that must be researched to enact the law functionally a trigger shorthand for "has any of these technologies" |
| unlocking_laws | a list of laws, one of which must be enacted to enact this law functionally a trigger shorthand for "has any of these laws" used with base laws |
| requires_law_or | a list of laws, one of which must be enacted to enact this law functionally a trigger shorthand for "has any of these laws" used with variant laws |
| disallowing_laws | a list of laws which block enacting this law functionally a trigger shorthand for "has none of these laws" |
| can_enact | a trigger block that must return true to enact this law |
| parent | another law which provides ideology stances to this law; this law also counts as a variant of the law for triggers |
| is_visible | a trigger block that must return true for this law to appear in the list of laws for a country |
| on_enact | an effect block that is done when the law is successfully enacted |
| on_activate | an effect block that is done when the law becomes the active law for any reason fired in addition to on_enact, when successfully enacted |
| on_deactivate | an effect block that is done when the law stops being the active law for any reason |
| tax_modifier_[level] | a modifier block that adds effects to the given taxation level Levels are `very_low`, `low`, `medium`, `high`, and `very_high` |
| can_impose | a trigger block which determines whether a country can impose this law on another |
| ai_impose_chance | a script value that determines how likely the AI is to impose this law when it can |
| ai_will_do | a trigger block which determines whether the AI will try to enact this law |
| ai_enact_weight_modifier | a script value that dermines how likely the AI is to try to enact this law |

## Other effects

Law effects can also be enabled in other files by referencing the law. Production methods are one such example.

## Law script documentation

The following [effects](Effect.md), [event targets](Event target.md), and [triggers](Trigger.md) can be used in law scope.

| Effect | Description | Example | Targets |
|---|---|---|---|
| every_possible_amendment_type | Iterate through amendment types that could be added to the scoped law | every_possible_amendment_type = { limit = { <triggers> } #optional <effects> } | amendment_type |
| every_scope_amendment | Iterate through amendments of the scoped law | every_scope_amendment = { limit = { <triggers> } #optional <effects> } | amendment |
| ordered_possible_amendment_type | Iterate through amendment types that could be added to the scoped law | ordered_possible_amendment_type = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | amendment_type |
| ordered_scope_amendment | Iterate through amendments of the scoped law | ordered_scope_amendment = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | amendment |
| random_possible_amendment_type | Iterate through amendment types that could be added to the scoped law | random_possible_amendment_type = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | amendment_type |
| random_scope_amendment | Iterate through amendments of the scoped law | random_scope_amendment = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | amendment |

| Trigger | Description | Example | Targets |
|---|---|---|---|
| any_possible_amendment_type | Iterate through amendment types that could be added to the scoped law | any_possible_amendment_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | amendment_type |
| any_scope_amendment | Iterate through amendments of the scoped law | any_scope_amendment = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | amendment |
| can_be_enacted | Checks if a law could be enacted by its country, considering its current situation | can_be_enacted = yes | boolean |
| is_reasonable_law_for_petition | Checks if a law is considered reasonable for a government petition to enact it | is_reasonable_law_for_petition = yes | boolean |
| law_approved_by | Checks whether the scoped law is approved by an interest group | law_approved_by = ig_rural_folk |  |
| law_is_available | Checks if a law is available for its country, considering its current situation. Like can_be_enacted, but ignores government support | law_is_available = yes | boolean |

| Event target | Description | To scope |
|---|---|---|
| currently_active_law_in_group | Scope from a law to the currently active law in that group | law |
| imposer_of_law | Scope from a country to the country currently imposing a law on them | country |
| law_type | Scope to a law type from its name (law_type:law_protected_speech) or from a scoped law | law_type |
| owner | Scope to the owner country of object | country |
| type | Scope from an object to its type | amendment_type, building_type, company_type, diplomatic_play_type, harvest_condition_type, institution_type, interest_group_type, law_type, political_movement_type, ship_type, strait_type |

### Law GUI script

Main article:
GUI script
| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessApprovingIGs |  | Unknown | Category: const |
| AccessDisapprovingIGs |  | Unknown | Category: const |
| AccessNeutralIGs |  | Unknown | Category: const |
| AccessSelf |  | Law | Category: const |
| AppliesTo | Country | bool |  |
| CannotEnactDesc |  | CString |  |
| GetActiveAmendments |  | Unknown | Category: nonconst |
| GetActiveGroupLaw |  | Law | Category: nonconst |
| GetAffectedMovementsFromCancelEnact |  | Unknown | Category: nonconst |
| GetAffectedMovementsFromStartEnact |  | Unknown | Category: nonconst |
| GetAllAmendments |  | Unknown | Category: nonconst |
| GetCancelTooltip |  | CString | Category: nonconst |
| GetCheckpointAdvanceBreakdown |  | CString | Category: nonconst |
| GetCheckpointAdvanceChance |  | CFixedPoint | Category: nonconst |
| GetCheckpointAdvanceWithImpositionBreakdown |  | CString | Category: nonconst |
| GetCheckpointAdvanceWithImpositionChance |  | CFixedPoint | Category: nonconst |
| GetCheckpointBaseDays |  | int32 | Category: nonconst |
| GetCheckpointDebateBreakdown |  | CString | Category: nonconst |
| GetCheckpointDebateChance |  | CFixedPoint | Category: nonconst |
| GetCheckpointDebateWithImpositionBreakdown |  | CString | Category: nonconst |
| GetCheckpointDebateWithImpositionChance |  | CFixedPoint | Category: nonconst |
| GetCheckpointEndDateString |  | CString | Category: nonconst |
| GetCheckpointProgress |  | CFixedPoint | Category: nonconst |
| GetCheckpointRemainingDays |  | int32 | Category: nonconst |
| GetCheckpointStallBreakdown |  | CString | Category: nonconst |
| GetCheckpointStallChance |  | CFixedPoint | Category: nonconst |
| GetCheckpointStallWithImpositionBreakdown |  | CString | Category: nonconst |
| GetCheckpointStallWithImpositionChance |  | CFixedPoint | Category: nonconst |
| GetCheckpointSuccessBreakdown |  | CString | Category: nonconst |
| GetCheckpointSuccessChance |  | CFixedPoint | Category: nonconst |
| GetCheckpointSuccessWithImpositionBreakdown |  | CString | Category: nonconst |
| GetCheckpointSuccessWithImpositionChance |  | CFixedPoint | Category: nonconst |
| GetCheckpointTotalDays |  | int32 | Category: nonconst |
| GetCheckpointTotalDaysBreakdown |  | CString | Category: nonconst |
| GetCountry |  | Country | Category: nonconst |
| GetCurrentEnactmentPhaseKey |  | CString | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetDailyProgress |  | CFixedPoint | Category: nonconst |
| GetDesc |  | CString | Category: nonconst |
| GetEnactmentLastCheckpointDate |  | Date | Category: nonconst |
| GetEnactmentLastCheckpointResult |  | CString | Category: nonconst |
| GetEnactmentPhase |  | int32 | Category: nonconst |
| GetEnactmentPhaseKey | Unknown | CString | Category: nonconst |
| GetEnactmentSetbackCount |  | int32 | Category: nonconst |
| GetExilesThatWouldJoinMovementSupportingLaw |  | Unknown | Category: nonconst |
| GetExilesThatWouldStartMovementSupportingLaw |  | Unknown | Category: nonconst |
| GetFlavor |  | CString | Category: nonconst |
| GetFullName |  | CString | Category: nonconst |
| GetFullNameWithStatus |  | CString | Category: nonconst |
| GetGroup |  | LawGroup | Category: nonconst |
| GetGroupName |  | CString | Category: nonconst |
| GetIGsApproveList |  | CString | Category: nonconst |
| GetIGsDisapproveList |  | CString | Category: nonconst |
| GetIGsEnactmentList |  | CString | Category: nonconst |
| GetIGsUndecidedList |  | CString | Category: nonconst |
| GetIGsWithApprovalChanges |  | Unknown | Category: nonconst |
| GetInstitution |  | Institution | Category: nonconst |
| GetInstitutionModifier |  | Modifier | Category: nonconst |
| GetInstitutionTooltip |  | CString | Category: nonconst |
| GetInstitutionType |  | InstitutionType | Category: nonconst |
| GetLawAlternatives |  | Unknown | Category: nonconst |
| GetLawType |  | LawType | Category: nonconst |
| GetMarginalizedIGsWithApprovalChanges |  | Unknown | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetNextEnactmentPhaseKey |  | CString | Category: nonconst |
| GetNumIGsApprove |  | uint32 | Category: nonconst |
| GetNumIGsDisapprove |  | uint32 | Category: nonconst |
| GetNumIGsUndecided |  | uint32 | Category: nonconst |
| GetNumSupportingInterestGroups |  | int32 | Category: nonconst |
| GetOnActivateDesc |  | CString | Category: nonconst |
| GetOnDeactivateDesc |  | CString | Category: nonconst |
| GetOnEnactDesc |  | CString | Category: nonconst |
| GetOnImposeDesc |  | CString | Category: nonconst |
| GetPercentPolStrApprove |  | CFixedPoint | Category: nonconst |
| GetPercentPolStrDisapprove |  | CFixedPoint | Category: nonconst |
| GetPercentPolStrUndecided |  | CFixedPoint | Category: nonconst |
| GetPreviousEnactmentPhaseKey |  | CString | Category: nonconst |
| GetRadicalismDriftTargetOnMovementFromCancelEnact | PoliticalMovement | CFixedPoint | Category: nonconst |
| GetRadicalismDriftTargetOnMovementFromStartEnact | PoliticalMovement | CFixedPoint | Category: nonconst |
| GetRadicalismEffectOnMovementFromCancelEnact | PoliticalMovement | CFixedPoint | Category: nonconst |
| GetRadicalismEffectOnMovementFromStartEnact | PoliticalMovement | CFixedPoint | Category: nonconst |
| GetReplacedLawEffect |  | CString | Category: nonconst |
| GetSupportingInterestGroupsBreakdown |  | CString | Category: nonconst |
| GetSupportingInterestGroupsSummary |  | CString | Category: nonconst |
| GetTexture |  | Unknown | Category: nonconst |
| GetTooltip |  | CString | Category: nonconst |
| GetTooltipNoRequirements |  | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetTypeDesc |  | CString | Category: nonconst |
| HasEnactmentLastCheckpoint |  | bool |  |
| HasInstitution |  | bool |  |
| HasNecessaryLaws |  | bool |  |
| HasNecessaryTech |  | bool |  |
| IsActive |  | bool |  |
| IsBeingEnacted |  | bool |  |
| IsMissingSupport |  | bool |  |
| IsSelected |  | bool |  |
| IsSupported |  | bool |  |
| IsValid |  | bool |  |
| IsVisible |  | bool |  |
| MakeScope |  | Scope |  |
| PredictApprovalChangesDuringEnactmentDesc |  | CString |  |
| PredictLegitimacyChangeToEnact |  | int32 |  |
| PredictLegitimacyChangeToEnactDesc |  | CString |  |
| PredictMovementLoyalistsFromEnactmentDesc |  | CString |  |
| PredictRadicalismChangesFromCancellationDesc |  | CString |  |
| PredictRadicalismChangesFromEnactmentDesc |  | CString |  |
| Select |  | void |  |
| Self |  | Law |  |
| StartEnacting |  | Command |  |
| StartImposing |  | Command |  |
| StopEnacting |  | Command |  |

| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessSelf |  | LawGroup | Category: const |
| GetDesc |  | CString | Category: nonconst |
| GetFirstInstitutionType |  | InstitutionType | Category: nonconst |
| GetKey |  | CString | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetNumEnactable |  | int32 | Category: nonconst |
| GetNumImposeOptions | Country | int32 | Category: nonconst |
| GetNumPotentialEnactable |  | int32 | Category: nonconst |
| GetTexture |  | Unknown | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| Self |  | LawGroup |  |

| Function | Arguments | Output | Description |
|---|---|---|---|
| AccessSelf |  | LawType | Category: const |
| GetAdditionalEffectDesc |  | CString | Category: nonconst |
| GetBlockingRequirements | Country | CString | Category: nonconst |
| GetCustom | CustomLocalization | CString | Category: nonconst |
| GetDesc |  | CString | Category: nonconst |
| GetEffectDesc | Country | CString | Category: nonconst |
| GetFullName |  | CString | Category: nonconst |
| GetFullNameWithStatus | Unknown | CString | Category: nonconst |
| GetGroup |  | LawGroup | Category: nonconst |
| GetName |  | CString | Category: nonconst |
| GetNameNoFormatting |  | CString | Category: nonconst |
| GetParentLawType |  | LawType | Category: nonconst |
| GetRequirements | Unknown | CString | Category: nonconst |
| GetTexture |  | Unknown | Category: nonconst |
| GetTooltip | Country | CString | Category: nonconst |
| GetTooltipTag |  | CString | Category: nonconst |
| GetTypeDesc |  | CString | Category: nonconst |
| GetUnlocks |  | CString | Category: nonconst |
| MakeScope |  | Scope |  |
| Self |  | LawType |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| GetActiveGroupLaw |  | Law | Category: nonconst |
| GetCheckpointEndDate |  | Date | Category: nonconst |
| GetCountry |  | Country | Category: nonconst |
| GetEnactmentLastCheckpointDate |  | Date | Category: nonconst |
| GetGroup |  | LawGroup | Category: nonconst |
| GetInstitution |  | Institution | Category: nonconst |
| GetInstitutionModifier |  | Modifier | Category: nonconst |
| GetInstitutionType |  | InstitutionType | Category: nonconst |
| GetLawType |  | LawType | Category: nonconst |
| MakeScope |  | Scope |  |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| GetCurrentlyActive |  | Law | Category: nonconst |
| GetCurrentlyEnacting |  | Law | Category: nonconst |
| GetFirstInstitutionType |  | InstitutionType | Category: nonconst |

| Promote | Arguments | Output | Description |
|---|---|---|---|
| GetGroup |  | LawGroup | Category: nonconst |
| GetParentLawType |  | LawType | Category: nonconst |
| MakeScope |  | Scope |  |

## References

Modding
Return to top
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • Laws • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| Map | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • [States](State modding.md) |
|---|---|

| Interface | [Interface](Interface modding.md) • [GUI script](GUI script.md) • [Localization](Localization.md) • [Customizable localization](Localization.md) • [Script localization](Script localization.md) |
|---|---|

| Graphics | [3D Models](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|

| Audio | Music • [Sound](Sound modding.md) |
|---|---|

| Other | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| Guides | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|
