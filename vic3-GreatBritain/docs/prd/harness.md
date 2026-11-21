# harness

harness 是整个程序的主体，一个 Python 进程，装四块：主体负责整个程序的生命周期、调用其余三块实现功能；三个子模块各管一摊——游戏接入（game）、agent、IM 接入。三个子模块在本文档只写声明（能力是什么），实现各在自己的文档：游戏接入已实现，见[游戏接入-mcp侧](游戏接入-mcp侧.md)；agent 与 IM 接入的实现文档随后另起。

## 主体

主体是 harness 的骨架，管整个程序的生命周期，三个子模块由它装载、调用。

- 进程与会话：harness 进程不绑局文件夹；agent 会话随局起止——开始或继续一局时起会话、把会话接上 IM 和游戏接入，保存时让会话整理自己的文件夹、结束会话
- 事件队列：主体维护一条事件队列，模块之间互不引用，来往全走它——每个模块都可以推事件，也都可以订事件，主体自己也订。四种事件：command（玩家命令，IM 接入推、主体订）、message（玩家消息，IM 接入推、agent 订）、new_year（年度通知，游戏接入推、agent 订）、reply（会话回复，agent 推、IM 接入订）

## 主体实现

主体是装配加调度的一层，自身没有业务逻辑，实现写在本节、不另起文档。代码在 vic3-GreatBritain/src/（测试在 test/，按模块分目录）：main 管入口与装配，调度模块管分流、局状态与命令执行，三大模块各成一个包（agent、game、im，实现进各包 impl/）——游戏接入的包就是现有 mcp-server 挪进来。

- 入口与配置：进程从 main 起，读一份总配置——Discord token、error.log 路径、游戏进程名、局文件夹与 GBR 路径
- 装配：按配置把三大模块建出来、接上——游戏接入是进程内模块，直接实例化；IM 接入登录 Discord；agent 持会话。模块之间互不引用，谁接谁只有主体知道
- 事件循环：一个主循环（asyncio），进程活着就在等事件——模块包成事件推进队列，主循环逐个取、按事件类型投给订了它的模块，一次投一个，投递串行
- 局状态与命令执行：主体记一个状态——会话在不在跑。命令到了按状态排动作：startGame 建全新的 GBR 文件夹，loadGame 用已有的，两者接着都起一个基于 GBR 的 agent 会话、把会话接上 IM 和游戏接入；stopGame 让会话整理自己的文件夹，然后结束会话。主体只排顺序，动作本身调三大模块干
- 退出：进程收摊，会话还在跑就先按 stopGame 收尾再退

## 游戏接入（game）

agent 的眼睛，跑在 harness 进程内：mod 在游戏里每年把世界格局写进 error.log，游戏接入把日志变成两个方法给 agent 调，每年察觉新年份记录时往事件队列推 new_year 事件。声明三个能力：

- get_state——读取世界局势：各国最新一条记录拼成的世界格局快照
- start_play——发起博弈：发起一局外交博弈
- new_year——年度通知（推送）：游戏内每过一年（error.log 出现新年份的本局记录），往事件队列推一个 new_year 事件

三个能力都以游戏在跑为前提。行格式与实现细节见[游戏接入-mcp侧](游戏接入-mcp侧.md)。

## agent

agent 本体是 Claude Code 会话。局文件夹固定一个：C:\Users\ZhangJunWei\Documents\Paradox Interactive\Victoria 3\vic3-GreatBritain；agent 的记忆文件放在它下面的 GBR 文件夹，profile/world/memory 三区由 agent 管理装载。事件侧的能力已定：

- wake——叫醒（订阅 message、new_year）：事件到了，会话空闲就叫醒它处理
- 串行：会话一次只做一批——会话在忙时，新到的事件不打断，攒着；会话空闲了，把攒下的一起送进会话，做完这批才轮到下一批
- reply——回复（推送 reply）：会话产出的回复包成 reply 事件推回队列，IM 接入订到后发回局频道

其余能力声明待想清楚后补齐。

## IM 接入

agent 的嘴和耳朵，通 Discord。声明两块能力：

- 命令通道（推送 command）：玩家在大厅频道和私信（DM）里对 bot 下命令，bot 非 LLM 驱动，命令包成 command 事件推进队列，主体订到后执行。三条命令：
  - startGame（开始新档）：初始化 GBR 文件夹，起一个基于它的 agent 会话，接上 IM 和游戏接入
  - loadGame（继续存档）：基于已有的 GBR 文件夹起 agent 会话，接上 IM 和游戏接入
  - stopGame（保存存档）：让会话整理自己的文件夹，然后结束会话
- 局频道（推送 message＋订阅 reply）：名叫 vic3-GreatBritain 的子频道，agent 的对话场所——玩家在频道发的消息包成 message 事件推进队列（agent 订到叫醒会话）；订 reply 事件，把回复发进频道
