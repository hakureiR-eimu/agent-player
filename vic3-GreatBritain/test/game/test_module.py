"""game 模块本体的单测：三个方法（游戏在跑门槛、样例日志、新年判定）。

链路走真路径不造 mock：日志用真实格式的样例或临时文件，游戏在跑检测把进程名配成
当前解释器过真路径（单测配置）；"游戏没跑"用查不到的进程名触发。配置一律写临时
config.toml 再加载，不碰真机 config.toml。新年判定直接调方法（节拍归主体，主体的
节拍在 test_main 的完整顺序里过）。
"""

import sys
from pathlib import Path

from sample import EXPECTED_SNAPSHOT, FIXTURE

from config import Config, load_config
from game.impl.module import GameModuleImpl, GameNotRunningError

# 真实格式的本局记录行（两年各一条，供年度通知测试模拟游戏内过一年）
LINE_1836 = "[t][e.cpp:1]: vic3-GreatBritain state tag=GBR year=12月 27, 1836 rank=1 gdp=1.0 army=10"
LINE_1837 = "[t][e.cpp:1]: vic3-GreatBritain state tag=GBR year=12月 27, 1837 rank=1 gdp=2.0 army=20"


def make_config(tmp_path: Path, log_path: Path, game_process: str) -> Config:
    """临时 config.toml → Config：单测用的小配置，指定日志路径与游戏进程名。"""
    toml = tmp_path / "config.toml"
    toml.write_text(
        f"log_path = '{log_path}'\ngame_process = '{game_process}'\n", encoding="utf-8"
    )
    return load_config(toml)


def test_get_state_reads_sample_log_snapshot(tmp_path):
    # 构造：配置指向真实格式样例，进程名配成当前解释器（过游戏在跑检测）
    config = make_config(tmp_path, FIXTURE, Path(sys.executable).name)
    module = GameModuleImpl(config)
    # 调用
    snapshot = module.get_state()
    # 校验
    assert snapshot == EXPECTED_SNAPSHOT


def test_get_state_returns_empty_when_log_missing(tmp_path):
    config = make_config(tmp_path, tmp_path / "no-such.log", Path(sys.executable).name)
    assert GameModuleImpl(config).get_state() == {"powers": [], "gbr_finance": None}


def test_get_state_raises_when_game_not_running(tmp_path):
    config = make_config(tmp_path, FIXTURE, "no-such-game.exe")
    module = GameModuleImpl(config)
    try:
        module.get_state()
    except GameNotRunningError as e:
        assert "游戏未启动" in str(e)
        assert "no-such-game.exe" in str(e)
    else:
        raise AssertionError("游戏没跑时 get_state 应报 GameNotRunningError")


def test_start_play_returns_fixed_not_implemented_response(tmp_path):
    config = make_config(tmp_path, FIXTURE, Path(sys.executable).name)
    response = GameModuleImpl(config).start_play()
    assert "未实现" in response


def test_check_new_year_returns_current_year_then_new_year(tmp_path):
    # 构造：日志先有 1836 记录，进程名配成当前解释器（过游戏在跑检测）
    log = tmp_path / "error.log"
    log.write_text(LINE_1836 + "\n", encoding="utf-8")
    config = make_config(tmp_path, log, Path(sys.executable).name)
    module = GameModuleImpl(config)
    # 首查：日志里已有 1836 记录，察觉即返回 1836（主体拿到会推事件）
    assert module.check_new_year() == 1836
    # 游戏内过一年：日志追加 1837 记录，再查返回 1837
    log.write_text(LINE_1836 + "\n" + LINE_1837 + "\n", encoding="utf-8")
    assert module.check_new_year() == 1837
    # 没有再新的年份：返回 None
    assert module.check_new_year() is None


def test_check_new_year_returns_none_when_game_not_running(tmp_path):
    # 构造：日志有 1836 记录，但进程名查不到（游戏没跑）
    log = tmp_path / "error.log"
    log.write_text(LINE_1836 + "\n", encoding="utf-8")
    config = make_config(tmp_path, log, "no-such-game.exe")
    module = GameModuleImpl(config)
    # 游戏没跑：读到的是上次留下的旧日志，不当作新年，返回 None（年份已记下，
    # 游戏启动后也不会把 1836 当新年推）
    assert module.check_new_year() is None
    assert module.check_new_year() is None
