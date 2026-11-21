"""入口与装配（声明见 docs/prd/harness.md 主体实现）。

进程从这起：读总配置 → 建事件总线 → 建三大模块 → 各模块接上总线 → 事件主循环 → 收摊退出。
三大模块的实现在各自包里：src/game/（现有 mcp-server 迁入）、src/agent/、src/im/，实现进各包 impl/。
"""

from __future__ import annotations

import asyncio
import logging

from config import Config, load_config
from dispatcher import AgentModule, Dispatcher, GameModule, ImModule
from events import EventBus

logger = logging.getLogger(__name__)


def build_modules(config: Config) -> tuple[GameModule, AgentModule, ImModule]:
    """装配第一步：按配置把三大模块建出来。骨架阶段三块都没建，迁入/实现一块改一处：

    - 游戏接入：mcp-server（开发文件夹下的 mcp-server/server.py）迁入 src/game/impl/ 后在此实例化
    - agent：src/agent/impl/ 实现后在此实例化
    - IM 接入：src/im/impl/ 实现后在此实例化
    """
    raise NotImplementedError(
        "三大模块待建：游戏接入待迁入 src/game/impl/（现有 mcp-server），agent 与 IM 接入待实现"
    )


async def run() -> None:
    config = load_config()
    bus = EventBus()
    game, agent, im = build_modules(config)
    dispatcher = Dispatcher(bus, game, agent, im)
    await game.start(bus)
    await agent.start(bus)
    await im.start(bus)
    try:
        await bus.run()
    finally:
        # 进程收摊：会话还在跑先按 stopGame 收尾，再按装配的反序让模块停
        await dispatcher.shutdown()
        await im.stop()
        await agent.stop()
        await game.stop()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        logger.info("收到 Ctrl+C，进程退出")


if __name__ == "__main__":
    main()
