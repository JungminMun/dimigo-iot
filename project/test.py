import RPi.GPIO as GPIO # GPIO 모듈
import time # 시간 모듈

# LED pins들 (GPIO)
ledPins = [6, 13, 19, 21]
GPIO.setmode(GPIO.BCM) 
GPIO.setup(ledPins, GPIO.OUT) 

# 7 segment pins GPIO 구성
SEGMENT_PINS =  (11,4,23,8,7,10,18,25)

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

DIGIT_PINS = (22,27,17,24)

for digit in DIGIT_PINS:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)

# 0 ~ 9까지 숫자 구성
data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9

# 표시하는 함수
def display(digit, number): #자릿수, 숫자
    # 자릿수에 해당하는 핀만 LOW로 설정
    for i in range(4): # 0~3
        if i + 1 == digit:
            GPIO.output(DIGIT_PINS[i], GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i], GPIO.HIGH)
    #숫자 출력
    for i in range(7): # 0~6
        GPIO.output(SEGMENT_PINS[i], data[number][i])
    time.sleep(0.001) # 0.1 -> 0.01 -> 0.001


try:
    while True:
        # 현재 시간 불러오기
        nowTime = time.localtime()
        
        # nowTime.tm_hour => 시간
        # nowTime.tm_min => 분
        
        #아침
        if int(nowTime.tm_hour) >= 8 and int(nowTime.tm_hour) <= 11:
            GPIO.output(ledPins[0], 1)
            print("좋은 아침 ~")
        
        #점심
        elif int(nowTime.tm_hour) >= 12 and int(nowTime.tm_hour) <= 16:
            GPIO.output(ledPins[1], 1)
            print("좋은 점심")

        #저녁
        elif int(nowTime.tm_hour) >= 17 and int(nowTime.tm_hour) <= 21:
            GPIO.output(ledPins[2], 1)
            print("좋은 저녁")

        #새벽
        else :
            GPIO.output(ledPins[3], 1)
            print("좋은 새벽")

        display(1, int(nowTime.tm_hour / 10))
        display(2, int(nowTime.tm_hour % 10) )
        display(3, int(nowTime.tm_min / 10))
        display(4, int(nowTime.tm_min % 10) )

finally:
    GPIO.cleanup()
    print('bye')
