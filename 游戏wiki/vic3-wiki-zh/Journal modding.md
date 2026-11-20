---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Journal modding
source: https://vic3.paradoxwikis.com/Journal_modding
pageid: 3457
categories: [Potentially_outdated, 1.8, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。至少部分章节最后核实的版本为 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.8。

日志条目
**游戏文件夹 该类型的文件存放目录。 ：** `common/journal_entries`

---

**图标文件夹 该类型的原版游戏图标通常存放的目录。 ：** `gfx/interface/icons/event_icons`

---

**可注入（Injectable） 该类型是否可以使用 INJECT 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **可替换（Replaceable） 该类型是否可以使用 REPLACE 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**相关游戏对象：** [决议](Decision modding.md)、[事件](Event modding.md)、[On action](On action.md)

[日志](Journal.md)条目代表玩家需要应对的持续局势或目标。日志条目定义于 /Victoria 3/game/common/journal_entries。

## 示例条目

日志条目既可以通过脚本化的 [trigger](Trigger.md) 块激活，也可以由某个 [effect](Effect.md) 激活。一旦激活，条目可以通过*完成*、*失败*、*超时*或*失效*来结束。当日志条目激活或结束时，可以触发 effect；在其处于活跃状态期间，可以对国家应用一个 modifier，并且可以在每周、每月或每年的脉冲中触发 effect。日志条目中脚本元素的顺序无关紧要。

| journal_entry_key = { # root = the owner of the Journal Entry (country scope) # scope:journal_entry = this Journal Entry (journalentry scope) # scope:target = target value, with which this Journal Entry was added using `add_journal_entry` effect # optional journal entry group as specified in common/journal_entry_groups group = journalentrygroup_mygroup # optional image that shows in the journal entry widget near the description, default = NDefines::GUI::JOURNAL_ENTRY_ICON_DEFAULT (set in /defines/00_interfaces.txt) icon = "gfx/interface/icons/event_icons/event_industry.dds" # optional trigger which determines if a journal entry is displayed during country selection, default = no is_shown_in_lobby = { c:GBR = this } # optional trigger which determines if a journal entry can be shown, default = no # is ignored when JE is added through `add_journal_entry` effect is_shown_when_inactive = { c:GBR = root } # one or more scripted buttons. See common/scripted_buttons/_scripted_buttons.info for more info scripted_button = scripted_button_key # optional trigger - when both this and is_shown_when_inactive is true, the JE is Activated, default = yes # is ignored when JE is added through `add_journal_entry` effect possible = { c:USA = { owns_entire_state_region = scope:target } } # effect which happens when a journal entry is activated by having its `is_shown_when_inactive` and `possible` triggers become true or when JE is added through `add_journal_entry` effect immediate = { c:USA = { # saved scopes can be used in any events triggered from the Journal Entry, as well as in the loc for the Journal Entry itself # To use saved scopes in loc: JournalEntry.GetTopScope.sCountry('saved_scope_name') or SCOPE.sCountry('saved_scope_name') save_scope_as = god_bless_america set_variable = { name = freedom value = 1 } } set_variable = test_variable # all events in these on_actions can refer to scope:god_bless_america trigger_event = { id = test_event.1 days = 0 popup = yes } } # completion trigger, use is_goal_complete = yes in here if you're testing a tracked goal metric; if left blank, cannot be completed complete = { scope:god_bless_america = { NOT = { owns_entire_state_region = STATE_ALASKA } } custom_tooltip = { # Following loc functions can be used: # [JournalEntry.GetTotalGoalValue] - goal absolute value (fixed point) # [JournalEntry.CalcCurrentGoalValue] - current progress absolute value (fixed point) # [JournalEntry.GetGoalAddValue] - goal relative value (fixed point) # [JournalEntry.GetGoalProgressValue] - current progress relative value (fixed point) # [JournalEntry.GetGoalProgressPercent] = GetGoalProgressValue / GetGoalAddValue (fixed point) text = journal_entry_key_goal_text scope:journal_entry = { is_goal_complete = yes } } } # effect which is executed when 'complete' trigger becomes true on_complete = { trigger_event = { id = test_event.10 days = 0 } } # failure trigger, should spawn event explaining what happens when triggered, framed as a failure; if left blank, cannot fail fail = { NOT = { c:GBR = root } } # effect which is executed when 'fail' trigger becomes true on_fail = { remove_variable = test_variable scope:god_bless_america = { remove_variable = freedom } } # optional invalidation trigger, should not notify player when it triggers, just clean up and silently disappear due to journal entry no longer being valid; if left blank, cannot be invalidated invalid = { } # effect which is executed when 'invalid' trigger becomes true on_invalid = { } # dynamically updated text, which describes the current status of the Journal Entry # To use in loc or UI: [JournalEntry.GetStatusDesc] # If this is not specified, GetStatusDesc will instead return loc from key <journal_entry_key>_status status_desc = { first_valid = { triggered_desc = { desc = journal_entry_key_status_1 trigger = { has_variable = mining_strike } } triggered_desc = { desc = journal_entry_key_status_2 trigger = { has_variable = industrial_strike } } triggered_desc = { desc = journal_entry_key_status_2 trigger = { has_variable = railway_strike } } } } # the number of days before this journal entry forcibly transitions, can be used to transition silently or into another event, framed either as success, failure, or neutral; if left blank or set to zero, will not time out timeout = 720 # effect which is executed when journal entry is timed out on_timeout = { } # zero or more static modifiers that will be applied to the Journal Entry when it activates, where they will propagate to the country modifiers_while_active = { } # on_action which is triggered every first day of the week on_weekly_pulse = { random_events = { 100 = 0 10 = test_event.2 10 = test_event.3 10 = test_event.4 } } # on_action which is triggered every first day of the month on_monthly_pulse = { events = { test_event.5 } } # on_action which is triggered every first day of the year on_yearly_pulse = { effect = { scope:god_bless_america = { change_variable = { name = freedom add = 1 } } } } # a script value computing the goal completion metric current_value = { value = gdp } # when the journal entry is activated current_value and goal_add_value are evaluated and added together to determine the goal value goal_add_value = { value = gdp multiply = 0.25 } # the highest weighted active journal entry appears in the goal tracker on the main screen weight = 200 # yes/no, determines if this journal entry should be transfered if the player switches country through a revolution or by releasing a subject. Note that external dependencies such as country variables etc are not automatically inherited transferable = no # yes/no, determines if this journal entry is allowed to be inherited by a victorious revolution. Revolutions also get all variables from the defeated parent country, so most JEs *should* be inherited in this way # NOTE: transferable = yes will always mean that revolution inheritance is blocked as these JEs should stay with the player at all times can_revolution_inherit = yes # optional trigger, progress text is shown if this is defined and true is_progressing = { exists = scope:target scope:target = { is_under_construction = yes } } # yes/no, if yes, a progress bar is shown progressbar = yes # yes/no, if yes, the Journal Entry can return to an inactive state if its possible trigger reverts to false # if no or unspecified, an activated Journal Entry cannot return to being inactive even if it is no longer considered possible can_deactivate = yes # dynamically updated text, which is shown over the progress bar of the Journal Entry # value can be a localization key or first_valid + triggered_desc script # To use in loc or UI: [JournalEntry.GetProgressDesc] # If this is not specified, GetProgressDesc will instead return loc from key <journal_entry_key>_progress progress_desc = journal_entry_goal_progress_integer # tutorial lesson explaining HOW to complete the Journal Entry how_tutorial = how_tutorial_lesson_key # tutorial lesson explaining the WHY around the Journal Entry why_tutorial = why_tutorial_lesson_key # whether a Journal Entry should be pinned in its outliner by default. Defaults to 'no' should_be_pinned_by_default = yes } |
|---|

## 条目组

日志条目组
**游戏文件夹 该类型的文件存放目录。 ：** `common/journal_entry_groups`

---

**可注入（Injectable） 该类型是否可以使用 INJECT 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **可替换（Replaceable） 该类型是否可以使用 REPLACE 数据库功能？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

日志条目可以通过脚本化的分类在视觉上进行分组。这些分组定义于 /Victoria 3/game/common/journal_entry_groups。分组的脚本名称也会被用作 [本地化（localization）](Localization.md) 键。

示例：

```
journalentrygroup_mygroup = {
    context = none/country
}
```

context 决定该分组中的日志条目是属于特定国家的还是国际性的。

日志条目通过 `group = group_script_name` 被添加到某个分组中。

## 激活

日志条目要成为活跃状态，必须满足其两个 [trigger](Trigger.md) 块之一，或者由 [effect](Effect.md) `add_journal_entry` 添加。

### 通过 effect

effect `add_journal_entry` 可以激活任何日志条目，无论它是否带有脚本化的 trigger 块，也无论这些 trigger 块是否被满足。此外，它还可以为日志条目指定一个*目标（target）*，该目标可在条目的 trigger 或 effect 中使用。

示例：

```
add_journal_entry = { 
	type = je_ig_suppression_1
	target = scope:suppressed_ig
}
```

### 通过 trigger

日志条目也可以通过满足脚本化的 trigger 块来激活，有两种不同的 trigger 块：`is_shown_when_inactive` 和 `possible`。前者决定日志条目是否出现在玩家的潜在条目列表中，后者决定该条目是否变为活跃状态。在不使用 `add_journal_entry` effect 的情况下，两者都必须为真条目才能激活。默认情况下，`is_shown_when_inactive` 返回 false，`possible` 返回 true。

示例：

```
is_shown_when_inactive = {
	is_player = yes
	NOT = { has_variable = mechanized_farming_je_done }
	has_technology_researched = threshing_machine
}

possible = {
	has_technology_researched = mechanized_farming
}
```

### 即时 effect

当日志条目变为活跃状态后，可以通过 `immediate` 块触发一个 effect。

示例：

```
immediate = {
	trigger_event = { id = suffragist_events.9 popup = yes }
}
```

## 结束

日志条目通过三种脚本化 trigger 块之一结束并被移除，或者因超时而结束。虽然在技术上这些由触发导致的结束方式没有区别，但它们呈现给玩家的方式不同。这些 trigger 块默认返回 false。每种结束方式都可以触发 effect。

### 通过完成

完成被表述为正面的，即达成了条目的目标，例如拥有某些州或实现较高的生活水平。

示例：

```
complete = {
	pop_type_percent_country = {
		pop_type = peasants
		percent < 0.35
	}
	NOT = {
		has_law = law_type:law_serfdom 
		has_law = law_type:law_land_based_taxation
	}
	ig:ig_industrialists = {
		is_marginal = no
	}
}

on_complete = {
	trigger_event = { id = urbanization_events.1 }
}
```

### 通过失败

失败被表述为负面的，即未能避免某些情况，例如失去州或生活水平低下。

示例：

```
fail = {
	NOT = { has_state_in_state_region = STATE_ORAN }
	NOT = { has_state_in_state_region = STATE_ALGIERS }
	NOT = { has_state_in_state_region = STATE_CONSTANTINE }
}

on_fail = {
	trigger_event = algeria_events.3
}
```

### 通过失效

失效被表述为中性的，例如条目不再具有相关性。

示例：

```
invalid = {
	NOT = {
		exists = c:BRZ
	}
}

on_invalid = {
	if = {
		limit = {
			has_modifier = brazilian_slave_trade_modifier
		}
		hidden_effect = {
			remove_modifier = brazilian_slave_trade_modifier
		}
	}
}
```

### 通过超时

超时是日志条目结束前的天数。它通常与 `complete` 或 `fail` trigger 块之一搭配使用，以表示完成条目的时间限制，或为避免失败条件而“坚持”的时间。日志条目也可能只有超时而没有 `complete` 或 `fail`，用于表示某种局势产生一定效果后，在一段时间后消失。

示例：

```
timeout = 3650

on_timeout = {
	trigger_event = { id = red_scare.20 }
}
```

## 脉冲 effect

有三种不同的脉冲：`on_weekly_pulse`、`on_monthly_pulse` 和 `on_yearly_pulse`。每种脉冲会在每个周期第一天的开始触发其包含的 effect。脉冲用于与日志条目相关的随机事件或重复性 effect。如有需要，两种用途可以在同一个脉冲中使用。脉冲实际上就是日志条目的 [on action](https://vic3.paradoxwikis.com/On_actions)。

示例：

```
on_monthly_pulse = {
	effect = {
		if = {
			limit = {
				has_law = law_type:law_slavery_banned
			}
			change_variable = {
				name = acw_progress_var
				add = 1
			}
		}
	}
	random_events = {
		# American Civil War buildup
		200 = 0
		10 = acw_events.1 # The Abolitionist's Martyrdom
		10 = acw_events.3 # The Wilmot Proviso
	}
}
on_yearly_pulse = {
	events = {
    	example_event.1 # an event which always triggers on pulse
    }
	random_events = {
		40 = 0
		20 = acw_events.2 # The Fugitive Slave
		20 = acw_events.5 # Bleeding Kansas
		20 = acw_events.6 # The Caning of Charles Sumner
	}
}
```

## 脚本化按钮

脚本化按钮（scripted button）是将[决议](Decision modding.md)与日志条目绑定的一种方式。日志条目可以使用 `scripted_button = scripted_button_key` 添加任意数量的脚本化按钮。脚本化按钮定义于 /Victoria 3/game/common/scripted_buttons。

脚本化按钮的脚本与决议非常相似，包含用于显示按钮的 trigger 块 `visible`、用于判断能否使用的 trigger 块 `possible`、一个 `ai_chance` 块和一个 `effect` 块。每个脚本化按钮的键必须唯一，但名称和本地化键不必唯一。

示例：

```
scripted_button_key = {
	name = "LOC_KEY"
	desc = "LOC_KEY_DESC"

	visible = { always = yes }
	
	#Country scope
	ai_chance = {
		value = 0
		if = {
			limit = { bureaucracy > 0 }
			add = 5
		}
	}

	possible = {
		not = {
			has_variable = my_cool_var
		}
	}

	effect = {
		set_variable = my_cool_var
	}
}
```

## 其他元素

日志条目还有许多其他可选元素。

### 目标

日志条目可以使用“目标”，它是一个在日志条目激活时计算的 [script value](Script value.md)，可以是脚本变量，也可以是 GDP 或生活水平等游戏数值。

目标的基础值通过 script value `current_value` 设置，并与 `goal_add_value` 相加。两者可以与特殊的布尔型日志 trigger `is_goal_complete` 配合使用，该 trigger 可用于任何结束 trigger 块中。该目标数值在条目激活后无法更改，通常与进度条结合使用，以检查某个数值（如月数）向目标的推进情况。

示例：

```
current_value = {
	value = scope:coffee_scope.market_goods_buy_orders
}

goal_add_value = {
	value = scope:coffee_scope.market_goods_buy_orders
	multiply = 2.5
}
```

注意，在上面的示例中，由于 `current_value` 和 `goal_add_value` 会相加，最终目标数值是条目激活时咖啡购买订单量的 3.5 倍。
### 修正项（Modifier）

日志条目可以使用 `modifiers_while_active` 块来定义一系列[脚本化修正项](Modifier modding.md)。

示例：

```
modifiers_while_active = {
	modifier_assimilation_nnc
}
```

### 进度条

`progressbar = yes` 会添加一个动态进度条，如果定义了目标值，它会与目标值绑定。

### 脚本化进度条

这类进度条定义在 /Victoria 3/game/common/scripted_progress_bars 中。一个日志条目可以使用 `scripted_progress_bar = scripted_progress_bar_key` 添加任意数量的脚本化进度条，每条进度条对应一个该语句。脚本化进度条不与目标值交互，而是具有定义好的最大值、最小值和起始值。

`start_value =` 设置初始值，`max_value =` 设置最大值，`min_value =` 设置最小值。数值可以按每周、每月或每年更新，或它们的某种组合。每一项都设置为一个脚本值（script value）块，用于设定数值量。

进度条有多种皮肤，分别是：

- double_sided_gold
- default_green
- default_bad
- default
- double_sided_bad

双向皮肤用于《大博弈》（The Great Game）风格的进度条，具有相互对立的结果。

`is_inverted = yes` 术语会反转描述，使负向进度被视为好事、正向进度被视为坏事，与默认描述相反。

示例：

```
divided_monarchists_bonapartist_progress_bar = {
	name = "divided_monarchists_bonapartist_progress_bar"
	desc = "divided_monarchists_bonapartist_progress_bar_desc"

	default = yes #This is the skin

	monthly_progress = {
		if = {
			limit = {
				NOT = {
					has_variable = fra_divided_monarchists_freeze #This variable stops iteration, and is granted by reaching 360 with one dynasty. It's reset when this JE is completed, or when je_cement_the_rightful_dynasty fails.
				}
			}
			add = {
				desc = "bonapartist_progress_from_characters"
				value = owner.var:bonapartist_progress_from_characters
			}
			add = {
				desc = "bonapartist_progress_from_igs"
				value = owner.var:bonapartist_progress_from_igs
			}
			add = {
				desc = "bonapartist_progress_from_military"
				value = owner.var:bonapartist_progress_from_military
			}
			add = {
				desc = "bonapartist_progress_from_legitimacy"
				value = owner.var:bonapartist_progress_from_legitimacy
			}
			add = {
				desc = "bonapartist_progress_from_effects"
				value = owner.var:bonapartist_progress_from_effects
			}
		}
	}

	start_value = 10
	min_value = 0
	max_value = 360

}
```

### 本地化与状态

日志条目具有以下默认的本地化键：

- <journal_entry_script_name>：条目的本地化名称/标题
- <journal_entry_script_name>_reason：条目的描述/背景文本
- <journal_entry_script_name>_status：描述条目当前状态的文本，可以用 `status_desc` 块覆盖
- <journal_entry_script_name>_progress：进度条上方的文本，可以用 `progress_desc` 键或块覆盖

只有当 trigger（触发条件）块 `is_progressing` 返回真时，进度文本才会显示。

示例：

```
is_progressing = {
	has_journal_entry = je_pedro_brazil
	scope:target ?= {
		is_heir = yes
	}
	NOT = {
		has_law = law_type:law_no_womens_rights
	}
}
```

### 图标

图标可以通过 `icon = "<file path>"` 定义，例如 `icon = "gfx/interface/icons/event_icons/event_industry.dds"`。

如果未定义图标，则使用默认图标 `event_default.dds`。

### 杂项

- `can_deactivate = yes/no`：默认为 no，如果为 yes，当 possible 触发条件块在任意时刻返回假时，该条目会停用。
- `weight = <int>`：按权重从高到低对大纲中的条目排序
- `transferable = yes/no`：默认为 no，如果为 yes，当玩家因革命或释放并扮演其他国家而变更国家时，该条目会随玩家转移。
- `can_revolution_inherit = yes/no`：默认为 yes，如果为 no，胜利的革命不会继承该条目；注意 `transferable = yes` 会阻止此项生效
- `should_be_pinned_by_default = yes/no`：默认为 no，如果为 yes，该日志在激活时会默认固定在大纲中
- `how_tutorial = scripted_tutorial`：为日志条目添加一个可点击的教程，其内容围绕*如何*完成该条目
- `why_tutorial = scripted_tutorial`：为日志条目添加一个可点击的教程，其内容围绕*为何*要完成该条目
- `display_progressbar_as_months = yes/no`：默认为 no，如果为 yes，进度条将以年加月的形式显示剩余进度

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [修正项类型](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本化内容 | [决议](Decision modding.md) • [事件](Event modding.md) • [历史](History modding.md) • 日志 • [修正项](Modifier modding.md) • 目标 • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本化类型 | [建筑](Building modding.md) • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [可自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图像](Event images.md) • [图形资源](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [音效](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [模组](Mod.md) • [模组兼容性](Mod compatibility.md) • [模组结构](Mod structure.md) • [脚本化测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [模组翻译](Mod translation.md) • [新国家模组制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州模组制作指南](State modding guide.md) |
|---|---|