---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Graphical asset modding
source: https://vic3.paradoxwikis.com/Graphical_asset_modding
pageid: 7461
categories: [Potentially_outdated, Unknown_version, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的部分。其中至少有一些最后一次验证时使用的版本是 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) unknown。

## 2-D 资源

《维多利亚3》主要使用 *DirectDraw Surface*（.dds）文件格式来存储纹理资源。这些纹理会由 UI 按需缩放。虽然游戏可以接受任意分辨率，但压缩纹理的分辨率必须能被 4 整除，否则 UI 会出现错误的缩放表现，并向日志输出一条错误信息。

### 通过 Paint.NET 导出图像

Paint.NET 是一款灵活且适合新手的 .dds 编辑工具，可在 https://www.getpaint.net/ 获取。

#### 保存压缩图像：

在保存配置中：

1. 选择 **BC7 (sRGB, DX 11+)**
2. 勾选 "**Generate Mip Maps**"
  1. 此复选框下方的下拉菜单决定了用于计算图像缩放后外观的插值算法。默认值应为 **Bicubic**，这在几乎所有情况下都完全可用。除非你清楚自己在做什么，否则不应更改此项。选择一个好的选项并避开其他差的选项非常重要，因为这决定了图像缩小后的外观，例如[意识形态](Ideology.md)图标就经常会被缩小。选了差的选项往往会导致你的纹理在某些 UI 面板中很难看，比如使用 Nearest Neighbor（最近邻）时会出现非常像素化或“颗粒感”的外观。

*记住要让你的分辨率能被 4 整除！*

Paint.NET .dds 导出的推荐导出选项

#### 保存未压缩图像：

在保存配置中：

1. 选择 **B8G8R8A8 (Linear, A8R8G8B8)**
2. 勾选 "**Generate Mip Maps"**
  1. 关于插值算法下拉菜单的说明，请参见上文压缩图像说明中的内容。默认值是 **Bicubic**，除非你清楚自己在做什么，否则应使用该设置以确保纹理外观良好。

### 通过 GIMP 导出图像

GIMP 是一款在功能与范围上与 Photoshop 类似的强大工具，可在 https://www.gimp.org/ 获取。

在导出设置中：

1. 将压缩方式设为 **BC3 / DXT5**
2. 为除事件图片以外的所有内容**生成 mipmap（Generate mipmaps）**
3. 建议在生成 mipmap 时使用 **Kaiser** 滤镜，因为默认设置的效果可能更差

GIMP .dds 导出的推荐导出选项

## 3-D 资源

*WIP*

## 参考

Modding
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

| 图形 | [3D Models](Model modding.md) • [Event images](Event images.md) • Graphical Assets • Fonts • [Flags](Flag modding.md) |
|---|---|

| 音频 | Music • [Sound](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|