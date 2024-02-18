from machine import Pin, ADC, PWM
import time

#定义GPIO9的输出频率为50Hz，占空比为4915，并分配给PWM。
servoPin = PWM(Pin(9))
servoPin.freq(50)
servoPin.duty_u16(4915)
time.sleep(1)

# 初始化左光阻至引脚26 (ADC功能)
adc1 = ADC(Pin(26))

# 将右光阻初始化为引脚27 (ADC功能)
adc2 = ADC(Pin(27))

# 右轮
pin1=Pin(14,Pin.OUT)
pin2=PWM(Pin(16))
pin2.freq(50)
# 左轮
pin3=Pin(15,Pin.OUT)
pin4=PWM(Pin(17))
pin4.freq(50)

# 作为小车前进的函数。
def car_forward(): 
  pin1.value(0)
  pin2.duty_u16(18000) 
  pin3.value(0)
  pin4.duty_u16(18000) 

# 作为小车向左的函数。
def car_left(): 
  pin1.value(0)
  pin2.duty_u16(18000)  
  pin3.value(1)
  pin4.duty_u16(50000) 

# 作为小车向右的函数。
def car_right(): 
  pin1.value(1)
  pin2.duty_u16(50000)  
  pin3.value(0)
  pin4.duty_u16(18000)

# 作为小车停止的函数。
def car_stop():
  pin2.deinit()
  pin4.deinit()
  pin1.value(0)
  pin2.duty_u16(0)  
  pin3.value(0)
  pin4.duty_u16(0)  

while True:
    adcValue1 = adc1.read_u16() # 读取左光敏电阻的ADC值。
    adcValue2 = adc2.read_u16() # 读取右光敏电阻的ADC值。
    print("ADC Value1:", adcValue1 ,"ADC Value2:", adcValue2)
    time.sleep(0.5)
    if adcValue1 > 50000 and adcValue2 > 50000: #由左、右光阻测量的范围值。
        pin2=PWM(Pin(16))
        pin2.freq(50)
        pin4=PWM(Pin(17))
        pin4.freq(50)
        car_forward() #小车前进
    elif adcValue1 > 50000 and adcValue2 <= 50000:
        pin2=PWM(Pin(16))
        pin2.freq(50)
        pin4=PWM(Pin(17))
        pin4.freq(50)
        car_left() #小车向左
    elif adcValue1 <= 50000 and adcValue2 > 50000:
        pin2=PWM(Pin(16))
        pin2.freq(50)
        pin4=PWM(Pin(17))
        pin4.freq(50)
        car_right() #小车向右
    else:
        car_stop() #小车停止