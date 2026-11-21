# harness 装依赖与启动（复制粘贴用，在 vic3-GreatBritain/ 目录执行）

# 1. 装依赖（IM 接入用 discord.py，依赖组里还有测试用的 pytest）
uv sync

# 2. 跑测试（端到端测试默认排除——game 的要游戏在跑、im 的要真 token 且 E2E_DISCORD_PLAYER_ID 填玩家 ID；
#    手动跑：uv run pytest -m e2e -s）
uv run pytest

# 3. 启动 harness 进程（游戏接入与 IM 接入已落地，agent 未建：起会话的命令回执会明确报未实现；Ctrl+C 退出）
#    配置走开发文件夹下的 config.toml（模板 config.example.toml，复制改名后填 dm_token、gbr_token）
uv run python -m main
