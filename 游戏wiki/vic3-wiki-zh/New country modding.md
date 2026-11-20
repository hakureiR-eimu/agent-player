---
translated: 2026-10-27
translator: machine (glm-5.3)
title: New country modding
source: https://vic3.paradoxwikis.com/New_country_modding
pageid: 3181
categories: [Potentially_outdated, 1.8, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。至少有部分内容最后验证于 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.8。

参见：
国家模组制作（Country modding）
本指南介绍如何向游戏中添加一个新国家，使其在 1836 年游戏开始时即已存在。

重要的起始提示：

- 建议使用比普通记事本更好的文本编辑器。我的推荐是 Notepad++（本指南将使用它）、Visual Studio Code 和 Sublime。
- 游戏中所有 .txt 文件必须采用 UTF8-BOM 编码，否则可能无法正常工作。如果不知道如何设置编码，只需复制一个现有文件并修改其内容即可。
- 文本文件中 `#` 之后的所有内容都被"注释掉"，即游戏会忽略 # 之后的内容。
- 本指南是在一个已设置好并能正常运行的 mod 的背景下编写的，请确保你先完成了这一重要步骤。

## 定义国家（Defining the country）

你可以在 /Victoria 3/game/common/country_definitions 中找到国家定义。

所谓"定义"包含两层含义：

- 人类意义上的"决定国家将在哪里、会是什么样子"
- 代码意义上的告诉游戏关于我们国家的信息，使其知道这个国家是什么

所以首先，想好你想要什么国家，尤其是它将位于何处。本指南中的国家将被称为昔兰尼加（Cyrenaica），位于的黎波里塔尼亚的土地上，将拥有整个利比亚沙漠（Libyan Desert）州。

- 新的示例国家将位于这里
- 利比亚沙漠州

现在该决定一个 tag（国家的三字符脚本简称）了。CYR 作为昔兰尼加的 tag 很合理，但任何名称都可以。使用 Notepad++ 的*在文件中查找（Find in Files）*功能检查 CYR 是否已在原版游戏的国家定义文件中出现过，确保 CYR 未被原版游戏使用。如果没有，太好了！否则，换一个别的。现在转到 mod 的国家定义文件夹，为它添加一个定义。

- 确保路径指向 Vic3 的国家定义文件夹，输入你想要的 tag，然后点击 Find All
- 国家定义文件必须位于的路径就是这里国家定义代码

可以看到，国家定义包含一些重要部分。关于国家定义参数的完整列表，参见[国家模组制作 § 国家定义](Country modding.md)。

它以 tag 开头，然后添加颜色（可以是 HSV360、HSV 小数或 RGB255 格式）。使用在线 RGB 取色工具或图像编辑软件找到想要的颜色。

之后，选择国家类型：

- recognized——主要用于"西方"国家
- unrecognized——用于"非西方"国家，类似于维多利亚2的"未开化"
- decentralized——用于没有中央政府体系的国家，通常用于原住民
- colonial——用于作为受承认国家之殖民地或前殖民地的国家

然后是国家的等级（tier），这本质上决定国家的大小，同时也在一定程度上控制它能否成立另一个国家

- city_state
- principality
- grand_principality
- kingdom
- empire
- hegemony

之后，输入主流文化。游戏内拼写通常与代码拼写相同，但并非总是如此。如不确定，请在原版游戏的 /Victoria 3/game/common/cultures 文件夹中核对。

最后，定义默认首都州。与上面一样，这通常与游戏中写的内容相同，只是空格必须始终用下划线代替，这就是为什么 CYR 的首都是 STATE_LIBYAN_DESERT 而不是 Libyan Desert。一个州的形式总是类似于 STATE_(NAME)。如不确定，请在 /Victoria 3/game/map_data/state_regions 或 /Victoria 3/game/common/history/states 中查看。

还要确保有闭合的括号。Notepad++、Visual Studio Code 和 Sublime 等更好的文字处理器都有某种方式来检查这一点。正确的括号配对非常重要！

## 必需的历史文件

历史文件位置：/Victoria 3/game/common/history

需要编辑的历史文件：states、pops、buildings、countries

现在国家已定义，是时候让它出现在游戏中了。目前，游戏只知道 CYR 是一个可能存在的国家，但还没有被告知它应当存在。为此需要 history 文件夹，具体来说是这三个文件夹，以及 countries 文件夹。

- 这三个 history 文件夹是最重要的
- 这是 countries 的历史文件夹

记得在 POPS 历史中把 TRI 改为 CYR
在 BUILDINGS 中也一样
编辑顺序无关紧要，但本指南从 states 开始。此文件夹中的文件告诉游戏游戏开始时谁拥有哪些州（或州中的哪些省份），以及哪些文化将该州视为本土的信息。注意，州历史文件必须使用 `STATES = { }` 块来包含所有州数据。导航到 STATE_LIBYAN_DESERT：

如高亮部分所示，TRI（的黎波里塔尼亚）目前控制着该州。让我们改变它：

- 州历史中所有者为 TRI
- 现在改为 CYR 为所有者

如果现在启动游戏，CYR 控制着该州，但缺少人口和建筑的信息，因此还不能游玩。接下来是 pops 文件夹，再次找到 STATE_LIBYAN_DESERT，同样把 TRI 改为 CYR。在 buildings 文件夹中也这样做。该州没有定义的建筑。这很合理，考虑到它大部分是沙漠且人口很少，但请记住生存建筑会自动添加。

从 /Victoria 3/game/common/history/countries 复制另一个国家的文件，粘贴到你的 mod 的 countries 文件夹中，并将其重命名为 `cyr - cyrenaica.txt`。内容可以之后再改。

至此，history 文件夹的条目暂时完成了。

## 本地化（Localization）

参见：
本地化（Localization）
国家现在可以游玩了，但在游戏中它仍然显示为 CYR 而不是正式的国家名称。这时就需要本地化（localization）了。

这是本地化文件所在的位置。路径比文件名更重要。
本地化是将代码翻译成英语等人类语言的方式。是时候进入我们 mod 的 localization 文件夹了。

新建的本地化文件可以有任何名称，只要符合特定模式。文件必须：

- 是 `.yml` 文件
- 文件名以 `_l_english` 结尾（如果你的本地化是英语；否则使用该语言的脚本名称，通常是其英文名称）
- 文件内容以 `l_english:` 开头

建议直接从其他 mod 或原版游戏复制一个本地化文件并清空它（保留 `l_english:` 部分）。

本地化示例
本地化非常简单，如下所示：

```
TAG: "country name"
TAG_ADJ: "country adjective"
```

这里的 `TAG` 代表国家的 tag，即本例中的 CYR。

现在国家可以正常运行，名称看起来也可以接受了。

国家可以运行了，但也许自定义的国旗和统治者会更好

## 人口历史（Population history）

人口历史条目示例
一个相当可选的文件：人口历史。不要与 Pops 历史混淆，history 文件夹中的 population 文件夹提供关于居住在该国的人们的信息，特别是他们的财富和识字率。它通常使用两个 scripted effect，但可以使用任何一组相关的 effect。这些会修改国家人口的初始特征，但主要效果取决于其他因素，例如财富取决于开局时的建筑和生产方式，识字率取决于技术和教育机构。也就是说，即使一个国家有 `effect_starting_pop_literacy_very_high = yes`，如果没有教育机构，其人口也大多不识字。

财富：（定义于 /Victoria 3/game/common/scripted_effects/00_starting_pop_wealth.txt）

- effect_starting_pop_wealth_low
- effect_starting_pop_wealth_medium
- effect_starting_pop_wealth_high
- effect_starting_pop_wealth_very_high

识字率（定义于 /Victoria 3/game/common/scripted_effects/00_starting_pop_literacy.txt）

- effect_starting_pop_literacy_baseline
- effect_starting_pop_literacy_very_low
- effect_starting_pop_literacy_low
- effect_starting_pop_literacy_middling
- effect_starting_pop_literacy_high
- effect_starting_pop_literacy_very_high

这有助于国家的初始平衡，并会随着时间的推移对国家产生重要影响。

## 人物（Characters）

参见：
人物模组制作（Character modding）
这方面有很多可谈的！
如果希望统治者和国旗不是自动生成的，这些也可以被定义。

要让一个特定人物成为国家的统治者——或任何其他角色，该国家需要在人物历史文件夹（/Victoria 3/game/common/history/characters）中的某个文件里有条目。同样，建议浏览原版游戏和/或某个 mod，从中复制信息和文件。人物的可能设置可以在原版游戏的 common 文件夹中找到，寻找名称中包含 character 的文件夹。

昔兰尼加的脚本在这里。有一个名字和一个姓氏。**重要提示：**如果你的名称尚未本地化（因为它们不是已存在的人物或文化名称），你必须为它们添加单独的本地化。就昔兰尼加的情况而言，两个名称都已被某处本地化了，太好了！如果有必要对它们进行本地化，本地化内容可以放在任何文件中（一般来说，本地化的组织方式只是为了让人们更容易找到东西的位置）。

如果需要本地化名称，方法与上面的国家本地化基本相同：

```
Name: "Localized name"
```

所以如果昔兰尼加领导人的姓氏需要新的本地化，它会是这样的：

```
al-Idrisi: "al-Idrisi"
```

左边是"al-Idrisi"的脚本键，右边是"al-Idrisi"的英语本地化。这看似是多余的步骤，但很重要。如果游戏检测不到某个名称的本地化，它就不会使用所提供的名称，而是使用一个随机名称。

接下来是出生日期，用于计算年龄。

叶海亚（Yahya）应该是这个国家的统治者，所以脚本是 `ruler = yes`。还有其他角色，例如 `heir`。查看原版游戏或 mod 中的其他人物文件以了解更多。例如，英国有许多人物。可以将统治者设置为游戏开始时就是将军，但就昔兰尼加而言这是不必要的。它已被注释掉以便游戏忽略它，但好奇的人可以看到它的样子。

然后必须定义该人物所属或代表的利益集团（Interest Group）。这个人物是逊尼派乌理玛（Sunni Ulema）的成员，即穆斯林的虔信派利益集团。接下来是意识形态（ideology）。它们位于 /Victoria 3/game/common/ideologies/00_leader_ideologies。由于昔兰尼加城市化程度不高且主要依靠生存经济，我认为传统主义者（Traditionalist）意识形态最合适。最后是几个特质（trait），位于 /Victoria 3/game/common/character_traits 文件夹。

这是我的成果！

叶海亚就在那里，运行完美！

## 国旗（Flag）

参见：
国旗模组制作（Flag modding）
这看起来会很棒
新国旗的灵感将来自奥斯曼帝国的黎波里塔尼亚省的旗帜，并做一些小的改动。

在 Vic3 中制作一个基本国旗，只需在 /Victoria 3/game/common/coat_of_arms/coat_of_arms 中的某个文件里添加一个条目。国旗可以作为普通图像放入，但这比用脚本编写占用更多空间，而且不如脚本灵活。这是昔兰尼加的脚本：

简要说明：所有国旗都需要一个基本图案作为基础。它们位于 /Victoria 3/game/gfx/coat_of_arms/patterns。重要的是，所有国旗组件都必须放在引号中并包含文件扩展名（.tga、.dds）才能正常工作。

接下来是 `color1`，它指的是国旗元素中可以使用的第一种颜色。就昔兰尼加而言，`pattern_solid.tga` 只有一种颜色，所以只需要这些。如果用户想在稍后的元素中引用更多颜色，可以添加更多颜色（因此，与其在三个月亮中都写 `color1 = "yellow"`，代码本可以写成 `color1 = color2`，并在图案的 `color1` 下方写上 `color2 = "yellow"`。这样只需一次就能改变所有三个月亮的颜色，而无需将"yellow"更改三次）。

还有三个来自 /Victoria 3/game/gfx/coat_of_arms/colored_emistles 文件中的月亮，它们都是同一个徽记。如上所述，彩色徽记需要指定颜色，但如果不想使用默认大小和位于国旗中央的位置，就需要告诉游戏"这个实例应该是这个大小，徽记的中心应该位于这里"，这正是昔兰尼加国旗中的 *instances* 所做的。scale 指 x 和 y 轴的变形，如果不希望变形，两者填相同的数字即可。这面国旗将两个轴都缩小了一半，所以这些月亮是默认大小的四分之一。第一个月亮位于 `{ 0.25 0.3 }`，意思是 0.25 表示从左到右四分之一的位置（0 在国旗的左边缘），0.3 表示从国旗顶部到底部 30% 的位置（0 在顶部）。为后两个月亮设置了旋转值，以确保它们不与第一个月亮朝向相同的方向。

**另一个重要提示：**为了让制作国旗更轻松，建议用户打开游戏的命令行（在 Steam 库中右键点击游戏，查看属性，在最下方），写入 *-filewatcher -debug_mode*。前者会在文件保存时实时更新某些文件，因此无需重启游戏即可看到国旗调整；后者使查找 bug 和在游戏中查找信息变得更容易。

国旗现在完成了，整个国家也完成了。

国旗就在那里

## 动态国家名称与颜色

许多国家在特定情况下有替代名称和颜色。例如，内志（Nejd）在完全拥有汉志（Hedjaz）时会获得动态名称"沙特阿拉伯（Saudi Arabia）"，德国在拥有"委员会共和制"法律时会变成绿色。在 mod 中使用动态国家名称和颜色可以获得更好的体验。

### 动态国家名称

你可以在 /Victoria 3/game/common/dynamic_country_names 中定义动态名称，只需添加一个 `UTF-8 with BOM` 编码的文本文件。

例如

```
CYR = {
	dynamic_country_name = {
		name = dyn_CYR_empire #This can be just the TAG to reuse the default name
		adjective = dyn_CYR_empire_adj # This can be TAG_ADJ to reuse the default adjective

		is_main_tag_only = yes # default no, if yes then only the primary country for a definition can use this name (i.e. Poland, not a civil war revolt Poland)
		priority = 0 # default 0, if multiple names have valid triggers, higher priority is used. If same priority, first valid one in file is used
		
		trigger = { # Scripted trigger, country-scope
			coa_def_monarchy_flag_trigger = yes
			scope:actor = {
				owns_entire_state_region = STATE_TUNISIA
			}
		}
	}	
}
```

然后，为动态名称和动态形容词添加本地化：

```
dyn_CYR_empire:0 "Cyrenacia Empire"
dyn_CYR_empire_adj:0 "Cyrenacian"
```

### 动态国家颜色

你可以在 /Victoria 3/game/common/named_colors 中定义颜色，并在 /Victoria 3/game/common/dynamic_country_map_colors 中应用该命名颜色。动态颜色会应用第一个触发条件有效的颜色。

在 `named_colors` 中

```
colors = {	
	cyrenacia_empire_red = rgb { 1.0 0.15 0.15 } #This is "decimal" RGB, this value is similar to RBG 255 38 38 or hexcode ff2626
}
```
在 `dynamic_country_map_colors` 中：

```
cyrenacia_empire_red = {
	color = "cyrenacia_empire_red"

	possible = {
		OR = {
			AND = {
				exists = c:CYR
				THIS = c:CYR
			}
			AND = {
				exists = c:TRI # dynamic color can be applied in other country
				THIS = c:TRI
			}
		}
		owns_entire_state_region = STATE_LIBYAN_DESERT
		owns_entire_state_region = STATE_TUNISIA
	}
}
```

## 参考

Modding（模组制作）
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier 类型](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • 目标 • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • 概念 • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • 政党 • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • 附属国类型 • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| 地图 | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • [States](State modding.md) |
|---|---|

| 界面 | [Interface](Interface modding.md) • [GUI script](GUI script.md) • [Localization](Localization.md) • [Customizable localization](Localization.md) • [Script localization](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • 字体 • [Flags](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [Sound](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod 兼容性](Mod compatibility.md) • [Mod 结构](Mod structure.md) • [Scripted tests](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [Mod 翻译](Mod translation.md) • 新国家模组制作 • [Save-game editing](Save-game editing.md) • [州模组制作指南](State modding guide.md) |
|---|---|