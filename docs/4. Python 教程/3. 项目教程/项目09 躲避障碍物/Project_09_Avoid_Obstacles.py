from machine import Pin,I2C,PWM
import time
import json
import matrix_fonts
from ht16k33_matrix import ht16k33_matrix

'''
#占空比与舵机角度相对应
0°----2.5%----1638
45°----5%----3276
90°----7.5%----4915
135°----10%----6553
180°----12.5%----8192
'''
# 定义GPIO9的输出频率为50Hz，占空比为4915，并分配给PWM。
servoPin = PWM(Pin(9))
servoPin.freq(50)
servoPin.duty_u16(4915)
time.sleep(1)

# 设置超声波传感器的引脚和声速。
trigPin=Pin(10,Pin.OUT,0)
echoPin=Pin(11,Pin.IN,0)
soundVelocity=340
distance=0

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
  pin4.duty_u16(40000)

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
    
# 子函数getSonar()用于启动超声波模块开始测量，并返回以厘米为单位的测量距离。
# 在这个函数中，首先让trigPin发送10us高电平启动超声波模块。
# 然后使用pulseIn()读取超声波模块并返回高电平持续时间。
# 最后根据时间计算测得的距离。  
def getSonar(): 
    trigPin.value(1)
    time.sleep_us(10)
    trigPin.value(0)
    while not echoPin.value():
        pass
    pingStart=time.ticks_us()
    while echoPin.value():
        pass
    pingStop=time.ticks_us()
    pingTime=time.ticks_diff(pingStop,pingStart)
    distance=pingTime*soundVelocity//2//10000
    time.sleep_ms(10)
    return int(distance)

## 制作图案的工具 https://gurgleapps.com/tools/matrix
#i2c配置
clock_pin = 21
data_pin = 20
bus = 0
i2c_addr_left = 0x70
use_i2c = True

def scan_for_devices():
    i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))
    devices = i2c.scan()
    if devices:
        for d in devices:
            print(hex(d))
    else:
        print('no i2c devices')

if use_i2c:
    scan_for_devices()
    left_eye = ht16k33_matrix(data_pin, clock_pin, bus, i2c_addr_left)

def show_char(left):
    if use_i2c:
        left_eye.show_char(left)
        
while True:
    Distance=getSonar() # 用超声波测量距离。
    if Distance>0 and Distance<10: # 如果距离大于0，它就小于10。
        car_stop() # 小车停止
        show_char(matrix_fonts.textFont1['!']) # 显示标点符号!
        time.sleep(0.2)
        servoPin.duty_u16(8192)
        time.sleep(0.3)
        a1=getSonar()
        time.sleep(0.2)
        servoPin.duty_u16(1638)
        time.sleep(0.3)
        a2=getSonar()
        time.sleep(0.2)
        if a1>a2:
            pin2=PWM(Pin(16))
            pin2.freq(50)
            pin4=PWM(Pin(17))
            pin4.freq(50)
            car_left()
            show_char(matrix_fonts.textFont1['>'])
            servoPin.duty_u16(4915)
            time.sleep(0.3)
            show_char(matrix_fonts.textFont1['^'])
        else:
            pin2=PWM(Pin(16))
            pin2.freq(50)
            pin4=PWM(Pin(17))
            pin4.freq(50)
            car_right()
            show_char(matrix_fonts.textFont1['<'])
            servoPin.duty_u16(4915)
            time.sleep(0.3)
            show_char(matrix_fonts.textFont1['^'])
    else:
        pin2=PWM(Pin(16))
        pin2.freq(50)
        pin4=PWM(Pin(17))
        pin4.freq(50)
        car_forward() #小车前进
        show_char(matrix_fonts.textFont1['^'])