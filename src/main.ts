// 入口：起运行时（阶段一 agent + 阶段二飞书），打开控制台前端。

import path from "node:path";
import { fileURLToPath } from "node:url";
import { exec } from "node:child_process";
import { log } from "./bus.js";
import { loadConfig } from "./config.js";
import { GameManager } from "./gameManager.js";
import { attachSse, startServer } from "./server.js";

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const port = Number(process.env.GAME_AGENT_PORT ?? 5678);

async function main(): Promise<void> {
  const { conf, feishuMode } = loadConfig(rootDir);
  const manager = new GameManager(rootDir, conf, feishuMode);
  await manager.init();

  const publicDir = path.join(rootDir, "public");
  const server = startServer(manager, port, publicDir);
  attachSse(server, manager, publicDir);

  const url = `http://localhost:${port}`;
  log("info", `控制台已就绪：${url}（局文件夹建在仓库根，按局名一个文件夹）`);
  if (!process.env.GAME_AGENT_NO_BROWSER) openBrowser(url);

  const shutdown = () => {
    log("info", "收到退出信号，收工");
    server.close();
    process.exit(0);
  };
  process.on("SIGINT", shutdown);
  process.on("SIGTERM", shutdown);
}

function openBrowser(url: string): void {
  const cmd =
    process.platform === "win32" ? `start "" "${url}"` : process.platform === "darwin" ? `open "${url}"` : `xdg-open "${url}"`;
  exec(cmd, (err) => {
    if (err) log("warn", `浏览器没打开（${err.message}），手动访问 ${url}`);
  });
}

main().catch((e) => {
  log("error", `启动失败：${(e as Error).message}`);
  process.exit(1);
});
