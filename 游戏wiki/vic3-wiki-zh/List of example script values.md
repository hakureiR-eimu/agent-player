---
translated: 2026-10-27
translator: machine (glm-5.3)
title: List of example script values
source: https://vic3.paradoxwikis.com/List_of_example_script_values
pageid: 7700
categories: [Timeless, Pages_with_interwiki_links_to_Wikipedia, Modding, Lists]
fetched: 2026-10-27
---
本文为 [timeless](https://vic3.paradoxwikis.com/Category:Timeless)（不受版本限制）文章，适用于游戏的任何版本。

主条目：
Script value
这些 [script value](Script value.md)（脚本值）公式以及配套的 [effect](Effect.md) 或 [trigger](Trigger.md) 对 mod 作者可能有用或有趣。欢迎自行添加。请附上一些关于公式如何运作以及它为何可能有用或有趣的说明。

## 斐波那契数列（Fibonacci sequence）

该公式通过设置两个变量的值并计算数列中的下一个值来复现 [斐波那契数列](http://en.wikipedia.org/wiki/en:Fibonacci_sequence)[wp 1]。它利用 scripted effect 来设置变量。

**Scripted effect**

```
initialize_sequence = {
  set_variable = { name = first_value value = 0 }
  set_variable = { name = second_value value = 1 }
}
increment_sequence = {
  set_local_variable = { name = current_value value = fibonacci }
  set_variable = { name = first_value value = var:second_value }
  set_variable = { name = second_value value = local_var:current_value }
}
```

**Script value**

```
fibonacci = {
  value = var:first_value
  add = var:second_value
}
```

变量以斐波那契数列的前两个值 0 和 1 初始化。然后将它们相加并移动数值，使第二个值变为第一个值，和变为第二个值，其间使用一个局部（临时）变量来存储和。

这是一个如何使用同一 script value 公式迭代递增变量值的示例。

## 伪随机排序

使用 `ordered_` 迭代器（[iterators](https://vic3.paradoxwikis.com/Iterators)，通过如下脚本可以获得一种伪随机排序：

```
ordered_country = {
 order_by = {
  value = gdp
  modulo = { int int }
 }
 max = int
 <effects>
}
```

其原理是将每个国家按其当前 GDP 的随机取模结果进行排序。这可以用来替代对 `random_` 迭代器的多次调用。

这种方法适用于任何能够找到足够唯一取值的迭代器。例如对州使用 `state_population` 或 `gdp`。

## HHI 指数

通过迭代运算，可以使用如下脚本获得一个表示 [市场集中度](https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index)（market concentration）的动态值：

```
if = {
  limit = {
    num_companies > 0
  }
  add = {
    add = {
      every_company = {
        add = {
          value = company_employed_levels
          multiply = company_employed_levels
        }
      }
    }
    divide = {
      value = {
        every_company = {
          add = company_employed_levels
        }
      }
      multiply = {
        every_company = {
          add = company_employed_levels
        }
      }
    }
    subtract = {
      value = 1
      divide = num_companies
    }
    multiply = 8.9  #Adjust to scale, results in a value of 1 if a company owns 50% of all company-owned building levels, and a value of 7.1 if you have just one company.
  }
}
```

该脚本通过将每家公司的规模（经由 company_employed_levels）与公司建筑的市场总量进行比较，来计算市场整合程度。通过对单个市场份额求平方，它会让较大的公司获得不成比例的权重，因此非常适合作为涉及垄断或公司竞争机制的 trigger。

减去 1 / num_companies 起到“归一化”的作用：如果市场中每家公司拥有的建筑等级完全相同，无论存在多少家公司，结果都恰好为 **0**。当某家公司变得比同行更大时，该值便会增加，从而为政治进度或经济 modifier 提供平滑的缩放效果。

( ∑ ∑ Co's employed levels 2 ( ∑ ∑ Co's employed levels ) ⋅ ⋅ ( ∑ ∑ Co's employed levels ) − − 1 number of Co's ) ⋅ ⋅ C {\displaystyle \left({\dfrac {\sum ^{\text{Co's}}{\text{employed levels}}^{2}}{(\sum ^{\text{Co's}}{\text{employed levels}})\cdot (\sum ^{\text{Co's}}{\text{employed levels}})}}-{\frac {1}{\text{number of Co's}}}\right)\cdot C} ![{\displaystyle \left({\dfrac {\sum ^{\text{Co's}}{\text{employed levels}}^{2}}{(\sum ^{\text{Co's}}{\text{employed levels}})\cdot (\sum ^{\text{Co's}}{\text{employed levels}})}}-{\frac {1}{\text{number of Co's}}}\right)\cdot C}](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/51823baee74a2363f3f8ad5c891bdf246d7519ac)

## 参考

---

维基百科链接参考：

1. ↑ 链接至英文维基百科条目

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

| 指南 | [Mod translation](Mod translation.md) • [New country modding](New country modding.md) • [Save-game editing](Save-game editing.md) • [State modding guide](State modding guide.md) |
|---|---|