// 全项目共用的类型。

export interface FeishuAppConf {
  appId: string;
  appSecret: string;
}

/** config/feishu.json 的形状。dm 必配（缺了启动报错），countries 配多少国家上多少。 */
export interface FeishuConf {
  dm: FeishuAppConf;
  countries?: Record<string, FeishuAppConf>;
}

/** 真人玩家。id 是飞书 open_id。 */
export interface HumanMember {
  id: string;
  name: string;
}

/** 群。id 是飞书 chat_id。 */
export interface GroupInfo {
  id: string;
  name: string;
  agents: string[];
  humans: HumanMember[];
  owner: "dm" | string;
}

/** 谁在说话。agent 用国家 tag，真人在飞书侧用群成员表里的名字。 */
export type Speaker =
  | { kind: "agent"; tag: string }
  | { kind: "human"; name: string }
  | { kind: "system" };

export function speakerName(s: Speaker): string {
  if (s.kind === "agent") return s.tag;
  if (s.kind === "human") return s.name;
  return "系统";
}

export interface ChatMessage {
  groupId: string;
  groupName: string;
  speaker: string;
  speakerKind: Speaker["kind"];
  content: string;
  ts: string;
}

export type AgentStatus = "starting" | "idle" | "busy" | "error" | "stopped";

export interface AgentState {
  tag: string;
  status: AgentStatus;
  sessionId: string | null;
  rounds: number;
  queued: number;
  lastError: string | null;
  /** 触发限速的次数（防死循环最小档在工作时会累计） */
  throttled: number;
}

export interface GameSummary {
  name: string;
  createdAt: string;
  mainGroupId: string | null;
  mainGroupName: string | null;
  agents: AgentState[];
  groups: GroupInfo[];
}

/** 根 state.json 的形状：当前局指针。同时只有一局，飞书应用多局复用。 */
export interface CurrentGameRef {
  name: string;
  status: "running" | "saved";
}

/** 前端可见的全量状态。 */
export interface AppState {
  /** 飞书配置到位情况：各国配了没（DM 必配，能跑起来就是配了） */
  countryConfigured: Record<string, boolean>;
  availableCountries: { tag: string; name: string }[];
  /** 存着没跑的局（可继续）。运行中有局时为 null。 */
  saved: { name: string; savedAt: string | null } | null;
  game: GameSummary | null;
  gameDir: string | null;
}
