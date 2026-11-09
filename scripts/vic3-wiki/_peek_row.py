# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
raw = Path(r"D:\work\game-agent\参考资料\vic3-wiki-en\Altai.md").read_text(encoding="utf-8")
print("file len:", len(raw))
for i, line in enumerate(raw.split("\n")):
    if "Releasable" in line:
        print(f"line {i} len={len(line)}:")
        print(line[:2000])
        print("...")
        print(line[-400:])
        break
else:
    print("no Releasable line found")

# 已译页 H1 格式
zh = Path(r"D:\work\game-agent\参考资料\vic3-wiki-zh\China.md").read_text(encoding="utf-8")
print("\n--- zh China.md head ---")
print(zh[:400])
en = Path(r"D:\work\game-agent\参考资料\vic3-wiki-en\China.md").read_text(encoding="utf-8")
print("--- en China.md head ---")
print(en[:300])
