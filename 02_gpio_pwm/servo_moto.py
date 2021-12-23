import RPi.GPIO as GPIO
import time

SERVO_PIN = 4

GPIO.setup(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

GPIO.PWM(SERVO_PIN, 50)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(7.5)

try:
    while True:
        controlValue = input('1: 0도, 2: -90도, 3: +90도, 9: Exit > ')

        if controlValue == '1':
            pwm.ChangeDutyCycle(7.5) # 0도
        elif controlValue == '2':
            pwm.ChangeDutyCycle(5) # -90도
        elif controlValue == '3':
            pwm.ChangeDutyCycle(10) # +90도
        elif controlValue == '9':
            break 

finally:
    pwm.stop()
    GPIO.cleanup()