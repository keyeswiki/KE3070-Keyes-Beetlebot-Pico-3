//*************************************************************************************
/*
项目 03 演奏音乐
蜂鸣器播放音乐
*/
#define PIN_BUZZER 12   //定义蜂鸣器的引脚

void setup() {
  pinMode(PIN_BUZZER, OUTPUT);
}

void loop() {
    alert();
}

void alert() {
  float sinVal;         // 定义一个变量来保存正弦值
  int toneVal;          // 定义一个变量来保存声音频率
  for (int x = 0; x < 360; x += 10) {     // X从0°到360°
    sinVal = sin(x * (PI / 180));       // 计算sinx
    toneVal = 2000 + sinVal * 500;      // 根据sinx计算声音频率
    freq(PIN_BUZZER, toneVal, 10);
  }
}

void freq(int PIN, int freqs, int times) {
  if (freqs == 0) {
    digitalWrite(PIN, LOW);
  }
  else {
    for (int i = 0; i < times * freqs / 1000; i ++) {
      digitalWrite(PIN, HIGH);
      delayMicroseconds(1000000 / freqs / 2);
      digitalWrite(PIN, LOW);
      delayMicroseconds(1000000 / freqs / 2);
    }
  }
}
//**********************************************************************
