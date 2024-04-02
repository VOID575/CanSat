# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_bma220 import bma220

#i2c = I2C(0, sda=Pin(20, pull=Pin.PULL_UP), scl=Pin(21, pull=Pin.PULL_UP), freq=400000)
i2c = I2C(0, scl=Pin(5, Pin.OUT, Pin.PULL_UP), sda=Pin(4, Pin.OUT, Pin.PULL_UP), freq=1000)

print("I2C Configuration: "+str(i2c)) 
# Correct I2C pins for RP2040
bma = bma220.BMA220(i2c)

while True:
    accx, accy, accz = bma.acceleration
    print(f"x:{accx:.2f}m/s², y:{accy:.2f}m/s², z:{accz:.2f}m/s²")
    time.sleep(0.5)
