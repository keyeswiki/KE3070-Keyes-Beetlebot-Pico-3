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