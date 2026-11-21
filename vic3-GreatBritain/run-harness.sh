# harness 装依赖与启动（复制粘贴用，在 vic3-GreatBritain/ 目录执行）

# 1. 装依赖（主体与游戏接入只用标准库，依赖组里只有测试用的 pytest）
uv sync

# 2. 跑测试（game 模块的端到端测试需要游戏在跑，默认排除；手动跑：uv run pytest -m e2e -s）
uv run pytest

# 3. 启动 harness 进程（游戏接入已迁入，agent 与 IM 接入未建，装配处会明确报待建；Ctrl+C 退出）
#    配置走开发文件夹下的 config.toml（模板 config.example.toml，复制改名后填 token）
uv run python -m main
