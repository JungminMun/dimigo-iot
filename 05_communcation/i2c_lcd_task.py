# dht11.py
import Adafruit_DHT
from lcd import drivers
import datetime

display = drivers.Lcd()

sensor = Adafruit_DHT.DHT11
DHD_PIN = 14

try:
    while True:
        nowTime = datetime.datetime.now()
        display.lcd_display_string(nowTime.strftime("%x%X"), 1)

        h, t = Adafruit_DHT.read_retry(sensor, DHD_PIN)

        if h is not None and t is not None:
            display.lcd_display_string(( f"{t:.1f}C,{h:.1f}%"), 2)

finally:
    display.lcd_clear()
    print('bye')
