//*************************************************************************************
/*
项目05 舵机转动
控制舵机进行扫地
*/
#include <Servo.h>
#define servoPin 9

Servo myServo;  // 创建舵机对象来控制舵机
int pos = 0;    // 变量存储舵机位置

void setup() {
  myServo.attach(servoPin);  // 将引脚9上的伺服连接到伺服对象上
}

void loop() {
  for (pos = 0; pos <= 180; pos += 1) { // 从0°到180°
    // in steps of 1 degree
    myServo.write(pos);              // 告诉舵机到变量“pos”的位置
    delay(15);                       // 等待15毫秒舵机到达“pos”的位置
  }
  for (pos = 180; pos >= 0; pos -= 1) { // 从180°到0°
    myServo.write(pos);              // 告诉舵机到变量“pos”的位置
    delay(15);                       // 等待15毫秒舵机到达“pos”的位置
  }
}
//********************************************************************************
