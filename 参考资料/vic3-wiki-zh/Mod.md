---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Mod
source: https://vic3.paradoxwikis.com/Mod
pageid: 7396
categories: [Timeless, Modding]
fetched: 2026-10-27
---
本文是一篇[不受版本限制](https://vic3.paradoxwikis.com/Category:Timeless)的文章，适用于游戏的任何版本。

关于如何制作 mod 的说明，请参见
modding
**mod**（*modification* 的简称）是对游戏的修改，也是[modding](Modding.md)的目的。修改内容可以从小调整到完全改造不等。

## 安装

可以从多个来源下载并安装 mod：

- 通过 Paradox Launcher 自动安装，或从 [Paradox Mods](https://mods.paradoxplaza.com/games/victoria3) 手动下载
- 通过 Steam 客户端从 [Steam 创意工坊](https://steamcommunity.com/app/529340/workshop/) 自动安装（仅限 Steam 版本）
- 从 [Victoria 3 用户修改子论坛](https://forum.paradoxplaza.com/forum/forums/victoria-3.1095/) 手动下载
- 从 [Nexus Mods](https://www.nexusmods.com/games/victoria3/mods) 手动下载

来自 Steam 创意工坊的 mod 会被放置在 `…\SteamLibrary\SteamApps\workshop\content\529340`，以其创意工坊 ID 命名。来自 Paradox Mods 的 mod 会被放置在 mod 文件夹位置，命名为 `PDX_*MOD_ID*`。

### 找到你的 Victoria 3 mod 目录

通过 Steam 或 Paradox Launcher 运行 Victoria 3 时，mod 安装文件夹为：

| 操作系统 | 路径 |
|---|---|
| Windows | `%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\mod\` |
| Linux | `~/.local/share/Paradox Interactive/Victoria 3/mod/` |
| Mac OS | `~/Documents/Paradox Interactive/Victoria 3/mod/` |

如果 mod 文件夹不存在，请自行创建。

切勿将 mod 安装到游戏安装目录中，否则 mod 将无法被正确加载。[1]

请在 mod 说明中查看该 mod 兼容的 Victoria 3 版本。如有需要，可通过 Steam 的"Steam Beta"选项卡或 Paradox Launcher 的"Game Settings"选项卡回退到旧版[补丁](Patches.md)。

## 手动安装

步骤通常如下（如有具体的 mod 说明，请参照其指示）：

1. **准备**：删除该 mod 已有的安装内容（mod 文件夹和 .mod 文件）。这一步非常重要，因为游戏会加载 mod 文件夹中存在的所有文件，旧版 mod 中已不存在或在新版中被重命名的文件会产生冲突。如果存在 <Victoria 3_settings>\<mod_name>\gfx 文件夹，请删除该文件夹以清除 gfx 缓存。
2. **正确放置 mod 文件**：解压下载的压缩包，使 mod 文件夹中包含该 mod 的 '.mod' 文件和目录。
3. **在启动器中启用 mod**：启动 Stellaris，在"Mod"选项卡中选择该 mod。注意，mod 在启动器中显示的名称可能与 '.mod' 文件的名称不同。
4. **启动游戏**：启用 mod 后，点击"Play"即可在 mod 生效的情况下启动 Stellaris！

如果遇到问题，可以使用启动器的 mod 区域在启动器内创建一个空 mod。创建完成后，前往 mod/ 文件夹查看新生成 mod 的结构，并将其与你正在尝试安装的 mod 的结构进行对比。

更多信息请参见[设置 mod 文件夹](Modding.md)。

## mod 列表

大多数 mod 发布在 Steam 创意工坊：

- [Victoria 3 Steam 创意工坊](https://steamcommunity.com/app/529340/workshop/)

## 拥有 wiki 页面的 mod

Victoria 3 修改内容的 wiki 页面由相应 mod 的开发者负责维护。
- [Victoria 3 转《钢铁雄心IV》转换器](Victoria 3 to Hearts of Iron IV converter.md)

## 另请参见

- [Modding](Modding.md)

## 参考

1. ↑ 即：`…\SteamApps\common\Victoria 3\mod` 或 `~/.local/share/Paradox Launcher/games/Victoria 3/mod`

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

| 图形 | [3D Models](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|

| 音频 | Music • [Sound](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • Mods • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|