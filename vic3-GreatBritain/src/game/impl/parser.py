"""error.log 解析（行格式见 docs/prd/游戏接入-mod侧.md，两侧以行格式为交接面）。

纯函数：一行日志 → 记录 dict；整份日志文本 → 世界格局快照。
"""

from __future__ import annotations

import re
from typing import Literal, TypedDict

from game.module import GbrFinance, Power, WorldSnapshot

PREFIX = "vic3-GreatBritain "


class StateRecord(TypedDict):
    """state 记录：一国的格局。"""

    kind: Literal["state"]
    tag: str
    year: int
    rank: int
    gdp: float
    army: int


class FinRecord(TypedDict):
    """fin 记录：大不列颠的财政。"""

    kind: Literal["fin"]
    tag: str
    year: int
    gold: float
    debt: float
    week_net: float

# 两类记录的必填字段（封闭清单，行格式以 mod 侧文档为准）
_REQUIRED = {
    "state": ("tag", "year", "rank", "gdp", "army"),
    "fin": ("tag", "year", "gold", "debt", "week_net"),
}

# year 的值是完整本地化日期（如 "12月 27, 1837"，含空格逗号），从值尾取 4 位数字
_TAIL_YEAR = re.compile(r"(\d{4})\s*$")
# 按字段名切 key=value 对：值里可以带空格逗号，遇到"空格＋新字段名="才切
_FIELD_SPLIT = re.compile(r"\s+(?=[A-Za-z_][A-Za-z0-9_]*=)")


def parse_record(line: str) -> StateRecord | FinRecord | None:
    """一行日志 → 记录；非本局行或解析不出（残行）返回 None。

    行首有游戏加的 [墙钟时间][来源文件:行号]: 头，本局记录按行内前缀认，
    前缀出现在别处（如原版日志提到 mod 名）的行不认。
    """
    idx = line.find(PREFIX)
    if idx < 0:
        return None
    tokens = _FIELD_SPLIT.split(line[idx + len(PREFIX):].strip())
    kind = tokens[0]
    if kind not in _REQUIRED:
        return None
    fields: dict[str, str] = {}
    for token in tokens[1:]:
        key, sep, value = token.partition("=")
        if not sep or not key or not value:
            return None
        fields[key] = value
    if any(key not in fields for key in _REQUIRED[kind]):
        return None

    found = _TAIL_YEAR.search(fields["year"])
    if found is None:
        return None
    year = int(found.group(1))
    if kind == "state":
        try:
            return StateRecord(
                kind="state",
                tag=fields["tag"],
                year=year,
                rank=int(fields["rank"]),
                gdp=float(fields["gdp"]),
                army=int(fields["army"]),
            )
        except ValueError:
            return None
    try:
        return FinRecord(
            kind="fin",
            tag=fields["tag"],
            year=year,
            gold=float(fields["gold"]),
            debt=float(fields["debt"]),
            week_net=float(fields["week_net"]),
        )
    except ValueError:
        return None


def build_snapshot(text: str) -> WorldSnapshot:
    """整份日志文本 → 读取世界局势的快照。

    同一 (tag, year) 后出现的覆盖先出现的（读档重跑以最新一次为准）；
    每国取最新一条；powers 按行内 rank 升序（可能并列，保持文件顺序）。
    """
    states: dict[tuple[str, int], StateRecord] = {}
    fins: dict[int, FinRecord] = {}
    for line in text.splitlines():
        record = parse_record(line)
        if record is None:
            continue
        if record["kind"] == "state":
            states[(record["tag"], record["year"])] = record
        else:
            fins[record["year"]] = record

    latest: dict[str, StateRecord] = {}
    for (tag, year), record in states.items():
        if tag not in latest or year > latest[tag]["year"]:
            latest[tag] = record

    newest_fin = fins[max(fins)] if fins else None
    return WorldSnapshot(
        powers=[
            Power(
                tag=record["tag"],
                year=record["year"],
                rank=record["rank"],
                gdp=record["gdp"],
                army=record["army"],
            )
            for record in sorted(latest.values(), key=lambda r: r["rank"])
        ],
        gbr_finance=(
            GbrFinance(
                year=newest_fin["year"],
                gold=newest_fin["gold"],
                debt=newest_fin["debt"],
                week_net=newest_fin["week_net"],
            )
            if newest_fin is not None
            else None
        ),
    )
