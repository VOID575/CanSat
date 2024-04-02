from machine import ADC,Pin
import time

adc0 = ADC(0)
adc1 = ADC(1)
while True:
    
    LM35_bin = adc0.read_u16()
    tmp = (LM35_bin / 2**16) * 3300 / 10.24
    
    anlg_slide = adc1.read_u16()
    
    
    print("dat=", tmp, "C")
    print("Analog slider", anlg_slide)
    
    time.sleep(1)