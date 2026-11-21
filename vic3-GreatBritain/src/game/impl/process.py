"""游戏在跑检测（声明见 docs/prd/游戏接入-harness侧.md 实现·游戏在跑检测）。"""

from __future__ import annotations

import subprocess


def game_running(process: str) -> bool:
    """按进程名查进程表（Windows tasklist），判断游戏是否已启动；查进程表本身失败抛错。"""
    result = subprocess.run(
        ["tasklist", "/FI", f"IMAGENAME eq {process}", "/FO", "CSV", "/NH"],
        capture_output=True,
        text=True,
        errors="replace",
        timeout=10,
    )
    if result.returncode != 0:
        raise RuntimeError(f"查进程表失败：{result.stderr.strip()}")
    return process.lower() in result.stdout.lower()
