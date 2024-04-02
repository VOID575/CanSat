from machine import Pin, I2C

# Create a hardware I2C object
# scl and sda are the GPIO numbers where your I2C device is connected

# i2c = I2C(0, scl=Pin(5, Pin.OUT, Pin.PULL_UP), sda=Pin(4, Pin.OUT, Pin.PULL_UP), freq = 1000)
i2c = I2C(0, freq = 40000)

print('I2C SCANNER')
print("I2C Configuration: "+str(i2c))                   # Display I2C config
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print("I2C SCANNER found", len(devices),"devices:")

  for device in devices:
    print("I2C hexadecimal address: ", hex(device))