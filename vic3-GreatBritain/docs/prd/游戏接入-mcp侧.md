# 游戏接入-mcp侧

游戏接入拆成两侧：mod 侧（[游戏接入-mod侧](游戏接入-mod侧.md)）把游戏内状态导出到 debug.log，mcp 侧（本文件）把日志变成 agent 可用的工具。mcp-server 在 vic3-GreatBritain/mcp-server/，TypeScript 写，是游戏侧唯一的外部通道。第一版只做读工具；写工具（操作注入、回执）随写侧后续版本。

## 职责与边界

mcp 侧的边界：从 debug.log 到 MCP 工具为止——解析 mod 侧定义的年度记录（封闭清单见 mod 侧文档），把状态读取包装成标准的 MCP 服务。下游是任意 MCP 客户端，不依赖 harness 存在，比如直接给 Claude Code 挂上就能用。

## 声明：做什么

第一版两个读工具：

- get_yearly_state：取最新一年的世界格局快照，返回结构化数据
- list_years：列出有哪些年份的记录

## 实现：怎么做

- get_yearly_state：解析 debug.log 里最新一年的记录，按 mod 侧定义的格式转成结构化数据
- list_years：扫描历史记录，生成年份索引
- 日志定位：Documents/Paradox Interactive/Victoria 3/logs/debug.log，路径可配置；游戏自动轮转保留 5 份（debug.1.log ~ debug.5.log），解析要考虑跨轮转文件

## 前提

- 存档可在 pdx_settings.json 里设成文本格式，mcp-server 可用它做全量校准
