"""总配置（声明见 docs/prd/harness.md 主体实现·入口与配置）。

进程从 main 起，读这一份配置，装配时发给三大模块。十三项：两个 Discord bot 的 token
（dm_token、gbr_token）、Discord 出口代理（discord_proxy，网络直连不通时填本地代理）、
error.log 路径、游戏进程名、局文件夹、gbr 路径（记忆三区所在，固定在局文件夹下一层
gbr，随局文件夹派生）、两处运行日志目录（system_log_dir、agent_log_dir——局文件夹下
logs/system 与 logs/agent，也随局文件夹派生，记录内容见 docs/prd/日志功能.md）、
人类玩家的 Discord 用户 ID（player_id，agent 的发消息工具定向发他的私信）、
agent 会话的模型与凭证三项（anthropic_base_url、anthropic_auth_token、agent_model——
配了 agent 会话走它，与玩家自己的 Claude Code 分开；全空走本机 Claude Code 的登录态）。

来源：开发文件夹下的 config.toml（模板见同目录 config.example.toml，复制改名后填两个
token）。三项派生（gbr 与两处日志目录，不从文件读），其余十项可省，省略即用默认，
默认值即真实值；文件没建按全默认。
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DEFAULT_LOG_PATH = Path.home() / "Documents" / "Paradox Interactive" / "Victoria 3" / "logs" / "error.log"
DEFAULT_GAME_PROCESS = "victoria3.exe"
DEFAULT_GAME_DIR = Path(r"C:\Users\ZhangJunWei\Documents\Paradox Interactive\Victoria 3\vic3-GreatBritain")

CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.toml"


@dataclass(frozen=True)
class Config:
    dm_token: str | None
    gbr_token: str | None
    discord_proxy: str | None
    log_path: Path
    game_process: str
    game_dir: Path
    gbr_dir: Path
    system_log_dir: Path
    agent_log_dir: Path
    player_id: str
    anthropic_base_url: str | None
    anthropic_auth_token: str | None
    agent_model: str | None


def load_config(path: Path = CONFIG_PATH) -> Config:
    """从配置文件读配置；path 参数供测试传入临时文件。文件没建按全默认，token 空串按没配。"""
    data: dict[str, Any] = {}
    if path.exists():
        with path.open("rb") as f:
            data = tomllib.load(f)
    game_dir = Path(data.get("game_dir", DEFAULT_GAME_DIR))
    return Config(
        dm_token=data.get("dm_token") or None,
        gbr_token=data.get("gbr_token") or None,
        discord_proxy=data.get("discord_proxy") or None,
        log_path=Path(data.get("log_path", DEFAULT_LOG_PATH)),
        game_process=data.get("game_process", DEFAULT_GAME_PROCESS),
        game_dir=game_dir,
        gbr_dir=game_dir / "gbr",
        system_log_dir=game_dir / "logs" / "system",
        agent_log_dir=game_dir / "logs" / "agent",
        player_id=str(data.get("player_id", "")),
        anthropic_base_url=data.get("anthropic_base_url") or None,
        anthropic_auth_token=data.get("anthropic_auth_token") or None,
        agent_model=data.get("agent_model") or None,
    )
