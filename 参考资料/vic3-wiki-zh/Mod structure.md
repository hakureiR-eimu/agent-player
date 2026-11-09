---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Mod structure
source: https://vic3.paradoxwikis.com/Mod_structure
pageid: 3814
categories: [Timeless, Modding]
fetched: 2026-10-27
---
本文是一篇[长期有效](https://vic3.paradoxwikis.com/Category:Timeless)的文章，适用于游戏的任何版本。

理解 mod 文件夹的结构是开始为《维多利亚3》制作 mod 的关键。

## mod 文件夹位置

默认情况下，本地 mod 所在的文件夹位于：

- Windows 和 MacOS：Users/[username]/Documents/Paradox Interactive/Victoria 3/mod
- Linux：home/[username]/.local/share/Paradox Interactive/Victoria 3/mod

请注意，《维多利亚3》无法加载任何文件路径中包含非 ASCII 字符的 mod。例如，当你的用户名包含带重音符号的字符或来自其他文字系统的字符时就会出现问题。你可以通过编辑 Steam/steamapps/common/Victoria 3/launcher/launcher-settings.json 中的 `"gameDataPath": "%USER_DOCUMENTS%/Paradox Interactive/Victoria 3",` 一行来更改本地 mod 的位置。例如，如果你把该行改为 `"gameDataPath": "C:/Paradox Interactive/Victoria 3",`，那么本地 mod 文件夹就会位于 C:/Paradox Interactive/Victoria 3/mod，而不是默认位置。

从 Steam 创意工坊下载的 mod 位于 Steam/steamapps/workshop/content/529340

请注意，这里有一个包含所有本地 mod 的总 mod 文件夹，以及每个 mod 各自专属的“mod 文件夹”。每个“mod 文件夹”应有一个清晰、唯一的名称，它对应于《维多利亚3》本体的 game 文件夹。

## 元数据

Mod 需要在 .metadata 文件夹内有一个 metadata.json 文件，以便为启动器提供额外信息。

元数据文件的基本结构如下所示：

```
  {
    "name" : "Mymod",                     /* Name of your mod as it should be displayed to players */
    "id" : "com.github.mymod",            /* Id of the mod, as chosen by the modder. This must be unique - we suggest using a reverse domain name 
                                             notation, but any string sufficiently unique will do. It is used when *other* mods refer to yours in relationships.
                                             Please note that the ID needs to be consistent over time. Do not include version numbers or change if you rename your
                                             mod, since that would wreck any relationships. Do not use the example ID given here! */
    "version" : "1.1",                    /* Version of your mod. The launcher will typically understand semantic versioning, others are hit-and-miss */
    "game_id" : "victoria3",              /* Game for which the mod is created. Should always be "victoria3", unless something is seriously off. Safety catch to 
                                             avoid games trying to load mods that are made for other games and violently crashing */
    "supported_game_version" : "1.0.4",   /* Version of the game for which your mod has been made. This works with "*" as a wildcard and "+" to indicate "or higher" */
    "short_description" : "Best mod!",    /* A description of your mod to be shown in popups or other places where longer texts or descriptions with 
                                             decorations won't fit */
    "tags" : ["province", "fix"],         /* Tags defines in what categories your mod will be listed under locally. To prevent tag spamming, a maximum of 5 are allowed.
                                             Please note that this does not guarantee that any mods backend list the mod correctly (make sure to specify tags during upload) */
    "relationships" : [                   /* Descriptions on how your mod relates to other mods. Naturally, an empty list means "no relationships" */
        {
            "rel_type" : "dependency",    /* The type of relationship that this item describes. Supported types are "dependency", "incompatible_with", 
                                             "load_before", "load_after" - The latter three are being tested in launcher version 2023.10-rc */
            "id" : "com.github.othermod", /* The "id" of the mod the relationship concerns. This does not relate to a mod's workshop ID/number string. */
            "display_name" : "Othermod",  /* Display name of the other mod if that mod is *not* present on disk - If you have it installed, we'll use 
                                             the "name" from its own descriptor file */
            "resource_type" : "mod",      /* What type of item you depend on. Currently we only support "mod", but "dlc" is being considered as well */
            "version" : "1.2.*"           /* If this version of your mod depends on a certain version of the other mod, you can put it here. If you don't 
                                             care, just use "*". Same globbing as for "supported_game_version" */
        }
    ],                 
    "game_custom_data" : {                /* Victoria 3-specific information that the game engine needs to know */
      "multiplayer_synchronized" : true   /*  */
    }
  }
```

.metadata 文件夹中还可以包含一个 *thumbnail.png* 文件，用作启动器中的缩略图。

## mod 文件夹结构

每个具体的 mod 文件夹对应于《维多利亚3》本体的 game 文件夹。因此，该文件夹内部必须保持相应的结构，mod 才能正常运作。例如，从 mod 文件夹出发，修改决议（decision）的结构应为：

- mod/[mod-name-folder]/common/decisions/[mod decision files]
- 常见错误是增加或减少了一级目录，以下写法都无法生效，因为游戏无法正确读取这些文件：
  - mod/[mod-name-folder]/game/common/decisions/[mod decision files]
  - mod/[mod-name-folder]/common/[mod decision files]
  - mod/[mod-name-folder]/decisions/[mod decision files]

还要注意拼写错误。拼写错误的文件夹无法被正确读取。另外请注意，大多数文件夹在英语语法允许时都使用复数形式；主要的例外是 common/technology。

某些文件夹，即 common/history 和 events，可以包含任意数量的子文件夹，且子文件夹可以随意命名。这主要用于整理组织，把相关的文件放在一起。

### 额外文件

游戏引擎通常会加载整个文件夹，而不是特定名称的文件。因此对于大多数 mod 来说，最好把内容定义在[加载顺序在本体之后](https://vic3.paradoxwikis.com/Mod_files_load_order)的文件中。例如，在 common/buildings 文件夹中新建一个名为 `my_modded_buildings.txt` 的文件，其加载效果与使用和本体游戏文件相同名称的文件完全一样。

### 文件命名

Mod 文件应使用较为独特的名称。一种常见做法是使用 mod 的“前缀”，例如 mod 名称的缩写或首字母缩略词。大多数游戏文件并不要求特定名称，命名只是为了清晰易懂。需要特定名称的文件应在本 wiki 相关条目中注明。

还要注意，文件名对于[加载顺序](https://vic3.paradoxwikis.com/Load_order)非常重要，当两个或更多 mod 修改同一游戏元素时，加载顺序决定了使用哪个 mod 文件。

## mod 文件夹模板

《维多利亚3》Mod 制作合作社的[这个仓库](https://github.com/Victoria-3-Modding-Co-op/Mod-Template)提供了基本的 mod 文件夹配置，以及从零开始进行 mod 开发的其他实用资源。

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

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • Mod 结构 • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|