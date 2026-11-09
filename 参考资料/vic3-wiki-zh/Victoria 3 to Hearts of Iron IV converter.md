---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Victoria 3 to Hearts of Iron IV converter
source: https://vic3.paradoxwikis.com/Victoria_3_to_Hearts_of_Iron_IV_converter
pageid: 7391
categories: [Mods]
fetched: 2026-10-27
---
游戏模组
：维多利亚3 转 钢铁雄心4 转换器（Victoria 3 to Hearts of Iron IV converter）
维多利亚3 转 钢铁雄心4 转换器（Victoria 3 to Hearts of Iron IV converter）
---

类型
工具
---

作者
Idhrendur
---

状态
兼容 Vic3 1.10-1.11 与 HoI4 1.16
---

论坛
Paradox Plaza 帖子
维多利亚3 转 钢铁雄心4 转换器（Victoria 3 to Hearts of Iron IV converter）
---

类型
工具
---

作者
Idhrendur
---

状态
兼容 Vic3 1.10-1.11 与 HoI4 1.16
---

论坛
Paradox Plaza 帖子
Vic3 转 HoI4 转换器是一个[工具](https://vic3.paradoxwikis.com/Mods)，它可以读取一份维多利亚3的存档并据此生成一个 HoI4 剧本。它可以从[这个论坛帖子](https://forum.paradoxplaza.com/forum/index.php?threads/1475076)下载。它兼容其他转换器的输出，使玩家能够从[Imperator](https://imperator.paradoxwikis.com/)一路玩到[HoI4](http://hoi4.paradoxwikis.com/)，进行一场连续的*超级战役*（megacampaign）。

本项目是[Vic2 转 HoI4 转换器项目](http://hoi4.paradoxwikis.com/Victoria_2_to_Hearts_of_Iron_IV_converter)的延续。

## 版本

### 近期版本与更新日志

- 0.8 - [Halsey](https://forum.paradoxplaza.com/forum/index.php?posts/31203633)
- 0.7 - [de Gaulle](https://forum.paradoxplaza.com/forum/index.php?posts/30818490)
- 0.6 - [Fioravanzo](https://forum.paradoxplaza.com/forum/index.php?posts/30081735)
- 0.5 - [Eisenhower](https://forum.paradoxplaza.com/forum/index.php?posts/29884682)
- 0.4 - [Doorman](https://forum.paradoxplaza.com/forum/index.php?posts/29492477)
- 0.3 - [Chen](https://forum.paradoxplaza.com/forum/index.php?posts/29285130)
- 0.2 - [Blamey](https://forum.paradoxplaza.com/forum/index.php?posts/29165292)
- 0.1 - [Anders](https://forum.paradoxplaza.com/forum/index.php?posts/28891729)

## 功能与转换机制

以下是转换器功能的总体列表及转换机制说明。如需更多信息，欢迎在论坛上提问或直接查看代码。**注意：**转换器包含一个 *configurables/* 文件夹，其中包含它在转换过程中使用的所有规则数据文件。提供这些文件是有原因的——用户可以查看它们并根据特定需求进行修改。请放心大胆地修改它们，使转换结果符合预期目标。

#### 需求

- 维多利亚3，最新版本。DLC 为可选项。
- 钢铁雄心4，最新版本。DLC 为可选项。

#### 输入存档

- 转换器支持压缩存档。
- 支持铁人模式存档。

#### 输出 mod

- 转换器将生成一个钢铁雄心4 的 mod。
- 在 Windows 上使用前端界面时，mod 将被复制到 Hoi4 mod/ 目录。
- 不使用前端界面（手动运行转换器）或在其他操作系统上，mod 将被导出到转换器的 output/ 文件夹，需要用户自行移动。

#### 书签

- 转换后的 mod 支持一个书签：1936。
- 转换日期对应的书签可能相当早，如果从 CK2 开始连续使用多个转换器，可以在 Hoi4 引擎中游玩 769 年开局的游戏——不过除了图个新鲜感之外，这是个糟糕的主意。
- 在早于 1936 年的时间点转换会导致人力水平、工业规模和转换后技术受到惩罚，不推荐这样做。

#### 国家

- 国家以基本方式进行转换。它们保留其名称、颜色和领导人。
- 政府通过确定对各项法律的意识形态支持度来转换，并使用 configurables/ideology_mappings.txt 中的规则将这些支持应用到 HoI4 意识形态上。
- 技术根据 configurables/tech_mappings.txt 进行转换。
- 旗帜通过查找 HoI4 和 blank_mod/gfx/flags/ 中的所有旗帜并应用于与相应 tag 匹配的国家来转换。可以通过编辑 configuratbles/flag_mapper_config.txt 来屏蔽特定旗帜。

#### 州（States）

- 州从 Vic3 的州转换而来，但岛屿及其他不相连的省份可能被拆分为独立的州。荒地会被拆分为单独的州。
- 资源根据 configurables/resources.txt 进行分配。
- 胜利点分配给由 Vic3 定义的数值最高的核心省份。点数由核心省份的类型决定。
- 人力即 Vic3 的人口数。
- 工业按每售出商品价值 175,000 折算一座工厂进行转换。如果某个州的工厂数超过十二座，多余的工厂将被分配给所有者的下一个州，以免超出 HoI4 的上限。
- 州类别将被分配为能够容纳转换后工厂数量的最小类别。

#### 军队

- 军队通过将 Vic3 的部队转换为 HoI4 的营，再使用这些营来填满师模板进行转换。

#### 战争

- 战争会被转换。
- 被占领土不会被转换。

#### 其他 mod

- 本转换器设计为可与 Vic3 mod 配合工作，包括[从 EU4 转换到 Vic3](EU4 To Vic3 Converter.md)的游戏。其他 mod 也可能有效。
- 未来可能支持将转换器的输出与其他 HoI4 mod 结合。但这将是低优先级事项，且目前完全未经测试。

## 常见问题

问：我使用了 mod，转换器还能与之配合工作吗？答：这取决于该 mod 修改了什么。最好的办法就是直接尝试（并告诉我们结果如何）。据我们所知，它与从 EU4 转换而来的游戏配合良好。

问：转换器显示"Saving Configuration: Failed!"，该如何解决？答：禁用你的杀毒软件，或将转换器加入白名单。

## 协助开发

如果你希望协助开发，有很多途径可以参与。以下是需要帮助的方面。

*程序员：*

我们始终需要更多程序员。转换器本体使用 C++ 编写，配套工具也使用 C++。其他转换器则使用 C++、C#、Java 和 Python 编写。

*盯地图专家：*

省份映射总是需要进一步完善。HoI4 省份关联的顺序会影响胜利点等要素的落点，因此如果你能为你熟悉的地区更新省份映射（并把文件发给我），那将很有帮助。

*测试者：*

更早发现 bug 和异常意味着它们能更早被修复。我会尝试在论坛上发布转换器的测试版本，运行这些版本并检查各项内容会很有帮助。如果你有测试方面的专业经验，我确信我们在很多地方还能做得更好。请告诉我们该怎么做！

*Mod 制作者：*

我们始终需要有人帮忙研究游戏机制的工作原理，以及如何做得更好。如果你知道如何 mod HoI4，我们可以借助你的帮助来弄清这些问题。此外，风味事件、决议等内容也永远有扩充空间。

*所有人：*

我们始终欢迎在论坛帖子里就转换方式展开更多讨论。你的鼓励比你所知的更有帮助。