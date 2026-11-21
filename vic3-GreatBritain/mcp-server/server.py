"""vic3-GreatBritain 局的 MCP server（读侧第一版）。

把 mod 写进 error.log 的年度记录（行格式见 docs/prd/游戏接入-mod侧.md，两侧以
行格式为交接面）暴露成两个 MCP 工具：

- get_state：读最新世界格局快照（各国最新一条国家行按名次排序＋大不列颠最新财政行）
- start_play：发起外交博弈（写侧占位，返回固定的"未实现"应答）

两个工具都以游戏在跑为前提：按进程名查进程表，游戏没启动直接报错、不读日志。

配置（环境变量，均可省略）：
  VIC3_MCP_LOG_DIR       日志目录，默认 ~/Documents/Paradox Interactive/Victoria 3/logs
  VIC3_MCP_LOG_FILE      日志文件名，默认 error.log
  VIC3_MCP_GAME_PROCESS  游戏进程名，默认 victoria3.exe

运行：python server.py（stdio 传输，客户端按常规 MCP 服务挂载）。
"""

from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path

from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

mcp = MCPServer("vic3-GreatBritain")

PREFIX = "vic3-GreatBritain "
DEFAULT_GAME_PROCESS = "victoria3.exe"

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


def log_path() -> Path:
    log_dir = os.environ.get("VIC3_MCP_LOG_DIR")
    if log_dir is None:
        log_dir = Path.home() / "Documents" / "Paradox Interactive" / "Victoria 3" / "logs"
    return Path(log_dir) / os.environ.get("VIC3_MCP_LOG_FILE", "error.log")


def game_process() -> str:
    return os.environ.get("VIC3_MCP_GAME_PROCESS", DEFAULT_GAME_PROCESS)


def game_running(process: str) -> bool:
    """按进程名查进程表，判断游戏是否已启动。"""
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


def require_game() -> None:
    process = game_process()
    if not game_running(process):
        raise ToolError(f"游戏未启动：进程表里没有 {process}，先启动 Victoria 3 再调用工具")


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
    """整份日志文本 → get_state 的快照。

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


@mcp.tool()
def get_state() -> dict:
    """读游戏最新世界格局快照：列强（通常 16 国）各国最新一条年度记录，含
    tag/年份/名次/GDP/营队数，按名次升序；附大不列颠最新财政（金库/债务本金/
    每周净收支）。游戏未启动时报错；游戏第一年还没导出过记录时返回空。"""
    require_game()
    try:
        text = log_path().read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return {"powers": [], "gbr_finance": None}
    return build_snapshot(text)


@mcp.tool()
def start_play() -> str:
    """发起外交博弈（写侧工具，实现空置）：随写侧版本补，当前调用返回固定的
    "未实现"应答。游戏未启动时同样报错。"""
    require_game()
    return "未实现：start_play 是写侧工具，随写侧版本补，当前只读。"


if __name__ == "__main__":
    mcp.run()
