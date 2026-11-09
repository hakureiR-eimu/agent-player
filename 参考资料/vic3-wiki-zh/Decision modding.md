---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Decision modding
source: https://vic3.paradoxwikis.com/Decision_modding
pageid: 3455
categories: [Potentially_outdated, 1.10, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。至少部分内容最后核实于 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10。

决策（Decision）
**游戏文件夹 存储此类文件的游戏文件夹。 ：** `common/decisions`

---

**可注入 此类型是否可以使用 INJECT 数据库函数？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes **可替换 此类型是否可以使用 REPLACE 数据库函数？ ：** ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) yes

---

**相关游戏对象：** [事件](Event modding.md)、[日志条目](Journal modding.md)

[决策](Decision.md) 是可以在特定情况下执行的脚本化 effect（游戏内效果脚本）。决策定义于 /Victoria 3/game/common/decisions。

## 决策示例

决策包含两个脚本化的 [trigger](Trigger.md) 块、一个脚本化的 [effect](Effect.md) 块，以及一个 AI 概率 script value 块。

示例：

```
#Internal reference name of the decision
example_decision = {

	#Trigger block that determines whether the decision is shown to the player as a potential option
	is_shown = {
		this = c:ABC
		
		#A variable is often used to make sure the decision is not repeatable
		NOT = { has_variable = example_decision_taken }
	}

	#Trigger block that determines when a shown decision can actually be selected
	possible = {
		has_technology_researched = organized_sports
	}
	
	#The effects that are executed once the decision is taken
	when_taken = {
		trigger_event = {
			id = example_events.1
			popup = yes
		}
		
		#The variable referenced in the is_shown trigger/section
		set_variable = {
			name = example_decision_taken
		} 	
	}	
	
	#The chance/weight that the ai will take the decision, defaults to 1 if not specified. If chance is 0, the AI will not use the decision
	ai_chance = {
		value = 100
		<script_value>
	}
}
```

### 决策要素

| 要素 | 描述 | 作用域（Scope） |
|---|---|---|
| decision 脚本名 | 决策的内部脚本名称/标识符，必须唯一 | 无 |
| `is_shown = { }` | 一个 [trigger](Trigger.md) 块，决定决策是否出现在国家的潜在决策列表中 | 国家 |
| `possible = { }` | 一个 [trigger](Trigger.md) 块，决定已显示的决策何时可以使用 | 国家 |
| `when_taken = { }` | 一个 [effect](Effect.md) 块，在点击决策时触发 | 国家 |
| `ai_chance = { }` | 一个 [script value](Script value.md) 块，为 AI 国家在可用时使用该决策提供权重 | 国家 |

## 本地化

决策有以下 [localization](Localization.md) 键：

- <decision_script_name>：决策的名称/标题
- <decision_script_name>_desc：决策的描述/背景文本
- <decision_script_name>_tooltip：决策的提示框标题；默认情况下提示框包含决策的 `possible` trigger 和 `when_taken` effect；此 localization 键为这些部分添加一个标题。

## 参考

模组制作
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | 决策 • [事件](Event modding.md) • [历史](History modding.md) • [日志](Journal modding.md) • [修改器](Modifier modding.md) • 目标 • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [建筑](Building modding.md) • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [可自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图片](Event images.md) • [图形资源](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [声音](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [模组](Mod.md) • [模组兼容性](Mod compatibility.md) • [模组结构](Mod structure.md) • [脚本测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [模组翻译](Mod translation.md) • [新国家模组制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州模组制作指南](State modding guide.md) |
|---|---|