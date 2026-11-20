---
translated: 2026-10-27
translator: machine (glm-5.3)
title: PDX DeepL
source: https://vic3.paradoxwikis.com/PDX_DeepL
pageid: 9899
categories: [Modding_tools, Modding]
fetched: 2026-10-27
---
Mod 工具
: PDX DeepL
PDX DeepL
---

类型
翻译
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

其他
下载
PDX DeepL
---

类型
翻译
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

其他
下载
**pdx-deepl** 是一个使用 DeepL 对 Paradox 游戏的 mod 进行增量自动翻译的工具。

## 它是如何工作的？

该工具会以一种基础语言为基准，检查基础语言中的 localization 键在其他语言中是否缺失或过期。如果某个键缺失或过期，它就会翻译基础语言的 localization（本地化文本），并将译文添加到另一种语言的同一文件中。此外，译文会附带基础语言键的校验和标记，这样在第二次运行时 pdx-deepl 就可以检查某个键是否被更新过。

## 手动翻译与机器翻译

由 pdx-deepl 生成的 localization 在结尾处会带有类似这样的注释：

```
 je_obj_magic_academy: "Magische Akademie bauen" #deepl:3993713733
```

这会将它们标记为机器翻译，必要时 pdx-deepl 会对其进行更新。

所有结尾处没有该注释的 localization 都会被视为手动翻译，pdx-deepl 不会对其进行改动。

在这个例子中，localization `objective_magic_dominance_idle_header` 被视为手动翻译，因此会被 pdx-deepl 忽略。

```
 je_obj_magic_academy: "Magische Akademie bauen" #deepl:3993713733
 objective_magic_dominance_idle_header: "Setzen Sie Ihren Weg fort"
```

该系统允许译者润色特定的 localization，这些润色在后续处理中会被保留。

## 支持的游戏

- 维多利亚3（Victoria 3）
- 十字军之王3（Crusader Kings 3）
- 欧陆风云5（Europa Universalis 5）

## 注释

不含 localization 的行上的注释会在翻译后的文件中被保留。

如果你想避免这种情况，可以使用 `#!` 来注释该行，这样它在翻译后的文件中就会被移除。 ### 示例 这个基础文件：

```
l_english:
 #! removed comment
 # preserved comment
 some_loc: "some loc content"
```

将变成：

```
l_german:
 # preserved comment
 some_loc: "some loc content"
```

### 特殊情况

翻译器会自动转义 localization 标签。

目前以下格式会被转义：

**格式化**

- 示例：`#bold Some Text#!`
- 像 `bold` 这样的格式化以及任何其他格式化都会被转义
- 任何以 `#` 开头、紧跟文本再跟一个空格的内容都不会被翻译
- 格式化的结束标记 `#!` 也会被转义，不会被改动

**函数**

- 示例：`Country [Country.GetName]`
- 像这样的 function 会被转义
- `[]` 内的所有内容都不会被翻译

**文本图标**

- 示例：`@innovation! Innovation`
- 像这样的文本图标会被转义
- `@!` 之间不含空格的所有内容都不会被翻译

**引用**

- 示例：`some $another_loc_key$ text`
- 像这样的引用会被转义
- 两个 `$` 之间的所有内容都不会被翻译

**换行符与制表符**

- 示例：`\tCountry\nNext Country`
- 像这样的换行符与制表符不会被翻译

## 配置

pdx-deepl 翻译需要使用 [translation-config.json](https://github.com/kaiser-chris/pdx-deepl/blob/master/translation-config.json) 进行配置。在这个文件中，你可以定义哪种语言作为翻译的基础语言，以及要生成哪些语言。

在这个例子中，`english` localization 会被视为唯一可信来源，pdx-deepl 将为 `german` 和 `french` 生成翻译，且不使用术语表。

```
{
  "base-language": "english",
  "target-languages": [
    {
      "name": "german"
    },
    {
      "name": "french"
    }
  ]
}
```

### 术语表

**注意：**不支持本地术语表！

可以在配置文件中通过 id 引用术语表：

```
{
  "base-language": "english",
  "target-languages": [
    {
      "name": "german",
      "glossary": "your-glossary-id"
    }
  ]
}
```

如何使用 DeepL API 创建和管理术语表可参见此处的文档：

- https://developers.deepl.com/docs/api-reference/glossaries

### 忽略文件

你可以通过将 localization 文件添加到忽略列表来忽略它们。

pdx-deepl 会完全忽略该列表中的文件，不会尝试翻译它们。

忽略列表包含不应被翻译的文件的（相对于 localization 根目录的）路径：

```
{
  "base-language": "english",
  "target-languages": [
    {
      "name": "german"
    }
  ],
  "ignore-files": [
    "english/your_loc_file_l_english.yml",
    "english/sub_directory/your_other_loc_file_l_english.yml"
  ]
}
```

## 统计信息

当 pdx-deepl 以 `-stats` 命令启动时，它会生成关于文件数和字符数的统计信息。这些信息在评估费用或使用额度时非常有用。

统计信息如下所示：

```
INFO 2025/05/02 01:12:49 API Type: free
INFO 2025/05/02 01:12:49 API Character Usage: 97919
INFO 2025/05/02 01:12:49 API Character Limit: 500000
INFO 2025/05/02 01:12:49 Target Language(s): german
INFO 2025/05/02 01:12:49 Base Language: english
INFO 2025/05/02 01:12:49 Localization Files: 62
INFO 2025/05/02 01:12:49 Localization Keys: 2456
INFO 2025/05/02 01:12:49 Total Characters: 159155
```

## 获取 DeepL API 访问权限

DeepL 提供免费版和专业版翻译方案。试用该工具时，我建议从免费账户开始。但如果你的 mod 很大，那么考虑专业版方案可能是值得的。

### DeepL 文档

- https://www.deepl.com/en/translator
- https://support.deepl.com/hc/en-us/articles/360019358899-Accessing-DeepL-s-API
- https://support.deepl.com/hc/en-us/articles/360020695820-API-Key-for-DeepL-s-API

## 用法

首先从仓库的 Releases 页面下载最新版本：- https://github.com/kaiser-chris/pdx-deepl/releases

该 ZIP 文件可能被标记为*病毒*。这是**误报**！

如果你不放心，可以自行构建。

然后你可以像这样运行该应用程序：

```
.\pdx-deepl.exe --localization="X:\path\to\localization\directory" --api-token="your token"
```

**注意：**此路径特指你 mod 中的 **localization** 文件夹

所有启动命令都可以在帮助对话框中找到。帮助对话框（`.\pdx-deepl.exe -h`）：

```
Usage of pdx-deepl:
  -api-token string
        Required: Deepl API Token
  -api-type string
        Optional: Whether to use free or paid Deepl API (default "free")
  -config string
        Optional: Path to translation config file (default "translation-config.json")
  -localization string
        Optional: Path to localization directory of your mod (default ".")
  -stats
        Optional: When set produces relevant statistics about the localization like the character count
```

### 使用提示

如果你不知道如何在 Windows 上打开命令行：

- 打开包含 `pdx-deepl.exe` 的文件夹
- 点击资源管理器顶部的地址栏
- 清空它
- 输入 `cmd` 并按回车
- 现在你应该已经打开了一个命令行窗口

## 免费 DeepL API 的问题

当前版本在使用 DeepL **免费** API 时存在一些问题：

- 你会遇到“too many requests”错误，这是由 DeepL API 的速率限制造成的。免费 API 的优先级低于付费 API
- 当前实现在遇到该问题时会跳过同一文件中的其余 loc 键。由于整个过程是增量的，你需要重新运行该应用程序来生成更多键。对于我的 `german` 翻译，我不得不运行非常多次，但最终还是完成了
- 免费 API 确实存在每月 50 万字符的限额，在翻译大型 mod 时这可能是个问题。但在另一位开发者的 PC 上使用另一个账户运行应该可以生成更多翻译
- 我建议先从一种语言开始，而不是多种语言

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

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|