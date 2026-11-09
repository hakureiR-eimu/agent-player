---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Interface modding
source: https://vic3.paradoxwikis.com/Interface_modding
pageid: 7398
categories: [Potentially_outdated, 1.9, Modding]
fetched: 2026-10-27
---
**用户界面**（User Interface）是玩家与《维多利亚3》交互的方式。该界面使用一种自定义脚本语言编写。这种语言没有官方名称，但被 Modding Co-op 称为"**GUIscript**"。目前它的文档极为匮乏，可读性也不如 [PDXscript](Introduction to the Paradox Scripting Language.md)。

**GUIscript** 用于 `/game/gui` 和 `jomini/gui` 文件夹中的内容。

仅在界面中完成的操作被称为*"在 gui 中"*完成，或者在不使用脚本端功能时被称为*"纯 gui"*。

*注意：本指南不涵盖用于游戏玩法脚本内容的 Paradox 脚本语言。*

请协助验证或更新本文中较旧的章节。其中至少有一部分最后是在 [版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.9 下验证的。

## 概述

用户界面由 `/game/gui` 和 `jomini/gui` 文件夹中的文件定义。

原则上，GUIscript 类似于 HTML。与脚本内容一样，gui 文件可以使用任意文本编辑器编辑，并以纯文本形式存储。

《维多利亚3》的绝大部分图形资源以 `.dds` 文件存储，位于 `/gfx` 文件夹中。引擎在大多数情况下也可以接受 `.png` 文件，但这种格式通常空间效率较低。

使用 `-debug_mode` 启动项启动游戏后，你可以热加载 .gui 文件的改动。引擎会在每次保存 .gui 文件时重新加载它们。重新加载通常是即时的，不过大规模的改动可能引起界面更全面的重新加载。

#### Promote 与 Function

界面通过“context（上下文）”运作。它们在很多方面类似于 PDXscript 的 scope。预定义的命令——promote 和 function——用于在对象之间移动、转换对象或获取信息。

- promote 返回一个游戏对象，例如 `Country.GetCapital` 会将你的 context 切换到该国的首都
- function 返回数字、字符串或布尔值。例如 `Country.GetArmyPowerProjection` 会返回该国陆军力量投射的数值

#### 类型转换

#### GUI 调试

#### GUI 编辑器

## 界面脚本

#### UI 组件概述

#### Flowcontainer

#### hbox 与 vbox

#### 动画状态

#### Datamodel 与 Datacontext

## 模板与类型

### 模板

模板只是属性的容器。因此 `using = template_name` 只是把模板块中的所有属性（如 `size` 等）以及 widget/容器添加到当前的 widget/容器中。

**定义模板**

在 `game/gui` 文件夹中新建一个 `.gui` 文件（也支持子文件夹）：

```
template example_template {
    container = {
        # Some container
    }

    # Properties
    size = { 100 100 }
}
```

### 类型

类型本身就是 widget/容器，允许复用并覆写其中的属性。

**定义类型**

在 `game/gui` 文件夹中新建一个 `.gui` 文件（也支持子文件夹）：

```
types my_types {
    # Base type
    type example_base_type = widget {
        # Anything you want

        # Defining a set of overwritable properties or widgets/containers
        block "test_block" {
            size = { 100 100 }
        }
    }

    # Extended type
    type extended_example_type = example_base_type {
        # Anything you define here will be added at the bottom of the base type

        # Overwriting a predefined block
        blockoverride "test_block" {
            size = { 200 200 }
        }
    }
}
```

### 使用类型

类型可以在任何地方引用，包括在其他类型中：

```
widget = {
    # Using the type as is
    example_base_type = {}

    # Overwriting a block in the type
    example_base_type = {
        # Overwriting a predefined block
        blockoverride "test_block" {
            size = { 200 200 }
        }
    }

    # Extending the type
    example_base_type = {
        widget = {
            # This widget will be added at the bottom of the existing content
        }
    }
}
```

## 脚本化 Widget

### 搭建窗口

为你想要实现的窗口创建一个类型。

以下是一个侧面板的示例：

```
type example_side_panel = default_block_window {
    # Important to make sure the window does not overlay other base game stuff
    layer = layer_ingame_menu
    
    # Decide visibility i.e. when should your window be shown
    # Best practice is using the GUI variable system
    visible = "[GetVariableSystem.HasValue('com_open_window', 'example_side_panel')]"

    # Adding this to the show state is important otherwise your window may be overlayed by
    # base game windows or not close base game windows correctly
    # See the base game for how to set sound effects and other stuff here
    blockoverride "animation_state_block" {
        state = {
            name = _show
            # Close other open panels before showing this one
            on_finish = "[InformationPanelBar.ClosePanel]"
            on_finish = "[MapListPanelManager.CloseCurrentPanel]"
        }
    }

    # Your window implementation
    # See base game panels for examples on how to set up
    # tabs, fixed bottoms and other stuff
}
```

对于全屏面板，上述要点同样适用，但要让窗口正常工作，你还需要隐藏一些 GUI 组件。为此，你可以覆写原版游戏的逻辑，或者使用 [Community Mod Framework](https://github.com/Victoria-3-Modding-Co-op/Community-Mod-Framework)。它提供了如何隐藏 GUI 元素的指南。全屏面板的主要区别在于它们基于另一个基础类型：

```
type example_full_screen_panel = fullscreen_block_window {
    # Same as side panel
}
```

### 将你的面板加入游戏

要将你的面板加入游戏，你需要创建一个脚本化 widget。

首先新建一个 GUI 文件并按如下方式设置：

```
widget = {
    name = example_panels
    layer = layer_ingame_menu
    size = { 100% 100% }

    # Full screen panels go here
    # Refer to them like this:
    example_full_screen_panel = {}

    vbox = {
        parentanchor = top|left
        layoutpolicy_horizontal = expanding
        layoutpolicy_vertical = expanding
        margin_top = 85 #margin topbar

        widget = {
            layoutpolicy_horizontal = expanding
            layoutpolicy_vertical = expanding

            hbox = {
                layoutpolicy_horizontal = expanding
                layoutpolicy_vertical = expanding

                # Side panels go here
                # Refer to them like this:
                example_side_panel = {}

                expand = {}
            }
        }
    }
}
```

接下来你需要注册你的脚本化 widget。为此，在 `game/gui/scripted_widgets/` 文件夹中新建一个 TXT 文件，并添加如下一行

```
gui/name_of_the_file_with_widget.gui = example_panels
```

## 故障排除

## 参考

Mod
返回顶部
| 文档 | [Defines](Defines.md) • [Effect](Effect.md) • [Event target](Event target.md) • [Scope](Scope.md) • [Trigger](Trigger.md) [宏](Macro.md) • [修改器类型](Modifier types.md) • [On action](https://vic3.paradoxwikis.com/On_actions) • [脚本值](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [决议](Decision modding.md) • [事件](Event modding.md) • [历史](History modding.md) • [日志](Journal modding.md) • [修改器](Modifier modding.md) • 目标 • [脚本化 GUI](Scripted gui.md) |
|---|---|

| 脚本类型 | [建筑](Building modding.md) • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | 界面 • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [可自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图片](Event images.md) • [图形资源](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [声音](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [Mod](Mod.md) • [Mod 兼容性](Mod compatibility.md) • [Mod 结构](Mod structure.md) • [脚本化测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [Mod 翻译](Mod translation.md) • [新国家 Mod 制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州 Mod 制作指南](State modding guide.md) |
|---|---|