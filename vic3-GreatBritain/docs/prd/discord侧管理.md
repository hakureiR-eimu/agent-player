# discord侧管理

Discord 平台侧要办的活：建两个 bot、拉进服务器、token 交给 harness——办完这些，IM 接入（实现见 [Discord 接入](discord接入.md)）就能连上 Discord。步骤对着 Discord 官方开发者后台（discord.com/developers/applications），界面如有出入以后台为准；涉平台事实的结论沿用 [Discord 接入](discord接入.md) 平台事实节的证据等级（一等＝官方文档）。

## 建两个 bot

每个 bot 一个应用，各办一遍：dm bot（主持命令）与 gbr bot（大不列颠玩家的门面，agent 的话从它嘴里出）。

1. 开发者后台 New Application 起名建应用
2. 左侧 Bot 页 → Reset Token → 复制 token——只显示这一次，抄下来
3. token 填进开发文件夹的 config.toml（模板 config.example.toml）：dm bot 的进 dm_token、gbr bot 的进 gbr_token（token 是凭证，config.toml 不进库）
4. 后台没有要打开的开关：bot 收发消息靠的 intent（服务器消息、私信消息）是非特权的，Discord 默认全给、后台不设开关；Bot 页 Privileged Gateway Intents 段陈列的三个开关（Presence、Server Members、Message Content）全是特权项，都保持关闭——与 bot 的私信、@ 到 bot 的消息豁免 MESSAGE_CONTENT（一等，Gateway 文档），harness 用 Intents.default() 就够。要授权的权限（View Channel、Send Messages）在邀请 bot 进服务器时给，见下节
5. Public Bot 关掉（Bot 页 Authorization Flow 段）：只有你能邀请，旁人拉不走

## 拉进服务器

两个 bot 都拉进人类玩家所在的同一个服务器——gbr bot 主动私信玩家的前提是玩家与 bot 同服务器（一等，Channels 文档）。

邀请走 OAuth2 链接，两种做法等价：

- 后台 OAuth2 → URL Generator：SCOPES 勾 bot，BOT PERMISSIONS 勾 View Channel、Send Messages（dm bot 再加勾 Manage Channels），复制底部生成的 URL，浏览器打开 → 选服务器 → 授权
- 直接拼链接：`https://discord.com/oauth2/authorize?client_id=<应用ID>&scope=bot&permissions=3072`（gbr bot 用这个；dm bot 把 3072 换成 3088——3072＝View Channel＋Send Messages，3088 再加 Manage Channels。应用 ID 在后台 General Information 页）

权限：View Channel（读公屏消息）、Send Messages（公屏提示与回执）两个 bot 都要；dm bot 还要 Manage Channels——开始游戏建本局频道（GreatBritain）、结束游戏销掉（一等前提，见 Discord 接入的平台事实节）。私信通道不走服务器权限，玩家侧的开销见下节。

## 人类玩家侧要办的（一次性）

- 允许服务器成员私信：右键服务器图标 → 隐私设置 → 打开"允许来自服务器成员的私信"——玩家隐私设置允许 bot 私信是一等前提（一等，Channels 文档），关着的话 bot 私信发出去被拒（403）
- 开发者模式（用户设置 → 高级 → 开发者模式）：右键头像能复制用户 ID——e2e 测试的 E2E_DISCORD_PLAYER_ID 用它

## 网络

国内网络直连不到 discord.com（连接被拒或超时），两个 bot 的登录与收发都在 Discord 的服务器上，程序得有一条能到 Discord 的路，两种做法挑一：

- 代理软件开 TUN／接管模式：整个进程的路由都被接管，harness 不用配任何东西
- config.toml 填 discord_proxy 指到本地代理端口（Clash 系是 `http://127.0.0.1:7890`，v2rayN 是 `http://127.0.0.1:10809`，以你的代理软件设置页为准）——REST 登录与 Gateway 长连接都走它（discord.py 的 Client proxy 参数）

## 验收

token 填好后（在 vic3-GreatBritain/ 目录执行）：

- `uv run python -m main` 启动——日志出现"dm bot 已登录 Discord""gbr bot 已登录 Discord"即连上
- 公屏 @ dm bot 发开始游戏：命令行打印命令内容，Discord 公屏收到回执（agent 未建的现在，回执如实报"agent 模块未建"，频道不建——agent 落地后这条会真建出 GreatBritain 频道）
- 私信 gbr bot 一句话：命令行打印私信内容
- e2e 一轮（给人发真私信）：`E2E_DISCORD_PLAYER_ID=<玩家ID> uv run pytest -m e2e test/im/test_im_e2e.py -s`

## 日常管理

- token 换发：怀疑泄漏或想换 token 时，后台 Bot 页 Reset Token，新 token 改进 config.toml 重启进程——旧 token 立即作废
- 门面观感：名字与头像在后台改，昵称在服务器里改——dm bot 是主持的门面、gbr bot 是大不列颠玩家的门面，叫什么长什么样归沉浸感管，跟 agent 的人设对齐着来
- 在线状态：两个 bot 的在线就是 harness 进程的活着——进程在跑才在线，Ctrl+C 退出后双双离线
