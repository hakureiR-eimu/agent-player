// 读配置：config/feishu.json 存在且含 DM 应用时走飞书模式，否则本地模式。

import fs from "node:fs";
import path from "node:path";
import type { FeishuConf } from "./types.js";

export interface LoadedConfig {
  conf: FeishuConf;
  /** 飞书模式 = DM 应用凭证齐了 */
  feishuMode: boolean;
}

export function loadConfig(rootDir: string): LoadedConfig {
  const file = path.join(rootDir, "config", "feishu.json");
  if (!fs.existsSync(file)) {
    return { conf: {}, feishuMode: false };
  }
  let conf: FeishuConf;
  try {
    conf = JSON.parse(fs.readFileSync(file, "utf8")) as FeishuConf;
  } catch (e) {
    throw new Error(`config/feishu.json 不是合法 JSON：${(e as Error).message}`);
  }
  const feishuMode = Boolean(conf.dm?.appId && conf.dm?.appSecret);
  return { conf, feishuMode };
}
