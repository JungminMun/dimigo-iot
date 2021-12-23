import RPi.GPIO as GPIO
import time

leds = [4, 5, 6]

GPIO.setmode(GPIO.BCM)
for i in range(3):
    GPIO.setup(leds[i], GPIO.OUT)

for i in leds:
    GPIO.output(i, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(i, GPIO.LOW)

GPIO.cleanup() 