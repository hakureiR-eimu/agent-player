"""游戏在跑检测的单测：查进程表（tasklist）。进程名与日志路径来自总配置的默认值，单测在 test_config。"""

import sys
from pathlib import Path

from game.impl.process import game_running


def test_不存在的进程不算在跑():
    assert game_running("no-such-process-xyz.exe") is False


def test_在跑的进程算在跑():
    # 当前跑测试用的解释器进程必然在进程表里
    assert game_running(Path(sys.executable).name) is True
