# mcp-server 装依赖与启动（复制粘贴用，在本目录执行）

# 1. 装依赖（首次要联网下包，慢）
uv sync

# 2. 启动 mcp 服务（stdio 传输，直接跑会挂起等 MCP 客户端连入，Ctrl+C 退出）
#    客户端挂载：command 配本目录/.venv/Scripts/python.exe，args 配本目录/server.py（绝对路径）
#    可配环境变量（日志目录/文件名/进程名，默认即真实路径）见 server.py 文件头
uv run python server.py
