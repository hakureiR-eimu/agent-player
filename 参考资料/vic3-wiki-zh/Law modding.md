---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Law modding
source: https://vic3.paradoxwikis.com/Law_modding
pageid: 6770
categories: [Potentially_outdated, 1.10, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。其中至少有一部分最后是在 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10 下核实的。

《维多利亚3》中的[法律](Laws.md)（Law）用于对国家进行重大变革。修改法律通常涉及修改若干相关概念。

## 法律组定义（Law group definition）

法律组为法律提供一些基本细节，例如颁布时间和政治运动出现的概率。每个法律组在同一时间只能有一条法律生效。

法律组定义于 /Victoria 3/game/common/law_groups。基本定义包括脚本名、类别和运动概率。例如：

```
lawgroup_taxation = {
	law_group_category = economy
	
	progressive_movement_chance = 1.5
	regressive_movement_chance = 0.15
}
```

三个类别分别是 `power_structure`、`economy` 和 `human_rights`。脚本名可以是任意内容，且脚本名还会生成本地化键：`[script name]` 和 `[script_name]_desc`。法律组会被意识形态以及 trigger 使用，因此建议使用清晰但唯一的名称。

运动概率是该组法律相关运动形成基础概率的乘数。

每个法律组还可以脚本化以下附加特性：

| 特性 | 说明 | 值类型 |
|---|---|---|
| base_enactment_days | 修改颁布检查之间间隔天数的默认值默认值由 define 设定：LAW_ENACTMENT_DEFAULT_BASE_DAYS | 整数 |
| enactment_approval_mult | 修改该组法律变化所影响的认可度数值 | 浮点数 |
| affected_by_regime_change | 该组的法律会受政权更迭（regime change）effect 的影响 | 布尔值 |
| change_allowed_trigger | 必须返回 true 才允许手动更改该组法律的 trigger 块 | trigger 块 |
| linked_social_hierarchy | 该组的法律只对具有指定社会等级的国家显示 | 社会等级 |

## 法律定义（Law definition）

法律定义于 /Victoria 3/game/common/laws。每条法律都有若干必需元素和一些可选元素。基本定义需要以下内容：脚本名、所属组、图标、进步性分数、人口支持度数值块、ai_will_do trigger 块以及 ai_enact_weight_modifier 数值块

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

与法律组一样，脚本名可以是任意内容，并生成本地化键 `[script_name]` 和 `[script_name]_desc`

法律还可以有附加的块和元素：

| 元素 | 说明 |
|---|---|
| group | 该法律所属的法律组 |
| icon | .dds 图像文件的路径 |
| progressiveness | 一个用于在法律之间进行相对评级 的整数；供其他脚本使用 |
| modifier | 该法律添加的 modifier 块 |
| institution | 该法律启用的[机构](Institution modding.md)（Institution） |
| institution_modifier | 添加到该法律所启用机构上的 modifier 块 |
| unlocking_technologies | 颁布该法律前必须研究完成的一组[技术](Technology modding.md)功能上等同于“拥有其中任一技术”的 trigger 简写 |
| unlocking_laws | 一组法律，其中之一必须已颁布才能颁布该法律功能上等同于“拥有其中任一法律”的 trigger 简写与基础法律（base laws）配合使用 |
| requires_law_or | 一组法律，其中之一必须已颁布才能颁布该法律功能上等同于“拥有其中任一法律”的 trigger 简写与变体法律（variant laws）配合使用 |
| disallowing_laws | 一组会阻止颁布该法律的法律功能上等同于“不拥有其中任何法律”的 trigger 简写 |
| can_enact | 必须返回 true 才能颁布该法律的 trigger 块 |
| parent | 另一条法律，为该法律提供意识形态立场；该法律在 trigger 中也被视为那条法律的变体 |
| is_visible | 必须返回 true 该法律才会出现在国家法律列表中的 trigger 块 |
| on_enact | 法律成功颁布时执行的 effect 块 |
| on_activate | 法律因任何原因成为现行法律时执行的 effect 块在成功颁布时，会与 on_enact 一同触发 |
| on_deactivate | 法律因任何原因不再成为现行法律时执行的 effect 块 |
| tax_modifier_[level] | 为指定税收等级添加效果的 modifier 块等级为 `very_low`、`low`、`medium`、`high` 和 `very_high` |
| can_impose | 决定一个国家能否将该法律强加于他国的 trigger 块 |
| ai_impose_chance | 决定 AI 在有能力时将该法律强加于他国的可能性的 script value |
| ai_will_do | 决定 AI 是否会尝试颁布该法律的 trigger 块 |
| ai_enact_weight_modifier | 决定 AI 尝试颁布该法律的可能性的 script value |

## 其他效果

法律效果也可以通过引用该法律在其他文件中启用。生产方式（Production methods）就是这样一个例子。

## 法律脚本文档

以下[effect](Effect.md)、[event target](Event target.md)和[trigger](Trigger.md)可在法律 scope 中使用。

| Effect | 说明 | 示例 | 目标 |
|---|---|---|---|
| every_possible_amendment_type | 遍历可添加到 scope 法律的修正案类型 | every_possible_amendment_type = { limit = { <triggers> } #optional <effects> } | amendment_type |
| every_scope_amendment | 遍历 scope 法律的修正案 | every_scope_amendment = { limit = { <triggers> } #optional <effects> } | amendment |
| ordered_possible_amendment_type | 遍历可添加到 scope 法律的修正案类型 | ordered_possible_amendment_type = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | amendment_type |
| ordered_scope_amendment | 遍历 scope 法律的修正案 | ordered_scope_amendment = { limit = { <triggers> } #optional order_by = script_value #determines ordering of scopes by comparison position = int #optional, default 0; selects scope from ordering, 0-indexed min = int #optional, default 0; sets "top" position to return, 0-indexed max = script_value #optional, default 1/inf; number of scopes to return, 1 if min isn't specified, inf if it is. check_range_bounds = no #optional; If you don't want an error logged if the list is smaller than the min/max <effects> } | amendment |
| random_possible_amendment_type | 遍历可添加到 scope 法律的修正案类型 | random_possible_amendment_type = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | amendment_type |
| random_scope_amendment | 遍历 scope 法律的修正案 | random_scope_amendment = { limit = { <triggers> } #optional weight = { <mtth blocks> } #optional <effects> } | amendment |

| Trigger | 说明 | 示例 | 目标 |
|---|---|---|---|
| any_possible_amendment_type | 遍历可添加到 scope 法律的修正案类型 | any_possible_amendment_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | amendment_type |
| any_scope_amendment | 遍历 scope 法律的修正案 | any_scope_amendment = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> } | amendment |
| can_be_enacted | 检查其国家在当前形势下是否能够颁布该法律 | can_be_enacted = yes | 布尔值 |
| is_reasonable_law_for_petition | 检查该法律是否被视为政府请愿颁布的合理对象 | is_reasonable_law_for_petition = yes | 布尔值 |
| law_approved_by | 检查 scope 法律是否被某利益集团认可 | law_approved_by = ig_rural_folk |  |
| law_is_available | 检查该法律在其国家当前形势下是否可用。类似 can_be_enacted，但忽略政府支持 | law_is_available = yes | 布尔值 |

| Event target | 说明 | 目标 scope |
|---|---|---|
| currently_active_law_in_group | 从一条法律指向该组当前生效法律的 scope | law |
| imposer_of_law | 从一个国家指向当前对其强加法律的国家的 scope | country |
| law_type | 从法律名称 指向法律类型的 scope，或从 scope 法律指向其类型 | law_type |
| owner | 指向对象所属国家的 scope | country |
| type | 从一个对象指向其类型的 scope | amendment_type、building_type、company_type、diplomatic_play_type、harvest_condition_type、institution_type、interest_group_type、law_type、political_movement_type、ship_type、strait_type |

### 法律 GUI 脚本

主条目：
GUI 脚本
| Function | 参数 | 输出 | 说明 |
|---|---|---|---|
| AccessApprovingIGs |  | Unknown | 类别：const |
| AccessDisapprovingIGs |  | Unknown | 类别：const |
| AccessNeutralIGs |  | Unknown | 类别：const |
| AccessSelf |  | Law | 类别：const |
| AppliesTo | Country | bool |  |
| CannotEnactDesc |  | CString |  |
| GetActiveAmendments |  | Unknown | 类别：nonconst |
| GetActiveGroupLaw |  | Law | 类别：nonconst |
| GetAffectedMovementsFromCancelEnact |  | Unknown | 类别：nonconst |
| GetAffectedMovementsFromStartEnact |  | Unknown | 类别：nonconst |
| GetAllAmendments |  | Unknown | 类别：nonconst |
| GetCancelTooltip |  | CString | 类别：nonconst |
| GetCheckpointAdvanceBreakdown |  | CString | 类别：nonconst |
| GetCheckpointAdvanceChance |  | CFixedPoint | 类别：nonconst |
| GetCheckpointAdvanceWithImpositionBreakdown |  | CString | 类别：nonconst |
| GetCheckpointAdvanceWithImpositionChance |  | CFixedPoint | 类别：nonconst |
| GetCheckpointBaseDays |  | int32 | 类别：nonconst |
| GetCheckpointDebateBreakdown |  | CString | 类别：nonconst |
| GetCheckpointDebateChance |  | CFixedPoint | 类别：nonconst |
| GetCheckpointDebateWithImpositionBreakdown |  | CString | 类别：nonconst |
| GetCheckpointDebateWithImpositionChance |  | CFixedPoint | 类别：nonconst |
| GetCheckpointEndDateString |  | CString | 类别：nonconst |
| GetCheckpointProgress |  | CFixedPoint | 类别：nonconst |
| GetCheckpointRemainingDays |  | int32 | 类别：nonconst |
| GetCheckpointStallBreakdown |  | CString | 类别：nonconst |
| GetCheckpointStallChance |  | CFixedPoint | 类别：nonconst |
| GetCheckpointStallWithImpositionBreakdown |  | CString | 类别：nonconst |
| GetCheckpointStallWithImpositionChance |  | CFixedPoint | 类别：nonconst |
| GetCheckpointSuccessBreakdown |  | CString | 类别：nonconst |
| GetCheckpointSuccessChance |  | CFixedPoint | 类别：nonconst |
| GetCheckpointSuccessWithImpositionBreakdown |  | CString | 类别：nonconst |
| GetCheckpointSuccessWithImpositionChance |  | CFixedPoint | 类别：nonconst |
| GetCheckpointTotalDays |  | int32 | 类别：nonconst |
| GetCheckpointTotalDaysBreakdown |  | CString | 类别：nonconst |
| GetCountry |  | Country | 类别：nonconst |
| GetCurrentEnactmentPhaseKey |  | CString | 类别：nonconst |
| GetCustom | CustomLocalization | CString | 类别：nonconst |
| GetDailyProgress |  | CFixedPoint | 类别：nonconst |
| GetDesc |  | CString | 类别：nonconst |
| GetEnactmentLastCheckpointDate |  | Date | 类别：nonconst |
| GetEnactmentLastCheckpointResult |  | CString | 类别：nonconst |
| GetEnactmentPhase |  | int32 | 类别：nonconst |
| GetEnactmentPhaseKey | Unknown | CString | 类别：nonconst |
| GetEnactmentSetbackCount |  | int32 | 类别：nonconst |
| GetExilesThatWouldJoinMovementSupportingLaw |  | Unknown | 类别：nonconst |
| GetExilesThatWouldStartMovementSupportingLaw |  | Unknown | 类别：nonconst |
| GetFlavor |  | CString | 类别：nonconst |
| GetFullName |  | CString | 类别：nonconst |
| GetFullNameWithStatus |  | CString | 类别：nonconst |
| GetGroup |  | LawGroup | 类别：nonconst |
| GetGroupName |  | CString | 类别：nonconst |
| GetIGsApproveList |  | CString | 类别：nonconst |
| GetIGsDisapproveList |  | CString | 类别：nonconst |
| GetIGsEnactmentList |  | CString | 类别：nonconst |
| GetIGsUndecidedList |  | CString | 类别：nonconst |
| GetIGsWithApprovalChanges |  | Unknown | 类别：nonconst |
| GetInstitution |  | Institution | 类别：nonconst |
| GetInstitutionModifier |  | Modifier | 类别：nonconst |
| GetInstitutionTooltip |  | CString | 类别：nonconst |
| GetInstitutionType |  | InstitutionType | 类别：nonconst |
| GetLawAlternatives |  | Unknown | 类别：nonconst |
| GetLawType |  | LawType | 类别：nonconst |
| GetMarginalizedIGsWithApprovalChanges |  | Unknown | 类别：nonconst |
| GetName |  | CString | 类别：nonconst |
| GetNameNoFormatting |  | CString | 类别：nonconst |
| GetNextEnactmentPhaseKey |  | CString | 类别：nonconst |
| GetNumIGsApprove |  | uint32 | 类别：nonconst |
| GetNumIGsDisapprove |  | uint32 | 类别：nonconst |
| GetNumIGsUndecided |  | uint32 | 类别：nonconst |
| GetNumSupportingInterestGroups |  | int32 | 类别：nonconst |
| GetOnActivateDesc |  | CString | 类别：nonconst |
| GetOnDeactivateDesc |  | CString | 类别：nonconst |
| GetOnEnactDesc |  | CString | 类别：nonconst |
| GetOnImposeDesc |  | CString | 类别：nonconst |
| GetPercentPolStrApprove |  | CFixedPoint | 类别：nonconst |
| GetPercentPolStrDisapprove |  | CFixedPoint | 类别：nonconst |
| GetPercentPolStrUndecided |  | CFixedPoint | 类别：nonconst |
| GetPreviousEnactmentPhaseKey |  | CString | 类别：nonconst |
| GetRadicalismDriftTargetOnMovementFromCancelEnact | PoliticalMovement | CFixedPoint | 类别：nonconst |
| GetRadicalismDriftTargetOnMovementFromStartEnact | PoliticalMovement | CFixedPoint | 类别：nonconst |
| GetRadicalismEffectOnMovementFromCancelEnact | PoliticalMovement | CFixedPoint | 类别：nonconst |
| GetRadicalismEffectOnMovementFromStartEnact | PoliticalMovement | CFixedPoint | 类别：nonconst |
| GetReplacedLawEffect |  | CString | 类别：nonconst |
| GetSupportingInterestGroupsBreakdown |  | CString | 类别：nonconst |
| GetSupportingInterestGroupsSummary |  | CString | 类别：nonconst |
| GetTexture |  | Unknown | 类别：nonconst |
| GetTooltip |  | CString | 类别：nonconst |
| GetTooltipNoRequirements |  | CString | 类别：nonconst |
| GetTooltipTag |  | CString | 类别：nonconst |
| GetTypeDesc |  | CString | 类别：nonconst |
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
| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessSelf |  | LawGroup | 类别：const |
| GetDesc |  | CString | 类别：nonconst |
| GetFirstInstitutionType |  | InstitutionType | 类别：nonconst |
| GetKey |  | CString | 类别：nonconst |
| GetName |  | CString | 类别：nonconst |
| GetNameNoFormatting |  | CString | 类别：nonconst |
| GetNumEnactable |  | int32 | 类别：nonconst |
| GetNumImposeOptions | Country | int32 | 类别：nonconst |
| GetNumPotentialEnactable |  | int32 | 类别：nonconst |
| GetTexture |  | Unknown | 类别：nonconst |
| GetTooltipTag |  | CString | 类别：nonconst |
| Self |  | LawGroup |  |

| Function | 参数 | 输出 | 描述 |
|---|---|---|---|
| AccessSelf |  | LawType | 类别：const |
| GetAdditionalEffectDesc |  | CString | 类别：nonconst |
| GetBlockingRequirements | Country | CString | 类别：nonconst |
| GetCustom | CustomLocalization | CString | 类别：nonconst |
| GetDesc |  | CString | 类别：nonconst |
| GetEffectDesc | Country | CString | 类别：nonconst |
| GetFullName |  | CString | 类别：nonconst |
| GetFullNameWithStatus | Unknown | CString | 类别：nonconst |
| GetGroup |  | LawGroup | 类别：nonconst |
| GetName |  | CString | 类别：nonconst |
| GetNameNoFormatting |  | CString | 类别：nonconst |
| GetParentLawType |  | LawType | 类别：nonconst |
| GetRequirements | Unknown | CString | 类别：nonconst |
| GetTexture |  | Unknown | 类别：nonconst |
| GetTooltip | Country | CString | 类别：nonconst |
| GetTooltipTag |  | CString | 类别：nonconst |
| GetTypeDesc |  | CString | 类别：nonconst |
| GetUnlocks |  | CString | 类别：nonconst |
| MakeScope |  | Scope |  |
| Self |  | LawType |  |

| Promote | 参数 | 输出 | 描述 |
|---|---|---|---|
| GetActiveGroupLaw |  | Law | 类别：nonconst |
| GetCheckpointEndDate |  | Date | 类别：nonconst |
| GetCountry |  | Country | 类别：nonconst |
| GetEnactmentLastCheckpointDate |  | Date | 类别：nonconst |
| GetGroup |  | LawGroup | 类别：nonconst |
| GetInstitution |  | Institution | 类别：nonconst |
| GetInstitutionModifier |  | Modifier | 类别：nonconst |
| GetInstitutionType |  | InstitutionType | 类别：nonconst |
| GetLawType |  | LawType | 类别：nonconst |
| MakeScope |  | Scope |  |

| Promote | 参数 | 输出 | 描述 |
|---|---|---|---|
| GetCurrentlyActive |  | Law | 类别：nonconst |
| GetCurrentlyEnacting |  | Law | 类别：nonconst |
| GetFirstInstitutionType |  | InstitutionType | 类别：nonconst |

| Promote | 参数 | 输出 | 描述 |
|---|---|---|---|
| GetGroup |  | LawGroup | 类别：nonconst |
| GetParentLawType |  | LawType | 类别：nonconst |
| MakeScope |  | Scope |  |

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [效果](Effect.md) • [事件目标](Event target.md) • [作用域](Scope.md) • [触发器](Trigger.md) [宏](Macro.md) • [修正类型](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [脚本值](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [决议](Decision modding.md) • [事件](Event modding.md) • [历史](History modding.md) • [日志](Journal modding.md) • [修正](Modifier modding.md) • 目标 • [脚本化 GUI](Scripted gui.md) |
|---|---|

| 脚本类型 | [建筑](Building modding.md) • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • 法律 • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [可自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图片](Event images.md) • [图形资源](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [音效](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod 兼容性](Mod compatibility.md) • [Mod 结构](Mod structure.md) • [脚本测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [Mod 翻译](Mod translation.md) • [新国家 Mod 制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州 Mod 制作指南](State modding guide.md) |
|---|---|