# -*- coding: utf-8 -*-
"""从已翻译语料构建翻译记忆库（TM）与双语名称词典，供 translate_dict.py 离线补翻使用。

对每个已机器翻译的文件：en/zh 逐行对齐——带链接/图片的行按结构签名唯一匹配做锚点，
无链接短行用前后锚点等距定位；行对全语料投票去噪。链接显示文本按目标配对收割名称词典。

产出 .cache/vic3-wiki-zh/tm.json：
  lines: {en行: [zh行, 票数]}
  names: {en链接显示名: [zh显示名, 票数]}
用法：python scripts/vic3-wiki/build_tm.py
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "游戏wiki" / "vic3-wiki-en"
DST = ROOT / "游戏wiki" / "vic3-wiki-zh"
OUT = ROOT / ".cache" / "vic3-wiki-zh" / "tm.json"

LINKFULL_RE = re.compile(r"!?\[[^\]]*\]\(([^)\n]*)\)")
FENCE_RE = re.compile(r"^\s*```")
HEAD_RE = re.compile(r"^#{1,6}\s")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")


def split_front_matter(text):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[: end + 5], text[end + 5:]
    return "", text


def signature(line):
    targets = tuple(sorted(LINKFULL_RE.findall(line)))
    return targets, len(re.findall(r"!\[", line)), bool(FENCE_RE.match(line)), bool(HEAD_RE.match(line))


def align_file(en_body, zh_body):
    """返回 [(en行, zh行)]，只含可信配对。"""
    en_lines, zh_lines = en_body.split("\n"), zh_body.split("\n")
    # 跳过围栏内部行（代码，en/zh 相同，且会干扰锚点距离）
    def mark_fences(lines):
        keep, in_fence = [], False
        for idx, ln in enumerate(lines):
            if FENCE_RE.match(ln):
                in_fence = not in_fence
                keep.append(False)
            else:
                keep.append(not in_fence)
        return keep

    en_ok, zh_ok = mark_fences(en_lines), mark_fences(zh_lines)
    pairs = []

    # 锚点：带链接/图片且结构签名在本文件内唯一
    en_sig = {}
    for i, ln in enumerate(en_lines):
        if en_ok[i]:
            sig = signature(ln)
            if (sig[0] or sig[1]) and not sig[2]:
                en_sig.setdefault(sig, []).append(i)
    zh_sig = {}
    for j, ln in enumerate(zh_lines):
        if zh_ok[j]:
            sig = signature(ln)
            if (sig[0] or sig[1]) and not sig[2]:
                zh_sig.setdefault(sig, []).append(j)

    anchors = []  # (en_idx, zh_idx)
    for sig, idxs in en_sig.items():
        js = zh_sig.get(sig)
        if js and len(idxs) == 1 and len(js) == 1:
            anchors.append((idxs[0], js[0]))

    # 恒等锚：段内 en==zh 的模板/符号行（Template:…、|---|、版本号）按出现顺序互相配对，
    # 修正译文区行数漂移导致的等距错位
    en_queues, zh_queues = defaultdict(list), defaultdict(list)
    for i, ln in enumerate(en_lines):
        if en_ok[i] and ln.strip() and not signature(ln)[0]:
            en_queues[ln.rstrip()].append(i)
    for j, ln in enumerate(zh_lines):
        if zh_ok[j] and ln.strip() and not signature(ln)[0]:
            zh_queues[ln.rstrip()].append(j)
    for text, iq in en_queues.items():
        jq = zh_queues.get(text)
        if jq:
            for k in range(min(len(iq), len(jq))):
                anchors.append((iq[k], jq[k]))
    anchors = sorted(set(anchors))

    def plausible(a, b):
        # 译值必须含中文，或与原文一致（未翻译的模板行）；纯符号行按原样
        return b == a or CJK_RE.search(b) or not re.search(r"[A-Za-z]", a)

    for i, j in anchors:
        pairs.append((en_lines[i].rstrip(), zh_lines[j].rstrip()))

    # 无链接行：前后锚点等距定位（含起始段：前锚点取文件头）
    bounds = [(-1, -1)] + anchors + [(len(en_lines), len(zh_lines))]
    for b in range(len(bounds) - 1):
        (pe, pz), (ne, nz) = bounds[b], bounds[b + 1]
        if ne - pe != nz - pz:
            continue  # 锚点间行数不一致（翻译并/拆了行），放弃本段
        for i in range(pe + 1, ne):
            j = i - pe + pz
            if not en_ok[i] or not zh_ok[j]:
                continue
            a, z = en_lines[i].rstrip(), zh_lines[j].rstrip()
            if plausible(a, z):
                pairs.append((a, z))
    return pairs


def harvest_names(en_line, zh_line):
    """按链接目标配对收割显示名翻译。"""
    out = []
    en_links = [(m.group(2), m.group(1)) for m in re.finditer(r"(!?\[[^\]]*\])\(([^)\n]*)\)", en_line)]
    zh_links = [(m.group(2), m.group(1)) for m in re.finditer(r"(!?\[[^\]]*\])\(([^)\n]*)\)", zh_line)]
    zh_by_target = {}
    for tgt, disp in zh_links:
        zh_by_target.setdefault(tgt, []).append(disp)
    used = Counter()
    for tgt, disp in en_links:
        js = zh_by_target.get(tgt)
        if not js:
            continue
        k = used[tgt]
        if k < len(js):
            out.append((disp.strip("![]"), js[k].strip("![]")))
            used[tgt] += 1
    return out


def main():
    line_votes = {}
    name_votes = {}
    n_files = 0
    for en_path in sorted(SRC.glob("*.md")):
        zh_path = DST / en_path.name
        if not zh_path.exists():
            continue
        zh_raw = zh_path.read_text(encoding="utf-8")
        if "kept-english" in zh_raw[:600]:
            continue
        en_body = split_front_matter(en_path.read_text(encoding="utf-8"))[1]
        zh_body = split_front_matter(zh_raw)[1]
        n_files += 1
        for a, b in align_file(en_body, zh_body):
            if a == b or "untranslated: blocked" in b:
                continue
            line_votes.setdefault(a, Counter())[b] += 1
            for ne, nz in harvest_names(a, b):
                name_votes.setdefault(ne, Counter())[nz] += 1

    tm_lines = {k: [v.most_common(1)[0][0], sum(v.values())] for k, v in line_votes.items() if k.strip()}
    tm_names = {k: [v.most_common(1)[0][0], sum(v.values())] for k, v in name_votes.items() if k.strip()}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"lines": tm_lines, "names": tm_names}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"对齐 {n_files} 个已译文件；TM 行条目 {len(tm_lines)}，名称词条 {len(tm_names)} → {OUT}")


if __name__ == "__main__":
    main()
