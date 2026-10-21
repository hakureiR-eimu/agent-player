// 事件总线：把聊天、日志、状态变化推给控制台前端（SSE），同时打到终端。

import type { ChatMessage } from "./types.js";

export type SseEvent =
  | { type: "chat"; chat: ChatMessage }
  | { type: "log"; line: string; level: LogLevel; ts: string }
  | { type: "state" };

export type LogLevel = "info" | "warn" | "error";

type Listener = (e: SseEvent) => void;

const listeners = new Set<Listener>();
const logBuffer: { line: string; level: LogLevel; ts: string }[] = [];
const chatBuffer: ChatMessage[] = [];
const MAX_BUFFER = 200;

export function subscribe(fn: Listener): () => void {
  listeners.add(fn);
  return () => listeners.delete(fn);
}

export function emit(e: SseEvent): void {
  for (const fn of listeners) {
    try {
      fn(e);
    } catch {
      // 单个 SSE 连接出错不影响别人
    }
  }
}

export function nowTs(): string {
  const d = new Date();
  const p = (n: number) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())} ${p(d.getHours())}:${p(d.getMinutes())}:${p(d.getSeconds())}`;
}

export function log(level: LogLevel, line: string): void {
  const entry = { line, level, ts: nowTs() };
  logBuffer.push(entry);
  if (logBuffer.length > MAX_BUFFER) logBuffer.shift();
  const tag = level === "error" ? "[错误]" : level === "warn" ? "[注意]" : "[运行时]";
  console.log(`${tag} ${line}`);
  emit({ type: "log", ...entry });
}

export function pushChat(msg: ChatMessage): void {
  chatBuffer.push(msg);
  if (chatBuffer.length > MAX_BUFFER) chatBuffer.shift();
  emit({ type: "chat", chat: msg });
}

export function recentLogs() {
  return logBuffer;
}

export function recentChats() {
  return chatBuffer;
}
