from machine import Pin,PWM
import time

# 右轮
pin1=Pin(14,Pin.OUT)
pin2=PWM(Pin(16))
pin2.freq(50)
# 左轮
pin3=Pin(15,Pin.OUT)
pin4=PWM(Pin(17))
pin4.freq(50)

# 作为小车前进的函数
def car_forward(): 
  pin1.value(0)
  pin2.duty_u16(50000) 
  pin3.value(0)
  pin4.duty_u16(50000)

# 作为小车后退的函数
def car_back(): 
  pin1.value(1)
  pin2.duty_u16(10000)  
  pin3.value(1)
  pin4.duty_u16(10000)

# 作为小车向左的函数
def car_left(): 
  pin1.value(0)
  pin2.duty_u16(50000)  
  pin3.value(1)
  pin4.duty_u16(32768)

# 作为小车向右的函数
def car_right(): 
  pin1.value(1)
  pin2.duty_u16(32768)  
  pin3.value(0)
  pin4.duty_u16(50000)

# 作为小车停止的函数
def car_stop(): 
  pin1.value(0)
  pin2.duty_u16(0)  
  pin3.value(0)
  pin4.duty_u16(0)    
try:
    while True:
        car_forward() #小车前进
        time.sleep(2) # 延时2s
        car_back() # 小车后退
        time.sleep(2)    
        car_left() # 小车向左
        time.sleep(2)    
        car_right() # 小车向右
        time.sleep(2)    
        car_stop() # 小车停止
        time.sleep(2)     
except:
    pass 