## seed 1392041844

https://github.com/MineDojo/Voyager/issues/77

## 运行

- 打开启动器: java -jar TLauncher.jar
- 启动器运行后, Voyager Release, 运行
- Create 或 Recreate 一个世界, 生存模式, 和平
- 进入游戏后打开 Lan 模式, 运行 Cheat, 开启 Lan, 记住端口
- 将端口改到 demo/start.py 或 demo/task.py 里
- 如果要运行 task, 可以改里面的一句话任务
- 需要切换虚拟环境 conda activate voyager
- 删除 tmp 目录
- 然后执行 python demo/start.py 或 demo/task.py
- 然后看日志成功切换回游戏

如果游戏卡住, 并且处于暂停状态, 则需要重进地图
如果游戏卡住, 但是不是暂停状态, 则可以只重启python程序
如果重启了游戏, 换了端口, 则重复`开Lan`及后续步骤
如果重启了python程序, 则重复`删除 tmp`及后续步骤
不能太久暂停游戏, 否则会超时程序卡住


## 怎么看

游戏内的命令 https://github.com/MineDojo/Voyager/issues/19

观察者模式 /gamemode spectator
bot 视角 /spectate bot, 但是因为 bot 总是离开游戏, 所以要经常打, 还不如传送到附近去看
传送到 bot 边上 /teleport bot
或者在 replay 里可以按 / 打开命令, 然后按 b 看玩家, 在bot加入后, 鼠标点击bot, 可以一直以bot视角回放

[ReplayMod](https://github.com/MineDojo/Voyager/issues/115)

