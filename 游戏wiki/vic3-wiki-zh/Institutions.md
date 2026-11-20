---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Institutions
source: https://vic3.paradoxwikis.com/Institutions
pageid: 1635
categories: [1.13, Politics]
fetched: 2026-10-27
---
本文已针对当前游戏[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

机构摘要标签页显示机构的等级、每级成本以及总成本。
机构代表特定的政府服务、办事处或部门。这包括学校和工作场所安全监管等，也包括殖民事务、警察和济贫院等。

机构由[法律](Laws.md)设立或废除。每个机构的成本和效果在 1 级到 5 级之间各不相同。当一项法律初次设立某个机构时，该机构自动设为 1 级，且只能通过废除该法律来移除。机构的等级会同时乘以其效果和[行政力](https://vic3.paradoxwikis.com/Bureaucracy)成本；因此一个 3 级机构的效果和成本是一个 1 级机构的三倍。虽然[利益集团](https://vic3.paradoxwikis.com/Interest_groups)可能对设立机构的法律持某种立场，但它们对机构本身的规模从不发表意见。法律还可能为机构增加额外效果，或提高其可能的最大投资等级。

机构只对已整合的州生效并产生行政力成本。

## 机构效果

共有七种机构，其中大多数都有基础效果。所有机构都需要一项法律来启用；大多数启用机构的法律还会为每级增加额外效果，而有些启用机构的法律还具有与该机构相关的其他效果，例如提高该机构的最大等级或增加一项相关的全国性效果。

例如，内政机构的基础效果是降低革命与分裂的推进速度。如果当前法律是国民卫队，那么每级还会增加征兵数量并降低[政治运动](Political movement.md)的激进度；而如果法律是自由保障，每级则改为减少来自运动的激进派并增加忠诚派。

某些[强权集团](Power bloc.md)原则也会修改机构效果。

| 机构 | 基础修正 | 启用法律类别 | 额外等级 | 描述 |
|---|---|---|---|---|
| 殖民事务 | **+10%** 殖民增长生成 | [殖民](Economy laws.md) | [Colonization](Society technology.md)（2）、[Quinine](Society technology.md)、[Civilizing Mission](Society technology.md)、[Malaria Prevention](Society technology.md) | 负责管理海外殖民领地的部门。 |
| 教育 | — | [教育制度](Economy laws.md) | 理性主义、经验主义、辩证法 儿童权利法律（1-2） | 国家的学校系统，确保人口识字率的增长。 |
| 卫生系统 | — | [卫生系统](Economy laws.md) | [Medical Degrees](Society technology.md)、[Pharmaceuticals](Society technology.md)、[Quinine](Society technology.md)、[Malaria Prevention](Society technology.md)、[Antibiotics](Society technology.md) | 遏制疾病的传播。 |
| 内政 | **−10%** 革命/分裂推进速度 | [国内安全](Power structure laws.md) | [Centralization](Society technology.md)、[Central Archives](Society technology.md)、[Identification Documents](Society technology.md)、[Central Planning](Society technology.md)、[Mass Surveillance](Society technology.md) | 负责阻止公民叛乱。 |
| 执法 | **−10%** 州因动荡受到的惩罚 | [治安](Economy laws.md) | 官僚制（2）、执法 治安法律（2） | 执行国家法律的全国警察力量。 |
| 社会保障 | +20% 福利支出 +2% 粮食安全 | [福利](Human rights laws.md) | [Democracy](Society technology.md)（2）、[Egalitarianism](Society technology.md)、[Human Rights](Society technology.md)、[Feminism](Society technology.md) | 为年老或体弱者提供的安全网。 |
| 工作场所安全办公室 | **−20%** 危险工作条件 | [劳工权利](Human rights laws.md) | [Labor Movement](Society technology.md)（3）、[Socialism](Society technology.md)（2） | 监督劳动法律得到遵守的部门。 |

## 机构等级

当一个机构被启用时，无论[行政力](https://vic3.paradoxwikis.com/Bureaucracy)是否充足，其第一级都会被自动添加。机构的效果和成本会乘以其当前等级，因此一个 5 级机构的效果和成本是一个 1 级机构的五倍。每个机构都有自己的最大等级，取决于已颁布的法律和已研究的技术。提升机构等级（从而提升其效果）需要同时满足机构最大等级足够以及可用行政力充足这两个条件。

提升或降低机构等级每级需要基础时间一年。在实施新等级期间，行政力成本会在这一年中按比例变化，但预期的效果只在新等级完全实施后才会生效。如果在提升机构等级期间可用行政力降至 0 以下，该机构会暂停升级，直到行政力重新变为正值。

已整合州中每 10 万人口，机构每级成本为基础值 1 行政力，最低成本为 10 行政力，即已整合州人口少于 100 万时。法律民选官僚将所有机构的行政力成本降低 **−15%**。

某些强权集团原则会修改某些机构的变更时间和成本。

## 策略

### 殖民事务

边疆殖民是一部严格劣于殖民安置的法律。对殖民地点和方式的限制相当严格。选择它的唯一理由是乡村民众不反对它，反而支持它，因此通常不会遭到实际反对。

殖民剥削降低工资和工厂吞吐量，以换取殖民地中种植园和资源吞吐量的提高。由于在殖民地发展任何工业本来就不太可能有利可图，这基本上可以算作一项吞吐量加成。

### 教育

5 级私立学校和 3 级公立学校总行政力成本相同
哪种教育制度最好在很大程度上取决于[生活水平](Standard of living.md)。教会学校严格劣于另外两种。这一点在游戏后期尤其明显，因为它无法升到 3 级以上。不过它也有其用武之地，因为它是游戏早期最容易实施的，这既是因为游戏早期典型的政治局面——虔信派强大而工会、知识分子和实业家弱小甚至不存在——也是因为在实行国教的国家它是唯一选择，还因为它是被更早的科技解锁的。

私立学校和公立学校都可能是最佳选择，取决于具体情况。私立学校每级每点财富提供 **0.5%** 的[教育普及](https://vic3.paradoxwikis.com/Education_access)，而公立学校每级为所有人提供固定的 **12.5%**。这意味着对于[生活水平](Standard of living.md)低于 25 的 POP，公立学校每级提供的教育更多；在 25 时二者相等；高于 25 时私立学校提供得更多。

然而，在平均生活水平低于 25 时，私立学校仍可能更优，因为其实施成本便宜 **40%**，因此在行政力紧张且当前科技允许再升一级的情况下，可以用同样的行政力维持更高的等级。3 级私立学校比 2 级公立学校便宜 **10%**，4 级私立学校比 3 级公立学校便宜 **20%**，5 级私立学校比 4 级公立学校便宜 **25%**。事实上，5 级私立学校和 3 级公立学校消耗的行政力完全相同。

以相同成本实施 5 级私立学校与 3 级公立学校相比，对生活水平在 16 到 24 之间的 POP 更好，对生活水平为 15 的 POP 相当，对生活水平低于 15 的 POP 更差。

### 工作场所安全

监管机构与工人保护之间的唯一区别是后者会提高最低工资。不应在无意之中提高最低工资。此外，对于走社会主义道路的国家，《我们赢得整个世界》事件中的一个选项会立即颁布监管机构，因此可以把精力放在其他法律上。

## 参考

1. 更新机构修正请参见参考文件 /Victoria 3/game/common/institutions/00_institutions.txt
2. 更新机构风味文本请参见参考文件 /Victoria 3/game/localization/english/institutions_l_english.yml:

游戏概念
返回顶部
| 人口 | [人口](Pops.md) • [接纳度](Acceptance.md) • [文化](Culture.md) • [迁移](Migration.md) • [需求](Needs.md) • [职业](Profession.md) • [宗教](Religion.md) • [生活水平](Standard of living.md) |
|---|---|

| 政府 | [政府](Government.md) • [能力](Capacity.md) • [人物](Character.md) • [法令](Decrees.md) • 机构 • [法律](Laws.md) • [技术](Technology.md) |
|---|---|

| 政治 | [选举](Elections.md) • [意识形态](Ideology.md) • [利益集团](Interest group.md) • [政治游说](Political lobby.md) • [政治运动](Political movement.md) • [政党](Political party.md) • [革命](https://vic3.paradoxwikis.com/Revolution) |
|---|---|

| 经济 | [建筑](Building.md) • [商品](Goods.md) • [收成状况](Harvest condition.md) • [基础设施](Infrastructure.md) • [市场](Market.md) • [生产方式](https://vic3.paradoxwikis.com/Production_methods) • [州](State.md) • [国库](Treasury.md) |
|---|---|

| 外交 | [外交](Diplomacy.md) • [外交行动](https://vic3.paradoxwikis.com/Diplomatic_action) • [外交博弈](Diplomatic play.md) • [强权集团](Power bloc.md) • [等级](Rank.md) • [附属国](Subject.md) • [条约](Treaty.md) |
|---|---|

| 战争 | [战争](Warfare overview.md) • [陆战](Land warfare.md) • [海战](Naval warfare.md) • [战争目标](https://vic3.paradoxwikis.com/Wargoal) • [征兵](https://vic3.paradoxwikis.com/Conscription) |
|---|---|

| 其他 | [国家](Countries.md) • [决策](Decision.md) • [事件](Events.md) • [日志](Journal.md) • [目标](Objective.md) • [Vickypedia](Vickypedia.md) |
|---|---|