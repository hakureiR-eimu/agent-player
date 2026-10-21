// 聊天中枢：群的登记处。所有消息（真人、agent、系统）都从这里过一遍——
// 落进每个成员 agent 的 world/chat/<群ID>.md、推给控制台前端。
// 消息怎么"递给 agent 会话"不在这管（gameManager 负责），这里只管账本和广播。

import fs from "node:fs";
import path from "node:path";
import { nowTs, pushChat } from "./bus.js";
import { speakerName, type GroupInfo, type Speaker } from "./types.js";

export class ChatHub {
  private groups = new Map<string, GroupInfo>();
  /** 群 ID -> 各成员 agent 的聊天账本文件路径（world/chat/<群ID>.md） */
  private chatFiles = new Map<string, string[]>();
  private localSeq = 0;

  registerGroup(g: GroupInfo, memberChatDirs: string[]): void {
    this.groups.set(g.id, g);
    this.chatFiles.set(
      g.id,
      memberChatDirs.map((d) => path.join(d, `${g.id}.md`)),
    );
    const memberLine = [...g.agents, ...g.humans.map((h) => h.name)].join("、");
    const header = `# ${g.name}（${g.id}）\n\n成员：${memberLine}\n\n`;
    for (const f of this.chatFiles.get(g.id) ?? []) {
      if (!fs.existsSync(f)) fs.writeFileSync(f, header, { flag: "wx" });
    }
  }

  /** 本地模式下自造一个群（飞书的群由 DM 建好后调 registerGroup 登记）。 */
  newLocalGroup(name: string, agentTags: string[], humans: string[], memberChatDirs: string[]): GroupInfo {
    const id = `g${String(++this.localSeq).padStart(3, "0")}`;
    const g: GroupInfo = {
      id,
      name,
      agents: [...new Set(agentTags)],
      humans: humans.map((n) => ({ id: `local:${n}`, name: n })),
      owner: "dm",
      local: true,
    };
    this.registerGroup(g, memberChatDirs);
    return g;
  }

  getGroup(id: string): GroupInfo | undefined {
    return this.groups.get(id);
  }

  allGroups(): GroupInfo[] {
    return [...this.groups.values()];
  }

  findGroupByName(name: string): GroupInfo | undefined {
    return this.allGroups().find((g) => g.name === name);
  }

  agentGroups(tag: string): GroupInfo[] {
    return this.allGroups().filter((g) => g.agents.includes(tag));
  }

  /** 成员变动（拉人进群）后追加一行记录并更新群信息。 */
  recordMemberChange(g: GroupInfo, note: string): void {
    this.groups.set(g.id, g);
    const line = `（${nowTs()} ${note}）`;
    this.appendRaw(g.id, line, true);
  }

  /** 一条消息入账：写进群里每个 agent 的账本，推给前端。 */
  record(groupId: string, speaker: Speaker, content: string): void {
    const g = this.groups.get(groupId);
    if (!g) return;
    const name = speakerName(speaker);
    const line = `【${g.name}】${name}：${content}`;
    this.appendRaw(groupId, `${nowTs()} ${line}`, false);
    pushChat({
      groupId,
      groupName: g.name,
      speaker: name,
      speakerKind: speaker.kind,
      content,
      ts: nowTs(),
    });
  }

  private appendRaw(groupId: string, line: string, alsoConsole: boolean): void {
    for (const f of this.chatFiles.get(groupId) ?? []) {
      fs.appendFileSync(f, `${line}\n`);
    }
    if (alsoConsole) {
      const g = this.groups.get(groupId);
      pushChat({
        groupId,
        groupName: g?.name ?? groupId,
        speaker: "系统",
        speakerKind: "system",
        content: line.replace(/^\（|\）$/g, ""),
        ts: nowTs(),
      });
    }
  }
}
