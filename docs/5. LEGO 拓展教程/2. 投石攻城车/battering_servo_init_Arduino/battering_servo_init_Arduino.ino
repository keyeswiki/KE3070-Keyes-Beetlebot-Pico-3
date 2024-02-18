#include <Servo.h>
Servo lgservo;  // 创建舵机对象来控制舵机

void setup() {
  lgservo.attach(3);  // 将舵机接到引脚G3上
}

void loop() {
  lgservo.write(0); // 舵机转到对应角度位置
}
