# Version : 1.6
# Status : Working
# Author : Christophe Chevallier / Celhryn


import utime
import ujson
from csv_module import dernieres_valeurs

location = "cansat"  # set "base" on the Pico W and "cansat" on the classic Pico
# Necessary modules needed to initialize a UART connection
from machine import Pin, UART
# Setting up the UART values
async_connect = UART(0, 9600)
async_connect.init(9600, bits=8, parity=None, stop=1)

# Simulated sensor data (replace with actual sensor readings)
val = dernieres_valeurs()

time = val[0]
temperature = val[1]
pressure = val[3]
humidity = val[2]
airquality = val[4]
# Data to be sent from the Pico classique (cansat)
data_to_send = {"temps": time,
                "temperature": temperature,
                "pressure": pressure,
                "humidity": humidity,
                "airquality": airquality
                }

def envoi():
    # Main loop
    
    csv_data = ""

    for value in dernieres_valeurs():

        csv_data += str(value) + ","
    
    print("Sending:", csv_data)

    # Convert the data to CSV format and send it
    async_connect.write(csv_data)

    #utime.sleep(1)

"""
csv_data = ""

for value in dernieres_valeurs():

    csv_data += str(value) + ","

#csv_data = 'i' for value in dernieres_valeurs()
print(csv_data)
csv_split = csv_data.strip().split(",")
print(csv_split)
print(csv_split[0])
"""