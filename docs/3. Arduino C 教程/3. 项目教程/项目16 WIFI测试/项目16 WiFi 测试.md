# 项目16 WiFi 测试

## 1. 实验简介：
ESP8266串口WiFi ESP-01模块，它是一款超低功耗的UART-WiFi 透传模块，拥有业内极富竞争力的封装尺寸和超低能耗技术，专为移动设备和物联网应用设计，可将用户的物理设备连接到Wi-Fi 无线网络上，进行互联网或局域网通信，实现联网功能。
在本实验中，我们使用ESP8266串口WiFi ESP-01模块通过WiFi测试代码软硬件相结合来读取WiFi 的IP地址。

## 2. 实验元件：
|![Img](../../media/ESP8266串口WIFI-ESP-01模块img-20230529145342.png)|![Img](../../media/USB转ESP-01S-WIFI模块串口测试扩展板img-20230529145619.png)|
| :--: | :--: |
| ESP8266串口WiFi ESP-01*1 | USB转ESP-01S WiFi模块串口测试扩展板*1 |

## 3. 元件知识：
![Img](../../media/USB转ESP-01S-WIFI模块串口测试扩展板img-20230529145619.png)    
USB转ESP-01S WiFi模块串口测试扩展板：适用于ESP-01S WiFi模块，扩展板的<span style="color: rgb(0, 209, 0);">拨动开关</span>打到<span style="color: rgb(255, 76, 65);">flash boot</span>端，直插于电脑USB口，用安信可串口调试助手测试AT指令。
扩展板的<span style="color: rgb(0, 209, 0);">拨动开关</span>打到<span style="color: rgb(255, 76, 65);">Uart Download </span>端，直插于电脑USB口，ESP-01模块处于下载模式，通过安信可固件下载软件可下载固件到ESP-01模块中。

![Img](../../media/ESP8266串口WIFI-ESP-01模块img-20230529145342.png)     
ESP8266串口WiFi ESP-01：ESP8266串口WiFi ESP-01是一款超低功耗的UART-WiFi 透传模块，ESP8266串口WIFI ESP-01可广泛应用于智能电网、智能交通、智能家具、手持设备、工业控制等领域。

## 4. 将WIFI模块串口测试扩展板插入电脑的USB口：
A. 将ESP8266串口WIFI ESP-01模块正确方向插入USB转ESP-01S WIFI模块串口测试扩展板上。
![Img](../../media/项目16-1img-20230531162927.png)
B. 先将USB转ESP-01S WIFI模块串口测试扩展板上的<span style="color: rgb(0, 209, 0);">拨码开关</span>拨到<span style="color: rgb(255, 76, 65);">Uart Download</span>端，再将USB转ESP-01S WIFI模块串口测试扩展板插入电脑的USB口。
![Img](../../media/项目16-2img-20230531163028.png)

## 5. 安装驱动文件
这个USB转ESP-01S WIFI模块串口测试扩展板的USB转串口芯片为CH340，我们需要安装这芯片的驱动，**驱动为 <span style="color: rgb(255, 76, 65);">usb_ch341_3.1.2009.06</span>**，我们把该驱动文件放到D盘（即：复制![Img](../../media/项目16-3img-20230531163227.png)
放到D盘），然后开始安装驱动。在不同系统在安装驱动方式大同小异，这里我们在win10系统上开始安装驱动。

A. 当USB转ESP-01S WIFI模块串口测试扩展板第一次接入你的电脑, 右击桌面上的“**我的电脑**”—>“**属性**”—>“**设备管理器**”, 即可看到“**USB-Serial**”。
![Img](../../media/项目16-4img-20230531163252.png)

B. 点击 “**USB-Serial**”, 选择“**更新驱动程序（P）**”。
![Img](../../media/项目16-5img-20230531163335.png)

C. 然后点击“**浏览计算机以查找驱动程序软件**”。 
![Img](../../media/项目16-6img-20230531163512.png)

D. 点击“**浏览（R）...**”找到提供的“**usb_ch341_3.1.2009.06**”驱动文件。(我这里是将“**usb_ch341_3.1.2009.06** ”文件放D盘，你也可以把驱动文件夹放在方便的地方也行)
![Img](../../media/项目16-7img-20230531163554.png)

E. 安装完成后点击“**关闭**”。
![Img](../../media/项目16-8img-20230531163717.png)

F. 驱动安装完成后右键点击“**我的电脑**”—>“**属性**”—>“**设备管理器**”, 你可以看到你CH340驱动程序已经成功安装到电脑，如下图。 
![Img](../../media/项目16-9img-20230531163757.png)

## 5.Arduino搭建Esp8266开发环境                                                  
确保已经将ESP8266串口WIFI ESP-01模块正确插入USB转ESP-01S WIFI模块串口测试扩展板中，然后已经将USB转ESP-01S WIFI模块串口测试扩展板插入电脑的USB口，点击arduino IDE进入arduino IDE界面。
![Img](../../media/项目16-10img-20230531164440.png)

（1）在Arduino IDE里面进行下载安装：
A.点击“**文件**” →“**首选项**”。
![Img](../../media/项目16-11img-20230511105108.png)
B. 打开下图标出的按钮。
![Img](../../media/项目16-12img-20230511105642.png)
C. 将这个地址：http://arduino.esp8266.com/stable/package_esp8266com_index.json ，复制粘贴到里面去再点击“**确定**”保存这个地址，如下图：
![Img](../../media/项目16-13img-20230531165047.png)

D. 再点击“**确定**”。
![Img](../../media/项目16-14img-20230531165135.png)
![Img](../../media/项目16-15img-20230531165206.png)

E. 先点击“**工具**”→“**开发板：**”，再点击“**开发板管理器...**”进入“**开发板管理器**”页面，如下图。
![Img](../../media/项目16-16img-20230531170134.png)
![Img](../../media/项目16-17img-20230531170243.png)

F. 在空格文本框中输入“<span style="color: rgb(255, 76, 65);">ESP8266</span>”，出现搜索内容，选择最新版本进行安装，安装包不大，点击“安装”开始安装相关插件。如下图。（可能会出现下载安装出错，有可能是服务器原因，需要重新点击“安装”就可以了，但由于网络原因，大多用户可能无法搜到<span style="color: rgb(0, 209, 0);">esp8266 by esp8266 Community</span>，对于小白而言不推荐使用此方法添加，推荐下面方法2）
![Img](../../media/项目16-18img-20230531170645.png)
![Img](../../media/项目16-19img-20230531170801.png)

G. 安装成功后点击“**关闭**”关闭页面，然后重启 Arduino IDE 软件，点击 Arduino IDE菜单栏“**工具**”→“**开发板：**” ，可查看到各种不同型号ESP8266开发板。选择对应的ESP8266开发板型号和端口（COMx），选中后即可对ESP8266进行编程。
![Img](../../media/项目16-20img-20230601100240.png)
![Img](../../media/项目16-21img-20230601100454.png)

（2）通过工具对ESP8266进行安装：（推荐使用这种方法）
A. 点击“**文件**” →“**首选项**”，在“**其他开发板管理器网址：**”框中复制粘贴这个地址：http://arduino.esp8266.com/stable/package_esp8266com_index.json ，然后点击“确定”保存这个地址。
![Img](../../media/项目16-22img-20230511105108.png)
![Img](../../media/项目16-23img-20230511105642.png)
![Img](../../media/项目16-24img-20230531165047.png)
![Img](../../media/项目16-25img-20230531165135.png)

B. 使用“<span style="color: rgb(255, 76, 65);">esp8266一键安装arduino板_2.5.0版.exe</span>”，一键安装，此方法安装便捷，且安装较快，推荐此方法安装。
![Img](../../media/项目16-26img-20230531173704.png)

鼠标左键双击“esp8266一键安装arduino板_2.5.0版.exe”，然后就安装完成了。
![Img](../../media/项目16-27img-20230531173815.png)

C. 在上述工具安装完成之后，重启 Arduino IDE 软件，点击 Arduino IDE菜单栏“**工具**”→“**开发板：**”  ，可查看到各种不同型号ESP8266开发板。选择对应的ESP8266开发板型号和端口（COMx），选中后即可对ESP8266进行编程。
![Img](../../media/项目16-28img-20230601100240.png)
![Img](../../media/项目16-29img-20230601100454.png)

## 6.实验代码：                                                                      
<span style="color: rgb(255, 76, 65);">注意：打开IDE后，一定要先设置好ESP8266板型和COM口。手机和设备需要连接在同一个WiFi上，如果家里没有WiFi需要打开手机热点共享WiFi，打开手机热点共享WiFi是最好的方法。</span>

```
//**********************************************************************************
/*  
项目16 : Wifi 测试
Wifi模块测试Wifi的ip
*/
#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <WiFiClient.h>

#ifndef STASSID
//#define STASSID "your-ssid"
//#define STAPSK  "your-password"
#define STASSID "ChinaNet_2.4G"   //用户的wifi名称
#define STAPSK  "ChinaNet@233"       //用户的wifi密码
#endif

const char* ssid = STASSID;
const char* password = STAPSK;

// 端口80的TCP服务器将响应HTTP需求
WiFiServer server(80);

void setup(void) {
  Serial.begin(115200);

  // 连接 WiFi 
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("");

  // 等待连接
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

//设置mDNS响应器:本例中。第一个参数是域名，全限定域名为“esp8266.local”；
//第二个参数是IP地址通过WiFi发送IP地址。

  if (!MDNS.begin("esp8266")) {
    Serial.println("Error setting up MDNS responder!");
    while (1) {
      delay(1000);
    }
  }
  Serial.println("mDNS responder started");

  // 激活TCP (HTTP)服务器
  server.begin();
  Serial.println("TCP server started");

  // 将服务器加入mmds - sd
  MDNS.addService("http", "tcp", 80);
}

void loop(void) {

  MDNS.update();
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  delay(1000);

  // 检查客户端是否连接
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
  Serial.println("");
  Serial.println("New client");

  // 等待来自客户端的有效数据
  while (client.connected() && !client.available()) {
    delay(1);
  }

  // 读取HTTP需求的第一行
  String req = client.readStringUntil('\r');

// HTTP需求的第一行如下所示:"GET /path HTTP/1.1"
// 通过查找空格来检索"/path"部分

  int addr_start = req.indexOf(' ');
  int addr_end = req.indexOf(' ', addr_start + 1);
  if (addr_start == -1 || addr_end == -1) {
    Serial.print("Invalid request: ");
    Serial.println(req);
    return;
  }
  req = req.substring(addr_start + 1, addr_end);
  Serial.print("Request: ");
  Serial.println(req);
  client.flush();

  String s;
  if (req == "/") {
    IPAddress ip = WiFi.localIP();
    String ipStr = String(ip[0]) + '.' + String(ip[1]) + '.' + String(ip[2]) + '.' + String(ip[3]);
    s = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE HTML>\r\n<html>Hello from ESP8266 at ";
    s += ipStr;
    s += "</html>\r\n\r\n";
    Serial.println("Sending 200");
  } else {
    s = "HTTP/1.1 404 Not Found\r\n\r\n";
    Serial.println("Sending 404");
  }
  client.print(s);

  Serial.println("Done with client");
}
//**********************************************************************************

```
**<span style="color: rgb(255, 76, 65);">特别注意：需要先将实验代码![Img](../../media/项目16-33img-20230601101103.png)中的用户Wifi名称和用户Wifi密码改成你们自己的Wifi名称和Wifi密码。</span>**

## 7.实验现象：                                                                     
<span style="color: rgb(61, 167, 66);">实验代码中的Wifi名称和Wifi密码修改后</span>，确保USB转ESP-01S WIFI模块串口测试扩展板上的<span style="color: rgb(255, 76, 65);">拨码开关</span>已经拨到<span style="color: rgb(255, 76, 65);">Uart Download</span> 端，并且也确定USB转ESP-01S WIFI模块串口测试扩展板已经插入电脑的USB口。**然后按照前面方法设置ESP8266板型和COM口**，IDE右下角会显示对应的ESP8266板型和COM口，再点击![Img](../../media/上传按钮img-20230506095425.png)将实验代码上传到ESP8266串口WIFI ESP-01模块上，上传成功。

（<span style="color: rgb(255, 76, 65);">注意：</span>如果上传失败，在板型和COM口没问题下，将USB转ESP-01S WIFI模块串口测试扩展板从电脑的USB口拔下来再次插到电脑的USB口。）
![Img](../../media/项目16-30img-20230601101653.png)
![Img](../../media/项目16-31img-20230601101916.png)

WIFI实验代码上传成功后，先将USB转ESP-01S WIFI模块串口测试扩展板从电脑的USB口拔下来，再将USB转ESP-01S WIFI模块串口测试扩展板上的<span style="color: rgb(255, 76, 0);">拨码开关</span>拨到<span style="color: rgb(255, 76, 65);">Flash Boot</span> 端，然后再次插到电脑的USB口上。打开串口监视器，设置波特率为<span style="color: rgb(255, 76, 65);">115200</span>，即可看到你的WIFI信息，如下图所示：
![Img](../../media/项目16-32img-20230601102155.png)





