---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Scripted gui
source: https://vic3.paradoxwikis.com/Scripted_gui
pageid: 3689
categories: [Potentially_outdated, 1.8, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。至少有部分内容最后核实的版本为 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.8。

Scripted GUI（脚本化图形界面）用于在点击 UI 中的按钮后执行 effect（游戏内效果脚本），或通过通常用于事件和 common 文件夹中的 trigger 代码来设置按钮或 UI 元素的有效性/可见性。它们以 .txt 文件的形式存储在 game/common/scripted_guis 中，并且无法在游戏中重载，这与 .gui 文件不同，你必须重启游戏才能使其生效/加载。

Scripted Gui 是 GUI 与代码之间的桥梁，这里将 `/common/` 中的代码称为 `code in code`，将 `/gui/` 中的代码称为 `code in GUI`。

code in code 中的代码实际上只是注册，除非在 code in GUI 中调用，否则它们不会产生效果。Scripted GUI 提供一个 effect 上下文和若干 trigger 上下文供 GUI 调用。

## 示例

### 按钮：

假设我们想创建一个按钮，为点击按钮的玩家添加一个日志条目。

#### 首先，我们在 game/common/scripted_guis 中的文件如下所示：

```
give_journal_entry_scriptedgui = {
    # remember that every code below just register multiple context TO BE USED in GUI. If GUI code not use them, they never effects
    
	scope = country 		# the root scope, i.e. the target of the effects
	saved_scopes = {
        saved_gdp
    } 		# any additional targets
    
    # These are scope, it should be added in GUI to effect.
    
	is_shown = {
        always = yes
    } 		# is it visible on the UI?
    
	ai_is_valid = {
        always = yes
    } 		# is the AI allowed to use it? Disabled by default.

	is_valid = {
        always = yes
    } 		# can the player use it?
    
    # Three trigger context, you can use them as you like whatever it used for vaild or shown
    
    effect = {			# what it does
		custom_tooltip = "I am the tooltip"	# adds a tooltip
        add_treasury = scope:saved_gdp
	}
}
```

#### 其次，我们在 GUI 文件中的按钮如下所示：

```
button = {
	using = default_button_action
    datacontext = "[GetScriptedGui('give_journal_entry_scriptedgui')]"
    visible = "[ScriptedGui.IsShown( GuiScope.SetRoot( GetPlayer.MakeScope ).End)]"
    enabled = "[ScriptedGui.IsValid( GuiScope.SetRoot( GetPlayer.MakeScope ).End)]"
    # you can use some code like visible = "[ScriptedGui.IsValid( GuiScope.SetRoot( GetPlayer.MakeScope ).End)]"， it's OK.
	size = { 250 50 }
	position = { 0 123 }
	text = "HIDE_AND_SEEK_BTN"
    tooltip = "[ScriptedGui.BuildTooltip( GuiScope.SetRoot( GetPlayer.MakeScope ).End)]"
	onclick = "[ScriptedGui.Execute( GuiScope.SetRoot( GetPlayer.MakeScope ).AddScope('saved_gdp', MakeScopeValue(GetPlayer.GetGDP)).End )]"
}

button = {
    using = default_button_action
    visible = "[GetScriptedGui('give_journal_entry_scriptedgui').IsValid( GuiScope.SetRoot( GetPlayer.MakeScope ).End)]"
    # you can use its 'is_vaild' context directly as you like
    size = { 250 50 }
	position = { 0 123 }
	text = "I_AM_ANOTHER_BTN"
}
```

## 参考

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • Scripted gui |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| 地图 | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • [States](State modding.md) |
|---|---|

| 界面 | [Interface](Interface modding.md) • [GUI script](GUI script.md) • [Localization](Localization.md) • [Customizable localization](Localization.md) • [Script localization](Script localization.md) |
|---|---|

| 图形 | [3D Models](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|

| 音频 | Music • [Sound](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|