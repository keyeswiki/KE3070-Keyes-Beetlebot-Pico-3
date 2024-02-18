from machine import ADC, Pin
import time

# 将光敏电阻初始化为引脚26 (ADC功能)
adc = ADC(Pin(26))

# 循环打印光敏电阻的当前adc值 
try:
    while True:
        adcValue = adc.read_u16() # 读取光敏电阻的ADC值
        print("ADC Value:", adcValue) #发送光敏电阻ADC值并打印结果。
        time.sleep(0.5)
except:
    pass