# Version : 1.7
# Status : Working
# Author : Christophe Chevallier / Celhryn

import utime
import ujson
from csv_module import *


location = "base"  # set "base" on the Pico W and "cansat" on the classic Pico

# Necessary modules needed to initialize a UART connection
from machine import Pin, UART

# Setting up the UART values
async_receipt = UART(0, 9600)
async_receipt.init(9600, bits=8, parity=None, stop=1)

# File to store received data
csv_file_path_base = "blackbox.csv"

# Main loop
def recevoir():
    # Receiving and processing data
    print(async_receipt.any())
    if async_receipt.any():

        received_data = async_receipt.read().decode('utf-8')  # decode bytes to string
        print("Received:", received_data)

        # Split the received CSV data into individual values
        received_values = received_data.strip().split(",")
        print("Received Values:", received_values)

        if location == "base":
            # Load existing data from the base data file
            date = utime.localtime(utime.time())
            ajouter_valeur(f"{date[0]}/{date[1]}/{date[2]} à {date[3]}h{date[4]}min{date[5]}sec :")
            for i in range(1,5):
                
                ajouter_valeur(received_values[i])
            
            print("Data appended to", csv_file_path_base)

        elif location == "cansat":
            print("Invalid location. Cansat should not store data.")

        else:
            print("Invalid location. Ignoring the received data.")

    utime.sleep(1)
