import RPi.GPIO as GPIO 

led_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        val = input("1: on, 0: off, 9:exit > ")

        if val == '0':
            GPIO.output(led_pin, GPIO.LOW)
            print("LED OFF")
        elif val == '1':
            GPIO.output(led_pin, GPIO.HIGH)
            print("LED ON")
        elif val == '9':
            GPIO.output(led_pin, GPIO.LOW)
            break

finally:
    GPIO.cleanup()
    print("cleanup")