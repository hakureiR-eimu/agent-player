---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Handbook for Victoria 3 Interface Scripting
source: https://vic3.paradoxwikis.com/Handbook_for_Victoria_3_Interface_Scripting
pageid: 10117
categories: [Potentially_outdated, 1.9, Modding]
fetched: 2026-10-27
---
**用户界面**（User Interface）是玩家与《维多利亚3》交互的方式。界面使用一种自定义脚本语言编写。这种语言没有官方名称，但被 Modding Co-op 称为"**GUIscript**"。目前它的文档非常匮乏，可读性也不如 [PDXscript](Introduction to the Paradox Scripting Language.md)。

**GUIscript** 用于 `/game/gui` 和 `jomini/gui` 文件夹中的内容。

仅在界面中完成的操作被称为*"in gui"*完成，或者在未使用脚本侧功能时称为*"pure gui"*。

*注意：本指南不涵盖用于脚本化游戏内容的 Paradox 脚本语言。*

请协助验证或更新本文中较旧的章节。至少有部分章节最后是针对 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.9 验证的。

## 概述

### 基本原则

原则上，GUIscript 类似于 HTML。一个 `.gui` 文件是**父**（parent）组件及其**子**（children）组件构成的树。每个组件要么创建一个 UI 控件，要么为其子组件设置属性。

```
window = {
    name = "my_panel"
    parentanchor = center
    size = { 500 300 }

    background = {
        using = default_background
    }

    vbox = {
        spacing = 8
        margin = { 16 16 }

        textbox = {
            text = "MY_PANEL_TITLE"
            fontsize = 22
        }

        textbox = {
            text = "MY_PANEL_BODY"
            autoresize = yes
            multiline = yes
        }

        button = {
            using = default_button
            size = { 0 40 }
            text = "MY_PANEL_CLOSE"
            onclick = "[PdxGuiWidget.AccessParent.AccessParent.Hide]"
        }
    }
}
```

例如，上面的脚本可以这样解释：

- 创建一个 `window`，其 `name` 为 "my_panel"，锚定在其父组件的 `center`，`size` 为 500px × 300px，并带有一个 `background`
- 在 `background` 中，插入由模板 `default_background` 定义的设置
- 在 `window` 中，创建一个 `vbox`，其边距为 16px × 16px，子组件之间的 `spacing` 为 8px
- 在 `vbox` 中，创建两个 `textbox` 控件和一个 `button` 控件，各有各的设置

从这个例子中，我们可以总结出 GUIscript 的以下要点：

- 文件中的顺序决定了屏幕上的顺序：代码中“靠后”的内容会较晚创建
- 大多数控件也可以包含其他控件。例如，一个 `button` 里可以有一个 `icon`，里面再有一个 `textbox`。嵌套元素，即**子组件**，会随其父组件一起移动，并可以继承父组件的属性
- 控件的位置相对于左上角（屏幕或父组件的左上角）设置。这可以通过 `parentanchor` 属性来改变
- 每个元素都用花括号打开和关闭，像这样：`container = { }`

还有一些值得尽早了解的重要信息：

- 键要么是**控件种类（widget kind）**，要么是**属性（property）**。
  - `vbox`、`textbox`、`button` 和 `background` 创建控件
  - `size`、`spacing`、`text` 和 `onclick` 在所在控件上设置属性
- `text` 属性默认是一个**本地化键（localization key）**。
  - 在上面的例子中，`"MY_PANEL_TITLE"` 会在本地化文件中查找，而不是按字面打印
- 子组件从父组件**继承属性**。在 `[]` 中调用的任何内容都是使用控件的**datacontext**求值的表达式。
  - 在上面的例子中，可以看到 `button` 控件从自身上下文出发，经过两次父组件的上下文切换后，在其顶层父组件上执行 `Hide` 命令

### 文件结构

用户界面由 `/game/gui` 和 `jomini/gui` 文件夹中的文件定义。

- 与脚本化内容一样，gui 文件可以用任何文本编辑器编辑，并以纯文本形式存储。
- 任一 `/gui` 目录中的所有文件都会被加载。游戏引擎会忽略文件夹结构，*脚本化控件的情况除外*

《维多利亚3》将绝大多数图形资产存储为 `.dds` 文件。这些文件位于 `/gfx` 文件夹中。引擎在大多数情况下也可以接受 `.png` 文件，尽管这种格式通常空间效率较低。

#### GUI 调试

使用 `-debug_mode` 启动选项启动游戏，可以对 .gui 文件的更改进行热加载。

引擎会在每次保存时重新加载 .gui 文件。重新加载通常是即时的，不过较大的更改可能引起界面更全面的重新加载。

#### 局限

- 只能在具有链接 function 的上下文之间切换。例如，如果不使用脚本向 GUI 传递一个 scope，就无法在两个国家之间切换上下文

- 不使用 sgui 的话，GUI 无法任意访问脚本。

## 界面脚本与构建

### 界面是如何构建的

《维多利亚3》中显示的画面由三个协作层产生：

```
   .gui file                      engine                      game script
┌──────────────────┐        ┌──────────────────┐        ┌──────────────────┐
│ widget tree      │  ───▶  │ layout, drawing, │  ◀───  │ triggers/effects │
│ + properties     │        │ input, animation │        │ scopes, values   │
│ + [ expressions ]│        │                  │        │ localisation     │
└──────────────────┘        └──────────────────┘        └──────────────────┘
```

游戏中的每个界面都由这些元素组成：

1. **结构。** `.gui` 文件声明一棵控件树并在其上设置属性。这是你最常打交道的部分。
2. **呈现。** 引擎负责布局、绘制这棵树，路由鼠标和键盘输入，并运行动画。这
3. **内容。** 数据绑定表达式、脚本化 GUI 和本地化提供文本、数字、列表和操作。

#### 控件

界面使用**控件（widget）**构建。在《维多利亚3》中，控件是屏幕上一个附有行为的矩形。每个控件都有：

| **种类** | 它是什么（`window`、`vbox`、`button`、`textbox`、`icon` 等） |
|---|---|
| **属性** | 它如何定位、绘制和交互等。 |
| **子组件** | 嵌套在其中的其他控件。 |

控件的子组件绘制在其上方并随其移动。没有单独的“添加子组件”调用：嵌套*即是*父子关系。

### 内置 UI 组件

《维多利亚3》提供了若干基本组件（种类）来构建界面。种类写作块的键：

```
vbox = {             # vbox is the kind
    spacing = 4
    textbox = { }    # textbox is the kind
}
```

#### 布局控件

| 种类 | 用途 |
|---|---|
| `container` | 子组件保持各自绝对位置的控件。没有固定大小（但可以设置 maximumsize）。自动调整大小以容纳所有子组件，包括不可见的。使用 ignoreinvisible = yes 来忽略它们。常用于将多个元素编组以便一起移动。 |
| `dynamicgridbox` | 仅与 datamodel 一起使用。将所有条目垂直排列。使用 flipdirection = yes 可使其水平。默认不忽略不可见条目。使用 ignoreinvisible = yes 来改变这一点。由内容调整大小，并受 minimumsize 和 maximumsize 限制。条目大小可以不同。列表非常长时可能变得卡顿。 |
| `fixedgridbox` | 类似于动态框，但所有条目大小固定（本质上是一个表格）。仅与 datamodel 一起使用。将所有条目垂直排列。使用 flipdirection = yes 可使其水平。无法忽略不可见条目。可以是固定大小，由内容调整大小并受 minimumsize 和 maximumsize 限制。对于长列表，性能要好得多。 |
| `flowcontainer` | 将所有子组件排成一行水平排列，并调整大小以容纳它们。使用 direction = vertical 可使其垂直。空间不足时会将其子组件换行到新行或新列。默认不忽略不可见子组件。使用 ignoreinvisible = yes 来改变这一点。不能有固定大小。其子组件不能有位置，因为位置是自动设置的。如需调整其子组件的位置，可以将其放入一个 container 或 widget 中，然后相对这个父组件改变位置。 |
| `hbox` / `vbox` | 将所有子组件排成一行水平排列，并沿其宽度分布。Vbox 相同但为垂直方向。不能有固定大小，而是根据布局策略调整大小以容纳子组件或匹配父组件大小。可受 minimumsize、maximumsize、min_width、max_width 和边距限制。默认忽略不可见子组件。使用 ignoreinvisible = no 来改变这一点。可以选择接受 datamodel（从游戏数据创建列表）。 |
| `margin_widget` | 在单个子组件周围保留边距。类似于 widget，但可以通过边距调整大小。这使我们能够制作适应不同尺寸屏幕的窗口，方法是将高度设为 100%，边距设为约 50 以显示 hud。 |
| `overlappingitembox` | 仅与 datamodel 一起使用。将所有条目水平排列，当列表长于框的大小时使条目重叠。使用 flipdirection = yes 可使其水平。可以是固定大小或自动调整大小。 |
| `scrollarea` | 带滚动条的视口，当内容大于其大小时滚动条会出现。可用 scrollbarpolicy_horizontal = always_off 和 scrollbarpolicy_vertical = always_off 禁用滚动条。可以是固定大小，由内容调整大小并受 minimumsize 和 maximumsize 限制。游戏文件主要使用 scrollbox 类型，它是带背景、滚动条和边距的 scrollarea。 |
| `stackedwidget` | 一次显示其一个子组件，按索引选择。 |
| `tabbar` | tabwidget 使用的按钮条。 |
| `tabwidget` | 带标签页的容器：一个标签条加一个 stacked widget。 |
| `widget` | 基础控件。一个可以定位、贴图、显示或隐藏的裸矩形，自身没有布局行为。点击它不会将其带到最前。如果子组件位于窗口之外，它将不可点击，也不会显示提示。使用 allow_outside = yes 来改变这一点。 |
| `window` | 可拖动、可调整大小的顶层容器。要启用移动，添加 movable = yes 属性。可以是固定大小或由子组件调整大小。如果子组件位于窗口之外，它将不可点击，也不会显示提示。使用 allow_outside = yes 来改变这一点。点击窗口会将其带到共享同一层的其他窗口之前。使用 PdxGuiWidget.StackTop 或 PdxGuiWidget.StackBottom 来操纵顺序。 |

#### 交互控件

| 种类 | 用途 |
|---|---|
| `button` | 可点击的控件，具有悬停/按下/禁用视觉状态。接受 onclick 和 onrightclick。添加右键功能时，需包含 button_ignore = none。默认没有纹理。可以是固定大小或由子组件调整大小。没有大小的按钮可用于添加不可见的热键。 |
| `button_group` | 使一组 checkbutton 互斥。 |
| `checkbutton` | 带选中状态的切换按钮。 |
| `colorpicker` | HSV/RGB 颜色选择弹窗。 |
| `dropDown` | 可折叠的可选项列表。 |
| `scrollbar` | 带递减/递增按钮的可拖动条。 |

#### 文本控件

| 种类 | 用途 |
|---|---|
| `editbox` | 可编辑的单行文本字段。 |
| `textbox` | 不可编辑的文本块，可选内联图标和文本格式。可以是固定大小或自动调整大小。使用 elide = right 或 elide = left 来截断过长的文本。可以单行或多行，用 multiline = yes。游戏文件主要使用 gui/shared/text.gui 中定义的类型，如 text_single。使用它们可以保持视觉一致，并减少每次输入的代码量。 |
| `texticon` | 字符串中可嵌入图标标记的 textbox。 |

#### 视觉控件

| 种类 | 用途 |
|---|---|
| `background` | 绘制在其父控件之后的纹理。 |
| `icon` | 绘制纹理（可选精灵图集），可带修改纹理和发光。可用作存放子组件的控件。可用 mirror = horizontal 或 mirror = vertical 翻转。 |
| `line` | 在多个点之间绘制的折线或样条线。 |
| `minimap` | 渲染地图小地图纹理。 |
| `minimap_window` | 承载小地图的窗口。 |
| `piechart` | 饼图容器。 |
| `pieslice` | 饼图的一个切片。 |
| `plotline` | 在一系列点上的折线图。 |
| `progressbar` | 显示某一范围内取值的水平或垂直条。 |
| `treemapchart` | 矩形树图容器。 |
| `treemapslice` | 矩形树图的一个切片。 |

### 控件属性

属性是简单的 `key = value` 条目。用于控制给定控件种类可用的设置。

| 形式 | 写法 | 示例 |
|---|---|---|
| 布尔值 | `yes` / `no` | `visible = no` |
| 数字 | 数字，可选小数或带 `%` | `spacing = 10`，`size = { 100% 40 }` |
| 向量 | 花括号中的两个或更多数字 | `position = { 8 30 }` |
| 颜色 | 0..1 范围内的四个数字 | `tintcolor = { 0 0 0 0.6 }` |
| 标记 | 裸标识符 | `direction = vertical` |
| 标志组合 | 由 `\|` 连接的标识符 | `parentanchor = bottom\|hcenter` |
| 字符串 | 带引号 | `texture = "gfx/..."` |
| 表达式 | 带引号，以 `[` 开头 | `visible = "[IsInGame]"` |
| 块 | 花括号 | `size = { 280 132 }` |

### 数据绑定与继承

当控件需要访问或修改游戏状态时，使用**命令（command）**。命令表达式放在带引号的方括号 `"[]"` 中，作为控件属性传入。`"[]"` 中的所有内容由游戏的数据绑定引擎求值。它从控件的 `datacontext` 出发，能够链式调用 function 和访问属性，类似于 PDXscript 中的点链接。例如：

```
visible  = "[Character.IsValid]"
text     = "[Character.GetName]"
tooltip  = "[Character.GetTooltip]"
onclick  = "[CharacterPanel.SelectCharacter(Character.Self)]"
```

两个属性控制表达式在运行时可以访问的内容：

- `datacontext` 将一个新对象作为该控件及其所有子组件的 `"[]"` 根。默认情况下，控件继承其父组件的 datacontext。
- `datamodel` 将一个集合传入容器，容器为 datamodel 中的每个条目实例化其 `item` 块作为子组件。通常，每个子组件会自动继承其从 datamodel 获得的特定对象的 datacontext。

```
dynamicgridbox = {
    datamodel = "[GetPlayer.GetStates]"
        item = { 
            textbox = {
                text = "[State.GetName]" 
            }
        }
    }
}
```

在上面的例子中：

- 引擎被指示创建一个 `dynamicgridbox` 控件。
- `datamodel` 属性首先使用 `GetPlayer`（返回玩家的国家）切换上下文，然后使用 `GetStates` 获取一个 datamodel，其中包含该国所有州（State）的列表。
- `item` 告诉引擎为 `GetStates` 提供的 datamodel 中的每个对象创建一个控件
- 传入 `item` 的任何种类或属性都定义了生成的子控件将包含的内容。

#### Promote 与 Function

数据绑定引擎通过“上下文”运作。这些在很多方面类似于 PDXscript 的 scope。预定义的命令——promote 和 function——用于在对象之间移动、变换对象或获取信息。

- **Promote** 返回一个游戏对象，例如 `Country.GetCapital` 会将你的上下文切换到该国的首都
- **Function** 返回数字、字符串或布尔值。例如 `Country.GetArmyPowerProjection` 会返回该国陆军力量投射的数值

### 系统变量

### 类型转换

## 控件用法与属性

### window

### widget

### container

### dynamicgridbox / fixedgridbox

### flowcontainer

### hbox / vbox

### scrollarea

## 视觉与外观

### 纹理

### 动画

## 交互
### 回调（Callbacks）

### 工具提示（Tooltips）

### 焦点（Focus）

## 用户自定义类型与模板

### 类型

### 模板

### 宏（Macros）

## 脚本化 GUI（Scripted GUIs）

### 文件结构

### 调用一个 SGUI

## 脚本化部件（Scripted Widgets）

### 创建脚本化部件

### 注册脚本化部件

## 故障排除

### 已知的崩溃原因

- 在 hbox 和 vbox 上设置 100% 大小
- 在 `flowcontainer` 内使用 `hbox` 或 `vbox`
- 在同一个父节点的多个子节点上设置 `resizeparent = yes`
- 类型引用自身，这会导致加载界面无限循环，直到内存耗尽

### 部件不出现/不消失

- 语法错误，例如缺少括号或引号
- 检查部件的 `visible` 属性是否有错误
- 确保你的类型设置正确，它们需要嵌套的 `types { type { } }` 语法，即使你只在该文件中创建了一个类型

## 参考

Modding（模组制作）
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本化内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本化类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
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