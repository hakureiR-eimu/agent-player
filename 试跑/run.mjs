#!/usr/bin/env node
// 本地试跑（docs/游戏agent/design.md 的"本地试跑"）：不接飞书，终端当群。
// 用法：
//   npm start             交互：你扮演其他玩家，逐行敲 【场景】说话人：内容
//   node run.mjs --once   只跑开局报到一轮就退出（自检用）
//   node run.mjs FRA      换一个国家跑（agents/ 下要有对应文件夹）

import readline from "node:readline";
import path from "node:path";
import fs from "node:fs";
import { fileURLToPath } from "node:url";
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-agent-sdk";
import { z } from "zod";

// ---------- 基本路径 ----------

const args = process.argv.slice(2);
const once = args.includes("--once");
const tag = args.find((a) => !a.startsWith("--")) || "GBR";

const here = path.dirname(fileURLToPath(import.meta.url));
const agentDir = path.resolve(here, "..", "agents", tag);
const memDir = path.join(agentDir, "memory");
const chatDir = path.join(agentDir, "world", "chat");

for (const d of [memDir, chatDir, path.join(agentDir, "world", "state")]) {
  fs.mkdirSync(d, { recursive: true });
}

const profile = {
  system: fs.readFileSync(path.join(agentDir, "profile", "system.md"), "utf8"),
  country: fs.readFileSync(path.join(agentDir, "profile", "country.md"), "utf8"),
};

// ---------- 终端版飞书 ----------

const colors = {
  agent: (s) => `\x1b[36m${s}\x1b[0m`, // 青
  dim: (s) => `\x1b[2m${s}\x1b[0m`,
  warn: (s) => `\x1b[33m${s}\x1b[0m`, // 黄
};

const groups = new Map(); // id -> { id, name, members: string[] }
const groupByName = new Map();
let groupSeq = 0;

function newGroup(name, members) {
  const id = `g${String(++groupSeq).padStart(3, "0")}`;
  const unique = [...new Set([tag, ...members])];
  const g = { id, name, members: unique };
  groups.set(id, g);
  groupByName.set(name, g);
  const file = path.join(chatDir, `${id}.md`);
  fs.writeFileSync(file, `# ${name}（${id}）\n\n成员：${unique.join("、")}\n\n`);
  return g;
}

newGroup("公屏", ["FRA", "GER", "RUS"]);

function ts() {
  const d = new Date();
  const p = (n) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())} ${p(d.getHours())}:${p(d.getMinutes())}:${p(d.getSeconds())}`;
}

function logChat(g, line) {
  fs.appendFileSync(path.join(chatDir, `${g.id}.md`), `${ts()} ${line}\n`);
}

// 全局配置里有"回复加后缀"一类的指令，会顺着全局 CLAUDE.md 漏进子会话；
// 出口滤掉，滤到就提示一声。
function scrub(content) {
  const out = content.replace(/\s*Ciallo[～~][^\n]*$/u, "").trimEnd();
  if (out !== content) {
    console.log(colors.warn(`（运行时：滤掉了一行全局后缀指令的残留）`));
  }
  return out;
}

function speak(g, speaker, content) {
  content = scrub(content);
  console.log(colors.agent(`\n【${g.name}】${speaker}：${content}\n`));
  logChat(g, `【${g.name}】${speaker}：${content}`);
  return content;
}

const tools = [
  tool(
    "send_message",
    "在指定群里发言。group_id 从 list_groups 拿。",
    { group_id: z.string().describe("群 ID"), content: z.string().describe("要说的话") },
    async ({ group_id, content }) => {
      const g = groups.get(group_id);
      if (!g) {
        return { content: [{ type: "text", text: `没有这个群：${group_id}。先用 list_groups 看 ID。` }], isError: true };
      }
      speak(g, tag, content);
      return { content: [{ type: "text", text: `已发到【${g.name}】（${g.members.length} 个成员在场）` }] };
    }
  ),
  tool(
    "list_groups",
    "看自己在哪些群：每行一个，ID、群名、成员。",
    {},
    async () => {
      const lines = [...groups.values()].map((g) => `${g.id} ${g.name}：${g.members.join("、")}`);
      return { content: [{ type: "text", text: lines.join("\n") || "（还不在任何群里）" }] };
    }
  ),
  tool(
    "list_members",
    "看指定群里有谁。",
    { group_id: z.string() },
    async ({ group_id }) => {
      const g = groups.get(group_id);
      if (!g) {
        return { content: [{ type: "text", text: `没有这个群：${group_id}` }], isError: true };
      }
      return { content: [{ type: "text", text: `【${g.name}】成员：${g.members.join("、")}` }] };
    }
  ),
  tool(
    "create_group",
    "拉一个新群，把想单独谈的人拉进来。members 填玩家名（国家 tag 或人名）。",
    { name: z.string().describe("群名"), members: z.array(z.string()).describe("要拉的人") },
    async ({ name, members }) => {
      const g = newGroup(name, members);
      const line = `（${tag} 建立了群「${name}」，成员：${g.members.join("、")}）`;
      console.log(colors.dim(`\n${line}\n`));
      logChat(g, line);
      return { content: [{ type: "text", text: `群「${name}」已建立，ID ${g.id}，成员：${g.members.join("、")}。可以 send_message 了。` }] };
    }
  ),
];

const terminalServer = createSdkMcpServer({
  name: "terminal",
  version: "0.1.0",
  instructions: "这些工具就是你的飞书：发言、看群、拉群。群就是聊天场景。",
  tools,
});

// ---------- 权限：读限自己文件夹，写限 memory/ ----------

const lc = (p) => path.resolve(p).toLowerCase();
const agentDirLc = lc(agentDir);
const memDirLc = lc(memDir);
const inside = (target, base) => {
  const t = lc(target);
  return t === base || t.startsWith(base + path.sep.toLowerCase());
};

async function canUseTool(toolName, input) {
  if (toolName.startsWith("mcp__terminal__")) {
    return { behavior: "allow", updatedInput: input };
  }
  const filePath = input.file_path ?? input.path; // Read/Write/Edit/Glob/Grep
  if (["Read", "Grep", "Glob"].includes(toolName)) {
    if (!filePath || inside(path.resolve(agentDir, filePath), agentDirLc)) {
      return { behavior: "allow", updatedInput: input };
    }
    return { behavior: "deny", message: `只能读自己的文件夹 agents/${tag}/ 以内的东西。` };
  }
  if (["Write", "Edit"].includes(toolName)) {
    if (filePath && inside(path.resolve(agentDir, filePath), memDirLc)) {
      return { behavior: "allow", updatedInput: input };
    }
    return { behavior: "deny", message: "只能在 memory/ 里写东西。" };
  }
  return { behavior: "deny", message: "试跑环境里只有：读自己的文件夹、写 memory/、terminal 的几个聊天工具。" };
}

// ---------- 会话 ----------

const baseOptions = {
  systemPrompt: `${profile.system}\n\n---\n\n${profile.country}`,
  cwd: agentDir,
  permissionMode: "default",
  mcpServers: { terminal: terminalServer },
  canUseTool,
};

let sessionId = null;
let busy = false;

async function runRound(prompt) {
  busy = true;
  try {
    const q = query({ prompt, options: sessionId ? { ...baseOptions, resume: sessionId } : baseOptions });
    for await (const m of q) {
      if (m.session_id) sessionId = m.session_id;
      if (m.type === "assistant") {
        for (const block of m.message.content) {
          if (block.type === "text" && block.text.trim()) {
            console.log(colors.dim(`（独白）${block.text.trim()}\n`));
          }
        }
      }
      if (m.type === "result" && m.subtype !== "success") {
        console.log(colors.warn(`（一轮出错：${m.subtype} ${m.error ?? m.result ?? ""}）`));
      }
    }
  } finally {
    busy = false;
  }
}

const opening =
  "（运行时）你刚被拉起，这是你收到的第一条消息。现在没有进行中的游戏。" +
  "请先读 profile/country.md 认一下自己是谁，顺便看一眼 world/ 里有什么；" +
  `然后用 send_message 在【公屏】群报到，说你的第一句话。`;

// ---------- 入口 ----------

console.log(`本地试跑 —— ${tag}（cwd: ${agentDir}）`);
if (!(process.env.ANTHROPIC_BASE_URL || process.env.ANTHROPIC_API_KEY || process.env.ANTHROPIC_AUTH_TOKEN)) {
  console.log(colors.warn("（环境里没有 ANTHROPIC_* 变量，认证将走 ~/.claude/settings.json）"));
}

await runRound(opening);

if (once) {
  console.log(colors.dim(`\n--once 结束。会话 ${sessionId}；聊天记录在 world/chat/，草稿在 memory/。`));
  process.exit(0);
}

console.log("接下来你扮演其他玩家，一行一条：【场景】说话人：内容（场景不存在就当场当新群建）。");
console.log("命令：/groups 看群列表，/exit 退出。\n");

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
rl.setPrompt("> ");
rl.prompt();

rl.on("line", async (raw) => {
  const line = raw.trim();
  if (!line) return void rl.prompt();
  if (line === "/exit" || line === "/quit") return void rl.close();
  if (line === "/groups") {
    for (const g of groups.values()) console.log(`${g.id} ${g.name}：${g.members.join("、")}`);
    return void rl.prompt();
  }
  if (line === "/help") {
    console.log("【场景】说话人：内容 ｜ /groups ｜ /exit");
    return void rl.prompt();
  }
  if (busy) {
    console.log(colors.dim("（上一轮还在跑，这句先丢了）"));
    return void rl.prompt();
  }
  const m = line.match(/^【([^】]+)】([^：:]+)[：:](.*)$/);
  if (!m) {
    console.log(colors.warn("格式不对，要 【场景】说话人：内容"));
    return void rl.prompt();
  }
  const [, scene, speaker, content] = m;
  let g = groupByName.get(scene);
  if (!g) {
    g = newGroup(scene, [speaker, "你"]);
    console.log(colors.dim(`（场景「${scene}」原来没有，已当新群建起来，ID ${g.id}）`));
  }
  logChat(g, `【${g.name}】${speaker}：${content}`);
  await runRound(line);
  rl.prompt();
}).on("close", () => {
  console.log(colors.dim(`\n收工。会话 ${sessionId ?? "无"}。`));
  process.exit(0);
});
