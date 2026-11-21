"""总配置单测：默认值即真实值、环境变量覆盖、GBR 路径随局文件夹派生。"""

from config import DEFAULT_GAME_DIR, load_config


def test_默认配置即真实值():
    config = load_config(env={})
    assert config.discord_token is None
    assert config.game_process == "victoria3.exe"
    assert config.log_path.name == "error.log"
    assert "Victoria 3" in str(config.log_path)
    assert config.game_dir == DEFAULT_GAME_DIR


def test_GBR路径随局文件夹派生():
    config = load_config(env={})
    assert config.gbr_dir == config.game_dir / "GBR"


def test_环境变量覆盖():
    env = {
        "HARNESS_DISCORD_TOKEN": "token-x",
        "HARNESS_LOG_PATH": r"D:\somewhere\error.log",
        "HARNESS_GAME_PROCESS": "vic3-test.exe",
        "HARNESS_GAME_DIR": r"D:\somewhere\game",
    }
    config = load_config(env)
    assert config.discord_token == "token-x"
    assert str(config.log_path) == r"D:\somewhere\error.log"
    assert config.game_process == "vic3-test.exe"
    assert str(config.game_dir) == r"D:\somewhere\game"
    assert str(config.gbr_dir) == r"D:\somewhere\game\GBR"
