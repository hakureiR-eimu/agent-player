---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Model modding
source: https://vic3.paradoxwikis.com/Model_modding
pageid: 3692
categories: [Potentially_outdated, Unknown_version, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。至少其中部分内容最后验证于 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) unknown。

## 简介

以下指南将说明如何编辑游戏中的模型或创建新模型。

### 工具：

- 一款能以 .mesh 格式编辑和导出的工具，例如 Ross G. 制作的 IO PDX Tools。
- 一款 3D 建模软件，例如 Blender。
- 一款文本编辑器，例如 Notepad++ 或 Visual Studio Code，用于编辑 .asset 文件。

## 编辑模型

### 找到要编辑的模型

首先要找到要编辑的模型。为此，请找到《维多利亚3》的安装文件夹（不是 mod 文件夹，而是《维多利亚3》本体文件所在的文件夹）。在该文件夹中有一个"gfx"文件夹，其内部还有一个名为"models"的文件夹。游戏中所有的 3D 模型都在这个文件夹里。在该文件夹中搜索要编辑的模型。本示例中使用的模型是欧洲风格的城市中心，位于 "gfx/models/buildings/european/city_urban_center_01"。

在该文件夹中有以下文件：

- *.asset* 文件。该文件不包含网格（mesh）数据，但包含游戏识别和使用网格数据的方式。它是 .mesh 文件与游戏内渲染之间的桥梁。
- *.mesh* 文件。这是 3D 模型所在的文件，也就是需要编辑的文件。
- *.dds* 文件。这些是模型的贴图。

要开始制作 mod，必须复制相同的文件夹结构，并复制需要编辑的文件。在本示例中，复制的文件夹是 "gfx/models/buildings/european/city_urban_center_01" 及其内容。

### 编辑 3D 建筑模型

要编辑 3D 模型，需要一款具备导入 Paradox *.mesh* 文件功能的 3D 建模软件（其他游戏可能也使用 *.mesh*，但它们并不是同一类文件，因为这取决于所使用的游戏引擎）。本示例将使用 Blender 以及免费使用的 PDX Blender Tools。

在 Blender 中，打开 mod 文件夹中的 *.mesh* 文件（**不要打开游戏文件夹中的**，不要直接编辑游戏资源文件，否则可能导致只有重新下载游戏才能修复的问题）。本例中，在 Blender 中通过该工具打开的 *.mesh* 是 "european_city_urban_center_01.mesh"。

该 .mesh 文件包含以下对象：

- LOD_0_decal_decal
- LOD_0_mesh_mesh
- LOD_0_worlddecal_worlddecal
- LOD_1_decal_decal
- LOD_1_mesh_mesh
- LOD_1_worlddecal_worlddecal
- LOD_2_decal_decal
- LOD_2_mesh_mesh
- LOD_2_worlddecal_worlddecal
- LOD_3_decal_decal
- LOD_3_mesh_mesh
- LOD_3_worlddecal_worlddecal

该文件包含 3 个模型：一个 decal、一个 mesh 和一个 worlddecal，它们各被复制了 4 次（每个 LOD_X 各一份）。这是出于优化目的：每个 LOD 具有不同的细节层级（**L**evel **O**f **D**etail），游戏引擎会根据镜头与模型的距离来决定使用哪个 LOD。如果镜头非常近，模型会显示高精度对象（LOD_0 对象）；如果镜头非常远，模型会显示低精度对象（LOD_3 对象）；其余 LOD 则用于介于极近与极远之间的情况。此外，所使用的 LOD 还取决于玩家设置的画质。这意味着同一个物体需要建模 4 次，但实际上只要主要的 LOD 完成后，制作其余 LOD 并不难（稍后会说明）。编辑时，应专注于 LOD_0。

共有 3 种对象：

- *decal_decal*。这是一个不应被修改的平面。该平面在建筑下方渲染一张贴图，使建筑可以拥有自定义的地面纹理。就城市中心而言，它是一个带有若干小径的鹅卵石广场。
- *mesh_mesh*。这是 3D 模型本体，可以被修改或从头重做。
- *wolddecal_worlddecal*。这是供游戏引擎使用的 decal，不应被编辑。该 decal 渲染的是城市地面的纹理（不是建筑本身，而是整座城市。在本例中，它渲染的是所有欧洲文化城市建筑共用的鹅卵石街道。该 decal 还显示了建筑在网格中的尺寸（城市是通过在方形网格上生成模型来创建的，模型不应大于 world decal 的尺寸）。

对于基础编辑，唯一需要编辑的对象是 LOD_0_mesh_mesh；对于进阶编辑，可能需要缩放 decal_decal 以适配编辑后的 mesh_mesh；对于非常高级的（涉及代码的）编辑，则可以编辑 wolrddecal_worlddecal。

TODO

## 注意事项

- `.asset` 文件必须使用 LF（Unix 风格）换行符编码，使用 CRLF（Windows 风格）换行符会破坏其功能。

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

| 图像 | 3D Models • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|

| 音频 | Music • [Sound](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|