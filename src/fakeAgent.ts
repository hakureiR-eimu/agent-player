// 假 agent：固定回复的小脚本，不调大模型。阶段二用它打薄链路——
// 控制台/飞书 → 运行时 → agent → 群，整条路不花一分钱 token 就能验。
// 只回真人和系统的话，agent 之间不互相接茬，避免假 agent 之间假聊起来没完。

import { log } from "./bus.js";
import type { AgentState } from "./types.js";
import type { AgentToolContext, IAgent } from "./agent.js";

const REPORTS = [
  "到。人在群里了，开打之前先聊聊。",
  "报到。这局的桌子我坐下了。",
  "来了。诸位，先认识一下？",
  "在场。有什么想谈的尽管说。",
];

export class FakeAgent implements IAgent {
  readonly tag: string;
  private ctx: AgentToolContext;
  /** 本局所有 agent 的 tag：说话人是 agent 一律不接茬（假 agent 只回真人） */
  private agentTags: Set<string>;
  private rounds = 0;
  private lastError: string | null = null;
  private stopped = false;
  private status: AgentState["status"] = "idle";

  constructor(tag: string, agentTags: string[], ctx: AgentToolContext) {
    this.tag = tag;
    this.agentTags = new Set(agentTags);
    this.ctx = ctx;
  }

  opening(mainGroupName: string): void {
    void (async () => {
      await sleep(800 + Math.random() * 1200);
      const id = this.findGroup(mainGroupName);
      if (!id) {
        log("warn", `假 ${this.tag} 找不到群【${mainGroupName}】，报到失败`);
        return;
      }
      this.status = "busy";
      try {
        await this.ctx.send(this.tag, id, REPORTS[Math.floor(Math.random() * REPORTS.length)]);
      } catch (e) {
        this.lastError = (e as Error).message;
        log("error", `假 ${this.tag} 报到失败：${this.lastError}`);
      }
      this.status = "idle";
    })();
  }

  deliver(line: string, groupId?: string): void {
    if (this.stopped || !groupId) return;
    const speaker = line.match(/^【.+?】(.+?)：/)?.[1] ?? "";
    if (this.agentTags.has(speaker)) return; // agent 的话不接（包括自己）
    if (Math.random() < 0.4) return; // 四成概率不接茬，像真人
    void (async () => {
      await sleep(1000 + Math.random() * 1500);
      if (this.stopped) return;
      this.status = "busy";
      this.rounds++;
      const echo = line.replace(/^【.*?】.*?：/, "").slice(0, 30);
      try {
        await this.ctx.send(this.tag, groupId, `（假${this.tag}）收到：「${echo}」——链路通了。`);
      } catch (e) {
        this.lastError = (e as Error).message;
        log("error", `假 ${this.tag} 回话失败：${this.lastError}`);
      }
      this.status = "idle";
    })();
  }

  private findGroup(name: string): string | null {
    for (const row of this.ctx.listGroups(this.tag).split("\n")) {
      if (row.includes(name)) return row.match(/^(\S+)/)?.[1] ?? null;
    }
    return null;
  }

  state(): AgentState {
    return {
      tag: this.tag,
      kind: "fake",
      status: this.stopped ? "stopped" : this.status,
      sessionId: null,
      rounds: this.rounds,
      queued: 0,
      lastError: this.lastError,
      throttled: 0,
    };
  }

  async stop(): Promise<void> {
    this.stopped = true;
    this.status = "stopped";
  }
}

function sleep(ms: number): Promise<void> {
  return new Promise((r) => setTimeout(r, ms));
}
