# -*- coding: utf-8 -*-
"""全量校验 vic3-wiki-zh：对照英文源逐文件检查结构保真度。

检查项：文件数一致、front matter 完整（title/source/pageid/fetched 四字段与源一致）、
代码围栏数、图片数、链接目标集合、标题数、中文占比、残留链接占位符 {#n}、已知笔误。
用法：python scripts/vic3-wiki/verify_zh.py
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "游戏wiki" / "vic3-wiki-en"
DST = ROOT / "游戏wiki" / "vic3-wiki-zh"

FENCE_RE = re.compile(r"^\s*```")
IMG_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]*)\)")
HEAD_RE = re.compile(r"^#{1,6}\s")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
ASCII_WORD_RE = re.compile(r"[A-Za-z]")


def stats(text):
    return {
        "fences": len([l for l in text.split("\n") if FENCE_RE.match(l)]),
        "imgs": len(IMG_RE.findall(text)),
        "links": sorted(LINK_RE.findall(text)),
        "heads": len([l for l in text.split("\n") if HEAD_RE.match(l)]),
    }


def main():
    src_files = {p.name for p in SRC.glob("*.md")}
    dst_files = {p.name for p in DST.glob("*.md")}
    missing = sorted(src_files - dst_files)
    extra = sorted(dst_files - src_files)
    print(f"源 {len(src_files)} 个 md，译文 {len(dst_files)} 个；缺失 {len(missing)}，多余 {len(extra)}")
    if missing:
        print("  缺失:", missing[:20], "..." if len(missing) > 20 else "")

    bad = []
    n_checked = 0
    for name in sorted(src_files & dst_files):
        s = (SRC / name).read_text(encoding="utf-8")
        d = (DST / name).read_text(encoding="utf-8")
        problems = []
        for key in ("title:", "source:", "pageid:", "fetched:"):
            sv = re.search(rf"^{key}.*$", s, re.M)
            dv = re.search(rf"^{key}.*$", d, re.M)
            if (sv is None) != (dv is None) or (sv and dv and sv.group(0) != dv.group(0)):
                problems.append(f"front matter {key} 不一致")
        ss, ds = stats(s), stats(d)
        if ss["fences"] != ds["fences"]:
            problems.append(f"围栏 {ss['fences']}→{ds['fences']}")
        if ss["imgs"] != ds["imgs"]:
            problems.append(f"图片 {ss['imgs']}→{ds['imgs']}")
        if ss["links"] != ds["links"]:
            lost = [x for x in ss["links"] if x not in ds["links"]][:3]
            add = [x for x in ds["links"] if x not in ss["links"]][:3]
            problems.append(f"链接 丢{lost} 多{add}")
        if ss["heads"] != ds["heads"]:
            problems.append(f"标题 {ss['heads']}→{ds['heads']}")
        if re.search(r"\{#\d+\}", d):
            problems.append("残留 {#n} 占位符")
        if len(ASCII_WORD_RE.findall(s)) > 500 and len(CJK_RE.findall(d)) < 0.1 * len(ASCII_WORD_RE.findall(s)):
            problems.append("提示:中文占比低（纯数据/标识符页属正常）")
        if "权力力" in d:
            problems.append("笔误 权力力")
        n_checked += 1
        if problems:
            bad.append((name, problems))
    print(f"逐文件检查 {n_checked} 个，异常 {len(bad)} 个")
    for name, probs in bad[:40]:
        print(f"  {name}: {'; '.join(probs)}")
    if len(bad) > 40:
        print(f"  ……共 {len(bad)} 个")


if __name__ == "__main__":
    main()
