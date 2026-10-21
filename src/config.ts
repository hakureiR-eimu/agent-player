// 读配置：两份文件都在 config/ 下，都不进 git。
// - feishu.json：飞书应用凭证，配了且含 DM 应用就走飞书模式，否则本地模式
// - llm.json：大模型认证（GLM 的 Anthropic 兼容端点），配了就设进环境变量给会话用

import fs from "node:fs";
import path from "node:path";
import type { FeishuConf } from "./types.js";

export interface LoadedConfig {
  feishu: FeishuConf;
  /** 飞书模式 = DM 应用凭证齐了 */
  feishuMode: boolean;
  llm: LlmConf | null;
}

export interface LlmConf {
  baseUrl?: string;
  apiKey?: string;
  model?: string;
}

export function loadConfig(rootDir: string): LoadedConfig {
  const feishu = loadJson<FeishuConf>(rootDir, "feishu.json");
  const llm = loadJson<LlmConf>(rootDir, "llm.json");
  const feishuMode = Boolean(feishu?.dm?.appId && feishu?.dm?.appSecret);
  return { feishu: feishu ?? {}, feishuMode, llm };
}

function loadJson<T>(rootDir: string, file: string): T | null {
  const full = path.join(rootDir, "config", file);
  if (!fs.existsSync(full)) return null;
  try {
    return JSON.parse(fs.readFileSync(full, "utf8")) as T;
  } catch (e) {
    throw new Error(`config/${file} 不是合法 JSON：${(e as Error).message}`);
  }
}
