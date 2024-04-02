from machine import Pin, I2C
from sh1106 import SH1106_I2C


i2c = I2C(0, freq=400000)
oled = SH1106_I2C(128, 64, i2c)

for i in range(64):
    oled.fill(0)
    oled.text('Hello World!', 0, i, 1)
    oled.show()