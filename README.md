# -Fire-Emblem-battlefield-battle-music-switch
实现同一首曲子两种不同版本的实时切换功能


火焰纹章是任天堂的一款战旗游戏，在玩游戏时我很喜欢他的背景音乐。
在火焰纹章中，若玩家在战场中切入战斗界面，其bgm会换成节奏更为激烈，乐器更为丰富的版本，这样一来，就可以解决玩家可能对一场可能动辄半小时的战斗的音乐感到无聊的问题。
游戏外在工作学习过程中，我也想实现这样的功能，但市面上任何一款音乐播放器都没有这样的功能，即两首曲子（时间一样），从A曲中断后播放B曲，能从A中断的位置开始，实现无缝的音乐切换。
除了该游戏外，该功能同样适用于其他多版本的曲目。

功能主要透过Pygame（提供音乐播放功能），eyed3(读取音频文件信息），datetime（获取时间）等库实现。

代码部分请参考：
火焰纹章 战场与战斗曲目切换.py
