#导入Pin, neopiexl和time模块。
import time
from machine import Pin
from neopixel import myNeopixel

#定义连接到新像素的引脚和led的数量。
NUM_LEDS = 4

np = myNeopixel(NUM_LEDS, 13)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
close = (0, 0, 0)
COLORS = [red, green, blue, white, close]

np.brightness(150) #亮度: 0 ~ 255
while True:
    for color in COLORS:
        np.fill(color[0], color[1], color[2])
        np.show()
        time.sleep(0.5)