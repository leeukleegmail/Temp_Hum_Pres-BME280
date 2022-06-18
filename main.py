from machine import Pin, I2C
import BME280
from utime import sleep


i2c = I2C(scl=Pin(5), sda=Pin(4))
bme = BME280.BME280(i2c=i2c) # addr 118

while True:
    print('Temp:{}'.format(bme.temperature[:-1]))
    print('Hum:{}'.format(bme.humidity[:-1]))
    print('Pres:{}'.format(bme.pressure[:-3]))
    sleep(1)