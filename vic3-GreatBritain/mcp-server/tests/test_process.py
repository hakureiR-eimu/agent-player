"""游戏在跑检测的单测：查进程表（tasklist）。"""

import os
import sys
from pathlib import Path

import server


def test_不存在的进程不算在跑():
    assert server.game_running("no-such-process-xyz.exe") is False


def test_在跑的进程算在跑():
    # 当前跑测试用的解释器进程必然在进程表里
    assert server.game_running(Path(sys.executable).name) is True


def test_未配置时默认查游戏进程():
    old = os.environ.pop("VIC3_MCP_GAME_PROCESS", None)
    try:
        assert server.game_process() == "victoria3.exe"
    finally:
        if old is not None:
            os.environ["VIC3_MCP_GAME_PROCESS"] = old


def test_日志路径默认指向游戏logs目录():
    old_dir = os.environ.pop("VIC3_MCP_LOG_DIR", None)
    old_file = os.environ.pop("VIC3_MCP_LOG_FILE", None)
    try:
        path = server.log_path()
        assert path.name == "error.log"
        assert path.parent == (
            Path.home() / "Documents" / "Paradox Interactive" / "Victoria 3" / "logs"
        )
    finally:
        for key, value in (("VIC3_MCP_LOG_DIR", old_dir), ("VIC3_MCP_LOG_FILE", old_file)):
            if value is not None:
                os.environ[key] = value
