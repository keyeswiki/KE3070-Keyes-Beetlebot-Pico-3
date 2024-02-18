from machine import Pin, PWM
import time

'''
# 占空比与舵机角度相对应
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

# 设置超声波传感器的引脚和声速
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
  pin2.duty_u16(30000) 
  pin3.value(0)
  pin4.duty_u16(30000)

# 作为小车后退的函数。
def car_back(): 
  pin1.value(1)
  pin2.duty_u16(30000)  
  pin3.value(1)
  pin4.duty_u16(30000)
  
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

while True:
    Distance=getSonar() # 用超声波测量距离。
    print(Distance) # 发送一个脉冲来计算以厘米为单位的距离，并打印结果。
    if Distance<8: # 如果距离小于8
        pin2=PWM(Pin(16))
        pin2.freq(50)
        pin4=PWM(Pin(17))
        pin4.freq(50) 
        car_back() #小车后退
    elif Distance>=8 and Distance<13: # 如果这个距离大于等于8，它就小于13。
        car_stop() # Car stop
    elif Distance>=13 and Distance<35: # 如果这个距离大于等于13，它就小于35。
        pin2=PWM(Pin(16))
        pin2.freq(50)
        pin4=PWM(Pin(17))
        pin4.freq(50)
        car_forward() #小车前进
    else:
       car_stop() #小车后退