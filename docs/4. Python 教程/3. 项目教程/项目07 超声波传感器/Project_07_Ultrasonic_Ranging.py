from machine import Pin 
import time

#定义超声波测距模块的控制引脚。 
trigPin=Pin(10,Pin.OUT,0)
echoPin=Pin(11,Pin.IN,0)
#设置声速。
soundVelocity=340
distance=0

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
    return int(distance)

# 延迟2秒，等待超声波模块稳定;
# 每500毫秒打印从超声波模块获得的数据。
time.sleep_ms(2000)
while True:
    time.sleep_ms(500)
    print('Distance: ',getSonar(),'cm' ) 