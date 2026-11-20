# -*- coding: utf-8 -*-
"""离线词典补翻（零 LLM 调用，不触发内容风控）。

对象：vic3-wiki-zh 里 front matter 标注 kept-english 的整页 + 含
`<!-- untranslated: blocked by content filter -->` 残块的文件。

翻译分层（每行依次尝试，命中即止）：
  1. 整行 TM：build_tm.py 从已译文件对齐投票出的行级译文（最高置信）；
  2. 人工词典：MANUAL_LINES 整行条目；
  3. 句式模板：RULES 正则模板，捕获组递归走同一管线；
  4. 术语替换：术语/名称最长匹配（术语自动从 TM 的独立短行收割 + 人工增补），
     已知词占比过低的行保留英文（宁缺毋滥）。

结构保真：链接目标、图片、代码块、围栏、标题层级全部原样；写盘前逐文件
对照 en 源校验围栏/图片/链接/标题计数，不一致则拒写。

用法：
    python scripts/vic3-wiki/translate_dict.py            # 处理全部剩余文件
    python scripts/vic3-wiki/translate_dict.py --only "Altai.md,Patch 1.13.md"
    python scripts/vic3-wiki/translate_dict.py --dry-run  # 只出报告不写盘
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "游戏wiki" / "vic3-wiki-en"
DST = ROOT / "游戏wiki" / "vic3-wiki-zh"
TM_PATH = ROOT / ".cache" / "vic3-wiki-zh" / "tm.json"
GLOSSARY = Path(__file__).resolve().parent / "glossary_zh.json"
TODAY = "2026-10-29"

FENCE_RE = re.compile(r"^\s*```")
LINKFULL_RE = re.compile(r"(!?\[[^\]]*\])\(([^)\n]*)\)")
IMG_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]*)\)")
HEAD_RE = re.compile(r"^(#{1,6})\s+(.*)$")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
ALPHA_RE = re.compile(r"[A-Za-z]")
MARKER = "<!-- untranslated: blocked by content filter -->"

# ---------------------------------------------------------------- 人工数据

NAME_OVERRIDES = {
    "West Siberia": "西西伯利亚",
    "East Siberia": "东西伯利亚",
    "Far East (Siberia)": "远东（西伯利亚）",
}

EXTRA_TERMS = {
    "releasable country": "可释放国家",
    "formable country": "可成立国家",
    "journal entry": "日志条目",
    "Journal Entry": "日志条目",
    "law variant": "法律变体",
    "character interaction": "角色互动",
    "government type": "政体类型",
    "Government Type": "政体类型",
    "primary culture": "主流文化",
    "Primary Cultures": "主流文化",
    "state religion": "国教",
    "State Religion": "国教",
    "country tier": "国家层级",
    "Country Tier": "国家层级",
    "country type": "国家类型",
    "Country Type": "国家类型",
    "capital state": "首都州",
    "core state": "核心州",
    "Core states": "核心州",
    "state traits": "州特质",
    "State Traits": "州特质",
    "arable land": "可耕地",
    "Arable Land": "可耕地",
    "homelands": "家园",
    "Homelands": "家园",
    "naval invasion": "海上入侵",
    "sea node": "海路节点",
    "strategic region": "战略区域",
    "interest group": "利益集团",
    "Interest Group": "利益集团",
    "power bloc": "强权集团",
    "Power Bloc": "强权集团",
    "Power Bloc Principle": "强权集团原则",
    "ship type": "舰船类型",
    "Ship Construction": "舰船建造",
    "Naval Doctrine": "海军学说",
    "naval mission": "海军任务",
    "Naval Missions": "海军任务",
    "Supply Ships": "补给舰",
    "supply route": "补给线",
    "Logistics Center": "后勤中心",
    "Merchant Marine": "商船队",
    "port connection": "港口连接",
    "trade good": "贸易商品",
    "prestige good": "威望商品",
    "unique building": "特色建筑",
    "free company": "自由佣兵公司",
    "decision": "决议",
    "Decision": "决议",
    "Diplomatic Action": "外交行动",
    "diplomatic play": "外交博弈",
    "Orchestrate Coup": "策划政变",
    "gunboat diplomacy": "炮舰外交",
    "Naval Hostilities": "海上敌对",
    "Ship Transfer Treaty": "舰船移交条约",
    "treaty article": "条约条款",
    "Port Bombardment": "港口炮击",
    "Hunt Pirates": "缉捕海盗",
    "Protect Supply Lines": "保护补给线",
    "construction queue": "建造队列",
    "character pool": "角色池",
    "National Cast": "国家角色库",
    "Prominence": "显赫度",
    "Popularity": "人气",
    "Manor House": "庄园宅邸",
    "Financial District": "金融区",
    "Holding building": "控股建筑",
    "Magnate": "豪商",
    "assimilation": "同化",
    "incorporated state": "整合州",
    "marginalized": "边缘化",
    "colonization": "殖民",
    "expansion pack": "扩展包",
    "main menu": "主菜单",
    "User Interface": "用户界面",
    "loadout": "配置",
    "devastation": "破坏度",
    "Piracy": "海盗活动",
    "Privateering": "私掠",
    "pirate fleet": "海盗舰队",
    "sea route": "海路",
    "sea zone": "海域",
    "strait": "海峡",
    "Naval Fortification": "海军要塞",
    "transportation capacity": "运输承载",
    "Troop Transportation": "部队运输",
    "naval combat": "海战",
    "Naval Combat": "海战",
    "hull damage": "船体损伤",
    "crew damage": "船员损伤",
    "formation": "编制",
    "military formation": "军事编制",
    "command limit": "指挥上限",
    "Marines": "海军陆战队",
    "Diplomatic Interest": "外交利益",
    "lobby": "政治游说集团",
    "political machine": "政治机器",
    "succession crisis": "继承危机",
    "Tokugawa": "德川",
    "Shogun": "将军",
    "Bakufu": "幕府",
    "Meiji Restoration": "明治维新",
    "Iwakura Mission": "岩仓使节团",
    "Zaibatsu": "财阀",
    "Tenpō Crisis": "天保危机",
    "Sakoku": "锁国",
    "Isolationism": "孤立主义",
    "Locked Country": "锁国令",
    "Ryukyu Kingdom": "琉球王国",
    "Hokkaido": "北海道",
    "earthquake": "地震",
    "Lacquer": "漆器",
    "ukiyo-e": "浮世绘",
    "Tatami": "榻榻米",
    "modder": "模组作者",
    "aka": "又名",
    "fascist government": "法西斯政府",
    "Presidential Republic": "总统共和制",
    "Parliamentary Republic": "议会共和制",
    "Council Republic": "委员会共和制",
    "Corporate State": "企业国家",
    "Technocracy": "技术官僚制",
    "Theocracy": "神权制",
    "Monarchy": "君主制",
    "State Atheism": "国家无神论",
    "Autocracy": "独裁制",
    "Oligarchy": "寡头制",
    "Dictatorial": "独裁",
    "Principality": "公国",
    "Kingdom": "王国",
    "Empire": "帝国",
    "City-State": "城邦",
    "Great Power": "列强",
    "Major Power": "主要政权",
    "Minor Power": "次要政权",
    "Insignificant Power": "无关紧要政权",
    "Unrecognized": "未受认可",
    "Recognized": "受承认",
    "recognized country": "受认可国家",
    "unrecognized power": "未受认可政权",
    "Puppet": "傀儡国",
    "Protectorate": "保护国",
    "Dominion": "自治领",
    "Personal Union": "君合国",
    "Vassal": "附庸国",
    "Tributary": "朝贡国",
    "liberty desire": "独立倾向",
    "civil war": "内战",
    "revolution": "革命",
    "Sunni": "逊尼派",
    "Shia": "什叶派",
    "Gelugpa": "格鲁派",
    "Protestant": "新教",
    "Catholic": "天主教",
    "Orthodox": "东正教",
    "Confucian": "儒教",
    "Arabian Peninsula": "阿拉伯半岛",
    "landlocked": "内陆",
    "Releasable": "可释放国家",
    "Formable": "可成立国家",
    "region": "地区",
    "superregion": "超区域",
    "Decentralized": "松散政权",
    "decentralized nation": "松散政权",
    "References": "参考",
    "Resources": "资源",
    "Name": "名称",
    "Size": "规模",
    "Uses": "用途",
    "Livestock Ranch": "畜牧场",
    "Russian": "俄罗斯",
    # 建筑与生产
    "Wheat Farm": "小麦农场",
    "Wheat Farms": "小麦农场",
    "Cotton Plantation": "棉花种植园",
    "Opium Plantation": "鸦片种植园",
    "Silk Plantation": "丝绸种植园",
    "Tea Plantation": "茶叶种植园",
    "Coffee Plantation": "咖啡种植园",
    "Sugar Plantation": "蔗糖种植园",
    "Banana Plantation": "香蕉种植园",
    "Dye Plantation": "染料种植园",
    "Tobacco Plantation": "烟草种植园",
    "Rubber Plantation": "橡胶种植园",
    "Vineyard": "葡萄园",
    "Vineyards": "葡萄园",
    "Logging Camp": "伐木场",
    "Logging Camps": "伐木场",
    "Barracks": "兵营",
    "Naval Base": "海军基地",
    "Port": "港口",
    "Shipyard": "造船厂",
    "Shipyards": "造船厂",
    # 军事
    "Battalions": "营",
    "Conscripts": "征召兵",
    "Flotillas": "分舰队",
    "Flotilla": "分舰队",
    "Irregular Infantry": "非正规步兵",
    "No Organized Training": "无组织训练",
    "Professional Army": "职业陆军",
    "Peasant Levies": "农民征召",
    "Naval Traditions": "航海传统",
    "one army": "一个集团军",
    "a single army": "一个集团军",
    "two armies": "两个集团军",
    "one fleet": "一支舰队",
    "a single fleet": "一支舰队",
    "army": "集团军",
    "fleet": "舰队",
    "Generals": "将军",
    "Admirals": "海军上将",
    # 文化与民族
    "Kazakh": "哈萨克",
    "Uzbek": "乌兹别克",
    "Kyrgyz": "吉尔吉斯",
    "Turkmen": "土库曼",
    "Tajik": "塔吉克",
    "Uighur": "维吾尔",
    "Hazara": "哈扎拉",
    "Pashtun": "普什图",
    "Baluchi": "俾路支",
    "Persian": "波斯",
    "Kurdish": "库尔德",
    "Jewish": "犹太",
    "Ashkenazi": "阿什肯纳兹",
    "Sephardim": "塞法迪",
    "Mongol": "蒙古",
    "Zhuz": "玉兹",
    "cultures": "文化",
    # 地名
    "Uralsk": "乌拉尔斯克",
    "Syrdarya": "锡尔河",
    "Semipalatinsk": "塞米巴拉金斯克",
    "Akmolinsk": "阿克莫林斯克",
    "Chelyabinsk": "车里雅宾斯克",
    "Aktobe": "阿克托别",
    "Samara": "萨马拉",
    "Tashkent": "塔什干",
    "Samarkand": "撒马尔罕",
    "Uzbekia": "乌兹别克尼亚",
    "Chorasmia": "花剌子模",
    "Turkmenia": "土库曼尼亚",
    "Fergana": "费尔干纳",
    "Kabulistan": "喀布尔斯坦",
    "Hazaristan": "哈扎拉斯坦",
    "Khorasan": "呼罗珊",
    "Kirghizia": "吉尔吉斯",
    "Tajikistan": "塔吉克斯坦",
    "Kazakh steppe": "哈萨克草原",
    "Zanzibar": "桑给巴尔",
    "Muscat": "马斯喀特",
    "Tanganyika": "坦噶尼喀",
    "Lindi": "林迪",
    "Kenya": "肯尼亚",
    "Rift Valley": "裂谷",
    "Palestine": "巴勒斯坦",
    "Arabian peninsula": "阿拉伯半岛",
    "Arabian minors": "阿拉伯小国",
    # 制度与概念
    "Nationalism": "民族主义",
    "Pan-nationalism": "泛民族主义",
    "split state": "拆分州",
    "split states": "拆分州",
    "princely state": "土邦",
    "princely states": "土邦",
    "tributaries": "朝贡国",
    "Khanate": "汗国",
    "Emirate": "埃米尔国",
    "Sultanate": "苏丹国",
    "Heir": "继承人",
    "Population": "人口",
    "population": "人口",
    "claims": "宣称",
    "resources": "资源",
    "oil": "石油",
    "coal": "煤",
    "iron": "铁",
    "wood": "木材",
    "Devout": "虔信派",
    "World Market Hub": "世界市场中心",
    "Trade Center": "贸易中心",
    "tolls": "通行费",
    "outliner": "大纲",
    "Formation": "编制",
    "formation panel": "编制面板",
    "Nation": "国家",
    "nations": "国家",
    # 补丁小节标签
    "Flagships": "旗舰",
    "Narrative content": "叙事内容",
    "Art": "美术",
    "Music": "音乐",
    "Improvements": "改进",
    "Features": "特性",
    "Balance": "平衡",
    "Bugfixes": "错误修复",
    "Interface": "界面",
    "AI": "AI",
    # 数字词（捕获组里常见，含首字母大写形态）
    "one": "一",
    "two": "二",
    "three": "三",
    "four": "四",
    "five": "五",
    "six": "六",
    "seven": "七",
    "eight": "八",
    "nine": "九",
    "ten": "十",
    "eleven": "十一",
    "twelve": "十二",
    "sixteen": "十六",
    "twenty": "二十",
    "Three": "三",
    "Six": "六",
    "Eight": "八",
    "Ten": "十",
    "One": "一",
    "Two": "二",
    "Four": "四",
    "Five": "五",
    "Seven": "七",
    "Nine": "九",
    # 其他高频
    "central Asia": "中亚",
    "Central Asia": "中亚",
    "Middle East": "中东",
    "Jerusalem": "耶路撒冷",
    "minors": "小国",
    "Turkestani": "突厥斯坦",
    "Starting states": "开局州",
    "Tier": "等级",
    "Country": "国家",
    "Western Steppe": "西大草原",
    "Irtysh River": "额尔齐斯河",
    "Ranches": "牧场",
    "Rye Farm": "黑麦农场",
    "Ili": "伊犁",
    "Moderate": "温和派",
    "Kazakh Reunification": "哈萨克重归统一",
    "homeland states": "家园州",
    "constituent countries": "组成国家",
    # 日志/事件单元格短语
    "One of the following:": "以下任一：",
    "weighted chance of:": "加权概率：",
    "For other countries:": "对其他国家：",
    "Triggers event": "触发事件",
    "Has researched": "已研究",
    "visibility conditions": "可见条件",
    "at least": "至少",
    "has reached": "已达到",
    "Either": "任一",
    "below": "低于",
    "progress": "进度",
    "country rank": "国家等级",
    "No": "无",
}

MANUAL_LINES = {}

# 句式模板：正则（作用于剥掉行首符号后的文本）→ 中文模板；{0}{1}… 为捕获组，递归翻译后填充
RULES = [
    # ---- 国家页导语 ----
    (re.compile(r"^\*\*(.+?)\*\* is a \[formable country\]\(([^)]+)\) in (.+?)\. It can be formed by any nation with (?:a )?(.+?) primary culture\.?$"),
     "**{0}**是{2}的一个[可成立国家]({1})。任何以{3}为主文化的国家均可成立它。"),
    (re.compile(r"^\*\*(.+?)\*\* \(called \*\*(.+?)\*\* at the start\) is a (.+?) in the (.+?)\. (.+)$"),
     "**{0}**（开局称为**{1}**）是{3}的一个{2}。{4}"),
    (re.compile(r"^\*\*(.+?)\*\* \(called \*\*(.+?)\*\* at the start\) is a (.+?) in the (.+?)\.$"),
     "**{0}**（开局称为**{1}**）是{3}的一个{2}。"),
    (re.compile(r"^\*\*(.+?)\*\* is a \[releasable country\]\(([^)]+)\) in the (.+?) (region|superregion)\. It can be released by any country controlling its capital\.$"),
     "**{0}**是{2}{3}的一个[可释放国家]({1})。任何控制其首都的国家均可将其释放。"),
    (re.compile(r"^\*\*(.+?)\*\* is a \[releasable country\]\(([^)]+)\) in the (.+?) (region|superregion)\.$"),
     "**{0}**是{2}{3}的一个[可释放国家]({1})。"),
    (re.compile(r"^\*\*(.+?)\*\* is an? (.+?) in the (.+?)\. (.+)$"),
     "**{0}**是{2}的一个{1}。{3}"),
    (re.compile(r"^At the start of the game, it is controlled by \[(.+?)\]\(([^)]+)\), (.+)$"),
     "游戏开局时，它处于[{0}]({1})的控制之下，{2}。"),
    (re.compile(r"^At the start of the game, it is controlled by \[(.+?)\]\(([^)]+)\)\.$"),
     "游戏开局时，它处于[{0}]({1})的控制之下。"),
    (re.compile(r"^(.+?) can also be released if China fails the \[(.+?)\]\(([^)]+)\) journal entry\.$"),
     "若大清未能完成[{1}]({2})日志条目，{0}也可被释放。"),
    (re.compile(r"^(.+?) can (?:also )?be released if (.+)$"),
     "若{1}，{0}也可被释放。"),
    (re.compile(r"^It can form \[(.+?)\]\(([^)]+)\) and \[(.+?)\]\(([^)]+)\)\.$"),
     "它可以成立[{0}]({1})和[{2}]({3})。"),
    (re.compile(r"^It can form \[(.+?)\]\(([^)]+)\)\.$"),
     "它可以成立[{0}]({1})。"),
    (re.compile(r"^It can be released by any country controlling its capital\.$"),
     "任何控制其首都的国家都可以将其释放。"),
    # ---- 动态地图色条件 ----
    (re.compile(r"^Was formed by (.+)$"), "由{0}成立"),
    (re.compile(r"^Has a fascist government$"), "拥有法西斯政府"),
    (re.compile(r"^A fascist government requires: (.+)$"), "法西斯政府需要：{0}"),
    (re.compile(r"^Is a recognized country$"), "是受认可国家"),
    (re.compile(r"^Has (.+?) and does \*\*not\*\* have (.+)$"), "拥有{0}且**不**拥有{1}"),
    (re.compile(r"^Does not have (.+)$"), "不拥有{0}"),
    (re.compile(r"^Has (.+?) or (.+)$"), "拥有{0}或{1}"),
    (re.compile(r"^Has (.+?) and (.+)$"), "拥有{0}与{1}"),
    (re.compile(r"^Has (.+)$"), "拥有{0}"),
    (re.compile(r"^Is (.+)$"), "是{0}"),
    (re.compile(r"^Default$"), "默认"),
    # ---- 日志条目表格标签 ----
    (re.compile(r"^Invalidation conditions: (.+?) \| Effects when invalid: (.+)$"), "失效条件：{0} | 失效时效果：{1}"),
    (re.compile(r"^Invalidation conditions: (.+)$"), "失效条件：{0}"),
    (re.compile(r"^Effects when invalid: (.+)$"), "失效时效果：{0}"),
    (re.compile(r"^Times out after (\d+) years with the following effects: (.+)$"), "{0} 年后超时，效果如下：{1}"),
    (re.compile(r"^Is triggered by: (.+)$"), "触发方式：{0}"),
    (re.compile(r"^Trigger conditions: (.+)$"), "触发条件：{0}"),
    (re.compile(r"^Immediate effects: (.+)$"), "立即效果：{0}"),
    (re.compile(r"^Completion conditions: (.+?) \| Effects when completed: (.+)$"), "完成条件：{0} | 完成时效果：{1}"),
    (re.compile(r"^Effects when completed: (.+)$"), "完成时效果：{0}"),
    (re.compile(r"^Failure conditions: (.+?) \| Effects when failed: (.+)$"), "失败条件：{0} | 失败时效果：{1}"),
    (re.compile(r"^Failure conditions: (.+)$"), "失败条件：{0}"),
    (re.compile(r"^Visibility conditions: (.+?) \| Effects when activated: (.+)$"), "可见条件：{0} | 激活时效果：{1}"),
    (re.compile(r"^Activated by: (.+?) \| Effects when activated: (.+)$"), "激活方式：{0} | 激活时效果：{1}"),
    (re.compile(r"^Option conditions Enabled if: (.+?) Offer (.+)$"), "选项条件——启用条件：{0}——提供{1}"),
    (re.compile(r"^Option conditions Disabled if: (.+?) Offer (.+)$"), "选项条件——禁用条件：{0}——提供{1}"),
    (re.compile(r"^All of our (.+?) subjects are Puppets and have no more than (\d+) liberty desire$"),
     "我们所有的{0}附属国均为傀儡国，且独立倾向不高于 {1}"),
    (re.compile(r"^Any civil war has reached (\d+)% progress$"), "任一内战进度达到 {0}%"),
    (re.compile(r"^Country rank is below (.+)$"), "国家排名低于{0}"),
    (re.compile(r"^Trigger event (.+)$"), "触发事件{0}"),
    (re.compile(r"^Activates the (.+?) journal entry$"), "激活{0}日志条目"),
    (re.compile(r"^Sets a random interest group that endorses (.+?) or the (.+?) as the \"(.+?)\" Interest Group$"),
     "将一个支持{0}或{1}的随机利益集团设为“{2}”利益集团"),
    (re.compile(r"^Event after game start$"), "游戏开始后的事件"),
    (re.compile(r"^None$"), "无"),
    # ---- 政体表 ----
    (re.compile(r"^Either: (.+)$"), "任一：{0}"),
    (re.compile(r"^Either (.+)$"), "任一：{0}"),
    (re.compile(r"^Capital in (.+?) or (.+?) region$"), "首都位于{0}或{1}地区"),
    (re.compile(r"^Capital in (.+)$"), "首都位于{0}"),
    (re.compile(r"^The following \[companies\]\(([^)]+)\) are associated with (.+?), its constituent countries, or its homeland states: (.+)$"),
     "以下[公司]({0})与{1}、其组成国家或其家园州相关联：{2}"),
    (re.compile(r"^The following \[companies\]\(([^)]+)\) are associated with (.+?), or its homeland states: (.+)$"),
     "以下[公司]({0})与{1}或其家园州相关联：{2}"),
    (re.compile(r"^The following \[companies\]\(([^)]+)\) are associated with (.+?), its constituent countries, or its homeland states:$"),
     "以下[公司]({0})与{1}、其组成国家或其家园州相关联："),
    (re.compile(r"^The following \[companies\]\(([^)]+)\) are associated with (.+?), or its homeland states:$"),
     "以下[公司]({0})与{1}或其家园州相关联："),
    (re.compile(r"^([\w]+) of the ([\w]+) core states are needed in order to form (.+?); the dashed states are considered cores for releasing (.+)$"),
     "成立{2}需要其{1}个核心州中的{0}个；虚线州在释放{3}时视为核心州。"),
    (re.compile(r"^(.+?) can also be released, in which case all ([\w]+) (.+?) homelands are considered its core states\.$"),
     "{0}也可被释放，此时其全部{1}个{2}家园均视为其核心州。"),
    (re.compile(r"^(.+?) has ([\w]+) core states, which comprise most of its primary culture's homelands\. Its core states mostly correspond to the modern country of (.+?)\.$"),
     "{0}拥有{1}个核心州，涵盖其主流文化的大部分家园。其核心州大致对应于现代的{2}。"),
    (re.compile(r"^\[Ruler Title\] \[Ruler Name\] has unified the (.+?) people under one banner\.$"),
     "[Ruler Title] [Ruler Name]将{0}人民统一在了一面旗帜之下。"),
    (re.compile(r"^(.*?)Split states in: ?(.*)$"), "{0}拆分州位于：{1}"),
    (re.compile(r"^(.*?)Split states in (.*)$"), "{0}拆分州位于{1}"),
    # ---- 军队/成立/统治者模板句（与语料 glm 译法同风格）----
    (re.compile(r"^(.+?) starts with (\d+|one|two|three|four|five|six|seven|eight|nine|ten) Battalions and can call upon ([\d]+|one|two|three|four|five|six|seven|eight|nine|ten) Conscripts?\. All Barracks use No Organized Training\. The battalions compose (.+?)\.$"),
     "{0}开局拥有 {1} 个营，并可征召 {2} 个营。所有兵营均使用“无组织训练”。这些营编成{3}。"),
    (re.compile(r"^(.+?) begins with (\d+|one|two|three|four|five) regular battalions and can call on (\d+|one|two|three|four|five|six|seven|eight|nine) conscripts\. All Barracks use No Organized Training\. The battalions compose (.+?)\.$"),
     "{0}开局拥有 {1} 个常规营，并可征召 {2} 个营。所有兵营均使用“无组织训练”。这些营编成{3}。"),
    (re.compile(r"^(.+?) starts with (?:no )?(\d+|one|two|three|four|five|six) Flotillas?\. All Naval Bases use Naval Traditions\. The flotillas compose (.+?)\.$"),
     "{0}开局拥有 {1} 支分舰队。所有海军基地均使用“航海传统”。这些分舰队编成{2}。"),
    (re.compile(r"^(.+?) starts with (.+?) and split states in (.+?)\.?$"),
     "{0}开局拥有{1}，并在{2}拥有拆分州。"),
    (re.compile(r"^(.+?) can continue on to form \[(.+?)\]\(([^)]+)\)\.$"),
     "{0}可以继续成立[{1}]({2})。"),
    (re.compile(r"^It may go on to form \[(.+?)\]\(([^)]+)\) and \[(.+?)\]\(([^)]+)\)\.$"),
     "它可以继续成立[{0}]({1})和[{2}]({3})。"),
    (re.compile(r"^(.+?) can be formed by the following nations when they control at least ([\w]+) of its ([\w]+) core states and have researched (.+?)\.?$"),
     "{0}可由以下国家成立：控制其{2}个核心州中的至少{1}个，且已研究{3}。"),
    (re.compile(r"^The following countries can form (.+?) when they fully control one of its ([\w]+) core states?\.?$"),
     "下列国家在完全控制其{1}个核心州之一时，可以成立{0}。"),
    (re.compile(r"^(.+?) is ruled by (.+?)\.?$"),
     "{0}由{1}统治。"),
    (re.compile(r"^(.+?) has the (.+?) law\.$"),
     "{0}拥有“{1}”法律。"),
    (re.compile(r"^([\d. ↑]+)Links to (\w+) Wikipedia article$"),
     "{0}链接到{1}语维基百科条目"),
    (re.compile(r"^(.+?) § (.+)$"),
     "{0} § {1}"),
    (re.compile(r"^([\w &'/-]{2,40}):$"),
     "{0}："),
    # ---- 补丁说明句式（动词开头）----
    (re.compile(r"^Added (?:the )?(.+?), which allows you to (.+?)\. (.+)$"), "新增了{0}，它允许你{1}。{2}"),
    (re.compile(r"^Added (?:the )?(.+?), which allows you to (.+?)\.?$"), "新增了{0}，它允许你{1}。"),
    (re.compile(r"^Added (?:a |an )?(.+?), which allows (.+?) to (.+?)\.?$"), "新增了{0}，允许{1}{2}。"),
    (re.compile(r"^Added a new (.+?) to the game along with (.+)$"), "为游戏新增了{0}，以及{1}"),
    (re.compile(r"^Added (?:a |an |the )?new (.+?) to the game$"), "为游戏新增了{0}"),
    (re.compile(r"^Added (\d+) (.+?) to the game$"), "为游戏新增了 {0} 个{1}"),
    (re.compile(r"^Added (?:a |an )?new (.+?), (.+)$"), "新增了{0}，{1}"),
    (re.compile(r"^Added (?:several |numerous )?(.+?) for (.+)$"), "为{1}新增了{0}"),
    (re.compile(r"^Added (.+?) for Japan$"), "为日本新增了{0}"),
    (re.compile(r"^Added (.+)$"), "新增了{0}"),
    (re.compile(r"^Fixed an issue where (.+?)(?: when (.+))?\.$"), "修复了{0}的问题。"),
    (re.compile(r"^Fixed an issue where (.+)$"), "修复了{0}的问题"),
    (re.compile(r"^Fixed a bug where (.+)$"), "修复了{0}的错误"),
    (re.compile(r"^Fixed (.+)$"), "修复了{0}"),
    (re.compile(r"^Reworked the (.+?) content for (.+)$"), "重做了{1}的{0}内容"),
    (re.compile(r"^(?:Completely reworked|Reworked) (.+?) entirely\. (.+)$"), "彻底重做了{0}。{1}"),
    (re.compile(r"^Completely reworked (.+?)\. (.+)$"), "彻底重做了{0}。{1}"),
    (re.compile(r"^Reworked how (.+?) works\. (.+)$"), "重做了{0}的运作方式。{1}"),
    (re.compile(r"^Reworked (.+)$"), "重做了{0}"),
    (re.compile(r"^Removed (.+?)\. (.+)$"), "移除了{0}。{1}"),
    (re.compile(r"^Removed (.+)$"), "移除了{0}"),
    (re.compile(r"^Changed (.+)$"), "变更了{0}"),
    (re.compile(r"^Updated (.+)$"), "更新了{0}"),
    (re.compile(r"^Adjusted (?:a number of )?(.+)$"), "调整了{0}"),
    (re.compile(r"^Increased (.+)$"), "提高了{0}"),
    (re.compile(r"^(?:Reduced|Decreased) (.+)$"), "降低了{0}"),
    (re.compile(r"^Improved (.+)$"), "改进了{0}"),
    (re.compile(r"^Optimized (.+)$"), "优化了{0}"),
    (re.compile(r"^Made (.+)$"), "使{0}"),
    (re.compile(r"^Merged (.+?) (?:back )?into (.+)$"), "将{0}合并回{1}"),
    (re.compile(r"^Consolidated (.+?) around the world as part of (.+)$"), "作为{1}更新的一部分，合并了世界各地的{0}"),
    (re.compile(r"^Over (\d+) (.+?) were added with the help of (.+)$"), "在{2}的帮助下新增了超过 {0} 位{1}"),
    (re.compile(r"^Japan now (?:begins the game with|starts with) (.+)$"), "日本现在开局拥有{0}"),
    (re.compile(r"^(.+?) now (?:begins the game with|starts with) (.+)$"), "{0}现在开局拥有{1}"),
    (re.compile(r"^(.+?) now only have (.+)$"), "{0}现在只有{1}"),
    (re.compile(r"^(.+?) now have (.+)$"), "{0}现在拥有{1}"),
    (re.compile(r"^(.+?) can now (.+)$"), "{0}现在可以{1}"),
    (re.compile(r"^(.+?) will now (.+)$"), "{0}现在将{1}"),
    (re.compile(r"^(.+?) will no longer (.+)$"), "{0}不再{1}"),
    (re.compile(r"^(.+?) are now (.+)$"), "{0}现在是{1}"),
    (re.compile(r"^(.+?) is now (.+)$"), "{0}现在是{1}"),
    (re.compile(r"^Characters? (?:will no longer|no longer) (.+)$"), "角色不再{0}"),
    (re.compile(r"^Works much akin to (.+?), but (.+)$"), "运作方式类似{0}，但{1}"),
    (re.compile(r"^You can now (.+)$"), "你现在可以{0}"),
    (re.compile(r"^You'll earn (.+?) from (.+)$"), "你将从{1}中获得{0}"),
    (re.compile(r"^There (?:is|are) now (.+)$"), "现在有{0}"),
    (re.compile(r"^There's now (.+)$"), "现在有{0}"),
    (re.compile(r"^They (?:also )?provide (.+)$"), "它们提供{0}"),
    (re.compile(r"^They have a (.+)$"), "它们拥有{0}"),
    (re.compile(r"^They are now (.+)$"), "它们现在是{0}"),
    (re.compile(r"^It allows a fleet to (.+)$"), "它允许舰队{0}"),
    (re.compile(r"^It works with (.+)$"), "它与{0}配合运作"),
    (re.compile(r"^It was released alongside \[(.+?)\]\(([^)]+)\) expansion pack\.$"), "它与[{0}]({1})扩展包同步发布。"),
    (re.compile(r"^If the opposing side declines the treaty you can (.+)$"), "若对方拒绝该条约，你可以{0}"),
    (re.compile(r"^If more than one dynamic color can be applied to a country, (.+)$"), "若一个国家可应用多种动态颜色，{0}"),
    (re.compile(r"^Unrecognized nations can (.+)$"), "未受认可国家可以{0}"),
    (re.compile(r"^Recognized nations also have access to a version of (.+?), that is only available while (.+)$"),
     "受认可国家也可使用{0}的一个版本，它仅在{1}期间可用"),
    (re.compile(r"^Your units will have (.+)$"), "你的部队将拥有{0}"),
    (re.compile(r"^Your fleet will only be sent out to (.+)$"), "你的舰队只会被派出{0}"),
    (re.compile(r"^All formations now have a (.+?) in their HQ, which they will trace a supply route to\.$"),
     "所有编制现在在其总部拥有{0}，并将补给线连接至此。"),
    (re.compile(r"^A formation that is overseas consumes (.+)$"), "位于海外的编制消耗{0}"),
    (re.compile(r"^A Japanese building style, which reflects (.+)$"), "一种日式建筑风格，体现了{0}"),
    (re.compile(r"^A new '(.+?)' User Interface skin, inspired by (.+)$"), "全新的“{0}”用户界面皮肤，灵感来自{1}"),
    (re.compile(r"^New clothing assets for (.+?), including;$"), "{0}的新服饰素材，包括；"),
    (re.compile(r"^New (.+?) table assets, featuring; (.+)$"), "新的{0}桌面素材，包含；{1}"),
    (re.compile(r"^Added new period appropriate music tracks to evoke (.+? era) (.+?), spread over (\d+) minutes in (\d+) tracks$"),
     "新增了贴合时代气息的音乐曲目，以唤起{0}{1}的氛围，共 {3} 首曲目、总长 {2} 分钟"),
    (re.compile(r"^featuring (.+)$"), " featuring {0}"),
    (re.compile(r"^inspired by (.+)$"), "灵感来自{0}"),
]

FUNCTION_WORDS = {
    "and": "且", "or": "或", "with": "与", "of": "", "the": "", "a": "", "an": "",
    "in": "位于", "for": "用于", "to": "", "is": "是", "are": "是", "not": "不",
    "any": "任意", "all": "所有", "no": "无", "per": "每", "via": "经由",
    "using": "使用", "from": "来自", "into": "成为",
}

# ---------------------------------------------------------------- 装载与索引

SENT_SPLIT_RE = re.compile(r"(?<=\.)\s+(?=[A-Z\*\[“\"'(])")
ZH_SPLIT_RE = re.compile(r"(。|！|？)")
URLISH_RE = re.compile(r"^(https?://|[\w .#/-]+\.(?:md|png|jpg|jpeg|html|txt|json)(?:[?#].*)?$)")


def split_en_sentences(text):
    return SENT_SPLIT_RE.split(text)


def split_zh_units(text):
    parts = ZH_SPLIT_RE.split(text)
    units, cur = [], parts[0]
    for i in range(1, len(parts), 2):
        cur += parts[i]
        units.append(cur)
        if i + 1 < len(parts):
            cur = parts[i + 1]
        else:
            cur = ""
    if cur:
        units.append(cur)
    return units

def load_all():
    tm = json.loads(TM_PATH.read_text(encoding="utf-8"))
    raw_lines = tm["lines"]
    # 键值统一去尾部空白（不同文件行尾空白不一致会导致整行 TM 命不中），票数合并
    lines_tm = {}
    for en, (zh, votes) in raw_lines.items():
        k, v = en.rstrip(), zh.rstrip()
        if k in lines_tm:
            lines_tm[k] = [v, lines_tm[k][1] + votes] if v == lines_tm[k][0] else lines_tm[k]
        else:
            lines_tm[k] = [v, votes]
    # 名称词典：剔除非正常值（中文与英文词混排的脏对齐，如 "what"→"什么  what"）
    names = {k: v[0] for k, v in tm["names"].items()
             if not (re.search(r"[\u4e00-\u9fff]", v[0]) and re.search(r"[A-Za-z]{2}", v[0]))}
    names.update(NAME_OVERRIDES)

    g = json.loads(GLOSSARY.read_text(encoding="utf-8"))
    terms = dict(EXTRA_TERMS)
    terms.update(g["terms"])

    # 从 TM 收割"独立短行"术语：en 是纯词组（无链接/表格），zh 是纯中文短语。
    # 排除短功能词（"is"→"是什么" 这类错位配对只出现在低票短行）
    STOP = set(FUNCTION_WORDS) | {"was", "were", "been", "has", "have", "had", "will",
                                  "can", "may", "this", "that", "these", "those", "from"}
    word_re = re.compile(r"^[A-Za-z][A-Za-z .&'/()-]{0,38}[A-Za-z)]$")
    for en, (zh, votes) in lines_tm.items():
        if en.lower() in STOP or not re.search(r"[A-Za-z]{3}", en):
            continue
        if (word_re.match(en) and CJK_RE.search(zh) and len(zh) <= 16
                and "|" not in zh and "[" not in zh and "(" not in zh
                and not re.search(r"[A-Za-z]{2}", zh)):
            if en not in terms or votes >= 3:
                terms.setdefault(en, zh)

    lookup = {}
    for k, v in {**terms, **names}.items():
        if len(k) < 2:
            continue
        w1m = re.match(r"[A-Za-z]+", k)
        if not w1m:
            continue
        w1 = w1m.group(0)
        lookup.setdefault(w1, []).append((k, v or k))
    for v in lookup.values():
        v.sort(key=lambda kv: -len(kv[0]))

    # 句级 TM：把行级 TM 拆成句对（句数一致且逐句链接集合一致才收录），跨行复用
    sent_votes = {}
    from collections import Counter as _C
    for en, (zh, votes) in lines_tm.items():
        if "." not in en:
            continue
        ens, zhs = split_en_sentences(en), split_zh_units(zh)
        if len(ens) != len(zhs) or not (1 <= len(ens) <= 8):
            continue
        for a, b in zip(ens, zhs):
            if (len(a) >= 8 and ALPHA_RE.search(a) and CJK_RE.search(b)
                    and not CJK_RE.search(a)
                    and sorted(LINK_RE.findall(a)) == sorted(LINK_RE.findall(b))):
                sent_votes.setdefault(a, _C())[b] += votes
    sent_tm = {a: c.most_common(1)[0][0] for a, c in sent_votes.items()}
    return lines_tm, names, lookup, sent_tm


# ---------------------------------------------------------------- 翻译管线

class Translator:
    def __init__(self):
        self.lines_tm, self.names, self.lookup, self.sent_tm = load_all()
        self.stats = Counter()
        self.miss_lines = []

    def tr_display(self, disp):
        d = disp.strip()
        if not ALPHA_RE.search(d) or CJK_RE.search(d):
            return disp
        sub, _ = self.substitute(d, aggressive=False)
        return sub if CJK_RE.search(sub) else disp

    def xlate_displays(self, text):
        """翻译文本中链接的显示部分（已是中文的跳过）。"""
        def repl(m):
            disp, tgt = m.group(1), m.group(2)
            is_img = disp.startswith("![")
            core = disp[2:-1] if is_img else disp[1:-1]
            inner = self.tr_display(core) if ALPHA_RE.search(core) else core
            wrapped = f"![{inner}]" if is_img else f"[{inner}]"
            return f"{wrapped}({tgt})"
        return LINKFULL_RE.sub(repl, text)

    def protect(self, text):
        codes, links = [], []
        def stash_code(m):
            codes.append(m.group(0))
            return f"\x00{len(codes)-1}\x00"
        text = re.sub(r"`[^`]+`", stash_code, text)
        def stash_link(m):
            links.append((m.group(1), m.group(2)))
            return f"\x01{len(links)-1}\x01"
        text = LINKFULL_RE.sub(stash_link, text)
        return text, codes, links

    def unprotect(self, text, codes, links):
        def unstash_link(m):
            disp, tgt = links[int(m.group(1))]
            is_img = disp.startswith("![")
            core = disp[2:-1] if is_img else disp[1:-1]
            inner = self.tr_display(core) if ALPHA_RE.search(core) else core
            wrapped = f"![{inner}]" if is_img else f"[{inner}]"
            return f"{wrapped}({tgt})"
        text = re.sub(r"\x01(\d+)\x01", unstash_link, text)
        return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)

    def substitute(self, text, aggressive=True):
        """术语/名称最长匹配替换。返回 (替换后文本, 已知字母占比)。"""
        if not ALPHA_RE.search(text):
            return text, 1.0
        out, known, total = [], 0, 0
        i, n = 0, len(text)
        while i < n:
            ch = text[i]
            if ch.isalpha():
                j = i
                while j < n and text[j].isalpha():
                    j += 1
                w = text[i:j]
                total += len(w)
                hit = None
                for k, v in self.lookup.get(w, ()):
                    if text.startswith(k, i):
                        e = i + len(k)
                        if e >= n or not (text[e].isalpha() or text[e] in "_-"):
                            hit = v
                            known += len(k)
                            i = e
                            break
                if hit is None:
                    lw = w.lower()
                    if aggressive and lw in FUNCTION_WORDS:
                        out.append(FUNCTION_WORDS[lw])
                        known += len(w)
                    else:
                        out.append(w)
                    i = j
                else:
                    out.append(hit)
            else:
                out.append(ch)
                i += 1
        return "".join(out), known / max(1, total)

    @staticmethod
    def join_zh(outs):
        res = ""
        for i, o in enumerate(outs):
            res += o
            if i < len(outs) - 1 and CJK_RE.search(o) and not re.search(r"[。．！？；：]$", o):
                res += "。"
        return res

    def translate_text(self, text, depth=0):
        """对无行首符号的文本做分层翻译（链接保持原样参与各层）。"""
        if not text.strip() or not ALPHA_RE.search(text):
            return text, "pass"
        if depth > 6:
            return text, "deep"
        entry = self.lines_tm.get(text)
        if entry and CJK_RE.search(entry[0]):
            self.stats["tm"] += 1
            return self.xlate_displays(entry[0]), "tm"
        if text in MANUAL_LINES:
            self.stats["manual"] += 1
            return self.xlate_displays(MANUAL_LINES[text]), "manual"
        # 多句：逐句走 句级TM→规则，全部成立才拼接（替换层的混合译文不参与组句）
        sents = split_en_sentences(text)
        if len(sents) > 1:
            outs, ok = [], True
            for s in sents:
                o, how = self.translate_unit(s, depth + 1)
                if how not in ("tm", "senttm", "rule", "manual", "pass"):
                    ok = False
                    break
                if (not CJK_RE.search(o) and ALPHA_RE.search(s) and len(s) > 3
                        and not LINKFULL_RE.fullmatch(s or "")):
                    ok = False
                    break
                outs.append(o)
            if ok and any(CJK_RE.search(o) for o in outs):
                self.stats["sent"] += 1
                return self.xlate_displays(self.join_zh(outs)), "sent"
        out, how = self.translate_unit(text, depth + 1)
        if how != "kept":
            return out, how
        self.miss_lines.append(text[:150])
        return text, "kept"

    def translate_unit(self, unit, depth=0):
        """单句/短语：句级 TM → 人工 → 规则模板 → 术语替换。"""
        if not ALPHA_RE.search(unit):
            return unit, "pass"
        zh = self.sent_tm.get(unit)
        if zh:
            self.stats["senttm"] += 1
            return self.xlate_displays(zh), "senttm"
        if unit in MANUAL_LINES:
            self.stats["manual"] += 1
            return self.xlate_displays(MANUAL_LINES[unit]), "manual"
        for pat, tpl in RULES:
            m = pat.match(unit)
            if not m:
                continue
            groups, ok = [], True
            for gi in range(1, pat.groups + 1):
                gv = m.group(gi) or ""
                if not gv:
                    groups.append("")
                    continue
                if URLISH_RE.match(gv):  # 链接目标/文件名永不翻译
                    groups.append(gv)
                    continue
                sub, _ = self.translate_text(gv, depth + 1)
                # 组没翻出来时：若本身就是名称（词典收录为保留英文，或短的首字母大写词组）可直接用
                if not CJK_RE.search(sub) and ALPHA_RE.search(gv):
                    if gv in self.names or LINKFULL_RE.fullmatch(gv):
                        sub = gv
                    elif len(gv) <= 30 and all(w[:1].isupper() or not w[:1].isalpha() for w in gv.split()):
                        sub = gv
                if (not CJK_RE.search(sub) and ALPHA_RE.search(gv) and len(gv) > 3
                        and sub != gv):
                    ok = False
                    break
                groups.append(sub)
            if ok:
                try:
                    out = tpl.format(*groups)
                except Exception:
                    continue
                if CJK_RE.search(out):
                    self.stats["rule"] += 1
                    return self.xlate_displays(out), "rule"
        stashed, codes, links = self.protect(unit)
        sub, ratio = self.substitute(stashed)
        # 长句要求更高的已知词占比：短标签/单元格 0.5，长句 0.75（避免词序杂拌）
        gate = 0.75 if len(unit) > 60 else 0.5
        if ratio >= gate and CJK_RE.search(sub):
            self.stats["subst"] += 1
            return self.unprotect(sub, codes, links), "subst"
        return unit, "kept"

    def translate_segment(self, seg):
        seg = seg.rstrip()
        # 整段 TM（含 ## 前缀、** 加粗等原始形态的键）优先
        entry = self.lines_tm.get(seg)
        if entry and CJK_RE.search(entry[0]):
            self.stats["tm"] += 1
            return self.xlate_displays(entry[0]), "tm"
        if seg in MANUAL_LINES:
            self.stats["manual"] += 1
            return self.xlate_displays(MANUAL_LINES[seg]), "manual"
        prefix, body = "", seg
        hm = HEAD_RE.match(body)
        if hm:
            prefix, body = hm.group(1) + " ", hm.group(2)
        lm = re.match(r"^(\s*(?:[-*+]|\d+\.)\s+)(.*)$", body)
        if lm:
            prefix += lm.group(1)
            body = lm.group(2)
        out, how = self.translate_text(body)
        return prefix + out, how

    def translate_line(self, line):
        line = line.rstrip("\n")
        if FENCE_RE.match(line):
            return line, "fence"
        if not line.strip():
            return line, "blank"
        if line.lstrip().startswith("|"):
            # 整行 TM 优先（导航框/表头行都有现成整行译文）
            whole = line.rstrip()
            entry = self.lines_tm.get(whole)
            if entry and CJK_RE.search(entry[0]):
                self.stats["tm"] += 1
                return self.xlate_displays(entry[0]), "tm"
            if whole in MANUAL_LINES:
                self.stats["manual"] += 1
                return self.xlate_displays(MANUAL_LINES[whole]), "manual"
            # 整行规则（"Activated by: X | Effects when activated: Y" 这类跨单元格模式）
            core = whole.strip().strip("|").strip()
            if core and ALPHA_RE.search(core):
                o, how = self.translate_text(core)
                if how in ("tm", "senttm", "rule", "sent", "manual") and CJK_RE.search(o):
                    pad = " " if whole.startswith("| ") else ""
                    return "| " + o + " |", "row_" + how
            cells, hows = [], []
            for c in whole.split("|"):
                if not c.strip():
                    cells.append(c)
                    continue
                pad_l = len(c) - len(c.lstrip())
                pad_r = len(c) - len(c.rstrip())
                oc, how = self.translate_segment(c.strip())
                cells.append(" " * pad_l + oc + " " * pad_r)
                hows.append(how)
            how = "tbl_" + (Counter(hows).most_common(1)[0][0] if hows else "-")
            return "|".join(cells), how
        return self.translate_segment(line)


# ---------------------------------------------------------------- 文件处理

def split_front_matter(text):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[: end + 5], text[end + 5:]
    return "", text


def structure_of(text):
    return {
        "fences": len([l for l in text.split("\n") if FENCE_RE.match(l)]),
        "imgs": len(IMG_RE.findall(text)),
        "links": sorted(LINK_RE.findall(text)),
        "heads": len([l for l in text.split("\n") if HEAD_RE.match(l)]),
    }


def structure_ok(a, b):
    sa, sb = structure_of(a), structure_of(b)
    return (sa["fences"] == sb["fences"] and sa["imgs"] == sb["imgs"]
            and sa["links"] == sb["links"] and sa["heads"] == sb["heads"])


def process_whole_file(name, tr, dry=False):
    raw = (SRC / name).read_text(encoding="utf-8")
    front, body = split_front_matter(raw)
    lines_out = [tr.translate_line(ln)[0] for ln in body.split("\n")]
    inject = f"translated: {TODAY}\ntranslator: machine (dictionary: tm + glossary)\n"
    out_text = front[:4] + inject + front[4:] + "\n".join(lines_out)
    if not structure_ok(raw, out_text):
        return None, "结构校验失败，拒写"
    if not dry:
        (DST / name).write_text(out_text, encoding="utf-8")
    kept = sum(1 for ln in lines_out
               if ln.strip() and ALPHA_RE.search(ln) and not CJK_RE.search(ln)
               and not FENCE_RE.match(ln) and not re.fullmatch(r"[\d. ]+|•", ln.strip()))
    return kept, len(lines_out)


def process_fragment_file(name, tr, dry=False):
    zh_raw = (DST / name).read_text(encoding="utf-8")
    out, mode = [], False
    for ln in zh_raw.split("\n"):
        if ln.strip() == MARKER:
            mode = True
            continue
        if mode:
            if CJK_RE.search(ln) or ln.startswith(("translator:", "translated:", "---")):
                mode = False
                out.append(ln)
                continue
            out.append(tr.translate_line(ln)[0])
        else:
            out.append(ln)
    new_text = "\n".join(out)
    new_text = re.sub(
        r"translator: machine \(([^);]+); [\d,]+ chars? untranslated, marked in text\)",
        r"translator: machine (\1 + dictionary)",
        new_text)
    if not structure_ok(zh_raw, new_text):
        return None, "结构校验失败，拒写"
    if not dry:
        (DST / name).write_text(new_text, encoding="utf-8")
    still, mode = 0, False
    for ln in out:
        if ln.strip() == MARKER:
            mode = True
        elif mode:
            if CJK_RE.search(ln):
                mode = False
            elif ln.strip() and ALPHA_RE.search(ln):
                still += 1
    return still, "-"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    tr = Translator()
    whole, frag = [], []
    for p in sorted(DST.glob("*.md")):
        txt = p.read_text(encoding="utf-8")
        if "kept-english" in txt[:600]:
            whole.append(p.name)
        elif MARKER in txt:
            frag.append(p.name)
    if args.only:
        sel = [x.strip() for x in args.only.split(",") if x.strip()]
        # 已处理过的文件也允许用 --only 从 en 源重跑（词典更新后局部刷新）
        whole = [n for n in sel if (SRC / n).exists() and (DST / n).exists()
                 and "kept-english" not in (DST / n).read_text(encoding="utf-8")[:600]]
        extra_whole = [n for n in sel if n not in whole and (SRC / n).exists() and (DST / n).exists()]
        whole += extra_whole
        frag = [n for n in sel if n not in whole and (DST / n).exists()
                and MARKER in (DST / n).read_text(encoding="utf-8")]
        missing = [n for n in sel if n not in whole and n not in frag]
        if missing:
            print("跳过（不存在或无残块）：", missing)

    print(f"整页 {len(whole)} 个，残块文件 {len(frag)} 个；TM 行 {len(tr.lines_tm)}，词典键 {sum(len(v) for v in tr.lookup.values())}")
    for n in whole:
        kept, total = process_whole_file(n, tr, args.dry_run)
        print(f"  [整页] {n:34s} {'写盘' if not args.dry_run else '演练'} 保留英文行 {kept}/{total}"
              if kept is not None else f"  [整页] {n:34s} 失败：{total}")
    for n in frag:
        still, info = process_fragment_file(n, tr, args.dry_run)
        print(f"  [残块] {n:50s} {'写盘' if not args.dry_run else '演练'} 剩余英文行 {still}"
              if still is not None else f"  [残块] {n:50s} 失败：{info}")
    print("\n管线统计:", dict(tr.stats))
    if tr.miss_lines:
        p = ROOT / ".cache" / "vic3-wiki-zh" / "dict_miss.txt"
        p.write_text("\n".join(tr.miss_lines), encoding="utf-8")
        print(f"保留英文的行 {len(tr.miss_lines)} 条已记录 → {p}")


if __name__ == "__main__":
    main()
