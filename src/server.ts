// 控制台前端的服务：静态文件 + JSON 接口 + SSE 实时推送。
// 原生 http，不引 web 框架——路由就这几个。

import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { log, recentChats, recentLogs, subscribe } from "./bus.js";
import type { GameManager } from "./gameManager.js";

const MIME: Record<string, string> = {
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml",
};

export function startServer(manager: GameManager, port: number, publicDir: string): http.Server {
  const server = http.createServer(async (req, res) => {
    const url = new URL(req.url ?? "/", `http://localhost:${port}`);
    try {
      if (url.pathname.startsWith("/api/")) {
        await handleApi(manager, req, res, url);
      } else {
        serveStatic(publicDir, url, res);
      }
    } catch (e) {
      const msg = (e as Error).message ?? String(e);
      log("error", `接口 ${url.pathname} 出错：${msg}`);
      json(res, 500, { error: msg });
    }
  });

  server.on("error", (e) => {
    log("error", `控制台起不来（端口 ${port}）：${(e as Error).message}。用 GAME_AGENT_PORT=别的端口 再试`);
    process.exit(1);
  });
  server.listen(port);
  return server;
}

async function handleApi(manager: GameManager, req: http.IncomingMessage, res: http.ServerResponse, url: URL): Promise<void> {
  const send = (code: number, body: unknown) => json(res, code, body);
  const body = await readBody(req);

  switch (`${req.method} ${url.pathname}`) {
    case "GET /api/state":
      send(200, { ...manager.state(), chats: recentChats(), logs: recentLogs() });
      return;
    case "POST /api/game": {
      const { name, tags } = body as { name?: string; tags?: string[] };
      if (!name || typeof name !== "string") return send(400, { error: "局名没填" });
      if (!Array.isArray(tags)) return send(400, { error: "国家没勾" });
      await manager.createGame(name, tags);
      send(200, { ok: true });
      return;
    }
    case "POST /api/game/humans": {
      const { ids } = body as { ids?: string };
      if (!ids) return send(400, { error: "ID 没填" });
      const added = await manager.addHumans(ids);
      send(200, { ok: true, added });
      return;
    }
    case "POST /api/game/stop": {
      await manager.stopGame();
      send(200, { ok: true });
      return;
    }
    case "POST /api/say": {
      const { name, content } = body as { name?: string; content?: string };
      if (!name || !content) return send(400, { error: "名字和内容都要填" });
      manager.say(name, content);
      send(200, { ok: true });
      return;
    }
    default:
      send(404, { error: "没有这个接口" });
  }
}

function readBody(req: http.IncomingMessage): Promise<any> {
  if (req.method !== "POST") return Promise.resolve({});
  return new Promise((resolve, reject) => {
    let data = "";
    req.on("data", (c) => (data += c));
    req.on("end", () => {
      try {
        resolve(data ? JSON.parse(data) : {});
      } catch {
        reject(new Error("请求体不是合法 JSON"));
      }
    });
    req.on("error", reject);
  });
}

function json(res: http.ServerResponse, code: number, body: unknown): void {
  res.writeHead(code, { "Content-Type": "application/json; charset=utf-8" });
  res.end(JSON.stringify(body));
}

function serveStatic(publicDir: string, url: URL, res: http.ServerResponse): void {
  let file = url.pathname === "/" ? "index.html" : url.pathname.slice(1);
  file = path.normalize(file).replace(/^(\.\.[/\\])+/, ""); // 别想跑出 public/
  const full = path.join(publicDir, file);
  if (!full.startsWith(publicDir) || !fs.existsSync(full) || !fs.statSync(full).isFile()) {
    res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
    res.end("没有这个页面");
    return;
  }
  res.writeHead(200, { "Content-Type": MIME[path.extname(full)] ?? "application/octet-stream" });
  fs.createReadStream(full).pipe(res);
}

/** SSE：聊天、日志、状态变化实时推给页面；另加每 3 秒一次全量状态（agent 队列之类的小变化）。 */
export function attachSse(server: http.Server, manager: GameManager, publicDir: string): void {
  const clients = new Set<http.ServerResponse>();
  const pushState = () => {
    const s = manager.state();
    const payload = `event: state\ndata: ${JSON.stringify({ ...s, chats: recentChats(), logs: recentLogs() })}\n\n`;
    for (const res of clients) res.write(payload);
  };
  const timer = setInterval(pushState, 3000);

  server.on("request", (req, res) => {
    const url = new URL(req.url ?? "/", "http://localhost");
    if (url.pathname !== "/api/events" || req.headers.accept !== "text/event-stream") return;
    res.writeHead(200, {
      "Content-Type": "text/event-stream; charset=utf-8",
      "Cache-Control": "no-cache",
      Connection: "keep-alive",
    });
    res.write(`retry: 3000\n\n`);
    clients.add(res);
    const unsub = subscribe((e) => {
      if (e.type === "state") pushState();
      else res.write(`data: ${JSON.stringify(e)}\n\n`);
    });
    const ping = setInterval(() => res.write(`: ping\n\n`), 25000);
    req.on("close", () => {
      clearInterval(ping);
      clients.delete(res);
      unsub();
    });
  });
}
