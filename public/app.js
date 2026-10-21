// 控制台前端：原生 JS，无构建。SSE 收实时消息，fetch 调接口。

const $ = (id) => document.getElementById(id);
let state = null;

// ---------- 初始化 ----------

async function refresh() {
  const res = await fetch("/api/state");
  state = await res.json();
  render();
}

function connectEvents() {
  const es = new EventSource("/api/events");
  es.addEventListener("state", (e) => {
    state = JSON.parse(e.data);
    render();
  });
  es.onmessage = (e) => {
    const ev = JSON.parse(e.data);
    if (ev.type === "chat") appendChat(ev.chat);
    if (ev.type === "log") appendLog(ev);
  };
}

// ---------- 渲染 ----------

function render() {
  const badge = $("modeBadge");
  badge.textContent = state.mode === "feishu" ? "飞书模式" : "本地模式";
  badge.className = "badge " + (state.mode === "feishu" ? "ok" : "local");

  const hint = $("configHint");
  if (state.mode === "local") {
    hint.textContent = "没配飞书（config/feishu.json 缺失或没填 DM 应用），群只在控制台里。想上飞书：把 config/feishu.example.json 拷成 config/feishu.json 填好 DM 和各国应用。";
  } else {
    const missing = state.availableCountries.filter((c) => !state.countryConfigured[c.tag]).map((c) => c.tag);
    hint.textContent = missing.length
      ? `飞书已接上。还没配应用的国家：${missing.join("、")}（config/feishu.json）。机器人在群里的显示名＝机器人名称，想让群里显示 tag，就把应用名设成 tag。`
      : "飞书已接上，8 国应用齐。机器人在群里的显示名＝机器人名称（应用名设成 tag 就会显示 tag）。";
  }

  const hasGame = Boolean(state.game);
  $("setup").classList.toggle("hidden", hasGame);
  $("game").classList.toggle("hidden", !hasGame);
  if (!hasGame) renderSetup();
  else renderGame();
}

function renderSetup() {
  const box = $("countries");
  box.innerHTML = "";
  for (const c of state.availableCountries) {
    const label = document.createElement("label");
    const configured = state.countryConfigured[c.tag];
    label.innerHTML =
      `<input type="checkbox" value="${c.tag}" ${state.mode === "feishu" && !configured ? "disabled" : ""} /> ` +
      `<b>${c.tag}</b> ${c.name}` +
      (state.mode === "feishu" && !configured ? `<span class="warn">（没配应用）</span>` : "");
    box.appendChild(label);
  }
}

function renderGame() {
  const g = state.game;
  $("gameTitle").textContent = `局「${g.name}」`;
  const kindName = g.agents[0]?.kind === "fake" ? "假" : "真";
  $("gameMeta").textContent =
    `开了 ${g.agents.length} 个${kindName} agent；局文件夹：${state.gameDir}`;
  $("mainGroup").textContent =
    `「${g.mainGroupName}」（${g.mainGroupId ?? ""}）—— 群主是 DM` +
    (g.mode === "local" ? "，本地群，说话用下面的输入框" : "，真话去飞书里说");

  const tbody = $("agentTable").querySelector("tbody");
  tbody.innerHTML = "";
  for (const a of g.agents) {
    const tr = document.createElement("tr");
    const note = a.lastError ? `出错：${a.lastError}` : a.throttled > 0 ? `限速压了 ${a.throttled} 次` : "";
    tr.innerHTML =
      `<td><b>${a.tag}</b></td><td>${a.kind === "fake" ? "假" : "真"}</td>` +
      `<td>${statusName(a.status)}</td><td>${a.queued}</td><td>${a.rounds}</td>` +
      `<td class="mono">${a.sessionId ? a.sessionId.slice(0, 8) : "—"}</td><td class="warn">${note}</td>`;
    tbody.appendChild(tr);
  }

  const ul = $("groupList");
  ul.innerHTML = "";
  for (const grp of g.groups) {
    const li = document.createElement("li");
    li.textContent = `${grp.name}（${grp.id}）：${[...grp.agents, ...grp.humans.map((h) => h.name)].join("、")}`;
    ul.appendChild(li);
  }

  const localSay = g.mode === "local";
  $("sayRow").classList.toggle("hidden", !localSay);
  $("chatHint").classList.toggle("hidden", localSay);

  // 聊天和日志全量重画（量小，够用）
  const chat = $("chat");
  chat.innerHTML = "";
  for (const m of state.chats ?? []) appendChat(m);
  const logs = $("logs");
  logs.innerHTML = "";
  for (const l of state.logs ?? []) appendLog(l);
}

function statusName(s) {
  return { starting: "启动中", idle: "待着", busy: "跑一轮", error: "出错", stopped: "已停" }[s] ?? s;
}

function appendChat(m) {
  const div = document.createElement("div");
  div.className = "msg " + m.speakerKind;
  const t = m.ts.slice(11, 16);
  div.innerHTML = `<span class="time">${t}</span> <span class="who">【${esc(m.groupName)}】${esc(m.speaker)}</span>：${esc(m.content)}`;
  $("chat").appendChild(div);
  div.scrollIntoView({ block: "end" });
}

function appendLog(l) {
  const div = document.createElement("div");
  div.className = "logline " + l.level;
  div.textContent = `[${l.ts.slice(11, 19)}] ${l.line}`;
  $("logs").appendChild(div);
  while ($("logs").children.length > 200) $("logs").firstChild.remove();
}

function esc(s) {
  return String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
}

// ---------- 动作 ----------

async function post(path, body) {
  const res = await fetch(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.error ?? res.statusText);
  return data;
}

$("createBtn").onclick = async () => {
  $("setupError").textContent = "";
  const tags = [...document.querySelectorAll("#countries input:checked")].map((i) => i.value);
  const kind = document.querySelector('input[name="kind"]:checked').value;
  try {
    await post("/api/game", { name: $("gameName").value, tags, kind });
  } catch (e) {
    $("setupError").textContent = e.message;
  }
};

$("addHumanBtn").onclick = async () => {
  try {
    const r = await post("/api/game/humans", { ids: $("humanIds").value });
    $("humanIds").value = "";
    alert(`已拉进群：${r.added.join("、")}`);
  } catch (e) {
    alert(e.message);
  }
};

$("stopBtn").onclick = async () => {
  if (!confirm("结束这一局？agent 会停下，局文件夹保留。")) return;
  await post("/api/game/stop", {});
};

async function say() {
  const name = $("sayName").value.trim();
  const content = $("sayContent").value.trim();
  if (!name || !content) return;
  try {
    await post("/api/say", { name, content });
    $("sayContent").value = "";
  } catch (e) {
    alert(e.message);
  }
}
$("sayBtn").onclick = say;
$("sayContent").addEventListener("keydown", (e) => {
  if (e.key === "Enter") say();
});

// ---------- 开跑 ----------

refresh().then(connectEvents);
