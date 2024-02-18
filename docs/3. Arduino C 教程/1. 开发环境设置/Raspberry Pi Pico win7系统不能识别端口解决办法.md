# Raspberry Pi Pico win7/8系统不能识别端口解决办法

按照下面这个步骤操作，第一次上传后没有出现端口。

打开示例代码后，编译前，要特別注意操作的顺序：
(1) 先断开Raspberry Pi Pico USB电源
(2) 按住开发板上白色 BOOTSEL 按鍵，然后插上USB电源 
(3) 点击Arduino IDE下的上传按钮![Img](../media/上传按钮img-20230506095425.png)，进行编译并上传至Raspberry Pi Pico开发板。 
(4) 等到编译“正在编译项目...”，下面提示信息出现上传中“正在上传...”，再松开BOOTSEL按键。
(5) 等待至上传完毕“上传完成”才算完成。
第一次上传过程中一定要注意这个顺序，不然则导致上传失败，后面上传选择对应的“端口”直接点击上传即可。上传完成后，就可以看到Raspberry Pi Pico开发板上的LED在闪烁。
![Img](../media/win7系统不能识别端口解决办法1img-20230511114713.png)
![Img](../media/win7系统不能识别端口解决办法2img-20230511113222.png)

接下来按照下面的操作步骤操作，可以出现串口。
第一步：将Raspberry Pi Pico开发板通过USB线连接到电脑。
第二步：打开我们提供的软件![Img](../media/win7系统不能识别端口解决办法3img-20230506102944.png)。
第三步：USB ID 红色框内为<span style="color: rgb(255, 76, 65);">2E8A</span> 。     
Driver红色框内为 USB Serial(CDC)，后面的箭头可以选择。
![Img](../media/win7系统不能识别端口解决办法4img-20230506103045.png)
第四步:点击下载，等待下载完毕就成功了，这一步最好关闭杀毒软件。
![Img](../media/win7系统不能识别端口解决办法5img-20230506103100.png)
![Img](../media/win7系统不能识别端口解决办法6img-20230506103104.png)
![Img](../media/win7系统不能识别端口解决办法7img-20230506103114.png)
<span style="color: rgb(255, 76, 65);">如果第一次没成功那就拔掉Raspberry Pi Pico板重新再插上，再重新安装一遍。</span>







