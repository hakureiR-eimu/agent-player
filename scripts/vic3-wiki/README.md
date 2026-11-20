# Victoria 3 Wiki 本地镜像工具

产出物在 `游戏wiki/vic3-wiki-en/`（627 页 Markdown + README + INDEX + 控制台速查表，`-en` 后缀标注内容语言）
与 `游戏wiki/vic3-wiki-zh/`（同结构的中文版，机器翻译＋规则保真，见下文「中文版」）。

## 文件

| 文件 | 用途 |
|---|---|
| `convert_to_md.py` | 把 `.cache/vic3-wiki-raw/*.json`（MediaWiki parse API 响应）转成 `游戏wiki/vic3-wiki-en/*.md`。幂等，可反复重跑。 |
| `build_index.py` | 生成 `README.md`、`INDEX.md`（分组全量索引）、`console-quick-reference.md`（从 Console commands.md 自动提取的命令速查表）。需在 convert 之后运行。 |
| `translate_to_zh.py` | 把 en 镜像全量翻译成 `游戏wiki/vic3-wiki-zh/`。读 `config/llm.json` 走智谱 Anthropic 兼容端点，断点续跑（分块缓存在 `.cache/vic3-wiki-zh/chunks/`）。 |
| `glossary_zh.json` | 翻译术语表：Vic3 官方简体中文明译名 + 保留英文的脚本概念词，翻译时注入提示词。 |
| `verify_zh.py` | zh 版全量校验：对照 en 源逐文件检查 front matter、围栏/图片/链接/标题数、中文占比、残留占位符。 |
| `fill_blocked.py` | 兜底：仍缺的 zh 文件用英文原版填充并标注 kept-english（保证文件齐全、链接可解析）。 |
| `translate_blocked.py` | 补翻被内容风控（HTTP 400 / 1301）拦截的页面：多模型级联 + 对半分块递归，叶子仍失败的片段保留英文打标记。 |
| `build_tm.py` | 从已译语料构建离线翻译记忆库：en/zh 逐行对齐（带链接行按结构签名做锚点、模板行恒等锚、无链接行锚点等距定位），全语料投票产出 `.cache/vic3-wiki-zh/tm.json`（行级 TM + 链接显示名双语词典）。 |
| `translate_dict.py` | 离线词典补翻（零 LLM 调用，不触发风控）：整行 TM → 句级 TM → 句式模板（捕获组递归）→ 术语/名称最长匹配替换；结构校验不过拒写。处理 kept-english 整页与 `<!-- untranslated -->` 残块。 |

## 如何刷新数据

源站 `vic3.paradoxwikis.com` 有 Fastly 反爬挑战，**curl / 普通 HTTP 客户端一律被拦**（含带 Cookie，
因为校验 TLS 指纹）。刷新必须走真实浏览器：

1. 用浏览器打开 `https://vic3.paradoxwikis.com/`，等 JS 挑战自动通过（页面正常显示）。
2. 在该页面的 DevTools Console（或等价的页面上下文执行通道）里跑同源 fetch：
   - 枚举：`/api.php?action=query&list=allpages&aplimit=500&apfilterredir=nonredirects&format=json&formatversion=2`（按 `continue.apcontinue` 翻页）
   - 每页：`/api.php?action=parse&format=json&formatversion=2&redirects=1&prop=text|displaytitle|categories&page=<标题URL编码>`
   - 响应 JSON 原样存为 `.cache/vic3-wiki-raw/<序号>__<标题>.json`
3. `python scripts/vic3-wiki/convert_to_md.py && python scripts/vic3-wiki/build_index.py`

2026-10-27 的抓取即用此法：627 页、约 90MB 原始数据、零失败，全程约 6 分钟（3 并发 + 限速）。

## 中文版（vic3-wiki-zh）

对 en 镜像逐页用 glm-5.3 翻译，`2026-10-27` 生成。要点：

- **保留的英文**：代码块、控制台命令与脚本标识符、文件路径、URL/HTML/图片语法、数字单位；
  链接目标全部原样（文件名与 en 版一致，站内互链在 zh 目录内照常可点）。
- **术语**：`glossary_zh.json` 里的官方中文译名强制执行；表外术语首次出现中文＋英文括注。
- **保真机制**：发送前把链接目标替换成 `{#n}` 占位符、译文返回后程序化还原（模型不可能改写目标）；
  每块校验围栏/图片/链接/标题数量，不合格带失败原因重试，仍不合格记 fail（重跑脚本自动补翻）。
- **front matter**：原字段保留，顶部注入 `translated` / `translator` 元数据。
- 运行：`python scripts/vic3-wiki/translate_to_zh.py`（已完成文件自动跳过；`--force` 重翻；
  `--only a.md,b.md` / `--limit N` / `--workers n` 可选）。翻译后跑 `verify_zh.py` 做全量结构校验。

### 内容风控与离线词典补翻（2026-10-29）

glm 端点的内容风控（HTTP 400 / 错误码 1301）拦下了一批页面——触发点高度集中：
俄国/中东相关页共享的「Releasable（可释放国家）」导航框行（Altai、Assyria、Israel、
Kurdistan、Palestine、Uyghuristan 等名称同现一行），以及日本内容补丁说明等。补翻路径：

1. `translate_blocked.py`：多模型级联（glm-4.7 → 4.6 → 4.5-air → 5.3）+ 对半分块递归；
   大部分页面由此完成，少数叶子片段保留英文。
2. `fill_blocked.py`：兜底填英文原版（translator 标注 kept-english）。
3. **离线词典补翻**（最终清零手段，零 LLM 调用、天然不触发风控）：
   - `build_tm.py` 先从 603 个已译文件构建 TM（行级译文 5.5 万条 + 名称词典 5 千条，
     锚点对齐 + 全语料投票去噪）；
   - `translate_dict.py` 分层翻译：整行 TM（导航框/信息框/表格整行复用现成译文）→
     句级 TM → 句式模板（国家页导语、军队编制句、成立条件、补丁动词句式等，捕获组递归）→
     术语/名称最长匹配替换（长句要求 75% 已知词占比，宁缺毋滥，翻不好保留英文）；
   - 术语自动从 TM 的独立短行收割（信息框标签/值），增补词条均取自全站已用的官方译名。

词典层完成了最后 26 个整页 + 9 个残块。**遗留**：Israel、Patch 1.13 等页的长段独特散文
（历史背景/攻略/风味文本）词典无法保证语序，保留英文——front matter 的 translator 字段
标注了 `dictionary`，`python scripts/vic3-wiki/_status_now.py` 可随时复查。

## 已知取舍

- 图片不落本地，Markdown 里指向线上 `vic3.paradoxwikis.com/images/...`。
- 表格的 rowspan/colspan 展平、单元格内嵌套表格压成纯文本（Markdown 表格能力所限）。
- 站内链接尽量解析为本地 `.md` 相对链接；未镜像目标（文件、模板、跨命名空间页）保留线上绝对 URL。
