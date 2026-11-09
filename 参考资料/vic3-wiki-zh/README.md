translated: 2026-10-28
translator: machine (glm-4.7)
# Victoria 3 Wiki 本地镜像

抓取自 [vic3.paradoxwikis.com](https://vic3.paradoxwikis.com/) 全部 627 个内容页面
（非重定向、主命名空间），已于 2026-10-27 通过 MediaWiki parse API 转为 Markdown。

## 快速入口（控制台相关）

- [Console commands](Console%20commands.md) — 控制台命令总表：debug mode 开启方法、按键、全部命令及示例
- [console-quick-reference](console-quick-reference.md) — 156 条命令的一句话速查表（自动生成）
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