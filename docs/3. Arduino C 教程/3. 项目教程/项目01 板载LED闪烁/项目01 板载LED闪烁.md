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

```
//**********************************************************************
/*
项目 01：板载LED闪烁
使PICO主板上的LED闪烁.
*/
#define LED_BUILTIN 25

// 按复位键或单板上电时，设置功能运行一次
void setup() {
  // 初始化数字引脚LED_BUILTIN作为输出模式.
  pinMode(LED_BUILTIN, OUTPUT);
}

// 循环函数会一直运行下去
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // 点亮LED (HIGH是高电平)
  delay(1000);                       // 延时1秒
  digitalWrite(LED_BUILTIN, LOW);    // 通过使电压为0来关闭LED
  delay(1000);                       // 延时1秒
}
//*************************************************************************************

```
在上传实验代码到Raspberry Pi Pico之前，请检查Arduino IDE的配置。
单击“**工具**”，确认“**开发板**”板型和“**端口**”，如下所示：
![Img](../../media/项目01-1img-20230531132905.jpg)

单击![Img](../../media/上传按钮img-20230506095425.png)将实验代码上传到Raspberry Pi Pico。
![Img](../../media/项目01-2img-20230531133117.png)

实验代码上传成功！
![Img](../../media/项目01-3img-20230531133211.png)

## 5.实验结果：
项目代码上传成功后，利用USB线上电，可以看到的现象是：Raspberry Pi Pico的LED开始闪烁，循环进行。
![Img](../../media/项目01-4img-20230506132541.png)

