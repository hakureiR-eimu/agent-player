---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Map modding
source: https://vic3.paradoxwikis.com/Map_modding
pageid: 6128
categories: [Potentially_outdated, Unknown_version, Under_construction, Modding]
fetched: 2026-10-27
---
请协助核实或更新本文中较旧的章节。至少部分章节最后核实时对应的版本是 [version](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning) unknown。

|  | **本文正在进行大规模重构。** 欢迎协助其翻新。 |
|---|---|

在《维多利亚3》中，可以通过修改游戏文件或使用地图编辑器来修改游戏地图。这包括编辑陆地、海洋、河流、省份（province）和州（state）。关于州的模组制作，请参阅 [state](State modding.md) modding。

本文不包括编辑人口、各国家拥有哪些州、建筑或国家定义的内容，请参阅 [历史模组制作](History modding.md)。

## 入门

打开地图编辑器的方法：

- 前往 Steam 库，右键点击 Victoria 3 并打开属性。
- 在“常规”选项卡下的“启动选项”部分，在指定字段中输入 `-map editor`。
- 直接打开 Victoria 3 即可。在尝试使用你自己创建的任何内容之前，请先用一个功能正常的地图进行此操作。之后你可以在编辑器内导入新资源。

或者，你也可以在 debug 模式下开始一场战役，并使用 "map_editor" 这个 [控制台命令](Console commands.md)。

#### 创建桌面快捷方式

如果你打算大量使用地图编辑器，或者需要在地图编辑器和游戏之间频繁切换，那么拥有一个专用的桌面快捷方式会很方便。要创建专用桌面快捷方式，请按照以下步骤操作，或参考 [The Iron Workshop](https://www.youtube.com/watch?v=5kmDfxSb8U0) 制作的 YouTube 视频：

- 前往 Steam 库，右键点击 Victoria 3 并打开属性。
- 在“已安装文件”选项卡下，选择“浏览……”。
- 然后选择 binaries 文件夹，该文件夹中应该有一个名为 "victoria3" 的应用程序。
- 右键点击该应用程序，（如果你使用 Windows 11）选择“显示更多选项”，然后选择“发送到桌面”。
- 现在你的桌面上应该有一个名为 victoria3 - Shortcut 的快捷方式（不要与默认安装的 Victoria 3 快捷方式混淆）。
- 右键点击该快捷方式，（如果你使用 Windows 11）选择“显示更多选项”，再选择“属性”。
- 在属性中应该有“目标”一项（例如 `"C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\binaries\victoria3.exe"`）。
- 在 (.exe") 之后添加：`-map editor`
- 点击“确定”，这会关闭该程序。要验证是否生效，双击该应用程序即可。
- 请注意，地图编辑器会打开在 Victoria 3 启动器中所选并启用的 mod 的地图文件。

## 高度图（Heightmap）

高度图是每张地图的基础，它定义了非纸质地图的整体形状。高度图以灰度图像表示，其中黑色是可能的最低海拔，白色是可能的最高海拔。可以在地图编辑器内修改高度图，也可以通过修改 png 文件来实现。

### 使用外部资源创建高度图

最小高度图——经 Mekbots 授权创建并发布。
对于真实世界地点，NASA 通过“蓝色弹珠”（Blue Marble）项目的地形部分向公众提供详细的高度图。

虚构的高度图通常使用多种软件组合来创建，一般是 Photoshop 或 GIMP 之类的图像编辑器，加上 World Machine 或 Gaea 之类的地形生成软件。

在 Steam 创意工坊的 [Total Conversion Sandbox](https://steamcommunity.com/sharedfiles/filedetails/?id=2893763054) mod 中可以找到一个最小高度图。如果你使用这个最小高度图，我建议将 Total Conversion Sandbox 的内容复制到你新 mod 的文件夹中，并按照本指南帮助你设置 mod。

### 原版游戏的高度图

高度图位于 /Victoria 3/game/map_data/heightmap.png，必须保存为 16 位灰度图像（在 Photoshop 中：图像：模式：灰度 + 16 位/通道）。

除了 "heightmap.png"，还有两个重要的**自动生成的**高度图文件："indirection_heightmap.png" 和 "packed_heightmap.png"。它们会在 Vic3 地图编辑器中重新打包并保存高度图时生成。

### 常见问题

- 有时，地图编辑器中的新高度图会出现随机的空洞，或者地图的某些部分会显示为海洋而非陆地。要修复此问题，在工具中选择 Heightmap Resolution（*快捷键*：5），选中受影响的图块并点击 Resoution +（*快捷键*：小键盘 +）。

## Victoria 3 地图编辑器概览

TODO

## 地图绘制

TODO

### 枢纽与定位器（Hubs and Locators）

在地图编辑器中，枢纽和定位器以球体网格表示，枢纽用品红/粉色球体表示，定位器用橙色球体表示。枢纽是样条线之间的连接点或节点，它们影响陆军和海军的移动、贸易以及某些州的邻接关系，一般来说它们比视觉定位器更容易导致崩溃或其他问题。定位器代表城市，但也可以是岩石、盘旋的鸟或其他地图物体之类的兴趣点。城市定位器尤其只是枢纽的视觉表现，不具有任何功能。

打开地图编辑器时通常不会显示定位器，要在地图物体编辑器中看到定位器，请在 Mask Painter 工具中开启 `Auto refresh` 和 `Draw city spheres`。

枢纽有两种类型：类型 0 和类型 1。类型 0 枢纽用于陆地网络，类型 1 枢纽用于海军网络。无法直接为枢纽选择类型，但通过选择 `Create a strip between two anchors`，然后选择 `Spline Type` 工具并选择 dirtroad 或 railroad，再回到 `Create new anchors` 工具放置一个新枢纽，你将创建一个类型 0 枢纽。如果改为选择 naval_route 或 coastal_naval_route，则会创建类型 1 枢纽。默认选择的是 dirtroad，因此在启动地图编辑器时放置的所有枢纽都是类型 0，除非更改了样条线类型。

## 纸质地图

TODO

## 河流绘制

河流图是定义河流的文件，游戏引擎用它来在你的地图上放置、绘制和渲染河流。河流图对错误极其敏感。根据错误的不同，制作不当的河流图要么导致崩溃，要么使河流图无法渲染。

目前似乎无法使用地图编辑器创建或修改河流图，而必须使用 GIMP 等外部程序来创建或修改。

### 导出河流图

河流图文件必须导出为带有特定调色板的 8 位索引 RGB 图像，并且必须与省份图具有相同的尺寸。为确保使用正确的调色板并以正确的格式保存文件，建议使用 GIMP，以游戏原版河流图（位于 /Victoria 3/game/map_data/rivers.png）为基础来导出河流图，必要时更改图像尺寸。以这种方式操作时，导出的图像就会是正确的格式，无需更改任何设置。

### 河流图颜色

只有特定的颜色可以在河流图中使用。每种颜色都有特定含义，游戏引擎利用它们在你的地图上绘制河流。

#### 参考颜色

这些颜色是为绘制地图的人提供参考的。据目前所知，游戏引擎在创建或渲染河流时并不使用它们。

- #ffffff（白色）表示陆地
- #7a7a7a（灰色）表示水域

#### 渐变颜色

这 13 种颜色定义河流的宽度和路径。它们是从浅蓝到深蓝，再从深绿到浅绿的渐变，浅蓝色对应最小河宽，浅绿色对应最大河宽。

游戏引擎根据一个单独文件（位于 /Victoria 3/game/common/defines/jomini/rivers.txt）中定义的范围，决定为每个渐变颜色分配什么河宽并绘制到你的地图上。引擎将 TH_MIN 为最小宽度、TH_MAX 为最大宽度的范围平均分配给这 13 种渐变颜色。未经修改时，该范围为最小宽度 1.25 到最大宽度 2.75，但只需更改该 defines 文件中 TH_MIN 和 TH_MAX 的值即可修改。

从最宽到最窄，颜色依次为：

- #00d400 为最大河宽
- #00a300
- #008100
- #005800
- #030068
- #08009b
- #0e00cf
- #1100e9
- #1500ff
- #005fff
- #0096ff
- #00cbff

- #00e5ff 为最小河宽

#### 特殊颜色

这些颜色用于开始、合并或分出河流系统。其用法和摆放位置参见下一节。

- #00ff00（纯绿）表示河流系统的源头
- #ff0000（纯红）表示支流汇入干流
- #ffc000（纯黄）表示河流分流

### 正确的河流构造

无效河流构造示例与正确构造示例
每个河流系统（干流、支流和分流）只能有一个源头。这个源头必须位于干流的起点。如果把它放在支流的起点，将导致整个河流系统无法渲染。支流用一个纯红像素与干流连接。该像素不能分割干流，而应正交相邻地放置在干流旁边。分流用一个纯黄像素从干流分离。该像素同样不能分割干流，而应正交相邻地放置在干流旁边。总之，每段河流应只在一端带有三种特殊颜色之一，另一端不带任何特殊颜色；河流从绿色和黄色像素处流出，流向红色像素。

河流系统的所有像素正交相邻的其他像素不得超过两个。如果河流使用了对角相邻的像素，或者某个像素与 3 个或更多其他像素正交相邻，该河流系统将无法渲染。

## 湖泊

创建湖泊有两种方式：将湖泊省份的高度降低到海平面以下，或者使用湖泊贴花。使用湖泊贴花时，请务必更新 /gfx/map/map_object_data/lakes.txt，加入 `disable_transform_packing=yes` 这一行。没有这一行，湖泊贴花不会在游戏中显示。注意，地图编辑器会自动删除这一行，因此在使用地图编辑器后必须重新添加。

湖泊省份还需要添加到 /map_data/default.map 的 `lakes` 块中。

## 省份绘制

手工进行省份绘制非常繁琐，不推荐这样做。有多种可用工具可以为你完成省份绘制（可通过 Google 或 Vic3 modding co-op 的 Discord 找到），你也可以轻松编写脚本（手工或用 AI）通过泰森多边形（Voronoi cells）或类似算法来创建省份。

如果你要自己编写脚本或手工绘制，有几点需要注意：

- provinces.png 是个难缠的东西。很容易不小心保存为错误格式，使数小时的辛勤工作付诸东流。请务必备份。
- 每个省份必须有一个独一无二的颜色。每个省份的 ID 就是其颜色的十六进制代码，例如 "xffffff"。
- 省份可以是不连续的。原版中的小岛常常与附近的小岛共享一个省份。
- 省份不能太大。海洋省份经常出现这个问题。你不能用一个巨大的海洋省份囊括你 mod 中所有的海洋。请参考原版来确定合适的省份大小。
- 海洋省份应该较大，因为每个海洋州只包含一个海洋省份。
- 湖泊省份不添加到任何州。
- 海洋省份和湖泊省份应分别添加到 /map_data/default.map 的 `sea_starts` 块和 `lakes` 块中。
- province_terrains.txt 不需要填写游戏也能加载。可以通过控制台的 `terrain.regenerate` 命令自动生成。使用该命令后，在 Documents\Paradox Interactive\Victoria 3\generated 中查看生成的文件。

## 州的模组制作

另请参阅：
州模组制作指南
要向游戏中添加一个州区域（state region）：

- 创建*州区域*，编辑或仿照以下原版文件：
  - /Victoria 3/game/map_data/state_regions/00_west_europe.txt
    - 州区域的 ID 不需要连续。例如，如果你用原本属于 ID 为 180 的原版州区域的省份创建一个新的州区域，可以将新州区域的 ID 设为 10180。
  - /Victoria 3/game/localization/english/map/states_l_english.yml
  - /Victoria 3/game/localization/english/hub_names_l_english.yml
  - /Victoria 3/game/common/strategic_regions/african_strategic_regions.txt
  - /Victoria 3/game/common/scripted_triggers/00_geography_triggers.txt
- 在新的州区域中创建一个*州*，编辑或仿照以下原版文件：
  - /Victoria 3/game/common/history/states/00_west_europe.txt
  - /Victoria 3/game/common/history/pops/00_west_europe.txt
- 以 debug 模式启动游戏。错误日志会提示 "map object locator" 不完整。这意味着你的 mod 中没有与你在 /Victoria 3/game/map_data/state_regions/00_west_europe.txt 中创建的五个枢纽相关联的位置（XY 坐标对）。要修复此问题，前往 `Documents\Victoria 3\generated`，将其中五个自动生成的位置文件复制到你 mod 的 /Victoria 3/game/gfx/map/map_object_data 中，然后关闭游戏。
- 再次以 debug 模式启动游戏。错误日志会提示 "Cannot connect state adjacency connection, no connection node found in state"。这意味着，虽然你已经为新区区域中的枢纽创建了关联位置，但这些位置尚未作为“锚点（anchor）”正确整合到游戏地图中。要修复此问题，打开地图编辑器（如上文所述），切换到 "Spline Network Strip Tool" 选项卡（位于窗口左侧，形似蜘蛛网），选中新的州区域，然后点击 "Automatically Place All Hub Anchors" 按钮（位于州区域列表上方，形似两个箭头指向两个圆圈）。这会在上一步自动生成的每个位置上创建一个紫色线框球体。现在，点击 "Save As" 按钮（位于窗口左上角，形似软盘上的铅笔）。在弹出的对话框中，取消勾选所有复选框，唯独保留标记为 "Spline Network" 的那一个。在 `"gfx/map/spline_network/spline_network.splnet"` 旁边的下拉列表中，你应该能够选择与你 mod 对应的文件夹。点击 "OK" 按钮将对样条线网络的修改保存，然后关闭游戏。
- 再次以 debug 模式启动游戏。错误日志会提示 "Strip between locators 1234 and 5678 connects state region to a non-adjacent one"，或 "State has nodes but they are not connected to anything"，或类似信息。这意味着你的锚点已正确整合到地图中，但尚未通过“条带（strip）”（军事单位的行军路径和图形效果）与地图上的其他任何锚点正确连接。要修复此问题，打开地图编辑器并切换到 "Spline Network Strip Tool" 选项卡。使用 "Select and Modify Anchors" 工具将锚点微调到理想位置；使用 "Select and Modify Strips" 工具删除有问题的条带；配合 "Spline Type" 下拉菜单，使用 "Create a Strip Between Two Anchors" 工具创建新条带。按照上一步的说明保存样条线网络，然后关闭游戏。（这一步可能需要反复尝试。请利用错误日志并参考原版州区域，弄清游戏要求你做什么。）
- 再一次以 debug 模式启动游戏。如果你新的州区域是沿海的，错误日志会提示 "Port node 1234 in state My New State Region has no harbor node to connect to"。这意味着你需要添加一个港口节点（harbor node）——即放置在水域州区域上的锚点，它使行军路径能够从陆地锚点（地图编辑器中称为“类型 0”）转移到水域锚点（“类型 1”）。要修复此问题：
  - 打开地图编辑器。
  - 切换到 "Spline Network Strip Tool" 选项卡。
  - 切换到 "Create New Anchors" 工具。
  - 将 "Spline Type" 下拉菜单更改为 "coastal_naval_route"。
  - 在你新州区域的港口（陆地、类型 0）锚点附近的地图上点击，创建一个水域（类型 1）锚点作为港口。移动该港口锚点使其与港口锚点重叠。在屏幕右侧的 "Spline Anchors" 菜单中，为港口锚点分配与城市锚点相同的索引（*而不是*与港口锚点相同的索引）。
  - 将枢纽 ID 重命名为州 ID 加上 "00" 后缀。如果你不知道州 ID，请选中港口枢纽。港口枢纽的命名格式应为 "XYZ03"，其中 "XYZ" 是州 ID。例如，港口枢纽 ID 为 "8903" 时，对应的沿海海军路线枢纽为 "8900"。
  - 切换到 "Select and Modify Strips" 工具。
  - 从你刚刚创建的锚点向你的新州区域所毗邻的水域州区域中心的锚点，绘制一条 "coastal_naval_route" 条带。
## 样条（Spline）模组制作

每个陆地州都必须为其每个城市定位器（city locator）设置一个样条枢纽（spline hub）——城市（00）、农场（01）、矿场（02）、港口（03，仅沿海州）和林地（04）。如果该州是沿海州，则还必须有一个额外的类型 1 枢纽。创建这些枢纽的步骤在上文的“州（State）模组制作”部分中已有说明。目前只有 "railroad" 和 "dirtroad" 两种样条类型可用。你的连接大部分应该是铁路（railroad）连接，泥土道路（dirtroad）连接则更多作为次要连接，或用于连接那些你不希望铺设铁路的难以到达的地点。

每个可通行的海洋州都必须有一个 ID 以 "00" 为后缀的类型 1 枢纽，并通过 "naval_route" 样条类型彼此连接。

#### 地图编辑器错误：

- 你无法编辑一个已有连接的枢纽的 ID。这样做会导致编辑器崩溃。你必须在创建枢纽后立即编辑其 ID。
- 北太平洋的 navmesh 存在一个错误。你无法在该区域创建跨越世界边界的样条。
- 如果你的高度图（heightmap）过于精细，可能会引发地图编辑器的问题。要解决此问题，请备份高度图，并将你工作用的高度图裁剪为 8 位（0, 20）。

### 如何为运河定义样条

- 注 1：在启动地图编辑器时，尚不清楚如何引用 3D 模型运河。
- 注 2：首先，请务必为你的 MOD 创建备份。这是因为在完成样条连接的编辑后，你只需要保存特定的文件。

- 原则上，样条只能连接相邻的地点。然而，运河必须穿过陆地。这看起来矛盾吗？解决办法就是避开这个矛盾。
- 让我们消除计划连接运河的区域中的陆地。也就是把它沉入海中。

1. 启用 “Map Content Editor"。
2. 选择你计划连接运河的一个海洋州。
3. 请用你刚选择的海洋州的颜色，填充阻挡另一个你计划连接的海洋州的陆地。Map Content Editor（之前）Map Content Editor（之后）
4. 不再有陆地阻挡你的路径了吗？如果是，请按下 “Apply Changes” 退出 “Map Content Editor” 模式。
5. 接下来，启动 “Spline Network Strip Tool"。
6. 选择 “Create a strip between two anchors"。
7. 打开 “Spline Type” 下拉菜单并启用 “naval_route”。
8. 连接这两个海洋州。（详细说明从略。）Spline Network Strip Tool（之前）Spline Network Strip Tool（之后）
  1. 你此时添加的样条是否显示了 “Invalid Strip”？在这种情况下，是地图编辑器误认为这两个海洋州不相邻。Spline Network Strip Tool（错误：Invalid Strip）
  2. 让我们做一些额外的处理。启动 “Heightmap Painter"。
  3. 找到 “Up” 和 “Dn” 按钮。如果找到了，请按下 "Dn"。
  4. 请将阻挡运河的陆地淹没。Heightmap Painter（之前）Heightmap Painter（之后）
  5. 请再次使用 “Spline Network Strip Tool” *(5)* 尝试。如果无效，请再次使用 “Map Content Editor” *(1)* 尝试。
9. 启动 “Spline Network Adjustment Tool”，并调整所添加样条的细节。用 Spline Network Adjustment Tool 调整之后
10. 保存 MOD。保存 MOD。点击 “Save as"，并**只**保存 gfx\map\spline_network\spline_network.splnet。

- 这里，我只说明与运河相关的样条定义方法。其他调整将省略。

### 创建新的样条类型

此部分留白，由 Realms of Exether 与 Anbennar 团队来补充说明。

## 参考
模组制作
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [Variables](Variable.md) |
|---|---|

| 脚本内容 | [Decisions](Decision modding.md) • [Events](Event modding.md) • [History](History modding.md) • [Journal](Journal modding.md) • [Modifiers](Modifier modding.md) • Objectives • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [Buildings](Building modding.md) • [Characters](Character modding.md) • Concepts • [Countries](Country modding.md) • [Culture](Culture modding.md) • [Decrees](Decree modding.md) • [Diplomacy](Diplomacy modding.md) • [Goods](Goods modding.md) • [Institutions](Institution modding.md) • [Interest groups](Interest group modding.md) • [Laws](Law modding.md) • Parties • [Pops](Pop modding.md) • [Power blocs](Power bloc modding.md) • [Religion](Religion modding.md) • Subject types • [Technology](Technology modding.md) • [Treaties](Treaty modding.md) • [War goals](War goal modding.md) |
|---|---|

| 地图 | Map • [Geographic regions](Geographic region modding.md) • [States](State modding.md) |
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