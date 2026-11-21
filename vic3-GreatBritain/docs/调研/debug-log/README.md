# debug-log 样例

真实游戏日志的原样拷贝，作为 mcp 侧解析与其他系统的格式参考。

- debug-2026-11-20.log：2026-11-21 从 `Documents/Paradox Interactive/Victoria 3/logs/debug.log` 拷贝，会话时段 2026-11-20 23:22–23:30。行首游戏加头、CRLF 行尾、与原版日志混杂的原始形态以此为准。该会话未触发本局年度导出，文件内没有 `vic3-GreatBritain` 记录行。
- error-2026-11-21.log：2026-11-21 从 `Documents/Paradox Interactive/Victoria 3/logs/error.log` 拷贝（游戏在跑中，会话 10:01 起）。含 1836/1837 两个游戏年的完整年度导出（各 16 国家行＋1 财政行）；记录行行尾 LF、引擎自身行 CRLF 混存，行首两级加头（`jomini_effect_impl.cpp` 来源＋`gb_agent_effects.txt` 脚本行号，国家行 14／财政行 20）的原始形态以此为准。
