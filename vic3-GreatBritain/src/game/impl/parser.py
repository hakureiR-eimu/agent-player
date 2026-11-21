"""error.log 解析（行格式见 docs/prd/游戏接入-mod侧.md，两侧以行格式为交接面）。

纯函数：一行日志 → 记录 dict；整份日志文本 → 世界格局快照。
"""

from __future__ import annotations

import re

PREFIX = "vic3-GreatBritain "

# 两类记录的必填字段（封闭清单，行格式以 mod 侧文档为准）
_REQUIRED = {
    "state": ("tag", "year", "rank", "gdp", "army"),
    "fin": ("tag", "year", "gold", "debt", "week_net"),
}
_INT_FIELDS = {"rank", "army"}
_FLOAT_FIELDS = {"gdp", "gold", "debt", "week_net"}

# year 的值是完整本地化日期（如 "12月 27, 1837"，含空格逗号），从值尾取 4 位数字
_TAIL_YEAR = re.compile(r"(\d{4})\s*$")
# 按字段名切 key=value 对：值里可以带空格逗号，遇到"空格＋新字段名="才切
_FIELD_SPLIT = re.compile(r"\s+(?=[A-Za-z_][A-Za-z0-9_]*=)")


def parse_record(line: str) -> dict | None:
    """一行日志 → 记录 dict；非本局行或解析不出（残行）返回 None。

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

    record: dict = {"kind": kind}
    for key, value in fields.items():
        if key == "tag":
            record["tag"] = value
        elif key == "year":
            found = _TAIL_YEAR.search(value)
            if not found:
                return None
            record["year"] = int(found.group(1))
        elif key in _INT_FIELDS:
            try:
                record[key] = int(value)
            except ValueError:
                return None
        elif key in _FLOAT_FIELDS:
            try:
                record[key] = float(value)
            except ValueError:
                return None
    if any(key not in record for key in _REQUIRED[kind]):
        return None
    return record


def build_snapshot(text: str) -> dict:
    """整份日志文本 → 读取世界局势的快照。

    同一 (tag, year) 后出现的覆盖先出现的（读档重跑以最新一次为准）；
    每国取最新一条；powers 按行内 rank 升序（可能并列，保持文件顺序）。
    """
    states: dict[tuple[str, int], dict] = {}
    fins: dict[int, dict] = {}
    for line in text.splitlines():
        record = parse_record(line)
        if record is None:
            continue
        if record["kind"] == "state":
            states[(record["tag"], record["year"])] = record
        else:
            fins[record["year"]] = record

    latest: dict[str, dict] = {}
    for (tag, year), record in states.items():
        if tag not in latest or year > latest[tag]["year"]:
            latest[tag] = record

    return {
        "powers": [
            {key: record[key] for key in ("tag", "year", "rank", "gdp", "army")}
            for record in sorted(latest.values(), key=lambda r: r["rank"])
        ],
        "gbr_finance": (
            {key: fins[max(fins)][key] for key in ("year", "gold", "debt", "week_net")}
            if fins
            else None
        ),
    }
