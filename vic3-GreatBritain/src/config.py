"""总配置（声明见 docs/prd/harness.md 主体实现·入口与配置）。

进程从 main 起，读这一份配置，装配时发给三大模块。五项：Discord token、error.log 路径、
游戏进程名、局文件夹、GBR 路径（记忆三区所在，固定在局文件夹下一层 GBR，随局文件夹派生）。

来源：环境变量，可省略的都有默认，默认值即真实值：

  HARNESS_DISCORD_TOKEN   Discord bot token（IM 接入用，未实现前可省）
  HARNESS_LOG_PATH        error.log 路径
  HARNESS_GAME_PROCESS    游戏进程名，默认 victoria3.exe
  HARNESS_GAME_DIR        局文件夹，默认 Victoria 3 用户目录下的 vic3-GreatBritain
"""

from __future__ import annotations

import os
from collections.abc import MutableMapping
from dataclasses import dataclass
from pathlib import Path

DEFAULT_LOG_PATH = Path.home() / "Documents" / "Paradox Interactive" / "Victoria 3" / "logs" / "error.log"
DEFAULT_GAME_PROCESS = "victoria3.exe"
DEFAULT_GAME_DIR = Path(r"C:\Users\ZhangJunWei\Documents\Paradox Interactive\Victoria 3\vic3-GreatBritain")


@dataclass(frozen=True)
class Config:
    discord_token: str | None
    log_path: Path
    game_process: str
    game_dir: Path
    gbr_dir: Path


def load_config(env: MutableMapping[str, str] | None = None) -> Config:
    """从环境变量读配置；env 参数供测试传入构造好的变量表。"""
    env = os.environ if env is None else env
    game_dir = Path(env.get("HARNESS_GAME_DIR", DEFAULT_GAME_DIR))
    return Config(
        discord_token=env.get("HARNESS_DISCORD_TOKEN"),
        log_path=Path(env.get("HARNESS_LOG_PATH", DEFAULT_LOG_PATH)),
        game_process=env.get("HARNESS_GAME_PROCESS", DEFAULT_GAME_PROCESS),
        game_dir=game_dir,
        gbr_dir=game_dir / "GBR",
    )
