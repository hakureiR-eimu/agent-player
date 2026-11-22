# agent-运行时

agent 是玩维多利亚3的玩家：与人机同局的人类玩家对等，只是他执掌的国家是大不列颠。他通过 harness 拿到两件游戏能力——读取世界状态、发起外交博弈；在 Discord 上收得到玩家的私信、回得上话。他的设计分两块：本文件写运行时——harness 用 Claude Agent SDK 起一个会话，配上文件夹、工具、消息队列，会话随局起止，让 agent 跑得起来；记忆与人格见 [agent-记忆和人格](agent-记忆和人格.md)。接口声明见 [harness](harness.md) 的 agent 节。

运行时是 Claude Agent SDK（Python 包 claude-agent-sdk，Claude Code 装成库）起的一个会话：agent 循环、文件工具、上下文管理都是 SDK 自带的，harness 不自研循环，只在会话外面包六件事——注 system prompt、给文件夹、挂工具、递消息、管起止、留运行记录。会话的模型与凭证由 config 三项配（anthropic_base_url、anthropic_auth_token、agent_model，如接 GLM 的 Anthropic 兼容入口），与玩家自己的 Claude Code 分开；三项全空走本机 Claude Code 的登录态。

system prompt 吃开发文件夹 prompt/ 下的 agent-system-prompt.md（固定内容，完全替换 SDK 默认的 system prompt——agent 是玩家，不吃助手默认人设）。

## 文件夹

- 运行时文件夹固定一个：C:\Users\ZhangJunWei\Documents\Paradox Interactive\Victoria 3\vic3-GreatBritain；agent 的一切文件在它下面的 gbr 文件夹
- 会话的工作目录设在 gbr——agent 的文件世界就是这一个文件夹
- gbr 的生灭随局：开始游戏把开发文件夹 prompt/ 的 gbr-template/ 整个复制成全新的 gbr，结束游戏清掉；模板里有什么、记忆怎么分区见 [agent-记忆和人格](agent-记忆和人格.md)

## 工具

- 文件读写——SDK 内置工具，围着 gbr 文件夹转，写权限配在 memory/
- 游戏动作——get_state（读取世界局势）、start_play（发起外交博弈）
- Discord 收发——读消息（翻与玩家的私信历史）、发消息（把话发给玩家）；两件都带玩家 ID 参数，agent 从收到的私信里学玩家的 Discord 用户 ID

后两类都是主体装配时经 SDK 的进程内 MCP 递入，agent 模块只管挂进会话，不知道工具背后是什么。

## 消息队列

消息的接收与读取是两回事：接收是队列的事，读取是会话里的工具（见「工具」）。两类到达进队列——玩家私信 gbr bot（IM 接入推 message 事件，收下即落盘 world/chat/）、游戏进新年（游戏接入推 new_year 事件）。队列到会话之间隔着 agent 模块，攒与送都在模块里：

- 空闲即送：会话空闲时消息一到，就送进会话、唤醒它
- 忙时攒批：会话在忙，新到的攒着不打断；等它空闲了，把攒下的 Discord 消息与新年合并成一段上下文送进会话、唤醒它
- 发消息与读消息带玩家 ID 参数，agent 调用时自己填——值从收到的私信学来（送进会话的私信带玩家的 Discord 用户 ID）；开局不主动发话，玩家第一条私信来了才亮相

送进会话的消息样式：私信一条是「玩家 〈用户 ID〉 发来私信：〈正文〉」，新年是「游戏进入了 〈年份〉 年。」。忙时攒下的一批合并成一段，最前面带一行标注告诉 agent 这些是它忙期间积下的——

    你在忙期间发生了以下事件：

    玩家 123456789012345678 发来私信：
    在吗

    玩家 123456789012345678 发来私信：
    你财政怎么样

    游戏进入了 1837 年。

## 会话随局起止

- 开始游戏：建本局频道（GreatBritain），把 gbr-template/ 整个复制成全新的 gbr 文件夹，起一个基于它的会话。频道已在（上次局没结束）就拒绝
- 保存游戏：让会话整理自己的文件夹（memory 收尾），然后结束会话；频道留着，局还挂着
- 结束游戏：会话在跑先按保存游戏收尾，然后销频道、清 gbr——这局彻底完

## 预期结果

一局跑起来后的样子：

- 开局：玩家在大厅频道 @ dm bot 下开始游戏，harness 建本局频道（GreatBritain）、把 gbr-template 复制成全新的 gbr、起会话；agent 按手册（gbr 里的 CLAUDE.md）把开局事办了，话等玩家先说——玩家第一条私信进来（带着他的 Discord 用户 ID），他才亮相回话：他是谁、这局想干什么
- 年度：游戏每进一个新年，new_year 把 agent 叫醒；他调 get_state 看世界格局，把研判写进 memory，并私信玩家一份年度研判
- 对话：玩家私信 gbr bot 谈外交——交易、结盟、威胁、试探；agent 结合盘上的记忆回话，两位玩家就各自执掌的国家讨价还价
- 博弈：谈拢或谈崩，agent 调 start_play 在游戏里发起外交博弈，博弈之后的游戏操作由游戏原生 AI 消化（写侧的其余注入后续版本再做）
- 收档：保存游戏让 agent 整理 memory 后结束会话，局还挂着（频道在）；结束游戏销频道、清 gbr，这局彻底完，下一局从全新的记忆开始

第一版验证的就是这条循环：观察、研判、对话、发起博弈。

## 实现：怎么做

代码在 src/agent/impl/（测试在 test/agent/），实现要点：

- 起会话：claude-agent-sdk 起会话，工作目录设在 gbr 文件夹、写权限配在 memory/；system prompt 吃项目里的 agent-system-prompt.md 注入（完全替换默认），gbr 里复制来的 CLAUDE.md 手册由 SDK 作为项目指令自动装载
- 挂工具：主体递入的 get_state/start_play 与 Discord 收发（读/发消息）经 SDK 的进程内 MCP 挂进会话
- 攒批与送批：消息到了先攒，会话空闲了把攒下的一批拼进会话跑完
- 落盘：私信对话到达时逐条追加进 world/chat/
- 运行记录：起会话时在 logs/agent（局文件夹派生）建本局记录文件，路径递进会话；SDK 送批流过的消息按四类逐条追加（见[日志功能](日志功能.md)）
- 上下文：长会话的压缩归 SDK 的上下文管理，压缩丢了细节不要紧——world/ 与 memory/ 在盘上
- 测试：单测盖消息队列（空闲即送、忙时攒批）、拼批、对话落盘、记录文件建立；集成测试起真会话（test/agent/test_agent_integration.py，在 VSCode 测试面板里跑，样式照 test/game/）
