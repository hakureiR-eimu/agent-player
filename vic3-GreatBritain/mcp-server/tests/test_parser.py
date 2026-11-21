"""解析与快照组装的单测：行识别、行尾混存、残行、去重、每国最新、排序、空数据。

真实样例（fixtures/error.log，拷自 docs/调研/debug-log/error-2026-11-21.log）覆盖：
真实加头、LF/CRLF 混存、与原版错误输出混杂、两年数据；去重/残行等边界用内联样例。
"""

import server
from conftest import EXPECTED_SNAPSHOT, FIXTURE

STATE_LINE = (
    "[10:04:58][jomini_effect_impl.cpp:475]: common/scripted_effects/gb_agent_effects.txt:14: "
    "vic3-GreatBritain state tag=FRA year=12月 27, 1836 rank=3 gdp=23460462.61572 army=253"
)
FIN_LINE = (
    "[10:04:59][jomini_effect_impl.cpp:475]: common/scripted_effects/gb_agent_effects.txt:20: "
    "vic3-GreatBritain fin tag=GBR year=12月 31, 1836 gold=176001.99175 debt=0 week_net=-21660.22135"
)
NOISE_LINE = (
    "[23:22:25][jomini_effect.cpp:160]: Adding effect after PostInitAndValidate, "
    "unless this is handled by filewatcher reload, it will not be validated."
)


def test_国家行按字段名解析():
    assert server.parse_record(STATE_LINE) == {
        "kind": "state",
        "tag": "FRA",
        "year": 1836,
        "rank": 3,
        "gdp": 23460462.61572,
        "army": 253,
    }


def test_财政行按字段名解析():
    assert server.parse_record(FIN_LINE) == {
        "kind": "fin",
        "tag": "GBR",
        "year": 1836,
        "gold": 176001.99175,
        "debt": 0.0,
        "week_net": -21660.22135,
    }


def test_原版噪音行不认():
    assert server.parse_record(NOISE_LINE) is None


def test_带局名的非记录行不认():
    line = "[23:22:26][game/modloader.cpp:318]: Loaded mod: vic3-GreatBritain (user directory)"
    assert server.parse_record(line) is None


def test_残行不认():
    # 末尾截断：日期没落全
    assert server.parse_record("[t]: vic3-GreatBritain fin tag=GBR year=12月 3") is None
    # 字段没落全
    assert server.parse_record("[t]: vic3-GreatBritain state tag=FRA year=12月 27, 18") is None
    assert server.parse_record("[t]: vic3-GreatBritain state tag=FRA") is None


def test_年份从日期值尾取():
    line = "[t]: vic3-GreatBritain state tag=MEX year=1月 1, 1840 rank=5 gdp=1.0 army=1"
    assert server.parse_record(line)["year"] == 1840


def test_记录行LF与引擎行CRLF混存():
    text = (
        "[t][e.cpp:1]: engine line\r\n"
        "[t][e.cpp:1]: vic3-GreatBritain state tag=FRA year=12月 27, 1837 rank=3 gdp=1.0 army=10\n"
        "[t][e.cpp:1]: vic3-GreatBritain fin tag=GBR year=12月 31, 1837 gold=1.0 debt=2.0 week_net=3.0\n"
        "[t][e.cpp:1]: engine line\r\n"
    )
    assert server.build_snapshot(text) == {
        "powers": [{"tag": "FRA", "year": 1837, "rank": 3, "gdp": 1.0, "army": 10}],
        "gbr_finance": {"year": 1837, "gold": 1.0, "debt": 2.0, "week_net": 3.0},
    }


def test_同年重复后一条覆盖():
    text = "\r\n".join(
        [
            "[t]: vic3-GreatBritain state tag=FRA year=12月 27, 1837 rank=3 gdp=1.0 army=10",
            "[t]: vic3-GreatBritain state tag=FRA year=12月 27, 1837 rank=3 gdp=2.0 army=20",
        ]
    )
    snapshot = server.build_snapshot(text)
    assert snapshot["powers"] == [
        {"tag": "FRA", "year": 1837, "rank": 3, "gdp": 2.0, "army": 20}
    ]


def test_每国取最新一条():
    text = "\r\n".join(
        [
            "[t]: vic3-GreatBritain state tag=FRA year=12月 27, 1836 rank=3 gdp=1.0 army=10",
            "[t]: vic3-GreatBritain state tag=FRA year=12月 27, 1837 rank=3 gdp=2.0 army=20",
            "[t]: vic3-GreatBritain state tag=GBR year=1月 03, 1837 rank=1 gdp=3.0 army=30",
        ]
    )
    snapshot = server.build_snapshot(text)
    assert [power["tag"] for power in snapshot["powers"]] == ["GBR", "FRA"]
    assert snapshot["powers"][1]["year"] == 1837


def test_当年未触发的国家落在上一年():
    # GBR 只有 1836 年的行（1837 还没触发），快照里它带着 1836 的记录
    text = "\r\n".join(
        [
            "[t]: vic3-GreatBritain state tag=GBR year=12月 31, 1836 rank=1 gdp=1.0 army=10",
            "[t]: vic3-GreatBritain state tag=FRA year=12月 27, 1837 rank=3 gdp=2.0 army=20",
        ]
    )
    snapshot = server.build_snapshot(text)
    assert snapshot["powers"][0] == {
        "tag": "GBR", "year": 1836, "rank": 1, "gdp": 1.0, "army": 10
    }


def test_财政取最新一年():
    text = "\r\n".join(
        [
            "[t]: vic3-GreatBritain fin tag=GBR year=12月 31, 1836 gold=1.0 debt=2.0 week_net=-3.0",
            "[t]: vic3-GreatBritain fin tag=GBR year=12月 31, 1837 gold=4.0 debt=5.0 week_net=6.0",
        ]
    )
    assert server.build_snapshot(text)["gbr_finance"] == {
        "year": 1837,
        "gold": 4.0,
        "debt": 5.0,
        "week_net": 6.0,
    }


def test_没有本局记录返回空():
    assert server.build_snapshot(NOISE_LINE + "\r\n" + NOISE_LINE) == {
        "powers": [],
        "gbr_finance": None,
    }


def test_真实样例日志整文件解析():
    assert server.build_snapshot(FIXTURE.read_text(encoding="utf-8")) == EXPECTED_SNAPSHOT
