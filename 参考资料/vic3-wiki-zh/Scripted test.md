---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Scripted test
source: https://vic3.paradoxwikis.com/Scripted_test
pageid: 8927
categories: [Potentially_outdated, 1.10, Modding]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的部分。其中至少有一些内容最后是在 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10 时验证的。

脚本化测试（Scripted tests）是用来检查已定义的游戏状态达成频率的实用工具文件。它们不会以任何方式影响游戏玩法。

## 定义

脚本化测试定义于 /tools/scripted_tests/ 目录下。

它们采用如下形式：

```
last_date = "1900.1.1"

tests = {
    GER_forms = {
        acceptable_fail_rate = 0.0
        success = {
            exists = c:GER 
        }
        fail = {
            game_date > "1890.1.1"
        }
    }
    another_test = {
        ...
    }
    ...
}
```

### 组成要素

一个脚本化测试文件包含若干要素，其中大多数是必需的。每个文件可以包含任意数量的测试。所有测试都包含在 `tests = { }` 块内。

- `last_date` 决定文件中测试的有效期限。如果该日期已过，测试将不再被检查。如果两个 trigger 都未返回 true，则该测试会被标记为“已跳过”。
- `success` 是一个 [trigger](Trigger.md) 块，如果它在 fail trigger 和 `last_date` 之前返回 true，则该测试被标记为“通过”。
- `fail` 是一个 trigger 块，如果它在 success trigger 返回 true 之前、且在 `last_date` 之前返回 true，则该测试被标记为“失败”。两个 trigger 每天都会被检查，如果它们在同一天都返回 true，该测试会被标记为“通过”。
- `acceptable_fail_rate` 是一个十进制百分数值，用于元数据分析。它完全不影响测试行为。如果未定义，默认值为 0。
- `run_count` 是一个整数值，定义测试运行的次数。只有失败或通过的运行才会被计入。小于 0 的值会使测试无限期运行，即一直运行到 `last_date`。只有最后一次运行会被记录到输出中。如果未定义，默认值为 1。

## 用法

脚本化测试可以通过命令行参数或 console command（控制台命令）来启用。

与脚本化测试相关的命令行参数有三个：

- `-run_tests` / `-scripted_tests` – 启用脚本化测试
- `-no_save_after_failed_test` – 禁用在测试失败后的第二天创建存档；否则默认启用
- `-save_before_failed_test` – 禁用在测试失败前创建存档。这会非常慢，通常不建议使用。

脚本化测试有一个 console command：`scripted_tests`。它可以接受一个可选参数，用于选择在测试之前、之后（默认）创建存档，或者完全不创建存档

- `scripted_tests` – 在测试之后创建存档
- `scripted_tests before` – 在测试之前创建存档
- `scripted_tests none` – 不创建存档

如果脚本化测试已处于激活状态，再次输入该命令会禁用测试。

## 输出

测试结束时，会在文档（Documents）文件夹中生成一个包含结果的文本文件。此外，还会在游戏的可执行文件目录中生成一个 XML 文件。

## 参考

- 信息改编自 /Victoria 3/game/tools/scripted_tests/scripted_tests.md

Modding
返回顶部
| Documentation | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| Scripted content | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| Scripted types | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| Map | [Map](Map modding.md) • [Geographic regions](Geographic region modding.md) • [States](State modding.md) |
|---|---|

| Interface | [Interface](Interface modding.md) • [GUI script](GUI script.md) • [Localization](Localization.md) • [Customizable localization](Localization.md) • [Script localization](Script localization.md) |
|---|---|

| Graphics | [3D Models](Model modding.md) • [Event images](Event images.md) • [Graphical Assets](Graphical asset modding.md) • Fonts • [Flags](Flag modding.md) |
|---|---|

| Audio | Music • [Sound](Sound modding.md) |
|---|---|

| Other | [AI](AI modding.md) • [Console commands](Console commands.md) • [Checksum](https://vic3.paradoxwikis.com/Checksum) • [Mods](Mod.md) • [Mod compatibility](Mod compatibility.md) • [Mod structure](Mod structure.md) • Scripted tests • [Troubleshooting](Troubleshooting.md) |
|---|---|

| Guides | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|