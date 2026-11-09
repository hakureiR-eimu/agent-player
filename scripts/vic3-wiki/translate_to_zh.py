# -*- coding: utf-8 -*-
"""把 参考资料/vic3-wiki-en/ 的 Markdown 翻译成中文，落到 参考资料/vic3-wiki-zh/。

用法：
    python scripts/vic3-wiki/translate_to_zh.py                 # 全量（断点续跑，已完成的跳过）
    python scripts/vic3-wiki/translate_to_zh.py --only Laws.md  # 只翻指定文件（逗号分隔）
    python scripts/vic3-wiki/translate_to_zh.py --limit 3       # 只翻前 N 个（按优先级排序）
    python scripts/vic3-wiki/translate_to_zh.py --force         # 忽略已有成品强制重翻
    可选：--workers 4 --chunk-chars 16000 --model glm-5.3

认证读取 config/llm.json（与 agent 运行时同一份），走智谱 Anthropic 兼容端点。
逐分块进度缓存在 .cache/vic3-wiki-zh/chunks/，中断后重跑只补失败的块。
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
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "参考资料" / "vic3-wiki-en"
DST = ROOT / "参考资料" / "vic3-wiki-zh"
CACHE = ROOT / ".cache" / "vic3-wiki-zh"
CHUNKS_DIR = CACHE / "chunks"
GLOSSARY = Path(__file__).resolve().parent / "glossary_zh.json"
TODAY = "2026-10-27"

# 入口与核心机制页最先翻（其余按：非国家页 → 国家页）
CORE_PAGES = [
    "README.md", "INDEX.md", "console-quick-reference.md",
    "Beginner's guide.md", "Victoria 3.md", "Jargon.md",
    "Laws.md", "Power structure laws.md", "Economy laws.md", "Human rights laws.md",
    "Amendments.md", "Government.md", "Government type.md", "Ideology.md",
    "Interest group.md", "Interest group content.md", "Political movement.md",
    "Political party.md", "Political lobby.md", "Elections.md", "Institutions.md",
    "Decrees.md", "Character.md", "Character ideology.md", "Agitator.md", "Trait.md",
    "Pops.md", "Needs.md", "Standard of living.md", "Wealth.md", "Profession.md",
    "Culture.md", "Religion.md", "Migration.md", "Discrimination.md",
    "Market.md", "Goods.md", "Trade.md", "Companies.md", "Treasury.md",
    "Building.md", "List of buildings.md", "Production method.md",
    "List of production methods.md", "Unique building.md", "Infrastructure.md",
    "Technology.md", "Production technology.md", "Society technology.md",
    "Military technology.md", "Education.md", "Urbanization.md", "Capacity.md",
    "Diplomacy.md", "Diplomatic play.md", "Rank.md", "Power bloc.md",
    "Subject.md", "Colonization.md", "Colonial administration.md",
    "Warfare overview.md", "Land warfare.md", "Naval warfare.md",
    "Front.md", "Battle.md", "Army.md", "Navy.md", "Commander.md",
    "Formable countries.md", "Releasable countries.md", "Countries.md",
    "Journal.md", "Objective.md", "Events.md", "Modifier.md",
    "Console commands.md", "Save-game editing.md", "Keyboard shortcuts.md",
    "Strategy_ America.md", "Strategy_ Austria.md", "Strategy_ Japan.md", "Strategy_ Prussia.md",
    "State.md", "State traits.md", "Harvest condition.md", "Expeditions.md",
    "Game rule.md", "Defines.md", "Effect.md", "Trigger.md", "Scope.md",
]

FENCE_RE = re.compile(r"^\s*```")
IMG_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]*)\)")
LINKFULL_RE = re.compile(r"(!?\[[^\]]*\])\(([^)\n]*)\)")
MARKER_RE = re.compile(r"\{#(\d+)\}")
HEAD_RE = re.compile(r"^#{1,6}\s")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(CACHE / "translate.log", "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")


# ---------- 分块 ----------

def split_front_matter(text):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[: end + 5], text[end + 5 :]
    return "", text


def chunk_body(body, budget):
    """按 段落/标题/表格行 边界切块；绝不切进代码围栏内部。"""
    lines = body.split("\n")
    chunks, cur, cur_len, in_fence = [], [], 0, False
    for i, line in enumerate(lines):
        prev = lines[i - 1] if i else ""
        is_fence = bool(FENCE_RE.match(line))
        if is_fence:
            in_fence = not in_fence
        can_cut = not in_fence and not is_fence and (
            HEAD_RE.match(line)  # 标题前可切
            or (prev.strip() == "")  # 空行后（段落边界）可切
            or (line.lstrip().startswith("|") and not prev.lstrip().startswith("|"))  # 表格开始
        )
        if cur and can_cut and cur_len >= budget:
            chunks.append("\n".join(cur))
            cur, cur_len = [], 0
        cur.append(line)
        cur_len += len(line) + 1
        if not in_fence and cur_len >= budget * 1.5:  # 兜底：无边界也切
            chunks.append("\n".join(cur))
            cur, cur_len = [], 0
    if cur:
        chunks.append("\n".join(cur))
    return [c for c in chunks if c.strip()]


# 译后确定性修正：模型偶发笔误的硬替换
POST_FIXES = {"权力力": "权威力"}


def POST_FIX(text):
    for a, b in POST_FIXES.items():
        text = text.replace(a, b)
    return text


# ---------- 链接占位保护 ----------

def protect_links(chunk):
    """把 (target) 部分换成 {#n} 占位符，模型不可能改写目标本身。"""
    store = []
    def repl(m):
        store.append("(" + m.group(2) + ")")
        return m.group(1) + "{#%d}" % (len(store) - 1)
    return LINKFULL_RE.sub(repl, chunk), store


def restore_links(text, store):
    """把 {#n} 还原回 (target)。返回 (还原后文本, 丢失的占位符序号, 多余/重复的占位符)。"""
    # 模型偶尔在占位符外加全角括号/方头括号、或加点空格，先归一化掉。
    # 注意：绝不能匹配 ASCII ()[]——那是 Markdown 链接语法本身（[文本]({#n})）。
    text = re.sub(r"（\s*(\{\s*#\s*\d+\s*\})\s*）", r"\1", text)
    text = re.sub(r"【\s*(\{\s*#\s*\d+\s*\})\s*】", r"\1", text)
    # 半全角混搭的配对
    text = re.sub(r"（\s*(\{\s*#\s*\d+\s*\})\s*\)", r"\1", text)
    text = re.sub(r"\(\s*(\{\s*#\s*\d+\s*\})\s*）", r"\1", text)
    text = re.sub(r"（(\{#\d+\})", r"\1", text)
    text = re.sub(r"(\{#\d+\})）", r"\1", text)
    # ( {#0} ) → {#0}：外层 ASCII 括号是模型多写的，剥掉外层后还原恰好得到正确语法
    text = re.sub(r"\(\s*(\{\s*#\s*\d+\s*\})\s*\)", r"\1", text)
    # { #0 } → {#0}
    text = re.sub(r"\{\s*#\s*(\d+)\s*\}", r"{#\1}", text)
    missing, seen = set(), []

    def back(m):
        i = int(m.group(1))
        seen.append(i)
        if 0 <= i < len(store):
            return store[i]
        return m.group(0)
    out = MARKER_RE.sub(back, text)
    expected = set(range(len(store)))
    missing = sorted(expected - set(seen))
    extra = sorted(x for x in set(seen) if x not in expected)
    return out, missing, extra


def flatten_surplus_links(src, dst):
    """模型偶尔把原文的纯文本提及也补成链接（重复使用占位符），导致某目标出现次数比源文多。
    多余的降回纯文本：每个目标保留源文中的前 N 次链接，其余 [文本](目标) → 文本。"""
    from collections import Counter
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


# ---------- 结构校验（防模型破坏 markdown） ----------

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
        from collections import Counter
        diff_s = Counter(s["links"]) - Counter(d["links"])
        diff_d = Counter(d["links"]) - Counter(s["links"])
        lost = [f"{k}×{v}" for k, v in list(diff_s.items())[:3]]
        add = [f"{k}×{v}" for k, v in list(diff_d.items())[:3]]
        problems.append(f"链接目标变了（源→译 各目标出现次数须一致） 丢:{lost} 多:{add}")
    if s["heads"] != d["heads"]:
        problems.append(f"标题数 {s['heads']}→{d['heads']}")
    if len(re.findall(r"[A-Za-z]", src)) > 200 and not CJK_RE.search(dst):
        problems.append("WARN:译文无中文（纯标识符块属正常）")
    if len(dst) < 0.2 * len(src):
        problems.append(f"译文过短 {len(src)}→{len(dst)}")
    # WARN 条目只记日志，不判失败（如纯标识符块无中文属正常）
    hard = [p for p in problems if not p.startswith("WARN:")]
    return not hard


# ---------- LLM 调用 ----------

class Translator:
    def __init__(self, cfg, model):
        self.url = cfg["baseUrl"].rstrip("/") + "/v1/messages"
        self.key = cfg["apiKey"]
        self.model = model or cfg.get("model", "glm-5.3")
        self.usage_lock = threading.Lock()
        self.usage = {"input": 0, "output": 0, "calls": 0, "retries": 0}

    def call(self, system, user, max_tokens):
        body = json.dumps({
            "model": self.model,
            "max_tokens": max_tokens,
            "temperature": 0.2,
            "thinking": {"type": "disabled"},
            "system": system,
            "messages": [{"role": "user", "content": user}],
        }).encode()
        last_err = None
        for attempt in range(7):
            req = urllib.request.Request(self.url, data=body, method="POST", headers={
                "content-type": "application/json",
                "x-api-key": self.key,
                "anthropic-version": "2023-06-01",
            })
            try:
                with urllib.request.urlopen(req, timeout=900) as r:
                    resp = json.loads(r.read())
                with self.usage_lock:
                    u = resp.get("usage", {})
                    self.usage["input"] += u.get("input_tokens", 0)
                    self.usage["output"] += u.get("output_tokens", 0)
                    self.usage["calls"] += 1
                text = "".join(b.get("text", "") for b in resp.get("content", []))
                stop = resp.get("stop_reason") or resp.get("stop_sequence")
                return text, stop
            except urllib.error.HTTPError as e:
                detail = e.read().decode(errors="replace")[:300]
                last_err = f"HTTP {e.code} {detail}"
                if e.code in (429, 500, 502, 503, 504, 529) and attempt < 6:
                    wait = min(120, (3 * 2 ** attempt) + random.uniform(0, 3))
                    if e.code == 429:
                        wait += 15
                    with self.usage_lock:
                        self.usage["retries"] += 1
                    time.sleep(wait)
                    continue
                raise RuntimeError(last_err)
            except Exception as e:
                last_err = f"{type(e).__name__} {e}"
                if attempt < 6:
                    time.sleep(min(120, 3 * 2 ** attempt))
                    continue
                raise RuntimeError(last_err)
        raise RuntimeError(last_err or "unknown")


SYSTEM_PROMPT = """你是《维多利亚3》（Victoria 3）官方 wiki 的专业译者，把英文 Markdown 逐段译成简体中文。

【输出要求】只输出译文本身。不要解释、不要加引号、不要用 ``` 代码围栏包裹整段输出。

【绝对不许改动的部分（原样保留）】
1. 代码块（``` 围栏内全部内容）、行内代码 `...`。
2. 控制台命令、脚本标识符（annex、tag、law_groups、building_chemical_plants 这类蛇形命名/命令）、文件路径、文件名。
3. URL、HTML 标签、图片语法 ![alt](url)（含 alt 文本）。
4. 变量占位符：方括号占位（如 [imposer country]、[imposed law]）与 $变量$，原样保留。
5. 数字、单位、百分比、正负号。
6. Markdown 链接：原文的链接目标已被替换成形如 {#数字} 的占位符，如 [国家]({#3})。译文中这些占位符必须一个不少、一个不改、位置对应地原样保留（方括号里的文本译成中文）。绝对不要把 {#数字} 写成其他任何形式。
7. 标点用中文全角（，。；：""），但 Markdown 语法字符（()[]|#!*`>）必须保持英文半角。

【翻译规则】
1. 逐段对译：段落数量与顺序和原文一致，不漏段、不并段、不总结、不增删内容。列表项、表格行逐条对应；保持行结构，不要把多行合并成一行。
2. 标题（# 开头）译成中文，可在标题里保留关键英文术语。
3. 游戏专有名词采用《维多利亚3》官方简体中文本地化译名，术语表里的译法必须严格执行。术语表之外的术语：首次出现译成中文并在括号内保留英文，如 权威力（Authority），此后只用中文；没有通行译法的（新机制、生造词、活动名）保留英文。
4. 术语表中"保留英文"的概念（effect、trigger、scope、on_action、defines、GUI 等）在正文里保留英文原词，首次出现可加中文说明，如 effect（游戏内效果脚本）。
5. 表格：表头与叙述性单元格翻译；单元格里的纯标识符、数字、代码不译。
6. 原文是模板/事件脚本残迹（孤立词组、UI 文案、事件描述）时按字面忠实翻译，不重组、不串联成文。
7. 文体：面向玩家的百科与指南，准确、自然、不机翻腔。

【术语表（英文 → 必用中文译名）】
{glossary}

【保留英文的概念词】
{keep}"""


def build_system_prompt():
    g = json.loads(GLOSSARY.read_text(encoding="utf-8"))
    terms = "\n".join(f"{k} → {v}" for k, v in g["terms"].items())
    keep = "、".join(g["keep_english"])
    return SYSTEM_PROMPT.replace("{glossary}", terms).replace("{keep}", keep)


def strip_outer_fence(text):
    t = text.strip()
    if t.startswith("```"):
        nl = t.find("\n")
        if nl != -1 and t.rstrip().endswith("```"):
            inner = t[nl + 1 :].rstrip()
            if inner.endswith("```"):
                inner = inner[: -3]
            return inner.strip("\n")
    return t


# ---------- 单文件翻译 ----------

def translate_file(name, tr, system, args, force=False):
    src_path = SRC / name
    dst_path = DST / name
    if dst_path.exists() and not force:
        return ("skip", name, 0)
    raw = src_path.read_text(encoding="utf-8")
    front, body = split_front_matter(raw)
    src_chunks = chunk_body(body, args.chunk_chars)

    cache_path = CHUNKS_DIR / (name.replace("/", "__") + ".json")
    cache = {"chunks": []}
    if cache_path.exists():
        try:
            cache = json.loads(cache_path.read_text(encoding="utf-8"))
        except Exception:
            cache = {"chunks": []}
    done = cache["chunks"] + [None] * (len(src_chunks) - len(cache["chunks"]))
    assert len(done) == len(src_chunks)

    def save_cache():
        cache_path.write_text(json.dumps({"chunks": done}, ensure_ascii=False), encoding="utf-8")

    for idx, chunk in enumerate(src_chunks):
        if done[idx] and done[idx].get("md5") == hashlib.md5(chunk.encode()).hexdigest():
            continue  # 命中缓存
        last_problems = ""
        protected, link_store = protect_links(chunk)
        for round_ in (1, 2, 3):
            problems = []
            if round_ > 1:
                log(f"{name} chunk{idx} 第{round_-1}次校验未过（{last_problems}），带反馈重试")
                user = (protected + f"\n\n---\n你上一次的译文存在以下问题：{last_problems}。\n"
                        "请重新完整翻译本段并修复这些问题（例如把漏掉的 {#数字} 链接占位符按原位置补回），仍只输出译文。")
            else:
                user = protected
            max_tokens = min(12000, 4096 + int(len(protected) * 0.6))
            text, stop = tr.call(system, user, max_tokens)
            text = strip_outer_fence(text)
            text, missing, extra = restore_links(text, link_store)
            text = flatten_surplus_links(chunk, text)
            if missing:
                problems.append(f"丢失链接占位符 {['{#%d}' % i for i in missing]}")
            if extra:
                problems.append(f"多余链接占位符 {extra}")
            if stop == "max_tokens":
                problems.append("输出被截断")
            if validate_chunk(chunk, text, problems):
                done[idx] = {"md5": hashlib.md5(chunk.encode()).hexdigest(), "text": text}
                save_cache()
                break
            last_problems = "；".join(problems)
        else:
            save_cache()
            log(f"{name} chunk{idx} 两次校验均失败：{last_problems}")
            return ("fail", name, idx)
        save_cache()

    # front matter 顶部（--- 之后）追加翻译元数据
    body_out = "\n".join(POST_FIX(c["text"]) for c in done)
    if front:
        inject = f"translated: {TODAY}\ntranslator: machine ({tr.model})\n"
        out = front[:4] + inject + front[4:] + body_out
    else:
        out = body_out
    tmp = dst_path.with_suffix(".md.tmp")
    tmp.write_text(out, encoding="utf-8")
    tmp.replace(dst_path)
    return ("ok", name, len(src_chunks))


def priority_key(name, is_country):
    try:
        tier = CORE_PAGES.index(name)
    except ValueError:
        tier = len(CORE_PAGES) + (2 if is_country else 1)
    return (tier, name.lower())


def is_country_page(text_head):
    m = re.search(r"^categories:\s*\[(.*?)\]", text_head, re.M)
    return bool(m and "Countries" in m.group(1))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--chunk-chars", type=int, default=16000)
    ap.add_argument("--model", default="")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    DST.mkdir(parents=True, exist_ok=True)
    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    cfg = json.loads((ROOT / "config" / "llm.json").read_text(encoding="utf-8"))
    tr = Translator(cfg, args.model)
    system = build_system_prompt()

    pages_json = SRC / "pages.json"
    if pages_json.exists():
        (DST / "pages.json").write_bytes(pages_json.read_bytes())

    files = sorted(p.name for p in SRC.glob("*.md"))
    if args.only:
        wanted = [x.strip() for x in args.only.split(",") if x.strip()]
        missing = [x for x in wanted if not (SRC / x).exists()]
        if missing:
            log(f"找不到文件：{missing}")
            return
        files = wanted
    else:
        metas = {p.name: is_country_page(p.read_text(encoding="utf-8")[:800]) for p in SRC.glob("*.md")}
        files.sort(key=lambda n: priority_key(n, metas[n]))
    if args.limit:
        files = files[: args.limit]

    log(f"开始：{len(files)} 个文件，workers={args.workers}，chunk={args.chunk_chars} 字符，model={tr.model}")
    results = {"ok": [], "skip": [], "fail": []}
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(translate_file, n, tr, system, args, args.force): n for n in files}
        for fut in as_completed(futs):
            n = futs[fut]
            try:
                status, name, info = fut.result()
                results.setdefault(status, []).append(name)
                log(f"[{status}] {name}" + (f"（{info} 块）" if status == "ok" else f"（chunk {info}）" if status == "fail" else ""))
            except Exception as e:
                results["fail"].append(n)
                log(f"[error] {n}: {type(e).__name__} {e}")

    dt = time.time() - t0
    u = tr.usage
    log(f"完成：ok={len(results['ok'])} skip={len(results['skip'])} fail={len(results['fail'])}，"
        f"用时 {dt/60:.1f} 分钟，调用 {u['calls']} 次（重试 {u['retries']}），"
        f"tokens 入 {u['input']/1e6:.2f}M / 出 {u['output']/1e6:.2f}M")
    if results["fail"]:
        log(f"失败清单（重跑本脚本即自动补翻）：{results['fail']}")


if __name__ == "__main__":
    main()
