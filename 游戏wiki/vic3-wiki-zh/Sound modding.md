---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Sound modding
source: https://vic3.paradoxwikis.com/Sound_modding
pageid: 7379
categories: [Potentially_outdated, 1.8, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。其中至少部分内容最后一次验证时的版本是 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.8。

注意：
本文假设你已经知道如何使用 FMOD。如果你需要帮助，FMOD 在其 Youtube 页面上提供了若干教程。
音频 mod 制作需要使用 FMOD Studio，可在此处获取：[FMOD](https://www.fmod.com/)

*请下载 2.02.03 版本*。*这是开发团队推荐的版本，并且已被 mod 作者确认可用。*

FMOD Studio 允许 mod 作者为事件添加并混合声音，这些事件可以通过脚本在事件、UI 元素等中被调用。

## 使用模板开始项目

下载这个 [FMOD 项目模板](https://github.com/Victoria-3-Modding-Co-op/Vic3-FMOD-Template) 并按照那里的说明操作。所有原版的 **Groups** 和 **VCAs** 都已经为你定义好了。否则，请按照下一节的说明从零开始创建项目。

如果使用模板，**请务必删除随附的 MASTER BANK！！！** *使用随附的 master bank 会破坏其他同样没有删除该 bank 的 mod。*

删除
随附的 bank，然后右键单击并选择
New Bank
来创建你自己的 bank。
为你的 master bank 取一个独特的名字，以避免与其他 mod 冲突。请确保你的 master bank 的名字在 `VFX` 之后。*尝试在任何原版音效 bank 之前加载 .bank 文件可能会破坏原版声音功能。*

如果你使用了位于 `MUSIC` 或 `SFX` 内的任何原版 group，你将需要按照下述说明匹配 GUID。

## 从零开始创建项目

1. 打开 FMOD 并创建一个新项目。
2. 创建一个新 bank，然后右键单击它并将其标记为 master bank。
  1. 如果你的项目将包含许多不同的事件（音轨），你可以同时使用多个 master bank 来组织它们。
3. 为你的 master bank 取一个在 `VFX` 之后的名字。
  1. *尝试在任何原版音效 bank 之前加载文件可能会破坏原版声音功能。*
  2. FMOD Studio 内 bank 的名字并*不需要*在 `VFX` 之后，但 FMOD Studio 生成 bank 文件时会以 FMOD Studio 内对应 bank 的名字命名文件，因此出于便利考虑建议这样做。
4. 创建你打算使用的任何 **Groups** 和 **VCAs**。
5. 保存项目，点击 **Build**，然后点击 **Export GUIs**。
6. 进入《维多利亚3》的安装目录，找到 `game\sound\GUIDs.txt`，获取 `bus:/` 的 ID。它会是一长串数字。
7. 进入你的 FMOD 项目的 `\build` 文件夹，找到 `GUIDs.txt`，获取该项目的 `bus:/` ID。
8. *关闭 FMOD*
9. 在你的 FMOD 项目的 `Metadata` 文件夹中，在所有文件里搜索并将你的项目的 `bus:/` ID 全部替换为《维多利亚3》的 ID。
10. 对你使用的每一个与原版匹配的 Group 或 VCA 重复此过程，例如：`bus:/MUSIC` `bus:/MUSIC/Mood``vca:/MUSIC`
11. *保存你的更改，然后关闭所有文件。*
12. 在 FMOD 中重新打开项目，进行你的音效/音乐工作。
13. 完成后点击 **Build**。
14. 在你项目的 `\build` 文件夹中找到相关文件，并将它们复制到你 mod 的 `\sound\banks` 文件夹。*注意拼写！是单数的*`sound`*和复数的*`banks`。

## 导入声音

1. 切换到 Assets 标签页，将你的音频文件拖放到那里。*FMOD 接受 wav、mp3、ogg、aiff、wma 和 flac 格式。*
2. 右键单击一个已导入的资产并选择 **Create Event**。
3. 选择一个事件类型。任何事件类型都可以。*如果不确定，就使用 2D Timeline。你也可以选择多个文件并一次性为它们全部创建事件。*右键单击你的资产并选择 Create Event
4. 切换到 Events 标签页并选择你的新事件。
5. 右键单击你的事件并选择 Assign to Bank > Browse > Master。对任何其他事件执行同样的操作。右键单击你的事件并选择 Assign to Bank
6. 进入 Window > Mixer Routing > VCA。*如果使用模板，这些已经为你定义好了。否则，创建你需要的并按照上一节的说明操作。*
7. 将你的事件分配到相应的 groups 和 VCAs。
8. 完成后，选择 File > Build。这将创建游戏将要使用的 bank 文件。
9. 在你项目的 `\build` 文件夹中找到相关文件，并将它们复制到你 mod 的 `\sound\banks` 文件夹。*注意拼写！是单数的*`sound`*和复数的*`banks`。

*提示：你可以让 FMOD 将 bank 导出到你的 mod 文件夹。方法如下：*

1. 进入 Edit > Preferences，Build 标签页。
2. 将你的 mod 的 sound 文件夹路径粘贴到“Build banks output directory”。
3. 在下方选择 Desktop 平台，并将其“Output sub-directory”设置为 banks。

### 故障排除：

- 如果错误日志显示无法加载某个 bank，你可能是没有正确替换 ID，或者在编辑 ID 后没有重新构建项目。
- 如果找不到特定事件，请仔细检查路径、名称，以及它在 FMOD 中是否已分配到某个 bank。

## 在游戏中播放声音

音效可以通过脚本、UI 元素或地图上的模型播放。

**控制台：**

使用命令 `audio.play_event event:/myevent`

- 注意，控制台无法播放名称中含空格的事件。这对脚本和 UI 来说不是问题。
- 如果你在 FMOD 中将事件放进了文件夹，那么此路径应包含文件夹名称，例如：`event:/somefolder/myevent`
- 你不需要在这里引用 bank 的名称。

**UI 按钮：**

- `clicksound = "event:/myevent"`

- `oversound = "event:/myevent"` - 这会在光标悬停在按钮上时播放

**UI 动画状态：**

```
 state = {
   name = "my_sound"
   start_sound = { soundeffect = "event:/myevent" }
   end_sound = { soundeffect = "event:/myevent" }
   soundparam = { name = parameterName value = 1 }
 }
```

- `start_sound` 会立即触发音效。
- `end_sound` 会在动画结束时播放（如果动画有持续时间）。
- `soundparam` 是可选的，用于通过在 FMOD 中设置的参数来修改事件。*参见下文的 Sound Parameters。*
- 请记住，状态不会自行触发。
- 你也可以使用一个 scripted gui，在脚本中播放声音，并通过按钮的 `onclick` 或状态的 `on_finish` 来触发。

**3D 模型：**

建筑（common/buildings）：

```
 asset = {
   ...
   soundeffect = { soundeffect = "event:/eventName" soundparameter = { "parameterName" = 0 } }
 }
```

单位（gfx/models/units/infantry）：

```
 state = { 
   ...
   event = {
     time = 0.0
     soundparameter = { "parameterName" = 0.0 }
     sound = { soundeffect = "event:/eventName" }
   }
 }
```

## 参考

Mod 制作
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [变量](Variable.md) |
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

| 音频 | Music • Sound |
|---|---|

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • [Scripted tests](Scripted test.md) • [Troubleshooting](Troubleshooting.md) |
|---|---|

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|