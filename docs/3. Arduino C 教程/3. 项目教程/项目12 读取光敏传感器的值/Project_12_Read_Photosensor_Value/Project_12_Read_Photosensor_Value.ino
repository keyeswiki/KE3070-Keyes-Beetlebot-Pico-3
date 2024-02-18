//*************************************************************************************
/*
项目 12:读取光敏传感器值
*/
#define PHOTOSENSITIVE_PIN 26 //定义树莓派pico读取光敏的引脚
int photosensitiveADC;        //定义一个变量来存储ADC值

void setup()
{
  pinMode(PHOTOSENSITIVE_PIN, INPUT);//配置输入模式的引脚
  Serial.begin(115200);          //初始化串口，波特率设置为115200
}

void loop()
{
  photosensitiveADC = analogRead(PHOTOSENSITIVE_PIN);//读取光敏电阻值
  Serial.print("photosensitiveADC: ");
  Serial.println(photosensitiveADC);         //打印光敏电阻值
  delay(500);
}
//*************************************************************************************
