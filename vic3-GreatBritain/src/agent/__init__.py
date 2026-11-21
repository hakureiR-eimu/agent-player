"""agent 包：agent 本体是 Claude Code 会话，能力声明补齐后在 impl/ 实现。

事件侧已定：订 message、new_year（会话空闲就叫醒，忙时攒着、空闲一批送进），推 reply。
会话随局起止——start_session（起会话，fresh 区分建全新 GBR 与用已有）、stop_session（让会话
整理自己的文件夹后结束）的调用顺序由调度排，接口形状见 src/dispatcher.py 的 AgentModule。
文档见 docs/prd/harness.md 的 agent 节。
"""
