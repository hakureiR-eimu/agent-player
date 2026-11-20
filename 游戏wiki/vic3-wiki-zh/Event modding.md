---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Event modding
source: https://vic3.paradoxwikis.com/Event_modding
pageid: 3471
categories: [Potentially_outdated, 1.11, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。至少部分内容最后验证于 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.11。

参见：
events
事件（Events）
**游戏文件夹 此类文件存储所在文件夹。 ：** `events`

---

**图标文件夹 此类基础游戏图标通常存放的文件夹。 ：** `gfx/interface/icons/event_icons`

---

**可注入（Injectable） 此类型是否可以使用 INJECT 数据库函数？ ：** ![No](/images/thumb/0/04/No.png/24px-No.png) no **可替换（Replaceable） 此类型是否可以使用 REPLACE 数据库函数？ ：** ![No](/images/thumb/0/04/No.png/24px-No.png) no

---

事件可以放置在 events 文件夹内的子文件夹中

---

**相关游戏对象：**[Decisions](Decision modding.md)、[Journal entries](Journal modding.md)、[On actions](On action.md)

事件是一个完善的 mod 中最重要的元素之一。事件可以通过提供玩家交互，并作为承载你 mod 中的历史、机制、背景设定等的载体，为你的 mod 增添风味与个性。

《维多利亚3》中的事件**从不**自行触发；它们必须始终由另一个 effect（游戏内效果脚本）触发，例如 on_action、日志条目、决议或另一个事件。

## 文件位置

事件存储在 /Victoria 3/game/events 文件夹内的 .txt 文件中；对于 mod，则是 /<mod>/events。事件文件也可以组织在子文件夹中，例如 `/events/gbr_events`。

*所有事件文件必须使用 UTF-8 BOM 编码。*

## 文件结构

### 命名空间（Namespace）

每个事件文件都以一个 `namespace` 条目开头。**你的事件文件中必须包含它，否则事件将无法工作**。此后，每个事件都使用该命名空间进行命名和编号。同一个文件可以包含多个命名空间，但每个命名空间都应在使用它的事件定义之前声明。

```
namespace = example_event

example_event.1 = {
	<event_contents>
}

example_event.2 = {
	<event_contents>
}
```

### 注释

与《维多利亚3》脚本的其他部分一样，一行中 `#` 符号之后的任何内容都会被游戏引擎忽略。你可以利用这一点来添加注释，为事件脚本提供背景说明或给自己留下备忘。

```
example_event.1 = {
	<event_content> # Anything you write here will be ignored by the game engine
}
```

## 事件结构

### 基本结构

每个事件的整体结构相当一致。下面是一个包含几乎所有元素的事件模板。这些内容将在后续章节中解释。

```
example_event.1 = { # 
	type = country_event
	placement = root
	
	title = example_event.1.t
	desc = example_event.1.d
	flavor = example_event.1.f
	
	event_image = {
		video = "<media_alias>"
	}
	
	icon = "gfx/interface/icons/event_icons/event_default.dds"
	
	on_opened_soundeffect = "event:/SFX/UI/Alerts/event_appear"
	
	duration = 3
	
	trigger = { #optional, defaults to yes if empty or unused
	}
	
	cancellation_trigger = { #optional, only use if event should be cancelled by a change in gamestate
	}

	cooldown = { #optional, defines time period before event can be evaluated again
	}

	immediate = { #optional, sets effects that happen immediately when event is fired
	}
	
	option = {
		name = example_event.1.a
		default_option = yes
	}
	
	option = {
		name = example_event.1.b
	}
    	
	option = {
		name = example_event.1.c
        trigger = { } #optional, determines if option is available/visible
        
	}
	
	after = { #optional, sets effects that happen after an option is selected
	}

}
```

### ID、类型与放置

事件 ID 的形式为 `<namespace>.<id>`。ID 可以是除 0 以外的任何数字，只要在任何事件文件中没有重复即可。例如，你可以写成 `example_event.1` 或 `example_event.0001`。

`type` 决定事件的起始 scope。通常为 `country_event`，但也可以是 `state_event` 或 `character_event`。关于如何使用 scope 的更多信息，请参见 [Scopes](https://vic3.paradoxwikis.com/Scopes)。

最后，`placement` 决定事件图标在地图上的放置位置。默认情况下，这是触发事件的 scope，但也可以使用已保存的 scope，即 `placement = scope:<your_saved_scope>`

### 标题、描述与风味文本

这些字段中的信息决定了事件标题栏中显示的内容，以及事件窗口右侧上方的描述文本框和下方的风味文本框中显示的内容。这些都对应于本地化文件中的本地化键。关于本地化的更多信息，请参见 [Localization](Localization.md)。

大多数事件使用固定的本地化文本，但你也可以通过使用 `triggered_desc` 为事件提供动态文本。例如：

```
	desc = {
		triggered_desc = {
			desc = example_event.1.d1
			trigger = {
				<your triggers here>
			}
		}
		triggered_desc = {
			desc = example_event.1.d2
			trigger = {
				<your triggers here>
			}
		}
	}
```

虽然该指令名为 `triggered_desc`，但它对 `title` 和 `flavor` 的用法完全相同。你可以根据需要使用任意多个这样的块。如果多个 `triggered_desc` 块都满足条件，它们将全部按照在事件文件中列出的顺序显示；另外，也可以用 `first_valid` 或 `random_valid` 块包裹任意数量的 `triggered_desc`。这样只会选取其中单个 `triggered_desc`：要么是第一个通过其触发条件的，要么是通过触发条件的块中随机选取的一个。

### 事件图像

参见：
事件图像列表
事件图像有两种类型：视频和纹理。视频应为 .bk2（Bink Video）文件，纹理应为 .dds（DirectDraw Surface）文件。

视频通过以下结构引用 /Victoria 3/game/gfx/media_aliases/media_aliases.txt 中的 `media_alias`：

```
	event_image = {
		video = "<media_alias>"
	}
```

纹理通过以下结构引用静态图像：

```
	event_image = {
		texture = "gfx/event_pictures/<texture_name>.dds"
	}
```

事件还可以通过 `gui_window` 以及 `left_icon` 和 `right_icon` 显示一个或两个人物头像。原版的 gui_windows 定义在 /Victoria 3/game/gui/eventwindow.gui 中的 `event_window` 块里。left_icon 和 right_icon 是在这些 event_window 中定义的术语，可以通过 scope 设置为人物。事件还可以使用 `minor_left_icon` 和 `minor_right_icon`，它们可以设置为国家的 scope 以显示该国国旗，或设置为人物的 scope 以显示一个小头像。

### 图标、音效与持续时间

`icon` 决定事件触发时在大纲（outliner）和地图上显示的纹理。这些图标位于 /Victoria 3/game/gfx/interface/icons/event_icons，应为 .dds（DirectDraw Surface）文件。也可以选择其他图标，例如技术图标。

`soundeffect` 决定点击事件并打开事件窗口时播放的声音。通常无需更改。事件打开时播放的音频由 `media_alias` 定义。

`duration` 决定事件在大纲中存在多少个月后自动结算。设置为 0 表示没有时间限制。

### 触发器与取消触发器

关于使用触发器的更多信息，请参见
Triggers
。关于这些元素的更多信息，请参见
On actions
、
Journal modding
和
Decision modding
《维多利亚3》中的事件必须由 effect 触发，常见的示例如下：

- 日志条目的 on_action 或 effect 块中的 `events` 或 `random_events` 块。
- 决议的 `when_taken` 块。
- 另一个事件中的 effect 块。

除了触发 effect 中使用的触发器之外，事件还可以使用自己的一组触发器来决定是否能够触发。如果 trigger 块被省略或为空，则视为始终可以触发。

触发器基于事件由其 `type` 决定的初始 scope 进行评估，并且会对每个国家/州/人物进行评估。结构不正确的 trigger 块可能导致事件反复触发、对错误的国家触发，或者根本不触发。

以下是一个简单 trigger 块的示例。触发器首先评估 USA 这个国家是否存在。接着评估当前国家是否为 USA。当所有触发条件都为真时，事件触发：

```
	trigger = {
		exists = c:USA # this checks if a country with the tag "USA" exists
		this = c:USA # this checks if a country with the tag "USA" is the current scoped country
	}
```

**请记住**：游戏会评估*每一个*与事件类型匹配的 scope。在上面的示例中，游戏会遍历每个国家，直到找到满足这两个触发条件的匹配项。你可以通过添加检查精确国家标签（tag）、主流文化、国教等的触发器，将事件限制在特定国家。如果你的事件反复触发，请从其他 scope 的角度审视你的触发器。*注意：如果你在 on_action 中包含一个事件而没有指定任何触发器，它会在该 on_action 每次被评估时触发。*

以下是一个更复杂的 trigger 块示例：

```
	trigger = {
		has_technology_researched = nationalism
		NOT = { has_technology_researched = pan-nationalism }
		is_subject = no
		is_junior_in_customs_union = no
		OR = {
			country_rank = rank_value:great_power
			country_rank = rank_value:major_power
			country_rank = rank_value:unrecognized_major_power
		}
		OR = {
			c:GRE ?= {
				has_technology_researched = nationalism
			}
			c:SER ?= {
				has_technology_researched = nationalism
			}
			c:MON ?= {
				has_technology_researched = nationalism
			}
		}
	}
```

在这个例子中，前几个触发器都是从 `root` scope（通常是国家的 scope）评估的。最后三个触发器则从其他 scope 评估。你可以让这些 trigger 块随心所欲地简单或复杂——只需记住，过多的 trigger 块可能会影响游戏性能。

`cancellation_trigger` 是一个可选块，用于决定事件是否应在未与玩家交互的情况下消失。例如，如果你希望在玩家颁布寡头制（Oligarchy）法律时取消某个事件，可以使用：

```
	cancellation_trigger = {
		has_law = law_type:law_oligarchy
	}
```

这对于在事件触发到玩家或 AI 选择选项、或事件持续时间结束之间，由于游戏状态变化而可能不再有效或不再相关的事件最为有用。

### 即时效果

关于 effect 的更多信息，请参见
Effects
。上一节涉及的所有内容都与触发器有关。而 `immediate` 块则使用 effect。

事件的 `immediate` 块中的任何内容都会在事件触发的瞬间、事件呈现给玩家之前执行。通常，这用于通过设置变量、创建人物和保存 scope 来为事件做准备，但你可以在该块中放入任何 effect。immediate 块的一个常见用途是保存 scope，以便自定义事件的本地化文本。

以下是一个示例：

```
	immediate = {
		ruler = {
			save_scope_as = ruler_scope
		}
		heir = {
			save_scope_as = heir_scope
		}
		ig:ig_armed_forces = {
			leader = {
				save_scope_as = ig_armed_forces_scope
			}
		}
		c:GBR = {
			save_scope_as = uk_scope
		}
		s:STATE_BAVARIA = {
			random_scope_state = {
				save_scope_as = bavaria_state_scope
			}
		}
		random_scope_character = {
			limit = {
				has_variable = example_variable
			}
			save_scope_as = example_character_scope
		}
		set_variable = example_event_happened
	}
```

与大多数 effect 块一样，所有 effect 都在 `root` scope 执行，除非另有说明。在这个例子中，保存了多个 scope，以便在本地化或后续的其他 effect 中使用。例如，你可以在本地化中设置 `[SCOPE.sCharacter('<scope_key>').GetFullName]`，然后在事件的 immediate 块中 scope 到某个人物并将其保存为 `scope_key`，从而使你的事件更具动态性。你可以在原版事件中找到许多这样的例子。你还可以设置变量，以确保事件只触发一次，或用于构建事件链。

例如，以下代码可以确保某个事件对某个国家只触发一次：

```
	trigger = {
		NOT = {
			has_variable = example_variable
		}
	}
	
	immediate = {
		set_variable = example_variable
	}
```

### 冷却（Cooldown）

`cooldown` 是一个可选块，用于在给定时间内暂时阻止事件再次触发。该块接受 `years`、`months` 和 `days` 参数。使用该块会设置一个变量，在指定时间内阻止事件被触发。请注意，使用 `set_variable` effect 设置的变量也可以带有持续时间。

```
	cooldown = {
		years = 3
	}
```

### 选项

每个事件必须至少有一个 `option`，并且其中至少一个必须带有 `default_option` 条目（隐藏事件除外，见下文）。一个事件可以有任意数量的选项，但选项过多会使事件窗口变得越来越难看，最终无法使用。

每个选项都有一个 `name`，即本地化键。虽然 Paradox 通常使用 `event_id.1.a`、`event_id.1.b` 等格式，但这些可以是任何本地化键。

以下是一组简单的两个选项：

```
	option = {
		name = example_event.1.a
		default_option = yes
		add_modifier = {
			name = modifier_example
			months = normal_modifier_time
		}
	}
	
	option = {
		name = example_event.1.b
		add_radicals = {
			pop_type = academics
			value = medium_radicals
		}
	}
```

与 `immediate` 块一样，每个选项中的 effect 都在 `root` scope 执行，除非另有说明。你还可以使用来自 `immediate` effect 或之前事件中保存的 scope（如果该事件是连续事件链的一部分）：

```
	immediate = {
		set_global_variable = example_var # global_variables are visible to all countries
		s:STATE_PELOPONNESE = { # this scopes to a specific state_region
			random_scope_state = { # this searches for a state within the state region; since there is no limit, it iterates until it finds the first state in this state_region
				save_scope_as = peloponnese_scope # we save this to use later
			}
		}
	}
	
	option = {
		name = example_event.1.a
		default_option = yes
		add_modifier = { # these can be applied to countries, states, characters, IGs, and units
			name = modifier_example # always ensure the modifier you use works in the scope you're assigning it to
			months = normal_modifier_time # this is pre-defined value provided by the game, but you can use your own amount
		}
		scope:peloponnese_scope = { # this changes the current scope to the state we saved earlier
			add_loyalists_in_state = { # this effect only works in the state scope. this is why we had to save a state scope earlier
				pop_type = academics # these are defined in \common\pop_types
				value = medium_radicals # this is a pre-defined value, don't be thrown off by the name "medium_radicals" it is actually referencing a fixed number in \common\script_values\event_values.txt
			}
		}	
	}
```

选项还可以拥有自己的 `trigger` 块，用于为事件增加额外的层次。在这个例子中，`trigger` 块向 FRA 显示一个选项，向其他国家显示另一个选项（`!=` 表示"不等于"）：

```
	option = {
		name = example_event.1.a # every option needs a name
		default_option = yes # every event needs a default option or the game will print an error
		trigger = {
			c:FRA != this # != means "not equal to"
		}
		show_as_tooltip = { # this presents the effects to the player as if it will be executed, but does nothing
			c:FRA = { # changes the current scope to the country FRA
				create_diplomatic_pact = {
					country = c:TUN # Must be a country scope. If you saved a country scope, you can use that instead.
					type = protectorate
				}
			}
		}
	}
	
	option = {
		name = example_event.1.a # options can have the same name as each other
		trigger = {
			c:FRA = this # This displays this option if the current country is FRA
		}
		create_diplomatic_pact = { # This effect will be executed, unlike the above one
			country = c:TUN
			type = protectorate
		}
	}
```
下面是一个更复杂的选项示例：

```
	option = {
		name = example_event.1.a
		default_option = yes
		add_journal_entry = {
			type = je_example_journal # this adds the specified journal entry. You must use the "type =" argument or the effect will fail
		}
		scope:example_saved_scope = { # lets say you saved this in the immediate
			add_modifier = {
				name = modifier_example # this is the name of a modifier
				months = normal_modifier_time # this is a pre-defined value, but you can substitute in your own duration if you wish
				is_decaying = yes # this is an optional argument that makes the modifier get weaker as it's duration counts down
			}
		}
		if = { # this effect will only happen if its limit is true
			limit = { # triggers go here
				country_has_primary_culture = cu:yankee # the cu: is telling the game to look for a culture definition, since that's what this trigger wants
			}
			hidden_effect = { # effects that are executed if limit evaluates to true; in this case, hidden_effect also hides this from the player
				trigger_event = { # fires the specified event
					id = example_event.2 # the ID of the event being triggered 
					days = 30 # an optional argument; fires the event after this duration has passed
					popup = yes # an optional argument; makes the event pop up without the player having to click on it; note this does NOT pause the game
				}
			}
		}
	}
```

### After（后置块）

`after` 块是一个可选的 effect（游戏内效果脚本）块，在选择某个选项之后执行其中包含的效果。绝大多数原版事件都不使用这个 function，但如果你希望无论玩家选择哪个选项都确保某件事发生，或者想在一条很长的事件链之后找一个方便的地方执行一些清理效果，它会非常有用：

```
	after = {
		set_variable = example_event_completed
		trigger_event = {
			id = example_event.2
		}
	}
```

### 其他特性

如果你正在开发一个带有 DLC 图标的 mod，可以在事件中添加 `dlc = <dlc_key>`，让你这个 mod 的图标和名称显示在事件左下角，与 Paradox 的 DLC 类似。

在 debug mode（调试模式）下，你可以使用命令 `event <event_id>` 手动触发事件。

## 隐藏事件

有时，你不一定想把某个事件展示给玩家，但又需要根据某些 trigger 执行一些效果。这种情况下，你可以创建一个隐藏事件。

隐藏事件所需的结构比普通事件更少。具体来说，隐藏事件不需要任何 localization（本地化文本）、音频或视觉元素。它们也不需要任何选项，而且由于事件不会被显示，任何选项都不会生效。要创建隐藏事件，只需在事件中添加 `hidden = yes`：

```
example_event.1 = { # every event always needs an ID
	type = country_event # remember, this can be state_event or character_event too
	hidden = yes # you must include this line or you'll get errors
	
	trigger = {
		<your_triggers_here> # this works exactly like normal events
	}

	immediate = {
		<your_effects_here> # this works exactly like normal events
	}
	
}
```

下面是一个更复杂的隐藏事件示例：

```
example_event.1 = {
	type = country_event # This means that, root is the country in which the event happened, instead of state or character.
    hidden = yes # remember, if there are no options, make it hidden or else the game will think this is a normal event
	
	immediate = {
		random_diplomatic_play = { # this searches for and scopes to a diplomatic play that meets the criteria specified in the "limit" block
			limit = { # this is where you tell the game what exactly you want it to look for
				is_war = yes
				any_scope_play_involved = {
					THIS = ROOT # THIS means the "current scope", in this case the "THIS" is any_scope_play_involved
				}
				NOR = { # Means "not or"; returns true only if all contained triggers are false
					initiator = ROOT # initiator and target is the event target of diplomatic_play
					target = ROOT
				}
			}
			initiator = { # this scope is only available in the diplomatic_play scope
				save_scope_as = initiator_scope # So if we want to use it later, we use this effect to provide a reference for it later
			}
			target = {
				save_scope_as =  target_scope
			}
			if = { # the contents of an "if" effect are only executed if its "limit" block is satisfied
				limit = { # place your triggers in this block
					ROOT = { # We want to evaluate this from the ROOT scope
						is_diplomatic_play_enemy_of = scope:initiator_scope
					}
				}
				if = { # you can nest "if" effects inside of other "if" effects to provide more dynamism to your events
					limit = {
						scope:initiator_scope = { # This is the scope we saved earlier, but used an effect that doesn't have access to "scope:initiator"
							infamy >= infamy_threshold:infamous 
						} 
					}
					ROOT = { change_infamy = 5 }
				}
				ROOT = {
					set_owes_obligation_to = {
						country = scope:target_scope
						setting = yes
					}
				}
				remove_target_backers = { ROOT } # The remove_target_backers effect only works in the  diplomatic_play scope, which was provided by random_diplomatic_play.
			}
		}
	}

}
```

## 事件模板

以下是一个普通事件的模板：

```
temp_event.123 = {
	type = country_event
	placement = root
	
	title = temp_event.123.t
	desc = temp_event.123.d
	flavor = temp_event.123.f
	
	event_image = {
		video = "######"
	}
	
	icon = "gfx/interface/icons/event_icons/event_######.dds"
	
	on_opened_soundeffect = "event:/SFX/UI/Alerts/event_appear"
	
	duration = 3
	
	trigger = {
	}
	
	cancellation_trigger = {
	}
	
	cooldown = {
	}	
	
	immediate = {
	}
	
	option = {
		name = temp_event.123.a
		default_option = yes
	}
	
	option = {
		name = temp_event.123.b
	}
	
	after = {
	}

}
```

以下是一个隐藏事件的模板：

```
temp_event.123 = {
	type = country_event
	hidden = yes
	
	trigger = {
	}

	immediate = {
	}
	
}
```

## 参考

Mod 制作（Modding）
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier 类型](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [决议](Decision modding.md) • 事件（Events） • [历史](History modding.md) • [日志](Journal modding.md) • [修正](Modifier modding.md) • 目标（Objectives） • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [建筑](Building modding.md) • [人物](Character modding.md) • 概念（Concepts） • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党（Parties） • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型（Subject types） • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [可自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图像](Event images.md) • [图形资产](Graphical asset modding.md) • 字体（Fonts） • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐（Music） • [音效](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [Mod](Mod.md) • [Mod 兼容性](Mod compatibility.md) • [Mod 结构](Mod structure.md) • [脚本测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [Mod 翻译](Mod translation.md) • [新国家 Mod 制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州 Mod 制作指南](State modding guide.md) |
|---|---|