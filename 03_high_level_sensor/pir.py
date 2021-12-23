import RPi.GPIO as GPIO
import time

PIR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

time.sleep(5)
print('PIR Ready...')

try:
    while True:
        inputValue = GPIO.input(PIR_PIN)

        if inputValue == GPIO.HIGH:
            print('움직임 감지')
        else :
            print('움직임 없음')
        
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print('Cleanup and Exit...')