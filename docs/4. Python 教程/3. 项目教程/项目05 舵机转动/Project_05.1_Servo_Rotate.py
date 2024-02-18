from machine import Pin, PWM
import time

#定义GPIO9的输出频率为50Hz，并将其分配给PWM。
pwm = PWM(Pin(9))
pwm.freq(50)

'''
#占空比与舵机角度相对应
0°----2.5%----1638
45°----5%----3276
90°----7.5%----4915
135°----10%----6553
180°----12.5%----8192
'''
#舵机角度与其占空比相适应。 
angle_0 = 1638
angle_45 = 3276
angle_90 = 4915
angle_135 = 6553
angle_180 = 8192

while True:
    pwm.duty_u16(angle_0)
    time.sleep(1)
    pwm.duty_u16(angle_45)
    time.sleep(1)
    pwm.duty_u16(angle_90)
    time.sleep(1)
    pwm.duty_u16(angle_135)
    time.sleep(1)
    pwm.duty_u16(angle_180)
    time.sleep(1)