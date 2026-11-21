"""游戏接入包（agent 的眼睛）：现有 mcp-server（开发文件夹下的 mcp-server/server.py）迁入本包 impl/。

迁入时照 src/dispatcher.py 的 GameModule 补进程内一面：start 起 error.log 轮询、
发现新年份的本局记录推 new_year 事件，get_state/start_play 两个方法由主体经 SDK 的进程内
MCP 注册进 agent 会话。实现语义见 docs/prd/游戏接入-mcp侧.md。
"""
