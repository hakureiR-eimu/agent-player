"""总配置单测：默认值即真实值、配置文件覆盖、gbr 路径随局文件夹派生。"""

from pathlib import Path

from config import DEFAULT_GAME_DIR, load_config


def write_config(tmp_path: Path, content: str) -> Path:
    path = tmp_path / "config.toml"
    path.write_text(content, encoding="utf-8")
    return path


def test_默认配置即真实值(tmp_path):
    config = load_config(tmp_path / "config.toml")
    assert config.dm_token is None
    assert config.gbr_token is None
    assert config.discord_proxy is None
    assert config.game_process == "victoria3.exe"
    assert config.log_path.name == "error.log"
    assert "Victoria 3" in str(config.log_path)
    assert config.game_dir == DEFAULT_GAME_DIR
    assert config.system_log_dir == DEFAULT_GAME_DIR / "logs" / "system"
    assert config.agent_log_dir == DEFAULT_GAME_DIR / "logs" / "agent"
    assert config.player_id == ""
    assert config.anthropic_base_url is None
    assert config.anthropic_auth_token is None
    assert config.agent_model is None


def test_配置文件覆盖(tmp_path):
    path = write_config(
        tmp_path,
        r"""
dm_token = "token-dm"
gbr_token = "token-gbr"
discord_proxy = "http://127.0.0.1:7890"
log_path = 'D:\somewhere\error.log'
game_process = "vic3-test.exe"
game_dir = 'D:\somewhere\game'
player_id = "123456789012345678"
anthropic_base_url = "https://api.z.ai/api/anthropic"
anthropic_auth_token = "sk-xxx"
agent_model = "glm-4.7"
""",
    )
    config = load_config(path)
    assert config.dm_token == "token-dm"
    assert config.gbr_token == "token-gbr"
    assert config.discord_proxy == "http://127.0.0.1:7890"
    assert str(config.log_path) == r"D:\somewhere\error.log"
    assert config.game_process == "vic3-test.exe"
    assert str(config.game_dir) == r"D:\somewhere\game"
    assert config.player_id == "123456789012345678"
    assert config.anthropic_base_url == "https://api.z.ai/api/anthropic"
    assert config.anthropic_auth_token == "sk-xxx"
    assert config.agent_model == "glm-4.7"


def test_gbr路径随局文件夹派生(tmp_path):
    path = write_config(tmp_path, r"game_dir = 'D:\somewhere\game'")
    config = load_config(path)
    assert config.gbr_dir == config.game_dir / "gbr"
    assert str(config.gbr_dir) == r"D:\somewhere\game\gbr"


def test_两处日志目录随局文件夹派生(tmp_path):
    path = write_config(tmp_path, r"game_dir = 'D:\somewhere\game'")
    config = load_config(path)
    assert config.system_log_dir == config.game_dir / "logs" / "system"
    assert config.agent_log_dir == config.game_dir / "logs" / "agent"
    assert str(config.system_log_dir) == r"D:\somewhere\game\logs\system"
    assert str(config.agent_log_dir) == r"D:\somewhere\game\logs\agent"


def test_空token等于没配(tmp_path):
    path = write_config(tmp_path, 'dm_token = ""\ngbr_token = ""\n')
    config = load_config(path)
    assert config.dm_token is None
    assert config.gbr_token is None
