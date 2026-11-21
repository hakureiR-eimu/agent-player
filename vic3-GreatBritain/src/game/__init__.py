"""游戏接入包（agent 的眼睛）：实现已从独立 mcp-server 迁入 impl/（parser 解析、process 在跑检测、module 模块本体）。

模块本体照 src/dispatcher.py 的 GameModule 协议实现：start 起 error.log 轮询，察觉
新年份的本局记录推 new_year 事件（data 为年份数字）；get_state/start_play 两个方法
给 agent 调，经 SDK 的进程内 MCP 注册进会话随 agent 模块实现落。
实现语义见 docs/prd/游戏接入-harness侧.md。
"""
