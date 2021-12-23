# '도'음 출력 (262Hz)
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 주파수 (262)
pwm = GPIO.PWM(BUZZER_PIN, 523)
pwm.start(50) # duty cycle (0~100) . 소리 크기

time.sleep(1)
pwm.ChangeDutyCycle(0) # 부저음 끄기

pwm.stop()
GPIO.cleanup()
print('cleanup and exit')