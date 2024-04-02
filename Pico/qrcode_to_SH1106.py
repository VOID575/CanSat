import machine
from sh1106 import SH1106_I2C

from uQR import QRCode
qr = QRCode()
qr.add_data('https://192.168.1.1')
matrix = qr.get_matrix()


i2c = machine.I2C(0)
screen = SH1106_I2C(128, 64, i2c)
screen.poweron()
for y in range(len(matrix)*2):                   # Scaling the bitmap by 2
    for x in range(len(matrix[0])*2):            # because my screen is tiny.
        value = not matrix[int(y/2)][int(x/2)]   # Inverting the values because
        screen.pixel(x, y, value)                # black is `True` in the matrix.
screen.show()               