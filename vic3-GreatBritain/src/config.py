"""总配置（声明见 docs/prd/harness.md 主体实现·入口与配置）。

进程从 main 起，读这一份配置，装配时发给三大模块。六项：两个 Discord bot 的 token
（dm_token、gbr_token）、error.log 路径、游戏进程名、局文件夹、GBR 路径（记忆三区所在，
固定在局文件夹下一层 GBR，随局文件夹派生）。

来源：开发文件夹下的 config.toml（模板见同目录 config.example.toml，复制改名后填两个
token）。四项可省，省略即用默认，默认值即真实值；文件没建按全默认。
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

DEFAULT_LOG_PATH = Path.home() / "Documents" / "Paradox Interactive" / "Victoria 3" / "logs" / "error.log"
DEFAULT_GAME_PROCESS = "victoria3.exe"
DEFAULT_GAME_DIR = Path(r"C:\Users\ZhangJunWei\Documents\Paradox Interactive\Victoria 3\vic3-GreatBritain")

CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.toml"


@dataclass(frozen=True)
class Config:
    dm_token: str | None
    gbr_token: str | None
    log_path: Path
    game_process: str
    game_dir: Path
    gbr_dir: Path


def load_config(path: Path = CONFIG_PATH) -> Config:
    """从配置文件读配置；path 参数供测试传入临时文件。文件没建按全默认，token 空串按没配。"""
    data: dict = {}
    if path.exists():
        with path.open("rb") as f:
            data = tomllib.load(f)
    game_dir = Path(data.get("game_dir", DEFAULT_GAME_DIR))
    return Config(
        dm_token=data.get("dm_token") or None,
        gbr_token=data.get("gbr_token") or None,
        log_path=Path(data.get("log_path", DEFAULT_LOG_PATH)),
        game_process=data.get("game_process", DEFAULT_GAME_PROCESS),
        game_dir=game_dir,
        gbr_dir=game_dir / "GBR",
    )
