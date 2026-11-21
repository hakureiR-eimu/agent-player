"""端到端演示测试（默认不跑，跑法：uv run pytest -m e2e -s）。

直接调游戏接入模块（server.py）的函数看效果：get_state() 返回真实世界格局
快照、start_play() 返回固定"未实现"应答。游戏在跑才通过；游戏没跑则
get_state() 抛"游戏未启动"、测试失败。MCP stdio 通道（起子进程、经客户端调）
的验证在 test_tools.py，这里不重复。
"""

import pytest

import server

pytestmark = pytest.mark.e2e


def test_get_state_returns_real_snapshot_when_game_running():
    """第一个函数 get_state()：游戏在跑时，应返回真实世界格局快照。"""
    # 构造调用：无参数
    # 调用：
    snapshot = server.get_state()

    # 查看结果：
    print(f"\nget_state() —— powers（{len(snapshot['powers'])} 国，按名次）：")
    for power in snapshot["powers"]:
        print(
            f"  {power['rank']:>2}  {power['tag']}  {power['year']}  "
            f"gdp={power['gdp']:.0f}  army={power['army']}"
        )
    fin = snapshot["gbr_finance"]
    if fin:
        print(
            f"GBR 财政 {fin['year']}：金库={fin['gold']:.0f} "
            f"债务本金={fin['debt']:.0f} 周净收支={fin['week_net']:.0f}"
        )
    assert snapshot["powers"], "一条国家记录都没读到——error.log 里有本局记录吗？"
    assert fin, "没读到 GBR 财政记录"


def test_start_play_returns_fixed_not_implemented_response():
    """第二个函数 start_play()：写侧占位函数，应返回固定的"未实现"应答。"""
    # 构造调用：无参数
    # 调用：
    response = server.start_play()

    # 查看结果：
    print(f"\nstart_play() —— {response}")
    assert "未实现" in response
