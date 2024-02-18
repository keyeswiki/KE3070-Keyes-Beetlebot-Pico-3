from machine import Pin, PWM
import time

#定义GPIO9的输出频率为50Hz，占空比为4915，并分配给PWM。
servoPin = PWM(Pin(9))
servoPin.freq(50)
servoPin.duty_u16(4915)
time.sleep(1)

#设置循迹传感器的引脚
tracking_left = Pin(7, Pin.IN)
tracking_right = Pin(8, Pin.IN)

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
  pin2.duty_u16(20000) 
  pin3.value(0)
  pin4.duty_u16(20000) 

# 作为小车向左的函数。
def car_left(): 
  pin1.value(0)
  pin2.duty_u16(20000)  
  pin3.value(1)
  pin4.duty_u16(4000) 

# 作为小车向右的函数。
def car_right(): 
  pin1.value(1)
  pin2.duty_u16(40000)  
  pin3.value(0)
  pin4.duty_u16(20000)

# 作为小车停止的函数。
def car_stop():
  pin2.deinit()
  pin4.deinit()
  pin1.value(0)
  pin2.duty_u16(0)  
  pin3.value(0)
  pin4.duty_u16(0)

while True:
    L_value = tracking_left.value() #左红外跟踪值赋给变量L_value。
    R_value = tracking_right.value() #右红外跟踪值赋给变量R_value。
    if L_value == 1 and R_value == 1: #左右红外跟踪均检测到黑线。
        pin2=PWM(Pin(16))
        pin2.freq(50)
        pin4=PWM(Pin(17))
        pin4.freq(50) 
        car_forward() #小车前进
    elif L_value == 1 and R_value == 0:
        pin2=PWM(Pin(16))
        pin2.freq(50)
        pin4=PWM(Pin(17))
        pin4.freq(50) 
        car_left() #小车向左
    elif L_value == 0 and R_value == 1:
        pin2=PWM(Pin(16))
        pin2.freq(50)
        pin4=PWM(Pin(17))
        pin4.freq(50) 
        car_right() #小车向右
    else:
        car_stop() #小车停止