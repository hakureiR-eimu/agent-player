# -*- coding: utf-8 -*-
"""Convert cached MediaWiki parse-API JSON (Victoria 3 wiki) into Markdown files.

Input : .cache/vic3-wiki-raw/*.json   (MediaWiki action=parse, formatversion=2)
Output: 游戏wiki/vic3-wiki-en/<Title>.md + pages.json manifest (for index building)

Usage: python scripts/vic3-wiki/convert_to_md.py
"""
import json
import re
import sys
import urllib.parse
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup, CData, Comment, Doctype, ProcessingInstruction, NavigableString, Tag

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / ".cache" / "vic3-wiki-raw"
OUT_DIR = ROOT / "游戏wiki" / "vic3-wiki-en"
WIKI_BASE = "https://vic3.paradoxwikis.com/"

# ---------------------------------------------------------------- utilities

_ILLEGAL = re.compile(r'[\\/:*?"<>|#]')


def safe_name(title: str) -> str:
    return _ILLEGAL.sub("_", title).strip().strip(".")[:150] or "untitled"


def href_to_markdown(href: str, text: str, existing: dict) -> str:
    """Resolve a wiki <a href> into a markdown link target."""
    if not href:
        return text
    if href.startswith("#"):  # same-page anchor -> not reliable in md
        return text
    if href.startswith("//"):
        href = "https:" + href
    if href.startswith("/"):
        path, _, frag = href.partition("#")
        path = path.split("?", 1)[0]
        if "/index.php" in path and not path.startswith("/wiki"):
            return text  # edit/redlink stub
        title = urllib.parse.unquote(path.lstrip("/")) or "Main_Page"
        md = existing.get(title.replace("_", " "))
        if md:
            return f"{md}.md"
        return WIKI_BASE + path.lstrip("/")
    if href.startswith("http"):
        return href
    return text


def inline_text(node, existing: dict) -> str:
    """Convert an inline node list to markdown (links kept)."""
    parts = []
    for child in node.children if isinstance(node, Tag) else [node]:
        parts.append(_inline(child, existing))
    return re.sub(r"\s+", " ", "".join(parts)).strip()


def _inline(node, existing: dict) -> str:
    if isinstance(node, NavigableString):
        return str(node).replace("\n", " ")
    if not isinstance(node, Tag):
        return ""
    name = node.name
    if name in ("script", "style"):
        return ""
    if name == "br":
        return " "
    if name in ("b", "strong"):
        inner = node.get_text(" ", strip=True)
        return f"**{inner}**" if inner else ""
    if name in ("i", "em"):
        inner = node.get_text(" ", strip=True)
        return f"*{inner}*" if inner else ""
    if name in ("code", "tt", "samp"):
        inner = node.get_text("", strip=True)
        return f"`{inner}`" if inner else ""
    if name == "a":
        text = node.get_text(" ", strip=True)
        href = node.get("href", "")
        target = href_to_markdown(href, text, existing)
        if target == text or not text:
            return text
        return f"[{text}]({target})"
    if name == "img":
        src = node.get("src", "")
        if src.startswith("//"):
            src = "https:" + src
        return f"![{node.get('alt', '')}]({src})"
    if name in ("sup", "sub", "span", "small", "abbr", "cite", "label"):
        return "".join(_inline(c, existing) for c in node.children)
    if name in ("p", "div", "table", "ul", "ol", "dl"):
        return node.get_text(" ", strip=True)
    return "".join(_inline(c, existing) for c in node.children)


def cell_text(cell: Tag, existing: dict) -> str:
    """Flatten a table cell into a single line, keeping links."""
    txt = inline_text(cell, existing)
    txt = txt.replace("|", "\\|")
    return re.sub(r"\s+", " ", txt).strip()


def table_to_md(table: Tag, existing: dict) -> str:
    rows = []
    thead = table.find("thead")
    tbody = table.find("tbody") or table
    trs = []
    if thead:
        trs.extend(thead.find_all("tr", recursive=False))
    for tr in tbody.find_all("tr"):
        if thead and thead in tr.parents:
            continue
        trs.append(tr)
    for tr in trs:
        cells = tr.find_all(["th", "td"], recursive=False)
        if not cells:
            cells = tr.find_all(["th", "td"])
        rows.append([cell_text(c, existing) for c in cells])
    rows = [r for r in rows if any(c for c in r)]
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    for r in rows:
        r.extend([""] * (width - len(r)))
    out = ["| " + " | ".join(rows[0]) + " |",
           "|" + "---|" * width]
    out.extend("| " + " | ".join(r) + " |" for r in rows[1:])
    return "\n".join(out)


def list_to_md(node: Tag, existing: dict, indent: int = 0, ordered: bool = False) -> str:
    lines = []
    idx = 1
    for li in node.find_all("li", recursive=False):
        marker = f"{idx}. " if ordered else "- "
        idx += 1
        # direct inline content of the li (excluding nested lists)
        content_parts = []
        sub_lists = []
        for child in li.children:
            if isinstance(child, Tag) and child.name in ("ul", "ol"):
                sub_lists.append(child)
            else:
                content_parts.append(_inline(child, existing) if isinstance(child, Tag) else str(child))
        text = re.sub(r"\s+", " ", "".join(content_parts)).strip()
        lines.append("  " * indent + marker + text)
        for sub in sub_lists:
            lines.append(list_to_md(sub, existing, indent + 1, sub.name == "ol"))
    return "\n".join(l for l in lines if l.strip())


def block_to_md(node, existing: dict) -> list:
    """Convert a block-level node into markdown lines."""
    if isinstance(node, (Comment, Doctype, ProcessingInstruction, CData)):
        return []
    if isinstance(node, NavigableString):
        t = str(node).strip()
        return [t] if t else []
    if not isinstance(node, Tag):
        return []
    name = node.name
    classes = node.get("class", []) or []

    if name in ("script", "style", "link", "meta"):
        return []
    if "mw-editsection" in classes or "mw-empty-elt" in classes:
        return []
    if node.get("id") == "toc" or "toc" in classes and name in ("div", "nav"):
        return []
    if "sortkey" in classes or "mw-cite-backlink" in classes:
        return []
    span_style = (node.get("style") or "").replace(" ", "").lower()
    if name == "span" and "display:none" in span_style:
        return []

    if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(name[1])
        text = node.get_text(" ", strip=True).replace("|", "\\|")
        return ["", "#" * level + " " + text, ""] if text else []

    if "mw-heading" in classes:  # wrapper div around headings
        out = []
        for c in node.children:
            out.extend(block_to_md(c, existing))
        return out

    if name == "p":
        text = inline_text(node, existing)
        return [text, ""] if text else []

    if name == "pre":
        code = node.get_text()
        lang = ""
        cls = " ".join(classes)
        if "javascript" in cls:
            lang = "javascript"
        return ["```" + lang, code.rstrip("\n"), "```", ""]

    if name == "table":
        # nested tables inside cells are flattened by cell_text
        if node.find_parent("table"):
            return []
        md = table_to_md(node, existing)
        return [md, ""] if md else []

    if name in ("ul", "ol"):
        if node.find_parent("li") is None:
            md = list_to_md(node, existing, 0, name == "ol")
            return [md, ""] if md else []
        return []

    if name == "dl":
        out = []
        for child in node.children:
            if isinstance(child, Tag) and child.name == "dt":
                t = inline_text(child, existing)
                if t:
                    out.append(f"**{t}**")
            elif isinstance(child, Tag) and child.name == "dd":
                t = inline_text(child, existing)
                if t:
                    out.append("  - " + t)
        return out + [""]

    if name in ("figure",):
        img = node.find("img")
        cap = node.find("figcaption")
        out = []
        if img is not None:
            out.append(_inline(img, existing))
        if cap is not None:
            out.append(f"*{cap.get_text(' ', strip=True)}*")
        return out + [""]

    if name == "hr":
        return ["---", ""]

    # generic container: recurse
    out = []
    for c in node.children:
        out.extend(block_to_md(c, existing))
    return out


# ---------------------------------------------------------------- main

def load_pages():
    pages = {}
    for f in sorted(RAW_DIR.glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            print(f"[warn] cannot parse {f.name}: {e}")
            continue
        p = data.get("parse")
        if not p or not p.get("text"):
            print(f"[warn] no parse.text in {f.name}")
            continue
        title = p.get("title", f.stem)
        rec = {
            "title": title,
            "pageid": p.get("pageid"),
            "displaytitle": p.get("displaytitle", title),
            "categories": [c.get("category", "") for c in (p.get("categories") or [])],
            "html": p["text"],
            "source_file": f.name,
        }
        old = pages.get(title)
        # prefer exact-title record; else first seen (priority pages were fetched first)
        if old is None or old["source_file"].split("__", 1)[0] > rec["source_file"].split("__", 1)[0]:
            pages[title] = rec
    return pages


def convert():
    pages = load_pages()
    existing = {t: safe_name(t) for t in pages}
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    manifest = []
    used_names = {}
    for title, rec in pages.items():
        base = safe_name(title)
        if base in used_names:
            base = f"{base}_{rec['pageid']}"
        used_names[base] = title
        existing[title] = base

    for title, rec in pages.items():
        base = existing[title]
        soup = BeautifulSoup(rec["html"], "lxml")
        for sel in (".mw-editsection", ".mw-jump-link", ".mw-indicators", "#siteSub",
                    ".navigation-not-searchable", ".nomobile"):
            for el in soup.select(sel):
                el.decompose()
        body = soup.body or soup
        lines = block_to_md(body, existing)
        md = "\n".join(lines)
        md = re.sub(r"\n{3,}", "\n\n", md).strip()
        disp = re.sub(r"<[^>]+>", "", rec["displaytitle"]).strip()
        front = [
            "---",
            f"title: {disp}",
            f"source: {WIKI_BASE + __import__('urllib.parse', fromlist=['quote']).quote(title.replace(' ', '_'), safe='')}",
            f"pageid: {rec['pageid']}",
            f"categories: [{', '.join(rec['categories'])}]",
            f"fetched: {date.today().isoformat()}",
            "---",
            "",
        ]
        (OUT_DIR / f"{base}.md").write_text("\n".join(front) + md + "\n", encoding="utf-8")
        manifest.append({"title": title, "file": base + ".md", "categories": rec["categories"]})

    (OUT_DIR / "pages.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    print(f"converted {len(manifest)} pages -> {OUT_DIR}")


if __name__ == "__main__":
    sys.exit(convert())
