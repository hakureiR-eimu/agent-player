---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Troubleshooting
source: https://vic3.paradoxwikis.com/Troubleshooting
pageid: 9664
categories: [1.13, Modding]
fetched: 2026-10-27
---
本文已针对当前游戏[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

**故障排查（Troubleshooting）**是查找 Bug 或其他问题并修复它们的过程。有多种工具和流程可帮助进行故障排查，其中最重要的是错误日志。

## 错误日志

激活 [debug_mode](Console commands.md) 后，可以点击屏幕右下角的错误图标来访问错误日志，也可以前往 `logs` 文件夹查看。

根据操作系统的不同，`logs` 文件夹位于不同的位置：

| 操作系统 | 路径 |
|---|---|
| Windows | %USERPROFILE%/Documents/Paradox Interactive/Victoria 3/logs/ |
| Linux | ~/.local/share/Paradox Interactive/Victoria 3/logs/ |
| Mac OS | ~/Documents/Paradox Interactive/Victoria 3/logs/ |

游戏启动时或当前日志文件过长时，错误日志会被拆分为多个文件。最新的日志条目文件名为 `error.log`。最旧的日志文件通常命名为 `error.5.log`。

### 分析错误日志条目

错误日志中的每个条目，其严重程度可能从灾难性到无关紧要不等。但错误日志本身并不会表明错误的严重程度。

错误日志由发生时间、错误类型的标识以及附加信息组成：

```
 [23:38:26][jomini_eventmanager.cpp:376]: Event cristo_redentor.1 is orphaned
```

例如这条错误发生在 `23:38:26`，是一个事件错误（`[jomini_eventmanager.cpp:376]`），意思是事件 `cristo_redentor.1` 没有被任何 [effect](Effect.md)、[on_action](On action.md) 或类似机制触发。这可能是刻意为之，也可能是需要修复的 Bug。

下面这条错误也是如此：

```
 [23:38:26][jomini_effect.cpp:1135]: Variable 'foo' is set but is never used. Note that use in localization doesn't count due to technical limitations. Use in unused scripted triggers and effects also does not count
```

它的意思是变量 foo 已被设置，但没有在任何 trigger（触发条件脚本）中使用。如果该变量仅用于在 localization（本地化文本）中显示某些内容，这可能是有意为之；但也可能表明它在某处被拼错了。

如果该变量确实不需要被使用，你可以在一个实际不会用到的 trigger 中使用它，以便将该错误从日志中移除。

#### 在脚本中定位错误来源

某些错误会导致错误日志被大量错误信息淹没。其中一种错误信息如下所示：

```
 [08:39:29.969](debug:268): [2026-05-12 08:39:29.192] [cw] [error] [pdx_persistent_reader.cpp:268] Error: "Unexpected token: character_role_prefix_thief, near line: 129" in file: "common/character_roles/prefix_character_roles.txt" near line: 135
```

它指出某个特定文件（`common/character_roles/prefix_character_roles.txt`）中特定行（`near line: 129"`）上或附近存在错误，还说明了具体是什么内容（`character_role_prefix_thief`）因为“意外”（`Unexpected token`）而造成了困惑。

第一步应该是查看该文件以找出问题的原因（注意指定行附近的行也很重要，所以最好不要只看那一行）：

```
character_role_prefix_inspector = {
	texture = "gfx/interface/icons/character_role_icons/prefix_inspector_role.dds"

	title_format = custom

	priority = 20

	spawn_characters_to_pool = no

### Criminals ###

character_role_prefix_thief = {
	texture = "gfx/interface/icons/character_role_icons/prefix_thief_role.dds"

	priority = 20

	spawn_characters_to_pool = no
}

character_role_prefix_crime_boss = {
	texture = "gfx/interface/icons/character_role_icons/crime_boss_role.dds"

	priority = 25

	spawn_characters_to_pool = no
}
```

单看 `character_role_prefix_thief` 条目，似乎没有任何问题。但第 125 行存在错误：那里缺少一个右花括号，这导致数百条错误涌入了错误日志。这是因为缺失的花括号会导致其下方的所有定义失效，进而可能在使用 `character_role_prefix_thief` 及其他人物角色的其他文件中引发更多错误。

因此，通常最好从最上方的错误入手，看看它是否会导致其他错误的出现。

## 定位崩溃来源

大多数情况下，小的错误不会导致游戏崩溃，但在某些极端情况下仍有可能发生。这种情况下，错误日志往往无法帮助定位问题，因为游戏在记录错误之前就已经崩溃了。

因此，掌握寻找崩溃来源的方法或了解最可能的元凶非常重要。

### 分而治之

**分而治之（divide and conquer）**策略是一种在庞大文件或文件集合中快速定位问题的方式。在《维多利亚3》的故障排查中，它通常有助于定位崩溃来源，尤其是在游戏启动时发生崩溃的情况下。

使用分而治之法时，需要删除 mod 的一半文件，然后查看游戏是否仍然崩溃。如果仍然崩溃，问题很可能出在保留的那一半文件中。如果游戏不再崩溃，则问题出在被删除的那一半文件中。

这个过程可以反复进行，直到找出引发问题的文件。但这种方法并非总是有效，因为有时崩溃只发生在需要多个文件协同运作的特定情况下。

### 崩溃来源示例

| 原因 | 说明 |
|---|---|
| 人物模板中不存在的特质 | 不存在的特质可能在创建人物时导致游戏崩溃。 |
| geographic_region 文件中的错误 | geographic_region 文件似乎经常因拼写错误之类的问题而导致崩溃。 |

### 已知错误日志代码列表

| 代码 | 说明 |
|---|---|
| [jomini_eventmanager.cpp:376] | 事件错误 |
| [jomini_effect.cpp:1135] | 变量错误 |

## 调试日志

调试日志（debug log）是另一个有用的文件，可以提供有助于调试的信息。

## 参考资料

Mod 制作
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
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

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • 故障排查 |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|