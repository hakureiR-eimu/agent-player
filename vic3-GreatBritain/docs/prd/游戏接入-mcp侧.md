# 游戏接入-mcp侧

游戏接入拆成两侧：mod 侧（[游戏接入-mod侧](游戏接入-mod侧.md)）把游戏内状态导出到 debug.log，mcp 侧（本文件）把日志变成 agent 可用的工具。mcp-server 在 vic3-GreatBritain/mcp-server/，TypeScript 写，是游戏侧唯一的外部通道。第一版读工具直接实现；写工具只声明一个——发起外交博弈（start_play），实现空置，随写侧版本补。

## 职责与边界

mcp 侧的边界：从 debug.log 到 MCP 工具为止——解析 mod 侧定义的年度记录（行格式与封闭清单见 mod 侧文档，两侧以行格式为交接面），把状态读取包装成标准的 MCP 服务。不读存档（直读已否决，见[存档直读验证](../调研/存档直读验证.md)）。下游是任意 MCP 客户端，不依赖 harness 存在，比如直接给 Claude Code 挂上就能用。

## 声明：做什么

第一版两个工具：

- get_state：读游戏的最新状态——最新一年的世界格局快照，返回结构化数据
- start_play：发起外交博弈（写工具），实现空置——工具注册给客户端，调用返回固定的"未实现"应答

## 实现：怎么做

- 记录识别：逐行扫日志，认前缀 `vic3-GreatBritain`（局名前缀，mod 侧定义），两类行：`state`（国家行）、`fin`（财政行）；行内 key=value 逐对解析，数值转数字，字段含义与行格式以 mod 侧文档为准
- 排序：mod 侧不保证行的先后（各国触发顺序不定），输出前 powers 按 rank 升序排好
- 合并去重：debug.log 与轮转的 debug.1.log ~ debug.5.log 按旧到新依次读入，同一 (tag, year) 后读的覆盖先读的——跨会话重跑同一年（读档、重开局）时，以最新一次记录为准
- 日志定位：默认 Documents/Paradox Interactive/Victoria 3/logs/，路径可配置；链路验证不造 mock，配置指向一份真实格式的样例日志即可单测
- MCP 接入：TypeScript＋官方 SDK（@modelcontextprotocol/sdk），stdio 传输，客户端按常规 MCP 服务挂载
- get_state 返回模板（`<>` 为占位）：

  ```json
  {
    "year": <年>,
    "powers": [
      { "tag": <tag>, "rank": <名次>, "gdp": <GDP>, "army": <营队数> }
    ],
    "gbr_finance": { "gold": <金库>, "debt": <债务本金>, "week_net": <每周净收支> }
  }
  ```

  示例（powers 共 16 国，此处截短）：

  ```json
  {
    "year": 1836,
    "powers": [
      { "tag": "GBR", "rank": 1, "gdp": 23456.7, "army": 30 },
      { "tag": "FRA", "rank": 3, "gdp": 12345.6, "army": 20 }
    ],
    "gbr_finance": { "gold": 54321.0, "debt": 0.0, "week_net": 12.3 }
  }
  ```

- 财政字段 week_net 若 mod 侧实测回退为 income，本侧字段名随之同步

待实测清单（首次跑 mod 一起验证）：

- 日志行是否带游戏加的时间戳/来源头（mod 侧同条待实测）——影响前缀过滤与解析的写法
- 游戏边写、agent 边读，文件末尾可能读到无换行的半行——实测出现的形态；处理方向是丢弃残行

## 前提

- 存档可在 pdx_settings.json 里设成文本格式，mcp-server 可用它做全量校准
