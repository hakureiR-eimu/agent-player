# -*- coding: utf-8 -*-
"""快照当前 zh 版状态：kept-english 文件、含未翻译标记的文件、translator 统计。"""
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
zh = Path(__file__).resolve().parents[2] / "游戏wiki" / "vic3-wiki-zh"

kept, untr, translators = [], [], Counter()
for p in sorted(zh.glob("*.md")):
    txt = p.read_text(encoding="utf-8")
    if "kept-english" in txt[:600]:
        kept.append(p.name)
    if "untranslated: blocked" in txt:
        untr.append(p.name)
    for line in txt.split("\n", 15):
        if line.startswith("translator:"):
            translators[line.strip()] += 1
            break

print("== kept-english files:", len(kept))
print("\n".join("  " + n for n in kept))
print("== files with untranslated markers:", len(untr))
print("\n".join("  " + n for n in untr))
print("== translator lines:")
for k, v in translators.most_common():
    print(f"  {v:4d}  {k}")
