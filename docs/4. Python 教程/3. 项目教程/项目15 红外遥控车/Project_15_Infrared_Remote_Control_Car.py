#导入库
from machine import Pin,I2C,PWM
import time
import json
import matrix_fonts
from ht16k33_matrix import ht16k33_matrix
from irrecvdata import irGetCMD 

recvPin = irGetCMD(6) #将红外解码器与引脚(6)相关联。
'''
#占空比与舵机角度相对应
0°----2.5%----1638
45°----5%----3276
90°----7.5%----4915
135°----10%----6553
180°----12.5%----8192
'''
## 定义GPIO9的输出频率为50Hz，占空比为4915，并将它们分配给PWM。
servoPin = PWM(Pin(9))
servoPin.freq(50)
servoPin.duty_u16(4915)
time.sleep(1)

# 右轮
pin1=Pin(14,Pin.OUT)
pin2=PWM(Pin(16))
pin2.freq(50)
# 左轮
pin3=Pin(15,Pin.OUT)
pin4=PWM(Pin(17))
pin4.freq(50)

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
    
# 作为小车前进的函数。
def car_forward(): 
  pin1.value(0)
  pin2.duty_u16(50000) 
  pin3.value(0)
  pin4.duty_u16(50000)

# 作为小车后退的函数。
def car_back(): 
  pin1.value(1)
  pin2.duty_u16(10000)  
  pin3.value(1)
  pin4.duty_u16(10000)

# 作为小车向左行驶的函数。
def car_left(): 
  pin1.value(0)
  pin2.duty_u16(50000)  
  pin3.value(1)
  pin4.duty_u16(32768)

# 作为小车向右行驶的函数。
def car_right(): 
  pin1.value(1)
  pin2.duty_u16(32768)  
  pin3.value(0)
  pin4.duty_u16(50000)

# 作为小车停车的功能。
def car_stop():
  pin2.deinit()
  pin4.deinit()
  pin1.value(0)
  pin2.duty_u16(0)  
  pin3.value(0)
  pin4.duty_u16(0) 
  
def handleControl(value): 
    if value == '0xff629d':
        pin2=PWM(Pin(16))
        pin2.freq(50)
        pin4=PWM(Pin(17))
        pin4.freq(50)
        car_forward() #小车前进
   # 点阵显示向前图案
        show_char(matrix_fonts.textFont1['^'])
    elif value == '0xffa857':
        pin2=PWM(Pin(16))
        pin2.freq(50)
        pin4=PWM(Pin(17))
        pin4.freq(50)
        car_back() # 小车后退
    # 点阵显示后退图案
        show_char(matrix_fonts.textFont1['v'])
    elif value == '0xff22dd': 
        pin2=PWM(Pin(16))
        pin2.freq(50)
        pin4=PWM(Pin(17))
        pin4.freq(50)
        car_left() # 小车向左
    # 点阵显示向左图案
        show_char(matrix_fonts.textFont1['>'])
    elif value == '0xffc23d': 
        pin2=PWM(Pin(16))
        pin2.freq(50)
        pin4=PWM(Pin(17))
        pin4.freq(50)
        car_right() # 小车向右
    # 点阵显示向右图案
        show_char(matrix_fonts.textFont1['<'])
    elif value == '0xff02fd':
        car_stop() # 小车停止
    # 点阵显示停止图案
        show_char(matrix_fonts.textFont1['!']) 
try:
    while True:
        irValue = recvPin.ir_read() #调用ir_read()读取按下的键的值并将其赋值给IRValue。
        if irValue:
            print(irValue)
            handleControl(irValue)
except:
    pass