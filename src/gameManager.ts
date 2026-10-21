// 局的编排：建局文件夹、建大群、拉 agent、消息扇入扇出。
// 阶段一（agent 会话）和阶段二（多 agent 上飞书）在这里组装成一个运行时。

import fs from "node:fs";
import path from "node:path";
import { emit, log } from "./bus.js";
import { ChatHub } from "./chatHub.js";
import { FeishuHub, type InboundFeishuMessage } from "./feishuHub.js";
import { RealAgent, type AgentToolContext, type IAgent } from "./agent.js";
import {
  speakerName,
  type AppState,
  type GroupInfo,
  type Speaker,
} from "./types.js";

const RESERVED_DIR_NAMES = new Set([
  "agents", "config", "docs", "src", "public", "资料", "node_modules", ".git", "backup",
]);

interface Game {
  name: string;
  dir: string;
  createdAt: string;
  mainGroupId: string;
  agents: Map<string, IAgent>;
}

export class GameManager {
  readonly mode: "feishu" | "local";
  private hub = new ChatHub();
  private feishu: FeishuHub | null = null;
  private game: Game | null = null;
  private available: { tag: string; name: string }[] = [];
  /** 会话用的模型名（config/llm.json 的 model，没配就不传） */
  private model: string | undefined;

  constructor(
    private rootDir: string,
    private conf: { dm?: { appId: string; appSecret: string }; countries?: Record<string, { appId: string; appSecret: string }> },
    feishuMode: boolean,
    model?: string,
  ) {
    this.mode = feishuMode ? "feishu" : "local";
    this.model = model;
  }

  async init(): Promise<void> {
    this.available = this.loadAvailableCountries();
    if (this.mode === "feishu") {
      this.feishu = new FeishuHub(this.conf, (m) => this.onFeishuMessage(m));
      await this.feishu.start();
    } else {
      log("info", "没配飞书（config/feishu.json 缺失或没有 DM 应用），本地模式：群只在控制台里");
    }
  }

  private loadAvailableCountries(): { tag: string; name: string }[] {
    const dir = path.join(this.rootDir, "资料", "主要国家");
    const out: { tag: string; name: string }[] = [];
    for (const tag of fs.readdirSync(dir)) {
      const intro = path.join(dir, tag, "介绍.md");
      if (!fs.existsSync(intro)) continue;
      const first = fs.readFileSync(intro, "utf8").split("\n").find((l) => l.startsWith("# "));
      out.push({ tag, name: first?.replace(/^#\s*/, "").trim() ?? tag });
    }
    return out.sort((a, b) => a.tag.localeCompare(b.tag));
  }

  // ---------- 建局 ----------

  async createGame(name: string, tags: string[]): Promise<void> {
    if (this.game) throw new Error("已经有一局在跑，先结束这一局再开新的");
    name = name.trim();
    if (!name || name.length > 30) throw new Error("局名要在 1–30 个字之间");
    if (/[\\/:*?"<>|]/.test(name)) throw new Error('局名里不能有 \\ / : * ? " < > | 这些字符');
    if (RESERVED_DIR_NAMES.has(name.toLowerCase())) throw new Error(`${name} 是仓库保留目录名，换一个局名`);
    const gameDir = path.join(this.rootDir, name);
    if (fs.existsSync(gameDir)) throw new Error(`局文件夹已存在：${name}，换个局名或删掉旧文件夹`);

    if (tags.length === 0) throw new Error("至少勾一个国家");
    for (const tag of tags) {
      if (!this.available.some((c) => c.tag === tag)) throw new Error(`没有国家 ${tag} 的资料（资料/主要国家/）`);
      if (this.mode === "feishu" && !this.conf.countries?.[tag]) {
        throw new Error(`国家 ${tag} 没配飞书应用（config/feishu.json 的 countries），先配上再拉它`);
      }
    }

    // 1. 建局文件夹：每个国家一个 agents/<tag>/，profile 从模板+资料装好
    for (const tag of tags) {
      const agentDir = path.join(gameDir, "agents", tag);
      fs.cpSync(path.join(this.rootDir, "agents", "模板"), agentDir, { recursive: true });
      const intro = fs.readFileSync(path.join(this.rootDir, "资料", "主要国家", tag, "介绍.md"), "utf8");
      fs.writeFileSync(path.join(agentDir, "profile", "country.md"), intro);
      for (const d of ["world/chat", "world/state", "memory"]) {
        fs.mkdirSync(path.join(agentDir, d), { recursive: true });
      }
    }
    log("info", `局文件夹已建：${name}/agents/（${tags.join("、")}）`);

    // 2. 建公屏大群，DM 当群主；拉各国 bot 进群
    let mainGroup: GroupInfo;
    if (this.mode === "feishu") {
      const chatId = await this.feishu!.createGroup(name);
      await this.feishu!.addCountryBots(chatId, tags);
      const humans = await this.feishu!.refreshMembers(chatId);
      mainGroup = { id: chatId, name, agents: tags, humans, owner: "dm", local: false };
      this.hub.registerGroup(mainGroup, tags.map((t) => this.chatDir(gameDir, t)));
      log("info", `大群「${name}」已建（${chatId}），${tags.length} 个国家 bot 已进群`);
    } else {
      mainGroup = this.hub.newLocalGroup("公屏", tags, [], tags.map((t) => this.chatDir(gameDir, t)));
      log("info", `本地模式：公屏群（${mainGroup.id}）已建，${tags.length} 个国家入座`);
    }

    this.game = { name, dir: gameDir, createdAt: new Date().toISOString(), mainGroupId: mainGroup.id, agents: new Map() };

    // 3. 群里发一条系统消息（真人侧能看到开局提示）
    const sysLine = `新的一局「${name}」开始了，本局玩家：${tags.join("、")}。真人玩家稍后进场。`;
    if (this.mode === "feishu") {
      await this.feishu!.sendSystem(mainGroup.id, `（系统）${sysLine}`);
    }
    this.hub.record(mainGroup.id, { kind: "system" }, sysLine);

    // 4. 拉起 agent，错开几秒免得挤在一起
    for (const tag of tags) {
      const agent = this.buildAgent(tag, tags);
      this.game.agents.set(tag, agent);
    }
    this.emitState();
    void this.launchSequence(tags, mainGroup.name);

    log("info", `局「${name}」开起来了：${tags.length} 个 agent 正在报到`);
  }

  private launchSequence(tags: string[], mainGroupName: string): Promise<void> {
    return (async () => {
      for (const tag of tags) {
        this.game?.agents.get(tag)?.opening(mainGroupName);
        await new Promise((r) => setTimeout(r, 3000));
      }
    })();
  }

  private buildAgent(tag: string, allTags: string[]): IAgent {
    const gameDir = this.game!.dir;
    const agentDir = path.join(gameDir, "agents", tag);
    const ctx: AgentToolContext = {
      send: (t, g, c) => this.agentSend(t, g, c),
      listGroups: (t) => this.listGroupsFor(t),
      listMembers: (t, g) => this.listMembersFor(t, g),
      createGroup: (t, n, m) => this.agentCreateGroup(t, n, m),
    };
    const system = fs.readFileSync(path.join(agentDir, "profile", "system.md"), "utf8");
    const country = fs.readFileSync(path.join(agentDir, "profile", "country.md"), "utf8");
    return new RealAgent(tag, agentDir, `${system}\n\n---\n\n${country}`, ctx, this.model);
  }

  private chatDir(gameDir: string, tag: string): string {
    return path.join(gameDir, "agents", tag, "world", "chat");
  }

  // ---------- 消息出入 ----------

  /** 所有消息的总入口：落账 + 推前端 + 扇入给群里的其他 agent。 */
  private inbound(groupId: string, speaker: Speaker, content: string): void {
    const g = this.hub.getGroup(groupId);
    if (!g) return;
    this.hub.record(groupId, speaker, content);
    const line = `【${g.name}】${speakerName(speaker)}：${content}`;
    for (const tag of g.agents) {
      if (speaker.kind === "agent" && speaker.tag === tag) continue;
      this.game?.agents.get(tag)?.deliver(line, groupId);
    }
  }

  /** agent 的 send_message 工具落点：以该国应用发出去，成功后扇入群内其他成员。 */
  private async agentSend(tag: string, groupId: string, content: string): Promise<string> {
    const g = this.hub.getGroup(groupId);
    if (!g) return `没有这个群：${groupId}。先用 list_groups 看 ID。`;
    if (!g.agents.includes(tag)) return `你不在群【${g.name}】里，发不了。`;
    if (this.mode === "feishu") {
      try {
        await this.feishu!.sendAs(tag, groupId, content);
      } catch (e) {
        log("error", `${tag} 发消息到【${g.name}】失败：${(e as Error).message}`);
        return `发到【${g.name}】失败了：${(e as Error).message}`;
      }
    }
    this.inbound(groupId, { kind: "agent", tag }, content);
    const n = g.agents.length + g.humans.length;
    return `已发到【${g.name}】（${n} 个成员在场）`;
  }

  /** 飞书长连接收到的消息（DM 视角，所有群都能收）。 */
  private onFeishuMessage(m: InboundFeishuMessage): void {
    const g = this.hub.getGroup(m.chatId);
    if (!g) {
      log("info", `收到非本局群的消息（${m.chatId}），忽略`);
      return;
    }
    // 自己国家 bot 发的话已经由扇入路径递过了，这里的 bot 消息只可能是平台重推
    // 或外来 bot，前者已被 message_id 去重，后者按名字再兜一道
    if (m.isBot && g.agents.some((t) => m.senderName === t)) return;
    if (!g.humans.some((h) => h.id === m.openId)) {
      g.humans.push({ id: m.openId, name: m.senderName });
      if (m.senderName.startsWith("用户")) void this.feishu!.refreshMembers(m.chatId);
    }
    this.inbound(m.chatId, { kind: "human", name: m.senderName }, m.text);
  }

  /** 本地模式下控制台里的真人发言。 */
  say(humanName: string, content: string): void {
    if (!this.game) throw new Error("还没有局");
    if (this.mode !== "local") throw new Error("飞书模式下请直接在飞书群里说话");
    const g = this.hub.getGroup(this.game.mainGroupId);
    if (!g) throw new Error("公屏群不见了");
    if (!g.humans.some((h) => h.name === humanName)) {
      g.humans.push({ id: `local:${humanName}`, name: humanName });
      this.hub.recordMemberChange(g, `${humanName} 加入了【${g.name}】`);
    }
    this.inbound(g.id, { kind: "human", name: humanName }, content);
  }

  // ---------- agent 的群工具 ----------

  private listGroupsFor(tag: string): string {
    const groups = this.hub.agentGroups(tag);
    if (groups.length === 0) return "（还不在任何群里）";
    return groups
      .map((g) => `${g.id} ${g.name}：${[...g.agents, ...g.humans.map((h) => h.name)].join("、")}`)
      .join("\n");
  }

  private listMembersFor(tag: string, groupId: string): string {
    const g = this.hub.getGroup(groupId);
    if (!g) return `没有这个群：${groupId}`;
    return `【${g.name}】成员：${[...g.agents, ...g.humans.map((h) => h.name)].join("、")}${g.owner === "dm" ? "（DM 当群主）" : ""}`;
  }

  /** agent 的 create_group 工具落点：DM 代建小群（DM 当群主），把人拉进去。 */
  private async agentCreateGroup(tag: string, name: string, members: string[]): Promise<string> {
    if (!this.game) return "还没有局";
    const botTags: string[] = [];
    const humanNames: string[] = [];
    for (const m of members) {
      if (this.game.agents.has(m)) botTags.push(m);
      else {
        const known = this.hub.allGroups().flatMap((g) => g.humans).some((h) => h.name === m);
        if (known) humanNames.push(m);
        else return `没这个人：${m}。members 填国家 tag 或群里真人的名字，用 list_members 先看谁在。`;
      }
    }
    let g: GroupInfo;
    if (this.mode === "feishu") {
      const openIds: string[] = [];
      for (const n of humanNames) {
        const id = this.feishu!.openIdByName(n);
        if (!id) return `知道有 ${n} 这个人，但查不到 open_id，拉不了。`;
        openIds.push(id);
      }
      const chatId = await this.feishu!.createSubGroup(name, tag, botTags, openIds);
      const humans = humanNames.map((n) => ({ id: this.feishu!.openIdByName(n) ?? "", name: n }));
      g = { id: chatId, name, agents: [...new Set([tag, ...botTags])], humans, owner: "dm", local: false };
      this.hub.registerGroup(g, g.agents.map((t) => this.chatDir(this.game!.dir, t)));
    } else {
      g = this.hub.newLocalGroup(name, [tag, ...botTags], humanNames, [...new Set([tag, ...botTags])].map((t) => this.chatDir(this.game!.dir, t)));
    }
    this.hub.recordMemberChange(g, `${tag} 建立了群「${name}」，成员：${[...g.agents, ...g.humans.map((h) => h.name)].join("、")}`);
    return `群「${name}」已建立（DM 替你建的，DM 当群主），ID ${g.id}，成员：${[...g.agents, ...g.humans.map((h) => h.name)].join("、")}。可以 send_message 了。`;
  }

  // ---------- 真人进群 ----------

  async addHumans(rawIds: string): Promise<string[]> {
    if (!this.game) throw new Error("还没有局");
    const ids = rawIds.split(/[,，\s]+/).map((s) => s.trim()).filter(Boolean);
    if (ids.length === 0) throw new Error("没填 ID");
    const g = this.hub.getGroup(this.game.mainGroupId);
    if (!g) throw new Error("公屏群不见了");
    if (this.mode === "feishu") {
      const added = await this.feishu!.addHumans(g.id, ids);
      for (const h of added) {
        if (!g.humans.some((x) => x.id === h.id)) g.humans.push(h);
      }
      this.hub.recordMemberChange(g, `DM 把 ${added.map((h) => h.name).join("、")} 拉进了【${g.name}】`);
      return added.map((h) => h.name);
    }
    for (const n of ids) {
      if (!g.humans.some((h) => h.name === n)) g.humans.push({ id: `local:${n}`, name: n });
    }
    this.hub.recordMemberChange(g, `${ids.join("、")} 进了【${g.name}】`);
    return ids;
  }

  // ---------- 状态与收尾 ----------

  async stopGame(): Promise<void> {
    if (!this.game) return;
    for (const a of this.game.agents.values()) await a.stop();
    log("info", `局「${this.game.name}」的 agent 都停了（局文件夹保留：${this.game.name}/）`);
    this.emitState();
  }

  private emitState(): void {
    emit({ type: "state" });
  }

  state(): AppState {
    const countryConfigured: Record<string, boolean> = {};
    for (const c of this.available) {
      countryConfigured[c.tag] = Boolean(this.conf.countries?.[c.tag]);
    }
    return {
      mode: this.mode,
      dmConfigured: Boolean(this.conf.dm),
      countryConfigured,
      availableCountries: this.available,
      gameDir: this.game?.dir ?? null,
      game: this.game
        ? {
            name: this.game.name,
            mode: this.mode,
            createdAt: this.game.createdAt,
            mainGroupId: this.game.mainGroupId,
            mainGroupName: this.hub.getGroup(this.game.mainGroupId)?.name ?? null,
            agents: [...this.game.agents.values()].map((a) => a.state()),
            groups: this.hub.allGroups(),
          }
        : null,
    };
  }
}
