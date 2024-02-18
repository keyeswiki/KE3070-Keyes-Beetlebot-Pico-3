//**********************************************************************************
/*
项目07 超声波传感器
超声波检测与物体的距离
*/
#define trigPin 10 // 定义trigPin引脚 G10
#define echoPin 11 // 定义echoPin引脚 G11
#define MAX_DISTANCE 700 // 最大传感器距离额定为400-500cm。
//timeOut= 2*MAX_DISTANCE /100 /340 *1000000 = MAX_DISTANCE*58.8
float timeOut = MAX_DISTANCE * 60; 
int soundVelocity = 340; // 定义声速=340m/s
void setup() {
 pinMode(trigPin,OUTPUT);// 设置trigPin为输出模式
 pinMode(echoPin,INPUT); // 设置echoPin为输入模式
 Serial.begin(115200); // 以115200波特打开串行监视器，查看打印结果。
}
void loop() {
 delay(100); // 等待100毫秒
 Serial.print("Distance: ");
 Serial.print(getSonar()); // 发送距离值，以厘米为单位获取距离并打印结果
 Serial.println("cm");
}
float getSonar() {
 unsigned long pingTime;
 float distance;
 // 使trigPin输出高电平持续10us触发HC_SR04
 digitalWrite(trigPin, HIGH); 
 delayMicroseconds(10);
 digitalWrite(trigPin, LOW);
 // 等待HC-SR04回到高电平并测量这个等待时间
 pingTime = pulseIn(echoPin, HIGH, timeOut); 
 // 根据时间计算距离
 distance = (float)pingTime * soundVelocity / 2 / 10000; 
 return distance; // 返回距离值
}
//**********************************************************************************
