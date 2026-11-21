# harness 装依赖与启动（复制粘贴用，在 vic3-GreatBritain/ 目录执行）

# 1. 装依赖（主体骨架只用标准库，依赖组里只有测试用的 pytest）
uv sync

# 2. 跑测试
uv run pytest

# 3. 启动 harness 进程（骨架阶段三大模块未建，装配处会明确报待建；Ctrl+C 退出）
#    可配环境变量（Discord token、error.log 路径、游戏进程名、局文件夹，默认即真实值）见 src/config.py 文件头
uv run python -m main
