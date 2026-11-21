"""游戏接入的接口声明（agent 的眼睛）：实现在 impl/（parser 解析、process 在跑检测、module 模块本体）。

声明三个能力：读方法 get_state、写方法 start_play、新年判定方法 check_new_year。
get_state/start_play 给 agent 调——主体装配时把它们包成会话工具（agent 调工具由
主体翻译成对方法的实际调用）；check_new_year 由主体定时调，查到新年份由主体推
new_year 事件。本模块零总线、零 agent 知识。
实现语义见 docs/prd/游戏接入-harness侧.md。
"""

from __future__ import annotations

from typing import Protocol


class GameModule(Protocol):
    """游戏接入的接口形状：实现 GameModuleImpl 在 impl/。

    三个能力，都以游戏在跑为前提（check_new_year 在游戏没跑时返回 None）：
    - get_state——读方法：读取世界局势，各国最新一条记录拼成的世界格局快照
    - start_play——写方法：发起一局外交博弈
    - check_new_year——新年判定：查 error.log 是否出现新的本局记录年份，有返回该年份、没有返回 None
    """

    # ---- 三个能力（前两个给 agent 调，新年判定给主体定时调） ----

    def get_state(self) -> dict:
        """读取世界局势：各国最新一条记录拼成的快照（powers 按 rank 升序），结构化数据。"""
        ...

    def start_play(self) -> str:
        """发起外交博弈：实现空置，返回固定的"未实现"应答。"""
        ...

    def check_new_year(self) -> int | None:
        """新年判定：查一次 error.log，出现比上次已通知新的本局记录年份返回该年份，没有返回 None。"""
        ...
