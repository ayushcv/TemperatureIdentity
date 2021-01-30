#Test code for testing the Temperature sensor.

from smbus import SMBus
from mlx90614 import MLX90614
bus = SMBus(1)
sensor = MLX90614(bus,address=0x5A)
print ("Amb temp", sensor.get_ambient())
print ("obj temp", sensor.get_object_1())
bus.close()

12 - 7 X axis


12 11.5 11 10.5 10 *9.5* 9 8.5 8 7.5 7


11variations