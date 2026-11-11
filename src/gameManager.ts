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
  type CurrentGameRef,
  type FeishuConf,
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

/** 局名/game.json 的形状：继续游戏要恢复的一切（群登记、各 agent 的会话 ID）。 */
interface GameRecord {
  name: string;
  createdAt: string;
  savedAt: string;
  mainGroupId: string;
  groups: GroupInfo[];
  agents: Record<string, { sessionId: string | null }>;
}

export class GameManager {
  private hub = new ChatHub();
  private feishu: FeishuHub | null = null;
  private game: Game | null = null;
  private available: { tag: string; name: string }[] = [];
  /** 存着没跑的局（state.json 指着，可继续）。飞书应用多局复用，agent 状态在局文件夹里不跨局。 */
  private saved: { name: string; savedAt: string | null } | null = null;
  /** 会话用的模型名（config/llm.json 的 model，没配就不传） */
  private model: string | undefined;

  constructor(
    private rootDir: string,
    private conf: FeishuConf,
    model?: string,
  ) {
    this.model = model;
  }

  async init(): Promise<void> {
    this.available = this.loadAvailableCountries();
    this.feishu = new FeishuHub(this.conf, (m) => this.onFeishuMessage(m));
    await this.feishu.start();
    this.loadCurrent();
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
      if (!this.conf.countries?.[tag]) {
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
    // 中途失败就清掉局文件夹，别让残留把重试挡住（飞书侧可能已建出群，那个只能手动删）
    let chatId: string;
    try {
      chatId = await this.feishu!.createGroup(name);
      await this.feishu!.addCountryBots(chatId, tags);
    } catch (e) {
      fs.rmSync(gameDir, { recursive: true, force: true });
      log("warn", `建局失败，局文件夹已清（飞书侧可能建出的群要手动删）：${(e as Error).message}`);
      throw e;
    }
    const humans = await this.feishu!.refreshMembers(chatId);
    const mainGroup: GroupInfo = { id: chatId, name, agents: tags, humans, owner: "dm" };
    this.hub.registerGroup(mainGroup, tags.map((t) => this.chatDir(gameDir, t)));
    log("info", `大群「${name}」已建（${chatId}），${tags.length} 个国家 bot 已进群`);

    this.game = { name, dir: gameDir, createdAt: new Date().toISOString(), mainGroupId: mainGroup.id, agents: new Map() };

    // 3. 群里发一条系统消息（真人侧能看到开局提示）
    const sysLine = `新的一局「${name}」开始了，本局玩家：${tags.join("、")}。真人玩家稍后进场。`;
    await this.feishu!.sendSystem(mainGroup.id, `（系统）${sysLine}`);
    this.hub.record(mainGroup.id, { kind: "system" }, sysLine);

    // 4. 拉起 agent，错开几秒免得挤在一起
    for (const tag of tags) {
      const agent = this.buildAgent(tag);
      this.game.agents.set(tag, agent);
    }
    this.emitState();
    void this.launchSequence(tags, mainGroup.name).then(() => this.persistGame());

    this.saved = null; // 开新局顶掉存档（前端已确认过）
    this.persistGame(); // 先落一版（sessionId 还是空），报到完成后再落一次
    this.writeCurrent(name, "running");
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

  /** resumeSessionId：继续游戏时接着存档里的会话跑。 */
  private buildAgent(tag: string, resumeSessionId?: string | null): IAgent {
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
    return new RealAgent(tag, agentDir, `${system}\n\n---\n\n${country}`, ctx, this.model, resumeSessionId);
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
    try {
      await this.feishu!.sendAs(tag, groupId, content);
    } catch (e) {
      log("error", `${tag} 发消息到【${g.name}】失败：${(e as Error).message}`);
      return `发到【${g.name}】失败了：${(e as Error).message}`;
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
    const openIds: string[] = [];
    for (const n of humanNames) {
      const id = this.feishu!.openIdByName(n);
      if (!id) return `知道有 ${n} 这个人，但查不到 open_id，拉不了。`;
      openIds.push(id);
    }
    const chatId = await this.feishu!.createSubGroup(name, tag, botTags, openIds);
    const humans = humanNames.map((n) => ({ id: this.feishu!.openIdByName(n) ?? "", name: n }));
    g = { id: chatId, name, agents: [...new Set([tag, ...botTags])], humans, owner: "dm" };
    this.hub.registerGroup(g, g.agents.map((t) => this.chatDir(this.game!.dir, t)));
    this.hub.recordMemberChange(g, `${tag} 建立了群「${name}」，成员：${[...g.agents, ...g.humans.map((h) => h.name)].join("、")}`);
    this.persistGame(); // 群登记变了，落盘免得崩了丢
    return `群「${name}」已建立（DM 替你建的，DM 当群主），ID ${g.id}，成员：${[...g.agents, ...g.humans.map((h) => h.name)].join("、")}。可以 send_message 了。`;
  }

  // ---------- 真人进群 ----------

  async addHumans(rawIds: string): Promise<string[]> {
    if (!this.game) throw new Error("还没有局");
    const ids = rawIds.split(/[,，\s]+/).map((s) => s.trim()).filter(Boolean);
    if (ids.length === 0) throw new Error("没填 ID");
    const g = this.hub.getGroup(this.game.mainGroupId);
    if (!g) throw new Error("公屏群不见了");
    const added = await this.feishu!.addHumans(g.id, ids);
    for (const h of added) {
      if (!g.humans.some((x) => x.id === h.id)) g.humans.push(h);
    }
    this.hub.recordMemberChange(g, `DM 把 ${added.map((h) => h.name).join("、")} 拉进了【${g.name}】`);
    this.persistGame(); // 成员变了，落盘免得崩了丢
    return added.map((h) => h.name);
  }

  // ---------- 状态与收尾 ----------

  /** 继续存着的局：恢复群登记和各 agent 会话。 */
  async resumeGame(): Promise<void> {
    if (this.game) throw new Error("已经有一局在跑，先处理它");
    if (!this.saved) throw new Error("没有存着的局");
    const name = this.saved.name;
    const gameDir = path.join(this.rootDir, name);
    const recordFile = path.join(gameDir, "game.json");
    if (!fs.existsSync(recordFile)) {
      throw new Error(`局「${name}」的 game.json 不见了，没法继续（局文件夹还在的话翻档案：${name}/）`);
    }
    const record = JSON.parse(fs.readFileSync(recordFile, "utf8")) as GameRecord;
    for (const g of record.groups) {
      this.hub.registerGroup(g, g.agents.map((t) => this.chatDir(gameDir, t)));
    }
    this.game = { name, dir: gameDir, createdAt: record.createdAt, mainGroupId: record.mainGroupId, agents: new Map() };
    for (const [tag, a] of Object.entries(record.agents)) {
      this.game.agents.set(tag, this.buildAgent(tag, a.sessionId));
    }
    this.saved = null;
    this.writeCurrent(name, "running");
    await this.feishu!.sendSystem(record.mainGroupId, `（系统）「${name}」继续进行，各位接着聊。`);
    void this.refreshAllGroups(); // 群成员可能有进出，后台刷一遍
    this.emitState();
    log("info", `局「${name}」已继续：${this.game.agents.size} 个 agent 回来了`);
  }

  /** 保存并退出：停 agent、状态落盘，控制台回到可继续/可新开。 */
  async saveGame(): Promise<void> {
    if (!this.game) throw new Error("还没有局");
    const name = this.game.name;
    for (const a of this.game.agents.values()) await a.stop();
    const savedAt = new Date().toISOString();
    this.persistGame(savedAt);
    this.game = null;
    this.saved = { name, savedAt };
    this.writeCurrent(name, "saved");
    this.emitState();
    log("info", `局「${name}」已保存退出（想接着玩用「继续」）`);
  }

  /** 结束游戏：局不可再继续，局文件夹和飞书群留档。 */
  async stopGame(): Promise<void> {
    if (!this.game) return;
    const name = this.game.name;
    for (const a of this.game.agents.values()) await a.stop();
    try {
      await this.feishu!.sendSystem(this.game.mainGroupId, `（系统）「${name}」本局结束，感谢各位。`);
    } catch (e) {
      log("warn", `发结束通知失败：${(e as Error).message}`);
    }
    this.game = null;
    this.saved = null;
    this.clearCurrent();
    this.emitState();
    log("info", `局「${name}」结束了（局文件夹保留：${name}/，翻档直接看文件）`);
  }

  // ---------- 持久化：局状态落盘，进程崩了也能续 ----------

  private persistGame(savedAt?: string): void {
    if (!this.game) return;
    const record: GameRecord = {
      name: this.game.name,
      createdAt: this.game.createdAt,
      savedAt: savedAt ?? new Date().toISOString(),
      mainGroupId: this.game.mainGroupId,
      groups: this.hub.allGroups(),
      agents: Object.fromEntries([...this.game.agents].map(([tag, a]) => [tag, { sessionId: a.state().sessionId }])),
    };
    fs.writeFileSync(path.join(this.game.dir, "game.json"), JSON.stringify(record, null, 2));
  }

  private writeCurrent(name: string, status: CurrentGameRef["status"]): void {
    fs.writeFileSync(path.join(this.rootDir, "state.json"), JSON.stringify({ current: { name, status } }, null, 2));
  }

  private clearCurrent(): void {
    const file = path.join(this.rootDir, "state.json");
    if (fs.existsSync(file)) fs.unlinkSync(file);
  }

  /** 启动时读当前局指针；上次在跑时退了进程的，按存档处理。 */
  private loadCurrent(): void {
    const file = path.join(this.rootDir, "state.json");
    if (!fs.existsSync(file)) return;
    try {
      const { current } = JSON.parse(fs.readFileSync(file, "utf8")) as { current?: CurrentGameRef };
      if (!current?.name) return;
      if (current.status === "running") {
        log("warn", `上次「${current.name}」在跑的时候进程退了，按存档处理（可以继续）`);
      }
      this.saved = { name: current.name, savedAt: this.readSavedAt(current.name) };
    } catch (e) {
      log("warn", `state.json 读不了：${(e as Error).message}`);
    }
  }

  private readSavedAt(name: string): string | null {
    try {
      const r = JSON.parse(fs.readFileSync(path.join(this.rootDir, name, "game.json"), "utf8")) as GameRecord;
      return r.savedAt ?? null;
    } catch {
      return null;
    }
  }

  /** 把所有群的真人成员刷新一遍（继续游戏后用，单个群失败不挡别的）。 */
  private async refreshAllGroups(): Promise<void> {
    for (const g of this.hub.allGroups()) {
      try {
        g.humans = await this.feishu!.refreshMembers(g.id);
      } catch (e) {
        log("warn", `刷新【${g.name}】成员失败（群可能被解散）：${(e as Error).message}`);
      }
    }
    this.persistGame();
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
      countryConfigured,
      availableCountries: this.available,
      saved: this.game ? null : this.saved,
      gameDir: this.game?.dir ?? null,
      game: this.game
        ? {
            name: this.game.name,
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
