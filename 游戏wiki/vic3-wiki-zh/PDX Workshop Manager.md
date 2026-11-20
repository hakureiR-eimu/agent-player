---
translated: 2026-10-27
translator: machine (glm-5.3)
title: PDX Workshop Manager
source: https://vic3.paradoxwikis.com/PDX_Workshop_Manager
pageid: 9897
categories: [Modding_tools, Modding]
fetched: 2026-10-27
---
Mod 工具
: PDX Workshop Manager
PDX Workshop Manager
---

类型
Steam 创意工坊
---

作者
Bahmut
---

状态
已发布
---

Github
链接
---

其他
下载
PDX Workshop Manager
---

类型
Steam 创意工坊
---

作者
Bahmut
---

状态
已发布
---

Github
链接
---

其他
下载
**pdx-workshop-manager** 是一个用于发布 P 社（Paradox）mod 到 Steam 创意工坊的工具，可以以可重复、可配置的方式进行发布。

提供 **Windows** 和 **Linux** 版本。如有需要，也可以添加 **MacOSX** 版本。

感谢 [nnnn20430](https://github.com/nnnn20430) 为原版 steamworks API 创建了基于 Go 语言的封装。

## 功能特性

- 根据配置或 `metadata.json` 更新不同语言的创意工坊**名称**
- 根据 `metadata.json` 中的标签更新创意工坊**标签**
- 根据配置的文件更新不同语言的创意工坊**描述**
- 更新创意工坊**缩略图**
- 根据配置的目录为创意工坊更新添加**更新说明**（change note）

## 工作原理

该工具会解析单个已配置 mod 或每个已配置 mod 的 `metadata.json`，然后将该 mod 发布到 Steam 创意工坊。

## 配置

该工具使用一个 json 文件进行配置。

### 属性

- **必填** `game` 要上传到的游戏的 steam app id
- **必填** `mods` 可上传的 mod 列表
- **必填** `id` 要上传的 mod 的 id，若保持为 `0`，则首次上传时会创建该 mod，并用新创建的 id 替换该值
- **必填** `directory` mod 的位置，可以是相对可执行文件的路径，也可以是绝对路径
- **必填** `thumbnail` 位于 mod 目录中的缩略图文件（默认为 `thumbnail.png`）
- **可选** `names` Steam [api 语言代码](https://partner.steamgames.com/doc/store/localization/languages) 到本地化 mod 名称的映射（默认为 `metadata.json` 中定义的名称）
- **可选** `descriptions` Steam [api 语言代码](https://partner.steamgames.com/doc/store/localization/languages) 到包含本地化 Steam 描述 bbcode 的文件的映射
- **可选** `change-note-directory` 包含基于版本的更新说明文件的目录（参见更新说明）

### JSON 配置示例

```
{
  "game": 529340,
  "mods": [
    {
      "id": 0,
      "directory": "/Path/To/Mod",
      "thumbnail": "thumbnail.png",
      "names": {
        "english": "Your mod name"
      },
      "descriptions": {
        "english": "/Path/To/Bbcode/File/STEAM_PAGE.bbcode"
      },
      "change-note-directory": "/Path/To/Change/Note/Directory"
    }
  ]
}
```

## 添加创意工坊更新说明

如果定义了 `change-note-directory`，应用程序会尝试添加更新说明。

它会读取 `metadata.json` 中的 `version` 属性，并在末尾加上 `.bbcode`。

因此，如果某个 mod 的版本为 `1.0.1`，它会在更新说明目录中尝试查找名为 `1.0.1.bbcode` 的文件。

**注意**：如果没有对应的更新说明，上传**不会**失败，只会在控制台输出中给出警告。

## 用法

首先从仓库的 Releases 页面下载最新版本：

- https://github.com/kaiser-chris/pdx-workshop-manager/releases

该 ZIP 文件可能被标记为*病毒*。这是**误报**！

如果你不信任它，可以自己构建。

### 图形界面

下载 GUI 版本，解压后直接运行随附的可执行文件。

应用程序会打开一个新的浏览器窗口显示 GUI。

它允许你设置要上传的 mod 并执行上传。**请务必在点击上传之前保存你的更改。**

**注意**：如果没有打开浏览器窗口，你可以在命令行窗口中找到 GUI 的链接。

### 命令行

完成配置后，你可以双击运行应用程序，或者在终端中像这样运行它：

```
.\pdx-workshop-manager.exe
```

默认情况下，应用程序要求配置文件与可执行文件位于同一文件夹中，并会上传其中配置的**所有** mod。

**注意**：该工具需要 Steam 正在运行且已登录才能工作！

所有可选命令都可以在帮助对话框中找到。帮助对话框（`.\pdx-workshop-manager.exe -h`）：

```
Usage of pdx-workshop-manager:
  -config string
    	Path to the config file (default "manager-config.json")
  -mod uint
    	Configured workshop mod id or 0 for all mods (default 0)
```

### 使用小贴士

如果你不知道如何在 Windows 上打开命令行：

- 打开包含 `pdx-deepl.exe` 的文件夹
- 点击资源管理器顶部的地址栏
- 清空内容
- 输入 `cmd` 并按回车
- 现在你应该已经打开了一个命令行窗口

## 参考
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

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|