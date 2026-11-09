---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Modding
source: https://vic3.paradoxwikis.com/Modding
pageid: 131
categories: [Timeless, Modding]
fetched: 2026-10-27
---
本文是一篇[不受版本时间限制](https://vic3.paradoxwikis.com/Category:Timeless)的文章，适用于游戏的任何版本。

本页讨论制作 mod 的基础知识。关于使用游戏 mod 的信息，请参见
Mod
**Mod 制作**（Modding，使用 'mod'，即 modification 的简称）在《维多利亚3》中让玩家能够修改游戏的各个方面或加入新功能，从而提升整体游戏体验。虽然某些元素是硬编码、无法修改的，例如迁移或战斗伤亡逻辑、地图模式，但仍有大量可自定义的选项。

mod 并不会在《维多利亚3》中禁用成就，因为游戏对这方面另有单独的规则。

## 入门

### 建立 mod 文件夹

主条目：
Mod structure
- 在 `Documents\Paradox Interactive\Victoria 3\mod` 中新建一个文件夹，这个新文件夹与原版游戏中的 `game` 文件夹相对应。
  - 不要直接修改游戏文件，它们会在任何游戏更新时被覆盖。
- 在新文件夹中，按需创建你 mod 的 "*common*"、"*localization*" 等文件夹。
  - 遵循与 *Victoria 3\game* 文件夹中相同的结构。
- 将实际内容的 .txt 和其他文件放入相应的文件夹中。
- 添加一个 `.metadata` 文件夹，其中包含一个 *metadata.json* 文件。该文件可以非常简陋，但它是游戏加载你的 mod 的必要条件。
- 在启动器中通过播放集中的"Add more mods"手动添加你的 mod 文件夹。

或者，使用 [GitHub 上的 Victoria 3 Mod Template](https://github.com/Victoria-3-Modding-Co-op/Mod-Template) 来建立基本结构。

### 基本工具与资源

**文件编辑器**

- 使用具备语法高亮和其他实用功能（例如代码搜索）的源代码编辑器。制作《维多利亚3》 mod 的常用免费软件包括：
  - [Sublime Text](https://www.sublimetext.com/) 拥有支持最好的插件：[Victoria 3 Tools](https://github.com/dementive/Victoria3Tools)
  - [Visual Studio Code](https://code.visualstudio.com/) 有 Paradox Highlight 扩展和 [CwTools](https://marketplace.visualstudio.com/items?itemName=tboby.cwtools-vscode)（支持自动补全、错误检查、工具提示等功能）可用。
  - [IntelliJ](https://www.jetbrains.com/idea/download/other.html)（社区版免费）有 [Paradox Language Support](https://plugins.jetbrains.com/plugin/16825-paradox-language-support) 扩展可用。
  - [Notepad++](https://notepad-plus-plus.org/) 是功能较弱的选择，但可能不那么令人眼花缭乱。
    - 由于没有专门针对《维多利亚3》的插件，可选择 *Perl* 作为语言语法以获得一些语法高亮。

**Debug mode**

- 使用 debug mode（调试模式）以访问游戏中隐藏的开发者信息和工具。
- 可以在启动器中以调试模式启动：在左侧边栏进入"Game settings"并滚动到最底部。
- 或者，在 Steam 中添加以下启动选项：在游戏库中右键点击 Victoria 3，在弹出菜单中选择“属性”，然后在“常规”选项卡底部添加 `-debug_mode`
  - 这样从主播放按钮启动时即为调试模式。
- 调试模式还会让游戏热加载（hotload）大多数游戏文件，让你无需重启游戏即可更快测试改动。
  - 少数文件夹/文件不在此列，例如 on_actions；其他一些可能需要返回主菜单并开始新的会话。
- 另外，也有一些 mod 允许在游戏内激活和关闭调试模式，不过它们不具备文件热加载功能。

**文档**

- 在游戏控制台中使用 **script_docs** 和 **DumpDataTypes** 命令，生成包含事件 effect（游戏内效果脚本）、trigger（条件判断脚本）和 scope（作用域）的其他日志。
  - 在 debug_mode 激活时，在游戏内用 `^` 打开控制台。
  - 生成的文件位于 `Documents\Paradox Interactive\Victoria 3\docs`
  - 这是你能获得的最可靠的技术文档。
- 大部分文档也可在本 wiki 上找到：主要示例见 [Effect](Effect.md)、[Trigger](Trigger.md)、[Event target](Event target.md) 和 [Data types](https://vic3.paradoxwikis.com/Data_types)，更多文档页面请参见本页底部的导航框。
- [Modding Git Guide](https://docs.google.com/document/d/1bQdOVMY6FTu-2AKXZblYp6bF2-_W2JMUtXc5a0nZ8Ls) 是一份由社区编写的指南，介绍如何使用 Git、GitHub/GitLab 以及 KDiff3 等相关工具。对于本 wiki 之外的问题，它可能是一个有用的去处，并且包含这里讨论的许多内容的分步指南。虽然示例基于 HOI4，但其原则同样适用于任何 Paradox 游戏 mod。

### 最佳实践

- 使用规范的、带制表符的缩进，确保开括号和闭括号处于同一层级。这便于代码折叠、更容易发现错误，并提高可读性。
  - 考虑为你的编辑器使用自动格式化扩展。
- 对实现方式不确定时，用编辑器在原版游戏代码中搜索相关关键词。
- 使用注释（总是以 `#` 开头）来为你的脚本写文档、便于导航，或在不删除的情况下禁用部分代码。
- 避免覆盖你不想修改的条目，以尽量减少冲突并提高清晰度。

### mod 文件的优先级

主条目：
Mod compatibility
- 使用与原版相同的文件名会完全覆盖原始文件。
  - 如果不同 mod 使用了多个同名文件，以启动器中 mod 列表位置最靠后的为准。
- 如果一个条目被多个 mod 中不同文件名的文件修改，游戏会按文件名以 ASCII 顺序对相关文件排序。
  - 这优先于启动器中 mod 列表里的位置。

### 调试

- 阅读 error.log 以查找游戏在 `Documents/Paradox Interactive/Victoria 3/logs` 中识别出的异常和警告。
- 调试模式会添加一个按钮，为你打开 `error.log`，并显示自上次打开以来的当前错误数。
  - Windows 下默认使用的编辑器是记事本，但可以配置。
  - 你可以直接编辑 Documents/Paradox Interactive/Victoria 3/pdx_settings.json，在 `System` 键下添加以下键：
    - `"editor": "C:\\Program Files\\Sublime Text\\sublime_text.exe"` - 告诉游戏使用哪个编辑器，你可以使用电脑上任何有效的编辑器，只需确保路径正确。
    - `"editor_postfix": ":$:1"` - 打开编辑器时会用到，例如这个 Sublime Text 特定的后缀可确保编辑器打开时滚动到最后一行。
  - 或者，你可以使用游戏内控制台中“设置”按钮提供的游戏内设置编辑器。在类别选择器中选择 System，找到 `Editor` 键。

- 备份你的工作，可能出现意外，拥有备份总是好的。
  - 使用 [Git](https://git-scm.com/) 等版本控制系统可以跟踪你的更改、回退到可用版本并进行协作。
  - 如果你是团队的一员，考虑使用 GitHub 进行团队协作。如果你是 Git 新手，[Github Desktop](https://desktop.github.com/) 这类程序非常适合初学者。

- 在编辑器中将代码文件的*编码*设置为 `UTF-8 with BOM`，尤其是 localization .yml 文件。
- 对于 localization 文件，确保文件名以 l_*language* 结尾，例如 `foo_l_english.yml`。注意后缀的第一个字符是小写字母 L，而不是数字 1 或大写字母 i。
- 加入[官方 discord](https://discord.com/invite/victoriagamePDX) 和 [modding discord](https://discord.gg/XJbqFbHdsM) 向其他 mod 作者寻求帮助。

## 工具与实用程序

有许多第三方工具可以辅助 mod 制作，涵盖文本编辑、图像编辑等多个方面。

| 名称 | 类别 | 链接 | 描述 |
|---|---|---|---|
| Paradox Highlight | 编辑器（VS Code） | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=dragon-archer.paradox-highlight) | 为所有《维多利亚3》文件提供最新的语法高亮。也支持十字军之王 III 等其他 Paradox 游戏。 |
| CWTools - Paradox Language Services | 编辑器（VS Code） | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=tboby.cwtools-vscode) | 用于在 Visual Studio Code 中编辑 Paradox 游戏文件。具备语法高亮、错误检查、自动补全等功能。基于 [Cwtools library](https://github.com/cwtools/cwtools)，用于解析、编辑和验证 Paradox Interactive 脚本文件。 |
| Victoria 3 Tools | 编辑器（Sublime Text） | [GitHub](https://github.com/dementive/Victoria3Tools) | Sublime Text 4 的《维多利亚3》语法支持 |
| Paradox Language Support | 编辑器（IntelliJ） | [JETBRAINS Marketplace](https://plugins.jetbrains.com/plugin/16825-paradox-language-support) | 用于 Paradox Interactive 游戏 mod 制作的 Intellij IDEA 插件。具备语法高亮、错误检查、自动补全等功能。 |
| Victoria 3 Modding Support | 编辑器（IntelliJ） | [JETBRAINS Marketplace](https://plugins.jetbrains.com/plugin/25284-victoria-3-modding-support) | 为《维多利亚3》的 definition 和 mod 文件添加支持。具备语法高亮。 |
| Tiger Mod Validator | 通用 | [GitHub](https://github.com/amtep/tiger) | Tiger 专抓 bug。检查十字军之王 3、维多利亚 3 或 Imperator: Rome 的用户 mod 文件中的错误并给出警告。例如：缺失的 localization，或对 character 使用信仰 trigger。 |
| Tiger Mod Validator for VSCode | 编辑器（VSCode） | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=unlomtrois.ck3tiger-for-vscode) | 一个将 Tiger 日志集成到“问题”选项卡的 VS Code 扩展，可直接在 IDE 中查看问题。 |
| Tiger Mod Validator Github Action | 通用 | [GitHub](https://github.com/kaiser-chris/tiger-action-public) | 一个基础仓库和指南，介绍如何将 ck3-tiger 设置为 GitHub workflow action。 |
| PDX Flag Builder | 纹章设计器 | [GitHub](https://github.com/kaiser-chris/pdx-flag-builder), [Microsoft Store](https://apps.microsoft.com/detail/9P4KDSQ0RMDG?hl=en-us&gl=US&ocid=pdpshare) | 一个为《维多利亚3》和欧陆风云 5 制作旗帜的工具。 |
| Pdx-Unlimiter | 通用 | [GitHub](https://github.com/crschnick/pdx_unlimiter) | 一个强大而智能的存档管理器；可以编辑存档文件，并可在不启动游戏的情况下预览 mod 旗帜。 |
| Map data editor | 通用 | [GitHub](https://github.com/Linnest2020/Vic3-mapdata-editor) | 一个地图数据编辑器，可以可视化地编辑 common/history/states 中的地图数据，有助于编辑哪些省份属于哪些国家。 |
| Vicky-Mapgen | 通用 | [GitHub](https://github.com/Chease23/Vicky-Mapgen) | 一个根据 heightmap.png 和 boundaries.png 生成省份的地图生成器 |
| Music Mod Creation Tool | 通用 | [GitHub](https://github.com/runite-drill/music-mod-creation-tool) | 顾名思义，用于音乐 mod，现已支持 Vic 3 |
| UWPDumper | 通用 | [GitHub](https://github.com/Wunkolo/UWPDumper) | 一个从 Microsoft Store 游戏中提取文件的工具。 |
| Clausewitz Maya Exporter | 通用 | [Paradox Forums](https://forum.paradoxplaza.com/forum) | 一个用于创建并导出 3D 模型的工具，可在 vic3 和其他 Clausewitz 引擎游戏中使用。 |
| Jomini.js | 通用 | [GitHub](https://github.com/nickbabcock/jomini) | 一个基于 webassembly 的强大 JavaScript 解析库，有一个名为 [Rakaly](https://github.com/rakaly/librakaly) 的 C 版本。 |
| Victoria 3 Mod Template | 通用 | [GitHub](https://github.com/Victoria-3-Modding-Co-op/Mod-Template) | 一个为《维多利亚3》 mod 建立 GitHub 仓库的模板。 |

## 常见问题

主条目：
Troubleshooting
- **部分本地 mod 文件加载失败。**
  - **症状：**
    - mod 在启动器中正确显示，也添加到了播放集，但部分文件没有生效。
    - `error.log` 中包含诸如 `[virtualfilesystem.cpp:562]: Could not create lexer from file due to 'fopen() failed: 2'` 的一行，后跟一行关于编码的信息。
    - 在使用 `-debug_mode` 标志启动的游戏中，点击错误小鹿打开 `error.log` 时也可能出现问题。
  - **可能原因：**
    - 权限问题。由于权限损坏，游戏可能无法访问 mod 文件。
    - 文件路径包含非 ASCII 字符。《维多利亚3》对此有问题（与[钢铁雄心 IV](http://hoi4.paradoxwikis.com/Modding#Common_mistakes) 等其他游戏类似）。在 Windows 中，这可能是由于用户名——因而包含 Documents/Paradox Interactive/Victoria 3/ 的用户文件夹——包含非 ASCII 字符导致的。查看你的文件路径即可轻松确认是否属于这种情况。
  - **解决方案：**
    - 你可以通过编辑 Steam/steamapps/common/Victoria 3/launcher/launcher-settings.json 中的 `"gameDataPath": "%USER_DOCUMENTS%/Paradox Interactive/Victoria 3",` 一行来更改本地 mod 的位置。
    - 例如，如果将该行改为 `"gameDataPath": "C:/Paradox Interactive/Victoria 3",`，那么本地 mod 文件夹将位于 C:/Paradox Interactive/Victoria 3/mod，而不是默认位置。

## 术语

《维多利亚3》 mod 制作有许多源自或类似于通用编程的术语。以下是不完整的常用术语列表。

**Script（脚本）**
  - 这是 mod 作者可以用来改变游戏运作方式的“代码”。
**[Effect](Effect.md)**
  - 以某种方式改变游戏状态的脚本命令
**[Trigger](Trigger.md)**
  - 用于为 effect 设置条件的游戏状态脚本检查
**[Scope](Scope.md)**
  - trigger 或 effect 的上下文
**[Event target](Event target.md)**
  - 指向 scope 或游戏值的关键字
**Type（类型）**
  - 游戏对象的“类”
**Key（键）**
  - 类型的脚本名称
**Tag/TAG**
  - 国家的 key

## 另请参见

[Console commands](Console commands.md)

### 指南

- [Grester's Compendium](https://vic3.paradoxwikis.com/User:Gr3st3r)
- [State modding guide](State modding guide.md)

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

| 图形 | [3D Models](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|

| 音频 | Music • [Sound](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|
| 指南 | [Mod 汉化](Mod translation.md) • [新国家模组制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州模组制作指南](State modding guide.md) |
|---|---|