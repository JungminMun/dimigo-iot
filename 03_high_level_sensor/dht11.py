# dht11.py
import Adafruit_DHT

sensor = Adafruit_DHT.DHD11
DHD_PIN = 4

try:
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, DHD_PIN)

        if h is not None and t is not None:
            print('Temperature = %1.f*, Humidity = %1.f%%' %(t, h))

finally:
    print('bye')