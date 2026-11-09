# -*- coding: utf-8 -*-
"""快速盘点 vic3-wiki-zh 的翻译状态：kept-english（风控拦截未翻）与已翻译文件统计。"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
DST = ROOT / "参考资料" / "vic3-wiki-zh"
CACHE = ROOT / ".cache" / "vic3-wiki-zh"

print("cache exists:", CACHE.exists())
if CACHE.exists():
    for p in sorted(CACHE.iterdir()):
        if p.is_dir():
            print(f"  dir   {p.name}: {len(list(p.iterdir()))} items")
        else:
            print(f"  file  {p.name}: {p.stat().st_size:,} bytes")

kept, translated, other = [], [], []
CJK = re.compile(r"[\u4e00-\u9fff]")
for f in sorted(DST.glob("*.md")):
    head = f.read_text(encoding="utf-8")[:600]
    if "kept-english" in head:
        kept.append(f.name)
    elif "translator:" in head:
        translated.append(f.name)
    else:
        other.append(f.name)

print(f"\nzh md 总数: {len(list(DST.glob('*.md')))}")
print(f"已翻译(translator 标记): {len(translated)}")
print(f"kept-english(风控未翻): {len(kept)}")
for n in kept:
    print("   -", n)
print(f"无 translator 标记: {len(other)}")
for n in other[:20]:
    print("   -", n)

# 失败块统计
bc = CACHE / "blocked-chunks"
if bc.exists():
    fails = list(bc.glob("*.fail*"))
    print(f"\nblocked-chunks: {len(list(bc.glob('*.json')))} chunks, fail 标记 {len(fails)}")
