// 飞书接入：一国一应用（决策 0001），再加一个 DM 应用（非 LLM，建群拉人当群主）。
//
// 收消息只连 DM 一条长连接（WebSocket）：DM 是所有群的成员和群主，真人消息都会推给它；
// agent 之间不靠平台投递 bot 消息（待实测项），agent 发的话由运行时直接扇入其他成员的会话。
// 发消息用各国自己的应用发（它在群里显示的名字就是它的机器人名称——机器人群昵称没有 API，
// 想让群里显示 tag，就把该国应用的机器人名称设成 tag）。

import * as lark from "@larksuiteoapi/node-sdk";
import { log } from "./bus.js";
import type { FeishuConf, HumanMember } from "./types.js";

export interface InboundFeishuMessage {
  messageId: string;
  chatId: string;
  openId: string;
  /** 说话人显示名（从群成员表查到的，查不到时是兜底名） */
  senderName: string;
  text: string;
  isBot: boolean;
}

export class FeishuHub {
  private dmClient: lark.Client;
  private countryClients = new Map<string, lark.Client>();
  /** message_id -> 收到时间，扇入/重推去重 */
  private seen = new Map<string, number>();
  /** open_id -> 显示名（从各群成员表攒出来的） */
  private nameByOpenId = new Map<string, string>();

  constructor(
    private conf: FeishuConf,
    private onMessage: (m: InboundFeishuMessage) => void,
  ) {
    this.dmClient = new lark.Client({
      appId: conf.dm.appId,
      appSecret: conf.dm.appSecret,
      domain: lark.Domain.Feishu,
      loggerLevel: lark.LoggerLevel.warn,
    });
    for (const [tag, app] of Object.entries(conf.countries ?? {})) {
      if (!app?.appId || !app?.appSecret) continue;
      this.countryClients.set(
        tag,
        new lark.Client({
          appId: app.appId,
          appSecret: app.appSecret,
          domain: lark.Domain.Feishu,
          loggerLevel: lark.LoggerLevel.warn,
        }),
      );
    }
  }

  configuredCountries(): string[] {
    return [...this.countryClients.keys()];
  }

  /** 连 DM 的长连接开始收消息。各国应用只发不收，不连。 */
  async start(): Promise<void> {
    const ws = new lark.WSClient({
      appId: this.conf.dm.appId,
      appSecret: this.conf.dm.appSecret,
      domain: lark.Domain.Feishu,
      loggerLevel: lark.LoggerLevel.warn,
    });
    await ws.start({
      eventDispatcher: new lark.EventDispatcher({}).register({
        "im.message.receive_v1": (data: any) => {
          // 3 秒内必须处理完，否则平台会重推：这里只做校验和入队，立即返回。
          this.handleEvent(data);
        },
      }),
    });
    log("info", `飞书长连接已建立（DM 应用 ${this.conf.dm.appId}），开始收群消息`);
  }

  private handleEvent(data: any): void {
    try {
      const msg = data?.message;
      if (!msg?.message_id || !msg?.chat_id) return;
      if (this.seen.has(msg.message_id)) return;
      this.markSeen(msg.message_id);
      if (msg.chat_type !== "group") return; // 单聊不进链路（bot 单聊本来也未支持）
      const openId = data?.sender?.sender_id?.open_id;
      if (!openId) return;
      const isBot = data?.sender?.sender_type === "app";
      let text: string;
      if (msg.message_type === "text") {
        const parsed = JSON.parse(msg.content ?? "{}");
        text = String(parsed.text ?? "").trim();
        // 去掉 @ 提及的标记，留人名
        text = text.replace(/<at user_id="[^"]*"[^>]*>([^<]*)<\/at>/g, "$1").trim();
      } else {
        text = `（发了一条${msg.message_type}消息，这里看不了）`;
      }
      if (!text) return;
      this.onMessage({
        messageId: msg.message_id,
        chatId: msg.chat_id,
        openId,
        senderName: this.nameByOpenId.get(openId) ?? `用户${openId.slice(-6)}`,
        text,
        isBot,
      });
    } catch (e) {
      log("error", `解析飞书消息事件失败：${(e as Error).message}`);
    }
  }

  private markSeen(id: string): void {
    this.seen.set(id, Date.now());
    if (this.seen.size > 2000) {
      const cutoff = Date.now() - 10 * 60 * 1000;
      for (const [k, t] of this.seen) if (t < cutoff) this.seen.delete(k);
    }
  }

  /** 自己发出去的消息也记一笔，收到平台重推/平台真投递了 bot 消息时好去重。 */
  private markSent(messageId: string | undefined): void {
    if (messageId) this.markSeen(messageId);
  }

  /** DM 建群（DM 自动当群主），返回 chat_id。 */
  async createGroup(name: string): Promise<string> {
    const res = await this.dmClient.im.chat.create({
      data: {
        name,
        description: `${name}（本局游戏的公屏，由 DM 创建）`,
        chat_mode: "group",
        chat_type: "private",
      },
    });
    const chatId = res?.data?.chat_id;
    if (!chatId) throw new Error(`DM 建群失败：${JSON.stringify(res?.data ?? res)}`);
    return chatId;
  }

  /** DM 往群里拉国家 bot（app_id）。对同一个群连续拉人要串行（并发报 232019）。 */
  async addCountryBots(chatId: string, tags: string[]): Promise<void> {
    for (const tag of tags) {
      const appId = this.conf.countries?.[tag]?.appId;
      if (!appId) throw new Error(`国家 ${tag} 没有配置飞书应用`);
      const res = await this.dmClient.im.chatMembers.create({
        params: { member_id_type: "app_id" },
        path: { chat_id: chatId },
        data: { id_list: [appId] },
      });
      const failed = (res?.data as any)?.failed_member_list ?? [];
      if (failed.length > 0) {
        throw new Error(`拉 ${tag} 进群失败：${JSON.stringify(failed)}（确认该应用已开启机器人能力并在本租户启用）`);
      }
      await sleep(300);
    }
  }

  /** DM 往群里拉真人（open_id 或 user_id）。 */
  async addHumans(chatId: string, ids: string[]): Promise<HumanMember[]> {
    const idType = ids.every((x) => x.startsWith("ou_")) ? "open_id" : "user_id";
    const res = await this.dmClient.im.chatMembers.create({
      params: { member_id_type: idType },
      path: { chat_id: chatId },
      data: { id_list: ids },
    });
    const failed = (res?.data as any)?.failed_member_list ?? [];
    if (failed.length > 0) {
      throw new Error(`拉真人进群失败：${JSON.stringify(failed)}（确认这些用户在 DM 应用的可用范围内）`);
    }
    await this.refreshMembers(chatId);
    const members = await this.listMembers(chatId);
    return members.filter((m) => ids.includes(m.id));
  }

  /** 拉群成员表（open_id 视角），顺手攒名字映射。 */
  async refreshMembers(chatId: string): Promise<HumanMember[]> {
    const items: { member_id: string; name: string }[] = [];
    let pageToken: string | undefined;
    do {
      const res = await this.dmClient.im.chatMembers.get({
        params: { member_id_type: "open_id", page_size: 100, page_token: pageToken },
        path: { chat_id: chatId },
      });
      const d: any = res?.data ?? {};
      items.push(...(d.items ?? []));
      pageToken = d.has_more ? d.page_token : undefined;
    } while (pageToken);
    for (const it of items) {
      if (it.member_id?.startsWith("ou_")) this.nameByOpenId.set(it.member_id, it.name);
    }
    return items.filter((i) => i.member_id.startsWith("ou_")).map((i) => ({ id: i.member_id, name: i.name }));
  }

  async listMembers(chatId: string): Promise<HumanMember[]> {
    return this.refreshMembers(chatId);
  }

  /** 名字反查 open_id（agent 拉小群时按人名找人）。 */
  openIdByName(name: string): string | undefined {
    for (const [id, n] of this.nameByOpenId) if (n === name) return id;
    return undefined;
  }

  /** 以某国应用的身份在群里发言。 */
  async sendAs(tag: string, chatId: string, text: string): Promise<void> {
    const client = this.countryClients.get(tag);
    if (!client) throw new Error(`国家 ${tag} 没有配置飞书应用，发不了消息`);
    const res = await client.im.message.create({
      params: { receive_id_type: "chat_id" },
      data: {
        receive_id: chatId,
        content: JSON.stringify({ text }),
        msg_type: "text",
      },
    });
    this.markSent(res?.data?.message_id);
  }

  /** DM 群里发系统通知（开局、成员变动这类提示）。 */
  async sendSystem(chatId: string, text: string): Promise<void> {
    const res = await this.dmClient.im.message.create({
      params: { receive_id_type: "chat_id" },
      data: {
        receive_id: chatId,
        content: JSON.stringify({ text }),
        msg_type: "text",
      },
    });
    this.markSent(res?.data?.message_id);
  }

  /** agent 发起的建小群：DM 代建并拉人，DM 当群主。 */
  async createSubGroup(name: string, requesterTag: string, botTags: string[], humanOpenIds: string[]): Promise<string> {
    const chatId = await this.createGroup(name);
    const tags = [...new Set([requesterTag, ...botTags])];
    await this.addCountryBots(chatId, tags);
    if (humanOpenIds.length > 0) {
      await this.dmClient.im.chatMembers.create({
        params: { member_id_type: "open_id" },
        path: { chat_id: chatId },
        data: { id_list: humanOpenIds },
      });
    }
    await this.refreshMembers(chatId);
    return chatId;
  }
}

function sleep(ms: number): Promise<void> {
  return new Promise((r) => setTimeout(r, ms));
}
