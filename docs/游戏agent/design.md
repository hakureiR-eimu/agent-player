# 游戏 agent：设计

对应 [requirements](requirements.md)。这里写"长什么样"：文件、格式、工具、会话怎么组装。薄版，实盘跑完回来改。

## 目录与权限

agents/<tag>/ 每局一套：

```
agents/<tag>/
  profile/     开局就位，整局只读
  world/       只有运行时写，agent 只读
    chat/      飞书聊天记录
    state/     游戏状态
  memory/      只有 agent 自己写
```

| 文件夹 | 谁写 | 谁读 |
| --- | --- | --- |
| profile/ | 建局时装好，之后整局没人写 | agent；运行时拉会话时取来组装 |
| world/ | 只有运行时 | agent 是主要读者 |
| memory/ | 只有 agent | agent；运行时排查问题时可看 |

权限在工具上配（Claude Agent SDK 的 permission 规则）：

- 允许 read、grep、glob：限 agents/<tag>/ 范围内。
- 允许 write、edit：限 memory/ 范围内。
- 其它工具一概不给（没有 bash 之类的通用执行）。

规则是第二道锁，第一道是工具箱本身只有下面清单里这几样。

## profile 的构成

- system.md：通用提示词，所有国家相同。内容：身份（扮演《维多利亚3》的一名玩家）、能力（可以操作游戏、可以去飞书跟其他玩家沟通）、习惯（重要的事随发生随记进 memory/，找旧账去 world/chat/ 翻）。
- country.md：国家介绍，建局时从 资料/主要国家/<tag>/介绍.md 取。

拉起会话时，把 system.md 和 country.md 按顺序拼成系统提示词。运行途中 agent 也可以回来翻这两个文件。

## 会话的组装与轮次

- 会话由运行时用 Claude Agent SDK 拉起，系统提示词来自 profile/。
- 开局第一轮：运行时注入一条开局消息，大意"新的一局开始了，先读 profile 和 world/state 了解形势，然后去大群报到"。文案实盘再打磨。
- 平时一轮：运行时把新消息（可打包几条）递进会话；agent 的回应就是调工具——发消息、记账、读文件。
- 上下文压缩交给 SDK 自己做；压缩丢掉的细节靠 world/chat/ 和 memory/ 找回，提示词里已交代。

## 消息格式（场景标签）

会话里递进来的消息和 world/chat/ 里的记录，用同一套格式，一行一条：

```
【<场景名>】<说话人>：<内容>
```

- 场景名用群名，人读得懂；运行时维护群名和群 ID 的对照，发消息时用 ID。
- 会话里递的消息不带时间戳（先后就是顺序，省字）；chat 文件里每行开头带日期时间（翻旧账要知道先后）。

## world/ 的文件组织

- chat/：一个群一个文件 world/chat/<群ID>.md，文件头写群名和成员，成员变动时追加一行记录。只追加，不改写。
- state/：开局时运行时写开局形势；之后游戏状态导成什么结构，等游戏接入的设计，这里占位。

## 工具清单（运行时实现）

| 工具 | 参数 | 作用 |
| --- | --- | --- |
| send_message | group_id, content | 在指定群发言 |
| list_groups | 无 | 群列表：ID、名称 |
| list_members | group_id | 指定群的成员列表 |
| create_group | name, members | 组建群；members 是国家 tag 或玩家 |
| act | payload | 操作游戏，空接口占位（游戏接入定形后细化） |

list_groups 和 list_members 也可以合并成一个（列表直接带成员），实盘看消息花销再定。

文件工具（read、grep、glob、write、edit）由 SDK 自带，靠上面的权限规则圈范围。

## 本地试跑（不接飞书的最小形态）

- 照常组装系统提示词、照常给文件夹。
- 飞书工具换成终端版：send_message 打印到终端，list_groups 返回几个写死的假群。
- 你在终端里扮演其他玩家，消息按场景标签格式敲进去。
- 目的：先验证人格、记账、翻旧账这三件事，平台一概不碰。

## 待定

- chat 文件过大了怎么分片（按时间还是按局内回合）——真跑长了再说。
- memory 内部结构——玩一两局看它自然记什么再定（requirements 已注明）。
- 开局消息的文案。
