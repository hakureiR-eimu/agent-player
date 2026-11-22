# harness 装依赖与启动（复制粘贴用，在 vic3-GreatBritain/ 目录执行）

# 1. 装依赖（IM 接入用 discord.py，依赖组里还有测试用的 pytest）
uv sync

# 2. 跑测试（集成测试默认排除，前提与跑法见 docs/运行与测试/集成测试.md）
uv run pytest

# 3. 启动 harness 进程（Ctrl+C 退出；启动前提与步骤见 docs/运行与测试/运行.md）
#    配置走开发文件夹下的 config.toml（模板 config.example.toml，复制改名后填 dm_token、gbr_token、player_id）
uv run python -m main
