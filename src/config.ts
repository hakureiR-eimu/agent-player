// 读配置：两份文件都在 config/ 下，都不进 git。
// - feishu.json：飞书应用凭证，必配——DM 应用缺了就报错退出，没有本地兜底
// - llm.json：大模型认证（GLM 的 Anthropic 兼容端点），配了就设进环境变量给会话用

import fs from "node:fs";
import path from "node:path";
import type { FeishuConf } from "./types.js";

export interface LoadedConfig {
  feishu: FeishuConf;
  llm: LlmConf | null;
}

export interface LlmConf {
  baseUrl?: string;
  apiKey?: string;
  model?: string;
}

export function loadConfig(rootDir: string): LoadedConfig {
  const feishu = loadJson<FeishuConf>(rootDir, "feishu.json");
  if (!feishu?.dm?.appId || !feishu?.dm?.appSecret) {
    throw new Error(
      "飞书没配好：config/feishu.json 不存在，或 dm 的 appId/appSecret 没填。把 config/feishu.example.json 拷成 config/feishu.json，填 DM 应用和要上的国家应用的凭证（建应用见 README「接飞书」）",
    );
  }
  const llm = loadJson<LlmConf>(rootDir, "llm.json");
  return { feishu, llm };
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
