# agents/

- 模板/：新建 agent 时的底子。建局不用手动拷——控制台建局时自动按模板生成，profile/country.md 换成 资料/主要国家/<tag>/介绍.md 的内容，文件夹名就是 tag。

三区结构、谁读谁写见 [docs/游戏agent/requirements](../docs/游戏agent/requirements.md)。world/chat/、world/state/、memory/ 建局时从空开始、随局生长（局文件夹在仓库根，形如 局名/agents/<tag>/，整局不进 git）。
