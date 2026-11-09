---
translated: 2026-10-27
translator: machine (glm-5.3)
title: List of flags
source: https://vic3.paradoxwikis.com/List_of_flags
pageid: 2599
categories: [Potentially_outdated, 1.12, Articles_with_potentially_outdated_tables, Flags, Lists]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的部分。至少有部分内容最后是针对 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.12 核实的。

另见：
Category:Flags
游戏中的许多国家可以根据不同情况使用不同的旗帜。最重要的因素通常是该国的法律。如果多个旗帜的条件同时满足，则使用优先级最高的旗帜。本列表展示的旗帜不包含宗主国旗帜，若[游戏规则](Game rule.md) *“附属国旗帜”* 处于启用状态，宗主国旗帜通常会出现在旗帜的一角。被多次列出的旗帜在 /Victoria 3/game/common/flag_definitions/ 中有多个条目（通常具有不同的条件，或关于在何处显示宗主国旗帜的不同规则）。只有一种旗帜的国家未包含在本列表中，因为它们可以在[国家列表](Countries.md)中找到。自动生成的旗帜同样未包含在内。

游戏脚本中的宗主国标记`subject_canton`是在该国附属国的旗帜及游戏规则允许时，应用于其附属国旗帜的标记。游戏脚本中的附属国旗帜`coa_with_overlord_canton`是在该国为附属国时使用的旗帜。大多数情况下，这两者之一或两者都与该国的主旗帜相同。某些国家拥有特殊的附属国旗帜，用于作为特定国家（如大不列颠或法国）的附属国时。附属国的附属国在允许时使用其最高宗主国的标记。保护国和朝贡国从不更改其旗帜，也不允许使用标记。

旗帜变体的条件通常与该国[国名](Dynamic country names.md)或[地图颜色](Dynamic map colors.md)的条件一致，但并非总是如此。

所有没有优先级 1000 或以上旗帜的国家，在实行委员会共和制法律时会获得一面随机生成的共产主义主题旗帜。类似地，所有没有优先级 2000 或以上旗帜的国家，在实行无政府状态法律时会获得一面随机生成的无政府主义主题旗帜。

| 跳转到章节 |
|---|
| A • B • C • D • E • F • G • H • I • J • K • L • M • N • O • P • Q-R • S • T • U • V-Z |

## 列表

| ![Ambox outdated info.png](https://central.paradoxwikis.com/images/thumb/6/65/Ambox_outdated_info.png/22px-Ambox_outdated_info.png) | 请协助核实或更新此表格。此表格最后是针对版本 1.12 核实的。 |
|---|---|

[美利坚合众国](America.md)拥有大量代表已建州数量的旗帜——从不计入哥伦比亚特区和西弗吉尼亚。这些旗帜的优先级均为 5，因此若美国某个更高优先级的旗帜被使用，则不会使用这些旗帜。它们都使用相同的宗主国标记 `sub_USA_canton_star`，并允许应用宗主国标记。

| 美国旗帜 |
|---|
| USA_25 USA_26 USA_27 USA_28 USA_29 USA_30 USA_31 USA_32 USA_33 USA_34 USA_35 USA_36 USA_37 USA_38 USA_39 USA_40 USA_41 USA_42 USA_43 USA_44 USA_45 USA_46 USA_47 USA_48 USA_49 USA_50 USA_51 USA_52 USA_53 USA_54 USA_55 USA_56 USA_57 USA_58 USA_59 USA_60 USA_61 USA_62 USA_63 USA_64 USA_65 USA_66 USA_67 USA_68 USA_69 USA_70 USA_71 USA_72 USA_73 USA_74 USA_75 USA_76 USA_77 USA_78 USA_79 USA_80 USA_81 USA_82 USA_83 USA_84 USA_85 USA_86 USA_87 USA_88 USA_89 USA_90 USA_91 USA_92 USA_93 USA_94 USA_95 USA_96 USA_97 USA_98 USA_99 USA_100 |

## 参考资料

1. ↑ 严格来说，拥有变量 `algeria_deylik_restored`
2. ↑ 严格来说，拥有变量 `algeria_barbary_restored`
3. ↑ 3.0 3.1 可能是 bug，存在两行 `subject_canton`；此为游戏中显示的第二行
4. ↑ 4.0 4.1 4.2 即使更改附属国旗帜的游戏规则处于关闭状态也会使用
5. ↑ 5.0 5.1 5.2 5.3 5.4 5.5 如果美国存在且日志条目 *The American Civil War* 处于激活状态，此旗帜无法使用革命的“撕裂”图案
6. ↑ 严格来说，拥有变量 `legitimist_restoration_var`
7. ↑ 严格来说，拥有变量 `bonapartist_restoration_var`
8. ↑ 8.0 8.1 严格来说，拥有变量 `ROM_united_principality`
9. ↑ 9.0 9.1 严格来说，拥有变量 `king_sounds_better`

要更新此表格，请参阅“子列表”页面：

- [List of flags/a-d](List of flags_a-d.md)
- [List of flags/e-l](List of flags_e-l.md)
- [List of flags/m-r](List of flags_m-r.md)
- [List of flags/s-z](List of flags_s-z.md)