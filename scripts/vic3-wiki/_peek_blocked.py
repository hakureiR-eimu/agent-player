# -*- coding: utf-8 -*-
"""查看 blocked-chunks 缓存里仍保留英文的片段，定位触发风控的词。"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
CD = ROOT / ".cache" / "vic3-wiki-zh" / "blocked-chunks"

for p in sorted(CD.glob("*.json")):
    cache = json.loads(p.read_text(encoding="utf-8"))
    for i, c in enumerate(cache.get("chunks", [])):
        if c and c.get("en"):
            text = c["text"]
            # 提取保留英文的片段（去掉标记行后看看内容）
            frag = text.split("<!-- untranslated: blocked by content filter -->")
            for f in frag[1:]:
                f = f.strip()[:400]
                print(f"### {p.name} chunk{i} ({c.get('en_chars')} chars):")
                print(f)
                print()
