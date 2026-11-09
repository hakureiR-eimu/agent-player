---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Game rule
source: https://vic3.paradoxwikis.com/Game_rule
pageid: 4773
categories: [Potentially_outdated, 1.10, Game_concepts, Lists]
fetched: 2026-10-27
---
请协助验证或更新本文中较旧的章节。至少部分章节最后验证于 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) 1.10。

**游戏规则（Game rules）** 是开局新建游戏时可用的配置选项，能够改变部分游戏机制。游戏规则可以保存为预设。只有*成就*游戏规则会影响玩家解锁[成就](Achievements.md)的能力。

游戏规则在游戏开始时设定，可通过*切换国家*菜单选项进行更改。铁人模式这一游戏规则无法更改，而更改成就游戏规则则不会产生任何效果。

## 游戏规则列表

在下表中，**加粗**的设置为默认设置。*学习游戏*这一[目标](Objective.md)默认使用*宽松*的 AI 行为与*低*的 AI 侵略性。

| 规则 | 设置 | 效果 |
|---|---|---|
| 成就 | **允许** | 在本次战役中可以解锁[成就](Achievements.md) |
| 禁止 | 在本次战役中*不会*解锁成就 |  |
| AI 对玩家的行为 | 宽松 | AI 国家会对玩家国家表现得更加友好，并在[外交博弈](https://vic3.paradoxwikis.com/Diplomatic_plays)中对其更加宽容 |
| **标准** | AI 国家以相同的方式看待玩家国家和 AI 国家，对玩家没有特殊考虑 |  |
| 严厉 | AI 国家会更加怀疑玩家国家的意图，并在外交博弈中对其更加严厉 |  |
| AI 侵略性 | 低 | AI 国家发起的外交博弈更少，征服领土的倾向更低 |
| **标准** | AI 国家根据其战略采用标准侵略性设置 |  |
| 严厉 | AI 国家发起的外交博弈更多，征服领土的倾向更高 |  |
| 忠诚宽限期 | **无** | 从游戏一开始，你就会承受[激进派](https://vic3.paradoxwikis.com/Radical_(pop)和[忠诚派](https://vic3.paradoxwikis.com/Loyalist_(pop)的全部影响 |
| 短 | 激进派和忠诚派的增长初始较低但会逐步提升，在开局 1 年后达到完全效果 |  |
| 长 | 激进派和忠诚派的增长初始较低但会逐步提升，在开局 5 年后达到完全效果 |  |
| 特长 | 激进派和忠诚派的增长初始较低但会逐步提升，在开局 10 年后达到完全效果 |  |
| 可成立国家 | **全部** | 允许[成立](Formable countries.md)不合常理以及幻想风格的国家 |
| 历史合理 | 仅允许成立历史上合理可行的国家[1] |  |
| 可释放国家 | **全部** | 允许[释放](Releasable countries.md)不合常理以及幻想风格的国家 |
| 历史合理 | 仅允许释放历史上合理可行的国家[2] |  |
| 人口合并（性能）[3] | 无 | [人口](Pops.md)除同化或转教规则外绝不会合并，无论其规模大小。这可能严重损害游戏中后期的性能 |
| 轻微 | 人口只有在规模极小且无足轻重时才会合并。可能损害游戏中后期的性能。 |  |
| **中等** | 人口在规模相当小且对游戏影响有限时可能会合并。 |  |
| 激进 | 在条件合适时，即使是中等规模的人口也可能合并。可能改善性能，但会影响游戏平衡 |  |
| 奇观效果 | **启用** | [奇观](https://vic3.paradoxwikis.com/Monuments)可根据其性质产生多种不同效果，且通常会雇佣人口来实现这一点。 |
| 仅威望 | 所有奇观为其国家产生固定数量的[威望](https://vic3.paradoxwikis.com/Prestige)。没有奇观会雇佣人口。[原文如此] |  |
| 禁用 | 奇观仅为装饰。建造它们的奖励纯粹是视觉上的。 |  |
| 附属国国旗 | 不更改国旗 | [附属国](Subject.md)的国旗*不会*根据其宗主国是谁而改变 |
| **允许更改国旗** | [附属国的国旗](List of flags.md)可能会根据其宗主国是谁而改变 |  |
| 附属国地图颜色 | 不更改地图颜色 | 附属国的地图颜色*不会*根据其宗主国是谁而改变 |
| **允许更改地图颜色** | 某些类型附属国的地图颜色可能会根据其宗主国是谁而改变 |  |
| 幻想内容 | **启用** | 在本次战役中允许超自然或幻想内容 |
| 禁用 | 在本次战役中不允许超自然或幻想内容 |  |
| 自定义随机数种子 | **禁用** | 游戏会自动设置随机数种子，使每次游玩的结果各不相同。 |
| 启用 | 允许设置特定的随机数种子，使大多数随机结果遵循该种子。因此，使用相同种子时，初始化以及无玩家交互的观察者模式游戏在多次游玩中会产生相同的结果。 |  |
| 动态命名 | **启用** | 州和城市会根据拥有国的文化改变其名称 |
| 禁用 | 州和城市不会根据拥有国的文化改变其名称 |  |

## 铁人模式

**铁人模式（Ironman）** 是一项特殊的游戏规则，它会禁用切换国家、进入观察者模式以及手动保存。游戏会按照游戏设置（默认为每个月）自动定期保存，退出游戏时也会保存。与其他 Paradox 游戏不同，铁人模式并非获得成就的前提条件。

## 注释

1. ↑ 不包括[拜占庭](Byzantium.md)、[卡罗来纳](Carolina.md)和[中欧](Central Europe.md)，并对[大不列颠](Great Britain.md)禁用“大曼彻斯特”这一名称。
2. ↑ 不包括[斯科讷](https://vic3.paradoxwikis.com/Scania)、[扬马延](Jan Mayen.md)、[密歇根](Michigan.md)、[康沃尔](https://vic3.paradoxwikis.com/Cornwall)、[北卡罗来纳](https://vic3.paradoxwikis.com/North_Carolina)、[南卡罗来纳](https://vic3.paradoxwikis.com/South_Carolina)、[卡罗来纳](Carolina.md)、[佐治亚（GRG）](https://vic3.paradoxwikis.com/Georgia_(GRG)和[佛罗里达](https://vic3.paradoxwikis.com/Florida)。
3. ↑ 关于机制影响的更多信息，请参阅[人口合并 defines](Defines.md)

Victoria 3
返回顶部
| 游戏 | [成就](Achievements.md) • [特性](Victoria 3.md) • 游戏规则 |
|---|---|

| 指南 | [新手指南](Beginner's guide.md) • [键盘快捷键](Keyboard shortcuts.md) • [地图模式](Map modes.md) • [教学视频](Tutorial videos.md) • [用户界面](User interface.md) • [游戏内百科](Vickypedia.md) |
|---|---|

| 开发 | [开发者日志](Developer diaries.md) • [可下载内容](Downloadable content.md) • [补丁](Patches.md) |
|---|---|

| 社区 | [彩蛋](Easter eggs.md) • [术语](Jargon.md) • [模组制作](Modding.md) |
|---|---|