# -*- coding: utf-8 -*-
"""Build README.md / INDEX.md / console quick reference for 游戏wiki/vic3-wiki-en."""
import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

OUT = Path(r"D:\work\game-agent\游戏wiki\vic3-wiki-en")
man = json.loads((OUT / "pages.json").read_text(encoding="utf-8"))
by_title = {m["title"]: m for m in man}

# ---------------------------------------------------------------- quick ref
cc = (OUT / "Console commands.md").read_text(encoding="utf-8")
rows = []
for line in cc.splitlines():
    m = re.match(r"^\|\s*`?([a-z][a-z0-9_]*(?:\s*<[^|]*?>|\s*\[[^\]|]*\])?)`?\s*\|([^|]*)(?:\|([^|]*))?\|$", line)
    if m:
        cmd = m.group(1).strip()
        desc = m.group(2).strip()
        extra = (m.group(3) or "").strip()
        if desc and not desc.startswith("---"):
            rows.append((cmd, desc, extra))
seen = set()
uniq = []
for r in rows:
    if r[0] not in seen:
        seen.add(r[0])
        uniq.append(r)

qr = ["---",
      "title: Console 命令速查表（自动提取）",
      f"source: https://vic3.paradoxwikis.com/Console_commands",
      f"extracted_from: Console commands.md",
      f"fetched: {date.today().isoformat()}",
      "---",
      "",
      f"共 {len(uniq)} 条命令，自动提取自 [Console commands](Console%20commands.md)；"
      "完整说明（含 debug mode 开启方法、按键、注意事项）见原页。",
      "",
      "| 命令 | 说明 |",
      "|---|---|"]
for cmd, desc, _ in sorted(uniq):
    qr.append(f"| `{cmd}` | {desc} |")
(OUT / "console-quick-reference.md").write_text("\n".join(qr) + "\n", encoding="utf-8")
print("quick ref commands:", len(uniq))

# ---------------------------------------------------------------- groups
def link(t):
    m = by_title.get(t)
    return f"[{t}]({m['file']})" if m else t


console_core = [
    ("Console commands", "全部控制台命令 + debug mode 开启方法"),
    ("Save-game editing", "存档修改"),
    ("Keyboard shortcuts", "快捷键"),
]
script_core = [
    ("Introduction to the Paradox Scripting Language", "PDX 脚本语言入门"),
    ("Effect", "effect 全量参考（配合控制台 `effect` 命令）"),
    ("Trigger", "trigger 全量参考"),
    ("Scope", "作用域/事件目标链"),
    ("Event target", "事件目标"),
    ("Variable", "变量系统"),
    ("Script value", "script value"),
    ("Modifier types", "修正类型全表"),
    ("On action", "on_action 钩子"),
    ("Defines", "defines 可调参数"),
]
modding_rest = sorted(
    m["title"] for m in man
    if "Modding" in m["categories"] and m["title"] not in [t for t, _ in console_core + script_core]
)

group_order = [
    ("Scripted_content", "脚本化内容（各国/资料片 content 包、journal、events）"),
    ("Guides", "官方指南"),
    ("Game_concepts", "游戏概念"),
    ("Lists", "数据列表（state regions / cultures / companies 等）"),
    ("Events", "事件"),
    ("Patches", "补丁与版本"),
    ("Countries", "国家页面（含 TAG、开局数据）"),
]
assigned = set(t for t, _ in console_core + script_core) | set(modding_rest)

idx = ["---",
       "title: Victoria 3 Wiki 本地镜像索引",
       f"fetched: {date.today().isoformat()}",
       f"pages: {len(man)}",
       "source: https://vic3.paradoxwikis.com/",
       "---",
       "",
       f"# Victoria 3 Wiki 本地镜像索引（{len(man)} 页）",
       "",
       "## 控制台 / 作弊",
       ""]
for t, d in console_core:
    idx.append(f"- {link(t)} — {d}")
idx += ["", "## 脚本参考（控制台 `effect` / `trigger` 及模组开发核心）", ""]
for t, d in script_core:
    idx.append(f"- {link(t)} — {d}")
idx += ["", "## 其他模组开发页面", ""]
idx += [f"- {link(t)}" for t in modding_rest]

used = set(assigned)
for cat, label in group_order:
    titles = sorted(m["title"] for m in man if cat in m["categories"] and m["title"] not in used)
    if not titles:
        continue
    used.update(titles)
    idx += ["", f"## {label}（{len(titles)}）", ""]
    idx += [f"- {link(t)}" for t in titles]

rest = sorted(m["title"] for m in man if m["title"] not in used)
if rest:
    idx += ["", f"## 其他（{len(rest)}）", ""]
    idx += [f"- {link(t)}" for t in rest]

(OUT / "INDEX.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

# ---------------------------------------------------------------- README
readme = f"""# Victoria 3 Wiki 本地镜像

抓取自 [vic3.paradoxwikis.com](https://vic3.paradoxwikis.com/) 全部 {len(man)} 个内容页面
（非重定向、主命名空间），已于 {date.today().isoformat()} 通过 MediaWiki parse API 转为 Markdown。

## 快速入口（控制台相关）

- [Console commands](Console%20commands.md) — 控制台命令总表：debug mode 开启方法、按键、全部命令及示例
- [console-quick-reference](console-quick-reference.md) — {len(uniq)} 条命令的一句话速查表（自动生成）
- [Effect](Effect.md) / [Trigger](Trigger.md) / [Scope](Scope.md) / [Event target](Event%20target.md) —
  `effect` / `trigger` 控制台命令与脚本可用的全部效果、条件、作用域
- [Countries](Countries.md) 及各国家页 — `annex` / `tag` 等命令所需的国家 TAG
- [Save-game editing](Save-game%20editing.md) — 存档直接改法
- [Defines](Defines.md) — 游戏可调参数（配合 mod 使用）

## 全量索引

见 [INDEX.md](INDEX.md)（按 控制台 → 脚本 → 模组 → 指南 → 数据列表 → 国家 分组）。

## 说明

- 每个文件头部 front matter 含 `source`（原页 URL）、`categories`、`fetched`（抓取日期）。
- 站内链接尽量解析为本地相对链接；未镜像的页面（文件、模板等）保留指向线上的绝对 URL。
- 图片仍指向线上（`vic3.paradoxwikis.com/images/...`），离线时只影响配图，不影响文字。
- 原始 HTML（约 90MB，627 个 API JSON）缓存在 `.cache/vic3-wiki-raw/`，可用
  `python scripts/vic3-wiki/convert_to_md.py` 重新转换，无需重新下载。
- 源站有 Fastly 反爬挑战，直接 curl/api.php 会被拦；刷新数据需经真实浏览器通过挑战后，
  在页面上下文用同源 fetch 调 `api.php?action=parse`（抓取流程见仓库 scripts/vic3-wiki/ 目录说明）。
"""
(OUT / "README.md").write_text(readme, encoding="utf-8")
print("README/INDEX/quick-ref written")
