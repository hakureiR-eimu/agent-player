"""游戏接入的实现（声明见 docs/prd/harness.md 游戏接入节）：parser 解析、process 在跑检测、module 模块本体。"""

from game.impl.module import GameModuleImpl, GameNotRunningError

__all__ = ["GameModuleImpl", "GameNotRunningError"]
