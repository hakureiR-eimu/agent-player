# -*- coding: utf-8 -*-
"""兜底：仍缺的 zh 文件用英文原版填充，front matter 标注被风控拦截、保留英文。
保证 629 个文件齐全、站内链接全部可解析。用法：python scripts/vic3-wiki/fill_blocked.py
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "游戏wiki" / "vic3-wiki-en"
DST = ROOT / "游戏wiki" / "vic3-wiki-zh"
TODAY = "2026-10-28"

INJECT = f"translated: {TODAY}\ntranslator: kept-english (translation blocked by content filter)\n"

filled = []
for p in sorted(SRC.glob("*.md")):
    dst = DST / p.name
    if dst.exists():
        continue
    raw = p.read_text(encoding="utf-8")
    if raw.startswith("---\n"):
        end = raw.find("\n---\n", 4)
        out = raw[:4] + INJECT + raw[4:]
    else:
        out = INJECT + raw
    dst.write_text(out, encoding="utf-8")
    filled.append(p.name)

print(f"filled {len(filled)} files with English originals:")
for n in filled:
    print(" -", n)
