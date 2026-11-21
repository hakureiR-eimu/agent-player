"""game 模块测试的公共样例：真实格式样例日志的路径与期望快照。

样例（fixtures/error.log）是 docs/调研/debug-log/error-2026-11-21.log 的原样拷贝
（普通模式跑两年、1836/1837 各 17 行记录）；期望快照从样例里的记录行手工整理——
每国最新一条都是 1837 年，按 rank 升序。换新的样例拷贝时，这份期望值要跟着
样例里的记录行同步改。
"""

from pathlib import Path

FIXTURE = Path(__file__).parent / "fixtures" / "error.log"

EXPECTED_SNAPSHOT = {
    "powers": [
        {"tag": "GBR", "year": 1837, "rank": 1, "gdp": 31386151.21408, "army": 137},
        {"tag": "RUS", "year": 1837, "rank": 2, "gdp": 23581644.84988, "army": 200},
        {"tag": "FRA", "year": 1837, "rank": 3, "gdp": 23031776.88604, "army": 249},
        {"tag": "AUS", "year": 1837, "rank": 4, "gdp": 11111469.40332, "army": 199},
        {"tag": "USA", "year": 1837, "rank": 5, "gdp": 19927420.9914, "army": 122},
        {"tag": "TUR", "year": 1837, "rank": 6, "gdp": 10800674.95312, "army": 140},
        {"tag": "PRU", "year": 1837, "rank": 7, "gdp": 9996669.6804, "army": 129},
        {"tag": "NET", "year": 1837, "rank": 8, "gdp": 2683345.81944, "army": 30},
        {"tag": "SWE", "year": 1837, "rank": 9, "gdp": 2399761.637, "army": 39},
        {"tag": "SPA", "year": 1837, "rank": 10, "gdp": 6987073.40292, "army": 71},
        {"tag": "BRZ", "year": 1837, "rank": 11, "gdp": 6086653.96144, "army": 41},
        {"tag": "SIC", "year": 1837, "rank": 12, "gdp": 4433705.72892, "army": 52},
        {"tag": "CHI", "year": 1837, "rank": 13, "gdp": 91705904.32796, "army": 555},
        {"tag": "JAP", "year": 1837, "rank": 14, "gdp": 12089963.92552, "army": 78},
        {"tag": "SIA", "year": 1837, "rank": 15, "gdp": 1361335.05248, "army": 58},
        {"tag": "PAN", "year": 1837, "rank": 16, "gdp": 3465655.45976, "army": 81},
    ],
    "gbr_finance": {"year": 1837, "gold": 209685.76327, "debt": 0, "week_net": 36978.43184},
}
