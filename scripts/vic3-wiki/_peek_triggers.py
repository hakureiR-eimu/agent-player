# -*- coding: utf-8 -*-
"""对比 参考资料/ 磁盘文件与 git 已跟踪文件，找出未提交的内容。"""
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
REF = ROOT / "参考资料"

# 磁盘上的全部文件（相对路径，统一 / 分隔）
disk = set()
for p in REF.rglob("*"):
    if p.is_file():
        disk.add(p.relative_to(ROOT).as_posix())
print(f"磁盘文件总数（参考资料/ 递归）: {len(disk)}")

# git 已跟踪
out = subprocess.run(
    ["git", "ls-files", "--", "参考资料"],
    cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout
tracked = set(x for x in out.split("\n") if x.strip())
print(f"git 已跟踪: {len(tracked)}")

untracked = sorted(disk - tracked)
extra = sorted(tracked - disk)
print(f"\n磁盘上有、git 没有（未提交）: {len(untracked)} 个")
for x in untracked[:60]:
    print("  ", x)
print(f"\ngit 有、磁盘没有: {len(extra)} 个")
for x in extra[:20]:
    print("  ", x)

# git status 角度再看一遍（含 ignored）
st = subprocess.run(
    ["git", "status", "--porcelain", "--ignored", "--", "参考资料"],
    cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout
lines = [l for l in st.split("\n") if l.strip()]
print(f"\ngit status（含 ignored）非空行: {len(lines)}")
for l in lines[:40]:
    print("  ", l)
