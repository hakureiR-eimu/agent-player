"""IM 接入包（agent 的嘴和耳朵，通 Discord）：实现在 impl/。

两块能力：命令通道（大厅频道与私信收玩家命令，推 command）、局频道 vic3-GreatBritain
（玩家消息推 message，订 reply 发回复）。接口形状见 src/dispatcher.py 的 ImModule。
文档见 docs/prd/harness.md 的 IM 接入节。
"""
