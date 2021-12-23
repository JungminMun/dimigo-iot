import RPi.GPIO as GPIO
import time

ledPin = 4
GPIO.setmode(GPIO.BCM) # GPIO.BCM or GPIO.BOARD
GPIO.setup(ledPin, GPIO.OUT) # GPIO.OUT or GIPo.in

for i in range(10):
    GPIO.output(ledPin, GPIO.HIGH) # 1
    print("LED ON")
    time.sleep(1)
    GPIO.output(ledPin, GPIO.LOW) # 0
    print("LED OFF")
    time.sleep(1)

GPIO.cleanup()