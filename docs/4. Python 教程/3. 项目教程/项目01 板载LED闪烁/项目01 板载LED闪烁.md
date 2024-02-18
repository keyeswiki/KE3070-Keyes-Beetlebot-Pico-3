# 项目01 板载LED闪烁

## 1.实验介绍：
Raspberry Pi Pico上有个板载LED，这个LED是固定接在Raspberry Pi Pico上的GP25引脚，在这个项目中，我们将来学习使板载LED闪烁的效果。

## 2.实验元件：
|![Img](../../media/Pico主板img-20230531131559.png)| ![Img](../../media/USB线img-20230531131614.png) |
| :--: | :--: |
| Raspberry Pi Pico*1 |USB 线*1 |

## 3.实验接线：
在本项目中，用USB线将Raspberry Pi Pico和电脑连起来。连接方法请参照文档：<span style="color: rgb(255, 76, 65);">开发环境配置</span>
![Img](../../media/项目01-实验接线img-20230510173548.png)

## 4.实验代码：
Raspberry Pi Pico板载LED是由GP25控制，当GP25输出高电平时，LED点亮;当输出低时，LED灯关闭。

本教程中使用的代码保存在：“**..\Keyes Beetlebot Pico 3合1 智能小车\4. Python 教程\3. 项目教程**” 的路径中。你可以把代码移到任何地方。例如，我们将代码保存在**D盘**中，<span style="color: rgb(0, 209, 0);">路径为D:\3. 项目教程</span>。
![Img](../../media/电脑D盘路径img-20230601164744.png)

打开“**Thonny**”软件，点击“**此电脑**”→“**D:**”→“**3. 项目教程**”→“**项目01 板载LED闪烁**”，然后鼠标左键双击“**Project_01_Onboard_LED_Flashing.py**”。
![Img](../../media/项目01-1img-20230602082534.png)

```
from machine import Pin
import time

led = Pin(25, Pin.OUT)   # 从引脚25创建LED对象，设置引脚25输出

try:
    while True:
        led.value(1)    # 点亮LED
        time.sleep(0.5) # 延时 0.5s
        led.value(0)    # 关闭LED
        time.sleep(0.5) # 延时 0.5s
except:
    pass

```

## 5.实验结果：
确保Raspberry Pi Pico主板已经连接到电脑上，单击“![Img](../../media/停止或重启后端进程img-20230511100302.png)”。
![Img](../../media/项目01-2img-20230602082956.png)

利用USB线上电，单击“![Img](../../media/运行img-20230511100130.png)”，代码开始执行，你会看到的现象是：Raspberry Pi Pico的LED开始闪烁，循环进行。按“Ctrl+C”或单击“![Img](../../media/停止或重启后端进程img-20230511100302.png)”退出程序。
![Img](../../media/项目01-3img-20230602083543.png)
![Img](../../media/项目01-4img-20230506132541.png)

