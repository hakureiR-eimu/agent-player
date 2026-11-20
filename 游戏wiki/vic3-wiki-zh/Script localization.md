---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Script localization
source: https://vic3.paradoxwikis.com/Script_localization
pageid: 9549
categories: [1.13, Modding]
fetched: 2026-10-27
---
本文已针对游戏当前 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

**脚本本地化（Script localization）**可用于本地化 [effect](Effect.md) 和 [trigger](Trigger.md)，使其根据上下文显示不同的本地化文本。例如，某个 effect 在用于根国家（root country）时可能显示“瑞士获得 3 个 foo"，而在其他国家 scope 中与其他 effect 一起使用时则可能显示"该国获得 3 个 foo"。

脚本本地化还允许显示数值，例如来自带参数的 scripted effect 的数值。

## 设置脚本本地化

### 自定义描述

要使用脚本本地化，需要一个 `custom_description` 块来包裹需要本地化的 effect 或 trigger。根据脚本本地化最终的呈现方式，可以添加多种额外元素。

- `text`：`text` 链接到 common/effect_localization 或 common/trigger_localization 文件夹中的一个定义。它定义了在何种情况下使用哪条本地化字符串。

- `subject`（可选）：`subject` 需要一个 scope，并可在本地化字符串中被引用。它通常表示该 effect 或 trigger 的主体，如国家、人物等。
- `object`（可选）：`object` 与 subject 类似，也需要一个 scope，并可在本地化字符串中被引用。注意 subject 和 object 可以是不同类型。例如，subject 可以是国家，而 object 可以是人物。
- `value`（可选）：如果 effect 或 trigger 使用了 `value`（如变量或参数），只要在 value 中进行了定义，就可以在本地化字符串中引用它。

本地化字符串“瑞士从瑞典偷取 10 个 Foo”使用了这些引用：“`subject` 从 `object` 偷取 `value` 个 Foo"

在 scripted effect 中使用自定义描述的示例如下：

```
steal_x_foo_example_effect = {
	custom_description = {
		text = "steal_x_foo_example_effect"
		subject = this
		object = $TARGET$
		value = $AMOUNT$

		change_variable = {
			name = foo
			add = $AMOUNT$
		}
		$TARGET$ = {
			change_variable = {
				name = foo
				subtract = $AMOUNT$
			}
		}
	}
}
```

在这个 effect 中，subject（`this`）获得 `AMOUNT` 数量的 foo，而 object（`TARGET`）失去相同数量。

### 本地化定义

脚本本地化文件将 effect 的使用与特定的本地化字符串关联起来。根据 effect 的使用方式和使用位置，可以关联多条字符串。

一个 effect 本地化定义可以如下所示：

```
steal_x_foo_example_effect = {
	global = STEAL_X_FOO_EXAMPLE_EFFECT_POSITIVE
	global_neg = STEAL_X_FOO_EXAMPLE_EFFECT_NEGATIVE
	first = STEAL_X_FOO_EXAMPLE_EFFECT_FIRST_POSITIVE
	first_neg = STEAL_X_FOO_EXAMPLE_EFFECT_FIRST_NEGATIVE
	third = STEAL_X_FOO_EXAMPLE_EFFECT_THIRD_POSITIVE
	third_neg = STEAL_X_FOO_EXAMPLE_EFFECT_THIRD_NEGATIVE
}
```

`global`、`first` 和 `third` 定义了以下情况所使用的字符串：

- `first`：该 effect 用于根国家。
- `third`：该 effect 用于另一个国家，但只有这一个 effect 在该国的 scope 中执行。
- `global`：该 effect 用于另一个国家，且有多个 effect 在该国的 scope 中执行。

后缀 `_neg` 在 effect 为负面时使用。对于 effect 而言，这通常出现在使用了数值且该数值为负数的情况下。

截图中的示例展示了不同的 effect 本地化在游戏中的显示效果。

`STEAL_X_FOO_EXAMPLE_EFFECT_POSITIVE`

`STEAL_X_FOO_EXAMPLE_EFFECT_NEGATIVE`

`STEAL_X_FOO_EXAMPLE_EFFECT_FIRST_POSITIVE`

`STEAL_X_FOO_EXAMPLE_EFFECT_FIRST_NEGATIVE`

`STEAL_X_FOO_EXAMPLE_EFFECT_THIRD_POSITIVE` 与 `STEAL_X_FOO_EXAMPLE_EFFECT_THIRD_NEGATIVE`

### 本地化字符串

在脚本本地化定义中定义的本地化字符串本身也需要进行本地化。[本地化](Localization.md) 页面可以帮助理解和格式化本地化字符串。

`steal_x_foo_example_effect` 的字符串如下所示：

```
 STEAL_X_FOO_EXAMPLE_EFFECT_POSITIVE: "The Country steals $VALUE|0+$ [concept_foo] from [TARGET_COUNTRY.GetName]"
 STEAL_X_FOO_EXAMPLE_EFFECT_NEGATIVE: "The Country loses $VALUE|0-$ [concept_foo] to [TARGET_COUNTRY.GetName]"
 STEAL_X_FOO_EXAMPLE_EFFECT_FIRST_POSITIVE: "[COUNTRY.GetNameNoFlag] steals $VALUE|0+$ [concept_foo] from [TARGET_COUNTRY.GetName]"
 STEAL_X_FOO_EXAMPLE_EFFECT_FIRST_NEGATIVE: "[COUNTRY.GetNameNoFlag] loses $VALUE|0-$ [concept_foo] to [TARGET_COUNTRY.GetName]"
 STEAL_X_FOO_EXAMPLE_EFFECT_THIRD_POSITIVE: "[COUNTRY.GetName] steals $VALUE|0+$ [concept_foo] from [TARGET_COUNTRY.GetName]"
 STEAL_X_FOO_EXAMPLE_EFFECT_THIRD_NEGATIVE: "[COUNTRY.GetName] loses $VALUE|0-$ [concept_foo] to [TARGET_COUNTRY.GetName]"
```

注意，`COUNTRY` 是对 `subject` 国家的引用，而 `TARGET_COUNTRY` 是对 `object` 国家的引用。根据 object 和 subject 的类型，需要使用其他 GUI 提升（GUI promote）。例如，人物需要使用 `CHARACTER`。`object` 始终通过 `TARGET_` 前缀加上相应的 GUI 提升来引用。

`$VALUE$` 是一个引擎硬编码的本地化键，返回自定义描述中 `value` 参数的值。

## 参考

模组制作
返回顶部
| 文档 | [Defines](Defines.md) • [Effect](Effect.md) • [Event target](Event target.md) • [Scope](Scope.md) • [Trigger](Trigger.md) [宏](Macro.md) • [修改器类型](Modifier types.md) • [On action](https://vic3.paradoxwikis.com/On_actions) • [脚本值](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [决议](Decision modding.md) • [事件](Event modding.md) • [历史](History modding.md) • [日志](Journal modding.md) • [修改器](Modifier modding.md) • 目标 • [脚本化 GUI](Scripted gui.md) |
|---|---|

| 脚本类型 | [建筑](Building modding.md) • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [可自定义本地化](Localization.md) • 脚本本地化 |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图片](Event images.md) • [图像资源](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [声音](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [模组](Mod.md) • [模组兼容性](Mod compatibility.md) • [模组结构](Mod structure.md) • [脚本测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [模组翻译](Mod translation.md) • [新国家模组制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州模组制作指南](State modding guide.md) |
|---|---|