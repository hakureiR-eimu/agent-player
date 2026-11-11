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
  const hint = $("configHint");
  const missing = state.availableCountries.filter((c) => !state.countryConfigured[c.tag]).map((c) => c.tag);
  hint.textContent = missing.length
    ? `飞书已接上。还没配应用的国家：${missing.join("、")}（config/feishu.json）。机器人在群里的显示名＝机器人名称，想让群里显示 tag，就把应用名设成 tag。`
    : "飞书已接上，8 国应用齐。机器人在群里的显示名＝机器人名称（应用名设成 tag 就会显示 tag）。";

  const hasGame = Boolean(state.game);
  $("resumeCard").classList.toggle("hidden", hasGame || !state.saved);
  if (state.saved) {
    const t = state.saved.savedAt ? `，存于 ${state.saved.savedAt.slice(0, 16).replace("T", " ")}` : "";
    $("resumeMeta").textContent = `「${state.saved.name}」${t}。开新局会顶掉它，之后不能继续。`;
    $("resumeBtn").textContent = `继续「${state.saved.name}」`;
  }
  $("setup").classList.toggle("hidden", hasGame);
  $("game").classList.toggle("hidden", !hasGame);
  if (!hasGame) renderSetup();
  else renderGame();
}

// 国家列表的签名：没变就不重画——state 每 3 秒推一次，重画会把勾选清掉
let countriesSig = "";

function renderSetup() {
  const sig = JSON.stringify([
    state.availableCountries.map((c) => [c.tag, Boolean(state.countryConfigured[c.tag])]),
  ]);
  if (sig === countriesSig) return;
  countriesSig = sig;

  const box = $("countries");
  box.innerHTML = "";

  // 一级：全选
  const parent = document.createElement("label");
  parent.className = "country-all";
  parent.innerHTML =
    '<input type="checkbox" id="allCountries" />' +
    '<span class="country-all-label">全选国家</span>' +
    '<span class="country-count" id="countryCount"></span>';
  box.appendChild(parent);

  // 二级：各国
  const children = document.createElement("div");
  children.className = "country-children";
  for (const c of state.availableCountries) {
    const configured = state.countryConfigured[c.tag];
    const disabled = !configured;
    // 名字自带的"（TAG）"尾缀去掉，tag 已经单独显示了
    const name = c.name.endsWith(`（${c.tag}）`) ? c.name.slice(0, -(c.tag.length + 2)) : c.name;
    const label = document.createElement("label");
    label.className = "country-item" + (disabled ? " disabled" : "");
    label.innerHTML =
      `<input type="checkbox" class="country-check" value="${c.tag}" ${disabled ? "disabled" : ""} />` +
      `<span class="tag">${c.tag}</span><span class="name">${esc(name)}</span>` +
      (disabled ? '<span class="warn">没配应用</span>' : "");
    children.appendChild(label);
  }
  box.appendChild(children);

  // 父子联动：勾父全选，子级变化时父级在全选/半选/全不选之间走
  const all = $("allCountries");
  const checks = [...children.querySelectorAll("input")];
  const usable = checks.filter((i) => !i.disabled);
  const updateParent = () => {
    const n = usable.filter((i) => i.checked).length;
    all.checked = n > 0 && n === usable.length;
    all.indeterminate = n > 0 && n < usable.length;
    $("countryCount").textContent = `已勾 ${n} / ${usable.length}`;
  };
  all.addEventListener("change", () => {
    for (const i of usable) i.checked = all.checked;
    updateParent();
  });
  checks.forEach((i) => i.addEventListener("change", updateParent));
  updateParent();
}

function renderGame() {
  const g = state.game;
  $("gameTitle").textContent = `局「${g.name}」`;
  $("gameMeta").textContent = `开了 ${g.agents.length} 个 agent；局文件夹：${state.gameDir}`;
  $("mainGroup").textContent =
    `「${g.mainGroupName}」（${g.mainGroupId ?? ""}）—— 群主是 DM，真话去飞书里说`;

  const tbody = $("agentTable").querySelector("tbody");
  tbody.innerHTML = "";
  for (const a of g.agents) {
    const tr = document.createElement("tr");
    const note = a.lastError ? `出错：${a.lastError}` : a.throttled > 0 ? `限速压了 ${a.throttled} 次` : "";
    tr.innerHTML =
      `<td><b>${a.tag}</b></td>` +
      `<td><span class="status st-${a.status}">${statusName(a.status)}</span></td><td>${a.queued}</td><td>${a.rounds}</td>` +
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
  div.innerHTML =
    `<div class="msg-head"><span class="who">【${esc(m.groupName)}】${esc(m.speaker)}</span><span class="time">${t}</span></div>` +
    `<div class="msg-body">${esc(m.content)}</div>`;
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
  if (state.saved && !confirm(`存着的「${state.saved.name}」会被新局顶掉，之后不能继续它。仍要开新局？`)) return;
  // 只取二级的国家勾选，一级全选框不算
  const tags = [...document.querySelectorAll("#countries .country-check:checked")].map((i) => i.value);
  try {
    await post("/api/game", { name: $("gameName").value, tags });
  } catch (e) {
    $("setupError").textContent = e.message;
  }
};

$("resumeBtn").onclick = async () => {
  try {
    await post("/api/game/resume", {});
  } catch (e) {
    alert(e.message);
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

$("saveBtn").onclick = async () => {
  try {
    await post("/api/game/save", {});
  } catch (e) {
    alert(e.message);
  }
};

$("stopBtn").onclick = async () => {
  if (!confirm("结束这一局？之后不能继续，局文件夹和飞书群留档。")) return;
  try {
    await post("/api/game/stop", {});
  } catch (e) {
    alert(e.message);
  }
};

// ---------- 开跑 ----------

refresh().then(connectEvents);
