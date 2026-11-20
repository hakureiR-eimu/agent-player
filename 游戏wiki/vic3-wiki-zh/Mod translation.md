---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Mod translation
source: https://vic3.paradoxwikis.com/Mod_translation
pageid: 7408
categories: [Timeless, Modding]
fetched: 2026-10-27
---
本文为[长期有效](https://vic3.paradoxwikis.com/Category:Timeless)文章，适用于游戏的任何版本。

## 使用 ParaTranz 翻译 mod

[ParaTranz](https://paratranz.cn/projects?game=vic3) 是一个将 PDX mod 翻译成不同语言的平台。它有许多非常实用的功能：

- 提供与其他 mod 部分匹配的翻译
- 导出时更新语言标签（`l_[language]` 后缀等）
- 在导入新版本的 localization 文件时，在文件和本地化键（localization key）级别进行校验和比对
- 以及更多其他功能

### 现有项目

许多大型 mod 已有现成的翻译项目。我联系了一个为我的 mod 提供中文翻译的现有项目，如今已正式将他们的翻译纳入我的 mod，并在更新前向他们提供最新的 loc 文件。

### 链接

- https://paratranz.cn/projects?game=vic3

### 设置指南

首先创建一个项目，操作非常直观。

进入“文件”页面并点击“Manage Files"。

点击“Add Files"。

勾选“update”复选框（以备将来使用），然后将整个英文 localization 文件夹拖放到指定区域。

如果你已有翻译内容，也可以一并导入。该工具会进行校验和检查，只更新发生变化的本地化键。

之后进行翻译时，转到文件页面（不是管理文件的页面），点击某个 loc 文件。

然后你会进入翻译视图。如你所见，它能识别 PDX 格式，甚至在翻译中缺少格式或概念标签时警告译者。此外，它还支持连接多种机器翻译服务，如 DeepL、Google Translate、Deepseek 等。

我还建议在导出设置中启用“replace yml”选项

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

| 指南 | Mod 翻译 • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|