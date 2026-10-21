// 全项目共用的类型。

export interface FeishuAppConf {
  appId: string;
  appSecret: string;
}

/** config/feishu.json 的形状。没有这个文件就是本地模式。 */
export interface FeishuConf {
  dm?: FeishuAppConf;
  countries?: Record<string, FeishuAppConf>;
}

/** 真人玩家。id 是飞书 open_id（本地模式下就是控制台里填的名字）。 */
export interface HumanMember {
  id: string;
  name: string;
}

/** 群。id 是飞书 chat_id（本地模式下是 g001 这样的自造 ID）。 */
export interface GroupInfo {
  id: string;
  name: string;
  agents: string[];
  humans: HumanMember[];
  owner: "dm" | string;
  local: boolean;
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

export type AgentKind = "real" | "fake";
export type AgentStatus = "starting" | "idle" | "busy" | "error" | "stopped";

export interface AgentState {
  tag: string;
  kind: AgentKind;
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
  mode: "feishu" | "local";
  createdAt: string;
  mainGroupId: string | null;
  mainGroupName: string | null;
  agents: AgentState[];
  groups: GroupInfo[];
}

/** 前端可见的全量状态。 */
export interface AppState {
  mode: "feishu" | "local";
  /** 飞书配置到位情况：DM 配了没、各国配了没 */
  dmConfigured: boolean;
  countryConfigured: Record<string, boolean>;
  availableCountries: { tag: string; name: string }[];
  game: GameSummary | null;
  gameDir: string | null;
}
