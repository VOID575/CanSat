import time
import utime
from breakout_bme68x import BreakoutBME68X, STATUS_HEATER_STABLE
from pimoroni_i2c import PimoroniI2C
from csv_module import *
from uartb import envoi

PINS_I2C_BME688 = {"sda": 4, "scl": 5}
i2c = PimoroniI2C(**PINS_I2C_BME688)
#J'associe les les pins de sorties du capteur BME688 à une variable pour pouvoir récupérer les données
bme = BreakoutBME68X(i2c)

while True:
    
    #Définitions des variable, elles renvoient toutes un int équivalent à leur unité de mesure
    temperature, pressure, humidity, gas, status, _, _,= bme.read()
    
    #définition du time stamp
    date = utime.localtime(utime.time())
 
    #J'écris toutes les mesures séparément :
    #D'abord j'écris le time stamp
    ajouter_valeur(f"{date[0]}/{date[1]}/{date[2]} à {date[3]}h{date[4]}min{date[5]}sec :")
    #La température
    ajouter_valeur(f"{round(temperature,2)}c")
    #la pression
    ajouter_valeur(f"{round(pressure,2)}Pa")
    #L'humidité
    ajouter_valeur(f"{round(humidity,2)}%")
    #La quantité de microparticule
    ajouter_valeur(f"{round(gas,2)}Ohms")
    #Je vérifie si le programme ne fait pas plus de 85 lignes pour qu'il ne prenne pas trop de place
    gerer_limitation_valeurs()

    #j'affiche les données dans la console
    print(f"{date[0]}/{date[1]}/{date[2]} à {date[3]}h{date[4]}min{date[5]}sec : {round(temperature,2)}c, {round(pressure,2)}Pa, {round(humidity,2)}%, {round(gas,2)} Ohms\n")

    #Je fais une pause de 1 seconde
    print("Valeurs enregistrées")
    envoi()
    
    time.sleep(1)

    
        
    
    
    

