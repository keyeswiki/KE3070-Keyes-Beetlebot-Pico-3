/*
  Project 00 Steering gear is initialized_Arduino
  调节舵机初始角度为90°.
*/
int servoPin = 9;//舵机的PIN

void setup() {
  pinMode(servoPin, OUTPUT);//舵机引脚设置为输出
  servopulse(servoPin, 90);//转动到90度
  delay(1000);
}

void loop() {
  
}

void servopulse(int pin, int myangle) { //脉冲函数
  int pulsewidth = map(myangle, 0, 180, 500, 2500); //将角度映射到脉宽
  for (int i = 0; i < 10; i++) { //多输出几次脉冲
    digitalWrite(pin, HIGH);//将舵机接口电平至高
    delayMicroseconds(pulsewidth);//延时脉宽值的微秒数
    digitalWrite(pin, LOW);//将舵机接口电平至低
    delay(20 - pulsewidth / 1000);
  }
}
