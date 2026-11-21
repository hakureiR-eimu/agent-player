"""游戏接入模块本体（声明见 docs/prd/harness.md 游戏接入节，实现语义见 docs/prd/游戏接入-harness侧.md）。

跑在 harness 进程内，零总线、零 agent 知识：get_state/start_play 两个方法是纯方法，
主体装配时把它们包成会话工具（agent 调工具由主体翻译成对方法的实际调用）；check_new_year
供主体定时调，主体查到新年份自己推 new_year 事件。三个方法都以游戏在跑为前提
（check_new_year 在游戏没跑时返回 None）。
"""

from __future__ import annotations

from pathlib import Path

from config import Config
from game.impl.parser import build_snapshot, parse_record
from game.impl.process import game_running


class GameNotRunningError(RuntimeError):
    """游戏没启动就调方法：不读日志、不发通知。"""


class GameModuleImpl:
    """GameModule 协议（src/game/module.py）的实现。"""

    def __init__(self, config: Config) -> None:
        self._log_path = config.log_path
        self._game_process = config.game_process
        self._last_mtime: float | None = None
        self._notified_year: int | None = None

    # ---- 两个方法（给 agent 调） ----

    def get_state(self) -> dict:
        """读取世界局势：各国最新一条记录拼成的快照（powers 按行内 rank 升序），
        游戏第一年还没导出过记录时返回空。"""
        self._require_game()
        try:
            text = self._log_path.read_text(encoding="utf-8", errors="replace")
        except FileNotFoundError:
            return {"powers": [], "gbr_finance": None}
        return build_snapshot(text)

    def start_play(self) -> str:
        """发起外交博弈（写侧占位）：实现随写侧版本补，当前返回固定的"未实现"应答。"""
        self._require_game()
        return "未实现：start_play 是写侧方法，随写侧版本补，当前只读。"

    def _require_game(self) -> None:
        if not game_running(self._game_process):
            raise GameNotRunningError(
                f"游戏未启动：进程表里没有 {self._game_process}，先启动 Victoria 3 再调用方法"
            )

    # ---- 新年判定（主体定时调） ----

    def check_new_year(self) -> int | None:
        """查一次 error.log：出现比上次已通知新的本局记录年份返回该年份，没有返回 None。

        先看文件修改时间，变了才解析；游戏没跑时不当作新年（读到的是上次留下的旧
        日志），但记下年份，免得游戏启动后把旧年份当新年。
        """
        try:
            mtime = self._log_path.stat().st_mtime
        except FileNotFoundError:
            return None
        if mtime == self._last_mtime:
            return None
        self._last_mtime = mtime

        year = _latest_year(self._log_path)
        if year is None or (self._notified_year is not None and year <= self._notified_year):
            return None
        self._notified_year = year
        if not game_running(self._game_process):
            return None
        return year


def _latest_year(log_path: Path) -> int | None:
    """整份日志里本局记录的最新年份；没有本局记录返回 None。"""
    try:
        text = log_path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return None
    years = [
        record["year"]
        for line in text.splitlines()
        if (record := parse_record(line)) is not None
    ]
    return max(years, default=None)
