# import module
# 모듈
from os import read
import RPi.GPIO as GPIO
from lcd import drivers

# SPI 통신
import spidev

# open cv & PIL & numpy
import cv2
from PIL import Image
import numpy as np

# ETC
import time



# Setting
# spi 통신 (조도센서)
# SPI 인스턴스 생성
spi = spidev.SpiDev()
# SPI 통신 시작
spi.open(0, 0) #bus : 0, device  : 0 (CE0, CE1)
# SPI 최대 통신 속도 설정
spi.max_speed_hz = 100000

# Switch 부품
GPIO.setmode(GPIO.BCM) # GPIO.BCM or GPIO.BOARD
sw_pin = 17                     
GPIO.setup(sw_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)   

# LCD 부품
display = drivers.Lcd()

# BUZZER 부품
BUZZER_PIN = 12
GPIO.setup(BUZZER_PIN, GPIO.OUT)
pwm = GPIO.PWM(BUZZER_PIN, 262)



#함수
# Module
# analog_read 함수
# 조도센서 analog_read를 위한 함수
def analog_read(channel):
    # [byte_1, byte_2, byte_3]
    # byte_1 : 1
    # byte_2 : channel(0) + 8 = 0000 1000 << 4 -> 1000 0000
    # byte_3 : 0
    ret = spi.xfer2([1, (channel + 8) << 4, 0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

# Photo and Filter
# makeFilter 함수
# ar 카메라와 같은 필터를 만들기 위한 함수
# frame(프레임), filterSize(필터의 크기)
def filteringPicture(frame, filterSize):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.15)
    # NumPy 배열을 Image 객체로 바꿀 때
    background = Image.fromarray(frame)

    # 얼굴 영역에서
    for (x,y,w,h) in faces:
        # 필터의 크기를 조정하는 resize()함수
        # 함수의 반환값을 resized_mask에 받음
        resized_mask = mask.resize((w * filterSize, h * filterSize), Image.ANTIALIAS)

        # 배경에 붙임
        background.paste(resized_mask, (x ,y), mask=resized_mask)

    return np.asarray(background)
# savePhoto 함수
# 사진 저장을 위해 카운트(3초)를 세고, 저장할 시간을 반환하는 함수
def savePhoto():
    for i in reversed(range(3)): 
        print(i + 1)
        pwm.start(50)
        time.sleep(0.7)  
        pwm.stop()
        time.sleep(0.3)

    nowTime = time.strftime("%y%m%d_%H%M%S")

    return nowTime
# darkPhoto 함수
# 사진이 너무 어두울 때 
# 피에조부저가 울린다.                   
def darkPhoto():
    pwm.start(50)
    time.sleep(3)
    pwm.stop()

# display 함수
# 매우 어두울 때
def veryDark():
    display.lcd_display_string("Very Dark", 1)
    darkPhoto()
# 매우 밝을 때
def niceBright():
    display.lcd_display_string("Nice ~ !", 1)


# ETC 
# hello 함수 
# 사용자가 스위치를 눌렀을 때 어떠한 필터를 선택할지 미리 알려주는 함수
def hello():
	print("1. head Ghost")
	print("2. real Ghost")
	print("3. real filter")
# bye 함수
# 나가기를 원할 때 입력을 받는 함수
def bye():
    print('Quit? please input "q"')
    a = input()
    if(a == 'q' or a == 'Q'):
        return True
    else :
        return False



# 실행
try:                                    
    while True: 
        # switch 값을 받아서 출력하기
        switchVar = GPIO.input(sw_pin)

        # if switchVar == 1
        # -> 사용자가 카메라를 open하기 원할 때
        if(switchVar == 1):
            while True:
                # hello 함수를 통하여 옵션들을 안내
                hello()
                # 옵션들에 대한 사용자의 선택 값을 받아옴
                userInput = input()

                # rightGhost 필터를 선택하였을 때
                if(userInput == "1"):
                    maskPath = "rightGhost.png"
                    faceCascade = cv2.CascadeClassifier('face.xml')
                    mask = Image.open(maskPath)

                    # 카메라 열기
                    cap = cv2.VideoCapture(0)
                    while True:
                        # 사진 저장을 위해 반환되는 변수
                        savePhotoswitchVar = GPIO.input(sw_pin)
                        flag, img = cap.read()

                        # filteringPicture의 함수를 통해 필터를 입혀진 사진을 실시간 (imshow)으로 보여주기
                        cv2.imshow('VIDEO', filteringPicture(img, 2))
                        key = cv2.waitKey(1)

                        # 만약에 savePhotoswitchVar == 1 이라면
                        # 즉, 사용자가 사진 저장을 원한다면
                        if (savePhotoswitchVar == 1):
                            # 조도센서 값 읽어오고 출력하기
                            reading = analog_read(0)
                            print("Reading=%d" % reading) # 0~1023

                            # 어두울 때 
                            if(reading < 50):
                                # 디스플래이에 표시
                                # Very Dark
                                veryDark()
                                continue
                            # 밝기가 정상일 때
                            else :
                                # 디스플래이에 표시
                                # Nice
                                niceBright()  

                                # 사진 저장하기                               
                                cv2.imwrite('RightGhostIMG_%s.jpg' %savePhoto(), filteringPicture(img, 2))
                                print('Save !')

                        # 나가기
                        if key == ord('q'):
                            if bye() == True:
                                exit()
                            else :
                                continue

                # RightWhiteGhost를 선택하였을 때
                elif(userInput == "2"):
                    maskPath = "RightWhiteGhost.png"
                    faceCascade = cv2.CascadeClassifier('face.xml')
                    mask = Image.open(maskPath)
                    cap = cv2.VideoCapture(0)

                    while True:
                        # 사진 저장을 위해 반환되는 변수
                        savePhotoswitchVar = GPIO.input(sw_pin)
                        flag, img = cap.read()

                        # filteringPicture의 함수를 통해 필터를 입혀진 사진을 실시간 (imshow)으로 보여주기
                        cv2.imshow('VIDEO', filteringPicture(img, 1))
                        key = cv2.waitKey(1)

                        # 만약에 savePhotoswitchVar == 1 이라면
                        # 즉, 사용자가 사진 저장을 원한다면
                        if (savePhotoswitchVar == 1):
                            # 조도센서 값 읽어오고 출력하기
                            reading = analog_read(0)
                            print("Reading=%d" % reading) # 0~1023

                            # 어두울 때 
                            if(reading < 50):
                                # 디스플래이에 표시
                                # Very Dark
                                veryDark()
                                continue
                            # 밝기가 정상일 때
                            else :
                                # 디스플래이에 표시
                                # Nice
                                niceBright()      

                                # 사진 저장하기                             
                                cv2.imwrite('RightGhostIMG_%s.jpg' %savePhoto(), filteringPicture(img, 2))
                                print('Save !')

                        # 나가기
                        if key == ord('q'):
                            if bye() == True:
                                exit()
                            else :
                                continue

                # puppy를 선택하였을 때
                elif(userInput == "3"):
                    maskPath = "puppy.png"
                    faceCascade = cv2.CascadeClassifier('face.xml')
                    mask = Image.open(maskPath)
                    cap = cv2.VideoCapture(0)

                    while True:
                        # 사진 저장을 위해 반환되는 변수
                        savePhotoswitchVar = GPIO.input(sw_pin)
                        flag, img = cap.read()

                        # filteringPicture의 함수를 통해 필터를 입혀진 사진을 실시간 (imshow)으로 보여주기
                        cv2.imshow('VIDEO', filteringPicture(img, 1))
                        key = cv2.waitKey(1)

                        # 만약에 savePhotoswitchVar == 1 이라면
                        # 즉, 사용자가 사진 저장을 원한다면
                        if (savePhotoswitchVar == 1):
                            # 조도센서 값 읽어오고 출력하기
                            reading = analog_read(0)
                            print("Reading=%d" % reading) # 0~1023

                            # 어두울 때 
                            if(reading < 50):
                                # 디스플래이에 표시
                                # Very Dark
                                veryDark()
                                continue
                            # 밝기가 정상일 때
                            else :
                                # 디스플래이에 표시
                                # Nice
                                niceBright()

                                # 사진 저장하기                                
                                cv2.imwrite('RightGhostIMG_%s.jpg' %savePhoto(), filteringPicture(img, 1))
                                print('Save !')
                                
                        # 나가기
                        if key == ord('q'):
                            if bye() == True:
                                exit()
                            else :
                                continue

finally:
    GPIO.cleanup()                     
    display.lcd_clear()
    spi.close()
    pwm.stop()