---
translated: 2026-10-27
translator: machine (glm-5.3)
title: PDX Flag Builder
source: https://vic3.paradoxwikis.com/PDX_Flag_Builder
pageid: 9974
categories: [Modding_tools, Modding]
fetched: 2026-10-27
---
Mod 模组工具
： PDX Flag Builder
PDX Flag Builder
类型
旗帜制作器
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

下载
链接
PDX Flag Builder
类型
旗帜制作器
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

下载
链接
**pdx-flag-builder** 是一款为《维多利亚3》和《欧陆风云5》制作旗帜的工具。

示例截图

## 用法

### 安装

从 [发布页面](https://github.com/kaiser-chris/pdx-flag-builder/releases) 下载适用于你系统的 zip 压缩包，解压到任意位置后运行 `pdx-flag-builder`。

在 Linux 上，该工具需要带有 glibc 2.38 或更新版本的分发版，例如 Ubuntu 24.04、Debian 13 或 Fedora 39，并且其文件对话框需要 `zenity` 或 `kdialog`，大多数桌面环境已自带其中之一。

### 初始设置

该工具会从游戏和你的 mod 中读取旗帜与纹理：

1. 打开 **Settings**（设置）（`Ctrl+,`）。
2. 点击 **Add Folder**，然后点击 **Browse...**，选择游戏的 `game` 文件夹或某个 mod 的根文件夹。
3. 可以随意添加任意多个文件夹。列表中靠下的文件夹会覆盖其上方的文件夹，就像 mod 覆盖游戏一样。
4. 点击 **Save**。

### 查找旗帜

**Databases → Flag Database**（数据库 → 旗帜数据库）会列出找到的每一个纹章，并附带预览。**Databases → Texture Database**（数据库 → 纹理数据库）会列出图案和纹样。在搜索框中输入即可缩小列表范围，点击列标题可以进行排序。

点击某个旗帜即可打开它。**File → New Flag**（文件 → 新建旗帜）则从一个空白旗帜开始。

### 编辑

**Layers**（图层）面板会列出纹章及其各个图层。点击其中一个，即可在 **Selected Layer**（所选图层）面板中进行编辑：

- 纹章拥有名称、图案和颜色。
- 纹样（emblem）拥有纹理、颜色、一个将其限制为图案中单一颜色的蒙版，以及它的放置属性：位置、缩放和旋转。
- 子旗帜（sub flag）会绘制另一个纹章，可设置偏移和缩放。

通过 **Add Layer**（添加图层）添加图层，也可以直接从纹理数据库通过 **Add as Layer**（作为图层添加）和 **Set as Pattern**（设为图案）添加，或从旗帜数据库通过 **Add as Sub Flag**（作为子旗帜添加）添加。图层旁边的箭头可以上下移动图层；列表中靠下的图层会绘制在上层。

数字字段可以通过在其上拖动来修改。双击则可直接输入数字。拖动时按住 **Shift** 可加大步长，按住 **Alt** 可减小步长。

要用键盘移动放置项，先点击旗帜再使用方向键：

| 按键 | 效果 |
|---|---|
| 方向键 | 移动所选放置项 |
| **Ctrl** + 方向键 | 缩放 |
| **Alt** + 左右键 | 旋转 |
| **Shift** + 以上任意按键 | 步长增大十倍 |

**Ctrl+Z** 撤销，**Ctrl+Y** 重做。

### 保存与导出

| 菜单项 | 效果 |
|---|---|
| **File → Save**（`Ctrl+S`） | 将旗帜写回其来源文件。只更改它自身的定义；文件其余部分保持原样。 |
| **File → Save To File...**（`Ctrl+Shift+S`） | 将旗帜放入你选择的文件中，替换其中同名的旗帜或添加到文件末尾。 |
| **File → Copy Script** | 将旗帜的脚本复制到剪贴板。 |
| **File → Export Image...** | 将旗帜保存为 768 × 512 的 PNG 图片。 |

文件中使用 `@variables` 或 `@[expressions]` 写入的值会按其计算出的数字保存。

工具在丢弃未保存的更改之前会先询问。

### 设置

**Settings → Interface Scale**（设置 → 界面缩放）可以在高分辨率显示器上放大整个界面。**View → Reset Layout**（视图 → 重置布局）可将各面板恢复到初始位置。

设置存储在 Windows 的 `%AppData%\pdx-flag-builder` 和 Linux 的 `~/.config/pdx-flag-builder` 中。

Mod 模组制作
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