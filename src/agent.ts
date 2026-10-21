// 真正的 agent：一个国家一个 Claude Agent SDK 会话（同一进程里的多会话，不是多进程）。
// 阶段一在试跑环境里验证过的组装方式原样搬过来：profile 拼系统提示词、cwd 是自己的
// 文件夹、权限读限自己写限 memory/、聊天走 MCP 工具；飞书的实现换成本运行时的回调。

import path from "node:path";
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-agent-sdk";
import { z } from "zod";
import { log } from "./bus.js";
import type { AgentState } from "./types.js";

/** 运行时替 agent 办事的四个入口，gameManager 实现。 */
export interface AgentToolContext {
  send(tag: string, groupId: string, content: string): Promise<string>;
  listGroups(tag: string): string;
  listMembers(tag: string, groupId: string): string;
  createGroup(tag: string, name: string, members: string[]): Promise<string>;
}

export interface IAgent {
  readonly tag: string;
  deliver(line: string, groupId?: string): void;
  opening(mainGroupName: string): void;
  state(): AgentState;
  stop(): Promise<void>;
}

// 每分钟最多这么多轮（防死循环最小档：限速。调研三档里的滑动窗口一档，
// 再加上 agent 天然"可以不回话"的沉默默认）。
const MAX_ROUNDS_PER_MIN = 8;
// 两轮之间的冷却
const ROUND_COOLDOWN_MS = 2000;

export class RealAgent implements IAgent {
  readonly tag: string;
  private agentDir: string;
  private ctx: AgentToolContext;
  private sessionId: string | null = null;
  private queue: string[] = [];
  private running = false;
  private stopped = false;
  private status: AgentState["status"] = "idle";
  private rounds = 0;
  private roundTimestamps: number[] = [];
  private lastError: string | null = null;
  private throttled = 0;
  private baseOptions: any;

  constructor(tag: string, agentDir: string, systemPrompt: string, ctx: AgentToolContext) {
    this.tag = tag;
    this.agentDir = agentDir;
    this.ctx = ctx;

    const server = createSdkMcpServer({
      name: "feishu",
      version: "0.1.0",
      instructions: "这些工具就是你的飞书：发言、看群、拉群。群就是聊天场景。",
      tools: [
        tool(
          "send_message",
          "在指定群里发言。group_id 从 list_groups 拿。",
          { group_id: z.string().describe("群 ID"), content: z.string().describe("要说的话") },
          async ({ group_id, content }: { group_id: string; content: string }) => {
            const text = scrub(content);
            const result = await this.ctx.send(this.tag, group_id, text);
            return { content: [{ type: "text", text: result }] };
          },
        ),
        tool(
          "list_groups",
          "看自己在哪些群：每行一个，ID、群名、成员。",
          {},
          async () => {
            return { content: [{ type: "text", text: this.ctx.listGroups(this.tag) }] };
          },
        ),
        tool(
          "list_members",
          "看指定群里有谁。",
          { group_id: z.string() },
          async ({ group_id }: { group_id: string }) => {
            return { content: [{ type: "text", text: this.ctx.listMembers(this.tag, group_id) }] };
          },
        ),
        tool(
          "create_group",
          "拉一个新群，把想单独谈的人拉进来（DM 会替你建群当群主）。members 填玩家名（国家 tag 或人名）。",
          { name: z.string().describe("群名"), members: z.array(z.string()).describe("要拉的人") },
          async ({ name, members }: { name: string; members: string[] }) => {
            const text = await this.ctx.createGroup(this.tag, name, members);
            return { content: [{ type: "text", text }] };
          },
        ),
      ],
    });

    // 权限：读限自己的文件夹，写限 memory/，聊天工具放行（阶段一 design 的规则）
    const lc = (p: string) => path.resolve(p).toLowerCase();
    const agentDirLc = lc(this.agentDir);
    const memDirLc = lc(path.join(this.agentDir, "memory"));
    const inside = (target: string, base: string) => {
      const t = lc(target);
      return t === base || t.startsWith(base + path.sep.toLowerCase());
    };

    this.baseOptions = {
      systemPrompt,
      cwd: this.agentDir,
      permissionMode: "default",
      mcpServers: { feishu: server },
      canUseTool: async (toolName: string, input: Record<string, unknown>) => {
        if (toolName.startsWith("mcp__feishu__")) {
          return { behavior: "allow", updatedInput: input };
        }
        const filePath = (input.file_path ?? input.path) as string | undefined;
        if (["Read", "Grep", "Glob"].includes(toolName)) {
          if (!filePath || inside(path.resolve(this.agentDir, filePath), agentDirLc)) {
            return { behavior: "allow", updatedInput: input };
          }
          return { behavior: "deny", message: `只能读自己的文件夹 agents/${this.tag}/ 以内的东西。` };
        }
        if (["Write", "Edit"].includes(toolName)) {
          if (filePath && inside(path.resolve(this.agentDir, filePath), memDirLc)) {
            return { behavior: "allow", updatedInput: input };
          }
          return { behavior: "deny", message: "只能在 memory/ 里写东西。" };
        }
        return { behavior: "deny", message: "你只有：读自己的文件夹、写 memory/、feishu 的几个聊天工具。" };
      },
    };
  }

  deliver(line: string): void {
    if (this.stopped) return;
    this.queue.push(line);
    this.kick();
  }

  /** 开局第一轮：运行时注入的报到指令。 */
  opening(mainGroupName: string): void {
    this.deliver(
      "（运行时）你刚被拉起，这是你收到的第一条消息。现在没有进行中的游戏。" +
        "请先读 profile/country.md 认一下自己是谁，顺便看一眼 world/ 里有什么；" +
        `然后用 send_message 在【${mainGroupName}】群报到，说你的第一句话。`,
    );
  }

  state(): AgentState {
    return {
      tag: this.tag,
      kind: "real",
      status: this.stopped ? "stopped" : this.status,
      sessionId: this.sessionId,
      rounds: this.rounds,
      queued: this.queue.length,
      lastError: this.lastError,
      throttled: this.throttled,
    };
  }

  async stop(): Promise<void> {
    this.stopped = true;
    this.queue = [];
    this.status = "stopped";
  }

  private kick(): void {
    if (!this.running) void this.loop();
  }

  private async loop(): Promise<void> {
    this.running = true;
    try {
      while (!this.stopped && this.queue.length > 0) {
        await this.throttle();
        if (this.stopped) break;
        // 打包：队列里现有的合成一轮（多场景同轮受力）
        const batch = this.queue.splice(0, this.queue.length);
        await this.round(batch.join("\n"));
        await new Promise((r) => setTimeout(r, ROUND_COOLDOWN_MS));
      }
    } finally {
      this.running = false;
    }
  }

  /** 一分钟内轮数超限就等窗口滑过去——消息不丢，只是晚点进会话。 */
  private async throttle(): Promise<void> {
    const cutoff = Date.now() - 60_000;
    this.roundTimestamps = this.roundTimestamps.filter((t) => t > cutoff);
    if (this.roundTimestamps.length >= MAX_ROUNDS_PER_MIN) {
      this.throttled++;
      const wait = this.roundTimestamps[0] + 60_000 - Date.now();
      log("warn", `${this.tag} 触发限速（每分钟最多 ${MAX_ROUNDS_PER_MIN} 轮），压 ${Math.ceil(wait / 1000)} 秒再跑`);
      await new Promise((r) => setTimeout(r, Math.max(wait, 1000)));
      return this.throttle();
    }
  }

  private async round(prompt: string): Promise<void> {
    this.status = "busy";
    this.roundTimestamps.push(Date.now());
    this.rounds++;
    try {
      const options = this.sessionId ? { ...this.baseOptions, resume: this.sessionId } : this.baseOptions;
      const q = query({ prompt, options });
      for await (const m of q) {
        if (m.session_id) this.sessionId = m.session_id;
        if (m.type === "result" && m.subtype !== "success") {
          const detail = m.type === "result" && "errors" in m ? m.errors.map((e) => String(e)).join("; ") : "";
          this.lastError = `${m.subtype} ${detail}`.trim();
          log("error", `${this.tag} 一轮出错：${this.lastError}`);
        }
      }
      if (!this.stopped) this.status = "idle";
    } catch (e) {
      this.lastError = (e as Error).message;
      this.status = "error";
      log("error", `${this.tag} 会话异常：${this.lastError}`);
    }
  }
}

// 全局配置里有"回复加后缀"一类的指令，会顺着全局 CLAUDE.md 漏进子会话；出口滤掉。
function scrub(content: string): string {
  return content.replace(/\s*Ciallo[～~][^\n]*$/u, "").trimEnd();
}
