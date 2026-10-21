# agents/

一国一个文件夹，一个 agent 的全部内容都在这。三区结构、谁读谁写见 [docs/游戏agent/requirements](../docs/游戏agent/requirements.md)。

- 模板/：新建 agent 时整份拷走，把 profile/country.md 换成 资料/主要国家/<tag>/介绍.md 的内容，文件夹名改成 tag。
- GBR/：阶段一的试跑实例。

world/chat/、world/state/、memory/ 从空开始、随局生长，空文件夹用 .gitkeep 占位。正式的建局脚本在阶段三才做（见 [docs/执行](../docs/执行.md)）。
