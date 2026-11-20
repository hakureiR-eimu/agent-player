# -*- coding: utf-8 -*-
"""补翻被内容风控拦截的页面（translate_to_zh.py 的接力者，独立实现）。

目标自动发现：游戏wiki/vic3-wiki-zh/ 里 front matter 带 `translator: kept-english` 的文件。
级联策略（逐块，一个模型被 1301 拦就换下一个）：
    glm-4.7 → glm-4.6 → glm-4.5-air → glm-5.3 → glm-4.7(精简提示词，不带术语表)
保真机制：链接目标 {#n} 占位符还原、多余链接降级、围栏/图片/链接/标题计数校验、带反馈重试。

用法：
    python scripts/vic3-wiki/translate_blocked.py               # 全部 47 页
    python scripts/vic3-wiki/translate_blocked.py --only China.md,Culture.md
    python scripts/vic3-wiki/translate_blocked.py --workers 4 --chunk-chars 12000
"""
import argparse
import hashlib
import json
import random
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "游戏wiki" / "vic3-wiki-en"
DST = ROOT / "游戏wiki" / "vic3-wiki-zh"
CACHE_DIR = ROOT / ".cache" / "vic3-wiki-zh" / "blocked-chunks"
GLOSSARY = Path(__file__).resolve().parent / "glossary_zh.json"
TODAY = "2026-10-28"

MODEL_CASCADE = ["glm-4.7", "glm-4.6", "glm-4.5-air", "glm-4.5", "glm-5.3"]

FENCE_RE = re.compile(r"^\s*```")
IMG_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]*)\)")
LINKFULL_RE = re.compile(r"(!?\[[^\]]*\])\(([^)\n]*)\)")
MARKER_RE = re.compile(r"\{#(\d+)\}")
HEAD_RE = re.compile(r"^#{1,6}\s")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")

POST_FIXES = {"权力力": "权威力"}


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(CACHE_DIR.parent / "translate_blocked.log", "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")


# ---------- 提示词 ----------

RULES_CORE = """你是《维多利亚3》（Victoria 3）官方 wiki 的专业译者，把英文 Markdown 逐段译成简体中文。

【输出要求】只输出译文本身。不要解释、不要加引号、不要用 ``` 代码围栏包裹整段输出。

【绝对不许改动的部分（原样保留）】
1. 代码块（``` 围栏内全部内容）、行内代码 `...`。
2. 控制台命令、脚本标识符（annex、tag、law_groups、building_chemical_plants 这类蛇形命名/命令）、文件路径、文件名。
3. URL、HTML 标签、图片语法 ![alt](url)（含 alt 文本）。
4. 变量占位符：方括号占位（如 [imposer country]、[imposed law]）与 $变量$，原样保留。
5. 数字、单位、百分比、正负号。
6. Markdown 链接：原文的链接目标已被替换成形如 {#数字} 的占位符，如 [国家]({#3})。译文中这些占位符必须一个不少、一个不改、位置对应地原样保留（方括号里的文本译成中文）。占位符两侧不要加任何括号。
7. 标点用中文全角（，。；：""），但 Markdown 语法字符（()[]|#!*`>）必须保持英文半角。

【翻译规则】
1. 逐段对译：段落数量与顺序和原文一致，不漏段、不并段、不总结、不增删内容。列表项、表格行逐条对应；保持行结构。
2. 标题（# 开头）译成中文，可在标题里保留关键英文术语。
3. 游戏专有名词采用《维多利亚3》官方简体中文本地化译名，下方术语表给出的译法必须严格执行；表外术语首次出现译成中文并在括号内保留英文，如 权威力（Authority），此后只用中文；没有通行译法的保留英文。
4. 术语表中"保留英文"的概念（effect、trigger、scope、on_action、defines、GUI 等）在正文里保留英文原词，首次出现可加中文说明。
5. 表格：表头与叙述性单元格翻译；单元格里的纯标识符、数字、代码不译。
6. 原文是模板/事件脚本残迹（孤立词组、UI 文案、事件描述）时按字面忠实翻译，不重组、不串联成文。
7. 文体：面向玩家的百科与指南，准确、自然、不机翻腔。"""

GLOSSARY_SECTION = """

【术语表（英文 → 必用中文译名）】
{terms}

【保留英文的概念词】
{keep}"""


def build_prompts():
    full = RULES_CORE
    slim = RULES_CORE + "\n（本段无术语表，按你的知识采用游戏官方中文译名。）"
    g = json.loads(GLOSSARY.read_text(encoding="utf-8"))
    terms = "\n".join(f"{k} → {v}" for k, v in g["terms"].items())
    full += GLOSSARY_SECTION.replace("{terms}", terms).replace("{keep}", "、".join(g["keep_english"]))
    return full, slim


# ---------- 分块 ----------

def split_front_matter(text):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[: end + 5], text[end + 5:]
    return "", text


def chunk_body(body, budget):
    lines = body.split("\n")
    chunks, cur, cur_len, in_fence = [], [], 0, False
    for i, line in enumerate(lines):
        prev = lines[i - 1] if i else ""
        is_fence = bool(FENCE_RE.match(line))
        if is_fence:
            in_fence = not in_fence
        can_cut = not in_fence and not is_fence and (
            HEAD_RE.match(line)
            or (prev.strip() == "")
            or (line.lstrip().startswith("|") and not prev.lstrip().startswith("|"))
        )
        if cur and can_cut and cur_len >= budget:
            chunks.append("\n".join(cur))
            cur, cur_len = [], 0
        cur.append(line)
        cur_len += len(line) + 1
        if not in_fence and cur_len >= budget * 1.5:
            chunks.append("\n".join(cur))
            cur, cur_len = [], 0
    if cur:
        chunks.append("\n".join(cur))
    return [c for c in chunks if c.strip()]


def split_in_half(chunk):
    """在中点附近找安全边界（代码围栏外的空行，退而求其次表格行间）把块切成两半。"""
    lines = chunk.split("\n")
    total = len(chunk)
    best_acc, best_acc_gap = None, None
    row_acc, row_gap = None, None
    acc, in_fence = 0, False
    for i, line in enumerate(lines[:-1]):
        if FENCE_RE.match(line):
            in_fence = not in_fence
        acc += len(line) + 1
        if in_fence:
            continue
        gap = abs(acc - total // 2)
        if line.strip() == "" and (best_acc_gap is None or gap < best_acc_gap):
            best_acc, best_acc_gap = acc, gap
        if line.lstrip().startswith("|") and (row_gap is None or gap < row_gap):
            row_acc, row_gap = acc, gap
    cut = best_acc if best_acc_gap is not None else (row_acc if row_gap is not None else total // 2)
    return chunk[:cut], chunk[cut:]


# ---------- 链接占位保护 ----------

def protect_links(chunk):
    store = []

    def repl(m):
        store.append("(" + m.group(2) + ")")
        return m.group(1) + "{#%d}" % (len(store) - 1)
    return LINKFULL_RE.sub(repl, chunk), store


def restore_links(text, store):
    text = re.sub(r"（\s*(\{\s*#\s*\d+\s*\})\s*）", r"\1", text)
    text = re.sub(r"【\s*(\{\s*#\s*\d+\s*\})\s*】", r"\1", text)
    text = re.sub(r"（\s*(\{\s*#\s*\d+\s*\})\s*\)", r"\1", text)
    text = re.sub(r"\(\s*(\{\s*#\s*\d+\s*\})\s*）", r"\1", text)
    text = re.sub(r"（(\{#\d+\})", r"\1", text)
    text = re.sub(r"(\{#\d+\})）", r"\1", text)
    text = re.sub(r"\(\s*(\{\s*#\s*\d+\s*\})\s*\)", r"\1", text)
    text = re.sub(r"\{\s*#\s*(\d+)\s*\}", r"{#\1}", text)
    seen = []

    def back(m):
        i = int(m.group(1))
        seen.append(i)
        return store[i] if 0 <= i < len(store) else m.group(0)
    out = MARKER_RE.sub(back, text)
    missing = sorted(set(range(len(store))) - set(seen))
    extra = sorted(x for x in set(seen) if x not in set(range(len(store))))
    return out, missing, extra


def flatten_surplus_links(src, dst):
    src_counts = Counter(LINK_RE.findall(src))
    dst_counts = Counter(LINK_RE.findall(dst))
    for target in (dst_counts - src_counts):
        pat = re.compile(r"\[([^\]]*)\]\(" + re.escape(target) + r"\)")
        keep = src_counts.get(target, 0)
        idx = [0]

        def repl(m):
            idx[0] += 1
            return m.group(1) if idx[0] > keep else m.group(0)
        dst = pat.sub(repl, dst)
    return dst


# ---------- 校验 ----------

def structure_of(text):
    return {
        "fences": len([l for l in text.split("\n") if FENCE_RE.match(l)]),
        "imgs": len(IMG_RE.findall(text)),
        "links": sorted(LINK_RE.findall(text)),
        "heads": len([l for l in text.split("\n") if HEAD_RE.match(l)]),
    }


def validate_chunk(src, dst, problems):
    s, d = structure_of(src), structure_of(dst)
    if s["fences"] != d["fences"]:
        problems.append(f"代码围栏数 {s['fences']}→{d['fences']}")
    if s["imgs"] != d["imgs"]:
        problems.append(f"图片数 {s['imgs']}→{d['imgs']}")
    if s["links"] != d["links"]:
        diff_s = Counter(s["links"]) - Counter(d["links"])
        diff_d = Counter(d["links"]) - Counter(s["links"])
        lost = [f"{k}×{v}" for k, v in list(diff_s.items())[:3]]
        add = [f"{k}×{v}" for k, v in list(diff_d.items())[:3]]
        problems.append(f"链接目标变了（各目标出现次数须一致） 丢:{lost} 多:{add}")
    if s["heads"] != d["heads"]:
        problems.append(f"标题数 {s['heads']}→{d['heads']}")
    if len(dst) < 0.2 * len(src):
        problems.append(f"译文过短 {len(src)}→{len(dst)}")
    return not problems


def strip_outer_fence(text):
    t = text.strip()
    if t.startswith("```"):
        nl = t.find("\n")
        if nl != -1 and t.rstrip().endswith("```"):
            inner = t[nl + 1:].rstrip()
            if inner.endswith("```"):
                inner = inner[:-3]
            return inner.strip("\n")
    return t


# ---------- API（Anthropic 兼容端点，多模型级联） ----------

class CascadeTranslator:
    def __init__(self, cfg):
        self.url = cfg["baseUrl"].rstrip("/") + "/v1/messages"
        self.key = cfg["apiKey"]
        self.lock = threading.Lock()
        self.usage = {"input": 0, "output": 0, "calls": 0, "blocked": 0}

    def _call_one(self, model, system, user, max_tokens):
        body = json.dumps({
            "model": model, "max_tokens": max_tokens, "temperature": 0.2,
            "thinking": {"type": "disabled"},
            "system": system, "messages": [{"role": "user", "content": user}],
        }).encode()
        last = None
        for attempt in range(5):
            req = urllib.request.Request(self.url, data=body, method="POST", headers={
                "content-type": "application/json", "x-api-key": self.key,
                "anthropic-version": "2023-06-01"})
            try:
                with urllib.request.urlopen(req, timeout=900) as r:
                    resp = json.loads(r.read())
                with self.lock:
                    u = resp.get("usage", {})
                    self.usage["input"] += u.get("input_tokens", 0)
                    self.usage["output"] += u.get("output_tokens", 0)
                    self.usage["calls"] += 1
                text = "".join(b.get("text", "") for b in resp.get("content", []))
                return text, resp.get("stop_reason"), None
            except urllib.error.HTTPError as e:
                detail = e.read().decode(errors="replace")[:200]
                last = f"HTTP {e.code} {detail}"
                if e.code == 400 and ("1301" in detail or "敏感" in detail):
                    with self.lock:
                        self.usage["blocked"] += 1
                    return None, None, "blocked"      # 内容风控：换模型
                if e.code in (429, 500, 502, 503, 504, 529) and attempt < 4:
                    time.sleep(min(120, (3 * 2 ** attempt) + random.uniform(0, 3)))
                    continue
                return None, None, last
            except Exception as e:
                last = f"{type(e).__name__} {e}"
                if attempt < 4:
                    time.sleep(min(120, 3 * 2 ** attempt))
                    continue
                return None, None, last
        return None, None, last

    def translate_chunk(self, models, system_full, system_slim, chunk, depth=0):
        """级联逐模型；全失败时对半分块递归到段落粒度（~400 字符，深度 5）。
        叶子仍失败的片段保留英文并打标记，绝不拖垮兄弟片段。
        返回 (译文, 模型或 None, 英文保留字符数)。"""
        text, model = self._translate_chunk_once(models, system_full, system_slim, chunk)
        if text is not None:
            return text, model, 0
        if depth >= 5 or len(chunk) < 400:
            return ("<!-- untranslated: blocked by content filter -->\n" + chunk), None, len(chunk)
        a, b = split_in_half(chunk)
        if not a.strip() or not b.strip():
            return ("<!-- untranslated: blocked by content filter -->\n" + chunk), None, len(chunk)
        ta, ma, ea = self.translate_chunk(models, system_full, system_slim, a, depth + 1)
        tb, mb, eb = self.translate_chunk(models, system_full, system_slim, b, depth + 1)
        model_out = ma if ma == mb else (ma or mb)
        return ta + "\n" + tb, model_out, ea + eb

    def _translate_chunk_once(self, models, system_full, system_slim, chunk):
        """按级联逐模型尝试；每模型带一次校验反馈重试。返回 (译文 or None, 使用的模型)。"""
        protected, store = protect_links(chunk)
        max_tokens = min(12000, 4096 + int(len(protected) * 0.6))
        attempts = [(m, system_full) for m in models] + [(models[0], system_slim)]
        for model, system in attempts:
            user = protected
            for round_ in (1, 2):
                text, stop, err = self._call_one(model, system, user, max_tokens)
                if err == "blocked":
                    break  # 该模型被风控拦，级联下一个
                if err:
                    break  # 其他错误（重试已尽），级联下一个
                text = strip_outer_fence(text)
                text, missing, extra = restore_links(text, store)
                text = flatten_surplus_links(chunk, text)
                problems = []
                if missing:
                    problems.append(f"丢失链接占位符 {['{#%d}' % i for i in missing]}")
                if extra:
                    problems.append(f"多余链接占位符 {extra}")
                if stop == "max_tokens":
                    problems.append("输出被截断")
                if validate_chunk(chunk, text, problems):
                    for a, b in POST_FIXES.items():
                        text = text.replace(a, b)
                    return text, model
                if round_ == 1:
                    user = (protected + f"\n\n---\n你上一次的译文存在以下问题：{'；'.join(problems)}。\n"
                            "请重新完整翻译本段并修复这些问题，仍只输出译文。")
        return None, None


# ---------- 单文件 ----------

def is_fill_file(path):
    head = path.read_text(encoding="utf-8")[:600]
    return "kept-english" in head


def translate_file(name, tr, prompts, args):
    raw = (SRC / name).read_text(encoding="utf-8")
    front, body = split_front_matter(raw)
    src_chunks = chunk_body(body, args.chunk_chars)

    cache_path = CACHE_DIR / (name.replace("/", "__") + ".json")
    cache = {"chunks": []}
    if cache_path.exists():
        try:
            cache = json.loads(cache_path.read_text(encoding="utf-8"))
        except Exception:
            cache = {"chunks": []}
    done = cache["chunks"] + [None] * (len(src_chunks) - len(cache["chunks"]))
    assert len(done) == len(src_chunks), f"{name}: 缓存块数 {len(done)} 与当前分块 {len(src_chunks)} 不符（chunk-chars 变了？删缓存重跑）"
    models_used = set(cache.get("models_used", []))

    def save_cache():
        cache["chunks"] = done
        cache["models_used"] = sorted(models_used)
        cache_path.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")

    untranslated_chars = 0
    for idx, chunk in enumerate(src_chunks):
        if done[idx] and done[idx].get("md5") == hashlib.md5(chunk.encode()).hexdigest() and not done[idx].get("en"):
            continue  # 命中缓存（英文保留的块允许下次重试改进）
        text, model, en_chars = tr.translate_chunk(MODEL_CASCADE, prompts[0], prompts[1], chunk)
        if en_chars:
            log(f"{name} chunk{idx} 有 {en_chars} 字符保留英文")
        done[idx] = {"md5": hashlib.md5(chunk.encode()).hexdigest(), "text": text,
                     "en": en_chars > 0, "en_chars": en_chars}
        untranslated_chars += en_chars
        if model:
            models_used.add(model)
        save_cache()

    untranslated_chars = sum(c.get("en_chars", 0) for c in done if c)
    body_len = max(1, len(body))
    if untranslated_chars > 0.05 * body_len:
        save_cache()
        log(f"{name} 未翻译字符 {untranslated_chars}/{body_len} 超过 5%，不接收")
        return ("fail", name, f"{untranslated_chars}字符未翻")

    body_out = "\n".join(c["text"] for c in done)
    tag = "/".join(sorted(models_used) or ["cascade"])
    if untranslated_chars > 0:
        inject = f"translated: {TODAY}\ntranslator: machine ({tag}; {untranslated_chars} chars untranslated, marked in text)\n"
    else:
        inject = f"translated: {TODAY}\ntranslator: machine ({tag})\n"
    out = front[:4] + inject + front[4:] + body_out
    tmp = (DST / name).with_suffix(".md.tmp")
    tmp.write_text(out, encoding="utf-8")
    tmp.replace(DST / name)
    return ("ok", name, len(src_chunks))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--chunk-chars", type=int, default=12000)
    args = ap.parse_args()

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cfg = json.loads((ROOT / "config" / "llm.json").read_text(encoding="utf-8"))
    tr = CascadeTranslator(cfg)
    prompts = build_prompts()

    if args.only:
        files = [x.strip() for x in args.only.split(",") if x.strip()]
    else:
        files = sorted(p.name for p in DST.glob("*.md") if is_fill_file(p))
    log(f"补翻开始：{len(files)} 个文件，级联 {' → '.join(MODEL_CASCADE)} → 精简提示，workers={args.workers}")

    results = {"ok": [], "fail": []}
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(translate_file, n, tr, prompts, args): n for n in files}
        for fut in as_completed(futs):
            n = futs[fut]
            try:
                status, name, info = fut.result()
                results[status].append(name)
                log(f"[{status}] {name}" + (f"（{info} 块）" if status == "ok" else f"（chunk {info}）"))
            except Exception as e:
                results["fail"].append(n)
                log(f"[error] {n}: {type(e).__name__} {e}")

    u = tr.usage
    log(f"补翻完成：ok={len(results['ok'])} fail={len(results['fail'])}，用时 {(time.time()-t0)/60:.1f} 分钟，"
        f"调用 {u['calls']} 次（风控拦截 {u['blocked']} 次），tokens 入 {u['input']/1e6:.2f}M / 出 {u['output']/1e6:.2f}M")
    if results["fail"]:
        log(f"仍失败：{results['fail']}")


if __name__ == "__main__":
    main()
