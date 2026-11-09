---
translated: 2026-10-27
translator: machine (glm-5.3)
title: Flag modding
source: https://vic3.paradoxwikis.com/Flag_modding
pageid: 3711
categories: [1.13, Modding]
fetched: 2026-10-27
---
本文已针对游戏的当前[版本](https://vic3.paradoxwikis.com/Victoria_3_Wiki:Versioning)（1.13）进行核实。

《维多利亚3》中的[国家国旗](List of flags.md)由[trigger](https://vic3.paradoxwikis.com/Triggers)（游戏内触发条件脚本）从脚本编写的*纹章（coats of arms）*中选取，纹章由一个或多个图形元素构成。

## 国旗定义

国家国旗的选取脚本位于 /common/flag_definitions/。每个拥有一面或多面已定义国旗的国家，应以其 TAG 作为一个块列出，每个可能的国旗各有一个 `flag_definition` 块。以下示例取自 /Victoria 3/game/common/flag_definitions/00_flag_definitions.txt。

```
# FLAG_DEFINITION_LIST = {        # countries search for a list with the same name as their tag, the DEFAULT list is always included, if no flag definition is applicable for a country then its tag is used a COA_KEY
#     includes = ANOTHER_LIST        # includes another list in this list, can be repeated
# 
#     flag_definition = {            # the flag definitions that make up this list, can be repeated
#         coa = [list] COA_KEY    # main flag, optional list keyword denotes a coa template
#         allow_overlord_canton = yes                # default no
#         coa_with_overlord_canton = <[list] coa>    # flag where a canton can be placed, optional list keyword same as above, defaults to coa
#         overlord_canton_offset = { x y }        # canton placement offset, default { 0 0 }
#         overlord_canton_scale = { x y }            # canton placement scale, default { 0.5 0.5 }
#         subject_canton = [list] COA_KEY    # canton applied to subjects by this country, optional list keyword same as above
# 
#         priority = value        # valid flag definition with the highest priority applies
#         trigger = {}            # a trigger that determines if this flag definition is valid, see below for scope
#       allow_revolutionary_indicator = no      # Default = yes. If yes, a temporary revolutionary indicator will appear while the country is revolutionary
#       revolutionary_canton = [list] COA_KEY   # Optional. Default = default_revolutionary_canton. Defines which flag should be used as canton while this country is revolutionary
#     }
# }
```

以下是原版游戏文件中的示例，并附有注释说明。

```
ALD = { # Algeria
    flag_definition = {
        coa = ALD
        subject_canton = ALD                    #If the game rule for modifying subject flags is on, this COA is added to the canton of this country's subjects, it does not need to match the main flag
        allow_overlord_canton = yes                #If the game rule for modifying subject flags is on, can another country's canton be added to this flag set
        coa_with_overlord_canton = ALD_subject    #If the game rule for modifying subject flags is on, alternate COA for adding the overlords canton, e.g. to move central emblems to one side
        priority = 1                            #Highest, i.e. largest priority definition which passes its triggers is used
    }
    flag_definition = {
        coa = ALD_republic
        subject_canton = ALD_republic
        priority = 10
        trigger = { 
            coa_def_republic_flag_trigger = yes    #Scripted triggers can be used, but note scope rules must still be respected
        }
    }
    flag_definition = {
        coa = ALD_subject_FRA
        priority = 30
        trigger = { 
            coa_def_french_ensign_trigger = yes
        }
    }    
}
```

如果某个国家没有脚本编写的国旗定义列表，游戏会以该国的 TAG 作为关键词查找对应的纹章；若仍找不到，则游戏会基于脚本化的随机元素生成一面国旗。

此外还有一个对所有国家都有效的 `DEFAULT` 块，其中列出的纹章可被任何国家使用，这对动态生成的国家（如革命政权或生成的殖民地附属国）非常有用。

### 修改国旗定义

另见：
Mod 兼容性
国旗定义使用 `INJECT:` 和 `REPLACE:` 关键字，因此向国旗定义中添加新纹章或移除已有纹章都非常简单。

可以通过 `INJECT` 到已有的 tag 块来添加新的国旗定义，新定义会被附加到末尾。例如，以下代码会在上文 ALD 的定义中追加内容：

```
INJECT:ALD = {
    flag_definition = {
        coa = ALD_cool_new_flag
        subject_canton = ALD_republic
        priority = 11 #relative priority is very important for injected flags to be used over base game flags
        trigger = {
            coa_def_republic_flag_trigger = yes
            has_variable = ALD_chose_new_flag
        }
    }
}
```

`REPLACE:` 也可以以同样的方式使用，用于移除已有的定义。

### Trigger 的 scope 规则

国旗定义的 trigger 有三种可能的状态，并有若干可用的已保存 scope（作用域）。

|  | 以下情况的已保存 scope 值： |  |  |
|---|---|---|---|
| scope 术语 | 已存在的国家 | 释放国家 | 成立国家 |
| root | 定义 | 定义 | 定义 |
| target | 国家 | 无 | 无 |
| initiator | 无 | 玩家 | 玩家 |
| actor | 国家 | 玩家 | 玩家 |
| overlord | 国家的直接宗主国（若有） | 玩家 | 玩家的直接宗主国（若有） |

## 纹章

你可以在本 wiki 的
国旗列表
页面找到游戏中的大部分国旗；该页面不包含只有一面已定义国旗的国家。
纹章（Coat of Arms，CoA）就是实际的旗帜图案，在国旗定义文件中被引用。每个 CoA 是一个以命名块形式脚本编写的对象，包含一系列图形元素，即*图案（pattern）*、*彩色徽记（colored emblem）*、*纹理徽记（textured emblem）*和*嵌套纹章（sub）*。CoA 定义在 /common/coat_of_arms/coat_of_arms/ 中。这些元素的固有尺寸通常为 768 × 512 像素，部分为 256×256。除 sub 是对其他 CoA 的引用外，其余均为图像文件，可在 game/gfx/coat_of_arms/colored_emblems、game/gfx/coat_of_arms/patterns 和 game/gfx/coat_of_arms/textured_emblems 中找到。

| …/game/common/coat_of_arms/coat_of_arms/02_countries.txt SWE_union_mark_canton = { pattern = "pattern_solid.tga" color1 = "blue" color2 = "yellow" sub = { parent = "sub_SWE_union_mark" instance = { scale = { @canton_scale_sweden_x @canton_scale_sweden_y } } } colored_emblem = { texture = "ce_cross_sweden.dds" color1 = color2 color2 = color2 } } | ![SWE_union_mark_canton](/images/thumb/7/79/Flag_SWE_union_mark_canton.png/330px-Flag_SWE_union_mark_canton.png) |
|---|---|
| 单独来看，这个 sub CoA 是…/game/common/coat_of_arms/coat_of_arms/01_subs.txt sub_SWE_union_mark = { # herring salad pattern = "pattern_per_saltire.dds" color1 = "red" color2 = "blue" color3 = "yellow" color4 = "white" colored_emblem = { texture = "ce_solid.dds" color1 = color3 color2 = color3 instance = { scale = { 1 @[1/5] } } } colored_emblem = { texture = "ce_solid.dds" color1 = color4 instance = { scale = { @[1/4.5] 1 } } mask = { 1 } } colored_emblem = { texture = "ce_solid.dds" color1 = color2 instance = { scale = { @[1/8] 1 } } mask = { 1 } } } | ![sub_SWE_union_mark](/images/thumb/2/21/Flag_sub_SWE_union_mark.png/330px-Flag_sub_SWE_union_mark.png) |

| …/game/common/coat_of_arms/coat_of_arms/02_countries.txt SCA = { pattern = "pattern_solid.tga" color1 = "red" color2 = "red" colored_emblem = { texture = "ce_bicolor_bottom.dds" color1 = "blue" color2 = "blue" } colored_emblem = { texture = "ce_cross_denmark.dds" color1 = "white" color2 = "white" instance = { scale = { 1.6 1.6 } position = { 0.6 0.5 } } } colored_emblem = { texture = "ce_cross_denmark.dds" color1 = "blue" color2 = "blue" instance = { scale = { 1.4 1.4 } position = { 0.565 0.5 } } } colored_emblem = { texture = "ce_cross_denmark.dds" color1 = "yellow" color2 = "yellow" instance = { scale = { 1.0 1.0 } position = { 0.5 0.5 } } } } | ![SCA](/images/thumb/3/31/Flag_SCA.png/330px-Flag_SCA.png) |
|---|---|

颜色名称定义在 /Victoria 3/game/common/named_colors 中，以 HSV 或十进制 RGB 值的形式定义。

### 图案（Pattern）

每个 CoA 都以一个单独的图案作为基底。图案位于 /Victoria 3/game/gfx/coat_of_arms/patterns。每张图案图像充当一个蒙版：其红色会被替换为 color1，黄色（如果存在）会被替换为 color2，少数图案还有第三种会被替换为 color3 的白色。除了设置国旗的基色之外，图案还可以对徽记或 sub 的元素进行遮罩，使徽记仅在图案与徽记相交的区域显示。

通过 `pattern = "pattern_name"`（pattern_name 包含文件扩展名）将图案添加到 CoA 中。

可以为图案未使用的 `color<#>` 赋予命名颜色，这些颜色可在彩色徽记元素中使用。类似地，也可以将两个不同的 `color<#>` 定义为相同的命名颜色。

前三种颜色还会用于该国的单位制服模型，除非国家定义中已指定单位颜色。

图案始终是纹章的最底层。

### 徽记（Emblem）

徽记是叠加在图案及其他徽记之上的更精细的图案。它们按定义的先后顺序分层，并且彩色徽记先于纹理徽记分层，因此最早定义的徽记会被其余徽记覆盖；若发生重叠，只有最后定义的徽记完全可见，而纹理徽记始终位于彩色徽记之上。徽记有两种类型：彩色徽记和纹理徽记。

彩色徽记与图案类似，徽记图像充当所定义颜色的蒙版。彩色徽记使用蓝色通道表示亮度。默认情况下，一个区域被定义为 color1，加入绿色即定义为 color2，加入红色即定义为 color3。因此，color1 像素的 RGB 值示例为 R0 G0 B128，color2 为 R0 G255 B128，color3 为 R255 G0 B128。在本例中，蓝色值大致处于光谱中段，这使该区域呈现为国旗脚本中所定义的精确颜色；增大蓝色值使其更亮，减小则使其更暗，蓝色值为 0 对应黑色，为 255 对应白色。

为避免透明度产生的瑕疵，国旗的透明区域应具有与相邻不透明区域相同的 RGB 值，相当于把颜色"扩散"到透明区域中。

纹理徽记是现成的图像，按原样添加到 CoA 中。它们适合用于向国旗添加包含超过 3 种不同颜色、或不需要便于重新着色的徽记，例如复杂的印章或纹章图案。

向 CoA 添加徽记的方法是添加一个标明徽记类型（`colored_emblem` 或 `textured_emblem`）的块，然后用 `texture = "emblem_name"` 定义徽记，与图案一样需包含文件扩展名。彩色徽记所需的颜色数量须与徽记图像中使用的数量一致。两类徽记都可以通过包含一个或多个 `instance` 块来进行修改。每个 instance 块会将徽记向国旗添加一次，并可调整其缩放、位置和旋转。

缩放以百分比修改徽记的大小，在 x 轴和 y 轴上独立进行；位置移动徽记，使其中心点相对于国旗左上角定位；旋转则按指定度数顺时针旋转徽记。

徽记按顺序分层，第一个定义的徽记紧位于图案之上，下一个再位于其上，依此类推。

### 嵌套纹章（Sub）

Sub 将另一个 CoA 当作纹理徽记来使用，主要区别在于 CoA 是通过 `parent = "CoA_Name"` 调用的，而且其定义中包含 sub 的 CoA 不能再作为另一个 CoA 的 sub 使用（不允许嵌套或递归）。Sub 仍可使用 `instance`，以复制和/或修改所引入的 CoA。

Sub 同样按顺序分层，但它们始终位于所有徽记之上，即使 sub 定义在徽记之前。

| BIC_republic = { pattern = "pattern_solid.tga" color1 = "white" color2 = "red" color3 = "blue" sub = { parent = "sub_BIC_cypher" instance = { scale = { 0.5 0.5 } } # top left } colored_emblem = { texture = "ce_stripes_10.dds" color1 = color2 color2 = color2 } } | ![BIC_republic](/images/thumb/5/50/Flag_BIC_republic.png/330px-Flag_BIC_republic.png) |
|---|---|

### 覆写纹章

另见：
Mod 兼容性
原版游戏的纹章可以在 mod 文件中定义同名纹章的新版本来覆写，只要该 mod 文件名在 ASCII 排序中位于原版游戏文件之后。例如，在名为 `zz_mod_coats_of_arms.txt` 的文件中定义 `SWE`，就会覆写 `02_countries.txt` 中的原版定义 `SWE`。这样 mod 国旗就能更好地与原版国旗整合，无需修改原版游戏文件。

## 强权集团徽记

另见：
强权集团 Mod 制作
强权集团徽记的脚本编写方式与国旗纹章相同。主要区别在于其宽高比为正方形（1:1），而国旗为长方形（3:2）。

原版游戏的定义如下：

```
template_power_bloc_1 = {
    pattern = "pattern_solid.tga"
    color1 = { 0.0 0.0 0.0 0.0 }

    # If we ever change the order of layers here, remember to also update them
    # in NGraphics::NPowerBlocCoa::PIECE_LAYERS_ORDER.

    colored_emblem = {
        texture = list "power_bloc_shield"
        color1 = list "power_bloc_colors"
        color2 = list "power_bloc_colors"
        instance = { scale = { 0.72 0.72 } position = { 0.49 0.6 } }  # when changing this remember to update NPowerBlocCoa in 00_defines.txt
    }

    textured_emblem = {
        texture = list "power_bloc_top"
        instance = { scale = { 0.7 0.7 } position = { 0.5 0.19 } }  # when changing this remember to update NPowerBlocCoa in 00_defines.txt
    }

    textured_emblem = {
        texture = list "power_bloc_frame"
        instance = { scale = { 0.9 0.9 } position = { 0.5 0.6 } }  # when changing this remember to update NPowerBlocCoa in 00_defines.txt
    }

    colored_emblem = {
        texture = list "power_bloc_center"
        color1 = list "power_bloc_colors"
        instance = { scale = { 0.45 0.45 } position = { 0.49 0.54 } }  # when changing this remember to update NPowerBlocCoa in 00_defines.txt
    }

    textured_emblem = {
        texture = list "power_bloc_side"
        instance = { scale = { 0.65 0.65 } position = { 0.155 0.55 } }  # when changing this remember to update NPowerBlocCoa in 00_defines.txt
    }

    textured_emblem = {
        texture = list "power_bloc_side"
        instance = { scale = { -0.65 0.65 } position = { 0.82 0.55 } }  # when changing this remember to update NPowerBlocCoa in 00_defines.txt
    }
}
```

这些列表定义在 /Victoria 3/game/common/coat_of_arms/template_lists 中。正如注释所述，这些值也在 [defines](Defines.md) 中被引用。

强权集团的*盾面（shield）*（346×346px）和*中心（center）*（220×220px）是与国旗彩色徽记位于同一文件夹的彩色徽记，但文件前缀为 `pb_` 而非 `ce_`。类似地，顶部（346×346px）、边框（432×432px）和侧面（360×360px）是纹理徽记。注意第二个（右侧）侧面是通过反转其 X 缩放系数来实现水平翻转的。

启用了"势力范围（Sphere of Influence）"DLC 的玩家可以从可用元素中自定义其强权集团徽记，而没有该 DLC 的玩家只能使用随机或预设的徽记。

预设强权集团徽记的创建方式是按上述方法脚本编写徽记，然后在 /Victoria 3/game/common/coat_of_arms/template_lists/coa_templates.txt 的随机强权集团徽记列表中为该脚本徽记赋予极高的权重，原版游戏的开局强权集团就是这样处理的。

## 纹章模板

另见：
Category:Generated flags
模板是一种生成"随机化"[1]纹章的方法。它用于生成大多数革命政权和分裂政权的国旗，以及大多数共产主义和无政府主义国旗。
模板在 `template = { }` 中定义，每个模板都有其自身的脚本名称，例如 `template_charge` 或 `template_centered_coa`[2]。这些模板通常使用 /Victoria 3/game/common/coat_of_arms/template_lists 中的列表来随机选取颜色、图案和纹章图案。模板本身则汇总在 /Victoria 3/game/common/coat_of_arms/template_lists/coa_templates.txt 的列表中，供旗帜定义使用。

纹章模板列表可以被赋予脚本名称，以便在旗帜定义中引用。此外还有一个默认列表 `all`，当找不到某个国家有效的旗帜定义时，将作为默认回退使用。

## 脚本术语

下表列出了定义纹章时使用的脚本术语。

| 术语 | 功能 | 示例 | 用于 |  |  |  |
|---|---|---|---|---|---|---|
| 基础 | CE | TE | Sub |  |  |  |
| pattern | 调用一个图案文件 | `pattern = "pattern_solid.tga"` | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| color<#> | 为图案或着色纹章图案定义颜色 引用一个命名颜色，或此前定义的颜色 也可以用 hsv360 格式定义任意颜色[3] | `color1 = "red"` `color1 = color3` `color1 = hsv360{ 180 50 50 }` | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| colored_emblem | 开始一个着色纹章图案块 | `colored_emblem = { … }` | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| textured_emblem | 开始一个纹理纹章图案块 | `textured_emblem = { … }` | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| list | `pattern`、`color` 或 `texture` 的修饰符 引用此类元素的加权列表，而非某个特定元素 | `color1 = list "normal_colors"` `pattern = list "pattern_borders"` `texture = list "charge"` | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| sub | 开始一个子块 | `sub = { … }` | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| texture | 调用一个纹章图案文件 | `texture = "ce_solid.dds"` | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) |
| parent | 调用一个纹章定义 | `parent = "sub_SWE_union_mark"` | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| instance | 开始一个实例块 | `instance = { … }` | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |
| mask | 选择图案的哪一部分遮罩该纹章图案或子块 | `mask = { 1 }` | ![No](/images/thumb/0/04/No.png/24px-No.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) | ![Yes](/images/thumb/7/77/Yes.png/24px-Yes.png) |

以下是在 *instance* 块内部使用的术语。这些术语中的所有值都可以用 `@prescripted_value_name` 替换为 [预设值](Macro.md)，或使用 `@[expression]` 的数学表达式。后者对于 1/3 或 1/6 这类在固定小数中不精确的值尤其有用。例如，1/3 应写作 `@[1/3]`。

| 术语 | 功能 | 示例 | 示例说明 |
|---|---|---|---|
| scale | 以 x y 格式按默认大小的百分比缩放实例 | `scale = { 0.5 0.25 }` | 水平缩放为二分之一，垂直缩放为四分之一 |
| position | 以 x y 格式将实例中心移动到相对于底层左上角的百分比位置 | `position = { 0.25 0.75 }` | 中心位于距底层左侧四分之一、距顶部四分之三处 |
| rotation | 将实例顺时针旋转指定度数（负值为逆时针） | `rotation = { 45 }` | 顺时针旋转 45 度 |

Sub 实例使用 `offset` 代替 `position`，除此之外完全相同，且它们不能被旋转。

## 纹章颜色与单位模型颜色

游戏中的单位模型颜色取自国家定义的单位颜色，或当前使用纹章的颜色。

单位模型颜色可以在国家定义中定义为：

```
    primary_unit_color = { 20 20 120 }
    secondary_unit_color  = { 150 190 210 }
    tertiary_unit_color = { 5 5 90 }
```

否则，纹章定义的前三个基础/图案颜色将决定单位模型颜色，即使这些颜色并未出现在旗帜上。为纹章图案定义的颜色永远不会被考虑。

## 参考文献

1. ↑ 在给定条件下，某一组合似乎是稳定的，即国家的内部游戏 ID；一个拥有生成旗帜的 tag 在不同游戏中会保持相同的旗帜。
2. ↑ 注意，这些脚本名称中的 "template" 很可能只是为了便于人类阅读，并非严格要求
3. ↑ 目前尚无其他颜色格式的基础游戏示例

Modding
返回顶部
| 文档 | [Defines](Defines.md) • [Effects](Effect.md) • [Event targets](Event target.md) • [Scopes](Scope.md) • [Triggers](Trigger.md) [Macros](Macro.md) • [Modifier types](Modifier types.md) • [On actions](https://vic3.paradoxwikis.com/On_actions) • [Script value](Script value.md) • [变量](Variable.md) |
|---|---|

| 脚本内容 | [决议](Decision modding.md) • [事件](Event modding.md) • [历史](History modding.md) • [日志](Journal modding.md) • [修正](Modifier modding.md) • 目标 • [Scripted gui](Scripted gui.md) |
|---|---|

| 脚本类型 | [建筑](Building modding.md) • [人物](Character modding.md) • 概念 • [国家](Country modding.md) • [文化](Culture modding.md) • [法令](Decree modding.md) • [外交](Diplomacy modding.md) • [商品](Goods modding.md) • [机构](Institution modding.md) • [利益集团](Interest group modding.md) • [法律](Law modding.md) • 政党 • [人口](Pop modding.md) • [强权集团](Power bloc modding.md) • [宗教](Religion modding.md) • 附属国类型 • [技术](Technology modding.md) • [条约](Treaty modding.md) • [战争目标](War goal modding.md) |
|---|---|

| 地图 | [地图](Map modding.md) • [地理区域](Geographic region modding.md) • [州](State modding.md) |
|---|---|

| 界面 | [界面](Interface modding.md) • [GUI 脚本](GUI script.md) • [本地化](Localization.md) • [可自定义本地化](Localization.md) • [脚本本地化](Script localization.md) |
|---|---|

| 图形 | [3D 模型](Model modding.md) • [事件图片](Event images.md) • [图形资源](Graphical asset modding.md) • 字体 • 旗帜 |
|---|---|

| 音频 | 音乐 • [音效](Sound modding.md) |
|---|---|

| 其他 | [AI](AI modding.md) • [控制台命令](Console commands.md) • [校验和](https://vic3.paradoxwikis.com/Checksum) • [Mod](Mod.md) • [Mod 兼容性](Mod compatibility.md) • [Mod 结构](Mod structure.md) • [脚本测试](Scripted test.md) • [故障排除](Troubleshooting.md) |
|---|---|

| 指南 | [Mod 翻译](Mod translation.md) • [新国家制作](New country modding.md) • [存档编辑](Save-game editing.md) • [州制作指南](State modding guide.md) |
|---|---|