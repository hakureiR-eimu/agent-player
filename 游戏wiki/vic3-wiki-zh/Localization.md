---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Localization
source: https://vic3.paradoxwikis.com/Localization
pageid: 3496
categories: [Potentially_outdated, 1.10, Expand, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。其中至少部分内容最后验证于 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10。

|  | 请通过[扩充](https://vic3.paradoxwikis.com/index.php?title=Localization&action=edit)本文或本章节来帮助改进它：更多数据 function 及其他本地化文档的细节。 |
|---|---|

本地化文件必须是 UTF-8-BOM 编码的 `.yml` 格式。否则，游戏会直接忽略该文件。此外，文件名必须以 `_l_<language>` 结尾；只要遵循此格式，可以使用任何文件名。例如：`MODNAME_USAGE_decisions_l_english.yml`。

本地化文件按字母倒序（从 Z 到 A）处理，在本地化文件名开头加上 `a` 或 `0` 可以确保其最后应用。在替换原版本地化时，更好的做法是使用 `replace` 文件夹，如 `/english/replace/overwriting_l_english.yml`。replace 文件夹中的文件运作方式略有不同，其中的本地化键会被专门检查，并覆盖其他任何相同的本地化键。

请注意，与 Paradox 开发工作室以往的一些游戏不同，本游戏中存放显示文本的文件夹名为带 "z" 的 "Localization"，而不是带 "s" 的 "Localisation"。

**注意：** 所有呈现给玩家的文本*必须*通过本地化键实现。脚本类型中使用的任何“已本地化”文本实际上只是一个未本地化的键，会按原样显示。在某些脚本类型中——例如事件，这可以正常运作，但其他脚本类型会显示错误或无法按预期工作。

## 语言

每种受支持的语言都有一个内部名称，用作该语言子文件夹的名称。内部名称加上前缀 `l_`（即小写字母 L），也用于 YAML 文件的命名格式，以及 YAML 文件第一行中的语言标识符。

| 语言 | 内部名称 |
|---|---|
| 英语 | english |
| 巴西葡萄牙语 | braz_por |
| 法语 | french |
| 德语 | german |
| 波兰语 | polish |
| 俄语 | russian |
| 西班牙语 | spanish |
| 日语 | japanese |
| 简体中文 | simp_chinese |
| 韩语 | korean |
| 土耳其语 | turkish |

## 基础示例

本地化允许游戏对象根据特定条件（通常是用户选择的语言）渲染出不同的文本。在《维多利亚3》中，本地化将一个本地化*键*（通常是一个已定义的脚本术语，如国家的 TAG，或事件、日志条目、外交行动的脚本名）与一个已定义的文本字符串连接起来。

许多本地化键有由游戏引擎生成的相关键。例如，国家的 TAG_ADJ，或日志条目描述文本的 journal_entry_reason。请参考游戏的信息文件或本 wiki 的其他 modding 文章来确定此类键。

每条本地化条目应如下所示：

```
 key: "Localized text"
```

具体来说：每条条目是一行，以一个空格开头，然后是确切的本地化键、一个冒号、再一个空格，以及包含在双引号中的本地化字符串。冒号后可以跟一个数字来跟踪修订版本，但这不是必需的。

一个完整但简短的本地化文件如下所示：

```
l_<lang>:
 key: "Localized text"
```

可以在引号外使用 `#` 添加注释，可单独成行或紧跟在本地化条目之后。

### 本地化复用

本地化键可以通过在本地化字符串中添加 `$key$` 来互相引用。

例如：

```
key1: "example"
key2: "This is an $key1$"
```

key2 在游戏中将显示为 "This is an example"。以这种方式复用本地化键是减少相关键所需改动的好方法。

## 格式化

与其他 Paradox 游戏类似，《维多利亚3》有多种为本地化应用自定义格式化的方法。所有自定义格式化都以 `#` 开头，后跟格式化键以开始格式化。格式化键与实际文本之间需要一个空格，但该空格不会体现在实际文本中。最后，需要 `#!` 来结束格式化。不过，`#!` 之前不应有空格。自定义格式化可以嵌套，每个新的格式化键都需要自己的 `#!` 来结束格式化。另外，自定义格式化也可以用分号连接。

### 字符着色

参见
{{Color}}
以在 wiki 上使用这些游戏文本颜色
下面是一个将部分文本着色为红色的示例：

```
my_loc: "This #R text#! is red!"
```

基础游戏中实现了以下格式化键来为字符着色：

| 键 | 说明 | 颜色 |
|---|---|---|
| #! | 结束当前格式化规则。 | 无 |
| #r |  | 红色 |
| #green |  | 绿色 |
| #light_green |  | 浅绿色 |
| #blue | 亦即 #U | 蓝色 |
| #white |  | 白色 |
| #darker_white | 亦即 #default_text | 暗白色 |
| #yellow |  | 黄色 |
| #gold | 亦即 #O，与概念文本同色。 | 金色 |
| #black |  | 黑色 |
| #gray | 亦即 #lore | 灰色 |

### 其他自定义格式化

在《维多利亚3》中，可以对本地化应用其他形式的格式化，包括加粗和斜体文本。其他格式化形式与着色文本类似，需要以 # 开始格式化规则，以 #! 结束。

| 键 | 效果 | 示例 |
|---|---|---|
| #! | 结束当前格式化规则。 |  |
| #b | 加粗文本。 |  |
| #italic | 使文本斜体。 |  |
| #lore | 使文本变浅。 |  |
| #shadow | 为文本添加阴影 |  |
| #l/#L | 为文本添加下划线 |  |

### 文本图标

以下是本地化中使用文本图标的示例，脚本为：
```
my_loc: "I love people who wear @capitalists! hats!"
```

可以在本地化字符串中添加图标。基础游戏文本图标定义在文件 /Victoria 3/game/gui/texticons.gui 中，mod 可在 <mod>/gui 中的任何 .gui 文件中添加新图标。

所有文本图标以 `@` 开头，后跟图标的键，键后跟 `!`。为简单起见，下表中已包含这些符号。

注意：这不是完整列表。以下仅为部分图标示例。

| 键 | 图标 |
|---|---|
| @information! | ![Information.png](/images/thumb/5/54/Information.png/24px-Information.png) |
| @warning! | ![Warning.png](/images/thumb/c/cb/Warning.png/24px-Warning.png) |
| @money! | ![Hud money.png](/images/thumb/3/32/Hud_money.png/24px-Hud_money.png) |
| @censored! |  |
| @green_checkmark! | ![Yes.png](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| @red_cross! | ![No.png](/images/thumb/0/04/No.png/24px-No.png) |
| @construction! | ![State status construction.png](/images/thumb/5/56/State_status_construction.png/24px-State_status_construction.png) |
| @bur! | ![Hud bureaucracy.png](/images/thumb/7/75/Hud_bureaucracy.png/24px-Hud_bureaucracy.png) |
| @aut! | ![Hud authority.png](/images/thumb/0/08/Hud_authority.png/24px-Hud_authority.png) |
| @inf! | ![Hud influence.png](/images/thumb/0/06/Hud_influence.png/24px-Hud_influence.png) |
| @innovation! | ![Innovation.png](/images/thumb/4/42/Innovation.png/24px-Innovation.png) |
| @officers! | ![Pop officers.png](/images/thumb/a/a4/Pop_officers.png/24px-Pop_officers.png) |
| @capitalists! | ![Pop capitalists.png](/images/thumb/1/12/Pop_capitalists.png/24px-Pop_capitalists.png) |
| @clergymen! | ![Pop clergymen.png](/images/thumb/a/ad/Pop_clergymen.png/24px-Pop_clergymen.png) |
| @engineers! | ![Pop engineers.png](/images/thumb/6/64/Pop_engineers.png/24px-Pop_engineers.png) |
| @devout! | ![IG devout.png](/images/thumb/a/a7/IG_devout.png/24px-IG_devout.png) |

## 数据函数

主条目：
GUI 脚本
数据函数允许在本地化字符串中包含动态文本。函数总是用方括号括起来。有些函数单独使用，而许多其他函数可以用句点“点链式”组合。通常，链式函数用于先切换 scope，再从最终 scope 获取某些本地化信息。输出字符串的数据函数也可视为本地化函数。

以下是一些数据函数的示例，其中许多以 "Get" 开头，且总是以 "UpperCamelCase" 或 "PascalCase"（大驼峰命名法）书写（如 "GetName"）

| 函数名 | 描述 |
|---|---|
| GetName | 以带工具提示的字符串返回名称。对于国家，还会返回国旗 |
| GetNameNoFlag | 以带工具提示的字符串返回国家名称，不含国旗 |
| GetAdjective | 以带工具提示的字符串返回国家形容词 |
| GetAdjectiveNoFormatting | 以纯字符串返回国家形容词 |
| GetPrimaryRoleTitle | 以带工具提示的字符串返回人物的主要角色 |

许多函数需要输入参数，例如类型键、变量或已保存的 scope 名称。这些函数用圆括号括住输入，游戏脚本对象用单引号，其他数据函数则不用。如果需要多个输入参数，则以逗号分隔。

| 函数名 | 描述 |
|---|---|
| GetGoods(' ') | 将输入的商品作为对象返回，以供后续函数使用 |
| ScriptValue(' ') | 返回输入的命名 script value 的计算值 |
| GetCurrentBarValue( ) | 返回进度条的值，通常与 `ScriptedProgressBar.Self` 一起使用 |

### 函数格式化

本地化函数可以像常规本地化字符串一样格式化，但它们还有特殊的格式化。函数格式化用右方括号前的竖线 `|` 表示。所有格式化修饰符放在竖线和方括号之间，许多可以一起使用。

| 格式代码 | 功能 | 与之不兼容 |
|---|---|---|
| `*` | 在阈值为 1 000、1 000 000 和 1 000 000 000 时将数值转换为 K、M 或 B 格式 | `K` |
| `K` | 将数值转换为 K 格式，固定 2 位小数 | 覆盖 `*` 和小数位数 |
| `=` | 为正值添加 "+"，为负值添加 "-" |  |
| `+` | 正值着绿色，负值着红色 | `- : ;` 使用最后定义的 |
| `-` | 正值着红色，负值着绿色 | `+ : ;` 使用最后定义的 |
| `:` | 正值着金色，负值着蓝色 | `- + ;` 使用最后定义的 |
| `;` | 正值着蓝色，负值着金色 | `- + :` 使用最后定义的 |
| U | 首字母大写 | 覆盖 `l` |
| l | 首字母小写 | `U` |
| L | 为文本添加下划线 |  |
| `%` | 将数值转换为百分比（乘以 100，添加百分号），若与 `*` 或 `K` 一起使用，则不进行乘法 |  |
| `1-5` | 决定显示的小数位数，与 `*` 一起使用时最多 3 位 | `K` |

## 概念

概念是内置的信息指南，通过解释该概念的工具提示向玩家提供信息。概念文本默认为橙色，但任何其他格式化也可应用于概念文本。概念定义在 /Victoria 3/game/common/game_concepts 中。概念可以指定自定义图标或使用默认图标。每个定义的概念之后都必须照常进行本地化。

要在本地化字符串中添加概念工具提示，请使用 `[<concept_name>]`。以下是将概念添加到另一个本地化字符串的示例：

```
my_loc: "We have no [concept_legitimacy]!"
```

### 备用概念文本

概念还可以使用备用文本，可以是另一个本地化字符串或临时本地化字符串。《维多利亚3》开发者常用备用概念文本来使概念文本变为复数形式或不同的动词形式，或为没有概念的事物创建概念文本。

以下是一个备用概念文本的示例，悬停时会显示建筑概念。这将建筑概念与文本 “国家建筑效率”（State Construction Efficiency）链接，而不仅仅是文本“建筑”（Construction）。注意，这是一个带参数的*本地化函数*示例，可通过圆括号识别。在此例中，该函数搜索以第一个参数给出的脚本名命名的概念，并以第二个参数给出的条目对该概念进行本地化。

```
my_loc: "It is unfortunate, but we do not have any [Concept('concept_construction', 'State Construction Efficiency')]"
```

## 自定义工具提示

本地化字符串可以将自定义工具提示定义为字符串的一部分。为此，本地化字符串应包含以下内容之一：

- `#tooltippable;tooltip:<tooltip_loc_key> <tooltip_text>#!`
- `#tooltippable #tooltip:<tooltip_loc_key> <tooltip_text>#!#!`

这将创建一个工具提示，其中主本地化字符串以黄色显示 <tooltip_text>，但若将鼠标悬停在其上，工具提示将显示 <tooltip_loc_key>

## 已保存的 scope

与其他 Paradox 游戏类似，《维多利亚3》允许保存游戏对象以供日后使用。在本地化中，这些已保存的 scope 可以与本地化函数（如 "GetName" 或 "GetHerHis"）一起使用。根据已保存 scope 的类型，不同的函数可能有效或无效，并可能输出不同结果。例如，对国家使用 "GetName" 时，除名称外还会显示该国当前国旗，而对人物或利益集团则仅显示名称。

已保存的 scope 可通过本地化函数包含在本地化中。它们总是以 `[SCOPE` 开头，后跟特定类型的 scope，以及后续的函数（如 "GetName"）。在每种情况下，函数都以句点分隔/链接。

保存 scope 是一种 effect（游戏内效果脚本），可在大多数允许 effect 的地方执行。已保存的 scope 可用于多种目的，包括本地化。但请注意，将已保存的 scope 用于本地化在时机上有一些限制；通常，scope 必须在 `immediate` 块中，或在更早的事件或相关内容对象中保存。已保存 scope 的存续时间取决于其用途。例如，对于日志条目，已保存的 scope 在该条目处于活动状态期间一直有效。

### 国家作为已保存的 scope

在此示例中，美利坚合众国被保存为一个任意命名的 scope，使用以下脚本：

```
immediate = {
	c:USA = {
		save_scope_as = usa_nation_scope
	}
}
```

既然美国的 scope 已保存，现在就可以在本地化函数中使用该已保存的脚本名。如下所示。

```
my_je_reason: "The [SCOPE.sCountry('usa_nation_scope').GetName] is a country in the Western Hemisphere."
```

对于已保存的国家 scope，使用函数 `sCountry('scope_name')`。后跟所需的本地化函数，如 "GetName" 或 "GetAdjective"

使用已保存 scope usa_nation_scope 的一些函数示例：

| 示例脚本 | 效果 |
|---|---|
| [SCOPE.sCountry('usa_nation_scope').GetName] | 获取国家名称。 |
| [SCOPE.sCountry('usa_nation_scope').GetNameNoFormatting] | 获取不带格式的国家名称。 |
| [SCOPE.sCountry('usa_nation_scope').GetNameNoFlag] | 获取不带国旗的国家名称。 |
| [SCOPE.sCountry('usa_nation_scope').GetAdjective] | 获取国家形容词（此处为 American）。 |
| [SCOPE.sCountry('usa_nation_scope').GetAdjectiveNoFormatting] | 获取不带格式的国家形容词（此处为 American）。 |

### 人物作为已保存的 scope

在此示例中，一国的统治者被保存为一个任意命名的 scope，使用以下脚本：

```
immediate = {
	ruler = {
		save_scope_as = pru_leader
	}
}
```

既然该人物已保存为 scope，现在就可以在本地化函数中使用该已保存的脚本名。

```
mymod_pru_events.1.f: "Our leader, [SCOPE.sCharacter('pru_leader').GetFullName] has informed us of our magnificence."
```

对于已保存的人物 scope，使用函数 `scharacter('scope_name')`。同样，后跟所需的本地化函数，如 "GetName" 或 "GetAdjective"

与国家 scope 类似，有多种可用的函数。以下展示了使用 pru_leader 示例的此类脚本示例。
| 示例脚本 | 效果 |
|---|---|
| [SCOPE.sCharacter('pru_leader').GetFullName] | 获取人物的全名。 |
| [SCOPE.sCharacter('pru_leader').GetFullNameNoFormatting] | 获取不带格式的人物全名。 |
| [SCOPE.sCharacter('pru_leader').GetFirstName] | 获取人物的名。 |
| [SCOPE.sCharacter('pru_leader').GetFirstNameNoFormatting] | 获取不带格式的人物名。 |
| [SCOPE.sCharacter('pru_leader').GetLastName] | 获取人物的姓。 |
| [SCOPE.sCharacter('pru_leader').GetLastNameNoFormatting] | 获取不带格式的人物姓。 |
| [SCOPE.sCharacter('pru_leader').GetSheHe] | 若人物为女性则获取 'she'，为男性则获取 'he'。 |
| [SCOPE.sCharacter('pru_leader').GetHerHis] | 若人物为女性则获取 'her'，为男性则获取 'his'。 |
| [SCOPE.sCharacter('pru_leader').GetHerselfHimself] | 若人物为女性则获取 'herself'，为男性则获取 'himself'。 |

## 可自定义本地化（Customizable Localization）

与其他 Paradox 游戏不同，自定义本地化只能通过局部 scope 中的数据 function GetCustom('custom_localization_name') 或全局 scope 中的 [Localize('custom_localization_name')] 来调用。二者都指向 /Victoria 3/game/common/customizable_localization 中的一个脚本化 function。

每个自定义本地化都有其脚本名称，由该 function 引用，然后是一个类型以及一列由 trigger 触发或随机选取的本地化键。类型决定其 trigger 使用哪个 scope，而 random_valid 决定是选取第一个有效的键还是随机选取一个有效的键。默认使用第一个有效的键。

### 示例

这是一个如何创建可自定义本地化文件的示例。它应放在 `/common/customizable_localization` 文件夹中。

```
ruler_residence = {
	type = country # The scope that the localization applies to. Examples include 'country', 'character' or 'building'
	random_valid = yes # Optional. If no, will pick the first valid option
	
	text = {
		trigger = { # The conditions that must be met for the key to be valid. The scope is the same as the localization, in this case, a country.
			has_law = law_type:law_monarchy
		}
		localization_key = custom_royal_palace
	}

	text = {
		trigger = {
			has_law = law_type:law_presidential_republic
		}
		localization_key = custom_presidential_palace
	}

	text = {
		trigger = {
			any_scope_state = {
				is_coastal = yes
			}
		}
		localization_key = custom_seaside_palace
	}

	text = {
		trigger = {
			always = no
		}
		fallback = yes # Optional. If fallback is enabled, this option will be picked when there are no other valid options, even if the trigger isn't met.
		localization_key = custom_palace
	}
}
```

要使其生效，这些键必须在本地化文件中定义。

```
l_english:
 custom_royal_palace: "royal palace"
 custom_presidential_palace: "presidential palace"
 custom_seaside_palace: "seaside palace"
 custom_palace: "palace"
```

### 用法

要使用自定义本地化，必须在本地化文件中调用 `GetCustom()` function。以下是示例自定义本地化在事件描述中的用法：

```
l_english:
 ruler_killed_event.1.t: "Ruler Killed"
 ruler_killer_event.1.d: "Our ruler was killed yesterday, while at the [ROOT.GetCountry.GetCustom('ruler_residence')]."
```

根据条件不同，括号中的代码会被随机选取的本地化内容替换。例如，如果国家是君主制且没有沿海的州，它会被替换为 "royal palace"。如果是总统制共和且有沿海的州，则会在 "presidential palace" 或 "seaside palace" 之间随机选取。而如果既不是君主制、也不是总统制共和、也没有任何沿海的州，则会使用通用的备用选项 "palace"。

### 支持的类型

自定义本地化可以使用以下任意类型：

- AmendmentType
- Battle
- Building
- BuildingType
- CanalType
- Character
- CivilWar
- CombatUnit
- CommanderOrder
- CommanderOrderType
- Country
- CountryCreation
- CountryDefinition
- CountryFormation
- Culture
- Decree
- DiplomaticActionType
- DiplomaticPact
- DiplomaticPlay
- DiplomaticRelations
- Front
- Hq
- Ideology
- Institution
- InstitutionType
- Interest
- InterestGroup
- InterestGroupTrait
- JournalEntry
- Law
- LawType
- Market
- MarketGoods
- Objective
- Party
- PoliticalMovement
- Pop
- PopType
- Province
- Religion
- ShippingLane
- State
- StateRegion
- StateTrait
- StrategicRegion
- Technology
- Theater
- TradeRoute
- War

## 参考

Mod 模组制作
返回顶部
| 文档 | [Defines](Defines.md) • [effect](Effect.md) • [Event targets](Event target.md) • [Scope](Scope.md) • [trigger](Trigger.md) [宏](Macro.md) • [修改器类型](Modifier types.md) • [on_action](https://vic3.paradoxwikis.com/On_actions) • [脚本值](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [决议](Decision modding.md) • [事件](Event modding.md) • [历史](History modding.md) • [日志](Journal modding.md) • [修改器](Modifier modding.md) • 目标 • [脚本化 GUI](Scripted gui.md) |
|---|---|

| 脚本类型 | [建筑](Building modding.md) • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • 本地化 • [可自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图片](Event images.md) • [图形资源](Graphical asset modding.md) • 字体 • [旗帜](Flag modding.md) |
|---|---|

| 音频 | 音乐 • [声音](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [Mod](Mod.md) • [Mod 兼容性](Mod compatibility.md) • [Mod 结构](Mod structure.md) • [脚本化测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [Mod 翻译](Mod translation.md) • [新国家制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州制作指南](State modding guide.md) |
|---|---|