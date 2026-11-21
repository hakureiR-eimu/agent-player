"""入口与装配（声明见 docs/prd/harness.md 主体实现）。

进程从这起：读总配置 → 建事件总线 → 建三大模块 → 各模块接上总线 → 事件主循环 → 收摊退出。
三大模块的实现在各自包里：src/game/（已从独立 mcp-server 迁入）、src/agent/、src/im/，实现进各包 impl/。
"""

from __future__ import annotations

import asyncio
import logging

from agent.module import AgentModule
from config import Config, load_config
from dispatcher import Dispatcher
from events import EventBus
from game.module import GameModule
from game.impl.module import GameModuleImpl
from im.module import ImModule

logger = logging.getLogger(__name__)


def build_modules(config: Config) -> tuple[GameModule, AgentModule, ImModule]:
    """装配第一步：按配置把三大模块建出来。游戏接入已迁入，agent 与 IM 接入待建，建到哪步报哪步：

    - 游戏接入：GameModuleImpl（src/game/impl/），吃总配置的 error.log 路径与游戏进程名
    - agent：src/agent/impl/ 实现后在此实例化
    - IM 接入：src/im/impl/ 实现后在此实例化
    """
    game: GameModule = GameModuleImpl(config)
    raise NotImplementedError("agent 与 IM 接入待建：src/agent/impl/、src/im/impl/")


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
